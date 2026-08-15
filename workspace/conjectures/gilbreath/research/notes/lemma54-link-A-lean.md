# Link A of Granville Lemma 5.4 — Lean 4 formalisation of the combinatorial core

```claim
id: lemma54-link-A-lean-formalised
statement: Link A of Granville Lemma 5.4 at its combinatorial core: the orbit
x_0 = w, x_{s+1} = |x_s - e_s| (runAbs) is bounded above by any M that bounds
the start w and every pattern entry e_s.  Concretely, for all naturals:
(1) |a - b| <= max(a,b)  (dist_le_max, the core induction step);
(2) runAbs w el <= M whenever w <= M and forall e in el, e <= M  (run_le);
(3) runAbs v el <= max v (maxAll el)  (orbit_le_max).
This is v <= g*_n modulo identifying g*_n as a common upper bound of v and
the eps_s (a geometric step, not covered here).
hypotheses: el : List Nat, w v M : Nat, no evenness/pattern restriction on el.
holds-here: yes
status: formalised
formalisation: code/lean/link_a.lean
anchor: code/lean/link_a.lean
bearing: Proves the |a-b| <= max(a,b) induction and the generic orbit-bounded
invariant that underpin the v <= g*_n leg of Granville Lemma 5.4.  Together
with descent_lemma.lean (descent-lemma-halved-formalised) it covers the two
structural legs of the lemma's combinatorial heart.  The composition
g*_n <= 2*nu2+2 => success still needs the record-gap definition and the
reduction-passage geometry in Lean.
```

## What Link A is

In the right-diagonal reduction of Granville Lemma 5.4 the orbit is

    x_0 = v,   x_{s+1} = |x_s - e_s|

(the `runAbs` trajectory, same convention as `code/lean/descent_lemma.lean`),
and `g*_n` is the record gap — a common upper bound for the starting value `v`
and every `eps_k`. Link A is the claim that the whole orbit never exceeds the
record:  `runAbs v el <= g*_n`.

The engine is the pointwise inequality `|a - b| <= max(a, b)`: each descent
step keeps the value at most the running max, so the orbit stays inside
`[0, max(v, max_s e_s)]`. The lower bound 0 is automatic for naturals, so
Link A reduces to the upper bound.

## What is proved (sorry-free, kernel-checked)

`code/lean/link_a.lean` — `lean_check` compiled=true, verified=true, sorry
warnings none (verdict `code/out/lean/code_lean_link_a.lean.json`).

- `dist_le_max (a b : Nat) : Nat.dist a b <= max a b` — the core induction
  step, for all naturals.
- `maxAll` / `maxAll_ge` — list maximum; every element <= its max.
- `run_le : forall el w M, w <= M -> (forall e in el, e <= M) -> runAbs w el <= M` —
  the generic orbit invariant: if the start and every pattern entry are <= M
  then the whole orbit is <= M.  This is exactly Link A modulo the
  identification of `g*_n` as a common upper bound.
- `orbit_le_max : runAbs v el <= max v (maxAll el)` — the boundedness
  invariant with the maximal bound made explicit.

Axiom footprint (`#print axioms`):

- `dist_le_max`, `run_le`, `orbit_le_max`: `[propext, Classical.choice, Quot.sound]`
- `maxAll_ge`: `[propext]`

No `sorry`, no `sorryAx`, no `native_decide`.

## What this joins, and what it does not

Cross-file import does **not** work in this container (read-only root, no
writable Lean project — verified: `import descent_lemma` fails with "unknown
module prefix"), so `link_a.lean` is deliberately self-contained and redefines
`runAbs` rather than importing `descent_lemma.lean`.  The two files agree on
the `runAbs` convention.

Together `descent_lemma.lean` (the absorption/descent core — {0,2} absorbing,
`x_L in {0,2} <-> v <= 2*nu2+2` for even v) and `link_a.lean` (the `v <= g*_n`
bound) cover the two structural legs of Lemma 5.4's combinatorial heart.  The
composition `g*_n <= 2*nu2+2 => v <= g*_n => success` would then close the
loop; it is not yet a single Lean theorem because the record gap `g*_n` and
the reduction-passage geometry entering it are not yet defined in Lean.  That
is the precise piece still missing toward a full Lean Lemma 5.4, and it is a
definitional/geometric step, not a gap in `dist_le_max` or `run_le`, which are
themselves complete and kernel-checked.
