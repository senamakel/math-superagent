<!-- source: https://ar5iv.labs.arxiv.org/html/1212.1368 | converted from HTML -->

[1212.1368] A Generalization of the Fibonacci Word Fractal and the Fibonacci Snowflake

# A Generalization of the Fibonacci Word Fractal and the Fibonacci Snowflake

José L. Ramírez Note: Corresponding author. Thanks: josel.ramirez@ima.usergioarboleda.edu.co Affiliation: Instituto de Matemáticas y sus Aplicaciones, Universidad Sergio Arboleda, Calle 74 no. 14 - 14, Bogotá, Colombia Gustavo N. Rubiano Thanks: gnrubianoo@unal.edu.co Affiliation: Departamento de Matemáticas, Universidad Nacional de Colombia, AA 14490, Bogotá, Colombia Rodrigo de Castro Thanks: rdecastrok@unal.edu.co Affiliation: Departamento de Matemáticas, Universidad Nacional de Colombia, AA 14490, Bogotá, Colombia

###### Abstract

In this paper we introduce a family of infinite words that generalize the Fibonacci word and we study their combinatorial properties. We associate with this family of words a family of curves that are like the Fibonacci word fractal and reveal some fractal features. Finally, we describe an infinite family of polyominoes stems from the generalized Fibonacci words and we study some of their geometric properties, such as perimeter and area. These last polyominoes generalize the Fibonacci snowflake and they are double squares polyominoes, i.e., tile the plane by translation in exactly two distinct ways.

Keywords: Fibonacci word, Fibonacci word fractal, Fibonacci snowflake, Polyomino, Tessellation.

## 1 Introduction

The infinite Fibonacci word,

 | *f*= 0100101001001010010100100101 ⋯ \displaystyle\textbf{\emph{f}}=\texttt{0100101001001010010100100101}\cdots |  |

is certainly one of the most studied examples in the combinatorial theory of infinite words, e.g. [3, 12, 13, 14, 15, 16, 21, 24]. It is the archetype of a Sturmian word [20]. The Fibonacci word *f*can be defined in several different ways [3]. For instance, Fibonacci word f satisfies lim n → ∞ σ n ​ ( 𝟷) = f \lim_{n\rightarrow\infty}\sigma^{n}(\verb"1")=\textbf{{f}}, where σ: { 0,1 } → { 0,1 } \sigma:\left\{\texttt{0,1}\right\}\rightarrow\left\{\texttt{0,1}\right\} is the morphism defined by σ ⁡ ( 𝟶) = 𝟶𝟷 \sigma(\verb"0")=\verb"01" and σ ⁡ ( 𝟷) = 𝟶 \sigma(\verb"1")=\verb"0". This morphism is called *Fibonacci morphism*. The name Fibonacci given to f is due to the fact that f is the limit sequence of the infinite sequence ( f n) n = 0 (f_{n})_{n=0} of finite words over { 0,1 } \left\{\texttt{0,1}\right\} defined inductively as follows

 | f 0 = 1, f 1 = 0, f n = f n − 1 ​ f n − 2, n ≥ 2. \displaystyle f_{0}=\texttt{1},\hskip 28.45274ptf_{1}=\texttt{0},\hskip 28.45274ptf_{n}=f_{n-1}f_{n-2},\ n\geq 2. |  |

The words f n f_{n} are called *finite Fibonacci words*. It is clear that | f n | = F n |f_{n}|=F_{n}, where F n F_{n} is the n n -th Fibonacci number defined by the recurrence relation F n = F n − 1 + F n − 2 F_{n}=F_{n-1}+F_{n-2}, for all integer n ≥ 2 n\geq 2 and with initial values F 0 = 1 = F 1 F_{0}=1=F_{1}.

The word f can be associated with a curve from a drawing rule, which has geometry properties obtained from combinatorial properties of *f*[4, 22]. We must travel the word in a particular way, depending on the symbol read a particular action is produced, this idea is the same as that used in the L-Systems [25]. In this case, the drawing rule is called “odd-even drawing rule” [22], this is defined as shown in the following table:

Symbol | Action |

`1` | Draw a line forward. |

`0` | Draw a line forward and if the symbol `0`is in an even position then turn left and if 0 is in an odd position then turn right. |

The *n n th-curve of Fibonacci*, denoted by ℱ n \mathcal{F}_{n}, is obtained by applying the odd-even drawing rule to the word f n f_{n}. The *Fibonacci word fractal*ℱ \mathcal{F}, is defined as

 | ℱ = lim n → ∞ ℱ n. \displaystyle\mathcal{F}=\lim_{n\rightarrow\infty}\mathcal{F}_{n}. |  |

For example, in Fig. 1 we show the curve ℱ 10 \mathcal{F}_{10} and ℱ 17 \mathcal{F}_{17}. The graphics in this paper were generated using the software `Mathematica 8.0`, [26].

f 10 = f_{10}=`010010100100101001010010010100100101001010010010`

`10010100100101001001010010100100101001001`.

[image: Refer to caption] Figure 1: Fibonacci curves ℱ 10 \mathcal{F}_{10} and ℱ 17 \mathcal{F}_{17} corresponding to the words f 10 f_{10} and f 17 f_{17}.

The word *f*can also be associated with a family of polyominoes which tile the plane by translation and are called *Fibonacci snowflakes*[4, 7]. By *polyomino*we mean a finite union of unit lattice squares in the square lattice ℤ × ℤ \mathbb{Z}\times\mathbb{Z} whose boundary is a non-crossing closed path (see [18] for more on tilings and [9] for related problems). A *path *in the square lattice is a polygonal path made of the elementary unit translations

 | 0 = ( 1, 0), 1 = ( 0, 1), 2 = ( − 1, 0), 3 = ( 0, − 1). \displaystyle\texttt{0}=(1,0),\hskip 28.45274pt\texttt{1}=(0,1),\hskip 28.45274pt\texttt{2}=(-1,0),\hskip 28.45274pt\texttt{3}=(0,-1). |  |

These paths are conveniently encoded by words on the alphabet 𝒜 = { 0, 1, 2, 3 } \mathcal{A}=\left\{\verb"0, 1, 2, 3"\right\}. This relation between discrete objects and words has been used in modeling of problems of tessellations in the plane with polyominoes, (see e.g. [2, 4, 5, 8, 11] and [10] for more relations between discrete geometry and combinatorics on words).

In [28] authors were the first to consider the problem of deciding if a given polyomino tiles the plane by translation and they coined the term *exact polyomino*. In [2] authors proved that a polyomino P P tiles the plane by translations if and only if the boundary word b ( P P) is equal up to a cyclic permutation of the symbols to A ⋅ B ⋅ C ⋅ A ^ ⋅ B ^ ⋅ C ^ A\cdot B\cdot C\cdot\widehat{A}\cdot\widehat{B}\cdot\widehat{C}, where one of the variables in the factorization may be empty. This condition is referred as the BN-factorization. If the boundary word is equal to A ⋅ B ⋅ C ⋅ A ^ ⋅ B ^ ⋅ C ^ A\cdot B\cdot C\cdot\widehat{A}\cdot\widehat{B}\cdot\widehat{C} such a polyomino is called *pseudo-hexagon*and when one of the variables is empty, i.e., b ​ ( P) = A ⋅ B ⋅ A ^ ⋅ B ^ \textbf{b}(P)=A\cdot B\cdot\widehat{A}\cdot\widehat{B}, we say that P P is a *square polyomino*.

For instance, the polyomino in Fig. 2 (left) is an exact polyomino and its boundary can be factorized by 𝟷𝟸𝟸 ⋅ 𝟸𝟷𝟸 ⋅ 𝟹𝟸𝟹 ⋅ 𝟶𝟶𝟹 ⋅ 𝟶𝟹𝟶 ⋅ 𝟷𝟶𝟷 \verb"122"\cdot\verb"212"\cdot\verb"323"\cdot\verb"003"\cdot\verb"030"\cdot\verb"101", (the factorization is not necessarily in a unique way).

[image: Refer to caption]
Figure 2: Exact polyomino and tiling.

In [5], authors prove that an exact polyomino tiles the plane in at most two distinct ways. Squares polyominoes having exactly two distinct BN-factorizations are called *double squares*. For instance, Christoffel and Fibonacci tiles or Fibonacci snowflakes, introduced in [4], are examples of double squares, however, there exist double squares not in the Christoffel and Fibonacci tiles families. In [8], they study the combinatorial properties and the problem of generating exhaustively double square tiles, however, they did not study the geometric properties, only in the case of Fibonacci polyominoes [7].

On the other hand, Fibonacci numbers and their generalizations have many interesting properties and applications to almost every field of science and art, (e.g. see [19]). In the present case we are interested in the generalization of the Fibonacci sequence by preserving the recurrence relation and altering the first two terms of the sequence.

The *( n, i) (n,i) -th Fibonacci number*F n [i] F_{n}^{\left[i\right]} is defined recursively by

 | F 0 [i] = 1, F 1 [i] = i, F n [i] = F n − 1 [i] + F n − 2 [i] \displaystyle F_{0}^{\left[i\right]}=1,\hskip 28.45274ptF_{1}^{\left[i\right]}=i,\hskip 28.45274ptF_{n}^{\left[i\right]}=F_{n-1}^{\left[i\right]}+F_{n-2}^{\left[i\right]} |  |

for all n ≥ 2 n\geq 2 and i ≥ 1 i\geq 1. For i = 1, 2 i=1,2 we have the Fibonacci numbers.

In this paper we introduce a family of words *f*[i] \textbf{\emph{f}}^{\left[i\right]} (Definition 2) that generalize the Fibonacci word. Each word *f*[i] \textbf{\emph{f}}^{\left[i\right]} is the limit sequence of an infinite sequence of finite words such that their length are ( n, i) (n,i) -th Fibonacci numbers. Moreover, the word *f*[i] \textbf{\emph{f}}^{\left[i\right]} is a characteristic word of slope i − ϕ i 2 − i − 1 \frac{i-\phi}{i^{2}-i-1}, where ϕ \phi is the golden ratio (Theorem 1). From this family of infinite words we define a family of plane curves called*i i -Fibonacci word fractal *(Definition 3), which are like the Fibonacci word fractal and have the same properties (Proposition 6). Finally, we introduce a family of polyominoes which generalize the Fibonacci snowflake and we study their geometric properties, such as perimeter (Proposition 12) and area (Proposition 13) which is related to generalized Pell numbers. These polyominoes are also double squares (Theorem 2) and have the same fractal dimension of the Fibonacci word Fractal. These generalizations are interesting, as they leave the question whether it is possible to generate all double squares polyominoes from families of words like the Fibonacci word.

## 2 Definitions and Notation

The terminology and notations are mainly those of Lothaire [20] and Allouche and Shallit [1]. Let Σ \Sigma be a finite alphabet, whose elements are called *symbols*. A *word*over Σ \Sigma is a finite sequence of symbols from Σ \Sigma. The set of all words over Σ \Sigma, i.e., the free monoid generated by Σ \Sigma, is denoted by Σ ∗ \Sigma^{*}. The identity element ϵ \epsilon of Σ ∗ \Sigma^{*} is called the *empty word*. For any word w ∈ Σ ∗ w\in\Sigma^{*}, | w | \left|w\right| denotes its *length*, i.e., the number of symbols occurring in w w. The length of ϵ \epsilon is taken to be equal to 0. If a ∈ Σ a\in\Sigma and w ∈ Σ ∗ w\in\Sigma^{*}, then | w | a \left|w\right|_{a} denotes the number of occurrences of a a in w w.

For two words u = a 1 a 2 ⋯ a k u=a_{1}a_{2}\cdots a_{k} and v = b 1 b 2 ⋯ b s v=b_{1}b_{2}\cdots b_{s} in Σ ∗ \Sigma^{*} we denote by u ​ v uv the *concatenation*of the two words, that is, u v = a 1 a 2 ⋯ a k b 1 b 2 ⋯ b s uv=a_{1}a_{2}\cdots a_{k}b_{1}b_{2}\cdots b_{s}. If v = ϵ v=\epsilon then u ​ ϵ = ϵ ​ u = u u\epsilon=\epsilon u=u, moreover, by u n u^{n} we denote the word u u ⋯ u uu\cdots u ( n n times). A word v v is a *factor*or *subword*of u u if there exist x, y ∈ Σ ∗ x,y\in\Sigma^{*} such that u = x ​ v ​ y u=xvy. If x = ϵ x=\epsilon ( y = ϵ y=\epsilon), then v v is called *prefix*(*suffix*) of u u.

The *reversal*of a word u = a 1 a 2 ⋯ a n u=a_{1}a_{2}\cdots a_{n} is the word u R = a n ⋯ a 2 a 1 u^{R}=a_{n}\cdots a_{2}a_{1} and ϵ R = ϵ \epsilon^{R}=\epsilon. A word u u is a *palindrome*if u R = u u^{R}=u.

An *infinite word*over Σ \Sigma is a map *u*: ℕ → Σ \textbf{\emph{u}}:\mathbb{N}\rightarrow\Sigma. It is written *u*= a 1 ​ a 2 ​ a 3 ​ … \textbf{\emph{u}}=a_{1}a_{2}a_{3}\ldots. The set of all infinite words over Σ \Sigma is denoted by Σ ω \Sigma^{\omega}.

###### Example 1.

Let p = ( p n) n ≥ 1 = 𝟶𝟷𝟷𝟶𝟷𝟶𝟷𝟶𝟶𝟶𝟷𝟶𝟷 ⋯ \textbf{p}=(p_{n})_{n\geq 1}=\verb"0110101000101"\cdots, where p n =*1*p_{n}=\texttt{\emph{1}} if n n is a prime number and p n =*0*p_{n}=\texttt{\emph{0}} otherwise, is an example of an infinite word. The word p is called the characteristic sequence of the prime numbers.

Let Σ \Sigma and Δ \Delta be alphabets. A *morphism*is a map h: Σ ∗ → Δ ∗ h:\Sigma^{*}\rightarrow\Delta^{*} such that h ⁡ ( x ​ y) = h ⁡ ( x) ​ h ​ ( y) h(xy)=h(x)h(y) for all x, y ∈ Σ ∗ x,y\in\Sigma^{*}. It is clear that h ⁡ ( ϵ) = ϵ h(\epsilon)=\epsilon. Furthermore, a morphism is completely determined by its action on single symbols.

