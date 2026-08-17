<!-- source: https://ar5iv.labs.arxiv.org/html/2204.13977 | converted from HTML -->

[2204.13977] Two-dimensional Fibonacci Words: Tandem Repeats and Factor Complexity

# Two-dimensional Fibonacci Words: Tandem Repeats and Factor Complexity

Sivasankar M Email: [ma16d028@smail.iitm.ac.in][1] Address: Department of Mathematics, Indian Institute of Technology Madras, Chennai, India Rama R Email: [ramar@iitm.ac.in][2] Address: Department of Mathematics, Indian Institute of Technology Madras, Chennai, India

###### Abstract

If x x is a non-empty string then the repetition x ​ x xx is called a tandem repeat. Similarly, a tandem in a two dimensional array X X is a configuration consisting of a same primitive block W W that touch each other with one side or corner. In [1], Apostolico and Brimkov have proved various bounds for the number of tandems in a two dimensional word of size m × n m\times n. Of the two types of tandems considered therein, they also proved that, for one type, the number of occurrences in an m × n m\times n Fibonacci array attained the general upper bound, 𝒪 ⁡ ( m 2 ​ n ​ log ​ n) \mathcal{O}(m^{2}n\hskip 2.84544pt\mbox{log}\hskip 2.84544ptn). In this paper, we derive an expression for the exact number of tandems in a given finite Fibonacci array f m, n f_{m,n}. As a required result, we derive the factor complexities of f m, n f_{m,n}, m, n ≥ 0 m,n\geq 0 and that of the infinite Fibonacci word f ∞, ∞ f_{\infty,\infty}. Generations of f ∞, ∞ f_{\infty,\infty} and f m, n f_{m,n}, for any given m, n ≥ 1 m,n\geq 1 using a two-dimensional homomorphism is also achieved.

###### Keywords:

Fibonacci Words , Fibonacci Arrays , Tandems , Two-dimensional Factor Complexity , Two-dimensional Morphic Words

###### 2020 MSC

68R15 , 68Q45

## 1 Introduction

The field of combinatorics of words produces many path breaking results which are directly used in computer science, molecular biology and particle physics. To be more specific, we can mention pattern recognition, image processing techniques in computer science, DNA computing in molecular biology and crystallography in physics [2, 3, 4]. In these research directions, similar to palindromes, another interesting and important structure is repetitive substrings. If x x is a non-empty string then the repetition x ​ x xx is called a tandem repeat or a square. Axel and Thue’s work on square free words and avoidable patterns, provided more insights in to tandems [5]. In DNAs, when a pattern of one or more nucleotides is repeated, with the repetitions directly adjacent to each other, we say a tandem has occurred. More information about tandem repeats can help in determining inherited traits of an individual and are useful in genealogical DNA tests. The capacity and expressiveness of genomic tandem duplication is explored in [6]. In computer science engineering, tandem repeats are used in compression algorithms [7].

A natural extension of one dimensional (hereafter, sometimes denoted by 1 ​ D 1D) words is to two dimensions. A two dimensional (hereafter, sometimes denoted by 2 ​ D 2D) word of size m × n m\times n is a rectangular arrangement of symbols from an alphabet, in m m rows and n n columns. A tandem in a two dimensional array X X is a configuration consisting of a same primitive block W W that touch each other with one side or corner. Basically, tandem repeats in one dimensional strings are detected using suffix trees [8, 9]. It is natural to expect more amount of work (compared to the one dimensional setup) to detect a tandem in two dimensions. Algorithms to locate periods,palindromes, runs etc. also become more complex in a multi dimensional setup [10, 11, 12, 13].

In [1],the authors have proved various bounds for the number of tandems in a two dimensional word of size m × n m\times n. In fact they have considered two types of tandems. They have introduced a sequence of 2 ​ D 2D words called 2 ​ D 2D Fibonacci arrays and proved that the number of occurrences of one of the tandem type attains the general upper bound of 𝒪 ⁡ ( m 2 ​ n ​ log ​ n) \mathcal{O}(m^{2}n\hskip 2.84544pt\mbox{log}\hskip 2.84544ptn) in an m × n m\times n Fibonacci array. Like Fibonacci numbers, Fibonacci words/arrays are very exciting. For a detailed study of Fibonacci words [14, 15] can be referred. Continuing the work done in [1] on Fibonacci arrays, we count the exact number of tandems in a given Fibonacci array f m, n f_{m,n}.

The main contributions of this paper are:

- -

The exact number of tandems occurring (with repetition and without repetition) in a given f m, n f_{m,n} are counted.

- -

Factor complexity of finite Fibonacci words are obtained.

- -

A two dimensional morphism generating the 2D infinite Fibonacci word f ∞, ∞ f_{\infty,\infty} is developed.

- -

A Deterministic Finite state Automaton with Output (DFAO) is constructed for f ∞, ∞ f_{\infty,\infty}.

This paper is organised as follows. Section 2 has the prerequisites for understanding the later sections. Section 3 explains the types of tandems that occur in a 2 ​ D 2D word. Section 4 counts the number of Tandems (repetitions included) in a given f m, n f_{m,n}. In Section 5 we find the factor complexity of the one-dimensional Fibonacci word f n f_{n} which is used in Section 6 to find the number of distinct tandems in f m, n f_{m,n}. In Section 7 the 2 ​ D 2D morphism generating f ∞, ∞ f_{\infty,\infty} is developed. In Section 8 the factor complexities of f m, n f_{m,n} and f ∞, ∞ f_{\infty,\infty} are found out. Section 9 discusses the DFAO generating f ∞, ∞ f_{\infty,\infty}.

## 2 Preliminaries

### 2.1 Words Over an Alphabet

A finite non-empty set of symbols is called an alphabet and is denoted by Σ \Sigma. A word w = x 1 x 2 ⋯ x n w=x_{1}x_{2}\cdots x_{n} of length n n, is the juxtaposition (familiarly known as concatenation) of symbols x 1, x 2, …, x n x_{1},x_{2},\ldots,x_{n} taken from Σ \Sigma. The length of the word w w, that is the number of symbols in w w, is denoted by | w | |w|. The set of all words over Σ \Sigma including the empty word λ \lambda, is denoted by Σ ∗ \Sigma^{*}, whereas Σ + \Sigma^{+} denotes the set of all non-empty words over Σ \Sigma. In fact, Σ ∗ \Sigma^{*} is a free monoid under the operation concatenation. A word x ∈ Σ ∗ x\in\Sigma^{*} is a factor of another word w ∈ Σ ∗ w\in\Sigma^{*} if w = u ​ x ​ v w=uxv for some u, v ∈ Σ ∗ u,v\in\Sigma^{*}. A word x ∈ Σ ∗ x\in\Sigma^{*} is a prefix (suffix, respectively) of the word w w if w = x ​ y w=xy ( w = y ​ x w=yx, respectively) for some y ∈ Σ ∗ y\in\Sigma^{*}. The reversal of w = x 1 x 2 ⋯ x n w=x_{1}x_{2}\cdots x_{n} is defined to be the string w R = x n ⋯ x 2 x 1 w^{R}=x_{n}\cdots x_{2}x_{1}. A word w w is said to be a palindrome or a one-dimensional palindrome if w = w R w=w^{R}. Powers w k w^{k}, k ≥ 0 k\geq 0 of a word w w are obtained by concatenating w w with itself, k k number of times. A word w w is said to be primitive if w = u n w=u^{n} implies n = 1 n=1 and w = u w=u. A square in a word w w is a subword of w w, which is of the form x ​ x xx, x ∈ Σ + x\in\Sigma^{+}. For a more elaborate study of formal language theory and combinatorics on words, the reader is referred to [16, 17].

### 2.2 Two-dimensional Words

A subset of Σ ∗ \Sigma^{*} is called a language. Studying the type and the grammar of the words in a language constitute the formal language theory where as analysing number of squares, palindromes etc. is combinatorics on words. Extending formal language theory and combinatorics of words to two dimensions is a challenging task. The difficulty arises due to the presence of two directions. Below a short introduction to two-dimensional languages is given. Interested reader can refer [18] for further concepts.

###### Definition 1.

[18] Let Σ \Sigma be an alphabet. An array ( ( also called a picture or two-dimensional word)) u = [u i, j] 1 ≤ i ≤ m, 1 ≤ j ≤ n u=[u_{i,j}]_{1\leq i\leq m,1\leq j\leq n} of size ( m, n) (m,n) over Σ \Sigma is a two-dimensional rectangular finite arrangement of letters:

 | u = u 1, 1 u 1, 2 ⋯ u 1, n − 1 u 1, n u 2, 1 u 2, 2 ⋯ u 2, n − 1 u 2, n ⋱ u m − 1, 1 u m − 1, 2 ⋯ u m − 1, n − 1 u m − 1, n u m, 1 u m, 2 ⋯ u m, n − 1 u m, n u=\begin{matrix}u_{1,1}&u_{1,2}&\cdots&u_{1,n-1}&u_{1,n}\\ u_{2,1}&u_{2,2}&\cdots&u_{2,n-1}&u_{2,n}\\ \vdots&\vdots&\ddots&\vdots&\vdots\\ u_{m-1,1}&u_{m-1,2}&\cdots&u_{m-1,n-1}&u_{m-1,n}\\ u_{m,1}&u_{m,2}&\cdots&u_{m,n-1}&u_{m,n}\\ \end{matrix} |  |

The number of rows and columns of u u are denoted, respectively, by | u | row |u|_{\text{row}} and | u | col |u|_{\text{col}}. The array of size ( 0, 0) (0,0) denoted by Λ \Lambda is the empty array. The arrays of sizes ( m, 0) (m,0) and ( 0, m) (0,m) for m > 0 m>0 are not defined. It is noted that some authors consider these arrays also as the empty array. The set of all arrays over Σ \Sigma including the empty array, Λ \Lambda, is denoted by Σ ∗ ⁣ ∗ \Sigma^{**}, whereas Σ + ⁣ + \Sigma^{++} is the set of all non-empty arrays over Σ \Sigma.

