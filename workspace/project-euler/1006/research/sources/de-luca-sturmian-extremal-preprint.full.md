<!-- source: https://ar5iv.labs.arxiv.org/html/1209.3927 | converted from HTML -->

[1209.3927] Some extremal properties of the Fibonacci word

# Some extremal properties of the Fibonacci word

Aldo de Luca Affiliation: Dipartimento di Matematica e Applicazioni “R. Caccioppoli” Affiliation: Università degli Studi di Napoli Federico II Affiliation: Via Cintia, Monte S. Angelo, I-80126 Napoli, Italy

###### Abstract

We prove that the Fibonacci word f f satisfies among all characteristic Sturmian words, three interesting extremal properties. The first concerns the length and the second the minimal period of its palindromic prefixes. Each of these two properties characterizes f f up to a renaming of its letters. A third property concerns the number of occurrences of the letter b b in its palindromic prefixes. It characterizes uniquely f f among all characteristic Sturmian words having the prefix a ​ b ​ a ​ a abaa.

Keywords. Fibonacci word, Sturmian words, Characteristic words, Central words, Standard words, Christoffel words, Continuants

## 1 Introduction

Words are finite or infinite sequences of elements, called letters, taken from a finite set called alphabet. In the combinatorics of infinite words the Fibonacci word is very famous since it satisfies a great number of beautiful properties which are of a paramount interest both from the theoretical and the applicative point of view.

As is well known, the Fibonacci word f f can be defined in several different ways. For instance, f f is the fixed point φ ω ​ ( a) \varphi^{\omega}(a) of the Fibonacci morphism φ: { a, b } ∗ → { a, b } ∗ \varphi:\{a,b\}^{*}\rightarrow\{a,b\}^{*} defined by φ ⁡ ( a) = a ​ b \varphi(a)=ab and φ ⁡ ( b) = a \varphi(b)=a. The name Fibonacci given to f f is due to the fact that f f is the limit sequence of the infinite sequence ( f n) n ≥ − 1 (f_{n})_{n\geq-1} of finite words recursively defined as

 | f − 1 = b, f 0 = a, and ​ f n + 1 = f n ​ f n − 1 ​ for n ≥ 0. f_{-1}=b,f_{0}=a,\ \mbox{and}\ f_{n+1}=f_{n}f_{n-1}\ \mbox{for}\ \ n\geq 0. |  |

For any n ≥ − 1 n\geq-1 one has | f n | = F n |f_{n}|=F_{n} where ( F n) n ≥ − 1 (F_{n})_{n\geq-1} is the Fibonacci numerical sequence:

 | F − 1 = F 0 = 1 ​ and F n + 1 = F n + F n − 1 ​ for ​ n ≥ 0. F_{-1}=F_{0}=1\ \mbox{and}\ \ F_{n+1}=F_{n}+F_{n-1}\ \mbox{for}\ n\geq 0. |  |

The Fibonacci word is a paradigmatic example of Sturmian word. As is well known, Sturmian words are infinite words over a binary alphabet of great interest in combinatorics on words for the many applications in Algebra, Number theory, Physics, and Computer Science.

Several different but equivalent definitions of Sturmian words exist (see, for instance, [23, Chap. 2]). A Sturmian word can be defined in a purely combinatorial way as an infinite sequence of letters such that for any integer n ≥ 0 n\geq 0, the number of its distinct factors of length n n is n + 1 n+1. This is equivalent to say that an infinite word is Sturmian if and only if it is aperiodic and for any n n it has the minimal possible of distinct factors of length n n.

A geometrical definition is the following: a Sturmian word is an infinite word associated to the sequence of the cuts (cutting sequence) in a squared-lattice made by a semi-line having a slope which is an irrational number. A horizontal cut is denoted by the letter b b, a vertical cut by a a and a cut with a corner by a ​ b ab or b ​ a ba. Sturmian words represented by a semi-line starting from the origin are usually called characteristic, or standard. For any Sturmian word there exists a characteristic Sturmian word having the same set of factors. The Fibonacci word is the characteristic Sturmian word having a slope equal to the golden ratio g = 5 − 1 2 g=\frac{\sqrt{5}-1}{2}.

In many cases, the Fibonacci word f f satisfies among all infinite words of a given class, some extremal properties in the sense that some quantity is maximal or minimal for f f (see, for instance [5, 6, 9, 25], and the overview [7]). A special case of great interest is when the class of infinite words is formed by all characteristic Sturmian words and the extremal property is satisfied only by the Fibonacci word f f and by E ⁡ ( f) E(f), where E E is the automorphism of { a, b } ∗ \{a,b\}^{*} interchanging the letter a a with the letter b b. In this way one obtains a characterization of f f, up to a renaming of the letters, inside the class of characteristic Sturmian words.

Some of these latter extremal properties are strictly related to a simple construction of characteristic Sturmian words, due to the author [10]. It is based on an operator definable in any free monoid A ∗ A^{*} and called right-palindromic closure, which associates to each word w ∈ A ∗ w\in A^{*} the shortest palindrome of A ∗ A^{*} having w w as a prefix. Any given word v ∈ A ∗ v\in A^{*} can suitably ‘direct’ subsequent iterations of the preceding operator according to the sequence of letters in v v as follows: at each step, one concatenates the next letter of v v to the right of the already constructed palindrome and then takes the right palindromic closure. Thus starting with any directive word v v one generates a palindrome ψ ⁡ ( v) \psi(v). The map ψ \psi, called palindromization map, is injective; the word v v is called the directive word of ψ ⁡ ( v) \psi(v).

Since for any u, v ∈ A ∗ u,v\in A^{*}, ψ ⁡ ( u ​ v) \psi(uv) has ψ ⁡ ( u) \psi(u) as a prefix, one can extend the map ψ \psi to right infinite words x ∈ A ω x\in A^{\omega} producing an infinite word ψ ⁡ ( x) \psi(x). It has been proved in [10] that in the case of a binary alphabet 𝒜 = { a, b } {\cal A}=\{a,b\} if each letter of 𝒜 {\cal A} occurs infinitely often in x x, then one can generate all characteristic Sturmian words 1 1 1 The palindromization map ψ \psi has been extended to infinite words over an arbitrary alphabet A A by X. Droubay, J. Justin, and G. Pirillo in [16], where the family of standard episturmian words over A A has been introduced. Some further extensions and generalizations of ψ \psi are in [12, 13]. An extension of ψ \psi to free group F 2 F_{2} was given by C. Reutenauer in [20].. Moreover, ψ ⁡ ( 𝒜 ∗) \psi({\cal A}^{*}) coincides with the set of the palindromic prefixes of all characteristic Sturmian words. These words can be also defined in a purely combinatorial way by an extremal property closely related to Fine and Wilf’s periodicity theorem [17]; they are usually c! alled also central words since they play a central role in Sturmian words theory. In Section 3 some remarkable structural properties of central words relating them to finite standard words and to Christoffel words are briefly presented.

A central word is of order n n if its directive word is of length n n. In [6] we proved that the Fibonacci word f = ψ ⁡ ( ( a ​ b) ω) f=\psi((ab)^{\omega}) is the only characteristic Sturmian word, up to a renaming of the letters, whose palindromic prefixes w w of any order are harmonic, that is the minimal period π ⁡ ( w) \pi(w) of w w satisfies the condition π 2 ​ ( w) ≡ ± 1 \pi^{2}(w)\equiv\pm 1 (mod OPEN | w | + 2) |w|+2).

The main results of the paper are three theorems (cf. Theorems 4.4, 4.7, and 4.11), somehow related to each other, showing the following extremal properties of f f. Theorem 4.4 states that a characteristic Sturmian word s s has the palindromic prefixes of any order of maximal length if and only if s = f s=f or s = E ⁡ ( f) s=E(f), where E E is the automorphism of { a, b } ∗ \{a,b\}^{*} interchanging the letter a a with b b. Similarly, Theorem 4.7 states that, up to a renaming of the letters, the Fibonacci word is the only characteristic Sturmian word whose palindromic prefixes of any order have a maximum value of the minimal period. Theorem 4.11 shows that a characteristic Sturmian word beginning with the letter a a has the palindromic prefixes of any order with the maximal number of occurrences of the letter b b if and only if s = f s=f or s s has the directive word ( a ​ b 2) ​ ( a ​ b) ω (ab^{2})(ab)^{\omega}. Hence, this extremal property characterizes uniquely f f among all characteristic Sturmian words having the prefix a ​ b ​ a ​ a abaa.

The proof of these theorems is given in Section 4 by using techniques of combinatorics on words and three extremal properties of central words which are prefixes of the Fibonacci word concerning their length (cf. Theorem 4.1), their minimal period (cf. Theorem 4.5), and the number of occurrences of the letter b b (cf. Theorem 4.9).

In Section 5 we consider the arithmetization of Sturmian words theory obtained by representing the directive words of central words, as well as of characteristic Sturmian words, by sequences of integers (integral representations). In this setting continued fractions and continuants associated to these numerical sequences play a relevant role. We show that Theorem 4.1 is equivalent to a property of continuants (cf. Theorem 5.4) and a direct proof of this latter result is also given. Moreover, we show that also Theorem 4.5 can be derived from Theorem 5.4 by using a suitable expression of the minimal periods of central words in terms of continuants.

## 2 Preliminaries

### 2.1 Notation and preliminary definitions

In the following 𝒜 {\cal A} will denote a binary alphabet 𝒜 = { a, b } {\cal A}=\{a,b\} and 𝒜 ∗ {\cal A}^{*} the *free monoid*generated by 𝒜 {\cal A}. The elements a a and b b of 𝒜 {\cal A} are usually called *letters*and those of 𝒜 ∗ {\cal A}^{*}*words*. We suppose that 𝒜 {\cal A} is totally ordered by setting a < b a<b. The identity element of 𝒜 ∗ {\cal A}^{*} is called *empty word*and denoted by ε \varepsilon. We set 𝒜 + = 𝒜 ∗ ∖ { ε } {\cal A}^{+}={\cal A}^{*}\setminus\{\varepsilon\}.

A word w ∈ 𝒜 + w\in{\cal A}^{+} can be written uniquely as a sequence of letters w = w 1 w 2 ⋯ w n w=w_{1}w_{2}\cdots w_{n}, with w i ∈ 𝒜 w_{i}\in{\cal A}, 1 ≤ i ≤ n 1\leq i\leq n, n > 0 n>0. The integer n n is called the *length*of w w and denoted | w | |w|. The length of ε \varepsilon is taken equal to 0 0. For any w ∈ 𝒜 ∗ w\in{\cal A}^{*} and x ∈ 𝒜 x\in{\cal A}, | w | x |w|_{x} denotes the number of occurrences of the letter x x in w w. For any w ∈ 𝒜 ∗ w\in{\cal A}^{*}, alph ⁡ w \alf w will denote the set of all distinct letters of 𝒜 {\cal A} occurring in w w.

We consider the map η: 𝒜 ∗ → ℚ ∪ { ∞ } \eta:{\cal A}^{*}\rightarrow{\mathbb{Q}}\cup\{\infty\} defined by

 | η ⁡ ( ε) = 1 and η ⁡ ( w) = | w | b | w | a for w ≠ ε. \eta(\varepsilon)=1\ \ \mbox{and}\ \ \eta(w)=\frac{|w|_{b}}{|w|_{a}}\ \ \mbox{for}\ \ w\neq\varepsilon. |  |

If | w | a = 0 |w|_{a}=0 and w ≠ ε w\neq\varepsilon, we assume η ⁡ ( w) = | w | b 0 = ∞ \eta(w)=\frac{|w|_{b}}{0}=\infty. For any w ∈ 𝒜 ∗ w\in{\cal A}^{*}, η ⁡ ( w) \eta(w) is called the slope of w w.

Let w ∈ 𝒜 ∗ w\in{\cal A}^{*}. The word u u is a *factor*of w w if there exist words r r and s s such that w = r ​ u ​ s w=rus. A factor u u of w w is called *proper*if u ≠ w u\neq w. If w = u ​ s w=us, for some word s s (resp., w = r ​ u w=ru, for some word r r), then u u is called a *prefix*(resp., a *suffix*) of w w.

Let p p be a positive integer. A word w = w 1 ⋯ w n w=w_{1}\cdots w_{n}, w i ∈ 𝒜 w_{i}\in{\cal A}, 1 ≤ i ≤ n 1\leq i\leq n, has period p p if the following condition is satisfied: for any integers i i and j j such that 1 ≤ i, j ≤ n 1\leq i,j\leq n,

 | if ​ i ≡ j ( mod p), then ​ w i = w j. \mbox{if }i\equiv j\pmod{p},\mbox{ then }w_{i}=w_{j}. |  |

Let us observe that if a word w w has a period p p, then any non-empty factor of w w has also the period p p. We shall denote by π ⁡ ( w) \pi(w) the minimal period of w w. Conventionally, we set π ⁡ ( ε) = 1 \pi(\varepsilon)=1.

We recall the following important periodicity theorem due to Fine and Wilf [17]: If a word w w has two periods p p and q q and | w | ≥ p + q − gcd ⁡ ( p, q) |w|\geq p+q-\gcd(p,q), then w w admits the period gcd ⁡ ( p, q) \gcd(p,q).

Let w = w 1 ⋯ w n w=w_{1}\cdots w_{n}, w i ∈ 𝒜 w_{i}\in{\cal A}, 1 ≤ i ≤ n 1\leq i\leq n. The *reversal*, or mirror image, of w w is the word w ∼ = w n ⋯ w 1 w^{\sim}=w_{n}\cdots w_{1}. One defines also ε ∼ = ε \varepsilon^{\sim}=\varepsilon. A word is called *palindrome*if it is equal to its reversal. We shall denote by 𝑃𝐴𝐿 \mathit{PAL} the set of all palindromes on the alphabet 𝒜 {\cal A}.

A right-infinite word x x, or simply *infinite word*, over the alphabet 𝒜 {\cal A} is just an infinite sequence of letters:

 | x = x 1 x 2 ⋯ x n ⋯ where x i ∈ 𝒜, for all i ≥ 1. x=x_{1}x_{2}\cdots x_{n}\cdots\text{ where }x_{i}\in{\cal A},\,\text{ for all }i\geq 1\kern 5.0pt. |  |

For any integer n ≥ 0 n\geq 0, x [n] x_{[n]} will denote the prefix x 1 x 2 ⋯ x n x_{1}x_{2}\cdots x_{n} of x x of length n n. A factor of x x is either the empty word or any sequence x i ⋯ x j x_{i}\cdots x_{j} with i ≤ j i\leq j. The set of all infinite words over 𝒜 {\cal A} is denoted by 𝒜 ω {\cal A}^{\omega}.

For all definitions and notation concerning words not explicitly given in the paper, the reader is referred to the book of M. Lothaire [22]; for Sturmian words see [23, Chap. 2].

### 2.2 The palindromization map

