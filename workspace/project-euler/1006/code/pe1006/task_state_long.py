"""Build length-k factor sets and compute exact STATE quantities for k=1..KMAX.

For each k the length-k factor set = set of distinct length-k substrings of a
long enough prefix of the infinite Fibonacci word f. We record:

  P(k)  = Psi(k) = sum of squares
  S(k)  = sum of values
  N1(k) = #{ length-k factors w : w+'1' is a factor }
  N0(k) = #{ length-k factors w : w+'0' is a factor }
  P1(k) = sum of values v_w over w with w+'1' a factor
  vR(k) = value of the unique right-special factor

Verification: Psi(k+1) = 100*(P+vR^2) + 20*P1 + N1  (extension formula).

Writes exact state to code/out/psi_state_1_<KMAX>.txt; checks extension
formula; and saves the mod-M residues of a candidate augmented state for a
Berlekamp-Massey recurrence search.
"""
import os, sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
MOD = 101001001

a, b = "0", "01"
while len(b) < 3 * KMAX + 50:
    a, b = b, b + a
f = b  # prefix of infinite Fibonacci word, long enough

# cache windows sets lazily
windows = {}
def win(k):
    if k not in windows:
        windows[k] = {f[i:i+k] for i in range(len(f) - k + 1)}
    return windows[k]

rows = []
for k in range(1, KMAX + 1):
    wk = win(k)
    assert len(wk) == k + 1, (k, len(wk))
    vals = {w: int(w) for w in wk}
    P = sum(v * v for v in vals.values())
    S = sum(vals.values())
    wk1 = win(k + 1)
    N1 = sum(1 for w in wk if w + '1' in wk1)
    N0 = sum(1 for w in wk if w + '0' in wk1)
    P1 = sum(vals[w] for w in wk if w + '1' in wk1)
    vR = next(vals[w] for w in wk if (w + '0' in wk1) and (w + '1' in wk1))
    rows.append(dict(k=k, P=P, S=S, N1=N1, N0=N0, P1=P1, vR=vR))

# verify extension formula
ok = True
for i in range(len(rows) - 1):
    r = rows[i]
    pred = 100 * (r["P"] + r["vR"] * r["vR"]) + 20 * r["P1"] + r["N1"]
    if pred != rows[i + 1]["P"]:
        ok = False
        print("MISMATCH at k=", r["k"], pred, rows[i+1]["P"])
print("extension formula held for k=1..%d:" % (len(rows)-1), ok)

out = os.path.join(os.path.dirname(__file__), "..", "out")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, f"psi_state_1_{KMAX}.txt")
with open(path, "w") as fh:
    fh.write("k,P_mod,S_mod,N1,N0,P1_mod,vR_mod\n")
    for r in rows:
        fh.write(f"{r['k']},{r['P']%MOD},{r['S']%MOD},{r['N1']},{r['N0']},{r['P1']%MOD},{r['vR']%MOD}\n")
print("wrote", path)

# Berlekamp-Massey over GF(MOD) on candidate sequences.
def berlekamp_massey(s, mod):
    """Return a generator polynomial c (list, c[0]=1) such that
    sum_i c[i]*s[n-i] = 0 for n>=len(c)-1, over GF(mod)."""
    C = [1]
    B = [1]
    L = 0
    m = 1
    b = 1
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            d = (d + C[i] * s[n - i]) % mod
        if d == 0:
            m += 1
        elif 2 * L <= n:
            T = C[:]
            coef = d * pow(b, mod - 2, mod) % mod
            if len(C) < len(B) + m:
                C += [0] * (len(B) + m - len(C))
            for j in range(len(B)):
                C[j + m] = (C[j + m] - coef * B[j]) % mod
            L = n + 1 - L
            B = T
            b = d
            m = 1
        else:
            coef = d * pow(b, mod - 2, mod) % mod
            if len(C) < len(B) + m:
                C += [0] * (len(B) + m - len(C))
            for j in range(len(B)):
                C[j + m] = (C[j + m] - coef * B[j]) % mod
            m += 1
    return C, L

Pseq = [r["P"] % MOD for r in rows]
for name, seq in [("P", Pseq),
                  ("P,P1,S,vR", [ (r["P"]*1000 + r["P1"]*100 + r["S"] + r["vR"]) % MOD for r in rows])]:
    C, L = berlekamp_massey(seq, MOD)
    print(f"BM on {name}: order={L}")

# Try augmented state vector: does (P_{n+1},P_n,...,?) follow small recurrence?
print("\nBM on sum/detail separate:")
# Test P itself for small order using more terms
for start in [0, 200]:
    pass
