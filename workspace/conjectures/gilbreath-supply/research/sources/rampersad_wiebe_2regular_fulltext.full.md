<!-- source: https://arxiv.org/html/2309.04012v1 | converted from HTML -->

Sums of products of binomial coefficients mod 2 and 2 -regular sequences

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2309.04012v1 [math.NT] 07 Sep 2023

# Sums of products of binomial coefficients mod 2 2 and 2 2 -regular sequences

Narad Rampersad Max Wiebe Note: Department of Math/Stats, University of Winnipeg, 515 Portage Ave., Winnipeg, MB, R3B 2E9 Canada; narad.rampersad@gmail.com.

###### Abstract

Wu showed that certain sums of products of binomial coefficients modulo 2 2 are given by the run length transforms of several famous linear recurrence sequences, such as the positive integers, the Fibonacci numbers, the extended Lucas numbers, and Narayana’s cows sequence. In this paper we show that the run length transform of such sequences are 2 2 -regular sequences. This allows us to obtain Wu’s results and some new ones using the computer program Walnut, eliminating the need for long technical proofs.

## 1 Introduction

Wu [6] recently studied sums of the form

 | T ⁡ ( n) = ∑ k = 0 n [( a 1 ​ n + a 2 ​ k a 3 ​ n + a 4 ​ k) ​ ( n k) ( mod 2)], T(n)=\sum^{n}_{k=0}\left[\dbinom{a_{1}n+a_{2}k}{a_{3}n+a_{4}k}\dbinom{n}{k}\pmod{2}\right], |  | (1.1) |

where a 1 + a 2 ≥ 0 a_{1}+a_{2}\geq 0 and a 3 + a 4 ≥ 0 a_{3}+a_{4}\geq 0. He showed that for certain values of a 1, a 2, a 3, a 4 a_{1},a_{2},a_{3},a_{4}, the sequence defined by ( 1.1) can be obtained as the run length transform of a famous linear recurrence sequence, such as the positive integers, the Fibonacci numbers, the extended Lucas numbers, or Narayana’s cows sequence.

The run length transform is a operation on integer sequences first introduced by Sloane [5].

###### Definition 1.

The *run length transform sequence*( T ⁡ ( n)) n ≥ 0 (T(n))_{n\geq 0} of a sequence ( S ⁡ ( n)) n ≥ 0 (S(n))_{n\geq 0} is given by:

 | T ⁡ ( n) = ∑ i ∈ ℒ ⁡ ( n) S ⁡ ( i) T(n)=\sum_{i\in\mathcal{L}(n)}S(i) |  | (1.2) |

where ℒ ⁡ ( n) \mathcal{L}(n) is the list of the lengths of all maximal runs of 1 1 ’s (with repetitions) in [n] 2 [n]_{2}, the binary representation of n n.

For example, if n = 11 n=11, then [n] 2 = 1011 [n]_{2}=1011. So ℒ ⁡ ( 11) \mathcal{L}(11) = { 1, 2 } \{1,2\} and T ⁡ ( 11) = S ⁡ ( 1) ​ S ​ ( 2) T(11)=S(1)S(2).

Although they did not not state it this way, Sloane [5] and Wu [6] showed that if ( S ⁡ ( n)) n ≥ 0 (S(n))_{n\geq 0} is a linear recurrence sequence, then its run length transform ( T ⁡ ( n)) n ≥ 0 (T(n))_{n\geq 0} is a 2 2 -regular sequence. This is a class of sequences with a deep theory (see [1]). Furthermore, the computer package Walnut can be used to perform various computations involving these sequences. Our goal is to show how to use Walnut to obtain the results of Wu, as well as some new ones.

## 2 2 2 -regular sequences and Walnut

Next we define the class of 2 2 -regular sequences. We will give two equivalent definitions. The first is the one used (implicitly) by Wu [6] and the second is the one we will use in the rest of this paper.

Let ( a ⁡ ( n)) n ≥ 0 (a(n))_{n\geq 0} be an integer sequence. We define the *2 2 -kernel*of a a to be the following set of subsequences:

 | 𝒦 2 ( a) = { ( a ( 2 i n + j)) n ≥ 0: i ≥ 0; 0 ≤ j < 2 i }. \mathcal{K}_{2}(a)=\{(a(2^{i}n+j))_{n\geq 0}\;:\;i\geq 0;\;0\leq j<2^{i}\}. |  |

If there is a finite subset R ⊆ 𝒦 k ​ ( a) R\subseteq\mathcal{K}_{k}(a) such that every sequence in 𝒦 k ​ ( a) \mathcal{K}_{k}(a) can be written as a linear combination over ℤ \mathbb{Z} of sequences in R R, then a a is a *2 2 -regular sequence*.

For explicit calculation, the following equivalent definition may be more useful. Consider a triple ( v, γ, w) (v,\gamma,w), where

- •

v ∈ ℤ d v\in\mathbb{Z}^{d} is a row vector;

- •

w ∈ ℤ d w\in\mathbb{Z}^{d} is a column vector; and,

- •

γ: { 0, 1 } ∗ → ℤ d × d \gamma:\{0,1\}^{*}\to\mathbb{Z}^{d\times d}, is a homomorphism from the set of binary words to the set of d × d d\times d integer matrices (that is, if w = w m w m − 1 ⋯ w 1 w=w_{m}w_{m-1}\cdots w_{1} is a binary word, then γ ( w) = γ ( w m) γ ( w m − 1) ⋯ γ ( w 1) \gamma(w)=\gamma(w_{m})\gamma(w_{m-1})\cdots\gamma(w_{1})).

Note that γ \gamma is uniquely determined by the two matrices γ ⁡ ( 0) \gamma(0) and γ ⁡ ( 1) \gamma(1), so from now on, we will instead write ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w) rather than ( v, γ, w) (v,\gamma,w). The quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w) is a *linear representation*for a a if, for all n ≥ 0 n\geq 0, we have a ⁡ ( n) = v ​ γ ​ ( [n] 2) ​ w a(n)=v\gamma([n]_{2})w, where [n] 2 [n]_{2} is the binary representation of n n. The quantity d d is the *rank*of the linear representation. If a a has a linear representation, then a a is a *2 2 -regular sequence*. The equivalence between this definition and the previous one can be found in [1, Theorem 16.1.3].

Any sum of the form ( 1.1) defines a 2 2 -regular sequence and we can obtain a linear representation for it using the computer package Walnut. The key idea behind this comes from the classical theorem of Lucas: for integers k k, n n, and prime p p, the following holds:

 | ( n k) ≡ ∏ i = 1 m ( n i k i) ( mod p) \dbinom{n}{k}\equiv\prod_{i=1}^{m}\dbinom{n_{i}}{k_{i}}\pmod{p} |  | (2.1) |

where [n] p = n m n m − 1 ⋯ n 1 [n]_{p}=n_{m}n_{m-1}\cdots n_{1} and [k] p = k m k m − 1 ⋯ k 1 [k]_{p}=k_{m}k_{m-1}\cdots k_{1} are the base- p p expansions of n n and k k respectively (if necessary, the shorter of the two base- p p expansions is padded with 0 0 ’s on the left so that both expansions have the same length). Furthermore, we use the convention that ( n k) = 0 \dbinom{n}{k}=0 if n < k n<k.

