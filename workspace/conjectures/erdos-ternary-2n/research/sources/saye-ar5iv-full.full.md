<!-- source: https://ar5iv.labs.arxiv.org/html/2202.13256 | converted from HTML -->

[2202.13256] On two conjectures concerning theternary digits of powers of two

# On two conjectures concerning the
ternary digits of powers of two

Robert I. Saye Thanks: Lawrence Berkeley National Laboratory, Berkeley, California, USA ( rsaye@lbl.gov)

August 8, 2026

###### Abstract

Erdős conjectured that 1, 4, and 256 are the only powers of two whose ternary representations consist solely of 0 s and 1 s. Sloane conjectured that, except for { 2 0, 2 1, 2 2, 2 3, 2 4, 2 15 } \{2^{0},2^{1},2^{2},2^{3},2^{4},2^{15}\}, every other power of two has at least one 0 in its ternary representation. In this paper, numerical results are given in strong support of these conjectures. In particular, we verify both conjectures for all 2 n 2^{n} with n ≤ 2 ⋅ 3 45 ≈ 5.9 × 10 21 n\leq 2\cdot 3^{45}\approx 5.9\times 10^{21}. Our approach makes use of a simple recursive construction of numbers 2 n 2^{n} having prescribed patterns in their trailing ternary digits.

###### keywords

powers of two, ternary expansion, conjectures in number theory, exponential Diophantine equations

###### AMS

11A63 (primary), 11Y55, 11D61, 11Y50

## 1 Introduction

Circa 1978, Erdős [2] conjectured that the only powers of two which do not have a 2 anywhere in their ternary representation are the numbers 2 0 2^{0}, 2 2 2^{2}, and 2 8 2^{8}. Gupta [3] verified this to be the case for every 2 n 2^{n} with n ≤ 4373 n\leq 4373. Extending this bound, a numerical study of Vardi [6] confirmed no counterexamples exist for n ≤ 2 ⋅ 3 20 ≈ 7 × 10 9 n\leq 2\cdot 3^{20}\approx 7\times 10^{9}. The conjecture remains open; see the additional references and analysis of Lagarias [4]; see also Dimitrov & Howe [1] who study a closely related question and prove that the only powers of two whose ternary representation contains no 2 and at most twenty-five 1 s are the aforementioned numbers, 2 0 2^{0}, 2 2 2^{2}, and 2 8 2^{8}.

Similar in spirit, Sloane [5] conjectured that, except for the numbers { 2 0, 2 1, 2 2, 2 3, 2 4, 2 15 } \{2^{0},2^{1},2^{2},2^{3},2^{4},2^{15}\}, every other power of two contains a 0 somewhere in its ternary representation. Along the same lines, one may conjecture that, for all but finite number of cases, every power of two contains a 1 somewhere in its ternary representation—however, it is straightforward to show this is essentially equivalent to the conjecture of Erdős (the exceptional cases being replaced by 2 1 2^{1}, 2 3 2^{3}, and 2 9 2^{9}).

One may summarize all three conjectures to say that, except for a handful of small, easily predictable cases, every power of two has every possible digit somewhere in its ternary representation. Heuristically, we anticipate this to be the case because the ternary digits of powers of two are expected to be essentially random, implying that the chances of omitting a particular digit becomes vanishingly small as the overall digit count increases. However, this is far from a proof; indeed, the conjectures represent examples of exponential Diophantine equations for which few methods of attack have been found [1, 4].

In this note, numerical results are given in strong support of these conjectures. In particular, we significantly extend prior verification bounds and confirm that the ternary representation of 2 n 2^{n} contains every possible ternary digit, for all 16 ≤ n ≤ 2 ⋅ 3 45 ≈ 5.9 × 10 21 16\leq n\leq 2\cdot 3^{45}\approx 5.9\times 10^{21}. Our approach focuses on examining the trailing ternary digits of 2 n 2^{n}, which can be efficiently calculated even for massive exponents. In particular, we develop a recursive algorithm to construct numbers 2 n 2^{n} having prescribed patterns in their trailing ternary digits. For example, to find a potential counterexample to Erdős’s conjecture, one may directly enumerate in increasing order the numbers 2 n 2^{n} whose trailing digits are some combination of 0 s and 1 s. We note the recursive algorithm shares some aspects with the sieving method of Gupta [3].

