#!/usr/bin/env python3
"""Check a pitch against CALLS-SPEC.md.

  python3 brand/check-call.py                      # every pitch
  python3 brand/check-call.py src/content/calls/my-slug.md

Exit code 1 if anything fails. Warnings do not fail the run.
"""
import sys, os, re, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SGT = datetime.timezone(datetime.timedelta(hours=8))
# The body's sections, in order. The call box and the claim render from the
# frontmatter above them; the charts render at the slot.
SECTIONS = [
    '## The thesis',
    '## What the market prices in, and where I differ',
    '## Valuation, with the working',
    '<div class="charts-slot"></div>',
    '## Risks, and what would change my view',
    '## Conclusion',
]
SOURCES_TAIL = 'Personal research, not investment advice.'
BANNED = [
    (r'—', 'em dash'), (r'–', 'en dash'),
    (r'\bcenters?\b', 'US spelling "center"'), (r'\benergized\b', 'US spelling "energized"'),
    (r'\b\w+yzed\b|\b\w+yze\b', 'US spelling "-yze"'),
    (r'\b(?:color|favor|behavior|labor)s?\b', 'US spelling "-or"'),
    (r'\bmodeling\b', 'US spelling "modeling"'),
]

CLAIMS_TS = open(os.path.join(ROOT, 'src/data/claims.ts')).read()
CLAIM_IDS = set(re.findall(r"^\s*id: '([^']+)'", CLAIMS_TS, re.M))


