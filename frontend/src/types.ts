export type ChapterStatus = 'not_started' | 'in_progress' | 'completed';
export type WorkbookStatus = 'todo' | 'struggled' | 'solved_with_hints' | 'mastered';

export interface ChapterProgress {
  chapter_id?: string;
  status: ChapterStatus;
  completed_sections: string[];
  completed_milestones: string[];
  quiz_answers: Record<string, number>;
  notes: string;
  updated_at?: string;
}

export interface ChapterSummary {
  id: string;
  number: number;
  phase: number;
  phase_title: string;
  title: string;
  subtitle: string;
  status_type: 'available' | 'roadmap';
  estimated_hours: number;
  why_it_matters: string;
  just_in_time_tags: string[];
  sections_count: number;
  project_title: string | null;
  milestones_count: number;
  progress: ChapterProgress;
}

export interface LessonSection {
  id: string;
  title: string;
  zero_assumption_note?: string;
  definition?: string;
  syntax_box?: {
    title: string;
    syntax: string;
    breakdown: string[];
  };
  tiny_example?: {
    title: string;
    code: string;
    line_by_line: string[];
  };
  body_markdown: string;
  code_example?: {
    title: string;
    code: string;
  };
  common_mistakes?: string[];
  key_takeaway: string;
}

export interface QuizQuestion {
  id: string;
  question: string;
  options: string[];
  correct_index: number;
  explanation: string;
}

export interface ProjectMilestone {
  id: string;
  label: string;
}

export interface ChapterProject {
  title: string;
  workspace_dir: string;
  overview: string;
  architecture_steps: string[];
  milestones: ProjectMilestone[];
}

export interface ChapterDetail extends ChapterSummary {
  visualizer: 'recursion_stack' | 'dp_table' | 'asyncio_loop' | 'numpy_broadcast' | null;
  sections: LessonSection[];
  quizzes: QuizQuestion[];
  project: ChapterProject | null;
  workbook_problem_ids: string[];
}

export interface WorkbookProgress {
  problem_id?: string;
  status: WorkbookStatus;
  last_code: string;
  attempts: number;
  hints_used: number;
  passed_tests: number;
  total_tests: number;
  updated_at?: string;
}

export interface WorkbookSummary {
  id: string;
  chapter_id: string;
  number: string;
  title: string;
  topic: string;
  question_type: string;
  difficulty: 'Foundation' | 'Intermediate' | 'Challenge';
  summary: string;
  progress: WorkbookProgress;
}

export interface WorkbookDetail extends WorkbookSummary {
  prompt_markdown: string;
  thinking_blueprint: string[];
  hints: string[];
  dry_run_trace: string;
  starter_code: string;
  solution_code: string;
  explanation_markdown: string;
  test_cases: { name: string; code: string }[];
}

export interface RunResult {
  ok: boolean;
  stdout: string;
  stderr: string;
  elapsed_ms: number;
  test_results: { name: string; passed: boolean; error: string }[];
  passed_count: number;
  total_count: number;
  progress?: WorkbookProgress;
}

export interface DashboardData {
  streak_days: number;
  chapters: {
    completed: number;
    available_total: number;
    roadmap_total: number;
  };
  sections: {
    completed: number;
    total: number;
  };
  projects: {
    milestones_completed: number;
    milestones_total: number;
  };
  workbook: {
    mastered: number;
    solved_with_hints: number;
    struggled_count: number;
    total: number;
  };
  topic_stats: Record<string, { total: number; mastered: number; struggled: number }>;
  needs_review: {
    id: string;
    title: string;
    chapter_id: string;
    topic: string;
    status: WorkbookStatus;
  }[];
  next_chapter: { id: string; number: number; title: string } | null;
  next_problem: { id: string; title: string; chapter_id: string; topic: string } | null;
}

export interface ProjectOverviewItem {
  chapter_id: string;
  chapter_number: number;
  chapter_title: string;
  phase: number;
  status_type: 'available' | 'roadmap';
  project: ChapterProject;
  completed_milestones: string[];
}
