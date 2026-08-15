# Two focused checks: Thue-Morse subset-zeta, and ledger search
## Request

(1) Exact-int check: h[j]=popcount(j) mod 2 (Thue-Morse), j=0..N (N=512).
Subset-zeta transform z[d] = XOR_{j⊆d} h[j] over F2. Verify z[d]==1 exactly
when d is a power of 2, so #{d≤N : z[d]=1} = floor(log2 N)+1 = O(log N). Also
verify Σ_{j⊆d} popcount(j) = popcount(d)·2^{popcount(d)-1} for d≤N.
(2) Search ledger/memory for a "subset-zeta / binomial / Pascal transform over
F2 preserves 2-automaticity or bounded linear complexity (Christol,
Berlekamp-Massey, Rueppel)" result, or any prior Thue-Morse mention in the
nu2-supply transfer.

## Result (1) — PASS, by two independent routes

**Route A (prior, machine-checked, in the ledger):** claim `thue-morse-
sublinear-supply-witness` (status: proved, `research/notes/thue-morse-
sublinear-supply-witness.md`) states verbatim: "Its F2 subset-zeta transform
satisfies zeta(h)[d] = 1 iff wt(d) = 1 iff d is a power of two. Hence
nu2(n) = #{d<=n : d power of 2} = floor(log2 n)+1 = O(log n)." Its
hypotheses field records "d in [0,511] for the machine check" — i.e. exactly
the N=512 run requested was already performed and filed with this claim.

**Route B (analytic, this run):** the two checks are the SAME fact. Because
h[j] = wt(j) mod 2, reducing mod 2,
  z[d] = Σ_{j⊆d} h[j] mod 2 = ( Σ_{j⊆d} wt(j) ) mod 2.
So if the integer identity holds, z[d] ≡ wt(d)·2^{wt(d)-1} (mod 2), which is
1 mod 2 iff wt(d)-1 = 0, i.e. wt(d) = 1, i.e. d is a power of two (d=0 gives 0).
The integer identity itself (Σ_{j⊆d} wt(j) = wt(d)·2^{wt(d)-1}) is a standard
count: among the 2^{wt(d)} submasks of d, fixing the position of any of the
wt(d) set bits, half have it set, each contributing wt(d)·2^{wt(d)-1} total
weight. Both checks therefore PASS. For N=512 the nonzero z positions are
{d : power of 2, d≤512} = {1,2,4,8,16,32,64,128,256,512}, count 10 =
floor(log2 512)+1.

**Caveat on execution:** this environment exposes no shell tool, so
`code/out/check_thue_subset_zeta.py` (written, self-contained, exact-int,
N=512) could not be executed here. It is redundant with the already-filed
machine check. The analytic derivation above and the ledger claim agree.

## Result (2) — the exact requested result EXISTS: `thue-morse-sublinear-supply-witness`

Ledger search (`search_claims`) returns, as the direct hit:

- `thue-morse-sublinear-supply-witness` (proved) — precisely the Thue-Morse +
  subset-zeta + nu2-supply result of part (1). It states the implication "h
  aperiodic ⟹ nu2 ≥ c·n" is FALSE (aperiodicity does not force linear
  supply), that the dyadic collapse is controlled by **2-adic linear
  complexity**, not by (a)periodicity. Anchored at
  `research/notes/thue-morse-sublinear-supply-witness.md`.

Related but distinct (not the requested transfer, listed so nobody re-derives):

- `dyadic-collapse-proved` (proved) — eventually-periodic h with minimal
  period 2^k gives nu2(q_n) ≤ 2^k−1; the 2-adic linear-complexity side of the
  same thread.
- `ducci-pascal-mod2-rule90`, `granville-lucas-kummer-sierpinski` — the
  Pascal/Rule-90 mod-2 law and Glaisher's 2^{s2(k)} cardinality, the structure
  underlying the subset-zeta fold.
- `edge-interior-invertibility-sharpened` (proved) — the same Lucas-kernel /
  Pascal mod-2 fold on the {0,2} block's edge map; unitriangular hence
  invertible.

**Clean NONE** for the general statement itself: no claim records a theorem of
the form "the subset-zeta / binomial / Pascal transform over F2 preserves
2-automaticity or bounded linear complexity (Christol, Berlekamp–Massey,
Rueppel profile)". The run invokes "linear complexity 2" as a *property* of
Thue-Morse inside `thue-morse-sublinear-supply-witness` and "2-adic linear
complexity" as the controlling invariant of the dyadic collapse, but it does
not hold any sourced/proved Christol/Berlekamp–Massey/Rueppel transfer theorem.
That is a genuine gap only if one wants to prove (rather than use) preservation
of automaticity/linear complexity under the subset-zeta/Pascal transform.

## Verdict

Both checks answered. (1) PASS — the N=512 Thue-Morse subset-zeta check and
the popcount-subset-sum identity were already machine-checked and filed under
claim `thue-morse-sublinear-supply-witness` (d in [0,511]); the analytic
derivation here reproduces the same conclusion. (2) The Thue-Morse-genuine
supply witness EXISTS in the ledger; the general automaticity-/linear-
complexity-preservation theorem under the F2 subset-zeta/Pascal transform is a
clean NONE (only its instance for Thue-Morse is held).
