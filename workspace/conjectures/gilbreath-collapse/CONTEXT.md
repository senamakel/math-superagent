# Shared context

The working brief for every role. Established results with their basis, dead
ends and why, key numbers, recalled memory, disagreements, and gaps. Not a file
catalogue and not a narration. Token budget 10,000; cut from the bottom when
over.

## The problem in one line

**COLLAPSE**: does every second-moment functional of `w(h)` — equivalently of
`S(n,h)² = Σ_{d,d'} (−1)^{XOR over M_d △ M_{d'} of h[i]}` — factor through the
**short-range (pair) correlations** of `h ∈ F₂ⁿ`? It is a finite question about
one explicit `F₂` matrix, `Φ_n`. No primes, none used. Full statement:
`problem.md`; objective and completion criteria: `GOAL.md`.

**Steer-1 reorientation (operative).** The census shows *size is the wrong
statistic*: at n=20 the occurring sets have |A| = 6..12 but diameter 10..18, up
to 8 runs, run_lengths mostly all-1s — small sets spread across nearly the whole
index range, coupling positions at opposite ends of the string. The question
turns on **diameter and run structure, not cardinality**; the O(n) distance
enumerator (problem.md item 4) weights by |A| and controls neither. `problem.md`
is **not authoritative**: three seeded values there were wrong and computation
caught all three — print the stated claim beside any measurement that disagrees
with it.

## Where this run stands (turn 0)

The workspace is **fresh scaffolding**: skeleton directories and the ledger
system exist, but **no ledger has entries, no code, no oracle, no captured
output, no memory, no scratch.** The seven structural results below are
imported from the *parent* investigation as proved, but **this run has not
re-verified any of them locally** — there is no canonical oracle yet, and
GOAL.md forbids trusting anything past the literature bound until one is built
and cross-checked. Treat items 1–7 as **sourced/asserted-by-source, not
locally checked**, until the oracle reproduces them.

## Established (imported as proved by the parent run; asserted-by-source here)

Definitions: `Φ_n[d][j] = C(d, j−(n−1−d)) mod 2` for `d=2..n−1`, `(n−2)×n`, row
`d` the indicator of down-set `M_d = { n−1−d + o : o ⊆ d }`. `T(n,d) = XOR over
i∈M_d of h[i]`, `w = #{d : T=1}`, `S(n,h) = (n−2) − 2w`. `pc` popcount.

1. **Rank/kernel**: `rank Φ_n = n−2` (full row rank), nullity 2,
   `ker = span(even-alt, odd-alt)`, their XOR = all-ones. Parent-verified by
   exact elimination `n=2..40`, kernel census `n=2..12`, exhaustive `2ⁿ`
   enum `n=2..9`.
2. **Exact image law**: `Φ_n` onto, every image has exactly 4 preimages; so for
   uniform `h`, `w ~ Binomial(n−2, ½)`, `E[w]=(n−2)/2`, `Var(w)=(n−2)/4`,
   `E[S²]=n−2`.
3. **Meet-semilattice size** (exact closed form):
   `M_d ∩ M_{d'} = M_{d∧d'}` (bitwise AND) and
   `|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`.
4. **Distance enumerator `O(n)`**: `F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|}` is
   `O(n)` uniformly in `n` for fixed `|z|<1`. The symmetric differences are
   concentrated on small sets — the strongest single piece of evidence *for*
   collapse.
5. **Run structure**: `M_d` (= ↓d) partitions into maximal runs of consecutive
   integers, each of length `2^g`, `g = ν₂(d+1)`, count `2^{pc(d)−g}`, the
   m-th occupying `[m·2^g, (m+1)·2^g − 1]`. Parent-checked `d ≤ 2¹⁴`.
6. **Telescoping identity**: over a run `[u,v]`, when `h` is the difference
   sequence of a **two-valued** sequence `r` (`h[j]=[r_j≠r_{j+1}]`),
   `XOR over o∈[u,v] of h[pos+o] = [ r_{pos+u} ≠ r_{pos+v+1} ]`. Two-valuedness
   is load-bearing: three-valued `r` breaks it with **438 mismatches over
   620,067 pairs** (parent, first at d=1,pos=0). This is the template negative
   control — every new verification must show its own broken variant failing.
