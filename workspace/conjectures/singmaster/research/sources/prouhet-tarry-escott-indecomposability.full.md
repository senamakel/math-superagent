<!-- source: https://link.springer.com/article/10.1007/s11139-022-00555-7 | converted from HTML -->

The Prouhet–Tarry–Escott problem, indecomposability of polynomials and Diophantine equations | The Ramanujan Journal | Springer Nature Link

Skip to main content

# The Prouhet–Tarry–Escott problem, indecomposability of polynomials and Diophantine equations

- [Open access][1]
- Published: 11 April 2022

- Volume 58, pages 1075–1093 ( 2022)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[The Ramanujan Journal][5] [Aims and scope][6] [Submit manuscript][7]

The Prouhet–Tarry–Escott problem, indecomposability of polynomials and Diophantine equations

[Download PDF][2]

## Abstract

In this paper, we show how the subjects mentioned in the title are related. First we study the structure of partitions of \(A \subseteq \{1, \dots , n\}\) in *k*-sets such that the first \(k-1\) symmetric polynomials of the elements of the *k*-sets coincide. Then we apply this result to derive a decomposability result for the polynomial \(f_A(x) := \prod _{x \in A} (x-a)\). Finally we prove two theorems on the structure of the solutions (*x*, *y*) of the Diophantine equation \(f_A(x)=P(y)\) where \(P(y)\in \mathbb {Q}[y]\) and on shifted power values of \(f_A(x)\).

### Similar content being viewed by others

### [Equal values of certain partition functions via Diophantine equations][8]

Article Open access 21 October 2021

### [On products of consecutive arithmetic progressions. II][9]

Article 26 June 2018

### [Properties of High Rank Subvarieties of Affine Spaces][10]

Article 20 August 2020

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algebra][11]
- [Combinatorics][12]
- [Discrete Mathematics][13]
- [Linear Algebra][14]
- [Mathematics][15]
- [Number Theory][16]
- [Partition Theory and Modular Forms][17]

## 1 Introduction

The Prouhet–Tarry–Escott problem, shortly PTE, asks to describe disjoint pairs *A*and *B*of sets of integers such that their first *k*power sum symmetric polynomials are equal (cf. [[18][18]]). For example, if

$$\begin{aligned} A=\{2,3,7\}\ \ \ \text {and}\ \ \ B=\{1,5,6\} \end{aligned}$$

then we can take \(k=2\), since we have

$$\begin{aligned} 2+3+7=1+5+6\ \ \ \text {and}\ \ \ 2^2+3^2+7^2=1^2+5^2+6^2. \end{aligned}$$

(1)

In this paper, we connect the PTE problem, and the question for which polynomials \(f(x), g(x) \in \mathbb {Z}[x]\) the equation \(f(x) = g(y)\) has infinitely many solutions \((x,y) \in \mathbb {Z}^2\) if the zeros of *f*are simple and form (almost) an arithmetical progression. Both problems have attracted a lot of attention. Already at this point we mention that the latter question (through a deep result of Bilu and Tichy [[4][19]]) is closely related to decomposability of polynomials. A polynomial \(f(x)\in {\mathbb {Q}}[x]\) is decomposable if we can write \(f(x)=h_1(h_2(x))\) with \(h_1,h_2\in {\mathbb {Q}}[x]\), in a nontrivial way. (Later we shall give the precise notion.) For example,

$$\begin{aligned} f(x)=(x-1)(x-2)(x-3)(x-5)(x-6)(x-7) \end{aligned}$$

is decomposable, since as one can readily check we have \(f(x)=h_1(h_2(x))\) with

$$\begin{aligned} h_1(x)=(x-2\cdot 3\cdot 7)(x-1\cdot 5\cdot 6),\ h_2(x)=(x-2)(x-3)(x-7)+2\cdot 3\cdot 7.\nonumber \\ \end{aligned}$$

(2)

The similarity of ( [1][20]) and ( [2][21]) is not a coincidence; in this paper, we show the general connections between these properties. In Sects. [1][22] and [2][23], we outline the studied problems, the established link and the results we obtain. The proofs of our theorems are given in Sects. [3][24] – [5][25].

The starting point of our study was a question of Benne de Weger. There is an extensive literature on binomial coefficients which are equal or differ by a small or fixed constant (see, e.g., [[8][26], [13][27], [24][28]] and the references there). In the latter paper, the authors study the related Diophantine equation

$$\begin{aligned} \left( {\begin{array}{c}f_1(x)\\ k\end{array}}\right) +\left( {\begin{array}{c}x\\ 2\end{array}}\right) =\left( {\begin{array}{c}f_2(x)\\ 2\end{array}}\right) , \end{aligned}$$

in polynomials \(f_1,f_2\in {\mathbb {Q}}[x]\) with \(\deg f_1=2\), \(\deg f_2=k\). Benne de Weger remarked that this equation leads to the following problem (private communication).

### Problem 1

Let \(k \ge 1\). Describe the values of *k*for which it is possible to partition the set \(\{1,\dots ,2k+1\}\) into a singleton \(A_0\) and two sets \(A_1\) and \(A_2\) with \(k=|A_1|=|A_2|\), such that the symmetric polynomials \(\sigma _1,\dots ,\sigma _{k-1}\) of the elements of \(A_1\) and of \(A_2\) coincide.

This is the PTE problem for \(n = 2k+1\). De Weger added that he had solutions for \(k=1,2,3\) and had proved that there are none for \(4\le k \le 14\). A solution for \(k=3\) is \(A=\{2,3,7\}\), \(B = \{1,5,6\}\). Indeed we have

$$\begin{aligned} 2+3+7=1+5+6, \end{aligned}$$

and, by ( [2][21]),

$$\begin{aligned} 2\cdot 3+2\cdot 7+3\cdot 7= & {} \frac{(2+3+7)^2-(2^2+3^2+7^2)}{2}\\= & {} \frac{(1+5+6)^2-(1^2+5^2+6^2)}{2}=1\cdot 5+1\cdot 6+5\cdot 6. \end{aligned}$$

Problem [1][29] was solved independently by Aart Blokhuis (private communication) and by the third author of the present paper (see Corollary [3.1][30]).

In this paper, we study the following more general problem.

### Problem 2

Let *r*be a fixed non-negative integer. Describe those positive integers *n*for which the set \(\{1,\dots ,n\}\) can be partitioned into sets \(A_0,A_1,\dots ,A_t\) with \(t\ge 2\), \(|A_0|=r\) and

$$\begin{aligned} k:=|A_1|=\dots =|A_t| \ge 2 \end{aligned}$$

such that all the symmetric polynomials \(\sigma _1,\dots ,\sigma _{k-1}\) of the elements of the \(A_i\) \((i=1,\dots ,t)\) coincide.

The problem asks: is it possible to omit a ‘few’ elements from the set \(\{1,\dots ,n\}\) such that the remaining set can be split into *t*subsets which have pairwise the PTE-property? Observe that Problem [1][29] is the special case \(r=1\), \(t=2\).

In Theorem [2.1][31], we show that if *r*is small enough with respect to *n*, then only \(k=2\) is possible and \(A_1, A_2, \dots , A_t\) are symmetric. We call a set \(A=\{a_1,\dots ,a_k\}\subset {\mathbb {R}}\) with \(a_1<\dots <a_k\) symmetric if the sums \(a_i+a_{k+1-i}\) \((i=1,\dots ,k)\) are all equal. It is obvious that such a symmetry implies a PTE-structure.

Next we establish a new link between PTE problems and the indecomposability of certain polynomials. We recall some standard notions. Let *K*be a field and \(f\in K[x]\). Then *f*is called decomposable (or composite) over *K*if there exists \(h_1,h_2\in K[x]\) such that

$$\begin{aligned} f(x) = h_1(h_2(x)) \ \ \ (h_1,h_2\in K[x],\ \deg h_1>1, \deg h_2>1). \end{aligned}$$

Otherwise *f*is called indecomposable. If \(f(x)=h_1(h_2(x))\) and \(\lambda (x)\in K[x]\) is a linear polynomial, then \(f(x)=h_3(h_4(x))\) with \(h_3(x)=h_1(\lambda ^{-1}(x))\) and \(h_4(x)=\lambda (h_2(x))\) is another decomposition of *f*(*x*). In the sequel we do not distinguish between such equivalent decompositions. Further, we consider the polynomials \(f(x),f(\lambda (x))\), as well as the polynomials \(f(x),\lambda (f(x))\) to be equivalent. There is a vast literature on (in)decomposability of polynomials (see, e.g., [[2][32], [4][19], [5][33], [7][34], [11][35], [12][36], [19][37]] and the references there). In Theorem [2.2][38], we show that the studied variant of the PTE problem is equivalent to asking for the indecomposability of certain polynomials.

Using this connection, we show in Corollary [2.1][39] for given integers \(n>r\ge 0\) with *r*small enough with respect to *n*that if for \(A\subseteq \{1,\dots ,n\}\) with \(|A|=n-r\) the polynomial

$$\begin{aligned} f_{A,c,d}(x) :=\prod _{a\in A} (x-c-ad), ~~c,d \in {\mathbb {Q}},~ d\ne 0 \end{aligned}$$

(3)

is decomposable over \({\mathbb {Q}}\) as \(h_1(h_2(x))\), then \(h_1\) and \(h_2\) can be given explicitly. Note that the polynomial \(f_{A,c,d}(x)\) represents the product with terms of an arithmetic progression of length *n*with *r*terms missing. For example, if

$$\begin{aligned} f_A(x) := f_{A,0,1}(x) = (x-1)(x-2)(x-3)(x-4)(x-6)(x-7)(x-8)(x-9) \end{aligned}$$

is decomposable as \(h_1(h_2(x))\), then, apart from equivalence,

$$\begin{aligned} h_2(x) = x^2 - 10x,~~h_1(x) = (x+9)(x+16)(x+21)(x+24). \end{aligned}$$

