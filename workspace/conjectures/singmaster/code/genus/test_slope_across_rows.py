"""Test the emerging slope conjecture across the whole verified table:
genus(C(x,m)=C(y,n)) grows linearly in n with slope (m-1)/2,
with a periodic-in-n correction of period m. Test on every row that has
enough points."""
from genus_table import TABLE

rows = {}
for (a,b), g in TABLE.items():
    m, n = sorted((a,b))
    rows.setdefault(m, []).append((n,g))
for m in sorted(rows):
    rows[m] = sorted(rows[m])

print("m : mean first-diff (should -> (m-1)/2) | n range | #pts | diffs")
for m in sorted(rows):
    pts = rows[m]
    if len(pts) < 4:
        print(f"{m}: too few pts {pts}")
        continue
    diffs = [pts[i+1][1]-pts[i][1] for i in range(len(pts)-1)]
    # For period-m diffs, mean over a full window predicts slope
    # Use final window of length len(pts)-1, mean
    mean = sum(diffs)/len(diffs)
    pred = (m-1)/2
    ok = abs(mean-pred) < 1e-6
    print(f"{m}: mean={mean:.3f} pred={(m-1)/2} {'OK' if ok else f'DIFF {mean-pred:+.3f}'} | n={pts[0][0]}..{pts[-1][0]} | {len(pts)} | {diffs}")
