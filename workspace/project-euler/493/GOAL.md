# Goal

## Problem statement (Project Euler 493, restated)

An urn contains **70 labelled balls**: **c = 7 colours**, with **m = 10** balls
of each colour. We draw **k = 20** balls uniformly at random *without
replacement*. Let X = number of *distinct colours* present among the drawn
balls. Find **E[X]**, the expected value, to nine digits after the decimal
point (`a.bcdefghij`).

### Symbols
- c : number of colours = 7
- m : balls per colour = 10  → total  N = c·m = 70
- k : balls drawn without replacement = 20
- X : distinct colours among the chosen k balls

### Worked example / test oracle
The statement gives *no* separate worked example beyond the answer itself.
The naive oracle (code/brute.py) therefore pins the definition on small
instances (c,m,k) by exhaustive enumeration of every k-subset, and cross-checks
a closed form against them. It then evaluates the real problem:
`E = 763700091/112000148 = 6.818741802...` → **6.818741802**.

Completion criterion: produce the decimal with nine digits after the point and
verify by a second independent route.
