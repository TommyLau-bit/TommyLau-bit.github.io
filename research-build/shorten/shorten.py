"""Shorten a journal piece safely (9 Nov 2026).

  python3 research-build/shorten/shorten.py extract <slug>
      Saves research-build/shorten/<slug>/original.md (a copy of the live piece) and
      prose.md: the piece's prose with every figure replaced by {{FIGn}}, the analogy
      fold by {{ANALOGY}}, and everything from the claims-record fold onward removed.
      Write the shortened prose to research-build/shorten/<slug>/short.md, keeping the
      placeholders you want (every {{FIGn}} you keep, and {{ANALOGY}}).

  python3 research-build/shorten/shorten.py assemble <slug>
      Rebuilds src/content/journal/<slug>.md from frontmatter + short.md (placeholders
      filled from the original) + the untouched tail (claims record, evidence, exposure
      map, sources), then checks: every anchor id kept, no number in the new prose
      that is not in the original, the study sheet's numbers still present, no dashes,
      visible word count, and the piece checker.
"""
import re, sys, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'research-build' / 'shorten'
FIG_RE = re.compile(r'<figure class="(?:chart|illo)">.*?</figure>', re.S)
SHEETS = {
    'the-queue-not-the-chip': 1, 'america-rations-the-plug': 2, 'building-your-own-power': 3,
    'the-equipment-queue': 4, 'powering-the-rack': 5, 'heat-and-water': 6,
    'nuclear-for-ai': 7, 'microreactors': 8, 'data-centres-in-space': 9,
}

def parts(text):
    fm_end = text.index('---', 3) + 3
    fm, body = text[:fm_end], text[fm_end:]
    tail_at = body.index('<details class="claims-record">')
    return fm, body[:tail_at], body[tail_at:]

def visible_words(text):
    s = text.split('---', 2)[2]
    s = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
    s = re.sub(r'<details.*?</details>', '', s, flags=re.S)
    s = re.sub(r'<figure.*?</figure>', '', s, flags=re.S)
    s = s.split('<section class="exposure">')[0]
    return len(re.findall(r"[A-Za-z0-9£$€%'’-]+", re.sub(r'<[^>]+>', ' ', s)))

def nums(t):
    return {n.replace(',', '') for n in re.findall(r'\d[\d,]*(?:\.\d+)?', t)}

def extract(slug):
    d = WORK / slug; d.mkdir(parents=True, exist_ok=True)
    text = (ROOT / f'src/content/journal/{slug}.md').read_text()
    (d / 'original.md').write_text(text)
    fm, prose, tail = parts(text)
    figs = FIG_RE.findall(prose)
    for i, f in enumerate(figs, 1):
        title = re.search(r'class="(?:illo|chart)-title">(.*?)</p>', f) or re.search(r'<p class="[^"]*title[^"]*">(.*?)</p>', f)
        prose = prose.replace(f, '{{FIG%d}}  <!-- %s -->' % (i, title.group(1) if title else 'figure'), 1)
    prose = re.sub(r'<details class="analogy">.*?</details>', '{{ANALOGY}}', prose, flags=re.S)
    (d / 'prose.md').write_text(prose.strip() + '\n')
    print(f'{slug}: {len(figs)} figures; {visible_words(text)} visible words now')
    print('anchors:', ' '.join(re.findall(r'<a id="([^"]+)"', prose)))
    print('wrote', d / 'prose.md')

def assemble(slug):
    d = WORK / slug
    orig = (d / 'original.md').read_text()
    fm, prose, tail = parts(orig)
    figs = FIG_RE.findall(prose)
    analogy = re.search(r'<details class="analogy">.*?</details>', prose, re.S).group(0)
    short = (d / 'short.md').read_text()
    short = re.sub(r'\s*<!--.*?-->', '', short)
    body = short.replace('{{ANALOGY}}', analogy)
    for i, f in enumerate(figs, 1):
        body = body.replace('{{FIG%d}}' % i, f)
    problems = []
    if '{{' in body:
        problems.append('unfilled placeholder: ' + ', '.join(set(re.findall(r'\{\{\w+\}\}', body))))
    new = fm + '\n\n' + body.strip() + '\n\n' + tail
    (ROOT / f'src/content/journal/{slug}.md').write_text(new)
    lost = set(re.findall(r'id="([^"]+)"', orig)) - set(re.findall(r'id="([^"]+)"', new))
    if lost: problems.append('anchors lost: ' + ', '.join(sorted(lost)))
    fresh = nums(re.sub(r'\{\{\w+\}\}', '', short)) - nums(orig)
    if fresh: problems.append('numbers not in the original: ' + ', '.join(sorted(fresh)))
    if re.search('[—–]', short): problems.append('em or en dash in the new prose')
    sheet = next((ROOT / 'study-decks').glob(f'Study sheet {SHEETS[slug]} - *.md'), None)
    if sheet:
        have = nums(new + (ROOT / 'src/data/claims.ts').read_text())
        gone = sorted(n for n in nums(sheet.read_text()) if len(n) > 1 and n not in have)
        if gone: problems.append(f'study sheet numbers no longer in the piece: {", ".join(gone)} (check each: fine only if the sheet got it from SemiAnalysis or Tommy\'s application)')
    kept = len(FIG_RE.findall(body))
    print(f'{slug}: visible words {visible_words(orig)} -> {visible_words(new)}; figures {len(figs)} -> {kept}')
    r = subprocess.run(['python3', 'brand/check-piece.py', f'src/content/journal/{slug}.md'], cwd=ROOT, capture_output=True, text=True)
    print(r.stdout.strip())
    print('PROBLEMS:\n- ' + '\n- '.join(problems) if problems else 'no problems found')

if __name__ == '__main__':
    {'extract': extract, 'assemble': assemble}[sys.argv[1]](sys.argv[2])