We introduce in 𝒜 ∗ {\cal A}^{*} the operator ( +): 𝒜 ∗ → 𝑃𝐴𝐿 {}^{(+)}:{\cal A}^{*}\rightarrow\mathit{PAL} which maps any word w ∈ 𝒜 ∗ w\in{\cal A}^{*} into the palindrome w ( +) w^{(+)} defined as the shortest palindrome having the prefix w w (cf. [10]). We call w ( +) w^{(+)} the *right palindromic closure of*w w. If Q Q is the longest palindromic suffix of w = u ​ Q w=uQ, then one has

 | w ( +) = u ​ Q ​ u ∼. w^{(+)}=uQu^{\sim}\,. |  |

Let us now define the map

 | ψ: 𝒜 ∗ → 𝑃𝐴𝐿, \psi:{\cal A}^{*}\rightarrow\mathit{PAL}, |  |

called right iterated palindromic closure, or simply palindromization map, as follows: ψ ⁡ ( ε) = ε \psi(\varepsilon)=\varepsilon and for all v ∈ 𝒜 ∗ v\in{\cal A}^{*}, x ∈ 𝒜 x\in{\cal A},

 | ψ ⁡ ( v ​ x) = ( ψ ⁡ ( v) ​ x) ( +). \psi(vx)=(\psi(v)x)^{(+)}\,. |  |

###### Example 2.1.

Let v = a ​ b 2 ​ a v=ab^{2}a. One has ψ ⁡ ( a) = a \psi(a)=a, ψ ⁡ ( a ​ b) = ( a ​ b) ( +) = a ​ b ​ a \psi(ab)=(ab)^{(+)}=aba, ψ ⁡ ( a ​ b 2) = a ​ b ​ a ​ b ​ a \psi(ab^{2})=ababa, and ψ ⁡ ( v) = ( a ​ b ​ a ​ b ​ a ​ a) ( +) = a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a \psi(v)=(ababaa)^{(+)}=ababaababa.

The following proposition summarizes some noteworthy properties of the palindromization map (cf., for instance [10, 16]):

###### Proposition 2.2.

The palindromization map ψ \psi satisfies the following properties:

- P1.

The palindromization map is injective.

- P2.

If u u is a prefix of v v, then ψ ⁡ ( u) \psi(u) is a palindromic prefix (and suffix) of ψ ⁡ ( v) \psi(v).

- P3.

If p p is a prefix of ψ ⁡ ( v) \psi(v), then p ( +) p^{(+)} is a prefix of ψ ⁡ ( v) \psi(v).

- P4.

Every palindromic prefix of ψ ⁡ ( v) \psi(v) is of the form ψ ⁡ ( u) \psi(u) for some prefix u u of v v.

- P5.

The palindromization map ψ \psi commute with the automorphism E E of 𝒜 ∗ {\cal A}^{*} defined by E ⁡ ( a) = b E(a)=b and E ⁡ ( b) = a E(b)=a, i.e., ψ ∘ E = E ∘ ψ. \psi\circ E=E\circ\psi.

- P6.

For every v ∈ 𝒜 ∗ v\in{\cal A}^{*}, | ψ ⁡ ( v) | = | ψ ⁡ ( v ∼) | |\psi(v)|=|\psi(v^{\sim})|.

For any w ∈ ψ ⁡ ( 𝒜 ∗) w\in\psi({\cal A}^{*}) the unique word v v such that ψ ⁡ ( v) = w \psi(v)=w is called the *directive word*of w w. The directive word v v of w = ψ ⁡ ( v) w=\psi(v) can be read from w w just by taking the subsequence of w w formed by all letters immediately following all proper palindromic prefixes of w w.

For any x ∈ 𝒜 x\in{\cal A} let μ x \mu_{x} denote the injective endomorphism of 𝒜 ∗ {\cal A}^{*}

 | μ x: 𝒜 ∗ → 𝒜 ∗ \mu_{x}:{\cal A}^{*}\rightarrow{\cal A}^{*} |  |

defined by

 | μ x ​ ( x) = x, μ x ​ ( y) = x ​ y, for ​ y ∈ 𝒜 ∖ { x }. \mu_{x}(x)=x,\ \ \mu_{x}(y)=xy,\,\,\mbox{for}\,\,y\in{\cal A}\setminus\{x\}. |  | (1) |

If v = x 1 x 2 ⋯ x n v=x_{1}x_{2}\cdots x_{n}, with x i ∈ 𝒜 x_{i}\in{\cal A}, i = 1, …, n i=1,\ldots,n, then we set:

 | μ v = μ x 1 ∘ ⋯ ∘ μ x n; \mu_{v}=\mu_{x_{1}}\circ\cdots\circ\mu_{x_{n}}; |  |

moreover, if v = ε v=\varepsilon, μ ε \mu_{\varepsilon} = id.

The following interesting theorem, proved by J. Justin [19] in the case of an arbitrary alphabet, relates the palindromization map to morphisms μ v \mu_{v}.

###### Theorem 2.3.

For all v, u ∈ 𝒜 ∗ v,u\in{\cal A}^{*},

 | ψ ⁡ ( v ​ u) = μ v ​ ( ψ ⁡ ( u)) ​ ψ ​ ( v). \psi(vu)=\mu_{v}(\psi(u))\psi(v). |  |

In particular, if x ∈ 𝒜 x\in{\cal A}, one has:

 | ψ ⁡ ( x ​ u) = μ x ​ ( ψ ⁡ ( u)) ​ x and ψ ⁡ ( v ​ x) = μ v ​ ( x) ​ ψ ​ ( v). \psi(xu)=\mu_{x}(\psi(u))x\ \ \mbox{and}\ \ \psi(vx)=\mu_{v}(x)\psi(v). |  |

###### Example 2.4.

Let v = a ​ b 2 ​ a v=ab^{2}a. One has (see Example 2.1) ψ ⁡ ( v) = a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a \psi(v)=ababaababa and ψ ⁡ ( a ​ v) = μ a ​ ( ψ ⁡ ( v)) ​ a = a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a \psi(av)=\mu_{a}(\psi(v))a=aabaabaaabaabaa.

One can extend ψ \psi to 𝒜 ω {\cal A}^{\omega} as follows: let x ∈ 𝒜 ω x\in{\cal A}^{\omega} be an infinite word

 | x = x 1 x 2 ⋯ x n ⋯, x i ∈ 𝒜, i ≥ 1. x=x_{1}x_{2}\cdots x_{n}\cdots,\ \ \ x_{i}\in{\cal A},\ i\geq 1. |  |

Since by property P2 of Proposition 2.2 for all n n, ψ ⁡ ( x [n]) \psi(x_{[n]}) is a proper prefix of ψ ⁡ ( x [n + 1]) \psi(x_{[n+1]}), we can define the infinite word ψ ⁡ ( x) \psi(x) as:

 | ψ ⁡ ( x) = lim n → ∞ ψ ⁡ ( x [n]). \psi(x)=\lim_{n\rightarrow\infty}\psi(x_{[n]}). |  |

The extended map ψ: 𝒜 ω → 𝒜 ω \psi:{\cal A}^{\omega}\rightarrow{\cal A}^{\omega} is injective. The word x x is called the directive word of ψ ⁡ ( x) \psi(x). It has been proved in [10] that the word ψ ⁡ ( x) \psi(x) is a characteristic Sturmian word if and only if both the letters a a and b b occur infinitely often in the directive word x x. From property P4 of Proposition 2.2 one easily derives that ψ ⁡ ( 𝒜 ∗) \psi({\cal A}^{*}) is equal to the set of the palindromic prefixes of all characteristic Sturmian words.

###### Example 2.5.

Let 𝒜 = { a, b } {\cal A}=\{a,b\}. If x = ( a ​ b) ω x=(ab)^{\omega}, then the characteristic Sturmian word ψ ⁡ ( ( a ​ b) ω) \psi((ab)^{\omega}) having the directive word x x is the Fibonacci word

 | f = a b a a b a b a a b a a b a b a a b a b a a b a a ⋯ f=abaababaabaababaababaabaa\cdots |  |

## 3 Central, standard, and Christoffel words

In this section we consider three noteworthy classes of finite words called central, standard, and Christoffel words which are closely interrelated and are very important in the combinatorics of Sturmian words as they satisfy remarkable structural properties and, moreover, can be regarded as a finite counterpart of Sturmian sequences.

A word w w is called central if w w has two periods p p and q q such that gcd ⁡ ( p, q) = 1 \gcd(p,q)=1 and | w | = p + q − 2 |w|=p+q-2. Thus a word is central if it is a power of a single letter or is a word of maximal length for which the theorem of Fine and Wilf does not apply. The set of central words, usually denoted by PER \mathop{\textit{PER}}\nolimits, was introduced in [14] where its main properties were studied. It has been proved that PER \mathop{\textit{PER}}\nolimits is equal to the set of the palindromic prefixes of all characteristic Sturmian words, i.e.,

 | PER = ψ ( 𝒜 ∗). \mathop{\textit{PER}}\nolimits=\psi({\cal A}^{*}). |  |

The term *central*was given by J. Berstel and P. Séébold in [23, Chap. 2] to emphasize the central role that these words play in Sturmian words theory.

We say that a central word w w is of order n n if its directive word has length n n. As proved in [14] the number of central words of order n n is ϕ ⁡ ( n + 2) \phi(n+2) where ϕ \phi is the totient Euler function. The following remarkable structural characterization of central words holds [10, 6]:

###### Proposition 3.1.

A word w w is central if and only if w w is a power of a single letter of 𝒜 \cal A or it satisfies the equation:

 | w = w 1 ​ a ​ b ​ w 2 = w 2 ​ b ​ a ​ w 1 w=w_{1}abw_{2}=w_{2}baw_{1} |  |

with w 1, w 2 ∈ 𝒜 ∗ w_{1},w_{2}\in{\cal A}^{*}. Moreover, in this latter case, w 1 w_{1} and w 2 w_{2} are uniquely determined central words, p = | w 1 | + 2 p=|w_{1}|+2 and q = | w 2 | + 2 q=|w_{2}|+2 are coprime periods of w w, and min ⁡ { p, q } \min\{p,q\} is the minimal period of w w.

Another important family of finite words, strictly related to central words, is the class of finite standard words. In fact, characteristic Sturmian words can be equivalently defined in the following way. Let c 1, …, c n, … c_{1},\ldots,c_{n},\ldots be any sequence of integers such that c 1 ≥ 0 c_{1}\geq 0 and c i > 0 c_{i}>0 for i > 1 i>1. We define, inductively, the sequence of words ( s n) n ≥ − 1 (s_{n})_{n\geq-1}, where

 | s − 1 = b, s 0 = a, and ​ s n = s n − 1 c n ​ s n − 2 ​ for ​ n ≥ 1. s_{-1}=b,\ s_{0}=a,\ \mbox{ and }\ s_{n}=s_{n-1}^{c_{n}}s_{n-2}\ \mbox{ for }\ n\geq 1\,. |  |

Since for any n ≥ 0 n\geq 0, s n s_{n} is a proper prefix of s n + 1 s_{n+1}, the sequence ( s n) n ≥ − 1 (s_{n})_{n\geq-1} converges to a limit s s which is a characteristic Sturmian word (cf. [23]). Any characteristic Sturmian word is obtained in this way. The sequence ( c 1, c 2, …, c n, …) (c_{1},c_{2},\ldots,c_{n},\ldots) is called the directive numerical sequence of s s. The Fibonacci word is obtained when c i = 1 c_{i}=1 for i ≥ 1 i\geq 1.

We shall denote by Stand \mathop{\textit{Stand}}\nolimits the set of all the words s n s_{n}, n ≥ − 1 n\geq-1 of any sequence ( s n) n ≥ − 1 (s_{n})_{n\geq-1}. Any word of Stand \mathop{\textit{Stand}}\nolimits is called *finite standard word*, or simply standard word.

The following remarkable relation existing between standard and central words, has been proved in [14]:

 | Stand = 𝒜 ∪ PER { a b, b a }. \mathop{\textit{Stand}}\nolimits={\cal A}\cup\mathop{\textit{PER}}\nolimits\{ab,ba\}. |  |

More precisely, the following holds (see, for instance [11, Propositions 4.9 and 4.10]):

###### Proposition 3.2.

Any standard word different from a single letter can be uniquely expressed as μ v ​ ( x ​ y) \mu_{v}(xy) with { x, y } = { a, b } \{x,y\}=\{a,b\} and v ∈ 𝒜 ∗ v\in{\cal A}^{*}. Moreover, one has:

 | μ v ​ ( x ​ y) = ψ ⁡ ( v) ​ x ​ y. \mu_{v}(xy)=\psi(v)xy. |  |

Let us set for any v ∈ 𝒜 ∗ v\in{\cal A}^{*} and x ∈ 𝒜 x\in{\cal A}, p x ​ ( v) = | μ v ​ ( x) | p_{x}(v)=|\mu_{v}(x)|. From Justin’s formula one derives (see, for instance, [15]) that p x ​ ( v) p_{x}(v) is the minimal period of ψ ⁡ ( v ​ x) \psi(vx) and then a period of ψ ⁡ ( v) \psi(v). Moreover, p x ​ ( v) = π ⁡ ( ψ ⁡ ( v) ​ x) p_{x}(v)=\pi(\psi(v)x), gcd ⁡ ( p x ​ ( v), p y ​ ( v)) = 1 \gcd(p_{x}(v),p_{y}(v))=1,

 | π ⁡ ( ψ ⁡ ( v)) = min ⁡ { p x ​ ( v), p y ​ ( v) }, \pi(\psi(v))=\min\{p_{x}(v),p_{y}(v)\}, |  | (2) |

and from Proposition 3.2,

 | | ψ ⁡ ( v) | = p x ​ ( v) + p y ​ ( v) − 2. |\psi(v)|=p_{x}(v)+p_{y}(v)-2. |  |

