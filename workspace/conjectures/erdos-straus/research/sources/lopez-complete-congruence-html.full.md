<!-- source: https://arxiv.org/html/2404.01508v3 | converted from HTML -->

A Complete Congruence System for the Erdos-Straus Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2404.01508v3 [math.NT] 15 Apr 2024

# A Complete Congruence System for the Erdos-Straus Conjecture

Miguel Angel Lopez

###### Abstract

Abstract: In this paper we attack the Erdos-Straus conjecture by means of the structure of its solutions, extending and improving the results of a previous paper. Using previous results and supported by the works of Elsholtz and Tao and Monks and Velingker we define a system of congruences for which there are always solutions to the Erdos-Straus conjecture and which we conjecture to include all prime numbers. For this purpose, and always taking into account a result due to Mordell that limits the congruences admitting polynomial identities to those that are not quadratic residues, we will adopt a transversal approach and classify the solutions by their form and not by those congruences that produce them. Thus we define two new types of solutions, which we call Type A and B, and relate them to the already known Type II solutions and study their properties. Finally we conjecture that every prime number has at least one solution of Type A or B and we associate a congruence and a general polynomial to each Type of solution.

email: migulo23@ucm.es, dagon.magnus@gmail.com

Keywords: Erdos-Straus, diophantine equation, unit fraction, egyptian fraction, congruences, integral solution, prime numbers, quadratic residues

Mathematics Subject Classification: 11D72, 11A07, 11A41

## 1 Introduction

In 1948, Paul Erdös and Ernst G. Straus formulated a conjecture that states the following: the equation

 | 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  |

has at least one solution where x, x, y, y, and z z are positive integers. There are many modular identities that solve this equation, for example for the case n ≡ 2 ( mod 3) n\equiv 2\pmod{3} we can use the following expression:

 | 4 n = 1 n + 1 ( n + 1) / 3 + 1 n ⁡ ( n + 1) / 3 \frac{4}{n}=\frac{1}{n}+\frac{1}{(n+1)/3}+\frac{1}{n(n+1)/3} |  |

L. J. Mordell studied this equation among many others in [1] and derived identities for the cases p ≡ 3 ( mod 4) p\equiv 3\pmod{4}, 2 2 or 3 ( mod 5) 3\pmod{5}, 5 or 6 ( mod 7) 6\pmod{7} and 5 ( mod 8) 5\pmod{8}. These combined identities solve all cases except those where p p is congruent to 1, 121, 169, 289, 361 or 529 ( mod 840) 529\pmod{840}. Mordell himself wondered whether it might not be possible to find a sufficient number of identities such that all possible cases would be completely covered. This possibility was limited, however, by his discovery that if an identity exists for a set of values p ≡ r ( mod q) p\equiv r\pmod{q} then r r cannot be a quadratic residue module q q. For example, no such identity can exist for values of p p congruent to 1 ( mod q) 1\pmod{q} since 1 is always a quadratic residue module q q for any natural value of q q. This implies, in fact, that it is not possible to find a value q q such that identities can be found for all elements of ℤ q \mathbb{Z}_{q}.

The conjecture has been verified up to value 10 7 10^{7} by Yamamoto [2] and 10 14 10^{14} by Swett [3]. Webb and others have shown that the natural density of possible counterexamples to the conjecture is zero, for as N N tends to infinity, the number of values in the interval [1, N] [1,N] that could be counterexamples tends to zero.

In [4] we showed that, if p = 4 ​ k + 1 p=4k+1, there exists a solution for p p such that

 | 4 p = 1 d ​ u + 1 d ​ v + 1 d ​ u ​ v \frac{4}{p}=\frac{1}{du}+\frac{1}{dv}+\frac{1}{duv} |  |

if and only if there exists t ≥ 0 t\geq 0 and a divisor w w of k + 1 + t k+1+t such that w ≡ − 1 ( mod 3 + 4 ​ t) w\equiv-1\pmod{3+4t}. In particular, if there exists a divisor w w of k + 1 k+1 congruent to 2 module 3, p p has the previously mentioned solution. This result is powerful even in the particular case where t = 0 t=0 and in fact only by employing this particular case all cases are ruled out except those where p ≡ 1 ( mod 24) p\equiv 1\pmod{24} and also works in many other cases within this congruence. That the problem cannot be solved completely with this result is logical not only because, as Mordell rightly points out, 1 is quadratic residue modulo 24, but also because this congruence contains the perfect square of every prime number greater than 3, with repercussions that we will explain later.

## 2 Main body

As in the previous article, we will establish a similar notation. We will consider the values of each possible solution in an increasing order, i.e. x ≤ y ≤ z x\leq y\leq z. We will write a solution for each value a ∈ ℕ a\in\mathbb{N} as what will allow us to list them in a more condensed form. We will use the following definition:

###### Definition 1.

We say that a number a ∈ ℕ a\in\mathbb{N} is Egyptian of order 3 if there exists a triplet of the form ( x, y, z) (x,y,z) such that the Erdos-Straus conjecture is fulfilled for the fraction 4 a \frac{4}{a}.

We will also use the following definition, used by Bradford in [5] and by Elsholtz and Tao in [6]:

###### Definition 2.

We will say that a solution ( x, y, z) (x,y,z) is of Type I if g ​ c ​ d ​ ( a, x) = g ​ c ​ d ​ ( a, y) = 1 gcd(a,x)=gcd(a,y)=1 and g ​ c ​ d ​ ( a, z) = a gcd(a,z)=a while a solution will be of Type II if g ​ c ​ d ​ ( a, y) = g ​ c ​ d ​ ( a, z) = a gcd(a,y)=gcd(a,z)=a and g ​ c ​ d ​ ( a, x) = 1 gcd(a,x)=1.

It is well known that prime numbers can only have these two types of solutions. We will also point out that, contrary to the previous article, in some cases we will consider the value a to be studied as a composite, and when it is prime we will use the letter p p. We will begin by recalling the result of the previous article that motivates the new approach to the conjecture, and it is the following.

###### Theorem 1.

Let be p ∈ ℕ p\in\mathbb{N} prime. Suppose that p = 4 ​ k + 1 p=4k+1, there exists a solution for p p with the form ( d ​ u, d ​ v, d ​ u ​ v) (du,dv,duv) with d, u, v ∈ ℕ d,u,v\in\mathbb{N} if and only if there exists t ≥ 0 t\geq 0 and a divisor w w of k + 1 + t k+1+t such that w ≡ − 1 ( mod 3 + 4 ​ t) w\equiv-1\pmod{3+4t}. In particular, if there exists a divisor w w of k + 1 k+1 congruent to 2 module 3, p p is Egyptian of order 3 with a solution of the form ( d ​ u, d ​ v, d ​ u ​ v) (du,dv,duv).

We will not prove this result, for anyone interested in seeing its proof may consult [4]. The proof is also constructive in an implicit way; following its steps, it follows that

 | d = k + 1 + t w, n = w + 1 3 + 4 ​ t, u = 1 + n ​ p 4 ​ d ​ n − 1, v = n ​ p d=\frac{k+1+t}{w},n=\frac{w+1}{3+4t},u=\frac{1+np}{4dn-1},v=np |  |

All these numbers are natural in a trivial way, without more than applying the hypotheses, except in the case of u u, for which it is simple to verify it by substituting the values to arrive at 1 + n ​ p ≡ 0 ( mod 4 ​ d ​ n − 1) 1+np\equiv 0\pmod{4dn-1}. It can be verified easily also that 4 p = 1 d ​ u + 1 d ​ v + 1 d ​ u ​ v \frac{4}{p}=\frac{1}{du}+\frac{1}{dv}+\frac{1}{duv} because it is a mere algebraic exercise.

It is also evident, without more than performing a modular arithmetic calculation that, for the case t = 0 t=0, if k + 1 k+1 has a divisor w w congruent to 2 modulo 3, then either w w itself is a prime number or there exists another divisor of k + 1 k+1 congruent to 2 modulo 3 that is, so we can restrict our search for valid w w divisors strictly to prime candidates.

As a result of the proof, in addition, the paper proved that for any value of t t it is satisfied that g ​ c ​ d ​ ( u, v) = 1 gcd(u,v)=1. We can also come to a quick conclusion as to whether it is one of the basic types of solution.

###### Theorem 2.

Let be p ∈ ℕ p\in\mathbb{N} prime of the form p = 4 ​ k + 1 p=4k+1, if p p has a solution ( d ​ u, d ​ v, d ​ u ​ v) (du,dv,duv), satisfies that this solution is of Type II.

