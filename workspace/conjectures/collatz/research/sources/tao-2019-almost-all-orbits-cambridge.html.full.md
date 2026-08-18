<!-- source: https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F | converted from HTML -->

Almost all orbits of the Collatz map attain almost bounded values | Forum of Mathematics, Pi | Cambridge Core

[Logo for Cambridge Core from Cambridge University Press. Click to return to homepage.][1]

Search

[Logo for Cambridge Core from Cambridge University Press. Click to return to homepage.][1]

---

Institution Login

Search

Hostname: page-component-5d84bcc8dc-t9h4t Total loading time: 0 Render date: 2026-08-18T09:40:09.164Z Has data issue: false hasContentIssue false

- [Home][2]
- > [Journals][3]
- > [Forum of Mathematics, Pi][4]
- > [Volume 10][5]
- > Almost all orbits of the Collatz map attain almost...

- English
- Français

[Forum of Mathematics, Pi][4]

---

## Article contents

- Abstract
-

Introduction

-

Notation and preliminaries

-

Reduction to stabilisation of first passage

-

$3$ -adic distribution of iterates

-

Reduction to fine-scale mixing of the n -Syracuse offset map

-

Reduction to Fourier decay bound

-

Decay of Fourier coefficients

-

Conflicts of interest

-

Financial support

- Footnotes
- References

# Almost all orbits of the Collatz map attain almost bounded values

Part of: [Arithmetic and non-Archimedean dynamical systems][6]

Published online by Cambridge University Press: **20 May 2022**

[Terence Tao][7][image: Open the ORCID record for Terence Tao] [[Opens in a new window]][8]

Show author details

---

Terence Tao*Affiliation:

University of California, Los Angeles, 405 Hilgard Ave, 90095 Los Angeles, CA, USA

*

E-mail: [tao@math.ucla.edu][9]

---

- Article
- Figures
- Metrics

Article contents

- Abstract
- Introduction
- Notation and preliminaries
- Reduction to stabilisation of first passage
- $3$-adic distribution of iterates
- Reduction to fine-scale mixing of the n-Syracuse offset map
- Reduction to Fourier decay bound
- Decay of Fourier coefficients
- Conflicts of interest
- Financial support
- Footnotes
- References

Save PDF

[Save PDF (0.82 mb)][10] [View PDF [Opens in a new window]][10] Save to Dropbox Save to Google Drive Save to Kindle

Share

Cite

---

## Abstract

Define the *Collatz map*${\operatorname {Col}} \colon \mathbb {N}+1 \to \mathbb {N}+1$ on the positive integers $\mathbb {N}+1 = \{1,2,3,\dots \}$ by setting ${\operatorname {Col}}(N)$ equal to $3N+1$ when *N*is odd and $N/2$ when *N*is even, and let ${\operatorname {Col}}_{\min }(N) := \inf _{n \in \mathbb {N}} {\operatorname {Col}}^n(N)$ denote the minimal element of the Collatz orbit $N, {\operatorname {Col}}(N), {\operatorname {Col}}^2(N), \dots $. The infamous *Collatz conjecture*asserts that ${\operatorname {Col}}_{\min }(N)=1$ for all $N \in \mathbb {N}+1$. Previously, it was shown by Korec that for any $\theta> \frac {\log 3}{\log 4} \approx 0.7924$, one has ${\operatorname {Col}}_{\min }(N) \leq N^\theta $ for almost all $N \in \mathbb {N}+1$ (in the sense of natural density). In this paper, we show that for *any*function $f \colon \mathbb {N}+1 \to \mathbb {R}$ with $\lim _{N \to \infty } f(N)=+\infty $, one has ${\operatorname {Col}}_{\min }(N) \leq f(N)$ for almost all $N \in \mathbb {N}+1$ (in the sense of logarithmic density). Our proof proceeds by establishing a stabilisation property for a certain first passage random variable associated with the Collatz iteration (or more precisely, the closely related Syracuse iteration), which in turn follows from estimation of the characteristic function of a certain skew random walk on a $3$ -adic cyclic group $\mathbb {Z}/3^n\mathbb {Z}$ at high frequencies. This estimation is achieved by studying how a certain two-dimensional renewal process interacts with a union of triangles associated to a given frequency.

---

## Keywords

[Collatz conjecture][11]

---

## MSC classification

Primary: [37P99: None of the above, but in this section][12]

---

## Information

Type Number Theory

Information

[Forum of Mathematics, Pi][4], [Volume 10][5], 2022, e12

DOI: [https://doi.org/10.1017/fmp.2022.8 [Opens in a new window]][13]

[image: Check for updates]

Creative Commons

[image: Creative Common License - CC][image: Creative Common License - BY]

This is an Open Access article, distributed under the terms of the Creative Commons Attribution licence ( [https://creativecommons.org/licenses/by/4.0/][14]), which permits unrestricted re-use, distribution, and reproduction in any medium, provided the original work is properly cited.

Copyright

© The Author(s), 2022. Published by Cambridge University Press

---

## 1 Introduction

### 1.1 Statement of main result

Let $\mathbb {N} := \{0,1,2,\dots \}$ denote the natural numbers, so that $\mathbb {N}+1 = \{1,2,3,\dots \}$ are the positive integers. The *Collatz map*${\operatorname {Col}} \colon \mathbb {N}+1 \to \mathbb {N}+1$ is defined by setting ${\operatorname {Col}}(N) := 3N+1$ when *N*is odd and ${\operatorname {Col}}(N) := N/2$ when *N*is even. For any $N \in \mathbb {N}+1$ , let ${\operatorname {Col}}_{\min }(N) := \min {\operatorname {Col}}^{\mathbb {N}}(N) = \inf _{n \in \mathbb {N}} {\operatorname {Col}}^n(N)$ denote the minimal element of the Collatz orbit ${\operatorname {Col}}^{\mathbb {N}}(N) := \{ N, {\operatorname {Col}}(N), {\operatorname {Col}}^2(N), \dots \}$ . We have the infamous *Collatz conjecture*(also known as the $3x+1$ conjecture):

#### Conjecture 1.1 (Collatz conjecture)

We have ${\operatorname {Col}}_{\min }(N)=1$ for all $N \in \mathbb {N}+1$ .

We refer the reader to [Reference Lagarias 14], [Reference Chamberland 6] for extensive surveys and historical discussion of this conjecture.

While the full resolution of Conjecture 1.1 remains well beyond the reach of current methods, some partial results are known. Numerical computation has verified ${\operatorname {Col}}_{\min }(N)=1$ for all $N \leq 5.78 \times 10^{18}$ [Reference Oliveira e Silva 17], for all $N \leq 10^{20}$ [Reference Roosendaal 18], and most recently for all $N \leq 2^{68} \approx 2.95 \times 10^{20}$ [Reference Barina 3], while Krasikov and Lagarias [Reference Krasikov and Lagarias 13] showed that

$$ \begin{align*}\# \{ N \in \mathbb{N}+1 \cap [1,x]: {\operatorname{Col}}_{\min}(N) = 1 \} \gg x^{0.84}\end{align*} $$

for all sufficiently large *x*, where $\# E$ denotes the cardinality of a finite set *E*, and our conventions for asymptotic notation are set out in Section 2. In this paper, we will focus on a different type of partial result, in which one establishes upper bounds on the minimal orbit value ${\operatorname {Col}}_{\min }(N)$ for ‘almost all’ $N \in \mathbb {N}+1$ . For technical reasons, the notion of ‘almost all’ that we will use here is based on logarithmic density, which has better approximate multiplicative invariance properties than the more familiar notion of natural density (see [Reference Tao 20] for a related phenomenon in a more number-theoretic context). Due to the highly probabilistic nature of the arguments in this paper, we will define logarithmic density using the language of probability theory.

#### Definition 1.2 (Almost all)

Given a finite non-empty subset *R*of $\mathbb {N}+1$ , we define Footnote 1 $\mathbf {Log}(R)$ to be a random variable taking values in *R*with the logarithmically uniform distribution

$$ \begin{align*}\mathbb{P}( \mathbf{Log}(R) \in A ) = \frac{\sum_{N \in A \cap R} \frac{1}{N}}{\sum_{N \in R} \frac{1}{N}}\end{align*} $$

for all $A \subset \mathbb {N}+1$ . The *logarithmic density*of a set $A \subset \mathbb {N}+1$ is then defined to be $\lim _{x \to \infty } \mathbb {P}( \mathbf {Log}(\mathbb {N}+1 \cap [1,x]) \in A )$ , provided that the limit exists. We say that a property $P(N)$ holds for *almost all*$N \in \mathbb {N}+1$ if $P(N)$ holds for *N*in a subset of $\mathbb {N}+1$ of logarithmic density $1$ , or equivalently if

$$ \begin{align*}\lim_{x \to \infty} \mathbb{P}( P( \mathbf{Log}( \mathbb{N}+1 \cap [1,x] ) ) ) = 1.\end{align*} $$

In Terras [Reference Terras 21] (and independently Everett [Reference Everett 8]), it was shown that ${\operatorname {Col}}_{\min }(N) < N$ for almost all *N*. This was improved by Allouche [Reference Allouche 1] to ${\operatorname {Col}}_{\min }(N) < N^\theta $ for almost all *N*, and any fixed constant $\theta>\frac {3}{2} - \frac {\log 3}{\log 2} \approx 0.869$ ; the range of $\theta $ was later extended to $\theta> \frac {\log 3}{\log 4} \approx 0.7924$ by Korec [Reference Korec 9]. (Indeed, in these results one can use natural density instead of logarithmic density to define ‘almost all’.) It is tempting to try to iterate these results to lower the value of $\theta $ further. However, one runs into the difficulty that the uniform (or logarithmic) measure does not enjoy any invariance properties with respect to the Collatz map: in particular, even if it is true that ${\operatorname {Col}}_{\min }(N) < x^\theta $ for almost all $N \in [1,x]$ , and ${\operatorname {Col}}_{\min }(N') \leq x^{\theta ^2}$ for almost all $N' \in [1, x^\theta ]$ , the two claims cannot be immediately concatenated to imply that ${\operatorname {Col}}_{\min }(N) \leq x^{\theta ^2}$ for almost all $N \in [1,x]$ , since the Collatz iteration may send almost all of $[1,x]$ into a very sparse subset of $[1,x^\theta ]$ , and in particular into the exceptional set of the latter claim ${\operatorname {Col}}_{\min }(N') \leq x^{\theta ^2}$ .

Nevertheless, in this paper, we show that it is possible to locate an alternate probability measure (or, more precisely, a family of probability measures) on the natural numbers with enough invariance properties that an iterative argument does become fruitful. More precisely, the main result of this paper is the following improvement of these ‘almost all’ results.

#### Theorem 1.3 (Almost all Collatz orbits attain almost bounded values)

Let $f \colon \mathbb {N} + 1 \to \mathbb {R}$ be any function with $\lim _{N \to \infty } f(N) = +\infty $ . Then one has ${\operatorname {Col}}_{\min }(N) < f(N)$ for almost all $N \in \mathbb {N}+1$ (in the sense of logarithmic density).

Thus, for instance, one has ${\operatorname {Col}}_{\min }(N) < \log \log \log \log N$ for almost all *N*.

Remark 1.4. One could ask whether it is possible to sharpen the conclusion of Theorem 1.3 further, to assert that there is an absolute constant $C_0$ such that ${\operatorname {Col}}_{\min }(N) \leq C_0$ for almost all $N \in \mathbb {N}+1$ . However, this question is likely to be almost as hard to settle as the full Collatz conjecture and out of reach of the methods of this paper. Indeed, suppose for any given $C_0$ that there existed an orbit ${\operatorname {Col}}^{\mathbb {N}}(N_0) = \{N_0, {\operatorname {Col}}(N_0), {\operatorname {Col}}^2(N_0),\dots \}$ that never dropped below $C_0$ (this is the case if there are infinitely many periodic orbits, or if there is at least one unbounded orbit). Then probabilistic heuristics (such as equation ( 1.16) below) suggest that for a positive density set of $N \in \mathbb {N}+1$ , the orbit ${\operatorname {Col}}^{\mathbb {N}}(N) = \{N, {\operatorname {Col}}(N), {\operatorname {Col}}^2(N), \dots \}$ should encounter one of the elements ${\operatorname {Col}}^n(N_0)$ of the orbit of $N_0$ before going below $C_0$ , and then the orbit of *N*will never dip below $C_0$ . However, Theorem 1.3 is easily seen Footnote 2 to be equivalent to the assertion that for any $\delta>0$ , there exists a constant $C_\delta $ such that ${\operatorname {Col}}_{\min }(N) \leq C_\delta $ for all *N*in a subset of $\mathbb {N}+1$ of lower logarithmic density (in which the limit in the definition of logarithmic density is replaced by the limit inferior) at least $1-\delta $ ; in fact, (see Theorem 3.1), our arguments give a constant of the form $C_\delta \ll \exp (\delta ^{-O(1)})$ , and it may be possible to refine the subset so that the logarithmic density (as opposed to merely the lower logarithmic density) exists and is at least $1-\delta $ . In particular, Footnote 3 it is possible in principle that a sufficiently explicit version of the arguments here, when combined with numerical verification of the Collatz conjecture, can be used to show that the Collatz conjecture holds for a set of *N*of positive logarithmic density. Also, it is plausible that some refinement of the arguments below will allow one to replace logarithmic density with natural density in the definition of ‘almost all’.

### 1.2 Syracuse formulation

We now discuss the methods of proof of Theorem 1.3. It is convenient to replace the Collatz map ${\operatorname {Col}} \colon \mathbb {N}+1 \to \mathbb {N}+1$ with a slightly more tractable acceleration $N \mapsto {\operatorname {Col}}^{f(N)}(N)$ of that map. One common instance of such an acceleration in the literature is the map ${\operatorname {Col}}_2 \colon \mathbb {N}+1 \to \mathbb {N}+1$ , defined by setting ${\operatorname {Col}}_2(N) := {\operatorname {Col}}^2(N) = \frac {3N+1}{2}$ when *N*is odd and ${\operatorname {Col}}_2(N) := \frac {N}{2}$ when *N*is even. Each iterate of the map ${\operatorname {Col}}_2$ performs exactly one division by $2$ , and for this reason ${\operatorname {Col}}_2$ is a particularly convenient choice of map when performing ‘ $2$ -adic’ analysis of the Collatz iteration. It is easy to see that ${\operatorname {Col}}_{\min }(N) = ({\operatorname {Col}}_2)_{\min }(N)$ for all $N \in \mathbb {N}+1$ , so all the results in this paper concerning ${\operatorname {Col}}$ may be equivalently reformulated using ${\operatorname {Col}}_2$ . The triple iterate ${\operatorname {Col}}^3$ was also recently proposed as an acceleration in [Reference Carletti and Fanelli 5]. However, the methods in this paper will rely instead on ‘ $3$ -adic’ analysis, and it will be preferable to use an acceleration of the Collatz map (first appearing to the author’s knowledge in [Reference Crandall 7]), which performs exactly one multiplication by $3$ per iteration. More precisely, let $2\mathbb {N}+1 = \{1,3,5,\dots \}$ denote the odd natural numbers, and define the *Syracuse map*${\operatorname {Syr}} \colon 2\mathbb {N}+1 \to 2\mathbb {N}+1$ (OEIS A075677) to be the largest odd number dividing $3N+1$ ; thus, for instance,

$$ \begin{align*}{\operatorname{Syr}}(1)=1; \quad {\operatorname{Syr}}(3) = 5; \quad {\operatorname{Syr}}(5) = 1; \quad {\operatorname{Syr}}(7) = 11.\end{align*} $$

Equivalently, one can write

(1.1) $$ \begin{align} {\operatorname{Syr}}(N) = {\operatorname{Col}}^{\nu_2(3N+1)+1}(N) = {\operatorname{Aff}}_{\nu_2(3N+1)}(N), \end{align} $$

where for each positive integer $a \in \mathbb {N}+1$ , ${\operatorname {Aff}}_a\colon \mathbb {R} \to \mathbb {R}$ denotes the affine map

$$ \begin{align*}{\operatorname{Aff}}_a(x) := \frac{3x+1}{2^a}\end{align*} $$

and for each integer *M*and each prime *p*, the *p-valuation*$\nu _p(M)$ of *M*is defined as the largest natural number *a*such that $p^a$ divides *M*(with the convention $\nu _p(0) = +\infty $ ). (Note that $\nu _2(3N+1)$ is always a positive integer when *N*is odd.) For any $N \in 2\mathbb {N}+1$ , let ${\operatorname {Syr}}_{\min }(N) := \min {\operatorname {Syr}}^{\mathbb {N}}(N)$ be the minimal element of the Syracuse orbit

$$ \begin{align*}{\operatorname{Syr}}^{\mathbb{N}}(N) := \{ N, {\operatorname{Syr}}(N), {\operatorname{Syr}}^2(N), \dots\}.\end{align*} $$

This Syracuse orbit ${\operatorname {Syr}}^{\mathbb {N}}(N)$ is nothing more than the odd elements of the corresponding Collatz orbit ${\operatorname {Col}}^{\mathbb {N}}(N)$ , and from this observation it is easy to verify the identity

(1.2) $$ \begin{align} {\operatorname{Col}}_{\min}(N) = {\operatorname{Syr}}_{\min}( N / 2^{\nu_2(N)} ) \end{align} $$

for any $N \in \mathbb {N}+1$ . Thus, the Collatz conjecture can be equivalently rephrased as

#### Conjecture 1.5 (Collatz conjecture, Syracuse formulation)

We have ${\operatorname {Syr}}_{\min }(N)=1$ for all $N \in 2\mathbb {N}+1$ .

We may similarly reformulate Theorem 1.3 in terms of the Syracuse map. We say that a property $P(N)$ holds for *almost all*$N \in 2\mathbb {N}+1$ if

$$ \begin{align*}\lim_{x \to \infty} \mathbb{P}( P(\mathbf{Log}( 2\mathbb{N}+1 \cap [1,x] ) ) )= 1,\end{align*} $$

or equivalently if $P(N)$ holds for a set of odd natural numbers of logarithmic density $1/2$ . Theorem 1.3 is then equivalent to

#### Theorem 1.6 (Almost all Syracuse orbits attain almost bounded values)

Let $f\colon 2\mathbb {N} + 1 \to \mathbb {R}$ be a function with $\lim _{N \to \infty } f(N) = +\infty $ . Then one has ${\operatorname {Syr}}_{\min }(N) < f(N)$ for almost all $N \in 2\mathbb {N}+1$ .

Indeed, if Theorem 1.6 holds and $f\colon \mathbb {N} +1 \to \mathbb {R}$ is such that $\lim _{N \to \infty } f(N) = +\infty $ , then from equation ( 1.2), we see that for any $a \in \mathbb {N}$ , the set of $N \in \mathbb {N}+1$ with $\nu _2(N) = a$ and ${\operatorname {Col}}_{\min }( N ) = {\operatorname {Syr}}_{\min }(N/2^a) < f(N)$ has logarithmic density $2^{-a}$ . Summing over any finite range $0 \leq a \leq a_0$ , we obtain a set of logarithmic density $1 - 2^{-a_0}$ on which the claim ${\operatorname {Col}}_{\min }(N) < f(N)$ holds, and on sending $a_0$ to infinity one obtains Theorem 1.3. The converse implication (which we will not need) is also straightforward and left to the reader.

The iterates ${\operatorname {Syr}}^n$ of the Syracuse map can be described explicitly as follows. For any finite tuple $\vec a = (a_1,\dots ,a_n) \in (\mathbb {N}+1)^n$ of positive integers, we define the composition ${\operatorname {Aff}}_{\vec a} = {\operatorname {Aff}}_{a_1,\dots ,a_n}\colon \mathbb {R} \to \mathbb {R}$ to be the affine map

$$ \begin{align*}{\operatorname{Aff}}_{a_1,\dots,a_n}(x) := {\operatorname{Aff}}_{a_n}( {\operatorname{Aff}}_{a_{n-1}}( \dots ({\operatorname{Aff}}_{a_1}(x)) \dots )).\end{align*} $$

A brief calculation shows that

(1.3) $$ \begin{align} {\operatorname{Aff}}_{a_1,\dots,a_n}(x) = 3^n 2^{-|\vec a|} x + F_n(\vec a), \end{align} $$

where the *size*$|\vec a|$ of a tuple $\vec a$ is defined as

(1.4) $$ \begin{align} |\vec a| := a_1 + \dots + a_n, \end{align} $$

and we define the *n-Syracuse offset map*$F_n\colon (\mathbb {N}+1)^n \to \mathbb {Z}[\frac {1}{2}]$ to be the function

(1.5) $$ \begin{align} F_n(\vec a) &:= \sum_{m=1}^n 3^{n-m} 2^{-a_{[m,n]}} \nonumber\\ &= 3^{n-1} 2^{-a_{[1,n]}} + 3^{n-2} 2^{-a_{[2,n]}} + \dots + 3^1 2^{-a_{[n-1,n]}} + 2^{-a_n}, \end{align} $$

where we adopt the summation notation

(1.6) $$ \begin{align} a_{[j,k]} := \sum_{i=j}^k a_i \end{align} $$

for any $1 \leq j \leq k \leq n$ ; thus, for instance, $|\vec a| = a_{[1,n]}$ . The *n*-Syracuse offset map $F_n$ takes values in the ring $\mathbb {Z}[\frac {1}{2}] := \{ \frac {M}{2^a}: M \in \mathbb {Z}, a \in \mathbb {N} \}$ formed by adjoining $\frac {1}{2}$ to the integers.

By iterating equation ( 1.1) and then using equation ( 1.3), we conclude that

(1.7) $$ \begin{align} {\operatorname{Syr}}^n(N) = {\operatorname{Aff}}_{\vec a^{(n)}(N)}(N) = 3^n 2^{-|\vec a^{(n)}(N)|} N + F_n(\vec a^{(n)}(N)) \end{align} $$

for any $N \in 2\mathbb {N}+1$ and $n \in \mathbb {N}$ , where we define *n-Syracuse valuation*$\vec a^{(n)}(N) \in (\mathbb {N}+1)^n$ of *N*to be the tuple

(1.8) $$ \begin{align} \vec a^{(n)}(N) := \left(\nu_2(3N+1), \nu_2(3{\operatorname{Syr}}(N)+1), \dots, \nu_2(3{\operatorname{Syr}}^{n-1}(N)+1)\right). \end{align} $$

This tuple is referred to as the *n-path*of *N*in [Reference Kontorovich and Sinai 12].

The identity in equation ( 1.7) asserts that ${\operatorname {Syr}}^n(N)$ is the image of *N*under a certain affine map ${\operatorname {Aff}}_{\vec a^{(n)}(N)}$ that is determined by the *n*-Syracuse valuation $\vec a^{(n)}(N)$ of *N*. This suggests that in order to understand the behaviour of the iterates ${\operatorname {Syr}}^n(N)$ of a typical large number *N*, one needs to understand the behaviour of *n*-Syracuse valuation $\vec a^{(n)}(N)$ , as well as the *n*-Syracuse offset map $F_n$ . For the former, we can gain heuristic insight by observing that for a positive integer *a*, the set of odd natural numbers $N \in 2\mathbb {N}+1$ with $\nu _2(3N+1)=a$ has (logarithmic) relative density $2^{-a}$ . To model this probabilistically, we introduce the following probability distribution:

#### Definition 1.7 (Geometric random variable)

If $\mu> 1$ , we use $\mathbf {Geom}(\mu )$ to denote a geometric random variable of mean $\mu $ , that is to say $\mathbf {Geom}(\mu )$ takes values in $\mathbb {N}+1$ with

$$ \begin{align*}\mathbb{P}( \mathbf{Geom}(\mu) = a ) = \frac{1}{\mu} \left( \frac{\mu-1}{\mu} \right)^{a-1}\end{align*} $$

for all $a \in \mathbb {N}+1$ . We use $\mathbf {Geom}(\mu )^n$ to denote a tuple of *n*independent, identically distributed (or *iid*for short) copies of $\mathbf {Geom}(\mu )$ , and use $\mathbf {X} \equiv \mathbf {Y}$ to denote the assertion that two random variables $\mathbf {X},\mathbf {Y}$ have the same distribution. Thus, for instance,

$$ \begin{align*}\mathbb{P}( \mathbf{a} = a ) = 2^{-a}\end{align*} $$

whenever $\mathbf {a} \equiv \mathbf {Geom}(2)$ and $a \in \mathbb {N}+1$ , and more generally

$$ \begin{align*}\mathbb{P}( \vec{\mathbf{a}} = \vec a ) = 2^{-|\vec a|}\end{align*} $$

whenever $\vec {\mathbf {a}} \equiv \mathbf {Geom}(2)^n$ and $\vec a \in (\mathbb {N}+1)^n$ for some $n \in \mathbb {N}$ .

In this paper, the only geometric random variables we will actually use are $\mathbf {Geom}(2)$ and $\mathbf {Geom}(4)$ .

We will then be guided by the following heuristic:

#### Heuristic 1.8 (Valuation heuristic)

If *N*is a ‘typical’ large odd natural number, and *n*is much smaller than $\log N$ , then the *n*-Syracuse valuation $\vec a^{(n)}(N)$ behaves like $\mathbf {Geom}(2)^n$ .

We can make this heuristic precise as follows. Given two random variables $\mathbf {X},\mathbf {Y}$ taking values in the same discrete space *R*, we define the *total variation*$d_{\operatorname {TV}}(\mathbf {X},\mathbf {Y})$ between the two variables to be the total variation of the difference in the probability measures; thus

(1.9) $$ \begin{align} d_{\operatorname{TV}}(\mathbf{X},\mathbf{Y}) := \sum_{r \in R} |\mathbb{P}( \mathbf{X} = r ) - \mathbb{P}( \mathbf{Y} = r )|. \end{align} $$

Note that

(1.10) $$ \begin{align} \sup_{E \subset R} |\mathbb{P}(\mathbf{X} \in E) - \mathbb{P}(\mathbf{Y} \in E)| \leq d_{\operatorname{TV}}(\mathbf{X},\mathbf{Y}) \leq 2 \sup_{E \subset R} |\mathbb{P}(\mathbf{X} \in E) - \mathbb{P}(\mathbf{Y} \in E)|. \end{align} $$

For any finite non-empty set *R*, let $\mathbf {Unif}(R)$ denote a uniformly distributed random variable on *R*. Then we have the following result, proven in Section 4:

#### Proposition 1.9 (Distribution of *n*-Syracuse valuation)

Let $n \in \mathbb {N}$ , and let $\mathbf {N}$ be a random variable taking values in $2\mathbb {N}+1$ . Suppose there exist an absolute constant $c_0> 0$ and some natural number $n' \geq (2+c_0) n$ such that $\mathbf {N} \bmod 2^{n'}$ is approximately uniformly distributed in the odd residue classes $(2\mathbb {Z}+1)/2^{n'}\mathbb {Z}$ of $\mathbb {Z}/2^\ell \mathbb {Z}$ , in the sense that

(1.11) $$ \begin{align} d_{\operatorname{TV}}( \mathbf{N} \bmod 2^{n'}, \mathbf{Unif}((2\mathbb{Z}+1)/2^{n'}\mathbb{Z}) ) \ll 2^{-n'}. \end{align} $$

Then

(1.12) $$ \begin{align} d_{\operatorname{TV}}( \vec a^{(n)}(\mathbf{N}), \mathbf{Geom}(2)^n ) \ll 2^{-c_1 n} \end{align} $$

for some absolute constant $c_1>0$ (depending on $c_0$ ). The implied constants in the asymptotic notation are also permitted to depend on $c_0$ .

Informally, this proposition asserts that Heuristic 1.8 is justified whenever *N*is expected to be uniformly distributed modulo $2^{n'}$ for some $n'$ slightly larger than $2n$ . The hypothesis in equation ( 1.11) is somewhat stronger than what is actually needed for the conclusion in equation ( 1.12) to hold, but this formulation of the implication will suffice for our applications. We will apply this proposition in Section 5, not to the original logarithmic distribution $\mathbf {Log}(2\mathbb {N}+1 \cap [1,x])$ (which has too heavy a tail near $1$ for the hypothesis in equation ( 1.11) to apply), but to the variant $\mathbf {Log}( 2\mathbb {N}+1 \cap [y,y^\alpha ])$ for some large *y*and some $\alpha>1$ close to $1$ .

Remark 1.10. Another standard way in the literature to justify Heuristic 1.8 is to consider the Syracuse dynamics on the $2$ -adic integers $\mathbb {Z}_2 := \varprojlim _m \mathbb {Z}/2^m\mathbb {Z}$ , or more precisely on the odd $2$ -adics $2\mathbb {Z}_2+1$ . As the $2$ -valuation $\nu _2$ remains well defined on (almost all of) $\mathbb {Z}_2$ , one can extend the Syracuse map ${\operatorname {Syr}}$ to a map on $2\mathbb {Z}_2+1$ . As is well known (see, e.g., [Reference Lagarias 14]), the Haar probability measure on $2\mathbb {Z}_2+1$ is preserved by this map, and if $\mathbf {Haar}(2\mathbb {Z}_2+1)$ is a random element of $2\mathbb {Z}_2+1$ drawn using this measure, then it is not difficult (basically using the $2$ -adic analogue of Lemma 2.1 below) to show that the random variables $\nu _2( 3{\operatorname {Syr}}^{j}(\mathbf {Haar}(2\mathbb {Z}_2+1)) + 1)$ for $j \in \mathbb {N}$ are iid copies of $\mathbf {Geom}(2)$ . However, we will not use this $2$ -adic formalism in this paper.

In practice, the offset $F_n(\vec a)$ is fairly small (in an Archimedean sense) when *n*is not too large; indeed, from equation ( 1.5), we have

(1.13) $$ \begin{align} 0 \leq F_n(\vec a) \leq 3^n 2^{-a_n} \leq 3^n \end{align} $$

for any $n \in \mathbb {N}$ and $\vec a \in (\mathbb {N}+1)^n$ . For large *N*, we then conclude from equation ( 1.7) that we have the heuristic approximation

$$ \begin{align*}{\operatorname{Syr}}^n(N) \approx 3^n 2^{-|\vec a^{(n)}(N)|} N\end{align*} $$

and hence by Heuristic 1.8, we expect ${\operatorname {Syr}}^n(N)$ to behave statistically like

(1.14) $$ \begin{align} {\operatorname{Syr}}^n(N) \approx 3^n 2^{-|\mathbf{Geom}(2)^n|} N = N \exp( n \log 3 - |\mathbf{Geom}(2)^n| \log 2 ) \end{align} $$

if *n*is much smaller than $\log N$ . One can view the sequence $n \mapsto n \log 3 - |\mathbf {Geom}(2)^n| \log 2$ as a simple random walk on $\mathbb {R}$ with negative drift $\log 3 - 2 \log 2 = \log \frac {3}{4}$ . From the law of large numbers, we expect to have

(1.15) $$ \begin{align} |\mathbf{Geom}(2)^n| \approx 2n \end{align} $$

most of the time; thus we are led to the heuristic prediction

(1.16) $$ \begin{align} {\operatorname{Syr}}^n(N) \approx (3/4)^n N \end{align} $$

for typical *N*; indeed, from the central limit theorem or the Chernoff bound, we in fact expect the refinement

(1.17) $$ \begin{align} {\operatorname{Syr}}^n(N) = \exp( O(n^{1/2}) ) (3/4)^n N \end{align} $$

for ‘typical’ *N*. In particular, we expect the Syracuse orbit $N, {\operatorname {Syr}}(N), {\operatorname {Syr}}^2(N), \dots $ to decay geometrically in time for typical *N*, which underlies the usual heuristic argument supporting the truth of Conjecture 1.1; see [Reference Lagarias and Weiss 16], [Reference Kontorovich and Lagarias 10] for further discussion. We remark that the multiplicative inaccuracy of $\exp ( O(n^{1/2}) )$ in equation ( 1.17) is the main reason why we work with logarithmic density instead of natural density in this paper (see also [Reference Kontorovich and Miller 11], [Reference Lagarias and Soundararajan 15] for a closely related ‘Benford’s law’ phenomenon).

### 1.3 Reduction to a stabilisation property for first passage locations

Roughly speaking, Proposition 1.9 lets one obtain good control on the Syracuse iterates ${\operatorname {Syr}}^n(N)$ for almost all *N*and for times *n*up to $c \log N$ for a small absolute constant *c*. This already can be used in conjunction with a rigorous version of equation ( 1.16) or ( 1.17) to recover the previously mentioned result ${\operatorname {Syr}}_{\min }(N) \leq N^{1-c}$ for almost all *N*and some absolute constant $c>0$ ; see Section 5 for details. In the language of evolutionary partial differential equations, these types of results can be viewed as analogous to ‘almost sure’ local wellposedness results, in which one has good short-time control on the evolution for almost all choices of initial condition *N*.

In this analogy, Theorem 1.6 then corresponds to an ‘almost sure’ almost global wellposedness result, where one needs to control the solution for times so large that the evolution gets arbitrary close to the bounded state $N=O(1)$ . To bootstrap from almost sure local wellposedness to almost sure almost global wellposedness, we were inspired by the work of Bourgain [Reference Bourgain 4], who demonstrated an almost sure global wellposedness result for a certain nonlinear Schrödinger equation by combining local wellposedness theory with a construction of an invariant probability measure for the dynamics. Roughly speaking, the point was that the invariance of the measure would almost surely keep the solution in a ‘bounded’ region of the state space for arbitrarily long times, allowing one to iterate the local wellposedness theory indefinitely.

In our context, we do not expect to have any useful invariant probability measures for the dynamics due to the geometric decay in equation ( 1.16) (and indeed Conjecture 1.5 would imply that the only invariant probability measure is the Dirac measure on $\{1\}$ ). Instead, we can construct a *family*of probability measures $\nu _x$ that are *approximately*transported to each other by certain iterations of the Syracuse map (by a variable amount of time). More precisely, given a threshold $x \geq 1$ and an odd natural number $N \in 2\mathbb {N}+1$ , define the *first passage time*

$$ \begin{align*}T_x(N) := \inf \{ n \in \mathbb{N}: {\operatorname{Syr}}^n(N) \leq x \},\end{align*} $$

with the convention that $T_x(N) := +\infty $ if ${\operatorname {Syr}}^n(N)> x$ for all *n*. (Of course, if Conjecture 1.5 were true, this latter possibility could not occur, but we will not be assuming this conjecture in our arguments.) We then define the *first passage location*

$$ \begin{align*}{\operatorname{Pass}}_x(N) := {\operatorname{Syr}}^{T_x(N)}(N)\end{align*} $$

with the (somewhat arbitrary and artificial) convention that ${\operatorname {Syr}}^\infty (N) := 1$ ; thus ${\operatorname {Pass}}_x(N)$ is the first location of the Syracuse orbit ${\operatorname {Syr}}^{\mathbb {N}}(N)$ that falls inside $[1,x]$ , or $1$ if no such location exists; if we ignore the latter possibility, then ${\operatorname {Pass}}_x$ can be viewed as a further acceleration of the Collatz and Syracuse maps. We will also need a constant $\alpha> 1$ sufficiently close to one. The precise choice of this parameter is not critical, but for sake of concreteness we will set

(1.18) $$ \begin{align} \alpha := 1.001. \end{align} $$

The key proposition is then

#### Proposition 1.11 (Stabilisation of first passage)

For any *y*with $2\mathbb {N}+1 \cap [y,y^\alpha ]$ is non-empty (and in particular, for any sufficiently large *y*), let $\mathbf {N}_y$ be a random variable with distribution $\mathbf {N}_y \equiv \mathbf {Log}( 2\mathbb {N}+1 \cap [y,y^\alpha ] )$ . Then for sufficiently large *x*, we have the estimates

(1.19) $$ \begin{align} \mathbb{P}( T_x(\mathbf{N}_y) = +\infty ) \ll x^{-c} \end{align} $$

for $y = x^\alpha , x^{\alpha ^2}$ , and also

(1.20) $$ \begin{align} d_{\operatorname{TV}}( {\operatorname{Pass}}_x( \mathbf{N}_{x^\alpha} ), {\operatorname{Pass}}_x( \mathbf{N}_{x^{\alpha^2}} ) ) \ll \log^{-c} x \end{align} $$

for some absolute constant $c>0$ . (The implied constants here are also absolute.)

Informally, this theorem asserts that the Syracuse orbits of $ \mathbf {N}_{x^\alpha } $ and $ \mathbf {N}_{x^{\alpha ^2}}$ are almost indistinguishable from each other once they pass *x*, as long as one synchronises the orbits so that they simultaneously pass *x*for the first time. In Section 3, we shall see how Theorem 1.6 (and hence Theorem 1.3) follows from Proposition 1.11; basically the point is that equations ( 1.19) and ( 1.20) imply that the first passage map ${\operatorname {Pass}}_x$ approximately maps the distribution $\nu _{x^\alpha }$ of ${\operatorname {Pass}}_{x^{\alpha }}( \mathbf {N}_{x^{\alpha ^2}} )$ to the distribution $\nu _x$ of ${\operatorname {Pass}}_{x}( \mathbf {N}_{x^{\alpha }} )$ , and one can then iterate this to map almost all of the probabilistic mass of $\mathbf {N}_y$ for large *y*to be arbitrarily close to the bounded state $N=O(1)$ . The implication is very general and does not use any particular properties of the Syracuse map beyond equations ( 1.19) and ( 1.20).

The estimate in equation ( 1.19) is easy to establish; it is equation ( 1.20) that is the most important and difficult conclusion of Proposition 1.11. We remark that the bound of $O(\log ^{-c} x)$ in equation ( 1.20) is stronger than is needed for this argument; any bound of the form $O((\log \log x)^{-1-c})$ would have sufficed. Conversely, it may be possible to improve the bound in equation ( 1.20) further, perhaps all the way to $x^{-c}$ .

### 1.4 Fine-scale mixing of Syracuse random variables

It remains to establish Proposition 1.11. Since the constant $\alpha $ in equation ( 1.18) is close to $1$ , this proposition falls under the regime of a (refined) ‘local wellposedness’ result, since from the heuristic in equation ( 1.16) (or equation ( 1.17)), we expect the first passage time $T_x(\mathbf {N}_y)$ to be comparable to a small multiple of $\log \mathbf {N}_y$ . Inspecting the iteration formula in equation ( 1.7), the behaviour of the *n*-Syracuse valuation $\vec a^{(n)}(\mathbf {N}_y)$ for such times *n*is then well understood thanks to Proposition 1.9; the main remaining difficulty is to understand the behaviour of the *n*-Syracuse offset map $F_n\colon (\mathbb {N}+1)^n \to \mathbb {Z}[\frac {1}{2}]$ , and more specifically to analyse the distribution of the random variable $F_n(\mathbf {Geom}(2)^n) \bmod 3^k$ for various $n,k$ , where by abuse of notation we use $x \mapsto x \bmod 3^k$ to denote the unique ring homomorphism from $\mathbb {Z}[\frac {1}{2}]$ to $\mathbb {Z}/3^k \mathbb {Z}$ (which in particular maps $\frac {1}{2}$ to the inverse $\frac {3^k+1}{2} \bmod 3^k$ of $2 \bmod 3^k$ ). Indeed, from equation ( 1.7), one has

(1.21) $$ \begin{align} {\operatorname{Syr}}^n(N) = F_n(\vec a^{(n)}(N)) \bmod 3^k \end{align} $$

whenever $0 \leq k \leq n$ and $N \in 2\mathbb {N}+1$ . Thus, if $n, \mathbf {N}, n', c_0$ obey the hypotheses of Proposition 1.9, one has

$$ \begin{align*}d_{\operatorname{TV}}( {\operatorname{Syr}}^n(\mathbf{N}) \bmod 3^k, F_n( \mathbf{Geom}(2)^n ) \bmod 3^k ) \ll 2^{-c_1 n}\end{align*} $$

for all $0 \leq k \leq n$ . If we now define the *Syracuse random variables*$\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ for $n \in \mathbb {N}$ to be random variables on the cyclic group $\mathbb {Z}/3^n\mathbb {Z}$ with the distribution

(1.22) $$ \begin{align} \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) \equiv F_n( \mathbf{Geom}(2)^n ) \bmod 3^n \end{align} $$

then from equation ( 1.5), we see that

(1.23) $$ \begin{align} \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) \bmod 3^k \equiv \mathbf{Syrac}(\mathbb{Z}/3^k\mathbb{Z}) \end{align} $$

whenever $k \leq n$ , and thus

$$ \begin{align*}d_{\operatorname{TV}}( {\operatorname{Syr}}^n(\mathbf{N}) \bmod 3^k, \mathbf{Syrac}(\mathbb{Z}/3^k\mathbb{Z}) ) \ll 2^{-c_1 n}.\end{align*} $$

We thus see that the $3$ -adic distribution of the Syracuse orbit ${\operatorname {Syr}}^{\mathbb {N}}(\mathbf {N})$ is controlled (initially, at least) by the random variables $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ . The distribution of these random variables can be computed explicitly for any given *n*via the following recursive formula:

#### Lemma 1.12 (Recursive formula for Syracuse random variables)

For any $n \in \mathbb {N}$ and $x \in \mathbb {Z}/3^{n+1}\mathbb {Z}$ , one has

$$ \begin{align*}\mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^{n+1}\mathbb{Z}) = x ) = \frac{\sum_{1 \leq a \leq 2 \times 3^n: 2^a x = 1 \bmod 3} 2^{-a} \mathbb{P}\left( \mathbf{Syrac}(\mathbb{Z}/3^{n}\mathbb{Z})= \frac{2^a x-1}{3} \right)}{1 - 2^{-2 \times 3^n}},\end{align*} $$

where $\frac {2^a x-1}{3}$ is viewed as an element of $\mathbb {Z}/3^n\mathbb {Z}$ .

Proof. Let $(\mathbf {a}_1,\dots ,\mathbf {a}_{n+1}) \equiv \mathbf {Geom}(2)^{n+1}$ be $n+1$ iid copies of $\mathbf {Geom}(2)$ . From equation ( 1.5) (after relabeling the variables $(\mathbf {a}_1,\dots ,\mathbf {a}_{n+1})$ in reverse order $(\mathbf {a}_{n+1},\dots ,\mathbf {a}_1)$ ) we have

(1.24) $$ \begin{align} F_{n+1}(\mathbf{a}_{n+1},\dots,\mathbf{a}_{1}) = \frac{3 F_n(\mathbf{a}_{n+1},\dots,\mathbf{a}_2)+1}{2^{\mathbf{a}_{1}}} \end{align} $$

and thus we have

$$ \begin{align*}\mathbf{Syrac}(\mathbb{Z}/3^{n+1}\mathbb{Z}) \equiv \frac{3\mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z})+1}{2^{\mathbf{Geom}(2)}},\end{align*} $$

