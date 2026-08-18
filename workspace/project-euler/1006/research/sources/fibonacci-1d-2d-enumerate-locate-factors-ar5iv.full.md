<!-- source: https://ar5iv.labs.arxiv.org/html/2207.04304 | converted from HTML -->

[2207.04304] Fibonacci Sequences of ⁢ 1 D , ⁢ 2 D Words: Enumerating and Locating the Factors of the Fixed Points

\publicationdetails

# Fibonacci Sequences of 1 ​ D 1D, 2 ​ D 2D Words: Enumerating and Locating the Factors of the Fixed Points

Sivasankar M Thanks: Corresponding Author Rama R Department of Mathematics, Indian Institute of Technology Madras, Chennai, India

###### Abstract

Given an infinite word, enumerating its factors is an important exercise for understanding the structure of the word. The process of finding all the factors is quite tricky for two-dimensional words. In this paper, two possible ways of enumerating the factors of the fixed point ( f ∞, ∞ f_{\infty,\infty}) of the sequence of Fibonacci arrays and a method for locating these factors in f ∞, ∞ f_{\infty,\infty} are explored. In addition, the factor complexity and the locations of the factors of the fixed point of Fibonacci sequence of arrays are also analysed.

###### Keywords:

Fibonacci words, Two-dimensional Fibonacci words (Fibonacci arrays), Sequence of Fibonacci Arrays, Fibonacci Sequence of Arrays, Factors, Conjugates of two-dimensional words, Directed Acyclic Word Graph.

## 1 Introduction

Let w w be finite/infinite word over an alphabet Σ \Sigma. The details about the subwords (otherwise called, the factors) of w w would be of considerable use for a better understanding of the structure and characteristics of w w. The number of factors and the periodic (or primitive) nature of the word w w are closely related and are in general analysed simultaneously. Any additional information about the factors of w w can help in the factorization/decomposition of w w. In turn, factorizations like Lyndon, Ziv–Lempel and Crochemore are used in text compression algorithms [5, 15].

Fibonacci words (more generally Sturmian words) are "simple" morphic words. By "simple", we mean that the morphisms defining these words are short and are easily conceivable. Also, it is known that, for infinite words w w, which are not ultimately periodic, p n ​ ( w) ≥ n + 1 p_{n}(w)\geq n+1, where p n ​ ( w) p_{n}(w) is the number of factors of length n n of w w [3]. It is interesting to note that Sturmian words are a class of aperiodic infinite words that achieve the least possible p n p_{n} value, namely n + 1 n+1 [20].

Generating the Fibonacci words over { 0, 1 } \{0,1\} can be systematically achieved either by the famous Fibonacci morphism, ϕ ⁡ ( 1) = 10 \phi(1)=10, ϕ ⁡ ( 0) = 1 \phi(0)=1 [20] or by recursive constructions like f 0 = 1, f 1 = 10, f n = f n − 1 ​ f n − 2, n ≥ 2 f_{0}=1,f_{1}=10,f_{n}=f_{n-1}f_{n-2},n\geq 2 [7, 8, 9]. Infinite iterations of the Fibonacci morphism or the recursion, generates the infinite Fibonacci word f ∞ = 10110101 ​ … f_{\infty}=10110101\ldots. Some remarkable properties of f n f_{n} and f ∞ f_{\infty} are: (i) f ∞ f_{\infty} contains no fourth power, (ii) if a word u 2 u^{2} is a factor of f ∞ f_{\infty}, then u u is a conjugate of some finite Fibonacci word, (iii) The finite Fibonacci words are primitive [3, 21].

With a minimum number of subwords of any particular length, it is no wonder that the subwords occur again and again, at various locations, in f ∞ f_{\infty} [10, 31, 24]. There are a few interesting systematic ways to list these subwords. In [3], subwords of length k k are used to list the subwords of length k + 1 k+1. In [26], a directed acyclic word graph ( D ​ A ​ W ​ G DAWG) is used to analyse the subwords. In [10], the suffixes of the conjugates of a specific conjugate of a finite Fibonacci word is used to find all the factors of a given length.

As a natural extension to the one-dimensional words, two-dimensional words are studied [13, 25, 27]. We will interchangeably use 1 ​ D 1D for one-dimensional and 2 ​ D 2D for two-dimensional, hereafter in this article. Two-dimensional words finding some useful applications in image processing, data compression and crystallography is another push for exploring two-dimensional words. In [2], 2 ​ D 2D Fibonacci words, f m, n, m, n ≥ 0 f_{m,n},m,n\geq 0, are introduced to show that they attain the general upper bound for the number of occurrences of a particular type of tandem. In [18, 22], a few combinatorial and palindromic properties of f m, n f_{m,n} are studied. In [28], the authors obtain f ∞, ∞ f_{\infty,\infty}, the 2 ​ D 2D infinite Fibonacci word, using a 2 ​ D 2D morphism. Further, they count the number of tandems occurring in it.

In this paper, we list all the subwords of a given size ( k, l), k, l ≥ 1 (k,l),k,l\geq 1 of the 2 ​ D 2D infinite Fibonacci word f ∞, ∞ f_{\infty,\infty}. We systematically extend the methods used in [26, 10] for finding the subwords of f ∞ f_{\infty}, to f ∞, ∞ f_{\infty,\infty}. In the later part of the paper, by using strings (of length two or more) for symbols in the Fibonacci sequence of arrays, we obtain sequences of Fibonacci arrays, and we investigate the factors of the fixed points of such sequences.

The remaining of the paper is organized as follows. In Section 2, all the required definitions and notions are elaborated. In Section 3, a D ​ A ​ W ​ G DAWG for f ∞, ∞ f_{\infty,\infty} is constructed and the subwords of f ∞, ∞ f_{\infty,\infty} are enumerated. In Section 4, given a k ≥ 2 k\geq 2 and a l ≥ 2 l\geq 2, to list all the subwords of size ( k, l) (k,l), the conjugates of a special conjugate of f m, n f_{m,n} ( m, n m,n depend on k, l k,l) are used. In Section 5, the location of the factors of f ∞, ∞ f_{\infty,\infty} are found out. Section 6 analyses the factors and the locations of the factors of the fixed points of the Fibonacci sequences of 1 ​ D 1D words. Section 7 extends the concepts of Section 6 to two dimensions. Finally, Section 8 has a few concluding remarks.

## 2 Preliminaries

### 2.1 One-dimensional Words

In formal language theory, Σ \Sigma, an alphabet is a finite set of symbols and Σ ∗ \Sigma^{*} is the free monoid generated by Σ \Sigma. The elements of Σ ∗ \Sigma^{*} are called words and are obtained by concatenating symbols from Σ \Sigma. The neutral element of Σ ∗ \Sigma^{*} is the empty word (denoted by λ \lambda) and we have Σ + = Σ ∗ − { λ } \Sigma^{+}=\Sigma^{*}-\{\lambda\}. For a word u ∈ Σ ∗ u\in\Sigma^{*}, | u | |u| called the length of the word is the number of letters occurring in u u. By definition, | λ | = 0 |\lambda|=0. Given a word w ∈ Σ ∗ w\in\Sigma^{*}, u ∈ Σ ∗ u\in\Sigma^{*} is a prefix (suffix, respectively) of w w, if w = u ​ v w=uv ( w = v ​ u w=vu, respectively) for some v ∈ Σ ∗ v\in\Sigma^{*}. The reversal of a word u = a 1 a 2 ⋯ a n u=a_{1}a_{2}\cdots a_{n}, a i ∈ Σ a_{i}\in\Sigma, for 1 ≤ i ≤ n 1\leq i\leq n, is the word u R = a n ⋯ a 2 a 1 u^{R}=a_{n}\cdots a_{2}a_{1}. A word u u is said to be a palindrome (or a one-dimensional palindrome) if u = u R u=u^{R}.

A word w w is said to be primitive if w = u n w=u^{n} implies n = 1 n=1 and w = u w=u. Note that a power of a word is nothing but repeated concatenation of the word with itself. That is u n u^{n} is obtained by concatenating u u with itself n n times. For a detailed study of formal language theory and combinatorics on words, the reader is referred to [19].

### 2.2 Two-dimensional Words

The concepts of formal language theory can be obviously extended to two dimensions [13]. A two-dimensional word is called a picture or array and is a rectangular array of symbols taken from Σ \Sigma.

###### Definition 1.

[18] A 2 ​ D 2D word u = [u i, j] 1 ≤ i ≤ m, 1 ≤ j ≤ n u=[u_{i,j}]_{1\leq i\leq m,1\leq j\leq n} of size ( m, n) (m,n) over Σ \Sigma is a two-dimensional rectangular finite arrangement of letters:

 | u = u 1, 1 u 1, 2 ⋯ u 1, n − 1 u 1, n u 2, 1 u 2, 2 ⋯ u 2, n − 1 u 2, n ⋱ u m − 1, 1 u m − 1, 2 ⋯ u m − 1, n − 1 u m − 1, n u m, 1 u m, 2 ⋯ u m, n − 1 u m, n u=\begin{matrix}u_{1,1}&u_{1,2}&\cdots&u_{1,n-1}&u_{1,n}\\ u_{2,1}&u_{2,2}&\cdots&u_{2,n-1}&u_{2,n}\\ \vdots&\vdots&\ddots&\vdots&\vdots\\ u_{m-1,1}&u_{m-1,2}&\cdots&u_{m-1,n-1}&u_{m-1,n}\\ u_{m,1}&u_{m,2}&\cdots&u_{m,n-1}&u_{m,n}\\ \end{matrix} |  |

We denote the number of rows and columns of u u by | u | row |u|_{\text{row}} and | u | col |u|_{\text{col}}, respectively. An empty array, denoted by Λ \Lambda is an array of size ( 0, 0) (0,0). Note that the arrays of size ( m, 0) (m,0) and ( 0, m) (0,m) for m > 0 m>0 are not defined. The set of all arrays over Σ \Sigma including Λ \Lambda, is denoted by Σ ∗ ⁣ ∗ \Sigma^{**} and Σ + ⁣ + \Sigma^{++} will denote the set of all non-empty arrays over Σ \Sigma. Any subset of Σ ∗ ⁣ ∗ \Sigma^{**} is called a picture language.

To locate any position or region in an array, we require a reference system [1]. Given an array u u, the set of coordinates { 1, 2, …, | u | row } × { 1, 2, …, | u | col } \{1,2,\ldots,|u|_{\text{row}}\}\times\{1,2,\ldots,|u|_{\text{col}}\} is referred to as the domain of u u. A subdomain or subarray of an array u u (that is, a factor of the 2 ​ D 2D word u u), denoted by u ⁡ [( i, j), ( i ′, j ′)] u[(i,j),(i^{\prime},j^{\prime})], is the portion of u u located in the region { i, i + 1, …, i ′ } × { j, j + 1, …, j ′ } \{i,i+1,\ldots,i^{\prime}\}\times\{j,j+1,\ldots,j^{\prime}\}, where 1 ≤ i ≤ i ′ ≤ | u | row, 1 ≤ j ≤ j ′ ≤ | u | col 1\leq i\leq i^{\prime}\leq|u|_{\text{row}},1\leq j\leq j^{\prime}\leq|u|_{\text{col}}.

Similar to the concatenation operation in one dimension, the column concatenation and the row concatenation operations between two arrays are as follows.

###### Definition 2.

[13] Let u, v u,v be arrays over Σ \Sigma of sizes ( m 1, n 1) (m_{1},n_{1}) and ( m 2, n 2) (m_{2},n_{2}), respectively with m 1, n 1, m 2, n 2 > 0 m_{1},n_{1},m_{2},n_{2}>0. Then, the column concatenation of u u and v v, denoted by ⦶ \obar, is a partial operation, defined if m 1 = m 2 = m m_{1}=m_{2}=m, and is given by

 | u ⦶ v = u 1, 1 ⋯ u 1, n 1 v 1, 1 ⋯ v 1, n 2 u m, 1 ⋯ u m, n 1 v m, 1 ⋯ v m, n 2. u\obar v=\begin{matrix}u_{1,1}&\cdots&u_{1,n_{1}}&v_{1,1}&\cdots&v_{1,n_{2}}\\ \vdots&&\vdots&\vdots&&\vdots\\ u_{m,1}&\cdots&u_{m,n_{1}}&v_{m,1}&\cdots&v_{m,n_{2}}\end{matrix}. |  |

Similarly, the row concatenation of u u and v v, denoted by ⊖ \ominus, is another partial operation, defined if n 1 = n 2 = n n_{1}=n_{2}=n, and is given by

 | u ⊖ v = u 1, 1 ⋯ u 1, n u m 1, 1 ⋯ u m 1, n v 1, 1 ⋯ v 1, n v m 2, 1 ⋯ v m 2, n. u\ominus v=\begin{matrix}u_{1,1}&\cdots&u_{1,n}\\ \vdots&&\vdots\\ u_{m_{1},1}&\cdots&u_{m_{1},n}\\ v_{1,1}&\cdots&v_{1,n}\\ \vdots&&\vdots\\ v_{m_{2},1}&\cdots&v_{m_{2},n}\end{matrix}. |  |

The column and row concatenation of u u and the empty array Λ \Lambda are always defined and Λ \Lambda is a neutral element for both the operations.

For a u ∈ Σ ∗ ⁣ ∗ u\in\Sigma^{**}, an array v ∈ Σ ∗ ⁣ ∗ v\in\Sigma^{**} is said to be a prefix of u u ( ( suffix of u u, respectively)), if u = ( v ⊖ x) ⦶ y u=(v\ominus x)\obar y ( u = y ⦶ ( x ⊖ v) CLOSE (u=y\obar(x\ominus v), respectively)) for some x, y ∈ Σ ∗ ⁣ ∗ x,y\in\Sigma^{**}. If x ∈ Σ + ⁣ + x\in\Sigma^{++}, then by ( x k 1 ⦶) k 2 ⊖ (x^{k_{1}\obar})^{k_{2}\ominus} we mean that the array is constructed by repeating x x, k 1 k_{1} times column-wise and x k 1 ⦶ x^{k_{1}\obar}, k 2 k_{2} times row-wise. An array w ∈ Σ + ⁣ + w\in\Sigma^{++} is said to be 2D primitive if w = ( x k 1 ⦶) k 2 ⊖ w=(x^{k_{1}\obar})^{k_{2}\ominus} implies that k 1 ​ k 2 = 1 k_{1}k_{2}=1 and w = x w=x [12].

### 2.3 Fibonacci Words

Fibonacci words are closely related with the Fibonacci numbers. Recall the recursive definition of the Fibonacci numerical sequence: F ⁡ ( 0) = 1 F(0)=1, F ⁡ ( 1) = 2 F(1)=2, F ⁡ ( n) = F ⁡ ( n − 1) + F ⁡ ( n − 2) F(n)=F(n-1)+F(n-2) for n ≥ 2 n\geq 2. Likewise, for Σ = { a, b } \Sigma=\{a,b\}, the sequence { f n } n ≥ 0 \{f_{n}\}_{n\geq 0} of Fibonacci words, is defined recursively by f 0 = a f_{0}=a, f 1 = a ​ b f_{1}=ab, f n = f n − 1 ​ f n − 2 f_{n}=f_{n-1}f_{n-2} for n ≥ 2 n\geq 2. First few words of this sequence are: f 0 = a, f 1 = a ​ b, f 2 = a ​ b ​ a, f 3 = a ​ b ​ a ​ a ​ b, f 4 = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a f_{0}=a,f_{1}=ab,f_{2}=aba,f_{3}=abaab,f_{4}=abaababa. Note that | f n | = F ⁡ ( n) |f_{n}|=F(n) for n ≥ 0 n\geq 0. The sequence of Fibonacci words can be obtained by iterating the Fibonacci morphism ϕ: Σ ∗ → Σ ∗ \phi:\Sigma^{*}\rightarrow\Sigma^{*} defined by ϕ ⁡ ( a) = a ​ b, ϕ ⁡ ( b) = a \phi(a)=ab,\phi(b)=a. An infinite number of iterations of ϕ \phi produces the 1 ​ D 1D infinite Fibonacci word f ∞ f_{\infty} [20]. That is,

 | lim n → ∞ ϕ n ​ ( b) = f ∞ = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ …. \lim_{n\to\infty}\phi^{n}(b)=f_{\infty}=abaababa\ldots. |  |

###### Remark 1.

In the literature, one can observe variations in the definitions of the Fibonacci numbers and the definitions of the Fibonacci words. That is, for the convenience of simplifying the indices used in the proofs, some authors define the Fibonacci number sequence as F ⁡ ( 0) = 1 F(0)=1, F ⁡ ( 1) = 1 F(1)=1, F ⁡ ( n) = F ⁡ ( n − 1) + F ⁡ ( n − 2) F(n)=F(n-1)+F(n-2) for n ≥ 2 n\geq 2 and the sequence of Fibonacci words as f 0 = b, f 1 = a, f n = f n − 1 ​ f n − 2 f_{0}=b,f_{1}=a,f_{n}=f_{n-1}f_{n-2} for n ≥ 2 n\geq 2. In such a case, the first few words of the sequence will be: f 0 = b, f 1 = a, f 2 = a ​ b, f 3 = a ​ b ​ a, f 4 = a ​ b ​ a ​ a ​ b f_{0}=b,f_{1}=a,f_{2}=ab,f_{3}=aba,f_{4}=abaab. But, in any case, the infinite Fibonacci word obtained will be the same. So, in the arguments used in this paper, we might have used the better of the two versions accordingly.

###### Remark 2.

We also use f ∞ s 1, s 2 f_{\infty}^{s_{1},s_{2}} to denote the 1 ​ D 1D infinite Fibonacci word s 1 ​ s 2 ​ s 1 ​ s 1 ​ s 2 ​ … s_{1}s_{2}s_{1}s_{1}s_{2}\ldots over the alphabet { s 1, s 2 } \{s_{1},s_{2}\}. Similarly, f n s 1, s 2 f_{n}^{s_{1},s_{2}} denotes the 1 ​ D 1D finite Fibonacci word s 1 ​ s 2 ​ s 1 ​ s 1 ​ s 2 ​ … ​ s 1 ​ s 2 s_{1}s_{2}s_{1}s_{1}s_{2}\ldots s_{1}s_{2} or s 1 ​ s 2 ​ s 1 ​ s 1 ​ s 2 ​ … ​ s 2 ​ s 1 s_{1}s_{2}s_{1}s_{1}s_{2}\ldots s_{2}s_{1} accordingly n n is even or odd.

The extension of 1 ​ D 1D Fibonacci words to 2 ​ D 2D Fibonacci words is presented in [2].

###### Definition 3.

[2] Let Σ = { a, b, c, d } \Sigma=\{a,b,c,d\}. The sequence of Fibonacci arrays, { f m, n } \{f_{m,n}\} where m, n ≥ 0 m,n\geq 0, is defined as:

1. 1.

f 0, 0 = β, f 0, 1 = γ, f 1, 0 = δ, f 1, 1 = α f_{0,0}=\beta,f_{0,1}=\gamma,f_{1,0}=\delta,f_{1,1}=\alpha where α, β, γ \alpha,\beta,\gamma and δ \delta are symbols from Σ \Sigma with some but not all, among α, β, γ \alpha,\beta,\gamma and δ \delta might be identical.

2. 2.

For k ≥ 0 k\geq 0 and m, n ≥ 1 m,n\geq 1,

 | f k, n + 1 = f k, n ⦶ f k, n − 1, f m + 1, k = f m, k ⊖ f m − 1, k. f_{k,n+1}=f_{k,n}\obar f_{k,n-1},\hskip 5.69046ptf_{m+1,k}=f_{m,k}\ominus f_{m-1,k}. |  |

For convenience, let us fix f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,f_{0,1}=b,f_{1,0}=c,f_{1,1}=d, where some but not all of a, b, c a,b,c and d d might be identical. For example, let us derive the 2 ​ D 2D Fibonacci word f 2, 2 f_{2,2}.

 | f 2, 2 = f 1, 2 ⊖ f 0, 2 = ( f 1, 1 ⦶ f 1, 0) ⊖ ( f 0, 1 ⦶ f 0, 0). f_{2,2}=f_{1,2}\ominus f_{0,2}=(f_{1,1}\obar f_{1,0})\ominus(f_{0,1}\obar f_{0,0}). |  |