###### Proof.

Suppose without loss of generality that u ≤ v u\leq v. Monks and Velingker prove in [7] that necessarily, since d ​ u ≤ d ​ v du\leq dv, p p does not divide d ​ u du. Since we know that

 | 4 p = 1 d ​ u + 1 d ​ v + 1 d ​ u ​ v \frac{4}{p}=\frac{1}{du}+\frac{1}{dv}+\frac{1}{duv} |  |

and therefore,

 | 4 ​ d ​ u ​ v = p ⁡ ( 1 + u + v) 4duv=p(1+u+v) |  |

we have then that p | 4 ​ v p\mid 4v, and since p p is always odd, being of the form p = 4 ​ k + 1 p=4k+1, then p | v p\mid v. This automatically implies that the solution ( d ​ u, d ​ v, d ​ u ​ v) (du,dv,duv) is of Type II. ∎

This reasoning can be replicated without variations for the case p = 4 ​ k + 3 p=4k+3 and it is trivial to observe that the condition is also fulfilled for the only solution of the case p = 2 p=2. The first limitation regarding this solution is that it can never be assumed with these same properties for any value that lacks Type II solutions, and such values, as Elsholtz and Tao already commented, exist.

At this point, we will name these types of solutions.

###### Definition 3.

We say that a value a ∈ ℕ a\in\mathbb{N} has a solution of Type A if there exist d, u, v ∈ ℕ d,u,v\in\mathbb{N} such that a a is Egyptian of order 3 with a solution ( d ​ u, d ​ v, d ​ u ​ v) (du,dv,duv). This solution is of Type II if a a is prime.

In the previous article it was shown that any prime number p p such that p ≢ 1 ( mod 24) p\not\equiv 1\pmod{24} always has a solution of Type A. For this, it was sufficient to use ( 1) and the particular case where t = 0 t=0. It is possible to keep digging in this direction until one finds huge lists of congruences with Type A solutions associated, since it has not even been used in particular cases other than the value of t = 0 t=0. There are many papers that develop large numbers of identities, but that approach has many limitations. It is interesting to note that the congruence p ≡ 1 ( mod 24) p\equiv 1\pmod{24} includes the values 25,49,121,169,289…All of them are perfect squares, which is no coincidence.

###### Theorem 3.

Let n n be odd such that n ≥ 5 n\geq 5, 3 ∤ n 3\nmid n.Then n 2 ≡ 1 ( mod 24) n^{2}\equiv 1\pmod{24}. In particular, the square of every prime number greater than 3 belongs to this congruence.

###### Proof.

We consider the value n 2 − 1 = ( n − 1) ​ ( n + 1) n^{2}-1=(n-1)(n+1). Since n n is odd, we know that n ≡ 1, 3 ( mod 4) n\equiv 1,3\pmod{4}. If n ≡ 1 ( mod 4) n\equiv 1\pmod{4} then n + 1 ≡ 2 ( mod 4) n+1\equiv 2\pmod{4} and n − 1 ≡ 0 ( mod 4) n-1\equiv 0\pmod{4}, which instantly implies that n 2 ≡ 1 ( mod 8) n^{2}\equiv 1\pmod{8}. If n ≡ 3 ( mod 4) n\equiv 3\pmod{4} we reach the same conclusion by analogous reasoning. On the other hand, since 3 ∤ n 3\nmid n we have that n ≡ 1, 2 ( mod 3) n\equiv 1,2\pmod{3}. If n ≡ 1 ( mod 3) n\equiv 1\pmod{3} then n − 1 ≡ 0 ( mod 3) n-1\equiv 0\pmod{3} and therefore n 2 − 1 ≡ 0 ( mod 3) n^{2}-1\equiv 0\pmod{3}. Likewise, if n ≡ 2 ( mod 3) n\equiv 2\pmod{3} then n + 1 ≡ 0 ( mod 3) n+1\equiv 0\pmod{3} and therefore n 2 − 1 ≡ 0 ( mod 3) n^{2}-1\equiv 0\pmod{3}. In both cases n 2 ≡ 1 ( mod 3) n^{2}\equiv 1\pmod{3}. Thanks to the Chinese Remainder Theorem we finally have that n 2 ≡ 1 ( mod 24) n^{2}\equiv 1\pmod{24}. ∎

This result we have just proved extends an earlier classical one by Conway and Guy published in [8] that said that the square of every odd number is congruent to 1 modulo 8. The fact that this happens imposes limits on what can be achieved with Type I and II solutions, as Schinzel and Yamamoto point out, since they proved that the square of every natural number lacks both Type I and Type II solutions. For a modern proof, see [6].

Solutions of Type A are transversal to the identity of prime and composite; both types of numbers can possess a solution with such a structure. If a prime number p p possesses a solution of the form ( d ​ u, d ​ v, d ​ u ​ v) (du,dv,duv) then every multiple m ​ p mp with m > 1 m>1 possesses a solution of the form ( m ​ d ​ u, m ​ d ​ v, m ​ d ​ u ​ v) (mdu,mdv,mduv) which still possesses the structure ( D ​ u, D ​ v, D ​ u ​ v) (Du,Dv,Duv) with D = m ​ d D=md. The main difference lies in the fact that, while the first solution is necessarily of Type II, the second does not belong to that type since g ​ c ​ d ​ ( m ​ p, D ​ u) ≥ m gcd(mp,Du)\geq m.

It is also immediate to verify that, if we try to expand ( 1) for composite values a a of the form a = 4 ​ k + 1 a=4k+1, then the implication from right to left is immediately fulfilled (it is enough to take d = k + 1 + t w d=\frac{k+1+t}{w}, n = w + 1 3 + 4 ​ t n=\frac{w+1}{3+4t}, u = 1 + n ​ p 4 ​ d ​ n − 1 u=\frac{1+np}{4dn-1}, v = n ​ p v=np, as we said before), while the opposite implication is false, for which it is enough to look for example at the value a = 25 a=25, that has solutions of Type A but for which there is no t ≥ 0 t\geq 0 such that 6 + 1 + t 6+1+t has a divisor w w such that w ≡ − 1 ( mod 3 + 4 ​ t) w\equiv-1\pmod{3+4t}. These solutions can never be of Type II for this value, being 25 a perfect square.

If a thorough analysis of prime numbers is performed, it can be seen that, among the first 9000 natural numbers, the only prime numbers lacking Type A solutions are 193 and 2521. In many articles these values suddenly appear as numbers that offer various types of problems or resist classification, as for example [9]. These two numbers, however, have a second common structure of the form d ⁡ ( u ​ v, u ​ p, v ​ p) d(uv,up,vp). Both numbers possess solutions of this type; 193 has e.g.

 | ( 50, 1930, 4825) = 5 ​ ( 10, 2 ⋅ 193, 5 ⋅ 193) (50,1930,4825)=5(10,2\cdot 193,5\cdot 193) |  |

and for 2521 we have the tern

 | ( 638, 55462, 804199) = 11 ​ ( 58, 2 ⋅ 2521, 29 ⋅ 2521) (638,55462,804199)=11(58,2\cdot 2521,29\cdot 2521) |  |

This will be our second structure to analyze.

###### Definition 4.

We say that a value a ∈ ℕ a\in\mathbb{N} has a solution of Type B if there exist d, u, v ∈ ℕ d,u,v\in\mathbb{N} such that a a is Egyptian of order 3 with a solution ( d ​ u ​ v, d ​ u ​ a, d ​ v ​ a) (duv,dua,dva).

First, let us characterize in a simple way what a prime number must fulfill to possess a solution of this type, and we will find an interesting parallelism with the previous case.

###### Theorem 4.

Let be p ∈ ℕ p\in\mathbb{N} prime, let d ∈ ℕ d\in\mathbb{N}. There exists a Type B solution for p p if and only if it exists n ∈ ℕ n\in\mathbb{N} such that p ≡ − n ( mod 4 ​ d ​ n − 1) p\equiv-n\pmod{4dn-1}. In addition this solution is of Type II.

###### Proof.

First we will prove the implication from left to right. We have a solution that satisfies the equation

 | 4 p = 1 d ​ u ​ v + 1 d ​ u ​ p + 1 d ​ v ​ p \frac{4}{p}=\frac{1}{duv}+\frac{1}{dup}+\frac{1}{dvp} |  |

and which we can rewrite as

 | 4 ​ d ​ u ​ v = p + u + v 4duv=p+u+v |  |

This implies that

 | u = p + v 4 ​ d ​ v − 1 u=\frac{p+v}{4dv-1} |  |

