<!-- source: http://www.ericr.nl/wondrous/index.html | converted from HTML -->

On The 3x + 1 Problem

On the 3x + 1 problem

By

**SUMMARY:***The so-called 3x+1 problem is to prove that all 3x+1 sequences eventually converge. The sequences themselves however and their lengths display some interesting properties and raise unanswered questions. These pages supply numerical data and propose some conjectures on this innocent looking problem.*

---

This page contains the following sections:

- Definition of the problem
- The Glide
- Delay and Residue
- Completeness and Gamma
- Class Records
- Strength and Levels
- Path Records
- Links to related pages
- Current status of the problem
- Join the distributed search for new class records!
- Watch the [progress][1] of the distributed search project
- Find pages quickly on the [Site Map][2]

*This page was last modified on June 30 2026*

---

Introduction and definitions

For any positive integer N a sequence S i can be defined by putting

S 0 = N

and for all i > 0:

S i = S i-1 / 2 | if S i-1 is even
 |

S i = S i-1 * 3 + 1 | if S i-1 is odd
 |

This latter formula usually gives the sequence its name, the **3x + 1**problem, sometimes also referred to as the Collatz problem, the Syracuse problem or some other name. Thus for N = 13 we find

S 0 = 13, S 1 = 40, S 2 = 20, S 3 = 10, S 4 = 5 S 5 = 16, S 6 = 8, S 7 = 4, S 8 = 2, S 9 = 1, S 10 = 4

and from now on the sequence will repeat itself.

Note : although the sequence is equally well defined when the process is applied to negative integers this page deals with **positive**integers only, also known as the Natural Numbers. Therefore all results on this page shall always be understood to refer to natural numbers only.

We now define Mx(N) Mx(N) = lim k &rarr; &infin; Max(S 0, S 1, ..., S k) Mn(N) Mn(N) = lim k &rarr; &infin; Min(S 0, S 1, ..., S k) Thus we will call any positive integer Convergent if Mn(N) = 1 Divergent if Mx(N) does not exist Cyclic otherwise No positive integer N is known which may possibly be divergent, and we therefore reach the widely believed yet still unproven:

Conjecture 1a : (weak 3x+1 conjecture) No integer N is divergent. Serious indications exist however that no other cycle but the simple 4-2-1 cycle exists. In fact it is already known that any other cycle must contain at least a very large number of elements. See the [cycles][3] page to find out the exact numbers and how they follow from the current status of the problem.

It is therefore not unreasonable to state
Conjecture 1b : (strong 3x+1 conjecture) All positive integers N are convergent. This conjecture remains unproven to this day.

While most authors on the subject have concerned themselves mainly with proving conjecture 1b, on these pages we will from here on assume that conjecture 1b holds and look into a number of other properties of the 3x+1 sequences.

---

The Glide

Glide for any positive integer N > 1 let k be the lowest index for which S k < N.
We shall call k the **Glide**of N and write this as G(N).
Calculating the Glide for any positive integer is tantamount to showing it is convergent, as long as all smaller numbers are known to be convergent as well.
Thus we may restate conjecture 1b as follows:
Conjecture 1b : (strong 3x+1 conjecture, restated) All positive integers N > 1 have a finite Glide This conjecture is obviously unproven as well. However **Terras**proved a very important though weaker theorem: Theorem (Terras) : Almost all positive integers N have finite Glide. For an informal proof of this theorem look at the [Terras theorem page][4]

It may not be immediately obvious from the definition of the sequence that arbitrarily high Glides must exist. But observe that any number of the form $N = 2^{p}-1$ with $p > 1$ will have $S_{2}=3 * 2^{p-1} - 1$ and, since $S_2$ is odd: $S_4=3 * 3 * 2^{p-2}-1$ and eventually $S_{2p}=3^{p}-1$.
Hence $S_i$ will not be below $N$ for at least $2p$, and therefore $G(N) > 2p$.

Although Glides are thus unbounded it is a far different proposition to find the smallest number for which $G(N) \gt k$. for any given $k$.

Glide Record a positive integer N is called a **Glide Record**
if for all $M \lt N$ we have $G(M) \lt G(N)$
Skipping the trivial numbers 1 and 2 the first Glide Records are

N = 3 G(N) = 6 N = 7 G(N) = 11 N = 27 G(N) = 96 N = 703 G(N) = 132

