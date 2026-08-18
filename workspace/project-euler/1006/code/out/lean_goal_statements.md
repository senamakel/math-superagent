# Reduction: Psi(k) ≡ mechanical second moment (mod M)

Status of the two statements the run depends on at the top level.

## G3 telescoped-v identity — stated, kernel checked, unproved
- File: `code/lean/pe1006_psi_G3_telescoped_v-1f79c34f.lean`
- `PE1006G3.telescoped_v_identity (a x : ℚ) (k : ℕ) (hk : 1 ≤ k) (ha0 : 0 < a) (ha1 : a < 1) :
    wordVal a x k = telescoped a x k`
- digit_j(x) = floor(x+(j+1)a) − floor(x+ja); wordVal = Σ_j digit_j·10^(k−1−j);
  telescoped = floor(x+ka) − 10^(k−1)·floor(x) + 9·Σ_{l=1}^{k−1} 10^(k−1−l)·floor(x+la).
- Kernel: compiles with 1 `sorry` (declared gap). Axioms: propext, sorryAx, Classical.choice, Quot.sound.
- Coefficient argument (exact, over ℤ, unconditional in a): floor(x+l·a) gets +10^(k−l)
  from j=l−1 and −10^(k−1−l) from j=l; l=0 → −10^(k−1); l=k → +1; 1≤l≤k−1 → 9·10^(k−1−l). ✓

## Overall goal — stated, kernel checked, unproved
- File: `code/lean/pe1006_psi_goal-1f79c34f.lean`
- `PE1006Goal.psi_mech_reduction (a) (ha0) (ha1) (k) (hk) :
    PsiMech a k % M = (Psi k : ℤ) % M`  — the problem's Psi (sum of squares of
  distinct length-k factors read as decimals) equals the mechanical second moment.
- `PE1006Goal.pe1006_answer_active : let k := 10^18; ∃ A < M, PsiMech 1 k % M = A`.
- PsiMech a k = Σ_{m=0}^{k} wordVal(a, arcMid a m, k)^2, arcMid via the three-distance
  partition cut points point m = fract(−m·a), m=0..k.
- Caveat: slope a is a parameter; the run uses Fibonacci ratios F(n)/F(n+2) (verified G2
  shell) or F(n−1)/F(n) with F(n)>>k (directive 2). The pe1006_answer_active uses a=1 as a
  placeholder slope — the actual slope for k=10^18 will be a Fibonacci approximant; the
  reduction is slope-parameterised and independent of the specific value.
- Kernel: compiles with 3 `sorry` (declared gaps). Axioms: propext, sorryAx, Classical.choice, Quot.sound.

Neither is `formalised` (both rest on declared `sorry` gaps); they are recorded statements
the run is working towards.
