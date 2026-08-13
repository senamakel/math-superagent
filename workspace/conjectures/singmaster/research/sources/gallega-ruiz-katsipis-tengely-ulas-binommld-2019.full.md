<!-- source: https://arxiv.org/html/1904.11369v1 | converted from HTML -->

On the Diophantine equation = ( n k ) + ( m l ) d

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1904.11369v1 [math.NT] 25 Apr 2019

# On the Diophantine equation ( n k) = ( m l) + d \binom{n}{k}=\binom{m}{l}+d

H. R. Gallegos-Ruiz Address: Homero R. Gallegos-Ruiz
Unidad Académica de Matemáticas
Universidad Autónoma de Zacatecas
Calzada Solidaridad y Paseo de la Bufa
Zacatecas, Zacatecas, CP 98000
Mexico Email address: [hgallegos@uaz.edu.mx][3], N. Katsipis Address: Nikolaos Katsipis
Department of Mathematics & Applied Mathematics
University of Crete
GR-70013, Heraklion, Crete
Greece Email address: [katsipis@gmail.com][4], Sz. Tengely Address: Szabolcs Tengely
Institute of Mathematics
University of Debrecen
P.O.Box 12
4010 Debrecen
Hungary Email address: [tengely@science.unideb.hu][5] and M. Ulas Address: Maciej Ulas
Jagiellonian University
Faculty of Mathematics and Computer Science
Institute of Mathematics
Łojasiewicza 6
30-348 Kraków
Poland Address: and Address: Institute of Mathematics of the Polish Academy of Sciences
Świȩtego Tomasza 30
31-014 Kraków, Poland Email address: [Maciej.Ulas@im.uj.edu.pl][6]

Date: August 11, 2026

###### Abstract.

By finding all integral points on certain elliptic and hyperelliptic curves we completely solve the Diophantine equation ( n k) = ( m l) + d \binom{n}{k}=\binom{m}{l}+d for − 3 ≤ d ≤ 3 -3\leq d\leq 3 and ( k, l) ∈ { ( 2, 3), ( 2, 4), ( 2, 5), ( 2, 6), ( 2, 8), ( 3, 4), ( 3, 6), ( 4, 6), ( 4, 8) }. (k,l)\in\{(2,3),\;(2,4),\;(2,5),\;(2,6),\;(2,8),\;(3,4),\;(3,6),\;(4,6),\;(4,8)\}. Moreover, we present some other observations of computational and theoretical nature concerning the title equation.

###### Key words and phrases:

binomial coefficient, Diophantine equation, elliptic curve, genus two curve, integer points

###### 2000 Mathematics Subject Classification

Primary 11G30, Secondary 11J8

## 1. Introduction

There are many nice results related to the equation

(1) |  | ( n k) = ( m l), \binom{n}{k}=\binom{m}{l}, |  |

in unknowns k k, l l, m m, n. n. This is usually considered with the restrictions 2 ≤ k ≤ n / 2, 2 ≤ l ≤ m / 2 2\leq k\leq n/2,2\leq l\leq m/2 and k < l. k<l. The only known solutions (with the above mentioned restrictions) are the following

 | ( 16 2) = ( 10 3), ( 56 2) = ( 22 3), ( 120 2) = ( 36 3), \displaystyle\binom{16}{2}=\binom{10}{3},\quad\binom{56}{2}=\binom{22}{3},\quad\binom{120}{2}=\binom{36}{3}, |  |

 | ( 21 2) = ( 10 4), ( 153 2) = ( 19 5), ( 78 2) = ( 15 5) = ( 14 6), \displaystyle\binom{21}{2}=\binom{10}{4},\quad\binom{153}{2}=\binom{19}{5},\quad\binom{78}{2}=\binom{15}{5}=\binom{14}{6}, |  |

 | ( 221 2) = ( 17 8), ( F 2 ​ i + 2 ​ F 2 ​ i + 3 F 2 ​ i ​ F 2 ​ i + 3) = ( F 2 ​ i + 2 ​ F 2 ​ i + 3 − 1 F 2 ​ i ​ F 2 ​ i + 3 + 1) for i = 1, 2, …, \displaystyle\binom{221}{2}=\binom{17}{8},\quad\binom{F_{2i+2}F_{2i+3}}{F_{2i}F_{2i+3}}=\binom{F_{2i+2}F_{2i+3}-1}{F_{2i}F_{2i+3}+1}\mbox{ for }i=1,2,\ldots, |  |

where F n F_{n} is the n n th Fibonacci number. The infinite family of solutions involving Fibonacci numbers was found by Lind [17] and Singmaster [21].

Equation ( 1) has been completely solved for pairs

 | ( k, l) = ( 2, 3), ( 2, 4), ( 2, 6), ( 2, 8), ( 3, 4), ( 3, 6), ( 4, 6), ( 4, 8). (k,l)=(2,3),\;(2,4),\;(2,6),\;(2,8),\;(3,4),\;(3,6),\;(4,6),\;(4,8). |  |

In cases of these pairs one can easily reduce the equation to the determination of solutions of a number of Thue equations or elliptic Diophantine equations. In 1966, Avanesov [1] found all integral solutions of equation ( 1) with ( k, l) = ( 2, 3). (k,l)=(2,3). De Weger [10] and independently Pintér [19] provided all the solutions of the equation with ( k, l) = ( 2, 4). (k,l)=(2,4). The case ( k, l) = ( 3, 4) (k,l)=(3,4) reduces to the equation Y ⁡ ( Y + 1) = X ⁡ ( X + 1) ​ ( X + 2) Y(Y+1)=X(X+1)(X+2) which was solved by Mordell [18]. The remaining pairs ( 2, 6), ( 2, 8), ( 3, 6), ( 4, 6), ( 4, 8) (2,6),(2,8),(3,6),(4,6),(4,8) were handled by Stroeker and de Weger [27], using linear forms in elliptic logarithms. The case with ( k, l) = ( 2, 5) (k,l)=(2,5) was completely solved by Bugeaud, Mignotte, Siksek, Stoll and Tengely [8], the integral solutions are as follows

 | ( n, m) = ( 0, 0), ( 0, 1), ( 1, 0), ( 1, 1), ( 2, 0), ( 2, 1), ( 3, 0), ( 3, 1), ( 4, 0), ( 4, 1), ( 5, − 1), \displaystyle(n,m)=(0,0),\;(0,1),\;(1,0),\;(1,1),\;(2,0),\;(2,1),\;(3,0),\;(3,1),\;(4,0),\;(4,1),\;(5,-1), |  |

 | ( 5, 2), ( 6, − 3), ( 6, 4), ( 7, − 6), ( 7, 7), ( 15, − 77), ( 15, 78), ( 19, − 152), ( 19,153). \displaystyle(5,2),\;(6,-3),\;(6,4),\;(7,-6),\;(7,7),\;(15,-77),\;(15,78),\;(19,-152),\;(19,153). |  |

In a recent paper Blokhuis, Brouwer and de Weger [4] determined all non-trivial solutions with ( n k) ≤ 10 60 \binom{n}{k}\leq 10^{60} or n ≤ 10 6. n\leq 10^{6}. General finiteness results are also known. In 1988, Kiss [15] proved that if k = 2 k=2 and l l is a given odd prime, then the equation has only finitely many positive integral solutions. Using Baker’s method, Brindza [6] showed that equation ( 1) with k = 2 k=2 and l ≥ 3 l\geq 3 has only finitely many positive integral solutions.

In case of the more general equation

(2) |  | ( n k) = ( m l) + d \binom{n}{k}=\binom{m}{l}+d |  |

Blokhuis, Brouwer and de Weger [4] determined all non-trivial solutions with d = 1 d=1 and ( k, l), ( l, k) = ( 2, 3), ( 2, 4), ( 2, 6), ( 3, 4), ( 4, 6), ( 4, 8) (k,l),(l,k)=(2,3),(2,4),(2,6),(3,4),(4,6),(4,8) and ( k, l) = ( 2, 8). (k,l)=(2,8). They provided a complete list of solutions for the above cases and if ( n k) ≤ 10 30. \binom{n}{k}\leq 10^{30}.

n | k | m | l | 11 2 8 3 60 2 23 3 160403633 2 425779 3 6 3 7 2 7 3 9 2 16 3 34 2 27 3 77 2 29 3 86 2 34 3 21 4 n | k | m | l | 19630 3 1587767 2 12 4 32 2 93 4 2417 2 10 5 23 2 22 5 230 2 62 5 3598 2 135 5 26333 2 139 5 28358 2 28 11 6554 2 \begin{array}[]{ll}\small\begin{tabular}[]{|l|l|l|l|}\hline\cr$n$&$k$&$m$&$l$\\ \hline\cr\hline\cr$11$&$2$&$8$&$3$\\ \hline\cr$60$&$2$&$23$&$3$\\ \hline\cr$160403633$&$2$&$425779$&$3$\\ \hline\cr$6$&$3$&$7$&$2$\\ \hline\cr$7$&$3$&$9$&$2$\\ \hline\cr$16$&$3$&$34$&$2$\\ \hline\cr$27$&$3$&$77$&$2$\\ \hline\cr$29$&$3$&$86$&$2$\\ \hline\cr$34$&$3$&$21$&$4$\\ \hline\cr\end{tabular}&\small\begin{tabular}[]{|l|l|l|l|}\hline\cr$n$&$k$&$m$&$l$\\ \hline\cr\hline\cr$19630$&$3$&$1587767$&$2$\\ \hline\cr$12$&$4$&$32$&$2$\\ \hline\cr$93$&$4$&$2417$&$2$\\ \hline\cr$10$&$5$&$23$&$2$\\ \hline\cr$22$&$5$&$230$&$2$\\ \hline\cr$62$&$5$&$3598$&$2$\\ \hline\cr$135$&$5$&$26333$&$2$\\ \hline\cr$139$&$5$&$28358$&$2$\\ \hline\cr$28$&$11$&$6554$&$2$\\ \hline\cr\end{tabular}\end{array}

Table 1. Known solutions of the Diophantine equation ( n k) = ( m l) \binom{n}{k}=\binom{m}{l}.

If d d is not fixed they also obtained some interesting infinite families, an example is given by

 | ( 12 ​ x 2 − 12 ​ x + 3 3) + ( x 2) = ( 24 ​ x 3 − 36 ​ x 2 + 15 ​ x − 1 2). \binom{12x^{2}-12x+3}{3}+\binom{x}{2}=\binom{24x^{3}-36x^{2}+15x-1}{2}. |  |

In 2019, Katsipis [14] completely resolved the case with ( k, l) = ( 8, 2) (k,l)=(8,2) and he also determined the integral solutions if ( k, l), ( l, k) = ( 3, 6) (k,l),(l,k)=(3,6) and d = 1. d=1.

The aim of this paper is to extend results mentioned above and offer some general observations and computational results.

## 2. Main results

We start our discussion with some numerical observations. More precisely, we observed that for certain pairs ( k, l) (k,l) and an integer d d, the congruence

(3) |  | ( n k) ≡ ( m l) + d ( mod p), \binom{n}{k}\equiv\binom{m}{l}+d\pmod{p}, |  |

with suitable chosen prime number p > max ⁡ { k, l } p>\operatorname{max}\{k,l\}, has no solutions. This immediately implies unsolvability in integers of the related Diophantine equation.

###### Theorem 1.

If ( k, l) = ( 2, 4), d ∈ ℤ (k,l)=(2,4),d\in{\mathbb{Z}} and 3 3 is a quadratic non-residue modulo p > 4 p>4, where the p p -adic valuation of 12 ​ d + 1 12d+1 is odd, then congruence ( 3) has no solutions. In particular, equation ( 2) has no solutions in integers.

###### Remark.

Based on the previous theorem we may provide some explicit results, for example if d ≡ u ( mod 75), d\equiv u\pmod{75}, where u ∈ { 7, 12, 17, 22, 32, 37, 42, 47, 57, 62, 67, 72 }, u\in\{7,12,17,22,32,37,42,47,57,62,67,72\}, then equation ( 2) has no solutions in integers with ( k, l) = ( 2, 4). (k,l)=(2,4).

By using elementary number theory we compute all integral solutions of equation ( 2) for some values of k k and d d with l = k l=k and d ≠ 0. d\neq 0. We note that the case k = 2 k=2 is in some sense trivial. Indeed, in this case the solvability of equation ( 5) is equivalent to the existence of integers u, v u,v such that u 2 − v 2 = 8 ​ d u^{2}-v^{2}=8d and u ≡ v ≡ 1 ( mod 2) u\equiv v\equiv 1\pmod{2}. Equivalently, we need to determine integers d 1, d 2 d_{1},d_{2} with d 1 ≤ d 2 d_{1}\leq d_{2} and 8 ​ d = d 1 ​ d 2 8d=d_{1}d_{2} satisfying the conditions

 | d 1 + d 2 ≡ 2 ( mod 4), d 2 − d 1 ≡ 2 ( mod 4). d_{1}+d_{2}\equiv 2\pmod{4},\quad d_{2}-d_{1}\equiv 2\pmod{4}. |  |