As part of our analysis, we also compute the smallest power of two which has no 0 in the last k k digits of its ternary expansion, for k = 1, 2, … k=1,2,\ldots (and similarly for trailing digits excluding 1 and 2). The results agree very well with what one may expect supposing that the ternary digits of 2 n 2^{n} are essentially rolls of a three-sided die.

## 2 Notation

It is convenient to define a shorthand notation for the purposes of examining the trailing ternary digits of a number: for integers a, b a,b and k k a positive integer, a ≡ k b a\equiv_{k}b means a ≡ b ( mod 3 k) a\equiv b\pmod{3^{k}}. In addition, d k ​ ( a) d_{k}(a) is defined as the k th k^{\text{th}} ternary digit of a a, with d 1 ​ ( a) d_{1}(a) being the least significant digit: more precisely, if a = ∑ i = 0 n a i ​ 3 i a=\sum_{i=0}^{n}a_{i}3^{i} is the ternary representation of a a, then d k ​ ( a):= a k − 1 d_{k}(a):=a_{k-1}. As a final piece of notation, ( ⋯) 3 (\cdots)_{3} indicates the digits in the ternary expansion of a number, e.g., 2 8 = ( 100111) 3 2^{8}=(\texttt{100111})_{3}.

## 3 Method

A simple recursive construction of numbers 2 n 2^{n}, having prescribed patterns in their trailing ternary digits, is made possible via the results of the following lemma; its proof is elementary, and shares some aspects with the method of Gupta [3]. A self-contained proof of the lemma is deferred to the appendix so as to simplify the presentation.

###### Lemma 1.

For a positive integer k k, define 1 1 1 In fact, u k = φ ⁡ ( 3 k) u_{k}=\varphi(3^{k}), where φ \varphi is the Euler totient function; Euler’s theorem implies that a u k ≡ 1 ( mod 3 k) a^{u_{k}}\equiv 1\pmod{3^{k}} for any positive integer a a coprime to 3. u k:= 2 ⋅ 3 k − 1 u_{k}:=2\cdot 3^{k-1}. Then

1. (i)

u k u_{k} is the smallest positive integer such that 2 u k ≡ k 1 2^{u_{k}}\equiv_{k}1;

2. (ii)

if i, j ∈ ℕ i,j\in\mathbb{N} and 2 i ≡ k 2 j 2^{i}\equiv_{k}2^{j}, then i i and j j differ by a multiple of u k u_{k};

3. (iii)

if i, j ∈ ℕ i,j\in\mathbb{N}, the ( k + 1) st (k+1)^{\text{st}} ternary digit of 2 i ​ u k + j 2^{iu_{k}+j} is related to that of 2 j 2^{j} via

 | d k + 1 ​ ( 2 i ​ u k + j) ≡ d k + 1 ​ ( 2 j) + i ⋅ d 1 ​ ( 2 j) ( mod 3). d_{k+1}(2^{iu_{k}+j})\equiv d_{k+1}(2^{j})+i\cdot d_{1}(2^{j})\pmod{3}. |  |

We demonstrate the recursive construction process by means of a generic five-digit example. (There is nothing special about the digit count of five.) Suppose we have constructed a positive integer j < u 5 j<u_{5} such that the last five ternary digits of 2 j 2^{j} is a ​ b ​ c ​ d ​ e abcde, for some fixed a, …, d ∈ { 0, 1, 2 } a,\ldots,d\in\{\texttt{0},\texttt{1},\texttt{2}\} and e ∈ { 1, 2 } e\in\{\texttt{1},\texttt{2}\}. Then, for i ∈ { 0, 1, 2 } i\in\{0,1,2\}, we claim the numbers j i:= i ​ u 5 + j j_{i}:=iu_{5}+j are such that 2 j i 2^{j_{i}} are the smallest possible powers of two whose last six ternary digits are 0 ​ a ​ b ​ c ​ d ​ e \texttt{0}abcde, 1 ​ a ​ b ​ c ​ d ​ e \texttt{1}abcde, and 2 ​ a ​ b ​ c ​ d ​ e \texttt{2}abcde. (The order of these six-digit combinations, as i i iterates from 0 to 2, depends on e e.) To see why, note that:

- •

Applying part (i) of the lemma with k = 5 k=5, observe that 2 j i = ( 2 u 5) i 2 j ≡ 5 2 j 2^{j_{i}}=(2^{u_{5}})^{i}2^{j}\equiv_{5}2^{j}, and so the last five digits are preserved.

- •

For i i held fixed, suppose that ℓ \ell is a positive integer such that ℓ < j i \ell<j_{i} and 2 ℓ 2^{\ell} matches the last six digits of 2 j i 2^{j_{i}}. Then, by part (ii) of the lemma, j i − ℓ j_{i}-\ell is a positive multiple of u 6 u_{6}, but this is impossible because j i = i ​ u 5 + j < 2 ​ u 5 + u 5 = u 6 j_{i}=iu_{5}+j<2u_{5}+u_{5}=u_{6}. Therefore, no such ℓ \ell exists and consequently 2 j i 2^{j_{i}} is the smallest possible power of two whose trailing six digits match those of 2 j i 2^{j_{i}}.

- •

Last, by part (iii), the sixth ternary digit of 2 j i 2^{j_{i}} is equal (modulo 3) to the sixth digit of 2 j 2^{j} plus 0, 1, or 2 multiples of the last digit of 2 j 2^{j}. The latter digit is either 1 or − 1 -1 (modulo 3), which means that, irrespective of what the sixth digit of 2 j 2^{j} is, we shall always obtain some arrangement of 0 ​ a ​ b ​ c ​ d ​ e \texttt{0}abcde, 1 ​ a ​ b ​ c ​ d ​ e \texttt{1}abcde, and 2 ​ a ​ b ​ c ​ d ​ e \texttt{2}abcde for the last six digits of 2 j i 2^{j_{i}}, as i i iterates over { 0, 1, 2 } \{0,1,2\}.

In general, we observe that adding multiples of u k u_{k} to a number j < u k j<u_{k} allow us to explicitly construct powers of two whose last k k digits match those of 2 j 2^{j} and whose ( k + 1) st (k+1)^{\text{st}} digit is controlled; moreover, the recursive approach builds powers of two in the smallest order possible. As an example application, we may then use this approach to test the conjecture of Erdős, by starting with 2 0 2^{0} (whose least significant digit is 1), then generate the smallest powers of two whose trailing two digits are 01 and 11, then generate the smallest powers of two whose trailing three digits are 001, 101, 011, and 111, etc. If any of these powers of two end up containing solely 0 s and 1 s in their ternary representation, then a counterexample to the conjecture has been discovered (provided it is not one of the trivial cases, of course); moreover, any such counterexample must be constructable by this process.

An algorithm implementing this strategy is given in algorithm 1. The input is k k, the number of so-far-constructed trailing digits, the unit u k u_{k} defined by lemma 1 and its corresponding power of two, along with an integer j j and its corresponding power of two. The parameter χ \chi specifies the digit controlling the recursive construction: if χ = 2 \chi=2 (resp., χ = 0 \chi=0), then algorithm 1 generates powers of two whose trailing k k digits contain only 0 s and 1 s (resp., only 1 s and 2 s), thereby examining the conjecture of Erdős (resp., Sloane). In particular, for χ = 2 \chi=2, the recursion is initiated with the first power of two having k = 1 k=1 valid digits, i.e., 𝒢 2 ​ ( k = 1, u k = 2, 2 u k = 4, j = 0, 2 j = 1) {\mathcal{G}}_{2}(k=1,u_{k}=2,2^{u_{k}}=4,j=0,2^{j}=1). Meanwhile, for χ = 0 \chi=0, the recursion is initiated via two base cases, 𝒢 0 ​ ( k = 1, u k = 2, 2 u k = 4, j = 0, 2 j = 1) {\mathcal{G}}_{0}(k=1,u_{k}=2,2^{u_{k}}=4,j=0,2^{j}=1) and 𝒢 0 ​ ( k = 1, u k = 2, 2 u k = 4, j = 1, 2 j = 2) {\mathcal{G}}_{0}(k=1,u_{k}=2,2^{u_{k}}=4,j=1,2^{j}=2). By construction, the recursive algorithm is depth-first, with a maximum depth controlled by the user-defined parameter K K. A straightforward calculation shows that the total number of powers of two constructed by the recursive algorithm is Θ ⁡ ( 2 K) \Theta(2^{K}), and that every such power is less than 2 u K 2^{u_{K}}. On the other hand, the total number of powers of two less than 2 u K 2^{u_{K}} is Θ ⁡ ( 3 K) \Theta(3^{K}). In that sense, and in the context of testing the conjectures, the recursive approach exponentially reduces the search space versus the more elementary method of simply testing every power of two in increasing order.

