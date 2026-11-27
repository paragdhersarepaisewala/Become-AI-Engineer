import React, { useMemo, useState } from 'react';
import { ChevronLeft, ChevronRight, RotateCcw } from 'lucide-react';

/* ---------- 1. Recursion Call Stack Visualizer ---------- */
const RECURSION_STEPS = [
  { stack: ['sum_nested([1, [2, 3]])'], note: 'Start root call. First element 1 is an int -> add 1.' },
  { stack: ['sum_nested([1, [2, 3]])', 'sum_nested([2, 3])'], note: 'Found sublist [2, 3]! Pause outer frame & push child frame.' },
  { stack: ['sum_nested([1, [2, 3]])', 'sum_nested([2, 3])', '2 -> base case'], note: 'Base case hit for 2 -> returns 2.' },
  { stack: ['sum_nested([1, [2, 3]])', 'sum_nested([2, 3])', '3 -> base case'], note: 'Base case hit for 3 -> returns 3.' },
  { stack: ['sum_nested([1, [2, 3]])'], note: 'Child frame returns 2 + 3 = 5 and pops off the stack!' },
  { stack: [], note: 'Root frame returns 1 + 5 = 6. Stack empty!' },
];

export const RecursionStackVisualizer: React.FC = () => {
  const [step, setStep] = useState(0);
  const current = RECURSION_STEPS[step];

  return (
    <div className="card" style={{ borderColor: 'rgba(167, 139, 250, 0.35)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
        <div>
          <span className="tag tag-purple">Interactive Visualizer</span>
          <h4 style={{ marginTop: '0.35rem' }}>Call Stack Stepper: `sum_nested([1, [2, 3]])`</h4>
        </div>
        <div style={{ display: 'flex', gap: '0.4rem' }}>
          <button className="btn" onClick={() => setStep((s) => Math.max(0, s - 1))} disabled={step === 0}>
            <ChevronLeft size={15} /> Back
          </button>
          <button className="btn btn-primary" onClick={() => setStep((s) => Math.min(RECURSION_STEPS.length - 1, s + 1))} disabled={step === RECURSION_STEPS.length - 1}>
            Next <ChevronRight size={15} />
          </button>
          <button className="btn" onClick={() => setStep(0)} title="Reset">
            <RotateCcw size={15} />
          </button>
        </div>
      </div>

      <p className="muted" style={{ marginBottom: '0.75rem' }}>
        Step {step + 1}/{RECURSION_STEPS.length}: <strong style={{ color: 'var(--text)' }}>{current.note}</strong>
      </p>

      <div style={{ display: 'flex', flexDirection: 'column-reverse', gap: '0.4rem', minHeight: 130, background: 'var(--bg-code)', padding: '0.85rem', borderRadius: 10, border: '1px solid var(--border)' }}>
        {current.stack.length === 0 ? (
          <div className="muted" style={{ textAlign: 'center', margin: 'auto' }}>Call stack empty — final result: 6</div>
        ) : (
          current.stack.map((frame, i) => (
            <div
              key={i}
              style={{
                padding: '0.45rem 0.75rem',
                borderRadius: 8,
                fontFamily: 'var(--font-mono)',
                fontSize: '0.82rem',
                background: i === current.stack.length - 1 ? 'var(--purple-soft)' : 'var(--bg-elevated)',
                border: `1px solid ${i === current.stack.length - 1 ? 'var(--purple)' : 'var(--border)'}`,
              }}
            >
              Frame #{i + 1}: {frame}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

/* ---------- 2. 2D Dynamic Programming Edit Distance Stepper ---------- */
export const DPTableVisualizer: React.FC = () => {
  const [wordA, setWordA] = useState('cat');
  const [wordB, setWordB] = useState('cut');
  const [progress, setProgress] = useState(9);

  const a = wordA.slice(0, 6);
  const b = wordB.slice(0, 6);

  const { grid, totalCells, lastExplain } = useMemo(() => {
    const m = a.length;
    const n = b.length;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) dp[i][0] = i;
    for (let j = 0; j <= n; j++) dp[0][j] = j;

    let stepIdx = 0;
    let explain = 'Base row & column initialized (insert/delete from empty string).';
    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
        stepIdx++;
        if (a[i - 1] === b[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1];
          if (stepIdx === progress) {
            explain = `a[${i - 1}]='${a[i - 1]}' == b[${j - 1}]='${b[j - 1]}' -> match! Copy diagonal dp[${i - 1}][${j - 1}] = ${dp[i][j]}.`;
          }
        } else {
          const del = dp[i - 1][j];
          const ins = dp[i][j - 1];
          const rep = dp[i - 1][j - 1];
          dp[i][j] = 1 + Math.min(del, ins, rep);
          if (stepIdx === progress) {
            explain = `'${a[i - 1]}' != '${b[j - 1]}' -> 1 + min(del=${del}, ins=${ins}, rep=${rep}) = ${dp[i][j]}.`;
          }
        }
      }
    }
    return { grid: dp, totalCells: m * n, lastExplain: explain };
  }, [a, b, progress]);

  const activeRow = progress > 0 && b.length > 0 ? Math.ceil(progress / b.length) : -1;
  const activeCol = progress > 0 && b.length > 0 ? ((progress - 1) % b.length) + 1 : -1;

  return (
    <div className="card" style={{ borderColor: 'rgba(56, 189, 248, 0.35)' }}>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', alignItems: 'center', gap: '0.75rem', marginBottom: '0.75rem' }}>
        <div>
          <span className="tag tag-accent">Interactive Visualizer</span>
          <h4 style={{ marginTop: '0.35rem' }}>2D Dynamic Programming Table: Edit Distance</h4>
        </div>
        <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
          <input className="input-control" style={{ width: 90 }} value={wordA} onChange={(e) => { setWordA(e.target.value); setProgress(0); }} placeholder="word a" />
          <span className="muted">→</span>
          <input className="input-control" style={{ width: 90 }} value={wordB} onChange={(e) => { setWordB(e.target.value); setProgress(0); }} placeholder="word b" />
          <button className="btn" onClick={() => setProgress((p) => Math.max(0, p - 1))} disabled={progress <= 0}>Back</button>
          <button className="btn btn-primary" onClick={() => setProgress((p) => Math.min(totalCells, p + 1))} disabled={progress >= totalCells}>Step Cell</button>
        </div>
      </div>

      <p className="muted" style={{ marginBottom: '0.75rem' }}>
        Cell ({progress}/{totalCells}): <strong style={{ color: 'var(--text)' }}>{lastExplain}</strong>
      </p>

      <div className="md-table-wrap">
        <table className="md-table" style={{ textAlign: 'center', fontFamily: 'var(--font-mono)' }}>
          <thead>
            <tr>
              <th>a \ b</th>
              <th>""</th>
              {b.split('').map((ch, j) => (
                <th key={j}>{ch}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {grid.map((row, i) => (
              <tr key={i}>
                <th>{i === 0 ? '""' : a[i - 1]}</th>
                {row.map((val, j) => {
                  const cellOrder = (i - 1) * b.length + j;
                  const isBase = i === 0 || j === 0;
                  const isVisible = isBase || cellOrder <= progress;
                  const isCurrent = i === activeRow && j === activeCol;
                  return (
                    <td
                      key={j}
                      style={{
                        background: isCurrent ? 'var(--accent-soft)' : isBase ? 'var(--bg-elevated)' : 'transparent',
                        color: isCurrent ? 'var(--accent)' : isVisible ? 'var(--text)' : 'var(--border-bright)',
                        fontWeight: isCurrent || (i === a.length && j === b.length && isVisible) ? 700 : 400,
                      }}
                    >
                      {isVisible ? val : '·'}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

/* ---------- 3. Asyncio Event Loop Timeline Visualizer ---------- */
export const AsyncioLoopVisualizer: React.FC = () => {
  const [mode, setMode] = useState<'seq' | 'gather' | 'sem2'>('gather');

  const bars =
    mode === 'seq'
      ? [
          { label: 'Task 1 (1s I/O)', start: 0, width: 25 },
          { label: 'Task 2 (1s I/O)', start: 25, width: 25 },
          { label: 'Task 3 (1s I/O)', start: 50, width: 25 },
          { label: 'Task 4 (1s I/O)', start: 75, width: 25 },
        ]
      : mode === 'gather'
      ? [
          { label: 'Task 1 (1s I/O)', start: 0, width: 25 },
          { label: 'Task 2 (1s I/O)', start: 0, width: 25 },
          { label: 'Task 3 (1s I/O)', start: 0, width: 25 },
          { label: 'Task 4 (1s I/O)', start: 0, width: 25 },
        ]
      : [
          { label: 'Task 1 (1s I/O)', start: 0, width: 25 },
          { label: 'Task 2 (1s I/O)', start: 0, width: 25 },
          { label: 'Task 3 (waits sem)', start: 25, width: 25 },
          { label: 'Task 4 (waits sem)', start: 25, width: 25 },
        ];

  const totalTime = mode === 'seq' ? '4.0s' : mode === 'gather' ? '1.0s' : '2.0s';

  return (
    <div className="card" style={{ borderColor: 'rgba(52, 211, 153, 0.35)' }}>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', alignItems: 'center', gap: '0.75rem', marginBottom: '0.75rem' }}>
        <div>
          <span className="tag tag-green">Interactive Visualizer</span>
          <h4 style={{ marginTop: '0.35rem' }}>Asyncio Event Loop Timeline (4 Network Requests @ 1s each)</h4>
        </div>
        <div style={{ display: 'flex', gap: '0.4rem' }}>
          <button className={`btn ${mode === 'seq' ? 'btn-primary' : ''}`} onClick={() => setMode('seq')}>Sequential `for await`</button>
          <button className={`btn ${mode === 'gather' ? 'btn-primary' : ''}`} onClick={() => setMode('gather')}>`asyncio.gather`</button>
          <button className={`btn ${mode === 'sem2' ? 'btn-primary' : ''}`} onClick={() => setMode('sem2')}>`Semaphore(2)`</button>
        </div>
      </div>

      <p className="muted" style={{ marginBottom: '0.75rem' }}>
        Total Wall-Clock Time: <strong style={{ color: 'var(--green)' }}>{totalTime}</strong>
      </p>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
        {bars.map((b, i) => (
          <div key={i} style={{ display: 'grid', gridTemplateColumns: '150px 1fr', alignItems: 'center', gap: '0.75rem' }}>
            <span style={{ fontSize: '0.82rem', fontFamily: 'var(--font-mono)' }}>{b.label}</span>
            <div style={{ position: 'relative', height: 22, background: 'var(--bg-code)', borderRadius: 6, border: '1px solid var(--border)' }}>
              <div
                style={{
                  position: 'absolute',
                  left: `${b.start}%`,
                  width: `${b.width}%`,
                  top: 2,
                  bottom: 2,
                  borderRadius: 4,
                  background: mode === 'seq' ? 'var(--rose)' : 'var(--green)',
                  transition: 'all 0.25s ease',
                }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

/* ---------- 4. NumPy Broadcasting Explorer ---------- */
function parseShape(raw: string): number[] | null {
  const parts = raw
    .replace(/[()\[\]\s]/g, '')
    .split(',')
    .filter(Boolean);
  if (parts.length === 0) return null;
  const nums = parts.map(Number);
  return nums.every((n) => Number.isInteger(n) && n > 0) ? nums : null;
}

export const NumpyBroadcastVisualizer: React.FC = () => {
  const [shapeA, setShapeA] = useState('4, 3');
  const [shapeB, setShapeB] = useState('3');

  const analysis = useMemo(() => {
    const a = parseShape(shapeA);
    const b = parseShape(shapeB);
    if (!a || !b) return { ok: false, error: 'Enter comma-separated positive integers like `4, 3` and `3`.' };
    const len = Math.max(a.length, b.length);
    const padA = [...Array(len - a.length).fill(1), ...a];
    const padB = [...Array(len - b.length).fill(1), ...b];
    const out: number[] = [];
    for (let i = 0; i < len; i++) {
      if (padA[i] === padB[i] || padA[i] === 1 || padB[i] === 1) {
        out.push(Math.max(padA[i], padB[i]));
      } else {
        return {
          ok: false,
          padA,
          padB,
          error: `Dimension mismatch at axis ${i}: ${padA[i]} vs ${padB[i]} (neither is 1!).`,
        };
      }
    }
    return { ok: true, padA, padB, out };
  }, [shapeA, shapeB]);

  return (
    <div className="card" style={{ borderColor: 'rgba(56, 189, 248, 0.35)' }}>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between', alignItems: 'center', gap: '0.75rem', marginBottom: '0.75rem' }}>
        <div>
          <span className="tag tag-accent">Interactive Visualizer</span>
          <h4 style={{ marginTop: '0.35rem' }}>NumPy Broadcasting Alignment Checker</h4>
        </div>
        <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
          <button className="btn" onClick={() => { setShapeA('4, 3'); setShapeB('3'); }}>(4,3) + (3,)</button>
          <button className="btn" onClick={() => { setShapeA('32, 1, 64'); setShapeB('1, 128, 64'); }}>(32,1,64) + (1,128,64)</button>
          <button className="btn" onClick={() => { setShapeA('4, 3'); setShapeB('4'); }}>(4,3) + (4,) ❌</button>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center', flexWrap: 'wrap', marginBottom: '0.75rem' }}>
        <label className="muted">Shape A: <input className="input-control" style={{ width: 130, marginLeft: 6 }} value={shapeA} onChange={(e) => setShapeA(e.target.value)} /></label>
        <label className="muted">Shape B: <input className="input-control" style={{ width: 130, marginLeft: 6 }} value={shapeB} onChange={(e) => setShapeB(e.target.value)} /></label>
      </div>

      {analysis.ok ? (
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.85rem', background: 'var(--bg-code)', padding: '0.8rem', borderRadius: 8, border: '1px solid var(--green)' }}>
          <div>Padded A: ({analysis.padA!.join(', ')})</div>
          <div>Padded B: ({analysis.padB!.join(', ')})</div>
          <div style={{ color: 'var(--green)', marginTop: 4, fontWeight: 700 }}>Output Shape: ({analysis.out!.join(', ')}) ✓</div>
        </div>
      ) : (
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.85rem', background: 'var(--bg-code)', padding: '0.8rem', borderRadius: 8, border: '1px solid var(--rose)', color: 'var(--rose)' }}>
          {analysis.error}
        </div>
      )}
    </div>
  );
};
