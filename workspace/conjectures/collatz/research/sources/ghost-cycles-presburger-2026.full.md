<!-- source: https://arxiv.org/html/2601.12772v1 | converted from HTML -->

2-Adic Obstructions to Presburger-Definable Characterizations of Collatz Cycles

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2601.12772v1 [math.NT] 19 Jan 2026

# 2-Adic Obstructions to Presburger-Definable
Characterizations of Collatz Cycles

Madhav Dhiman Thanks: Corresponding author: mmdhiman09@gmail.com Email: [mmdhiman09@gmail.com][3] Rohan Pandey Email: [rpande@uw.edu][3]

August 11, 2026

###### Abstract

I investigate structural limitations of Presburger-arithmetic–based approaches to the Collatz problem. I show that the Collatz cycle equation admits a unique solution in the 2 2 -adic integers, which I term a *ghost cycle*. These ghost cycles are shown to be genuine periodic orbits of the 2 2 -adic Collatz map, satisfying all local parity constraints.

I prove unconditionally that the divisibility predicate 𝒟 y = { ( x, C) ∈ ℕ 2: ( 2 x − 3 y) ∣ C } \mathcal{D}_{y}=\{(x,C)\in\mathbb{N}^{2}:(2^{x}-3^{y})\mid C\}, which acts as the algebraic necessary condition for integrality, is not semilinear for any fixed number of odd steps y ≥ 1 y\geq 1. This result is established by demonstrating that the fibers of 𝒟 y \mathcal{D}_{y} exhibit unbounded periods, an obstruction to Presburger definability. Consequently, strategies relying solely on Presburger arithmetic or finite automata to define the integrality constraint cannot capture the distinction between ghost cycles and genuine integer cycles. I conclude with a heuristic argument suggesting that because ghost cycles satisfy the algebraic cycle equation, the non-existence of integer cycles cannot be proven solely through algebraic manipulation of the cycle equation itself.

## 1 Introduction

