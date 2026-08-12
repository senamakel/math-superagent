# Tasks

## Done
- [x] Read problem statement; restate in GOAL.md with symbols.
- [x] tool_builder: `code/brute.py circle` reproduces V_circle = 4.60333885 (oracle ✓).
- [x] tool_builder: `code/solution.py` (stewbasic formula, mpmath dps=50) reproduces
      all anchors n=3→7.4049183473, n=4→5.78859314459 (oracle 5.78859314),
      n→∞→4.60333885. V_hexagon = 5.055050463303893 (15 dp) = 5.05505046 (8 dp).
- [x] tool_builder: exact closed form V_hexagon = 2 + 2√21/3 confirmed.
- [x] Governing theory identified: stewbasic n-gon formula, Abel et al. model,
      David K square closed form, circle identity (Ponder This May 2001).
- [x] Single independent game-encoding solver (`code/indep_game_encoding.py`)
      built and run — FAILS (encodes straight-dash red herring, not the
      tangent-chord staging). Output captured but must not be cited as
      verification. See CONTEXT.md Validation section.

## In flight (directive 1)
- [ ] **librarian: primary-source research pass.** Fetch and download into
      `research/sources/` the pursuit-evasion literature the hexagon game rests
      on. Do not rely on the run's existing summaries — get the primary texts.
      Specific targets:
      (a) lion-and-man problem classics and Besicovitch's escape argument;
      (b) "boy escaping teacher on regular n-gon" — any primary formulation
          beyond the Math.SE thread already in library;
      (c) swimmer-in-circular-pool — the Martin Gardner / Richard Guy origin,
          and any rigorous treatment of the two-phase staging strategy;
      (d) general theory of optimal escape trajectories from convex domains —
          involutes, chase curves, and the critical speed ratio.
      Record source URL in every file; put each governing result as a claim
      block so it reaches `research/CLAIMS.md`. Save full texts as
      `research/sources/<slug>.full.md` with a summary beside it.
- [ ] **symbolic_math: independent first-principles hexagon derivation.**
      Derive V_hexagon from geometry alone, without relying on the stewbasic
      K-index formula. Goal: agree with 5.05505046330389… to 8 dp. This is the
      missing independent route that the current CONTEXT.md Gaps section flags.
      Derive the staging region and dash geometry for the regular hexagon
      directly from the boundary-time equalization principle, and produce an
      exact expression (not a numeric root-find). Write the derivation to
      `research/notes/hexagon-first-principles.md`.
- [ ] **curator: verify and close.** When both the librarian's sources and
      symbolic_math's derivation are in, confirm the independent derivation
      agrees with the stewbasic value, update CONTEXT.md to record the second
      route, and close the hexagon-critical-speed thread.