It can also be obtained by column-wise expansion,

 | f 2, 2 = f 2, 1 ⦶ f 2, 0 = ( f 1, 1 ⊖ f 0, 1) ⦶ ( f 1, 0 ⊖ f 0, 0). f_{2,2}=f_{2,1}\obar f_{2,0}=(f_{1,1}\ominus f_{0,1})\obar(f_{1,0}\ominus f_{0,0}). |  |

Using f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,f_{0,1}=b,f_{1,0}=c,f_{1,1}=d, f 2, 2 f_{2,2} is given by

 | f 2, 2 = f 1, 1 f 1, 0 f 0, 1 f 0, 0 = d c b a. f_{2,2}=\>\begin{matrix}f_{1,1}&f_{1,0}\\ f_{0,1}&f_{0,0}\end{matrix}\>=\>\begin{matrix}d&c\\ b&a\end{matrix}. |  |

We state here some properties of f m, n f_{m,n} which we would use later in our proofs.

###### Lemma 1.

[22] Let f m, n, ( m, n = 0, 1, 2, …) f_{m,n},(m,n=0,1,2,\dotsc) be the sequence of 2 ​ D 2D Fibonacci arrays over Σ = { a, b, c, d } \Sigma=\{a,b,c,d\}, with f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,f_{0,1}=b,f_{1,0}=c,f_{1,1}=d. Also let Σ 1 = { a, b } \Sigma_{1}=\{a,b\}, Σ 2 = { c, d } \Sigma_{2}=\{c,d\}, Σ 1 ′ = { a, c } \Sigma_{1}^{\prime}=\{a,c\} and Σ 2 ′ = { b, d } \Sigma_{2}^{\prime}=\{b,d\} such that Σ = Σ 1 ∪ Σ 2 = Σ 1 ′ ∪ Σ 2 ′ \Sigma=\Sigma_{1}\cup\Sigma_{2}=\Sigma_{1}^{\prime}\cup\Sigma_{2}^{\prime}. Then,

- a.

any row of f m, n f_{m,n} is a 1 ​ D 1D Fibonacci word over either Σ 1 \Sigma_{1} or Σ 2 \Sigma_{2}.

- b.

if Σ 1 ≠ Σ 2 \Sigma_{1}\neq\Sigma_{2} then all the rows of f m, n f_{m,n}, over Σ 1 \Sigma_{1} are identical and all the rows of f m, n f_{m,n}, over Σ 2 \Sigma_{2} are identical.

- c.

any column of f m, n f_{m,n} is a 1 ​ D 1D Fibonacci word over either Σ 1 ′ \Sigma_{1}^{\prime} or Σ 2 ′ \Sigma_{2}^{\prime}.

- d.

if Σ 1 ′ ≠ Σ 2 ′ \Sigma_{1}^{\prime}\neq\Sigma_{2}^{\prime} then all the columns of f m, n f_{m,n}, over Σ 1 ′ \Sigma_{1}^{\prime} are identical and all the columns of f m, n f_{m,n}, over Σ 2 ′ \Sigma_{2}^{\prime} are identical.

- e.

if Σ 1 = Σ 2 ​ ( Σ 1 ′ = Σ 2 ′) \Sigma_{1}=\Sigma_{2}(\Sigma_{1}^{\prime}=\Sigma_{2}^{\prime}), then either all the rows ( ( columns)) of f m, n f_{m,n} are identical or a set of rows are identical and are complementary to the set of remaining rows ( ( columns, respectively)) which are identical.

### 2.4 The 2 ​ D 2D Infinite Fibonacci Word, f ∞, ∞ f_{\infty,\infty}

The sequence of 2 ​ D 2D finite Fibonacci words, { f m, n } m, n ≥ 0 \{f_{m,n}\}_{m,n\geq 0}, in a sense, has the 2 ​ D 2D infinite Fibonacci word, f ∞, ∞ f_{\infty,\infty}, as its limit. This can be perceived by extending each row, column of any f m, n f_{m,n}, m, n ≥ 2 m,n\geq 2, to the 1 ​ D 1D infinite Fibonacci word over the alphabet of the word present in that row, column. But this outlook is informal. Formally, in [28], the authors have defined the 2 ​ D 2D infinite Fibonacci word through the 2 ​ D 2D morphism,

 | μ: d → d c b a, c → d b, b → d c, a → d. \mu:~~d\rightarrow\begin{matrix}d&c\\ b&a\end{matrix},~~c\rightarrow\begin{matrix}d\\ b\end{matrix},~~b\rightarrow\begin{matrix}d&c\end{matrix},~~~a\rightarrow d. |  | (1) |

For a detailed study of multidimensional morphisms, [6] can be referred.

Observe that the morphism defined by ( 1) is prolongable on d d and an infinite number of iterations of μ \mu on d d produces f ∞, ∞ f_{\infty,\infty} [28]. That is to say, f ∞, ∞ f_{\infty,\infty} is the fixed point of the morphism μ \mu. That is,

 | f ∞, ∞ = lim n → + ∞ μ n ​ ( d) = μ ω ​ ( d). f_{\infty,\infty}=\lim_{n\rightarrow+\infty}\mu^{n}(d)=\mu^{\omega}(d). |  |

First few iterations of μ \mu on d d are shown below.

 | d → d c b a → d c d b a b d c d → d c d d c b a b b a d c d d c d c d d c b a b b a → ⋯ → d c d d c d c d ⋯ b a b b a b a b ⋯ d c d d c d c d ⋯ d c d d c d c d ⋯ b a b b a b a b ⋯ d c d d c d c d ⋯ b a b b a b a b ⋯ d c d d c d c d ⋯ ⋱ d\rightarrow\begin{matrix}d&c\\ b&a\end{matrix}\rightarrow\begin{matrix}d&c&d\\ b&a&b\\ d&c&d\end{matrix}\rightarrow\begin{matrix}d&c&d&d&c\\ b&a&b&b&a\\ d&c&d&d&c\\ d&c&d&d&c\\ b&a&b&b&a\\ \end{matrix}\rightarrow\cdots\rightarrow\begin{matrix}d&c&d&d&c&d&c&d&\cdots\\ b&a&b&b&a&b&a&b&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ b&a&b&b&a&b&a&b&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ b&a&b&b&a&b&a&b&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ \vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\ddots\end{matrix} |  |

As f ∞, ∞ f_{\infty,\infty} is the limit of { f m, n } m, n ≥ 0 \{f_{m,n}\}_{m,n\geq 0}, all the properties listed in Lemma 1 are true for f ∞, ∞ f_{\infty,\infty} also.

## 3 Enumeration Using Subword Graphs

In [26] the authors have given a way to identify the subwords of f ∞ f_{\infty} using a directed acyclic graph.

The directed acyclic word graph of a word w w, D ​ A ​ W ​ G ​ ( w) DAWG(w), is the smallest finite state automaton that recognizes all the suffixes of the word [4]. C ​ D ​ A ​ W ​ G ​ ( w) CDAWG(w), a space efficient variant of D ​ A ​ W ​ G ​ ( w) DAWG(w), is obtained by compacting D ​ A ​ W ​ G ​ ( w) DAWG(w) [11].

In [26], the subwords of f ∞ f_{\infty} are analysed through the graph 𝒢 ∞ \mathcal{G}_{\infty}, which is, in a certain sense, a D ​ A ​ W ​ G DAWG of f ∞ = a ​ b ​ a ​ a ​ b ​ a ​ b ​ b ​ … = f ∞ ​ ( 1, 2, 3, …) f_{\infty}=abaababb\ldots=f_{\infty}(1,2,3,\ldots). The D ​ A ​ W ​ G DAWG is constructed as below:

Let F ⁡ ( 0) = 1, F ⁡ ( 1) = 2, F ⁡ ( n) = F ⁡ ( n − 1) + F ⁡ ( n − 2) F(0)=1,F(1)=2,F(n)=F(n-1)+F(n-2), for n ≥ 2 n\geq 2, be the Fibonacci sequence (Note that for a n a_{n}). The nodes of 𝒢 ∞ \mathcal{G}_{\infty} are all non-negative integers. For i > 0 i>0, with F ⁡ ( i) F(i) being the i t ​ h i^{th} Fibonacci number, the labelled edges of 𝒢 ∞ \mathcal{G}_{\infty} are

 | ( i − 1) → f ∞ ​ ( i) i, F ⁡ ( i) − 2 → 𝑠 F ⁡ ( i + 1) − 1 \displaystyle(i-1)\xrightarrow{f_{\infty}(i)}i,\quad F(i)-2\;\xrightarrow{\;s\;}\;F(i+1)-1 |  |

where s = a s=a whenever i i is even and s = b s=b whenever i i is odd (Refer Fig. 1).

[image: Refer to caption] Figure 1: DAWG, 𝒢 ∞ \mathcal{G}_{\infty} of f ∞ a, b f_{\infty}^{a,b}

### 3.1 Cross Product of D ​ A ​ W ​ G DAWG s

As the 2 ​ D 2D finite Fibonacci words, f m, n f_{m,n}, can be obtained by the Cartesian product of Fibonacci reduced representation of the integers m, n m,n [18], a natural extension of 𝒢 ∞ \mathcal{G}_{\infty} for the 2 ​ D 2D infinite Fibonacci word will be the Cartesian product of 𝒢 ∞ \mathcal{G}_{\infty} with itself.

###### Definition 4.

[32] The Cartesian product of G and H, written G ​ □ ​ H G\,\square\,H, is the graph with vertex set V ⁡ ( G) × V ⁡ ( H) V(G)\times V(H) specified by putting ( u, v) (u,v) adjacent to ( u ′, v ′) (u^{\prime},v^{\prime}) if and only if ( 1) ​ u = u ′ (1)u=u^{\prime} and v ​ v ′ ∈ E ⁡ ( H) vv^{\prime}\in E(H), or ( 2) ​ v = v ′ (2)v=v^{\prime} and u ​ u ′ ∈ E ⁡ ( G) uu^{\prime}\in E(G).

Since f ∞, ∞ f_{\infty,\infty} has two distinct rows (one over { d, c } \{d,c\} and one over { b, a } \{b,a\}), to obtain a D ​ A ​ W ​ G DAWG of f ∞, ∞ f_{\infty,\infty}, we slightly modify the labels of 𝒢 ∞ \mathcal{G}_{\infty}. Note that, all the rows of f ∞, ∞ f_{\infty,\infty} are f ∞ f_{\infty} only. In fact the rows over { d, c } \{d,c\} would be d ​ c ​ d ​ d ​ c ​ d ​ c ​ d ​ … dcddcdcd\ldots and the rows over { b, a } \{b,a\} would be b ​ a ​ b ​ b ​ a ​ b ​ a ​ b ​ … babbabab\ldots. In order to simultaneously control these two categories of rows/words, we will use a single D ​ A ​ W ​ G DAWG, the D ​ A ​ W ​ G DAWG of the Fibonacci word D ​ C ​ D ​ D ​ C ​ D ​ C ​ D ​ … DCDDCDCD\ldots, with D = { d, b } D=\{d,b\} and C = { c, a } C=\{c,a\}. With this adaptation, D D is allowed to assume either d d or b b and C C is allowed to assume either c c or a a. As the rows of f ∞, ∞ f_{\infty,\infty} are words over a binary alphabet, we also impose an additional condition that, if D D assumes d d then C C would assume c c and if D D assumes b b then C C would assume a a. This D ​ A ​ W ​ G DAWG, say " 𝒢 ∞ \mathcal{G}_{\infty} for rows ", is depicted at the top, in Fig. 2. In the graph, for convenience, we have written D = { d, b } D=\{d,b\} and C = { c, a } C=\{c,a\} as ‘ d, b d,b ’and ‘ c, a c,a ’, respectively.

[image: Refer to caption] Figure 2: The Cartesian product of 𝒢 ∞ \mathcal{G}_{\infty} for columns and 𝒢 ∞ \mathcal{G}_{\infty} for rows

Similarly, since f ∞, ∞ f_{\infty,\infty} has two distinct columns (one over { d, b } \{d,b\} and one over { c, a } \{c,a\}), to manage both the type of columns through a single D ​ A ​ W ​ G DAWG, we consider the D ​ A ​ W ​ G DAWG of the Fibonacci word D ′ ​ B ​ D ′ ​ D ′ ​ B ​ D ′ ​ B ​ D ′ ​ … D^{\prime}BD^{\prime}D^{\prime}BD^{\prime}BD^{\prime}\ldots, where D ′ = { d, c } D^{\prime}=\{d,c\} and B = { b, a } B=\{b,a\}, implying D ′ D^{\prime} can be either d d or c c, and B B can be either b b or a a, with an additional condition that, if D ′ D^{\prime} is d d then B B would be b b and if D ′ D^{\prime} is c c then B B would be a a. Again, in the graph, for convenience we write only ‘ d, c d,c ’ and ‘ b, a b,a ’ (without the curly braces). This D ​ A ​ W ​ G DAWG, say " 𝒢 ∞ \mathcal{G}_{\infty} for columns ", is depicted at the left, in Fig. 2.

Now we obtain the Cartesian product of " 𝒢 ∞ \mathcal{G}_{\infty} for columns " and " 𝒢 ∞ \mathcal{G}_{\infty} for rows ". Note that, when G G and H H are labelled, the labels are carried over to the edges of the Cartesian product appropriately. The resulting graph is given in Fig. 2.

Since 1 ​ D 1D words have only one direction, one can get all the letters of a subword by traversing along a directed path (starting at the root) of their D ​ A ​ W ​ G DAWG s. But in D ​ A ​ W ​ G DAWG s of 2 ​ D 2D words, to get all the letters in a subword, all the edges that lie between the root and any node that lie in a different column/row may have to be traversed. Clearly, this is not possible as the intended D ​ A ​ W ​ G DAWG (that is, the Cartesian product) is acyclic and also prevents any back-and-forth traversals.

But the structure of 2 ​ D 2D Fibonacci words is such that, for a subword u u of f ∞, ∞ f_{\infty,\infty}, the knowledge of any one row and any one column of u u is enough to write down the entire u u. Due to this, the Cartesian product will serve as the D ​ A ​ W ​ G DAWG of f ∞, ∞ f_{\infty,\infty}. Further, since it is enough to know just a row and a column of u u, even the Cartesian product is redundant and we need only the " rooted product " of " 𝒢 ∞ \mathcal{G}_{\infty} for rows " and " 𝒢 ∞ \mathcal{G}_{\infty} for columns ".

### 3.2 Rooted Product of D ​ A ​ W ​ G DAWG s

###### Definition 5.

[17] The rooted product of a graph G G and a rooted graph H H, denoted by G ∘ H G\circ H, is defined as follows:: take | V ⁡ ( G) | |V(G)| copies of H H, and for every vertex v i v_{i} of G G, identify v i v_{i} with the root vertex of the i t ​ h i^{th} copy of H H.

In other words if the vertex set of G G is { g 1, …, g n } \{g_{1},\ldots,g_{n}\} and the vertex set of H H is { h 1, …, h m } \{h_{1},\ldots,h_{m}\} with h 1 h_{1} as its root, then the vertex set, V V and the edge set, E E of G ∘ H G\circ H will be as below.

 | V \displaystyle V | = { ( g i, h j): 1 ≤ i ≤ n, 1 ≤ j ≤ m } \displaystyle=\{(g_{i},h_{j}):1\leq i\leq n,1\leq j\leq m\} |  |

 | E \displaystyle E | = E 1 ∪ E 2 where, \displaystyle=E_{1}\cup E_{2}\quad\text{where,} |  |

 | E 1 \displaystyle E_{1} | = { ( ( g i, h 1), ( g k, h 1)): ( g i, g k) ∈ E ⁡ ( G) }, \displaystyle=\{((g_{i},h_{1}),(g_{k},h_{1})):(g_{i},g_{k})\in E(G)\}, |  |

 | E 2 \displaystyle E_{2} | = ⋃ i = 1 n { ( ( g i, h j), ( g i, h k)): ( h j, h k) ∈ E ⁡ ( H) } \displaystyle=\bigcup_{i=1}^{n}\{((g_{i},h_{j}),(g_{i},h_{k})):(h_{j},h_{k})\in E(H)\} |  |

In fact, it is easy to see that, G ∘ H G\circ H is a subgraph of G ​ □ ​ H G\square H.

Now, we take the " rooted product " of " 𝒢 ∞ \mathcal{G}_{\infty} for rows " and " 𝒢 ∞ \mathcal{G}_{\infty} for columns " (Refer Fig. 3) to get the D ​ A ​ W ​ G DAWG of f ∞, ∞ f_{\infty,\infty} and denote it by 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}. From 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}, we can obtain the first row and the last column of any subword of f ∞, ∞ f_{\infty,\infty}. We designate the node ( 0, 0) (0,0) as the root node of 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}.

[image: Refer to caption] Figure 3: DAWG, 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty} of f ∞, ∞ f_{\infty,\infty}: ( 𝒢 ∞ \mathcal{G}_{\infty} for rows) ∘ \circ ( 𝒢 ∞ \mathcal{G}_{\infty} for columns)

### 3.3 Enumerating the subwords: The D ​ A ​ W ​ G DAWG way

In this subsection, we prove that the number of finite paths in 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}, starting at its root node, equals the number of subwords of f ∞, ∞ f_{\infty,\infty}. In particular, we prove that, for k, l ≥ 1 k,l\geq 1, a path of length k + l k+l, comprising of a horizontal path of length k k and a vertical path of length l l, will lead to subword of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l). Note that by a horizontal path (a vertical path, respectively), we mean a path whose adjacent vertices are in 𝒢 ∞ \mathcal{G}_{\infty} for rows ( 𝒢 ∞ \mathcal{G}_{\infty} for columns, respectively).

###### Theorem 1.

Let k, l ∈ ℕ k,l\in\mathbb{N} be given. Then, from a path of length k + l k+l (starting at the root) in 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}, comprising of a horizontal path of length l l and a vertical path of length k k, we can construct a subword of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l).

###### Proof.

Due to the construction of 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}, when we start at the root and traverse a horizontal path of length l ≥ 1 l\geq 1, we get a subword of the 1 ​ D 1D Fibonacci infinite word D ​ C ​ D ​ D ​ C ​ D ​ C ​ D ​ … DCDDCDCD\ldots. In fact, we can obtain two horizontal subwords of length l l, one over { d, c } \{d,c\} (obtained by taking d d for D D and c c for C C) and one over { b, a } \{b,a\} (obtained by taking b b for D D and a a for C C). The former subword occurs in any row of f ∞, ∞ f_{\infty,\infty} which is over { d, c } \{d,c\}, and the later occurs in any row of f ∞, ∞ f_{\infty,\infty} which is over { b, a } \{b,a\}.

Now, starting from the last node of this horizontal path, we traverse a vertical path of length k k. Note that, the rooted product guarantees such a path. Similar to the earlier argument, here we obtain a vertical path of length k ≥ 1 k\geq 1, which corresponds to a subword of length k k of the 1 ​ D 1D Fibonacci infinite word D ′ ​ B ​ D ′ ​ D ′ ​ B ​ D ′ ​ B ​ D ′ ​ … D^{\prime}BD^{\prime}D^{\prime}BD^{\prime}BD^{\prime}\ldots. Here also we can obtain two vertical subwords of length k k, one over { d, b } \{d,b\} (obtained by taking d d for D ′ D^{\prime} and b b for B B) and one over { c, a } \{c,a\} (obtained by taking c c for D ′ D^{\prime} and a a for B B). The former subword occurs in any column of f ∞, ∞ f_{\infty,\infty} which is over { d, b } \{d,b\}, and the later occurs in any column of f ∞, ∞ f_{\infty,\infty} which is over { c, a } \{c,a\}.

