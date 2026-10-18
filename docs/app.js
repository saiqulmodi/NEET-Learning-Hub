// NEET Learning Hub: Class 1 -> 12 -> NEET path, revision notes, chapter practice (incl. NEET formats),
// NEET-pattern mocks, a weekly Mock Day with a score chart, and progress. UI in English, Hindi and Bengali.
// A question is [id, chapterId, difficulty E/M/H, text, [A, B, C, D], correctIndex, explanation, fromSchoolBank, type].
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const shuffle = (a, rnd = Math.random) => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const SUBJ = { Physics: 'var(--phy)', Chemistry: 'var(--che)', Biology: 'var(--bio)' };
  const SECTIONS = [
    { key: 'Physics', test: (c) => c.subject === 'Physics', c: 'var(--phy)' },
    { key: 'Chemistry', test: (c) => c.subject === 'Chemistry', c: 'var(--che)' },
    { key: 'Botany', test: (c) => c.subject === 'Biology' && c.branch === 'Botany', c: 'var(--bio)' },
    { key: 'Zoology', test: (c) => c.subject === 'Biology' && c.branch === 'Zoology', c: 'var(--bio)' },
  ];
  const MODES = { weekly: { per: 45, mins: 180 }, full: { per: 45, mins: 180 }, half: { per: 23, mins: 90 }, quick: { per: 12, mins: 48 } };
  const ECOS_URL = 'https://saiqulmodi.github.io/EcosSynthetica/';
  const ISSUES = 'https://github.com/saiqulmodi/NEET-Learning-Hub/issues/new';

  // ---------------------------------------------------------------- language
  const LANGS = { en: 'English', hi: 'हिन्दी', bn: 'বাংলা' };
  const T = {
    en: {
      'nav.path': 'Path', 'nav.mock': 'Mock test', 'nav.progress': 'My progress', 'brand.sub': 'Class 1 → 12 → MBBS',
      'disc.short': 'Answers are AI-generated. Please confirm them with your mentor or teacher.',
      'disc.long': 'Practice material, not official NTA or NCERT content. Answers and explanations are AI-generated and may contain mistakes: confirm doubtful answers with your mentor or teacher, and treat the NCERT textbook as the final authority.',
      'disc.report': 'Report a problem with this question',
      'loading': 'Loading the question hub...', 'loadingQ': 'Loading questions...', 'loadFail': 'The question data could not be loaded. Please check your connection and reload.',
      'sub.Physics': 'Physics', 'sub.Chemistry': 'Chemistry', 'sub.Biology': 'Biology', 'sub.Botany': 'Botany', 'sub.Zoology': 'Zoology',
      'path.eyebrow': 'Biology · Chemistry · Physics', 'path.h1': 'From Class 1 to the NEET hall',
      'path.lead': '{total} questions with answers and explanations, arranged by class and chapter. Classes 1-10 build the foundation; Class 11-12 chapters follow the NCERT books and the official NEET-UG units ({neet} questions, including assertion-reason, match-the-list and multi-statement questions). Revise a chapter, practise it, then take the weekly NEET mock.',
      'rung.class': 'Class', 'rung.exam': 'Exam', 'rung.mock': 'mock',
      'cls.neet': 'NEET syllabus', 'cls.sci': 'Science foundation', 'cls.evs': 'EVS foundation',
      'next.class': 'Next: Class {n}', 'next.mock': 'Next: NEET mock test', 'qcount': '{n} questions', 'unit': 'NEET unit {n}: ',
      'beyond': 'beyond NEET', 'practise': 'Practise', 'revise': 'Revise', 'formats': 'NEET formats',
      'meta.q': '{n} Q', 'meta.done': '{n} done', 'meta.correct': '{n}% correct', 'meta.fmt': '{n} NEET-format', 'ecos': 'Play in Ecos-Synthetica',
      'notes.eyebrow': 'Revision notes', 'notes.lead': 'Read these key points, then practise the chapter.', 'notes.practise': 'Practise this chapter',
      'notes.formats': 'Practise NEET-format questions', 'back.class': 'Back to Class {n}', 'notes.none': 'Revision notes are not available for this chapter yet.',
      'q.of': 'Question {i} of {n}', 'q.correct': 'Correct', 'q.answer': 'Answer: {a}.', 'q.next': 'Next question', 'q.score': 'See my score',
      'q.bank': 'From the School MCQ Bank', 'q.hub': 'NEET Hub question', 'q.diff': 'difficulty {d}', 'd.E': 'easy', 'd.M': 'medium', 'd.H': 'hard',
      'q.english': 'Questions are in English.', 'type.ar': 'Assertion-Reason', 'type.match': 'Match the list', 'type.multi': 'Statements',
      'sum.all': 'All correct. Try a NEET mock to test it under time pressure.', 'sum.good': 'Good work. Practise again to clear the ones you missed.',
      'sum.low': 'Read the explanations and the revision notes, then practise again; missed questions come back first.', 'sum.more': 'Practise 10 more',
      'sum.formats': 'NEET-format practice',
      'mock.eyebrow': 'NEET-UG pattern', 'mock.h1': 'Mock tests',
      'mock.lead': 'Questions come from every NEET chapter of Class 11 and 12, spread evenly across chapters, including assertion-reason, match-the-list and statement questions. Marking follows NEET: +4 correct, -1 wrong, 0 blank. Your test is saved as you go.',
      'mode.weekly': 'Mock Day paper', 'mode.full': 'Full NEET mock', 'mode.half': 'Half mock', 'mode.quick': 'Quick test',
      'mode.desc': '{n} questions · {m} minutes · maximum {x} marks', 'mode.start': 'Start',
      'tbl.section': 'Section', 'tbl.full': 'Full mock', 'tbl.covers': 'Covers',
      'cov.P': '20 NEET units, Class 11-12', 'cov.C': 'Physical, inorganic and organic chemistry',
      'cov.B': 'Plant diversity, cell, plant physiology, genetics, ecology', 'cov.Z': 'Animal kingdom, human physiology, reproduction, health, biotechnology',
      'day.eyebrow': 'Mock Day', 'day.week': 'Week {w} paper · {range}',
      'day.lead': 'Everyone gets the same full-length paper this week, so scores can be compared. Take it on Sunday, like the real exam day, and watch your score climb week by week.',
      'day.take': "Take this week's paper", 'day.done': "You scored {s}/{m} on this week's paper.", 'day.next': 'A new paper arrives on Monday.',
      'day.streak': 'Weekly streak: {n}', 'day.resume': 'Resume your test',
      'chart.title': 'Full-length mock scores (out of 720)', 'chart.empty': 'Take a full-length mock to start your chart.', 'chart.tip': '{d}: {s}/720',
      'last': 'Your last score: {s}/{m} ({mode}, {d}).',
      'test.submit': 'Submit', 'test.prev': 'Previous', 'test.clear': 'Clear answer', 'test.mark': 'Mark for review', 'test.unmark': 'Unmark review',
      'test.next': 'Save & next', 'test.save': 'Save', 'test.sheet': '{s} answer sheet · {a}/{n} answered', 'test.legend1': '● filled = answered', 'test.legend2': '◯ gold = for review',
      'test.confirm': 'Submit now? You have answered {a} of {n}. Unanswered questions score 0.', 'test.yes': 'Submit test', 'test.no': 'Keep going',
      'res.eyebrow': '{mode} · result', 'res.time': 'Time used: {m} min. Marking: +4 correct, -1 wrong, 0 blank.', 'res.tile': '{c} right · {w} wrong · {u} blank',
      'res.another': 'Take another test', 'res.review': 'Review: {n} to learn from', 'res.blank': 'Left blank.', 'res.chose': 'You chose {x}.',
      'pr.eyebrow': 'Saved on this device', 'pr.h1': 'My progress', 'pr.tried': 'Questions tried', 'pr.of': 'of {n}', 'pr.notstarted': 'not started',
      'pr.subtried': '{n} questions tried', 'pr.overall': 'Overall accuracy: {p}% over {n} answers.', 'pr.weak': 'Chapters to work on',
      'pr.weakline': 'Class {c} {s} · {p}% correct over {n} answers', 'pr.weaknone': 'Answer at least 5 questions in a chapter and your weakest chapters will appear here.',
      'pr.hist': 'Mock test history', 'pr.date': 'Date', 'pr.test': 'Test', 'pr.score': 'Score', 'pr.nohist': 'No mock tests yet.', 'pr.take': 'Take one',
      'pr.erase': 'Erase my progress', 'pr.eraseq': 'Erase all answers and mock history on this device?', 'pr.yes': 'Yes, erase', 'pr.keep': 'Keep',
      'lang': 'Language',
    },
    hi: {
      'nav.path': 'राह', 'nav.mock': 'मॉक टेस्ट', 'nav.progress': 'मेरी प्रगति', 'brand.sub': 'कक्षा 1 → 12 → MBBS',
      'disc.short': 'उत्तर AI द्वारा बनाए गए हैं। कृपया अपने मेंटर या शिक्षक से पुष्टि करें।',
      'disc.long': 'यह अभ्यास सामग्री है, NTA या NCERT की आधिकारिक सामग्री नहीं। उत्तर और व्याख्याएँ AI द्वारा बनाई गई हैं और इनमें गलतियाँ हो सकती हैं: संदेह वाले उत्तर अपने मेंटर या शिक्षक से जाँचें, और NCERT पुस्तक को अंतिम प्रमाण मानें।',
      'disc.report': 'इस प्रश्न में समस्या बताएँ',
      'loading': 'प्रश्न हब लोड हो रहा है...', 'loadingQ': 'प्रश्न लोड हो रहे हैं...', 'loadFail': 'प्रश्न डेटा लोड नहीं हो सका। कृपया इंटरनेट जाँचकर फिर से लोड करें।',
      'sub.Physics': 'भौतिकी', 'sub.Chemistry': 'रसायन विज्ञान', 'sub.Biology': 'जीव विज्ञान', 'sub.Botany': 'वनस्पति विज्ञान', 'sub.Zoology': 'प्राणि विज्ञान',
      'path.eyebrow': 'जीव विज्ञान · रसायन विज्ञान · भौतिकी', 'path.h1': 'कक्षा 1 से NEET परीक्षा हॉल तक',
      'path.lead': 'कक्षा और अध्याय के अनुसार {total} प्रश्न, उत्तर और व्याख्या सहित। कक्षा 1-10 नींव बनाती हैं; कक्षा 11-12 के अध्याय NCERT पुस्तकों और आधिकारिक NEET-UG इकाइयों पर हैं ({neet} प्रश्न, अभिकथन-कारण, सूची मिलान और कथन वाले प्रश्नों सहित)। अध्याय दोहराएँ, अभ्यास करें, फिर साप्ताहिक NEET मॉक दें।',
      'rung.class': 'कक्षा', 'rung.exam': 'परीक्षा', 'rung.mock': 'मॉक',
      'cls.neet': 'NEET पाठ्यक्रम', 'cls.sci': 'विज्ञान की नींव', 'cls.evs': 'पर्यावरण अध्ययन की नींव',
      'next.class': 'आगे: कक्षा {n}', 'next.mock': 'आगे: NEET मॉक टेस्ट', 'qcount': '{n} प्रश्न', 'unit': 'NEET इकाई {n}: ',
      'beyond': 'NEET से बाहर', 'practise': 'अभ्यास', 'revise': 'दोहराएँ', 'formats': 'NEET प्रारूप',
      'meta.q': '{n} प्रश्न', 'meta.done': '{n} हल', 'meta.correct': '{n}% सही', 'meta.fmt': '{n} NEET-प्रारूप', 'ecos': 'Ecos-Synthetica में खेलें',
      'notes.eyebrow': 'दोहराव नोट्स', 'notes.lead': 'ये मुख्य बिंदु पढ़ें, फिर अध्याय का अभ्यास करें।', 'notes.practise': 'इस अध्याय का अभ्यास करें',
      'notes.formats': 'NEET-प्रारूप प्रश्नों का अभ्यास', 'back.class': 'कक्षा {n} पर लौटें', 'notes.none': 'इस अध्याय के नोट्स अभी उपलब्ध नहीं हैं।',
      'q.of': 'प्रश्न {i} / {n}', 'q.correct': 'सही', 'q.answer': 'उत्तर: {a}।', 'q.next': 'अगला प्रश्न', 'q.score': 'मेरे अंक देखें',
      'q.bank': 'स्कूल MCQ बैंक से', 'q.hub': 'NEET हब प्रश्न', 'q.diff': 'कठिनाई: {d}', 'd.E': 'आसान', 'd.M': 'मध्यम', 'd.H': 'कठिन',
      'q.english': 'प्रश्न अंग्रेज़ी में हैं।', 'type.ar': 'अभिकथन-कारण', 'type.match': 'सूची मिलान', 'type.multi': 'कथन',
      'sum.all': 'सब सही! समय के दबाव में जाँचने के लिए NEET मॉक दें।', 'sum.good': 'बढ़िया। छूटे प्रश्न ठीक करने के लिए फिर अभ्यास करें।',
      'sum.low': 'व्याख्याएँ और दोहराव नोट्स पढ़ें, फिर अभ्यास करें; गलत प्रश्न पहले आएँगे।', 'sum.more': '10 और अभ्यास करें',
      'sum.formats': 'NEET-प्रारूप अभ्यास',
      'mock.eyebrow': 'NEET-UG पैटर्न', 'mock.h1': 'मॉक टेस्ट',
      'mock.lead': 'प्रश्न कक्षा 11 और 12 के हर NEET अध्याय से, बराबर फैले हुए, अभिकथन-कारण, सूची मिलान और कथन प्रश्नों सहित। अंकन NEET जैसा: सही +4, गलत -1, खाली 0। आपका टेस्ट साथ-साथ सहेजा जाता है।',
      'mode.weekly': 'मॉक डे पेपर', 'mode.full': 'पूर्ण NEET मॉक', 'mode.half': 'आधा मॉक', 'mode.quick': 'त्वरित टेस्ट',
      'mode.desc': '{n} प्रश्न · {m} मिनट · अधिकतम {x} अंक', 'mode.start': 'शुरू करें',
      'tbl.section': 'खंड', 'tbl.full': 'पूर्ण मॉक', 'tbl.covers': 'विषय-वस्तु',
      'cov.P': '20 NEET इकाइयाँ, कक्षा 11-12', 'cov.C': 'भौतिक, अकार्बनिक और कार्बनिक रसायन',
      'cov.B': 'पादप विविधता, कोशिका, पादप कार्यिकी, आनुवंशिकी, पारिस्थितिकी', 'cov.Z': 'प्राणि जगत, मानव कार्यिकी, जनन, स्वास्थ्य, जैव प्रौद्योगिकी',
      'day.eyebrow': 'मॉक डे', 'day.week': 'सप्ताह {w} का पेपर · {range}',
      'day.lead': 'इस सप्ताह सबको एक ही पूर्ण पेपर मिलता है, ताकि अंकों की तुलना हो सके। इसे असली परीक्षा की तरह रविवार को दें और सप्ताह-दर-सप्ताह अपने अंक बढ़ते देखें।',
      'day.take': 'इस सप्ताह का पेपर दें', 'day.done': 'इस सप्ताह के पेपर में आपके अंक: {s}/{m}।', 'day.next': 'नया पेपर सोमवार को आएगा।',
      'day.streak': 'साप्ताहिक लगातार: {n}', 'day.resume': 'अपना टेस्ट जारी रखें',
      'chart.title': 'पूर्ण मॉक के अंक (720 में से)', 'chart.empty': 'अपना चार्ट शुरू करने के लिए एक पूर्ण मॉक दें।', 'chart.tip': '{d}: {s}/720',
      'last': 'आपके पिछले अंक: {s}/{m} ({mode}, {d})।',
      'test.submit': 'जमा करें', 'test.prev': 'पिछला', 'test.clear': 'उत्तर हटाएँ', 'test.mark': 'समीक्षा के लिए चिह्नित करें', 'test.unmark': 'चिह्न हटाएँ',
      'test.next': 'सहेजें और आगे', 'test.save': 'सहेजें', 'test.sheet': '{s} उत्तर पत्रक · {a}/{n} उत्तरित', 'test.legend1': '● भरा = उत्तरित', 'test.legend2': '◯ सुनहरा = समीक्षा हेतु',
      'test.confirm': 'अभी जमा करें? आपने {n} में से {a} उत्तर दिए हैं। खाली प्रश्नों के 0 अंक।', 'test.yes': 'टेस्ट जमा करें', 'test.no': 'जारी रखें',
      'res.eyebrow': '{mode} · परिणाम', 'res.time': 'लगा समय: {m} मिनट। अंकन: सही +4, गलत -1, खाली 0।', 'res.tile': '{c} सही · {w} गलत · {u} खाली',
      'res.another': 'एक और टेस्ट दें', 'res.review': 'समीक्षा: सीखने के लिए {n} प्रश्न', 'res.blank': 'खाली छोड़ा।', 'res.chose': 'आपने {x} चुना।',
      'pr.eyebrow': 'इस डिवाइस पर सहेजा गया', 'pr.h1': 'मेरी प्रगति', 'pr.tried': 'हल किए प्रश्न', 'pr.of': '{n} में से', 'pr.notstarted': 'शुरू नहीं',
      'pr.subtried': '{n} प्रश्न हल किए', 'pr.overall': 'कुल सटीकता: {n} उत्तरों में {p}%।', 'pr.weak': 'जिन अध्यायों पर मेहनत चाहिए',
      'pr.weakline': 'कक्षा {c} {s} · {n} उत्तरों में {p}% सही', 'pr.weaknone': 'किसी अध्याय में कम से कम 5 प्रश्न हल करें, तब कमज़ोर अध्याय यहाँ दिखेंगे।',
      'pr.hist': 'मॉक टेस्ट इतिहास', 'pr.date': 'तारीख', 'pr.test': 'टेस्ट', 'pr.score': 'अंक', 'pr.nohist': 'अभी कोई मॉक टेस्ट नहीं।', 'pr.take': 'एक दें',
      'pr.erase': 'मेरी प्रगति मिटाएँ', 'pr.eraseq': 'इस डिवाइस से सारे उत्तर और मॉक इतिहास मिटाएँ?', 'pr.yes': 'हाँ, मिटाएँ', 'pr.keep': 'रखें',
      'lang': 'भाषा',
    },
    bn: {
      'nav.path': 'পথ', 'nav.mock': 'মক টেস্ট', 'nav.progress': 'আমার অগ্রগতি', 'brand.sub': 'শ্রেণি 1 → 12 → MBBS',
      'disc.short': 'উত্তরগুলো AI দিয়ে তৈরি। অনুগ্রহ করে তোমার মেন্টর বা শিক্ষকের সঙ্গে মিলিয়ে নাও।',
      'disc.long': 'এটি অনুশীলনের উপকরণ, NTA বা NCERT-এর সরকারি বিষয়বস্তু নয়। উত্তর ও ব্যাখ্যা AI দিয়ে তৈরি এবং ভুল থাকতে পারে: সন্দেহজনক উত্তর মেন্টর বা শিক্ষকের সঙ্গে মিলিয়ে নাও, আর NCERT বইকেই চূড়ান্ত প্রমাণ মানো।',
      'disc.report': 'এই প্রশ্নে সমস্যা জানাও',
      'loading': 'প্রশ্ন হাব লোড হচ্ছে...', 'loadingQ': 'প্রশ্ন লোড হচ্ছে...', 'loadFail': 'প্রশ্নের ডেটা লোড হয়নি। ইন্টারনেট দেখে আবার লোড করো।',
      'sub.Physics': 'পদার্থবিদ্যা', 'sub.Chemistry': 'রসায়ন', 'sub.Biology': 'জীববিদ্যা', 'sub.Botany': 'উদ্ভিদবিদ্যা', 'sub.Zoology': 'প্রাণীবিদ্যা',
      'path.eyebrow': 'জীববিদ্যা · রসায়ন · পদার্থবিদ্যা', 'path.h1': 'শ্রেণি 1 থেকে NEET পরীক্ষা হল পর্যন্ত',
      'path.lead': 'শ্রেণি ও অধ্যায় অনুযায়ী {total}টি প্রশ্ন, উত্তর ও ব্যাখ্যাসহ। শ্রেণি 1-10 ভিত গড়ে; শ্রেণি 11-12-র অধ্যায় NCERT বই ও সরকারি NEET-UG ইউনিট অনুসরণ করে ({neet}টি প্রশ্ন, বিবৃতি-কারণ, তালিকা মেলানো ও একাধিক বিবৃতির প্রশ্নসহ)। অধ্যায় ঝালিয়ে নাও, অনুশীলন করো, তারপর সাপ্তাহিক NEET মক দাও।',
      'rung.class': 'শ্রেণি', 'rung.exam': 'পরীক্ষা', 'rung.mock': 'মক',
      'cls.neet': 'NEET পাঠ্যক্রম', 'cls.sci': 'বিজ্ঞানের ভিত', 'cls.evs': 'পরিবেশ পরিচিতির ভিত',
      'next.class': 'পরের: শ্রেণি {n}', 'next.mock': 'পরের: NEET মক টেস্ট', 'qcount': '{n}টি প্রশ্ন', 'unit': 'NEET ইউনিট {n}: ',
      'beyond': 'NEET-এর বাইরে', 'practise': 'অনুশীলন', 'revise': 'ঝালাও', 'formats': 'NEET ধরন',
      'meta.q': '{n} প্রশ্ন', 'meta.done': '{n} সমাধান', 'meta.correct': '{n}% সঠিক', 'meta.fmt': '{n} NEET-ধরন', 'ecos': 'Ecos-Synthetica-য় খেলো',
      'notes.eyebrow': 'ঝালাই নোট', 'notes.lead': 'এই মূল বিষয়গুলো পড়ো, তারপর অধ্যায়টি অনুশীলন করো।', 'notes.practise': 'এই অধ্যায় অনুশীলন করো',
      'notes.formats': 'NEET-ধরনের প্রশ্ন অনুশীলন', 'back.class': 'শ্রেণি {n}-এ ফেরো', 'notes.none': 'এই অধ্যায়ের নোট এখনও নেই।',
      'q.of': 'প্রশ্ন {i} / {n}', 'q.correct': 'সঠিক', 'q.answer': 'উত্তর: {a}।', 'q.next': 'পরের প্রশ্ন', 'q.score': 'আমার নম্বর দেখো',
      'q.bank': 'স্কুল MCQ ব্যাংক থেকে', 'q.hub': 'NEET হাবের প্রশ্ন', 'q.diff': 'কাঠিন্য: {d}', 'd.E': 'সহজ', 'd.M': 'মাঝারি', 'd.H': 'কঠিন',
      'q.english': 'প্রশ্নগুলো ইংরেজিতে।', 'type.ar': 'বিবৃতি-কারণ', 'type.match': 'তালিকা মেলানো', 'type.multi': 'বিবৃতি',
      'sum.all': 'সব ঠিক! সময়ের চাপে যাচাই করতে NEET মক দাও।', 'sum.good': 'দারুণ। ভুলগুলো ঠিক করতে আবার অনুশীলন করো।',
      'sum.low': 'ব্যাখ্যা ও ঝালাই নোট পড়ো, তারপর আবার অনুশীলন করো; ভুল প্রশ্নগুলো আগে আসবে।', 'sum.more': 'আরও 10টি অনুশীলন',
      'sum.formats': 'NEET-ধরনের অনুশীলন',
      'mock.eyebrow': 'NEET-UG ধাঁচ', 'mock.h1': 'মক টেস্ট',
      'mock.lead': 'প্রশ্ন আসে শ্রেণি 11 ও 12-র প্রতিটি NEET অধ্যায় থেকে, সমানভাবে ছড়ানো, বিবৃতি-কারণ, তালিকা মেলানো ও বিবৃতির প্রশ্নসহ। নম্বর NEET-এর মতো: সঠিক +4, ভুল -1, ফাঁকা 0। টেস্ট চলতে চলতেই সংরক্ষিত হয়।',
      'mode.weekly': 'মক ডে পেপার', 'mode.full': 'পূর্ণ NEET মক', 'mode.half': 'অর্ধেক মক', 'mode.quick': 'দ্রুত টেস্ট',
      'mode.desc': '{n}টি প্রশ্ন · {m} মিনিট · সর্বোচ্চ {x} নম্বর', 'mode.start': 'শুরু করো',
      'tbl.section': 'বিভাগ', 'tbl.full': 'পূর্ণ মক', 'tbl.covers': 'বিষয়',
      'cov.P': '20টি NEET ইউনিট, শ্রেণি 11-12', 'cov.C': 'ভৌত, অজৈব ও জৈব রসায়ন',
      'cov.B': 'উদ্ভিদ বৈচিত্র্য, কোষ, উদ্ভিদ শারীরবিদ্যা, বংশগতি, বাস্তুবিদ্যা', 'cov.Z': 'প্রাণীজগৎ, মানব শারীরবিদ্যা, জনন, স্বাস্থ্য, জৈবপ্রযুক্তি',
      'day.eyebrow': 'মক ডে', 'day.week': 'সপ্তাহ {w}-এর পেপার · {range}',
      'day.lead': 'এই সপ্তাহে সবাই একই পূর্ণ পেপার পায়, তাই নম্বর তুলনা করা যায়। আসল পরীক্ষার মতো রবিবারে দাও, আর সপ্তাহে সপ্তাহে নম্বর বাড়তে দেখো।',
      'day.take': 'এই সপ্তাহের পেপার দাও', 'day.done': 'এই সপ্তাহের পেপারে তোমার নম্বর: {s}/{m}।', 'day.next': 'নতুন পেপার আসবে সোমবার।',
      'day.streak': 'টানা সপ্তাহ: {n}', 'day.resume': 'তোমার টেস্ট চালিয়ে যাও',
      'chart.title': 'পূর্ণ মকের নম্বর (720-এর মধ্যে)', 'chart.empty': 'চার্ট শুরু করতে একটি পূর্ণ মক দাও।', 'chart.tip': '{d}: {s}/720',
      'last': 'তোমার শেষ নম্বর: {s}/{m} ({mode}, {d})।',
      'test.submit': 'জমা দাও', 'test.prev': 'আগের', 'test.clear': 'উত্তর মোছো', 'test.mark': 'পর্যালোচনার জন্য চিহ্ন দাও', 'test.unmark': 'চিহ্ন সরাও',
      'test.next': 'সংরক্ষণ ও পরের', 'test.save': 'সংরক্ষণ', 'test.sheet': '{s} উত্তরপত্র · {a}/{n} উত্তর দেওয়া', 'test.legend1': '● ভরা = উত্তর দেওয়া', 'test.legend2': '◯ সোনালি = পর্যালোচনার জন্য',
      'test.confirm': 'এখনই জমা দেবে? {n}টির মধ্যে {a}টির উত্তর দিয়েছ। ফাঁকা প্রশ্নে 0।', 'test.yes': 'টেস্ট জমা দাও', 'test.no': 'চালিয়ে যাও',
      'res.eyebrow': '{mode} · ফল', 'res.time': 'সময় লেগেছে: {m} মিনিট। নম্বর: সঠিক +4, ভুল -1, ফাঁকা 0।', 'res.tile': '{c} সঠিক · {w} ভুল · {u} ফাঁকা',
      'res.another': 'আরেকটি টেস্ট দাও', 'res.review': 'পর্যালোচনা: শেখার জন্য {n}টি', 'res.blank': 'ফাঁকা রেখেছ।', 'res.chose': 'তুমি {x} বেছেছিলে।',
      'pr.eyebrow': 'এই ডিভাইসে সংরক্ষিত', 'pr.h1': 'আমার অগ্রগতি', 'pr.tried': 'চেষ্টা করা প্রশ্ন', 'pr.of': '{n}-এর মধ্যে', 'pr.notstarted': 'শুরু হয়নি',
      'pr.subtried': '{n}টি প্রশ্ন চেষ্টা', 'pr.overall': 'মোট নির্ভুলতা: {n}টি উত্তরে {p}%।', 'pr.weak': 'যে অধ্যায়ে আরও কাজ দরকার',
      'pr.weakline': 'শ্রেণি {c} {s} · {n}টি উত্তরে {p}% সঠিক', 'pr.weaknone': 'কোনো অধ্যায়ে অন্তত 5টি প্রশ্নের উত্তর দিলে দুর্বল অধ্যায়গুলো এখানে দেখাবে।',
      'pr.hist': 'মক টেস্টের ইতিহাস', 'pr.date': 'তারিখ', 'pr.test': 'টেস্ট', 'pr.score': 'নম্বর', 'pr.nohist': 'এখনও কোনো মক টেস্ট নেই।', 'pr.take': 'একটি দাও',
      'pr.erase': 'আমার অগ্রগতি মোছো', 'pr.eraseq': 'এই ডিভাইস থেকে সব উত্তর ও মক ইতিহাস মুছবে?', 'pr.yes': 'হ্যাঁ, মোছো', 'pr.keep': 'রাখো',
      'lang': 'ভাষা',
    },
  };

  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* storage blocked: progress lasts this visit */ } },
  };
  let lang = store.get('nh-lang', 'en');
  if (!LANGS[lang]) lang = 'en';
  const t = (k, v = {}) => { let s = (T[lang] && T[lang][k]) ?? T.en[k] ?? k; for (const [a, b] of Object.entries(v)) s = s.split(`{${a}}`).join(b); return s; };
  const num = (n) => Number(n).toLocaleString('en-IN');
  const chTitle = (c) => (lang !== 'en' && c.t && c.t[lang]) || c.title;
  const unitTitle = (c) => (lang !== 'en' && c.ut && c.ut[lang]) || c.unitTitle;
  const sub = (s) => t('sub.' + s);
  const modeLabel = (m) => t('mode.' + m);

  let INDEX = null;
  let NOTES = null;
  const CH = {};
  const DATA = {};
  const BYID = {};
  let stats = store.get('nh-stats', {});
  let session = null;
  let mock = store.get('nh-mock-live', null);
  let timerId = null;
  const app = $('#app');

  async function loadIndex() {
    INDEX = await (await fetch('data/index.json')).json();
    for (const c of INDEX.chapters) CH[c.id] = c;
  }
  async function loadNotes() {
    if (!NOTES) NOTES = await (await fetch('data/notes.json')).json();
    return NOTES;
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
    for (const [, [tr, c, cid]] of Object.entries(stats)) {
      const a = agg[cid] || (agg[cid] = { seen: 0, tries: 0, correct: 0 });
      a.seen++; a.tries += tr; a.correct += c;
    }
    return agg;
  }
  const pct = (a, b) => (b ? Math.round((100 * a) / b) : 0);

  // ---------------------------------------------------------------- week helpers (Mock Day)
  function isoWeek(d = new Date()) {
    const x = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
    const day = x.getUTCDay() || 7;
    x.setUTCDate(x.getUTCDate() + 4 - day);
    const y0 = new Date(Date.UTC(x.getUTCFullYear(), 0, 1));
    return { year: x.getUTCFullYear(), week: Math.ceil(((x - y0) / 86400000 + 1) / 7) };
  }
  function weekRange(d = new Date()) {
    const mon = new Date(d); mon.setDate(d.getDate() - ((d.getDay() + 6) % 7));
    const sun = new Date(mon); sun.setDate(mon.getDate() + 6);
    const f = (x) => x.toLocaleDateString(lang === 'en' ? 'en-IN' : lang === 'hi' ? 'hi-IN' : 'bn-IN', { day: 'numeric', month: 'short' });
    return `${f(mon)} - ${f(sun)}`;
  }
  const weekKey = () => { const w = isoWeek(); return `${w.year}-W${String(w.week).padStart(2, '0')}`; };
  function seeded(seed) {
    let a = seed >>> 0;
    return () => { a = (a + 0x6D2B79F5) >>> 0; let x = a; x = Math.imul(x ^ (x >>> 15), x | 1); x ^= x + Math.imul(x ^ (x >>> 7), x | 61); return ((x ^ (x >>> 14)) >>> 0) / 4294967296; };
  }

  // ---------------------------------------------------------------- shared pieces
  function chrome() {
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-t]').forEach((el) => { el.textContent = t(el.dataset.t); });
    $('#langPick').innerHTML = Object.entries(LANGS).map(([k, v]) => `<option value="${k}" ${k === lang ? 'selected' : ''}>${v}</option>`).join('');
    $('#footDisc').textContent = t('disc.long');
  }
  $('#langPick').addEventListener('change', (e) => { lang = e.target.value; store.set('nh-lang', lang); chrome(); route(); });

  // Question text: lines; "a || b" lines become a two-column list table (match-the-list).
  function qhtml(text) {
    const lines = text.split('\n');
    let out = '';
    let rows = [];
    const flush = () => {
      if (!rows.length) return;
      const [head, ...body] = rows;
      out += `<div class="scroll-x"><table class="mtable"><thead><tr><th>${esc(head[0])}</th><th>${esc(head[1])}</th></tr></thead><tbody>${body.map((r) => `<tr><td>${esc(r[0])}</td><td>${esc(r[1])}</td></tr>`).join('')}</tbody></table></div>`;
      rows = [];
    };
    for (const l of lines) {
      if (l.includes(' || ')) rows.push(l.split(' || '));
      else { flush(); out += `<p>${esc(l)}</p>`; }
    }
    flush();
    return out;
  }
  const typeTag = (q) => (q[8] && q[8] !== 'mcq' ? `<span class="ttag">${esc(t('type.' + q[8]))}</span>` : '');
  const reportLink = (q) => {
    const c = CH[q[1]];
    const body = `Question id: ${q[0]}\nChapter: ${c ? c.title : q[1]}\n\nQuestion: ${q[3]}\n\nWhat looks wrong?\n`;
    return `<a class="report" href="${ISSUES}?title=${encodeURIComponent('Question ' + q[0] + ' - possible error')}&body=${encodeURIComponent(body)}" target="_blank" rel="noopener">${esc(t('disc.report'))}</a>`;
  };
  const discLine = () => `<p class="disc">${esc(t('disc.short'))}</p>`;

  // ---------------------------------------------------------------- routing
  function route() {
    clearInterval(timerId);
    const h = location.hash.slice(1) || 'path';
    document.querySelectorAll('[data-nav]').forEach((a) => a.classList.toggle('on', h.startsWith(a.dataset.nav) || (a.dataset.nav === 'path' && /^(class|practice|notes)/.test(h))));
    if (h.startsWith('class-')) { store.set('nh-class', Number(h.slice(6))); return viewPath(); }
    if (h.startsWith('notes-')) return viewNotes(h.slice(6));
    if (h.startsWith('practicex-')) return viewPractice(h.slice(10), true);
    if (h.startsWith('practice-')) return viewPractice(h.slice(9), false);
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
      rungs.push(`<a class="rung ${k === cls ? 'on' : ''}" href="#class-${k}"><span>${esc(t('rung.class'))}</span><b>${k}</b><span class="num">${cnt}</span><div class="bar"><i style="width:${pct(seen, cnt)}%"></i></div></a>`);
    }
    rungs.push(`<a class="rung neet" href="#mock"><span>${esc(t('rung.exam'))}</span><b>NEET</b><span>${esc(t('rung.mock'))}</span></a>`);

    const chs = INDEX.chapters.filter((c) => c.cls === cls);
    const subjects = ['Physics', 'Chemistry', 'Biology'].filter((s) => chs.some((c) => c.subject === s));
    const cols = subjects.map((s) => {
      const list = chs.filter((c) => c.subject === s);
      const n = list.reduce((a, c) => a + c.count, 0);
      let lastUnit = null;
      const rows = list.map((c) => {
        const a = agg[c.id] || { seen: 0, tries: 0, correct: 0 };
        const unit = cls >= 11 && c.unitTitle !== lastUnit ? `<div class="unit">${c.neet ? esc(t('unit', { n: c.unit })) : ''}${esc(unitTitle(c))}</div>` : '';
        lastUnit = c.unitTitle;
        const nfmt = c.types ? (c.types.ar || 0) + (c.types.match || 0) + (c.types.multi || 0) : 0;
        return `${unit}<div class="ch">
          <div class="ch-title">${esc(chTitle(c))} ${c.neet || cls < 11 ? '' : `<span class="tag-beyond">${esc(t('beyond'))}</span>`}</div>
          <div class="ch-btns">${c.notes ? `<a class="btn small" href="#notes-${c.id}">${esc(t('revise'))}</a>` : ''}<a class="btn small" href="#practice-${c.id}">${esc(t('practise'))}</a></div>
          <div class="ch-meta"><span class="num">${esc(t('meta.q', { n: c.count }))}</span><span class="num">${esc(t('meta.done', { n: a.seen }))}</span>${a.tries ? `<span class="num">${esc(t('meta.correct', { n: pct(a.correct, a.tries) }))}</span>` : ''}${nfmt ? `<a class="fmt" href="#practicex-${c.id}">${esc(t('meta.fmt', { n: nfmt }))}</a>` : ''}${c.ecos ? `<a class="ecos" href="${ECOS_URL}" target="_blank" rel="noopener">${esc(t('ecos'))}</a>` : ''}</div>
          <div class="prog"><i style="width:${pct(a.seen, c.count)}%"></i></div>
        </div>`;
      }).join('');
      return `<section class="subj" style="--c:${SUBJ[s]}"><header><h2>${esc(sub(s))}</h2><span class="eyebrow num">${esc(t('qcount', { n: num(n) }))}</span></header>${rows}</section>`;
    }).join('');

    app.innerHTML = `
      <p class="eyebrow">${esc(t('path.eyebrow'))}</p>
      <h1>${esc(t('path.h1'))}</h1>
      <p class="lead">${esc(t('path.lead', { total: num(total), neet: num(neetTotal) }))}</p>
      <div class="banner">${esc(t('disc.short'))}${lang !== 'en' ? ` ${esc(t('q.english'))}` : ''}</div>
      <div class="ladder">${rungs.join('')}</div>
      <div class="row" style="justify-content:space-between;margin-bottom:12px"><h2 style="margin:0">${esc(t('rung.class'))} ${cls} · ${esc(t(cls >= 11 ? 'cls.neet' : cls >= 6 ? 'cls.sci' : 'cls.evs'))}</h2>
      ${cls < 12 ? `<a class="btn small" href="#class-${cls + 1}">${esc(t('next.class', { n: cls + 1 }))}</a>` : `<a class="btn small primary" href="#mock">${esc(t('next.mock'))}</a>`}</div>
      <div class="subjects">${cols}</div>`;
  }

  // ---------------------------------------------------------------- notes
  async function viewNotes(cid) {
    const c = CH[cid];
    if (!c) { location.hash = 'path'; return; }
    app.innerHTML = `<p class="loading">${esc(t('loading'))}</p>`;
    const notes = await loadNotes();
    const n = notes[cid];
    const pts = n ? (n[lang] && n[lang].length ? n[lang] : n.en) : [];
    const nfmt = c.types ? (c.types.ar || 0) + (c.types.match || 0) + (c.types.multi || 0) : 0;
    app.innerHTML = `<div class="qwrap">
      <div class="qhead"><div><p class="eyebrow" style="color:${SUBJ[c.subject]}">${esc(t('notes.eyebrow'))} · ${esc(sub(c.subject))} · ${esc(t('rung.class'))} ${c.cls}</p><h1 style="font-size:28px">${esc(chTitle(c))}</h1></div>
      <a class="btn small" href="#class-${c.cls}">${esc(t('back.class', { n: c.cls }))}</a></div>
      <div class="qcard notes" style="--c:${SUBJ[c.subject]}">
        <p class="note">${esc(t('notes.lead'))}</p>
        ${pts.length ? `<ol class="points">${pts.map((p) => `<li>${esc(p)}</li>`).join('')}</ol>` : `<p>${esc(t('notes.none'))}</p>`}
        <div class="row" style="margin-top:14px"><a class="btn primary" href="#practice-${c.id}">${esc(t('notes.practise'))}</a>${nfmt ? `<a class="btn" href="#practicex-${c.id}">${esc(t('notes.formats'))}</a>` : ''}</div>
        ${discLine()}
      </div></div>`;
  }

  // ---------------------------------------------------------------- practice
  async function viewPractice(cid, formats) {
    const c = CH[cid];
    if (!c) { location.hash = 'path'; return; }
    if (!session || session.cid !== cid || session.formats !== formats || session.done) {
      app.innerHTML = `<p class="loading">${esc(t('loadingQ'))}</p>`;
      const all = (await loadClass(c.cls)).filter((q) => q[1] === cid && (!formats || (q[8] && q[8] !== 'mcq')));
      const unseen = shuffle(all.filter((q) => !stats[q[0]]));
      const wrong = shuffle(all.filter((q) => stats[q[0]] && stats[q[0]][1] < stats[q[0]][0]));
      const rest = shuffle(all.filter((q) => stats[q[0]] && stats[q[0]][1] === stats[q[0]][0]));
      session = { cid, formats, qs: [...unseen, ...wrong, ...rest].slice(0, 10), i: 0, picks: [], done: false };
    }
    renderPractice();
  }

  function renderPractice() {
    const s = session;
    const c = CH[s.cid];
    const back = `<a class="btn small" href="#class-${c.cls}">${esc(t('back.class', { n: c.cls }))}</a>`;
    if (s.i >= s.qs.length) {
      s.done = true;
      const right = s.picks.filter((p, k) => p === s.qs[k][5]).length;
      app.innerHTML = `<div class="qwrap"><div class="qcard summary" style="--c:${SUBJ[c.subject]}">
        <p class="eyebrow">${esc(sub(c.subject))} · ${esc(t('rung.class'))} ${c.cls}${s.formats ? ` · ${esc(t('sum.formats'))}` : ''}</p><h2>${esc(chTitle(c))}</h2>
        <div class="big num">${right}/${s.qs.length}</div>
        <p class="lead" style="margin:10px auto">${esc(t(right === s.qs.length ? 'sum.all' : right >= s.qs.length * 0.7 ? 'sum.good' : 'sum.low'))}</p>
        <div class="row" style="justify-content:center"><button class="btn primary" id="again">${esc(t('sum.more'))}</button>${c.notes ? `<a class="btn" href="#notes-${c.id}">${esc(t('revise'))}</a>` : ''}${back}</div></div></div>`;
      $('#again').onclick = () => { session = null; viewPractice(c.id, s.formats); };
      return;
    }
    const q = s.qs[s.i];
    const picked = s.picks[s.i];
    const answered = picked !== undefined;
    const dots = s.qs.map((qq, k) => `<i class="${k < s.picks.length ? (s.picks[k] === qq[5] ? 'r' : 'w') : k === s.i ? 'c' : ''}"></i>`).join('');
    app.innerHTML = `<div class="qwrap">
      <div class="qhead"><div><p class="eyebrow" style="color:${SUBJ[c.subject]}">${esc(sub(c.subject))} · ${esc(t('rung.class'))} ${c.cls}${c.neet ? ` · ${esc(t('unit', { n: c.unit }).replace(/: $/, ''))}` : ''}</p><h3 style="margin:0">${esc(chTitle(c))}</h3></div>${back}</div>
      <div class="qcard">
        <div class="qhead"><span class="eyebrow num">${esc(t('q.of', { i: s.i + 1, n: s.qs.length }))} ${typeTag(q)}</span><div class="dots">${dots}</div></div>
        <div class="qtext" lang="en">${qhtml(q[3])}</div>
        <div class="opts">${q[4].map((o, k) => {
          let cls = '';
          if (answered && k === q[5]) cls = 'right';
          else if (answered && k === picked) cls = 'wrong';
          return `<button class="opt ${cls}" data-k="${k}" ${answered ? 'disabled' : ''} lang="en"><span class="l">${'ABCD'[k]}</span><span>${esc(o)}</span></button>`;
        }).join('')}</div>
        ${answered ? `<div class="explain ${picked === q[5] ? '' : 'bad'}"><b>${picked === q[5] ? esc(t('q.correct')) : esc(t('q.answer', { a: `${'ABCD'[q[5]]}. ${q[4][q[5]]}` }))}</b><span lang="en">${esc(q[6])}</span></div>${discLine()}` : ''}
        <p class="src">${esc(t(q[7] ? 'q.bank' : 'q.hub'))} · ${esc(t('q.diff', { d: t('d.' + q[2]) }))} · ${reportLink(q)}</p>
        <div class="qfoot"><span></span>${answered ? `<button class="btn primary" id="next">${esc(t(s.i + 1 < s.qs.length ? 'q.next' : 'q.score'))}</button>` : ''}</div>
      </div></div>`;
    app.querySelectorAll('.opt').forEach((b) => {
      b.onclick = () => { const k = Number(b.dataset.k); s.picks[s.i] = k; record(q, k === q[5]); renderPractice(); };
    });
    if ($('#next')) $('#next').onclick = () => { s.i++; renderPractice(); window.scrollTo(0, 0); };
  }

  // ---------------------------------------------------------------- mock tests
  async function viewMock() {
    if (mock && !mock.done) { app.innerHTML = `<p class="loading">${esc(t('loadingQ'))}</p>`; await loadClass(11); await loadClass(12); return renderTest(); }
    if (mock && mock.done) { await loadClass(11); await loadClass(12); return renderResult(); }
    const hist = store.get('nh-mocks', []);
    const wk = weekKey();
    const thisWeek = hist.find((h) => h.week === wk);
    const w = isoWeek();
    app.innerHTML = `
      <p class="eyebrow">${esc(t('mock.eyebrow'))}</p>
      <h1>${esc(t('mock.h1'))}</h1>
      <p class="lead">${esc(t('mock.lead'))}</p>
      <section class="day">
        <div class="day-main">
          <p class="eyebrow" style="color:var(--accent)">${esc(t('day.eyebrow'))} · ${esc(t('day.streak', { n: streak(hist) }))}</p>
          <h2>${esc(t('day.week', { w: w.week, range: weekRange() }))}</h2>
          <p class="note">${esc(t('day.lead'))}</p>
          ${thisWeek ? `<p><b class="num">${esc(t('day.done', { s: thisWeek.score, m: thisWeek.max }))}</b> ${esc(t('day.next'))}</p>`
            : `<button class="btn primary" data-mode="weekly">${esc(t('day.take'))}</button> <span class="note">${esc(t('mode.desc', { n: 180, m: 180, x: 720 }))}</span>`}
        </div>
        <div class="day-chart">${chartSVG(hist)}</div>
      </section>
      <div class="modes">${['full', 'half', 'quick'].map((k) => { const m = MODES[k]; return `
        <div class="mode"><span class="eyebrow">${esc(modeLabel(k))}</span><div class="big num">${m.per * 4}</div><span>${esc(t('mode.desc', { n: m.per * 4, m: m.mins, x: m.per * 16 }))}</span>
        <button class="btn" data-mode="${k}">${esc(t('mode.start'))}</button></div>`; }).join('')}</div>
      <div class="scroll-x"><table class="pattern"><thead><tr><th>${esc(t('tbl.section'))}</th><th>${esc(t('tbl.full'))}</th><th>${esc(t('tbl.covers'))}</th></tr></thead><tbody>
        <tr><td style="color:var(--phy);font-weight:600">${esc(sub('Physics'))}</td><td class="num">45</td><td>${esc(t('cov.P'))}</td></tr>
        <tr><td style="color:var(--che);font-weight:600">${esc(sub('Chemistry'))}</td><td class="num">45</td><td>${esc(t('cov.C'))}</td></tr>
        <tr><td style="color:var(--bio);font-weight:600">${esc(sub('Botany'))}</td><td class="num">45</td><td>${esc(t('cov.B'))}</td></tr>
        <tr><td style="color:var(--bio);font-weight:600">${esc(sub('Zoology'))}</td><td class="num">45</td><td>${esc(t('cov.Z'))}</td></tr>
      </tbody></table></div>
      ${hist.length ? `<p class="note" style="margin-top:14px">${esc(t('last', { s: hist[0].score, m: hist[0].max, mode: modeLabel(hist[0].modeKey || 'full'), d: hist[0].date }))} <a href="#progress">${esc(t('nav.progress'))}</a></p>` : ''}
      ${discLine()}`;
    app.querySelectorAll('[data-mode]').forEach((b) => { b.onclick = () => startMock(b.dataset.mode); });
    wireChart();
  }

  function streak(hist) {
    const weeks = new Set(hist.filter((h) => h.week).map((h) => h.week));
    let n = 0;
    const d = new Date();
    if (!weeks.has(weekKey())) d.setDate(d.getDate() - 7);
    for (;;) {
      const w = isoWeek(d);
      if (!weeks.has(`${w.year}-W${String(w.week).padStart(2, '0')}`)) break;
      n++; d.setDate(d.getDate() - 7);
    }
    return n;
  }

  // Line chart of full-length scores (out of 720): 2px line, 8px markers with a surface ring,
  // 10% area wash, hairline grid, end value labelled, tooltip on hover/focus. The history table is the table view.
  function chartSVG(hist) {
    const pts = hist.filter((h) => h.max === 720).slice(0, 12).reverse();
    if (!pts.length) return `<p class="note chart-empty">${esc(t('chart.title'))}: ${esc(t('chart.empty'))}</p>`;
    const W = 420, H = 190, L = 38, R = 14, Tp = 14, B = 26;
    const x = (i) => (pts.length === 1 ? (L + W - R) / 2 : L + (i * (W - L - R)) / (pts.length - 1));
    const y = (s) => Tp + (1 - (s + 180) / 900) * (H - Tp - B);   // axis from -180 to 720
    const ticks = [0, 180, 360, 540, 720];
    const line = pts.map((p, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(p.score).toFixed(1)}`).join(' ');
    const area = `${line} L${x(pts.length - 1).toFixed(1)},${y(-180).toFixed(1)} L${x(0).toFixed(1)},${y(-180).toFixed(1)} Z`;
    const last = pts[pts.length - 1];
    return `<figure class="chart"><figcaption class="eyebrow">${esc(t('chart.title'))}</figcaption>
      <div class="chart-box"><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(t('chart.title'))}">
        ${ticks.map((v) => `<line x1="${L}" x2="${W - R}" y1="${y(v)}" y2="${y(v)}" class="grid"/><text x="${L - 6}" y="${y(v) + 4}" class="tick" text-anchor="end">${v}</text>`).join('')}
        <path d="${area}" class="area"/>
        <path d="${line}" class="line"/>
        ${pts.map((p, i) => `<circle cx="${x(i)}" cy="${y(p.score)}" r="5" class="dot" tabindex="0" data-tip="${esc(t('chart.tip', { d: p.date, s: p.score }))}"/>`).join('')}
        <text x="${x(pts.length - 1)}" y="${y(last.score) - 12}" class="endlabel" text-anchor="${pts.length > 1 ? 'end' : 'middle'}">${last.score}</text>
        ${pts.length > 1 ? `<text x="${x(0)}" y="${H - 6}" class="tick" text-anchor="start">${esc(pts[0].date)}</text><text x="${x(pts.length - 1)}" y="${H - 6}" class="tick" text-anchor="end">${esc(last.date)}</text>` : ''}
      </svg><div class="tip" id="chartTip" hidden></div></div></figure>`;
  }
  function wireChart() {
    const tip = $('#chartTip');
    if (!tip) return;
    const box = tip.parentElement;
    const show = (dot) => {
      tip.textContent = dot.dataset.tip;
      tip.hidden = false;
      const b = box.getBoundingClientRect();
      const d = dot.getBoundingClientRect();
      tip.style.left = `${Math.min(b.width - 120, Math.max(0, d.left - b.left - 50))}px`;
      tip.style.top = `${d.top - b.top - 34}px`;
    };
    box.querySelectorAll('.dot').forEach((dot) => {
      dot.addEventListener('mouseenter', () => show(dot));
      dot.addEventListener('focus', () => show(dot));
      dot.addEventListener('mouseleave', () => { tip.hidden = true; });
      dot.addEventListener('blur', () => { tip.hidden = true; });
    });
  }

  async function startMock(mode) {
    app.innerHTML = `<p class="loading">${esc(t('loadingQ'))}</p>`;
    const pool = [...(await loadClass(11)), ...(await loadClass(12))].filter((q) => CH[q[1]] && CH[q[1]].neet);
    const per = MODES[mode].per;
    // The weekly paper is seeded by the week, so everyone gets the same paper.
    const w = isoWeek();
    const rnd = mode === 'weekly' ? seeded(w.year * 100 + w.week) : Math.random;
    const ids = [];
    const sections = [];
    for (const sec of SECTIONS) {
      const byCh = {};
      for (const q of pool) if (sec.test(CH[q[1]])) (byCh[q[1]] = byCh[q[1]] || []).push(q);
      const keys = Object.keys(byCh).sort();
      const lists = shuffle(keys.map((k) => byCh[k]), rnd).map((l) => shuffle(l, rnd));
      const picked = [];
      while (picked.length < per && lists.some((l) => l.length)) for (const l of lists) { if (l.length && picked.length < per) picked.push(l.pop()[0]); }
      sections.push({ key: sec.key, start: ids.length, n: picked.length });
      ids.push(...shuffle(picked, rnd));
    }
    mock = { mode, week: mode === 'weekly' ? weekKey() : null, ids, sections, answers: {}, review: {}, cur: 0, start: Date.now(), mins: MODES[mode].mins, done: false };
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
        <div class="stabs">${mock.sections.map((s) => `<button class="stab ${s === sec ? 'on' : ''}" style="--c:${SECTIONS.find((d) => d.key === s.key).c}" data-sec="${s.start}">${esc(sub(s.key))}</button>`).join('')}</div>
        <div class="row"><span class="timer num" id="timer"></span><button class="btn small" id="submit">${esc(t('test.submit'))}</button></div>
      </div>
      <div id="confirm"></div>
      <div class="test">
        <div class="qcard">
          <div class="qhead"><span class="eyebrow num" style="color:${secDef.c}">${esc(sub(sec.key))} · ${esc(t('q.of', { i: i + 1, n: mock.ids.length }))} ${typeTag(q)}</span><span class="eyebrow">${esc(chTitle(CH[q[1]]))}</span></div>
          <div class="qtext" lang="en">${qhtml(q[3])}</div>
          <div class="opts">${q[4].map((o, k) => `<button class="opt ${ans === k ? 'sel' : ''}" data-k="${k}" lang="en"><span class="l">${'ABCD'[k]}</span><span>${esc(o)}</span></button>`).join('')}</div>
          <div class="qfoot">
            <div class="row"><button class="btn small" id="prev" ${i === 0 ? 'disabled' : ''}>${esc(t('test.prev'))}</button><button class="btn small" id="clear">${esc(t('test.clear'))}</button></div>
            <div class="row"><button class="btn small" id="rev">${esc(t(mock.review[i] ? 'test.unmark' : 'test.mark'))}</button><button class="btn primary small" id="nxt">${esc(t(i + 1 < mock.ids.length ? 'test.next' : 'test.save'))}</button></div>
          </div>
        </div>
        <aside class="omr">
          <p class="eyebrow" style="margin:0 0 8px">${esc(t('test.sheet', { s: sub(sec.key), a: answered, n: mock.ids.length }))}</p>
          <div class="omr-grid">${Array.from({ length: sec.n }, (_, k) => {
            const j = sec.start + k;
            return `<button class="bub ${mock.answers[j] !== undefined ? 'ans' : ''} ${mock.review[j] ? 'rev' : ''} ${j === i ? 'cur' : ''}" data-j="${j}" aria-label="${j + 1}">${j + 1}</button>`;
          }).join('')}</div>
          <div class="legend"><span>${esc(t('test.legend1'))}</span><span style="color:var(--mark)">${esc(t('test.legend2'))}</span></div>
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
      $('#confirm').innerHTML = `<div class="confirm row"><span>${esc(t('test.confirm', { a: answered, n: mock.ids.length }))}</span>
        <button class="btn small primary" id="yes">${esc(t('test.yes'))}</button><button class="btn small" id="no">${esc(t('test.no'))}</button></div>`;
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
    hist.unshift({ date: new Date().toLocaleDateString('en-IN'), modeKey: mock.mode, week: mock.week, score, max: mock.result.max, per });
    store.set('nh-mocks', hist.slice(0, 60));
    store.set('nh-mock-live', mock);
    renderResult();
  }

  function renderResult() {
    const r = mock.result;
    const wrongOrBlank = mock.ids.map((id, i) => ({ q: BYID[id], i, a: mock.answers[i] })).filter((x) => x.q && x.a !== x.q[5]);
    app.innerHTML = `
      <p class="eyebrow">${esc(t('res.eyebrow', { mode: modeLabel(mock.mode) }))}</p>
      <h1><span class="num">${r.score}</span> / <span class="num">${r.max}</span></h1>
      <p class="lead">${esc(t('res.time', { m: Math.floor(r.secs / 60) }))}</p>
      <div class="score-grid">${mock.sections.map((s) => {
        const p = r.per[s.key] || { c: 0, w: 0, u: 0 };
        return `<div class="tile" style="--c:${SECTIONS.find((d) => d.key === s.key).c}"><span>${esc(sub(s.key))}</span><b class="num">${p.c * 4 - p.w}</b><span class="num">${esc(t('res.tile', p))}</span></div>`;
      }).join('')}</div>
      <div class="row" style="margin-bottom:18px"><button class="btn primary" id="newmock">${esc(t('res.another'))}</button><a class="btn" href="#progress">${esc(t('nav.progress'))}</a></div>
      ${discLine()}
      <h2>${esc(t('res.review', { n: wrongOrBlank.length }))}</h2>
      <div style="display:grid;gap:10px">${wrongOrBlank.map(({ q, i, a }) => `
        <div class="qcard"><p class="eyebrow">Q${i + 1} · ${esc(chTitle(CH[q[1]]))} ${typeTag(q)}</p><div class="qtext small" lang="en">${qhtml(q[3])}</div>
        <div class="explain ${a === undefined ? '' : 'bad'}"><b>${a === undefined ? esc(t('res.blank')) : esc(t('res.chose', { x: `${'ABCD'[a]}. ${q[4][a]}` }))} ${esc(t('q.answer', { a: `${'ABCD'[q[5]]}. ${q[4][q[5]]}` }))}</b><span lang="en">${esc(q[6])}</span></div>
        <p class="src">${reportLink(q)}</p></div>`).join('')}</div>`;
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
      <p class="eyebrow">${esc(t('pr.eyebrow'))}</p>
      <h1>${esc(t('pr.h1'))}</h1>
      <div class="score-grid">
        <div class="tile"><span>${esc(t('pr.tried'))}</span><b class="num">${num(seen)}</b><span>${esc(t('pr.of', { n: num(INDEX.chapters.reduce((n, c) => n + c.count, 0)) }))}</span></div>
        ${['Physics', 'Chemistry', 'Biology'].map((s) => { const b = bySub[s]; return `<div class="tile" style="--c:${SUBJ[s]}"><span>${esc(sub(s))}</span><b class="num">${b ? pct(b.correct, b.tries) + '%' : '-'}</b><span class="num">${esc(b ? t('pr.subtried', { n: b.seen }) : t('pr.notstarted'))}</span></div>`; }).join('')}
      </div>
      <p class="note">${esc(t('pr.overall', { p: pct(correct, tries), n: num(tries) }))}</p>
      <div class="day-chart" style="max-width:560px">${chartSVG(hist)}</div>
      <h2 style="margin-top:20px">${esc(t('pr.weak'))}</h2>
      ${weak.length ? `<ul class="weak">${weak.map(({ c, acc, a }) => `<li style="--c:${SUBJ[c.subject]}"><div><b>${esc(chTitle(c))}</b><div class="note">${esc(t('pr.weakline', { c: c.cls, s: sub(c.subject), p: acc, n: a.tries }))}</div></div><div class="ch-btns">${c.notes ? `<a class="btn small" href="#notes-${c.id}">${esc(t('revise'))}</a>` : ''}<a class="btn small" href="#practice-${c.id}">${esc(t('practise'))}</a></div></li>`).join('')}</ul>`
        : `<p class="note">${esc(t('pr.weaknone'))}</p>`}
      <h2 style="margin-top:20px">${esc(t('pr.hist'))}</h2>
      ${hist.length ? `<div class="scroll-x"><table class="hist"><thead><tr><th>${esc(t('pr.date'))}</th><th>${esc(t('pr.test'))}</th><th>${esc(t('pr.score'))}</th>${['Physics', 'Chemistry', 'Botany', 'Zoology'].map((k) => `<th>${esc(sub(k))}</th>`).join('')}</tr></thead><tbody>
        ${hist.map((h) => `<tr><td>${esc(h.date)}</td><td>${esc(modeLabel(h.modeKey || 'full'))}${h.week ? ` <span class="note">${esc(h.week)}</span>` : ''}</td><td class="num"><b>${h.score}</b>/${h.max}</td>${['Physics', 'Chemistry', 'Botany', 'Zoology'].map((k) => `<td class="num">${h.per[k] ? h.per[k].c * 4 - h.per[k].w : '-'}</td>`).join('')}</tr>`).join('')}
      </tbody></table></div>` : `<p class="note">${esc(t('pr.nohist'))} <a href="#mock">${esc(t('pr.take'))}</a>.</p>`}
      <div style="margin-top:28px"><button class="btn small" id="reset">${esc(t('pr.erase'))}</button><span id="resetc"></span></div>`;
    wireChart();
    $('#reset').onclick = () => {
      $('#resetc').innerHTML = ` <span class="note">${esc(t('pr.eraseq'))}</span> <button class="btn small primary" id="ry">${esc(t('pr.yes'))}</button> <button class="btn small" id="rn">${esc(t('pr.keep'))}</button>`;
      $('#ry').onclick = () => { stats = {}; mock = null; store.set('nh-stats', {}); store.set('nh-mocks', []); store.set('nh-mock-live', null); viewProgress(); };
      $('#rn').onclick = () => { $('#resetc').innerHTML = ''; };
    };
  }

  chrome();
  app.innerHTML = `<p class="loading">${esc(t('loading'))}</p>`;
  loadIndex().then(route).catch(() => { app.innerHTML = `<p class="loading">${esc(t('loadFail'))}</p>`; });
})();
