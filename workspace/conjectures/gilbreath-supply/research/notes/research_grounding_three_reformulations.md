# Literature grounding: three candidate reformulations (research pass)

Scope: the inventor proposed (via the failed subagent message) a set of lines of
attack; the three that were still marked `proposed`/`unchecked` or newly under
study, and this pass took to the literature, are:
`abel-boundary-recurrence`, `substitution-incidence-perron`, `f2-gram-disjointness-spectrum`.
The other candidates in `APPROACHES.md` already carry verdicts from earlier passes.

Verdicts were set in each `research/approaches/*.md` file by editing the `status`/
`precedent`/`killed-by` fields (the parent `research/APPROACHES.md` re-derives from them).

---

## 1. abel-boundary-recurrence — status: **refuted**

**What it is:** Abel summation by parts (Abel's lemma) combined with recurrence
derivation for definite sums, applied to the excess S(n) = Σ_{d=2}^{n−1}(−1)^{T(n,d)}
in the depth index d.

**Named machinery:** real and citable.
- Chen–Hou–Jin, *The Abel–Zeilberger algorithm*, Electron. J. Combin. 18 (2011),
  https://doi.org/10.48550/arxiv.1105.0178 — Abel's lemma on summation by parts
  combined with Zeilberger's creative telescoping produces recurrences for
  definite sums, including non-hypergeometric ones (harmonic numbers, etc.). This
  is precisely the "sum in one index, recur in another" move the approach advertises.
- Koepf, *Algorithms for the indefinite and definite summation*, arXiv:math/9412227 —
  extended Zeilberger/Gosper for rational-linear hypergeometric terms.
- Bostan–Lairez–Salvy, *Multiple binomial sums*, J. Symbolic Comput. (2016),
  https://doi.org/10.1016/j.jsc.2016.04.002 — creative telescoping, diagonal
  generating functions, P-recursive recurrences for definite binomial sums.

**Precise theorem relied on / does it hold here:** The machinery converts a definite
sum Σ_k a_k, with a_k governed by a first-order difference recurrence, into a
boundary evaluation. The load-bearing *literal* input is the neighbour relation
`T(n,d) = T(n−1,d) ⊕ T(n−1,d−1)`. **That relation is FALSE for the actual fold cell.**
Counterexample (hand-verified; claim `abel-boundary-recurrence-relation-false`):
h=(0,0,0,1), n=4, d=2: T(4,2)=h[1]⊕h[3]=1, but T(3,2)⊕T(3,1)=h[0]⊕h[2]⊕h[1]⊕h[2]=0.
Generally T(n,d)⊕T(n−1,d)⊕T(n−1,d−1)=h[n−1]⊕h[0] (the far-end boundary h[n−1] never
cancels because the three cells read different contiguous windows whose starts
shift with n). So the whole Abel-sum body — which is S(n) as a function of the
neighbour relation — has no correct starting relation as stated.

**Applied to this problem?** No. No source applies Abel summation in the depth index
to a submask-XOR fold weight; this was the route's own construction.

**What it would have bought:** a reduction of SUPPLY to a local (O(log n)-supported)
boundary statistic of the prime string, provable by PNT-in-AP or at worst the
adjacent-switch density. That reduction is **not delivered**: the boundary is not
local in the sense claimed, because the relation it needed is false.

**Why refuted:** first-step falsifier fires (the exact neighbour relation is false),
and the false relation was the only thing carrying the "local boundary" claim.
The deeper idea (the d-sum telescopes into a *local* boundary) survives as an
untested speculation, but with no correct relation to telescope in, it has no
machinery to run on. Not a duplicate of `pascal-cascade` (block recursion) or
`newton-series-degree-dichotomy` (degree): distinct move, killed on its own
literal relation.

---

## 2. substitution-incidence-perron — status: **refuted**

**What it is:** read the fold spacetime T(n,d) as a 2-D primitive substitution /
Sierpinski (Rule 90) structure and use the Perron–Frobenius theory of its
incidence matrix to get a fixed point / spectral gap separating prime-like h from
the dyadic-period collapse inputs.

**Named machinery:** real and citable.
- Rule 90 = Sierpiński triangle = Pascal mod 2: Claussen–Nagler–Schuster, *Sierpinski
  signal generates 1/f^α spectra*, Phys. Rev. E 70 (2004),
  https://doi.org/10.1103/physreve.70.032101; Callan, *Sierpinski's triangle and the
  Prouhet-Thue-Morse word*, arXiv:math/0610932.
- Primitive substitutions / incidence matrices / Perron eigenvalue:
  Bédaride–Hilion, *Geometric realizations of two-dimensional substitutive tilings*,
  Quart. J. Math. 2012, https://doi.org/10.1093/qmath/has025; Břinda thesis,
  https://doi.org/10.5281/zenodo.2112128 (fixed points; Perron eigenvalue governs
  letter frequencies; balance).
