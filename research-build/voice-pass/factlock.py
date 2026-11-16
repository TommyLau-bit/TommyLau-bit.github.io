#!/usr/bin/env python3
"""Fact lock for the voice pass. Usage: factlock.py <path relative to repo> [base ref, default main]
Compares the file on the base ref with the working copy: every number, URL, anchor id,
image src and claim id must survive unchanged (as a multiset). Also flags em dashes and
banned AI phrasing in the new text. Exit 1 on any fact difference."""
import re, subprocess, sys, collections
if sys.argv[1] == '--files':
    # factlock.py --files <original copy> <edited file>  (for files outside the journal repo)
    old = open(sys.argv[2]).read(); new = open(sys.argv[3]).read(); path = sys.argv[3]
else:
    path = sys.argv[1]; base = sys.argv[2] if len(sys.argv) > 2 else 'main'
    old = subprocess.run(['git', 'show', f'{base}:{path}'], capture_output=True, text=True, cwd='/Users/tommylau/Desktop/journal').stdout
    new = open('/Users/tommylau/Desktop/journal/' + path).read()
def grab(t):
    return {
        'numbers': collections.Counter(re.findall(r'(?<![\w#-])\d[\d,]*(?:\.\d+)?(?:%|bn|m|GW|MW|kW|GWh|MWh)?', re.sub(r'<svg.*?</svg>', ' ', t, flags=re.S))),
        'urls': collections.Counter(re.findall(r'https?://[^\s)"\'<>\]]+', t)),
        'ids': collections.Counter(re.findall(r'id="([^"]+)"', t)),
        'srcs': collections.Counter(re.findall(r'src="([^"]+)"', t)),
        'svg': collections.Counter([s for s in re.findall(r'<svg.*?</svg>', t, flags=re.S)]),
    }
o, n = grab(old), grab(new)
bad = False
for k in o:
    if o[k] != n[k]:
        lost = o[k] - n[k]; added = n[k] - o[k]
        if k == 'svg':
            # svg text labels may be reworded; only flag if numbers inside changed
            on = collections.Counter(re.findall(r'\d[\d.,]*', ''.join(o[k].elements())))
            nn = collections.Counter(re.findall(r'\d[\d.,]*', ''.join(n[k].elements())))
            if on == nn: continue
            lost, added = on - nn, nn - on
        bad = True
        print(f'FACT CHANGE [{k}] lost={dict(lost)} added={dict(added)}')
em = new.count('—')
if em: bad = True; print(f'EM DASHES: {em}')
banned = ['underscore', 'crucially', 'notably', 'landscape', 'navigate', 'robust', 'leverage', 'pivotal', 'delve', 'tapestry', 'nuanced', 'in essence', 'it is worth noting', 'the whole story', 'the real story', 'here is the part', 'turns the usual picture']
hits = [b for b in banned if re.search(r'\b' + re.escape(b), new, re.I) and not re.search(r'\b' + re.escape(b), old, re.I)]
if hits: print('NEW AI PHRASES:', hits)
print('FACT LOCK', 'FAIL' if bad else 'PASS', path)
sys.exit(1 if bad else 0)