and so on. The author calculated Glides over a substantial interval, and the Glide Records found so far are given in the [Glide Records Table][5].

---

Delay and Residue

Delay for any positive integer N let k be the lowest index for which $S_k = 1$.
We shall call k the **Delay**of N and write this as $D(N)$. Delay Record A positive integer N is called a **Delay Record**
if for all $M \lt N$ we have $D(M) \lt D(N)$. Lengthy calculations have been made in trying to find Delay Records.
All currently known Delay Records are given in the [Delay Records Table][6].

*Note: to calculate the delay of any number yourself, try the [3x + 1 calculator page][7]*.
Residue for any positive integer $N$ let $E(N)$ and $O(N)$ denote the number of elements from $S_0$ to $S_{D(N)-1}$ which are even or odd, respectively. Obviously $O(N) + E(N) = D(N)$.
Now due to the construction of the sequence we may write

$2^{E(N)} = 3^{O(N)} * N * Res(N)$

where $Res(N)$ is a factor equal to the product of
$(1 + 1 / ( 3 * S_i ) )$ taken over the odd elements $S_i$ for $0 ≤ i \lt D(N)$.
We will call $Res(N)$ the **Residue**of N. It turns out that $Res(N)$ is usually small and typically lies between 1.10 and 1.25. Therefore it appears reasonable to propose
Conjecture 2a : (weak residue conjecture) A number $Res_{max}$ exists such that for every positive integer

$Res(N) \lt Res_{max}$.

There are serious indications though that a much more explicit conjecture can be made:

Conjecture 2b : (strong residue conjecture) For all $N : Res(N) ≤ Res(993)$. For the evidence to support this conjecture look at the [residues page][8].
Whether conjecture 2b is true or not, we will from now on assume that at least conjecture 2a holds, and also that $Res_{max} \ll 6$.

---

Completeness

Completeness for all integers $N \gt 1$ the **Completeness**of N, C(N), is defined by $C(N) = O(N) / E(N)$. Theorem 1 : For all $N \gt 1: C(N) \lt ln(2)/ln(3) = 0.63092975...$ Proof : From the previous paragraph we had, by definition
$2 ^E(N) = 3 ^O(N) * N * Res(N)$
Taking the logarithm and regrouping yields
$O(N) / E(N) = ln(2) / ln(3) - (ln(N) + ln(Res(N))) / (E(N).ln(3) )$
The final term is often small, but always $\gt 0$. This leads to the rather more complex question of how close C(N) can get to its theoretical limit. If the final term could get infinitesimally close to zero then the completeness would get infinitesimally close to this limit. For large N the final term is proportional to ln(N) / E(N). The reciprocal of this quantity is usually defined as **Gamma**. Gamma for all integers $N \gt 1$ **Gamma(N)**is defined by $E(N) / ln(N)$. There is ample evidence to suggest that Gamma(N) will *not*reach arbitrary large values, and so we reach
Conjecture 3 : A number $C _{max}$ exists such that for all $N \lt 1 : C(N) \lt C _{max}$.
with $C _{max} \lt ln(2) / ln(3)$. Or, in simpler terms: C(N) will **not**get infinitesimally close to its theoretical limit. For the evidence to support this conjecture look at the [completeness page][9].
Completeness Record A number $N \gt 1$ is called a **Completeness Record**
if for all $M \lt N$ we have $C(M) \lt C(N)$. Similarly we have
Gamma Record A number $N \gt 1$ is called a **Gamma Record**
if for all $M \lt N$ we have $Gamma(M) \lt Gamma(N)$. From the similarity of their definitions it should come as no surprise that the tables of known Completeness and Gamma records are virtually the same.

All Completeness and Gamma Records currently known are given in the [Completeness and Gamma Records Table][10].

---

Class Records

Assuming Conjecture 1b holds we can partition the positive integers into Delay Classes $DC _k (k=0,1,2,3...)$ where an integer $N$ is said to belong to class $D(N)$.

We note that no class is empty as for $N = 2^k$ we have $D(N) = k$.

