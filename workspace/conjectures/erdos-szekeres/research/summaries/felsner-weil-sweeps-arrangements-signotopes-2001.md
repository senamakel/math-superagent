# Felsner & Weil 2001, "Sweeps, arrangements and signotopes" (Discrete Appl. Math. 109, 257–284)

Source: https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf
Full text: [[felsner-weil-sweeps-arrangements-signotopes-2001.full]] (PDF, text-garbled single-line; the statements below come from the complete abstract and the clean restatement in [[bergold-felsner-scheucher-extension-theorem-signotopes]])

The canonical source for the triple-orientation representation of pseudoline arrangements — the combinatorial backbone of this run's entire orientation-variable SAT arm.

## What it establishes

- **Triple orientations (§4).** For an arrangement of n pseudolines one can record an orientation for each triple of lines. **Theorem (main, §4): a triple orientation on [n] corresponds to a (marked) pseudoline arrangement EXACTLY IF it obeys a "generalized transitivity law."** The triple orientations carry a natural order, inducing an order on arrangements, leading to the **signotope orders S_r(n)** whose elements are called **signotopes**, existing for all 1 ≤ r ≤ n and closely related to the **higher Bruhat orders B(n, r−1)** (Manin–Schechtman, Ziegler). [abstract]
- **Sweeping Lemma (Lemma 1).** Every marked Euclidean arrangement of pseudolines can be swept: a sequence of curves from north to south face crossing each pseudoline once, one arrangement vertex between consecutive curves. Used to give a new proof of **Levi's Extension Lemma** and to represent Euclidean pseudoline arrangements by wiring diagrams and zonotopal tilings. [abstract, §2–3]
- **§5.** A signotope σ ∈ S_r(n) represents an arrangement A(σ) of n pseudohyperplanes in R^r; a maximum chain in S_{r−1}(n) represents a sweep of A(σ). [abstract]

## Rank-3 instance (the one this run uses)

Restated in the held Bergold–Felsner–Scheucher summary: an **r-signotope** is a sign map σ:[n]^r → {+,-} with **at most one sign change** in every (r+1)-subset. Then r=2: signotopes ⟺ permutations; **r=3: rank-3 signotopes ⟺ simple pseudoline arrangements with a fixed top/north cell**. A *realizable* point set ⟺ a *stretchable* (straight-line) arrangement. This is exactly the equality the run's encoders ("ordered-signotope axioms", "CC-system / Knuth triples") post.

```claim
id: fw-rank3-signotope-pseudoline
statement: Rank-3 signotopes on [n] (triple-orientation sign maps with at most one sign change per 4-set) are in bijection with simple pseudoline arrangements with a fixed top cell (Felsner & Weil 2001). A triple orientation corresponds to such an arrangement exactly when it satisfies the generalized transitivity law; the rank-3 structure is the CC-system / Knuth order-type data the SAT arm encodes, and a realizable point set corresponds to a stretchable (straight-line) arrangement.
hypotheses: rank-3 signotope, n points in general position / n pseudolines, fixed top cell
holds-here: yes — this is the exact statement the run's orientation-variable SAT encoders mirror
status: proved (stated as the paper's main theorem in the abstract; restated precisely in Bergold–Felsner–Scheucher 2023, held)
bearing: justifies encoding ES via orientation variables + transitivity axioms; separates realizable (stretchable) from abstract — abstract solutions must be realized in exact coordinates before counting
anchor: research/sources/felsner-weil-sweeps-arrangements-signotopes-2001.full.md
```

## Not helpful for the ES bound itself

Sweeping / Levi-lemma / wiring-diagram / higher-Bruhat machinery is what the encoders cite but does not improve the 2^{n−2} upper-bound question; its value here is the exact rank-3 correspondence and the stretchability divide.