There is a special class of infinite words, with many remarkable properties, the so-called Sturmian words. These words admit several equivalent definitions (see, e.g. [1] or [20]). Let w ∈ Σ ω \textbf{{w}}\in\Sigma^{\omega}. We define P ⁡ ( w, n) P(\textbf{{w}},n), the *complexity function*of w, to be the map that counts, for all integer n ≥ 0 n\geq 0, the number of subwords of length n n in w. An infinite word w is a *Sturmian word*if P ⁡ ( w, n) = n + 1 P(\textbf{{w}},n)=n+1 for all integer n ≥ 0 n\geq 0. Since for any Sturmian word P ⁡ ( w, 1) = 2 P(\textbf{{w}},1)=2, then Sturmian words are over two symbols. The word *p*, in example 1, is not a Sturmian word because P ⁡ (*p*, 2) = 4 P(\textbf{\emph{p}},2)=4.

Given two real numbers α, β ∈ ℝ \alpha,\beta\in\mathbb{R} with α \alpha irrational and 0 < α < 1 0<\alpha<1, 0 ≤ β < 1 0\leq\beta<1, we define the infinite word *w*= w 1 w 2 w 3 ⋯ \textbf{\emph{w}}=w_{1}w_{2}w_{3}\cdots as

 | w n = ⌊ ( n + 1) ​ α + β ⌋ − ⌊ n ​ α + β ⌋. w_{n}=\lfloor(n+1)\alpha+\beta\rfloor-\lfloor n\alpha+\beta\rfloor. |  |

The numbers α \alpha and β \beta are called the *slope*and the *intercept*, respectively. Words of this form are called *lower mechanical words*and are known to be equivalent to Sturmian words [20]. As special case, when β = 0 \beta=0, we obtain the *characteristic words*.

###### Definition 1.

Let α \alpha be an irrational number with 0 < α < 1 0<\alpha<1. For n ≥ 1 n\geq 1, define

 | w α ​ ( n):= ⌊ ( n + 1) ​ α ⌋ − ⌊ n ​ α ⌋ \displaystyle w_{\alpha}(n):=\left\lfloor(n+1)\alpha\right\rfloor-\left\lfloor n\alpha\right\rfloor |  |

and

 | w ( α):= w α ( 1) w α ( 2) w α ( 3) ⋯ \displaystyle\textbf{w}(\alpha):=w_{\alpha}(1)w_{\alpha}(2)w_{\alpha}(3)\cdots |  |

Then w ​ ( α) \textbf{w}(\alpha) is called the characteristic word with slope α \alpha.

On the other hand, note that every irrational α ∈ ( 0, 1) \alpha\in(0,1) has a unique continued fraction expansion

 | α = [0, a 1, a 2, a 3, …] = 1 a 1 + 1 a 2 + 1 a 3 + ⋯ \displaystyle\alpha=\left[0,a_{1},a_{2},a_{3},\ldots\right]=\cfrac{1}{a_{1}+\cfrac{1}{a_{2}+\cfrac{1}{a_{3}+\cdots}}} |  |

where each a i a_{i} is a positive integer. Let α = [0, 1 + d 1, d 2, …] \alpha=\left[0,1+d_{1},d_{2},\dots\right] be an irrational number with d 1 ≥ 0 d_{1}\geq 0 and d n > 0 d_{n}>0 for n > 1 n>1. With the directive sequence ( d 1, d 2, …, d n, …) (d_{1},d_{2},\dots,d_{n},\dots), we associate a sequence ( s n) n ≥ − 1 (s_{n})_{n\geq-1} of words defined by

 | s − 1 = 1, s 0 = 0, s n = s n − 1 d n s n − 2, ( n ≥ 1) \displaystyle s_{-1}=\texttt{1},\ \ s_{0}=\texttt{0},\ \ s_{n}=s_{n-1}^{d_{n}}s_{n-2},\ \ (n\geq 1) |  |

Such a sequence of words is called a *standard sequence*. This sequence is related to characteristic words in the following way. Observe that, for any n ≥ 0 n\geq 0, s n s_{n} is a prefix of s n + 1 s_{n+1}, which gives meaning to lim n → ∞ s n \lim_{n\rightarrow\infty}s_{n} as an infinite word. In fact, one can prove [20] that each s n s_{n} is a prefix of *w*​ ( α) \textbf{\emph{w}}(\alpha) for all n ≥ 0 n\geq 0 and

 | *w*​ ( α) = lim n → ∞ s n. \displaystyle\textbf{\emph{w}}(\alpha)=\lim_{n\rightarrow\infty}s_{n}. |  | (1) |

### 2.1 Fibonacci Word and Its Fractal Curve

The infinite Fibonacci word *f*is a Sturmian word [20], more precisely, *f*= w ​ ( 1 ϕ 2) \textbf{\emph{f}}=\textbf{{w}}\left(\frac{1}{\phi^{2}}\right) where ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2} is the golden ratio.

Let Φ: { 𝟶, 𝟷 } ∗ → { 𝟶, 𝟷 } ∗ \Phi:\left\{\verb"0",\verb"1"\right\}^{*}\rightarrow\left\{\verb"0",\verb"1"\right\}^{*} be a map such that Φ \Phi deletes the last two symbols, i.e., Φ ( a 1 a 2 ⋯ a n) = a 1 a 2 ⋯ a n − 2 \Phi(a_{1}a_{2}\cdots a_{n})=a_{1}a_{2}\cdots a_{n-2}, ( n ≥ 2) (n\geq 2).

The following proposition summarizes some basic properties about Fibonacci word.

###### Proposition 1 (Pirillo [24]).

The Fibonacci word and the finite Fibonacci words, satisfy the following properties

1. i.

The words `11`and `000`are not subwords of the Fibonacci word.

2. ii.

For all n ≥ 2 n\geq 2. Let a ​ b ab be the last two symbols of f n f_{n}, then we have a ​ b = 𝟶𝟷 ab=\verb"01" if n n is even and a ​ b = 𝟷𝟶 ab=\verb"10" if n n is odd.

3. iii.

The concatenation of two successive Fibonacci words is “almost commutative”, i.e., f n ​ f n − 1 f_{n}f_{n-1} and f n − 1 ​ f n f_{n-1}f_{n} have a common prefix of length F n − 2 F_{n}-2 for all n ≥ 2 n\geq 2.

4. iv.

Φ ⁡ ( f n) \Phi(f_{n}) is a palindrome for all n ≥ 2 n\geq 2.

5. v.

For all n ≥ 6 n\geq 6, f n = f n − 3 ​ f n − 3 ​ f n − 6 ​ l n − 3 ​ l n − 3 f_{n}=f_{n-3}f_{n-3}f_{n-6}l_{n-3}l_{n-3}, where l n = Φ ⁡ ( f n) ​ b ​ a l_{n}=\Phi(f_{n})ba, i.e., l n l_{n} exchanges the two last symbols of f n f_{n}.

In the next proposition we show some properties of the curves ℱ n \mathcal{F}_{n} and ℱ \mathcal{F}. It comes directly from the properties of the Fibonacci word, see Proposition 1.

###### Proposition 2 (Monnerot [22]).

Fibonacci word fractal ℱ \mathcal{F} and the curve ℱ n \mathcal{F}_{n} have the following properties:

1. i.

ℱ \mathcal{F} is composed only of segments of length 1 or 2.

2. ii.

The curve ℱ n \mathcal{F}_{n} is similar to the curve ℱ n − 3 \mathcal{F}_{n-3}, i.e., they have the same shape except for the number of segments.

3. iii.

The curve ℱ n \mathcal{F}_{n} is symmetric. More precisely, the curves ℱ 3 ​ n \mathcal{F}_{3n} and ℱ 3 ​ n + 1 \mathcal{F}_{3n+1} are symmetric with respect to a line and ℱ 3 ​ n + 2 \mathcal{F}_{3n+2} is symmetric with respect to a point.

4. iv.

The curve ℱ n \mathcal{F}_{n} is composed of 5 curves: ℱ n = ℱ n − 3 ​ ℱ n − 3 ​ ℱ n − 6 ​ ℱ ′ n − 3 ​ ℱ ′ n − 3 \mathcal{F}_{n}=\mathcal{F}_{n-3}\mathcal{F}_{n-3}\mathcal{F}_{n-6}\mathcal{F^{\prime}}_{n-3}\mathcal{F^{\prime}}_{n-3}, where ℱ ′ n \mathcal{F^{\prime}}_{n} is obtained by applying the odd-even drawing rule to word l n l_{n}, see Proposition 1 -v.

5. v.

The fractal dimension of the Fibonacci word fractal is

 | 3 ​ log ⁡ ϕ log ⁡ ( 1 + 2) = 1.6379 ​ … \displaystyle 3\frac{\log\phi}{\log(1+\sqrt{2})}=1.6379\dots |  |

More of these properties can be found in [22].

## 3 Generalized Fibonacci Words and Fibonacci Word Fractals

In this section, we introduce a generalization of the Fibonacci word and the Fibonacci word fractal, and we show that Propositions 1 and 2 remain.

###### Definition 2.

The ( n, i) (n,i) -Fibonacci words are words over {*0,1*} \left\{\texttt{\emph{0,1}}\right\} defined inductively as follows

 | f 0 [i] =*0*, f 1 [i] =*0*i − 1 ​*1*, f n [i] = f n − 1 [i] ​ f n − 2 [i], \displaystyle f_{0}^{\left[i\right]}=\texttt{\emph{0}},\hskip 28.45274ptf_{1}^{\left[i\right]}=\texttt{\emph{0}}^{i-1}\texttt{\emph{1}},\hskip 28.45274ptf_{n}^{\left[i\right]}=f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]}, |  |

for all n ≥ 2 n\geq 2 and i ≥ 1 i\geq 1. The infinite word

 | f [i]:= lim n → ∞ f n [i] \displaystyle\textbf{f}^{\,\left[i\right]}:=\lim_{n\rightarrow\infty}f_{n}^{\left[i\right]} |  |

is called the i i -Fibonacci word.

For i = 2 i=2 we have the classical Fibonacci word.

###### Example 2.

The first i i -Fibonacci words are

f [1] = 𝟷𝟶𝟷𝟷𝟶𝟷𝟶𝟷𝟷𝟶𝟷𝟷𝟶 ⋯ = f ¯ \textbf{f}^{\,\left[1\right]}=\verb"1011010110110"\cdots=\overline{\textbf{f}\ }, | f [2] = 𝟶𝟷𝟶𝟶𝟷𝟶𝟷𝟶𝟶𝟷𝟶𝟶𝟷 ⋯ = f \textbf{f}^{\,\left[2\right]}=\verb"0100101001001"\cdots=\textbf{f}, | f [3] = 𝟶𝟶𝟷𝟶𝟶𝟶𝟷𝟶𝟶𝟷𝟶𝟶𝟶 ⋯ \textbf{f}^{\,\left[3\right]}=\verb"0010001001000"\cdots, |

f [4] = 𝟶𝟶𝟶𝟷𝟶𝟶𝟶𝟶𝟷𝟶𝟶𝟶𝟷 ⋯ \textbf{f}^{\,\left[4\right]}=\verb"0001000010001"\cdots, | f [5] = 𝟶𝟶𝟶𝟶𝟷𝟶𝟶𝟶𝟶𝟶𝟷𝟶𝟶 ⋯ \textbf{f}^{\,\left[5\right]}=\verb"0000100000100"\cdots, | f [6] = 𝟶𝟶𝟶𝟶𝟶𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟷 ⋯ \textbf{f}^{\,\left[6\right]}=\verb"0000010000001"\cdots |

Note that the length of the word f n [i] f_{n}^{\left[i\right]} is the ( n, i) − (n,i)- th Fibonacci number F n [i] F_{n}^{\left[i\right]}, i.e., | f n [i] | = F n [i] |f_{n}^{\left[i\right]}|=F_{n}^{\left[i\right]}. It is clear because f n [i] = f n − 1 [i] ​ f n − 2 [i] f_{n}^{\left[i\right]}=f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]} and then | f n [i] | = | f n − 1 [i] | + | f n − 2 [i] | |f_{n}^{\left[i\right]}|=|f_{n-1}^{\left[i\right]}|+|f_{n-2}^{\left[i\right]}|, moreover | f 0 [i] | = 1 |f_{0}^{\left[i\right]}|=1 and | f 1 [i] | = i |f_{1}^{\left[i\right]}|=i.

###### Proposition 3.

A formula for the ( n, i) (n,i) -th Fibonacci number is

 | F n [i] = 1 2 ​ 5 ​ ( ( 1 − 5 2) n ​ ( 5 + 1 − 2 ​ i) + ( 1 + 5 2) n ​ ( 5 − 1 + 2 ​ i)). \displaystyle F_{n}^{\left[i\right]}=\frac{1}{2\sqrt{5}}\left(\left(\frac{1-\sqrt{5}}{2}\right)^{n}(\sqrt{5}+1-2i)+\left(\frac{1+\sqrt{5}}{2}\right)^{n}(\sqrt{5}-1+2i)\right). |  |

###### Proof.

The proof is by induction on n n. This is clearly true for n = 0, 1 n=0,1. Now suppose the result is true for n n. Then

 | F n + 1 [i] \displaystyle F_{n+1}^{\left[i\right]} | = F n [i] + F n − 1 [i] = 1 2 ​ 5 ​ ( ( ϕ 1 n + ϕ 1 n − 1) ​ ( 5 + 1 − 2 ​ i) + ( ϕ 2 n + ϕ 2 n − 1) ​ ( 5 − 1 + 2 ​ i)) \displaystyle=F_{n}^{\left[i\right]}+F_{n-1}^{\left[i\right]}=\frac{1}{2\sqrt{5}}\left(\left(\phi_{1}^{n}+\phi_{1}^{n-1}\right)\left(\sqrt{5}+1-2i\right)+\left(\phi_{2}^{n}+\phi_{2}^{n-1}\right)\left(\sqrt{5}-1+2i\right)\right) |  |

where ϕ 1 = 1 − 5 2 \phi_{1}=\frac{1-\sqrt{5}}{2} and ϕ 2 = 1 + 5 2 \phi_{2}=\frac{1+\sqrt{5}}{2}. Moreover,

 | ϕ 1 n + ϕ 1 n − 1 = ϕ 1 n − 1 ​ ( ϕ 1 + 1) = ϕ 1 n − 1 ​ ( 1 − 5 2 + 1) = ϕ 1 n − 1 ​ ϕ 1 2 = ϕ 1 n + 1, \displaystyle\phi_{1}^{n}+\phi_{1}^{n-1}=\phi_{1}^{n-1}(\phi_{1}+1)=\phi_{1}^{n-1}\left(\frac{1-\sqrt{5}}{2}+1\right)=\phi_{1}^{n-1}\phi_{1}^{2}=\phi_{1}^{n+1}, |  |