Class Record The lowest element of a Delay Class $DC_k$ is called its **Class Record**, indicated by $R_k$.
Class Records of consecutive classes are often 'related', the lower one occurring in the sequence of the higher one.
Assuming Conjecture 2a holds, with $Res_{max} \lt 6$ we have: Theorem 2 : Let $R_k$ and $R_{k+1}$ be the records of Delay Classes $k$ and $k+1$, respectively.
Then $O(R_k) \le O(R_{k+1})$ and $E(R_k) \le E(R_{k+1})$. Proof : Let $R_k$ and $R_{k+1}$ be the records of classes $k$ and $k+1$ respectively.
Assume $O(R_k) - O(R_{k+1}) = x$, $x \gt 0$. Then $R_{k+1} / R_k$ is equal to $2^{x+1} * 3^x * Res(R_k) / Res(R_{k+1})$ which for positive $x$ is definitely $\gg 2$.
Since $N = 2 * R_k$ has a delay of $k + 1$ and is smaller than $R_{k+1}$, this would imply that $R_{k+1}$ would be no class record.
Therefore $O(R_k) \le O(R_{k+1})$.

Assume that $E(R_k) - E(R_{k+1}) = x$, $x \gt 0$. Then $R_k / R_{k+1}$ is equal to $2^x * 3^{x+1} * Res(R_{k+1}) / Res(R_k)$ which for positive *x*is definitely $\gg 3$.
Since either $N = 3 * R_{k+1} + 1$ or $N = R_{k+1} / 2$ has delay $k$, and both are smaller than $R_k$ this would imply that $R_k$ would be no class record.
Therefore $E(R_k) \le E(R_{k+1})$. From the above result we may easily derive Theorem 3 : Let $N$ be any Completeness Record.
Then $N$ is a Class Record as well. Proof : Assume a number $M \lt N$ exists with $D(M) = D(N)$.

&bull; If $O(M) = O(N)$, and thus $E(M) = E(N)$, then $C(M) = C(N)$ and thus $N$ would be no Completeness Record.
&bull; If $O(M) \gt O(N)$ then $C(M) \gt C(N)$ and again $N$ would be no Completeness Record.
&bull; Finally if $O(M) \lt O(N)$ then, still assuming conjecture 2a holds, $M$ would not be $ \lt N$. Therefore such an $M$ does not exist and $N$ is therefore a Class Record.
Theoretically a Completeness Record does not necessarily have to be a Delay Record as well, since a lower number with a higher Delay but lower Completeness might exist. All currently known Completeness Records are Delay Records as well though.

As of October 2024 all class Records up to 2318 are known.

A complete list of known Class Records can be found in the [Class Records Table][11].

---

Strength and Levels

If Conjecture 2a holds, with $Rmax \ll 6$, this also implies that the elements of a Delay Class occur at discrete levels, which roughly lie a factor 6 apart. The elements of class 13 for example are 34, 35, 192, 208, 212, 213, 226, 227, 1280, 1344, 1360, 1364, 1365 and 8192. The grouping into four different "subclasses" is obvious.
In order to work with levels we first define a more basic parameter called the Strength:

Strength For all positive integers $N$ with $D(N) = k$ the **Strength**$S(N)$ is defined by
$S(N) = 5 * O(N) - 3 * E(N)$. The Strength of most numbers is well below zero, and positive Strengths are quite rare. It would appear though that arbitrarily high Strengths should exist. Strength Record A positive integer $N$ is called a **Strength Record**
if for all $M \lt N$ we have $S(M) \lt S(N)$. Strength records are quite rare. Only five non-trivial records are known, and the highest one of those has 18 digits already. They can be found on the [Strength page][12] together with a few numbers that are currently the best known candidates for the next records.
Based on the Strength it is easy to define the Level. Note that for all numbers $N$ with $D(N) = k$ we have necessarily $S(N) \equiv 5k (mod 8)$
Level For all positive integers $N$ with $D(N) = k$ the **Level**$L(N)$ is defined by
$L(N) = - [S(N) / 8 ]$
(where $[x]$ is meant to be the largest integer $≤ x$) Thus $S(34) = 5 * 3 - 3 * 10 = -15$. Therefore $L(34) = -[-15/8] = 2$ Similarly $L(192) = 3$, $L(1280) = 4$ and $L(8192) = 5$. For any delay $k$ the highest possible level occurs at $N = 2^k$, as this is the highest number with this delay. Level 0 can be seen as the highest level for which $C(N) ≥ 0.60$.

