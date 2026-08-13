<!-- source: https://en.wikipedia.org/wiki/Falling_and_rising_factorials | converted from HTML -->

Falling and rising factorials - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Mathematical functions

"Rising power" redirects here. For the description of a sovereign state or union of states with significant rising influence in global affairs, see [emerging power][1].

In [mathematics][2], the **falling factorial**(sometimes called the **descending factorial**, [1]**falling sequential product**, or **lower factorial**) is defined as the polynomial ( x) n = x n _ = x ( x − 1) ( x − 2) ⋯ ( x − n + 1) ⏞ n factors = ∏ k = 1 n ( x − k + 1) = ∏ k = 0 n − 1 ( x − k). {\displaystyle {\begin{aligned}(x)_{n}=x^{\underline {n}}&=\overbrace {x(x-1)(x-2)\cdots (x-n+1)} ^{n{\text{ factors}}}\\&=\prod _{k=1}^{n}(x-k+1)=\prod _{k=0}^{n-1}(x-k).\end{aligned}}}[image: {\displaystyle {\begin{aligned}(x)_{n}=x^{\underline {n}}&=\overbrace {x(x-1)(x-2)\cdots (x-n+1)} ^{n{\text{ factors}}}\\&=\prod _{k=1}^{n}(x-k+1)=\prod _{k=0}^{n-1}(x-k).\end{aligned}}}]

The **rising factorial**(sometimes called the **Pochhammer function**, **Pochhammer polynomial**, **ascending factorial**, [1]**rising sequential product**, or **upper factorial**) is defined as x ( n) = x n ¯ = x ( x + 1) ( x + 2) ⋯ ( x + n − 1) ⏞ n factors = ∏ k = 1 n ( x + k − 1) = ∏ k = 0 n − 1 ( x + k). {\displaystyle {\begin{aligned}x^{(n)}=x^{\overline {n}}&=\overbrace {x(x+1)(x+2)\cdots (x+n-1)} ^{n{\text{ factors}}}\\&=\prod _{k=1}^{n}(x+k-1)=\prod _{k=0}^{n-1}(x+k).\end{aligned}}}[image: {\displaystyle {\begin{aligned}x^{(n)}=x^{\overline {n}}&=\overbrace {x(x+1)(x+2)\cdots (x+n-1)} ^{n{\text{ factors}}}\\&=\prod _{k=1}^{n}(x+k-1)=\prod _{k=0}^{n-1}(x+k).\end{aligned}}}]

The value of each is taken to be 1 (an [empty product][3]) when n = 0 {\displaystyle n=0}[image: {\displaystyle n=0}]. These symbols are collectively called **factorial powers**. [2]

The **Pochhammer symbol**, introduced by [Leo August Pochhammer][4], is the notation ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}], where n is a [non-negative integer][5]. It may represent *either*the rising or the falling factorial, with different articles and authors using different conventions. Pochhammer himself actually used ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}] with yet another meaning, namely to denote the [binomial coefficient][6] ( x n) {\displaystyle {\tbinom {x}{n}}}[image: {\displaystyle {\tbinom {x}{n}}}]. [3]

In this article, the symbol ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}] is used to represent the falling factorial, and the symbol x ( n) {\displaystyle x^{(n)}}[image: {\displaystyle x^{(n)}}] is used for the rising factorial. These conventions are used in [combinatorics][7], [4] although [Knuth][8] 's underline and [overline][9] notations x n _ {\displaystyle x^{\underline {n}}}[image: {\displaystyle x^{\underline {n}}}] and x n ¯ {\displaystyle x^{\overline {n}}}[image: {\displaystyle x^{\overline {n}}}] are increasingly popular. [2] [5] In the theory of [special functions][10] (in particular the [hypergeometric function][11]) and in the standard reference work *[Abramowitz and Stegun][12]*, the Pochhammer symbol ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}] is used to represent the rising factorial. [6] [7]

When x {\displaystyle x}[image: {\displaystyle x}] is a positive integer, the falling factorial ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}] gives the number of [n -permutations][13], sequences of n {\displaystyle n}[image: {\displaystyle n}] distinct elements) from an x {\displaystyle x}[image: {\displaystyle x}] -element set, or equivalently the number of [injective functions][14] from a set of size n {\displaystyle n}[image: {\displaystyle n}] to a set of size x {\displaystyle x}[image: {\displaystyle x}]. The rising factorial x ( n) {\displaystyle x^{(n)}}[image: {\displaystyle x^{(n)}}] gives the number of [partitions][15] of an n {\displaystyle n}[image: {\displaystyle n}] -element set into x {\displaystyle x}[image: {\displaystyle x}] ordered sequences (possibly empty). (12, -)</math>, <math>(21, -)</math>, <math>(1, 2)</math>, <math>(2, 1)</math>, <math>(-, 12)</math>, and <math>(-, 21)</math>, where − denotes an empty part."}},"i":0}}]}'> [a]

## Examples and combinatorial interpretation

[[edit][16]]