To prove that these two paths can produce a unique subword of size ( k, l) (k,l) of f ∞, ∞ f_{\infty,\infty}, we use the fact that ‘ the last letter in the first row and the first letter in the last column of a 2 ​ D 2D word are the same’. Hence, while constructing the subword, the last letter (say " s j ​ o ​ i ​ n ​ t s_{joint} ") in the horizontal path has to be the first letter in the vertical path. For example, out of the two available subwords of length l l, suppose we select the subword over { d, c } \{d,c\}, say H H, and if s j ​ o ​ i ​ n ​ t s_{joint} = d =d ( s j ​ o ​ i ​ n ​ t s_{joint} = c =c, respectively), then we will(have to) select the vertical subword , say V V, over { d, b } \{d,b\} ( { c, a } \{c,a\}, respectively). Now, by taking H H and V V as the first row and the last column, respectively, in a 2 ​ D 2D word of size ( k, l) (k,l), we will obtain the entire subword. Again note that, this is not possible for all 2 ​ D 2D words, but for f ∞, ∞ f_{\infty,\infty}, due to its structure.

As any row of f ∞, ∞ f_{\infty,\infty} is either over Σ 1 = { a, b } \Sigma_{1}=\{a,b\} or Σ 2 = { c, d } \Sigma_{2}=\{c,d\}, s j ​ o ​ i ​ n ​ t s_{joint} has to be either in Σ 1 \Sigma_{1} or in Σ 2 \Sigma_{2}. As any column of f ∞, ∞ f_{\infty,\infty} is either over Σ 1 ′ = { a, c } \Sigma_{1}^{\prime}=\{a,c\} or Σ 2 ′ = { b, d } \Sigma_{2}^{\prime}=\{b,d\}, V V has to be either in Σ 1 ′ \Sigma_{1}^{\prime} or in Σ 2 ′ \Sigma_{2}^{\prime}. Hence the following four cases only arise.

Case (i) | : | s j ​ o ​ i ​ n ​ t s_{joint} = a =a (then, V V will be over { a, c } \{a,c\}) |

Case (ii) | : | s j ​ o ​ i ​ n ​ t s_{joint} = b =b (then, V V will be over { b, d } \{b,d\}) |

Case (iii) | : | s j ​ o ​ i ​ n ​ t s_{joint} = c =c (then, V V will be over { a, c } \{a,c\}) |

Case (iv) | : | s j ​ o ​ i ​ n ​ t s_{joint} = d =d (then, V V will be over { b, d } \{b,d\}) |

To find the letters occurring at the other positions of u u we define two substitutions. If H H is over { a, b } \{a,b\}, we create a 1 ​ D 1D word H ′ H^{\prime} from H H using the substitution θ 1: θ 1 ​ ( a) = c, θ 1 ​ ( b) = d \theta_{1}:\theta_{1}(a)=c,\theta_{1}(b)=d. If H H is over { c, d } \{c,d\}, we create a 1 ​ D 1D word H ′′ H^{\prime\prime} from H H using the substitution θ 2: θ 2 ​ ( c) = a, θ 2 ​ ( d) = b \theta_{2}:\theta_{2}(c)=a,\theta_{2}(d)=b. These words H ′ H^{\prime} and H ′′ H^{\prime\prime} will be used to fill up/find the other rows of the subword we are constructing. These substitutions are motivated by the fact that, a row of f ∞, ∞ f_{\infty,\infty} over { a, b } \{a,b\} can be obtained from a row of f ∞, ∞ f_{\infty,\infty} over { c, d } \{c,d\} and vice-versa through simple substitutions.

Let R 1, R 2, R 3, …, R k R_{1},R_{2},R_{3},\ldots,R_{k} be the k k rows of the subword being constructed. Note that R 1 = H R_{1}=H. Now, for 2 ≤ j ≤ k 2\leq j\leq k,

Case(i): s j ​ o ​ i ​ n ​ t s_{joint} = a =a (and hence H H is over { a, b } \{a,b\})

If the letter in the j t ​ h j^{th} row of V V is s j ​ o ​ i ​ n ​ t s_{joint}, then R j = H R_{j}=H else R j = H ′ R_{j}=H^{\prime}.

Case(ii): s j ​ o ​ i ​ n ​ t s_{joint} = b =b (and hence H H is over { a, b } \{a,b\})

If the letter in the j t ​ h j^{th} row of V V is s j ​ o ​ i ​ n ​ t s_{joint}, then R j = H R_{j}=H else R j = H ′ R_{j}=H^{\prime}.

Case(iii): s j ​ o ​ i ​ n ​ t s_{joint} = c =c (and hence H H is over { c, d } \{c,d\})

If the letter in the j t ​ h j^{th} row of V V is s j ​ o ​ i ​ n ​ t s_{joint}, then R j = H R_{j}=H else R j = H ′′ R_{j}=H^{\prime\prime}.

Case(iv): s j ​ o ​ i ​ n ​ t s_{joint} = d =d (and hence H H is over { c, d } \{c,d\})

If the letter in the j t ​ h j^{th} row of V V is s j ​ o ​ i ​ n ​ t s_{joint}, then R j = H R_{j}=H else R j = H ′′ R_{j}=H^{\prime\prime}.

Note that while constructing the subword, the alphabet of each row and the order in which the two distinct rows ( H H and H ′ H^{\prime} (or) H H and H ′′ H^{\prime\prime}) of the subword are getting arranged are decided/guided by V V. Since V V is a subword of length l l of some column of f ∞, ∞ f_{\infty,\infty}, the obtained 2 ​ D 2D word is a subword of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l). ∎

###### Remark 3.

Theorem 1 can be proved by taking " rooted product " of " 𝒢 ∞ \mathcal{G}_{\infty} for columns" and " 𝒢 ∞ \mathcal{G}_{\infty} for rows". In that case, first we have to traverse a vertical path of length k k, then a horizontal path of length l l to obtain the first column and the last row of the subword in that order. Finding the other rows can be done similar to the process explained in the proof.

###### Remark 4.

Since we constructed 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty} as the " rooted product " of " 𝒢 ∞ \mathcal{G}_{\infty} for rows" by " 𝒢 ∞ \mathcal{G}_{\infty} for columns", we will always use a horizontal edge (an edge of 𝒢 ∞ \mathcal{G}_{\infty} for rows) at first. Also, as l ≥ 1 l\geq 1, we will never use the copy of 𝒢 ∞ \mathcal{G}_{\infty} for columns rooted at ( 0, 0) (0,0). Hence we can remove this redundant copy from 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty} and can still entitle the new graph 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}.

###### Remark 5.

The D ​ A ​ W ​ G DAWG also can be constructed by a similar methodology as given in [26]. Let

 | f r ​ o ​ w, ∞ = D ​ C ​ D ​ D ​ C ​ D ​ C ​ D ​ … = f r ​ o ​ w, ∞ ​ ( 1, 2, 3, …), f_{row,\infty}=DCDDCDCD\ldots=f_{row,\infty}(1,2,3,\ldots), |  |

 | f c ​ o ​ l, ∞ = D ′ ​ B ​ D ′ ​ D ′ ​ B ​ D ′ ​ B ​ D ′ ​ … = f c ​ o ​ l, ∞ ​ ( 1, 2, 3, …) f_{col,\infty}=D^{\prime}BD^{\prime}D^{\prime}BD^{\prime}BD^{\prime}\ldots=f_{col,\infty}(1,2,3,\ldots) |  |

where D, C, D ′ D,C,D^{\prime} and B B are as defined earlier. The nodes of 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty} are all non-negative integer pairs, ( i, j), i, j ≥ 0 (i,j),i,j\geq 0.

For j > 0 j>0, with F ⁡ ( j) F(j) being the j t ​ h j^{th} Fibonacci number, the labelled edges of 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty} are

 | ( 0, j − 1) → f r ​ o ​ w, ∞ ​ ( j) ( 0, j), ( 0, F ⁡ ( j) − 2) → 𝑠 ( 0, F ⁡ ( j + 1) − 1) \displaystyle(0,j-1)\xrightarrow{f_{row,\infty}(j)}(0,j),\quad(0,F(j)-2)\;\xrightarrow{\;s\;}\;(0,F(j+1)-1) |  |

where s = D s=D whenever j j is even and s = C s=C whenever j j is odd, and

for each j ≥ 0 j\geq 0 ( j ≥ 1 j\geq 1 is suffice; refer Remark 4) and i > 0 i>0,

 | ( i − 1, j) → f c ​ o ​ l, ∞ ​ ( i) ( i, j), ( F ⁡ ( i) − 2, j) → 𝑠 ( F ⁡ ( i + 1) − 1, j) \displaystyle(i-1,j)\xrightarrow{f_{col,\infty}(i)}(i,j),\quad(F(i)-2,j)\;\xrightarrow{\;s\;}\;(F(i+1)-1,j) |  |

where s = D ′ s=D^{\prime} whenever i i is even and s = B s=B whenever i i is odd.

###### Corollary 1.

For k, l ≥ 1 k,l\geq 1, there are ( k + 1) ​ ( l + 1) (k+1)(l+1) subwords of size ( k, l) (k,l) in f ∞, ∞ f_{\infty,\infty}.

###### Proof.

As the graph " 𝒢 ∞ \mathcal{G}_{\infty} for rows " is the D ​ A ​ W ​ G DAWG of the 1 ​ D 1D Fibonacci word D ​ C ​ D ​ D ​ C ​ … DCDDC\ldots, there are ( l + 1) (l+1) horizontal paths in 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty} [26]. Since the graph " 𝒢 ∞ \mathcal{G}_{\infty} for columns " is the D ​ A ​ W ​ G DAWG of the 1 ​ D 1D Fibonacci word D ′ ​ B ​ D ′ ​ D ′ ​ B ​ … D^{\prime}BD^{\prime}D^{\prime}B\ldots, from the last node of every horizontal path of 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}, there are ( k + 1) (k+1) vertical paths available for traversing. Note that, though paths with labels from { D, C } \{D,C\} and { D ′, B } \{D^{\prime},B\} have two possibilities, due to the condition on s j ​ o ​ i ​ n ​ t s_{joint} (as explained in the proof of Theorem 1), only one path with labels { a, b, c, d } \{a,b,c,d\} will materialize. Thus, there are ( k + 1) ​ ( l + 1) (k+1)(l+1) paths of length k + l k+l, comprising of a horizontal path of length l l and a vertical path of length k k. Now, by Theorem 1, a path of length k + l k+l in 𝒢 ∞, ∞ \mathcal{G}_{\infty,\infty}, comprising of a horizontal path of length l l and a vertical path of length k k, uniquely corresponds to a subword of size ( k, l) (k,l) of f ∞, ∞ f_{\infty,\infty}. Hence the corollary. ∎

The following example will explain the construction used in the proof of Theorem 1.

###### Example 1.

Let k = 2 k=2 and l = 2 l=2 so that all the subwords of size ( 2, 2) (2,2) will be obtained. By corollary 1, there will be 9 9 subwords of this size. Construction of one of these 9 subwords is explained here.

The horizontal paths of length 2 2 in D ​ C ​ D ​ D ​ C ​ … DCDDC\ldots are D ​ C, D ​ D DC,DD and C ​ D CD. Suppose we select d d for D D. Then H H can be any one of { d ​ c, d ​ d, c ​ d } \{dc,dd,cd\}. Let us choose H H as c ​ d cd.

Now the vertical paths of length 2 2 in D ′ ​ B ​ D ′ ​ D ′ ​ B ​ … D^{\prime}BD^{\prime}D^{\prime}B\ldots are D ′ B, D ′ D ′ \begin{matrix}D^{\prime}\\ B\end{matrix},\;\begin{matrix}D^{\prime}\\ D^{\prime}\end{matrix} and B D ′ \begin{matrix}B\\ D^{\prime}\end{matrix}. Since s j ​ o ​ i ​ n ​ t s_{joint} = d d, to have a subword of f ∞, ∞ f_{\infty,\infty}, the vertical path of length 2 should start with d d. By selecting d d for D ′ D^{\prime} we have the three vertical paths { d b, d d, b d } \left\{\begin{matrix}d\\ b\end{matrix},\begin{matrix}d\\ d\end{matrix},\begin{matrix}b\\ d\end{matrix}\right\}.

Let us take V = d b V=\begin{matrix}d\\ b\end{matrix}. Then the first column and the last row of the subword are fixed. The incomplete subword is, c d ∗ b \begin{matrix}c&d\\ *&b\end{matrix}, where the symbol ’ ∗ *’ denotes the entry therein is unknown yet.

Since s j ​ o ​ i ​ n ​ t = d s_{joint}=d and the letter in the second row of V V is not a d d, we fill the second row with H ′′ = a ​ b H^{\prime\prime}=ab. Hence the subword corresponding to this path is c d a b \begin{matrix}c&d\\ a&b\end{matrix}.

All the possible 9 cases of H H, V V and their corresponding subwords are listed in Tab. 1.

Table 1: All the factors of size ( 2, 2) (2,2) of f ∞, ∞ f_{\infty,\infty}

H d ​ c dc d ​ c dc d ​ d dd d ​ d dd c ​ d cd c ​ d cd b ​ a ba b ​ b bb a ​ b ab V c a \begin{matrix}c\\ a\end{matrix} c c \begin{matrix}c\\ c\end{matrix} d b \begin{matrix}d\\ b\end{matrix} d d \begin{matrix}d\\ d\end{matrix} d b \begin{matrix}d\\ b\end{matrix} d d \begin{matrix}d\\ d\end{matrix} a c \begin{matrix}a\\ c\end{matrix} b d \begin{matrix}b\\ d\end{matrix} b d \begin{matrix}b\\ d\end{matrix} Incomplete d c ∗ a \begin{matrix}d&c\\ *&a\end{matrix} d c ∗ c \begin{matrix}d&c\\ *&c\end{matrix} d d ∗ b \begin{matrix}d&d\\ *&b\end{matrix} d d ∗ d \begin{matrix}d&d\\ *&d\end{matrix} c d ∗ b \begin{matrix}c&d\\ *&b\end{matrix} c d ∗ d \begin{matrix}c&d\\ *&d\end{matrix} b a ∗ c \begin{matrix}b&a\\ *&c\end{matrix} b b ∗ d \begin{matrix}b&b\\ *&d\end{matrix} a b ∗ d \begin{matrix}a&b\\ *&d\end{matrix} Subword Complete d c b a \begin{matrix}d&c\\ b&a\end{matrix} d c d c \begin{matrix}d&c\\ d&c\end{matrix} d d b b \begin{matrix}d&d\\ b&b\end{matrix} d d d d \begin{matrix}d&d\\ d&d\end{matrix} c d a b \begin{matrix}c&d\\ a&b\end{matrix} c d c d \begin{matrix}c&d\\ c&d\end{matrix} b a d c \begin{matrix}b&a\\ d&c\end{matrix} b b d d \begin{matrix}b&b\\ d&d\end{matrix} a b c d \begin{matrix}a&b\\ c&d\end{matrix} Subword

## 4 Enumeration by Conjugation

For a given k k, let n n be the smallest integer such that 1 ≤ k < F ⁡ ( n) 1\leq k<F(n), where F ⁡ ( n) F(n) is the n t ​ h n^{th} Fibonacci number. In this section we use the method described in [10], wherein it is proved that the prefixes of length k k of the conjugates of a "special" conjugate of f n f_{n} are the subwords of length k k of f ∞ f_{\infty}. The Lemma is recalled here.

With Σ \Sigma, an alphabet, define the operator T T on Σ + \Sigma^{+} as follows. For a word w = a 1 ​ a 2 ​ … ​ a n ∈ Σ + w=a_{1}a_{2}\ldots a_{n}\in\Sigma^{+}, T ⁡ ( a 1 ​ a 2 ​ … ​ a n − 1 ​ a n) = a 2 ​ … ​ a n − 1 ​ a n ​ a 1 T(a_{1}a_{2}\ldots a_{n-1}a_{n})=a_{2}\ldots a_{n-1}a_{n}a_{1} and T − 1 ​ ( a 1 ​ a 2 ​ … ​ a n − 1 ​ a n) = a n ​ a 1 ​ a 2 ​ … ​ a n − 1 T^{-1}(a_{1}a_{2}\ldots a_{n-1}a_{n})=a_{n}a_{1}a_{2}\ldots a_{n-1}. Higher powers of T T are defined iteratively. That is, T p ​ ( w) = T ⁡ ( T p − 1 ​ ( w)) T^{p}(w)=T(T^{p-1}(w)) and T − p ​ ( w) = T − 1 ​ ( T − ( p − 1) ​ ( w)) T^{-p}(w)=T^{-1}(T^{-(p-1)}(w)).

###### Lemma 2.

