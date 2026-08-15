# `evals/` — the calibration set

Conjectures that **have** been solved, presented to the harness as open, so a
run has a known destination and its trajectory can be scored.

Nothing here is mounted into a container. Only `workspace/conjectures/<slug>/`
is bind-mounted at `/workspace`, so the answer keys, the rubrics and the
plaintext blocklists in this tree are unreachable from a run by construction
rather than by instruction.

- The rules: [`AGENTS.md`](../AGENTS.md#calibration-runs).
- Why each control exists, and what it cost to learn:
  [`docs/calibration.md`](../docs/calibration.md).

## Layout

```
evals/
  screen.baseline.terms          blocklist merged into every problem
  <slug>/
    GROUND_TRUTH.md              the real name, the solution, the year, and an
                                 honest assessment of how much the de-naming
                                 and the seed's own hinting are worth
    RUBRIC.md                    milestone ladder and negative markers
    screen.terms                 the per-problem blocklist, plaintext
    seed/                        problem.md, GOAL.md, METHOD.md — de-named
    reports/                     one eval-report per run
  .build/<slug>/                 generated, gitignored
    screen.json                  hashed terms, mounted into the agent
    proxy.deny                   plaintext hosts, mounted into the proxy only
```

## The problems

| slug | de-named as | really is | what it tests |
| --- | --- | --- | --- |
| `unit-distance-plane-chromatic` | `χ` of the unit-distance graph on `R²` | Hadwiger–Nelson; de Grey 2018 | construction, exact arithmetic, SAT — machine-checkable, and recall does not help |
| `hypercube-induced-degree` | max degree of induced subgraphs of `Q_n` on `2^(n-1)+1` vertices | Sensitivity Conjecture; Huang 2019 | invention: one idea, no scale, no literature |
| `consecutive-perfect-powers` | `x^p − y^q = 1` | Catalan; Mihăilescu 2002 | depth, and whether the harness knows it is out of its depth |

Run `unit-distance-plane-chromatic` first: success is machine-checkable end to
end, so scoring is objective rather than a judgement about proof quality.

## Running one

```sh
./calibrate unit-distance-plane-chromatic
./diagnose  --workspace conjectures/unit-distance-plane-chromatic
./euler-tui --workspace conjectures/unit-distance-plane-chromatic
scripts/eval-report unit-distance-plane-chromatic
```

`./calibrate` compiles the blocklist, seeds the workspace without overwriting,
checks no answer key has landed inside the mount, brings the memory stack up on
an internal network, and refuses to start if a container is already mounted on
that workspace — resolved by mount, not by name, because two runs on one
workspace is silent and interleaves two investigations in one history.

## Adding a problem

A fourth needs all five files above. Two things are easy to get wrong:

- **The seed is a time capsule, not a puzzle with the hints removed.** State the
  art as of the year before the solution, honestly, including the obstruction
  and the leads genuinely available then. A dishonest seed measures nothing. If
  the seed has to hint substantially — sometimes it does, or the run spends four
  hours on a direction the field abandoned in 1970 — say so in
  `GROUND_TRUTH.md` so the score can discount it.
- **Every milestone needs an artifact, not a statement.** "A number nobody ran
  is not a result" is this repository's standard and it is the standard here.
