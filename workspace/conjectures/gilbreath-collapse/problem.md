# The collapse question

Let `F₂` be the two-element field. Fix `n` and define the **fold matrix** `Φ_n`,
an `(n−2) × n` matrix over `F₂`, by

```
Φ_n[d][j] = C(d, j − (n−1−d))  mod 2,        d = 2, …, n−1
```

By Lucas' theorem `C(d,i) mod 2 = 1` exactly when `i` is a binary submask of
`d`, so row `d` of `Φ_n` is the indicator of the **down-set**

```
M_d = { n−1−d + o  :  o ⊆ d }          (o ⊆ d means o is a binary submask of d)
```

and for a bit string `h ∈ F₂ⁿ` the depth-`d` fold cell is

```
T(n,d) = XOR over i ∈ M_d of h[i].
```

Write `w(h) = wt(Φ_n h) = #{ d ∈ [2, n−1] : T(n,d) = 1 }` and define the
**signed excess**

```
S(n,h) = Σ_{d=2}^{n−1} (−1)^{T(n,d)}  =  (n−2) − 2·w(h).
```

> **(COLLAPSE)** Does every second-moment functional of `w(h)` factor through
> the short-range correlations of `h`?

Concretely, and this is the form to attack first:

```
S(n,h)²  =  Σ_{d,d'}  (−1)^{ XOR over i ∈ M_d △ M_{d'} of h[i] }
```

so `S²` is a sum of `(n−2)²` Walsh characters of `h`, indexed by the symmetric
differences `M_d △ M_{d'}`. **The question is what that index multiset looks
like.**

- If the multiset `{ M_d △ M_{d'} }` is dominated by sets that are unions of a
  bounded number of adjacent positions, then `S²` — and hence the whole
  second-moment theory of `w` — depends only on the short-range (pair)
  correlations of `h`, and nothing finer about `h` can ever be used.
- If it is not, some functional of `w` sees structure beyond pairs, and the
  route it opens is the point of this problem.

**No number theory is required and none should be used.** `h` is an arbitrary
element of `F₂ⁿ`. There are no primes in this problem.

## What is already established, and may be used freely

Imported as proved. Do not re-derive.

1. **Rank and kernel.** `rank Φ_n = n−2` (full row rank), nullity 2, and
   `ker Φ_n = span(even-alt, odd-alt)`, whose XOR is the all-ones vector.
   Exact `F₂` elimination `n = 2..40`, exhaustive kernel census `n = 2..12`,
   exhaustive `2ⁿ` enumeration `n = 2..9`.
2. **Surjectivity and the exact image law.** `Φ_n` is onto `F₂^{n−2}` and every
   image has exactly `4` preimages. Hence for `h` uniform on the cube,
   `w(h)` is **exactly** `Binomial(n−2, ½)`: `E[w] = (n−2)/2`,
   `Var(w) = (n−2)/4`, so `E[S²] = n−2` in the uniform model.
3. **Meet-semilattice structure of the rows.** `M_d ∩ M_{d'} = M_{d ∧ d'}`
   (bitwise AND), hence the exact size formula
   ```
   |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d ∧ d') + 1}
   ```
   where `pc` is popcount.
4. **The distance enumerator is `O(n)`.** `F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|}`
   is `O(n)` uniformly in `n`, for every fixed `|z| < 1`. So the symmetric
   differences are *concentrated on small sets* — which is precisely why the
   collapse is plausible, and is the strongest single piece of evidence for it.
5. **Down-set run structure.** `M_d` (equivalently `↓d`) partitions into maximal
   runs of consecutive integers, each of length `2^g` with `g = ν₂(d+1)`, and
   there are `2^{pc(d) − g}` of them, the `m`-th occupying `[m·2^g, (m+1)·2^g − 1]`.
   Checked by brute submask enumeration for all `d ≤ 2¹⁴`.
6. **The telescoping identity.** Over any such run `[u,v]`, when `h` is the
   difference sequence of a **two-valued** boundary sequence `r`
   (`h[j] = [r_j ≠ r_{j+1}]`),
   ```
   XOR over o ∈ [u,v] of h[pos+o]  =  [ r_{pos+u} ≠ r_{pos+v+1} ].
   ```
   A block of any length collapses to a comparison of its two endpoints. The
   two-valuedness is load-bearing: replacing `r` by a three-valued sequence
   breaks the identity with **438 mismatches over 620,067 pairs**, first at
   `d=1, pos=0`.
7. **The endpoint-sign form.** `(−1)^{T(n,d)} = ∏_R χ(r_{a_R}) χ(r_{b_R})` over
   the runs `R` of `M_d` with endpoints `a_R, b_R`, with **no** `(−1)^{#runs(d)}`
   prefactor. The prefactored form is false — it fails 449 of 6868 `(n,d)` pairs
   for `n = 20..120`, where the corrected form holds on all 6868.

Items 3–7 are the collapse mechanism in miniature: (6) says a run of any length
reduces to two endpoints, (7) says a fold cell is a product over run endpoints,
and (4) says the pairwise symmetric differences are small. **The question is
whether these compose into a theorem.**

## What counts as a result

In descending order of value.

1. **A collapse theorem.** Every second-moment functional of `w(h)` is a
   function of the short-range correlations of `h` alone. State the exact class
   of functionals and the exact correlation order it factors through — "pairs"
   is the expected answer but the true order is part of the result.
2. **A refutation with a witness.** An explicit functional, and two explicit
   strings `h, h'` with identical short-range correlations up to the stated
   order but different values of that functional. A witness pair beats any
   amount of argument.
3. **A partial collapse.** The theorem for a restricted family of `d` (say
   `pc(d) ≤ k`, or `d` in a dyadic stratum), with the obstruction to the general
   case named.
4. **An exact description of the multiset `{ M_d △ M_{d'} }`** — its
   distribution over set sizes, and which sets actually occur. Item 3 gives the
   sizes; what is missing is *which* sets, and that is likely the crux.
5. **A sixth structural fact about `Φ`** that is not any of the above, proved
   and with its bearing on (1) stated.

## Rules of engagement

- **This is a finite problem.** Every claim is checkable by exhaustive
  enumeration at small `n`. Check before conjecturing, and state the `n` range
  checked.
- **A measurement is not a proof.** Label it.
- **Every verification carries a negative control shown failing.** A predicate
  that cannot fail measures nothing.
- **Stream, never materialise.** An earlier investigation was OOM-killed
  holding a depth-4000 exact triangle. State the memory ceiling of any long
  compute before running it.
- **No primes.** If an argument needs a fact about the primes it is out of
  scope and belongs to the parent problem, not this one.
