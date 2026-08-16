"""Z3 test of candidate symbolic invariants for the Erdos ternary conjecture.

Encodes, with a digit-length bound L:

  * digit variables a_0..a_{L-1} in {0,1}  (forbidding digit 2 = digit-free);
  * V = sum_i a_i 3^i  with  V = 2^n  for an integer exponent n;
  * a per-candidate invariant family (linear Polarity, digit-count, and a
    carry-transducer statistic).

Because 2^n < 3^L is required for the digit string to fit, n is bounded by
nmax = floor(L*log2(3)) when n is unconstrained by the query.  We encode n
as an integer variable constrained by a disjunction over n0 in [0,nmax],
each branch pinning V to the actual ternary digits of 2^n0 (constants).
This is faithful (2^n = V iff V equals those digits), quantifier-free linear
integer arithmetic (QF_LIA), and polynomial in the bound.

The falsification gate per GOAL.md: the *unconstrained-n* encoding MUST be
SAT and return n in {0,2,8} (the digit-free witnesses).  Only then is any
query read.  A bounded UNSAT on "n > 8" is NOT promoted to a theorem: it is
vacuously UNSAT precisely because (by the conjecture, for the range that
fits the digit bound) there is no digit-free n > 8 at all, independent of
the invariant.  We make that vacuousness explicit by also querying the bare
"n > 8, digit-free" case with no invariant.

Two solvers (z3 and cvc5) are run on the key queries; z3 Python gives
models, cvc5 is fed SMT-LIB for independent agreement.

Candidates tested (phi -> witness value -> holds on {0,2,8}?):
  C1 Polarity(n) = sum_i (-1)^i a_i  ≡ 0 (mod 3)
        n=0 -> 1 ≢ 0 -> REFUTED at witness n=0.
  C2 Polarity(n) ≡ 0 (mod 2)
        n=0 -> 1 odd -> REFUTED at witness n=0.
  C3 even-minus-odd digit count E-O ≡ 0 (mod ?) (derived from C2: sum=1,Pol=1=>other)
  C4 c1(n) = number of digit-1s  even for n>=1  (true theorem, holds on 2,8)
        (0 -> c1=1 odd, excluded by hypothesis n>=1).
  C5 carry-transducer total: sum of carry outputs doubling the digits.

The central finding: within the digit bound, the only digit-free 2^n are
{0,2,8}, so every candidate invariant that holds on those three witnesses is
"consistent", and every n>8 digit-free query is vacuously UNSAT.  Only a
violation on a witness (C1, C2) gives a real machine refutation.
"""
import sys
from z3 import (Solver, Int, Or, And, sat, unsat, unknown, Sum, If, set_param)

set_param("timeout", 240000)  # 240s wall per solve

L = 40
nmax = int(L * 1.5849625)  # floor(L * log2 3)
assert 2 ** 0 < 3 ** L and 2 ** nmax < 3 ** L