[10] Let f 0 = a, f 1 = b, f n = f n − 1 ​ f n − 2, n ≥ 2 f_{0}=a,f_{1}=b,f_{n}=f_{n-1}f_{n-2},n\geq 2 be the sequence of Fibonacci words. Let F ⁡ ( n) = | f n | F(n)=|f_{n}| and let

 | q n = { T F ⁡ ( n) − 1 ​ ( f n) if n is even T F ⁡ ( n − 1) − 1 ​ ( f n) if n is odd. q_{n}=\begin{cases}T^{F(n)-1}(f_{n})&\text{if n is even}\\ T^{F(n-1)-1}(f_{n})&\text{if n is odd}.\end{cases} |  |

Then for each k k with 1 ≤ k < F ⁡ ( n) 1\leq k<F(n), the k + 1 k+1 prefixes of T 0 ​ ( q n), T − 1 ​ ( q n), …, T − k ​ ( q n) T^{0}(q_{n}),T^{-1}(q_{n}),\ldots,T^{-k}(q_{n}) having length k k are the k + 1 k+1 distinct factors of f ∞ f_{\infty} of length k k.

###### Example 2.

Let f ∞ = a ​ b ​ a ​ a ​ b ​ … f_{\infty}=abaab\ldots. For k = 4 k=4, n n will be 4 4, as 4 < F ⁡ ( 4) 4<F(4). So, f n = f 4 = a ​ b ​ a ​ a ​ b f_{n}=f_{4}=abaab. With F ⁡ ( 4) = 5, F ⁡ ( 3) = 3 F(4)=5,F(3)=3, we have q 4 = T 4 ​ ( a ​ b ​ a ​ a ​ b) = b ​ a ​ b ​ a ​ a q_{4}=T^{4}(abaab)=babaa, is the special conjugate of f 4 f_{4}.

Now, T 0 ​ ( q 4), T − 1 ​ ( q 4), T − 2 ​ ( q 4), T − 3 ​ ( q 4), T − 4 ​ ( q 4) T^{0}(q_{4}),T^{-1}(q_{4}),T^{-2}(q_{4}),T^{-3}(q_{4}),T^{-4}(q_{4}) are b ​ a ​ b ​ a ​ a babaa, a ​ b ​ a ​ b ​ a ababa, a ​ a ​ b ​ a ​ b aabab, b ​ a ​ a ​ b ​ a baaba, a ​ b ​ a ​ a ​ b abaab respectively and the subwords of f ∞ f_{\infty} of length 4 are b ​ a ​ b ​ a, a ​ b ​ a ​ b, a ​ a ​ b ​ a, b ​ a ​ a ​ b, a ​ b ​ a ​ a baba,abab,aaba,baab,abaa.

Similar to the operators T T and T − 1 T^{-1}, we define four operators on 2 ​ D 2D words.

###### Definition 6.

Let r 1, r 2, ⋯, r m r_{1},r_{2},\cdots,r_{m} and c 1, c 2, ⋯, c n c_{1},c_{2},\cdots,c_{n} be the m m rows and the n n columns of a 2 ​ D 2D word w w of size ( m, n) (m,n). Then the operations T c ​ o ​ l ​ ( w) T_{col}(w), T c ​ o ​ l − 1 ​ ( w) T^{-1}_{col}(w), T r ​ o ​ w ​ ( w) T_{row}(w) and T r ​ o ​ w − 1 ​ ( w) T^{-1}_{row}(w) are defined as below.

 | T c ​ o ​ l ​ ( w) \displaystyle T_{col}(w) | = c 2 ⦶ c 3 ⦶ ⋯ ⦶ c n ⦶ c 1 \displaystyle=c_{2}\obar c_{3}\obar\cdots\obar c_{n}\obar c_{1} |  |

 | T c ​ o ​ l − 1 ​ ( w) \displaystyle T^{-1}_{col}(w) | = c n ⦶ c 1 ⦶ c 2 ⦶ ⋯ ⦶ c n − 2 ⦶ c n − 1 \displaystyle=c_{n}\obar c_{1}\obar c_{2}\obar\cdots\obar c_{n-2}\obar c_{n-1} |  |

 | T r ​ o ​ w ​ ( w) \displaystyle T_{row}(w) | = r 2 ⊖ r 3 ⊖ ⋯ ⊖ r m ⊖ r 1 \displaystyle=r_{2}\ominus r_{3}\ominus\cdots\ominus r_{m}\ominus r_{1} |  |

 | T r ​ o ​ w − 1 ​ ( w) \displaystyle T^{-1}_{row}(w) | = r n ⊖ r 1 ⊖ r 2 ⊖ ⋯ ⊖ r n − 2 ⊖ r n − 1. \displaystyle=r_{n}\ominus r_{1}\ominus r_{2}\ominus\cdots\ominus r_{n-2}\ominus r_{n-1}. |  |

Higher powers of T c ​ o ​ l ​ ( w) T_{col}(w), T c ​ o ​ l − 1 ​ ( w) T^{-1}_{col}(w), T r ​ o ​ w ​ ( w) T_{row}(w) and T r ​ o ​ w − 1 ​ ( w) T^{-1}_{row}(w) are defined iteratively. For example, with s ≥ 1 s\geq 1, T c ​ o ​ l s ​ ( w) = T c ​ o ​ l ​ ( T c ​ o ​ l s − 1 ​ ( w)) T^{s}_{col}(w)=T_{col}(T^{s-1}_{col}(w)).

Through these operators we define the conjucacy class of a 2 ​ D 2D word w w.

###### Definition 7.

Let w w be a 2 ​ D 2D word of size ( m, n) (m,n). Then

 | C ​ o ​ n ​ j ​ ( w) \displaystyle Conj(w) | = { T r ​ o ​ w i T c ​ o ​ l j ( w), 0 ≤ i ≤ m − 1, 0 ≤ j ≤ n − 1 } \displaystyle=\left\{T_{row}^{i}T_{col}^{j}(w),0\leq i\leq m-1,0\leq j\leq n-1\right\} |  |

 |  | = { T c ​ o ​ l j T r ​ o ​ w i ( w), 0 ≤ j ≤ n − 1, 0 ≤ i ≤ m − 1 } \displaystyle=\left\{T_{col}^{j}T_{row}^{i}(w),0\leq j\leq n-1,0\leq i\leq m-1\right\} |  |

is called the Conjugacy Class of w w.

Since 0 ≤ i ≤ m − 1 0\leq i\leq m-1 and 0 ≤ j ≤ n − 1 0\leq j\leq n-1, it is easy to see that the number of conjugates of w w can be at the maximum m ​ n mn. Note that, if no two rows of w w are conjugates of each other and if no two columns of w w are conjugates of each other, then the maximum possible value of m ​ n mn will be achieved by | C ​ o ​ n ​ j ​ ( w) | |Conj(w)|.

Now, we will enumerate the subwords of size ( k, l) (k,l) of f ∞, ∞ f_{\infty,\infty} using the conjugates of a "special" conjugate of f m, n f_{m,n} ( m, n ≥ 3 m,n\geq 3 and depend on k, l k,l).

###### Theorem 2.

Let F ( 0) = F ( 1) = 1, F ( 2) = 2, F ( 3) = 3, F ( 4) = 5, … F(0)=F(1)=1,F(2)=2,F(3)=3,F(4)=5,\ldots be the sequence of Fibonacci numbers. For a given k, l ≥ 1 k,l\geq 1, consider the 2 ​ D 2D finite Fibonacci word f m, n f_{m,n}, where m m, n n are the smallest integers such that k < F ⁡ ( m) k<F(m) and l < F ⁡ ( n) l<F(n). Let

 | q m, n = { T r ​ o ​ w F ⁡ ( m) − 1 ​ ( T c ​ o ​ l F ⁡ ( n) − 1 ​ ( f m, n)) if m is even and n is even T r ​ o ​ w F ⁡ ( m) − 1 ​ ( T c ​ o ​ l F ⁡ ( n − 1) − 1 ​ ( f m, n)) if m is even and n is odd T r ​ o ​ w F ⁡ ( m − 1) − 1 ​ ( T c ​ o ​ l F ⁡ ( n) − 1 ​ ( f m, n)) if m is odd and n is even T r ​ o ​ w F ⁡ ( m − 1) − 1 ​ ( T c ​ o ​ l F ⁡ ( n − 1) − 1 ​ ( f m, n)) if m is odd and n is odd q_{m,n}=\begin{cases}T_{row}^{F(m)-1}\left(T_{col}^{F(n)-1}(f_{m,n})\right)&\text{if m is even and n is even}\\ T_{row}^{F(m)-1}\left(T_{col}^{F(n-1)-1}(f_{m,n})\right)&\text{if m is even and n is odd}\\ T_{row}^{F(m-1)-1}\left(T_{col}^{F(n)-1}(f_{m,n})\right)&\text{if m is odd and n is even}\\ T_{row}^{F(m-1)-1}\left(T_{col}^{F(n-1)-1}(f_{m,n})\right)&\text{if m is odd and n is odd}\end{cases} |  |

Then for each k k with 1 ≤ k < F ⁡ ( m) 1\leq k<F(m) and for each l l with 1 ≤ l < F ⁡ ( n) 1\leq l<F(n), the ( k + 1) ​ ( l + 1) (k+1)(l+1) prefixes of

T r ​ o ​ w 0 ​ T c ​ o ​ l 0 ​ ( q m, n), T r ​ o ​ w 0 ​ T c ​ o ​ l − 1 ​ ( q m, n), … ​ …, T r ​ o ​ w 0 ​ T c ​ o ​ l − l ​ ( q m, n) T^{0}_{row}T^{0}_{col}(q_{m,n}),T^{0}_{row}T^{-1}_{col}(q_{m,n}),\ldots\>\dots,\>T^{0}_{row}T^{-l}_{col}(q_{m,n}), |

T r ​ o ​ w − 1 ​ T c ​ o ​ l 0 ​ ( q m, n), T r ​ o ​ w − 1 ​ T c ​ o ​ l − 1 ​ ( q m, n), … ​ …, T r ​ o ​ w − 1 ​ T c ​ o ​ l − l ​ ( q m, n) T^{-1}_{row}T^{0}_{col}(q_{m,n}),T^{-1}_{row}T^{-1}_{col}(q_{m,n}),\ldots\>\dots,\>T^{-1}_{row}T^{-l}_{col}(q_{m,n}), |

⋯ ⋯ ⋯ \cdots\quad\cdots\quad\cdots |

⋯ ⋯ ⋯ \cdots\quad\cdots\quad\cdots |

T r ​ o ​ w − k ​ T c ​ o ​ l 0 ​ ( q m, n), T r ​ o ​ w − k ​ T c ​ o ​ l − 1 ​ ( q m, n), … ​ …, T r ​ o ​ w − k ​ T c ​ o ​ l − l ​ ( q m, n) T^{-k}_{row}T^{0}_{col}(q_{m,n}),T^{-k}_{row}T^{-1}_{col}(q_{m,n}),\ldots\>\ldots,\>T^{-k}_{row}T^{-l}_{col}(q_{m,n}) |

having size ( k, l) (k,l) are the ( k + 1) ​ ( l + 1) (k+1)(l+1) distinct factors of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l).

###### Proof.

Suppose that we want to find all the subwords of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l). Let F ( 0) = F ( 1) = 1, F ( 2) = 2, F ( 3) = 3, F ( 4) = 5, … F(0)=F(1)=1,F(2)=2,F(3)=3,F(4)=5,\ldots be the sequence of Fibonacci numbers. Consider the 2 ​ D 2D finite Fibonacci word f m, n f_{m,n} where m m and n n are such that k < F ⁡ ( m) k<F(m) and l < F ⁡ ( n) l<F(n). Note that f m, n f_{m,n} will be of size ( F ⁡ ( m), F ⁡ ( n) F(m),F(n)) [22].

We prove the theorem for the case where both m m and n n are even. The proofs of other cases are similar.

Denote the columns of f m, n f_{m,n} by C 1, C 2, …, C F ⁡ ( n) C_{1},C_{2},\ldots,C_{F(n)}. Since there are only two distinct columns (refer Lemma 1), let us symbolize the columns over { b, d } \{b,d\} by D D and the columns over { a, c } \{a,c\} by C C. As every row of f m, n f_{m,n} is a Fibonacci word of size F ⁡ ( n) F(n), the two distinct columns are indeed arranged in a Fibonacci pattern in f m, n f_{m,n}. That is, the symbolized word for f m, n = C 1 ⦶ C 2 ⦶ … ⦶ C F ⁡ ( n) = D ​ C ​ D ​ D ​ C ​ … ​ D ​ C = H n f_{m,n}=C_{1}\obar C_{2}\obar\ldots\obar C_{F(n)}=DCDDC\ldots DC=H_{n}, say, is a Fibonacci word of size F ⁡ ( n) F(n). Since n n is even, the suffix of length 2 of H n H_{n} will be D ​ C DC. Now by Lemma 2, the prefixes of length l l of the conjugates of T F ⁡ ( n) − 1 ​ ( H n) = q n ′ T^{F(n)-1}(H_{n})=q_{n}^{\prime} (say), are the subwords of length l l of H n H_{n}. We now replace the symbols D D and C C occurring in q n ′ q_{n}^{\prime} by the original columns to get the 2 ​ D 2D word q n q_{n}. What we have proved is that, we can arrange the columns of f m, n f_{m,n} in a way that we can obtain all the subwords of length l l of the infinite Fibonacci words occupying the rows of f m, n f_{m,n} through the conjugates of q n q_{n}.

Now, let us denote the rows of q n q_{n} by R 1, R 2, …, R F ⁡ ( m) R_{1},R_{2},\ldots,R_{F(m)}. By symbolizing the rows over { d, c } \{d,c\} as D ′ D^{\prime} and { a, b } \{a,b\} as B B, we get V m V_{m}, the symbolized word of q n q_{n} over { D ′, B } \{D^{\prime},B\} as V m = R 1 ⊖ R 2 ⊖ … ⊖ R F ⁡ ( m) = D ′ ​ B ​ D ′ ​ D ′ ​ B ​ … ​ D ′ ​ B V_{m}=R_{1}\ominus R_{2}\ominus\ldots\ominus R_{F(m)}=D^{\prime}BD^{\prime}D^{\prime}B\ldots D^{\prime}B. Following a similar argument as above, we get a word q m ′ = T F ⁡ ( m) − 1 ​ ( V m) q_{m}^{\prime}=T^{F(m)-1}(V_{m}) over { D ′, B } \{D^{\prime},B\}. We can now replace the symbols occurring in q m ′ q_{m}^{\prime} to get the 2 ​ D 2D word q m, n q_{m,n}. What we have proved is that, we can arrange the rows of q n q_{n} in a way that we can get all the subwords of length k k of the infinite Fibonacci words occupying the columns of f m, n f_{m,n} through the conjugates of q m, n q_{m,n}.

Note that q m, n q_{m,n} is a conjugate of f m, n f_{m,n}. In fact, by the two stage process, what we have obtained as q m, n q_{m,n} is nothing but T r ​ o ​ w F ⁡ ( m) − 1 ​ ( T c ​ o ​ l F ⁡ ( n) − 1 ​ ( f m, n)) T_{row}^{F(m)-1}\left(T_{col}^{F(n)-1}(f_{m,n})\right). As assured by Lemma 2, the rows and columns of q m, n q_{m,n} are arranged in such a way that, for each 0 ≤ i ≤ k 0\leq i\leq k, 0 ≤ j ≤ l 0\leq j\leq l, the prefixes of length k k of the first columns and the prefixes of length l l of the first rows of T r ​ o ​ w i ​ T c ​ o ​ l j ​ ( q m, n) T^{i}_{row}T^{j}_{col}(q_{m,n}), produces ( k + 1) ​ ( l + 1) (k+1)(l+1) distinct F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} s. We can call q m, n q_{m,n} a "special" conjugate of f m, n f_{m,n}, in this context. Since in each of these F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} s, F ​ R ​ A ​ M ​ E L FRAME_{L} s are subwords of f ∞ d, b f_{\infty}^{d,b} or f ∞ c, a f_{\infty}^{c,a}, and F ​ R ​ A ​ M ​ E T FRAME_{T} s are subwords of f ∞ d, c f_{\infty}^{d,c} or f ∞ b, a f_{\infty}^{b,a}, by Lemma 3 we get ( k + 1) ​ ( l + 1) (k+1)(l+1) distinct subwords of f ∞, ∞ f_{\infty,\infty}. ∎

Let us understand the enumeration of the subwords through an example.

###### Example 3.

Let k = 2 k=2, l = 2 l=2. That is, we wish to find all the ( 2, 2) (2,2) -subwords of f ∞, ∞ f_{\infty,\infty}. As k k and l l are less than F ⁡ ( 3) = 3 F(3)=3, m = n = 3 m=n=3 and we consider

 | f 3, 3 = d c d b a b d c d. \displaystyle f_{3,3}=\begin{matrix}d&c&d\\ b&a&b\\ d&c&d\end{matrix}. |  |

Then, as both m m and n n are odd, q 3, 3 = T r ​ o ​ w 2 − 1 ​ ( T c ​ o ​ l 2 − 1 ​ ( f 3, 3)) = f 3, 3 = a b b c d d c d d. q_{3,3}=T_{row}^{2-1}\left(T_{col}^{2-1}(f_{3,3})\right)=f_{3,3}=\begin{matrix}a&b&b\\ c&d&d\\ c&d&d\end{matrix}.

As mentioned earlier q 3, 3 q_{3,3} is a "special" conjugate of f 3, 3 f_{3,3}. Since no two rows(columns) of q 3, 3 q_{3,3} are conjugates of each other, q 3, 3 q_{3,3} has 9 9 distinct conjugates. All the 9 9 conjugates and their corresponding subwords of size ( 2, 2) (2,2) of f ∞, ∞ f_{\infty,\infty} are listed in Table 2.

Table 2: Conjugates of q 3, 3 q_{3,3} and the subwords of size ( 2, 2) (2,2) of f ∞, ∞ f_{\infty,\infty}

𝑻 𝒓 ​ 𝒐 ​ 𝒘 𝒊 ​ ( 𝑻 𝒄 ​ 𝒐 ​ 𝒍 𝒋 ​ ( 𝒒 𝟑, 𝟑)) T_{row}^{i}(T_{col}^{j}(q_{3,3})) Conjugate of q 3, 3 q_{3,3} Subword T r ​ o ​ w 0 ​ ( T c ​ o ​ l 0 ​ ( q 3, 3)) T_{row}^{0}(T_{col}^{0}(q_{3,3})) a b b c d d c d d \begin{matrix}a&b&b\\ c&d&d\\ c&d&d\end{matrix} a b c d \begin{matrix}a&b\\ c&d\end{matrix} T r ​ o ​ w 0 ​ ( T c ​ o ​ l − 1 ​ ( q 3, 3)) T_{row}^{0}(T_{col}^{-1}(q_{3,3})) b a b d c d d c d \begin{matrix}b&a&b\\ d&c&d\\ d&c&d\end{matrix} b a d c \begin{matrix}b&a\\ d&c\end{matrix} T r ​ o ​ w 0 ​ ( T c ​ o ​ l − 2 ​ ( q 3, 3)) T_{row}^{0}(T_{col}^{-2}(q_{3,3})) b b a d d c d d c \begin{matrix}b&b&a\\ d&d&c\\ d&d&c\end{matrix} b b d d \begin{matrix}b&b\\ d&d\end{matrix} T r ​ o ​ w − 1 ​ ( T c ​ o ​ l 0 ​ ( q 3, 3)) T_{row}^{-1}(T_{col}^{0}(q_{3,3})) c d d a b b c d d \begin{matrix}c&d&d\\ a&b&b\\ c&d&d\end{matrix} c d a b \begin{matrix}c&d\\ a&b\end{matrix} T r ​ o ​ w − 1 ​ ( T c ​ o ​ l − 1 ​ ( q 3, 3)) T_{row}^{-1}(T_{col}^{-1}(q_{3,3})) d c d b a b d c d \begin{matrix}d&c&d\\ b&a&b\\ d&c&d\end{matrix} d c b a \begin{matrix}d&c\\ b&a\end{matrix} T r ​ o ​ w − 1 ​ ( T c ​ o ​ l − 2 ​ ( q 3, 3)) T_{row}^{-1}(T_{col}^{-2}(q_{3,3})) d d c b b a d d c \begin{matrix}d&d&c\\ b&b&a\\ d&d&c\par\end{matrix} d d b b \begin{matrix}d&d\\ b&b\end{matrix} T r ​ o ​ w − 2 ​ ( T c ​ o ​ l 0 ​ ( q 3, 3)) T_{row}^{-2}(T_{col}^{0}(q_{3,3})) c d d c d d a b b \begin{matrix}c&d&d\\ c&d&d\\ a&b&b\par\end{matrix} c d c d \begin{matrix}c&d\\ c&d\end{matrix} T r ​ o ​ w − 2 ​ ( T c ​ o ​ l − 1 ​ ( q 3, 3)) T_{row}^{-2}(T_{col}^{-1}(q_{3,3})) d c d d c d b a b \begin{matrix}d&c&d\\ d&c&d\\ b&a&b\par\end{matrix} d c d c \begin{matrix}d&c\\ d&c\end{matrix} T r ​ o ​ w − 2 ​ ( T c ​ o ​ l − 2 ​ ( q 3, 3)) T_{row}^{-2}(T_{col}^{-2}(q_{3,3})) d d c d d c b b a \begin{matrix}d&d&c\\ d&d&c\\ b&b&a\end{matrix} d d d d \begin{matrix}d&d\\ d&d\end{matrix}

In [10], apart from the sophisticated way of obtaining the subwords of f ∞ f_{\infty}, described in Lemma 2, the author provides another simple way of obtaining the subwords of length k k.

###### Proposition 1.

[10] Let n ≥ 2 n\geq 2 and F ⁡ ( n) ≤ k < F ⁡ ( n + 1) F(n)\leq k<F(n+1). Then, the prefixes of length k k of T i ​ ( f n + 1) T^{i}(f_{n+1}), i ∈ { 0, 1, …, F ⁡ ( n) − 1 } ∪ i\in\{0,1,\ldots,F(n)-1\}\cup { F ⁡ ( n + 2) − k − 1, F ⁡ ( n + 2) − k, …, F ⁡ ( n + 1) − 1 } \{F(n+2)-k-1,F(n+2)-k,\ldots,F(n+1)-1\}, are the k + 1 k+1 distinct factors of f ∞ f_{\infty} of length k k.

Proposition 1 is extended to f ∞, ∞ f_{\infty,\infty} as below.

###### Proposition 2.

Let m, n ≥ 2 m,n\geq 2 and F ⁡ ( m) ≤ k < F ⁡ ( m + 1) F(m)\leq k<F(m+1), F ⁡ ( n) ≤ l < F ⁡ ( n + 1) F(n)\leq l<F(n+1). Then the ( k + 1) ​ ( l + 1) (k+1)(l+1) prefixes of T r ​ o ​ w i ​ ( T c ​ o ​ l j ​ ( f m + 1, n + 1)) T_{row}^{i}(T_{col}^{j}(f_{m+1,n+1})) of size ( k, l) (k,l), where i ∈ { 0, 1, …, F ⁡ ( m) − 1 } ∪ { F ⁡ ( m + 2) − k − 1, F ⁡ ( m + 2) − k, …, F ⁡ ( m + 1) − 1 } i\in\{0,1,\ldots,F(m)-1\}\cup\{F(m+2)-k-1,F(m+2)-k,\ldots,F(m+1)-1\}, j ∈ { 0, 1, …, F ⁡ ( n) − 1 } ∪ { F ⁡ ( n + 2) − l − 1, F ⁡ ( n + 2) − l, …, F ⁡ ( n + 1) − 1 } j\in\{0,1,\ldots,F(n)-1\}\cup\{F(n+2)-l-1,F(n+2)-l,\ldots,F(n+1)-1\}, are the ( k + 1) ​ ( l + 1) (k+1)(l+1) distinct factors of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l).