To locate any position or region in an array, we require a reference system [19]. Given an array u u, the set of coordinates { 1, 2, …, | u | row } × { 1, 2, …, | u | col } \{1,2,\ldots,|u|_{\text{row}}\}\times\{1,2,\ldots,|u|_{\text{col}}\} is referred to as the domain of u u. We also use t, b, l, r (the initials of the words top, bottom, left, right, respectively) to detect the sides or boundaries of u u. A subdomain or subarray of an array u u, denoted by u ⁡ [( i, j), ( i ′, j ′)] u[(i,j),(i^{\prime},j^{\prime})], is the portion of u u located in the region { i, i + 1, …, i ′ } × { j, j + 1, …, j ′ } \{i,i+1,\ldots,i^{\prime}\}\times\{j,j+1,\ldots,j^{\prime}\}, where 1 ≤ i ≤ | u | row, 1 ≤ j ≤ | u | col 1\leq i\leq|u|_{\text{row}},1\leq j\leq|u|_{\text{col}}. Below we state the concatenation operation between two arrays and further definitions associated with 2D arrays.

###### Definition 2.

[18] Let u, v u,v be arrays over Σ \Sigma, of sizes ( m 1, n 1) (m_{1},n_{1}) and ( m 2, n 2) (m_{2},n_{2}), respectively with m 1, n 1, m 2, n 2 > 0 m_{1},n_{1},m_{2},n_{2}>0. Then,

1. 1.

The column concatenation of u u and v v, denoted by ⦶ \obar, is a partial operation, defined if m 1 = m 2 = m m_{1}=m_{2}=m, and is given by

 | u ⦶ v = u 1, 1 ⋯ u 1, n 1 v 1, 1 ⋯ v 1, n 2 u m, 1 ⋯ u m, n 1 v m, 1 ⋯ v m, n 2 u\obar v=\begin{matrix}u_{1,1}&\cdots&u_{1,n_{1}}&v_{1,1}&\cdots&v_{1,n_{2}}\\ \vdots&&\vdots&\vdots&&\vdots\\ u_{m,1}&\cdots&u_{m,n_{1}}&v_{m,1}&\cdots&v_{m,n_{2}}\end{matrix} |  |

2. 2.

The row concatenation of u u and v v, denoted by ⊖ \ominus, is a partial operation, defined if n 1 = n 2 = n n_{1}=n_{2}=n, and is given by

 | u ⊖ v = u 1, 1 ⋯ u 1, n u m 1, 1 ⋯ u m 1, n v 1, 1 ⋯ v 1, n v m 2, 1 ⋯ v m 2, n u\ominus v=\begin{matrix}u_{1,1}&\cdots&u_{1,n}\\ \vdots&&\vdots\\ u_{m_{1},1}&\cdots&u_{m_{1},n}\\ v_{1,1}&\cdots&v_{1,n}\\ \vdots&&\vdots\\ v_{m_{2},1}&\cdots&v_{m_{2},n}\end{matrix} |  |

Note that, the operations of column and row concatenations are associative but not commutative and Λ \Lambda is the neutral element for both the operations.

With these operations defined, the definitions of a subword, prefix, primitive word and palindromes follow.

###### Definition 3.

[20] Given u ∈ Σ ∗ ⁣ ∗ u\in\Sigma^{**}, v ∈ Σ ∗ ⁣ ∗ v\in\Sigma^{**} is said to be a subword (respectively, proper subword) of u u, denoted by v ≤ s ​ w u v\leq_{sw}u (respectively v < s ​ w u) v<_{sw}u) if u = x ⦶ ( x ′ ⊖ v ⊖ y ′) ⦶ y u=x\obar(x^{\prime}\ominus v\ominus y^{\prime})\obar y or u = x ⊖ ( x ′ ⦶ v ⦶ y ′) ⊖ y u=x\ominus(x^{\prime}\obar v\obar y^{\prime})\ominus y for some x, x ′, y, y ′ ∈ Σ ∗ ⁣ ∗ x,x^{\prime},y,y^{\prime}\in\Sigma^{**} (respectively if any of x, x ′, y, y ′ x,x^{\prime},y,y^{\prime} are non-empty).

###### Definition 4.

[20] Let u ∈ Σ ∗ ⁣ ∗ u\in\Sigma^{**}. An array v ∈ Σ ∗ ⁣ ∗ v\in\Sigma^{**} is said to be a prefix of u u ( ( suffix of u u, respectively)), denoted by v ≤ p 2 ​ d u v\leq_{p}^{2d}u ( v ≤ s 2 ​ d u (v\leq_{s}^{2d}u, respectively)) if u = ( v ⊖ x) ⦶ y u=(v\ominus x)\obar y ( u = y ⦶ ( x ⊖ v) 𝐶𝐿𝑂𝑆𝐸 (u=y\obar(x\ominus v), respectively)) for some x, y ∈ Σ ∗ ⁣ ∗ x,y\in\Sigma^{**}. Furthermore, v v is said to be a proper prefix of u u ( ( proper suffix of u u, respectively)) denoted by v < p 2 ​ d u v<_{p}^{2d}u ( v < s 2 ​ d u (v<_{s}^{2d}u, respectively)) if either x ≠ Λ x\neq\Lambda or y ≠ Λ y\neq\Lambda, or both x, y ∈ Σ + ⁣ + x,y\in\Sigma^{++}.

###### Definition 5.

[21] If x ∈ Σ + ⁣ + x\in\Sigma^{++}, then by ( x k 1 ⦶) k 2 ⊖ (x^{k_{1}\obar})^{k_{2}\ominus} we mean that the array is constructed by repeating x x, k 1 k_{1} times column-wise to get x k 1 ⦶ x^{k_{1}\obar}, and repeating x k 1 ⦶ x^{k_{1}\obar}, k 2 k_{2} times row-wise. An array w ∈ Σ + ⁣ + w\in\Sigma^{++} is said to be 2D primitive if w = ( x k 1 ⦶) k 2 ⊖ w=(x^{k_{1}\obar})^{k_{2}\ominus} implies that k 1 ​ k 2 = 1 k_{1}k_{2}=1 and w = x w=x.

By Q 2 ​ d Q_{2d}, let us denote the set of all 2D primitive arrays. Also, if w = ( x k 1 ⦶) k 2 ⊖ w=(x^{k_{1}\obar})^{k_{2}\ominus} and x x is 2D primitive, then x x is said to be a 2D- primitive root of w w denoted by ρ 2 ​ d ​ ( w) \rho_{2d}(w). Note that 2D- primitive root is always unique for a given array.

###### Definition 6.

[22] Let u = [u i, j] 1 ≤ i ≤ m, 1 ≤ j ≤ n u=[u_{i,j}]_{1\leq i\leq m,1\leq j\leq n} be an array of size ( m, n) (m,n). The reverse image of u u, denoted by u R u^{R} is [u m − i + 1, n − j + 1] 1 ≤ i ≤ m, 1 ≤ j ≤ n [u_{m-i+1,n-j+1}]_{1\leq i\leq m,1\leq j\leq n}. Furthermore, if u u is equal to its reverse image u R u^{R}, then u u is said to be a two-dimensional palindrome. By P 2 ​ d P_{2d}, we denote the set of all 2D palindromes in Σ ∗ ⁣ ∗ \Sigma^{**}.

Just for completion, recall that the transpose of u = [u i, j] 1 ≤ i ≤ m, 1 ≤ j ≤ n u=[u_{i,j}]_{1\leq i\leq m,1\leq j\leq n}, denoted by u T u^{T} is defined as:

 | u T = ( u 1, 1 ⦶ u 2, 1 ⦶ ⋯ ⦶ u m, 1) ⊖ ⋯ ⊖ ( u 1, n ⦶ u 2, n ⦶ ⋯ ⦶ u m, n). \displaystyle u^{T}=(u_{1,1}\obar u_{2,1}\obar\cdots\obar u_{m,1})\ominus\cdots\ominus(u_{1,n}\obar u_{2,n}\obar\cdots\obar u_{m,n}). |  |

### 2.3 Two-dimensional Fibonacci Words

We are familiar with the Fibonacci numerical sequence F ⁡ ( n) F(n) is defined recursively as F ⁡ ( 0) = 1 F(0)=1, F ⁡ ( 1) = 1 F(1)=1, F ⁡ ( n) = F ⁡ ( n − 1) + F ⁡ ( n − 2) F(n)=F(n-1)+F(n-2) for n ≥ 2 n\geq 2. Similarly, the sequence { f n } n ≥ 0 \{f_{n}\}_{n\geq 0} of Fibonacci words over Σ = { a, b } \Sigma=\{a,b\}, is defined recursively by f 0 = a f_{0}=a, f 1 = b f_{1}=b, f n = f n − 1 ​ f n − 2 f_{n}=f_{n-1}f_{n-2} for n ≥ 2 n\geq 2. Note that the Fibonacci words are always defined over the binary alphabet and | f n | = F ⁡ ( n) |f_{n}|=F(n) for n ≥ 0 n\geq 0.

The 2D extension to Fibonacci arrays is defined in [1], as below.

###### Definition 7.

[1] Let Σ = { a, b, c, d } \Sigma=\{a,b,c,d\}. The sequence of Fibonacci arrays, { f m, n } m, n ≥ 0 \{f_{m,n}\}_{m,n\geq 0}, is defined as:

1. 1.

f 0, 0 = β, f 0, 1 = γ, f 1, 0 = δ, f 1, 1 = α f_{0,0}=\beta,f_{0,1}=\gamma,f_{1,0}=\delta,f_{1,1}=\alpha where α, β, γ \alpha,\beta,\gamma and δ \delta are symbols from Σ \Sigma with some but not all, among α, β, γ \alpha,\beta,\gamma and δ \delta might be identical.

2. 2.

For k ≥ 0 k\geq 0 and m, n ≥ 1 m,n\geq 1,

 | f k, n + 1 = f k, n ⦶ f k, n − 1, f m + 1, k = f m, k ⊖ f m − 1, k. f_{k,n+1}=f_{k,n}\obar f_{k,n-1},\hskip 5.69046ptf_{m+1,k}=f_{m,k}\ominus f_{m-1,k}. |  |

For convenience, throughout this paper we fix f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,f_{0,1}=b,f_{1,0}=c,f_{1,1}=d, where some but not all of a, b, c a,b,c and d d might be identical. Let us call f k, n + 1 = f k, n ⦶ f k, n − 1 f_{k,n+1}=f_{k,n}\obar f_{k,n-1} as column-wise expansion and f m + 1, k = f m, k ⊖ f m − 1, k f_{m+1,k}=f_{m,k}\ominus f_{m-1,k} as row-wise expansion. Example 1 explains the construction of f 2, 3 f_{2,3} in two ways. In the first way, row-wise expansions precede column-wise expansions and in the second way column-wise expansions precede row-wise expansions.

