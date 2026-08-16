# Stijn Cambie, "Better Bounds for the Union-Closed Sets Conjecture Using the Entropy Approach" — arXiv:2212.12500 (Dec 2022 / rev 2025, preprint)

The full precise note is at `research/summaries/cambie-better-bounds-entropy-2022.html.md`
with claim `cambie-question2-exact-0-3823455`. Full body:
[[cambie-better-bounds-entropy-2022.html.full]] (also non-html `.full.md` and a
`.pdf.full.md` copy, all the same paper).

## What it establishes (verified in body)

Solves **Sawin's Question 2** exactly: the maximum `c` for which a linear
combination (weight `α`) of an iid and a negatively-correlated Sawin-style
coupling certifies constant `c`.

- **The optimal constant is `c ≈ 0.3823455333667`**, attained at:
  - `α ≈ 0.0356069`;
  - distribution on `{b,1}`, `E[p]=c`, `P(p=1)=a`, `P(p=b)=1−a`;
  - `b ≈ 0.3294547385` (larger root of `H(x)(2−H(x))−H(2x−x²)=0`);
  - `a = (1−H(b))/(2−H(b)) ≈ 0.0788772927`.
  - Tight bounds `0.382345533366702 ≤ t̂_max ≤ 0.382345533366703`.
- **The cap.** One cannot prove a constant better than `0.382345533366703`
  with "the exact suggested approach of Sawin" (the two-coupling linear
  combination).
- Single negatively-correlated term alone cannot beat `ψ=(3−√5)/2` — a linear
  combination is necessary.
- The approximate-UC sharpness construction does not cap the dependent method:
  under Sawin's dependency the union of two sets has size `(0.5+o(1))n`, so the
  union entropy exceeds the independent analysis.

## Hypotheses and holds-here

`ℱ` finite union-closed, `≠{∅}`; densities exact marginals. **Holds-here: yes.**
The value `0.3823455…` rests on numerical verification with stated safe bounds
and a plot; the structural claims (≤3-support reduction, the cap) are proved
in-paper. Preprint (rev 2025) — the *published* record is Yu's `0.38234`
(Entropy 2023), of which this is the exact tight value of the same optimization.

## What it lets the run do

Sets the exact value of the run's live attack object (`Γ̂(t)`): `t̂_max ≈
0.3823455333667` with the precise extremal atomic distribution. The concrete
object any attempt to push the constant higher must optimize (or escape by a
differently-shaped coupling, as Liu's conditional `0.38271` does).

```claim
id: cambie-question2-exact-0-3823455
statement: The maximum c of Sawin's Question 2 (linear combination of an iid and
  a negatively-correlated Sawin-style coupling, weight α) is exactly
  c≈0.3823455333667, attained at α≈0.0356069, P(p=1)=a, P(p=b)=1−a, with
  b≈0.3294547385 (larger root of H(x)(2−H(x))−H(2x−x²)=0),
  a=(1−H(b))/(2−H(b))≈0.0788772927; one cannot exceed 0.382345533366703 with
  this exact approach of Sawin.
hypotheses: ℱ finite union-closed, ≠{∅}; densities exact marginals
holds-here: yes
status: proved structurally in-paper (≤3-support reduction, the cap); final
  numeric value verified computationally with stated bounds and plot
bearing: fixes the exact tight value of Yu's Γ̂ optimization, the run's attack
  object; gives the extremal atomic distribution to test any improvement
anchor: research/sources/cambie-better-bounds-entropy-2022.html.full.md
follows-from: sawin-iid-ceiling, yu-record-0-38234
answers: exact-current-published-c8b8 (Yu 0.38234 published; Cambie t̂_max the
  tight value of the same optimization)
```