Let us now recall the important notion of Christoffel word [8] (see also [2, 3]). Let p p and q q be positive relatively prime integers such that n = p + q n=p+q. The Christoffel word w w of slope p q \frac{p}{q} is defined as w = x 1 ⋯ x n w=x_{1}\cdots x_{n} with

 | x i = { a if i ​ p mod n > ( i − 1) ​ p mod n b if i ​ p mod n < ( i − 1) ​ p mod n x_{i}=\left\{\begin{array}[]{ll}a&\mbox{if $ip\mod n>(i-1)p\mod n$}\\ b&\mbox{if $ip\mod n<(i-1)p\mod n$}\end{array}\right. |  |

for i = 1, …, n i=1,\ldots,n where k mod n k\mod n denotes the remainder of the Euclidean division of k k by n n. The term slope given to the irreducible fraction p q \frac{p}{q} is due to the fact that, as one easily derives from the definition, p = | w | b p=|w|_{b} and q = | w | a q=|w|_{a}. The words a a and b b are also Christoffel words with a respective slope 0 1 \frac{0}{1} and 1 0 \frac{1}{0}. The Christoffel words of slope p q \frac{p}{q} with p p and q q positive integers are called proper Christoffel words.

Let us denote by C ​ H CH the class of Christoffel words. The following important result, proved in [1], shows a basic relation existing between central and Christoffel words:

 | C ​ H = a ​ PER ⁡ b ∪ 𝒜. CH=a\mathop{\textit{PER}}\nolimits b\ \cup\cal A. |  |

Hence, there exists a simple bijection of the set of central words onto the set of proper Christoffel words. Any proper Christoffel word w w can be uniquely represented as a ​ ψ ​ ( v) ​ b a\psi(v)b for a suitable v ∈ 𝒜 ∗ v\in{\cal A}^{*}.

Let < l ​ e ​ x <_{lex} denote the lexicographic order of 𝒜 ∗ {\cal A}^{*} and let L ​ y ​ n ​ d Lynd be the set of Lyndon words [22] of 𝒜 ∗ {\cal A}^{*} and S ​ t St be the set of (finite) factors of all Sturmian words. The following theorem summarizes some results on Christoffel words proved in [4, 1, 3, 15].

###### Theorem 3.3.

Let w = a ​ ψ ​ ( v) ​ b w=a\psi(v)b with v ∈ 𝒜 ∗ v\in{\cal A}^{*} be a proper Christoffel word. Then the following hold:

1. 1.

C ​ H = S ​ t ∩ L ​ y ​ n ​ d CH=St\cap Lynd, i.e., C ​ H CH equals the set of all factors of Sturmian words which are Lyndon words.

2. 2.

There exist and are unique two Christoffel words w 1 w_{1} and w 2 w_{2} such that w = w 1 ​ w 2 w=w_{1}w_{2}. Moreover, w 1 < l ​ e ​ x w 2 w_{1}<_{lex}w_{2}, and ( w 1, w 2) (w_{1},w_{2}) is the standard factorization of w w in Lyndon words.

3. 3.

If w w has the slope η ⁡ ( w) = p q \eta(w)=\frac{p}{q}, then | w 1 | = p ′ |w_{1}|=p^{\prime}, | w 2 | = q ′ |w_{2}|=q^{\prime}, where p ′ p^{\prime} and q ′ q^{\prime} are the respective multiplicative inverse of p p and q q ( m ​ o ​ d ​ | w |) (mod\ |w|). Moreover, p ′ = p a ​ ( v) p^{\prime}=p_{a}(v), q ′ = p b ​ ( v) q^{\prime}=p_{b}(v) and p = p a ​ ( v ∼) p=p_{a}(v^{\sim}), q = p b ​ ( v ∼) q=p_{b}(v^{\sim}).

###### Example 3.4.

The Christoffel word having slope 5 12 \frac{5}{12} is

 | w = a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b = a ​ u ​ b, w=aaabaabaaabaabaab=aub, |  |

where u = a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a = ψ ⁡ ( a 2 ​ b 2 ​ a) u=aabaabaaabaabaa=\psi(a^{2}b^{2}a) is the central word of length 15 15 having the two coprime periods 7 = p a ​ ( v) 7=p_{a}(v) and 10 = p b ​ ( v) 10=p_{b}(v) with v = a 2 ​ b 2 ​ a v=a^{2}b^{2}a. The word w w can be uniquely factorized as w = w 1 ​ w 2 w=w_{1}w_{2}, where w 1 w_{1} and w 2 w_{2} are the Lyndon words w 1 = a ​ a ​ a ​ b ​ a ​ a ​ b w_{1}=aaabaab and w 2 = a ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b w_{2}=aaabaabaab. One has w 1 < l ​ e ​ x w 2 w_{1}<_{lex}w_{2} with | w 1 | = 7 = p a ​ ( v) |w_{1}|=7=p_{a}(v) and | w 2 | = 10 = p b ​ ( v) |w_{2}|=10=p_{b}(v). Moreover, w 2 w_{2} is the proper suffix of w w of maximal length which is a Lyndon word. Finally, ψ ⁡ ( v ∼) = ψ ⁡ ( a ​ b 2 ​ a 2) = a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a \psi(v^{\sim})=\psi(ab^{2}a^{2})=ababaababaababa, p a ​ ( v ∼) = 5 = | w | b p_{a}(v^{\sim})=5=|w|_{b}, p b ​ ( v ∼) = 12 = | w | a p_{b}(v^{\sim})=12=|w|_{a} and | w | b p a ( v) = 5. 7 = 35 ≡ | w | a p b ( v) = 12. 10 = 120 ≡ 1 mod 17 |w|_{b}p_{a}(v)=5^{.}7=35\equiv|w|_{a}p_{b}(v)=12^{.}10=120\equiv 1\mod 17.

## 4 The Fibonacci word

The Fibonacci word f f is without doubt the most famous characteristic Sturmian word. As is well known it can be constructed in several differents ways. As we have seen is Section 2.2, f f can be generated by the palindromization map ψ \psi from the directive word x = ( a ​ b) ω x=(ab)^{\omega}, i.e., f = ψ ⁡ ( x) f=\psi(x). In the following we set for any n ≥ 0 n\geq 0

 | v ( n) = x 1 ⋯ x n = x [n], v^{(n)}=x_{1}\cdots x_{n}=x_{[n]}, |  |

so that v ( 0) = ε v^{(0)}=\varepsilon, v ( 1) = a v^{(1)}=a,

 | v ( n) = ( a ​ b) n 2 ​ if ​ n ​ is even, and ​ v ( n) = ( a ​ b) ⌊ n 2 ⌋ ​ a ​ if ​ n ​ is odd. v^{(n)}=(ab)^{\frac{n}{2}}\ \mbox{ if}\ n\ \mbox{ is even, and}\ v^{(n)}=(ab)^{\lfloor\frac{n}{2}\rfloor}a\mbox{ if}\ n\ \mbox{ is odd}. |  |

###### Theorem 4.1.

Let n ≥ 0 n\geq 0. For any v ∈ 𝒜 n v\in{\cal A}^{n} one has:

 | | ψ ⁡ ( v) | ≤ | ψ ⁡ ( v ( n)) |, |\psi(v)|\leq|\psi(v^{(n)})|, |  |

where the equality holds if and only if

 | v = v ( n) or v = E ⁡ ( v ( n)). v=v^{(n)}\ \ \mbox{or}\ \ v=E(v^{(n)}). |  |

###### Proof.

The proof is by induction on the length n n of v v. The result is trivially true for n ≤ 1 n\leq 1. For n = 2 n=2 the result is also true since | ψ ⁡ ( a ​ a) | = | ψ ⁡ ( b ​ b) | = 2 |\psi(aa)|=|\psi(bb)|=2, whereas | ψ ⁡ ( a ​ b) | = | ψ ⁡ ( b ​ a) | = 3 |\psi(ab)|=|\psi(ba)|=3. Let us then suppose that the result is achieved up to the length n ≥ 2 n\geq 2 and prove it for the length n + 1 n+1.

We can write v ( n + 1) = v ( n) ​ z v^{(n+1)}=v^{(n)}z with z = a z=a if n n is even and z = b z=b, otherwise. By Justin’s formula (cf. Theorem 2.3) one has:

 | ψ ⁡ ( v ( n + 1)) = ψ ⁡ ( v ( n) ​ z) = μ v ( n) ​ ( z) ​ ψ ​ ( v ( n)). \psi(v^{(n+1)})=\psi(v^{(n)}z)=\mu_{v^{(n)}}(z)\psi(v^{(n)}). |  | (3) |

From the definition v ( n) = v ( n − 1) ​ z ¯ v^{(n)}=v^{(n-1)}\bar{z} having set z ¯ = E ⁡ ( z) \bar{z}=E(z). Thus, since by ( 1) μ z ¯ ​ ( z) = z ¯ ​ z \mu_{\bar{z}}(z)=\bar{z}z, from Proposition 3.2 one has

 | μ v ( n) ​ ( z) = ( μ v ( n − 1) ∘ μ z ¯) ​ ( z) = μ v ( n − 1) ​ ( z ¯ ​ z) = ψ ⁡ ( v ( n − 1)) ​ z ¯ ​ z \mu_{v^{(n)}}(z)=(\mu_{v^{(n-1)}}\circ\mu_{\bar{z}})(z)=\mu_{v^{(n-1)}}(\bar{z}z)=\psi(v^{(n-1)})\bar{z}z |  |

and replacing in ( 3), one derives:

 | ψ ⁡ ( v ( n + 1)) = ψ ⁡ ( v ( n − 1)) ​ z ¯ ​ z ​ ψ ​ ( v ( n)). \psi(v^{(n+1)})=\psi(v^{(n-1)})\bar{z}z\psi(v^{(n)}). |  | (4) |

Let v ∈ 𝒜 n + 1 v\in{\cal A}^{n+1} and write v = u ​ y v=uy with u ∈ 𝒜 n u\in{\cal A}^{n} and y ∈ 𝒜 y\in{\cal A}. One has by Justin’s formula:

 | ψ ⁡ ( v) = ψ ⁡ ( u ​ y) = μ u ​ ( y) ​ ψ ​ ( u). \psi(v)=\psi(uy)=\mu_{u}(y)\psi(u). |  | (5) |

If v ∈ y ∗ v\in y^{*}, i.e., v = y n + 1 v=y^{n+1}, then ψ ⁡ ( v) = y n + 1 \psi(v)=y^{n+1}. In this case we are done since for n ≥ 1 n\geq 1, | ψ ⁡ ( v) | = n + 1 < | ψ ⁡ ( v ( n + 1)) | |\psi(v)|=n+1<|\psi(v^{(n+1)})| (cf. Lemma 4.2). Let us then suppose that card ⁡ ( alph ⁡ v) = 2 \card(\alf v)=2. We can write u = u ′ ​ y ¯ ​ ζ u=u^{\prime}\bar{y}\zeta with ζ ∈ y ∗ \zeta\in y^{*} and u ′ ∈ 𝒜 ∗ u^{\prime}\in{\cal A}^{*}. From ( 5) and Proposition 3.2 one has, since μ ζ ​ ( y) = y \mu_{\zeta}(y)=y,

 | ψ ⁡ ( v) = μ u ′ ​ y ¯ ​ ( y) ​ ψ ​ ( u) = ( μ u ′ ∘ μ y ¯) ​ ( y) ​ ψ ​ ( u) = μ u ′ ​ ( y ¯ ​ y) ​ ψ ​ ( u) = ψ ⁡ ( u ′) ​ y ¯ ​ y ​ ψ ​ ( u). \psi(v)=\mu_{u^{\prime}\bar{y}}(y)\psi(u)=(\mu_{u^{\prime}}\circ\mu_{\bar{y}})(y)\psi(u)=\mu_{u^{\prime}}(\bar{y}y)\psi(u)=\psi(u^{\prime})\bar{y}y\psi(u). |  |

From ( 4) and the preceding equation it follows:

 | | ψ ⁡ ( v ( n + 1)) | − | ψ ⁡ ( v) | = ( | ψ ⁡ ( v ( n)) | − | ψ ⁡ ( u) |) + ( | ψ ⁡ ( v ( n − 1)) | − | ψ ⁡ ( u ′) |). |\psi(v^{(n+1)})|-|\psi(v)|=(|\psi(v^{(n)})|-|\psi(u)|)+(|\psi(v^{(n-1)})|-|\psi(u^{\prime})|). |  | (6) |

Setting k = | u ′ | ≤ n − 1 k=|u^{\prime}|\leq n-1 one has | ψ ⁡ ( v ( n − 1)) | ≥ | ψ ⁡ ( v ( k)) | |\psi(v^{(n-1)})|\geq|\psi(v^{(k)})|, so that

 | | ψ ⁡ ( v ( n + 1)) | − | ψ ⁡ ( v) | ≥ ( | ψ ⁡ ( v ( n)) | − | ψ ⁡ ( u) |) + ( | ψ ⁡ ( v ( k)) | − | ψ ⁡ ( u ′) |). |\psi(v^{(n+1)})|-|\psi(v)|\geq(|\psi(v^{(n)})|-|\psi(u)|)+(|\psi(v^{(k)})|-|\psi(u^{\prime})|). |  |

By induction, | ψ ⁡ ( v ( n)) | ≥ | ψ ⁡ ( u) | |\psi(v^{(n)})|\geq|\psi(u)| and | ψ ⁡ ( v ( k)) | ≥ | ψ ⁡ ( u ′) | |\psi(v^{(k)})|\geq|\psi(u^{\prime})| that implies

 | | ψ ⁡ ( v ( n + 1)) | ≥ | ψ ⁡ ( v) |, |\psi(v^{(n+1)})|\geq|\psi(v)|, |  |

which proves the first part of theorem.

If v = v ( n + 1) v=v^{(n+1)} or v = E ⁡ ( v ( n + 1)) v=E(v^{(n+1)}), then | ψ ⁡ ( v) | = | ψ ⁡ ( v ( n + 1)) | |\psi(v)|=|\psi(v^{(n+1)})|. Indeed, one has only to observe that in view of property P5 of Proposition 2.2, ψ ⁡ ( E ⁡ ( v ( n + 1))) = E ⁡ ( ψ ⁡ ( v ( n + 1))) \psi(E(v^{(n+1)}))=E(\psi(v^{(n+1)})), so that | ψ ⁡ ( E ⁡ ( v ( n + 1))) | = | ψ ⁡ ( v ( n + 1)) | |\psi(E(v^{(n+1)}))|=|\psi(v^{(n+1)})|.

Conversely, let us suppose that | ψ ⁡ ( v) | = | ψ ⁡ ( v ( n + 1)) | |\psi(v)|=|\psi(v^{(n+1)})|. From ( 6) one derives:

 | | ψ ⁡ ( v ( n)) | = | ψ ⁡ ( u) ​ | and | ​ ψ ​ ( v ( n − 1)) | = | ψ ⁡ ( u ′) |. |\psi(v^{(n)})|=|\psi(u)|\ \mbox{and}\ |\psi(v^{(n-1)})|=|\psi(u^{\prime})|. |  | (7) |

From equation ( 7) 2 (\ref{eq:fib4})_{2} one obtains k = | u ′ | = n − 1 k=|u^{\prime}|=n-1. Indeed, if k < n − 1 k<n-1 one would have: | ψ ⁡ ( v ( n − 1)) | > | ψ ⁡ ( v ( k)) | ≥ | ψ ⁡ ( u ′) | |\psi(v^{(n-1)})|>|\psi(v^{(k)})|\geq|\psi(u^{\prime})|, a contradiction. Hence, from ( 7) 2 (\ref{eq:fib4})_{2} one has u = u ′ ​ y ¯ u=u^{\prime}\bar{y} and v = u ​ y = u ′ ​ y ¯ ​ y v=uy=u^{\prime}\bar{y}y.

By induction ( 7) is satisfied if and only if

 | a) ​ u = v ( n) ​ or b) ​ u = E ⁡ ( v ( n)) \mbox{ a)}\ u=v^{(n)}\ \mbox{or}\ \ \mbox{b)}\ u=E(v^{(n)}) |  |

