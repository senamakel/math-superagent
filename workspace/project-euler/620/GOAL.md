# Goal

Solve Project Euler 620 ("Planet Gears"). Statement at `/workspace/problem.md`.

## Precise restatement (every symbol defined)

- A big gear C: an *internal* ring gear (teeth on the inside), circumference `c` cm
  (so `c` teeth, pitch 1cm).
- A small gear S: circle of circumference `s`, placed off-centre inside C.
- Four "planet" gears, circumferences `p, p, q, q` (p<q), inscribed within C but
  outside S, each tangent to BOTH C (internally) and S (externally). Planets may
  overlap each other. The closest gap between the boundaries of S and C must be
  >= 1cm.
- All of c,s,p,q integers >= 5 (number of teeth).
- "Perfectly meshing": constant angular-velocity ratio, teeth of one gear align
  with grooves of the other. Only certain discrete arrangements allow all gears
  to mesh simultaneously; these are counted.

- `g(c,s,p,q)` = number of such valid arrangements (finite).
  - Worked example: g(16,5,5,6) = 9.
- `G(n) = sum over s+p+q<=n of g(s+p+q, s, p, q)`, only p<q, p>=5, s>=5.
  - Worked examples: G(16) = 9, G(20) = 205.
- Target: G(500).

## Completion criteria (verifiable)

1. `code/brute.py`: an obviously-correct program (geometry + meshing, or an
   explicit enumeration of the discrete arrangement model) reproducing
   g(16,5,5,6)=9, G(16)=9, G(20)=205. If it cannot reproduce these, the
   arrangement/meshing model is wrong — fix it before anything else.
2. `solution.md`: the governing theory — how the meshing condition discretizes
   the configurations into a finite, efficiently computable count — and a method
   whose cost does NOT grow with the bound 500.
3. `code/solution.py`: exact integer arithmetic implementation agreeing with
   brute.py on every reachable case and reproducing all examples, then computing
   G(500).
4. G(500) verified by a second independent route.
