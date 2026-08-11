# Goswick, Kiss, Moussong, Simányi — "Sums of squares and orthogonal integral vectors" (arXiv:0806.3943)

Source: https://arxiv.org/pdf/0806.3943 (full converted text in `research/icubes_goswick.md`).

**What it is.** The classification/counting paper for 2- and 3-dimensional icubes in Z^3
(a *3-icube* = three pairwise-orthogonal equal-norm nonzero integer vectors). This is the
governing source for enumerating lattice cubes — exactly the objects PE 579 counts.

## Euler matrix parametrization (the key construction)
Identify v∈R^3 with pure quaternion V(v)=v1 i + v2 j + v3 k. For α = m+ni+pj+qk,
d = Norm(α) = m²+n²+p²+q². **Theorem 1.1**: ρ(α): x↦α x ᾱ is the rotation
M(α)=(1/d)·[the 3×3 matrix below]; its columns α i ᾱ, α j ᾱ, α k ᾱ each have norm d²,
so the **columns of E(α)=d·M(α) form a 3-icube of edge length d = Norm(α)**. E(α) has
integer entries when α is a Hurwitz/Lipschitz integral quaternion. Explicitly
  u = (m²+n²−p²−q², 2(n p−m q), 2(m p+n q))
  v = (2(n p+m q), m²−n²+p²−q², 2(p q−m n))
  w = (2(m p−n q), 2(p q+m n), m²−n²−p²+q²).

## Sárközy's Theorem 1.2 (the enumeration core)
E(m+ni+pj+qk) is **primitive** (gcd of its 9 entries = 1) iff gcd(m,n,p,q)=1 **and**
d is odd. Every primitive 3-icube in Z^3 is obtained from such an Euler matrix by
permuting columns and (if orientation-reversing) changing the sign of the third column.
⇒ **Primitive 3-icubes ↔ primitive Lipschitz quaternions of odd norm**, modulo the
24-fold column-permutation/sign symmetry.

## Other statements used
- **Proposition 1.3**: for odd n, the edge length of an n-icube in Z^n is an integer
  (determinant argument). So every 3-icube has integer edge length.
- **Theorem 1.4**: a vector in Z^3 is contained in a 3-icube iff its length is an integer.
- **Theorem 3.3** (+ **Corollary 3.9**): E(α) is a primitive integral Euler matrix iff α
  is one of three types, the principal one being *type (1): primitive Lipschitz quaternion
  with odd norm*; the other two types reduce to type (1) by right-multiplying by a unit.
  Cor 3.9: a primitive icube (columns of M) equals a column-permutation/sign-adjusted E(α)
  with α a primitive Lipschitz quaternion.
- **Corollary 5.12**: any 3-icube (u,v,w) satisfies (u,v,w) ≅ columns of d·E(α) up to
  column permutation and sign changes, for some α∈E, d∈Z; edge length = d·Norm(α). This
  is the frame×(integer scale) decomposition used in `frame_method.py`.
- **Theorem 5.10**: exact count T(M) (multiplicative, Euler-factor g,h forms) of twin
  pairs of norm M — not directly needed for PE 579 but an independent counting formula.

## Hypotheses and applicability to PE 579
The theorems need only integer coordinates and hold for all of Z^3; all hypotheses are met
(a lattice cube IS a 3-icube). This source supplies the **parametrization the run uses**:
enumerate primitive frames by primitive Lipschitz quaternions of odd norm, scale by t.

## What it implies here
It reduces the C(n)/S(n) enumeration to (a) loop over primitive×odd-norm integer
quaternions with edge length ≤ n, (b) fix the 24-fold symmetry canonically, (c) apply the
frame×scale + Ehrhart summation already validated in `frame_method.py`. It does **not**
itself specify the canonical (primary) choice that kills the 24-fold symmetry — that is
Kiss–Kutas (arXiv:1108.3113), summarized separately.

## Caveat
The dimension-4 uniqueness theorems (used for the 24-fold pinning) live in 1108.3113; the
3D primitive↔quaternion correspondence is Sárközy Thm 1.2 / Cor 3.9 as stated here. Do not
cite 1108.3113 alone for the 3D theorem.
