# Pattern analysis: sequences in the Catalan descent data

Programs: `code/pattern_sequences.py`, `code/pattern_irregular83.py`,
`code/pattern_irregularity.py`, `code/pattern_dw_extend.py`.
Output: `code/out/pattern_sequences.captured.txt`,
`code/out/pattern_irregular83.captured.txt`,
`code/out/pattern_irregularity.captured.txt`,
`code/out/pattern_dw_extend.captured.txt`.
All arithmetic exact (lib.cyclo over Fractions, sympy.bernoulli, integer pow).

## The sequences that matter

**1. h^-(Q(zeta_p)) — the minus class number.** [1,1,1,1,1,1,1,3,8,9,37,121,211,
695,4889,41241,76301,853513,3882809] over p=3..71 (already exact against OEIS
A000927 over all odd primes p <= 97). `analyze_sequence`: no constant-coefficient
linear recurrence of order <= 8 fits; not eventually polynomial (differences
never constant); leading ratio ~1 (it grows as p^(p/2), near-exponential but not
geometric). This is the quantity the descent on the both-odd content must
control, and there is **no simple recurrence shortcut to it**.

**2. v_p(h^-(Q(zeta_p))) — the index-of-irregularity sequence.** = [0,0,0,0,0,0,
0,0,0,0,1,0,0,0,0,1,0,1,0] over p=3..71 (irregular primes {37,59,67}, each with
index 1). `analyze_sequence`: no polynomial/recurrence structure — it is a
sparse 0/1 indicator of the classical irregular primes. This is the p-part of
the minus class group, the precise obstruction the both-odd descent must kill.

**3. Double-Wieferich odd-prime pairs (p<q), both congruences
p^(q-1)≡1 mod q^2 and q^(p-1)≡1 mod p^2.** Below 3·10^4 there are exactly two:
(83,4871) and (2903,18787). These are the ONLY pairs the conditional theorem
R-double-wieferich does not already exclude, so they are where the descent must
run.

## New structural observation (conjecture, 4 data points)

**The small double-Wieferich primes 83, 2903, 4871, 18787 are all REGULAR** —
none divides its own h^-(Q(zeta_p)):
- h^-(83) = 838216959 = 3 · 279405653 (no 83); Kummer: no Bernoulli numerator
  B_2k, 2<=2k<=80, is divisible by 83.
- Kummer for 2903, 4871, 18787: each has index of irregularity 0 (no k with
  p | numerator(B_2k), 2<=2k<=p-3).
Sanity: the code reproduces the classical irregular primes 37 (B_32), 59 (B_44),
67 (B_58), 101 (B_68) — exactly the known bad Bernoulli indices.

Interpretation (heuristic, not a theorem): the two hypotheses that would close
the both-odd case — *regular* on R-regular (Kummer), and *non-double-Wieferich*
on R-double-wieferich — both happen to hold on the small pairs where either
could bite. If a hypothetical second solution forces DOUBLE-Wieferich (Cassels →
double-Wieferich), the pairs it could sit at are exactly the double-Wieferich
ones; the small ones being regular is precisely the coincidence that would let
R-regular close them too. This is a 4-point observation below 2·10^4 only — 
**not** evidence that all double-Wieferich pairs are regular, and not a proof of
anything. It is the one spot where the ladder's two independent necessary
conditions are observed to point the same way, and the natural falsifier/
extension is a double-Wieferich pair at a genuinely irregular prime.

## Exact vs conjecture — say which

- h^- = A000927 over all odd primes <= 97: **checked** (exact rational arithmetic
  against the catalogue); the *formula itself* is still asserted-by-source
  (classical analytic class number formula), not proved in-workspace.
- v_p(h^-) = irregular indicator over p<=71: **checked** (exact), matches the
  classical irregular prime list.
- Double-Wieferich pairs below 3·10^4: **checked** (exact exhaustive search).
- "Double-Wieferich primes are regular": **conjecture** over 4 primes; the
  Kummer computations behind it are exact but cover only {83,2903,4871,18787}.
- No recurrence/polynomial structure in h^- or v_p(h^-): **checked** over the
  terms given (and consistent with the fast growth of A000927).

## Where this points next

The most likely derivation-friendly regularity is on R-regular (Kummer): a
clean, exact, citable theorem ("if p ∤ h_p and q ∤ h_q then no solution"). The
sequence data independently validates the Kummer criterion machinery (exact
matching of the known irregular primes), which is exactly the tool a proof of
R-regular would run on. The double-Wieferich-regular coincidence is worth
recording so a later run does not accidentally assume "double-Wieferich ⟹
irregular"; the small data says the opposite.