Algorithm 1 𝒢 χ ​ ( k, u k, 2 u k, j, 2 j) {\mathcal{G}}_{\chi}(k,u_{k},2^{u_{k}},j,2^{j}).

1: Determine the first occurrence of digit χ \chi in 2 j 2^{j}.

2: if digit χ \chi not found and j > 16 j>16 then

3: output j j (nontrivial counterexample found)

4: if d k ​ ( 2 j) = χ d_{k}(2^{j})=\chi then

5: return

6: if k ≥ K k\geq K then

7: return

8: Compute 2 u k + 1 = ( 2 u k) 3 2^{u_{k+1}}=(2^{u_{k}})^{3}.

9: Execute 𝒢 χ ​ ( k + 1, 3 ​ u k, 2 u k + 1, j, 2 j) {\mathcal{G}}_{\chi}\bigl(k+1,3u_{k},2^{u_{k+1}},j,2^{j}\bigr).

10: Execute 𝒢 χ ​ ( k + 1, 3 ​ u k, 2 u k + 1, j + u k, 2 j ⋅ 2 u k) {\mathcal{G}}_{\chi}\bigl(k+1,3u_{k},2^{u_{k+1}},j+u_{k},2^{j}\cdot 2^{u_{k}}\bigr).

11: Execute 𝒢 χ ​ ( k + 1, 3 ​ u k, 2 u k + 1, j + 2 ​ u k, 2 j ⋅ ( 2 u k) 2) {\mathcal{G}}_{\chi}\bigl(k+1,3u_{k},2^{u_{k+1}},j+2u_{k},2^{j}\cdot(2^{u_{k}})^{2}\bigr).

Figure 1: Recursive generation of powers of two whose trailing k k ternary digits are required to satisfy particular conditions.

Our implementation of algorithm 1 includes the following aspects, mainly targeting its efficient execution:

- •

Except for line 1, all powers of two are computed in the cyclic group modulo 3 κ 3^{\kappa} for a fixed κ \kappa. In particular, we have used a tailor-made, fixed precision integer type representing a κ = 54 \kappa=54 digit ternary number. It is implemented as a three-digit number in base 3 18 3^{18}, with each such digit represented by a conventional 32-bit unsigned integer (`uint32_t`in C++). This approach is particularly fast at computing the cubes and multiplications in algorithm 1.

- •

On line 1, we first query for the occurrence of digit χ \chi in the fixed-precision 54-ternary digit number representing 2 j 2^{j}. (Here, the “first occurrence” essentially means min ⁡ { i: d i ​ ( j) = χ } \min\{i:d_{i}(j)=\chi\}.) Although sufficiently rare, it can happen that no such digit occurs in these 54 digits, in which case we switch over to an alternative algorithm. The alternative algorithm computes 2 j 2^{j} (via exponentiation-by-squaring) in the cycling group modulo 3 ℓ 3^{\ell} (using a similar ternary digit implementation as above), in progressively increasing lengths ℓ \ell, until χ \chi is found. In essence, this method tries to compute as few of the trailing digits of 2 j 2^{j} as possible in order to find the digit χ \chi; owing to the nature of the distribution of ternary digits of powers of two, it is usually the case that not many additional digits are required. (We note that a nontrivial counterexample to the conjectures would require ℓ \ell to reach the full digit length of the ternary representation of 2 j 2^{j}, however this circumstance never occurred in our computational study.)

