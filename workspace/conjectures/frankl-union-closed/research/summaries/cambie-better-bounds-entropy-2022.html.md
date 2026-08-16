# Stijn Cambie, "Better Bounds for the Union-Closed Sets Conjecture Using the Entropy Approach" — arXiv:2212.12500 (Dec 2022 / rev 2025)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2212.12500 (also arxiv.org/pdf/2212.12500).
> Full text: `research/sources/cambie-better-bounds-entropy-2022.html.full.md`.

The paper that **solves the Sawin-style Question 2 exactly**, pinning the
tight extremes of the dependent-coupling record and proving the cap on that
specific approach.

## Setting (Question 2, Sawin's dependent-coupling form)

"Maximum `c` for which there exists `α∈[0,1]` such that: for every `p,q,r`
identically distributed `[0,1]`-valued random variables with expectation `< c`,
`p,q` independent but `p,r` not necessarily independent, we have a certain
linear-combination entropy inequality (`α` weights the independent pair, `1−α`
weights the negatively-correlated pair)."

The idea: sample `A,B ∈ ℱ` element-wise once, in a Sawin-style dependent manner
so each is uniform; the worst case over conditional distributions for the two
sampling strategies differs, so a linear combination of the two gives a better
bound than either alone.

## What it establishes

- **The optimal constant for Question 2 is `c ≈ 0.3823455333667`.** Specifically
  at the optimum:
  - `α ≈ 0.0356069`;
  - distribution supported on `{b,1}` with `E[p] = c`, `P(p=1)=a`, `P(p=b)=1−a`;
  - `b = b₂ ≈ 0.329454738503037` (the larger root of
    `H(x)(2−H(x)) − H(2x−x²) = 0`);
  - `a = (1−H(b))/(2−H(b)) ≈ 0.0788772927059232`;
  - `E[p] = 0.382345533366703…`.
  - Equality: `E[H(p+q−pq)] = E[H(max(p,r,min(p+r,1/2)))] = E[H(p)]`, with
    `(1−a)²H(2b−b²) = (1−2a) = (1−a)H(b)`.
- **The cap.** *"One cannot aim to prove the result with a constant better than
  `0.382345533366703` with the exact suggested approach of Sawin."* I.e. the
  linear-combination-of-two-couplings form is exactly solved at
  `≈0.3823455333667`.
- **Why the single negatively-correlated term alone cannot improve `ψ`:** for
  `P(p=1)=a`, `P(p=b)=1−a` with `b=1/4`, `a=(1−H(b))/(2−H(b))+ε`, we get
  `E[H(max(p,r,min(p+r,1/2)))] < E[H(p)]`; and `E[p] < 0.37 < ψ`, so the single
  term never beats `ψ` on its own — a *linear combination* is necessary.
- **Why the approximate-UC sharpness construction does not cap the dependent
  method:** for the layer family `ℱ = {A:|A|=ψn+g(n)} ∪ {A: |A|≥(1−ψ)n}` with
  `g(n)=ω(n^0.5), o(n)`, under Sawin's dependency the union of two sets almost
  surely has size `(0.5+o(1))n`, so the union entropy exceeds what the
  independent analysis gives.

## Proof structure (technical core)

- Reduces the support of the possible probability distributions; proves the
  critical distributions have support of at most 3 values (Section 3.1, 3.2).
- With Yu's work (the re-fetched Yu body is in this library), this reduces to
  two cases depending on two variables each.
- The final minimization is verified numerically in two ways, with a plot
  establishing the global minimum at the proposed atomic distribution.
- Sharpness computation available at
  github.com/StijnCambie/UCconjecture/Sharpness.sagews.

## Hypotheses and holds-here

- `ℱ` finite union-closed, `≠{∅}`; element densities exact marginals. **Holds-
  here: yes.**
- The value `0.3823455333667` rests on numerical verification (safe bounds;
  the plot and two-way check). The *structural* claims (≤3-support reduction,
  the cap being a cap of the two-coupling form) are proved in-paper.
- Cambie remains a **preprint** (rev 2025); the *published* record is Yu's
  `0.38234` (Entropy 2023), of which `0.3823455333667` is the exact tight value
  of the same optimization.

## What it lets the run do

- **The exact value of the run's live attack object** (`Γ̂(t)`) is now on disk:
  `t̂_max ≈ 0.3823455333667`, the maximum `c` of Question 2. The Yu body gives
  the safer `0.38234`; Cambie gives `10⁻¹⁵`-precision bounds
  `0.382345533366702 ≤ t̂_max ≤ 0.382345533366703` and the exact extremal
  distribution `P(p=1)=a, P(p=b)=1−a` with `a≈0.078877, b≈0.329455`.
- This is the concrete object any attempt to push the constant higher must
  optimize (or escape by a differently-shaped coupling, as Liu's 0.38271 does).

```claim
id: cambie-question2-exact-0-3823455
statement: The maximum c of Sawin's Question 2 (linear combination of an iid
  and a negatively-correlated coupling, weighted by α) is exactly
  c≈0.3823455333667, attained at α≈0.0356069 and distribution P(p=1)=a,
  P(p=b)=1−a with b≈0.3294547385 (larger root of H(x)(2−H(x))−H(2x−x²)=0),
  a=(1−H(b))/(2−H(b))≈0.0788772927; one cannot exceed 0.382345533366703 with
  this exact approach of Sawin.
hypotheses: ℱ finite union-closed, ≠{∅}; densities exact marginals
holds-here: yes
status: proved structurally in-paper (≤3-support reduction, the cap); the
  final numeric value verified computationally with stated bounds and plot
bearing: fixes the exact tight value of Yu's Γ̂ optimization, the run's attack
  object; gives the extremal atomic distribution to test any improvement
anchor: research/sources/cambie-better-bounds-entropy-2022.html.full.md
follows-from: sawin-iid-ceiling, yu-record-0-38234
answers: exact-current-published-c8b8 (refines the published-record resolution:
  Yu's 0.38234 in print, Cambie's t̂_max=0.3823455333667 the tight value)
```