and this number will only be natural if 4 ​ d ​ v − 1 | p + v 4dv-1\mid p+v or, what is the same thing, there exists a certain n ∈ ℕ n\in\mathbb{N} such that

 | p + n ≡ 0 ( mod 4 ​ d ​ n − 1) p+n\equiv 0\pmod{4dn-1} |  |

To prove the converse implication, let n ∈ ℕ n\in\mathbb{N} be such that the above congruence is satisfied for a certain value d ∈ ℕ d\in\mathbb{N}. We define u = p + n 4 ​ d ​ n − 1 u=\frac{p+n}{4dn-1}, v = n v=n. Both numbers are natural and it’s straigthforward to prove that

 | 4 p = 1 d ​ u ​ v + 1 d ​ u ​ p + 1 d ​ v ​ p \frac{4}{p}=\frac{1}{duv}+\frac{1}{dup}+\frac{1}{dvp} |  |

Moreover, it always happens that g ​ c ​ d ​ ( p, d ​ u ​ v) = 1 gcd(p,duv)=1, otherwise p 2 p^{2} would be divisor of at least one of the three coordinates of the solution and such a thing is impossible, as demonstrated by Monks and Velingker in [7]. That classifies these solutions again in the Type II category, which was the last thing we wanted to prove. ∎

An immediate and very interesting conclusion is that this characterization does not use the fact that p p is a prime number, but it is necessary to consider it to demonstrate that this solution is of Type II, since there are composite numbers that have solutions of Type B but are not of Type II, for example n = 6 n=6. On the other hand there are also composite numbers that do not have solutions of this type, for example n = 15 n=15. As a joint conclusion, we have that all the solutions of Type A and B are in particular of Type II when they are referred to a prime number.

Again, Type B solutions are transversal to the identity of prime and composite; both types of numbers can possess a solution with such a structure. However, unlike the previous case, if a prime number p p has a solution of the form d ⁡ ( u ​ v, u ​ p, v ​ p) d(uv,up,vp) this does not imply that every multiple m ​ p mp with m > 1 m>1 has a solution of the form d ​ m ​ ( u ​ v, u ​ p, v ​ p) dm(uv,up,vp).

As we have already mentioned above, perfect squares can never have solutions of Type I or II. This implies, first of all, that if a perfect square a a has a Type A solution, this solution cannot be of Type II and, therefore, must be inherited from one of its divisors.

On the other hand, a stronger conclusion is the following:

###### Theorem 5.

A perfect square s s can never have a Type B solution,, whether or not it is of Type II.

###### Proof.

If it does, then using ( 4) we have that there exist d, n ∈ ℕ d,n\in\mathbb{N} such that

 | s ≡ − n ( mod 4 ​ d ​ n − 1) s\equiv-n\pmod{4dn-1} |  |

and therefore, following the steps of the theorem, we construct the identity

 | 4 s = 1 d ​ n ​ s + n 4 ​ d ​ n − 1 + 1 s ​ d ​ s + n 4 ​ d ​ n − 1 + 1 s ​ d ​ n \frac{4}{s}=\frac{1}{dn\frac{s+n}{4dn-1}}+\frac{1}{sd\frac{s+n}{4dn-1}}+\frac{1}{sdn} |  |

This identity is of the form

 | 4 s = 1 P d, n ​ ( s) + 1 Q d, n ​ ( s) + 1 R d, n ​ ( s) \frac{4}{s}=\frac{1}{P_{d,n}(s)}+\frac{1}{Q_{d,n}(s)}+\frac{1}{R_{d,n}(s)} |  |

where all these functions are polynomial in the variable s s, and Mordell proved that, then, − n -n cannot be a quadratic residue module 4 ​ d ​ n − 1 4dn-1, but it is, since s s is a perfect square, and this is a contradiction. Therefore no perfect square ever possesses a Type B solution. ∎

Another immediate conclusion is the following:

###### Corollary 1.

Let d, n ∈ ℕ d,n\in\mathbb{N}, then ( − n 4 ​ d ​ n − 1) = − 1 \left(\frac{-n}{4dn-1}\right)=-1 with ( a b) \left(\frac{a}{b}\right) equal to the Jacobi symbol. In particular if 4 ​ d ​ n − 1 4dn-1 is prime then ( n 4 ​ d ​ n − 1) = 1 \left(\frac{n}{4dn-1}\right)=1 and n n is always quadratic residue module 4 ​ d ​ n − 1 4dn-1 (but may or may not be if 4 ​ d ​ n − 1 4dn-1 is a composite number).

We can also characterize the Type B solutions for the particular case of prime numbers p = 4 ​ k + 1 p=4k+1.

###### Theorem 6.

Let be p ∈ ℕ p\in\mathbb{N} prime. Suppose that p = 4 ​ k + 1 p=4k+1, there exists a solution for p p with the form ( d ​ u ​ v, d ​ u ​ p, d ​ v ​ p) (duv,dup,dvp) with d, u, v ∈ ℕ d,u,v\in\mathbb{N} if and only if there exists t ≥ 0 t\geq 0 and two positive divisors a, b a,b of k + 1 + t k+1+t such that a + b = 3 + 4 ​ t a+b=3+4t.

###### Proof.

We suppose first that p p has a Type B solution, then exists d, n ∈ ℕ d,n\in\mathbb{N} such that

 | p ≡ − n ( mod 4 ​ d ​ n − 1) p\equiv-n\pmod{4dn-1} |  |

then

 | 4 ​ k ≡ − n − 1 ( mod 4 ​ d ​ n − 1) 4k\equiv-n-1\pmod{4dn-1} |  |

and we can deduce that

 | k ≡ − d ​ n 2 − d ​ n ( mod 4 ​ d ​ n − 1) k\equiv-dn^{2}-dn\pmod{4dn-1} |  |

This implies that exists c ∈ ℤ c\in\mathbb{Z} with k + d ​ n 2 + d ​ n = c ⁡ ( 4 ​ d ​ n − 1) k+dn^{2}+dn=c(4dn-1). We can also suppose that c c is natural because 4 ​ d ​ n − 1 4dn-1 and k + d ​ n 2 + d ​ n ∈ ℕ k+dn^{2}+dn\in\mathbb{N}. If we reorder the expression, we have that

 | k + c = d ​ n ​ ( 4 ​ c − 1 − n) k+c=dn(4c-1-n) |  |

We define c = t + 1 c=t+1, t ≥ 0 t\geq 0, so k + 1 + t = d ​ n ​ ( 3 + 4 ​ t − n) k+1+t=dn(3+4t-n). We define a = n a=n, b = 3 + 4 ​ t − n b=3+4t-n.We have trivially then that a, b ∈ ℕ a,b\in\mathbb{N}, a ​ b | k + 1 + t ab\mid k+1+t, a + b = 3 + 4 ​ t a+b=3+4t.

Conversely, lets suppose that ∃ a, b ∈ ℕ \exists a,b\in\mathbb{N}, t ≥ 0 t\geq 0 such that a ​ b | k + 1 + t ab\mid k+1+t, a + b = 3 + 4 ​ t a+b=3+4t. We can reverse all the process defining a = n a=n, b = 3 + 4 ​ t − a b=3+4t-a. We define

 | z = n ⁡ ( 3 + 4 ​ t − n) = a ​ b z=n(3+4t-n)=ab |  |

then

 | k + 1 + t = d ​ z, d ∈ ℕ k+1+t=dz,d\in\mathbb{N} |  |

and therefore

 | k + 1 + t = 3 ​ d ​ n + 4 ​ d ​ n ​ t − d ​ n 2 k+1+t=3dn+4dnt-dn^{2} |  |

We define t = c − 1 t=c-1, c ≥ 1 c\geq 1 because t ≥ 0 t\geq 0. Then k + c = 4 ​ d ​ n ​ c − d ​ n − d ​ n 2 k+c=4dnc-dn-dn^{2} and rearranging we arrive to k + d ​ n + d ​ n 2 = c ⁡ ( 4 ​ d ​ n − 1) k+dn+dn^{2}=c(4dn-1), c ≥ 1 c\geq 1. It is straightforward then that

 | k ≡ − d ​ n − d ​ n 2 ( mod 4 ​ d ​ n − 1) k\equiv-dn-dn^{2}\pmod{4dn-1} |  |

and this implies automatically that there are d, n ∈ ℕ d,n\in\mathbb{N} such that p ≡ − n ( mod 4 ​ d ​ n − 1) p\equiv-n\pmod{4dn-1} and therefore p p has a Type B solution. ∎