and

 | c) ​ u ′ = v ( n − 1) ​ or d) ​ u ′ = E ⁡ ( v ( n − 1)). \mbox{ c)}\ u^{\prime}=v^{(n-1)}\ \mbox{or}\ \ \mbox{d)}\ u^{\prime}=E(v^{(n-1)}). |  |

Since u ′ u^{\prime} is a non-empty prefix of u u, condition OPEN a) a) & \& OPEN d) d), as well as OPEN b) b) & \& OPEN c) c), is a contradiction. Indeed, u ′ u^{\prime} would begin with the letter a a and with the letter b b. Thus ( 7) is satisfied if and only if

 | u = v ( n) ​ and u ′ = v ( n − 1) u=v^{(n)}\ \mbox{and}\ \ \ u^{\prime}=v^{(n-1)} |  |

or

 | u = E ⁡ ( v ( n)) and u ′ = E ⁡ ( v ( n − 1)). u=E(v^{(n)})\ \ \mbox{and}\ \ \ u^{\prime}=E(v^{(n-1)}). |  |

In the first case one has:

 | v ( n + 1) = v ( n) ​ z = u ​ z = v ( n − 1) ​ z ¯ ​ z. v^{(n+1)}=v^{(n)}z=uz=v^{(n-1)}\bar{z}z. |  |

Moreover, u = u ′ ​ y ¯ = v ( n − 1) ​ y ¯ u=u^{\prime}\bar{y}=v^{(n-1)}\bar{y}, so that

 | v ( n + 1) = u ​ z = v ( n − 1) ​ y ¯ ​ z. v^{(n+1)}=uz=v^{(n-1)}\bar{y}z. |  |

Hence, y = z y=z and

 | v = u ​ y = u ​ z = v ( n + 1). v=uy=uz=v^{(n+1)}. |  |

In the second case one has:

 | v = u ​ y = u ′ ​ y ¯ ​ y = E ⁡ ( v ( n − 1)) ​ y ¯ ​ y = E ⁡ ( v ( n)) ​ y. v=uy=u^{\prime}\bar{y}y=E(v^{(n-1)})\bar{y}y=E(v^{(n)})y. |  |

Thus E ⁡ ( v ( n)) = E ⁡ ( v ( n − 1)) ​ y ¯ = E ⁡ ( v ( n − 1) ​ y) E(v^{(n)})=E(v^{(n-1)})\bar{y}=E(v^{(n-1)}y), so that v ( n) = v ( n − 1) ​ y v^{(n)}=v^{(n-1)}y. Since v ( n + 1) = v ( n) ​ z v^{(n+1)}=v^{(n)}z, one derives: v ( n + 1) = v ( n − 1) ​ y ​ z v^{(n+1)}=v^{(n-1)}yz. This implies z = y ¯ z=\bar{y} and

 | v = E ⁡ ( v ( n)) ​ y = E ⁡ ( v ( n + 1)), v=E(v^{(n)})y=E(v^{(n+1)}), |  |

which concludes our proof. ∎

###### Lemma 4.2.

Let ( F n) n ≥ − 1 (F_{n})_{n\geq-1} be the Fibonacci numerical sequence. For all n ≥ 0 n\geq 0 one has:

 | | ψ ⁡ ( v ( n)) | = F n + 1 − 2. |\psi(v^{(n)})|=F_{n+1}-2. |  |

###### Proof.

The result is trivial for n ≤ 1 n\leq 1. Indeed, for n = 0 n=0 one has | ψ ⁡ ( ε) | = 0 |\psi(\varepsilon)|=0 and F 1 = 2 F_{1}=2. For n = 1 n=1, | ψ ⁡ ( a) | = 1 |\psi(a)|=1 and F 2 = 3 F_{2}=3. Suppose by induction the result true up to n n and prove it for n + 1 n+1. By ( 4) one has:

 | | ψ ⁡ ( v ( n + 1)) | = | ψ ⁡ ( v ( n − 1)) | + | ψ ⁡ ( v ( n)) | + 2. |\psi(v^{(n+1)})|=|\psi(v^{(n-1)})|+|\psi(v^{(n)})|+2. |  |

Since by induction | ψ ⁡ ( v ( n − 1)) | = F n − 2 |\psi(v^{(n-1)})|=F_{n}-2 and | ψ ⁡ ( v ( n)) | = F n + 1 − 2 |\psi(v^{(n)})|=F_{n+1}-2, the result follows. ∎

###### Corollary 4.3.

Let n ≥ 0 n\geq 0. For any v ∈ 𝒜 n v\in{\cal A}^{n} one has:

 | | ψ ⁡ ( v) | ≤ F n + 1 − 2, |\psi(v)|\leq F_{n+1}-2, |  |

where the equality holds if and only if

 | v = v ( n) or v = E ⁡ ( v ( n)). v=v^{(n)}\ \ \mbox{or}\ \ v=E(v^{(n)}). |  |

###### Proof.

Immediate from Theorem 4.1 and Lemma 4.2. ∎

Let us recall (cf., Section 3) that a palindromic prefix of a characteristic Sturmian word is of order n n if its directive word is of length n n. From Theorem 4.1 the following extremal property of the Fibonacci word holds:

###### Theorem 4.4.

A characteristic Sturmian word s s has the palindromic prefixes of any order of maximal length if and only if s = f s=f or s = E ⁡ ( f) s=E(f).

###### Proof.

Let s = ψ ⁡ ( y) s=\psi(y), with y = y 1 ⋯ y n ⋯ y=y_{1}\cdots y_{n}\cdots, y i ∈ 𝒜 y_{i}\in{\cal A}, i ≥ 1 i\geq 1, be any characteristic Sturmian word. By Theorem 4.1 for any n ≥ 0 n\geq 0,

 | | ψ ( y 1 ⋯ y n) | ≤ | ψ ( v ( n)) | = | ψ ( E ( v ( n))) |, |\psi(y_{1}\cdots y_{n})|\leq|\psi(v^{(n)})|=|\psi(E(v^{(n)}))|, |  |

where v ( n) v^{(n)} and E ⁡ ( v ( n)) E(v^{(n)}) are respectively the prefixes of ( a ​ b) ω (ab)^{\omega} and of ( b ​ a) ω (ba)^{\omega} of length n n. Since ψ ⁡ ( v ( n)) \psi(v^{(n)}) and E ⁡ ( ψ ⁡ ( v ( n))) E(\psi(v^{(n)})) are respectively the palindromic prefixes of order n n of f f and of E ⁡ ( f) E(f), the ‘if part’ of theorem follows.

Let now s = ψ ⁡ ( y) s=\psi(y) be any characteristic Sturmian word such that for any n n and v ∈ 𝒜 n v\in{\cal A}^{n}, | ψ ( y 1 ⋯ y n) | ≥ | ψ ( v) | |\psi(y_{1}\cdots y_{n})|\geq|\psi(v)|. In particular, one has | ψ ( y 1 ⋯ y n) | ≥ | ψ ( v ( n)) | |\psi(y_{1}\cdots y_{n})|\geq|\psi(v^{(n)})|. By Theorem 4.1 it follows that for any n ≥ 0 n\geq 0

 | | ψ ( y 1 ⋯ y n) | = | ψ ( v ( n)) |. |\psi(y_{1}\cdots y_{n})|=|\psi(v^{(n)})|. |  |

Moreover, the equality occurs if and only if y 1 ⋯ y n = v ( n) y_{1}\cdots y_{n}=v^{(n)} or y 1 ⋯ y n = E ( v ( n)) y_{1}\cdots y_{n}=E(v^{(n)}). Since for n > 0 n>0, v ( n) v^{(n)} begins with the letter a a and E ⁡ ( v ( n)) E(v^{(n)}) begins with the letter b b, it follows that either for any n ≥ 0 n\geq 0, y 1 ⋯ y n = v ( n) y_{1}\cdots y_{n}=v^{(n)} or for any n ≥ 0 n\geq 0, y 1 ⋯ y n = E ( v ( n)) y_{1}\cdots y_{n}=E(v^{(n)}), i.e., s = f s=f or s = E ⁡ ( f) s=E(f), which concludes the proof. ∎

Let us introduce in 𝒜 ∗ {\cal A}^{*} the operator c c defined as: c ⁡ ( ε) = ε c(\varepsilon)=\varepsilon, c ⁡ ( x) = x c(x)=x for any x ∈ 𝒜 x\in{\cal A}, and for v = u ​ x ​ y v=uxy with u ∈ 𝒜 ∗ u\in{\cal A}^{*}, x, y ∈ 𝒜 x,y\in{\cal A}, c ⁡ ( v) = c ⁡ ( u ​ x ​ y) = u ​ y ​ x c(v)=c(uxy)=uyx. Thus the operator c c acting on words v v of length ≥ 2 \geq 2 changes the suffix x ​ y xy of v v of length 2 in y ​ x yx. Note that if x ≠ y x\neq y, then c ⁡ ( u ​ x ​ y) = u ​ x ¯ ​ y ¯ c(uxy)=u\bar{x}\bar{y}. For instance, c ⁡ ( a ​ b ​ b ​ a ​ b ​ a) = a ​ b ​ b ​ a ​ a ​ b c(abbaba)=abbaab. It is ready verified that the operator c c commutes with E E, i.e., c ∘ E = E ∘ c c\circ E=E\circ c.

The following theorem concerns the minimal periods of the central words having a directive word of any length.

###### Theorem 4.5.

For any n ≥ 0 n\geq 0 and v ∈ 𝒜 n v\in{\cal A}^{n},

 | π ⁡ ( ψ ⁡ ( v)) ≤ π ⁡ ( ψ ⁡ ( v ( n))) = F n − 1, \pi(\psi(v))\leq\pi(\psi(v^{(n)}))=F_{n-1}, |  |

where the maximum is reached if and only if v v is one of the following words:

 | v ( n), E ⁡ ( v ( n)), c ⁡ ( v ( n)), and E ⁡ ( c ⁡ ( v ( n))). v^{(n)},E(v^{(n)}),c(v^{(n)}),\ \mbox{and}\ \ E(c(v^{(n)})). |  |

###### Proof.

The result is trivial for n = 0 n=0. We first prove that for any n ≥ 0 n\geq 0 π ⁡ ( ψ ⁡ ( v ( n + 1))) = F n \pi(\psi(v^{(n+1)}))=F_{n}. Indeed, setting v ( n + 1) = v ( n) ​ z v^{(n+1)}=v^{(n)}z with z ∈ 𝒜 z\in{\cal A} one has, in view of ( 4),

 | ψ ⁡ ( v ( n + 1)) = ψ ⁡ ( v ( n − 1)) ​ z ¯ ​ z ​ ψ ​ ( v ( n)) = ψ ⁡ ( v ( n)) ​ z ​ z ¯ ​ ψ ​ ( v ( n − 1)). \psi(v^{(n+1)})=\psi(v^{(n-1)})\bar{z}z\psi(v^{(n)})=\psi(v^{(n)})z\bar{z}\psi(v^{(n-1)}). |  |

From Proposition 3.1 and Lemma 4.2, one has:

 | π ( ψ ( v ( n + 1))) = min { | ψ ( v ( n − 1)) | + 2, | ψ ( v ( n)) |) + 2 } = | ψ ( v ( n − 1)) | + 2 = F n. \pi(\psi(v^{(n+1)}))=\min\{|\psi(v^{(n-1)})|+2,|\psi(v^{(n)})|)+2\}=|\psi(v^{(n-1)})|+2=F_{n}. |  |

We prove now that for any v ∈ 𝒜 n + 1 v\in{\cal A}^{n+1}, π ⁡ ( ψ ⁡ ( v)) ≤ π ⁡ ( ψ ⁡ ( v ( n + 1))) = F n \pi(\psi(v))\leq\pi(\psi(v^{(n+1)}))=F_{n}.

Indeed, we can write v = u ​ y v=uy with u ∈ 𝒜 n u\in{\cal A}^{n} and y ∈ 𝒜 y\in{\cal A}. If u = y n u=y^{n}, then v = y n + 1 v=y^{n+1} and ψ ⁡ ( y n + 1) = y n + 1 \psi(y^{n+1})=y^{n+1} that implies π ⁡ ( y n + 1) = 1 ≤ F n \pi(y^{n+1})=1\leq F_{n}. Let us then suppose card ⁡ ( alph ⁡ v) = 2 \card(\alf v)=2. As we have seen in the proof of Theorem 4.1, we can write u = u ′ ​ y ¯ ​ ζ u=u^{\prime}\bar{y}\zeta with ζ ∈ y ∗ \zeta\in y^{*} and u ′ ∈ 𝒜 ∗ u^{\prime}\in{\cal A}^{*} having:

 | ψ ⁡ ( v) = ψ ⁡ ( u ′) ​ y ¯ ​ y ​ ψ ​ ( u). \psi(v)=\psi(u^{\prime})\bar{y}y\psi(u). |  |

From Proposition 3.1, as | ψ ⁡ ( u ′) | < | ψ ⁡ ( u) | |\psi(u^{\prime})|<|\psi(u)|, one has

 | π ⁡ ( ψ ⁡ ( v)) = | ψ ⁡ ( u ′) | + 2. \pi(\psi(v))=|\psi(u^{\prime})|+2. |  | (8) |

By Theorem 4.1 and Lemma 4.2, | ψ ⁡ ( u ′) | ≤ | ψ ⁡ ( v ( | u ′ |)) | = F | u ′ | + 1 − 2 |\psi(u^{\prime})|\leq|\psi(v^{(|u^{\prime}|)})|=F_{|u^{\prime}|+1}-2. Since | u ′ | ≤ n − 1 |u^{\prime}|\leq n-1 it follows | ψ ⁡ ( u ′) | ≤ F n − 2 |\psi(u^{\prime})|\leq F_{n}-2. Hence, from ( 8) one obtains that for all v ∈ 𝒜 n + 1 v\in{\cal A}^{n+1}, π ⁡ ( ψ ⁡ ( v)) ≤ F n = π ⁡ ( ψ ⁡ ( v ( n + 1))) \pi(\psi(v))\leq F_{n}=\pi(\psi(v^{(n+1)})), and the first part of theorem is proved.

As regards the second part, the result is trivial for n ≤ 1 n\leq 1. We shall suppose n > 1 n>1 and prove that for v ∈ 𝒜 n + 1 v\in{\cal A}^{n+1}, n ≥ 1 n\geq 1, the maximal value of π ⁡ ( ψ ⁡ ( v)) \pi(\psi(v)) is reached if and only if v v is one of the following words v ( n + 1), E ⁡ ( v ( n + 1)) v^{(n+1)},E(v^{(n+1)}), c ⁡ ( v ( n + 1)) c(v^{(n+1)}), and E ⁡ ( c ⁡ ( v ( n + 1))) E(c(v^{(n+1)})).