analogously ϕ 2 n + ϕ 2 n − 1 = ϕ 2 n + 1 \phi_{2}^{n}+\phi_{2}^{n-1}=\phi_{2}^{n+1}. So

 | F n + 1 [i] \displaystyle F_{n+1}^{\left[i\right]} | = 1 2 ​ 5 ​ ( ϕ 1 n + 1 ​ ( 5 + 1 − 2 ​ i) + ϕ 2 n + 1 ​ ( 5 − 1 + 2 ​ i)). ∎ \displaystyle=\frac{1}{2\sqrt{5}}\left(\phi_{1}^{n+1}\left(\sqrt{5}+1-2i\right)+\phi_{2}^{n+1}\left(\sqrt{5}-1+2i\right)\right).\qed |  |

Table 1 shows the first numbers F n [i] F_{n}^{\left[i\right]} and their coincidence with some remarkable sequences in the OIES 1 1 1 Many integer sequences and their properties are to be found electronically on the On-Line Encyclopedia of Sequences, [27]..

i i | { F n [i] } n ≥ 0 \left\{F_{n}^{\left[i\right]}\right\}_{n\geq 0} |

1 | { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, … } \left\{1,1,2,3,5,8,13,21,34,55,89,144,...\right\}, | (A000045). |

2 | { 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, … } \left\{1,2,3,5,8,13,21,34,55,89,144,233,...\right\}, | (A000045). |

3 | { 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, … } \left\{1,3,4,7,11,18,29,47,76,123,199,322,...\right\}, | (A000204). |

4 | { 1, 4, 5, 9, 14, 23, 37, 60, 97, 157, 254, 411, … } \left\{1,4,5,9,14,23,37,60,97,157,254,411,...\right\}, | (A000285). |

5 | { 1, 5, 6, 11, 17, 28, 45, 73, 118, 191, 309, 500, … } \left\{1,5,6,11,17,28,45,73,118,191,309,500,...\right\}, | (A022095). |

6 | { 1, 6, 7, 13, 20, 33, 53, 86, 139, 225, 364, 589, … } \left\{1,6,7,13,20,33,53,86,139,225,364,589,...\right\}, | (A022096). |

Table 1: First numbers F n [i] F_{n}^{\left[i\right]}.

The following proposition relates the Fibonacci word *f*with *f*[i] \textbf{\emph{f}}^{\left[i\right]}.

###### Proposition 4.

Let φ i: { 𝟶, 𝟷 } ∗ → { 𝟶, 𝟷 } ∗ \varphi_{i}:\left\{\verb"0",\verb"1"\right\}^{*}\rightarrow\left\{\verb"0",\verb"1"\right\}^{*} be the morphism defined by φ i ​ ( 𝟶) = 𝟶 \varphi_{i}(\verb"0")=\verb"0" and φ i ​ ( 𝟷) = 𝟶 i ​ 𝟷 \varphi_{i}(\verb"1")=\verb"0"^{i}\verb"1", i ≥ 0 i\geq 0, then

 | f [i + 2] = φ i ​ ( f) \displaystyle\textbf{f}^{\,\left[i+2\right]}=\varphi_{i}\left(\textbf{f}\right) |  |

for all i ≥ 0 i\geq 0.

###### Proof.

It suffices to prove that ​ f n − 1 [i + 2] = φ i ​ ( f n) \emph{f}_{n-1}^{\,\left[i+2\right]}=\varphi_{i}(f_{n}) for all integers n ≥ 2 n\geq 2 and i ≥ 0 i\geq 0. We prove this by induction on n n. For n = 2 n=2 we have φ i ​ ( f 2) = φ i ​ ( 01) = 0 i + 1 ​ 1 = ​ f 1 [i + 2] \varphi_{i}(f_{2})=\varphi_{i}(\texttt{01})=\texttt{0}^{i+1}\texttt{1}=\emph{f}_{1}^{\,\left[i+2\right]}. Now suppose the result is true for n n. Then φ i ​ ( f n + 1) = φ i ​ ( f n ​ f n − 1) = φ i ​ ( ​ f n) ​ φ i ​ ( ​ f n − 1) = ​ f n − 1 [i + 2] ​ ​ f n − 2 [i + 2] = ​ f n [i + 2] \varphi_{i}(f_{n+1})=\varphi_{i}(f_{n}f_{n-1})=\varphi_{i}(\emph{f}_{n})\varphi_{i}(\emph{f}_{n-1})=\emph{f}_{n-1}^{\,\left[i+2\right]}\emph{f}_{n-2}^{\,\left[i+2\right]}=\emph{f}_{n}^{\,\left[i+2\right]}. ∎

The following proposition generalizes Proposition 1.

###### Proposition 5.

The i i -Fibonacci word and the ( n, i) (n,i) -Fibonacci word, satisfy the following properties

1. i.

The word *11*is not a subword of the i i -Fibonacci word, i ≥ 2 i\geq 2.

2. ii.

Let a ​ b ab be the last two symbols of f n [i] f_{n}^{\left[i\right]}. For n ≥ 1 n\geq 1, we have a ​ b =*10*ab=\texttt{\emph{10}} if n n is even and a ​ b = 𝟶𝟷 ab=\verb"01" if n n is odd, i ≥ 2 i\geq 2.

3. iii.

The concatenation of two successive i i -Fibonacci words is “almost commutative”, i.e., f n − 1 [i] ​ f n − 2 [i] f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]} and f n − 2 [i] ​ f n − 1 [i] f_{n-2}^{\left[i\right]}f_{n-1}^{\left[i\right]} have a common prefix of length F n [i] − 2 F_{n}^{\left[i\right]}-2 for all n ≥ 2 n\geq 2 and i ≥ 2 i\geq 2.

4. iv.

Φ ⁡ ( f n [i]) \Phi(f_{n}^{\left[i\right]}) is a palindrome for all n ≥ 1 n\geq 1.

5. v.

For all n ≥ 6 n\geq 6, f n [i] = f n − 3 [i] ​ f n − 3 [i] ​ f n − 6 [i] ​ l n − 3 [i] ​ l n − 3 [i] f_{n}^{\left[i\right]}=f_{n-3}^{\left[i\right]}f_{n-3}^{\left[i\right]}f_{n-6}^{\left[i\right]}l_{n-3}^{\left[i\right]}l_{n-3}^{\left[i\right]}, where l n [i] = Φ ⁡ ( f n [i]) ​ b ​ a l_{n}^{\left[i\right]}=\Phi(f_{n}^{\left[i\right]})ba.

###### Proof.

1. i. i.

It suffices to prove that 𝟷𝟷 \verb"11" is not a subword of f n [i] f_{n}^{\left[i\right]}, for n ≥ 0 n\geq 0. By induction on n n. For n = 0, 1 n=0,1 it is clear. Assume for all j < n j<n; we prove it for n n. We know that f n [i] = f n − 1 [i] ​ f n − 2 [i] f_{n}^{\left[i\right]}=f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]} so by the induction hypothesis we have that 𝟷𝟷 \verb"11" is not a subword of f n − 1 [i] f_{n-1}^{\left[i\right]} and f n − 2 [i] f_{n-2}^{\left[i\right]}. Therefore, the only possibility is that 𝟷 \verb"1" is a suffix of f n − 1 [i] f_{n-1}^{\left[i\right]} and 𝟷 \verb"1" is a prefix of f n − 2 [i] f_{n-2}^{\left[i\right]}, but this is impossible.

2. i ​ i. ii.

It is clear by induction on n n.

3. i ​ i ​ i. iii.

By definition of f n [i] f_{n}^{\left[i\right]}, we have

 | f n − 1 [i] ​ f n − 2 [i] \displaystyle f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]} | = f n − 2 [i] ​ f n − 3 [i] ⋅ f n − 3 [i] ​ f n − 4 [i] = f n − 3 [i] ​ f n − 4 [i] ⋅ f n − 3 [i] ​ f n − 3 [i] ​ f n − 4 [i], \displaystyle=f_{n-2}^{\left[i\right]}f_{n-3}^{\left[i\right]}\cdot f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}=f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}\cdot f_{n-3}^{\left[i\right]}f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}, |  |

 | f n − 2 [i] ​ f n − 1 [i] \displaystyle f_{n-2}^{\left[i\right]}f_{n-1}^{\left[i\right]} | = f n − 3 [i] ​ f n − 4 [i] ⋅ f n − 2 [i] ​ f n − 3 [i] = f n − 3 [i] ​ f n − 4 [i] ⋅ f n − 3 [i] ​ f n − 4 [i] ⋅ f n − 3 [i]. \displaystyle=f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}\cdot f_{n-2}^{\left[i\right]}f_{n-3}^{\left[i\right]}=f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}\cdot f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}\cdot f_{n-3}^{\left[i\right]}. |  |

Hence the words have a common prefix of length F n − 3 [i] + F n − 4 [i] + F n − 3 [i] F_{n-3}^{\left[i\right]}+F_{n-4}^{\left[i\right]}+F_{n-3}^{\left[i\right]}. By the induction hypothesis f n − 3 [i] ​ f n − 4 [i] f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]} and f n − 4 [i] ​ f n − 3 [i] f_{n-4}^{\left[i\right]}f_{n-3}^{\left[i\right]} have common prefix of length F n − 2 [i] − 2 F_{n-2}^{\left[i\right]}-2. Therefore the words have a common prefix of length

 | 2 ​ F n − 3 [i] + F n − 4 [i] + F n − 2 [i] − 2 = F n − 2 [i] + F n − 1 [i] − 2 = F n [i] − 2. 2F_{n-3}^{\left[i\right]}+F_{n-4}^{\left[i\right]}+F_{n-2}^{\left[i\right]}-2=F_{n-2}^{\left[i\right]}+F_{n-1}^{\left[i\right]}-2=F_{n}^{\left[i\right]}-2. |  |

4. i ​ v. iv.

By induction on n n. If n = 2 n=2 then Φ ⁡ ( f 2 [i]) = 0 i \Phi(f_{2}^{\left[i\right]})=\texttt{0}^{i}. Now suppose that the result is true for all j < n j<n; we prove it for n n. Then

 | ( Φ ⁡ ( f n [i])) R = ( Φ ⁡ ( f n − 1 [i] ​ f n − 2 [i])) R = ( f n − 1 [i] ​ Φ ​ ( f n − 2 [i])) R = Φ ​ ( f n − 2 [i]) R ​ ( f n − 1 [i]) R = Φ ⁡ ( f n − 2 [i]) ​ ( f n − 1 [i]) R. \displaystyle(\Phi(f_{n}^{\left[i\right]}))^{R}=(\Phi(f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]}))^{R}=(f_{n-1}^{\left[i\right]}\Phi(f_{n-2}^{\left[i\right]}))^{R}=\Phi(f_{n-2}^{\left[i\right]})^{R}(f_{n-1}^{\left[i\right]})^{R}=\Phi(f_{n-2}^{\left[i\right]})(f_{n-1}^{\left[i\right]})^{R}. |  |

If n n is even then f n [i] = Φ ⁡ ( f n [i]) ​ 𝟷𝟶 f_{n}^{\left[i\right]}=\Phi(f_{n}^{\left[i\right]})\verb"10" and

 | Φ ​ ( f n [i]) R \displaystyle\Phi(f_{n}^{\left[i\right]})^{R} | = Φ ⁡ ( f n − 2 [i]) ​ ( Φ ⁡ ( f n − 1 [i]) ​ 01) R = Φ ⁡ ( f n − 2 [i]) ​ 10 ​ Φ ​ ( f n − 1 [i]) R = f n − 2 [i] ​ Φ ​ ( f n − 1 [i]) = Φ ⁡ ( f n [i]). \displaystyle=\Phi(f_{n-2}^{\left[i\right]})(\Phi(f_{n-1}^{\left[i\right]})\texttt{01})^{R}=\Phi(f_{n-2}^{\left[i\right]})\texttt{10}\Phi(f_{n-1}^{\left[i\right]})^{R}=f_{n-2}^{\left[i\right]}\Phi(f_{n-1}^{\left[i\right]})=\Phi(f_{n}^{\left[i\right]}). |  |

If n n is odd, the proof is analogous.

5. v. v.

By definition of f n [i] f_{n}^{\left[i\right]}, we have

 | f n [i] \displaystyle f_{n}^{\left[i\right]} | = f n − 1 [i] ​ f n − 2 [i] = ( f n − 2 [i] ​ f n − 3 [i]) ​ ( f n − 3 [i] ​ f n − 4 [i]) \displaystyle=f_{n-1}^{\left[i\right]}f_{n-2}^{\left[i\right]}=(f_{n-2}^{\left[i\right]}f_{n-3}^{\left[i\right]})(f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}) |  |

 |  | = ( f n − 3 [i] ​ f n − 4 [i]) ​ ( f n − 4 [i] ​ f n − 5 [i]) ​ f n − 3 [i] ​ f n − 4 [i] \displaystyle=(f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]})(f_{n-4}^{\left[i\right]}f_{n-5}^{\left[i\right]})f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]} |  |

 |  | = f n − 3 [i] ​ f n − 4 [i] ​ ( f n − 5 [i] ​ f n − 6 [i]) ​ f n − 5 [i] ​ ( f n − 4 [i] ​ f n − 5 [i]) ​ f n − 4 [i] \displaystyle=f_{n-3}^{\left[i\right]}f_{n-4}^{\left[i\right]}(f_{n-5}^{\left[i\right]}f_{n-6}^{\left[i\right]})f_{n-5}^{\left[i\right]}(f_{n-4}^{\left[i\right]}f_{n-5}^{\left[i\right]})f_{n-4}^{\left[i\right]} |  |

 |  | = f n − 3 [i] ​ ( f n − 4 [i] ​ f n − 5 [i]) ​ f n − 6 [i] ​ ( f n − 5 [i] ​ f n − 4 [i]) ​ ( f n − 5 [i] ​ f n − 4 [i]) \displaystyle=f_{n-3}^{\left[i\right]}(f_{n-4}^{\left[i\right]}f_{n-5}^{\left[i\right]})f_{n-6}^{\left[i\right]}(f_{n-5}^{\left[i\right]}f_{n-4}^{\left[i\right]})(f_{n-5}^{\left[i\right]}f_{n-4}^{\left[i\right]}) |  |

 |  | = f n − 3 [i] ​ f n − 3 [i] ​ f n − 6 [i] ​ l n − 3 [i] ​ l n − 3 [i]. ∎ \displaystyle=f_{n-3}^{\left[i\right]}f_{n-3}^{\left[i\right]}f_{n-6}^{\left[i\right]}l_{n-3}^{\left[i\right]}l_{n-3}^{\left[i\right]}.\qed |  |

###### Theorem 1.

