# Kiss & Kutas — "Cubes of integral vectors in dimension four" (arXiv:1108.3113)

Source: https://ar5iv.labs.arxiv.org/html/1108.3113 (full text in `research/kk_full_actual.full.md`).

**What it is.** Classifies m-icubes (2≤m≤4) in Z^4 using Hurwitz quaternions, counts them
per edge norm, and proves unlimited extension. Its value to PE 579 is the **canonical
"primary" representative** that pins down the 24-fold symmetry so each cube is generated
exactly once; the 3D-icube classification itself is Goswick et al. (Sárközy Thm 1.2).

## Primary Hurwitz quaternion (§2)
Write α = a1 + ai i + aj j + ak k ∈ L (Lipschitz, integer coeffs). Define
S_g = {α ∈ L : a_g ≢ a_h (mod 2) for every h≠g in {1,i,j,k}}. For odd norm:
- **Claim 2.5**: every α∈L of odd norm lies in exactly one S_g; twins cannot share an S_g;
  products: S_g·S_h ⊆ S_{g*h} (Klein-group).
- **Definition (primary)**: α is *primary* if α ∈ S_1 **and** a1+ai+aj+ak ≡ 1 (mod 4).
  For α∈S_1 exactly one of α, −α is primary.
- **Claim 2.6**: every γ∈E of odd norm has exactly one primary left and one primary right
  associate; primaries form a semigroup; a unit ε satisfies ε α∈L iff ε∈Q={±1,±i,±j,±k}
  (Claim 2.6(3) — this is what makes the canonical choice well-defined and of size 24/Q).
- **Claim 2.7 (Jacobi)**: # primary *primitive* quaternions of odd norm N is
  h(N) = N·∏_{p|N}(1+1/p).

## Representation & uniqueness (Theorems 3.5 / 3.9 / 4.2)
- **Theorem 3.9**: if γ,δ∈L are primary and ε1=±1, ε2=±i, ε3=±j, ε4=±k, then
  (γ ε1 δ, …, γ εm δ) is an *orderly* m-icube in L with odd edge norm; conversely every
  orderly m-icube with odd edge norm arises this way.
- **Theorem 4.2** (m≥3): the representation with γ,δ primary **and primitive** is unique:
  γ1=γ2, δ1=δ2; the resulting icube is primitive iff both γ and δ are primitive. This is the
  readability/uniqueness guarantee needed later (though it is stated in Z^4, it is what the
  "primary" machinery provides; in Z^3 the primitive↔quaternion part is Sárközy).

## Counting (Theorem 1.3 / Corollary 4.3) — not needed for S(5000)
g_m(N)=f_m(N)/c_m is multiplicative; on odd prime powers k(≥1):
  g_1(p^k)=σ(p^k), g_3(p^k)=g_4(p^k)=g(p^k)=((k+1)p^k(p²−1)−2(p^{k+1}−1))/(p−1)²,
  g_2(p^k)=g(p^k) if p≡3(4), else (k+1)p^k; g_m(2^k)=3.
Cor 4.3: # orderly primitive m-icubes of odd norm N = 2^m Σ_{d|N} h(d)h(N/d). These give
independent closed-form counts to check a primitive-frame enumeration **if** one restricts to
odd norm frames (see caveats).

## Hypotheses & applicability
Primary pinning is developed for Z^4 and is exact there. For Z^3: every primitive 3-icube =
column perm + sign of E(α), α primitive Lipschitz of **odd norm**. The primary rule selects a
canonical representative of each 24-fold orbit. **Checks the run must still do** (flagged, not
settled here): (1) confirm the primary rule, applied to Z^3 frames, counts each primitive frame
exactly once (the run's `verify_primary.py` is the intended test: compare distinct frames from
all primitive odd-norm quats vs. distinct frames from primary primitive quats — must run);
(2) handle **even-norm** primitive frames, which Sárközy Thm 1.2 says do NOT arise from a
primitive Lipschitz quaternion of odd norm (Thm 3.3 type 2/3 cover even cases); the primary
definition assumes odd norm, so the even-norm primitive frames need the type-(2)/type-(3)
reduction of Goswick Thm 3.3, or an independent even-frame enumeration.

## What it implies here
Gives the canonical enumeration that makes the frame count grow poly(n) rather than (2n+1)³:
loop over bounded primary primitive quaternions, build E(α) once per orbit, then use the
already-validated frame×scale + Ehrhart/Faulhaber summation of `frame_method.py`/
`solution_power.py`. Two open points (even-norm frames; primary-rule exactness in 3D) must be
resolved before S(5000) can be trusted.
