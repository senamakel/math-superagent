<!-- source: https://arxiv.org/html/2605.23601v1 | converted from HTML -->

Congruence Classes of Supporting the Erdös-Straus

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2605.23601v1 [math.NT] 22 May 2026

# Congruence Classes of Supporting the Erdös-Straus

Conjecture I: Tame Solutions 1 1 1 2010 Mathematical Subject Classification. Primary 11D68: Secondary 11D85, 11A67, 11B75

Xiaoping Xu

HLM, Institute of Mathematics, Academy of Mathematics & System Sciences

Chinese Academy of Sciences, Beijing 100190, P.R. China

& School of Mathematics, University of Chinese Academy of Sciences,

Beijing 100049, P.R. China

###### Abstract

In 1948, Erdös and Straus formulated a conjecture : for any positive integer n > 2 n>2, there exist positive integers n 1, n 2 n_{1},n_{2} and n 3 n_{3} such that

 | 4 n = 1 n 1 + 1 n 2 + 1 n 3, \frac{4}{n}=\frac{1}{n_{1}}+\frac{1}{n_{2}}+\frac{1}{n_{3}}, |  |

which is still open. It is known that one only needs to prove the conjecture for any prime number n n such that n ≡ 1 ​ ( mod ​ 24) n\equiv 1\;(\mbox{mod}\;24). If n = 24 ​ m + 1 n=24m+1 and n 1 ≤ n 2, n 3 n_{1}\leq n_{2},n_{3}, then n 1 = 6 ​ m + k n_{1}=6m+k with 1 ≤ k ≤ 12 ​ m 1\leq k\leq 12m. A solution ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) of the above equation is called a tame solution if n 2 n_{2} and n 3 n_{3} are factors of ( 6 ​ m + k) ​ ( 24 ​ m + 1) (6m+k)(24m+1). We call n = 24 ​ m + 1 n=24m+1 wild if it does not have any tame solution. Computer calculation shows that there are only nine wild primes among the 7185 primes of the form 24 ​ m + 1 24m+1 with m ≤ 30000 m\leq 30000. In this paper, we derive the tame solutions of the above equation for the integers of the form 24 ​ m + 1 24m+1 with m m parameterized by certain congruence classes. They cover the solvability of all the 586 tame primes among the 591 primes of the form 24 ​ m + 1 24m+1 with m ≤ 2000 m\leq 2000.

Keywords: Erdös-Straus conjecture; Egyptian fraction; congruence class; tame solution; wild solution; wild prime.

## 1 Introduction

Ancient Egyptians used sums of unit fractions (whose numerators are 1) to express fractions due to their ways of distributing food. For instance, 5 / 8 5/8 was interpreted by ancient Egyptians as distributing five pancakes fairly among eight people. They cut first four pancakes into halves and then cut the last one into eight equal pieces. So each person got the same share: 1 / 2 + 1 / 8 1/2+1/8 pancakes. This amazingly interpreted the mathematical equation

 | 5 8 = 1 2 + 1 8. \frac{5}{8}=\frac{1}{2}+\frac{1}{8}. |  | (1.1) |

So an Egyptian fraction is a sum of distinct unit fractions. By repeatedly applying the simple fact

 | 1 k = 1 k + 1 + 1 k ⁡ ( k + 1), \frac{1}{k}=\frac{1}{k+1}+\frac{1}{k(k+1)}, |  | (1.2) |

one can easily prove that any fraction is a Egyptian fraction. However, it is very difficult to determine if a fraction can be expressed as a sum of fixed number of unit fractions (cf. [3] for an excellent exposition and extensive references). For example, it is difficult to know if a fraction can be written as a sum of two unit fractions (e.g., cf. [5, 6, 7, 9, 15]). In 1948, Erdös and Straus formulated a conjecture : for any positive integer n > 2 n>2, there exist positive integers n 1, n 2 n_{1},n_{2} and n 3 n_{3} such that

 | 4 n = 1 n 1 + 1 n 2 + 1 n 3, \frac{4}{n}=\frac{1}{n_{1}}+\frac{1}{n_{2}}+\frac{1}{n_{3}}, |  | (1.3) |

which is still open up to now. For each n n, the number of solution can go to infinity as n n does. Elscholtz and Tao [3] found excellent bounds for it.

Mordell [14] proved that the conjecture holds for positive integers in 834 congruence classes modulo 840. Terzi [22] used computer to verify that the conjecture holds for positive integers in the congruence classes modulo 120120 except 198 classes. Kotsireas [11] verified the conjecture for every n < 10 10 n<10^{10}. There are other interesting partial results on the conjecture or related works (e.g., cf. [1, 2, 4, 10, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]).

It is known that one only needs to prove the conjecture for any prime number n n such that n ≡ 1 ​ ( mod ​ 24) n\equiv 1\;(\mbox{mod}\;24), which will be reviewed in next section. Suppose that n = 24 ​ m + 1 n=24m+1 and n 1 ≤ n 2, n 3 n_{1}\leq n_{2},n_{3}. Then n 1 = 6 ​ m + k n_{1}=6m+k with 1 ≤ k ≤ 12 ​ m 1\leq k\leq 12m and

 | 4 24 ​ m + 1 = 1 6 ​ m + k + 4 ​ k − 1 ( 6 ​ m + k) ​ ( 24 ​ m + 1). \frac{4}{24m+1}=\frac{1}{6m+k}+\frac{4k-1}{(6m+k)(24m+1)}. |  | (1.4) |

If

 | 1 n 2 = ℑ 1 ( 6 ​ m + k) ​ ( 24 ​ m + 1) and 1 n 2 = ℑ 2 ( 6 ​ m + k) ​ ( 24 ​ m + 1) \frac{1}{n_{2}}=\frac{\Im_{1}}{(6m+k)(24m+1)}\quad\mbox{and}\quad\frac{1}{n_{2}}=\frac{\Im_{2}}{(6m+k)(24m+1)} |  | (1.5) |

for some positive integers ℑ 1 \Im_{1} and ℑ 2 \Im_{2} such that ℑ 1 + ℑ 2 = 4 ​ k − 1 \Im_{1}+\Im_{2}=4k-1, we call the triple ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) a tame solution of the Erdös-Straus equation (1.3) for the positive integer n = 24 ​ m + 1 n=24m+1. Moreover, we call n = 24 ​ m + 1 n=24m+1 wild if it does not have any tame solution. Computer calculation shows that there are only nine wild primes among the 7185 primes of the form 24 ​ m + 1 24m+1 with m ≤ 30000 m\leq 30000. Furthermore, we call ℑ 1 \Im_{1} and ℑ 2 \Im_{2} the numerator summands for the tame solution ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}).

A key difficulty of solving the conjecture is that we so far do not have enough knowledge on the exact solutions of the Erdös-Straus equation. Computer shows that there are infinitely many ways of constructing solutions. However, the conjecture is about the existence of the solutions for each positive integer n > 2 n>2 (i.e., one solution is enough). Like the minimal models in birational geometry or generators in an algebra, there may be finite ways of constructing solutions which cover the solvability for all n n. The goal of this paper and next [25] is to find finite families of exact solutions that may lead to a final solution of the conjecture. The paper is organized as follows.

In Section 2, we present some basic known facts about the Erdös-Straus equation and prove that a tame solution ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) of the equation for a prime n = 24 ​ m + 1 n=24m+1 must satisfy (1.4), (1.5) and ℑ 1, ℑ 2 \Im_{1},\Im_{2} are factors of 6 ​ m + k 6m+k. In Section 3, we completely solve the equation for the tame solutions under the condition ℑ 2 ≤ 6 \Im_{2}\leq 6. In Section 3, we primarily find the complete tame solutions of the equation for a prime of the form 24 ​ m + 1 24m+1 with ℑ 1 = 2 ​ ( 2 ​ j + 1) \Im_{1}=2(2j+1) and ℑ 2 = 4 ​ ℓ + 1 \Im_{2}=4\ell+1 such that 2 ​ j + 1 2j+1 and ℑ 2 > 5 \Im_{2}>5 are odd primes. Later we slightly relax the condition in order to cover the solvability of all the 586 tame primes among the 591 primes of the form 24 ​ m + 1 24m+1 with m ≤ 2000 m\leq 2000. In Section 5, we do the same thing for a prime of the form 24 ​ m + 1 24m+1 with ℑ 1 = 4 ​ j \Im_{1}=4j and ℑ 2 = 4 ​ ℓ + 3 \Im_{2}=4\ell+3 such that j j and ℑ 2 > 5 \Im_{2}>5 are odd primes. and slightly relax the condition. In fact, ( ℑ 1, ℑ 2) (\Im_{1},\Im_{2}) is either in the form ( 2 ​ ( 2 ​ j + 1), 4 ​ ℓ + 1) (2(2j+1),4\ell+1) or ( 4 ​ j, 4 ​ ℓ + 3) (4j,4\ell+3) due to the fact ℑ 1 + ℑ 2 = 4 ​ k − 1 \Im_{1}+\Im_{2}=4k-1. Our computer calculated list of the exact solutions of the Erdös-Straus equation for the primes of the form 24 ​ m + 1 24m+1 with m ≤ 2000 m\leq 2000 shows that we need the tame solutions with powers of 2 2 as a numerator summand in order to cover the complete solvability. In Section 6, we use simple 2-adic analysis to find thirteen families of such solutions. It is reasonable to speculate that our solutions may cover the solvability for all the tame primes of the form 24 ​ m + 1 24m+1.

## 2 Basics of the Erdös-Straus Equation

In this section, we list some basic known facts about the Erdös-Straus equation (1.3). Then we prove that the numerator summands of the tame solution of the equation for a prime n = 24 ​ m + 1 n=24m+1 must be factors of 6 ​ m + k 6m+k.

As shown in [20], a simple calculation

 | 4 2 ​ k = 1 k + 1 k + 1 + 1 k ⁡ ( k + 1), \frac{4}{2k}=\frac{1}{k}+\frac{1}{k+1}+\frac{1}{k(k+1)}, |  | (2.1) |

 | 4 3 ​ k = 1 3 ​ k + 1 k + 1 + 1 k ⁡ ( k + 1), \frac{4}{3k}=\frac{1}{3k}+\frac{1}{k+1}+\frac{1}{k(k+1)}, |  | (2.2) |

and

 | 4 3 ​ k − 1 = 1 3 ​ k − 1 + 1 k + 1 k ⁡ ( 3 ​ k − 1) \frac{4}{3k-1}=\frac{1}{3k-1}+\frac{1}{k}+\frac{1}{k(3k-1)} |  | (2.3) |

shows that Erdös-Straus equation holds for all n n except those n ≡ 1 ​ ( mod ​ 6) n\equiv 1\;(\mbox{mod}\;6). Throughout this paper, we denote by ℕ \mathbb{N} the set of nonnegative integers. So we only need to solve (1.3) for n ∈ 1 + 6 ​ ℕ n\in 1+6\mathbb{N}. Further calculations

 | 4 4 ​ k − 1 = 1 k + 1 k ⁡ ( 4 ​ k − 1) + 1 + 1 k ⁡ ( 4 ​ k − 1) ​ ( k ⁡ ( 4 ​ k − 1) + 1) \frac{4}{4k-1}=\frac{1}{k}+\frac{1}{k(4k-1)+1}+\frac{1}{k(4k-1)(k(4k-1)+1)} |  | (2.4) |

and

 | 4 24 ​ k − 11 = 1 6 ​ k − 2 + 1 ( 3 ​ k − 1) ​ ( 24 ​ k − 11) + 1 ( 6 ​ k − 2) ​ ( 24 ​ k − 11) \frac{4}{24k-11}=\frac{1}{6k-2}+\frac{1}{(3k-1)(24k-11)}+\frac{1}{(6k-2)(24k-11)} |  | (2.5) |

show that Erdös-Straus equation holds for all n n except those n ≡ 1 ​ ( mod ​ 24) n\equiv 1\;(\mbox{mod}\;24). This fact is known to some people (e.g., cf. [13]). If ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) is a solution of the Erdös-Straus equation (1.3) for n n and k k is another positive integer, then

 | 4 n ​ k = 1 n 1 ​ k + 1 n 2 ​ k + 1 n 3 ​ k \frac{4}{nk}=\frac{1}{n_{1}k}+\frac{1}{n_{2}k}+\frac{1}{n_{3}k} |  | (2.6) |

naturally holds. So it is enough to solve the equation for any prime number n n. From now on, we always assume that

 | n = 24 ​ m + 1 is a prime and ​ m ∈ ℕ. n=24m+1\quad\mbox{is a prime and}\;m\in\mathbb{N}. |  | (2.7) |

Moreover, we can assume a tame solution ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) of (1.3) for n n satisfying n 1 ≤ n 2, n 3 n_{1}\leq n_{2},n_{3}. Then we have

 | 4 3 ​ ( 24 ​ m + 1) ≤ 1 n 1 ≤ 4 24 ​ m + 1. \frac{4}{3(24m+1)}\leq\frac{1}{n_{1}}\leq\frac{4}{24m+1}. |  | (2.8) |

Equivalently

 | 6 ​ m + 1 ≤ n 1 ≤ 18 ​ m. 6m+1\leq n_{1}\leq 18m. |  | (2.9) |

Thus

 | n 1 = 6 ​ m + k ​ with ​ 1 ≤ k ≤ 12 ​ m. n_{1}=6m+k\;\;\mbox{with}\;\;1\leq k\leq 12m. |  | (2.10) |

In particular,

 | 4 24 ​ m + 1 = 1 6 ​ m + k + 4 ​ k − 1 ( 6 ​ m + k) ​ ( 24 ​ m + 1) \frac{4}{24m+1}=\frac{1}{6m+k}+\frac{4k-1}{(6m+k)(24m+1)} |  | (2.11) |

and

 | 1 n 2 = ℑ 1 ( 6 ​ m + k) ​ ( 24 ​ m + 1) and 1 n 2 = ℑ 2 ( 6 ​ m + k) ​ ( 24 ​ m + 1) \frac{1}{n_{2}}=\frac{\Im_{1}}{(6m+k)(24m+1)}\quad\mbox{and}\quad\frac{1}{n_{2}}=\frac{\Im_{2}}{(6m+k)(24m+1)} |  | (2.12) |

for some positive integers ℑ 1 \Im_{1} and ℑ 2 \Im_{2} such that

 | ℑ 1 + ℑ 2 = 4 ​ k − 1. \Im_{1}+\Im_{2}=4k-1. |  | (2.13) |

Denote

 | ℑ = l.c.m ​ ( ℑ 1, ℑ 2), \Im=\mbox{l.c.m}(\Im_{1},\Im_{2}), |  | (2.14) |

the least common multiple of ℑ 1 \Im_{1} and ℑ 2 \Im_{2}. Let c ∈ ℤ c\in\mathbb{Z} such that m + c ​ ℑ > 0 m+c\Im>0. Observe

 | ( 6 ​ ( m + c ​ ℑ) + k) ​ ( 24 ​ ( m + c ​ ℑ) + 1) = ( 6 ​ m + k) ​ ( 24 ​ m + 1) + 6 ​ c ​ ℑ ⁡ ( 48 ​ m + 24 ​ c ​ ℑ + 4 ​ k + 1). (6(m+c\Im)+k)(24(m+c\Im)+1)=(6m+k)(24m+1)+6c\Im(48m+24c\Im+4k+1). |  | (2.15) |

By Assumption (2.12),

 | ( 6 ​ m + k) ​ ( 24 ​ m + 1) = n 2 ​ ℑ 1 = n 3 ​ ℑ 2. (6m+k)(24m+1)=n_{2}\Im_{1}=n_{3}\Im_{2}. |  | (2.16) |

The above two expressions imply that

 | ℑ 1 ( 6 ​ ( m + c ​ ℑ) + k) ​ ( 24 ​ ( m + c ​ ℑ) + 1) and ℑ 2 ( 6 ​ ( m + c ​ ℑ) + k) ​ ( 24 ​ ( m + c ​ ℑ) + 1) \frac{\Im_{1}}{(6(m+c\Im)+k)(24(m+c\Im)+1)}\quad\mbox{and}\quad\frac{\Im_{2}}{(6(m+c\Im)+k)(24(m+c\Im)+1)} |  | (2.17) |

are unit fractions. Moreover,

 | 4 ​ ( 6 ​ ( m + c ​ ℑ) + k) − ( 24 ​ ( m + c ​ ℑ) + 1) = 4 ​ ( 6 ​ m + 1) − ( 2 ​ m + 1) = 4 ​ k − 1 = ℑ 1 + ℑ 2. 4(6(m+c\Im)+k)-(24(m+c\Im)+1)=4(6m+1)-(2m+1)=4k-1=\Im_{1}+\Im_{2}. |  | (2.18) |

Therefore,

 | 4 24 ​ ( m + c ​ ℑ) + 1 \displaystyle\frac{4}{24(m+c\Im)+1} | = \displaystyle= | 1 6 ​ ( m + c ​ ℑ) + k + ℑ 1 ( 6 ​ ( m + c ​ ℑ) + k) ​ ( 24 ​ ( m + c ​ ℑ) + 1) \displaystyle\frac{1}{6(m+c\Im)+k}+\frac{\Im_{1}}{(6(m+c\Im)+k)(24(m+c\Im)+1)} |  | (2.19) |

 |  |  | + ℑ 1 ( 6 ​ ( m + c ​ ℑ) + k) ​ ( 24 ​ ( m + c ​ ℑ) + 1) \displaystyle+\frac{\Im_{1}}{(6(m+c\Im)+k)(24(m+c\Im)+1)} |  |

is a solution of the Erdös-Straus equation (1.3); that is,

 | { 24 ​ ( m + c ​ ℑ) + 1 ∣ c ∈ ℤ ​ such that ​ m + c ​ ℑ > 0 } are tame numbers. \{24(m+c\Im)+1\mid c\in\mathbb{Z}\;\mbox{such that}\;m+c\Im>0\}\quad\mbox{are tame numbers}. |  | (2.20) |

This partially explains why Mordell [14] and Terzi [22] had their modulo conditions.

Note that

 | 4 ​ k − 1 ≤ 48 ​ m − 1 4k-1\leq 48m-1 |  | (2.21) |

by (2.10). Suppose ℑ i | ( 6 ​ m + k) \Im_{i}\not|(6m+k). Since 24 ​ m + 1 24m+1 is a prime, we must have ( 24 ​ m + 1) | ℑ i (24m+1)|\Im_{i}. So the above equation yields

 | ℑ i = 24 ​ m + 1. \Im_{i}=24m+1. |  | (2.22) |

Without loss of generality, we may assume i = 2 i=2. Then

 | ℑ 1 = 4 ​ k − 1 − ℑ 2 = 4 ​ k − 24 ​ m − 2 ≤ 24 ​ m − 2. \Im_{1}=4k-1-\Im_{2}=4k-24m-2\leq 24m-2. |  | (2.23) |

Thus

 | ℑ 1 | ( 6 ​ m + k). \Im_{1}|(6m+k). |  | (2.24) |

According to (2.23), we can write

 | ℑ 1 = 4 ​ j + 2 with ​ j ∈ ℕ. \Im_{1}=4j+2\qquad\mbox{with}\;\;j\in\mathbb{N}. |  | (2.25) |

Based on (2.11) and (2.13), we have

 | ℑ 1 + 24 ​ m + 1 = ℑ 1 + ℑ 2 = 4 ​ k − 1 = 4 ​ ( 6 ​ m + k) − ( 24 ​ m + 1). \Im_{1}+24m+1=\Im_{1}+\Im_{2}=4k-1=4(6m+k)-(24m+1). |  | (2.26) |

By (2.24),

 | ℑ 1 | [2 ​ ( 24 ​ m + 1)] ⟹ ( 2 ​ j + 1) | ( 24 ​ m + 1). \Im_{1}|[2(24m+1)]\Longrightarrow(2j+1)|(24m+1). |  | (2.27) |

If j = 0 j=0, 24 ​ m + 3 = 4 ​ k − 1 ⟹ k = 6 ​ m + 1 24m+3=4k-1\Longrightarrow k=6m+1 is odd, which contradicts (2.24) and (2.25). So j > 0 j>0. Then (2.23) and (2.25) show that 2 ​ j + 1 ≥ 3 2j+1\geq 3 is a proper factor of 24 ​ m + 1 24m+1. This contradicts the assumption that 24 ​ m + 1 24m+1 is a prime.

Theorem 2.1 For a prime n n of the form 24 ​ m + 1 24m+1, its tame solution ( n 1, n 2, n 3) (n_{1},n_{2},n_{3}) must satisfies (2.10)-(2.13) and

 | ℑ 1 | ( 6 m + k), ℑ 2 | ( 6 m + k). \Im_{1}|(6m+k),\quad\Im_{2}|(6m+k). |  | (2.28) |

## 3 Cases When the Numerator Summand ℑ 2 ≤ 6 \Im_{2}\leq 6

These cases are picked out because the number 6 6 in 6 ​ m + k 6m+k in (2.10). It turns out that the results in this section cover the solvability of the majority tame primes of the form 24 ​ m + 1 24m+1 with m ≤ 2000 m\leq 2000.

### 3.1 Case ℑ 2 = 1 \Im_{2}=1

In this case,

 | ℑ 1 = 4 ​ j + 2 = 2 ​ ( 2 ​ j + 1), k = j + 1 with ​ j ∈ ℕ \Im_{1}=4j+2=2(2j+1),\quad k=j+1\quad\mbox{with}\;\;j\in\mathbb{N} |  | (3.1) |

by (2.13). The first expression in (2.28) gives’

 | 2 | ( 6 ​ m + j + 1). 2|(6m+j+1). |  | (3.2) |

So

 | j = 2 ​ s + 1 j=2s+1 |  | (3.3) |

is odd. Hence

 | 2 ​ j + 1 = 4 ​ s + 3 2j+1=4s+3 |  | (3.4) |

and

 | 6 ​ m + j + 1 = 2 ​ ( 3 ​ m + s + 1). 6m+j+1=2(3m+s+1). |  | (3.5) |

Again by first expression in (2.28), we have

 | ( 4 ​ s + 3) | ( 3 ​ m + s + 1), (4s+3)|(3m+s+1), |  | (3.6) |

which is impossible if s ≡ 0 ​ ( mod ​ 3) s\equiv 0\;(\mbox{mod}\;3). So we consider the following two subcases.

Subcase (a). s = 3 ​ r + 1 s=3r+1 with r ∈ ℕ r\in\mathbb{N}.

In this subcase,

 | 4 ​ s + 3 = 12 ​ r + 7 4s+3=12r+7 |  | (3.7) |

and

 | 3 ​ m + s + 1 = 3 ​ m + 3 ​ r + 2. 3m+s+1=3m+3r+2. |  | (3.8) |

According to (2.28),

 | 3 ​ m + 3 ​ r + 2 ≡ 0 ( mod ​ 12 ​ r + 7). 3m+3r+2\equiv 0\quad(\mbox{mod}\;12r+7). |  | (3.9) |

Thus

 | 3 ​ m + 3 ​ r + 2 ≡ 2 ​ ( 12 ​ r + 7) ( mod ​ 12 ​ r + 7), 3m+3r+2\equiv 2(12r+7)\quad(\mbox{mod}\;12r+7), |  | (3.10) |

equivalently,

 | 3 ​ m ≡ 21 ​ r + 12 ( mod ​ 12 ​ r + 7). 3m\equiv 21r+12\quad(\mbox{mod}\;12r+7). |  | (3.11) |

Hence

 | m ≡ 7 ​ r + 4 ( mod ​ 12 ​ r + 7). m\equiv 7r+4\quad(\mbox{mod}\;12r+7). |  | (3.12) |

Under this condition,

 | m = 7 ​ r + 4 + c ⁡ ( 12 ​ r + 7) for some ​ c ∈ ℕ m=7r+4+c(12r+7)\quad\mbox{for some}\;\;c\in\mathbb{N} |  | (3.13) |

and

 | 3 ​ m + 3 ​ r + 2 = ( 3 ​ c + 2) ​ ( 12 ​ r + 7). 3m+3r+2=(3c+2)(12r+7). |  | (3.14) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 2 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 7) + 2 ​ ( 12 ​ r + 7) + 1 2 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 7) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3c+2)(12r+7)}+\frac{2(12r+7)+1}{2(3c+2)(12r+7)(24m+1)} |  | (3.15) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 7) + 1 ( 3 ​ c + 2) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3c+2)(12r+7)}+\frac{1}{(3c+2)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3c+2)(12r+7)(24m+1)}. |  |

Subcase (b). s = 3 ​ r + 2 s=3r+2 with r ∈ ℕ r\in\mathbb{N}.

In this subcase,

 | 4 ​ s + 3 = 12 ​ r + 11 4s+3=12r+11 |  | (3.16) |

and

 | 3 ​ m + s + 1 = 3 ​ ( m + r + 1). 3m+s+1=3(m+r+1). |  | (3.17) |

According to (2.28),

 | 3 ​ ( m + r + 1) ≡ 0 ( mod ​ 12 ​ r + 11). 3(m+r+1)\equiv 0\quad(\mbox{mod}\;12r+11). |  | (3.18) |

Thus

 | m ≡ 11 ​ r + 10 ( mod ​ 12 ​ r + 11). m\equiv 11r+10\quad(\mbox{mod}\;12r+11). |  | (3.19) |

Under this condition,

 | m = 11 ​ r + 10 + c ⁡ ( 12 ​ r + 11) for some ​ c ∈ ℕ m=11r+10+c(12r+11)\quad\mbox{for some}\;\;c\in\mathbb{N} |  | (3.20) |

and

 | 3 ​ ( m + r + 1) = 3 ​ ( c + 1) ​ ( 12 ​ r + 11). 3(m+r+1)=3(c+1)(12r+11). |  | (3.21) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 6 ​ ( c + 1) ​ ( 12 ​ r + 11) + 2 ​ ( 12 ​ r + 11) + 1 6 ​ ( c + 1) ​ ( 12 ​ r + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6(c+1)(12r+11)}+\frac{2(12r+11)+1}{6(c+1)(12r+11)(24m+1)} |  | (3.22) |

 |  | = \displaystyle= | 1 6 ​ ( c + 1) ​ ( 12 ​ r + 11) + 1 3 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6(c+1)(12r+11)}+\frac{1}{3(c+1)(24m+1)} |  |

 |  |  | + 1 6 ​ ( c + 1) ​ ( 12 ​ r + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{6(c+1)(12r+11)(24m+1)}. |  |

Theorem 3.1 For any positive integer m m in (3.13), we have the tame solution (3.15) of the Erdös-Straus equation. If m m is of the form (3.20), then we have the tame solution (3.22) of the Erdös-Straus equation.

In (3.13), 12 ​ r + 7 = 7, 19, 31, 43, 67, 79, 103 12r+7=7,19,31,43,67,79,103 are primes when r = 0, 1, 2, 3, 5, 6, 8 r=0,1,2,3,5,6,8, respectively. In (3.20), 12 ​ r + 11 = 11, 23, 59, 71, 83, 107 12r+11=11,23,59,71,83,107 are primes when r = 0, 1, 2, 4, 5, 6, 8 r=0,1,2,4,5,6,8, respectively.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 4 ​ ( mod ​ 7) m\equiv 4\;(\mbox{mod}\;7) (cf. (3.12) with r = 0 r=0) are given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)):

( 4, 0), ( 25, 3), ( 32, 4), ( 39, 5), ( 67, 9), ( 74, 10), ( 95, 12), ( 109, 15), ( 130, 18), ( 144, 20), ( 172, 24), ( 179, 25), ( 200, 28), ( 207, 29), ( 235, 33), ( 270, 38), ( 305, 43), ( 312, 44), ( 333, 47), ( 340, 48), ( 347, 49), ( 375, 53), ( 389, 55), ( 417, 59), ( 424, 60), ( 487, 69), ( 529, 75), ( 564, 80), ( 634, 90), ( 662, 94), ( 669, 95), ( 690, 98), ( 697, 99), ( 725,103), ( 732,104), ( 739,105), ( 795,113), ( 802,114), ( 809,115), ( 837,119), ( 872,124), ( 900,128), ( 914,130), ( 935,133), ( 949,135), ( 1005,143), ( 1075,153), ( 1082,154), ( 1110,158), ( 1145,163), ( 1159,165), ( 1194,170), ( 1257,179), ( 1285,183), ( 1299,185), ( 1327,189), ( 1397,199), ( 1432,204), ( 1509,215), ( 1530,218), ( 1544,220), ( 1565,223), ( 1579,225), ( 1607,229), ( 1635,233), ( 1642,234), ( 1719,245), ( 1740,248), ( 1810,258), ( 1817,259), ( 1845,263), ( 1824,260), ( 1852,264), ( 1859,265), ( 1880,268), ( 1887,269), ( 1964,280), ( 1992,284), ( 1999,285). (4,0),(25,3),(32,4),(39,5),(67,9),(74,10),(95,12),(109,15),(130,18),(144,20),\\ (172,24),(179,25),(200,28),(207,29),(235,33),(270,38),(305,43),(312,44),(333,47),\\ (340,48),(347,49),(375,53),(389,55),(417,59),(424,60),(487,69),(529,75),(564,80),\\ (634,90),(662,94),(669,95),(690,98),(697,99),(725,103),(732,104),(739,105),(795,113),\\ (802,114),(809,115),(837,119),(872,124),(900,128),(914,130),(935,133),(949,135),\\ (1005,143),(1075,153),(1082,154),(1110,158),(1145,163),(1159,165),(1194,170),\\ (1257,179),(1285,183),(1299,185),(1327,189),(1397,199),(1432,204),(1509,215),\\ (1530,218),(1544,220),(1565,223),(1579,225),(1607,229),(1635,233),(1642,234),\\ (1719,245),(1740,248),(1810,258),(1817,259),(1845,263),(1824,260),(1852,264),\\ (1859,265),(1880,268),(1887,269),(1964,280),(1992,284),(1999,285). Total 79.
Ratio 79/591=0.1337.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 10 ​ ( mod ​ 11) m\equiv 10\;(\mbox{mod}\;11) (cf. (3.19) with r = 0 r=0) are given by the following ( m, c) (m,c) (cf. (3.20) and (3.22)):

( 10, 0), ( 54, 4), ( 87, 7), ( 175, 15), ( 197, 17), ( 230, 20), ( 274, 24), ( 285, 25), ( 362, 32), ( 472, 42), ( 560, 50), ( 637, 57), ( 714, 64), ( 747, 67), ( 824, 74), ( 967, 87), ( 1044, 94), ( 1055, 95), ( 1154,104), ( 1407,127), ( 1462,132), ( 1484,134), ( 1550,140), ( 1660,150), ( 1704,154), ( 1715,155), ( 1825,165), ( 1935,175). (10,0),(54,4),(87,7),(175,15),(197,17),(230,20),(274,24),(285,25),(362,32),\\ (472,42),(560,50),(637,57),(714,64),(747,67),(824,74),(967,87),(1044,94),(1055,95),\\ (1154,104),(1407,127),(1462,132),(1484,134),(1550,140),(1660,150),(1704,154),\\ (1715,155),(1825,165),(1935,175).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 11 ​ ( mod ​ 19) m\equiv 11\;(\mbox{mod}\;19) (cf. (3.12) with r = 1 r=1) are given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)):

( 220, 11), ( 315, 16), ( 334, 17), ( 600, 31), ( 752, 39), ( 1037, 54), ( 1170, 61), ( 1284, 67), ( 1664, 87), ( 1702, 89). (220,11),(315,16),(334,17),(600,31),(752,39),(1037,54),(1170,61),(1284,67),\\ (1664,87),(1702,89).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 21 ​ ( mod ​ 23) m\equiv 21\;(\mbox{mod}\;23) (cf. (3.19) with r = 1 r=1) are given by the following ( m, c) (m,c) (cf. (3.20) and (3.22)):

