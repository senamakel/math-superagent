# The numeric oracle in code/lib/gears.py does not reproduce g(16,5,5,6)=9

`code/lib/gears.py` implements a continuous model: it parametrizes the S↔C
centre distance `d`, requires each planet's centre to lie on `circle(O,R−ρ) ∩
circle(S,r+ρ)`, and checks 8 tooth-alignment phase congruences. `g_count` scans
the continuous `d` interval, isolates residual minima, and counts them.

## Check performed (this run)

Command (single oracle call, the same code path `brute.py` would use):

```
PYTHONPATH=/workspace/code python3 -c "from lib.gears import g_count; print(g_count(16,5,5,6))"
```

**Result: `g(16,5,5,6) = 0`** — but the problem statement gives **9**.

## Why it is not a numerical fluke

A fine scan (20000 points) of the residual `|sin(4πFp)|+|sin(4πFq)|+|sin(2πH)|
` over the entire valid `d` interval found its global minimum **only at the
degenerate endpoint** `d = 1/(2π)` (where the two same-size planets coincide),
and a scan excluding that endpoint found **zero** near-zero residuals. So the
model believes no non-degenerate valid arrangement exists at all. It is not a
grid-resolution miss; the parameterization itself misses all 9 real
arrangements.

## Conclusion

```claim
id: oracle_model_reproduces_zero
statement: The continuous centre-distance model in code/lib/gears.py returns
  g(16,5,5,6)=0, contradicting the stated value 9; no non-degenerate valid d
  exists under that model.
hypotheses: g is parametrized by a single continuous centre-offset d, and the
  meshing condition is the 8 phase congruences on that d.
holds-here: false — contradicts the worked oracle value 9.
status: checked Per least-mesh-angle
  theory (beta = 2*pi/(s+c)) the arrangements are a discrete combinatorial
  count over planet angular positions that are multiples of beta; the run has
  not yet implemented that model, so no genuine g/G sequence exists yet.
anchor: code/lib/gears.py; this run's g_count(16,5,5,6) = 0
```

## Consequence for pattern analysis

Until the discrete (least-mesh-angle) model is implemented and reproduces
g(16,5,5,6)=9, G(16)=9, G(20)=205, the workspace contains no trustworthy
computed integer sequence. `analyze_sequence` / `find_linear_recurrence` /
`oeis_lookup` were therefore not run: there are no program-produced terms to
feed them. Pattern work resumes the moment the discrete oracle emits a genuine
G(n) (or per-tuple g) sequence.