7. **Endpoint-sign form**: `(−1)^{T(n,d)} = ∏_R χ(r_{a_R})χ(r_{b_R})` over runs
   `R` of `M_d` with endpoints `a_R,b_R`; **no** `(−1)^{#runs(d)}` prefactor.
   Prefactored form is false (fails 449 of 6868 `(n,d)` pairs, `n=20..120`);
   corrected form holds on all 6868.

Items 5–7 are the collapse mechanism in miniature (run→endpoints, cell→product
over endpoints, differences small). **Whether they compose into a theorem is
the open question** — GOAL.md priority 2.

## The library, digested (this run's scholar pass)

The 13-source reference library is read and distilled into claim blocks
(`research/CLAIMS.md`). What it actually establishes, in order of bearing on
COLLAPSE:

- **Canonical/definitional.** `lucas-submask` (Meštrović): `C(d,i) mod 2 = 1` iff
  `i ⊆ d`, the definition of the fold rows. `odonnell-walsh-character-basis`
  (O'Donnell): `S² = Σ(−1)^{XOR over M_d△M_{d'}}` is a sum of Walsh characters
  `χ_{M_d△M_{d'}}`; collapse = the index multiset is dominated by short-range sets.
- **Crux machinery.** `callan-downset-inverse` + `callan-selfsimilar` (Callan):
  the down-set matrix `S` has inverse `S^{-1}=S(−1)` (Thue–Morse signs, same zero
  pattern), satisfies `S(x)S(y)=S(x+y)`, and its 2^k corner is a k-fold Kronecker
  product of `[[1,0],[1,1]]`. This is the Moebius/carry-free scaffolding behind the
  run structure (item 5) and the O(n) enumerator (item 4). `amarilli-ncpd-setup`
  (Amarilli–Monet–Suciu): the rows form the principal-downset meet-semilattice;
  `amarilli-moebius-multiplicity` (unchecked here): multiplicity in a
  union/complement expression = −µ. This is the vocabulary for the crux multiset.
- **Background, not crux.** `fine-glaisher-2pc` (|M_d|=2^pc), `harborth-density`,
  `shevelev-fermat-factorization` (Fermat factorization, algebra only, no primes),
  `mathonet-not-regular`, `wu-submask-criterion`/`wu-2regular-rlt`,
  `bacher-chapman-sym-pascal` (holds-here **no** — the *symmetric* Pascal matrix
  `C(i+j,i)` is not `Φ_n`).

None of the 13 sources describes **which** distinct `M_d △ M_{d'}` occur with what
multiplicity — the crux (priority 1) is still open (`REQUESTS.md
reference-that-establishes-5a15`).

## Numbers

Imported (parent-run, unverified here): rank data to `n=40`; image-law census
to `n=9`; run structure to `d≤2¹⁴`; endpoint-sign corrected form holds on all
6868 `(n,d)` pairs `n=20..120`, prefactored form fails 449 of them; three-valued
telescoping breaks at 438/620067.

No locally computed terms exist yet. E[S²]=n−2 under uniform model.

Locally computed (checked, two routes — frozenset and bitset,
`code/out/verify_census_bitset.txt` "ALL CHECKS PASSED"): census of *which* sets
`A = M_d △ M_{d'}` occur to n=128. Every nonempty A occurs with multiplicity
exactly 2, the empty set n−2 times, #distinct = 1+C(n−2,2) (claim
`pf-s2multiset-rigid`, verified n≤256). **Diameter/run structure:** max span
carrying weight is n−1 at weight n−2 for every n=3..128; at n=128 the top-span
sets include |A|=126 with runs [125,1] and |A|=64 with 32 singleton runs;
`M_{2^k−1}△M_{2^k−2}` is 2^{k−1} singleton runs. At n=20 the sets have |A|=6..12
but diam 10..18, up to 8 runs, run_lengths mostly [1,1,…]. No witness found at
full pair order for n≤16 (claim `g-witness-order`, K*(n)=ceil((n−1)/2) for n≥6).

## Ruled out

Nothing yet in this run. (Parent run closed eight second-moment routes, all
reducing at coarsest dyadic scale to the same short-range statistic — never
proved. That observation *is* the reason this run exists; it is not recorded as
a refutation.)

**The cardinality reading is refuted (steer-1, computed).** "Small |A| ⇒
short-range structure" is false: small sets occur at diameter up to n−1 with
many singleton runs, so the O(n) size enumerator (item 4) does not establish
short-range structure. Note the converse trap is *not* ruled out: long-span
support alone does not refute collapse — the decision is C_K-fiber constancy,
not support, so "max-runs grows" kills only the framing.

The coil folding is not the problem; no literature source yet describes the
symmetric-difference multiset, so no component of the crux is ruled out by the
library.

## Recalled

Cognee is empty for this run — no durable memory, no prior-run notes, no scratch.
Nothing to import; nothing checked against.

## Contradictions

None recorded yet. The one unresolved tension that defines the problem: item 4
(concentration on small sets) *suggests* collapse, but the conjecture has never
been proved and the parent's eight routes all hit the same wall. Not a
contradiction, a gap.

## Gaps — the forward path

Steer-1 priority order (the joint distribution is the object that decides):

1. **Joint distribution of (|A|, diam A, #runs A)** over all (d,d') at every n
   reached — the replacement for "describe the multiset by size". At n=20 it is
   already decisive-looking: small |A|, large diam, up to 8 singleton runs.
2. **Max-runs(n) and max-diam(n) as functions of n**, and the sharp form: is
   there a uniform bound R with every A a union of ≤ R runs of bounded length?
   Data suggests NO — if max-runs grows, say so plainly and kill the
   short-range-support framing (but remember that is not a collapse refutation).
3. **Witness hunt, now higher priority**: isolated singletons at large
   separation are exactly what separates two strings with identical pair
   correlations. Find an explicit A of that shape and build h,h' around it (SAT:
   ⟨h,I⟩=⟨h',I⟩ for |I|≤K, and A* weight ≡ 1 mod 2, with K below span A*).
   Existence ends the run; absence at n ≤ 20 is strong evidence to keep pushing.
4. **Describe the multiset exactly — which sets occur, with multiplicity.** Sizes
   are closed form (item 3); multiplicity is settled (`pf-s2multiset-rigid`);
   what remains is diameter/run structure, i.e. gaps 1–2.
5. **Compose items 4, 6, 7** into a proof; if they don't compose, name the exact
   failing step. (Item 4 is an analytic O(n) bound on sizes; steer-1 shows it
   weights the wrong quantity, so the composition as originally stated is dead —
   name the replacement precisely.)

Hard requirements in force (GOAL.md): one canonical oracle `Φ_n`/`M_d`/`S(n,h)`
in `code/lib`, cross-checked against brute-force submask enumeration, no second
implementation; every settled conclusion gets a fenced claim block mirroring an
id in `research/ROOT.md`; every verification carries a negative control shown
failing; state the `n` range on every claim; no exponential-time method as the
approach (oracle's the sole exception); `forbid_exponential_time/space` is on in
`config/config.toml`.

## The ledgers, and how to reach them

State lives in ledgers rendered to derived files: `tasks`→`TASKS.md`,
`goals`→`research/BACKWARD.md`, `claims`→`research/CLAIMS.md`,
`threads`→`research/THREADS.md`, `approaches`→`research/APPROACHES.md`,
`frontier`→`research/FRONTIER.md`, `requests`→`research/REQUESTS.md`,
`weakened`, `blueprint`, `entailment`, `board`. The rendered file in your
prompt is a bounded row; the full entry is on disk via `read_ledger`. Claim
blocks live in the source notes (under `research/` and `code/out/`) and reach
`CLAIMS.md` by derivation — a claim written only in the ledger dies on the next
re-write. All are currently empty: there is nothing to read yet and nothing to
re-propose.
