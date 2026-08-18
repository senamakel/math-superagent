# I^1_6b four-passage ECT oracle run

**Claim linkage:** `h16-i6b-four-passage-ect-obstruction`.

## Precisely tested claim
The shortcut “four passage contributions each form an ECT pair, therefore their sum forms an ECT pair/system” is false without an additional independence/non-cancellation hypothesis. A second finite algebraic boundary claim is that a parameterized pair `[a, a*x]` loses ECT rank at `a=0`.

## Method and theory
The ECT criterion used is the nonvanishing Wronskian criterion for a polynomial pair. The executable uses exact SymPy symbolic determinants. It is not a dynamical I^1_6b model and therefore cannot prove or refute the actual graphic's cyclicity; it tests the proposed algebraic inference and explicitly exposes its missing hypothesis.

## Required naive guard
`code/i6b_four_passage_oracle.py` calls `naive_count` from `code/naive_examples_oracle.py` and reproduces all five worked examples in `problem.md`: counts `1,0,0,2,1` respectively. These outputs are an oracle consistency check only.

## Executed command
`python code/i6b_four_passage_oracle.py > code/out/.i6b_four_passage_oracle.run.tmp.txt && cat code/out/.i6b_four_passage_oracle.run.tmp.txt && mv code/out/.i6b_four_passage_oracle.run.tmp.txt code/out/i6b_four_passage_oracle.captured.txt`

Parameters: symbolic `x`; parameter `a` with boundary `a=0`; polynomial degree at most 1 in the ECT representatives. Precision: exact rationals/symbolics, no floating point. Complexity: polynomial for fixed number of passages and polynomial degree.

## Output
- `W(1,x)=1`, `W(-1,-x)=1`; their componentwise sum is `[0,0]` with Wronskian `0`.
- `[a,a*x]` has Wronskian `a**2`; at `a=0` it becomes `[0,0]` with Wronskian `0`.
- All five guards pass.
- Verdict: the proposed ECT closure under four-passage addition is **refuted algebraically**.

## Obstruction and status
This is a logical/algebraic obstruction, not a faithful dynamical counterexample. A valid I^1_6b route must establish a non-cancellation/independence condition for the actual passage functions, uniformly including boundary strata, before invoking ECT. The smooth test is not passed by this shortcut alone: ECT/analytic structure is present in the criterion, but the tested inference has no dynamical analyticity control. Lower-bound and slow-fast tests are not applicable to this purely algebraic refutation; they remain required for any proposed cyclicity bound.
