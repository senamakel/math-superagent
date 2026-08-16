```thread
question: Where exactly does the claimed Ghosh proof (arXiv:2501.09272) break in characteristic p, and is the ℂ-only Brouwer-degree / Abel-Gontcharoff step the break point?
status: dead
rests-on: ghosh-2025-claim, ghosh-char0-step, charp-false
blocked-by: none (char-p stress test done; claim ghosh-char0-break-4-18 written)
next: closed (directive 9) — the char-0-only step is located and computationally verified; recorded as checked claim ghosh-char0-break-4-18
```

# Thread: the char-0-only step in the claimed Ghosh proof

## Question
Ghosh (arXiv:2501.09272) claims CA for all degrees over char-0 fields. CA is
false in char p. Therefore the proof MUST have a step that breaks in char p.
What is that step, and can it be located and named? Naming it is part of
stating the proof, and locating it tells us what a genuine proof would need.

## What rests on it
- If the Ghosh proof stands (peer-reviewed/verified), the run's target changes
  to understanding and stress-testing it rather than proving CA.
- If it has a gap, the run continues with CA open; the failing step is the
  obstruction every future attempt must beat.

## What the held source says (ghosh2025_proof_html.full.md, intro §1.1.1)
The proof has two ingredients:
1. **Algebraic**: local and global minimal number of generators of the ideals
   are equal to expected; reduce local to global using
   **Abel-Gontcharoff polynomials and Brouwer degree**. The intro states
   explicitly: "we note that this step works only over ℂ".
2. **Homological**: Koszul homology; a filtration relates truncated Koszul
   complexes in degrees n+1 and n; injectivity on 0th homology + vanishing of
   higher homology (via depth sensitivity + finiteness of [14]) gives the
   downward induction.

## The char-0-only step to test
The Brouwer-degree / Abel-Gontcharoff step "works only over ℂ" — this is a real
analysis/topology input with NO char-p analogue. That is the prime candidate
for the step that must break in char p. A char-p reduction of the same argument
should be impossible at exactly this point. **To do**: verify the downward
induction really relies on the ℂ step (i.e., that the algebraic/Koszul part
alone, applied in char p, would not collapse to the (correct, false-in-char-p)
conclusion). This is the sharpest test GOAL.md demands.

## Status
Open — needs a close reading of the proof's Section 4 and an attempt to run the
Koszul machinery in char p to see where it stops (or would produce a false
positive).

## Collateral finding
CA attracts claimed proofs that fail: **Battiston (arXiv:1511.04932, 2015) was
withdrawn** ("crucial error in its last page", pointed out by Joseph Schicho).
Ghosh (2025) is the current open claim, unverified. This is a pattern worth
recording: the deliverable for this run is a partial result stated exactly, not
a claim of the whole.

## References
- research/sources/ghosh2025_proof_html.full.md (intro §1.1.1, §4)
- research/sources/battiston_casas-alvero-survey_2015.full.md (withdrawn note)

---

## Findings (goals-close-read, this run) — char-0-only step located exactly

Close-read of `ghosh2025_proof_html.full.md`: the downward induction is a
regular-sequence claim (Prop D / §4.1): CA(d) follows once, for every index
choice j_1..j_{d-1}, the sequence S_{d-1}(j_1,..,j_{d-1}) = the
Hasse-Schmidt-derivative images Φ^#_{j_i}(HD^{i-1} x) is a regular sequence in
R_{d-1} = 𝕂[x_1..x_{d-1}]. This is proven by downward induction on d via the
**Koszul homology filtration** (§4.2.1–4.2.2) built on the leading-coefficient
(dehomogenisation in x_n) identification.

The induction's key injectivity lemma is **Proposition 4.3** (lines 503–510):
the maps ι_{k,*} : H_0(K̂^{n}_{k-1,∙}) → H_0(K̂^{n}_{k,∙}) are injective for all
k≥1 — *stated with the explicit hypothesis "when characteristic of the base
field 𝕂 is 0"*. Injectivity of ι_{1,*} is what makes the whole H_0/H_1
long-exact-sequence argument (4.25) collapse to H_1(K^{n-1}_{∙}) = 0, i.e. the
regularity of S_{n-1} in R_{n-1}, completing the step.

**Char-0 is used in exactly two spots inside the proof of Prop 4.3 (lines
513–606):**

