#!/usr/bin/env python3
"""Check a journal piece against WRITING-FORMAT.md.

  python3 brand/check-piece.py                     # every published piece
  python3 brand/check-piece.py src/content/journal/my-slug.md

A body containing <hr class="layer"> is a deep piece (WRITING-FORMAT.md §D)
and is checked in deep mode: the 15-figure and length budgets apply to the
plain-English top only, and the investor layer must carry its claims on
record, falsifier, exposure map and sources. Any other piece is checked as
before.

Exit code 1 if anything fails. Warnings do not fail the run.
"""
import sys, os, re, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = {'Explainer', 'Analysis', 'Note'}
SGT = datetime.timezone(datetime.timedelta(hours=8))
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
# WRITING-FORMAT §3.4: the one whole-stack orientation map, exempt from the against block.
WHOLE_STACK_MAPS = {'the-two-seconds-after-you-hit-send'}

def _read(rel):
    try:
        return open(os.path.join(ROOT, rel)).read()
    except OSError:
        return ''
CLAIMS_TS = _read('src/data/claims.ts')
STACK_TS = _read('src/data/stack.ts')
CLAIM_IDS = set(re.findall(r"^\s*id: '([^']+)'", CLAIMS_TS, re.M))

def _claims(ts):
    """Each claims.ts entry as a dict of id, home and claim text."""
    out = []
    starts = [m.start() for m in re.finditer(r"^\s*id: '", ts, re.M)] + [len(ts)]
    for a, b in zip(starts, starts[1:]):
        blk = ts[a:b]
        get = lambda k: (re.search(rf"^\s*{k}: '((?:[^'\\]|\\.)*)'", blk, re.M) or [None, None])[1]
        out.append({'id': get('id'), 'home': get('home'), 'claim': (get('claim') or '').replace("\\'", "'")})
    return out
CLAIMS = _claims(CLAIMS_TS)
def claims_homed_at(slug):
    """Mirror of claimsHomedAt() in src/data/claims.ts."""
    return [c for c in CLAIMS if c['home'] == slug or c['id'] == slug]

# Deep pieces (WRITING-FORMAT.md §D)
LAYER_HR = '<hr class="layer">'
LAYER_LABEL = '<p class="layer-label">For investors</p>'
DEEP_TOP_WORDS = (300, 600)
DEEP_TOP_FIGURES = 15
DEEP_INVESTOR_WORDS = 2600   # before the exposure map
DEEP_REQUIRED = ['## Claims on record', '## What would prove me wrong']
FIGURE_RE = r'(?<![A-Za-z\d.,])\d[\d,.]*(?![A-Za-z]*\d)'

def storyline(s):
    """The story a reader follows: no charts, no folded evidence or earlier claims."""
    s = re.sub(r'<figure class="chart">.*?</figure>', ' ', s, flags=re.S)
    return re.sub(r'<details class="(?:evidence|claims-earlier|claims-record)">.*?</details>', ' ', s, flags=re.S)

def reading_text(s):
    """The reading body: no exposure map, no sources line, no tags."""
    s = re.sub(r'<section class="exposure">.*?</section>', '', s, flags=re.S)
    s = re.sub(r'<p class="sources">.*?</p>', '', s, flags=re.S)
    return re.sub(r'<[^>]+>', ' ', s)
STACK_IDS = set(re.findall(r"'([a-z0-9-]+)'", ''.join(re.findall(r'pieces: \[([^\]]*)\]', STACK_TS))))

