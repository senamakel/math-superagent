"""Test the general hypothesis for genus(m,n) of C(x,m)=C(y,n) with m small:
slope ((m-1)/2)*n plus a periodic-in-n correction of period m (as verified for
m=2,3,4,5). Uses the verified table from genus_table.py."""
from genus_table import TABLE, spam_genus

# gather rows: for each small m, list (n, genus), n>m
rows = {}
for (a,b), g in TABLE.items():
    m, n = sorted((a,b))  # m small, n large
    rows.setdefault(m, []).append((n,g))
for m in sorted(rows):
    rows[m] = sorted(rows[m])

print("=== slope test: g(m,n) vs ((m-1)/2)*n ===")
for m in sorted(rows):
    pts = rows[m]
    if len(pts) < 3:
        print(f"m={m}: only {len(pts)} pts", pts)
        continue
    # linear fit slope via last few consecutive points (local slope)
    slope = (pts[-1][1]-pts[-2][1])/(pts[-1][0]-pts[-2][0]) if pts[-1][0]!=pts[-2][0] else 0
    print(f"m={m}: pts={[(n,g) for n,g in pts]} local-last-slope={slope:.3f} predicted={(m-1)/2}")

print("\n=== periodic-diff structure for each row ===")
for m in sorted(rows):
    pts = sorted(rows[m])
    diffs = [pts[i+1][1]-pts[i][1] for i in range(len(pts)-1)]
    ns = [pts[i][0] for i in range(len(pts))]
    print(f"m={m}: n={ns} diffs={diffs}")

print("\n=== cross-check verified closed forms (spam_genus) vs table ===")
for m in (2,3,4,5):
    mism=[]
    for n,g in rows.get(m,[]):
        if n==m: continue
        v=spam_genus(m,n)
        if v!=g: mism.append((n,g,v))
    print(f"m={m}: closed-form mismatches over table: {len(mism)} {mism[:6]}")