With lower numbers the 'limited availability' of numbers makes statistics a risky approach, but with higher numbers we may say that the level yields information about the relative 'exclusiveness' of the record. From a statistical point of view with levels 'close to 0' we find that the lower the level, the less numbers are found at that level. Although numbers with negative levels do exist they are quite rare. The *only*number below $10\,000\,000\,000$ for which $L(N) \lt 0$ occurs at $N = 63\,728\,127$, for which $L(N) = -1$.

The next ones are $L(12\,235\,060\,455) = -1$ $(D(N) = 1184)$ and $L(13\,371\,194\,527) = -1$ $(D(N) = 1210)$. Up to $21\,000\,000\,000$ three more level -1 numbers exist, but then surprisingly the next one does not appear until $R_{1408} = 1\,444\,338\,092\,271$, a number almost 70 times larger than its predecessor. Only 9 numbers of level -1 exist before the first number of level -2 occurs: $R_{1549} = 3\,743\,559\,068\,799$. This number shows a surprisingly high delay, surpassing the previous Delay Record by no less than over one hundred.

Up to $100\,000\,000\,000\,000 (10^{14})$ one finds approximately 100 numbers of level -1 and just a single one of level -2, which gives a fair indication of their rarity. Thus it is rather unexpected the first number of level -3 is found just outside this interval at $N = 100\,759\,293\,214\,567$. With a Delay of $1820$ this number is not only a Delay Record, surpassing the previous record with no fewer than 158 steps, but a Strength and Completeness Record as well. Remarkably a further level -3 number pops up almost immediately as $R_{1789}$ is found at $N = 104\,797\,092\,792\,063$.

A total of 15 level -3 numbers exist between $100 * 10^{12}$ and $531 * 10^{12}$, but no others appear quickly thereafter. In fact no further level -3 numbers exist below $10^{16}$. The next one is $N = 12\,769\,884\,180\,266\,527$, over 20 times larger than the previous one.

Still lower levels are ever harder to come by. As the numbers increase searches become slower and search intervals get wider. The lowest level -4 number, now confirmed as a Delay and Strength record, has 18 digits. The smallest number of level -5 found so far has 21 digits and the lowest number currently known of level -10 has no less than 36 digits.

---

Path records and Expansion

Any positive integer N can be completely defined by the delay, the level and the residue, i.e. from these three data N can be calculated exactly. None of these however give any information about the path of the sequence $S_i$. In particular no information is available of $Mx(N)$, the highest number occurring in the 3x+1-sequence. This number is of practical importance as well, since it indicates the minimum number of bits needed for a computer algorithm to calculate a particular sequence without overflows occurring.

*Note: to calculate the maximum of any number yourself, try the [3x + 1 calculator page][7]*. Path Record a positive integer $N$ is called a **Path Record**
if for all $M \lt N$ we have $Mx(M) \lt Mx(N)$ The first Path Records are

$N = 2$ $Mx(N) = 2$ $N = 3$ $Mx(N) = 16$ $N = 7$ $Mx(N) = 52$ $N = 15$ $Mx(N) = 160$ $N = 27$ $Mx(N) = 9232$

and so on. Path records can be conveniently numbered in the order in which they occur. Thus $P_1 = 2$, $P_2 = 3$, etc.
A curious observation about the values of $Mx(N)$ is Theorem 4 : Let $N$ be any odd number $\gt 2$. If $Mx(N) \gt 3N + 1$ then $Mx(N) \equiv 16 \pmod {36}$. Proof : Let $q$ be $Mx(N)$, where $q \equiv a \pmod {36}$. We note that $a$ can not be odd, since $q$ must be even. We also note that we can not have $a \equiv 2 \pmod 4$ or else $q/2$ would be odd which would yield a higher number than $q$. Therefore $a \equiv 0 \pmod 4$.
Since q must be produced by a $3n+1$ iteration we have $a \equiv 1 \pmod 3$. This leaves just $4, 16$ and $28$ as possible values for $a$.
Assume $a = 4$. Then let $q = 36n+4$. The predecessor of q must have been $12n+1$. Then *its*predecessor was $24n+2$. Since this number is not $\equiv 4 \pmod 6$ it must have had $48n+4$ as its predecessor. But this number is greater than $q$, which contradicts the assumption that $q$ is $Mx(N)$.
Similarly for $a = 28$ we find predecessors $12n+9$, $24n+18$ and $48n+36$, which again contradicts the assumption that q is Mx(N).
Therefore we can only have $a = 16$, and therefore $Mx(N) \equiv 16 \pmod {36}$ (and its predecessors in the sequence are $12n+5$, $24n+10$ and $8n+3$). For all Path Records $P_i \ge 3$ we indeed have $Mx(P_i) \gt 3.P_i + 1$, therefore for $i \ge 2$ all $(P_i) \equiv 16 \pmod {36}$.

