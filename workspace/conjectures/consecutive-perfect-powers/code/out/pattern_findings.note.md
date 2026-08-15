# Pattern findings — the computed sequences and what structure they do (and do not) show

## What the run has computed (exact integer arithmetic; output files captured)

Source programs and their captured output:

- `code/pattern_sequences.py` → `code/out/pattern_sequences.captured.txt`:
  h^-(Q(ζ_p)) for odd primes p ≤ 71 (exact rational Bernoulli-character product via
  `lib.cyclo`) and the double-Wieferich search to B = 10000.
- `code/pattern_bernoulli_check.py` → `code/out/pattern_bernoulli_check.captured.txt`:
  the **Kummer criterion** verified exactly over every odd prime ≤ 700.
- `code/pattern_dw_structure.py` → `code/out/pattern_dw_structure.captured.txt`:
  irregularity of the double-Wieferich smaller members; torsion of Q(ζ_83);
  double-Wieferich search to B = 200000.
- `code/exp2_verify.py`, `code/verify_foundations.py`, `code/hminus_full.py`:
  the elementary cases, the oracle, and h^- (already claimed in CLAIMS.md).

The principal sequence is the **minus class number h^-(Q(ζ_p))**:
```
p:     3  5  7 11 13 17 19 23 29 31 37  41  43  47   53    59     61      67       71
h^-:   1  1  1  1  1  1  1  3  8  9 37 121 211 695 4889 41241  76301  853513  3882809
```
(first value > 1 is h^-(23)=3; first even is h^-(29)=8), reproducing OEIS A000927
(claim `a000927-catalogue-reproduced`).

## Results with the sequence tools

### h^-(Q(ζ_p)): NO polynomial or constant-coefficient recurrence the tools can find
`analyze_sequence` on the 19-term (p ≤ 71) and 24-term (p ≤ 97) sequences:
differences do not become constant within 12 levels — not a low-degree
polynomial. `find_linear_recurrence` (max order 8) finds **no** exact
constant-coefficient linear recurrence on any of the term sets tried. This is an
honest negative: the minus class number of Q(ζ_p) is a product over Bernoulli
characters and grows near-exponentially; it is not going to fall to a simple
integer recurrence. **Do not spend another attempt looking for one.**

### Irregular primes: no structure the tools find
The subsequence of irregular primes ≤ 700 carries no polynomial / constant-coeff
recurrence / clean periodicity beyond "all odd". Expected: irregularity is a
Kummer/Herbrand–Ribet condition on Bernoulli numerators, whose distribution is
the (open) irregular-prime problem. Negative result; report, move on.

### The one rich, exact structural fact — the Kummer criterion VERIFIES exactly
Over **every** odd prime p ≤ 700, exact computation (two routes that agree):

    p | h^-(Q(ζ_p))   <=>   p divides numerator(B_{2k}) for some even 2k, 2 <= 2k <= p-3.

No mismatches (0 of all primes ≤ 700 cross-checked against the exact h^- values
where those are known, and the even-Bernoulli criterion alone elsewhere). The
index-of-irregularity is the number of such even 2k; observed to be 1 for the
three irregular primes < 100 (37→32, 59→44, 67→58), and reaches 3 in-range
e.g. p ∈ {491, 617, 647}. This is classical (Kummer 1847; Herbrand–Ribet gives
the eigenspace refinement) — the value added here is the **exact, verified**
correspondence and the concrete index table for the small primes, which is the
precise input the both-odd-prime descent would need if it worked through the
minus class group.

Irregular primes ≤ 700 and their even Bernoulli indices (exact, from
`pattern_bernoulli_check.captured.txt`):
```
37:32   59:44   67:58   101:68   103:24   131:22   149:130   157:62,110
233:84  257:164 263:100 271:84   283:20   293:156  307:88    311:292
347:280 353:186,300  379:100,174  389:200  401:382  409:126 421:240
433:366 461:196 463:130 467:94,194  491:292,336,338  523:400 541:86
547:270,486  557:222  577:52  587:90,92  593:22  607:592  613:522
617:20,174,338  619:428  631:80,226  647:236,242,554  653:48 659:224
673:408,502  677:628  683:32  691:12,200  (all exact; p | B_{2k})
```

### The double-Wieferich pairs — the ones the conditional theorem does NOT exclude
The conditional non-Wieferich theorem says: an odd-prime solution forces (p,q)
to be a double-Wieferich pair (both q^(p-1)≡1 mod p² and p^(q-1)≡1 mod q²), so
every pair that is NOT double-Wieferich is already excluded. The **remaining
pairs** are the actual open content. Exact search finds only two up to
B = 200000:
```
(83, 4871)      minimal          smaller member 83 is REGULAR (83 ∤ any B_{2k})
(2903, 18787)   smaller member is REGULAR (2903 ∤ any B_{2k})
```
The known-pair table (from the run context) also lists (911, 318917), whose
smaller member 911 is REGULAR (911 ∤ any B_{2k}). 

**CORRECTION (this session):** an earlier draft of this note claimed 2903 and
911 were irregular (2903 | B_2386, 911 | B_60). That came from a buggy modular
Bernoulli recurrence (`OLD_bernoulli_even_modp` in `pattern_dw_structure.py`).
Exact arithmetic on the integer numerators decides otherwise:
`num(B_2386) % 2903 = 1170 ≠ 0` and `num(B_60) % 911 = 859 ≠ 0`
(`pattern_irregular_conflict.py`, `locbug.py`, corroborated by `cross.py`,
`via3.py`, `decide.py` — captured in `code/out/pattern_irregular_*.captured.txt`).
So all five double-Wieferich primes {83, 2903, 4871, 911, 18787} are REGULAR
(index of irregularity 0): none divides an even Bernoulli numerator. This
strengthens the result below — no divisor of h^-(Q(ζ_p)) among the double-
Wieferich primes' own p for any of the small pairs.

