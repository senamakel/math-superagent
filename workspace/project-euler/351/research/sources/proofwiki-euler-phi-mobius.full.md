<!-- source: https://proofwiki.org/wiki/Euler_Phi_Function_in_terms_of_M%C3%B6bius_Function | converted from HTML -->

Euler Phi Function in terms of Möbius Function - ProofWiki

# Euler Phi Function in terms of Möbius Function

From ProofWiki

Jump to navigation Jump to search

## Theorem

Let $n \in \Z_{>0}$ be a [strictly positive integer][1].

Then:

$\ds \sum_{d \mathop \divides n} \map \mu d \frac n d = \map \phi n$

where:

$\ds \sum_{d \mathop \divides n}$ denotes the [sum over all of the divisors][2] of $n$ $\map \phi n$ is the [Euler $\phi$ function][3], the number of [integers][4] less than $n$ that are [prime to][5] $n$ $\map \mu d$ is the [Möbius function][6].

Equivalently, this says that:

$\phi = \mu * I_{\Z_{>0} }$

where:

$*$ denotes [Dirichlet convolution][7] $I_{\Z_{>0} }$ denotes the [identity mapping][8] on $\Z_{>0}$, that is: $\forall n \in \Z_{>0}: I_{\Z_{>0} }: n \mapsto n$

 | ***Work In Progress***
In particular: **Add a link to a page proving this equivalence.**
*You can help $\mathsf{Pr} \infty \mathsf{fWiki}$ by [completing it][9].*
*To discuss this page in more detail, feel free to use the [talk page][10].*
*When this work has been completed, you may remove this instance of `{{ [WIP][11] }}`from the code.* |

## Proof

[Sum of Möbius Function over Divisors][12] says:

$\ds \sum_{d \mathop \divides n} \map \mu d = \floor {\frac 1 n}$

where $\floor {\dfrac 1 n}$ is the [floor][13] of $\dfrac 1 n$.

$\Box$

Let $\map 1 k = 1$ be the [constant mapping][14].

Then $\phi$ is defined as:

$\ds \map \phi n = \sum_{\substack {k \mathop \perp n \\ 1 \mathop \le k \mathop \le n}} \map 1 k$

We have that $\floor {\dfrac 1 {\gcd \set {n, k} } }$ is $1$ if $k \perp n$ and $0$ otherwise.

Thus we can rewrite the above [summation][15] as:

$\ds \sum_{k \mathop = 1}^n \floor {\frac 1 {\gcd \set {n, k} } }$

Now we may use [Sum of Möbius Function over Divisors][12], with $\gcd \set {n, k}$ replacing $n$, to get:

 |  |  |  |  |  |  | \(\ds \map \phi n\)  | \(=\)  |  |  |  | \(\ds \sum_{k \mathop = 1}^n \paren {\sum_{d \mathop \divides \gcd \set {n, k} } \map \mu d}\)  |  |  |  |  |

 |  |  |  |  |  |  | \(\ds \)  | \(=\)  |  |  |  | \(\ds \sum_{k \mathop = 1}^n \sum_{\substack {d \mathop \divides n \\ d \mathop \divides k} } \map \mu d\)  |  |  |  |  |

For a fixed [divisor][16] $d$ of $n$, we must sum over all those $k$ in the range $1 \le k \le n$ which are multiples of $d$.

If we write $k = q d$, then $1 \le k \le n$ [if and only if][17] $1 \le q \le \dfrac n d$.

Hence the last sum for $\map \phi n$ can be written as:

 |  |  |  |  |  |  | \(\ds \map \phi n\)  | \(=\)  |  |  |  | \(\ds \sum_{d \mathop \divides n} \paren {\sum_{q \mathop = 1}^{\tfrac n d} \map \mu d}\)  |  |  |  |  |

 |  |  |  |  |  |  | \(\ds \)  | \(=\)  |  |  |  | \(\ds \sum_{d \mathop \divides n} \map \mu d \sum_{q \mathop = 1}^{\tfrac n d} \map 1 q\)  |  |  |  |  |

 |  |  |  |  |  |  | \(\ds \)  | \(=\)  |  |  |  | \(\ds \sum_{d \mathop \divides n} \map \mu d \frac n d\)  |  |  |  |  |

$\blacksquare$

## Sources

- 1971: [Allan Clark][18]: **[Elements of Abstract Algebra][19]... [(previous)][20]... [(next)][21]: Chapter $1$: Properties of the Natural Numbers: $\S 25 \beta$
- 1976: [Tom M. Apostol][22]: **[Introduction to Analytic Number Theory][23]... [(previous)][24]... [(next)][25]: $2.4$: A relation connected $\varphi$ and $\mu$

Retrieved from " [https://proofwiki.org/w/index.php?title=Euler_Phi_Function_in_terms_of_Möbius_Function&oldid=657633][26] "

[Categories][27]:

- [Work To Do][28]
- [Proven Results][29]
- [Euler Phi Function][30]
- [Möbius Function][31]

## Navigation menu

### Search

[32]


## Links

[1]: /wiki/Definition:Strictly_Positive_Integer
[2]: /wiki/Definition:Sum_Over_Divisors
[3]: /wiki/Definition:Euler_Phi_Function
[4]: /wiki/Definition:Integer
[5]: /wiki/Definition:Coprime_Integers
[6]: /wiki/Definition:M%C3%B6bius_Function
[7]: /wiki/Definition:Dirichlet_Convolution
[8]: /wiki/Definition:Identity_Mapping
[9]: https://proofwiki.org/w/index.php?title=Euler_Phi_Function_in_terms_of_M%C3%B6bius_Function&amp;action=edit
[10]: /wiki/Talk:Euler_Phi_Function_in_terms_of_M%C3%B6bius_Function
[11]: /wiki/Template:WIP
[12]: /wiki/Sum_of_M%C3%B6bius_Function_over_Divisors
[13]: /wiki/Definition:Floor_Function
[14]: /wiki/Definition:Constant_Mapping
[15]: /wiki/Definition:Summation
[16]: /wiki/Definition:Divisor_of_Integer
[17]: /wiki/Definition:Iff
[18]: /wiki/Mathematician:Allan_Clark
[19]: /wiki/Book:Allan_Clark/Elements_of_Abstract_Algebra
[20]: /wiki/M%C3%B6bius_Function_is_Multiplicative
[21]: /wiki/Definition:Group_Theory
[22]: /wiki/Mathematician:Tom_M._Apostol
[23]: /wiki/Book:Tom_M._Apostol/Introduction_to_Analytic_Number_Theory
[24]: /wiki/Sum_of_Euler_Phi_Function_over_Divisors
[25]: /wiki/Euler_Phi_Function_of_Integer
[26]: https://proofwiki.org/w/index.php?title=Euler_Phi_Function_in_terms_of_Möbius_Function&amp;oldid=657633
[27]: /wiki/Special:Categories
[28]: /wiki/Category:Work_To_Do
[29]: /wiki/Category:Proven_Results
[30]: /wiki/Category:Euler_Phi_Function
[31]: /wiki/Category:M%C3%B6bius_Function
[32]: /wiki/Main_Page