For what concerns the ‘if part’ of the statement we have proved above that π ⁡ ( ψ ⁡ ( v ( n + 1))) = π ⁡ ( E ⁡ ( ψ ⁡ ( v ( n + 1)))) = π ⁡ ( ψ ⁡ ( E ⁡ ( v ( n + 1)))) = F n \pi(\psi(v^{(n+1)}))=\pi(E(\psi(v^{(n+1)})))=\pi(\psi(E(v^{(n+1)})))=F_{n}. Let us now prove that

 | π ⁡ ( ψ ⁡ ( v ( n + 1))) = π ⁡ ( ψ ⁡ ( c ⁡ ( v ( n + 1)))). \pi(\psi(v^{(n+1)}))=\pi(\psi(c(v^{(n+1)}))). |  |

Since v ( n + 1) = v ( n) ​ z = v ( n − 1) ​ z ¯ ​ z v^{(n+1)}=v^{(n)}z=v^{(n-1)}\bar{z}z, one has c ⁡ ( v ( n + 1)) = v ( n − 1) ​ z ​ z ¯ c(v^{(n+1)})=v^{(n-1)}z\bar{z}. From Justin’s formula one derives:

 | ψ ⁡ ( c ⁡ ( v ( n + 1))) = ψ ⁡ ( v ( n − 1) ​ z ​ z ¯) = μ v ( n − 1) ​ ( z ​ z ¯) ​ ψ ​ ( v ( n − 1) ​ z). \psi(c(v^{(n+1)}))=\psi(v^{(n-1)}z\bar{z})=\mu_{v^{(n-1)}}(z\bar{z})\psi(v^{(n-1)}z). |  |

By Proposition 3.2, μ v ( n − 1) ​ ( z ​ z ¯) = ψ ⁡ ( v ( n − 1)) ​ z ​ z ¯ \mu_{v^{(n-1)}}(z\bar{z})=\psi(v^{(n-1)})z\bar{z}, so that

 | ψ ⁡ ( c ⁡ ( v ( n + 1))) = ψ ⁡ ( v ( n − 1)) ​ z ​ z ¯ ​ ψ ​ ( v ( n − 1) ​ z). \psi(c(v^{(n+1)}))=\psi(v^{(n-1)})z\bar{z}\psi(v^{(n-1)}z). |  |

From Proposition 3.1 and Lemma 4.2, π ⁡ ( ψ ⁡ ( c ⁡ ( v ( n + 1)))) = | ψ ⁡ ( v ( n − 1)) | + 2 = F n = π ⁡ ( ψ ⁡ ( v ( n + 1))) \pi(\psi(c(v^{(n+1)})))=|\psi(v^{(n-1)})|+2=F_{n}=\pi(\psi(v^{(n+1)})).

Let us now prove the ‘only if part’. We suppose that v ∈ 𝒜 n + 1 v\in{\cal A}^{n+1} is such that π ⁡ ( ψ ⁡ ( v)) = π ⁡ ( ψ ⁡ ( v ( n + 1))) = F n \pi(\psi(v))=\pi(\psi(v^{(n+1)}))=F_{n}. This implies by ( 8),

 | | ψ ⁡ ( u ′) | = F n − 2 ​ and ​ | u ′ | = n − 1. |\psi(u^{\prime})|=F_{n}-2\ \mbox{ and}\ |u^{\prime}|=n-1. |  |

By Theorem 4.1 this can occur if and only if

 | u ′ = v ( n − 1) ​ or u ′ = E ⁡ ( v ( n − 1)). u^{\prime}=v^{(n-1)}\ \mbox{or}\ \ u^{\prime}=E(v^{(n-1)}). |  |

Let us recall that v ( n + 1) = v ( n − 1) ​ z ¯ ​ z v^{(n+1)}=v^{(n-1)}\bar{z}z and v = u ′ ​ y ¯ ​ y v=u^{\prime}\bar{y}y. Suppose first u ′ = v ( n − 1) u^{\prime}=v^{(n-1)}. If y = z y=z, we have v = v ( n − 1) ​ z ¯ ​ z = v ( n + 1) v=v^{(n-1)}\bar{z}z=v^{(n+1)}. If y = z ¯ y=\bar{z}, then one has v = v ( n − 1) ​ z ​ z ¯ = c ⁡ ( v ( n + 1)) v=v^{(n-1)}z\bar{z}=c(v^{(n+1)}). In the case u ′ = E ⁡ ( v ( n − 1)) u^{\prime}=E(v^{(n-1)}) one has v = E ⁡ ( v ( n − 1)) ​ y ¯ ​ y v=E(v^{(n-1)})\bar{y}y. If y = z ¯ y=\bar{z}, then v = E ⁡ ( v ( n − 1) ​ z ¯ ​ z) = E ⁡ ( v ( n + 1)) v=E(v^{(n-1)}\bar{z}z)=E(v^{(n+1)}). If y = z y=z, then v = E ⁡ ( v ( n − 1) ​ z ​ z ¯) = E ⁡ ( c ⁡ ( v ( n + 1))) v=E(v^{(n-1)}z\bar{z})=E(c(v^{(n+1)})), which concludes the proof. ∎

###### Example 4.6.

For n = 4 n=4 the maximum value of the minimal period of central words of order 4 is 5 = F 3 5=F_{3}. It is reached with the directive words a ​ b ​ a ​ b abab, a ​ b ​ b ​ a abba, b ​ a ​ b ​ a baba, and b ​ a ​ a ​ b baab. The corresponding central words are respectively, ψ ⁡ ( a ​ b ​ a ​ b) = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a \psi(abab)=abaababaaba, ψ ⁡ ( a ​ b ​ b ​ a) = a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a \psi(abba)=ababaababa, E ⁡ ( ψ ⁡ ( a ​ b ​ a ​ b)) E(\psi(abab)), and E ⁡ ( ψ ⁡ ( a ​ b ​ b ​ a)) E(\psi(abba)).

###### Theorem 4.7.

The minimal periods of the palindromic prefixes of any order of a characteristic Sturmian word s s are maximal if and only if s = f s=f or s = E ⁡ ( f) s=E(f).

###### Proof.

The proof follows the same lines of that of Theorem 4.4. Let s = ψ ⁡ ( y) s=\psi(y), with y = y 1 ⋯ y n ⋯ y=y_{1}\cdots y_{n}\cdots, y i ∈ 𝒜 y_{i}\in{\cal A}, i ≥ 1 i\geq 1, be any characteristic Sturmian word. By Theorem 4.5, for any n ≥ 0 n\geq 0,

 | π ( ψ ( y 1 ⋯ y n)) ≤ π ( ψ ( v ( n))) = π ( ψ ( E ( v ( n)))), \pi(\psi(y_{1}\cdots y_{n}))\leq\pi(\psi(v^{(n)}))=\pi(\psi(E(v^{(n)}))), |  |

where v ( n) v^{(n)} and E ⁡ ( v ( n)) E(v^{(n)}) are respectively the prefixes of ( a ​ b) ω (ab)^{\omega} and of ( b ​ a) ω (ba)^{\omega} of length n n. Since ψ ⁡ ( v ( n)) \psi(v^{(n)}) and E ⁡ ( ψ ⁡ ( v ( n))) E(\psi(v^{(n)})) are respectively the palindromic prefixes of order n n of f f and E ⁡ ( f) E(f), the ‘if part’ of theorem follows.

Let now s = ψ ⁡ ( y) s=\psi(y) be any characteristic Sturmian word such that for any n n and v ∈ 𝒜 n v\in{\cal A}^{n}, π ( ψ ( y 1 ⋯ y n)) ≥ π ( ψ ( v)) \pi(\psi(y_{1}\cdots y_{n}))\geq\pi(\psi(v)). In particular, one has π ( ψ ( y 1 ⋯ y n)) ≥ π ( ψ ( v ( n))) \pi(\psi(y_{1}\cdots y_{n}))\geq\pi(\psi(v^{(n)})). By Theorem 4.5 it follows that for any n ≥ 0 n\geq 0

 | π ( ψ ( y 1 ⋯ y n)) = π ( ψ ( v ( n))), \pi(\psi(y_{1}\cdots y_{n}))=\pi(\psi(v^{(n)})), |  | (9) |

where the equality occurs if and only if for any n n, y 1 ⋯ y n y_{1}\cdots y_{n} is one of the following words v ( n), E ⁡ ( v ( n)), c ⁡ ( v ( n)) v^{(n)},E(v^{(n)}),c(v^{(n)}), and E ⁡ ( c ⁡ ( v ( n))) E(c(v^{(n)})). We can suppose, without loss of generality, that y 1 = a y_{1}=a, i.e., y ∈ a ​ 𝒜 ω y\in a{\cal A}^{\omega}. In this case equality ( 9) implies that for each n n

 | either y 1 ⋯ y n = v ( n) or y 1 ⋯ y n = c ( v ( n)). \mbox{either}\ \ y_{1}\cdots y_{n}=v^{(n)}\ \ \mbox{or}\ \ \ y_{1}\cdots y_{n}=c(v^{(n)}). |  |

Let us prove that the preceding equation implies that for all n ≥ 0 n\geq 0 one has y 1 ⋯ y n = v ( n) y_{1}\cdots y_{n}=v^{(n)}. This is trivial for n ≤ 1 n\leq 1. For n = 2 n=2, one has that y 1 ​ y 2 = v ( 2) = a ​ b y_{1}y_{2}=v^{(2)}=ab or y 1 ​ y 2 = b ​ a y_{1}y_{2}=ba. However, this second case cannot occur since y 1 = a y_{1}=a. Thus y 1 ​ y 2 = v ( 2) y_{1}y_{2}=v^{(2)}. Let us now prove by induction that if y 1 ⋯ y n = v ( n) y_{1}\cdots y_{n}=v^{(n)} with n ≥ 2 n\geq 2, then y 1 ⋯ y n + 1 = v ( n + 1) y_{1}\cdots y_{n+1}=v^{(n+1)}. Indeed, suppose by contradiction that y 1 ⋯ y n − 1 y n y n + 1 = c ( v ( n + 1)) y_{1}\cdots y_{n-1}y_{n}y_{n+1}=c(v^{(n+1)}). This would imply v ( n + 1) = y 1 ⋯ y n − 1 y ¯ n y ¯ n + 1 v^{(n+1)}=y_{1}\cdots y_{n-1}\bar{y}_{n}\bar{y}_{n+1}, so that v ( n) = y 1 ⋯ y n − 1 y ¯ n v^{(n)}=y_{1}\cdots y_{n-1}\bar{y}_{n} which is absurd. Thus y = ( a ​ b) ω y=(ab)^{\omega} and s = f s=f.

If y ∈ b ​ 𝒜 ω y\in b{\cal A}^{\omega}, one proves in a perfect similar way that y = ( b ​ a) ω y=(ba)^{\omega}, i.e., s = E ⁡ ( f) s=E(f) and this concludes the proof. ∎

The following lemma relates the composition, i.e., the number of letters a a and b b, of a proper Christoffel word a ​ ψ ​ ( v) ​ b a\psi(v)b to the minimal period of ψ ⁡ ( v ∼) \psi(v^{\sim}).

###### Lemma 4.8.

For any proper Christoffel word w = a ​ ψ ​ ( v) ​ b w=a\psi(v)b,

 | π ⁡ ( ψ ⁡ ( v ∼)) = min ⁡ { | w | a, | w | b }. \pi(\psi(v^{\sim}))=\min\{|w|_{a},|w|_{b}\}. |  |

In particular, if v ∈ a ​ 𝒜 ∗ v\in a{\cal A}^{*}, then

 | π ⁡ ( ψ ⁡ ( v ∼)) = | ψ ⁡ ( v) | b + 1. \pi(\psi(v^{\sim}))=|\psi(v)|_{b}+1. |  |

###### Proof.

In view of ( 2) and statement 3. of Theorem 3.3, one has

 | π ⁡ ( ψ ⁡ ( v ∼)) = min ⁡ { p a ​ ( v ∼), p b ​ ( v ∼) } = min ⁡ { | w | a, | w | b }. \pi(\psi(v^{\sim}))=\min\{p_{a}(v^{\sim}),p_{b}(v^{\sim})\}=\min\{|w|_{a},|w|_{b}\}. |  |

If v ∈ a ​ 𝒜 ∗ v\in a{\cal A}^{*}, then | w | b < | w | a |w|_{b}<|w|_{a}. Hence, in such a case

 | π ⁡ ( ψ ⁡ ( v ∼)) = | w | b = | ψ ⁡ ( v) | b + 1. ∎ \pi(\psi(v^{\sim}))=|w|_{b}=|\psi(v)|_{b}+1.\qed |  |

Let us denote by d d the operator in 𝒜 ∗ {\cal A}^{*} defined as: d ⁡ ( ε) = ε d(\varepsilon)=\varepsilon, d ⁡ ( x) = x d(x)=x for any x ∈ 𝒜 x\in{\cal A}, and for v = x ​ y ​ u v=xyu with u ∈ 𝒜 ∗ u\in{\cal A}^{*}, x, y ∈ 𝒜 x,y\in{\cal A}, d ⁡ ( v) = d ⁡ ( x ​ y ​ u) = y ​ x ​ u d(v)=d(xyu)=yxu. Thus the operator d d acting on words v v of length ≥ 2 \geq 2 changes the prefix x ​ y xy of v v of length 2 in y ​ x yx. As it is readily verified the operator d d is related to c c as follows: for any v ∈ 𝒜 ∗ v\in{\cal A}^{*}, d ⁡ ( v) = ( c ⁡ ( v ∼)) ∼ d(v)=(c(v^{\sim}))^{\sim}. Moreover, d d commute with E E.

###### Theorem 4.9.

For any n ≥ 0 n\geq 0 and v ∈ a ​ 𝒜 ∗ v\in a{\cal A}^{*} of length n n

 | | ψ ⁡ ( v) | b ≤ | ψ ⁡ ( v ( n)) | b = F n − 1 − 1, |\psi(v)|_{b}\leq|\psi(v^{(n)})|_{b}=F_{n-1}-1, |  |

where the equality holds if and only if v = v ( n) v=v^{(n)} or v = E ⁡ ( d ⁡ ( v ( n))) v=E(d(v^{(n)})).

###### Proof.

By Lemma 4.8 one has:

 | | ψ ⁡ ( v) | b = π ⁡ ( ψ ⁡ ( v ∼)) − 1 ​ and ​ | ψ ⁡ ( v ( n)) | b = π ⁡ ( ψ ⁡ ( ( v ( n)) ∼)) − 1. |\psi(v)|_{b}=\pi(\psi(v^{\sim}))-1\ \mbox{and}\ |\psi(v^{(n)})|_{b}=\pi(\psi((v^{(n)})^{\sim}))-1. |  |

By Theorem 4.5,

 | π ⁡ ( ψ ⁡ ( v ∼)) ≤ π ⁡ ( ψ ⁡ ( v ( n))) = F n − 1. \pi(\psi(v^{\sim}))\leq\pi(\psi(v^{(n)}))=F_{n-1}. |  |