Thus, if d d is odd, one can take d 1 = 4 ​ z 1, d 2 = 2 ​ z 2 d_{1}=4z_{1},d_{2}=2z_{2}, where d = z 1 ​ z 2 d=z_{1}z_{2}, i.e., the number of solutions of our equation is at least σ 0 ​ ( d) \sigma_{0}(d), where σ 0 ​ ( n) = ∑ k | n 1 \sigma_{0}(n)=\sum_{k|n}1. If d d is even one possible choice is d 1 = 2, d 2 = 4 ​ d d_{1}=2,d_{2}=4d.

###### Theorem 2.

All integral solutions ( n, m) (n,m) of equation ( 2) with l = k, k ∈ { 3, 4, 5 } l=k,k\in\{3,4,5\} and d ≠ 0, d ∈ { 1, 2, …, 20 } d\neq 0,d\in\{1,2,\ldots,20\} are as follows

( k, d, s ​ o ​ l ​ u ​ t ​ i ​ o ​ n ​ s) (k,d,solutions) | ( k, d, s ​ o ​ l ​ u ​ t ​ i ​ o ​ n ​ s) (k,d,solutions) |

( 3, 3, [( 4, 3)]) \left(3,3,\left[\left(4,3\right)\right]\right) | ( 4, 4, [( 5, 4)]) \left(4,4,\left[\left(5,4\right)\right]\right) |

( 3, 6, [( 5, 4)]) \left(3,6,\left[\left(5,4\right)\right]\right) | ( 4, 10, [( 6, 5)]) \left(4,10,\left[\left(6,5\right)\right]\right) |

( 3, 9, [( 5, 3)]) \left(3,9,\left[\left(5,3\right)\right]\right) | ( 4, 14, [( 6, 4)]) \left(4,14,\left[\left(6,4\right)\right]\right) |

( 3, 10, [( 6, 5)]) \left(3,10,\left[\left(6,5\right)\right]\right) | ( 4, 20, [( 7, 6)]) \left(4,20,\left[\left(7,6\right)\right]\right) |

( 3, 15, [( 7, 6)]) \left(3,15,\left[\left(7,6\right)\right]\right) | ( 5, 5, [( 6, 5)]) \left(5,5,\left[\left(6,5\right)\right]\right) |

( 3, 16, [( 6, 4)]) \left(3,16,\left[\left(6,4\right)\right]\right) | ( 5, 15, [( 7, 6)]) \left(5,15,\left[\left(7,6\right)\right]\right) |

( 3, 19, [( 6, 3)]) \left(3,19,\left[\left(6,3\right)\right]\right) | ( 5, 20, [( 7, 5)]) \left(5,20,\left[\left(7,5\right)\right]\right) |

In the next result we deal with the cases that can be reduced to elliptic curves.

###### Theorem 3.

All integral solutions ( m, n) (m,n) of equation ( 2) with d ∈ { − 3, …, 3 } d\in\{-3,\ldots,3\} and n ≥ k, m ≥ l n\geq k,m\geq l are as follows.

d d | ( k, l) = ( 2, 3) (k,l)=(2,3) |

3 3 | [( 75,368), ( 77,383), ( 421726, 158118758)] \left[\left(75,368\right),\left(77,383\right),\left(421726,158118758\right)\right] |

2 2 | [( 3, 3), ( 4, 4), ( 104,604)] \left[\left(3,3\right),\left(4,4\right),\left(104,604\right)\right] |

1 1 | [( 6, 7), ( 7, 9), ( 16, 34), ( 27, 77), ( 29, 86), ( 260, 2407), ( 665, 9879), ( 19630, 1587767)] \left[\left(6,7\right),\left(7,9\right),\left(16,34\right),\left(27,77\right),\left(29,86\right),\left(260,2407\right),\left(665,9879\right),\left(19630,1587767\right)\right] |

0 0 | [( 3, 2), ( 5, 5), ( 10, 16), ( 22, 56), ( 36,120)] \left[\left(3,2\right),\left(5,5\right),\left(10,16\right),\left(22,56\right),\left(36,120\right)\right] |

− 1 -1 | [( 4, 3), ( 8, 11), ( 23, 60), ( 425779, 160403633)] \left[\left(4,3\right),\left(8,11\right),\left(23,60\right),\left(425779,160403633\right)\right] |

− 2 -2 | [] \left[\right] |

− 3 -3 | [( 4, 2)] \left[\left(4,2\right)\right] |

d | ( k, l) = ( 2, 4) | 3 [] 2 [( 4, 3)] 1 [( 5, 4), ( 7, 9), ( 12, 32), ( 93, 2417)] 0 [( 4, 2), ( 6, 6), ( 10, 21)] − 1 [] − 2 [] − 3 [] d | ( k, l) = ( 2, 6) | 3 [( 7, 5), ( 11, 31), ( 50, 5638)] 2 [( 6, 3)] 1 [] 0 [( 6, 2), ( 8, 8), ( 10, 21), ( 14, 78)] − 1 [( 7, 4)] − 2 [] − 3 [] \begin{array}[]{ll}\small\par\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(2,4)$\\ \hline\cr\hline\cr$3$&$\left[\right]$\\ \hline\cr$2$&$\left[(4,3)\right]$\\ \hline\cr$1$&$\left[(5,4),(7,9),(12,32),(93,2417)\right]$\\ \hline\cr$0$&$\left[(4,2),(6,6),(10,21)\right]$\\ \hline\cr$-1$&$\left[\right]$\\ \hline\cr$-2$&$\left[\right]$\\ \hline\cr$-3$&$\left[\right]$\\ \hline\cr\end{tabular}&\small\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(2,6)$\\ \hline\cr\hline\cr$3$&$\left[(7,5),(11,31),(50,5638)\right]$\\ \hline\cr$2$&$\left[(6,3)\right]$\\ \hline\cr$1$&$\left[\right]$\\ \hline\cr$0$&$\left[(6,2),(8,8),(10,21),(14,78)\right]$\\ \hline\cr$-1$&$\left[(7,4)\right]$\\ \hline\cr$-2$&$\left[\right]$\\ \hline\cr$-3$&$\left[\right]$\\ \hline\cr\end{tabular}\end{array}

d | ( k, l) = ( 2, 8) | 3 [] 2 [( 8, 3)] 1 [( 5, 9), ( 32, 12)] 0 [( 8, 2), ( 10, 10), ( 14, 78), ( 17,221)] − 1 [] − 2 [] − 3 [( 9, 4)] d | ( k, l) = ( 3, 4) | 3 [( 4, 4)] 2 [] 1 [] 0 [( 4, 3), ( 7, 7)] − 1 [( 5, 4), ( 21, 34)] − 2 [] − 3 [] \begin{array}[]{ll}\small\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(2,8)$\\ \hline\cr\hline\cr$3$&$\left[\right]$\\ \hline\cr$2$&$\left[(8,3)\right]$\\ \hline\cr$1$&$\left[(5,9),(32,12)\right]$\\ \hline\cr$0$&$\left[(8,2),(10,10),(14,78),(17,221)\right]$\\ \hline\cr$-1$&$\left[\right]$\\ \hline\cr$-2$&$\left[\right]$\\ \hline\cr$-3$&$\left[(9,4)\right]$\\ \hline\cr\end{tabular}&\small\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(3,4)$\\ \hline\cr\hline\cr$3$&$\left[(4,4)\right]$\\ \hline\cr$2$&$\left[\right]$\\ \hline\cr$1$&$\left[\right]$\\ \hline\cr$0$&$\left[(4,3),(7,7)\right]$\\ \hline\cr$-1$&$\left[(5,4),(21,34)\right]$\\ \hline\cr$-2$&$\left[\right]$\\ \hline\cr$-3$&$\left[\right]$\\ \hline\cr\end{tabular}\end{array}

d | ( k, l) = ( 3, 6) | 3 [( 6, 4), ( 7, 5)] 2 [] 1 [] 0 [( 6, 3), ( 9, 9)] − 1 [] − 2 [] − 3 [( 7, 4)] d | ( k, l) = ( 4, 6) | 3 [] 2 [] 1 [] 0 [( 6, 4), ( 10, 10)] − 1 [] − 2 [( 7, 5)] − 3 [] d | ( k, l) = ( 4, 8) | 3 [] 2 [] 1 [] 0 [( 8, 4), ( 12, 12)] − 1 [] − 2 [] − 3 [] \begin{array}[]{lll}\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(3,6)$\\ \hline\cr\hline\cr$3$&$\left[(6,4),(7,5)\right]$\\ \hline\cr$2$&$\left[\right]$\\ \hline\cr$1$&$\left[\right]$\\ \hline\cr$0$&$\left[(6,3),(9,9)\right]$\\ \hline\cr$-1$&$\left[\right]$\\ \hline\cr$-2$&$\left[\right]$\\ \hline\cr$-3$&$\left[(7,4)\right]$\\ \hline\cr\end{tabular}&\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(4,6)$\\ \hline\cr\hline\cr$3$&$\left[\right]$\\ \hline\cr$2$&$\left[\right]$\\ \hline\cr$1$&$\left[\right]$\\ \hline\cr$0$&$\left[(6,4),(10,10)\right]$\\ \hline\cr$-1$&$\left[\right]$\\ \hline\cr$-2$&$\left[(7,5)\right]$\\ \hline\cr$-3$&$\left[\right]$\\ \hline\cr\end{tabular}&\begin{tabular}[]{|c|l|}\hline\cr$d$&$(k,l)=(4,8)$\\ \hline\cr\hline\cr$3$&$\left[\right]$\\ \hline\cr$2$&$\left[\right]$\\ \hline\cr$1$&$\left[\right]$\\ \hline\cr$0$&$\left[(8,4),(12,12)\right]$\\ \hline\cr$-1$&$\left[\right]$\\ \hline\cr$-2$&$\left[\right]$\\ \hline\cr$-3$&$\left[\right]$\\ \hline\cr\end{tabular}\end{array}

Among the solutions given by Blokhuis, Brouwer and de Weger [4] there are some with ( k, l) = ( 2, 5) (k,l)=(2,5) e.g.:

 | ( 10 5) + 1 = ( 23 2), ( 22 5) + 1 = ( 230 2), ( 62 5) + 1 = ( 3598 2) \binom{10}{5}+1=\binom{23}{2},\quad\binom{22}{5}+1=\binom{230}{2},\quad\binom{62}{5}+1=\binom{3598}{2} |  |

in these cases the problem can be reduced to genus 2 curves.

###### Theorem 4.

All integral solutions ( n, m) (n,m) of equation ( 2) with d ∈ { − 3, …, 3 }, k = 2, l = 5 d\in\{-3,\ldots,3\},k=2,l=5 are as follows.

d d | solutions |

− 3 -3 | [( 3, 6)] \left[(3,6)\right] |

− 2 -2 | [] \left[\right] |

− 1 -1 | [( 11, 8)] \left[(11,8)\right] |

0 0 | [( 2, 5), ( 4, 6), ( 7, 7), ( 78, 15), ( 153, 19)] \left[(2,5),(4,6),(7,7),(78,15),(153,19)\right] |

1 1 | [( 23, 10), ( 230, 22), ( 3598, 62), ( 26333,135), ( 28358,139)] \left[(23,10),(230,22),(3598,62),(26333,135),(28358,139)\right] |

2 2 | [( 3, 5)] \left[(3,5)\right] |

3 3 | [( 31, 11), ( 94, 16), ( 346888,375), ( 356263,379)] \left[(31,11),(94,16),(346888,375),(356263,379)\right] |

Let k ∈ ℕ k\in{\mathbb{N}} be odd. In the following theorem we consider the Diophantine equation

(4) |  | ( f 1 ​ ( x) k) + ( x 2) = ( f 2 ​ ( x) 2) \binom{f_{1}(x)}{k}+\binom{x}{2}=\binom{f_{2}(x)}{2} |  |

in polynomials f 1, f 2 ∈ ℚ ⁡ [x] f_{1},f_{2}\in{\mathbb{Q}}[x] satisfying the condition deg ⁡ f 1 = 2, deg ⁡ f 2 = k \operatorname{deg}f_{1}=2,\operatorname{deg}f_{2}=k. Note that if f 1 ​ ( x), f 2 ​ ( x) f_{1}(x),f_{2}(x) is a solution of ( 4), then due to the identity ( x 2) = ( 1 − x 2) \binom{x}{2}=\binom{1-x}{2}, f 1 ​ ( 1 − x), f 2 ​ ( 1 − x) f_{1}(1-x),f_{2}(1-x) is also a solution. In the sequel we count such pairs of solutions as one. We are motivated by findings presented in [4].

###### Theorem 5.

Let x x be a variable.

1. (1)

For k = 3, 5 k=3,5 equation ( 4) has exactly three solutions.

2. (2)

For k = 7 k=7 equation ( 4) has exactly one solution.

3. (3)

For k ∈ { 9, 11, 13, 15, 17, 19 } k\in\{9,11,13,15,17,19\} equation ( 4) has no solutions.

## 3. Proofs of the theorems

###### Proof of Theorem 1.

In order to get the result it is enough to note that the equation ( y 2) = ( x 4) + d \binom{y}{2}=\binom{x}{4}+d can be rewritten as

 | X 2 − 3 ​ Y 2 = − 2 ​ ( 12 ​ d + 1), X^{2}-3Y^{2}=-2(12d+1), |  |