## 4 Results

Running on a modest 64-core compute server for a few days, the computational study in this work applied a maximum recursion depth of K = 46 K=46. This corresponds to testing the conjectures of Erdős and Sloane against all powers 2 n 2^{n} such that n ≤ u 46 = 2 ⋅ 3 46 − 1 ≈ 5.9 × 10 21 n\leq u_{46}=2\cdot 3^{46-1}\approx 5.9\times 10^{21}. No counterexamples were found.

As part of this study, trailing digit count “record breakers” were tracked. Specifically, for χ ∈ { 0, 1, 2 } \chi\in\{0,1,2\}, we define ρ χ: ℕ → ℕ \rho_{\chi}:\mathbb{N}\to\mathbb{N} such that

 | ρ χ ​ ( k) = min ⁡ { n ∈ ℕ: 2 n ≥ 3 k − 1 and χ occurs nowhere in the last k ternary digits of 2 n }. \rho_{\chi}(k)=\min\{n\in\mathbb{N}:\text{$2^{n}\geq 3^{k-1}$ and $\chi$ occurs nowhere in the last $k$ ternary digits of $2^{n}$}\}. |  |

(In particular, the powers of two must have at least k k ternary digits, i.e., 2 n ≥ 3 k − 1 2^{n}\geq 3^{k-1}.) As an example, ρ 2 ​ ( 100) = 710982592620911336 \rho_{2}(100)=710982592620911336; the last 110 ternary digits of 2 710982592620911336 2^{710982592620911336} are

 |  | ( 0102020002100100100110011100110101011111010101010110010 ↩ CLOSE \displaystyle\bigl(\texttt{0102020002100100100110011100110101011111010101010110010}\raisebox{-5.38193pt}[0.0pt][0.0pt]{$\hookleftarrow$} |  |

 |  | OPEN 1000111001000101110010101011111010001110110001110111011) 3. \displaystyle\qquad\qquad\texttt{1000111001000101110010101011111010001110110001110111011}\bigr)_{3}. |  |

As another example, ρ 0 ​ ( 100) = 388128961376647359 \rho_{0}(100)=388128961376647359; the last 110 digits of 2 388128961376647359 2^{388128961376647359} are

 |  | ( 2021120020121121111112111222212121111112222122221212212 ↩ CLOSE \displaystyle\bigl(\texttt{2021120020121121111112111222212121111112222122221212212}\raisebox{-5.38193pt}[0.0pt][0.0pt]{$\hookleftarrow$} |  |

 |  | OPEN 1122111112221212212211111121221222222111222122221212122) 3. \displaystyle\qquad\qquad\texttt{1122111112221212212211111121221222222111222122221212122}\bigr)_{3}. |  |

It is straightforward to show that ρ 1 ​ ( k) = ρ 2 ​ ( k) + 1 \rho_{1}(k)=\rho_{2}(k)+1 for all k k. This is because 2 n 2^{n} ends in a sequence of 0 s and 2 s if and only if 2 n − 1 2^{n-1} ends in a sequence of 0 s and 1 s; moreover, the maximal number of trailing non- 1 digits (for the former) and non- 2 digits (for the latter) are exactly the same. As a result, we only consider ρ 0 \rho_{0} and ρ 2 \rho_{2} in the following analysis.

Figure 2: Plots of ρ 0 \rho_{0} (resp., ρ 2 \rho_{2}), defined as the smallest integer n n such that the digit 0 (resp., 2) occurs nowhere in the last k k ternary digits of 2 n 2^{n}. The arrow points to the instance where ρ 2 ​ ( k) = 201015414581294 \rho_{2}(k)=201015414581294 for all 82 ≤ k ≤ 98 82\leq k\leq 98.