where $3\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ is viewed as an element of $\mathbb {Z}/3^{n+1}\mathbb {Z}$ , and the random variables $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z}), \mathbf {Geom}(2)$ on the right-hand side are understood to be independent. We therefore have

$$ \begin{align*} \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^{n+1}\mathbb{Z}) = x ) &= \sum_{a \in \mathbb{N}+1} 2^{-a} \mathbb{P}\left( \frac{3\mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z})+1}{2^a} = x \right) \\ &= \sum_{a \in \mathbb{N}+1: 2^a x = 1 \bmod 3} 2^{-a} \mathbb{P}\left( \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) = \frac{2^a x-1}{3} \right). \end{align*} $$

By Euler’s theorem, the quantity $\frac {2^a x-1}{3} \in \mathbb {Z}/3^n \mathbb {Z}$ is periodic in *a*with period $2 \times 3^n$ . Splitting *a*into residue classes modulo $2 \times 3^n$ and using the geometric series formula, we obtain the claim.

Thus, for instance, we trivially have $\mathbf {Syrac}(\mathbb {Z}/3^0\mathbb {Z})$ takes the value $0 \bmod 1$ with probability $1$ ; then by the above lemma, $\mathbf {Syrac}(\mathbb {Z}/3\mathbb {Z})$ takes the values $0,1,2 \bmod 3$ with probabilities $0, 1/3, 2/3$ respectively; another application of the above lemma then reveals that $\mathbf {Syrac}(\mathbb {Z}/3^2\mathbb {Z})$ takes the values $0,1,\dots ,8 \bmod 9$ with probabilities

$$ \begin{align*}0, \frac{8}{63}, \frac{16}{63}, 0, \frac{11}{63}, \frac{4}{63}, 0, \frac{2}{63}, \frac{22}{63}\end{align*} $$

respectively; and so forth. More generally, one can numerically compute the distribution of $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ exactly for small values of *n*, although the time and space required to do so increases exponentially with *n*.

Remark 1.13. One could view the Syracuse random variables $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ as projections

(1.25) $$ \begin{align} \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) \equiv \mathbf{Syrac}(\mathbb{Z}_3) \bmod 3^n \end{align} $$

of a single random variable $\mathbf {Syrac}(\mathbb {Z}_3)$ taking values in the $3$ -adics $\mathbb {Z}_3 := \varprojlim _n \mathbb {Z}/3^n\mathbb {Z}$ (equipped with the usual metric $d(x,y) := 3^{-\nu _3(x-y)}$ ), which can for instance be defined as

$$ \begin{align*} \mathbf{Syrac}(\mathbb{Z}_3) &\equiv \sum_{j=0}^\infty 3^j 2^{-\mathbf{a}_{[1,j+1]}}\\ &= 2^{-\mathbf{a}_1} + 3^1 2^{-\mathbf{a}_{[1,2]}} + 3^2 2^{-\mathbf{a}_{[1,3]}} + \dots \end{align*} $$

where $\mathbf {a}_1,\mathbf {a}_2,\dots $ are iid copies of $\mathbf {Geom}(2)$ ; note that this series converges in $\mathbb {Z}_3$ , and the equivalence of distribution in equation ( 1.25) follows from equations ( 1.22) and ( 1.5) after reversing Footnote 4 the order of the tuple $(\mathbf {a}_1,\dots ,\mathbf {a}_n)$ (cf. ( 1.24)). One can view the distribution of $\mathbf {Syrac}(\mathbb {Z}_3)$ as the unique stationary measure for the discrete Markov process Footnote 5 on $\mathbb {Z}_3$ that maps each $x \in \mathbb {Z}_3$ to $\frac {3x+1}{2^{a}}$ for each $a \in \mathbb {N}+1$ with transition probability $2^{-a}$ (this fact is implicit in the proof of Lemma 1.12). However, we will not explicitly adopt the $3$ -adic perspective in this paper, preferring to work instead with the finite projections $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ of $\mathbf {Syrac}(\mathbb {Z}_3)$ .

While the Syracuse random variables $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ fail to be uniformly distributed on $\mathbb {Z}/3^n \mathbb {Z}$ , we can show that they do approach uniform distribution $n \to \infty $ at fine scales (as measured in a $3$ -adic sense), and this turns out to be the key ingredient needed to establish Proposition 1.11. More precisely, we will show

#### Proposition 1.14 (Fine-scale mixing of *n*-Syracuse offsets)

For all $1 \leq m \leq n$ one has

(1.26) $$ \begin{align} {\operatorname{Osc}}_{m,n} \left( \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) = Y \bmod 3^n ) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \ll_A m^{-A} \end{align} $$

for any fixed $A>0$ , where the oscillation ${\operatorname {Osc}}_{m,n}( c_Y )_{Y \in \mathbb {Z}/3^n\mathbb {Z}}$ of a tuple of real numbers $c_Y \in \mathbb {R}$ indexed by $\mathbb {Z}/3^n\mathbb {Z}$ at $3$ -adic scale $3^{-m}$ is defined by

(1.27) $$ \begin{align} {\operatorname{Osc}}_{m,n}( c_Y )_{Y \in \mathbb{Z}/3^n\mathbb{Z}} := \sum_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \left| c_Y - 3^{m-n} \sum_{Y' \in \mathbb{Z}/3^n\mathbb{Z}: Y' = Y \bmod 3^m} c_{Y'} \right|. \end{align} $$

Informally, the above proposition asserts that the Syracuse random variable $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ is approximately uniformly distributed in ‘fine-scale’ or ‘high-frequency’ cosets $Y + 3^m\mathbb {Z}/3^n\mathbb {Z}$ , after conditioning to the event $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z}) = Y \bmod 3^m$ . Indeed, one could write the left-hand side of equation ( 1.26) if desired as

$$ \begin{align*}d_{{\operatorname{TV}}}( \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}), \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) + \mathbf{Unif}( 3^m\mathbb{Z}/3^n\mathbb{Z}) )\end{align*} $$

where the random variables $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z}), \mathbf {Unif}( 3^m\mathbb {Z}/3^n\mathbb {Z})$ are understood to be independent. In Section 5, we show how Proposition 1.11 (and hence Theorem 1.3) follows from Proposition 1.14 and Proposition 1.9.

Remark 1.15. One can heuristically justify this mixing property as follows. The geometric random variable $\mathbf {Geom}(2)$ can be computed to have a Shannon entropy of $\log 4$ ; thus, by asymptotic equipartition, the random variable $\mathbf {Geom}(2)^n$ is expected to behave like a uniform distribution on $4^{n+o(n)}$ separate tuples in $(\mathbb {N}+1)^n$ . On the other hand, the range $\mathbb {Z}/3^n\mathbb {Z}$ of the map $\vec a \mapsto F_n(\vec a) \bmod 3^n$ only has cardinality $3^n$ . While this map does have substantial irregularities at coarse $3$ -adic scales (for instance, it always avoids the multiples of $3$ ), it is not expected to exhibit any such irregularity at fine scales, and so if one models this map by a random map from $4^{n+oW(n)}$ elements to $\mathbb {Z}/3^n\mathbb {Z}$ , one is led to the estimate in equation ( 1.26) (in fact, this argument predicts a stronger bound of $\exp ( - cm )$ for some $c>0$ , which we do not attempt to establish here).

Remark 1.16. In order to upgrade logarithmic density to natural density in our results, it seems necessary to strengthen Proposition 1.14 by establishing a suitable fine-scale mixing property of the entire random affine map ${\operatorname {Aff}}_{\mathbf {Geom}(2)^n}$ , as opposed to just the offset $F_n(\mathbf {Geom}(2)^n)$ . This looks plausibly attainable from the methods in this paper, but we do not pursue this question here.

To prove Proposition 1.14, we use a partial convolution structure present in the *n*-Syracuse offset map, together with Plancherel’s theorem, to reduce matters to establishing a superpolynomial decay bound for the characteristic function (or Fourier coefficients) of a Syracuse random variable $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ . More precisely, in Section 6, we derive Proposition 1.14 from

#### Proposition 1.17 (Decay of characteristic function)

Let $n \geq 1$ , and let $\xi \in \mathbb {Z}/3^n\mathbb {Z}$ be not divisible by $3$ . Then

(1.28) $$ \begin{align} \mathbb{E} e^{-2\pi i \xi \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z})/3^n} \ll_A n^{-A} \end{align} $$

for any fixed $A>0$ .

A key point here is that the implied constant in equation ( 1.28) is uniform in the parameters $n \geq 1$ and $\xi \in \mathbb {Z}/3^n\mathbb {Z}$ (assuming of course that $\xi $ is not divisible by $3$ ), although as indicated, we permit this constant to depend on *A*.

Remark 1.18. In the converse direction, it is not difficult to use the triangle inequality to establish the inequality

$$ \begin{align*}|\mathbb{E} e^{-2\pi i \xi \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z})/3^n}| \leq {\operatorname{Osc}}_{n-1,n} \left( \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) = Y \bmod 3^n ) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}}\end{align*} $$

whenever $\xi $ is not a multiple of $3$ (so in particular the function $x \mapsto e^{-2\pi i \xi x/3^n}$ has mean zero on cosets of $3^{n-1}\mathbb {Z}/3^n\mathbb {Z}$ ). Thus Proposition 1.17 and Proposition 1.14 are in fact equivalent. One could also equivalently phrase Proposition 1.17 in terms of the decay properties of the characteristic function of $\mathbf {Syrac}(\mathbb {Z}_3)$ (which would be defined on the Pontryagin dual $\hat {\mathbb {Z}}_3 = \mathbb {Q}_3/\mathbb {Z}_3$ of $\mathbb {Z}_3$ ), but we will not do so here.

The remaining task is to establish Proposition 1.17. This turns out to be the most difficult step in the argument, and is carried out in Section 7. From equations ( 1.5) and ( 1.22) and reversing the order of the random variables $\mathbf {a}_1,\dots ,\mathbf {a}_n$ (cf. equation ( 1.24)), we can describe the distribution of the Syracuse random variable by the formula

(1.29) $$ \begin{align} \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) \equiv 2^{-\mathbf{a}_1} + 3^1 2^{-\mathbf{a}_{[1,2]}} + \dots + 3^{n-1} 2^{-\mathbf{a}_{[1,n]}} \bmod 3^n, \end{align} $$

with $(\mathbf {a}_1,\dots ,\mathbf {a}_n) \equiv \mathbf {Geom}(2)^n$ ; this also follows from equation ( 1.25). If this random variable $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ was the sum of independent random variables, then the characteristic function of $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ would factor as something like a Riesz product of cosines, and its estimation would be straightforward. Unfortunately, the expression in equation ( 1.29) does not obviously resolve into such a sum of independent random variables; however, by grouping adjacent terms $3^{2j-2} 2^{-\mathbf {a}_{[1,2j-1]}}, 3^{2j-1} 2^{-\mathbf {a}_{[1,2j]}}$ in equation ( 1.29) into pairs, one can at least obtain a decomposition into the sum of independent expressions once one conditions on the sums $\mathbf {b}_j := \mathbf {a}_{2j-1}+\mathbf {a}_{2j}$ (which are iid copies of a Pascal distribution $\mathbf {Pascal}$ ). This lets one express the characteristic functions as an *average*of products of cosines (times a phase), where the average is over trajectories of a certain random walk $\mathbf {v}_1, \mathbf {v}_{[1,2]}, \mathbf {v}_{[1,3]},\dots $ in $\mathbb {Z}^2$ with increments in the first quadrant that we call a *two-dimensional renewal process*. If we color certain elements of $\mathbb {Z}^2$ ‘white’ when the associated cosines are small, and ‘black’ otherwise, then the problem boils down to ensuring that this renewal process encounters a reasonably large number of white points (see Figure 3 in Section 7).

From some elementary number theory, we will be able to describe the black regions of $\mathbb {Z}^2$ as a union of ‘triangles’ $\Delta $ that are well separated from each other; again, see Figure 3. As a consequence, whenever the renewal process passes through a black triangle, it will very likely also pass through at least one white point after it exits the triangle. This argument is adequate so long as the triangles are not too large in size; however, for very large triangles, it does not produce a sufficient number of white points along the renewal process. However, it turns out that large triangles tend to be fairly well separated from each other (at least in the neighbourhood of even larger triangles), and this geometric observation allows one to close the argument.

As with Proposition 1.14, it is possible that the bound in Proposition 1.17 could be improved, perhaps to as far as $O(\exp (-cn))$ for some $c>0$ . However, we will not need or pursue such a bound here.

## 2 Notation and preliminaries

We use the asymptotic notation $X \ll Y$ , $Y \gg X$ , or $X = O(Y)$ to denote the bound $|X| \leq CY$ for an absolute constant *C*. We also write $X \asymp Y$ for $X \ll Y \ll X$ . We also use $c>0$ to denote various small constants that are allowed to vary from line to line or even within the same line. If we need the implied constants to depend on other parameters, we will indicate this by subscripts unless explicitly stated otherwise; thus, for instance, $X \ll _A Y$ denotes the estimate $|X| \leq C_A Y$ for some $C_A$ depending on *A*.

If *E*is a set, we use $1_E$ to denote its indicator; thus $1_E(n)$ equals $1$ when $n \in E$ and $0$ otherwise. Similarly, if *S*is a statement, we define the indicator $1_S$ to equal $1$ when *S*is true and $0$ otherwise; thus, for instance, $1_E(n) = 1_{n \in E}$ . If $E,F$ are two events, we use $E \wedge F$ to denote their conjunction (the event that both $E,F$ hold) and $\overline {E}$ to denote the complement of *E*(the event that *E*does not hold).

The following alternate description of the *n*-Syracuse valuation $\vec a^{(n)}(N)$ (variants of which have frequently occurred in the literature on the Collatz conjecture; see, e.g., [Reference Sinai 19]) will be useful.

### Lemma 2.1 (Description of *n*-Syracuse valuation)

Let $N \in 2\mathbb {N}+1$ and $n \in \mathbb {N}$ . Then $\vec a^{(n)}(N)$ is the unique tuple $\vec a$ in $(\mathbb {N}+1)^n$ for which ${\operatorname {Aff}}_{\vec a}(N) \in 2\mathbb {N}+1$ .

Proof. It is clear from equation ( 1.7) that ${\operatorname {Aff}}_{\vec a^{(n)}(N)} \in 2\mathbb {N}+1$ . It remains to prove uniqueness. The claim is easy for $n=0$ , so suppose inductively that $n \geq 1$ and that uniqueness has already been established for $n-1$ . Suppose that we have found a tuple $\vec a \in (\mathbb {N}+1)^n$ for which ${\operatorname {Aff}}_{\vec a}(N)$ is an odd integer. Then

$$ \begin{align*}{\operatorname{Aff}}_{\vec a}(N) = {\operatorname{Aff}}_{a_n}( {\operatorname{Aff}}_{a_1,\dots,a_{n-1}}(N) ) = \frac{3{\operatorname{Aff}}_{a_1,\dots,a_{n-1}}(N)+1}{2^{a_n}}\end{align*} $$

and thus

(2.1) $$ \begin{align} 2^{a_n} {\operatorname{Aff}}_{\vec a}(N) =3{\operatorname{Aff}}_{a_1,\dots,a_{n-1}}(N)+1. \end{align} $$

This implies that $3{\operatorname {Aff}}_{a_1,\dots ,a_{n-1}}(N)$ is an odd natural number. But from equation ( 1.3), ${\operatorname {Aff}}_{a_1,\dots ,a_{n-1}}(N)$ also lies in $\mathbb {Z}[\frac {1}{2}]$ . The only way these claims can both be true is if ${\operatorname {Aff}}_{a_1,\dots ,a_{n-1}}(N)$ is also an odd natural number, and then by induction $(a_1,\dots ,a_{n-1}) = \vec a^{(n-1)}(N)$ , which by equation ( 1.7) implies that

$$ \begin{align*}{\operatorname{Aff}}_{a_1,\dots,a_{n-1}}(N) = {\operatorname{Syr}}^{n-1}(N).\end{align*} $$

Inserting this into equation ( 2.1) and using the fact that ${\operatorname {Aff}}_{\vec a}(N)$ is odd, we obtain

$$ \begin{align*}a_n = \nu_2( 3{\operatorname{Syr}}^{N-1}(N) + 1 ) \end{align*} $$

and hence by equation ( 1.8), we have $\vec a = \vec a^{(n)}$ as required.

We record the following concentration of measure bound of Chernoff type, which also bears some resemblance to a local limit theorem. We introduce the gaussian-type weights

(2.2) $$ \begin{align} G_n(x) := \exp( - |x|^2/n ) + \exp( - |x| ) \end{align} $$

for any $n \geq 0$ and $x \in \mathbb {R}^d$ for some $d \geq 1$ , where we adopt the convention that $\exp (-\infty )=0$ (so that $G_0(x) = \exp (-|x|)$ ). Thus $G_n(x)$ is comparable to $1$ for $x = O(n^{1/2})$ , decays in a gaussian fashion in the regime $n^{1/2} \leq |x| \leq n$ and decays exponentially for $|x| \geq n$ .

### Lemma 2.2 (Chernoff type bound(

Let $d \in \mathbb {N}+1$ , and let $\mathbf {v}$ be a random variable taking values in $\mathbb {Z}^d$ obeying the exponential tail condition

(2.3) $$ \begin{align} \mathbb{P}( |\mathbf{v}| \geq \lambda ) \ll \exp( -c_0 \lambda ) \end{align} $$

for all $\lambda \geq 0$ and some $c_0>0$ . Assume the non-degeneracy condition that $\mathbf {v}$ is not almost surely concentrated on any coset of any proper subgroup of $\mathbb {Z}^d$ . Let $\vec \mu := \mathbb {E} \mathbf {v} \in \mathbb {R}^d$ denote the mean of $\mathbf {v}$ . In this lemma all implied constants, as well as the constant *c*, can depend on *d*, $c_0$ , and the distribution of $\mathbf {v}$ . Let $n \in \mathbb {N}$ , and let $\mathbf {v}_1,\dots ,\mathbf {v}_n$ be *n*iid copies of $\mathbf {v}$ . Following equation ( 1.6), we write $\mathbf {v}_{[1,n]} := \mathbf {v}_1 + \dots + \mathbf {v}_n$ .

1.

(i) For any $\vec L \in \mathbb {Z}^d$ , one has

$$ \begin{align*}\mathbb{P}\left( \mathbf{v}_{[1,n]} = \vec L \right) \ll \frac{1}{(n+1)^{d/2}}G_n\left( c \left(\vec L - n \vec \mu\right) \right)\!.\end{align*} $$

2.

(ii) For any $\lambda \geq 0$ , one has

$$ \begin{align*}\mathbb{P}\left( |\mathbf{v}_{[1,n]}- n \vec \mu| \geq \lambda \right) \ll G_n( c \lambda ).\end{align*} $$

Thus, for instance for any $n \in \mathbb {N}$ , we have

$$ \begin{align*}\mathbb{P}\left( |\mathbf{Geom}(2)^n| = L \right) \ll \frac{1}{\sqrt{n+1}} G_n( c(L-2n))\end{align*} $$

for every $L \in \mathbb {Z}$ , and

$$ \begin{align*}\mathbb{P}\left( \left||\mathbf{Geom}(2)^n| - 2n\right| \geq \lambda \right) \ll G_n(c \lambda)\end{align*} $$

for any $\lambda \geq 0$ .

Proof. We use the Fourier-analytic (and complex-analytic) method. We may assume that *n*is positive since the claim is trivial for $n=0$ . We begin with (i). Let *S*denote the complex strip $S := \{ z \in \mathbb {C}: |\mathrm {Re}(z)| < c_0 \}$ , then we can define the (complexified) moment generating function $M \colon S^d \to \mathbb {C}$ by the formula

$$ \begin{align*}M(z_1,\dots,z_d) := \mathbb{E} \exp( (z_1,\dots,z_d) \cdot \mathbf{v} ),\end{align*} $$

where $\cdot $ is the usual bilinear dot product. From equation ( 2.3) and Morera’s theorem, one verifies that this is a well-defined holomorphic function of *d*complex variables on $S^d$ , which is periodic with respect to the lattice $(2\pi i\mathbb {Z})^d$ . By Fourier inversion, we have

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,n]} = \vec L) = \frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} M\left( i\vec t \right)^n \exp\left( - i \vec t \cdot \vec L \right)\ d\vec t.\end{align*} $$

By contour shifting, we then have

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,n]} = \vec L) = \frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} M\left( i\vec t + \vec \lambda\right)^n \exp\left( - (i\vec t + \lambda) \cdot \vec L \right)\ d\vec t\end{align*} $$

whenever $\vec \lambda = (\lambda _1,\dots ,\lambda _d) \in (-c_0,c_0)^d$ . By the triangle inequality, we thus have

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,n]} = \vec L) \ll \int_{[-\pi,\pi]^d} \left|M\left( i\vec t + \vec \lambda\right)\right|{}^n \exp\left( - \vec \lambda \cdot \vec L \right)\ d\vec t.\end{align*} $$

From Taylor expansion and the non-degeneracy condition we have

$$ \begin{align*}M(\vec z) = \exp\left( \vec z \cdot \vec \mu + \frac{1}{2} \Sigma(\vec z) + O(|\vec z|^3) \right)\end{align*} $$

for all $\vec z \in S^d$ sufficiently close to $0$ , where $\Sigma $ is a positive definite quadratic form (the covariance matrix of $\mathbf {v}$ ). From the non-degeneracy condition we also see that $|M(i\vec t)| < 1$ whenever $\vec t \in [-\pi ,\pi ]^d$ is not identically zero, hence by continuity $|M(i\vec t + \vec \lambda )| \leq 1-c$ whenever $\vec t \in [-\pi ,\pi ]^d$ is bounded away from zero and $\vec \lambda $ is sufficiently small. This implies the estimates

$$ \begin{align*}|M(i\vec t + \vec \lambda )| \leq \exp\left( \vec \lambda \cdot \vec \mu - c |\vec t|^2 + O( |\vec \lambda|^2) \right)\end{align*} $$

for all $\vec t \in [-\pi ,\pi ]^d$ and all sufficiently small $\vec \lambda \in \mathbb {R}^d$ . Thus we have

$$ \begin{align*} \mathbb{P}( \mathbf{v}_{[1,n]} = \vec L) &\ll \int_{[-\pi,\pi]^d} \exp\left( - \vec \lambda \cdot (\vec L-n\vec \mu) - c n|\vec t|^2 + O( n |\vec \lambda|^2 ) \right)\ d\vec t \\ &\ll n^{-1/2} \exp\left( - \vec \lambda \cdot (\vec L-n\vec \mu) + O( n |\vec \lambda|^2 ) \right). \end{align*} $$

If $|\vec L-n\vec \mu | \leq n$ , we can set $\vec \lambda := c(\vec L-n\vec \mu ) / n$ for a sufficiently small *c*and obtain the claim; otherwise if $|\vec L-n\vec \mu |> n$ , we set $\vec \lambda := c(\vec L-n\vec \mu )/|\vec L-n\vec \mu |$ for a sufficiently small *c*and again obtain the claim. This gives (i), and the claim (ii) then follows from summing in $\vec L$ and applying the integral test.

Remark 2.3. Informally, the above lemma asserts that as a crude first approximation we have

(2.4) $$ \begin{align} \mathbf{v}_{[1,n]} \approx n\vec \mu + \mathbf{Unif}( \{ k \in \mathbb{Z}^d: k = O(\sqrt{n}) \} ), \end{align} $$

and in particular

(2.5) $$ \begin{align} |\mathbf{Geom}(2)^n| \approx \mathbf{Unif}( \mathbb{Z} \cap [2n - O(\sqrt{n}), 2n + O(\sqrt{n})] ), \end{align} $$