The first few falling factorials are as follows: ( x) 0 = 1 ( x) 1 = x ( x) 2 = x ( x − 1) = x 2 − x ( x) 3 = x ( x − 1) ( x − 2) = x 3 − 3 x 2 + 2 x ( x) 4 = x ( x − 1) ( x − 2) ( x − 3) = x 4 − 6 x 3 + 11 x 2 − 6 x {\displaystyle {\begin{alignedat}{2}(x)_{0}&&&=1\\(x)_{1}&&&=x\\(x)_{2}&=x(x-1)&&=x^{2}-x\\(x)_{3}&=x(x-1)(x-2)&&=x^{3}-3x^{2}+2x\\(x)_{4}&=x(x-1)(x-2)(x-3)&&=x^{4}-6x^{3}+11x^{2}-6x\end{alignedat}}}[image: {\displaystyle {\begin{alignedat}{2}(x)_{0}&&&=1\\(x)_{1}&&&=x\\(x)_{2}&=x(x-1)&&=x^{2}-x\\(x)_{3}&=x(x-1)(x-2)&&=x^{3}-3x^{2}+2x\\(x)_{4}&=x(x-1)(x-2)(x-3)&&=x^{4}-6x^{3}+11x^{2}-6x\end{alignedat}}}]

The first few rising factorials are as follows: x ( 0) = 1 x ( 1) = x x ( 2) = x ( x + 1) = x 2 + x x ( 3) = x ( x + 1) ( x + 2) = x 3 + 3 x 2 + 2 x x ( 4) = x ( x + 1) ( x + 2) ( x + 3) = x 4 + 6 x 3 + 11 x 2 + 6 x {\displaystyle {\begin{alignedat}{2}x^{(0)}&&&=1\\x^{(1)}&&&=x\\x^{(2)}&=x(x+1)&&=x^{2}+x\\x^{(3)}&=x(x+1)(x+2)&&=x^{3}+3x^{2}+2x\\x^{(4)}&=x(x+1)(x+2)(x+3)&&=x^{4}+6x^{3}+11x^{2}+6x\end{alignedat}}}[image: {\displaystyle {\begin{alignedat}{2}x^{(0)}&&&=1\\x^{(1)}&&&=x\\x^{(2)}&=x(x+1)&&=x^{2}+x\\x^{(3)}&=x(x+1)(x+2)&&=x^{3}+3x^{2}+2x\\x^{(4)}&=x(x+1)(x+2)(x+3)&&=x^{4}+6x^{3}+11x^{2}+6x\end{alignedat}}}]

The coefficients that appear in the expansions are [Stirling numbers of the first kind][17]; see § Connection coefficients and identities below.

When the variable x {\displaystyle x}[image: {\displaystyle x}] is a positive integer, the number ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}] is equal to the number of [n -permutations from a set of x items][13], that is, the number of ways of choosing an ordered list of length n {\displaystyle n}[image: {\displaystyle n}] consisting of distinct elements drawn from a collection of size x {\displaystyle x}[image: {\displaystyle x}]. For example, ( 8) 3 = 8 × 7 × 6 = 336 {\displaystyle (8)_{3}=8\times 7\times 6=336}[image: {\displaystyle (8)_{3}=8\times 7\times 6=336}] is the number of possible different podiums, assignments of gold, silver, and bronze medals in eight-person race. On the other hand, x ( n) {\displaystyle x^{(n)}}[image: {\displaystyle x^{(n)}}] is "the number of ways to arrange n {\displaystyle n}[image: {\displaystyle n}] flags on x {\displaystyle x}[image: {\displaystyle x}] flagpoles", [8] where all flags must be used and each flagpole can have any number of flags. Equivalently, this is the number of ways to partition a set of size n {\displaystyle n}[image: {\displaystyle n}] (the flags) into x {\displaystyle x}[image: {\displaystyle x}] disjoint parts (the flagpoles), with a linear order on the elements in each part (the order of the flags on each pole).

## Properties

[[edit][18]]

The rising and falling factorials are simply related to one another: ( x) n = ( x − n + 1) ( n) = ( − 1) n ( − x) ( n), x ( n) = ( x + n − 1) n = ( − 1) n ( − x) n. {\displaystyle {\begin{alignedat}{2}{(x)}_{n}&={(x-n+1)}^{(n)}&&=(-1)^{n}(-x)^{(n)},\\x^{(n)}&={(x+n-1)}_{n}&&=(-1)^{n}(-x)_{n}.\end{alignedat}}}[image: {\displaystyle {\begin{alignedat}{2}{(x)}_{n}&={(x-n+1)}^{(n)}&&=(-1)^{n}(-x)^{(n)},\\x^{(n)}&={(x+n-1)}_{n}&&=(-1)^{n}(-x)_{n}.\end{alignedat}}}] Falling and rising factorials of integers are directly related to the ordinary [factorial][19]: n! = 1 ( n) = ( n) n, ( m) n = m! ( m − n)!, m ( n) = ( m + n − 1)! ( m − 1)!. {\displaystyle {\begin{aligned}n!&=1^{(n)}=(n)_{n},\\[6pt](m)_{n}&={\frac {m!}{(m-n)!}},\\[6pt]m^{(n)}&={\frac {(m+n-1)!}{(m-1)!}}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}n!&=1^{(n)}=(n)_{n},\\[6pt](m)_{n}&={\frac {m!}{(m-n)!}},\\[6pt]m^{(n)}&={\frac {(m+n-1)!}{(m-1)!}}.\end{aligned}}}] A useful identity for the sums of falling factorials is [9] ∑ k = 0 n − 1 ( k) m = ( n) m + 1 m + 1. {\displaystyle \sum _{k=0}^{n-1}(k)_{m}={\frac {(n)_{m+1}}{m+1}}.}[image: {\displaystyle \sum _{k=0}^{n-1}(k)_{m}={\frac {(n)_{m+1}}{m+1}}.}] Rising factorials of half integers are directly related to the [double factorial][20] m!! = m ( m − 2) ( m − 4) ⋯ {\displaystyle m!!=m(m-2)(m-4)\cdots }[image: {\displaystyle m!!=m(m-2)(m-4)\cdots }]: [1 2] ( n) = ( 2 n − 1)!! 2 n, [2 m + 1 2] ( n) = ( 2 ( n + m) − 1)!! 2 n ( 2 m − 1)!!. {\displaystyle {\begin{aligned}\left[{\frac {1}{2}}\right]^{(n)}={\frac {(2n-1)!!}{2^{n}}},\quad \left[{\frac {2m+1}{2}}\right]^{(n)}={\frac {(2(n+m)-1)!!}{2^{n}(2m-1)!!}}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}\left[{\frac {1}{2}}\right]^{(n)}={\frac {(2n-1)!!}{2^{n}}},\quad \left[{\frac {2m+1}{2}}\right]^{(n)}={\frac {(2(n+m)-1)!!}{2^{n}(2m-1)!!}}.\end{aligned}}}] The falling and rising factorials can be used to express a [binomial coefficient][6]: ( x) n n! = ( x n), x ( n) n! = ( x + n − 1 n). {\displaystyle {\begin{aligned}{\frac {(x)_{n}}{n!}}&={\binom {x}{n}},\\[6pt]{\frac {x^{(n)}}{n!}}&={\binom {x+n-1}{n}}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}{\frac {(x)_{n}}{n!}}&={\binom {x}{n}},\\[6pt]{\frac {x^{(n)}}{n!}}&={\binom {x+n-1}{n}}.\end{aligned}}}] Thus many identities on binomial coefficients carry over to the falling and rising factorials.

