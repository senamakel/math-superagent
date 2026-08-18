<!-- source: https://en.wikipedia.org/wiki/Collatz_conjecture | converted from HTML -->

Collatz conjecture - Wikipedia

Jump to content

[image: Page semi-protected] [1]

From Wikipedia, the free encyclopedia

Open problem on 3x+1 and x/2 functions

Unsolved problem in mathematics

- For even numbers, divide by 2;
- For odd numbers, multiply by 3 and add 1.

With enough repetition, do all positive integers converge to 1?

[More unsolved problems in mathematics][2]

[3] [Directed graph][4] showing the [orbits][5] of small numbers under the Collatz map, skipping even numbers. The Collatz conjecture states that all paths eventually lead to 1.

The **Collatz conjecture**{{cite book |last1=Maddux |first1=Cleborne D. |last2=Johnson |first2=D. Lamont |year=1997 |title=Logo: A Retrospective |publisher=Haworth Press |location=New York |isbn=0-7890-0374-0 |page=160 |quote=The problem is also known by several other names, including: Ulam's conjecture, the Hailstone problem, the Syracuse problem, Kakutani's problem, Hasse's algorithm, and the Collatz problem.}}</ref>{{refn|According to {{named ref|name=Lagarias (1985)}} p.&nbsp;4, the name \"Syracuse problem\" was proposed by Hasse in the 1950s, during a visit to [[Syracuse University]].}}"}},"i":0}}]}"> [a] is one of the most famous [unsolved problems in mathematics][2]. The [conjecture][6] asks whether repeating two simple arithmetic operations will eventually transform every [positive integer][7] into 1. It concerns [sequences of integers][8] in which each term is obtained from the previous term as follows: if a term is [even][9], the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. The conjecture has been shown to hold for all positive integers up to 2.36 × 10 21, but no general proof has been found.

It is named after the mathematician [Lothar Collatz][10], who introduced the idea in 1937. [4] The sequence of numbers involved is sometimes referred to as the **hailstone sequence**, **hailstone numbers**or **hailstone numerals**(because the values are usually subject to multiple descents and ascents like [hailstones][11] in a cloud), [5] or as **wondrous numbers**. [6]

[Paul Erdős][12] has said about the Collatz conjecture: "Mathematics may not be ready for such problems." [7] [Jeffrey Lagarias][13] stated in 2010 that the Collatz conjecture "is an extraordinarily difficult problem, completely out of reach of present day mathematics". [8] However, though the Collatz conjecture itself remains open, efforts to solve the problem have led to new techniques and many partial results. [8] [9]

## Statement of the problem

[14] Numbers from 1 to 9999 and their corresponding total stopping time [15] Histogram of total stopping times for the numbers 1 to 10 8. Total stopping time is on the x axis, frequency on the y axis. [16] Histogram of total stopping times for the numbers 1 to 10 9. Total stopping time is on the x axis, frequency on the y axis. [17] Iteration time for inputs of 2 to 10 7.[image: Total Stopping Time: numbers up to 250, 1000, 4000, 20000, 100000, 500000] [18] Total stopping time of numbers up to 250, 1000, 4000, 20000, 100000, 500000

Consider the following operation on an arbitrary [positive integer][7]:

- If the number is even, divide it by two.
- If the number is odd, triple it and add one.

In [modular arithmetic][19] notation, define the [function][20] f as follows: f ( n) = { n / 2 if n ≡ 0 ( mod 2), 3 n + 1 if n ≡ 1 ( mod 2). {\displaystyle f(n)={\begin{cases}n/2&{\text{if }}n\equiv 0{\pmod {2}},\\3n+1&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}[image: {\displaystyle f(n)={\begin{cases}n/2&{\text{if }}n\equiv 0{\pmod {2}},\\3n+1&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}]

Now form a sequence by performing this operation repeatedly, beginning with any positive integer, and taking the result at each step as the input at the next.

In notation: 0 \\end{cases}"}}'> 0\end{cases}}}"> a i = { n for i = 0, f ( a i − 1) for i > 0 {\displaystyle a_{i}={\begin{cases}n&{\text{for }}i=0,\\f(a_{i-1})&{\text{for }}i>0\end{cases}}} 0\end{cases}}}"/> (that is: i</sub>''"}},"i":0}}]}'>*a i*is the value of f applied to n recursively i times; i</sub>'' {{=}} ''f''{{hsp}}{{isup|''i''}}(''n'')"}},"i":0}}]}'>*a i*= *f**i*(*n*)).

The Collatz conjecture is: *This process will eventually reach the number 1, regardless of which positive integer is chosen initially. That is, for each*n {\displaystyle n}[image: {\displaystyle n}], there is some i {\displaystyle i}[image: {\displaystyle i}] with a i = 1 {\displaystyle a_{i}=1}[image: {\displaystyle a_{i}=1}].

If the conjecture is false, it can only be because there is some starting number which gives rise to a sequence that does not contain 1. Such a sequence would either enter a repeating cycle that excludes 1, or increase without bound. No such sequence has been found.

The smallest i such that i</sub>'' < ''a''<sub>0</sub> "}},"i":0}}]}'>*a i*< *a*0 is called the **stopping time**of n. Similarly, the smallest k such that k</sub>'' {{=}} 1"}},"i":0}}]}'>*a k*= 1 is called the **total stopping time**of n. [2] If one of the indexes i or k does not exist, we say that the stopping time or the total stopping time, respectively, is infinite.

The Collatz conjecture asserts that the total stopping time of every n is finite. It is also equivalent to saying that every *n*≥ 2 has a finite stopping time.

Since 3*n*+ 1 is even whenever n is odd, one may instead use the "shortcut" form of the Collatz function: f ( n) = { n 2 if n ≡ 0 ( mod 2), 3 n + 1 2 if n ≡ 1 ( mod 2). {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0{\pmod {2}},\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}[image: {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0{\pmod {2}},\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}] This definition yields smaller values for the stopping time and total stopping time without changing the overall dynamics of the process.

## Empirical data

For instance, starting with *n*= 12 and applying the function *f*without "shortcut", one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1 .

The number *n*= 19 takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 .

The sequence for *n*= 27, listed and graphed below, takes 111 steps (41 steps through odd numbers, in bold), climbing as high as 9232 before descending to 1.

**27**, 82, **41**, 124, 62, **31**, 94, **47**, 142, **71**, 214, **107**, 322, **161**, 484, 242, **121**, 364, 182, **91**, 274, **137**, 412, 206, **103**, 310, **155**, 466, **233**, 700, 350, **175**, 526, **263**, 790, **395**, 1186, **593**, 1780, 890, **445**, 1336, 668, 334, **167**, 502, **251**, 754, **377**, 1132, 566, **283**, 850, **425**, 1276, 638, **319**, 958, **479**, 1438, **719**, 2158, **1079**, 3238, **1619**, 4858, **2429**, 7288, 3644, 1822, **911**, 2734, **1367**, 4102, **2051**, 6154, **3077**, 9232, 4616, 2308, 1154, **577**, 1732, 866, **433**, 1300, 650, **325**, 976, 488, 244, 122, **61**, 184, 92, 46, **23**, 70, **35**, 106, **53**, 160, 80, 40, 20, 10, **5**, 16, 8, 4, 2, **1**

(sequence [A008884][21] in the [OEIS][22])

[23]

Numbers with a total stopping time longer than that of any smaller starting value form a sequence beginning with:

1, 2, 3, 6, 7, 9, 18, 25, 27, 54, 73, 97, 129, 171, 231, 313, 327, 649, 703, 871, 1161, 2223, 2463, 2919, 3711, 6171, ... (sequence [A006877][24] in the [OEIS][22]).

The starting values whose [maximum][25] trajectory point is greater than that of any smaller starting value are as follows:

1, 2, 3, 7, 15, 27, 255, 447, 639, 703, 1819, 4255, 4591, 9663, 20895, 26623, 31911, 60975, 77671, 113383, 138367, 159487, 270271, 665215, 704511, ... (sequence [A006884][26] in the [OEIS][22])

Number of steps for n to reach 1 are

0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20, 7, 7, 15, 15, 10, 23, 10, 111, 18, 18, 18, 106, 5, 26, 13, 13, 21, 21, 21, 34, 8, 109, 8, 29, 16, 16, 16, 104, 11, 24, 24, ... (sequence [A006577][27] in the [OEIS][22])

The starting value having the largest total stopping time while being

less than 10 is 9, which has 19 steps, less than 100 is 97, which has 118 steps, less than 1000 is 871, which has 178 steps, less than 10 4 is 6171, which has 261 steps, less than 10 5 is 77 031, which has 350 steps, less than 10 6 is 837 799, which has 524 steps, less than 10 7 is 8 400 511, which has 685 steps, less than 10 8 is 63 728 127, which has 949 steps, less than 10 9 is 670 617 279, which has 986 steps, less than 10 10 is 9 780 657 630, which has 1132 steps, [10] less than 10 11 is 75 128 138 247, which has 1228 steps, less than 10 12 is 989 345 275 647, which has 1348 steps. [11] (sequence [A284668][28] in the [OEIS][22])

These numbers are the lowest ones with the indicated step count, but not necessarily the only ones below the given limit. As an example, 9 780 657 631 has 1132 steps, as does 9 780 657 630.

The starting values having the smallest total stopping time with respect to their number of digits (in base 2) are the [powers of two][29], since ''n''</sup>"}},"i":0}}]}'>2*n*is halved n times to reach 1, and it is never increased.

## Visualizations

-

[image: Directed graph showing the orbits of the first 1000 numbers.] [30]

Directed graph showing the orbits of the first 1000 numbers.

-

[image: The x axis represents starting number, the y axis represents the highest number reached during the chain to 1. This plot shows a restricted y axis: some x values produce intermediates as high as 2.7×107 (for x = 9663)] [31]

The x axis represents starting number, the y axis represents the highest number reached during the chain to 1. This plot shows a restricted y axis: some x values produce intermediates as high as 2.7 × 10 7 (for *x*= 9663)

-

[image: The same plot as the previous one but on log scale, so all y values are shown. The first thick line towards the middle of the plot corresponds to the tip at 27, which reaches a maximum at 9232.] [32]

The same plot as the previous one but on log scale, so all y values are shown. The first thick line towards the middle of the plot corresponds to the tip at 27, which reaches a maximum at 9232.

-

[image: The tree of all the numbers having fewer than 20 steps.] [33]

The tree of all the numbers having fewer than 20 steps.

-

[image: Collatz Conjecture 100M] [34]

The number of iterations it takes to get to one for the first 100 million numbers.

-

[image: Collatz conjecture paths for 5000 random starting points below 1 million.] [35]

Collatz conjecture paths for 5000 random starting points below 1 million.

## Supporting arguments

Although the conjecture has not been proven, most mathematicians [*[citation needed][36]*] who have looked into the problem think the conjecture is true because experimental evidence and heuristic arguments support it.

### Experimental evidence

The conjecture has been checked by computer for all starting values up to 2 71 ≈ 2.36 × 10 21. All values tested so far converge to 1. [12]

This computer evidence is still not rigorous proof that the conjecture is true for all starting values, as [counterexamples][37] may be found when considering very large positive integers, as in the case of the disproven [Pólya conjecture][38] and [Mertens conjecture][39].

However, such verifications may have other implications. Certain constraints on any non-trivial cycle, such as [lower bounds][40] on the length of the cycle, can be proven based on the value of the lowest term in the cycle. Therefore, computer searches to rule out cycles that have a small lowest term can strengthen these constraints. [13] [14] [15]

### A probabilistic heuristic

If one considers only the *odd*numbers in the sequence generated by the Collatz process, then each odd number is on average ⁠ 3 / 4 ⁠ of the previous one. [16] (More precisely, the geometric mean of the ratios of outcomes is ⁠ 3 / 4 ⁠.) This yields a heuristic argument that every Hailstone sequence should decrease in the long run, although this is not evidence against other cycles, only against divergence. The argument is not a proof, however, because it assumes that Hailstone sequences are assembled from uncorrelated probabilistic events. (It does rigorously establish that the [2-adic][41] extension of the Collatz process has two division steps for every multiplication step for [almost all][42] 2-adic starting values.)

### Stopping times

As proven by [Riho Terras][43], almost every positive integer has a finite stopping time. [b] [17] In other words, almost every Collatz sequence reaches a point that is strictly below its initial value. The proof is based on the distribution of parity vectors and uses the [central limit theorem][44].

In 2019, [Terence Tao][45] improved this result by showing, using [logarithmic density][46], that [almost all][42] (in the sense of logarithmic density) Collatz orbits descend below any given function of the starting point, provided that this function diverges to infinity, no matter how slowly. Responding to this work, *[Quanta Magazine][47]*wrote that Tao "came away with one of the most significant results on the Collatz conjecture in decades". [9] [18]

### Lower bounds

In a [computer-aided proof][48], Krasikov and Lagarias showed that the number of integers in the interval [1,*x*] that eventually reach 1 is at least equal to 0.84</sup>"}},"i":0}}]}'>*x*0.84 for all sufficiently large x. [19]

## Cycles

In this part, consider the shortcut form of the Collatz function f ( n) = { n 2 if n ≡ 0 ( mod 2), 3 n + 1 2 if n ≡ 1 ( mod 2). {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0{\pmod {2}},\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}[image: {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0{\pmod {2}},\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1{\pmod {2}}.\end{cases}}}] A [cycle][49] is a sequence 0</sub>, ''a''<sub>1</sub>, ..., ''a<sub>q</sub>'')"}},"i":0}}]}'>(*a*0, *a*1, ..., *a q*) of distinct positive integers where 0</sub>) {{=}} ''a''<sub>1</sub>"}},"i":0}}]}'>*f*(*a*0) = *a*1, 1</sub>) {{=}} ''a''<sub>2</sub>"}},"i":0}}]}'>*f*(*a*1) = *a*2, ..., and q</sub>'') {{=}} ''a''<sub>0</sub>"}},"i":0}}]}'>*f*(*a q*) = *a*0.