( 297, 12), ( 757, 32), ( 1102, 47), ( 1240, 53), ( 1447, 62), ( 1470, 63), ( 1562, 67). (297,12),(757,32),(1102,47),(1240,53),(1447,62),(1470,63),(1562,67).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 18 ​ ( mod ​ 31) m\equiv 18\;(\mbox{mod}\;31) (cf. (3.12) with r = 2 r=2) are given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)): ( 855, 27), ( 1475, 47), ( 1785, 57). (855,27),(1475,47),(1785,57).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 25 ​ ( mod ​ 43) m\equiv 25\;(\mbox{mod}\;43) (cf. (3.12) with r = 3 r=3) are given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)): ( 154, 3), ( 1272, 29), ( 1960, 45). (154,3),(1272,29),(1960,45).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 54 ​ ( mod ​ 59) m\equiv 54\;(\mbox{mod}\;59) (cf. (3.19) with r = 4 r=4) are given by the following ( m, c) (m,c) (cf. (3.20) and (3.22)): ( 290, 4), ( 880, 14). (290,4),(880,14).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 39 ​ ( mod ​ 67) m\equiv 39\;(\mbox{mod}\;67) (cf. (3.12) with r = 5 r=5) is given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)): ( 910, 13). (910,13).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 65 ​ ( mod ​ 71) m\equiv 65\;(\mbox{mod}\;71) (cf. (3.19) with r = 5 r=5) is given by the following ( m, c) (m,c) (cf. (3.20) and (3.22)): ( 1414, 19). (1414,19).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 46 ​ ( mod ​ 79) m\equiv 46\;(\mbox{mod}\;79) (cf. (3.12) with r = 6 r=6) is given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)): ( 915, 11). (915,11).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 60 ​ ( mod ​ 103) m\equiv 60\;(\mbox{mod}\;103) (cf. (3.12) with r = 8 r=8) is given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)): ( 1090, 10). (1090,10).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 74 ​ ( mod ​ 127) m\equiv 74\;(\mbox{mod}\;127) (cf. (3.12) with r = 10 r=10) is given by the following ( m, c) (m,c) (cf. (3.13) and (3.15)): ( 1344, 10). (1344,10).

### 3.2 Case ℑ 2 = 2 \Im_{2}=2

In this case,

 | ℑ 1 = 4 ​ j + 1, k = j + 1 with ​ j ∈ ℕ \Im_{1}=4j+1,\quad k=j+1\quad\mbox{with}\;\;j\in\mathbb{N} |  | (3.23) |

by (2.13). The second expression in (2.28) gives

 | 2 | ( 6 ​ m + j + 1). 2|(6m+j+1). |  | (3.24) |

So

 | j = 2 ​ s + 1 j=2s+1 |  | (3.25) |

is again odd. Hence

 | 4 ​ j + 1 = 8 ​ s + 5 4j+1=8s+5 |  | (3.26) |

and

 | 6 ​ m + j + 1 = 2 ​ ( 3 ​ m + s + 1). 6m+j+1=2(3m+s+1). |  | (3.27) |

By first expression in (2.28), we have

 | ( 8 ​ s + 5) | ( 3 ​ m + s + 1), (8s+5)|(3m+s+1), |  | (3.28) |

that is,

 | 3 ​ m + s + 1 ≡ 0 ( mod ​ 8 ​ s + 5). 3m+s+1\equiv 0\quad(\mbox{mod}\;8s+5). |  | (3.29) |

Thus

 | 3 ​ m + s + 1 ≡ 2 ​ ( 8 ​ s + 5) ( mod ​ 8 ​ s + 5), 3m+s+1\equiv 2(8s+5)\quad(\mbox{mod}\;8s+5), |  | (3.30) |

equivalently,

 | 3 ​ m ≡ 15 ​ s + 9 ( mod ​ 8 ​ s + 5). 3m\equiv 15s+9\quad(\mbox{mod}\;8s+5). |  | (3.31) |

Subcase (a). s ≢ 2 ​ ( mod ​ 3). s\not\equiv 2\;(\mbox{mod}\;3).

In this subcase,

 | m ≡ 5 ​ s + 3 ( mod ​ 8 ​ s + 5). m\equiv 5s+3\quad(\mbox{mod}\;8s+5). |  | (3.32) |

Under this condition,

 | m = 5 ​ s + 3 + c ⁡ ( 8 ​ s + 5) for some ​ c ∈ ℕ m=5s+3+c(8s+5)\quad\mbox{for some}\;\;c\in\mathbb{N} |  | (3.33) |

and

 | 3 ​ m + s + 1 = ( 3 ​ c + 2) ​ ( 8 ​ s + 5). 3m+s+1=(3c+2)(8s+5). |  | (3.34) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 2 ​ ( 3 ​ c + 2) ​ ( 8 ​ s + 5) + ( 8 ​ s + 5) + 2 2 ​ ( 3 ​ c + 2) ​ ( 8 ​ s + 5) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3c+2)(8s+5)}+\frac{(8s+5)+2}{2(3c+2)(8s+5)(24m+1)} |  | (3.35) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ c + 2) ​ ( 8 ​ s + 5) + 1 2 ​ ( 3 ​ c + 2) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3c+2)(8s+5)}+\frac{1}{2(3c+2)(24m+1)} |  |

 |  |  | + 1 ( 3 ​ c + 2) ​ ( 8 ​ s + 5) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{(3c+2)(8s+5)(24m+1)}. |  |

Subcase (b). s ≡ 2 ​ ( mod ​ 3). s\equiv 2\;(\mbox{mod}\;3).

In this subcase, s = 2 + 3 ​ t s=2+3t with t ∈ ℕ t\in\mathbb{N}. Moreover,

 | ℑ 1 = 8 ​ s + 5 = 24 ​ t + 21 = 3 ​ ( 8 ​ t + 7) \Im_{1}=8s+5=24t+21=3(8t+7) |  | (3.36) |

and

 | 6 ​ m + j + 1 = 2 ​ ( 3 ​ m + s + 1) = 6 ​ ( m + t + 1). 6m+j+1=2(3m+s+1)=6(m+t+1). |  | (3.37) |

Expression (2.28) gives

 | ( 8 ​ t + 7) | ( m + t + 1). (8t+7)|(m+t+1). |  | (3.38) |

Thus

 | m ≡ 7 ​ t + 6 ( mod ​ 8 ​ t + 7). m\equiv 7t+6\quad(\mbox{mod}\;8t+7). |  | (3.39) |

Under this condition,

 | m = 7 ​ t + 6 + c ⁡ ( 8 ​ t + 7) with ​ c ∈ ℕ m=7t+6+c(8t+7)\quad\mbox{with}\;\;c\in\mathbb{N} |  | (3.40) |

and

 | 6 ​ m + j + 1 = 6 ​ ( m + t + 1) = 6 ​ ( c + 1) ​ ( 8 ​ t + 7). 6m+j+1=6(m+t+1)=6(c+1)(8t+7). |  | (3.41) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 6 ​ ( c + 1) ​ ( 8 ​ t + 7) + 3 ​ ( 8 ​ t + 7) + 2 6 ​ ( c + 1) ​ ( 8 ​ t + 7) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6(c+1)(8t+7)}+\frac{3(8t+7)+2}{6(c+1)(8t+7)(24m+1)} |  | (3.42) |

 |  | = \displaystyle= | 1 6 ​ ( c + 1) ​ ( 8 ​ t + 7) + 1 2 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6(c+1)(8t+7)}+\frac{1}{2(c+1)(24m+1)} |  |

 |  |  | + 1 3 ​ ( c + 1) ​ ( 8 ​ t + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{3(c+1)(8t+7)(24m+1)}. |  |

Theorem 3.2 For any positive integer m m in (3.33), we have the tame solution (3.35) of the Erdös-Straus equation. If m m is of the form (3.40), we have the tame solution (3.42) of the Erdös-Straus equation.

In (3.33), 8 ​ s + 5 = 5, 13, 29, 37, 53, 61, 101 8s+5=5,13,29,37,53,61,101 are primes when s = 0, 1, 3, 4, 6, 7, 12 s=0,1,3,4,6,7,12, respectively. In (3.40), 8 ​ t + 7 = 7, 23, 31, 47, 71, 79, 103 8t+7=7,23,31,47,71,79,103 are primes when t = 0, 2, 3, 5, 8, 9, 12, t=0,2,3,5,8,9,12, respectively.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 3 ​ ( mod ​ 5) m\equiv 3\;(\mbox{mod}\;5) (cf. (3.32) with s = 0 s=0) are given by the following ( m, c) (m,c) (cf. (3.33) and (3.35)):

( 3, 0), ( 8, 1), ( 13, 2), ( 18, 3), ( 28, 5), ( 43, 8), ( 48, 9), ( 73, 14), ( 78, 15), ( 83, 16), ( 88, 17), ( 103, 20), ( 108, 21), ( 113, 22), ( 118, 23), ( 123, 24), ( 138, 27), ( 143, 28), ( 153, 30), ( 158, 31), ( 173, 34), ( 178, 35), ( 188, 37), ( 208, 41), ( 213, 42), ( 218, 43), ( 248, 49), ( 253, 50), ( 273, 54), ( 278, 55), ( 283, 56), ( 308, 61), ( 323, 64), ( 328, 65), ( 333, 66), ( 343, 68), ( 348, 69), ( 363, 72), ( 393, 78), ( 428, 85), ( 438, 87), ( 448, 89), ( 458, 91), ( 463, 92), ( 473, 94), ( 483, 96), ( 493, 98), ( 498, 99), ( 503,100), ( 518,103), ( 523,104), ( 543,108), ( 563,112), ( 568,113), ( 578,115), ( 608,121), ( 613,122), ( 628,125), ( 633,125), ( 638,127), ( 663,132), ( 668,133), ( 678,135), ( 693,138), ( 708,141), ( 738,147), ( 763,152), ( 768,153), ( 773,154), ( 783,156), ( 788,157), ( 803,160), ( 823,164), ( 833,166), ( 838,167), ( 843,168), ( 848,169), ( 858,171), ( 883,176), ( 888,177), ( 893,178), ( 903,180), ( 923,184), ( 928,185), ( 958,191), ( 978,195), ( 983,196), ( 993,198), ( 1033,206), ( 1043,208), ( 1048,209), ( 1068,213), ( 1078,215), ( 1088,217), ( 1113,222), ( 1118,223), ( 1123,224), ( 1128,225), ( 1153,230), ( 1158,233), ( 1183,236), ( 1188,237), ( 1198,239), ( 1228,245), ( 1243,248), ( 1263,252), ( 1273,254), ( 1293,258), ( 1298,259), ( 1308,261), ( 1313,262), ( 1328,265), ( 1343,268), ( 1348,269), ( 1363,272), ( 1368,273), ( 1378,275), ( 1418,283), ( 1428,285), ( 1438,287), ( 1473,294), ( 1483,296), ( 1503,300), ( 1513,302), ( 1518,303), ( 1533,306), ( 1538,307), ( 1553,310), ( 1568,313), ( 1583,316), ( 1588,317), ( 1608,321), ( 1613,322), ( 1618,323), ( 1623,324), ( 1638,327), ( 1673,334), ( 1708,341), ( 1713,342), ( 1718,343), ( 1733,346), ( 1748,349), ( 1753,350), ( 1758,351), ( 1768,353), ( 1783,356), ( 1818,363), ( 1823,364), ( 1873,374), ( 1893,378), ( 1898,379), ( 1903,380), ( 1923,384), ( 1928,385), ( 1943,388), ( 1958,391), ( 1973,394), ( 1988,397). (3,0),(8,1),(13,2),(18,3),(28,5),(43,8),(48,9),(73,14),(78,15),(83,16),(88,17),\\ (103,20),(108,21),(113,22),(118,23),(123,24),(138,27),(143,28),(153,30),(158,31),\\ (173,34),(178,35),(188,37),(208,41),(213,42),(218,43),(248,49),(253,50),(273,54),\\ (278,55),(283,56),(308,61),(323,64),(328,65),(333,66),(343,68),(348,69),(363,72),\\ (393,78),(428,85),(438,87),(448,89),(458,91),(463,92),(473,94),(483,96),(493,98),\\ (498,99),(503,100),(518,103),(523,104),(543,108),(563,112),(568,113),(578,115),\\ (608,121),(613,122),(628,125),(633,125),(638,127),(663,132),(668,133),(678,135),\\ (693,138),(708,141),(738,147),(763,152),(768,153),(773,154),(783,156),(788,157),\\ (803,160),(823,164),(833,166),(838,167),(843,168),(848,169),(858,171),(883,176),\\ (888,177),(893,178),(903,180),(923,184),(928,185),(958,191),(978,195),(983,196),\\ (993,198),(1033,206),(1043,208),(1048,209),(1068,213),(1078,215),(1088,217),\\ (1113,222),(1118,223),(1123,224),(1128,225),(1153,230),(1158,233),(1183,236),\\ (1188,237),(1198,239),(1228,245),(1243,248),(1263,252),(1273,254),(1293,258),\\ (1298,259),(1308,261),(1313,262),(1328,265),(1343,268),(1348,269),(1363,272),\\ (1368,273),(1378,275),(1418,283),(1428,285),(1438,287),(1473,294),(1483,296),\\ (1503,300),(1513,302),(1518,303),(1533,306),(1538,307),(1553,310),(1568,313),\\ (1583,316),(1588,317),(1608,321),(1613,322),(1618,323),(1623,324),(1638,327),\\ (1673,334),(1708,341),(1713,342),(1718,343),(1733,346),(1748,349),(1753,350),\\ (1758,351),(1768,353),(1783,356),(1818,363),(1823,364),(1873,374),(1893,378),\\ (1898,379),(1903,380),(1923,384),(1928,385),(1943,388),(1958,391),(1973,394),\\ (1988,397). Total 158. Ratio 158 / 591 = 0.2673. 158/591=0.2673.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 6 ​ ( mod ​ 7) m\equiv 6\;(\mbox{mod}\;7) (cf. (3.39) with t = 0 t=0) are given by the following ( m, c) (m,c) (cf. (3.40) and (3.42)):

( 62, 8), ( 69, 9), ( 90, 12), ( 125, 17), ( 132, 18), ( 174, 24), ( 230, 32), ( 237, 33), ( 244, 34), ( 265, 37), ( 272, 38), ( 307, 43), ( 314, 44), ( 342, 48), ( 349, 49), ( 377, 53), ( 405, 57), ( 447, 63), ( 510, 72), ( 517, 73), ( 524, 74), ( 552, 78), ( 559, 79), ( 580, 82), ( 622, 88), ( 650, 92), ( 664, 94), ( 727,103), ( 755,107), ( 762,108), ( 769,109), ( 825,117), ( 860,122), ( 867,123), ( 895,127), ( 902,128), ( 909,129), ( 979,139), ( 1000,142), ( 1007,143), ( 1014,144), ( 1035,147), ( 1077,153), ( 1084,154), ( 1140,162), ( 1147,163), ( 1175,167), ( 1189,169), ( 1217,173), ( 1245,177), ( 1322,188), ( 1350,192), ( 1357,193), ( 1392,198), ( 1462,208), ( 1469,209), ( 1504,214), ( 1560,222), ( 1595,227), ( 1602,228), ( 1672,238), ( 1700,242), ( 1735,247), ( 1742,248), ( 1777,253), ( 1805,257), ( 1889,269), ( 1910,272), ( 1945,277), ( 1959,279), ( 1980,282), ( 1994,284). (62,8),(69,9),(90,12),(125,17),(132,18),(174,24),(230,32),(237,33),(244,34),\\ (265,37),(272,38),(307,43),(314,44),(342,48),(349,49),(377,53),(405,57),(447,63),\\ (510,72),(517,73),(524,74),(552,78),(559,79),(580,82),(622,88),(650,92),(664,94),\\ (727,103),(755,107),(762,108),(769,109),(825,117),(860,122),(867,123),(895,127),\\ (902,128),(909,129),(979,139),(1000,142),(1007,143),(1014,144),(1035,147),\\ (1077,153),(1084,154),(1140,162),(1147,163),(1175,167),(1189,169),(1217,173),\\ (1245,177),(1322,188),(1350,192),(1357,193),(1392,198),(1462,208),(1469,209),\\ (1504,214),(1560,222),(1595,227),(1602,228),(1672,238),(1700,242),(1735,247),\\ (1742,248),(1777,253),(1805,257),(1889,269),(1910,272),(1945,277),(1959,279),\\ (1980,282),(1994,284). Total 72. Ratio 72 / 591 = 0.1218. 72/591=0.1218.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 8 ​ ( mod ​ 13) m\equiv 8\;(\mbox{mod}\;13) (cf. (3.32) with s = 1 s=1) are given by the following ( m, c) (m,c) (cf. (3.33) and (3.35)):

( 47, 3), ( 99, 7), ( 112, 8), ( 125, 9), ( 190, 14), ( 255, 19), ( 294, 22), ( 307, 23), ( 320, 24), ( 372, 28), ( 385, 29), ( 424, 32), ( 502, 38), ( 554, 42), ( 580, 44), ( 684, 52), ( 697, 53), ( 710, 54), ( 749, 57), ( 762, 58), ( 840, 64), ( 1035, 79), ( 1139, 87), ( 1165, 89), ( 1165, 89), ( 1217, 93), ( 1295, 99), ( 1399,107), ( 1412,108), ( 1477,113), ( 1529,117), ( 1555,119), ( 1672,128), ( 1789,137), ( 1854,142), ( 1880,144), ( 1945,144). (47,3),(99,7),(112,8),(125,9),(190,14),(255,19),(294,22),(307,23),(320,24),\\ (372,28),(385,29),(424,32),(502,38),(554,42),(580,44),(684,52),(697,53),(710,54),\\ (749,57),(762,58),(840,64),(1035,79),(1139,87),(1165,89),(1165,89),(1217,93),\\ (1295,99),(1399,107),(1412,108),(1477,113),(1529,117),(1555,119),(1672,128),\\ (1789,137),(1854,142),(1880,144),(1945,144). Total 37. Ratio 37 / 591 = 0.0626. 37/591=0.0626.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 20 ​ ( mod ​ 23) m\equiv 20\;(\mbox{mod}\;23) (cf. (3.39) with t = 2 t=2) are given by the following ( m, c) (m,c) (cf. (3.40) and (3.42)):

( 365, 15), ( 595, 25), ( 1354, 58), ( 1377, 59), ( 1837, 79), ( 1860, 80). (365,15),(595,25),(1354,58),(1377,59),(1837,79),(1860,80).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 18 ​ ( mod ​ 29) m\equiv 18\;(\mbox{mod}\;29) (cf. (3.32) with s = 3 s=3) are given by the following ( m, c) (m,c) (cf. (3.33) and (3.35)):

( 105, 3), ( 134, 4), ( 337, 41), ( 1004, 34), ( 1120, 38), ( 1439, 49), ( 1642, 56). (105,3),(134,4),(337,41),(1004,34),(1120,38),(1439,49),(1642,56).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 27 ​ ( mod ​ 31) m\equiv 27\;(\mbox{mod}\;31) (cf. (3.39) with t = 3 t=3) is given by the following ( m, c) (m,c) (cf. (3.40) and (3.42)): ( 1205, 38) (1205,38).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 23 ​ ( mod ​ 37) m\equiv 23\;(\mbox{mod}\;37) (cf. (3.32) with s = 4 s=4) are given by the following ( m, c) (m,c) (cf. (3.33) and (3.35)):

( 245, 6), ( 430, 11), ( 504, 13), ( 652, 17), ( 1429, 39), ( 1614, 43), ( 1799, 48). (245,6),(430,11),(504,13),(652,17),(1429,39),(1614,43),(1799,48).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 38 ​ ( mod ​ 61) m\equiv 38\;(\mbox{mod}\;61) (cf. (3.32) with s = 7 s=7) are given by the following ( m, c) (m,c) (cf. (3.33) and (3.35)): ( 770, 12), ( 1197, 19), ( 1624, 26). (770,12),(1197,19),(1624,26).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 69 ​ ( mod ​ 79) m\equiv 69\;(\mbox{mod}\;79) (cf. (3.39) with t = 9 t=9) is given by the following ( m, c) (m,c) (cf. (3.40) and (3.42)): ( 1965, 24) (1965,24).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 63 ​ ( mod ​ 101) m\equiv 63\;(\mbox{mod}\;101) (cf. (3.32) with s = 12 s=12) is given by the following ( m, c) (m,c) (cf. (3.33) and (3.35)): ( 1982, 19). (1982,19).

### 3.3 Case ℑ 2 = 3 \Im_{2}=3

In this case,

 | ℑ 1 = 4 ​ j, k = j + 1 with ​ j ∈ ℕ \Im_{1}=4j,\quad k=j+1\quad\mbox{with}\;\;j\in\mathbb{N} |  | (3.43) |

by (2.13). Moreover, The first expression in (2.28) implies

 | 4 ​ j | ( 6 ​ m + j + 1). 4j|(6m+j+1). |  | (3.44) |

So

 | 4 | ( 6 ​ m + j + 1). 4|(6m+j+1). |  | (3.45) |

The above expression implies that

 | j = 2 ​ s + 1 j=2s+1 |  | (3.46) |

is odd. Moreover,

 | 6 ​ m + j + 1 = 2 ​ ( 3 ​ m + s + 1). 6m+j+1=2(3m+s+1). |  | (3.47) |

According to (2.28),

 | 3 | ( 6 ​ m + j + 1) ⟹ 3 | ( 3 ​ m + s + 1). 3|(6m+j+1)\Longrightarrow 3|(3m+s+1). |  | (3.48) |

Thus

 | s = 3 ​ r + 2 for some ​ r ∈ ℕ. s=3r+2\quad\mbox{for some}\;r\in\mathbb{N}. |  | (3.49) |

 | j = 2 ​ ( 3 ​ r + 2) + 1 = 6 ​ r + 5. j=2(3r+2)+1=6r+5. |  | (3.50) |

Note

 | 3 ​ m + s + 1 = 3 ​ ( m + r + 1). 3m+s+1=3(m+r+1). |  | (3.51) |

So (3.44) yields

 | m + r + 1 ≡ 0 ( mod ​ 2 ​ ( 6 ​ r + 5)). m+r+1\equiv 0\quad(\mbox{mod}\;2(6r+5)). |  | (3.52) |

Subcase (a). r = 2 ​ t r=2t and m = 2 ​ m 1 + 1 m=2m_{1}+1 with t, m 1 ∈ ℕ t,m_{1}\in\mathbb{N}.

In this subcase, m + r + 1 = 2 ​ ( m 1 + t + 1) m+r+1=2(m_{1}+t+1) and 6 ​ r + 5 = 12 ​ t + 5 6r+5=12t+5. By the above equation,

 | m 1 + t + 1 ≡ 0 ( mod ​ 12 ​ t + 5); m_{1}+t+1\equiv 0\quad(\mbox{mod}\;12t+5); |  | (3.53) |

that is,

 | m 1 ≡ 11 ​ t + 4 ( mod ​ 12 ​ t + 5). m_{1}\equiv 11t+4\quad(\mbox{mod}\;12t+5). |  | (3.54) |

Under this condition,

 | m 1 = 11 ​ t + 4 + c ⁡ ( 12 ​ t + 5) for some ​ c ∈ ℕ m_{1}=11t+4+c(12t+5)\quad\mbox{for some}\;\;c\in\mathbb{N} |  | (3.55) |

So

 | m = 2 ​ m 1 + 1 = 22 ​ t + 9 + 2 ​ c ​ ( 12 ​ t + 5) m=2m_{1}+1=22t+9+2c(12t+5) |  | (3.56) |

and

 | 3 ​ m + s + 1 = 6 ​ ( c + 1) ​ ( 12 ​ t + 5). 3m+s+1=6(c+1)(12t+5). |  | (3.57) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 12 ​ t + 5) + 4 ​ ( 12 ​ t + 5) + 3 12 ​ ( c + 1) ​ ( 12 ​ t + 5) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(12t+5)}+\frac{4(12t+5)+3}{12(c+1)(12t+5)(24m+1)} |  | (3.58) |

 |  | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 12 ​ t + 5) + 1 3 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(12t+5)}+\frac{1}{3(c+1)(24m+1)} |  |

 |  |  | + 1 4 ​ ( c + 1) ​ ( 12 ​ t + 5) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(c+1)(12t+5)(24m+1)}. |  |

Subcase (b). r = 2 ​ t + 1 r=2t+1 and m = 2 ​ m 1 m=2m_{1} with t, m 1 ∈ ℕ t,m_{1}\in\mathbb{N}.

In this subcase, m + r + 1 = 2 ​ ( m 1 + t + 1) m+r+1=2(m_{1}+t+1) and 6 ​ r + 5 = 12 ​ t + 11 6r+5=12t+11. By the above equation,

 | m 1 + t + 1 ≡ 0 ( mod ​ 12 ​ t + 11); m_{1}+t+1\equiv 0\quad(\mbox{mod}\;12t+11); |  | (3.59) |

that is,

 | m 1 ≡ 11 ​ t + 10 ( mod ​ 12 ​ t + 11). m_{1}\equiv 11t+10\quad(\mbox{mod}\;12t+11). |  | (3.60) |

Under this condition,

 | m 1 = 11 ​ t + 10 + c ⁡ ( 12 ​ t + 11) for some ​ c ∈ ℕ m_{1}=11t+10+c(12t+11)\quad\mbox{for some}\;\;c\in\mathbb{N} |  | (3.61) |

So

 | m = 2 ​ m 1 = 22 ​ t + 20 + 2 ​ c ​ ( 12 ​ t + 11). m=2m_{1}=22t+20+2c(12t+11). |  | (3.62) |

 | 3 ​ m + s + 1 = 6 ​ ( c + 1) ​ ( 12 ​ t + 11). 3m+s+1=6(c+1)(12t+11). |  | (3.63) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 12 ​ t + 11) + 4 ​ ( 12 ​ t + 11) + 3 12 ​ ( c + 1) ​ ( 12 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(12t+11)}+\frac{4(12t+11)+3}{12(c+1)(12t+11)(24m+1)} |  | (3.64) |

 |  | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 12 ​ t + 11) + 1 3 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(12t+11)}+\frac{1}{3(c+1)(24m+1)} |  |

 |  |  | + 1 4 ​ ( c + 1) ​ ( 12 ​ t + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(c+1)(12t+11)(24m+1)}. |  |

Theorem 3.3 For any positive integer m m in (3.56), we have the tame solution (3.58) of the Erdös-Straus equation. If m m is of the form (3.62), then we have the tame solution (3.64) of the Erdös-Straus equation.

In (3.56), 12 ​ t + 5 = 5, 17, 29, 41, 53, 89, 101 12t+5=5,17,29,41,53,89,101 are primes when s = 0, 1, 3, 4, 7, 8 s=0,1,3,4,7,8, respectively.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 9 ​ ( mod ​ 10) m\equiv 9\;(\mbox{mod}\;10) (cf. (3.56) with t = 0 t=0) are given by the following ( m, c) (m,c) (cf. (3.56) and (3.58)):

( 19, 1), ( 89, 8), ( 119, 11), ( 169, 16), ( 239, 23), ( 259, 25), ( 299, 29), ( 309, 30), ( 409, 40), ( 469, 46), ( 479, 47), ( 549, 54), ( 579, 57), ( 659, 65), ( 719, 71), ( 729, 72), ( 759, 75), ( 869, 86), ( 899, 89), ( 959, 95), ( 999, 99), ( 1029,102), ( 1069,106), ( 1169,116), ( 1179,117), ( 1209,120), ( 1279,127), ( 1319,131), ( 1349,134), ( 1419,141), ( 1499,149), ( 1519,151), ( 1569,156), ( 1599,159), ( 1629,162), ( 1709,170), ( 1739,173), ( 1769,176), ( 1779,177), ( 1909,190), ( 1979,197), ( 1989,198). (19,1),(89,8),(119,11),(169,16),(239,23),(259,25),(299,29),(309,30),(409,40),\\ (469,46),(479,47),(549,54),(579,57),(659,65),(719,71),(729,72),(759,75),(869,86),\\ (899,89),(959,95),(999,99),(1029,102),(1069,106),(1169,116),(1179,117),(1209,120),\\ (1279,127),(1319,131),(1349,134),(1419,141),(1499,149),(1519,151),(1569,156),\\ (1599,159),(1629,162),(1709,170),(1739,173),(1769,176),(1779,177),(1909,190),\\ (1979,197),(1989,198). Total 42. Ratio 42/591=0.071.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 20 ​ ( mod ​ 22) m\equiv 20\;(\mbox{mod}\;22) (cf. (3.62) with t = 0 t=0) are given by the following ( m, c) (m,c) (cf. (3.62) and (3.64)):

( 42, 1), ( 108, 8), ( 570, 55), ( 614, 27), ( 724, 32), ( 812, 36), ( 922, 41), ( 1142, 51), ( 1274, 57), ( 1692, 76). (42,1),(108,8),(570,55),(614,27),(724,32),(812,36),(922,41),(1142,51),(1274,57),\\ (1692,76).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 42 ​ ( mod ​ 46) m\equiv 42\;(\mbox{mod}\;46) (cf. (3.62) with t = 1 t=1) are given by the following ( m, c) (m,c) (cf. (3.62) and (3.64)): ( 364, 7), ( 640, 13), ( 1790, 38). (364,7),(640,13),(1790,38).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 53 ​ ( mod ​ 58) m\equiv 53\;(\mbox{mod}\;58) (cf. (3.56) with t = 2 t=2) is given by the following ( m, c) (m,c) (cf. (3.56) and (3.58)): ( 1387, 23). (1387,23).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 64 ​ ( mod ​ 70) m\equiv 64\;(\mbox{mod}\;70) (cf. (3.62) with t = 2 t=2) are given by the following ( m, c) (m,c) (cf. (3.62) and (3.64)): ( 484, 6), ( 694, 9), ( 1674, 23). (484,6),(694,9),(1674,23).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 75 ​ ( mod ​ 82) m\equiv 75\;(\mbox{mod}\;82) (cf. (3.56) with t = 3 t=3) is given by the following ( m, c) (m,c) (cf. (3.56) and (3.58)): ( 157, 1). (157,1).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 86 ​ ( mod ​ 94) m\equiv 86\;(\mbox{mod}\;94) (cf. (3.62) with t = 3 t=3) is given by the following ( m, c) (m,c) (cf. (3.62) and (3.64)): ( 932, 9). (932,9).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 141 ​ ( mod ​ 154) m\equiv 141\;(\mbox{mod}\;154) (cf. (3.56) with t = 6 t=6) is given by the following ( m, c) (m,c) (cf. (3.56) and (3.58)): ( 1065, 6). (1065,6).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 163 ​ ( mod ​ 178) m\equiv 163\;(\mbox{mod}\;178) (cf. (3.56) with t = 6 t=6) is given by the following ( m, c) (m,c) (cf. (3.56) and (3.58)): ( 875, 4). (875,4).

### 3.4 Case ℑ 2 = 4 \Im_{2}=4

This is the case when

 | ℑ 1 = 4 ​ j + 3, k = j + 2 with ​ j ∈ ℕ \displaystyle\Im_{1}=4j+3,\quad k=j+2\quad\mbox{with}\;\;j\in\mathbb{N} |  | (3.65) |