The rising and falling factorials are well defined in any [unital][21] [ring][22], and therefore x {\displaystyle x}[image: {\displaystyle x}] can be taken to be, for example, a [complex number][23], including negative integers, or a [polynomial][24] with complex coefficients, or any [complex-valued function][25].

### Calculus

[[edit][26]]

Falling factorials appear in multiple [differentiation][27] of simple power functions: ( d d x) n x a = ( a) n ⋅ x a − n. {\displaystyle \left({\frac {\mathrm {d} }{\mathrm {d} x}}\right)^{n}x^{a}=(a)_{n}\cdot x^{a-n}.}[image: {\displaystyle \left({\frac {\mathrm {d} }{\mathrm {d} x}}\right)^{n}x^{a}=(a)_{n}\cdot x^{a-n}.}] The rising factorial is also integral to the definition of the [hypergeometric function][11]: The hypergeometric function is defined for | z | < 1 {\displaystyle |z|<1}[image: {\displaystyle |z|<1}] by the [power series][28] 2 F 1 ( a, b; c; z) = ∑ n = 0 ∞ a ( n) b ( n) c ( n) z n n! {\displaystyle {}_{2}F_{1}(a,b;c;z)=\sum _{n=0}^{\infty }{\frac {a^{(n)}b^{(n)}}{c^{(n)}}}{\frac {z^{n}}{n!}}}[image: {\displaystyle {}_{2}F_{1}(a,b;c;z)=\sum _{n=0}^{\infty }{\frac {a^{(n)}b^{(n)}}{c^{(n)}}}{\frac {z^{n}}{n!}}}] provided that c ≠ 0, − 1, − 2, … {\displaystyle c\neq 0,-1,-2,\ldots }[image: {\displaystyle c\neq 0,-1,-2,\ldots }]. Note, however, that the hypergeometric function literature typically uses the notation ( a) n {\displaystyle (a)_{n}}[image: {\displaystyle (a)_{n}}] for rising factorials.

## Connection coefficients and identities

[[edit][29]]

Falling and rising factorials are closely related to [Stirling numbers][30]. Indeed, expanding the product reveals [Stirling numbers of the first kind][17] ( x) n = ∑ k = 0 n s ( n, k) x k = ∑ k = 0 n [n k] ( − 1) n − k x k x ( n) = ∑ k = 0 n [n k] x k {\displaystyle {\begin{aligned}(x)_{n}&=\sum _{k=0}^{n}s(n,k)x^{k}=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}(-1)^{n-k}x^{k}\\x^{(n)}&=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}x^{k}\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}(x)_{n}&=\sum _{k=0}^{n}s(n,k)x^{k}=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}(-1)^{n-k}x^{k}\\x^{(n)}&=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}x^{k}\\\end{aligned}}}] And the inverse relations uses [Stirling numbers of the second kind][31] x n = ∑ k = 0 n { n k } ( x) k = ∑ k = 0 n { n k } ( − 1) n − k x ( k). {\displaystyle {\begin{aligned}x^{n}&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix}}(x)_{k}\\&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix}}(-1)^{n-k}x^{(k)}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}x^{n}&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix}}(x)_{k}\\&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix}}(-1)^{n-k}x^{(k)}.\end{aligned}}}] The falling and rising factorials are related to one another through the [image: {\textstyle L(n,k)={\binom {n-1}{k-1}}{\frac {n!}{k!}}}] [Lah numbers L ( n, k) = ( n − 1 k − 1) n! k! {\textstyle L(n,k)={\binom {n-1}{k-1}}{\frac {n!}{k!}}}][32]: [10] x ( n) = ∑ k = 0 n L ( n, k) ( x) k ( x) n = ∑ k = 0 n L ( n, k) ( − 1) n − k x ( k) {\displaystyle {\begin{aligned}x^{(n)}&=\sum _{k=0}^{n}L(n,k)(x)_{k}\\(x)_{n}&=\sum _{k=0}^{n}L(n,k)(-1)^{n-k}x^{(k)}\end{aligned}}}[image: {\displaystyle {\begin{aligned}x^{(n)}&=\sum _{k=0}^{n}L(n,k)(x)_{k}\\(x)_{n}&=\sum _{k=0}^{n}L(n,k)(-1)^{n-k}x^{(k)}\end{aligned}}}] Since the falling factorials are a basis for the [polynomial ring][33], one can express the product of two of them as a [linear combination][34] of falling factorials: [11] ( x) m ( x) n = ∑ k = 0 m ( m k) ( n k) k! ⋅ ( x) m + n − k. {\displaystyle (x)_{m}(x)_{n}=\sum _{k=0}^{m}{\binom {m}{k}}{\binom {n}{k}}k!\cdot (x)_{m+n-k}\ .}[image: {\displaystyle (x)_{m}(x)_{n}=\sum _{k=0}^{m}{\binom {m}{k}}{\binom {n}{k}}k!\cdot (x)_{m+n-k}\ .}] The coefficients ( m k) ( n k) k! {\displaystyle {\tbinom {m}{k}}{\tbinom {n}{k}}k!}[image: {\displaystyle {\tbinom {m}{k}}{\tbinom {n}{k}}k!}] are called *connection coefficients*, and have a combinatorial interpretation as the number of ways to identify (or "glue together") k elements each from a set of size m and a set of size n.