The only known cycle is (1,2) of period 2, called the trivial cycle.

### Cycle length

As of 2025, the best known bound on cycle length is 217 976 794 617 ( 355 504 839 929 without shortcut). [12] In 1993, Eliahou proved that the period p of any non-trivial cycle is of the form p = 301994 a + 17087915 b + 85137581 c {\displaystyle p=301994a+17087915b+85137581c}[image: {\displaystyle p=301994a+17087915b+85137581c}] where a, b and c are non-negative integers, *b*≥ 1 and *ac*= 0. This result is based on the [simple continued fraction][50] expansion of ⁠ ln 3 / ln 2 ⁠. [14]

### k -cycles

A k -cycle is a cycle that can be partitioned into *k*contiguous subsequences, each consisting of an increasing sequence of odd numbers, followed by a decreasing sequence of even numbers. [15] For instance, if the cycle consists of a single increasing sequence of odd numbers followed by a decreasing sequence of even numbers, it is called a *1-cycle*.

Steiner (1977) proved that there is no 1-cycle other than the trivial (1; 2). [20] Simons (2005) used Steiner's method to prove that there is no 2-cycle. [21] Simons and de Weger (2005) extended this proof up to 68-cycles; there is no k -cycle up to *k*= 68. [15] Hercher extended the method further and proved that there exists no *k*-cycle with *k*≤ 91. [22] As exhaustive computer searches continue, larger *k*values may be ruled out. To state the argument more intuitively; we do not have to search for cycles that have less than 92 subsequences, where each subsequence consists of consecutive ups followed by consecutive downs. [*[clarification needed][51]*]

## Other formulations of the conjecture

### In reverse

[52] The first 21 levels of the *Collatz [graph][53]*generated in bottom-up fashion. The graph includes all numbers with an orbit length of 21 or less.

There is another approach to prove the conjecture, which considers the bottom-up method of growing the so-called *Collatz graph*, a [graph][53] defined by the inverse [relation][54] R ( n) = { { 2 n } if n ≡ 0, 1, 2, 3, 5 { 2 n, n − 1 3 } if n ≡ 4 ( mod 6). {\displaystyle R(n)={\begin{cases}\{2n\}&{\text{if }}n\equiv 0,1,2,3,5\\\left\{2n,{\frac {n-1}{3}}\right\}&{\text{if }}n\equiv 4\end{cases}}{\pmod {6}}.}[image: {\displaystyle R(n)={\begin{cases}\{2n\}&{\text{if }}n\equiv 0,1,2,3,5\\\left\{2n,{\frac {n-1}{3}}\right\}&{\text{if }}n\equiv 4\end{cases}}{\pmod {6}}.}]

So, instead of proving that all positive integers eventually lead to 1, we can try to prove that 1 leads backwards to all positive integers. For any integer n, *n*≡ 1 (mod 2) [if and only if][55] 3*n*+ 1 ≡ 4 (mod 6). Equivalently, ⁠*n*− 1 / 3 ⁠ ≡ 1 (mod 2) if and only if *n*≡ 4 (mod 6). Conjecturally, this inverse relation forms a [tree][56] for positive integers except for the 1–2–4 loop (the inverse of the 4–2–1 loop of the unaltered function f defined in the Statement of the problem section of this article).

When the relation 3*n*+ 1 of the function f is replaced by the common substitute "shortcut" relation ⁠ 3*n*+ 1 / 2 ⁠, the Collatz graph is defined by the inverse relation, R ( n) = { { 2 n } if n ≡ 0, 1 { 2 n, 2 n − 1 3 } if n ≡ 2 ( mod 3). {\displaystyle R(n)={\begin{cases}\{2n\}&{\text{if }}n\equiv 0,1\\\left\{2n,{\frac {2n-1}{3}}\right\}&{\text{if }}n\equiv 2\end{cases}}{\pmod {3}}.}[image: {\displaystyle R(n)={\begin{cases}\{2n\}&{\text{if }}n\equiv 0,1\\\left\{2n,{\frac {2n-1}{3}}\right\}&{\text{if }}n\equiv 2\end{cases}}{\pmod {3}}.}]

For any integer n, *n*≡ 1 (mod 2) if and only if ⁠ 3*n*+ 1 / 2 ⁠ ≡ 2 (mod 3). Equivalently, ⁠ 2*n*− 1 / 3 ⁠ ≡ 1 (mod 2) if and only if *n*≡ 2 (mod 3). Conjecturally, this inverse relation forms a tree for positive integers except for a 1–2 loop (the inverse of the 1–2 loop of the function f(n) revised as indicated above).

Alternatively, replace the 3*n*+ 1 with ⁠*n*′ /*H*(*n*′) ⁠ where *n*′ = 3*n*+ 1 and *H*(*n*′) is the highest [power of 2][57] that divides *n*′ (with no [remainder][58]). The resulting function f maps from [odd numbers][59] to odd numbers. Now suppose that for some odd number n, applying this operation k times yields the number 1 (that is, *f**k*(*n*) = 1). Then in [binary][60], the number n can be written as the concatenation of [strings][61] ''k''</sub> ''w''<sub>''k''−1</sub> ... ''w''<sub>1</sub>"}},"i":0}}]}'>*w**k**w**k*−1... *w*1 where each ''h''</sub>"}},"i":0}}]}'>*w**h*is a finite and contiguous extract from the representation of ''h''</sup>}}"}},"i":0}}]}'> ⁠ 1 / 3*h*⁠. [23] The representation of n therefore holds the [repetends][62] of ''h''</sup>}}"}},"i":0}}]}'> ⁠ 1 / 3*h*⁠, where each repetend is optionally rotated and then replicated up to a finite number of bits. It is only in binary that this occurs. [24] Conjecturally, every binary string s that ends with a '1' can be reached by a representation of this form (where we may add or delete leading '0's to s).

### As an abstract machine that computes in base two

Repeated applications of the Collatz function can be represented as an [abstract machine][63] that handles [strings][61] of [bits][64]. The machine will perform the following three steps on any odd number until only one 1 remains:

1. Append 1 to the (right) end of the number in binary (giving 2*n*+ 1);
2. Add this to the original number by binary addition (giving 2*n*+ 1 + *n*= 3*n*+ 1);
3. Remove all trailing 0 s (that is, repeatedly divide by 2 until the result is odd).

#### Example

The starting number 7 is written in [binary][65] as 111. The resulting Collatz sequence is:

```
         111
        111**1**
       10110
      1011**1**
     100010
    10001**1**
    110100
   1101**1**
  101000
 101**1**
10000
```

### As a parity sequence

For this section, consider the shortcut form of the Collatz function f ( n) = { n 2 if n ≡ 0 3 n + 1 2 if n ≡ 1 ( mod 2). {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1\end{cases}}{\pmod {2}}.}[image: {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1\end{cases}}{\pmod {2}}.}]

If P(...) is the parity of a number, that is P(2*n*) = 0 and P(2*n*+ 1) = 1, then we can define the Collatz parity sequence (or parity vector) for a number n as i</sub>'' {{=}} P(''a<sub>i</sub>'')"}},"i":0}}]}'>*p i*= P(*a i*), where 0</sub> {{=}} ''n''"}},"i":0}}]}'>*a*0 = *n*, and ''i''+1</sub> {{=}} ''f''(''a''<sub>''i''</sub>)"}},"i":0}}]}'>*a**i*+1 = *f*(*a**i*).

Which operation is performed, ⁠ 3*n*+ 1 / 2 ⁠ or ⁠*n*/ 2 ⁠, depends on the parity. The parity sequence is the same as the sequence of operations.

Using this form for *f*(*n*), it can be shown that the parity sequences for two numbers m and n will agree in the first k terms if and only if m and n are equivalent modulo ''k''</sup>"}},"i":0}}]}'>2*k*. This implies that every number is uniquely identified by its parity sequence, and moreover that if there are multiple Hailstone cycles, then their corresponding parity cycles must be different. [2] [17]

Applying the f function k times to the number ''k''</sup>''a'' + ''b''"}},"i":0}}]}'>*n*= 2*k**a*+ *b*will give the result ''c''</sup>''a'' + ''d''"}},"i":0}}]}'>3*c**a*+ *d*, where d is the result of applying the f function k times to b, and c is how many increases were encountered during that sequence. For example, for 5</sup>''a'' + 1"}},"i":0}}]}'>2 5*a*+ 1 there are 3 increases as 1 iterates to 2, 1, 2, 1, and finally to 2 so the result is 3</sup>''a'' + 2"}},"i":0}}]}'>3 3*a*+ 2; for 2</sup>''a'' + 1"}},"i":0}}]}'>2 2*a*+ 1 there is only 1 increase as 1 rises to 2 and falls to 1 so the result is 3*a*+ 1. When b is ''k''</sup> − 1"}},"i":0}}]}'>2*k*− 1 then there will be k rises and the result will be ''k''</sup>''a'' + 3<sup>''k''</sup> − 1"}},"i":0}}]}'>3*k**a*+ 3*k*− 1. The power of 3 multiplying a is independent of the value of a; it depends only on the behavior of b. This allows one to predict that certain forms of numbers will always lead to a smaller number after a certain number of iterations: for example, 4*a*+ 1 becomes 3*a*+ 1 after two applications of f and 16*a*+ 3 becomes 9*a*+ 2 after four applications of f. Whether those smaller numbers continue to 1, however, depends on the value of a.

### As a tag system

For the Collatz function in the shortcut form