Let α = [0, i, 1 ¯] \alpha=\left[0,i,\overline{1}\right] be an irrational number, with i i a positive integer, then

 | w ​ ( α) = f [i]. \displaystyle\textbf{w}(\alpha)=\textbf{f}^{\,\left[i\right]}. |  |

###### Proof.

Let α = [0, i, 1 ¯] \alpha=\left[0,i,\overline{1}\right] an irrational number, then its associated standard sequence is

 | s − 1 = 1, s 0 = 0, s 1 = s 0 i − 1 ​ s − 1 = 0 i − 1 ​ 1 ​ and ​ s n = s n − 1 ​ s n − 2, n ≥ 2. \displaystyle s_{-1}=\texttt{1},\ \ s_{0}=\texttt{0},\ \ s_{1}=s_{0}^{i-1}s_{-1}=\texttt{0}^{i-1}\texttt{1}\ \text{and}\ s_{n}=s_{n-1}s_{n-2},\ n\geq 2. |  |

Hence { s n } n ≥ 0 = { f n [i] } n ≥ 0 \left\{s_{n}\right\}_{n\geq 0}=\left\{f_{n}^{\left[i\right]}\right\}_{n\geq 0} and from Eq. ( 1), we have

 | *w*​ ( α) \displaystyle\textbf{\emph{w}}(\alpha) | = lim n → ∞ s n =*f*[i]. ∎ \displaystyle=\lim_{n\rightarrow\infty}s_{n}=\textbf{\emph{f}}^{\left[i\right]}.\qed |  |

Remark. Note that

 | [0, i, 1 ¯] = 1 i + 1 1 + 1 1 + 1 ⋱ = i − ϕ i 2 − i − 1 \displaystyle\left[0,i,\overline{1}\right]=\cfrac{1}{i+\cfrac{1}{1+\cfrac{1}{1+\cfrac{1}{\ddots}}}}=\frac{i-\phi}{i^{2}-i-1} |  |

where ϕ \phi is the golden ratio.

From the above theorem, we conclude that i i -Fibonacci words are Sturmian words.

### 3.1 The i i -Fibonacci Word Fractal

###### Definition 3.

The ( n, i) (n,i) th-curve of Fibonacci, denoted by ℱ n [i] \mathcal{F}_{n}^{\left[i\right]}, is obtained by applying the odd-even drawing rule to the word f n [i] f_{n}^{\left[i\right]}. The i i -Fibonacci word fractal ℱ [i] \mathcal{F}^{\left[i\right]} is defined as

 | ℱ [i] = lim n → ∞ ℱ n [i]. \displaystyle\mathcal{F}^{\left[i\right]}=\lim_{n\rightarrow\infty}\mathcal{F}_{n}^{\left[i\right]}. |  |

In Table 2, we show the curves ℱ 16 [i] \mathcal{F}_{16}^{\left[i\right]} for i = 1, 2, 3, 4, 5 i=1,2,3,4,5 and 6 6.

ℱ 16 [1] \mathcal{F}_{16}^{\left[1\right]} | ℱ 16 [2] \mathcal{F}_{16}^{\left[2\right]} | ℱ 16 [3] \mathcal{F}_{16}^{\left[3\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

ℱ 16 [4] \mathcal{F}_{16}^{\left[4\right]} | ℱ 16 [5] \mathcal{F}_{16}^{\left[5\right]} | ℱ 16 [6] \mathcal{F}_{16}^{\left[6\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

Table 2: Curves ℱ 16 [i] \mathcal{F}_{16}^{\left[i\right]} for i = 1, 2, 3, 4, 5 i=1,2,3,4,5 and 6 6.

The following proposition generalizes Proposition 2.

###### Proposition 6.

The i i -Fibonacci word fractal and the curve ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} have the following properties:

1. i.

The Fibonacci fractal ℱ [i] \mathcal{F}^{\left[i\right]} is composed only of segments of length 1 or 2.

2. ii.

The curve ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} is similar to the curve ℱ n − 3 [i] \mathcal{F}_{n-3}^{\left[i\right]}.

3. iii.

The curve ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} is composed of 5 curves: ℱ n [i] = ℱ n − 3 [i] ​ ℱ n − 3 [i] ​ ℱ n − 6 [i] ​ ℱ ′ n − 3 [i] ​ ℱ ′ n − 3 [i] \mathcal{F}_{n}^{\left[i\right]}=\mathcal{F}_{n-3}^{\left[i\right]}\mathcal{F}_{n-3}^{\left[i\right]}\mathcal{F}_{n-6}^{\left[i\right]}\mathcal{F^{\prime}}_{n-3}^{\left[i\right]}\mathcal{F^{\prime}}_{n-3}^{\left[i\right]}.

4. iv.

The curve ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} is symmetric. More precisely, the curves ℱ 3 ​ n [i] \mathcal{F}_{3n}^{\left[i\right]} and ℱ 3 ​ n + 2 [i] \mathcal{F}_{3n+2}^{\left[i\right]} are symmetric with respect to a line and the curve ℱ 3 ​ n + 1 [i] \mathcal{F}_{3n+1}^{\left[i\right]} is symmetric with respect to a point.

5. v.

The scale factor between ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} and ℱ n − 3 [i] \mathcal{F}_{n-3}^{\left[i\right]} is 1 + 2 1+\sqrt{2}.

###### Proof.

1. i. i.

It is clear from Proposition 5 - i i, because 110 and 111 are not subwords of *f*[i] \textbf{\emph{f}}^{\left[i\right]}.

2. i ​ i. ii.

By Proposition 4 we have ​ f n − 1 [i + 2] = φ i ​ ( f n) \emph{f}_{n-1}^{\,\left[i+2\right]}=\varphi_{i}(f_{n}) for all integer n ≥ 2 n\geq 2 and i ≥ 0 i\geq 0. Moreover, φ i \varphi_{i} maps the different segments as shown in Table 3.

If i i is even |

φ i ​ ( 𝟶𝟷) = 0 i + 1 ​ 1 \varphi_{i}(\verb"01")=\texttt{0}^{i+1}\texttt{1} | φ i ​ ( 10) = 0 i ​ 10 \varphi_{i}(\texttt{10})=\texttt{0}^{i}\texttt{10} | φ i ​ ( 00) = 00 \varphi_{i}(\texttt{00})=\texttt{00} |

0,-2)(13,5) | 0,-1)(11,7) | 0,-2)(10,4) |

If i i is odd |

φ i ​ ( 𝟶𝟷) = 0 i + 1 ​ 1 \varphi_{i}(\verb"01")=\texttt{0}^{i+1}\texttt{1} | φ i ​ ( 10) = 0 i ​ 10 \varphi_{i}(\texttt{10})=\texttt{0}^{i}\texttt{10} | φ i ​ ( 00) = 00 \varphi_{i}(\texttt{00})=\texttt{00} |

0,-2)(12,5) | 0,-1)(11,7) | 0,-2)(10,4) |

Table 3: Mapping of segments.

For example in Fig. 3, we show the mapping of f 10 f_{10} by φ i \varphi_{i} when i = 2, 3 i=2,3.

[image: Refer to caption] Figure 3: Mapping of φ 2 ​ ( f 10) \varphi_{2}(f_{10}) and φ 3 ​ ( f 10) \varphi_{3}(f_{10}).

Hence, it is clear that φ i \varphi_{i} preserves the geometric properties. By Proposition 2 we have ℱ n \mathcal{F}_{n} is similar to the curve ℱ n − 3 \mathcal{F}_{n-3} then ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} is similar to ℱ n − 3 [i] \mathcal{F}_{n-3}^{\left[i\right]}.

3. i ​ i ​ i. iii.

It is clear from Proposition 5 - v v.

4. i ​ v. iv.

The proof runs like in i ​ i ii.

5. v. v.

We show that

 | f n [i] = f n − 3 [i] ​ f n − 3 [i] ​ f n − 6 [i] ​ l n − 3 [i] ​ l n − 3 [i] = Φ ⁡ ( f n − 3 [i]) ​ a ​ b ​ Φ ​ ( f n − 3 [i]) ​ a ​ b ​ f n − 6 [i] ​ Φ ​ ( l n − 3 [i]) ​ b ​ a ​ Φ ​ ( l n − 3 [i]) ​ b ​ a. f_{n}^{\left[i\right]}=f_{n-3}^{\left[i\right]}f_{n-3}^{\left[i\right]}f_{n-6}^{\left[i\right]}l_{n-3}^{\left[i\right]}l_{n-3}^{\left[i\right]}=\Phi(f_{n-3}^{\left[i\right]})ab\Phi(f_{n-3}^{\left[i\right]})abf_{n-6}^{\left[i\right]}\Phi(l_{n-3}^{\left[i\right]})ba\Phi(l_{n-3}^{\left[i\right]})ba. |  |

Since a ​ b ab is either 01 or 10, and ℱ n [i] = ℱ n − 3 [i] ​ ℱ n − 3 [i] ​ ℱ n − 6 [i] ​ ℱ ′ n − 3 [i] ​ ℱ ′ n − 3 [i] \mathcal{F}_{n}^{\left[i\right]}=\mathcal{F}_{n-3}^{\left[i\right]}\mathcal{F}_{n-3}^{\left[i\right]}\mathcal{F}_{n-6}^{\left[i\right]}\mathcal{F^{\prime}}_{n-3}^{\left[i\right]}\mathcal{F^{\prime}}_{n-3}^{\left[i\right]}, then the first two curves are orthogonal and the last two curves are orthogonal. Let L n [i] L_{n}^{\left[i\right]} be the length of the curve ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} from first to last point drawn. Then L n [i] = 2 ​ L n − 3 [i] + L n − 6 [i] L_{n}^{\left[i\right]}=2L_{n-3}^{\left[i\right]}+L_{n-6}^{\left[i\right]} and by definition, the scale factor Γ \Gamma is

 | Γ = L n [i] L n − 3 [i] = L n − 3 [i] L n − 6 [i] \displaystyle\Gamma=\frac{L_{n}^{\left[i\right]}}{L_{n-3}^{\left[i\right]}}=\frac{L_{n-3}^{\left[i\right]}}{L_{n-6}^{\left[i\right]}} |  |

hence Γ ​ L n − 3 [i] = L n [i] = 2 ​ L n − 3 [i] + L n − 6 [i] = 2 ​ L n − 3 [i] + L n − 3 [i] Γ \Gamma L_{n-3}^{\left[i\right]}=L_{n}^{\left[i\right]}=2L_{n-3}^{\left[i\right]}+L_{n-6}^{\left[i\right]}=2L_{n-3}^{\left[i\right]}+\frac{L_{n-3}^{\left[i\right]}}{\Gamma}, then Γ = 1 + 2 \Gamma=1+\sqrt{2}. ∎

For each i i the system ℱ n [i] \mathcal{F}_{n}^{\left[i\right]} ( n ≥ 0 n\geq 0) has as attractor the curve ℱ \mathcal{F} (the same argument given in Proposition 6 - i ​ i ii).

## 4 Generalized Fibonacci Snowflakes

We say that a path w w is *closed*if it satisfies | w | 0 = | w | 2 |w|_{0}=|w|_{2} and | w | 1 = | w | 3 |w|_{1}=|w|_{3}. A *simple path*is a word w w such that none of its proper subwords is a closed path. A *boundary word*is a closed path such that none of its proper subwords is closed. Therefore, a *polyomino*is a subset of ℤ × ℤ \mathbb{Z}\times\mathbb{Z} contained in some boundary word.

###### Example 3.

In Fig. 4 we show a polyomino P P such that starting from point S S, (counterclockwise) the boundary b ​ ( P) \textbf{b}(P) is coded by the word w = 𝟸𝟷𝟸𝟸𝟹𝟸𝟹𝟶𝟹𝟶𝟷𝟶𝟹𝟶𝟷𝟷 w=\verb"2122323030103011". Moreover, we denoted by w ^ \widehat{w} the path traveled in the opposite direction, i.e., w ^ = ρ 2 ​ ( w R) \widehat{w}=\rho^{2}(w^{R}), where ρ 2 \rho^{2} is the morphism defined by ρ 2 ​ ( a) = 2 + a \rho^{2}(a)=2+a, a ∈ 𝒜 a\in\mathcal{A}. In this example w ^ = ρ 2 ​ ( 𝟷𝟷𝟶𝟹𝟶𝟷𝟶𝟹𝟶𝟹𝟸𝟹𝟸𝟸𝟷𝟸) = 𝟹𝟹𝟸𝟷𝟸𝟹𝟸𝟷𝟸𝟷𝟶𝟷𝟶𝟶𝟹𝟶. \widehat{w}=\rho^{2}(\verb"1103010303232212")=\verb"3321232121010030".

[image: Refer to caption] Figure 4: Polyomino P P.

In this section, we study a new generalization of Fibonacci polyominoes from i i -Fibonacci words. We use the same procedure as in [4] and we present some geometric properties.

### 4.1 Construction of Generalized Fibonacci Polyominoes

First, rewrite the i i -Fibonacci words over alphabet { 𝟶, 𝟸 } ⊂ 𝒜 \left\{\verb"0",\verb"2"\right\}\subset\mathcal{A}, specifically we apply the morphism 𝟶 → 2 , 𝟷 → 𝟶 \verb"0"\rightarrow\verb"2 ",\verb"1"\rightarrow\verb"0". Next, apply the operator Σ 1 \Sigma_{1} followed by the operator Σ 0 \Sigma_{0}, where

 | Σ α ( w) = α ⋅ ( α + w 1) ⋅ ( α + w 1 + w 2) ⋯ ( α + w 1 + w 2 + ⋯ w n), \displaystyle\Sigma_{\alpha}(w)=\alpha\cdot(\alpha+w_{1})\cdot(\alpha+w_{1}+w_{2})\cdots(\alpha+w_{1}+w_{2}+\cdots w_{n}), |  |

with α ∈ 𝒜 \alpha\in\mathcal{A} and w = w 1 w 2 ⋯ w n w=w_{1}w_{2}\cdots w_{n}. This yield the words p [i] = Σ 0 ​ Σ 1 ​*f*[i] \textbf{p}^{\left[i\right]}=\Sigma_{0}\Sigma_{1}\textbf{\emph{f}}^{\left[i\right]}.

###### Example 4.

In Table 4, we show the first words *p*[i] \textbf{\emph{p}}^{\left[i\right]}, with its corresponding curves. The case n = 2 n=2 corresponds to a version of the Fibonacci word fractal with only segments of length 1 *[4]*.

