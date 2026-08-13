"""Out-of-sample falsification test for the unified genus formula

    g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2          (2 <= m < n)

(the symmetric form; algebraically identical to ((m-1)n - (m-2) -
gcd(n,m))/2, and symmetric in m and n. Each candidate is stored with
m < n, so the two forms agree on every row.)

The formula is `checked` against 116 previously computed points (TABLE grid
k1<=12, k2.3/4/5 rows to k1=24, extensions m=6..10 to n=19, three diagonal
families to n=22), ALL inside the region it was fitted against.

This run attacks it out of sample: predict g for pairs no Singular run has
ever computed, then compute them freshly with Singular's normal.lib::genus
and compare. Any mismatch REFUTES the formula as stated. Column m=13..16 has
never been touched (no (13,n) pair exceeds n=13 via symmetry into the table),
and residues n mod m = 0 (large gcd) were rarely computed.

Prediction failure modes this deliberately samples:
  * new column m=13,14,15,16   (formula's linear-in-n + gcd term extrapolates)
  * gcd(m,n) = m  (residue 0, the large-gcd correction term)
  * gcd(m,n) = 2..14 between 1 and m
  * rows 2,3,5,10 pushed past their last computed n, which the diagonal
    closed forms independently predict (floor((n-1)/2), n-1 or n-2, 2n-4/2n-5)

Method (mirrors the established grid runs): Singular 4.3.1, normal.lib,
genus(ideal) = geometric genus of projective closure by resolution of
singularities, exact integer arithmetic, same CB() proc as extend_*.sing.

Complexity: 17 Singular genus calls on curves of bidegree <= 416, each a
resolution computation on a degree <= 30 plane curve; seconds per call.
"""
import subprocess
import sys
import re
from math import gcd
from genus.genus_table import TABLE

# ---------------------------------------------------------------- candidates
CANDIDATES = [
    (2, 13), (3, 25), (5, 25), (10, 20),          # rows 2,3,5,10 past last n
    (13, 17), (13, 19), (13, 26),                  # new column 13 (gcd 1,1,13)
    (14, 18), (14, 23), (14, 28),                  # new column 14 (gcd 2,1,14)
    (15, 19), (15, 20), (15, 26),                  # new column 15 (gcd 1,5,1)
    (16, 19), (16, 21), (16, 24), (16, 26),        # new column 16 (gcd 1,1,8,2)
]

def gform(m, n):
    """Genus of the projective closure of C(x,m) = C(y,n), m != n."""
    return ((m - 1) * (n - 1) + 1 - gcd(m, n)) // 2


# Singular emits PAIR lines on ONE line:  PAIR {m,n} genus= <value>.
# In some versions the value is followed (not preceded) by the
# "// ** redefining ..." warnings because they are printed AFTER the
# value on the same stream; split()-and-take-last then captured the
# warning, and int() threw, so the row was silently dropped. Match one
# whole line instead and never touch anything around it.
PAIR_RE = re.compile(r"^PAIR \{(\d+),(\d+)\} genus=\s*(\d+)\s*$")

# ------------------------------------------------- covered-pair bookkeeping
covered = set()
for (a, b) in TABLE:
    covered.add(tuple(sorted((a, b))))
# verify_closed.py extensions: k2=3,4,5 with k1=13..24 (as unordered pairs)
for k1 in range(13, 25):
    for k2 in (3, 4, 5):
        covered.add(tuple(sorted((k1, k2))))
# verify_genus_formula.py EXT: rows m=6..10 to n=13..19
EXT = {(6,13),(6,14),(6,15),(6,16),(6,17),(6,18),(7,13),(7,14),(7,15),
       (8,13),(8,14),(8,15),(8,16),(9,13),(9,14),(9,15),(9,16),(9,17),
       (10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(10,19)}
covered |= EXT
# diagonal families: {n-1,n} n=3..22 ; {n-2,n} n=4..21 (n+2 direction same sets)
for n in range(3, 23):
    covered.add((n - 1, n))
for n in range(4, 22):
    covered.add((n - 2, n))

uncov = [p for p in CANDIDATES if tuple(sorted(p)) not in covered]
print(f"Candidates: {len(CANDIDATES)}; already covered by prior runs: "
      f"{len(CANDIDATES) - len(uncov)}; out-of-sample: {len(uncov)}")
for (m, n) in CANDIDATES:
    tag = "COVERED" if tuple(sorted((m, n))) in covered else "NEW"
    print(f"  {tag}  {{{m},{n}}}  gcd={gcd(m, n)}  predict g={gform(m, n)}")

# ------------------------------------------------------------- run Singular
sing = r"""
LIB "normal.lib";
ring r=0,(x,y),dp;
proc CB(xx, k)
{
  poly p = 1;
  int i;
  for(i=0;i<k;i++){ p = p*(xx-i); }
  return(p/factorial(k));
}
"""
for (m, n) in CANDIDATES:
    sing += f'poly F = CB(x,{m}) - CB(y,{n});\n'
    sing += f'ideal I = F;\n'
    sing += f'"PAIR {{{m},{n}}} genus=", genus(I);\n'

proc = subprocess.run(["Singular", "-q"], input=sing, capture_output=True,
                      text=True, timeout=580)
print("\n--- Singular stdout ---")
print(proc.stdout)
if proc.returncode != 0:
    print("Singular exit code:", proc.returncode)
    print("--- Singular stderr (tail) ---")
    print("\n".join(proc.stderr.splitlines()[-15:]))
    sys.exit(2)

# ---------------------------------------------------------------- compare
results = {}
for line in proc.stdout.splitlines():
    m = PAIR_RE.match(line)
    if m is not None:
        key = tuple(sorted((int(m.group(1)), int(m.group(2)))))
        val = int(m.group(3))
        results[key] = val

print("\n--- Comparison ---")
mism = []
for (m, n) in CANDIDATES:
    key = tuple(sorted((m, n)))
    pred = gform(*key)
    got = results.get(key)
    ok = (got == pred)
    print(f"  {{{m},{n}}}: predicted {pred:4d}  Singular {got}  "
          f"{'MATCH' if ok else '*** MISMATCH ***'}")
    if not ok:
        mism.append((m, n, pred, got))

print(f"\nSingular returned {len(results)} of {len(CANDIDATES)} pairs")
print(f"MISMATCHES: {len(mism)}")
for x in mism:
    print("   ", x)
print("VERDICT:", "FORMULA REFUTED" if mism else
      "formula survives out-of-sample Singular recomputation")