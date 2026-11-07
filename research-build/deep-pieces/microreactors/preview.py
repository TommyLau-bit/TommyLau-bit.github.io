import glob,os
css=open('/Users/tommylau/Desktop/journal/src/styles/global.css').read()
figs=''.join(f'<figure class="illo"><p class="illo-title">{os.path.basename(f)}</p>{open(f).read()}</figure>' for f in sorted(glob.glob('illos/*.svg')))
out='/private/tmp/claude-501/-Users-tommylau--claude-spares-spare-RRWPpI/9a7b8bfe-8a6d-47d8-9528-d740a682e54f/scratchpad/illos.html'
os.makedirs(os.path.dirname(out),exist_ok=True)
open(out,'w').write(f'<!doctype html><meta charset=utf-8><style>{css}</style><body><div class="wrap prose" style="max-width:54rem;margin:auto;padding:1rem">{figs}</div>')
print(out)
