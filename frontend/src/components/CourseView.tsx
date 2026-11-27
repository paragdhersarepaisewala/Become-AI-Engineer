import React, { useEffect, useState } from 'react';
import { CheckCircle2, Circle, Code2, FileText, FolderKanban, Play, Save, Terminal } from 'lucide-react';
import { api } from '../api';
import type { ChapterDetail, ChapterStatus, ChapterSummary, RunResult } from '../types';
import { MarkdownBlock } from './MarkdownBlock';
import {
  AsyncioLoopVisualizer,
  DPTableVisualizer,
  NumpyBroadcastVisualizer,
  RecursionStackVisualizer,
} from './Visualizers';

interface Props {
  chapters: ChapterSummary[];
  selectedChapterId: string;
  onSelectChapter: (id: string) => void;
  onProgressChanged: () => void;
  onJumpToWorkbook: (chapterId: string) => void;
}

export const CourseView: React.FC<Props> = ({
  chapters,
  selectedChapterId,
  onSelectChapter,
  onProgressChanged,
  onJumpToWorkbook,
}) => {
  const [detail, setDetail] = useState<ChapterDetail | null>(null);
  const [notes, setNotes] = useState('');
  const [savingNotes, setSavingNotes] = useState(false);
  const [snippetOutputs, setSnippetOutputs] = useState<Record<string, RunResult>>({});
  const [runningSnippet, setRunningSnippet] = useState<string | null>(null);

  const runSnippet = async (key: string, snippetCode: string) => {
    setRunningSnippet(key);
    try {
      const res = await api.runCode({ code: snippetCode, mode: 'scratch' });
      setSnippetOutputs((prev) => ({ ...prev, [key]: res }));
    } finally {
      setRunningSnippet(null);
    }
  };

  useEffect(() => {
    let active = true;
    api.getChapter(selectedChapterId).then((res) => {
      if (active) {
        setDetail(res);
        setNotes(res.progress.notes || '');
      }
    });
    return () => {
      active = false;
    };
  }, [selectedChapterId]);

  const updateProgress = async (payload: {
    status?: ChapterStatus;
    completed_sections?: string[];
    completed_milestones?: string[];
    quiz_answers?: Record<string, number>;
    notes?: string;
  }) => {
    if (!detail) return;
    const updated = await api.updateChapterProgress(detail.id, payload);
    setDetail({ ...detail, progress: updated });
    onProgressChanged();
  };

  const toggleSection = (sectionId: string) => {
    if (!detail) return;
    const set = new Set(detail.progress.completed_sections);
    if (set.has(sectionId)) set.delete(sectionId);
    else set.add(sectionId);
    const next = Array.from(set);
    const allDone = detail.sections.length > 0 && next.length === detail.sections.length;
    const nextStatus: ChapterStatus = allDone
      ? 'completed'
      : next.length > 0
      ? 'in_progress'
      : detail.progress.status;
    updateProgress({ completed_sections: next, status: nextStatus });
  };

  const toggleMilestone = (milestoneId: string) => {
    if (!detail) return;
    const set = new Set(detail.progress.completed_milestones);
    if (set.has(milestoneId)) set.delete(milestoneId);
    else set.add(milestoneId);
    updateProgress({ completed_milestones: Array.from(set) });
  };

  const answerQuiz = (quizId: string, optionIdx: number) => {
    if (!detail) return;
    updateProgress({
      quiz_answers: { ...detail.progress.quiz_answers, [quizId]: optionIdx },
    });
  };

  return (
    <div className="split-layout">
      {/* Left Chapter Navigator */}
      <div className="sidebar-list">
        {chapters.map((ch) => (
          <button
            key={ch.id}
            className={`sidebar-item ${ch.id === selectedChapterId ? 'active' : ''}`}
            onClick={() => onSelectChapter(ch.id)}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 3 }}>
              <span style={{ fontSize: '0.76rem', color: 'var(--accent)', fontWeight: 700 }}>
                CHAPTER {ch.number}
              </span>
              {ch.status_type === 'roadmap' ? (
                <span className="tag tag-purple" style={{ fontSize: '0.68rem' }}>Roadmap</span>
              ) : ch.progress.status === 'completed' ? (
                <CheckCircle2 size={14} color="var(--green)" />
              ) : ch.progress.status === 'in_progress' ? (
                <span className="tag tag-amber" style={{ fontSize: '0.68rem' }}>Active</span>
              ) : null}
            </div>
            <div style={{ fontWeight: 600, fontSize: '0.88rem' }}>{ch.title}</div>
          </button>
        ))}
      </div>

      {/* Main Reader */}
      {!detail ? (
        <div className="card">Loading chapter...</div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.1rem' }}>
          <div className="card">
            <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', gap: '0.75rem', alignItems: 'flex-start' }}>
              <div>
                <div className="muted" style={{ fontWeight: 600, color: 'var(--accent)' }}>{detail.phase_title}</div>
                <h2 style={{ fontSize: '1.5rem', marginTop: '0.2rem' }}>
                  Chapter {detail.number}: {detail.title}
                </h2>
                <p className="muted" style={{ marginTop: '0.3rem' }}>{detail.subtitle}</p>
              </div>
              {detail.status_type === 'available' && (
                <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
                  <select
                    className="input-control"
                    value={detail.progress.status}
                    onChange={(e) => updateProgress({ status: e.target.value as ChapterStatus })}
                  >
                    <option value="not_started">Not Started</option>
                    <option value="in_progress">In Progress</option>
                    <option value="completed">Completed</option>
                  </select>
                  {detail.workbook_problem_ids.length > 0 && (
                    <button className="btn btn-primary" onClick={() => onJumpToWorkbook(detail.id)}>
                      <Code2 size={15} /> Practice Drills ({detail.workbook_problem_ids.length})
                    </button>
                  )}
                </div>
              )}
            </div>

            <div className="callout" style={{ borderLeftColor: 'var(--accent)', background: 'var(--accent-soft)', marginTop: '0.9rem' }}>
              <strong>Why It Matters:</strong> {detail.why_it_matters}
            </div>

            <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap', marginTop: '0.6rem' }}>
              {detail.just_in_time_tags.map((t) => (
                <span key={t} className="tag">{t}</span>
              ))}
            </div>
          </div>

          {detail.status_type === 'roadmap' ? (
            <div className="card">
              <h3>Phase 3–4 Roadmap Preview</h3>
              <p className="muted" style={{ marginTop: '0.4rem' }}>
                This chapter is part of Phase 3–4 (ML, PyTorch, Transformers, Training Small LLMs, QLoRA Fine-Tuning & LangChain).
                Complete Phase 1–2 first so every tensor, autograd graph, and LangChain runnable makes effortless sense—then expand Phase 3–4 next!
              </p>
              {detail.project && (
                <div style={{ marginTop: '0.85rem' }}>
                  <strong>Planned Project:</strong> {detail.project.title} (<code className="inline-code">{detail.project.workspace_dir}</code>)
                </div>
              )}
            </div>
          ) : (
            <>
              {/* Lesson Sections */}
              {detail.sections.map((sec) => {
                const done = detail.progress.completed_sections.includes(sec.id);
                return (
                  <div key={sec.id} className="card">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.75rem', marginBottom: '0.65rem' }}>
                      <h3 style={{ fontSize: '1.15rem' }}>{sec.title}</h3>
                      <button
                        className={`btn ${done ? 'btn-success' : ''}`}
                        onClick={() => toggleSection(sec.id)}
                      >
                        {done ? <CheckCircle2 size={15} /> : <Circle size={15} />}
                        {done ? 'Understood' : 'Mark Done'}
                      </button>
                    </div>

                    {sec.zero_assumption_note && (
                      <div className="callout">
                        <strong>Before You Start:</strong> {sec.zero_assumption_note}
                      </div>
                    )}

                    {sec.definition && (
                      <div style={{ background: 'var(--bg-elevated)', border: '1px solid var(--border)', borderRadius: 10, padding: '0.75rem 0.95rem', marginBottom: '0.75rem' }}>
                        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: 4 }}>
                          1. Definition (What Is It?)
                        </div>
                        <div style={{ fontSize: '0.94rem' }}>{sec.definition}</div>
                      </div>
                    )}

                    {sec.syntax_box && (
                      <div style={{ background: 'var(--bg-elevated)', border: '1px solid var(--border)', borderRadius: 10, padding: '0.75rem 0.95rem', marginBottom: '0.75rem' }}>
                        <div style={{ fontSize: '0.78rem', fontWeight: 700, color: 'var(--purple)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: 4 }}>
                          2. Exact Syntax — {sec.syntax_box.title}
                        </div>
                        <pre className="code-block" style={{ margin: '0.4rem 0' }}>{sec.syntax_box.syntax}</pre>
                        <ul style={{ margin: '0.4rem 0 0', paddingLeft: '1.25rem', fontSize: '0.88rem' }}>
                          {sec.syntax_box.breakdown.map((b, bi) => (
                            <li key={bi} style={{ marginBottom: 3 }}>{b}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {sec.tiny_example && (
                      <div style={{ background: 'var(--bg-elevated)', border: '1px solid var(--border)', borderRadius: 10, padding: '0.75rem 0.95rem', marginBottom: '0.75rem' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.5rem', marginBottom: 4 }}>
                          <div style={{ fontSize: '0.78rem', fontWeight: 700, color: 'var(--green)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                            3. Tiny Example (Line-by-Line) — {sec.tiny_example.title}
                          </div>
                          <button
                            className="btn"
                            style={{ padding: '0.25rem 0.6rem', fontSize: '0.76rem' }}
                            disabled={runningSnippet === `${sec.id}-tiny`}
                            onClick={() => runSnippet(`${sec.id}-tiny`, sec.tiny_example!.code)}
                          >
                            <Play size={12} /> {runningSnippet === `${sec.id}-tiny` ? 'Running...' : 'Run Code'}
                          </button>
                        </div>
                        <pre className="code-block" style={{ margin: '0.4rem 0' }}>{sec.tiny_example.code}</pre>
                        {snippetOutputs[`${sec.id}-tiny`] && (
                          <div style={{ background: 'var(--bg-code)', border: '1px solid var(--border-bright)', borderRadius: 8, padding: '0.55rem 0.75rem', marginBottom: '0.5rem' }}>
                            <div className="muted" style={{ fontSize: '0.74rem', display: 'flex', alignItems: 'center', gap: 4 }}>
                              <Terminal size={12} /> Output ({snippetOutputs[`${sec.id}-tiny`].elapsed_ms} ms)
                            </div>
                            <pre style={{ margin: '4px 0 0', fontFamily: 'var(--font-mono)', fontSize: '0.8rem', whiteSpace: 'pre-wrap', color: snippetOutputs[`${sec.id}-tiny`].stderr ? 'var(--rose)' : 'var(--green)' }}>
                              {snippetOutputs[`${sec.id}-tiny`].stderr || snippetOutputs[`${sec.id}-tiny`].stdout || '(no printed output)'}
                            </pre>
                          </div>
                        )}
                        <ol style={{ margin: '0.4rem 0 0', paddingLeft: '1.25rem', fontSize: '0.88rem' }}>
                          {sec.tiny_example.line_by_line.map((line, li) => (
                            <li key={li} style={{ marginBottom: 3 }}>{line}</li>
                          ))}
                        </ol>
                      </div>
                    )}

                    <MarkdownBlock content={sec.body_markdown} />

                    {sec.code_example && (
                      <div style={{ marginTop: '0.75rem' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.5rem' }}>
                          <div className="muted" style={{ fontWeight: 600 }}>4. Practical Example — {sec.code_example.title}</div>
                          <button
                            className="btn"
                            style={{ padding: '0.25rem 0.6rem', fontSize: '0.76rem' }}
                            disabled={runningSnippet === `${sec.id}-main`}
                            onClick={() => runSnippet(`${sec.id}-main`, sec.code_example!.code)}
                          >
                            <Play size={12} /> {runningSnippet === `${sec.id}-main` ? 'Running...' : 'Run Code'}
                          </button>
                        </div>
                        <pre className="code-block">{sec.code_example.code}</pre>
                        {snippetOutputs[`${sec.id}-main`] && (
                          <div style={{ background: 'var(--bg-code)', border: '1px solid var(--border-bright)', borderRadius: 8, padding: '0.55rem 0.75rem', marginBottom: '0.5rem' }}>
                            <div className="muted" style={{ fontSize: '0.74rem', display: 'flex', alignItems: 'center', gap: 4 }}>
                              <Terminal size={12} /> Output ({snippetOutputs[`${sec.id}-main`].elapsed_ms} ms)
                            </div>
                            <pre style={{ margin: '4px 0 0', fontFamily: 'var(--font-mono)', fontSize: '0.8rem', whiteSpace: 'pre-wrap', color: snippetOutputs[`${sec.id}-main`].stderr ? 'var(--rose)' : 'var(--green)' }}>
                              {snippetOutputs[`${sec.id}-main`].stderr || snippetOutputs[`${sec.id}-main`].stdout || '(no printed output)'}
                            </pre>
                          </div>
                        )}
                      </div>
                    )}

                    {sec.common_mistakes && sec.common_mistakes.length > 0 && (
                      <div className="callout" style={{ borderLeftColor: 'var(--rose)', background: 'var(--rose-soft)', marginTop: '0.75rem' }}>
                        <strong>Common Mistakes to Avoid:</strong>
                        <ul style={{ margin: '0.35rem 0 0', paddingLeft: '1.2rem' }}>
                          {sec.common_mistakes.map((m, mi) => (
                            <li key={mi}>{m}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    <div className="takeaway">
                      <strong>Key Takeaway:</strong> {sec.key_takeaway}
                    </div>
                  </div>
                );
              })}

              {/* Interactive Visualizer */}
              {detail.visualizer === 'recursion_stack' && <RecursionStackVisualizer />}
              {detail.visualizer === 'dp_table' && <DPTableVisualizer />}
              {detail.visualizer === 'asyncio_loop' && <AsyncioLoopVisualizer />}
              {detail.visualizer === 'numpy_broadcast' && <NumpyBroadcastVisualizer />}

              {/* Concept Check Quizzes */}
              {detail.quizzes.length > 0 && (
                <div className="card">
                  <h3 style={{ marginBottom: '0.85rem' }}>Quick Concept Check</h3>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                    {detail.quizzes.map((q) => {
                      const chosen = detail.progress.quiz_answers[q.id];
                      const answered = chosen !== undefined;
                      const isCorrect = chosen === q.correct_index;
                      return (
                        <div key={q.id} style={{ padding: '0.85rem', borderRadius: 10, background: 'var(--bg-elevated)', border: '1px solid var(--border)' }}>
                          <div style={{ fontWeight: 600, marginBottom: '0.55rem' }}>{q.question}</div>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
                            {q.options.map((opt, idx) => {
                              const selected = chosen === idx;
                              const right = idx === q.correct_index;
                              let borderColor = 'var(--border)';
                              if (answered && selected) borderColor = right ? 'var(--green)' : 'var(--rose)';
                              else if (answered && right) borderColor = 'var(--green)';
                              return (
                                <button
                                  key={idx}
                                  className="sidebar-item"
                                  style={{ borderColor, padding: '0.5rem 0.75rem', fontSize: '0.86rem' }}
                                  onClick={() => answerQuiz(q.id, idx)}
                                >
                                  {opt}
                                </button>
                              );
                            })}
                          </div>
                          {answered && (
                            <div style={{ marginTop: '0.55rem', fontSize: '0.84rem', color: isCorrect ? 'var(--green)' : 'var(--amber)' }}>
                              {isCorrect ? '✓ Correct! ' : 'Not quite — '} {q.explanation}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}

              {/* Chapter Project Checklist */}
              {detail.project && (
                <div className="card">
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem' }}>
                    <h3 style={{ display: 'flex', alignItems: 'center', gap: '0.45rem' }}>
                      <FolderKanban size={18} color="var(--accent)" /> Hands-On Project: {detail.project.title}
                    </h3>
                    <code className="inline-code">{detail.project.workspace_dir}</code>
                  </div>
                  <p className="muted" style={{ marginTop: '0.45rem' }}>{detail.project.overview}</p>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.45rem', marginTop: '0.75rem' }}>
                    {detail.project.milestones.map((m) => {
                      const checked = detail.progress.completed_milestones.includes(m.id);
                      return (
                        <button
                          key={m.id}
                          className="sidebar-item"
                          onClick={() => toggleMilestone(m.id)}
                          style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', padding: '0.55rem 0.75rem' }}
                        >
                          {checked ? <CheckCircle2 size={16} color="var(--green)" /> : <Circle size={16} color="var(--text-muted)" />}
                          <span style={{ textDecoration: checked ? 'line-through' : 'none', color: checked ? 'var(--text-muted)' : 'var(--text)' }}>
                            {m.label}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </div>
              )}

              {/* Personal Learning Notes */}
              <div className="card">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.55rem' }}>
                  <h3 style={{ display: 'flex', alignItems: 'center', gap: '0.45rem' }}>
                    <FileText size={17} color="var(--amber)" /> Personal Notes & Mental Models
                  </h3>
                  <button
                    className="btn btn-primary"
                    disabled={savingNotes}
                    onClick={async () => {
                      setSavingNotes(true);
                      await updateProgress({ notes });
                      setSavingNotes(false);
                    }}
                  >
                    <Save size={14} /> {savingNotes ? 'Saving...' : 'Save Notes'}
                  </button>
                </div>
                <textarea
                  className="code-editor"
                  style={{ minHeight: 110, fontFamily: 'var(--font-sans)' }}
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="Write down tricky edge cases, your own analogies, or bugs you hit in this chapter..."
                />
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};
