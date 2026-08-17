<!-- source: https://doi.org/10.1007/s00025-025-02486-3 | converted from HTML -->

On the Equisingularity Class of the General Higher Order Polars of Plane Branches | Results in Mathematics | Springer Nature Link

Skip to main content

# On the Equisingularity Class of the General Higher Order Polars of Plane Branches

- [Open access][1]
- Published: 02 August 2025

- Volume 80, article number 177 ( 2025)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Results in Mathematics][5] [Aims and scope][6] [Submit manuscript][7]

On the Equisingularity Class of the General Higher Order Polars of Plane Branches

[Download PDF][2]

## Abstract

In this paper we describe the factorization of the higher order polars of a generic branch in its equisingularity class. We generalize the results of Casas-Alvero and Hefez-Hernandes-Hernández to higher order polars.

### Similar content being viewed by others

### [On Polars of Plane Branches][8]

Chapter © 2017

### [On the Factorization of the Polar of a Plane Branch][9]

Chapter © 2018

### [Generalized growth and weighted polynomial approximation of entire function solutions of certain elliptic partial differential equation][10]

Article 03 October 2023

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algebraic Geometry][11]
- [Apicobasal Polarity][12]
- [Basolateral Polarity][13]
- [Polarization][14]
- [Projective Geometry][15]
- [Group Theory and Generalizations][16]
- [Algebraic Geometry of Varieties and Moduli Spaces][17]

## 1 Introduction

Let \(f(x,y)\in {\mathbb {C}}[[x,y]]\) be an irreducible formal power series and \(C=\{f(x,y)=0\}\) be the *branch*determined by \(f(x,y)=0\). The *multiplicity*of *C*is the order of *f*. When this multiplicity is \(n>1\) we say that *C*is *singular*. Otherwise *C*is a *smooth*branch. In this paper we will consider singular branches. After a change of coordinates, if necessary, we may assume that \(x=0\) is not tangent to the curve *C*at the origin. This is equivalent to \({\textrm{ord}}f(0,y)={\textrm{ord}}f=n\). By Newton Theorem there is \(\alpha (x)=\sum _{i\ge n}a_ix^{i/n}\in \mathbb C[[x^{1/n}]]\subset {\mathbb {C}}[[x]]^{*}\) such that \(f(x,\alpha (x))=0\), where \({\mathbb {C}}[[x]]^{*}\) denotes the ring of Puiseux power series. The power series \(\alpha (x)\) is called a *Newton-Puiseux root*of *f*(*x*, *y*). It is well-known that the set of all Newton-Puiseux roots of *f*(*x*, *y*) is \({\textrm{Zer}}f:=\{\alpha _{\epsilon }(x)=\sum _{i\ge n}a_i\epsilon ^i x^{i/n}\;:\;\epsilon \in {\mathbb {U}}_{n}\}\), where \({\mathbb {U}}_{n}\) is the multiplicative group of *n*th complex roots of unity. By Puiseux Theorem

$$\begin{aligned} f(x,y)=u(x,y)\prod _{\epsilon \in \mathbb {U}_n}(y-\alpha _{\epsilon }(x)), \end{aligned}$$

(1)

where *u*(*x*, *y*) is a unit in \({\mathbb {C}}[[x,y]]\).

The *index*of \(\alpha \in {\mathbb {C}}[[x]]^{*}\) is the smallest natural number *m*such that \(\alpha \) belongs to \(\mathbb C[[x^{1/m}]]\). To any \(\alpha (x)=\sum _{i}a_ix^{i/n}\in \mathbb C[[x]]^{*}\) of positive order and index *n*we associate with two finite sequences \((e_{i})_{i}\) and \((b_{i})_{i}\) of natural numbers as follows: \(e_{0}=b_{0}=n\); if \(e_{k}> 1\) then \(b_{k+1}:=\min \{i\;:\; a_i\ne 0;\; \gcd (e_k,i)<e_k\}\) and \(e_{k+1}:=\gcd (e_k, b_{k+1})\). The sequence \((e_{i})_{i}\) is strictly decreasing and for some \(h \in {\mathbb {N}}\) we have \(e_h=1\). The sequence \((b_{0},b_{1},\ldots ,b_{h})\) is called the *characteristic*of \(\alpha \). By [[9][18], Lemma 6.8] we get

$$\begin{aligned} \begin{aligned} {\text {ord}}(\alpha _{\epsilon }(x)-\alpha (x))=\tfrac{b_{j}}{n}\;\; \hbox {if and only if } \epsilon \in {\mathbb {U}}_{e_{j-1}} \backslash {\mathbb {U}}_{e_{j}}. \end{aligned} \end{aligned}$$

(2)

Let \(\lambda _l(x)\) be the sum of all terms of \(\alpha (x)\) of degree strictly less than \(\frac{b_l}{b_0}\). We denote by \(f_l(y)\) the minimal polynomial of \(\lambda _l(x)\) in the ring \(\mathbb C[[x]][y]\). The polynomial \(f_l(y)\) does not depend on the choice of \(\alpha (x)\in {\textrm{Zer}}f\) and its degree is \(\frac{n}{e_{l-1}}\).

Observe that the characteristic of \( \alpha _{\epsilon }\) equals the characteristic of \(\alpha \). The *characteristic*of an irreducible power series \(f(x,y)\in {\mathbb {C}}[[x,y]]\) is the characteristic of any of its Newton-Puiseux roots. The set of *characteristic exponents*of *f*is \({\textrm{Char}}(f)=\left\{ \frac{b_{i}}{n} \;:\; i\in \{1,\ldots ,h\}\right\} \). After ( [2][19]) the characteristic exponents of *f*are the orders of differences of any two of its distinct Newton-Puiseux roots.

Let \(C=\{f(x,y)=0\}\) and \(D=\{g(x,y)=0\}\) be two curves with \(f,g\in {\mathbb {C}}[[x,y]]\). The *intersection multiplicity*of *C*and *D*is \(i_0(C,D)=\dim {\mathbb {C}}[[x,y]]/(f,g)\) where \((\cdot , \cdot )\) denotes the ideal generated by two power series. Usually \(i_0(C,D)\) is also denoted by \(i_0(f,g)\).

If *C*and *D*are branches then the *contact*of *C*and *D*is

$$\begin{aligned} {\textrm{cont}}(C,D)={\textrm{cont}}(f,g)=\max \{{\textrm{ord}}(\alpha -\gamma )\;:\;\alpha \in {\textrm{Zer}}\,f,\;\gamma \in {\textrm{Zer}}\,g\}. \end{aligned}$$

If \(\alpha \) is a Puiseux series and \(v\in {\mathbb {C}}[[x,y]]\) is irreducible then we put

$$\begin{aligned} {\textrm{cont}}(\alpha ,v)= \max \{{\textrm{ord}}(\alpha -\gamma )\;:\;\gamma \in {\textrm{Zer}}\,v\}. \end{aligned}$$

We say that the branches *C*and *D*are *equisingular*if and only if they have the same characteristic. We will denote by \(K(b_{0},b_{1},\ldots ,b_{h})\) the coset of equisingular branches of characteristic \((b_{0},b_{1},\ldots ,b_{h})\). If \(C=\{f(x,y)=0\}\) is a branch in \(K(b_{0},b_{1},\ldots ,b_{h})\), by abuse of language we will put \(f\in K(b_{0},b_{1},\ldots ,b_{h})\). Let \(f(x,y)=\sum _{ij}a_{ij}x^{i}y^{j}\in K(b_{0},b_{1},\ldots ,b_{h})\).

We say that \(f\in K(b_{0},b_{1},\ldots ,b_{h})\) is *generic*in its equisingularity class if within that class the coefficients of *f*satisfy a Zariski-open condition.

Let *A*be a nonempty subset of \({\mathbb {N}}\times {\mathbb {N}}\). The *Newton diagram*\({\mathcal {N}}(A)\) of the set *A*is the convex hull of \(A+({\mathbb {R}}_{\ge 0})^{2}\), where \(+\) means the Minkowski sum. By definition, the *support*of any Newton diagram \(\Delta \) is \({\textrm{supp}}(\Delta ):=\Delta \cap {\mathbb {N}}^2\). We say that \({\mathcal {N}}(A)\) is *convenient*if it intersects both coordinate axes. The *Newton polygon*of the Newton diagram \(\Delta \) is the union of the compact edges of the boundary of \(\Delta \), and we will denote it by \(\delta ^{*}(\Delta )\). A convenient Newton diagram is *elementary*if its boundary has exactly one compact edge. In this case, following Teissier [[12][20]], we will denote by the elementary Newton diagram of \(A=\{(m,0), (0,n)\}\), for any positive natural numbers *m*, *n*(see Figure [1][21]).

**Fig. 1**

[image: Fig. 1]

[Full size image][22]

Elementary Newton diagram

The *inclination*of the elementary Newton diagram (and of any of its translations) is *m*/*n*. Any convenient Newton diagram \({\mathcal {N}}\) can be written as a Minkowski sum of elementary Newton diagrams, where inclinations of successive elementary diagrams form a strictly decreasing sequence. This writing is called the *canonical representation*of \({\mathcal {N}}\). A convenient Newton diagram \({\mathcal {N}}\) can also be written as a sum of elementary Newton diagrams where \(\gcd (m_{i},n_{i})=1\) for any \(i\in \{1,\ldots ,r\}\) and \(m_{i}/n_{i}\ge m_{i+1}/n_{i+1}\) for \(i\in \{1,\ldots ,r-1\}\). This new writing is called the *long canonical representation*of \({\mathcal {N}}\). The long canonical representation is unique.

### Example 1.1

The long canonical representation of is

Figure [2][23] illustrates both canonical representations.

If we drop the hypothesis of \(\gcd (m_{i},n_{i})=1\) in the definition of the long canonical representation we can express \({\mathcal {N}}\) in other ways that are not canonical, for example

**Fig. 2**

[image: Fig. 2]

[Full size image][24]

Canonical and long canonical representation of

The Newton diagram \({\mathcal {N}}(f)\) of a nonzero power series \(f(x,y)=\sum _{i,j}a_{ij}x^{i}y^{j}\) is the Newton diagram \({\mathcal {N}}({\textrm{supp}}(f))\), where \({\textrm{supp}}(f):=\{(i,j)\in {\mathbb {N}}^{2}\;:\; a_{ij}\ne 0\}\) is the support of *f*. It is well-known (see [[3][25], Lemme 8.4.2]) that if is the canonical representation of \({\mathcal {N}}(f)\) then for any \(i\in \{1,\ldots ,r\}\) there are exactly \(N_i\) Newton-Puiseux roots of *f*of order \(\frac{M_i}{N_i}\). Let *S*be a compact edge of \({\mathcal {N}}(f)\) of inclination *p*/*q*, where *p*and *q*are coprime integers. The initial part of *f*(*x*, *y*) with respect to *S*is the quasi-homogeneous polynomial \(f_S(x,y) = \sum _{ij} a_{ij}x^iy^j\) where the sum runs over all points in \(S\cap {\textrm{supp}}(f)\). Let \(f_S(x,y)=ax^ky^l\prod _{j=1}^r(y^q-c_jx^p)^{s_j}\) be the factorization of \(f_S\) into irreducible factors, where *k*, *l*are non-negative integers and \(a,c_j\in {\mathbb {C}}\backslash \{0\}\) with \(c_j\) pairwise different. The power series *f*(*x*, *y*) is *non-degenerate*(in the sense of Kouchnirenko [[11][26]]) on *S*if one of the following equivalent conditions holds:

1. (ND1)

\(s_j=1\) for any \(j\in \{1,\ldots ,r\}\).

2. (ND2)

All non-zero roots of \(f_S(1,y)\) are simple.

3. (ND3)

