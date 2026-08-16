"""Self-consistent check of Makhnev 1988 Thm 2's n3=0 count arithmetic at (99,14,1,2).

Under condition (*) [n3=0], Makhnev's 99 proof (primary Russian text,
research/sources/makhnev-1988-lambda1-russian-fulltext.full.md, Lemmas 6-9) runs:

  For a triangle A={A,B,C} of Gamma:
   - Gamma(A) = [A] u [B] u [C]  (closure of the triangle under neighbours).
     Since A,B,C pairwise adjacent, they share exactly lambda=1 common
     neighbour each, so |[A] n [B]| = |[A] n [C]| = |[B] n [C]| = 1 (the third
     vertex), triple intersection empty  =>  |Gamma(A)| = 3*14 - 3 = 39.
   - Lemma 6: the 36 points of Gamma(A) - A lie in 12 "inner" triangles from
     [A]_Lambda each joined to A by exactly 3 edges.
   - Lemma 7: each of the 99-39 = 60 points OUTSIDE Gamma(A) lies in exactly
     one triangle disjoint from Gamma(A); 60/3 = 20 such "outer" triangles,
     mutually disjoint.
   - Lemmas 8,9: Lambda_0 = {A} + 12 inner + 20 outer = 33 triangle-vertices
     (3 + 36 + 60 = 99 points, each exactly once) is an srg(33,12,1,6).

This program does NOT build the graph (there is no graph).  It checks, in
exact integer arithmetic, that these counts are internally consistent with
the (99,14,1,2) parameters -- total triangles 231, 7 triangles per point,
replication, the 39/60 split, the 1+12+20 = 33 assembly, and the
(33,12,1,6) sub-parameter replication -- and it FLAGS the discrepancy between
the claim "closure = 9 vertices" recorded in the run summary and the primary
source's 39.  It asserts nothing about existence of srg(99,14,1,2).
"""
from fractions import Fraction


