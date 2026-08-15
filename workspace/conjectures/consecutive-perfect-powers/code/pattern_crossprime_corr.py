"""Cross-prime minus-class-number divisibility vs Wieferich / double-Wieferich.

Question: over odd-prime pairs (p,q), how does the divisibility
    q | h^-(Q(zeta_p))
relate to
    (a) q being a Wieferich prime base p, i.e. p^(q-1) == 1 (mod q^2),
    (b) p being a Wieferich prime base q, i.e. q^(p-1) == 1 (mod p^2),
    (c) the pair being double-Wieferich (both (a) and (b)),
    (d) irregularity of p and of q (p | h^-(p), q | h^-(q)).

Exact integer arithmetic only. h^-(Q(zeta_p)) values are the exact analytic
Bernoulli-product values already computed and captured in this run
(crossprime_sweep200.captured.txt, matched OEIS A000927 for all odd primes
<= 199): reusing them avoids a 148s recomputation and is exact.

For a fixed (p,q), 'q | h^-(p)' is a cross-prime statement about a concrete
integer, completely different from the same-prime Kummer statement p | h^-(p).
We measure the empirical co-occurrence (contingency) of these events over all
odd-prime pairs p < q <= 199.

Deliberate direction check: the double-Wieferich necessary conditions are
q^(p-1)==1 mod p^2 and p^(q-1)==1 mod q^2, so
  'q Wieferich base p'  = p^(q-1) == 1 (mod q^2)   (matches the (b)-style congruence),
  'p Wieferich base q'  = q^(p-1) == 1 (mod p^2).
We make BOTH explicit so the direction of the (claimed, not re-proved) forcing
does not get muddled.
"""
import itertools
from math import comb

# Exact h^-(Q(zeta_p)) for odd primes p <= 199, from crossprime_sweep200.captured.txt
HM = {
    3:1,5:1,7:1,11:1,13:1,17:1,19:1,23:3,29:8,31:9,37:37,41:121,43:211,
    47:695,53:4889,59:41241,61:76301,67:853513,71:3882809,73:11957417,
    79:100146415,83:838216959,89:13379363737,97:411322824001,
    101:3547404378125,103:9069094643165,107:63434933542623,109:161784800122409,
    113:1612072001362952,127:2604529186263992195,131:28496379729272136525,
    137:646901570175200968153,139:1753848916484925681747,149:687887859687174720123201,
    151:2333546653547742584439257,157:56234327700401832767069245,
    163:2708534744692077051875131636,167:28121189830322933178315382891,
    173:1702546266654155847516780034265,179:77281577212030298592756974721745,
    181:211421757749987541697225501539625,191:165008365487223656458987611326929859,
    193:546617105913568165545650752630767041,197:5532802218713600706095993713290631720,
    199:18844055286602530802019847012721555487,
}
primes = sorted(HM)
B = primes[-1]

def q_wieferich_base_p(q, p):
    """q is a Wieferich prime base p: p^(q-1) == 1 (mod q^2)."""
    return pow(p, q - 1, q * q) == 1

def p_wieferich_base_q(p, q):
    """p is a Wieferich prime base q: q^(p-1) == 1 (mod p^2)."""
    return pow(q, p - 1, p * p) == 1

rows = []
for p, q in itertools.combinations(primes, 2):
    h_p = HM[p]
    h_q = HM[q]
    A_qdivhp = (h_p % q == 0)          # q | h^-(Q(zeta_p))
    A_pdivhq = (h_q % p == 0)          # p | h^-(Q(zeta_q))
    wq = q_wieferich_base_p(q, p)      # q Wieferich base p
    wp = p_wieferich_base_q(p, q)      # p Wieferich base q
    dw = wq and wp
    irr_p = (h_p % p == 0)
    irr_q = (h_q % q == 0)
    rows.append((p, q, A_qdivhp, A_pdivhq, wq, wp, dw, irr_p, irr_q))

N = len(rows)
print("odd-prime pairs p<q<=%d : %d  (primes: %d)" % (B, N, len(primes)))

def counts(pred):
    return sum(1 for r in rows if pred(r))

# ---- Base rates ----
A   = counts(lambda r: r[2])   # q | h^-(p)
A_m = counts(lambda r: r[3])   # p | h^-(q)
Bq  = counts(lambda r: r[4])   # q Wieferich base p
Bp  = counts(lambda r: r[5])   # p Wieferich base q
DW  = counts(lambda r: r[6])
print("\nBase rates over all pairs:")
print("  q | h^-(p)                  : %d  (%.2f%%)" % (A, 100*A/N))
print("  p | h^-(q)                  : %d  (%.2f%%)" % (A_m, 100*A_m/N))
print("  q Wieferich base p          : %d  (%.2f%%)" % (Bq, 100*Bq/N))
print("  p Wieferich base q          : %d  (%.2f%%)" % (Bp, 100*Bp/N))
print("  double-Wieferich (both)     : %d" % DW)

# ---- Contingency: A (q|h^-(p))  x  Bq (q Wieferich base p) ----
AB_both = counts(lambda r: r[2] and r[4])
A_only  = counts(lambda r: r[2] and not r[4])
B_only  = counts(lambda r: not r[2] and r[4])
neither = counts(lambda r: not r[2] and not r[4])
print("\nContingency  q|h^-(p)  vs  q Wieferich base p :")
print("  A&B (divis & wieferich) : %d" % AB_both)
print("  A only (divis, not wief): %d" % A_only)
print("  B only (wieferich, not : %d" % B_only)
print("  neither                 : %d" % neither)
# co-occurrence rate of A given B, and of B given A
print("  P(A | B) = %d/%d = %.3f   (base P(A)=%.3f)" % (AB_both, Bq, (AB_both/Bq if Bq else 0), A/N))
print("  P(B | A) = %d/%d = %.3f   (base P(B)=%.3f)" % (AB_both, A, (AB_both/A if A else 0), Bq/N))

# ---- Which specific pairs have q | h^-(p) ? print them all with the other flags ----
print("\nAll pairs with q | h^-(p) (p, q, qWiebP, pWiebQ, doubleW, irr_p, irr_q):")
for r in rows:
    if r[2]:
        print("  p=%3d q=%4d  q-wieferich-base-p=%s  p-wieferich-base-q=%s  doubleW=%s  irr_p=%s  irr_q=%s  (h^-(p)=%d, q*%d=%d)"
              % (r[0], r[1], r[4], r[5], r[6], r[7], r[8], HM[r[0]], HM[r[0]]//r[1], HM[r[0]]))

# ---- All pairs with p | h^-(q) (the other cross direction) ----
print("\nAll pairs with p | h^-(q):")
for r in rows:
    if r[3]:
        print("  p=%3d q=%4d  qWiebP=%s pWiebQ=%s doubleW=%s" % (r[0], r[1], r[4], r[5], r[6]))

# ---- double-Wieferich pairs within bound and their cross-divisibility ----
print("\nDouble-Wieferich pairs within bound and q|h^-(p), p|h^-(q):")
for r in rows:
    if r[6]:
        print("  (%d,%d) q|h^-(p)=%s p|h^-(q)=%s irr_p=%s irr_q=%s" % (r[0], r[1], r[2], r[3], r[7], r[8]))
