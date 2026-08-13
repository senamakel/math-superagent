# Tao 2026 — Gilbreath decay constants c_n (companion applet page)

**Full text:** none separate — the applet page (2275 bytes) is a thin HTML shell
linking a browser simulation; its whole content is this summary.
**Source URL:** https://teorth.github.io/tao-web/apps/gilbreath-cn.html
**Complete source on disk as this summary.** (The `.full.md` file is not
created because the page IS the 2275-byte document; the summary carries all of
its content.)

## What it establishes

The CHT (Chase–Hunter–Tao 2026) stationary continuous Gilbreath model: top row
iid standard exponential, `c_n = E a(n,j)` depends only on depth. The page states:

- CHT proved `Σ_{i≤n} c_i ≥ log(n+e)` — the constants cannot decay exponentially;
- CHT computed `c_0..c_3` exactly and **cannot prove `(c_n)` bounded**;
- Michael M. Ross's Monte-Carlo study to depth 8192 (Zenodo 10.5281/zenodo.21326026,
  code at github.com/michaelmross/Gilbreath) anchored by new exact rationals
  `c_4, c_5, c_6` found the digit-sum law:
  `c_n ≈ C·λ^{s2(n)}/n`, `λ ≈ 1.14–1.20`, explaining the sawtooth (`c_2<c_3>c_4<c_5>c_6`);
- the applet is a browser estimator of `c_n` (deterministic per seed, no network calls).

## Bearing on this run

The averaged decay rate of the array (its "regeneration rate" measured in
expectation) is itself still open — `c_n` bounded vs not is unsettled even in
the model. Any claimed regeneration mechanism for the primes has this
quantified, still-open shadow that a mechanism which *forced* fast decay would
have to be checked against. The digit-sum law is the current empirical shape of
the decay.

## Status

Sourced from Tao's own companion page (July 2026), consistent with the landed
CHT full HTML (which proves the log bound and exact c_0..c_3) and the Ross
Zenodo note already in the library. The digit-sum law is empirical (Monte
Carlo), not a theorem.