Moreover, since ( v ( n)) ∼ (v^{(n)})^{\sim} is equal to v ( n) v^{(n)} if n n is odd and is equal to E ⁡ ( v ( n)) E(v^{(n)}) if n n is even, by Theorem 4.5 one has

 | π ⁡ ( ψ ⁡ ( ( v ( n)) ∼)) = π ⁡ ( ψ ⁡ ( v ( n))). \pi(\psi((v^{(n)})^{\sim}))=\pi(\psi(v^{(n)})). |  |

Hence,

 | | ψ ⁡ ( v) | b = π ⁡ ( ψ ⁡ ( v ∼)) − 1 ≤ F n − 1 − 1 = | ψ ⁡ ( v ( n)) | b |\psi(v)|_{b}=\pi(\psi(v^{\sim}))-1\leq F_{n-1}-1=|\psi(v^{(n)})|_{b} |  |

and the first part of the theorem is proved.

Now | ψ ⁡ ( v) | b = | ψ ⁡ ( v ( n)) | b |\psi(v)|_{b}=|\psi(v^{(n)})|_{b} if and only if

 | π ⁡ ( ψ ⁡ ( v ∼)) = π ⁡ ( ψ ⁡ ( v ( n))). \pi(\psi(v^{\sim}))=\pi(\psi(v^{(n)})). |  |

By Theorem 4.5 this occurs if and only if v ∼ v^{\sim} is one of the following words: v ( n), E ⁡ ( v ( n)), c ⁡ ( v ( n)) v^{(n)},E(v^{(n)}),c(v^{(n)}), and E ⁡ ( c ⁡ ( v ( n))) E(c(v^{(n)})). We have to consider two cases:

Case 1. n n is even. The word v ( n) v^{(n)} terminates with the letter b b, so that, as v v begins with the letter a a, v ∼ v^{\sim} cannot be equal to v ( n) v^{(n)}. Similarly, v ∼ v^{\sim} cannot be equal to E ⁡ ( c ⁡ ( v ( n))) E(c(v^{(n)})). Indeed, c ⁡ ( v ( n)) c(v^{(n)}) terminates with the letter a a and E ⁡ ( c ⁡ ( v ( n))) E(c(v^{(n)})) with the letter b b. This would imply that, v v will begin with the letter b b which is a contradiction.

Now, as one easily verifies, v ∼ = E ⁡ ( v ( n)) v^{\sim}=E(v^{(n)}) if and only if v = v ( n) v=v^{(n)}. Moreover, v ∼ = c ⁡ ( v ( n)) v^{\sim}=c(v^{(n)}) if and only if v = E ⁡ ( d ⁡ ( v ( n))) v=E(d(v^{(n)})).

Case 2. n n is odd. The word v ( n) v^{(n)} is a palindrome beginning and terminating with the letter a a. Thus E ⁡ ( v ( n)) E(v^{(n)}) is also a palindrome terminating with the letter b b. Thus, as v v begins with the letter a a, v ∼ v^{\sim} cannot be equal to E ⁡ ( v ( n)) E(v^{(n)}). Similarly, the word c ⁡ ( v ( n)) c(v^{(n)}) terminates with the letter b b, so that v ∼ v^{\sim} cannot be equal to c ⁡ ( v ( n)) c(v^{(n)}).

Trivially, as v ( n) v^{(n)} is a palindrome, v ∼ = v ( n) v^{\sim}=v^{(n)} if and only if v = v ( n) v=v^{(n)}. Finally, it is ready verified that v ∼ = E ⁡ ( c ⁡ ( v ( n))) v^{\sim}=E(c(v^{(n)})) if and only if v = E ⁡ ( d ⁡ ( v ( n))) v=E(d(v^{(n)})).

Hence, in conclusion the maximal value of | ψ ⁡ ( v) | b |\psi(v)|_{b} is reached if and only if v = v ( n) v=v^{(n)} or v = E ⁡ ( d ⁡ ( v ( n))) v=E(d(v^{(n)})). ∎

###### Example 4.10.

For n = 5 n=5 the central words of a ​ 𝒜 ∗ a{\cal A}^{*} with a maximal number of b b have the directive words v ( 5) = a ​ b ​ a ​ b ​ a v^{(5)}=ababa and E ⁡ ( d ⁡ ( v ( 5))) = a ​ b ​ b ​ a ​ b E(d(v^{(5)}))=abbab. One has ψ ⁡ ( a ​ b ​ a ​ b ​ a) = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a \psi(ababa)=abaababaabaababaaba, ψ ⁡ ( a ​ b ​ b ​ a ​ b) = a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a \psi(abbab)=ababaabababaababa, and the number of b b is 7 = F 5 − 1 7=F_{5}-1.

###### Theorem 4.11.

The only characteristic Sturmian words beginning with the letter a a whose palindromic prefixes of any order have the maximal number of occurrences of the letter b b are the Fibonacci word f = ψ ⁡ ( ( a ​ b) ω 𝐶𝐿𝑂𝑆𝐸 f=\psi((ab)^{\omega} and the word g = ψ ⁡ ( a ​ b 2 ​ ( a ​ b) ω) g=\psi(ab^{2}(ab)^{\omega}).

###### Proof.

Let s = ψ ⁡ ( y) s=\psi(y) be any characteristic Sturmian word such that y = y 1 y 2 ⋯ y n ⋯ y=y_{1}y_{2}\cdots y_{n}\cdots, with y 1 = a y_{1}=a and y i ∈ 𝒜 y_{i}\in{\cal A} for i > 1 i>1. Let us suppose that for any n ≥ 1 n\geq 1,

 | | ψ ( y 1 y 2 ⋯ y n) | b = | ψ ( x 1 x 2 ⋯ x n) | b |\psi(y_{1}y_{2}\cdots y_{n})|_{b}=|\psi(x_{1}x_{2}\cdots x_{n})|_{b} |  |

where x 1 x 2 ⋯ x n = v ( n) x_{1}x_{2}\cdots x_{n}=v^{(n)} is the prefix of length n n of the word ( a ​ b) ω (ab)^{\omega}. Setting v = y 1 y 2 ⋯ y n v=y_{1}y_{2}\cdots y_{n}, from Theorem 4.9 the preceding equality can occur if and only if v = v ( n) v=v^{(n)} or v = E ⁡ ( d ⁡ ( v ( n))) v=E(d(v^{(n)})), that is

 | v = x 1 x 2 x 3 ⋯ x n or v = x 1 x 2 x 2 x 3 ⋯ x n − 1. v=x_{1}x_{2}x_{3}\cdots x_{n}\ \mbox{or}\ \ v=x_{1}x_{2}x_{2}x_{3}\cdots x_{n-1}. |  |

For any n > 2 n>2, if y 1 y 2 ⋯ y n = v ( n) y_{1}y_{2}\cdots y_{n}=v^{(n)}, then y 1 y 2 ⋯ y n y n + 1 ≠ E ( d ( v ( n + 1))) y_{1}y_{2}\cdots y_{n}y_{n+1}\neq E(d(v^{(n+1)})) so that y 1 y 2 ⋯ y n y n + 1 = v ( n + 1) y_{1}y_{2}\cdots y_{n}y_{n+1}=v^{(n+1)}. Similarly, if y 1 y 2 ⋯ y n = E ( d ( v ( n))) y_{1}y_{2}\cdots y_{n}=E(d(v^{(n)})), then y 1 y 2 ⋯ y n y n + 1 ≠ v ( n + 1) y_{1}y_{2}\cdots y_{n}y_{n+1}\neq v^{(n+1)} so that y 1 y 2 ⋯ y n y n + 1 = E ( d ( v ( n + 1))) y_{1}y_{2}\cdots y_{n}y_{n+1}=E(d(v^{(n+1)})).

Thus if y 1 ​ y 2 ​ y 3 = v ( 3) = a ​ b ​ a y_{1}y_{2}y_{3}=v^{(3)}=aba, then y = ( a ​ b) ω y=(ab)^{\omega} and s = ψ ⁡ ( ( a ​ b) ω) = f s=\psi((ab)^{\omega})=f. If, on the contrary, y 1 ​ y 2 ​ y 3 = E ⁡ ( d ⁡ ( v ( 3))) = a ​ b ​ b y_{1}y_{2}y_{3}=E(d(v^{(3)}))=abb, then y = a ​ b 2 ​ ( a ​ b) ω y=ab^{2}(ab)^{\omega} and s = ψ ⁡ ( a ​ b 2 ​ ( a ​ b) ω) s=\psi(ab^{2}(ab)^{\omega}). ∎

From the preceding theorem one derives the following extremal property of Fibonacci word.

###### Corollary 4.12.

Fibonacci word is the unique characteristic Sturmian word s s whose directive word begins with a ​ b ​ a aba, or equivalently s s begins with a ​ b ​ a ​ a abaa, such that its palindromic prefixes of any order have the maximal number of occurrences of the letter b b.

## 5 Arithmetization

In this section we shall give an interpretation of the extremal properties satisfied by the palindromic prefixes of f f and E ⁡ ( f) E(f) shown in the preceding section, in terms of continued fractions and more precisely of continuants.

Any word v ∈ 𝒜 ∗ v\in{\cal A}^{*} can be uniquely represented as:

 | v = b α 0 a α 1 b α 2 ⋯ a α m − 1 b α m, v=b^{\alpha_{0}}a^{\alpha_{1}}b^{\alpha_{2}}\cdots a^{\alpha_{m-1}}b^{\alpha_{m}}, |  |

where m m is an even integer, α i > 0 \alpha_{i}>0, i = 1, …, m − 1 i=1,\dots,m-1, and α 0 ≥ 0 \alpha_{0}\geq 0, α m ≥ 0 \alpha_{m}\geq 0. We call the list ( α 0, α 1, …, α n) (\alpha_{0},\alpha_{1},\dots,\alpha_{n}), where n = m n=m if α m > 0 \alpha_{m}>0 and n = m − 1 n=m-1 otherwise, the *integral representation*of the word v v.

We can identify the word v v with its integral representation and write v ≡ ( α 0, α 1, …, α n) v\equiv(\alpha_{0},\alpha_{1},\dots,\alpha_{n}). One has:

 | | v | = ∑ i = 0 n | α i |. |v|=\sum_{i=0}^{n}|\alpha_{i}|. |  |

For instance, the words v 1 = b 2 ​ a ​ b ​ a 2 v_{1}=b^{2}aba^{2} and v 2 = a 3 ​ b ​ a ​ b 2 v_{2}=a^{3}bab^{2} have the integral representations v 1 ≡ ( 2, 1, 1, 2) v_{1}\equiv(2,1,1,2) and v 2 ≡ ( 0, 3, 1, 1, 2) v_{2}\equiv(0,3,1,1,2).

If v ∈ 𝒜 ω v\in{\cal A}^{\omega} is the directive word of the characteristic word ψ ⁡ ( v) \psi(v), then v v can be uniquely represented by

 | v = b α 0 a α 1 b α 2 ⋯, v=b^{\alpha_{0}}a^{\alpha_{1}}b^{\alpha_{2}}\cdots, |  |

with α 0 ≥ 0 \alpha_{0}\geq 0 and α i > 0 \alpha_{i}>0, i > 0 i>0. The infinite sequence ( α 0, α 1, α 2, ⋯, α n, ⋯) ({\alpha_{0}},{\alpha_{1}},{\alpha_{2}},\cdots,{\alpha_{n}},\cdots) is called the integral representation of v v. It has been proved in [10] that if α 0 = 0 \alpha_{0}=0 then ( α 1, α 2, ⋯, α n, ⋯) ({\alpha_{1}},{\alpha_{2}},\cdots,{\alpha_{n}},\cdots) coincides with the directive numerical sequence of the characteristic word ψ ⁡ ( v) \psi(v). If α 0 > 0 \alpha_{0}>0, then the directive numerical sequence of ψ ⁡ ( v) \psi(v) is ( 0, α 0, α 1, …, α n, …) (0,\alpha_{0},\alpha_{1},\ldots,\alpha_{n},\ldots).

The following important theorem holds (cf. [1, 2]):

###### Theorem 5.1.

Let w = a ​ u ​ b w=aub be a proper Christoffel word with u = ψ ⁡ ( v) u=\psi(v) and ( α 0, α 1, …, α n) (\alpha_{0},\alpha_{1},\ldots,\alpha_{n}), n ≥ 0 n\geq 0, be the integral representation of v v. Then the slope η ⁡ ( w) \eta(w) of w w is given by the continued fraction

 | [α 0; α 1, …, α n − 1, α n + 1]. [\alpha_{0};\alpha_{1},\ldots,\alpha_{n-1},\alpha_{n}+1]. |  |

We remark that in the case n = 0 n=0 the preceding formula becomes [α 0 + 1] [\alpha_{0}+1], or, equivalently, [α 0; 1] [\alpha_{0};1].

###### Example 5.2.

Let v = a 2 ​ b 2 ​ a v=a^{2}b^{2}a. One has w = a 3 ​ b ​ a 2 ​ b ​ a 3 ​ b ​ a 2 ​ b ​ a 2 ​ b w=a^{3}ba^{2}ba^{3}ba^{2}ba^{2}b and η ⁡ ( w) = [0; 2, 2, 2] \eta(w)=[0;2,2,2] = 5 12 \frac{5}{12}. If v = b ​ a 2 ​ b v=ba^{2}b, then w = a ​ b ​ a ​ b ​ a ​ b ​ b ​ a ​ b ​ a ​ b ​ b w=abababbababb and η ⁡ ( w) = [1; 2, 2] \eta(w)=[1;2,2] = 7 5 \frac{7}{5}. If v = b 3 v=b^{3}, then w = a ​ b 4 w=ab^{4} and η ⁡ ( w) = 4 1 = [4] = [3; 1] \eta(w)=\frac{4}{1}=[4]=[3;1].

Let [a 0; a 1, …, a n] [a_{0};a_{1},\ldots,a_{n}] be a continued fraction. As is well known (see, for instance, [21]), for any 0 ≤ k ≤ n 0\leq k\leq n, the k k -order convergent C k = [a 0; a 1, …, a k] C_{k}=[a_{0};a_{1},\ldots,a_{k}] is given by the ratio A k B k \frac{A_{k}}{B_{k}}, where ( A k) k ≥ − 1 (A_{k})_{k\geq-1}, ( B k) k ≥ − 1 (B_{k})_{k\geq-1} is a bisequence defined by

 | A − 1 = 1, A 0 = a 0, B − 1 = 0, B 0 = 1 A_{-1}=1,\ A_{0}=a_{0},\ B_{-1}=0,\ B_{0}=1 |  |

and

 | A k + 1 = a k + 1 ​ A k + A k − 1, B k + 1 = a k + 1 ​ B k + B k − 1, A_{k+1}=a_{k+1}A_{k}+A_{k-1},\ B_{k+1}=a_{k+1}B_{k}+B_{k-1}, |  |

for 0 ≤ k ≤ n − 1 0\leq k\leq n-1. For any k ≥ 0 k\geq 0 the fraction A k B k \frac{A_{k}}{B_{k}} is irreducible.

Let us now set for any k ≥ − 1 k\geq-1,

 | P k = A k + B k. P_{k}=A_{k}+B_{k}. |  |

One has that P − 1 = 1 P_{-1}=1, P 0 = a 0 + 1 P_{0}=a_{0}+1, and

 | P k + 1 = a k + 1 ​ P k + P k − 1, for ​ k ≥ 0. P_{k+1}=a_{k+1}P_{k}+P_{k-1},\ \ \mbox{for}\ k\geq 0. |  | (10) |

The value of P n P_{n} for n ≥ 0 n\geq 0 can be expressed in terms of continuants (cf. [18]) (called cumulants in [24]). Let a 0, a 1, …, a n, … a_{0},a_{1},\ldots,a_{n},\ldots be any sequence of numbers. The n n -th continuant K ⁡ [a 0, …, a n] K[a_{0},\ldots,a_{n}] is defined recursively as: K ⁡ [] = 1 K[\ \ ]=1, K ⁡ [a 0] = a 0 K[a_{0}]=a_{0}, and for n ≥ 1 n\geq 1,

 | K ⁡ [a 0, a 1, …, a n] = a n ​ K ​ [a 0, a 1, …, a n − 1] + K ⁡ [a 0, a 1, …, a n − 2]. K[a_{0},a_{1},\ldots,a_{n}]=a_{n}K[a_{0},a_{1},\ldots,a_{n-1}]+K[a_{0},a_{1},\ldots,a_{n-2}]. |  | (11) |

As it is ready verified for any n ≥ 0 n\geq 0, K ⁡ [a 0, a 1, …, a n] K[a_{0},a_{1},\ldots,a_{n}] is a multivariate polynomial in the variables a 0, a 1, …, a n a_{0},a_{1},\ldots,a_{n} which is obtained by starting with the product a 0 a 1 ⋯ a n a_{0}a_{1}\cdots a_{n} and then striking out adjacent pairs a k ​ a k + 1 a_{k}a_{k+1} in all possible ways. For instance, K ⁡ [a 0, a 1, a 2, a 3, a 4] = a 0 ​ a 1 ​ a 2 ​ a 3 ​ a 4 + a 2 ​ a 3 ​ a 4 + a 0 ​ a 3 ​ a 4 + a 0 ​ a 1 ​ a 4 + a 0 ​ a 1 ​ a 2 + a 0 + a 2 + a 4. K[a_{0},a_{1},a_{2},a_{3},a_{4}]=a_{0}a_{1}a_{2}a_{3}a_{4}+a_{2}a_{3}a_{4}+a_{0}a_{3}a_{4}+a_{0}a_{1}a_{4}+a_{0}a_{1}a_{2}+a_{0}+a_{2}+a_{4}.

We recall (cf. [18, 24]) that for every n ≥ 0 n\geq 0,

 | K ⁡ [a 0, …, a n] = K ⁡ [a n, …, a 0], K[a_{0},\ldots,a_{n}]=K[a_{n},\ldots,a_{0}], |  | (12) |

i.e., a continuant does not change its value by reversing the order of its elements; moreover, one has K ⁡ [1 n] = F n − 1 K[1^{n}]=F_{n-1}, where we have denoted by 1 n 1^{n} the sequence of length n n, ( 1, 1, …, 1) (1,1,\ldots,1). A further property that we shall use in the following, is:

 | K ⁡ [a 0, …, a n, 1] = K ⁡ [a 0, …, a n − 1, a n + 1]. K[a_{0},\ldots,a_{n},1]=K[a_{0},\ldots,a_{n-1},a_{n}+1]. |  | (13) |

There exists a strong relation between continued fractions and continuants. More precisely the following holds. Let [a 0; a 1, …, a n] [a_{0};a_{1},\ldots,a_{n}] be any continued fraction. Then

 | [a 0; a 1, …, a n] = K ⁡ [a 0, a 1, …, a n] K ⁡ [a 1, …, a n] [a_{0};a_{1},\ldots,a_{n}]=\frac{K[a_{0},a_{1},\ldots,a_{n}]}{K[a_{1},\ldots,a_{n}]} |  | (14) |

Indeed, as is ready verified, K ⁡ [a 0, a 1, …, a n] = A n K[a_{0},a_{1},\ldots,a_{n}]=A_{n} and K ⁡ [a 1, …, a n] = B n K[a_{1},\ldots,a_{n}]=B_{n}.

From ( 10) and ( 11), or using the preceding properties of continuants, one derives that if [a 0; a 1, …, a n] [a_{0};a_{1},\ldots,a_{n}] is a continued fraction, then for any n ≥ 0 n\geq 0,

 | P n = A n + B n = K ⁡ [a 0 + 1, a 1, …, a n]. P_{n}=A_{n}+B_{n}=K[a_{0}+1,a_{1},\ldots,a_{n}]. |  | (15) |

The following holds:

###### Theorem 5.3.

Let w = a ​ u ​ b w=aub be a proper Christoffel word with u = ψ ⁡ ( v) u=\psi(v) and ( α 0, α 1, …, α n) (\alpha_{0},\alpha_{1},\ldots,\alpha_{n}), n ≥ 0 n\geq 0, be the integral representation of v v. Then

 | | w | = K ⁡ [α 0 + 1, α 1, …, α n − 1, α n + 1]. |w|=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{n-1},\alpha_{n}+1]. |  |

We remark that for n = 0 n=0 the preceding formula becomes K ⁡ [α 0 + 1, 1] = K ⁡ [α 0 + 2] K[\alpha_{0}+1,1]=K[\alpha_{0}+2].

###### Proof.

By Theorem 5.1, the slope | w | b | w | a \frac{|w|_{b}}{|w|_{a}} of w w is given by the continued fraction [α 0; α 1, …, α n − 1, α n + 1]. [\alpha_{0};\alpha_{1},\ldots,\alpha_{n-1},\alpha_{n}+1]. Since the n n -th order convergent C n ′ = A n ′ B n ′ = | w | b | w | a C^{\prime}_{n}=\frac{A^{\prime}_{n}}{B^{\prime}_{n}}=\frac{|w|_{b}}{|w|_{a}} and gcd ⁡ ( | w | a, | w | b) = 1 \gcd(|w|_{a},|w|_{b})=1, one has P n ′ = A n ′ + B n ′ = | w | b + | ​ w | a = | w | P^{\prime}_{n}=A^{\prime}_{n}+B^{\prime}_{n}=|w|_{b}+|w|_{a}=|w|. Then the result follows from ( 15). ∎

Theorem 4.1 and Corollary 4.3 can be restated equivalently in terms of continuants as follows:

###### Theorem 5.4.

Let n ≥ 0 n\geq 0 and α 0, α 1, …, α m \alpha_{0},\alpha_{1},\ldots,\alpha_{m} be any sequence of integers such that

 | α 0 ≥ 0, α i > 0, i = 1, …, m, and ∑ i = 0 m α i = n. \alpha_{0}\geq 0,\ \alpha_{i}>0,\ i=1,\ldots,m,\ \ \mbox{and}\ \ \sum_{i=0}^{m}\alpha_{i}=n. |  |

Then

 | K ⁡ [α 0 + 1, α 1, …, α m − 1, α m + 1] ≤ K ⁡ [1 n, 2] = K ⁡ [2, 1 n] = F n + 1, K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1},\alpha_{m}+1]\leq K[1^{n},2]=K[2,1^{n}]=F_{n+1}, |  | (16) |

