"""Extract integer sequences from the OeS Goldbach verification top-50 table.
Evidence only; it does not test Goldbach itself. Source: research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md.
"""
from pathlib import Path
import re

p = Path('research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md')
text = p.read_text()
rows = []
for line in text.splitlines():
    m = re.match(r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([0-9 ]+)\s*\|', line)
    if m:
        rank = int(m.group(1)); least = int(m.group(2))
        S = int(m.group(3).replace(' ', ''))
        rows.append((rank, least, S))
print('rows', len(rows))
print('rank', [x[0] for x in rows])
print('least_prime', [x[1] for x in rows])
print('S', [x[2] for x in rows])
print('least_prime_ascending', [x[1] for x in reversed(rows)])
print('S_ascending_by_least_prime', [x[2] for x in reversed(rows)])