###### Example 1.

Let Σ = { a, b, c, d } \Sigma=\{a,b,c,d\}. Then,

 | f 2, 3 = f 1, 3 ⊖ f 0, 3 \displaystyle f_{2,3}=f_{1,3}\ominus f_{0,3} | = ( f 1, 2 ⦶ f 1, 1) ⊖ ( f 0, 2 ⦶ f 0, 1) \displaystyle=(f_{1,2}\obar f_{1,1})\ominus(f_{0,2}\obar f_{0,1}) |  |

 |  | = ( f 1, 1 ⦶ f 1, 0 ⦶ f 1, 1) ⊖ ( f 0, 1 ⦶ f 0, 0 ⦶ f 0, 1). \displaystyle=(f_{1,1}\obar f_{1,0}\obar f_{1,1})\ominus(f_{0,1}\obar f_{0,0}\obar f_{0,1}). |  |

Or,

 | f 2, 3 = f 2, 2 ⦶ f 2, 1 \displaystyle f_{2,3}=f_{2,2}\obar f_{2,1} | = f 2, 1 ⦶ f 2, 0 ⦶ f 2, 1 \displaystyle=f_{2,1}\obar f_{2,0}\obar f_{2,1} |  |

 |  | = ( f 1, 1 ⊖ f 0, 1) ⦶ ( f 1, 0 ⊖ f 0, 0) ⦶ ( f 1, 1 ⊖ f 0, 1). \displaystyle=(f_{1,1}\ominus f_{0,1})\obar(f_{1,0}\ominus f_{0,0})\obar(f_{1,1}\ominus f_{0,1}). |  |

Since, f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,f_{0,1}=b,f_{1,0}=c,f_{1,1}=d, f 2, 3 f_{2,3} we can write,

 | f 2, 3 = d c d b a b \displaystyle f_{2,3}=\begin{matrix}d&c&d\\ b&a&b\end{matrix} |  |

We state here some required properties of f m, n f_{m,n}.

###### Lemma 1.

[20] Let f m, n, ( m, n = 0, 1, 2, …) f_{m,n},(m,n=0,1,2,\dotsc) be the sequence of 2D Fibonacci arrays over Σ = { a, b, c, d } \Sigma=\{a,b,c,d\}, with f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,f_{0,1}=b,f_{1,0}=c,f_{1,1}=d. Also let Σ 1 = { a, b } \Sigma_{1}=\{a,b\}, Σ 2 = { c, d } \Sigma_{2}=\{c,d\}, Σ 1 ′ = { a, c } \Sigma_{1}^{\prime}=\{a,c\} and Σ 2 ′ = { b, d } \Sigma_{2}^{\prime}=\{b,d\} such that Σ = Σ 1 ∪ Σ 2 = Σ 1 ′ ∪ Σ 2 ′ \Sigma=\Sigma_{1}\cup\Sigma_{2}=\Sigma_{1}^{\prime}\cup\Sigma_{2}^{\prime}. Then,

- a.

Any row of f m, n f_{m,n} is a 1D Fibonacci word over either Σ 1 \Sigma_{1} or Σ 2 \Sigma_{2}.

- b.

If Σ 1 ≠ Σ 2 \Sigma_{1}\neq\Sigma_{2} then all the rows of f m, n f_{m,n}, over Σ 1 \Sigma_{1} are identical and all the rows of f m, n f_{m,n}, over Σ 2 \Sigma_{2} are identical.

- c.

Any column of f m, n f_{m,n} is a 1D Fibonacci word over either Σ 1 ′ \Sigma_{1}^{\prime} or Σ 2 ′ \Sigma_{2}^{\prime}.

- d.

If Σ 1 ′ ≠ Σ 2 ′ \Sigma_{1}^{\prime}\neq\Sigma_{2}^{\prime} then all the columns of f m, n f_{m,n}, over Σ 1 ′ \Sigma_{1}^{\prime} are identical and all the columns of f m, n f_{m,n}, over Σ 2 ′ \Sigma_{2}^{\prime} are identical.

- e.

If Σ 1 = Σ 2 ​ ( Σ 1 ′ = Σ 2 ′) \Sigma_{1}=\Sigma_{2}(\Sigma_{1}^{\prime}=\Sigma_{2}^{\prime}), then either all the rows ( ( columns)) of f m, n f_{m,n} are identical or a set of rows are identical and are complementary to the set of remaining rows ( ( columns, respectively)) which are identical.

For more properties of 2D Fibonacci words the reader can refer [20] and [23].

## 3 Tandem Repeats in f m, n f_{m,n}

In molecular genetics, data is represented as a sequence of characters. Many algorithms in molecular biology try to find structures called tandems, which are patterns of nucleotides repeated adjacent to each other in a DNA. In fact more than half of the human genome contains repeated sequences [24, 25]. They are related to inherited traits of an individual and play a role in DNA tests. Even an approximate tandem repeat is related to some human diseases [26]. Tandem repeats in 2 ​ D 2D words were studied in [1, 11, 10, 12] with varying interests.

### 3.1 Types of Tandems

###### Definition 8.

[1] In a two dimensional array X X, a tandem is a configuration consisting of two occurrences of a same primitive block W W that touch each other with one side( T ​ y ​ p ​ e ​ I Type~I tandem) or with a corner( T ​ y ​ p ​ e ​ I ​ I Type~II tandem).

We further divide Type I and Type II tandems as defined below.

###### Definition 9.

Let u u be a 2D word. For a primitive block W W, the T ​ y ​ p ​ e ​ I Type~I tandem W ⦶ W W\obar W is called a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem of u u and W ⊖ W W\ominus W is called a T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem of u u.

###### Definition 10.

Let u u be a 2D word. For a primitive block W W which is a subarray of u u, and for A A, B ∈ Σ + ⁣ + B\in\Sigma^{++}, whose sizes are the same as that of W W, if the T ​ y ​ p ​ e ​ I ​ I Type~II tandem is such that ( W ⦶ A) ⊖ ( B ⦶ W) (W\obar A)\ominus(B\obar W) is a sub array of u u, then it is called a T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandem of u u. And if the T ​ y ​ p ​ e ​ I ​ I Type~II tandem is such that ( C ⦶ W) ⊖ ( W ⦶ D) (C\obar W)\ominus(W\obar D) is a sub array of u u, for some C C, D ∈ Σ + ⁣ + D\in\Sigma^{++}, whose sizes are the same as that of W W, then it is called a T ​ y ​ p ​ e ​ I ​ I ​ ( b) Type~II(b) tandem of u u.

All the four types of tandems are shown in Figure 1.

[image: Refer to caption] Figure 1: Types of tandems that can occur in a two-dimensional array

###### Remarks.

Block W W is called the root of the tandem. A tandem need not be a 2D array. Also note that, T ​ y ​ p ​ e ​ I ​ ( b) ​ ( T ​ y ​ p ​ e ​ I ​ I ​ ( b) 𝐶𝐿𝑂𝑆𝐸 Type~I(b)~(Type~II(b), respectively)) tandem will be a 90 ∘ 90^{\circ} rotation of T ​ y ​ p ​ e ​ I ​ ( a) ​ ( T ​ y ​ p ​ e ​ I ​ I ​ ( a) 𝐶𝐿𝑂𝑆𝐸 Type~I(a)~(Type~II(a), respectively)) and vice versa.

Formulas to count the exact number of squares including repetitions and without including repetitions(i.e. distinct) are established in [27]. Both the theorems are recalled here. Note that, there is a corrigendum [28] to [27] correcting an error in the formula for number of squares, derived in [27]. The correct formula was verified in [29] also, using a logic-based decision procedure, implemented as W ​ a ​ l ​ n ​ u ​ t Walnut.

Denote by D ⁡ ( n) D(n) and by R ⁡ ( n) R(n) the exact number of distinct and repeated squares, respectively, in f n f_{n}. Then,

###### Theorem 1.

[27] For n ≥ 5 n\geq 5, D ⁡ ( n) = 2 ​ ( F ⁡ ( n − 2) − 1) D(n)=2(F(n-2)-1).

###### Theorem 2.

[28] For n ≥ 3 n\geq 3, R ⁡ ( n) = 4 5 ​ n ​ F ​ ( n) − 2 5 ​ ( n + 6) ​ F ​ ( n − 1) − 4 ​ F ​ ( n − 2) + n + 1 R(n)=\frac{4}{5}nF(n)-\frac{2}{5}(n+6)F(n-1)-4F(n-2)+n+1.

## 4 Number of Tandems of f m, n f_{m,n}

In this section we count the number of tandems (with repetition included, i.e. same tandems, but positioned at different locations are included in the counting) in the given Fibonacci array f m, n f_{m,n}.

### 4.1 The number of T ​ y ​ p ​ e ​ I Type~I Tandems in the Fibonacci Array f m, n f_{m,n}

First we prove two Propositions to help our counting.

###### Proposition 1.

Let S S be a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem of size ( r, c) (r,c), with r ≥ 1 r\geq 1 and c ≥ 2 c\geq 2 is even. Then there are r ⁡ ( r + 1) 2 \frac{r(r+1)}{2} number of T ​ y ​ p ​ e ​ I ​ ( a) TypeI(a) tandems in S S.

###### Proof.

Observe that if S S is a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem, then every row of S S will be a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem. Conversely, if every row of an array is a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem then the array itself will be a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem.

Denote the top left corner of S S as position [1, 1] [1,1]. Consider the T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem, S 1 S_{1}, with r r rows, and c c columns, located at [1, 1] [1,1] (i.e. S 1 = S S_{1}=S itself). The sub arrays of S 1 S_{1} consisting of its first i i rows alone, 1 ≤ i ≤ r 1\leq i\leq r, will be T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems of sizes ( i, c) (i,c). Hence there are r r tandems, located at [1, 1] [1,1]. Now consider the tandem, S 2 S_{2}, with ( r − 1) (r-1) rows, located at [2, 1] [2,1]. The sub arrays of S 2 S_{2} consisting of its first i i rows alone, 1 ≤ i ≤ r − 1 1\leq i\leq r-1 will be T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems of sizes ( i, c) (i,c). Hence there are r − 1 r-1 tandems, located at [2, 1] [2,1]. Continuing this process we get r + ( r − 1) + ⋯ + 1 = r ⁡ ( r + 1) 2 r+(r-1)+\cdots+1=\frac{r(r+1)}{2} T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems in S S. ∎