where X = x 2 − 3 ​ x + 1, Y = 2 ​ y − 1 X=x^{2}-3x+1,Y=2y-1. If 2 ​ ( 12 ​ d + 1) ≡ 0 ( mod p) 2(12d+1)\equiv 0\pmod{p}, then X 2 ≡ 3 ​ Y 2 ( mod p) X^{2}\equiv 3Y^{2}\pmod{p}. Under our assumption on p p we see that 3 is quadratic non-residue modulo p p and congruence ( 3), and hence equation ( 2), has no integer solutions. ∎

Motivated by the result above, we performed numerical search for pairs ( k, l), k ≤ l ≤ 10, d ∈ ℤ (k,l),k\leq l\leq 10,d\in{\mathbb{Z}} and prime numbers p > l p>l such that the congruence ( 3) has no solutions modulo p p. Here are results of our computations.

 | ( k, l) p d ( mod p) ( k, l) p d ( mod p) ( 2, 6) 7 4 ( 6, 8) 11 4 ( 2, 8) 11 7 13 3 13 11 19 4 ( 2, 9) 11 8 ( 6, 9) 11 3, 4, 9 ( 2, 10) 11 7, 8 ( 6, 10) 11 2, 3, 4 13 11 13 10, 11 ( 3, 4) 5 2 19 2, 4 ( 3, 8) 11 5 ( 7, 8) 11 4, 6 ( 3, 10) 11 5 17 11 ( 4, 4) 5 2, 3 19 15 ( 4, 5) 7 3 ( 7, 9) 11 5, 6 ( 4, 6) 7 2, 3 ( 7, 10) 11 4, 5, 6 13 10 13 6 19 2 ( 8, 8) 11 4, 5, 6, 7 ( 4, 8) 11 8, 9 13 2, 11 13 10, 11 17 4, 13 ( 4, 9) 11 7, 8 19 3, 16 13 7 23 7, 16 ( 4, 10) 11 6, 7, 8, 9 ( 8, 9) 11 3, 4, 5, 7 13 6, 10 ( 8, 10) 11 2, 3, 4, 5, 6 23 9 13 4, 7, 10 ( 5, 5) 7 3, 4 19 16 11 3, 8 ( 9, 10) 11 2, 3, 4, 5, 6, 7, 8 ( 5, 6) 7 2, 3, 4 13 4, 6, 7, 8 11 2, 7, 8 17 8, 11, 14 ( 5, 8) 11 5 23 7 ( 5, 9) 11 3, 8 ( 10, 10) 11 2, 3, 4, 5, 6, 7, 8 ( 5, 10) 11 2, 3, 7, 8 13 4, 5, 6, 7, 8, 9 ( 6, 6) 7 2, 3, 4, 5 17 5, 8, 9, 12 11 2, 3, 8, 9 19 3, 5, 14, 16 13 3, 10 23 5, 18 29 6, 23 \begin{array}[]{|l|l|l||l|l|l|}\hline\cr(k,l)&p&d\pmod{p}&(k,l)&p&d\pmod{p}\\ \hline\cr(2,6)&7&4&(6,8)&11&4\\ (2,8)&11&7&&13&3\\ &13&11&&19&4\\ (2,9)&11&8&(6,9)&11&3,4,9\\ (2,10)&11&7,8&(6,10)&11&2,3,4\\ &13&11&&13&10,11\\ (3,4)&5&2&&19&2,4\\ (3,8)&11&5&(7,8)&11&4,6\\ (3,10)&11&5&&17&11\\ (4,4)&5&2,3&&19&15\\ (4,5)&7&3&(7,9)&11&5,6\\ (4,6)&7&2,3&(7,10)&11&4,5,6\\ &13&10&&13&6\\ &19&2&(8,8)&11&4,5,6,7\\ (4,8)&11&8,9&&13&2,11\\ &13&10,11&&17&4,13\\ (4,9)&11&7,8&&19&3,16\\ &13&7&&23&7,16\\ (4,10)&11&6,7,8,9&(8,9)&11&3,4,5,7\\ &13&6,10&(8,10)&11&2,3,4,5,6\\ &23&9&&13&4,7,10\\ (5,5)&7&3,4&&19&16\\ &11&3,8&(9,10)&11&2,3,4,5,6,7,8\\ (5,6)&7&2,3,4&&13&4,6,7,8\\ &11&2,7,8&&17&8,11,14\\ (5,8)&11&5&&23&7\\ (5,9)&11&3,8&(10,10)&11&2,3,4,5,6,7,8\\ (5,10)&11&2,3,7,8&&13&4,5,6,7,8,9\\ (6,6)&7&2,3,4,5&&17&5,8,9,12\\ &11&2,3,8,9&&19&3,5,14,16\\ &13&3,10&&23&5,18\\ &&&&29&6,23\\ \hline\cr\end{array} |  |

Table 2. Pairs ( k, l), k ≤ l ≤ 10 (k,l),k\leq l\leq 10 such that there exist p ∈ ℙ, p ≥ max ⁡ { k, l } p\in\mathbb{P},p\geq\operatorname{max}\{k,l\} such that for some d ∈ { 1, …, p } d\in\{1,\ldots,p\} the congruence ( 3) has no solutions.

###### Proof of Theorem 2.

Here we obtain that

 | ∏ i = 0 k − 1 ( n − i) − ∏ i = 0 k − 1 ( m − i) = d ⋅ k!, \prod_{i=0}^{k-1}(n-i)-\prod_{i=0}^{k-1}(m-i)=d\cdot k!, |  |

and the polynomial is reducible. It follows that

 | ( n − m) ​ F ​ ( n, m) = d ⋅ k!. (n-m)F(n,m)=d\cdot k!. |  |

Hence ( n − m) (n-m) divides d ⋅ k!. d\cdot k!. It remains to solve the one variable polynomial equation

 | F ⁡ ( m + d 1, m) − d ⋅ k! d 1 F(m+d_{1},m)-\frac{d\cdot k!}{d_{1}} |  |

for d 1 | ( d ⋅ k!). d_{1}|(d\cdot k!). ∎

###### Remark.

Let us note that if k = l > 2 k=l>2, then in the considered range, i.e, d ∈ { − 20, …, 20 } d\in\{-20,\ldots,20\} we have found at most one integer solution. It is an interesting problem to look for values of d d such that the equation

(5) |  | ( n k) = ( m k) + d \binom{n}{k}=\binom{m}{k}+d |  |

has more than one solution in positive integers m, n m,n satisfying n > m n>m. In order to construct values of d d such that equation ( 5) has “many” solutions we used the following strategy. First, we computed the set

 | D k:= { ( n k) − ( m k): k < m < n ≤ 10 4 }, D_{k}:=\left\{\binom{n}{k}-\binom{m}{k}:\;k<m<n\leq 10^{4}\right\}, |  |

and then looked for duplications in D k D_{k}. We considered k ∈ { 3, …, 10 } k\in\{3,\ldots,10\}. As one could expect, in the case k = 3 k=3 the number of duplicates is big. In fact, we found 488 values of d d which appeared at least three times in D 3 D_{3}. The smallest value correspond to d = 2180 d=2180 with the solutions ( n, m) = ( 25, 10), ( 33, 28), ( 36, 32) (n,m)=(25,10),(33,28),(36,32). We found only three values of d d such that equation ( 5) has four solutions. The values of d d and the corresponding solutions are as follows:

 | d = 10053736 ( n, m) = ( 398,132), ( 628,572), ( 968,946), ( 990,969), d = 209920964 ( n, m) = ( 1081, 58), ( 1144,617), ( 1242,868), ( 3532, 3498), d = 1928818640 ( n, m) = ( 2266,362), ( 2268,428), ( 3622, 3300), ( 4991, 4831). \begin{array}[]{lll}d=10053736&&(n,m)=(398,132),(628,572),(968,946),(990,969),\\ d=209920964&&(n,m)=(1081,58),(1144,617),(1242,868),(3532,3498),\\ d=1928818640&&(n,m)=(2266,362),(2268,428),(3622,3300),(4991,4831).\end{array} |  |

We strongly believe that the following is true.

###### Conjecture.

For each N ∈ ℕ N\in{\mathbb{N}} there is d N ∈ ℕ d_{N}\in{\mathbb{N}} such that the equation ( n 3) − ( m 3) = d N \binom{n}{3}-\binom{m}{3}=d_{N} has at least N N positive integer solutions.

For k = 4 k=4 we found 1190 values of d d which appeared at least two times in D 4 D_{4}. The smallest value corresponds to d = 680 d=680 with the solutions ( n, m) = ( 13, 7), ( 18, 17) (n,m)=(13,7),(18,17). We found only one value of d d such that equation ( 5) has three solutions. More precisely, for d = 18896570 d=18896570 equation ( 5) has three solutions ( n, m) = ( 185,163), ( 258,251), ( 486,485) (n,m)=(185,163),(258,251),(486,485).

For k = 5 k=5 we found 4 values of d d which appeared at least 2 times in D 5 D_{5}. The values of d d and the corresponding solutions are as follows:

 | d = 146438643 ( n, m) = ( 117, 78), ( 133,118), d = 153852348 ( n, m) = ( 118, 78), ( 133,117), d = 817514347 ( n, m) = ( 160, 53), ( 209,197), d = 2346409884 ( n, m) = ( 197, 53), ( 209,160). \begin{array}[]{lll}d=146438643&&(n,m)=(117,78),(133,118),\\ d=153852348&&(n,m)=(118,78),(133,117),\\ d=817514347&&(n,m)=(160,53),(209,197),\\ d=2346409884&&(n,m)=(197,53),(209,160).\end{array} |  |

For k = 6 k=6 we also found 4 values of d d which appeared at least 2 times in D 6 D_{6}. The values of d d and the corresponding solutions are as follows:

 | d = 3819816 ( n, m) = ( 40, 18), ( 57, 56), d = 32449872 ( n, m) = ( 56, 18), ( 57, 40), d = 66273157776 ( n, m) = ( 193, 66), ( 252,243), d = 268624373556 ( n, m) = ( 243, 66), ( 252,193). \begin{array}[]{lll}d=3819816&&(n,m)=(40,18),(57,56),\\ d=32449872&&(n,m)=(56,18),(57,40),\\ d=66273157776&&(n,m)=(193,66),(252,243),\\ d=268624373556&&(n,m)=(243,66),(252,193).\end{array} |  |

For k = 7 k=7 we found only one value of d ∈ D 7 d\in D_{7} such that equation ( 5) (\ref{keql}) has two solutions. For d = 8008 d=8008 we have solutions ( n, m) = ( 16, 14), ( 17, 16) (n,m)=(16,14),(17,16).

For k = 8, 9, 10 k=8,9,10 there are no duplicates in the set D k D_{k}.

###### Proof of Theorem 3.

All the equations related to this part can be reduced to elliptic curves given is some model.

( k, l) (k,l) | equation | transformation |

(2,3) | Y 2 = X 3 − 36 ​ X 2 + 288 ​ X + 10368 ​ d + 1296 Y^{2}=X^{3}-36X^{2}+288X+10368d+1296 | X = 12 ​ m, Y = 216 ​ n − 108 X=12m,Y=216n-108 |

(2,4) | Y 2 = 3 ​ X ​ ( X − 1) ​ ( X − 2) ​ ( X − 3) + 72 ​ d + 9 Y^{2}=3X(X-1)(X-2)(X-3)+72d+9 | X = m, Y = 6 ​ n − 3 X=m,Y=6n-3 |

(2,6) | Y 2 = X ⁡ ( X + 40) ​ ( X + 60) + 10 4 ⋅ ( 72 ​ d + 9) Y^{2}=X(X+40)(X+60)+10^{4}\cdot(72d+9) | X = 10 ​ m 2 − 50 ​ m, Y = 600 ​ n − 300 X=10m^{2}-50m,Y=600n-300 |

(2,8) | Y 2 = 35 ​ X ​ ( X + 6) ​ ( X + 10) ​ ( X + 12) + 420 2 ​ ( 8 ​ d + 1) Y^{2}=35X(X+6)(X+10)(X+12)+420^{2}(8d+1) | X = m 2 − 7 ​ m, Y = 420 ​ ( 2 ​ n − 1) X=m^{2}-7m,Y=420(2n-1) |

(3,4) | Y 2 = X ⁡ ( X − 4) ​ ( X − 8) − 384 ​ d + 16 Y^{2}=X(X-4)(X-8)-384d+16 | X = 4 ​ n, Y = 4 ​ m 2 − 12 ​ m + 4 X=4n,Y=4m^{2}-12m+4 |

(3,6) | 15 ​ X ​ ( X − 1) ​ ( X + 1) = Y ⁡ ( Y − 3) ​ ( Y + 4) + 90 ​ d 15X(X-1)(X+1)=Y(Y-3)(Y+4)+90d | X = n − 1, Y = ( m − 2) ​ ( m − 3) / 2 X=n-1,Y=(m-2)(m-3)/2 |

(4,6) | Y 2 = X ⁡ ( X + 120) ​ ( X + 180) + 30 4 ⋅ ( 24 ​ d + 1) Y^{2}=X(X+120)(X+180)+30^{4}\cdot(24d+1) | X = 30 ​ m 2 − 150 ​ m, Y = 900 ​ ( n 2 − 3 ​ n + 1) X=30m^{2}-150m,Y=900(n^{2}-3n+1) |