where the equality occurs if and only if m = n m=n and α 0 = 0, α 1 = α 2 = ⋯ = α n = 1 \alpha_{0}=0,\alpha_{1}=\alpha_{2}=\cdots=\alpha_{n}=1 or m = n − 1 m=n-1 and α 0 = α 1 = α 2 = ⋯ = α n − 1 = 1 \alpha_{0}=\alpha_{1}=\alpha_{2}=\cdots=\alpha_{n-1}=1.

###### Proof.

Let v v be any word of 𝒜 n {\cal A}^{n} having the integral representation v ≡ ( α 0, α 1, …, α m) v\equiv(\alpha_{0},\alpha_{1},\ldots,\alpha_{m}) such that n = ∑ i = 0 m α i n=\sum_{i=0}^{m}\alpha_{i}. By Theorem 4.1 and Corollary 4.3 one has

 | | ψ ⁡ ( v) | ≤ | ψ ⁡ ( v ( n)) | = F n + 1 − 2, |\psi(v)|\leq|\psi(v^{(n)})|=F_{n+1}-2, |  |

so that | a ​ ψ ​ ( v) ​ b | ≤ F n + 1 |a\psi(v)b|\leq F_{n+1}. Thus, by Theorem 5.3 one derives

 | | a ​ ψ ​ ( v) ​ b | = K ⁡ [α 0 + 1, α 1, …, α m − 1, α m + 1] ≤ F n + 1 = K ⁡ [1 n, 2] = K ⁡ [2, 1 n]. |a\psi(v)b|=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1},\alpha_{m}+1]\leq F_{n+1}=K[1^{n},2]=K[2,1^{n}]. |  |

By Corollary 4.3 the equality occurs if and only if v = v ( n) v=v^{(n)} or v = E ⁡ ( v ( n)) v=E(v^{(n)}). In the first case m = n m=n and α 0 = 0, α 1 = α 2 = ⋯ = α n = 1 \alpha_{0}=0,\alpha_{1}=\alpha_{2}=\cdots=\alpha_{n}=1. In the second case m = n − 1 m=n-1, and α 0 = α 1 = α 2 = ⋯ = α n − 1 = 1 \alpha_{0}=\alpha_{1}=\alpha_{2}=\cdots=\alpha_{n-1}=1. Hence, the theorem is proved. ∎

Let us observe that the preceding theorem implies the validity of Theorem 4.1 and Corollary 4.3. Indeed, let v v be any word over 𝒜 {\cal A} having the integral representation v ≡ ( α 0, α 1, …, α m) v\equiv(\alpha_{0},\alpha_{1},\ldots,\alpha_{m}) and length n = ∑ i = 0 m α i n=\sum_{i=0}^{m}\alpha_{i}. From ( 16) and Theorem 5.3 one derives | ψ ⁡ ( v) | ≤ | ψ ⁡ ( v ( n)) | = F n + 1 − 2, |\psi(v)|\leq|\psi(v^{(n)})|=F_{n+1}-2, where the equality holds if and only if v = v ( n) v=v^{(n)} or v = E ⁡ ( v ( n)) v=E(v^{(n)}).

We shall give now a direct proof of Theorem 5.4 without using combinatorics on words. We need the following lemma on Fibonacci numbers.

###### Lemma 5.5.

Let n ≥ 1 n\geq 1. For any integer x x such that 0 < x ≤ n 0<x\leq n, one has:

 | x ​ F n − x + F n − x + 1 ≤ F n + 1, xF_{n-x}+F_{n-x+1}\leq F_{n+1}, |  |

where the equality holds if and only if x = 1 x=1.

###### Proof.

The proof is by induction on the value of x ≤ n x\leq n. For x = 1 x=1 one has F n − 1 + F n = F n + 1 F_{n-1}+F_{n}=F_{n+1}. For x = 2 ≤ n x=2\leq n one has 2 ​ F n − 2 + F n − 1 = F n − 2 + F n − 2 + F n − 1 = F n − 2 + F n < F n − 1 + F n = F n + 1 2F_{n-2}+F_{n-1}=F_{n-2}+F_{n-2}+F_{n-1}=F_{n-2}+F_{n}<F_{n-1}+F_{n}=F_{n+1}. Suppose the statement true up to 1 < x − 1 < n 1<x-1<n and prove it for x x. One has by using the inductive hypothesis,

 | x ​ F n − x + F n − x + 1 = ( x − 1) ​ F n − x + F n − x + F n − x + 1 = ( x − 1) ​ F n − x + F n − x + 2 xF_{n-x}+F_{n-x+1}=(x-1)F_{n-x}+F_{n-x}+F_{n-x+1}=(x-1)F_{n-x}+F_{n-x+2} |  |

 | < ( x − 1) ​ F n − x + 1 + F n − x + 2 < F n + 1. ∎ <(x-1)F_{n-x+1}+F_{n-x+2}<F_{n+1}.\qed |  |

(Second proof of Theorem 5.4). The proof is by induction on the integer n n. The result is trivial if n ≤ 1 n\leq 1. Let us suppose the result true for all integers less than n > 1 n>1 and prove it for n n. Let α 0, α 1, …, α m \alpha_{0},\alpha_{1},\ldots,\alpha_{m} be any sequence of integers such that α 0 ≥ 0, α i > 0, i = 1, …, m, and ∑ i = 0 m α i = n \alpha_{0}\geq 0,\ \alpha_{i}>0,\ i=1,\ldots,m,\ \ \mbox{and}\ \ \sum_{i=0}^{m}\alpha_{i}=n. From the definition of continuant one has:

 | K ⁡ [α 0 + 1, α 1, …, α m − 1, α m + 1] = ( α m + 1) ​ K ​ [α 0 + 1, α 1, …, α m − 1] K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1},\alpha_{m}+1]=(\alpha_{m}+1)K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1}] |  |

 | + K ⁡ [α 0 + 1, α 1, …, α m − 2]. +K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}]. |  |

By induction one derives:

 | K ⁡ [α 0 + 1, α 1, …, α m − 1] ≤ F n − α m. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1}]\leq F_{n-\alpha_{m}}. |  | (17) |

Indeed, if α m − 1 > 1 \alpha_{m-1}>1 one has

 | K ⁡ [α 0 + 1, α 1, …, α m − 1] = K ⁡ [α 0 + 1, α 1, …, α m − 2, ( α m − 1 − 1) + 1]. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1}]=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2},(\alpha_{m-1}-1)+1]. |  |

Since, ∑ i = 0 m − 2 α i + ( α m − 1 − 1) = n − α m − 1 \sum_{i=0}^{m-2}\alpha_{i}+(\alpha_{m-1}-1)=n-\alpha_{m}-1, equation ( 17) follows by induction. If α m − 1 = 1 \alpha_{m-1}=1, by ( 13), one has

 | K ⁡ [α 0 + 1, α 1, …, α m − 2, 1] = K ⁡ [α 0 + 1, α 1, …, α m − 2 + 1]. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2},1]=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}+1]. |  |

Since ∑ i = 0 m − 2 α i = n − α m − 1 \sum_{i=0}^{m-2}\alpha_{i}=n-\alpha_{m}-1, equation ( 17) follows again by induction. In a similar way one derives by induction

 | K ⁡ [α 0 + 1, α 1, …, α m − 2] ≤ F n − α m − α m − 1. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}]\leq F_{n-\alpha_{m}-\alpha_{m-1}}. |  | (18) |

