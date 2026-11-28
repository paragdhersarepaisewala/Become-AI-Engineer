import React from 'react';
import { ArrowRight, BookOpen, CheckCircle2, Code2, Flame, FolderKanban, AlertTriangle } from 'lucide-react';
import type { ChapterSummary, DashboardData } from '../types';

interface Props {
  dashboard: DashboardData;
  chapters: ChapterSummary[];
  onOpenChapter: (chapterId: string) => void;
  onOpenProblem: (problemId: string, chapterId?: string) => void;
}

export const DashboardView: React.FC<Props> = ({
  dashboard,
  chapters,
  onOpenChapter,
  onOpenProblem,
}) => {
  const secPct = dashboard.sections.total
    ? Math.round((dashboard.sections.completed / dashboard.sections.total) * 100)
    : 0;
  const wbPct = dashboard.workbook.total
    ? Math.round((dashboard.workbook.mastered / dashboard.workbook.total) * 100)
    : 0;
  const projPct = dashboard.projects.milestones_total
    ? Math.round(
        (dashboard.projects.milestones_completed / dashboard.projects.milestones_total) * 100
      )
    : 0;

  const phases = [1, 2, 3, 4].map((p) => ({
    phase: p,
    items: chapters.filter((c) => c.phase === p),
  }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
      {/* Hero & Recommended Next Step */}
      <div className="card" style={{ background: 'linear-gradient(135deg, rgba(56,189,248,0.1), rgba(167,139,250,0.08))', borderColor: 'var(--border-bright)' }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', alignItems: 'center', gap: '1rem' }}>
          <div>
            <span className="tag tag-accent">AI Engineering Path · RTX 5070 Ti Ready</span>
            <h1 style={{ fontSize: '1.6rem', marginTop: '0.45rem' }}>From Basic Scripts to Training Small LLMs</h1>
            <p className="muted" style={{ maxWidth: 720, marginTop: '0.35rem' }}>
              Zero assumed knowledge, one library per chapter. Master Python basics, files, <code className="inline-code">os</code> automations, OOP, logic building, DP, Asyncio, NumPy, Pandas, Pydantic, Requests, FastAPI, FastMCP, and Docker before diving into PyTorch, Transformers, QLoRA, and LangChain.
            </p>
          </div>
          <div style={{ display: 'flex', gap: '0.6rem', flexWrap: 'wrap' }}>
            {dashboard.next_chapter && (
              <button className="btn btn-primary" onClick={() => onOpenChapter(dashboard.next_chapter!.id)}>
                <BookOpen size={16} /> Ch {dashboard.next_chapter.number}: {dashboard.next_chapter.title.slice(0, 26)}… <ArrowRight size={15} />
              </button>
            )}
            {dashboard.next_problem && (
              <button className="btn" onClick={() => onOpenProblem(dashboard.next_problem!.id, dashboard.next_problem!.chapter_id)}>
                <Code2 size={16} /> Next Drill: {dashboard.next_problem.title.slice(0, 24)}…
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Stat Cards */}
      <div className="grid-4">
        <div className="card">
          <div className="muted" style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Chapters Completed</span> <BookOpen size={16} color="var(--accent)" />
          </div>
          <div className="stat-value">
            {dashboard.chapters.completed} / {dashboard.chapters.available_total}
          </div>
          <div className="muted">{dashboard.chapters.roadmap_total} total chapters in full track</div>
        </div>

        <div className="card">
          <div className="muted" style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Lesson Sections</span> <CheckCircle2 size={16} color="var(--green)" />
          </div>
          <div className="stat-value">{secPct}%</div>
          <div className="progress-track" style={{ marginTop: '0.4rem' }}>
            <div className="progress-fill" style={{ width: `${secPct}%` }} />
          </div>
          <div className="muted" style={{ marginTop: '0.3rem' }}>
            {dashboard.sections.completed} / {dashboard.sections.total} sections understood
          </div>
        </div>

        <div className="card">
          <div className="muted" style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Workbook Mastery</span> <Code2 size={16} color="var(--purple)" />
          </div>
          <div className="stat-value">{wbPct}%</div>
          <div className="progress-track" style={{ marginTop: '0.4rem' }}>
            <div className="progress-fill" style={{ width: `${wbPct}%` }} />
          </div>
          <div className="muted" style={{ marginTop: '0.3rem' }}>
            {dashboard.workbook.mastered} mastered · {dashboard.workbook.solved_with_hints} with hints · {dashboard.workbook.total} total
          </div>
        </div>

        <div className="card">
          <div className="muted" style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Projects & Streak</span> <Flame size={16} color="var(--amber)" />
          </div>
          <div className="stat-value">{dashboard.streak_days}d streak</div>
          <div className="muted" style={{ marginTop: '0.3rem' }}>
            <FolderKanban size={13} style={{ verticalAlign: 'middle' }} /> {dashboard.projects.milestones_completed} / {dashboard.projects.milestones_total} project milestones ({projPct}%)
          </div>
        </div>
      </div>

      {/* Topic Breakdown & Weak-Spot Radar */}
      <div className="grid-2">
        <div className="card">
          <h3 style={{ marginBottom: '0.85rem' }}>Skill Mastery by Topic</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
            {Object.entries(dashboard.topic_stats).map(([topic, stat]) => {
              const pct = stat.total ? Math.round((stat.mastered / stat.total) * 100) : 0;
              return (
                <div key={topic}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: 4 }}>
                    <span>{topic}</span>
                    <span className="muted">
                      {stat.mastered}/{stat.total} mastered
                      {stat.struggled > 0 && <span style={{ color: 'var(--rose)' }}> · {stat.struggled} review</span>}
                    </span>
                  </div>
                  <div className="progress-track">
                    <div className="progress-fill" style={{ width: `${pct}%` }} />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        <div className="card">
          <h3 style={{ marginBottom: '0.85rem', display: 'flex', alignItems: 'center', gap: '0.45rem' }}>
            <AlertTriangle size={17} color="var(--amber)" /> Needs Review (Logic & Weak Spots)
          </h3>
          {dashboard.needs_review.length === 0 ? (
            <p className="muted">
              No struggled drills yet! Any workbook problem you fail or mark <strong>Struggled</strong> or solve using hints will appear here for spaced review.
            </p>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              {dashboard.needs_review.map((item) => (
                <button
                  key={item.id}
                  className="sidebar-item"
                  onClick={() => onOpenProblem(item.id, item.chapter_id)}
                  style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}
                >
                  <div>
                    <div style={{ fontWeight: 600, fontSize: '0.9rem' }}>{item.title}</div>
                    <div className="muted" style={{ fontSize: '0.78rem' }}>{item.topic}</div>
                  </div>
                  <span className={`tag ${item.status === 'struggled' ? 'tag-rose' : 'tag-amber'}`}>
                    {item.status === 'struggled' ? 'Struggled' : 'Used Hints'}
                  </span>
                </button>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Full 20-Chapter Roadmap */}
      <div className="card">
        <h3 style={{ marginBottom: '1rem' }}>20-Chapter Master Curriculum</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          {phases.map(({ phase, items }) => (
            <div key={phase}>
              <div style={{ fontSize: '0.92rem', fontWeight: 700, color: 'var(--accent)', marginBottom: '0.6rem' }}>
                {items[0]?.phase_title}
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(270px, 1fr))', gap: '0.75rem' }}>
                {items.map((ch) => {
                  const isRoadmap = ch.status_type === 'roadmap';
                  const st = ch.progress.status;
                  return (
                    <button
                      key={ch.id}
                      className="sidebar-item"
                      onClick={() => onOpenChapter(ch.id)}
                      style={{ opacity: isRoadmap ? 0.72 : 1, display: 'flex', flexDirection: 'column', gap: '0.4rem' }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', alignItems: 'center' }}>
                        <span className="tag tag-accent">Ch {ch.number}</span>
                        {isRoadmap ? (
                          <span className="tag tag-purple">Phase 3–4 Roadmap</span>
                        ) : st === 'completed' ? (
                          <span className="tag tag-green">Completed</span>
                        ) : st === 'in_progress' ? (
                          <span className="tag tag-amber">In Progress</span>
                        ) : (
                          <span className="tag">Ready · {ch.estimated_hours}h</span>
                        )}
                      </div>
                      <div style={{ fontWeight: 600, fontSize: '0.95rem' }}>{ch.title}</div>
                      <div className="muted" style={{ fontSize: '0.8rem' }}>{ch.subtitle}</div>
                    </button>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
