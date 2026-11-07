"""The single depth launch (Tommy, 7 Nov 2026): move the nine depth drafts onto their live URLs.

  python3 research-build/deep-pieces/launch.py            # does it
Run once, on the launch branch, after every draft has passed its fact-check, the checker and the build.
Then run the checkers, make-og, the build and the link check before merging to main.
"""
import os, re, shutil, datetime, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
J = os.path.join(ROOT, 'src/content/journal'); A = os.path.join(ROOT, 'research-build/archive/pieces')
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).replace(microsecond=0)
STAMP = now.isoformat(); DAY = now.date().isoformat()

# depth draft -> live slug, and the updateNote shown under the title
MOVES = {
 'johor-singapore-depth': ('the-queue-not-the-chip', 'Rebuilt in depth: every gate from application to a working hall explained and mapped, with Hong Kong folded in, and evidence to 7 November 2026.'),
 'nuclear-for-ai-depth': ('nuclear-for-ai', 'Rebuilt in depth: the fuel chain from mine to core explained step by step and drawn, with evidence to 7 November 2026.'),
 'building-your-own-power-depth': ('building-your-own-power', 'Rebuilt in depth: how an off-grid campus is powered, what each machine does and why the turbine queue sets the date, with evidence to 7 November 2026.'),
 'the-equipment-queue-depth': ('the-equipment-queue', 'Rebuilt in depth: what a transformer and switchgear do, how they are made and why the wait persists, with evidence to 7 November 2026.'),
 'america-rations-the-plug-depth': ('america-rations-the-plug', 'Rebuilt in depth: the path from application to running explained and mapped, with Abilene and Nebius folded in, and evidence to 7 November 2026.'),
 'powering-the-rack-depth': ('powering-the-rack', 'Rebuilt in depth: one megawatt from the grid to the chip, every step explained and drawn, with evidence to 7 November 2026.'),
 'heat-and-water-depth': ('heat-and-water', 'Rebuilt in depth: one watt of heat from the chip to the sky, every machine explained and drawn, with evidence to 7 November 2026.'),
 'data-centres-in-space-depth': ('data-centres-in-space', 'Rebuilt in depth: what an orbital data centre weighs, part by part, against the launch fare, with evidence to 7 November 2026.'),
}
FOLDED = {'contracted-energised-running': 'america-rations-the-plug', 'hong-kong-has-the-plug': 'the-queue-not-the-chip'}

def fm_set(s, key, val):
    head, body = s.split('\n---\n', 1) if s.startswith('---\n') else (None, None)
    assert head, 'no frontmatter'
    if re.search(rf'^{key}:', head, re.M):
        head = re.sub(rf'^{key}:.*$', f'{key}: {val}', head, count=1, flags=re.M)
    else:
        head += f'\n{key}: {val}'
    return head + '\n---\n' + body

def git(*a): subprocess.run(['git', *a], cwd=ROOT, check=True)

# 1 archive the live text of every piece being replaced or folded, verbatim
for live in [m[0] for m in MOVES.values()] + list(FOLDED):
    dst = os.path.join(A, f'{live}--pre-depth-2026-11-07.md')
    assert not os.path.exists(dst), dst
    shutil.copy(os.path.join(J, live + '.md'), dst)

# 2 the depth drafts take the live URLs: original date kept, updated today, draft off
for draft, (live, note) in MOVES.items():
    old = open(os.path.join(J, live + '.md')).read()
    date = re.search(r'^date: (.+)$', old, re.M).group(1).strip()
    s = open(os.path.join(J, draft + '.md')).read()
    s = fm_set(s, 'date', date); s = fm_set(s, 'draft', 'false')
    s = fm_set(s, 'updated', DAY); s = fm_set(s, 'updateNote', '"' + note + '"')
    open(os.path.join(J, live + '.md'), 'w').write(s)
    git('rm', '-q', f'src/content/journal/{draft}.md')

# 3 microreactors is new: it goes live now
p = os.path.join(J, 'microreactors.md'); s = open(p).read()
s = fm_set(s, 'date', STAMP); s = fm_set(s, 'draft', 'false'); open(p, 'w').write(s)

# 4 folded pieces leave src; their URLs redirect to their anchors in the deep piece
for old in FOLDED: git('rm', '-q', f'src/content/journal/{old}.md')
cfg = os.path.join(ROOT, 'astro.config.mjs'); c = open(cfg).read()
c = c.replace("'/journal/contracted-energised-running/#", "'/journal/america-rations-the-plug/#")
add = ("  // folded into the depth pieces, 7 Nov 2026\n"
       "  '/journal/contracted-energised-running': '/journal/america-rations-the-plug/#contracted-energised-running',\n"
       "  '/journal/hong-kong-has-the-plug': '/journal/the-queue-not-the-chip/#hong-kong-has-the-plug',\n")
anchor = "  // contracted-energised-running\n"
assert c.count(anchor) == 1; c = c.replace(anchor, add + anchor); open(cfg, 'w').write(c)

# 5 claims: new claims dated at launch; homes follow the pieces
ct = os.path.join(ROOT, 'src/data/claims.ts'); t = open(ct).read()
def claim_blk(cid):
    i = t.index(f"id: '{cid}'"); j = t.index('\n  },', i); return i, j
def set_field(cid, key, val):
    global t
    i, j = claim_blk(cid); blk = t[i:j]
    if re.search(rf"\n\s+{key}: '", blk): blk = re.sub(rf"(\n\s+){key}: '[^']*'", rf"\g<1>{key}: '{val}'", blk, count=1)
    else: blk = blk.replace(f"id: '{cid}',", f"id: '{cid}',\n    {key}: '{val}',", 1)
    t = t[:i] + blk + t[j:]
for cid in ('microreactors', 'johor-singapore-rights', 'nuclear-order-of-holdings'): set_field(cid, 'date', STAMP)
set_field('johor-singapore-rights', 'home', 'the-queue-not-the-chip')
set_field('nuclear-order-of-holdings', 'home', 'nuclear-for-ai')
set_field('hong-kong-has-the-plug', 'home', 'the-queue-not-the-chip')
for cid in ('contracted-energised-running', 'power-first-chips-last', 'nebius-paid-for-what-is-switched-on'): set_field(cid, 'home', 'america-rations-the-plug')
assert "home: 'contracted-energised-running'" not in t and '-depth' not in t
open(ct, 'w').write(t)

# 6 the map: microreactors onsite; folded slugs off; operators keeps its stop
st = os.path.join(ROOT, 'src/data/stack.ts'); s = open(st).read()
for a, b in (("pieces: ['the-queue-not-the-chip', 'hong-kong-has-the-plug', ", "pieces: ['the-queue-not-the-chip', "),
             ("pieces: ['building-your-own-power', 'nuclear-for-ai'],", "pieces: ['building-your-own-power', 'nuclear-for-ai', 'microreactors'],"),
             ("pieces: ['contracted-energised-running'],", "pieces: [], // folded into america-rations-the-plug 7 Nov 2026; the layer stays for the descent walk")):
    assert s.count(a) == 1, a; s = s.replace(a, b)
open(st, 'w').write(s)
print('launched at', STAMP)