###### Proof.

For m, n ≥ 2 m,n\geq 2, consider the 2 ​ D 2D finite Fibonacci word f m + 1, n + 1 f_{m+1,n+1}. Recall that the columns and rows of f m + 1, n + 1 f_{m+1,n+1} are 1 ​ D 1D finite Fibonacci words (in fact, they are f m + 1 d, b f_{m+1}^{d,b} or f m + 1 c, a f_{m+1}^{c,a}, and f n + 1 d, c f_{n+1}^{d,c} or f n + 1 b, a f_{n+1}^{b,a}). Hence, the F ​ R ​ A ​ M ​ E L FRAME_{L} s and F ​ R ​ A ​ M ​ E T FRAME_{T} s of the ( k + 1) ​ ( l + 1) (k+1)(l+1) F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} s obtained from the conjugates T r ​ o ​ w i ​ ( T c ​ o ​ l j ​ ( f m + 1, n + 1)) T_{row}^{i}(T_{col}^{j}(f_{m+1,n+1})), i ∈ { 0, 1, …, F ⁡ ( m) − 1 } ∪ { F ⁡ ( m + 2) − k − 1, F ⁡ ( m + 2) − k, …, F ⁡ ( m + 1) − 1 } i\in\{0,1,\ldots,F(m)-1\}\cup\{F(m+2)-k-1,F(m+2)-k,\ldots,F(m+1)-1\}, j ∈ { 0, 1, …, F ⁡ ( n) − 1 } ∪ { F ⁡ ( n + 2) − l − 1, F ⁡ ( n + 2) − l, …, F ⁡ ( n + 1) − 1 } j\in\{0,1,\ldots,F(n)-1\}\cup\{F(n+2)-l-1,F(n+2)-l,\ldots,F(n+1)-1\} are nothing but the ( k + 1) ​ ( l + 1) (k+1)(l+1) appropriate combinations of vertical factors of length k k and horizontal factors of length l l of the infinite Fibonacci words occurring in the columns and in the rows of f ∞, ∞ f_{\infty,\infty}. Since all these F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} s are taken from the prefixes of f ∞, ∞ f_{\infty,\infty}, the subword constructed from these F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} s (refer Lemma 3) will be obviously prefixes of f ∞, ∞ f_{\infty,\infty}. Hence, the prefixes of size ( k, l) (k,l) of T r ​ o ​ w i ​ ( T c ​ o ​ l j ​ ( f m + 1, n + 1)) T_{row}^{i}(T_{col}^{j}(f_{m+1,n+1})) for the stated values of i, j i,j are the factors of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l). ∎

## 5 Locating the Factors of f ∞, ∞ f_{\infty,\infty}

In the previous sections, we developed two methods for listing all the ( k + 1) ​ ( l + 1) (k+1)(l+1) factors of size ( k, l) (k,l) of f ∞, ∞ f_{\infty,\infty}. In this section we will locate (find the exact positions { ( i, j), i, j ≥ 1 } \{(i,j),i,j\geq 1\} of) these factors in the domain of f ∞, ∞ f_{\infty,\infty}. We know that since there are only k + 1 k+1 factors of length k k in f ∞ f_{\infty}, there are many repetitions of every factor in f ∞ f_{\infty} [3]. As the rows and columns of f ∞, ∞ f_{\infty,\infty} are composed of f ∞ f_{\infty}, the same happens in f ∞, ∞ f_{\infty,\infty} also.

For locating the factors of f ∞ f_{\infty}, the reader may either refer [10] or [26]. We recall some terminologies from [26] for our use.

Let f 0 = a, f 1 = a ​ b f_{0}=a,f_{1}=ab and for n ≥ 1, f n + 1 = f n ​ f n − 1 n\geq 1,f_{n+1}=f_{n}f_{n-1} so that f ∞ = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ … ​ … = f ∞ ​ ( 1, 2, 3, …) f_{\infty}=abaababaabaab\ldots\ldots=f_{\infty}(1,2,3,\ldots). Also, for n ≥ 0 n\geq 0 let F ⁡ ( n) = | f n | F(n)=|f_{n}| be the n t ​ h n^{th} Fibonacci number. For n ≥ 2 n\geq 2, let g n g_{n} be the n t ​ h n^{th} truncated Fibonacci word, the word obtained from f n f_{n} by removing its last two letters.

Let u u be a subword of f ∞ f_{\infty}. By an occurrence of u u we mean a i ≥ 0 i\geq 0 such that f ∞ ​ ( i + 1) ​ f ∞ ​ ( i + 2) ​ … ​ f ∞ ​ ( i + | u |) = u f_{\infty}(i+1)f_{\infty}(i+2)\dots f_{\infty}(i+|u|)=u. By first-occ( u u) we mean the least value of occurrence of u u and by occ( u u) we mean the set of all occurrences of u u in f ∞ f_{\infty}. Now, for a set of integers X X and for a j ≥ 0 j\geq 0, define the operator ⊞ \boxplus as, X ⊞ j = { x + j: x ∈ X } X\boxplus j=\{x+j:x\in X\}.

Recall that the Fibonacci number system represents a number as a sum of Fibonacci numbers such that no two consecutive Fibonacci numbers are used. Also, the sum of zero number of integers equals zero. This representation of any nonnegative integer n n, in the Fibonacci number system is called the Fibonacci representation of n n. For n ≥ 1 n\geq 1, let 𝒵 n \mathcal{Z}_{n} be the set of nonnegative integers which do not use Fibonacci numbers F ⁡ ( 0), F ⁡ ( 1), F ⁡ ( 2), …, F ⁡ ( n − 1) F(0),F(1),F(2),\ldots,F(n-1) in their Fibonacci representation. For example 𝒵 1 = { 0, 2, 3, 5, … } \mathcal{Z}_{1}=\{0,2,3,5,\ldots\} and 𝒵 2 = { 0, 3, 5, 8, 11, … } \mathcal{Z}_{2}=\{0,3,5,8,11,\ldots\}. Then, it is proved in [26] that,

 | occ ​ ( u) = o ​ c ​ c ​ ( g n) ⊞ first-occ ​ ( u), \textit{occ}(u)=occ(g_{n})\boxplus\textit{first-occ}(u), |  | (2) |

where n n is such that g n g_{n} is the shortest truncated Fibonacci word containing u u. Since for n ≥ 2 n\geq 2, occ ( g n + 1 g_{n+1}) = occ ( f n f_{n}) = 𝒵 n \mathcal{Z}_{n}, we have,

 | occ ​ ( u) = 𝒵 n − 1 ⊞ first-occ ​ ( u). \textit{occ}(u)=\mathcal{Z}_{n-1}\boxplus\textit{first-occ}(u). |  |

We also have that occ ( f 1 f_{1}) = occ ( f 2 f_{2}) and occ ( f 0 f_{0}) = 𝒵 1 =\mathcal{Z}_{1}.

###### Example 4.

Let us locate the positions of the factor u = a ​ b ​ a ​ b u=abab in f ∞ a, b f_{\infty}^{a,b}. We have first-occ( u u) = 3 3. Since u u occurs for the first time in g 5 g_{5}, we get n = 5 n=5 and hence occ( a ​ b ​ a ​ b abab) = 𝒵 4 ⊞ 3 = { 0, 8, 13, 21, 29, … } ⊞ 3 = { 3, 11, 16, 24, 32, … } \mathcal{Z}_{4}\boxplus 3=\{0,8,13,21,29,\ldots\}\boxplus 3=\{3,11,16,24,32,\ldots\}.

For locating the factors of f ∞, ∞ f_{\infty,\infty}, let us define a structure called " FRAME ".

###### Definition 8.

Let w w be a 2 ​ D 2D word. The structure obtained by considering only the first row, the first column, the last row and the last column of w w is called the FRAME of w w. In particular, the first row (first column, last row, and last column, respectively) is called F ​ R ​ A ​ M ​ E T FRAME_{T} ( F ​ R ​ A ​ M ​ E L FRAME_{L}, F ​ R ​ A ​ M ​ E B FRAME_{B}, and F ​ R ​ A ​ M ​ E R FRAME_{R}, respectively).

It is understood that by F ​ R ​ A ​ M ​ E T, F ​ R ​ A ​ M ​ E L, … FRAME_{T},FRAME_{L},\ldots, we refer to the words they contain. Extending Definition 8, we can have the substructures F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} (which consists of F ​ R ​ A ​ M ​ E T FRAME_{T} and F ​ R ​ A ​ M ​ E L FRAME_{L}), F ​ R ​ A ​ M ​ E T ​ R FRAME_{TR}, F ​ R ​ A ​ M ​ E L ​ B FRAME_{LB} and F ​ R ​ A ​ M ​ E R ​ B FRAME_{RB}. We will be predominantly using F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} only. Note that F ​ R ​ A ​ M ​ E T FRAME_{T} and F ​ R ​ A ​ M ​ E L FRAME_{L} share a common prefix of length one. We call this common symbol s j ​ o ​ i ​ n ​ t, T ​ L s_{joint,TL}. Similarly s j ​ o ​ i ​ n ​ t, T ​ R s_{joint,TR} is defined (Refer Fig. 4).

[image: Refer to caption] (a) F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL}

[image: Refer to caption] (b) F ​ R ​ A ​ M ​ E T ​ R FRAME_{TR}

Figure 4: Two of the four substructures of F ​ R ​ A ​ M ​ E FRAME

The following Lemma is inspired by the properties listed in Lemma 1. Note that there are only two distinct rows in f ∞, ∞ f_{\infty,\infty}. These distinct rows also are one and the same words except that their respective alphabets are different. Hence, given the entire first row and any one letter of another row R R, row R R can be written down with ease using a substitution rule.

###### Lemma 3.

Given F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} of a subword of f ∞, ∞ f_{\infty,\infty} with its F ​ R ​ A ​ M ​ E T FRAME_{T} being a subword of length l l of f ∞ a, b f_{\infty}^{a,b} or f ∞ c, d f_{\infty}^{c,d} and F ​ R ​ A ​ M ​ E L FRAME_{L} being a subword of length k k of f ∞ a, c f_{\infty}^{a,c} or f ∞ b, d f_{\infty}^{b,d}, we can construct the subword of size ( k, l) (k,l) of f ∞, ∞ f_{\infty,\infty} with that F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL}.

###### Proof.

Let u u be the 2 ​ D 2D word whose F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} is given. We will make use of the two substitution rules defined in the proof of Theorem 1 to get the factor u u of f ∞, ∞ f_{\infty,\infty}.

If F ​ R ​ A ​ M ​ E T FRAME_{T} is over { a, b } \{a,b\}, then define θ 1: θ 1 ​ ( a) = c, θ 1 ​ ( b) = d \theta_{1}:\theta_{1}(a)=c,\theta_{1}(b)=d. Now, for any row i i, 2 ≤ i ≤ k 2\leq i\leq k, of F ​ R ​ A ​ M ​ E L FRAME_{L}, if the letter present therein is s j ​ o ​ i ​ n ​ t, T ​ L s_{joint,TL}, the i t ​ h i^{th} row of u u is F ​ R ​ A ​ M ​ E T FRAME_{T} itself; else, the i t ​ h i^{th} row of u u is θ 1 ​ ( F ​ R ​ A ​ M ​ E T) \theta_{1}(\textit{$FRAME_{T}$}).

If F ​ R ​ A ​ M ​ E T FRAME_{T} is over { c, d } \{c,d\}, then define θ 2: θ 2 ​ ( c) = a, θ 2 ​ ( d) = b \theta_{2}:\theta_{2}(c)=a,\theta_{2}(d)=b. Now, for any row i i, 2 ≤ i ≤ k 2\leq i\leq k, of F ​ R ​ A ​ M ​ E L FRAME_{L}, if the letter present therein is s j ​ o ​ i ​ n ​ t, T ​ L s_{joint,TL}, the i t ​ h i^{th} row of u u is F ​ R ​ A ​ M ​ E T FRAME_{T} itself; else, the i t ​ h i^{th} row of u u is θ 2 ​ ( F ​ R ​ A ​ M ​ E T) \theta_{2}(\textit{$FRAME_{T}$}).

As mentioned in the proof of Theorem 1, the rows other than F ​ R ​ A ​ M ​ E T FRAME_{T} are constructed using F ​ R ​ A ​ M ​ E L FRAME_{L}. That is the alphabet of a particular row and the order in which the two distinct rows of the subword are arranged are decided by F ​ R ​ A ​ M ​ E L FRAME_{L}. Since F ​ R ​ A ​ M ​ E L FRAME_{L} is a subword of length l l of some column of f ∞, ∞ f_{\infty,\infty}, the obtained 2 ​ D 2D word is a subword of f ∞, ∞ f_{\infty,\infty} of size ( k, l) (k,l). ∎

###### Remark 6.

In Lemma 3, we have constructed the entire subword from F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL}. Similarly, with appropriate conditions on F ​ R ​ A ​ M ​ E L FRAME_{L}, F ​ R ​ A ​ M ​ E T FRAME_{T}, F ​ R ​ A ​ M ​ E R FRAME_{R}, F ​ R ​ A ​ M ​ E B FRAME_{B}, one can construct the entire subword from any of F ​ R ​ A ​ M ​ E L ​ B FRAME_{LB}, F ​ R ​ A ​ M ​ E T ​ R FRAME_{TR} and F ​ R ​ A ​ M ​ E R ​ B FRAME_{RB} also.

We are now ready to locate any factor of f ∞, ∞ f_{\infty,\infty}. Let w w be a subword of f ∞, ∞ f_{\infty,\infty}. Let the size of w w be ( k, l) (k,l). Note that, because w w is a 2 ​ D 2D word, first-occ( w w) will be a pair ( i, j) (i,j) such that first-occ ( F ​ R ​ A ​ M ​ E T FRAME_{T} of w w) is j j in the i t ​ h i^{th} row of f ∞, ∞ f_{\infty,\infty} and first-occ ( F ​ R ​ A ​ M ​ E L FRAME_{L} of w w) is i i in the j t ​ h j^{th} column of f ∞, ∞ f_{\infty,\infty} and thus the domain of w w in f ∞, ∞ f_{\infty,\infty} is { i + 1, i + 2, …, i + k } × { j + 1, j + 2, …, j + l } \{i+1,i+2,\ldots,i+k\}\times\{j+1,j+2,\dots,j+l\}. The definition of occ( w w) is similar to its 1 ​ D 1D counterpart. Since a subword of f ∞, ∞ f_{\infty,\infty} is uniquely determined by its F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL}, its first occurrence and hence its all other occurrences will be determined by the first occurrences of its F ​ R ​ A ​ M ​ E T FRAME_{T} and F ​ R ​ A ​ M ​ E L FRAME_{L}. With F ​ R ​ A ​ M ​ E T FRAME_{T} and F ​ R ​ A ​ M ​ E L FRAME_{L} both being subwords of 1 ​ D 1D Fibonacci words, we have the following Proposition.

###### Proposition 3.

Let w w be a subword of f ∞, ∞ f_{\infty,\infty}. Let F ​ R ​ A ​ M ​ E T FRAME_{T} and F ​ R ​ A ​ M ​ E L FRAME_{L} denote its first row and first column respectively. Then,

 | first-occ( w) = { ( f ​ o L d, b, f ​ o T d, c) if F ​ R ​ A ​ M ​ E L is over { d, b } and F ​ R ​ A ​ M ​ E T is over { d, c } ( f ​ o L d, b, f ​ o T b, a) if F ​ R ​ A ​ M ​ E L is over { d, b } and F ​ R ​ A ​ M ​ E T is over { b, a } ( f ​ o L c, a, f ​ o T d, c) if F ​ R ​ A ​ M ​ E L is over { c, a } and F ​ R ​ A ​ M ​ E T is over { d, c } ( f ​ o L c, a, f ​ o T b, a) if F ​ R ​ A ​ M ​ E L is over { c, a } and F ​ R ​ A ​ M ​ E T is over { b, a } \displaystyle\textit{first-occ($w$)}=\begin{cases}(fo_{L}^{d,b},fo_{T}^{d,c})&\quad\text{if $FRAME_{L}$ is over $\{d,b\}$ and $FRAME_{T}$ is over $\{d,c\}$}\\ (fo_{L}^{d,b},fo_{T}^{b,a})&\quad\text{if $FRAME_{L}$ is over $\{d,b\}$ and $FRAME_{T}$ is over $\{b,a\}$}\\ (fo_{L}^{c,a},fo_{T}^{d,c})&\quad\text{if $FRAME_{L}$ is over $\{c,a\}$ and $FRAME_{T}$ is over $\{d,c\}$}\\ (fo_{L}^{c,a},fo_{T}^{b,a})&\quad\text{if $FRAME_{L}$ is over $\{c,a\}$ and $FRAME_{T}$ is over $\{b,a\}$}\\ \end{cases} |  |

where f ​ o L d, b fo_{L}^{d,b} is the first-occ( F ​ R ​ A ​ M ​ E L FRAME_{L}) in f ∞ d, b f_{\infty}^{d,b}, f ​ o L c, a fo_{L}^{c,a} is the first-occ( F ​ R ​ A ​ M ​ E L FRAME_{L}) in f ∞ c, a f_{\infty}^{c,a}, f ​ o T d, c fo_{T}^{d,c} is the first-occ( F ​ R ​ A ​ M ​ E T FRAME_{T}) in f ∞ d, c f_{\infty}^{d,c} and f ​ o T b, a fo_{T}^{b,a} is the first-occ( F ​ R ​ A ​ M ​ E T FRAME_{T}) in f ∞ b, a f_{\infty}^{b,a}.

###### Proof.

We discuss the proof for the case in which F ​ R ​ A ​ M ​ E L FRAME_{L} is over { d, b } \{d,b\} and F ​ R ​ A ​ M ​ E T FRAME_{T} is over { d, c } \{d,c\}. Proofs of the other cases are similar.

Since w w can occur in f ∞, ∞ f_{\infty,\infty}, only when F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} of w w occurs in f ∞, ∞ f_{\infty,\infty}, it is clear that first-occ( w w) is decided by first-occ ( F ​ R ​ A ​ M ​ E L FRAME_{L}) in f ∞ d, b f_{\infty}^{d,b} and first-occ ( F ​ R ​ A ​ M ​ E T FRAME_{T}) in f ∞ d, c f_{\infty}^{d,c}. Let f ​ o L d, b ≥ 0 fo_{L}^{d,b}\geq 0, be first-occ ( F ​ R ​ A ​ M ​ E L FRAME_{L}) in f ∞ d, b f_{\infty}^{d,b}. Let f ​ o T d, c ≥ 0 fo_{T}^{d,c}\geq 0 be first-occ ( F ​ R ​ A ​ M ​ E T FRAME_{T}) in f ∞ d, c f_{\infty}^{d,c}. Since all the columns of f ∞, ∞ f_{\infty,\infty} over { d, b } \{d,b\} are identical f ​ o L d, b fo_{L}^{d,b} value will be the same in all the columns which are over { d, b } \{d,b\}. So in the f ​ o T d, c t ​ h {fo_{T}^{d,c}}^{\>th} column (where F ​ R ​ A ​ M ​ E T ​ ( w) FRAME_{T}(w) occurs for the first time) also, f ​ o L d, b fo_{L}^{d,b} will be the same. Similarly, since all the rows of f ∞, ∞ f_{\infty,\infty} over { d, c } \{d,c\} are identical f ​ o T d, c fo_{T}^{d,c} value will be the same in all the rows which are over { d, c } \{d,c\}.