p [1] = p [2] = 𝟶𝟷𝟶𝟹𝟶𝟹𝟸𝟹𝟶𝟹𝟶𝟷 ⋯ \textbf{p}^{\left[1\right]}=\textbf{p}^{\left[2\right]}=\verb"010303230301"\cdots | p [3] = 𝟶𝟷𝟶𝟷𝟸𝟷𝟸𝟷𝟶𝟷𝟶𝟹𝟶𝟹 ⋯ \textbf{p}^{\left[3\right]}=\verb"01012121010303"\cdots | p [4] = 𝟶𝟷𝟶𝟷𝟶𝟹𝟶𝟹𝟶𝟹𝟸𝟹𝟸𝟹 ⋯ \textbf{p}^{\left[4\right]}=\verb"01010303032323"\cdots |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

p [5] = 𝟶𝟷𝟶𝟷𝟶𝟷𝟸𝟷𝟸𝟷𝟸𝟷𝟶𝟷 ⋯ \textbf{p}^{\left[5\right]}=\verb"01010121212101"\cdots | p [6] = 01010103030303 ⋯ \textbf{p}^{\left[6\right]}=\verb" 01010103030303 "\cdots | p [7] = 𝟶𝟷𝟶𝟷𝟶𝟷𝟶𝟷𝟸𝟷𝟸𝟷𝟸𝟷 ⋯ \textbf{p}^{\left[7\right]}=\verb"01010101212121"\cdots |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

Table 4: Words p [i] \textbf{p}^{\left[i\right]} and its corresponding curves.

Given a word w ∈ 𝒜 ∗ w\in\mathcal{A}^{*} we define the word Δ ( w) = ( w 2 − w 1) ⋅ ( w 3 − w 2) ⋯ ( w n − w n − 1) ∈ 𝒜 ∗ \Delta(w)=(w_{2}-w_{1})\cdot(w_{3}-w_{2})\cdots(w_{n}-w_{n-1})\in\mathcal{A}^{*}, then it is clear that Δ ⁡ ( p [i]) = Σ 1 ​*f*[i] \Delta(\textbf{p}^{\left[i\right]})=\Sigma_{1}\textbf{\emph{f}}^{\left[i\right]}. We shall denote this sequence by q [i] \textbf{q}^{\left[i\right]}. Last, we define the morphism a ¯ \overline{a}, with a ∈ 𝒜 a\in\mathcal{A}, as 0 ¯ = 𝟶, 1 ¯ = 𝟹, 2 ¯ = 𝟸, 3 ¯ = 𝟷. \overline{\texttt{0}}=\verb"0",\overline{\texttt{1}}=\verb"3",\overline{\texttt{2}}=\verb"2",\overline{\texttt{3}}=\verb"1". Moreover, the words w ∈ 𝒜 ∗ w\in\mathcal{A}^{*} satisfying w ¯ = w R \overline{w}=w^{R} are called*antipalindromes*.

###### Definition 4.

Consider the sequence { q n [i] } n ≥ 0 \left\{q_{n}^{\left[i\right]}\right\}_{n\geq 0} defined by:

- •

If i i is even, q 0 [i] = ϵ q_{0}^{\left[i\right]}=\epsilon, q 1 [i] = 𝟷 q_{1}^{\left[i\right]}=\verb"1", q 2 [i] = ( 𝟷𝟹) i 2 q_{2}^{\left[i\right]}=(\verb"13")^{\frac{i}{2}} and

 | q n [i] = { q n − 1 [i] ​ q n − 2 [i], n ≅ 1 mod 3 q n − 1 [i] ​ q n − 2 [i] ¯, n ≅ 0, 2 mod 3. \displaystyle q_{n}^{\left[i\right]}=\begin{cases}q_{n-1}^{\left[i\right]}q_{n-2}^{\left[i\right]},&\ n\cong 1\mod 3\\ q_{n-1}^{\left[i\right]}\overline{q_{n-2}^{\left[i\right]}},&\ n\cong 0,2\mod 3.\end{cases} |  |

- •

If i i is odd, q 0 [i] = ϵ q_{0}^{\left[i\right]}=\epsilon, q 1 [i] ​ =1 q_{1}^{\left[i\right]}\verb"=1", q 2 [i] = ( 𝟷𝟹) i − 1 2 ​ 𝟷 q_{2}^{\left[i\right]}=(\verb"13")^{\frac{i-1}{2}}\verb"1" and

 | q n [i] = { q n − 1 [i] ​ q n − 2 [i], n ≅ 0 mod 3 q n − 1 [i] ​ q n − 2 [i] ¯, n ≅ 1, 2 mod 3. \displaystyle q_{n}^{\left[i\right]}=\begin{cases}q_{n-1}^{\left[i\right]}q_{n-2}^{\left[i\right]},&\ n\cong 0\mod 3\\ q_{n-1}^{\left[i\right]}\overline{q_{n-2}^{\left[i\right]}},&\ n\cong 1,2\mod 3.\end{cases} |  |

It is clear that | q n [i] | = F n − 1 [i] |q_{n}^{\left[i\right]}|=F_{n-1}^{\left[i\right]}.

###### Example 5.

The first terms of { q n [i] } n ≥ 0 \left\{q_{n}^{\left[i\right]}\right\}_{n\geq 0} are:

{ q n [2] } n ≥ 0 = { ϵ ​, 1, 13, 133, 13313, 13313311, 1331331131131, ​ … } \left\{q_{n}^{\left[2\right]}\right\}_{n\geq 0}=\left\{\epsilon\verb", 1, 13, 133, 13313, 13313311, 1331331131131,"\ldots\right\}, |

{ q n [3] } n ≥ 0 = { ϵ ​, 1, 131, 1311, 1311313, 13113133133, 131131331331311313, ​ … ​ … } \left\{q_{n}^{\left[3\right]}\right\}_{n\geq 0}=\left\{\epsilon\verb", 1, 131, 1311, 1311313, 13113133133, 131131331331311313,"\ldots\ldots\right\}, |

{ q n [4] } n ≥ 0 = { ϵ ​, 1, 1313, 13133, 131331313, 13133131331311, ​ … } \left\{q_{n}^{\left[4\right]}\right\}_{n\geq 0}=\left\{\epsilon\verb", 1, 1313, 13133, 131331313, 13133131331311,"\ldots\right\}, |

{ q n [5] } n ≥ 0 = { ϵ ​, 1, 13131, 131311, 13131131313, 13131131313313133, ​ … } \left\{q_{n}^{\left[5\right]}\right\}_{n\geq 0}=\left\{\epsilon\verb", 1, 13131, 131311, 13131131313, 13131131313313133,"\ldots\right\}. |

The following propositions generalize the case when i = 2 i=2, [4].

###### Proposition 7.

The word *q*[i] = Σ 1 ​ f [i] \textbf{\emph{q}}^{\left[i\right]}=\Sigma_{1}\textbf{f}^{\left[\,i\right]} is the limit of the sequence { q n [i] } n ≥ 0 \left\{q_{n}^{\left[i\right]}\right\}_{n\geq 0}.

###### Proof.

We know that Δ ⁡ ( q [i]) =*f*[i] \Delta(\textbf{q}^{\left[i\right]})=\textbf{\emph{f}}^{\left[i\right]}, then it suffices to prove that Δ ⁡ ( q n [i]) ​ α n − 1 = f n − 1 [i] \Delta(q_{n}^{\left[i\right]})\alpha_{n-1}=f_{n-1}^{\left[i\right]} for all n ≥ 2 n\geq 2, where α n = 2 \alpha_{n}=\texttt{2} if n n is even and α n = 0 \alpha_{n}=\texttt{0} if n n is odd. By induction on n n. If i i is even, then

 | Δ ⁡ ( q 2 [i]) ​ α 1 \displaystyle\Delta(q_{2}^{\left[i\right]})\alpha_{1} | = Δ ⁡ ( ( 13) i / 2) ​ α 1 = ( 22) i / 2 − 1 ​ 20 = 2 i − 2 ​ 20 = 2 i − 1 ​ 0 = f 1 [i], \displaystyle=\Delta((\texttt{13})^{i/2})\alpha_{1}=(\texttt{22})^{i/2-1}\texttt{20}=\texttt{2}^{i-2}\texttt{20}=\texttt{2}^{i-1}\texttt{0}=f_{1}^{\left[i\right]}, |  |

 | Δ ⁡ ( q 3 [i]) ​ α 2 \displaystyle\Delta(q_{3}^{\left[i\right]})\alpha_{2} | = Δ ⁡ ( ( 13) i / 2 ​ 3) ​ α 2 = 2 i − 1 ​ 02 = f 1 [i] ​ f 0 [i] = f 2 [i], \displaystyle=\Delta((\texttt{13})^{i/2}\texttt{3})\alpha_{2}=\texttt{2}^{i-1}\texttt{02}=f_{1}^{\left[i\right]}f_{0}^{\left[i\right]}=f_{2}^{\left[i\right]}, |  |

 | Δ ⁡ ( q 4 [i]) ​ α 3 \displaystyle\Delta(q_{4}^{\left[i\right]})\alpha_{3} | = Δ ⁡ ( ( 13) i / 2 ​ 3 ​ ( 13) i / 2) ​ α 3 = 2 i − 1 ​ 0 2 i ​ 0 = f 2 [i] ​ f 1 [i] = f 3 [i]. \displaystyle=\Delta((\texttt{13})^{i/2}\texttt{3}(\texttt{13})^{i/2})\alpha_{3}=\texttt{2}^{i-1}\texttt{0}\texttt{2}^{i}\texttt{0}=f_{2}^{\left[i\right]}f_{1}^{\left[i\right]}=f_{3}^{\left[i\right]}. |  |

Assume for all m m, with 2 ≤ m < n 2\leq m<n; we prove it for n n. We only prove the case n ≅ 1 mod 3 n\cong 1\mod 3, since the argument is similar for the other cases. Let n = 3 ​ k + 1 n=3k+1 for some integer k k. Then

 | Δ ⁡ ( q 3 ​ k + 1 [i]) ​ α 3 ​ k \displaystyle\Delta(q_{3k+1}^{\left[i\right]})\alpha_{3k} | = Δ ⁡ ( q 3 ​ k [i] ​ q 3 ​ k − 1 [i]) ​ α 3 ​ k = Δ ⁡ ( q 3 ​ k [i]) ​ α 3 ​ k − 1 ​ Δ ​ ( q 3 ​ k − 1 [i]) ​ α 3 ​ k − 2 = f 3 ​ k − 1 [i] ​ f 3 ​ k − 2 [i] = f 3 ​ k [i]. \displaystyle=\Delta(q_{3k}^{\left[i\right]}q_{3k-1}^{\left[i\right]})\alpha_{3k}=\Delta(q_{3k}^{\left[i\right]})\alpha_{3k-1}\Delta(q_{3k-1}^{\left[i\right]})\alpha_{3k-2}=f_{3k-1}^{\left[i\right]}f_{3k-2}^{\left[i\right]}=f_{3k}^{\left[i\right]}. |  |

If i i is odd, the proof is similar. ∎

###### Proposition 8.

Let n ∈ ℕ n\in\mathbb{N} and σ n =*1*\sigma_{n}=\texttt{\emph{1}} if n n is even and σ n =*3*\sigma_{n}=\texttt{\emph{3}} if n n is odd. Then if i i is even q 3 ​ n + 1 [i] = r ​ σ n, q 3 ​ n + 2 [i] = m ​ σ n ¯ q_{3n+1}^{\left[i\right]}=r\sigma_{n},q_{3n+2}^{\left[i\right]}=m\overline{\sigma_{n}} and q 3 ​ n + 3 [i] = p ​ σ n ¯ q_{3n+3}^{\left[i\right]}=p\overline{\sigma_{n}} for some antipalindrome p p and some palindromes r r, m m. If i i is odd q 3 ​ n + 1 [i] = r ​ σ n ¯, q 3 ​ n + 2 [i] = m ​ σ n ¯ q_{3n+1}^{\left[i\right]}=r\overline{\sigma_{n}},q_{3n+2}^{\left[i\right]}=m\overline{\sigma_{n}} and q 3 ​ n + 3 [i] = p ​ σ n q_{3n+3}^{\left[i\right]}=p\sigma_{n} for some antipalindrome m m and some palindromes r r, p p.

###### Proof.

The proof is by induction on n n. If i i is even, for n = 0 n=0 we have q 1 [i] = ϵ ⋅ 1, q 2 [i] = ( 13) i / 2 = ( ( 13) i 2 − 1 ​ 1) ​ 3 = ( ( 13) i 2 − 1 ​ 1) ⋅ 1 ¯ q_{1}^{\left[i\right]}=\epsilon\cdot\texttt{1},q_{2}^{\left[i\right]}=(\texttt{13})^{i/2}=((\texttt{13})^{\frac{i}{2}-1}\texttt{1})\texttt{3}=((\texttt{13})^{\frac{i}{2}-1}\texttt{1})\cdot\overline{\texttt{1}} and q 3 [i] = ( 13) i / 2 ​ 3 = ( 13) i / 2 ⋅ 1 ¯ q_{3}^{\left[i\right]}=(\texttt{13})^{i/2}\texttt{3}=(\texttt{13})^{i/2}\cdot\overline{\texttt{1}}. Now, suppose that q 3 ​ n + 1 = r ​ σ n, q 3 ​ n + 2 = m ​ σ n ¯ q_{3n+1}=r\sigma_{n},q_{3n+2}=m\overline{\sigma_{n}} and q 3 ​ n + 3 = p ​ σ n ¯ q_{3n+3}=p\overline{\sigma_{n}} for some antipalindrome p p and some palindromes r r, m m. Then

 | q 3 ​ n + 4 [i] \displaystyle q_{3n+4}^{\left[i\right]} | = q 3 ​ n + 3 [i] ​ q 3 ​ n + 2 [i] = q 3 ​ n + 2 [i] ​ q 3 ​ n + 1 [i] ¯ ​ q 3 ​ n + 2 [i] = m ​ σ n ¯ ⋅ r ​ σ n ¯ ⋅ m ​ σ n ¯ = m ​ σ n ​ r ​ σ n ¯ ​ m ⋅ σ n + 1, \displaystyle=q_{3n+3}^{\left[i\right]}q_{3n+2}^{\left[i\right]}=q_{3n+2}^{\left[i\right]}\overline{q_{3n+1}^{\left[i\right]}}q_{3n+2}^{\left[i\right]}=m\overline{\sigma_{n}}\cdot\overline{r\sigma_{n}}\cdot m\overline{\sigma_{n}}=m\overline{\sigma_{n}r\sigma_{n}}m\cdot\sigma_{n+1}, |  |

 | q 3 ​ n + 5 [i] \displaystyle q_{3n+5}^{\left[i\right]} | = q 3 ​ n + 4 [i] ​ q 3 ​ n + 3 [i] ¯ = q 3 ​ n + 3 [i] ​ q 3 ​ n + 2 [i] ​ q 3 ​ n + 3 [i] ¯ = p ​ σ n ¯ ⋅ m ​ σ n ¯ ⋅ p ​ σ n ¯ ¯ = p ​ σ n ¯ ​ m ​ σ n ​ p ¯ ⋅ σ n + 1 ¯, \displaystyle=q_{3n+4}^{\left[i\right]}\overline{q_{3n+3}^{\left[i\right]}}=q_{3n+3}^{\left[i\right]}q_{3n+2}^{\left[i\right]}\overline{q_{3n+3}^{\left[i\right]}}=p\overline{\sigma_{n}}\cdot m\overline{\sigma_{n}}\cdot\overline{p\overline{\sigma_{n}}}=p\overline{\sigma_{n}}m\overline{\sigma_{n}p}\cdot\overline{\sigma_{n+1}}, |  |

 | q 3 ​ n + 6 [i] \displaystyle q_{3n+6}^{\left[i\right]} | = q 3 ​ n + 5 [i] ​ q 3 ​ n + 4 [i] ¯ = q 3 ​ n + 4 [i] ​ q 3 ​ n + 3 [i] ¯ ​ q 3 ​ n + 4 [i] ¯ = m ​ σ n ​ r ​ σ n ¯ ​ m ​ σ n ¯ ⋅ p ​ σ n + 1 ¯ ⋅ m ¯ ​ σ n ​ r ​ σ n ​ m ¯ ​ σ n \displaystyle=q_{3n+5}^{\left[i\right]}\overline{q_{3n+4}^{\left[i\right]}}=q_{3n+4}^{\left[i\right]}\overline{q_{3n+3}^{\left[i\right]}}\overline{q_{3n+4}^{\left[i\right]}}=m\overline{\sigma_{n}r\sigma_{n}}m\overline{\sigma_{n}}\cdot\overline{p\sigma_{n+1}}\cdot\overline{m}\sigma_{n}r\sigma_{n}\overline{m}\sigma_{n} |  |

 |  | = m ​ σ n ​ r ​ σ n ¯ ​ m ​ σ n ​ p ¯ ​ σ n ​ m ¯ ​ σ n ​ r ​ σ n ​ m ¯ ⋅ σ n + 1 ¯ \displaystyle=m\overline{\sigma_{n}r\sigma_{n}}m\overline{\sigma_{n}p}\sigma_{n}\overline{m}\sigma_{n}r\sigma_{n}\overline{m}\cdot\overline{\sigma_{n+1}} |  |

with palindromes m ​ σ n ​ r ​ σ n ¯ ​ m m\overline{\sigma_{n}r\sigma_{n}}m and p ​ σ n ¯ ​ m ​ σ n ​ p ¯ p\overline{\sigma_{n}}m\overline{\sigma_{n}p}, and antipalindrome m ​ σ n ​ r ​ σ n ¯ ​ m ​ σ n ​ p ¯ ​ σ n ​ m ¯ ​ σ n ​ r ​ σ n ​ m ¯ m\overline{\sigma_{n}r\sigma_{n}}m\overline{\sigma_{n}p}\sigma_{n}\overline{m}\sigma_{n}r\sigma_{n}\overline{m}. If i i is odd, the proof is similar. ∎

###### Proposition 9.

Let n n be a positive integer and α ∈ 𝒜 \alpha\in\mathcal{A} then

1. i.

The path Σ α ​ q n [i] \Sigma_{\alpha}q_{n}^{\left[i\right]} is simple.

2. ii.

If i i is even, then the path Σ α ∘ ​ ( q 3 ​ n [i]) 4 \Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4} is the boundary word of a polyomino.

3. iii.

If i i is odd, then the path Σ α ∘ ​ ( q 3 ​ n + 2 [i]) 4 \Sigma_{\alpha}^{\circ}(q_{3n+2}^{\left[i\right]})^{4} is the boundary word of a polyomino.

Where Σ α ∘ ( w) = α ⋅ ( α + w 1) ⋅ ( α + w 1 + w 2) ⋯ ( α + w 1 + w 2 + ⋯ w n − 1) \Sigma^{\circ}_{\alpha}(w)=\alpha\cdot(\alpha+w_{1})\cdot(\alpha+w_{1}+w_{2})\cdots(\alpha+w_{1}+w_{2}+\cdots w_{n-1}).

###### Proof.

1. i. i.

The proof is by induction on n n. It is the similar to [4] or [7], we only describe the basic ideas because the proof is rather technical. For n = 1, 2, 3 n=1,2,3 it is clear. Assume for all j j such that 1 ⩽ j < n 1\leqslant j<n; we prove it for n n. The idea is to divide the path Σ α ​ q n [i] \Sigma_{\alpha}q_{n}^{\left[i\right]} into three smaller parts, for example the path Σ 0 ​ q 12 [5] \Sigma_{0}q_{12}^{\left[5\right]} is divided into parts Σ 0 ​ q 10 [5] \Sigma_{0}q_{10}^{\left[5\right]}, Σ 2 ​ q 9 [5] \Sigma_{2}q_{9}^{\left[5\right]} and Σ 3 ​ q 10 [5] \Sigma_{3}q_{10}^{\left[5\right]}, (see Fig. 5).

[image: Refer to caption]
Figure 5: Σ 0 ​ q 12 [5] \Sigma_{0}q_{12}^{\left[5\right]} is divide into parts Σ 0 ​ q 10 [5] \Sigma_{0}q_{10}^{\left[5\right]}, Σ 2 ​ q 9 [5] \Sigma_{2}q_{9}^{\left[5\right]} and Σ 3 ​ q 10 [5] \Sigma_{3}q_{10}^{\left[5\right]}.

By the induction hypothesis Σ α 1 ​ q n − 2 [i] \Sigma_{\alpha_{1}}q_{n-2}^{\left[i\right]} and Σ α 2 ​ q n − 3 [i] \Sigma_{\alpha_{2}}q_{n-3}^{\left[i\right]} are simples, moreover, the three smaller paths are contained in disjoint boxes, then Σ α 1 ​ q n − 2 [i] \Sigma_{\alpha_{1}}q_{n-2}^{\left[i\right]} is simple.

2. i ​ i. ii.

If i i is even. From Proposition 8, we have q 3 ​ n [i] = p ​ σ n − 1 ¯ q_{3n}^{\left[i\right]}=p\overline{\sigma_{n-1}} for some antipalindrome p = w 1 ⋯ w n p=w_{1}\cdots w_{n} and σ n − 1 ¯ ∈ { 1, 3 } \overline{\sigma_{n-1}}\in\left\{\texttt{1},\texttt{3}\right\}. If σ n − 1 ¯ = 3 \overline{\sigma_{n-1}}=\texttt{3}, we can consider the reversal of the path, so suppose that σ n − 1 ¯ = 1 \overline{\sigma_{n-1}}=\texttt{1}. Hence Σ α ∘ ​ ( q 3 ​ n [i]) 4 = Σ α ​ ( p ​ 1 ⋅ p ​ 1 ⋅ p ​ 1 ⋅ p) \Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4}=\Sigma_{\alpha}(p\texttt{1}\cdot p\texttt{1}\cdot p\texttt{1}\cdot p), as

 | Σ α p 1 = α ⋅ ( α + w 1) ⋅ ( α + w 1 + w 2) ⋯ ( α + w 1 + w 2 + ⋯ w n + 1) \Sigma_{\alpha}p\texttt{1}=\alpha\cdot(\alpha+w_{1})\cdot(\alpha+w_{1}+w_{2})\cdots(\alpha+w_{1}+w_{2}+\cdots w_{n}+1) |  |