(a) **Eq (4.18)** (line ~556): the isomorphism
R_n/(F(1,j_1,n),…,F(n-1,j_{n-1},n),F(n,j_n,n))
≅ R_{n-1}/(Δ_{1n},…,Δ_{n-1,n}) is asserted to hold **"if the characteristic of
the base field does not divide n"**, because F(n,j_n,n) = x_n·f(n,j_n,n) +
g(n,j_n,n) has leading coefficient f(n,n,n) = **−n** (and f(n,j_n,n)=1 for
j_n≠n). This is where the induction needs char ∤ n: at the step d = n with
char p | n, the leading coefficient −n vanishes, (4.18) fails, and the proof
cannot conclude the H_0/K_0 complex is Cohen–Macaulay of the right dimension.

(b) **Corollary 3.9 / Theorem 3.6** (lines 393–396, used at the end of the
proof of Lemma 4.5, line ~601): the minimal-generator bound
μ_{(R_{n-1})_{𝔭}}(I_{n-1}(j_1,..,j_{n-1})_{𝔭}) = n−1 that is needed to rule
out f(l,j_l,n) ∈ 𝔭 is asserted only for **char p ∉ 𝒫(n)**, a finite exceptional
set. Theorem 3.6's bound is the Abel–Gontcharoff/Brouwer-degree result — the
step the author explicitly flags in §1.1.1 as "works only over ℂ".

**Verdict for the char-p stress test:** the Ghosh argument is *not*
characteristic-free and does NOT prove the (false) char-p statement. It
genuinely stops in char p: at the step d = n with p | n, input (a) fails —
−n = 0 in 𝔽_p kills the degree-lowering isomorphism (4.18) and the injectivity
of ι_{1,*} that the induction needs; and even before that, input (b) may place
n in 𝔽_p-terms in the exceptional set 𝒫(n) where the minimal-generator bound is
not available. So the char dependence is a *named divisibility* (char | n and
char ∈ 𝒫(n)), not an after-the-fact search: the char-p witnesses x^{p+1}−x^p
(degree n = p+1) are excluded because the step to d = p needs char | p to
fail, which is exactly the boundary CA is false at. This is consistent: the
proof "works only over ℂ" precisely where it needs char 0, and it gives no
char-p theorem, so it does not contravene the char-p counterexamples the
oracle flags. (Verified-computational part: none; this is a close-read of a
held source, with line numbers. The stated PAC: the claim "Ghosh's step
(4.18) uses −n as a unit, requiring char∤n" is read directly from the text.)

## Follow-up (tool-builder, this run) — the break verified computationally

`code/ghosh_charp/verify_break.py` now verifies the whole §2 object layer and
the break, exactly over QQ and GF(p) (no floating point), all 1313 checks
PASS, capture `code/out/ghosh_break.captured.txt`:

- HD^i_n(x_1…x_n) computed from definition (2.1) equals e_{n-i} for
  n=2..10, i=0..n-1, over QQ and GF(2,3,5,7).
- Φ^#_{d,j} (2.2) is an algebra automorphism (linearity, multiplicativity,
  involution Φ^#∘Φ^# = id, Φ^#_{d,d+1} = identity) for d=2..6.
- **The divisibility (4.18)**: f(n,j,n) = 1 for j ≠ n and = −n for j = n,
  for all n=2..10, j=1..n+1, over QQ and GF(p), p∈{2,3,5,7}; re-derived
  independently via `Poly.coeff_monomial`. Over QQ f(n,n,n)=−n≠0; over
  GF(p) with p|n the unit is 0 — it dies exactly at step d=n.
- Concrete: Φ^#_{n,n}(e_1) = (x_1+…+x_{n−1}) − n·x_n, Φ^#_{n,j}(e_1) =
  e_1 − (n+1)·x_j (j≠n), for n=2,3,5,6,10 over QQ and GF(p).
- The char-p witnesses x^{p+1}−x^p (p=2,3,5,7; degree n=p+1) are
  counterexamples per the canonical oracle (is_ca=True, not a pure power),
  and the downward induction would need step d=p where char | p kills the
  unit f(p,p,p) = −p = 0 — the exact boundary CA is false at.

So the named break is not just read off the text: the divisibility holds over
QQ, dies precisely when char | n, and the escape family sits exactly at the
step where it dies.