Now, first-occ ( F ​ R ​ A ​ M ​ E T ​ L ​ ( w) FRAME_{TL}(w)) can be ( i, j) (i,j), say, only when both first-occ ( F ​ R ​ A ​ M ​ E L ​ ( w) FRAME_{L}(w)) and first-occ ( F ​ R ​ A ​ M ​ E T ​ ( w) FRAME_{T}(w)) are ( i, j) (i,j). Hence first-occ( w w) = first-occ ( F ​ R ​ A ​ M ​ E T ​ L ​ ( w) FRAME_{TL}(w)) = ( f ​ o L d, b fo_{L}^{d,b}, f ​ o T d, c fo_{T}^{d,c}), if F ​ R ​ A ​ M ​ E L FRAME_{L} is over { d, b } \{d,b\} and F ​ R ​ A ​ M ​ E T FRAME_{T} is over { d, c } \{d,c\}. ∎

###### Corollary 2.

Let w w be a subword of f ∞, ∞ f_{\infty,\infty}. Let first-occ( w w) be given by Proposition 3. Let F ​ R ​ A ​ M ​ E L ​ ( w) FRAME_{L}(w) be over { s 1, s 2 } \{s_{1},s_{2}\} and F ​ R ​ A ​ M ​ E T ​ ( w) FRAME_{T}(w) be over { s 1 ′, s 2 ′ } \{s^{\prime}_{1},s^{\prime}_{2}\}. Then, occ( w w) = X × Y X\times Y, where X = 𝒵 m − 1 ⊞ f ​ o L s 1, s 2 X=\mathcal{Z}_{m-1}\boxplus fo_{L}^{s_{1},s_{2}} and Y = 𝒵 n − 1 ⊞ f ​ o T s 1 ′, s 2 ′ Y=\mathcal{Z}_{n-1}\boxplus fo_{T}^{s^{\prime}_{1},s^{\prime}_{2}}.

###### Proof.

In all the columns of f ∞, ∞ f_{\infty,\infty} which are over { s 1, s 2 } \{s_{1},s_{2}\}, occ ( F ​ R ​ A ​ M ​ E L FRAME_{L}) = 𝒵 m − 1 ⊞ f ​ o L s 1, s 2 \mathcal{Z}_{m-1}\boxplus fo_{L}^{s_{1},s_{2}}, where m m is such that g m g_{m} is the shortest truncated Fibonacci word over { s 1, s 2 } \{s_{1},s_{2}\} containing F ​ R ​ A ​ M ​ E L FRAME_{L}. Similarly, in all the rows of f ∞, ∞ f_{\infty,\infty} which are over { s 1 ′, s 2 ′ } \{s_{1}^{\prime},s_{2}^{\prime}\}, occ ( F ​ R ​ A ​ M ​ E T FRAME_{T}) = 𝒵 n − 1 ⊞ f ​ o T s 1 ′, s 2 ′ \mathcal{Z}_{n-1}\boxplus fo_{T}^{s_{1}^{\prime},s_{2}^{\prime}}, where n n is such that g n g_{n} is the shortest truncated Fibonacci word over { s 1 ′, s 2 ′ } \{s_{1}^{\prime},s_{2}^{\prime}\} containing F ​ R ​ A ​ M ​ E T FRAME_{T}. Therefore, occ ( F ​ R ​ A ​ M ​ E T ​ L ​ ( w) FRAME_{TL}(w)) = ( occ ( F ​ R ​ A ​ M ​ E L ​ ( w) FRAME_{L}(w)), occ ( F ​ R ​ A ​ M ​ E T ​ ( w) FRAME_{T}(w))) = { ( x, y): x ∈ 𝒵 m − 1 ⊞ f o L s 1, s 2, y ∈ 𝒵 n − 1 ⊞ f o T s 1 ′, s 2 ′ } = X × Y \{(x,y):x\in\mathcal{Z}_{m-1}\boxplus fo_{L}^{s_{1},s_{2}},y\in\mathcal{Z}_{n-1}\boxplus fo_{T}^{s_{1}^{\prime},s_{2}^{\prime}}\}=X\times Y where X = 𝒵 m − 1 ⊞ f ​ o L s 1, s 2 X=\mathcal{Z}_{m-1}\boxplus fo_{L}^{s_{1},s_{2}} and Y = 𝒵 n − 1 ⊞ f ​ o T s 1 ′, s 2 ′ Y=\mathcal{Z}_{n-1}\boxplus fo_{T}^{s^{\prime}_{1},s^{\prime}_{2}}. Since occ ( w w) = occ ( F ​ R ​ A ​ M ​ E T ​ L ​ ( w) FRAME_{TL}(w)), the result follows. ∎

###### Example 5.

Let us find the occ( w w) where w = d d c d d c b b a w=\begin{matrix}d&d&c\\ d&d&c\\ b&b&a\end{matrix}.

Note that, F ​ R ​ A ​ M ​ E L FRAME_{L} of w w is d d b \begin{matrix}d\\ d\\ b\end{matrix} and first-occ( F ​ R ​ A ​ M ​ E L FRAME_{L}) in f ∞ d, b f_{\infty}^{d,b} is 2 2. That is f ​ o L d, b = 2 fo_{L}^{d,b}=2. Also the value of m m such that g m d, b g_{m}^{d,b} contains F ​ R ​ A ​ M ​ E L FRAME_{L} is 4 4. Similarly, F ​ R ​ A ​ M ​ E T FRAME_{T} of w w is " d d c \begin{matrix}d&d&c\end{matrix} " and first-occ( F ​ R ​ A ​ M ​ E T FRAME_{T}) in f ∞ d, c f_{\infty}^{d,c} is f ​ o T d, c = 2 fo_{T}^{d,c}=2. The value of n n such that g n d, c g_{n}^{d,c} contains F ​ R ​ A ​ M ​ E T FRAME_{T} is 4 4.

Therefore, first-occ( w w) = ( 2, 2) (2,2). And, occ( w w) = X × Y X\times Y, where where X = 𝒵 3 ⊞ 2 X=\mathcal{Z}_{3}\boxplus 2 and Y = 𝒵 3 ⊞ 2 Y=\mathcal{Z}_{3}\boxplus 2. With 𝒵 3 = { 0, 5, 8, 13, 18, … } \mathcal{Z}_{3}=\{0,5,8,13,18,\ldots\}, we have X = { 2, 7, 10, 15, 20, … } X=\{2,7,10,15,20,\ldots\} and Y = { 2, 7, 10, 15, 20, … } Y=\{2,7,10,15,20,\ldots\}. Hence occ( w w) = { ( 2, 2), ( 2, 7), ( 2, 10), …, ( 7, 2), ( 7, 7), ( 7, 10), … } \{(2,2),(2,7),(2,10),\ldots,(7,2),(7,7),(7,10),\ldots\}.

## 6 Fibonacci sequence of 1 ​ D 1D words

In this section we discuss the factor complexity of the Fibonacci language F u, v F_{u,v} where u, v ∈ { a, b } + u,v\in\{a,b\}^{+} and | u |, | v | ≥ 2 |u|,|v|\geq 2. We find the bounds of the factor complexity function and the location of the factors of the fixed point of the Fibonacci sequence of words.

###### Definition 9.

[33] Let Σ \Sigma be a finite alphabet consisting of more than one element. For two words u, v ∈ Σ + u,v\in\Sigma^{+} the following two types of Fibonacci sequences of words can be defined.

 | ( 1) w 0 = u, w 1 = v, w 2 = v u, …, w n = w n − 1 w n − 2 …; (1)\text{~}w_{0}=u,w_{1}=v,w_{2}=vu,\ldots,w_{n}=w_{n-1}w_{n-2}\ldots; |  |

 | ( 2) w 0 ′ = u, w 1 ′ = v, w 2 ′ = u u, …, w n ′ = w n − 2 ′ w n − 1 ′ …; (2)\text{~}w_{0}^{\prime}=u,w_{1}^{\prime}=v,w_{2}^{\prime}=uu,\ldots,w_{n}^{\prime}=w_{n-2}^{\prime}w_{n-1}^{\prime}\ldots; |  |

For example, with Σ = { a, b }, u = a ​ b ​ b ​ a \Sigma=\{a,b\},u=abba and v = b ​ b ​ a v=bba we have, w 0 = a b b a, w 1 = b b a, w 2 = b b a a b b a, w 3 = b b a a b b a b b a, … w_{0}=abba,w_{1}=bba,w_{2}=bbaabba,w_{3}=bbaabbabba,\ldots. The languages F u, v = { w i ∣ i ≥ 0 } F_{u,v}=\{w_{i}\mid i\geq 0\} and F u, v ′ = { w i ′ ∣ i ≥ 0 } F^{\prime}_{u,v}=\{w_{i}^{\prime}\mid i\geq 0\} are called Fibonacci Languages. As F u, v F_{u,v} and F u, v ′ F^{\prime}_{u,v} are similar, it is enough to study F u, v F_{u,v}. In [33], primitive and palindromic words in F u, v F_{u,v} are studied.

Note that if we denote by Γ \Gamma the alphabet { u, v } \{u,v\} then w 0, w 1, w 2, … w_{0},w_{1},w_{2},\ldots are the 1 ​ D 1D Fibonacci words over Γ \Gamma generated by the familiar Fibonacci morphism g: u → v, v → v ​ u g:u\rightarrow v,\quad v\rightarrow vu. Denoting the fixed point of this sequence of Fibonacci words by f ∞, u, v f_{\infty,u,v} we have, f ∞; u, v = v u v v u v u v ⋯ f_{\infty;u,v}=vuvvuvuv\cdots. Now, for k, k ′ ≥ 2 k,k^{\prime}\geq 2, suppose we have u = u 1 u 2 ⋯ u k, v = v 1 v 2 ⋯ v k ′ u=u_{1}u_{2}\cdots u_{k},v=v_{1}v_{2}\cdots v_{k^{\prime}}, with u 1, ⋯, u k, v 1, ⋯, v k ′ ∈ Σ u_{1},\cdots,u_{k},v_{1},\cdots,v_{k^{\prime}}\in\Sigma, then we get the fixed point of this Fibonacci sequence of words as an infinite word over { a, b } \{a,b\}. Let us denote this fixed point by f ∞; a, b f_{\infty;a,b}.

### 6.1 Factor Complexity of f ∞; a, b f_{\infty;a,b}

Here, as a first step, we study the factor complexity of f ∞; a, b f_{\infty;a,b} under the condition that | u | = | v | |u|=|v| (i.e. when k = k ′ k=k^{\prime}).

###### Theorem 3.