- Linear CA over F₂ / p-automatic columns: Rowland–Yassawi, Adv. Appl. Math. 2014,
  https://doi.org/10.1016/j.aam.2014.10.002.

**Precise rules relied on / do they hold here:** the four substitution rules
T(2n,2d)=T(n,d), T(2n,2d+1)=0, T(2n+1,2d)=T(n,d), T(2n+1,2d+1)=T(n,d), claimed to
hold because (1+σ)^{2^k}=1+σ^{2^k} (Frobenius). **They are FALSE.** Recorded claim
`substitution-incidence-rules-false`, hand-verified:
- (i) h=(0,0,0,1), n=2, d=1: T(4,2)=h[1]⊕h[3]=1, T(2,1)=h[0]⊕h[1]=0 — rule
  T(2n,2d)=T(n,d) fails.
- (ii) h=(1,0,0), n=1, d=0: T(2,1)=h[0]⊕h[1]=1≠0 — rule T(2n,2d+1)=0 fails.
Structural reason: Φ^{2d}=(1+σ²)^d reads even-offset positions h[x],h[x+2],… of a
_fixed_ h, while Φ^d reads consecutive offsets h[x],h[x+1],… — genuinely different
data. The self-similarity would require h to be dyadic-periodic, i.e. a closed door.
So the fixed-point/Perron bootstrap, which runs on those rules, has no valid rule
set from which to start.

**Applied to this problem?** No. The h-weighted incidence-matrix spectral-gap
transfer is the route's own construction with no published precedent for or against.

**What it would have bought:** a spectral-gap input strictly weaker-looking than
mod-4 switch density (empirical frequency of h at 2–4 positions of a local 2×2
block). Not delivered: the transfer cannot start without correct substitution rules.

**Why refuted:** the exact rules are false, so the intended MPS / incidence-matrix
transfer has no valid generator. The Perron–Frobenius framework is real and the
fixed point it supplies is exactly what the refuted `dyadic-renormalization-selfsimilar`
lacked, but it was mounted on an incorrect literal rule set.

---

## 3. f2-gram-disjointness-spectrum — status: **grounded** (machinery verified; transfer to a weight bound is the open step)

**What it is:** Φ_n is a window of the self-inverse F₂ zeta/Möbius matrix Z (Z²=I),
so the F₂ Gram G_n = Φ_n Φ_n^T is the *disjointness* matrix G_{d,d'}=[d∧d'=0], whose
ℂ spectrum over the full cube is the golden-ratio Kron power (eigenvalues
φ^{m−2k}(−1)^k, max n^{log₂φ}≈n^{0.694}); the proposal is to bound wt(Φ_n h) = ‖Φh‖₁
through a spectral quantity of G.

**Precise facts relied on / do they hold here:**
1. `Z² = I over F₂` — the submask-zeta/Möbius transform is its own inverse in
   characteristic 2. This is classical (Rota; the self-inverse zeta/Möbius transform),
   and reproduces in-workspace claim `supply-fold-submask-zeta-involution`. **Holds.**