In this paper we will only consider p = 2 p=2. Note that in this case we have

 | ( n i k i) ≡ { 0 ( mod 2) if n i = 0, k i = 1, 1 ( mod 2) o ​ t ​ h ​ e ​ r ​ w ​ i ​ s ​ e. \dbinom{n_{i}}{k_{i}}\equiv\begin{cases}0\pmod{2}&\text{if }n_{i}=0,\;k_{i}=1,\\ 1\pmod{2}&otherwise.\end{cases} |  | (2.2) |

It follows that ( n k) ( mod 2) ≡ 0 ( mod 2) \dbinom{n}{k}\pmod{2}\equiv 0\pmod{2} if and only if there exists i i such that [k i, n i] = [1, 0] [k_{i},n_{i}]=[1,0]. This condition can be checked by the finite automaton given in Figure 1.

Figure 1: Automaton for ( n k) \dbinom{n}{k} modulo 2 2

This automaton reads pairs of digits [k i, n i] [k_{i},n_{i}] and remains in state 1 1 if no [1, 0] [1,0] is seen; otherwise, the automaton transitions to state 0 0 and stays there once a [1, 0] [1,0] is read.

Given such an automaton, the program Walnut can prove many things about the sequence computed by the automaton, and, what is important for our purposes, it can compute linear representations for sequences of the form ( 1.1) (see the book by Shallit [4] and in particular Chapter 9 for details on how to use this program). The Walnut command we use to compute linear representations for ( 1.1) is

```

eval [Sequence Name] n "?msd_2 (k <= n) &
    BINOM2[a_1*n+a_2*k][a_3*n+a_4*k]=@1 &
    BINOM2[n][k]=@1":
```

(here BINOM2 refers to the automaton given in Figure 1). The output of this command is a Maple program containing the linear representation of the sequence ( 1.1) (i.e., the triple ( v, γ, w) (v,\gamma,w) such that T ⁡ ( n) = v ​ γ ​ ( [n] 2) ​ w T(n)=v\gamma([n]_{2})w). (In fact, what the eval command does in this case is return a linear representation for the sequence that counts, as a function of n n, the number of k k ’s for which the expression in quotation marks evaluates to TRUE.)

It is important to note that the linear representation that Walnut generates may not have minimal rank. However, there is an algorithm due to Schutzenberger and presented in the book of Berstel and Reutenauer [3, Section 2.3], that will take a linear representation of a regular sequence and produce a new representation of minimal rank. When we refer to ‘‘minimizing’’ a linear representation, we mean applying this algorithm 1 1 1 Jeffrey Shallit has kindly provided us with a Maple implementation of the minimization algorithm..

## 3 The run length transform of a linear recurrence sequence

In order to obtain Wu’s results, we need to make the connection between the linear representations for ( 1.1) computed in the previous section and the run length transform of linear recurrence sequences.

###### Definition 2.

Let ( S ⁡ ( n)) n ≥ 0 (S(n))_{n\geq 0} be a sequence defined by:

 | S ⁡ ( n + 1) = d 0 ​ S ​ ( n) + ⋯ + d r ​ S ​ ( n − r) S(n+1)=d_{0}S(n)+\dots+d_{r}S(n-r) |  | (3.1) |

with

 | S ⁡ ( i) = { 1 if ​ i = 0 c i if ​ i = 1,.., r S(i)=\begin{cases}1&\text{if }i=0\\ c_{i}&\text{if }i=1,..,r\end{cases} |  |

We define

 | v \displaystyle v | = [1 0 … 0] 1 × ( r + 1), w = [1 c 1 c r], \displaystyle=\begin{bmatrix}1&0&\dots&0\end{bmatrix}_{1\times(r+1)},\quad\quad w=\begin{bmatrix}1\\ c_{1}\\ \vdots\\ c_{r}\end{bmatrix}, |  |

 | γ ⁡ ( 0) \displaystyle\gamma(0) | = [1 0 … 0 c 1 0 … 0 … c r 0 … 0], γ ⁡ ( 1) = [0 I r × r 0 d r … d 0] \displaystyle=\begin{bmatrix}1&0&\dots&0\\ c_{1}&0&\dots&0\\ \vdots&\vdots&\dots&\vdots\\ c_{r}&0&\dots&0\end{bmatrix},\quad\gamma(1)=\begin{bmatrix}0\\ \vdots&I_{r\times r}\\ 0\\ d_{r}&\dots&d_{0}\end{bmatrix} |  |

We will prove that ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w) is a linear representation for the run length transform T ⁡ ( n) T(n) of S ⁡ ( n) S(n).

For the purposes of the following two results, let

 | w n:= [S ⁡ ( n) S ⁡ ( n + 1) S ⁡ ( n + r)], where ​ w 0 = [S ⁡ ( 0) S ⁡ ( 1) S ⁡ ( r)] = [1 c 1 c r] = w \displaystyle w_{n}:=\begin{bmatrix}S(n)\\ S(n+1)\\ \vdots\\ S(n+r)\end{bmatrix},\;\text{where}\;w_{0}=\begin{bmatrix}S(0)\\ S(1)\\ \vdots\\ S(r)\end{bmatrix}=\begin{bmatrix}1\\ c_{1}\\ \vdots\\ c_{r}\end{bmatrix}=w |  |

###### Lemma 3.

S ⁡ ( n) = v ​ γ ​ ( 1) n ​ w S(n)=v\gamma(1)^{n}w.

###### Proof.

Let n ≥ n\geq 1. Observe:

 | γ ⁡ ( 1) ​ w n \displaystyle\gamma(1)w_{n} | = [0 I r × r 0 d r … d 0] ​ [S ⁡ ( n) S ⁡ ( n + 1) S ⁡ ( n + r)] \displaystyle=\begin{bmatrix}0\\ \vdots&I_{r\times r}\\ 0\\ d_{r}&\dots&d_{0}\end{bmatrix}\begin{bmatrix}S(n)\\ S(n+1)\\ \vdots\\ S(n+r)\end{bmatrix} |  |

 |  | = [S ⁡ ( n + 1) S ⁡ ( n + 2) d r ​ S ​ ( n) + d r − 1 ​ S ​ ( n + 1) + ⋯ + d 0 ​ S ​ ( n + r)] \displaystyle=\begin{bmatrix}S(n+1)\\ S(n+2)\\ \vdots\\ d_{r}S(n)+d_{r-1}S(n+1)+\dots+d_{0}S(n+r)\end{bmatrix} |  |

 |  | = w n + 1. \displaystyle=w_{n+1}. |  |

Then

 | γ ​ ( 1) n ​ w = γ ​ ( 1) n − 1 ​ ( γ ⁡ ( 1) ​ w) = γ ​ ( 1) n − 1 ​ w 1 = ⋯ = w n. \gamma(1)^{n}w=\gamma(1)^{n-1}(\gamma(1)w)=\gamma(1)^{n-1}w_{1}=\dots=w_{n}. |  | (3.2) |

Therefore,

 | v ​ γ ​ ( 1) n ​ w = v ​ w n = [1 0 … 0] ​ [S ⁡ ( n) S ⁡ ( n + 1) S ⁡ ( n + r)] = S ⁡ ( n). \displaystyle v\gamma(1)^{n}w=vw_{n}=\begin{bmatrix}1&0&\dots&0\end{bmatrix}\begin{bmatrix}S(n)\\ S(n+1)\\ \vdots\\ S(n+r)\end{bmatrix}=S(n). |  |

∎

###### Theorem 4.

The run length transform T ⁡ ( n) T(n) of the linear recurrence sequence S ⁡ ( n) S(n) is a 2 2 -regular sequence. In particular, we have T ⁡ ( n) = v ​ γ ​ ( [n] 2) ​ w T(n)=v\gamma([n]_{2})w.

###### Proof.

First, note that:

 | γ ​ ( 0) 2 = [1 0 … 0 c 1 0 … 0 … c r 0 … 0] 2 = γ ⁡ ( 0) \gamma(0)^{2}=\begin{bmatrix}1&0&\dots&0\\ c_{1}&0&\dots&0\\ \vdots&\vdots&\dots&\vdots\\ c_{r}&0&\dots&0\end{bmatrix}^{2}=\gamma(0) |  | (3.3) |

It follows that for any integer k ≥ 0 k\geq 0, γ ​ ( 0) k = γ ⁡ ( 0) \gamma(0)^{k}=\gamma(0). Now let n ≥ 0 n\geq 0, then:

 | γ ⁡ ( 0) ​ w n \displaystyle\gamma(0)w_{n} | = [1 0 … 0 c 1 0 … 0 … c r 0 … 0] ​ [S ⁡ ( n) S ⁡ ( n + 1) S ⁡ ( n + r)] \displaystyle=\begin{bmatrix}1&0&\dots&0\\ c_{1}&0&\dots&0\\ \vdots&\vdots&\dots&\vdots\\ c_{r}&0&\dots&0\end{bmatrix}\begin{bmatrix}S(n)\\ S(n+1)\\ \vdots\\ S(n+r)\end{bmatrix} |  |

 |  | = [S ⁡ ( n) c 1 ​ S ​ ( n) c r ​ S ​ ( n)] \displaystyle=\begin{bmatrix}S(n)\\ c_{1}S(n)\\ \vdots\\ c_{r}S(n)\end{bmatrix} |  |

 |  | = S ⁡ ( n) ​ [1 c 1 c r] \displaystyle=S(n)\begin{bmatrix}1\\ c_{1}\\ \vdots\\ c_{r}\end{bmatrix} |  |

 |  | = S ⁡ ( n) ​ w. \displaystyle=S(n)w. |  |

So

 | γ ⁡ ( 0) ​ w n = S ⁡ ( n) ​ w. \gamma(0)w_{n}=S(n)w. |  | (3.4) |

Now let [n] 2 = 1 a 1 0 b 1 ⋯ 1 a k 0 b k [n]_{2}=1^{a_{1}}0^{b_{1}}\cdots 1^{a_{k}}0^{b_{k}} for some k ≥ 1 k\geq 1, and a i, b i ≥ 1 a_{i},b_{i}\geq 1 for i = 1, …, k i=1,\dots,k, except possible b k = 0 b_{k}=0. But if b k ≠ 0 b_{k}\neq 0, then γ ​ ( 0) b k ​ w = γ ⁡ ( 0) ​ w = S ⁡ ( 0) ​ w = w \gamma(0)^{b_{k}}w=\gamma(0)w=S(0)w=w, so without loss of generality, we may assume b k = 0 b_{k}=0. Then using ( 3.2), ( 3.3), ( 3.4), and Lemma 3, we get our result:

 | v ​ γ ​ ( [n] 2) ​ w \displaystyle v\gamma([n]_{2})w | = v ​ γ ​ ( 1 a 1 ​ 0 b 1 ​ ⋯ ​ 0 b k − 1 ​ 1 a k) ​ w \displaystyle=v\gamma(1^{a_{1}}0^{b_{1}}\dotsm 0^{b_{k-1}}1^{a_{k}})w |  |

 |  | = v ​ γ ​ ( 1) a 1 ​ γ ​ ( 0) b 1 ​ ⋯ ​ γ ​ ( 0) b k − 1 ​ γ ​ ( 1) a k ​ w \displaystyle=v\gamma(1)^{a_{1}}\gamma(0)^{b_{1}}\dotsm\gamma(0)^{b_{k-1}}\gamma(1)^{a_{k}}w |  |

 |  | = v ​ γ ​ ( 1) a 1 ​ γ ​ ( 0) ​ ⋯ ​ γ ​ ( 0) ​ γ ​ ( 1) a k ​ w \displaystyle=v\gamma(1)^{a_{1}}\gamma(0)\dotsm\gamma(0)\gamma(1)^{a_{k}}w |  |

 |  | = v ​ γ ​ ( 1) a 1 ​ γ ​ ( 0) ​ ⋯ ​ γ ​ ( 0) ​ w a k \displaystyle=v\gamma(1)^{a_{1}}\gamma(0)\dotsm\gamma(0)w_{a_{k}} |  |

 |  | = v ​ γ ​ ( 1) a 1 ​ γ ​ ( 0) ​ ⋯ ​ γ ​ ( 1) a k − 1 ​ S ​ ( a k) ​ w \displaystyle=v\gamma(1)^{a_{1}}\gamma(0)\dotsm\gamma(1)^{a_{k-1}}S(a_{k})w |  |

 |  |  |

 |  | = S ⁡ ( a k) ​ S ​ ( a k − 1) ​ ⋯ ​ S ​ ( a 2) ​ v ​ γ ​ ( 1) a 1 ​ w \displaystyle=S(a_{k})S(a_{k-1})\dotsm S(a_{2})v\gamma(1)^{a_{1}}w |  |

 |  | = S ⁡ ( a k) ​ S ​ ( a k − 1) ​ ⋯ ​ S ​ ( a 2) ​ S ​ ( a 1) \displaystyle=S(a_{k})S(a_{k-1})\dotsm S(a_{2})S(a_{1}) |  |

 |  | = ∑ i ∈ ℒ ⁡ ( n) S ⁡ ( i) = T ⁡ ( n) \displaystyle=\sum_{i\in\mathcal{L}(n)}S(i)=T(n) |  |

∎

We can therefore generate the n t ​ h n^{th} term of S ⁡ ( n) S(n) by evaluating v ​ γ ​ ( 1) n ​ w v\gamma(1)^{n}w and the n t ​ h n^{th} term of T ⁡ ( n) T(n) by evaluating v ​ γ ​ ( [n] 2) ​ w v\gamma([n]_{2})w. So if a sequence T ⁡ ( n) T(n) defined by ( 1.1) has an associated quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), then T ⁡ ( n) T(n) is the run length transform of S ⁡ ( n) S(n), where the coefficients of S ⁡ ( n) S(n) are given by the bottom row of γ ⁡ ( 1) \gamma(1), and the first r + 1 r+1 terms are given by w w.