by (2.13). Moreover,

 | 6 ​ m + k = 6 ​ m + j + 2. 6m+k=6m+j+2. |  | (3.66) |

According to the second expression in (2.28),

 | 4 | ( 6 ​ m + j + 2). 4|(6m+j+2). |  | (3.67) |

Subcase (a). m = 2 ​ m 1 m=2m_{1} with m 1 ∈ ℕ m_{1}\in\mathbb{N}.

In this subcase, 6 ​ m + j + 2 = 12 ​ m 1 + j + 2 6m+j+2=12m_{1}+j+2. The above expression yields

 | j = 4 ​ s + 2 for some ​ s ∈ ℕ. j=4s+2\quad\mbox{for some}\;s\in\mathbb{N}. |  | (3.68) |

Now

 | 4 ​ j + 3 = 16 ​ s + 11, 6 ​ m + j + 2 = 4 ​ ( 3 ​ m 1 + s + 1). 4j+3=16s+11,\quad 6m+j+2=4(3m_{1}+s+1). |  | (3.69) |

According to the first expression in (2.28),

 | ( 16 ​ s + 11) | ( 3 ​ m 1 + s + 1); (16s+11)|(3m_{1}+s+1); |  | (3.70) |

that is,

 | 3 ​ m 1 + s + 1 ≡ 0 ( mod ​ 16 ​ s + 11). 3m_{1}+s+1\equiv 0\quad(\mbox{mod}\;16s+11). |  | (3.71) |

It is impossible if s ≡ 1 ​ ( mod ​ 3) s\equiv 1\;(\mbox{mod}\;3).

Situation (a1). s = 3 ​ r s=3r with r ∈ ℕ r\in\mathbb{N}.

In this situation,

 | 3 ​ m 1 + 3 ​ r + 1 ≡ 2 ​ ( 48 ​ r + 11) ( mod ​ 48 ​ r + 11). 3m_{1}+3r+1\equiv 2(48r+11)\quad(\mbox{mod}\;48r+11). |  | (3.72) |

So

 | 3 ​ m 1 ≡ 93 ​ r + 21 ( mod ​ 48 ​ r + 11). 3m_{1}\equiv 93r+21\quad(\mbox{mod}\;48r+11). |  | (3.73) |

Hence

 | m 1 ≡ 31 ​ r + 7 ( mod ​ 48 ​ r + 11). m_{1}\equiv 31r+7\quad(\mbox{mod}\;48r+11). |  | (3.74) |

Under this condition,

 | m 1 = 31 ​ r + 7 + c ⁡ ( 48 ​ r + 11) for some ​ c ∈ ℕ m_{1}=31r+7+c(48r+11)\quad\mbox{for some}\;\;c\in\mathbb{N} |  | (3.75) |

So

 | m = 2 ​ m 1 = 62 ​ r + 14 + 2 ​ c ​ ( 48 ​ r + 11) m=2m_{1}=62r+14+2c(48r+11) |  | (3.76) |

and

 | 6 ​ m + j + 2 = 4 ​ ( 3 ​ m 1 + s + 1) = 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ r + 11). 6m+j+2=4(3m_{1}+s+1)=4(3c+2)(48r+11). |  | (3.77) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ r + 11) + ( 48 ​ r + 11) + 4 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ r + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3c+2)(48r+11)}+\frac{(48r+11)+4}{4(3c+2)(48r+11)(24m+1)} |  | (3.78) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ r + 11) + 1 4 ​ ( 3 ​ c + 2) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3c+2)(48r+11)}+\frac{1}{4(3c+2)(24m+1)} |  |

 |  |  | + 1 ( 3 ​ c + 2) ​ ( 48 ​ r + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{(3c+2)(48r+11)(24m+1)}.\qquad |  |

Situation (a2). s = 3 ​ r + 2 s=3r+2 with r ∈ ℕ r\in\mathbb{N}.

In this situation, 4 ​ j + 3 = 48 ​ r + 43 4j+3=48r+43 and (2.70) gives

 | 3 ​ m 1 + 3 ​ r + 3 ≡ 0 ( mod ​ 48 ​ r + 43). 3m_{1}+3r+3\equiv 0\quad(\mbox{mod}\;48r+43). |  | (3.79) |

So

 | m 1 + r + 1 ≡ 0 ( mod ​ 48 ​ r + 43); m_{1}+r+1\equiv 0\quad(\mbox{mod}\;48r+43); |  | (3.80) |

that is,

 | m 1 ≡ 47 ​ r + 42 ( mod ​ 48 ​ r + 43). m_{1}\equiv 47r+42\quad(\mbox{mod}\;48r+43). |  | (3.81) |

Under this condition,

 | m 1 = 47 ​ r + 42 + c ⁡ ( 48 ​ r + 43) for some ​ c ∈ ℕ, m_{1}=47r+42+c(48r+43)\quad\mbox{for some}\;\;c\in\mathbb{N}, |  | (3.82) |

So

 | m = 94 ​ r + 84 + 2 ​ c ​ ( 48 ​ r + 43). m=94r+84+2c(48r+43). |  | (3.83) |

and

 | 6 ​ m + j + 2 = 4 ​ ( 3 ​ m 1 + s + 1) = 12 ​ ( m 1 + r + 1) = 12 ​ ( c + 1) ​ ( 48 ​ r + 43). 6m+j+2=4(3m_{1}+s+1)=12(m_{1}+r+1)=12(c+1)(48r+43). |  | (3.84) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 48 ​ r + 43) + ( 48 ​ r + 43) + 4 12 ​ ( c + 1) ​ ( 48 ​ r + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(48r+43)}+\frac{(48r+43)+4}{12(c+1)(48r+43)(24m+1)} |  | (3.85) |

 |  | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 48 ​ r + 43) + 1 12 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(48r+43)}+\frac{1}{12(c+1)(24m+1)} |  |

 |  |  | + 1 3 ​ ( c + 1) ​ ( 48 ​ r + 43) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{3(c+1)(48r+43)(24m+1)}.\qquad |  |

Subcase (b). m = 2 ​ m 1 + 1 m=2m_{1}+1 with m 1 ∈ ℕ m_{1}\in\mathbb{N}.

In this subcase, 6 ​ m + j + 2 = 12 ​ m 1 + j + 8 6m+j+2=12m_{1}+j+8. Expression (3.59) yields

 | j = 4 ​ s for some ​ s ∈ ℕ. j=4s\quad\mbox{for some}\;s\in\mathbb{N}. |  | (3.86) |

Now

 | ℑ 1 = 4 ​ j + 3 = 16 ​ s + 3, 6 ​ m + j + 2 = 4 ​ ( 3 ​ m 1 + s + 2). \Im_{1}=4j+3=16s+3,\quad 6m+j+2=4(3m_{1}+s+2). |  | (3.87) |

According to the first expression in (2.28),

 | ( 16 ​ s + 3) | ( 3 ​ m 1 + s + 2); (16s+3)|(3m_{1}+s+2); |  | (3.88) |

that is,

 | 3 ​ m 1 + s + 2 ≡ 0 ( mod ​ 16 ​ s + 3). 3m_{1}+s+2\equiv 0\quad(\mbox{mod}\;16s+3). |  | (3.89) |

This is impossible if s ≡ 0 ​ ( mod ​ 3) s\equiv 0\;(\mbox{mod}\;3).

Situation (b1). s ≡ 1 ​ ( mod ​ 3) s\equiv 1\;(\mbox{mod}\;3).

In this situation, s = 3 ​ t + 1 s=3t+1 with t ∈ ℕ t\in\mathbb{N}. Note

 | ℑ 1 = 48 ​ t + 19, 6 ​ m + j + 2 = 12 ​ ( m 1 + t + 1). \Im_{1}=48t+19,\quad 6m+j+2=12(m_{1}+t+1). |  | (3.90) |

According to (2.28),

 | ( 48 ​ t + 19) | ( m 1 + t + 1). (48t+19)|(m_{1}+t+1). |  | (3.91) |

Equivalently,

 | m 1 + t + 1 ≡ 0 ( mod ​ 48 ​ t + 19); m_{1}+t+1\equiv 0\quad(\mbox{mod}\;48t+19); |  | (3.92) |

that is,

 | m 1 ≡ 47 ​ t + 18 ( mod ​ 48 ​ t + 19); m_{1}\equiv 47t+18\quad(\mbox{mod}\;48t+19); |  | (3.93) |

Under this condition,

 | m 1 = 47 ​ t + 18 + c ⁡ ( 48 ​ t + 19) with ​ c ∈ ℕ. m_{1}=47t+18+c(48t+19)\quad\mbox{with}\;\;c\in\mathbb{N}. |  | (3.94) |

Hence

 | m = 2 ​ m 1 + 1 = 94 ​ t + 37 + 2 ​ c ​ ( 48 ​ t + 19) m=2m_{1}+1=94t+37+2c(48t+19) |  | (3.95) |

and

 | 6 ​ m + k = 6 ​ m + j + 2 = 12 ​ ( c + 1) ​ ( 48 ​ t + 19). 6m+k=6m+j+2=12(c+1)(48t+19). |  | (3.96) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 48 ​ t + 19) + ( 48 ​ t + 19) + 4 12 ​ ( c + 1) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(48t+19)}+\frac{(48t+19)+4}{12(c+1)(48t+19)(24m+1)} |  | (3.97) |

 |  | = \displaystyle= | 1 12 ​ ( c + 1) ​ ( 48 ​ t + 19) + 1 12 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12(c+1)(48t+19)}+\frac{1}{12(c+1)(24m+1)} |  |

 |  |  | + 1 3 ​ ( c + 1) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{3(c+1)(48t+19)(24m+1)}. |  |

Situation (b2). s ≡ 2 ​ ( mod ​ 3) s\equiv 2\;(\mbox{mod}\;3).

In this situation, s = 3 ​ t + 2 s=3t+2 with t ∈ ℕ t\in\mathbb{N}. Note

 | ℑ 1 = 48 ​ t + 35, 6 ​ m + j + 2 = 4 ​ ( 3 ​ ( m 1 + t) + 4). \Im_{1}=48t+35,\quad 6m+j+2=4(3(m_{1}+t)+4). |  | (3.98) |

According to (2.28),

 | ( 48 ​ t + 35) | ( 3 ​ ( m 1 + t) + 4). (48t+35)|(3(m_{1}+t)+4). |  | (3.99) |

Equivalently,

 | 3 ​ ( m 1 + t) + 4 ≡ 0 ( mod ​ 48 ​ t + 35). 3(m_{1}+t)+4\equiv 0\quad(\mbox{mod}\;48t+35). |  | (3.100) |

Observe

 | 3 ​ ( m 1 + t) + 4 ≡ 2 ​ ( 48 ​ t + 35) ( mod ​ 48 ​ t + 35). 3(m_{1}+t)+4\equiv 2(48t+35)\quad(\mbox{mod}\;48t+35). |  | (3.101) |

Thus

 | m 1 ≡ 31 ​ t + 22 ( mod ​ 48 ​ t + 35); m_{1}\equiv 31t+22\quad(\mbox{mod}\;48t+35); |  | (3.102) |

Under this condition,

 | m 1 = 31 ​ t + 22 + c ⁡ ( 48 ​ t + 35) with ​ c ∈ ℕ. m_{1}=31t+22+c(48t+35)\quad\mbox{with}\;\;c\in\mathbb{N}. |  | (3.103) |

Hence

 | m = 2 ​ m 1 + 1 = 62 ​ t + 45 + 2 ​ c ​ ( 48 ​ t + 35) m=2m_{1}+1=62t+45+2c(48t+35) |  | (3.104) |

and

 | 6 ​ m + k = 6 ​ m + j + 2 = 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ t + 35). 6m+k=6m+j+2=4(3c+2)(48t+35). |  | (3.105) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ t + 35) + ( 48 ​ t + 35) + 4 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3c+2)(48t+35)}+\frac{(48t+35)+4}{4(3c+2)(48t+35)(24m+1)} |  | (3.106) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ c + 2) ​ ( 48 ​ t + 35) + 1 4 ​ ( 3 ​ c + 2) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3c+2)(48t+35)}+\frac{1}{4(3c+2)(24m+1)} |  |

 |  |  | + 1 ( 3 ​ c + 2) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{(3c+2)(48t+35)(24m+1)}. |  |

Theorem 3.4 For any positive integer m m in (3.76), we have the tame solution (3.78) of the Erdös-Straus equation. If m m is of the form (3.83), then we have the tame solution (3.85) of the Erdös-Straus equation. When m m is of the form (3.95), we have the tame solution (3.97) of the Erdös-Straus equation. Letting m m be of the form (3.104), we have the tame solution (3.106) of the Erdös-Straus equation

In (3.76), 48 ​ r + 11 = 11, 59, 107 48r+11=11,59,107 are primes when r = 0, 1, 2 r=0,1,2, respectively. In (3.83), 48 ​ r + 43 = 43,139,283 48r+43=43,139,283 are primes when t = 0, 2, 5 t=0,2,5, respectively. In (3.95), 48 ​ r + 19 = 19, 67, 163 48r+19=19,67,163 are primes when r = 0, 1, 3 r=0,1,3, respectively. In (3.104), 48 ​ r + 35 = 83,131,179 48r+35=83,131,179 are primes when r = 1, 2, 3 r=1,2,3, respectively.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 14 ​ ( mod ​ 22) m\equiv 14\;(\mbox{mod}\;22) (cf. (3.75) with r = 0 r=0) are given by the following ( m, c) (m,c) (cf. (3.76) and (3.78)):

( 14, 0), ( 432, 19), ( 542, 24), ( 630, 28), ( 740, 33), ( 960, 43), ( 1092, 43), ( 1114, 50), ( 1312, 59), ( 1400, 63), ( 1422, 64), ( 1510, 68), ( 1730, 78). (14,0),(432,19),(542,24),(630,28),(740,33),(960,43),(1092,43),(1114,50),(1312,59),\\ (1400,63),(1422,64),(1510,68),(1730,78).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 37 ​ ( mod ​ 38) m\equiv 37\;(\mbox{mod}\;38) (cf. (3.95) with t = 0 t=0) are given by the following ( m, c) (m,c) (cf. (3.95) and (3.97)):

( 75, 1), ( 227, 5), ( 987, 25), ( 1405, 36), ( 1557, 40), ( 1937, 50). (75,1),(227,5),(987,25),(1405,36),(1557,40),(1937,50).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 45 ​ ( mod ​ 70) m\equiv 45\;(\mbox{mod}\;70) (cf. (3.104) with t = 0 t=0) are given by the following ( m, c) (m,c) (cf. (3.104) and (3.106)):

( 465, 6), ( 535, 7), ( 745, 10), ( 955, 13), ( 1235, 17). (465,6),(535,7),(745,10),(955,13),(1235,17).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 84 ​ ( mod ​ 86) m\equiv 84\;(\mbox{mod}\;86) (cf. (3.83) with r = 0 r=0) is given by the following ( m, c) (m,c) (cf. (3.83) and (3.85)): ( 1890, 21) (1890,21).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 76 ​ ( mod ​ 118) m\equiv 76\;(\mbox{mod}\;118) (cf. (3.75) with r = 1 r=1) are given by the following ( m, c) (m,c) (cf. (3.76) and (3.78)): ( 1020, 8), ( 1492, 12) (1020,8),(1492,12).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 131 ​ ( mod ​ 134) m\equiv 131\;(\mbox{mod}\;134) (cf. (3.95) with t = 1 t=1) is given by the following ( m, c) (m,c) (cf. (3.95) and (3.97)): ( 1337, 9) (1337,9).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 178 ​ ( mod ​ 182) m\equiv 178\;(\mbox{mod}\;182) (cf. (3.83) with r = 1 r=1) are given by the following ( m, c) (m,c) (cf. (3.83) and (3.85)): ( 360, 1), ( 1452, 7) (360,1),(1452,7).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 177 ​ ( mod ​ 259) m\equiv 177\;(\mbox{mod}\;259) (cf. (3.104) with t = 5 t=5) is given by the following ( m, c) (m,c) (cf. (3.104) and (3.106)): ( 355, 0) (355,0).

### 3.5 Case ℑ 2 = 5 \Im_{2}=5

This is the case when

 | ℑ 1 = 4 ​ j + 2, k = j + 2. \displaystyle\Im_{1}=4j+2,\quad k=j+2. |  | (3.107) |

Moreover,

 | 6 ​ m + k = 6 ​ m + j + 2. 6m+k=6m+j+2. |  | (3.108) |

According to the firs expression in (2.28),

 | 2 | ( 6 ​ m + j + 2). 2|(6m+j+2). |  | (3.109) |

So

 | j = 2 ​ s for some ​ s ∈ ℕ. j=2s\quad\mbox{for some}\;s\in\mathbb{N}. |  | (3.110) |

Now

 | 4 ​ j + 2 = 2 ​ ( 4 ​ s + 1), 6 ​ m + j + 2 = 2 ​ ( 3 ​ m + s + 1). 4j+2=2(4s+1),\quad 6m+j+2=2(3m+s+1). |  | (3.111) |

According to the first expression in (2.28),

 | ( 4 ​ s + 1) | ( 3 ​ m + s + 1); (4s+1)|(3m+s+1); |  | (3.112) |

that is,

 | 3 ​ m + s + 1 ≡ 0 ( mod ​ 4 ​ s + 1). 3m+s+1\equiv 0\quad(\mbox{mod}\;4s+1). |  | (3.113) |

Note

 | 3 ​ m + s + 1 ≡ 4 ​ s + 1 ( mod ​ 4 ​ s + 1). 3m+s+1\equiv 4s+1\quad(\mbox{mod}\;4s+1). |  | (3.114) |

Equivalently,

 | 3 ​ m ≡ 3 ​ s ( mod ​ 4 ​ s + 1). 3m\equiv 3s\quad(\mbox{mod}\;4s+1). |  | (3.115) |

Subcase (a). s ≡ 2 ​ ( mod ​ 3) s\equiv 2\;(\mbox{mod}\;3).

In this subcase, s = 3 ​ t + 2 s=3t+2 for some s ∈ ℕ s\in\mathbb{N}. Then

 | 3 ​ m ≡ 3 ​ s ( mod ​ 12 ​ t + 9). 3m\equiv 3s\quad(\mbox{mod}\;12t+9). |  | (3.116) |

Thus

 | m ≡ 3 ​ t + 2 ( mod ​ 4 ​ t + 3). m\equiv 3t+2\quad(\mbox{mod}\;4t+3). |  | (3.117) |

So

 | 4 ​ j + 2 = 2 ​ ( 4 ​ s + 1) = 6 ​ ( 4 ​ t + 3) 4j+2=2(4s+1)=6(4t+3) |  | (3.118) |

and

 | m = 3 ​ t + 2 + c ⁡ ( 4 ​ t + 3) for some ​ c ∈ ℕ. m=3t+2+c(4t+3)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (3.119) |

Moreover,

 | 3 ​ m + s + 1 = 3 ​ ( m + t + 1) = 3 ​ ( c + 1) ​ ( 4 ​ t + 3). 3m+s+1=3(m+t+1)=3(c+1)(4t+3). |  | (3.120) |

According (2.11) and (2.13),

 | ℑ 1 + ℑ 2 = 4 ​ k − 1 = 4 ​ ( 6 ​ m + k) − ( 24 ​ m + 1). \Im_{1}+\Im_{2}=4k-1=4(6m+k)-(24m+1). |  | (3.121) |

If (2.28) holds, then

 | g. c. d ⁡ ( ℑ 1, ℑ 2) = 1 because ​ 24 ​ m + 1 ​ is a prime. g.c.d(\Im_{1},\Im_{2})=1\quad\mbox{because}\;24m+1\;\mbox{is a prime}. |  | (3.122) |

By the second expression in (2.28) and (3.102),

 | 5 | [3 ​ ( c + 1) ​ ( 4 ​ t + 3)] ⟹ 5 | ( c + 1) ⟹ c = 5 ​ d + 4 with ​ d ∈ ℕ. 5|[3(c+1)(4t+3)]\Longrightarrow 5|(c+1)\Longrightarrow c=5d+4\quad\mbox{with}\;\;d\in\mathbb{N}. |  | (3.123) |

Hence

 | m = 3 ​ t + 2 + ( 5 ​ d + 4) ​ ( 4 ​ t + 3) m=3t+2+(5d+4)(4t+3) |  | (3.124) |

and

 | 6 ​ m + j + 2 = 2 ​ ( 3 ​ m + s + 1) = 30 ​ ( d + 1) ​ ( 4 ​ t + 3). 6m+j+2=2(3m+s+1)=30(d+1)(4t+3). |  | (3.125) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 30 ​ ( d + 1) ​ ( 4 ​ t + 3) + 6 ​ ( 4 ​ t + 3) + 5 30 ​ ( d + 1) ​ ( 4 ​ t + 3) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{30(d+1)(4t+3)}+\frac{6(4t+3)+5}{30(d+1)(4t+3)(24m+1)} |  | (3.126) |

 |  | = \displaystyle= | 1 30 ​ ( d + 1) ​ ( 4 ​ t + 3) + 1 5 ​ ( d + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{30(d+1)(4t+3)}+\frac{1}{5(d+1)(24m+1)} |  |

 |  |  | + 1 OPEN 6 ​ ( d + 1) ​ ( 4 ​ t + 3)) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{6(d+1)(4t+3))(24m+1)}. |  |

Subcase (b). s ≢ 2 ​ ( mod ​ 3) s\not\equiv 2\;(\mbox{mod}\;3).

Now (3.115) yields

 | m ≡ s ( mod ​ 4 ​ s + 1). m\equiv s\quad(\mbox{mod}\;4s+1). |  | (3.127) |

Thus

 | m = s + c ⁡ ( 4 ​ s + 1) m=s+c(4s+1) |  | (3.128) |

for some c ∈ ℕ c\in\mathbb{N} and

 | 6 ​ m + j + 2 = 2 ​ ( 3 ​ m + s + 1) = 2 ​ ( 3 ​ c + 1) ​ ( 4 ​ s + 1). 6m+j+2=2(3m+s+1)=2(3c+1)(4s+1). |  | (3.129) |

By (3.122), the second expression in (2.28) implies

 | 5 | [2 ​ ( 3 ​ c + 1) ​ ( 4 ​ s + 1)] ⟹ 5 | ( 3 ​ c + 1). 5|[2(3c+1)(4s+1)]\Longrightarrow 5|(3c+1). |  | (3.130) |

Thus

 | c = 5 ​ d + 3 for some ​ d ∈ ℕ. c=5d+3\quad\mbox{for some}\;d\in\mathbb{N}. |  | (3.131) |

Now

 | m = s + ( 5 ​ d + 3) ​ ( 4 ​ s + 1) m=s+(5d+3)(4s+1) |  | (3.132) |

and

 | 6 ​ m + j + 2 = 10 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1). 6m+j+2=10(3d+2)(4s+1). |  | (3.133) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 10 ​ ( 4 ​ s + 1) ​ ( 3 ​ d + 2) + 2 ​ ( 4 ​ s + 1) + 5 10 ​ ( 4 ​ s + 1) ​ ( 3 ​ d + 2) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{10(4s+1)(3d+2)}+\frac{2(4s+1)+5}{10(4s+1)(3d+2)(24m+1)} |  | (3.134) |

 |  | = \displaystyle= | 1 10 ​ ( 4 ​ s + 1) ​ ( 3 ​ d + 2) + 1 5 ​ ( 3 ​ d + 2) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{10(4s+1)(3d+2)}+\frac{1}{5(3d+2)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 4 ​ s + 1) ​ ( 3 ​ d + 2) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(4s+1)(3d+2)(24m+1)}. |  |

Theorem 3.5 For any positive integer m m in (3.124), we have the tame solution (3.126) of the Erdös-Straus equation. If m m is of the form (3.132), then we have the tame solution (3.134) of the Erdös-Straus equation.

In (3.124), 4 ​ a + 3 = 3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103 4a+3=3,7,11,19,23,31,43,47,59,67,71,79,83,103 are primes when r = 0, 1, 2, 4, 5, 7, 10, 11, 14, 16, 17, 19, 20, 25 r=0,1,2,4,5,7,10,11,14,16,17,19,20,25, respectively. In (3.132), 4 ​ s + 1 = 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101 4s+1=5,13,17,29,37,41,\\ 53,61,73,89,97,101 are primes when s = 1, 3, 4, 7, 9, 10, 13, 15, 18, 22, 24, 25 s=1,3,4,7,9,10,13,15,18,22,24,25, respectively.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 14 ​ ( mod ​ 15) m\equiv 14\;(\mbox{mod}\;15) (cf. (3.124) with t = 0 t=0) are given by the following ( m, d) (m,d) (cf. (3.124) and (3.126)):

( 194, 12), ( 404, 26), ( 1064, 70), ( 1214, 80), ( 1394, 92), ( 1454, 96), ( 1844,122), ( 1904,120). (194,12),(404,26),(1064,70),(1214,80),(1394,92),(1454,96),(1844,122),(1904,120).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 52 ​ ( mod ​ 55) m\equiv 52\;(\mbox{mod}\;55) (cf. (3.124) with t = 2 t=2) are given by the following ( m, d) (m,d) (cf. (3.124) and (3.126)):

( 52, 0), ( 217, 3), ( 602, 10), ( 1482, 26), ( 1757, 31). (52,0),(217,3),(602,10),(1482,26),(1757,31).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 42 ​ ( mod ​ 65) m\equiv 42\;(\mbox{mod}\;65) (cf. (3.132) with s = 3 s=3) are given by the following ( m, d) (m,d) (cf. (3.132) and (3.134)): ( 1277, 19), ( 1667, 25) (1277,19),(1667,25).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 55 ​ ( mod ​ 85) m\equiv 55\;(\mbox{mod}\;85) (cf. (3.132) with s = 4 s=4) are given by the following ( m, d) (m,d) (cf. (3.132) and (3.134)): ( 140, 1), ( 820, 9), ( 990, 11) (140,1),(820,9),(990,11).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 90 ​ ( mod ​ 95) m\equiv 90\;(\mbox{mod}\;95) (cf. (3.124) with t = 4 t=4) are given by the following ( m, d) (m,d) (cf. (3.124) and (3.126)):

( 1135, 11), ( 1800, 18), ( 1895, 19). (1135,11),(1800,18),(1895,19).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 94 ​ ( mod ​ 145) m\equiv 94\;(\mbox{mod}\;145) (cf. (3.132) with s = 7 s=7) are given by the following ( m, d) (m,d) (cf. (3.132) and (3.134)): ( 1254, 8), ( 1834, 12) (1254,8),(1834,12).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 147 ​ ( mod ​ 155) m\equiv 147\;(\mbox{mod}\;155) (cf. (3.124) with t = 7 t=7) is given by the following ( m, d) (m,d) (cf. (3.124) and (3.126)): ( 147, 0) (147,0).

### 3.6 Case ℑ 2 = 6 \Im_{2}=6

In this case,

 | ℑ 1 = 4 ​ j + 1, k = j + 2 with ​ j ∈ ℕ \Im_{1}=4j+1,\quad k=j+2\quad\mbox{with}\;\;j\in\mathbb{N} |  | (3.135) |

by (2.13). Moreover,

 | 6 ​ m + k = 6 ​ m + j + 2 6m+k=6m+j+2 |  | (3.136) |

According the second expression in (2.28),

 | 6 | ( 6 ​ m + j + 2). 6|(6m+j+2). |  | (3.137) |

So

 | j = 6 ​ s + 4 for some ​ s ∈ ℕ. j=6s+4\quad\mbox{for some}\;s\in\mathbb{N}. |  | (3.138) |

Hence,

 | 4 ​ j + 1 = 24 ​ s + 17 4j+1=24s+17 |  | (3.139) |

and

 | 6 ​ m + j + 2 = 6 ​ ( m + s + 1). 6m+j+2=6(m+s+1). |  | (3.140) |

According to the first expression in (2.28),

 | ( 24 ​ s + 17) | 6 ​ ( m + s + 1) ⟹ ( 24 ​ s + 17) | ( m + s + 1); (24s+17)|6(m+s+1)\Longrightarrow(24s+17)|(m+s+1); |  | (3.141) |

that is,

 | m ≡ 23 ​ s + 16 ( mod ​ 24 ​ s + 17). m\equiv 23s+16\quad(\mbox{mod}\;24s+17). |  | (3.142) |

Under this condition,

 | m = 23 ​ s + 16 + c ⁡ ( 24 ​ s + 17) with ​ c ∈ ℕ m=23s+16+c(24s+17)\quad\mbox{with}\;\;c\in\mathbb{N} |  | (3.143) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ ( m + s + 1) = 6 ​ ( c + 1) ​ ( 24 ​ s + 17). 6m+j+\ell+1=6(m+s+1)=6(c+1)(24s+17). |  | (3.144) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 6 ​ ( c + 1) ​ ( 24 ​ s + 17) + ( 24 ​ s + 17) + 6 6 ​ ( c + 1) ​ ( 24 ​ s + 17) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6(c+1)(24s+17)}+\frac{(24s+17)+6}{6(c+1)(24s+17)(24m+1)} |  | (3.145) |

 |  | = \displaystyle= | 1 6 ​ c ​ ( 24 ​ s + 17) + 1 6 ​ ( c + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6c(24s+17)}+\frac{1}{6(c+1)(24m+1)} |  |

 |  |  | + 1 ( c + 1) ​ ( 24 ​ s + 17) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{(c+1)(24s+17)(24m+1)}.\qquad |  |

Theorem 3.6 For any positive integer m m in (3.143), we have the tame solution (3.145) of the Erdös-Straus equation.

In (3.143), 24 ​ s + 17 = 17, 41, 89, 103 24s+17=17,41,89,103 are primes when s = 0, 1, 3, 4 s=0,1,3,4, respectively.

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 16 ​ ( mod ​ 17) m\equiv 16\;(\mbox{mod}\;17) (cf. (3.143) with s = 0 s=0) are given by the following ( m, c) (m,c) (cf. (3.143) and (3.145)):

( 50, 2), ( 84, 4), ( 407, 23), ( 1002, 58), ( 1104, 64), ( 1597, 93), ( 1767,103). (50,2),(84,4),(407,23),(1002,58),(1104,64),(1597,93),(1767,103).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 39 ​ ( mod ​ 41) m\equiv 39\;(\mbox{mod}\;41) (cf. (3.143) with s = 1 s=1) are given by the following ( m, c) (m,c) (cf. (3.143) and (3.145)): ( 162, 3), ( 572, 13), ( 1720, 41). (162,3),(572,13),(1720,41).

Examples of the primes 24 ​ m + 1 24m+1 with m m satisfying m ≡ 62 ​ ( mod ​ 65) m\equiv 62\;(\mbox{mod}\;65) (cf. (3.143) with s = 2 s=2) are given by the following ( m, c) (m,c) (cf. (3.143) and (3.145)): ( 127, 1), ( 1232, 18). (127,1),(1232,18).

Example of the prime 24 ​ m + 1 24m+1 with m m satisfying m ≡ 522 ​ ( mod ​ 545) m\equiv 522\;(\mbox{mod}\;545) (cf. (3.143) with s = 22 s=22) is given by the following ( m, c) (m,c) (cf. (3.143) and (3.145)): ( 1067, 1). (1067,1).

## 4 Cases with the Numerator Summand ℑ 2 = 4 ​ ℓ + 1 \Im_{2}=4\ell+1

First we have

 | ℑ 1 = 4 j + 2, k = j + ℓ + 1 with j, ℓ ∈ ℕ \displaystyle\Im_{1}=4j+2,\quad k=j+\ell+1\quad\mbox{with}\;\;j,\ell\in\mathbb{N} |  | (4.1) |

