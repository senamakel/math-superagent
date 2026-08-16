# The char-p collapse step: coefficient descent (Graf von Bothmer et al 2007)

Closing a load-bearing gap in the open thread `root-difference-coloring`. The
thread's last remaining question is *where the char-0 collapse step breaks in
characteristic p* — the GOAL.md admissibility test every argument must name.
Reading the newly-landed full text of Graf von Bothmer, Labs, Schicho, van de
Woestijne 2007 (`research/sources/grafvonbothmer2007_infinitely_many_html.full.md`)
resolves the "no F_p analogue" half of the thread's answer into its exact
mechanism — and shows a finer picture than the thread previously recorded.

## The claim: collapse DOES happen in positive characteristic — by coefficient descent

The thread's `root-difference-identity-verified.md` stated the char-p break as:
"(a) per-colour vacuity, (b) the Polstra/Gauss-Lucas convex-hull propagation
... has no F_p analogue." That is correct but incomplete: the convex-hull
propagation is not the *only* collapse mechanism, and the F_p one is not absent
— it is coefficient descent, proved in Section 2.

**Proposition 2.5** (Graf von Bothmer et al, d = p^k). If `d = p^k`, then
`X_d(Fbar_p)` is empty: there is NO CA-polynomial of degree p^k over Fbar_p
except x^d.

*Mechanism.* By their Lemma 2.4 (a Kummer/carrying fact): since p | d and
`v_p(i) < v_p(d)` for `1 ≤ i ≤ d−1`, we get `(d choose i) ≡ 0 (mod p)` for all
`i = 1,…,d−1`. In particular `(d choose d−1) = d ≡ 0`, so the highest Hasse
derivative `P_{d−1} = a_1` is a *constant*. Sharing a factor with `P = x^d +
… + a_1 x` then forces `a_1 = 0`. Iterate: `P_{d−2} = a_2` forces `a_2 = 0`,…
so `a_1 = … = a_{d−1} = 0`, i.e. `P = x^d`, the trivial point excluded as
projective. (Lines 129-145 of the held source.)

**Proposition 2.6** (legal lift). If `d = n·p^k` and `X_n(Fbar_p)` is empty,
then `X_d(Fbar_p)` is empty. The descent forces `a_i = 0` unless `p^k | i`,
leaving `P = x^d + a_{p^k} x^{d−p^k} + … + a_{d−p^k} x^{p^k} = Q^{p^k}` for a
degree-n `Q` over the perfect field Fbar_p, and `Q` is itself CA — a smaller
CA polynomial. (Lines 145-157.)

**Theorem** (Section 2 conclusion): `X_{p^k}(Fbar_p)` and `X_{2p^k}(Fbar_p)`
are empty, so CA holds in degree `p^k` and `2p^k` over char 0. This is the
paper's headline result.

## The break for the witness degree: the descent never starts at d = p+1