All Newton-Puiseux roots of *f*of order *p*/*q*have different initial coefficients.

Let \(\Delta \) be a Newton diagram and *k*a nonnegative integer. The *symbolic**k**th derivative*\(\Delta ^{(k)}\) of \(\Delta \) is the Newton diagram of the set \((\Delta -(0,k))\cap {\mathbb {N}}^2\).

### Example 1.2

The symbolic first derivative of is and its symbolic second derivative is (see Figure [3][27]).

**Fig. 3**

[image: Fig. 3]

[Full size image][28]

Symbolic derivatives

The main result of this paper is

### Theorem 1.3

Let \(f\in {\mathbb {C}}[[x,y]]\) be a generic element of \(K(b_0,\ldots ,b_h)\). Put \(e_{i} =\gcd (b_{0}, \ldots , b_{i})\), \(n_{i}=\frac{e_{i-1}}{e_{i}}\), \(m_{i}=\frac{b_{i}}{e_{i}}\) and for \(i\in \{1,\ldots ,h\}\). Fix \(1\le k < b_0\) and let \(\{1,\dots ,i_k\}=\{\,j\in \{1,\dots ,h\}: e_{j-1}>k\,\}\). Then \(\frac{\partial ^{k}f}{\partial y^k}\) admits the following factorization:

$$\begin{aligned} \frac{\partial ^{k}f}{\partial y^k}=\Gamma ^{(1)}\cdots \Gamma ^{(i_{k})}, \end{aligned}$$

where, for any \(\ell \in \{1,\ldots ,i_{k}\}\), the power series \(\Gamma ^{(\ell )}\) is not necessarily irreducible, and it verifies:

1. (1)

\({\textrm{cont}}(f,v)=\frac{b_{\ell }}{b_{0}}\) for any irreducible factor *v*of \(\Gamma ^{(\ell )}\).

2. (2)

Let *t*be the natural number such that \(0< t\le n_\ell \) and \(t\equiv k\) (mod \(n_{\ell }\)). If is the long canonical representation of \(\Delta _{\ell }^{(t)}\) and \(m=\min \{e_{\ell }, k\}-\lceil \frac{k}{n_{\ell }}\rceil \) then \(\Gamma ^{(\ell )}\) can be written as a product of irreducible factors

$$\begin{aligned} \Gamma ^{(\ell )}=\prod _{j=1}^{r}z^{(\ell )}_j\prod _{i=1}^{m}w^{(\ell )}_i \end{aligned}$$

such that

  1. (2a)

for any power series \(z^{(\ell )}_j\), \(\,{\textrm{cont}}(f_{\ell },z^{(\ell )}_j)=\frac{M_{j}}{n_{1}\cdots n_{\ell -1}N_{j}}\) and

$$\begin{aligned} \begin{aligned} {\text {Char}}(z^{(\ell )}_j)= \left\{ \begin{array}{lr} \left\{ \frac{b_{1}}{b_{0}},\ldots , \frac{b_{\ell -1}}{b_{0}}\right\} & \hbox {if } N_j=1\\ & \\ \left\{ \frac{b_{1}}{b_{0}},\ldots , \frac{b_{\ell -1}}{b_{0}}, \frac{M_{j}}{n_{1}\cdots n_{\ell -1}N_{j}}\right\} & \hbox {if } N_j>1. \end{array} \right. \end{aligned} \end{aligned}$$

  2. (2b)

for any power series \(w^{(\ell )}_i\), \(\,{\textrm{Char}}(w^{(\ell )}_i)=\left\{ \frac{b_{1}}{b_{0}},\ldots , \frac{b_{\ell }}{b_{0}}\right\} \) and the contact \({\textrm{cont}}(f_{\ell },w^{(\ell )}_i)=\frac{b_{\ell }}{b_{0}}\).

  3. (2c)

\({\textrm{cont}}(v_1,v_2)=\min \{{\textrm{cont}}(f_l,v_1),{\textrm{cont}}(f_l,v_2)\}\) for any two different irreducible factors \(v_1,v_2\) of \(\Gamma ^{(\ell )}\).

The curve \(\left\{ \tfrac{\partial f}{\partial y}=0\right\} \) is called the *first polar*of \(C=\{f(x,y)=0\}\) and \(\left\{ \tfrac{\partial ^{k}f}{\partial y^k}=0\right\} _{k=2}^{b_{0}-1}\) are called *higher order polars*of *C*.

Theorem [1.3][29] will be proved in Section [4][30]. It improves the results of Casas-Alvero (see [[2][31]]) and those of the first and second author (see [[7][32]]) since, under the hypothesis that *f*is generic in its equisingularity class, we fully describe the equisingularity class of the considered polar curve. Theorem [1.3][29] also generalizes the results of Casas-Alvero (see [[1][33]]) and Hefez-Hernandes-Hernández (see [[10][34]]) to higher order polars.

It is well known that the equisingularity class of the polar curves can vary within a family of equisingular branches. The motivation of this paper was to prove that it is fixed and independent of the analytical type of the branches, under the hypothesis that they are generic in their equisingularity class.

## 2 Symbolic Derivatives of a Newton Diagram

In this section we prove some properties of the symbolic derivatives of a Newton diagram.

### Property 2.1

For any Newton diagram \(\Delta \) and any nonnegative integers *k*, *l*we have \((\Delta ^{(k)})^{(l)}=\Delta ^{(k+l)}\).

### Proof

Note that \({\textrm{supp}}(\Delta ^{(k+l)})=({\textrm{supp}}(\Delta )-(0,k+l))\cap \mathbb N^2=({\textrm{supp}}(\Delta ^{(k)})-(0,l))\cap \mathbb {N}^2={\textrm{supp}}(\Delta ^{(k)})^{(l)}\). \(\square \)

Let \(\omega \in ({\mathbb {R}}_{> 0})^2\) and \(\Delta \) be any Newton diagram. The \(\omega \) -*weigthed initial part*of \(\Delta \) is

$$\begin{aligned} {\textrm{in}}_{\omega }(\Delta ):=\{d\in \Delta \;:\;\langle d, \omega \rangle =\min \{\langle e ,\omega \rangle \;:\;e\in \Delta \}\}, \end{aligned}$$

where \(\langle \cdot ,\cdot \rangle \) denotes the canonical scalar product in \({\mathbb {R}}^2\).

The Minkowski sum of Newton diagrams satisfies the following property (see [[5][35], Theorem 1.5, Chapter IV]).

### Property 2.2

Let \(\Delta _1, \Delta _2\) be two Newton diagrams and \(\omega \in ({\mathbb {R}}_{> 0})^2\). Then

$$\begin{aligned} {\textrm{in}}_{\omega }(\Delta _1+\Delta _2)={\textrm{in}}_{\omega }(\Delta _1)+{\textrm{in}}_{\omega }(\Delta _2). \end{aligned}$$

### Remark 2.3

Let

(3)

be the canonical or the long canonical representation of \({\mathcal {N}}\). For any \(0\le j\le r\) we put \(A_j:=(a_j,b_j)\), where \(a_j=\sum _{i=j+1}^rM_i\) and \(b_j=\sum _{i=1}^jN_i\) (see Figure [4][36]).

**Fig. 4**

[image: Fig. 4]

[Full size image][37]

Points \(A_{i-1}\) and \(A_i\)

Note that the set \(T:=\{A_j\;:\; 0\le j\le r\}\) is a subset of the Newton polygon of \({\mathcal {N}}\) containing the vertices of \(\mathcal N\), with equality if and only if ( [3][38]) is the canonical representation of \({\mathcal {N}}\). In fact, if we consider \(\omega _j:=(N_j,M_j)\) then for any \(i>j\) and for any \(i \le j\). By Property [2.2][39] we have \((a_j,b_j)\in {\textrm{in}}_{\omega _j}(\Delta )\), so \(A_j\in \delta ^{*}(\Delta )\).

For any Newton polygon \(\Delta \) let \(\textrm{trunc}(\Delta ,k):={\mathcal {N}}(\{(i,j)\in \Delta \cap \mathbb N^2\;:\; j\ge k\})\). It follows directly from the definitions that

$$\begin{aligned} \textrm{trunc}(\Delta ,k)=\Delta ^{(k)}+(0,k). \end{aligned}$$

(4)

### Proposition 2.4

Let be the long canonical representation of the convenient Newton diagram \(\Delta \). Put , and assume that \(0\le k\le \sum _{i=1}^s N_i\). Then

$$\begin{aligned} \Delta ^{(k)} = R^{(k)}+L. \end{aligned}$$

(5)

### Proof

By Remark [2.3][40] the points \(A_j=(a_j,b_j)=(\sum _{i=j+1}^rM_i,\sum _{i=1}^jN_i)\) for \(0\le j\le r\) are lattice points of \(\delta ^{*}(\Delta )\).

Let \(R_1={\mathcal {N}}(\{A_0,\dots ,A_s\})\). Since the points \(A_0,\dots ,A_s\) are the lattice points of \(\delta ^{*}(R_1)\), we get by Remark [2.3][40] that \(R_1=(a_s,0)+R\). The same argument applies \(L_1={\mathcal {N}}(\{A_s,\dots ,A_r\})\) giving \(L_1=(0,b_s)+L\). Since \(\Delta =L_1\cup R_1\), we get \(\textrm{trunc}(\Delta ,k)=L_1\cup \textrm{trunc}(R_1,k)\), and consequently \(\textrm{trunc}(\Delta ,k)=L + \textrm{trunc}(R,k)\). Hence equality ( [5][41]) follows. \(\square \)

### Corollary 2.5

Let be the long canonical representation of a convenient Newton diagram \(\Delta \). Then

Recall the notion of continued fraction expansions of rational numbers.

Let \(n,m\in {\mathbb {N}}\) with \(0<n<m\). Denote by \([h_{0},h_{1},\ldots ,h_{s}]\) the **continued fraction expansion**of \(\frac{m}{n}\), that is:

$$\begin{aligned} \frac{m}{n}=h_0+\frac{1}{h_1 +\frac{1}{h_2 +\frac{1}{\ddots + \frac{1}{h_s}}}}. \end{aligned}$$

(6)

Note that the expansion given in equation ( [6][42]) is unique if we impose the condition that \(h_s>1\), that is, *s*is the minimal possible value. This is the classical definition of a continued fraction expansion. However, if \(h_s>1\), then \([h_{0},h_{1},\ldots ,h_{s}]= [h_{0},h_{1},\ldots ,h_{s}-1,1]\). Therefore, if necessary, we can always assume that *s*is even.

Given the expansion ( [6][42]), we put \(p_{-1}=1\), \(q_{-1}=0\), \(p_{0}=h_{0}\), \(q_{0}=1\) and consider the irreducible fractions

$$\begin{aligned} \frac{p_{i}}{q_{i}}=[h_{0},h_{1},\ldots ,h_{i}]=h_0+\frac{1}{h_1 +\frac{1}{h_2 +\frac{1}{\ddots + \frac{1}{h_i}}}} \end{aligned}$$

for \(1\le i\le s\). The next properties are well-known (see for example [[13][43]]).

### Properties 2.6

With the above notations we have:

1. (1)

\(p_{i+1}=h_{i+1}p_{i}+p_{i-1}\) and \(q_{i+1}=h_{i+1}q_{i}+q_{i-1}\), for \(0\le i\le s-1\).

2. (2)

\(p_{i}q_{i-1}-p_{i-1}q_{i}=(-1)^{i+1}\).

3. (3)

\(\gcd (p_{i},q_{i})=1\).

4. (4)

\(\frac{p_0}{q_0}<\frac{p_2}{q_2}<\cdots \le \frac{m}{n}\).

5. (5)

\(\frac{p_1}{q_1}>\frac{p_{3}}{q_{3}}>\cdots \ge \frac{m}{n}.\)

Observe that \(\frac{p_{s}}{q_{s}}=\frac{m}{n}\). If *m*and *n*are coprime then \(m=p_{s}\) and \(n=q_{s}\).

### Proposition 2.7

If with \(n,m\in {\mathbb {N}}\) coprime then

In particular if then , that is the first quadrant.

### Proof

Suppose that *s*is even. Consider the Newton diagram

Since \(p_1/q_1>p_3/q_3>\dots >p_{s-1}/q_{s-1}\), we get by Remark [2.3][40] that the points

$$\begin{aligned} B_i:=\Bigl (\sum _{j=i+1}^{s/2}h_{2j}p_{2j-1}, \, 1 + \sum _{j=1}^{i}h_{2j}q_{2j-1}\Bigr ) \end{aligned}$$

are the vertices of *N*for \(i=0, \dots , s/2\). By the first item of Properties [2.6][44] we get

$$\begin{aligned} B_i = \left( \sum _{j=i+1}^{s/2}(p_{2j}-p_{2j-2}), \, 1 + \sum _{j=1}^{i}(q_{2j}-q_{2j-2})\right) = (p_{s}-p_{2i}, q_{2i}) \end{aligned}$$

for \(i=0, \dots , s/2\).

We claim that

$$\begin{aligned} N={\mathcal {N}}(\{B_0, \dots , B_{s/2}\})=\textrm{trunc}(\Delta ,1). \end{aligned}$$

(7)

**Fig. 5**

[image: Fig. 5]

[Full size image][45]

Points \(B_i\)

Consider the closed polygon \({\mathcal {P}}\) which vertices are \(B_{-1}:=(p_s,0), B_0, \dots , B_{s/2}\) (see Figure [5][46]).

In order to prove equality ( [7][47]) it is enough to show that there are no lattice points in the interior of \({\mathcal {P}}\). Let *B*denote the number of lattice points on the boundary of the polygon \({\mathcal {P}}\) and let *I*denote the number of lattice points in its interior.

By the third item of Properties [2.6][44] we get \(B=2+\sum _{i=0}^{s/2-1}h_{2i+2}\). By Pick’s Formula [[4][48], Theorem 13.51], we have \(2\text{ Area }\,{\mathcal {P}}=2I+B-2\). On the other hand if \(\triangle _i\) denotes the triangle of vertices \(O,B_{i-1},B_i\) for \(i=0, \dots , r\) then \(2\text{ Area }\,{\mathcal {P}}=\sum _{i=0}^{s/2} 2\text{ Area }\,\triangle _i - p_sq_s\). We have \(2\text{ Area }\,\triangle _0=p_s\) and \(2\text{ Area }\,\triangle _i=(p_s-p_{2i-2})q_{2i}-(p_s-p_{2i})q_{2i-2}=p_sq_{2i}-p_sq_{2i-2}+ p_{2i}q_{2i-2}-p_{2i-2}q_{2i}=p_sq_{2i}-p_sq_{2i-2}+(h_{2i}p_{2i-1}+p_{2i-2})q_{2i-2}-p_{2i-2}(h_{2i}q_{2i-1}+q_{2i-2})= p_sq_{2i}-p_sq_{2i-2}+h_{2i}(p_{2i-1}q_{2i-2}-p_{2i-2}q_{2i-1})= p_{s}q_{2i}-p_{s}q_{2i-2}+h_{2i}\) for \(i=1,\dots ,s/2\). Hence

$$\begin{aligned} 2\text{ Area }\,{\mathcal {P}}= p_s+\sum _{i=1}^{s/2} (p_{s}q_{2i}-p_{s}q_{2i-2}+h_{2i}) - p_sq_s = \sum _{i=1}^{s/2} h_{2i}. \end{aligned}$$

Therefore \(2\text{ Area }\,{\mathcal {P}}=B-2\), and so \(I=0\).

Suppose now that *s*is odd. Note that \([h_0,\ldots ,h_s]\) can be represented by the even continued fraction \([h_0,\ldots ,h_{s}-1,1]\). We have \([h_0,\ldots ,h_{s}-1]=\frac{{\tilde{p}}_s}{{\tilde{q}}_s}\), where, by the first item of Properties [2.6][44], we get \({\tilde{p}}_s=(h_s-1)p_{s-1}+p_{s-2}=p_s-p_{s-1}\) and \({\tilde{q}}_s=(h_s-1)q_{s-1}+q_{s-2}=q_s-q_{s-1}\). Therefore the proof for the odd case follows from the statement for the even case. \(\square \)

## 3 Technical Tools

The *extreme right edge*of a Newton polygon is its compact edge of greatest inclination.

### Lemma 3.1

Let \(\lambda (x)=\sum _{i=1}^{N} a_ix^{i/n}\) be a finite Puiseux power series of characteristic \((n, b_1,\ldots , b_l)\) and let \(v\in {\mathbb {C}}[[x,y]]\) be an irreducible power series such that \(v(x,\lambda (x))\ne 0\). Let

(8)

be the canonical representation of the Newton diagram of \({{\hat{v}}}(x,y):=v(x^{n},y+\lambda (x^{n}))\). Then

1. (i)

\(M_i/N_i\le N \) for all *i*such that \(1< i\le r\),

2. (ii)

\(M_1/N_1= n\,{\textrm{cont}}(\lambda ,v)\),

3. (iii)

if \(M_1/N_1>N\) and \({{\hat{v}}}\) is non-degenerate on the extreme right edge of its Newton polygon, then \(M_1\) and \(N_1\) are coprime and

$$\begin{aligned}\begin{aligned}{\text {Char}}(v)= \left\{ \begin{array}{lr} \left( \frac{b_{1}}{n},\ldots , \frac{b_{\ell }}{n}\right) & \hbox {if } N_1=1\\ & \\ \left( \frac{b_{1}}{n},\ldots , \frac{b_{\ell }}{n}, \frac{M_{1}}{nN_{1}}\right) & \hbox {if } N_1>1. \end{array} \right. \end{aligned} \end{aligned}$$

### Proof

Let \(\alpha _1,\dots ,\alpha _m\) be the Newton-Puiseux roots of *v*. Then the set of Newton-Puiseux roots of \({{\hat{v}}}\) equals \(\{ \alpha _i(x^n)-\lambda (x^n): 1\le i\le m \} . \) Hence the set of inclinations of the edges of the Newton diagram of \({{\hat{v}}}\) is equal to \( \{\, n\,{\textrm{ord}}(\alpha _i(x)-\lambda (x)): 1\le i\le m \,\}\). In particular the biggest inclination \(M_1/N_1\) of the Newton polygon of \({{\hat{v}}}(x,y)\) equals \(n\,{\textrm{cont}}(\lambda ,v)\), which gives (ii).

If \(M_1/N_1\le N\) then (i) is clearly true. Hence in what follows, assume that \(n\,{\textrm{cont}}(\lambda ,v)=M_1/N_1>N\). Then any Newton-Puiseux root \(\alpha _i\) of *v*that realizes the contact with \(\lambda \) has the form \(\alpha _i=\lambda +c_ix^{M_1/(nN_1)}+\cdots \) with some \(c_i\ne 0\). Thus for any \(1\le j\le m\): either \({\textrm{ord}}(\alpha _j-\lambda )=M_1/(n N_1)\) or \({\textrm{ord}}(\alpha _j-\lambda )\le N/n\). This proves (i).

Assume that \({{\hat{v}}}\) is non-degenerate on the compact edge *S*of ( [8][49]) of inclination \(M_1/N_1\) and suppose to the contrary that \(\alpha _i\) has a characteristic exponent \(\gamma \) bigger than \(M_1/(n N_1)\). Then there exists \(k\ne i\) such that \(\gamma ={\textrm{ord}}(\alpha _k-\alpha _i)\). This implies that \(c_ix^{M_1/N_1}\) is the initial term of both \(\alpha _i(x^n)-\lambda (x^n)\) and \(\alpha _k(x^n)-\lambda (x^n)\). Consequently after (ND3), \({{\hat{v}}}\) is degenerate on the edge *S*which is a contradiction. Thus all characteristic exponents of \(\alpha _i\) are less than of equal to \(M_1/(n N_1)\).

By ( [8][49]) there are \(N_1\) Newton-Puiseux roots of \({{\hat{v}}}\) of order \(\frac{M_1}{ N_1}\). Write \(\frac{M_1}{n N_1}=\frac{m_{l+1}}{n\cdot n_{l+1}}\) with \(m_{l+1}\) and \(n_{l+1}\) coprime. According to ( [2][19]) there are \(n_{l+1}\) Newton-Puiseux roots \(\alpha _j\) of *v*such that \({\textrm{ord}}(\alpha _j-\alpha _i) > \frac{b_{l}}{n}\). These Newton-Puiseux roots of *v*yield the Newton-Puiseux roots \(\alpha _j(x^n)-\lambda (x^n)\) of \({{\hat{v}}}\) of order \(M_1/N_1\). Hence \(N_1=n_{l+1}\). This proves (iii). \(\square \)

### Corollary 3.2

Let \(\lambda =\sum _{i=1}^N a_ix^{i/n}\) be a finite Puiseux series of characteristic \((n, b_1,\ldots , b_l)\) with minimal polynomial \(g\in {\mathbb {C}}[[x]][y]\). Let \(v\in {\mathbb {C}}[[x,y]]\) be a power series coprime with *g*. Set \({{\hat{v}}}(x,y)=v(x^{n},y+\lambda (x^{n}))\). Let

be the long canonical representation of \({{\mathcal {N}}}({{\hat{v}}})\). Assume that for some rational number \(q\ge N\) the power series \({{\hat{v}}}\) is non-degenerate on all edges of inclination bigger than *q*. Let *r*be the number of elements of the set \(\{\,i\in \{1,\dots ,s\}: M_i/N_i>q\,\}\). Then there exists a decomposition \(v=\prod _{i=1}^a v_i\) into irreducible factors in \({\mathbb {C}}[[x,y]]\) such that:

1. (i)

\({\textrm{cont}}(v_i,g)>q/n\) if and only if \(1\le i\le r\),

2. (ii)

for every \(1\le i\le r\); \({\textrm{cont}}(v_i,g)=\frac{M_{i}}{n\cdot N_{i}}\) and

$$\begin{aligned}\begin{aligned}{\text {Char}}(v_i)= \left\{ \begin{array}{lr} \left( \frac{b_{1}}{n},\ldots , \frac{b_{\ell }}{n}\right) & \hbox {if } N_{i}=1\\ & \\ \left( \frac{b_{1}}{n},\ldots , \frac{b_{\ell }}{n}, \frac{M_{i}}{nN_{i}}\right) & \hbox {if } N_i>1, \end{array} \right. \end{aligned} \end{aligned}$$

3. (iii)

for every \(1\le i<j\le r\); \({\textrm{cont}}(v_i,v_j)=\min \{{\textrm{cont}}(v_i,g),{\textrm{cont}}(v_j,g)\}\).

### Proof

Let \(v=\prod _{i=1}^a v_i\) be a decomposition of *v*into irreducible factors in \({\mathbb {C}}[[x,y]]\) such that \({\textrm{cont}}(g,v_i)\ge {\textrm{cont}}(g,v_{i+1})\), for \(1\le i<a\). Choose \(r'\in \{1,\ldots ,a\}\) such that \({\textrm{cont}}(v_i,g)>q/n\) for any \(1\le i\le r'\) and \({\textrm{cont}}(v_i,g)\le q/n\) for any \(r'+1\le i\le a\). Then by Lemma [3.1][50], for \(1\le i\le r'\), the Newton diagram of \({{\hat{v}}}_i:=v_i(x^{n},y+\lambda (x^{n}))\) has one edge *L*of inclination \(n\,{\textrm{cont}}(v_i,g)\) and all other edges have inclinations not greater than *q*. Let \(V_i={{\hat{v}}}/{{\hat{v}}}_i\). Then \({\mathcal {N}}({{\hat{v}}})= {\mathcal {N}}(V_i)+{\mathcal {N}}({{\hat{v}}}_i)\). In particular \({\mathcal {N}}({{\hat{v}}})\) has an edge *S*of inclination \(n\,{\textrm{cont}}(v_i,g)\). Since \({{\hat{v}}}\) is non-degenerate on *S*and the initial part of \({{\hat{v}}}_i\) with respect to *L*divides the initial part of \({{\hat{v}}}\) with respect to *S*, we get, by \(\mathrm{(ND1)}\) that \({{\hat{v}}}_i\) is non-degenerate on *L*. By (ii) and (iii) of Lemma [3.1][50], the long canonical representation of \({{\mathcal {N}}}({{\hat{v}}}_i)\) has only one elementary Newton diagram (corresponding to *L*) of inclination greater than *q*. For \(r'+1\le i\le a\), (i) and (ii) of Lemma 1 imply that the inclinations of \({{\mathcal {N}}}({{\hat{v}}}_i)\) are less than or equal to *q*.

From the identity

$$\begin{aligned} {\mathcal {N}}({{\hat{v}}}) = \sum _{i=1}^a {\mathcal {N}}({{\hat{v}}}_i) \end{aligned}$$

we have \(r=r'\) and the extreme right compact edges of \({\mathcal {N}}({{\hat{v}}}_i)\) for \(1\le i\le r\) are in one-to-one correspondence with the set of elementary Newton diagrams of the long canonical representation of \({\mathcal {N}}({{\hat{v}}})\).

Then, by (iii) of Lemma [3.1][50], (i) and (ii) hold true.

Suppose that there exists \(1\le i<j\le r\) such that the conclusion of (iii) does not hold. This is possible only if \({\textrm{cont}}(v_i,g)={\textrm{cont}}(v_j,g)<{\textrm{cont}}(v_i,v_j)\). Let \(\alpha _{i_0}\) be a Newton-Puiseux root of \(v_i\) such that \({\textrm{ord}}(\alpha _{i_0}-\lambda )={\textrm{cont}}(v_i,g)\) and let \(\alpha _{j_0}\) be a Newton-Puiseux root of \(v_j\) such that \({\textrm{ord}}(\alpha _{j_0}-\alpha _{i_0})={\textrm{cont}}(v_i,v_j)\). Then the Puiseux series \(\alpha _{i_0}(x^n)-\lambda (x^n)\), \(\alpha _{j_0}(x^n)-\lambda (x^n)\) have the same initial term of order \(n\,{\textrm{cont}}(v_i,g)\). Hence, by (ND3), \({{\hat{v}}}\) is degenerate on the edge of inclination \(n\,{\textrm{cont}}(v_i,g)\). This contradiction gives (iii). \(\square \)

### Remark 3.3

For any positive integers *r*, *s*we have the epimorphism of groups \({\mathbb {U}}_r\ni \epsilon \longrightarrow \epsilon ^s\in {\mathbb {U}}_{r/\gcd (r,s)}\). This becomes an isomorphism when *r*, *s*are coprime.

### Properties 3.4

Let \(n\in {\mathbb {N}}\), \(n>1\). Consider the strictly decreasing sequence \(n=e_0>e_1>\cdots >e_h=1\) from page 1. Put \(n_{i}=\frac{e_{i-1}}{e_{i}}\) for \(1\le i\le h\). Then for any \(l\in \{1,\ldots , h\}\) we get:

1. (1)

\(\prod _{\varepsilon \in {\mathbb {U}}_{e_{l-1}}} (t-c\varepsilon ^{b_l}) = (t^{n_l}-c^{n_l})^{e_l}\) for any \(c\in {\mathbb {C}}\).

2. (2)

\(\prod _{\varepsilon \in {\mathbb {U}}_{e_{l-1}}\setminus {\mathbb {U}}_{e_l}} (1-\varepsilon ^{b_l}) = n_l^{e_l} \).

3. (3)

\(\sum _{\varepsilon \in {\mathbb {U}}_{n_l}} \varepsilon ^{i} = \left\{ \begin{array}{ll} n_l,& \hbox { if}\ i \equiv 0 \pmod {n_l} \\ 0, & \text{ otherwise }. \end{array}\right. \)

### Proof

By Remark [3.3][51] the map \(U_{e_{l-1}}\ni \varepsilon \rightarrow \varepsilon ^{b_l}\in U_{n_l}\) is a group epimorphism, so

$$\begin{aligned} \prod _{\varepsilon \in U_{e_{l-1}}} (t-c\varepsilon ^{b_l}) = \prod _{\tau \in U_{n_l}} (t-c\tau )^{e_l} = (t^{n_l}-c^{n_l})^{e_l}. \end{aligned}$$

In order to prove (2) consider \(h(x):=\prod _{\tau \in U_{n_l}\setminus \{1\}} (x-\tau )\). We have \((x-1)h(x)=x^{n_l}-1\), hence \(h(x)+(x-1)h'(x)=\frac{d}{dx} (x^{n_l}-1)=n_lx^{n_l-1}\). Substituting \(x=1\) we get \(h(1)=n_l\) which gives

$$\begin{aligned} \prod _{\varepsilon \in U_{e_{l-1}}\setminus U_{e_l}} (1-\varepsilon ^{b_l}) = \prod _{\tau \in U_{n_l}\setminus \{1\}} (1-\tau )^{e_l} = n_l^{e_l} . \end{aligned}$$

Statement (3) follows from Remark [3.3][51]. \(\square \)

Let \(f(x,y)=\sum _{ij}a_{ij}x^iy^j\in {\mathbb {C}}[[x,y]\) and \(\omega =(\omega _1,\omega _2)\in {\mathbb {Q}}_{>0}^2\). The \(\omega \)*-weighted order of**f*is \({\textrm{ord}}_{\omega }(f)=\min \{\omega _1 i+ \omega _2 j\,:\; a_{ij}\ne 0\}\) and the \(\omega \)*-weighted initial form of**f*is \({\textrm{in}}_{\omega }(f)=\sum _{ij}a_{ij}x^iy^j\), where the sum runs over (*i*, *j*) such that \(\omega _1 i+ \omega _2 j={\textrm{ord}}_{\omega }(f)\).

### Lemma 3.5

Let \(f\in K(n,b_1,\ldots ,b_h)\) and \(\alpha =\sum _{i\ge n} a_ix^{i/n}\) be a Newton-Puiseux root of *f*. Let \(\lambda =\sum _{i=n}^{b_{l}-1} a_ix^{i/n}\) and \({{\hat{f}}}(x,y)=f(x^{n/e_{l-1}},y+\lambda (x^{n/e_{l-1}}))\). Let \(\Delta \) be the Newton diagram of \({{\hat{f}}}\). Then, for \(k<e_{l-1}\) we have \(\Delta ^{(k)}=R^{(t)}+L\) where and *t*is the remainder of the division of *k*by \(n_l\). The inclination of every compact edge of *L*is smaller than or equal to \(m_l/n_l\) and the inclination of every compact edge of \(R^{(t)}\) is bigger than \(m_l/n_l\). Moreover if *f*is a generic member of \(K(n,\ldots ,b_h)\) then

$$\begin{aligned} {\mathcal {N}}\left( \tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\right) = \Delta ^{(k)} \end{aligned}$$

(9)

and \(\frac{\partial ^k {{\hat{f}}}}{\partial y^k}\) is non-degenerate on all edges of its Newton diagram with inclinations bigger than \(m_l/n_l\).

### Proof

Observe that \(\lambda (x^{n/e_{l-1}})\in {\mathbb {C}}[[x]]\), so \({{\hat{f}}}(x,y)=f(x^{n/e_{l-1}},y+\lambda (x^{n/e_{l-1}}))\) is a formal power series in \({\mathbb {C}}[[x,y]]\). The set of Newton-Puiseux roots of \({{\hat{f}}}(x,y)\) is \({\textrm{Zer}}{{\hat{f}}}=\{\alpha _{\epsilon }(x^{n/e_{l-1}})-\lambda (x^{n/e_{l-1}})\;:\;\epsilon \in {\mathbb {U}}_n\}\). Hence \(\{{\textrm{ord}}(\gamma )\;:\; \gamma \in {\textrm{Zer}}{{\hat{f}}}\}=\left\{ \frac{b_j}{e_{l-1}}\;:\; j=1,\ldots ,l \right\} \). In particular the biggest inclination of the Newton diagram \({{\mathcal {N}}}({{\hat{f}}})\) equals \(\frac{m_l}{n_l}\). Denote by *S*the compact edge of \({{\mathcal {N}}}({{\hat{f}}})\) of this inclination. If *g*is the minimal polynomial of \(\lambda (x)\) then *g*is a *l*-semiroot of *f*, that is, \(g\in {\mathbb {C}}[[x]][y]\) is monic, irreducible, its *y*-degree equals \(n/e_{l-1}\) and the intersection multiplicity of *f*and *g*is \({{\bar{b}}}_l:=b_l+\sum _{i=1}^{l-1}\left( \frac{e_{i-1}-e_i}{e_{l-1}}\right) b_i\) (see [[15][52], Theorem 3.9 (a)]). Hence the vertex of *S*living on the horizontal axis is \(({{\overline{b}}}_l,0)\) since \(i_0( {{\hat{f}}},y)={\textrm{ord}}(f(x^{n/e_{l-1}},\lambda (x^{n/e_{l-1}}))=i_0( f,g)\). On the other hand the length of the vertical projection of *L*equals the cardinality of the set

$$\begin{aligned} \begin{aligned}&\{\alpha _{\epsilon }\in {\text {Zer}}f\;:\;{\text {ord}}(\alpha _{\epsilon }(x^{n/e_{l-1}})-\lambda (x^{n/e_{l-1}})) =\tfrac{m_l}{n_l}\}= \{\alpha _{\epsilon }\in {\text {Zer}}f\;:\;{\text {ord}}(\alpha _{\epsilon }-\alpha )\ge \tfrac{b_l}{n}\} \end{aligned} \end{aligned}$$

which is, after ( [2][19]), equal to \(e_{l-1}\).

Let \(k=qn_l+t\) be the Euclidean division of *k*by \(n_l\). Then , for some Newton diagram *L*with inclinations less than or equal \(\frac{m_l}{n_l}\).

Consequently where the first equality follows from Property [2.1][53], the second one follows from Proposition [2.4][54] since and the third equality also follows from Proposition [2.4][54].

Now we are going to prove the second part of the lemma.

Suppose first that *f*is a Weierstrass polynomial, that is *f*is as in ( [1][55]) with \(u(x,y)=1\). Then

$$\begin{aligned} {{\hat{f}}}(x,y)=\prod _{\epsilon \in \mathbb U_n}(y-(\alpha _{\epsilon }(x^{n/e_{l-1}})-\lambda (x^{n/e_{l-1}}))). \end{aligned}$$

(10)

Fix \(q\in \{1,\dots ,n_l-1\}\) and let \(z_q:=a_{b_l+qe_l}\) be a coefficient of \(\alpha \) treated as indeterminate. Expand \({{\hat{f}}}\) as a polynomial in \(z_q\)

$$\begin{aligned} {{\hat{f}}}= {{\hat{f}}}_{q,0}+{{\hat{f}}}_{q,1}z_q+\cdots +{{\hat{f}}}_{q,n}z_q^n. \end{aligned}$$

(11)

Consider \(\omega :=(1,m_l/n_l)\).

*Claim 1.*The \(\omega -\) weighted order of \({{\hat{f}}}\) is \({\textrm{ord}}_{\omega }({{\hat{f}}})={{\bar{b}}}_l\) and the \(\omega -\) weighted initial form of \({{\hat{f}}}\) is

$$\begin{aligned} \textrm{in}_{\omega }{{\hat{f}}} = a x^b (y^{n_l}-a_{b_l}^{n_l}x^{m_l})^{e_l} \end{aligned}$$

(12)

for some nonzero complex number *a*and a nonnegative integer *b*.

Indeed, after ( [10][56]) \(\textrm{in}_{\omega }{{\hat{f}}}=\prod _{\epsilon \in {\mathbb {U}}_n}\textrm{in}_{\omega }A_{\epsilon }\), where \(A_{\epsilon }=y-(\alpha _{\epsilon }(x^{n/e_{l-1}})-\lambda (x^{n/e_{l-1}}))\). Notice that

$$\begin{aligned} \begin{aligned} \text {in}_{\omega }A_{\epsilon }=\left\{ \begin{array}{ll} (1-\epsilon ^{b_j})a_{b_j}x^{b_j/e_{l-1}},& \hbox {if } \epsilon \in {\mathbb {U}}_{e_{j-1}}\backslash {\mathbb {U}}_{e_{j}}\;\hbox {for } 1\le j\le l-1\\ & \\ y-a_{b_j}\epsilon ^{b_l}x^{b_l/e_{l-1}} & \hbox {if } \epsilon \in {\mathbb {U}}_{e_{l-1}}. \end{array} \right. \end{aligned} \end{aligned}$$

Hence

$$\begin{aligned} \textrm{in}_{\omega }{{\hat{f}}}= & \left( \prod _{j=1}^{l-1}\prod _{\epsilon \in {\mathbb {U}}_{e_{j-1}}\backslash {\mathbb {U}}_{e_{j}}}(1-\epsilon ^{b_j})a_{b_j}x^{b_j/e_{l-1}}\right) \prod _{\epsilon \in {\mathbb {U}}_{e_{l-1}}}\left( y-a_{b_l}\epsilon ^{b_l}x^{b_l/e_{l-1}}\right) . \end{aligned}$$

By Properties [3.4][57] we get

$$\begin{aligned}\textrm{in}_{\omega }{{\hat{f}}}= & \left( \prod _{j=1}^{l-1}n_j^{e_j}a_{b_j}^{e_{j-1}-e_j}x^{b_j(e_{j-1}-e_j)/e_{l-1}}\right) (y^{n_l}-a_{b_l}^{n_l}x^{b_l/e_l})^{e_l}.\\ \end{aligned}$$

Notice that \(b_l/e_l=m_l\) and the proof of Claim 1 follows taking \(a:=\prod _{j=1}^{l-1} n_j^{e_j}a_{b_j}^{e_{j-1}-e_j}\) and \(b:={\textrm{ord}}_x {{\hat{f}}}(x,0)-b_l={{\bar{b}}}_l-b_l\in {\mathbb {N}}\).

*Claim 2.*Let \(q\in \{1,\dots ,n_l-1\}\) and \({{\hat{f}}}_{q,0}\), \({{\hat{f}}}_{q,1}\) be as in ( [11][58]). Then \({\textrm{ord}}_{\omega }({{\hat{f}}}_{q,1})={{\bar{b}}}_l+\frac{q}{n_l}\) and

$$\begin{aligned} \textrm{in}_{\omega }({{\hat{f}}}-{{\hat{f}}}_{q,0}) = \textrm{in}_{\omega }{{\hat{f}}}_{q,1}z_q = -e_{l-1} a a_{b_l}^{s-1} x^{b+(m_ls+q)/n_l} y^{n_l-s} (y^{n_l}-a_{b_l}^{n_l}x^{m_l})^{e_l-1} z_q, \end{aligned}$$

where \(s\in \{1,\dots ,n_l\}\) is the solution of the congruence \(m_ls+q\equiv 0 \pmod {n_l}\).

Indeed by Leibnitz rule

$$\begin{aligned} \frac{d}{dz_q}{{\hat{f}}}={{\hat{f}}}\sum _{\varepsilon \in {\mathbb {U}}_n} \frac{-\varepsilon ^{b_l+qe_l} x^{(m_l+q)/n_l}}{A_{\varepsilon }}.\end{aligned}$$

Hence by Remark [3.3][51] (for \(r=e_{l-1}\) and \(s=e_l\)) we get

$$\begin{aligned} \textrm{in}_{\omega }\frac{d}{dz_q}{{\hat{f}}}= & \textrm{in}_{\omega }{{\hat{f}}} \cdot \left( \sum _{\varepsilon \in {\mathbb {U}}_{e_{l-1}}} \frac{-\varepsilon ^{b_l+qe_l} x^{(m_l+q)/n_l}}{y-\varepsilon ^{b_l}a_{b_l}x^{m_l/n_l}} \right) \nonumber \\= & \textrm{in}_{\omega }{{\hat{f}}} \cdot \left( \sum _{\varepsilon \in {\mathbb {U}}_{e_{l-1}}} \frac{-(\varepsilon ^{e_l})^{m_l+q} x^{(m_l+q)/n_l}}{y-(\varepsilon ^{e_l})^{m_l}a_{b_l}x^{m_l/n_l}} \right) \nonumber \\= & - e_lx^{(m_l+q)/n_l}\textrm{in}_{\omega }{{\hat{f}}} \cdot \sum _{\theta \in {\mathbb {U}}_{n_l}} \frac{\theta ^{m_l+q} }{y-\theta ^{m_l}a_{b_l}x^{m_l/n_l}}. \end{aligned}$$

(13)

Let \(q'\) be a solution of the congruence \(m_lq'\equiv q\pmod {n_l}\). Then

$$\begin{aligned} \sum _{\theta \in {\mathbb {U}}_{n_l}} \frac{\theta ^{m_l+q}}{y-\theta ^{m_l}a_{b_l}x^{m_l/n_l}} = \sum _{\theta \in {\mathbb {U}}_{n_l}} \frac{(\theta ^{m_l})^{1+q'}}{y-\theta ^{m_l}a_{b_l}x^{m_l/n_l}} = \sum _{\varepsilon \in {\mathbb {U}}_{n_l}} \frac{\varepsilon ^{1+q'}}{y-\varepsilon a_{b_l}x^{m_l/n_l}}, \nonumber \\ \end{aligned}$$

(14)

where the last equality follows from Remark [3.3][51] for \(r=n_{l}\) and \(s=m_l\).

Using the equality

$$\begin{aligned} \frac{y^{n_l}-a_{b_l}^{n_l}x^{m_l}}{y-\varepsilon a_{b_l}x^{m_l/n_l}}= \sum _{j=0}^{n_l-1} \varepsilon ^j a_{b_l}^jx^{jm_l/n_l} y^{n_l-1-j} \end{aligned}$$

for any \(\varepsilon \in {\mathbb {U}}_{n_l}\) we have

$$\begin{aligned} (y^{n_l}-a_{b_l}^{n_l}x^{m_l}) \sum _{\varepsilon \in {\mathbb {U}}_{n_l}} \frac{\varepsilon ^{1+q'}}{y-\varepsilon a_{b_l}x^{m_l/n_l}}= & \sum _{j=0}^{n_l-1} \sum _{\varepsilon \in {\mathbb {U}}_{n_l}} \varepsilon ^{1+q'+j} a_{b_l}^jx^{jm_l/n_l} y^{n_l-1-j} \nonumber \\= & n_l a_{b_l}^{j_0}x^{j_0m_l/n_l} y^{n_l-1-j_0} \end{aligned}$$

(15)

where the last equality follows from the third part of Properties [3.4][57] and \(j_0\in \{0,\dots ,n_l-1\}\) satisfies \(1+q'+j_0 \equiv 0 \pmod {n_l}\), that is \(j_0\) is the solution of the congruence \(m_l(j+1)+q\equiv 0 \pmod {n_l}\).

From ( [13][59]), ( [14][60]) and ( [15][61]) it follows

$$\begin{aligned} \textrm{in}_{\omega }\tfrac{d}{dz_q}{{\hat{f}}} = \frac{\textrm{in}_{\omega }{{\hat{f}}}}{(y^{n_l}-a_{b_l}^{n_l}x^{m_l})}(-1)e_{l-1} a_{b_l}^{s-1}x^{(m_ls+q)/n_l} y^{n_l-s} \end{aligned}$$

(16)

with \(s=j_0+1\).

We see that \(\textrm{in}_{\omega }\tfrac{d}{dz_q}{{\hat{f}}}\) does not depend on \(z_q\). Thus, in view of the equality \(\tfrac{d}{dz_q} {{\hat{f}}} = {{\hat{f}}}_{q,1} +2{{\hat{f}}}_{q,2} z_q+\cdots +n{{\hat{f}}}_{q,n} z_q^{n-1}\) we have \(\textrm{in}_{\omega }\tfrac{d}{dz_q}{{\hat{f}}}=\textrm{in}_{\omega }{{\hat{f}}}_{q,1}\) and \(\textrm{ord}_{\omega } ({{\hat{f}}}_{q,1})<\textrm{ord}_{\omega } ({{\hat{f}}}_{q,j})\) for \(j>1\). Consequently \(\textrm{in}_{\omega }({{\hat{f}}}-{{\hat{f}}}_{q,0})= \textrm{in}_{\omega }({{\hat{f}}}_{q,1}z_q + \cdots +{{\hat{f}}}_{q,n} z_q^{n}) = \textrm{in}_{\omega }{{\hat{f}}}_{q,1}z_q\). Claim 2 follows from Claim 1 and ( [16][62]).

*Claim 3.*Let \(q\in \{1,\dots ,n_l-1\}\). Consider \(u(x,y)\in {\mathbb {C}}[[x,y]]\), \(u(0,0)=1\). Put \({{\hat{u}}}=u(x^{n/e_{l-1}},y+\lambda (x^{n/e_{l-1}})\). Then \({{\hat{u}}} {{\hat{f}}}\) is a polynomial in \(z_q\) equal to \({{\hat{u}}} {{\hat{f}}}_{q,0}+{{\hat{u}}} {{\hat{f}}}_{q,1}z_q+\cdots + {{\hat{u}}} {{\hat{f}}}_{q,n}z_q^n\), where \({{\hat{f}}}_{q,i}\) is as in ( [11][58]). Moreover \(\textrm{in}_{\omega }{{\hat{u}}} {{\hat{f}}} =\textrm{in}_{\omega }{{\hat{f}}}\) and \(\textrm{in}_{\omega }({{\hat{u}}} {{\hat{f}}}-{{\hat{u}}}{\hat{f}}_{q,0}) =\textrm{in}_{\omega }({{\hat{f}}} -{\hat{f}}_{q,0}\)).

Since \(z_q=a_{b_l+qe_l}\) is not a coefficient of \(\lambda (x)\) then \({{\hat{u}}}\) is independent of \(z_q\). The first part of the claim follows. The second part also follows since the weighted initial part of a product is the product of the weighted initial parts of the factors, and \(\textrm{in}_{\omega }({{\hat{u}}})=1\).

Consider now the truncation \(\textrm{trunc}(\Delta ,k)\) and the lines \( L_q:i+\frac{m_l}{n_l}j={{\bar{b}}}_l+\frac{q}{n_l}\) where *q*is a natural number satisfying \(0\le q\le n_l\).

*Claim 4.*The lattice points on the compact edges of \(\textrm{trunc}(\Delta ,k)\) with inclinations strictly bigger than \(\frac{m_l}{n_l}\) belong to the lines \(L_q\) with \(0\le q\le n_l-1\).

Indeed, consider \(D:=\{(i,j)\in {\mathbb {R}}^2\;:\;{{\bar{b}}}_l\le i+\frac{m_l}{n_l}j<{{\bar{b}}}_l+1\}\cap \{(i,j)\in {\mathbb {R}}^2\;:\;0\le j\le e_{l-1}\}\) (see Figure [6][63]). Observe that any lattice point \((i_0,j_0)\) in *D*belongs to \(\bigcup _{q=0}^{n_l-1}L_q\) since the rational number \(i_0+\frac{m_l}{n_l}j_0\) belonging to the interval \([{{\bar{b}}}_l,{{\bar{b}}}_l+1)\) has the form \(\bar{b}_l+\frac{q}{n_l}\) for some \(q\in \{0,\ldots ,n_l-1\}\). Let \(k<e_{l-1}\) and consider \(d:=\min \{i\in \mathbb N\;:\;i+k\frac{m_l}{n_l}\ge {{\bar{b}}}_l\}\).

Let \({{\mathcal {B}}}\) be the intersection of the compact edges of \(\textrm{trunc}(\Delta ,k)\) and the strip \({\mathbb {R}}\times [k,e_{l-1}]\). Since \(\textrm{trunc}(\Delta ,k)\) is contained in \(\Delta \) then \({{\mathcal {B}}}\) also. The set \({{\mathcal {B}}}\) is the graph of a piecewise linear, convex, decreasing function, contained in \(L_0^+:=\{(i,j)\in {\mathbb {R}}^2\;:\;i+\frac{m_l}{n_l}j\ge \bar{b}_l\}\). The endpoints of \({{\mathcal {B}}}\) are \((b,e_{l-1})\), (*d*, *k*). By convexity, \({{\mathcal {B}}}\) is contained in \(L_{n_l}^-:=\{(i,j)\in {\mathbb {R}}^2\;:\;i+\frac{m_l}{n_l}j< {{\bar{b}}}_l+1\}\) so \({{\mathcal {B}}}\subseteq D\) and Claim 4 follows.

**Fig. 6**

[image: Fig. 6]

[Full size image][64]

The set D

Fix \(q\in \{1,\ldots , n_l-1\}\). The lattice points of \(L_q\cap D\) are the solutions of the linear Diophantine equation \(n_li+m_lj=n_l{{\bar{b}}}_l+q\) for \(0\le j\le e_{l-1}\). Reducing this Diophantine equation modulo \(n_l\) we realize that there is no solution for \(j=0\) or \(j=e_{l-1}\). Hence the number of these lattice points is \(e_l-1\) since \(e_{l-1}=n_le_l\). Under the assumptions of Claim 3, the polynomial \(\textrm{in}_{\omega }({{\hat{u}}} {{\hat{f}}}_{q,1})\) has \(e_l-1\) monomials of \(\omega \) -weigthed order \({{\bar{b}}}_l+\frac{q}{n_l}\) and *y*-degree strictly less than \(e_{l-1}\). Consequently these lattice points are in the support of \(\textrm{in}_{\omega }({{\hat{u}}} {{\hat{f}}}_{q,1})\).

Let *f*be a generic member of \(K(n,b_1,\ldots ,b_h)\). As the multiplication by a nonzero constant does not affect the statement of the lemma, we may assume that \(f=uf^*\) where \(f^*\in {\mathbb {C}}[[x]][y]\) is a Weierstrass polynomial and \(u(x,y)\in {\mathbb {C}}[[x,y]]\) with \(u(0,0)=1\).

Note that equality ( [9][65]) is equivalent to equality \({\mathcal {N}}\left( y^k\tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\right) = \textrm{trunc}(\Delta ,k)\). Moreover it follows from (ND2) that \(\frac{\partial ^k {{\hat{f}}}}{\partial y^k}\) is non-degenerate on the edge *S*of its Newton diagram if and only if \(y^k\frac{\partial ^k {{\hat{f}}}}{\partial y^k}\) is also non-degenerate on the edge \(S+(0,k)\) of its Newton diagram.

Let \(\{(i_r,j_r)\}_{r=0}^s\) be the set of lattice points belonging to the compact edges of \({{\mathcal {B}}}\) with inclinations strictly bigger than \(\frac{m_l}{n_l}\), ordered by the first coordinate, that is \(i_r<i_{r+1}\) for any \(r\in \{0,\ldots , s-1\}\). Note that \((i_s,j_s)=(d,k)\). We have \(\bar{b}_l={\textrm{ord}}_{\omega }(x^{i_0}y^{j_0})<{\textrm{ord}}_{\omega }(x^{i_1}y^{j_1})<\cdots<{\textrm{ord}}_{\omega }(x^{i_{s}}y^{j_{s}})<{{\bar{b}}}_l+1\). For any \(r\in \{1,\ldots , s\}\) there exists \(q_r\in \{1,\ldots , n_l-1\}\) such that \({\textrm{ord}}_{\omega }(x^{i_r}y^{j_r})={{\bar{b}}}_l+\frac{q_r}{n_l}\).

Set \(y^k\tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}=\sum c_{ij}x^iy^j\).

By Claims 3 and 1, for any \(r\in \{1,\ldots , s\}\), we have

$$\begin{aligned} c_{i_rj_r}=W_{r}(z_1,\ldots ,z_{q_r-1})+\gamma _rz_{q_r}, \end{aligned}$$

(17)

where \(\gamma _r\in {\mathbb {C}}\backslash \{0\}\), \(W_r\in \mathbb C[z_1,\ldots ,z_{q_r-1}]\) and \(c_{i_0j_0}\) is a nonzero constant polynomial in \({\mathbb {C}}[z_1,\ldots ,z_{q_s}]\). The map

$$\begin{aligned} \begin{array}{rll}\Phi :{\mathbb {C}}^s& \longrightarrow & {\mathbb {C}}^s\\ (z_{q_1},\ldots ,z_{q_s})& \longrightarrow & \Phi (z_{q_1},\ldots ,z_{q_s})=(c_{i_1j_1}(z_{q_1},\ldots ,z_{q_s}), \ldots , c_{i_sj_s}(z_{q_1},\ldots ,z_{q_s})) \end{array} \end{aligned}$$

is surjective after the triangular form of its components given by ( [17][66]). The equality \({\mathcal {N}}\left( y^k\tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\right) = \textrm{trunc}(\Delta ,k)\) is equivalent to the non-vanishing of all coefficients \(c_{ij}\) where \((i,j)\in \{(i_r,j_r)\}_{r=1}^s\) is a vertex of \({\mathcal {B}}\).

Assume for a moment that the equality \({\mathcal {N}}\left( y^k\tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\right) = \textrm{trunc}(\Delta ,k)\) holds. Let *R*be a compact edge of \(\textrm{trunc}(\Delta ,k)\) of inclination bigger than \(\frac{m_l}{n_l}\). Denote by \(\alpha _R\) the maximum natural number *i*such that \(y^{i}\) divides the initial form \(g_R\) of \(g:=y^k\tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\) with respect to *R*. The non-degeneracy of \(y^k\tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\) on the compact edge *R*is equivalent to the non-vanishing of the discriminant of the polynomial \(y^{-\alpha _R}g_R(1,y)\). Denote by \(H_R\) this discriminant. Since the coefficients of \(y^{-\alpha _R}g_R(1,y)\) are in the set \(\{c_{i_{q_\ell }j_{q_\ell }}\}_{\ell =0}^s\) then \(H_R\in {\mathbb {C}}[c_{i_{q_1}j_{q_1}},\ldots , c_{i_{q_s}j_{q_s}}]\backslash \{0\}\).

Consider

$$\begin{aligned}{{\mathcal {A}}}_1:=\{c_{ij}\;:\;(i,j)\in \{(i_r,j_r)\}_{r=1}^s \;\mathrm{is\ a\ vertex\ of}\ {\mathcal {B}}\}\end{aligned}$$

and

$$\begin{aligned} \begin{aligned} {{\mathcal {A}}}_2:=\left\{ H_R\;:\;R \;\mathrm {is\ a\ compact\ edge\ of\ }\text {trunc}(\Delta ,k)\; \mathrm {of\ inclination\ bigger\ than \ }\tfrac{m_l}{n_l}\right\} . \end{aligned}\end{aligned}$$

The complement of the solutions of the polynomial defined as the product of all elements of \({{\mathcal {A}}}_1 \cup {{\mathcal {A}}}_2\) is a non-empty open Zariski set in the target of \(\Phi \) and its preimage by \(\Phi \) is a non-empty open Zariski set in the source of \(\Phi \). Hence there is a non-empty open Zariski set in the space of coefficients of the Puiseux root \(\alpha (x)\) of \(f\in K(n,b_1,\ldots ,b_g)\) such that

$$\begin{aligned} {\mathcal {N}}\left( \tfrac{\partial ^k {{\hat{f}}}}{\partial y^k}\right) = \textrm{trunc}(\Delta ,k) \end{aligned}$$

and \(\frac{\partial ^k {{\hat{f}}}}{\partial y^k}\) is non-degenerate on all edges of its Newton diagram which inclinations are bigger than \(m_l/n_l\). This last non-empty open Zariski is the complement of the solutions of a polynomial depending on a finite number of coefficients of \(\alpha \), let us say \(a_{s_1},\ldots , a_{s_{\ell }}\); and we denote this polynomial by \(G(a_{s_1},\ldots , a_{s_{\ell }})\). Consider now the polynomial \(\overline{G}=\prod _{\epsilon \in {\mathbb {U}}_n}G(\epsilon ^{s_1}a_{s_1},\ldots , \epsilon ^{s_{\ell }}a_{s_{\ell }})\). By [[8][67], Theorem 3], there exists a finite set of coefficients of *f*, let us say \(a_{u_1v_1},\ldots , a_{u_Iv_I}\) and a polynomial \(W\in \mathbb C[T_1, \ldots , T_I]\) such that \(W(a_{u_1v_1},\ldots , a_{u_Iv_I})=0\) if and only if \({{\overline{G}}}(a_{s_1},\ldots , a_{s_{\ell }})=0\). We conclude that if *f*is a generic element in \(K(n,b_1,\ldots , b_h)\), that is \(W(a_{u_1v_1},\ldots , a_{u_Iv_I})\ne 0\), then \(G(a_{s_1},\ldots , a_{s_{\ell }})\ne 0\) and the lemma follows. \(\square \)

## 4 Proof of the Main Theorem

In this section we will prove Theorem [1.3][29]. Let *f*be a generic member of \(K(b_0,\ldots ,b_h)\). Remember that \(e_i=\gcd (b_0,\ldots ,b_i)\), for \(0\le i\le h\) and \(n_i=\frac{e_{i-1}}{e_i}\), \(m_i=\frac{b_i}{e_i}\), for \(1\le i\le h\). Fix \(1\le k < b_0\) and let \(\ell \in \{1,\ldots , h\}\) be such that \(e_{\ell -1}>k\). Let \(\alpha \) be any Newton-Puiseux root of *f*.

Denote the sum of all terms of \(\alpha \) of degree strictly less than \(\frac{b_{\ell }}{b_0}\) by \(\lambda _{\ell }\) and let \(f_{\ell }(y)\) be the minimal polynomial of \(\lambda _{\ell }\) in \({\mathbb {C}}[[x]][y]\). The degree of \(f_{\ell }(y)\) equals \(n_1\cdots n_{\ell -1}\). Let \(\frac{\partial ^k f}{\partial y^k}=g_1\cdots g_r\) be the factorization into irreducible factors of the *k*th derivative of *f*. Put \(\Gamma ^{(\ell )}:=\prod _jg_j\) where the product runs over the factors \(g_j\) such that \({\textrm{cont}}(g_j,f)=\frac{b_{\ell }}{b_0}\). According to [[7][32], Theorem 6.2 ] we have that \(\frac{\partial ^{k}f}{\partial y^k}=\Gamma ^{(1)}\cdots \Gamma ^{(i_{k})}\) which proves item (1) of the theorem.

We can write \(\Gamma ^{(\ell )}=\Gamma ^{(\ell )}_1\Gamma ^{(\ell )}_2\) verifying \({\textrm{cont}}(g,f_{\ell })> \frac{b_{\ell }}{b_0}\) for any irreducible factor *g*of \(\Gamma ^{(\ell )}_{1}\) and \({\textrm{cont}}(g,f_{\ell })=\frac{b_{\ell }}{b_0}\) for any irreducible factor *g*of \(\Gamma ^{(\ell )}_{2}\). Remark that the factors \(\Gamma ^{(\ell )}_{1}\) and \(\Gamma ^{(\ell )}_{2}\) coincide with those given in [[7][32], Theorem 6.2 ].

After [[7][32], Theorem 6.2 (v), (ii)] \(\Gamma ^{(\ell )}_{2}=\prod _{i=1}^{m}w^{(\ell )}_i\) where \(m=\min \{e_{\ell }, k\}-\lceil \frac{k}{n_{\ell }}\rceil \) and the set of characteristic exponents of its irreducible factors \(w^{(\ell )}_i\) is \(\left\{ \frac{b_{1}}{b_{0}},\ldots , \frac{b_{\ell }}{b_{0}}\right\} \).

Since \(\frac{b_{\ell }}{b_{0}}\) is not in the support of \(\lambda _\ell \) we get \({\textrm{cont}}(f_\ell , w_i^{(\ell )})=b_\ell /b_0\) for \(1\le i\le m\), and statement (2*b*) follows.

On the other hand we get \(\widehat{\frac{\partial ^k f}{\partial y^k}}=\frac{\partial ^k {\hat{f}}}{\partial y^k}\), so by Lemma [3.5][68], where the inclinations of the compact edges of *L*are less than or equal to \(\frac{m_\ell }{n_\ell }\). Moreover \(\widehat{\frac{\partial ^k f}{\partial y^k}}\) is non-degenerate on all edges of its Newton diagram which inclinations are bigger than \(m_l/n_l\).

Now applying Corollary [3.2][69] to \(\lambda =\lambda _{\ell }\), which characteristic is \(\left( \frac{b_{0}}{e_{\ell -1}},\frac{b_{1}}{e_{\ell -1}},\ldots , \frac{b_{\ell -1}}{e_{\ell -1}}\right) \), \(g=f_l\), \(v=\frac{\partial ^k f}{\partial y^k}\) and \(q=\frac{m_\ell }{n_\ell }\), we get that \(\Gamma _1^{(\ell )}\) can be written as \(\prod _{j=1}^{r}z^{(\ell )}_j\) with \(z^{(\ell )}_j\) irreducible verifying statements (2*a*) and (2*c*) of the theorem.

In order to prove the statement (2*c*) in full generality it is sufficient to show that

$$\begin{aligned} {\textrm{cont}}(w_i^{(\ell )},w_j^{(\ell )})=\tfrac{b_\ell }{b_0} \;\;\;\; \textrm{for}\ 1\le i<j\le m. \end{aligned}$$

Suppose that \({\textrm{cont}}(w_i^{(\ell )},w_j^{(\ell )})>\frac{b_\ell }{b_0}\) for some \(i,j\in \{1,\ldots ,m\}\), \(i\ne j\). Then there is a nonzero complex number *u*and a Newton-Puiseux root \(\gamma _d\) of \(w_d^{(\ell )}\) such that \(\gamma _d=\lambda _\ell +ux^{b_\ell /b_0}+\cdots \), for \(d=i,j\). We claim that *u*is not a root of the univariate polynomial \(y^{n_\ell }-a_{b_\ell }^{n_\ell }\). Indeed suppose that \(u=\tau ^{n_\ell }a_{b_\ell }\) for some \(n_\ell \) -th root of unity \(\tau \). Let \(\varepsilon \) be an \(e_{\ell -1}\) -th root of the unity such that \(\tau =\varepsilon ^{b_\ell }\). Then the Newton-Puiseux root \(\alpha _{\varepsilon }\) of *f*has the form \(\alpha _{\varepsilon }=\lambda _\ell +\varepsilon ^{b_\ell }a_{b_\ell }x^{b_\ell /b_0}+\cdots =\lambda _\ell +ux^{b_\ell /b_0}+\cdots \), hence \({\textrm{ord}}(\alpha _\varepsilon -w_d^{(\ell )})>b_l/b_0\) which is a contradiction since \({\textrm{cont}}(f,w_d^{(\ell )})=b_l/b_0\) and we finished the proof of the claim.

Observe that \(\tilde{\gamma }_d:=\gamma _d(x^{n/e_{\ell -1}})-\lambda _\ell (x^{n/e_{\ell -1}})=ux^{m_\ell /n_l}+\cdots \) are Newton-Puiseux roots of \(\frac{\partial ^k {{\hat{f}}}}{\partial y^k}\), for \(d=i,j\).

Let \(F(y):={\textrm{in}}_\omega {{\hat{f}}}(x,y)\vert _{x=1}\) (see ( [12][70])). Hence we get \( \tfrac{d^kF}{dy^k}={\textrm{in}}_\omega \left( \tfrac{\partial ^k {{\hat{f}}}(x,y)}{\partial y^k}\right) _{\vert _{x=1}}. \) Given that \((y-ux^{m_\ell /n_\ell })^2\) is a factor of \({\textrm{in}}_\omega \left( \tfrac{\partial ^k {{\hat{f}}}(x,y)}{\partial y^k}\right) \) then \((y-u)^2\) is a factor of \( \tfrac{d^kF}{dy^k}\) which is a contradiction since \(\tfrac{d^kF}{dy^k}\) has no multiple complex roots except 0 and the roots of \(y^{n_\ell }-a_{b_\ell }^{n_\ell }\) (see [[7][32], Corollary 5.4]).The proof of Theorem [1.3][29] is finished.

### Example 4.1

Consider a generic element *f*of *K*(12, 16, 31). Then

$$\begin{aligned} \frac{\partial f}{\partial y}=\Gamma ^{(1)}\Gamma ^{(2)} \end{aligned}$$

where

$$\begin{aligned} {\textrm{cont}}(f,v)=\left\{ \begin{array}{ll} \frac{4}{3} & \mathrm{for\ any\ irreducible\ factor}\ v\ \textrm{of}\ \Gamma ^{(1)}\\ & \\ \frac{31}{12} & \mathrm{for\ any\ irreducible\ factor}\ v\ \textrm{of}\ \Gamma ^{(2)}.\\ \end{array} \right. \end{aligned}$$

We have \((n_1,m_1)=(3,4)\) and \((n_2,m_2)=(4,31)\). The first symbolic derivatives of Newton diagrams , are , . Hence \(\Gamma ^{(1)}=z_1^{(1)}\) and \(\Gamma ^{(2)}=\prod _{j=1}^3 z_j^{(2)}\) where

-

\({\textrm{cont}}(f_1,z_1^{(1)})=\frac{3}{2}\) and \({\textrm{Char}}(z^{(1)}_1)=\left\{ \frac{3}{2} \right\} \),

-

\({\textrm{cont}}(f_2,z_j^{(2)})=\frac{8}{3}\) and \({\textrm{Char}}(z^{(2)}_j)=\left\{ \frac{4}{3} \right\} \), for \(j\in \{1,2,3\}\).

For the second polar we have \(\frac{\partial ^2 f}{\partial y^2}=\Gamma ^{(1)}\Gamma ^{(2)}\) where as before

$$\begin{aligned} {\textrm{cont}}(f,v)=\left\{ \begin{array}{ll} \frac{4}{3} & \mathrm{for\ any\ irreducible\ factor}\ v\ \textrm{of}\ \Gamma ^{(1)}\\ & \\ \frac{31}{12} & \mathrm{for\ any\ irreducible\ factor}\ v\ \textrm{of}\ \Gamma ^{(2)}.\\ \end{array} \right. \end{aligned}$$

Since , , we get in this case that \(\Gamma ^{(1)}=z_1^{(1)}w_1^{(1)}\) and \(\Gamma ^{(2)}=z_1^{(2)} z_2^{(2)}\) where

-

\({\textrm{cont}}(f_1,z_1^{(1)})=\frac{2}{1}\) and \({\textrm{Char}}(z^{(1)}_1)=\emptyset \), that is, \(z^{(1)}_1\) is smooth,

-

\({\textrm{cont}}(f_1,w_1^{(1)})=\frac{4}{3}\) and \({\textrm{Char}}(w^{(1)}_1)=\left\{ \frac{4}{3} \right\} \),

-

\({\textrm{cont}}(f_2,z_j^{(2)})=\frac{8}{3}\) and \({\textrm{Char}}(z^{(2)}_j)=\left\{ \frac{4}{3} \right\} \), for \(j\in \{1,2\}\).

Consider now \(g(x,y)\in K(12,16,31)\) which admits \(\alpha (x)=x^{4/3}+x^2+x^{31/12}\) as a Newton-Puiseux root. Applying a symbolic computation program **Maxima**we get \(g(x,y)=y^{12}-12x^{2}y^{11}+66x^{4}y^{10}+h(x,y)\), where \(\deg _yh(x,y)=9\). Hence \(\frac{\partial ^{10}g}{\partial y^{10}}=6\cdot 11!(y-x^2)^2\). However, after Theorem [1.3][29], for a generic element \(f\in K(12,16,31)\) we get, \(\frac{\partial ^{10}f}{\partial y^{10}}=\Gamma ^{(1)}=z_1^{(1)}\), with \({\textrm{Char}}(z^{(1)}_1)=\left\{ \frac{3}{2} \right\} \), \({\textrm{cont}}(f,z_1^{(1)})=\frac{4}{3}\) and \({\textrm{cont}}(f_1,z_1^{(1)})=\frac{3}{2}\). We conclude that *g*is not a generic element of *K*(12, 16, 31) in the sense of Theorem [1.3][29].,

### Example 4.2

Consider a generic element *f*of *K*(10, 14, 15). We have and . By Proposition [2.7][71] the first symbolic derivatives of these Newton diagrams are and .

We get

$$\begin{aligned} \frac{\partial f}{\partial y}=\Gamma ^{(1)}\Gamma ^{(2)}, \end{aligned}$$

where

$$\begin{aligned} {\textrm{cont}}(f,v)=\left\{ \begin{array}{ll} \frac{7}{5} & \mathrm{for\ any\ irreducible\ factor}\ v\ \textrm{of}\ \Gamma ^{(1)}\\ & \\ \frac{3}{2} & \mathrm{for\ any\ irreducible\ factor}\ v\ \textrm{of}\ \Gamma ^{(2)}.\\ \end{array} \right. \end{aligned}$$

Moreover \(\Gamma ^{(1)}=z_1^{(1)}z_2^{(1)}\) and \(\Gamma ^{(2)}= z_1^{(2)}\) where

-

\({\textrm{cont}}(f_1,z_j^{(1)})=\frac{3}{2}\) and \({\textrm{Char}}(z^{(1)}_j)=\left\{ \frac{3}{2} \right\} \), for \(j\in \{1,2\}\);

-

\({\textrm{cont}}(f_2,z_1^{(2)})=\frac{8}{5}\) and \({\textrm{Char}}(z^{(2)}_1)=\left\{ \frac{7}{5} \right\} \).

For the second polar we have \(\frac{\partial ^2 f}{\partial y^2}=\Gamma ^{(1)}\) where \({\textrm{cont}}(f,v)=\frac{7}{5}\) for any irreducible factor *v*of \(\Gamma ^{(1)}\).

**Fig. 7**

[image: Fig. 7]

[Full size image][72]

Eggers-Wall trees of Example [4.1][73]: on the left \(\Theta (ff_1f_2\frac{\partial f}{\partial y})\) and on the right \(\Theta (ff_1f_2\frac{\partial ^2 f}{\partial y^2})\)

**Fig. 8**

[image: Fig. 8]

[Full size image][74]

Eggers-Wall trees of Example [4.2][75]: on the left \(\Theta (ff_1f_2\frac{\partial f}{\partial y})\) and on the right \(\Theta (ff_1f_2\frac{\partial ^2 f}{\partial y^2})\)

In this case . Hence \(\Gamma ^{(1)}=z_1^{(1)}z_2^{(1)}w_1^{(1)}\) where

-

\({\textrm{cont}}(f_1,z_1^{(1)})=\frac{2}{1}\) and \(z^{(1)}_1\) is smooth,

-

\({\textrm{cont}}(f_1,z_2^{(1)})=\frac{3}{2}\) and \({\textrm{Char}}(z^{(1)}_2)=\{\frac{3}{2}\}\),

-

\({\textrm{cont}}(f_1,w_1^{(1)})=\frac{7}{5}\) and \({\textrm{Char}}(w^{(1)}_1)=\left\{ \frac{7}{5} \right\} \).

### Remark 4.3

Figures [7][76] and [8][77] illustrate Examples [4.1][73] and [4.2][75] using Eggers-Wall trees. Recall that the Eggers-Wall tree \(\Theta (h)\) of a reduced power series *h*(*x*, *y*) is a rooted tree with leaves corresponding to irreducible factors of *h*. For any two irreducible factors \(h_1,h_2\) of *h*the last common vertex of the paths from the root of \(\Theta (h)\) to \(h_1\) and from the root to \(h_2\) is labelled by the contact \({\textrm{cont}}(h_1,h_2)\). The Eggers-Wall tree \(\Theta (h)\) equipped with some additional information (weights of edges) characterizes the equisingularity class of *h*(*x*, *y*) (see [[14][78]] and [[6][79]]).

## Data Availibility

Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

## References

1.

Casas-Alvero, E.: On the singularities of polar curves. Manuscripta Math. **43**, 167–190 (1983)

[Article][80] [MathSciNet][81] [Google Scholar][82]

2.

Casas-Alvero, E.: Higher order polar germs. J. Algebra **240**, 326–337 (2001)

[Article][83] [MathSciNet][84] [MATH][85] [Google Scholar][86]

3.

Chenciner, A.: Courbes Algébriques Planes; Publications Mathématiques de l’Université Paris VII: Paris, France, 1978; p. 203

4.

Coxeter, H.S.M.: Introduction to Geometry. Wiley, New York (1969)

[MATH][87] [Google Scholar][88]

5.

Ewald, G.: Combinatorial Convexity and Algebraic Geometry. Springer, (1996)

6.

García Barroso, E.R., Pérez González, P., Popescu-Pampu, P.: The combinatorics of plane curve singularities. How Newton polygons blossom into lotuses. In Cisneros Molina J.L., Lê D.T., Seade J. (eds) Handbook of Geometry and Topology of Singularities I, Springer (2020), 1–150

7.

García Barroso, E.R., Gwoździewicz, J.: Decompositions of the higher order polars of plane branches. Forum Math. **29**(2), 357–367 (2017)

[Article][89] [MathSciNet][90] [MATH][91] [Google Scholar][92]

8.

Gryszka, B., Gwoździewicz, J.: On polynomials depending on coefficients of Puiseux parametrizations. J. Algebra **666**, 289–307 (2025)

[Article][93] [MathSciNet][94] [MATH][95] [Google Scholar][96]

9.

Hefez, A.: Irreducible Plane Curve Singularities, in Real and Complex Singularities, the sixth workshop at São Carlos, Marcel Dekker, 1-120 (2003)

10.

Hefez, A., Hernandes, M.E., Hernández Iglesias, M.F.: On the factorization of the polar of a plane branch. Singularities and foliations. geometry, topology and applications, 347-362, Springer Proc. Math. Stat., 222, Springer, Cham, (2018)

11.

Kouchnirenko, A.G.: Polyèdres de Newton et nombres de Milnor. Invent. Math. **32**, 1–31 (1976)

[Article][97] [MathSciNet][98] [Google Scholar][99]

12.

Teissier, B.: The hunting of invariants in the geometry of discriminants, in: Proc. Ninth Nordic Summer School, Oslo, 1976, 565-678 (1978)

13.

Teissier, B.: Continued fractions. JAMS Seminar at Yamaguchi, 1993. Accesible in [https://webusers.imj-prg.fr/~bernard.teissier/documents/Yamaguchi93.pdf][100]

14.

Wall, C.T.C.: Chains on the Eggers tree and polar curves. Rev. Mat. Iberoamericana **19**(2), 745–754 (2003)

[Article][101] [MathSciNet][102] [Google Scholar][103]

15.

Zariski, O.: The Moduli Problem for plane branches. University Lecture Series AMS. Volume 39. (2006)

[Download references][104]

## Funding

Open Access funding provided thanks to the CRUE-CSIC agreement with Springer Nature. The first two authors were partially supported by the Spanish grant PID2019-105896GB-I00 funded by MCIN/AEI/10.13039/501100011033.

## Author information

### Authors and Affiliations

1.

Departamento de Matemáticas, Estadística e Investigación Operativa, Instituto Universitario de Matemáticas y Aplicaciones (IMAULL), Universidad de La Laguna, Apartado de Correos 456, 38200, La Laguna, Tenerife, Spain

Evelia R. García Barroso

2.

Institute of Mathematics, University of the National Education Commission, Krakow, Podchora̧żych 2, PL 30-084, Cracow, Poland

Janusz Gwoździewicz

3.

Institute of Mathematics, Faculty of Exact and Natural Sciences, Jan Kochanowski University of Kielce, ul. Uniwersytecka 7, PL 25-406, Kielce, Poland

Mateusz Masternak

Authors

1. Evelia R. García Barroso

[View author publications][105]

Search author on: [PubMed][106] [Google Scholar][107]

2. Janusz Gwoździewicz

[View author publications][108]

Search author on: [PubMed][109] [Google Scholar][110]

3. Mateusz Masternak

[View author publications][111]

Search author on: [PubMed][112] [Google Scholar][113]

### Corresponding author

Correspondence to [Evelia R. García Barroso][114].

## Ethics declarations

### Conflict of interest

The authors have no relevant financial or non-financial interests to disclose.

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][115].

[Reprints and permissions][116]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [117]

### Cite this article

García Barroso, E.R., Gwoździewicz, J. & Masternak, M. On the Equisingularity Class of the General Higher Order Polars of Plane Branches. *Results Math***80**, 177 (2025). https://doi.org/10.1007/s00025-025-02486-3

[Download citation][118]

-

Received: 16 October 2024

-

Accepted: 18 July 2025

-

Published: 02 August 2025

-

Version of record: 02 August 2025

-

DOI: https://doi.org/10.1007/s00025-025-02486-3

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Irreducible plane curve][119]
- [higher order polar][120]
- [equisingularity class][121]

### Mathematics Subject Classification

- [Primary 32S05][122]
- [Secondary 32S15][123]

### Profiles

1. Evelia R. García Barroso [View author profile][124]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s00025-025-02486-3.pdf
[3]: /article/10.1007/s00025-025-02486-3/save-research?_csrf=DFOPLRSRkrefRUBqs1gvDcC9qeQP8rPP
[4]: /saved-research
[5]: /journal/25
[6]: /journal/25/aims-and-scope
[7]: https://www.editorialmanager.com/rima/
[8]: https://link.springer.com/10.1007/978-3-319-39339-1_8?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/978-3-319-73639-6_11?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s41478-023-00671-7?fromPaywallRec=false
[11]: /subjects/algebraic-geometry
[12]: /subjects/apicobasal-polarity
[13]: /subjects/basolateral-polarity
[14]: /subjects/polarization
[15]: /subjects/projective-geometry
[16]: /subjects/group-theory-and-generalizations
[17]: /subjects/algebraic-geometry-of-varieties-and-moduli-spaces
[18]: /article/10.1007/s00025-025-02486-3#ref-CR9
[19]: /article/10.1007/s00025-025-02486-3#Equ2
[20]: /article/10.1007/s00025-025-02486-3#ref-CR12
[21]: /article/10.1007/s00025-025-02486-3#Fig1
[22]: /article/10.1007/s00025-025-02486-3/figures/1
[23]: /article/10.1007/s00025-025-02486-3#Fig2
[24]: /article/10.1007/s00025-025-02486-3/figures/2
[25]: /article/10.1007/s00025-025-02486-3#ref-CR3
[26]: /article/10.1007/s00025-025-02486-3#ref-CR11
[27]: /article/10.1007/s00025-025-02486-3#Fig3
[28]: /article/10.1007/s00025-025-02486-3/figures/3
[29]: /article/10.1007/s00025-025-02486-3#FPar3
[30]: /article/10.1007/s00025-025-02486-3#Sec4
[31]: /article/10.1007/s00025-025-02486-3#ref-CR2
[32]: /article/10.1007/s00025-025-02486-3#ref-CR7
[33]: /article/10.1007/s00025-025-02486-3#ref-CR1
[34]: /article/10.1007/s00025-025-02486-3#ref-CR10
[35]: /article/10.1007/s00025-025-02486-3#ref-CR5
[36]: /article/10.1007/s00025-025-02486-3#Fig4
[37]: /article/10.1007/s00025-025-02486-3/figures/4
[38]: /article/10.1007/s00025-025-02486-3#Equ3
[39]: /article/10.1007/s00025-025-02486-3#FPar6
[40]: /article/10.1007/s00025-025-02486-3#FPar7
[41]: /article/10.1007/s00025-025-02486-3#Equ5
[42]: /article/10.1007/s00025-025-02486-3#Equ6
[43]: /article/10.1007/s00025-025-02486-3#ref-CR13
[44]: /article/10.1007/s00025-025-02486-3#FPar11
[45]: /article/10.1007/s00025-025-02486-3/figures/5
[46]: /article/10.1007/s00025-025-02486-3#Fig5
[47]: /article/10.1007/s00025-025-02486-3#Equ7
[48]: /article/10.1007/s00025-025-02486-3#ref-CR4
[49]: /article/10.1007/s00025-025-02486-3#Equ8
[50]: /article/10.1007/s00025-025-02486-3#FPar14
[51]: /article/10.1007/s00025-025-02486-3#FPar18
[52]: /article/10.1007/s00025-025-02486-3#ref-CR15
[53]: /article/10.1007/s00025-025-02486-3#FPar4
[54]: /article/10.1007/s00025-025-02486-3#FPar8
[55]: /article/10.1007/s00025-025-02486-3#Equ1
[56]: /article/10.1007/s00025-025-02486-3#Equ10
[57]: /article/10.1007/s00025-025-02486-3#FPar19
[58]: /article/10.1007/s00025-025-02486-3#Equ11
[59]: /article/10.1007/s00025-025-02486-3#Equ13
[60]: /article/10.1007/s00025-025-02486-3#Equ14
[61]: /article/10.1007/s00025-025-02486-3#Equ15
[62]: /article/10.1007/s00025-025-02486-3#Equ16
[63]: /article/10.1007/s00025-025-02486-3#Fig6
[64]: /article/10.1007/s00025-025-02486-3/figures/6
[65]: /article/10.1007/s00025-025-02486-3#Equ9
[66]: /article/10.1007/s00025-025-02486-3#Equ17
[67]: /article/10.1007/s00025-025-02486-3#ref-CR8
[68]: /article/10.1007/s00025-025-02486-3#FPar21
[69]: /article/10.1007/s00025-025-02486-3#FPar16
[70]: /article/10.1007/s00025-025-02486-3#Equ12
[71]: /article/10.1007/s00025-025-02486-3#FPar12
[72]: /article/10.1007/s00025-025-02486-3/figures/7
[73]: /article/10.1007/s00025-025-02486-3#FPar23
[74]: /article/10.1007/s00025-025-02486-3/figures/8
[75]: /article/10.1007/s00025-025-02486-3#FPar24
[76]: /article/10.1007/s00025-025-02486-3#Fig7
[77]: /article/10.1007/s00025-025-02486-3#Fig8
[78]: /article/10.1007/s00025-025-02486-3#ref-CR14
[79]: /article/10.1007/s00025-025-02486-3#ref-CR6
[80]: https://link.springer.com/doi/10.1007/BF01165829
[81]: http://www.ams.org/mathscinet-getitem?mr=707043
[82]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20singularities%20of%20polar%20curves&amp;journal=Manuscripta%20Math.&amp;doi=10.1007%2FBF01165829&amp;volume=43&amp;pages=167-190&amp;publication_year=1983&amp;author=Casas-Alvero%2CE
[83]: https://doi.org/10.1006%2Fjabr.2000.8727
[84]: http://www.ams.org/mathscinet-getitem?mr=1830556
[85]: http://www.emis.de/MATH-item?0985.14012
[86]: http://scholar.google.com/scholar_lookup?amp;title=Higher%20order%20polar%20germs&amp;journal=J.%20Algebra&amp;doi=10.1006%2Fjabr.2000.8727&amp;volume=240&amp;pages=326-337&amp;publication_year=2001&amp;author=Casas-Alvero%2CE
[87]: http://www.emis.de/MATH-item?0181.48101
[88]: http://scholar.google.com/scholar_lookup?amp;title=Introduction%20to%20Geometry&amp;publication_year=1969&amp;author=Coxeter%2CHSM
[89]: https://doi.org/10.1515%2Fforum-2016-0049
[90]: http://www.ams.org/mathscinet-getitem?mr=3619118
[91]: http://www.emis.de/MATH-item?1364.32021
[92]: http://scholar.google.com/scholar_lookup?amp;title=Decompositions%20of%20the%20higher%20order%20polars%20of%20plane%20branches&amp;journal=Forum%20Math.&amp;doi=10.1515%2Fforum-2016-0049&amp;volume=29&amp;issue=2&amp;pages=357-367&amp;publication_year=2017&amp;author=Garc%C3%ADa%20Barroso%2CER&amp;author=Gwo%C5%BAdziewicz%2CJ
[93]: https://doi.org/10.1016%2Fj.jalgebra.2024.11.024
[94]: http://www.ams.org/mathscinet-getitem?mr=4837802
[95]: http://www.emis.de/MATH-item?1558.32049
[96]: http://scholar.google.com/scholar_lookup?amp;title=On%20polynomials%20depending%20on%20coefficients%20of%20Puiseux%20parametrizations&amp;journal=J.%20Algebra&amp;doi=10.1016%2Fj.jalgebra.2024.11.024&amp;volume=666&amp;pages=289-307&amp;publication_year=2025&amp;author=Gryszka%2CB&amp;author=Gwo%C5%BAdziewicz%2CJ
[97]: https://link.springer.com/doi/10.1007/BF01389769
[98]: http://www.ams.org/mathscinet-getitem?mr=419433
[99]: http://scholar.google.com/scholar_lookup?amp;title=Poly%C3%A8dres%20de%20Newton%20et%20nombres%20de%20Milnor&amp;journal=Invent.%20Math.&amp;doi=10.1007%2FBF01389769&amp;volume=32&amp;pages=1-31&amp;publication_year=1976&amp;author=Kouchnirenko%2CAG
[100]: https://webusers.imj-prg.fr/%7ebernard.teissier/documents/Yamaguchi93.pdf
[101]: https://doi.org/10.4171%2Frmi%2F367
[102]: http://www.ams.org/mathscinet-getitem?mr=2023205
[103]: http://scholar.google.com/scholar_lookup?amp;title=Chains%20on%20the%20Eggers%20tree%20and%20polar%20curves&amp;journal=Rev.%20Mat.%20Iberoamericana&amp;doi=10.4171%2Frmi%2F367&amp;volume=19&amp;issue=2&amp;pages=745-754&amp;publication_year=2003&amp;author=Wall%2CCTC
[104]: https://citation-needed.springer.com/v2/references/10.1007/s00025-025-02486-3?format=refman&amp;flavour=references
[105]: /search?sortBy=newestFirst&amp;contributor=Evelia%20R.%20Garc%C3%ADa%20Barroso
[106]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Evelia%20R.%20Garc%C3%ADa%20Barroso
[107]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Evelia%20R.%20Garc%C3%ADa%20Barroso%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[108]: /search?sortBy=newestFirst&amp;contributor=Janusz%20Gwo%C5%BAdziewicz
[109]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Janusz%20Gwo%C5%BAdziewicz
[110]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Janusz%20Gwo%C5%BAdziewicz%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[111]: /search?sortBy=newestFirst&amp;contributor=Mateusz%20Masternak
[112]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Mateusz%20Masternak
[113]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Mateusz%20Masternak%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[114]: mailto:ergarcia@ull.es
[115]: http://creativecommons.org/licenses/by/4.0/
[116]: https://s100.copyright.com/AppDispatchServlet?title=On%20the%20Equisingularity%20Class%20of%20the%20General%20Higher%20Order%20Polars%20of%20Plane%20Branches&amp;author=Evelia%20R.%20Garc%C3%ADa%20Barroso%20et%20al&amp;contentID=10.1007%2Fs00025-025-02486-3&amp;copyright=The%20Author%28s%29&amp;publication=1422-6383&amp;publicationDate=2025-08-02&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[117]: https://crossmark.crossref.org/dialog/?doi=10.1007/s00025-025-02486-3
[118]: https://citation-needed.springer.com/v2/references/10.1007/s00025-025-02486-3?format=refman&amp;flavour=citation
[119]: /search?query=Irreducible%20plane%20curve&amp;facet-discipline=#34;Mathematics&#34;
[120]: /search?query=higher%20order%20polar&amp;facet-discipline=#34;Mathematics&#34;
[121]: /search?query=equisingularity%20class&amp;facet-discipline=#34;Mathematics&#34;
[122]: /search?query=Primary%2032S05&amp;facet-discipline=#34;Mathematics&#34;
[123]: /search?query=Secondary%2032S15&amp;facet-discipline=#34;Mathematics&#34;
[124]: /researchers/41076569SN