and ℓ ≥ 2 \ell\geq 2 by (2.13). Moreover,

 | 6 ​ m + k = 6 ​ m + j + ℓ + 1. 6m+k=6m+j+\ell+1. |  | (4.2) |

According to the firs expression in (2.28),

 | 2 | ( 6 ​ m + j + ℓ + 1). 2|(6m+j+\ell+1). |  | (4.3) |

So

 | j + ℓ ≡ 1 ( mod ​ 2). j+\ell\equiv 1\quad(\mbox{mod}\;2). |  | (4.4) |

### 4.1 Case j = 6 ​ s j=6s and ℓ = 6 ​ t + 1 \ell=6t+1

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 1), ℑ 2 = 24 ​ t + 5 \Im_{1}=2(12s+1),\quad\Im_{2}=24t+5 |  | (4.5) |

by (4.1), and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ ( m + s + t) + 1)) 6m+j+\ell+1=2(3(m+s+t)+1)) |  | (4.6) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 1) | ( 3 ​ ( m + s + t) + 1); (12s+1)|(3(m+s+t)+1); |  | (4.7) |

that is,

 | 3 ​ ( m + s + t) + 1 ≡ 0 ( mod ​ 12 ​ s + 1). 3(m+s+t)+1\equiv 0\quad(\mbox{mod}\;12s+1). |  | (4.8) |

So

 | 3 ​ ( m + s + t) + 1 ≡ 12 ​ s + 1 ( mod ​ 12 ​ s + 1). 3(m+s+t)+1\equiv 12s+1\quad(\mbox{mod}\;12s+1). |  | (4.9) |

Equivalently,

 | 3 ​ ( m + t) ≡ 9 ​ s ( mod ​ 12 ​ s + 1). 3(m+t)\equiv 9s\quad(\mbox{mod}\;12s+1). |  | (4.10) |

So

 | m + t ≡ 3 ​ s ( mod ​ 12 ​ s + 1). m+t\equiv 3s\quad(\mbox{mod}\;12s+1). |  | (4.11) |

Under this condition,

 | m + t = 3 ​ s + c ⁡ ( 12 ​ s + 1) for some ​ c ∈ ℕ m+t=3s+c(12s+1)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.12) |

and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ c + 1) ​ ( 12 ​ s + 1)). 6m+j+\ell+1=2(3c+1)(12s+1)). |  | (4.13) |

According to the second expression in (2.28),

 | ( 24 ​ t + 5) | ( 3 ​ c + 1) ⟹ c = 16 ​ t + 3 + d ⁡ ( 24 ​ t + 5) for ​ d ∈ ℕ. (24t+5)|(3c+1)\Longrightarrow c=16t+3+d(24t+5)\quad\mbox{for}\;d\in\mathbb{N}. |  | (4.14) |

Now

 | m \displaystyle m | = \displaystyle= | 3 ​ s − t + ( 16 ​ t + 3 + d ⁡ ( 24 ​ t + 5)) ​ ( 12 ​ s + 1) \displaystyle 3s-t+(16t+3+d(24t+5))(12s+1) |  | (4.15) |

 |  | = \displaystyle= | 15 ​ t − s + 3 + [8 ​ s + d ⁡ ( 12 ​ s + 1)] ​ ( 24 ​ t + 5) \displaystyle 15t-s+3+[8s+d(12s+1)](24t+5) |  |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 5). 6m+j+\ell+1=2(3d+2)(12s+1)(24t+5). |  | (4.16) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 5) + 2 ​ ( 12 ​ s + 1) + ( 24 ​ t + 5) 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 5) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{2(3d+2)(12s+1)(24t+5)}+\frac{2(12s+1)+(24t+5)}{2(3d+2)(12s+1)(24t+5)(24m+1)} |  | (4.17) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 5) + 1 ( 3 ​ d + 2) ​ ( 24 ​ t + 5) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3d+2)(12s+1)(24t+5)}+\frac{1}{(3d+2)(24t+5)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3d+2)(12s+1)(24m+1)}. |  |

Theorem 4.1 For any positive integer m m in (4.15), we have the tame solution (4.17) of the Erdös-Straus equation.

Note that (4.15) with d ∈ ℕ d\in\mathbb{N} are the solution of the following system

 | m ≡ 3 ​ s − t ⁡ ( mod ​ 12 ​ s + 1), m ≡ 15 ​ t − s + 3 ​ ( mod ​ 24 ​ t + 5). m\equiv 3s-t\;\;(\mbox{mod}\>12s+1),\qquad m\equiv 15t-s+3\;\;(\mbox{mod}\>24t+5). |  | (4.18) |

Moreover, 12 ​ s + 1 = 13, 37, 61, 73, 97, 109 12s+1=13,37,61,73,97,109 are primes when s = 1, 3, 5, 6, 8, 9 s=1,3,5,6,8,9, respectively. Furthermore, 24 ​ t + 5 = 5, 29, 53, 101 24t+5=5,29,53,101 are primes when s = 0, 1, 2, 4 s=0,1,2,4, respectively.

Example 4.1.1 When m = 1302 m=1302, 24 ​ m + 1 = 31249 24m+1=31249 is a prime. Moreover, 1302 satisfies the above expression with s = 3 s=3 and t = 2 t=2. Moreover, (4.15) gives d = 0 d=0. Expression (4.17) yields

 | 4 31249 = 1 7844 + 1 3312394 + 1 4624852. \frac{4}{31249}=\frac{1}{7844}+\frac{1}{3312394}+\frac{1}{4624852}. |  | (4.19) |

### 4.2 Case j = 6 ​ s j=6s and ℓ = 6 ​ t + 3 \ell=6t+3

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 1), ℑ 2 = 24 ​ t + 13 \Im_{1}=2(12s+1),\quad\Im_{2}=24t+13 |  | (4.20) |

by (4.1), and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ ( m + s + t) + 2)) 6m+j+\ell+1=2(3(m+s+t)+2)) |  | (4.21) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 1) | ( 3 ​ ( m + s + t) + 2); (12s+1)|(3(m+s+t)+2); |  | (4.22) |

that is,

 | 3 ​ ( m + s + t) + 2 ≡ 0 ( mod ​ 12 ​ s + 1). 3(m+s+t)+2\equiv 0\quad(\mbox{mod}\;12s+1). |  | (4.23) |

So

 | 3 ​ ( m + s + t) + 2 ≡ 2 ​ ( 12 ​ s + 1) ( mod ​ 12 ​ s + 1). 3(m+s+t)+2\equiv 2(12s+1)\quad(\mbox{mod}\;12s+1). |  | (4.24) |

Equivalently,

 | 3 ​ ( m + t) ≡ 21 ​ s ( mod ​ 12 ​ s + 1). 3(m+t)\equiv 21s\quad(\mbox{mod}\;12s+1). |  | (4.25) |

Hence

 | m + t ≡ 7 ​ s ( mod ​ 12 ​ s + 1). m+t\equiv 7s\quad(\mbox{mod}\;12s+1). |  | (4.26) |

Under this condition,

 | m + t = 7 ​ s + c ⁡ ( 12 ​ s + 1) for some ​ c ∈ ℕ m+t=7s+c(12s+1)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.27) |

and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ c + 2) ​ ( 12 ​ s + 1)). 6m+j+\ell+1=2(3c+2)(12s+1)). |  | (4.28) |

According to the second expression in (2.28),

 | ( 24 ​ t + 13) | ( 3 ​ c + 2) ⟹ c = 16 ​ t + 8 + d ⁡ ( 24 ​ t + 13) for ​ d ∈ ℕ. (24t+13)|(3c+2)\Longrightarrow c=16t+8+d(24t+13)\quad\mbox{for}\;d\in\mathbb{N}. |  | (4.29) |

Now

 | m \displaystyle m | = \displaystyle= | 7 ​ s − t + ( 16 ​ t + 8 + d ⁡ ( 24 ​ t + 13)) ​ ( 12 ​ s + 1) \displaystyle 7s-t+(16t+8+d(24t+13))(12s+1) |  | (4.30) |

 |  | = \displaystyle= | 15 ​ t − s + 8 + [d ⁡ ( 12 ​ s + 1) + 8 ​ s] ​ ( 24 ​ t + 13) \displaystyle 15t-s+8+[d(12s+1)+8s](24t+13) |  |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 13). 6m+j+\ell+1=2(3d+2)(12s+1)(24t+13). |  | (4.31) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 13) + 2 ​ ( 12 ​ s + 1) + ( 24 ​ t + 13) 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 13) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{2(3d+2)(12s+1)(24t+13)}+\frac{2(12s+1)+(24t+13)}{2(3d+2)(12s+1)(24t+13)(24m+1)} |  | (4.32) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ t + 13) + 1 ( 3 ​ d + 2) ​ ( 24 ​ t + 13) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3d+2)(12s+1)(24t+13)}+\frac{1}{(3d+2)(24t+13)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3d+2)(12s+1)(24m+1)}. |  |

Theorem 4.2 For any positive integer m m in (4.30), we have the tame solution (4.32) of the Erdös-Straus equation.

Note that (4.30) with d ∈ ℕ d\in\mathbb{N} are the solution of the following system

 | m ≡ 7 ​ s − t ⁡ ( mod ​ 12 ​ s + 1), m ≡ 15 ​ t − s + 8 ​ ( mod ​ 24 ​ t + 13). m\equiv 7s-t\;\;(\mbox{mod}\>12s+1),\qquad m\equiv 15t-s+8\;\;(\mbox{mod}\>24t+13). |  | (4.33) |

Example 4.2.1 When m = 525 m=525, 24 ​ m + 1 = 12601 24m+1=12601 is a prime. Moreover, 525 satisfies the above expression with s = 1 s=1 and t = 2 t=2:

 | 525 ≡ 5 ​ ( mod ​ 13), 525 ≡ 37 ​ ( mod ​ 61). 525\equiv 5\;\;(\mbox{mod}\>13),\qquad 525\equiv 37\;\;(\mbox{mod}\>61). |  | (4.34) |

According to (4.30),

 | 525 = 5 + ( 40 + 61 ​ d) × 13 ⟹ d = 0. 525=5+(40+61d)\times 13\Longrightarrow d=0. |  | (4.35) |

Expression (4.32) yields

 | 4 12601 = 1 3172 + 1 1537322 + 1 655252. \frac{4}{12601}=\frac{1}{3172}+\frac{1}{1537322}+\frac{1}{655252}. |  | (4.36) |

### 4.3 Case j = 6 ​ s j=6s and ℓ = 6 ​ t + 5 \ell=6t+5

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 1), ℑ 2 = 24 ​ t + 21 = 3 ​ ( 8 ​ t + 7) \Im_{1}=2(12s+1),\quad\Im_{2}=24t+21=3(8t+7) |  | (4.37) |

by (4.1), and

 | 6 ​ m + j + ℓ + 1 = 6 ​ ( m + s + t + 1) 6m+j+\ell+1=6(m+s+t+1) |  | (4.38) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 1) | ( m + s + t + 1); (12s+1)|(m+s+t+1); |  | (4.39) |

that is,

 | m = − s − t − 1 + c ⁡ ( 12 ​ s + 1) for some ​ c ∈ ℕ. m=-s-t-1+c(12s+1)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (4.40) |

Moreover,

 | 6 ​ m + j + ℓ + 1 = 6 ​ c ​ ( 12 ​ s + 1). 6m+j+\ell+1=6c(12s+1). |  | (4.41) |

According to the second expression in (2.28),

 | ( 24 ​ t + 21) | [6 ​ c ​ ( 12 ​ s + 1)] ⟹ ( 8 ​ t + 7) | c ⟹ c = d ⁡ ( 8 ​ t + 7) (24t+21)|[6c(12s+1)]\Longrightarrow(8t+7)|c\Longrightarrow c=d(8t+7) |  | (4.42) |

for some d ∈ ℕ d\in\mathbb{N}. Thus

 | m = − s − t − 1 + d ⁡ ( 12 ​ s + 1) ​ ( 8 ​ t + 7) m=-s-t-1+d(12s+1)(8t+7) |  | (4.43) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ d ​ ( 12 ​ s + 1) ​ ( 8 ​ t + 7). 6m+j+\ell+1=6d(12s+1)(8t+7). |  | (4.44) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 6 ​ d ​ ( 12 ​ s + 1) ​ ( 8 ​ t + 7) + 2 ​ ( 12 ​ s + 1) + 3 ​ ( 8 ​ t + 7) 6 ​ d ​ ( 12 ​ s + 1) ​ ( 8 ​ t + 7) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{6d(12s+1)(8t+7)}+\frac{2(12s+1)+3(8t+7)}{6d(12s+1)(8t+7)(24m+1)} |  | (4.45) |

 |  | = \displaystyle= | 1 6 ​ d ​ ( 12 ​ s + 1) ​ ( 8 ​ t + 7) + 1 3 ​ d ​ ( 8 ​ t + 7) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6d(12s+1)(8t+7)}+\frac{1}{3d(8t+7)(24m+1)} |  |

 |  |  | + 1 2 ​ d ​ ( 12 ​ s + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2d(12s+1)(24m+1)}. |  |

Theorem 4.3 If

 | m ≡ − s − t − 1 ( mod ​ ( 12 ​ s + 1) ​ ( 8 ​ t + 7)), m\equiv-s-t-1\quad(\mbox{mod}\;(12s+1)(8t+7)), |  | (4.46) |

then the Erdö-Straus equation (4.45) holds.

Example 4.3.1 Let m = 635 m=635. Then 24 ​ m + 1 = 15241 24m+1=15241 is a prime. Moreover, (4.43) holds with s = 1 s=1 and t = 0 t=0. In fact

 | 635 = − 2 + 91 ​ d ⟹ d = 7. 635=-2+91d\Longrightarrow d=7. |  | (4.47) |

Equation (4.45) implies

 | 4 15241 = 1 3822 + 1 2240427 + 1 2273862. \frac{4}{15241}=\frac{1}{3822}+\frac{1}{2240427}+\frac{1}{2273862}. |  | (4.48) |

Example 4.3.2 Let m = 810 m=810. Then 24 ​ m + 1 = 19441 24m+1=19441 is a prime. Moreover, (4.39) holds with s = 1 s=1 and t = 7 t=7. In fact

 | 810 = − 9 + 13 × 63 ​ d ⟹ d = 1 810=-9+13\times 63d\Longrightarrow d=1 |  | (4.49) |

Equation (4.45) implies

 | 4 19441 = 1 4914 + 1 3674349 + 1 505466. \frac{4}{19441}=\frac{1}{4914}+\frac{1}{3674349}+\frac{1}{505466}. |  | (4.50) |

Example 4.3.3 Let m = 817 m=817. Then 24 ​ m + 1 = 19609 24m+1=19609 is a prime. Moreover, (4.39) holds with s = 1 s=1 and t = 0 t=0. In fact

 | 817 = − 2 + 91 ​ d ⟹ d = 9 817=-2+91d\Longrightarrow d=9 |  | (4.51) |

Equation (4.45) implies

 | 4 19609 = 1 4914 + 1 3706101 + 1 4588506. \frac{4}{19609}=\frac{1}{4914}+\frac{1}{3706101}+\frac{1}{4588506}. |  | (4.52) |

### 4.4 Case j = 6 ​ s + 2 j=6s+2 and ℓ = 6 ​ t + 1 \ell=6t+1

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 5), ℑ 2 = 24 ​ t + 5 \Im_{1}=2(12s+5),\quad\Im_{2}=24t+5 |  | (4.53) |

by (4.1), and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ ( m + s + t) + 2) 6m+j+\ell+1=2(3(m+s+t)+2) |  | (4.54) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 5) | ( 3 ​ ( m + s + t) + 2); (12s+5)|(3(m+s+t)+2); |  | (4.55) |

that is,

 | 3 ​ ( m + s + t) + 2 ≡ 0 ( mod ​ 12 ​ s + 5). 3(m+s+t)+2\equiv 0\quad(\mbox{mod}\;12s+5). |  | (4.56) |

Equivalently,

 | 3 ​ ( m + s + t) + 2 ≡ 12 ​ s + 5 ( mod ​ 12 ​ s + 5). 3(m+s+t)+2\equiv 12s+5\quad(\mbox{mod}\;12s+5). |  | (4.57) |

Thus

 | m = 3 ​ s − t + 1 + c ⁡ ( 12 ​ s + 5) for some ​ c ∈ ℕ. m=3s-t+1+c(12s+5)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (4.58) |

Moreover,

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ c + 1) ​ ( 12 ​ s + 5). 6m+j+\ell+1=2(3c+1)(12s+5). |  | (4.59) |

According to the second expression in (2.28) and (3.122),

 | ( 24 ​ t + 5) | ( 3 ​ c + 1) ⟹ c = 16 ​ t + 3 + d ⁡ ( 24 ​ t + 5) (24t+5)|(3c+1)\Longrightarrow c=16t+3+d(24t+5) |  | (4.60) |

for some d ∈ ℕ d\in\mathbb{N}. Thus

 | m \displaystyle m | = \displaystyle= | 3 ​ s − t + 1 + ( 16 ​ t + 3 + d ⁡ ( 24 ​ t + 5)) ​ ( 12 ​ s + 5) \displaystyle 3s-t+1+(16t+3+d(24t+5))(12s+5) |  | (4.61) |

 |  | = \displaystyle= | − s + 7 ​ t + 1 + ( 8 ​ s + 3 + d ⁡ ( 12 ​ s + 5)) ​ ( 24 ​ t + 5). \displaystyle-s+7t+1+(8s+3+d(12s+5))(24t+5). |  |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 5). 6m+j+\ell+1=2(3d+2)(12s+5)(24t+5). |  | (4.62) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 5) + 2 ​ ( 12 ​ s + 5) + ( 24 ​ t + 5) 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 5) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{2(3d+2)(12s+5)(24t+5)}+\frac{2(12s+5)+(24t+5)}{2(3d+2)(12s+5)(24t+5)(24m+1)} |  | (4.63) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 5) + 1 ( 3 ​ d + 2) ​ ( 24 ​ t + 5) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3d+2)(12s+5)(24t+5)}+\frac{1}{(3d+2)(24t+5)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 5) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3d+2)(12s+5)(24m+1)}. |  |

Theorem 4.4 For the positive integer m m in (4.61), we have the Erdö-Straus equation (4.63).

Example 4.4.1 Let m = 1764 m=1764. Then 24 ​ m + 1 = 42337 24m+1=42337 is a prime. Moreover, (4.58) holds with s = 0 s=0 and t = 2 t=2. In fact, (4.61) gives

 | 1764 = 174 + 265 ​ d ⟹ d = 6. 1764=174+265d\Longrightarrow d=6. |  | (4.64) |

Equation (4.63) implies

 | 4 42337 = 1 10600 + 1 44877220 + 1 8457400. \frac{4}{42337}=\frac{1}{10600}+\frac{1}{44877220}+\frac{1}{8457400}. |  | (4.65) |

### 4.5 Case j = 6 ​ s + 2 j=6s+2 and ℓ = 6 ​ t + 3 \ell=6t+3

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 5), ℑ 2 = 24 ​ t + 13 \Im_{1}=2(12s+5),\quad\Im_{2}=24t+13 |  | (4.66) |

by (4.1), and

 | 6 ​ m + j + ℓ + 1 = 6 ​ ( m + s + t + 1) 6m+j+\ell+1=6(m+s+t+1) |  | (4.67) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 5) | ( m + s + t + 1); (12s+5)|(m+s+t+1); |  | (4.68) |

that is,

 | m = − s − t − 1 + c ⁡ ( 12 ​ s + 5) for some ​ c ∈ ℕ. m=-s-t-1+c(12s+5)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (4.69) |

Moreover,

 | 6 ​ m + j + ℓ + 1 = 6 ​ c ​ ( 12 ​ s + 5). 6m+j+\ell+1=6c(12s+5). |  | (4.70) |

According to the second expression in (2.28),

 | ( 24 ​ t + 13) | c ⟹ c = d ⁡ ( 24 ​ t + 13) (24t+13)|c\Longrightarrow c=d(24t+13) |  | (4.71) |

for some d ∈ ℕ d\in\mathbb{N}. Thus

 | m = − s − t − 1 + d ⁡ ( 12 ​ s + 5) ​ ( 24 ​ t + 13) m=-s-t-1+d(12s+5)(24t+13) |  | (4.72) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ d ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 13). 6m+j+\ell+1=6d(12s+5)(24t+13). |  | (4.73) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 6 ​ d ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 13) + 2 ​ ( 12 ​ s + 5) + ( 24 ​ t + 13) 6 ​ d ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 13) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{6d(12s+5)(24t+13)}+\frac{2(12s+5)+(24t+13)}{6d(12s+5)(24t+13)(24m+1)} |  | (4.74) |

 |  | = \displaystyle= | 1 6 ​ d ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 13) + 1 3 ​ d ​ ( 24 ​ t + 13) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6d(12s+5)(24t+13)}+\frac{1}{3d(24t+13)(24m+1)} |  |

 |  |  | + 1 6 ​ d ​ ( 12 ​ s + 5) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{6d(12s+5)(24m+1)}. |  |

Theorem 4.5 If

 | m ≡ − s − t − 1 ( mod ​ ( 12 ​ s + 5) ​ ( 24 ​ t + 13)), m\equiv-s-t-1\quad(\mbox{mod}\;(12s+5)(24t+13)), |  | (4.75) |

then the Erdö-Straus equation (4.74) holds.

Example 4.5.1 Let m = 882 m=882. Then 24 ​ m + 1 = 21169 24m+1=21169 is a prime. Moreover, the above equation holds with s = 1 s=1 and t = 0 t=0. In fact, (4.72) gives

 | 882 = − 2 + 221 ​ d ⟹ d = 4 882=-2+221d\Longrightarrow d=4 |  | (4.76) |

Equation (4.74) implies

 | 4 21169 = 1 5304 + 1 3302364 + 1 8636952. \frac{4}{21169}=\frac{1}{5304}+\frac{1}{3302364}+\frac{1}{8636952}. |  | (4.77) |

Example 4.5.2 Let m = 1522 m=1522. Then 24 ​ m + 1 = 36529 24m+1=36529 is a prime. Moreover, (4.75) holds with s = 0 s=0 and t = 2 t=2. In fact, (4.72) gives

 | 1522 = − 3 + 305 ​ d ⟹ d = 6 1522=-3+305d\Longrightarrow d=6 |  | (4.78) |

Equation (4.74) implies

 | 4 36529 = 1 10980 + 1 40108842 + 1 6575220. \frac{4}{36529}=\frac{1}{10980}+\frac{1}{40108842}+\frac{1}{6575220}. |  | (4.79) |

### 4.6 Case j = 6 ​ s + 3 j=6s+3 and ℓ = 6 ​ t \ell=6t

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 7), ℑ 2 = 24 ​ t + 1 \Im_{1}=2(12s+7),\quad\Im_{2}=24t+1 |  | (4.80) |

by (4.1), and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ ( m + s + t) + 2)) 6m+j+\ell+1=2(3(m+s+t)+2)) |  | (4.81) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 7) | ( 3 ​ ( m + s + t) + 2); (12s+7)|(3(m+s+t)+2); |  | (4.82) |

that is,

 | 3 ​ ( m + s + t) + 2 ≡ 0 ( mod ​ 12 ​ s + 7). 3(m+s+t)+2\equiv 0\quad(\mbox{mod}\;12s+7). |  | (4.83) |

So

 | 3 ​ ( m + s + t) + 2 ≡ 2 ​ ( 12 ​ s + 7) ( mod ​ 12 ​ s + 7). 3(m+s+t)+2\equiv 2(12s+7)\quad(\mbox{mod}\;12s+7). |  | (4.84) |

Equivalently,

 | 3 ​ ( m + t) ≡ 21 ​ s + 12 ( mod ​ 12 ​ s + 7). 3(m+t)\equiv 21s+12\quad(\mbox{mod}\;12s+7). |  | (4.85) |

So

 | m + t ≡ 7 ​ s + 4 ( mod ​ 12 ​ s + 7). m+t\equiv 7s+4\quad(\mbox{mod}\;12s+7). |  | (4.86) |

Under this condition,

 | m + t = 7 ​ s + 4 + c ⁡ ( 12 ​ s + 7) for some ​ c ∈ ℕ m+t=7s+4+c(12s+7)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.87) |

and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ c + 2) ​ ( 12 ​ s + 7)). 6m+j+\ell+1=2(3c+2)(12s+7)). |  | (4.88) |

The second expression in (2.28) implies

 | ( 24 ​ t + 1) | ( 3 ​ c + 2) ⟹ c = 16 ​ t + d ⁡ ( 24 ​ t + 1) for ​ d ∈ ℕ. (24t+1)|(3c+2)\Longrightarrow c=16t+d(24t+1)\quad\mbox{for}\;d\in\mathbb{N}. |  | (4.89) |

Now

 | m \displaystyle m | = \displaystyle= | 7 ​ s − t + 4 + ( 16 ​ t + d ⁡ ( 24 ​ t + 1)) ​ ( 12 ​ s + 7) \displaystyle 7s-t+4+(16t+d(24t+1))(12s+7) |  | (4.90) |

 |  | = \displaystyle= | 15 ​ t − s + 7 + [d ⁡ ( 12 ​ s + 1) + 8 ​ s + 4] ​ ( 24 ​ t + 1) \displaystyle 15t-s+7+[d(12s+1)+8s+4](24t+1) |  |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 1). 6m+j+\ell+1=2(3d+2)(12s+7)(24t+1). |  | (4.91) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 1) + 2 ​ ( 12 ​ s + 7) + ( 24 ​ t + 1) 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{2(3d+2)(12s+7)(24t+1)}+\frac{2(12s+7)+(24t+1)}{2(3d+2)(12s+7)(24t+1)(24m+1)} |  | (4.92) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 1) + 1 ( 3 ​ d + 2) ​ ( 24 ​ t + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3d+2)(12s+7)(24t+1)}+\frac{1}{(3d+2)(24t+1)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3d+2)(12s+7)(24m+1)}. |  |

Theorem 4.6 For any positive integer m m in (4.90), we have the tame solution (4.92) of the Erdös-Straus equation.

Note that (4.90) with d ∈ ℕ d\in\mathbb{N} are the solution of the following system

 | m ≡ 7 ​ s − t + 4 ​ ( mod ​ 12 ​ s + 7), m ≡ 15 ​ t − s + 7 ​ ( mod ​ 24 ​ t + 1). m\equiv 7s-t+4\;\;(\mbox{mod}\>12s+7),\qquad m\equiv 15t-s+7\;\;(\mbox{mod}\>24t+1). |  | (4.93) |

Furthermore, 24 ​ t + 1 = 73, 97, 193 24t+1=73,97,193 are primes when t = 3, 4, 8 t=3,4,8, respectively.

### 4.7 Case j = 6 ​ s + 3 j=6s+3 and ℓ = 6 ​ t + 2 \ell=6t+2

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 7), ℑ 2 = 24 ​ t + 9 = 3 ​ ( 8 ​ t + 3) \Im_{1}=2(12s+7),\quad\Im_{2}=24t+9=3(8t+3) |  | (4.94) |

by (4.1), and

 | 6 ​ m + j + ℓ + 1 = 6 ​ ( m + s + t + 1) 6m+j+\ell+1=6(m+s+t+1) |  | (4.95) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 7) | ( m + s + t + 1); (12s+7)|(m+s+t+1); |  | (4.96) |

that is,

 | m + s + t + 1 ≡ 0 ( mod ​ 12 ​ s + 7). m+s+t+1\equiv 0\quad(\mbox{mod}\;12s+7). |  | (4.97) |

So

 | m + t ≡ 11 ​ s + 6 ( mod ​ 12 ​ s + 7). m+t\equiv 11s+6\quad(\mbox{mod}\;12s+7). |  | (4.98) |

Under this condition,

 | m + t = 11 ​ s + 6 + c ⁡ ( 12 ​ s + 7) for some ​ c ∈ ℕ m+t=11s+6+c(12s+7)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.99) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ ( c + 1) ​ ( 12 ​ s + 7). 6m+j+\ell+1=6(c+1)(12s+7). |  | (4.100) |

The second expression in (2.28) implies

 | ( 8 ​ t + 3) | ( c + 1). (8t+3)|(c+1). |  | (4.101) |

Thus

 | c = d ⁡ ( 8 ​ t + 3) − 1 for ​ 0 < d ∈ ℕ. c=d(8t+3)-1\quad\mbox{for}\;\;0<d\in\mathbb{N}. |  | (4.102) |

Now

 | m = − t − s − 1 + d ⁡ ( 12 ​ s + 7) ​ ( 8 ​ t + 3) m=-t-s-1+d(12s+7)(8t+3) |  | (4.103) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ d ​ ( 12 ​ s + 7) ​ ( 8 ​ t + 3). 6m+j+\ell+1=6d(12s+7)(8t+3). |  | (4.104) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 6 ​ d ​ ( 12 ​ s + 7) ​ ( 8 ​ t + 3) + 2 ​ ( 12 ​ s + 7) + 3 ​ ( 8 ​ t + 3) 6 ​ d ​ ( 12 ​ s + 7) ​ ( 8 ​ t + 3) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6d(12s+7)(8t+3)}+\frac{2(12s+7)+3(8t+3)}{6d(12s+7)(8t+3)(24m+1)} |  | (4.105) |

 |  | = \displaystyle= | 1 6 ​ d ​ ( 12 ​ s + 7) ​ ( 8 ​ t + 3) + 1 3 ​ d ​ ( 8 ​ t + 3) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{6d(12s+7)(8t+3)}+\frac{1}{3d(8t+3)(24m+1)} |  |

 |  |  | + 1 2 ​ d ​ ( 12 ​ s + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2d(12s+7)(24m+1)}. |  |

Theorem 4.7 For any positive integer m m in (4.103), we have the tame solution (4.105) of the Erdös-Straus equation.

Note that (4.103) with d ∈ ℕ d\in\mathbb{N} are the solution of the following equation

 | m ≡ − s − t − 1 ​ ( mod ​ ( 12 ​ s + 7) ​ ( 8 ​ t + 3)). m\equiv-s-t-1\;\;(\mbox{mod}\>(12s+7)(8t+3)). |  | (4.106) |

Moreover, 8 ​ t + 3 = 3, 11, 19, 43, 59, 67, 83 8t+3=3,11,19,43,59,67,83 are primes when t = 0, 1, 2, 5, 7, 10 t=0,1,2,5,7,10, respectively.

Example 4.7.1 Let m = 897 m=897. Then 24 ​ m + 1 = 21529 24m+1=21529 is a prime. Moreover, (4.106) holds with s = 0 s=0 and t = 5 t=5. In fact, (4.103) gives

 | 897 = − 6 + 301 ​ d ⟹ d = 3 897=-6+301d\Longrightarrow d=3 |  | (4.107) |

Equation (4.105) implies

 | 4 21529 = 1 5418 + 1 8331723 + 1 904218. \frac{4}{21529}=\frac{1}{5418}+\frac{1}{8331723}+\frac{1}{904218}. |  | (4.108) |

Example 4.7.2 Let m = 1480 m=1480. Then 24 ​ m + 1 = 35521 24m+1=35521 is a prime. Moreover, (4.106) holds with s = 1 s=1 and t = 0 t=0. In fact, (4.103) gives

 | 1480 = − 2 + 57 ​ d ⟹ d = 26 1480=-2+57d\Longrightarrow d=26 |  | (4.109) |

