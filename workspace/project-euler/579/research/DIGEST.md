# Research digest — PE 579

Ordered by usefulness to the current goal (full O(1)-per-frame solution + S(5000)).

## 1. Goswick–Kiss–Moussong–Simányi, arXiv:0806.3943 — the enumeration engine
The governing 3D classification. Every lattice cube is a 3-icube (three pairwise-orthogonal
equal-norm integer vectors). **Euler matrix E(α)=d·M(α)**, α=m+ni+pj+qk, d=Norm(α), has
columns forming a 3-icube of edge length d. **Sárközy Thm 1.2**: E(α) primitive iff
gcd(m,n,p,q)=1 and d odd; every primitive 3-icube is a column-permutation/sign of such E(α).
**Cor 5.12**: every 3-icube = frame×integer scale of E(α). This is exactly what
`frame_method.py` already uses, and it is how to enumerate primitive frames without pairing
vectors. Note Sárközy covers **odd-norm** primitive quats; even-norm primitive frames
(Goswick Thm 3.3 types 2,3) need separate handling.
[note](goswick_0806.3943.md)

## 2. Kiss–Kutas, arXiv:1108.3113 — canonical (primary) pinning of the 24-fold symmetry
Primitive → unique quaternion up to the unit group. A quaternion is **primary** if the real
part has parity opposite to the other three and a1+ai+aj+ak≡1 (mod 4). Claim 2.6: exactly
one primary left/right associate; unit ∈Q iff it preserves integrality. **Thm 4.2** (m≥3):
representation (γ ε1 δ,…,γ εm δ) with γ,δ primary+primitive is unique. This is the
canonical representative so each frame is generated once. Caveat: developed in Z^4; for the
3D primitive frames, primary-rule exactness is checked by `verify_primary.py` (must run).
[note](kiss_kutas_1108.3113.md)

## 3. Ionascu — Ehrhart polynomial of a cube (the point-count half of S)
**Thm 3.1**: L(t)=ℓ³t³+ℓ(d1+d2+d3)t²+(d1+d2+d3)t+1 = pts(t) for the t-scaled cube. Reproduces
cubes A (64) and B (40) exactly. Combined with the run's box-fit translation polynomial
T(t)=(n+1−tA)(n+1−tB)(n+1−tC), the S-summand pts(t)·T(t) is degree 6 in t → Faulhaber sums.
[note](ehrhart_cubes.md)

## 4. Horváth, arXiv:2203.01901 — independent corroboration (cross products)
Theorem 1 / Theorem 2 give the unique Γ(v,d)=k·Γ(v,d) decomposition of cubic sublattices by
an elementary route. Confirms the frame×scale structure and coordinate spans. Does not give
a frame-counting formula.
[note](cubic_sublattices.md)

## 5. Run's own theory synthesis
`pe579_lattice_cube_theory.md` assembles enumeration + Ehrhart + power-sum strategy; the
derivation it proposes is already validated in `solution_power.py` (per-frame O(1)). The
only unimplemented piece is the canonical primitive-frame enumeration at n=5000 scale.

## Gaps / must-run checks
- **`verify_primary.py`**: confirm primary primitive odd-norm quats generate each primitive
  frame exactly once (frames_primary[N]==frames_all[N]).
- **Even-norm primitive frames**: primary/odd-norm machinery does not cover them; original
  `frame_method.py` handled all frames direct-vector. The canonical enumeration must include
  even-norm frames (Goswick Thm 3.3 types 2,3 or an even-frame enumeration) or S(5000) will
  be incomplete.
- The full pipeline (enumeration + Faulhaber) must be run to produce S(5000) mod 10^9 and be
  cross-verified by an independent route.