fig. 2 plots ρ 0 \rho_{0} and ρ 2 \rho_{2} as a function of k k. We observe that ρ χ ​ ( k) \rho_{\chi}(k) grows approximately exponentially with k k. The longer horizontal steps correspond to the record breakers which have, roughly speaking, an uncharacteristic number of trailing non- χ \chi digits. One notable example is n = 201015414581294 n=201015414581294, which corresponds to the smallest power of two having 82 trailing non- 2 digits; this same example has, in fact, 98 trailing non- 2 digits. On the other hand, the total number of ternary digits of this power of two is about 1.3 × 10 14 1.3\times 10^{14}, far exceeding this 98 digit count.

Figure 3: Length of the ternary representation of 2 ρ χ 2^{\rho_{\chi}} (being approximately ρ χ ​ log 3 ​ 2 \rho_{\chi}\log_{3}2) as a fraction of the expected number of rolls of three-sided die required to generate an uninterrupted sequence of k k non- χ \chi digits (that average roll count being 3 ​ ( 3 2) k − 3 3(\tfrac{3}{2})^{k}-3).

An alternative analysis comes from the heuristic that the ternary digits of powers of two are essentially random. Imagining the digits of 2 n 2^{n}, reading from right-to-left, are a random number generator implementing the rolls of a three-sided die, we may ask how many rolls are necessary to generate an uninterrupted sequence of k k non- χ \chi digits. Each non- χ \chi digit has a probability of 2 3 \tfrac{2}{3}, and a routine calculation shows that we need, on average, 3 ​ ( 3 2) k − 3 \smash{3(\tfrac{3}{2})^{k}-3} total rolls to generate such a sequence. Of course, this is only an approximation given that the digits of powers of two are entirely deterministic; in particular, the first and last digit of 2 n 2^{n} is never a 0, so this heuristic analysis could be slightly improved. Nevertheless, the expected roll count serves as an estimate of what the total ternary digit length is expected to be. Corresponding to the record breakers, fig. 3 plots the ternary digit length of 2 n 2^{n} (being approximately n ​ log 3 ​ 2 n\log_{3}2) as a fraction of the expected roll count. We observe that, within zero to four of orders of magnitude, the digit counts of record breakers roughly match the expected roll count. The example of n = 201015414581294 n=201015414581294, mentioned in the previous paragraph, is uncharacteristic in the sense that for k = 98 k=98, we expect to require about 5.4 × 10 17 5.4\times 10^{17} rolls, yet 2 201015414581294 2^{201015414581294} has only 1.3 × 10 14 1.3\times 10^{14} ternary digits. Nevertheless, we observe in fig. 3 that there is no reasonable indication of finding any counterexamples to the conjectures: even the outlier record breakers are nowhere close to having the entire string of digits devoid of χ \chi.

## 5 Conclusions

By way of a recursive algorithm and extensive computation, we studied here the two conjectures of Erdős and Sloane. These conjectures essentially state that, except for small number of trivial cases, every power of two has all possible digits somewhere in its ternary representation. The recursive algorithm explicitly constructs powers of two such that their trailing digits satisfy a certain requirement, e.g., consist solely of 0 s and 1 s. Testing these conjectures against all powers 2 n 2^{n} with n ≤ 2 ⋅ 3 45 ≈ 5.9 × 10 21 n\leq 2\cdot 3^{45}\approx 5.9\times 10^{21}, no counterexamples were found. This extends an earlier study by Vardi [6] which considered n ≤ 2 ⋅ 3 20 ≈ 7 × 10 9 n\leq 2\cdot 3^{20}\approx 7\times 10^{9}. As part of the analysis, two “record breaking” integer sequences were defined: these record the smallest powers of two having no 0 (resp., 2) in the last k k digits of its ternary representation, for k = 1, 2, … k=1,2,\ldots. These integer sequences have been entered into the OEIS as [A351927][1] and [A351928][2].

## Appendix A Proof of Lemma 1

We begin with a few elementary observations:

1. (a)