Equation (4.105) implies

 | 4 35521 = 1 8892 + 1 8311914 + 1 35094748. \frac{4}{35521}=\frac{1}{8892}+\frac{1}{8311914}+\frac{1}{35094748}. |  | (4.110) |

### 4.8 Case j = 6 ​ s + 3 j=6s+3 and ℓ = 6 ​ t + 4 \ell=6t+4

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 7), ℑ 2 = 24 ​ t + 17 \Im_{1}=2(12s+7),\quad\Im_{2}=24t+17 |  | (4.111) |

by (4.1), and

 | OPEN 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ ( m + s + t) + 4)) 6m+j+\ell+1=2(3(m+s+t)+4)) |  | (4.112) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 7) | ( 3 ​ ( m + s + t) + 4); (12s+7)|(3(m+s+t)+4); |  | (4.113) |

that is,

 | 3 ​ ( m + s + t) + 4 ≡ 0 ( mod ​ 12 ​ s + 7). 3(m+s+t)+4\equiv 0\quad(\mbox{mod}\;12s+7). |  | (4.114) |

So

 | 3 ​ ( m + s + t) + 4 ≡ 12 ​ s + 7 ( mod ​ 12 ​ s + 7). 3(m+s+t)+4\equiv 12s+7\quad(\mbox{mod}\;12s+7). |  | (4.115) |

Equivalently,

 | 3 ​ ( m + t) ≡ 9 ​ s + 3 ( mod ​ 12 ​ s + 7). 3(m+t)\equiv 9s+3\quad(\mbox{mod}\;12s+7). |  | (4.116) |

So

 | m + t ≡ 3 ​ s + 1 ( mod ​ 12 ​ s + 7). m+t\equiv 3s+1\quad(\mbox{mod}\;12s+7). |  | (4.117) |

Under this condition,

 | m + t = 3 ​ s + 1 + c ⁡ ( 12 ​ s + 7) for some ​ c ∈ ℕ m+t=3s+1+c(12s+7)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.118) |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ c + 1) ​ ( 12 ​ s + 7). 6m+j+\ell+1=2(3c+1)(12s+7). |  | (4.119) |

According to the second expression in (2.28),

 | ( 24 ​ t + 17) | ( 3 ​ c + 1) ⟹ c = 16 ​ t + 11 + d ⁡ ( 24 ​ t + 17) for ​ d ∈ ℕ. (24t+17)|(3c+1)\Longrightarrow c=16t+11+d(24t+17)\quad\mbox{for}\;d\in\mathbb{N}. |  | (4.120) |

Now

 | m \displaystyle m | = \displaystyle= | 3 ​ s + 1 − t + ( 16 ​ t + 11 + d ⁡ ( 24 ​ t + 17)) ​ ( 12 ​ s + 7) \displaystyle 3s+1-t+(16t+11+d(24t+17))(12s+7) |  | (4.121) |

 |  | = \displaystyle= | 15 ​ t − s + 10 + [d ⁡ ( 12 ​ s + 7) + 8 ​ s + 4] ​ ( 24 ​ t + 17) \displaystyle 15t-s+10+[d(12s+7)+8s+4](24t+17) |  |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 17). 6m+j+\ell+1=2(3d+2)(12s+7)(24t+17). |  | (4.122) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 17) + 2 ​ ( 12 ​ s + 7) + ( 24 ​ t + 17) 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 17) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{2(3d+2)(12s+7)(24t+17)}+\frac{2(12s+7)+(24t+17)}{2(3d+2)(12s+7)(24t+17)(24m+1)} |  | (4.123) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ t + 17) + 1 ( 3 ​ d + 2) ​ ( 24 ​ t + 17) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3d+2)(12s+7)(24t+17)}+\frac{1}{(3d+2)(24t+17)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3d+2)(12s+7)(24m+1)}. |  |

Theorem 4.8 For any positive integer m m in (4.121), we have the tame solution (4.123) of the Erdös-Straus equation.

Note that (4.121) with d ∈ ℕ d\in\mathbb{N} are the solution of the following system

 | m ≡ 3 ​ s + 1 − t ⁡ ( mod ​ 12 ​ s + 7), m ≡ 15 ​ t − s + 10 ​ ( mod ​ 24 ​ t + 17). m\equiv 3s+1-t\;\;(\mbox{mod}\>12s+7),\qquad m\equiv 15t-s+10\;\;(\mbox{mod}\>24t+17). |  | (4.124) |

Example 4.8.1 Let m = 792 m=792. Then 24 ​ m + 1 = 19009 24m+1=19009 is a prime. Moreover, (4.124) holds with s = t = 0 s=t=0. In fact, (4.121) gives

 | 792 = 1 + 7 ​ ( 11 + 17 ​ d) ⟹ 113 = 11 + 17 ​ d ⟹ d = 6. 792=1+7(11+17d)\Longrightarrow 113=11+17d\Longrightarrow d=6. |  | (4.125) |

Equation (4.123) implies

 | 4 19009 = 1 4760 + 1 6463060 + 1 5322520. \frac{4}{19009}=\frac{1}{4760}+\frac{1}{6463060}+\frac{1}{5322520}. |  | (4.126) |

Example 4.8.2 Let m = 1657 m=1657. Then 24 ​ m + 1 = 39769 24m+1=39769 is a prime. Moreover, (4.124) holds with s = 0 s=0 and t = 3 t=3. In fact, (4.121) gives

 | 1657 = − 2 + 7 ​ ( 59 + 89 ​ d) ⟹ 237 = 59 + 89 ​ d ⟹ d = 2. 1657=-2+7(59+89d)\Longrightarrow 237=59+89d\Longrightarrow d=2. |  | (4.127) |

Equation (4.123) implies

 | 4 39769 = 1 9968 + 1 28315528 + 1 4454128. \frac{4}{39769}=\frac{1}{9968}+\frac{1}{28315528}+\frac{1}{4454128}. |  | (4.128) |

### 4.9 Case j = 6 ​ s + 5 j=6s+5 and ℓ = 6 ​ t \ell=6t

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 11), ℑ 2 = 24 ​ t + 1 \Im_{1}=2(12s+11),\quad\Im_{2}=24t+1 |  | (4.129) |

by (4.1), and

 | 6 ​ m + j + ℓ + 1 = 6 ​ ( m + s + t + 1) 6m+j+\ell+1=6(m+s+t+1) |  | (4.130) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 11) | ( m + s + t + 1); (12s+11)|(m+s+t+1); |  | (4.131) |

that is,

 | m + s + t + 1 ≡ 0 ( mod ​ 12 ​ s + 11). m+s+t+1\equiv 0\quad(\mbox{mod}\;12s+11). |  | (4.132) |

So

 | m ≡ − s − t − 1 ( mod ​ 12 ​ s + 11). m\equiv-s-t-1\quad(\mbox{mod}\;12s+11). |  | (4.133) |

Under this condition,

 | m = − s − t − 1 + c ⁡ ( 12 ​ s + 11) for some ​ c ∈ ℕ m=-s-t-1+c(12s+11)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.134) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ c ​ ( 12 ​ s + 11). 6m+j+\ell+1=6c(12s+11). |  | (4.135) |

The second expression in (2.28) implies

 | ( 24 ​ t + 1) | c ⟹ c = d ⁡ ( 24 ​ t + 1) for ​ 0 < d ∈ ℕ. (24t+1)|c\Longrightarrow c=d(24t+1)\quad\mbox{for}\;0<d\in\mathbb{N}. |  | (4.136) |

Now

 | OPEN m = − s − t − 1 + d ⁡ ( 24 ​ t + 1)) ​ ( 12 ​ s + 11). m=-s-t-1+d(24t+1))(12s+11). |  | (4.137) |

and

 | 6 ​ m + j + ℓ + 1 = 6 ​ d ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 1). 6m+j+\ell+1=6d(12s+11)(24t+1). |  | (4.138) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 6 ​ d ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 1) + 2 ​ ( 12 ​ s + 11) + ( 24 ​ t + 1) 6 ​ d ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{6d(12s+11)(24t+1)}+\frac{2(12s+11)+(24t+1)}{6d(12s+11)(24t+1)(24m+1)} |  | (4.139) |

 |  | = \displaystyle= | 1 d ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 1) + 1 3 ​ d ​ ( 24 ​ t + 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{d(12s+11)(24t+1)}+\frac{1}{3d(24t+1)(24m+1)} |  |

 |  |  | + 1 6 ​ d ​ ( 12 ​ s + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{6d(12s+11)(24m+1)}. |  |

Theorem 4.9 For any positive integer m m in (4.137), we have the tame solution (4.139) of the Erdös-Straus equation.

Note that (4.137) is equivalent to

 | m ≡ − s − t − 1 ( mod ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 1)). m\equiv-s-t-1\quad(\mbox{mod}\;(12s+11)(24t+1)). |  | (4.140) |

### 4.10 Case j = 6 ​ s + 5 j=6s+5 and ℓ = 6 ​ t + 4 \ell=6t+4

In this case,

 | ℑ 1 = 2 ​ ( 12 ​ s + 11), ℑ 2 = 24 ​ t + 17 \Im_{1}=2(12s+11),\quad\Im_{2}=24t+17 |  | (4.141) |

by (4.1), and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ ( m + s + t) + 5) 6m+j+\ell+1=2(3(m+s+t)+5) |  | (4.142) |

According to the firs expression in (2.28),

 | ( 12 ​ s + 11) | ( 3 ​ ( m + s + t) + 5); (12s+11)|(3(m+s+t)+5); |  | (4.143) |

that is,

 | 3 ​ ( m + s + t) + 5 ≡ 0 ( mod ​ 12 ​ s + 11). 3(m+s+t)+5\equiv 0\quad(\mbox{mod}\;12s+11). |  | (4.144) |

So

 | 3 ​ ( m + s + t) + 5 ≡ 12 ​ s + 11 ( mod ​ 12 ​ s + 11). 3(m+s+t)+5\equiv 12s+11\quad(\mbox{mod}\;12s+11). |  | (4.145) |

Equivalently,

 | 3 ​ ( m + t) ≡ 9 ​ s + 6 ( mod ​ 12 ​ s + 11). 3(m+t)\equiv 9s+6\quad(\mbox{mod}\;12s+11). |  | (4.146) |

So

 | m + t ≡ 3 ​ s + 2 ( mod ​ 12 ​ s + 11). m+t\equiv 3s+2\quad(\mbox{mod}\;12s+11). |  | (4.147) |

Under this condition,

 | m + t = 3 ​ s + 2 + c ⁡ ( 12 ​ s + 11) for some ​ c ∈ ℕ m+t=3s+2+c(12s+11)\qquad\mbox{for some}\;c\in\mathbb{N} |  | (4.148) |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ c + 1) ​ ( 12 ​ s + 11). 6m+j+\ell+1=2(3c+1)(12s+11). |  | (4.149) |

According to the second expression in (2.28),

 | ( 24 ​ t + 17) | ( 3 ​ c + 1) ⟹ c = 16 ​ t + 11 + d ⁡ ( 24 ​ t + 17) for ​ d ∈ ℕ. (24t+17)|(3c+1)\Longrightarrow c=16t+11+d(24t+17)\quad\mbox{for}\;d\in\mathbb{N}. |  | (4.150) |

Now

 | m \displaystyle m | = \displaystyle= | 3 ​ s − t + 2 + ( 16 ​ t + 11 + d ⁡ ( 24 ​ t + 17)) ​ ( 12 ​ s + 11) \displaystyle 3s-t+2+(16t+11+d(24t+17))(12s+11) |  | (4.151) |

 |  | = \displaystyle= | 31 ​ t − s + 21 + [d ⁡ ( 12 ​ s + 17) + 8 ​ s + 6] ​ ( 24 ​ t + 17) \displaystyle 31t-s+21+[d(12s+17)+8s+6](24t+17) |  |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 17). 6m+j+\ell+1=2(3d+2)(12s+11)(24t+17). |  | (4.152) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 17) + 2 ​ ( 12 ​ s + 11) + ( 24 ​ t + 17) 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 17) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{2(3d+2)(12s+11)(24t+17)}+\frac{2(12s+11)+(24t+17)}{2(3d+2)(12s+11)(24t+17)(24m+1)} |  | (4.153) |

 |  | = \displaystyle= | 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 11) ​ ( 24 ​ t + 17) + 1 ( 3 ​ d + 2) ​ ( 24 ​ t + 17) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{2(3d+2)(12s+11)(24t+17)}+\frac{1}{(3d+2)(24t+17)(24m+1)} |  |

 |  |  | + 1 2 ​ ( 3 ​ d + 2) ​ ( 12 ​ s + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2(3d+2)(12s+11)(24m+1)}. |  |

Theorem 4.10 For any positive integer m m in (4.151), we have the tame solution (4.153) of the Erdös-Straus equation.

Note that (4.151) with d ∈ ℕ d\in\mathbb{N} are the solution of the following system

 | m ≡ 3 ​ s − t + 2 ​ ( mod ​ 12 ​ s + 11), m ≡ 31 ​ t − s + 21 ​ ( mod ​ 24 ​ t + 17). m\equiv 3s-t+2\;\;(\mbox{mod}\>12s+11),\qquad m\equiv 31t-s+21\;\;(\mbox{mod}\>24t+17). |  | (4.154) |

## 5 Cases with the Numerator Summand ℑ 2 = 4 ​ ℓ + 3 \Im_{2}=4\ell+3

This is the case when

 | ℑ 1 = 4 j, k = j + ℓ + 1 with j, ℓ ∈ ℕ \displaystyle\Im_{1}=4j,\quad k=j+\ell+1\quad\mbox{with}\;\;j,\ell\in\mathbb{N} |  | (5.1) |

and ℓ ≥ 1 \ell\geq 1 by (2.13). Moreover,

 | 6 ​ m + k = 6 ​ m + j + ℓ + 1. 6m+k=6m+j+\ell+1. |  | (5.2) |

According to the firs expression in (2.28),

 | 4 | ( 6 ​ m + j + ℓ + 1). 4|(6m+j+\ell+1). |  | (5.3) |

So

 | j + ℓ ≡ 1 ( mod ​ 2). j+\ell\equiv 1\quad(\mbox{mod}\;2). |  | (5.4) |

### 5.1 Case m = 2 ​ m 1, j = 4 ​ s + 1 m=2m_{1},j=4s+1 and ℓ = 12 ​ t + 2 \ell=12t+2

Now

 | ℑ 1 = 4 ​ ( 4 ​ s + 1), ℑ 2 = 48 ​ t + 11 \Im_{1}=4(4s+1),\quad\Im_{2}=48t+11 |  | (5.5) |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + t) + s + 1). 6m+j+\ell+1=4(3(m_{1}+t)+s+1). |  | (5.6) |

According to the first expression in (2.28),

 | ( 4 ​ s + 1) | ( 3 ​ ( m 1 + t) + s + 1); (4s+1)|(3(m_{1}+t)+s+1); |  | (5.7) |

that is

 | 3 ​ ( m 1 + t) + s + 1 ≡ 0 ( mod ​ 4 ​ s + 1). 3(m_{1}+t)+s+1\equiv 0\quad(\mbox{mod}\;4s+1). |  | (5.8) |

Note

 | 3 ​ ( m 1 + t) + s + 1 ≡ 4 ​ s + 1 ( mod ​ 4 ​ s + 1). 3(m_{1}+t)+s+1\equiv 4s+1\quad(\mbox{mod}\;4s+1). |  | (5.9) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 3 ​ s ( mod ​ 4 ​ s + 1). 3(m_{1}+t)\equiv 3s\quad(\mbox{mod}\;4s+1). |  | (5.10) |

First we assume s ≢ 2 ​ ( mod ​ 3) s\not\equiv 2\;(\mbox{mod}\;3). Then

 | m 1 + t ≡ s ( mod ​ 4 ​ s + 1). m_{1}+t\equiv s\quad(\mbox{mod}\;4s+1). |  | (5.11) |

Hence

 | m 1 + t = s + c ⁡ ( 4 ​ s + 1) for some ​ c ∈ ℕ. m_{1}+t=s+c(4s+1)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.12) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 1) ​ ( 4 ​ s + 1). 6m+j+\ell+1=4(3c+1)(4s+1). |  | (5.13) |

According to the second expression in (2.28),

 | ( 48 ​ t + 11) | ( 3 ​ c + 1). (48t+11)|(3c+1). |  | (5.14) |

Therefore,

 | c = 32 ​ t + 7 + d ⁡ ( 48 ​ t + 11) for some ​ d ∈ ℕ. c=32t+7+d(48t+11)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.15) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 = 2 ​ [s − t + ( 32 ​ t + 7 + d ⁡ ( 48 ​ t + 11)) ​ ( 4 ​ s + 1)] \displaystyle 2m_{1}=2[s-t+(32t+7+d(48t+11))(4s+1)] |  | (5.16) |

 |  | = \displaystyle= | 2 ​ [32 ​ s ​ t + 7 ​ s + 31 ​ t + 6 + ( d ⁡ ( 4 ​ s + 1) + 2 ​ s) ​ ( 48 ​ t + 11)] \displaystyle 2[32st+7s+31t+6+(d(4s+1)+2s)(48t+11)] |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 11). 6m+j+\ell+1=4(3d+2)(4s+1)(48t+11). |  | (5.17) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 11) + 4 ​ ( 4 ​ s + 1) + ( 48 ​ t + 11) 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(4s+1)(48t+11)}+\frac{4(4s+1)+(48t+11)}{4(3d+2)(4s+1)(48t+11)(24m+1)} |  | (5.18) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 11) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(4s+1)(48t+11)}+\frac{1}{(3d+2)(48t+11)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(4s+1)(24m+1)}. |  |

Example 5.1.1 Let m = 304 m=304. Then n = 24 ​ m + 1 = 7297 n=24m+1=7297 is a prime. Moreover, m 1 = 152 m_{1}=152 satisfies (5.12) with s = 5 s=5 and t = 0 t=0. By (5.16),

 | 152 = 5 + 21 ​ ( 11 ​ d + 7) ⟹ d = 0. 152=5+21(11d+7)\Longrightarrow d=0. |  | (5.19) |

Now the above equation becomes

 | 4 7297 = 1 1848 + 1 160534 + 1 1225896. \frac{4}{7297}=\frac{1}{1848}+\frac{1}{160534}+\frac{1}{1225896}. |  | (5.20) |

Example 5.1.2 Let m = 402 m=402. Then n = 24 ​ m + 1 = 9649 n=24m+1=9649 is a prime. Moreover, m 1 = 201 m_{1}=201 satisfies (5.12) with s = 1 s=1 and t = 0 t=0. By (5.16),

 | 201 = 1 + 5 ​ ( 11 ​ d + 7) ⟹ 40 = 11 ​ d + 7 ⟹ d = 3. 201=1+5(11d+7)\Longrightarrow 40=11d+7\Longrightarrow d=3. |  | (5.21) |

Now (5.18) becomes

 | 4 9649 = 1 2420 + 1 1167529 + 1 2122780. \frac{4}{9649}=\frac{1}{2420}+\frac{1}{1167529}+\frac{1}{2122780}. |  | (5.22) |

Example 5.1.3 Let m = 512 m=512. Then n = 24 ​ m + 1 = 12289 n=24m+1=12289 is a prime. Moreover, m 1 = 256 m_{1}=256 satisfies (5.12) with s = 1 s=1 and t = 0 t=0. By (5.16),

 | 256 = 1 + 5 ​ ( 11 ​ d + 7) ⟹ 51 = 11 ​ d + 7 ⟹ d = 4. 256=1+5(11d+7)\Longrightarrow 51=11d+7\Longrightarrow d=4. |  | (5.23) |

Now (5.18) becomes

 | 4 12289 = 1 3080 + 1 1892506 + 1 3440920. \frac{4}{12289}=\frac{1}{3080}+\frac{1}{1892506}+\frac{1}{3440920}. |  | (5.24) |

Example 5.1.4 Let m = 994 m=994. Then n = 24 ​ m + 1 = 23857 n=24m+1=23857 is a prime. Moreover, m 1 = 497 m_{1}=497 satisfies (5.12) with s = 4 s=4 and t = 0 t=0. By (5.16),

 | 497 = 4 + 17 ​ ( 11 ​ d + 7) ⟹ 29 = 11 ​ d + 7 ⟹ d = 2. 497=4+17(11d+7)\Longrightarrow 29=11d+7\Longrightarrow d=2. |  | (5.25) |

Now (5.18) becomes

 | 4 23857 = 1 5984 + 1 2099416 + 1 12978208. \frac{4}{23857}=\frac{1}{5984}+\frac{1}{2099416}+\frac{1}{12978208}. |  | (5.26) |

Example 5.1.5 Let m = 1832 m=1832. Then n = 24 ​ m + 1 = 43969 n=24m+1=43969 is a prime. Moreover, m 1 = 916 m_{1}=916 satisfies (5.12) with s = 1 s=1 and t = 0 t=0. By (5.16),

 | 916 = 1 + 5 ​ ( 11 ​ d + 7) ⟹ 183 = 11 ​ d + 7 ⟹ d = 16. 916=1+5(11d+7)\Longrightarrow 183=11d+7\Longrightarrow d=16. |  | (5.27) |

Now (5.18) becomes

 | 4 43969 = 1 11000 + 1 24182950 + 1 43969000. \frac{4}{43969}=\frac{1}{11000}+\frac{1}{24182950}+\frac{1}{43969000}. |  | (5.28) |

Next we assume s = 3 ​ s 1 + 2 s=3s_{1}+2. Then (5.10) is equivalent to

 | m 1 + t ≡ 3 ​ s 1 + 2 ( mod ​ 4 ​ s 1 + 3). m_{1}+t\equiv 3s_{1}+2\quad(\mbox{mod}\;4s_{1}+3). |  | (5.29) |

Hence

 | m 1 + t = 3 ​ s 1 + 2 + c ⁡ ( 4 ​ s 1 + 3) for some ​ c ∈ ℕ. m_{1}+t=3s_{1}+2+c(4s_{1}+3)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.30) |

Moreover,

 | 3 ​ ( m 1 + t) + s + 1 = 3 ​ ( m 1 + t + s 1 + 1) = 3 ​ ( c + 1) ​ ( 4 ​ s 1 + 3). 3(m_{1}+t)+s+1=3(m_{1}+t+s_{1}+1)=3(c+1)(4s_{1}+3). |  | (5.31) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 11) | ( c + 1). (48t+11)|(c+1). |  | (5.32) |

Thus

 | c = d ⁡ ( 48 ​ t + 11) − 1 for some ​ d ∈ ℕ. c=d(48t+11)-1\quad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.33) |

Now

 | m = 2 ​ m 1 = − 2 ​ s 1 − 2 ​ t − 2 + 2 ​ d ​ ( 4 ​ s 1 + 3) ​ ( 48 ​ t + 11) m=2m_{1}=-2s_{1}-2t-2+2d(4s_{1}+3)(48t+11) |  | (5.34) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 4 ​ s 1 + 3) ​ ( 48 ​ t + 11). 6m+j+\ell+1=12d(4s_{1}+3)(48t+11). |  | (5.35) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 4 ​ s 1 + 3) ​ ( 48 ​ t + 11) + 12 ​ ( 4 ​ s 1 + 3) + ( 48 ​ t + 11) 12 ​ d ​ ( 4 ​ s 1 + 3) ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(4s_{1}+3)(48t+11)}+\frac{12(4s_{1}+3)+(48t+11)}{12d(4s_{1}+3)(48t+11)(24m+1)} |  | (5.36) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 4 ​ s 1 + 3) ​ ( 48 ​ t + 11) + 1 d ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(4s_{1}+3)(48t+11)}+\frac{1}{d(48t+11)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 4 ​ s 1 + 3) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(4s_{1}+3)(24m+1)}. |  |

Theorem 5.1 For any positive integer m m in (5.16), we have the tame solution (5.18) of the Erdös-Straus equation. When m m is of the form (5.34), we have the tame solution (5.36) of the Erdös-Straus equation.

### 5.2 Case m = 2 ​ m 1, j = 12 ​ r + 1 m=2m_{1},j=12r+1 and ℓ = 12 ​ t + 10 \ell=12t+10

Now

 | ℑ 1 = 4 ​ ( 12 ​ r + 1), ℑ 2 = 48 ​ t + 43 \Im_{1}=4(12r+1),\quad\Im_{2}=48t+43 |  | (5.37) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + r + t + 1). 6m+j+\ell+1=12(m_{1}+r+t+1). |  | (5.38) |

According to the first expression in (2.28),

 | ( 12 ​ r + 1) | ( m 1 + r + t + 1); (12r+1)|(m_{1}+r+t+1); |  | (5.39) |

that is

 | m 1 + r + t + 1 ≡ 0 ( mod ​ 12 ​ r + 1). m_{1}+r+t+1\equiv 0\quad(\mbox{mod}\;12r+1). |  | (5.40) |

Thus

 | m 1 ≡ − r − t − 1 ( mod ​ 12 ​ r + 1). m_{1}\equiv-r-t-1\quad(\mbox{mod}\;12r+1). |  | (5.41) |

Hence

 | m 1 = − r − t − 1 + c ⁡ ( 12 ​ r + 1) for some ​ c ∈ ℕ. m_{1}=-r-t-1+c(12r+1)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.42) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 12 ​ c ​ ( 12 ​ r + 1). 6m+j+\ell+1=12c(12r+1). |  | (5.43) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 43) | c. (48t+43)|c. |  | (5.44) |

Therefore,

 | c = d ⁡ ( 48 ​ t + 43) for some ​ d ∈ ℕ. c=d(48t+43)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.45) |

This implies

 | m = 2 m 1 = 2 [− r − t − 1 + d ( 48 t + 43)) ( 12 r + 1)] m=2m_{1}=2[-r-t-1+d(48t+43))(12r+1)] |  | (5.46) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 43). 6m+j+\ell+1=12d(12r+1)(48t+43). |  | (5.47) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 43) + 4 ​ ( 12 ​ r + 1) + ( 48 ​ t + 43) 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(12r+1)(48t+43)}+\frac{4(12r+1)+(48t+43)}{12d(12r+1)(48t+43)(24m+1)} |  | (5.48) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 43) + 1 3 ​ d ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(12r+1)(48t+43)}+\frac{1}{3d(48t+43)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 12 ​ r + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(12r+1)(24m+1)}. |  |

Theorem 5.2 For any positive integer m m in (5.46), we have the tame solution (5.48) of the Erdös-Straus equation.

### 5.3 Case m = 2 ​ m 1, j = 12 ​ r + 5 m=2m_{1},j=12r+5 and ℓ = 12 ​ t + 10 \ell=12t+10

In this case,

 | ℑ 1 = 4 ​ ( 12 ​ r + 5), ℑ 2 = 48 ​ t + 43 \Im_{1}=4(12r+5),\quad\Im_{2}=48t+43 |  | (5.49) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + r + t) + 4). 6m+j+\ell+1=4(3(m_{1}+r+t)+4). |  | (5.50) |

According to the first expression in (2.28),

 | ( 12 ​ r + 5) | ( 3 ​ ( m 1 + r + t) + 4); (12r+5)|(3(m_{1}+r+t)+4); |  | (5.51) |

that is

 | 3 ​ ( m 1 + r + t) + 4 ≡ 0 ( mod ​ 12 ​ r + 5). 3(m_{1}+r+t)+4\equiv 0\quad(\mbox{mod}\;12r+5). |  | (5.52) |

Note

 | 3 ​ ( m 1 + r + t) + 4 ≡ 2 ​ ( 12 ​ r + 5) ( mod ​ 12 ​ r + 5). 3(m_{1}+r+t)+4\equiv 2(12r+5)\quad(\mbox{mod}\;12r+5). |  | (5.53) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 21 ​ r + 6 ( mod ​ 12 ​ r + 5). 3(m_{1}+t)\equiv 21r+6\quad(\mbox{mod}\;12r+5). |  | (5.54) |

So

 | m 1 + t ≡ 7 ​ r + 2 ( mod ​ 12 ​ r + 5). m_{1}+t\equiv 7r+2\quad(\mbox{mod}\;12r+5). |  | (5.55) |

Thus

 | m 1 ≡ 7 ​ r − t + 2 ( mod ​ 12 ​ r + 5). m_{1}\equiv 7r-t+2\quad(\mbox{mod}\;12r+5). |  | (5.56) |

Hence

 | m 1 = 7 ​ r − t + 2 + c ⁡ ( 12 ​ r + 5) for some ​ c ∈ ℕ. m_{1}=7r-t+2+c(12r+5)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.57) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 5). 6m+j+\ell+1=4(3c+2)(12r+5). |  | (5.58) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 43) | ( 3 ​ c + 2). (48t+43)|(3c+2). |  | (5.59) |

Therefore,

 | c = 32 ​ t + 28 + d ⁡ ( 48 ​ t + 43) for some ​ d ∈ ℕ. c=32t+28+d(48t+43)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.60) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 = 2 ​ [7 ​ r − t + 2 + ( 32 ​ t + 28 + d ⁡ ( 48 ​ t + 43)) ​ ( 12 ​ r + 5)] \displaystyle 2m_{1}=2[7r-t+2+(32t+28+d(48t+43))(12r+5)] |  | (5.61) |

 |  | = \displaystyle= | 2 ​ [15 ​ t − r + 13 + ( d ⁡ ( 12 ​ r + 5) + 8 ​ r + 3) ​ ( 48 ​ t + 43)] \displaystyle 2[15t-r+13+(d(12r+5)+8r+3)(48t+43)] |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 43). 6m+j+\ell+1=4(3d+2)(12r+5)(48t+43). |  | (5.62) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 43) + 4 ​ ( 12 ​ r + 5) + ( 48 ​ t + 43) 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(12r+5)(48t+43)}+\frac{4(12r+5)+(48t+43)}{4(3d+2)(12r+5)(48t+43)(24m+1)} |  | (5.63) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 43) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(12r+5)(48t+43)}+\frac{1}{(3d+2)(48t+43)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(12r+5)(24m+1)}. |  |

Theorem 5.3 For any positive integer m m in (5.61), we have the tame solution (5.63) of the Erdös-Straus equation.

### 5.4 Case m = 2 ​ m 1, j = 12 ​ r + 7 m=2m_{1},j=12r+7 and ℓ = 12 ​ t + 4 \ell=12t+4

Now

 | ℑ 1 = 4 ​ ( 12 ​ r + 7), ℑ 2 = 48 ​ t + 19 \Im_{1}=4(12r+7),\quad\Im_{2}=48t+19 |  | (5.64) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + r + t + 1). 6m+j+\ell+1=12(m_{1}+r+t+1). |  | (5.65) |

According to the first expression in (2.28),

 | ( 12 ​ r + 7) | ( m 1 + r + t + 1); (12r+7)|(m_{1}+r+t+1); |  | (5.66) |

that is

 | m 1 + r + t + 1 ≡ 0 ( mod ​ 12 ​ r + 7). m_{1}+r+t+1\equiv 0\quad(\mbox{mod}\;12r+7). |  | (5.67) |

Hence

 | m 1 = − r − t − 1 + c ⁡ ( 12 ​ r + 7) for some ​ c ∈ ℕ. m_{1}=-r-t-1+c(12r+7)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.68) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 12 ​ c ​ ( 12 ​ r + 7). 6m+j+\ell+1=12c(12r+7). |  | (5.69) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 19) | c. (48t+19)|c. |  | (5.70) |

Therefore,

 | c = d ⁡ ( 48 ​ t + 19) for some ​ d ∈ ℕ. c=d(48t+19)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.71) |

