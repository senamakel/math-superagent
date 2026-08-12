# Tasks

- [x] tool_builder naive-oracle run: `python code/brute.py circle` reproduces
      V_circle = 4.60333885 (worked example 1 ✓). `code/explore_general_dash.py`
      confirms the naive straight-dash model caps at pi+1 = 4.14159 and does
      NOT match the circle oracle (red herring, on record). Square example
      (5.78859314) reproduced by `code/polygon_critical.py` → 5.78859314459.
      Attempted naive polygon oracle was degenerate (unconstrained staging
      inflates the ratio) — deleted, not a result.
- [x] Read problem statement; restate in GOAL.md with symbols.
- [x] tool_builder: write and run code/solution.py (exact stewbasic formula, mpmath dps=50).
       Reproduces anchors n=3->7.4049183473, n=4->5.78859314459 (oracle 5.78859314),
       n->inf->4.60333885. ANSWER V_hexagon=5.055050463303893 (15 dp) = 5.05505046 (8 dp).
- [ ] research: governing theory (circle critical speed identity) + source URL.
- [ ] symbolic_math: exact circle critical equation and high-precision V_circle.
- [ ] Derive polygon (square, hexagon) model; V_hexagon to 8 decimals.
- [ ] Implement code/solution.py with exact arithmetic; agree with brute + oracle.
- [ ] Verify V_hexagon by a second independent route.