Thus, since α m − 1 ≥ 1 \alpha_{m-1}\geq 1, one has:

 | K ⁡ [α 0 + 1, α 1, …, α m − 1, α m + 1] ≤ ( α m + 1) ​ F n − α m + F n − α m − α m − 1 K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1},\alpha_{m}+1]\leq(\alpha_{m}+1)F_{n-\alpha_{m}}+F_{n-\alpha_{m}-\alpha_{m-1}} |  |

 | = α m ​ F n − α m + F n − α m + F n − α m − α m − 1 ≤ α m ​ F n − α m + F n − α m + 1, =\alpha_{m}F_{n-\alpha_{m}}+F_{n-\alpha_{m}}+F_{n-\alpha_{m}-\alpha_{m-1}}\leq\alpha_{m}F_{n-\alpha_{m}}+F_{n-\alpha_{m}+1}, |  |

where in the last inequality the equality sign occurs if and only if α m − 1 = 1 \alpha_{m-1}=1. By Lemma 5.5, α m ​ F n − α m + F n − α m + 1 ≤ F n + 1 \alpha_{m}F_{n-\alpha_{m}}+F_{n-\alpha_{m}+1}\leq F_{n+1}, where the equality holds if and only if α m = 1 \alpha_{m}=1. Thus in any case

 | K ⁡ [α 0 + 1, α 1, …, α m − 1, α m + 1] ≤ F n + 1. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1},\alpha_{m}+1]\leq F_{n+1}. |  |

The equality can occur in the preceding equation if and only if α m = α m − 1 = 1 \alpha_{m}=\alpha_{m-1}=1 and, moreover, in view of ( 17) and ( 18),

 | K ⁡ [α 0 + 1, α 1, …, α m − 2 + 1] = F n − 1 ​ and ​ K ​ [α 0 + 1, α 1, …, α m − 2] = F n − 2. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}+1]=F_{n-1}\ \mbox{and}\ K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}]=F_{n-2}. |  |

Since ∑ i = 0 m − 2 α i = n − 2 \sum_{i=0}^{m-2}\alpha_{i}=n-2, by induction the first of the two preceding equations is satisfied if and only if α 0 = 0 \alpha_{0}=0, m = n m=n, and α 1 = ⋯ = α n − 2 = 1 \alpha_{1}=\cdots=\alpha_{n-2}=1 or α 0 = 1 \alpha_{0}=1, m = n − 1 m=n-1, and α 1 = ⋯ = α n − 3 = 1 \alpha_{1}=\cdots=\alpha_{n-3}=1. In the first case α m − 1 = α n − 1 = α n = α m = 1 \alpha_{m-1}=\alpha_{n-1}=\alpha_{n}=\alpha_{m}=1, and in the second case, α m − 1 = α n − 2 = α m = α n − 1 = 1 \alpha_{m-1}=\alpha_{n-2}=\alpha_{m}=\alpha_{n-1}=1. Since for the previous values of α \alpha ’s the second equation is certainly satisfied, the result follows. □ \Box

###### Proposition 5.6.

Let v ∈ 𝒜 ∗ v\in{\cal A}^{*} be a word having the integral representation v = ( α 0, α 1, …, α n) v=(\alpha_{0},\alpha_{1},\ldots,\alpha_{n}). Then

 | π ⁡ ( ψ ⁡ ( v)) = K ⁡ [α 0 + 1, α 1, …, α n − 1]. \pi(\psi(v))=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{n-1}]. |  |

###### Proof.

It has been proved in [10] (see also [1, 6]) that if v v has the integral representation v = ( α 0, α 1, …, α n) v=(\alpha_{0},\alpha_{1},\ldots,\alpha_{n}), then

 | [0; α n, α n − 1, …, α 1, α 0 + 1] = π ⁡ ( ψ ⁡ ( v)) q, [0;\alpha_{n},\alpha_{n-1},\ldots,\alpha_{1},\alpha_{0}+1]=\frac{\pi(\psi(v))}{q}, |  |

where π ⁡ ( ψ ⁡ ( v)) \pi(\psi(v)) is the minimal period of ψ ⁡ ( v) \psi(v) and q q is the period of ψ ⁡ ( v) \psi(v) such that gcd ⁡ ( q, π ⁡ ( ψ ⁡ ( v))) = 1 \gcd(q,\pi(\psi(v)))=1 and | ψ ⁡ ( v) | = π ⁡ ( ψ ⁡ ( v)) + q − 2 |\psi(v)|=\pi(\psi(v))+q-2. By ( 14) one has:

 | [0; α n, α n − 1, …, α 1, α 0 + 1] = K ⁡ [0, α n, …, α 1, α 0 + 1] K ⁡ [α n, …, α 1, α 0 + 1]. [0;\alpha_{n},\alpha_{n-1},\ldots,\alpha_{1},\alpha_{0}+1]=\frac{K[0,\alpha_{n},\ldots,\alpha_{1},\alpha_{0}+1]}{K[\alpha_{n},\ldots,\alpha_{1},\alpha_{0}+1]}. |  |

Since the preceding fraction is irreducible, by ( 12) and ( 11) one derives:

 | π ⁡ ( ψ ⁡ ( v)) = K ⁡ [0, α n, …, α 1, α 0 + 1] = K ⁡ [α 0 + 1, α 1, …, α n − 1, α n, 0] \pi(\psi(v))=K[0,\alpha_{n},\ldots,\alpha_{1},\alpha_{0}+1]=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{n-1},\alpha_{n},0] |  |

 | = K ⁡ [α 0 + 1, α 1, …, α n − 1], =K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{n-1}], |  |

which concludes the proof. ∎

By the preceding proposition and the extremal property of continuants expressed by Theorem 5.4, we can give a different proof of Theorem 4.5. Indeed, the following proposition holds:

###### Proposition 5.7.

Let n ≥ 0 n\geq 0 and α 0, α 1, …, α m \alpha_{0},\alpha_{1},\ldots,\alpha_{m} be any sequence of integers such that

 | α 0 ≥ 0, α i > 0, i = 1, …, m, and ∑ i = 0 m α i = n. \alpha_{0}\geq 0,\ \alpha_{i}>0,\ i=1,\ldots,m,\ \ \mbox{and}\ \ \sum_{i=0}^{m}\alpha_{i}=n. |  |

One has that

 | K ⁡ [α 0 + 1, α 1, …, α m − 1] ≤ F n − 1. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1}]\leq F_{n-1}. |  | (19) |

The equality is reached if and only if one of the following conditions is satisfied:

1) α 0 = 0 \alpha_{0}=0, m = n m=n, and α 1 = α 2 = ⋯ = α n − 1 = α n = 1 \alpha_{1}=\alpha_{2}=\cdots=\alpha_{n-1}=\alpha_{n}=1,

2) α 0 = 0 \alpha_{0}=0, m = n − 1 m=n-1, and α i = 1 \alpha_{i}=1 for 1 ≤ i ≤ n − 3 1\leq i\leq n-3, α n − 2 = 2 \alpha_{n-2}=2, α n − 1 = 1 \alpha_{n-1}=1,

3) α 0 = 1 \alpha_{0}=1, m = n − 1 m=n-1, and α 1 = α 2 = ⋯ = α n − 1 = 1 \alpha_{1}=\alpha_{2}=\cdots=\alpha_{n-1}=1,

4) α 0 = 1 \alpha_{0}=1, m = n − 2 m=n-2, and α i = 1 \alpha_{i}=1 for 1 ≤ i ≤ n − 4 1\leq i\leq n-4, α n − 3 = 2 \alpha_{n-3}=2, α n − 2 = 1 \alpha_{n-2}=1.

###### Proof.

We have to consider two cases. If α m − 1 = 1 \alpha_{m-1}=1, since

 | K ⁡ [α 0 + 1, α 1, …, α m − 2, 1] = K ⁡ [α 0 + 1, α 1, …, α m − 2 + 1], K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2},1]=K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}+1], |  |

one has

 | K ⁡ [α 0 + 1, α 1, …, α m − 2 + 1] ≤ F n − α m ≤ F n − 1. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2}+1]\leq F_{n-\alpha_{m}}\leq F_{n-1}. |  | (20) |

Indeed, since ∑ i = 0 m − 2 α i = n − 1 − α m \sum_{i=0}^{m-2}\alpha_{i}=n-1-\alpha_{m}, the preceding formula follows from Theorem 5.4. If α m − 1 > 1 \alpha_{m-1}>1, one derives:

 | K ⁡ [α 0 + 1, α 1, …, α m − 2, ( α m − 1 − 1) + 1] ≤ F n − α m ≤ F n − 1. K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-2},(\alpha_{m-1}-1)+1]\leq F_{n-\alpha_{m}}\leq F_{n-1}. |  | (21) |

Indeed, since ∑ i = 0 m − 2 α i + α m − 1 − 1 = n − 1 − α m \sum_{i=0}^{m-2}\alpha_{i}+\alpha_{m-1}-1=n-1-\alpha_{m}, the previous inequality follows again from Theorem 5.4. Thus in any case ( 19) is satisfied.

The maximal value of K ⁡ [α 0 + 1, α 1, …, α m − 1] K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1}] is then F n − 1 F_{n-1}. It is reached if and only if one of the conditions 1), 2), 3), 1),2),3), and OPEN 4) 4) is satisfied. The sufficiency of the preceding conditions is readily verified. Let us prove the necessity.

Indeed, necessarily α m = 1 \alpha_{m}=1. Moreover, by Theorem 5.4, if K ⁡ [α 0 + 1, α 1, …, α m − 1] = F n − 1 K[\alpha_{0}+1,\alpha_{1},\ldots,\alpha_{m-1}]=F_{n-1}, then α 0 = 0 \alpha_{0}=0 or α 0 = 1 \alpha_{0}=1. We consider only the case α 0 = 0 \alpha_{0}=0; the case α 0 = 1 \alpha_{0}=1 is similarly dealt with.

If α m − 1 = 1 \alpha_{m-1}=1, in view of ( 20), one derives by Theorem 5.4, that m = n m=n and α 1 = α 2 = ⋯ = α n − 2 = 1 \alpha_{1}=\alpha_{2}=\cdots=\alpha_{n-2}=1. Since α m − 1 = α n − 1 = α m = α n = 1 \alpha_{m-1}=\alpha_{n-1}=\alpha_{m}=\alpha_{n}=1, condition 1) is satisfied.

If α m − 1 > 1 \alpha_{m-1}>1, in view of ( 21), one derives by Theorem 5.4, that m = n − 1 m=n-1 and α 1 = α 2 = ⋯ = α m − 2 = α m − 1 − 1 = 1 \alpha_{1}=\alpha_{2}=\cdots=\alpha_{m-2}=\alpha_{m-1}-1=1. Thus α m − 1 = α n − 2 = 2 \alpha_{m-1}=\alpha_{n-2}=2. Hence, since α m = α n − 1 = 1 \alpha_{m}=\alpha_{n-1}=1, condition 2) is satisfied. ∎

By Propositions 5.6 and 5.7, one easily derives Theorem 4.5 of the previous section.

## References

- [1] J. Berstel, A. de Luca, Sturmian words, Lyndon words and trees, *Theoret. Comput. Sci.*178 (1997) 171–203
- [2] J. Berstel, A. Lauve, C. Reutenauer, F.V. Saliola, Combinatorics on Words, Christoffel Words and Repetitions in Words, CRM Monograph series, vol. 27, American Mathematical Society, (Providence, RI, 2009)
- [3] V. Berthé, A. de Luca, C. Reutenauer, On an involution of Christoffel words and Sturmian morphisms, European J. Combin. 29 (2008) 535–553
- [4] J.-P. Borel, F. Laubie, Quelques mots sur la droite projective réelle, Journal de Théorie des Nombres de Bordeaux 5 (1993) 23–52
- [5] A. Carpi, A. de Luca, Special factors, Periodicity, and an Application to Sturmian words, Acta Informatica 36 (2000) 983–1006
- [6] A. Carpi, A. de Luca, Harmonic and gold Sturmian words, European J. Combin. 25 (2004) 685–705
- [7] J. Cassaigne, On extremal properties of the Fibonacci word, Theor. Inform. Appl. 42 (2008) 701–715
- [8] E.B. Christoffel, Observatio arithmetica, Annali di Matematica Pura e Applicata 6 (1875) 148–152
- [9] A. de Luca, A combinatorial property of the Fibonacci words, Information Processing Letters 12 (1981) 193–195
- [10] A. de Luca, Sturmian words: Structure, Combinatorics, and their Arithmetics, *Theoret. Comput. Sci.*183 (1997) 45–82
- [11] A. de Luca, A standard correspondence on epicentral words, European J. Combin. 33 (2012) 1514–1536
- [12] A. de Luca, A. De Luca, Pseudopalindrome closure operators in free monoids, *Theoret. Comput. Sci.*362 (2006) 282–300
- [13] A. de Luca, A. De Luca, A generalized palindromization map in free monoids, *Theoret. Comput. Sci.*(2012), doi:10.1016/j.tcs.2012.01.029
- [14] A. de Luca, F. Mignosi, Some combinatorial properties of Sturmian words, *Theoret. Comput. Sci.*136 (1994) 361–385
- [15] A. de Luca, L. Q. Zamboni, Involutions of epicentral words, *European J. Combin.*31 (2010) 867–886
- [16] X. Droubay, J. Justin, G. Pirillo, Episturmian words and some constructions of de Luca and Rauzy, *Theoret. Comput. Sci.*255 (2001) 539–553
- [17] N. J. Fine, H.S. Wilf, Uniqueness theorem for periodic functions, Proc. Amer. Math. Soc. 16 (1965) 109–114
- [18] R.L. Graham, D.E. Knuth, O. Patashnik, Concrete Mathematics, 2-nd edition, Addison-Wesley (Reading Mass., 1994)
- [19] J. Justin, Episturmian morphisms and a Galois theorem on continued fractions, *Theor. Inform. Appl.*39 (2005) 207–215
- [20] C. Kassel, C. Reutenauer, A palindromization map for the free group, *Theoret. Comput. Sci.*409 (2008) 461–470
- [21] A. Ya. Khinchin, Continued fractions, The University of Chicago Press, (Chicago Ill., 1964)
- [22] M. Lothaire, *Combinatorics on Words*, Addison-Wesley (Reading, MA, 1983)
- [23] M. Lothaire, *Algebraic Combinatorics on Words*, Encyclopedia of Mathematics and its Applications, vol. 90, Cambridge University Press (Cambridge, 2002)
- [24] E. Lucas, Théorie des nombres, Gauthier-Villars (Paris, 1891)
- [25] F. Mignosi, A. Restivo, S. Salemi, Periodicity and golden ratio, Theoret. Comput. Sci. 204 (1998) 199–204

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1209.3926
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1209.3927
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1209.3927
[7]: https://arxiv.org/pdf/1209.3927
[8]: /html/1209.3928