Suppose the last k ≥ 2 k\geq 2 ternary digits of an integer x x are ( a ​ [0] k − 2 ​ 1) 3 (a[\texttt{0}]^{k-2}\texttt{1})_{3} with a ∈ { 0, 1, 2 } a\in\{\texttt{0},\texttt{1},\texttt{2}\}. (Here and in the following, the notation [⋅] ℓ [\,\cdot\,]^{\ell} means ℓ \ell copies of the indicated digit.) Then, for some exponent i ∈ ℕ i\in\mathbb{N}, we have that x i ≡ ( a ⋅ 3 k − 1 + 1) i ≡ a ​ i ⋅ 3 k − 1 + 1 ( mod 3 k) x^{i}\equiv(a\cdot 3^{k-1}+1)^{i}\equiv ai\cdot 3^{k-1}+1\pmod{3^{k}}, as shown by a simple application of the binomial theorem.

2. (b)

For a positive integer k k, the last k + 1 k+1 ternary digits of 2 u k 2^{u_{k}} are ( 1 ​ [0] k − 1 ​ 1) 3 (\texttt{1}[\texttt{0}]^{k-1}\texttt{1})_{3}. A simple inductive proof is as follows. Suppose the result holds for some k ≥ 2 k\geq 2 (the base cases with k ∈ { 1, 2 } k\in\{1,2\} are trivial to verify). Then 2 u k − 1 = ( 3 ​ x + 1) ​ 3 k 2^{u_{k}}-1=(3x+1)3^{k} for some non-negative integer x x, and so

 | 2 u k + 1 \displaystyle 2^{u_{k+1}} | = ( 2 u k) 3 = ( ( 2 u k − 1) + 1) 3 = ( 2 u k − 1) 3 + 3 ​ ( 2 u k − 1) 2 + 3 ​ ( 2 u k − 1) + 1 \displaystyle=(2^{u_{k}})^{3}=\bigl((2^{u_{k}}-1)+1\bigr)^{3}=(2^{u_{k}}-1)^{3}+3(2^{u_{k}}-1)^{2}+3(2^{u_{k}}-1)+1 |  |

 |  | ≡ 3 k + 1 + 1 ( mod 3 k + 2), \displaystyle\equiv 3^{k+1}+1\pmod{3^{k+2}}, |  |

as required.

Applying these observations, the proof of lemma 1 is as follows.

1. (i)

For k ≥ 2 k\geq 2, assume by induction that u k − 1 u_{k-1} is the smallest positive integer j j such that 2 j ≡ k − 1 1 2^{j}\equiv_{k-1}1, and let ℓ \ell be the smallest positive integer such that 2 ℓ ≡ k 1 2^{\ell}\equiv_{k}1. This number clearly satisfies 2 ℓ ≡ k − 1 1 2^{\ell}\equiv_{k-1}1, and so if ℓ = a ​ u k − 1 + b \ell=au_{k-1}+b with a, b ∈ ℕ a,b\in\mathbb{N} and 0 ≤ b < u k − 1 0\leq b<u_{k-1}, we see that ( 2 u k − 1) a 2 b ≡ k − 1 1 (2^{u_{k-1}})^{a}2^{b}\equiv_{k-1}1. This linear congruence problem has a unique solution, namely 2 b ≡ k − 1 1 2^{b}\equiv_{k-1}1, which by the inductive hypothesis implies b = 0 b=0, and so ℓ \ell is a multiple of u k − 1 u_{k-1}. By observation (b) above, ℓ \ell cannot equal u k − 1 u_{k-1} because the k th k^{\text{th}} digit of 2 u k − 1 2^{u_{k-1}} is 1. Further, ℓ \ell cannot equal 2 ​ u k − 1 2u_{k-1} because the square of 2 u k − 1 2^{u_{k-1}} has k th k^{\text{th}} digit equal to 2. The next multiple of u k − 1 u_{k-1} satisfies all requirements, and so ℓ = 3 ​ u k − 1 = u k \ell=3u_{k-1}=u_{k}, as claimed. (Note: the base cases of the inductive argument trivially hold by elementary computation.)

2. (ii)

