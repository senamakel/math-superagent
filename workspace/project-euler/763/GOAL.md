# Goal

## Problem (Project Euler 763)

Three-dimensional grid of cubes. An amoeba in cube (x,y,z) can divide into
three amoebas occupying (x+1,y,z), (x,y+1,z), (x,y,z+1), provided those three
cubes are all empty. The dividing amoeba disappears.

- Start: one amoeba at (0,0,0).
- Each division: the dividing amoeba is removed and three new ones appear
  (+2 amoebas net). After N divisions there are 2N+1 amoebas.
- D(N) = number of **distinct** arrangements (sets of occupied cubes) reachable
  after exactly N divisions. The same arrangement reached many ways counts
  once.

## Worked examples (test oracle)

- D(2) = 3
- D(10) = 44499
- D(20) = 9204559704
- last nine digits of D(100) = 780166455

## Target

- Find D(10000), last nine digits.

## Completion criteria

- brute.py reproduces D(2)=3 and D(10)=44499 (done: both matched).
- brute.py at D(20) times out at 50s (state space ~9.2e9) — out of reach for
  the oracle, as expected; it is a definition-checker, not a solver.
- solution.py agrees with brute.py on every case brute.py can reach and
  reproduces D(20) and the D(100) last-nine-digits example.
- Final D(10000) verified by a second independent route.

## Progress notes

- Exact BFS oracle ceiling reached: D(14)=5949063 is the last D(N) computable
  by exact BFS in this container (2 GiB cgroup memory cap; D(15) ~20M states
  needs ~12+ GiB). D(14) verified by three independent routes.
- Actual reachable configs for N=3 (9) and N=4 (30) dumped to
  code/out/configs_n3_n4.txt for structural study.
