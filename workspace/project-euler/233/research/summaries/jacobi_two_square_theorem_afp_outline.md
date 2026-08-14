> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/jacobi_two_square_theorem_afp_outline.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://isa-afp.org/browser_info/current/AFP/Sum_Of_Squares_Count/outline.pdf | converted from PDF -->

The Sum-of-Squares Function and Jacobi’s
Two-Square Theorem

Manuel Eberl

February 6, 2026

Abstract

This entry defines the sum-of-squares function rk(n), which counts
the number of ways to write a natural number n as a sum of k squares
of integers. Signs and permutations of these integers are taken into
account, such that e.g. 1
2 + 22, 2
2 + 12, and (−1)
2 + 22 are all different
decompositions of 5.
Using this, I then formalise the main result: Jacobi’s two-square
theorem, which states that for n > 0 we have r2(n) = 4(d1(n) − d3(n)),
where di(n) denotes the number of divisors m of n such that m =
i (mod 4).
Corollaries include the identities r2(2n) = r2(n) and r2(p
2n) =
r2(n) if p = 3 (mod 4) and the well-known theorem that r2(n) = 0 iff
n has a prime factor p of odd multiplicity with p = 3 (mod 4).

Contents

1 Sum-of-square decompositions and Jacobi’s two-squares The-
orem 2
1.1 Auxiliary material . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Decompositions into squares of integers . . . . . . . . . . . . 2
1.3 Decompositions into squares of positive integers . . . . . . . . 4
1.4 Decompositions into two squares . . . . . . . . . . . . . . . . 7
1.4.1 Gaussian integers on a circle . . . . . . . . . . . . . . 7
1.4.2 The number of divisors in a given congruence class . . 10
1.4.3 Jacobi’s two-square Theorem . . . . . . . . . . . . . . 12

1

1 Sum-of-square decompositions and Jacobi’s two-
squares Theorem

theory Sum_Of_Squares_Count
imports
"HOL-Library.Discrete_Functions"
"HOL-Library.FuncSet"
"Gaussian_Integers.Gaussian_Integers"
"Dirichlet_Series.Multiplicative_Function"
"List-Index.List_Index"
begin

1.1 Auxiliary material

lemma is_square_conv_sqrt: "is_square n ←→ floor_sqrt n ^ 2 = n"
⟨proof ⟩

lemma sum_replicate_mset_count_eq: "(∑ x∈set_mset X. replicate_mset
(count X x) x) = X"
⟨proof ⟩

lemma coprime_crossproduct_strong:
fixes a b c d :: "'a :: semiring_gcd"
assumes "coprime a d" "coprime b c"
shows "normalize (a * b) = normalize (c * d) ←→
normalize a = normalize c ∧ normalize b = normalize d"
⟨proof ⟩

lemma divisor_coprime_product_decomp_normalize:
fixes d n1 n2 :: "'a :: factorial_semiring_gcd"
assumes "d dvd n1 * n2" "coprime n1 n2"
shows "normalize d = normalize (gcd d n1 * gcd d n2)"
⟨proof ⟩

lemma divisor_coprime_product_decomp:
fixes d n1 n2 :: nat
assumes "d dvd n1 * n2" "coprime n1 n2"
shows "d = gcd d n1 * gcd d n2"
⟨proof ⟩

1.2 Decompositions into squares of integers

The following definition gives the set of all the different ways to decompose
a natural number n into a sum of k squares of integers. The signs and
permutation of these integers is taken into account, i.e. 12 + 22, 22 + 12, and
12 + (−2)2 are all counted as different decompositions of 5.

definition sos_decomps :: "nat ⇒ nat ⇒ int list set" where
"sos_decomps k n = {xs. length xs = k ∧ int n = (
∑ x←xs. x ^ 2)}"

2

The following function that counts the number of such decompositions is
known as the “sum-of-squares function” in the literature, and frequently
denoted with rk(n).

definition count_sos :: "nat ⇒ nat ⇒ nat" where
"count_sos k n = card (sos_decomps k n)"

lemma finite_sos_decomps [simp, intro]: "finite (sos_decomps k n)"
⟨proof ⟩

lemma sos_decomps_0_right [simp]: "sos_decomps k 0 = {replicate k 0}"
⟨proof ⟩

lemma sos_decomps_0: "sos_decomps 0 n = (if n = 0 then {[]} else {})"
⟨proof ⟩

lemma sos_decomps_1:
"sos_decomps (Suc 0) n = (if is_square n then {[floor_sqrt n], [-floor_sqrt
n]} else {})"
(is "?lhs = ?rhs")
⟨proof ⟩

lemma bij_betw_sos_decomps_2: "bij_betw (λ(x,y). [x,y]) {(i,j). i
2 +
j2 = int n} (sos_decomps 2 n)"
⟨proof ⟩

lemma sos_decomps_Suc:
"sos_decomps (Suc k) n =
(#) 0 ` sos_decomps k n ∪
(
⋃ i∈{1..floor_sqrt n}. ⋃ xs∈sos_decomps k (n - i ^ 2). {int i #
xs, (-int i) # xs})"
(is "?A = ?B ∪ ?C")
⟨proof ⟩

lemma count_sos_0_right [simp]: "count_sos k 0 = 1"
⟨proof ⟩


*[excerpt ends; 16738 characters not shown — see `research/sources/jacobi_two_square_theorem_afp_outline.full.md`]*