A list of all currently known Path Records can be found in the [Path Records Table][13].

Expansion The **Expansion**with respect to $Q$, $X_Q$ of $N$ is defined as
$X_Q(N) = {Mx(N) \over N^Q}$ It is easily seen that $X_1(N)$ is unbounded, since if $N = 2^p - 1$ then, as we saw earlier, $S_{2p} = 3^p - 1$ and ${Mx(N) \over N}$ is at least approximately equal to ${3^p \over 2^p}$.

A more interesting question arises when we ask for which $p$ $X_p$ might stay bounded. The following result is well known: Theorem 5 : $X_Q$ is unbounded for $Q \lt {ln(3) \over ln(2)}$ Proof : We saw earlier that for $N = 2^p - 1$ $Mx(N)$ will be at least $3^p - 1$.
Thus for $p \to \infty$ we find $\log(X_Q( N )) = \log( Mx(N) ) - Q * \log( N ) \ge p * ( \log(3) - Q * \log(2) )$
So for $Q \lt \log(3) / \log(2)$ the limit does not exist. When $^2\log( Mx(P_i))$ is depicted graphically against $^2\log( P_i )$ the [curve][13] shows a tendency to become linear with an approximate slope of 2. It is not currently known whether or not this tendency is likely to persist. If it does it implies that $X_Q(N)$ is bounded for $Q \gt 2$.
Open Question 1 : Does a number *C*exist for which *X 2 (N) < C*for all *N*?
And if it does, what is the value of *C*? For many years the highest $X_2(N)$ known was that of $P_{62} (\approx 15.054)$ and it looked unlikely a higher one would be found in the near future. In 2005 however [Tom&aacute;s Oliveira e Silva][14] found $P_{88}$ which has an expansion of $\approx 16.315$. As can be seen from the [Path Records Table][13] record expansions are very rare. The function $X_2(N)$ reaches a temporary maximum of $12.66$ at $N = 27$, which holds until $P_{43} = 319\,804\,831$ is reached, a number over $10\,000\,000$ times larger. Again, the value of $13.83$ reached by $P_{43}$ is not surpassed until $P_{62}$, which scores $15.05$. $P_{62}$ is over $10\,000$ times larger than $P_{43}$. Finally the highest expansion currently known is that of $P_{88}$ which reaches $16.32$. $P_{88}$ is well over $500\,000$ times larger than its predecessor.

If successive gaps between ever higher values of the function $X_2 (N)$ continue to be of this magnitude it looks unlikely we will ever know more than a handful of Expansion Records.

---

References to other pages on this topic

&bull; In August 1999 the first conference on the 3x+1 problem took place in Eichst&auml;tt, Germany. (sorry, page no longer available)
&bull; Here's a nice picture of the Eichst&auml;tt conference [participants][15].
&bull; [Lagarias overview][16] of the 3x+1 problem.
&bull; [Super-Index][17] of the 3x+1 Problem and its generalizations.
&bull; ****[Gary T. Leavens and Mike Vermeulen: 3x+1 search programs][18]
*Computers Math. Applic. Vol. 24, No 11, pp. 79-99 (1992)*
&bull; In 2020 Terence Tao was able to prove that [almost all orbits of the Collatz map attain almost bounded values][19].
&bull; [Tom&aacute;s Oliveira e Silva][14] was the first to find all Path and Glide Records up to 100.2 50.
He has extended his search well beyond 2 60.
&bull; [MathWorld page][20] on the collatz Problem
&bull; The [On-Line Encyclopedia of Integer Sequences][21] contains many sequences related to the 3x+1 problem;
for instance [A6370][22], [A6884][23], [A600412][24], [A6577][25], [A6877][26] and [A6878][27].
&bull; Eric Farin has developed a number of [very interesting models][28].
&bull; Ken Conrow's [3x+1 problem structure page][29].
&bull; Marc Lapierre's page to [calculate the delay and paths of arbitrary big numbers][30].
&bull; Darrell Cox is [researching 3x+1 and 3x-1 loops][31].
&bull; Peter Schorer believes he might have a proof of the 3x + 1 Conjecture. Take a look at his papers [here][32].
&bull; Thanks to some hard working Chinese translators you can also view this page in [Chinese][33].