## 4 Wu’s run length transforms

The theorems in this section are due to Wu [6], but are proved by obtaining a linear representation using Walnut, minimizing the linear representation, if necessary, and observing that the resulting linear representation gives the run length transform of the specified linear recurrence sequence, as described in Theorem 4. In this way we avoid the technical bitwise arithmetic of Wu’s proofs.

###### Theorem 5.

Let T ⁡ ( n) = ∑ k = 0 n [( n − k 2 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n-k}{2k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the Fibonacci sequence 1, 1, 2, 3, 5, 8, … 1,1,2,3,5,8,\dots (OEIS A000045).

###### Proof.

Putting the above sequence into Walnut returns the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0], w = [1 1], γ ⁡ ( 0) = [1 0 1 0], γ ⁡ ( 1) = [0 1 1 1] \displaystyle v=\begin{bmatrix}1&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0\\ 1&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1\\ 1&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) S(n)=S(n-1)+S(n-2) for n ≥ 2 n\geq 2, with S ⁡ ( 0) = S ⁡ ( 1) = 1 S(0)=S(1)=1. This is precisely the Fibonacci sequence, which confirms the result. ∎

###### Theorem 6.

Let T ⁡ ( n) = ∑ k = 0 n [( 3 ​ k k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{3k}{k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the truncated Fibonacci sequence 1, 2, 3, 5, 8, 13, … 1,2,3,5,8,13,\dots

###### Proof.

Putting the above sequence into Walnut, and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0], w = [1 2], γ ⁡ ( 0) = [1 0 2 0], γ ⁡ ( 1) = [0 1 1 1] \displaystyle v=\begin{bmatrix}1&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 2\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0\\ 2&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1\\ 1&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) S(n)=S(n-1)+S(n-2) for n ≥ 2 n\geq 2, with S ⁡ ( 0) = 1 S(0)=1, S ⁡ ( 1) = 2 S(1)=2. This is precisely the truncated Fibonacci sequence, which confirms the result. ∎

###### Theorem 7.

Let T ⁡ ( n) \displaystyle T(n) = ∑ k = 0 n [( n 2 ​ k) ​ ( n k) ( mod 2)] \sum^{n}_{k=0}\Bigg[\dbinom{n}{2k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence 1, 1, 2, 4, 8, 16, …, 1,1,2,4,8,16,\dots, i.e., 1 1 followed by the positive powers of 2 2 (OEIS A000079).

###### Proof.

Putting the above sequence into Walnut returns the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0], w = [1 1], γ ⁡ ( 0) = [1 0 1 0], γ ⁡ ( 1) = [0 1 0 2] \displaystyle v=\begin{bmatrix}1&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0\\ 1&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1\\ 0&2\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = 2 ​ S ​ ( n − 1) S(n)=2S(n-1) for n ≥ 2 n\geq 2, with S ⁡ ( 0) = S ⁡ ( 1) = 1 S(0)=S(1)=1. This is precisely the sequence 1 1 followed by the positive powers of 2 2, which confirms the result. ∎

###### Theorem 8.

Let T ⁡ ( n) = ∑ k = 0 n [( n + 2 ​ k 2 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n+2k}{2k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence 1, 2, 2, 2, 2, 2, …, 1,2,2,2,2,2,\dots, i.e., the sequence of 2 2 ’s prepended with a 1 1 (OEIS A040000).

###### Proof.

Putting the above sequence into Walnut, and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0], w = [1 2], γ ⁡ ( 0) = [1 0 2 0], γ ⁡ ( 1) = [0 1 0 1] \displaystyle v=\begin{bmatrix}1&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 2\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0\\ 2&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1\\ 0&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) S(n)=S(n-1) for n ≥ 2 n\geq 2, with S ⁡ ( 0) = 1 S(0)=1, S ⁡ ( 1) = 2 S(1)=2. This is precisely the sequence of 2 2 ’s, prepended with a 1 1, which confirms the result. ∎

###### Theorem 9.

Let T ⁡ ( n) = ∑ k = 0 n [( n + k n − k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n+k}{n-k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence of positive integers 1, 2, 3, 4, 5, 6, … 1,2,3,4,5,6,\dots (OEIS A000027).

###### Proof.

Putting the above sequence into Walnut, and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0], w = [1 2], γ ⁡ ( 0) = [1 0 2 0], γ ⁡ ( 1) = [0 1 − 1 2] \displaystyle v=\begin{bmatrix}1&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 2\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0\\ 2&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1\\ -1&2\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = 2 ​ S ​ ( n − 1) − S ⁡ ( n − 2) S(n)=2S(n-1)-S(n-2) for n ≥ 2 n\geq 2, with S ⁡ ( 0) = 1 S(0)=1, S ⁡ ( 1) = 2 S(1)=2. This is precisely the sequence of positive integers, which confirms the result. ∎

###### Theorem 10.

Let T ⁡ ( n) = ∑ k = 0 n [( n − k 6 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n-k}{6k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of Narayana’s cows sequence 1, 1, 1, 2, 3, 4, 6, 9, … 1,1,1,2,3,4,6,9,\dots (OEIS A000930).

###### Proof.

Putting the above sequence into Walnut returns the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0], w = [1 1 1], γ ⁡ ( 0) = [1 0 0 1 0 0 1 0 0], γ ⁡ ( 1) = [0 1 0 0 0 1 1 0 1] \displaystyle v=\begin{bmatrix}1&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0\\ 1&0&0\\ 1&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0\\ 0&0&1\\ 1&0&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 3) S(n)=S(n-1)+S(n-3) for n ≥ 3 n\geq 3, with S ⁡ ( 0) = S ⁡ ( 1) = S ⁡ ( 2) = 1 S(0)=S(1)=S(2)=1. This is precisely Narayana’s cows sequence, which confirms the result. ∎

###### Theorem 11.

Let T ⁡ ( n) = ∑ k = 0 n [( n + 3 ​ k 6 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n+3k}{6k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence of doubled positive integers, i.e., 1, 1, 2, 2, 3, 3, 4, 4, … 1,1,2,2,3,3,4,4,\dots (OEIS A008619).

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0], w = [1 1 2], γ ⁡ ( 0) = [1 0 0 1 0 0 2 0 0], γ ⁡ ( 1) = [0 1 0 0 0 1 − 1 1 1] \displaystyle v=\begin{bmatrix}1&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 2\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0\\ 1&0&0\\ 2&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0\\ 0&0&1\\ -1&1&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = − S ⁡ ( n − 1) + S ⁡ ( n − 2) + S ⁡ ( n − 3) S(n)=-S(n-1)+S(n-2)+S(n-3) for n ≥ 3 n\geq 3, with S ⁡ ( 0) = S ⁡ ( 1) = 1 S(0)=S(1)=1, S ⁡ ( 2) = 2 S(2)=2. This is precisely the sequence of doubled positive integers, which confirms the result. ∎

###### Theorem 12.

Let T ⁡ ( n) = ∑ k = 0 n [( n + 2 ​ k 2 ​ n − k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n+2k}{2n-k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the Lucas numbers, prepended with the terms 1, 1 1,1, i.e., the sequence 1, 1, 2, 1, 3, 4, 7, 11, … 1,1,2,1,3,4,7,11,\dots (OEIS A329723).

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0 0], w = [1 1 2 1], γ ⁡ ( 0) = [1 0 0 0 1 0 0 0 2 0 0 0 1 0 0 0], γ ⁡ ( 1) = [0 1 0 0 0 0 1 0 0 0 0 1 0 0 1 1] \displaystyle v=\begin{bmatrix}1&0&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 2\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0&0\\ 1&0&0&0\\ 2&0&0&0\\ 1&0&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0&0\\ 0&0&1&0\\ 0&0&0&1\\ 0&0&1&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) S(n)=S(n-1)+S(n-2) for n ≥ 4 n\geq 4, with S ⁡ ( 0) = S ⁡ ( 1) = 1 S(0)=S(1)=1, S ⁡ ( 2) = 2 S(2)=2, S ⁡ ( 3) = 1 S(3)=1. This is precisely the Lucas numbers prepended by the terms 1, 1 1,1. ∎

## 5 New run length transforms

In this section we give some new run length transforms.

###### Theorem 13.

Let T ⁡ ( n) = ∑ k = 0 n [( n + 5 ​ k 2 ​ n + 2 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\left[\dbinom{n+5k}{2n+2k}\dbinom{n}{k}\pmod{2}\right]. Then T ⁡ ( n) T(n) is the run length transform of the sequence generated by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) − S ⁡ ( n − 3) + S ⁡ ( n − 4) S(n)=S(n-1)+S(n-2)-S(n-3)+S(n-4) for n ≥ 4 n\geq 4, with S ⁡ ( 0) = S ⁡ ( 1) = S ⁡ ( 2) = S ⁡ ( 3) = 1 S(0)=S(1)=S(2)=S(3)=1; i.e., the sequence 1, 1, 1, 1, 2, 3, 5, 7, 11, 16, 25, … 1,1,1,1,2,3,5,7,11,16,25,\dots.

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0 0], w = [1 1 1 1], γ ⁡ ( 0) = [1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0], γ ⁡ ( 1) = [0 1 0 0 0 0 1 0 0 0 0 1 1 − 1 1 1] \displaystyle v=\begin{bmatrix}1&0&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 1\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0&0\\ 1&0&0&0\\ 1&0&0&0\\ 1&0&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0&0\\ 0&0&1&0\\ 0&0&0&1\\ 1&-1&1&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) − S ⁡ ( n − 3) + S ⁡ ( n − 4) S(n)=S(n-1)+S(n-2)-S(n-3)+S(n-4) for n ≥ 4 n\geq 4, with S ⁡ ( 0) = S ⁡ ( 1) = S ⁡ ( 2) = S ⁡ ( 3) = 1 S(0)=S(1)=S(2)=S(3)=1; i.e., the sequence 1, 1, 1, 1, 2, 3, 5, 7, 11, 16, 25, … 1,1,1,1,2,3,5,7,11,16,25,\dots. ∎

###### Theorem 14.

Let T ⁡ ( n) = ∑ k = 0 n [( n + 5 ​ k 2 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n+5k}{2k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence generated by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) − S ⁡ ( n − 3) + S ⁡ ( n − 4) S(n)=S(n-1)+S(n-2)-S(n-3)+S(n-4), with S ⁡ ( 0) = 1 S(0)=1, S ⁡ ( 1) = S ⁡ ( 2) = 2 S(1)=S(2)=2, S ⁡ ( 3) = 3 S(3)=3.

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0 0], w = [1 2 2 3], γ ⁡ ( 0) = [1 0 0 0 2 0 0 0 2 0 0 0 3 0 0 0], γ ⁡ ( 1) = [0 1 0 0 0 0 1 0 0 0 0 1 1 − 1 1 1] \displaystyle v=\begin{bmatrix}1&0&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 2\\ 2\\ 3\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0&0\\ 2&0&0&0\\ 2&0&0&0\\ 3&0&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0&0\\ 0&0&1&0\\ 0&0&0&1\\ 1&-1&1&1\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 1) + S ⁡ ( n − 2) − S ⁡ ( n − 3) + S ⁡ ( n − 4) S(n)=S(n-1)+S(n-2)-S(n-3)+S(n-4) for n ≥ 4 n\geq 4, with S ⁡ ( 0) = 1 S(0)=1, S ⁡ ( 1) = S ⁡ ( 2) = 2 S(1)=S(2)=2, S ⁡ ( 3) = 3 S(3)=3. ∎

Note that the previous two sequences are generated by the same rule, and differ only by their starting terms.

###### Theorem 15.

Let T ⁡ ( n) = ∑ k = 0 n [( − n + 7 ​ k n + k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{-n+7k}{n+k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the Padovan numbers (OEIS A000931) starting with offset 5 5, i.e. the sequence 1, 1, 1, 2, 2, 3, 4, 5, … 1,1,1,2,2,3,4,5,\dots

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0], w = [1 1 1], γ ⁡ ( 0) = [1 0 0 1 0 0 1 0 0], γ ⁡ ( 1) = [0 1 0 0 0 1 1 1 0] \displaystyle v=\begin{bmatrix}1&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0\\ 1&0&0\\ 1&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0\\ 0&0&1\\ 1&1&0\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 2) + S ⁡ ( n − 3) S(n)=S(n-2)+S(n-3) for n ≥ 3 n\geq 3, with S ⁡ ( 0) = S ⁡ ( 1) = S ⁡ ( 2) = 1 S(0)=S(1)=S(2)=1. This is precisely the Padovan numbers starting with offset 5 5. ∎

###### Theorem 16.

Let T ⁡ ( n) = ∑ k = 0 n [( n + 7 ​ k 3 ​ n + k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{n+7k}{3n+k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the Padovan numbers (OEIS A000931) starting with offset 3 3, i.e. the sequence 1, 0, 1, 1, 1, 2, 2, 3, … 1,0,1,1,1,2,2,3,\dots

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0], w = [1 0 1], γ ⁡ ( 0) = [1 0 0 1 0 0 1 0 0], γ ⁡ ( 1) = [0 1 0 0 0 1 1 1 0] \displaystyle v=\begin{bmatrix}1&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 0\\ 1\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0\\ 1&0&0\\ 1&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0\\ 0&0&1\\ 1&1&0\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 2) + S ⁡ ( n − 3) S(n)=S(n-2)+S(n-3) for n ≥ 3 n\geq 3, with S ⁡ ( 0) = 1 S(0)=1, S ⁡ ( 1) = 0 S(1)=0, S ⁡ ( 2) = 1 S(2)=1. This is precisely the Padovan numbers starting with offset 3 3. ∎

###### Theorem 17.

Let T ⁡ ( n) = ∑ k = 0 n [( 6 ​ k n + 3 ​ k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{6k}{n+3k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence given by alternating between 1 1 and the natural numbers, i.e. the sequence 1, 1, 1, 2, 1, 3, 1, 4, … 1,1,1,2,1,3,1,4,\dots

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0 0], w = [1 1 1 2], γ ⁡ ( 0) = [1 0 0 0 1 0 0 0 1 0 0 0 2 0 0 0], γ ⁡ ( 1) = [0 1 0 0 0 0 1 0 0 0 0 1 − 1 0 2 0] \displaystyle v=\begin{bmatrix}1&0&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 1\\ 2\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0&0\\ 1&0&0&0\\ 1&0&0&0\\ 2&0&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0&0\\ 0&0&1&0\\ 0&0&0&1\\ -1&0&2&0\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = 2 ​ S ​ ( n − 2) − S ⁡ ( n − 4) S(n)=2S(n-2)-S(n-4) for n ≥ 4 n\geq 4, with S ⁡ ( 0) = S ⁡ ( 1) = S ⁡ ( 2) = 1 S(0)=S(1)=S(2)=1, S ⁡ ( 3) = 2 S(3)=2, which is the sequence alternating between 1 1 and the natural numbers. ∎

###### Theorem 18.

Let T ⁡ ( n) = ∑ k = 0 n [( − 2 ​ n + 8 ​ k n + k) ​ ( n k) ( mod 2)] \displaystyle T(n)=\sum^{n}_{k=0}\Bigg[\dbinom{-2n+8k}{n+k}\dbinom{n}{k}\pmod{2}\Bigg]. Then T ⁡ ( n) T(n) is the run length transform of the sequence with period 1, 1, 0 1,1,0.

###### Proof.

Putting the above sequence into Walnut and then minimizing it, we get the quadruple ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w), with:

 | v = [1 0 0], w = [1 1 0], γ ⁡ ( 0) = [1 0 0 1 0 0 0 0 0], γ ⁡ ( 1) = [0 1 0 0 0 1 1 0 0] \displaystyle v=\begin{bmatrix}1&0&0\end{bmatrix},\;w=\begin{bmatrix}1\\ 1\\ 0\end{bmatrix},\;\gamma(0)=\begin{bmatrix}1&0&0\\ 1&0&0\\ 0&0&0\end{bmatrix},\;\gamma(1)=\begin{bmatrix}0&1&0\\ 0&0&1\\ 1&0&0\end{bmatrix} |  |

Thus by Lemma 3 and Theorem 4, T ⁡ ( n) T(n) is the run length transform of the sequence defined by S ⁡ ( n) = S ⁡ ( n − 3) S(n)=S(n-3) for n ≥ 3 n\geq 3, with S ⁡ ( 0) = S ⁡ ( 1) = 1 S(0)=S(1)=1, S ⁡ ( 2) = 0 S(2)=0, which is the sequence with period 1, 1, 0 1,1,0. ∎

## 6 Average value of select run length transforms

One of the advantages of using linear representations to describe the run length transforms T ⁡ ( n) T(n) that we have given in the previous sections is that we can easily compute the average value of T ⁡ ( n) T(n) in the interval 2 r ≤ n < 2 r + 1 2^{r}\leq n<2^{r+1} for r ≥ 0 r\geq 0. The method is described, with many examples, in Shallit [4, Sections 9.8–9.11].

We will give the details of this calculation for the sequence given in Theorem 5, and simply state the rest. Let ( v, γ ⁡ ( 0), γ ⁡ ( 1), w) (v,\gamma(0),\gamma(1),w) be as in Theorem 5, and define

 | M = γ ⁡ ( 0) + γ ⁡ ( 1) = [1 0 1 0] + [0 1 1 1] = [1 1 2 1]. M=\gamma(0)+\gamma(1)=\begin{bmatrix}1&0\\ 1&0\end{bmatrix}+\begin{bmatrix}0&1\\ 1&1\end{bmatrix}=\begin{bmatrix}1&1\\ 2&1\end{bmatrix}. |  |

Let g ⁡ ( r) g(r) denote the sum of the first 2 r 2^{r} terms of T ⁡ ( n) T(n). Then

 | g ⁡ ( r) \displaystyle g(r) | = ∑ 0 ≤ n < 2 r T ⁡ ( n) \displaystyle=\sum_{0\leq n<2^{r}}T(n) |  |

 |  | = ∑ 0 ≤ n < 2 r v ​ γ ​ ( [n] 2) ​ w \displaystyle=\sum_{0\leq n<2^{r}}v\gamma([n]_{2})w |  |

 |  | = v ⁡ ( ∑ 0 ≤ n < 2 r γ ⁡ ( [n] 2)) ​ w \displaystyle=v\left(\sum_{0\leq n<2^{r}}\gamma([n]_{2})\right)w |  |

 |  | = v ⁡ ( ∑ z ∈ { 0, 1 } n γ ⁡ ( z)) ​ w \displaystyle=v\left(\sum_{z\in\{0,1\}^{n}}\gamma(z)\right)w |  |

 |  | = v ​ ( γ ⁡ ( 0) + γ ⁡ ( 1)) n ​ w \displaystyle=v\left(\gamma(0)+\gamma(1)\right)^{n}w |  |

 |  | = v ​ M n ​ w. \displaystyle=vM^{n}w. |  |

The minimal polynomial for M M is

 | p ⁡ ( x) = x 2 − 2 ​ x − 1 = ( x − ( 1 + 2)) ​ ( x − ( 1 − 2)). \displaystyle p(x)=x^{2}-2x-1=(x-(1+\sqrt{2}))(x-(1-\sqrt{2})). |  |

It follows that g ⁡ ( r) g(r) is given by the exponential polynomial

 | g ⁡ ( r) = c 1 ​ ( 1 + 2) r + c 2 ​ ( 1 − 2) r, \displaystyle g(r)=c_{1}(1+\sqrt{2})^{r}+c_{2}(1-\sqrt{2})^{r}, |  |

for some coefficients c 1, c 2 c_{1},c_{2}, which we determine by solving the linear system

 | g ⁡ ( 0) \displaystyle g(0) | = 1 = c 1 + c 2 \displaystyle=1=c_{1}+c_{2} |  |

 | g ⁡ ( 1) \displaystyle g(1) | = 2 = c 1 ​ ( 1 + 2) + c 2 ​ ( 1 − 2). \displaystyle=2=c_{1}(1+\sqrt{2})+c_{2}(1-\sqrt{2}). |  |

We get

 | c 1 = 1 + 2 2 ​ 2, c 2 = − 1 − 2 2 ​ 2, \displaystyle c_{1}=\frac{1+\sqrt{2}}{2\sqrt{2}},\quad c_{2}=-\frac{1-\sqrt{2}}{2\sqrt{2}}, |  |

and hence,

 | g ⁡ ( r) \displaystyle g(r) | = 1 + 2 2 ​ 2 ​ ( 1 + 2) r − 1 − 2 2 ​ 2 ​ ( 1 − 2) r \displaystyle=\frac{1+\sqrt{2}}{2\sqrt{2}}(1+\sqrt{2})^{r}-\frac{1-\sqrt{2}}{2\sqrt{2}}(1-\sqrt{2})^{r} |  |

 |  | = 1 2 ​ 2 ​ ( ( 1 + 2) r + 1 − ( 1 − 2) r + 1). \displaystyle=\frac{1}{2\sqrt{2}}\left((1+\sqrt{2})^{r+1}-(1-\sqrt{2})^{r+1}\right). |  |

Next, we want to find g ⁡ ( r + 1) − g ⁡ ( r) g(r+1)-g(r), which is the sum of the terms of T ⁡ ( n) T(n) in the range 2 r ≤ n < 2 r + 1 2^{r}\leq n<2^{r+1}:

 | g ⁡ ( r + 1) − g ⁡ ( r) \displaystyle g(r+1)-g(r) | = 1 2 ​ 2 ​ ( ( ( 1 + 2) r + 2 − ( 1 − 2) r + 2) − ( ( 1 + 2) r + 1 − ( 1 − 2) r + 1)) \displaystyle=\frac{1}{2\sqrt{2}}\left(\left((1+\sqrt{2})^{r+2}-(1-\sqrt{2})^{r+2}\right)-\left((1+\sqrt{2})^{r+1}-(1-\sqrt{2})^{r+1}\right)\right) |  |

 |  | = ( ( ( 1 + 2) r + 2 − ( 1 + 2) r + 1) − ( ( 1 − 2) r + 2 − ( 1 − 2) r + 1)) \displaystyle=\left(\left((1+\sqrt{2})^{r+2}-(1+\sqrt{2})^{r+1}\right)-\left((1-\sqrt{2})^{r+2}-(1-\sqrt{2})^{r+1}\right)\right) |  |

 |  | = 1 2 ​ 2 ​ ( ( 1 + 2 − 1) ​ ( 1 + 2) r + 1 − ( 1 − 2 − 1) ​ ( 1 − 2) r + 1) \displaystyle=\frac{1}{2\sqrt{2}}\left((1+\sqrt{2}-1)(1+\sqrt{2})^{r+1}-(1-\sqrt{2}-1)(1-\sqrt{2})^{r+1}\right) |  |

 |  | = 1 2 ​ ( ( 1 + 2) r + 1 + ( 1 − 2) r + 1). \displaystyle=\frac{1}{2}\left((1+\sqrt{2})^{r+1}+(1-\sqrt{2})^{r+1}\right). |  |

Finally, the average value of T ⁡ ( n) T(n) in the range 2 r ≤ n < 2 r + 1 2^{r}\leq n<2^{r+1} is given by

 | μ ⁡ ( r) = g ⁡ ( r + 1) − g ⁡ ( r) 2 r = 1 2 r + 1 ​ ( ( 1 + 2) r + 1 + ( 1 − 2) r + 1). \displaystyle\mu(r)=\frac{g(r+1)-g(r)}{2^{r}}=\frac{1}{2^{r+1}}\bigg((1+\sqrt{2})^{r+1}+(1-\sqrt{2})^{r+1}\bigg). |  |

We now summarize the average values for some of Wu’s run length transforms (see Section 4) below, where the coefficients a i a_{i} refer to the parameters in ( 1.1). We omit the average value results for the results involving recurrence relations of order 3 3 or higher, since the roots of the associated minimal polynomials can’t be displayed as nicely, but the reader can easily carry out the above method for those sequences as well.

Reference | ( a 1, a 2, a 3, a 4) (a_{1},a_{2},a_{3},a_{4}) | Average Value μ ⁡ ( r) \mu(r) |

Thm. 5 | ( 1, − 1, 0, 2) (1,-1,0,2) | 1 2 r + 1 ​ ( ( 1 + 2) r + 1 + ( 1 − 2) r + 1) \frac{1}{2^{r+1}}\big((1+\sqrt{2})^{r+1}+(1-\sqrt{2})^{r+1}\big) |

Thm. 6 | ( 0, 3, 0, 1) (0,3,0,1) | 1 2 r + 1 ​ ( ( 2 + 3) ​ ( 1 + 3) r + ( 2 − 3) ​ ( 1 − 3) r) \frac{1}{2^{r+1}}\big((2+\sqrt{3})(1+\sqrt{3})^{r}+(2-\sqrt{3})(1-\sqrt{3})^{r}\big) |

Thm. 7 | ( 1, 0, 0, 2) (1,0,0,2) | 1 2 2 ​ r + 2 ​ 5 ​ ( ( 1 + 5) 2 ​ ( 3 + 5) r − ( 1 − 5) 2 ​ ( 3 − 5) r) \frac{1}{2^{2r+2}\sqrt{5}}\big((1+\sqrt{5})^{2}(3+\sqrt{5})^{r}-(1-\sqrt{5})^{2}(3-\sqrt{5})^{r}\big) |

Thm. 8 | ( 1, 2, 0, 2) (1,2,0,2) | 2 2 r + 1 ​ ( ( 1 + 2) r + 1 − ( 1 − 2) r + 1) \frac{\sqrt{2}}{2^{r+1}}\big((1+\sqrt{2})^{r+1}-(1-\sqrt{2})^{r+1}\big) |

Thm. 9 | ( 1, 1, 1, − 1) (1,1,1,-1) | 1 2 2 ​ r + 2 ​ 5 ​ ( ( 1 + 5) ​ ( 3 + 5) r + 1 − ( 1 − 5) ​ ( 3 − 5) r + 1) \frac{1}{2^{2r+2}\sqrt{5}}\big((1+\sqrt{5})(3+\sqrt{5})^{r+1}-(1-\sqrt{5})(3-\sqrt{5})^{r+1}\big) |

## 7 Characterizing a family of run length transforms

In this section we analyze the family of sequences defined by

 | T m ​ ( n) = ∑ k = 0 n [( 2 m ​ k n + k) ​ ( n k) ( mod 2)], T_{m}(n)=\sum^{n}_{k=0}\left[\binom{2^{m}k}{n+k}\binom{n}{k}\pmod{2}\right], |  |

for m ≥ 2 m\geq 2. We claim that T m ​ ( n) T_{m}(n) is the run length transform of the sequence defined by S m ​ ( n) = S m ​ ( n − m) S_{m}(n)=S_{m}(n-m) for n ≥ m n\geq m, with S m ​ ( 0) = 1, S m ​ ( 1) = S m ​ ( 2) = ⋯ = S m ​ ( m − 1) = 0 S_{m}(0)=1,S_{m}(1)=S_{m}(2)=\dots=S_{m}(m-1)=0, or, in other words, the sequence with the period of 1 1 followed by m − 1 m-1 0 0 ’s.

In the proofs that follow, we will be looking for integers k ≤ n k\leq n such that ( 2 m ​ k n + k) ≡ 1 ( mod 2) \binom{2^{m}k}{n+k}\equiv 1\pmod{2}. If for a particular k k, there exists i i such that the i t ​ h i^{th} bit of [2 m ​ k] 2 [2^{m}k]_{2} is 0 0, but the i t ​ h i^{th} bit of [n + k] 2 [n+k]_{2} is 1 1, then ( 2 m ​ k n + k) ≡ 0 ( mod 2) \binom{2^{m}k}{n+k}\equiv 0\pmod{2} by ( 2.2), and so we say the i t ​ h i^{th} bit fails. Here we count bits from right to left, starting with index 1 1.

Consider the case where n = 2 ℓ − 1 n=2^{\ell}-1 for some ℓ ≥ 0 \ell\geq 0. Then [n] 2 = 1 ℓ [n]_{2}=1^{\ell}, so ℒ ⁡ ( n) = { ℓ } \mathcal{L}(n)=\{\ell\}. Thus T m ​ ( n) = S m ​ ( ℓ) T_{m}(n)=S_{m}(\ell) in such cases.

###### Lemma 19.

Let n = 2 ℓ − 1 n=2^{\ell}-1 for some ℓ ≥ 0 \ell\geq 0. Then

 | T m ​ ( n) = { 1 if ​ ℓ ≡ 0 ( mod m), 0 otherwise. T_{m}(n)=\begin{cases}1&\text{if }\ell\equiv 0\pmod{m},\\ 0&\text{otherwise.}\end{cases} |  |

###### Proof.

We will show that for each n n of the form n = 2 ℓ − 1 n=2^{\ell}-1 with ℓ ≡ 0 ( mod m) \ell\equiv 0\pmod{m}, there is exactly one k k such that ( 2 m ​ k n + k) ≡ 1 ( mod 2) \binom{2^{m}k}{n+k}\equiv 1\pmod{2}, namely, k = 2 ℓ − 1 2 m − 1 k=\frac{2^{\ell}-1}{2^{m}-1}, and that only n n ’s of this form have such a k k. In fact, 2 ℓ − 1 2 m − 1 \frac{2^{\ell}-1}{2^{m}-1} is an integer only when ℓ ≡ 0 ( mod m) \ell\equiv 0\pmod{m}. So such a k k only exists under these conditions, and it is this observation which motivates the proof.

First, note that [n] 2 = 1 ℓ [n]_{2}=1^{\ell} implies ( n k) ≡ 1 ( mod 2) \binom{n}{k}\equiv 1\pmod{2} for k ≤ n k\leq n by ( 2.1) and ( 2.2). So T m ​ ( n) = ∑ k = 0 n [( 2 m ​ k n + k) ( mod 2)] T_{m}(n)=\sum^{n}_{k=0}\big[\binom{2^{m}k}{n+k}\pmod{2}\big]. Consider some k ≤ n k\leq n, where the length of [k] 2 [k]_{2} is r r. If 2 m ​ k < n + k 2^{m}k<n+k, then ( 2 m ​ k n + k) = 0 \binom{2^{m}k}{n+k}=0, so assume 2 m ​ k ≥ n + k 2^{m}k\geq n+k, or equivalently,

 | n 2 m − 1 ≤ k ≤ n. \frac{n}{2^{m}-1}\leq k\leq n. |  | (7.1) |

Moreover, this also implies r ≤ ℓ r\leq\ell.

Clearly, if ℓ = 0 \ell=0, then n = 0 n=0, and T m ​ ( 0) = 1 T_{m}(0)=1. Suppose that 0 < ℓ < m 0<\ell<m. Then by ( 7.1), we have k > 0 k>0. But the first m m bits of [2 m ​ k] 2 [2^{m}k]_{2} will all be 0 0 ’s, and [n + k] 2 [n+k]_{2} will have length ℓ + 1 \ell+1, where the ( ℓ + 1) t ​ h (\ell+1)^{th} bit is 1 1. However, we have ℓ + 1 ≤ m \ell+1\leq m, which means that the ( ℓ + 1) t ​ h (\ell+1)^{th} bit of [2 m ​ k] 2 [2^{m}k]_{2} is a 0 0, and hence the ( ℓ + 1) t ​ h (\ell+1)^{th} bit fails. So for every n = 2 ℓ − 1 n=2^{\ell}-1 with 0 < ℓ < m 0<\ell<m, there is no k ≤ n k\leq n such that ( 2 m ​ k n + k) ≢ 0 ( mod 2) \binom{2^{m}k}{n+k}\not\equiv 0\pmod{2}. So the claim holds for ℓ < m \ell<m.

Write

 | [k] 2 \displaystyle[k]_{2} | = a ℓ ⋯ a 1, \displaystyle=a_{\ell}\cdots a_{1}, |  |

 | [n + k] 2 \displaystyle[n+k]_{2} | = b ℓ + 1 ⋯ b 1, and \displaystyle=b_{\ell+1}\cdots b_{1},\text{ and} |  |

 | [2 m ​ k] 2 \displaystyle[2^{m}k]_{2} | = c ℓ + m ⋯ c 1, \displaystyle=c_{\ell+m}\cdots c_{1}, |  |

where a ℓ, …, a ℓ − m + 1 a_{\ell},\ldots,a_{\ell-m+1} may be 0 0 ’s if necessary. Of course, we have c ℓ + m ⋯ c m + 1 = a ℓ ⋯ a 1 c_{\ell+m}\cdots c_{m+1}=a_{\ell}\cdots a_{1} and c m ⋯ c 1 = 0 m c_{m}\cdots c_{1}=0^{m}. Furthermore, we suppose there is no index i i such that c i = 0 c_{i}=0 and b i = 1 b_{i}=1.

Note that since [n] 2 = 1 ℓ [n]_{2}=1^{\ell}, when adding n + k n+k there is a carry at every position after the first. Since c m ⋯ c 1 = 0 m c_{m}\cdots c_{1}=0^{m}, we have b m ⋯ b 1 = 0 m b_{m}\cdots b_{1}=0^{m}. However, this forces a m ⋯ a 1 = 0 m − 1 1 a_{m}\cdots a_{1}=0^{m-1}1. Now since a m ⋯ a 2 = c 2 ​ m ⋯ c m + 2 = 0 m − 1 a_{m}\cdots a_{2}=c_{2m}\cdots c_{m+2}=0^{m-1}, we have b 2 ​ m ⋯ b m + 2 = 0 m − 1 b_{2m}\cdots b_{m+2}=0^{m-1}. However, this forces a 2 ​ m ⋯ a m + 2 = 0 m − 1 a_{2m}\cdots a_{m+2}=0^{m-1}. Continuing in this manner, we find that

 | b m ​ i ⋯ b m ⁡ ( i − 1) + 2 = a m ​ i ⋯ a m ⁡ ( i − 1) + 2 = 0 m − 1 b_{mi}\cdots b_{m(i-1)+2}=a_{mi}\cdots a_{m(i-1)+2}=0^{m-1} |  |

for i = 1, …, ⌊ ℓ / m ⌋. i=1,\ldots,\lfloor\ell/m\rfloor.

We also have b ℓ + 1 = 1 b_{\ell+1}=1, which implies ℓ ≡ 0 ( mod m) \ell\equiv 0\pmod{m}, since otherwise we would have ℓ + 1 − m ≢ 1 ( mod m) \ell+1-m\not\equiv 1\pmod{m} and hence a ℓ + 1 − m = c ℓ + 1 = 0 a_{\ell+1-m}=c_{\ell+1}=0, which is a contradiction. Indeed we must have a ℓ + 1 − m = c ℓ + 1 = 1 a_{\ell+1-m}=c_{\ell+1}=1, which forces b ℓ + 1 − m = 1 b_{\ell+1-m}=1. Continuing in this way we find that b ℓ + 1 − 2 ​ m = a ℓ + 1 − 2 ​ m = 1 b_{\ell+1-2m}=a_{\ell+1-2m}=1, and so on; i.e., that

 | a m ⁡ ( i − 1) + 1 = b m ⁡ ( i − 1) + 1 = 1 a_{m(i-1)+1}=b_{m(i-1)+1}=1 |  |

for i = 1, …, ℓ / m i=1,\ldots,\ell/m.

We have thus seen that ( 2 m ​ k n + k) ≡ 1 ( mod 2) \binom{2^{m}k}{n+k}\equiv 1\pmod{2} exactly when ℓ ≡ 0 ( mod m) \ell\equiv 0\pmod{m} and [k] 2 = ( 0 m − 1 ​ 1) ℓ / m [k]_{2}=(0^{m-1}1)^{\ell/m}; i.e., that

 | k = ∑ i = 0 ℓ m − 1 2 m ​ i = 2 ℓ − 1 2 m − 1. \displaystyle k=\sum_{i=0}^{\frac{\ell}{m}-1}2^{mi}=\frac{2^{\ell}-1}{2^{m}-1}. |  |

∎

Thus we have that T m ​ ( 2 ℓ − 1) = S m ​ ( ℓ) = 1 T_{m}(2^{\ell}-1)=S_{m}(\ell)=1. In order to prove T m ​ ( n) T_{m}(n) is indeed the run length transform of S m ​ ( n) S_{m}(n), it is sufficient to prove the following:

###### Theorem 20.

Let n ≥ 0 n\geq 0. Then

 | T m ​ ( n) = { 1 if each run of 1’s in ​ [n] 2 ​ has length divisible by m, 0 otherwise. T_{m}(n)=\begin{cases}1&\text{if each run of 1's in }[n]_{2}\text{ has length divisible by $m$},\\ 0&\text{otherwise}.\end{cases} |  |

###### Proof.

Let n ≥ 0 n\geq 0, where the length of [n] 2 = ℓ [n]_{2}=\ell. We’ve already covered the case where [n] 2 [n]_{2} is a run of ℓ \ell 1 1 ’s, so assume the j t ​ h j^{th} bit of [n] 2 [n]_{2} is 0 0. Then any k k with a 1 1 in the j t ​ h j^{th} bit will fail, as by ( 2.1):

 |  | ( n j k j) = ( 0 1) = 0 \displaystyle\dbinom{n_{j}}{k_{j}}=\dbinom{0}{1}=0 |  |

 | ⟹ \displaystyle\implies | ( n k) ≡ 0 ( mod 2) \displaystyle\dbinom{n}{k}\equiv 0\pmod{2} |  |

 | ⟹ \displaystyle\implies | ( 2 m ​ k n + k) ​ ( n k) ≡ 0 ( mod 2) \displaystyle\dbinom{2^{m}k}{n+k}\dbinom{n}{k}\equiv 0\pmod{2} |  |

So we only need to examine k ≤ n k\leq n such that

 | ∀ i ≤ ℓ, n i = 0 ⟹ k i = 0 \forall i\leq\ell,\;\;\;n_{i}=0\implies k_{i}=0 |  |

If [n] 2 [n]_{2} only has a single run of 1 1 ’s, say [n] 2 = 1 ℓ 1 ​ 0 t 1 [n]_{2}=1^{\ell_{1}}0^{t_{1}}, where t 1 ≥ 0 t_{1}\geq 0, then by the proof of Lemma 19, we have ℓ 1 ≡ 0 ( mod m) \ell_{1}\equiv 0\pmod{m} and the only possible k k that contributes a non-zero value to the sum defining T m ​ ( n) T_{m}(n) is [k] 2 = ( 0 m − 1 ​ 1) ℓ 1 / m ​ 0 t 1 [k]_{2}=(0^{m-1}1)^{\ell_{1}/m}0^{t_{1}}. So suppose [n] 2 [n]_{2} has two runs of 1 1 ’s, say

 | [n] 2 = 1 ℓ 2 ​ 0 t 2 ​ 1 ℓ 1 ​ 0 t 1, t 2 ≥ 1, t 1 ≥ 0. [n]_{2}=1^{\ell_{2}}0^{t_{2}}1^{\ell_{1}}0^{t_{1}},\quad t_{2}\geq 1,t_{1}\geq 0. |  |

Again, by Lemma 19 and its proof we have ℓ 1 ≡ 0 ( mod m) \ell_{1}\equiv 0\pmod{m} and the only possible k k that contributes a non-zero value to the sum defining T m ​ ( n) T_{m}(n) has the form

 | [k] 2 = a r ⋯ a r − ℓ 2 + 1 0 t 2 ( 0 m − 1 1) ℓ 1 / m 0 t 1, [k]_{2}=a_{r}\cdots a_{r-\ell_{2}+1}0^{t_{2}}(0^{m-1}1)^{\ell_{1}/m}0^{t_{1}}, |  |

where r = ℓ 2 + t 2 + ℓ 1 + t 1 r=\ell_{2}+t_{2}+\ell_{1}+t_{1}. Note that when adding n + k n+k, there is a carry at position ℓ 1 + t 1 + 1 \ell_{1}+t_{1}+1 but there is no carry at position r − ℓ 2 + 1 r-\ell_{2}+1. Furthermore, since t 2 ≥ 1 t_{2}\geq 1, there are at least m m 0 0 ’s to the right of a r ⋯ a r − ℓ 2 + 1 a_{r}\cdots a_{r-\ell_{2}+1} in [k] 2 [k]_{2}. We can therefore apply the same analysis from the proof of Lemma 19 to the run 1 ℓ 2 1^{\ell_{2}} in [n] 2 [n]_{2} and we find that ℓ 2 ≡ 0 ( mod m) \ell_{2}\equiv 0\pmod{m} and

 | [k] 2 = ( 0 m − 1 ​ 1) ℓ 2 / m ​ 0 t 2 ​ ( 0 m − 1 ​ 1) ℓ 1 / m ​ 0 t 1. [k]_{2}=(0^{m-1}1)^{\ell_{2}/m}0^{t_{2}}(0^{m-1}1)^{\ell_{1}/m}0^{t_{1}}. |  |

We can continue this argument if [n] 2 [n]_{2} has more than two runs of 1 1 ’s and we find T m ​ ( n) T_{m}(n) is non-zero only when

 | [n] 2 = 1 ℓ s 0 t s ⋯ 1 ℓ 1 0 t 1, t s ≥ 1, …, t 2 ≥ 1, t 1 ≥ 0, [n]_{2}=1^{\ell_{s}}0^{t_{s}}\cdots 1^{\ell_{1}}0^{t_{1}},\quad t_{s}\geq 1,\ldots,t_{2}\geq 1,t_{1}\geq 0, |  |

for some s s, and ℓ i ≡ 0 ( mod m) \ell_{i}\equiv 0\pmod{m} for i = 1, …, s i=1,\ldots,s. Furthermore, for such n n, we have T m ​ ( n) = 1 T_{m}(n)=1, since the only k k that contributes a non-zero value to the sum defining T m ​ ( n) T_{m}(n) has the form

 | [k] 2 = ( 0 m − 1 1) ℓ s / m 0 t s ⋯ ( 0 m − 1 1) ℓ 1 / m 0 t 1. [k]_{2}=(0^{m-1}1)^{\ell_{s}/m}0^{t_{s}}\cdots(0^{m-1}1)^{\ell_{1}/m}0^{t_{1}}. |  |

∎

The sequence T 2 T_{2} can be viewed as a variant of the *Baum–Sweet sequence*(OEIS A086747) [2], which is the sequence ( B ​ S ​ ( n)) n ≥ 0 (BS(n))_{n\geq 0} defined by

 | B ​ S ​ ( n) = { 1 if each run of 0’s in ​ [n] 2 ​ has even length; 0 otherwise. BS(n)=\begin{cases}1&\text{if each run of 0's in }[n]_{2}\text{ has even length};\\ 0&\text{otherwise}.\end{cases} |  |

In general then, the family of sequences T m T_{m} could perhaps be taken as a family of *generalized Baum–Sweet sequences*.

## References

- [1] J.-P. Allouche and J. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cambridge, 2003.
- [2] L. Baum, M. Sweet, Continued fractions of algebraic power series in characteristic 2, Annals of Mathematics 103 (1976), 593–610.
- [3] J. Berstel and C. Reutenauer, Noncommutative Rational Series with Applications, Cambridge, 2011.
- [4] J. Shallit, The Logical Approach To Automatic Sequences: Exploring Combinatorics on Words with Walnut, Cambridge, 2022.
- [5] N. J. A. Sloane, On the number of ON cells in cellular automata, in S. Butler, J. Cooper, and G. Hurlbert, editors, Connections in Discrete Mathematics: A Celebration of the Work of Ron Graham, Cambridge, 2018, 13–38.
- [6] C. W. Wu, Sums of products of binomial coefficients mod 2 2 and run length transforms of sequences, INTEGERS 22 (2022), Article #A81. Available online at http://math.colgate.edu/~integers/w81/w81.pdf.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
