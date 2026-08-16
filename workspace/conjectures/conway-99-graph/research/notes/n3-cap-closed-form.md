# n3 cap closed form — the tightest upper bound on n3 at (99,14,1,2)

**Status: checked.** Capture: `code/out/n3_cap_closed_form.captured.txt`
(real program output), source script `code/out/n3_cap_closed_form.py`,
brute cross-check `code/out/n3_cap_crosscheck.py`,
Integer check `code/out/n3_cap_intcheck.py`.

## The result

The 62 Reimbayev order-6 subgraph-count formulas are each of the form
`(n,k)-term ± c·n3`. The tightest nonnegative upper bound on `n3` they admit is

```
cap = n*k*(k-2)/4 = k*(k-2)*(k^2+2)/8     (n = v = 1 + k^2/2)
```

- For `k>=6` the binding formula is `n1 = (1/12) n k (k-2) - n3/3`.
- For `k=4` the binding formula is `n5 = (1/8) n k (k-2)(k-4) - n3`, whose base
  vanishes, so `cap = 0` (the rook graph has no free n3).

Verified symbolically in sympy (exact, coeff rationals) **and** against brute
force over all 62 formulas at every `k>=6` feasible member:
`k=14 -> 4158`, `k=22 -> 26730`, `k=112 -> 19320840`, `k=994 -> 121781611728`,
all `match=True`. Degree 8 in `u`.

Cap sequence over the five feasible members:
`[0, 4158, 26730, 19320840, 121781611728]`.

Residue: `n3 === 0 (mod 3)` at every member; at `(99,14)` the admissible set is
the 1387 multiples of 3 in `[0, 4158]` — sharp (4158 admissible, 4159 not).

## Two-sided statement at 99

```claim
id: n3-cap-closed-form
status: checked
scope: any putative srg(99,14,1,2)
holds-here: yes -- the statement is intrinsically about (99,14,1,2): lower side
  is the Makhnev conditional (n3=0 => nonexistence) applied at 99; upper side
  is the cap k(k-2)(k^2+2)/8 evaluated at k=14. Both control graphs have n3=0
  and are not contradictory to this constraint (they are the n3=0 witnesses the
  lower bound's contrapositive exempts via mu<=3).
statement: 1 <= n3 <= 4158
lower side: n3 >= 1  -- re-derived Makhnev 1988 Thm 2 chain
    (n3=0 would force the parameter-infeasible srg(33,12,1,6) subobject);
    verified-computationally for the integrality step, asserted-by-source
    for the lemma chain. Anchor: code/out/check_srg33_12_1_6.captured.txt,
    code/out/check_makhnev_n3_counts.captured.txt, and solution.md section 1.
upper side: n3 <= 4158  -- THIS note; the cap closed form n*k*(k-2)/4,
    checked here (exact symbolic + brute force over all 62 formulas).
harms: supersedes the older interval [0,4158] used where n3>=1 was not yet
    imported; the lower endpoint is now 1, not 0.
falsifiers: an n3 value outside [1,4158]; on the upper side by an error in
    the 62-formula transcription; on the lower side by an error in the
    Makhnev conditional. Within the family the residue n3===0 (mod 3)
    makes the only admissible sharp values 3, 6, ..., 4158.
```

## How this is categoryised

- **Checked:** the cap closed form `n*k*(k-2)/4` over the sourced 62-formula
  catalogue (exact arithmetic; a derivation, not a fit).
- **Sourced + re-derived:** the `n3 >= 1` lower bound (Makhnev 1988 Thm 2;
  this run re-derived the integrality step rejecting srg(33,12,1,6)).
- The conjunction `1 <= n3 <= 4158` is a **constraint**, not a nonexistence
  proof: the interior case `n3 >= 1` (and specifically `n3 >= 3` from the
  residue class) remains open.
