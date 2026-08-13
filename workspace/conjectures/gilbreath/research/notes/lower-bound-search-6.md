# Search for a solved route to the (2,4)-event rate lower bound — attempt 5

Question asked: how has this problem, or the structure it reduces to, actually
been solved; return concrete methods with sources; say which run approaches it
supersedes.

## What the run already has (do not re-derive)

- Reduction: GC ⟺ A_k(1) ∈ {0,2} for all k. **Proved** (`research/notes/reduction.md`).
- Block lemma: constant = 1 (n+1 rows per length-n block). **Proved** (`research/notes/block_lemma.md`).
- Step law + recharge identity: `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1}=b_k−1`;
  `b_k = 2 + Σ_{i<k}(j_i+1) − (k−1)`. **Proved**, universal (primes AND random arrays).
  GC ⟺ `Σ_{events i<k}(j_i+1) ≥ k−2` for all k. (`research/notes/step_law_proved.md`)
- Drain law: `y_{k+1} = y_k − 2·[x_k=2]`. Verified.
- Rule 90 interior: halved block evolves under XOR. **Proved** (`research/notes/rule90-interior.md`).
- Conditional-rate experiment: post-startup (2,4)-rate is family-independent (λ̂=0.585, p=0.68). Route A supported. **The gap: it is a point estimate, not a lower bound for all k.** This is TASKS.md item 1, the blocking task.
- CHT 2026 Thm 1.6: only obstructions are long zero-blocks / long shallow {0,d}-blocks. `holds-here: no` at reachable depth (R_0=4.2e8 ≫ 1000).
- Eppstein 2011: bounded-gap class alone insufficient. Colonna g=4 deletion gives left-edge failure.

## The blocking task (TASKS.md item 1, Route A)

Bound the (2,4)-event rate from BELOW. The mechanism is the coupled process:
intruder y drains by the drain law (2 per x=2 row, 0 per x=0 row) monotonically
to 4 and sticks; the edge x evolves as the terminal entry of the Rule-90/XOR
evolution of the halved block. Regeneration = first (x=2, y=4) hit. The rate
desired: if the (0,4)-stall (edge=0, intruder=4) cannot last more than G(b)
rows before the edge flips to 2, then inter-event gaps are bounded and the
rate is ≥ 1/(G(b)+1)-ish — but jumps are big, so recharge keeps pace.

Blocking lemma needed: **bound the worst-case number of consecutive rows the
terminal edge of a {0,2} block stays 0 while y=4** — a function of the halved
block's bit pattern only.

## What the searches turned up — concrete, usable, with sources

### 1. Blair Morgan (2026) — independent reduction to a local condition, and a new local obstruction

- **"Reducing Gilbreath's Conjecture to a Local Condition"**, Zenodo, 2026-03-21.
  https://doi.org/10.5281/zenodo.19143643
  Proves (his own reduction) that GC follows from `|G_r[2] − G_r[1]| ≤ 2` for
  all r ≥ 1 — i.e. the second entry in {0,2}/the gap between the first two
  entries of each row stays ≤ 2. This is logically the SAME content as the
  run's proved reduction (A_k(1) ∈ {0,2}), reached independently. Value:
  corroboration that the "second entry" framing is the standard reduction; and
  an independent computational check through 100,000 rows. Caveat: author
  h-index 0, Zenodo preprint, not peer-reviewed — a secondary corroboration,
  not a primary theorem the run does not already hold.