Next, using the above results, we establish a finiteness theorem for the number of times that a polynomial \(f_{A,c,d}\) of the form ( [3][40]) assumes a value which is also assumed by a given polynomial *P*with rational coefficients. Related problems are investigated in the papers [[2][32], [3][41], [16][42], [26][43]] for consecutive integers and in [[15][44]] for arithmetic progressions with at most one term missing. Generalizing and extending many of the above mentioned results, in Theorem [2.3][45], we provide a finiteness result for the number of values of \(f_{A,c,d}\) also taken by another polynomial \(P(x)\in {\mathbb {Q}}[x]\). This result, similarly to the above mentioned ones, is ineffective.

Finally, we consider shifted power values (i.e., values of the shape \(ay^\ell +b\)) of \(f_{A,c,d}\). Related problems have been investigated by many authors. We recall some important results. (For a more detailed survey see, e.g., the introduction of [[15][44]].) A celebrated result of Erdős and Selfridge [[10][46]] says that the product of two or more consecutive positive integers is never a perfect power. Papers of Erdős [[9][47]] and Győry [[14][48]] give similar results for binomial coefficients. A recent result of Bennett and Siksek [[1][49]] states that if the number *k*of terms of the arithmetic progression is fixed and large enough, then there are only finitely many instances that the product yields a perfect power. For results with \(r=1\) (just one term missing), see, e.g., [[20][50], [21][51]] (for consecutive integers) and [[22][52]] (for general arithmetic progressions). In the equation \(f_{A,c,d}(x)=ay^\ell +b\) we give an effective upper bound for the exponent \(\ell \) and for the integer values *x*, *y*for which this equation holds, in Theorem [2.4][53]. This result implies for example that for every integer \(n\ge 24\) and rational numbers *a*, *b*with \(a\ne 0\) there exists an effectively computable number *C*such that the equation \(f_A(x) = ay^{\ell }+b\) with \(A \subset \{1,2, \dots , n\}, |A|=n-2\) implies max \((|x|,|y|,\ell ) < C\).

Our results make a step forward toward the solution of the problem how much one can ‘mutilate’ an arithmetic progression such that the corresponding product of terms still can take only finitely many values of a given polynomial, or shifted power values.

## 2 Results

In connection with Problem [2][54], we prove the following result.

### Theorem 2.1

Let *n*, *r*be non-negative integers with

$$\begin{aligned} n>2r^{3/2}+5r+8. \end{aligned}$$

(4)

Then every decomposition of \(\{1,\dots ,n\}\) as in Problem [2][54] has the following structure. Putting \(A:=\{1,\dots ,n\}\setminus A_0\) with \(r=|A_0|\), we have \(k=2\), and all classes \(A_i=\left\{ a_1^{(i)},a_2^{(i)}\right\} \) \((i=1,\dots ,t)\) are symmetric with respect to

$$\begin{aligned} \bar{a}:=\frac{1}{n-r}\sum \limits _{a\in A} a\ \end{aligned}$$

(5)

that is,

$$\begin{aligned} a_1^{(i)}+a_2^{(i)}=2\bar{a}\ \ \ (i=1,\dots ,t). \end{aligned}$$

### Remark 1

Theorem [2.1][31] yields a complete answer to Problem [2][54] for every \(n>2r^{3/2}+5r+8\). On the other hand, for any *r*and *n*with \(n-r\) even, if \(A=\{1,\dots ,n\}\setminus A_0\) is symmetric with respect to \(\bar{a}\) (i.e., \(a\in A\) implies that \(2\bar{a}-a\in A\)), then we have a partition as in Problem [2][54] with \(k=2\).

### Remark 2

The following extension of Theorem [2.1][31] is also valid. Let \(b_1,\dots ,b_n\) be a non-constant arithmetic progression in \({\mathbb {Q}}\). Put \(B=\{b_1,\dots ,b_n\}\) and suppose that \(B_0,B_1,\dots ,B_t\) is a partition of *B*such that \(r:=|B_0|\), \(k:=|B_1|=\dots =|B_t|\), \(n>2r^{3/2}+5r+8\) and for all \(i=1,\dots ,t\) the symmetric polynomials \(\sigma _1,\dots ,\sigma _{k-1}\) of the elements of \(B_i\) \((i=1,\dots ,t)\) are the same. Then \(k=2\) and writing \(B_i=\{b_1^{(i)},b_2^{(i)}\}\) \((i=1,\dots ,t)\) we have

$$\begin{aligned} b_1^{(i)}+b_2^{(i)}=b_1^{(j)}+b_2^{(j)}\ \ \ (1\le i,j\le t). \end{aligned}$$

Indeed, writing \(b_s=c+da_s\) with \(a_s\in A\setminus A_0\) and \(c,d\in {\mathbb {Q}}\), \(d\ne 0\), it can be easily seen by induction on *n*that *c*can be taken to be zero. Then clearly, we may take \(d=1\), and the claim follows.

The next result establishes a link between partitions as in Problem [2][54] and decomposability of certain polynomials.

### Theorem 2.2

Let *n*be a positive integer and *r*a non-negative integer. Then there exists a partition \(A_0,A_1,\dots ,A_t\) of \(\{1,\dots ,n\}\) as in Problem [2][54] if and only if there exists an \(A\subseteq \{1,\dots ,n\}\) with \(|A|=n-r\) such that the polynomial

$$\begin{aligned} f_A(x)=\prod _{a\in A} (x-a) \end{aligned}$$

(6)

is decomposable over \({\mathbb {Q}}\). In particular, if \(A_0,A_1,\dots ,A_t\) is a partition of the required type, then \(f_A(x)=h_1(h_2(x))\) with \(A=\{1,\dots ,n\}\setminus A_0\) and

$$\begin{aligned} h_2(x)=\prod _{a\in A_1} (x-a)-\prod _{a\in A_1} (-a) \end{aligned}$$

and

$$\begin{aligned} h_1(x)=\left( x+\prod _{a\in A_1} (-a)\right) \cdots \left( x+\prod _{a\in A_t} (-a)\right) . \end{aligned}$$

### Remark 3

From the proof of the theorem, it will be clear that in fact \(h_2\) is independent of which \(A_i\) we use in its definition.

As a simple consequence of Theorems [2.1][31] and [2.2][38] we obtain the following statement.

### Corollary 2.1

Let \(A\subseteq \{1,\dots ,n\}\) with \(|A|=n-r\) where *n*and *r*are integers with \(r\ge 0\) and \(n>2r^{3/2}+5r+8\). Further, let \(c,d\in {\mathbb {Q}}\) with \(d\ne 0\). Then the polynomial

$$\begin{aligned} f_{A,c,d}(x)=\prod \limits _{a\in A} (x-c-ad) \end{aligned}$$

(7)

is decomposable over \({\mathbb {Q}}\) if and only if \(n-r\) is even and *A*is symmetric with respect to

$$\begin{aligned} \bar{a}:=\frac{1}{n-r}\sum \limits _{a\in A} a, \end{aligned}$$

when (up to equivalence) the only decomposition of \(f_{A,c,d}(x)\) is given by \(f_{A,c,d}(x)=\varphi ^*((\frac{x-c}{d}-\bar{a})^2)\) with

$$\begin{aligned} \varphi ^*(x)=d^{n-r}h_1\left( x-\overline{a}^2\right) . \end{aligned}$$

(8)

Here, \(h_1\) is the polynomial defined in Theorem [2.2][38] corresponding to the partition \(A_1,\dots ,A_t\) of *A*with \(|A_1| = |A_2| = \dots = |A_t| =2\).

Next we apply our results to the equation \(f_{A,c,d}(x)=P(y)\) where *P*is a given polynomial. The first theorem of this type is general, but ineffective: it only guarantees the finiteness of the number of integral solutions.

### Theorem 2.3

Let \(A\subseteq \{1,\dots ,n\}\) with \(|A|=n-r\) for integers \(r\ge 0\) and \(n>2r^{3/2}+5r+8\) and let \(c,d\in {\mathbb {Q}}\) with \(d\ne 0\). Let \(f_{A,c,d}(x)\) be as in ( [7][55]) and let \(P(y)\in {\mathbb {Q}}[y]\) with \(\deg P\ge 2\). Then the equation

$$\begin{aligned} f_{A,c,d}(x)=P(y) \end{aligned}$$

(9)

has only finitely many integer solutions *x*, *y*, unless we are in one of the following cases:

1. (i)

\(P(y)=f_{A,c,d}(T(y))\), where *T*is an arbitrary non-constant polynomial with rational coefficients,

2. (ii)

\(P(y)=\varphi ^*(Q(y))\), where \(\varphi ^*\) is given by ( [8][56]) and *Q*is a non-constant polynomial with rational coefficients having at most two roots of odd multiplicities.

### Remark 4

In cases (i) and (ii) one can easily give examples where equation ( [9][57]) has infinitely many integer solutions *x*, *y*.

If the right hand side of ( [9][57]) is of the shape \(ay^\ell +b\) where \(\ell \) is also unknown, then we can give an effective result.

### Theorem 2.4

Let \(A\subseteq \{1,\dots ,n\}\) with \(|A|=n-r\) with integers \(r\ge 0\) and \(n>2r^{3/2}+5r+8\) and let \(c,d\in {\mathbb {Q}}\) with \(d\ne 0\). Let \(f_{A,c,d}(x)\) be given by ( [7][55]) and let \(a,b\in {\mathbb {Q}}\) with \(a\ne 0\). Then all solutions of the equation

$$\begin{aligned} f_{A,c,d}(x)=ay^\ell +b \end{aligned}$$

(10)

in integers \(x,y,\ell \) with \(\ell \ge 2\) satisfy \(\max (|x|,|y|,\ell )<C\) for some effectively computable constant *C*depending only on *a*, *b*, *c*, *d*, *n*. Here we use the convention that for \(|y|\le 1\) we have \(\ell \le 3\).

## 3 Proofs of results of Prouhet–Tarry–Escott type

### Proof of Theorem 2.1

Throughout the proof, we shall use the earlier notation: \(r=|A_0|\) stands for the number of ’missing elements’ from \(\{1,\dots ,n\}\), \(A_0,A_1,\dots ,A_t\) form a partition of \(\{1,\dots ,n\}\) with the prescribed properties and

