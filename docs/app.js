// NEET Learning Hub: Class 1 -> 12 -> NEET path, chapter practice, NEET-pattern mock tests and progress.
// Data: data/index.json (syllabus + counts) and data/cNN.json (questions per class).
// A question is [id, chapterId, difficulty E/M/H, text, [A, B, C, D], correctIndex, explanation, fromSchoolBank].
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const shuffle = (a) => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const SUBJ = { Physics: 'var(--phy)', Chemistry: 'var(--che)', Biology: 'var(--bio)' };
  const SECTIONS = [
    { key: 'Physics', label: 'Physics', test: (c) => c.subject === 'Physics', c: 'var(--phy)' },
    { key: 'Chemistry', label: 'Chemistry', test: (c) => c.subject === 'Chemistry', c: 'var(--che)' },
    { key: 'Botany', label: 'Botany', test: (c) => c.subject === 'Biology' && c.branch === 'Botany', c: 'var(--bio)' },
    { key: 'Zoology', label: 'Zoology', test: (c) => c.subject === 'Biology' && c.branch === 'Zoology', c: 'var(--bio)' },
  ];
  const MODES = {
    full: { label: 'Full NEET mock', per: 45, mins: 180 },
    half: { label: 'Half mock', per: 23, mins: 90 },
    quick: { label: 'Quick test', per: 12, mins: 48 },
  };
  const ECOS_URL = 'https://saiqulmodi.github.io/EcosSynthetica/';

  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* storage blocked: progress lasts this visit */ } },
  };

  let INDEX = null;
  const CH = {};
  const DATA = {};
  const BYID = {};
  let stats = store.get('nh-stats', {});   // id -> [tries, correct, chapterId]
  let session = null;                       // chapter practice
  let mock = store.get('nh-mock-live', null);
  let timerId = null;
  const app = $('#app');

  async function loadIndex() {
    INDEX = await (await fetch('data/index.json')).json();
    for (const c of INDEX.chapters) CH[c.id] = c;
  }
  async function loadClass(cls) {
    if (!DATA[cls]) {
      DATA[cls] = await (await fetch(`data/c${String(cls).padStart(2, '0')}.json`)).json();
      for (const q of DATA[cls]) BYID[q[0]] = q;
    }
    return DATA[cls];
  }

  function record(q, ok) {
    const s = stats[q[0]] || [0, 0, q[1]];
    s[0]++; if (ok) s[1]++; s[2] = q[1];
    stats[q[0]] = s;
    store.set('nh-stats', stats);
  }
  function chapterAgg() {
    const agg = {};
    for (const [, [t, c, cid]] of Object.entries(stats)) {
      const a = agg[cid] || (agg[cid] = { seen: 0, tries: 0, correct: 0 });
      a.seen++; a.tries += t; a.correct += c;
    }
    return agg;
  }
  const pct = (a, b) => (b ? Math.round((100 * a) / b) : 0);

  // ---------------------------------------------------------------- routing
  function route() {
    clearInterval(timerId);
    const h = location.hash.slice(1) || 'path';
    document.querySelectorAll('[data-nav]').forEach((a) => a.classList.toggle('on', h.startsWith(a.dataset.nav) || (a.dataset.nav === 'path' && /^(class|practice)/.test(h))));
    if (h.startsWith('class-')) { store.set('nh-class', Number(h.slice(6))); return viewPath(); }
    if (h.startsWith('practice-')) return viewPractice(h.slice(9));
    if (h === 'mock') return viewMock();
    if (h === 'progress') return viewProgress();
    return viewPath();
  }
  window.addEventListener('hashchange', route);

  // ---------------------------------------------------------------- path
  function viewPath() {
    const cls = store.get('nh-class', 11);
    const agg = chapterAgg();
    const total = INDEX.chapters.reduce((n, c) => n + c.count, 0);
    const neetTotal = INDEX.chapters.filter((c) => c.neet).reduce((n, c) => n + c.count, 0);
    const rungs = [];
    for (let k = 1; k <= 12; k++) {
      const chs = INDEX.chapters.filter((c) => c.cls === k);
      const cnt = chs.reduce((n, c) => n + c.count, 0);
      const seen = chs.reduce((n, c) => n + ((agg[c.id] || {}).seen || 0), 0);
      rungs.push(`<a class="rung ${k === cls ? 'on' : ''}" href="#class-${k}" style="text-decoration:none;color:inherit"><span>Class</span><b>${k}</b><span class="num">${cnt}</span><div class="bar"><i style="width:${pct(seen, cnt)}%"></i></div></a>`);
    }
    rungs.push(`<a class="rung neet" href="#mock" style="text-decoration:none"><span>Exam</span><b>NEET</b><span>mock</span></a>`);

    const chs = INDEX.chapters.filter((c) => c.cls === cls);
    const subjects = ['Physics', 'Chemistry', 'Biology'].filter((s) => chs.some((c) => c.subject === s));
    const cols = subjects.map((s) => {
      const list = chs.filter((c) => c.subject === s);
      const n = list.reduce((a, c) => a + c.count, 0);
      let lastUnit = null;
      const rows = list.map((c) => {
        const a = agg[c.id] || { seen: 0, tries: 0, correct: 0 };
        const unit = cls >= 11 && c.unitTitle !== lastUnit ? `<div class="unit">${c.neet ? `NEET unit ${c.unit}: ` : ''}${esc(c.unitTitle)}</div>` : '';
        lastUnit = c.unitTitle;
        return `${unit}<div class="ch">
          <div class="ch-title">${esc(c.title)} ${c.neet || cls < 11 ? '' : '<span class="tag-beyond">beyond NEET</span>'}</div>
          <a class="btn small" href="#practice-${c.id}">Practise</a>
          <div class="ch-meta"><span class="num">${c.count} Q</span><span class="num">${a.seen} done</span>${a.tries ? `<span class="num">${pct(a.correct, a.tries)}% correct</span>` : ''}${c.ecos ? `<a class="ecos" href="${ECOS_URL}" target="_blank" rel="noopener">Play in Ecos-Synthetica</a>` : ''}</div>
          <div class="prog"><i style="width:${pct(a.seen, c.count)}%"></i></div>
        </div>`;
      }).join('');
      return `<section class="subj" style="--c:${SUBJ[s]}"><header><h2>${s}</h2><span class="eyebrow num">${n} questions</span></header>${rows}</section>`;
    }).join('');

    app.innerHTML = `
      <p class="eyebrow">Biology · Chemistry · Physics</p>
      <h1>From Class 1 to the NEET hall</h1>
      <p class="lead">${total.toLocaleString('en-IN')} questions with answers and explanations, arranged by class and chapter. Classes 1-10 build the foundation; Class 11-12 chapters follow the NCERT books and the official NEET-UG units (${neetTotal.toLocaleString('en-IN')} questions). Pick a class, practise a chapter, then take a full NEET-pattern mock.</p>
      <div class="ladder">${rungs.join('')}</div>
      <div class="row" style="justify-content:space-between;margin-bottom:12px"><h2 style="margin:0">Class ${cls}${cls >= 11 ? ' · NEET syllabus' : cls >= 6 ? ' · Science foundation' : ' · EVS foundation'}</h2>
      ${cls < 12 ? `<a class="btn small" href="#class-${cls + 1}">Next: Class ${cls + 1}</a>` : '<a class="btn small primary" href="#mock">Next: NEET mock test</a>'}</div>
      <div class="subjects">${cols}</div>`;
  }

  // ---------------------------------------------------------------- practice
  async function viewPractice(cid) {
    const c = CH[cid];
    if (!c) { location.hash = 'path'; return; }
    if (!session || session.cid !== cid || session.done) {
      app.innerHTML = '<p class="loading">Loading questions...</p>';
      const all = (await loadClass(c.cls)).filter((q) => q[1] === cid);
      const unseen = shuffle(all.filter((q) => !stats[q[0]]));
      const wrong = shuffle(all.filter((q) => stats[q[0]] && stats[q[0]][1] < stats[q[0]][0]));
      const rest = shuffle(all.filter((q) => stats[q[0]] && stats[q[0]][1] === stats[q[0]][0]));
      session = { cid, qs: [...unseen, ...wrong, ...rest].slice(0, 10), i: 0, picks: [], done: false };
    }
    renderPractice();
  }

  function renderPractice() {
    const s = session;
    const c = CH[s.cid];
    const back = `<a class="btn small" href="#class-${c.cls}">Back to Class ${c.cls}</a>`;
    if (s.i >= s.qs.length) {
      s.done = true;
      const right = s.picks.filter((p, k) => p === s.qs[k][5]).length;
      app.innerHTML = `<div class="qwrap"><div class="qcard summary" style="--c:${SUBJ[c.subject]}">
        <p class="eyebrow">${esc(c.subject)} · Class ${c.cls}</p><h2>${esc(c.title)}</h2>
        <div class="big num">${right}/${s.qs.length}</div>
        <p class="lead" style="margin:10px auto">${right === s.qs.length ? 'All correct. Try a NEET mock to test it under time pressure.' : right >= s.qs.length * 0.7 ? 'Good work. Practise again to clear the ones you missed.' : 'Read the explanations, then practise again; missed questions come back first.'}</p>
        <div class="row" style="justify-content:center"><button class="btn primary" id="again">Practise 10 more</button>${back}</div></div></div>`;
      $('#again').onclick = () => { session = null; viewPractice(c.id); };
      return;
    }
    const q = s.qs[s.i];
    const picked = s.picks[s.i];
    const answered = picked !== undefined;
    const dots = s.qs.map((qq, k) => `<i class="${k < s.picks.length ? (s.picks[k] === qq[5] ? 'r' : 'w') : k === s.i ? 'c' : ''}"></i>`).join('');
    app.innerHTML = `<div class="qwrap">
      <div class="qhead"><div><p class="eyebrow" style="color:${SUBJ[c.subject]}">${esc(c.subject)} · Class ${c.cls}${c.neet ? ` · NEET unit ${c.unit}` : ''}</p><h3 style="margin:0">${esc(c.title)}</h3></div>${back}</div>
      <div class="qcard">
        <div class="qhead"><span class="eyebrow num">Question ${s.i + 1} of ${s.qs.length}</span><div class="dots">${dots}</div></div>
        <p class="qtext">${esc(q[3])}</p>
        <div class="opts">${q[4].map((o, k) => {
          let cls = '';
          if (answered && k === q[5]) cls = 'right';
          else if (answered && k === picked) cls = 'wrong';
          return `<button class="opt ${cls}" data-k="${k}" ${answered ? 'disabled' : ''}><span class="l">${'ABCD'[k]}</span><span>${esc(o)}</span></button>`;
        }).join('')}</div>
        ${answered ? `<div class="explain ${picked === q[5] ? '' : 'bad'}"><b>${picked === q[5] ? 'Correct' : `Answer: ${'ABCD'[q[5]]}. ${esc(q[4][q[5]])}`}</b>${esc(q[6])}</div>` : ''}
        <p class="src">${q[7] ? 'From the School MCQ Bank' : 'NEET Hub question'} · difficulty ${{ E: 'easy', M: 'medium', H: 'hard' }[q[2]] || 'medium'}</p>
        <div class="qfoot"><span></span>${answered ? `<button class="btn primary" id="next">${s.i + 1 < s.qs.length ? 'Next question' : 'See my score'}</button>` : ''}</div>
      </div></div>`;
    app.querySelectorAll('.opt').forEach((b) => {
      b.onclick = () => { const k = Number(b.dataset.k); s.picks[s.i] = k; record(q, k === q[5]); renderPractice(); };
    });
    if ($('#next')) $('#next').onclick = () => { s.i++; renderPractice(); window.scrollTo(0, 0); };
  }

  // ---------------------------------------------------------------- mock test
  async function viewMock() {
    if (mock && !mock.done) { app.innerHTML = '<p class="loading">Loading your test...</p>'; await loadClass(11); await loadClass(12); return renderTest(); }
    if (mock && mock.done) return renderResult();
    const hist = store.get('nh-mocks', []);
    app.innerHTML = `
      <p class="eyebrow">NEET-UG pattern</p>
      <h1>Mock tests</h1>
      <p class="lead">Questions are drawn from every NEET chapter of Class 11 and 12, spread evenly across chapters. Marking follows NEET: +4 for a correct answer, -1 for a wrong one, 0 if left blank. Your test is saved as you go, so you can close the page and come back.</p>
      <div class="modes">${Object.entries(MODES).map(([k, m]) => `
        <div class="mode"><span class="eyebrow">${esc(m.label)}</span><div class="big num">${m.per * 4}</div><span>questions · ${m.mins} minutes · maximum ${m.per * 16} marks</span>
        <button class="btn ${k === 'full' ? 'primary' : ''}" data-mode="${k}">Start ${esc(m.label.toLowerCase())}</button></div>`).join('')}</div>
      <div class="scroll-x"><table class="pattern"><thead><tr><th>Section</th><th>Full mock</th><th>Covers</th></tr></thead><tbody>
        <tr><td style="color:var(--phy);font-weight:600">Physics</td><td class="num">45</td><td>20 NEET units, Class 11-12</td></tr>
        <tr><td style="color:var(--che);font-weight:600">Chemistry</td><td class="num">45</td><td>Physical, inorganic and organic chemistry</td></tr>
        <tr><td style="color:var(--bio);font-weight:600">Botany</td><td class="num">45</td><td>Plant diversity, cell, plant physiology, genetics, ecology</td></tr>
        <tr><td style="color:var(--bio);font-weight:600">Zoology</td><td class="num">45</td><td>Animal kingdom, human physiology, reproduction, health, biotechnology</td></tr>
      </tbody></table></div>
      ${hist.length ? `<p class="note" style="margin-top:14px">Your last score: <b class="num">${hist[0].score}/${hist[0].max}</b> (${esc(hist[0].mode)}, ${esc(hist[0].date)}). See all in <a href="#progress">My progress</a>.</p>` : ''}`;
    app.querySelectorAll('[data-mode]').forEach((b) => { b.onclick = () => startMock(b.dataset.mode); });
  }

  async function startMock(mode) {
    app.innerHTML = '<p class="loading">Building your test...</p>';
    const pool = [...(await loadClass(11)), ...(await loadClass(12))].filter((q) => CH[q[1]] && CH[q[1]].neet);
    const per = MODES[mode].per;
    const ids = [];
    const sections = [];
    for (const sec of SECTIONS) {
      const byCh = {};
      for (const q of pool) if (sec.test(CH[q[1]])) (byCh[q[1]] = byCh[q[1]] || []).push(q);
      const lists = shuffle(Object.values(byCh)).map(shuffle);
      const picked = [];
      while (picked.length < per && lists.some((l) => l.length)) for (const l of lists) { if (l.length && picked.length < per) picked.push(l.pop()[0]); }
      sections.push({ key: sec.key, start: ids.length, n: picked.length });
      ids.push(...shuffle(picked));
    }
    mock = { mode, ids, sections, answers: {}, review: {}, cur: 0, start: Date.now(), mins: MODES[mode].mins, done: false };
    store.set('nh-mock-live', mock);
    renderTest();
  }

  const secOf = (i) => mock.sections.find((s) => i >= s.start && i < s.start + s.n);

  function renderTest() {
    const i = mock.cur;
    const q = BYID[mock.ids[i]];
    const sec = secOf(i);
    const secDef = SECTIONS.find((s) => s.key === sec.key);
    const ans = mock.answers[i];
    const answered = Object.keys(mock.answers).length;
    app.innerHTML = `
      <div class="testbar">
        <div class="stabs">${mock.sections.map((s) => `<button class="stab ${s === sec ? 'on' : ''}" style="--c:${SECTIONS.find((d) => d.key === s.key).c}" data-sec="${s.start}">${s.key}</button>`).join('')}</div>
        <div class="row"><span class="timer num" id="timer"></span><button class="btn small" id="submit">Submit</button></div>
      </div>
      <div id="confirm"></div>
      <div class="test">
        <div class="qcard">
          <div class="qhead"><span class="eyebrow num" style="color:${secDef.c}">${sec.key} · Question ${i + 1} of ${mock.ids.length}</span><span class="eyebrow">${esc(CH[q[1]].title)}</span></div>
          <p class="qtext">${esc(q[3])}</p>
          <div class="opts">${q[4].map((o, k) => `<button class="opt ${ans === k ? 'sel' : ''}" data-k="${k}"><span class="l">${'ABCD'[k]}</span><span>${esc(o)}</span></button>`).join('')}</div>
          <div class="qfoot">
            <div class="row"><button class="btn small" id="prev" ${i === 0 ? 'disabled' : ''}>Previous</button><button class="btn small" id="clear">Clear answer</button></div>
            <div class="row"><button class="btn small" id="rev">${mock.review[i] ? 'Unmark review' : 'Mark for review'}</button><button class="btn primary small" id="nxt">${i + 1 < mock.ids.length ? 'Save & next' : 'Save'}</button></div>
          </div>
        </div>
        <aside class="omr">
          <p class="eyebrow" style="margin:0 0 8px">${sec.key} answer sheet · ${answered}/${mock.ids.length} answered</p>
          <div class="omr-grid">${Array.from({ length: sec.n }, (_, k) => {
            const j = sec.start + k;
            return `<button class="bub ${mock.answers[j] !== undefined ? 'ans' : ''} ${mock.review[j] ? 'rev' : ''} ${j === i ? 'cur' : ''}" data-j="${j}" aria-label="Question ${j + 1}">${j + 1}</button>`;
          }).join('')}</div>
          <div class="legend"><span>● filled = answered</span><span style="color:var(--mark)">◯ gold = for review</span></div>
        </aside>
      </div>`;
    const save = () => store.set('nh-mock-live', mock);
    const go = (j) => { mock.cur = Math.max(0, Math.min(mock.ids.length - 1, j)); save(); renderTest(); };
    app.querySelectorAll('.opt').forEach((b) => { b.onclick = () => { mock.answers[i] = Number(b.dataset.k); save(); renderTest(); }; });
    app.querySelectorAll('.bub').forEach((b) => { b.onclick = () => go(Number(b.dataset.j)); });
    app.querySelectorAll('[data-sec]').forEach((b) => { b.onclick = () => go(Number(b.dataset.sec)); });
    $('#prev').onclick = () => go(i - 1);
    $('#nxt').onclick = () => go(i + 1);
    $('#clear').onclick = () => { delete mock.answers[i]; save(); renderTest(); };
    $('#rev').onclick = () => { if (mock.review[i]) delete mock.review[i]; else mock.review[i] = 1; save(); go(i + 1); };
    $('#submit').onclick = () => {
      $('#confirm').innerHTML = `<div class="confirm row"><span>Submit now? You have answered <b class="num">${answered}</b> of ${mock.ids.length}. Unanswered questions score 0.</span>
        <button class="btn small primary" id="yes">Submit test</button><button class="btn small" id="no">Keep going</button></div>`;
      $('#yes').onclick = finishMock;
      $('#no').onclick = () => { $('#confirm').innerHTML = ''; };
    };
    tick();
    clearInterval(timerId);
    timerId = setInterval(tick, 1000);
  }

  function tick() {
    if (!mock || mock.done) { clearInterval(timerId); return; }
    const left = Math.max(0, mock.start + mock.mins * 60000 - Date.now());
    const el = $('#timer');
    if (el) {
      const s = Math.floor(left / 1000);
      el.textContent = `${Math.floor(s / 3600)}:${String(Math.floor((s % 3600) / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
      el.classList.toggle('low', left < 5 * 60000);
    }
    if (left <= 0) finishMock();
  }

  function finishMock() {
    clearInterval(timerId);
    const per = {};
    let score = 0;
    mock.ids.forEach((id, i) => {
      const q = BYID[id];
      const sec = secOf(i).key;
      const p = per[sec] || (per[sec] = { c: 0, w: 0, u: 0 });
      const a = mock.answers[i];
      if (a === undefined) p.u++;
      else if (a === q[5]) { p.c++; score += 4; record(q, true); }
      else { p.w++; score -= 1; record(q, false); }
    });
    mock.done = true;
    mock.result = { score, max: mock.ids.length * 4, per, secs: Math.round((Date.now() - mock.start) / 1000) };
    const hist = store.get('nh-mocks', []);
    hist.unshift({ date: new Date().toLocaleDateString('en-IN'), mode: MODES[mock.mode].label, score, max: mock.result.max, per });
    store.set('nh-mocks', hist.slice(0, 30));
    store.set('nh-mock-live', mock);
    renderResult();
  }

  function renderResult() {
    const r = mock.result;
    const wrongOrBlank = mock.ids.map((id, i) => ({ q: BYID[id], i, a: mock.answers[i] })).filter((x) => x.q && x.a !== x.q[5]);
    app.innerHTML = `
      <p class="eyebrow">${esc(MODES[mock.mode].label)} · result</p>
      <h1><span class="num">${r.score}</span> / <span class="num">${r.max}</span></h1>
      <p class="lead">Time used: <span class="num">${Math.floor(r.secs / 60)} min</span>. Marking: +4 correct, -1 wrong, 0 blank.</p>
      <div class="score-grid">${mock.sections.map((s) => {
        const p = r.per[s.key] || { c: 0, w: 0, u: 0 };
        return `<div class="tile" style="--c:${SECTIONS.find((d) => d.key === s.key).c}"><span>${s.key}</span><b class="num">${p.c * 4 - p.w}</b><span class="num">${p.c} right · ${p.w} wrong · ${p.u} blank</span></div>`;
      }).join('')}</div>
      <div class="row" style="margin-bottom:18px"><button class="btn primary" id="newmock">Take another test</button><a class="btn" href="#progress">My progress</a></div>
      <h2>Review: ${wrongOrBlank.length} to learn from</h2>
      <div style="display:grid;gap:10px">${wrongOrBlank.map(({ q, i, a }) => `
        <div class="qcard"><p class="eyebrow">Q${i + 1} · ${esc(CH[q[1]].title)}</p><p class="qtext" style="font-size:17px">${esc(q[3])}</p>
        <div class="explain ${a === undefined ? '' : 'bad'}"><b>${a === undefined ? 'Left blank.' : `You chose ${'ABCD'[a]}. ${esc(q[4][a])}`} Answer: ${'ABCD'[q[5]]}. ${esc(q[4][q[5]])}</b>${esc(q[6])}</div></div>`).join('')}</div>`;
    $('#newmock').onclick = () => { mock = null; store.set('nh-mock-live', null); viewMock(); };
  }

  // ---------------------------------------------------------------- progress
  function viewProgress() {
    const agg = chapterAgg();
    const bySub = {};
    for (const [cid, a] of Object.entries(agg)) {
      const c = CH[cid];
      if (!c) continue;
      const b = bySub[c.subject] || (bySub[c.subject] = { seen: 0, tries: 0, correct: 0 });
      b.seen += a.seen; b.tries += a.tries; b.correct += a.correct;
    }
    const seen = Object.keys(stats).length;
    const tries = Object.values(stats).reduce((n, s) => n + s[0], 0);
    const correct = Object.values(stats).reduce((n, s) => n + s[1], 0);
    const weak = Object.entries(agg).filter(([cid, a]) => CH[cid] && a.tries >= 5).map(([cid, a]) => ({ c: CH[cid], acc: pct(a.correct, a.tries), a }))
      .sort((x, y) => x.acc - y.acc).slice(0, 8);
    const hist = store.get('nh-mocks', []);
    app.innerHTML = `
      <p class="eyebrow">Saved on this device</p>
      <h1>My progress</h1>
      <div class="score-grid">
        <div class="tile"><span>Questions tried</span><b class="num">${seen.toLocaleString('en-IN')}</b><span>of ${INDEX.chapters.reduce((n, c) => n + c.count, 0).toLocaleString('en-IN')}</span></div>
        ${['Physics', 'Chemistry', 'Biology'].map((s) => { const b = bySub[s]; return `<div class="tile" style="--c:${SUBJ[s]}"><span>${s}</span><b class="num">${b ? pct(b.correct, b.tries) + '%' : '-'}</b><span class="num">${b ? `${b.seen} questions tried` : 'not started'}</span></div>`; }).join('')}
      </div>
      <p class="note">Overall accuracy: <b class="num">${pct(correct, tries)}%</b> over ${tries.toLocaleString('en-IN')} answers.</p>
      <h2 style="margin-top:20px">Chapters to work on</h2>
      ${weak.length ? `<ul class="weak">${weak.map(({ c, acc, a }) => `<li style="--c:${SUBJ[c.subject]}"><div><b>${esc(c.title)}</b><div class="note">Class ${c.cls} ${esc(c.subject)} · ${acc}% correct over ${a.tries} answers</div></div><a class="btn small" href="#practice-${c.id}">Practise</a></li>`).join('')}</ul>`
        : '<p class="note">Answer at least 5 questions in a chapter and your weakest chapters will appear here.</p>'}
      <h2 style="margin-top:20px">Mock test history</h2>
      ${hist.length ? `<div class="scroll-x"><table class="hist"><thead><tr><th>Date</th><th>Test</th><th>Score</th><th>Physics</th><th>Chemistry</th><th>Botany</th><th>Zoology</th></tr></thead><tbody>
        ${hist.map((h) => `<tr><td>${esc(h.date)}</td><td>${esc(h.mode)}</td><td class="num"><b>${h.score}</b>/${h.max}</td>${['Physics', 'Chemistry', 'Botany', 'Zoology'].map((k) => `<td class="num">${h.per[k] ? h.per[k].c * 4 - h.per[k].w : '-'}</td>`).join('')}</tr>`).join('')}
      </tbody></table></div>` : '<p class="note">No mock tests yet. <a href="#mock">Take one</a>.</p>'}
      <div style="margin-top:28px"><button class="btn small" id="reset">Erase my progress</button><span id="resetc"></span></div>`;
    $('#reset').onclick = () => {
      $('#resetc').innerHTML = ` <span class="note">Erase all answers and mock history on this device?</span> <button class="btn small primary" id="ry">Yes, erase</button> <button class="btn small" id="rn">Keep</button>`;
      $('#ry').onclick = () => { stats = {}; mock = null; store.set('nh-stats', {}); store.set('nh-mocks', []); store.set('nh-mock-live', null); viewProgress(); };
      $('#rn').onclick = () => { $('#resetc').innerHTML = ''; };
    };
  }

  loadIndex().then(route).catch(() => { app.innerHTML = '<p class="loading">The question data could not be loaded. Please check your connection and reload.</p>'; });
})();