and | p | 1 = | p | 3 |p|_{1}=|p|_{3}, because p p is an antipalindrome, then

 | α + w 1 + w 2 + ⋯ w n + 1 = α + | p | 1 + 3 | p | 3 + 1 = α + 4 | p | 1 + 1 ≅ α + 1 mod 4. \displaystyle\alpha+w_{1}+w_{2}+\cdots w_{n}+1=\alpha+|p|_{1}+3|p|_{3}+1=\alpha+4|p|_{1}+1\cong\alpha+1\mod 4. |  |

Therefore

 | Σ α ∘ ​ ( q 3 ​ n [i]) 4 = Σ α ​ ( p ​ 1 ⋅ p ​ 1 ⋅ p ​ 1 ⋅ p) = Σ α ​ p ⋅ Σ α + 1 ​ p ⋅ Σ α + 2 ​ p ⋅ Σ α + 3 ​ p. \displaystyle\Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4}=\Sigma_{\alpha}(p\texttt{1}\cdot p\texttt{1}\cdot p\texttt{1}\cdot p)=\Sigma_{\alpha}p\cdot\Sigma_{\alpha+1}p\cdot\Sigma_{\alpha+2}p\cdot\Sigma_{\alpha+3}p. |  |

But, the initial segments in the paths Σ α ​ p \Sigma_{\alpha}p and Σ α + 1 ​ p \Sigma_{\alpha+1}p are orthogonal because α \alpha and α + 1 \alpha+1 represent orthogonal vectors. Hence Σ α ​ p ⋅ Σ α + 1 ​ p ⋅ Σ α + 2 ​ p ⋅ Σ α + 3 ​ p \Sigma_{\alpha}p\cdot\Sigma_{\alpha+1}p\cdot\Sigma_{\alpha+2}p\cdot\Sigma_{\alpha+3}p is a closed polygonal path, illustrated in Fig. 6 with an angle of π / 2 \pi/2 counterclockwise.

[image: Refer to caption]
Figure 6: Case i ​ i ii with an angle of π / 2 \pi/2.
3. i ​ i ​ i. iii.

If i i is odd, the proof is similar.

∎

An *i i -generalized Fibonacci snowflake of order n n*is a polyomino having Σ α ∘ ​ ( q 3 ​ n [i]) 4 \Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4} or Σ α ∘ ​ ( q 3 ​ n + 2 [i]) 4 \Sigma_{\alpha}^{\circ}(q_{3n+2}^{\left[i\right]})^{4} as a boundary word, we denote this as ∏ n [i] \prod_{n}^{\left[i\right]}. In Table 5 we show first i i -generalized Fibonacci snowflakes.