###### Corollary 2.

The theorem also holds if p = 4 ​ k + 1 p=4k+1 but it’s not prime (we never use the primality of p p in the demonstration).

In our previous paper, to obtain the characterization of ( 1), we employed the following prior result, whose proof, similar to ( 4) but more complex in some steps, can be read in [4].

###### Theorem 7.

Let be p ∈ ℕ p\in\mathbb{N} prime. There exists a Type A solution for p p if and only if it exists d, n ∈ ℕ d,n\in\mathbb{N} such that p ≡ − 4 ​ d ( mod 4 ​ d ​ n − 1) p\equiv-4d\pmod{4dn-1}. In addition the values u u and v v are coprime and the solution is of Type II.

Experimental evidence shows that every prime number always has at least one solution with one of these two types of structure. This leads us to formulate what is the main conjecture of this article:

###### Conjecture 1.

Let be p ∈ ℕ p\in\mathbb{N} prime, then exists d, n ∈ ℕ d,n\in\mathbb{N} such that p ≡ − 4 ​ d ( mod 4 ​ d ​ n − 1) p\equiv-4d\pmod{4dn-1} or p ≡ − n ( mod 4 ​ d ​ n − 1) p\equiv-n\pmod{4dn-1}. If this result is true, then this congruence system covers all primes and the Erdos-Straus conjecture is true.

It is very interesting to note that there is a modular relationship between the type − n -n and type − 4 ​ d -4d values, since both sets of divisors are mutual inverses in ℤ 4 ​ d ​ n − 1 \mathbb{Z}_{4dn-1}.

The conjecture has been experimentally verified and is true for any prime number less than or equal to 104729, that is, it has been verified for the first 10000 prime numbers. Minor cases like p = 2 p=2 or p = 3 p=3 also satisfy the conjecture. The number of solutions does not have a regular growth pattern: a value as large as 83449 not only lacks Type B solutions, but also has only two Type A solutions that are at the same time of Type II (and they are, since 83449 is a prime number, the only two of this type that it has, since it cannot inherit others from any factor).

Both types of structure are necessary for the conjecture to be true: as previously mentioned, 193 and 2521 do not have Type A solutions but do have Type B solutions, and these are not isolated cases, since, for example, 66529 is another case. On the contrary, 23929 does not have Type B solutions but it does have Type A solutions. Both types of solutions, therefore, complement each other.

It may be asked whether it is possible to choose d, n ∈ ℕ d,n\in\mathbb{N} such that 4 ​ d ​ n − 1 4dn-1 is always a prime number. While such a thing is possible for a huge number of cases of p p, it is not possible to do so in general, and a significant example is, again, the case p = 2521 p=2521. This number has only one Type B solution which has two 4 ​ d ​ n − 1 4dn-1 associated values, which are 87 and 1275, neither of which is a prime number. 2521 does, in fact, satisfy a property that may perhaps explain in part why it is so elusive: all values from 1 to 10 are quadratic residues in ℤ 2521 \mathbb{Z}_{2521}. In fact, all prime numbers congruent to 1 module 840 fulfill it, precisely one of the congruences that resisted Mordell when studying the conjecture and one of the most resistant to being categorized, perhaps in part because of this special property.

Elsholtz and Tao relate in [6] the Type II solutions to six-coordinate vectors ( a, b, c, d, e, f) ∈ ℂ 6 (a,b,c,d,e,f)\in\mathbb{C}^{6} satisfying a system of equations. They call the set of all these values Σ n π \Sigma_{n}^{\pi} and define an application Π n π \Pi_{n}^{\pi} between this set and the algebraic surface S n = { ( x, y, z) ∈ ℂ 3: 4 ​ x ​ y ​ z = n ​ y ​ z + n ​ x ​ z + n ​ x ​ y } S_{n}=\{{(x,y,z)\in\mathbb{C}^{3}:4xyz=nyz+nxz+nxy}\} as follows:

 | Π n π ​ ( a, b, c, d, e, f) = ( a ​ b ​ d, a ​ c ​ d ​ n, b ​ c ​ d ​ n) \Pi_{n}^{\pi}(a,b,c,d,e,f)=(abd,acdn,bcdn) |  |

These solutions are not just Type II, but a ​ b ​ d abd must be required to be coprime with n n. This condition becomes automatic when n n is a prime number, but is not held in general.

It can be immediately observed that Type A solutions, with their values ordered in any possible way, are given when a = 1 a=1 or b = 1 b=1 with the identification u = b u=b, v = c ​ n v=cn in the case a = 1 a=1 and analogously when b = 1 b=1. When c = 1 c=1 we obtain, precisely, the Type B solutions, performing this time the automatic identification u = a u=a, v = b v=b. This fact suggests that these two forms of solutions are canonically relevant, being obtained by substituting for the smallest natural values for each of the three main parameters of the Type II solutions. Also, if we allow d = 1 d=1, we will obtain a very relevant result, as we will see later.

The conjecture concerning the existence or non-existence of solutions of Type A and B can be studied under a purely polynomial point of view, associating to each type of solution an algebraic expression, as can be seen in the following theorem.

###### Theorem 8.

Let p p be prime congruent to 1 modulo 4, we define the following polynomials for x, y, z, t ∈ ℕ x,y,z,t\in\mathbb{N}:

- •

P ⁡ ( x, y, t) = ( 4 ​ x ​ y − 1) ​ ( 3 + 4 ​ t) − 4 ​ x 2 ​ y P(x,y,t)=(4xy-1)(3+4t)-4x^{2}y, x, y, t ≥ 0 x,y,t\geq 0

- •

Q ⁡ ( x, y, t) = ( 4 ​ x ​ y − 1) ​ ( 3 + 4 ​ t) − 4 ​ y Q(x,y,t)=(4xy-1)(3+4t)-4y, x, y, t ≥ 0 x,y,t\geq 0

- •

R ⁡ ( x, y, t, z) = ( 4 ​ x ​ y ​ z − 1) ​ ( 3 + 4 ​ t) − 4 ​ x 2 ​ y R(x,y,t,z)=(4xyz-1)(3+4t)-4x^{2}y, x, y, z, t ≥ 0 x,y,z,t\geq 0

1. (i)

If p = P ⁡ ( x, y, t) p=P(x,y,t) then p p has a Type B solution.

2. (ii)

If p = Q ⁡ ( x, y, t) p=Q(x,y,t) then p p has a Type A solution.

3. (iii)

If p = R ⁡ ( x, y, t) p=R(x,y,t) then p p has a Type II solution.

All the implications, moreover, also hold conversely: if p p possesses a solution of any of the above types, then it necessarily belongs to the image of the corresponding polynomial.

###### Proof.

It is immediate to check, first, that the image of the three polynomials when their variables take natural values are always numbers congruent to 1 modulo 4. Now, we start with (i). We know that

 | p ≡ − x ( mod 4 ​ x ​ y − 1) p\equiv-x\pmod{4xy-1} |  |

which is equivalent by ( 4) to having a Type B solution. Now we consider p = 4 ​ k + 1 p=4k+1 with a Type B solution, by ( 6) we know that there exists a, b a,b divisors of k + 1 + t k+1+t such that a + b = 3 + 4 ​ t a+b=3+4t. We rename a = x a=x, b = 3 + 4 ​ t − x b=3+4t-x, then exists a certain y y such that

 | k + 1 + t = x ​ y ​ ( 3 + 4 ​ t − x) k+1+t=xy(3+4t-x) |  |

and then, with elementary algebra,

 | p = 4 ​ k + 1 = ( 4 ​ x ​ y − 1) ​ ( 3 + 4 ​ t) − 4 ​ x 2 ​ y p=4k+1=(4xy-1)(3+4t)-4x^{2}y |  |

To prove (ii), if we define p = ( 4 ​ x ​ y − 1) ​ ( 3 + 4 ​ t) − 4 ​ y p=(4xy-1)(3+4t)-4y, it is immediate to prove that

 | p ≡ − 4 ​ y ( mod 4 ​ x ​ y − 1) p\equiv-4y\pmod{4xy-1} |  |

which by ( 7) implies that if p p is prime, then it has a Type A solution. To prove the opposite, we consider that p = 4 ​ k + 1 p=4k+1 has a solution of Type A, then by ( 1) there exists a divisor w w of k + 1 + t k+1+t such that w w is congruent to − 1 -1 modulus 3 + 4 ​ t 3+4t. This implies that w + 1 = c ⁡ ( 3 + 4 ​ t) w+1=c(3+4t) for a certain c ≥ 1 c\geq 1, and therefore there exists a certain natural number e e such that k + 1 + t = e ​ w = e ⁡ ( c ⁡ ( 3 + 4 ​ t) − 1) k+1+t=ew=e(c(3+4t)-1). Rearranging we arrive at

 | k + 1 + t = c ​ e ​ ( 3 + 4 ​ t) − e k+1+t=ce(3+4t)-e |  |

