<!-- source: https://ar5iv.labs.arxiv.org/html/0902.3257 | converted from HTML -->

[0902.3257] Regularity versus complexity in the binary representation of 3 n

# Regularity versus complexity
in the binary representation of 3 n 3^{n}

Eric S. Rowland Address: Mathematics Department
Tulane University
New Orleans, LA 70118, USA

Date: October 31, 2009

###### Abstract.

We use the grid consisting of bits of 3 n 3^{n} to motivate the definition of 2 2 -adic numbers. Specifically, we exhibit diagonal stripes in the bits of 3 2 n 3^{2^{n}}, which turn out to be the first in an infinite sequence of such structures. Our observations are explained by a 2 2 -adic power series, providing some regularity among the disorder in the bits of powers of 3 3. Generally, the base- p p representation of k p n k^{p^{n}} has these features.

## 1. Several mysteries

The binary representation of a number m m can be thought of as encoding the unique set of distinct powers of 2 2 that sum to m m. For example,

 | 81 = 1010001 2 = 1 ⋅ 2 6 + 0 ⋅ 2 5 + 1 ⋅ 2 4 + 0 ⋅ 2 3 + 0 ⋅ 2 2 + 0 ⋅ 2 1 + 1 ⋅ 2 0 = 2 6 + 2 4 + 2 0. 81=1010001_{2}=1\cdot 2^{6}+0\cdot 2^{5}+1\cdot 2^{4}+0\cdot 2^{3}+0\cdot 2^{2}+0\cdot 2^{1}+1\cdot 2^{0}=2^{6}+2^{4}+2^{0}. |  |

We will display binary representations graphically by rendering 0 0 and 1 1 respectively as □ \square and ■ \blacksquare. For reasons that will become clear, the convention in this paper when displaying binary representations graphically is to reverse the order of the digits relative to the standard ordering, so that higher indices are to the right. For example, we write 81 = $̣\blacksquare$ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ ■ = 2 0 + 2 4 + 2 6 81=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare=2^{0}+2^{4}+2^{6}, where the dot identifies the 2 0 2^{0} position (somewhat like a decimal point).

The binary representations of the first several powers of 3 3 grow steadily in length:

 | 3 0 \displaystyle 3^{0} | = $̣\blacksquare$ \displaystyle=\text{\@text@daccent{$\bc$}} |  |

 | 3 1 \displaystyle 3^{1} | = $̣\blacksquare$ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\blacksquare |  |

 | 3 2 \displaystyle 3^{2} | = $̣\blacksquare$ ​ □ ​ □ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare |  |

 | 3 3 \displaystyle 3^{3} | = $̣\blacksquare$ ​ ■ ​ □ ​ ■ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare |  |

 | 3 4 \displaystyle 3^{4} | = $̣\blacksquare$ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare |  |

Figure 1 displays a grid in which the n n th row contains the binary digits of 3 n 3^{n}. Pictures like this were considered by Stephen Wolfram [4, page 119]. Small triangles and other local features can be seen, but overall we get an impression of uniform disorder. There is no global structure evident, aside from the right boundary of the pattern, which has slope log 2 ⁡ 3 \log_{2}3.

[image: Refer to caption] Figure 1. Powers of 3 3 in base 2 2. The n n th row consists of the binary digits of 3 n 3^{n}, in order of increasing exponents.

There are some global regularities, however. In particular, every column is eventually periodic. This is because there are only finitely many (in fact 2 a 2^{a}) states that can be assumed by the first a a columns taken together, so eventually the first a a columns return to a state that they have reached before, at which point they become periodic.

In fact, each column is not just eventually periodic but periodic from the start. This is because each row has a unique predecessor, namely the integer obtained by dividing by 3 3. Put algebraically, 3 3 is invertible modulo 2 a 2^{a} for every a ≥ 1 a\geq 1, so from a given row we may compute the previous row to as many bits as we want.

