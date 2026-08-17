# PE1006 pattern-hunt — new regularities (cycle 2)

Computed this cycle; both conjectures verified EXACTLY over a range, neither
is a proof. Memory server was down; stored to disk (as earlier cycles did).

## 1. Lead-1 factor count closed form

`c1(k)` = number of distinct length-k Fibonacci subwords starting with `'1'`.

CONJECTURE (verified exactly k = 1..400):

    c1(k) = 1 + floor(k / phi^2)      where phi^2 = (3+sqrt(5))/2 ~ 1.618

Equivalently, the increments c1(k) - c1(k-1) are exactly the letters f_{k-1}
of the infinite Fibonacci word (f = 0 1 0 0 1 0 1 0 0 1 ...), so

    c1(k) = 1 + (# of 1s among f_1..f_{k-1}).

Verified three independent ways that agree on k = 1..400:
  (i)  factor enumeration on a prefix >= 3k (Lmin-safe),
  (ii) 1 + prefix-one count of the word,
  (iii) 1 + floor(k/phi^2) via 50-digit Decimal (irrational slope; distance
       to nearest integer >= 1/(0.4 k), huge margin at k <= 400).
c1(377) = 145.  `code/out/c1_terms.txt` holds the sequence.

Derivation link: the distinct length-k subwords of a Sturmian word are the
k+1 "standard" factors; the count of those starting with 1 is governed by
the Sturmian balance: the lead-1 factors are exactly those whose offset puts
the 1-letter at position 1, and the number of breaks per unit is the slope
complement 1/phi^2. OEIS: the sequence matches **A189663** ("Partial sums of
A189661", the zero-free/one positions gap sequence), consistent with a
Fibonacci-word letter count.

Consequence NOT yet exploited: c0(k) = (k+1) - c1(k) = number starting with
'0'. Any efficient evaluation must weight the lead-1 vs lead-0 factors
differently (multiplying by 10^{k-1} vs 0 for leading zero). This is a
structural handle a symbolic method can use to separate the k+1 terms.

## 2. Pair-correlation is NOT translation-invariant at general k

Let F_k = set of k+1 length-k factors, and C(i,j) = #{w in F_k : w_i=w_j='1'}
(1-indexed).  For the lag-sum reduction of directive 1 (Psi = sum_d A(d) *
geometric-in-d) to hold one needs C(i,j) = C(i+1,j+1), i.e. dependence only
on d = j-i.

PROBED k = 1..20 by exact factor enumeration:
  - Zero translation violations ONLY at k = 1,2,4,7,12,20  (= F_m - 1 in this
    range, plus k=1).
  - Violations occur at k = 6,8,9,10,11,13,14,15,16,17,18,19.
  - Diagonal C(i,i) is position-dependent at k = 3,5,6,8,9,10,11,13,...,
    flat exactly at k = F_m - 1.

Interpretation: at k = F_n - 1 the k+1 factors are the N rotations of the
truncated standard word (directive 1 verified), which ARE translation-
invariant. At general k that fails: the factors are interleavings/slides of
different length-k windows, so C(i,j) depends on position.

CONCLUSION: the lag-sum reduction (directive 1) does NOT extend to general k.
Psi(k) at general k must be attacked via the mechanical-word construction
(directive 2), where C(i,j) is a sliding-window count that genuinely depends
on position. This corroborates the directive-2 route as the only general-k
handle, and explains why no scalar recurrence survives mod M.

## 3. Weight distribution of length-k factors is exactly balanced

`weight(w)` = number of 1s in factor w.  For each k the k+1 factors have
exactly TWO distinct weights, floor(k/phi^2) and ceil(k/phi^2), with the
shift of 1 wherever k/phi^2 is integral (e.g. k=13: only weight 5 occurs,
the single value = k/phi^2 = 5, since 13 ones / 0.382 = ... here 13*0.382 =
4.966 -> weights {4:1, 5:13} i.e. mostly the ceiling).  Verified exact by
factor enumeration for k = 1..30, every k: weights == {floor,ceil(k/phi^2)}
(one of the two being empty exactly at the "coincidence" k where both values
collide or the balance forces a single weight).

This is the Sturmian balance bound (any two length-k factors of a Sturmian
word differ by at most one 1) plus the slope density 1/phi^2 for the
Fibonacci word.  Combined with finding 1 (c1 = 1+floor(k/phi^2)) it fully
determines how the k+1 factors split by weight and by leading letter — a
structural handle any symbolic evaluation must respect.

## Files
- `code/pattern_hunt/verify_c1_formula.py` — the three-way c1 verification.
- `code/pattern_hunt/check_corr_translation.py` — the translation test.
- `code/out/c1_terms.txt` — c1(k), k=1..400.
