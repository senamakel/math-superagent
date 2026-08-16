"""Verify the Phillips Thm 4.2 criterion for srg(99,14,1,2), the BvLS control (243),
and the three Thm 4.5 graphs (9, 15, 27).

Correct note: for a locally-linear (lambda=1) srg, lambda=1 forbids K4 (each edge
in exactly one triangle), so the maximal clique size is omega = 3, NOT k/2.
The k/2 = 7 is the number of triangles through a vertex (used to compute the
DEGREE of the triangle graph, d = 3(k/2 - 1) = 18), not the clique size omega.
Thm 4.2 (with omega=3, omega-1=2):
  C_3(Gamma) strongly regular  iff  s == -k/2  OR  k == 6
where s is the negative eigenvalue.
"""
import math

def eig_s(v, k, lam=1, mu=2):
    """negative eigenvalue s of srg(v,k,lam,mu)."""
    # roots of x^2 + (mu-lam)x + (mu-k) = 0
    b, c = (mu - lam), (mu - k)
    disc = b*b - 4*c
    return (-b - math.sqrt(disc)) / 2

print("Thm 4.2 criterion for C_3 strongly regular: s == -k/2  OR  k == 6")
print("(omega = clique size = 3 for lambda=1; omega-1 = 2)")
print()

cases = [(9,4,2,"rook/Paley 9 (in Thm 4.5 set)"),
         (15,6,3,"(in Thm 4.5 set)"),
         (27,10,5,"(in Thm 4.5 set)"),
         (99,14,2,"Conway 99 (not in set)"),
         (243,22,2,"BvLS control (not in set)")]
for v, k, mu, label in cases:
    s = eig_s(v, k, 1, mu)
    c1 = (abs(s - (-k/2)) < 1e-9)
    c2 = (k == 6)
    print(f"srg({v},{k},1,{mu}) {label:35s} s={s:7.3f} "
          f"s==-k/2?{str(c1):5s} k==6?{str(c2):5s} C3-srg?{c1 or c2}")

print()
print("Interpretation:")
print(" - rook(9,4,1,2) passes (s=-2 == -k/2)  -> in the three, C3 IS srg")
print(" - (15,6,1,3),(27,10,1,5) pass (k=6)    -> in the three")
print(" - (99,14,1,2) fails BOTH                -> C3 NOT srg  (Thm 4.5)")
print(" - (243,22,1,2) BvLS fails BOTH          -> C3 NOT srg too,")
print("   so the claim does NOT kill 243: it is a constraint shared by 99 and 243,")
print("   consistent with the negative-control rule (does not rule out 99).")