which implies that

 | p = 4 ​ k + 1 = ( 4 ​ c ​ e − 1) ​ ( 3 + 4 ​ t) − 4 ​ e p=4k+1=(4ce-1)(3+4t)-4e |  |

By renaming x = c x=c, y = e y=e,we already have it.

To prove (iii) we rely on a classic result of Mordell, which can be read for example in [1], which says that a value n n has a Type II solution if and only if there exist natural values a, b, c, d a,b,c,d such that they satisfy

 | ( 4 ​ a ​ b ​ c ​ d − 1) ​ d = a ​ n + b (4abcd-1)d=an+b |  |

By clearing we obtain that

 | n = 4 ​ b ​ c ​ d − d + b a n=4bcd-\frac{d+b}{a} |  |

which will be a natural number if and only if there exists a certain w w such that d + b = a ​ w d+b=aw. By making the change of variable d = a ​ w − b d=aw-b we get that

 | n = 4 ​ a ​ b ​ c ​ ( a ​ w − b) − w n=4abc(aw-b)-w |  |

and this number can only be congruent to 1 modulo 4 if w w is congruent to 3 modulo 4 or, what is the same, there exists a certain positive value s s for which w = 3 + 4 ​ s w=3+4s. By making a new change of variable we get that

 | n = 4 ​ a ​ b ​ c ​ ( a ⁡ ( 3 + 4 ​ s) − b) − ( 3 + 4 ​ s) n=4abc(a(3+4s)-b)-(3+4s) |  |

which, renaming the variables and with some easy manipulations, leads us to the polynomial R ⁡ ( x, y, z, t) R(x,y,z,t) we were looking for. The whole procedure is immediately reversible so that the implication works both ways. ∎

###### Remark 1.

It is immediate to check that

- •

R ⁡ ( x, y, t, 1) = P ⁡ ( x, y, t) R(x,y,t,1)=P(x,y,t)

- •

R ⁡ ( 1, y, t, x) = Q ⁡ ( x, y, t) R(1,y,t,x)=Q(x,y,t)

###### Remark 2.

A p-value has a solution that is both of Type A and B in the particular case in which x = 1 x=1; in that case P ⁡ ( x, y, t) = Q ⁡ ( x, y, t) P(x,y,t)=Q(x,y,t) and, therefore, 0 = P ⁡ ( x, y, t) − Q ⁡ ( x, y, t) = 4 ​ y ​ ( x + 1) ​ ( x − 1) 0=P(x,y,t)-Q(x,y,t)=4y(x+1)(x-1), that can only happen when x = 1 x=1. Below we offer an alternative way of characterizing these solutions that are both of Type A and B.

We mention now some general statements of Type A and B solutions concerning bounds for d d and other simple properties.

###### Proposition 1.

Let p p be a prime number congruent to 1 module 4. If p p has a solution of Type A then d ≤ ⌊ p + 3 8 ⌋ d\leq\lfloor\frac{p+3}{8}\rfloor. This bound is also optimal.

###### Proof.

By ( 1), we know that if p p has a solution of Type A then there exists t > 0 t>0 and w ≡ − 1 ( mod 3 + 4 ​ t) w\equiv-1\pmod{3+4t} such that w | k + 1 + t w\mid k+1+t and, in fact, d = k + 1 + t w d=\frac{k+1+t}{w}. We can write w = − 1 + n ⁡ ( 3 + 4 ​ t) w=-1+n(3+4t) with n ≥ 1 n\geq 1. Then d = k + 1 + t 3 ​ n + 4 ​ n ​ t − 1 d=\frac{k+1+t}{3n+4nt-1}. Therefore,

 | d = k + 1 + t 3 ​ n + 4 ​ n ​ t − 1 ≤ k + 1 + t 4 ​ t + 2 ≤ k + 1 2 = p + 3 8 d=\frac{k+1+t}{3n+4nt-1}\leq\frac{k+1+t}{4t+2}\leq\frac{k+1}{2}=\frac{p+3}{8} |  |

and then we have that d ≤ ⌊ p + 3 8 ⌋ d\leq\lfloor\frac{p+3}{8}\rfloor.The coordinate is also reached whenever t = 0 t=0, n = 1 n=1, what implies that w = 2 w=2 and 2 | k + 1 2\mid k+1, and therefore k is odd. For example, it is reached for p = 13 p=13, for this value k = 3 k=3 and d = k + 1 2 = 2 = p + 3 8 = ⌊ p + 3 8 ⌋ d=\frac{k+1}{2}=2=\frac{p+3}{8}=\lfloor\frac{p+3}{8}\rfloor. Therefore the bound is optimal. ∎

###### Proposition 2.

Under the conditions of Proposition 1, if t t is such that k + 1 + t k+1+t has a divisor w w that satisfies that w ≡ − 1 ( mod 3 + 4 ​ t) w\equiv-1\pmod{3+4t} then t ∈ [0, ⌊ k − 1 3 ⌋] t\in[{0,\lfloor\frac{k-1}{3}\rfloor}].

###### Proof.

Suppose that t > k − 1 3 t>\frac{k-1}{3}, then 3 ​ t > k − 1 3t>k-1 and therefore 3 + 4 ​ t > k + 2 + t 3+4t>k+2+t. This then implies that k + 1 + t ≢ − 1 ( mod 3 + 4 ​ t) k+1+t\not\equiv-1\pmod{3+4t} and, in particular, any divisor w w of k + 1 + t k+1+t is less than 3 + 4 ​ t 3+4t, so there is no divisor w w of k + 1 + t k+1+t such that it is satisfied that w ≡ − 1 ( mod 3 + 4 ​ t) w\equiv-1\pmod{3+4t}. We have therefore proved the contrapositive of what we were looking for. ∎

###### Remark 3.

There are many examples for which t t takes the maximum value of the interval, e.g. k = 4 k=4. In fact, the bound is always optimal whenever k ≡ 1 ( mod 3) k\equiv 1\pmod{3}, because if we consider k = 3 ​ u + 1 k=3u+1 with u ≥ 0 u\geq 0 we have that, if we take t = u t=u,

 | k + 1 + t = 3 ​ u + 1 + 1 + u = 2 + 4 ​ u k+1+t=3u+1+1+u=2+4u |  |

 | 3 + 4 ​ t = 3 + 4 ​ u 3+4t=3+4u |  |

and in this case we have that k + 1 + t ≡ − 1 ( mod 3 + 4 ​ t) k+1+t\equiv-1\pmod{3+4t} and therefore we can take w w as k + 1 + t k+1+t.

The propositions 3 and 4 shows that there are also parallels between Type A and B solutions when calculating their coordinates for d d.

###### Proposition 3.

Let p p be an odd prime number, if p p has a solution of Type B, ( d ​ u ​ v, d ​ u ​ p, d ​ v ​ p) (duv,dup,dvp) then d ≤ ⌊ p + 3 8 ⌋ d\leq\lfloor\frac{p+3}{8}\rfloor. This bound is also optimal.

###### Proof.

We know that if p p has a Type B solution, then the equation 4 ​ d ​ u ​ v = p + u + v 4duv=p+u+v is satisfied and therefore d = p 4 ​ u ​ v + 1 4 ​ u + 1 4 ​ v d=\frac{p}{4uv}+\frac{1}{4u}+\frac{1}{4v}. We know that there are multiple values where u = 1 u=1 and v = 2 v=2 or vice versa (by symmetry, they give rise to the same solution), and for those values we have that d = p 8 + 1 8 + 1 4 = p + 3 8 d=\frac{p}{8}+\frac{1}{8}+\frac{1}{4}=\frac{p+3}{8}. For any larger values of u u and v v we have therefore that d ≤ ⌊ p + 3 8 ⌋ d\leq\lfloor\frac{p+3}{8}\rfloor.

On the other hand, if u = v = 1 u=v=1 then, using the construction of ( 4), we have that n = v = 1 n=v=1, u = p + n 4 ​ d ​ n − 1 = p + 1 4 ​ d − 1 = 1 u=\frac{p+n}{4dn-1}=\frac{p+1}{4d-1}=1 and therefore 4 ​ d − 1 = p + 1 4d-1=p+1. But this then implies that p p is even, and by hypothesis p p is always odd, so the above bound is correct. ∎

