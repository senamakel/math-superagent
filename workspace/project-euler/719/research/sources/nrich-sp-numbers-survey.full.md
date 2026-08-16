<!-- source: https://nrich.maths.org/articles/recent-developments-sp-numbers | converted from HTML -->

Recent Developments on S.P. Numbers | NRICH Skip to main content

menu

search

close

## Or search by topic

### Number and algebra

-

[Place value and the number system][1]

-

[Fractions, decimals, percentages, ratio and proportion][2]

-

[Calculations and numerical methods][3]

-

[Algebraic expressions, equations and formulae][4]

-

[Coordinates, functions and graphs][5]

-

[Patterns, sequences and structure][6]

-

[Properties of numbers][7]

### Geometry and measure

-

[Transformations and constructions][8]

-

[Vectors and matrices][9]

-

[Measuring and calculating with units][10]

-

[Pythagoras and trigonometry][11]

-

[Angles, polygons, and geometrical proof][12]

-

[3D geometry, shape and space][13]

### Probability and statistics

-

[Handling, processing and representing data][14]

-

[Probability][15]

### Working mathematically

-

[Thinking mathematically][16]

-

[Mathematical mindsets][17]

### Advanced mathematics

-

[Decision mathematics and combinatorics][18]

-

[Mechanics][19]

-

[Calculus][20]

-

[Advanced probability and statistics][21]

### For younger learners

-

[Early years foundation stage][22]

# Recent Developments on S.P. Numbers

Since writing the July 1998 NRICH article [Sums and Products of Digits and SP Numbers][23] the outstanding question concerning S.P. numbers has been resolved. The questions concerning S.P. numbers were first raised by S. Parameswaran in the July 1997 issue (Volume 81) of the Mathematical Gazette. The March 1998 issue (Volume 82) of the Gazette contained four short articles (by six authors) in which it was shown that any S.P. number has at most 60 digits. In addition, S.P. numbers (whose definition is given in base 10) were studied in other bases.

Within the last two months, it has been proved that the only S.P. numbers are $0$, $1$, $135$ and $144$ (originally, only positive S.P. numbers were considered, but obviously $0$ is also an S.P. number). The proofs (there are two of them) both require a computer to check a considerable number of cases, but this is not all for first it is necessary to reduce the number of cases so that a computer search is feasible (for example, one cannot check $10^{60}$ cases in a reasonable time). These two proofs will be published in the March 1999 issue of the Mathematical Gazette. Independently, Tom Sanders has written a very nice paper on the subject; well done Tom.

### [S.P. Numbers Continued][24]

by Tom Sanders, age 16, Dr Challoner's Grammar School, Amersham

The NRICH July 1998 article by Dr Alan Beardon on S.P. numbers prompted some thought on my part which I thought I might share. I will assume from hereon in that anyone who has not found the remaining S.P. number will stop reading or have their fun spoilt. The article stipulated that it was conjectured that there were only 4 S.P. numbers, namely $0$, $1$, $135$ and $144$. I have contrived a proof that there are at most finitely many S.P. numbers. Consider an '$n$' digit number:

$$n\geq 1 \quad \quad \text{ (1)}$$

$$10^{n-1}a_1 + 10^{n-2}a_2 + \ldots + a_n = z$$

N.B. $$0\leq a_i\leq 9 \text{ for } i=2 \text{ to n} \quad \text{ (2)}$$and $$1\leq a_1\leq 9$$

For $z$ to be an S.P. number we have:

$$z=\prod_{j=1}^n a_j\times \sum_{i=1}^n a_i \quad \quad \text{ (a)}$$

Let us also define: $S_n=\sum_{i=1}^n a_i$ and $P_n=\prod_{i=1}^n a_i$.

We notice that $z\geq 1$ from (1) and (2). Now for (a) to hold none of $a_i$ as $i$ ranges from $1$ to $n$ can be $0$. Thus we have the following statement:

$$z\geq 10^{n-1}+10^{n-2}+\ldots+1=k$$

This is because $k$ is the smallest $n$ digit number with no digits as $0$.

$$\Rightarrow z\geq\frac{10^n-1}{9} \quad \quad \text{ (b)}$$

N.B. See Lemma 1 for proof.

Now we also know from Lemma 2 that the following is true:

$$\frac{1}{n}\sum_{i=1}^n a_i\geq\left(\prod_{j=1}^n a_j\right)^{\frac{1}{n}}$$

Or stated another way

$$S_n^2\geq n^n P_n \quad \quad \text{ (c)}$$

(c) helps bring Lemma 2 into context.