def deep_checks(slug, body, draft):
    """Structure of a deep piece (§D): the divider and its label, the investor
    layer's required sections, and every claim it carries anchored and quoted."""
    fails = []
    if body.count(LAYER_HR) != 1:
        fails.append(f'a deep piece has exactly one {LAYER_HR}, found {body.count(LAYER_HR)}')
    top, inv = body.split(LAYER_HR, 1)
    if not inv.lstrip().startswith(LAYER_LABEL):
        fails.append(f'the divider must be followed by {LAYER_LABEL}')
    # Story format (STORY-RULES.md, 31 Oct 2026): charts at the turns of the
    # argument, and no section named after a company.
    charts = body.count('<figure class="chart">')
    if not 2 <= charts <= 5:
        fails.append(f'{charts} charts; a deep piece carries 2 to 4 at the turns of its argument (STORY-RULES.md)')
    for h in ('## How it works', '## The number that matters', '## The mechanism in depth'):
        if re.search(rf'^{re.escape(h)}\s*$', body, re.M):
            fails.append(f'"{h}" is a topic label; headings are steps in the argument (STORY-RULES.md)')
    # The claims fold at the foot (Tommy, 31 Oct 2026) replaces the old
    # "Claims on record" section: the story ends on what to watch, not a recap.
    record = re.search(r'<details class="claims-record">(.*?)</details>', inv, re.S)
    required = [h for h in DEEP_REQUIRED if not (record and h == '## Claims on record')]
    pos = -1
    for h in required:
        m = re.search(rf'^{re.escape(h)}\s*$', inv, re.M)
        if not m:
            fails.append(f'investor layer is missing "{h}"')
        elif m.start() < pos:
            fails.append(f'"{h}" is out of order')
        else:
            pos = m.start()
    if '<section class="exposure">' in top or '<p class="sources">' in top:
        fails.append('exposure map and sources belong below the divider')
    # Every claim the piece carries is quoted word for word, and each merged
    # slug is anchored so its redirect and its claim link land on it.
    rec = record.group(1) if record else (inv.split('## Claims on record')[1] if '## Claims on record' in inv else '')
    flat = lambda t: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>|[*_]', '', t)).replace('\u2019', "'").strip()
    for c in claims_homed_at(slug):
        if c['claim'] and flat(c['claim']) not in flat(rec):
            fails.append(f'claim "{c["id"]}" is not quoted word for word in Claims on record')
        if c['id'] != slug and f'<a id="{c["id"]}"></a>' not in body:
            fails.append(f'no anchor <a id="{c["id"]}"></a> for the merged claim')
    return fails