What if we try to compute a a bits of “row − 1 -1 ” — the predecessor to the initial condition? Certainly we can do this, and the result simply maintains the periodicity of the columns. We can iteratively compute predecessors and thereby uniquely continue the picture up the page. Figure 2 shows the end of the unique infinite “history” leading up to the initial condition.

[image: Refer to caption] Figure 2. Part of the history obtained by periodically continuing each column up the page.

For those readers familiar with cellular automata, we mention that the ability to evolve the system backward in time is analogous to the same ability in a class of cellular automata whose local rules are bijective functions in the rightmost position. As with multiplying each row by 3 3 to form the next, information only propagates to the right and is not lost in these automata, and consequently they are reversible under the condition that the left half of each row is determined (say, all white) [3]. Indeed, several themes of the present paper can be carried over to such cellular automata.

But what do the bits in such rows mean? Rows n < 0 n<0 in the history illustrated in Figure 2 do not represent integers, since they contain 1 1 s in positions arbitrarily far to the right: The sum used to compute the value of such a row diverges. For example, row − 1 -1 represents the “infinite integer”

 | ⋯ □ □ □ □ □ $̣\blacksquare$ ■ □ ■ □ ■ □ ■ □ ■ □ ⋯ \displaystyle\cdots\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\cdots | = 2 0 + 2 1 + 2 3 + 2 5 + 2 7 + 2 9 + ⋯ \displaystyle=2^{0}+2^{1}+2^{3}+2^{5}+2^{7}+2^{9}+\cdots |  |

 |  | = 1 + ∑ i = 0 ∞ 2 2 ​ i + 1. \displaystyle=1+\sum_{i=0}^{\infty}2^{2i+1}. |  |

However, formally applying the geometric series formula to this divergent series produces

 | 1 + 2 ​ ∑ i = 0 ∞ 4 i =? 1 + 2 1 − 4 = 1 3 = 3 − 1, 1+2\sum_{i=0}^{\infty}4^{i}\stackrel{{\scriptstyle?}}{{=}}1+\frac{2}{1-4}=\frac{1}{3}=3^{-1}, |  |

which is certainly a natural object for row n = − 1 n=-1 to correspond to. Similarly, row − 2 -2 represents

 | ⋯ □ □ □ □ □ $̣\blacksquare$ □ □ ■ ■ ■ □ □ □ ■ ■ ■ □ □ □ ⋯ \displaystyle\cdots\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\cdots | = 2 0 + ∑ i = 0 ∞ ( 2 6 ​ i + 3 + 2 6 ​ i + 4 + 2 6 ​ i + 5) \displaystyle=2^{0}+\sum_{i=0}^{\infty}\left(2^{6i+3}+2^{6i+4}+2^{6i+5}\right) |  |

 |  | =? 1 + 2 3 1 − 2 6 + 2 4 1 − 2 6 + 2 5 1 − 2 6 \displaystyle\stackrel{{\scriptstyle?}}{{=}}1+\frac{2^{3}}{1-2^{6}}+\frac{2^{4}}{1-2^{6}}+\frac{2^{5}}{1-2^{6}} |  |

 |  | = 1 9 = 3 − 2. \displaystyle=\frac{1}{9}=3^{-2}. |  |

This is our first mystery, and in fact for each n < 0 n<0 there is a divergent series which produces 3 n 3^{n} under invalid applications of the geometric series formula.

###### Mystery 1.

Each power 3 n 3^{n} for n < 0 n<0 is the “sum” of a divergent series.

In order to resolve this mystery we must first encounter several additional mysteries — all related to the first — regarding the binary representation of 3 n 3^{n}.

