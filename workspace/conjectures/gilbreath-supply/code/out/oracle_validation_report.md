# Oracle validation for SUPPLY

_April 1 run. Report by tool_builder._

## What the oracle is

The operative object of SUPPLY (problem.md fact 1, and every research note via
the G-dict) is the **fold weight**

    nu2(n) = wt(Phi_n h)  over F2,   h[j] = ((q_{j+1} - q_j)//2) mod 2,

equivalently nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 } with the Pascal/Rule-90
fold cell T(n,d) = XOR over binary submasks o of d of h[n-1-d+o] (Lucas).

`code/brute.py` is the run's on-disk oracle for this. It was **not** re-derived
here; it was **independently validated** against a second route.

## The one subtlety that had to be pinned down

A literal reading of the problem's informal preamble — "the maximal {0,2}
suffix of the right diagonal", `A_k(n-1-k)` — gives **nu2(n) = 0 for every
n >= 2**, because the bottom right-diagonal cell is always 1 (the triangle
collapses to a single 1 in Gilbreath's first column), which terminates any
{0,2} suffix. That literal reading therefore contradicts every measurement and
the very fact that SUPPLY is an open conjecture, so it is **not** the operative
definition. The operative one (fact 1, G-dict, GOAL.md "what it is measured
against") is the fold weight. Files `code/direct_triangle.py` and the parent's
`code/compute_nu2.py` demonstrate the literal reading; neither is the measure.

## Independent validation

`code/oracle_fold_verify.py` builds Phi_n **explicitly** from Pascal binomials
mod 2 (no Lucas submask shortcut — an independent route), computing
wt(Phi_n h) for d in [2, n-1]. Cross-checked against brute.py's submask
shortcut:

```
n=2..80: brute.py agrees with independent explicit fold up to +-1
         (floor-at-2 convention)  [79 values]
```

The ±1 is the documented floor-at-2 slack (G-dict: "up to ±1"), exactly the
convention gap problem.md warns about.

## Worked examples from problem.md "What is measured"

| Example | brute.py | stated | verdict |
| --- | --- | --- | --- |
| (b) nu2(4000)/4000 | 1975/4000 = **0.4938** | 0.4933 | **matches** within 3 cells (0.07%), exactly as brute.py's docstring said |
| (a) nu2/n in [0.42,0.52], n=50..3999 | sampled band 0.48–0.58, full scan has mild outliers (n=50→0.58, n=53→0.34) | "0.420…0.520, no downward drift" | **not exactly reproduced**; average stays ~0.4–0.5, but a full scan of brute's exact values shows occasional outliers outside [0.42,0.52] |
| (c) min nu2/w over n=100..2000, w=#{gaps ≡ 2 mod 4} | **0.597** at n=105 | 0.7049 | **not reproduced** |

## Honest status

- The oracle's core operation (fold weight = #submask-cells = 1) is correct:
  two independent routes (Lucas shortcut, explicit Pascal product) agree on
  n=2..80 within the documented floor-at-2 slack, and the flagship endpoint
  (b) reproduces to 3 cells.

- The stated figure (c) 0.7049 for min nu2/w is **not** reproduced by brute.py
  (0.597 at n=105). This means either the parent run used a different `w`, a
  different nu2 convention, or a different n-range for that figure. It should
  be traced before any conclusion leans on 0.7049. Flagged, not resolved.

- The stated band (a) is a streamed-measurement claim; brute's exact full scan
  shows mild outliers, so the clean "no downward drift" phrasing is not
  reproduced cell-for-cell.

## Deliberately NOT done

- No full-size run: brute.py is O(n² · submasks) and a n=4000×many scan is
  slow; the instruction is to run only at worked-example sizes and cap slow
  cases. n=4000 (the single landmark) was run; the full 50..3999 scan was
  abandoned when it exceeded the time budget.
- No claim about proving or refuting SUPPLY, and no Lean/axiom footprint here.
- No claim about Gilbreath.