The canonical witness `x^{p+1} − x^p` (paper's own Prop 3.1) lives in degree
`d = p+1`. The reason it survives is now *exact*: at `d = p+1` the
coefficient-descent pivot does not vanish —

    (d choose d−1) = (p+1 choose p) = p+1 ≡ 1 (mod p) ≠ 0.

So `P_{d−1} = (p+1)X + a_1` (not a constant), the first step of the descent
cannot force `a_1 = 0`, and `x^{p+1} − x^p` (roots 0 multiplicitly p, and 1)
is a genuine CA counterexample that is not a pure power. Degree `p+1` is not
of the form `p^k` or `2p^k` for `p > 2`, and for `p = 2`, `3 = 2+1` triggers
the `2p^k` clause colliding at the quadratic subcase — the paper's own
handle on the `2p^k` side. So the *reason* the char-p hypothesis is separable
into "collapse exactly where `(d choose d−1) ≡ 0`" is the fade of that pivot.

## What this settles for the thread's admissibility test

The run's GOAL.md requires every argument to name the step that breaks in char
p. The `root-difference-coloring` collapse step now has a *named, sourced*
char-p boundary, and it is sharper than "the convex-hull step":

- The F_p collapse mechanism is NOT absent — it is **coefficient descent** on
  the Hasse derivatives (Props 2.5-2.6), and it works whenever `(d choose i) ≡
  0 mod p` for the full range, i.e. `d = p^k` (and `2p^k`).
- The break is the **first pivot** `(d choose d−1) = d`. Where `d ≢ 0 mod p`
  (e.g. `d = p+1`), the descent's first step fails immediately and witnesses
  exist.
- The convex-hull/Gauss-Lucas propagation remains the *char-0-only* ingredient
  needed to collapse the degrees between the p^k grid — but the causality the
  thread recorded ("F_p analogue absent") is upgraded: F_p does have a collapse,
  it just stops at the degrees where `p ∤ d`.

This also gives the run a precise, testable correspondence between degrees
`d ≡ 0 mod p` (descent starts, CA tends to hold/be pure-power) and `d ≢ 0 mod p`
(witnesses can exist), worth checking against the bad-prime lists at the small
degrees in `badprimes-criterion-n5.md`.

## Evidence class

Prop 2.5, Prop 2.6, Lemma 2.4 and the Theorem are **proved in the source**
(lines 129-157; mechanism verified by my reading of the proof and the one-line
`(p+1 choose p) ≡ 1 mod p` computation, which is exact integer arithmetic).
The claim is `proved` for the sourced theorems; my own reading confirms the
witness-degree pivot fails to vanish but does not independently re-verify the
full `p^k` emptiness (that is the paper's proof). An executor is welcome to
confirm `binomial(d,i) ≡ 0 mod p` for all `1≤i≤d−1` at `d = p^k` via
`code/scholar/descent_check.py` (written, not yet run).

```claim
id: gvb-coefficient-descent-charp
statement: For degree d = p^k (and 2p^k), there is NO CA-polynomial over Fbar_p
  except the pure power x^d: the Hasse derivatives collapse the coefficients by
  descent (P_{d-1}=a_1 forces a_1=0, then P_{d-2}=a_2, ...) because
  (d choose i) ≡ 0 mod p for all 1 <= i <= d-1 (Lemma 2.4/Kummer). The descent
  pivot (d choose d-1) = d is what fails to vanish for the witness degree
  d = p+1: (p+1 choose p) = p+1 ≢ 0 mod p, so x^{p+1} - x^p survives as a CA
  counterexample that is not a pure power.
hypotheses: d = p^k or 2p^k; Hasse derivatives; char p; Kummer's theorem on
  binomial coefficients; Fbar_p perfect for the Q^{p^k} factorization
holds-here: yes — this is the exact char-p collapse/boundary mechanism the
  root-difference-coloring thread needs to name its break
status: proved (Props 2.5, 2.6, Theorem, Lemma 2.4 in Graf von Bothmer et al
  2007, J. Algebra 316:224-230, arXiv:math/0605090v2, lines 129-157; witness
  pivot (p+1 choose p) ≡ 1 mod p confirmed by exact integer arithmetic)
bearing: names the exact char-p collapse step (coefficient descent) and the
  exact break point (the pivot d ≡ 0 mod p) for the CA admissibility test; the
  char-0-only ingredient is confined to the convex-hull/Gauss-Lucas step
  between the p^k grid.
anchor: research/notes/gvb-coefficient-descent.md
falsifies: a degree p^k (or 2p^k) CA counterexample over Fbar_p other than x^d,
  or a witness in degree d=p+1 whose descent pivot (d choose d-1) is 0 mod p
```

## Notes and refs

- Full text: `research/sources/grafvonbothmer2007_infinitely_many_html.full.md`,
  source URL https://arxiv.org/html/math/0605090v2; journal J. Algebra 316
  (2007) 224-230, https://doi.org/10.1016/j.jalgebra.2007.06.017.
- Related claim already on disk: `gvb-lift`, `gvb-lift-and-bad-primes`
  (the lift statement), `charp-witness-xpp1-xp`, `root-difference-identity`.
- The thread `root-difference-coloring` previously said collapse "has no F_p
  analogue" — this note corrects that to "F_p collapse = coefficient descent,
  which stops where its first pivot d ≢ 0 mod p, i.e. the witness degree p+1."