thus refining equation ( 1.15). The reader may wish to use this heuristic for subsequent arguments (for instance, in heuristically justifying equation ( 1.17)).

## 3 Reduction to stabilisation of first passage

In this section, we show how Theorem 1.6 follows from Proposition 1.11. In fact, we show that Proposition 1.11 implies a stronger claim Footnote 6:

### Theorem 3.1 (Alternate form of main theorem)

For $N_0 \geq 2$ and $x \geq 2$ , one has

$$ \begin{align*}\frac{1}{\log x} \sum_{N \in 2\mathbb{N}+1 \cap [1,x]: {\operatorname{Syr}}_{\min}(N)> N_0} \frac{1}{N} \ll \frac{1}{\log^c N_0}\end{align*} $$

or equivalently

$$ \begin{align*}\mathbb{P}( {\operatorname{Syr}}_{\min}( \mathbf{Log}(2\mathbb{N}+1 \cap [1,x]) ) \leq N_0 ) \geq 1 - O\left( \frac{1}{\log^c N_0} \right)\!.\end{align*} $$

In particular, by equation ( 1.2), we have

$$ \begin{align*}\mathbb{P}( {\operatorname{Col}}_{\min}( \mathbf{Log}(\mathbb{N}+1 \cap [1,x]) ) \leq N_0 ) \geq 1 - O\left( \frac{1}{\log^c N_0} \right)\end{align*} $$

for all $x \geq 2$ .

In other words, for $N_0 \geq 2$ , one has $\mathrm {Syr}_{\min }(N) \leq N_0$ for all *N*in a set of odd natural numbers of (lower) logarithmic density $\frac {1}{2} - O( \log ^{-c} N_0)$ , and one also has $\mathrm {Col}_{\min }(N) \leq N_0$ for all *N*in a set of positive natural numbers of (lower) logarithmic density $1 - O( \log ^{-c} N_0)$ .

Proof. We may assume that $N_0$ is larger than any given absolute constant, since the claim is trivial for bounded $N_0$ . Let $E_{N_0} \subset 2\mathbb {N}+1$ denote the set

$$ \begin{align*}E_{N_0} := \{ N \in 2\mathbb{N}+1: {\operatorname{Syr}}_{\min}(N) \leq N_0 \}\end{align*} $$

of starting positions *N*of Syracuse orbits that reach $N_0$ or below. Let $\alpha $ be defined by equation ( 1.18), let $x \geq 2$ , and let $\mathbf {N}_y$ be the random variables from Proposition 1.11. Let $B_x = B_{x,N_0}$ denote the event that $T_x(\mathbf {N}_{x^\alpha }) < +\infty $ and ${\operatorname {Pass}}_{x}(\mathbf {N}_{x^{\alpha }}) \in E_{N_0}$ . Informally, this is the event that the Syracuse orbit of $\mathbf {N}_{x^\alpha }$ reaches *x*or below and then reaches $N_0$ or below. (For $x < N_0$ , the latter condition is automatic, while for $x \geq N_0$ , it is the former condition which is redundant.)

Observe that if $T_x( \mathbf {N}_{x^{\alpha ^2}} ) < +\infty $ and ${\operatorname {Pass}}_x(\mathbf {N}_{x^{\alpha ^2}}) \in E_{N_0}$ , then

$$ \begin{align*}T_{x^\alpha}( \mathbf{N}_{x^{\alpha^2}} ) \leq T_x( \mathbf{N}_{x^{\alpha^2}} ) < +\infty\end{align*} $$

and

$$ \begin{align*}{\operatorname{Syr}}^{\mathbb{N}}({\operatorname{Pass}}_x(\mathbf{N}_{x^{\alpha^2}})) \subset {\operatorname{Syr}}^{\mathbb{N}}({\operatorname{Pass}}_{x^\alpha}(\mathbf{N}_{x^{\alpha^2}}))\end{align*} $$

which implies that

$$ \begin{align*}{\operatorname{Syr}}_{\min}( {\operatorname{Pass}}_{x^\alpha}(\mathbf{N}_{x^{\alpha^2}}) ) \leq {\operatorname{Syr}}_{\min}( {\operatorname{Pass}}_x(\mathbf{N}_{x^{\alpha^2}}) ) \leq N_0.\end{align*} $$

In particular, the event $B_{x^\alpha }$ holds in this case. From this and equations ( 1.19), ( 1.20) and ( 1.10), we have

$$ \begin{align*} \mathbb{P}( B_{x^\alpha}) &\geq \mathbb{P}( {\operatorname{Pass}}_{x}(\mathbf{N}_{x^{\alpha^2}}) \in E_{N_0} \wedge T_{x}( \mathbf{N}_{x^{\alpha^2}} ) < +\infty ) \\ &\geq \mathbb{P}( {\operatorname{Pass}}_{x}(\mathbf{N}_{x^{\alpha^2}}) \in E_{N_0} ) - O( x^{-c} ) \\ &\geq \mathbb{P}( {\operatorname{Pass}}_{x}(\mathbf{N}_{x^{\alpha}}) \in E_{N_0} ) - O( \log^{-c} x ) \\ &\geq \mathbb{P}( B_x ) - O( \log^{-c} x ) \end{align*} $$

whenever *x*is larger than a suitable absolute constant (note that the $O(x^{-c})$ error can be absorbed into the $O(\log ^{-c} x)$ term). In fact, the bound holds for all $x \geq 2$ , since the estimate is trivial for bounded values of *x*.

Let $J = J(x,N_0)$ be the first natural number such that the quantity $y := x^{\alpha ^{-J}}$ is less than $N_0^{1/\alpha }$ . Since $N_0$ is assumed to be large, we then have (by replacing *x*with $y^{\alpha ^{j-2}}$ in the preceding estimate) that

$$ \begin{align*}\mathbb{P}( B_{y^{\alpha^{j-1}}} ) \geq \mathbb{P}( B_{y^{\alpha^{j-2}}} ) - O( (\alpha^j \log y)^{-c} ) \end{align*} $$

for all $j=1,\dots ,J$ . The event $B_{y^{\alpha ^{-1}}}$ occurs with probability $1 - O(y^{-c})$ , thanks to equation ( 1.19) and the fact that $\mathbf {N}_{y} \leq y^\alpha \leq N_0$ . Summing the telescoping series, we conclude that

$$ \begin{align*}\mathbb{P}( B_{y^{\alpha^{J-1}}} ) \geq 1 - O( \log^{-c} y )\end{align*} $$

(note that the $O(y^{-c})$ error can be absorbed into the $O( \log ^{-c} y )$ term). By construction, $y \geq N_0^{1/\alpha ^2}$ and $y^{\alpha ^J} = x$ , so

$$ \begin{align*}\mathbb{P}( B_{x^{1/\alpha}} ) \geq 1 - O( \log^{-c} N_0 ).\end{align*} $$

If $B_{x^{1/\alpha }}$ holds, then ${\operatorname {Pass}}_{x^{1/\alpha }}( \mathbf {N}_x )$ lies in the Syracuse orbit ${\operatorname {Syr}}^{\mathbb {N}}(\mathbf {N}_x)$ , and thus ${\operatorname {Syr}}_{\min }(\mathbf {N}_x) \leq {\operatorname {Syr}}_{\min }({\operatorname {Pass}}_{x^{1/\alpha }}( \mathbf {N}_x )) \leq N_0$ . We conclude that for any $x \geq 2$ , one has

$$ \begin{align*}\mathbb{P}( {\operatorname{Syr}}_{\min}(\mathbf{N}_x)> N_0 ) \ll \log^{-c} N_0.\end{align*} $$

By definition of $\mathbf {N}_x$ (and using the integral test to sum the harmonic series $\sum _{N \in 2\mathbb {N}+1 \cap [x,x^\alpha ]} \frac {1}{N}$ ), we conclude that

(3.1) $$ \begin{align} \sum_{N \in 2\mathbb{N}+1 \cap [x,x^\alpha]: {\operatorname{Syr}}_{\min}(N)> N_0} \frac{1}{N} \ll \frac{1}{\log^c N_0} \log x \end{align} $$

for all $x \geq 2$ . Covering the interval $2\mathbb {N}+1 \cap [1,x]$ by intervals of the form $2\mathbb {N}+1 \cap [y,y^\alpha ]$ for various *y*, we obtain the claim.

Now let $f\colon 2\mathbb {N}+1 \to [0,+\infty )$ be such that $\lim _{N \to \infty } f(N) = +\infty $ . Set $\tilde f(x) := \inf _{N \in 2\mathbb {N}+1: N \geq x} f(N)$ , then $\tilde f(x) \to \infty $ as $x \to \infty $ . Applying Theorem 3.1 with $N_0 := \tilde f(x)$ , we conclude that

$$ \begin{align*}\sum_{N \in 2\mathbb{N}+1 \cap [1,x]: {\operatorname{Syr}}_{\min}(N)> f(N)} \frac{1}{N} \ll \frac{1}{\log^c \tilde f(x)} \log x\end{align*} $$

for all sufficiently large *x*. Since $\frac {1}{\log ^c\tilde f(x)}$ goes to zero as $x \to \infty $ , we conclude from telescoping series that the set $\{ N \in 2\mathbb {N}+1: {\operatorname {Syr}}_{\min }(N)> f(N) \}$ has zero logarithmic density, and Theorem 1.6 follows.

## 4 $3$ -adic distribution of iterates

In this section, we establish Proposition 1.9. Let $n, \mathbf {N}, c_0, n'$ be as in that proposition; in particular, $n' \geq (2+c_0) n$ . In this section, we allow implied constants in the asymptotic notation, as well as the constants $c>0$ , to depend on $c_0$ .

We first need a tail bound on the size of the *n*-Syracuse valuation $\vec a^{(n)}(\mathbf {N})$ :

### Lemma 4.1 (Tail bound)

We have

$$ \begin{align*}\mathbb{P}( |\vec a^{(n)}(\mathbf{N})| \geq n' ) \ll 2^{-cn}.\end{align*} $$

Proof. Write $\vec a^{(n)}(\mathbf {N}) = (\mathbf {a}_1,\dots ,\mathbf {a}_n)$ , then we may split

$$ \begin{align*}\mathbb{P}( |\vec a^{(n)}(\mathbf{N})| \geq n' ) = \sum_{k=0}^{n-1} \mathbb{P}( \mathbf{a}_{[1,k]} < n' \leq \mathbf{a}_{[1,k+1]} )\end{align*} $$

(using the summation convention in equation ( 1.6)), and so it suffices to show that

$$ \begin{align*}\mathbb{P}( \mathbf{a}_{[1,k]} < n' \leq \mathbf{a}_{[1,k+1]} ) \ll 2^{-cn}\end{align*} $$

for each $0 \leq k \leq n-1$ .

From Lemma 2.1 and equation ( 1.3), we see that

$$ \begin{align*}3^{k+1} 2^{- \mathbf{a}_{[1,k+1]}} \mathbf{N} + \sum_{i=1}^{k+1} 3^{k+1-i} 2^{-\mathbf{a}_{[i,k+1]}}\end{align*} $$

is an odd integer, and thus

$$ \begin{align*}3^{k+1} \mathbf{N} + \sum_{i=1}^{k+1} 3^{k+1-i} 2^{\mathbf{a}_{[1,i-1]}}\end{align*} $$

is a multiple of $2^{\mathbf {a}_{[1,k+1]}}$ . In particular, when the event $\mathbf {a}_{[1,k]} < n' \leq \mathbf {a}_{[1,k+1]}$ holds, one has

$$ \begin{align*}3^{k+1} \mathbf{N} + \sum_{i=1}^{k+1} 3^{k+1-i} 2^{\mathbf{a}_{[1,i-1]}} = 0 \bmod 2^{n'}.\end{align*} $$

Thus, if one conditions to the event $\mathbf {a}_j = a_j, j=1,\dots ,k$ for some positive integers $a_1,\dots ,a_k$ , then $\mathbf {N}$ is constrained to a single residue class $b \bmod 2^{n'}$ depending on $a_1,\dots ,a_k$ (because $3^{k+1}$ is invertible in the ring $\mathbb {Z}/2^{n'}\mathbb {Z}$ ). From equations ( 1.11) and ( 1.9), we have the quite crude estimate

$$ \begin{align*}\mathbb{P}( \mathbf{N} = b \bmod 2^{n'} ) \ll 2^{-n'}\end{align*} $$

and hence

$$ \begin{align*}\mathbb{P}( \mathbf{a}_{[1,k]} \leq n' < \mathbf{a}_{[1,k+1]} ) \ll \sum_{a_1,\dots,a_k \in \mathbb{N}+1: a_{[1,k]} < n'} 2^{-n'}.\end{align*} $$

The tuples $(a_1,\dots ,a_k)$ in the above sum are in one-to-one correspondence with the *k*-element subsets $\{ a_1, a_{[1,2]},\dots ,a_{[1,k]}\}$ of $\{1,\dots ,n'-1\}$ , and hence have cardinality $\binom {n'-1}{k}$ ; thus

$$ \begin{align*}\mathbb{P}( \mathbf{a}_{[1,k]} < n' \leq \mathbf{a}_{[1,k+1]} ) \ll 2^{-n'} \binom{n'-1}{k}.\end{align*} $$

Since $k \leq n-1$ and $n' \geq (2+c_0) n$ , the right-hand side is $O(2^{-cn})$ by Stirling’s formula (one can also use the Chernoff inequality for the sum of $n'-1$ Bernoulli random variables $\mathbf {Ber}(\frac {1}{2})$ , or Lemma 2.2). The claim follows.

From Lemma 2.2, we also have

$$ \begin{align*}\mathbb{P}( |\mathbf{Geom}(2)^n| \geq n' ) \ll 2^{-cn}.\end{align*} $$

From equation ( 1.9) and the triangle inequality, we therefore have

$$ \begin{align*}d_{\operatorname{TV}}(\vec a^{(n)}(\mathbf{N}), \mathbf{Geom}(2)^n) = \sum_{\vec a \in (\mathbb{N}+1)^n: |\vec a| < m} |\mathbb{P}(\vec a^{(n)}(\mathbf{N})=\vec a) - \mathbb{P}(\mathbf{Geom}(2)^n=\vec a)| + O( 2^{-cn} ).\end{align*} $$

From Definition 1.7, we have

$$ \begin{align*}\mathbb{P}(\mathbf{Geom}(2)^n=\vec a) = 2^{-|\vec a|}\end{align*} $$

so it remains to show that

(4.1) $$ \begin{align} \sum_{\vec a \in (\mathbb{N}+1)^n: |\vec a| < m} |\mathbb{P}(\vec a^{(n)}(\mathbf{N})=\vec a) - 2^{-|\vec a|}| \ll 2^{-cn}. \end{align} $$

By Lemma 2.1, the event $\vec a^{(n)}(\mathbf {N})=\vec a$ occurs precisely when ${\operatorname {Aff}}_{\vec a}(\mathbf {N})$ is an odd integer, which by equation ( 1.3), we may write (for $\vec a = (a_1,\dots ,a_n)$ ) as

$$ \begin{align*}3^n 2^{-a_{[1,n]}} \mathbf{N} + 3^{n-1} 2^{-a_{[1,n]}} + 3^{n-2} 2^{-a_{[2,n]}} + \dots + 2^{-a_n} \in 2\mathbb{N}+1.\end{align*} $$

Equivalently one has

$$ \begin{align*}3^n \mathbf{N} = - 3^{n-1} - 3^{n-2} 2^{a_1} - \dots - 2^{a_{[1,n-1]}} + 2^{|\vec a|} \bmod 2^{|\vec a|+1}.\end{align*} $$

This constrains $\mathbf {N}$ to a single odd residue class modulo $2^{|\vec a|+1}$ . For $|\vec a| < n'$ , the probability of falling in this class can be computed using equations ( 1.11) and ( 1.9) as $2^{-|\vec a|} + O( 2^{-n'} )$ . The left-hand side of equation ( 4.1) is then bounded by

$$ \begin{align*}\ll 2^{-n'} \# \{ \vec a \in (\mathbb{N}+1)^n: |\vec a| < n' \} = 2^{-n'} \binom{n'-1}{n}.\end{align*} $$

The claim now follows from Stirling’s formula (or Chernoff’s inequality), as in the proof of Lemma 4.1. This completes the proof of Proposition 1.9.

## 5 Reduction to fine-scale mixing of the *n*-Syracuse offset map

We are now ready to derive Proposition 1.11 (and thus Theorem 1.3) assuming Proposition 1.14. Let *x*be sufficiently large. We take *y*to be either $x^\alpha $ or $x^{\alpha ^2}$ . From the heuristic in equation ( 1.16) (or equation ( 1.17)), we expect the first passage time ${\operatorname {Pass}}_x(\mathbf {N}_y)$ to be roughly

$$ \begin{align*}{\operatorname{Pass}}_x(\mathbf{N}_y) \approx \frac{\log \mathbf{N}_y / x}{\log(4/3)}\end{align*} $$

with high probability. Now introduce the quantities

(5.1) $$ \begin{align} n_0 := \left\lfloor \frac{\log x}{10 \log 2} \right\rfloor \end{align} $$

(so that $2^{n_0} \asymp x^{0.1}$ ) and

(5.2) $$ \begin{align} m_0 := \left\lfloor \frac{\alpha-1}{100} \log x \right\rfloor \!. \end{align} $$

Since the random variable $\mathbf {N}_y$ takes values in $[y,y^\alpha ]$ , we see from equation ( 1.18) that we would expect the bounds

(5.3) $$ \begin{align} m_0 \leq T_x(\mathbf{N}_y) \leq n_0 \end{align} $$

to hold with high probability. We will use these parameters $m_0, n_0$ to help control the distribution of $T_x(\mathbf {N}_y)$ and ${\operatorname {Pass}}_x(\mathbf {N}_y)$ in order to prove equations ( 1.19) and ( 1.20).

We begin with the proof of equation ( 1.19). Let $n_0$ be defined by equation ( 5.1). Since $\mathbf {N}_y \equiv \mathbf {Log}(2\mathbb {N}+1 \cap [y,y^\alpha ])$ , a routine application of the integral test reveals that

$$ \begin{align*}d_{\operatorname{TV}}( \mathbf{N}_y \bmod 2^{3n_0}, \mathbf{Unif}((2\mathbb{Z}+1)/2^{3n_0}\mathbb{Z})) \ll 2^{-3n_0}\end{align*} $$

(with plenty of room to spare), hence by Proposition 1.9

(5.4) $$ \begin{align} d_{\operatorname{TV}}( \vec a^{(n_0)}(\mathbf{N}_y), \mathbf{Geom}(2)^{n_0} ) \ll 2^{-c n_0}. \end{align} $$

In particular, by equation ( 1.10) and Lemma 2.2, we have

(5.5) $$ \begin{align} \mathbb{P}( |\vec a^{(n_0)}(\mathbf{N}_y)| \leq 1.9 n_0 ) \leq \mathbb{P}( |\mathbf{Geom}(2)^{n_0}| \leq 1.9 n_0 ) + O(2^{-cn_0}) \ll 2^{-cn_0} \ll x^{-c} \end{align} $$

(recall we allow *c*to vary even within the same line). On the other hand, from equations ( 1.7) and ( 1.5), we have

$$ \begin{align*}{\operatorname{Syr}}^{n_0}(\mathbf{N}_y) \leq 3^{n_0} 2^{-|\vec a^{(n_0)}(\mathbf{N}_y)|} \mathbf{N}_y + O( 3^{n_0} ) \leq 3^{n_0} 2^{-|\vec a^{(n_0)}(\mathbf{N}_y)|} x^{\alpha^3} + O(3^{n_0})\end{align*} $$

and hence if $|\vec a^{(n_0)}(\mathbf {N}_y)|> 1.9 n$ , then

$$ \begin{align*}{\operatorname{Syr}}^{n_0}(\mathbf{N}_y) \ll 3^{n_0} 2^{-1.9 n_0} x^{\alpha^3} + O(3^{n_0}).\end{align*} $$

From equations ( 5.1) and ( 1.18) and a brief calculation, the right-hand side is $O(x^{0.99})$ (say). In particular, for *x*large enough, we have

$$ \begin{align*}{\operatorname{Syr}}^{n_0}(\mathbf{N}_y) \leq x,\end{align*} $$

and hence $T_x(\mathbf {N}_y) \leq n_0 < +\infty $ whenever $|\vec a^{(n_0)}(\mathbf {N}_y)|> 1.9 n_0$ (cf., the upper bound in equation ( 5.3)). The claim in equation ( 1.19) now follows from equation ( 5.5).

Remark 5.1. This argument already establishes that ${\operatorname {Syr}}_{\min }(N) \leq N^\theta $ for almost all *N*for any $\theta> 1/\alpha $ ; by optimising the numerical exponents in this argument one can eventually recover the results of Korec [Reference Korec 9] mentioned in the introduction. It also shows that most odd numbers do not lie in a periodic Syracuse orbit, or more precisely that

$$ \begin{align*}\mathbb{P}( {\operatorname{Syr}}^n(\mathbf{N}_y) = \mathbf{N}_y \text{ for some } n \in \mathbb{N}+1 ) \ll x^{-c}.\end{align*} $$

Indeed, the above arguments show that outside of an event of probability $x^{-c}$ , one has ${\operatorname {Syr}}^{\mathbf {m}}(\mathbf {N}_y) \leq x$ for some $\mathbf {m} \leq n_0$ , which we can assume to be minimal amongst all such $\mathbf {m}$ . If ${\operatorname {Syr}}^n(\mathbf {N}_y) = \mathbf {N}_y$ for some *n*, we then have

(5.6) $$ \begin{align} \mathbf{N}_y = {\operatorname{Syr}}^{n(\mathbf{M})-\mathbf{m}}(\mathbf{M}) \end{align} $$

for $\mathbf {M} := {\operatorname {Syr}}^{\mathbf {m}}(\mathbf {N}_y) \in [1,x]$ that generates a periodic Syracuse orbit with period $n(\mathbf {M})$ . (This period $n(\mathbf {M})$ could be extremely large, and the periodic orbit could attain values much larger than *x*or *y*, but we will not need any upper bounds on the period in our arguments, other than that it is finite.) The number of possible pairs $(\mathbf {M},\mathbf {m})$ obtained in this fashion is $O(xn_0)$ . By equation ( 5.6), the pair $(\mathbf {M},\mathbf {m})$ uniquely determines $\mathbf {N}_y$ . Thus, outside of the aforementioned event, a periodic orbit is only possible for at most $O(xn_0)$ possible values of $\mathbf {N}_y$ ; as this is much smaller than *y*, we thus see that a periodic orbit is only attained with probability $O(x^{-c})$ , giving the claim. It is then a routine matter to then deduce that almost all positive integers do not lie in a periodic Collatz orbit; we leave the details to the interested reader.

Now we establish equation ( 1.20). By equation ( 1.10), it suffices to show that for $E \subset 2\mathbb {N}+1 \cap [1,x]$ , that

(5.7) $$ \begin{align} \mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) = \left(1 + O( \log^{-c} x )\right) Q + O( \log^{-c} x ) \end{align} $$

for some quantity *Q*that can depend on $x,\alpha ,E$ but is independent of whether *y*is equal to $x^\alpha $ or $x^{\alpha ^2}$ (note that this bound automatically forces $Q = O(1)$ when *x*is large, so the first error term $O(\log ^{-c} x) Q$ on the right-hand side may be absorbed into the second term $O(\log ^{-c} x)$ ). The strategy is to manipulate the left-hand side of equation ( 5.7) into an expression that involves the Syracuse random variables $\mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ for various *n*(in a range $I_y$ depending on *y*) plus a small error, and then appeal to Proposition 1.14 to remove the dependence on *n*and hence on *y*in the main term. The main difficulty is that the first passage location ${\operatorname {Pass}}_x(\mathbf {N}_y)$ involves a first passage time $n = T_x(\mathbf {N}_y)$ whose value is not known in advance; but by stepping back in time by a fixed number of steps $m_0$ , we will be able to express the left-hand side of equation ( 5.7) (up to negligible errors) without having to explicitly refer to the first passage time.

The first step is to establish the following approximate formula for the left-hand side of equation ( 5.7).

### Proposition 5.2 (Approximate formula)

Let $E \subset 2\mathbb {N}+1 \cap [1,x]$ and $y = x^\alpha , x^{\alpha ^2}$ . Then we have

(5.8) $$ \begin{align} \mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) = \sum_{n \in I_y} \sum_{\vec a \in {\mathcal A}^{(n-m_0)}} \sum_{M \in E'} \mathbb{P}( {\operatorname{Aff}}_{\vec a}(\mathbf{N}_y) = M ) + O( \log^{-c} x ) \end{align} $$

where $I_y$ is the interval

(5.9) $$ \begin{align} I_y := \left[\frac{\log( y / x )}{\log \frac{4}{3}} + \log^{0.8} x, \frac{\log( y^\alpha / x )}{\log \frac{4}{3}} - \log^{0.8} x\right]\! , \end{align} $$

$E'$ is the set of odd natural numbers $M \in 2\mathbb {N}+1$ such that $T_x(M) = m_0$ and ${\operatorname {Pass}}_x(M) \in E$ with

(5.10) $$ \begin{align} \exp( - \log^{0.7} x ) (4/3)^{m_0} x \leq M \leq \exp( \log^{0.7} x ) (4/3)^{m_0} x, \end{align} $$

and for any natural number $n'$ , ${\mathcal A}^{(n')} \subset (\mathbb {N}+1)^{n'}$ denotes the set of all tuples $(a_1,\dots ,a_{n'}) \in (\mathbb {N}+1)^{n'}$ such that

(5.11) $$ \begin{align} |a_{[1,n]} - 2n| < \log^{0.6} x \end{align} $$

for all $0 \leq n \leq n'$ .

A key point in the formula in equation ( 5.8) is that the right-hand side does not involve the passage time $T_x(\mathbf {N}_y)$ or the first passage location ${\operatorname {Pass}}_x(\mathbf {N}_y)$ , and the dependence on whether *y*is equal to $x^\alpha $ or $x^{\alpha ^2}$ is confined to the range $I_y$ of the summation variable *n*, as well as the input $\mathbf {N}_y$ of the affine map ${\operatorname {Aff}}_{\vec a}$ . (In particular, note that the set $E'$ does *not*depend on *y*.) We also observe from equations ( 5.9), ( 5.1) and ( 5.2) that $I_y \subset [m_0,n_0]$ , which is consistent with the heuristic in equation ( 5.3).

Proof. Fix *E*, and write $\vec a^{(n_0)}(\mathbf {N}_y) = (\mathbf {a}_1,\dots ,\mathbf {a}_{n_0})$ . From equations ( 5.4) and ( 1.10) and Lemma 2.2, we see that for every $0 \leq n \leq n_0$ , one has

$$ \begin{align*}\mathbb{P}( |\mathbf{a}_{[1,n]} - 2n| \geq \log^{0.6} x ) \ll \exp( - c \log^{0.2} x ).\end{align*} $$

Hence, if ${\mathcal A}^{(n_0)}$ is the set defined in the proposition, we see from the union bound that

(5.12) $$ \begin{align} \mathbb{P}( \vec a^{(n_0)}(\mathbf{N}_y) \not \in {\mathcal A}^{(n_0)} ) \ll \log^{-10} x \end{align} $$

(say); this can be viewed as a rigorous analogue of the heuristic in equation ( 2.5). Hence

$$ \begin{align*}\mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) = \mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E \wedge \vec a^{(n_0)}(\mathbf{N}_y) \in {\mathcal A}^{(n_0)} ) + O( \log^{-c} x ).\end{align*} $$

Suppose that $\vec a^{(n_0)}(\mathbf {N}_y) \in {\mathcal A}^{(n_0)}$ . For any $0 \leq n \leq n_0$ , we have from equations ( 1.7) and ( 1.13) that

$$ \begin{align*}{\operatorname{Syr}}^n(\mathbf{N}_y) = 3^{n} 2^{-\mathbf{a}_{[1,n]}} \mathbf{N}_y + O( 3^{n_0} )\end{align*} $$

and hence by equations ( 5.11) and ( 5.1) and some calculation

(5.13) $$ \begin{align} {\operatorname{Syr}}^n(\mathbf{N}_y) = (1 + O(x^{-0.1})) 3^{n} 2^{-\mathbf{a}_{[1,n]}} \mathbf{N}_y. \end{align} $$

In particular, from equation ( 5.11), one has

(5.14) $$ \begin{align} {\operatorname{Syr}}^n(\mathbf{N}_y) = \exp( O( \log^{0.6} x)) (3/4)^n \mathbf{N}_y \end{align} $$

for all $0 \leq n \leq n_0$ , which can be viewed as a rigorous version of the heuristic in equation ( 1.17). With regards to Figure 1, equation ( 5.14) asserts that the Syracuse orbit stays close to the dashed line.

Figure 1

The Syracuse orbit $n \mapsto \mathrm {Syr}^n(\mathbf {N}_y)$ , where the vertical axis is drawn in shifted log-scale. The diagonal lines have slope $-\log (4/3)$ . For times *n*up to $n_0$ , the orbit usually stays close to the dashed line and hence usually lies between the two dotted diagonal lines; in particular, the first passage time $T_x(\mathbf {N}_y)$ will usually lie in the interval $I_y$ . Outside of a rare exceptional event, for any given $n \in I_y$ , ${\operatorname {Syr}}^{n-m}(\mathbf {N}_y)$ will lie in $E'$ if and only if $n = T_x(\mathbf {N}_y)$ and ${\operatorname {Syr}}^n(\mathbf {N}_y)$ lies in *E*; equivalently, outside of a rare exceptional event, ${\operatorname {Pass}}_x(\mathbf {N}_y)$ lies in *E*if and only if ${\operatorname {Syr}}^{n-m}(\mathbf {N}_y)$ lies in $E'$ for precisely one $n \in I_y$ .

As $T_x(\mathbf {N}_y)$ is the first time *n*for which ${\operatorname {Syr}}^n(\mathbf {N}_y) \leq x$ , the estimate in equation ( 5.14) gives an approximation

(5.15) $$ \begin{align} T_x(\mathbf{N}_y) = \frac{\log( \mathbf{N}_y / x )}{\log \frac{4}{3}} + O( \log^{0.6} x); \end{align} $$

note from equations ( 5.1) and ( 1.18) and a brief calculation that the right-hand side automatically lies between $0$ and $n_0$ if *x*is large enough. In particular, if $I_y$ is the interval in equation ( 5.9), then equation ( 5.14) will imply that $T_x(\mathbf {N}_y) \in I_y$ whenever

$$ \begin{align*}\mathbf{N}_y \subset [y + 2 \log^{0.8} x, y^\alpha - 2 \log^{0.8} x];\end{align*} $$

a straightforward calculation using the integral test (and equation ( 5.12)) then shows that

(5.16) $$ \begin{align} \mathbb{P}( T_x(\mathbf{N}_y) \in I_y) = 1 - O( \log^{-c} x ). \end{align} $$

Again, see Figure 1. Note from equations ( 5.1) and ( 5.2) that $I_y \subset [m_0,n_0]$ ; compare with equation ( 5.3).

Now suppose that *n*is an element of $I_y$ . In particular, $n \geq m_0$ . We observe the following implications:

-

• If $T_x(\mathbf {N}_y) = n$ , then certainly $T_x( {\operatorname {Syr}}^{n-m_0}(\mathbf {N}_y) ) = m_0$ .

-

• Conversely, if $T_x( {\operatorname {Syr}}^{n-m_0}(\mathbf {N}_y) ) = m_0$ and $\vec a^{(n_0)}(\mathbf {N}_y) \in {\mathcal A}^{(n_0)}$ , we have ${\operatorname {Syr}}^n(\mathbf {N}_y) \leq x < {\operatorname {Syr}}^{n-1}(\mathbf {N}_y)$ , which by equation ( 5.14) forces

$$ \begin{align*}n = \frac{\log( \mathbf{N}_y / x )}{\log \frac{4}{3}} + O( \log^{0.6} x),\end{align*} $$

which by equations ( 5.15) and ( 5.2) implies that $T_x(\mathbf {N}_y) \geq n - m_0$ , and hence

$$ \begin{align*}T_x(\mathbf{N}_y) = n - m_0 + T_x({\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y)) = n.\end{align*} $$

We conclude that for any $n \in I_y$ , the event

$$ \begin{align*}\left( T_x(\mathbf{N}_y) = n\right) \wedge \left( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E \right) \wedge \left( \vec a^{(n_0)}(\mathbf{N}_y) \in {\mathcal A}^{(n_0)}\right)\end{align*} $$

holds precisely when the event

$$ \begin{align*}B_{n,y} := \left( T_x( {\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y) ) = m_0\right) \wedge \left({\operatorname{Pass}}_x({\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y)) \in E \right) \wedge \left( \vec a^{(n_0)}(\mathbf{N}_y) \in {\mathcal A}^{(n_0)}\right)\end{align*} $$

does. From equation ( 5.16), we therefore have the estimate

$$ \begin{align*}\mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) = \sum_{n \in I_y} \mathbb{P}(B_{n,y}) + O( \log^{-c} x ). \end{align*} $$

With $E'$ the set defined in the proposition, we observe the following implications:

-

• If $B_{n,y}$ occurs, then from equations ( 5.14) and ( 5.15), we have

