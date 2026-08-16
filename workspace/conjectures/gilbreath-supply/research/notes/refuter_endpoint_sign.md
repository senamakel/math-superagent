# Refuter report: what is still false, what is already closed

Attacked the most-likely-false *checkable* committed statements in the SUPPLY
run. The genuinely open gaps are all arithmetic statements about the real prime
string (essentially the full open problem, not falsifiable at small size). The
pure-Boolean structural pieces — the ones a refuter can actually break — are
surveyed below, with each verdict and where it is banked.

## 1. Spurious sign in the collaborator formula — FALSE, but already documented

**Committed statement** (`G-endpoint-comparison-density`, character-sum form,
still in the live files `research/backward/supply-from-endpoint-parity.md` and
`research/BACKWARD.md`):

    (-1)^{T(n,d)} = (-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})

**Correct identity**: no `(-1)^{#runs}` factor. Each down-set run telescopes
independently: XOR over a run of h equals the endpoint comparison
`[r_{a} != r_{b}]`, and `(-1)^{[...]}=chi(r_a)chi(r_b)` since `[x!=y]=1 <=>
chi(x)chi(y)=-1`; XOR carries signs multiplicatively, so

    (-1)^{T(n,d)} = prod_R chi(r_{a_R}) chi(r_{b_R}).

**Hand proof it is false as written (d=3, the smallest odd d that is a single
run).** d = 3 = binary `11`: g = nu2(4) = 2 trailing ones, popcount = 2, so
#runs = 2^{2-2} = 1, the single run [0,3].  Then
T = h0^h1^h2^h3, and each h[j] = [r_{j+1} != r_j] = r_j xor r_{j+1}, so

    T = (r0^r1)^(r1^r2)^(r2^r3)^(r3^r4) = r0 ^ r4   (interior terms cancel).

So T = mismatch and (-1)^T = chi(r0)chi(r4).  The committed formula says
(-1)^T = (-1)^1 * chi(r0)chi(r4) = -chi(r0)chi(r4) = -(-1)^T, an impossible
equation since (-1)^T = ±1.

**Verdict.** The committed formula is refuted **for every binary string** at
d=3 (and more generally for every odd d, which always contains the single-run
case).  The corrected identity holds; it was verified on all 6868 (n,d) pairs
for n=20..120 against the literal oracle (spurious form fails 449 pairs),
recorded in the refuted approach `dyadic-gap-character-correlation` and posted
on the board ("Two sign/identity corrections").

**Status: already documented — NOT a new finding.** Nothing downstream relies on
the sign factor (it is a rewrite in a prose reduction of an open lemma; the
density #{T=1} is unaffected, and the correction is on disk).  The only stale
part is the prose in the two live skeleton files, which should be updated so no
reader recomputes the wrong product.

## 2. G-run-telescope (run decomposition + telescoping) — TRUE, verified

Every digital down-set partitions into 2^{popcount(d)-nu2(d+1)} runs of length
2^{nu2(d+1)}, each a block [m·2^g, (m+1)·2^g - 1], and XOR over a run
telescopes to an endpoint comparison.  Verified exhaustively on disk
(`code/out/g_run_telescope_verify.captured.txt`): run structure for d = 0..2^14
= 16385 values, telescoping on the real prime string (1.65M pairs) and 30
random controls (49.6M pairs), ALL PASSED; claim `g-run-telescope-verified`
filed.  I re-derived the count by hand (submasks of d = submask of H shifted by
g+1 plus arbitrary low-g bits; popcount(H)=popcount(d)-g) and it matches.  Not
breakable.

## 3. R-random-pointwise — already CLOSED (not open as the ladder says)

`wt(Phi_n h) >= n/4` with probability 1 - exp(-Omega(n)) for uniform h.  With
rank Phi_n = n-2 (proved, nullity 2, surjective onto F2^{n-2}), Mh is uniform
on the whole cube, so wt ~ Binomial(n-2, 1/2) exactly, and Chernoff gives the
concentration (n/4 is a Theta(n) gap below the mean).  Already banked as
`r-random-pointwise-closed-by-exact-binomial` (proved).  The rung's "open"
marker in WEAKENED.md is stale.  Small-n constant failure (P(wt<n/4) ~ 1/4 at
n=4, model h=0 wt=0 at n=5) is the binomial's lower tail, decays, not a
disproof.

## 4. Sparse-strictness rivals — both settled on the board

G-weak-input-strictness (∃ fixed sparse h with linear fold weight) vs
G-eq-sparse-fold-is-sublinear (no such h): the general "sparse => sublinear"
transfer is refuted (h=e_{n-1}, a single 1, gives wt=n-2), while every *fixed*
sparse string has liminf ratio 0 (so no fixed witness).  Documented in
`code/out/sparse_fold_capture.settles.md`.  Not breakable by me.

## What I encoded and why the tool could not help

I wrote several TPTP problems (code/refute/*.p) encoding the committed-formula
sign defect for d=3, both the honest test and the forced-witness versions.
`find_counterexample` returned "undecided" on every one.  These are
finite-propositional problems whose axioms already decide all boolean atoms
(h from r, T from h, T<=>mismatch), so the model-finder has no free boolean
left to satisfy — it neither finds a model nor proves, on this finite boolean
domain.  The n4/n5 problems that DID resolve were different: they left boolean
variables free so a countermodel (specific h) could be exhibited.  The
spurious-sign defect does not need a free model — it is falsified by *every*
assignment at d=3 — so the tool is the wrong instrument; the hand proof is
complete.

## Bottom line

No *new* refutation.  Every small, checkable, pure-Boolean committed statement
this run could be breaking is already closed or already documented:
- spurious sign: false, corrected, documented (stale prose in two files);
- run telescope: true, verified;
- R-random-pointwise: proved via the exact binomial;
- sparse-strictness: both sides settled.

The only live gaps are genuinely arithmetic (second-moment / autocorrelation
bounds on the prime string, switch density, variance vanishing) — exactly the
open problem, not falsifiable at small size.  If the run wants a cleanup: update
the two skeleton files' prose so the spurious `(-1)^{#runs}` is removed, and
merge the closed `R-random-pointwise` rung so it stops being re-attacked.