∏ 1 [2] \prod_{1}^{\left[2\right]} | ∏ 2 [2] \prod_{2}^{\left[2\right]} | ∏ 3 [2] \prod_{3}^{\left[2\right]} | ∏ 4 [2] \prod_{4}^{\left[2\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

∏ 1 [3] \prod_{1}^{\left[3\right]} | ∏ 2 [3] \prod_{2}^{\left[3\right]} | ∏ 3 [3] \prod_{3}^{\left[3\right]} | ∏ 4 [3] \prod_{4}^{\left[3\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

∏ 1 [4] \prod_{1}^{\left[4\right]} | ∏ 2 [4] \prod_{2}^{\left[4\right]} | ∏ 3 [4] \prod_{3}^{\left[4\right]} | ∏ 4 [4] \prod_{4}^{\left[4\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

∏ 1 [5] \prod_{1}^{\left[5\right]} | ∏ 2 [5] \prod_{2}^{\left[5\right]} | ∏ 3 [5] \prod_{3}^{\left[5\right]} | ∏ 4 [5] \prod_{4}^{\left[5\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

∏ 1 [6] \prod_{1}^{\left[6\right]} | ∏ 2 [6] \prod_{2}^{\left[6\right]} | ∏ 3 [6] \prod_{3}^{\left[6\right]} | ∏ 4 [6] \prod_{4}^{\left[6\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

Table 5: The i i -Generalized Fibonacci Snowflakes ∏ n [i] \prod_{n}^{\left[i\right]} for i = 2, 3, 4, 5, 6 i=2,3,4,5,6 and n = 1, 2, 3, 4 n=1,2,3,4.

###### Theorem 2.

The i i -generalized Fibonacci snowflake of order n ≥ 1 n\geq 1 is a double square, for all positive integers i i.

###### Proof.

Suppose that i i even. We show in Proposition 9 - i ​ i ii that

 | Σ α ∘ ​ ( q 3 ​ n [i]) 4 = Σ α ​ ( p ​ 1 ⋅ p ​ 1 ⋅ p ​ 1 ⋅ p) = Σ α ​ p ⋅ Σ α + 1 ​ p ⋅ Σ α + 2 ​ p ⋅ Σ α + 3 ​ p. \displaystyle\Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4}=\Sigma_{\alpha}(p\texttt{1}\cdot p\texttt{1}\cdot p\texttt{1}\cdot p)=\Sigma_{\alpha}p\cdot\Sigma_{\alpha+1}p\cdot\Sigma_{\alpha+2}p\cdot\Sigma_{\alpha+3}p. |  |

Moreover w j = − w n − ( j − 1) w_{j}=-w_{n-(j-1)}, for all j j with 1 ⩽ j ⩽ n 1\leqslant j\leqslant n, because p p is an antipalindrome. Then

 | Σ α + 2 ​ p \displaystyle\Sigma_{\alpha+2}p | = ( α + 2) ( α + 2 + w 1) ⋯ ( α + 2 + w 1 + w 2 + ⋯ w n) \displaystyle=(\alpha+2)(\alpha+2+w_{1})\cdots(\alpha+2+w_{1}+w_{2}+\cdots w_{n}) |  |

 |  | = ( α + 2 + w 1 + w 2 + ⋯ w n) ( α + 2 + w 1 + w 2 + ⋯ w n − 1) ⋯ ( α + 2) \displaystyle=(\alpha+2+w_{1}+w_{2}+\cdots w_{n})(\alpha+2+w_{1}+w_{2}+\cdots w_{n-1})\cdots(\alpha+2) |  |

 |  | = Σ α ​ p ^. \displaystyle=\widehat{\Sigma_{\alpha}p}. |  |

Hence

 | Σ α ∘ ​ ( q 3 ​ n [i]) 4 = Σ α ​ p ⋅ Σ α + 1 ​ p ⋅ Σ α + 2 ​ p ⋅ Σ α + 3 ​ p = Σ α ​ p ⋅ Σ α + 1 ​ p ⋅ Σ α ​ p ^ ⋅ Σ α + 1 ​ p ^. \displaystyle\Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4}=\Sigma_{\alpha}p\cdot\Sigma_{\alpha+1}p\cdot\Sigma_{\alpha+2}p\cdot\Sigma_{\alpha+3}p=\Sigma_{\alpha}p\cdot\Sigma_{\alpha+1}p\cdot\widehat{\Sigma_{\alpha}p}\cdot\widehat{\Sigma_{\alpha+1}p}. |  |

By the other hand, the word q 3 ​ n ′ [i] = q 3 ​ n − 2 [i] ¯ q 3 ​ n − 1 [i] q_{3n}^{{}^{\prime}\left[i\right]}=\overline{q_{3n-2}^{\left[i\right]}}q_{3n-1}^{\left[i\right]} corresponds to another boundary word of the same title. In fact, by Proposition 8, we have q 3 ​ n − 1 [i] = m ​ 1 q_{3n-1}^{\left[i\right]}=m\texttt{1} and q 3 ​ n − 2 [i] = r ​ 3 q_{3n-2}^{\left[i\right]}=r\texttt{3}, for some palindromes m m and r r. Hence p ​ 1 = q 3 ​ n [i] = q 3 ​ n − 1 [i] ​ q 3 ​ n − 2 [i] ¯ = m ​ 1 ​ r ¯ ​ 1 p\texttt{1}=q_{3n}^{\left[i\right]}=q_{3n-1}^{\left[i\right]}\overline{q_{3n-2}^{\left[i\right]}}=m\texttt{1}\overline{r}\texttt{1}, so that p = m ​ 1 ​ r ¯ p=m\texttt{1}\overline{r}.

Therefore

 | q 3 ​ n ′ [i] = q 3 ​ n − 2 [i] ¯ q 3 ​ n − 1 [i] = r ¯ 1 m 1 = p R 1 = p ¯ 1 q_{3n}^{{}^{\prime}\left[i\right]}=\overline{q_{3n-2}^{\left[i\right]}}q_{3n-1}^{\left[i\right]}=\overline{r}\texttt{1}m\texttt{1}=p^{R}\texttt{1}=\overline{p}\texttt{1} |  |

and Σ α ∘ ( q 3 ​ n ′ [i]) 4 = Σ α ( p ¯ 1 ⋅ p ¯ 1 ⋅ p R 1 ⋅ p R) = Σ α p ¯ ⋅ Σ α + 1 p ¯ ⋅ Σ α ​ p ¯ ^ ⋅ Σ α + 1 ​ p ¯ ^. \Sigma_{\alpha}^{\circ}(q_{3n}^{{}^{\prime}\left[i\right]})^{4}=\Sigma_{\alpha}(\overline{p}\texttt{1}\cdot\overline{p}\texttt{1}\cdot p^{R}\texttt{1}\cdot p^{R})=\Sigma_{\alpha}\overline{p}\cdot\Sigma_{\alpha+1}\overline{p}\cdot\widehat{\Sigma_{\alpha}\overline{p}}\cdot\widehat{\Sigma_{\alpha+1}\overline{p}}. ∎

Remark. Note that if A ⋅ B ⋅ A ^ ⋅ B ^ A\cdot B\cdot\widehat{A}\cdot\widehat{B} is a BN-factorization of an i i -generalized Fibonacci snowflake, then A A and B B are palindromes, because p p is an antipalindrome then Σ α ​ p \Sigma_{\alpha}p and Σ α ​ p ¯ \Sigma_{\alpha}\overline{p} are palindromes.

###### Example 6.

In Table 6, we show tessellations of ∏ 2 [3] \prod_{2}^{\left[3\right]} and ∏ 3 [6] \prod_{3}^{\left[6\right]}.

∏ 2 [3] \prod_{2}^{\left[3\right]} | ∏ 3 [6] \prod_{3}^{\left[6\right]} |

[image: [Uncaptioned image]] | [image: [Uncaptioned image]] |

Table 6: Tessellations of ∏ 2 [3] \prod_{2}^{\left[3\right]} and ∏ 3 [6] \prod_{3}^{\left[6\right]}.

### 4.2 Some Geometric Properties

###### Definition 5.

The number P [i] ​ ( n) P^{\left[i\right]}(n) is defined recursively by P [i] ​ ( 0) = − i P^{\left[i\right]}(0)=-i, P [i] ​ ( 1) = i + 1 P^{\left[i\right]}(1)=i+1 and P [i] ​ ( n) = 2 ​ P [i] ​ ( n − 1) + P [i] ​ ( n − 2) P^{\left[i\right]}(n)=2P^{\left[i\right]}(n-1)+P^{\left[i\right]}(n-2) for all n ≥ 2 n\geq 2 and i ≥ 0 i\geq 0.

For i = 0 i=0 we have Pell numbers. In Table 7 are the first numbers P [i] ​ ( n) P^{\left[i\right]}(n).

i i | P [i] ​ ( n) P^{\left[i\right]}(n) |

0 | { 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, … } \left\{0,1,2,5,12,29,70,169,408,985,2378,...\right\}, | (A000129). |

1 | { − 1, 2, 3, 8, 19, 46, 111, 268, 647, 1562, 3771, … } \left\{-1,2,3,8,19,46,111,268,647,1562,3771,...\right\}, | (A078343). |

2 | { − 2, 3, 4, 11, 26, 63, 152, 367, 886, 2139, 5164, … } \left\{-2,3,4,11,26,63,152,367,886,2139,5164,...\right\}. |  |

3 | { − 3, 4, 5, 14, 33, 80, 193, 466, 1125, 2716, 6557, … } \left\{-3,4,5,14,33,80,193,466,1125,2716,6557,...\right\}. |  |

4 | { − 4, 5, 6, 17, 40, 97, 234, 565, 1364, 3293, 7950, … } \left\{-4,5,6,17,40,97,234,565,1364,3293,7950,...\right\}. |  |

5 | { − 5, 6, 7, 20, 47, 114, 275, 664, 1603, 3870, 9343, … } \left\{-5,6,7,20,47,114,275,664,1603,3870,9343,...\right\}. |  |

Table 7: First numbers P [i] ​ ( n) P^{\left[i\right]}(n).

###### Proposition 10.

A formula for the P [i] ​ ( n) P^{\left[i\right]}(n) numbers is

 | P [i] ​ ( n) = 1 4 ​ ( ( 1 + 2) n ​ ( 2 − ( 2 − 2 ​ 2) ​ i) − ( 1 − 2) n ​ ( 2 + ( 2 + 2 ​ 2) ​ i)). \displaystyle P^{\left[i\right]}(n)=\frac{1}{4}\left(\left(1+\sqrt{2}\right)^{n}(\sqrt{2}-(2-2\sqrt{2})i)-\left(1-\sqrt{2}\right)^{n}(\sqrt{2}+(2+2\sqrt{2})i)\right). |  |

###### Proof.

By induction on n n. ∎

Let α ∈ 𝒜 \alpha\in\mathcal{A}, we denote by Σ α → α q \stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{\alpha}}}q the coordinates of the vector whose initial point is the origin and the terminal point is the last point of the path Σ α ∘ ​ ( q) \Sigma^{\circ}_{\alpha}(q). In the next proposition, we show that the coordinates of the vector Σ 0 → ( q n [i]) \stackrel{{\scriptstyle\rightarrow}}{{\Sigma}}_{0}(q_{n}^{\left[i\right]}) are expressed in terms of the numbers P [i] ​ ( n) P^{\left[i\right]}(n). A similar thing happens when α = 1, 2, 3 \alpha=1,2,3.

###### Proposition 11.

For all n ∈ ℕ n\in\mathbb{N}, we have that if i i is even then

 | Σ 0 → 0 q 3 ​ n + 1 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+1}^{\left[i\right]} | = ( P [k] ​ ( n + 1) + P [k] ​ ( n), 0), \displaystyle=\left(P^{\left[k\right]}(n+1)+P^{\left[k\right]}(n),0\right), |  |

 | Σ 0 → 0 q 3 ​ n + 2 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+2}^{\left[i\right]} | = ( P [k] ​ ( n + 1), ( − 1) n ​ P [k] ​ ( n + 1)), \displaystyle=\left(P^{\left[k\right]}(n+1),(-1)^{n}P^{\left[k\right]}(n+1)\right), |  |

 | Σ 0 → 0 q 3 ​ n + 3 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+3}^{\left[i\right]} | = ( P [k] ​ ( n + 2), ( − 1) n ​ P [k] ​ ( n + 1)), \displaystyle=\left(P^{\left[k\right]}(n+2),(-1)^{n}P^{\left[k\right]}(n+1)\right), |  |

where k = i − 2 2 k=\frac{i-2}{2}. If i i is odd then

 | Σ 0 → 0 q 3 ​ n + 1 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+1}^{\left[i\right]} | = { ( P [k] ​ ( n + 1) + P [k] ​ ( n), 0), if n is even, ( 0, P [k] ​ ( n + 1) + P [k] ​ ( n)), if n is odd, \displaystyle=\begin{cases}(P^{\left[k\right]}(n+1)+P^{\left[k\right]}(n),0),&\text{if $n$ is even},\\ (0,P^{\left[k\right]}(n+1)+P^{\left[k\right]}(n)),&\text{if $n$ is odd},\\ \end{cases} |  |

 | Σ 0 → 0 q 3 ​ n + 2 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+2}^{\left[i\right]} | = { ( P [k] ​ ( n + 2), P [k] ​ ( n + 1)), if n is even, ( P [k] ​ ( n + 1), P [k] ​ ( n + 2)), if n is odd, \displaystyle=\begin{cases}(P^{\left[k\right]}(n+2),P^{\left[k\right]}(n+1)),&\text{if $n$ is even},\\ (P^{\left[k\right]}(n+1),P^{\left[k\right]}(n+2)),&\text{if $n$ is odd},\\ \end{cases} |  |

 | Σ 0 → 0 q 3 ​ n + 3 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+3}^{\left[i\right]} | = ( P [k] ​ ( n + 2), P [k] ​ ( n + 2)), \displaystyle=\left(P^{\left[k\right]}(n+2),P^{\left[k\right]}(n+2)\right), |  |

where k = i − 3 2 k=\frac{i-3}{2}.

###### Proof.

By induction on n n. If i i is even. For n = 0 n=0 it is clear. Assume for all j j such that 0 ≤ j ≤ 3 ​ n + 5 0\leq j\leq 3n+5; we prove it for 3 ​ n + 6 3n+6. Then passing to vectors we have

 | Σ 0 → 0 q 3 ​ n + 6 [i] \displaystyle\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+6}^{\left[i\right]} | = Σ 0 → 0 q 3 ​ n + 5 [i] + Σ 0 → 0 q 3 ​ n + 4 [i] ¯ \displaystyle=\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+5}^{\left[i\right]}+\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}\overline{q_{3n+4}^{\left[i\right]}} |  |

 |  | = ( P [k] ​ ( n + 2), ( − 1) n + 1 ​ P [k] ​ ( n + 2)) + ( P [k] ​ ( n + 2) + P [k] ​ ( n + 1), 0) ¯ \displaystyle=\left(P^{\left[k\right]}(n+2),(-1)^{n+1}P^{\left[k\right]}(n+2)\right)+\overline{\left(P^{\left[k\right]}(n+2)+P^{\left[k\right]}(n+1),0\right)} |  |

 |  | = ( P [k] ​ ( n + 2), ( − 1) n + 1 ​ P [k] ​ ( n + 2)) + ( P [k] ​ ( n + 2) + P [k] ​ ( n + 1), 0) \displaystyle=\left(P^{\left[k\right]}(n+2),(-1)^{n+1}P^{\left[k\right]}(n+2)\right)+\left(P^{\left[k\right]}(n+2)+P^{\left[k\right]}(n+1),0\right) |  |

 |  | = ( 2 ​ P [k] ​ ( n + 2) + P [k] ​ ( n + 1), ( − 1) n + 1 ​ P [k] ​ ( n + 2)) \displaystyle=\left(2P^{\left[k\right]}(n+2)+P^{\left[k\right]}(n+1),(-1)^{n+1}P^{\left[k\right]}(n+2)\right) |  |

 |  | = ( P [k] ​ ( n + 3), ( − 1) n + 1 ​ P [k] ​ ( n + 2)) \displaystyle=\left(P^{\left[k\right]}(n+3),(-1)^{n+1}P^{\left[k\right]}(n+2)\right) |  |

where Σ 0 → 0 q n [i] ¯ = ( A ¯, B ¯) \stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}\overline{q_{n}^{\left[i\right]}}=(\overline{A},\overline{B}) is the coordinate the last point of the path Σ α ∘ ​ ( q ¯ n) \Sigma^{\circ}_{\alpha}(\overline{q}_{n}). In this case Σ 0 → 0 q 3 ​ n + 4 [i] ¯ = Σ 0 → 0 q 3 ​ n + 4 [i] \stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}\overline{q_{3n+4}^{\left[i\right]}}=\stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{0}}}q_{3n+4}^{\left[i\right]}, because a ¯ \overline{a} leaves the horizontal direction unchanged. The other cases are similar. ∎

###### Example 7.

Table 8 are the endpoints coordinates of the paths Σ 0 ∘ ​ ( q n [4]) \Sigma^{\circ}_{0}(q_{n}^{\left[4\right]}) and Fig. 7 shows the coordinates.

n n | 0 | 1 | 2 | 3 | 4 |

Σ 0 ∘ ​ ( q 3 ​ n + 1 [4]) \Sigma^{\circ}_{0}(q_{3n+1}^{\left[4\right]}) | (1, 0) | (5,0) | (11,0) | (27, 0) | (65, 0) |

Σ 0 ∘ ​ ( q 3 ​ n + 2 [4]) \Sigma^{\circ}_{0}(q_{3n+2}^{\left[4\right]}) | (2, 2) | (3,-3) | (8,8) | (19, -19) | (46, 6) |

Σ 0 ∘ ​ ( q 3 ​ n + 3 [4]) \Sigma^{\circ}_{0}(q_{3n+3}^{\left[4\right]}) | (3, 2) | (8,-3) | (19,8) | (46, -19) | (111, 46) |

Table 8: Coordinates of the path Σ 0 ∘ ​ ( q n [4]) \Sigma^{\circ}_{0}(q_{n}^{\left[4\right]}). [image: Refer to caption]
Figure 7: Graph with the coordinates of the path Σ 0 ∘ ​ ( q n [4]) \Sigma^{\circ}_{0}(q_{n}^{\left[4\right]}).

The following proposition is clear because | q n [i] | = F n − 1 [i] |q_{n}^{\left[i\right]}|=F_{n-1}^{\left[i\right]}.

###### Proposition 12.