$$ \begin{align*}{\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y) = \exp( O( \log^{0.6} x)) (3/4)^{T_x(\mathbf{N}_y)-m_0} \mathbf{N}_y = \exp( O( \log^{0.6} x)) (4/3)^{m_0} x\end{align*} $$

and hence

(5.17) $$ \begin{align} \left( {\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y) \in E'\right) \wedge \left(\vec a^{(n_0)}(\mathbf{N}_y) \in {\mathcal A}^{(n_0)}\right). \end{align} $$

-

• Conversely, if equation ( 5.17) holds, then from equation ( 5.14), we have

$$ \begin{align*}{\operatorname{Syr}}^{n'}(\mathbf{N}_y) = \exp(O(\log^{0.6} x)) (4/3)^{n-m_0-n'} {\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y) \geq \exp(O(\log^{0.6} x)) {\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y)\end{align*} $$

for all $0 \leq n' \leq n-m_0$ , and hence by equation ( 5.10)

$$ \begin{align*}{\operatorname{Syr}}^{n'}(\mathbf{N}_y)> x\end{align*} $$

for all $0 \leq n' \leq n-m_0$ . We conclude that

$$ \begin{align*}{\operatorname{Pass}}_x(\mathbf{N}_y) = n-m_0 + {\operatorname{Pass}}_x({\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y)) = n\end{align*} $$

thanks to the definition of $E'$ , and hence also

$$ \begin{align*}T_x(\mathbf{N}_y) = T_x({\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y)) \in E.\end{align*} $$

In particular, the event $B_{n,y}$ holds.

We conclude that we have the equality of events

$$ \begin{align*}B_{n,y} = \left({\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y) \in E'\right) \wedge \left(\vec a^{(n_0)}(\mathbf{N}_y) \in {\mathcal A}^{(n_0)}\right)\end{align*} $$

for any $n \in I_y$ . Since the event $\vec a^{(n_0)}(\mathbf {N}_y) \in {\mathcal A}^{(n_0)}$ is contained in the event $\vec a^{(n-m_0)}(\mathbf {N}_y) \in {\mathcal A}^{(n-m_0)}$ , we conclude from equation ( 5.12) that

$$ \begin{align*}\mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) = \sum_{n \in I_y} \mathbb{P}\left( \left({\operatorname{Syr}}^{n-m_0}(\mathbf{N}_y) \in E'\right) \wedge \left(\vec a^{(n-m_0)}(\mathbf{N}_y) \in {\mathcal A}^{(n-m_0)}\right) \right) + O( \log^{-c} x ).\end{align*} $$

Suppose that $\vec a = (a_1,\dots ,a_{n-m})$ is a tuple in ${\mathcal A}^{(n-m)}$ , and $M \in E'$ . From Lemma 2.1, we see that the event $\left ({\operatorname {Syr}}^{n-m_0}(\mathbf {N}_y) = M\right ) \wedge \left (\vec a^{(n-m_0)}(\mathbf {N}_y) = \vec a\right )$ holds if and only if ${\operatorname {Aff}}_{\vec a}( \mathbf {N}_y) \in E'$ , and the claim in equation ( 5.8) follows.

Now we compute the right-hand side of equation ( 5.8). Let $n \in I_y$ , $\vec a \in {\mathcal A}^{(n-m_0)}$ , and $M \in E'$ . Then by equation ( 1.3), the event ${\operatorname {Aff}}_{\vec a}(\mathbf {N}_y) = M$ is only non-empty when

(5.18) $$ \begin{align} M = F_{n-m_0}(\vec a) \bmod 3^{n-m_0}. \end{align} $$

Conversely, if equation ( 5.18) holds, then ${\operatorname {Aff}}_{\vec a}(\mathbf {N}_y) = M$ holds precisely when

(5.19) $$ \begin{align} \mathbf{N}_y = 2^{|\vec a|} \frac{M - F_{n-m_0}(\vec a)}{3^{n-m_0}}. \end{align} $$

Note from equations ( 5.11) and ( 1.13) that the right-hand side of equation ( 5.19) is equal to

$$ \begin{align*}2^{2(n-m_0)+O(\log^{0.6} x)} \frac{M + O( 3^{n-m_0} )}{3^{n-m_0}},\end{align*} $$

which by equations ( 5.10) and ( 5.1) simplifies to

$$ \begin{align*}\exp( O(\log^{0.7} x)) (4/3)^{n} x.\end{align*} $$

Since $n \in I_y$ , we conclude from equation ( 5.9) that the right-hand side of equation ( 5.19) lies in $[y, y^\alpha ]$ ; from equations ( 5.18) and ( 1.5), we also see that this right-hand side is a odd integer. Since $\mathbf {N}_y \equiv \mathbf {Log}( 2\mathbb {N}+1 \cap [y,y^\alpha ] )$ and

$$ \begin{align*}\sum_{N \in 2\mathbb{N}+1 \cap [y,y^\alpha]} \frac{1}{N} = \left(1 + O\left( \frac{1}{x}\right)\right) \frac{\alpha-1}{2} \log y,\end{align*} $$

we thus see that when equation ( 5.18) occurs, one has

$$ \begin{align*}\mathbb{P}( {\operatorname{Aff}}_{\vec a}(\mathbf{N}_y) = M ) = \frac{1}{\left(1 + O( \frac{1}{x})\right)\frac{\alpha-1}{2} \log y} 2^{-|\vec a|} \frac{3^{n-m_0}}{M - F_{n-m_0}(\vec a)}.\end{align*} $$

From equations ( 5.10), ( 5.1) and ( 1.13), we can write

$$ \begin{align*}M - F_{n-m_0}(\vec a) = M - O(3^{n_0}) = (1 + O(x^{-c})) M\end{align*} $$

and thus

$$ \begin{align*}\mathbb{P}( {\operatorname{Aff}}_{\vec a}(\mathbf{N}_y) = M ) = \frac{1 + O(x^{-c})}{\frac{\alpha-1}{2} \log y} \frac{2^{-|\vec a|} 3^{n-m_0}}{M}.\end{align*} $$

We conclude that

$$ \begin{align*} \mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) &= \frac{1 + O(x^{-c})}{\frac{\alpha-1}{2} \log y} \sum_{n \in I_y} 3^{n-m_0} \sum_{\vec a \in {\mathcal A}^{(n-m_0)}} 2^{-|\vec a|} \sum_{M \in E': M = F_{n-m_0}(\vec a) \bmod 3^{n-m_0}} \frac{1}{M} \\ &\quad + O( \log^{-c} x ). \end{align*} $$

We will eventually establish the estimate

(5.20) $$ \begin{align} 3^{n-m_0} \sum_{\vec a \in {\mathcal A}^{(n-m_0)}} 2^{-|\vec a|} \sum_{M \in E': M = F_{n-m_0}(\vec a) \bmod 3^{n-m_0}} \frac{1}{M} = Z + O( \log^{-c} x ) \end{align} $$

for all $n \in I_y$ , where *Z*is the quantity

(5.21) $$ \begin{align} Z := \sum_{M \in E'} \frac{3^{m_0} \mathbb{P}( M = \mathbf{Syrac}(\mathbb{Z}/3^{m_0}\mathbb{Z}) \bmod 3^{m_0})}{M}. \end{align} $$

Since from equation ( 5.9), we have

$$ \begin{align*}\# I_y = (1 + O( \log^{-c} x )) \frac{\alpha-1}{\log \frac{4}{3}} \log y,\end{align*} $$

we see that equation ( 5.20) would imply the bound

$$ \begin{align*}\mathbb{P}( {\operatorname{Pass}}_x( \mathbf{N}_y ) \in E ) = (1 + O(\log^{-c} x)) \frac{2}{\log \frac{4}{3}} Z + O(\log^{-c} x)\end{align*} $$

which would give the desired estimate in equation ( 5.7) since *Z*does not depend on whether *y*is equal to $x^\alpha $ or $x^{\alpha ^2}$ .

It remains to establish equation ( 5.20). Fix $n \in I_y$ . The left-hand side of equation ( 5.20) may be written as

(5.22) $$ \begin{align} \mathbb{E} 1_{(\mathbf{a}_1,\dots,\mathbf{a}_{n-m_0}) \in {\mathcal A}^{(n-m_0)}} c_n( F_{n-m_0}(\mathbf{a}_1,\dots,\mathbf{a}_{n-m_0}) \bmod 3^{n-m_0} ), \end{align} $$

where $(\mathbf {a}_1,\dots ,\mathbf {a}_{n-m_0}) \equiv \mathbf {Geom}(2)^{n-m_0}$ and $c_n\colon \mathbb {Z}/3^{n-m_0}\mathbb {Z} \to \mathbb {R}^+$ is the function

(5.23) $$ \begin{align} c_n( X ) := 3^{n-m_0} \sum_{M \in E': M = X \bmod 3^{n-m_0}} \frac{1}{M}. \end{align} $$

We have a basic estimate:

Lemma 5.3. We have $c_n(X) \ll 1$ for all $n \in I_y$ and $X \in \mathbb {Z}/3^{n-m_0}\mathbb {Z}$ .

Proof. We can split

$$ \begin{align*}c_n(X) \leq \sum_{(a_1,\dots,a_{m_0}) \in \mathbb{N}^{m_0}} c_{n,a_1,\dots,a_{m_0}}(X),\end{align*} $$

where

$$ \begin{align*}c_{n,a_1,\dots,a_{m_0}}(X) := 3^{n-m_0} \sum_{M \in E': M = X \bmod 3^{n-m_0}; (a_1,\dots,a_{m_0}) := \vec a^{(m_0)}(M)} \frac{1}{M}.\end{align*} $$

We now estimate $c_{n,a_1,\dots ,a_{m_0}}(X)$ for a given $(a_1,\dots ,a_{m_0}) \in \mathbb {N}^{m_0}$ . If $M \in E'$ , then on setting $(a_1,\dots ,a_{m_0}) := \vec a^{(m_0)}(M)$ , we see from equation ( 1.7) that

$$ \begin{align*}3^{m_0} 2^{-a_{[1,m_0]}} M + F_{m_0}(a_1,\dots,a_{m_0}) \leq x < 3^{m_0} 2^{-a_{[1,m_0-1]}} M + F_{m_0-1}(a_1,\dots,a_{m_0-1})\end{align*} $$

which by equations ( 5.2) and ( 1.13) implies that

$$ \begin{align*}3^{m_0} 2^{-a_{[1,m_0]}} M \leq x \ll 3^{m_0} 2^{-a_{[1,m_0-1]}} M\end{align*} $$

or equivalently

(5.24) $$ \begin{align} 3^{-m_0} 2^{a_{[1,m_0-1]}} x \ll M \leq 3^{-m_0} 2^{a_{[1,m_0]}} x. \end{align} $$

Also, from equation ( 1.7), we have that

$$ \begin{align*}3^{m_0} M + 2^{a_{[1,m_0]}} F_{m_0}(a_1,\dots,a_{m_0}) = 2^{a_{[1,m_0]}} \bmod 2^{a_{[1,m_0]}+1}\end{align*} $$

and so *M*is constrained to a single residue class modulo $2^{a_{[1,m_0]}+1}$ . In equation ( 5.23), we are also constraining *M*to a single residue class modulo $3^{n-m_0}$ ; by the Chinese remainder theorem, these constraints can be combined into a single residue class modulo $2^{a_{[1,m_0]}+1} 3^{n-m_0}$ . Note from the integral test that

(5.25) $$ \begin{align} \sum_{M_0 \leq M \leq M_1: M = a \bmod q} \frac{1}{M} &\leq \frac{1}{M_0} + \sum_{M_0+q \leq M \leq M_1: M = a \bmod q} \frac{1}{M} \nonumber\\ &\leq \frac{1}{M_0} + \frac{1}{q} \int_{M_0}^{M_1} \frac{dt}{t} \nonumber\\ &= \frac{1}{M_0} + \frac{1}{q} \log \frac{M_1}{M_0} \end{align} $$

for any $M_0 \leq M_1$ and any residue class $a \bmod q$ . In particular, for $q \leq M_0$ , we have

(5.26) $$ \begin{align} \sum_{M_0 \leq M \leq M_1: M = a \bmod q} \frac{1}{M} \ll \frac{1}{q} \log O \left( \frac{M_1}{M_0} \right). \end{align} $$

If $2^{a_{[1,m_0]}} \leq x^{0.5}$ (say), then the modulus $2^{a_{[1,m_0]}+1} 3^{n-m_0}$ is much less than the lower bound on *M*in equation ( 5.24), and we can then use the integral test to bound

$$ \begin{align*} c_{n,a_1,\dots,a_{m_0}}(X) & \ll 3^{n-m_0} (2^{a_{[1,m_0]}+1} 3^{n-m_0})^{-1} \log O \left( \frac{3^{-m_0} 2^{a_{[1,m_0]}} x}{3^{-m_0} 2^{a_{[1,m_0-1]}} x } \right)\\ &\ll 2^{-a_{[1,m_0]}} a_{m_0} \\ &\ll 2^{-a_{[1,m_0]}/2}. \end{align*} $$

Now suppose instead that $2^{a_{[1,m_0]}}> x^{0.5}$ ; we recall from equation ( 1.7) that

$$ \begin{align*}a_{m_0} = \nu_2\left( 3 (3^{m_0} 2^{-a_{[1,m_0-1]}} M + F_{m_0-1}(a_1,\dots,a_{m_0-1})) + 1\right)\end{align*} $$

so

$$ \begin{align*}2^{a_{m_0}} \ll 3^{m_0} 2^{-a_{[1,m_0-1]}} M + F_{m_0-1}(a_1,\dots,a_{m_0-1}) \ll 3^{m_0} 2^{-a_{[1,m_0-1]}} M\end{align*} $$

(using equations ( 1.13) and ( 5.24) to handle the lower order term). Hence we we have the additional lower bound

$$ \begin{align*}M \gg 3^{-m_0} 2^{a_{[1,m_0]}}.\end{align*} $$

Applying equation ( 5.25) with $M_0$ equal to the larger of the two lower bounds on *M*, we conclude that

$$ \begin{align*} c_{n,a_1,\dots,a_{m_0}}(X) & \ll \frac{3^{n-m_0}}{3^{-m_0} 2^{a_{[1,m_0]}}} + 3^{n-m_0} (2^{a_{[1,m_0]}+1} 3^{n-m_0})^{-1} \log O \left( \frac{3^{-m_0} 2^{a_{[1,m_0]}} x}{3^{-m_0} 2^{a_{[1,m_0-1]}} x } \right)\\ &\ll 3^n 2^{-a_{[1,m_0]}} + 2^{-a_{[1,m_0]}} a_{m_0}\\ &\ll 2^{-a_{[1,m_0]}/2} \end{align*} $$

since $2^{-a_{[1,m_0]}} \leq x^{-1/4} 2^{-a_{[1,m_0]}/2} \leq 3^{-n} 2^{-a_{[1,m_0]}/2}$ for $n \in I_y$ . Thus we have

$$ \begin{align*}c_n(X) \ll \sum_{a_1,\dots,a_{m_0} \in \mathbb{N}} 2^{-a_{[1,m_0]}/2}\end{align*} $$

and the claim follows from summing the geometric series.

From the above lemma and equation ( 5.12), we may write equation ( 5.22) as

$$ \begin{align*}\mathbb{E} c_n( F_{n-m_0}(\mathbf{a}_1,\dots,\mathbf{a}_{n-m_0}) \bmod 3^{n-m_0} ) + O( \log^{-c} x )\end{align*} $$

which by equation ( 1.22) is equal to

$$ \begin{align*}\sum_{X \in \mathbb{Z}/3^{n-m_0}\mathbb{Z}} c_n(X) \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^{n-m_0}\mathbb{Z}) = X ) + O( \log^{-c} x ).\end{align*} $$

From equations ( 5.9) and ( 5.2), we have $n-m_0 \geq m_0$ . Applying Proposition 1.14, Lemma 5.3 and the triangle inequality, one can thus write the preceding expression as

$$ \begin{align*}\sum_{X \in \mathbb{Z}/3^{n-m_0}\mathbb{Z}} c_n(X) 3^{2m_0-n} \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^{m_0}\mathbb{Z}) = X \bmod 3^{m_0}) + O( \log^{-c} x )\end{align*} $$

and the claim in equation ( 5.20) then follows from equation ( 5.23).

## 6 Reduction to Fourier decay bound

In this section, we derive Proposition 1.14 from Proposition 1.17. We first observe that to prove Proposition 1.14, it suffices to do so in the regime

(6.1) $$ \begin{align} 0.9 n \leq m \leq n. \end{align} $$

(The main significance of the constant $0.9$ here is that it lies between $\frac {\log 3}{2\log 2} \approx 0.7925$ and $1$ .) Indeed, once one has equation ( 1.26) in this regime, one also has from equation ( 1.23) that

$$ \begin{align*}\sum_{Y \in \mathbb{Z}/3^{n'}\mathbb{Z}} \left|3^{n-n'} \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) = Y \bmod 3^n ) - 3^{m-n'} \mathbb{P}( \mathbf{Syrac}(\mathbb{Z}/3^n\mathbb{Z}) = Y \bmod 3^m ) \right| \ll_A m^{-A} \end{align*} $$

whenever $0.9 n \leq m \leq n \leq n'$ , and the claim in equation ( 1.26) for general $10 \leq m \leq n$ then follows from telescoping series, with the remaining cases $1 \leq m < 10$ following trivially from the triangle inequality.

Henceforth we assume equation ( 6.1). We also fix $A>0$ , and let $C_A$ be a constant that is sufficiently large depending on *A*. We may assume that *n*(and hence *m*) are sufficiently large depending on $A,C_A$ , since the claim is trivial otherwise.

Let $(\mathbf {a}_1,\dots ,\mathbf {a}_n) \equiv \mathbf {Geom}(2)^n$ , and define the random variable

$$ \begin{align*}\mathbf{X}_n := 2^{-\mathbf{a}_1} + 3^1 2^{-\mathbf{a}_{[1,2]}} + \dots + 3^{n-1} 2^{-\mathbf{a}_{[1,n]}} \bmod 3^n,\end{align*} $$

thus $\mathbf {X}_n \equiv \mathbf {Syrac}(\mathbb {Z}/3^n\mathbb {Z})$ . The strategy will be to split $\mathbf {X}_n$ (after some conditioning and removal of exceptional events) as the sum of two independent components, one of which has quite large entropy (or more precisely, Renyi $2$ -entropy) in $\mathbb {Z}/3^n\mathbb {Z}$ thanks to some elementary number theory, and the other having very small Fourier coefficients at high frequencies thanks to Proposition 1.17. The desired bound will then follow from some $L^2$ -based Fourier analysis (i.e., Plancherel’s theorem).

We turn to the details. Let *E*denote the event that the inequalities

(6.2) $$ \begin{align} |\mathbf{a}_{[i,j]} - 2(j-i)| \leq C_A ( \sqrt{(j-i)(\log n)} + \log n ) \end{align} $$

hold for every $1 \leq i \leq j \leq n$ . The event *E*occurs with nearly full probability; indeed, from Lemma 2.2 and the union bound, we can bound the probability of the complementary event $\overline {E}$ by

(6.3) $$ \begin{align} \mathbb{P}( \overline{E}) &\ll \sum_{1 \leq i \leq j \leq n} G_{j-i}( c C_A ( \sqrt{(j-i)(\log n)} + \log n ) ) \nonumber\\ &\ll \sum_{1 \leq i \leq j \leq n} \exp( - c C_A \log n ) + \exp( - c C_A \log n) \nonumber\\ &\ll n^2 n^{-c C_A} \nonumber\\ &\ll n^{-A-1} \end{align} $$

if $C_A$ is large enough. By the triangle inequality, we may then bound the left-hand side of equation ( 1.26) by

$$ \begin{align*}{\operatorname{Osc}}_{m,n}\left( \mathbb{P}( (\mathbf{X}_n = Y) \wedge E ) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}} + O(n^{-A-1}),\end{align*} $$

so it now suffices to show that

$$ \begin{align*}{\operatorname{Osc}}_{m,n}\left( \mathbb{P}( (\mathbf{X}_n = Y) \wedge E ) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \ll_{A,C_A} n^{-A}.\end{align*} $$

Now suppose that *E*holds. From equation ( 6.2), we have

$$ \begin{align*}\mathbf{a}_{[1,n]} \geq 2(n-1) - C_A (\sqrt{n \log n} + \log n)> n \frac{\log 3}{\log 2}\end{align*} $$

since $\frac {\log 3}{\log 2} < 2$ and *n*is large. Thus, there is a well-defined *stopping time*$0 \leq \mathbf {k} < n$ , defined as the unique natural number $\mathbf {k}$ for which

$$ \begin{align*}\mathbf{a}_{[1,\mathbf{k}]} \leq n \frac{\log 3}{\log 2} - (C_A)^2 \log n < \mathbf{a}_{[1,\mathbf{k}+1]}.\end{align*} $$

From equation ( 6.2), we have

$$ \begin{align*}\mathbf{k} = n \frac{\log 3}{2 \log 2} + O( C_A \sqrt{n\log n} ).\end{align*} $$

It thus suffices by the union bound to show that

(6.4) $$ \begin{align} {\operatorname{Osc}}_{m,n}\left( \mathbb{P}( (\mathbf{X}_n = Y) \wedge E \wedge B_k) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \ll_{A,C_A} n^{-A-1} \end{align} $$

for all

(6.5) $$ \begin{align} k = n \frac{\log 3}{2 \log 2} + O( C_A \sqrt{n \log n} ), \end{align} $$

where $B_k$ is the event that $\mathbf {k}=k$ , or equivalently that

(6.6) $$ \begin{align} \mathbf{a}_{[1,k]}\leq n \frac{\log 3}{\log 2} - (C_A)^2 \log n < \mathbf{a}_{[1,k+1]}. \end{align} $$

Fix *k*. In order to decouple the events involved in equation ( 6.4), we need to enlarge the event *E*slightly, so that it only depends on $\mathbf {a}_1,\dots ,\mathbf {a}_{k+1}$ and not on $\mathbf {a}_{k+2},\dots ,\mathbf {a}_n$ . Let $E_k$ denote the event that the inequalities in equation ( 6.2) hold for $1 \leq i < j \leq k+1$ ; thus $E_k$ contains *E*. Then the difference between *E*and $E_k$ has probability $O(n^{-A-1})$ by in equation ( 6.3). Thus by the triangle inequality, the estimate in equation ( 6.4) is equivalent to

$$ \begin{align*}{\operatorname{Osc}}_{m,n}\left( \mathbb{P}( (\mathbf{X}_n = Y) \wedge E_k \wedge B_k ) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \ll_{A,C_A} n^{-A-1}.\end{align*} $$

From equations ( 6.6) and ( 6.2), we see that we have

(6.7) $$ \begin{align} n \frac{\log 3}{\log 2} - (C_A)^2 \log n \leq \mathbf{a}_{[1,k+1]} \leq n \frac{\log 3}{\log 2} - \frac{1}{2} (C_A)^2 \log n \end{align} $$

whenever one is in the event $E_k \wedge B_k$ . By a further application of the triangle inequality, it suffices to show that

$$ \begin{align*}{\operatorname{Osc}}_{m,n}\left( \mathbb{P}( (\mathbf{X}_n = Y) \wedge E_k \wedge B_k \wedge C_{k,l} ) \right)_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \ll_{A,C_A} n^{-A-2} \end{align*} $$

for all *l*in the range

(6.8) $$ \begin{align} n \frac{\log 3}{\log 2} - (C_A)^2 \log n \leq l \leq n \frac{\log 3}{\log 2} - \frac{1}{2} (C_A)^2 \log n, \end{align} $$

where $C_{k,l}$ is the event that $\mathbf {a}_{[1,k+1]}=l$ .

Fix *l*. If we let $g = g_{n,k,l}\colon \mathbb {Z}/3^n\mathbb {Z} \to \mathbb {R}$ denote the function

(6.9) $$ \begin{align} g(Y) = g_{n,k,l}(Y) := \mathbb{P}( (\mathbf{X}_n = Y) \wedge E_k \wedge B_k \wedge C_{k,l}), \end{align} $$

then our task can be written as

$$ \begin{align*}\sum_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \left|g(Y) - \frac{1}{3^{n-m}} \sum_{Y' \in \mathbb{Z}/3^n\mathbb{Z}: Y' = Y \bmod 3^m} g(Y') \right| \ll_{A,C_A} n^{-A-2}.\end{align*} $$

By Cauchy-Schwarz, it suffices to show that

(6.10) $$ \begin{align} 3^{n} \sum_{Y \in \mathbb{Z}/3^n\mathbb{Z}} \left|g(Y) - \frac{1}{3^{n-m}} \sum_{Y' \in \mathbb{Z}/3^n\mathbb{Z}: Y' = Y \bmod 3^m} g(Y') \right|{}^2 \ll_{A,C_A} n^{-2A-4}. \end{align} $$

By the Fourier inversion formula, we have

$$ \begin{align*}g(Y) = 3^{-n} \sum_{\xi \in \mathbb{Z}/3^n\mathbb{Z}} \left( \sum_{Y' \in \mathbb{Z}/3^n\mathbb{Z}} g(Y') e^{-2\pi i \xi Y' / 3^n} \right) e^{2\pi i \xi Y/3^n}\end{align*} $$

and

$$ \begin{align*}\frac{1}{3^{n-m}} \sum_{Y' \in \mathbb{Z}/3^n\mathbb{Z}: Y' = Y \bmod 3^m} g(Y') = 3^{-n} \sum_{\xi \in 3^{n-m}\mathbb{Z}/3^n\mathbb{Z}} \left( \sum_{Y' \in \mathbb{Z}/3^n\mathbb{Z}} g(Y') e^{-2\pi i \xi Y' / 3^n} \right) e^{2\pi i \xi Y/3^n}\end{align*} $$

for any $Y \in \mathbb {Z}/3^n\mathbb {Z}$ , so by Plancherel’s theorem, the left-hand side of equation ( 6.10) may be written as

$$ \begin{align*}\sum_{\xi \in \mathbb{Z}/3^n\mathbb{Z}: \xi \not \in 3^{n-m}\mathbb{Z}/3^n\mathbb{Z}} \left| \sum_{Y \in \mathbb{Z}/3^n\mathbb{Z}} g(Y) e^{-2\pi i \xi Y / 3^n} \right|{}^2.\end{align*} $$

By equation ( 6.9), we can write

$$ \begin{align*}\sum_{Y \in \mathbb{Z}/3^n\mathbb{Z}} g(Y) e^{-2\pi i \xi Y / 3^n} = \mathbb{E} e^{-2\pi i \xi \mathbf{X}_n / 3^n} 1_{E_k \wedge B_k \wedge C_{k,l}}.\end{align*} $$

On the event $C_{k,l}$ , one can use equations ( 1.5) and ( 1.29) to write

$$ \begin{align*}\mathbf{X}_n = F_{k+1}(\mathbf{a}_{k+1},\dots,\mathbf{a}_1) + 3^{k+1} 2^{-l} F_{n-k-1}(\mathbf{a}_n,\dots,\mathbf{a}_{k+2}) \bmod 3^n.\end{align*} $$

The key point here is that the random variable $3^{k+1} 2^{-l} F_{n-k-1}(\mathbf {a}_n,\dots ,\mathbf {a}_{k+2})$ is independent of $\mathbf {a}_1,\dots ,\mathbf {a}_{k+1}, E_k, B_k, C_{k,l}$ . Thus we may factor

$$ \begin{align*} \sum_{Y \in \mathbb{Z}/3^n\mathbb{Z}} g(Y) e^{-2\pi i \xi Y / 3^n} &= \mathbb{E} e^{-2\pi i \xi (F_{k+1}(\mathbf{a}_{k+1},\dots,\mathbf{a}_1) \bmod 3^n) / 3^n} 1_{E_k \wedge B_k \wedge C_{k,l}} \\ &\quad \times \mathbb{E} e^{-2\pi i \xi (2^{-l} F_{n-k-1}(\mathbf{a}_n,\dots,\mathbf{a}_{k+2}) \bmod 3^{n-k-1}) / 3^{n-k-1}}. \end{align*} $$

For $\xi $ in $\mathbb {Z}/3^n\mathbb {Z}$ that does not lie in $3^{n-m}\mathbb {Z}/3^n\mathbb {Z}$ , we can write $\xi = 3^j 2^l \xi ' \bmod 3^n$ , where $0 \leq j < n-m \leq 0.1 n$ and $\xi '$ is not divisible by $3$ . In particular, from equation ( 6.5), one has

$$ \begin{align*}n-k-j-1 \geq 0.9 n - n \frac{\log 3}{2 \log 2} - O(C_A \sqrt{n \log n}) - 1 \gg n.\end{align*} $$

Then by equation ( 1.23), we have

$$ \begin{align*}\mathbb{E} e^{-2\pi i \xi (2^{-l} F_{n-k-1}(\mathbf{a}_n,\dots,\mathbf{a}_{k+2}) \bmod 3^{n-k-1}) / 3^{n-k-1}} = \mathbb{E} e^{-2\pi i \xi' \mathbf{Syrac}(\mathbb{Z}/3^{n-k-j-1}\mathbb{Z}) / 3^{n-k-j-1}} \end{align*} $$

and hence by Proposition 1.17 this quantity is $O_{A'}(n^{-A'})$ for any $A'$ . Thus we can bound the left-hand side of equation ( 6.10) by

(6.11) $$ \begin{align} \ll_{A'} n^{-2 A'} \sum_{\xi \in \mathbb{Z}/3^n\mathbb{Z}} \left|\mathbb{E} e^{-2\pi i \xi (F_{k+1}(\mathbf{a}_{k+1},\dots,\mathbf{a}_1) \bmod 3^n) / 3^n} 1_{\overline{E}_k \wedge B_k \wedge C_{k,l}} \right|{}^2 \end{align} $$

(where we have now discarded the restriction $\xi \not \in 3^{n-m}\mathbb {Z}/3^n\mathbb {Z}$ ); by Plancherel’s theorem, this expression can be written as

$$ \begin{align*}\ll_{A'} n^{-2 A'} 3^n \sum_{Y_{k+1} \in \mathbb{Z}/3^n\mathbb{Z}} \mathbb{P} ( (F_{k+1}(\mathbf{a}_{k+1},\dots,\mathbf{a}_1) = Y_{k+1}) \wedge E_k \wedge B_k \wedge C_{k,l} )^2.\end{align*} $$

Remark 6.1. If we ignore the technical restriction to the events $E_k, B_k, C_{k,l}$ , this quantity is essentially the Renyi $2$ -entropy (also known as *collision entropy*) of the random variable $F_{k+1}(\mathbf {a}_{k+1},\dots ,\mathbf {a}_1) \bmod 3^n$ .

Now we make a key elementary number theory observation:

### Lemma 6.2 (Injectivity of offsets)

For each natural number *n*, the *n*-Syracuse offset map $F_n\colon (\mathbb {N}+1)^n \to \mathbb {Z}[\frac {1}{2}]$ is injective.

Proof. Suppose that $(a_1,\dots ,a_n), (a^{\prime }_1,\dots ,a^{\prime }_n) \in (\mathbb {N}+1)^n$ are such that $F_n(a_1,\dots ,a_n) = F_n(a^{\prime }_1,\dots ,a^{\prime }_n)$ . Taking $2$ -valuations of both sides using equation ( 1.5), we conclude that

$$ \begin{align*}- a_{[1,n]} = - a^{\prime}_{[1,n]}.\end{align*} $$

On the other hand, from equation ( 1.5), we have

$$ \begin{align*}F_n(a_1,\dots,a_n) = 3^n 2^{-a_{[1,n]}} + F_{n-1}(a_2,\dots,a_n)\end{align*} $$

and similarly for $a^{\prime }_1,\dots ,a^{\prime }_n$ , hence

$$ \begin{align*}F_{n-1}(a_2,\dots,a_n) = F_{n-1}(a^{\prime}_2,\dots,a^{\prime}_n).\end{align*} $$

The claim now follows from iteration (or an induction on *n*).

We will need a more quantitative $3$ -adic version of this injectivity:

### Corollary 6.3 $3$ -adic separation of offsets

Let $C_A$ be sufficiently large, let *n*be sufficiently large (depending on $C_A$ ), let *k*be a natural number, and let *l*be a natural number obeying equation ( 6.8). Then the residue classes $F_{k+1}(a_{k+1},\dots ,a_1) \bmod 3^n$ , as $(a_1,\dots ,a_{k+1}) \in (\mathbb {N}+1)^{k+1}$ range over ${k+1}$ -tuples of positive integers that obey the conditions

(6.12) $$ \begin{align} |a_{[i+1,j]} - 2(j-i)| \leq C_A \left( \sqrt{(j-i)(\log n)} + \log n \right) \end{align} $$

for $1 \leq i < j \leq k+1$ as well as

(6.13) $$ \begin{align} a_{[1,k+1]} = l, \end{align} $$

are distinct.

Proof. Suppose that $(a_1,\dots ,a_{k+1}), (a^{\prime }_1,\dots ,a^{\prime }_{k+1})$ are two tuples of positive integers that both obey equations ( 6.12) and ( 6.13), and such that

$$ \begin{align*}F_{k+1}(a_{k+1},\dots,a_1) = F_{k+1}(a^{\prime}_{k+1},\dots,a^{\prime}_1) \bmod 3^n.\end{align*} $$

Applying equation ( 1.5) and multiplying by $2^l$ , we conclude that

(6.14) $$ \begin{align} \sum_{j=1}^{k+1} 3^{j-1} 2^{l - a_{[1,j]}} = \sum_{j=1}^{k+1} 3^{j-1} 2^{l - a^{\prime}_{[1,j]}} \bmod 3^n. \end{align} $$

From equation ( 6.13), the expressions on the left and right sides are natural numbers. Using equations ( 6.12) and ( 6.8), and Young’s inequality $C_A j^{1/2} \log ^{1/2} n \leq \frac {\varepsilon }{2} j + \frac {1}{2\varepsilon } C_A^2 \log n$ for a sufficiently small $\varepsilon>0$ , the left-hand side may be bounded for $C_A$ large enough by

$$ \begin{align*} \sum_{j=1}^{k+1} 3^{j-1} 2^{l - a_{[1,j]}} &\ll 2^l \sum_{j=1}^{k+1} 3^{j} 2^{- 2j + C_A (\sqrt{j \log n} + \log n)} \\ &\ll \exp( - \frac{(C_A)^2}{2} \log n ) 3^n \sum_{j=1}^{k+1} \exp\left( - j \log \frac{4}{3} + O( C_A j^{1/2} \log^{1/2} n ) + O( C_A \log n ) \right) \\ &\ll \exp\left( - \frac{(C_A)^2}{4} \log n \right) 3^n \sum_{j=1}^{k+1} \exp( - c j ) \\ &\ll n^{- \frac{(C_A)^2}{4}} 3^n; \end{align*} $$

in particular, for *n*large enough, this expression is less than $3^n$ . Similarly for the right-hand side of equation ( 6.14). Thus these two sides are equal as natural numbers, not simply as residue classes modulo $3^n$ :

(6.15) $$ \begin{align} \sum_{j=1}^{k+1} 3^{j-1} 2^{l-a_{[1,j]}} = \sum_{j=1}^{k+1} 3^{j-1} 2^{l-a^{\prime}_{[1,j]}}. \end{align} $$

Dividing by $2^l$ , we conclude $F_{k+1}(a_{k+1},\dots ,a_1) = F_{k+1}(a^{\prime }_{k+1},\dots ,a^{\prime }_1)$ . From Lemma 6.2, we conclude that $(a_1,\dots ,a_{k+1}) = (a^{\prime }_1,\dots ,a^{\prime }_{k+1})$ , and the claim follows.

In view of the above lemma, we see that for a given choice of $Y_{k+1} \in \mathbb {Z}/3^n\mathbb {Z}$ , the event

$$ \begin{align*}(F_{k+1}(\mathbf{a}_{k+1},\dots,\mathbf{a}_1) = Y_{k+1}) \wedge E_k \wedge B_k \wedge C_{k,l}\end{align*} $$

can only be non-empty for at most one value $(a_1,\dots ,a_{m})$ of the tuple $(\mathbf {a}_1,\dots ,\mathbf {a}_{m})$ . By Definition 1.7, such a value is attained with probability $2^{-a_{[1,m]}} = 2^{-l}$ , which by equation ( 6.8) is equal to $n^{O((C_A)^2)} 3^{-n}$ . We can thus bound equation ( 6.11) (and hence the left-hand side of equation ( 6.10)) by

$$ \begin{align*}\ll_{A'} n^{-2 A' + O( (C_A)^2 ) },\end{align*} $$

and the claim now follows by taking $A'$ large enough. This concludes the proof of Proposition 1.14 assuming Proposition 1.17.

## 7 Decay of Fourier coefficients

In this section, we establish Proposition 1.17, which, when combined with all the implications established in preceding sections, will yield Theorem 1.3.

Let $n \geq 1$ , let $\xi \in \mathbb {Z}/3^n\mathbb {Z}$ be not divisible by $3$ , and let $A>0$ be fixed. We will not vary *n*or $\xi $ in this argument, but it is important that all of our estimates are uniform in these parameters. Without loss of generality we may assume *A*to be larger than any fixed absolute constant. We let $\chi = \chi _{n,\xi } \colon \mathbb {Z}[\frac {1}{2}] \to \mathbb {C}$ denote the character

(7.1) $$ \begin{align} \chi(x) := e^{-2\pi i \xi (x \bmod 3^n) / 3^n}, \end{align} $$

where $x \mapsto x \bmod 3^n$ is the ring homomorphism from $\mathbb {Z}[\frac {1}{2}]$ to $\mathbb {Z}/3^n\mathbb {Z}$ (mapping $\frac {1}{2}$ to $\frac {1}{2} \bmod 3^n = \frac {3^n+1}{2} \bmod 3^n$ ). Note that $\chi $ is a group homomorphism from the additive group $\mathbb {Z}[\frac {1}{2}]$ to the multiplicative group $\mathbb {C}$ , which is periodic modulo $3^n$ , so it also descends to a group homomorphism from $\mathbb {Z}/3^n\mathbb {Z}$ to $\mathbb {C}$ , which is still defined by the same formula in equation equation ( 7.1). From equation ( 1.29), our task now reduces Footnote 7 to establishing the following claim.

### Proposition 7.1 (Key Fourier decay estimate)

Let $\chi $ be defined by equation ( 7.1), and let $(\mathbf {a}_1,\dots ,\mathbf {a}_n) \equiv \mathbf {Geom}(2)^n$ be *n*iid copies of the geometric distribution $\mathbf {Geom}(2)$ (as defined in Definition 1.7). Then the quantity

(7.2) $$ \begin{align} S_\chi(n) := \mathbb{E} \chi( 2^{-\mathbf{a}_1} + 3^1 2^{-\mathbf{a}_{[1,2]}} + \dots + 3^{n-1} 2^{-\mathbf{a}_{[1,n]}} ) \end{align} $$

obeys the estimate

(7.3) $$ \begin{align} S_\chi(n) \ll_A n^{-A} \end{align} $$

for any $A>0$ , where we use the summation convention $\mathbf {a}_{[i,j]} := \mathbf {a}_i + \dots + \mathbf {a}_j$ from equation ( 1.6).

### 7.1 Estimation in terms of white points

To extract some usable cancellation in the expression $S_\chi (n)$ , we will group the sum on the left-hand side into pairs. For any real $x>0$ , let $[x]$ denote the discrete interval

$$ \begin{align*}[x] := \{j \in \mathbb{N}+1: j \leq x \} = \{ 1, \dots, \lfloor x\rfloor\}.\end{align*} $$

For $j \in [n/2]$ , set $\mathbf {b}_j := \mathbf {a}_{2j-1} + \mathbf {a}_{2j}$ , so that

$$ \begin{align*}2^{-\mathbf{a}_1} + 3^1 2^{-\mathbf{a}_{[1,2]}} + \dots + 3^{n-1} 2^{-\mathbf{a}_{[1,n]}} = \sum_{j \in [n/2]} 3^{2j-2} 2^{-\mathbf{b}_{[1,j]}} ( 2^{\mathbf{a}_{2j}} + 3 ) + 3^{n-1} 2^{-\mathbf{b}_{[1,\lfloor n/2\rfloor]}-\mathbf{a}_n}\end{align*} $$

when *n*is odd, where we extend the summation notation in equation ( 1.6) to the $\mathbf {b}_j$ . For *n*even, the formula is the same except that the final term $3^{n-1} 2^{-\mathbf {b}_{[1,\lfloor n/2\rfloor ]}-\mathbf {a}_n}$ is omitted. Note that the $\mathbf {b}_1,\dots ,\mathbf {b}_{\lfloor n/2\rfloor }$ are jointly independent random variables taking values in $\mathbb {N}+2 = \{2,3,4,\dots \}$ ; they are iid copies of a Pascal (or negative binomial) random variable $\mathbf {Pascal} \equiv \mathbf {NB}(2,\frac {1}{2})$ on $\mathbb {N}+2$ , defined by

$$ \begin{align*}\mathbb{P}( \mathbf{Pascal} = b ) = \frac{b-1}{2^b}\end{align*} $$

for $b \in \mathbb {N}+2$ .

For any $j \in [n/2]$ , $\mathbf {a}_{2j}$ is independent of all of the $\mathbf {b}_1,\dots ,\mathbf {b}_{\lfloor n/2\rfloor }$ except for $\mathbf {b}_j$ . For *n*odd, $\mathbf {a}_n$ is independent of all of the $\mathbf {b}_j$ . Regardless of whether *n*is even or odd, once one conditions on all of the $\mathbf {b}_j$ to be fixed, the random variables $\mathbf {a}_{2j}, j \leq [n/2]$ (as well as $\mathbf {a}_n$ , if *n*is odd) are all independent of each other. We conclude that

$$ \begin{align*}S_\chi(n) = \mathbb{E} \left(\prod_{j \in [n/2]} f( 3^{2j-2} 2^{-\mathbf{b}_{[1,j]}}, \mathbf{b}_j )\right) g( 3^{n-1} 2^{-\mathbf{b}_{[1,\lfloor n/2\rfloor]}} )\end{align*} $$

when *n*is odd, with the factor $g( 2^{-\mathbf {b}_{[1,\lfloor n/2\rfloor ]}} )$ omitted when *n*is even, where $f(x,b)$ is the conditional expectation

(7.4) $$ \begin{align} f( x, b ) := \mathbb{E} \left( \chi( x (2^{\mathbf{a}_2}+3)) | \mathbf{a}_1 + \mathbf{a}_2 = b \right) \end{align} $$

(with $(\mathbf {a}_1,\mathbf {a}_2) \equiv \mathbf {Geom}(2)^2$ ) and

$$ \begin{align*}g(x) := \mathbb{E} \chi( x 2^{-\mathbf{Geom}(2)} ).\end{align*} $$

Clearly $|g(x)| \leq 1$ , so by the triangle inequality we can bound

(7.5) $$ \begin{align} |S_\chi(n)| \leq \mathbb{E} \prod_{j \in [n/2]} |f( 3^{2j-2} 2^{-\mathbf{b}_{[1,j]}}, \mathbf{b}_j )| \end{align} $$

regardless of whether *n*is even or odd.

From equation ( 7.4), we certainly have

(7.6) $$ \begin{align} |f(x,b)| \leq 1. \end{align} $$

We now perform an explicit computation to improve upon this estimate for many values of *x*(of the form $x = 3^{2j-2} 2^{-l}$ ) in the case $b = 3$ , which is the least value of $b \in \mathbb {N}+2$ for which the event $\mathbf {a}_1+\mathbf {a}_2=b$ does not completely determine $\mathbf {a}_1$ or $\mathbf {a}_2$ . For any $(j,l) \in (\mathbb {N}+1) \times \mathbb {Z}$ , we can write

(7.7) $$ \begin{align} \chi( 3^{2j-2} 2^{-l+1} ) = e^{-2\pi i \theta(j,l)}, \end{align} $$

where $\theta (j,l) = \theta _{n,\xi }(j,l) \in (-1/2,1/2]$ denotes the argument

(7.8) $$ \begin{align} \theta(j,l) := \left\{ \frac{\xi 3^{2j-2} (2^{-l+1} \bmod 3^n)}{3^n} \right\} \end{align} $$

and $\{\}\colon \mathbb {R}/\mathbb {Z} \to (-1/2,1/2]$ is the signed fractional part function; thus $\{x\}$ denotes the unique element of the coset $x + \mathbb {Z}$ that lies in $(-1/2,1/2]$ .

Let $0 < \varepsilon < \frac {1}{100}$ be a sufficiently small absolute constant to be chosen later; we will take care to ensure that the implied constants in many of our asymptotic estimates do not depend on $\varepsilon $ . Call a point $(j,l) \in [n/2] \times \mathbb {Z}$ *black*Footnote 8 if

(7.9) $$ \begin{align} |\theta(j,l)| \leq \varepsilon, \end{align} $$

and *white*otherwise. We let $B = B_{n,\xi }, W = W_{n,\xi }$ denote the black and white points of $[n/2] \times \mathbb {Z}$ respectively; thus we have the partition $[n/2] \times \mathbb {Z} = B \uplus W$ .

#### Lemma 7.2 (Cancellation for white points)

If $(j,l)$ is white, then

$$ \begin{align*}|f(3^{2j-2} 2^{-l},3)| \leq \exp( -\varepsilon^3 ).\end{align*} $$

Proof. If $\mathbf {a}_1,\mathbf {a}_2$ are independent copies of $\mathbf {Geom}(2)$ , then after conditioning to the event $\mathbf {a}_1+\mathbf {a}_2 = 3$ , the pair $(\mathbf {a}_1,\mathbf {a}_2)$ is equal to either $(1,2)$ or $(2,1)$ , with each pair occurring with (conditional) probability $1/2$ . From equation ( 7.4), we thus have

$$ \begin{align*}f(x,3) = \frac{1}{2} \chi( 5 x ) + \frac{1}{2} \chi( 7 x ) = \frac{\chi(5x)}{2} (1 + \chi(2x))\end{align*} $$

for any *x*, so that

$$ \begin{align*}|f(x,3)| = \frac{|1 + \chi(2x)|}{2}.\end{align*} $$

We specialise to the case $x := 3^{2j-2} 2^{-l}$ . By equation ( 7.7), we have

$$ \begin{align*}\chi(2x) = e^{-2\pi i \theta(j, \mathbf{b}_{[1,j]})}\end{align*} $$

and hence by elementary trigonometry

$$ \begin{align*}|f(3^{2j-2} 2^{-l},3)| = \cos( \pi \theta(j, l) ).\end{align*} $$

By hypothesis we have

$$ \begin{align*}|\theta(j, l)|> \varepsilon \end{align*} $$

and the claim now follows by Taylor expansion (if $\varepsilon $ is small enough); indeed one can even obtain an upper bound of $\exp (-c\varepsilon ^2)$ for some absolute constant $c>0$ independent of $\varepsilon $ .

From the above lemma, equation ( 7.6) and the law of total probability, we see that

$$ \begin{align*}|S_\chi(n)| \leq \mathbb{E} \exp( - \varepsilon^3 \# \{ j \in [n/2]: \mathbf{b}_j = 3, (j,\mathbf{b}_{[1,j]}) \in W \} ).\end{align*} $$

As we shall see later, we can interpret the $(j,\mathbf {b}_{[1,j]})$ with $\mathbf {b}_j=3$ as a two-dimensional renewal process. To establish Proposition 7.1 (and thus Proposition 1.17 and Theorem 1.3), it thus suffices to show the following estimate.

#### Proposition 7.3 (Renewal process encounters many white points)

(7.10) $$ \begin{align} \mathbb{E} \exp( - \varepsilon^3 \# \{ j \in [n/2]: \mathbf{b}_j = 3, (j,\mathbf{b}_{[1,j]}) \in W \} ) \ll_A n^{-A}. \end{align} $$

We remark that this proposition is of a simpler nature to establish than Proposition 7.1 as it is entirely ‘non-negative’; it does not require the need to capture any cancellation in an oscillating sum, as was the case in Proposition 7.1.

### 7.2 Deterministic structural analysis of black points

The proof of Proposition 7.3 consists of a ‘deterministic’ part, in which we understand the structure of the white set *W*(or the black set *B*), and a ‘probabilistic’ part, in which we control the random walk $\mathbf {b}_{[1,j]}$ and the events $\mathbf {b}_j=3$ . We begin with the former task. Define a *triangle*to be a subset $\Delta $ of $(\mathbb {N}+1) \times \mathbb {Z}$ of the form

(7.11) $$ \begin{align} \Delta = \{ (j,l): j \geq j_\Delta; l \leq l_\Delta; (j-j_\Delta) \log 9 + (l_\Delta-l) \log 2 \leq s_\Delta \} \end{align} $$

for some $(j_\Delta , l_\Delta ) \in (\mathbb {N}+1) \times \mathbb {Z}$ (which we call the *top-left corner*of $\Delta $ ) and some $s_\Delta \geq 0$ (which we call the *size*of $\Delta $ ); see Figure 2.

Figure 2

A triangle $\Delta $ , which we have drawn as a solid region rather than as a subset of the discrete lattice $\mathbb {Z}^2$ .

#### Lemma 7.4 (Structure of black set)

The black set $B \subset [n/2] \times \mathbb {Z}$ of points $(j,l)$ with $|\theta (j,l)| \leq \varepsilon $ can be expressed as a disjoint union

$$ \begin{align*}B = \biguplus_{\Delta \in {\mathcal T}} \Delta\end{align*} $$

of triangles $\Delta $ , each of which is contained in $[\frac {n}{2} - \frac {1}{10} \log \frac {1}{\varepsilon }] \times \mathbb {Z}$ . Furthermore, any two triangles $\Delta ,\Delta '$ in ${\mathcal T}$ are separated by a distance $\geq \frac {1}{10} \log \frac {1}{\varepsilon }$ (using the Euclidean metric on $[n/2] \times \mathbb {Z} \subset \mathbb {R}^2$ ). (See Figure 3.)

Figure 3

The black set is a union of triangles, in the strip $[\frac {n}{2} - \frac {1}{10} \log \frac {1}{\varepsilon }] \times \mathbb {Z}$ , that are separated from each other by $\gg \log \frac {1}{\varepsilon }$ . The red dots depict (a portion of) a renewal process $\mathbf {v}_1, \mathbf {v}_{[1,2]}, \mathbf {v}_{[1,3]}$ that we will encounter later in this section; our main objective will be to establish that this process usually contains a fair number of white points. We remark that the average slope $\frac {16}{4}=4$ of this renewal process will exceed the slope $\frac {\log 9}{\log 2} \approx 3.17$ of the triangle diagonals, so that the process tends to exit a given triangle through its horizontal side. The coordinate *j*increases in the rightward direction, while the coordinate *l*increases in the upward direction.

Proof. We first observe some simple relations between adjacent values of $\theta $ . From equation ( 7.8) (or equation ( 7.7)), we observe the identity

(7.12) $$ \begin{align} 3^{2(j_*-j)} 2^{(l-l_*)} \theta(j,l) = \theta(j_*,l_*) \bmod \mathbb{Z} \end{align} $$

whenever $j \leq j_*$ and $l \geq l_*$ . Thus, for instance,

(7.13) $$ \begin{align} \theta(j+1,l) = 9\theta(j,l) \bmod \mathbb{Z} \end{align} $$

and

(7.14) $$ \begin{align} \theta(j,l-1) = 2 \theta(j,l) \bmod \mathbb{Z}. \end{align} $$

Among other things, this implies that

$$ \begin{align*}\theta(j,l) = \theta(j+1,l) - 4 \theta(j,l-1) \bmod \mathbb{Z}\end{align*} $$

and hence by the triangle inequality

(7.15) $$ \begin{align} |\theta(j,l)| \leq |\theta(j+1,l)| + 4 |\theta(j,l-1)|. \end{align} $$

These identities have the following consequences. Call a point $(j,l) \in [n/2] \times \mathbb {Z}$ *weakly black*if

$$ \begin{align*}|\theta(j,l)| \leq \frac{1}{100}.\end{align*} $$

Clearly any black point is weakly black. We have the following further claims.

1.

(i) If $(j,l)$ is weakly black, and either $(j+1,l)$ or $(j,l-1)$ is black, then $(j,l)$ is black. (This follows from equation ( 7.13) or ( 7.14) respectively.)

2.

(ii) If $(j+1,l), (j,l-1)$ are weakly black, then $(j,l)$ is also weakly black. (Indeed, from equation ( 7.15), we have $|\theta (j,l)| \leq \frac {5}{100}$ , and the claim now follows from equation ( 7.13) or ( 7.14).)

3.

(iii) If $(j-1, l)$ and $(j,l-1)$ are weakly black, then $(j,l)$ is also weakly black. (Indeed, from equation ( 7.13), we have $|\theta (j,l)| \leq \frac {9}{100}$ , and the claim now follows from equation ( 7.14).)

Now we begin the proof of the lemma. Suppose $(j,l) \in [n/2] \times \mathbb {Z}$ is black, then by equations ( 7.9) and ( 7.8), we have

$$ \begin{align*}\frac{\xi 3^{2j-2} (2^{-l+1} \bmod 3^n)}{3^n} \in [-\varepsilon, \varepsilon] \bmod \mathbb{Z}\end{align*} $$

and hence

$$ \begin{align*}\frac{\xi 3^{n-1} (2^{-l+1} \bmod 3^n)}{3^n} \in [-3^{n+1-2j} \varepsilon, 3^{n+1-2j}\varepsilon] \bmod \mathbb{Z}. \end{align*} $$

On the other hand, since $\xi $ is not a multiple of $3$ , the expression $\frac {\xi 3^{n-1} (2^{-l+1} \bmod 3^n)}{3^n}$ is either equal to $1/3$ or $2/3$ mod $\mathbb {Z}$ . We conclude that

(7.16) $$ \begin{align} 3^{n+1-2j}\varepsilon \geq \frac{1}{3}, \end{align} $$

so the black points in $[n/2] \times \mathbb {Z}$ actually lie in $[\frac {n}{2} - \frac {1}{10} \log \frac {1}{\varepsilon }] \times \mathbb {Z}$ .

Suppose that $(j,l) \in [n/2] \times \mathbb {Z}$ is such that $(j,l')$ is black for all $l' \geq l$ ; thus

$$ \begin{align*}|\theta(j,l')| \leq \varepsilon\end{align*} $$

for all $l' \geq l$ . From equation ( 7.14), this implies that

$$ \begin{align*}\theta(j,l') = 2 \theta(j,l'+1)\end{align*} $$

for all $l' \geq l$ , hence

$$ \begin{align*}\theta(j,l') \leq 2^{l-l'} \varepsilon\end{align*} $$

for all $l' \geq l$ . Repeating the proof of equation ( 7.16), one concludes that

$$ \begin{align*}3^{n+1-2j} 2^{l-l'} \varepsilon \geq \frac{1}{3},\end{align*} $$

which is absurd for $l'$ large enough. Thus it is not possible for $(j,l')$ to be black for all $l' \geq l$ .

Figure 4

The proof of Lemma 7.4. The points connecting $(j,l)$ to $(j,l_*)$ , and from $(j,l_*)$ to $(j_*,l_*)$ , are known to be black, while the points $(j, l_*+1), (j_*-1, l_*)$ are known to be white. The point $(j',l')$ can be in various locations, as illustrated by the red dots here. From equation ( 7.18), one can obtain that every point in the dashed triangle $\Delta _*$ is black (and every point in the Case 1 region is weakly black), which can treat the Case 1 locations of $(j',l')$ (and also forces $(j,l)$ to lie inside $\Delta _*$ ). In Case 2, $(j',l')$ can be to the right or left of $(j,l_*+1)$ , but in either case one can show that if $(j',l')$ is black, then $(j',l_*+1)$ (displayed here in blue) is weakly black and hence $(j,l_*+1)$ is weakly black and in fact black, a contradiction. Similarly, in Case 3, $(j',l')$ can be above or below $(j_*-1,l_*)$ , but in either case one can show that if $(j',l')$ is black, then so $(j_*-1,l')$ (displayed here in green) is weakly black and hence $(j_*-1,l_*)$ is weakly black and in fact black, again giving a contradiction.

Now let $(j,l) \in [n/2] \times \mathbb {Z}$ be black. By the preceding discussion, there exists a unique $l_* = l_*(j,l) \geq l$ such that $(j,l')$ is black for all $l \leq l' \leq l_*$ , but such that $(j,l_*+1)$ is white. Now let $j_* = j_*(j,l) \leq j$ be the unique positive integer such that $(j',l_*)$ is black for all $j_* \leq j' \leq j$ , but such that either $j_*=1$ or $(j_*-1,l_*)$ is white. Informally, $(j_*,l_*)$ is obtained from $(j,l)$ by first moving upward as far as one can go in *B*, then moving leftwards as far as one can go in *B*; see Figure 4. As one should expect from glancing at this figure (or Figure 3), $(j_*,l_*)$ should be the top-left corner of the triangle containing $(j,l)$ , and the arguments below are intended to support this claim.

By construction, $(j_*,l_*)$ is black; thus by equation ( 7.9), we have

(7.17) $$ \begin{align} |\theta(j_*,l_*)| = \varepsilon \exp(-s_*) \end{align} $$

for some $s_* \geq 0$ . From equation ( 7.12) this implies in particular that

(7.18) $$ \begin{align} |\theta(j',l')| \leq \varepsilon \exp(-s_* + (j'-j_*) \log 9 + (l_*-l') \log 2 ) \end{align} $$

whenever $j' \geq j_*, l' \geq l_*$ , with equality whenever the right-hand side is strictly less than $1/2$ .

Let $\Delta _*$ denote the triangle with top-left corner $(j_*,l_*)$ and size $s_*$ . If $(j',l') \in \Delta _*$ , then by equation ( 7.18), we have

$$ \begin{align*}|\theta(j',l')| \leq 3^{2(j'-j_*)} 2^{(l_*-l')} \varepsilon \exp(-s_*) \leq \varepsilon\end{align*} $$

and hence every element of $\Delta _*$ is black (and thus lies in $[\frac {n}{2} - c \log \frac {1}{\varepsilon }] \times \mathbb {Z}$ ).

Next, we make the following claim:

-

(*) Every point $(j',l') \in [n/2] \times \mathbb {Z}$ that lies outside of $\Delta _*$ , but is at a distance of at most $\frac {1}{10} \log \frac {1}{\varepsilon }$ to $\Delta _*$ , is white.

To verify Claim (*), we divide into three cases (see Figure 4):

**Case 1:**$j' \geq j_*, l' \leq l_*$ . In this case we have from equation ( 7.11) that

$$ \begin{align*}s_* < (j'-j_*) \log 9 + (l_*-l') \log 2 \leq s_* + \frac{\log 9 + \log 2}{10} \log \frac{1}{\varepsilon}\end{align*} $$

and hence

$$ \begin{align*}\varepsilon \exp(-s_* + (j'-j_*) \log 9 + (l_*-l') \log 2 ) \varepsilon^{1-\frac{\log 9 + \log 2}{10}} < \frac{1}{2}. \end{align*} $$

Applying the equality case of equation ( 7.18), we conclude that

$$ \begin{align*}\theta = \varepsilon \exp(-s_* + (j'-j_*) \log 9 + (l_*-l') \log 2 ) \varepsilon^{1-\frac{\log 9 + \log 2}{10}}> \varepsilon\end{align*} $$

and thus $(j',l')$ is white as claimed.

**Case 2:**$j' \geq j_*, l'> l_*$ . In this case we have from equation ( 7.11) that

(7.19) $$ \begin{align} 0 < (l'-l_*) \log 2 \leq \frac{\log 2}{10} \log \frac{1}{\varepsilon} \end{align} $$

and

(7.20) $$ \begin{align} (j'-j_*) \log 9 \leq s_* + \frac{\log 9}{10} \log \frac{1}{\varepsilon} \end{align} $$

(say). Suppose for contradiction that $(j',l')$ was black; thus

$$ \begin{align*}|\theta(j',l')| \leq \varepsilon.\end{align*} $$

From equations ( 7.19) and ( 7.12) (or equation ( 7.14)) this implies that

$$ \begin{align*}|\theta(j',l_*+1)| \leq \varepsilon^{1-\frac{\log 2}{10}},\end{align*} $$

so in particular $(j',l_*+1)$ is weakly black.

If $j' \geq j$ , then from equations ( 7.18) and ( 7.20), we also have

(7.21) $$ \begin{align} |\theta(j'-1,l_*)| \leq \varepsilon^{1-\frac{\log 9}{10}}, \end{align} $$

thus $(j'-1,l_*)$ is weakly black. Applying claim (ii) and the fact that $(j',l_*+1)$ is weakly black, we conclude that $(j'-1,l_*+1)$ is weakly black. Iterating this argument, we conclude that $(j'',l_*+1)$ is weakly black for all $j_* \leq j'' \leq j'$ . In particular, $(j,l_*+1)$ is weakly black; since $(j,l_*)$ is black by construction of $l_*$ , we conclude from Claim (i) that $(j,l_*+1)$ is black. But this contradicts the construction of $l_*$ .

Now suppose that $j' < j$ . From construction of $l_*, j_*$ , we see that $(j'+1,l_*)$ is black, hence weakly black; since $(j',l_*+1)$ is weakly black, we conclude from Claim (iii) that $(j'+1,l_*+1)$ is weakly black. Iterating this argument, we conclude that $(j'',l_*+1)$ is weakly black for all $j' \leq j'' \leq j$ ; thus in particular $(j,l_*+1)$ is weakly black, and we obtain a contradiction as before.

**Case 3:**$j' < j_*$ . Clearly this implies $j_*> 1$ ; also, from equation ( 7.11), we have

(7.22) $$ \begin{align} - \frac{\log 2}{10} \log \frac{1}{\varepsilon} \leq (l_*-l') \log 2 \leq s_* + \frac{\log 2}{10} \log \frac{1}{\varepsilon} \end{align} $$

and

(7.23) $$ \begin{align} 0 < (j_* - j') \log 9 \leq \frac{\log 9}{10} \log \frac{1}{\varepsilon}. \end{align} $$

Suppose for contradiction that $(j',l')$ was black; thus

$$ \begin{align*}|\theta(j',l')| \leq \varepsilon.\end{align*} $$

From equations ( 7.23) and ( 7.12) (or equation ( 7.13)) we thus have

(7.24) $$ \begin{align} |\theta(j_*-1,l')| \leq \varepsilon^{1-\frac{\log 9}{10}}. \end{align} $$

If $l' \geq l_*$ , then from equations ( 7.22) and ( 7.12), we then have

$$ \begin{align*}|\theta(j_*-1,l_*)| \leq \varepsilon^{1-\frac{\log 9 + \log 2}{10}},\end{align*} $$

so $(j_*-1,l_*)$ is weakly black. By construction of $j_*$ , $(j_*,l_*)$ is black, hence by Claim (i) $(j_*-1,l_*)$ is black, contradicting the construction of $j_*$ .

Now suppose that $l' < l_*$ . From equation ( 7.24), $(j_*-1, l')$ is weakly black. On the other hand, from equations ( 7.22) and ( 7.18) that

$$ \begin{align*}|\theta(j_*,l'+1)| \leq \varepsilon^{1-\frac{\log 2}{10}}\end{align*} $$

so $(j_*, l'+1)$ is also weakly black. By Claim (ii), this implies that $(j_*-1, l'+1)$ is weakly black. Iterating this argument, we see that $(j_*-1, l'')$ is weakly black for all $l' \leq l'' \leq l_*$ , hence $(j_*-1,l_*)$ is weakly black and we can obtain a contradiction as before. This concludes the treatment of Case 3 of Claim (*).

We have now verified Claim (*) in all cases. From this claim and the construction $(j_*,l_*)$ from $(j,l)$ , we now see that $(j,l)$ must lie in $\Delta _*$ ; indeed, if $(j,l_*)$ was outside of $\Delta _*$ , then one of the (necessarily black) points between $(j_*,l_*)$ and $(j,l_*)$ would violate Case 1 of Claim (*), and similarly if $(j,l_*)$ was in $\Delta _*$ but $(j,l)$ was outside $\Delta _*$ , then one of the (necessarily black points) between $(j,l_*)$ and $(j,l)$ would again violate Case 1 of Claim (*); see Figure 4. Furthermore, for any $(j',l') \in \Delta _*$ , that $l_*(j',l') = l_*$ and $j_*(j',l') = j_*$ . In other words, we have

$$ \begin{align*}\Delta_* = \{ (j',l') \in B: l_*(j',l') = l_*; j_*(j',l') = j_* \},\end{align*} $$

and so the triangles $\Delta _*$ form a partition of *B*. By the preceding arguments, we see that these triangles lie in $[\frac {n}{2} - \frac {1}{10} \log \frac {1}{\varepsilon }] \times \mathbb {Z}$ and are separated from each other by at least $\frac {1}{10} \log \frac {1}{\varepsilon }$ . This proves the lemma.

Remark 7.5. One can say a little bit more about the structure of the black set *B*; for instance, from Euler’s theorem, we see that *B*is periodic with respect to the vertical shift $(0, 2 \times 3^{n-1})$ (cf. Lemma 1.12), and one could use Baker’s theorem [Reference Baker 2] that (among other things) establishes a Diophantine property of $\frac {\log 3}{\log 2}$ in order to obtain some further control on *B*. However, we will not exploit any further structure of the black set in our arguments beyond what is provided by Lemma 7.4.

### 7.3 Formulation in terms of holding time

We now return to the probabilistic portion of the proof of Proposition 7.3. Currently we have a finite sequence $\mathbf {b}_1,\dots ,\mathbf {b}_{\lfloor n/2\rfloor }$ of random variables that are iid copies of the sum $\mathbf {a}_1+\mathbf {a}_2$ of two independent copies $\mathbf {a}_1,\mathbf {a}_2$ of $\mathbf {Geom}(2)$ . We may extend this sequence to an infinite sequence $\mathbf {b}_1,\mathbf {b}_2,\mathbf {b}_3,\dots $ of iid copies of $\mathbf {a}_1+\mathbf {a}_2$ . Recalling from definition that *W*is a subset of $[n/2] \times \mathbb {Z}$ , the point $(j,\mathbf {b}_{[1,j]})$ can only lie in *W*when $j \in [n/2]$ . Thus the left-hand side of equation ( 7.10) can then be written as

$$ \begin{align*}\mathbb{E} \exp( - \varepsilon^3 \# \{ j \in \mathbb{N}+1: \mathbf{b}_j = 3, (j,\mathbf{b}_{[1,j]}) \in W \} ).\end{align*} $$

We now describe the random set $\{ (j,\mathbf {b}_{[1,j]}): j \in \mathbb {N}+1, \mathbf {b}_j = 3\}$ as Footnote 9 a two-dimensional renewal process (a special case of a *renewal-reward process*). Since the events $\mathbf {b}_j=3$ are independent and each occur with probability

(7.25) $$ \begin{align} \mathbb{P}( \mathbf{b}_j = 3 ) = \mathbb{P}( \mathbf{Pascal} = 3 ) = \frac{1}{4}> 0, \end{align} $$

we see that almost surely one has $\mathbf {b}_j=3$ for at least one $j \in \mathbb {N}$ . Define the *two-dimensional holding time*$\mathbf {Hold} \in (\mathbb {N}+1) \times (\mathbb {N}+2)$ to be the random shift $(\mathbf {j},\mathbf {b}_{[1,\mathbf {j}]})$ , where $\mathbf {j}$ is the least positive integer for which $\mathbf {b}_{\mathbf {j}} =3$ ; this random variable is almost surely well defined. Note from equation ( 7.25) that the first component $\mathbf {j}$ of $\mathbf {Hold}$ has the distribution $\mathbf {j} \equiv \mathbf {Geom}(4)$ . A little thought then reveals that the random set

(7.26) $$ \begin{align} \{ (j,\mathbf{b}_{[1,j]}): j \in \mathbb{N}+1, \mathbf{b}_j = 3\} \end{align} $$

has the same distribution as the random set

(7.27) $$ \begin{align} \{ \mathbf{v}_1, \mathbf{v}_{[1,2]}, \mathbf{v}_{[1,3]}, \dots \}, \end{align} $$

where $\mathbf {v}_1, \mathbf {v}_2, \dots $ are iid copies of $\mathbf {Hold}$ , and we extend the summation notation in equation ( 1.6) to the $\mathbf {v}_j$ ; thus, for instance, $\mathbf {v}_{[1,k]} := \mathbf {v}_1 + \dots + \mathbf {v}_k$ . In particular, we have

$$ \begin{align*}\# \{ j \in \mathbb{N}+1: \mathbf{b}_j = 3, (j,\mathbf{b}_{[1,j]}) \in W \} \equiv \# \{ k \in \mathbb{N}+1: \mathbf{v}_{[1,k]} \in W \},\end{align*} $$

and so we can write the left-hand side of equation ( 7.10) as

(7.28) $$ \begin{align} \mathbb{E} \prod_{k \in \mathbb{N}+1} \exp( - \varepsilon^3 1_W(\mathbf{v}_{[1,k]}) ); \end{align} $$

note that all but finitely many of the terms in this product are equal to $1$ .

We now pause our analysis of equations ( 7.10) and ( 7.28) to record some basic properties about the distribution of $\mathbf {Hold}$ .

#### Lemma 7.6 (Basic properties of holding time)

The random variable $\mathbf {Hold}$ has exponential tail (in the sense of equation ( 2.3)), is not supported in any coset of any proper subgroup of $\mathbb {Z}^2$ and has mean $(4,16)$ . In particular, the conclusion of Lemma 2.2 holds for $\mathbf {Hold}$ with $\vec \mu = (4,16)$ .

Proof. From the definition of $\mathbf {Hold}$ and equation ( 7.25), we see that $\mathbf {Hold}$ is equal to $(1,3)$ with probability $1/4$ , and on the remaining event of probability $3/4$ , it has the distribution of $(1,\mathbf {Pascal}') + \mathbf {Hold}'$ , where $\mathbf {Pascal}'$ is a copy of $\mathbf {Pascal}$ that is conditioned to the event $\mathbf {Pascal} \neq 3$ , so that

(7.29) $$ \begin{align} \mathbb{P}( \mathbf{Pascal}' = b ) = \frac{4}{3} \frac{b-1}{2^b} \end{align} $$

for $b \in \mathbb {N}+2 \backslash \{3\}$ , and $\mathbf {Hold}'$ is a copy of $\mathbf {Hold}$ that is independent of $\mathbf {Pascal}'$ . Thus $\mathbf {Hold}$ has the distribution of $(1,3) + (1,\mathbf {b}^{\prime }_1) + \dots + (1,\mathbf {b}^{\prime }_{\mathbf {j}-1})$ , where $\mathbf {b}^{\prime }_1,\mathbf {b}^{\prime }_2,\dots $ are iid copies of $\mathbf {Pascal}'$ and $\mathbf {j} \equiv \mathbf {Geom}(4)$ is independent of the $\mathbf {b}^{\prime }_j$ . In particular, for any $k = (k_1,k_2) \in \mathbb {R}^2$ , one has from monotone convergence that

(7.30) $$ \begin{align} \mathbb{E} \exp( \mathbf{Hold} \cdot k ) = \sum_{j \in \mathbb{N}} \frac{1}{4} \left(\frac{3}{4}\right)^{j-1} \exp\left( (1,3) \cdot k\right) \left(\mathbb{E} \exp( (1,\mathbf{Pascal}') \cdot k) \right)^j. \end{align} $$

From equation ( 7.29) and dominated convergence, we have $\mathbb {E} \exp ( (1,\mathbf {Pascal}') \cdot k ) < \frac {4}{3}$ for *k*sufficiently close to $0$ , which by equation ( 7.30) implies that $\mathbb {E} \exp ( \mathbf {Hold} \cdot k ) < \infty $ for *k*sufficiently close to zero. This gives the exponential tail property by Markov’s inequality.

Since $\mathbf {Hold}$ attains the value $(1,3)+(1,b)$ for any $b \in \mathbb {N}+2 \backslash \{3\}$ with positive probability, as well as attaining $(1,3)$ with positive probability, we see that the support of $\mathbf {Hold}$ is not supported in any coset of any proper subgroup of $\mathbb {Z}^2$ . Finally, from the description of $\mathbf {Hold}$ at the start of this proof we have

$$ \begin{align*}\mathbb{E} \mathbf{Hold} = \frac{1}{4} (1,3) + \frac{3}{4} \left((1,\mathbb{E} \mathbf{Pascal}') + \mathbb{E} \mathbf{Hold}\right);\end{align*} $$

also, from the definition of $\mathbf {Pascal}'$ , we have

$$ \begin{align*}\mathbb{E} \mathbf{Pascal} = \frac{1}{4} 3 + \frac{3}{4} \mathbb{E} \mathbf{Pascal}'. \end{align*} $$

We conclude that

$$ \begin{align*}\mathbb{E} \mathbf{Hold} = (1,\mathbb{E} \mathbf{Pascal}) + \frac{3}{4} \mathbb{E} \mathbf{Hold};\end{align*} $$

since $\mathbb {E} \mathbf {Pascal} = 2 \mathbb {E} \mathbf {Geom}(2) =4$ , we thus have $\mathbb {E} \mathbf {Hold} = (4,16)$ as required.

The following lemma allows us to control the distribution of first passage locations of renewal processes with holding times $\equiv \mathbf {Hold}$ , which will be important for us as it lets us understand how such renewal processes exit a given triangle $\Delta $ :

#### Lemma 7.7 (Distribution of first passage location)

Let $\mathbf {v}_1,\mathbf {v}_2,\dots $ be iid copies of $\mathbf {Hold}$ , and write $\mathbf {v}_k = (\mathbf {j}_k,\mathbf {l}_k)$ . Let $s \in \mathbb {N}$ , and define the first passage time $\mathbf {k}$ to be the least positive integer such that $\mathbf {l}_{[1,k]}> s$ . Then for any $j,l \in \mathbb {N}$ with $l> s$ , one has

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,\mathbf{k}]} = (j,l) ) \ll \frac{e^{-c(l-s)}}{(1+s)^{1/2}} G_{1+s}\left( c\left(j - \frac{s}{4}\right) \right),\end{align*} $$

where $G_{1+s}(x) = \exp (-\frac {|x|^2}{1+s}) + \exp (-|x|)$ was the function defined in equation ( 2.2).

Informally, this lemma asserts that as a rough first approximation one has

(7.31) $$ \begin{align} \mathbf{v}_{[1,\mathbf{k}]} \approx \mathbf{Unif}\left( \left\{ (j,l): j = \frac{s}{4} + O( (1+s)^{1/2}); s < l \leq s + O(1) \right\} \right). \end{align} $$

Proof. Note that by construction of $\mathbf {k}$ one has $\mathbf {l}_{[1,\mathbf {k}]} - \mathbf {l}_{\mathbf {k}} \leq s$ , so that $\mathbf {l}_{\mathbf {k}} \geq \mathbf {l}_{[1,\mathbf {k}]}-s$ . From the union bound, we therefore have

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,\mathbf{k}]} = (j,l) ) \leq \sum_{k \in \mathbb{N}+1} \mathbb{P}( (\mathbf{v}_{[1,k]} = (j,l)) \wedge (\mathbf{l}_k \geq l - s) );\end{align*} $$

since $\mathbf {v}_k$ has the exponential tail and is independent of $\mathbf {v}_1,\dots ,\mathbf {v}_{k-1}$ , we thus have

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,\mathbf{k}]} = (j,l) ) \ll \sum_{k \in \mathbb{N}+1} \sum_{l_k \geq l-s} \sum_{j_k \in \mathbb{N}+1} e^{- c(j_k+l_k)} \mathbb{P}( \mathbf{v}_{[1,k-1]} = (j-j_k,l-l_k) ).\end{align*} $$

Writing $l_k = l - s + l^{\prime }_k$ , we then have

$$ \begin{align*} \mathbb{P}( \mathbf{v}_{[1,\mathbf{k}]} = (j,l) ) &\ll e^{-c(l-s)} \sum_{k \in \mathbb{N}+1} \sum_{l^{\prime}_k \in \mathbb{N}} \sum_{j_k \in \mathbb{N}+1} \\ &\quad\quad\quad e^{-c(j_k+l^{\prime}_k)} \mathbb{P}( \mathbf{v}_{[1,k-1]} = (j-j_k,s-l^{\prime}_k) ). \end{align*} $$

We can restrict to the region $l^{\prime }_k \leq s$ , since the summand vanishes otherwise. It now suffices to show that

(7.32) $$ \begin{align} &\sum_{k \in \mathbb{N}+1} \sum_{0 \leq l_k' \leq s} \sum_{j_k \in \mathbb{N}+1} e^{- c(j_k+l^{\prime}_k)} \mathbb{P}\left( \mathbf{v}_{[1,k-1]} = (j-j_k,s-l^{\prime}_k) \right)\nonumber\\ &\quad \ll (1+s)^{-1/2} G_{1+s}\left( c \left(j - \frac{s}{4}\right) \right). \end{align} $$

This is in turn implied by

(7.33) $$ \begin{align} &\sum_{k \in \mathbb{N}+1} \sum_{0 \leq l_k' \leq s} e^{-cl^{\prime}_k} \mathbb{P}( \mathbf{v}_{[1,k-1]} = (j',s-l^{\prime}_k) ) \nonumber\\ &\quad \ll (1+s)^{-1/2} G_{1+s}\left( c\left(j' - \frac{s}{4}\right) \right) \end{align} $$

for all $j' \in \mathbb {Z}$ , since equation ( 7.32) then follows by replacing $j'$ by $j - j_k$ , multiplying by $\exp (-cj_k)$ , and summing in $j_k$ (and adjusting the constants *c*appropriately). In a similar vein, it suffices to show that

$$ \begin{align*}\sum_{k \in \mathbb{N}+1} \mathbb{P}( \mathbf{v}_{[1,k-1]} = (j',s') ) \ll (1+s')^{-1/2} G_{1+s'}\left( c \left(j' - \frac{s'}{4} \right) \right)\end{align*} $$

for all $s' \in \mathbb {N}$ , since equation ( 7.33) follows after setting $s' = s - l^{\prime }_k$ , multiplying by $\exp (-cl^{\prime }_k)$ , and summing in $l^{\prime }_k$ (splitting into the regions $l^{\prime }_k \leq s/2$ and $l^{\prime }_k> s/2$ if desired to simplify the calculations).

From Lemma 7.6 and Lemma 2.2, one has

$$ \begin{align*}\mathbb{P}( \mathbf{v}_{[1,k-1]} = (j',s') ) \ll k^{-1} G_{k-1}\left( c ((j',s') - (k-1)(4,16))\right),\end{align*} $$

and the claim now follows from summing in *k*and a routine calculation (splitting for instance into the regions $16 (k-1) \in [s'/2,2s']$ , $16(k-1) < s'/2$ , and $16(k-1)>2s'$ ).

### 7.4 Recursively controlling a maximal expression

We return to the study of the left-hand side of equation ( 7.10), which we have expressed as equation ( 7.28). For any $(j,l) \in \mathbb {N}+1 \times \mathbb {Z}$ , let $Q(j,l)$ denote the quantity

(7.34) $$ \begin{align} Q(j,l) := \mathbb{E} \prod_{k \in \mathbb{N}} \exp( - \varepsilon^3 1_W((j,l) + \mathbf{v}_{[1,k]}) ) \end{align} $$

then we have the recursive formula

(7.35) $$ \begin{align} Q(j,l) = \exp( - \varepsilon^3 1_W(j,l) ) \mathbb{E} Q((j,l) + \mathbf{Hold}). \end{align} $$

Observe that for each $(j,l) \in \mathbb {N}+1 \times \mathbb {Z}$ , we have the conditional expectation

$$ \begin{align*}\mathbb{E}\left( \prod_{k \in \mathbb{N}+1} \exp( - \varepsilon^3 1_W(\mathbf{v}_{[1,k]}) ) | \mathbf{v}_1 = (j,l) \right) = Q(j,l)\end{align*} $$

since after conditioning on $\mathbf {v}_1 = (j,l)$ , then the $\mathbf {v}_{[1,k]}$ have the same distribution as $(j,l) + \mathbf {v}^{\prime }_{[1,k-1]}$ , where $\mathbf {v}^{\prime }_1,\mathbf {v}^{\prime }_2,\dots $ is another sequence of iid copies of $\mathbf {Hold}$ . Since $\mathbf {v}_1$ has the distribution of $\mathbf {Hold}$ , we conclude from the law of total probability that

$$ \begin{align*}\mathbb{E} \prod_{k \in \mathbb{N}+1} \exp( - \varepsilon^3 1_W(\mathbf{v}_{[1,k]}) ) = \mathbb{E} Q(\mathbf{Hold}).\end{align*} $$

From equation ( 7.28), we thus see that we can rewrite the desired estimate in equation ( 7.10) as

(7.36) $$ \begin{align} \mathbb{E} Q(\mathbf{Hold}) \ll_A n^{-A}. \end{align} $$

One can think of $Q(j,l)$ as a quantity controlling how often one encounters white points when one walks along a two-dimensional renewal process $(j,l), (j,l) + \mathbf {v}_1, (j,l)+\mathbf {v}_{[1,2]}, \dots $ starting at $(j,l)$ with holding times given by iid copies of $\mathbf {Hold}$ . The smaller this quantity is, the more white points one is likely to encounter. The main difficulty is thus to ensure that this renewal process is usually not trapped within the black triangles $\Delta $ from Lemma 7.4; as it turns out (and as may be evident from an inspection of Figure 3), the large triangles will be the most troublesome to handle (as they are so large compared to the narrow band of white points surrounding them that are provided by Lemma 7.4).

Suppose that we can prove a bound of the form

(7.37) $$ \begin{align} Q(j,l) \ll_A \max(\lfloor n/2\rfloor -j,1)^{-A} \end{align} $$

for all $(j,l) \in (\mathbb {N}+1) \times \mathbb {Z}$ ; this is trivial for $j \geq n/2$ but becomes increasingly non-trivial for smaller values of *j*. Then

$$ \begin{align*}Q(\mathbf{Hold}) \ll_A \max(\lfloor n/2\rfloor -\mathbf{j},1)^{-A} \ll_A n^{-A} \mathbf{j}^A\end{align*} $$

where $\mathbf {j} \equiv \mathbf {Geom}(4)$ is the first component of $\mathbf {Hold}$ . As $\mathbf {Geom}(4)$ has exponential tail, we conclude equation ( 7.36) and hence Proposition 7.3, which then implies Propositions 7.1, 1.17 and Theorem 1.3.

It remains to prove equation ( 7.37). Roughly speaking, we will accomplish this by a downward induction on *j*, or more precisely, by an upward induction on a quantity *m*, which is morally equivalent to $\lfloor n/2\rfloor - j$ . To make this more precise, it is convenient to introduce the quantities $Q_m$ for any $m \in [n/2]$ by the formula

(7.38) $$ \begin{align} Q_m := \sup_{(j,l) \in (\mathbb{N}+1) \times \mathbb{Z}: j \geq \lfloor n/2\rfloor - m} \max(\lfloor n/2\rfloor -j,1)^A Q(j,l). \end{align} $$

Clearly we have

(7.39) $$ \begin{align} Q_m \leq m^A, \end{align} $$

since $Q(j,l) \leq 1$ for all $j,l$ ; this bound can be thought of as supplying the ‘base case’ for our induction). We trivially have $Q_m \geq Q_{m-1}$ for any $1 \leq m \leq n/2$ . We will shortly establish the opposite inequality:

#### Proposition 7.8 (Monotonicity)

We have

(7.40) $$ \begin{align} Q_m \leq Q_{m-1} \end{align} $$

whenever $C_{A,\varepsilon } \leq m \leq n/2$ for some sufficiently large $C_{A,\varepsilon }$ depending on $A,\varepsilon $ .

Assuming Proposition 7.8, we conclude from equation ( 7.39) and a (forward) induction on *m*that $Q_m \leq C_{A,\varepsilon }^A \ll _A 1$ for all $1 \leq m \leq n/2$ , which gives equation ( 7.37). This in turn implies Proposition 7.3, and hence Proposition 7.1, Proposition 1.17, and Theorem 1.3.

It remains to establish Proposition ( 7.8). Let $C_{A,\varepsilon } \leq m \leq n/2$ for some sufficiently large $C_{A,\varepsilon }$ . It suffices to show that

(7.41) $$ \begin{align} Q(j,l) \leq m^{-A} Q_{m-1} \end{align} $$

whenever $j = \lfloor n/2 \rfloor - m$ and $l \in \mathbb {Z}$ . Note from equation ( 7.38) that we immediately obtain $Q(j,l) \leq m^{-A} Q_m$ , but to be able to use $Q_{m-1}$ instead of $Q_m$ , we will apply equation ( 7.35) at least once, in order to estimate $Q(j,l)$ in terms of other values $Q(j',l')$ of *Q*with $j'> j$ . This causes a degradation in the $m^{-A}$ term, even when *m*is large; to overcome this loss we need to ensure that (with high probability) the two-dimensional renewal process visits a sufficient number of white points before we use $Q_{m-1}$ to bound the resulting expression. This is of course consistent with the interpretation of equation ( 7.10) as an assertion that the renewal process encounters plenty of white points.

We divide the proof of equation ( 7.41) into three cases. Let ${\mathcal T}$ be the family of triangles from Lemma 7.4.

**Case 1:**$(j,l) \in W$ . This is the easiest case, as one can immediately get a gain from the white point $(j,l)$ . From equation ( 7.35), we have

$$ \begin{align*}Q(j,l) = \exp( - \varepsilon^3 ) \mathbb{E} Q((j,l) + \mathbf{Hold}).\end{align*} $$

For any $(j',l') \in (\mathbb {N}+1) \times \mathbb {Z}$ , we have from equation ( 7.38) (applied with *m*replaced by $m-1$ ) that

$$ \begin{align*}Q((j,l) + (j',l')) \leq \max( \lfloor n/2\rfloor -j - j', 1)^{-A} Q_{m-1} = \max( m - j', 1)^{-A} Q_{m-1}\end{align*} $$

since $j+j' \geq j+1 = \lfloor n/2 \rfloor - (m-1)$ . Replacing $(j',l')$ by $\mathbf {Hold}$ (so that $j'$ has the distribution of $\mathbf {Geom}(4)$ ) and taking expectations, we conclude that

$$ \begin{align*}Q(j,l) \leq \exp( - \varepsilon^3 ) Q_{m-1} \mathbb{E} \max( m - \mathbf{Geom}(4), 1)^{-A}.\end{align*} $$

We can bound

(7.42) $$ \begin{align} \max(m-r,1)^{-1} \leq m^{-1} \exp\left( O\left( \frac{r\log m}{m}\right ) \right) \end{align} $$

for any $r \in \mathbb {N}+1$ ; indeed this bound is trivial for $r \geq m$ , and for $r < m$ one can use the concave nature of $x \mapsto \log (1-x)$ for $0 < x < 1$ to conclude that

$$ \begin{align*}\frac{\log\left(1-\frac{r}{m}\right)}{r/m} \geq \frac{\log \left(1 - \frac{m-1}{m}\right)}{(m-1)/m}\end{align*} $$

which rearranges to give the stated bound. Replacing *r*by $\mathbf {Geom}(4)$ and raising to the $A^{\mathrm {th}}$ power, we obtain

$$ \begin{align*}Q(j,l) \leq \exp( - \varepsilon^3 ) m^{-A} Q_{m-1} \mathbb{E} \exp\left( O\left( \frac{A\log m}{m} \mathbf{Geom}(4) \right) \right).\end{align*} $$

For *m*large enough depending on $A,\varepsilon $ , we then have

(7.43) $$ \begin{align} Q(j,l) \leq \exp( - \varepsilon^3/2 ) m^{-A} Q_{m-1} \end{align} $$

which gives equation ( 7.41) in this case (with some room to spare).

**Case 2:**$(j,l) \in \Delta $ **for some triangle**$\Delta \in {\mathcal T}$ , **and**$l \geq l_\Delta - \frac {m}{\log ^2 m}$ . This case is slightly harder than the preceding one, as one has to walk randomly through the triangle $\Delta $ before one has a good chance to encounter a white point, but because this portion of the walk is relatively short, the degradation of the weight $m^{-A}$ during this portion will be negligible.

We turn to the details. Set $s := l_\Delta - l$ ; thus $0 \leq s \leq \frac {m}{\log ^2 m}$ . Let $\mathbf {v} _1,\mathbf {v}_2,\dots $ be iid copies of $\mathbf {Hold}$ , write $\mathbf {v}_k = (\mathbf {j}_k, \mathbf {l}_k)$ for each *k*with the usual summation notations in equation ( 1.6), and define the first passage time $\mathbf {k} \in \mathbb {N}+1$ to be the least positive integer such that

(7.44) $$ \begin{align} \mathbf{l}_{[1,\mathbf{k}]}> s. \end{align} $$

This is a finite random variable since the $\mathbf {l}_k$ are all positive integers. Heuristically, $\mathbf {k}$ represents the time in which the sequence first exits the triangle $\Delta $ , assuming that this exit occurs on the top edge of the triangle. It is in principle possible for the sequence to instead exit $\Delta $ through the hypotenuse of the triangle, in which case $\mathbf {k}$ will be somewhat larger than the first exit time; however, as we shall see below, the Chernoff bound in Lemma 7.7 can be used to show that the former scenario will occur with probability $\gg 1$ , which will be sufficient for the purposes of establishing equation ( 7.41) in this case.

By iterating equation ( 7.35) appropriately (or using equation ( 7.34)), we have the identity

(7.45) $$ \begin{align} Q(j,l) = \mathbb{E} \left[ \exp\left( - \varepsilon^3 \sum_{i=0}^{\mathbf{k}-1} 1_W((j,l) + \mathbf{v}_{[1,i]}) \right) Q((j,l) + \mathbf{v} _{[1,\mathbf{k}]}) \right] \end{align} $$

and hence by equation ( 7.38)

$$ \begin{align*}Q(j,l) \leq Q_{m-1} \mathbb{E} \left[ \exp\left( - \frac{\varepsilon^3}{2} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}]}) \right) \max(m - \mathbf{j}_{[1,\mathbf{k}]},1)^{-A}\right]\end{align*} $$

which by equation ( 7.42) gives

$$ \begin{align*}Q(j,l) \leq m^{-A} Q_{m-1} \mathbb{E} \exp\left( - \frac{\varepsilon^3}{2} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}]})\right) \exp\left( O\left( \frac{A \log m}{m} \mathbf{j}_{[1,\mathbf{k}]} \right)\right).\end{align*} $$

To prove equation ( 7.41) in this case, it thus suffices to show that

(7.46) $$ \begin{align} \mathbb{E} \exp\left( - \frac{\varepsilon^3}{2} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}]}) \right) \exp\left( O\left( \frac{A \log m}{m} \mathbf{j}_{[1,\mathbf{k}]} \right)\right) \leq 1. \end{align} $$

Since $\exp (-\varepsilon ^3/2) \leq 1 - \varepsilon ^3/4$ , we can upper bound the left-hand side by

(7.47) $$ \begin{align} \mathbb{E} \exp\left( O\left( \frac{A\log m}{m} \mathbf{j}_{[1,\mathbf{k}]} \right) \right) - \frac{\varepsilon^3}{4} \mathbb{P}( (j,l) + \mathbf{v} _{[1,\mathbf{k}]} \in W ). \end{align} $$

We begin by controlling the first term on the right-hand side of equation ( 7.47). By definition, the first passage location $(j,l) + \mathbf {v}_{[1,\mathbf {k}]}$ takes values in the region $\{ (j',l') \in \mathbb {Z}^2: j'> j, l' > l_\Delta \}$ . From Lemma 7.7, we have

(7.48) $$ \begin{align} \mathbb{P}( (j,l) + \mathbf{v}_{[1,\mathbf{k}]} = (j',l') ) \ll \frac{e^{-c(l'-l_\Delta)}}{(1+s)^{1/2} } G_{1+s}\left(c\left(j'-j - \frac{s}{4}\right) \right). \end{align} $$

Summing in $l'$ , we conclude that

$$ \begin{align*}\mathbb{P}( \mathbf{j}_{[1,\mathbf{k}]} = j'-j ) \ll (1+s)^{-1/2} G_{1+s}\left( c \left(j'-j - \frac{s}{4}\right) \right)\end{align*} $$

for any $j'$ ; informally, $\mathbf {j}_{[1,\mathbf {k}]}$ is behaving like a Gaussian random variable centred at $s/4$ with standard deviation $\asymp (1+s)^{1/2}$ . In particular, because of the hypothesis $s \leq \frac {m}{\log ^2 m}$ , we have

$$ \begin{align*}\mathbb{P}( \mathbf{j}_{[1,\mathbf{k}]} = r ) \ll \exp( - |r| )\end{align*} $$

when $r> \frac {m}{\log ^2 m}$ (say). With our hypotheses $s \leq \frac {m}{\log ^2 m}$ and $m \geq C_{A,\varepsilon }$ , the quantity $\frac {A \log m}{m}$ is much smaller than $1$ , and by using the above bound to control the contribution when $\mathbf {j}_{[1,\mathbf {k}]}> \frac {m}{\log ^2 m}$ , we have

(7.49) $$ \begin{align} \mathbb{E} \exp\left( O\left( \frac{A\log m}{m} \mathbf{j}_{[1,\mathbf{k}]} \right) \right) &\leq \mathbb{E} \exp\left( O\left( \frac{A\log m}{m} \frac{m}{\log^2 m} \right) \right) + O\left( \exp\left( - c \frac{m}{\log^2 m} \right) \right)\nonumber\\ = 1 + O\left( \frac{A}{\log m} \right). \end{align} $$

Now we turn attention to the second term on the right-hand side of equation ( 7.47). Using equation ( 7.48) to handle all points $(j',l')$ outside the region $l' = l_\Delta +O(1)$ and $j' = j + \frac {s}{4} + O( (1+s)^{1/2} )$ , we have

(7.50) $$ \begin{align} \mathbb{P}\left( (j,l) + \mathbf{v}_{[1,\mathbf{k}]} = \left(j+\frac{s}{4} + O((1+s)^{1/2}),l_\Delta + O(1)\right) \right) \gg 1 \end{align} $$

for a suitable choice of implied constants in the *O*-notation that is independent of $\varepsilon $ (cf. equation ( 7.31)). On the other hand, since $(j,l) \in \Delta $ and $s = l_\Delta - l$ , we have from equation ( 7.11) that

$$ \begin{align*}0 \leq (j-j_\Delta) \log 9 \leq s_\Delta - s \log 2\end{align*} $$

and thus (since $0 < \frac {1}{4} \log 9 < \log 2$ ) one has

$$ \begin{align*}-O(1) \leq (j'-j_\Delta ) \log 9 \leq s_\Delta + O(1)\end{align*} $$

whenever $j' = j + \frac {s}{4} + O((1+s)^{1/2})$ , with the implied constants independent of $\varepsilon $ . We conclude that with probability $\gg 1$ , the first passage location $(j,l) + \mathbf {v}_{[1,\mathbf {k}]}$ lies outside of $\Delta $ , but at a distance $O(1)$ from $\Delta $ , hence is white by Lemma 7.4. We conclude that

(7.51) $$ \begin{align} \mathbb{P}( (j,l) + \mathbf{v}_{[1,\mathbf{k}]} \in W ) \gg 1 \end{align} $$

and equation ( 7.41) (and hence equation ( 7.46)) now follows from equations ( 7.47), ( 7.49) and ( 7.51) since $m \geq C_{A,\varepsilon }$ .

**Case 3:**$(j,l) \in \Delta $ **for some triangle**$\Delta \in {\mathcal T}$ , **and**$l < l_\Delta - \frac {m}{\log ^2 m}$ . This is the most difficult case, as one has to walk so far before exiting $\Delta $ that one needs to encounter multiple white points, not just a single white point, in order to counteract the degradation of the weight $m^{-A}$ . Fortunately, the number of white points one needs to encounter is $O_{A,\varepsilon }(1)$ , and we will be able to locate such a number of white points on average for *m*large enough.

We will need a large constant *P*(much larger than *A*or $1/\varepsilon $ , but much smaller than *m*) depending on $A,\varepsilon $ to be chosen later; the implied constants in the asymptotic notation below will not depend on *P*unless otherwise specified. As before, we set $s := l_\Delta - l$ , so now $s> \frac {m}{\log ^2 m}$ . From equation ( 7.11), we have

$$ \begin{align*}(j-j_\Delta) \log 9 + s \log 2 \leq s_\Delta\end{align*} $$

, while from Lemma 7.4, one has $j_\Delta + \frac {s_\Delta }{\log 9} \leq \lfloor \frac {n}{2} \rfloor \leq j+m$ , hence

(7.52) $$ \begin{align} s \leq \frac{\log 9}{\log 2} m. \end{align} $$

We again let $\mathbf {v}_1,\mathbf {v}_2,\dots $ be iid copies of $\mathbf {Hold}$ , write $\mathbf {v}_k = (\mathbf {j}_k, \mathbf {l}_k)$ for each *k*, and define the first passage time $\mathbf {k} \in \mathbb {N}+1$ to be the least positive integer such that equation ( 7.44) holds. From equation ( 7.45), we have

$$ \begin{align*}Q(j,l) \leq \mathbb{E} Q((j,l) + \mathbf{v}_{[1,\mathbf{k}]}). \end{align*} $$

Applying equation ( 7.35), we then have

(7.53) $$ \begin{align} Q(j,l) \leq \mathbb{E} \exp\left( - \varepsilon^3 \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} ) \right) Q((j,l) + \mathbf{v} _{[1,\mathbf{k}+P]}). \end{align} $$

Applying equation ( 7.38) to $Q((j,l) + \mathbf {v}_{[1,\mathbf {k}+P]}) = Q(j+\mathbf {j}_{[1,\mathbf {k}+P]}, l+\mathbf {l}_{[1,\mathbf {k}+P]})$ , we have

$$ \begin{align*}\max( \lfloor n/2 \rfloor - j - \mathbf{j}_{[1,\mathbf{k}+P]}, 1)^A Q((j,l) + \mathbf{v}_{[1,\mathbf{k}+P]}) \leq Q_{m-1}\end{align*} $$

(since $j + \mathbf {j}_{[1,\mathbf {k}+P]} \geq j+1 \geq \lfloor n/2 \rfloor - (m-1)$ ). We can rearrange this inequality as

$$ \begin{align*}Q((j,l) + \mathbf{v}_{[1,\mathbf{k}+P]}) \leq m^{-A} Q_{m-1} \max\left( 1 - \frac{\mathbf{j}_{[1,\mathbf{k}+P]}}{m}, \frac{1}{m}\right)^{-A};\end{align*} $$

inserting this back into equation ( 7.53), we conclude that

$$ \begin{align*}Q(j,l) \leq m^{-A} Q_{m-1} \mathbb{E} \exp\left( - \varepsilon^3 \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]}) \right) \max\left( 1 - \frac{\mathbf{j}_{[1,\mathbf{k}+P]}}{m}, \frac{1}{m}\right)^{-A}. \end{align*} $$

Thus, to establish equation ( 7.41) in this case, it suffices to show that

(7.54) $$ \begin{align} \mathbb{E} \exp\left( - \varepsilon^3 \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} )\right) \max\left( 1 - \frac{\mathbf{j}_{[1,\mathbf{k}+P]}}{m}, \frac{1}{m}\right)^{-A} \leq 1. \end{align} $$

Let us first consider the event that $\mathbf {j}_{[1,\mathbf {k}+P]} \geq 0.9 m$ . From Lemma 7.7 and the bound in equation ( 7.52), we have

$$ \begin{align*}\mathbb{P}( \mathbf{j}_{[1,\mathbf{k}]} \geq 0.8 m ) \ll \exp( -c m)\end{align*} $$

(noting that $0.8> \frac {1}{4} \frac {\log 9}{\log 2}$ ) while from Lemma 2.2 (recalling that the $\mathbf {j}_k$ are iid copies of $\mathbf {Geom}(4)$ ), we have

$$ \begin{align*}\mathbb{P}( \mathbf{j}_{[\mathbf{k}+1,\mathbf{k}+P]} \geq 0.1m ) \ll_P \exp( -c m)\end{align*} $$

and thus by the triangle inequality

$$ \begin{align*}\mathbb{P}( \mathbf{j}_{[1,\mathbf{k}+P]} \geq 0.9 m ) \ll_P \exp( -c m).\end{align*} $$

Thus the contribution of this case to equation ( 7.54) is $O_{P,A}(m^A \exp (-cm)) = O_{P,A}(\exp (-cm/2))$ . If instead we have $\mathbf {j}_{[1,\mathbf {k}+P]} < 0.9 m$ , then

$$ \begin{align*}\max\left( 1 - \frac{\mathbf{j}_{[1,\mathbf{k}+P]}}{m}, \frac{1}{m}\right)^{-A} \leq 10^A.\end{align*} $$

Since *m*is large compared to $A,P$ , to show equation ( 7.54) it thus suffices to show that

(7.55) $$ \begin{align} \mathbb{E} \exp\left( - \varepsilon^3 \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} )\right) \leq 10^{-A-1}. \end{align} $$

Since the left-hand side of equation ( 7.55) is at most

$$ \begin{align*}\mathbb{P}\left( \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} ) \leq \frac{10 A}{\varepsilon^3} \right) + \exp(-10A),\end{align*} $$

it will suffice to establish the bound

(7.56) $$ \begin{align} \mathbb{P}\left( \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} ) \leq \frac{10 A}{\varepsilon^3} \right) \leq 10^{-A-2} \end{align} $$

