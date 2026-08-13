<!-- source: https://link.springer.com/article/10.1007/s00208-023-02579-w | converted from HTML -->

A random analogue of Gilbreath’s conjecture | Mathematische Annalen | Springer Nature Link

Skip to main content

# A random analogue of Gilbreath’s conjecture

- [Open access][1]
- Published: 24 February 2023

- Volume 388, pages 2611–2625 ( 2024)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Mathematische Annalen][5] [Aims and scope][6] [Submit manuscript][7]

A random analogue of Gilbreath’s conjecture

[Download PDF][2]

## Abstract

A well-known conjecture of Gilbreath, and independently Proth from the 1800s, states that if \(a_{0,n} = p_n\) denotes the *n*th prime number and \(a_{i,n} = |a_{i-1,n}-a_{i-1,n+1}|\) for \(i, n \ge 1\), then \(a_{i,1} = 1\) for all \(i \ge 1\). It has been postulated repeatedly that the property of having \(a_{i,1} = 1\) for *i*large enough should hold for any choice of initial \((a_{0,n})_{n \ge 1}\) provided that the gaps \(a_{0,n+1}-a_{0,n}\) are not too large and are sufficiently random. We prove (a precise form of) this postulate.

### Similar content being viewed by others

### [Extending an Erdős result on a Romanov type problem][8]

Article 11 April 2022

### [On permutations of \(\{1,\ldots ,n\}\) and related topics][9]

Article 25 March 2021

### [Combinatorics on n-sets: Arithmetic Properties and Numerical Results][10]

Chapter © 2020

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Combinatorics][11]
- [Computational Number Theory][12]
- [Discrete Mathematics][13]
- [Mathematics][14]
- [Number Theory][15]
- [Probability Theory][16]
- [Probabilistic Methods in Additive Number Theory][17]

## 1 Introduction

Given any sequence of non-negative integers \((a_n)_{n \ge 1}\), we can form the sequence of non-negative integers \((|a_n-a_{n+1}|)_{n \ge 1}\). Start with the primes as the initial sequence and iterate this consecutive differencing procedure. Gilbreath’s conjecture is that the first term in every sequence, starting with the first iteration, is a 1. Precisely, if \(a_{0,n} = p_n\) for \(n \ge 1\) and \(a_{i,n} = |a_{i-1,n}-a_{i-1,n+1}|\) for \(i, n \ge 1\), then \(a_{i,1} = 1\) for all \(i \ge 1\). Below are the first few terms of the first few iterations.

[image: figure a]

Proth [[6][18]] discussed Gilbreath’s conjecture in 1878, before Gilbreath independently made the conjecture. Many sources claim Proth asserted he had a proof of the conjecture, and that his proof was wrong. However, we believe this claim is baseless. See Sect. [7][19] for more details. Odlyzko [[3][20]] verified Gilbreath’s conjecture for \(1 \le i \le \pi (10^{13}) \approx 3.34\times 10^{11}\). One is led to wonder how special the primes are in Gilbreath’s conjecture and whether any sequence beginning with 2 followed by an increasing sequence of odd numbers with small and “random” gaps between them will have first term 1 from some iteration onwards.

Odlyzko, at the end of Section 2 of [[3][20]], speculates that such a random sequence indeed will have first term 1 from some iteration onwards. Additionally, Problem 68 of [[2][21]] asks what gap or density properties of an initial sequence suffices to ensure the conclusion of Gilbreath’s conjecture. Despite Gilbreath’s conjecture being around for over a decade and several additional sources postulating that the conjecture should hold for initial sequences with small and random gaps, as of date, nothing has actually been *proven*along these lines, nor about Gilbreath’s conjecture specifically.

In this paper, we initiate a rigorous study of Gilbreath’s conjecture by proving a random analogue of it.

### Theorem 1

Let \(f: \mathbb {N}\rightarrow \mathbb {N}\) be an increasing function with \(f(M) \le \frac{1}{100}\frac{\log \log M}{\log \log \log M}\) for *M*large and \(f(M) \ge 2\) for all \(M \ge 1\). Let \(a_1,a_2,\dots \) be a random infinite sequence formed as follows. Let \(a_1 = 2, a_2 = 3\), and for \(n \ge 2\), \(a_{n+1} = a_n+2u_n\), where \(u_n\) is drawn uniformly at random from \(\{0,1,\dots ,f(n)-1\}\), independent of the other \(u_i\) ’s. Then, with probability 1, there is some \(M_0\) so that for all \(M \ge M_0\), after *M*iterations of consecutive differencing, the first term of the sequence is a 1.

Computations suggest that Gilbreath’s conjecture holds because 0s and 2s form to the right of the leading 1 early on. We prove Theorem [1][22] by showing that our random initial sequence indeed has that property almost surely. Since the first iteration is \(1, 2u_2, 2u_3, \dots \), if we ignore the leading 1 and divide by 2, what we wish to show is encapsulated by the following theorem, which is the heart of the paper.

### Theorem 2

For *M*large, for any *C*with \(2 \le C \le \frac{1}{100}\frac{\log \log M}{\log \log \log M}\), if we form an initial sequence of length *M*by choosing numbers from \(\{0,\dots ,C-1\}\) independently and uniformly at random, then, with probability at least \(1-e^{-e^{\root 20 \of {\log M}}}\), after \(e^{\root 5 \of {\log M}}\) iterations of consecutive differencing, everything is a 0 or 1.

The randomness in Theorem [2][23] is certainly necessary. For example, if the initial sequence consists of only 0s and 3s, then after any number of iterations, everything is still a 0 or 3. However, there are more exotic examples of initial sequences

[image: figure b]

for which all future iterations have only 0s and 3s (say). These exotic examples Footnote 1 suggest that we are far away from a proof of Gilbreath’s conjecture.

## 2 A general bootstrapping argument

In this section, we prove a result about random walks on regular directed graphs that will be of use to proving Theorem [2][23].

### Definition 2.1