This implies

 | m = 2 ​ m 1 = 2 ​ [− r − t − 1 + d ⁡ ( 12 ​ r + 7) ​ ( 48 ​ t + 19)] m=2m_{1}=2[-r-t-1+d(12r+7)(48t+19)] |  | (5.72) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 19). 6m+j+\ell+1=12d(12r+7)(48t+19). |  | (5.73) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 19) + 4 ​ ( 12 ​ r + 7) + ( 48 ​ t + 19) 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(12r+7)(48t+19)}+\frac{4(12r+7)+(48t+19)}{12d(12r+7)(48t+19)(24m+1)} |  | (5.74) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 19) + 1 3 ​ d ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(12r+7)(48t+19)}+\frac{1}{3d(48t+19)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 12 ​ r + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(12r+7)(24m+1)}. |  |

Theorem 5.4 For any positive integer m m in (5.72), we have the tame solution (5.74) of the Erdös-Straus equation.

Example 5.4.1 Let m = 264 m=264. Then n = 24 ​ m + 1 = 6337 n=24m+1=6337 is a prime. Note m 1 = 232 m_{1}=232 and (5.68) gives r = t = 0 r=t=0. Moreover, (5.72) shows d = 1 d=1. Now (5.74) becomes

 | 4 6337 = 1 1596 + 1 361209 + 1 532308. \frac{4}{6337}=\frac{1}{1596}+\frac{1}{361209}+\frac{1}{532308}. |  | (5.75) |

Example 5.4.2 Let m = 530 m=530. Then n = 24 ​ m + 1 = 12721 n=24m+1=12721 is a prime. Note m 1 = 265 m_{1}=265 and (5.68) gives r = t = 0 r=t=0. Moreover, (5.72) shows d = 2 d=2. Now (5.74) becomes

 | 4 12721 = 1 3192 + 1 722418 + 1 1064616. \frac{4}{12721}=\frac{1}{3192}+\frac{1}{722418}+\frac{1}{1064616}. |  | (5.76) |

### 5.5 Case m = 2 ​ m 1, j = 4 ​ s + 3 m=2m_{1},j=4s+3 and ℓ = 12 ​ t + 8 \ell=12t+8

In this case,

 | ℑ 1 = 4 ​ ( 4 ​ s + 3), ℑ 2 = 48 ​ t + 35 \Im_{1}=4(4s+3),\quad\Im_{2}=48t+35 |  | (5.77) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + t + 1) + s). 6m+j+\ell+1=4(3(m_{1}+t+1)+s). |  | (5.78) |

Suppose s = 0 s=0. Then

 | ℑ 1 = 12, 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + t + 1). \Im_{1}=12,\quad 6m+j+\ell+1=12(m_{1}+t+1). |  | (5.79) |

So the first expression in (2.28) naturally holds. The second expression in (2.28) yields

 | ( 48 ​ t + 35) | ( m 1 + t + 1). (48t+35)|(m_{1}+t+1). |  | (5.80) |

Hence

 | m 1 = − t − 1 + c ⁡ ( 48 ​ t + 35) for some ​ c ∈ ℕ. m_{1}=-t-1+c(48t+35)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.81) |

Note

 | 6 ​ m + j + ℓ + 1 = 12 ​ c ​ ( 48 ​ t + 35). 6m+j+\ell+1=12c(48t+35). |  | (5.82) |

So (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 12 ​ c ​ ( 48 ​ t + 35) + 12 + ( 48 ​ t + 35) 12 ​ c ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12c(48t+35)}+\frac{12+(48t+35)}{12c(48t+35)(24m+1)} |  | (5.83) |

 |  | = \displaystyle= | 1 12 ​ c ​ ( 48 ​ t + 35) + 1 c ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) + 1 12 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{12c(48t+35)}+\frac{1}{c(48t+35)(24m+1)}+\frac{1}{12c(24m+1)}. |  |

Example 5.5.1 Let m = 444 m=444. Then n = 24 ​ m + 1 = 10657 n=24m+1=10657 is a prime. Note m 1 = 222 m_{1}=222 and (5.74) gives t = 4 t=4 and c = 1 c=1. Now (2.11) becomes

 | 4 10657 = 1 2724 + 1 2419139 + 1 127884. \frac{4}{10657}=\frac{1}{2724}+\frac{1}{2419139}+\frac{1}{127884}. |  | (5.84) |

In the rest of this subsection, we always assume s > 0 s>0. According to the first expression in (2.28), (5.77) and (5.78),

 | ( 4 ​ s + 3) | ( 3 ​ ( m 1 + t + 1) + s); (4s+3)|(3(m_{1}+t+1)+s); |  | (5.85) |

that is

 | 3 ​ ( m 1 + t + 1) + s ≡ 0 ( mod ​ 4 ​ s + 3). 3(m_{1}+t+1)+s\equiv 0\quad(\mbox{mod}\;4s+3). |  | (5.86) |

Note

 | 3 ​ ( m 1 + t + 1) + s ≡ 4 ​ s + 3 ( mod ​ 4 ​ s + 3). 3(m_{1}+t+1)+s\equiv 4s+3\quad(\mbox{mod}\;4s+3). |  | (5.87) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 3 ​ s ( mod ​ 4 ​ s + 3). 3(m_{1}+t)\equiv 3s\quad(\mbox{mod}\;4s+3). |  | (5.88) |

First we assume s ≡ 0 ​ ( mod ​ 3) s\equiv 0\;(\mbox{mod}\;3); that is, s = 3 ​ s 1 s=3s_{1} for some s 1 ∈ ℕ s_{1}\in\mathbb{N}. Moreover, the above equation becomes

 | 3 ​ ( m 1 + t) ≡ 9 ​ s 1 ( mod ​ 12 ​ s 1 + 3). 3(m_{1}+t)\equiv 9s_{1}\quad(\mbox{mod}\;12s_{1}+3). |  | (5.89) |

So

 | m 1 + t ≡ 3 ​ s 1 ( mod ​ 4 ​ s 1 + 1). m_{1}+t\equiv 3s_{1}\quad(\mbox{mod}\;4s_{1}+1). |  | (5.90) |

Thus

 | m 1 = 3 ​ s 1 − t + c ⁡ ( 4 ​ s 1 + 1) for some ​ c ∈ ℕ. m_{1}=3s_{1}-t+c(4s_{1}+1)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.91) |

In particular,

 | 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + t + s 1 + 1) = 12 ​ ( c + 1) ​ ( 4 ​ s 1 + 1). 6m+j+\ell+1=12(m_{1}+t+s_{1}+1)=12(c+1)(4s_{1}+1). |  | (5.92) |

The second expression in (2.28) yields

 | ( 48 ​ t + 35) | ( c + 1) ⟹ c = d ⁡ ( 48 ​ t + 35) − 1 for some ​ d ∈ ℕ. (48t+35)|(c+1)\Longrightarrow c=d(48t+35)-1\quad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.93) |

Equation (5.91) shows

 | m 1 = − s 1 − t − 1 + d ⁡ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 35). m_{1}=-s_{1}-t-1+d(4s_{1}+1)(48t+35). |  | (5.94) |

Furthermore,

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 35). 6m+j+\ell+1=12d(4s_{1}+1)(48t+35). |  | (5.95) |

Therefore, (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 35) + 12 ​ ( 4 ​ s 1 + 1) + ( 48 ​ t + 35) 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(4s_{1}+1)(48t+35)}+\frac{12(4s_{1}+1)+(48t+35)}{12d(4s_{1}+1)(48t+35)(24m+1)} |  | (5.96) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 35) + 1 d ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(4s_{1}+1)(48t+35)}+\frac{1}{d(48t+35)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(4s_{1}+1)(24m+1)}. |  |

Next we assume s ≢ 0 ​ ( mod ​ 3) s\not\equiv 0\;(\mbox{mod}\;3). By (5.88),

 | m 1 + t ≡ s ( mod ​ 4 ​ s + 3). m_{1}+t\equiv s\quad(\mbox{mod}\;4s+3). |  | (5.97) |

Thus

 | m 1 ≡ s − t ( mod ​ 4 ​ s + 3). m_{1}\equiv s-t\quad(\mbox{mod}\;4s+3). |  | (5.98) |

Hence

 | m 1 = s − t + c ⁡ ( 4 ​ s + 3) for some ​ c ∈ ℕ. m_{1}=s-t+c(4s+3)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.99) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 1) ​ ( 4 ​ s + 3). 6m+j+\ell+1=4(3c+1)(4s+3). |  | (5.100) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 35) | ( 3 ​ c + 1). (48t+35)|(3c+1). |  | (5.101) |

Therefore,

 | c = 32 ​ t + 23 + d ⁡ ( 48 ​ t + 35) for some ​ d ∈ ℕ. c=32t+23+d(48t+35)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.102) |

This implies

 | m 1 \displaystyle m_{1} | = \displaystyle= | s − t + ( 32 ​ t + 23 + d ⁡ ( 48 ​ t + 35)) ​ ( 4 ​ s + 3) \displaystyle s-t+(32t+23+d(48t+35))(4s+3) |  | (5.103) |

 |  | = \displaystyle= | 32 ​ s ​ t + 23 ​ s − t − 1 + ( d ⁡ ( 4 ​ s + 1) + 2 ​ ( s + 1)) ​ ( 48 ​ t + 35) \displaystyle 32st+23s-t-1+(d(4s+1)+2(s+1))(48t+35) |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 35). 6m+j+\ell+1=4(3d+2)(4s+3)(48t+35). |  | (5.104) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 35) + 4 ​ ( 4 ​ s + 3) + ( 48 ​ t + 35) 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(4s+3)(48t+35)}+\frac{4(4s+3)+(48t+35)}{4(3d+2)(4s+3)(48t+35)(24m+1)} |  | (5.105) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 35) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(4s+3)(48t+35)}+\frac{1}{(3d+2)(48t+35)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(4s+3)(24m+1)}. |  |

In summary, we have:

Theorem 5.5 Assume m = 2 ​ m 1 m=2m_{1}. If m 1 ≡ − t − 1 ​ ( mod ​ 48 ​ t + 35) m_{1}\equiv-t-1\;(\mbox{mod}\;48t+35), then the Erdös-Straus equation (5.83) holds. When

 | m 1 ≡ − s 1 − t − 1 ​ ( mod ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 35)), m_{1}\equiv-s_{1}-t-1\;(\mbox{mod}\;(4s_{1}+1)(48t+35)), |  | (5.106) |

the Erdös-Straus equation (5.96) holds. Suppose that

 | m 1 ≡ s − t ⁡ ( mod ​ 4 ​ s + 3). m 1 ≡ 32 ​ s ​ t + 23 ​ s − t − 1 ( mod ​ 48 ​ t + 35). m_{1}\equiv s-t\;(\mbox{mod}\;4s+3).\quad m_{1}\equiv 32st+23s-t-1\quad(\mbox{mod}\;48t+35). |  | (5.107) |

We get the Erdös-Straus equation (5.105).

### 5.6 Case m = 2 ​ m 1, j = 12 ​ r + 11 m=2m_{1},j=12r+11 and ℓ = 12 ​ t + 4 \ell=12t+4

Now

 | ℑ 1 = 4 ​ ( 12 ​ r + 11), ℑ 2 = 48 ​ t + 19 \Im_{1}=4(12r+11),\quad\Im_{2}=48t+19 |  | (5.108) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + r + t) + 4). 6m+j+\ell+1=4(3(m_{1}+r+t)+4). |  | (5.109) |

According to the first expression in (2.28),

 | ( 12 ​ r + 11) | ( 3 ​ ( m 1 + r + t) + 4); (12r+11)|(3(m_{1}+r+t)+4); |  | (5.110) |

that is

 | 3 ​ ( m 1 + r + t) + 4 ≡ 0 ( mod ​ 12 ​ r + 11). 3(m_{1}+r+t)+4\equiv 0\quad(\mbox{mod}\;12r+11). |  | (5.111) |

Note

 | 3 ​ ( m 1 + r + t) + 4 ≡ 2 ​ ( 12 ​ r + 11) ( mod ​ 12 ​ r + 11). 3(m_{1}+r+t)+4\equiv 2(12r+11)\quad(\mbox{mod}\;12r+11). |  | (5.112) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 21 ​ r + 18 ( mod ​ 12 ​ r + 11). 3(m_{1}+t)\equiv 21r+18\quad(\mbox{mod}\;12r+11). |  | (5.113) |

So

 | m 1 ≡ 7 ​ r − t + 6 ( mod ​ 12 ​ r + 11). m_{1}\equiv 7r-t+6\quad(\mbox{mod}\;12r+11). |  | (5.114) |

Hence

 | m 1 = 7 ​ r − t + 6 + c ⁡ ( 12 ​ r + 11) for some ​ c ∈ ℕ. m_{1}=7r-t+6+c(12r+11)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.115) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 11). 6m+j+\ell+1=4(3c+2)(12r+11). |  | (5.116) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 19) | ( 3 ​ c + 2). (48t+19)|(3c+2). |  | (5.117) |

Therefore,

 | c = 32 ​ t + 12 + d ⁡ ( 48 ​ t + 19) for some ​ d ∈ ℕ. c=32t+12+d(48t+19)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.118) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 = 2 ​ [7 ​ r − t + 6 + ( 32 ​ t + 12 + d ⁡ ( 48 ​ t + 19)) ​ ( 12 ​ r + 11)] \displaystyle 2m_{1}=2[7r-t+6+(32t+12+d(48t+19))(12r+11)] |  | (5.119) |

 |  | = \displaystyle= | 2 ​ [15 ​ t − r + 5 + ( d ⁡ ( 12 ​ r + 11) + 8 ​ r + 7) ​ ( 48 ​ t + 19)] \displaystyle 2[15t-r+5+(d(12r+11)+8r+7)(48t+19)] |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 19). 6m+j+\ell+1=4(3d+2)(12r+11)(48t+19). |  | (5.120) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 19) + 4 ​ ( 12 ​ r + 11) + ( 48 ​ t + 19) 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(12r+11)(48t+19)}+\frac{4(12r+11)+(48t+19)}{4(3d+2)(12r+11)(48t+19)(24m+1)} |  | (5.121) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 19) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(12r+11)(48t+19)}+\frac{1}{(3d+2)(48t+19)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(12r+11)(24m+1)}. |  |

Theorem 5.6 Assume m = 2 ​ m 1 m=2m_{1}. If m m is of the form (5.119), then the Erdös-Straus equation (5.121) holds.

### 5.7 Case m = 2 ​ m 1 + 1, j = 12 ​ r + 1 m=2m_{1}+1,j=12r+1 and ℓ = 12 ​ t + 4 \ell=12t+4

In this case,

 | ℑ 1 = 4 ​ ( 12 ​ r + 1), ℑ 2 = 48 ​ t + 19 \Im_{1}=4(12r+1),\quad\Im_{2}=48t+19 |  | (5.122) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + r + t + 1). 6m+j+\ell+1=12(m_{1}+r+t+1). |  | (5.123) |

According to the first expression in (2.28),

 | ( 12 ​ r + 1) | ( m 1 + r + t + 1); (12r+1)|(m_{1}+r+t+1); |  | (5.124) |

that is

 | m 1 + r + t + 1 ≡ 0 ( mod ​ 12 ​ r + 1). m_{1}+r+t+1\equiv 0\quad(\mbox{mod}\;12r+1). |  | (5.125) |

Note

 | m 1 ≡ − r − t − 1 ( mod ​ 12 ​ r + 1). m_{1}\equiv-r-t-1\quad(\mbox{mod}\;12r+1). |  | (5.126) |

So Hence

 | m 1 = − r − t − 1 + c ⁡ ( 12 ​ r + 1) for some ​ c ∈ ℕ. m_{1}=-r-t-1+c(12r+1)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.127) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 12 ​ c ​ ( 12 ​ r + 1). 6m+j+\ell+1=12c(12r+1). |  | (5.128) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 19) | c. (48t+19)|c. |  | (5.129) |

Therefore,

 | c = d ⁡ ( 48 ​ t + 19) for some ​ d ∈ ℕ. c=d(48t+19)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.130) |

This implies

 | m = 2 ​ m 1 + 1 = 2 ​ [− r − t + d ⁡ ( 48 ​ t + 19) ​ ( 12 ​ r + 1)] − 1 m=2m_{1}+1=2[-r-t+d(48t+19)(12r+1)]-1 |  | (5.131) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 19). 6m+j+\ell+1=12d(12r+1)(48t+19). |  | (5.132) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 19) + 4 ​ ( 12 ​ r + 1) + ( 48 ​ t + 19) 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(12r+1)(48t+19)}+\frac{4(12r+1)+(48t+19)}{12d(12r+1)(48t+19)(24m+1)} |  | (5.133) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 12 ​ r + 1) ​ ( 48 ​ t + 19) + 1 3 ​ d ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(12r+1)(48t+19)}+\frac{1}{3d(48t+19)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 12 ​ r + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(12r+1)(24m+1)}. |  |

Theorem 5.7 If m m is of the form (5.131), then the Erdös-Straus equation (5.133) holds.

Note that (5.31) is equivalent to

 | m ≡ − 2 ​ r − 2 ​ t − 1 ( mod ​ 2 ​ ( 48 ​ t + 19) ​ ( 12 ​ r + 1)). m\equiv-2r-2t-1\quad(\mbox{mod}\;2(48t+19)(12r+1)). |  | (5.134) |

### 5.8 Case m = 2 ​ m 1 + 1, j = 12 ​ r + 5 m=2m_{1}+1,j=12r+5 and ℓ = 12 ​ t + 4 \ell=12t+4

Now

 | ℑ 1 = 4 ​ ( 12 ​ r + 5), ℑ 2 = 48 ​ t + 19 \Im_{1}=4(12r+5),\quad\Im_{2}=48t+19 |  | (5.135) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + r + t) + 4). 6m+j+\ell+1=4(3(m_{1}+r+t)+4). |  | (5.136) |

According to the first expression in (2.28),

 | ( 12 ​ r + 19) | ( 3 ​ ( m 1 + r + t) + 4); (12r+19)|(3(m_{1}+r+t)+4); |  | (5.137) |

that is

 | 3 ​ ( m 1 + r + t) + 4 ≡ 0 ( mod ​ 12 ​ r + 5). 3(m_{1}+r+t)+4\equiv 0\quad(\mbox{mod}\;12r+5). |  | (5.138) |

Note

 | 3 ​ ( m 1 + r + t) + 4 ≡ 2 ​ ( 12 ​ r + 5) ( mod ​ 12 ​ r + 5); 3(m_{1}+r+t)+4\equiv 2(12r+5)\quad(\mbox{mod}\;12r+5); |  | (5.139) |

that is,

 | 3 ​ ( m 1 + t) ≡ 21 ​ r + 6 ( mod ​ 12 ​ r + 5). 3(m_{1}+t)\equiv 21r+6\quad(\mbox{mod}\;12r+5). |  | (5.140) |

 | m 1 ≡ 7 ​ r − t + 2 ( mod ​ 12 ​ r + 5). m_{1}\equiv 7r-t+2\quad(\mbox{mod}\;12r+5). |  | (5.141) |

Hence

 | m 1 = 7 ​ r − t + 2 + c ⁡ ( 12 ​ r + 5) for some ​ c ∈ ℕ. m_{1}=7r-t+2+c(12r+5)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.142) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 5). 6m+j+\ell+1=4(3c+2)(12r+5). |  | (5.143) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 19) | ( 3 ​ c + 2). (48t+19)|(3c+2). |  | (5.144) |

Therefore,

 | c = 32 ​ t + 12 + d ⁡ ( 48 ​ t + 19) for some ​ d ∈ ℕ. c=32t+12+d(48t+19)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.145) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 + 1 = 2 ​ [7 ​ r − t + 2 + ( 32 + 12 + d ⁡ ( 48 ​ t + 19)) ​ ( 12 ​ r + 5)] + 1 \displaystyle 2m_{1}+1=2[7r-t+2+(32+12+d(48t+19))(12r+5)]+1 |  | (5.146) |

 |  | = \displaystyle= | 2 ​ [15 ​ t − r + ( d ⁡ ( 12 ​ r + 5) + 8 ​ r + 3) ​ ( 48 ​ t + 19)] + 9 \displaystyle 2[15t-r+(d(12r+5)+8r+3)(48t+19)]+9 |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 19). 6m+j+\ell+1=4(3d+2)(12r+5)(48t+19). |  | (5.147) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 19) + 4 ​ ( 12 ​ r + 5) + ( 48 ​ t + 19) 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(12r+5)(48t+19)}+\frac{4(12r+5)+(48t+19)}{4(3d+2)(12r+5)(48t+19)(24m+1)} |  | (5.148) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 48 ​ t + 19) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 19) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(12r+5)(48t+19)}+\frac{1}{(3d+2)(48t+19)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 5) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(12r+5)(24m+1)}. |  |

Theorem 5.8 If m m is of the form (5.146), then the Erdös-Straus equation (5.148) holds.

### 5.9 Case m = 2 ​ m 1 + 1, j = 4 ​ s + 1 m=2m_{1}+1,j=4s+1 and ℓ = 12 ​ t + 8 \ell=12t+8

In this case,

 | ℑ 1 = 4 ​ ( 4 ​ s + 1), ℑ 2 = 48 ​ t + 35 \Im_{1}=4(4s+1),\quad\Im_{2}=48t+35 |  | (5.149) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + t) + s + 4). 6m+j+\ell+1=4(3(m_{1}+t)+s+4). |  | (5.150) |

According to the first expression in (2.28),

 | ( 4 ​ s + 1) | ( 3 ​ ( m 1 + t) + s + 4); (4s+1)|(3(m_{1}+t)+s+4); |  | (5.151) |

that is

 | 3 ​ ( m 1 + t) + s + 4 ≡ 0 ( mod ​ 4 ​ s + 1). 3(m_{1}+t)+s+4\equiv 0\quad(\mbox{mod}\;4s+1). |  | (5.152) |

Note

 | 3 ​ ( m 1 + t) + s + 4 ≡ 4 ​ s + 1 ( mod ​ 4 ​ s + 1). 3(m_{1}+t)+s+4\equiv 4s+1\quad(\mbox{mod}\;4s+1). |  | (5.153) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 3 ​ s − 3 ( mod ​ 4 ​ s + 1). 3(m_{1}+t)\equiv 3s-3\quad(\mbox{mod}\;4s+1). |  | (5.154) |

Thus

 | m 1 + t ≡ s − 1 ( mod ​ 4 ​ s + 1). m_{1}+t\equiv s-1\quad(\mbox{mod}\;4s+1). |  | (5.155) |

Hence

 | m 1 = s − t − 1 + c ⁡ ( 4 ​ s + 1) for some ​ c ∈ ℕ. m_{1}=s-t-1+c(4s+1)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.156) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 1) ​ ( 4 ​ s + 1). 6m+j+\ell+1=4(3c+1)(4s+1). |  | (5.157) |

According to the second expression in (2.28) and (3.122),

 | ( 48 ​ t + 35) | ( 3 ​ c + 1). (48t+35)|(3c+1). |  | (5.158) |

Therefore,

 | c = 32 ​ t + 23 + d ⁡ ( 48 ​ t + 35) for some ​ d ∈ ℕ. c=32t+23+d(48t+35)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.159) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 + 1 = 2 ​ [s − t − 1 + ( 32 ​ t + 23 + d ⁡ ( 48 ​ t + 35)) ​ ( 4 ​ s + 1)] + 1 \displaystyle 2m_{1}+1=2[s-t-1+(32t+23+d(48t+35))(4s+1)]+1 |  | (5.160) |

 |  | = \displaystyle= | 2 [32 s t + 23 s + 31 t + ( d ( 12 r + 1) + 2 s) ( 48 t + 35))] + 43 \displaystyle 2[32st+23s+31t+(d(12r+1)+2s)(48t+35))]+43 |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 35). 6m+j+\ell+1=4(3d+2)(4s+1)(48t+35). |  | (5.161) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 35) + 4 ​ ( 4 ​ s + 1) + ( 48 ​ t + 35) 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(4s+1)(48t+35)}+\frac{4(4s+1)+(48t+35)}{4(3d+2)(4s+1)(48t+35)(24m+1)} |  | (5.162) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 48 ​ t + 35) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 35) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(4s+1)(48t+35)}+\frac{1}{(3d+2)(48t+35)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(4s+1)(24m+1)}. |  |

Theorem 5.9 If m m is of the form (5.160), then the Erdös-Straus equation (5.162) holds.

### 5.10 Case m = 2 ​ m 1 + 1, j = 4 ​ s + 3 m=2m_{1}+1,j=4s+3 and ℓ = 12 ​ t + 2 \ell=12t+2

Now

 | ℑ 1 = 4 ​ ( 4 ​ s + 3), ℑ 2 = 48 ​ t + 11 \Im_{1}=4(4s+3),\quad\Im_{2}=48t+11 |  | (5.163) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + t + 1) + s). 6m+j+\ell+1=4(3(m_{1}+t+1)+s). |  | (5.164) |

According to the first expression in (2.28),

 | ( 4 ​ s + 3) | ( 3 ​ ( m 1 + t + 1) + s); (4s+3)|(3(m_{1}+t+1)+s); |  | (5.165) |

that is

 | 3 ​ ( m 1 + t + 1) + s ≡ 0 ( mod ​ 4 ​ s + 3). 3(m_{1}+t+1)+s\equiv 0\quad(\mbox{mod}\;4s+3). |  | (5.166) |

Note

 | 3 ​ ( m 1 + t + 1) + s ≡ 4 ​ s + 3 ( mod ​ 4 ​ s + 3). 3(m_{1}+t+1)+s\equiv 4s+3\quad(\mbox{mod}\;4s+3). |  | (5.167) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 3 ​ s ( mod ​ 4 ​ s + 3). 3(m_{1}+t)\equiv 3s\quad(\mbox{mod}\;4s+3). |  | (5.168) |

First we assume s = 0 s=0. Then

 | ℑ 1 = 12, 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + t + 1). \Im_{1}=12,\quad 6m+j+\ell+1=12(m_{1}+t+1). |  | (5.169) |

The first expression in (2.28) naturally holds. Moreover, the second expression in (2.28) yields

 | ( 48 ​ t + 11) | ( m 1 + t + 1). (48t+11)|(m_{1}+t+1). |  | (5.170) |

Hence

 | m 1 = − t − 1 + c ⁡ ( 48 ​ t + 11) for some ​ c ∈ ℕ. m_{1}=-t-1+c(48t+11)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.171) |

Moreover,

 | m = 2 ​ m 1 + 1 = − 2 ​ t − 1 + 2 ​ c ​ ( 48 ​ t + 11) m=2m_{1}+1=-2t-1+2c(48t+11) |  | (5.172) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ c ​ ( 48 ​ t + 11). 6m+j+\ell+1=12c(48t+11). |  | (5.173) |

Expression (2.11) becomes

 | 4 24 ​ m + 1 \displaystyle\frac{4}{24m+1} | = \displaystyle= | 1 12 ​ c ​ ( 48 ​ t + 11) + 12 + ( 48 ​ t + 11) 12 ​ c ​ ( 48 ​ t + 11) ​ ( 24 ​ m +) \displaystyle\frac{1}{12c(48t+11)}+\frac{12+(48t+11)}{12c(48t+11)(24m+)} |  | (5.174) |

 |  | = \displaystyle= | 1 12 ​ c ​ ( 48 ​ t + 11) + 1 c ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) + 1 12 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{12c(48t+11)}+\frac{1}{c(48t+11)(24m+1)}+\frac{1}{12c(24m+1)}. |  |

Example 5.10.1 Let m = 705 m=705. Then n = 24 ​ m + 1 = 16921 n=24m+1=16921 is a prime. Note m 1 = 352 m_{1}=352 and (5.171) gives t = 1 t=1. In fact,

 | 352 = − 2 + 59 ​ c ⟹ c = 6. 352=-2+59c\Longrightarrow c=6. |  | (5.175) |

Moreover, (5.174) becomes

 | 4 16921 = 1 4248 + 1 5990034 + 1 1218312. \frac{4}{16921}=\frac{1}{4248}+\frac{1}{5990034}+\frac{1}{1218312}. |  | (5.176) |

Next we assume s = 3 ​ s 1 s=3s_{1} with 0 < s 1 ∈ ℕ 0<s_{1}\in\mathbb{N}. Now (5.168) becomes

 | 3 ​ ( m 1 + t) ≡ 9 ​ s 1 ( mod ​ 3 ​ ( 4 ​ s 1 + 1)). 3(m_{1}+t)\equiv 9s_{1}\quad(\mbox{mod}\;3(4s_{1}+1)). |  | (5.177) |

Thus

 | m 1 + t ≡ 3 ​ s 1 ( mod ​ 4 ​ s 1 + 1) ⟹ m 1 = 3 ​ s 1 − t + c ⁡ ( 4 ​ s 1 + 1) m_{1}+t\equiv 3s_{1}\quad(\mbox{mod}\;4s_{1}+1)\Longrightarrow m_{1}=3s_{1}-t+c(4s_{1}+1) |  | (5.178) |

for some c ∈ ℕ c\in\mathbb{N}. Moreover,

 | ℑ 1 = 12 ​ ( 4 ​ s 1 + 1) \Im_{1}=12(4s_{1}+1) |  | (5.179) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + s 1 + t + 1) = 12 ​ ( c + 1) ​ ( 4 ​ s 1 + 1). 6m+j+\ell+1=12(m_{1}+s_{1}+t+1)=12(c+1)(4s_{1}+1). |  | (5.180) |

By the second expression in (2.28),

 | ( 48 ​ t + 11) | ( c + 1) ⟹ c + 1 = d ⁡ ( 48 ​ t + 11) (48t+11)|(c+1)\Longrightarrow c+1=d(48t+11) |  | (5.181) |

for some d ∈ ℕ d\in\mathbb{N}. Now

 | m 1 = − s 1 − t − 1 + d ⁡ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 11). m_{1}=-s_{1}-t-1+d(4s_{1}+1)(48t+11). |  | (5.182) |

Moreover,

 | m = 2 ​ m 1 + 1 = − 2 ​ s 1 − 2 ​ t − 1 + 2 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 11) m=2m_{1}+1=-2s_{1}-2t-1+2d(4s_{1}+1)(48t+11) |  | (5.183) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 11). 6m+j+\ell+1=12d(4s_{1}+1)(48t+11). |  | (5.184) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 11) + 12 ​ ( 4 ​ s 1 + 1) + ( 48 ​ t + 11) 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 11) ​ ( 24 ​ m +) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(4s_{1}+1)(48t+11)}+\frac{12(4s_{1}+1)+(48t+11)}{12d(4s_{1}+1)(48t+11)(24m+)} |  | (5.185) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 48 ​ t + 11) + 1 d ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(4s_{1}+1)(48t+11)}+\frac{1}{d(48t+11)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 4 ​ s 1 + 1) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(4s_{1}+1)(24m+1)}. |  |

Example 5.10.2 Let m = 1995 m=1995. Then n = 24 ​ m + 1 = 47881 n=24m+1=47881 is a prime. Note m 1 = 997 m_{1}=997 and (5.182) gives s 1 = 3 s_{1}=3 and t = 0 t=0. In fact,

 | 997 = − 4 + 143 ​ d ⟹ d = 7. 997=-4+143d\Longrightarrow d=7. |  | (5.186) |

Moreover, (5.185) becomes

 | 4 47881 = 1 12012 + 1 3686837 + 1 52286052. \frac{4}{47881}=\frac{1}{12012}+\frac{1}{3686837}+\frac{1}{52286052}. |  | (5.187) |