(say).

Roughly speaking, the estimate in equation ( 7.56) asserts that once one exits the large triangle $\Delta $ , then one should almost always encounter at least $10A/\varepsilon ^3$ white points by a certain time $P = O_{A,\varepsilon }(1)$ .

To prove equation ( 7.56), we introduce another random statistic that measures the number of triangles that one encounters on an infinite two-dimensional renewal process $(j',l'), (j',l') + \mathbf {v}_1, (j',l') + \mathbf {v} _{[1,2]},\dots $ , where $(j',l') \in (\mathbb {N}+1) \times \mathbb {Z}$ and $\mathbf {v}_1,\mathbf {v}_2,\dots $ are iid copies of $\mathbf {Hold}$ . (We will eventually set $(j',l') := (j,l) + \mathbf {v}_{[1,\mathbf {k}]}$ , so that the above renewal process is identical in distribution to $(j,l) + \mathbf {v}_{[1,\mathbf {k}]}$ , $(j,l) + \mathbf {v}_{[1,\mathbf {k}+1]}$ , $(j,l) + \mathbf {v}_{[1,\mathbf {k}+2]}, \dots $ .)

Given an initial point $(j',l') \in (\mathbb {N}+1) \times \mathbb {Z}$ , we recursively introduce the *stopping times*$\mathbf {t}_1 = \mathbf {t}_1(j',l'),\dots ,\mathbf {t}_{\mathbf {r}} = \mathbf {t}_{\mathbf {r}(j',l')}(j,l)$ by defining $\mathbf {t}_1$ to be the first natural number (if it exists) for which $(j',l') + \mathbf {v}_{[1,\mathbf {t}_1]}$ lies in a triangle $\mathbf {\Delta }_1 \in {\mathcal T}$ , then for each $i>1$ , defining $\mathbf {t}_i$ to be the first natural number (if it exists) with $l' + \mathbf {l}_{[1,\mathbf {t}_i]}> l_{\mathbf {\Delta }_{i-1}}$ and $(j',l') + \mathbf {v}_{[1,\mathbf {t}_i]}$ lies in a triangle $\mathbf {\Delta }_i \in {\mathcal T}$ . We set $\mathbf {r} = \mathbf {r}(j',l')$ to be the number of stopping times that can be constructed in this fashion (thus, there are no natural numbers *k*with $l + \mathbf {l}_{[1,k]}> l_{\mathbf {\Delta }_{\mathbf {r}}}$ and $(j',l') + \mathbf {v}_{[1,k]}$ black). Note that $\mathbf {r}$ is finite since the process $(j',l')+\mathbf {v}_{[1,k]}$ eventually exits the strip $[n/2] \times \mathbb {Z}$ when *k*is large enough, at which point it no longer encounters any black triangles.

