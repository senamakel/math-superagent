# Shared context

Run state: **very early.** No research notes, no durable memory, no library, no
scratch yet. The only concrete computation that has landed is the witness set in
`code/out/witnesses.json`. Everything below marked `asserted-by-source` comes
from `problem.md` and is not yet verified by this run — verify before leaning on
it. Marked `computed` is read from the witness file and cross-checks against the
problem statement's worked examples by hand arithmetic.

## Established

- **Counting convention (must be fixed before stating any bound).** The witness
  file counts `N(a)` as **both mirrored occurrences plus the trivial pair**
  `C(a,1)=C(a,a-1)`. So `N(3003)=8` means 3 nontrivial entries × 2 mirrors + 2
  trivial. A bound of 8 under this convention is 4 counting only `k<=n/2`
  excluding the trivial pair. **Every claim and every program must name its
  convention.** `computed` from `code/out/witnesses.json`.

- **The witness set (the falsifier every bound must survive).**
  `computed`, exact integer arithmetic over `2<=k<=n/2, n<=20000, value<=10^12`:
  `3003 = C(3003,1) = C(78,2) = C(15,5) = C(14,6)`, so `N(3003)=8`. A claimed
  `B<8`, or any lemma implying one, is **false — record refuted, not weakened.**
  Values in that range with `N=6`: `120,210,1540,7140,11628,24310` (each = one
  nontrivial pair + mirrors + trivial). This is the bound's extent: "no number
  known >8" is only established here up to `n<=20000`; Singmaster has no proof.

- **Elementary facts** (`asserted-by-source` in `problem.md`, not yet checked by
  a program): `N(a)>=2` for all `a>1` via `C(a,1)=C(a,a-1)`; occurrences pair
  under `C(n,k)=C(n,n-k)`; for fixed `a` only `k<=log2(a)` can occur because
  `C(n,k)>=C(2k,k)>=2^k`. Verify these (they are cheap) before any derivation.

## Ruled out

- **Finiteness per fixed `(k1,k2)` is already known and is NOT the conjecture.**
  `C(x,k1)=C(y,k2)` is a curve of growing genus: Faltings (genus>1) and Siegel
  (integral points, any genus) each give finitely many points, but **ineffective**
  — no count computable in `(k1,k2)`. Singmaster needs a bound **uniform over all
  pairs at once and effective**. This is the central obstruction, `sourced` from
  `problem.md`/`GOAL.md`; every proposed approach must say how it beats it.

## Numbers

- `N(3003)=8` (both+trivial convention), `N=6` values listed above, all verified
  for `n<=20000`. Each of the `N=6` witnesses is a single nontrivial pair in a
  small column (`k=2,3`) plus the trivial pair — consistent with the elementary
  `k=2` relation `C(x,2)=C(y,k)` being the main source of multiplicity.

## Recalled

- **None.** `recall_memory` returned nothing for Singmaster, MRSTT, or the genus
  of `C(x,k1)=C(y,k2)`. No earlier run, no durable finding. This run starts from
  scratch; treat any claim about the literature as unverified until a source
  lands.

## Contradictions

- None between sources yet (no sources loaded). One standing tension to keep
  visible: the `k<=log2(a)` elementary bound says high `N(a)` must come from
  small `k`, yet the infinite family with `N(a)>=6` (Fibonacci-indexed, per
  `problem.md`, **unverified**) and `3003` both feature `k=2`/`k=3` columns — so
  small-column curves carry the witnesses and any uniform bound must control them
  uniformly. State and check this before relying on it.

## Gaps

Each is a `request_research`-sized gap, not a mood. Primary urgent ones:

- **Exact MRSTT statement** (Matomäki–Radziwiłł–Shao–Tao–Teräväinen): the exact
  range of `k` their interior-Pascal bound covers, the constant, and precisely
  what it leaves open — the current record, worth being precise about because it
  is the strongest known partial result.
- **The `N(a)>=6` infinite family identity** (proposed Fibonacci-indexed,
  `problem.md` lead): get the exact identity, verify it computationally, record it
  as the reason `B>=6`.
- **Genus of `C(x,k1)=C(y,k2)` as a function of `(k1,k2)`** and where it crosses
  1 — sets the Faltings threshold, and whether it can be made effective/uniform.
- **Baker/linear-forms effective height bound** with a **computed** constant for
  a specific `(k1,k2)` family (names in `problem.md`: de Weger, `C(x,2)=C(y,k)`
  curves) — the realistic partial-result target.
- **An effective bound that is uniform in `k`** — the open core; only the small-`k`
  column families are plausibly attackable.

Compute policy already in place (from `GOAL.md`, follow it): never build the
triangle; invert `C(n,k)=a` by binary search in `n` per small `k`
(`O(log)` per `k`), parallelise over `a`/pairs (28 CPUs), `timeout 540`, state
workers+range in every capture. The oracle is `multiplicity(a,n_max)` and
`genus(k1,k2)`; `code/lib/` is empty so `multiplicity` does not exist yet.