###### Proposition 4.

Under the conditions of Proposition 3, if there exists t ≥ 0 t\geq 0 and two positive divisors a, b a,b of k + 1 + t k+1+t such that a + b = 3 + 4 ​ t a+b=3+4t then t ∈ [0, ⌊ k − 1 3 ⌋] t\in[{0,\lfloor\frac{k-1}{3}\rfloor}].

###### Proof.

It’s obvious to prove that, given n ∈ ℕ n\in\mathbb{N}, m ​ a ​ x ​ { a + b / a ​ b ∣ n } = n + 1 max\{a+b/ab\mid n\}=n+1. Therefore there can’t be such divisors for k + 1 + t k+1+t when m ​ a ​ x ​ { a + b / a ​ b ∣ k + 1 + t } < 3 + 4 ​ t max\{a+b/ab\mid k+1+t\}<3+4t, and this implies that ( k + 1 + t) + 1 < 3 + 4 ​ t (k+1+t)+1<3+4t, which implies that 3 + 4 ​ t > k + 2 + t 3+4t>k+2+t, the same values for which we couldn’t find a Type A solution, so again t t must belong to the interval [0, ⌊ k − 1 3 ⌋] [{0,\lfloor\frac{k-1}{3}\rfloor}]. ∎

###### Proposition 5.

Let a a be any natural number, then if a ≡ − n ( mod 4 ​ d ​ n − 1) a\equiv-n\pmod{4dn-1} we also have that a ≡ − ( a + n 4 ​ d ​ n − 1) ( mod ( 4 ​ a ​ d + 1 4 ​ d ​ n − 1)) a\equiv-\left(\frac{a+n}{4dn-1}\right)\pmod{\left(\frac{4ad+1}{4dn-1}\right)} and the converse is also true. Both congruences lead us, moreover, to the same Type B solution for a.

###### Proof.

In the first case, using ( 4), we arrive at a Type B solution of the form ( d ​ u ​ v, d ​ u ​ a, d ​ v ​ a) (duv,dua,dva) with u = a + n 4 ​ d ​ n − 1 u=\frac{a+n}{4dn-1}, v = n v=n. In the second case we have that 4 ​ d ​ ( a + n 4 ​ d ​ n − 1) − 1 = 4 ​ a ​ d + 1 4 ​ d ​ n − 1 4d\left(\frac{a+n}{4dn-1}\right)-1=\frac{4ad+1}{4dn-1}, so using the same theorem we arrive at another Type B solution of the form ( d ​ u ​ v, d ​ u ​ a, d ​ v ​ a) (duv,dua,dva), with v = a + n 4 ​ d ​ n − 1 v=\frac{a+n}{4dn-1} and u = n u=n, because

 | u = a + v 4 ​ d ​ v − 1 = a + a + n 4 ​ d ​ n − 1 4 ​ d ​ a + n 4 ​ d ​ n − 1 − 1 = 4 ​ a ​ d ​ n − a + a + n 4 ​ d ​ n − 1: 4 ​ a ​ d + 1 4 ​ d ​ n − 1 = 4 ​ a ​ d ​ n + n 4 ​ d ​ n + 1 = n u=\frac{a+v}{4dv-1}=\frac{a+\frac{a+n}{4dn-1}}{4d\frac{a+n}{4dn-1}-1}=\frac{4adn-a+a+n}{4dn-1}:\frac{4ad+1}{4dn-1}=\frac{4adn+n}{4dn+1}=n |  |

Both solutions are the same except for a translation of their coordinates, and therefore both congruences must be true or false simultaneously. The operations also show that they are cyclic, and by means of one congruence the other can be reconstructed and vice versa. ∎

This last proposition implies, therefore, that every Type B solution always has at least two congruences associated with it, as we already saw in the case of 2521, which possessed a single Type B solution but two associated congruences, which are 2521 ≡ − 2 ( mod 87) 2521\equiv-2\pmod{87} and 2521 ≡ − 29 ( mod 1275) 2521\equiv-29\pmod{1275}. It is a result that can be applied outside the context of the conjecture as a proposition in the field of modular arithmetic.

###### Proposition 6.

Let p p be prime, then p p possesses a solution that is both of Type A and B if and only if p ≡ − 1 ( mod 4 ​ d − 1) p\equiv-1\pmod{4d-1} for some d ∈ ℕ d\in\mathbb{N}.

###### Proof.

If p ≡ − 1 ( mod 4 ​ d − 1) p\equiv-1\pmod{4d-1} then, by ( 4), it has a Type B solution. Moreover, as − 4 ​ d ≡ − 1 ( mod 4 ​ d − 1) -4d\equiv-1\pmod{4d-1} by ( 5) that same congruence also generates a Type A solution, which is the one we already had.

Now suppose that p has a solution that is both of Type A and B, i.e.,

 | ( x, y, z) = ( d ​ u, d ​ v, d ​ u ​ v) = ( D ​ U ​ V, D ​ U ​ p, D ​ V ​ p) (x,y,z)=(du,dv,duv)=(DUV,DUp,DVp) |  |

with d, u, v, D, U, V ∈ ℕ d,u,v,D,U,V\in\mathbb{N}. We can consider without loss of generality that u < v u<v. From the Type A structure of the solution we obtain that x ​ y = d ​ z xy=dz, and from the Type B structure we obtain that y ​ z = D ​ x ​ p 2 yz=Dxp^{2}. This implies that y 2 = D ​ d ​ p 2 y^{2}=Ddp^{2}. Substituting into the Type B solution we have that

 | D 2 ​ U 2 ​ p 2 = D ​ d ​ p 2 D^{2}U^{2}p^{2}=Ddp^{2} |  |

and therefore D ​ U 2 = d DU^{2}=d, which implies that U 2 = d D U^{2}=\frac{d}{D} and, in particular, that D | d D\mid d. Substituting y 2 = D ​ d ​ p 2 y^{2}=Ddp^{2} into the Type A structure we obtain that

 | d ​ v 2 = D ​ p 2 dv^{2}=Dp^{2} |  |

Since p ∤ u p\nmid u we know that p | v p\mid v and that implies that D d = v 2 p 2 ∈ ℕ \frac{D}{d}=\frac{v^{2}}{p^{2}}\in\mathbb{N} and d | D d\mid D. We conclude that d = D d=D and this automatically implies that v = p v=p and U = 1 U=1. This implies that the solution has the form ( d ​ u, d ​ p, d ​ u ​ p) (du,dp,dup). Since it is of Type B, we have, by ( 4), that necessarily p ≡ − 1 ( mod 4 ​ d − 1) p\equiv-1\pmod{4d-1}. ∎

## 3 Appendix I: Solutions of Type C?

As was said in Remark 1 it happens that, if we have the polynomial R ⁡ ( x, y, t, z) = ( 4 ​ x ​ y ​ z − 1) ​ ( 3 + 4 ​ t) − 4 ​ x 2 ​ y R(x,y,t,z)=(4xyz-1)(3+4t)-4x^{2}y that has as its image all the values that possess a Type II solution, the Type A and B solutions are related to it since the Type A solutions are obtained in the particular case in which x = 1 x=1 while the Type B solutions are obtained when z = 1 z=1. This motivates the idea of considering what happens in the case in which y = 1 y=1, for which we obtain the polynomial R ⁡ ( x, 1, t, z) = ( 4 ​ x ​ z − 1) ​ ( 3 + 4 ​ t) − 4 ​ x 2 R(x,1,t,z)=(4xz-1)(3+4t)-4x^{2}. We will study it in the following theorem that encompasses this new type of solutions.

###### Theorem 9.

Let n ∈ ℕ n\in\mathbb{N} be of the form n = 4 ​ k + 1 n=4k+1. They are equivalent:

1. (i)

There exists ( x 0, z 0, t 0) (x_{0},z_{0},t_{0}) such that n = R ⁡ ( x 0, 1, t 0, z 0) n=R(x_{0},1,t_{0},z_{0});

2. (ii)

There exist d, m ∈ ℕ d,m\in\mathbb{N} such that − n ≡ 4 ​ d 2 ( mod 4 ​ d ​ m − 1) -n\equiv 4d^{2}\pmod{4dm-1};

3. (iii)

n has a solution of the Erdos-Straus conjecture with the form ( u ​ v, u ​ w ​ n, v ​ w ​ n) (uv,uwn,vwn), with u, v, w ∈ ℕ u,v,w\in\mathbb{N};