(4,8) | Y 2 = 105 ​ X ​ ( X + 6) ​ ( X + 10) ​ ( X + 12) + 420 2 ​ ( 24 ​ d + 1) Y^{2}=105X(X+6)(X+10)(X+12)+420^{2}(24d+1) | X = m 2 − 7 ​ m, Y = 420 ​ ( n 2 − 3 ​ n + 1) X=m^{2}-7m,Y=420(n^{2}-3n+1) |

Table 3. Elliptic models of certain Diophantine equations of the form ( m k) = ( n l) + d \binom{m}{k}=\binom{n}{l}+d

There exists a number of software implementations for finding integral points on elliptic curves [5, 22]. These procedures are based on a method developed by Stroeker and Tzanakis [28] and independently by Gebel, Pethő and Zimmer [13]. One may follow the transformations provided in [27] to handle these cases. Here we used the Magma procedures IntegralPoints() and IntegralQuarticPoints(). In some cases there exist no solution and we used IsLocallySolvable() and TwoCoverDescent() [7]. In cases related to ( k, l) = ( 3, 6) (k,l)=(3,6) we follow the above mentioned elliptic logarithm method, the cases with d = − 1, 0, 1 d=-1,0,1 were solved earlier as given in the introduction, so it remains to deal with the values d ∈ { − 3, − 2, 2, 3 }. d\in\{-3,-2,2,3\}.

The case d = 2 d=2 yields an elliptic curve with Mordell-Weil rank 3 while the remaining three values of d d yield elliptic curves with Mordell-Weil rank 2; we only provide details for the case d = 2 d=2.

For this case we set u = X u=X, Y = v Y=v and we have the equation

(6) |  | C: g ⁡ ( u, v) = 0, where g ⁡ ( u, v) = 15 ​ u 3 − v 3 + 4 ​ v 2 − 15 ​ u − 3 ​ v − 180, \displaystyle C:g(u,v)=0,\quad\mbox{where}\quad g(u,v)=15u^{3}-v^{3}+4v^{2}-15u-3v-180, |  |

where u = n − 1 u=n-1 and v = 1 2 ​ ( ( m − 5 2) 2 − 1 4) = ( m − 2) ​ ( m − 3) / 2 v=\dfrac{1}{2}\left(\left(m-\dfrac{5}{2}\right)^{2}-\dfrac{1}{4}\right)=(m-2)(m-3)/2 and the Weierstrass model which is birationally equivalent to C C over ℚ {\mathbb{Q}} is

(7) |  | E: y 2 = x 3 − 1575 ​ x − 48749850 =: f ⁡ ( x). \displaystyle E:y^{2}=x^{3}-1575x-48749850=:f(x). |  |

A notation remark: We will use “exponents” C and E on a point to declare whether the point is viewed as one on C C or E E, respectively. Also, we will use ( u, v) (u,v) or ( x, y) (x,y) for the C C -coordinates or the E E -coordinates, respectively.

As already mentioned, E ⁡ ( ℚ) E({\mathbb{Q}}) has rank 3; its free part is generated by the points

 | P 1 E = ( 10905 / 4, − 1137285 / 8), P 2 E = ( 7465 / 9, 616040 / 27), P 3 E = ( 10246 / 25, − 551206 / 125) P_{1}^{E}=\left(10905/4,-1137285/8\right),\;P_{2}^{E}=\left(7465/9,616040/27\right),\;P_{3}^{E}=\left(10246/25,-551206/125\right) |  |

and the torsion subgroup is trivial.

The birational transformation between the models C C and E E is

 | C ∋ P C:= ( u, v) \displaystyle C\ni P^{C}:=(u,v) | ⟶ ( x, y) = ( 𝒳 ⁡ ( u, v), 𝒴 ⁡ ( u, v)):= P E ∈ E \displaystyle\longrightarrow(x,y)=\left(\mathcal{X}(u,v),\mathcal{Y}(u,v)\right):=P^{E}\in E |  |

 | C ∋ P C =: ( 𝒰 ⁡ ( x, y), 𝒱 ⁡ ( x, y)) = ( u, v) \displaystyle C\ni P^{C}=:\left(\mathcal{U}(x,y),\mathcal{V}(x,y)\right)=(u,v) | ⟵ ( x, y) =: P E ∈ E \displaystyle\longleftarrow(x,y)=:P^{E}\in E |  |

with

 | 𝒳 ⁡ ( u, v) = 3 ​ ( 620 ​ u 2 + 235 ​ u ​ v + 106 ​ v 2 − 210 ​ u − 438 ​ v + 1960) ( u + 4) 2, \mathcal{X}(u,v)=\frac{3(620u^{2}+235uv+106v^{2}-210u-438v+1960)}{(u+4)^{2}}, |  |

 | 𝒴 ⁡ ( u, v) = 𝒴 ​ num ​ ( u, v) ( u + 4) 3, \mathcal{Y}(u,v)=\frac{\mathcal{Y}\mbox{num}(u,v)}{(u+4)^{3}}, |  |

where

 | 𝒴 ​ num ​ ( u, v) = \displaystyle\mathcal{Y}\mbox{num}(u,v)= | 3 ​ ( 45795 ​ u 3 + 19080 ​ u 2 ​ v + 7285 ​ u ​ v 2 − 35895 ​ u 2 − 16795 ​ u ​ v − 4568 ​ v 2 + CLOSE \displaystyle 3(45795u^{3}+19080u^{2}v+7285uv^{2}-35895u^{2}-16795uv-4568v^{2}+ |  |

 |  | OPEN + 32940 ​ u + 65744 ​ v − 408000) \displaystyle+32940u+65744v-408000) |  |

and

 | 𝒰 ⁡ ( x, y) \displaystyle\mathcal{U}(x,y) | = \displaystyle= | 4 ​ x 3 − 465 ​ x 2 + 318 ​ x ​ y + 3903030 ​ x − 94455 ​ y + 257567175 − x 3 + 5580 ​ x 2 − 290250 ​ x + 161614575, \displaystyle\frac{4x^{3}-465x^{2}+318xy+3903030x-94455y+257567175}{-x^{3}+5580x^{2}-290250x+161614575}, |  |

 | 𝒱 ⁡ ( x, y) \displaystyle\mathcal{V}(x,y) | = \displaystyle= | 9 ​ x 3 + 7020 ​ x 2 + 705 ​ x ​ y − 9215775 ​ x + 205560 ​ y + 1359589050 − x 3 + 5580 ​ x 2 − 290250 ​ x + 161614575. \displaystyle\frac{9x^{3}+7020x^{2}+705xy-9215775x+205560y+1359589050}{-x^{3}+5580x^{2}-290250x+161614575}. |  |

With the aid of Maple we find out that there is exactly one conjugacy class of Puiseux series v ⁡ ( u) v(u) solving g ⁡ ( u, v) = 0 g(u,v)=0. This unique class contains exactly three series and only the following one has real coefficients:

 | v 1 ​ ( u) = \displaystyle v_{1}(u)= | ζ ​ u + 4 3 + ( 7 135 ​ ζ 2 − 1 3 ​ ζ) ​ u − 1 + 968 443 ​ ζ ​ u − 2 + ( 7 405 ​ ζ 2 − 1 9 ​ ζ) ​ u − 3 \displaystyle\,\zeta u+\frac{4}{3}+\left(\dfrac{7}{135}\zeta^{2}-\dfrac{1}{3}\zeta\right)u^{-1}+\dfrac{968}{443}\zeta u^{-2}+\left(\dfrac{7}{405}\zeta^{2}-\dfrac{1}{9}\zeta\right)u^{-3} |  |

(9) |  |  | + ( 6776 32805 ​ ζ 2 − 1936 729 ​ ζ) ​ u − 4 + …. \displaystyle+\left(\dfrac{6776}{32805}\zeta^{2}-\dfrac{1936}{729}\zeta\right)u^{-4}+\ldots. |  |

Here ζ \zeta is the cubic root of 15 15. For every real solution of g ⁡ ( u, v) = 0 g(u,v)=0 with | u | ≥ 3 |u|\geq 3 it is true that v = v 1 ​ ( u) v=v_{1}(u) (according to Lemma 8.3.1 in [29]).

Then the point P 0 E P_{0}^{E} that plays a crucial role in the resolution (see [29, Definition 8.3.3]) is

 | P 0 E = ( 318 ​ ζ 2 + 705 ​ ζ + 1860, 21855 ​ ζ 2 + 57240 ​ ζ + 137385). P_{0}^{E}=(318\zeta^{2}+705\zeta+1860,21855\zeta^{2}+57240\zeta+137385). |  |

Referring to the discussion of Section 1 of [14], we consider the linear form

 | L ⁡ ( P) = ( m 0 + s t) ​ ω 1 + m 1 ​ 𝔩 ​ ( P 1) + m 2 ​ 𝔩 ​ ( P 2) + m 3 ​ 𝔩 ​ ( P 3) ± 𝔩 ⁡ ( P 0). L(P)=\left(m_{0}+\dfrac{s}{t}\right)\omega_{1}+m_{1}{\mathfrak{l}}(P_{1})+m_{2}{\mathfrak{l}}(P_{2})+m_{3}{\mathfrak{l}}(P_{3})\pm{\mathfrak{l}}(P_{0}). |  |

Since f ⁡ ( X) f(X) has only one real root, namely e 1 ≈ 366.7439448002 e_{1}\approx 366.7439448002, we have E ​ ( ℝ) = E 0 ​ ( ℝ) E({\mathbb{R}})=E_{0}({\mathbb{R}}), therefore 𝔩 ⁡ ( P i) \mathfrak{l}(P_{i}) coincides with the elliptic logarithm of P i E P_{i}^{E} for i = 1, …, 3 i=1,\ldots,3 (see Chapter 3 of [29], especially, Theorem 3.5.2). On the other hand, P 0 E P_{0}^{E} has irrational coordinates. As Magma does not possess a routine for calculating elliptic logarithms of non-rational points, we wrote our own routine in Maple for computing 𝔩 {\mathfrak{l}} -values of points with algebraic coordinates. Thus we compute

 | 𝔩 ⁡ ( P 1) ≈ 0.0191558345, 𝔩 ⁡ ( P 2) ≈ − 0.0349501519, \mathfrak{l}(P_{1})\approx 0.0191558345,\quad\mathfrak{l}(P_{2})\approx-0.0349501519, |  |

 | 𝔩 ⁡ ( P 3) ≈ 0.0532999952, 𝔩 ⁡ ( P 0) ≈ − 0.00763363355. \mathfrak{l}(P_{3})\approx 0.0532999952,\quad\mathfrak{l}(P_{0})\approx-0.00763363355. |  |

Note that the four points P i E, i = 0, 1, …, 3 P_{i}^{E},\,i=0,1,\ldots,3 are ℤ {\mathbb{Z}} -linearly independent because their regulator is non-zero (see [20, Theorem 8.1]). Therefore our linear form L ⁡ ( P) L(P) falls under the scope of the second “bullet” in [29, page 99] and we have r 0 = 1 r_{0}=1, s / t = s 0 / t 0 = 0 / 1 = 0 s/t=s_{0}/t_{0}=0/1=0, d = 1 d=1, r = 4 r=4, n i = m i n_{i}=m_{i} for i = 1, …, 3 i=1,\ldots,3, n 4 = ± 1 n_{4}=\pm 1, n 0 = m 0 n_{0}=m_{0}, k = r + 1 = 4 k=r+1=4, η = 1 \eta=1 and N = max 0 ≤ i ≤ 4 ⁡ | n i | ≤ r 0 ​ max ⁡ { M, 1 2 ​ r ​ M + 1 } + 1 2 ​ η ​ r 0 = 3 2 ​ M + 3 2 N=\max_{0\leq i\leq 4}|n_{i}|\leq r_{0}\max\{M,\frac{1}{2}rM+1\}+\frac{1}{2}\eta r_{0}=\frac{3}{2}M+\frac{3}{2}, so that, in the relation (9.6) of [29] we can take

(10) |  | α = 3 / 2, β = 3 / 2. \alpha=3/2,\beta=3/2. |  |

We compute the canonical heights of P 1 E, P 2 E, P 3 E P_{1}^{E},P_{2}^{E},P_{3}^{E} using Magma 1 1 1 For the definition of the canonical height we follow J.H. Silverman; as a consequence the values displayed here for the canonical heights are the halves of those computed by Magma and the least eigenvalue ρ \rho of the height-pairing matrix ℋ \mathcal{H} below, is half that computed by Magma; cf. “Warning” at bottom of p. 106 in [29]. and for the canonical height of P 0 E P_{0}^{E} we confine ourselves to the upper bound by applying [29, Proposition 2.6.4]. Thus we have

 | h ^ ​ ( P 1 E) ≈ 3.6037959076, h ^ ​ ( P 2 E) ≈ 3.7072405585, \hat{h}(P_{1}^{E})\approx 3.6037959076,\quad\hat{h}(P_{2}^{E})\approx 3.7072405585, |  |

 | h ^ ​ ( P 3 E) ≈ 4.8663287093, h ^ ​ ( P 0 E) ≤ 8.022765298. \hat{h}(P_{3}^{E})\approx 4.8663287093,\quad\hat{h}(P_{0}^{E})\leq 8.022765298\,. |  |