2. `Gram = disjointness`: (Z Z^T mod 2)_{d,d'} = 2^{pc(d∧d')} mod 2 = [d∧d'=0],
   matching the proved meet formula `downset-row-intersection-meet-formula`.
   **Holds.**
3. Golden-ratio Kron spectrum on the *full cube*: the disjointness matrix on all
   subsets of an m-set decomposes as ⊗[[1,1],[1,0]] with eigenvalues φ^{m−2k}(−1)^k.
   **Holds (elementary Kron structure).** Meet/join-matrix eigenvalue machinery is
   confirmed by Mattila–Haukkanen, *On the positive definiteness and eigenvalues of
   meet and join matrices*, Discrete Math. 330 (2014),
   https://doi.org/10.1016/j.disc.2014.02.018 — the standard home of the disjointness/
   meet-matrix spectral question.

**Caveat that keeps it `grounded` and not `proved`:** the clean golden spectrum is
literally that of the *full-cube* disjointness matrix. The operative fold Gram is a
*principal submatrix* indexed by d∈[2,n−1] (size n−2, rows 0,1 removed). Whether that
submatrix keeps the spectral gap, and whether ‖Φh‖₁ can be bounded below via any
spectral quantity of it, is the open transfer that no source addresses. The literature
bounds Hamming weights of codes from *incidence matrices of designs/graphs* (Ding,
arXiv:1503.06511; GHW of incidence-matrix codes, Springer 10.1007/s40314-022-01891-6)
but none connects a disjointness/Golden spectrum to the image weight of a submask-XOR
fold against a fixed coefficient string.

**Applied to this problem?** No.

**What it would buy:** a spectral input on h in the submask coordinates, claimed
weaker than switch density. That transfer is unproven; the first-step (compute the
principal-submatrix spectrum of G on the primes vs all-ones/Thue-Morse) is the cheap
decisive test. This approach is NOT among the refuted ones and does not reopen any
closed door.

---

## Negative results worth carrying forward

- No source applies Abel/creative-telescoping summation *in the depth index d* to a
  submask-XOR fold weight, and the specific recurrence the route needed is false.
- No source gives the substitution/Perron transfer for an *h-weighted* (empirically
  block-weighted) incidence matrix of an F₂ linear CA against a non-automatic
  coefficient string, and the literal substitution rules are false.
- No source converts a disjointness/Golden-ratio Kron spectrum into a Hamming-weight
  bound on the image of a submask-zeta linear map. That direction is open.

## Sources

- Abel–Zeilberger: arXiv:1105.0178 (https://doi.org/10.48550/arxiv.1105.0178)
- Koepf summation: arXiv:math/9412227
- Multiple binomial sums: https://doi.org/10.1016/j.jsc.2016.04.002
- Rule 90 / Sierpiński: https://doi.org/10.1103/physreve.70.032101
- Sierpiński/Pascal matrix & PTM: arXiv:math/0610932
- Primitive substitutions / Perron: https://doi.org/10.1093/qmath/has025
- Abelian complexity / substitution fixed points: https://doi.org/10.5281/zenodo.2112128
- p-automatic columns of linear CA: https://doi.org/10.1016/j.aam.2014.10.002
- Meet/join matrix eigenvalues: https://doi.org/10.1016/j.disc.2014.02.018
- Codes from incidence matrices: 10.1007/s40314-022-01891-6; arXiv:1503.06511

## Verification caveat

This pass has no execution tool; the two counterexamples (abel relation, substitution
rules) are hand-verified Boolean arithmetic, matching the refuter's on-disk record
(claims `abel-boundary-recurrence-relation-false`, `substitution-incidence-rules-false`)
and the engine's captured outputs where the engine could decide. Tool_builder should
re-run `code/out/research_verify_relations.py` (written but not executed here) to
machine-confirm both counterexamples over the full small range before any downstream
step relies on the refutations.