There is also a connection formula for the ratio of two rising factorials given by x ( n) x ( i) = ( x + i) ( n − i), for n ≥ i. {\displaystyle {\frac {x^{(n)}}{x^{(i)}}}=(x+i)^{(n-i)},\quad {\text{for }}n\geq i.}[image: {\displaystyle {\frac {x^{(n)}}{x^{(i)}}}=(x+i)^{(n-i)},\quad {\text{for }}n\geq i.}] Additionally, we can expand generalized exponent laws and negative rising and falling powers through the following identities: [12] (p52) ( x) m + n = ( x) m ( x − m) n = ( x) n ( x − n) m x ( m + n) = x ( m) ( x + m) ( n) = x ( n) ( x + n) ( m) x ( − n) = Γ ( x − n) Γ ( x) = ( x − n − 1)! ( x − 1)! = 1 ( x − n) ( n) = 1 ( x − 1) n = 1 ( x − 1) ( x − 2) ⋯ ( x − n) ( x) − n = Γ ( x + 1) Γ ( x + n + 1) = x! ( x + n)! = 1 ( x + n) n = 1 ( x + 1) ( n) = 1 ( x + 1) ( x + 2) ⋯ ( x + n) {\displaystyle {\begin{aligned}(x)_{m+n}&=(x)_{m}(x-m)_{n}=(x)_{n}(x-n)_{m}\\[6pt]x^{(m+n)}&=x^{(m)}(x+m)^{(n)}=x^{(n)}(x+n)^{(m)}\\[6pt]x^{(-n)}&={\frac {\Gamma (x-n)}{\Gamma (x)}}={\frac {(x-n-1)!}{(x-1)!}}={\frac {1}{(x-n)^{(n)}}}={\frac {1}{(x-1)_{n}}}={\frac {1}{(x-1)(x-2)\cdots (x-n)}}\\[6pt](x)_{-n}&={\frac {\Gamma (x+1)}{\Gamma (x+n+1)}}={\frac {x!}{(x+n)!}}={\frac {1}{(x+n)_{n}}}={\frac {1}{(x+1)^{(n)}}}={\frac {1}{(x+1)(x+2)\cdots (x+n)}}\end{aligned}}}[image: {\displaystyle {\begin{aligned}(x)_{m+n}&=(x)_{m}(x-m)_{n}=(x)_{n}(x-n)_{m}\\[6pt]x^{(m+n)}&=x^{(m)}(x+m)^{(n)}=x^{(n)}(x+n)^{(m)}\\[6pt]x^{(-n)}&={\frac {\Gamma (x-n)}{\Gamma (x)}}={\frac {(x-n-1)!}{(x-1)!}}={\frac {1}{(x-n)^{(n)}}}={\frac {1}{(x-1)_{n}}}={\frac {1}{(x-1)(x-2)\cdots (x-n)}}\\[6pt](x)_{-n}&={\frac {\Gamma (x+1)}{\Gamma (x+n+1)}}={\frac {x!}{(x+n)!}}={\frac {1}{(x+n)_{n}}}={\frac {1}{(x+1)^{(n)}}}={\frac {1}{(x+1)(x+2)\cdots (x+n)}}\end{aligned}}}] Finally, [duplication][35] and [multiplication formulas][36] for the falling and rising factorials provide the next relations: ( x) k + m n = x ( k) m m n ∏ j = 0 m − 1 ( x − k − j m) n for m ∈ N x ( k + m n) = x ( k) m m n ∏ j = 0 m − 1 ( x + k + j m) ( n) for m ∈ N ( a x + b) ( n) = x n ∏ j = 0 n − 1 ( a + b + j x) for x ≠ 0 ( 2 x) ( 2 n) = 2 2 n x ( n) ( x + 1 2) ( n). {\displaystyle {\begin{aligned}(x)_{k+mn}&=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x-k-j}{m}}\right)_{n}&{\text{ for }}m&\in \mathbb {N} \\[6pt]x^{(k+mn)}&=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x+k+j}{m}}\right)^{(n)}&{\text{ for }}m&\in \mathbb {N} \\[6pt](ax+b)^{(n)}&=x^{n}\prod _{j=0}^{n-1}\left(a+{\frac {b+j}{x}}\right)&{\text{ for }}x&\neq 0\\[6pt](2x)^{(2n)}&=2^{2n}x^{(n)}\left(x+{\frac {1}{2}}\right)^{(n)}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}(x)_{k+mn}&=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x-k-j}{m}}\right)_{n}&{\text{ for }}m&\in \mathbb {N} \\[6pt]x^{(k+mn)}&=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x+k+j}{m}}\right)^{(n)}&{\text{ for }}m&\in \mathbb {N} \\[6pt](ax+b)^{(n)}&=x^{n}\prod _{j=0}^{n-1}\left(a+{\frac {b+j}{x}}\right)&{\text{ for }}x&\neq 0\\[6pt](2x)^{(2n)}&=2^{2n}x^{(n)}\left(x+{\frac {1}{2}}\right)^{(n)}.\end{aligned}}}]

