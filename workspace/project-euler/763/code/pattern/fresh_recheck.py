# Fresh independent re-check of the max-level decomposition and a probe of
# whether the level histogram determines the config (i.e. counts of configs
# sharing one histogram might factor).
from fractions import Fraction
import glob, re
from collections import defaultdict

# ---- build (N,M) histogram from raw data ----
hist = {}
for path in sorted(glob.glob('data/level_*.txt'), key=lambda p: int(p.split('_')[1].split('.')[0])):
    N = int(path.split('_')[1].split('.')[0])
    c = {}
    for line in open(path):
        line = line.strip()
        if not line: continue
        parts = line.split('|')
        M = int(parts[1].strip())
        c[M] = c.get(M,0)+1
    hist[N] = c

for line in open('code/out/mhist_13_14.txt'):
    line=line.strip()
    if 'M=' in line:
        m = re.match(r'N=(\d+) M=(\d+): (\d+)', line)
        if m:
            N,M,cnt = int(m.group(1)),int(m.group(2)),int(m.group(3))
            hist.setdefault(N,{})[M]=cnt

Q = defaultdict(dict)
for N in sorted(hist):
    for M,cnt in hist[N].items():
        k = N-M
        exp = N-2*k-1
        if exp<0: continue
        Q[k][N] = Fraction(cnt)/Fraction(3**exp)

print("Q_k columns (exact rationals):")
for k in sorted(Q):
    pts=sorted(Q[k])
    print(f"  k={k}: N={pts} vals={[str(Q[k][n]) for n in pts]}")

# leading coefficient via top finite difference over available points
def fin_diff(vals):
    v=list(vals)
    out=[]
    while len(v)>1:
        v=[v[i+1]-v[i] for i in range(len(v)-1)]
        out.append(v)
    return out
print("\nLeading-coeff (top finite diff) check for each k with enough points:")
for k in sorted(Q):
    pts=sorted(Q[k]); vals=[Q[k][n] for n in pts]
    # degree-k polynomial needs k+1 points; leading coeff = top-diff/(k!)
    need=k+1
    if len(pts)>=need:
        # take last need points (highest N, stable)
        spts=pts[-need:]; svals=[Q[k][n] for n in spts]
        levels=fin_diff(svals)
        top=levels[-1][0] if levels else svals[0]
        # leading coeff = top-diff derived at spacing 1 over degree k
        # for exact polynomial of degree k, k-th diff = k! * a_k ... but that's
        # only if all k+1 points on one polynomial. Check separately.
        leading_guess=top/Fraction(1)
    # simpler: compute kth finite difference at the LAST point using all available
    if len(pts)>=k+1:
        vals_full=[Q[k][n] for n in pts]
        fd=fin_diff(vals_full)
        kth=fd[k-1][-1] if k>=1 else vals_full[-1]
        print(f"  k={k}: #pts={len(pts)} kth-diff(last,spacing1)={kth} ; conjectured leading*a*k! , check equals 1? -> {kth}")
    else:
        print(f"  k={k}: only {len(pts)} pts, not enough (need {k+1})")

print("\n--- histogram-vs-config probe (N=4, 30 configs) ---")
byh=defaultdict(int)
for line in open('data/level_4.txt'):
    h=line.split('|')[0].strip(); byh[h]+=1
for h,cnt in sorted(byh.items()):
    print(f"  hist {h}: {cnt} configs")