f ( n) = { n 2 if n ≡ 0 3 n + 1 2 if n ≡ 1. ( mod 2) {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1.\end{cases}}{\pmod {2}}}[image: {\displaystyle f(n)={\begin{cases}{\frac {n}{2}}&{\text{if }}n\equiv 0\\{\frac {3n+1}{2}}&{\text{if }}n\equiv 1.\end{cases}}{\pmod {2}}}]

Hailstone sequences can be computed by the [2-tag system][66] with production rules

*a*→ *bc*, *b*→ *a*, *c*→ *aaa*.

In this system, the positive integer n is represented by a string of n copies of a, and iteration of the tag operation halts on any word of length less than 2. (Adapted from De Mol.)

The Collatz conjecture equivalently states that this tag system, with an arbitrary finite string of a as the initial word, eventually halts (see *[Tag system][66]*for a worked example).

## Extensions to larger domains

### Iterating on all integers

An extension to the Collatz conjecture is to include all integers, not just positive integers. Leaving aside the cycle 0 → 0 which cannot be entered from outside, there are a total of four known cycles, which all nonzero integers seem to eventually fall into under iteration of f. These cycles are listed here, starting with the well-known cycle for positive n:

Odd values are listed in large bold. Each cycle is listed with its member of least absolute value (which is always odd) first.

Cycle | Odd-value cycle length | Full cycle length |

**1**→ 4 → 2 → **1****...** | 1 | 3 |

**−1**→ −2 → **−1****...** | 1 | 2 |

**−5**→ −14 → **−7**→ −20 → −10 → **−5****...** | 2 | 5 |

**−17**→ −50 → **−25**→ −74 → **−37**→ −110 → **−55**→ −164 → −82 → **−41**→ −122 → **−61**→ −182 → **−91**→ −272 → −136 → −68 → −34 → **−17****...** | 7 | 18 |

The generalized Collatz conjecture is the assertion that every integer, under iteration by f, eventually falls into one of the four cycles above or the cycle 0 → 0.

### Iterating on rationals with odd denominators

The Collatz map can be extended to (positive or negative) rational numbers which have odd denominators when written in lowest terms. The number is taken to be 'odd' or 'even' according to whether its numerator is odd or even. Then the formula for the map is exactly the same as when the domain is the integers: an 'even' such rational is divided by 2; an 'odd' such rational is multiplied by 3 and then 1 is added. A closely related fact is that the Collatz map extends to the ring of [2-adic integers][67], which contains the ring of rationals with odd denominators as a subring.

When using the "shortcut" definition of the Collatz map, it is known that any periodic parity sequence is generated by exactly one rational. [25] Conversely, it is conjectured that every rational with an odd denominator has an eventually cyclic parity sequence (Periodicity Conjecture [2]).

If a parity cycle has length n and includes odd numbers exactly m times at indices 0</sub> < ⋯ < ''k''<sub>''m''−1</sub>"}},"i":0}}]}'>*k*0 < ⋯ < *k**m*−1, then the unique rational which generates immediately and periodically this parity cycle is

\\frac{3^{m-1} 2^{k_0} + \\cdots + 3^0 2^{k_{m-1}}}{2^n - 3^m}.</math>"},"3":{"wt":"{{EquationRef|1}}"}},"i":0}}]}'>

3 m − 1 2 k 0 + ⋯ + 3 0 2 k m − 1 2 n − 3 m. {\displaystyle {\frac {3^{m-1}2^{k_{0}}+\cdots +3^{0}2^{k_{m-1}}}{2^{n}-3^{m}}}.}[image: {\displaystyle {\frac {3^{m-1}2^{k_{0}}+\cdots +3^{0}2^{k_{m-1}}}{2^{n}-3^{m}}}.}] |  | 1 |

For example, the parity cycle (1 0 1 1 0 0 1) has length 7 and four odd terms at indices 0, 2, 3, and 6. It is repeatedly generated by the fraction 3 3 2 0 + 3 2 2 2 + 3 1 2 3 + 3 0 2 6 2 7 − 3 4 = 151 47 {\displaystyle {\frac {3^{3}2^{0}+3^{2}2^{2}+3^{1}2^{3}+3^{0}2^{6}}{2^{7}-3^{4}}}={\frac {151}{47}}}[image: {\displaystyle {\frac {3^{3}2^{0}+3^{2}2^{2}+3^{1}2^{3}+3^{0}2^{6}}{2^{7}-3^{4}}}={\frac {151}{47}}}] as the latter leads to the rational cycle 151 47 → 250 47 → 125 47 → 211 47 → 340 47 → 170 47 → 85 47 → 151 47. {\displaystyle {\frac {151}{47}}\rightarrow {\frac {250}{47}}\rightarrow {\frac {125}{47}}\rightarrow {\frac {211}{47}}\rightarrow {\frac {340}{47}}\rightarrow {\frac {170}{47}}\rightarrow {\frac {85}{47}}\rightarrow {\frac {151}{47}}.}[image: {\displaystyle {\frac {151}{47}}\rightarrow {\frac {250}{47}}\rightarrow {\frac {125}{47}}\rightarrow {\frac {211}{47}}\rightarrow {\frac {340}{47}}\rightarrow {\frac {170}{47}}\rightarrow {\frac {85}{47}}\rightarrow {\frac {151}{47}}.}]

Any cyclic permutation of (1 0 1 1 0 0 1) is associated to one of the above fractions. For instance, the cycle (0 1 1 0 0 1 1) is produced by the fraction 3 3 2 1 + 3 2 2 2 + 3 1 2 5 + 3 0 2 6 2 7 − 3 4 = 250 47. {\displaystyle {\frac {3^{3}2^{1}+3^{2}2^{2}+3^{1}2^{5}+3^{0}2^{6}}{2^{7}-3^{4}}}={\frac {250}{47}}.}[image: {\displaystyle {\frac {3^{3}2^{1}+3^{2}2^{2}+3^{1}2^{5}+3^{0}2^{6}}{2^{7}-3^{4}}}={\frac {250}{47}}.}]

For a one-to-one correspondence, a parity cycle should be *irreducible*, that is, not partitionable into identical sub-cycles. As an illustration of this, the parity cycle (1 1 0 0 1 1 0 0) and its sub-cycle (1 1 0 0) are associated to the same fraction ⁠ 5 / 7 ⁠ when reduced to lowest terms.

In this context, assuming the validity of the Collatz conjecture implies that (1 0) and (0 1) are the only parity cycles generated by positive whole numbers (1 and 2, respectively).

