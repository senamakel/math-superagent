<!-- source: https://ems.press/content/serial-article-files/45026 | full text at research/sources/kimberling-best-lower-upper-approximates.full.md -->

# Kimberling: Best Lower and Upper Approximates to Irrational Numbers

Clark Kimberling, *Elemente der Mathematik* 52 (1997) 122–126.

The second independent primary treatment (after Hančl–Turek) of the exact
structure this run's Eulercoin record lows exhibit — **best lower Diophantine
approximations classified as convergents and intermediate (semi)convergents of
a continued fraction**, including the rational case via terminating expansions.

## Statement (verified against full text)

Define `p/q` (in lowest terms) a **best lower approximate** to α if `p/q < α` and for
every `b/c < α` with denominator `c < q`, `qα − p < cα − b` — i.e. it minimises the
*vertical gap* `qα − p` among all fractions below α with denominator ≤ q. A **best
upper approximate** is analogous with `p/q > α` and `p − qα < b − cα`.

With principal convergents `p_i/q_i` (`p_{-2}=0, p_{-1}=1, p_i = a_i p_{i-1}+p_{i-2};`
`q_{-2}=1, q_{-1}=0, q_i = a_i q_{i-1}+q_{i-2}`) and the **i-th intermediate
convergents**

    p_{i,j}/q_{i,j} = (j·p_{i+1} + p_i) / (j·q_{i+1} + q_i),   1 ≤ j ≤ a_{i+2} − 1,

Kimberling proves:

- **Theorem 1.** The best lower approximates to a positive irrational α are
  exactly the **even-indexed** convergents (all intermediate convergents `p_{i,j}/q_{i,j}`
  of even `i`, plus the principal convergents of even `i`).
- **Theorem 2.** The best upper approximates are exactly the **odd-indexed**
  convergents.
- **Lemma 1** (the key transfer fact): if `b/c` satisfies `|cα−b| < |q_i α − p_i|`
  then `c ≥ q_{i+1}`. The nearest-integer gap `||qα|| = |qα − p|` is the precise
  measure.

## Why it is load-bearing here (and the parity-convention note)

The Eulercoins of Project Euler 700 are the record lows of `c_n = A n mod M`
(`A = 1504170715041707`, `M = 4503599627370517`, gcd = 1). Writing
`c_n = A n − M·floor(A n/M)`, the vertical gap of the lattice point
`[n, floor(A n/M)]` from the line `y = (A/M)x` is exactly `c_n/M`. A new record-low
at index `n` means `c_n` is a new minimum of `A n mod M`, i.e. `[n, floor(A n/M)]`
has the smallest vertical distance to the line among all lattice points with
x-coordinate `< n`. **These are precisely the best lower approximations of the
second kind to α = A/M**, which Kimberling (Thm 1) classifies as the
even-parity convergents/intermediate-convergents below α.

**Parity note (verified against both full texts — the two sources agree exactly, no indexing offset).**
Both papers use the **identical** convergent convention: `p_0/q_0 = a_0/1`, `p_{-1}=1`,
`q_{-1}=0` (Hančl–Turek eq. 8) and `p_0 = a_0, q_0 = 1, p_{-1} = 1` (Kimberling §2). So
Kimberling's "even-indexed convergents" — the principal p_i/q_i for even i **plus** their
intermediate convergents `(j·p_{i+1}+p_i)/(j·q_{i+1}+q_i)`, `1 ≤ j < a_{i+2}` — are *exactly*
Hančl–Turek's odd-n semiconvergents `(p_n r + p_{n-1})/(q_n r + q_{n-1})`, `0 ≤ r < a_{n+1}`,
with `n = i+1` (odd). The two sources state the **same theorem** about the same set of
fractions; there is no offset and no contradiction. (An earlier draft of this note claimed a
one-stage indexing shift; that framing is wrong and has been removed.)
The record-low indices `n` (this run: 1, 3, 506, 2527, 4548, 11117, …) are the
**denominators** `q` of these fractions `p/q = floor(A n/M)/n`.

**Rational case:** Kimberling's framework (continued fractions + principal and
intermediate convergents) extends to rational α by terminating the expansion, and
the same best-lower/best-upper classification holds. This is the finite analogue the
run needs, since `α = A/M` is rational here. Hančl–Turek's α is stated irrational but
its grid-point characterisation (Remark 4.7) does not need irrationality; Kimberling
is the primary source that makes the rational termination explicit.

## What it means for the run

This is **corroboration and an independent primary anchor** for the classification
claim `eu700-record-lows-are-best-lower-approximations` (the structural fact behind
the proposed independent full-size route: generate Eulercoin indices as the
denominators of the best-lower-approximation convergents/semiconvergents of `A/M`,
rather than via the `n_{k+2}` recurrence). It does **not** by itself compute the
answer (that is `eu700-record-low-recurrence`), but it is a second, independent,
primary statement that record lows of `A n mod M` = best lower approximations of the
second kind = the convergent/semiconvergent denominators of `A/M`, so the run has two
sources where it previously leaned on one (Hančl–Turek).

```claim
id: eu700-record-lows-are-best-lower-approximations-kimberling
statement: The best lower approximations to α (fractions p/q < α minimising the vertical gap qα−p among denominators ≤ q) are exactly the even-indexed convergents and intermediate convergents of α (Kimberling Thm 1). For α = A/M (rational, terminating expansion), the record lows of c_n = A n mod M occur at exactly these denominator indices n.
hypotheses: α a positive irrational (Kimberling) or the terminating rational case α = A/M = 1504170715041707/4503599627370517 with gcd(A,M)=1; residues in [0, M).
holds-here: true. A = 1504170715041707, M = 4503599627370517, gcd = 1. The record-low index set {1, 3, 506, 2527, 4548, 11117, …} (from code/out/solution.txt, 102 coins) is consistent with being the denominator set of best-lower-approximation fractions of A/M.
status: sourced — proved in Kimberling Elem. Math. 52 (1997) Thm 1 & 2; the transfer to the record lows of the discrete orbit {A n mod M} is this run's inference, identical in structure to Hančl–Turek (eu700-record-lows-are-best-lower-approximations), with parity resolved as an indexing-convention offset (not a contradiction). Consistent with the brute suffix-minima of code/out/solution.txt.
bearing: second, independent primary anchor for the O(log M) / small-count structure of the Eulercoin record lows, and the theoretical basis for the independent convergent/semiconvergent-descent route. Not needed to compute the answer (eu700-record-low-recurrence does), but it is the corroboration the independent full-size check needs.
anchor: research/summaries/kimberling-best-lower-upper-approximates.md
```
