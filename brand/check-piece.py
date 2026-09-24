#!/usr/bin/env python3
"""Check a journal piece against WRITING-FORMAT.md.

  python3 brand/check-piece.py                     # every published piece
  python3 brand/check-piece.py src/content/journal/my-slug.md

Exit code 1 if anything fails. Warnings do not fail the run.
"""
import sys, os, re, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = {'Explainer', 'Analysis', 'Note'}
ANALOGY_SUMMARY = "<summary>Explain it like I don't work in finance</summary>"
# The disclaimer must open with this exact sentence pair. A piece may add a
# further statement after it, as the memory piece does.
EXPOSURE_NOTE = ('This maps who operates in each layer. It is not a recommendation, '
                 'and naming a company is not a view on its shares.')
SOURCES_TAIL = 'Personal research, not investment advice.'
BANNED = [
    (r'—', 'em dash'), (r'–', 'en dash'),
    (r'\bcenters?\b', 'US spelling "center"'), (r'\benergized\b', 'US spelling "energized"'),
    (r'\banaly[sz]ed?\b(?<=zed)', 'US spelling "analyzed"'),
    (r'\bprice target\b', 'price target'), (r'\bmarket share\b', 'market share'),
    (r'\boverweight\b', 'a rating'), (r'\bunderweight\b', 'a rating'),
    (r'\bbuy rating\b', 'a rating'), (r'\bundervalued\b', 'a valuation call'),
    (r'\bovervalued\b', 'a valuation call'),
    (r'\bP/E\b|\bprice[- ]to[- ]earnings\b|\btimes (?:next year.s |forward |trailing )?earnings\b', 'a valuation multiple'),
    (r'\bmarket (?:cap|capitali[sz]ation|value)\b', 'market value'),
    (r'\bshare price\b|\bstock price\b', 'a share price'),
    (r'\bpriced for perfection\b|\bpriced in\b', 'a valuation call'),
]

def check(path):
    fails, warns = [], []
    raw = open(path).read()
    slug = os.path.basename(path)[:-3]
    parts = raw.split('---')
    if len(parts) < 3:
        return [f'{slug}: no frontmatter'], []
    fm, body = parts[1], '---'.join(parts[2:])

    def field(k):
        m = re.search(rf'^{k}:\s*(.+?)\s*$', fm, re.M)
        return m.group(1).strip().strip('"') if m else None

    # ── frontmatter
    for k in ('title', 'date', 'summary', 'category', 'cover', 'tags'):
        if not field(k):
            fails.append(f'missing frontmatter: {k}')
    cat = field('category')
    if cat and cat not in CATEGORIES:
        fails.append(f'category "{cat}" is not one of {sorted(CATEGORIES)}')
    if field('shortLabel'):
        warns.append('shortLabel is legacy and read by nothing; remove it')
    d = field('date')
    if d:
        try:
            dt = datetime.date.fromisoformat(d)
            if dt.weekday() >= 5:
                warns.append(f'date {d} is a {dt.strftime("%A")}; the others are weekdays')
        except ValueError:
            fails.append(f'date "{d}" is not YYYY-MM-DD')
    t = field('tags')
    if t:
        n = len(re.findall(r'"[^"]+"', t))
        if not 2 <= n <= 4:
            warns.append(f'{n} tags; the format asks for 2 to 4')
    cov = field('cover')
    if cov and not os.path.exists(os.path.join(ROOT, 'public' + cov)):
        fails.append(f'cover {cov} does not exist in public/covers/')
    s = field('summary')
    if s and not 2 <= len(re.findall(r'[.!?](?:\s|$)', s)) <= 4:
        warns.append('summary should be two or three sentences')
    ti = field('title')
    if ti and not 6 <= len(ti.split()) <= 20:
        warns.append(f'title is {len(ti.split())} words; the format asks for 8 to 16')

    # ── the two mandatory blocks
    if ANALOGY_SUMMARY not in body:
        fails.append('no analogy block, or its summary line has been edited')
    else:
        blk = body.split(ANALOGY_SUMMARY)[1].split('</details>')[0]
        n = blk.count('<p>')
        if not 2 <= n <= 4:
            warns.append(f'analogy has {n} paragraphs; the format asks for 2 to 4')
        first_h2 = body.find('\n## ')
        if first_h2 != -1 and body.find(ANALOGY_SUMMARY) > first_h2:
            fails.append('analogy block must come before the first ## heading')
    if '<section class="exposure">' not in body:
        fails.append('no exposure map')
    else:
        note = re.search(r'<p class="note">(.*?)</p>', body, re.S)
        if not note or not note.group(1).strip().startswith(EXPOSURE_NOTE):
            fails.append('exposure disclaimer must open with the fixed sentence pair')
        if '<dl class="against">' not in body:
            # A whole-stack orientation map has no loser. A directional claim always does.
            (fails if cat == 'Analysis' else warns).append(
                'exposure map has no "on the other side" block')
        if '<span class="names">' not in body:
            warns.append('exposure map names no companies in <span class="names">')
        groups = body.count('<dt>')
        if not 3 <= groups <= 7:
            warns.append(f'{groups} exposure groups; the format asks for 3 to 6')

    # ── sources
    m = re.search(r'<p class="sources">(.*?)</p>', body, re.S)
    if not m:
        fails.append('no sources paragraph')
    elif not m.group(1).strip().endswith(SOURCES_TAIL):
        fails.append(f'sources paragraph must end "{SOURCES_TAIL}"')

    # ── shape
    h2 = re.findall(r'^## (.+)$', body, re.M)
    if not 3 <= len(h2) <= 7:
        warns.append(f'{len(h2)} ## sections; the format asks for 4 to 6')
    if cat == 'Analysis' and not any('prove me wrong' in h.lower() for h in h2):
        fails.append('an Analysis piece must carry a "What would prove me wrong" section')

    # ── style
    prose = re.sub(r'<[^>]+>', '', body)
    for pat, label in BANNED:
        hits = re.findall(pat, prose, re.I)
        if hits:
            fails.append(f'{label} appears {len(hits)}x')
    words = len(prose.split())
    if not 900 <= words <= 1700:
        warns.append(f'{words} words; the format asks for 1,050 to 1,500')
    sents = [x for x in re.split(r'(?<=[.!?]) ', ' '.join(
        p for p in prose.split('\n\n') if p.strip() and not p.strip().startswith('#'))) if x.strip()]
    if sents:
        avg = sum(len(x.split()) for x in sents) / len(sents)
        if avg > 24:
            warns.append(f'average sentence is {avg:.0f} words; the others run 14 to 20')
    return [f'{slug}: {x}' for x in fails], [f'{slug}: {x}' for x in warns]

targets = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'src/content/journal/*.md')))
allf, allw = [], []
for t in targets:
    f, w = check(t)
    allf += f; allw += w
for w in allw: print('  warn  ' + w)
for f in allf: print('  FAIL  ' + f)
print(f'\n{len(targets)} piece(s): {len(allf)} failure(s), {len(allw)} warning(s)')
sys.exit(1 if allf else 0)