$$\begin{aligned} k=|A_1|=\dots =|A_t|. \end{aligned}$$

In particular, we have \(n-r=tk\). Observe that ( [4][58]) implies that \(n-1>2(r-1)^{3/2}+5(r-1)+8\) for \(r>0\). Therefore, by induction on *r*, we may assume without loss of generality that \(n \in A\).

We shall frequently use the identity

$$\begin{aligned} \sum \limits _{i=j}^I \left( {\begin{array}{c}i\\ j\end{array}}\right) =\left( {\begin{array}{c}I+1\\ j+1\end{array}}\right) , \end{aligned}$$

valid for all \(j\ge 0\). Also, we shall make use of the fact that it follows from the conditions of the theorem by induction on *h*that

$$\begin{aligned} \sum _{a \in A_i} \left( {\begin{array}{c}a + \ell \\ h\end{array}}\right) = \sum _{a \in A_j} \left( {\begin{array}{c}a + \ell \\ h\end{array}}\right) \ \ \ \mathrm{for} \ h=0,1, \dots , k-1 \ \mathrm{and ~ all} \ i,j. \end{aligned}$$

(11)

As we shall see, our choice of \(\ell \) will depend on the parity of *k*.

Suppose first *k*is odd. Then \(k\ge 3\). We choose \(\ell =-r-2\) in ( [11][59]) and let

$$\begin{aligned} f(x)=\left( {\begin{array}{c}x-r-2\\ k-1\end{array}}\right) . \end{aligned}$$

Since \(\deg f=k-1\), by our assumptions we have

$$\begin{aligned} \sum \limits _{a\in A_i} f(a) = \sum \limits _{a\in A_j} f(a)\ \ \ (1\le i,j\le t). \end{aligned}$$

Recall that \(A=A_1\cup \dots \cup A_t\) and \(n\in A\). Observe that

$$\begin{aligned} f(1)=\left( {\begin{array}{c}k+r-1\\ k-1\end{array}}\right) ,\ f(2)=\left( {\begin{array}{c}k+r-2\\ k-1\end{array}}\right) ,\dots , f(r+1)=\left( {\begin{array}{c}k-1\\ k-1\end{array}}\right) . \end{aligned}$$

Thus we have

$$\begin{aligned} \sum \limits _{a\in A} f(a)\le \sum \limits _{i=k-1}^{n-r-2} \left( {\begin{array}{c}i\\ k-1\end{array}}\right) +\sum \limits _{i=k-1}^{k+r-1} \left( {\begin{array}{c}i\\ k-1\end{array}}\right) =\left( {\begin{array}{c}n-r-1\\ k\end{array}}\right) +\left( {\begin{array}{c}k+r\\ k\end{array}}\right) . \end{aligned}$$

Hence for any *j*with \(1\le j\le t\) we get

$$\begin{aligned} \sum \limits _{a\in A_j} f(a)\le \frac{\left( {\begin{array}{c}n-r-1\\ k\end{array}}\right) +\left( {\begin{array}{c}k+r\\ k\end{array}}\right) }{t}=\frac{n-r-1}{n-r}\left( {\begin{array}{c}n-r-2\\ k-1\end{array}}\right) +\frac{k}{n-r}\left( {\begin{array}{c}k+r\\ k\end{array}}\right) . \end{aligned}$$

(12)

On the other hand, assuming without loss of generality that \(n\in A_1\), we also have

$$\begin{aligned} \sum \limits _{a\in A_1} f(a)\ge \left( {\begin{array}{c}n-r-2\\ k-1\end{array}}\right) . \end{aligned}$$

(13)

Combining ( [12][60]) and ( [13][61]), we obtain

$$\begin{aligned} k\left( {\begin{array}{c}k+r\\ k\end{array}}\right) \ge \left( {\begin{array}{c}n-r-2\\ k-1\end{array}}\right) . \end{aligned}$$

Since \(k\ge 3\), we can rewrite this inequality as

$$\begin{aligned}&(r+1)(r+2)(r+3)\prod \limits _{i=1}^{k-3} (r+3+i)\\&\quad \ge (n-r-2)(n-r-3)\prod \limits _{i=1}^{k-3} (n-r-k-1+i). \end{aligned}$$

We show that it is impossible. On the one hand, in view of \(k\le (n-r)/2\) and ( [4][58]), we have

$$\begin{aligned} n-r-k-1+i>r+3+i\ \ \ (i=1,\dots ,k-3). \end{aligned}$$

On the other hand, we get from ( [4][58]) that

$$\begin{aligned} (r+1)(r+2)(r+3)< (n-r-2)(n-r-3). \end{aligned}$$

(14)

This yields a contradiction, which proves our claim for *k*odd.

Suppose *k*is even and \(k \ge 4\). Here we choose \(\ell =-2r-2\) in ( [11][59]) and let

$$\begin{aligned} f(x)=\left( {\begin{array}{c}x-2r-2\\ k-1\end{array}}\right) . \end{aligned}$$

Since \(\deg f=k-1\), by our assumptions we have

$$\begin{aligned} \sum \limits _{a\in A_i} f(a) = \sum \limits _{a\in A_j} f(a)\ \ \ (1\le i,j\le t). \end{aligned}$$

Observe that the negative values of *f*are

$$\begin{aligned} f(1)=-\left( {\begin{array}{c}k+2r-1\\ k-1\end{array}}\right) ,\ f(2)=-\left( {\begin{array}{c}k+2r-2\\ k-1\end{array}}\right) ,\dots , f(2r+1)=-\left( {\begin{array}{c}k-1\\ k-1\end{array}}\right) . \end{aligned}$$

Thus we have

$$\begin{aligned} \sum \limits _{a\in A, f(a) < 0} |f(a)| \le \sum \limits _{i=k-1}^{k+2r-1} \left( {\begin{array}{c}i\\ k-1\end{array}}\right) = \left( {\begin{array}{c}k+2r\\ k\end{array}}\right) . \end{aligned}$$

(15)

Furthermore,

$$\begin{aligned} \sum \limits _{a\in A, f(a) \ge 0} f(a) \le \sum \limits _{i=2r+2}^{n} \left( {\begin{array}{c}i-2r-2\\ k-1\end{array}}\right) = \sum \limits _{j=0}^{n-2r-2} \left( {\begin{array}{c}j\\ k-1\end{array}}\right) = \left( {\begin{array}{c}n-2r-1\\ k\end{array}}\right) . \end{aligned}$$

Hence for any *j*with \(1\le j\le t\) we get

$$\begin{aligned} \sum \limits _{a\in A_j} f(a)\le \frac{\left( {\begin{array}{c}n-2r-1\\ k\end{array}}\right) }{t}=\frac{n-2r-1}{n-r}\left( {\begin{array}{c}n-2r-2\\ k-1\end{array}}\right) . \end{aligned}$$

(16)

On the other hand, assuming without loss of generality that \(n\in A_1\), we also have, by ( [15][62]),

$$\begin{aligned} \sum \limits _{a\in A_1} f(a)\ge \left( {\begin{array}{c}n-2r-2\\ k-1\end{array}}\right) -\left( {\begin{array}{c}k+2r\\ k\end{array}}\right) . \end{aligned}$$

(17)

Combining ( [16][63]) and ( [17][64]), we obtain

$$\begin{aligned} (n-r)\left( {\begin{array}{c}k+2r\\ k\end{array}}\right) \ge (r+1)\left( {\begin{array}{c}n-2r-2\\ k-1\end{array}}\right) . \end{aligned}$$

Since \(k\ge 4\), we can rewrite this inequality as

$$\begin{aligned}&(n-r)(2r+1)(2r+2)(2r+3)(2r+4)\prod \limits _{i=1}^{k-4} (2r+4+i)\\&\quad \ge k(r+1)(n-2r-2)(n-2r-3)(n-2r-4)\prod \limits _{i=1}^{k-4} (n-2r-k-1+i). \end{aligned}$$

We show that it is impossible. In view of \(k\le (n-r)/2\) and ( [4][58]), we have

$$\begin{aligned} n-2r-k-1+i>2r+4+i\ \ \ (i=1,\dots ,k-4). \end{aligned}$$

On using \(k\ge 4\) and writing \(m=n-2r\), it follows that

$$\begin{aligned} (m+r)(2r+1)(2r+3)(r+2)>(m-2)(m-3)(m-4). \end{aligned}$$

(18)

Since ( [4][58]) implies \(m > 2r^{3/2} + 3r +8\), this yields a contradiction.

Finally, let \(k=2\). Then we have \(t=(n-r)/2\); in particular, \(n-r\) is even. That is, we have pairs of elements of *A*having the same sum. Obviously, this is possible only if we take the largest number with the smallest one, and so on, so the pairs are symmetric with respect to \(\bar{a}\). \(\square \)

### Corollary 3.1

The only solution of Problem [1][29] with \(k>2\) is for \(n=7\).

### Proof

We apply the proof of Theorem [2.1][31] with \(r=1\) and \(t=2\). It follows that \(k=2\) if \(n>15\). On the other hand, *n*has to be odd and if \(k>2\), then \(n \ge 7\). Hence it remains to check the odd values of *n*between 7 and 15.

If \(n=15, 13, 11\) or 9, then \(k=(n-1)/2\) and we apply ( [11][59]) with \(h=k-1, \ell =-3\). If \(n \not = 9\), then the largest coefficient \(\left( {\begin{array}{c}2k-2\\ k-1\end{array}}\right) \) is larger than the sum of the absolute values of the other 2*k*binomial coefficients. Hence the sums in ( [11][59]) cannot be equal. If \(n=9\), the largest binomial coefficient, \(\left( {\begin{array}{c}6\\ 3\end{array}}\right) =20\), is equal to the sum of the absolute values of the other terms. It follows that \(9, 1, 2 \in A_1\) and \(8,7,6 \in A_2\). However, when applying ( [11][59]) with \(h=1, \ell =-3\) we see that the sum of the elements in \(A_2\) exceeds that of \(A_1\) for all possible choices of the remaining elements 3, 4 and 5.

