"""Interlacing analysis of the 84-vertex second subconstituent of srg(99,14,1,2).

Fix vertex 0. N(0)=7K2 (14 neighbours; c5). The 84 distance-2 vertices form an
induced subgraph H, each having degree 2 into N(0) and degree 12 within H, so
H is 12-regular on 84 vertices (trace 0, Perron eigenvalue 12).

G has spectrum 14^1, 3^54, -4^44 (n=99). By Cauchy interlacing for a principal
84x84 submatrix (n-m = 15 removed):
    alpha_i  >=  beta_i  >=  alpha_{i+15}
where alpha (1-indexed): alpha_1=14, alpha_2..55=3, alpha_56..99=-4.

Index arithmetic (1-indexed), beta_i for i=1..84:
  i=1      : beta_1 in [alpha_16=3, alpha_1=14]        -> Perron (12)
  i=2..40  : [alpha_{i+15}=3, alpha_i=3]            -> forced = 3   (39 values)
  i=41..55 : [alpha_{i+15}=-4, alpha_i=3]           -> free band [-4,3] (15)
  i=56..84 : [alpha_{i+15}=-4, alpha_i=-4]          -> forced = -4  (29 values)

Trace (12-regular, zero diagonal => sum of eigenvalues = 0):
  S = 12 + 39*3 + 29*(-4) + (sum of 15 free in [-4,3]) = 13 + F
  => F (the 15 free eigenvalues) must sum to -13, each in [-4,3].
  -13 in [-60,45]  => arithmetically consistent (no cheap contradiction).
  The interesting content is whether a 12-regular 84-vertex graph whose spectrum
  has EXACTLY 39 threes, 29 mines-fours and 15 values in [-4,3] summing to -13
  can simultaneously satisfy the mu=2 outer-adjacency rule -- the constrained
  object the pair-labeling approach builds. That graph is a highly rigid spectra
  + degree object, which is the a=7/14-specific 84-vertex lever.
"""
alpha = [14] + [3]*54 + [-4]*44   # 1-indexed by position (index 0 = alpha_1)
assert len(alpha) == 99
n, m = 99, 84
gap = n - m   # 15

forced3, forcedm4, freeband = [], [], []
for i in range(1, m + 1):            # beta index i, 1..84
    hi, lo = alpha[i - 1], alpha[(i + gap) - 1]
    if lo == hi == 3:
        forced3.append(i)
    elif lo == hi == -4:
        forcedm4.append(i)
    else:
        freeband.append((i, lo, hi))

print("Spectrum G: 14^1, 3^54, -4^44;  H on m=84, gap=15")
print(f"beta forced =3 : {len(forced3)}  indices {forced3}")
print(f"beta forced =-4: {len(forcedm4)}  indices {forcedm4}")
print(f"beta free band : {len(freeband)}  (pairs (index,lo,hi)) -> {freeband}")

perron = 12  # 12-regular
F = -perron - len(forced3)*3 - len(forcedm4)*(-4)
print(f"\nPerron=12, forced sum = 12 + {len(forced3)}*3 + {len(forcedm4)}*(-4) "
      f"= {perron + len(forced3)*3 - len(forcedm4)*4}")
print(f"15 free eigenvalues must sum to F = {F}; each in [-4,3]; "
      f"is -{F} in [{-4*len(freeband)},{3*len(freeband)}] -> "
      f"{'-4*15 <= F <= 3*15' if not(-60 <= F <= 45) else f'{-60} <= {F} <= 45 : yes, consistent'}"
      if F in range(-60,46) else f"PROBLEM: F={F} outside feasible band")
