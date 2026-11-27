import { useEffect, useState } from 'react';
import { BookOpen, Code2, Cpu, Flame, FolderKanban, LayoutDashboard } from 'lucide-react';
import { api } from './api';
import { CourseView } from './components/CourseView';
import { DashboardView } from './components/DashboardView';
import { ProjectsView } from './components/ProjectsView';
import { WorkbookView } from './components/WorkbookView';
import type { ChapterSummary, DashboardData } from './types';

type Tab = 'dashboard' | 'course' | 'workbook' | 'projects';

export function App() {
  const [tab, setTab] = useState<Tab>('dashboard');
  const [dashboard, setDashboard] = useState<DashboardData | null>(null);
  const [chapters, setChapters] = useState<ChapterSummary[]>([]);
  const [selectedChapterId, setSelectedChapterId] = useState('ch01');
  const [workbookChapterFilter, setWorkbookChapterFilter] = useState('');
  const [workbookProblemId, setWorkbookProblemId] = useState('');
  const [error, setError] = useState('');

  const refreshAll = async () => {
    try {
      const [dash, chs] = await Promise.all([api.getDashboard(), api.getChapters()]);
      setDashboard(dash);
      setChapters(chs);
      setError('');
    } catch (err) {
      setError(
        err instanceof Error
          ? `Backend not reachable (${err.message}). Start FastAPI on port 8000.`
          : 'Failed to load backend API.'
      );
    }
  };

  useEffect(() => {
    refreshAll();
  }, []);

  const openChapter = (chapterId: string) => {
    setSelectedChapterId(chapterId);
    setTab('course');
  };

  const openProblem = (problemId: string, chapterId = '') => {
    setWorkbookChapterFilter(chapterId);
    setWorkbookProblemId(problemId);
    setTab('workbook');
  };

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand">
          <div className="brand-badge">
            <Cpu size={18} />
          </div>
          <span>AI Engineer Academy</span>
        </div>

        <nav className="nav-tabs">
          <button className={`nav-tab ${tab === 'dashboard' ? 'active' : ''}`} onClick={() => setTab('dashboard')}>
            <LayoutDashboard size={15} /> Dashboard
          </button>
          <button className={`nav-tab ${tab === 'course' ? 'active' : ''}`} onClick={() => setTab('course')}>
            <BookOpen size={15} /> Course
          </button>
          <button className={`nav-tab ${tab === 'workbook' ? 'active' : ''}`} onClick={() => setTab('workbook')}>
            <Code2 size={15} /> Practice Workbook
          </button>
          <button className={`nav-tab ${tab === 'projects' ? 'active' : ''}`} onClick={() => setTab('projects')}>
            <FolderKanban size={15} /> Projects
          </button>
        </nav>

        <div className="streak-pill">
          <Flame size={15} />
          <span>{dashboard ? `${dashboard.streak_days}d streak` : '…'}</span>
        </div>
      </header>

      <main className="main-container">
        {error && (
          <div className="card" style={{ borderColor: 'var(--rose)', color: 'var(--rose)', marginBottom: '1rem' }}>
            {error}
          </div>
        )}

        {tab === 'dashboard' && dashboard && (
          <DashboardView
            dashboard={dashboard}
            chapters={chapters}
            onOpenChapter={openChapter}
            onOpenProblem={openProblem}
          />
        )}

        {tab === 'course' && chapters.length > 0 && (
          <CourseView
            chapters={chapters}
            selectedChapterId={selectedChapterId}
            onSelectChapter={setSelectedChapterId}
            onProgressChanged={refreshAll}
            onJumpToWorkbook={(chId) => {
              setWorkbookChapterFilter(chId);
              setWorkbookProblemId('');
              setTab('workbook');
            }}
          />
        )}

        {tab === 'workbook' && (
          <WorkbookView
            chapters={chapters}
            initialChapterFilter={workbookChapterFilter}
            initialProblemId={workbookProblemId}
            onProgressChanged={refreshAll}
          />
        )}

        {tab === 'projects' && (
          <ProjectsView onOpenChapter={openChapter} onProgressChanged={refreshAll} />
        )}
      </main>
    </div>
  );
}

export default App;