The corresponding height-pairing matrix for the particular Mordell-Weil basis is

 | ℋ ≈ ( 3.6037959076 − 1.0424191872 − 1.2722619781 − 1.0424191872 3.7072405585 3.0174040388 − 1.2722619781 3.0174040388 4.8663287093) \mathcal{H}\approx\left(\begin{array}[]{rrr}3.6037959076&-1.0424191872&-1.2722619781\\ -1.0424191872&3.7072405585&3.0174040388\\ -1.2722619781&3.0174040388&4.8663287093\end{array}\right) |  |

with minimum eigenvalue

(11) |  | ρ ≈ 1.2142056695. \rho\approx 1.2142056695. |  |

Next we apply [29, Proposition 2.6.3] in order to compute a positive constant γ \gamma with the property that h ^ ​ ( P E) − 1 2 ​ h ​ ( x ⁡ ( P)) ≤ γ \hat{h}(P^{E})-\frac{1}{2}h(x(P))\leq\gamma for every point P E = ( x ⁡ ( P), y ⁡ ( P)) ∈ E ⁡ ( ℚ) P^{E}=(x(P),y(P))\in E({\mathbb{Q}}), where h h denotes Weil height; 2 2 2 In the notation of [29, Proposition 2.6.3], as a curve D D we take the minimal model of E E which is E E itself. it turns out that

(12) |  | γ ≈ 4.8726444820. \gamma\approx 4.8726444820. |  |

Finally, we have to specify the constants c 12, c 13, c 14, c 15 c_{12},c_{13},c_{14},c_{15} defined in [29, Theorem 9.1.2]. This can be carried out almost automatically with a Maple program. In this way we compute

(13) |  | c 12 ≈ 1.07690 ⋅ 10 27, c 13 ≈ 4.04702 ⋅ 10 162, c 14 ≈ 2.09861, c 15 ≈ 24.99686. c_{12}\approx 1.07690\cdot 10^{27},\quad c_{13}\approx 4.04702\cdot 10^{162},\quad\\ c_{14}\approx 2.09861,\quad c_{15}\approx 24.99686. |  |

According to [29, Theorem 9.1.3], applied to “case of Theorem 8.7.2”, if | u ⁡ ( P) | ≥ max ⁡ { B 2, B 3 } |u(P)|\geq\max\{B_{2},B_{3}\}, where B 2 B_{2} and B 3 B_{3} are explicit positive constants, then either M ≤ c 12 M\leq c_{12}, where c 12 c_{12} is an explicit constant, or

(14) |  | ρ ​ M 2 ≤ c 11 ​ c 13 2 ​ θ ​ ( log ⁡ ( α ​ M + β) + c 14) ​ ( log ⁡ log ⁡ ( α ​ M + β) + c 15) r + 3 + γ + c 11 2 ​ θ ​ log ​ c 9 1 + θ + 1 2 ​ c 10, \rho M^{2}\leq\frac{c_{11}c_{13}}{2\theta}(\log(\alpha M+\beta)+c_{14})(\log\log(\alpha M+\beta)+c_{15})^{r+3}+\gamma+\frac{c_{11}}{2\theta}\log\frac{c_{9}}{1+\theta}+\textstyle{\frac{1}{2}}c_{10}, |  |

where all constants involved in it are explicit. More specifically, (in a similar way as in Appendix B in [14] for the case of d = ( N 3 − N) / 6 d=(N^{3}-N)/6),

 | B 2 = 4, B 3 = 5, θ = 1, c 9 = 0.17, c 10 = log ⁡ ( 11800), c 11 = 2. B_{2}=4,\quad B_{3}=5,\quad\theta=1,\quad c_{9}=0.17,\quad c_{10}=\log(11800),\quad c_{11}=2. |  |

So, in view of ( 14) and ( 10), ( 11), ( 12), ( 13), we conclude that, if | u ⁡ ( P) | ≥ 5 |u(P)|\geq 5, then either M ≤ c 12 M\leq c_{12} or

 | 1.2142056695 ⋅ M 2 ≤ \displaystyle 1.2142056695\cdot M^{2}\leq |  |

 |  |  | 4.04 ⋅ 10 162 ⋅ ( log ⁡ ( 1.5 ​ M + 1.5) + 2.0986) ⋅ ( log ⁡ ( log ⁡ ( 1.5 ​ M + 1.5)) + 24.9968) 6 + 7.09542. \displaystyle 4.04\cdot 10^{162}\cdot(\log(1.5M+1.5)+2.0986)\cdot(\log(\log(1.5M+1.5))+24.9968)^{6}+7.09542. |  |

But for all M ≥ 6.64 ⋅ 10 86 M\geq 6.64\cdot 10^{86}, we check that the left-hand side is strictly larger than the right-hand side which implies that M < 6.64 ⋅ 10 86 M<6.64\cdot 10^{86}, therefore

(15) |  | M ≤ max ⁡ { c 12, 6.64 ⋅ 10 86 } = 6.64 ⋅ 10 86 provided that | u ⁡ ( P) | ≥ 5. M\leq\max\{c_{12},\;6.64\cdot 10^{86}\}=6.64\cdot 10^{86}\quad\mbox{provided that $|u(P)|\geq 5$.} |  |

An easy straightforward computation shows that P C = ( − 4, − 9) P^{C}=(-4,-9) is the only one integer point with | u ⁡ ( P) | ≤ 4 |u(P)|\leq 4 (equivalently, the integer solution ( u, v) (u,v) of ( 6) with | u | ≤ 4 |u|\leq 4).

In order to find explicitly all points P C P^{C} with | u ⁡ ( P) | ≥ 5 |u(P)|\geq 5 it is necessary to reduce the huge upper bound ( 15) to an upper bound of manageable size. This is accomplished with LLL-algorithm [16], in a similar way as in Appendix D in [14], and we obtain the reduced bound M ≤ 10 M\leq 10. Therefore, we have to check which points

 | P E = m 1 ​ P 1 E + m 2 ​ P 2 E + m 3 ​ P 3 E, with max 1 ≤ i ≤ 3 ⁡ | m i | ≤ 10, P^{E}=m_{1}P_{1}^{E}+m_{2}P_{2}^{E}+m_{3}P_{3}^{E},\quad\mbox{with $\max_{1\leq i\leq 3}|m_{i}|\leq 10,$} |  |

have the property that P E = ( x, y) P^{E}=(x,y) maps via the transformation () to a point P C = ( u, v) ∈ C P^{C}=(u,v)\in C with integer coordinates. We remark here that every point P C P^{C} with u ⁡ ( P) u(P) integer and | u ⁡ ( P) | ≥ 5 |u(P)|\geq 5 is obtained in this way, but the converse is not necessarily true; i.e. if max 1 ≤ i ≤ 3 ⁡ | m i | ≤ 10 \max_{1\leq i\leq 3}|m_{i}|\leq 10 and the above P E P^{E} maps to P C P^{C} with integer coordinates, it is not necessarily true that | u ⁡ ( P) | ≥ 5 |u(P)|\geq 5. After a computational search we find the only one point P C = ( − 4, − 9) P^{C}=(-4,-9) which corresponds to the zero point 𝒪 ∈ E \mathcal{O}\in E.

So no integral solution ( m, n) (m,n) (with n ≥ k n\geq k and m ≥ l m\geq l) of equation ( 2) with d = 2 d=2 exists.

For the other three cases we provide some details in the tables below:

 | d a ⁡ ( d) r Generators ρ e 1 − 2 − 49559850 2 P 1 = ( 956289 / 4, 935155287 / 8) 1.499191 368.748212 P 2 = ( 198006 / 169, − 86688954 / 2197) − 3 − 111271725 2 P 1 = ( 1230, − 41805) 2.568215 482.072907 P 2 = ( 221597697975 / 91145209, OPEN 103896688780607535 / 870163310323) 3 − 110056725 2 P 1 = ( 1072825 / 2116, − 429530005 / 97336) 1.786872 480.319851 P 2 = ( 16866855 / 34969, − 7734674565 / 6539203) \begin{array}[]{|l|l|l|l|l|l|}\hline\cr d&a(d)&r&\mbox{Generators}&\rho&e_{1}\\ \hline\cr-2&-49559850&2&P_{1}=(956289/4,935155287/8)&1.499191&368.748212\\ &&&P_{2}=(198006/169,-86688954/2197)&&\\ -3&-111271725&2&P_{1}=(1230,-41805)&2.568215&482.072907\\ &&&P_{2}=(221597697975/91145209,&&\\ &&&\quad\quad 103896688780607535/870163310323)&&\\ 3&-110056725&2&P_{1}=(1072825/2116,-429530005/97336)&1.786872&480.319851\\ &&&P_{2}=(16866855/34969,&&\\ &&&\quad\quad-7734674565/6539203)&&\\ \hline\cr\end{array} |  |

Table 4. C: 15 ​ u 3 − v 3 + 4 ​ v 2 − 15 ​ u − 3 ​ v − 90 ​ d C:15u^{3}-v^{3}+4v^{2}-15u-3v-90d and E: y 2 = x 3 − 1575 ​ x + a ⁡ ( d) E:y^{2}=x^{3}-1575x+a(d)

 | d B ⁡ ( M): Initial bound Reduced bound − 2 5.06 ⋅ 10 62 6 − 3 8.66 ⋅ 10 62 5 3 9.07 ⋅ 10 62 5 \begin{array}[]{|c|c|c|}\hline\cr d&B(M):\mbox{Initial bound}&\mbox{Reduced bound}\\ \hline\cr-2&5.06\cdot 10^{62}&6\\ -3&8.66\cdot 10^{62}&5\\ 3&9.07\cdot 10^{62}&5\\ \hline\cr\end{array} |  |

Table 5. Upper bounds of M M.

 | d P E = ( x, y) P C = ( u, v) − 2 𝒪 ( − 2, 6) − 3 𝒪 ( 3, 10) 3 𝒪, ( 16155, − 2053305) ( 3, 6), ( 4, 10) \begin{array}[]{|c|c|c|}\hline\cr d&P^{E}=(x,y)&P^{C}=(u,v)\\ \hline\cr-2&\mathcal{O}&(-2,6)\\ -3&\mathcal{O}&(3,10)\\ 3&\mathcal{O},\;(16155,-2053305)&(3,6),\;(4,10)\\ \hline\cr\end{array} |  |

Table 6. All points P E = Σ i ​ m i ​ P i E P^{E}=\Sigma_{i}m_{i}P_{i}^{E} with P C = ( u, v) ∈ ℤ × ℤ P^{C}=(u,v)\in{\mathbb{Z}}\times{\mathbb{Z}}.

∎

###### Proof of Theorem 4.

We provide details only in case of d = 3, d=3, here the rank of the Jacobian is 6 (like in case of d = 1 d=1). Equation ( 2) with d = 3 d=3 defines the hyperelliptic curve

 | y 2 = 15 ​ x ​ ( x − 1) ​ ( x − 2) ​ ( x − 3) ​ ( x − 4) + 75 2. y^{2}=15x(x-1)(x-2)(x-3)(x-4)+75^{2}. |  |

Based on Stoll’s papers [23], [24], [25] one can determine generators for the Mordell-Weil group by using Magma [5]. We obtain that J ⁡ ( ℚ) J(\mathbb{Q}) is free of rank 6 6 with Mordell-Weil basis given by (in Mumford representation)

 | D 1 = < x − 4, − 75 >, \displaystyle D_{1}=<x-4,-75>, |  |

 | D 2 = < x − 3, 75 >, \displaystyle D_{2}=<x-3,75>, |  |

 | D 3 = < x − 1, − 75 >, \displaystyle D_{3}=<x-1,-75>, |  |

 | D 4 = < x, 75 >, \displaystyle D_{4}=<x,75>, |  |

 | D 5 = < x 2 − 7 ​ x + 30,195 >, \displaystyle D_{5}=<x^{2}-7x+30,195>, |  |

 | D 6 = < x 2 − 3 x + 20, − 30 x − 45 > \displaystyle D_{6}=<x^{2}-3x+20,-30x-45> |  |

and the torsion subgroup is trivial. We apply Baker’s method [2] to get a large upper bound for log ⁡ | x |, \log|x|, here we use the improvements given in [8] and [12]. It follows that

 | log ⁡ | x | ≤ 1.028 × 10 612. \log|x|\leq 1.028\times 10^{612}. |  |

We have from Corollary 3.2 of [12] that every integral point on the curve can be expressed in the form

 | P − ∞ = ∑ i = 1 6 n i ​ D i P-\infty=\sum_{i=1}^{6}n_{i}D_{i} |  |

with ‖ ( n 1, n 2, n 3, n 4, n 5, n 6) ‖ ≤ 1.92 × 10 306 =: N. ||(n_{1},n_{2},n_{3},n_{4},n_{5},n_{6})||\leq 1.92\times 10^{306}=:N. Proposition 6.2 in [12] gives an estimate for the precision we need to compute the appropriate matrices, this bound is as follows

 | ( ( 1 / 5) ​ ( 48 ​ r ​ N ​ t + 12 ​ r ​ N + 5 ​ N + 48)) ( r + 4) / 4 ≈ 2.6 × 10 769, ((1/5)(48\sqrt{r}Nt+12\sqrt{r}N+5N+48))^{(r+4)/4}\approx 2.6\times 10^{769}, |  |