Example 5.10.3 Let m = 537 m=537. Then n = 24 ​ m + 1 = 12889 n=24m+1=12889 is a prime. Note m 1 = 268 m_{1}=268 and (5.182) gives s 1 = 6 s_{1}=6 and t = 0 t=0. In fact,

 | 268 = − 7 + 275 ​ d ⟹ d = 1. 268=-7+275d\Longrightarrow d=1. |  | (5.188) |

Moreover, (5.185) becomes

 | 4 12889 = 1 3300 + 1 141779 + 1 3866700. \frac{4}{12889}=\frac{1}{3300}+\frac{1}{141779}+\frac{1}{3866700}. |  | (5.189) |

In the rest of this subsection, we assume OPEN s ≢ 0 ​ mod ​ 3) s\not\equiv 0\;\mbox{mod}\;3). By (5.168),

 | m 1 + t ≡ s ( mod ​ 4 ​ s + 3). m_{1}+t\equiv s\quad(\mbox{mod}\;4s+3). |  | (5.190) |

Hence

 | m 1 = s − t + c ⁡ ( 4 ​ s + 3) for some ​ c ∈ ℕ. m_{1}=s-t+c(4s+3)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.191) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 1) ​ ( 4 ​ s + 3). 6m+j+\ell+1=4(3c+1)(4s+3). |  | (5.192) |

The second expression in (2.28) and (3.122) yield

 | ( 48 ​ t + 11) | ( 3 ​ c + 1). (48t+11)|(3c+1). |  | (5.193) |

Therefore,

 | c = 32 ​ t + 7 + d ⁡ ( 48 ​ t + 11) for some ​ d ∈ ℕ. c=32t+7+d(48t+11)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.194) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 + 1 = 2 ​ [s − t + ( 32 ​ t + 7 + d ⁡ ( 48 ​ t + 11)) ​ ( 4 ​ s + 3)] + 1 \displaystyle 2m_{1}+1=2[s-t+(32t+7+d(48t+11))(4s+3)]+1 |  | (5.195) |

 |  | = \displaystyle= | 2 ​ [32 ​ s ​ t + 7 ​ s − t + ( d ⁡ ( 4 ​ s + 3) + 2 ​ s + 2) ​ ( 48 ​ t + 35)] − 1 \displaystyle 2[32st+7s-t+(d(4s+3)+2s+2)(48t+35)]-1 |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 11). 6m+j+\ell+1=4(3d+2)(4s+3)(48t+11). |  | (5.196) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 11) + 4 ​ ( 4 ​ s + 3) + ( 48 ​ t + 11) 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(4s+3)(48t+11)}+\frac{4(4s+3)+(48t+11)}{4(3d+2)(4s+3)(48t+11)(24m+1)} |  | (5.197) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 48 ​ t + 11) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(4s+3)(48t+11)}+\frac{1}{(3d+2)(48t+11)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 4 ​ s + 3) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(4s+3)(24m+1)}. |  |

Theorem 5.10 If m m is of the form (5.172), then the Erdös-Straus equation (5.174) holds. For a positive integer m m in (5.183), the Erdös-Straus equation (5.185) holds. When m m is of the form (5.195), the Erdös-Straus equation (5.197) holds.

Example 5.10.4 Let m = 717 m=717. Then n = 24 ​ m + 1 = 17209 n=24m+1=17209 is a prime. Note m 1 = 358 m_{1}=358 and (5.195) gives s = 1 s=1 and t = 0 t=0. In fact,

 | 358 = 50 + 77 ​ d ⟹ d = 4. 358=50+77d\Longrightarrow d=4. |  | (5.198) |

Moreover, (5.197) becomes

 | 4 17209 = 1 4312 + 1 2650186 + 1 6745928. \frac{4}{17209}=\frac{1}{4312}+\frac{1}{2650186}+\frac{1}{6745928}. |  | (5.199) |

### 5.11 Case m = 2 ​ m 1 + 1, j = 12 ​ r + 7 m=2m_{1}+1,j=12r+7 and ℓ = 12 ​ t + 10 \ell=12t+10

In this case,

 | ℑ 1 = 4 ​ ( 12 ​ r + 7), ℑ 2 = 48 ​ t + 43 \Im_{1}=4(12r+7),\quad\Im_{2}=48t+43 |  | (5.200) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 12 ​ ( m 1 + r + t + 2). 6m+j+\ell+1=12(m_{1}+r+t+2). |  | (5.201) |

According to the first expression in (2.28),

 | ( 12 ​ r + 7) | ( m 1 + r + t + 2); (12r+7)|(m_{1}+r+t+2); |  | (5.202) |

that is

 | m 1 + r + t + 2 ≡ 0 ( mod ​ 12 ​ r + 7). m_{1}+r+t+2\equiv 0\quad(\mbox{mod}\;12r+7). |  | (5.203) |

Thus

 | m 1 ≡ − r − t − 2 ( mod ​ 12 ​ r + 7). m_{1}\equiv-r-t-2\quad(\mbox{mod}\;12r+7). |  | (5.204) |

Hence

 | m 1 = − r − t − 2 + c ⁡ ( 12 ​ r + 7) for some ​ c ∈ ℕ. m_{1}=-r-t-2+c(12r+7)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.205) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 12 ​ c ​ ( 12 ​ r + 7). 6m+j+\ell+1=12c(12r+7). |  | (5.206) |

The second expression in (2.28) and (3.122) yield

 | ( 48 ​ t + 43) | c. (48t+43)|c. |  | (5.207) |

Therefore,

 | c = d ⁡ ( 48 ​ t + 43) for some ​ d ∈ ℕ. c=d(48t+43)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.208) |

This implies

 | m = 2 ​ m 1 + 1 = 2 ​ [− r − t + d ⁡ ( 12 ​ r + 7) ​ ( 48 ​ t + 43)] − 3 m=2m_{1}+1=2[-r-t+d(12r+7)(48t+43)]-3 |  | (5.209) |

and

 | 6 ​ m + j + ℓ + 1 = 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 43). 6m+j+\ell+1=12d(12r+7)(48t+43). |  | (5.210) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 43) + 4 ​ ( 12 ​ r + 7) + ( 48 ​ t + 43) 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{12d(12r+7)(48t+43)}+\frac{4(12r+7)+(48t+43)}{12d(12r+7)(48t+43)(24m+1)} |  | (5.211) |

 |  | = \displaystyle= | 1 12 ​ d ​ ( 12 ​ r + 7) ​ ( 48 ​ t + 43) + 1 3 ​ d ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{12d(12r+7)(48t+43)}+\frac{1}{3d(48t+43)(24m+1)} |  |

 |  |  | + 1 12 ​ d ​ ( 12 ​ r + 7) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{12d(12r+7)(24m+1)}. |  |

Theorem 5.11 If m m is of the form (5.209), then the Erdös-Straus equation (5.211) holds.

### 5.12 Case m = 2 ​ m 1 + 1, j = 12 ​ r + 11 m=2m_{1}+1,j=12r+11 and ℓ = 12 ​ t + 10 \ell=12t+10

Now

 | ℑ 1 = 4 ​ ( 12 ​ r + 11), ℑ 2 = 48 ​ t + 43 \Im_{1}=4(12r+11),\quad\Im_{2}=48t+43 |  | (5.212) |

by (5.1), and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ ( m 1 + r + t + 2) + 1). 6m+j+\ell+1=4(3(m_{1}+r+t+2)+1). |  | (5.213) |

According to the first expression in (2.28),

 | ( 12 ​ r + 11) | [3 ​ ( m 1 + r + t + 2) + 1]; (12r+11)|[3(m_{1}+r+t+2)+1]; |  | (5.214) |

that is

 | 3 ​ ( m 1 + r + t + 2) + 1 ≡ 0 ( mod ​ 12 ​ r + 11). 3(m_{1}+r+t+2)+1\equiv 0\quad(\mbox{mod}\;12r+11). |  | (5.215) |

Note

 | 3 ​ ( m 1 + r + t + 2) + 1 ≡ 2 ​ ( 12 ​ r + 11) ( mod ​ 12 ​ r + 11). 3(m_{1}+r+t+2)+1\equiv 2(12r+11)\quad(\mbox{mod}\;12r+11). |  | (5.216) |

Equivalently,

 | 3 ​ ( m 1 + t) ≡ 21 ​ r + 15 ( mod ​ 12 ​ r + 11). 3(m_{1}+t)\equiv 21r+15\quad(\mbox{mod}\;12r+11). |  | (5.217) |

Thus

 | m 1 ≡ 7 ​ r − t + 5 ( mod ​ 12 ​ r + 11). m_{1}\equiv 7r-t+5\quad(\mbox{mod}\;12r+11). |  | (5.218) |

Hence

 | m 1 = 7 ​ r − t + 5 + c ⁡ ( 12 ​ r + 11) for some ​ c ∈ ℕ. m_{1}=7r-t+5+c(12r+11)\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (5.219) |

Observe that

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ c + 2) ​ ( 12 ​ r + 11). 6m+j+\ell+1=4(3c+2)(12r+11). |  | (5.220) |

The second expression in (2.28) and (2.122) yield

 | ( 48 ​ t + 43) | ( 3 ​ c + 2). (48t+43)|(3c+2). |  | (5.221) |

Therefore,

 | c = 32 ​ t + 28 + d ⁡ ( 48 ​ t + 43) for some ​ d ∈ ℕ. c=32t+28+d(48t+43)\qquad\mbox{for some}\;\;d\in\mathbb{N}. |  | (5.222) |

This implies

 | m \displaystyle m | = \displaystyle= | 2 ​ m 1 + 1 = 2 ​ [7 ​ r − t + 5 + ( 32 ​ t + 28 + d ⁡ ( 48 ​ t + 43)) ​ ( 12 ​ r + 11)] + 1 \displaystyle 2m_{1}+1=2[7r-t+5+(32t+28+d(48t+43))(12r+11)]+1 |  | (5.223) |

 |  | = \displaystyle= | 2 ​ [15 ​ t − r + ( d ⁡ ( 12 ​ r + 11) + 8 ​ r + 7) ​ ( 48 ​ t + 43)] + 15 \displaystyle 2[15t-r+(d(12r+11)+8r+7)(48t+43)]+15 |  |

and

 | 6 ​ m + j + ℓ + 1 = 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 43). 6m+j+\ell+1=4(3d+2)(12r+11)(48t+43). |  | (5.224) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 43) + 4 ​ ( 12 ​ r + 11) + ( 48 ​ t + 43) 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{4(3d+2)(12r+11)(48t+43)}+\frac{4(12r+11)+(48t+43)}{4(3d+2)(12r+11)(24m+1)} |  | (5.225) |

 |  | = \displaystyle= | 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 48 ​ t + 43) + 1 ( 3 ​ d + 2) ​ ( 48 ​ t + 43) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{4(3d+2)(12r+11)(48t+43)}+\frac{1}{(3d+2)(48t+43)(24m+1)} |  |

 |  |  | + 1 4 ​ ( 3 ​ d + 2) ​ ( 12 ​ r + 11) ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{4(3d+2)(12r+11)(24m+1)}. |  |

Theorem 5.12 If m m is of the form (5.225), then the Erdös-Straus equation (5.227) holds.

## 6 Solutions with 2 s 2^{s} as a Numerator Summand

The complexity of last section comes from the fact 4 | ( 6 ​ m + k) 4|(6m+k). The larger power of 2 is involved in ℑ 1 = 4 ​ j \Im_{1}=4j in (5.1), and the more difficulties the Erdös-Straus equation has. In this section, we want to solve the equation with

 | ℑ 1 = 4 ​ j, ℑ 2 = 4 ​ ℓ + 3, \Im_{1}=4j,\quad\Im_{2}=4\ell+3, |  | (6.1) |

where j j is any power of 2 and ℓ \ell is a related positive integer. Indeed, we have applied simple 2-adic analysis to some known such solutions and obtained various ansatz of solving the equation. The solutions in this section may play the analogous roles in the tame solutions of the Erdös-Straus equation as those the sporadic groups play in the theory of finite simple groups.

### 6.1 Case j = 2 2 ​ ι + 1 j=2^{2\iota+1} and ℓ = 3 \ell=3

In this case, we consider

 | m = 2 ​ ( 4 ι − 1) 3 + a × 2 2 ​ ι m=\frac{2(4^{\iota}-1)}{3}+a\times 2^{2\iota} |  | (6.2) |

with ι, a ∈ ℕ \iota,a\in\mathbb{N} and ι ≥ 1 \iota\geq 1.. Moreover,

 | ℑ 1 = 4 ​ j = 2 2 ​ ι + 3, ℑ 2 = 4 ​ ℓ + 3 = 15. \Im_{1}=4j=2^{2\iota+3},\quad\Im_{2}=4\ell+3=15. |  | (6.3) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 4 ​ ( 4 ι − 1) + 3 ​ a × 2 2 ​ ι + 1 + 2 2 ​ ι + 1 + 4 \displaystyle 4(4^{\iota}-1)+3a\times 2^{2\iota+1}+2^{2\iota+1}+4 |  | (6.4) |

 |  | = \displaystyle= | 4 ι + 1 + 3 ​ a × 2 2 ​ ι + 1 + 2 2 ​ ι + 1 \displaystyle 4^{\iota+1}+3a\times 2^{2\iota+1}+2^{2\iota+1} |  |

 |  | = \displaystyle= | 3 × 2 2 ​ ι + 1 + 3 ​ a × 2 2 ​ ι + 1 = 3 ​ ( a + 1) ​ 2 2 ​ ι + 1. \displaystyle 3\times 2^{2\iota+1}+3a\times 2^{2\iota+1}=3(a+1)2^{2\iota+1}. |  |

According to (2.28),

 | [15 × 2 2 ​ ι + 3] | [3 ​ ( a + 1) ​ 2 2 ​ ι + 1] ⟹ 20 | ( a + 1). [15\times 2^{2\iota+3}]|[3(a+1)2^{2\iota+1}]\Longrightarrow 20|(a+1). |  | (6.5) |

Thus

 | a = 19 + 20 ​ c with ​ c ∈ ℕ. a=19+20c\quad\mbox{with}\;\;c\in\mathbb{N}. |  | (6.6) |

Moreover,

 | m = 2 ​ ( 4 ι − 1) 3 + ( 19 + 20 ​ c) ​ 2 2 ​ ι m=\frac{2(4^{\iota}-1)}{3}+(19+20c)2^{2\iota} |  | (6.7) |

and

 | 6 ​ m + j + ℓ + 1 = 15 ​ ( c + 1) ​ 2 2 ​ ι + 3. 6m+j+\ell+1=15(c+1)2^{2\iota+3}. |  | (6.8) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 15 ​ ( c + 1) ​ 2 2 ​ ι + 3 + 2 2 ​ ι + 3 + 15 15 ​ ( c + 1) ​ 2 2 ​ ι + 3 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{15(c+1)2^{2\iota+3}}+\frac{2^{2\iota+3}+15}{15(c+1)2^{2\iota+3}(24m+1)} |  | (6.9) |

 |  | = \displaystyle= | 1 15 ​ ( c + 1) ​ 2 2 ​ ι + 3 + 1 15 ​ ( c + 1) ​ ( 24 ​ m + 1) + 1 ( c + 1) ​ 2 2 ​ ι + 3 ​ ( 24 ​ m + 1). \displaystyle\frac{1}{15(c+1)2^{2\iota+3}}+\frac{1}{15(c+1)(24m+1)}+\frac{1}{(c+1)2^{2\iota+3}(24m+1)}. |  |

Theorem 6.1 If m m is of the form (6.7), then the Erdös-Straus equation (6.9) holds.

Example 6.1.1 Let m = 314 m=314. Then 24 ​ m + 1 = 7537 24m+1=7537 is a prime. Moreover, (6.7) holds with ι = 2 \iota=2 and c = 0 c=0. Equation (6.9) implies

 | 4 7537 = 1 1920 + 1 113955 + 1 964736. \frac{4}{7537}=\frac{1}{1920}+\frac{1}{113955}+\frac{1}{964736}. |  | (6.10) |

Example 6.1.2 Let m = 634 m=634. Then 24 ​ m + 1 = 15217 24m+1=15217 is a prime. Moreover, (6.7) holds with ι = 2 \iota=2 and c = 1 c=1. Equation (6.9) implies

 | 4 15217 = 1 3840 + 1 456510 + 1 3895552. \frac{4}{15217}=\frac{1}{3840}+\frac{1}{456510}+\frac{1}{3895552}. |  | (6.11) |

Example 6.1.3 Let m = 1274 m=1274. Then 24 ​ m + 1 = 30577 24m+1=30577 is a prime. Moreover, (6.7) holds with ι = 2 \iota=2 and c = 3 c=3. Equation (6.9) implies

 | 4 30577 = 1 7680 + 1 1834620 + 1 15655424. \frac{4}{30577}=\frac{1}{7680}+\frac{1}{1834620}+\frac{1}{15655424}. |  | (6.12) |

### 6.2 Case j = 2 r j=2^{r} and ℓ = 11 \ell=11

Next we suppose

 | m = 2 r − 1 − 2 + a × 2 r + 1 m=2^{r-1}-2+a\times 2^{r+1} |  | (6.13) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 1 r\geq 1. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 47. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=47. |  | (6.14) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 12 ​ ( 2 r − 2 − 1) + 3 ​ a × 2 r + 2 + 2 r + 12 \displaystyle 12(2^{r-2}-1)+3a\times 2^{r+2}+2^{r}+12 |  | (6.15) |

 |  | = \displaystyle= | 3 × 2 r + 3 ​ a × 2 r + 2 + 2 r \displaystyle 3\times 2^{r}+3a\times 2^{r+2}+2^{r} |  |

 |  | = \displaystyle= | 2 r + 2 + 3 ​ a × 2 r + 2 = ( 3 ​ a + 1) ​ 2 r + 2. \displaystyle 2^{r+2}+3a\times 2^{r+2}=(3a+1)2^{r+2}. |  |

According to (2.28),

 | [47 × 2 r + 2] | [( 3 ​ a + 1) ​ 2 r + 2] ⟹ 47 | ( 3 ​ a + 1). [47\times 2^{r+2}]|[(3a+1)2^{r+2}]\Longrightarrow 47|(3a+1). |  | (6.16) |

Thus

 | a = 31 + 47 ​ c with ​ c ∈ ℕ. a=31+47c\quad\mbox{with}\;\;c\in\mathbb{N}. |  | (6.17) |

Moreover,

 | m = 2 r − 1 − 2 + ( 31 + 47 ​ c) ​ 2 r + 1 m=2^{r-1}-2+(31+47c)2^{r+1} |  | (6.18) |

and

 | 6 ​ m + j + ℓ + 1 = 47 ​ ( 3 ​ c + 2) ​ 2 r + 2. 6m+j+\ell+1=47(3c+2)2^{r+2}. |  | (6.19) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 47 ​ ( 3 ​ c + 2) ​ 2 r + 2 + 2 r + 2 + 47 47 ​ ( 3 ​ c + 2) ​ 2 r + 2 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{47(3c+2)2^{r+2}}+\frac{2^{r+2}+47}{47(3c+2)2^{r+2}(24m+1)} |  | (6.20) |

 |  | = \displaystyle= | 1 47 ​ ( 3 ​ c + 2) ​ 2 r + 2 + 1 47 ​ ( 3 ​ c + 2) ​ ( 24 ​ m + 1) + 1 ( 3 ​ c + 2) ​ 2 r + 2 ​ ( 24 ​ m + 1). \displaystyle\frac{1}{47(3c+2)2^{r+2}}+\frac{1}{47(3c+2)(24m+1)}+\frac{1}{(3c+2)2^{r+2}(24m+1)}. |  |

Theorem 6.2 If m m is of the form (6.18), then the Erdös-Straus equation (6.20) holds.

Example 6.2.1 Let m = 248 m=248. Then 24 ​ m + 1 = 5953 24m+1=5953 is a prime. Moreover, (6.18) holds with r = 2 r=2 and c = 0 c=0. Equation (6.20) implies

 | 4 5953 = 1 1504 + 1 559582 + 1 190496. \frac{4}{5953}=\frac{1}{1504}+\frac{1}{559582}+\frac{1}{190496}. |  | (6.21) |

Example 6.2.2 Let m = 498 m=498. Then 24 ​ m + 1 = 11953 24m+1=11953 is a prime. Moreover, (6.18) holds with r = 3 r=3 and c = 0 c=0. Equation (6.20) implies

 | 4 11953 = 1 3008 + 1 1123582 + 1 764992. \frac{4}{11953}=\frac{1}{3008}+\frac{1}{1123582}+\frac{1}{764992}. |  | (6.22) |

### 6.3 Case j = 2 r j=2^{r} and ℓ = 2 r + 1 − 1 \ell=2^{r+1}-1 (I)

Assume

 | m = 2 r − 1 + a × 2 r m=2^{r-1}+a\times 2^{r} |  | (6.23) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 1 r\geq 1. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 2 r + 3 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=2^{r+3}-1. |  | (6.24) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 3 × 2 r + 3 ​ a × 2 r + 1 + 2 r + 2 r + 1 \displaystyle 3\times 2^{r}+3a\times 2^{r+1}+2^{r}+2^{r+1} |  | (6.25) |

 |  | = \displaystyle= | 6 × 2 r + 3 ​ a × 2 r + 1 = 3 ​ ( a + 1) ​ 2 r + 1. \displaystyle 6\times 2^{r}+3a\times 2^{r+1}=3(a+1)2^{r+1}. |  |

According to (2.28),

 | [2 r + 2 ​ ( 2 r + 3 − 1)] | [3 ​ ( a + 1) ​ 2 r + 1] ⟹ ( 2 ​ ( 2 r + 3 − 1)) | [3 ​ ( a + 1)]. [2^{r+2}(2^{r+3}-1)]|[3(a+1)2^{r+1}]\Longrightarrow(2(2^{r+3}-1))|[3(a+1)]. |  | (6.26) |

Thus

 | a = 2 ​ c ​ ( 2 r + 3 − 1) 3 − 1 for some ​ c ∈ ℕ. a=\frac{2c(2^{r+3}-1)}{3}-1\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.27) |

Moreover,

 | m = − 2 r − 1 + 2 ​ c ​ ( 2 r + 3 − 1) ​ 2 r 3 m=-2^{r-1}+\frac{2c(2^{r+3}-1)2^{r}}{3} |  | (6.28) |

and

 | 6 ​ m + j + ℓ + 1 = 2 ​ c ​ ( 2 r + 3 − 1) ​ 2 r + 1 = c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2. 6m+j+\ell+1=2c(2^{r+3}-1)2^{r+1}=c(2^{r+3}-1)2^{r+2}. |  | (6.29) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2 + 2 r + 2 + ( 2 r + 3 − 1) c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(2^{r+3}-1)2^{r+2}}+\frac{2^{r+2}+(2^{r+3}-1)}{c(2^{r+3}-1)2^{r+2}(24m+1)} |  | (6.30) |

 |  | = \displaystyle= | 1 c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2 + 1 c ⁡ ( 2 r + 3 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 2 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(2^{r+3}-1)2^{r+2}}+\frac{1}{c(2^{r+3}-1)(24m+1)}+\frac{1}{2^{r+2}c(24m+1)}. |  |

Theorem 6.3 If m m is of the form (6.28), then the Erdös-Straus equation (6.30) holds.

Example 6.3.1 Let m = 1982 m=1982. Then 24 ​ m + 1 = 47569 24m+1=47569 is a prime. Moreover, (6.28) holds with r = 2 r=2 and c = 8 c=8. Equation (6.30) implies

 | 4 47569 = 1 11904 + 1 17968668 + 1 18266496. \frac{4}{47569}=\frac{1}{11904}+\frac{1}{17968668}+\frac{1}{18266496}. |  | (6.31) |

Example 6.3.2 Let m = 668 m=668. Then 24 ​ m + 1 = 16033 24m+1=16033 is a prime. Moreover, (6.28) holds with r = 3 r=3 and c = 2 c=2. Equation (6.30) implies

 | 4 16033 = 1 4032 + 1 2020158 + 1 1026112. \frac{4}{16033}=\frac{1}{4032}+\frac{1}{2020158}+\frac{1}{1026112}. |  | (6.32) |

### 6.4 Case j = 2 r j=2^{r} and ℓ = 2 r + 2 − 1 \ell=2^{r+2}-1

Let

 | m = 2 r − 1 + a × 2 r + 2 m=2^{r-1}+a\times 2^{r+2} |  | (6.33) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 1 r\geq 1. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 2 r + 4 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=2^{r+4}-1. |  | (6.34) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 3 × 2 r + 3 ​ a × 2 r + 3 + 2 r + 2 r + 2 \displaystyle 3\times 2^{r}+3a\times 2^{r+3}+2^{r}+2^{r+2} |  | (6.35) |

 |  | = \displaystyle= | 8 × 2 r + 3 ​ a × 2 r + 3 = ( 3 ​ a + 1) ​ 2 r + 3. \displaystyle 8\times 2^{r}+3a\times 2^{r+3}=(3a+1)2^{r+3}. |  |

According to (2.28),

 | [2 r + 2 ( 2 r + 4 − 1)] | [3 a + 1) 2 r + 3] ⟹ ( 2 r + 4 − 1) | ( 3 a + 1). [2^{r+2}(2^{r+4}-1)]|[3a+1)2^{r+3}]\Longrightarrow(2^{r+4}-1)|(3a+1). |  | (6.36) |

Thus

 | 3 ​ a = c ⁡ ( 2 r + 4 − 1) − 1 with ​ c ∈ ℕ. 3a=c(2^{r+4}-1)-1\quad\mbox{with}\;\;c\in\mathbb{N}. |  | (6.37) |

Moreover,

 | m = 2 r − 1 + 1 3 ​ [c ⁡ ( 2 r + 4 − 1) − 1] ​ 2 r + 2 m=2^{r-1}+\frac{1}{3}[c(2^{r+4}-1)-1]2^{r+2} |  | (6.38) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 2 r + 4 − 1) ​ 2 r + 3. 6m+j+\ell+1=c(2^{r+4}-1)2^{r+3}. |  | (6.39) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 2 r + 4 − 1) ​ 2 r + 3 + 2 r + 2 + ( 2 r + 4 − 1) c ⁡ ( 2 r + 4 − 1) ​ 2 r + 3 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(2^{r+4}-1)2^{r+3}}+\frac{2^{r+2}+(2^{r+4}-1)}{c(2^{r+4}-1)2^{r+3}(24m+1)} |  | (6.40) |

 |  | = \displaystyle= | 1 c ⁡ ( 2 r + 4 − 1) ​ 2 r + 3 + 1 2 ​ c ​ ( 2 r + 4 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 3 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(2^{r+4}-1)2^{r+3}}+\frac{1}{2c(2^{r+4}-1)(24m+1)}+\frac{1}{2^{r+3}c(24m+1)}. |  |

Theorem 6.4 If m m is of the form (6.38), then the Erdös-Straus equation (6.40) holds.

Example 6.4.1 Let m = 1348 m=1348. Then 24 ​ m + 1 = 32353 24m+1=32353 is a prime. Moreover, (6.38) holds with r = 3 r=3 and c = 1 c=1. Equation (6.40) implies

 | 4 32353 = 1 8128 + 1 8217662 + 1 2070592. \frac{4}{32353}=\frac{1}{8128}+\frac{1}{8217662}+\frac{1}{2070592}. |  | (6.41) |

### 6.5 Case j = 2 r j=2^{r} and ℓ = 2 r + 1 − 1 \ell=2^{r+1}-1 (II)

Suppose

 | m = 3 × 2 r − 1 + a × 2 r + 1 m=3\times 2^{r-1}+a\times 2^{r+1} |  | (6.42) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 1 r\geq 1. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 3 = 4 ​ ℓ + 3 = 2 r + 3 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{3}=4\ell+3=2^{r+3}-1. |  | (6.43) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 9 × 2 r + 3 ​ a × 2 r + 2 + 2 r + 2 r + 1 \displaystyle 9\times 2^{r}+3a\times 2^{r+2}+2^{r}+2^{r+1} |  | (6.44) |

 |  | = \displaystyle= | 12 × 2 r + 3 ​ a × 2 r + 2 = 3 ​ ( a + 1) ​ 2 r + 2. \displaystyle 12\times 2^{r}+3a\times 2^{r+2}=3(a+1)2^{r+2}. |  |

According to (2.28),

 | [( 2 r + 3 − 1) ​ 2 r + 2] | [3 ​ ( a + 1) ​ 2 r + 2] ⟹ ( 2 r + 3 − 1) | [3 ​ ( a + 1)]. [(2^{r+3}-1)2^{r+2}]|[3(a+1)2^{r+2}]\Longrightarrow(2^{r+3}-1)|[3(a+1)]. |  | (6.45) |

Thus

 | a = ( 2 r + 3 − 1) ​ c 3 − 1 for some ​ c ∈ ℕ. a=\frac{(2^{r+3}-1)c}{3}-1\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.46) |

Moreover,

 | m = − 2 r − 1 + ( 2 r + 3 − 1) ​ 2 r + 1 ​ c 3 m=-2^{r-1}+\frac{(2^{r+3}-1)2^{r+1}c}{3} |  | (6.47) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2. 6m+j+\ell+1=c(2^{r+3}-1)2^{r+2}. |  | (6.48) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2 + 2 r + 2 + ( 2 r + 3 − 1) c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(2^{r+3}-1)2^{r+2}}+\frac{2^{r+2}+(2^{r+3}-1)}{c(2^{r+3}-1)2^{r+2}(24m+1)} |  | (6.49) |

 |  | = \displaystyle= | 1 c ⁡ ( 2 r + 3 − 1) ​ 2 r + 2 + 1 c ⁡ ( 2 r + 3 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 2 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(2^{r+3}-1)2^{r+2}}+\frac{1}{c(2^{r+3}-1)(24m+1)}+\frac{1}{2^{r+2}c(24m+1)}. |  |

Theorem 6.5 If m m is of the form (6.47), then the Erdös-Straus equation (6.49) holds.

Example 6.5.1 Let m = 1734 m=1734. Then 24 ​ m + 1 = 41617 24m+1=41617 is a prime. When ι = 1 \iota=1,

 | ℓ = 2 3 − 1 = 7, ℑ 2 = 2 5 − 1 = 31. \ell=2^{3}-1=7,\quad\Im_{2}=2^{5}-1=31. |  | (6.50) |

Moreover, (6.47) holds with r = 2 r=2 and c = 21 c=21. Equation (6.49) implies

 | 4 41617 = 1 10416 + 1 27092667 + 1 13983312. \frac{4}{41617}=\frac{1}{10416}+\frac{1}{27092667}+\frac{1}{13983312}. |  | (6.51) |

### 6.6 Case j = 2 r j=2^{r} and ℓ = 5 × 2 r − 1 \ell=5\times 2^{r}-1

Now we assume

 | m = 2 r + a × 2 r + 1 m=2^{r}+a\times 2^{r+1} |  | (6.52) |

with a, r ∈ ℕ a,r\in\mathbb{N}. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 5 × 2 r + 2 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=5\times 2^{r+2}-1. |  | (6.53) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 6 × 2 r + 3 ​ a × 2 r + 2 + 2 r + 5 × 2 r \displaystyle 6\times 2^{r}+3a\times 2^{r+2}+2^{r}+5\times 2^{r} |  | (6.54) |

 |  | = \displaystyle= | 12 × 2 r + 3 ​ a × 2 r + 2 = 3 ​ ( a + 1) ​ 2 r + 2. \displaystyle 12\times 2^{r}+3a\times 2^{r+2}=3(a+1)2^{r+2}. |  |