## Relation to umbral calculus

[[edit][37]]

The falling factorial occurs in a formula which represents [polynomials][24] using the forward [difference operator][38] Δ ⁡ f ( x) = d e f f ( x + 1) − f ( x), {\displaystyle \operatorname {\Delta } f(x)~{\stackrel {\mathrm {def} }{=}}~f(x+1)-f(x),}[image: {\displaystyle \operatorname {\Delta } f(x)~{\stackrel {\mathrm {def} }{=}}~f(x+1)-f(x),}] which in form is an exact analogue to [Taylor's theorem][39]: Compare the [series expansion][40] from [umbral calculus][41]

f ( t) = ∑ n = 0 ∞ 1 n! Δ x n ⁡ f ( x) | x = 0 ( t) n {\displaystyle \qquad f(t)=\sum _{n=0}^{\infty }\ {\frac {1}{n!}}\operatorname {\Delta } _{x}^{n}f(x){\bigg \vert }_{x=0}(t)_{n}\qquad }[image: {\displaystyle \qquad f(t)=\sum _{n=0}^{\infty }\ {\frac {1}{n!}}\operatorname {\Delta } _{x}^{n}f(x){\bigg \vert }_{x=0}(t)_{n}\qquad }]

with the corresponding series from [differential calculus][42]

f ( t) = ∑ n = 0 ∞ 1 n! [d d x] n f ( x) | x = 0 t n. {\displaystyle \qquad f(t)=\sum _{n=0}^{\infty }{\frac {1}{n!}}\left[{\frac {d}{dx}}\right]^{n}f(x){\bigg \vert }_{x=0}t^{n}~.}[image: {\displaystyle \qquad f(t)=\sum _{n=0}^{\infty }{\frac {1}{n!}}\left[{\frac {d}{dx}}\right]^{n}f(x){\bigg \vert }_{x=0}t^{n}~.}]

In this formula and in many other places, the falling factorial ( x) n {\displaystyle (x)_{n}}[image: {\displaystyle (x)_{n}}] in the calculus of [finite differences][43] plays the role of x n {\displaystyle x^{n}}[image: {\displaystyle x^{n}}] in differential calculus. For another example, note the similarity of Δ ⁡ ( x) n = n ( x) n − 1 {\displaystyle ~\operatorname {\Delta } (x)_{n}=n(x)_{n-1}~}[image: {\displaystyle ~\operatorname {\Delta } (x)_{n}=n(x)_{n-1}~}] to d d x x n = n x n − 1. {\displaystyle ~{\frac {d}{dx}}x^{n}=nx^{n-1}~.}[image: {\displaystyle ~{\frac {d}{dx}}x^{n}=nx^{n-1}~.}]

A corresponding relation holds for the rising factorial and the backward difference operator.

The study of analogies of this type is known as [umbral calculus][41]. A general theory covering such relations, including the falling and rising factorial functions, is given by the theory of [polynomial sequences of binomial type][44] and [Sheffer sequences][45]. Falling and rising factorials are Sheffer sequences of binomial type, as shown by the relations:

( a + b) n = ∑ j = 0 n ( n j) ( a) n − j ( b) j ( a + b) ( n) = ∑ j = 0 n ( n j) a ( n − j) b ( j) {\displaystyle \ {\begin{aligned}(a+b)_{n}&=\sum _{j=0}^{n}{\binom {n}{j}}(a)_{n-j}(b)_{j}\\[6pt](a+b)^{(n)}&=\sum _{j=0}^{n}{\binom {n}{j}}a^{(n-j)}b^{(j)}\end{aligned}}\ }[image: {\displaystyle \ {\begin{aligned}(a+b)_{n}&=\sum _{j=0}^{n}{\binom {n}{j}}(a)_{n-j}(b)_{j}\\[6pt](a+b)^{(n)}&=\sum _{j=0}^{n}{\binom {n}{j}}a^{(n-j)}b^{(j)}\end{aligned}}\ }]

where the coefficients are the same as those in the [binomial theorem][46].

Similarly, the [generating function][47] of Pochhammer polynomials then amounts to the umbral exponential,

∑ n = 0 ∞ ( x) n t n n! = ( 1 + t) x, {\displaystyle \ \sum _{n=0}^{\infty }(x)_{n}{\frac {t^{n}}{n!}}=(1+t)^{x},}[image: {\displaystyle \ \sum _{n=0}^{\infty }(x)_{n}{\frac {t^{n}}{n!}}=(1+t)^{x},}]

since

Δ x ⁡ ( 1 + t) x = t ⋅ ( 1 + t) x. {\displaystyle \ \operatorname {\Delta } _{x}(1+t)^{x}=t\cdot (1+t)^{x}~.}[image: {\displaystyle \ \operatorname {\Delta } _{x}(1+t)^{x}=t\cdot (1+t)^{x}~.}]

## Alternative notations

[[edit][48]]

An alternative notation for the rising factorial x m ¯ ≡ ( x) + m ≡ ( x) m = x ( x + 1) … ( x + m − 1) ⏞ m factors for integer m ≥ 0 {\displaystyle x^{\overline {m}}\equiv (x)_{+m}\equiv (x)_{m}=\overbrace {x(x+1)\ldots (x+m-1)} ^{m{\text{ factors}}}\quad {\text{for integer }}m\geq 0}[image: {\displaystyle x^{\overline {m}}\equiv (x)_{+m}\equiv (x)_{m}=\overbrace {x(x+1)\ldots (x+m-1)} ^{m{\text{ factors}}}\quad {\text{for integer }}m\geq 0}] and for the falling factorial x m _ ≡ ( x) − m = x ( x − 1) … ( x − m + 1) ⏞ m factors for integer m ≥ 0 {\displaystyle x^{\underline {m}}\equiv (x)_{-m}=\overbrace {x(x-1)\ldots (x-m+1)} ^{m{\text{ factors}}}\quad {\text{for integer }}m\geq 0}[image: {\displaystyle x^{\underline {m}}\equiv (x)_{-m}=\overbrace {x(x-1)\ldots (x-m+1)} ^{m{\text{ factors}}}\quad {\text{for integer }}m\geq 0}] goes back to A. Capelli (1893) and L. Toscano (1939), respectively. [2] Graham, Knuth, and Patashnik [12] (pp47, 48) propose to pronounce these expressions as " x to the m rising" and " x to the m falling", respectively.

An alternative notation for the rising factorial x ( n) {\displaystyle x^{(n)}}[image: {\displaystyle x^{(n)}}] is the less common ( x) n +. {\displaystyle (x)_{n}^{+}~.}[image: {\displaystyle (x)_{n}^{+}~.}] When ( x) n + {\displaystyle (x)_{n}^{+}}[image: {\displaystyle (x)_{n}^{+}}] is used to denote the rising factorial, the notation ( x) n − {\displaystyle (x)_{n}^{-}}[image: {\displaystyle (x)_{n}^{-}}] is typically used for the ordinary falling factorial, to avoid confusion. [3]

## Generalizations

[[edit][49]]

The Pochhammer symbol has a generalized version called the [generalized Pochhammer symbol][50], used in multivariate [analysis][51]. There is also a [q -analogue][52], the [q -Pochhammer symbol][53].

For any fixed [arithmetic function][54] f: N → C {\displaystyle f:\mathbb {N} \rightarrow \mathbb {C} }[image: {\displaystyle f:\mathbb {N} \rightarrow \mathbb {C} }] and symbolic parameters x, t, related generalized factorial products of the form

( x) n, f, t:= ∏ k = 0 n − 1 ( x + f ( k) t k) {\displaystyle (x)_{n,f,t}:=\prod _{k=0}^{n-1}\left(x+{\frac {f(k)}{t^{k}}}\right)}[image: {\displaystyle (x)_{n,f,t}:=\prod _{k=0}^{n-1}\left(x+{\frac {f(k)}{t^{k}}}\right)}]

may be studied from the point of view of the classes of generalized [Stirling numbers of the first kind][17] defined by the following coefficients of the powers of x in the expansions of ''n'',''f'',''t''</sub>"}},"i":0}}]}'>(*x*)*n*,*f*,*t*and then by the next corresponding triangular recurrence relation:

[n k] f, t = [x k − 1] ( x) n, f, t = f ( n − 1) t 1 − n [n − 1 k] f, t + [n − 1 k − 1] f, t + δ n, 0 δ k, 0. {\displaystyle {\begin{aligned}\left[{\begin{matrix}n\\k\end{matrix}}\right]_{f,t}&=\left[x^{k-1}\right](x)_{n,f,t}\\&=f(n-1)t^{1-n}\left[{\begin{matrix}n-1\\k\end{matrix}}\right]_{f,t}+\left[{\begin{matrix}n-1\\k-1\end{matrix}}\right]_{f,t}+\delta _{n,0}\delta _{k,0}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}\left[{\begin{matrix}n\\k\end{matrix}}\right]_{f,t}&=\left[x^{k-1}\right](x)_{n,f,t}\\&=f(n-1)t^{1-n}\left[{\begin{matrix}n-1\\k\end{matrix}}\right]_{f,t}+\left[{\begin{matrix}n-1\\k-1\end{matrix}}\right]_{f,t}+\delta _{n,0}\delta _{k,0}.\end{aligned}}}]

