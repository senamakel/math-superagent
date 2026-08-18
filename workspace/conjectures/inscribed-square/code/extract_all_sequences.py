from pathlib import Path
import re
for p in Path('.').rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.name=='trace.jsonl': continue
    try: text=p.read_text()
    except: continue
    for m in re.finditer(r'\[\s*(-?\d+(?:\s*,\s*-?\d+)+)\s*\]', text):
        vals=tuple(int(x) for x in re.findall(r'-?\d+',m.group(1)))
        if len(vals)>=3: print(p, vals)