Let k ≥ 2 k\geq 2 and | u | = | v | = k |u|=|v|=k. Let m m denote the length of the factors of f ∞; u, v f_{\infty;u,v} and let l l denote the length of the factors of f ∞; a, b f_{\infty;a,b}. Given an l ≥ 2 l\geq 2, consider the least m ≥ 2 m\geq 2 such that k ​ m ≥ l km\geq l. Then for ( m − 1) ​ k + 2 ≤ l ≤ m ​ k + 1 (m-1)k+2\leq l\leq mk+1, we have,

 | p f ∞; a, b ​ ( l) ≤ { ( k − 1) ​ ( m + 1) + ( 1) ​ ( m + 2), if l = ( m − 1) ​ k + 2 ( k − 2) ​ ( m + 1) + ( 2) ​ ( m + 2), if l = ( m − 1) ​ k + 3 ⋮ ⋮ ( 1) ​ ( m + 1) + ( k − 1) ​ ( m + 2), if l = m ​ k ( k) ​ ( m + 2), if l = m ​ k + 1 p_{f_{\infty;a,b}}(l)\leq\begin{cases}\text{$(k-1)(m+1)+(1)(m+2)$,}&\quad\text{if $l=(m-1)k+2$}\\ \text{$(k-2)(m+1)+(2)(m+2)$,}&\quad\text{if $l=(m-1)k+3$}\\ \hskip 42.67912pt\text{$\vdots$}&\hskip 42.67912pt\text{$\vdots$}\\ \text{$(1)(m+1)+(k-1)(m+2)$,}&\quad\text{if $l=mk$}\\ \text{$(k)(m+2)$,}&\quad\text{if $l=mk+1$}\\ \end{cases} |  |

That is, for l = ( m − 1) ​ k + i + 1 l=(m-1)k+i+1, 1 ≤ i ≤ k 1\leq i\leq k, we have p f ∞; a, b ​ ( l) ≤ ( k − i) ​ ( m + 1) + ( i) ​ ( m + 2) p_{f_{\infty;a,b}}(l)\leq(k-i)(m+1)+(i)(m+2).

###### Proof.

Let m ≥ 2 m\geq 2 denote the length of the factors of f ∞; u, v f_{\infty;u,v} and let l ≥ 2 l\geq 2 denote the length of the factors of f ∞; a, b f_{\infty;a,b}. We analyze p f ∞; a, b ​ ( l) p_{f_{\infty;a,b}}(l) iteratively as m m increases from 2 2, in steps of 1 1. At every iterative stage we count the number of new factors created by appending either u = u 1 u 2 ⋯ u k u=u_{1}u_{2}\cdots u_{k} or v = v 1 v 2 ⋯ v k v=v_{1}v_{2}\cdots v_{k} and update l l. Observe that only these two symbols can be appended to the existing factor (of length m − 1 m-1) of f ∞; u, v f_{\infty;u,v}. In other words we analyze the factors of f ∞; a, b f_{\infty;a,b} through the factors of f ∞; u, v f_{\infty;u,v}.

Let us visualize f ∞; u, v f_{\infty;u,v} and f ∞; a, b f_{\infty;a,b} as shown below.

f ∞; u, v = v u v v u ⋯ ⋯. f_{\infty;u,v}=\begin{tabular}[]{|c|c|c|c|c|}\hline\cr$v$&$u$&$v$&$v$&$u$\\ \hline\cr\end{tabular}\cdots\cdots.

f ∞; a, b = v 1 v 2 ⋯ v k u 1 u 2 ⋯ u k v 1 v 2 ⋯ v k v 1 v 2 ⋯ v k u 1 u 2 ⋯ u k ⋯ ⋯. f_{\infty;a,b}=\begin{tabular}[]{|c|c|c|c|c|}\hline\cr$v_{1}v_{2}\cdots v_{k}$&$u_{1}u_{2}\cdots u_{k}$&$v_{1}v_{2}\cdots v_{k}$&$v_{1}v_{2}\cdots v_{k}$&$u_{1}u_{2}\cdots u_{k}$\\ \hline\cr\end{tabular}\cdots\cdots.

Recall that f ∞; u, v f_{\infty;u,v} being the infinite Fibonacci word has m + 1 m+1 factors of length m m. For an easy understanding, let us elaborate the counting process for m = 2 m=2. Consider any one of the three factors v ​ u, u ​ v, v ​ v vu,uv,vv. Let us take v ​ u = v 1 v 2 ⋯ v k u 1 u 2 ⋯ u k vu=\begin{tabular}[]{|c|c|}\hline\cr$v_{1}v_{2}\cdots v_{k}$&$u_{1}u_{2}\cdots u_{k}$\\ \hline\cr\end{tabular}. The following table can be constructed easily by observing the starting and the ending positions of the new factors created while appending u u with v v.

Factors of f ∞; a, b f_{\infty;a,b} | Length of the factor ( l l) | Number of factors |

v 1 v 2 ⋯ v k u 1 v_{1}v_{2}\cdots v_{k}u_{1}, v 2 v 3 ⋯ v k u 1 u 2 v_{2}v_{3}\cdots v_{k}u_{1}u_{2}, ⋯ \cdots | k + 1 k+1 | k k |

v 2 v 3 ⋯ v k u 1 v_{2}v_{3}\cdots v_{k}u_{1}, v 3 v 4 ⋯ v k u 1 u 2 v_{3}v_{4}\cdots v_{k}u_{1}u_{2}, ⋯ \cdots | k k | k − 1 k-1 |

⋯ \cdots | ⋯ \cdots | ⋯ \cdots |

v k − 1 ​ v k ​ u 1 v_{k-1}v_{k}u_{1}, v k ​ u 1 ​ u 2 v_{k}u_{1}u_{2} | 3 3 | 2 2 |

v k ​ u 1 v_{k}u_{1} | 2 2 | 1 1 |

Table 3: Factors of f ∞; a, b f_{\infty;a,b} formed when m = 2 m=2

This counting has to be done for each of the three factors possible ( v ​ u, u ​ v, v ​ v vu,uv,vv) and hence the values in the ‘Number of factors’ column in Tab. 3 are to be multiplied by 3 3. Now, a few more factors of the same lengths, listed above, will be created by the factors of length 3 3 of f ∞; u, v f_{\infty;u,v} also. For example, from v ​ u ​ v = v 1 v 2 ⋯ v k u 1 u 2 ⋯ u k v 1 v 2 ⋯ v k vuv=\begin{tabular}[]{|c|c|c|}\hline\cr$v_{1}v_{2}\cdots v_{k}$&$u_{1}u_{2}\cdots u_{k}$&$v_{1}v_{2}\cdots v_{k}$\\ \hline\cr\end{tabular}, we get one factor of length ( k + 2) (k+2) (namely, v k u 1 u 2 ⋯ u k v 1 v_{k}u_{1}u_{2}\cdots u_{k}v_{1}) and two factors of length ( k + 3) (k+3) and so on. Note that, for a given l l and an appropriate m m, the factors of length l l are (inherently) available at the beginning of a factor of length m m of f ∞; u, v f_{\infty;u,v} and are available at the middle of a factor of length ( m + 1) (m+1) of f ∞; u, v f_{\infty;u,v}.

Extending this counting technique, for an m ≥ 2 m\geq 2, we have,

Length ( l l) of the | No. of factors created | No. of factors created |

factor of f ∞; a, b f_{\infty;a,b} | by a factor of length m m | by a factor of length m + 1 m+1 |

 | of f ∞; u, v f_{\infty;u,v} | of f ∞; u, v f_{\infty;u,v} |

( m − 1) ​ k + 2 (m-1)k+2 | k − 1 k-1 | 1 1 |

( m − 1) ​ k + 3 (m-1)k+3 | k − 2 k-2 | 2 2 |

⋯ \cdots | ⋯ \cdots | ⋯ \cdots |

m ​ k mk | 1 1 | k − 1 k-1 |

m ​ k + 1 mk+1 | 0 0 | k k |

Now for an m ≥ 2 m\geq 2, as there are m + 1 m+1 factors of length m m and m + 2 m+2 factors of length m + 1 m+1 in f ∞; u, v f_{\infty;u,v}, we get the bound for p f ∞; a, b ​ ( l) p_{f_{\infty;a,b}}(l) as stated in the theorem. That is, by adding together the number of factors of length ( m − 1) ​ k + 2 ≤ l ≤ m ​ k + 1 (m-1)k+2\leq l\leq mk+1 that occur in the factors of length m m and m + 1 m+1 of f ∞; u, v f_{\infty;u,v} we get, for m ≥ 2 m\geq 2,

Length of the factor ( l l) | Maximum number of factors |

( m − 1) ​ k + 2 (m-1)k+2 | ( k − 1) ​ ( m + 1) + 1 ​ ( m + 2) (k-1)(m+1)+1(m+2) |

( m − 1) ​ k + 3 (m-1)k+3 | ( k − 2) ​ ( m + 1) + 2 ​ ( m + 2) (k-2)(m+1)+2(m+2) |

⋯ \cdots | ⋯ \cdots |

m ​ k mk | ( 1) ​ ( m + 1) + ( k − 1) ​ ( m + 2) (1)(m+1)+(k-1)(m+2) |

m ​ k + 1 mk+1 | ( k) ​ ( m + 2) (k)(m+2) |

Table 4: Maximum Number of Factors of length l l in f ∞; a, b f_{\infty;a,b}

Note that some of the factors created by a factor of length m m of f ∞; u, v f_{\infty;u,v} may repeat in the factors created by a factor of length m + 1 m+1 of f ∞; u, v f_{\infty;u,v}. Hence, the total number of factors obtained (i.e. the last column of Tab. 4) is, in fact a bound.

Though the proof uses an iterative argument over m m, in practical situations, when we require the number of factors of a given length l l, we should fix m ≥ 2 m\geq 2 as the least integer such that k ​ m ≥ l km\geq l. This is clear from the fact that, a factor of length l l of f ∞; a, b f_{\infty;a,b} will be created by a factor w w of f ∞; u, v f_{\infty;u,v} only when | w | ​ k ≥ l |w|k\geq l. ∎

###### Remark 7.

Also while obtaining a general formula for p f ∞; a, b ​ ( l) p_{f_{\infty;a,b}}(l), the bounds for the cases l = 2, 3, …, k − 1 l=2,3,\ldots,k-1 might have been scaled up. But this can be resolved by a simple manipulation.

###### Remark 8.

The value of the maximum number of factors (in fact the total number of factors) given by Theorem 3, in the degenerate case ( k = 1 k=1 and u = a, v = b u=a,v=b) is m + 1 m+1, the factor complexity of the 1 ​ D 1D infinite Fibonacci word.

We note that, achieving the bound given in Theorem 3 depends on the selection of u u and v v.

###### Example 6.

Let u = a ​ b ​ a ​ a, v = a ​ a ​ b ​ a u=abaa,v=aaba with k = 4 k=4. Then, f ∞; a, b = a a b a | a b a a | a a b a | a a b a | a b a a ⋯ f_{\infty;a,b}=aaba|abaa|aaba|aaba|abaa\cdots. Markers are used for better readability. Let us find the maximum number of factors of length 10 10 in f ∞; a, b f_{\infty;a,b}. As 3. k > l 3.k>l, m m is 3 3. Thus, p f ∞; a, b ​ ( 10) ≤ ( k − 1) ​ ( m + 1) + ( 1) ​ ( m + 2) = 3.4 + 1.5 = 17 p_{f_{\infty;a,b}}(10)\leq(k-1)(m+1)+(1)(m+2)=3.4+1.5=17.

Elaborating further, we have the factors of length 3 3 of f ∞; u, v f_{\infty;u,v} as v ​ u ​ v, u ​ v ​ v, v ​ v ​ u, u ​ v ​ u vuv,uvv,vvu,uvu.

Thus, factors of length 10 10 of f ∞; a, b f_{\infty;a,b},

created by v ​ u ​ v vuv: a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ a ​ a, a ​ b ​ a ​ a ​ b ​ a ​ a ​ a ​ a ​ b, b ​ a ​ a ​ b ​ a ​ a ​ a ​ a ​ b ​ a aabaabaaaa,abaabaaaab,baabaaaaba

created by u ​ v ​ v uvv: a ​ b ​ a ​ a ​ a ​ a ​ b ​ a ​ a ​ a, b ​ a ​ a ​ a ​ a ​ b ​ a ​ a ​ a ​ b, a ​ a ​ a ​ a ​ b ​ a ​ a ​ a ​ b ​ a abaaaabaaa,baaaabaaab,aaaabaaaba

created by v ​ v ​ u vvu: a ​ a ​ b ​ a ​ a ​ a ​ b ​ a ​ a ​ b, a ​ b ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a, b ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a aabaaabaab,abaaabaaba,baaabaabaa

created by u ​ v ​ u uvu: a ​ b ​ a ​ a ​ a ​ a ​ b ​ a ​ a ​ b, b ​ a ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a, a ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a abaaaabaab,baaaabaaba,aaaabaabaa

The factors of length 4 4 of f ∞; u, v f_{\infty;u,v} as v ​ u ​ v ​ u, v ​ u ​ v ​ v, u ​ v ​ v ​ u, v ​ v ​ u ​ v, u ​ v ​ u ​ v vuvu,vuvv,uvvu,vvuv,uvuv.

Thus, factors of length 10 10 of f ∞; a, b f_{\infty;a,b},

created by v ​ u ​ v ​ u vuvu: a ​ a ​ b ​ a ​ a ​ a ​ a ​ b ​ a ​ a aabaaaabaa

created by v ​ u ​ v ​ v vuvv: a ​ a ​ b ​ a ​ a ​ a ​ a ​ b ​ a ​ a aabaaaabaa

created by u ​ v ​ v ​ u uvvu: a ​ a ​ a ​ b ​ a ​ a ​ a ​ b ​ a ​ a aaabaaabaa

created by v ​ v ​ u ​ v vvuv: a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ a aaabaabaaa

created by u ​ v ​ u ​ v uvuv: a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ a aaabaabaaa

Observe that, as both u u and v v start and end with the same symbol a a, some of the factors are repeated. This happens when a factor is created again by a different arrangement of u u ’s and v v ’s. Such a situation happens in this example and hence p f ∞; a, b ​ ( 10) = 15 p_{f_{\infty;a,b}}(10)=15 only.

###### Example 7.

Let u = a ​ b ​ b ​ a ​ b u=abbab and v = b ​ a ​ a ​ b ​ a = u ¯ v=baaba=\bar{u}, the complement of v v. Let us evaluate p f ∞; a, b ​ ( 8) p_{f_{\infty;a,b}}(8). As k = 5 k=5 and l = 8 l=8, m m is 2 2. Hence, p f ∞; a, b ​ ( 8) ≤ 17 p_{f_{\infty;a,b}}(8)\leq 17. It is easy to check that all the 17 17 factors are distinct and the bound is tight for this selection of u u and v v.

### 6.2 Location of the Factors

After counting and enumerating the factors of f ∞; a, b f_{\infty;a,b} for a given l ≥ 2 l\geq 2, we can now locate the positions of occurrences of these factors in f ∞; a, b f_{\infty;a,b}.

###### Theorem 4.

Let k ≥ 2 k\geq 2 and | u | = | v | = k |u|=|v|=k. Let m m denote the length of the factors of f ∞; u, v f_{\infty;u,v} and let l l denote the length of the factors of f ∞; a, b f_{\infty;a,b}. For an m ≥ 2 m\geq 2, let L ​ o ​ c ​ ( f ​ a ​ c m i, f ∞; u, v) Loc(fac^{i}_{m},f_{\infty;u,v}), 0 ≤ i ≤ m 0\leq i\leq m, be the locations of the i t ​ h i^{th} factor of length m m of f ∞; u, v f_{\infty;u,v} in f ∞; u, v f_{\infty;u,v}. Given an l ≥ 2 l\geq 2, consider the least m ≥ 2 m\geq 2 such that k ​ m ≥ l km\geq l. Let L ​ o ​ c ​ ( f ​ a ​ c l r, f ∞; a, b) Loc(fac^{r}_{l},f_{\infty;a,b}), 0 ≤ r < ( m + 1) ​ ( m ​ k − l + 1) + ( m + 2) ​ ( l − ( m − 1) ​ k − 1) 0\leq r<(m+1)(mk-l+1)+(m+2)(l-(m-1)k-1), be the locations of the r t ​ h r^{th} factor of length l l of f ∞; a, b f_{\infty;a,b} in f ∞; a, b f_{\infty;a,b}.

Then, for 0 ≤ j ≤ m, 0 ≤ j ′ ≤ m ​ k − l 0\leq j\leq m,0\leq j^{\prime}\leq mk-l, r = j ⁡ ( m ​ k − l + 1) + j ′ r=j(mk-l+1)+j^{\prime}

 | L o c ( f a c l r, f ∞; a, b) = ⋃ L m j { ( k. L m j − ( k − 1)) + j ′ } Loc(fac^{r}_{l},f_{\infty;a,b})=\bigcup_{L^{j}_{m}}\left\{(k.L^{j}_{m}-(k-1))+j^{\prime}\right\} |  |

where the union is taken over all L m j ∈ L ​ o ​ c ​ ( f ​ a ​ c m j, f ∞; u, v) L^{j}_{m}\in Loc(fac^{j}_{m},f_{\infty;u,v}); and

for 0 ≤ j ≤ ( m + 1), 0 ≤ j ′ < l − [( m − 1) ​ k + 1] 0\leq j\leq(m+1),0\leq j^{\prime}<l-[(m-1)k+1], r = ( m + 1) ​ ( m ​ k − l + 1) + j ⁡ ( l − ( m − 1) ​ k − 1 + j ′ 𝐶𝐿𝑂𝑆𝐸 r=(m+1)(mk-l+1)+j(l-(m-1)k-1+j^{\prime},

 | L o c ( f a c l r, f ∞; a, b) = ⋃ L m + 1 j { k. L m + 1 j − j ′ } Loc(fac^{r}_{l},f_{\infty;a,b})=\bigcup_{L^{j}_{m+1}}\left\{k.L^{j}_{m+1}-j^{\prime}\right\} |  |

where the union is taken over all L m + 1 j ∈ L ​ o ​ c ​ ( f ​ a ​ c m + 1 j, f ∞; u, v) L^{j}_{m+1}\in Loc(fac^{j}_{m+1},f_{\infty;u,v}).

###### Proof.

From the counting process we used in the proof of Theorem 3, it is easy to observe that, for a given l l, ( m ​ k − l + 1) (mk-l+1) factors of length l l are created (in f ∞; a, b f_{\infty;a,b}), by each factor of length m m of f ∞; u, v f_{\infty;u,v}, and ( l − ( m − 1) ​ k − 1) (l-(m-1)k-1) factors of length l l are created (in f ∞; a, b f_{\infty;a,b}) by each factor of length ( m + 1) (m+1) of f ∞; u, v f_{\infty;u,v}. This explains the range of the index, ‘ r r ’ in L ​ o ​ c ​ ( f ​ a ​ c l r, f ∞; a, b) Loc(fac^{r}_{l},f_{\infty;a,b}).

f ∞; u, v f_{\infty;u,v} being the infinite Fibonacci word over { u, v } \{u,v\}, we know the locations of its factors of length m ≥ 1 m\geq 1. Refer ( 2) for the same. Here, as multiplication operations of the locations are involved, after finding the locations of a factor of f ∞; u, v f_{\infty;u,v}, we shift the values by 1 1 before using them. Now, as u = u 1 u 2 ⋯ u k u=u_{1}u_{2}\cdots u_{k} and v = v 1 v 2 ⋯ v k v=v_{1}v_{2}\cdots v_{k}, if a factor of length m m of f ∞; u, v f_{\infty;u,v} (say, f ​ a ​ c m fac_{m}) is located at position L m ≥ 1 L_{m}\geq 1 in f ∞; u, v f_{\infty;u,v}, then the factors of length l l of f ∞; a, b f_{\infty;a,b} will occur at positions k. L m − ( k − 1), k. L m − ( k − 2), … ​ k. L m − ( k − ( m ​ k − l + 1)) k.L_{m}-(k-1),k.L_{m}-(k-2),\ldots k.L_{m}-(k-(mk-l+1)). And whenever f ​ a ​ c m fac_{m} occurs in f ∞; u, v f_{\infty;u,v}, the same set of factors of length l l of f ∞; a, b f_{\infty;a,b} will occur in f ∞; a, b f_{\infty;a,b}. Hence, for specific values of j, j ′ j,j^{\prime} such that 0 ≤ j ≤ m, 0 ≤ j ′ ≤ m ​ k − l 0\leq j\leq m,0\leq j^{\prime}\leq mk-l,

 | ⋃ L m j { ( k. L m j − ( k − 1)) + j ′ } \bigcup_{L^{j}_{m}}\left\{(k.L^{j}_{m}-(k-1))+j^{\prime}\right\} |  |

gives the locations of the factor f ​ a ​ c l j ⁡ ( m ​ k − l + 1) + j ′ fac_{l}^{j(mk-l+1)+j^{\prime}}.

Recall that, factors of length l l are formed through factors of length m + 1 m+1 (say f ​ a ​ c m + 1 fac_{m+1}) of f ∞; u, v f_{\infty;u,v} also. As the starting positions of these factors are k. L m + 1 − j ′, 0 ≤ j ′ < l − [( m − 1) ​ k + 1] k.L_{m+1}-j^{\prime},0\leq j^{\prime}<l-[(m-1)k+1], by a similar argument as above, the second part of the result follows. ∎

###### Remark 9.

As remarked earlier all the factors of length l l obtained from f ​ a ​ c m fac_{m} and f ​ a ​ c m + 1 fac_{m+1} need not be distinct. In such a scenario, when an already obtained factor is obtained again through different j, j ′ j,j^{\prime} values, the location sets of the factor can be combined together.

###### Example 8.

Let us use the set up of Example 6 and find the locations of the factor a ​ a ​ b ​ a ​ a ​ a ​ a ​ b ​ a ​ a aabaaaabaa of length 10 10 of f ∞; a, b f_{\infty;a,b}. This factor is created by the 4 4 -length factor v ​ u ​ v ​ u vuvu of f ∞; u, v f_{\infty;u,v}. By the indexing process we use, this factor is named as f ​ a ​ c 10 12 fac_{10}^{12} in f ∞; a, b f_{\infty;a,b}. Now from Example 4 the locations set of the factor v ​ u ​ v ​ u vuvu in f ∞; u, v f_{\infty;u,v} is, L ​ o ​ c ​ ( f ​ a ​ c 4 4, f ∞; u, v) = { 4, 12, 17, 25, 33, … } Loc(fac^{4}_{4},f_{\infty;u,v})=\{4,12,17,25,33,\ldots\}. Now, using ⋃ L m + 1 j { ( k. L m + 1 j − j ′ } \bigcup\limits_{L^{j}_{m+1}}\left\{(k.L^{j}_{m+1}-j^{\prime}\right\} with appropriate values, we have , L ​ o ​ c ​ ( f ​ a ​ c 10 12, f ∞; a, b) = { 16, 18, 68, 100, 132, … } Loc(fac^{12}_{10},f_{\infty;a,b})=\{16,18,68,100,132,\ldots\}.

## 7 Fibonacci Sequence of 2 ​ D 2D Words

Similar to the Fibonacci sequence of 1 ​ D 1D words, one can construct a Fibonacci sequence of 2 ​ D 2D words. We will outline the process here.

In the development of the Fibonacci sequence of 1 ​ D 1D words, one might have observed that the sequence can be obtained in two ways. One can first develop the sequence of Fibonacci words v, v ​ u, v ​ u ​ v, v ​ u ​ v ​ v ​ u, … v,vu,vuv,vuvvu,\ldots over the alphabet { u, v } \{u,v\} and thereafter replace u u and v v, respectively by u 1 u 2 ⋯ u k u_{1}u_{2}\cdots u_{k} and v 1 v 2 ⋯ v k v_{1}v_{2}\cdots v_{k}. In the second way of construction, we start with the words u 1 u 2 ⋯ u k u_{1}u_{2}\cdots u_{k} and v 1 v 2 ⋯ v k v_{1}v_{2}\cdots v_{k} themselves and concatenate them iteratively in the Fibonacci way to get the sequence of words v 1 v 2 ⋯ v k v_{1}v_{2}\cdots v_{k}, v 1 v 2 ⋯ v k u 1 u 2 ⋯ u k v_{1}v_{2}\cdots v_{k}u_{1}u_{2}\cdots u_{k}, v 1 v 2 ⋯ v k u 1 u 2 ⋯ u k v 1 v 2 ⋯ v k v_{1}v_{2}\cdots v_{k}u_{1}u_{2}\cdots u_{k}v_{1}v_{2}\cdots v_{k}, … \ldots.

Similarly a Fibonacci sequence of 2 ​ D 2D words can be obtained in two ways. First we can develop the sequence of 2 ​ D 2D Fibonacci words over the alphabet { u, v, w, x } \{u,v,w,x\}, as defined in section 2.4 to get,

 | W 0 = u, W 1 = x, W 2 = x w v u, W 3 = x w x v u v x w x, W 4 = x w x x w v u v v u x w x x w x w x x w v u v v u, … W_{0}=u,\quad W_{1}=x,\quad W_{2}=\begin{matrix}x&w\\ v&u\end{matrix},\quad W_{3}=\begin{matrix}x&w&x\\ v&u&v\\ x&w&x\end{matrix},\quad W_{4}=\begin{matrix}x&w&x&x&w\\ v&u&v&v&u\\ x&w&x&x&w\\ x&w&x&x&w\\ v&u&v&v&u\end{matrix},\quad\ldots |  | (3) |

and then replace u, v, w, x u,v,w,x respectively by 2 ​ D 2D words over { a, b, c, d } \{a,b,c,d\} of the same size, ( m, n) (m,n). That is, with u i. j, v i, j, w i, j, x i, j ∈ { a, b, c, d }, 1 ≤ i ≤ m, 1 ≤ j ≤ n u_{i.j},v_{i,j},w_{i,j},x_{i,j}\in\{a,b,c,d\},1\leq i\leq m,1\leq j\leq n,

 | u ​ can be replaced by ​ u 1, 1 u 1, 2 ⋯ u 1, n u 2, 1 u 2, 2 ⋯ u 2, n ⋯ ⋯ u m, 1 u m, 2 ⋯ u m, n, v ​ can be replaced by ​ v 1, 1 v 1, 2 ⋯ v 1, n v 2, 1 v 2, 2 ⋯ v 2, n ⋯ ⋯ v m, 1 v m, 2 ⋯ v m, n, u\text{ can be replaced by }\begin{matrix}u_{1,1}&u_{1,2}&\cdots&u_{1,n}\\ u_{2,1}&u_{2,2}&\cdots&u_{2,n}\\ &\cdots&\cdots&\\ u_{m,1}&u_{m,2}&\cdots&u_{m,n}\par\end{matrix},\quad v\text{ can be replaced by }\begin{matrix}v_{1,1}&v_{1,2}&\cdots&v_{1,n}\\ v_{2,1}&v_{2,2}&\cdots&v_{2,n}\\ &\cdots&\cdots&\\ v_{m,1}&v_{m,2}&\cdots&v_{m,n}\par\end{matrix}, |  |

 | w ​ can be replaced by ​ w 1, 1 w 1, 2 ⋯ w 1, n w 2, 1 w 2, 2 ⋯ w 2, n ⋯ ⋯ w m, 1 w m, 2 ⋯ w m, n, x ​ can be replaced by ​ x 1, 1 x 1, 2 ⋯ x 1, n x 2, 1 x 2, 2 ⋯ x 2, n ⋯ ⋯ x m, 1 x m, 2 ⋯ x m, n. w\text{ can be replaced by }\begin{matrix}w_{1,1}&w_{1,2}&\cdots&w_{1,n}\\ w_{2,1}&w_{2,2}&\cdots&w_{2,n}\\ &\cdots&\cdots&\\ w_{m,1}&w_{m,2}&\cdots&w_{m,n}\par\end{matrix},\quad x\text{ can be replaced by }\begin{matrix}x_{1,1}&x_{1,2}&\cdots&x_{1,n}\\ x_{2,1}&x_{2,2}&\cdots&x_{2,n}\\ &\cdots&\cdots&\\ x_{m,1}&x_{m,2}&\cdots&x_{m,n}\par\end{matrix}. |  |

In the other way of construction, initially itself we can take u, v, w, x u,v,w,x as 2 ​ D 2D words of the same size, say, ( m, n) (m,n), and use Definition 3 with f 0, 0 = u, f 0, 1 = v, f 1, 0 = w, f 1, 1 = x f_{0,0}=u,f_{0,1}=v,f_{1,0}=w,f_{1,1}=x to get the desired sequence of words, { W 0, W 1, W 2, W 3, … } \{W_{0},W_{1},W_{2},W_{3},\ldots\}.

Note that the sizes of the 2 ​ D 2D words u, v, w, x u,v,w,x all have to be the same for the partial operations ⦶ \obar and ⊖ \ominus to be valid. For an easier analysis, similar to what we have assumed in 1 ​ D 1D setup, we can take u, v, w, x u,v,w,x all as square 2 ​ D 2D words of size ( k, k) (k,k). Then we can easily extend the factor complexity analysis we performed in Section 6.1 to a Fibonacci sequence of 2 ​ D 2D words.

###### Example 9.

Consider the Fibonacci sequence of 2 ​ D 2D words as in ( 3). Let u, v, w, x u,v,w,x be the 2 ​ D 2D words as given below.

 | u = a a b b b a b a b, v = b b a a a b a b a, w = d d c c c c d c c, x = c c d d d d c d d. u=\begin{matrix}a&a&b\\ b&b&a\\ b&a&b\end{matrix},\quad v=\begin{matrix}b&b&a\\ a&a&b\\ a&b&a\end{matrix},\quad w=\begin{matrix}d&d&c\\ c&c&c\\ d&c&c\end{matrix},\quad x=\begin{matrix}c&c&d\\ d&d&d\\ c&d&d\end{matrix}. |  |

Then a few initial words of the Fibonacci sequence of 2 ​ D 2D words are,

 | W 0 = a a b b b a b a b, W 1 = c c d d d d c d d, W 2 = c c d d d c d d d c c c c d d d c c b b a a a b a a b b b a a b a b a b, W 3 = c c d d d c c c d d d d c c c d d d c d d d c c c d d b b a a a b b b a a a b b b a a a b a b a b a b a b a c c d d d c c c d d d d c c c d d d c d d d c c c d d. W_{0}=\begin{matrix}a&a&b\\ b&b&a\\ b&a&b\end{matrix},\>W_{1}=\begin{matrix}c&c&d\\ d&d&d\\ c&d&d\end{matrix},\>W_{2}=\begin{matrix}c&c&d&d&d&c\\ d&d&d&c&c&c\\ c&d&d&d&c&c\\ b&b&a&a&a&b\\ a&a&b&b&b&a\\ a&b&a&b&a&b\end{matrix},\>W_{3}=\begin{matrix}c&c&d&d&d&c&c&c&d\\ d&d&d&c&c&c&d&d&d\\ c&d&d&d&c&c&c&d&d\\ b&b&a&a&a&b&b&b&a\\ a&a&b&b&b&a&a&a&b\\ a&b&a&b&a&b&a&b&a\\ c&c&d&d&d&c&c&c&d\\ d&d&d&c&c&c&d&d&d\\ c&d&d&d&c&c&c&d&d\end{matrix}. |  |

### 7.1 Factor Complexity of the Fixed Point

The fixed point of the above discussed sequence, W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}, can be obtained either directly or from the fixed point, W ∞, ∞; u, v, w, x W_{\infty,\infty;u,v,w,x}, of the sequence ( 3).

###### Theorem 5.

Let k ≥ 2 k\geq 2 and let the sizes of u, v, w, x u,v,w,x be ( k, k) (k,k). Let ( m, m ′) (m,m^{\prime}) denote the size of the factors of W ∞, ∞; u, v, w, x W_{\infty,\infty;u,v,w,x} and let ( l, l ′) (l,l^{\prime}) denote the size of the factors of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}. Given l, l ′ ≥ 2 l,l^{\prime}\geq 2, consider the least m ≥ 2 m\geq 2 such that k ​ m ≥ l km\geq l and the least m ′ ≥ 2 m^{\prime}\geq 2 such that k ​ m ′ ≥ l ′ km^{\prime}\geq l^{\prime}. Then for l = ( m − 1) ​ k + i + 1 l=(m-1)k+i+1, 1 ≤ i ≤ k 1\leq i\leq k, m ≥ 2 m\geq 2, and for l ′ = ( m ′ − 1) ​ k + i ′ + 1 l^{\prime}=(m^{\prime}-1)k+i^{\prime}+1, 1 ≤ i ′ ≤ k 1\leq i^{\prime}\leq k, m, m ′ ≥ 2 m,m^{\prime}\geq 2, we have

 | p f ∞, ∞; a, b, c, d ​ ( ( l, l ′)) ≤ [( k − i) ​ ( m + 1) + ( i) ​ ( m + 2)] ​ [( k − i ′) ​ ( m ′ + 1) + ( i ′) ​ ( m ′ + 2)]. p_{f_{\infty,\infty;a,b,c,d}}((l,l^{\prime}))\leq\left[(k-i)(m+1)+(i)(m+2)\right]\left[(k-i^{\prime})(m^{\prime}+1)+(i^{\prime})(m^{\prime}+2)\right]. |  |

###### Proof.

Before finding the bound for p f ∞, ∞; a, b, c, d ​ ( ( l, l ′)) p_{f_{\infty,\infty;a,b,c,d}}((l,l^{\prime})), l, l ′ ≥ 2 l,l^{\prime}\geq 2, observe that every row of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d} is f ∞; s 1, s 2 f_{\infty;s_{1},s_{2}} where s 1, s 2 ∈ { a, b, c, d }, s 1 ≠ s 2 s_{1},s_{2}\in\{a,b,c,d\},s_{1}\neq s_{2} and there are only 2 ​ k 2k distinct rows. Similarly every column of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}, written as a 1 ​ D 1D Fibonacci word is f ∞; s 1, s 2 f_{\infty;s_{1},s_{2}} where s 1, s 2 ∈ { a, b, c, d }, s 1 ≠ s 2 s_{1},s_{2}\in\{a,b,c,d\},s_{1}\neq s_{2} and there are only 2 ​ k 2k distinct columns. This follows from the properties listed in Lemma 1 and the fact that each of u, v, w, x u,v,w,x are of size ( k, k) (k,k).

Given l, l ′ ≥ 2 l,l^{\prime}\geq 2, we can find m ≥ 2, m ′ ≥ 2 m\geq 2,m^{\prime}\geq 2 as the least values such that l ≥ k ​ m l\geq km, l ′ ≥ k ​ m ′ l^{\prime}\geq km^{\prime}. As the columns of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d} are f ∞; s 1, s 2 f_{\infty;s_{1},s_{2}}, in any arbitrary column, there will be a maximum of ( k − i 0) ​ ( m + 1) + ( i 0) ​ ( m + 2) (k-i^{0})(m+1)+(i^{0})(m+2) factors of length l = ( m − 1) ​ k + i 0 + 1 l=(m-1)k+i^{0}+1, where i 0 ∈ { 1, 2, …, k } i^{0}\in\{1,2,\ldots,k\} (and corresponds to the given l l). Let us denote this set of factors by ‘ V ​ F VF ’ and call them ‘vertical factors’. As the rows of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d} are f ∞; s 1, s 2 f_{\infty;s_{1},s_{2}}, in any arbitrary row, there will be a maximum of ( k − i ∗) ​ ( m ′ + 1) + ( i ∗) ​ ( m ′ + 2) (k-i^{*})(m^{\prime}+1)+(i^{*})(m^{\prime}+2) factors of length l ′ = ( m ′ − 1) ​ k + i ∗ + 1 l^{\prime}=(m^{\prime}-1)k+i^{*}+1, where i ∗ ∈ { 1, 2, …, k } i^{*}\in\{1,2,\ldots,k\} (and corresponds to the given l ′ l^{\prime}). Let us denote this set of factors by ‘ H ​ F HF ’ and call them ‘horizontal factors’. As there are 2 ​ k 2k distinct columns and 2 ​ k 2k distinct rows, there will be at the maximum ( 2 ​ k) ​ ( ( k − i 0) ​ ( m + 1) + ( i 0) ​ ( m + 2)) (2k)((k-i^{0})(m+1)+(i^{0})(m+2)) vertical factors of length l l and ( 2 ​ k) ​ ( ( k − i ∗) ​ ( m + 1) + ( i ∗) ​ ( m + 2)) (2k)((k-i^{*})(m+1)+(i^{*})(m+2)) horizontal factors of length l ′ l^{\prime} available in W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}.