where in our case r = 6 r=6 and t = 1. t=1. We choose to compute the period matrix and the hyperelliptic logarithms with 1500 digits of precision. The hyperelliptic logarithms of the divisors D i D_{i} are given by

 | φ ⁡ ( D 1) \displaystyle\varphi(D_{1}) | = \displaystyle= | ( 0.087945 ​ … + i ​ 0.112834 ​ …, − 0.473844 ​ … − i ​ 0.741784 ​ …) ∈ ℂ 2, \displaystyle(0.087945\ldots+i0.112834\ldots,-0.473844\ldots-i0.741784\ldots)\in\mathbb{C}^{2}, |  |

 | φ ⁡ ( D 2) \displaystyle\varphi(D_{2}) | = \displaystyle= | ( 0.114612 ​ … + i ​ 0.112834 ​ …, − 0.420527 ​ … − i ​ 0.741784 ​ …) ∈ ℂ 2, \displaystyle(0.114612\ldots+i0.112834\ldots,-0.420527\ldots-i0.741784\ldots)\in\mathbb{C}^{2}, |  |

 | φ ⁡ ( D 3) \displaystyle\varphi(D_{3}) | = \displaystyle= | ( − 0.044486 ​ … + i ​ 1.333456 ​ …, − 0.416321 ​ … + i ​ 5.329970 ​ …) ∈ ℂ 2, \displaystyle(-0.044486\ldots+i1.333456\ldots,-0.416321\ldots+i5.329970\ldots)\in\mathbb{C}^{2}, |  |

 | φ ⁡ ( D 4) \displaystyle\varphi(D_{4}) | = \displaystyle= | ( 0.127905 ​ … + i ​ 0.112834 ​ …, − 0.413878 ​ … − i ​ 0.741784 ​ …) ∈ ℂ 2, \displaystyle(0.127905\ldots+i0.112834\ldots,-0.413878\ldots-i0.741784\ldots)\in\mathbb{C}^{2}, |  |

 | φ ⁡ ( D 5) \displaystyle\varphi(D_{5}) | = \displaystyle= | ( − 0.118415 ​ … + i ​ 0.037611 ​ …, − 0.857076 ​ … − i ​ 0.247261 ​ …) ∈ ℂ 2, \displaystyle(-0.118415\ldots+i0.037611\ldots,-0.857076\ldots-i0.247261\ldots)\in\mathbb{C}^{2}, |  |

 | φ ⁡ ( D 6) \displaystyle\varphi(D_{6}) | = \displaystyle= | ( 0.128537 ​ … + i ​ 0.075223 ​ …, − 0.173077 ​ … − i ​ 0.494522 ​ …) ∈ ℂ 2. \displaystyle(0.128537\ldots+i0.075223\ldots,-0.173077\ldots-i0.494522\ldots)\in\mathbb{C}^{2}. |  |

We need now to choose an integer K K that is larger than the constant given by Proposition 6.2 in [12]. Setting K = 10 1300 K=10^{1300} we get a new bound 126.98 126.98 for ‖ ( n 1, n 2, n 3, n 4, n 5, n 6) ‖. ||(n_{1},n_{2},n_{3},n_{4},n_{5},n_{6})||. We repeat the reduction process with K = 10 16 K=10^{16} that yields a better bound, namely 15.6. 15.6. Two more steps with K = 6 × 10 11 K=6\times 10^{11} and K = 2 × 10 11 K=2\times 10^{11} provide the bounds 13.94 13.94 and 13.8. 13.8. It remains to compute all possible expressions of the form

 | n 1 ​ D 1 + … + n 6 ​ D 6 n_{1}D_{1}+\ldots+n_{6}D_{6} |  |

with ‖ ( n 1, n 2, n 3, n 4, n 5, n 6) ‖ ≤ 13.8. ||(n_{1},n_{2},n_{3},n_{4},n_{5},n_{6})||\leq 13.8. We performed a parallel computation to enumerate linear combinations coming from integral points on a machine having 12 cores. The computation took 3 hours and 23 minutes. We obtained the following non-trivial solutions

 | ( 11 5) + 3 \displaystyle\binom{11}{5}+3 | = \displaystyle= | ( 31 2), \displaystyle\binom{31}{2}, |  |

 | ( 16 5) + 3 \displaystyle\binom{16}{5}+3 | = \displaystyle= | ( 94 2), \displaystyle\binom{94}{2}, |  |

 | ( 375 5) + 3 \displaystyle\binom{375}{5}+3 | = \displaystyle= | ( 346888 2), \displaystyle\binom{346888}{2}, |  |

 | ( 379 5) + 3 \displaystyle\binom{379}{5}+3 | = \displaystyle= | ( 356263 2). \displaystyle\binom{356263}{2}. |  |

If d = 1, d=1, then the rank of the Jacobian is 6 and the Baker bound is log ⁡ | x | ≤ 1.225 × 10 532 \log|x|\leq 1.225\times 10^{532} and we have that ‖ ( n 1, n 2, n 3, n 4, n 5, n 6) ‖ ≤ 2.23 × 10 266. ||(n_{1},n_{2},n_{3},n_{4},n_{5},n_{6})||\leq 2.23\times 10^{266}. In three steps it is reduced to 14.97. 14.97. In this case the non-trivial solutions are as follows

 | ( 10 5) + 1 \displaystyle\binom{10}{5}+1 | = \displaystyle= | ( 23 2), \displaystyle\binom{23}{2}, |  |

 | ( 22 5) + 1 \displaystyle\binom{22}{5}+1 | = \displaystyle= | ( 230 2), \displaystyle\binom{230}{2}, |  |

 | ( 62 5) + 1 \displaystyle\binom{62}{5}+1 | = \displaystyle= | ( 3598 2), \displaystyle\binom{3598}{2}, |  |

 | ( 135 5) + 1 \displaystyle\binom{135}{5}+1 | = \displaystyle= | ( 26333 2), \displaystyle\binom{26333}{2}, |  |

 | ( 139 5) + 1 \displaystyle\binom{139}{5}+1 | = \displaystyle= | ( 28358 2). \displaystyle\binom{28358}{2}. |  |

If d = − 3, − 1, 2, d=-3,-1,2, then the rank of the Jacobian is 3, we followed the arguments given in [8] and [11] to obtain a large bound for the size of possible integral solutions. We present them in the table below.

 | d bound for ​ log ⁡ | x | − 3 2.91 ⋅ 10 608 − 1 1.21 ⋅ 10 552 2 3.25 ⋅ 10 590 \begin{array}[]{|c|c|}\hline\cr d&\mbox{bound for}\;\log|x|\\ \hline\cr-3&2.91\cdot 10^{608}\\ -1&1.21\cdot 10^{552}\\ 2&3.25\cdot 10^{590}\\ \hline\cr\end{array} |  |

Table 7. Upper bounds for log ⁡ | x | \log|x|.

In all three cases the rank of the Jacobians are equal to 3 and the torsion subgroup is trivial hence all points can be written as

 | n 1 ​ D 1 + n 2 ​ D 2 + n 3 ​ D 3, n_{1}D_{1}+n_{2}D_{2}+n_{3}D_{3}, |  |

where n i ∈ ℤ. n_{i}\in\mathbb{Z}. Using the previously applied hyperelliptic logarithm method the initial large upper bounds for max ⁡ { | n i | } \max\{|n_{i}|\} can be significantly reduced. If d = − 3, d=-3, then after one reduction step we get the bound 64 and other two steps make it 7. The only pair of integral points we obtain is given by ( 6, ± 75). (6,\pm 75). Therefore we have

 | ( 3 2) = ( 6 5) − 3. \binom{3}{2}=\binom{6}{5}-3. |  |

If d = − 1, d=-1, then first we obtain a reduced bound 51 and finally it follows that max ⁡ { | n i | } ≤ 5. \max\{|n_{i}|\}\leq 5. The complete list of integral points is given by ( 5, ± 15), ( 8, ± 315). (5,\pm 15),(8,\pm 315). Thus we obtain

 | ( 11 2) = ( 8 5) − 1. \binom{11}{2}=\binom{8}{5}-1. |  |

Finally, in case of d = 2 d=2 the first reduction yields a bound 58 and the third one provides 6. The complete set of integral solutions is { ( − 1, ± 45), ( 5, ± 75) }, \{(-1,\pm 45),(5,\pm 75)\}, so we do not get non-trivial solution of ( 2).

If d = − 2, d=-2, then the rank of the Jacobian is 1, therefore classical Chabauty’s method [9] can be applied, it is now implemented in Magma [5]. We obtain that the equation ( n 2) = ( m 5) − 2 \binom{n}{2}=\binom{m}{5}-2 has no non-trivial solution. ∎

###### Remark.

Let

 | C d: y 2 = 15 ​ x ​ ( x − 1) ​ ( x − 2) ​ ( x − 3) ​ ( x − 4) + 15 2 ​ ( 8 ​ d + 1) C_{d}:\;y^{2}=15x(x-1)(x-2)(x-3)(x-4)+15^{2}(8d+1) |  |

and write J d:= Jac ⁡ ( C d) J_{d}:=\operatorname{Jac}(C_{d}). The curve C d C_{d} is isomorphic to the curve defined by the equation ( y 2) = ( x 5) + d \binom{y}{2}=\binom{x}{5}+d. We computed upper bounds for the numbers r d = rank ⁡ J d ​ ( ℚ) r_{d}=\operatorname{rank}J_{d}({\mathbb{Q}}) using the Magma procedure RankBound. We obtained the following data

 | i the value of d such that ​ r d ≤ i 0 − 45, − 40, − 39, − 37, − 34, − 10, − 9, − 4, 8, 25, 26, 40, 47 1 − 47, − 36, − 33, − 31, − 28, − 26, − 25, − 22, − 14, − 13, − 8, − 5, − 2, 5, 11, 17, 20, 29, 32, 41, 50 2 − 50, − 46, − 41, − 38, − 32, − 30, − 29, − 24, − 23, − 19, − 16, − 7, 4, 13 14, 23, 30, 31, 38, 43, 44 3 − 48, − 44, − 43, − 42, − 35, − 21, − 20, − 15, − 11, − 3, − 1, 2, 7, 16, 18 19, 33, 35, 39, 42, 48 4 − 49, − 27, − 18, − 17, − 12, − 6, 9, 12, 22, 24, 34, 37, 46, 49 5 27, 36 6 0, 1, 3, 6, 10, 15, 45 7 21, 28 \begin{array}[]{|l|l|}\hline\cr i&\mbox{the value of $d$ such that}\;r_{d}\leq i\\ \hline\cr 0&-45,-40,-39,-37,-34,-10,-9,-4,8,25,26,40,47\\ 1&-47,-36,-33,-31,-28,-26,-25,-22,-14,-13,-8,-5,-2,5,\\ &11,17,20,29,32,41,50\\ 2&-50,-46,-41,-38,-32,-30,-29,-24,-23,-19,-16,-7,4,13\\ &14,23,30,31,38,43,44\\ 3&-48,-44,-43,-42,-35,-21,-20,-15,-11,-3,-1,2,7,16,18\\ &19,33,35,39,42,48\\ 4&-49,-27,-18,-17,-12,-6,9,12,22,24,34,37,46,49\\ 5&27,36\\ 6&0,1,3,6,10,15,45\\ 7&21,28\\ \hline\cr\end{array} |  |

Table 8. Upper bounds for the rank of Jacobian of the curve C d C_{d} for d ∈ { − 50, …, 50 } d\in\{-50,\ldots,50\}.

We checked that for i ∈ { 0, 4, 5, 6, 7 } i\in\{0,4,5,6,7\} the upper bounds computed by RankBound are actually equal to the ranks.

Let us note that 21 = ( 7 2) 21=\binom{7}{2} and 28 = ( 8 2) 28=\binom{8}{2}. We checked that in both cases the rank is equal to 7. This follows from the existence of seven independent divisors in J d ​ ( ℚ) J_{d}({\mathbb{Q}}). They are as follows:

 | d = 21; \displaystyle d=21;\; | < x − 3, − 345 >, < x − 1, − 345 >, < x − 4,345 >, < x, 345 >, \displaystyle<x-3,-345>,<x-1,-345>,<x-4,345>,<x,345>, |  |

 |  | < x + 3,285 >, < x + 4,135 >, < x − 11,975 >, < x 2 + x + 30, − 30 x + 165 >, \displaystyle<x+3,285>,<x+4,135>,<x-11,975>,<x^{2}+x+30,-30x+165>, |  |

 | d = 28; \displaystyle d=28;\; | < x − 3,225 >, < x − 1, − 225 >, < x − 4,225 >, < x − 12, 1215 >, \displaystyle<x-3,225>,<x-1,-225>,<x-4,225>,<x-12,1215>, |  |

 |  | < x − 17, − 3345 >, < x, 225 >, < x 2 − x + 18, − 135 >. \displaystyle<x-17,-3345>,<x,225>,<x^{2}-x+18,-135>. |  |