If the odd denominator d of a rational is not a multiple of 3, then all the iterates have the same denominator and the sequence of numerators can be obtained by applying the " 3*n*+ *d*" generalization [26] of the Collatz function T d ( x) = { x 2 if x ≡ 0 ( mod 2), 3 x + d 2 if x ≡ 1 ( mod 2). {\displaystyle T_{d}(x)={\begin{cases}{\frac {x}{2}}&{\text{if }}x\equiv 0{\pmod {2}},\\{\frac {3x+d}{2}}&{\text{if }}x\equiv 1{\pmod {2}}.\end{cases}}}[image: {\displaystyle T_{d}(x)={\begin{cases}{\frac {x}{2}}&{\text{if }}x\equiv 0{\pmod {2}},\\{\frac {3x+d}{2}}&{\text{if }}x\equiv 1{\pmod {2}}.\end{cases}}}]

### 2-adic extension

The function T ( x) = { x 2 if x ≡ 0 ( mod 2) 3 x + 1 2 if x ≡ 1 ( mod 2) {\displaystyle T(x)={\begin{cases}{\frac {x}{2}}&{\text{if }}x\equiv 0{\pmod {2}}\\{\frac {3x+1}{2}}&{\text{if }}x\equiv 1{\pmod {2}}\end{cases}}}[image: {\displaystyle T(x)={\begin{cases}{\frac {x}{2}}&{\text{if }}x\equiv 0{\pmod {2}}\\{\frac {3x+1}{2}}&{\text{if }}x\equiv 1{\pmod {2}}\end{cases}}}] is well-defined on the ring Z 2 {\displaystyle \mathbb {Z} _{2}}[image: {\displaystyle \mathbb {Z} _{2}}] of [2-adic integers][67], where it is continuous and [measure-preserving][68] with respect to the 2-adic measure. Moreover, its dynamics is known to be [ergodic][69]. [2]

Define the *parity vector*function Q acting on Z 2 {\displaystyle \mathbb {Z} _{2}}[image: {\displaystyle \mathbb {Z} _{2}}] as Q ( x) = ∑ k = 0 ∞ ( T k ( x) mod 2) 2 k. {\displaystyle Q(x)=\sum _{k=0}^{\infty }\left(T^{k}(x){\bmod {2}}\right)2^{k}.}[image: {\displaystyle Q(x)=\sum _{k=0}^{\infty }\left(T^{k}(x){\bmod {2}}\right)2^{k}.}]

The function Q is a 2-adic [isometry][70]. [27] Consequently, every infinite parity sequence occurs for exactly one 2-adic integer, so that [almost all][42] trajectories are acyclic in Z 2 {\displaystyle \mathbb {Z} _{2}}[image: {\displaystyle \mathbb {Z} _{2}}].

An equivalent formulation of the Collatz conjecture is that Q ( Z +) ⊂ 1 3 Z. {\displaystyle Q\left(\mathbb {Z} ^{+}\right)\subset {\tfrac {1}{3}}\mathbb {Z} .}[image: {\displaystyle Q\left(\mathbb {Z} ^{+}\right)\subset {\tfrac {1}{3}}\mathbb {Z} .}]

### Iterating on real or complex numbers

[71] [Cobweb plot][72] of the orbit 10 → 5 → 8 → 4 → 2 → 1 → ... in an extension of the Collatz map to the real line.

The Collatz map can be extended to the [real line][73] by choosing any function which evaluates to x / 2 {\displaystyle x/2}[image: {\displaystyle x/2}] when x {\displaystyle x}[image: {\displaystyle x}] is an even integer, and to either 3 x + 1 {\displaystyle 3x+1}[image: {\displaystyle 3x+1}] or ( 3 x + 1) / 2 {\displaystyle (3x+1)/2}[image: {\displaystyle (3x+1)/2}] (for the "shortcut" version) when x {\displaystyle x}[image: {\displaystyle x}] is an odd integer. This is called an [interpolating][74] function. A simple way to do this is to pick two functions g 1 {\displaystyle g_{1}}[image: {\displaystyle g_{1}}] and g 2 {\displaystyle g_{2}}[image: {\displaystyle g_{2}}], where:

g 1 ( n) = { 1, n is even, 0, n is odd, {\displaystyle g_{1}(n)={\begin{cases}1,&n{\text{ is even,}}\\0,&n{\text{ is odd,}}\end{cases}}}[image: {\displaystyle g_{1}(n)={\begin{cases}1,&n{\text{ is even,}}\\0,&n{\text{ is odd,}}\end{cases}}}] g 2 ( n) = { 0, n is even, 1, n is odd, {\displaystyle g_{2}(n)={\begin{cases}0,&n{\text{ is even,}}\\1,&n{\text{ is odd,}}\end{cases}}}[image: {\displaystyle g_{2}(n)={\begin{cases}0,&n{\text{ is even,}}\\1,&n{\text{ is odd,}}\end{cases}}}]

and use them as switches for our desired values:

f ( x) = x 2 ⋅ g 1 ( x) + 3 x + 1 2 ⋅ g 2 ( x) {\displaystyle f(x)={\frac {x}{2}}\cdot g_{1}(x)\,+\,{\frac {3x+1}{2}}\cdot g_{2}(x)}[image: {\displaystyle f(x)={\frac {x}{2}}\cdot g_{1}(x)\,+\,{\frac {3x+1}{2}}\cdot g_{2}(x)}].

One such choice is g 1 ( x) = cos 2 ⁡ ( π 2 x) {\displaystyle g_{1}(x)=\cos ^{2}\left({\tfrac {\pi }{2}}x\right)}[image: {\displaystyle g_{1}(x)=\cos ^{2}\left({\tfrac {\pi }{2}}x\right)}] and g 2 ( x) = sin 2 ⁡ ( π 2 x) {\displaystyle g_{2}(x)=\sin ^{2}\left({\tfrac {\pi }{2}}x\right)}[image: {\displaystyle g_{2}(x)=\sin ^{2}\left({\tfrac {\pi }{2}}x\right)}]. The [iterations][75] of this map lead to a [dynamical system][76], further investigated by Marc Chamberland. [28] He showed that the conjecture does not hold for positive real numbers since there are infinitely many [fixed points][77], as well as [orbits][5] escaping [monotonically][78] to infinity. The function f {\displaystyle f}[image: {\displaystyle f}] has two [attracting][79] cycles of period 2 {\displaystyle 2}[image: {\displaystyle 2}]: ( 1; 2) {\displaystyle (1;\,2)}[image: {\displaystyle (1;\,2)}] and ( 1.1925...; 2.1386...) {\displaystyle (1.1925...;\,2.1386...)}[image: {\displaystyle (1.1925...;\,2.1386...)}]. Moreover, the set of unbounded orbits is conjectured to be of [measure][80] 0 {\displaystyle 0}[image: {\displaystyle 0}].

Letherman, Schleicher, and Wood extended the study to the [complex plane][81]. [29] They used Chamberland's function for [complex sine and cosine][82] and added the extra term 1 π ( 1 2 − cos ⁡ ( π z)) sin ⁡ ( π z) + {\displaystyle {\tfrac {1}{\pi }}\left({\tfrac {1}{2}}-\cos(\pi z)\right)\sin(\pi z)\,+}[image: {\displaystyle {\tfrac {1}{\pi }}\left({\tfrac {1}{2}}-\cos(\pi z)\right)\sin(\pi z)\,+}] h ( z) sin 2 ⁡ ( π z) {\displaystyle h(z)\sin ^{2}(\pi z)}[image: {\displaystyle h(z)\sin ^{2}(\pi z)}], where h ( z) {\displaystyle h(z)}[image: {\displaystyle h(z)}] is any [entire function][83]. Since this expression evaluates to zero for real integers, the extended function

f ( z) = z 2 cos 2 ⁡ ( π 2 z) + 3 z + 1 2 sin 2 ⁡ ( π 2 z) + 1 π ( 1 2 − cos ⁡ ( π z)) sin ⁡ ( π z) + h ( z) sin 2 ⁡ ( π z) {\displaystyle {\begin{aligned}f(z)=\;&{\frac {z}{2}}\cos ^{2}\left({\frac {\pi }{2}}z\right)+{\frac {3z+1}{2}}\sin ^{2}\left({\frac {\pi }{2}}z\right)\,+\\&{\frac {1}{\pi }}\left({\frac {1}{2}}-\cos(\pi z)\right)\sin(\pi z)+h(z)\sin ^{2}(\pi z)\end{aligned}}}[image: {\displaystyle {\begin{aligned}f(z)=\;&{\frac {z}{2}}\cos ^{2}\left({\frac {\pi }{2}}z\right)+{\frac {3z+1}{2}}\sin ^{2}\left({\frac {\pi }{2}}z\right)\,+\\&{\frac {1}{\pi }}\left({\frac {1}{2}}-\cos(\pi z)\right)\sin(\pi z)+h(z)\sin ^{2}(\pi z)\end{aligned}}}]

is an interpolation of the Collatz map to the complex plane. The reason for adding the extra term is to make all integers [critical points][84] of f {\displaystyle f}[image: {\displaystyle f}]. With this, they show that no integer is in a [Baker domain][85], which implies that any integer is either eventually periodic or belongs to a [wandering domain][86]. They conjectured that the latter is not the case, which would make all integer orbits finite.

[87] A Collatz [fractal][88] centered at the origin, with real parts from –5 to 5.

Most of the points have orbits that diverge to infinity. Coloring these points based on how fast they diverge produces the image on the left, for h ( z) = 0 {\displaystyle h(z)=0}[image: {\displaystyle h(z)=0}]. The inner black regions and the outer region are the [Fatou components][89], and the boundary between them is the [Julia set][90] of f {\displaystyle f}[image: {\displaystyle f}], which forms a [fractal][88] pattern, sometimes called a "Collatz fractal".

[91] Julia set of the exponential interpolation.

There are many other ways to define a complex interpolating function, such as using the [complex exponential][92] instead of sine and cosine:

f ( z) = z 2 + 1 4 ( 2 z + 1) ( 1 − e i π z) {\displaystyle f(z)={\frac {z}{2}}+{\frac {1}{4}}(2z+1)\left(1-e^{i\pi z}\right)}[image: {\displaystyle f(z)={\frac {z}{2}}+{\frac {1}{4}}(2z+1)\left(1-e^{i\pi z}\right)}],

which exhibit different dynamics. In this case, for instance, if Im ⁡ ( z) ≫ 1 {\displaystyle \operatorname {Im} (z)\gg 1}[image: {\displaystyle \operatorname {Im} (z)\gg 1}], then f ( z) ≈ z + 1 4 {\displaystyle f(z)\approx z+{\tfrac {1}{4}}}[image: {\displaystyle f(z)\approx z+{\tfrac {1}{4}}}]. The corresponding Julia set, shown on the right, consists of uncountably many curves, called *hairs*, or *rays*.

## Optimizations

### Time–space tradeoff

The section *As a parity sequence*above gives a way to speed up simulation of the sequence. To jump ahead k steps on each iteration (using the f function from that section), break up the current number into two parts, b (the k least significant bits, interpreted as an integer), and a (the rest of the bits as an integer). The result of jumping ahead k is given by

''k''</sup>''a'' + ''b'') {{=}} 3<sup>''c''(''b'', ''k'')</sup>''a'' + ''d''(''b'', ''k'')"}},"i":0}}]}">*f**k*(2*k**a*+ *b*) = 3*c*(*b*, *k*)*a*+ *d*(*b*, *k*).

The values of c (or better ''c''</sup>"}},"i":0}}]}'>3*c*) and d can be precalculated for all possible k -bit numbers b, where *d*(*b*, *k*) is the result of applying the f function k times to b, and *c*(*b*, *k*) is the number of odd numbers encountered on the way. [30] For example, if *k*= 5, one can jump ahead 5 steps on each iteration by separating out the 5 least significant bits of a number and using

c (0...31, 5) = { 0, 3, 2, 2, 2, 2, 2, 4, 1, 4, 1, 3, 2, 2, 3, 4, 1, 2, 3, 3, 1, 1, 3, 3, 2, 3, 2, 4, 3, 3, 4, 5 }, d (0...31, 5) = { 0, 2, 1, 1, 2, 2, 2, 20, 1, 26, 1, 10, 4, 4, 13, 40, 2, 5, 17, 17, 2, 2, 20, 20, 8, 22, 8, 71, 26, 26, 80, 242 }.

This requires ''k''</sup>"}},"i":0}}]}'>2*k*[precomputation][93] and storage to speed up the resulting calculation by a factor of k, a [space–time tradeoff][94].

### Modular restrictions

For the special purpose of searching for a counterexample to the Collatz conjecture, this precomputation leads to an even more important acceleration, used by Tomás Oliveira e Silva in his computational confirmations of the Collatz conjecture up to large values of n. If, for some given b and k, the inequality

''k''</sup>''a'' + ''b'') {{=}} 3<sup>''c''(''b'')</sup>''a'' + ''d''(''b'') < 2<sup>''k''</sup>''a'' + ''b''"}},"i":0}}]}">*f**k*(2*k**a*+ *b*) = 3*c*(*b*)*a*+ *d*(*b*) < 2*k**a*+ *b*

holds for all a, then the first counterexample, if it exists, cannot be b modulo ''k''</sup>"}},"i":0}}]}'>2*k*. [13] For instance, the first counterexample must be odd because *f*(2*n*) = *n*, smaller than 2*n*; and it must be 3 mod 4 because *f*2 (4*n*+ 1) = 3*n*+ 1, smaller than 4*n*+ 1. For each starting value a which is not a counterexample to the Collatz conjecture, there is a k for which such an inequality holds, so checking the Collatz conjecture for one starting value is as good as checking an entire congruence class. As k increases, the search only needs to check those residues b that are not eliminated by lower values of k. Only an exponentially small fraction of the residues survive. [31] For example, the only surviving residues mod 32 are 7, 15, 27, and 31.

Integers divisible by 3 cannot form a cycle, so these integers do not need to be checked as counterexamples. [32]

## Syracuse function

If k is an odd integer, then 3*k*+ 1 is even, so ''a''</sup>''k''{{prime}}"}},"i":0}}]}'>3*k*+ 1 = 2*a**k*′ with *k*′ odd and *a*≥ 1. The **Syracuse function**is the function f from the set I of positive odd integers into itself, for which *f*(*k*) = *k*′ (sequence [A075677][95] in the [OEIS][22]).

Some properties of the Syracuse function are:

- For all *k*∈ *I*, *f*(4*k*+ 1) = *f*(*k*). (Because 3(4*k*+ 1) + 1 = 12*k*+ 4 = 4(3*k*+ 1).)
- In more generality: For all *p*≥ 1 and odd h, ''p''</sup>''h'' − 1) {{=}} 2 × 3<sup>''p'' − 1</sup>''h'' − 1"}},"i":0}}]}">*f**p*− 1 (2*p**h*− 1) = 2 × 3*p*− 1*h*− 1. (Here *f**p*− 1 is [function iteration notation][96].)
- For all odd h, *f*(2*h*− 1) ≤ ⁠ 3*h*− 1 / 2 ⁠

The Collatz conjecture is equivalent to the statement that, for all k in I, there exists an integer *n*≥ 1 such that *f**n*(*k*) = 1.

## Undecidable generalizations

In 1972, [John Horton Conway][97] proved that a natural generalization of the Collatz problem is algorithmically [undecidable][98]. [33]

Specifically, he considered functions of the form g ( n) = a i n + b i when n ≡ i ( mod P), {\displaystyle {g(n)=a_{i}n+b_{i}}{\text{ when }}{n\equiv i{\pmod {P}}},}[image: {\displaystyle {g(n)=a_{i}n+b_{i}}{\text{ when }}{n\equiv i{\pmod {P}}},}] where 0</sub>, ''b''<sub>0</sub>, ..., ''a''<sub>''P'' − 1</sub>, ''b''<sub>''P'' − 1</sub>"}},"i":0}}]}">*a*0, *b*0, ..., *a**P*− 1, *b**P*− 1 are rational numbers which are so chosen that *g*(*n*) is always an integer. The standard Collatz function is given by *P*= 2, 0</sub> {{=}} {{sfrac|1|2}}"}},"i":0}}]}'>*a*0 = ⁠ 1 / 2 ⁠, 0</sub> {{=}} 0"}},"i":0}}]}'>*b*0 = 0, 1</sub> {{=}} 3"}},"i":0}}]}'>*a*1 = 3, 1</sub> {{=}} 1"}},"i":0}}]}'>*b*1 = 1. Conway proved that the problem

Given g and n, does the sequence of iterates k</sup>''(''n'')"}},"i":0}}]}'>*g k*(*n*) reach 1?

is undecidable, by representing the [halting problem][99] in this way.

Closer to the Collatz problem is the following *universally quantified*problem:

Given g, does the sequence of iterates k</sup>''(''n'')"}},"i":0}}]}'>*g k*(*n*) reach 1, for all 0"}},"i":0}}]}'>*n*> 0?

Modifying the condition in this way can make a problem either harder or easier to solve (intuitively, it is harder to justify a positive answer but might be easier to justify a negative one). Kurtz and Simon [34] proved that the universally quantified problem is, in fact, undecidable and even higher in the [arithmetical hierarchy][100]; specifically, it is Π 0
2 -complete. This hardness result holds even if one restricts the class of functions g by fixing the modulus P to 6480. [35]

