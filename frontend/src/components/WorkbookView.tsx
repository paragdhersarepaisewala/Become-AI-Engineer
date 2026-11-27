import React, { useEffect, useState } from 'react';
import {
  AlertCircle,
  CheckCircle2,
  Eye,
  Lightbulb,
  Play,
  RotateCcw,
  Terminal,
  XCircle,
} from 'lucide-react';
import { api } from '../api';
import type {
  ChapterSummary,
  RunResult,
  WorkbookDetail,
  WorkbookStatus,
  WorkbookSummary,
} from '../types';
import { MarkdownBlock } from './MarkdownBlock';

interface Props {
  chapters: ChapterSummary[];
  initialChapterFilter?: string;
  initialProblemId?: string;
  onProgressChanged: () => void;
}

const STATUS_BADGE: Record<WorkbookStatus, { label: string; cls: string }> = {
  todo: { label: 'Todo', cls: 'tag' },
  struggled: { label: 'Needs Review', cls: 'tag tag-rose' },
  solved_with_hints: { label: 'Solved w/ Hints', cls: 'tag tag-amber' },
  mastered: { label: 'Mastered', cls: 'tag tag-green' },
};

export const WorkbookView: React.FC<Props> = ({
  chapters,
  initialChapterFilter = '',
  initialProblemId = '',
  onProgressChanged,
}) => {
  const [problems, setProblems] = useState<WorkbookSummary[]>([]);
  const [chapterFilter, setChapterFilter] = useState(initialChapterFilter);
  const [topicFilter, setTopicFilter] = useState('');
  const [selectedId, setSelectedId] = useState(initialProblemId);
  const [detail, setDetail] = useState<WorkbookDetail | null>(null);
  const [code, setCode] = useState('');
  const [revealedHints, setRevealedHints] = useState(0);
  const [showTrace, setShowTrace] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const [running, setRunning] = useState(false);
  const [runResult, setRunResult] = useState<RunResult | null>(null);

  useEffect(() => {
    setChapterFilter(initialChapterFilter);
  }, [initialChapterFilter]);

  useEffect(() => {
    if (initialProblemId) setSelectedId(initialProblemId);
  }, [initialProblemId]);

  const loadList = async () => {
    const list = await api.getWorkbook({
      chapter_id: chapterFilter || undefined,
      topic: topicFilter || undefined,
    });
    setProblems(list);
    if (list.length > 0 && !list.some((p) => p.id === selectedId)) {
      setSelectedId(list[0].id);
    }
  };

  useEffect(() => {
    loadList();
  }, [chapterFilter, topicFilter]);

  useEffect(() => {
    if (!selectedId) return;
    let active = true;
    api.getProblem(selectedId).then((res) => {
      if (!active) return;
      setDetail(res);
      setCode(res.progress.last_code || res.starter_code);
      setRevealedHints(res.progress.hints_used || 0);
      setShowTrace(false);
      setShowSolution(false);
      setRunResult(null);
    });
    return () => {
      active = false;
    };
  }, [selectedId]);

  const allTopics = Array.from(new Set(problems.map((p) => p.topic)));

  const handleRevealHint = async () => {
    if (!detail) return;
    const next = Math.min(detail.hints.length, revealedHints + 1);
    setRevealedHints(next);
    const prog = await api.updateProblemProgress(detail.id, { hints_used: next });
    setDetail({ ...detail, progress: prog });
  };

  const handleRun = async (mode: 'scratch' | 'test') => {
    if (!detail) return;
    setRunning(true);
    try {
      const res = await api.runCode({ problem_id: detail.id, code, mode });
      setRunResult(res);
      if (res.progress) {
        setDetail({ ...detail, progress: res.progress });
      }
      await loadList();
      onProgressChanged();
    } finally {
      setRunning(false);
    }
  };

  const handleStatusChange = async (status: WorkbookStatus) => {
    if (!detail) return;
    const prog = await api.updateProblemProgress(detail.id, { status, last_code: code });
    setDetail({ ...detail, progress: prog });
    await loadList();
    onProgressChanged();
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const target = e.currentTarget;
      const start = target.selectionStart;
      const end = target.selectionEnd;
      const updated = code.slice(0, start) + '    ' + code.slice(end);
      setCode(updated);
      requestAnimationFrame(() => {
        target.selectionStart = target.selectionEnd = start + 4;
      });
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* Filter Bar */}
      <div className="card" style={{ display: 'flex', flexWrap: 'wrap', gap: '0.75rem', alignItems: 'center', justifyContent: 'space-between', padding: '0.85rem 1.1rem' }}>
        <div>
          <strong style={{ fontSize: '1rem' }}>Separate Practice Workbook</strong>
          <span className="muted" style={{ marginLeft: '0.65rem' }}>
            Questions, Thinking Blueprints, Dry-Run Traces, Answers & Automated Python Verification
          </span>
        </div>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          <select className="input-control" value={chapterFilter} onChange={(e) => setChapterFilter(e.target.value)}>
            <option value="">All Chapters</option>
            {chapters
              .filter((c) => c.status_type === 'available')
              .map((c) => (
                <option key={c.id} value={c.id}>
                  Ch {c.number}: {c.title.slice(0, 28)}
                </option>
              ))}
          </select>
          <select className="input-control" value={topicFilter} onChange={(e) => setTopicFilter(e.target.value)}>
            <option value="">All Topics</option>
            {allTopics.map((t) => (
              <option key={t} value={t}>{t}</option>
            ))}
          </select>
        </div>
      </div>

      {/* 3-Column Workbook Layout */}
      <div className="workbook-split">
        {/* Column 1: Problem List */}
        <div className="sidebar-list">
          {problems.map((p) => {
            const badge = STATUS_BADGE[p.progress.status];
            return (
              <button
                key={p.id}
                className={`sidebar-item ${p.id === selectedId ? 'active' : ''}`}
                onClick={() => setSelectedId(p.id)}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                  <span style={{ fontSize: '0.75rem', color: 'var(--accent)', fontWeight: 700 }}>
                    #{p.number} · {p.topic}
                  </span>
                  <span className={badge.cls} style={{ fontSize: '0.68rem' }}>{badge.label}</span>
                </div>
                <div style={{ fontWeight: 600, fontSize: '0.88rem' }}>{p.title}</div>
                <div className="muted" style={{ fontSize: '0.76rem', marginTop: 2 }}>{p.difficulty}</div>
              </button>
            );
          })}
        </div>

        {/* Column 2: Problem Statement, Thinking Blueprint, Hints, Trace & Solution */}
        {!detail ? (
          <div className="card">Select a problem from the left.</div>
        ) : (
          <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem', maxHeight: 'calc(100vh - 180px)', overflowY: 'auto' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '0.5rem' }}>
              <div>
                <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap', marginBottom: '0.35rem' }}>
                  <span className="tag tag-accent">{detail.topic}</span>
                  <span className="tag">{detail.question_type}</span>
                  <span className="tag tag-purple">{detail.difficulty}</span>
                </div>
                <h3 style={{ fontSize: '1.2rem' }}>{detail.number} {detail.title}</h3>
              </div>
              <select
                className="input-control"
                value={detail.progress.status}
                onChange={(e) => handleStatusChange(e.target.value as WorkbookStatus)}
              >
                <option value="todo">Todo</option>
                <option value="struggled">Needs Review</option>
                <option value="solved_with_hints">Solved w/ Hints</option>
                <option value="mastered">Mastered</option>
              </select>
            </div>

            <MarkdownBlock content={detail.prompt_markdown} />

            {/* Thinking Blueprint */}
            <div style={{ background: 'var(--bg-elevated)', padding: '0.75rem 0.9rem', borderRadius: 10, border: '1px solid var(--border)' }}>
              <div style={{ fontWeight: 700, fontSize: '0.86rem', color: 'var(--accent)', marginBottom: '0.35rem' }}>
                Logic Thinking Blueprint (Plan Before Coding)
              </div>
              <ol style={{ margin: 0, paddingLeft: '1.25rem', fontSize: '0.86rem' }}>
                {detail.thinking_blueprint.map((step, i) => (
                  <li key={i} style={{ marginBottom: 3 }}>{step}</li>
                ))}
              </ol>
            </div>

            {/* Progressive Hints */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.45rem' }}>
              <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                {revealedHints < detail.hints.length && (
                  <button className="btn" onClick={handleRevealHint}>
                    <Lightbulb size={15} color="var(--amber)" /> Reveal Hint ({revealedHints}/{detail.hints.length})
                  </button>
                )}
                <button className="btn" onClick={() => setShowTrace((s) => !s)}>
                  <Eye size={15} /> {showTrace ? 'Hide' : 'Show'} Dry-Run Trace
                </button>
                <button className="btn" onClick={() => setShowSolution((s) => !s)}>
                  <Eye size={15} color="var(--green)" /> {showSolution ? 'Hide' : 'Show'} Answer & Explanation
                </button>
              </div>

              {revealedHints > 0 && (
                <div className="callout">
                  <strong>Hints:</strong>
                  <ol style={{ margin: '0.35rem 0 0', paddingLeft: '1.2rem' }}>
                    {detail.hints.slice(0, revealedHints).map((h, i) => (
                      <li key={i}>{h}</li>
                    ))}
                  </ol>
                </div>
              )}

              {showTrace && (
                <div style={{ background: 'var(--bg-elevated)', padding: '0.75rem', borderRadius: 10, border: '1px solid var(--border)' }}>
                  <div style={{ fontWeight: 700, fontSize: '0.85rem', color: 'var(--purple)', marginBottom: 4 }}>Dry-Run Trace Table</div>
                  <MarkdownBlock content={detail.dry_run_trace} />
                </div>
              )}

              {showSolution && (
                <div style={{ background: 'var(--bg-elevated)', padding: '0.85rem', borderRadius: 10, border: '1px solid var(--green)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                    <strong style={{ color: 'var(--green)', fontSize: '0.9rem' }}>Reference Answer & Explanation</strong>
                    <button className="btn" style={{ padding: '0.25rem 0.6rem', fontSize: '0.76rem' }} onClick={() => setCode(detail.solution_code)}>
                      Copy to Editor
                    </button>
                  </div>
                  <pre className="code-block">{detail.solution_code}</pre>
                  <MarkdownBlock content={detail.explanation_markdown} />
                </div>
              )}
            </div>
          </div>
        )}

        {/* Column 3: Live Python Editor & Test Runner */}
        {detail && (
          <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem' }}>
              <span className="muted" style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem' }}>
                solution.py · Attempts: {detail.progress.attempts}
              </span>
              <div style={{ display: 'flex', gap: '0.45rem' }}>
                <button className="btn" onClick={() => setCode(detail.starter_code)} title="Reset Starter">
                  <RotateCcw size={14} /> Reset
                </button>
                <button className="btn" disabled={running} onClick={() => handleRun('scratch')}>
                  <Play size={14} /> Run Code
                </button>
                <button className="btn btn-primary" disabled={running} onClick={() => handleRun('test')}>
                  <CheckCircle2 size={14} /> {running ? 'Running...' : 'Verify Tests'}
                </button>
              </div>
            </div>

            <textarea
              className="code-editor"
              spellCheck={false}
              value={code}
              onChange={(e) => setCode(e.target.value)}
              onKeyDown={handleKeyDown}
            />

            {runResult && (
              <div style={{ background: 'var(--bg-code)', border: `1px solid ${runResult.ok ? 'var(--green)' : 'var(--rose)'}`, borderRadius: 10, padding: '0.8rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.45rem' }}>
                  <strong style={{ color: runResult.ok ? 'var(--green)' : 'var(--rose)', display: 'flex', alignItems: 'center', gap: 6 }}>
                    {runResult.ok ? <CheckCircle2 size={16} /> : <AlertCircle size={16} />}
                    {runResult.total_count > 0
                      ? `${runResult.passed_count}/${runResult.total_count} Tests Passed`
                      : runResult.ok
                      ? 'Executed Cleanly'
                      : 'Execution Error'}
                  </strong>
                  <span className="muted" style={{ fontSize: '0.78rem' }}>{runResult.elapsed_ms} ms</span>
                </div>

                {runResult.test_results.length > 0 && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.35rem', marginBottom: '0.5rem' }}>
                    {runResult.test_results.map((tr, i) => (
                      <div key={i} style={{ fontSize: '0.82rem', fontFamily: 'var(--font-mono)', display: 'flex', flexDirection: 'column', gap: 2 }}>
                        <span style={{ color: tr.passed ? 'var(--green)' : 'var(--rose)', display: 'flex', alignItems: 'center', gap: 5 }}>
                          {tr.passed ? <CheckCircle2 size={13} /> : <XCircle size={13} />} {tr.name}
                        </span>
                        {!tr.passed && tr.error && (
                          <pre style={{ margin: '2px 0 0 18px', fontSize: '0.75rem', color: 'var(--rose)', whiteSpace: 'pre-wrap' }}>{tr.error}</pre>
                        )}
                      </div>
                    ))}
                  </div>
                )}

                {(runResult.total_count === 0 || runResult.stdout) && (
                  <div style={{ marginTop: 6 }}>
                    <div className="muted" style={{ fontSize: '0.76rem', display: 'flex', alignItems: 'center', gap: 4 }}>
                      <Terminal size={12} /> Output (stdout)
                    </div>
                    <pre style={{ margin: '4px 0 0', fontSize: '0.82rem', fontFamily: 'var(--font-mono)', whiteSpace: 'pre-wrap', color: runResult.stdout ? 'var(--text)' : 'var(--text-muted)' }}>
                      {runResult.stdout ? runResult.stdout : '(no printed output — add a print(...) line at the bottom to see values here, or click "Verify Tests")'}
                    </pre>
                  </div>
                )}

                {runResult.stderr && (
                  <pre style={{ margin: '6px 0 0', fontSize: '0.78rem', color: 'var(--rose)', whiteSpace: 'pre-wrap' }}>
                    {runResult.stderr}
                  </pre>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