Now, let us call the prefix of size ( 1, 1) (1,1) of a factor (vertical or horizontal) as its head. For any random vertical factor of length l l, say V ​ F I VF_{I}, available in the J t ​ h J^{th} column of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}, with its head being positioned in the I t ​ h I^{th} row of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}, there will be a unique horizontal factor of length l ′ l^{\prime}, say H ​ F J HF_{J}, available in the I t ​ h I^{th} row, having its head positioned at the J t ​ h J^{th} column. This argument is similar to the argument used in the proof of Preposition 5 5 of [28]. Now, V ​ F I VF_{I} and H ​ F J HF_{J}, having the same head, will form a F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} with the symbol available at the head becoming s j ​ o ​ i ​ n ​ t, T ​ L s_{joint,TL}. Similar to the construction used in Lemma 3, this F ​ R ​ A ​ M ​ E T ​ L FRAME_{TL} can be completed to get a factor of size ( l, l ′) (l,l^{\prime}) of W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}. As every vertical factor in V ​ F VF pairs up with a unique horizontal factor in H ​ F HF, there will be [( k − i 0) ​ ( m + 1) + ( i 0) ​ ( m + 2)] ​ [( k − i ∗) ​ ( m ′ + 1) + ( i ∗) ​ ( m ′ + 2)] \left[(k-i^{0})(m+1)+(i^{0})(m+2)\right]\left[(k-i^{*})(m^{\prime}+1)+(i^{*})(m^{\prime}+2)\right] factors of size ( l, l ′) (l,l^{\prime}). As all these factors being distinct depends on the selection of u, v, w, x u,v,w,x, we have,

 | p f ∞, ∞; a, b, c, d ​ ( ( l, l ′)) ≤ [( k − i) ​ ( m + 1) + ( i) ​ ( m + 2)] ​ [( k − i ′) ​ ( m ′ + 1) + ( i ′) ​ ( m ′ + 2)]. p_{f_{\infty,\infty;a,b,c,d}}((l,l^{\prime}))\leq\left[(k-i)(m+1)+(i)(m+2)\right]\left[(k-i^{\prime})(m^{\prime}+1)+(i^{\prime})(m^{\prime}+2)\right]. |  |

∎

###### Example 10.

Let us extend Example 7 here. Let u, v, w, x u,v,w,x be any random 2 ​ D 2D words over { a, b, c, d } \{a,b,c,d\} of size ( 5, 5) (5,5). Then p f ∞, ∞; a, b, c, d ​ ( ( 8, 8)) ≤ 17.17 = 289 p_{f_{\infty,\infty;a,b,c,d}}((8,8))\leq 17.17=289.

### 7.2 Location of the Factors

The procedure we followed to locate a factor of f ∞; a, b f_{\infty;a,b} can be extended to locate any factor of f ∞, ∞; a, b, c, d f_{\infty,\infty;a,b,c,d}. We conclude this section by outlining the steps to perform the same.

Given a factor ‘ F ​ a ​ c ​ t Fact ’ of f ∞, ∞; a, b, c, d f_{\infty,\infty;a,b,c,d} of size ( l, l ′) (l,l^{\prime}), l, l ′ ≥ 2 l,l^{\prime}\geq 2, consider the least m ≥ 2 m\geq 2 such that k ​ m ≥ l km\geq l and the least m ′ ≥ 2 m^{\prime}\geq 2 such that k ​ m ′ ≥ l ′ km^{\prime}\geq l^{\prime}. Let us index all the factors of size ( l, l ′) (l,l^{\prime}) as f ​ a ​ c ( l, l ′) r, r ′ fac_{(l,l^{\prime})}^{r,r^{\prime}}, where 0 ≤ r < ( m + 1) ​ ( m ​ k − l + 1) + ( m + 2) ​ ( l − ( m − 1) ​ k − 1) 0\leq r<(m+1)(mk-l+1)+(m+2)(l-(m-1)k-1) and 0 ≤ r ′ < ( m ′ + 1) ​ ( m ′ ​ k − l ′ + 1) + ( m ′ + 2) ​ ( l ′ − ( m ′ − 1) ​ k − 1) 0\leq r^{\prime}<(m^{\prime}+1)(m^{\prime}k-l^{\prime}+1)+(m^{\prime}+2)(l^{\prime}-(m^{\prime}-1)k-1). Then using Theorem 4, we can find the locations of F ​ R ​ A ​ M ​ E L FRAME_{L} (i.e. L ​ o ​ c ​ ( f ​ a ​ c l r, f ∞; s 1, s 2 CLOSE Loc(fac^{r}_{l},f_{\infty;s_{1},s_{2}}, s 1 ≠ s 2 s_{1}\neq s_{2}) in the columns in which F ​ R ​ A ​ M ​ E L FRAME_{L} occurs as a factor. Similarly, we can find the locations of F ​ R ​ A ​ M ​ E T FRAME_{T} (i.e. L ​ o ​ c ​ ( f ​ a ​ c l ′ r ′, f ∞; s 1, s 2, s 1 ≠ s 2 CLOSE Loc(fac^{r^{\prime}}_{l^{\prime}},f_{\infty;s_{1},s_{2}},s_{1}\neq s_{2}) in the rows in which F ​ R ​ A ​ M ​ E T FRAME_{T} occurs as a factor. As s j ​ o ​ i ​ n ​ t, T ​ L s_{joint,TL} occurs at the locations " L ​ o ​ c ​ ( f ​ a ​ c l r, f ∞; s 1, s 2) × L ​ o ​ c ​ ( f ​ a ​ c l ′ r ′, f ∞; s 1, s 2) Loc(fac^{r}_{l},f_{\infty;s_{1},s_{2}})\times Loc(fac^{r^{\prime}}_{l^{\prime}},f_{\infty;s_{1},s_{2}}) ", we have,

 | L ​ o ​ c ​ ( f ​ a ​ c ( l, l ′) r, r ′, f ∞, ∞; a, b, c, d) = ( L ​ o ​ c ​ ( f ​ a ​ c l r, f ∞; s 1, s 2), L ​ o ​ c ​ ( f ​ a ​ c l r, f ∞; s 1, s 2)). Loc(fac_{(l,l^{\prime})}^{r,r^{\prime}},f_{\infty,\infty;a,b,c,d})=(Loc(fac^{r}_{l},f_{\infty;s_{1},s_{2}}),Loc(fac^{r}_{l},f_{\infty;s_{1},s_{2}})). |  |

## 8 Concluding Remarks

The knowledge of all the subwords of an infinite word would be very useful to analyse the characteristics of the word. Though any sort of analysis like periodicity, factor complexity is tricky in 2 ​ D 2D words, 2 ​ D 2D Fibonacci words with their simple and elegant structure are pliable for exploring their properties. In this paper we have enumerated the subwords of the 2 ​ D 2D infinite Fibonacci word, f ∞, ∞ f_{\infty,\infty}, in a few possible ways. The location of the occurrences of these subwords are also found out.

Suffix tree is an important tool used for pattern matching and dictionary searching [23, 29]. Again, there are some limitations while extending this tool for 2 ​ D 2D words [14]. But the relatively simpler structure of f ∞, ∞ f_{\infty,\infty} may help us to develop one for 2 ​ D 2D words of similar type. Also, variations attempted in the generation of the Fibonacci sequence [30] lead to variants of 1 ​ D 1D / 2 ​ D 2D Fibonacci words [16]. We might start exploring these directions. One more compelling direction of work can be towards estimating the factor complexities of f ∞; a, b f_{\infty;a,b} ( W ∞, ∞; a, b, c, d W_{\infty,\infty;a,b,c,d}, respectively,) when the length of u u and v v are not equal in f ∞; u, v f_{\infty;u,v} (when the sizes of u u, v v, w w, x x are not equal in W ∞, ∞; u, v, w, x W_{\infty,\infty;u,v,w,x}, respectively).

## References

- [1] Anselmo, M., Giammarresi, D., Madonia, M.: Prefix picture codes: A decidable class of two-dimensional codes. International Journal of Foundations of Computer Science 25(08), 1017–1031 (2014)
- [2] Apostolico, A., Brimkov, V.E.: Fibonacci arrays and their two-dimensional repetitions. Theoretical Computer Science 237(1-2), 263–273 (2000)
- [3] Berstel, J.: Fibonacci words - a survey. In: Rozenberg, G., Salomaa, A. (eds.) The book of L, pp. 13–27. Springer-Verlag (1986)
- [4] Blumer, A., Blumer, J., Haussler, D., Ehrenfeucht, A., Chen, M., Seiferas, J.: The smallest automaton recognizing the subwords of a text. Theoretical Computer Science 40, 31–55 (1985)
- [5] Burcroff, A., Winsor, E.: Generalized Lyndon factorizations of infinite words. Theoretical Computer Science 809, 30–38 (2020)
- [6] Charlier, E., Kärki, T., Rigo, M.: Multidimensional generalized automatic sequences and shape-symmetric morphic words. Discrete Mathematics 310(6), 1238–1252 (2010)
- [7] Chuan, W.F.: Fibonacci words. Fibonacci Quarterly 30(1), 68–76 (1992)
- [8] Chuan, W.F.: Symmetric Fibonacci words. Fibonacci Quarterly 31(3), 251–255 (1993)
- [9] Chuan, W.F.: Generating Fibonacci words. Fibonacci Quarterly 33(2), 104 – 112 (1995)
- [10] Chuan, W.F., Ho, H.L.: Locating factors of the infinite Fibonacci word. Theoretical Computer Science 349(3), 429–442 (2005)
- [11] Crochemore, M., Vérin, R.: Direct construction of compact directed acyclic word graphs. In: Proceedings of the 8th Annual Symposium on Combinatorial Pattern Matching. pp. 116–129. CPM ’97, Springer-Verlag (1997)
- [12] Gamard, G., Richomme, G., Shallit, J., Smith, T.: Periodicity in rectangular arrays. Information Processing Letters 118, 58–63 (2017)
- [13] Giammarresi, D., Restivo, A.: Two-dimensional languages. In: G. Rozenberg, A. Salomaa (eds), Handbook of Formal Languages, Vol. 3. Springer-Verlag (1997)
- [14] Giancarlo, R., Guaiana, D.: On-line construction of two-dimensional suffix trees. Journal of Complexity 15(1), 72–127 (1999)
- [15] Jahannia, M., Mohammad-noori, M., Rampersad, N., Stipulanti, M.: Palindromic Ziv–Lempel and Crochemore factorizations of m-bonacci infinite words. Theoretical Computer Science 790, 16–40 (2019)
- [16] Jishe, F.: Some new remarks about the dying rabbit problem. Fibonacci Quarterly 49(2), 171–176 (2011)
- [17] Kitaev, S., Lozin, V.: Words and Graphs. Springer Cham (2015)
- [18] Kulkarni, M.S., Mahalingam, K., Sivasankar, M.: Combinatorial properties of Fibonacci arrays. In: Gopal, T., Watada, J. (eds.) Theory and Applications of Models of Computation. pp. 448–466. Springer International Publishing (2019)
- [19] Lothaire, M.: Combinatorics on words. Cambridge University Press (1997)
- [20] Lothaire, M.: Algebraic combinatorics on words. Cambridge University Press (2002)
- [21] de Luca, A.: A combinatorial property of the F ibonacci words. Information Processing Letters 12(4), 193–195 (1981)
- [22] Mahalingam, K., Sivasankar, M., Krithivasan, K.: Palindromic properties of two dimensional Fibonacci words. The Romanian Journal of Information Science and Technology 21(3), 256 – 266 (2018)
- [23] Maxime, C., Christophe, H., Thierry, L.: Algorithms on Strings. Cambridge University Press (2007)
- [24] Mignosi, F., Pirillo, G.: Repetitions in the Fibonacci infinite word. RAIRO Theoretical Informatics and Applications 26(3), 199 – 204 (1992)
- [25] Rosenfeld, A.: Picture languages: Formal models of picture recognition. Academic Press (1979)
- [26] Rytter, W.: The structure of subword graphs and suffix trees of Fibonacci words. Theoretical Computer Science 363(2), 211–223 (2006)
- [27] Siromoney, G., Siromoney, R., Krithivasan, K.: Picture languages with array rewriting rules. Information and Control 22, 447–470 (1973)
- [28] Sivasankar, M., Rama, R.: Two-dimensional Fibonacci words: Tandem repeats and factor complexity. Advances in Applied Mathematics 149, 102553 (2023)
- [29] Smyth, B., Smyth, W.: Computing Patterns in Strings. Pearson Education (2003)
- [30] Swain, Gordon, A.: Exploring sequences through variations on Fibonacci. Ohio Journal of School Mathematics 77(1), 29–33 (2017)
- [31] Walczak, B.: A simple representation of subwords of the Fibonacci word. Information Processing Letters 110(21), 956–960 (2010)
- [32] West, D.B.: Introduction to Graph Theory. Pearson Education, 2nd edn. (2001)
- [33] Yu, S.S.: Languages and codes. Tsang Hai Book Publishing Co. (2005)

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2207.04303
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2207.04304
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2207.04304
[7]: https://arxiv.org/pdf/2207.04304
[8]: /html/2207.04305