These coefficients satisfy a number of analogous properties to those for the [Stirling numbers of the first kind][17] as well as recurrence relations and functional equations related to the f -harmonic numbers, [13] F n ( r) ( t):= ∑ k ≤ n t k f ( k) r. {\displaystyle F_{n}^{(r)}(t):=\sum _{k\leq n}{\frac {t^{k}}{f(k)^{r}}}\,.}[image: {\displaystyle F_{n}^{(r)}(t):=\sum _{k\leq n}{\frac {t^{k}}{f(k)^{r}}}\,.}]

## See also

[[edit][55]]

- [Pochhammer k -symbol][56]
- [Vandermonde identity][57]

## References

[[edit][58]]

1. ↑ Here the parts are distinct; for example, when *x*= *n*= 2, the (2) (2) = 6 partitions are ( 12, −) {\displaystyle (12,-)}[image: {\displaystyle (12,-)}], ( 21, −) {\displaystyle (21,-)}[image: {\displaystyle (21,-)}], ( 1, 2) {\displaystyle (1,2)}[image: {\displaystyle (1,2)}], ( 2, 1) {\displaystyle (2,1)}[image: {\displaystyle (2,1)}], ( −, 12) {\displaystyle (-,12)}[image: {\displaystyle (-,12)}], and ( −, 21) {\displaystyle (-,21)}[image: {\displaystyle (-,21)}], where − denotes an empty part.