def check(path):
    fails, warns = [], []
    raw = open(path).read()
    slug = os.path.basename(path)[:-3]
    parts = raw.split('---')
    if len(parts) < 3:
        return [f'{slug}: no frontmatter'], []
    fm, body = parts[1], '---'.join(parts[2:])
    deep = LAYER_HR in body

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
        # The date is when the piece actually went live, never a planned or
        # invented one. A full datetime with offset keeps same-day pieces in order.
        try:
            dt = datetime.datetime.fromisoformat(d)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=SGT)
            if dt > datetime.datetime.now(SGT):
                fails.append(f'date {d} is in the future; use the real publish time')
        except ValueError:
            fails.append(f'date "{d}" is not YYYY-MM-DDTHH:MM:SS+08:00')
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
        if not 2 <= n <= 3:
            warns.append(f'analogy has {n} paragraphs; the format asks for 2')
        first_h2 = body.find('\n## ')
        if first_h2 != -1 and body.find(ANALOGY_SUMMARY) > first_h2:
            fails.append('analogy block must come before the first ## heading')
    if '<section class="exposure">' not in body:
        fails.append('no exposure map')
    else:
        note = re.search(r'<p class="note">(.*?)</p>', body, re.S)
        if not note or not note.group(1).strip().startswith(EXPOSURE_NOTE):
            fails.append('exposure disclaimer must open with the fixed sentence pair')
        if '<dl class="against">' not in body and slug not in WHOLE_STACK_MAPS:
            # A whole-stack orientation map has no loser. A directional claim always does.
            (fails if cat == 'Analysis' else warns).append(
                'exposure map has no "on the other side" block')
        if '<span class="names">' not in body:
            warns.append('exposure map names no companies in <span class="names">')
        groups = body.count('<dt>')  # includes "On the other side"
        if not 3 <= groups <= 6:
            warns.append(f'{groups} exposure groups; the format asks for 3 or 4 plus the other side')
        ex = re.search(r'<section class="exposure">(.*?)</section>', body, re.S)
        exw = len(re.sub(r'<[^>]+>', ' ', ex.group(1)).split()) if ex else 0
        if exw > 150:
            warns.append(f'exposure map is {exw} words; the format asks for about 100')

    # ── sources
    m = re.search(r'<p class="sources">(.*?)</p>', body, re.S)
    if not m:
        fails.append('no sources paragraph')
    elif not m.group(1).strip().endswith(SOURCES_TAIL):
        fails.append(f'sources paragraph must end "{SOURCES_TAIL}"')
    elif len(m.group(1).split()) > (200 if deep else 60):
        warns.append(f'sources line is {len(m.group(1).split())} words; the format asks for one or two sentences')

    # ── shape
    h2 = re.findall(r'^## (.+)$', body, re.M)
    if deep:
        fails += deep_checks(slug, body, field('draft') == 'true')
    elif not 2 <= len(h2) <= 4:
        warns.append(f'{len(h2)} ## sections; the format asks for 3')
    if cat == 'Analysis' and not any('prove me wrong' in h.lower() for h in h2):
        fails.append('an Analysis piece must carry a "What would prove me wrong" section')

    # ── the site around the piece
    # Every piece sits on the map; every Analysis piece is on the claims ledger.
    if field('draft') != 'true':
        if slug not in STACK_IDS:
            fails.append('not on the map: add the slug to one layer in src/data/stack.ts')
        if deep and not claims_homed_at(slug):
            fails.append('deep piece carries no claim: no entry in src/data/claims.ts has this id or home')
        if not deep and cat == 'Analysis' and slug not in CLAIM_IDS:
            fails.append('Analysis piece has no entry in src/data/claims.ts')
    if field('updated') and not field('updateNote'):
        fails.append('updated is set without an updateNote saying what changed')

    # ── style
    prose = re.sub(r'<[^>]+>', '', storyline(body))
    for pat, label in BANNED:
        hits = re.findall(pat, re.sub(r'<[^>]+>', '', body), re.I)
        if hits:
            fails.append(f'{label} appears {len(hits)}x')
    # length and numbers budget, measured on the reading body only (WRITING-FORMAT §4, §4b);
    # in a deep piece, on the plain-English top only (§D)
    rb = reading_text(storyline(body.split(LAYER_HR)[0]))
    if deep:
        words = len(rb.split())
        lo, hi = DEEP_TOP_WORDS
        if not lo <= words <= hi:
            fails.append(f'top layer is {words} words; a deep piece\'s plain-English top is {lo} to {hi} (§D asks about 400 to 550)')
        elif not 400 <= words <= 550:
            warns.append(f'top layer is {words} words; §D asks about 400 to 550')
        figures = len(re.findall(FIGURE_RE, rb))
        if figures > DEEP_TOP_FIGURES:
            fails.append(f'{figures} figures in the top layer; §D allows {DEEP_TOP_FIGURES}')
        inv = storyline(body.split(LAYER_HR, 1)[1].split('<section class="exposure">')[0])
        iw = len(re.sub(r'<[^>]+>', ' ', inv).split())
        if iw > DEEP_INVESTOR_WORDS:
            fails.append(f'investor layer is {iw} words before the exposure map; §D allows {DEEP_INVESTOR_WORDS:,}')
        elif iw < 900:
            warns.append(f'investor layer storyline is {iw} words; STORY-RULES.md asks about 900 to 2,000')
    else:
        words = len(rb.split())
        if words > 700:
            fails.append(f'{words} words; a journal piece is 450 to 600 in the body (about 5 minutes), never over 700')
        elif not 400 <= words <= 600:
            warns.append(f'{words} words; the format asks for 450 to 600')
        figures = len(re.findall(FIGURE_RE, rb))
        if figures > 25:
            fails.append(f'{figures} figures in the body; §4b allows 15')
        elif figures > 15:
            warns.append(f'{figures} figures in the body; §4b asks for 15 at most')
    money = len(re.findall(r'(?:(?:US|S|HK)?\$|€|£|¥)\s?\d[\d.,]*(?:\s*(?:billion|million|bn)\b)?|(?<![\d.,$€£¥])\d[\d.,]*\s*(?:billion|million|bn)\b', rb))
    if money > 4:
        fails.append(f'{money} money figures; the journal allows 3 company financial figures (§4b), the numbers live in the research note')
    elif money > 3:
        warns.append(f'{money} money figures; §4b allows 3')
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