###### Proposition 2.

Let S S be a T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem of size ( r, c) (r,c), with c ≥ 1 c\geq 1 and r ≥ 2 r\geq 2 is even. Then there are c ⁡ ( c + 1) 2 \frac{c(c+1)}{2} number of T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandems in S S.

###### Proof.

The proof is similar to the proof of Proposition 1. ∎

Now through a combinatorial argument we can count the number of T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) and T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandems in f m, n f_{m,n}.

###### Theorem 3.

For m ≥ 1 m\geq 1 and n ≥ 3 n\geq 3, let R ⁡ ( m, n, I ⁡ ( a)) R(m,n;I(a)) denote the exact number of T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems occurring in f m, n f_{m,n}. Then,

R ⁡ ( m, n, I ⁡ ( a)) = R ⁡ ( n) ​ F ​ ( m) ​ ( F ​ ( m) + 1) 2 R(m,n;I(a))=R(n)\frac{F(m)(F(m)+1)}{2},

where R ⁡ ( n) R(n) is the number of squares in the Fibonacci word f n f_{n} (see Theorem 2).

###### Proof.

Due to the characteristics of f m, n f_{m,n}, as mentioned in the Lemma 1, if there is a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem (square) of length 2 ​ l 2l, 1 ≤ l ≤ ⌊ F ⁡ ( n) 2 ⌋ 1\leq l\leq\lfloor\frac{F(n)}{2}\rfloor in the first row, occurring at the position [1, s], 1 ≤ s ≤ F ⁡ ( n) − 1 [1,s],1\leq s\leq F(n)-1, then there will be squares of the same length 2 ​ l 2l, at the positions [i, s] [i,s] for all 2 ≤ i ≤ F ⁡ ( m) 2\leq i\leq F(m). Therefore, there will be a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem of size ( F ⁡ ( m), 2 ​ l) (F(m),2l) located at [1, s] [1,s]. Now by Proposition 1, we get F ​ ( m) ​ ( F ​ ( m) + 1) 2 \frac{F(m)(F(m)+1)}{2} number of T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems from this tandem. Note that, for every square present in the first row of f m, n f_{m,n}, we get F ​ ( m) ​ ( F ​ ( m) + 1) 2 \frac{F(m)(F(m)+1)}{2} number of T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems.

By Theorem 2, we have,

 | R ⁡ ( n) = 4 5 ​ n ​ F n − 2 5 ​ ( n + 6) ​ F n − 1 − 4 ​ F n − 2 + n + 1 R(n)=\frac{4}{5}nF_{n}-\frac{2}{5}(n+6)F_{n-1}-4F_{n-2}+n+1~ |  |

number of squares present in the first row of f m, n f_{m,n}. Hence, f m, n f_{m,n} has R ⁡ ( n) ​ F ​ ( m) ​ ( F ​ ( m) + 1) 2 R(n)\frac{F(m)(F(m)+1)}{2} number of T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems. ∎

###### Theorem 4.

For m ≥ 3 m\geq 3 and n ≥ 1 n\geq 1, Let R ⁡ ( m, n, I ⁡ ( b)) R(m,n;I(b)) denote the exact number of T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandems occurring in f m, n f_{m,n}. Then,

R ⁡ ( m, n, I ⁡ ( b)) = R ⁡ ( m) ​ F ​ ( n) ​ ( F ​ ( n) + 1) 2 R(m,n;I(b))=R(m)\frac{F(n)(F(n)+1)}{2},

where R ⁡ ( m) R(m) is the number of squares in the Fibonacci word f m f_{m} (see Theorem 2)

###### Proof.

The proof is similar to the proof of Theorem 3. ∎

### 4.2 The Number T ​ y ​ p ​ e ​ I ​ I Type~II Tandems in the Fibonacci Array f m, n f_{m,n}

In this section we count the number of T ​ y ​ p ​ e ​ I ​ I Type~II tandems (repetition included) in the given Fibonacci array f m, n f_{m,n}.

###### Proposition 3.

Let Σ = { a, b, c, d } \Sigma=\{a,b,c,d\} be the alphabet. Let A, B, C, D ∈ Σ + ⁣ + A,B,C,D\in\Sigma^{++} be arrays of same size such that ( A ⦶ B) ⊖ ( C ⦶ D) (A\obar B)\ominus(C\obar D) is a sub array of f m, n f_{m,n}. Then, A = D = W A=D=W (i.e. a T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandem occurs) iff A = B = C = D = W A=B=C=D=W.

###### Proof.

If A = B = C = D = W A=B=C=D=W, then obviously there occurs a T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandem. Conversely, Let A = D = W A=D=W (i.e. a T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandem occurs) in ( A ⦶ B) ⊖ ( C ⦶ D) (A\obar B)\ominus(C\obar D). Then A A and D D have identical first rows over a same alphabet say Σ ′ ⊂ Σ \Sigma^{\prime}\subset\Sigma. By Lemma 1, the first rows of ( A ⦶ B) (A\obar B) and ( C ⦶ D) (C\obar D) will be identical. A similar argument on the other rows show that A = B = C = D = W A=B=C=D=W. ∎

###### Definition 11.

[1] Given a 2D array X X, a quartic in X X is a configuration consisting of the form W W W W W W W W where block W W is primitive.

From Proposition 3 and Definition 11 we infer that, in Fibonacci arrays, T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandems occur only as a part of quartics. Hence, the number of T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandems in a Fibonacci array equals the number of quartics in the Fibonacci array. In the next theorem we count the number of quartics and hence the number of T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandems.

###### Theorem 5.

For m, n ≥ 3 m,n\geq 3, let R ⁡ ( m), R ⁡ ( n) R(m),R(n) denote the number of squares ( ( repetitions included)) in the Fibonacci words f m, f n f_{m},f_{n} respectively. Then, there are R ⁡ ( m) ​ R ​ ( n) R(m)R(n) quartics in the Fibonacci array f m, n f_{m,n} and hence there are as many T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandems in f m, n f_{m,n}.

###### Proof.

We know that, every row of a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem will be a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem and every column of T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem will be a T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem. Since a quartic is both a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) and a T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem, only the sub arrays having the intersection of a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem and a T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem as its domain, can be quartics of f m, n f_{m,n}. In fact a T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandem of size ( F ⁡ ( m), 2 ​ l) (F(m),2l), 1 ≤ l ≤ ⌊ F ⁡ ( n) 2 ⌋ 1\leq l\leq\lfloor\frac{F(n)}{2}\rfloor and a T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandem of size ( 2 ​ k, F ⁡ ( n)) (2k,F(n)), 1 ≤ k ≤ ⌊ F ⁡ ( m) 2 ⌋ 1\leq k\leq\lfloor\frac{F(m)}{2}\rfloor will create a quartic of size ( 2 ​ k, 2 ​ l) (2k,2l) (Refer Figure 2). Now, as there are R ⁡ ( m), R ⁡ ( n) R(m),R(n) number squares, respectively, in the Fibonacci words f m, f n f_{m},f_{n} there will be R ⁡ ( m) R(m) number of squares in the first column and R ⁡ ( n) R(n) number of squares the first row of f m, n f_{m,n}. Hence, there will be R ⁡ ( m) ​ R ​ ( n) R(m)R(n) quartics in the Fibonacci array f m, n f_{m,n}. Therefore by proposition 3 there are as many T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandems in f m, n f_{m,n}. (Values of R ⁡ ( m) R(m) and R ⁡ ( n) R(n) are given in proposition 1 as derived in [27]) . ∎

[image: Refer to caption] Figure 2: Formation of a quartic

###### Theorem 6.

There are R ⁡ ( m) ​ R ​ ( n) R(m)R(n) number of T ​ y ​ p ​ e ​ I ​ I ​ ( b) Type~II(b) tandems in f m, n f_{m,n}.

###### Proof.

Like T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) tandems, a T ​ y ​ p ​ e ​ I ​ I ​ ( b) Type~II(b) tandem can occur as a part of some quartic only. Hence the number of T ​ y ​ p ​ e ​ I ​ I ​ ( b) Type~II(b) tandems will be the same as the number of quartics in f m, n f_{m,n}. Hence by the Theorem 5 there will be R ⁡ ( m) ​ R ​ ( n) R(m)R(n) number of T ​ y ​ p ​ e ​ I ​ I ​ ( b) Type~II(b) tandems in f m, n f_{m,n}. ∎

## 5 Number of Distinct Factors of f n f_{n}

We derive an important result of factor complexity of finite 1D Fibonacci words here. This will help us to count the distinct T ​ y ​ p ​ e ​ I Type~I, T ​ y ​ p ​ e ​ I ​ I Type~II tandems in f n f_{n} and f m, n f_{m,n}. Analysing the factor complexity of an infinite word is crucial as we can conclude many things about the nature of the word. For an infinite word u u, the factor complexity function is bounded if u u is ultimately periodic. Conversely, u u will be ultimately periodic, if p n ​ ( u) ≤ n p_{n}(u)\leq n for some n n [30]. Balanced words, Sturmian words, Arnoux-Rauzy word over a ternary alphabet all have been characterised through their complexity functions. Entropy of an infinite word and unavoidable patterns in an infinite word are also closely related to the concept complexity function.

###### Definition 12.

[17] For an infinite word w w, the subword complexity function of w w, p w ​ ( n) p_{w}(n), counts the number of distinct subwords of length n n in w w. The subword complexity sequence of w w is the sequence p w = ( p w ​ ( 1), p w ​ ( 2), p w ​ ( 3), …) p_{w}=(p_{w}(1),p_{w}(2),p_{w}(3),\dotsc).

Recall that, the 1D infinite Fibonacci word [17],

 | f ∞ = lim n → ∞ h n ( a) = h ω ( a) = b a b b a b a b ⋯ ⋯ f_{\infty}=\lim_{n\to\infty}h^{n}(a)=h^{\omega}(a)=babbabab\cdots\cdots |  |

is the fixed point of the morphism h ⁡ ( a) = b, h ⁡ ( b) = b ​ a h(a)=b,h(b)=ba on Σ = { a, b } \Sigma=\{a,b\}.

###### Proposition 4.

[17] The subword complexity function of f ∞ f_{\infty} is p f ∞ ​ ( n) = n + 1 p_{f_{\infty}}(n)=n+1. That is the infinite Fibonacci word has exactly n + 1 n+1 factors of length n n.