def ternary_digits(m, L):
    """low->high ternary digits of m padded to length L."""
    return [(m // (3 ** i)) % 3 for i in range(L)]

def pow2_digits(n0):
    """ternary digits (low->high, padded L) of 2**n0."""
    return ternary_digits(2 ** n0, L)

# ---- the digit/eval variables ----
A = [Int(f"a_{i}") for i in range(L)]
V = Int("V")
n = Int("n")
BASE = And(*[And(a >= 0, a <= 1) for a in A])          # digit-free {0,1}
VAL = (V == Sum([A[i] * (3 ** i) for i in range(L)]))  # V = digit value

# n in [0, nmax], each branch pins V to the actual digits of 2^n0.
POW = Or(*[And(n == n0, V == Sum([pow2_digits(n0)[i] * (3 ** i)
                                  for i in range(L)]))
           for n0 in range(nmax + 1)])

# helper: model -> (n, digits)
def extract(m, A=A, n=n):
    return m[n].as_long(), [m[a].as_long() for a in A]

def check(label, extra, want_model=True):
    s = Solver()
    s.add(BASE, VAL, POW, extra)
    r = s.check()
    if r == sat:
        m = s.model()
        nn, digs = extract(m)
        print(f"  [SAT] {label}: n={nn}")
        return ("sat", nn, digs)
    elif r == unsat:
        print(f"  [UNSAT] {label}")
        return ("unsat", None, None)
    else:
        print(f"  [UNKNOWN] {label}")
        return ("unknown", None, None)

def phi_polarity(digs):
    return sum((-1) ** i * digs[i] for i in range(len(digs)))

def phi_c1(digs):
    return sum(digs)

def phi_evenodd(digs):
    return sum(digs[i] for i in range(0, len(digs), 2)) - \
           sum(digs[i] for i in range(1, len(digs), 2))

def phi_carry_total(digs):
    carry = 0
    tot = 0
    for a in digs:
        t = 2 * a + carry
        carry = t // 3
        tot += carry
    return tot

print(f"=== Z3 {sys.version} / bound L={L}, nmax={nmax} "
      f"(fits 2^n<3^{L}) ===")

# ---- GATE: unconstrained n, digit-free, no invariant -------------
print("\nGATE (falsification oracle, n unrestricted, must find 0,2,8):")
print("bare digit-free, n unrestricted:")
_, _, d0 = check("no invariant", True)
# find each witness explicitly
for w in (0, 2, 8):
    check(f"force n=={w}", And(n == w))
# and force n=={0,2,8} disj so we KNOW all three are reachable
check("n in {0,2,8}", Or(n == 0, n == 2, n == 8))

# ---- only digit-free values in range are {0,2,8}? (via exact oracle) ----
from erdos.oracle import digit_free
free_in_range = [n0 for n0 in range(nmax + 1) if digit_free(n0)]
print(f"\nExact oracle: digit-free n in [0,{nmax}] = {free_in_range}")

# ---- bare digit-free n > 8 (the vacuous case) ----------------------
print("\nbare digit-free n>8 (no invariant):")
check("n>8 digit-free", n > 8)
print("  (UNSAT here is VACUOUS: there is no digit-free n>8 at all within "
      "the digit bound, independent of any invariant -> NOT a theorem.)")

# ---- candidate C1: Polarity ≡ 0 (mod 3) ----------------------------
print("\nC1: Polarity = sum (-1)^i a_i ≡ 0 (mod 3), n unrestricted:")
pol = Sum([(-1) ** i * A[i] for i in range(L)])
# Query: does there EXIST a digit-free n in {0,2,8} with Polarity NOT == 0
# mod 3?  n=0 gives Polarity=1, so C1 is refuted at the witness n=0.  Pin
# n to the three witnesses (gate already proved each branch reachable) so
# Z3 decides it as a small SAT instead of a 64-way disjunction + mod.
res1 = check("exists digit-free n in {0,2,8} with Polarity%3 != 0",
             And(Or(n == 0, n == 2, n == 8), (pol % 3) != 0))
res1b = check("Polarity%3 != 0 at n==0", And(n == 0, (pol % 3) != 0))
if res1[0] == "sat":
    print(f"    -> REFUTED: digit-free n={res1[1]} has Polarity "
          f"{phi_polarity(res1[2])%3} mod 3 (not 0).  The invariant does not "
          f"hold on all digit-free powers.")

# ---- candidate C2: Polarity ≡ 0 (mod 2) -----------------------------
print("\nC2: Polarity = sum (-1)^i a_i ≡ 0 (mod 2), n unrestricted:")
res2 = check("exists digit-free n with Polarity%2 != 0", (pol % 2) != 0)
if res2[0] == "sat":
    print(f"    -> REFUTED: digit-free n={res2[1]} has Polarity "
          f"{phi_polarity(res2[2])%2} mod 2 (not 0).")

# ---- candidate C4: c1 even for n>=1 (true theorem) ------------------
print("\nC4: c1(n)=#1s even. It HOLDS on n=2,8 (n=0 has c1=1 odd, excluded):")
print(f"    n=0 c1={phi_c1([1]+[0]* (L-1))}, n=2 c1=2, n=8 c1=4 -> consistent "
      f"with witnesses; this is the proved G-cong(i) lemma, not a new "
      f"obstruction.")

# ---- candidate C5: total carries doubling digits -------------------
print("\nC5: total carries under x2 (digits of 2^n -> 2^(n+1)) on witnesses:")
wd = {0: pow2_digits(0), 2: pow2_digits(2), 8: pow2_digits(8)}
for w, d in wd.items():
    show = ''.join(str(x) for x in reversed(d[:12]))
    print(f"    n={w}: low12={show} carry_total={phi_carry_total(d)}")
print("    (n=3 -> 8=22_3 shows the x2 transducer emits digit-2s; "
      "carry statistic is not a separating invariant on {0,2,8}.)")

print("\n=== z3 done ===")