1. 1 2 [Steffensen, J.F.][59] (17 March 2006). *Interpolation*(2nd ed.). Dover Publications. p. 8. [ISBN][60] [0-486-45009-0][61]. — A reprint of the 1950 edition by Chelsea Publishing.
2. 1 2 3 [Knuth, D.E.][8]*[The Art of Computer Programming][62]*. Vol. 1 (3rd ed.). p. 50.
3. 1 2 [Knuth, D.E.][8] (1992). "Two notes on notation". *[American Mathematical Monthly][63]*. **99**(5): 403– 422. [arXiv][64]: [math/9205211][65]. [doi][66]: [10.2307/2325085][67]. [JSTOR][68] [2325085][69]. [S2CID][70] [119584305][71]. The remark about the Pochhammer symbol is on page 414.
4. ↑ [Olver, P.J.][72] (1999). *Classical Invariant Theory*. Cambridge University Press. p. 101. [ISBN][60] [0-521-55821-2][73]. [MR][74] [1694364][75].
5. ↑ Harris; Hirst; Mossinghoff (2008). *Combinatorics and Graph Theory*. Springer. ch. 2. [ISBN][60] [978-0-387-79710-6][76].
6. ↑ Abramowitz, Milton; Stegun, Irene A., eds. (December 1972) [June 1964]. **[Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables][12]. [National Bureau of Standards][77] [Applied Mathematics][78] Series. Vol. 55. Washington, DC: [United States Department of Commerce][79]. p. 256 eqn. 6.1.22. [LCCN][80] [64-60036][81].
7. ↑ Slater, Lucy J. (1966). *Generalized Hypergeometric Functions*. Cambridge University Press. Appendix I. [MR][74] [0201688][82]. — Gives a useful list of formulas for manipulating the rising factorial in (*x*)*n*notation.
8. ↑ Feller, William. *An Introduction to Probability Theory and Its Applications*. Vol. 1. Ch. 2.
9. ↑ Graham, Ronald L.; Knuth, Donald Ervin; Patashnik, Oren (1994). *Concrete mathematics: a foundation for computer science*(2nd ed.). Reading, Mass: Addison-Wesley. p. 50. [ISBN][60] [0-201-55802-5][83].
10. ↑ ["Introduction to the factorials and binomials"][84]. *Wolfram Functions Site*.
11. ↑ Rosas, Mercedes H. (2002). "Specializations of MacMahon symmetric functions and the polynomial algebra". *Discrete Math*. **246**( 1– 3): 285– 293. [doi][66]: [10.1016/S0012-365X(01)00263-1][85]. [hdl][86]: [11441/41678][87].
12. 1 2 [Graham, Ronald L.][88]; [Knuth, Donald E.][89] & [Patashnik, Oren][90] (1988). *[Concrete Mathematics][91]*. Reading, MA: Addison-Wesley. pp. 47, 48, 52. [ISBN][60] [0-201-14236-8][92].
13. ↑ Schmidt, Maxie D. (2018). "Combinatorial identities for generalized Stirling numbers expanding f -factorial functions and the f -harmonic numbers". *Journal of Integer Sequences*. **21**(2) 18.2.7. [arXiv][64]: [1611.04708v2][93]. [MR][74] [3779776][94].

## External links

[[edit][95]]

- [Weisstein, Eric W.][96] ["Pochhammer Symbol"][97]. *[MathWorld][98]*.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Falling_and_rising_factorials&oldid=1368603025][99] "

[Categories][100]:

- [Gamma and related functions][101]
- [Factorial and binomial topics][102]
- [Finite differences][103]
- [Operations on numbers][104]

Hidden categories:

- [Articles with short description][105]
- [Short description matches Wikidata][106]
- [Use American English from March 2019][107]
- [All Wikipedia articles written in American English][108]

Search

Falling and rising factorials

