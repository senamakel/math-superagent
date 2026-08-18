# Request status — geometric-weight floor-sum monoid (deferred, unfilled in English lit)

The three requests `citable-name-treatment-0c91`, `citable-precise-statement-600d`,
`citable-precise-statement-d2e7` ask for a citable academic treatment of the
geometric-weight (x^i) generalized floor_sum / universal-Euclidean monoid.

**Status as of this cycle: not fillable from English-language primary
literature.** A `deep_research` synthesis (which read 9+ sources and - after
weighing them - said the same conclusion) plus several `exa_search`/`find_similar`
rounds confirm: the closest peer-reviewed anchors carry the *spirit* (a closed
moment family under Euclidean affine+reciprocal transforms) but not the exact
`sum x^i floor((ai+b)/c)` / `(count, sum x^i, sum x^i floor, sum x^i floor^2)`
monoid-closure recursion this run uses.

The claims that close these requests already exist and are sourced to the
strongest obtainable anchors:
- `req-close-universal-euclidean` — OI-wiki / fhq / LOJ138 / AtCoder library
  (primary, Chinese + AtCoder), all on disk.
- `universal-euclidean-geometric-floor-sum` — fhq note carries the exact
  6-component monoid and merge recursion verbatim.
- `geometric-sum-division-algorithm` — Patrício & Hartwig, "From Euclid to
  corner sums" (Filomat 2021, on disk), the citable published statement of the
  geometric-weight Euclidean split.

**What would falsify the run's belief (and reopen the hunt):** a source showing
the x^i recursion is NOT O(log) for x != 0 (i.e., the tuple closure is not
preserved under the Euclidean reduction) — none found; or the run's own
in-container execution of `code/lib/ueuclid.py` failing its acceptance tests.
The latter is the real gate and is tool_builder's job, not the librarian's.

The literature hunting of this exact question has now been done 4+ times; this
cycle's confirmation closes the search for good. If a later run wants to
re-visit, the falsifies-column wording above is the query to aim at, not the
topic name.