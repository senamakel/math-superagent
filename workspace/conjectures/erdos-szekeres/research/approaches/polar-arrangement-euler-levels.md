```approach
idea: Point-line polar duality, counting faces/cells/zone-levels of the dual arrangement of lines rather than points in convex position.
mechanism: (unchanged) Hoped an Euler-characteristic / level-count of the dual line arrangement would bound the number of lines by 2^{n-2}.
status: refuted
killed-by: The polar dual is NOT the point-ES problem. Bárány–Roldán-Pensado–Tóth, "Erdős–Szekeres theorem for lines" (arXiv:1307.5666, Thm 1.1): ES_L(n), the least #lines forcing n lines bounding a convex n-cell, satisfies 2^{n-4}⌊n/2⌋−1 ≤ ES_L(n) ≤ C(2n-4,n-2) — ~4^n/n to ~4^n/√n — and the authors state explicitly that in the affine plane the point and line versions are NOT dual ("the dual of the convex hull of n points is not an n-cell"); only caps/cups duality survives (ESl(n) ≤ ES(2n)). So any Euler/zone/level face-count reproduces exactly the ~4^n loss the mechanism's own falsifier predicted. The Goodman–Pollack pseudoline conjecture Nps(n) ≤ 2^{n-2}+1 is itself open (Morris–Soltan §5.5), so the dual formulation restates the difficulty rather than removing it. Closed on the literature, not on absence.
```