According to (2.28),

 | [( 5 × 2 r + 2 − 1) ​ 2 r + 2] | [3 ​ ( a + 1) ​ 2 r + 2] ⟹ ( 5 × 2 r + 2 − 1) | [3 ​ ( a + 1)]. [(5\times 2^{r+2}-1)2^{r+2}]|[3(a+1)2^{r+2}]\Longrightarrow(5\times 2^{r+2}-1)|[3(a+1)]. |  | (6.55) |

Thus

 | a = ( 5 × 2 r + 2 − 1) ​ c 3 − 1 for some ​ c ∈ ℕ. a=\frac{(5\times 2^{r+2}-1)c}{3}-1\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.56) |

Moreover,

 | m = − 2 r + ( 5 × 2 r + 2 − 1) ​ 2 r + 1 ​ c 3 m=-2^{r}+\frac{(5\times 2^{r+2}-1)2^{r+1}c}{3} |  | (6.57) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 5 × 2 r + 2 − 1) ​ 2 r + 2. 6m+j+\ell+1=c(5\times 2^{r+2}-1)2^{r+2}. |  | (6.58) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 5 × 2 r + 2 − 1) ​ 2 r + 2 + 2 r + 2 + ( 5 × 2 r + 2 − 1) c ⁡ ( 5 × 2 r + 2 − 1) ​ 2 r + 2 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(5\times 2^{r+2}-1)2^{r+2}}+\frac{2^{r+2}+(5\times 2^{r+2}-1)}{c(5\times 2^{r+2}-1)2^{r+2}(24m+1)} |  | (6.59) |

 |  | = \displaystyle= | 1 c ⁡ ( 5 × 2 r + 2 − 1) ​ 2 r + 2 + 1 c ⁡ ( 5 × 2 r + 2 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 2 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(5\times 2^{r+2}-1)2^{r+2}}+\frac{1}{c(5\times 2^{r+2}-1)(24m+1)}+\frac{1}{2^{r+2}c(24m+1)}. |  |

Theorem 6.6 If m m is of the form (6.57), then the Erdös-Straus equation (6.59) holds.

Example 6.6.1 Let m = 1260 m=1260. Then 24 ​ m + 1 = 30241 24m+1=30241 is a prime. When ι = 1 \iota=1,

 | ℓ = 5 × 4 − 1 = 19, 4 ​ ℓ + ι 2 = 5 × 4 2 − 1 = 79. \ell=5\times 4-1=19,\quad 4\ell+\iota_{2}=5\times 4^{2}-1=79. |  | (6.60) |

Moreover, (6.57) holds with r = 2 r=2 and c = 6 c=6. Equation (6.59) implies

 | 4 30241 = 1 7584 + 1 14334234 + 1 2903136. \frac{4}{30241}=\frac{1}{7584}+\frac{1}{14334234}+\frac{1}{2903136}. |  | (6.61) |

### 6.7 Case j = 2 r j=2^{r} and ℓ = 7 × 2 r + 1 − 1 \ell=7\times 2^{r+1}-1

Let

 | m = 2 r − 1 + a × 2 r m=2^{r-1}+a\times 2^{r} |  | (6.62) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 1 r\geq 1. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 7 × 2 r + 3 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=7\times 2^{r+3}-1. |  | (6.63) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 3 × 2 r + 3 ​ a × 2 r + 1 + 2 r + 7 × 2 r + 1 \displaystyle 3\times 2^{r}+3a\times 2^{r+1}+2^{r}+7\times 2^{r+1} |  | (6.64) |

 |  | = \displaystyle= | 9 × 2 r + 1 + 3 ​ a × 2 r + 1 = 3 ​ ( a + 3) ​ 2 r + 1. \displaystyle 9\times 2^{r+1}+3a\times 2^{r+1}=3(a+3)2^{r+1}. |  |

According to (2.28),

 | [( 7 × 2 r + 3 − 1) 2 r + 2] | 3 ( a + 3) 2 r + 1] ⟹ [2 ( 7 × 2 r + 3 − 1)] | [3 ( a + 3)]. [(7\times 2^{r+3}-1)2^{r+2}]|3(a+3)2^{r+1}]\Longrightarrow[2(7\times 2^{r+3}-1)]|[3(a+3)]. |  | (6.65) |

Thus

 | a = 2 ​ c ​ ( 7 × 2 r + 3 − 1) 3 − 3 for some ​ c ∈ ℕ. a=\frac{2c(7\times 2^{r+3}-1)}{3}-3\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.66) |

Moreover,

 | m = − 5 × 2 r − 1 + c ⁡ ( 7 × 2 r + 3 − 1) 3 2 r + 1 m=-5\times 2^{r-1}+\frac{c(7\times 2^{r+3}-1)}{3}2^{r+1} |  | (6.67) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 7 × 2 r + 3 − 1) ​ 2 r + 2. 6m+j+\ell+1=c(7\times 2^{r+3}-1)2^{r+2}. |  | (6.68) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 7 × 2 r + 3 − 1) ​ 2 r + 2 + 2 r + 2 + ( 7 × 2 r + 3 − 1) c ⁡ ( 7 × 2 r + 3 − 1) ​ 2 r + 2 \displaystyle\frac{4}{24m+1}=\frac{1}{c(7\times 2^{r+3}-1)2^{r+2}}+\frac{2^{r+2}+(7\times 2^{r+3}-1)}{c(7\times 2^{r+3}-1)2^{r+2}} |  | (6.69) |

 |  | = \displaystyle= | 1 c ⁡ ( 7 × 2 r + 3 − 1) ​ 2 r + 2 + 1 c ⁡ ( 7 × 2 r + 3 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 2 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(7\times 2^{r+3}-1)2^{r+2}}+\frac{1}{c(7\times 2^{r+3}-1)(24m+1)}+\frac{1}{2^{r+2}c(24m+1)}. |  |

Theorem 6.7 If m m is of the form (6.67), then the Erdös-Straus equation (6.69) holds.

Example 6.7.1 Let m = 1774 m=1774. Then 24 ​ m + 1 = 42557 24m+1=42557 is a prime. Moreover, (6.67) holds with r = 2 r=2 and c = 3 c=3. Equation (6.69) implies

 | 4 42557 = 1 10704 + 1 28470633 + 1 2042736. \frac{4}{42557}=\frac{1}{10704}+\frac{1}{28470633}+\frac{1}{2042736}. |  | (6.70) |

### 6.8 Case j = 2 r j=2^{r} and ℓ = 9 × 2 r − 1 \ell=9\times 2^{r}-1

Let

 | m = 2 r + a × 2 r + 3 m=2^{r}+a\times 2^{r+3} |  | (6.71) |

with a, r ∈ ℕ a,r\in\mathbb{N}.

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 9 × 2 r + 2 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=9\times 2^{r+2}-1. |  | (6.72) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 6 × 2 r + 3 ​ a × 2 r + 4 + 2 r + 9 × 2 r \displaystyle 6\times 2^{r}+3a\times 2^{r+4}+2^{r}+9\times 2^{r} |  | (6.73) |

 |  | = \displaystyle= | 16 × 2 r + 3 ​ a × 2 r + 4 = ( 3 ​ a + 1) ​ 2 r + 4. \displaystyle 16\times 2^{r}+3a\times 2^{r+4}=(3a+1)2^{r+4}. |  |

According to (2.28),

 | [( 9 × 2 r + 2 − 1) 2 r + 2] [( 3 a + 1) 2 r + 4] ⟹ ( 9 × 2 r + 2 − 1) | ( 3 a + 1)]. [(9\times 2^{r+2}-1)2^{r+2}][(3a+1)2^{r+4}]\Longrightarrow(9\times 2^{r+2}-1)|(3a+1)]. |  | (6.74) |

Thus

 | a = c ⁡ ( 9 × 2 r + 2 − 1) − 1 3 for some ​ c ∈ ℕ. a=\frac{c(9\times 2^{r+2}-1)-1}{3}\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.75) |

Moreover,

 | m = 2 r + [c ⁡ ( 9 × 2 r + 2 − 1) − 1] ​ 2 r + 3 3 m=2^{r}+\frac{[c(9\times 2^{r+2}-1)-1]2^{r+3}}{3} |  | (6.76) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 9 × 2 r + 2 − 1) ​ 2 r + 4. 6m+j+\ell+1=c(9\times 2^{r+2}-1)2^{r+4}. |  | (6.77) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 9 × 2 r + 2 − 1) ​ 2 r + 4 + 2 r + 2 + ( 9 × 2 r + 2 − 1) c ⁡ ( 9 × 2 r + 2 − 1) ​ 2 r + 4 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(9\times 2^{r+2}-1)2^{r+4}}+\frac{2^{r+2}+(9\times 2^{r+2}-1)}{c(9\times 2^{r+2}-1)2^{r+4}(24m+1)} |  | (6.78) |

 |  | = \displaystyle= | 1 c ⁡ ( 9 × 2 r + 2 − 1) ​ 2 r + 4 + 1 4 ​ c ​ ( 9 × 2 r + 2 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 4 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(9\times 2^{r+2}-1)2^{r+4}}+\frac{1}{4c(9\times 2^{r+2}-1)(24m+1)}+\frac{1}{2^{r+4}c(24m+1)}. |  |

Theorem 6.8 If m m is of the form (6.76), then the Erdös-Straus equation (6.78) holds.

Example 6.8.1 Let m = 754 m=754. Then 24 ​ m + 1 = 18097 24m+1=18097 is a prime. Moreover, (6.76) holds with r = 1 r=1 and c = 2 c=2. Equation (6.78) implies

 | 4 18097 = 1 4544 + 1 10279096 + 1 1158208. \frac{4}{18097}=\frac{1}{4544}+\frac{1}{10279096}+\frac{1}{1158208}. |  | (6.79) |

### 6.9 Case j = 2 r j=2^{r} and ℓ = 13 × 2 r − 1 \ell=13\times 2^{r}-1

Consider

 | m = 2 r + 5 ​ a × 2 r + 2 m=2^{r}+5a\times 2^{r+2} |  | (6.80) |

with a, r ∈ ℕ a,r\in\mathbb{N}. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 13 × 2 r + 2 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=13\times 2^{r+2}-1. |  | (6.81) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 6 × 2 r + 30 ​ a × 2 r + 2 + 2 r + 13 × 2 r \displaystyle 6\times 2^{r}+30a\times 2^{r+2}+2^{r}+13\times 2^{r} |  | (6.82) |

 |  | = \displaystyle= | 5 × 2 r + 2 + 30 ​ a × 2 r + 2 = 5 ​ ( 6 ​ a + 1) ​ 2 r + 2. \displaystyle 5\times 2^{r+2}+30a\times 2^{r+2}=5(6a+1)2^{r+2}. |  |

According to (2.28),

 | [( 13 × 2 r + 2 − 1) ​ 2 r + 2] ​ [5 ​ ( 6 ​ a + 1) ​ 2 r + 2] ⟹ ( 13 × 2 r + 2 − 1) | [5 ​ ( 6 ​ a + 1)]. [(13\times 2^{r+2}-1)2^{r+2}][5(6a+1)2^{r+2}]\Longrightarrow(13\times 2^{r+2}-1)|[5(6a+1)]. |  | (6.83) |

Thus

 | a = c ⁡ ( 13 × 2 r + 2 − 1) − 5 30 for some ​ c ∈ ℕ. a=\frac{c(13\times 2^{r+2}-1)-5}{30}\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.84) |

Moreover,

 | m = 2 r + [c ⁡ ( 13 × 2 r + 2 − 1) − 5] ​ 2 r + 1 3 m=2^{r}+\frac{[c(13\times 2^{r+2}-1)-5]2^{r+1}}{3} |  | (6.85) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 13 × 2 r + 2 − 1) ​ 2 r + 2. 6m+j+\ell+1=c(13\times 2^{r+2}-1)2^{r+2}. |  | (6.86) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 13 × 2 r + 2 − 1) ​ 2 r + 2 + 2 r + 2 + ( 13 × 2 r + 2 − 1) c ⁡ ( 13 × 2 r + 2 − 1) ​ 2 r + 2 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(13\times 2^{r+2}-1)2^{r+2}}+\frac{2^{r+2}+(13\times 2^{r+2}-1)}{c(13\times 2^{r+2}-1)2^{r+2}(24m+1)} |  | (6.87) |

 |  | = \displaystyle= | 1 c ⁡ ( 13 × 2 r + 2 − 1) ​ 2 r + 2 + 1 c ⁡ ( 13 × 2 r + 2 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 2 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(13\times 2^{r+2}-1)2^{r+2}}+\frac{1}{c(13\times 2^{r+2}-1)(24m+1)}+\frac{1}{2^{r+2}c(24m+1)}. |  |

Theorem 6.9 If m m is of the form (6.85), then the Erdös-Straus equation (6.87) holds.

Example 6.9.1 Let m = 682 m=682. Then 24 ​ m + 1 = 16369 24m+1=16369 is a prime. Moreover, (6.85) holds with r = 1 r=1 and c = 5 c=5. Equation (6.87) implies

 | 4 16369 = 1 4120 + 1 8430035 + 1 654760. \frac{4}{16369}=\frac{1}{4120}+\frac{1}{8430035}+\frac{1}{654760}. |  | (6.88) |

### 6.10 Case j = 2 r j=2^{r} and ℓ = 19 × 2 r − 1 − 1 \ell=19\times 2^{r-1}-1

Suppose

 | m = 2 r − 2 + a × 2 r + 2 m=2^{r-2}+a\times 2^{r+2} |  | (6.89) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 2 r\geq 2. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 19 × 2 r + 1 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=19\times 2^{r+1}-1. |  | (6.90) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 3 × 2 r − 1 + 6 ​ a × 2 r + 2 + 2 r + 19 × 2 r − 1 \displaystyle 3\times 2^{r-1}+6a\times 2^{r+2}+2^{r}+19\times 2^{r-1} |  | (6.91) |

 |  | = \displaystyle= | 24 × 2 r − 1 + 6 ​ a × 2 r + 2 = 3 ​ ( 2 ​ a + 1) ​ 2 r + 2. \displaystyle 24\times 2^{r-1}+6a\times 2^{r+2}=3(2a+1)2^{r+2}. |  |

According to (2.28),

 | [( 19 × 2 r + 1 − 1) ​ 2 r + 2] | [3 ​ ( 2 ​ a + 1) ​ 2 r + 2] ⟹ ( 19 × 2 r + 1 − 1) | [3 ​ ( 2 ​ a + 1)]. [(19\times 2^{r+1}-1)2^{r+2}]|[3(2a+1)2^{r+2}]\Longrightarrow(19\times 2^{r+1}-1)|[3(2a+1)]. |  | (6.92) |

Thus

 | a = c ⁡ ( 19 × 2 r + 1 − 1) − 3 6 for some ​ c ∈ ℕ. a=\frac{c(19\times 2^{r+1}-1)-3}{6}\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.93) |

Moreover,

 | m = − 3 × 2 r − 2 + c ⁡ ( 19 × 2 r + 1 − 1) ​ 2 r + 1 3 m=-3\times 2^{r-2}+\frac{c(19\times 2^{r+1}-1)2^{r+1}}{3} |  | (6.94) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 19 × 2 r + 1 − 1) ​ 2 r + 2. 6m+j+\ell+1=c(19\times 2^{r+1}-1)2^{r+2}. |  | (6.95) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 19 × 2 r + 1 − 1) ​ 2 r + 2 + 2 r + 2 + ( 19 × 2 r + 1 − 1) c ⁡ ( 19 × 2 r + 1 − 1) ​ 2 r + 2 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(19\times 2^{r+1}-1)2^{r+2}}+\frac{2^{r+2}+(19\times 2^{r+1}-1)}{c(19\times 2^{r+1}-1)2^{r+2}(24m+1)} |  | (6.96) |

 |  | = \displaystyle= | 1 c ⁡ ( 19 × 2 r + 1 − 1) ​ 2 r + 2 + 1 c ⁡ ( 19 × 2 r + 1 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 2 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(19\times 2^{r+1}-1)2^{r+2}}+\frac{1}{c(19\times 2^{r+1}-1)(24m+1)}+\frac{1}{2^{r+2}c(24m+1)}. |  |

Theorem 6.10 If m m is of the form (6.94), then the Erdös-Straus equation (6.96) holds.

Example 6.10.1 Let m = 1602 m=1602. Then 24 ​ m + 1 = 38449 24m+1=38449 is a prime. Moreover, (6.94) holds with r = 3 r=3 and c = 1 c=1. Equation (6.96) implies

 | 4 38449 = 1 9696 + 1 11650047 + 1 1230368. \frac{4}{38449}=\frac{1}{9696}+\frac{1}{11650047}+\frac{1}{1230368}. |  | (6.97) |

### 6.11 Case j = 2 r + 2 j=2^{r+2} and ℓ = 3 × 2 r + 1 − 1 \ell=3\times 2^{r+1}-1

Consider

 | m = 2 r + a × 2 r + 3 m=2^{r}+a\times 2^{r+3} |  | (6.98) |

with a, r ∈ ℕ a,r\in\mathbb{N}. Then

 | ℑ 1 = 4 ​ j = 2 r + 4, ℑ 2 = 4 ​ ℓ + 3 = 3 × 2 r + 3 − 1. \Im_{1}=4j=2^{r+4},\quad\Im_{2}=4\ell+3=3\times 2^{r+3}-1. |  | (6.99) |

Observe

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 6 × 2 r + 3 ​ a × 2 r + 4 + 2 r + 2 + 3 × 2 r + 1 \displaystyle 6\times 2^{r}+3a\times 2^{r+4}+2^{r+2}+3\times 2^{r+1} |  | (6.100) |

 |  | = \displaystyle= | 16 × 2 r + 3 ​ a × 2 r + 4 = ( 3 ​ a + 1) ​ 2 r + 4. \displaystyle 16\times 2^{r}+3a\times 2^{r+4}=(3a+1)2^{r+4}. |  |

According to (2.28),

 | [( 3 × 2 r + 3 − 1) ​ 2 r + 4] | [( 3 ​ a + 1) ​ 2 r + 4] ⟹ ( 3 × 2 r + 3 − 1) | ( 3 ​ a + 1). [(3\times 2^{r+3}-1)2^{r+4}]|[(3a+1)2^{r+4}]\Longrightarrow(3\times 2^{r+3}-1)|(3a+1). |  | (6.101) |

Thus

 | a = c ⁡ ( 3 × 2 r + 3 − 1) − 1 3 for some ​ c ∈ ℕ. a=\frac{c(3\times 2^{r+3}-1)-1}{3}\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.102) |

Moreover,

 | m = 2 r + ( c ⁡ ( 3 × 2 r + 3 − 1) − 1) ​ 2 r + 3 3 m=2^{r}+\frac{(c(3\times 2^{r+3}-1)-1)2^{r+3}}{3} |  | (6.103) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 3 × 2 r + 3 − 1) ​ 2 r + 4. 6m+j+\ell+1=c(3\times 2^{r+3}-1)2^{r+4}. |  | (6.104) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 3 × 2 r + 3 − 1) ​ 2 r + 4 + 2 r + 4 + ( 3 × 2 r + 3 − 1) c ⁡ ( 3 × 2 r + 3 − 1) ​ 2 r + 4 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(3\times 2^{r+3}-1)2^{r+4}}+\frac{2^{r+4}+(3\times 2^{r+3}-1)}{c(3\times 2^{r+3}-1)2^{r+4}(24m+1)} |  | (6.105) |

 |  | = \displaystyle= | 1 c ⁡ ( 3 × 2 r + 3 − 1) ​ 2 r + 4 + 1 c ⁡ ( 3 × 2 r + 3 − 1) ​ ( 24 ​ m + 1) + 1 2 r + 4 ​ c ​ ( 24 ​ m + 1). \displaystyle\frac{1}{c(3\times 2^{r+3}-1)2^{r+4}}+\frac{1}{c(3\times 2^{r+3}-1)(24m+1)}+\frac{1}{2^{r+4}c(24m+1)}. |  |

Theorem 6.11 If m m is of the form (6.103), then the Erdös-Straus equation (6.105) holds.

Example 6.11.1 Let m = 1225 m=1225. Then 24 ​ m + 1 = 29401 24m+1=29401 is a prime. Moreover, (6.103) holds with r = 0 r=0 and c = 20 c=20. Equation (6.105) implies

 | 4 29401 = 1 7360 + 1 13524460 + 1 9408320. \frac{4}{29401}=\frac{1}{7360}+\frac{1}{13524460}+\frac{1}{9408320}. |  | (6.106) |

To make the thing complete, we add the following two cases.

### 6.12 Case j = 2 r j=2^{r} and ℓ = 11 × 2 r − 1 − 1 \ell=11\times 2^{r-1}-1

Let

 | m = 2 r − 2 + a × 2 r + 2 m=2^{r-2}+a\times 2^{r+2} |  | (6.107) |

with a, r ∈ ℕ a,r\in\mathbb{N} and r ≥ 2 r\geq 2. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 11 × 2 r + 1 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=11\times 2^{r+1}-1. |  | (6.108) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 3 × 2 r − 1 + 3 ​ a × 2 r + 3 + 2 r + 11 × 2 r − 1 \displaystyle 3\times 2^{r-1}+3a\times 2^{r+3}+2^{r}+11\times 2^{r-1} |  | (6.109) |

 |  | = \displaystyle= | 16 × 2 r − 1 + 3 ​ a × 2 r + 3 = ( 3 ​ a + 1) ​ 2 r + 3. \displaystyle 16\times 2^{r-1}+3a\times 2^{r+3}=(3a+1)2^{r+3}. |  |

According to (2.28),

 | [( 11 × 2 r + 1 − 1) 2 r + 2] [( 3 a + 1) 2 r + 3] ⟹ ( 11 × 2 r + 1 − 1) | ( 3 a + 1)]. [(11\times 2^{r+1}-1)2^{r+2}][(3a+1)2^{r+3}]\Longrightarrow(11\times 2^{r+1}-1)|(3a+1)]. |  | (6.110) |

Thus

 | a = c ⁡ ( 11 × 2 r + 1 − 1) − 1 3 with ​ c ∈ ℕ. a=\frac{c(11\times 2^{r+1}-1)-1}{3}\quad\mbox{with}\;\;c\in\mathbb{N}. |  | (6.111) |

Moreover,

 | m = 2 r − 1 + [c ⁡ ( 11 × 2 r + 1 − 1) − 1] ​ 2 r + 2 3 m=2^{r-1}+\frac{[c(11\times 2^{r+1}-1)-1]2^{r+2}}{3} |  | (6.112) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 11 × 2 r + 1 − 1) ​ 2 r + 3. 6m+j+\ell+1=c(11\times 2^{r+1}-1)2^{r+3}. |  | (6.113) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 11 × 2 r + 1 − 1) ​ 2 r + 3 + 2 r + 2 + ( 11 × 2 r + 1 − 1) c ⁡ ( 11 × 2 r + 1 − 1) ​ 2 r + 3 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(11\times 2^{r+1}-1)2^{r+3}}+\frac{2^{r+2}+(11\times 2^{r+1}-1)}{c(11\times 2^{r+1}-1)2^{r+3}(24m+1)} |  | (6.114) |

 |  | = \displaystyle= | 1 c ⁡ ( 11 × 2 r + 1 − 1) ​ 2 r + 3 + 1 2 ​ c ​ ( 11 × 2 r + 1 − 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{c(11\times 2^{r+1}-1)2^{r+3}}+\frac{1}{2c(11\times 2^{r+1}-1)(24m+1)} |  |

 |  |  | + 1 2 r + 3 ​ c ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2^{r+3}c(24m+1)}. |  |

Theorem 6.12 If m m is of the form (6.112), then the Erdös-Straus equation (6.114) holds.

### 6.13 Case j = 2 r j=2^{r} and ℓ = 23 × 2 r − 1 \ell=23\times 2^{r}-1

Consider

 | m = 2 r + 2 + a × 2 r + 3 m=2^{r+2}+a\times 2^{r+3} |  | (6.115) |

with a, r ∈ ℕ a,r\in\mathbb{N}. Then

 | ℑ 1 = 4 ​ j = 2 r + 2, ℑ 2 = 4 ​ ℓ + 3 = 23 × 2 r + 2 − 1. \Im_{1}=4j=2^{r+2},\quad\Im_{2}=4\ell+3=23\times 2^{r+2}-1. |  | (6.116) |

Note

 | 6 ​ m + j + ℓ + 1 \displaystyle 6m+j+\ell+1 | = \displaystyle= | 6 × 2 r + 2 + 3 ​ a × 2 r + 4 + 2 r + 23 × 2 r \displaystyle 6\times 2^{r+2}+3a\times 2^{r+4}+2^{r}+23\times 2^{r} |  | (6.117) |

 |  | = \displaystyle= | 48 × 2 r + 3 ​ a × 2 r + 4 = 3 ​ ( a + 1) ​ 2 r + 4. \displaystyle 48\times 2^{r}+3a\times 2^{r+4}=3(a+1)2^{r+4}. |  |

According to (2.28),

 | [( 23 × 2 r + 2 − 1) ​ 2 r + 2] ​ [3 ​ ( a + 1) ​ 2 r + 3] ⟹ ( 23 × 2 r + 2 − 1) | [3 ​ ( a + 1)] [(23\times 2^{r+2}-1)2^{r+2}][3(a+1)2^{r+3}]\Longrightarrow(23\times 2^{r+2}-1)|[3(a+1)] |  | (6.118) |

Thus

 | a = c ⁡ ( 23 × 2 r + 2 − 1) 3 − 1 for some ​ c ∈ ℕ. a=\frac{c(23\times 2^{r+2}-1)}{3}-1\quad\mbox{for some}\;\;c\in\mathbb{N}. |  | (6.119) |

Moreover,

 | m = − 2 r + 2 + c ⁡ ( 23 × 2 r + 2 − 1) ​ 2 r + 3 3 m=-2^{r+2}+\frac{c(23\times 2^{r+2}-1)2^{r+3}}{3} |  | (6.120) |

and

 | 6 ​ m + j + ℓ + 1 = c ⁡ ( 23 × 2 r + 2 − 1) ​ 2 r + 4. 6m+j+\ell+1=c(23\times 2^{r+2}-1)2^{r+4}. |  | (6.121) |

Expression (2.11) becomes

 |  |  | 4 24 ​ m + 1 = 1 c ⁡ ( 23 × 2 r + 2 − 1) ​ 2 r + 4 + 2 r + 2 + ( 23 × 2 r + 2 − 1) c ⁡ ( 23 × 2 r + 2 − 1) ​ 2 r + 4 ​ ( 24 ​ m + 1) \displaystyle\frac{4}{24m+1}=\frac{1}{c(23\times 2^{r+2}-1)2^{r+4}}+\frac{2^{r+2}+(23\times 2^{r+2}-1)}{c(23\times 2^{r+2}-1)2^{r+4}(24m+1)} |  | (6.122) |

 |  | = \displaystyle= | 1 c ⁡ ( 23 × 2 r + 2 − 1) ​ 2 r + 4 + 1 4 ​ c ​ ( 23 × 2 r + 2 − 1) ​ ( 24 ​ m + 1) \displaystyle\frac{1}{c(23\times 2^{r+2}-1)2^{r+4}}+\frac{1}{4c(23\times 2^{r+2}-1)(24m+1)} |  |

 |  |  | + 1 2 r + 4 ​ c ​ ( 24 ​ m + 1). \displaystyle+\frac{1}{2^{r+4}c(24m+1)}. |  |

Theorem 6.13 If m m is of the form (6.120), then the Erdös-Straus equation (6.122) holds.

## References

- [1] K. Bradford, A note on the Erdös-Straus conjecture, Integers 21 (2021), Paper No. A24, 10pp.
- [2] M. Bright and D. Loughran, Brauer-Manin obstruction for Erdös-Straus surfaces, Bull. Lond. Math. Soc. 52 (2020), no. 4, 746–761.
- [3] C. Elscholtz and T. Tao, Counting the number of solutions to the equations on unit fractions, J. Aust. Math. Soc. 94 (2013), 50–105.
- [4] T. R. Hagedon, A proof of a conjecture on Egyptian fractions, Amer. Math. Monthly 107 (2000), no. 1, 62–63.
- [5] J. Huang and R. Vaughan, Mean value theorems for binary Egyptian fractions, J. Number Theory 121 (2011), no. 9, 1641–1656.
- [6] J. Huang and R. Vaughan, Mean value theorems for binary Egyptian fractions II, Acta Arith. 115 (2012), no. 3, 287–296.
- [7] J. Huang and R. Vaughan, On the exceptional set for binary Egyptian fractions, Bull. Lond. Math. Soc. 45 (2013), no. 4. 861–874.
- [8] C. Jia, The estimate for mean values on prime numbers relative to 4 / n = 1 / n 1 + 1 / n 2 + 1 / n 3 4/n=1/{n_{1}}+1/{n_{2}}+1/{n_{3}}, Sci. China: Math. 55 (3), (2012), 465–474.
- [9] C. Jia, Mean value from representation of a rational number as sum of two Egyptina fractions, J. Number Theory 132 (2012), no. 4, 701–713.
- [10] E. J. Ionascu and A. Wilson, On the Erdös-Straus conjecture, Rev. Roumaine Math. Pures Appl. 56 (2011), no. 1, 21–30.
- [11] I. Kotsireas, The Erdös-Straus conjecture on Egyptian fractions, Paul Erdös and his mathematics (Budapest, 1999), 140–144, János Nolgai Math. Soc. Budapest, 1999.
- [12] D. Li, On the equation 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z, J. Number Theory 13 (1981), no. 4, 485–494.
- [13] S. Maiti, A study on Erdös-Straus conjecture on Diophantime equation 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}, arXiv: 2010.00975v1 [math.GM] 30 Dec 2020.
- [14] L. J. Mordell, Diophantime Equations, Academic Press, London/New York, 1969.
- [15] S. Prugsapitak, The Egyptian fraction of the form 1 a + 1 b = q − 1 p ​ q \frac{1}{a}+\frac{1}{b}=\frac{q-1}{pq}, Int. J. Math. Comput. Sci. 18 (2023), no. 4, 595–597.
- [16] L. Antonio Rosati, Sull’equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3}, Boll. Uni. Mat. Ital. (3) 9 (1954), 59–63.
- [17] J. W. Sander, On 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z and Rosser’s sieve, Acta Arith. 59 (1991), no. 2, 183–204.
- [18] J. W. Sander, On 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z and Iwanniec’s half-dimensional sieve, J. Number Theory 46 (1994), no. 2, 123–136.
- [19] J. W. Sander, Egyptian fractions and the Erdös-Straus conjecture, Nieuw Arch. Wisk (4) 15 (1997), no. 1-2, 43–50.
- [20] J. D. Serna, Partial proof without words: shapping some cases of the Erdös-Straus conjecture, College. Math. J. 40 (2015), no. 3, 181.
- [21] S. Subburam and A. Togb’e, A note on Erdös-Straus conjecture, Period Math. Hungar. 72 (2016), no. 1, 43–49.
- [22] D. G. Terzi, On a conjecture by Erdös and Straus, Nordisk Tidsk. Informationsbehindling (BIT) 11 (1971), 212–216.
- [23] R. C. Vaughan, On a problem of Erdös, Straus and Schinzel, Mathematika 17 (1970), 193–198.
- [24] W. A. Webb, On 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z, Proc. Amer. Math. Soc. 25 (1970), 578–584.
- [25] X. Xu, Congruence classes of supporting the Erdös-Straus conjecture II: tame solutions, in preparation.

E-Mail: X, Xu: xiaoping@math.ac.cn


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
