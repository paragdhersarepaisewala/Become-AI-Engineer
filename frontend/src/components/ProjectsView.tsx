import React, { useEffect, useState } from 'react';
import { CheckCircle2, Circle, FolderKanban } from 'lucide-react';
import { api } from '../api';
import type { ProjectOverviewItem } from '../types';

interface Props {
  onOpenChapter: (chapterId: string) => void;
  onProgressChanged: () => void;
}

export const ProjectsView: React.FC<Props> = ({ onOpenChapter, onProgressChanged }) => {
  const [projects, setProjects] = useState<ProjectOverviewItem[]>([]);

  const load = () => {
    api.getProjects().then(setProjects);
  };

  useEffect(() => {
    load();
  }, []);

  const toggleMilestone = async (item: ProjectOverviewItem, milestoneId: string) => {
    const set = new Set(item.completed_milestones);
    if (set.has(milestoneId)) set.delete(milestoneId);
    else set.add(milestoneId);
    await api.updateChapterProgress(item.chapter_id, {
      completed_milestones: Array.from(set),
    });
    load();
    onProgressChanged();
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <div className="card">
        <h2>Project-Based Learning Hub</h2>
        <p className="muted" style={{ marginTop: '0.25rem' }}>
          Every chapter ends with a real engineering artifact in your workspace. Check off milestones here as you build and test each project in VS Code.
        </p>
      </div>

      <div className="grid-2">
        {projects.map((item) => {
          const isRoadmap = item.status_type === 'roadmap';
          const total = item.project.milestones.length;
          const done = item.completed_milestones.length;
          const pct = total ? Math.round((done / total) * 100) : 0;

          return (
            <div key={item.chapter_id} className="card" style={{ opacity: isRoadmap ? 0.72 : 1, display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span className="tag tag-accent">Chapter {item.chapter_number}</span>
                <code className="inline-code">{item.project.workspace_dir}</code>
              </div>
              <h3 style={{ display: 'flex', alignItems: 'center', gap: '0.45rem' }}>
                <FolderKanban size={17} color="var(--accent)" /> {item.project.title}
              </h3>
              <p className="muted" style={{ margin: 0 }}>{item.project.overview}</p>

              {!isRoadmap && total > 0 && (
                <>
                  <div className="progress-track">
                    <div className="progress-fill" style={{ width: `${pct}%` }} />
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.35rem' }}>
                    {item.project.milestones.map((m) => {
                      const checked = item.completed_milestones.includes(m.id);
                      return (
                        <button
                          key={m.id}
                          className="sidebar-item"
                          onClick={() => toggleMilestone(item, m.id)}
                          style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.45rem 0.65rem', fontSize: '0.84rem' }}
                        >
                          {checked ? <CheckCircle2 size={15} color="var(--green)" /> : <Circle size={15} color="var(--text-muted)" />}
                          <span style={{ textDecoration: checked ? 'line-through' : 'none', color: checked ? 'var(--text-muted)' : 'var(--text)' }}>
                            {m.label}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </>
              )}

              <div>
                <button className="btn" onClick={() => onOpenChapter(item.chapter_id)}>
                  Open Chapter Lesson
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