---

Current status

All numbers up to $2^{71}$ ( ~$2.36 * 10^{21}$ ) have been checked once for convergence.
All numbers up to $87 * 2^{60}$ ( ~$1.00 * 10^{20}$ ) have been double checked for convergence.
All numbers up to $5 * 2^{60}$ ( ~$5.76 * 10^{18}$ ) have been at least triple checked for convergence.
All numbers up to $2^{60}$ ( ~$1.15 * 10^{18}$ ) have been checked in at least four projects for convergence.  |

All numbers up to $46.5 * 10^{18}$ have been checked for class records. ( [View progress][1]) |

 |

[Number of Glide Records][5] | 32 |

[Highest known Glide Record][5] | 1575 | at N = | 180352,746940,718527 |

[Highest known Residue][8] | 1.253142 | at N = | 993 |

[Number of known Class Records][11] | 2425 |  |

[Lowest unknown Class Record][11] | 2369 | Limit = | 51,973085,677454,932905 |  |

[Number of known Delay Records][6] | 147 |  |

[Highest known Delay Record][6] | 2456 | at N = | 28,019077,177231,758495 |

[Number of Completeness Records][10] | 16 |  |

[Highest known Completeness Record][10] | 0.605413 | at N = | 104899,295810,901231 |

[Number of Gamma Records][10] | 15 |  |

[Highest known Gamma Record][10] | 35.823841 | at N = | 104899,295810,901231 |

[Number of Path Records][13] | 97 |  |

[Highest known Path Record][13] | ~ 9.88 E+41 | at N = | 2358,909599,867980,429759 |

[Highest known Expansion (for Q=2)][13] | 16.315 | at N = | 1,980976,057694,848447 |

To find out more on the programming techniques used to obtain these results please consult this [page on technical details][34].

---

Join the 3x + 1 search!

Whenever (computer) time is available the quest for new records still continues!
The program currently focuses on using (NVIDIA) GPU cards for maximal progress.
The program runs totally unattended, so anyone with an NVIDIA GPU can join the 3x+1 search! Just look at the [3x+1 search page][35] to see how to join, or take a look at the Class record [progress map][1].

Special thanks to **Kevin Hebb**from Canada for the time and effort he took for many years to make dozens of PC's work day and night on the problem and to **Fang Wenjie**for creating the recent GPU version of the program.

Please mail any offers for additional help to of these pages.

---


## Links

[1]: progress.html
[2]: sitemap.html
[3]: cycles.html
[4]: terras.html
[5]: glidrecs.html
[6]: delrecs.html
[7]: showsteps.html
[8]: residues.html
[9]: compness.html
[10]: comprecs.html
[11]: classrec.html
[12]: strengths.html
[13]: pathrecs.html
[14]: http://sweet.ua.pt/tos/bib.html
[15]: eichstatt.html
[16]: http://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/node2-an.shtml
[17]: http://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/superLagarias.html
[18]: https://lib.dr.iastate.edu/cs_techreports/125/
[19]: https://arxiv.org/pdf/1909.03562
[20]: http://mathworld.wolfram.com/CollatzProblem.html
[21]: http://www.oeis.org/
[22]: http://www.oeis.org/A006370
[23]: http://www.oeis.org/A006884
[24]: http://www.oeis.org/A060412
[25]: http://www.oeis.org/A006577
[26]: http://www.oeis.org/A006877
[27]: http://www.oeis.org/A006878
[28]: http://collatz.freehostia.com/index.html
[29]: http://www-personal.ksu.edu/~kconrow/
[30]: http://ahonga.fr/js/syracuse_3n+1.html
[31]: http://www.darrellcox.website/
[32]: http://www.occampress.com
[33]: http://www.equn.com/3x+1/
[34]: techpage.html
[35]: search.html
