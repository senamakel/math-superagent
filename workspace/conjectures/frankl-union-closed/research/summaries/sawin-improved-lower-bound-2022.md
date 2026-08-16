# An improved lower bound for the union-closed sets conjecture

Will Sawin. arXiv:2211.11504 (Nov 2022, v3). Preprint.
Full text (read): `research/sources/sawin-improved-lower-bound-2022.html.full.md`

<!-- source: https://arxiv.org/html/2211.11504v3 ; also https://arxiv.org/pdf/2211.11504 -->

## What it establishes (primary source, read)

Independent (Nov 2022) achievement of the `(3−√5)/2 ≈ 0.382` iid-entropy
bound (Theorem 1), following Gilmer and replacing one key estimate by a sharp
one (Lemma 3). Theorem 2 is the sharp entropic statement, shown tight at
`u = (3−√5)/2` from both sides by the two Gilmer-type examples (the
independent-`u` example and the `[n]`-mixture example).

**The two things this paper adds beyond the iid barrier:**
1. It suggests a new addition to Gilmer's method — using **non-independent /
   dependent couplings** — and sketches a proof that this obtains a constant
   **strictly greater than** `(3−√5)/2`.
2. It **disproves a conjecture of Gilmer** that would have implied the full
   union-closed set conjecture. (This is the key content of Proposition 6 and
   the surrounding examples: the natural strengthening is false.)

## Why it matters for this run

This is the origin of the **dependent-coupling escape** from the
`(3−√5)/2` iid barrier: Yu (0.38234) and Liu (0.38271) make Sawin's sketch
computable/explicit. It also **refutes a claimed route to a full proof**
(Gilmer's conjecture), so any attack that would rely on that conjecture is a
dead end — worth recording under Ruled out.

```claim
id: sawin-iid-bound
answers: sawin-above-barrier
statement: Every nonempty union-closed family has an element in at least
  (3−√5)/2 ≈ 0.38207 of its sets; the bound is sharp for the iid entropy
  inequality (Theorem 2 + the two tightness examples).
hypotheses: F union-closed finite.
holds-here: true
status: proved
bearing: the iid-entropy barrier; dependent couplings (this paper §2) escape it.
anchor: Sawin arXiv:2211.11504, Theorems 1-2 & Lemma 3; full text in sources.
```

```claim
id: sawin-disproves-gilmer-conj
statement: Sawin disproves a conjecture of Gilmer that would have implied the
  union-closed set conjecture; hence that particular route to a full proof is
  closed.
hypotheses: none.
holds-here: true
status: proved
bearing: dead-end: an attack relying on Gilmer's (now disproved) strengthening
  cannot work.
anchor: Sawin arXiv:2211.11504, Proposition 6 + examples; full text in sources.
```

```claim
id: sawin-dependent-coupling
statement: Sawin shows a dependent (non-independent) coupling yields a constant
  strictly greater than (3−√5)/2; Yu makes this explicit at ≈0.38234.
hypotheses: F union-closed.
holds-here: true
status: asserted (sketch in Sawin; explicit in Yu)
bearing: the mechanism by which the entropy method escapes the iid barrier.
anchor: Sawin arXiv:2211.11504 §2; Yu arXiv:2212.00658; full texts in sources.
```