Proposition 4 says that the 1D infinite Fibonacci word f ∞ f_{\infty} has exactly n + 1 n+1 factors of length n n for any n ≥ 1 n\geq 1. This characterisation itself is sometimes used as the definition of 1D Fibonacci words (in fact the broad category of 1D Sturmian words). Though the count for distinct factors ( ( of any length)) of the infinite Fibonacci word is already available, the count for the number of distinct factors of the finite Fibonacci word f n f_{n}, n ≥ 2 n\geq 2, is not available. In this section we derive a formula for this count. Later we use it to count the number of distinct tandems in a given 2D Fibonacci array, f m, n f_{m,n}.

We recall the following theorem regarding the positions of all the distinct factors of length k ≥ 1 k\geq 1, of f ∞ = f f_{\infty}=f.

###### Theorem 7.

[31] Let n ≥ 2 n\geq 2 and F ⁡ ( n) ≤ k < F ⁡ ( n + 1) F(n)\leq k<F(n+1). Define

 | z j ( k) = { f ⁡ [j + 1; k], 0 ≤ j ≤ F ⁡ ( n) − 1 f ⁡ [j + F ⁡ ( n + 1) − k; k], F ⁡ ( n) ≤ j ≤ k z_{j}^{(k)}=\begin{cases}f[j+1;k],&0\leq j\leq F(n)-1\\ f[j+F(n+1)-k;k],&F(n)\leq j\leq k\end{cases} |  |

where f ⁡ [i ′; j ′] f[i^{\prime};j^{\prime}], j ′ ≥ i ′ j^{\prime}\geq i^{\prime} is the sub word of f f of length j ′ j^{\prime} starting at position i ′ i^{\prime}. Then the words z 0 ( k) z_{0}^{(k)}, z 1 ( k) z_{1}^{(k)}, ⋯ \cdots, z k ( k) z_{k}^{(k)} are the k + 1 k+1 distinct factors of f f of length k k which are listed in the order of their first occurrences in f f.

We now state and prove one of the major theorems of this paper, related to the factor complexity of f n f_{n}.

###### Theorem 8.

For n ≥ 2 n\geq 2, let p k ​ ( f n) p_{k}(f_{n}) denote the number of distinct subwords of length k k, 1 ≤ k ≤ F ⁡ ( n) 1\leq k\leq F(n) in f n f_{n}. Then,

 | p k ​ ( f n) = { k + 1, 1 ≤ k ≤ F ⁡ ( n − 2) F ⁡ ( n − 2) + 2, F ⁡ ( n − 2) + 1 ≤ k ≤ F ⁡ ( n − 1) − 1 F ⁡ ( n) + 1 − k, F ⁡ ( n − 1) ≤ k ≤ F ⁡ ( n) p_{k}(f_{n})=\begin{cases}k+1~,&1\leq k\leq F(n-2)\\ F(n-2)+2~,&F(n-2)+1\leq k\leq F(n-1)-1\\ F(n)+1-k~,&F(n-1)\leq k\leq F(n)\end{cases} |  |

Given f n f_{n}, proof is done in three cases.

Table 1 lists the number of distinct factors of various lengths that occur in f n f_{n} for n = 2, 3, 4, 5, 6 n=2,3,4,5,6.

Table 1: Number of distinct factors of various lengths occurring in f n f_{n}

Factor Length → \rightarrow | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

f n f_{n} and F ⁡ ( n) F(n) ↓ \downarrow |  |  |  |  |  |  |  |  |  |  |  |  |  |

f 2 f_{2}, F ⁡ ( 2) = 2 F(2)=2 | 2 | 1 |  |  |  |  |  |  |  |  |  |  |  |

f 3 f_{3}, F ⁡ ( 3) = 3 F(3)=3 | 2 | 2 | 1 |  |  |  |  |  |  |  |  |  |  |

f 4 f_{4}, F ⁡ ( 4) = 5 F(4)=5 | 2 | 3 | 3 | 2 | 1 |  |  |  |  |  |  |  |  |

f 5 f_{5}, F ⁡ ( 5) = 8 F(5)=8 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |  |  |  |  |  |

f 6 f_{6}, F ⁡ ( 6) = 13 F(6)=13 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

###### Corollary 1.

For n ≥ 2 n\geq 2, let p ⁡ ( f n) p(f_{n}) denote the number of distinct subwords of f n f_{n}. Then p ⁡ ( f n) = ∑ k = 1 F ⁡ ( n) p k ​ ( f n) p(f_{n})=\sum_{k=1}^{F(n)}p_{k}(f_{n}).

###### Proof.

As p k ​ ( f n) p_{k}(f_{n}) denote the number of distinct subwords of length k k in f n f_{n}, summation over k k yields the value of p ⁡ ( f n) p(f_{n}). ∎

## 6 Number of Distinct Tandems of f m, n f_{m,n}

We use the result obtained in Theorem 8 to count the number of distinct tandems in f m, n f_{m,n}.

Recall from Theorem 1 that, For n ≥ 5 n\geq 5, D ⁡ ( n) = 2 ​ ( F ⁡ ( n − 2) − 1) D(n)=2(F(n-2)-1), where D ⁡ ( n) D(n) denotes the exact number of distinct squares in f n f_{n}.

### 6.1 The Number of Distinct T ​ y ​ p ​ e ​ I Type~I Tandems in f m, n f_{m,n}

###### Theorem 9.

For m ≥ 2 m\geq 2 and n ≥ 5 n\geq 5, let D ⁡ ( m, n, I ⁡ ( a)) D(m,n;I(a)) denote the exact number of distinct T ​ y ​ p ​ e ​ I ​ ( a) Type~I(a) tandems occurring in f m, n f_{m,n}. Then,

D ⁡ ( m, n, I ⁡ ( a)) = D ⁡ ( n) ​ p ​ ( f m) D(m,n;I(a))=D(n)~p(f_{m}).

###### Proof.

The counting process is very similar to the process explained in the proof of Theorem 3, except that, we have to consider only the distinct squares in the first row and the distinct factors of the first column. Hence by Theorem 1 (number of distinct squares in any row) and Corollary 1 (number of distinct factors in f m f_{m}), the result follows. ∎

###### Theorem 10.

For m ≥ 5 m\geq 5 and n ≥ 2 n\geq 2, let D ⁡ ( m, n, I ⁡ ( b)) D(m,n;I(b)) denote the exact number of distinct T ​ y ​ p ​ e ​ I ​ ( b) Type~I(b) tandems occurring in f m, n f_{m,n}. Then,

D ⁡ ( m, n, I ⁡ ( b)) = D ⁡ ( m) ​ p ​ ( f n) D(m,n;I(b))=D(m)~p(f_{n}).

###### Proof.

The proof is similar to the proof of Theorem 9 with the roles of m m and n n interchanged. ∎

### 6.2 The Number of Distinct T ​ y ​ p ​ e ​ I ​ I Type~II Tandems in f m, n f_{m,n}

In this section we count the number of distinct T ​ y ​ p ​ e ​ I ​ I Type~II tandems in f m, n f_{m,n}.

###### Theorem 11.

For m, n ≥ 3 m,n\geq 3, let D ⁡ ( m), D ⁡ ( n) D(m),D(n) denote the number distinct squares in the Fibonacci words f m, f n f_{m},f_{n} respectively. Then, there are D ⁡ ( m) ​ D ​ ( n) D(m)D(n) distinct quartics in the Fibonacci array f m, n f_{m,n}; and hence there are as many distinct T ​ y ​ p ​ e ​ I ​ I ​ ( a) Type~II(a) and T ​ y ​ p ​ e ​ I ​ I ​ ( b) Type~II(b) tandems in f m, n f_{m,n}.

###### Proof.

The proof is similar to Theorem 5 except that only distinct squares are considered in the counting. ∎

## 7 The 2D Infinite Fibonacci Word, f ∞, ∞ f_{\infty,\infty}

We know that, a morphism is a map h: Σ ∗ → Δ ∗ h:\Sigma^{*}\rightarrow\Delta^{*}, where Σ \Sigma, Δ \Delta are alphabets, such that h ⁡ ( x ​ y) = h ⁡ ( x) ​ h ​ ( y) h(xy)=h(x)h(y) for all strings x, y ∈ Σ ∗ x,y\in\Sigma^{*}. If Σ = Δ \Sigma=\Delta we can iterate h h. That is h n ​ ( x) = h ⁡ ( h n − 1 ​ ( x)), n ≥ 2 h^{n}(x)=h(h^{n-1}(x)),n\geq 2. In the literature, analysis of the Fibonacci language, { f n } n ≥ 0 \{f_{n}\}_{n\geq 0}, over the alphabet Σ = { a, b } \Sigma=\{a,b\}, is done with the help of the Fibonacci morphism, h: a → b, b → b ​ a h:a\rightarrow b,b\rightarrow ba. That is to say that, the infinite Fibonacci word 𝐟 ∞ = b a b b a b a b b a b b a ⋯ \mathbf{f_{\infty}}=babbababbabba\cdots is the limit of the sequence { f n } n ≥ 0 \{f_{n}\}_{n\geq 0}. That is,

 | f ∞ = lim n → ∞ h n ( a) = h ω ( a) = b a b b a b a b ⋯ ⋯ f_{\infty}=\lim_{n\to\infty}h^{n}(a)=h^{\omega}(a)=babbabab\cdots\cdots |  |

is the fixed point of the morphism h ⁡ ( a) = b, h ⁡ ( b) = b ​ a h(a)=b,h(b)=ba on Σ = { a, b } \Sigma=\{a,b\}.

Also, note that, finitely many iterations of the above morphism ( h ⁡ ( a) = b, h ⁡ ( b) = b ​ a h(a)=b,h(b)=ba) generates the intermediate finite Fibonacci words, f n f_{n} for all n ≥ 0 n\geq 0, ultimately leading to f ∞ f_{\infty}, the fixed point of the morphism, when n → ∞ n\rightarrow\infty.

### 7.1 d − d- dimensional Morphisms

Similar to f ∞ f_{\infty} we define f ∞, ∞ f_{\infty,\infty}, the 2D infinite Fibonacci word. It is noted that, the concept of two dimensional iterated morphisms was first introduced in [32]. But, such morphisms might not always result in rectangular patterns. Interestingly, in [33], d − d- dimensional morphisms are introduced and using them d − d- dimensional infinite words are defined. After stating the required definitions and results from [33, 34], we will define and validate the 2D morphism generating f ∞, ∞ f_{\infty,\infty}. As a continuation, in section 9, we construct a DFAO (Deterministic Finite Automaton with Output) which generates f ∞, ∞ f_{\infty,\infty}.

### 7.2 The 2D Fibonacci Morphism

Now, we state and prove another important theorem of this paper. Consider the case d = 2 d=2 in [33].

###### Definition 13.

Let μ: Σ → B 2 ​ ( Σ) \mu:\Sigma\rightarrow B_{2}(\Sigma) be a map and x x be a 2-dimensional array such that,

 | ∀ i ∈ ⟦ 1, 2 ⟧, ∀ k < | x | i, ∀ a, b ∈ F a c t 1 ( x | i, k): | μ ( a) | i = | μ ( b) | i. \forall i\in\llbracket 1,2\rrbracket,\forall k<|x|_{i},\forall a,b\in Fact_{\textbf{1}}(x_{|i,k}):|\mu(a)|_{i}=|\mu(b)|_{i}. |  | (1) |

Then the image of x by μ \mu is the 2-dimensional array defined as,

 | μ ( x) = ⊙ 0 ≤ n 1 < | x | 1 1 ( ⊙ 0 ≤ n 2 < | x | 2 2 μ ( x ( n 1, n 2))). \mu(x)=\odot_{0\leq n_{1}<|x|_{1}}^{1}\left(\odot_{0\leq n_{2}<|x|_{2}}^{2}\mu(x(n_{1},n_{2}))\right). |  |

If for all a ∈ Σ a\in\Sigma and all n ≥ 1 n\geq 1, μ n − 1 ​ ( a) \mu^{n-1}(a) satisfies ( 1), then μ \mu is said to be a 2-dimensional morphism. Further, the properties of μ \mu being prolongable on a a and μ \mu having a fixed point, follow automatically.

Now, consider the map,

 | μ: d → d c b a, c → d b, b → d c, a → d. \mu:~~d\rightarrow\begin{matrix}d&c\\ b&a\end{matrix},~~c\rightarrow\begin{matrix}d\\ b\end{matrix},~~b\rightarrow\begin{matrix}d&c\end{matrix},~~~a\rightarrow d. |  | (2) |

We have written in the order d, c, b, a d,c,b,a as ( μ ⁡ ( d)) 0 = d (\mu(d))_{\textbf{0}}=d (i.e. as μ \mu is prolongable on d d).

The following result is proved by induction technique.

###### Theorem 12.

Let f 0, 0 = a, f 0, 1 = b, f 1, 0 = c, f 1, 1 = d f_{0,0}=a,~f_{0,1}=b,~f_{1,0}=c,~f_{1,1}=d and μ \mu be defined as in ( 2). Then for m, n ≥ 1, m,n\geq 1,

 | μ ⁡ ( f m, n) = f m + 1, n + 1. \mu(f_{m,n})=f_{m+1,n+1}. |  |

###### Corollary 2.

For n ≥ 1, μ ⁡ ( f n, n) = f n + 1, n + 1. n\geq 1,~~\mu(f_{n,n})=f_{n+1,n+1}.

###### Proof.

By taking m = n m=n in the theorem, the corollary follows. ∎

###### Corollary 3.

w = μ ω ​ ( d) w=\mu^{\omega}(d) exists.

###### Proof.

Since, μ ⁡ ( f n, n) = f n + 1, n + 1 \mu(f_{n,n})=f_{n+1,n+1}, μ n ​ ( d) \mu^{n}(d) is inductively well defined from μ n − 1 ​ ( d) \mu^{n-1}(d) and hence μ \mu is a 2D morphism. Now, since ( μ ⁡ ( d)) 0 = d (\mu(d))_{\textbf{0}}=d, μ \mu is prolongable on d d, and

 | w = lim n → + ∞ μ n ​ ( d) = μ ω ​ ( d) w=\lim_{n\rightarrow+\infty}\mu^{n}(d)=\mu^{\omega}(d) |  |

exists. This fixed point w w is called the infinite 2D Fibonacci word and is denoted by f ∞, ∞ f_{\infty,\infty}. ∎

First few iterations of μ \mu on d d are shown below.

 | d → d c b a → d c d b a b d c d → d c d d c b a b b a d c d d c d c d d c b a b b a → d c d d c d c d ⋯ b a b b a b a b ⋯ d c d d c d c d ⋯ d c d d c d c d ⋯ b a b b a b a b ⋯ d c d d c d c d ⋯ b a b b a b a b ⋯ d c d d c d c d ⋯ ⋱ d\rightarrow\begin{matrix}d&c\\ b&a\end{matrix}\rightarrow\begin{matrix}d&c&d\\ b&a&b\\ d&c&d\end{matrix}\rightarrow\begin{matrix}d&c&d&d&c\\ b&a&b&b&a\\ d&c&d&d&c\\ d&c&d&d&c\\ b&a&b&b&a\\ \end{matrix}\rightarrow\begin{matrix}d&c&d&d&c&d&c&d&\cdots\\ b&a&b&b&a&b&a&b&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ b&a&b&b&a&b&a&b&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ b&a&b&b&a&b&a&b&\cdots\\ d&c&d&d&c&d&c&d&\cdots\\ \vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\vdots&\ddots\end{matrix} |  |

### 7.3 2D Finite Fibonacci Words as Morphic Words

As μ ⁡ ( f m, n) = f m + 1, n + 1 \mu(f_{m,n})=f_{m+1,n+1}, it is interesting to note that, the morphism μ \mu behaves like a shift operator. Hence, iterated applications of μ \mu on f 1, n ′ f_{1,n^{\prime}} or f m ′, 1 f_{m^{\prime},1} with appropriate m ′, n ′ m^{\prime},n^{\prime} values, can generate any finite 2D Fibonacci word.

###### Corollary 4.

Let m, n ≥ 2 m,n\geq 2 and m ≠ n m\neq n. Then, we have

 | f m, n = { μ ( m − 1) ​ ( f 1, n − m + 1) if ​ m < n μ ( n − 1) ​ ( f m − n + 1, 1) if ​ m > n f_{m,n}=\left\{\begin{array}[]{ll}\mu^{(m-1)}(f_{1,n-m+1})&\mbox{if }m<n\\ \\ \mu^{(n-1)}(f_{m-n+1,1})&\mbox{if }m>n\end{array}\right. |  |

###### Proof.

We know that the 2D Fibonacci words f 1, n ′ f_{1,n^{\prime}} and f m ′, 1 f_{m^{\prime},1} for any m ′, n ′ ≥ 2 m^{\prime},n^{\prime}\geq 2 can be easily obtained, as they are literally 1D Fibonacci words over { d, c } \{d,c\} and { d, b } \{d,b\} respectively.

Now, since μ ⁡ ( f m, n) = f m + 1, n + 1 \mu(f_{m,n})=f_{m+1,n+1}, for k ≥ 1, μ k ​ ( f m, n) = f m + k, n + k k\geq 1,~\mu^{k}(f_{m,n})=f_{m+k,n+k}.

Therefore,

 | if ​ m < n, μ ( m − 1) ​ ( f 1, n − m + 1) = f 1 + m − 1, n − m + 1 + m − 1 = f m, n and if ​ m > n, μ ( n − 1) ​ ( f m − n + 1, 1) = f m − n + 1 + n − 1, 1 + n − 1 = f m, n. \begin{array}[]{ll}~~\mbox{if }~m<n,&\mu^{(m-1)}(f_{1,n-m+1})=f_{1+m-1,n-m+1+m-1}=f_{m,n}~~~~\mbox{and }\\ \\ ~~\mbox{if }~m>n,&\mu^{(n-1)}(f_{m-n+1,1})=f_{m-n+1+n-1,1+n-1}=f_{m,n}.\end{array} |  |

∎

###### Example 2.

Suppose we want to generate f 3, 5 f_{3,5}.

Since n > m n>m, n − m ≥ 1 n-m\geq 1 and we start with f 1, n − m + 1 = f 1, 3 = d ​ c ​ d f_{1,n-m+1}=f_{1,3}=d~c~d, so that, μ 2 ​ ( f 1, 3) \mu^{2}(f_{1,3}) will be f 3, 5 f_{3,5}.

 | μ 2 ​ ( f 1, 3) = μ 2 ​ ( d ​ c ​ d) \displaystyle\mu^{2}(f_{1,3})=\mu^{2}(d~c~d) | = μ ⁡ ( d c d d c b a b b a) \displaystyle=\mu\left(\begin{matrix}d&c&d&d&c\\ b&a&b&b&a\end{matrix}\right) |  |

 |  | = d c d d c d c d b a b b a b a b d c d d c d c d = f 3, 5. \displaystyle=\begin{matrix}d&c&d&d&c&d&c&d\\ b&a&b&b&a&b&a&b\\ d&c&d&d&c&d&c&d\end{matrix}=f_{3,5}. |  |

## 8 Factor Complexities of f ∞, ∞ f_{\infty,\infty} and f m, n f_{m,n}

In this section we find the number of distinct subwords of any given f m, n f_{m,n} and also of f ∞, ∞ f_{\infty,\infty}. The result proved in Theorem 8, will be used to find the factor complexity of f m, n f_{m,n}. We denote by p k, l ​ ( u) p_{k,l}(u), the complexity function of the two dimensional word u u. It is understood through the subscripts k k and l l that u u is a two dimensional word.

###### Proposition 5.

For u u, a 2D word over Σ \Sigma, let p k, l ​ ( u), k, l ≥ 1 p_{k,l}(u),~k,l\geq 1 denote the number of subwords (subarrays) of u u of size ( k, l) (k,l). Then, for the two dimensional infinite Fibonacci word, f ∞, ∞ f_{\infty,\infty}, p k, l ​ ( f ∞, ∞) = ( k + 1) ​ ( l + 1) p_{k,l}(f_{\infty,\infty})=(k+1)(l+1).

###### Proof.

The result is immediate through a simple combinatorial argument. By lemma 1, every row (every column) of f ∞, ∞ f_{\infty,\infty} written as a 1D word is an 1D infinite Fibonacci word f ∞ f_{\infty} over any one of the two letter alphabets { d, c }, { b, a } ​ ( { d, b }, { c, a }) \{d,c\},\{b,a\}(\{d,b\},\{c,a\}). By proposition 4, there are k + 1 k+1 distinct subwords of length k k in every column (we call them, vertical factors) and l + 1 l+1 distinct subwords of length l l in every row (we call them, horizontal factors). Since there are only two distinct columns (one over { d, b } \{d,b\} and one over { c, a } \{c,a\}) in f ∞, ∞ f_{\infty,\infty}, there are 2 ​ ( k + 1) 2(k+1) vertical factors of length k k. Similarly, there are 2 ​ ( l + 1) 2(l+1) horizontal factors of length l l. By pairing the vertical(horizontal) factors located in the same row(column), we get k + 1 k+1 ( l+1 ) pairs of vertical(horizontal) factors. Now, note that a 2D subword of f ∞, ∞ f_{\infty,\infty} is formed by the process similar to the one explained in the proof of Theorem 2 from [23]. That is, a vertical factor will produce a 2D factor through a horizontal factor, if both have the same prefix of size ( 1, 1) (1,1). Now, as one factor in a pair of vertical factors shares a common prefix of size ( 1, 1) (1,1) with one factor in a pair of horizontal factors, there will be ( k + 1) ​ ( l + 1) (k+1)(l+1) distinct factors of size ( k, l) (k,l) in f ∞, ∞ f_{\infty,\infty}. ∎

To understand the process, in Example 3 we list the factors of size ( 2, 3) (2,3) in f ∞, ∞ f_{\infty,\infty}.

###### Example 3.

Consider f ∞, ∞ f_{\infty,\infty}.

Horizontal Factors of dcd cdd ddc cdc length 3 3 → \rightarrow (or) (or) (or) (or) V ​ e ​ r ​ t ​ i ​ c ​ a ​ l Vertical bab abb bba aba Factors of length 2 ↓ \downarrow ​ ( o ​ r) ​ \begin{tabular}[]{c}d\\ b\end{tabular}(or)\begin{tabular}[]{c}c\\ a\end{tabular} d c d b a b c d d a b b d d c b b a c d c a b a ​ ( o ​ r) ​ \begin{tabular}[]{c}b\\ d\end{tabular}(or)\begin{tabular}[]{c}a\\ c\end{tabular} b a b d c d a b b c d d b b a d d c a b a c d c ​ ( o ​ r) ​ \begin{tabular}[]{c}d\\ d\end{tabular}(or)\begin{tabular}[]{c}c\\ c\end{tabular} d c d d c d c d d c d d d d c d d c c d c c d c

We have 3 × 4 = 12 3\times 4=12 factors of size ( 2, 3) (2,3).

The count, carried out in proposition 5 can be restricted to any finite Fibonacci word f m, n f_{m,n}. Note that, while counting factors of size ( k, l) (k,l) in a given f m, n f_{m,n}, contrary to the availability of all ( k + 1) (k+1) vertical factors and ( l + 1) (l+1) horizontal factors in f ∞, ∞ f_{\infty,\infty}, not all will be available in f m, n f_{m,n}. This is due to the finite nature of f m, n f_{m,n}. But, by theorem 8, we know the exact number of horizontal and vertical factors available in any given f m, n f_{m,n}. Hence we have the following result.

###### Proposition 6.

Given a finite Fibonacci array, f m, n f_{m,n}, the number of factors of size ( k, l) (k,l) in it are,

 | p k, l ​ ( f m, n) = p k ​ ( f m) ​ p l ​ ( f n). p_{k,l}(f_{m,n})=p_{k}(f_{m})p_{l}(f_{n}). |  |

###### Proof.

Using the count derived in theorem 8, one can show the equality in identical lines with the proof of proposition 5. ∎

In Example 4 also, we count the factors of size ( 2, 3) (2,3), but in f 3, 4 f_{3,4}. We can observe the non availability of some horizontal, vertical factors due to the finite nature of f 3, 4 f_{3,4}.

###### Example 4.

Consider f 3, 4 = f_{3,4}=\begin{tabular}[]{|c c c c c|}\hline\cr d&c&d&d&c\\ b&a&b&b&a\\ d&c&d&d&c\\ \hline\cr\end{tabular}.

Horizontal dcd cdd ddc Factors of length 3 3 → \rightarrow (or) (or) (or) V ​ e ​ r ​ t ​ i ​ c ​ a ​ l Vertical bab abb bba Factors of length 2 ↓ \downarrow d b (or) c a d c d b a b c d d a b b d d c b b a b d (or) a c b a b d c d a b b c d d b b a d d c

We have, p 2 ​ ( f 3) × p 3 ​ ( f 4) = 2 × 3 = 6 p_{2}(f_{3})\times p_{3}(f_{4})=2\times 3=6 factors of size ( 2, 3) (2,3).

## 9 2D Fibonacci Words as S − a ​ u ​ t ​ o ​ m ​ a ​ t ​ i ​ c S-automatic Words

In this section we construct a DFAO which generates f ∞, ∞ f_{\infty,\infty}.

To construct the DFAO, first we construct | Σ | |\Sigma| number of automata, one for each letter of Σ \Sigma, as outlined [33].These automata will be integrated to get the required DFAO.

###### Definition 14.

[33] For each d-dimensional morphism μ: Σ → B d ​ ( Σ) \mu:\Sigma\rightarrow B_{d}{(\Sigma)} and for each letter a ∈ Σ a\in\Sigma, define a DFA 𝒜 μ, a \mathscr{A}_{\mu,a} over the alphabet { 0, 1, …, r μ − 1 } d \{0,1,\ldots,r_{\mu}-1\}^{d} where r μ:= m ​ a ​ x ​ { | μ ⁡ ( b) | i | ​ b ∈ Σ, i = 1, …, d } r_{\mu}:=max\{|\mu(b)|_{i}~~|~b\in\Sigma,i=1,\ldots,d\}. The set of states is Σ \Sigma, the initial state is a a and all states are final. The (partial) transition function is defined by

 | δ μ ​ ( b, n) = ( μ ⁡ ( b)) n, ∀ b ∈ Σ ​ and ​ n ≤ | μ ⁡ ( b) |. \delta_{\mu}(b,\textbf{n})=(\mu(b))_{\textbf{n}},~~~\forall b\in\Sigma~\text{and}~\textbf{n}\leq|\mu(b)|. |  |

This automaton will be such that, for all m, n ≥ 0 m,n\geq 0,

 | y m, n = δ μ ​ ( a, ( r ​ e ​ p S ​ ( m), r ​ e ​ p S ​ ( n)) 0), y_{m,n}=\delta_{\mu}(a,(rep_{S}(m),rep_{S}(n))^{0}), |  |

where we have padded the shortest word with enough 0 0 s to make the length of the two words the same. If we consider the coding v: Σ ∗ → Γ ∗ v:\Sigma^{*}\rightarrow\Gamma^{*}, as the output function, the corresponding DFAO generates x x as an S-automatic sequence.

The procedure is outlined below.

- Step 1

From the first rows of the morphism μ \mu, derive the one dimensional morphism μ 1: Σ 1 → Σ 1 ∗ \mu_{1}:\Sigma_{1}\rightarrow\Sigma_{1}^{*}, Σ 1 ⊆ Σ \Sigma_{1}\subseteq\Sigma, which is prolongable on a a (This is the restricted morphism along the first direction)

- Step 2

Construct the automaton 𝒜 μ 1, a \mathscr{A}_{\mu_{1},a} and obtain the directive language L ​ μ 1, a L{\mu_{1},a}

( Alternatively, we can consider the first columns of the morphism μ \mu to derive the one dimensional morphism μ 2: Σ 2 → Σ 2 ∗ \mu_{2}:\Sigma_{2}\rightarrow\Sigma_{2}^{*}, Σ 2 ⊆ Σ \Sigma_{2}\subseteq\Sigma, which is also prolongable on a a. Note that, this is the restricted morphism along the second direction. Then by constructing the automaton 𝒜 μ 2, a \mathscr{A}_{\mu_{2},a} we can obtain the directive language L ​ μ 2, a L{\mu_{2},a}. But since S ​ h ​ a ​ p ​ e μ 1 ​ ( x) = S ​ h ​ a ​ p ​ e μ 2 ​ ( y) Shape_{\mu_{1}}(x)=Shape_{\mu_{2}}(y), where x = μ 1 ω ​ ( a) \mu_{1}^{\omega}(a) and y = μ 2 ω ​ ( a) y=\mu_{2}^{\omega}(a), the languages L μ 1, a L_{\mu_{1},a} and L μ 2, a L_{\mu_{2},a} will be equal [33])

- Step 3

For each letter a ∈ Σ a\in\Sigma, define a DFA 𝒜 μ, a \mathscr{A}_{\mu,a} as described in the Definition 14. The DFAO 𝒜 μ \mathscr{A}_{\mu} is constructed by combining (superimposing) these DFAs.

- Step 4

For an input ( r ​ e ​ p S ​ ( m), r ​ e ​ p S ​ ( n)) 0 (rep_{S}(m),rep_{S}(n))^{0}, the output of 𝒜 μ \mathscr{A}_{\mu} is the symbol s ∈ Σ s\in\Sigma in the accepting state which will be written at x m, n x_{m,n}, the ( m, n) t ​ h (m,n)^{th} entry in the 2D infinite word.

### 9.1 DFAO Generating f ∞, ∞ f_{\infty,\infty} as an S-automatic word

As explained earlier, we have the two unidimensional morphisms derived from (2). Let Σ 1 = { d, c } \Sigma_{1}=\{d,c\} and Σ 2 = { d, b } \Sigma_{2}=\{d,b\}. Then,

μ 1: Σ 1 → Σ 1 ∗:= d → d ​ c, c → d \mu_{1}:\Sigma_{1}\rightarrow\Sigma_{1}^{*}~~:=d\rightarrow dc,~~c\rightarrow d and μ 2: Σ 2 → Σ 2 ∗:= d → d ​ b, b → d \mu_{2}:\Sigma_{2}\rightarrow\Sigma_{2}^{*}~~:=d\rightarrow db,~~b\rightarrow d.

The automaton 𝒜 μ 1, d \mathscr{A}_{\mu_{1},d} will be as in Figure 3. And the directive language will be

 | L μ 1, d = { ϵ, 1, 10, 100, 101, 1000, 1001, 1010, … }. L_{\mu_{1},d}=\{\epsilon,1,10,100,101,1000,1001,1010,\dots\}. |  |

[image: Refer to caption] Figure 3: Automaton 𝒜 μ 1, d \mathscr{A}_{\mu_{1},d}

Note that r μ:= m ​ a ​ x ​ { | μ ⁡ ( b) | i | ​ b ∈ Σ, i = 1, 2 } = 2 r_{\mu}:=max\{|\mu(b)|_{i}~~|~b\in\Sigma,i=1,2\}=2. Hence, for each letter a ∈ Σ a\in\Sigma, we define a DFA, 𝒜 μ, a \mathscr{A}_{\mu,a} over the alphabet { 0, 1 } 2 = { ( 0, 0), ( 0, 1), ( 1, 0), ( 1, 1) } \{0,1\}^{2}=\{(0,0),(0,1),(1,0),(1,1)\}. All the four automata are given in Figure 4. We combine all the four automata to get the required automaton, 𝒜 μ \mathscr{A}_{\mu}, given in Figure 5.

[image: Refer to caption] Figure 4: 𝒜 μ, d \mathscr{A}_{\mu,d}, 𝒜 μ, c \mathscr{A}_{\mu,c}, 𝒜 μ, b \mathscr{A}_{\mu,b}, 𝒜 μ, a \mathscr{A}_{\mu,a}[image: Refer to caption] Figure 5: DFAO 𝒜 μ \mathscr{A}_{\mu} generating f ∞, ∞ f_{\infty,\infty}

For a given m, n ≥ 0 m,n\geq 0, the steps involved in obtaining the symbol at ( m, n) (m,n) in f ∞, ∞ f_{\infty,\infty} are briefly explained in Example 5, using the values m = 2 m=2 and n = 4 n=4..

###### Example 5.

Let us generate the symbol at ( 2, 4) (2,4) in f ∞, ∞ f_{\infty,\infty}. From the directive language we get r ​ e ​ p S ​ ( 2) = 10 rep_{S}(2)=10 and r ​ e ​ p S ​ ( 4) = 101 rep_{S}(4)=101.

The ( 2, 4) t ​ h (2,4)^{th} entry will be δ μ ​ ( d, ( 10,101) 0) = δ μ ​ ( d, ( 010,101)) \delta_{\mu}(d,(10,101)^{0})=\delta_{\mu}(d,(010,101)).

 | d → ( 0, 1) c → ( 1, 0) b → ( 0, 1) c. d\xrightarrow{(0,1)}c\xrightarrow{(1,0)}b\xrightarrow{(0,1)}c. |  |

By generating all the symbols at ( i, j) (i,j), i ∈ ⟦ 0, s − 1 ⟧ i\in\llbracket 0,s-1\rrbracket, j ∈ ⟦ 0, t − 1 ⟧ j\in\llbracket 0,t-1\rrbracket the prefix of size, (s,t) of f ∞, ∞ f_{\infty,\infty} can be generated. More specifically any finite 2D Fibonacci array can be generated.

## 10 Conclusion

Though the theory of two-dimensional words is a natural extension of the theory of one-dimensional words, exploring their combinatorial and structural properties is not a straightforward task. In this paper we have analysed two important properties - tandem repeats and factor complexity - of finite 2D Fibonacci words and the infinite 2D Fibonacci word. A 2D homomorphism with the infinite 2D Fibonacci word as its fixed point is presented, proving that the infinite 2D Fibonacci word is a morphic word. A DFAO generating the 2D Fibonacci words is also constructed. Some closely related properties to tandem repeats are, approximate tandem repeats and approximate periodicity of 2D Fibonacci words. Future research might concentrate on these properties.

## References

- [1] A. Apostolico, V. E. Brimkov, Fibonacci arrays and their two-dimensional repetitions, Theoretical Computer Science 237 (1–2) (2000) 263–273.
- [2] M. Lothaire, Combinatorics on words, Cambridge University Press, 1997.
- [3] G. Paun, G. Rozenberg, A. Salomaa, DNA Computing: New Computing Paradigms, Springer-Verlag Berlin Heidelberg, 1998.
- [4] R. Dallapiccola, A. Gopinath, F. Stellacci, L. D. Negro, Quasi-periodic distribution of plasmon modes in two-dimensional Fibonacci arrays of metal nanoparticles, Optics Express 16 (8) (2008) 5544–5555.
- [5] J. Berstel, Axel Thue’s work on repetitions in words, Series Formelles et Combinatoire Algerique 11 (1992) 65–80.
- [6] S. Jain, F. F. Hassanzadeh, J. Bruck, Capacity and expressiveness of genomic tandem duplication, IEEE Transactions on Information Theory 63 (10) (2017) 6129–6138.
- [7] D. Salomon, Data Compression: The Complete Reference, 4th Edition, Springer, 2007.
- [8] D. Gusfield, J. Stoye, Linear time algorithms for finding and representing all the tandem repeats in a string, Journal of Computer and System Sciences 69 (4) (2004) 525–546.
- [9] M. Crochemore, L. Ilie, W. Rytter, Repetitions in strings: Algorithms and combinatorics, Theoretical Computer Science 410 (50) (2009) 5227–5235.
- [10] A. Amir, G. M. Landau, S. Marcus, D. Sokol, Two-dimensional maximal repetitions, Theoretical Computer Science 812 (2020) 49–61.
- [11] P. Charalampopoulos, J. Radoszewski, W. Rytter, T. Waleń, W. Zuba, The number of repetitions in 2D-strings, in: F. Grandoni, G. Herman, P. Sanders (Eds.), 28th Annual European Symposium on Algorithms (ESA 2020), Vol. 173 of Leibniz International Proceedings in Informatics (LIPIcs), Schloss Dagstuhl–Leibniz-Zentrum für Informatik, 2020, pp. 32:1–32:18.
- [12] A. Amir, A. Butman, G. M. Landau, S. Marcus, D. Sokol, Double String Tandem Repeats, in: I. L. Gørtz, O. Weimann (Eds.), 31st Annual Symposium on Combinatorial Pattern Matching (CPM 2020), Vol. 161 of Leibniz International Proceedings in Informatics (LIPIcs), Schloss Dagstuhl–Leibniz-Zentrum für Informatik, 2020, pp. 3:1–3:13.
- [13] A. Amihood, B. Ayelet, K. Eitan, L. Avivit, S. Dina, Multidimensional period recovery, Algorithmica.
- [14] J. Berstel, Fibonacci words - a survey, in: G. Rozenberg, A. Salomaa (Eds.), The book of L, Springer-Verlag, 1986, pp. 13–27.
- [15] S. S. Yu, Y. K. Zhao, Properties of Fibonacci languages, Discrete Mathematics 224 (2000) 215–223.
- [16] K. Kamala, R. Rama, Introduction to Formal Languages, Automata Theory and Computation, Pearson Education, 2009.
- [17] M. Lothaire, Algebraic combinatorics on words, Cambridge University Press, 2002.
- [18] D. Giammarresi, A. Restivo, Two-dimensional languages, in: G. Rozenberg, A. Salomaa (Eds.), Handbook of formal languages, Springer, 1997, pp. 215–267.
- [19] M. Anselmo, D. Giammarresi, M. Madonia, Prefix picture codes: a decidable class of two-dimensional codes, International Journal of Foundations of Computer Science 25 (08) (2014) 1017–1031.
- [20] M. S. Kulkarni, K. Mahalingam, M. Sivasankar, Combinatorial properties of Fibonacci arrays, in: T. V. Gopal, J. Watada (Eds.), Theory and Applications of Models of Computation, Springer International Publishing, 2019, pp. 448–466.
- [21] G. Gamard, G. Richomme, J. Shallit, T. J. Smith, Periodicity in rectangular arrays, Information Processing Letters 118 (2017) 58–63.
- [22] V. Berthe, L. Vuillon, Palindromes and two-dimensional sturmian sequences, Journal of Automata, Languages and Combinatorics 6 (2) (2001) 121–138.
- [23] K. Mahalingam, M. Sivasankar, K. Krithivasan, Palindromic properties of two dimensional Fibonacci words, The Romanian Journal of Information Science and Technology 21 (3) (2018) 256–266.
- [24] E. S. Lander, Initial sequencing and analysis of the human genome, Nature 409 (6822) (2001) 860–921.
- [25] N. I. Mundy, A. J. Helbig, Origin and evolution of tandem repeats in the mitochondrial DNA control region of shrikes, Journal of Molecular Evolution 59 (2) (2004) 250–257.
- [26] G. M. Landau, J. P. Schmidt, An algorithm for approximate tandem repeats, in: A. Apostolico, M. Crochemore, Z. Galil, U. Manber (Eds.), Combinatorial Pattern Matching, Springer Berlin Heidelberg, 1993, pp. 120–133.
- [27] A. Fraenkel, J. Simpson, The exact number of squares in Fibonacci words, Theoretical Computer Science 218 (1) (1999) 83–94.
- [28] A. Fraenkel, J. Simpson, Corrigendum to “The exact number of squares in Fibonacci words” [Theoretical computer science 218 (1) (1999) 95–106], Theoretical Computer Science 547 (2014) 122.
- [29] C. F. Du, H. Mousavi, L. Schaeffer, J. Shallit, Decision algorithms for Fibonacci-automatic words, III: Enumeration and abelian properties, International Journal of Foundations of Computer Science 27 (8) (2016) 943 – 963.
- [30] J. P. Allouche, J. Shallit, Automatic sequences: Theory, applications, generalizations, Cambridge University Press, 2003.
- [31] W. F. Chuan, H. L. Ho, Locating factors of the infinite Fibonacci word, Theoretical Computer Science 349 (3) (2005) 429–442.
- [32] P. Arnoux, V. Berthé, A. Siegel, Two dimensional iterated morphisms and discrete planes, Theoretical Computer Science 319 (1) (2004) 145 – 176.
- [33] E. Charlier, T. Karki, M. Rigo, Multidimensional generalized automatic sequences and shape-symmetric morphic words, Discrete Mathematics 310 (6) (2010) 1238–1252.
- [34] P. B. A. Lecomte, M. Rigo, Numeration systems on a regular language, Theory of Computing Systems 34 (1) (2000) 27–44.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:ma16d028@smail.iitm.ac.in
[2]: mailto:ramar@iitm.ac.in
[3]: /html/2204.13976
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/2204.13977
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2204.13977
[9]: https://arxiv.org/pdf/2204.13977
[10]: /html/2204.13978
