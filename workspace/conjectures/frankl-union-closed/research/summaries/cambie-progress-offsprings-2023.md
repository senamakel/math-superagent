# Cambie, "Progress on the union-closed conjecture and offsprings in winter 2022-2023" — arXiv:2306.12351

Full body: [[cambie-progress-offsprings-2023.full]]

A survey by Stijn Cambie written during the entropy breakthrough winter
2022–2023. Verifies and places the entropy line, and records several results
not yet in ROOT.md.

## What it establishes (verified in body)

- **The ψ = (3−√5)/2 iid bound** is confirmed as the work of four papers
  (AHS, Chase–Lovett, Sawin, Pebody), all reducing UC-with-constant-ψ to the
  one-variable inequality `h(x²) ≥ φ·x·h(x)`, φ=(√5+1)/2 (Lemma 5). Boppana's
  proof originates in 1989 (Rolle multiplicity argument). This matches the
  library's `boppana-entropy-inequality`.
- **Sharpness construction (Chase–Lovett) restated**: `ℱ₁+ℱ₂` with
  `ℱ₁ = C([n], ψn+n^{2/3})`, `ℱ₂ = C([n], ≥(1−ψ)n)` is 1−o(1) approximate
  union-closed with every element in ≤ψ+o(1) fraction of sets. The n^{2/3}
  can be any g(n) with n ≫ g(n) ≫ n^{1/2}. **This confirms Cambie's own paper's
  claim that the dependent method escapes the ψ cap because the union of two
  random sets has size (1−ψ)n+Θ(n^{2/3}) > (1−ψ)²n, so union entropy exceeds
  the independent analysis.**
- **Sawin → Yu → Cambie.** Yu makes Sawin's suggestion computable (bounding
  the support of the joint distribution by 4 via AHS Lem 5 + Krein-Milman),
  yielding ≈0.38234. Cambie gives an upper bound showing the improvement is
  "way smaller than expected": extremal distribution on two values, one =1,
  support reduced to 3 (one value =1). Confirms `cambie-question2-exact`.
- **Yuster's k-union-closed** generalisation: ψ_k = unique real root of
  (1−x)^k = x in [0,1]; UC-analogue conjectured tight, proved for k≤4.
  Confirms `yuster-psi-k-approx-optimal`. ψ₂ = (3−√5)/2.
- **Scandone's claimed full proof is flawed** (found by Tao): his single global
  bit Z_δ loses its indeterminacy after the first chain-rule step; "a single
  global bit is not sufficient, a more involved construction is needed." This is
  a recorded dead end / caution: the specific πδ-modification of the union
  operation does NOT prove UC. Do not re-attempt this exact construction.
- **Conjecture 7 (Cui–Hu):** if the smallest set of a finite union-closed
  family has size ≥2, then at least two elements each belong to more than half
  the sets. This would imply UC. **Refuted in the ≥k-size variant**: the
  P_k^n construction (family of sets of size ≥k over an even-n universe with
  1,2 pervasive and even/odd subfamilies) has exactly **2 abundant elements**,
  all others non-abundant for n large (n≥10k). For k=4,n=12, |P_4^12|=1045,
  each element 2≤i≤11 appears 522 times (< 522.5). This is a **known sharp
  limit on the "many abundant elements" line**: you cannot guarantee more than
  one abundant element even with all sets large.
- **Poonen's block reduction**: to prove UC it suffices to consider families
  where no block is a singleton (blocks = maximal sets of elements in exactly
  the same sets). The P_k^n construction extends to such families.
- **Ellis–Ivan–Leader** smallest-set construction reconfirmed (log k/(2k)),
  and Pulaj–Wood verified their remaining open case. Confirms small-set fault
  line.
- **Chase's communicated direction**: maybe UC is a distraction from the more
  general `|F∪F| > |F|^c` for some c(ε)>1 when every element is in < 1/2−ε
  fraction. A candidate new structural inequality to investigate.

## Hypotheses and holds-here

- Survey; the sourced results carry their papers' hypotheses (finite
  union-closed). **Holds-here: yes** for the statements taken.
- The **two-abundant-elements refutation** (P_k^n) is proved by construction in
  the cited [11]; present here as an exposition with the counting argument.

## What this lets the run do

- **Ruled out**: Scandone's global-bit construction (flawed, Tao's objection);
  and the "≥2 abundant when all sets large" line is capped at exactly 2,
  so a "many abundant elements" proof of UC cannot rely on more than one
  abundant element.
- **Load-bearing**: Poonen's reduction to no-singleton-blocks families is a
  genuine structural simplification available to any minimal-counterexample
  attack.
- Confirms the record and the record's caveat (Sawin's combination gives only a
  tiny improvement — the Cambie cap ≈0.3823455), so the run's `cambie-question2`
  exact value is right and there is no big slack in the Sawin two-coupling
  constant.

```claim
id: cambie-survey-two-abundant-capped
statement: Families whose smallest set has size ≥k (k arbitrary large) can have
  exactly 2 abundant elements (construction P_k^n), so UC cannot be proved by
  showing several elements are abundant; and Conjecture 7 (Cui–Hu: smallest
  set size ≥2 ⟹ ≥2 elements in >half the sets, which would imply UC) is
  refuted in its ≥k-size variant.
hypotheses: F finite union-closed, all sets size ≥k, n≥10k even
holds-here: yes
status: sourced (Cambie survey; construction in cited [11], counting shown)
bearing: caps the 'many abundant elements' route at exactly 2; UC must come
  from some other structural fact
anchor: research/sources/cambie-progress-offsprings-2023.full.md §6
```

```claim
id: scandone-global-bit-flawed
statement: Scandone's claimed full proof of UC (modifying the union operation
  by padding with a single global Bernoulli bit Z_δ) is flawed: the bit's
  indeterminacy is lost after the first chain-rule step; a single global bit
  is insufficient. The construction does not prove UC.
hypotheses: none (the construction)
holds-here: yes
status: asserted (Cambie's account, attributed to Tao's communication)
bearing: a recorded dead end — do not re-attempt this exact padding
  construction
anchor: research/sources/cambie-progress-offsprings-2023.full.md §5
```

```claim
id: poonen-no-singleton-block-reduction
statement: To prove UC it suffices to consider families in which no block is a
  singleton, where a block is a maximal set of elements belonging to exactly
  the same sets of the family (Poonen).
hypotheses: F finite union-closed
holds-here: yes
status: sourced (via Cambie survey, attributed to Poonen)
bearing: a genuine structural simplification for minimal-counterexample attacks
anchor: research/sources/cambie-progress-offsprings-2023.full.md §6
```
