# Lu & Raz, "Note on the union-closed sets conjecture and Reimer's average set size theorem" (arXiv:2405.10639, 2024)

**Full text:** [[lu-raz-reimer-note-2024.full]] · **Source URL:** https://arxiv.org/pdf/2405.10639

## What it establishes

Reimer's 2001 average-set-size theorem: any union-closed family `S` on `[n]` has
average set size `≥ (1/2) log₂|S|`. Reimer proved this by showing union-closure
implies a family satisfies "Reimer's conditions" (there is a filter `F ⊆ P([n])`
and a bijection `A → F_A` carrying the family to the filter, structured so the
average-size bound follows).

**Question (from Gowers' polymath project):** do Reimer's *conditions alone* (without
union-closure) force the abundance condition (the UC conclusion)? If yes, UC would
follow from Reimer's conditions.

```claim
id: lu-raz-reimer-conditions-dont-force
statement: Reimer's conditions (a bijection of the family onto a filter, as in
  Reimer's proof) do NOT force the abundance condition. There are arbitrarily many
  families satisfying Reimer's conditions that lack an element in ≥ half the sets,
  with any fixed lower bound on member-set size. A minimal counterexample was first
  given by Raz (2017); this note generalises it.
hypotheses: families satisfying Reimer's conditions (filter-bijection), universe [n].
holds-here: yes (negative result about the natural relaxation of UC's hypotheses).
status: proved (Theorem 1, constructions in source).
bearing: rules out the "replace union-closure by Reimer's conditions" route to UC:
  the averaging structure alone is insufficient; union-closure proper must be used.
  Reinforces the run's negative control #2 (union-closure must be used) and gives
  explicit families.
anchor: research/sources/lu-raz-reimer-note-2024.full.md
```

```claim
id: lu-raz-closure-size
statement: For the constructed families S, the size of the union-closed closure
  cl(S) is Θ(n²), so |S|/|cl(S)| → 0 as the universe size grows.
hypotheses: the constructed S (Section 3), ground set [n].
holds-here: yes
status: proved (Corollary 1).
bearing: the counterexamples to "Reimer's conditions ⟹ abundance" are sparse
  relative to their closure — a quantitative note on how far such constructions
  sit from being union-closed.
anchor: research/sources/lu-raz-reimer-note-2024.full.md
```

## Bearing for this run
A concrete, recorded dead end for the *average-size* line: GoAL's negative
control #2 (union-closure must be used) is here sharpened to "even Reimer's
conditions are not enough". Any argument that works from average set size /
Reimer's conditions without union-closure is refuted by these families. Relevant
to the combinatorial line and to anyone attempting the Reimer route.