Since there are only two cell values ( □ \square and ■ \blacksquare) in Figure 1, the period length of each column is a power of 2 2. (In fact for a ≥ 3 a\geq 3 the period length of 3 n mod 2 a 3^{n}\mod 2^{a} is 2 a − 2 2^{a-2}.) Therefore, another consequence of the column periodicity is that row 2 n 2^{n} resembles the initial condition in several bits, since the periods of the first several columns will have just started over. Brenton Bostick brought this “local nestedness” to my attention at the Midwest NKS Conference in 2005. For example 3 2 2 = 81 = $̣\blacksquare$ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ ■ 3^{2^{2}}=81=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare agrees with the initial condition 3 0 = $̣\blacksquare$ □ □ □ □ □ □ ⋯ 3^{0}=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\cdots to three places to the right of the 2 0 2^{0} position. Other terms in the subsequence 3 2 n 3^{2^{n}} agree with the initial condition to more places:

 | 3 2 0 \displaystyle 3^{2^{0}} | = $̣\blacksquare$ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\blacksquare |  |

 | 3 2 1 \displaystyle 3^{2^{1}} | = $̣\blacksquare$ ​ □ ​ □ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare |  |

 | 3 2 2 \displaystyle 3^{2^{2}} | = $̣\blacksquare$ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare |  |

 | 3 2 3 \displaystyle 3^{2^{3}} | = $̣\blacksquare$ ​ □ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ ■ ​ ■ ​ □ ​ □ ​ ■ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare |  |

 | 3 2 4 \displaystyle 3^{2^{4}} | = $̣\blacksquare$ ​ □ ​ □ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ ■ ​ ■ ​ ■ ​ □ ​ ■ ​ □ ​ ■ ​ ■ ​ □ ​ □ ​ □ ​ □ ​ ■ ​ □ ​ □ ​ ■ ​ □ ​ ■ \displaystyle=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare |  |

Figure 3 shows many more rows, each row truncated at 600 600 bits; the image can be efficiently produced with the following *Mathematica*code.

Arr | ayPlot[  |

 | Rev | erse /@  |

 |  | IntegerDigits[PowerMod[3, 2 ˆ Range[0, 255], 2 ˆ 600], 2, 600]  |

]  |

The large triangular region of white cells indicates a sort of convergence to the initial condition: The farther down we go in this image, the more columns have stabilized to the first bit in their period — the bit in row 0 0. As Figure 3 shows, each column (except the leftmost column) eventually becomes white, because row 0 0 is simply ⋯ □ □ □ □ □ $̣\blacksquare$ □ □ □ □ □ ⋯ = 1 = 3 0 \cdots\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\cdots=1=3^{0}. In other words, 3 2 n 3^{2^{n}} “converges” bitwise to 1 1 as n → ∞ n\to\infty.

[image: Refer to caption] Figure 3. The subsequence 3 2 n 3^{2^{n}}. The n n th row contains the first 600 600 bits of 3 2 n 3^{2^{n}}.

This can be proven by Euler’s theorem, which states that if k k is coprime to b b then k ϕ ⁡ ( b) ≡ 1 mod b k^{\phi(b)}\equiv 1\mod b, where the Euler totient function ϕ ⁡ ( b) \phi(b) is the number of integers 1 ≤ x ≤ b 1\leq x\leq b that are relatively prime to b b. It is not difficult to convince oneself that if p p is prime then ϕ ⁡ ( p n + 1) = p − 1 p ⋅ p n + 1 = ( p − 1) ​ p n \phi(p^{n+1})=\frac{p-1}{p}\cdot p^{n+1}=(p-1)p^{n}. In our case, letting k = 3 k=3 and b = 2 n + 1 b=2^{n+1} gives 3 2 n ≡ 1 mod 2 n + 1 3^{2^{n}}\equiv 1\mod 2^{n+1}. Letting n → ∞ n\to\infty shows that every bit in 3 2 n 3^{2^{n}} eventually approaches the corresponding bit of 1 1.

Perhaps we feel a little uneasy about giving much credence to this convergence, because certainly 3 2 n 3^{2^{n}} gets very large and far away from 1 1 as n n gets large. Thus we record it as another mystery.

###### Mystery 2.

lim n → ∞ 3 2 n = 1 \displaystyle{\lim_{n\to\infty}3^{2^{n}}=1}.

