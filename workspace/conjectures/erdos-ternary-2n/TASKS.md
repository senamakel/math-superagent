# Tasks

**Directive**: the lifting theorem is now PROVED unconditionally
(`code/out/lifting_theorem.md`, claim `ternary-lifting-theorem`). The three
lemmas — order-3 of the step element, shared low digits, affine bijection of
Z/3 — give `|A_k| = 2^(k-1)` for all k. The sieve set doubles at every level
and never empties, so NO congruence modulo any power of 3 can prove this
conjecture at any finite precision. **Stop sieving**: `sieve_structure.py`
enumerating `A_k` explicitly is data no longer needed, and `|A_k|` is now a
theorem rather than a table.

## 1. Formalise the lifting theorem in Lean 4 (theorem is proved on paper; this makes it machine-checked)

The three lemmas are about orders in `(Z/3^k)^×` and an affine bijection of
`Z/3`. This is well within Mathlib's reach and a machine-checked version is a
real artifact. Report `#print axioms` and every `sorry`.

Thread: `research/threads/lean-formalization.md`.

- [ ] Write the Lean 4 formalisation of Lemma 1 (step element has order 3).
- [ ] Write Lemma 2 (lifts share low digits).
- [ ] Write Lemma 3 (affine bijection of Z/3 on top digit).
- [ ] Assemble the induction giving `|A_k| = 2^(k-1)`.
- [ ] Report `#print axioms` output and every remaining `sorry`.

## 2. Go where the sieve cannot see — DH-1 × Lagarias

DH-1 (Dimitrov & Howe, proved): any exception has a digit 2 **or** at least 26
digits equal to 1. The gap: what structural fact about the 3-adic orbit limits
how many ones can appear without a 2? And can Lagarias's density bound
(`N(X) ≤ 2 X^{log_3 2}`) and DH-1 be **combined** — the DH constraint on the
shape of a counterexample plus the Lagarias constraint on how many
counterexamples can exist?

Thread: `research/threads/dh1-gap.md`.

- [ ] State precisely what DH-1 leaves open (already done; review for
  completeness).
- [ ] What would improve the 26: the DH modulus-selection method — which
  moduli gave the 26, and what would a larger computation cost?
- [ ] Can Lagarias's density bound and DH-1 be combined? If a counterexample
  must have ≥ 26 ones (DH-1) and there are at most `O(X^{log_3 2})`
  candidates below X (LAG-2), does the intersection of these constraints
  force anything stronger than either alone?
- [ ] Connect to SIEVE-EXACT: the 2-to-1 lifting gives every {0,1} pattern is
  realised by some residue class at every finite level; DH-1 constrains which
  patterns can be *consistent* across levels. Make that coupling precise.

## 3. Narkiewicz bound — secondary (statement already extracted)

The bound `N(x) ≤ 1.62 x^(log_3 2)` is already extracted as EP-406 and LAG-1.
The primary Narkiewicz (1980) paper is not yet downloaded but the statement is
not in doubt — downloading it is a verification step, not a gap.

Thread: `research/threads/narkiewicz-bound.md`.

- [ ] Download the Narkiewicz primary source (JSTOR 43667894).
- [ ] Verify the constant and method against EP-406/LAG-1.

## Operational

- **No sieving.** The lifting theorem makes `sieve_structure.py` obsolete.
  Work modulo `3^k`, never materialise `2^n` or `A_k` as a set.
- Launch with `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
- State workers and range in every capture. Keep commands.log current.