12 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Emerging_power
[2]: https://en.wikipedia.org/wiki/Mathematics
[3]: https://en.wikipedia.org/wiki/Empty_product
[4]: https://en.wikipedia.org/wiki/Leo_August_Pochhammer
[5]: https://en.wikipedia.org/wiki/Non-negative_integer
[6]: https://en.wikipedia.org/wiki/Binomial_coefficient
[7]: https://en.wikipedia.org/wiki/Combinatorics
[8]: https://en.wikipedia.org/wiki/Donald_Knuth
[9]: https://en.wikipedia.org/wiki/Overline
[10]: https://en.wikipedia.org/wiki/Special_functions
[11]: https://en.wikipedia.org/wiki/Hypergeometric_function
[12]: https://en.wikipedia.org/wiki/Abramowitz_and_Stegun
[13]: https://en.wikipedia.org/wiki/K-permutation
[14]: https://en.wikipedia.org/wiki/Injective_function
[15]: https://en.wikipedia.org/wiki/Partition_of_a_set
[16]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=1
[17]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
[18]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=2
[19]: https://en.wikipedia.org/wiki/Factorial
[20]: https://en.wikipedia.org/wiki/Double_factorial
[21]: https://en.wikipedia.org/wiki/Unital_ring
[22]: https://en.wikipedia.org/wiki/Ring_(mathematics)
[23]: https://en.wikipedia.org/wiki/Complex_number
[24]: https://en.wikipedia.org/wiki/Polynomial
[25]: https://en.wikipedia.org/wiki/Complex-valued_function
[26]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=3
[27]: https://en.wikipedia.org/wiki/Derivative
[28]: https://en.wikipedia.org/wiki/Power_series
[29]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=4
[30]: https://en.wikipedia.org/wiki/Stirling_number
[31]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
[32]: https://en.wikipedia.org/wiki/Lah_numbers
[33]: https://en.wikipedia.org/wiki/Polynomial_ring
[34]: https://en.wikipedia.org/wiki/Linear_combination
[35]: https://en.wikipedia.org/wiki/Duplication_formula
[36]: https://en.wikipedia.org/wiki/Multiplication_formula
[37]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=5
[38]: https://en.wikipedia.org/wiki/Difference_operator
[39]: https://en.wikipedia.org/wiki/Taylor's_theorem
[40]: https://en.wikipedia.org/wiki/Series_expansion
[41]: https://en.wikipedia.org/wiki/Umbral_calculus
[42]: https://en.wikipedia.org/wiki/Differential_calculus
[43]: https://en.wikipedia.org/wiki/Finite_difference
[44]: https://en.wikipedia.org/wiki/Binomial_type
[45]: https://en.wikipedia.org/wiki/Sheffer_sequence
[46]: https://en.wikipedia.org/wiki/Binomial_theorem
[47]: https://en.wikipedia.org/wiki/Generating_function
[48]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=6
[49]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=7
[50]: https://en.wikipedia.org/wiki/Generalized_Pochhammer_symbol
[51]: https://en.wikipedia.org/wiki/Mathematical_analysis
[52]: https://en.wikipedia.org/wiki/Q-analog
[53]: https://en.wikipedia.org/wiki/Q-Pochhammer_symbol
[54]: https://en.wikipedia.org/wiki/Arithmetic_function
[55]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=8
[56]: https://en.wikipedia.org/wiki/Pochhammer_k-symbol
[57]: https://en.wikipedia.org/wiki/Vandermonde_identity
[58]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=9
[59]: https://en.wikipedia.org/wiki/Johan_Frederik_Steffensen
[60]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[61]: https://en.wikipedia.org/wiki/Special:BookSources/0-486-45009-0
[62]: https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming
[63]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[64]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[65]: https://arxiv.org/abs/math/9205211
[66]: https://en.wikipedia.org/wiki/Doi_(identifier)
[67]: https://doi.org/10.2307%2F2325085
[68]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[69]: https://www.jstor.org/stable/2325085
[70]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[71]: https://api.semanticscholar.org/CorpusID:119584305
[72]: https://en.wikipedia.org/wiki/Peter_J._Olver
[73]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-55821-2
[74]: https://en.wikipedia.org/wiki/MR_(identifier)
[75]: https://mathscinet.ams.org/mathscinet-getitem?mr=1694364
[76]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-79710-6
[77]: https://en.wikipedia.org/wiki/National_Bureau_of_Standards
[78]: https://en.wikipedia.org/wiki/Applied_Mathematics
[79]: https://en.wikipedia.org/wiki/United_States_Department_of_Commerce
[80]: https://en.wikipedia.org/wiki/LCCN_(identifier)
[81]: https://lccn.loc.gov/64-60036
[82]: https://mathscinet.ams.org/mathscinet-getitem?mr=0201688
[83]: https://en.wikipedia.org/wiki/Special:BookSources/0-201-55802-5
[84]: http://functions.wolfram.com/GammaBetaErf/Factorial/introductions/FactorialBinomials/05/
[85]: https://doi.org/10.1016%2FS0012-365X%2801%2900263-1
[86]: https://en.wikipedia.org/wiki/Hdl_(identifier)
[87]: https://hdl.handle.net/11441%2F41678
[88]: https://en.wikipedia.org/wiki/Ronald_L._Graham
[89]: https://en.wikipedia.org/wiki/Donald_E._Knuth
[90]: https://en.wikipedia.org/wiki/Oren_Patashnik
[91]: https://en.wikipedia.org/wiki/Concrete_Mathematics
[92]: https://en.wikipedia.org/wiki/Special:BookSources/0-201-14236-8
[93]: https://arxiv.org/abs/1611.04708v2
[94]: https://mathscinet.ams.org/mathscinet-getitem?mr=3779776
[95]: /w/index.php?title=Falling_and_rising_factorials&amp;action=edit&amp;section=10
[96]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[97]: https://mathworld.wolfram.com/PochhammerSymbol.html
[98]: https://en.wikipedia.org/wiki/MathWorld
[99]: https://en.wikipedia.org/w/index.php?title=Falling_and_rising_factorials&amp;oldid=1368603025
[100]: /wiki/Help:Category
[101]: /wiki/Category:Gamma_and_related_functions
[102]: /wiki/Category:Factorial_and_binomial_topics
[103]: /wiki/Category:Finite_differences
[104]: /wiki/Category:Operations_on_numbers
[105]: /wiki/Category:Articles_with_short_description
[106]: /wiki/Category:Short_description_matches_Wikidata
[107]: /wiki/Category:Use_American_English_from_March_2019
[108]: /wiki/Category:All_Wikipedia_articles_written_in_American_English
