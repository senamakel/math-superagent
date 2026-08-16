# Burrell & Yu, "Digit expansions of numbers in different bases" (2021)

**Source:** arXiv:1905.00832 (v3, 2021); published J. Number Theory 226 (2021) 284–306, DOI 10.1016/j.jnt.2021.01.003.
Full body text: `research/sources/burrell-yu-2021-digit-expansions-different-bases-body.full.md` (arXiv HTML v3).
Landing page: `research/sources/burrell-yu-2021-digit-expansions-different-bases.full.md`.

## What it establishes (all asserted-by-source, read from the arXiv full text here)

The paper is about **which integers are digit-{0,1} in several bases at once** — i.e. the discrete/Furstenberg-transversality line. It is NOT about the sequence `2^n`.

- **Theorem 1.2.** For each ε > 0 a constant C_ε: `#{k ∈ [1,n] : base-4 AND base-5 expansions of k use only {0,1}} ≤ C_ε n^ε`. (o(n^ε)-grade thin.) Adding base 3 gives **Corollary 1.3** — the base-3,4,5 case is also ≤ C_ε n^ε. This is directly about the folklore Conjecture 1.1 (only 0,1,82000 are {0,1}-digit in bases 3,4,5).
- **Theorem 1.4.** The base-3-AND-base-4 pair is **not** thin: `S(n) := #{k ∈ [4^n, 4^{n+1}-1] : {0,1} in bases 3 and 4} ≤ C_ε 4^{n(log2/log3 − 0.5 + ε)}`, and there are infinitely many n with S(n) > 0 (plus a lower-density 0.36907 statement on where S(n)=0). The exponent `log2/log3 − 1/2 ≈ 0.1309` is the `s − (k−1)` prediction of Conjecture 6.5 with `s = dim(base3) + dim(base4) = log2/log3 + 1/2 ≈ 1.1309 ∈ (1,2)`.
- **Conjecture 6.5** is the discrete analogue of Furstenberg transversality: for k multiplicatively-independent bases, with `A = ∩ A_{p_i}(D_i)` and `s = Σ dim A_{p_i}`, one has `#{A∩[1,N]} ≈ N^{s-(k-1)}` when `s ∈ (k−1,k)`, and `A` finite when `s < k−1`. Under Schanuel it would resolve Graham's ×1000 problem (`binom{2n}{n}` coprime to 105).
- The engine is a high-dimensional uniform Furstenberg-intersection theorem (their §2.6, from [24] Wu / [26] Shmerkin / [27]): if `Σ dim A_{p_i} < k−1` and the logs are Q-linearly independent, the box dimension of `∩(u_i A_{p_i}+v_i)` is 0. Main theorems need only k=2.

## What it implies for the Erdős ternary conjecture — and the limit

- The mechanism is the **discrete Furstenberg transversality / dimension-sum** principle: restricted-digit sets in multiplicatively independent bases intersect thinly according to `dim-sum minus (k−1)`.
- **Erdős is the thin-sequence special case**: `2^n = {0,1}-in-base-3` asks whether the *sequence* `2^n` (not all integers) is digit-{0,1} in base 3. Burrell–Yu bounds counts over *all* integers. So Theorems 1.2/1.4 and Corollary 1.3 are **density/transversality facts about integer sets**, and do **not** by themselves force any statement about which integers lie in the orbit `2^n`. This is exactly the "density trap" the problem statement warns about.
- Its value to the run: it fixes the correct discrete transversality vocabulary and confirms that the base-(3,4) analogue genuinely has infinitely many members (exponent > 0), while the base-(3,4,5) case is sub-polynomial. It does **not** provide the symbolic/3-adic-orbit invariant the run is hunting.

## Claims

```claim
id: BURRELL-YU-COR1.3
statement: For each ε>0 there is a constant C_ε with
  #{k ∈ [1,n] : k is digit-{0,1} in base 3, 4 AND 5} ≤ C_ε n^ε.
  (Theorem 1.2 is the base-(4,5) case; adding base 3 gives Corollary 1.3.)
hypotheses: none, unconditional.
holds-here: yes — a counting bound over all integers with restricted digits;
  background for the transversality line, not a statement about the orbit 2^n.
status: asserted-by-source
class: source
source: burrell-yu-2021-digit-expansions-different-bases-body.full.md (Thm 1.2, Cor 1.3)
bearing: fixes the discrete Furstenberg-transversality vocabulary; the (3,4,5)
  restricted-digit integer set is o(n^ε)-thin.
```

```claim
id: BURRELL-YU-THM1.4-BASE34
statement: S(n) := #{k∈[4^n,4^{n+1}-1] : k is digit-{0,1} in bases 3 and 4}
  ≤ C_ε 4^{n(log2/log3 − 0.5 + ε)} for each ε>0, and infinitely many n have
  S(n) > 0 (base 3 AND 4 is not thin, unlike base 4 AND 5).
hypotheses: none, unconditional.
holds-here: yes — background; contrast with the Erdős case (3 alone, over the
  thin sequence 2^n).
status: asserted-by-source
class: source
source: burrell-yu-2021-digit-expansions-different-bases-body.full.md (Thm 1.4)
bearing: the exponent log2/log3 − 1/2 = s − (k−1) for s = dim3 + dim4 in
  (1,2), consistent with Conjecture 6.5 discrete transversality.
```

```claim
id: BURRELL-YU-DENSITY-VS-THIN-SEQUENCE
statement: Burrell–Yu count all integers with restricted digits; their theorems
  do not bound which integers lie in the orbit {2^n}. Hence Theorems 1.2, 1.4,
  Corollary 1.3 do not reach the Erdős conjecture (the thin sequence 2^n).
hypotheses: n/a (a reading of the paper's scope).
holds-here: yes — this is exactly the "density trap" the problem statement warns
  the run about.
status: established (as a limitation)
class: reasoned
source: burrell-yu-2021-digit-expansions-different-bases-body.full.md
bearing: the run should not cite Burrell–Yu as evidence for or against Erdős;
  its value is the transversality vocabulary and the dim-sum−(k−1) exponent.
```