The key estimate relating $\mathbf {r}$ with the expression in equation ( 7.56) is then

#### Lemma 7.9 (Many triangles usually implies many white points)

Let $\mathbf {v}_1,\mathbf {v}_2,\dots $ be iid copies of $\mathbf {Hold}$ . Then for any $(j',l') \in (\mathbb {N}+1) \times \mathbb {Z}$ and any positive integer *R*, we have

(7.57) $$ \begin{align} \mathbb{E} \exp\left( - \sum_{p=1}^{\mathbf{t}_{\min(\mathbf{r},R)}} 1_W((j',l') + \mathbf{v}_{[1,p]}) + \varepsilon \min(\mathbf{r},R) \right) \leq \exp(\varepsilon), \end{align} $$

where $0 < \varepsilon < 1/100$ is the sufficiently small absolute constant that has been in use throughout this section.

Informally the estimate in equation ( 7.57) asserts that when $\mathbf {r}$ is large (so that the renewal process $(j',l'), (j',l') + \mathbf {v}_1, (j',l') + \mathbf {v}_{[1,2]},\dots $ passes through many different triangles), then the quantity $\sum _{p=1}^{\mathbf {t}_{\min (\mathbf {r},R)}} 1_W((j',l') + \mathbf {v}_{[1,p]}$ is usually also large, implying that the same renewal process also visits many white points. This is basically due to the separation between triangles that is given by Lemma 7.4.

Proof. Denote the quantity on the left-hand side of equation ( 7.57) by $Z( (j',l'), R )$ . We induct on *R*. The case $R=1$ is trivial, so suppose $R \geq 2$ and that we have already established that

(7.58) $$ \begin{align} Z((j'',l''), R-1) \leq \exp(\varepsilon) \end{align} $$

for all $(j'',l'') \in (\mathbb {N}+1) \times \mathbb {Z}$ . If $\mathbf {r}=0$ , then we can bound

$$ \begin{align*}\exp\left( - \sum_{p=1}^{\mathbf{t}_{\min(\mathbf{r},R)}} 1_W((j',l') + \mathbf{v}_{[1,p]} ) + \varepsilon \min(\mathbf{r},R) \right) \leq 1.\end{align*} $$

Suppose that $\mathbf {r} \neq 0$ , so that the first stopping time $\mathbf {t}_1$ and triangle $\mathbf {\Delta }_1$ exists. Let $\mathbf {k}_1$ be the first natural number for which $l' + \mathbf {l}_{[1,\mathbf {k}_1]}> l_{\Delta _1}$ ; then $\mathbf {k}_1$ is well-defined (since we have an infinite number of $\mathbf {l}_k$ , all of which are at least $2$ ) and $\mathbf {k}_1> \mathbf {t}_1$ . The conditional expectation of $\exp ( - \sum _{p=1}^{\mathbf {t}_{\min (\mathbf {r},R)}} 1_W((j',l') + \mathbf {v}_{[1,p]} ) + \varepsilon \min (\mathbf {r},R))$ relative to the random variables $\mathbf {v}_1,\dots ,\mathbf {v}_{\mathbf {k}_1}$ is equal to

$$ \begin{align*}\exp\left( - \sum_{p=1}^{\mathbf{k}_1} 1_W((j',l') + \mathbf{v}_{[1,p]} ) + \varepsilon \right) Z( 1_W((j',l') + \mathbf{v} _{[1,\mathbf{k}_1]}, R-1)\end{align*} $$

which we can upper bound using the inductive hypothesis in equation ( 7.58) as

$$ \begin{align*}\exp\left( - 1_W((j',l') + \mathbf{v}_{[1,\mathbf{k}_1]} ) + 2\varepsilon \right).\end{align*} $$

We thus obtain the inequality

$$ \begin{align*}Z( (j',l'), R) \leq \mathbb{P}( \mathbf{r} = 0 ) + \exp(2\varepsilon) \mathbb{E} 1_{\mathbf{r} \neq 0} \exp( - 1_W((j',l') + \mathbf{v}_{[1,\mathbf{k}_1]} ) ) \end{align*} $$

so to close the induction it suffices to show that

$$ \begin{align*}\mathbb{E} 1_{\mathbf{r} \neq 0} \exp( - 1_W((j',l') + \mathbf{v}_{[1,\mathbf{k}_1]} ) ) \leq \exp(-\varepsilon) \mathbb{P}( \mathbf{r} \neq 0).\end{align*} $$

Since the left-hand side is equal to

$$ \begin{align*}\mathbb{P}( \mathbf{r} \neq 0 ) - (1-1/e) \mathbb{P}( (\mathbf{r} \neq 0) \wedge ((j',l') + \mathbf{v}_{[1,\mathbf{k}_1]} \in W) )\end{align*} $$

and $\varepsilon>0$ is a sufficiently small absolute constant, it will thus suffice to establish the bound

$$ \begin{align*}\mathbb{P}( (\mathbf{r} \neq 0) \wedge ((j',l') + \mathbf{v}_{[1,\mathbf{k}_1]} \in W) ) \gg \mathbb{P}( \mathbf{r} \neq 0 ).\end{align*} $$

For each $p \in \mathbb {N}+1$ , triangle $\Delta _1 \in {\mathcal T}$ , and $(j'',l'') \in \Delta _1$ , let $E_{p,\Delta _1,(j'',l'')}$ denote the event that $(j',l') + \mathbf {v}_{[1,p]} = (j'',l'')$ , and $(j',l') + \mathbf {v} _{[1,p']} \in W$ for all $1 \leq p' < p$ . Observe that the event $\mathbf {r} \neq 0$ is the disjoint union of the events $E_{p,\Delta _1,(j'',l'')}$ . It therefore suffices to show that

(7.59) $$ \begin{align} \mathbb{P}\left( E_{p,\Delta_1,(j'',l'')} \wedge ((j',l') + \mathbf{v}_{[1,\mathbf{k}_1]} \in W) \right) \gg \mathbb{P}( E_{p,\Delta_1,(j'',l'')} ). \end{align} $$

We may of course assume that the event $E_{p,\Delta _1,(j'',l'')}$ occurs with non-zero probability. Conditioning to this event, we see that $(j',l') + \mathbf {v}_{[1,\mathbf {k}_1]}$ has the same distribution as (the unconditioned random variable) $(j'',l'') + \mathbf {v}_{[1,\mathbf {k}'']}$ , where the first passage time $\mathbf {k}''$ is the first natural number for which $l'' + \mathbf {l}_{[1,\mathbf {k}'']}> l_{\Delta _1}$ . By repeating the proof of equation ( 7.51), one has

$$ \begin{align*}\mathbb{P}( (j'',l'') + \mathbf{v}_{[1,\mathbf{k}'']} \in W | E_{p,\Delta_1,(j'',l'')} ) \gg 1 \end{align*} $$

giving equation ( 7.59). This establishes the lemma.

To use this bound we need to show that the renewal process $(j,l)+\mathbf {v}_{[1,\mathbf {k}]}, (j,l) + \mathbf {v}_{[1,\mathbf{k}+1]}, (j,l) + \mathbf {v}_{[1,\mathbf {k}+2]},\dots $ passes either through many white points or through many triangles. This will be established via a probabilistic upper bound on the size $s_\Delta $ of the triangles encountered. The key lemma in this regard is

#### Lemma 7.10 (Large triangles are rarely encountered shortly after a lengthy crossing)

Let $(j,l)$ be an element of a black triangle $\Delta $ with $s := l_\Delta - l$ obeying $s> \frac {m}{\log ^2 m}$ (where we recall $m = \lfloor n/2\rfloor - j$ ), and let $\mathbf {k}$ be the first passage time associated to *s*defined in Lemma 7.7. Let $p \in \mathbb {N}$ and $1 \leq s' \leq m^{0.4}$ . Let $E_{p,s'}$ denote the event that $(j,l) + \mathbf {v} _{[1,\mathbf {k}+p]}$ lies in a triangle $\Delta ' \in {\mathcal T}$ of size $s_{\Delta '} \geq s'$ . Then

$$ \begin{align*}\mathbb{P}( E_{p,s'} ) \ll A^2 \frac{1+p}{s'} + \exp( - c A^2 (1+p) ).\end{align*} $$

As in the rest of this section, we stress that the implied constants in our asymptotic notation are uniform in *n*and $\xi $ .

Proof. We can assume that

(7.60) $$ \begin{align} s' \geq C A^2 (1+p) \end{align} $$

for a large constant *C*, since the claim is trivial otherwise.

From Lemma 7.7, we have equation ( 7.48) as before, so on summing in $j'$ , we have

$$ \begin{align*}\mathbb{P}( l + \mathbf{l}_{[1,k]} = l' ) \ll \exp( - c (l'-l_\Delta) )\end{align*} $$

and thus

$$ \begin{align*}\mathbb{P}( l + \mathbf{l}_{[1,k]} \geq l_\Delta + A^2 (1+p) ) \ll \exp( - c A^2 (1+p) ).\end{align*} $$

Similarly, from Lemma 2.2, one has

$$ \begin{align*}\mathbb{P}( \mathbf{l}_{[\mathbf{k}+1,\mathbf{k}+p]} \geq A^2 (1+p) ) \ll \exp( - c A^2 (1+p) )\end{align*} $$

and thus

$$ \begin{align*}\mathbb{P}( l + \mathbf{l}_{[1,\mathbf{k}+p]} \geq l_\Delta + 2A^2 (1+p) ) \ll \exp( - c A^2 (1+p) ).\end{align*} $$

In a similar spirit, from equation ( 7.48) and summing in $l'$ one has

$$ \begin{align*}\mathbb{P}( j + \mathbf{j}_{[1,\mathbf{k}]} = j' ) \ll s^{-1/2} G_{1+s}\left( c\left(j'-j - \frac{s}{4}\right) \right)\end{align*} $$

so in particular

$$ \begin{align*}\mathbb{P}\left( \left|\mathbf{j}_{[1,\mathbf{k}]} - \frac{s}{4}\right| \geq s^{0.6} \right) \ll \exp( - c s^{0.2} ) \ll A^2 \frac{1+p}{s'}\end{align*} $$

from the upper bound on $s'$ . From Lemma 2.2, we also have

$$ \begin{align*}\mathbb{P}( |\mathbf{j}_{[\mathbf{k}+1,\mathbf{k}+p]}| \geq s^{0.6} ) \ll \exp( - c s^{0.6} ) \ll A^2 \frac{1+p}{s'}\end{align*} $$

and hence

$$ \begin{align*}\mathbb{P}\left( \left|\mathbf{j}_{[1,\mathbf{k}+p]} - \frac{s}{4}\right| \geq 2s^{0.6} \right) \ll A^2 \frac{1+p}{s'}.\end{align*} $$

Thus, if $E'$ denotes the event that $l + \mathbf {l}_{[1,\mathbf {k}+p]} \geq l_\Delta + 2A^2 (1+p)$ or $|\mathbf {j}_{[1,\mathbf {k}+p]} - \frac {s}{4}| \geq 2s^{0.6}$ , then

(7.61) $$ \begin{align} \mathbb{P}( E') \ll A^2 \frac{1+p}{s'} + \exp( - c A^2 (1+p) ). \end{align} $$

We will devote the rest of the proof to establishing the complementary estimate

(7.62) $$ \begin{align} \mathbb{P}( E_{p,s'} \wedge \bar{E'}) \ll A^2 \frac{1+p}{s'} \end{align} $$

which together with equation ( 7.61) implies the lemma.

Suppose now that we are outside the event $E'$ , and that $(j,l) + \mathbf {v}_{[1,\mathbf {k}+p]}$ lies in a triangle $\Delta '$ ; thus

(7.63) $$ \begin{align} l + \mathbf{l}_{[1,\mathbf{k}+p]} = l_\Delta + O( A^2 (1+p) ) \end{align} $$

and

(7.64) $$ \begin{align} \mathbf{j}_{[1,\mathbf{k}+p]} = \frac{s}{4} + O(s^{0.6}) = \frac{s}{4} + O(m^{0.6}) \end{align} $$

thanks to equation ( 7.52). From equation ( 7.11), we then have

(7.65) $$ \begin{align} 0 \leq j+\mathbf{j}_{[1,\mathbf{k}+p]}-j_{\Delta'} \leq \frac{1}{\log 9} s_{\Delta'} - \frac{\log 2}{\log 9} (l_{\Delta'}-l-\mathbf{l}_{[1,\mathbf{k}+p]}). \end{align} $$

Suppose that the lower tip of $\Delta '$ lies well below the upper edge of $\Delta $ in the sense that

$$ \begin{align*}l_{\Delta'} - \frac{s_{\Delta'}}{\log 2} \leq l_\Delta - 10.\end{align*} $$

Then by equation ( 7.63), we can find an integer $j' = j+\mathbf {j}_{[1,\mathbf {k}+p]} + O( A^2 (1+p) )$ such that $j' \geq j_{\Delta '}$ and

$$ \begin{align*}0 \leq j'-j_{\Delta'} \leq \frac{1}{\log 9} s_{\Delta'} - \frac{\log 2}{\log 9} (l_{\Delta'}-l_\Delta).\end{align*} $$

In other words, $(j',l_\Delta ) \in \Delta '$ . But by equation ( 7.64), we have

$$ \begin{align*}j' = j + \frac{s}{4} + O(m^{0.6}) + O( A^2 (1+p) ) = j + \frac{s}{4} + O(m^{0.6}).\end{align*} $$

From equation ( 7.11), we have

$$ \begin{align*}0 \leq (j-j_\Delta) \log 9 \leq s_\Delta - s \log 2\end{align*} $$

and hence (since $s \geq \frac {m}{\log ^2 m}$ and $\frac {1}{4} \log 9 < \log 2$ )

$$ \begin{align*}0 \leq (j'-j_\Delta) \log 9 \leq s_\Delta.\end{align*} $$

Thus $(j',l_\Delta ) \in \Delta $ . Thus $\Delta $ and $\Delta '$ intersect, which by Lemma 7.4 forces $\Delta =\Delta '$ , which is absurd since $(j,l) + \mathbf {v}_{[1,\mathbf {k}+p]}$ lies in $\Delta '$ but not $\Delta $ (the *l*coordinate is larger than $l_\Delta $ ). We conclude that

$$ \begin{align*}l_{\Delta'} - \frac{s_{\Delta'}}{\log 2}> l_\Delta - 10.\end{align*} $$

On the other hand, from equation ( 7.11), we have

$$ \begin{align*}l_{\Delta'} - \frac{s_{\Delta'}}{\log 2} \leq l + \mathbf{l}_{[1,\mathbf{k}+p]}\end{align*} $$

hence by equation ( 7.63), we have

(7.66) $$ \begin{align} l_{\Delta'} - \frac{s_{\Delta'}}{\log 2} = l_\Delta + O( A^2 (1+p) ). \end{align} $$

From equations ( 7.65), ( 7.66) and ( 7.63), we then have

$$ \begin{align*} 0 \leq j + \mathbf{j}_{[1,\mathbf{k}+p]} - j_{\Delta'} &\leq \frac{1}{\log 9} s_{\Delta'} - \frac{\log 2}{\log 9} (l_{\Delta'} - l - \mathbf{l}_{[1,\mathbf{k}+p]}) \\ &= -\frac{\log 2}{\log 9} (l_\Delta - l - \mathbf{l}_{[1,\mathbf{k}+p]} + O(A^2(1+p)) ) \\ &= O( A^2 (1+p) ) \end{align*} $$

so that

$$ \begin{align*}j + \mathbf{j}_{[1,\mathbf{k}+p]} = j_{\Delta'} + O( A^2 (1+p) ).\end{align*} $$

Thus, outside the event $E'$ , the event that $(j,l) + \mathbf {v}_{[1,\mathbf {k}+p]}$ lies in a triangle $\Delta '$ can only occur if $(j,l) + \mathbf {v}_{[1,\mathbf {k}+p]}$ lies within a distance $O(A^2(1+p))$ of the point $(j_{\Delta '}, l_\Delta )$ .

Now suppose we have two distinct triangles $\Delta ', \Delta ''$ in ${\mathcal T}$ obeying equation ( 7.66), with $s_{\Delta '}, s_{\Delta ''} \geq s'$ with $j_{\Delta '} \leq j_{\Delta ''}$ . Set $l_* := l_\Delta + \lfloor s'/2 \rfloor $ , and observe from equation ( 7.11) that $(j_*,l_*) \in \Delta '$ whenever $j_*$ lies in the interval

$$ \begin{align*}j_{\Delta'} \leq j_* \leq j_{\Delta'} + \frac{1}{\log 9} s_{\Delta'} - \frac{\log 2}{\log 9} (l_{\Delta'} - l_*)\end{align*} $$

and similarly $(j_*,l_*) \in \Delta ''$ whenever

$$ \begin{align*}j_{\Delta''} \leq j_* \leq j_{\Delta''} + \frac{1}{\log 9} s_{\Delta''} - \frac{\log 2}{\log 9} (l_{\Delta''} - l_*).\end{align*} $$

By Lemma 7.4, these two intervals cannot have any integer point in common; thus

$$ \begin{align*}j_{\Delta'} + \frac{1}{\log 9} s_{\Delta'} - \frac{\log 2}{\log 9} (l_{\Delta'} - l_*) \leq j_{\Delta''}.\end{align*} $$

Applying equation ( 7.66) and the definition of $l_*$ , we conclude that

$$ \begin{align*}j_{\Delta'} + \frac{1}{2} \frac{\log 2}{\log 9} s' + O( A^2 (1+p) )\leq j_{\Delta''}\end{align*} $$

and hence by equation ( 7.60)

$$ \begin{align*}j_{\Delta''} - j_{\Delta'} \gg s'.\end{align*} $$

We conclude that for the triangles $\Delta '$ in ${\mathcal T}$ obeying equation ( 7.66) with $s_{\Delta '} \geq s'$ , the points $(j_{\Delta '}, l_\Delta )$ are $\gg s'$ -separated. Let $\Sigma $ denote the collection of such points; thus $\Sigma $ is a $\gg s'$ -separated set of points, and outside of the event $E'$ , $(j,l) + \mathbf {v}_{[1,\mathbf {k}+p]}$ can only occur in a triangle $\Delta '$ with $s_{\Delta '} \geq s'$ if

$$ \begin{align*}{\operatorname{dist}}( (j,l) + \mathbf{v}_{[1,\mathbf{k}+p]}, \Sigma ) \ll A^2(1+p).\end{align*} $$

We conclude that

$$ \begin{align*}\mathbb{P}( E_{p,s'} \wedge \bar{E'} ) \ll \mathbb{P}\left( {\operatorname{dist}}( (j,l) + \mathbf{v}_{[1,\mathbf{k}+p]}, \Sigma ) \ll A^2(1+p) \right).\end{align*} $$

From equation ( 7.48), we see that

$$ \begin{align*} &\mathbb{P}\left( (j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} = (j_{\Delta'},l_\Delta) + O( A^2(1+p) ) \right)\\ &\quad\quad\ll \frac{A^2(1+p)}{s^{1/2}} G_{1+s}\left( c \left(j_{\Delta'}-j - \frac{s}{4}\right) \right)\\ &\quad\quad\ll \frac{A^2(1+p)}{s'} \sum_{j' = j_{\Delta'} + O(s')} \frac{1}{s^{1/2}} G_{1+s}\left( c \left(j'-j - \frac{s}{4}\right) \right). \end{align*} $$

Summing and using the $\gg s'$ -separated nature of $\Sigma $ , we conclude that

$$ \begin{align*} \mathbb{P}\left( {\operatorname{dist}}( (j,l) + \mathbf{v}_{[1,\mathbf{k}+p]}, \Sigma ) \ll A^2(1+p) \right) &\ll \frac{A^2(1+p)}{s'} \sum_{j' \in \mathbb{Z}} \frac{1}{s^{1/2}} G_{1+s}\left( c \left(j'-j - \frac{s}{4}\right) \right) \\ &\ll \frac{A^2(1+p)}{s'} \end{align*} $$

and the claim in equation ( 7.62) follows.

From Lemma 7.10, we have

$$ \begin{align*}\mathbb{P}( E_{p,4^A (1+p)^3} ) \ll A^2 \frac{1}{4^A (1+p)^2} + \exp( - c A^2 (1+p) )\end{align*} $$

whenever $0 \leq p \leq m^{0.1}$ . Thus by the union bound, if $E_*$ denotes the union of the $E_{p,4^A (1+p)^3}$ for $0 \leq p \leq m^{0.1}$ , then

$$ \begin{align*}\mathbb{P}( E_*) \ll A^2 4^{-A}.\end{align*} $$

Next, we apply Lemma 7.9 with $(j',l') := (j,l) + \mathbf {v}_{[1,\mathbf {k}]}$ to conclude that

$$ \begin{align*}\mathbb{E} \exp\left( - \sum_{p=1}^{\mathbf{t}_{\min(\mathbf{r},R)}} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} + \varepsilon \min(\mathbf{r},R) \right) \leq \exp(\varepsilon),\end{align*} $$

where now $\mathbf {r} = \mathbf {r}((j,l) + \mathbf {v}_{[1,\mathbf {k}]})$ and $\mathbf {t}_i = \mathbf {t}_i((j,l) + \mathbf {v}_{[1,\mathbf {k}]})$ . If we then let $F_*$ to be the event that

$$ \begin{align*}\exp\left( - \sum_{p=1}^{\mathbf{t}_{\min(\mathbf{r},R)}} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} + \varepsilon \min(\mathbf{r},R) \right)> 10^{A+2} \exp(\varepsilon)\end{align*} $$

then by Markov’s inequality we have

$$ \begin{align*}\mathbb{P}( F_*) \leq 10^{-A-2}.\end{align*} $$

Outside of the event $F_*$ , we have

$$ \begin{align*}\exp\left( - \sum_{p=1}^{\mathbf{t}_{\min(\mathbf{r},R)}} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} + \varepsilon \min(\mathbf{r},R) \right) \ll 10^A\end{align*} $$

which implies that

$$ \begin{align*}\sum_{p=1}^{\mathbf{t}_{\min(\mathbf{r},R)}} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]}) \gg \varepsilon \min(\mathbf{r},R) - O( A ).\end{align*} $$

In particular, if we set $R := \lfloor A^2 / \varepsilon ^4\rfloor $ , we have

(7.67) $$ \begin{align} \sum_{p=1}^{\mathbf{t}_{R}} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]}) \gg \frac{A^2}{\varepsilon^3} \end{align} $$

whenever we lie outside of $F_*$ and $\mathbf {r} \geq R$ .

Now suppose we lie outside of both $E_*$ and $F_*$ , so in particular equation ( 7.67) holds. To prove equation ( 7.56), it will now suffice to show the deterministic claim

(7.68) $$ \begin{align} \sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} )> \frac{10 A}{\varepsilon^3}. \end{align} $$

We argue by contradiction. Suppose that equation ( 7.68) fails; thus

$$ \begin{align*}\sum_{p=0}^{P-1} 1_W((j,l) + \mathbf{v}_{[1,\mathbf{k}+p]} ) \leq \frac{10 A}{\varepsilon^3}.\end{align*} $$

Then the point $(j,l) + \mathbf {v}_{[1,\mathbf {k}+p]}$ is white for at most $10 A/\varepsilon ^3$ values of $0 \leq p \leq P-1$ , so in particular for *P*large enough there is $0 \leq p \leq 10A/\varepsilon ^3+1 = O_{A,\varepsilon }(1)$ such that $(j,l) + \mathbf {v} _{[1,\mathbf {k}+p]}$ is black. By Lemma 7.4, this point lies in a triangle $\Delta ' \in {\mathcal T}$ . As we are outside $E_*$ , the event $E_{p,4^A(1+p^3)}$ fails, so we have

$$ \begin{align*}s_{\Delta'} < 4^A (1+p)^3.\end{align*} $$

Thus by equation ( 7.11), for $p'$ in the range

$$ \begin{align*}p + 10 \times 4^A (1+p)^3 < p' \leq P-1,\end{align*} $$

we must have $l + \mathbf {l}_{[1,\mathbf {k}+p']}> l_{\Delta '}$ , hence we exit $\Delta '$ (and increment the random variable $\mathbf {r}$ ). In particular, if

$$ \begin{align*}p + 10 \times 4^A (1+p)^3 + 10 A/\varepsilon^3 + 1 \leq P-1,\end{align*} $$

then we can find

$$ \begin{align*}p' \leq p + 10 \times 4^A (1+p)^3 + 10 A/\varepsilon^3 + 1 = O_{p,A,\varepsilon}(1)\end{align*} $$

such that $l + \mathbf {l}_{[1,\mathbf {k}+p']}> l_{\Delta '}$ and $(j,l) + \mathbf {v}_{[1,\mathbf {k} +p]}$ is black (and therefore lies in a new triangle $\Delta ''$ ). Iterating this *R*times, we conclude (if *P*is sufficiently large depending on $A,\varepsilon $ ) that $\mathbf {r} \geq R$ and that $\mathbf {t}_R \leq P$ . Choosing *P*large enough so that all the previous arguments are justified, the claim in equation ( 7.68) now follows from equation ( 7.67), giving the required contradiction. This (finally!) concludes the proof of equation ( 7.41), and hence Proposition 7.8. As discussed previously, this implies Propositions 7.3, 7.1, 1.17 and Theorem 1.3.

## Acknowledgments

The author thanks Marek Biskup for useful discussions and Ben Green, Matthias Hippold, Alex Kontorovich, Alexandre Patriota, Sankeerth Rao, Mary Rees, Lior Silberman and several anonymous commenters on his blog for corrections and other comments. We are especially indebted to the anonymous referee for a careful reading and many useful suggestions.

## Conflicts of interest

None.

## Financial support

The author is supported by NSF grant DMS-1764034 and by a Simons Investigator Award.

---

## Footnotes

1 In this paper, all random variables will be denoted by boldface symbols, to distinguish them from purely deterministic quantities that will be denoted by non-boldface symbols. When it is only the distribution of the random variable that is important, we will use multi-character boldface symbols such as $\mathbf {Log}$ , $\mathbf {Unif}$ or $\mathbf {Geom}$ to denote the random variable, but when the dependence or independence properties of the random variable are also relevant, we shall usually use single-character boldface symbols such as $\mathbf {a}$ or $\mathbf {j}$ instead.

2 Indeed, if the latter assertion failed, then there exists a $\delta $ such that the set $\{ N \in \mathbb {N}+1: {\operatorname {Col}}_{\min }(N) \leq C\}$ has lower logarithmic density less than $1-\delta $ for every *C*. A routine diagonalisation argument then shows that there exists a function *f*growing to infinity such that $\{ N \in \mathbb {N}+1: {\operatorname {Col}}_{\min }(N) \leq f(N)\}$ has lower logarithmic density at most $1-\delta $ , contradicting Theorem 1.3.

3 We thank Ben Green for this observation.

4 As an alternative to reversing the order of the tuple $(\mathbf {a}_1,\dots ,\mathbf {a}_n)$ , one could instead index time by the negative integers $-1,-2,-3,\dots $ rather than the positive integers $1,2,3,\dots $ , viewing $\mathbf {Syrac}(\mathbb {Z}_3)$ as the outcome of an ‘ancient’ Syracuse iteration that extends to arbitrarily large negative times (and whose initial condition is irrelevant). This perspective toward the Syracuse variables is arguably more natural and could be adopted elsewhere in the paper; however, we have chosen (mostly for aesthetic reasons) to index time by positive integers rather than negative ones, which necessitates some reversal of the labeling at some junctures.

5 This Markov process may possibly be related to the $3$ -adic Markov process for the *inverse*Collatz map studied in [Reference Wirsching 24]. See also a recent investigation of $3$ -adic irregularities of the Collatz iteration in [Reference Thomas 23].

6 We thank the anonymous referee for suggesting this formulation of the main theorem.

7 Note that we have reversed the order of variables $\mathbf {a}_1,\dots ,\mathbf {a}_n$ from that in equation ( 1.5), as this will be a slightly more convenient normalization for the arguments in this section.

8 This choice of notation was chosen purely in order to be consistent with the color choices in Figures 2, 3, 4.

9 We are indebted to Marek Biskup for this suggestion.

---

## References

[1]

Allouche, J.-P., *Sur la conjecture de “Syracuse-Kakutani-Collatz”*, Séminaire de Théorie des Nombres, 1978–1979, Exp. No. 9, 15 pp., CNRS, Talence, 1979. [Google Scholar][15]

[2]

Baker, A., *Linear forms in the logarithms of algebraic numbers. I*, Mathematika. A Journal of Pure and Applied Mathematics, 13 ( 1966), 204 – 216. [Google Scholar][16]

[3]

Barina, D., *Convergence verification of the Collatz problem*, The Journal of Supercomputing, 2020. [Google Scholar][17]

[4]

Bourgain, J., *Periodic nonlinear Schrödinger equation and invariant measures*, Comm. Math. Phys. 166 ( 1994), 1 – 26. [CrossRef][18] [Google Scholar][19]

[5]

Carletti, T., Fanelli, D., *Quantifying the degree of average contraction of Collatz orbits*, Boll. Unione Mat. Ital. 11 ( 2018), 445 – 468. [CrossRef][20] [Google Scholar][21]

[6]

Chamberland, M., A $3x+1$ survey: number theory and dynamical systems, The ultimate challenge: the $3x+1$ problem, 57 – 78, Amer. Math. Soc., Providence, RI, 2010. [Google Scholar][22]

[7]

Crandall, R. E., *On the*‘ $3x+1$ ’ *problem*, Math. Comp. 32 ( 1978), 1281 – 1292. [Google Scholar][23]

[8]

Everett, C. J., Iteration of the number-theoretic function $f(2n)=n$ , $f\left(2n+1\right)=3n+2$ , Adv. Math. 25 ( 1977), no. 1, 42 – 45. [CrossRef][24] [Google Scholar][25]

[9]

Korec, I., *A density estimate for the*$3x+1$ *problem*, Math. Slovaca 44 ( 1994), no. 1, 85 – 89. [Google Scholar][26]

[10]

Kontorovich, A., Lagarias, J., *Stochastic models for the*$3x+1$ *and*$5x+1$ *problems and related problems*, The ultimate challenge: the $3x+1$ problem, 131 – 188, Amer. Math. Soc., Providence, RI, 2010. [Google Scholar][27]

[11]

Kontorovich, A., Miller, S. J., *Benford’s law, values of*$L$ *-functions and the*$3x+1$ *problem*, Acta Arith. 120 ( 2005), no. 3, 269 – 297. [CrossRef][28] [Google Scholar][29]

[12]

Kontorovich, A. V., Sinai, Ya. G., *Structure theorem for*$\left(d,g,h\right)$ *-maps*, Bull. Braz. Math. Soc. (N.S.) 33 ( 2002), no. 2, 213 – 224. [CrossRef][30] [Google Scholar][31]

[13]

Krasikov, I., Lagarias, J., *Bounds for the*$3x+1$ *problem using difference inequalities*, Acta Arith. 109 ( 2003), 237 – 258. [CrossRef][32] [Google Scholar][33]

[14]

Lagarias, J., *The 3x+1 problem and its generalizations*, Amer. Math. Monthly 92 ( 1985), no. 1, 3 – 23. [CrossRef][34] [Google Scholar][35]

[15]

Lagarias, J., Soundararajan, K., *Benford’s law for the*$3x+1$ *function*, J. London Math. Soc. (2) 74 ( 2006), no. 2, 289 – 303. [CrossRef][36] [Google Scholar][37]

[16]

Lagarias, J., Weiss, A., *The*$3x+1$ *problem: two stochastic models*, Ann. Appl. Probab. 2 ( 1992), no. 1, 229 – 261. [CrossRef][38] [Google Scholar][39]

[17]

Oliveira e Silva, T., *Empirical verification of the 3x+1 and related conjectures*, The ultimate challenge: the $3x+1$ problem, 189 – 207, Amer. Math. Soc., Providence, RI, 2010. [Google Scholar][40]

[18]

Roosendaal, E., [www.ericr.nl/wondrous][41]. [Google Scholar][42]

[19]

Sinai, Ya. G., *Statistical*$\left(3x+1\right)$ *problem*, Dedicated to the memory of Jürgen K. Moser. Comm. Pure Appl. Math. 56 ( 2003), no. 7, 1016 – 1028. [CrossRef][43] [Google Scholar][44]

[20]

Tao, T., *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum Math. Pi 4 ( 2016), e8, 36 pp. [CrossRef][45] [Google Scholar][46]

[21]

Terras, R., *A stopping time problem on the positive integers*, Acta Arith. 30 ( 1976), 241 – 252. [CrossRef][47] [Google Scholar][48]

[22]

Terras, R., *On the existence of a density*, Acta Arith. 35 ( 1979), 101 – 102. [CrossRef][49] [Google Scholar][50]

[23]

Thomas, A., *A non-uniform distribution property of most orbits, in case the*$3x+1$ *conjecture is true*, Acta Arith. 178 ( 2017), no. 2, 125 – 134. [CrossRef][51] [Google Scholar][52]

[24]

Wirsching, G., The Dynamical System Generated by the $3n+1$ Function, Lecture Notes in Math. No. 1681, Springer-Verlag: Berlin 1998. [Google Scholar][53]

View in content [image: Figure 0]

Figure 1 The Syracuse orbit $n \mapsto \mathrm {Syr}^n(\mathbf {N}_y)$, where the vertical axis is drawn in shifted log-scale. The diagonal lines have slope $-\log (4/3)$. For times n up to $n_0$, the orbit usually stays close to the dashed line and hence usually lies between the two dotted diagonal lines; in particular, the first passage time $T_x(\mathbf {N}_y)$ will usually lie in the interval $I_y$. Outside of a rare exceptional event, for any given $n \in I_y$, ${\operatorname {Syr}}^{n-m}(\mathbf {N}_y)$ will lie in $E'$ if and only if $n = T_x(\mathbf {N}_y)$ and ${\operatorname {Syr}}^n(\mathbf {N}_y)$ lies in E; equivalently, outside of a rare exceptional event, ${\operatorname {Pass}}_x(\mathbf {N}_y)$ lies in E if and only if ${\operatorname {Syr}}^{n-m}(\mathbf {N}_y)$ lies in $E'$ for precisely one $n \in I_y$.

---

View in content [image: Figure 1]

Figure 2 A triangle $\Delta $, which we have drawn as a solid region rather than as a subset of the discrete lattice $\mathbb {Z}^2$.

---

View in content [image: Figure 2]

Figure 3 The black set is a union of triangles, in the strip $[\frac {n}{2} - \frac {1}{10} \log \frac {1}{\varepsilon }] \times \mathbb {Z}$, that are separated from each other by $\gg \log \frac {1}{\varepsilon }$. The red dots depict (a portion of) a renewal process $\mathbf {v}_1, \mathbf {v}_{[1,2]}, \mathbf {v}_{[1,3]}$ that we will encounter later in this section; our main objective will be to establish that this process usually contains a fair number of white points. We remark that the average slope $\frac {16}{4}=4$ of this renewal process will exceed the slope $\frac {\log 9}{\log 2} \approx 3.17$ of the triangle diagonals, so that the process tends to exit a given triangle through its horizontal side. The coordinate j increases in the rightward direction, while the coordinate l increases in the upward direction.

---

View in content [image: Figure 3]

Figure 4 The proof of Lemma 7.4. The points connecting $(j,l)$ to $(j,l_*)$, and from $(j,l_*)$ to $(j_*,l_*)$, are known to be black, while the points $(j, l_*+1), (j_*-1, l_*)$ are known to be white. The point $(j',l')$ can be in various locations, as illustrated by the red dots here. From equation (7.18), one can obtain that every point in the dashed triangle $\Delta _*$ is black (and every point in the Case 1 region is weakly black), which can treat the Case 1 locations of $(j',l')$ (and also forces $(j,l)$ to lie inside $\Delta _*$). In Case 2, $(j',l')$ can be to the right or left of $(j,l_*+1)$, but in either case one can show that if $(j',l')$ is black, then $(j',l_*+1)$ (displayed here in blue) is weakly black and hence $(j,l_*+1)$ is weakly black and in fact black, a contradiction. Similarly, in Case 3, $(j',l')$ can be above or below $(j_*-1,l_*)$, but in either case one can show that if $(j',l')$ is black, then so $(j_*-1,l')$ (displayed here in green) is weakly black and hence $(j_*-1,l_*)$ is weakly black and in fact black, again giving a contradiction.

You have Access Open access

25 Cited by

---

# Cited by

Loading...

Cited by

-

[image: Crossref logo] 25

-

[image: Google Scholar logo]

Crossref Citations

[image: Crossref logo] [54]

##### This article has been cited by the following publications. This list is generated based on data provided by [Crossref][54].

---

CARBÓ DORCA, Ramon and PERELMAN, Carlos 2022. *Boolean Hypercubes, Classification of Natural Numbers, and the Collatz Conjecture*. Journal of Mathematical Sciences and Modelling, Vol. 5, Issue. 3, p. 80.

- [CrossRef][55]
- [Google Scholar][56]

---

Zhang, Jinqing and Zhang, Xintong 2023. *Collatz Iterative Trajectories of All Odd Numbers Attain Bounded Values*. Journal of Applied Mathematics and Physics, Vol. 11, Issue. 10, p. 3030.

- [CrossRef][57]
- [Google Scholar][58]

---

Polli, J G Raposo, E P Viswanathan, G M and da Luz, M G E 2024. *Stochastic-like characteristics of arithmetic dynamical systems: the Collatz hailstone sequences*. Journal of Physics: Complexity, Vol. 5, Issue. 1, p. 015011.

- [CrossRef][59]
- [Google Scholar][60]

---

Béhani, Vincent 2024. *Linear dynamics of an operator associated to the Collatz map*. Proceedings of the American Mathematical Society, Vol. 152, Issue. 3, p. 1191.

- [CrossRef][61]
- [Google Scholar][62]

---

Du, Zhibin and Huang, Yinhao 2024. *Some extensions of Collatz (periodic) conjecture*. Applied Mathematics and Computation, Vol. 475, Issue. , p. 128742.

- [CrossRef][63]
- [Google Scholar][64]

---

Neklyudov, Mikhail 2024. *Functional Analysis Approach to the Collatz Conjecture*. Results in Mathematics, Vol. 79, Issue. 4,

- [CrossRef][65]
- [Google Scholar][66]

---

Dubickas, Artūras 2024. *A Class of Bounded Iterative Sequences of Integers*. Axioms, Vol. 13, Issue. 2, p. 107.

- [CrossRef][67]
- [Google Scholar][68]

---

Kosobutskyy, Petro Rebot, Dariia and Guzowski, Bartłomiej 2024. *STATISTICAL MODELING OF κ·q±1 DISCRETE DATA TRANSFORMATION SYSTEMS*. Computer Design Systems. Theory and Practice, Vol. 6, Issue. 2, p. 61.

- [CrossRef][69]
- [Google Scholar][70]

---

A.A, Durmagambetov and A.A, Durmagambetova 2024. *Collatz Conjecture*. PROOF, Vol. 4, Issue. , p. 85.

- [CrossRef][71]
- [Google Scholar][72]

---

Nathanson, Melvyn B. 2025. *Combinatorial and Additive Number Theory VI*. Vol. 464, Issue. , p. 371.

- [CrossRef][73]
- [Google Scholar][74]

---

LONGSTAFF, W. E. 2025. *MONOTONIC COLLATZ SUBSEQUENCES WITH TERMS CONGRUENT MODULO A FIXED POWER OF TWO*. Bulletin of the Australian Mathematical Society, Vol. 112, Issue. 3, p. 418.

- [CrossRef][75]
- [Google Scholar][76]

---

Ebnenasir, Ali 2025. *Stabilization, Safety, and Security of Distributed Systems*. Vol. 14931, Issue. , p. 417.

- [CrossRef][77]
- [Google Scholar][78]

---

Eliahou, Shalom and Verger-Gaugry, Jean-Louis 2025. *The number system in rational base 3/2 and the 3x+1 problem*. Comptes Rendus. Mathématique, Vol. 363, Issue. G4, p. 329.

- [CrossRef][79]
- [Google Scholar][80]

---

Diarte-Carot, Emilio A. 2025. *Solving the Collatz Conjecture, Using Gaussian Arithmetic*. Journal of Applied Mathematics and Physics, Vol. 13, Issue. 05, p. 1960.

- [CrossRef][81]
- [Google Scholar][82]

---

Tutaj, Edward and Tutaj-Gasinska, Halszka 2025. *Furstenberg Topology and Collatz Problem*. Axioms, Vol. 14, Issue. 4, p. 297.

- [CrossRef][83]
- [Google Scholar][84]

---

Kosobutskyy, Petro 2025. *The Jacobsthal-Collatz-Terras model of conjecture the natural numbers in <i>κq</i> + 1 problems*. Journal of AppliedMath, Vol. 3, Issue. 2, p. 1767.

- [CrossRef][85]
- [Google Scholar][86]

---

Fu, Weicheng and Wang, Yisen 2026. *The Structure of the Route to the Period-Three Orbit in the Collatz Map*. Mathematical and Computational Applications, Vol. 31, Issue. 1, p. 23.

- [CrossRef][87]
- [Google Scholar][88]

---

Carbó-Dorca, Ramon 2026. *Natural Numbers Generalized Parity, and the Collatz Algorithm*. Journal of Mathematical Sciences and Modelling, Vol. 9, Issue. 2, p. 137.

- [CrossRef][89]
- [Google Scholar][90]

---

Koyuncu, Selcuk Sathiyakumar, Thevasha Alayode, Praise Ellis, Christopher and Thomas, Peyton 2026. *Parity-Based Level-Set Approach to the Collatz Conjecture*. Mathematics, Vol. 14, Issue. 10, p. 1763.

- [CrossRef][91]
- [Google Scholar][92]

---

Alic, Nikola 2026. *Collatz Progressions Reframed: Exponent Representation, Algorithmic Hierarchies, and Record Computations*. IEEE Access, Vol. 14, Issue. , p. 98935.

- [CrossRef][93]
- [Google Scholar][94]

---

[Download full list][95]

Google Scholar Citations

View all [Google Scholar citations][96] for this article.

×

#

Cancel

Confirm

×

# Save article to Kindle

To send this article to your Kindle, first ensure no-reply@cambridge.org is added to your Approved Personal Document E-mail List under your Personal Document Settings on the Manage Your Content and Devices page of your Amazon account. Then enter the ‘name’ part of your Kindle email address below. Find out more about sending to your Kindle. [Find out more about saving to your Kindle][97].

Note you can select to save to either the @free.kindle.com or @kindle.com variations. ‘@free.kindle.com’ emails are free but can only be saved to your device when it is connected to wi-fi. ‘@kindle.com’ emails can be delivered even when you are not connected to wi-fi, but note that service fees apply.

Find out more about the [Kindle Personal Document Service.][98]

Almost all orbits of the Collatz map attain almost bounded values

- Volume 10
- [Terence Tao][99] [8] (a1)
- DOI: [https://doi.org/10.1017/fmp.2022.8][13]

Cancel

Save

×

# Save article to Dropbox

To save this article to your Dropbox account, please select one or more formats and confirm that you agree to abide by our usage policies. If this is the first time you used this feature, you will be asked to authorise Cambridge Core to connect with your Dropbox account. [Find out more about saving content to Dropbox][97].

Almost all orbits of the Collatz map attain almost bounded values

- Volume 10
- [Terence Tao][99] [8] (a1)
- DOI: [https://doi.org/10.1017/fmp.2022.8][13]

Cancel

Save

×

# Save article to Google Drive

To save this article to your Google Drive account, please select one or more formats and confirm that you agree to abide by our usage policies. If this is the first time you used this feature, you will be asked to authorise Cambridge Core to connect with your Google Drive account. [Find out more about saving content to Google Drive][97].

Almost all orbits of the Collatz map attain almost bounded values

- Volume 10
- [Terence Tao][99] [8] (a1)
- DOI: [https://doi.org/10.1017/fmp.2022.8][13]

Cancel

Save

×

×

#### Reply to: Submit a response


## Links

[1]: /core/
[2]: /core
[3]: /core/publications/journals
[4]: /core/journals/forum-of-mathematics-pi
[5]: /core/journals/forum-of-mathematics-pi/volume/10698C1D3340FD1019F9361A62AAEA70
[6]: /core/product/identifier/MSC_2010_ARITHMETIC_AND_NON_ARCHIMEDEAN_DYNAMICAL/type/BESPOKE_COLLECTION
[7]: /core/search?filters%5BauthorTerms%5D=Terence%20Tao&amp;eventCode=SE-AU
[8]: https://orcid.org/0000-0002-0140-7641
[9]: mailto:tao@math.ucla.edu
[10]: /core/services/aop-cambridge-core/content/view/1008CC2DF91AF87F66D190C5E01C907F/S2050508622000087a.pdf/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values.pdf
[11]: /core/search?filters[keywords]=Collatz conjecture
[12]: /core/search?filters[classificationCodesByType]=MSC%3B37P99%3BNone%20of%20the%20above%2C%20but%20in%20this%20section
[13]: https://doi.org/10.1017/fmp.2022.8
[14]: https://creativecommons.org/licenses/by/4.0/
[15]: https://scholar.google.com/scholar?q=[1]+Allouche,+J.-P.,+Sur+la+conjecture+de+“Syracuse-Kakutani-Collatz”,+Séminaire+de+Théorie+des+Nombres,+1978–1979,+Exp.+No.+9,+15+pp.,+CNRS,+Talence,+1979.
[16]: https://scholar.google.com/scholar_lookup?title=%0ALinear+forms+in+the+logarithms+of+algebraic+numbers.+I%0A&author=Baker+A.&publication+year=1966&journal=Mathematika.+A+Journal+of+Pure+and+Applied+Mathematics&volume=13&pages=204-216
[17]: https://scholar.google.com/scholar_lookup?title=%0AConvergence+verification+of+the+Collatz+problem%0A&author=Barina+D.&publication+year=2020&journal=The+Journal+of+Supercomputing
[18]: https://dx.doi.org/10.1007/BF02099299
[19]: https://scholar.google.com/scholar_lookup?title=%0APeriodic+nonlinear+Schr%C3%B6dinger+equation+and+invariant+measures%0A&author=Bourgain+J.&publication+year=1994&journal=Comm.+Math.+Phys.&volume=166&doi=10.1007%2FBF02099299&pages=1-26
[20]: https://dx.doi.org/10.1007/s40574-017-0145-x
[21]: https://scholar.google.com/scholar_lookup?title=%0AQuantifying+the+degree+of+average+contraction+of+Collatz+orbits%0A&author=Carletti+T.&author=Fanelli+D.&publication+year=2018&journal=Boll.+Unione+Mat.+Ital.&volume=11&doi=10.1007%2Fs40574-017-0145-x&pages=445-468
[22]: https://scholar.google.com/scholar_lookup?title=A+%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A+survey%3A+number+theory+and+dynamical+systems%2C+The+ultimate+challenge%3A+the+%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A+problem&author=Chamberland+M.&publication+year=2010
[23]: https://scholar.google.com/scholar_lookup?title=%0AOn+the+%E2%80%98%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%E2%80%99+problem%0A&author=Crandall+R.+E.&publication+year=1978&journal=Math.+Comp.&volume=32&pages=1281-1292
[24]: https://dx.doi.org/10.1016/0001-8708(77)90087-1
[25]: https://scholar.google.com/scholar_lookup?title=Iteration+of+the+number-theoretic+function+%0A%0A%0A%0A%24f(2n)%3Dn%24%0A%0A%0A%2C+%0A%0A%0A%0A%24f%5Cleft(2n%2B1%5Cright)%3D3n%2B2%24%0A%0A%0A%0A&author=Everett+C.+J.&publication+year=1977&journal=Adv.+Math.&volume=25&doi=10.1016%2F0001-8708(77)90087-1&pages=42-45
[26]: https://scholar.google.com/scholar_lookup?title=%0AA+density+estimate+for+the%0A%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%0Aproblem%0A&author=Korec+I.&publication+year=1994&journal=Math.+Slovaca&volume=44&pages=85-89
[27]: https://scholar.google.com/scholar?q=[10]+Kontorovich,+A.,+Lagarias,+J.,+Stochastic+models+for+the+$3x+1$+and+$5x+1$+problems+and+related+problems,+The+ultimate+challenge:+the+$3x+1$+problem,+131–188,+Amer.+Math.+Soc.,+Providence,+RI,+2010.
[28]: https://dx.doi.org/10.4064/aa120-3-4
[29]: https://scholar.google.com/scholar_lookup?title=%0ABenford%E2%80%99s+law%2C+values+of%0A%0A%0A%0A%0A%24L%24%0A%0A%0A%0A-functions+and+the%0A%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%0Aproblem%0A&author=Kontorovich+A.&author=Miller+S.+J.&publication+year=2005&journal=Acta+Arith.&volume=120&doi=10.4064%2Faa120-3-4&pages=269-297
[30]: https://dx.doi.org/10.1007/s005740200010
[31]: https://scholar.google.com/scholar_lookup?title=%0AStructure+theorem+for%0A%0A%0A%0A%0A%24%5Cleft(d%2Cg%2Ch%5Cright)%24%0A%0A%0A%0A-maps%0A&author=Kontorovich+A.+V.&author=Sinai+Ya.+G.&publication+year=2002&journal=Bull.+Braz.+Math.+Soc.+(N.S.)&volume=33&doi=10.1007%2Fs005740200010&pages=213-224
[32]: https://dx.doi.org/10.4064/aa109-3-4
[33]: https://scholar.google.com/scholar_lookup?title=%0ABounds+for+the%0A%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%0Aproblem+using+difference+inequalities%0A&author=Krasikov+I.&author=Lagarias+J.&publication+year=2003&journal=Acta+Arith.&volume=109&doi=10.4064%2Faa109-3-4&pages=237-258
[34]: https://dx.doi.org/10.1080/00029890.1985.11971528
[35]: https://scholar.google.com/scholar_lookup?title=%0AThe+3x%2B1+problem+and+its+generalizations%0A&author=Lagarias+J.&publication+year=1985&journal=Amer.+Math.+Monthly&volume=92&doi=10.1080%2F00029890.1985.11971528&pages=3-23
[36]: https://dx.doi.org/10.1112/S0024610706023131
[37]: https://scholar.google.com/scholar_lookup?title=%0ABenford%E2%80%99s+law+for+the%0A%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%0Afunction%0A&author=Lagarias+J.&author=Soundararajan+K.&publication+year=2006&journal=J.+London+Math.+Soc.+(2)&volume=74&doi=10.1112%2FS0024610706023131&pages=289-303
[38]: https://dx.doi.org/10.1214/aoap/1177005779
[39]: https://scholar.google.com/scholar_lookup?title=%0AThe%0A%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%0Aproblem%3A+two+stochastic+models%0A&author=Lagarias+J.&author=Weiss+A.&publication+year=1992&journal=Ann.+Appl.+Probab.&volume=2&doi=10.1214%2Faoap%2F1177005779&pages=229-261
[40]: https://scholar.google.com/scholar_lookup?title=Amer.+Math.+Soc.&author=Oliveira+e+Silva+T.&publication+year=2010&pages=189-207
[41]: http://www.ericr.nl/wondrous
[42]: https://scholar.google.com/scholar?q=[18]+Roosendaal,+E.,+www.ericr.nl/wondrous.
[43]: https://dx.doi.org/10.1002/cpa.10084
[44]: https://scholar.google.com/scholar_lookup?title=%0AStatistical%0A%0A%0A%0A%0A%24%5Cleft(3x%2B1%5Cright)%24%0A%0A%0A%0Aproblem%0A&author=Sinai+Ya.+G.&publication+year=2003&journal=Dedicated+to+the+memory+of+J%C3%BCrgen+K.+Moser.+Comm.+Pure+Appl.+Math&volume=56&doi=10.1002%2Fcpa.10084&pages=1016-1028
[45]: https://dx.doi.org/10.1017/fmp.2016.6
[46]: https://scholar.google.com/scholar_lookup?title=%0AThe+logarithmically+averaged+Chowla+and+Elliott+conjectures+for+two-point+correlations%0A&author=Tao+T.&publication+year=2016&journal=Forum+Math.+Pi&volume=4&doi=10.1017%2Ffmp.2016.6
[47]: https://dx.doi.org/10.4064/aa-30-3-241-252
[48]: https://scholar.google.com/scholar_lookup?title=%0AA+stopping+time+problem+on+the+positive+integers%0A&author=Terras+R.&publication+year=1976&journal=Acta+Arith.&volume=30&doi=10.4064%2Faa-30-3-241-252&pages=241-252
[49]: https://dx.doi.org/10.4064/aa-35-1-101-102
[50]: https://scholar.google.com/scholar_lookup?title=%0AOn+the+existence+of+a+density%0A&author=Terras+R.&publication+year=1979&journal=Acta+Arith.&volume=35&doi=10.4064%2Faa-35-1-101-102&pages=101-102
[51]: https://dx.doi.org/10.4064/aa8385-9-2016
[52]: https://scholar.google.com/scholar_lookup?title=%0AA+non-uniform+distribution+property+of+most+orbits%2C+in+case+the%0A%0A%0A%0A%0A%243x%2B1%24%0A%0A%0A%0Aconjecture+is+true%0A&author=Thomas+A.&publication+year=2017&journal=Acta+Arith.&volume=178&doi=10.4064%2Faa8385-9-2016&pages=125-134
[53]: https://scholar.google.com/scholar?q=[24]+Wirsching,+G.,+The+Dynamical+System+Generated+by+the+$3n+1$+Function,+Lecture+Notes+in+Math.+No.+1681,+Springer-Verlag:+Berlin+1998.
[54]: http://www.crossref.org/citedby/index.html
[55]: https://doi.org/10.33187/jmsm.972781
[56]: https://scholar.google.com/scholar_lookup?title#x3D;Boolean+Hypercubes+Classification+of+Natural+Numbers+and+the+Collatz+Conjecture&amp;author&#x3D;CARBÓ+DORCA+Ramon&amp;author&#x3D;PERELMAN+Carlos&amp;publication_year&#x3D;2022
[57]: https://doi.org/10.4236/jamp.2023.1110200
[58]: https://scholar.google.com/scholar_lookup?title#x3D;Collatz+Iterative+Trajectories+of+All+Odd+Numbers+Attain+Bounded+Values&amp;author&#x3D;Zhang+Jinqing&amp;author&#x3D;Zhang+Xintong&amp;publication_year&#x3D;2023
[59]: https://doi.org/10.1088/2632-072X/ad271f
[60]: https://scholar.google.com/scholar_lookup?title#x3D;Stochastic-like+characteristics+of+arithmetic+dynamical+systems:+the+Collatz+hailstone+sequences&amp;author&#x3D;Polli+J+G&amp;author&#x3D;Raposo+E+P&amp;author&#x3D;Viswanathan+G+M&amp;author&#x3D;da+Luz+M+G+E&amp;publication_year&#x3D;2024
[61]: https://doi.org/10.1090/proc/16627
[62]: https://scholar.google.com/scholar_lookup?title#x3D;Linear+dynamics+of+an+operator+associated+to+the+Collatz+map&amp;author&#x3D;Béhani+Vincent&amp;publication_year&#x3D;2024
[63]: https://doi.org/10.1016/j.amc.2024.128742
[64]: https://scholar.google.com/scholar_lookup?title#x3D;Some+extensions+of+Collatz+(periodic)+conjecture&amp;author&#x3D;Du+Zhibin&amp;author&#x3D;Huang+Yinhao&amp;publication_year&#x3D;2024
[65]: https://doi.org/10.1007/s00025-024-02167-7
[66]: https://scholar.google.com/scholar_lookup?title#x3D;Functional+Analysis+Approach+to+the+Collatz+Conjecture&amp;author&#x3D;Neklyudov+Mikhail&amp;publication_year&#x3D;2024
[67]: https://doi.org/10.3390/axioms13020107
[68]: https://scholar.google.com/scholar_lookup?title#x3D;A+Class+of+Bounded+Iterative+Sequences+of+Integers&amp;author&#x3D;Dubickas+Artūras&amp;publication_year&#x3D;2024
[69]: https://doi.org/10.23939/cds2024.02.061
[70]: https://scholar.google.com/scholar_lookup?title#x3D;STATISTICAL+MODELING+OF+κ·q±1+DISCRETE+DATA+TRANSFORMATION+SYSTEMS&amp;author&#x3D;Kosobutskyy+Petro&amp;author&#x3D;Rebot+Dariia&amp;author&#x3D;Guzowski+Bartłomiej&amp;publication_year&#x3D;2024
[71]: https://doi.org/10.37394/232020.2024.4.7
[72]: https://scholar.google.com/scholar_lookup?title#x3D;Collatz+Conjecture&amp;author&#x3D;A.A+Durmagambetov&amp;author&#x3D;A.A+Durmagambetova&amp;publication_year&#x3D;2024
[73]: https://doi.org/10.1007/978-3-031-65064-2_18
[74]: https://scholar.google.com/scholar_lookup?title#x3D;Combinatorial+and+Additive+Number+Theory+VI&amp;author&#x3D;Nathanson+Melvyn+B.&amp;publication_year&#x3D;2025
[75]: https://doi.org/10.1017/S0004972725000267
[76]: https://scholar.google.com/scholar_lookup?title#x3D;MONOTONIC+COLLATZ+SUBSEQUENCES+WITH+TERMS+CONGRUENT+MODULO+A+FIXED+POWER+OF+TWO&amp;author&#x3D;LONGSTAFF+W.+E.&amp;publication_year&#x3D;2025
[77]: https://doi.org/10.1007/978-3-031-74498-3_30
[78]: https://scholar.google.com/scholar_lookup?title#x3D;Stabilization+Safety+and+Security+of+Distributed+Systems&amp;author&#x3D;Ebnenasir+Ali&amp;publication_year&#x3D;2025
[79]: https://doi.org/10.5802/crmath.662
[80]: https://scholar.google.com/scholar_lookup?title#x3D;The+number+system+in+rational+base+3/2+and+the+3x+1+problem&amp;author&#x3D;Eliahou+Shalom&amp;author&#x3D;Verger-Gaugry+Jean-Louis&amp;publication_year&#x3D;2025
[81]: https://doi.org/10.4236/jamp.2025.135109
[82]: https://scholar.google.com/scholar_lookup?title#x3D;Solving+the+Collatz+Conjecture+Using+Gaussian+Arithmetic&amp;author&#x3D;Diarte-Carot+Emilio+A.&amp;publication_year&#x3D;2025
[83]: https://doi.org/10.3390/axioms14040297
[84]: https://scholar.google.com/scholar_lookup?title#x3D;Furstenberg+Topology+and+Collatz+Problem&amp;author&#x3D;Tutaj+Edward&amp;author&#x3D;Tutaj-Gasinska+Halszka&amp;publication_year&#x3D;2025
[85]: https://doi.org/10.59400/jam1767
[86]: https://scholar.google.com/scholar_lookup?title#x3D;The+Jacobsthal-Collatz-Terras+model+of+conjecture+the+natural+numbers+in+&lt;i&gt;κq&lt;/i&gt;+1+problems&amp;author&#x3D;Kosobutskyy+Petro+&amp;publication_year&#x3D;2025
[87]: https://doi.org/10.3390/mca31010023
[88]: https://scholar.google.com/scholar_lookup?title#x3D;The+Structure+of+the+Route+to+the+Period-Three+Orbit+in+the+Collatz+Map&amp;author&#x3D;Fu+Weicheng&amp;author&#x3D;Wang+Yisen&amp;publication_year&#x3D;2026
[89]: https://doi.org/10.33187/jmsm.1817738
[90]: https://scholar.google.com/scholar_lookup?title#x3D;Natural+Numbers+Generalized+Parity+and+the+Collatz+Algorithm&amp;author&#x3D;Carbó-Dorca+Ramon&amp;publication_year&#x3D;2026
[91]: https://doi.org/10.3390/math14101763
[92]: https://scholar.google.com/scholar_lookup?title#x3D;Parity-Based+Level-Set+Approach+to+the+Collatz+Conjecture&amp;author&#x3D;Koyuncu+Selcuk&amp;author&#x3D;Sathiyakumar+Thevasha&amp;author&#x3D;Alayode+Praise&amp;author&#x3D;Ellis+Christopher&amp;author&#x3D;Thomas+Peyton&amp;publication_year&#x3D;2026
[93]: https://doi.org/10.1109/ACCESS.2026.3704917
[94]: https://scholar.google.com/scholar_lookup?title#x3D;Collatz+Progressions+Reframed:+Exponent+Representation+Algorithmic+Hierarchies+and+Record+Computations&amp;author&#x3D;Alic+Nikola&amp;publication_year&#x3D;2026
[95]: /core/services/aop-cambridge-core/download/cited-by?doi#x3D;10.1017/fmp.2022.8&amp;productType&#x3D;JOURNAL_ARTICLE&amp;productId&#x3D;1008CC2DF91AF87F66D190C5E01C907F
[96]: https://scholar.google.com/scholar?hl=en&lr=&cites=https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F
[97]: /core/help
[98]: https://www.amazon.com/gp/help/customer/display.html/ref=kinw_myk_wl_ln?ie=UTF8&nodeId=200767340#fees
[99]: /core/search?filters%5BauthorTerms%5D=Terence Tao&eventCode=SE-AU