(a) $\Rightarrow S_n P_n=z$ (a) and (b) $\Rightarrow S_n P_n \geq\frac{10^n-1}{9}\Rightarrow P_n\geq\frac{10^n-1}{9S_n}$

(c) $\Rightarrow \left(\frac{S_n}{n}\right)^n\geq P_n\geq\frac{10^n-1}{9S_n} \Rightarrow S_n\geq\left(\frac{n^n(10^n-1)}{9}\right)^{\frac{1}{n+1}}$

However we know that no digit in $z$ can be greater than $9$, so we have: $9n\geq S_n$

$$\Rightarrow 9n\geq\left(\frac{n^n(10^n-1)}{9}\right)^{\frac{1}{n+1}} \Rightarrow 81n\geq\frac{10^n-1}{9^n}$$

Solving this inequality for $n$ is hard, however since we can only have an integral number of digits we know $n$ is integral. It turns out that $n\leq 83$, we know that the right hand side of the inequality must get larger than the left hand side eventually as $n\to\infty$ since the R.H.S. is an exponential,and the L.H.S. is linear. The answer is in fact $83.7323$ to 4d.p. although I would be curious as to an analytic solution.

#### Lemma 1

We wish to prove that

$$a^{n-1}+a^{n-2}+\ldots+1=\frac{a^n-1}{a-1}$$

$$a^{n-1}+a^{n-2}+\ldots+1=S\Rightarrow S a=a^n+a^{n-1}+\ldots+a \Rightarrow aS-S=a^n-1\Rightarrow\frac{a^n-1}{a-1}$$ if $a\neq 1$

It can be trivially applied to the problem.

#### Lemma 2

This is a very well known result called the A.M. G.M. inequality. It is well worth proving to yourself before considering the proof below, it actually warrants a discussion all of its own.

$$f(x)=e^x -e x\Rightarrow f^{\prime}(x)=e^3-e\Leftrightarrow x=1$$

$$f^{\prime\prime}(1)=e> 0$$ so $x=1$ is a minimum and $f(1)=0$.

Hence we have:

$$e^x\geq e x$$ for $x\in \mathbb{R}$

Now put: $x_i=\frac{a_i}{A}$ ($i=1$, $\ldots$, $n$) Where $A=\frac{1}{n}\sum_{j=1}^n a_j$ and $a_1$, $\ldots$, $a_n\in \mathbb{R}$

Now we have

$$ \prod_{i=1}^n e^{\frac{a_i}{A}}\geq\prod_{i=1}^n\left(e\left(\frac{a_i}{A} \right)\right)\Rightarrow e^{\sum_{i=1}^n\frac{a_i}{A}}\geq\frac{e^n}{A^n} \prod_{i=1}^na_i\Rightarrow A^n\geq\prod_{i=1}^n a_i\Rightarrow\left( \sum_{j=1}^na_j\right)^n\geq n^n\prod_{i=1}^n a_i $$

The proof above shows that an S.P. number must have less than 84 digits for it to be possible. Obviously this means that there are a finite number of S.P. numbers. It is not particularly helpful however in determining that there are only 4 S.P. numbers since it would take a long time to test all numbers up to those with 84 digits. I have considered some other approaches through the use of congruence arguments, in particular I was trying to make use of the expression:

$$(P_n-1)S_n=9(11\ldots 1a_1 + \ldots + a_{n-1})$$

Clearly if one of the digits of the S.P. number is divisible by three then 9 must divide the sum, vastly reducing the possible numbers. I also note that no even digit and any fives can be in a number for it to be an S.P. number. I would be very interested to hear about any other approaches.


## Links

[1]: /tags/place-value-and-number-system
[2]: /tags/fractions-decimals-percentages-ratio-and-proportion
[3]: /tags/calculations-and-numerical-methods
[4]: /tags/algebraic-expressions-equations-and-formulae
[5]: /tags/coordinates-functions-and-graphs
[6]: /tags/patterns-sequences-and-structure
[7]: /tags/properties-numbers
[8]: /tags/transformations-and-constructions
[9]: /tags/vectors-and-matrices
[10]: /tags/measuring-and-calculating-units
[11]: /tags/pythagoras-and-trigonometry
[12]: /tags/angles-polygons-and-geometrical-proof
[13]: /tags/3d-geometry-shape-and-space
[14]: /tags/handling-processing-and-representing-data
[15]: /tags/probability-group
[16]: /tags/thinking-mathematically
[17]: /tags/mathematical-mindsets
[18]: /tags/decision-mathematics-and-combinatorics
[19]: /tags/mechanics
[20]: /tags/calculus
[21]: /tags/advanced-probability-and-statistics
[22]: /tags/early-years-foundation-stage
[23]: ../public/viewer.php?obj_id=1336
[24]: 