A directed graph is *regular*if there is a positive integer *d*such that each vertex has in-degree and out-degree equal to *d*. We allow our graphs to have self-loops (but no multiple edges). For our discussion, a *simple random walk*on a regular directed graph of degree *d*is formed by choosing a starting point uniformly at random, and then walking along the directed edges, with each out-edge chosen with probability 1/*d*, independent of the previous steps.

### Proposition 2.2

Let \(G = (V,E)\) be a regular directed graph. Suppose *V*is red-blue colored such that the probability a simple random walk on *G*of length *L*consists entirely of red vertices is at least *c*. Then the probability a simple random walk on *G*of length \(\lfloor (1+\frac{1}{10}c)L\rfloor \) consists entirely of red vertices is at least \(\frac{1}{10}c^2\).

### Proof

Let \(X_1,X_2,\dots \) denote the steps of a simple random walk. Define functions \(w_1,\dots ,w_L\) on *V*by \(w_j(v):= \Pr (X_1,\dots ,X_L \text { all red} | X_j = v).\) Note (by, e.g., induction on the number of steps) the regularity assumption implies

$$\begin{aligned} w_j(v) = |V|\Pr (X_1,\dots ,X_L \text { all red}, X_j = v). \end{aligned}$$

Thus, setting

$$\begin{aligned} \rho := \Pr (X_1,\dots ,X_L \text { all red}), \end{aligned}$$

we have by assumption for any *j*that

$$\begin{aligned} \sum _v w_j(v) = \sum _v |V|\Pr (X_1,\dots ,X_L \text { all red}, X_j = v) = \rho |V|. \end{aligned}$$

Let \(K = \lceil \frac{3}{\rho } \rceil \), and let \(k_1,\dots ,k_K\) be \(k_j:= \lfloor \frac{j}{K}L\rfloor \). By Cauchy–Schwarz,

$$\begin{aligned} \left( \sum _v \sum _j w_{k_j}(v)\right) ^2&\le \left[ \sum _v 1^2\right] \cdot \left[ \sum _v \left( \sum _j w_{k_j}(v)\right) ^2\right] \\ \nonumber&= |V|\left[ \sum _j \sum _v w_{k_j}(v)^2+\sum _{j \not = j'} \sum _v w_{k_j}(v)w_{k_{j'}}(v)\right] . \end{aligned}$$

(1)

Note

$$\begin{aligned} \sum _v \sum _j w_{k_j}(v) = \sum _j \sum _v w_{k_j}(v) = K\rho |V|; \end{aligned}$$

also, since \(||w_j||_\infty \le 1\), we have

$$\begin{aligned} \sum _j \sum _v w_{k_j}(v)^2 \le \sum _j \sum _v w_{k_j}(v) = K\rho |V|. \end{aligned}$$

So ( [1][24]) implies

$$\begin{aligned} K^2\rho ^2|V|^2 \le |V|\left[ K\rho |V|+\sum _{j \not = j'} \sum _v w_{k_j}(v)w_{k_{j'}}(v)\right] , \end{aligned}$$

and thus, since \(K^2\rho ^2|V|-K\rho |V|\) is increasing in *K*for (in particular) \(K \ge 3/\rho \),

$$\begin{aligned} 6|V| \le \sum _{j \not = j'} \sum _v w_{k_j}(v)w_{k_{j'}}(v). \end{aligned}$$

By the pigeonhole principle, there are \(j \not = j'\) with

$$\begin{aligned} \sum _v w_{k_j}(v)w_{k_{j'}}(v) \ge \frac{1}{K^2}6|V|. \end{aligned}$$

Using

$$\begin{aligned} w_{k_j}(v)\le & {} \Pr (X_{k_j+1},\dots ,X_L \text { all red} | X_{k_j} = v)\\= & {} \Pr (X_{k_{j'}+1},\dots ,X_{L+k_{j'}-k_j} \text { all red} | X_{k_{j'}} = v), \end{aligned}$$

which is true merely due to translation invariance of the random walk, and the trivial

$$\begin{aligned} w_{k_{j'}}(v) \le \Pr (X_1,\dots ,X_{k_{j'}} \text { all red} | X_{k_{j'}} = v), \end{aligned}$$

we obtain

$$\begin{aligned} \frac{1}{K^2}6|V|&\le \sum _v \Pr (X_1,\dots ,X_{k_{j'}} \text { all red} | X_{k_{j'}} = v)\Pr (X_{k_{j'}+1},\dots ,X_{L+k_{j'}-k_j} | X_{k_{j'}} = v) \\ {}&= |V| \sum _v \Pr (X_1,\dots ,X_{k_{j'}} , X_{k_{j'}} = v)\Pr (X_{k_{j'}+1},\dots ,X_{L+k_{j'}-k_j} | X_{k_{j'}} = v) \\ {}&= |V|\sum _v \Pr (X_1,\dots ,X_{L+k_{j'}-k_j} , X_{k_{j'}} = v)\\ {}&= |V|\Pr (X_1,\dots ,X_{L+k_{j'}-k_j} ), \end{aligned}$$

yielding

$$\begin{aligned} \Pr (X_1,\dots ,X_{L+k_{j'}-k_j}) \ge \frac{1}{K^2}6. \end{aligned}$$

Note \(K \le \frac{3}{\rho }+1 \le \frac{4}{\rho }\), so \(\frac{1}{K^2}6 \ge \frac{6}{16}\rho ^2 \ge \frac{1}{10}c^2\). Since the proposition is trivial if \(L < 10/c\), we may assume \(L \ge 10/c\) to obtain \(k_{j'}-k_j \ge \frac{L}{K}-1 \ge \frac{\rho }{4}L-1 \ge \frac{c}{10}L\). \(\square \)

### Remark

It is natural to think that Proposition [2.2][25] can be extended, in some form, to arbitrary length increases. However, such an extension is not possible in general (note that iterating Proposition [2.2][25] results in only a summable geometric series of length increases). For example, consider \(V = \{1,\dots ,n\}, E = \{(1 \mapsto 2),\dots ,(n-1 \mapsto n),(n \mapsto 1)\}\) with the vertices \(\{1,\dots ,\frac{1}{10}n\}\) colored red and the rest blue. Then with \(L = \frac{1}{20}n\) and \(c = \frac{1}{20}\), it holds that a simple random walk on *G*of length *L*will hit only red vertices with probability at least *c*. However, of course no simple (random) walk on *G*of length \(5L = \frac{1}{2}n\) will hit only red vertices.

Examples of such “bad” colorings also exist on the graph we apply Proposition [2.2][25] to, namely a Debrujin graph. We don’t think these colorings are actually the ones we need to address in our proof of Theorem [2][23], but we couldn’t prove that.

## 3 A lower bound for ending with 0

We begin by exploiting the main property of the “dynamical system” of taking consecutive differences: the supremum never increases. In fact, we use that it quickly decreases provided there is no trivial obstruction to it doing so (Lemma [3.2][26]).

### Definition 3.1

We say non-negative integers \(a_1,\dots ,a_i\)*come from*\(\widetilde{a}_1,\dots ,\widetilde{a}_{i+1}\) if \(|\widetilde{a}_j-\widetilde{a}_{j+1}| = a_j\) for each \(1 \le j \le i\). Given \(a_1,\dots ,a_i\) and a subset \(E \subseteq \mathbb {Z}\), an *E*-*block*is a contiguous set of terms \(a_{j_1+1},\dots ,a_{j_1'}\) such that \(a_j \in E\) for each \(j_1+1 \le j \le j_1'\); the *length*of the block is \(j_1'-j_1\).

### Lemma 3.2

Let \(a_1,\dots ,a_i\) be non-negative integers with \(d:= \max _j a_j\). Let *L*denote the length of the longest \(\{0,d\}\) -block containing at least one *d*. If \(L \le i-1\), then, after *L*iterations of consecutive differencing, the largest number is at most \(d-1\).

### Proof

We induct on *L*. For \(L=1\), the result is clear. Assume \(L \ge 2\) and the result is true for all \(L' < L\). It is easy to see that, since *d*is the maximum, any \(\{0,d\}\) -block containing a *d*after an iteration would have had to have come from a \(\{0,d\}\) -block of greater length containing a *d*, so the longest \(\{0,d\}\) -block containing a *d*after one iteration is at most \(L-1\), say \(L'\). By induction, after \(L'\) more iterations, the largest number is at most \(d-1\). It follows that after *L*(total) iterations, the largest number is at most \(d-1\). \(\square \)

So, to prove Theorem [2][23], “all” we need to do is argue that long \(\{0,d\}\) -blocks are unlikely to exist. In this next lemma, we observe that any large \(\{0,d\}\) -block essentially must have come from a block with no 0s.

### Lemma 3.3

Suppose that after *i*iterations, there is a \(d\mathbb {Z}\) -block of length *L*. Then either there was a \(d\mathbb {Z}\) -block of length \(L+i\) in the initial sequence, or there is some \(i'\), \(0 \le i' \le i-1\), such that after \(i'\) iterations, there is a block of length \(L+i-i'\) with no 0s.

### Proof

We prove by induction on *i*the statement for all *L*. For \(i=0\), the result is tautological. Take \(i \ge 1\), and suppose the result holds for \(i-1\). The \(d\mathbb {Z}\) -block of length *L*had to come from either a \(d\mathbb {Z}\) -block of length \(L+1\) or a block of length \(L+1\) with no 0s (since everything will have the same residue modulo *d*), so we are done by the induction hypothesis. \(\square \)

Another nice property of the consecutive differencing operation is that it “commutes” with reducing mod 2. This allows for a decently explicit formula for the parity of a term after a given number of iterations, merely in terms of the parities of the initial terms.

### Definition 3.4

For non-negative integers \(a_1,a_2\), define \(f_1(a_1,a_2) = |a_1-a_2|\), and for any \(i \ge 2\) and non-negative \(a_1,\dots ,a_{i+1}\), define \(f_i(a_1,\dots ,a_{i+1}) = |f_{i-1}(a_1,\dots ,a_i)-f_{i-1}(a_2,\dots ,a_{i+1})|\). We say \(a_1,\dots ,a_{i+1}\)*ultimately iterate*to \(f_i(a_1,\dots ,a_{i+1})\).

### Lemma 3.5

For any \(i \ge 1\), there is a subset \(J_i \subseteq [i+1]\) containing 1 and \(i+1\) so that for any non-negative integers \(a_1,\dots ,a_{i+1}\), \(f_i(a_1,\dots ,a_{i+1}) \equiv \sum _{j \in J_i} a_j \text { mod } 2\).

### Proof

We induct on *i*. For \(i=1\), the result follows from \(|a_1-a_2| \equiv a_1+a_2 \text { mod } 2\). Assume \(i \ge 2\) and the result is true for \(i-1\). Note that \(f_i(a_1,\dots ,a_{i+1}) \equiv |f_{i-1}(a_1,\dots ,a_i)-f_{i-1}(a_2,\dots ,a_{i+1})| \equiv f_{i-1}(a_1,\dots ,a_i)+f_{i-1}(a_2,\dots ,a_{i+1}) \equiv \)

\(\sum _{j \in J_{i-1}} a_j+\sum _{j \in J_{i-1}} a_{j+1} \equiv \sum _{j \in J_{i-1} \triangle (J_{i-1}+1)} a_j \text { mod } 2\). By induction, \(J_{i-1}\) contains 1 and *i*, and so \(J_i:= J_{i-1} \triangle (J_{i-1}+1)\) contains 1 and \(i+1\), as desired. \(\square \)

We take a moment to note a useful immediate corollary of Lemma [3.5][27] which tells us that the parity of what \(a_1,\dots ,a_{i+1}\) ultimately iterate to depends linearly on each of the parities of \(a_1\) and \(a_{i+1}\).

### Corollary 3.6

Let \(a_1,\dots ,a_{i+1}\) be drawn independently, uniformly at random from \(\{0,\dots ,C-1\}\). Then, the probability \(a_1,\dots ,a_{i+1}\) ultimately iterate to an even integer is between \(\frac{1}{3}\) and \(\frac{2}{3}\). Furthermore, for any applicable *j*, *T*, the probability that all of \(f_j(a_t,\dots ,a_{t+j})\) are even for *T*consecutive values of *t*is exponentially small in *T*.

Let \([C]_0 = \{0,\dots ,C-1\}\).

The following proposition shows that 0s are never too rare, which will be useful in conjunction with Lemma [3.3][28]. Before the proof, we introduce some notation for a given *C*and *i*. Define \(i_0 = i\) and \(i_{j+1} = \lfloor \frac{i_j}{1000C} \rfloor \) for \(0 \le j \le C-3\). For \(1 \le j \le C-2\), let \(E_j\) denote the event that after \(i-i_{j-1}\) iterations there’s a \(\{0,C-j\}\) -block of length (at least) \(i_{j-1}-i_j\). For example, \(E_1\) is the event that after 0 iterations, there’s a \(\{0,C-1\}\) -block of length \(i-i_1\), and \(E_2\) is the event that after \(i-i_1\) iterations, there’s a \(\{0,C-2\}\) -block of length \(i_1-i_2\).

### Proposition 3.7

For any \(C \ge 2\) and any \(i \ge (2000C)^{2C}\), if \(a_1,\dots ,a_i\) are chosen independently and uniformly at random from \(\{0,\dots ,C-1\}\), then the probability they ultimately iterate to 0 is at least \(\frac{1}{4000C^2}\).

### Proof

Fix \(C \ge 2\) and \(i \ge (2000C)^{2C}\). If \(C=2\), then Corollary [3.6][29] gives the result, so assume \(C \ge 3\). We may suppose that the desired probability is at most 0.01. Let \(\mathcal {B}_0\) denote all *i*-tuples in \([C]_0^i\) that ultimately iterate to something 0 mod 2; we say “conditional probability” when speaking of the conditional probability that \(\mathcal {B}_0\) induces. Then, by Corollary [3.6][29], the conditional probability of ultimately iterating to 0 is at most 0.03, and so the conditional probability of not having only 0s and 1s after some iteration is at least 0.97.

Therefore, with notation as defined above Proposition [3.7][30], with conditional probability at least 0.97 some \(E_j\) occurs. Indeed, otherwise, repeated use of Lemma [3.2][26] shows that after \(i-i_{C-2}\) iterations, everything is a 0 or 1: after \(i-i_1\) iterations, there are no more \((C-1)\) s and thus no \((C-1)\) s ever again; after \(i-i_2\) iterations, there are no more \((C-2)\) s and thus no \((C-2)\) s ever again, etc..

Consequently, by the pigeonhole principle, there is some *j*, \(1 \le j \le C-2\), such that \(E_j\) occurs with conditional probability at least \(\frac{0.97}{C-2}\). Clearly *j*cannot be 1, since we have the uniform distribution after 0 iterations. Also, *j*must be such that \(C-j\) is odd, since by Corollary [3.6][29], the probability of having \(i_{j-1}-i_j\) evens in a row is at most \((\frac{2}{3})^{i_{j-1}-i_j}\), which is at most \((\frac{2}{3})^{2(2000C)^C}\) since, as are easy to verify, \(i_{j-1}-i_j \ge 2i_j\) and that \(i \ge (2000C)^{2C}\) implies \(i_j \ge i_{C-2} \ge (2000C)^C\) for each *j*. Since after \(i-i_{j-1}\) iterations, there are only \(i_{j-1}\) indices, a block of length \(i_{j-1}-i_j\) must contain the block \([i_j+1,i_{j-1}-i_j]\) (see Fig. [1][31]). So, with conditional probability at least \(\frac{0.97}{C-2}\), all indices \(i_j+\Delta \), for \(1 \le \Delta \le i_{j-1}-2i_j\), will be 0 or \(C-j\).

With \(a_1,\dots ,a_i\) denoting the initial sequence, note that after \(i-i_{j-1}\) iterations, none of the indices \(i_j+\Delta \), \(1 \le \Delta \le i_{j-1}-2i_j\), depend on \(a_1\) or \(a_i\) (only the first and last indices do). Therefore, by Corollary [3.6][29], we see that with (unconditional) probability at least \(\frac{1}{3}\frac{0.97}{C-2} \ge \frac{0.30}{C-2}\), all \(i_j+\Delta \) will be 0 or \(C-j\). Note that after \(\overline{i}:= i-i_{j-1}\) iterations, the integer at any index *r*is equal to \(f_{\overline{i}}(a_r, a_{r+1},\dots ,a_{r+\overline{i}})\).

**Fig. 1**

[image: Fig. 1]

[Full size image][32]

Indicates which initial indices (in [*i*]) a particular index after \(\overline{i}\) iterations depends on

Define a (regular) directed graph on \([C]_0^{\overline{i}+1}\) by \((x_1,\dots ,x_{\overline{i}+1}) \rightarrow (x_2,\dots ,x_{\overline{i}+1},y)\) for any \(x_1,\dots ,x_{\overline{i}+1},y \in [C]_0\). Color a tuple \((x_1,\dots ,x_{\overline{i}+1}) \in [C]_0^{\overline{i}+1}\) “red” if and only if it ultimately iterates to 0 or \(C-j\). The fact that, with probability at least \(\frac{0.30}{C-2}\), all \(f_{\overline{i}}(a_r, a_{r+1},\dots ,a_{r+\overline{i}})\), for \(i_j+1 \le r \le i_{j-1}-i_j\), are 0 or \(C-j\) corresponds exactly to: with probability at least \(\frac{0.30}{C-2}\), a simple random walk in \([C]_0^{\overline{i}+1}\) of length \(L:= i_{j-1}-2i_j\) consists entirely of red vertices.

Proposition [2.2][25] now tells us that with probability at least \(\frac{1}{200C^2}\), a simple random walk of length Footnote 2 \((1+\frac{1}{200C})L\) consists entirely of red vertices. Note \((1+\frac{1}{200C})L \ge (1+\frac{1}{400C})i_{j-1}\), since it is equivalent to \(\frac{1}{400C}i_{j-1} \ge (2+\frac{1}{200C})i_j\), which is true since \(i_j \le \frac{i_{j-1}}{1000C}\). We have thus shown that, if \(a_1,\dots ,a_{(1+\frac{1}{400C})i_{j-1}+\overline{i}}\) are chosen independently and uniformly at random from \([C]_0\), then with probability at least \(\frac{1}{200C^2}\), all \(f_{\overline{i}}(a_r,\dots ,a_{r+\overline{i}})\) for \(1 \le r \le (1+\frac{1}{400C})i_{j-1}\) are either 0 or \(C-j\).

We are nearly done, as, for \(L':= i_{j-1}\), we have that \((f_{\overline{i}}(a_r,\dots ,a_{r+\overline{i}}))_{1 \le r \le L'}\) is the whole sequence after \(\overline{i}\) iterations; since a \(\{0,C-j\}\) -block ultimately iterates to either 0 or \(C-j\) and since \(C-j\) is odd, we just need to additionally ensure that the ultimate iterate is even.

We now deduce that, if \(a_1,\dots ,a_i\) are chosen independently and uniformly at random from \([C]_0\), then with probability at least \(\frac{1}{4000C^2}\), they ultimately iterate to something 0 mod 2 and each \(f_{\overline{i}}(a_r,\dots ,a_{r+\overline{i}})\), for \(1 \le r \le L'\), is either 0 or \(C-j\). Let \(\delta = \frac{1}{400C^2}\). By Corollary [3.6][29], the proportion of walks \((X_1,\dots ,X_{(1+\delta )L'})\) in \([C]_0^{\overline{i}}\) of length \((1+\delta )L'\) that have at most \(\frac{\delta L'}{8}\) values of \(j \in [\delta L']\) with Footnote 3 \((X_{j+1},X_{j+2},\dots ,X_{j+L'}) \in \mathcal {B}_0\) is at most Footnote 4 \(\frac{\delta L'}{8}{\delta L' \atopwithdelims ()\delta L'/8}(2/3)^{\delta L'} \le \frac{1}{400C^2}\). Therefore, since the proportion of walks \((X_1,\dots ,X_{(1+\delta )L'})\) with \(X_1,\dots ,X_{(1+\delta )L'}\) all red is at least \(\frac{1}{200C^2}\), if we let \(\mathcal {A}\) denote the walks \((X_1,\dots ,X_{(1+\delta )L'})\) such that \(X_1,\dots ,X_{(1+\delta )L'}\) are all red and such that there are at least \(\frac{\delta L'}{8}\) values of *j*with \((X_{j+1},X_{j+2},\dots ,X_{j+L'}) \in \mathcal {B}_0\), then the density of \(\mathcal {A}\) is at least \(\frac{1}{400C^2}\). So on one hand,

$$\begin{aligned} \sum _{(X_1,\dots ,X_{(1+\delta )L'}) \in \mathcal {A}} \sum _{j=1}^{\delta L'} 1_{(X_{j+1},\dots ,X_{j+L'}) \in \mathcal {B}_0} \ge \frac{\delta L'}{8}\frac{1}{400C^2}C^{\overline{i}}C^{(1+\delta )L'-1}, \end{aligned}$$

while on another hand,

$$\begin{aligned}&\sum _{(X_1,\dots ,X_{(1+\delta )L'}) \in \mathcal {A}} \sum _{j=1}^{\delta L'} 1_{(X_{j+1},\dots ,X_{j+L'}) \in \mathcal {B}_0}\\&\quad = \sum _{j=1}^{\delta L'}\sum _{(X_{j+1},\dots ,X_{j+L'}) \in \mathcal {B}_0} \sum _{\begin{array}{c} X_1,\dots ,X_j,X_{j+L'+1},\dots ,X_{(1+\delta )L'} \\ (X_1,\dots ,X_{(1+\delta )L'}) \in \mathcal {A} \end{array}} 1 \\&\quad \le \sum _{j=1}^{\delta L'}\sum _{(X_{j+1},\dots ,X_{j+L'}) \in \mathcal {B}_0} C^{\delta L'} 1_{X_{j+1},\dots ,X_{j+L'} \text { all red}} \\&\quad = \delta L' C^{\delta L'} \sum _{(X_1,\dots ,X_{L'}) \in \mathcal {B}_0} 1_{X_1,\dots ,X_{L'} \text { all red}}. \end{aligned}$$

We deduce that

$$\begin{aligned} \sum _{(X_1,\dots ,X_{L'}) \in \mathcal {B}_0} 1_{X_l,\dots , X_{L'} \text { all red}} \ge \frac{1}{3200C^2}C^{\overline{i}}C^{L'-1}, \end{aligned}$$

which is what we wanted to deduce. \(\square \)

### Corollary 3.8

For any \(C \ge 2\) and any \(i \ge 1\), if \(a_1,\dots ,a_i\) are chosen independently and uniformly at random from \(\{0,\dots ,C-1\}\), then the probability they ultimately iterate to 0 is at least \((\frac{1}{C})^{(2000C)^{2C}}\).

### Proof

For \(i \ge (2000C)^{2C}\), Proposition [3.7][30] yields a lower bound of \(\frac{1}{4000C^2}\), and for \(1 \le i < (2000C)^{2C}\), we use the trivial lower bound coming from \(a_j = 0\) for all *j*. \(\square \)

## 4 Finishing the proof of Theorem [2][33]

We now finish the proof of Theorem [2][33], copied below for the reader’s convenience.

### Theorem 2

For *M*large, for any *C*with \(2 \le C \le \frac{1}{100}\frac{\log \log M}{\log \log \log M}\), if we form an initial sequence of length *M*by choosing numbers from \(\{0,\dots ,C-1\}\) independently and uniformly at random, then, with probability at least \(1-e^{-e^{\root 20 \of {\log M}}}\), after \(e^{\root 5 \of {\log M}}\) iterations of consecutive differencing, everything is a 0 or 1.

Fix *M*large and *C*in the range \([3,\frac{1}{100}\frac{\log \log M}{\log \log \log M}]\) (the case \(C=2\) is trivial). Let \(E_1\) denote Footnote 5 the event that after 0 iterations, there is a \(\{0,C-1\}\) -block of length \(R:= e^{\root 10 \of {\log M}}\). Let \(E_2\) be the event that after 2*R*iterations, there is a \(\{0,C-2\}\) -block of length \(R^2\). Let \(E_3\) be the event that after \(2R^2\) iterations, there is a \(\{0,C-3\}\) -block of length \(R^3\). In general, for \(2 \le j \le C-2\), \(E_j\) is the event that after \(2R^{j-1}\) iterations, there is a \(\{0,C-j\}\) -block of length \(R^j\). Since \(2R^{j-1} \ge 2R^{j-2}+R^{j-1}\) for \(3 \le j \le C-1\), we see that, as before, by Lemma [3.2][26], if no \(E_j\) occurs, then after \(2R^{C-2}\) iterations, everything is a 0 or a 1. Note that \(2R^{C-2} \le e^{\root 5 \of {\log M}}\), so it suffices to show that the probability that some \(E_j\) occurs is at most \(e^{-e^{\root 20 \of {\log M}}}\). By the union bound, it suffices to show \(\Pr (E_j) \le e^{-e^{\root 13 \of {\log M}}}\), say, for each \(1 \le j \le C-2\).

Clearly, \(\Pr (E_1) \le M(\frac{2}{3})^R \le e^{-e^{\root 13 \of {\log M}}}\), so fix some *j*with \(2 \le j \le C-2\). By Lemma [3.3][28], if \(E_j\) occurs, either there is a \((C-j)\mathbb {Z}\) -block of length \(R^j\) in the initial sequence or there is a block of length \(R^j\) in the first \(2R^{j-1}-1\) iterations containing no 0s. Once again, the first option holds with probability at most \(M(\frac{2}{3})^{R^j} \le \frac{1}{2}e^{-e^{\root 13 \of {\log M}}}\), so by the union bound, it suffices to show that for each \(0 \le i \le 2R^{j-1}-1\), the probability that there is a block of length \(L:= R^j = e^{j\root 10 \of {\log M}}\) without 0s after *i*iterations is at most \(e^{-e^{\root 12 \of {\log M}}}\), say.

So fix some \(i \in [0,2R^{j-1}-1]\). Let \(b_1,\dots ,b_{M-i}\) denote the sequence after *i*iterations. Let’s first focus on the block \(b_1,\dots ,b_L\). Say the initial sequence is \(a_1,\dots ,a_M\). Note that \(b_{k(i+1)+1} = f_i(a_{k(i+1)+1},\dots ,a_{(k+1)(i+1)})\) for \(0 \le k \le \frac{1}{2}R-1\). Since \((\frac{1}{2}R-1)(i+1)+1 \le \frac{1}{2}R(i+1) \le L\) and the sets \(\{a_{k(i+1)+1},\dots ,a_{(k+1)(i+1)}\}\) are disjoint as *k*ranges, by independence the probability that \(b_1,\dots ,b_L\) are all nonzero is at most \(\left( 1-(\frac{1}{C})^{(400C^2)^{2C}}\right) ^{R/2}\) by Corollary [3.8][34]. Using the standard inequality \(1-x \le e^{-x}\), we see that \(\left( 1-(\frac{1}{C})^{(400C^2)^{2C}}\right) ^{R/2} \le \exp \left( -\frac{R}{2}(\frac{1}{C})^{(400C^2)^{2C}}\right) \le \exp \left( -\frac{R}{2}e^{-(\log C)e^{5C\log C}}\right) \le \exp \left( -\frac{R}{2}e^{-(\log \log \log M)e^{\frac{1}{19}\log \log M}}\right) \le \exp \left( -\frac{R}{2}e^{-\root 15 \of {\log M}}\right) \le \exp \left( -e^{\root 11 \of {\log M}}\right) \). Therefore, by the union bound, the probability that there is some block of length *L*after *i*iterations containing no 0s is at most \(Me^{-e^{\root 11 \of {\log M}}} \le e^{-e^{\root 12 \of {\log M}}}\). The proof is thus complete.

## 5 Proof of Theorem [1][22]

In this section we deduce Theorem [1][22] from Theorem [2][23]. We start with a lemma.

### Lemma 5.1

Take *M*large. Let \(f: [M] \rightarrow \{2,3,\dots ,\lfloor \frac{1}{100}\frac{\log \log M}{\log \log \log M}\rfloor \}\) be an increasing function. Form a random initial sequence \(b_1,\dots ,b_M\) by choosing \(b_m\) uniformly at random from \(\{0,1,\dots ,f(m)-1\}\), independently of the other \(b_i\) ’s. Then, with probability at least \(1-e^{-\frac{1}{20}\log ^2 M}\), after \(3\frac{M}{\log ^2 M}\) iterations of consecutive differencing, everything is a 0 or 1.

Before proving Lemma [5.1][35], let’s prove Theorem [1][22], copied below, assuming it.

### Theorem 1

Let \(f: \mathbb {N}\rightarrow \mathbb {N}\) be an increasing function with \(f(M) \le \frac{1}{100}\frac{\log \log M}{\log \log \log M}\) for *M*large and \(f(M) \ge 2\) for all \(M \ge 1\). Let \(a_1,a_2,\dots \) be a random infinite sequence formed as follows. Let \(a_1 = 2, a_2 = 3\), and for \(n \ge 2\), \(a_{n+1} = a_n+2u_n\), where \(u_n\) is drawn uniformly at random from \(\{0,1,\dots ,f(n)-1\}\), independent of the other \(u_i\) ’s. Then, with probability 1, there is some \(M_0\) so that for all \(M \ge M_0\), after *M*iterations of consecutive differencing, the first term of the sequence is a 1.

### Proof of Theorem 1

Let \(A_M\) denote the event that after *M*iterations, the first term is not a 1. We wish to show that, with probability 1, only finitely many \(A_M\) ’s occur. By Borel–Cantelli, it suffices to show that for all *M*large, the probability of \(A_M\) occurring is at most \(e^{-\frac{1}{30}\log ^2 M}\). Note that \(A_M\) is equivalent to \(a_1,\dots ,a_{M+1}\) not ultimately iterating to 1. For *M*large enough, by Lemma [5.1][35], with probability at least \(1-e^{-\frac{1}{20}\log ^2 M}\), after \(3\frac{M}{\log ^2 M}\) iterations of consecutive differencing beginning with initial sequence \(u_2,\dots ,u_M\), everything is a 0 or 1. Therefore, with probability at least \(1-e^{-\frac{1}{20}\log ^2 M}\), after \(3\frac{M}{\log ^2 M}\) iterations of consecutive differencing beginning with initial sequence \(2u_2,\dots ,2u_M\), everything is a 0 or 2. It follows that with probability at least \(1-e^{-\frac{1}{20}\log ^2 M}\), after \(1+3\frac{M}{\log ^2 M}\) iterations of consecutive differencing beginning with initial sequence \(a_1,\dots ,a_{M+1}\), the obtained sequence starts off with an odd number at most \(\frac{1}{100}\frac{\log \log M}{\log \log \log M}\) followed by only 0s and 2s. Since this odd number, whenever at least 3, decreases by 2 at each iteration in which the second (and adjacent) term of the sequence is 2, we wish to show that there are many 2s amongst the (only) 0s and 2s that follow; indeed, then the first term will become a 1 and consequently stay a 1 throughout the remaining iterations, since everything that follows is either a 0 or a 2.

By Corollary [3.6][29], with probability at least \(1-e^{-\frac{1}{10}\log ^2M}\), the second term of the sequence is congruent to \(2 \text { mod } 4\) at least \(\frac{1}{3}\log ^2 M\) times out of the \(\log ^2 M\) iterations following the \((1+3\frac{M}{\log ^2\,M}){\text {th}}\) iteration. Therefore, with probability at least \(1-e^{-\frac{1}{20}\log ^2\,M}-e^{-\frac{1}{10}\log ^2\,M} \ge 1-e^{-\frac{1}{30}\log ^2\,M}\), starting with \(a_1,\dots ,a_{M+1}\), after \(1+3\frac{M}{\log ^2 M}+\log ^2 M\) iterations, the first term will be a 1, and therefore will remain a 1 all the way until the final (i.e., \(M{\text {th}}\)) iteration, since everything else is a 0 or 2. \(\square \)

We finish by proving Lemma [5.1][35]. We begin with a definition.

### Definition 5.2

Let \(a_1,\dots ,a_{M+1}\) be non-negative integers. We say that an index \(i \in [M+1]\)*influenced*the index \(j \in [M+1-t]\) after *t*iterations if \(0 \le i-j \le t\). Recall that \(f_t(a_j,\dots ,a_{j+t})\) is the value at index *j*after *t*iterations.

The idea of the proof of Lemma [5.1][35] is as follows. By Theorem [2][23], the blocks on which *f*is constant will become all 0s and 1s after not too many iterations. Although there are some indices that were influenced by initial indices on which *f*took different values, these indices are contained in not too many not too large intervals (since *f*is increasing), so we can let all the 0s and 1s drop the values at these “bad indices” with a few extra iterations.

We start by proving a lemma that allows us to isolate these “bad indices”. For an interval \(I \subseteq \mathbb {N}\), let *L*(*I*) and *R*(*I*) denote its left and right endpoints, respectively.

### Lemma 5.3

Suppose *M*is large, and let \(C_M\) be a positive integer with \(C_M \le \log \log M\). Let \(I_1,\dots ,I_r \subseteq [M]\) be disjoint intervals with \(r \le C_M\) and \(|I_t| \le C_Me^{\root 5 \of {\log M}}\) for each *t*. Then there are pairwise disjoint intervals \(J_1,\dots ,J_s \subseteq [M]\), each containing some \(I_t\), such that the following two hold.

-

For all *t*, \(1 \le t \le r\), there is some *m*with \(I_t \subseteq J_m\).

-

For any *m*, \(1 \le m \le s\), if we let \(B_m\) denote the smallest interval containing all of the \(I_t\) ’s in \(J_m\), then we have that either \(L(B_m)-L(J_m) \ge (\log ^2\,M)^{C_M}|B_m|\) or \(R(J_m)-R(B_m) \ge (\log ^2\,M)^{C_M}|B_m|\), with both being true if \(J_m\) contains neither 1 nor *M*.

### Proof

For a subset *A*of [*r*], let \(B_A\) denote the smallest interval containing \(\cup _{t \in A} I_t\), and let *J*(*A*) denote the smallest interval containing \(\cup _{t \in A} I_t\) such that either \(L(B_A)-L(J(A)) \ge (\log ^2\,M)^{C_M}|B_A|\) or \(R(J(A))-R(B_A) \ge (\log ^2\,M)^{C_M}|B_A|\), with both required to be true if *J*(*A*) contains neither 1 nor *M*; if no such interval exists, we let \(J(A) = \emptyset \). We construct a finite sequence of sets \(\mathcal {C}_0,\mathcal {C}_1,\dots \) in an iterative manner as follows. Let \(\mathcal {C}_0 = \{J(\{t\}): 1 \le t \le r\}\). Assume we have defined \(\mathcal {C}_j\) for \(0 \le j \le i\). If \(\mathcal {C}_i\) contains distinct intervals \(J(A_1),J(A_2)\) that intersect, we define Footnote 6 \(\mathcal {C}_{i+1}\) to be the same as \(\mathcal {C}_i\), except we replace \(J(A_1)\) and \(J(A_2)\) with \(J(A_1\cup A_2)\); otherwise, we terminate the construction (of the \(\mathcal {C}_j\) ’s). It is clear that the construction will terminate after at most *r*steps, say after *k*steps. Let \(\mathcal {C}_0,\dots ,\mathcal {C}_{k-1}\) be the constructed collections. It is clear that if each element of \(\mathcal {C}_{k-1}\) is non-empty, then the elements of \(\mathcal {C}_{k-1}\) satisfy the conditions of Lemma [5.3][36]. The largest diameter of an interval in \(\mathcal {C}_0\) is at most \((2(\log ^2\,M)^{C_M}+1)C_Me^{\root 5 \of {\log M}} \le 3(\log ^2\,M)^{C_M}C_Me^{\root 5 \of {\log M}}\). If \(J(A_1)\) and \(J(A_2)\) each have diameter at most *D*and intersect, then the diameter of \(J(A_1\cup A_2)\) is at most \((2(\log ^2\,M)^{C_M}+1)(2D) \le 6(\log ^2\,M)^{C_M}D\). Therefore, each interval in any \(\mathcal {C}_{i-1}\) has diameter at most \(6^{i-1}(\log ^2\,M)^{(i-1)C_M}3(\log ^2\,M)^{C_M}C_Me^{\root 5 \of {\log M}} \le 6^r(\log ^2\,M)^{rC_M} C_Me^{\root 5 \of {\log M}} \le e^{\root 4 \of {\log M}}\). To finish the proof, it just remains to note that \(J(A) \not = \emptyset \) if the diameter of \(\cup _{t \in A} I_t\) is at most \(e^{\root 4 \of {\log M}}\). \(\square \)

### Proof of Lemma 5.1

Do \(e^{\root 5 \of {\log M}}\) iterations of consecutive differencing. For \(2 \le C \le \frac{1}{100}\frac{\log \log M}{\log \log \log M} =: C_M\), we say that an index *j*is *C*-*pure*if *f*took the value *C*at all indices in the initial sequence that influenced *j*(after \(e^{\root 5 \of {\log M}}\) iterations). Let *I*denote the indices that are not *C*-pure for any *C*. Write \(I = \sqcup _{t=1}^r I_t\) as a disjoint union of intervals with *r*minimal. Clearly \(r \le C_M\). Also, crudely, \(|I_t| \le C_Me^{\root 5 \of {\log M}}\) for each *t*; indeed, since *f*is increasing and is always between 2 and \(C_M\), there are at most \(C_M\) indices at which *f*strictly increased, and after \(e^{\root 5 \of {\log M}}\) iterations, there are thus at most \(C_M e^{\root 5 \of {\log M}}\) indices which were influenced by two indices at which *f*took different values.

Let \(J_1,\dots ,J_s\) be the intervals guaranteed Footnote 7 by Lemma [5.3][36], and let \(B_1,\dots ,B_s\) be as in Lemma [5.3][36]. For any *C*, by Footnote 8 Theorem [2][23] applied to the (interval of) *C*-pure indices, the probability that all *C*-pure indices are 0 or 1 is at least \(1-e^{-e^{\root 20 \of {\log M}}}\), and therefore the probability that all indices that are *C*-pure for some *C*are 0 or 1 is at least \(1-C_Me^{-e^{\root 20 \of {\log M}}} \ge 1-e^{-\root 21 \of {\log M}}\). In particular, with probability at least \(1-e^{-\root 21 \of {\log M}}\), all indices in \(\cup _{m=1}^s (J_m{\setminus } B_m)\) are 0 or 1; going forward, we condition on this being the case. For \(1 \le m \le s\) and \(1 \le j \le C_M-1\), let \(J_m^j\) denote the interval (of length \(|J_m|-2(\log ^2\,M)^j |B_m|\)) whose indices after \(2(\log ^2\,M)^j |B_m|\) iterations past the \(e^{\root 5 \of {\log M}}\) th are influenced by indices only in \(J_m\), and let \(B_m^j\) denote the interval (of length \(|B_m|+2(\log ^2\,M)^j |B_m|\)) whose indices after \(2(\log ^2\,M)^j |B_m|\) iterations past the \(e^{\root 5 \of {\log M}}\) th are influenced by at least one index in \(B_m\). Note that Lemma [5.3][36] implies \(B_m^j \subseteq J_m^j\) for each \(1 \le j \le C_M-1\) (since \(2(\log ^2 M)^{C_M-1}|B_m| \le (\log ^2 M)^{C_M}|B_m|\)).

For \(1 \le m \le s\), let \(E_m^0\) denote the event that there is a \(\{0,C_M\}\) -block in \(J_m\) of length \((\log ^2 M)|B_m|\) containing a \(C_M\). For \(1 \le m \le s\) and \(1 \le j \le C_M-2\), let \(E_m^j\) denote the event that, after \(2(\log ^2 M)^j |B_m|\) iterations (past the \(e^{\root 5 \of {\log M}}\) th), there is a \(\{0,C_M-j\}\) -block in \(J_m^j\) of length \((\log ^2M)^{j+1}|B_m|\) containing a \(C_M-j\). Fix *m*with \(1 \le m \le s\). As in the proofs of Proposition [3.7][30] and Theorem [2][23], since \(2(\log ^2\,M)^{i+1} |B_m| \ge (\log ^2\,M)^{i+1}|B_m|+2(\log ^2\,M)^i|B_m|\), if none of \(E_m^0, E_m^1,\dots ,E_m^{C_M-2}\) occur, then after \(2(\log ^2\,M)^{C_M-1}\) iterations, the largest number in \(J_m^{C_M-1}\) is a 1.

We claim first that the probability \(E_m^0\) occurs is at most \(2(\frac{1}{2})^{\frac{1}{2}\log ^2 M}\). Indeed, if \(J_m\) contains a \(\{0,C_M\}\) -block of length \((\log ^2 M)|B_m|\), then at least \((\log ^2M -1)|B_m|\) of that \(\{0,C_M\}\) -block must lie outside of \(B_m\), and thus in \(J_m\setminus B_m\), where everything is 0 or 1. Therefore, either to the left or to the right of \(B_m\) must be at least \(\frac{1}{2}\log ^2M|B_m|\) consecutive 0’s, so our claim follows from Corollary [3.6][29].

Similarly, the length of the longest \(\{0,C_M-j\}\) -block in \(J_m^j\) is at most the whole of \(B_m^j\) and 0s surrounding it, so the probability \(E_m^j\) occurs is at most \(2(\frac{1}{2})^{\frac{1}{4}\log ^2 M}\). Therefore, the probability that at least one of \(E_m^0,\dots ,E_m^{C_M-2}\) occurs is at most \(2(\frac{1}{2})^{\frac{1}{2}\log ^2\,M}+(C_M-2)2(\frac{1}{2})^{\frac{1}{4}\log ^2\,M} \le e^{-\frac{1}{10}\log ^2\,M}\). Since \(B_m^{C_M-1} \subseteq J_m^{C_M-1}\), if none of \(E_m^0,\dots ,E_m^{C_m-2}\) occur, then the elements of (the growing) \(B_m\) became 0 and 1 quickly enough to not affect anything outside of (the shrinking) \(J_m\). In particular, if for each *m*, none of \(E_m^0,\dots ,E_m^{C_M-2}\) occur, then Footnote 9 after \(2(\log ^2\,M)^{C_M-1}\max _{1 \le m \le s} |B_m| \le 2\frac{M}{\log ^2\,M}\) iterations past the \(e^{\root 5 \of {\log M}}\) th, everything is a 0 or 1. Since the probability at least one \(E_m^j\) (over all *j*, *m*) occurs is at most \(se^{-\frac{1}{10}\log ^2\,M} \le e^{-\frac{1}{20}\log ^2\,M}\), Lemma [5.1][35] is established. \(\square \)

## 6 Additional mathematical remarks

The proof of Theorem [2][23] can be relatively easily adapted to handle any distribution (not just the uniform distribution) on \(\{0,\dots ,C-1\}\) that gives not too large, positive weight to each of \(0,\dots ,C-1\) (one should create duplicate vertices in \([C]_0^i\) so that the obtained simple random walk models this different probability distribution).

In Theorem [2][23] we did not try to optimize \(e^{-e^{\root 20 \of {\log M}}}\) nor \(e^{\root 5 \of {\log M}}\). A proof allowing *C*to go all the way up to \(\log ^2 M\), or even a power of *M*, would be interesting. We expect that, in reality, the highest *C*can go is *M*, in that if \(C = o(M)\), then with probability \(1-o(1)\), after \(\frac{M}{2}\) iterations, everything is a 0 or 1, while if \(C = \omega (M)\), with probability *o*(1), after \(\frac{M}{2}\) iterations, everything is a 0 or 1.

## 7 A historical remark

Various sources (websites, blog posts, etc.) have claimed that Proth believed he had proven Gilbreath’s conjecture, and that his proof turned out to be wrong.

Not only do we currently have no evidence for this claim, the apparent source of this claim has retracted it.

The claim seemed plausible, for Proth did publish a paper [[6][18]] on (what later became known as) Gilbreath’s conjecture and did, admittedly confusingly, call it a “theorem”. However, a reading through the paper shows he did not seriously claim a proof. Indeed, Hugh Williams who made the claim about Proth without reference [[7][37], p. 123], said “On rereading his actual paper...I can find no support for my assertion.... My apologies for seeming to have started a myth” [[8][38]].

We also take this time to correct another historical error, which actually is composed of two suberrors. The first suberror is that many sources incorrectly cited [[5][39]] when referring to Proth’s discussion of Gilbreath’s conjecture, referring to the correct title “Théorèmes sur les nombres premiers” but citing Comp. Rend. Acad. Sci. Paris, 85 (1877) instead of Comp. Rend. Acad. Sci. Paris, 87 (1877). The former actually corresponds to a completely unrelated paper of Pepin [[4][40]]. The second suberror is that, the intended reference, [[5][39]], didn’t even discuss Gilbreath’s conjecture! We were only able to find Proth discussing Gilbreath’s conjecture in [[6][18]].

We refer the reader to [[1][41]] for more information surrounding all of this.

## Notes

1.

To clarify, in the setting in which the primes are the initial sequence, the analogous situation to having only 0s and 3s is having only 0s and 6s past the first index, making the first index very likely to repeatedly change from 1 to 5 (see Lemma [3.5][27]), thereby violating Gilbreath’s conjecture.

2.

To be light on notation, we suppress ceiling and floor functions in the rest of this section.

3.

Here we have abused notation, by associating the *i*-tuple that \(X_{j+1},\dots ,X_{j+L'}\) form with \((X_{j+1},\dots ,X_{j+L'})\).

4.

The (very crude) inequality following this footnote follows from the well known \({n \atopwithdelims ()k} \le (\frac{en}{k})^k\), giving \(\frac{\delta L'}{8}{\delta L' \atopwithdelims ()\delta L'/8}(2/3)^{\delta L'} \le \frac{\delta L'}{8}(\frac{e\delta L'}{\delta L'/8})^{\delta L'/8}(2/3)^{\delta L'} < \frac{\delta L'}{8}(0.98)^{\delta L'}\). Note \(\delta L' \ge \frac{1}{80C^2}(400C^2)^C\).

5.

To be light on notation, we suppress ceiling and floor functions in this section.

6.

It does not matter, but \(\mathcal {C}_{i+1}\) thus could depend on the choice of intersecting intervals.

7.

We are applying Lemma [5.3][36] with \(M-e^{\root 5 \of {\log M}}\) instead of *M*, but all bounds are essentially the same.

8.

As stated, Theorem [2][23] only applies to initial sequences of length *M*. However, given any shorter initial sequence, we can independently add elements uniformly chosen from \(\{0,\dots ,C-1\}\) to obtain a sequence of length *M*, then do \(e^{\root 5 \of {\log M}}\) iterations, and then truncate the sequence to keep only indices influenced by the original initial sequence.

9.

It is clear from Lemma [5.3][36] that \(|B_m| \le \frac{M}{(\log ^2\,M)^{C_M}}\) for each *m*.

## References

1.

Arias-de-Reyna, J.: Gilbreath’s conjecture, blog post. [https://institucional.us.es/blogimus/en/2020/07/gilbreaths-conjecture/][42]

2.

Montgomery, H.L.: Ten lectures on the interface between analytic number theory and harmonic analysis, CBMS No. 84. Amer. Math. Soc., Providence (1994)

3.

Odlyzko, A.M.: Iterated absolute values of differences of consecutive primes. Math. Comput. **61**, 373–380 (1993)

[Article][43] [MathSciNet][44] [ADS][45] [Google Scholar][46]

4.

Pepin, F.: Sur la formule \(2^{2^n}+1\). Comp. Rend. Acad. Sci. Paris **85**, 329–331 (1877)

[Google Scholar][47]

5.

Proth, F.: Théorèmes sur les nombres premiers. Comp. Rend. Acad. Sci. Paris **87**, 329–331 (1877)

[Google Scholar][48]

6.

Proth, F.: Sur la série des nombres premiers. Nouvelle Correspondance Mathématique **4**, 236–240 (1878)

[Google Scholar][49]

7.

Williams, H.C.: Edouard Lucas and Primality Testing. Canad. Math. Soc. Ser. Monogr. Adv. Texts. Wiley, New York (1998)

[Google Scholar][50]

8.

Williams, H.C.: Email correspondence (2020)

[Download references][51]

## Acknowledgements

I would like to thank an anonymous referee for several helpful comments improving the presentation of the paper and pointing out a quick improvement to Proposition [2.2][25]. I would also like to thank my advisor, Ben Green, for suggesting this problem to me and Daniel Korandi for helpful feedback on the introduction. Finally, thanks are due to Juan Arias de Reyna for bringing to attention the dubious nature of the claim discussed in Sect. [7][19], and Hugh Williams for kindly responding to emails and helping resolve the situation.

## Author information

### Authors and Affiliations

1.

Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory Quarter, Woodstock Road, Oxford, OX2 6GG, UK

Zachary Chase

Authors

1. Zachary Chase

[View author publications][52]

Search author on: [PubMed][53] [Google Scholar][54]

### Corresponding author

Correspondence to [Zachary Chase][55].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

The author is partially supported by Ben Green’s Simons Investigator Grant 376201 and gratefully acknowledges the support of the Simons Foundation.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][56].

[Reprints and permissions][57]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [58]

### Cite this article

Chase, Z. A random analogue of Gilbreath’s conjecture. *Math. Ann.***388**, 2611–2625 (2024). https://doi.org/10.1007/s00208-023-02579-w

[Download citation][59]

-

Received: 11 January 2022

-

Accepted: 25 January 2023

-

Published: 24 February 2023

-

Version of record: 24 February 2023

-

Issue date: March 2024

-

DOI: https://doi.org/10.1007/s00208-023-02579-w

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s00208-023-02579-w.pdf
[3]: /article/10.1007/s00208-023-02579-w/save-research?_csrf=opxAhppU2NGlcD_2ec3b5-rKNXPxhf6Z
[4]: /saved-research
[5]: /journal/208
[6]: /journal/208/aims-and-scope
[7]: https://www.editorialmanager.com/maan
[8]: https://link.springer.com/10.1007/s00013-022-01737-x?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s10801-021-01028-8?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/978-3-030-39081-5_34?fromPaywallRec=false
[11]: /subjects/combinatorics
[12]: /subjects/computational-number-theory
[13]: /subjects/discrete-mathematics
[14]: /subjects/mathematics
[15]: /subjects/number-theory
[16]: /subjects/probability-theory
[17]: /subjects/probabilistic-methods-in-additive-number-theory
[18]: /article/10.1007/s00208-023-02579-w#ref-CR6
[19]: /article/10.1007/s00208-023-02579-w#Sec7
[20]: /article/10.1007/s00208-023-02579-w#ref-CR3
[21]: /article/10.1007/s00208-023-02579-w#ref-CR2
[22]: /article/10.1007/s00208-023-02579-w#FPar1
[23]: /article/10.1007/s00208-023-02579-w#FPar2
[24]: /article/10.1007/s00208-023-02579-w#Equ1
[25]: /article/10.1007/s00208-023-02579-w#FPar4
[26]: /article/10.1007/s00208-023-02579-w#FPar8
[27]: /article/10.1007/s00208-023-02579-w#FPar13
[28]: /article/10.1007/s00208-023-02579-w#FPar10
[29]: /article/10.1007/s00208-023-02579-w#FPar15
[30]: /article/10.1007/s00208-023-02579-w#FPar16
[31]: /article/10.1007/s00208-023-02579-w#Fig1
[32]: /article/10.1007/s00208-023-02579-w/figures/1
[33]: /article/10.1007/s00208-023-02579-w#FPar20
[34]: /article/10.1007/s00208-023-02579-w#FPar18
[35]: /article/10.1007/s00208-023-02579-w#FPar21
[36]: /article/10.1007/s00208-023-02579-w#FPar25
[37]: /article/10.1007/s00208-023-02579-w#ref-CR7
[38]: /article/10.1007/s00208-023-02579-w#ref-CR8
[39]: /article/10.1007/s00208-023-02579-w#ref-CR5
[40]: /article/10.1007/s00208-023-02579-w#ref-CR4
[41]: /article/10.1007/s00208-023-02579-w#ref-CR1
[42]: https://institucional.us.es/blogimus/en/2020/07/gilbreaths-conjecture/
[43]: https://doi.org/10.1090%2FS0025-5718-1993-1182247-7
[44]: http://www.ams.org/mathscinet-getitem?mr=1182247
[45]: http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&amp;bibcode=1993MaCom..61..373O
[46]: http://scholar.google.com/scholar_lookup?amp;title=Iterated%20absolute%20values%20of%20differences%20of%20consecutive%20primes&amp;journal=Math.%20Comput.&amp;doi=10.1090%2FS0025-5718-1993-1182247-7&amp;volume=61&amp;pages=373-380&amp;publication_year=1993&amp;author=Odlyzko%2CAM
[47]: http://scholar.google.com/scholar_lookup?amp;title=Sur%20la%20formule%20%24%242%5E%7B2%5En%7D%2B1%24%24%202%202%20n%20%2B%201&amp;journal=Comp.%20Rend.%20Acad.%20Sci.%20Paris&amp;volume=85&amp;pages=329-331&amp;publication_year=1877&amp;author=Pepin%2CF
[48]: http://scholar.google.com/scholar_lookup?amp;title=Th%C3%A9or%C3%A8mes%20sur%20les%20nombres%20premiers&amp;journal=Comp.%20Rend.%20Acad.%20Sci.%20Paris&amp;volume=87&amp;pages=329-331&amp;publication_year=1877&amp;author=Proth%2CF
[49]: http://scholar.google.com/scholar_lookup?amp;title=Sur%20la%20s%C3%A9rie%20des%20nombres%20premiers&amp;journal=Nouvelle%20Correspondance%20Math%C3%A9matique&amp;volume=4&amp;pages=236-240&amp;publication_year=1878&amp;author=Proth%2CF
[50]: http://scholar.google.com/scholar_lookup?amp;title=Edouard%20Lucas%20and%20Primality%20Testing.%20Canad.%20Math.%20Soc.%20Ser.%20Monogr.%20Adv.%20Texts&amp;publication_year=1998&amp;author=Williams%2CHC
[51]: https://citation-needed.springer.com/v2/references/10.1007/s00208-023-02579-w?format=refman&amp;flavour=references
[52]: /search?sortBy=newestFirst&amp;contributor=Zachary%20Chase
[53]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Zachary%20Chase
[54]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Zachary%20Chase%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[55]: mailto:zachary.chase@maths.ox.ac.uk
[56]: http://creativecommons.org/licenses/by/4.0/
[57]: https://s100.copyright.com/AppDispatchServlet?title=A%20random%20analogue%20of%20Gilbreath%E2%80%99s%20conjecture&amp;author=Zachary%20Chase&amp;contentID=10.1007%2Fs00208-023-02579-w&amp;copyright=The%20Author%28s%29&amp;publication=0025-5831&amp;publicationDate=2023-02-24&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[58]: https://crossmark.crossref.org/dialog/?doi=10.1007/s00208-023-02579-w
[59]: https://citation-needed.springer.com/v2/references/10.1007/s00208-023-02579-w?format=refman&amp;flavour=citation