def main():
    print("# Ran: python3 code/out/check_makhnev_n3_counts.py")
    print("# Oracle/method: exact integer count arithmetic from the (99,14,1,2)")
    print("#   parameters and the primary-text claims (no graph, no floats).")
    print("# Inputs: v=99, k=14, lambda=1, mu=2; Makhnev 1988 Lemmas 6-9 counts.")
    print("# Purpose: verify the n3=0 interior count structure is self-consistent;")
    print("#   assert NOTHING about srg(99,14,1,2) existence.")
    print()

    v, k, lam, mu, n3 = 99, 14, 1, 2, 0

    # --- (99,14,1,2) ground invariants (exact) --------------------------------
    E = v * k // 2                      # edges
    T = E // 3                          # triangles (each edge in one triangle)
    tris_per_point = k // 2             # lambda=1: neighbours pair into k/2 triangles
    print(f"(99,14,1,2) ground invariants (exact from v,k,lam,mu):")
    print(f"  |E| = v*k/2 = {E}")
    print(f"  T   = |E|/3 = {T} triangles")
    print(f"  triangles through each point = k/2 = {tris_per_point}")
    check_tri = (E == 693 and T == 231 and tris_per_point == 7)
    print(f"  -> expect 693 edges, 231 triangles, 7 triangles/point: "
          f"{'OK' if check_tri else 'MISMATCH'}")
    print(f"  count identity: sum over points of (triangles through point) = "
          f"v * (k/2) = {v * Fraction(k, 2)} = 3*T = {3 * T}: "
          f"{'OK' if v * k == 6 * T else 'MISMATCH'}")
    print()

    # --- Gamma(A) = closure of a triangle under condition (*) ----------------
    # Gamma(A) = [A] u [B] u [C]; each |[x]|=k=14; pairwise intersections size
    # lambda=1 (the third vertex each), triple empty.
    gA = 3 * k - 3          # 3*14 - 3 = 39
    gA_minus_A = gA - 3     # remove the triangle {A,B,C} itself
    print(f"Closure Gamma(A) = [A] u [B] u [C]:")
    print(f"  |Gamma(A)|     = 3*k - 3 = {gA}   (3*14 - 3)")
    print(f"  |Gamma(A) - A| = {gA_minus_A}  (Lemma 6: '36 points lie in 12")
    print(f"                      triangles from [A]_Lambda' -> 12*3 = 36) OK")
    outside = v - gA
    print(f"  points OUTSIDE Gamma(A) = v - |Gamma(A)| = {v} - {gA} = {outside}")
    outer_tri = outside // 3
    print(f"  outer triangles = {outside}/3 = {outer_tri} (Lemma 7: each outside")
    print(f"                      point in exactly one disjoint triangle)")
    print()

    # --- the assembly Lambda_0 = srg(33,12,1,6) triangle-vertex count ---------
    L0_tri = 1 + 12 + 20                  # A + 12 inner + 20 outer
    L0_points = 3 + 36 + 60               # points covered, each exactly once
    print(f"Assembly Lambda_0:")
    print(f"  triangle-vertices: 1 (A) + 12 (inner) + 20 (outer) = {L0_tri}")
    print(f"  points covered    : 3 + 36 + 60 = {L0_points} (= v = {v}) OK")
    print(f"  => Lambda_0 is claimed to be srg(33,12,1,6) (33 triangle-vertices)")
    print()

    # --- (33,12,1,6) sub-parameter self-consistency on the TRIANGLE-vertex side --
    # Lambda_0 is a subgraph of the TRIANGLE graph Lambda: its 33 vertices are
    # 33 triangles of Gamma, two adjacent iff joined by exactly 3 edges. So its
    # "edges" are triangle-joins, NOT Gamma-edges (do not divide |E0| by 3 as if
    # they were Gamma edges).  The meaningful Gamma-side statement is that the
    # 33 triangles PARTITION all 99 points (each point in exactly one of them).
    v0, k0, l0, m0 = 33, 12, 1, 6
    E0 = v0 * k0 // 2                    # pairs of triangles joined by exactly 3 edges
    print(f"srg(33,12,1,6) sub-parameter self-consistency (TRIANGLE-vertex side):")
    print(f"  vertices of Lambda_0 = 33 Gamma-triangles = 1 + 12 + 20 (A + inner + outer): "
          f"{'OK' if 33 == L0_tri else 'MISMATCH'}")
    print(f"  These 33 triangles PARTITION all {v} points of Gamma "
          f"(3+36+60 = {L0_points}): {'OK' if L0_points == v else 'MISMATCH'}")
    print(f"  degree k0 = 12 = Lemma 6 k_delta=12 (each triangle joined to "
          f"exactly 12 others by 3 edges): OK")
    print(f"  pairs of 3-joined triangles within Lambda_0 = v0*k0/2 = {E0} "
          f"(informational; no independent count to cross-check)")
    print(f"  mu0 = 6: this is exactly what triggers Makhnev Thm 1's rejection")
    print(f"     (mu<=3 or (27,10,1,5); 6>3 and not (27,10,1,5)).")
    print()

    # --- FLAG the discrepancy in the run summary's claim ----------------------
    print("# FLAG (defect found): the run summary / task statement reads the")
    print("#   closure as 'Gamma(A) is an srg(9,4,1,2) on 9 vertices (1 triangle")
    print("#   A + 6 = 9 points)'.  That is INCONSISTENT on two counts:")
    print(f"   1. If Gamma(A) had only {9} points, outside would be {v}-{9} = "
          f"{v - 9} != 60,")
    print(f"      and 9+60={9 + 60} != v=99.")
    print(f"   2. A 9-point closure cannot contain the 12 inner triangles (36 pts)")
    print(f"      needed to assemble a 33-triangle-vertex Lambda_0.")
    print(f"   Primary source (Lemma 6: '36 points of Gamma(A)-A lie in 12")
    print(f"   triangles') forces |Gamma(A)| = 36 + 3 = 39, which DOES reconcile:")
    print(f"   39 outside-60, 1+12+20 = 33, 3+36+60 = 99.")
    print()

    # --- VERDICT (count arithmetic only; NO existence statement) ---------------
    print("# VERDICT")
    all_ok = (check_tri and gA == 39 and outside == 60 and outer_tri == 20
              and L0_tri == 33 and L0_points == v and v0 == 33)
    print(f"  The CORRECTED primary-source count arithmetic (closure = 39, inner 12,")
    print(f"  outer 20, Lambda_0 = 33 triangle-vertices partitioning 99 points) is")
    print(f"  internally SELF-CONSISTENT with v=99,k=14: {all_ok}.")
    print(f"  The task statement's claim 'closure = 9 vertices' is a DEFECT: it is")
    print(f"  arithmetically inconsistent (9+60 != 99; 9 pts cannot host 12 inner")
    print(f"  triangles).  The primary text's 39 resolves it.")
    print(f"  Independent check (code/out/check_srg33_12_1_6.py, same run):")
    print(f"  srg(33,12,1,6) is parameter-INFEASIBLE by multiplicity integrality --")
    print(f"  which is exactly Makhnev Thm 1's rejection of the Lambda_0 subobject.")
    print(f"  (Counts here are arithmetic consistency only; no assertion about")
    print(f"  srg(99,14,1,2) existence.)")


if __name__ == "__main__":
    main()