- **"The Return of the Lemma: launchpads, corridor obstructions"**, Zenodo,
  2026-03-21. https://doi.org/10.5281/zenodo.19144967
  Proves a local obstruction: a pure minimal 8→7→6→5→4 erosion corridor from
  the frontier-8 launchpad row is *impossible* (would force a zero-block in
  positions 4–7 contradicting Row 2's twos). This is an INDEPENDENT confirmation
  of the run's own finding that the regeneration obstruction is a local boundary
  affair that cannot be reached by a single straight erosion path — the same
  shape as the run's step-law + drain-law picture. Also a preprint, 0 citations.

**What these supersede:** neither is a rate bound; both are corroborating
framings of the reduction and of the local-obstruction picture the run already
holds. They do NOT close the gap; they confirm the run is attacking the right
object and that third parties now arrive independently at the same local shape
(the first external sign the "second entry in {0,2}" and "local obstruction"
picture is the accepted one).

### 2. Northshield (2010) — the exact generating-function machinery for the edge-evolution

- **"Sums across Pascal's triangle modulo 2"**, Sam Northshield, SUNY (2010).
  http://hdl.handle.net/1951/69939
  Studies sums `Σ (C(i+j,i) mod 2)` along lines `ai+bj=n` of Pascal's triangle,
  via generating functions with functional equations like `A(x) = (1+x+x^3) A(x^2)`.
  The run's edge value in the Rule-90 interior is EXACTLY a mod-2 binomial
  convolution: `e_d = XOR_{j=0}^d [C(d,j) mod 2] · h_{...}` (the block-lemma apex).
  The worst-case zero-run of the edge sequence `(e_0, e_1, ...)` is the question
  Route A's blocking lemma reduces to, and Northshield gives the generating
  functions / functional-equation (divide-and-conquer, base-representation)
  techniques for exactly these mod-2 Pascal sums. **This is the concrete toolset
  for the blocking lemma: express the edge as a mod-2 sum along a Pascal line and
  analyse its runs via the recursion `A(x) = P(x) A(x^2)`.**

**What it supersedes:** none of the refuted approaches (mod4 lift died on the
min branch; rule90 absorption died on bounded absorption time). This is a
*new, live* technical handle for the blocking lemma — it gives the algebraic
form of the edge-evolution so the zero-run can be bounded, which is the 
combinatorial Route A content that was left as "write a small program and
conjecture a bound." Northshield's recursion is the exact, non-numerical form.

### 3. Malyshev (2021) — extremal 1s in Boolean Pascal triangles

- **"Boolean analogues of Pascal's triangle with maximal possible number of
  ones"**, Malyshev, Discrete Math. Appl. (2021).
  https://doi.org/10.1515/dma-2021-0029
  Max # of 1s in a size-s Boolean Pascal triangle is ≤ ⌈s(s+1)/3⌉, achieved
  exactly on top row = Fibonacci mod 2. Relevant to the edge zero-run: bounds
  how sparse the 1s (edge=2 rows) can be in a triangular window — a lower
  bound on the rate of edge=2 rows, which combined with the drain law bounds
  the stall. A different extremal fact (Fibonacci-mod-2 extremality) worth
  knowing when bounding the (0,4)-stall.

### 4. OEIS — the block profile is uncatalogued (already known, confirmed again)

`[2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,175,175,175,290,289,288,739]`
→ no OEIS match. Not a dead end, but no closed form will be looked up; the
structure must come from the problem. (Also matches the run's known
`block_profile = A000232 − 1`.)

### 5. Cyclic Ducci — confirmed NOT the model

Lewis–Tefft 2024 (arXiv:2401.17502): vanishing of Z_{2^k}^{2^l} Ducci in ≤
(l+1)·2^{k−1} steps; Breuer–Shparlinski 2019 (Bull. Austral. Math. Soc.):
period lower bounds. All cyclic. The run's `ducci-classical-nilpotence-iff-
power-of-2` claim holds: power-of-2 vanishing is a *cyclic* fact, and the
half-infinite regeneration (where the cyclic theorem has no right edge) is
not covered. No new source gives a half-infinite rate bound; the cyclic
literature's period/vanishing results do not transfer.

## Verdict

- No published source proves a (2,4)-event rate lower bound for the 
  half-infinite Gilbreath triangle — that remains genuinely open and is this
  run's blocking task.
- The blocking lemma's own technical machinery **is** in the literature
  (Northshield's mod-2 Pascal-sum generating functions; Malyshev's extremal
  1s), and this run had not brought that to bear — the renewal-process approach
  file only proposed a brute-force `2^n` check. Northshield gives the exact
  algebraic form to replace the brute force with.
- Blair Morgan's two preprints independently rediscover the run's own
  reduction and local-obstruction shape — corroboration, not a rate bound.
- The two refuted approaches (rule90-absorbing-boundary, mod4-pascal) are not
  revived: the new handle is *different* — it uses Rule 90 only to get the
  exact algebraic form of the edge value (not a bounded absorption time), and
  it never needs the mod-4 lift.

## Sources

- https://doi.org/10.5281/zenodo.19143643 (Morgan, local-condition reduction)
- https://doi.org/10.5281/zenodo.19144967 (Morgan, return of the lemma)
- http://hdl.handle.net/1951/69939 (Northshield, modular Pascal sums)
- https://doi.org/10.1515/dma-2021-0029 (Malyshev, Boolean Pascal extremal)
- https://doi.org/10.48550/arxiv.2401.17502 (Lewis–Tefft, Z_{2^k} Ducci vanish)
- https://arxiv.org/abs/2607.08712 (CHT 2026 — already in library)
- https://doi.org/10.48550/arxiv.2510.06688 (Plouffe 2025, 10^14 — already in library)

All Morgan/Northshield/Malyshev items are preprints or working notes with
h-index 0 / low citation counts; treat as directional evidence, not
peer-reviewed theorem. I did not download them (search halted per directive);
they are cited from search collisions, so the exact statement of Northshield's
functional equation should be read in the source before building on it.