We also looked for high rank Jacobians for further values of d d of the form ( w 2). \binom{w}{2}. For d = 66 = ( 12 2) d=66=\binom{12}{2} we obtained the equality r 66 = 8 r_{66}=8 with the following independent divisors

 |  | < x − 3, − 345 >, < x − 1, − 345 >, < x − 4,345 >, < x, 345 >, \displaystyle<x-3,-345>,<x-1,-345>,<x-4,345>,<x,345>, |  |

 |  | < x + 3,285 >, < x + 4,135 >, < x − 11,975 >, < x 2 + x + 30, − 30 x + 165 >. \displaystyle<x+3,285>,<x+4,135>,<x-11,975>,<x^{2}+x+30,-30x+165>. |  |

The torsion part of J 66 ​ ( ℚ) J_{66}({\mathbb{Q}}) is trivial. We conjecture that the only solutions in positive integers of the equation ( y 2) = ( x 5) + 66 \binom{y}{2}=\binom{x}{5}+66 are

 | ( x, y) = \displaystyle(x,y)= | ( 1, 23), ( 2, 23), ( 3, 23), ( 4, 23), ( 11, 65), ( 28,887), \displaystyle(1,23),(2,23),(3,23),(4,23),(11,65),(28,887), |  |

 |  | ( 7935, 1447264765), ( 7939, 1449089815). \displaystyle(7935,1447264765),(7939,1449089815). |  |

The large points are explained by the fact that on the curve C ( w 2) C_{\binom{w}{2}} we have the following solutions

 | x \displaystyle x | = \displaystyle= | 3 ⋅ 5 ⋅ ( 2 ​ w − 1) 2, \displaystyle 3\cdot 5\cdot(2w-1)^{2}, |  |

 | y \displaystyle y | = \displaystyle= | 75 ​ ( 720 ​ w 4 − 1440 ​ w 3 + 1020 ​ w 2 − 300 ​ w + 31) ​ ( 2 ​ w − 1) ​ and \displaystyle 75(720w^{4}-1440w^{3}+1020w^{2}-300w+31)(2w-1)\mbox{ and } |  |

 | x \displaystyle x | = \displaystyle= | 3 ⋅ 5 ⋅ ( 2 ​ w − 1) 2 + 4, \displaystyle 3\cdot 5\cdot(2w-1)^{2}+4, |  |

 | y \displaystyle y | = \displaystyle= | 75 ​ ( 720 ​ w 4 − 1440 ​ w 3 + 1140 ​ w 2 − 420 ​ w + 61) ​ ( 2 ​ w − 1). \displaystyle 75(720w^{4}-1440w^{3}+1140w^{2}-420w+61)(2w-1). |  |

Hence we obtain the following divisors on J ( w 2) ​ ( ℚ) J_{\binom{w}{2}}({\mathbb{Q}})

 | ( x, 30 ​ w − 15, 1), \displaystyle(x,30w-15,1), |  |

 | ( x − 1, 30 ​ w − 15, 1), \displaystyle(x-1,30w-15,1), |  |

 | ( x − 2, 30 ​ w − 15, 1), \displaystyle(x-2,30w-15,1), |  |

 | ( x − 3, 30 ​ w − 15, 1), \displaystyle(x-3,30w-15,1), |  |

 | ( x − 4, 30 ​ w − 15, 1), \displaystyle(x-4,30w-15,1), |  |

 | ( x − 60 ​ w 2 + 60 ​ w − 15, 108000 ​ w 5 − 270000 ​ w 4 + 261000 ​ w 3 − 121500 ​ w 2 + 27150 ​ w − 2325, 1), \displaystyle(x-60w^{2}+60w-15,108000w^{5}-270000w^{4}+261000w^{3}-121500w^{2}+27150w-2325,1), |  |

 | ( x − 60 ​ w 2 + 60 ​ w − 19, 108000 ​ w 5 − 270000 ​ w 4 + 279000 ​ w 3 − 148500 ​ w 2 + 40650 ​ w − 4575, 1). \displaystyle(x-60w^{2}+60w-19,108000w^{5}-270000w^{4}+279000w^{3}-148500w^{2}+40650w-4575,1). |  |

###### Remark.

In case of the equation

 | ( n 2) = ( m 7) + d \binom{n}{2}=\binom{m}{7}+d |  |

one obtains genus 3 curves. Stoll [26] proved that the rank of the Jacobian is 9 if d = 0. d=0. For other values of d d in the range { − 3, …, 3 } \{-3,\ldots,3\} many of the genus 3 hyperelliptic curves have high ranks as well. Balakrishnan et. al. [3] developed an algorithm to deal with genus 3 hyperelliptic curves defined over ℚ \mathbb{Q} whose Jacobians have Mordell-Weil rank 1. If d = − 2, d=-2, then the equation is isomorphic to the curve

 | Y 2 = 70 ​ X 7 − 1470 ​ X 6 + 12250 ​ X 5 − 51450 ​ X 4 + 113680 ​ X 3 − 123480 ​ X 2 + 50400 ​ X − 661500 Y^{2}=70X^{7}-1470X^{6}+12250X^{5}-51450X^{4}+113680X^{3}-123480X^{2}+50400X-661500 |  |

and using Magma (with SetClassGroupBounds("GRH") to speed up computation) we get that the rank of the Jacobian is 1. Therefore we may try to use the Sage implementation described in [3] to compute the set of rational points on this curve. The affine points are ( 8, ± 1470), (8,\pm 1470), hence we have the solution

 | ( 4 2) = ( 8 7) − 2. \binom{4}{2}=\binom{8}{7}-2. |  |

###### Proof of Theorem 5.

In each case we will be working in the same way. More precisely, for given k k we write f 1 ​ ( x) = a 2 ​ x 2 + a 1 ​ x + a 0 f_{1}(x)=a_{2}x^{2}+a_{1}x+a_{0} and f 2 ​ ( x) = ∑ i = 0 k b i ​ x i f_{2}(x)=\sum_{i=0}^{k}b_{i}x^{i}. The polynomial ( f 1 ​ ( x) k) + ( x 2) − ( f 2 ​ ( x) 2) = ∑ i = 0 2 ​ k A i ​ x i \binom{f_{1}(x)}{k}+\binom{x}{2}-\binom{f_{2}(x)}{2}=\sum_{i=0}^{2k}A_{i}x^{i} needs to be zero. Thus the coefficient near x i x^{i} in F k ​ ( x) F_{k}(x) need to be zero for i = 0, …, 2 ​ k i=0,\ldots,2k. In consequence, we are interested in solving the system of polynomial equations

 | S k: A 0 = A 1 = … = A 2 ​ k = 0 S_{k}:\;A_{0}=A_{1}=\ldots=A_{2k}=0 |  |

in k + 4 k+4 variables a 0, a 1, a 2, b 0, …, b k a_{0},a_{1},a_{2},b_{0},\ldots,b_{k}. We have A 2 ​ k = a 2 k k! − b k 2 2 A_{2k}=\frac{a_{2}^{k}}{k!}-\frac{b_{k}^{2}}{2} and thus a 2 = k! 2 ​ t 2, b k = ( k! 2) k − 1 2 ​ t k a_{2}=\frac{k!}{2}t^{2},b_{k}=\left(\frac{k!}{2}\right)^{\frac{k-1}{2}}t^{k} for some non-zero t ∈ ℚ t\in{\mathbb{Q}}. We note that after the substitution of the computed values of a 2, b k a_{2},b_{k} into the system S k S_{k}, the related system of equations

 | S k ′: A k ′ = A k + 1 ′ = … = A 2 ​ k − 1 ′, S_{k}^{\prime}:\;A_{k}^{\prime}=A_{k+1}^{\prime}=\ldots=A_{2k-1}^{\prime}, |  |

where A i ′ A_{i}^{\prime} comes from A i A_{i} after the substitution of the computed values of a 2, b k a_{2},b_{k}, is triangular with respect to the variables b 0, b 1, …, b k − 1 b_{0},b_{1},\ldots,b_{k-1}. More precisely, we have deg b i ⁡ A k + i ′ = 1 \operatorname{deg}_{b_{i}}A_{k+i}^{\prime}=1 for i = 0, …, k − 1 i=0,\ldots,k-1. Moreover, the coefficient near b i b_{i} is a power of t t times a rational number. Solving for b 0, …, b k − 1 b_{0},\ldots,b_{k-1} and substituting into S k ′ S_{k}^{\prime} we are left with the system of equations

 | S k ′′: A 0 ′′ = A 1 ′′ = … = A k − 1 ′′, S_{k}^{\prime\prime}:\;A_{0}^{\prime\prime}=A_{1}^{\prime\prime}=\ldots=A_{k-1}^{\prime\prime}, |  |

in three variables a 0, a 1, t a_{0},a_{1},t. The polynomial A i ′′ A_{i}^{\prime\prime} is the numerator of the rational function A i ′ A_{i}^{\prime} after substitution of the computed values b 0, …, b k − 1 b_{0},\ldots,b_{k-1}. It seems that for each fixed odd k ≥ 3 k\geq 3, the system S k ′′ S_{k}^{\prime\prime} can be solved using Gröbner bases techniques. More precisely, we compute G k G_{k} - the Gröbner basis of the ideal generated by the polynomials A i ′′, i = 0, …, k − 1 A_{i}^{\prime\prime},i=0,\ldots,k-1. For k ≥ 5 k\geq 5 we have more equations than variables we expect that the system S k ′′ S_{k}^{\prime\prime} for all sufficiently large k k has no rational (and even complex) solutions. This can be confirmed with our approach for k ∈ { 11, …, 19 } k\in\{11,\ldots,19\}. However, we were unable to prove such a statement in full generality.

We prove the first part of our theorem. However, we present details of the reasoning only for k = 3 k=3. The case k = 5 k=5 is proved in exactly the same way. We are interested in rational solutions of the system

 | S 3: A 0 = … = A 6 = 0. S_{3}:\;A_{0}=\ldots=A_{6}=0. |  |

We have a 2 = 3 ​ t 2, b 3 = 3 ​ t 3 a_{2}=3t^{2},b_{3}=3t^{3} for some t ≠ 0 t\neq 0. We put the values of a 2, b 3 a_{2},b_{3} into the system S 3 S_{3} and solve corresponding system of equations

 | S 3 ′: A 3 ′ = A 4 ′ = A 5 ′ = 0, S_{3}^{\prime}:\;A_{3}^{\prime}=A_{4}^{\prime}=A_{5}^{\prime}=0, |  |

with respect to b 0, b 1, b 2 b_{0},b_{1},b_{2}. We get

 | b 0 = 36 ​ a 0 ​ a 1 ​ t 2 − 36 ​ a 1 ​ t 2 − a 1 3 + 72 ​ t 3 144 ​ t 3, b 1 = 12 ​ a 0 ​ t 2 + a 1 2 − 12 ​ t 2 8 ​ t, b 0 = 3 ​ a 1 ​ t 2. b_{0}=\frac{36a_{0}a_{1}t^{2}-36a_{1}t^{2}-a_{1}^{3}+72t^{3}}{144t^{3}},\;b_{1}=\frac{12a_{0}t^{2}+a_{1}^{2}-12t^{2}}{8t},\;b_{0}=\frac{3a_{1}t}{2}. |  |

In consequence, after the substitution of the values of a 2, b 0, b 1, b 2, b 3 a_{2},b_{0},b_{1},b_{2},b_{3} into the system S 3 S_{3} we obtain the system

 | S 3 ′′: A 0 ′′ = A 1 ′′ = A 2 ′′ = 0, S_{3}^{\prime\prime}:\;A_{0}^{\prime\prime}=A_{1}^{\prime\prime}=A_{2}^{\prime\prime}=0, |  |

where A i ′′ = t 2 ​ ( 3 − i) ​ A i ′ ∈ ℚ ⁡ [t, a 0, a 1] A_{i}^{\prime\prime}=t^{2(3-i)}A_{i}^{\prime}\in{\mathbb{Q}}[t,a_{0},a_{1}]. It is an easy task to solve the system S 3 ′′ S_{3}^{\prime\prime}. Indeed, we compute Gröbner basis G 3 G_{3}, of the ideal generated by A 0 ′′, A 1 ′′, A 2 ′′ A_{0}^{\prime\prime},A_{1}^{\prime\prime},A_{2}^{\prime\prime}. The basis G 3 G_{3} contains four polynomials. Two of them are the following

 | a 1 5 ​ ( a 1 + 3) ​ ( a 1 + 12), ( 4 ​ a 0 − 7) ​ a 1 5 ​ ( a 1 + 12) a_{1}^{5}(a_{1}+3)(a_{1}+12),\;(4a_{0}-7)a_{1}^{5}(a_{1}+12) |  |

