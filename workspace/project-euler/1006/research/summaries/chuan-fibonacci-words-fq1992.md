# Chuan, "Fibonacci Words" (Fibonacci Quarterly 30:1, 1992, 68–76)

Source: https://www.fq.math.ca/Scanned/30-1/chuan.pdf
Full text: [[chuan-fibonacci-words-fq1992.full]]

## Conventions

Fibonacci sequence of words from initials x,y: w_1=x, w_2=y, w_{n+1}=w_nw_{n-1}
OR w_{n-1}w_n, order an arbitrary {0,1} label per step. ℱ_n = all n-th terms over
all labels. w_n^0 = all-labels-0 = Knuth's sequence w_3=xy, w_4=yxy, … (the
rabbit word; PE1006's S_n is its 0↔1 complement). ℓ(w_n^0)=F_{n-2}ℓ(x)+F_{n-1}ℓ(y).

## Established (elementary proofs, in text)

- Lemma 1: no xx, no yyy factor; integer letter-count/boundary constraints.
- Thm 3: reversal closure (labels flip).
- Thm 4 + Lemma 5: w_n^0 = v_n u_n (v,u symmetric); ℓ(w_n)=ℓ(w_{n-1})+ℓ(w_{n-2});
  closed forms ℓ(w_n^1)=(F_{n-4}+1)ℓ(x)+(F_{n-3}+1)ℓ(y),
  ℓ(v_n)=(F_{n-3}−1)ℓ(x)+(F_{n-2}−1)ℓ(y).
- Thm 6: every ℱ_n word is a cyclic shift of w_n^0 (shift amount k_p=Σ p_jℓ(w_{j+1}^0)).
- Thm 7: x,y distinct letters ⟹ n-th Fibonacci word ⟺ cyclic shift of w_n^0;
  ℱ_n = full rotation class of the standard word.
- Lemma 8: for each 0≤v≤F_n−1, v=Σ_j p_jℓ(w_{j+1}^0) has a {0,1} solution —
  proof vehicle for Thm 7, remark ⇒ "every positive integer = sum of distinct
  Fibonacci numbers, each ≤ once". (NOT a residue statement; that is Lemma 9.)
- Lemma 9: {jF_{n-1} mod F_n} and {jF_{n-2} mod F_n}, 0≤j<F_n, are complete
  residue systems mod F_n.
- Thm 11: q_n:=w_n^{0101…}: a_k=a iff k≡jt (mod F_n), t=F_{n-1} (n odd) /
  F_{n-2} (n even), 1≤j≤F_{n-2}. Letters sit at Fibonacci-residue positions.
- Cor 12: T^{js}q_n (s=F_{n-2} n odd / F_{n-1} n even), 0≤j<F_n, are F_n
  DISTINCT shifts; index-sum of a's advances by 1 mod F_n per j ⇒ |ℱ_n|=F_n
  (Thm 14, Cor 13 letter-counts).

## Bearing for PE1006

- Primary finite-word anchor for the ROTATION half of the factor structure:
  length-F_n standard word + its F_n distinct cyclic shifts = exactly the n-th
  stage Fibonacci words, letters at Fibonacci-residue positions. Supports
  (with the held Sturmian p(k)=k+1 and position theorems Sivasankar–Rama
  arXiv:2204.13977 Thm 7, arXiv:2207.04304 Lemma 2) directive 9 Claim 1's
  identification of the k+1 distinct length-k factors with contiguous windows
  of the standard word.
- Lemma 5's length recurrence = Fibonacci-block renormalisation basis for the
  O(log) collapse of the prefix sum of v_r² (~87 blocks at 10^18).

## NOT established here (do not cite it for)

- The exact window range r=F_n−k−1..F_n−1 of q_n q_n (directive 9 Claim 1's
  precise positions) — solver-verified vs mech_psi/brute, not literature.
- Occurrence location in the infinite word (paywalled Chuan–Ho TCS 2005,
  unobtainable, non-blocking); nothing about Ψ(k) or mod arithmetic.