4. (iv)

For a certain t ≥ 0 t\geq 0 exists a, b ∈ ℕ a,b\in\mathbb{N} such that a ​ b = k + 1 + t ab=k+1+t, 3 + 4 ​ t | a + b 3+4t\mid a+b.

We will consider this new solution as a Type C solution.

###### Proof.

First we will see that (i) implies (ii). We know that n n can be written as n = ( 4 ​ x 0 ​ z 0 − 1) ​ ( 3 + 4 ​ t 0) − 4 ​ x 0 2 n=(4x_{0}z_{0}-1)(3+4t_{0})-4x_{0}^{2}, then it is automatically satisfied that

 | n ≡ − 4 ​ x 0 2 ( mod 4 ​ x 0 ​ z 0 − 1) n\equiv-4x_{0}^{2}\pmod{4x_{0}z_{0}-1} |  |

and so we have (ii) automatically by identifying d = x 0 d=x_{0}, m = z 0 m=z_{0}.

To show that (ii) implies (iii) we know that − n ≡ 4 ​ d 2 ( mod 4 ​ d ​ m − 1) -n\equiv 4d^{2}\pmod{4dm-1} and therefore − n ​ m ≡ d ( mod 4 ​ d ​ m − 1) -nm\equiv d\pmod{4dm-1}. This implies that d + n ​ m = v ⁡ ( 4 ​ d ​ m − 1) d+nm=v(4dm-1) for a certain v ∈ ℕ v\in\mathbb{N}, so we have that 4 ​ d ​ m ​ v = d + n ​ m + v 4dmv=d+nm+v. Dividing by d ​ m ​ v ​ n dmvn we have that

 | 4 n = 1 m ​ v ​ n + 1 d ​ v + 1 d ​ m ​ n \frac{4}{n}=\frac{1}{mvn}+\frac{1}{dv}+\frac{1}{dmn} |  |

which is of the form requested with u = d u=d, w = m w=m.

Now we start from (iii) and assume that we have a solution of the form ( u ​ v, u ​ w ​ n, v ​ w ​ n) (uv,uwn,vwn), so multiplying by d ​ m ​ v ​ n dmvn we have again that 4 ​ u ​ w ​ v = u + n ​ w + v 4uwv=u+nw+v. This implies that v ⁡ ( 4 ​ u ​ w − 1) = u + n ​ w v(4uw-1)=u+nw and therefore that n ​ w ≡ − u ( mod 4 ​ u ​ w − 1) nw\equiv-u\pmod{4uw-1}. If we substitute n = 4 ​ k + 1 n=4k+1 this leads us to that

 | 4 ​ w ​ k ≡ − u − v ( mod 4 ​ u ​ w − 1) 4wk\equiv-u-v\pmod{4uw-1} |  |

and therefore that

 | k ≡ − u 2 − u ​ w ( mod 4 ​ u ​ w − 1) k\equiv-u^{2}-uw\pmod{4uw-1} |  |

Translating the congruence to an equality leads to the fact that k + u 2 + u ​ w = d ⁡ ( 4 ​ u ​ w − 1) k+u^{2}+uw=d(4uw-1) for a certain d ∈ ℕ d\in\mathbb{N} and hence

 | k + d = 4 ​ d ​ u ​ w − u ​ w − u 2 k+d=4duw-uw-u^{2} |  |

which can be rewritten as

 | k + d = u ⁡ ( w ⁡ ( 4 ​ d − 1) − u) k+d=u(w(4d-1)-u) |  |

Since we know that d d is a natural number we can make the change of variable d = t + 1 d=t+1, t ≥ 0 t\geq 0 and we have then that the equality can be written as

 | k + 1 + t = u ⁡ ( w ⁡ ( 3 + 4 ​ t) − u) k+1+t=u(w(3+4t)-u) |  |

This implies that k + 1 + t k+1+t can be decomposed as the product of two divisors a = u a=u, b = w ⁡ ( 3 + 4 ​ t) − u b=w(3+4t)-u, such that a + b = w ⁡ ( 3 + 4 ​ t) a+b=w(3+4t) and therefore 3 + 4 ​ t | a + b 3+4t\mid a+b, as we were looking for.

To prove finally that (iv) implies (i), we assume that we have two divisors a, b a,b of k + 1 + t k+1+t for a certain t ≥ 0 t\geq 0 such that 3 + 4 ​ t | a + b 3+4t\mid a+b. Undoing the same math as above we have that

 | k + 1 + t = u ⁡ ( w ⁡ ( 3 + 4 ​ t) − u) k+1+t=u(w(3+4t)-u) |  |

and therefore that

 | k + 1 + t = 3 ​ u ​ w + 4 ​ u ​ w ​ t − u 2 k+1+t=3uw+4uwt-u^{2} |  |

This leads us to the fact that

 | 4 ​ k + 4 + 4 ​ t = 12 ​ u ​ w + 16 ​ u ​ w ​ t − 4 ​ u 2 4k+4+4t=12uw+16uwt-4u^{2} |  |

and therefore

 | 4 ​ k + 1 = 12 ​ u ​ w + 16 ​ u ​ w ​ t − ( 3 + 4 ​ t) − 4 ​ u 2 4k+1=12uw+16uwt-(3+4t)-4u^{2} |  |

which by rearranging the terms leaves us with the expression

 | n = ( 4 ​ u ​ w − 1) ​ ( 3 + 4 ​ t) − 4 ​ u 2 n=(4uw-1)(3+4t)-4u^{2} |  |

which shows that n = R ⁡ ( u, 1, t, w) n=R(u,1,t,w) and therefore that n n belongs to the image of the reduced polynomial n = R ⁡ ( x, 1, t, z) n=R(x,1,t,z), which was just what was said in section (i). ∎

###### Corollary 3.

Given the nature as a quadratic equation of the congruence − n ≡ 4 ​ d 2 ( mod 4 ​ d ​ m − 1) -n\equiv 4d^{2}\pmod{4dm-1} and taking into account the notation of Legendre’s symbol and that it always happens that

 | ( − 1 4 ​ u − 1) = − 1 \left(\frac{-1}{4u-1}\right)=-1 |  |

we have then that a necessary condition for a number n n of the form n = 4 ​ k + 1 n=4k+1 to have a solution of Type C will be that there exists a certain u u for which n n is not a quadratic residue in ℤ 4 ​ u − 1 \mathbb{Z}_{4u-1}. This will imply that − n -n will possess not only one but two solutions to the equation − n ≡ x 2 ( mod 4 ​ u − 1) -n\equiv x^{2}\pmod{4u-1}. If we denote by x 0 x_{0} and 4 ​ u − 1 − x 0 4u-1-x_{0} those solutions we have that exactly one of them will be even and the other odd and, therefore, either x 0 2 \frac{x_{0}}{2} or 4 ​ u − 1 − x 0 2 \frac{4u-1-x_{0}}{2} will be a natural number. Then it will be an indispensable condition, for a solution of Type C to exist, that this number be a divisor of u u.

Although this type of solution does not seem necessary in experimental terms to cover all the prime values congruent to 1 modulo 4, it can be added to the conjecture we already have, by extending the system of congruences without any cost:

###### Conjecture 2.

Let be p ∈ ℕ p\in\mathbb{N} prime, then exists d, n ∈ ℕ d,n\in\mathbb{N} such that p ≡ − 4 ​ d ( mod 4 ​ d ​ n − 1) p\equiv-4d\pmod{4dn-1}, p ≡ − n ( mod 4 ​ d ​ n − 1) p\equiv-n\pmod{4dn-1} or p ≡ − 4 ​ d 2 ( mod 4 ​ d ​ n − 1) p\equiv-4d^{2}\pmod{4dn-1}. If this result is true, then this congruence system covers all primes and the Erdos-Straus conjecture is true.

Another immediate implication, thanks to the fact that ( 4) is true for all natural numbers, not just prime numbers, is that there exist infinite pairs of values of the form 4 ​ k + 1 4k+1 such that their distance is equal to 4 ​ s 4s, with s ≥ 1 s\geq 1 chosen at our option and satisfying the conjecture. Indeed, if we call

 | S ⁡ ( x, y, t) = R ⁡ ( x, 1, t, y) = ( 4 ​ x ​ y − 1) ​ ( 3 + 4 ​ t) − 4 ​ x 2 S(x,y,t)=R(x,1,t,y)=(4xy-1)(3+4t)-4x^{2} |  |