Iterations of g in a simplified version of this form, with all b i {\displaystyle b_{i}}[image: {\displaystyle b_{i}}] equal to zero, are formalized in an [esoteric programming language][101] called [FRACTRAN][102].

## In computational complexity

The Collatz and related conjectures are often used when studying computational complexity. [36] [37] The connection is made through the [busy beaver][103] function, where BB(n) is the maximum number of steps taken by any *n*-state [Turing machine][104] that halts. There is a 15-state Turing machine that halts if and only if the following conjecture by [Paul Erdős][12] (closely related to the Collatz conjecture) is false: for all n > 8 there is at least one digit 2 in the base 3 representation of 2*n*. [38] [39] Hence if BB(15) was known, and this machine did not stop in that number of steps, it would be known to run forever and hence no counterexamples exist (which proves the conjecture true). This is a completely impractical way to settle the conjecture; instead it is used to suggest that BB(15) will be very hard to compute, at least as difficult as settling this Collatz-like conjecture.

In 2024, a six-state machine was found for which determining whether it halts involves solving a Collatz-like problem called the antihydra problem. As proofs of even simple conjectures of this nature are not currently known, this suggests that BB(6) will be very hard to compute. [40] [41]

## In proofs of correctness

Errors in proofs are a serious concern in mathematics. To address this, and to help avoid subtle errors sneaking through, software such as [Lean (proof assistant)][105] formally verifies that every step in a proof is correct. This formal verification of each step means a Lean-verified proof is considered the 'gold standard', the strongest known evidence that a theorem is true. Such proofs are considered even more trustworthy than proofs that have passed peer review by expert humans, the previous best check.

In July 2026, a disproof of the Collatz conjecture was verified not only by Lean, but another formal verification system *Nanoda*. However, investigation quickly revealed that the proof exploited bug(s) in these verifiers. Once the bugs were fixed, the proof was shown invalid (by both verifiers), and the Collatz problem remains a conjecture. [42] [43]

## See also

- [image: icon] [106] [Mathematics portal][107]

[image: Wikimedia Commons logo] [108]

Wikimedia Commons has media related to [Collatz conjecture][109].

- **[3 x + 1 semigroup][110]
- [Arithmetic dynamics][111]
- [Juggler sequence][112]
- [Modular arithmetic][19]
- [Residue-class-wise affine group][113]

## Notes

1. ↑ It is also known as the **3*n*+ 1 problem**(or **conjecture**), the **3*x*+ 1 problem**(or **conjecture**), the **Ulam conjecture**(after [Stanisław Ulam][114]), **Kakutani's problem**(after [Shizuo Kakutani][115]), the **Thwaites conjecture**(after [Bryan Thwaites][116]), **Hasse's algorithm**(after [Helmut Hasse][117]), or the **Syracuse problem**(after [Syracuse University][118]). [1] [3]
2. ↑ Here "almost every" means that the [natural density][119] of the set of integers with finite stopping times is 1.

## References

{{cite journal |first=Jeffrey C. |last=Lagarias |title=The 3''x'' + 1 problem and its generalizations |journal=[[The American Mathematical Monthly]] |volume=92 |issue=1 |pages=3–23 |year=1985 |jstor=2322189|doi=10.1080/00029890.1985.11971528 }}</ref>\n<!--<ref name=\"Lagarias (2001)\">{{SpringerEOM | urlname=S/s110330 | title=Syracuse problem | author=Jeffrey C. Lagarias}}.</ref>-->\n<ref name=\"Chamberland (1996)\">{{cite journal |first=Marc |last=Chamberland |title=A continuous extension of the 3''x''&nbsp;+&nbsp;1 problem to the real line |journal=Dynam. Contin. Discrete Impuls Systems |volume=2 |issue=4 |pages=495–509 |year=1996 }}</ref>\n<ref name=\"Garner (1981)\">{{cite journal |last=Garner |first=Lynn E. |year=1981 |title=On the Collatz 3''n''&nbsp;+&nbsp;1 algorithm |journal=[[Proceedings of the American Mathematical Society]] |volume=82 |issue=1 |pages=19–22 |doi=10.1090/S0002-9939-1981-0603593-2 |doi-access=free |jstor=2044308}}</ref>\n<ref name=\"Hercher (2023)\">{{cite journal |first1=C. |last1=Hercher |title=There are no Collatz ''m''-cycles with ''m'' ≤ 91 |journal=Journal of Integer Sequences |volume=26 |issue=3 |pages=Article 23.3.5 |year=2023 |url=https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf |archive-date=2023-12-08 |access-date=2023-03-27 |archive-url=https://web.archive.org/web/20231208101612/https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf |url-status=live }} With corrigendum {{cite journal|last=Hercher| first=Christian | title = Corrigendum to Article 23.3.5: There are no Collatz-''m''-Cycles with ''m'' ≤ 91| journal = Journal of Integer Sequences |url = https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf | date = June 14, 2026}}</ref>\n<ref name=\"Letherman, Schleicher, and Wood (1999)\">{{cite journal |first1=Simon |last1=Letherman |first2=Dierk |last2=Schleicher |first3=Reg |last3=Wood |title=The (3''n''&nbsp;+&nbsp;1)-problem and holomorphic dynamics |journal=Experimental Mathematics |volume=8 |issue=3 |pages=241–252 |year=1999 |doi= 10.1080/10586458.1999.10504402}}</ref>\n<ref name=\"Eliahou (1993)\">{{Cite journal|last=Eliahou|first=Shalom|year=1993|title=The 3''x'' + 1 problem: new lower bounds on nontrivial cycle lengths|journal=Discrete Mathematics|volume=118|issue=1|pages=45–56|doi=10.1016/0012-365X(93)90052-U|doi-access=free}}</ref>\n<!--<ref name=\"Andrei (1998)\">{{cite journal |author1=Andrei, Stefan |author2=Masalagiu, Cristian |doi=10.1007/s002360050117 |title=About the Collatz conjecture |year=1998 |journal=Acta Informatica |volume=35 |issue=2 |pages=167–179}}</ref>-->\n<!--<ref name=\"Van Bendegem (2005)\">{{cite journal |first=Jean Paul |last=Van Bendegem |title=The Collatz Conjecture: A Case Study in Mathematical Problem Solving |journal=Logic and Logical Philosophy |volume=14 |pages=7–23 |year=2005 |doi= 10.12775/llp.2005.002|url=https://compmath.files.wordpress.com/2008/08/jpvb_collatz.pdf |archive-url=https://ghostarchive.org/archive/20221009/https://compmath.files.wordpress.com/2008/08/jpvb_collatz.pdf |archive-date=2022-10-09 |url-status=live |format=PDF}}</ref>-->\n<!--<ref name=\"Belaga (2006)\">{{cite book |first=Edward G. |last=Belaga |last2=Mignotte |first2=Maurice |chapter=Walking Cautiously into the Collatz Wilderness: Algorithmically, Number Theoretically, Randomly |chapter-url=http://www-irma.u-strasbg.fr/~belaga/a8*BelagaMathInfo06Presentation060920.ppt |format=PowerPoint |title=Fourth Colloquium on Mathematics and Computer Science : Algorithms, Trees, Combinatorics and Probabilities, September 18–22, 2006, Institut Élie Cartan, Nancy, France }}</ref>-->\n<ref name=\"Belaga (1998a)\">{{cite journal |first1=Edward G. |last1=Belaga |last2=Mignotte |first2=Maurice |title=Embedding the 3x+1 Conjecture in a 3x+d Context |journal=Experimental Mathematics |volume=7 |issue=2 |year=1998 |pages=145–151 |doi=10.1080/10586458.1998.10504364 |s2cid=17925995 |url=http://www.emis.de/journals/EM/expmath/volumes/7/7.html |archive-date=2023-06-09 |access-date=2009-05-20 |archive-url=https://web.archive.org/web/20230609111925/https://www.emis.de/journals/EM/expmath/volumes/7/7.html |url-status=live }}</ref>-->\n<ref name=\"Steiner (1977)\">{{cite book |first=R. P. |last=Steiner |chapter=A theorem on the syracuse problem |title=Proceedings of the 7th Manitoba Conference on Numerical Mathematics |year=1977 |pages=553–9 |mr=535032}}</ref>\n<ref name=\"Simons & de Weger (2005)\">{{cite journal |first1=J. |last1=Simons |first2=B. |last2=de Weger |title=Theoretical and computational bounds for ''m''-cycles of the 3''n''&nbsp;+&nbsp;1 problem |journal=Acta Arithmetica |volume=117 |issue=1 |pages=51–70 |year=2005 |doi=10.4064/aa117-1-3 |url=http://deweger.xs4all.nl/papers/[35]SidW-3n+1-ActaArith[2005].pdf |bibcode=2005AcAri.117...51S |doi-access=free |access-date=2023-03-28 |archive-date=2022-03-18 |archive-url=https://web.archive.org/web/20220318094356/http://deweger.xs4all.nl/papers/&#91;35&#93;SidW-3n+1-ActaArith&#91;2005&#93;.pdf |url-status=bot: unknown }}</ref>\n<ref name=\"Terras (1976)\">{{cite journal | last = Terras | first = Riho | year = 1976 | title = A stopping time problem on the positive integers | journal = Acta Arithmetica | mr = 0568274 | volume = 30 | issue = 3 | pages = 241–252 | url = http://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf | doi = 10.4064/aa-30-3-241-252 | doi-access = free | archive-date = 2023-12-04 | access-date = 2014-01-23 | archive-url = https://web.archive.org/web/20231204130944/http://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf | url-status = live }}</ref>\n<!--<ref name=\"Sinyor (2010)\">Sinyor, J.; [http://downloads.hindawi.com/journals/ijmms/2010/458563.pdf \"The 3x+1 Problem as a String Rewriting System\"], ''International Journal of Mathematics and Mathematical Sciences'', volume 2010 (2010), Article ID 458563, 6 pages.</ref>-->\n\n<!--<ref name=\"Belaga (1998b)\">{{cite paper | author1-link = Edward Belaga | author1-last = Belaga | author1-first = Edward G. | citeseerx = 10.1.1.54.483 | title = Reflecting on the 3x+1 Mystery | publisher = [[University of Strasbourg]] | date = 1998 }}</ref>\n<ref name=\"Bruschi (2008)\">{{cite arXiv |author=Bruschi, Mario |eprint=0810.5169 |title=A generalization of the Collatz problem and conjecture |class=math.NT |year=2008}}</ref>\n<ref name=\"De Mol (2008)\">{{cite journal | last = De Mol | first = Liesbeth | title = Tag systems and Collatz-like functions | journal = Theoretical Computer Science | volume = 390 | issue = 1 | pages =92–101 | date = January 2008 | url = http://logica.ugent.be/liesbeth/TagColOK.pdf | doi=10.1016/j.tcs.2007.10.020}}</ref>\n<ref name=\"Lagarias (2006)\">{{cite arXiv |author=Jeffrey C. Lagarias |eprint=math.NT/0608208 |title=The 3''x''&nbsp;+&nbsp;1 problem: An annotated bibliography, II (2000–) |class=math.NT |year=2006}}</ref>\n<ref name=\"Ohira\">{{cite paper | last1 = Ohira | first1 = Reiko | last2 = Yamashita | first2 = Michinori | url = http://risweb2.ris.ac.jp/faculty/earth_env/yamasita/open/p-col.pdf | title = A generalization of the Collatz problem | language = ja }}</ref>\n<ref name=\"Sinisalo (2003)\">{{cite paper | first = Matti K. | last = Sinisalo | archive-date = 2009-10-24 | archive-url = https://web.archive.org/web/20091024183537/http://geocities.com/mattiksinisalo/collatz.doc | url = http://geocities.com/mattiksinisalo/collatz.doc | title = On the minimal cycle lengths of the Collatz sequences | date = June 2003 | publisher = University of Oulu }}</ref>\n<ref name=\"Stadfeld\">{{cite paper | first = Paul | last = Stadfeld | url = http://home.versatel.nl/galien8/blueprint/blueprint.html | title = Blueprint for Failure: How to Construct a Counterexample to the Collatz Conjecture }}</ref>\n<ref name=\"Urata\">{{cite paper | last = Urata | first = Toshio | url = http://auemath.aichi-edu.ac.jp/~turata/Fall.files/CTZVI.pdf | archive-url = https://web.archive.org/web/20041128171946/http://auemath.aichi-edu.ac.jp/~turata/Fall.files/CTZVI.pdf | url-status = dead | archive-date = 2004-11-28 | title = Some Holomorphic Functions connected with the Collatz Problem }}</ref>-->\n\n<!--<ref name=\"Everest (2003)\">{{cite book | last1=Everest | first1=Graham | last2=van der Poorten | first2=Alf | author2-link=Alfred van der Poorten | last3=Shparlinski | first3=Igor | last4=Ward | first4=Thomas | title=Recurrence sequences | series=Mathematical Surveys and Monographs | volume=104 | location=[[Providence, RI|Providence]], Rhode Island, USA | publisher=[[American Mathematical Society]] | year=2003 | isbn=0-8218-3387-1 | zbl=1033.11006 | at=Chapter 3.4 }}</ref>-->\n<ref name=\"Guy (2004)\">{{cite book |last=Guy | first=Richard K. | author-link=Richard K. Guy | title=Unsolved Problems in Number Theory | publisher=[[Springer-Verlag]] |edition=3rd | year=2004 |isbn=0-387-20860-7 | zbl=1058.11001 | chapter=\"E16: The 3x+1 problem\" |pages=330–6 |chapter-url=https://books.google.com/books?id=1AP2CEGxTkgC&pg=PA330}}</ref>\n<ref name=\"Lagarias (2010)\">{{cite book |editor1-last=Lagarias |editor1-first=Jeffrey C. |editor1-link=Jeffrey Lagarias |year=2010 |title=The Ultimate Challenge: The 3''x'' + 1 Problem |publisher=[[American Mathematical Society]] |isbn=978-0-8218-4940-8 |zbl=1253.11003}}</ref>"}},"i":0}}]}'>