Suppose i, j ∈ ℕ i,j\in\mathbb{N} are such that 2 i ≡ k 2 j 2^{i}\equiv_{k}2^{j}. Without loss of generality, suppose i < j i<j. Then 2 i ​ 2 j − i = 2 j 2^{i}2^{j-i}=2^{j} yields a linear congruence ( 2 i mod 3 k) ​ ( 2 j − i mod 3 k) ≡ 2 j ( mod 3 k) (2^{i}\bmod 3^{k})(2^{j-i}\bmod 3^{k})\equiv 2^{j}\pmod{3^{k}}. Since the gcd of ( 2 i mod 3 k) (2^{i}\bmod 3^{k}) and 3 k 3^{k} is unity, there is exactly one solution to the linear congruence, namely 2 j − i ≡ k 1 2^{j-i}\equiv_{k}1. Now suppose j − i = a ​ u k + b j-i=au_{k}+b with a, b ∈ ℕ a,b\in\mathbb{N} and 0 ≤ b < u k 0\leq b<u_{k}; since 2 j − i = ( 2 u k) a 2 b ≡ k 1 2^{j-i}=(2^{u_{k}})^{a}2^{b}\equiv_{k}1 and 2 u k ≡ k 1 2^{u_{k}}\equiv_{k}1, again by uniqueness of the linear congruence problem, we find that 2 b ≡ k 1 2^{b}\equiv_{k}1. Part (i) then implies b = 0 b=0, and so i i and j j differ by a multiple of u k u_{k}, as claimed.

3. (iii)

Suppose i, j ∈ ℕ i,j\in\mathbb{N}. Note that 2 i ​ u k + j ≡ k + 1 ( 2 u k mod 3 k + 1) i 2 j ( mod 3 k + 1) 2^{iu_{k}+j}\equiv_{k+1}(2^{u_{k}}\bmod 3^{k+1})^{i}2^{j}\pmod{3^{k+1}}. By observations (a) and (b), the trailing k + 1 k+1 ternary digits of the first term are ( [i mod 3] ​ [0] k − 1 ​ 1) 3 \bigl([i\bmod 3][\texttt{0}]^{k-1}\texttt{1}\bigr)_{3}. It is then a straightforward application of long multiplication to show that, modulo three, the ( k + 1) st (k+1)^{\text{st}} digit of 2 i ​ u k + j 2^{iu_{k}+j} is equal to the sum of the ( k + 1) st (k+1)^{\text{st}} digit of 2 j 2^{j} plus i i times the first digit of 2 j 2^{j}, as claimed.

## Acknowledgements

The author thanks an anonymous reviewer for suggesting refinements to the proof of lemma 1. Some computations used resources made possible by the Applied Mathematics Program of the U.S. Department of Energy Office of Advanced Scientific Computing Research under contract number DE-AC02-05CH11231.

## References

- [1] V. S. Dimitrov and E. W. Howe, Powers of 3 with few nonzero bits and a conjecture of Erdős, preprint, 2021. Available at [https://arxiv.org/abs/2105.06440][3].
- [2] P. Erdős, Some unconventional problems in number theory, Math. Mag., 52 (1979), pp. 67–70.
- [3] H. Gupta, Powers of 2 and sums of distinct powers of 3, Univ. Beograd Publ. Elecktrotehn, 602–633 (1978), pp. 151–158.
- [4] J. C. Lagarias, Ternary expansions of powers of 2, J. Lond. Math. Soc., 79 (2009), pp. 562–588, [https://doi.org/10.1112/jlms/jdn080][4].
- [5] N. J. A. Sloane, The persistence of a number, J. Recreational Math., 6 (1973), pp. 97–98.
- [6] I. Vardi, Computational Recreations in Mathematica, Addison Wesley Longman Publishing Co., Inc., 1991.

[◄][5][image: ar5iv homepage] [6]
[Feeling lucky?][7] [8]
[Conversion report][9]
[Report an issue][10]
[View original on arXiv][11] [►][12]


## Links

[1]: https://oeis.org/A351927
[2]: https://oeis.org/A351928
[3]: https://arxiv.org/abs/2105.06440
[4]: https://doi.org/10.1112/jlms/jdn080
[5]: /html/2202.13255
[6]: /
[7]: /feeling_lucky
[8]: /land_of_honey_and_milk
[9]: /log/2202.13256
[10]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2202.13256
[11]: https://arxiv.org/abs/2202.13256
[12]: /html/2202.13257