then we have that S ⁡ ( x, y, t) − P ⁡ ( x, y, t) = 4 ​ x 2 ​ ( y − 1) S(x,y,t)-P(x,y,t)=4x^{2}(y-1), and given s ∈ ℕ s\in\mathbb{N}, if we define n = S ⁡ ( 1, s + 1, t) n=S(1,s+1,t) and n ′ = P ⁡ ( 1, s + 1, t) n^{\prime}=P(1,s+1,t) then it is immediate to check that n − n ′ = 4 ​ s n-n^{\prime}=4s for every value t ≥ 0 t\geq 0 and we have made the infinite pairs requested, which satisfy the Erdos-Straus conjecture by being image of the polynomials mentioned above.

## 4 Appendix II: Reduction to Egyptian Numbers of Order 2

Although the values that have the form n = 4 ​ k + 1 n=4k+1 turn out to be the most problematic to study, we can also take advantage of their particular structure to reach results that only they can fulfill, like this theorem that proves the existence of infinite consecutive values that satisfy the Erdos-Straus Conjecture, something that Manuel Bello Hernández, Manuel Benito and Emilio Fernández already proved in [10], but that is shown here in a much simpler and direct way and by means of an ingenious transformation.

###### Theorem 10.

Given n ∈ ℕ n\in\mathbb{N}, there exists a chain of n n consecutive natural numbers that satisfies the Erdos-Straus conjecture.

###### Proof.

Since identities are known for even values and of the form n = 4 ​ k + 3 n=4k+3, it will suffice to prove this for those of the form n = 4 ​ k + 1 n=4k+1. First we will show that, if there exists d ∈ ℕ d\in\mathbb{N} such that 4 ​ d − 1 k + d \frac{4d-1}{k+d} is Egyptian of order 2, then n = 4 ​ k + 1 n=4k+1 satisfies the Erdos-Straus conjecture.

If 4 ​ d − 1 k + d = 1 y + 1 z \frac{4d-1}{k+d}=\frac{1}{y}+\frac{1}{z} then 4 ​ d k + d = 1 k + d + 1 y + 1 z \frac{4d}{k+d}=\frac{1}{k+d}+\frac{1}{y}+\frac{1}{z}. We call k + d = x k+d=x, and therefore d = x − k d=x-k and it follows that

 | 4 ​ ( x − k) x = 1 x + 1 y + 1 z \frac{4(x-k)}{x}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  |

which implies that

 | 4 = 4 ​ k + 1 x + 1 y + 1 z 4=\frac{4k+1}{x}+\frac{1}{y}+\frac{1}{z} |  |

We call n = 4 ​ k + 1 n=4k+1 and we have that

 | 4 n = 1 x + 1 n ​ y + 1 n ​ z \frac{4}{n}=\frac{1}{x}+\frac{1}{ny}+\frac{1}{nz} |  |

which was what we were looking for.

Now, it is well known that a b \frac{a}{b} is Egyptian of order 2 if and only if there exist u, v u,v divisors of b b such that a a divides to u + v u+v. Applied to 4 ​ d − 1 k + d \frac{4d-1}{k+d} we have that there exist u, v u,v divisors of k + d k+d such that 4 ​ d − 1 4d-1 divides to u + v u+v. Note that if k k is odd it is automatically fulfilled by taking d = u = 1 d=u=1, v = 2 v=2.

We consider k k of the form n! − f ⁡ ( n) n!-f(n), and take d = f ⁡ ( n) d=f(n). For this form to be satisfactory there must exist u, v u,v divisors of n! n! such that 4 ​ f ​ ( n) − 1 | u + v 4f(n)-1\mid u+v. We look for f ⁡ ( n) f(n) to be as large as possible, and that is the case if it is also u + v u+v, with u ≠ v u\neq v. We take therefore u + v = n + ( n − 1) u+v=n+(n-1). Equaling we have that

 | 4 ​ f ​ ( n) − 1 = 2 ​ n − 1 4f(n)-1=2n-1 |  |

And therefore these values u, v u,v will always be possible and valid if f ⁡ ( n) ≤ ⌊ n 2 ⌋ f(n)\leq\lfloor\frac{n}{2}\rfloor, which implies that all values 4 ​ k + 1 4k+1, with k k belonging to the interval [n! − ⌊ n 2 ⌋, n! − 1] [{n!-\lfloor\frac{n}{2}\rfloor,n!-1}], satisfy the Erdos-Straus conjecture. Since we can take n n as large as we want and the length of the interval increases with n n, we can find consecutive values to our liking that satisfy this conjecture. ∎

###### Corollary 4.

Proving that there exists d ∈ ℕ d\in\mathbb{N} such that 4 ​ d − 1 k + d \frac{4d-1}{k+d} is Egyptian of order 2 is equivalent to finding a Type II solution for 4 ​ k + 1 4k+1.

###### Proof.

If 4 ​ d − 1 k + d = 1 y + 1 z \frac{4d-1}{k+d}=\frac{1}{y}+\frac{1}{z}, then there exists u, v | k + d u,v\mid k+d, 4 ​ d − 1 | u + v 4d-1\mid u+v, and therefore k + d = u ​ v ​ w k+d=uvw, u + v = t ⁡ ( 4 ​ d − 1) u+v=t(4d-1) for some certain naturals w, t w,t. By elementary calculations and calling n = 4 ​ k + 1 n=4k+1 we obtain that

 | n = 4 ​ u ​ v ​ w − u + v t n=4uvw-\frac{u+v}{t} |  |

Renaming u = c ​ t − v u=ct-v, we have that n = c ⁡ ( 4 ​ v ​ w ​ t − 1) − 4 ​ v 2 ​ w n=c(4vwt-1)-4v^{2}w. By changing the names of the variables, n = ( 4 ​ x ​ y ​ z − 1) ​ c − 4 ​ x 2 ​ y n=(4xyz-1)c-4x^{2}y. Since n n is congruent with 1 modulo 4, then c c is congruent with 3 modulo 4, and so c = 3 + 4 ​ s c=3+4s, s ≥ 0 s\geq 0, and n = R ⁡ ( x, y, z, s) n=R(x,y,z,s). By ( 8), n n is then a value with a Type II solution. ∎

## 5 Conclusion

We have defined two types of solutions, Type A and B, which have allowed us to propose a system of congruences that we conjecture gives a solution of the Erdos-Straus conjecture to all prime numbers. This is one of the most reasonable techniques for solving the Erdos-Straus conjecture: to obtain a system of congruences such that they all have an associated polynomial identity and that they completely cover all prime numbers. The first part, that every congruence has an associated polynomial identity and therefore none of them contain quadratic residues, has already been shown. It remains to be seen whether counterexamples to this new conjecture are found, which is the same as finding some prime number that lacks solutions of both Type A and Type B and, if not found and therefore suspecting that the conjecture is true, whether or not we have created an alternative formulation of the same problem as difficult to prove or more difficult to prove than the original problem. So far we have experimentally proved that our proposed system of congruences gives a solution to the first ten thousand prime numbers without exceptions, which gives us hope for its usefulness as a tool to solve the Erdos-Straus conjecture.

## References

- [1] L. J. Mordell. Diophantine equations. Number 30 in Pure and applied mathematics. Acad. Pr, London, 2. print edition, 1970.
- [2] Koichi Yamamoto. On the Diophantine Equation 4/n=1/x+1/y+1/z. Memoirs of the Faculty of Science, Kyushu University. Series A, Mathematics, 19(1):37–47, 1965.
- [3] Serge E. Salez. The Erdos-Straus conjecture. New modular equations and checking up to N=10^17, June 2014. arXiv:1406.6307 [math].
- [4] Miguel Angel Lopez. Structure and form of the solutions of the Erdos-Straus conjecture, December 2022. arXiv:2206.10319 [math].
- [5] Kyle Bradford. A note on the Erdos-Straus Conjecture, March 2020. arXiv:1906.00561 [math].
- [6] Christian Elsholtz and Terence Tao. Counting the number of solutions to the Erdos-Straus equation on unit fractions, August 2015. arXiv:1107.1010 [math].
- [7] M. Monks and A. Velingker. On the Erdös-Straus conjecture : Properties of solutions to its underlying diophantine equation. 2007.
- [8] John H. Conway and Richard K. Guy. The Book of Numbers. Springer, New York, NY, 1996.
- [9] Eugen J. Ionascu and Andrew Wilson. On the Erdos-Straus conjecture, January 2010. arXiv:1001.1100 [math].
- [10] Manuel Bello-Hernández, Manuel Benito, and Emilio Fernández. On Egyptian fractions, April 2012. arXiv:1010.2035 [math].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
