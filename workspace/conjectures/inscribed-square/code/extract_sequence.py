"""Extract numeric sequences from existing result artifacts; no new search."""
from pathlib import Path
import re

files = [Path('code/out/sequence_provisional.md'), Path('code/brute.py')]
for p in files:
    text = p.read_text()
    print(p)
    for m in re.finditer(r'\[([0-9]+(?:\s*,\s*[0-9]+)+)\]', text):
        print('sequence:', [int(x) for x in m.group(1).split(',')])