If \(n=7\), choose \(A_0=\{4\}, A_1=\{2,3,7\}, A_2=\{1,5,6\}\). This is the only valid choice. \(\square \)

### Remark 5

Remark 2 implies that the symmetric polynomials \(\sigma _1, \sigma _2\) of 1, 2, 6 and of 0, 4, 5, and also of 3, 5, 13 and of 1, 9, 11, coincide too.

## 4 Proofs of results on indecomposability

### Proof of Theorem 2.2

Let \(A_0,A_1, \dots , A_t\) be a partition as stated in Problem [2][54]. Put \(A=\{1,\dots ,n\}\setminus A_0\) and let \(f_A,h_1,h_2\) be as in the theorem. We want to show that \(f_A(x)=h_1(h_2(x))\). If two polynomials of degree \(n-r\) have the same values at \(n-r+1\) points, then they coincide. It is clear that \(f_A(0) = h_1(h_2(0)) = \prod _{a\in A}(-a)\) and that both \(f_A(x)\) and \(h_1(h_2(x))\) have all \(a\in A_1\) as roots. In view of

$$\begin{aligned} \prod _{a\in A_1}(x-a)-\prod _{a\in A_1}(-a) = \prod _{a\in A_i}(x-a) - \prod _{a\in A_i}(-a) \end{aligned}$$

for \(2\le i \le t\), we see that every \(a\in A\) is both a root of \(f_A(x)\) and of \(h_1(h_2(x))\). Thus \(f_A(x)\) and \(h_1(h_2(x))\) assume the same value at \(n-r+1\) points, hence \(f_A=h_1(h_2)\). This proves the “only if” statement and the second statement of the theorem.

To prove the “if” statement, let \(A\subseteq \{1,\dots ,n\}\) with \(|A|=n-r\), and suppose that \(h_1(h_2)\) is a decomposition of \(f_A\) with \(h_1,h_2\in {\mathbb {Q}}[x]\). Clearly, we may assume that both \(h_1\) and \(h_2\) are monic polynomials. Set \(h_1(x)=(x-\alpha _1)\dots (x-\alpha _t)\) with \(\alpha _1,\dots ,\alpha _t\in {\mathbb {C}}\). Observe that these roots are pairwise distinct. Then

$$\begin{aligned} \prod _{a \in A} (x-a) = h_1(h_2(x)) = (h_2(x)-\alpha _1) \cdots (h_2(x) - \alpha _t). \end{aligned}$$

Let \(A_i\) consist of the roots of the polynomial \(h_2(x)-\alpha _i\) \((i=1,\dots ,t)\). Then all the symmetric polynomials of the elements of \(A_i\) for \(i=1, \dots , t\) coincide. So putting \(A_0=\{1,\dots ,n\}\setminus A\), the sets \(A_0 ,A_1, \dots , A_t\) form a partition as in Problem [2][54]. \(\square \)

### Proof of Corollary 2.1

Clearly, by

$$\begin{aligned} f_{A,c,d}(x)=d^{n-r}\prod _{a\in A}\left( \frac{x-c}{d} -a\right) = d^{n-r} f_A\left( \frac{x-c}{d}\right) , \end{aligned}$$

\(f_{A,c,d}\) and \(f_A\) are equivalent and therefore have equivalent decompositions. It follows from Theorems [2.2][38] and [2.1][31] that \(f_{A,c,d}\) is decomposable if and only if \(n-r\) is even, each partition set \(A_i\) has two elements, \(a_1^{(i)}\) and \(a_2^{(i)}\) for \(i=1, \dots , t\), say, the set *A*is symmetric with respect to \(\bar{a}\) and ( [5][65]) holds.

To get the specific decomposition observe that

$$\begin{aligned} (x-a_1^{(i)})(x-a_2^{(i)}) - a_1^{(i)}a_2^{(i)} = (x-\overline{a})^2-\overline{a}^2 \end{aligned}$$

for \(i=1,\dots ,n\). Thus, using the decomposition \(f_A=h_1(h_2)\) with \(h_1,h_2\) as in Theorem [2.2][38], we have

$$\begin{aligned} f_{A,c,d}(x) = d^{n-r}h_1\left( h_2\left( \frac{x-c}{d}\right) \right) = d^{n-r}h_1\left( \left( \frac{x-c}{d}-\overline{a}\right) ^2-\overline{a}^2\right) , \end{aligned}$$

so choosing \(\varphi ^*(x) = d^{n-r} h_1(x-\overline{a}^2)\) we obtain the decomposition as given in the theorem.

To prove the uniqueness let \(f_A(x) = P(Bx^2+Cx+D)\) any decomposition of \(f_A(x)\) with \(P(x)\in {\mathbb {Q}}[x]\) and \(B,C,D\in {\mathbb {Q}}, B\ne 0\). Without loss of generality we may assume \(B=1\). Then \(f_A(x) = P\left( (x+C/2)^2+D-C^2/4\right) \). Hence the roots of \(f_A\) form a symmetric set with respect to \(-C/2\), but they also form a symmetric set with respect to \(\overline{a}\). Thus \(C=-2\overline{a}\). This proves the uniqueness. \(\square \)

## 5 Proofs of results on Diophantine equations

We start with the proof of Theorem [2.4][53]. For this, we introduce some notation and state three lemmas.

Let \(f(x)\in {\mathbb {Z}}[x]\) of degree *d*and height (i.e, the maximum of the absolute values of the coefficients) *H*, and let *a*be a non-zero integer. Consider the equation

$$\begin{aligned} f(x)=ay^\ell \end{aligned}$$

(19)

in \(x,y,\ell \in {\mathbb {Z}}\) with \(\ell \ge 2\). The next lemma is due to Schinzel and Tijdeman [[23][66]]. Actually already Tijdeman [[25][67]] suffices.

### Lemma 5.1

Suppose that *f*(*x*) has at least two different roots. Then for all solutions \(x,y,\ell \) of ( [19][68]) with \(|y|>1\) we have

$$\begin{aligned} \ell <C_1, \end{aligned}$$

where \(C_1=C_1(a,d,H)\) is an effectively computable constant depending only on *a*, *d*and *H*.

The second lemma is a result of Brindza [[6][69]]. Let *S*be a finite set of primes, and write \({\mathbb {Z}}_S\) for the set of those rational numbers whose denominators have no prime divisors outside *S*. For a rational number *q*(given in its minimal form), by its height *h*(*q*) we mean the maximum of the absolute values of its denominator and numerator.

### Lemma 5.2

Let \(f(x)\in {\mathbb {Z}}[x]\) with

$$\begin{aligned} f(x)=a_0\prod _{i=1}^s (x-\gamma _i)^{r_i}, \end{aligned}$$

where \(\gamma _1,\dots ,\gamma _s\) are the (distinct, complex) zeros of *f*(*x*), with multiplicities \(r_1,\dots ,r_s\), respectively. Further, suppose that \(\ell \) (with \(\ell \ge 2\)) is fixed, and write

Suppose that is not a permutation of any of the *s*-tuples

Then for any finite set *S*of primes, for the solutions \(x,y\in {\mathbb {Z}}_S\) of ( [19][68]) we have

$$\begin{aligned} \max (h(x),h(y))<C_2. \end{aligned}$$

Here \(C_2=C_2(a,\ell ,d,H,S)\) is an effectively computable constant depending only on \(a,\ell ,d,H,S\).

Finally, we formulate a statement taking care of the cases \(r\le 1\).

### Lemma 5.3

Let *k*, *j*be integers with \(k\ge 8\) and \(1\le j\le k\), and put

$$\begin{aligned} f_{k,j}(x)=\underset{i\ne j}{\prod \limits _{i=1}^k} (x-i). \end{aligned}$$

Further, let \(a,b\in {\mathbb {Q}}\) with \(a\ne 0\). Then for all solutions of the equation

$$\begin{aligned} f_{k,j}(x)=ay^\ell +b \end{aligned}$$

in integers \(x,y,\ell \) with \(\ell \ge 2\) we have \(\max (|x|,|y|,\ell )<C_3\), where \(C_3\) is an effectively computable constant depending only on *k*, *a*, *b*. Here we use the convention that for \(|y|\le 1\) we have \(\ell \le 3\).

### Proof

In case of \(j=1\) or \(j=k\), the statement follows from the main result of [[26][43]], while in the other cases it is a consequence of Theorem 2.2 of [[15][44]]. \(\square \)

Now we are ready to give the proof of our effective result.

### Proof of Theorem 2.4

Consider ( [10][70]) with fixed *A*, *c*, *d*, *a*, *b*in integers \(x,y,\ell \) with \(\ell \ge 2\). Our proof relies on Lemmas [5.1][71] and [5.2][72], hence ultimately on the multiplicities of the roots of \(f_{A,c,d}(x)\) and its shifts \(f_{A,c,d}(x)-b\). Thus as by a simple rational substitution and multiplication by appropriate rationals we can transform \(f_{A,c,d}(x)\) into \(f_A(x)\), we may consider \(f_A(x)\) in place of \(f_{A,c,d}(x)\). In view of Lemma [5.3][73] and \(n\ge 9\), we may assume \(r=n-|A|\ge 2\) as well.

As all the roots of \(f_A(x)\) are simple and real, the same is valid for the polynomial \(f_A'(x)\), and consequently for \((f_A(x)-b)'\). Thus the polynomial \(f_A(x)-b\) can have at most double roots. Since its degree is \(n-r \ge 22\), the statement immediately follows from Lemmas [5.1][71] and [5.2][72], unless \(\ell =2\) and \(f_A(x)\) is of the form

$$\begin{aligned} f_A(x)=p(x)(q(x))^2+b \end{aligned}$$

(20)

with some \(p,q\in {\mathbb {Q}}[x]\) with \(\deg p\le 2\). In particular,

$$\begin{aligned} N:=|A|=\deg f_A(x) \end{aligned}$$

