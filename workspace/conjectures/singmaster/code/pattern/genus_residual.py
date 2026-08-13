"""Residual structure of genus(m,n) against the slope (m-1)/2:
compute R = 2g - (m-1)*n over the verified table, grouped by m and n mod m.
If the slope conjecture holds with a period-m correction, R is periodic in n
with period m (exactly, over the table). Reports the exact correction.
"""
from code.genus.genus_table import TABLE

rows = {}
for (a, b), g in TABLE.items():
    m, n = sorted((a, b))
    rows.setdefault(m, []).append((n, g))
for m in sorted(rows):
    rows[m] = sorted(rows[m])

print("m : (n mod m) -> R = 2g - (m-1)n   (want: constant within each residue)")
for m in sorted(rows):
    pts = rows[m]
    groups = {}
    for n, g in pts:
        r = n % m
        R = 2 * g - (m - 1) * n
        groups.setdefault(r, []).append((n, R))
    line = []
    for r in sorted(groups):
        vals = sorted(set(R for _, R in groups[r]))
        # how many distinct R per residue
        line.append(f"r{r}:{vals if len(vals) <= 3 else str(len(vals)) + 'vals'}")
    print(f"m={m}: {'; '.join(line)}")

print()
print("Exact R values per m (each entry 'n->R'):")
for m in sorted(rows):
    pts = rows[m]
    print(f"m={m}: " + " ".join(f"{n}->{2*g-(m-1)*n}" for n, g in pts))