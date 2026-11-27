import type {
  ChapterDetail,
  ChapterProgress,
  ChapterStatus,
  ChapterSummary,
  DashboardData,
  ProjectOverviewItem,
  RunResult,
  WorkbookDetail,
  WorkbookProgress,
  WorkbookStatus,
  WorkbookSummary,
} from './types';

const BASE = '/api';

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...init,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `HTTP ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export const api = {
  getDashboard: () => request<DashboardData>('/dashboard'),
  getChapters: () => request<ChapterSummary[]>('/chapters'),
  getChapter: (id: string) => request<ChapterDetail>(`/chapters/${id}`),
  updateChapterProgress: (
    id: string,
    payload: {
      status?: ChapterStatus;
      completed_sections?: string[];
      completed_milestones?: string[];
      quiz_answers?: Record<string, number>;
      notes?: string;
    }
  ) =>
    request<ChapterProgress>(`/chapters/${id}/progress`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  getWorkbook: (params?: { chapter_id?: string; topic?: string; difficulty?: string }) => {
    const qs = new URLSearchParams();
    if (params?.chapter_id) qs.set('chapter_id', params.chapter_id);
    if (params?.topic) qs.set('topic', params.topic);
    if (params?.difficulty) qs.set('difficulty', params.difficulty);
    const suffix = qs.toString() ? `?${qs.toString()}` : '';
    return request<WorkbookSummary[]>(`/workbook${suffix}`);
  },
  getProblem: (id: string) => request<WorkbookDetail>(`/workbook/${id}`),
  updateProblemProgress: (
    id: string,
    payload: { status?: WorkbookStatus; last_code?: string; hints_used?: number }
  ) =>
    request<WorkbookProgress>(`/workbook/${id}/progress`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  runCode: (payload: { problem_id?: string; code: string; mode: 'scratch' | 'test' }) =>
    request<RunResult>('/workbook/run', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  getProjects: () => request<ProjectOverviewItem[]>('/projects'),
};