In Figure 3 we see additional structure as well — surprising diagonal lines above the white triangular region. More diagonals are filled in as we go down the page, so there appears to be another bitwise-convergent sequence here. To change the diagonal lines into vertical lines, we make the first column white (for uniformity) and shear the image (shifting each row one position left relative to the row above it). The result is shown as Figure 4. Indeed these (shifted) rows are converging bitwise to something — the row

 | c 1 = ⋯ □ □ □ □ □ $̣\square$ □ ■ □ ■ ■ ■ ■ □ □ □ ■ □ ■ ■ ■ □ ■ □ □ ■ □ □ ■ □ ■ □ □ □ ■ □ □ ⋯. c_{1}=\cdots\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\text{\@text@daccent{$\wc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\cdots. |  |

The shearing operation can also be effected by shifting the n n th row left by n n bits; in other words, divide the n n th row by 2 n 2^{n}. We may therefore write

 | c 1 = lim n → ∞ 3 2 n − 1 2 n. c_{1}=\lim_{n\to\infty}\frac{3^{2^{n}}-1}{2^{n}}. |  |

[image: Refer to caption] Figure 4. Bits of 3 2 n 3^{2^{n}}, sheared so that the diagonal lines are now vertical.

In Figure 4 we also observe some secondary diagonal structures that were not easily visible before. They are not as demarcated as the first set and seem to be interacting with the complex background. In order to make the secondary diagonals vertical we would like to perform the same shearing operation. However, first we need to subtract the limiting pattern c 1 c_{1} from each row. But subtract it how? The limit is a divergent “infinite integer”, but forming an integer from the first a a bits of c 1 c_{1} and subtracting this integer from each row clears all the corresponding equal bits. Once we have subtracted the limit, we divide by 2 n 2^{n} to remove the n n bits of 0 0 s on row n n. This produces Figure 5, in which the secondary diagonals are no longer muddied by the background but produce a clear limiting pattern themselves. The new limit is

 | c 2 \displaystyle c_{2} | = lim n → ∞ 3 2 n − 1 2 n − c 1 2 n \displaystyle=\lim_{n\to\infty}\frac{\frac{3^{2^{n}}-1}{2^{n}}-c_{1}}{2^{n}} |  |

 |  | = ⋯ □ □ □ □ □ $̣\square$ □ □ ■ □ □ ■ □ □ □ ■ □ ■ □ □ ■ ■ □ ■ □ □ ■ □ □ ■ □ ■ ■ □ ■ □ ■ ⋯. \displaystyle=\cdots\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\text{\@text@daccent{$\wc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\cdots. |  |

[image: Refer to caption] Figure 5. Bits of ( ( 3 2 n − 1) / 2 n − c 1) / 2 n \left((3^{2^{n}}-1)/2^{n}-c_{1}\right)/2^{n}, obtained from 3 2 n 3^{2^{n}} by twice subtracting the limit and shearing.

It is natural to let c 0 = lim n → ∞ 3 2 n = 1 c_{0}=\lim_{n\to\infty}3^{2^{n}}=1 be the first limit. If we continue to iterate this subtract-and-shear operation we continue to find convergent sequences of rows. This means that, despite the apparent complexity in bits of 3 2 n 3^{2^{n}}, every region can be decomposed into a sum of simple periodic regions.

The next limit

 | c 3 = ⋯ □ □ □ □ □ $̣\square$ □ □ □ □ ■ ■ ■ □ ■ ■ □ □ □ □ ■ ■ ■ □ ■ □ ■ ■ □ □ ■ □ □ ■ □ □ □ ⋯ c_{3}=\cdots\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\text{\@text@daccent{$\wc$}}\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\square\mspace{-2.76mu}\square\mspace{-2.76mu}\square\cdots |  |

satisfies

 | lim n → ∞ 3 2 n − c 0 2 n − c 1 2 n − c 2 2 n − c 3 = 0. \lim_{n\to\infty}\frac{\frac{\frac{3^{2^{n}}-c_{0}}{2^{n}}-c_{1}}{2^{n}}-c_{2}}{2^{n}}-c_{3}=0. |  |

Let us take this expression and unravel it to see the structure better. We find

 | 3 2 n − ( c 0 + c 1 ​ 2 n + c 2 ​ 2 2 ​ n + c 3 ​ 2 3 ​ n) → 0 3^{2^{n}}-(c_{0}+c_{1}2^{n}+c_{2}2^{2n}+c_{3}2^{3n})\to 0 |  |

as n → ∞ n\to\infty. Replacing 2 n 2^{n} with x x reveals that this is a power series:

 | 3 x = c 0 + c 1 ​ x + c 2 ​ x 2 + c 3 ​ x 3 + O ⁡ ( x 4). 3^{x}=c_{0}+c_{1}x+c_{2}x^{2}+c_{3}x^{3}+O(x^{4}). |  |

Of course, we know a power series for 3 x 3^{x}, namely

 | 3 x = e x ​ log ⁡ 3 = 1 + x ​ log ​ 3 + 1 2! ​ ( x ​ log ​ 3) 2 + 1 3! ​ ( x ​ log ​ 3) 3 + 1 4! ​ ( x ​ log ​ 3) 4 + ⋯, 3^{x}=e^{x\log 3}=1+x\log 3+\frac{1}{2!}(x\log 3)^{2}+\frac{1}{3!}(x\log 3)^{3}+\frac{1}{4!}(x\log 3)^{4}+\cdots, |  |

so we might conjecture that c i = ( log ⁡ 3) i / i! c_{i}=(\log 3)^{i}/i!.

For i = 0 i=0 we indeed have ( log ⁡ 3) 0 / 0! = 1 = c 0 (\log 3)^{0}/0!=1=c_{0}. But for i = 1 i=1 the conjecture seems to fail, because c 1 c_{1} is not a real number but an “infinite integer”. (In any case, the bits of c 1 c_{1} don’t resemble the binary representation of the real number log 3 = 1.00011001001111101010 ⋯ 2 \log 3=1.00011001001111101010\cdots_{2}.)

###### Mystery 3.

“ log ⁡ 3 \log 3 ” is not the real number log ⁡ 3 \log 3.

A final observation we make is that the direction of convergence is opposite that of real numbers. All the sequences we have seen approach their limits by filling in bits from low indices to high indices, which is toward the right in our graphical convention of reversing the digits of integers. A convergent sequence of real numbers, on the other hand, fills in bits from high indices to low indices. Take the sequence ( 1 + 1 / n) n (1+1/n)^{n}, for example. Some terms of this sequence (as real numbers) are shown in Figure 6. The convergence proceeds from left to right, which is the same graphical direction but opposite numerical direction as the convergence of the sequence 3 2 n 3^{2^{n}} in Figure 3.

[image: Refer to caption] Figure 6. Binary representations of ( 1 + 1 / n) n (1+1/n)^{n} as real numbers, with most significant bits on the left. The terms are slowly converging to e = 10.10110111111000010101 ⋯ 2 e=10.10110111111000010101\cdots_{2}.

In the setting of bits of 3 2 n 3^{2^{n}}, then, the low indices of a number are somehow stronger than the higher indices. Therefore we should really think of the “tail” of numbers as being backward from the normal sense: In this mode of convergence, two numbers are close to each other if their leftmost bits agree — if their difference is divisible by a large power of 2 2. This is why we have chosen the convention that higher indices are to the right.

###### Mystery 4.

Two numbers are close if their difference is highly divisible by 2 2.

## 2. 2 2 -adic numbers

Our four mysteries suggest that there is a notion of number presenting itself through the binary representation of 3 2 n 3^{2^{n}} that is quite different from the real numbers. From Mystery 4 we must conclude that in some sense 2 i 2^{i} gets small as i i gets large, and the other mysteries support this conclusion. Let us therefore make this a *definition*instead of a mystery and introduce a new notion of “size” to make this precise.

Every rational number r ≠ 0 r\neq 0 has a representation r = 2 α ​ n d r=2^{\alpha}\frac{n}{d} for integers α \alpha, n n, and d d, where n n and d d are not divisible by 2 2. Moreover, α \alpha is unique. We want | r | 2 |r|_{2} to be large when α \alpha is small and small (but positive) when α \alpha is large. A natural choice is to let | r | 2 = 2 − α |r|_{2}=2^{-\alpha}; this is called the *2 2 -adic norm*of r r. For example, | 64 | 2 = 1 / 64 |64|_{2}=1/64 and | − 691 / 2730 | 2 = 2 |-691/2730|_{2}=2. Since 0 0 is very highly divisible by 2 2, let us define | 0 | 2 = 0 |0|_{2}=0.

Since large powers 2 i 2^{i} are small in the 2 2 -adic norm, a rational number can be a sum of arbitrarily large powers of 2 2 when thought of 2 2 -adically, just as it can be a sum of arbitrarily large powers of 1 / 2 1/2 when thought of as a real number. For example,

 | 1 3 = 1 + ∑ i = 0 ∞ 2 2 ​ i + 1. \frac{1}{3}=1+\sum_{i=0}^{\infty}2^{2i+1}. |  |

In fact, every rational number has the representation ∑ i = N ∞ c i ​ 2 i \sum_{i=N}^{\infty}c_{i}2^{i} for some integer N N and c i ∈ { 0, 1 } c_{i}\in\{0,1\}. For example, − 1 -1 is rendered 2 2 -adically as

 | − 1 = 1 1 − 2 = ∑ i = 0 ∞ 2 i = 2 0 + 2 1 + 2 2 + 2 3 + ⋯ = $̣\blacksquare$ ■ ■ ■ ⋯, -1=\frac{1}{1-2}=\sum_{i=0}^{\infty}2^{i}=2^{0}+2^{1}+2^{2}+2^{3}+\cdots=\text{\@text@daccent{$\bc$}}\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\mspace{-2.76mu}\blacksquare\cdots, |  |

which illustrates that the 2 2 -adic representation of a number is really a “limit” of its representations modulo 2 a 2^{a} as a → ∞ a\to\infty. For finite a a, the representation modulo 2 a 2^{a} of course coincides with its two’s complement representation.

In general, a a bits of the 2 2 -adic representation of a rational number r = 2 α ​ n d r=2^{\alpha}\frac{n}{d} can be found by computing the inverse d − 1 mod 2 a d^{-1}\mod 2^{a}, which is an integer, and multiplying by 2 α ​ n 2^{\alpha}n.

One can check that the 2 2 -adic norm induces a metric d ⁡ ( x, y) = | x − y | 2 d(x,y)=|x-y|_{2} on the rational numbers, akin to the usual metric induced by the absolute value. In particular, it satisfies the triangle inequality | x − y | 2 + | ​ y − z | 2 ≥ | x − z | 2 |x-y|_{2}+|y-z|_{2}\geq|x-z|_{2}.

There are some strange properties of this metric, however. Perhaps the most immediate is that every triangle is isosceles: If | x − y | 2 = | y − z | 2 |x-y|_{2}=|y-z|_{2}, then the triangle is isosceles by definition. On the other hand, if | x − y | 2 ≠ | y − z | 2 |x-y|_{2}\neq|y-z|_{2}, then

 | | x − z | 2 = max ⁡ ( | x − y | 2, | y − z | 2). |x-z|_{2}=\max(|x-y|_{2},|y-z|_{2}). |  |

For example, if x − y = 20 x-y=20 and y − z = 6 y-z=6 then | x − y | 2 = 1 / 4 ≠ 1 / 2 = | y − z | 2 |x-y|_{2}=1/4\neq 1/2=|y-z|_{2} and | x − z | 2 = | 26 | 2 = 1 / 2 |x-z|_{2}=|26|_{2}=1/2.

Naturally, we write x n → x x_{n}\to x if the sequence of 2 2 -adic norms | x − x n | 2 |x-x_{n}|_{2} approaches 0 0 as n → ∞ n\to\infty. So indeed 3 2 n → 1 3^{2^{n}}\to 1 in the 2 2 -adic metric.

Of course, when we take a limit of rational numbers we may not get another rational number. Traditionally, the real numbers can be constructed by taking limits of rationals with respect to the real metric; each real number has an expansion ∑ i = N ∞ c i ​ 2 − i \sum_{i=N}^{\infty}c_{i}2^{-i} for c i ∈ { 0, 1 } c_{i}\in\{0,1\}. Similarly, we can take limits of rationals with respect to the 2 2 -adic metric and get a different completion of the rationals. This completion is called the *set of 2 2 -adic numbers*, and each 2 2 -adic number has a representation ∑ i = N ∞ c i ​ 2 i \sum_{i=N}^{\infty}c_{i}2^{i}, where again c i ∈ { 0, 1 } c_{i}\in\{0,1\}. Like the real numbers, this set is complete — it contains all its limit points.

It turns out that our power series 3 x = ∑ i = 0 ∞ ( log ⁡ 3) i ​ x i / i! 3^{x}=\sum_{i=0}^{\infty}(\log 3)^{i}x^{i}/i! is correct, but it must be interpreted not as a real power series but as a 2 2 -adic power series. This means that “ log ⁡ 3 \log 3 ” is not the real number log ⁡ 3 \log 3 but the 2 2 -adic number log ⁡ 3 \log 3. How do we compute it? The function log ⁡ ( 1 − x) \log(1-x) has a 2 2 -adic power series that coincides with its real power series:

 | log ( 1 − x) = − ∑ i = 1 ∞ x i i. \log(1-x)=-\sum_{i=1}^{\infty}\frac{x^{i}}{i}. |  |

Of course, in the real metric this power series diverges at x = − 2 x=-2, so it cannot be used to compute the real log ⁡ 3 \log 3. But 2 2 -adically this series converges at x = − 2 x=-2 to the 2 2 -adic c 1 = log ⁡ 3 c_{1}=\log 3. Similarly, c 2 = ( log ⁡ 3) 2 / 2! c_{2}=(\log 3)^{2}/2!, c 3 = ( log ⁡ 3) 3 / 3! c_{3}=(\log 3)^{3}/3!, and so on.

To be precise, one must of course establish the standard objects of calculus over the 2 2 -adic numbers — derivatives, power series, tests for convergence, etc. We do not undertake this task here but refer the reader to texts on the subject. The book of Gouvêa [1] serves as a solid introduction, and Koblitz [2] provides a more advanced treatment.

## 3. Generalizations

The results of the previous section can be generalized in several directions, and we discover that the power series structure we have seen is quite common.

Euler’s theorem tells us that there is nothing particularly special about 3 2 n 3^{2^{n}}, and in fact 5 2 n 5^{2^{n}} and 7 2 n 7^{2^{n}} have exactly analogous structures in binary, as shown in the first row of Figure 7. In general, if k k is odd then k x k^{x} has a 2 2 -adic power series 1 + x ​ log ⁡ k + ⋯ 1+x\log k+\cdots. Gouvêa [1, Section 4.5] discusses the region of convergence of such power series.

[image: Refer to caption] Figure 7. Powers k p n k^{p^{n}} in base p p.

What about other bases b > 2 b>2? The second and third rows of Figure 7 show several examples. To address these cases we briefly generalize the discussion to p p -adic numbers for prime p p.

Of course we may define | x | b |x|_{b} for general b b (prime or composite) in the analogous way. For primes p p, | x | p |x|_{p} is a norm on the set of rational numbers. For composite b b it is not since in general | x ⋅ y | b ≠ | x | b ⋅ | y | b |x\cdot y|_{b}\neq|x|_{b}\cdot|y|_{b}; for example, | 4 | 4 = 1 / 4 ≠ 1 = | 2 | 4 ⋅ | 2 | 4 |4|_{4}=1/4\neq 1=|2|_{4}\cdot|2|_{4}. In fact, it is a theorem of Ostrowski that the p p -adic norms and the real norm are (up to equivalence) the only nontrivial norms on the set of rational numbers.

Evidently 4 3 n → 1 4^{3^{n}}\to 1 in the 3 3 -adic metric. However, the 3 3 -adic limit of 2 3 n 2^{3^{n}} is not 1 1 but 2 + 2 ⋅ 3 1 + 2 ⋅ 3 2 + ⋯ = − 1 2+2\cdot 3^{1}+2\cdot 3^{2}+\cdots=-1. For general k k relatively prime to p p, Euler’s theorem provides that k ( p − 1) ​ p n ≡ 1 mod p n + 1 k^{(p-1)p^{n}}\equiv 1\mod p^{n+1}. In the limit, then, k p n k^{p^{n}} approaches a ( p − 1) (p-1) th root of unity 1 1 / ( p − 1) 1^{1/(p-1)}. This root of unity is congruent to k k modulo p p and is called the *Teichmüller representative*of k k. This accounts for the vertical stripes in the base- 5 5 digits of 2 5 n 2^{5^{n}} and 3 5 n 3^{5^{n}}; the 5 5 -adic fourth roots of unity congruent to 2 2 and 3 3 modulo 5 5 are irrational. Note also that 2 5 n + 3 5 n → 0 2^{5^{n}}+3^{5^{n}}\to 0.

The p p -adic power series of functions f ⁡ ( x) f(x) other than k x k^{x} are also evident in the base- p p digits of f ⁡ ( p n) f(p^{n}). Let F n F_{n}, C n C_{n}, M n M_{n}, and B n B_{n} be the sequences of Fibonacci, Catalan, Motzkin, and Bell numbers. The sequences C 2 n C_{2^{n}} and M 2 n M_{2^{n}} have 2 2 -adic limits. The sequences F 2 n F_{2^{n}} and B 2 n B_{2^{n}} do not have 2 2 -adic limits, but F 2 2 ​ n F_{2^{2n}}, F 2 2 ​ n + 1 F_{2^{2n+1}}, B 2 2 ​ n B_{2^{2n}}, and B 2 2 ​ n + 1 B_{2^{2n+1}} do, giving some indication of the ubiquity of p p -adic convergence in combinatorial sequences.

Finally, consider the factorial function x! x!. The terms of the sequence 2 n! 2^{n}!, of course, become highly divisible by 2 2, so 2 n! → 0 2^{n}!\to 0 in the 2 2 -adic norm. However, a theorem of Legendre implies that | 2 n! | 2 = 1 / 2 2 n − 1 |2^{n}!|_{2}=1/2^{2^{n}-1}, and it turns out that

 | 2 n! 2 2 n − 1 \frac{2^{n}!}{2^{2^{n}-1}} |  |

has a (nonzero) 2 2 -adic limit.

## References

- [1] Fernando Gouvêa, *p p -adic Numbers: An Introduction*second edition, Universitext, Springer–Verlag, Berlin, 1997.
- [2] Neil Koblitz, *p p -adic Numbers, p p -adic Analysis, and Zeta-Functions*second edition, Springer–Verlag, New York, 1984.
- [3] Eric Rowland, Local nested structure in rule 30, *Complex Systems*16 (2006) 239–258.
- [4] Stephen Wolfram, *A New Kind of Science*, Wolfram Media, Champaign, IL, 2002.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/0902.3256
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/0902.3257
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0902.3257
[7]: https://arxiv.org/pdf/0902.3257
[8]: /html/0902.3258