The Collatz map T: ℕ → ℕ T:\mathbb{N}\to\mathbb{N} is defined by

 | T ⁡ ( n) = { n / 2, n ≡ 0 ( mod 2), 3 ​ n + 1, n ≡ 1 ( mod 2). T(n)=\begin{cases}n/2,&n\equiv 0\pmod{2},\\ 3n+1,&n\equiv 1\pmod{2}.\end{cases} |  |

The Collatz conjecture asserts that every positive integer eventually reaches 1 1 under iteration of T T. Despite its elementary definition, the conjecture remains one of the most intractable problems in mathematics. The difficulty lies in the pseudo-random mixing of modular constraints (parity) and magnitude constraints (inequalities) under iteration. [6, 11, 10].

### 1.1 Motivation

A wide class of approaches to the Collatz conjecture apply linear or automata-theoretic methods. These include:

- •

Parity-vector encodings,

- •

Modular constraints and residue class analysis,

- •

Finite automata representations of binary strings,

- •

Symbolic reasoning over linear integer arithmetic.

Such methods naturally fall within the expressive power of *Presburger Arithmetic*, the first-order theory of ( ℕ, +, <) (\mathbb{N},+,<) first introduced in 1929 [8]. This observation motivates the following question:

*To what extent can the existence or nonexistence of Collatz cycles be captured within Presburger arithmetic?*

Rather than addressing the Collatz Conjecture directly, I study the limitations of these methods. Specifically, I analyze whether the *integrality condition*—the constraint distinguishing genuine integer cycles from formal algebraic solutions—can be expressed using Presburger-definable sets.

Prior work by Lagarias [5] and Bernstein [2] established the relevance of 2 2 -adic integers to the problem, noting that solutions exist in the 2 2 -adic limit. My results demonstrate that the integrality constraints required to filter these 2 2 -adic solutions fail to be semilinear and therefore are not definable in Presburger arithmetic. Consequently, any approach that attempts to distinguish genuine integer cycles from 2 2 -adic ”ghost cycles” using only linear arithmetic, finite automata, or bounded congruence reasoning is inherently insufficient.

## 2 Background and Preliminaries

To make the logical obstructions precise, we review the relevant logical and algebraic structures.

### 2.1 Presburger Arithmetic and Semilinear Sets

Presburger Arithmetic is the first-order theory of the structure ( ℕ, +, <, 0, 1) (\mathbb{N},+,<,0,1). It allows for quantification over integers, addition, and order, but excludes multiplication between variables. This restriction makes the theory decidable, unlike full Peano arithmetic.

A fundamental result by Ginsburg and Spanier [4] characterizes the sets definable in this theory.

###### Theorem 2.1 (Ginsburg–Spanier Characterization).

A subset of ℕ d \mathbb{N}^{d} is definable by a Presburger arithmetic formula if and only if it is semilinear.

###### Definition 2.2 (Semilinear Sets).

A set L ⊆ ℕ d L\subseteq\mathbb{N}^{d} is *linear*if there exist a base vector b ∈ ℕ d b\in\mathbb{N}^{d} and a finite set of period vectors P = { v 1, …, v k } ⊂ ℕ d P=\{v_{1},\dots,v_{k}\}\subset\mathbb{N}^{d} such that

 | L = { b + ∑ i = 1 k λ i ​ v i: λ i ∈ ℕ }. L=\left\{b+\sum_{i=1}^{k}\lambda_{i}v_{i}:\lambda_{i}\in\mathbb{N}\right\}. |  |

A set is *semilinear*if it is a finite union of linear sets.

This theorem provides a geometric method to prove undecidability or undefinability: if a set’s projection or fiber structure implies it is not semilinear, it cannot be defined in Presburger arithmetic.

Below is a well-known lemma that is central to the arguments in this paper.

###### Lemma 2.3 (Unbounded Fiber Period Obstruction).

Let S ⊆ ℕ 2 S\subseteq\mathbb{N}^{2}. For x ∈ ℕ x\in\mathbb{N}, let S x = { y: ( x, y) ∈ S } S_{x}=\{y:(x,y)\in S\} be the fiber at x x. If there exists a constant M M such that for every x x, the fiber S x S_{x} is eventually periodic with minimal period p ⁡ ( x) p(x) dividing M M, then S S is semilinear. Conversely, if the set of minimal eventual periods { p ⁡ ( x): x ∈ ℕ } \{p(x):x\in\mathbb{N}\} is unbounded, then S S is not semilinear and not Presburger-definable.

###### Proof.

If S S is semilinear, it is a finite union of linear sets. The fiber of a linear set is an arithmetic progression (or finite union thereof) whose period is determined by the lattice vectors. Since there are finitely many linear components, the least common multiple of their periods provides a uniform bound M M for all fibers. If the actual minimal periods p ⁡ ( x) p(x) grow without bound as x → ∞ x\to\infty, this contradicts the existence of M M. ∎

### 2.2 The 2-adic Integers

The ring of 2 2 -adic integers, ℤ 2 \mathbb{Z}_{2}, is the completion of ℤ \mathbb{Z} with respect to the 2 2 -adic metric | x | 2 = 2 − v 2 ​ ( x) |x|_{2}=2^{-v_{2}(x)}. As detailed in Mahler [7], elements of ℤ 2 \mathbb{Z}_{2} can be represented as formal power series:

 | α = ∑ i = 0 ∞ a i ​ 2 i, a i ∈ { 0, 1 }. \alpha=\sum_{i=0}^{\infty}a_{i}2^{i},\quad a_{i}\in\{0,1\}. |  |

A key property relevant to our analysis is the unit structure of ℤ 2 \mathbb{Z}_{2}. An element x ∈ ℤ 2 x\in\mathbb{Z}_{2} is a unit (invertible) if and only if x ≡ 1 ( mod 2) x\equiv 1\pmod{2}. In contrast to ℤ \mathbb{Z}, where the only units are ± 1 \pm 1, ℤ 2 \mathbb{Z}_{2} contains infinitely many units, allowing for unique solutions to equations like 3 ​ x + 1 = 2 k ​ x 3x+1=2^{k}x that have no integer solutions.

## 3 Parity Patterns and Cycle Equations

We formalize the structure of a cycle by the sequence of operations performed.

###### Definition 3.1 (Cycle-Admissible Pattern).

A parity pattern is a tuple ( x, y, σ →) (x,y,\vec{\sigma}) characterizing a hypothetical cycle of length ℓ = x + y \ell=x+y, where:

1. 1.

y ≥ 1 y\geq 1 is the number of odd steps ( 3 ​ n + 1 3n+1).

2. 2.

x ≥ 1 x\geq 1 is the number of even steps ( n / 2 n/2).

3. 3.

σ → = ( σ 0, …, σ y − 1) \vec{\sigma}=(\sigma_{0},\ldots,\sigma_{y-1}) satisfies 0 = σ 0 < σ 1 < ⋯ < σ y − 1 < x 0=\sigma_{0}<\sigma_{1}<\cdots<\sigma_{y-1}<x, representing the cumulative number of divisions by 2 performed before each odd step.

For a non-trivial cycle to exist ( n 0 > 0 n_{0}>0), we require the logarithmic constraint 2 x > 3 y 2^{x}>3^{y}, or x > y ​ log 2 ​ 3 x>y\log_{2}3. Note that equality is impossible by the transcendence of log 2 ⁡ 3 \log_{2}3 (see Baker [1] or Gelfond [3]).

### 3.1 Derivation of the Cycle Equation

A cycle corresponds to a fixed point of the composed function. By tracing the affine operations n ↦ 3 ​ n + 1 n\mapsto 3n+1 and n ↦ n / 2 n\mapsto n/2, we derive the standard cycle equation [9].

###### Proposition 3.2.

A positive integer n 0 n_{0} generates a cycle with pattern ( x, y, σ →) (x,y,\vec{\sigma}) if and only if:

 | n 0 ​ ( 2 x − 3 y) = ∑ k = 0 y − 1 3 y − 1 − k ​ 2 σ k =: C ⁡ ( y, σ →). n_{0}(2^{x}-3^{y})=\sum_{k=0}^{y-1}3^{y-1-k}2^{\sigma_{k}}=:C(y,\vec{\sigma}). |  | (1) |

###### Proof.

Let m k m_{k} be the value of the integer at the k k -th odd step, with m 0 = n 0 m_{0}=n_{0}. The transition from m k m_{k} to m k + 1 m_{k+1} involves one multiplication by 3, adding 1, and dividing by 2 s k + 1 2^{s_{k+1}}, where s k + 1 = σ k + 1 − σ k s_{k+1}=\sigma_{k+1}-\sigma_{k}. Thus:

 | m k + 1 = 3 ​ m k + 1 2 s k + 1 ⟹ m k + 1 ​ 2 s k + 1 = 3 ​ m k + 1. m_{k+1}=\frac{3m_{k}+1}{2^{s_{k+1}}}\implies m_{k+1}2^{s_{k+1}}=3m_{k}+1. |  |

Multiplying both sides by 2 σ k 2^{\sigma_{k}} (noting that σ k + 1 = σ k + s k + 1 \sigma_{k+1}=\sigma_{k}+s_{k+1}), we get:

 | m k + 1 ​ 2 σ k + 1 = 3 ​ ( m k ​ 2 σ k) + 2 σ k. m_{k+1}2^{\sigma_{k+1}}=3(m_{k}2^{\sigma_{k}})+2^{\sigma_{k}}. |  |

Let A k = m k ​ 2 σ k A_{k}=m_{k}2^{\sigma_{k}}. The recurrence becomes A k + 1 = 3 ​ A k + 2 σ k A_{k+1}=3A_{k}+2^{\sigma_{k}}. We solve this linear recurrence by induction.

- •

Base Case ( k = 0 k=0): A 0 = m 0 ​ 2 0 = n 0 A_{0}=m_{0}2^{0}=n_{0}.

- •

Step 1: A 1 = 3 ​ n 0 + 2 σ 0 A_{1}=3n_{0}+2^{\sigma_{0}}.

- •

Step 2: A 2 = 3 ​ ( 3 ​ n 0 + 2 σ 0) + 2 σ 1 = 3 2 ​ n 0 + 3 1 ​ 2 σ 0 + 2 σ 1 A_{2}=3(3n_{0}+2^{\sigma_{0}})+2^{\sigma_{1}}=3^{2}n_{0}+3^{1}2^{\sigma_{0}}+2^{\sigma_{1}}.

By induction, after y y steps:

 | A y = 3 y ​ n 0 + ∑ k = 0 y − 1 3 y − 1 − k ​ 2 σ k. A_{y}=3^{y}n_{0}+\sum_{k=0}^{y-1}3^{y-1-k}2^{\sigma_{k}}. |  |

However, since this is a cycle, m y = m 0 = n 0 m_{y}=m_{0}=n_{0}. Since σ y = x \sigma_{y}=x (the total number of divisions), we have A y = n 0 ​ 2 x A_{y}=n_{0}2^{x}. Substituting this into the equation:

 | n 0 ​ 2 x = 3 y ​ n 0 + ∑ k = 0 y − 1 3 y − 1 − k ​ 2 σ k. n_{0}2^{x}=3^{y}n_{0}+\sum_{k=0}^{y-1}3^{y-1-k}2^{\sigma_{k}}. |  |

Rearranging terms yields the result. ∎

## 4 Ghost Cycles in ℤ 2 \mathbb{Z}_{2}

Equation ( 1) is a linear Diophantine equation in one variable n 0 n_{0}. Over ℤ \mathbb{Z}, solvability depends on divisibility. Over ℤ 2 \mathbb{Z}_{2}, the situation is simpler.

###### Theorem 4.1 (Existence of Ghost Cycles).

For every cycle-admissible pattern ( x, y, σ →) (x,y,\vec{\sigma}), there exists a unique solution n 0 ∈ ℤ 2 n_{0}\in\mathbb{Z}_{2} to Equation ( 1). We term this solution a *ghost cycle*.

###### Proof.

Consider the coefficient 2 x − 3 y 2^{x}-3^{y}. Since x ≥ 1 x\geq 1, we have 2 x ≡ 0 ( mod 2) 2^{x}\equiv 0\pmod{2}. Since y ≥ 1 y\geq 1, we have 3 y ≡ 1 ( mod 2) 3^{y}\equiv 1\pmod{2}. Therefore:

 | 2 x − 3 y ≡ 0 − 1 ≡ 1 ( mod 2). 2^{x}-3^{y}\equiv 0-1\equiv 1\pmod{2}. |  |

In the ring of 2 2 -adic integers, any number congruent to 1 modulo 2 is a unit (invertible). Thus, ( 2 x − 3 y) − 1 (2^{x}-3^{y})^{-1} exists and is unique. The solution is explicitly:

 | n 0 = ( 2 x − 3 y) − 1 ⋅ C ⁡ ( y, σ →). n_{0}=(2^{x}-3^{y})^{-1}\cdot C(y,\vec{\sigma}). |  |

∎

###### Definition 4.2 (Ghost Cycle).

A Ghost Cycle is the unique 2 2 -adic integer n 0 ∈ ℤ 2 n_{0}\in\mathbb{Z}_{2} satisfying the cycle equation for a specific parity pattern. It represents a ”virtual” cycle that exists algebraically but may not be an integer.

## 5 Integrality: The Global Constraint

A ghost cycle n 0 ∈ ℤ 2 n_{0}\in\mathbb{Z}_{2} is a genuine integer cycle if and only if n 0 ∈ ℕ n_{0}\in\mathbb{N}. This requires the infinite binary expansion of n 0 n_{0} to terminate.

###### Lemma 5.1.

An element α = ∑ i = 0 ∞ a i ​ 2 i ∈ ℤ 2 \alpha=\sum_{i=0}^{\infty}a_{i}2^{i}\in\mathbb{Z}_{2} lies in ℕ \mathbb{N} if and only if the sequence ( a i) (a_{i}) is eventually zero. It lies in ℤ \mathbb{Z} if and only if its binary expansion is eventually constant.

Since standard Collatz dynamics are restricted to positive integers, we are concerned with expansions that terminate. The condition n 0 ∈ ℕ n_{0}\in\mathbb{N} is equivalent to the divisibility condition in ℤ \mathbb{Z}:

 | ( 2 x − 3 y) | C ⁡ ( y, σ →). (2^{x}-3^{y})\mid C(y,\vec{\sigma}). |  |

This divisibility check separates ghost cycles from real cycles.

## 6 Verification of Ghost Cycle Dynamics

A potential objection to the relevance of ghost cycles is that they might be purely algebraic artifacts that violate the Collatz map. For instance, does the ghost cycle actually generate the correct sequence of odd and even numbers when we define the Collatz map over ℤ 2 \mathbb{Z}_{2}?

###### Definition 6.1 ( 2 2 -adic Collatz map).

Define T 2: ℤ 2 × → ℤ 2 T_{2}:\mathbb{Z}_{2}^{\times}\to\mathbb{Z}_{2} by:

 | T 2 ​ ( n) = { n / 2, v 2 ​ ( n) > 0, ( 3 ​ n + 1) / 2 v 2 ​ ( 3 ​ n + 1), v 2 ​ ( n) = 0, T_{2}(n)=\begin{cases}n/2,&v_{2}(n)>0,\\ (3n+1)/2^{v_{2}(3n+1)},&v_{2}(n)=0,\end{cases} |  |

where ℤ 2 × = ℤ 2 ∖ { 0 } \mathbb{Z}_{2}^{\times}=\mathbb{Z}_{2}\setminus\{0\}.

###### Remark 6.2.

The map T 2 T_{2} extends the classical Collatz map to ℤ 2 \mathbb{Z}_{2} by treating odd 2 2 -adic integers analogously to odd positive integers: we apply n ↦ 3 ​ n + 1 n\mapsto 3n+1 and then divide by the maximal power of 2 2 that divides the result. This is well-defined because for any unit u ∈ ℤ 2 × u\in\mathbb{Z}_{2}^{\times} (i.e., v 2 ​ ( u) = 0 v_{2}(u)=0), we have 3 ​ u + 1 ≡ 0 ( mod 2) 3u+1\equiv 0\pmod{2}, ensuring v 2 ​ ( 3 ​ u + 1) ≥ 1 v_{2}(3u+1)\geq 1.

To analyze ghost cycles as periodic points of T 2 T_{2}, we establish notation consistent with the cycle structure.

###### notation 1.

For a cycle-admissible pattern ( x, y, σ →) (x,y,\vec{\sigma}) with σ → = ( σ 0, σ 1, …, σ y − 1) \vec{\sigma}=(\sigma_{0},\sigma_{1},\ldots,\sigma_{y-1}), define σ y:= x \sigma_{y}:=x. Let s k:= σ k − σ k − 1 s_{k}:=\sigma_{k}-\sigma_{k-1} for k = 1, …, y k=1,\ldots,y denote the number of halvings between the ( k − 1) (k-1) -th and k k -th odd steps. By admissibility, s k ≥ 1 s_{k}\geq 1 for all k k.

###### Lemma 6.3 (Forced valuations).

Let n 0 = ( 2 x − 3 y) − 1 ​ C ​ ( y, σ →) n_{0}=(2^{x}-3^{y})^{-1}C(y,\vec{\sigma}) be the ghost cycle for an admissible pattern ( x, y, σ →) (x,y,\vec{\sigma}). Define the sequence of 2 2 -adic integers m 0, m 1, …, m y m_{0},m_{1},\ldots,m_{y} by m 0 = n 0 m_{0}=n_{0} and the recurrence relation

 | m k + 1 ⋅ 2 s k + 1 = 3 ​ m k + 1 m_{k+1}\cdot 2^{s_{k+1}}=3m_{k}+1 |  |

for k = 0, …, y − 1 k=0,\ldots,y-1, where s k + 1 = σ k + 1 − σ k s_{k+1}=\sigma_{k+1}-\sigma_{k}. Then:

1. 1.

v 2 ​ ( m k) = 0 v_{2}(m_{k})=0 for all k = 0, …, y k=0,\ldots,y (each m k m_{k} is a unit in ℤ 2 \mathbb{Z}_{2}).

2. 2.

v 2 ​ ( 3 ​ m k + 1) = s k + 1 v_{2}(3m_{k}+1)=s_{k+1} for all k = 0, …, y − 1 k=0,\ldots,y-1.

3. 3.

m y = m 0 = n 0 m_{y}=m_{0}=n_{0} (the sequence closes into a cycle).

###### Proof.

We first establish claim (3), then use it to prove claims (1) and (2).

Step 1: Proving m y = n 0 m_{y}=n_{0} (claim 3).

From Proposition 3.2, the quantity A j:= m j ⋅ 2 σ j A_{j}:=m_{j}\cdot 2^{\sigma_{j}} satisfies

 | A j = 3 j ​ n 0 + ∑ i = 0 j − 1 3 j − 1 − i ​ 2 σ i A_{j}=3^{j}n_{0}+\sum_{i=0}^{j-1}3^{j-1-i}2^{\sigma_{i}} |  | (2) |

for each j = 0, 1, …, y j=0,1,\ldots,y.

For j = y j=y, we have σ y = x \sigma_{y}=x by Notation 1, so:

 | A y = m y ⋅ 2 x \displaystyle A_{y}=m_{y}\cdot 2^{x} | = 3 y ​ n 0 + ∑ i = 0 y − 1 3 y − 1 − i ​ 2 σ i \displaystyle=3^{y}n_{0}+\sum_{i=0}^{y-1}3^{y-1-i}2^{\sigma_{i}} |  |

 |  | = 3 y ​ n 0 + C ⁡ ( y, σ →). \displaystyle=3^{y}n_{0}+C(y,\vec{\sigma}). |  |

By the cycle equation n 0 ​ ( 2 x − 3 y) = C ⁡ ( y, σ →) n_{0}(2^{x}-3^{y})=C(y,\vec{\sigma}), we have C ⁡ ( y, σ →) = n 0 ⋅ 2 x − 3 y ⋅ n 0 C(y,\vec{\sigma})=n_{0}\cdot 2^{x}-3^{y}\cdot n_{0}. Substituting:

 | m y ⋅ 2 x = 3 y ​ n 0 + ( n 0 ⋅ 2 x − 3 y ⋅ n 0) = n 0 ⋅ 2 x. m_{y}\cdot 2^{x}=3^{y}n_{0}+(n_{0}\cdot 2^{x}-3^{y}\cdot n_{0})=n_{0}\cdot 2^{x}. |  |

Since 2 x 2^{x} is non-zero in ℤ 2 \mathbb{Z}_{2}, we conclude m y = n 0 m_{y}=n_{0}.

Step 2: Proving v 2 ​ ( m 0) = 0 v_{2}(m_{0})=0 (base case for claim 1).

We have m 0 = n 0 = ( 2 x − 3 y) − 1 ​ C ​ ( y, σ →) m_{0}=n_{0}=(2^{x}-3^{y})^{-1}C(y,\vec{\sigma}). Since 2 x ≡ 0 ( mod 2) 2^{x}\equiv 0\pmod{2} and 3 y ≡ 1 ( mod 2) 3^{y}\equiv 1\pmod{2}, we have 2 x − 3 y ≡ − 1 ≡ 1 ( mod 2) 2^{x}-3^{y}\equiv-1\equiv 1\pmod{2}, so 2 x − 3 y 2^{x}-3^{y} is a unit in ℤ 2 \mathbb{Z}_{2}.

The cycle constant is

 | C ⁡ ( y, σ →) = ∑ j = 0 y − 1 3 y − 1 − j ​ 2 σ j = 3 y − 1 ⋅ 2 σ 0 + ∑ j = 1 y − 1 3 y − 1 − j ​ 2 σ j. C(y,\vec{\sigma})=\sum_{j=0}^{y-1}3^{y-1-j}2^{\sigma_{j}}=3^{y-1}\cdot 2^{\sigma_{0}}+\sum_{j=1}^{y-1}3^{y-1-j}2^{\sigma_{j}}. |  |

Since σ 0 = 0 \sigma_{0}=0, the first term is 3 y − 1 3^{y-1}, which is odd. For j ≥ 1 j\geq 1, admissibility gives σ j ≥ 1 \sigma_{j}\geq 1, so each term 3 y − 1 − j ​ 2 σ j 3^{y-1-j}2^{\sigma_{j}} is even. Therefore, C ⁡ ( y, σ →) ≡ 1 ( mod 2) C(y,\vec{\sigma})\equiv 1\pmod{2}, making it a unit.

Thus n 0 n_{0} is the product of two units, so v 2 ​ ( m 0) = 0 v_{2}(m_{0})=0.

Step 3: Proving v 2 ​ ( m k) = 0 v_{2}(m_{k})=0 for all k k and v 2 ​ ( 3 ​ m k + 1) = s k + 1 v_{2}(3m_{k}+1)=s_{k+1} (claims 1 and 2).

We proceed by induction on k k for k = 0, 1, …, y k=0,1,\ldots,y.

*Base case*( k = 0 k=0): Already established v 2 ​ ( m 0) = 0 v_{2}(m_{0})=0 in Step 2.

*Inductive step*: Assume v 2 ​ ( m j) = 0 v_{2}(m_{j})=0 for all j ≤ k j\leq k where k ∈ { 0, …, y − 1 } k\in\{0,\ldots,y-1\}. We prove v 2 ​ ( 3 ​ m k + 1) = s k + 1 v_{2}(3m_{k}+1)=s_{k+1} and v 2 ​ ( m k + 1) = 0 v_{2}(m_{k+1})=0.

From the recurrence m k + 1 ⋅ 2 s k + 1 = 3 ​ m k + 1 m_{k+1}\cdot 2^{s_{k+1}}=3m_{k}+1, taking valuations:

 | v 2 ​ ( m k + 1) + s k + 1 = v 2 ​ ( 3 ​ m k + 1). v_{2}(m_{k+1})+s_{k+1}=v_{2}(3m_{k}+1). |  | (3) |

Since m k m_{k} is a unit, 3 ​ m k 3m_{k} is also a unit, so 3 ​ m k + 1 ≡ 0 ( mod 2) 3m_{k}+1\equiv 0\pmod{2}. Thus v 2 ​ ( 3 ​ m k + 1) ≥ 1 v_{2}(3m_{k}+1)\geq 1.

Now, using equation ( 2) for j = k + 1 j=k+1:

 | A k + 1 = m k + 1 ⋅ 2 σ k + 1 = 3 k + 1 ​ n 0 + ∑ i = 0 k 3 k − i ​ 2 σ i. A_{k+1}=m_{k+1}\cdot 2^{\sigma_{k+1}}=3^{k+1}n_{0}+\sum_{i=0}^{k}3^{k-i}2^{\sigma_{i}}. |  |

From the recurrence, we also have:

 | A k + 1 = m k + 1 ⋅ 2 σ k + 1 = m k + 1 ⋅ 2 σ k + s k + 1 = 2 σ k ​ ( 3 ​ m k + 1). A_{k+1}=m_{k+1}\cdot 2^{\sigma_{k+1}}=m_{k+1}\cdot 2^{\sigma_{k}+s_{k+1}}=2^{\sigma_{k}}(3m_{k}+1). |  |

Therefore:

 | 3 k + 1 ​ n 0 + ∑ i = 0 k 3 k − i ​ 2 σ i = 2 σ k ​ ( 3 ​ m k + 1). 3^{k+1}n_{0}+\sum_{i=0}^{k}3^{k-i}2^{\sigma_{i}}=2^{\sigma_{k}}(3m_{k}+1). |  | (4) |

Taking valuations of both sides:

 | v 2 ​ ( 3 k + 1 ​ n 0 + ∑ i = 0 k 3 k − i ​ 2 σ i) = v 2 ​ ( 2 σ k ​ ( 3 ​ m k + 1)) = σ k + v 2 ​ ( 3 ​ m k + 1). v_{2}\left(3^{k+1}n_{0}+\sum_{i=0}^{k}3^{k-i}2^{\sigma_{i}}\right)=v_{2}(2^{\sigma_{k}}(3m_{k}+1))=\sigma_{k}+v_{2}(3m_{k}+1). |  |

To compute the left side, write:

 | ∑ i = 0 k 3 k − i ​ 2 σ i = 3 k + ∑ i = 1 k 3 k − i ​ 2 σ i. \sum_{i=0}^{k}3^{k-i}2^{\sigma_{i}}=3^{k}+\sum_{i=1}^{k}3^{k-i}2^{\sigma_{i}}. |  |

Since n 0 n_{0} is a unit, the term 3 k + 1 ​ n 0 + 3 k = 3 k ​ ( 3 ​ n 0 + 1) 3^{k+1}n_{0}+3^{k}=3^{k}(3n_{0}+1) has v 2 ​ ( 3 k ​ ( 3 ​ n 0 + 1)) = v 2 ​ ( 3 ​ n 0 + 1) ≥ 1 v_{2}(3^{k}(3n_{0}+1))=v_{2}(3n_{0}+1)\geq 1.

For i ≥ 1 i\geq 1, we have σ i ≥ σ 1 ≥ 1 \sigma_{i}\geq\sigma_{1}\geq 1, so v 2 ​ ( 3 k − i ​ 2 σ i) = σ i ≥ 1 v_{2}(3^{k-i}2^{\sigma_{i}})=\sigma_{i}\geq 1.

Thus, all terms in 3 k + 1 ​ n 0 + ∑ i = 0 k 3 k − i ​ 2 σ i 3^{k+1}n_{0}+\sum_{i=0}^{k}3^{k-i}2^{\sigma_{i}} have valuation at least 1 1. The minimum valuation determines v 2 v_{2} of the sum.

By the structure of equation ( 4) and the fact that this must hold in ℤ 2 \mathbb{Z}_{2}, combined with our knowledge that m y = n 0 m_{y}=n_{0} (from Step 1), we can deduce the exact valuation by a counting argument.

Specifically, summing equation ( 3) over all k = 0, …, y − 1 k=0,\ldots,y-1:

 | ∑ k = 0 y − 1 v 2 ​ ( m k + 1) + ∑ k = 0 y − 1 s k + 1 = ∑ k = 0 y − 1 v 2 ​ ( 3 ​ m k + 1). \sum_{k=0}^{y-1}v_{2}(m_{k+1})+\sum_{k=0}^{y-1}s_{k+1}=\sum_{k=0}^{y-1}v_{2}(3m_{k}+1). |  |

The left side becomes:

 | ∑ k = 1 y v 2 ​ ( m k) + ∑ k = 1 y s k = ∑ k = 1 y v 2 ​ ( m k) + x, \sum_{k=1}^{y}v_{2}(m_{k})+\sum_{k=1}^{y}s_{k}=\sum_{k=1}^{y}v_{2}(m_{k})+x, |  |

where we used ∑ k = 1 y s k = ∑ k = 1 y ( σ k − σ k − 1) = σ y − σ 0 = x \sum_{k=1}^{y}s_{k}=\sum_{k=1}^{y}(\sigma_{k}-\sigma_{k-1})=\sigma_{y}-\sigma_{0}=x.

Since m y = n 0 = m 0 m_{y}=n_{0}=m_{0} and we’re assuming v 2 ​ ( m j) = 0 v_{2}(m_{j})=0 for j ≤ k j\leq k by induction, and we need to show this holds for all j ≤ y j\leq y, we observe that the only consistent solution to the recurrence system with the boundary condition m y = m 0 m_{y}=m_{0} is that v 2 ​ ( m k) = 0 v_{2}(m_{k})=0 for all k k.

To see this rigorously: suppose v 2 ​ ( m ℓ) > 0 v_{2}(m_{\ell})>0 for some ℓ ∈ { 1, …, y } \ell\in\{1,\ldots,y\}. Then from ( 3):

 | v 2 ​ ( 3 ​ m ℓ − 1 + 1) = v 2 ​ ( m ℓ) + s ℓ > s ℓ. v_{2}(3m_{\ell-1}+1)=v_{2}(m_{\ell})+s_{\ell}>s_{\ell}. |  |

Summing v 2 ​ ( 3 ​ m k + 1) v_{2}(3m_{k}+1) over all k k would then give:

 | ∑ k = 0 y − 1 v 2 ​ ( 3 ​ m k + 1) > ∑ k = 0 y − 1 s k + 1 = x. \sum_{k=0}^{y-1}v_{2}(3m_{k}+1)>\sum_{k=0}^{y-1}s_{k+1}=x. |  |

But from ( 4), the total halving in one complete cycle must equal exactly x x (since A y = A 0 ⋅ 2 x / 2 0 = n 0 ⋅ 2 x A_{y}=A_{0}\cdot 2^{x}/2^{0}=n_{0}\cdot 2^{x}). This contradiction shows v 2 ​ ( m k) = 0 v_{2}(m_{k})=0 for all k k.

From ( 3), we then obtain v 2 ​ ( 3 ​ m k + 1) = s k + 1 v_{2}(3m_{k}+1)=s_{k+1} for each k = 0, …, y − 1 k=0,\ldots,y-1. ∎

###### Remark 6.4.

The key insight in Lemma 6.3 is that the cycle equation imposes a global constraint: the total number of halvings around the cycle must equal x x. Combined with the uniqueness of the 2 2 -adic solution and the recurrence structure, this forces the local valuations at each step to match the prescribed pattern. This is a non-trivial consistency condition that is satisfied for ghost cycles.

###### Theorem 6.5 (Ghost cycles satisfy iteration dynamics).

Let n 0 ∈ ℤ 2 n_{0}\in\mathbb{Z}_{2} be a ghost cycle for pattern ( x, y, σ →) (x,y,\vec{\sigma}). Then n 0 n_{0} is a periodic point of T 2 T_{2} with minimal period dividing ℓ = x + y \ell=x+y, following the parity pattern encoded by ( x, y, σ →) (x,y,\vec{\sigma}).

###### Proof.

Let m 0, m 1, …, m y m_{0},m_{1},\ldots,m_{y} be the sequence from Lemma 6.3. By that lemma, v 2 ​ ( m k) = 0 v_{2}(m_{k})=0 for all k k, so each m k m_{k} is a unit, and v 2 ​ ( 3 ​ m k + 1) = s k + 1 v_{2}(3m_{k}+1)=s_{k+1}.

Starting from n 0 = m 0 n_{0}=m_{0}, we apply T 2 T_{2} iteratively. Since v 2 ​ ( m 0) = 0 v_{2}(m_{0})=0, the map T 2 T_{2} acts as

 | T 2 ​ ( m 0) = 3 ​ m 0 + 1 2 v 2 ​ ( 3 ​ m 0 + 1) = 3 ​ m 0 + 1 2 s 1. T_{2}(m_{0})=\frac{3m_{0}+1}{2^{v_{2}(3m_{0}+1)}}=\frac{3m_{0}+1}{2^{s_{1}}}. |  |

From the recurrence m 1 ⋅ 2 s 1 = 3 ​ m 0 + 1 m_{1}\cdot 2^{s_{1}}=3m_{0}+1, we have T 2 ​ ( m 0) = m 1 T_{2}(m_{0})=m_{1}.

Between steps k k and k + 1 k+1, the value m k m_{k} is odd (a unit), so T 2 T_{2} maps it to ( 3 ​ m k + 1) / 2 v 2 ​ ( 3 ​ m k + 1) = ( 3 ​ m k + 1) / 2 s k + 1 = m k + 1 (3m_{k}+1)/2^{v_{2}(3m_{k}+1)}=(3m_{k}+1)/2^{s_{k+1}}=m_{k+1}. This transformation involves exactly s k + 1 s_{k+1} halvings.

After y y such operations, we reach m y = m 0 = n 0 m_{y}=m_{0}=n_{0} by Lemma 6.3 (3). The total number of steps is

 | y + ∑ k = 0 y − 1 s k + 1 = y + x = ℓ. y+\sum_{k=0}^{y-1}s_{k+1}=y+x=\ell. |  |

Here, y y counts the number of times we apply the n ↦ 3 ​ n + 1 n\mapsto 3n+1 operation (once per odd step), and ∑ s k + 1 = x \sum s_{k+1}=x counts the total number of halvings.

Therefore, T 2 ( ℓ) ​ ( n 0) = n 0 T_{2}^{(\ell)}(n_{0})=n_{0}, showing n 0 n_{0} is a periodic point with period dividing ℓ \ell. ∎

###### Corollary 6.6.

Ghost cycles are genuine periodic orbits of the 2 2 -adic dynamical system ( ℤ 2 ×, T 2) (\mathbb{Z}_{2}^{\times},T_{2}), not merely algebraic solutions to the cycle equation.

###### Proof.

Theorem 6.5 establishes that every ghost cycle n 0 n_{0} satisfies T 2 ( ℓ) ​ ( n 0) = n 0 T_{2}^{(\ell)}(n_{0})=n_{0} for ℓ = x + y \ell=x+y, where the iteration follows the prescribed parity pattern with the correct number of halvings at each step. This confirms that ghost cycles are dynamically realized periodic points under repeated application of T 2 T_{2}. ∎

###### Remark 6.7.

The verification that ghost cycles are genuine periodic orbits addresses a potential gap in purely algebraic treatments of the Collatz problem. It is conceivable that a formal 2 2 -adic solution to the cycle equation might fail to respect the discrete iteration structure of the Collatz map. Theorem 6.5 shows this does not occur: the algebraic and dynamical perspectives coincide for ghost cycles in ℤ 2 \mathbb{Z}_{2}.

## 7 Non-Semilinearity of the Integrality Condition

We now present the main logical obstruction. The integrality condition for a ghost cycle is the requirement that the cycle constant C ⁡ ( y, σ →) C(y,\vec{\sigma}) is divisible by 2 x − 3 y 2^{x}-3^{y}. We analyze the definability of this divisibility relation itself.

###### Definition 7.1 (General Divisibility Core).

Fix y ≥ 1 y\geq 1. Define the set of pairs ( x, C) (x,C) satisfying the divisibility condition:

 | 𝒟 y:= { ( x, C) ∈ ℕ 2: x > y log 2 3, C ≥ 1, ( 2 x − 3 y) ∣ C }. \mathcal{D}_{y}:=\{(x,C)\in\mathbb{N}^{2}:x>y\log_{2}3,\ C\geq 1,\ (2^{x}-3^{y})\mid C\}. |  |

###### Theorem 7.2 (Unconditional Non-Semilinearity).

For any fixed y ≥ 1 y\geq 1, the set 𝒟 y \mathcal{D}_{y} is not semilinear.

###### Proof.

Consider the fiber ( 𝒟 y) x (\mathcal{D}_{y})_{x} for a fixed x > y ​ log 2 ​ 3 x>y\log_{2}3.

 | ( 𝒟 y) x = { C ≥ 1: ( 2 x − 3 y) ∣ C } = { k ( 2 x − 3 y): k ∈ ℤ > 0 }. (\mathcal{D}_{y})_{x}=\{C\geq 1:(2^{x}-3^{y})\mid C\}=\{k(2^{x}-3^{y}):k\in\mathbb{Z}_{>0}\}. |  |

This is an arithmetic progression with initial term and common difference equal to f ⁡ ( x) = 2 x − 3 y f(x)=2^{x}-3^{y}. The minimal period of this fiber is exactly f ⁡ ( x) f(x).

As x → ∞ x\to\infty, the value f ⁡ ( x) = 2 x − 3 y f(x)=2^{x}-3^{y} grows exponentially.

Thus, the set of minimal periods { 2 x − 3 y: x > y ​ log 2 ​ 3 } \{2^{x}-3^{y}:x>y\log_{2}3\} is unbounded. By Lemma 2.3, 𝒟 y \mathcal{D}_{y} cannot be semilinear. ∎

###### Corollary 7.3.

The logical predicate P ⁡ ( x, C) ≡ [( 2 x − 3 y) ∣ C] P(x,C)\equiv[(2^{x}-3^{y})\mid C] is not definable in Presburger arithmetic. Since detecting whether a ghost cycle is an integer requires evaluating this predicate, the integrality question lies strictly outside the scope of Presburger arithmetic.

## 8 Heuristic Implications on Provability

We now consider a thought experiment regarding the sufficiency of the cycle equation and its implications for the provability of the Collatz conjecture.

###### Heuristic Argument 1 (The Sufficiency of the Cycle Equation).

Suppose that the cycle equation ( 1) encapsulates *all*arithmetic constraints on a Collatz cycle. That is, assume that any property derived about a cycle (bounds, distribution, etc.) is effectively a derivation on the variables within this equation.

If this hypothesis holds, we face a significant barrier to proving the non-existence of cycles. A common method of proof in number theory is *proof by contradiction*: assume a cycle exists, derive a set of properties from its definition, and show that two of these properties contradict each other (e.g., n n must be both even and odd, or n < n n<n).

However, we have established in Theorem 4.1 that for every admissible pattern, a ”Ghost Cycle” exists in ℤ 2 \mathbb{Z}_{2}. This ghost cycle is a concrete realization of the cycle parameters. It satisfies the cycle equation exactly.

Because a solution exists in the completion ℤ 2 \mathbb{Z}_{2}, the system of equations describing the cycle is **locally consistent**. It does not lead to an algebraic contradiction like 1 = 0 1=0. If the cycle equation is the only source of constraints, and those constraints are satisfied by the ghost cycle, then no contradiction can be derived from the equation itself without invoking an external property.

The only property that the ghost cycle fails to satisfy is **Integrality** (being in ℤ \mathbb{Z} rather than ℤ 2 ∖ ℤ \mathbb{Z}_{2}\setminus\mathbb{Z}). But as we proved in Theorem 7.2, the condition for Integrality is not definable in the linear logic (Presburger arithmetic) usually used to manipulate these equations.

Conclusion of the Heuristic: If a contradiction exists, it cannot be found by manipulating the algebraic cycle equation within standard arithmetic logic. The contradiction must arise from the ”Integrality Gap”—the analytic distance between the 2 2 -adic ghost cycle and the integers—which is a property of analytic number theory, not algebraic logic. This suggests that ”pure” algebraic approaches to the Collatz conjecture are likely formally unprovable.

## 9 Conclusion

I have established a rigorous framework for understanding the limitations of linear methods in the Collatz conjecture. By formalizing the concept of ghost cycles in ℤ 2 \mathbb{Z}_{2}, I demonstrated that algebraic solutions to the cycle equation always exist and are dynamically valid.

However, the condition required to collapse these spectral solutions into integer solutions exhibits unbounded periodicity. This proves that the integrality constraint is not semilinear, and thus, the Collatz problem lies strictly outside the decidable fragment of arithmetic provided by Presburger theory.

Furthermore, the existence of ghost cycles implies that the cycle equation is logically consistent. Therefore, non-existence proofs for Collatz cycles cannot rely on algebraic contradictions alone; they must exploit the specific analytic obstructions of mapping 2 2 -adic solutions to the integers.

## References

- [1] A. Baker (1975) Transcendental number theory. Cambridge University Press, Cambridge. Cited by: Definition 3.1.
- [2] D. J. Bernstein (1994) A non-iterative 2-adic statement of the 3 ​ n + 1 3n+1 conjecture. Proceedings of the American Mathematical Society 121 ( 2), pp. 405–408. Cited by: §1.1.
- [3] A. O. Gelfond (1960) Transcendental and algebraic numbers. Dover Publications. Cited by: Definition 3.1.
- [4] S. Ginsburg and E. Spanier (1966) Semigroups, Presburger formulas, and languages. Pacific Journal of Mathematics 16 ( 2), pp. 285–296. Cited by: §2.1.
- [5] J. C. Lagarias (1985) The 3 ​ x + 1 3x+1 problem and its generalizations. The American Mathematical Monthly 92 ( 1), pp. 3–23. Cited by: §1.1.
- [6] J. C. Lagarias (2011) The 3 ​ x + 1 3x+1 problem: an annotated bibliography, II (2000–2009). External Links: math/0608208v6 Cited by: §1.
- [7] K. Mahler (1981) p p -Adic numbers and their functions. Cambridge Tracts in Mathematics, Vol. 76, Cambridge University Press. Cited by: §2.2.
- [8] M. Presburger (1929) Über die vollständigkeit eines gewissen systems der arithmetik ganzer zahlen. Comptes Rendus du I congrès de Mathématiciens des Pays Slaves, pp. 92–101. Cited by: §1.1.
- [9] J. Simons and B. de Weger (2005) Theoretical and computational bounds for m m -cycles of the 3 ​ n + 1 3n+1 problem. Acta Arithmetica 117, pp. 51–70. Cited by: §3.1.
- [10] T. Tao (2022) Almost all Collatz orbits attain almost bounded values. Forum of Mathematics, Pi 10, pp. e12. Cited by: §1.
- [11] G. J. Wirsching (1998) The dynamical system generated by the 3 ​ n + 1 3n+1 function. Lecture Notes in Mathematics, Vol. 1681, Springer-Verlag, Berlin, Heidelberg. Cited by: §1.

## Appendix A Open Questions and Future Directions

The results of this paper suggest several avenues for further research, specifically regarding the structure of the set of ghost cycles.

### A.1 Topological Density of Ghost Cycles

An immediate question concerns the distribution of ghost cycles within the ring ℤ 2 \mathbb{Z}_{2}. Is the set of all ghost cycles (for all valid parity patterns) dense in ℤ 2 \mathbb{Z}_{2}? If ghost cycles can approximate any 2-adic integer arbitrarily well, it would suggest that the ”algebraic structure” of Collatz cycles is ubiquitous, making the exclusion of integers a purely statistical or analytic phenomenon rather than an algebraic one.

### A.2 Effective Certificates of Non-Integrality

While we showed that the general integrality predicate is not semilinear, specific instances might be effectively decidable. Is there a computationally efficient algorithm (faster than computing the full cycle constant) that can certify a ghost cycle is *not*an integer by examining only the initial segment of the parity vector? Such a certificate would be valuable for computational searchers.

## Appendix B Extensions to 3 ​ n + d 3n+d

The methods used here likely apply to generalized Collatz maps of the form q ​ n + d qn+d. Do ghost cycles for the 5 ​ n + 1 5n+1 problem (which is known to have cycles) exhibit different structural properties in ℤ 2 \mathbb{Z}_{2} compared to the 3 ​ n + 1 3n+1 problem? Comparing the 2-adic properties of a system with known cycles against one without could illuminate the specific defect that hinders 3 ​ n + 1 3n+1 cycles.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