\n{{#parsoid\u0000fragment:76}}\n{{#parsoid\u0000fragment:77}}\n{{#parsoid\u0000fragment:78}}\n\n\n{{#parsoid\u0000fragment:79}}\n{{#parsoid\u0000fragment:80}}"}}'>
1. ↑ Maddux, Cleborne D.; Johnson, D. Lamont (1997). *Logo: A Retrospective*. New York: Haworth Press. p. 160. [ISBN][120] [0-7890-0374-0][121]. The problem is also known by several other names, including: Ulam's conjecture, the Hailstone problem, the Syracuse problem, Kakutani's problem, Hasse's algorithm, and the Collatz problem.
2. 1 2 3 4 5 6 7 Lagarias, Jeffrey C. (1985). "The 3*x*+ 1 problem and its generalizations". *[The American Mathematical Monthly][122]*. **92**(1): 3– 23. [doi][123]: [10.1080/00029890.1985.11971528][124]. [JSTOR][125] [2322189][126].
3. ↑ According to Lagarias (1985), [2] p. 4, the name "Syracuse problem" was proposed by Hasse in the 1950s, during a visit to [Syracuse University][118].
4. ↑ O'Connor, John J.; [Robertson, Edmund F.][127], ["Lothar Collatz"][128], *[MacTutor History of Mathematics Archive][129]*, [University of St Andrews][130]
5. ↑ Pickover, Clifford A. (2001). **[Wonders of Numbers][131]. Oxford: Oxford University Press. pp. [116][132] –118. [ISBN][120] [0-19-513342-0][133].
6. ↑ [Hofstadter, Douglas R.][134] (1979). **[Gödel, Escher, Bach][135]. New York: Basic Books. pp. [400–2][136]. [ISBN][120] [0-465-02685-0][137].
7. ↑ [Guy, Richard K.][138] (2004). [" "E16: The 3x+1 problem" "][139]. *Unsolved Problems in Number Theory*(3rd ed.). [Springer-Verlag][140]. pp. 330– 6. [ISBN][120] [0-387-20860-7][141]. [Zbl][142] [1058.11001][143].
8. 1 2 [Lagarias, Jeffrey C.][13], ed. (2010). *The Ultimate Challenge: The 3*x*+ 1 Problem*. [American Mathematical Society][144]. [ISBN][120] [978-0-8218-4940-8][145]. [Zbl][142] [1253.11003][146].
9. 1 2 Tao, Terence (2022). ["Almost all orbits of the Collatz map attain almost bounded values"][147]. *Forum of Mathematics, Pi*. **10**e12. [arXiv][148]: [1909.03562][149]. [doi][123]: [10.1017/fmp.2022.8][147]. [ISSN][150] [2050-5086][151].
10. ↑ Leavens, Gary T.; Vermeulen, Mike (December 1992). **["3 x + 1 search programs"][152]. *Computers & Mathematics with Applications*. **24**(11): 79– 99. [doi][123]: [10.1016/0898-1221(92)90034-F][153].
11. ↑ Roosendaal, Eric. ["3x+1 delay records"][154]. [Archived][155] from the original on 27 March 2023. Retrieved 14 March 2020. (Note: "Delay records" are total stopping time records.)
12. 1 2 Barina, David (2025). ["Improved verification limit for the convergence of the Collatz conjecture"][156] (PDF). *The Journal of Supercomputing*. **81**(7) 810. [doi][123]: [10.1007/s11227-025-07337-0][157]. [S2CID][158] [220294340][159].
13. 1 2 Garner, Lynn E. (1981). **["On the Collatz 3 n + 1 algorithm"][160]. *[Proceedings of the American Mathematical Society][161]*. **82**(1): 19– 22. [doi][123]: [10.1090/S0002-9939-1981-0603593-2][160]. [JSTOR][125] [2044308][162].
14. 1 2 Eliahou, Shalom (1993). **["The 3 x + 1 problem: new lower bounds on nontrivial cycle lengths"][163]. *Discrete Mathematics*. **118**(1): 45– 56. [doi][123]: [10.1016/0012-365X(93)90052-U][163].
15. 1 2 3 Simons, J.; de Weger, B. (2005). ****["Theoretical and computational bounds for m -cycles of the 3 n + 1 problem"][164] (PDF). *Acta Arithmetica*. **117**(1): 51– 70. [Bibcode][165]: [2005AcAri.117...51S][166]. [doi][123]: [10.4064/aa117-1-3][167]. Archived from the original on 2022-03-18. Retrieved 2023-03-28.`{{ [cite journal][168] }}`: CS1 maint: bot: original URL status unknown ( [link][169])
16. ↑ Lagarias (1985), [2] section " [A heuristic argument"][170].
17. 1 2 Terras, Riho (1976). ["A stopping time problem on the positive integers"][171] (PDF). *Acta Arithmetica*. **30**(3): 241– 252. [doi][123]: [10.4064/aa-30-3-241-252][172]. [MR][173] [0568274][174]. [Archived][175] (PDF) from the original on 2023-12-04. Retrieved 2014-01-23.
18. ↑ Hartnett, Kevin (December 11, 2019). ["Mathematician Proves Huge Result on 'Dangerous' Problem"][176]. *Quanta Magazine*. [Archived][177] from the original on January 16, 2024. Retrieved December 22, 2022.
19. ↑ Krasikov, Ilia; [Lagarias, Jeffrey C.][13] (2003). **["Bounds for the 3 x + 1 problem using difference inequalities"][178]. *Acta Arithmetica*. **109**(3): 237– 258. [arXiv][148]: [math/0205002][179]. [Bibcode][165]: [2003AcAri.109..237K][180]. [doi][123]: [10.4064/aa109-3-4][181]. [MR][173] [1980260][182]. [S2CID][158] [18467460][183]. [*[dead link][184]*]
20. ↑ Steiner, R. P. (1977). "A theorem on the syracuse problem". *Proceedings of the 7th Manitoba Conference on Numerical Mathematics*. pp. 553– 9. [MR][173] [0535032][185].
21. ↑ Simons, John L. (2005). **["On the nonexistence of 2-cycles for the 3 x + 1 problem"][186]. *Math. Comp*. **74**: 1565– 72. [Bibcode][165]: [2005MaCom..74.1565S][187]. [doi][123]: [10.1090/s0025-5718-04-01728-4][186]. [MR][173] [2137019][188].
22. ↑ Hercher, C. (2023). ****["There are no Collatz m -cycles with m ≤ 91"][189] (PDF). *Journal of Integer Sequences*. **26**(3): Article 23.3.5. [Archived][190] (PDF) from the original on 2023-12-08. Retrieved 2023-03-27. With corrigendum Hercher, Christian (June 14, 2026). ****["Corrigendum to Article 23.3.5: There are no Collatz- m -Cycles with m ≤ 91"][191] (PDF). *Journal of Integer Sequences*.
23. ↑ Colussi, Livio (9 September 2011). ["The convergence classes of Collatz function"][192]. *Theoretical Computer Science*. **412**(39): 5409– 5419. [doi][123]: [10.1016/j.tcs.2011.05.056][192]. [hdl][193]: [11577/106892][194].
24. ↑ ''h''</sup>: Comment on Colussi's 'The convergence classes of Collatz function'"},"journal":{"wt":"Theoretical Computer Science"},"doi":{"wt":"10.1016/j.tcs.2015.12.033"},"volume":{"wt":"618"},"pages":{"wt":"135–141"},"doi-access":{"wt":"free"}},"i":0}}]}'/> Hew, Patrick Chisan (7 March 2016). **["Working in binary protects the repetends of 1/3 h: Comment on Colussi's 'The convergence classes of Collatz function' "][195]. *Theoretical Computer Science*. **618**: 135– 141. [doi][123]: [10.1016/j.tcs.2015.12.033][195].
25. ↑ Lagarias, Jeffrey (1990). ["The set of rational cycles for the 3x+1 problem"][196]. *Acta Arithmetica*. **56**(1): 33– 53. [doi][123]: [10.4064/aa-56-1-33-53][197]. [ISSN][150] [0065-1036][198]. [Archived][199] from the original on 2023-03-27. Retrieved 2019-06-10.
26. ↑ Belaga, Edward G.; Mignotte, Maurice (1998). ["Embedding the 3x+1 Conjecture in a 3x+d Context"][200]. *Experimental Mathematics*. **7**(2): 145– 151. [doi][123]: [10.1080/10586458.1998.10504364][201]. [S2CID][158] [17925995][202]. [Archived][203] from the original on 2023-06-09. Retrieved 2009-05-20.
27. ↑ Bernstein, Daniel J.; Lagarias, Jeffrey C. (1996). **["The 3 x + 1 conjugacy map"][204]. *[Canadian Journal of Mathematics][205]*. **48**(6): 1154– 1169. [doi][123]: [10.4153/CJM-1996-060-x][204]. [ISSN][150] [0008-414X][206].
28. ↑ Chamberland, Marc (1996). "A continuous extension of the 3*x*+ 1 problem to the real line". *Dynam. Contin. Discrete Impuls Systems*. **2**(4): 495– 509.
29. ↑ Letherman, Simon; Schleicher, Dierk; Wood, Reg (1999). "The (3*n*+ 1)-problem and holomorphic dynamics". *Experimental Mathematics*. **8**(3): 241– 252. [doi][123]: [10.1080/10586458.1999.10504402][207].
30. ↑ Scollo, Giuseppe (2007). **["Looking for class records in the 3 x + 1 problem by means of the COMETA grid infrastructure"][208] (PDF). *Grid Open Days at the University of Palermo*. [Archived][209] (PDF) from the original on 2023-12-09. Retrieved 2018-05-18.
31. ↑ Lagarias (1985), [2] Theorem D.
32. ↑ Clay, Oliver Keatinge. ["The Long Search for Collatz Counterexamples"][210]. p. 208. [Archived][211] from the original on 9 March 2024. Retrieved 26 July 2024.
33. ↑ Conway, John H. (1972). "Unpredictable iterations". *Proc. 1972 Number Theory Conf., Univ. Colorado, Boulder*. pp. 49– 52.
34. ↑ Kurtz, Stuart A.; Simon, Janos (2007). ["The undecidability of the generalized Collatz problem"][212]. In Cai, J.-Y.; Cooper, S. B.; Zhu, H. (eds.). *Proceedings of the 4th International Conference on Theory and Applications of Models of Computation, TAMC 2007, held in Shanghai, China in May 2007*. pp. 542– 553. [doi][123]: [10.1007/978-3-540-72504-6_49][213]. [ISBN][120] [978-3-540-72503-9][214]. As [PDF][215]
35. ↑ Ben-Amram, Amir M. (2015). "Mortality of iterated piecewise affine functions over the integers: Decidability and complexity". *Computability*. **1**(1): 19– 56. [doi][123]: [10.3233/COM-150032][216].
36. ↑ Michel, Pascal (1993). "Busy beaver competition and Collatz-like problems". *Archive for Mathematical Logic*. **32**(5): 351– 367. [doi][123]: [10.1007/BF01409968][217].
37. ↑ ["Hardness of busy beaver value BB(15)"][218].
38. ↑ Stérin, Tristan; Woods, Damien (2021). "Hardness of busy beaver value BB(15)". [arXiv][148]: [2107.12475][219] [[cs.LO][220]].
39. ↑ [Erdös, Paul][12] (1979). ["Some unconventional problems in number theory"][221]. *[Mathematics Magazine][222]*. **52**(2): 67– 70. [doi][123]: [10.1080/0025570X.1979.11976756][223]. [JSTOR][125] [2689842][224]. [Archived][225] from the original on 2022-06-13. Retrieved 2022-07-07.
40. ↑ Brubaker, Ben (July 2, 2024). ["With Fifth Busy Beaver, Researchers Approach Computation's Limits"][226]. *Quanta*. [Archived][227] from the original on 2025-05-09. Retrieved 2025-08-24.
41. ↑ [Sloane, N. J. A.][228] (ed.). ["Sequence A386792 (Antihydra, a BB(6) Turing machine (values of a))"][229]. *The [On-Line Encyclopedia of Integer Sequences][22]*. OEIS Foundation.
42. ↑ ["Why is it all in the kernel?"][230].
43. ↑ ["The Collatz Conjecture was FALSE (for 2.5 days in July)"][231]. *[YouTube][232]*.

## External links

- Matthews, Keith. [" 3 x + 1 page"][233].
- An ongoing volunteer computing [project][234] by Eric Roosendaal verifies the Collatz conjecture for larger and larger values.
- Another ongoing volunteer computing [project][235] by Tomás Oliveira e Silva continues to verify the Collatz conjecture (with fewer statistics than Eric Roosendaal's page but with further progress made).
- [Weisstein, Eric W.][236] ["Collatz Problem"][237]. *[MathWorld][238]*.
- [Collatz Problem][239] at [PlanetMath][240].
- Nochella, Jesse. ["Collatz Paths"][241]. *[Wolfram Demonstrations Project][242]*.
- [Eisenbud, D.][243] (8 August 2016). **[Uncrackable? The Collatz conjecture][244] (short video). Numberphile. [Archived][245] from the original on 2021-12-11 – via YouTube.
- [Eisenbud, D.][243] (August 9, 2016). **[Uncrackable? Collatz conjecture][246] (extra footage). Numberphile. [Archived][247] from the original on 2021-12-11 – via YouTube.
- [Alex Kontorovich][248] (featuring) (30 July 2021). **[The simplest math problem no one can solve][249] (short video). Veritasium – via YouTube.
- [Are computers ready to solve this notoriously unwieldy math problem?][250]

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Collatz_conjecture&oldid=1369477899][251] "

[Categories][252]:

- [Conjectures][253]
- [Arithmetic dynamics][254]
- [Integer sequences][255]
- [Unsolved problems in number theory][256]

Hidden categories:

- [Articles with short description][257]
- [Short description is different from Wikidata][258]
- [Wikipedia indefinitely semi-protected pages][259]
- [All articles with unsourced statements][260]
- [Articles with unsourced statements from April 2025][261]
- [All articles with dead external links][262]
- [Articles with dead external links from July 2026][263]
- [Wikipedia articles needing clarification from September 2024][264]
- [Commons category link from Wikidata][265]
- [CS1 maint: bot: original URL status unknown][266]

Search

Collatz conjecture

40 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Wikipedia:Protection_policy#semi
[2]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[3]: https://en.wikipedia.org/wiki/File:Collatz-graph-50-no27.svg
[4]: https://en.wikipedia.org/wiki/Directed_graph
[5]: https://en.wikipedia.org/wiki/Orbit_(dynamics)
[6]: https://en.wikipedia.org/wiki/Conjecture
[7]: https://en.wikipedia.org/wiki/Positive_integer
[8]: https://en.wikipedia.org/wiki/Integer_sequence
[9]: https://en.wikipedia.org/wiki/Parity_(mathematics)
[10]: https://en.wikipedia.org/wiki/Lothar_Collatz
[11]: https://en.wikipedia.org/wiki/Hailstones
[12]: https://en.wikipedia.org/wiki/Paul_Erdős
[13]: https://en.wikipedia.org/wiki/Jeffrey_Lagarias
[14]: https://en.wikipedia.org/wiki/File:Collatz-stopping-time.svg
[15]: https://en.wikipedia.org/wiki/File:CollatzStatistic100million.png
[16]: https://en.wikipedia.org/wiki/File:CollatzStatistic1billion.png
[17]: https://en.wikipedia.org/wiki/File:Collatz-10Million.png
[18]: https://en.wikipedia.org/wiki/File:Collatz_Gif.gif
[19]: https://en.wikipedia.org/wiki/Modular_arithmetic
[20]: https://en.wikipedia.org/wiki/Function_(mathematics)
[21]: //oeis.org/A008884
[22]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[23]: https://en.wikipedia.org/wiki/File:Collatz5.svg
[24]: //oeis.org/A006877
[25]: https://en.wikipedia.org/wiki/Maximum
[26]: //oeis.org/A006884
[27]: //oeis.org/A006577
[28]: //oeis.org/A284668
[29]: https://en.wikipedia.org/wiki/Power_of_two
[30]: https://en.wikipedia.org/wiki/File:Collatz_orbits_of_the_all_integers_up_to_1000.svg
[31]: https://en.wikipedia.org/wiki/File:CollatzConjectureGraphMaxValues.jpg
[32]: https://en.wikipedia.org/wiki/File:Collatz-max.png
[33]: https://en.wikipedia.org/wiki/File:All_Collatz_sequences_of_a_length_inferior_to_20.svg
[34]: https://en.wikipedia.org/wiki/File:Collatz_Conjecture_100M.jpg
[35]: https://en.wikipedia.org/wiki/File:Collatz_conjecture_tree_visualization.png
[36]: https://en.wikipedia.org/wiki/Wikipedia:Citation_needed
[37]: https://en.wikipedia.org/wiki/Counterexamples
[38]: https://en.wikipedia.org/wiki/Pólya_conjecture
[39]: https://en.wikipedia.org/wiki/Mertens_conjecture
[40]: https://en.wikipedia.org/wiki/Lower_bound
[41]: https://en.wikipedia.org/wiki/P-adic_numbers
[42]: https://en.wikipedia.org/wiki/Almost_all
[43]: https://en.wikipedia.org/wiki/Riho_Terras_(mathematician)
[44]: https://en.wikipedia.org/wiki/Central_limit_theorem
[45]: https://en.wikipedia.org/wiki/Terence_Tao
[46]: https://en.wikipedia.org/wiki/Logarithmic_density
[47]: https://en.wikipedia.org/wiki/Quanta_Magazine
[48]: https://en.wikipedia.org/wiki/Computer-aided_proof
[49]: https://en.wikipedia.org/wiki/Periodic_sequence
[50]: https://en.wikipedia.org/wiki/Simple_continued_fraction
[51]: https://en.wikipedia.org/wiki/Wikipedia:Please_clarify
[52]: https://en.wikipedia.org/wiki/File:Collatz-tree,_depth=20.svg
[53]: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
[54]: https://en.wikipedia.org/wiki/Relation_(mathematics)
[55]: https://en.wikipedia.org/wiki/If_and_only_if
[56]: https://en.wikipedia.org/wiki/Tree_(graph_theory)
[57]: https://en.wikipedia.org/wiki/Power_of_2
[58]: https://en.wikipedia.org/wiki/Remainder
[59]: https://en.wikipedia.org/wiki/Odd_number
[60]: https://en.wikipedia.org/wiki/Binary_number
[61]: https://en.wikipedia.org/wiki/String_(computer_science)
[62]: https://en.wikipedia.org/wiki/Repeating_decimal
[63]: https://en.wikipedia.org/wiki/Abstract_machine
[64]: https://en.wikipedia.org/wiki/Bit
[65]: https://en.wikipedia.org/wiki/Binary_numeral_system
[66]: https://en.wikipedia.org/wiki/Tag_system#Example:_Computation_of_Collatz_sequences
[67]: https://en.wikipedia.org/wiki/2-adic_integers
[68]: https://en.wikipedia.org/wiki/Measure-preserving_transformation
[69]: https://en.wikipedia.org/wiki/Ergodic_theory
[70]: https://en.wikipedia.org/wiki/Isometry
[71]: https://en.wikipedia.org/wiki/File:Collatz_Cobweb.svg
[72]: https://en.wikipedia.org/wiki/Cobweb_plot
[73]: https://en.wikipedia.org/wiki/Real_line
[74]: https://en.wikipedia.org/wiki/Interpolating
[75]: https://en.wikipedia.org/wiki/Iterations
[76]: https://en.wikipedia.org/wiki/Dynamical_system
[77]: https://en.wikipedia.org/wiki/Fixed_point_(mathematics)
[78]: https://en.wikipedia.org/wiki/Monotonic_function
[79]: https://en.wikipedia.org/wiki/Attractor
[80]: https://en.wikipedia.org/wiki/Lebesgue_measure
[81]: https://en.wikipedia.org/wiki/Complex_plane
[82]: https://en.wikipedia.org/wiki/Trigonometric_functions#In_the_complex_plane
[83]: https://en.wikipedia.org/wiki/Entire_function
[84]: https://en.wikipedia.org/wiki/Critical_point_(mathematics)
[85]: https://en.wikipedia.org/wiki/Classification_of_Fatou_components#Baker_domain
[86]: https://en.wikipedia.org/wiki/Wandering_set
[87]: https://en.wikipedia.org/wiki/File:Collatz_Fractal.jpg
[88]: https://en.wikipedia.org/wiki/Fractal
[89]: https://en.wikipedia.org/wiki/Classification_of_Fatou_components
[90]: https://en.wikipedia.org/wiki/Julia_set
[91]: https://en.wikipedia.org/wiki/File:Exponential_Collatz_Fractal.jpg
[92]: https://en.wikipedia.org/wiki/Exponential_function#Complex_plane
[93]: https://en.wikipedia.org/wiki/Precomputation
[94]: https://en.wikipedia.org/wiki/Space–time_tradeoff
[95]: //oeis.org/A075677
[96]: https://en.wikipedia.org/wiki/Functional_power
[97]: https://en.wikipedia.org/wiki/John_Horton_Conway
[98]: https://en.wikipedia.org/wiki/Undecidable_problem
[99]: https://en.wikipedia.org/wiki/Halting_problem
[100]: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
[101]: https://en.wikipedia.org/wiki/Esoteric_programming_language
[102]: https://en.wikipedia.org/wiki/FRACTRAN
[103]: https://en.wikipedia.org/wiki/Busy_beaver
[104]: https://en.wikipedia.org/wiki/Turing_machine
[105]: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
[106]: https://en.wikipedia.org/wiki/File:Square_root_of_x.svg
[107]: https://en.wikipedia.org/wiki/Portal:Mathematics
[108]: https://en.wikipedia.org/wiki/File:Commons-logo.svg
[109]: https://commons.wikimedia.org/wiki/Category:Collatz%20conjecture
[110]: https://en.wikipedia.org/wiki/3x_+_1_semigroup
[111]: https://en.wikipedia.org/wiki/Arithmetic_dynamics#Other_areas_in_which_number_theory_and_dynamics_interact
[112]: https://en.wikipedia.org/wiki/Juggler_sequence
[113]: https://en.wikipedia.org/wiki/Residue-class-wise_affine_group
[114]: https://en.wikipedia.org/wiki/Stanisław_Ulam
[115]: https://en.wikipedia.org/wiki/Shizuo_Kakutani
[116]: https://en.wikipedia.org/wiki/Bryan_Thwaites
[117]: https://en.wikipedia.org/wiki/Helmut_Hasse
[118]: https://en.wikipedia.org/wiki/Syracuse_University
[119]: https://en.wikipedia.org/wiki/Natural_density
[120]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[121]: https://en.wikipedia.org/wiki/Special:BookSources/0-7890-0374-0
[122]: https://en.wikipedia.org/wiki/The_American_Mathematical_Monthly
[123]: https://en.wikipedia.org/wiki/Doi_(identifier)
[124]: https://doi.org/10.1080%2F00029890.1985.11971528
[125]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[126]: https://www.jstor.org/stable/2322189
[127]: https://en.wikipedia.org/wiki/Edmund_F._Robertson
[128]: https://mathshistory.st-andrews.ac.uk/Biographies/Collatz.html
[129]: https://en.wikipedia.org/wiki/MacTutor_History_of_Mathematics_Archive
[130]: https://en.wikipedia.org/wiki/University_of_St_Andrews
[131]: https://archive.org/details/wondersnumbersad00pick
[132]: https://archive.org/details/wondersnumbersad00pick/page/n136
[133]: https://en.wikipedia.org/wiki/Special:BookSources/0-19-513342-0
[134]: https://en.wikipedia.org/wiki/Douglas_Hofstadter
[135]: https://en.wikipedia.org/wiki/Gödel,_Escher,_Bach
[136]: https://archive.org/details/godelescherbach00doug/page/400
[137]: https://en.wikipedia.org/wiki/Special:BookSources/0-465-02685-0
[138]: https://en.wikipedia.org/wiki/Richard_K._Guy
[139]: https://books.google.com/books?id=1AP2CEGxTkgC&amp;pg=PA330
[140]: https://en.wikipedia.org/wiki/Springer-Verlag
[141]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-20860-7
[142]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[143]: https://zbmath.org/?format=complete&amp;q=an:1058.11001
[144]: https://en.wikipedia.org/wiki/American_Mathematical_Society
[145]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-4940-8
[146]: https://zbmath.org/?format=complete&amp;q=an:1253.11003
[147]: https://doi.org/10.1017%2Ffmp.2022.8
[148]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[149]: https://arxiv.org/pdf/1909.03562
[150]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[151]: https://search.worldcat.org/issn/2050-5086
[152]: https://lib.dr.iastate.edu/cs_techreports/125
[153]: https://doi.org/10.1016%2F0898-1221%2892%2990034-F
[154]: http://www.ericr.nl/wondrous/delrecs.html
[155]: https://web.archive.org/web/20230327064659/http://www.ericr.nl/wondrous/delrecs.html
[156]: https://link.springer.com/content/pdf/10.1007/s11227-025-07337-0.pdf
[157]: https://doi.org/10.1007%2Fs11227-025-07337-0
[158]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[159]: https://api.semanticscholar.org/CorpusID:220294340
[160]: https://doi.org/10.1090%2FS0002-9939-1981-0603593-2
[161]: https://en.wikipedia.org/wiki/Proceedings_of_the_American_Mathematical_Society
[162]: https://www.jstor.org/stable/2044308
[163]: https://doi.org/10.1016%2F0012-365X%2893%2990052-U
[164]: https://web.archive.org/web/20220318094356/http://deweger.xs4all.nl/papers/%5B35%5DSidW-3n+1-ActaArith%5B2005%5D.pdf
[165]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[166]: https://ui.adsabs.harvard.edu/abs/2005AcAri.117...51S
[167]: https://doi.org/10.4064%2Faa117-1-3
[168]: https://en.wikipedia.org/wiki/Template:Cite_journal
[169]: https://en.wikipedia.org/wiki/Category:CS1_maint:_bot:_original_URL_status_unknown
[170]: http://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/node3.html
[171]: http://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf
[172]: https://doi.org/10.4064%2Faa-30-3-241-252
[173]: https://en.wikipedia.org/wiki/MR_(identifier)
[174]: https://mathscinet.ams.org/mathscinet-getitem?mr=0568274
[175]: https://web.archive.org/web/20231204130944/http://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf
[176]: https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/
[177]: https://web.archive.org/web/20240116114346/https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/
[178]: https://www.impan.pl/download/pdf/aa109-3-4
[179]: https://arxiv.org/pdf/math/0205002
[180]: https://ui.adsabs.harvard.edu/abs/2003AcAri.109..237K
[181]: https://doi.org/10.4064%2Faa109-3-4
[182]: https://mathscinet.ams.org/mathscinet-getitem?mr=1980260
[183]: https://api.semanticscholar.org/CorpusID:18467460
[184]: https://en.wikipedia.org/wiki/Wikipedia:Link_rot
[185]: https://mathscinet.ams.org/mathscinet-getitem?mr=0535032
[186]: https://doi.org/10.1090%2Fs0025-5718-04-01728-4
[187]: https://ui.adsabs.harvard.edu/abs/2005MaCom..74.1565S
[188]: https://mathscinet.ams.org/mathscinet-getitem?mr=2137019
[189]: https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf
[190]: https://web.archive.org/web/20231208101612/https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf
[191]: https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf
[192]: https://doi.org/10.1016%2Fj.tcs.2011.05.056
[193]: https://en.wikipedia.org/wiki/Hdl_(identifier)
[194]: https://hdl.handle.net/11577%2F106892
[195]: https://doi.org/10.1016%2Fj.tcs.2015.12.033
[196]: https://eudml.org/doc/206298
[197]: https://doi.org/10.4064%2Faa-56-1-33-53
[198]: https://search.worldcat.org/issn/0065-1036
[199]: https://web.archive.org/web/20230327065345/https://eudml.org/doc/206298
[200]: http://www.emis.de/journals/EM/expmath/volumes/7/7.html
[201]: https://doi.org/10.1080%2F10586458.1998.10504364
[202]: https://api.semanticscholar.org/CorpusID:17925995
[203]: https://web.archive.org/web/20230609111925/https://www.emis.de/journals/EM/expmath/volumes/7/7.html
[204]: https://doi.org/10.4153%2FCJM-1996-060-x
[205]: https://en.wikipedia.org/wiki/Canadian_Journal_of_Mathematics
[206]: https://search.worldcat.org/issn/0008-414X
[207]: https://doi.org/10.1080%2F10586458.1999.10504402
[208]: http://www.dmi.unict.it/~scollo/seminars/gridpa2007/CR3x+1paper.pdf
[209]: https://web.archive.org/web/20231209184321/https://www.dmi.unict.it/~scollo/seminars/gridpa2007/CR3x+1paper.pdf
[210]: https://scholarship.claremont.edu/cgi/viewcontent.cgi?article=2052&amp;context=jhm
[211]: https://web.archive.org/web/20240309084321/https://scholarship.claremont.edu/cgi/viewcontent.cgi?article=2052&amp;context=jhm
[212]: https://books.google.com/books?id=mhrOkx-xyJIC&amp;pg=PA542
[213]: https://doi.org/10.1007%2F978-3-540-72504-6_49
[214]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-72503-9
[215]: http://www.cs.uchicago.edu/~simon/RES/collatz.pdf
[216]: https://doi.org/10.3233%2FCOM-150032
[217]: https://doi.org/10.1007%2FBF01409968
[218]: https://arxiv.org/html/2107.12475v2
[219]: https://arxiv.org/pdf/2107.12475
[220]: https://arxiv.org/archive/cs.LO
[221]: https://jstor.org/stable/2689842
[222]: https://en.wikipedia.org/wiki/Mathematics_Magazine
[223]: https://doi.org/10.1080%2F0025570X.1979.11976756
[224]: https://www.jstor.org/stable/2689842
[225]: https://web.archive.org/web/20220613231912/https://www.jstor.org/stable/2689842
[226]: https://www.quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702/
[227]: https://web.archive.org/web/20250509092257/https://www.quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702/
[228]: https://en.wikipedia.org/wiki/Neil_Sloane
[229]: https://oeis.org/A386792
[230]: https://lawrencecpaulson.github.io/2026/07/30/Collatz.html
[231]: https://www.youtube.com/watch?v=RnfFC_LowtU
[232]: https://en.wikipedia.org/wiki/YouTube
[233]: http://www.numbertheory.org/3x+1/
[234]: http://www.ericr.nl/wondrous/index.html
[235]: http://sweet.ua.pt/tos/3x+1.html
[236]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[237]: https://mathworld.wolfram.com/CollatzProblem.html
[238]: https://en.wikipedia.org/wiki/MathWorld
[239]: https://planetmath.org/CollatzProblem
[240]: https://en.wikipedia.org/wiki/PlanetMath
[241]: http://demonstrations.wolfram.com/CollatzPaths/
[242]: https://en.wikipedia.org/wiki/Wolfram_Demonstrations_Project
[243]: https://en.wikipedia.org/wiki/David_Eisenbud
[244]: https://www.youtube.com/watch?v=5mFpVDpKX70
[245]: https://ghostarchive.org/varchive/youtube/20211211/5mFpVDpKX70
[246]: https://www.youtube.com/watch?v=O2_h3z1YgEU
[247]: https://ghostarchive.org/varchive/youtube/20211211/O2_h3z1YgEU
[248]: https://en.wikipedia.org/wiki/Alex_Kontorovich
[249]: https://www.youtube.com/watch?v=094y1Z2wpJg
[250]: https://www.technologyreview.com/2021/07/02/1027475/computers-ready-solve-this-notorious-math-problem/
[251]: https://en.wikipedia.org/w/index.php?title=Collatz_conjecture&amp;oldid=1369477899
[252]: /wiki/Help:Category
[253]: /wiki/Category:Conjectures
[254]: /wiki/Category:Arithmetic_dynamics
[255]: /wiki/Category:Integer_sequences
[256]: /wiki/Category:Unsolved_problems_in_number_theory
[257]: /wiki/Category:Articles_with_short_description
[258]: /wiki/Category:Short_description_is_different_from_Wikidata
[259]: /wiki/Category:Wikipedia_indefinitely_semi-protected_pages
[260]: /wiki/Category:All_articles_with_unsourced_statements
[261]: /wiki/Category:Articles_with_unsourced_statements_from_April_2025
[262]: /wiki/Category:All_articles_with_dead_external_links
[263]: /wiki/Category:Articles_with_dead_external_links_from_July_2026
[264]: /wiki/Category:Wikipedia_articles_needing_clarification_from_September_2024
[265]: /wiki/Category:Commons_category_link_from_Wikidata
[266]: /wiki/Category:CS1_maint:_bot:_original_URL_status_unknown
