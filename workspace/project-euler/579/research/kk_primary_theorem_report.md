# Primary Hurwitz quaternions and 3-icube enumeration — citable statements

Question: confirm, citable for a PE579 solution writeup, the "Kiss–Kutas
primary-Hurwitz-quaternion theorem" for enumerating 3-icubes. Bear in mind that
arXiv:1108.3113 (Kiss & Kutas, *Cubes of integral vectors in dimension four*)
is about m-icubes in **Z^4**. The 3-icube-in-**Z^3** enumeration lives in the
companion paper **arXiv:0806.3943** (Goswick, Kiss, Moussong, Simányi, *Sums of
squares and orthogonal integral vectors*), which 1108.3113 cites as [3]. Both
were fetched and read in full. Below, exact wordings with section/theorem
numbers and URLs.

## 1. Exact definition of a PRIMARY Hurwitz integral quaternion

From Kiss–Kutas, §2 "Integral quaternions" (arXiv:1108.3113):

> *Call a quaternion α primary if α ∈ S_1 and a_1 + a_i + a_j + a_k ≡ 1 (mod 4).*

where the quaternion is written α = a_1 + a_i i + a_j j + a_k k, K = {1,i,j,k},
and

> *S_g = { a_1 + a_i i + a_j j + a_k k ∈ L ∣ a_g ≢ a_h (mod 2) for every h ≠ g }*

so S_1 means the **real-part coefficient has parity opposite to the other
three**. Primary is used for quaternions of **odd norm**; the paper notes
"Obviously, if α ∈ S_1, then exactly one of α and −α is primary."

Useful supporting facts (§2): every γ ∈ E of odd norm has exactly one primary
left associate and one primary right associate (**Claim 2.6**); primaries form a
semigroup under multiplication. A quaternion is *primitive* if its four
coefficients are relatively prime. **Claim 2.7 (Jacobi):** the number of primary
primitive quaternions with odd norm N is h(N) = N·∏_p(1+1/p), over primes p | N.

URL: https://ar5iv.labs.arxiv.org/html/1108.3113

## 2. Every integral 3-icube, up to column permutation and sign changes, is an Euler matrix of a quaternion with edge length = its norm

This is the content of **arXiv:0806.3943**, not 1108.3113. Identify v∈R^3 with
the pure quaternion V(v) = v_1 i + v_2 j + v_3 k. For α = m+ni+pj+qk with
d = Norm(α) = m²+n²+p²+q², the **Euler matrix** E(α) = d·M(α) (Theorem 1.1,
M(α) the rotation matrix of x ↦ α x α⁻¹ on the pure quaternions) has columns
α i ᾱ, α j ᾱ, α k ᾱ, each of norm d² — so the three columns form a 3-icube of
**edge length d = Norm(α)**.

**Sárközy's Theorem 1.2** (restated in 0806.3943):

> *E(m+ni+pj+qk) is primitive iff gcd(m,n,p,q)=1 and d is odd. Every primitive
> 3-dimensional icube in Z^3 can be obtained from such an Euler matrix by
> permuting columns and changing the sign of the third column if necessary.*

**Corollary 3.9** (same paper): a primitive 3-icube (as the columns of a matrix
M) comes from a **Lipschitz** integral quaternion α by permuting columns of
E(α) and changing sign of the last column if needed. **Corollary 5.12**: for
*any* 3-icube (u,v,w) there is α ∈ E and d ∈ Z such that (u,v,w) and d·E(α)
differ only by column permutation and sign changes — i.e. edge length
= d·Norm(α), the integer edge length guaranteed by **Proposition 1.3**
(length of a 3-icube in Z^3 is an integer).

URL: https://ar5iv.labs.arxiv.org/html/0806.3943

## 3. Primitive (gcd=1) icubes ↔ primitive quaternions of odd norm

In 0806.3943 an icube is *primitive* if the gcd of all its entries is 1, and a
Lipschitz quaternion is *primitive* if its coefficients are relatively prime.
Sárközy's Theorem 1.2 states exactly the gcd(a,b,c,d)=1 **and** d odd
(respectively, type-(1) of **Theorem 3.3**). In 1108.3113 the primality↔primitive
correspondence is the dimension-4 statement **Theorem 4.2** — that a primitive
icube equals (γ ε_1 δ, …, γ ε_m δ) with γ, δ **both primary and primitive**, and
this representation is unique; a primitive 3-icube therefore corresponds to
primary quaternions γ, δ of odd norm (see also **Theorem 4.4** for m=2). Note this
is for **Z^4**, the 3-icube-in-Z^3 primitive statement being Sárközy Thm 1.2.

## Caveat for the writeup

The cleanest citable chain for the 3D enumeration is: Sárközy Thm 1.2 + Cor 3.9
+ Cor 5.12 of arXiv:0806.3943 (edge vectors = columns of E(α), primitive iff
gcd(α-coefficients)=1 and norm odd, normalization by column permutation / sign
/ column renaming). "Primary" pinning down the 24-fold symmetry is developed in
1108.3113 §2 (Claim 2.6). Do not cite 1108.3113 alone for the 3-icube theorem —
its edge cases (m≥3 uniqueness, Theorem 4.2) are set in dimension 4.
