# Library update report

## Reproduction requirement

The existing naive oracle `code/collatz_oracle.py` was retained as the small-instance oracle. Its existing output `code/out/brute_worked_examples.txt` reproduces the standard examples used by the statement, including the 1→4→2→1 cycle and small starting values. The full-size method is not brute force: Barina’s source reports distributed accelerated/sieved computation to 2^71.

## Structural line chosen

This run uses accelerated Collatz dynamics, parity-vector/sufficiency reductions, and Diophantine analysis of hypothetical cycles. A minimal counterexample is treated as either an unbounded orbit or a nontrivial cycle. Monks’s theorem reduces each sub-conjecture to any arithmetic progression, while Hercher and Simons–de Weger constrain cycle patterns. The unresolved obstruction is worst-case control of parity frequencies and divergence; density-one theorems do not address it.

## Source-backed facts

- Barina 2025: finite verification below 2^71; source and bounded note under `research/sources/` and `research/summaries/`.
- Tao: logarithmic-density-one almost-boundedness, not universal convergence.
- Monks: every nonconstant arithmetic progression is sufficient, including for divergence and nontrivial cycles.
- Everett: density-one finite stopping time for the accelerated map.
- Hercher: no m-cycle with m≤91 local minima.

The claims with hypotheses, evidence, status, and falsifiers are in `research/CLAIMS.md`; the expanded overview and known failed approaches are in `research/ROOT.md`. The memory service was unavailable, so the same durable findings were copied to `MEMORY.md`.

## Open gaps

The exact current effective irrationality measure for log(3)/log(2), and a clean independently checked cycle-length theorem beyond the local-minima result, remain requests. The official Simons–de Weger published PDF also remains blocked by HTTP 502; the author-hosted preprint is held and used with that limitation recorded.
