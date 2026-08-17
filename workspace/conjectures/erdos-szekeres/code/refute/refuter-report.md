# Refuter report

## What I attacked

I attacked the run's **current open rung**, `R-one-interior`
(`research/weakened/es-conjecture.md`):

> For every n >= 4, every set of 2^(n-2)+1 points in general position with
> at most one interior point (a point strictly inside the convex hull of the
> set) contains n points in convex position.

I did the "look by hand first" step, then encoded the smallest fragment and
ran `find_counterexample`.

## Hand check (one line, covers all n)

A set with at most one interior point has at least 2^(n-2) points *on* its
convex hull. In general position every hull point is a hull vertex, and the
hull vertices of a finite planar set are in convex position. Since
2^(n-2) >= n for every n >= 4 (equality at n=4), the hull alone already
supplies n points in convex position. This regime has **no chirotope/
realizability gap**: hull vertices are extreme in every realization, so the
claim holds for every realizable order type.

So `R-one-interior` is trivially true — the interior points never begin to
matter until k >= 2. It is the k=1 case of the same hull-count argument that
goes through.

## Machine verdict

I re-ran the tightest case, n=4 (5 points), through `find_counterexample`
fresh this session. The tool's verdict discriminates correctly, which itself
is a useful calibration:

| problem | verdict |
|---|---|
| `r-one-interior-n4.p` (n=4, at-most-one-interior, 4-point criterion) | **proved** (SZS Theorem) |
| `r-k-interior-n4-k2.p` (n=4, worst case k=2, triangle hull — hull-count dies) | **proved** (SZS Theorem) — equals ES(4)=5, an established library value |
| `es4-equals-5-fragment.p` (weak fragment, NO interiority/transitivity axioms) | **refuted** — a non-realizable abstract chirotope witness (the known abstract-vs-realizable trap, already documented) |

The two "proved" results are proof *from the axioms I wrote* converging with
the established exact values ES(4)=5; the "refuted" is a known artefact of
the weak fragment, not a counterexample to the real statement. I checked the
realizability point: the weak-fragment model has two points mutually inside
each other's triangles, impossible in the plane — so it is NOT a
counterexample, it is the documented trap.

**Answer: `proved` (hand for all n, machine at the tightest case).**
`R-one-interior` is the trivial k=1 case and should be marked settled; its
"merge" text belongs to `R-k-interior`.

## Where the genuinely falsifiable surface is

`R-k-interior` and `R-one-interior` are not the most-likely-false statements
on the plate: for fixed n, `R-k-interior(n,k)` is logically equivalent to
`ES(n) <= 2^(n-2)+1` (the hypothesis "at most k interior points" is satisfied
by every set if the conjecture holds), so every small case is a settled value
ES(3..6). The genuinely falsifiable statements are the run's **own new,
sampled structural claims about `es_construct` at n=8**, where evidence is
THIN SAMPLING (K=150 realizations per pattern), and sampling can only
under-count realized classes:

- `es-construct-realized-pattern-classes-triangular` — "exactly C(7,2)=21
  distinct realized block-pattern classes at n=8". A convex 7-subset of
  `es_construct(8)` with a block pattern outside the 21 refutes it.
- `es-construct-realized-pattern-bijection` — the closed-form profile
  bijection; same n=8 sampled basis.

These are not encodable in the first-order fragment this tool can search (they
are computable properties of a concrete 64-point set, not propositions over an
abstract order type), so `find_counterexample` cannot reach them. I staged the
heavy-sampling hunt instead.

## Staged attack on the n=8 triangular-count claim (ready to run)

`code/refute/pattern_triangular_n8_attack.py` (overwrote the earlier "unrun"
placeholder with a complete, correct, parallel version). It:

- Phase 0: confirms every one of the 21 formula patterns realises.
- Phase 1: reproduces the 21 realised classes by moderate sampling over ALL
  874 candidate patterns (sum 7, c_i <= |T_i|).
- Phase 2: heavy-hunts (K=30k/pattern, 28 cores) every candidate pattern NOT
  yet realised, looking for a convex 7-subset outside the 21.
- Exact integer arithmetic via `lib.es_geom.in_convex_position` throughout
  (never float); no finite model search, because this is not a first-order
  proposition.

A hit prints `REFUTED` with the witness pattern and refutes
'exactly 21 at n=8'. Capture idiom (no bashisms):
`cd /workspace && { echo "$ python code/refute/pattern_triangular_n8_attack.py"; timeout 550 python code/refute/pattern_triangular_n8_attack.py; echo "EXIT: $?"; } > code/out/pattern_triangular_n8_attack.captured.txt 2>&1`

I could not execute it myself — I do not hold an execution tool — so its
result is not yet in hand. Until it runs, the n=8 side of the two pattern
claims remains `undecided`: no counterexample found, but the search covering
it (any class beyond 21 under the sampled sizes) has not been carried out.
That is precisely the honest status: the sampled n=8 basis is a lower bound,
and the refutation of "exactly 21" is an open, reachable question.

## Boundaries

- `proved` is proof *from the axioms I wrote*, converging with the settled
  library value ES(4)=5; the hand argument is the authority for all n.
- The n=8 pattern attack is staged, not run (no exec tool in my set). Its
  verdict is pending; a future tool_builder/sat/searcher run should execute it
  and record the result (REFUTED with a witness, or the sizes covered).