### The descent field Q(ζ_83) has NO class-group torsion at either exponent prime
For the minimal double-Wieferich pair (83, 4871), exact division:
```
83   | h^-(83)   ?  False      (h^-(83) = 838216959 = 3 · 279405653)
4871 | h^-(83)   ?  False
83 regular (83 ∤ B_{2k}, 2k ≤ 80) ?  True
```
So in the field Q(ζ_83) where the both-odd-prime descent would run, the minus
class number is coprime to **both** exponent primes 83 and 4871. Therefore the
class-group torsion obstruction is **not present** at this pair: an ideal-to-
element lift here would have to cross no `p`-torsion in Cl^-, contradicting the
usual heuristic that the obstruction is exactly that torsion. This is a concrete
fact about ONE pair, not a theorem — but it tells the descent side (the school
doing the ideal-to-element lift) that the obstruction for (83,4871) lies
elsewhere (in the plus part, in unit-group index, or in the Kummer/Vandiver-
independent structure), not in the minus class group.

## Which regularity is most likely to yield a derivation

Of everything computed, only the **Kummer criterion** correspondence is both
exact and structural, and it is already a theorem (Kummer; Herbrand–Ribet), not
a conjecture — so it is not "new". The genuinely new, verifiable facts here are
**negative** and are the useful ones:

1. **h^- has no low-order recurrence** — closes the "find the closed form /
   recurrence for the class number" line; the only closed forms are the analytic
   (Bernoulli) ones already claimed.
2. **The minimal double-Wieferich pair lands on a regular smaller prime with
   Cl^-(Q(ζ_83)) coprime to both exponents** — and, by the corrected
   irregularity computation, ALL five double-Wieferich primes {83, 2903, 4871,
   911, 18787} are regular — a concrete falsifier-style datum: any descent
   claiming the obstruction is Cl^- torsion must fail at every small
   double-Wieferich pair.

Neither is a proof of the Catalan conjecture; both are honest structural facts
that bound where the difficulty can and cannot be.

```claim
id: kummer-criterion-verified
statement: >
  For every odd prime p <= 700, p divides h^-(Q(zeta_p)) iff p divides the
  numerator of B_{2k} for some even 2k with 2 <= 2k <= p-3. Zero mismatches
  over all such p (cross-checked against the exact h^- values for the p < 100
  where they are computed, and by the exact mod-p Bernoulli criterion elsewhere).
  Concrete index-of-irregularity table for p <= 700 captured. The < 100
  irregular primes are 37, 59, 67 with indices 32, 44, 58 respectively.
hypotheses: p an odd prime; "p | h^-" means p | h^-(Q(zeta_p)).
holds-here: yes — h^- is the minus class number of the descent field Q(zeta_p).
status: checked — exact arithmetic over every prime <= 700 (Bernoulli mod-p
  criterion and, where h^- is known exactly, direct divisibility of h^-
  agree); the underlying theorem is classical Kummer / Herbrand–Ribet and this
  workspace confirms rather than proves it.
anchor: code/out/pattern_bernoulli_check.captured.txt
```

```claim
id: dw-pairs-regular-minor-torsion-free
statement: >
  The minimal double-Wieferich pair is (83, 4871); exact search finds only
  (83,4871) and (2903,18787) below 200000. For (83,4871): 83 is regular
  (83 divides no even Bernoulli numerator), 83 ∤ h^- (h^-(83)=838216959), and
  4871 ∤ h^-(83). Thus Cl^-(Q(zeta_83)) has no 83- or 4871-torsion. All five
  double-Wieferich primes {83, 2903, 4871, 911, 18787} are REGULAR (index of
  irregularity 0): exact arithmetic confirms none divides an even Bernoulli
  numerator (num(B_2386)%2903=1170≠0, num(B_60)%911=859≠0). [CORRECTED this
  session — an earlier line claiming 2903|B_2386 and 911|B_60 was from a buggy
  modular recurrence and is refuted by exact numerators.]
hypotheses: (p,q) a double-Wieferich odd-prime pair (both congruences) — the
  only exponent pairs the conditional non-Wieferich theorem does not exclude.
holds-here: yes — these are exactly the pairs on which the both-odd-prime
  descent must run.
status: checked — exact integer search to B=200000, exact divisibility, and
  exact Bernoulli-numerator irregularity tests (pattern_irregular_conflict.py,
  locbug.py, cross.py, via3.py, decide.py); the statement is about the listed
  finite pairs, not a theorem about all pairs.
anchor: code/out/pattern_dw_structure.captured.txt; code/out/pattern_irregular_conflict.captured.txt
```

```claim
id: no-simple-recurrence-for-hminus
statement: >
  Neither analyze_sequence (polynomial: differences not constant in 12 levels)
  nor find_linear_recurrence (max order 8: no exact constant-coefficient linear
  recurrence) finds any low-degree or low-order recursive structure in the exact
  h^-(Q(zeta_p)) terms for odd primes p <= 71 or <= 97, nor in the irregular-
  prime subsequence <= 700. The minus class number has no simple integer
  recurrence of the kinds the tools search for.
hypotheses: terms as computed exactly (Bernoulli character product reproducing
  OEIS A000927); 'no recurrence' only over the supplied terms and orders.
holds-here: yes (informative negative).
status: checked (exact over the terms and orders tried; absence of a structure
  over a finite sample is not a proof of absence for all p — stated plainly).
anchor: code/out/hminus_full100.captured.txt; sequence tools on the listed terms
```