def check(path):
    fails, warns = [], []
    raw = open(path).read()
    slug = os.path.basename(path)[:-3]
    parts = raw.split('\n---\n', 1)
    if not raw.startswith('---') or len(parts) < 2:
        return ['no frontmatter'], []
    fm, body = parts[0][3:], parts[1]

    def field(k, src=fm):
        m = re.search(rf'^\s*{k}:\s*(.+?)\s*$', src, re.M)
        v = m.group(1).strip().strip('"') if m else None
        return None if v in (None, 'null', '~', '') else v

    for k in ('title', 'summary', 'company', 'ticker', 'exchange'):
        if not field(k):
            fails.append(f'missing frontmatter: {k}')
    draft = field('draft') != 'false'
    call = fm.split('\ncall:', 1)[1] if '\ncall:' in fm else ''
    call = re.split(r'\n\S', call, maxsplit=1)[0]
    for k in ('price', 'priceDate', 'horizon', 'wrongIf'):
        if not field(k, call):
            fails.append(f'missing call.{k}')
    lay = re.search(r'^layer:\s*"?([a-z-]+)"?', fm, re.M)
    if lay and f"id: '{lay.group(1)}'" not in open(os.path.join(ROOT, 'src/data/stack.ts')).read():
        fails.append(f'layer "{lay.group(1)}" is not a layer in src/data/stack.ts')
    ids = re.findall(r"[a-z0-9-]+", (re.search(r'^claims:\s*\[([^\]]*)\]', fm, re.M) or [None, ''])[1])
    if re.search(r'^correction:', fm, re.M):
        fails.append('correction field: fix the piece in place instead (2 Nov 2026)')
    # error classes found in the deep checks of 2 Nov 2026, scanned in the md and the PDF
    texts = {'md': raw}
    pdf_rel = re.search(r'^\s*pdf:\s*"([^"]+)"', fm, re.M)
    if pdf_rel and os.path.exists(os.path.join(ROOT, 'public', pdf_rel.group(1).lstrip('/'))):
        try:
            import pypdfium2
            doc = pypdfium2.PdfDocument(os.path.join(ROOT, 'public', pdf_rel.group(1).lstrip('/')))
            texts['pdf'] = ' '.join(pg.get_textpage().get_text_range() for pg in doc).replace('\r\n', ' ')
            pg_field = re.search(r'^\s*pages:\s*(\d+)', fm, re.M)
            if pg_field and int(pg_field.group(1)) != len(doc):
                fails.append(f'pages: {pg_field.group(1)} but the PDF has {len(doc)}')
        except ImportError:
            warns.append('pypdfium2 missing: PDF text not checked')
    NOTE_BANNED = [
        (r'\bwhere I was wrong\b|\bI was wrong\b|\bshows the piece was wrong\b|\bwhat showed me the slip\b|\bI withdraw\b', 'correction framing', re.I),
        (r'\bWhat would change our mind\b|\b[Ww]e initiate\b|\bour view\b', '"we/our" instead of "I/my"', 0),
        (r'\b[Aa] (?:8|11|18|8\d)(?:[.,]\d+)?(?:%|x\b| per cent| times\b)', '"a" before a number read with a vowel sound', 0),
        (r'[\u2014\u2013\u2212]', 'an em or en dash or minus sign', 0),
        (r'\bdraft view\b|\bDRAFT\b', 'draft wording', 0),
        (r'\bClaude\b|\bpaper portfolio\b', 'a mention of Claude or a paper portfolio', 0),
    ]
    for where, t in texts.items():
        t = t if where == 'pdf' else re.sub(r'^draft:.*$', '', t, flags=re.M)
        for pat, label, flags in NOTE_BANNED:
            n = len(re.findall(pat, t, flags))
            if n and not (where == 'md' and label == 'draft wording' and draft):
                fails.append(f'{label} in the {where} ({n}x)')
    for i in ids:
        if i not in CLAIM_IDS:
            fails.append(f'claim "{i}" is not in src/data/claims.ts')

    if not draft:
        direction = field('direction', call)
        need = ('direction', 'conviction') + (('revisitIf',) if direction == 'NO CALL' else ('target',))
        for k in need:
            if not field(k, call):
                fails.append(f'published without Tommy\'s call.{k}')
        d = field('date')
        if not d:
            fails.append('published without a date')
        else:
            try:
                dt = datetime.datetime.fromisoformat(d)
                if dt.tzinfo is None:
                    fails.append('date has no +08:00 offset')
                elif dt > datetime.datetime.now(SGT):
                    fails.append(f'date {d} is in the future')
            except ValueError:
                fails.append(f'date not ISO: {d}')
        for k in ('pdf', 'xlsx', 'thumb'):
            f = field(k, fm.split('\nfiles:', 1)[1] if '\nfiles:' in fm else '')
            if f and not os.path.exists(os.path.join(ROOT, 'public', f.lstrip('/'))):
                (warns if k == 'thumb' else fails).append(f'files.{k} not found in public/: {f}')
        if not re.search(r'^keyPoints:', fm, re.M):
            fails.append('missing keyPoints')
        if 'draftView' in fm:
            warns.append('published pitch still carries draftView; remove it')
    else:
        if not re.search(r'^draftView:', fm, re.M):
            warns.append('draft has no draftView for Tommy')

    pos = -1
    for s in SECTIONS:
        i = body.find(s)
        if i < 0:
            fails.append(f'missing section: {s}')
        elif i < pos:
            fails.append(f'section out of order: {s}')
        else:
            pos = i
    if not re.search(r'<p class="sources">Sources:.*' + re.escape(SOURCES_TAIL) + r'</p>', body):
        fails.append('sources line missing or does not end with the fixed tail')

    for pat, name in BANNED:
        for m in re.finditer(pat, raw):
            line = raw[:m.start()].count('\n') + 1
            fails.append(f'line {line}: {name}: "{m.group(0)}"')

    text = re.sub(r'<[^>]+>', ' ', body)
    words = len(re.findall(r"[A-Za-z0-9$%.,']+", text))
    if not 1500 <= words <= 3200:
        warns.append(f'{words} words; pitches run 1,500 to 3,200')
    sents = [s for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', text)) if len(s.split()) > 3]
    if sents:
        avg = sum(len(s.split()) for s in sents) / len(sents)
        if not 12 <= avg <= 22:
            warns.append(f'average sentence {avg:.1f} words; house style is 14 to 20')
    return fails, warns


def main():
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'src/content/calls/*.md')))
    bad = 0
    for p in paths:
        f, w = check(p)
        name = os.path.basename(p)
        print(f'{"FAIL" if f else "ok  "} {name}')
        for x in f:
            print(f'     x {x}')
        for x in w:
            print(f'     ! {x}')
        bad += bool(f)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