and we easily obtain the following solutions

 | f 1 ​ ( x) = 3 ​ ( − 1 + 2 ​ x) 2, f 2 ​ ( x) = 2 − 15 ​ x + 36 ​ x 2 − 24 ​ x 3, f 1 ​ ( x) = 5 − 12 ​ x + 12 ​ x 2, f 2 ​ ( x) = 5 − 21 ​ x + 36 ​ x 2 − 24 ​ x 3, f 1 ​ ( x) = 1 4 ​ ( 12 ​ x 2 − 12 ​ x + 7), f 2 ​ ( x) = 1 8 ​ ( − 24 ​ x 3 + 36 ​ x 2 − 18 ​ x + 7). \begin{array}[]{lll}f_{1}(x)=3(-1+2x)^{2},&&f_{2}(x)=2-15x+36x^{2}-24x^{3},\\ f_{1}(x)=5-12x+12x^{2},&&f_{2}(x)=5-21x+36x^{2}-24x^{3},\\ f_{1}(x)=\frac{1}{4}(12x^{2}-12x+7),&&f_{2}(x)=\frac{1}{8}(-24x^{3}+36x^{2}-18x+7).\end{array} |  |

Note that the first two solutions were presented in [4]. Unfortunately, the polynomials from the third solution take only non-integer values.

For k = 5 k=5 we proceed in the same way and omit details. However, let us note that the Gröbner basis G 5 G_{5} contains 7 polynomials. Two of them are the following

 | a 1 9 ​ ( a 1 + 60) ​ ( 3 ​ a 1 + 80), a 1 9 ​ ( 3 ​ a 0 − 26) ​ ( a 1 + 60) a_{1}^{9}(a_{1}+60)(3a_{1}+80),\;a_{1}^{9}(3a_{0}-26)(a_{1}+60) |  |

and we obtain two solutions with integer coefficients and the solution (corresponding to the triple t = 2 / 3, a 0 = 26 / 3, a 1 = − 80 / 3 t=2/3,a_{0}=26/3,a_{1}=-80/3)

 | f 1 ​ ( x) = 2 3 ​ ( 40 ​ x 2 − 40 ​ x + 13), f 2 ​ ( x) = 1 27 ​ ( 12800 ​ x 5 − 32000 ​ x 4 + 32000 ​ x 3 − 16000 ​ x 2 + 3955 ​ x − 364). f_{1}(x)=\frac{2}{3}(40x^{2}-40x+13),\;f_{2}(x)=\frac{1}{27}(12800x^{5}-32000x^{4}+32000x^{3}-16000x^{2}+3955x-364). |  |

By replacing x x by 3 ​ x − 1 3x-1 we obtain polynomial with integer coefficients, which is exactly the third solution from the paper [4].

For k = 7 k=7 the Gröbner basis G 7 G_{7} contains 11 elements. In particular, the following three polynomials are in G 7 G_{7}:

 | a 1 12 ​ ( a 1 + 70), a 1 12 ​ ( 2 ​ a 0 − 41), a 1 10 ​ ( 420 ​ t − a 1) ​ ( a 1 + 420 ​ t). a_{1}^{12}(a_{1}+70),\;a_{1}^{12}(2a_{0}-41),\;a_{1}^{10}(420t-a_{1})(a_{1}+420t). |  |

We found that the only solution (corresponding to t = 1 / 6, a 0 = 41 / 2, a 1 = − 70 t=1/6,a_{0}=41/2,a_{1}=-70) is the following

 | f 1 ​ ( x) \displaystyle f_{1}(x) | = 1 2 ​ ( 140 ​ x 2 − 140 ​ x + 41), \displaystyle=\frac{1}{2}(140x^{2}-140x+41), |  |

 | f 2 ​ ( x) \displaystyle f_{2}(x) | = 1 96 ​ ( 5488000 ​ x 7 − 19208000 ​ x 6 + 28812000 ​ x 5 − 24010000 ​ x 4 + 11997160 ​ x 3 − 3589740 ​ x 2 + CLOSE \displaystyle=\frac{1}{96}(5488000x^{7}-19208000x^{6}+28812000x^{5}-24010000x^{4}+11997160x^{3}-3589740x^{2}+ |  |

 |  | OPEN + 594370 ​ x − 41847). \displaystyle+594370x-41847). |  |

The last part of our theorem follows from certain Gröbner basis computations. For k ∈ { 9, 11, 13, 15, 17, 19 } k\in\{9,11,13,15,17,19\} we found that the G k G_{k} contains polynomial of the form t u k t^{u_{k}} for some u k ∈ ℕ + u_{k}\in{\mathbb{N}}_{+}, i.e., t t need to be zero which leads to contradiction. ∎

###### Remark.

Using the same approach as in the proof of the above theorem one can prove that the Diophantine equation ( f 1 ​ ( x) k) − ( x 2) = ( f 2 ​ ( x) 2) \binom{f_{1}(x)}{k}-\binom{x}{2}=\binom{f_{2}(x)}{2} has no polynomial solutions f 1, f 2 ∈ ℚ ⁡ [x] f_{1},f_{2}\in{\mathbb{Q}}[x] satisfying deg ⁡ f 1 = 2, deg ⁡ f 2 = k \operatorname{deg}f_{1}=2,\operatorname{deg}f_{2}=k for k ∈ { 3, 5, …, 19 } k\in\{3,5,\ldots,19\}.

We also looked for solutions of the more general Diophantine equation

(16) |  | ( f 1 ​ ( x) k) + ( f 0 ​ ( x) 2) = ( f 2 ​ ( x) 2), \binom{f_{1}(x)}{k}+\binom{f_{0}(x)}{2}=\binom{f_{2}(x)}{2}, |  |

where f 0 f_{0} is of degree 2. By using the same approach as in the proof of Theorem 5 one can prove that for k ∈ { 5, 7, …, 19 } k\in\{5,7,\ldots,19\} there are no solutions f 0, f 1, f 2 ∈ ℚ ⁡ [x] f_{0},f_{1},f_{2}\in{\mathbb{Q}}[x] of ( 16) satisfying deg ⁡ f 0 = deg ⁡ f 1 = 2 \operatorname{deg}f_{0}=\operatorname{deg}f_{1}=2 and deg ⁡ f 2 = k \operatorname{deg}f_{2}=k.

However, if we allow f 0 f_{0} to be of degree 3 we found the following solutions. For k = 5 k=5 we have the solution

 | f 1 ​ ( x) \displaystyle f_{1}(x) | = 15 ​ x 2, \displaystyle=15x^{2}, |  |

 | f 0 ​ ( x) \displaystyle f_{0}(x) | = 1 2 ​ ( 30 ​ x 3 − 5 ​ x + 1), \displaystyle=\frac{1}{2}\left(30x^{3}-5x+1\right), |  |

 | f 2 ​ ( x) \displaystyle f_{2}(x) | = 1 2 ​ ( 225 ​ x 5 − 75 ​ x 3 + 7 ​ x + 1). \displaystyle=\frac{1}{2}\left(225x^{5}-75x^{3}+7x+1\right). |  |

For k = 7 k=7 we have the solution

 | f 1 ​ ( x) \displaystyle f_{1}(x) | = 2520 ​ x 2 + 1, \displaystyle=2520x^{2}+1, |  |

 | f 0 ​ ( x) \displaystyle f_{0}(x) | = 1 2 ​ ( 17640 ​ x 3 − 23 ​ x + 1), \displaystyle=\frac{1}{2}\left(17640x^{3}-23x+1\right), |  |

 | f 2 ​ ( x) \displaystyle f_{2}(x) | = 1 2 ​ ( 32006016000 ​ x 7 − 88905600 ​ x 5 + 52920 ​ x 3 + 7 ​ x + 1). \displaystyle=\frac{1}{2}\left(32006016000x^{7}-88905600x^{5}+52920x^{3}+7x+1\right). |  |

Note that in both cases by replacing x x by 2 ​ x − 1 2x-1 we get polynomials with integer coefficients.

Playing around with the Diophantine equation ( f 0 ​ ( x) 3) + ( f 1 ​ ( x) 3) = ( f 2 ​ ( x) 2) \binom{f_{0}(x)}{3}+\binom{f_{1}(x)}{3}=\binom{f_{2}(x)}{2} we also found the polynomial solution

 | f 0 ​ ( x) = x ⁡ ( 3 ​ x + 2), f 1 ​ ( x) = ( 2 ​ x + 1) ​ ( 3 ​ x + 2), f 2 ​ ( x) = 9 ​ x 3 + 15 ​ x 2 + 6 ​ x + 1. f_{0}(x)=x(3x+2),\;f_{1}(x)=(2x+1)(3x+2),\;f_{2}(x)=9x^{3}+15x^{2}+6x+1. |  |

## References

- [1] È. T. Avanesov. Solution of a problem on figurate numbers. Acta Arith., 12:409–420, 1966/1967.
- [2] A. Baker. Bounds for the solutions of the hyperelliptic equation. Proc. Cambridge Philos. Soc., 65:439–444, 1969.
- [3] J. S. Balakrishnan, F. Bianchi, V. Cantoral- Farfán, M. Çiperiani, and A. Etropolski. Chabauty-Coleman experiments for genus 3 hyperelliptic curves. arXiv e-prints, May 2018. arXiv:1805.03361.
- [4] A. Blokhuis, A. Brouwer, and B. de Weger. Binomial collisions and near collisions. Integers, 17:Paper No. A64, 8, 2017.
- [5] W. Bosma, J. Cannon, and C. Playoust. The Magma algebra system. I. The user language. J. Symbolic Comput., 24(3-4):235–265, 1997. Computational algebra and number theory (London, 1993).
- [6] B. Brindza. On a special superelliptic equation. Publ. Math. Debrecen, 39(1-2):159–162, 1991.
- [7] N. Bruin and M. Stoll. Two-cover descent on hyperelliptic curves. Math. Comp., 78(268):2347–2370, 2009.
- [8] Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll, and Sz. Tengely. Integral points on hyperelliptic curves. Algebra Number Theory, 2(8):859–885, 2008.
- [9] C. Chabauty. Sur les points rationnels des courbes algébriques de genre supérieur à l’unité. C. R. Acad. Sci. Paris, 212:882–885, 1941.
- [10] B. M. M. de Weger. A binomial Diophantine equation. Quart. J. Math. Oxford Ser. (2), 47(186):221–231, 1996.
- [11] H. R. Gallegos-Ruiz. S-integral points on hyperelliptic curves. International Journal of Number Theory, 07(03):803–824, 2011.
- [12] H. R. Gallegos-Ruiz. Computing integral points on genus 2 curves estimating hyperelliptic logarithms. Acta Arith., 187(4):329–344, 2019.
- [13] J. Gebel, A. Pethő, and H. G. Zimmer. Computing integral points on elliptic curves. Acta Arith., 68(2):171–192, 1994.
- [14] N. Katsipis. Diophantine equations coming from binomial near-collisions. arXiv e-prints, January 2019. 1901.03841.
- [15] P. Kiss. On the number of solutions of the Diophantine equation ( x p) = ( y 2) \binom{x}{p}=\binom{y}{2}. Fibonacci Quart., 26(2):127–130, 1988.
- [16] A. K. Lenstra, H. W. Lenstra, Jr., and L. Lovász. Factoring polynomials with rational coefficients. Math. Ann., 261(4):515–534, 1982.
- [17] D. A. Lind. The quadratic field Q ⁡ ( 5) Q(\surd 5) and a certain Diophantine equation. Fibonacci Quart., 6(3):86–93, 1968.
- [18] L. J. Mordell. On the integer solutions of y ⁡ ( y + 1) = x ⁡ ( x + 1) ​ ( x + 2) y(y+1)=x(x+1)(x+2). Pacific J. Math., 13:1347–1351, 1963.
- [19] Á. Pintér. A note on the Diophantine equation ( x 4) = ( y 2) \binom{x}{4}=\binom{y}{2}. Publ. Math. Debrecen, 47(3-4):411–415, 1995.
- [20] S. Schmitt and H. Zimmer. Elliptic Curves, volume 31 of Studies in Mathematics. De Gruyter, Berlin/ New York, 2003. A Computational Approach.
- [21] D. Singmaster. Repeated binomial coefficients and Fibonacci numbers. Fibonacci Quart., 13(4):295–298, 1975.
- [22] W. A. Stein et al. Sage Mathematics Software, version 8.5. The Sage Development Team, 2019. http://www.sagemath.org.
- [23] M. Stoll. On the height constant for curves of genus two. Acta Arith., 90(2):183–201, 1999.
- [24] M. Stoll. Implementing 2-descent for Jacobians of hyperelliptic curves. Acta Arith., 98(3):245–277, 2001.
- [25] M. Stoll. On the height constant for curves of genus two. II. Acta Arith., 104(2):165–182, 2002.
- [26] M. Stoll. An explicit theory of heights for hyperelliptic Jacobians of genus three. In Algorithmic and experimental methods in algebra, geometry, and number theory, pages 665–715. Springer, Cham, 2017.
- [27] R. J. Stroeker and B. M. M. de Weger. Elliptic binomial Diophantine equations. Math. Comp., 68(227):1257–1281, 1999.
- [28] R. J. Stroeker and N. Tzanakis. Solving elliptic Diophantine equations by estimating linear forms in elliptic logarithms. Acta Arith., 67(2):177–196, 1994.
- [29] N. Tzanakis. Elliptic Diophantine Equations, volume 2 of Discrete Mathematics And Applications. De Gruyter, Heraklion, Crete, 2013. A concrete approach via the elliptic logarithm.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:hgallegos@uaz.edu.mx
[4]: mailto:katsipis@gmail.com
[5]: mailto:tengely@science.unideb.hu
[6]: mailto:Maciej.Ulas@im.uj.edu.pl