has the same parity as \(\deg p\) has. Write \(a_1<\dots <a_N\) for the elements of *A*. Taking derivatives, ( [20][74]) gives

$$\begin{aligned} f_A'(x)=q(x)(p'(x)q(x)+2p(x)q'(x)). \end{aligned}$$

(21)

Let \(\alpha _1,\dots ,\alpha _{N-1}\) be the roots of \(f_A'(x)\). Then by Rolle’s theorem these are distinct real numbers with

$$\begin{aligned} a_i<\alpha _i<a_{i+1}\ \ \ (i=1,\dots ,N-1). \end{aligned}$$

We only consider the case \(\deg p=2\). In fact, it is the most complicated possibility, the other cases are simpler and can be handled similarly. Then clearly, \(\deg q=N/2-1\), and ( [21][75]) shows that the roots of *q*(*x*) are among the \(\alpha _i\) -s. Further, ( [20][74]) implies that for these \(\alpha _i\) -s we have \(f_A(\alpha _i)=b\). Observe that, by ( [6][76]), \(f_A(\alpha _i)<0\) for *i*odd, while \(f_A(\alpha _i)>0\) for *i*even. Altogether, we have two options:

1. (a)

either the roots of *q*(*x*) are given by \(\alpha _2,\alpha _4,\dots ,\alpha _{N-2}\) (i.e., all the roots with even indices are involved),

2. (b)

or the \(N/2-1\) roots of *q*(*x*) are among \(\alpha _1,\alpha _3,\dots ,\alpha _{N-1}\) (that is, all the roots with odd indices with one exception are involved).

Put

$$\begin{aligned} G(x)=f_A(x-2)-f_A(x) \end{aligned}$$

and set

$$\begin{aligned} A^*=\{a\in A\ :\ a+2\in A\}. \end{aligned}$$

Observe that \(|A^*|\ge N-r-2\) and

$$\begin{aligned} G(x)=H(x)\prod \limits _{a^*\in A^*} (x-a^*) \end{aligned}$$

with \(\deg H\le r+2\). Further, among the (not disjoint) quadruples

$$\begin{aligned} \{2i-2,2i-1,2i,2i+1\}\ \ \ (i=2,\dots ,\lfloor (n-1)/2\rfloor ) \end{aligned}$$

at least \(n/2-2-2r\) are subsets of *A*. So by ( [4][58]), there is a quadruple \(2i-2,2i-1,2i,2i+1\) contained in *A*, such that *H*(*x*), and thus *G*(*x*) has no root in some interval \((2i,2i+1)\). However, then the sign of *G*(*x*) does not change in this interval. If \(G(x)> 0\) for \(x\in (2i,2i+1)\) then \(f_A(x-2)>f_A(x)\) and choosing \(x=\alpha _{2i}\) we have

$$\begin{aligned} f_A(\alpha _{2i-2})\ge f_A(\alpha _{2i}-2)>f_A(\alpha _{2i}). \end{aligned}$$

Here we use that \(\alpha _{2i-2}\) is the maximum of \(f_A\) on \((2i-2,2i-1)\). If \(G(x)<0\) for \(x\in (2i,2i+1)\) then \(f_A(x-2)<f_A(x)\) and choosing \(x=\alpha _{2i-2}+2\) the same reasoning gives

$$\begin{aligned} f_A(\alpha _{2i-2})< f_A(\alpha _{2i-2}+2)\le f_A(\alpha _{2i}). \end{aligned}$$

Hence in both cases

$$\begin{aligned} f_A(\alpha _{2i-2})\ne f_A(\alpha _{2i}), \end{aligned}$$

(22)

which shows that the option (a) above concerning the roots of *q*(*x*) is not possible. On the other hand, among the quadruples

$$\begin{aligned} \{2i-1,2i,2i+1,2i+2\}\ \ \ (i=1,\dots ,\lfloor n/2-1\rfloor ) \end{aligned}$$

at least \(n/2-2r-2\) are subsets of *A*. So by ( [4][58]), there are three quadruples as above contained in *A*, such that *H*(*x*), and thus *G*(*x*) has no root in three distinct intervals \((2i_j+1,2i_j+2)\) \((j=1,2,3)\). Similarly to ( [22][77]) we obtain

$$\begin{aligned} f_A(\alpha _{2i_j-1})\ne f_A(\alpha _{2i_j+1})\ \ \ (j=1,2,3), \end{aligned}$$

which shows that the option (b) above concerning the roots of *q*(*x*) is also impossible. \(\square \)

Now we give the proof of Theorem [2.3][45]. For this we need some more results and notation.

Let \(\delta \) be a non-zero rational number and \(\mu \) be a positive integer. Then

$$\begin{aligned} D_\mu (x,\delta ):=\sum _{i=0}^{\lfloor \mu /2\rfloor }d_{\mu ,i}x^{\mu -2i}\ \ \ \text {where}\ d_{\mu ,i}=\frac{\mu }{\mu -i} \left( {\begin{array}{c}\mu -i\\ i\end{array}}\right) (-\delta )^i \end{aligned}$$

is the \(\mu \) -th Dickson polynomial. For properties of these polynomials see, e.g., [[17][78]].

We shall use a deep result of Bilu and Tichy [[4][19]] concerning equations of the type

$$\begin{aligned} f(x)=g(y) \end{aligned}$$

(23)

in integers *x*, *y*, where *f*, *g*are polynomials with rational coefficients. To describe this result, we introduce some notation. We say that \(F,G\in {\mathbb {Q}}[x]\) form a standard pair over \(\mathbb {Q}\) if either (*F*(*x*), *G*(*x*)) or (*G*(*x*), *F*(*x*)) appears in Table [1][79].

**Table 1 Standard pairs. Here \(\alpha ,\beta \) are non-zero rational numbers, \(\mu ,\nu ,q\) are positive integers, *p*is a non-negative integer, \(v(x)\in {\mathbb {Q}}[x]\) is a non-zero, but possibly constant polynomial**

[Full size table][80]

Now we recall the main result of [[4][19]], which will play a key role in the proof of Theorem [2.3][45].

### Lemma 5.4

Let \(f(x),g(x)\in {\mathbb {Q}}[x]\) be non-constant polynomials. Then the following two statements are equivalent.

1. (I)

Equation ( [23][81]) has infinitely many rational solutions *x*, *y*with a bounded denominator.

2. (II)

We have \(f=\varphi \circ F\circ \lambda \) and \(g=\varphi \circ G\circ \kappa \), where \(\lambda (x),\kappa (x)\in {\mathbb {Q}}[x]\) are linear polynomials, \(\varphi (x)\in {\mathbb {Q}}[x]\), and *F*(*x*), *G*(*x*) form a standard pair over \({\mathbb {Q}}\) such that the equation \(F(x)=G(y)\) has infinitely many rational solutions *x*, *y*with a bounded denominator.

### Proof of Theorem 2.3

By Lemma [5.4][82], if \(f_{A,c,d}(x)=P(y)\) has infinitely many integer solutions then \(f_{A,c,d}=\varphi \circ F \circ \lambda \) and \(P=\varphi \circ G \circ \kappa \), where \(\varphi ,\lambda ,\kappa \) are rational polynomials with \(\deg \lambda =\deg \kappa =1\), and *F*and *G*form a standard pair. By Corollary [2.1][39], \(\deg \varphi \in \{n-r,(n-r)/2,1\}\). Observe that since the decompositions of the polynomials \(f_{A,c,d}\) and \(f_A\) are equivalent, we may assume that \(c=0\) and \(d=1\), that is, it is enough to deal with \(f_A(x)\). Further, since all quadratic polynomials are equivalent, in view of the case \(\ell =2\) in Theorem [2.4][53], we may assume without loss of generality that \(\deg P\ge 3\). Finally, by the main result of [[16][42]] and by Theorem 2.1 of [[15][44]] we may assume that \(r=n-|A|\ge 2\). By ( [4][58]) this implies

$$\begin{aligned} \deg f_A(x)=N=n-r\ge 24. \end{aligned}$$

(24)

If \(\deg \varphi = n-r\) then \(\deg F = 1\), and we easily get that we are in case (i) of Theorem [2.3][45].

Suppose \(\deg \varphi = (n-r)/2\). Then we have \(\deg F = 2\). By Corollary [2.1][39] the decomposition is given up to a linear transformation: \(f_A(x)=\varphi ^*((x-\overline{a})^2)\). If we have infinitely many solutions then by Lemma [5.4][82] we have \(\varphi ^*((x-\overline{a})^2) = P(y) = \varphi ^*(G(y))\) for some \(G(y)\in {\mathbb {Q}}[y]\) such that \((x-\overline{a})^2 = G(y)\) has infinitely many solutions. Lemma [5.2][72] implies that we must be in case (ii).

Finally, consider the case \(\deg \varphi = 1\). Then \(\deg F=n-r\), and we have

$$\begin{aligned} f_A(x)=aF(sx+t)+b, \end{aligned}$$

where *F*is a member of a standard pair. We check the possible cases.

As \(\deg f_A\ge 24\), *F*cannot come from a standard pair of the fifth kind. Since we assumed that \(\deg P\ge 3\), the polynomial *F*cannot belong to a standard pair of the second type, either.

Assume that *F*belongs to a standard pair of the first kind. Since all the zeros of \(f_A(x)\) are real and simple, hence by Rolle’s theorem all the roots of \(f_A'(x)\) are real and simple, \(F(x)=x^q\) is not possible. On the other hand, if \(F(x)=x^p(v(x))^q\), then \(f_A\) is of the form

$$\begin{aligned} f_A(x)=a(s_1x+s_2)^p(v(s_1x+s_2))^q+b \end{aligned}$$

with some \(s_1,s_2\in {\mathbb {Q}}\), \(s_1\ne 0\). Using again that the roots of \(f_A'(x)\) are simple, we get \(q\le 2\). However, then in view of that the other term in the standard pair in question is \(x^q\), we see that \(\deg P\le 2\), which is excluded.

Finally, assume that *F*belongs to a standard pair of the third or fourth kind. Then \(f_A(x)\) should be a linear transform of a Dickson polynomial. More precisely, with some rationals \(s_1,s_2,t_1,t_2\) \((s_1t_1\ne 0)\) and non-negative integer *N*we can write

$$\begin{aligned} t_1f_A(s_1x+s_2)+t_2=D_N(x,\delta ), \end{aligned}$$

where \(D_N(x,\delta )\) is the *N*-th Dickson polynomial, with non-zero parameter \(\delta \in {\mathbb {Q}}\). (Here we apply the inside and outside linear transformations to \(f_A\) rather than to \(D_N\). In fact, writing \(f_A=\varphi \circ D_N\circ \lambda \), \(t_1x+t_2\) and \(s_1x+s_2\) are the inverses of the linear polynomials \(\varphi (x)\) and \(\lambda (x)\), respectively.) Observe that here \(N=\deg f_A(x)=|A|\) must hold. Then, by the well-known identity (see. e.g., formula (2.2) on p. 9 of [[17][78]])

$$\begin{aligned} D_N\left( y+\frac{\delta }{y},\delta \right) =y^N+\left( \frac{\delta }{y}\right) ^N \end{aligned}$$

we obtain

$$\begin{aligned} t_1\prod \limits _{a\in A} \left( s_1\left( y+\frac{\delta }{y}\right) +s_2-a\right) +t_2=y^N+\left( \frac{\delta }{y}\right) ^N. \end{aligned}$$

Hence as \(|A|=N\),

$$\begin{aligned} \prod \limits _{a\in A} \left( y^2+\frac{s_2-a}{s_1}y+\delta \right) =y^{2N}-t_2y^N+\delta ^N \end{aligned}$$

follows. Here we used by comparing the leading coefficients, that \(t_1s_1^N=1\) must hold. Write \(\zeta ,\xi \) for the roots of the polynomial \(y^2-t_2y+\delta ^N\). Clearly, \(\zeta ,\xi \) are algebraic numbers of degree at most two. Further, we have

$$\begin{aligned} \prod \limits _{a\in A} \left( y^2+\frac{s_2-a}{s_1}y+\delta \right) =(y^N-\zeta )(y^N-\xi ). \end{aligned}$$

(25)

If \(\zeta _0\), \(\xi _0\) are roots of \(y^N-\zeta \) and \(y^N-\xi \), respectively, then all the roots of these polynomials are given by

$$\begin{aligned} \zeta _0 \varepsilon ^i\ \ \text {and}\ \ \xi _0 \varepsilon ^i\ \ \ (i=0,1,\dots ,N-1), \end{aligned}$$

respectively, where \(\varepsilon \) is a primitive *N*-th root of unity. By ( [25][83]) we see that all these roots are algebraic numbers of degrees at most two. This immediately gives that the degree of \(\varepsilon \) is at most four, hence \(\varphi (N)\le 4\). We conclude that \(N \le 12\). This contradicts ( [24][84]). \(\square \)

## References

1.

Bennett, M., Siksek, S.: A conjecture of Erdős, supersingular primes and short character sums. Ann. Math. **191**, 355–392 (2020)

[Article][85] [MathSciNet][86] [Google Scholar][87]

2.

Beukers, F., Shorey, T.N., Tijdeman, R.: Irreducibility of polynomials and arithmetic progressions with equal product of terms. In: Győry, K., Iwaniec, H., Urbanowicz, J. (eds.) Number Theory in Progress (Proceedings of the International Conference in Number Theory in Honor of A. Schinzel, Zakopane, 1997). de Gruyter, pp. 11–26 (1999)

3.

Bilu, Yu., Kulkarni, M., Sury, B.: The Diophantine equation \(x(x+1)\dots (x+(m-1))+r=y^n\). Acta Arith. **113**, 303–308 (2004)

[Article][88] [MathSciNet][89] [Google Scholar][90]

4.

Bilu, Yu., Tichy, R.: The Diophantine equation \(f(x)=g(y)\). Acta Arith. **95**, 261–288 (2000)

[Article][91] [MathSciNet][92] [Google Scholar][93]

5.

Blankertz, R.: A polynomial time algorithm for computing all minimal decompositions of a polynomial. ACM Commun. Comput. Algebra **48:1**(187), 13–23 (2014)

[Article][94] [MathSciNet][95] [Google Scholar][96]

6.

Brindza, B.: On \(S\) -integral solutions of the equation \(y^m=f(x)\). Acta Math. Hungar. **44**, 133–139 (1984)

[Article][97] [MathSciNet][98] [Google Scholar][99]

7.

Davenport, H., Lewis, D.J., Schinzel, A.: Equations of the form \(f(x)=g(y)\). Q. J. Oxf. Ser. (2) **12**, 304–312 (1961)

8.

de Weger, B.: Equal binomial coefficients: some elementary considerations. J. Number Theory **63**, 373–386 (1997)

[Article][100] [MathSciNet][101] [Google Scholar][102]

9.

Erdős, P.: On a Diophantine equation. J. Lond. Math. Soc. **26**, 176–178 (1951)

[Article][103] [Google Scholar][104]

10.

Erdős, P., Selfridge, J.L.: The product of consecutive integers is never a power. Ill. J. Math. **19**, 292–301 (1975)

[MathSciNet][105] [MATH][106] [Google Scholar][107]

11.

Fried, M.: On a theorem of Ritt and related Diophantine problems. J. Reine Angew. Math. **264**, 40–55 (1973)

[MathSciNet][108] [MATH][109] [Google Scholar][110]

12.

Fried, M.: Variables Separated Polynomials, the Genus 0 Problem and Moduli Spaces, Number Theory in Progress, vol. 1, pp. 169–228. Walter de Gruyter, Berlin (1999)

[MATH][111] [Google Scholar][112]

13.

Gallegos-Ruiz, H. R., Katsipis, N., Tengely, Sz., Ulas, M.: On the Diophantine equation \({{n}\atopwithdelims (){k}}={{m}\atopwithdelims (){l}} + d\). J. Number Theory **208**, 418–440 (2020)

14.

Győry, K.: On the Diophantine equation \({{n}\atopwithdelims (){k}}=x^l\). Acta Arith. **80**, 289–295 (1997)

[Article][113] [MathSciNet][114] [Google Scholar][115]

15.

Hajdu, L., Papp, Á: Polynomial values of products of terms from an arithmetic progression. Monatsh. Math. **162**(2020)

16.

Kulkarni, M., Sury, B.: On the Diophantine equation \(x(x+1)(x+2)\cdots (x+(m-1)) = g(y)\). Indag. Math. **14**, 35–44 (2003)

[Article][116] [MathSciNet][117] [Google Scholar][118]

17.

Lidl, R., Mullen, G., Turnwald, G.: Dickson Polynomials, Pitman Monographs and Surveys in Pure and Applied Mathematics, vol. 65. Longman Scientific & Technical, Harlow (1993)

[MATH][119] [Google Scholar][120]

18.

Raghavendran, S., Varayanan, V.: The Prouhet Tarry Escott problem: a review. MDPI Math. **7**, 227 (2019)

[Article][121] [Google Scholar][122]

19.

Ritt, J.F.: Prime and composite polynomials. Trans. Am. Math. Soc. **23**, 51–66 (1922)

[Article][123] [MathSciNet][124] [Google Scholar][125]

20.

Saradha, N., Shorey, T.N.: Almost perfect powers in arithmetic progression. Acta Arith. **99**, 363–388 (2001)

[Article][126] [MathSciNet][127] [Google Scholar][128]

21.

Saradha, N., Shorey, T.N.: Almost squares and factorizations in consecutive integers. Compositio Math. **138**, 113–124 (2003)

[Article][129] [MathSciNet][130] [Google Scholar][131]

22.

Saradha, N., Shorey, T.N.: On the equation \(n(n+d)\cdots (n+(i_0-1)d)(n+(i_0+1)d)\cdots (n+(k-1)d)=y^l\) with \(0<i_0<k-1\). Acta Arith. **129**, 1–21 (2007)

[Article][132] [MathSciNet][133] [Google Scholar][134]

23.

Schinzel, A., Tijdeman, R.: On the equation \(y^m = P(x)\). Acta Arith. **31**, 199–204 (1976)

[Article][135] [MathSciNet][136] [Google Scholar][137]

24.

Stoll, T., Tichy, R. F.: The Diophantine equation \(\alpha {{x}\atopwithdelims (){m}}+\beta {{y}\atopwithdelims (){n}}=\gamma \). Publ. Math. Debrecen **64**, 155–165 (2004)

25.

Tijdeman, R.: Applications of the Gel’fond-Baker method to rational number theory. Topics in Number Theory, Proceedings of the Conference at Debrecen 1974, Colloquia Mathematica Societatis János Bolyai **13**, pp. 399–416, North-Holland, Amsterdam (1976)

26.

Yuan, P.-Z.: On a special diophantine equation \(a {{x}\atopwithdelims (){m}}=by^r+c\). Publ. Math. Debrecen **44**, 137–143 (1994)

[Download references][138]

## Acknowledgements

The authors are grateful to the Referee for the useful and helpful remarks.

## Funding

Open access funding provided by University of Debrecen.

## Author information

### Authors and Affiliations

1.

Institute of Mathematics, University of Debrecen, P.O. Box 400, Debrecen, 4002, Hungary

L. Hajdu & Á. Papp

2.

Alfréd Rényi Institute of Mathematics, P.O. Box 127, Budapest, 1367, Hungary

L. Hajdu

3.

Mathematical Institute, Leiden University, Postbus 9512, 2300 RA, Leiden, The Netherlands

R. Tijdeman

Authors

1. L. Hajdu

[View author publications][139]

Search author on: [PubMed][140] [Google Scholar][141]

2. Á. Papp

[View author publications][142]

Search author on: [PubMed][143] [Google Scholar][144]

3. R. Tijdeman

[View author publications][145]

Search author on: [PubMed][146] [Google Scholar][147]

### Corresponding author

Correspondence to [Á. Papp][148].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Research of L.H. supported in part by the NKFIH Grants 115479, 128088, and 130909, and the projects EFOP-3.6.1-16-2016-00022 and EFOP-3.6.2-16-2017-00015 co-financed by the European Union and the European Social Fund. Research of Á. P. was supported by the ÚNKP-20-3 New National Excellence Program of the Ministry for Innovation and Technology from the source of the National Research, Development and Innovation Fund.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][149].

[Reprints and permissions][150]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [151]

### Cite this article

Hajdu, L., Papp, Á. & Tijdeman, R. The Prouhet–Tarry–Escott problem, indecomposability of polynomials and Diophantine equations. *Ramanujan J***58**, 1075–1093 (2022). https://doi.org/10.1007/s11139-022-00555-7

[Download citation][152]

-

Received: 19 February 2021

-

Accepted: 18 January 2022

-

Published: 11 April 2022

-

Version of record: 11 April 2022

-

Issue date: August 2022

-

DOI: https://doi.org/10.1007/s11139-022-00555-7

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Partitions of][153]
- [Symmetric polynomials][154]
- [The Prouhet–Tarry–Escott problem][155]
- [Products of consecutive integers][156]
- [Indecomposability of polynomials][157]
- [Polynomial values][158]

### Mathematics Subject Classification

- [11P05][159]
- [11B75][160]
- [11D41][161]

### Profiles

1. L. Hajdu [View author profile][162]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s11139-022-00555-7.pdf
[3]: /article/10.1007/s11139-022-00555-7/save-research?_csrf=b5T_0dMrg5s2aiLjWcMIuXB8zIFuaSm_
[4]: /saved-research
[5]: /journal/11139
[6]: /journal/11139/aims-and-scope
[7]: https://submission.nature.com/new-submission/11139/3
[8]: https://link.springer.com/10.1007/s40993-021-00293-7?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s10474-018-0850-7?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s00039-020-00542-4?fromPaywallRec=false
[11]: /subjects/algebra
[12]: /subjects/combinatorics
[13]: /subjects/discrete-mathematics
[14]: /subjects/linear-algebra
[15]: /subjects/mathematics
[16]: /subjects/number-theory
[17]: /subjects/partition-theory-and-modular-forms
[18]: /article/10.1007/s11139-022-00555-7#ref-CR18
[19]: /article/10.1007/s11139-022-00555-7#ref-CR4
[20]: /article/10.1007/s11139-022-00555-7#Equ1
[21]: /article/10.1007/s11139-022-00555-7#Equ2
[22]: /article/10.1007/s11139-022-00555-7#Sec1
[23]: /article/10.1007/s11139-022-00555-7#Sec2
[24]: /article/10.1007/s11139-022-00555-7#Sec3
[25]: /article/10.1007/s11139-022-00555-7#Sec5
[26]: /article/10.1007/s11139-022-00555-7#ref-CR8
[27]: /article/10.1007/s11139-022-00555-7#ref-CR13
[28]: /article/10.1007/s11139-022-00555-7#ref-CR24
[29]: /article/10.1007/s11139-022-00555-7#FPar1
[30]: /article/10.1007/s11139-022-00555-7#FPar13
[31]: /article/10.1007/s11139-022-00555-7#FPar3
[32]: /article/10.1007/s11139-022-00555-7#ref-CR2
[33]: /article/10.1007/s11139-022-00555-7#ref-CR5
[34]: /article/10.1007/s11139-022-00555-7#ref-CR7
[35]: /article/10.1007/s11139-022-00555-7#ref-CR11
[36]: /article/10.1007/s11139-022-00555-7#ref-CR12
[37]: /article/10.1007/s11139-022-00555-7#ref-CR19
[38]: /article/10.1007/s11139-022-00555-7#FPar6
[39]: /article/10.1007/s11139-022-00555-7#FPar8
[40]: /article/10.1007/s11139-022-00555-7#Equ3
[41]: /article/10.1007/s11139-022-00555-7#ref-CR3
[42]: /article/10.1007/s11139-022-00555-7#ref-CR16
[43]: /article/10.1007/s11139-022-00555-7#ref-CR26
[44]: /article/10.1007/s11139-022-00555-7#ref-CR15
[45]: /article/10.1007/s11139-022-00555-7#FPar9
[46]: /article/10.1007/s11139-022-00555-7#ref-CR10
[47]: /article/10.1007/s11139-022-00555-7#ref-CR9
[48]: /article/10.1007/s11139-022-00555-7#ref-CR14
[49]: /article/10.1007/s11139-022-00555-7#ref-CR1
[50]: /article/10.1007/s11139-022-00555-7#ref-CR20
[51]: /article/10.1007/s11139-022-00555-7#ref-CR21
[52]: /article/10.1007/s11139-022-00555-7#ref-CR22
[53]: /article/10.1007/s11139-022-00555-7#FPar11
[54]: /article/10.1007/s11139-022-00555-7#FPar2
[55]: /article/10.1007/s11139-022-00555-7#Equ7
[56]: /article/10.1007/s11139-022-00555-7#Equ8
[57]: /article/10.1007/s11139-022-00555-7#Equ9
[58]: /article/10.1007/s11139-022-00555-7#Equ4
[59]: /article/10.1007/s11139-022-00555-7#Equ11
[60]: /article/10.1007/s11139-022-00555-7#Equ12
[61]: /article/10.1007/s11139-022-00555-7#Equ13
[62]: /article/10.1007/s11139-022-00555-7#Equ15
[63]: /article/10.1007/s11139-022-00555-7#Equ16
[64]: /article/10.1007/s11139-022-00555-7#Equ17
[65]: /article/10.1007/s11139-022-00555-7#Equ5
[66]: /article/10.1007/s11139-022-00555-7#ref-CR23
[67]: /article/10.1007/s11139-022-00555-7#ref-CR25
[68]: /article/10.1007/s11139-022-00555-7#Equ19
[69]: /article/10.1007/s11139-022-00555-7#ref-CR6
[70]: /article/10.1007/s11139-022-00555-7#Equ10
[71]: /article/10.1007/s11139-022-00555-7#FPar18
[72]: /article/10.1007/s11139-022-00555-7#FPar19
[73]: /article/10.1007/s11139-022-00555-7#FPar20
[74]: /article/10.1007/s11139-022-00555-7#Equ20
[75]: /article/10.1007/s11139-022-00555-7#Equ21
[76]: /article/10.1007/s11139-022-00555-7#Equ6
[77]: /article/10.1007/s11139-022-00555-7#Equ22
[78]: /article/10.1007/s11139-022-00555-7#ref-CR17
[79]: /article/10.1007/s11139-022-00555-7#Tab1
[80]: /article/10.1007/s11139-022-00555-7/tables/1
[81]: /article/10.1007/s11139-022-00555-7#Equ23
[82]: /article/10.1007/s11139-022-00555-7#FPar23
[83]: /article/10.1007/s11139-022-00555-7#Equ25
[84]: /article/10.1007/s11139-022-00555-7#Equ24
[85]: https://doi.org/10.4007%2Fannals.2020.191.2.2
[86]: http://www.ams.org/mathscinet-getitem?mr=4076628
[87]: http://scholar.google.com/scholar_lookup?amp;title=A%20conjecture%20of%20Erd%C5%91s%2C%20supersingular%20primes%20and%20short%20character%20sums&amp;journal=Ann.%20Math.&amp;doi=10.4007%2Fannals.2020.191.2.2&amp;volume=191&amp;pages=355-392&amp;publication_year=2020&amp;author=Bennett%2CM&amp;author=Siksek%2CS
[88]: https://doi.org/10.4064%2Faa113-4-1
[89]: http://www.ams.org/mathscinet-getitem?mr=2079406
[90]: http://scholar.google.com/scholar_lookup?amp;title=The%20Diophantine%20equation%20%24%24x%28x%2B1%29%5Cdots%20%28x%2B%28m-1%29%29%2Br%3Dy%5En%24%24%20x%20%28%20x%20%2B%201%20%29%20%E2%8B%AF%20%28%20x%20%2B%20%28%20m%20-%201%20%29%20%29%20%2B%20r%20%3D%20y%20n&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa113-4-1&amp;volume=113&amp;pages=303-308&amp;publication_year=2004&amp;author=Bilu%2CYu&amp;author=Kulkarni%2CM&amp;author=Sury%2CB
[91]: https://doi.org/10.4064%2Faa-95-3-261-288
[92]: http://www.ams.org/mathscinet-getitem?mr=1793164
[93]: http://scholar.google.com/scholar_lookup?amp;title=The%20Diophantine%20equation%20%24%24f%28x%29%3Dg%28y%29%24%24%20f%20%28%20x%20%29%20%3D%20g%20%28%20y%20%29&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa-95-3-261-288&amp;volume=95&amp;pages=261-288&amp;publication_year=2000&amp;author=Bilu%2CYu&amp;author=Tichy%2CR
[94]: https://doi.org/10.1145%2F2644288.2644292
[95]: http://www.ams.org/mathscinet-getitem?mr=3234125
[96]: http://scholar.google.com/scholar_lookup?amp;title=A%20polynomial%20time%20algorithm%20for%20computing%20all%20minimal%20decompositions%20of%20a%20polynomial&amp;journal=ACM%20Commun.%20Comput.%20Algebra&amp;doi=10.1145%2F2644288.2644292&amp;volume=48%3A1&amp;issue=187&amp;pages=13-23&amp;publication_year=2014&amp;author=Blankertz%2CR
[97]: https://link.springer.com/doi/10.1007/BF01974110
[98]: http://www.ams.org/mathscinet-getitem?mr=759041
[99]: http://scholar.google.com/scholar_lookup?amp;title=On%20%24%24S%24%24%20S%20-integral%20solutions%20of%20the%20equation%20%24%24y%5Em%3Df%28x%29%24%24%20y%20m%20%3D%20f%20%28%20x%20%29&amp;journal=Acta%20Math.%20Hungar.&amp;doi=10.1007%2FBF01974110&amp;volume=44&amp;pages=133-139&amp;publication_year=1984&amp;author=Brindza%2CB
[100]: https://doi.org/10.1006%2Fjnth.1997.2109
[101]: http://www.ams.org/mathscinet-getitem?mr=1443768
[102]: http://scholar.google.com/scholar_lookup?amp;title=Equal%20binomial%20coefficients%3A%20some%20elementary%20considerations&amp;journal=J.%20Number%20Theory&amp;doi=10.1006%2Fjnth.1997.2109&amp;volume=63&amp;pages=373-386&amp;publication_year=1997&amp;author=Weger%2CB
[103]: https://doi.org/10.1112%2Fjlms%2Fs1-26.3.176
[104]: http://scholar.google.com/scholar_lookup?amp;title=On%20a%20Diophantine%20equation&amp;journal=J.%20Lond.%20Math.%20Soc.&amp;doi=10.1112%2Fjlms%2Fs1-26.3.176&amp;volume=26&amp;pages=176-178&amp;publication_year=1951&amp;author=Erd%C5%91s%2CP
[105]: http://www.ams.org/mathscinet-getitem?mr=376517
[106]: http://www.emis.de/MATH-item?0295.10017
[107]: http://scholar.google.com/scholar_lookup?amp;title=The%20product%20of%20consecutive%20integers%20is%20never%20a%20power&amp;journal=Ill.%20J.%20Math.&amp;volume=19&amp;pages=292-301&amp;publication_year=1975&amp;author=Erd%C5%91s%2CP&amp;author=Selfridge%2CJL
[108]: http://www.ams.org/mathscinet-getitem?mr=337915
[109]: http://www.emis.de/MATH-item?0278.12101
[110]: http://scholar.google.com/scholar_lookup?amp;title=On%20a%20theorem%20of%20Ritt%20and%20related%20Diophantine%20problems&amp;journal=J.%20Reine%20Angew.%20Math.&amp;volume=264&amp;pages=40-55&amp;publication_year=1973&amp;author=Fried%2CM
[111]: http://www.emis.de/MATH-item?1053.14509
[112]: http://scholar.google.com/scholar_lookup?amp;title=Variables%20Separated%20Polynomials%2C%20the%20Genus%200%20Problem%20and%20Moduli%20Spaces%2C%20Number%20Theory%20in%20Progress&amp;pages=169-228&amp;publication_year=1999&amp;author=Fried%2CM
[113]: https://doi.org/10.4064%2Faa-80-3-289-295
[114]: http://www.ams.org/mathscinet-getitem?mr=1451415
[115]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20Diophantine%20equation%20%24%24%7B%7Bn%7D%5Catopwithdelims%20%28%29%7Bk%7D%7D%3Dx%5El%24%24%20n%20k%20%3D%20x%20l&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa-80-3-289-295&amp;volume=80&amp;pages=289-295&amp;publication_year=1997&amp;author=Gy%C5%91ry%2CK
[116]: https://doi.org/10.1016%2FS0019-3577%2803%2990069-3
[117]: http://www.ams.org/mathscinet-getitem?mr=2015597
[118]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20Diophantine%20equation%20%24%24x%28x%2B1%29%28x%2B2%29%5Ccdots%20%28x%2B%28m-1%29%29%20%3D%20g%28y%29%24%24%20x%20%28%20x%20%2B%201%20%29%20%28%20x%20%2B%202%20%29%20%E2%8B%AF%20%28%20x%20%2B%20%28%20m%20-%201%20%29%20%29%20%3D%20g%20%28%20y%20%29&amp;journal=Indag.%20Math.&amp;doi=10.1016%2FS0019-3577%2803%2990069-3&amp;volume=14&amp;pages=35-44&amp;publication_year=2003&amp;author=Kulkarni%2CM&amp;author=Sury%2CB
[119]: http://www.emis.de/MATH-item?0823.11070
[120]: http://scholar.google.com/scholar_lookup?amp;title=Dickson%20Polynomials%2C%20Pitman%20Monographs%20and%20Surveys%20in%20Pure%20and%20Applied%20Mathematics&amp;publication_year=1993&amp;author=Lidl%2CR&amp;author=Mullen%2CG&amp;author=Turnwald%2CG
[121]: https://doi.org/10.3390%2Fmath7030227
[122]: http://scholar.google.com/scholar_lookup?amp;title=The%20Prouhet%20Tarry%20Escott%20problem%3A%20a%20review&amp;journal=MDPI%20Math.&amp;doi=10.3390%2Fmath7030227&amp;volume=7&amp;publication_year=2019&amp;author=Raghavendran%2CS&amp;author=Varayanan%2CV
[123]: https://doi.org/10.1090%2FS0002-9947-1922-1501189-9
[124]: http://www.ams.org/mathscinet-getitem?mr=1501189
[125]: http://scholar.google.com/scholar_lookup?amp;title=Prime%20and%20composite%20polynomials&amp;journal=Trans.%20Am.%20Math.%20Soc.&amp;doi=10.1090%2FS0002-9947-1922-1501189-9&amp;volume=23&amp;pages=51-66&amp;publication_year=1922&amp;author=Ritt%2CJF
[126]: https://doi.org/10.4064%2Faa99-4-5
[127]: http://www.ams.org/mathscinet-getitem?mr=1845691
[128]: http://scholar.google.com/scholar_lookup?amp;title=Almost%20perfect%20powers%20in%20arithmetic%20progression&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa99-4-5&amp;volume=99&amp;pages=363-388&amp;publication_year=2001&amp;author=Saradha%2CN&amp;author=Shorey%2CTN
[129]: https://doi.org/10.1023%2FA%3A1025480729778
[130]: http://www.ams.org/mathscinet-getitem?mr=2002956
[131]: http://scholar.google.com/scholar_lookup?amp;title=Almost%20squares%20and%20factorizations%20in%20consecutive%20integers&amp;journal=Compositio%20Math.&amp;doi=10.1023%2FA%3A1025480729778&amp;volume=138&amp;pages=113-124&amp;publication_year=2003&amp;author=Saradha%2CN&amp;author=Shorey%2CTN
[132]: https://doi.org/10.4064%2Faa129-1-1
[133]: http://www.ams.org/mathscinet-getitem?mr=2326483
[134]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20equation%20%24%24n%28n%2Bd%29%5Ccdots%20%28n%2B%28i_0-1%29d%29%28n%2B%28i_0%2B1%29d%29%5Ccdots%20%28n%2B%28k-1%29d%29%3Dy%5El%24%24%20n%20%28%20n%20%2B%20d%20%29%20%E2%8B%AF%20%28%20n%20%2B%20%28%20i%200%20-%201%20%29%20d%20%29%20%28%20n%20%2B%20%28%20i%200%20%2B%201%20%29%20d%20%29%20%E2%8B%AF%20%28%20n%20%2B%20%28%20k%20-%201%20%29%20d%20%29%20%3D%20y%20l%20with%20%24%240%3Ci_0%3Ck-1%24%24%200%20%3C%20i%200%20%3C%20k%20-%201&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa129-1-1&amp;volume=129&amp;pages=1-21&amp;publication_year=2007&amp;author=Saradha%2CN&amp;author=Shorey%2CTN
[135]: https://doi.org/10.4064%2Faa-31-2-199-204
[136]: http://www.ams.org/mathscinet-getitem?mr=422150
[137]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20equation%20%24%24y%5Em%20%3D%20P%28x%29%24%24%20y%20m%20%3D%20P%20%28%20x%20%29&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa-31-2-199-204&amp;volume=31&amp;pages=199-204&amp;publication_year=1976&amp;author=Schinzel%2CA&amp;author=Tijdeman%2CR
[138]: https://citation-needed.springer.com/v2/references/10.1007/s11139-022-00555-7?format=refman&amp;flavour=references
[139]: /search?sortBy=newestFirst&amp;contributor=L.%20Hajdu
[140]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=L.%20Hajdu
[141]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22L.%20Hajdu%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[142]: /search?sortBy=newestFirst&amp;contributor=%C3%81.%20Papp
[143]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=%C3%81.%20Papp
[144]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22%C3%81.%20Papp%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[145]: /search?sortBy=newestFirst&amp;contributor=R.%20Tijdeman
[146]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=R.%20Tijdeman
[147]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22R.%20Tijdeman%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[148]: mailto:papp.agoston@science.unideb.hu
[149]: http://creativecommons.org/licenses/by/4.0/
[150]: https://s100.copyright.com/AppDispatchServlet?title=The%20Prouhet%E2%80%93Tarry%E2%80%93Escott%20problem%2C%20indecomposability%20of%20polynomials%20and%20Diophantine%20equations&amp;author=L.%20Hajdu%20et%20al&amp;contentID=10.1007%2Fs11139-022-00555-7&amp;copyright=The%20Author%28s%29&amp;publication=1382-4090&amp;publicationDate=2022-04-11&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[151]: https://crossmark.crossref.org/dialog/?doi=10.1007/s11139-022-00555-7
[152]: https://citation-needed.springer.com/v2/references/10.1007/s11139-022-00555-7?format=refman&amp;flavour=citation
[153]: /search?query=Partitions%20of%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20&amp;facet-discipline=#34;Mathematics&#34;
[154]: /search?query=Symmetric%20polynomials&amp;facet-discipline=#34;Mathematics&#34;
[155]: /search?query=The%20Prouhet%E2%80%93Tarry%E2%80%93Escott%20problem&amp;facet-discipline=#34;Mathematics&#34;
[156]: /search?query=Products%20of%20consecutive%20integers&amp;facet-discipline=#34;Mathematics&#34;
[157]: /search?query=Indecomposability%20of%20polynomials&amp;facet-discipline=#34;Mathematics&#34;
[158]: /search?query=Polynomial%20values&amp;facet-discipline=#34;Mathematics&#34;
[159]: /search?query=11P05&amp;facet-discipline=#34;Mathematics&#34;
[160]: /search?query=11B75&amp;facet-discipline=#34;Mathematics&#34;
[161]: /search?query=11D41&amp;facet-discipline=#34;Mathematics&#34;
[162]: /researchers/17001538SN