The perimeter L ⁡ ( n, i) L(n,i) of the i i -generalized Fibonacci snowflake of order n n is

 | L ⁡ ( n, i) = { 4 ​ F 3 ​ n − 1 [i], if i is even 4 ​ F 3 ​ n + 1 [i], if i is odd. \displaystyle L(n,i)=\begin{cases}4F_{3n-1}^{\left[i\right]},&\text{if $i$ is even}\\ 4F_{3n+1}^{\left[i\right]},&\text{if $i$ is odd.}\end{cases} |  |

###### Proposition 13.

The area A ⁡ ( n, i) A(n,i) of the i i -generalized Fibonacci snowflake of order n n is:

1. i.

If i i is even, then A ⁡ ( n, i) = ( P [k] ​ ( n + 1)) 2 + ( P [k] ​ ( n)) 2 A(n,i)=\left(P^{\left[k\right]}(n+1)\right)^{2}+\left(P^{\left[k\right]}(n)\right)^{2}, where k = i − 2 2 k=\frac{i-2}{2}.

2. ii.

If i i is odd then, A ⁡ ( n, i) = ( P [k] ​ ( n + 2)) 2 + ( P [k] ​ ( n + 1)) 2 A(n,i)=\left(P^{\left[k\right]}(n+2)\right)^{2}+\left(P^{\left[k\right]}(n+1)\right)^{2}, where k = i − 3 2 k=\frac{i-3}{2}.

3. iii.

Moreover A ⁡ ( n, i) A(n,i) satisfies the recurrence formula

 | A ⁡ ( n, i) = 6 ​ A ​ ( n − 1, i) − A ⁡ ( n − 2, i) \displaystyle A(n,i)=6A(n-1,i)-A(n-2,i) |  | (2) |

for all n ≥ 3 n\geq 3, (initial values can be calculated with the above items).

###### Proof.

Suppose that i i is even. If a word w ∈ 𝒜 ∗ w\in\mathcal{A}^{*} is an antipalindrome then its corresponding polygonal line is symmetric with respect to midpoint of the vector Σ α → α w \stackrel{{\scriptstyle\rightarrow}}{{\Sigma_{\alpha}}}w, see Lemma 2.6 in [7]. Moreover, from Proposition 9 -ii, we have that the parallelogram determined by the word Σ α ∘ ​ ( q 3 ​ n [i]) 4 \Sigma_{\alpha}^{\circ}(q_{3n}^{\left[i\right]})^{4} is a square, (in Fig. 8, we show some examples for i = 2, 3, 4 i=2,3,4 and n = 2 n=2), and by Proposition 11 the area A ⁡ ( n, i) A(n,i) is equal to the area of square determined by Σ 0 ∘ ​ ( q 3 ​ n [i]) = ( P [k] ​ ( n + 1), ± P [k] ​ ( n)) \Sigma^{\circ}_{0}(q_{3n}^{\left[i\right]})=\left(P^{\left[k\right]}(n+1),\pm P^{\left[k\right]}(n)\right). Hence A ⁡ ( n, i) = ( P [k] ​ ( n + 1)) 2 + ( P [k] ​ ( n)) 2 A(n,i)=\left(P^{\left[k\right]}(n+1)\right)^{2}+\left(P^{\left[k\right]}(n)\right)^{2}, where k = i − 2 2 k=\frac{i-2}{2}. If i i is odd, the proof is similar.

The Eq. 2 is obtained from i i and i ​ i ii, and by definition of P [i] ​ ( n) P^{\left[i\right]}(n).

[image: Refer to caption]
Figure 8: Examples, Areas of i i -generalized Fibonacci snowflakes.

∎

Let S [i] ​ ( n) S^{\left[i\right]}(n) be the smallest square having sides parallel to the axes and containing to ∏ [i] \prod^{\left[i\right]}. In Fig. 9, we show the cases for i = 4 i=4 and n = 2, 3 n=2,3. If i i is even, from Proposition 11 we have that ( A, B) = ( P [i] ​ ( n), ( − 1) n ​ P ​ ( n + 1) [i]) (A,B)=(P^{\left[i\right]}(n),(-1)^{n}P(n+1)^{\left[i\right]}). Therefore

 | S [i] ​ ( n) = ( A + 3 ​ B 2 − A − B 2 − 1) 2 = ( 2 ​ B − 1) 2 = ( 2 ​ P [i] ​ ( n + 1) − 1) 2 \displaystyle S^{\left[i\right]}(n)=\left(\frac{A+3B}{2}-\frac{A-B}{2}-1\right)^{2}=(2B-1)^{2}=(2P^{\left[i\right]}(n+1)-1)^{2} |  |

When i i is odd it is similar.

[image: Refer to caption]
Figure 9: S [i] ​ ( n) S^{\left[i\right]}(n) for i = 4 i=4 and n = 2, 3 n=2,3.

Next theorem generalizes theorem 1 of [6].

###### Theorem 3.

The fractal dimension of ∏ [i] = lim n → ∞ ∏ n [i] \prod^{\left[i\right]}=\lim_{n\rightarrow\infty}\prod_{n}^{\left[i\right]} is

 | 3 ​ ln ⁡ ϕ ln ⁡ ( 1 + 2). \displaystyle\frac{3\ln\phi}{\ln(1+\sqrt{2})}. |  |

###### Proof.

Suppose that i i is even, then the polyomino ∏ n [i] \prod_{n}^{\left[i\right]} is composed of 4 ​ | q 3 ​ n [i] | 4|q_{3n}^{\left[i\right]}| unit segments and this value blows up when n → ∞ n\rightarrow\infty. However, the normalized polyomino 1 2 ​ P [i] ​ ( n + 1) − 1 ∏ n [i] \frac{1}{2P^{\left[i\right]}(n+1)-1}\prod_{n}^{\left[i\right]} stays bounded. It has 4 ​ | q 3 ​ n [i] | 4|q_{3n}^{\left[i\right]}| segments of length 1 2 ​ P [i] ​ ( n + 1) − 1 \frac{1}{2P^{\left[i\right]}(n+1)-1}. Hence the total d − d- dimensional normalized polyomino has length

 | 4 ​ | q 3 ​ n [i] | ( 2 ​ P [i] ​ ( n + 1) − 1) d \displaystyle\frac{4|q_{3n}^{\left[i\right]}|}{(2P^{\left[i\right]}(n+1)-1)^{d}} |  |

and therefore the self-similarity dimension (see [23] for the definition the self-similarity dimension) of ∏ [i] \prod^{\left[i\right]} is

 | d = lim n → ∞ ln ⁡ ( 4 ​ | q 3 ​ n [i] |) ln ⁡ ( 2 ​ P [i] ​ ( n + 1) − 1) = 3 ​ ln ⁡ ϕ ln ⁡ ( 1 + 2). \displaystyle d=\lim_{n\rightarrow\infty}\frac{\ln(4|q_{3n}^{\left[i\right]}|)}{\ln(2P^{\left[i\right]}(n+1)-1)}=\frac{3\ln\phi}{\ln(1+\sqrt{2})}. |  |

∎

## 5 Conclusion

In this paper, we study a generalization of the Fibonacci word and the Fibonacci word fractal founds in [22]. Particularly , we defined the curves ℱ [i] \mathcal{F}^{\left[i\right]} from the i i -Fibonacci words and show their properties remain. Moreover, the i i -generalized Fibonacci snowflakes generalize the Fibonacci snowflake studied in [7] and we show that they are a subclass of double squares. Finally, we found that i i -generalized Fibonacci snowflakes are related with Fibonacci and Pell numbers, and some generalizations.

In [17] authors have introduced a generalization of the Fibonacci sequence. For any two nonzero real numbers a a and b b, the *generalized Fibonacci sequence*, say { F n ( a, b) } 0 ∞ \left\{F_{n}^{(a,b)}\right\}_{0}^{\infty}, is defined recursively by

 |  | F 0 ( a, b) = 0, F 1 ( a, b) = 1, \displaystyle F_{0}^{(a,b)}=0,\ \ \ F_{1}^{(a,b)}=1, |  |

 |  | F n ( a, b) = { a ​ F n − 1 ( a, b) + F n − 2 ( a, b), if n is even b ​ F n − 1 ( a, b) + F n − 2 ( a, b), if n is odd ⁡ ( n ≥ 2) \displaystyle F_{n}^{(a,b)}=\begin{cases}aF_{n-1}^{(a,b)}+F_{n-2}^{(a,b)},&\ \text{if $n$ is even}\\ bF_{n-1}^{(a,b)}+F_{n-2}^{(a,b)},&\ \text{if $n$ is odd}\end{cases}(n\geq 2) |  |

On the other hand, there is a word-combinatorial interpretation of this generalized Fibonacci sequence. Let α = [0, a, b, a, b, …] = [0, a, b ¯] \alpha=\left[0,a,b,a,b,\ldots\right]=\left[0,\overline{a,b}\right] then *w*​ ( α) = lim n → ∞ s n \textbf{\emph{w}}(\alpha)=\lim_{n\rightarrow\infty}s_{n} where

 |  | s 0 = 1, s 1 = 0, s 2 = 0 a − 1 ​ 1, \displaystyle s_{0}=\texttt{1},\ \ s_{1}=\texttt{0},\ \ s_{2}=\texttt{0}^{a-1}\texttt{1}, |  |

 |  | s n = { s n − 1 a ​ s n − 2, if n is even s n − 1 b ​ s n − 2, if n is odd, n ≥ 3 \displaystyle s_{n}=\begin{cases}s_{n-1}^{a}s_{n-2},&\text{if $n$ is even}\\ s_{n-1}^{b}s_{n-2},&\text{if $n$ is odd}\end{cases},n\geq 3 |  |

Let r 0 = 0, r n = | s n |, n ≥ 1 r_{0}=0,\ \ r_{n}=|s_{n}|,\ n\geq 1 then { r n } = { F n ( a, b) } \left\{r_{n}\right\}=\left\{F_{n}^{(a,b)}\right\}. It would be interesting to study different curves obtained by applying the odd-even drawing rule to the word s n s_{n}. Empirical observations show interesting patterns. For instance with a = 2, b = 5 a=2,b=5 and n = 9 n=9 we obtain the curve Fig. 10.

[image: Refer to caption]
Figure 10: Curve obtained with a = 2, b = 5 a=2,b=5 and n = 9 n=9.

## References

- [1] J. Allouche, J. Shallit, Automatic Sequences, Cambridge University Press, Cambridge, 2003.
- [2] D. Beauquier, M. Nivat, On translating one polyomino to tile the plane, Discrete Comput. Geom. 6 (1991), 575–592.
- [3] J. Berstel, Fibonacci words-a survey, in: G. Rosenberg, A. Salomaa (Eds.), The Book of L, Springer, Berlin, (1986), 11–26.
- [4] A. Blondin-Massé, S. Brlek, A. Garon, S. Labbé, Two infinite families of polyominoes that tile the plane by translation in two distinct ways, Theoret. Comput. Sci. 412 (2011), 4778–4786.
- [5] A. Blondin-Massé, S. Brlek, S. Labbé, A parallelogram tile fills the plane by translation in at most two distinct ways, Discrete Appl. Math. 160 (2012), 1011–1018.
- [6] A. Blondin-Massé, S. Brlek, S. Labbé, M. Mendès France, Complexity of the Fibonacci snowflake, Fractals 20 (2012), 157–260.
- [7] A. Blondin-Massé, S. Brlek, S. Labbé, M. Mendès France, Fibonacci snowflakes, Ann. Sci. Math. Québec 35 (2)(2010), 141–152.
- [8] A. Blondin Massé, A. Garon, S. Labbé, Combinatorial properties of double square tiles, Theoret. Comput. Sci. 502 (2013), 98–117.
- [9] P. Brass, W. Moser, J. Pach, Research Problems in Discrete Geometry, Springer-Verlag, New York, 2005.
- [10] S. Brlek. Interactions between Digital Geometry and Combinatorics on Words, in: P. Ambroz̆, S̆. Holub, Z. Masáková (Eds.), Proc. WORDS 2011, 8th International Conference Words 2011, Prague, Czech Republic, 12-16 September, EPTCS, vol 63, 2011, 1–12 .
- [11] S. Brlek, J. Fédou, X. Provençal, On the Tiling by Translation Problem, Discrete Appl. Math. 157 (2009), 464–475.
- [12] J. Cassaigne, On extremal properties of the Fibonacci word, RAIRO - Theor. Inf. Appl. 42 (4) (2008), 701–715.
- [13] W. Chuan, Fibonacci words, Fibonacci Quart., 30 (1) (1992), 68–76.
- [14] W. Chuan, Generating Fibonacci words, Fibonacci Quart., 33 (2) (1995), 104–112.
- [15] A. de Luca, A division property of the Fibonacci word, Inform. Process. Lett., 54 (1995), 307–312.
- [16] X. Droubay, Palindromes in the Fibonacci word, Inform. Process. Lett., 55 (1995), 217–221.
- [17] M. Edson, O. Yayenie, A new generalization of Fibonacci sequence and extended Binet’s formula. Integers, 9 (6) (2009), 639–654.
- [18] B. Grünbaum, G.C. Shephard, Tilings and Patterns, W.H. Freeman, New York, 1987.
- [19] T. Koshy, Fibonacci and Lucas Numbers with Applications, Wiley-Interscience, 2001.
- [20] M. Lothaire, Algebraic Combinatorics on Words, Encyclopedia of Mathematics and its Applications, Cambridge University Press, Cambridge, 2002.
- [21] F. Mignosi, G. Pirillo, Repetitions in the Fibonacci infinite word, RAIRO Inform. Theor. Appl. 26 (1992), 199–204.
- [22] A. Monnerot, The Fibonacci Word Fractal, preprint http://hal.archives-ouvertes.fr/hal-00367972/fr/, (2009).
- [23] H.O. Heitgen, H. Jürgens, D. Saupe, Chaos and Fractals: New Frontiers of Science, 2nd ed., Springer-Verlag, New York, 2004.
- [24] G. Pirillo, Fibonacci numbers and words, Discrete Math. 173 (1997), 197–207.
- [25] P. Prusinkiewicz, A. Lindenmayer, The algorithmic beauty of plants, Springer-Verlag. Nueva York, 2004. http://algorithmicbotany.org/papers/abop/abop.pdf.
- [26] J. Ramírez, G. Rubiano, Generating fractals curves from homomorphisms between languages [\left[\right. with Mathematica] ® {}^{\circledR}\left.\right] ” (Spanish), Revista Integración 30 (2), (2012), 129–150.
- [27] N. Sloane, The On-Line Encyclopedia of Integer Sequences.
- [28] H.A.G. Wijshoff, J. van Leeuven, Arbitrary versus periodic storage schemes and tesselations of the plane using one type of polyomino, Inform. Control, 62 (1984), 1–25.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1212.1366
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1212.1368
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1212.1368
[7]: https://arxiv.org/pdf/1212.1368
[8]: /html/1212.1369
