<!-- source: https://ar5iv.labs.arxiv.org/html/0801.1655 | converted from HTML -->

[0801.1655] EPISTURMIAN WORDS: A SURVEY

# EPISTURMIAN WORDS: A SURVEY This paper grew out of an invited lecture given by the second author at the Sixth International Conference on Words, Marseille, France, September 17–21, 2007.

Amy Glen 2 2 2 Corresponding author: LaCIM, Université du Québec à Montréal, C.P. 8888, succursale Centre-ville, Montréal, Québec, H3C 3P8, CANADA \ \backslash The Mathematics Institute, Reykjavik University, Kringlan 1, IS-103 Reykjavik, ICELAND ( amy.glen@gmail.com). Jacques Justin 3 3 3 LIAFA, Université Paris Diderot - Paris 7, Case 7014, 75205 Paris Cedex 13, FRANCE ( jacjustin@free.fr).

Submitted: December 11, 2007; Revised: September 16, 2008

###### Abstract

In this paper, we survey the rich theory of infinite episturmian words which generalize to any finite alphabet, in a rather resembling way, the well-known family of Sturmian words on two letters. After recalling definitions and basic properties, we consider episturmian morphisms that allow for a deeper study of these words. Some properties of factors are described, including factor complexity, palindromes, fractional powers, frequencies, and return words. We also consider lexicographical properties of episturmian words, as well as their connection to the balance property, and related notions such as finite episturmian words, Arnoux-Rauzy sequences, and “episkew words” that generalize the skew words of Morse and Hedlund.

Keywords: combinatorics on words; episturmian words; Arnoux-Rauzy sequences; Sturmian words; episturmian morphisms.

MSC (2000): 68R15.

## 1 Introduction

### 1.1 From Sturmian to episturmian

Most renowned amongst the branches of combinatorics on words is the theory of infinite binary sequences called *Sturmian words*, which are fascinating in many respects, having been studied from combinatorial, algebraic, and geometric points of view. Their beautiful properties are related to many fields such as Number Theory, Geometry, Symbolic Dynamical Systems, Theoretical Physics, and Theoretical Computer Science (see [7, 83, 96] for recent surveys).

Since the seminal works of Morse and Hedlund [91], Sturmian words have been shown to admit numerous equivalent definitions and characterizations. For instance, it is well known that an infinite word 𝐰 \mathbf{w} over { a, b } \{a,b\} is Sturmian if and only if 𝐰 \mathbf{w} is aperiodic and balanced: for any two factors u u, v v of 𝐰 \mathbf{w} of the same length, the number of a a ’s in each of u u and v v differs by at most 1 1. Sturmian words are also characterized by their factor complexity function (which counts the number of distinct factors of each length): they have exactly n + 1 n+1 distinct factors of length n n for each n n. In this sense, Sturmian words are precisely the aperiodic infinite words of minimal factor complexity since, as is well known, an infinite word is ultimately periodic if and only if it has less than n + 1 n+1 factors of length n n for some n n (see [37]). Many interesting properties of Sturmian words can be attributed to their low complexity, which induces certain regularities in such words without, however, making them periodic. Sturmian words can also be geometrically realized as cutting sequences by considering the sequence of ‘cuts’ in an integer grid made by a line of irrational slope (see for instance [38, 13]). They also provide a symbolic coding of the orbit of a point on a circle with respect to a rotation by an irrational number (see [91, 4]).

All of the above characteristic properties of Sturmian words lead to natural generalizations on arbitrary finite alphabets. In one direction, the balance property naturally extends to an alphabet with more than two letters (e.g., see [68, 110, 115]) as does the following generalized balance property that also characterizes Sturmian words (see [49, 1]): the difference between the number of occurrences of a word u u in any pair of factors of the same length is at most 1 1. In another direction, we could consider relaxing the minimality condition for the factor complexity p ⁡ ( n) p(n). For example, quasi-Sturmian words are infinite words for which there exist two positive integers N N and c c such that n + 1 ≤ p ⁡ ( n) ≤ n + c n+1\leq p(n)\leq n+c for all n ≥ N n\geq N. This generalization was introduced in [5] when studying the transcendence of certain continued fraction expansions. See also [31, 36, 66, 105] for similar extensions of Sturmian words with respect to factor complexity. From the geometric point of view, cutting sequences naturally generalize to trajectories in the hypercube billiard (e.g., see [25]), and codings of rotational orbits carry over to codings of interval exchange transformations (e.g., see [18]).

Two other very interesting natural generalizations of Sturmian words are Arnoux-Rauzy sequences [12, 97] and episturmian words [43, 73], which we will now define.

From the factor complexity of Sturmian words, it immediately follows that any Sturmian word is over a 2 2 -letter alphabet and has exactly one left special factor of each length. A factor u u of a finite or infinite word w w is said to be left special (resp. right special) in w w if there exists at least two distinct letters a a, b b such that a ​ u au and b ​ u bu (resp. u ​ a ua, u ​ b ub) are factors of w w. Extending the left special property of Sturmian words, a recurrent infinite word 𝐰 \mathbf{w} over a finite alphabet 𝒜 \mathcal{A} is said to be an Arnoux-Rauzy sequence (or a strict episturmian word) if it has exactly one left special factor and one right special factor of each length, and for every left (resp. right) special factor u u of 𝐰 \mathbf{w}, x ​ u xu (resp. u ​ x ux) is a factor of 𝐰 \mathbf{w} for all letters x ∈ 𝒜 x\in\mathcal{A}. A noteable property that is shared by Sturmian words and Arnouxy-Rauzy sequences is their closure under reversal, i.e., if u u is a factor of such a word, then its reversal is also a factor. This nice property inspired Droubay, Justin, and Pirillo’s generalization of Sturmian words in [43]: an infinite word is episturmian if it is closed under reversal and has at most one left special factor of each length. Sturmian, Arnoux-Rauzy, and episturmian words all have standard (or characteristic) elements, which are those having all of their left special factors as prefixes. Within these families of words, standard words are good representatives in the sense that an infinite word belongs to one such family if and only if it has the same set of factors as some standard word in that family.

From the definitions, it is clear that the family of Arnoux-Rauzy sequences is a particular subclass of the family of episturmian words. More precisely, episturmian words are composed of the Arnoux-Rauzy sequences, images of the Arnoux-Rauzy sequences by episturmian morphisms, and certain periodic infinite words (see Section 5). In the 2 2 -letter case, Arnoux-Rauzy sequences are exactly the Sturmian words whereas episturmian words include all recurrent balanced words, i.e., periodic balanced words and Sturmian words.

The study of episturmian words and Arnoux-Rauzy sequences has enjoyed a great deal of popularity in recent times, owing mostly to the many properties that they share with Sturmian words. In this paper we survey the purely combinatorial work on episturmian words, beginning with their definition and basic properties in Section 2. Then, in Section 3, we recall episturmian morphisms which allow for a deeper study of episturmian words. In particular, any episturmian word is the image of another episturmian word by some so-called pure episturmian morphism. Even more, any episturmian word can be infinitely decomposed over the set of pure episturmian morphisms. This last property allows an episturmian word to be defined by one of its morphic decompositions or, equivalently, by a certain directive word, which is an infinite sequence of rules for decomposing the given episturmian word by morphisms. In Section 4 we consider notions such as shifts, spins, and block-equivalence in connection with directive words, which allow us to study when two different spinned infinite words direct the same episturmian word. We also consider periodic and purely morphic episturmian words. In Section 5, our discussion briefly turns to Arnoux-Rauzy sequences and finite episturmian words. Following this, we study in Section 6 some properties of factors of episturmian words (and Arnoux-Rauzy sequences), including factor complexity, palindromes, fractional powers, frequencies, and return words. Lastly, we consider more recent work involving lexicographic order and the balance property (including Fraenkel’s conjecture).

### 1.2 Notation & terminology

We assume the reader is familiar with combinatorics on words and morphisms (e.g., see [82, 83]). In this section, we recall some basic definitions and properties relating to episturmian words which are needed throughout the paper. For the most part, we follow the notation and terminology of [43, 73, 75, 62].

Let 𝒜 \mathcal{A} denote a finite alphabet, i.e., a non-empty finite set of symbols called letters. A finite *word*over 𝒜 \mathcal{A} is a finite sequence of letters from 𝒜 \mathcal{A}. The empty word ε \varepsilon is the empty sequence. Under the operation of concatenation, the set 𝒜 ∗ \mathcal{A}^{*} of all finite words over 𝒜 \mathcal{A} is a free monoid with identity element ε \varepsilon and set of generators 𝒜 \mathcal{A}. The set of non-empty words over 𝒜 \mathcal{A} is the free semigroup 𝒜 +:= 𝒜 ∗ ∖ { ε } \mathcal{A}^{+}:=\mathcal{A}^{*}\setminus\{\varepsilon\}.

A right-infinite (resp. left-infinite, bi-infinite) word over 𝒜 \mathcal{A} is a sequence indexed by ℕ + \mathbb{N}^{+} (resp. ℤ ∖ ℕ + \mathbb{Z}\setminus\mathbb{N}^{+}, ℤ \mathbb{Z}) with values in 𝒜 \mathcal{A}. For instance, a left-infinite word is represented by 𝐮 = ⋯ b − 2 b − 1 b 0 \mathbf{u}=\cdots b_{-2}b_{-1}b_{0} and a right-infinite word by 𝐯 = b 1 b 2 b 3 ⋯ \mathbf{v}=b_{1}b_{2}b_{3}\cdots where b i ∈ 𝒜 b_{i}\in\mathcal{A}. The concatenation of 𝐮 \mathbf{u} and 𝐯 \mathbf{v} gives the bi-infinite word 𝐮. 𝐯 = ⋯ b − 2 b − 1 b 0. b 1 b 2 b 3 ⋯ \mathbf{u}.\mathbf{v}=\cdots b_{-2}b_{-1}b_{0}.b_{1}b_{2}b_{3}\cdots with a dot written between b 0 b_{0} and b 1 b_{1} to avoid ambiguity. For easier reading, infinite words are hereafter typically typed in boldface to distinguish them from finite words.

The shift map T \mathrm{T} is defined for bi-infinite words 𝐛 = ( b i) i ∈ ℤ \mathbf{b}=(b_{i})_{i\in\mathbb{Z}} by T ⁡ ( 𝐛) = ( b i + 1) i ∈ ℤ \mathrm{T}(\mathbf{b})=(b_{i+1})_{i\in\mathbb{Z}} and its k k -th iteration is denoted by T k \mathrm{T}^{k}. This extends to right-infinite words for k ≥ 0 k\geq 0 and left-infinite words for k ≤ 0 k\leq 0. For finite words w ∈ 𝒜 ∗ w\in\mathcal{A}^{*}, the shift map T \mathrm{T} acts circularly, i.e., if w = x ​ v w=xv where x ∈ 𝒜 x\in\mathcal{A}, then T ⁡ ( w) = v ​ x \mathrm{T}(w)=vx.

The set of all right-infinite words over 𝒜 \mathcal{A} is denoted by 𝒜 ω \mathcal{A}^{\omega}, and we define 𝒜 ∞:= 𝒜 ∗ ∪ 𝒜 ω \mathcal{A}^{\infty}:=\mathcal{A}^{*}\cup\mathcal{A}^{\omega}. An ultimately periodic right-infinite word can be written as u v ω = u v v v ⋯ uv^{\omega}=uvvv\cdots, for some u u, v ∈ 𝒜 ∗ v\in\mathcal{A}^{*}, v ≠ ε v\neq\varepsilon. If u = ε u=\varepsilon, then such a word is periodic. A right-infinite word that is not ultimately periodic is said to be aperiodic.

Given a finite word w = x 1 x 2 ⋯ x m ∈ 𝒜 ∗ w=x_{1}x_{2}\cdots x_{m}\in\mathcal{A}^{*} with each x i ∈ 𝒜 x_{i}\in\mathcal{A}, the *length*of w w, denoted by | w | |w|, is equal to m m. By convention, the empty word ε \varepsilon is the unique word of length 0 0. The number of occurrences of a letter a a in w w is denoted by | w | a |w|_{a}. If | w | a = 0 |w|_{a}=0, then w w is said to be a a -free. The *reversal*w ~ \widetilde{w} of w w is its mirror image: w ~ = x m x m − 1 ⋯ x 1 \widetilde{w}=x_{m}x_{m-1}\cdots x_{1}, and if w = w ~ w=\widetilde{w}, then w w is called a *palindrome*. The reversal operator naturally extends to bi-infinite words; that is, the reversal of the bi-infinite word 𝐛 = 𝐥. 𝐫 \mathbf{b}=\mathbf{l}.\mathbf{r}, with 𝐥 \mathbf{l} left-infinite and 𝐫 \mathbf{r} right-infinite, is given by 𝐛 ~ = 𝐫 ~. 𝐥 ~ \widetilde{\mathbf{b}}=\widetilde{\mathbf{r}}.\widetilde{\mathbf{l}}.

A finite word w w is a *factor*of a finite or infinite word z z if z = u ​ w ​ v z=uwv for some words u u, v v (which are finite or infinite depending on z z). In the special case u = ε u=\varepsilon (resp. v = ε v=\varepsilon), we call w w a *prefix*(resp. *suffix*) of z z. We use the notation p − 1 ​ w p^{-1}w (resp. w ​ s − 1 ws^{-1}) to indicate the removal of a prefix p p (resp. suffix s s) of a finite word w w. Note that a prefix or suffix u u of a finite word w w is said to be proper if u ≠ w u\neq w. A factor u u of a finite or infinite word w w is *right*(resp. *left*) *special*if u ​ a ua, u ​ b ub (resp. a ​ u au, b ​ u bu) are factors of w w for some letters a a, b ∈ 𝒜 b\in\mathcal{A}, a ≠ b a\neq b.

For any finite or infinite word w w, F ⁡ ( w) F(w) denotes the set of all its factors. Moreover, the *alphabet*of w w is Alph ( w):= F ⁡ ( w) ∩ 𝒜 (w):=F(w)\cap\mathcal{A} and, if w w is infinite, we denote by Ult ( w) (w) the set of all letters occurring infinitely often in w w. Any two infinite words 𝐱 \mathbf{x}, 𝐲 \mathbf{y} are said to be *factor-equivalent*if F ⁡ ( 𝐱) = F ⁡ ( 𝐲) F(\mathbf{x})=F(\mathbf{y}), i.e., if 𝐱 \mathbf{x} and 𝐲 \mathbf{y} have the same set of factors.

A factor of an infinite word 𝐱 \mathbf{x} is *recurrent*in 𝐱 \mathbf{x} if it occurs infinitely often in 𝐱 \mathbf{x}, and 𝐱 \mathbf{x} itself is said to be *recurrent*if all of its factors are recurrent in it. For a bi-infinite word to be recurrent, any factor must occur infinitely often to the left and to the right. An infinite word is said to be *uniformly recurrent*if any factor occurs infinitely many times in it with bounded gaps [37].

A morphism φ \varphi on 𝒜 \mathcal{A} is a map from 𝒜 ∗ \mathcal{A}^{*} to 𝒜 ∗ \mathcal{A}^{*} such that φ ⁡ ( u ​ v) = φ ⁡ ( u) ​ φ ​ ( v) \varphi(uv)=\varphi(u)\varphi(v) for any words u u, v v over 𝒜 \mathcal{A}. A morphism on 𝒜 \mathcal{A} is entirely defined by the images of letters in 𝒜 \mathcal{A}. All morphisms considered in this paper will be non-erasing: the image of any non-empty word is never empty. Hence the action of a morphism φ \varphi on 𝒜 ∗ \mathcal{A}^{*} can be naturally extended to infinite words; that is, if 𝐱 = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \mathbf{x}=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega}, then f ( 𝐱) = f ( x 1) f ( x 2) f ( x 3) ⋯ f(\mathbf{x})=f(x_{1})f(x_{2})f(x_{3})\cdots. An infinite word 𝐱 \mathbf{x} can therefore be a fixed point of a morphism φ \varphi, i.e., φ ⁡ ( 𝐱) = 𝐱 \varphi(\mathbf{x})=\mathbf{x}. If φ \varphi is a (non-erasing) morphism such that φ ⁡ ( a) = a ​ w \varphi(a)=aw for some letter a ∈ 𝒜 a\in\mathcal{A} and w ∈ 𝒜 + w\in\mathcal{A}^{+}, then φ n ​ ( a) \varphi^{n}(a) is a proper prefix of the word φ n + 1 ​ ( a) \varphi^{n+1}(a) for each n ∈ ℕ n\in\mathbb{N}, and the limit of the sequence ( φ n ​ ( a)) n ≥ 0 (\varphi^{n}(a))_{n\geq 0} is the unique infinite word:

 | 𝐰 = lim n → ∞ φ n ( a) = φ ω ( a) ( = a w φ ( w) φ 2 ( w) φ 3 ( w) ⋯). \mathbf{w}=\underset{n\rightarrow\infty}{\lim}\varphi^{n}(a)=\varphi^{\omega}(a)~(=aw\varphi(w)\varphi^{2}(w)\varphi^{3}(w)\cdots). |  |

Clearly, 𝐰 \mathbf{w} is a fixed point of φ \varphi and we say that 𝐰 \mathbf{w} is *generated*by φ \varphi. Furthermore, an infinite word generated by a morphism is said to be purely morphic.

In what follows, we will denote the composition of morphisms by juxtaposition as for concatenation of words.

## 2 Definitions & basic properties

In the initiating paper [43], episturmian words were defined as an extension of standard episturmian words, which were first introduced as a generalization of standard (or characteristic) Sturmian words using iterated palindromic closure (a construction due to de Luca [41]). Here we choose instead to begin with the following definition for deriving the main basic properties of episturmian words.

###### Definition 2.1.

[43] An infinite word 𝐭 ∈ 𝒜 ω \mathbf{t}\in\mathcal{A}^{\omega} is *episturmian*if F ⁡ ( 𝐭) F(\mathbf{t}) is closed under reversal and 𝐭 \mathbf{t} has at most one left special factor (or equivalently, right special factor) of each length. Moreover, an episturmian word is *standard*if all of its left special factors are prefixes of it.

###### Note.

We can equivalently consider left or right special factors in the first part of the above definition since, by closure under reversal, a factor is left (resp. right) special if and only if its reversal is right (resp. left) special.

###### Remark 2.2.

When | 𝒜 | = 2 |\mathcal{A}|=2, Definition 2.1 gives the (aperiodic) Sturmian words, as well as the periodic balanced infinite words (also known as the periodic Sturmian words). See for instance [62] or Section 7.1.

The following theorem collects together some useful characteristic properties of standard episturmian words. Before stating it, let us first recall the some definitions.

Given two palindromes p p, q q, we say that q q is a central factor of p p if p = w ​ q ​ w ~ p=wq\widetilde{w} for some w ∈ 𝒜 ∗ w\in\mathcal{A}^{*}. The *palindromic right-closure*w ( +) w^{(+)} of a finite word w w is the (unique) shortest palindrome having w w as a prefix (see [41]). That is, w ( +) = w ​ v − 1 ​ w ~ w^{(+)}=wv^{-1}\widetilde{w} where v v is the longest palindromic suffix of w w. For example, ( r ​ a ​ c ​ e) ( +) = r ​ a ​ c ​ e ​ c ​ a ​ r (race)^{(+)}=race\thinspace car. The iterated palindromic closure function [71], denoted by P ​ a ​ l Pal, is defined recursively as follows. Set P ​ a ​ l ​ ( ε) = ε Pal(\varepsilon)=\varepsilon and, for any word w w and letter x x, define P ​ a ​ l ​ ( w ​ x) = ( P ​ a ​ l ​ ( w) ​ x) ( +) Pal(wx)~=~(Pal(w)x)^{(+)}. For instance, P ​ a ​ l ​ ( a ​ b ​ c) = ( P ​ a ​ l ​ ( a ​ b) ​ c) ( +) = ( a ​ b ​ a ​ c) ( +) = a ​ b ​ a ​ c ​ a ​ b ​ a Pal(abc)=(Pal(ab)c)^{(+)}=(abac)^{(+)}=abacaba. (See Sections 4.1 and 6.2.1 for further insight about palindromic closure.)

###### Theorem 2.3.

For an infinite word 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega}, the following properties are equivalent.

1. i)

𝐬 \mathbf{s} is standard episturmian.

2. ii)

Any first occurrence of a palindrome in 𝐬 \mathbf{s} is a central factor of some palindromic prefix of 𝐬 \mathbf{s} (property Pi).

3. iii)

If w w is a prefix of 𝐬 \mathbf{s}, then w ( +) w^{(+)} is also a prefix of 𝐬 \mathbf{s} (property Al).

4. iv)

There exists an infinite word Δ = x 1 x 2 ⋯ \Delta=x_{1}x_{2}\cdots ( x i ∈ 𝒜) (x_{i}\in\mathcal{A}), called the directive word of 𝐬 \mathbf{s}, such that 𝐬 = lim n → ∞ P a l ( x 1 ⋯ x n) \mathbf{s}=\lim_{n\rightarrow\infty}Pal(x_{1}\cdots x_{n}).

###### Remark 2.4.

The palindromes P a l ( x 1 ⋯ x n) Pal(x_{1}\cdots x_{n}) are very often denoted by u n + 1 u_{n+1} in the literature (and we will sometimes use the latter notation when convenient). By construction, these palindromes are exactly the palindromic prefixes of 𝐬 \mathbf{s}. Moreover, 𝐬 \mathbf{s} is uniquely determined by the directive word Δ \Delta.

###### Proof of Theorem 2.3.

OPEN OPEN i) ⇒ i ​ i) i)\Rightarrow ii): Let 𝐬 = u ​ p ​ 𝐭 \mathbf{s}=up\mathbf{t}, u ∈ 𝒜 ∗, 𝐭 ∈ 𝒜 ω u\in\mathcal{A}^{*},\,\mathbf{t}\in\mathcal{A}^{\omega} showing the first occurrence of some palindrome p p in 𝐬 \mathbf{s}. Suppose p p is not the central factor of a palindromic prefix. Then we have 𝐬 = v ​ x ​ w ​ p ​ w ~ ​ y ​ 𝐭 ′ \mathbf{s}=vxwp\tilde{w}y\mathbf{t}^{\prime}, x ≠ y ∈ 𝒜 x\neq y\in\mathcal{A}. By the reversal property, y ​ w ​ p ​ w ~ ​ x ∈ F ⁡ ( s) ywp\tilde{w}x\in F(s), thus w ​ p ​ w ~ wp\tilde{w} is left special, hence is a prefix of 𝐬 \mathbf{s}. Thus p p has another occurrence strictly on the left of the considered one, a contradiction.

OPEN OPEN i) ⇒ i ​ i ​ i) i)\Rightarrow iii): If OPEN i ​ i ​ i) iii) is false, let w = u ​ x w=ux, with u ∈ 𝒜 ∗ u\in\mathcal{A}^{*} and x ∈ 𝒜 x\in\mathcal{A}, be the shortest prefix of 𝐬 \mathbf{s} such that w ( +) w^{(+)} is not a prefix of 𝐬 \mathbf{s}. Thus u ( +) u^{(+)} is a prefix of 𝐬 \mathbf{s}. If u u were not a palindrome then w w would be a prefix of u ( +) u^{(+)}; whence w ( +) = u ( +) w^{(+)}=u^{(+)}, a contradiction. Thus u u is a palindrome. Now let q q be the longest palindromic suffix of w w. Then w ( +) = w 1 ​ q ​ w ~ 1 = w ​ w ~ 1 w^{(+)}=w_{1}q\tilde{w}_{1}=w\tilde{w}_{1} where w = w 1 ​ q w=w_{1}q, and w ( +) = w 1 ​ q ​ f ​ y ​ g w^{(+)}=w_{1}qfyg and w 1 ​ q ​ f ​ z w_{1}qfz is a prefix of 𝐬 \mathbf{s} for some y ≠ z ∈ 𝒜 y\neq z\in\mathcal{A}, f f, g ∈ 𝒜 ∗ g\in\mathcal{A}^{*}. Hence y ​ f ~ ​ q ∈ F ⁡ ( w ~) ⊂ F ⁡ ( 𝐬) y\tilde{f}q\in F(\tilde{w})\subset F(\mathbf{s}) and z ​ f ~ ​ q ∈ F ⁡ ( 𝐬) z\tilde{f}q\in F(\mathbf{s}). Therefore f ~ ​ q \tilde{f}q is a left special prefix of 𝐬 \mathbf{s}. As q ​ f qf is a prefix of w ~ = x ​ u \tilde{w}=xu, x − 1 ​ q ​ f x^{-1}qf is a prefix of u u, hence x − 1 ​ q ​ f ​ α x^{-1}qf\alpha is a prefix of u u for some letter α \alpha. So we have x − 1 ​ q ​ f ​ α = f ~ ​ q x^{-1}qf\alpha=\tilde{f}q, whence α = x \alpha=x and q ​ f ​ x = x ​ f ~ ​ q qfx=x\tilde{f}q. This word is a palindrome and, as it is a suffix of w w, this contradicts the minimality of | q | |q|.

OPEN OPEN i ​ i ​ i) ⇒ i ​ v) iii)\Rightarrow iv): Trivial.

At this stage, we have proved that standard episturmian words satisfy i i), i i i), i v) ii),iii),iv). The equivalence of these three properties is proved in [43, Theorem 1]. Finally, if 𝐬 \mathbf{s} satisfies them, then F ⁡ ( 𝐬) F(\mathbf{s}) is closed under reversal and by [43, Proposition 5] all of its left special factors are prefixes of it, thus 𝐬 \mathbf{s} is standard episturmian. ∎

###### Remark 2.5.

Hereafter, we adopt “epistandard” as a shortcut for “standard episturmian”, as in [64, 99, 101]. Also, unless stated otherwise, the notation Δ = x 1 x 2 x 3 ⋯ \Delta=x_{1}x_{2}x_{3}\cdots ( x i ∈ 𝒜 x_{i}\in\mathcal{A}) will remain for the directive word of an epistandard word 𝐬 \mathbf{s}.

###### Example 2.6.

The epistandard word directed by Δ = ( a ​ b ​ c) ω \Delta=(abc)^{\omega} is known as the Tribonacci word (or Rauzy word [97]); it begins in the following way:

 | 𝐫 = a ¯ b ¯ a c ¯ a b a a ¯ b a c a b a b ¯ a c a b a a b a c a b a c ¯ a b a a b a c a ⋯, \mathbf{r}=\underline{a}\underline{b}a\underline{c}aba\underline{a}bacaba\underline{b}acabaabacaba\underline{c}abaabaca\cdots~, |  |

where each palindromic prefix P a l ( x 1 ⋯ x n) Pal(x_{1}\cdots x_{n}) is followed by an underlined letter x n x_{n}. More generally, for k ≥ 2 k\geq 2, the k k -bonacci word is the epistandard word over { a 1, …, a k } \{a_{1},\ldots,a_{k}\} directed by ( a 1 a 2 ⋯ a k) ω (a_{1}a_{2}\cdots a_{k})^{\omega} (e.g., see [59]).

###### Note.

For recent studies of the properties of Tribonacci word, see for instance [57, 107] and the chapter by Allouche and Berthé in [84].

### 2.1 Equivalence classes

In [43], an infinite word 𝐭 ∈ 𝒜 ω \mathbf{t}\in\mathcal{A}^{\omega} was said to be episturmian if F ⁡ ( 𝐭) = F ⁡ ( 𝐬) F(\mathbf{t})=F(\mathbf{s}) for some epistandard word 𝐬 \mathbf{s}. This definition is equivalent to Definition 2.1 by Theorem 5 in [43]. Moreover, it was proved in [43] that episturmian words are uniformly recurrent, by showing that this nice property is implied by OPEN i ​ v) iv) of Theorem 2.3. Thus, ultimately periodic episturmian words are (purely) periodic. The aperiodic episturmian words are exactly those episturmian words with exactly one left special factor of each length.

In each equivalence class of episturmian words (i.e., same set of factors), there is one epistandard word in the aperiodic case and two in the periodic case, except if this word is a ω a^{\omega} with a a a letter. For example, 𝐬 1 = ( a ​ b ​ a ​ c) ω \mathbf{s}_{1}=(abac)^{\omega} has directive word Δ 1 = a ​ b ​ c ω \Delta_{1}=abc^{\omega} and 𝐬 2 = ( a ​ c ​ a ​ b) ω \mathbf{s}_{2}=(acab)^{\omega} is directed by Δ 2 = a ​ c ​ b ω \Delta_{2}=acb^{\omega}. Both 𝐬 1 \mathbf{s}_{1} and 𝐬 2 \mathbf{s}_{2} are standard with the same factors. Theorem 4.8 in Section 4.3 demonstrates why this is true in general (see also Remark 4.10).

### 2.2 Bi-infinite episturmian words

Definition 2.1 can be extended to bi-infinite words, in which case we must assume they are recurrent. (As is well known, recurrence follows automatically from closure under reversal in the case of right-infinite words; see for instance [29] for a proof of this fact.) Bi-infinite words are sometimes more natural because in particular they can be shifted in both directions, allowing for simpler formulations. More specifically, a (right-infinite) episturmian word 𝐭 \mathbf{t} can be prolonged infinitely to the left with the same set of factors, i.e., remaining in the same equivalence class. There are several or one such prolongation according to whether or not 𝐭 = T i ​ ( 𝐬) \mathbf{t}=\mathrm{T}^{i}(\mathbf{s}), with 𝐬 \mathbf{s} epistandard and i ≥ 0 i\geq 0 (see [73, 75]).

###### Note.

Hereafter, ‘infinite word’ should be taken to mean a right-infinite word, whereas left-infinite and bi-infinite words will be explicitly referred to as such.

### 2.3 Strict episturmian words

An epistandard word 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega}, or any factor-equivalent (episturmian) word 𝐭 \mathbf{t}, is said to be *ℬ \mathcal{B} -strict*(or k k -*strict*if | ℬ | = k |\mathcal{B}|=k, or strict if ℬ \mathcal{B} is understood) if Alph ( Δ) = (\Delta)= Ult ( Δ) = ℬ ⊆ 𝒜 (\Delta)=\mathcal{B}\subseteq\mathcal{A}. That is, an episturmian word is strict if every letter in its alphabet occurs infinitely often in its directive word.

The k k -strict episturmian words are precisely the episturmian words 𝐭 \mathbf{t} having exactly one left special factor of each length and for which any left special factor u u in 𝐭 \mathbf{t} has k = | 𝒜 | k=|\mathcal{A}| different left extensions in 𝐭 \mathbf{t} (i.e., x ​ u xu is a factor of 𝐭 \mathbf{t} for all letters x x in the k k -letter alphabet 𝒜 \mathcal{A}). As a consequence, k k -strict episturmian words have factor complexity ( k − 1) ​ n + 1 (k-1)n+1 for each n ∈ ℕ n\in\mathbb{N} (see [43, Theorem 7]); such words are exactly the k k -letter Arnoux-Rauzy sequences, the study of which began in [12] (see also [74, 105] for example). In particular, the 2 2 -strict episturmian words correspond to the (aperiodic) Sturmian words. Arnoux-Rauzy sequences will be discussed further in Section 5.

###### Remark 2.7.

A noteworthy fact is that an episturmian word is periodic if and only if | Ult ⁡ ( Δ) | = 1 |\mathrm{Ult}(\Delta)|=1 (see [73, Proposition 2.9]). The exact form of a periodic episturmian word is given by Theorem 4.15 in Section 4.4. We first need to consider episturmian morphisms.

## 3 Episturmian morphisms

From Lemma 4 in [43], if 𝐬 \mathbf{s} is epistandard with first letter a = x 1 a=x_{1}, then a a is separating for 𝐬 \mathbf{s} and its factors, i.e., any factor of 𝐬 \mathbf{s} of length 2 2 contains the letter a a. Any episturmian word 𝐭 \mathbf{t} that is factor-equivalent to 𝐬 \mathbf{s} also has separating letter a a, and hence can be factorized with a code:

 | { { a } ∪ a ⁡ ( 𝒜 ∖ { a }) if 𝐭 begins with a, { a } ∪ ( 𝒜 ∖ { a }) ​ a otherwise. \begin{cases}\{a\}\cup a(\mathcal{A}\setminus\{a\})&\mbox{if $\mathbf{t}$ begins with $a$},\\ \{a\}\cup(\mathcal{A}\setminus\{a\})a&\mbox{otherwise}.\end{cases} |  |

This leads to *episturmian morphisms*, which were introduced by Justin and Pirillo [73] in order to study deeper properties of episturmian words. As we shall see in Section 3.2, episturmian morphisms are precisely the morphisms that preserve the set of aperiodic episturmian words (i.e., the morphisms that map aperiodic episturmian words onto aperiodic episturmian words). Such morphisms naturally generalize to any finite alphabet the Sturmian morphisms on two letters. A morphism φ \varphi is said to be Sturmian if φ ⁡ ( 𝐬) \varphi(\mathbf{s}) is Sturmian for any Sturmian word 𝐬 \mathbf{s}. The set of Sturmian morphisms over { a, b } \{a,b\} is closed under composition, and consequently it is a submonoid of the endomorphisms of { a, b } ∗ \{a,b\}^{*}. Moreover, it is well known that the monoid of Sturmian morphisms is generated by the three morphisms: ( a ↦ a b, b ↦ a) (a\mapsto ab,b\mapsto a), ( a ↦ b a. b ↦ a) (a\mapsto ba.b\mapsto a), ( a ↦ b, b ↦ a) (a\mapsto b,b\mapsto a) and that Sturmian morphisms are precisely the morphisms that map Sturmian words onto Sturmian words (see [16, 87]).

### 3.1 Generators & monoids

By definition (see [43, 73]), the monoid of all episturmian morphisms ℰ \mathcal{E} is generated, under composition, by all the morphisms:

- •

ψ a \psi_{a}: ψ a ​ ( a) = a \psi_{a}(a)=a, ψ a ​ ( x) = a ​ x \psi_{a}(x)=ax for any letter x ≠ a x\neq a;

- •

ψ ¯ a \bar{\psi}_{a}: ψ ¯ a ​ ( a) = a \bar{\psi}_{a}(a)=a, ψ ¯ a ​ ( x) = x ​ a \bar{\psi}_{a}(x)=xa for any letter x ≠ a x\neq a;

- •

θ a ​ b \theta_{ab}: exchange of letters a a and b b.

###### Note.

This system of generators is far from minimal, e.g., ψ a = θ a ​ b ​ ψ b ​ θ a ​ b \psi_{a}=\theta_{ab}\psi_{b}\theta_{ab}, but gives simpler formulae.

Moreover, the monoid of so-called epistandard morphisms 𝒮 \mathcal{S} is generated by all the ψ a \psi_{a} and the θ a ​ b \theta_{ab}, and the monoid of pure episturmian morphisms ℰ p \mathcal{E}_{p} (resp. pure epistandard morphisms 𝒮 p \mathcal{S}_{p}) is generated by the ψ a \psi_{a} and ψ ¯ a \bar{\psi}_{a} only (resp. the ψ a \psi_{a} only). The monoid 𝒫 \mathcal{P} of the permutation morphisms (i.e., the morphisms φ \varphi such that φ ⁡ ( 𝒜) = 𝒜 \varphi(\mathcal{A})=\mathcal{A}) is generated by all the θ a ​ b \theta_{ab}. The importance of the monoid of pure episturmian morphisms will become clearer in the next section where we shall see that such morphisms are strongly linked to spinned directive words of episturmian words, which can be viewed as infinite sequences of rules for decomposing episturmian words by morphisms (see Theorems 3.1 and 3.3, to follow). In particular, any episturmian word is the image of another episturmian word by some pure episturmian morphism.

The following diagram illustrates the inclusions between the monoids defined above.

We note in particular that the monoid ℰ \mathcal{E} is a semidirect product of the submonoids of its pure morphisms and of its permutations. Consequently, any episturmian morphism φ ∈ ℰ \varphi\in\mathcal{E} can be expressed in a unique way as φ = π ​ μ = μ ′ ​ π \varphi=\pi\mu=\mu^{\prime}\pi, where μ \mu, μ ′ \mu^{\prime} are pure episturmian morphisms and π \pi is a permutation.

###### Note.

The episturmian morphisms are exactly the Sturmian morphisms when | 𝒜 | = 2 |\mathcal{A}|=2.

Clearly, all episturmian morphisms on 𝒜 \mathcal{A} can be viewed as automorphisms of the free group generated by 𝒜 \mathcal{A} (e.g., see [57, 65, 99, 116]) and it follows that they are injective and that the monoids ℰ \mathcal{E} and 𝒮 \mathcal{S} are left cancellative (see [99, Lemma 7.2]) which means that for any episturmian morphisms f, g, h f,g,h, if f ​ g = f ​ h fg=fh then g = h g=h. Other fundamental properties of episturmian morphisms will be discussed in the next section and in Section 4. For an in-depth study of some further properties of these morphisms, the interested reader is referred to Richomme’s paper [99], in which he considers invertibility, presentation, cancellativity, unitarity, characterization by conjugacy, and so on. Most of the results in [99] naturally generalize those already known for Sturmian morphisms, but some new ones are also proved, such as a characterization of episturmian morphisms that preserve palindromes. In [100, 103], Richomme also characterized the episturmian morphisms that preserve finite and infinite Lyndon words and those that preserve a lexicographic order on words.

### 3.2 Relation with episturmian words

We now state two insightful characterizations of epistandard and episturmian words, which show that any episturmian word can be infinitely decomposed over the set of pure episturmian morphisms.

In the ‘standard’ case:

###### Theorem 3.1.

[73, Corollary 2.7] An infinite word 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega} is epistandard if and only if there exists an infinite word Δ = x 1 x 2 ⋯ \Delta=x_{1}x_{2}\cdots over 𝒜 \mathcal{A} and a sequence ( 𝐬 ( i)) i ≥ 0 (\mathbf{s}^{(i)})_{i\geq 0} of recurrent infinite words such that 𝐬 ( 0) = 𝐬 \mathbf{s}^{(0)}=\mathbf{s} and 𝐬 ( i − 1) = ψ x i ​ ( 𝐬 ( i)) \mathbf{s}^{(i-1)}=\psi_{x_{i}}(\mathbf{s}^{(i)}) for i > 0 i>0. ∎

In [73], Justin and Pirillo showed that the infinite word Δ \Delta appearing in the above theorem is exactly the directive word of 𝐬 \mathbf{s} that arises from the equivalent definition of epistandard words given in Theorem 2.3. In the binary case, the directive word Δ \Delta is related to the continued fraction expansion of the slope of the straight line represented by a standard word (see Chapter 2 in [83]).

###### Example 3.2.

Recall the Tribonacci word 𝐫 \mathbf{r}, which has directive word Δ = ( a ​ b ​ c) ω \Delta=(abc)^{\omega}. We have 𝐫 = ψ a ​ ( 𝐫 ( 1)) \mathbf{r}=\psi_{a}(\mathbf{r}^{(1)}), where 𝐫 ( 1) \mathbf{r}^{(1)} is directed by T ⁡ ( Δ) = ( b ​ c ​ a) ω \mathrm{T}(\Delta)=(bca)^{\omega}. Notice that 𝐫 ( 1) = π ⁡ ( 𝐫) \mathbf{r}^{(1)}=\pi(\mathbf{r}) with π = ( a ​ b ​ c) \pi=(abc); a very particular case.

More generally, the following result (Theorem 3.3) extends the notion of a directive word to all episturmian words. Before stating the theorem, we need to introduce some more notation. First we define a new alphabet, 𝒜 ¯:= { x ¯ | x ∈ 𝒜 } \bar{\mathcal{A}}:=\{\bar{x}~|~x\in\mathcal{A}\}. A letter x ¯ ∈ 𝒜 ¯ \bar{x}\in\bar{\mathcal{A}} is considered to be x x with spin 1 1, whilst x x itself has spin 0 0. The notion of a spin provides a convenient way to call upon the elementary pure episturmian morphisms ψ x \psi_{x} and ψ ¯ x \bar{\psi}_{x}. Moreover, as well shall see in Section 4, it allows us to derive many properties of episturmian words from episturmian morphisms (as a consequence of the next theorem). This approach is used for instance in [23, 60, 81, 101, 102, 105] and of course in the papers of Justin et al.

A finite or infinite word over 𝒜 ∪ 𝒜 ¯ \mathcal{A}\cup\bar{\mathcal{A}} is said to be a spinned word. Given a finite or infinite word w = x 1 x 2 ⋯ w=x_{1}x_{2}\cdots over 𝒜 \mathcal{A}, we sometimes denote by w ˘ = x ˘ 1 x ˘ 2 ⋯ \breve{w}=\breve{x}_{1}\breve{x}_{2}\cdots any spinned word such that x ˘ i = x i \breve{x}_{i}=x_{i} if x i x_{i} has spin 0 0 and x ˘ i = x ¯ i \breve{x}_{i}=\bar{x}_{i} if x i x_{i} has spin 1 1. Such a word w ˘ \breve{w} is called a spinned version of w w.

###### Theorem 3.3.

[73, Theorem 3.10] An infinite word 𝐭 ∈ 𝒜 ω \mathbf{t}\in\mathcal{A}^{\omega} is episturmian if and only if there exists a spinned infinite word Δ ˘ = x ˘ 1 x ˘ 2 x ˘ 3 ⋯ \breve{\Delta}=\breve{x}_{1}\breve{x}_{2}\breve{x}_{3}\cdots over 𝒜 ∪ 𝒜 ¯ \mathcal{A}\cup\bar{\mathcal{A}} and an infinite sequence ( 𝐭 ( i)) i ≥ 0 (\mathbf{t}^{(i)})_{i\geq 0} of recurrent infinite words such that

 | 𝐭 ( 0) = 𝐭 and 𝐭 ( i − 1) = ψ x i ​ ( 𝐭 ( i)) or 𝐭 ( i − 1) = ψ ¯ x i ​ ( 𝐭 ( i)) for all i > 0, \mathbf{t}^{(0)}=\mathbf{t}\hskip 10.00002pt\mbox{and}\hskip 10.00002pt\mathbf{t}^{(i-1)}=\psi_{x_{i}}(\mathbf{t}^{(i)})\hskip 10.00002pt\mbox{or}\hskip 10.00002pt\mathbf{t}^{(i-1)}=\bar{\psi}_{x_{i}}(\mathbf{t}^{(i)})\hskip 10.00002pt\mbox{for all $i>0$}, |  |

according to the spin 0 0 or 1 1 of x ˘ i \breve{x}_{i}, respectively.

For any epistandard word (resp. episturmian word) 𝐭 \mathbf{t} and infinite word Δ \Delta (resp. spinned infinite word Δ ˘ \breve{\Delta}) satisfying the conditions of the Theorem 3.1 (resp. Theorem 3.3), we say that Δ \Delta (resp. Δ ˘ \breve{\Delta}) is a directive word (resp. a (spinned) directive word) for 𝐭 \mathbf{t} or 𝐭 \mathbf{t} is directed by Δ \Delta (resp. Δ ˘ \breve{\Delta}).

###### Remark 3.4.

It follows immediately from Theorem 3.3 that if 𝐭 \mathbf{t} is an episturmian word directed by a spinned infinite word Δ ˘ \breve{\Delta}, then each 𝐭 ( n) \mathbf{t}^{(n)} (as defined in the theorem) is an episturmian word directed by T n ( Δ ˘) = x ˘ n + 1 x ˘ n + 2 x ˘ n + 3 ⋯ \mathrm{T}^{n}(\breve{\Delta})=\breve{x}_{n+1}\breve{x}_{n+2}\breve{x}_{n+3}\cdots.

The following important fact links Theorems 3.1 and 3.3.

###### Remark 3.5.

[73] If 𝐭 \mathbf{t} is an episturmian word directed by a spinned version Δ ˘ \breve{\Delta} of an infinite word Δ \Delta over 𝒜 \mathcal{A}, then 𝐭 \mathbf{t} is factor-equivalent to the (unique) epistandard word 𝐬 \mathbf{s} directed by Δ \Delta.

Moreover, with the same notation as in the above remark, the episturmian word 𝐭 \mathbf{t} is periodic if and only if the epistandard word 𝐬 \mathbf{s} is periodic, and this holds if and only if | Ult ⁡ ( Δ) | = 1 |\mathrm{Ult}(\Delta)|=1 (see Remark 2.7 or Theorem 4.15 later).

###### Example 3.6.

Consider the episturmian word 𝐦 = b a a b a c a b a b ⋯ \mathbf{m}=baabacabab\cdots directed by Δ ˘ = a ¯ ​ b ​ c ¯ ​ ( a ​ b ​ c) ω \breve{\Delta}=\bar{a}b\bar{c}(abc)^{\omega}. Observe that 𝐦 \mathbf{m} is factor-equivalent to the Tribonacci word 𝐫 \mathbf{r}, and we have

 | 𝐦 = ψ ¯ a ​ ( 𝐦 ( 1)) = ψ ¯ a ​ ψ b ​ ( 𝐦 ( 2)) = ψ ¯ a ​ ψ b ​ ψ ¯ c ​ ( 𝐦 ( 3)), \mathbf{m}=\bar{\psi}_{a}(\mathbf{m}^{(1)})=\bar{\psi}_{a}\psi_{b}(\mathbf{m}^{(2)})=\bar{\psi}_{a}\psi_{b}\bar{\psi}_{c}(\mathbf{m}^{(3)}), |  |

where 𝐦 ( 3) \mathbf{m}^{(3)} is directed by T 3 ​ ( Δ ˘) = ( a ​ b ​ c) ω \mathrm{T}^{3}(\breve{\Delta})=(abc)^{\omega}, i.e., 𝐦 ( 3) = 𝐫 \mathbf{m}^{(3)}=\mathbf{r}.

###### Example 3.7.

We now consider an example where the condition that the 𝐭 ( i) \mathbf{t}^{(i)} in Theorem 3.3 are recurrent is not satisfied. Let 𝐭 = d 𝐫 = d a b a c a b a a b a c a b a ⋯ \mathbf{t}=d\mathbf{r}=dabacabaabacaba\cdots where 𝐫 \mathbf{r} is the Tribonacci word and d d is a letter. Then 𝐭 = ψ ¯ a ​ ( 𝐭 ( 1)) \mathbf{t}=\bar{\psi}_{a}(\mathbf{t}^{(1)}), 𝐭 ( 1) = ψ ¯ b ​ ( 𝐭 ( 2)) \mathbf{t}^{(1)}=\bar{\psi}_{b}(\mathbf{t}^{(2)}), 𝐭 ( 2) = ψ ¯ c ​ ( 𝐭 ( 3)) \mathbf{t}^{(2)}=\bar{\psi}_{c}(\mathbf{t}^{(3)}), and so on; however, these 𝐭 ( i) \mathbf{t}^{(i)} are not recurrent (and 𝐭 \mathbf{t} is not episturmian). The infinite word 𝐭 = d ​ 𝐫 \mathbf{t}=d\mathbf{r} is actually an example of an episkew word, i.e., a non-recurrent infinite word having episturmian factors. Such words are discussed in more detail in Section 7.2.

###### Remark 3.8.

Let us point out that the construction of epistandard words by palindromic closure (given in Theorem 2.3) extends to all episturmian words: when x ˘ n = x ¯ n \breve{x}_{n}=\bar{x}_{n} write x n x_{n} on the *left*and use palindromic left-closure. Here 𝐦 \mathbf{m} (from the above example) appears step by step on the right:

 |  | a ¯ ⋅ \displaystyle\underline{a}\>\cdot |  |

 |  | a ⋅ b ¯ ​ a \displaystyle a\cdot\underline{b}a |  |

 | a ​ b ​ a ​ c ¯ \displaystyle aba\underline{c} | a ⋅ b ​ a \displaystyle a\cdot ba |  |

 | a ​ b ​ a ​ c \displaystyle abac | a ⋅ b ​ a ​ a ¯ ​ b ​ a ​ c ​ a ​ b ​ a \displaystyle a\cdot ba\underline{a}bacaba |  |

When an episturmian word is aperiodic, we have the following fundamental link between the words ( 𝐭 ( n)) n ≥ 0 (\mathbf{t}^{(n)})_{n\geq 0} and the spinned infinite word Δ ˘ \breve{\Delta} occurring in Theorem 3.3: if a n a_{n} is the first letter of 𝐭 ( n) \mathbf{t}^{(n)}, then μ x ˘ 1 ⋯ x ˘ n ( a n) \mu_{\breve{x}_{1}\cdots\breve{x}_{n}}(a_{n}) is a prefix of 𝐭 \mathbf{t} and the sequence ( μ x ˘ 1 ⋯ x ˘ n ( a n)) n ≥ 1 (\mu_{\breve{x}_{1}\cdots\breve{x}_{n}}(a_{n}))_{n\geq 1} is not ultimately constant (since Δ ˘ \breve{\Delta} is not ultimately constant), then 𝐭 = lim n → ∞ μ x ˘ 1 ⋯ x ˘ n ( a n) \mathbf{t}=\lim_{n\rightarrow\infty}\mu_{\breve{x}_{1}\cdots\breve{x}_{n}}(a_{n}). This fact is a slight generalization of a result of Risley and Zamboni [105, Prop. III.7] on S-adic representations for standard Arnoux-Rauzy sequences. See also the recent paper [23] for S-adic representations of Sturmian words. Note that S S -adic dynamical systems were introduced by Ferenczi [50] as minimal dynamical systems (e.g., see [96]) generated by a finite number of substitutions. In the case of episturmian words, the notion itself is actually a reformulation of the well-known Rauzy rules, as studied in [98]. In fact, it is well known that the subshift of an aperiodic episturmian word 𝐭 \mathbf{t} (i.e., the topological closure of the shift orbit of 𝐭 \mathbf{t}) is a minimal dynamical system, i.e., it consists of all the episturmian words with the same set of factors as 𝐭 \mathbf{t}.

It is not hard to see that a morphism is episturmian (resp. epistandard) if and only if it preserves the set of aperiodic episturmian (resp. epistandard) words (see [73]). Even more:

###### Theorem 3.9.

[73, Theorem 3.13] A morphism φ \varphi is episturmian (resp. epistandard) if there exist strict episturmian (resp. epistandard) words 𝐦 \mathbf{m}, 𝐭 \mathbf{t} such that 𝐦 = φ ⁡ ( 𝐭) \mathbf{m}=\varphi(\mathbf{t}). ∎

Purely morphic episturmian words (i.e., those generated by morphisms) are discussed further in Section 4, where we consider the relationship between spins and the shifts that they induce. These ideas were used in [75] to obtain a complete answer to the question: if an episturmian word is purely morphic, which shifts of it, if any, are also purely morphic? (See Theorem 4.19, to follow.) Such rigidity issues are discussed in more detail in Sections 4.4 and 8.

In [75], Justin and Pirillo also made use of bi-infinite words, which often allow for more natural formulations. Indeed, the characterization (Theorem 3.3) of right-infinite episturmian words by a sequence ( 𝐭 ( i)) i ≥ 0 (\mathbf{t}^{(i)})_{i\geq 0} extends to bi-infinite episturmian words, with all the 𝐭 ( i) \mathbf{t}^{(i)} now bi-infinite episturmian words. That is, as for right-infinite episturmian words, we have bi-infinite words of the form 𝐥 ( i). 𝐫 ( i) \mathbf{l}^{(i)}.\mathbf{r}^{(i)} where 𝐥 ( i) \mathbf{l}^{(i)} is a left-infinite episturmian word and 𝐫 ( i) \mathbf{r}^{(i)} is a right-infinite episturmian word. Moreover, if the bi-infinite episturmian word 𝐛 = 𝐥. 𝐫 \mathbf{b}=\mathbf{l}.\mathbf{r} is directed by Δ ˘ \breve{\Delta} with associated bi-infinite episturmian words 𝐛 ( i) = 𝐥 ( i). 𝐫 ( i) \mathbf{b}^{(i)}=\mathbf{l}^{(i)}.\mathbf{r}^{(i)}, then 𝐫 \mathbf{r} is directed by Δ ˘ \breve{\Delta} with associated right-infinite episturmian words 𝐫 ( i) \mathbf{r}^{(i)}.

## 4 Spins, shifts, and directive words

In this section, we discuss in more detail the notion of spins, the shifts they induce, and the concept of block-equivalence in connection with directive words. These notions allow us to study in particular when two different spinned infinite words direct the same episturmian word. Indeed, as we shall see in Section 4.3, the correspondence between episturmian words and spinned directive words is not one-to-one.

### 4.1 Notation for pure episturmian morphisms

For a ∈ 𝒜 a\in\mathcal{A}, let μ a = ψ a \mu_{a}=\psi_{a} and μ a ¯ = ψ ¯ a \mu_{\bar{a}}=\bar{\psi}_{a}. This operator μ \mu can be naturally extended (as done in [73]) to a pure episturmian morphism: for any spinned finite word w ˘ = x ˘ 1 ⋯ x ˘ n \breve{w}=\breve{x}_{1}\cdots\breve{x}_{n} over 𝒜 ∪ 𝒜 ¯ \mathcal{A}\cup\bar{\mathcal{A}}, we define μ w ˘:= μ x ˘ 1 ⋯ μ x ˘ n \mu_{\breve{w}}:=\mu_{\breve{x}_{1}}\cdots\mu_{\breve{x}_{n}} and set μ ε \mu_{\varepsilon} equal to the identity morphism Id.

Viewing w = x 1 x 2 ⋯ x n w=x_{1}x_{2}\cdots x_{n} as a prefix of the directive word Δ = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega}, it is clear from Theorem 3.1 that the words

 | μ x 1 ⋯ x n − 1 ( x n), n ≥ 1, \mu_{x_{1}\cdots x_{n-1}}(x_{n}),\hskip 10.00002ptn\geq 1, |  |

are prefixes of the epistandard word 𝐬 \mathbf{s} directed by Δ \Delta.

###### Example 4.1.

We observe that any epistandard word 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega} has the form 𝐬 = μ w ​ ( 𝐬 ′) \mathbf{s}=\mu_{w}(\mathbf{s}^{\prime}) for some uniquely determined finite word w w and strict epistandard word 𝐬 ′ \mathbf{s}^{\prime}. Indeed, if Δ = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega} is the directive word of 𝐬 \mathbf{s} and m m is the smallest positive integer such that Alph ( x m + 1 x m + 2 ⋯) = Alph ( Δ) \textrm{Alph}(x_{m+1}x_{m+2}\cdots)=\textrm{Alph}(\Delta), then x 1 ⋯ x m x_{1}\cdots x_{m} is the shortest prefix of Δ \Delta that contains all the letters not appearing infinitely often in Δ \Delta. Moreover, by Theorem 3.1, 𝐬 = μ x 1 ⋯ x m ( 𝐬 ( m)) \mathbf{s}=\mu_{x_{1}\cdots x_{m}}(\mathbf{s}^{(m)}) where 𝐬 ( m) \mathbf{s}^{(m)} is the epistandard word directed by T m ( Δ) = x m + 1 x m + 2 ⋯ \mathrm{T}^{m}(\Delta)=x_{m+1}x_{m+2}\cdots. Since Ult ⁡ ( T m ​ ( Δ)) = Alph ​ ( T m ​ ( Δ)) \mathrm{Ult}(\mathrm{T}^{m}(\Delta))=\textrm{Alph}(\mathrm{T}^{m}(\Delta)) by construction, the epistandard word 𝐬 ( m) \mathbf{s}^{(m)} is strict. For example, with Δ = c ​ ( a ​ b) ω \Delta=c(ab)^{\omega}, we have 𝐬 = ψ c ​ ( 𝐬 ( 1)) \mathbf{s}=\psi_{c}(\mathbf{s}^{(1)}) where 𝐬 ( 1) \mathbf{s}^{(1)} is directed by ( a ​ b) ω (ab)^{\omega}, i.e., 𝐬 ( 1) \mathbf{s}^{(1)} is the well-known *Fibonacci word*over { a, b } \{a,b\}.

For n ≥ 1 n\geq 1, let u n + 1:= P a l ( x 1 ⋯ x n) u_{n+1}:=Pal(x_{1}\cdots x_{n}) and set u 1 = ε u_{1}=\varepsilon. Then by part OPEN i ​ v) iv) of Theorem 2.3, the epistandard word 𝐬 \mathbf{s} directed by Δ \Delta is given by 𝐬 = lim n → ∞ u n \mathbf{s}=\lim_{n\rightarrow\infty}u_{n}. We have the following useful formula from [73]:

 | u i + 1 = μ x 1 ⋯ x i − 1 ( x i) u i for i > 0. u_{i+1}=\mu_{x_{1}\cdots x_{i-1}}(x_{i})u_{i}\hskip 10.00002pt\mbox{for $i>0$}. |  | (4.1) |

For letters ( x j) 1 ≤ j ≤ i (x_{j})_{1\leq j\leq i}, formula ( 4.1) inductively leads to:

 | u i + 1 = μ x 1 ⋯ x i − 1 ( x i) ⋯ μ x 1 ( x 2) x 1 = ∏ 1 ≤ j ≤ i μ x 1 ⋯ x j − 1 ( x j). u_{i+1}=\mu_{x_{1}\cdots x_{i-1}}(x_{i})\cdots\mu_{x_{1}}(x_{2})x_{1}=\prod_{1\leq j\leq i}\mu_{x_{1}\cdots x_{j-1}}(x_{j}). |  | (4.2) |

(Note that by convention, x 1 ⋯ x 0 = ε x_{1}\cdots x_{0}=\varepsilon in the above product.) For example, with Δ = a b c b ⋯ \Delta=abcb\cdots, we compute:

 | u 3 = P ​ a ​ l ​ ( a ​ b ​ c ​ b) = μ a ​ b ​ c ​ ( b) ​ μ a ​ b ​ ( c) ​ μ a ​ ( b) ​ a = a ​ b ​ a ​ c ​ a ​ b ⋅ a ​ b ​ a ​ c ⋅ a ​ b ⋅ a. u_{3}=Pal(abcb)=\mu_{abc}(b)\mu_{ab}(c)\mu_{a}(b)a=abacab\cdot abac\cdot ab\cdot a. |  |

### 4.2 Shifts

Now let w ˘ = x ˘ 1 x ˘ 2 ⋯ x ˘ n \breve{w}=\breve{x}_{1}\breve{x}_{2}\cdots\breve{x}_{n} be a spinned version of w = x 1 x 2 ⋯ x n w=x_{1}x_{2}\cdots x_{n} (viewed as a prefix of a spinned version Δ ˘ \breve{\Delta} of Δ \Delta). Then, for any finite word v v, we have

 | μ w ˘ ​ ( v) = S w ˘ − 1 ​ μ w ​ ( v) ​ S w ˘ where S w ˘ = ∏ i = n, …, 1 ∣ x ˘ i = x ¯ i μ x 1 ⋯ x i − 1 ( x i). \mu_{\breve{w}}(v)=S_{\breve{w}}^{-1}\mu_{w}(v)S_{\breve{w}}\hskip 10.00002pt\mbox{where $S_{\breve{w}}=\underset{\underset{\mid\breve{x}_{i}=\bar{x}_{i}}{i=n,\ldots,1}}{\prod}\mu_{x_{1}\cdots x_{i-1}}(x_{i})$.} |  | (4.3) |

Observe that S w ˘ S_{\breve{w}} is a prefix of P ​ a ​ l ​ ( w) Pal(w); in particular S w ¯ = P ​ a ​ l ​ ( w) S_{\bar{w}}=Pal(w) by equation ( 4.2). Note also that μ w ˘ ​ ( v) = T | S w ˘ | ​ ( μ w ​ ( v)) \mu_{\breve{w}}(v)=\mathrm{T}^{|S_{\breve{w}}|}(\mu_{w}(v)). The word S w ˘ S_{\breve{w}} is called the shifting factor of μ w ˘ \mu_{\breve{w}} and its length | S w ˘ | |S_{\breve{w}}| is called the shift induced by the prefix w ˘ \breve{w} of Δ ˘ \breve{\Delta} of length n n [75].

###### Example 4.2.

If we take w ˘ = a ​ b ¯ ​ c ​ a ¯ \breve{w}=a\bar{b}c\bar{a}, then

 | S w ˘ = μ a ​ b ​ c ​ ( a) ​ μ a ​ ( b) = a ​ b ​ a ​ c ​ a ​ b ​ a ⋅ a ​ b. S_{\breve{w}}=\mu_{abc}(a)\mu_{a}(b)=abacaba\cdot ab. |  |

Thus since μ a ​ b ​ c ​ a ​ ( c ​ a) = a ​ b ​ a ​ c ​ a ​ b ​ a ​ a ​ b ⋅ a ​ c ​ a ​ b ​ a ​ c ​ a ​ b ​ a \mu_{abca}(ca)=abacabaab\cdot acabacaba, we have

 | μ a ​ b ¯ ​ c ​ a ¯ ​ ( c ​ a) = T 9 ​ ( μ a ​ b ​ c ​ a ​ ( c ​ a)) = a ​ c ​ a ​ b ​ a ​ c ​ a ​ b ​ a ⋅ a ​ b ​ a ​ c ​ a ​ b ​ a ​ a ​ b. \mu_{a\bar{b}c\bar{a}}(ca)=\mathrm{T}^{9}(\mu_{abca}(ca))=acabacaba\cdot abacabaab. |  |

Likewise, for any infinite word 𝐲 ∈ 𝒜 ω \mathbf{y}\in\mathcal{A}^{\omega}, μ w ˘ ​ ( 𝐲) = S w ˘ − 1 ​ μ w ​ ( 𝐲) \mu_{\breve{w}}(\mathbf{y})=S_{\breve{w}}^{-1}\mu_{w}(\mathbf{y}). For example, if we take w ˘ = a ¯ ​ b ¯ \breve{w}=\bar{a}\bar{b}, then S w ˘ = P ​ a ​ l ​ ( a ​ b) = a ​ b ​ a S_{\breve{w}}=Pal(ab)=aba, and hence μ a ¯ ​ b ¯ ​ ( 𝐲) = ( a ​ b ​ a) − 1 ​ μ a ​ b ​ ( 𝐲) \mu_{\bar{a}\bar{b}}(\mathbf{y})=(aba)^{-1}\mu_{ab}(\mathbf{y}) for any infinite word 𝐲 \mathbf{y}.

###### Note.

The morphisms μ w \mu_{w} and μ w ˘ \mu_{\breve{w}} are conjugate morphisms [99].

### 4.3 Block-equivalence & directive words

By Theorem 2.3 (and also Theorem 3.1), any epistandard word 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega} has a unique directive word over 𝒜 \mathcal{A}, but 𝐬 \mathbf{s} also has infinitely many other spinned directive words (see [73, 75, 63]). For example, the Tribonacci word is directed by ( a ​ b ​ c) ω (abc)^{\omega} and also by ( a ​ b ​ c) n ​ a ¯ ​ b ¯ ​ c ¯ ​ ( a ​ b ¯ ​ c ¯) ω (abc)^{n}\bar{a}\bar{b}\bar{c}(a\bar{b}\bar{c})^{\omega} for each n ≥ 0 n\geq 0, as well as infinitely many other spinned words. The natural question: “does any spinned word direct a unique episturmian word?” was answered in [73].

###### Proposition 4.3.

[73]

1. 1.

Any spinned infinite word Δ ˘ \breve{\Delta} having infinitely many letters with spin 0 0 directs a unique episturmian word beginning with the left-most letter having spin 0 0 in Δ ˘ \breve{\Delta}.

2. 2.

Any spinned infinite word Δ ˘ \breve{\Delta} with all spins ultimately 1 1 directs exactly | Ult ⁡ ( Δ) | |\mathrm{Ult}(\Delta)| episturmian words.

3. 3.

Let Δ ˘ \breve{\Delta} be a spinned infinite word having all its letters with spin 1 1 and let a ∈ Ult ⁡ ( Δ) a\in\mathrm{Ult}(\Delta). Then Δ ˘ \breve{\Delta} directs exactly one episturmian word starting with a a. ∎

###### Note.

The above statement corrects a small error in Proposition 3.11 of [73] where item 3 was stated in the more general case when Δ ˘ \breve{\Delta} has all spins ultimately 1 1. In this case, Δ ˘ \breve{\Delta} still directs exactly one episturmian word for each letter a a in Ult ⁡ ( Δ) \mathrm{Ult}(\Delta), but contrary to what is written in [73], nothing can be said about its first letter.

Block-equivalence for spinned words was introduced in [75] as a way of studying when Δ ˘ \breve{\Delta} and Δ ^ \hat{\Delta} (two spinned versions of a directive word Δ \Delta) direct the same bi-infinite episturmian word. We do not recall the full details here, only a few notions relating to it.

###### Notation.

If v ∈ 𝒜 + v\in\mathcal{A}^{+}, then v ¯ ∈ 𝒜 ¯ + \bar{v}\in\bar{\mathcal{A}}^{+} is v v with all spins 1 1.

A word of the form x ​ v ​ x xvx, where x ∈ 𝒜 x\in\mathcal{A} and v ∈ ( 𝒜 ∖ { x }) ∗ v\in(\mathcal{A}\setminus\{x\})^{*}, is called a ( x x -based) block. A ( x x -based) block-transformation is the replacement in a spinned word of an occurrence of x ​ v ​ x ¯ xv\bar{x} (where x ​ v ​ x xvx is a block) by x ¯ ​ v ¯ ​ x \bar{x}\bar{v}x or vice-versa. Two finite spinned words w w, w ′ w^{\prime} are said to be block-equivalent if we can pass from one to the other by a (possibly empty) chain of block-transformations, in which case we write w ≡ w ′ w\equiv w^{\prime}. For example, b ¯ ​ a ¯ ​ b ​ c ¯ ​ b ​ a ¯ ​ c ¯ \bar{b}\bar{a}b\bar{c}b\bar{a}\bar{c} and b ​ a ​ b ​ c ​ b ¯ ​ a ¯ ​ c ¯ babc\bar{b}\bar{a}\bar{c} are block-equivalent because b ¯ ​ a ¯ ​ b ​ c ¯ ​ b ​ a ¯ ​ c ¯ → b ​ a ​ b ¯ ​ c ¯ ​ b ​ a ¯ ​ c ¯ → b ​ a ​ b ​ c ​ b ¯ ​ a ¯ ​ c ¯ \bar{b}\bar{a}b\bar{c}b\bar{a}\bar{c}\rightarrow ba\bar{b}\bar{c}b\bar{a}\bar{c}\rightarrow babc\bar{b}\bar{a}\bar{c} and vice-versa. Note that if w ≡ w ′ w\equiv w^{\prime} then w w and w ′ w^{\prime} are spinned versions of the same word over 𝒜 \mathcal{A}. Block-equivalence extends to (right-)infinite words as follows.

Let Δ 1 \Delta_{1}, Δ 2 \Delta_{2} be spinned versions of Δ \Delta. We write Δ 1 ↝ Δ 2 \Delta_{1}\rightsquigarrow\Delta_{2} if there exist infinitely many prefixes f i {f}_{i} of Δ 1 \Delta_{1} and g i {g}_{i} of Δ 2 \Delta_{2} with the g i g_{i} of strictly increasing lengths, and such that, for all i i, | g i | ≤ | f i | |g_{i}|\leq|f_{i}| and f i ≡ g i ​ c i {f}_{i}\equiv{g}_{i}{c}_{i} for a suitable spinned word c i {c}_{i}. Infinite words Δ 1 \Delta_{1} and Δ 2 \Delta_{2} are said to be block-equivalent (denoted by Δ 1 ≡ Δ 2 \Delta_{1}\equiv\Delta_{2}) if Δ 1 ↝ Δ 2 \Delta_{1}\rightsquigarrow\Delta_{2} and Δ 2 ↝ Δ 1 \Delta_{2}\rightsquigarrow\Delta_{1}.

###### Remark 4.4.

If x x is a letter and v ∈ 𝒜 ∗ v\in\mathcal{A}^{*} is x x -free, then x ¯ ​ v ¯ ​ x \bar{x}\bar{v}x and x ​ v ​ x ¯ xv\bar{x} are block-equivalent and they induce the same shift, i.e., μ x ¯ ​ v ¯ ​ x = μ x ​ v ​ x ¯ \mu_{\bar{x}\bar{v}x}=\mu_{xv\bar{x}} [75, Theorem 2.2]. Thus the monoid of pure episturmian morphisms, ℰ p \mathcal{E}_{p}, is isomorphic to the quotient of ( 𝒜 ∪ 𝒜 ¯) ∗ (\mathcal{A}\cup\bar{\mathcal{A}})^{*} by the block-equivalence generated by

 | { x ¯ v ¯ x ≡ x v x ¯ ∣ x ∈ 𝒜, v is x -free }. \{\bar{x}\bar{v}x\equiv xv\bar{x}\mid x\in\mathcal{A},v\ \mathrm{is}\ \mbox{$x$-free}\}. |  |

Note that this has some relation to the study of conjugacy and episturmian morphisms carried out by Richomme [99].

From what we have already learned about bi-infinite episturmian words (in Sections 2.2 and 3.2), it is clear that Justin and Pirillo’s results about spinned infinite words directing the same bi-infinite episturmian word are still valid for words directing the same (right-infinite) episturmian word. Roughly speaking, two spinned infinite words direct the same episturmian word if and only if they are block-equivalent. For instance, we have the following results for wavy spinned versions of Δ ∈ 𝒜 ω \Delta\in\mathcal{A}^{\omega}. A spinned version Δ ˘ \breve{\Delta} of Δ \Delta is said to be wavy if Δ ˘ \breve{\Delta} contains infinitely many letters of spin 0 0 and infinitely many letters of spin 1 1.

###### Theorem 4.5.

[75, Theorem 3.4] Suppose Δ ˘ \breve{\Delta} and Δ ^ \hat{\Delta} are wavy versions of Δ ∈ 𝒜 ω \Delta\in\mathcal{A}^{\omega} with | Ult ⁡ ( Δ) | > 1 |\mathrm{Ult}(\Delta)|>1. Then Δ ˘ \breve{\Delta} and Δ ^ \hat{\Delta} direct the same episturmian word if and only if Δ ˘ ≡ Δ ^ \breve{\Delta}\equiv\hat{\Delta}. ∎

For example, b ​ a ​ ( b ¯ ​ c ​ a ¯) ω ba(\bar{b}c\bar{a})^{\omega} and b ¯ ​ a ¯ ​ b ​ ( c ​ a ¯ ​ b ¯) ω \bar{b}\bar{a}b(c\bar{a}\bar{b})^{\omega} direct the same episturmian word, namely μ b ​ a ​ b ¯ ​ c ​ ( c ​ 𝐫) \mu_{ba\bar{b}c}(c\mathbf{r}) ( = μ b ¯ ​ a ¯ ​ b ​ c ​ ( c ​ 𝐫) =\mu_{\bar{b}\bar{a}bc}(c\mathbf{r})) where 𝐫 \mathbf{r} is the Tribonacci word.

###### Theorem 4.6.

[75, Prop. 3.6] Let Δ ˘ \breve{\Delta}, Δ ^ \hat{\Delta} be two spinned versions of Δ ∈ 𝒜 ω \Delta\in\mathcal{A}^{\omega} with | Ult ⁡ ( Δ) | > 1 |\mathrm{Ult}(\Delta)|>1, Δ ˘ \breve{\Delta} wavy, and Δ ^ \hat{\Delta} having all spins ultimately 0 0 or 1 1. If Δ ˘ \breve{\Delta} and Δ ^ \hat{\Delta} direct the same episturmian word, then Δ ˘ ↝ Δ ^ \breve{\Delta}\rightsquigarrow\hat{\Delta}. ∎

Similar results also hold when all spins are ultimately 0 0 or 1 1 and in the periodic case. See Propositions 3.7 and 3.10 in [75].

###### Remark 4.7.

In [75], the study of block-equivalence for finite spinned words led to numeration systems that resemble the Ostrowski systems [20] associated with Sturmian words. A matrix formula for computing the number of representations of an integer in such a system was also given in [75, Section 2].

More recently, Glen, Levé, and Richomme [63] established the following complete characterization of pairs of spinned infinite words directing the same unique episturmian word. Not only does the following theorem provide the relative forms of two spinned infinite words directing the same episturmian word, but it also fully solves the periodic case, which was only partially solved in [75].

###### Theorem 4.8.

[63] Given two spinned infinite words Δ 1 \Delta_{1} and Δ 2 \Delta_{2}, the following assertions are equivalent.

i) Δ 1 \Delta_{1} and Δ 2 \Delta_{2} direct the same right-infinite episturmian word.

ii) One of the following cases holds for some i, j i,j such that { i, j } = { 1, 2 } \{i,j\}=\{1,2\}:

1. 1.

Δ i = ∏ n ≥ 1 v n \Delta_{i}=\prod_{n\geq 1}v_{n}, Δ j = ∏ n ≥ 1 z n \Delta_{j}=\prod_{n\geq 1}z_{n} where ( v n) n ≥ 1, ( z n) n ≥ 1 (v_{n})_{n\geq 1},(z_{n})_{n\geq 1} are spinned words such that μ v n = μ z n \mu_{v_{n}}=\mu_{z_{n}} for all n ≥ 1 n\geq 1;

2. 2.

Δ i = w ​ x ​ ∏ n ≥ 1 v n ​ x ˘ n \Delta_{i}={w}x\prod_{n\geq 1}v_{n}{\breve{x}}_{n}, Δ j = w ′ ​ x ¯ ​ ∏ n ≥ 1 v ¯ n ​ x ^ n \Delta_{j}={w^{\prime}}{\bar{x}}\prod_{n\geq 1}{\bar{v}}_{n}{\hat{x}}_{n} where w {w}, w ′ {w^{\prime}} are spinned words such that μ w = μ w ′ \mu_{w}=\mu_{w^{\prime}}, x x is a letter, ( v n) n ≥ 1 (v_{n})_{n\geq 1} is a sequence of non-empty x x -free words, and ( x ˘ n) n ≥ 1 ({\breve{x}}_{n})_{n\geq 1}, ( x ^ n) n ≥ 1 ({\hat{x}}_{n})_{n\geq 1} are sequences of non-empty spinned words over { x, x ¯ } \{x,\bar{x}\} such that, for all n ≥ 1 n\geq 1, | x ˘ n | = | x ^ n | |{\breve{x}}_{n}|=|{\hat{x}}_{n}| and | x ˘ n | x = | x ^ n | x |{\breve{x}}_{n}|_{x}=|{\hat{x}}_{n}|_{x};

3. 3.

Δ 1 = w ​ 𝐱 \Delta_{1}=w\mathbf{x} and Δ 2 = w ′ ​ 𝐲 \Delta_{2}=w^{\prime}\mathbf{y} where w w, w ′ w^{\prime} are spinned words, x x and y y are letters, and 𝐱 ∈ { x, x ¯ } ω \mathbf{x}\in\{x,\bar{x}\}^{\omega}, 𝐲 ∈ { y, y ¯ } ω \mathbf{y}\in\{y,\bar{y}\}^{\omega} are spinned infinite words such that μ w ​ ( x) = μ w ′ ​ ( y) \mu_{w}(x)=\mu_{w^{\prime}}(y).

∎

In items 1 and 2 of Theorem 4.8, the two considered directive words are spinned versions of the same infinite word. This does not hold in item 3, which concerns only periodic episturmian words. In particular, we observe the following:

###### Remark 4.9.

If an aperiodic episturmian word is directed by two different spinned infinite words Δ 1 \Delta_{1} and Δ 2 \Delta_{2}, then Δ 1 \Delta_{1} and Δ 2 \Delta_{2} are spinned versions of the same word Δ \Delta.

As an example of item 3, one can consider the periodic episturmian word ( b ​ c ​ b ​ a) ω (bcba)^{\omega} which is directed by both b ​ c ​ a ω bca^{\omega} and b ​ a ¯ ​ c ω b\bar{a}c^{\omega} (since μ b ​ c ​ ( a) = μ b ​ a ¯ ​ ( c) \mu_{bc}(a)=\mu_{b\bar{a}}(c)). Note also that ( b ​ c ​ b ​ a) ω (bcba)^{\omega} is epistandard and has the same set of factors as the epistandard word ( b ​ a ​ b ​ c) ω (babc)^{\omega} directed by b ​ a ​ c ω bac^{\omega}. Actually, in view of Remark 3.5, we observe the following:

###### Remark 4.10.

The subshift of any aperiodic episturmian word contains a unique (aperiodic) epistandard word, whereas the subshift of a periodic episturmian word contains exactly two (periodic) epistandard words, except if this word is a ω a^{\omega} with a a a letter.

We also observe that x x and y y can be equal in item 3 of Theorem 4.8; for example ( a ​ b) ω (ab)^{\omega} is directed by a ​ b ¯ ​ b ω a\bar{b}b^{\omega} and by a ​ b ω ab^{\omega}.

###### Example 4.11.

[63] For a, b, c a,b,c three different letters in 𝒜 \mathcal{A}, the spinned infinite words Δ 1 = a ​ ( b ​ c ​ a ¯) ω \Delta_{1}=a(bc{\bar{a}})^{\omega} and Δ 2 = a ¯ ​ ( b ¯ ​ c ¯ ​ a ¯) ω \Delta_{2}={\bar{a}}({\bar{b}}{\bar{c}}{\bar{a}})^{\omega} direct the same episturmian word that starts with the letter a a. Indeed, these two directive words fulfill item 2 of Theorem 4.8 with w = w ′ = ε w=w^{\prime}=\varepsilon, x = a x=a, and for all n n, v n = b ​ c v_{n}=bc and x ˘ n = x ^ n = a ¯ \breve{x}_{n}=\hat{x}_{n}=\bar{a}. Moreover the fact that Δ 1 \Delta_{1} starts with the letter a a shows that the word it directs starts with a a. Similarly Δ 1 ′ = a ¯ ​ b ​ ( c ​ a ​ b ¯) ω \Delta_{1}^{\prime}={\bar{a}}b(ca{\bar{b}})^{\omega} and Δ 2 ′ = a ¯ ​ b ¯ ​ ( c ¯ ​ a ¯ ​ b ¯) ω \Delta_{2}^{\prime}={\bar{a}}{\bar{b}}({\bar{c}}{\bar{a}}{\bar{b}})^{\omega} direct the same episturmian word starting with the letter b b. Since Δ 2 = Δ 2 ′ \Delta_{2}=\Delta_{2}^{\prime}, this shows that the relation “direct the same episturmian word” over spinned infinite words is not an equivalence relation.

Items 2 and 3 of Theorem 4.8 show that any episturmian word is directed by a spinned infinite word having infinitely many letters of spin 0, but also by a spinned word having both infinitely many letters of spin 0 and infinitely many letters of spin 1 (i.e., a wavy word). To emphasize the importance of these facts, let us recall from Proposition 4.3 that if Δ ˘ \breve{\Delta} is a spinned infinite word over 𝒜 ∪ 𝒜 ¯ \mathcal{A}\cup\bar{\mathcal{A}} with infinitely many letters of spin 0, then there exists a unique episturmian word 𝐭 \mathbf{t} directed by Δ ˘ \breve{\Delta}. Unicity comes from the fact that the first letter of 𝐭 \mathbf{t} is fixed by the first letter of spin 0 in Δ ˘ \breve{\Delta}. We also note that if an episturmian word 𝐭 \mathbf{t} has two directive words satisfying items 2 or 3, then 𝐭 \mathbf{t} has infinitely many directive words (this was shown in [63]).

When studying repetitions in Sturmian words, Berthé, Holton, and Zamboni [23] proved that any Sturmian word has a unique directive word over { a, b, a ¯, b ¯ } \{a,b,\bar{a},\bar{b}\} containing infinitely many letters of spin 0, but no factor of the form a ¯ ​ b ¯ n ​ a {\bar{a}}{\bar{b}}^{n}a or b ¯ ​ a ¯ n ​ b {\bar{b}}{\bar{a}}^{n}b with n n an integer. Levé and Richomme [80] recently generalized this result to episturmian words by introducing a way to ‘normalize’ the directive word(s) of an episturmian word so that any episturmian word can be defined uniquely by its so-called normalized directive word, defined by some factor avoidance, as follows. This idea has since proved useful in the study of quasiperiodic episturmian words (see Section 8); in particular, it provides an effective way to decide whether or not a given episturmian word is quasiperiodic.

###### Theorem 4.12.

[63, 80] Any episturmian word 𝐭 ∈ 𝒜 ω \mathbf{t}\in\mathcal{A}^{\omega} has a spinned directive word Δ ˘ \breve{\Delta} containing infinitely many letters of spin 0 0, but no factor in ⋃ a ∈ 𝒜 a ¯ ​ 𝒜 ¯ ∗ ​ a {\bigcup}_{a\in\mathcal{A}}\bar{a}\bar{\mathcal{A}}^{*}a. Such a directive word is unique if 𝐭 \mathbf{t} is aperiodic, in which case Δ ˘ \breve{\Delta} is called the normalized directive word for 𝐭 \mathbf{t}. ∎

###### Note.

Unicity does not necessarily hold for periodic episturmian words. For example, the periodic episturmian word ( a ​ b) ω = ψ a ​ ( b ω) = ψ ¯ b ​ ( a ω) (ab)^{\omega}=\psi_{a}(b^{\omega})=\bar{\psi}_{b}(a^{\omega}) is directed by a ​ b ω a{b}^{\omega} and by b ¯ ​ a ω \bar{b}a^{\omega} (since ψ a ​ ( b) = a ​ b = ψ ¯ b ​ ( a) \psi_{a}(b)=ab=\bar{\psi}_{b}(a)).

The following result tells us precisely which episturmian words have a unique directive word.

###### Theorem 4.13.

[63] An episturmian word 𝐭 ∈ 𝒜 ω \mathbf{t}\in\mathcal{A}^{\omega} has a unique directive word if and only if the (normalized) directive word of 𝐭 \mathbf{t} contains 1) infinitely many letters of spin 0 0, 2) infinitely many letters of spin 1 1, 3) no factor in ⋃ a ∈ 𝒜 a ¯ ​ 𝒜 ¯ ∗ ​ a {\bigcup}_{a\in\mathcal{A}}\bar{a}\bar{\mathcal{A}}^{*}a, and 4) no factor in ⋃ a ∈ 𝒜 a ​ 𝒜 ∗ ​ a ¯ {\bigcup}_{a\in\mathcal{A}}a\mathcal{A}^{*}\bar{a}. Such an episturmian word is necessarily aperiodic. ∎

For instance, a particular family of episturmian words having unique directive words consists of those directed by regular wavy words [58, 64], i.e., spinned infinite words having both infinitely many letters of spin 0 0 and infinitely many letters of spin 1 1 such that each letter occurs with the same spin everywhere in the directive word. More formally, a spinned version w ˘ \breve{w} of a finite or infinite word w w is said to be regular if, for each letter x ∈ Alph ​ ( w) x\in\textrm{Alph}(w), all occurrences of x ˘ \breve{x} in w ˘ \breve{w} have the same spin ( 0 CLOSE (0 or OPEN 1) 1). For example, the regular wavy word ( a ​ b ¯ ​ c ¯) ω (a\bar{b}\bar{c})^{\omega} is the unique directive word for the episturmian word a 𝐫 = a a b a c a b a a b a c a b ⋯ a\mathbf{r}=a{a}{b}a{c}aba{a}bacab\cdots~ where 𝐫 \mathbf{r} is the Tribonacci word.

In the Sturmian case, we have:

###### Proposition 4.14.

[63] Any Sturmian word has either a unique spinned directive word or infinitely many spinned directive words. Moreover, a Sturmian word has a unique directive word if and only if its (normalized) directive word is regular wavy. ∎

As pointed out in [63], Proposition 4.14 shows a great difference between Sturmian words and episturmian words constructed over alphabets with at least three letters. Indeed, when considering words over a ternary alphabet, one can find episturmian words having exactly m m directive words for any m ≥ 1 m\geq 1. For instance, the episturmian word 𝐭 \mathbf{t} directed by Δ ˘ = a ​ ( b ​ a ¯) m − 1 ​ b ​ c ¯ ​ ( a ​ b ​ c ¯) ω \breve{\Delta}=a(b\bar{a})^{m-1}b\bar{c}(ab\bar{c})^{\omega} has exactly m m directive words, namely ( a ¯ ​ b ¯) i ​ a ​ ( b ​ a ¯) j ​ b ​ c ¯ ​ ( a ​ b ​ c ¯) ω (\bar{a}\bar{b})^{i}a(b\bar{a})^{j}b\bar{c}(ab\bar{c})^{\omega} with i + j = m − 1 i+j=m-1. Notice that the suffix b ​ c ¯ ​ ( a ​ b ​ c ¯) ω b\bar{c}(ab\bar{c})^{\omega} of Δ ˘ \breve{\Delta} is regular wavy, and the other m − 1 m-1 spinned versions of Δ \Delta that also direct 𝐭 \mathbf{t} arise from the m − 1 m-1 words that are block-equivalent to the prefix a ​ ( b ​ a ¯) m − 1 a(b\bar{a})^{m-1}.

### 4.4 Periodic and purely morphic episturmian words

We are now ready to describe periodic and purely morphic episturmian words.

Recall from Remark 2.7 that the periodic episturmian words correspond to | Ult ⁡ ( Δ) | = 1 |\mathrm{Ult}(\Delta)|=1. The following theorem gives the form of such words in terms of pure episturmian morphisms.

###### Theorem 4.15.

[73] An episturmian word is periodic if and only if it is ( μ w ˘ ​ ( x)) ω (\mu_{\breve{w}}(x))^{\omega} for some spinned finite word w ˘ \breve{w} and letter x x. ∎

For example, ( μ a ​ b ¯ ​ ( c)) ω = ( a ​ c ​ a ​ b) ω (\mu_{a\bar{b}}(c))^{\omega}=(acab)^{\omega} is the periodic episturmian word directed by a ​ b ¯ ​ c ω a\bar{b}c^{\omega} (in fact, it is epistandard as it is also directed by a ​ c ​ b ω acb^{\omega}).

The next theorem characterizes purely morphic episturmian words with respect to their directive words.

###### Theorem 4.16.

[73, Theorem 3.14] An aperiodic episturmian word is purely morphic (i.e., generated by a morphism) if and only if it is directed by a periodic spinned infinite word Δ ˘ = ( f ˘) ω \breve{\Delta}=(\breve{f})^{\omega} for some spinned word f ˘ \breve{f}. Moreover it can be generated by μ f ˘ \mu_{\breve{f}}. ∎

We observe from Theorem 4.16 that any purely morphic episturmian word is strict (i.e., an Arnoux-Rauzy sequence) as Ult ⁡ ( Δ) = Alph ​ ( f) = Alph ​ ( Δ) \mathrm{Ult}(\Delta)=\textrm{Alph}(f)=\textrm{Alph}(\Delta). The proof of this theorem makes use of Proposition 4.3 and Theorem 3.9.

###### Example 4.17.

The Tribonacci word is generated by μ a ​ b ​ c \mu_{abc}. Notice that μ a ​ b ​ c = σ 3 \mu_{abc}=\sigma^{3} where σ \sigma is the Tribonacci morphism defined by σ: ( a, b, c) ↦ ( a ​ b, a ​ c, a) \sigma:(a,b,c)\mapsto(ab,ac,a).

###### Remark 4.18.

Purely morphic standard Sturmian words were previously characterized independently in the following papers: [16, 38, 77]. Yasutomi [118] has since established a characterization of all purely morphic Sturmian words with respect to their slopes and intercepts (when viewed as cutting sequences). An alternative geometric proof of Yasutomi’s result was recently given by Berthé et al. in [21].

Using the notion of block-equivalence, Justin and Pirillo [75] explicitly determined which shifts, if any, of a purely morphic episturmian word are also purely morphic.

###### Theorem 4.19.

[75] If an episturmian word 𝐭 \mathbf{t} is purely morphic, then its shift T i ​ ( 𝐭) \mathrm{T}^{i}(\mathbf{t}) is also purely morphic if and only if i i belongs to some particular interval. ∎

See Section 4 of [75] for specific (and very technical) details.

###### Example 4.20.

For the Tribonacci word 𝐫 \mathbf{r}, only itself and T − 1 ​ ( 𝐫) \mathrm{T}^{-1}(\mathbf{r}) are purely morphic. Note that T − 1 ​ ( 𝐫) \mathrm{T}^{-1}(\mathbf{r}) corresponds to three episturmian words: a ​ 𝐫 a\mathbf{r}, b ​ 𝐫 b\mathbf{r}, c ​ 𝐫 c\mathbf{r}, directed by ( a ​ b ¯ ​ c ¯) ω (a\bar{b}\bar{c})^{\omega}, ( a ¯ ​ b ​ c ¯) ω (\bar{a}b\bar{c})^{\omega}, ( a ¯ ​ b ¯ ​ c) ω (\bar{a}\bar{b}c)^{\omega}, respectively.

###### Remark 4.21.

Theorem 4.19 corrects an error in [73, Section 5.1] where it was mistakenly said that if an episturmian word is purely morphic then any shift of it is also purely morphic. Indeed, this is false even in the Sturmian case as Fagnot [48] has shown that if 𝐬 \mathbf{s} is a purely morphic standard Sturmian word on { a, b } \{a,b\}, then a ​ 𝐬 a\mathbf{s}, b ​ 𝐬 b\mathbf{s}, a ​ b ​ 𝐬 ab\mathbf{s}, b ​ a ​ 𝐬 ba\mathbf{s} (which are purely morphic [17]) are the only purely morphic Sturmian words related to 𝐬 \mathbf{s} by a shift.

## 5 Arnoux-Rauzy sequences

We now briefly turn our attention to Arnoux-Rauzy sequences since their combinatorial properties are also considered in the sections that follow.

Arnoux-Rauzy sequences are uniformly recurrent infinite words over a finite alphabet 𝒜 \mathcal{A} with factor complexity ( | 𝒜 | − 1) ​ n + 1 (|\mathcal{A}|-1)n+1 for each n ∈ ℕ n\in\mathbb{N}, and exactly one right and one left special factor of each length. They were introduced by Arnoux and Rauzy [97, 12], who studied them using Rauzy graphs, with particular emphasis on the case | 𝒜 | = 3 |\mathcal{A}|=3. (Note that the foregoing definition is equivalent to the one given in the introduction.)

As mentioned previously (in Section 2.3), Arnoux-Rauzy sequences are exactly the strict episturmian words; in particular, any episturmian word has the form φ ⁡ ( 𝐭) \varphi(\mathbf{t}) with φ \varphi an episturmian morphism and 𝐭 \mathbf{t} an Arnoux-Rauzy sequence. In this sense, episturmian words are only a slight generalization of Arnoux-Rauzy sequences. For example, the family of episturmian words on three letters { a, b, c } \{a,b,c\} consists of the Arnoux-Rauzy sequences over { a, b, c } \{a,b,c\}, the Sturmian words over { a, b } \{a,b\}, { b, c } \{b,c\}, { a, c } \{a,c\} and their images under episturmian morphisms on { a, b, c } \{a,b,c\}, and periodic infinite words of the form φ ​ ( x) ω \varphi(x)^{\omega} where φ \varphi is an episturmian morphism on { a, b, c } \{a,b,c\} and x ∈ { a, b, c } x\in\{a,b,c\}.

Arnoux-Rauzy sequences have deep properties studied in the framework of dynamical systems, with connections to geometrical realizations such as Rauzy fractals [11] and interval exchanges. When | 𝒜 | = 3 |\mathcal{A}|=3, the condition on the special factors distinguishes Arnoux-Rauzy sequences from other infinite words of complexity 2 ​ n + 1 2n+1, such as those obtained by coding trajectories of 3 3 -interval exchange transformations (e.g., see [51]). In [12], it was shown how Arnoux-Rauzy sequences of complexity 2 ​ n + 1 2n+1 (i.e., the 3 3 -strict episturmian words) can be geometrically realized by an exchange of six intervals on the unit circle, which generalizes the representation of Sturmian sequences by rotations.

An alternative way of introducing and studying Arnoux-Rauzy sequences is in the context of S S -adic dynamical systems, as done in [105] for instance (see our remarks following Theorem 3.3 in Section 3.2). In [40], Damanik and Zamboni give a kind of survey on this approach by considering Arnoux-Rauzy subshifts and answering various combinatorial questions concerning linear recurrence, maximal powers of factors, and the number of palindromes of a given length. They also present some applications of their results to the spectral theory of discrete one-dimensional Schr o ¨ \ddot{\textrm{o}} dinger operators with potentials given by Arnoux-Rauzy sequences.

Arnoux-Rauzy sequences also have interesting arithmetical properties. For instance, if one considers the frequencies of letters (as discussed later in Section 6.4), they are well-defined, and renormalization by an episturmian morphism leads to a generalization of the continued fraction algorithm that associates to each k k -letter Arnoux-Rauzy sequence an infinite array of k × k k\times k rational numbers. In the special case k = 2 k=2, these fractions are consecutive Farey numbers arising from the continued fraction expansion of the frequencies of the two letters. More generally, given an Arnoux-Rauzy sequence on k k -letters, its directive word is determined by the ‘multi-dimensional’ continued fraction expansion of the frequencies of the first k − 1 k-1 letters. Unfortunately, this generalized algorithm (except for the case k = 2 k=2 when it is exactly the usual continued fraction algorithm) is only defined on a set of measure zero in ℝ k − 1 \mathbb{R}^{k-1}. This reduces its interest and explains why it has not been appropriately studied since its inception (see Sections 6.2.1 and 6.4 for further details). Nonetheless, a nice arithmetical characterization of 3 3 -letter Arnoux-Rauzy sequences can be given, as follows. We say that a triple ( a, b, c) (a,b,c) does not satisfy the triangular inequality if one of the coordinates is larger than the sum of the other two (e.g., a > b + c a>b+c). ÊIn that case, we can renormalize in a unique way to obtain the triple ( a − b − c, b, c) (a-b-c,b,c) satisfying the triangular inequality. The set of allowable frequencies for 3 3 -letter Arnouxy-Rauzy sequences is exactly the set of triples ( a, b, c) (a,b,c) that can be infinitely renormalized, each time to a triple that does not satisfy the triangular inequality (see [12]). The resulting picture exhibits a kind of Sierpinski carpet.

For further details on Arnoux-Rauzy sequences, we refer the reader to the interesting survey [22] in which Berthé, Ferenczi, and Zamboni discuss connections between Arnoux-Rauzy sequences and rotations of the 2 2 -torus; coding of two-dimensional actions and two-dimensional Sturmian words; and interval exchanges and sequences of low complexity. See also [35], Section 12.2.3 in [96], and J. Berstel’s nice survey paper [15] in which he compares some combinatorial properties of Arnoux-Rauzy sequences (as well as episturmian words) to those of Sturmian words.

### 5.1 Finite Arnoux-Rauzy words

A finite word w w is said to be *finite episturmian*if w w is a factor of some infinite episturmian word. When considering factors of (infinite) episturmian words, it suffices to consider only the strict standard ones (i.e., the standard Arnoux-Rauzy sequences). Indeed, for any prefix u u of an epistandard word, there exists a strict epistandard word also having u u as a prefix. In particular, the words μ w ​ ( x) \mu_{w}(x), with w ∈ 𝒜 ∗ w\in\mathcal{A}^{*} and x ∈ 𝒜 x\in\mathcal{A}, are the standard ones ( cf. standard words, e.g., [83, Chapter 2]). They can be obtained by the Rauzy rules [98] (see also [43, Theorem 8]), and this has a strong connection with the set of periods of the palindromes u n + 1 = P a l ( x 1 ⋯ x n) u_{n+1}=Pal(x_{1}\cdots x_{n}) (given in Theorem 2.3) and the Euclidean algorithm. This relation was studied by Castelli, Mignosi, and Restivo [34], who extended the well-known Fine and Wilf Theorem [82] to words having three periods. Justin [70] generalized this result even further to words having an arbitrary number of periods, which led to a characterization of finite episturmian words.

Finite episturmian words are exactly the finite Arnoux-Rauzy words. Such words were enumerated by Mignosi and Zamboni [88], who described a multi-dimensional generalization of the Euler phi-function that counts the number of finite Arnoux-Rauzy words of each length. Finite episturmian words have also been characterized with respect to lexicographic orderings in [62] (see Theorem 7.5 later).

## 6 Some properties of factors

### 6.1 Factor complexity

As mentioned previously, any k k -strict episturmian word has complexity ( k − 1) ​ n + 1 (k-1)n+1 for all n ∈ ℕ n\in\mathbb{N}. More generally:

###### Theorem 6.1.

[43, Theorem 7] Suppose 𝐭 \mathbf{t} is an episturmian word directed by Δ ˘ \breve{\Delta} with | Ult ⁡ ( Δ) | > 1 |\mathrm{Ult}(\Delta)|>1. Then, for n n large enough, 𝐭 \mathbf{t} has complexity ( k − 1) ​ n + q (k-1)n+q for some q ∈ ℕ + q\in\mathbb{N}^{+}, where k = | Ult ⁡ ( Δ) | k=|\mathrm{Ult}(\Delta)|. ∎

This theorem can be easily deduced from the fact that for sufficiently large n n, any left special factor of 𝐭 \mathbf{t} of length at least n n has exactly k = | Ult ⁡ ( Δ) | k=|\mathrm{Ult}(\Delta)| different left extensions in 𝐭 \mathbf{t} (by Theorem 6 in [43]).

### 6.2 Palindromic factors

The palindromic complexity of episturmian words was established in [73] by carrying out a similar study to the one for Sturmian words in [44].

###### Theorem 6.2.

[73, Theorem 4.4] If 𝐭 \mathbf{t} is an 𝒜 \mathcal{A} -strict episturmian word, then there exists exactly

- •

one palindrome of length n n for all even n n,

- •

one palindrome of length n n and centre x x for all odd n n and x ∈ 𝒜 x\in\mathcal{A}. ∎

As shown in [44], the above property is characteristic in the Sturmian case, but not when 𝒜 \mathcal{A} contains more than two letters because it also holds for billiard words, which are not episturmian (see Borel and Reutenauer [25]).

###### Theorem 6.3.

[73, Section 4.2] If 𝐭 \mathbf{t} is episturmian, then there exist | Ult ⁡ ( Δ) | + 1 |\mathrm{Ult}(\Delta)|+1 bi-infinite episturmian words of the form 𝐦 ~. 𝐦 \tilde{\mathbf{m}}.\mathbf{m} and 𝐦 ~ ​ x ​ 𝐦 \tilde{\mathbf{m}}x\mathbf{m} with x ∈ Ult ⁡ ( Δ) x\in\mathrm{Ult}(\Delta) giving the palindromic factors of 𝐭 \mathbf{t}. The spinned versions of Δ \Delta directing these bi-infinite episturmian words can be easily constructed via a simple algorithm. ∎

For more precise technical details, see Section 4.2 in [73].

###### Example 6.4.

For the Tribonacci word, 𝐫 ~. 𝐫 \tilde{\mathbf{r}}.\mathbf{r} is directed by ( a ​ b ​ c ​ a ¯ ​ b ​ c ​ a ​ b ¯ ​ c ​ a ​ b ​ c ¯) ω (abc\bar{a}bca\bar{b}cab\bar{c})^{\omega}.

#### 6.2.1 Iterated palindromic closure

In [105], Risley and Zamboni gave an alternative construction of the sequence ( u n) n ≥ 1 (u_{n})_{n\geq 1} of palindromic prefixes of an epistandard word (where u 1 = ε u_{1}=\varepsilon and u i + 1 = P a l ( x 1 ⋯ x i) u_{i+1}=Pal(x_{1}\cdots x_{i}) for all i ≥ 1 i\geq 1), using a ‘hat operation’ as opposed to palindromic closure. The so-called hat operation is defined as follows. We construct a new alphabet 𝒜 ′:= 𝒜 ∪ 𝒜 ^ \mathcal{A}^{\prime}:=\mathcal{A}\cup\widehat{\mathcal{A}} where 𝒜 ^ = { x ^ | x ∈ 𝒜 } \widehat{\mathcal{A}}=\{\widehat{x}~|~x\in\mathcal{A}\} and denote by ϕ \phi the morphism ϕ: 𝒜 ′ → 𝒜 \phi:\mathcal{A}^{\prime}\to\mathcal{A} defined by ϕ ⁡ ( x) = ϕ ⁡ ( x ^) = x \phi(x)=\phi(\widehat{x})=x for all letters x ∈ 𝒜 x\in\mathcal{A}. The morphism ϕ \phi extends to a morphism (also denoted by ϕ \phi) from words over 𝒜 ′ \mathcal{A}^{\prime} to words over 𝒜 \mathcal{A}. Now, from a given directive word Δ = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega}, we construct a sequence of words ( p i) i ≥ 1 (p_{i})_{i\geq 1} as follows. We begin with p 1 = ε p_{1}=\varepsilon and p 2 = x ^ 1 p_{2}=\widehat{x}_{1}. Then, for n ≥ 2 n\geq 2, p n + 1 p_{n+1} is obtained from p n p_{n} according to the rule: if x ^ n \widehat{x}_{n} does not occur in p n p_{n}, then p n + 1 = p n ​ x ^ n ​ ϕ ​ ( p n) p_{n+1}=p_{n}\widehat{x}_{n}\phi(p_{n}); otherwise p n + 1 = p n ​ x ^ n ​ ϕ ​ ( s n) p_{n+1}=p_{n}\widehat{x}_{n}\phi(s_{n}), where s n s_{n} is the longest palindromic suffix of p n p_{n} containing no occurrence of x ^ n \widehat{x}_{n}.

###### Example 6.5.

Let Δ = ( a ​ b ​ c) ω \Delta=(abc)^{\omega}. Then using the hat operation, we obtain:

 | p 1 \displaystyle p_{1} | = \displaystyle= | ε \displaystyle\varepsilon |  |

 | p 2 \displaystyle p_{2} | = \displaystyle= | a ^ \displaystyle\hat{a} |  |

 | p 3 \displaystyle p_{3} | = \displaystyle= | a ^ ​ b ^ ​ a \displaystyle\hat{a}\hat{b}a |  |

 | p 4 \displaystyle p_{4} | = \displaystyle= | a ^ ​ b ^ ​ a ​ c ^ ​ a ​ b ​ a \displaystyle\hat{a}\hat{b}a\hat{c}aba |  |

 | p 5 \displaystyle p_{5} | = \displaystyle= | a ^ ​ b ^ ​ a ​ c ^ ​ a ​ b ​ a ​ a ^ ​ b ​ a ​ c ​ a ​ b ​ a \displaystyle\hat{a}\hat{b}a\hat{c}aba\hat{a}bacaba |  |

 | p 6 \displaystyle p_{6} | = \displaystyle= | a ^ ​ b ^ ​ a ​ c ^ ​ a ​ b ​ a ​ a ^ ​ b ​ a ​ c ​ a ​ b ​ a ​ b ^ ​ a ​ c ​ a ​ b ​ a ​ a ​ b ​ a ​ c ​ a ​ b ​ a \displaystyle\hat{a}\hat{b}a\hat{c}aba\hat{a}bacaba\hat{b}acabaabacaba |  |

Now removing all hats (by applying ϕ \phi), we see that the p i p_{i} ’s are precisely the palindromic prefixes of the Tribonacci word: a b a c a b a a b a c a b a b a c a b a a b a c a b a ⋯ abacabaabacababacabaabacaba\cdots.

As demonstrated by the above example, the hat operation is clearly the same as iterated palindromic closure; in fact, the relationship between these two constructions is evident by formula ( 4.1), which we now rewrite as:

 | P a l ( x 1 ⋯ x n) = μ x 1 ⋯ x n − 1 ( x n) P a l ( x 1 ⋯ x n − 1) for n > 0. Pal(x_{1}\cdots x_{n})=\mu_{x_{1}\cdots x_{n-1}}(x_{n})Pal(x_{1}\cdots x_{n-1})\hskip 10.00002pt\mbox{for $n>0$}. |  |

The above formula is actually a special case of formula (3) from [71], which also happens to be formula (3) in [73], namely:

 | P ​ a ​ l ​ ( v ​ w) = μ v ​ ( P ​ a ​ l ​ ( w)) ​ P ​ a ​ l ​ ( v) for any words w, v. Pal(vw)=\mu_{v}(Pal(w))Pal(v)\hskip 10.00002pt\mbox{for any words $w$, $v$}. |  | (6.1) |

This formula is commonly referred to as Justin’s Formula, from which we deduce the following two special cases:

 | P ​ a ​ l ​ ( x ​ w) = ψ x ​ ( P ​ a ​ l ​ ( w)) ​ x and P ​ a ​ l ​ ( w ​ x) = μ w ​ ( x) ​ P ​ a ​ l ​ ( w) for any word v and letter x. Pal(xw)=\psi_{x}(Pal(w))x\hskip 10.00002pt\mbox{and}\hskip 10.00002ptPal(wx)=\mu_{w}(x)Pal(w)\hskip 10.00002pt\mbox{for any word $v$ and letter $x$. } |  | (6.2) |

The first formula given in ( 6.2) tells us that P ​ a ​ l ​ ( x ​ w) Pal(xw) is obtained from P ​ a ​ l ​ ( w) Pal(w) simply by inserting the letter x x before each letter different from x x and then appending x x to the resulting word. For example, P ​ a ​ l ​ ( b ​ c) = b ​ c ​ b Pal(bc)=bcb and P ​ a ​ l ​ ( a ​ b ​ c) = a ​ b ​ a ​ c ​ a ​ b ​ a Pal(abc)=abacaba. The second formula given in ( 6.2) provides another way to compute the palindromic right-closure of w ​ x wx by placing the finite epistandard word μ w ​ ( x) \mu_{w}(x) in front of P ​ a ​ l ​ ( w) Pal(w). For example, to compute P ​ a ​ l ​ ( a ​ b ​ c ​ b) Pal(abcb) we need only compute the words μ a ​ b ​ c ​ ( b) = a ​ b ​ a ​ c ​ a ​ b \mu_{abc}(b)=abacab and P ​ a ​ l ​ ( a ​ b ​ c) = a ​ b ​ a ​ c ​ a ​ b ​ a Pal(abc)=abacaba, and then we have:

 | P ​ a ​ l ​ ( a ​ b ​ c ​ b) = μ a ​ b ​ c ​ ( a) ​ P ​ a ​ l ​ ( a ​ b ​ c) = a ​ b ​ a ​ c ​ a ​ b ⋅ a ​ b ​ a ​ c ​ a ​ b ​ a. Pal(abcb)=\mu_{abc}(a)Pal(abc)=abacab\cdot abacaba. |  |

In [71], Justin established some relations between the words P ​ a ​ l ​ ( w) Pal(w), μ w \mu_{w}, P ​ a ​ l ​ ( w ~) Pal(\widetilde{w}), and μ w ~ \mu_{\widetilde{w}} where w w is any finite word. Moreover, he showed that his results can be explained by the similarity of the incidence matrices of μ w \mu_{w} and μ w ~ \mu_{\widetilde{w}}. One curious result is that | P ​ a ​ l ​ ( w) | = | P ​ a ​ l ​ ( w ~) | |Pal(w)|=|Pal(\tilde{w})|. For example, with w = a ​ b ​ a ​ c w=abac, P ​ a ​ l ​ ( w) = a ​ b ​ a ​ a ​ b ​ a ​ c ​ a ​ b ​ a ​ a ​ b ​ a Pal(w)=abaabacabaaba and P ​ a ​ l ​ ( w ~) = c ​ a ​ c ​ b ​ c ​ a ​ c ​ a ​ c ​ a ​ c ​ b ​ c ​ a ​ c Pal(\widetilde{w})=cacbcacacacbcac, both of length 15 15.

Applying his results to a 2-letter alphabet, Justin [71] gave a new proof of a Galois theorem on continued fractions, by considering the epistandard words that are fixed points of μ w \mu_{w} and μ w ~ \mu_{\widetilde{w}} for any finite word w w. From this point of view, Justin’s result highlights the relevance of the previously mentioned ‘multi-dimensional’ continued fraction algorithm, proposed by Zamboni [119, 117] (see also [96, Section 12.2]). However, there still remains much work to be done in this direction, especially concerning the generalized intercept (coherent with the Sturmian case) introduced in [73, Section 5.4] and the generalized Ostrowski numeration systems [20, 75] (recall Remark 4.7).

###### Note.

The aforementioned Galois theorem was used in the theory of Sturmian words to characterize so-called Sturm numbers (see [83, Theorem 2.3.26]).

#### 6.2.2 Palindromic richness

In [43], Droubay, Justin, and Pirillo observed that any finite word w w contains at most | w | + 1 |w|+1 distinct palindromes (including the empty word). Even further, they proved that a word w w contains exactly | w | + 1 |w|+1 distinct palindromes if and only if the longest palindromic suffix of any prefix p p of w w occurs exactly once in p p (i.e., every prefix of w w has Property J ​ u Ju [43]). Such words are ‘rich’ in palindromes in the sense that they contain the maximum number of different palindromic factors. Accordingly, we say that a finite word w w is rich if it contains exactly | w | + 1 |w|+1 distinct palindromes (or equivalently, if every prefix of w w has Property J ​ u Ju). For example, a ​ b ​ a ​ c abac is rich since it is of length 4 4 and contains the following five palindromes: ε \varepsilon, a a, b b, c c, a ​ b ​ a aba. Naturally, an infinite word is rich if all of its factors are rich. For example, the periodic infinite words a ω = a a a ⋯ a^{\omega}=aaa\cdots and ( a b) ω = a b a b a b ⋯ (ab)^{\omega}=ababab\cdots are clearly rich, whereas ( a b c) ω = a b c a b a c a b c ⋯ (abc)^{\omega}=abcabacabc\cdots is not rich since it contains the non-rich word a ​ b ​ c ​ a abca.

Droubay et al. [43] showed that all finite and infinite episturmian words are rich. Specifically, they proved that if an infinite word has property P ​ i Pi (and hence is epistandard – see Theorem 2.3), then all of its prefixes have property J ​ u Ju. Consequently, any factor u u of an epistandard word (and hence, of an episturmian word) contains exactly | u | + 1 |u|+1 distinct palindromes, and is therefore rich (see Corollary 2 in [43]).

Another special class of rich words the encompasses the episturmian words consists of Fischler’s sequences with “abundant palindromic prefixes”. These words were introduced and studied in [54, 55] in the context of Diophantine approximation. See also papers by Adamczewski and Bugeaud [2, 3] concerning the transcendence of certain real numbers whose sequences of partial quotients contain arbitrarily long palindromes.

The theory of rich words has recently been further developed in a series of papers [61, 29, 42, 30]. In independent work, Ambrož, Frougny, Masáková, and Pelantová [8] have considered the same class of words which they call full words, following the earlier work of Brlek, Hamel, Nivat, and Reutenauer in [26].

### 6.3 Fractional powers & critical exponent

The study of fractional powers occurring in Sturmian words has been a topic of growing interest in recent times. See for instance [14, 23, 39, 72, 86, 111], as well as [73, 105, 59] for similar results concerning episturmian words and Arnoux-Rauzy sequences.

The following theorem extends the results in [72] on fractional powers in Sturmian words. Throughout this section, we let 𝐬 \mathbf{s} denote an epistandard word with directive word Δ = x 1 x 2 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}\cdots\in\mathcal{A}^{\omega} (as usual), and for all n ≥ 1 n\geq 1, we denote by u n + 1 u_{n+1} the palindromic prefix P a l ( x 1 ⋯ x n) Pal(x_{1}\cdots x_{n}) of 𝐬 \mathbf{s} given in Theorem 2.3. As in [72], we denote by L ⁡ ( m) L(m) the length of the longest factor v ∈ F ⁡ ( 𝐬) v\in F(\mathbf{s}) having period m ∈ ℕ m\in\mathbb{N}, and write L ⁡ ( m) = e ​ m + r L(m)=em+r, e ∈ ℕ + e\in\mathbb{N}^{+}, 0 ≤ r < m 0\leq r<m. Given a finite or infinite word w w, we denote by w ⁡ ( i) w(i) (resp. w ⁡ ( i, j) w(i,j)) the letter in position i i of w w (resp. the factor of w w beginning at position i i and ending at position j j).

When L ⁡ ( m) ≥ 2 ​ m L(m)\geq 2m, all factors of 𝐬 \mathbf{s} having period m m and length L ⁡ ( m) L(m) are equal to a palindrome v v, and for 0 ≤ i < e 0\leq i<e, the word v i:= v ⁡ ( 1, i ​ m + r) v_{i}:=v(1,im+r) is a palindromic prefix of 𝐬 \mathbf{s} by Lemma 4.1 in [73]. Moreover, with the preceding notation, we have:

###### Theorem 6.6.

[73, Theorem 4.2] Let m m, n ∈ ℕ n\in\mathbb{N} be such that | u n | < m ≤ | u n + 1 | |u_{n}|<m\leq|u_{n+1}| and 𝐬 ⁡ ( 1, m) = w \mathbf{s}(1,m)=w is primitive with 𝐬 ⁡ ( m) = x \mathbf{s}(m)=x occurring in 𝐬 ⁡ ( 1, m − 1) \mathbf{s}(1,m-1). Then the following properties hold.

1. i)

L ⁡ ( m) ≥ 2 ​ m L(m)\geq 2m if and only if w = μ x 1 ⋯ x n ( x) w=\mu_{x_{1}\cdots x_{n}}(x) and x ∈ Alph ( x n + 1 x n + 2 ⋯) x\in\mbox{{Alph}}(x_{n+1}x_{n+2}\cdots).

2. ii)

Suppose L ⁡ ( m) ≥ 2 L(m)\geq 2 and define p = max ⁡ { i ≤ n | x i = x } p=\max\{i\leq n~|~x_{i}=x\} and t = min ⁡ { j ∈ ℕ + | x n + j ≠ x } t=\min\{j\in\mathbb{N}^{+}~|~x_{n+j}\neq x\}. Then u n + 1 = w t ​ u p u_{n+1}=w^{t}u_{p} is the longest prefix of 𝐬 \mathbf{s} having period m m. Moreover, if x ∈ Alph ( x n + t + 1 x n + t + 2 ⋯) x\in\mbox{{Alph}}(x_{n+t+1}x_{n+t+2}\cdots), then e = t + 1 e=t+1; that is, v = w t + 1 ​ u p v=w^{t+1}u_{p}, otherwise e = t e=t and v = w t ​ u p v=w^{t}u_{p}. ∎

###### Remark 6.7.

Let us mention a few noteworthy facts.

- •

Exponents of powers in 𝐬 \mathbf{s} are bounded if and only if exponents of letters in Δ \Delta are bounded [105, 73].

- •

Any Sturmian word has square prefixes and so do epistandard words [5, 105].

- •

Any episturmian word has infinitely many prefixes of the form u ​ v 2 uv^{2} with | u | / | v | |u|/|v| bounded above.

The latter fact is readily deduced from the following result of Risley and Zamboni [105].

###### Theorem 6.8.

[105, Prop. I.3] If 𝐭 \mathbf{t} is an Arnoux-Rauzy sequence, then there exists a positive number ϵ \epsilon such that 𝐭 \mathbf{t} begins with infinitely many blocks of the form U ​ V ​ V ​ V ′ UVVV^{\prime}, where V ′ V^{\prime} is a prefix of V V and min ⁡ { | V ′ | / | V |, | V | / | U | } > ϵ \min\{|V^{\prime}|/|V|,|V|/|U|\}>\epsilon. ∎

###### Note.

Such a result is motivated by transcendence issues; see for instance [52].

When 𝐬 \mathbf{s} is purely morphic, it is possible to give a rather explicit formula for the critical exponent: γ = lim sup n → ∞ L ⁡ ( m) / m \gamma=\limsup_{n\rightarrow\infty}L(m)/m, as follows.

###### Notation.

Let P P be the function defined by P ⁡ ( n) = sup { i < n | x i = x n } P(n)=\sup\{i<n~|~x_{i}=x_{n}\} if this integer exists, undefined otherwise. That is, if x n = a x_{n}=a, then P ⁡ ( n) P(n) is the position of the right-most occurrence of the letter a a in the prefix x 1 x 2 ⋯ x n − 1 x_{1}x_{2}\cdots x_{n-1} of the directive word Δ = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega}.

###### Theorem 6.9.

[73, Theorem 5.2] Let 𝐬 \mathbf{s} be an 𝒜 \mathcal{A} -strict epistandard word generated by a morphism with directive word Δ \Delta having period q q. Further, let l ∈ ℕ l\in\mathbb{N} be maximal such that y l ∈ F ⁡ ( Δ) y^{l}\in F(\Delta) for some letter y y, and define L = { r, 0 ≤ r < q | x r + 1 = x r + 2 = ⋯ = x r + l } L=\{r,0\leq r<q~|~x_{r+1}=x_{r+2}=\cdots=x_{r+l}\} and d ⁡ ( r) = r + q + 1 − P ⁡ ( r + q − 1) d(r)=r+q+1-P(r+q-1) for 0 ≤ r < q 0\leq r<q. Then the critical exponent for 𝐬 \mathbf{s} is given by

 | γ = l + 2 + sup r ∈ L { lim i → ∞ | u r + i ​ q + 1 − d ⁡ ( r) | / | h r + i ​ q | }. \gamma=l+2+\sup_{r\in L}\left\{\lim_{i\rightarrow\infty}|u_{r+iq+1-d(r)}|/|h_{r+iq}|\right\}. |  |

Moreover, for any letter x x in 𝐬 \mathbf{s} the limit above can be obtained as a rational function with rational coefficients of the frequency α x \alpha_{x} of this letter. ∎

See also [86, 107, 111] for results on the critical exponent for the Fibonacci word, Tribonacci word, and Sturmian words, respectively.

###### Example 6.10.

For the ever-so popular Fibonacci word 𝐟 \mathbf{f}, directed by ( a ​ b) ω (ab)^{\omega}, we have q = 2 q=2, l = 1 l=1, d ⁡ ( 0) = d ⁡ ( 1) = 2 d(0)=d(1)=2. Hence, since | u n − 1 | / | h n | |u_{n-1}|/|h_{n}| has limit 1 / φ 1/\varphi where φ = ( 1 + 5) / 2 \varphi=(1+\sqrt{5})/2 is the golden ratio, we obtain the well-known value 2 + φ 2+\varphi for the critical exponent, originally proved by Mignosi and Pirillo [86].

More generally, the k k -bonacci word, directed by ( a 1 a 2 ⋯ a k) ω (a_{1}a_{2}\cdots a_{k})^{\omega}, has critical exponent 2 + 1 / ( φ k − 1) 2+1/(\varphi_{k}-1), where the k k -bonacci constant φ k \varphi_{k} is the (unique) positive real root of the k k -th degree monic polynomial x k − x k − 1 − ⋯ − x − 1 x^{k}-x^{k-1}-\cdots-x-1.

### 6.4 Frequencies

Let w w be a non-empty finite word. For any v ∈ F ⁡ ( w) v\in F(w), the frequency of v v in w w is | w | v / | w | |w|_{v}/|w| where | w | v |w|_{v} denotes the number of distinct occurrences of v v in w w. The notion of frequency can be extended to infinite words in two ways, as follows.

###### Definition 6.11.

Suppose v v is a non-empty factor of an infinite word 𝐱 \mathbf{x}. Then:

1. i)

the frequency of v v in 𝐱 \mathbf{x} in the weak sense is lim n → ∞ | w ⁡ ( 1, n) | v / n \lim_{n\rightarrow\infty}|w(1,n)|_{v}/n if this limit exists;

2. ii)

v v has frequency α v \alpha_{v} in 𝐱 \mathbf{x} in the strong sense if, for any sequence ( w n) n ≥ 0 (w_{n})_{n\geq 0} of factors of 𝐱 \mathbf{x} with increasing lengths, we have α v = lim n → ∞ | w n | v / | w n | \alpha_{v}=\lim_{n\rightarrow\infty}|w_{n}|_{v}/|w_{n}|.

In a purely combinatorial way, Justin and Pirillo [73, Section 6] proved that any factor occurring in an episturmian word has frequency in the strong sense.

Wozny and Zamboni [117] also studied frequencies (in the weak sense) for Arnoux-Rauzy sequences. Using a reformulation of a vectorial division algorithm, originally introduced in [105], they computed each allowable frequency of factors of the same length, as well as the number of factors with a given frequency. In particular, the authors of [117] gave simultaneous rational approximations of the frequencies by unreduced fractions having a common denominator. From this work, one recovers the results of Berthé [19] for Sturmian words in terms of Farey approximations arising from the continued fraction expansions of the frequencies of the letters. For instance, the frequencies of factors of the same length in a Sturmian word assume at most three values, which were explicitly given by Berthé [19], who also discovered that this result is in strong connection with the three distance theorem in Diophantine analysis.

### 6.5 Return words

Let us now recall the notion of a return word, which was introduced independently by Durand [45], and Holton and Zamboni [67] when studying primitive substitutive sequences.

###### Definition 6.12.

Let v v be a recurrent factor of 𝐲 ∈ 𝒜 ω \mathbf{y}\in\mathcal{A}^{\omega}, starting at positions n 1 < n 2 < n 3 ⋯ n_{1}<n_{2}<n_{3}\cdots. Then each word r i = y n i y n i + 1 ⋯ y n i + 1 − 1 r_{i}=y_{n_{i}}y_{n_{i}+1}\cdots y_{n_{i+1}-1} is called a return to v v in 𝐲 \mathbf{y}. Moreover, 𝐲 \mathbf{y} can be factorized in a unique way as 𝐲 = y 1 ⋯ y n 1 − 1 r 1 r 2 r 3 ⋯ \mathbf{y}=y_{1}\cdots y_{n_{1}-1}r_{1}r_{2}r_{3}\cdots where r 1 r 2 r 3 ⋯ r_{1}r_{2}r_{3}\cdots, viewed as a word on the r i r_{i}, is called the derived word of 𝐲 \mathbf{y} with respect to v v.

That is, a return to v v in 𝐲 \mathbf{y} is a non-empty factor of 𝐲 \mathbf{y} beginning at an occurrence of v v and ending exactly before the next occurrence of v v in 𝐲 \mathbf{y}. Thus, if r r is a return to v v in 𝐲 \mathbf{y}, then r ​ v rv is a factor of 𝐲 \mathbf{y} that contains exactly two occurrences of v v, one as a prefix and one as a suffix. We call r ​ v rv a complete return to v v [76].

Return words play an important role in the study of minimal subshifts in symbolic dynamics; see for instance [45, 46, 47, 53, 106]. In the context of episturmian words, such words have recently proven to be a useful tool in the study of quasiperiodicity (see Section 8 for further details). This latest work made use of the following result of Justin and Vuillon [76] which completely describes the returns to any factor of an epistandard word. In fact, their result actually characterizes return words in episturmian words (not just epistandard words) since, by uniform recurrence, the returns to any factor v v in an epistandard word 𝐬 \mathbf{s} are the same as the returns to v v as a factor of any episturmian word 𝐭 \mathbf{t} having the same set of factors as 𝐬 \mathbf{s}.

###### Theorem 6.13.

[76] Let 𝐬 \mathbf{s} be an epistandard word directed by Δ = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega} and consider any v ∈ F ⁡ ( 𝐬) v\in F(\mathbf{s}). If u n + 1 u_{n+1} is the shortest palindromic prefix of 𝐬 \mathbf{s} containing v v with u n + 1 = f ​ v ​ g u_{n+1}=fvg, then the returns to v v in 𝐬 \mathbf{s} are the words f − 1 μ x 1 ⋯ x n ( x) f f^{-1}\mu_{x_{1}\cdots x_{n}}(x)f where x ∈ Alph ( x n + 1 x n + 2 ⋯) x\in\mbox{{Alph}}(x_{n+1}x_{n+2}\cdots). Moreover, the corresponding complete returns to v v are the words f − 1 ​ ( u n + 1 ​ x) ( +) ​ g − 1 f^{-1}(u_{n+1}x)^{(+)}g^{-1} and the derived word of 𝐬 \mathbf{s} with respect to v v is given by 𝐬 ( n) = μ x 1 ⋯ x n − 1 ( 𝐬) \mathbf{s}^{(n)}=\mu_{x_{1}\cdots x_{n}}^{-1}(\mathbf{s}). ∎

###### Note.

It follows immediately that any factor of an 𝒜 \mathcal{A} -strict episturmian word has exactly | 𝒜 | |\mathcal{A}| return words.

Theorem 6.13 extends earlier work of Vuillon on return words in Sturmian words (see [114]). In particular, Vuillon proved that Sturmian words are characterized by the property that any non-empty factor has exactly 2 2 different return words in the given Sturmian word. However, contrary to what one might expect, such a property with 2 2 replaced by a positive integer k ≥ 3 k\geq 3 does not characterize k k -strict episturmian words. For instance, infinite words coding 3 3 -interval exchange transformations, which constitute a different generalization of Sturmian words to 3 3 -letter alphabets, are known to have the property that every factor has 3 3 different return words (see the work by Ferenczi, Holton, and Zamboni in [51]).

## 7 Balance & lexicographic order

### 7.1 q q -Balance

###### Definition 7.1.

A finite or infinite word is q q -balanced if, for any two of its factors u u, v v with | u | = | v | |u|=|v|, we have

 | | | u | x − | ​ v | x | ≤ q for any letter x, ||u|_{x}-|v|_{x}|\leq q\hskip 10.00002pt\mbox{for any letter $x$}, |  |

i.e., the number of x x ’s in each of u u and v v differs by at most q q.

###### Note.

A 1 1 -balanced word is simply said to be balanced.

The term ‘balanced’ is relatively new; it appeared in [16, 17] (also see [83, Chapter 2]), and the notion itself dates back to [91, 37]. In the pioneering work of Morse and Hedlund [91], balanced infinite words over a 2 2 -letter alphabet were called ‘Sturmian trajectories’ and belong to three classes: aperiodic Sturmian; periodic Sturmian; and infinite words that are ultimately periodic (but not periodic), called skew words. That is, the family of balanced infinite words consists of the (recurrent) Sturmian words and the (non-recurrent) skew infinite words, the factors of which are balanced. Skew words are ultimately periodic suffixes of words of the form μ ⁡ ( a p ​ b ​ a ω) \mu(a^{p}ba^{\omega}), where μ \mu is a pure standard Sturmian morphism and p ∈ ℕ p\in\mathbb{N}. For example, a ​ b ​ a ω aba^{\omega} and ψ b ​ ( a ​ b ​ a ω) = b ​ a ​ b ​ ( b ​ a) ω \psi_{b}(aba^{\omega})=bab(ba)^{\omega} are skew. See also [108, 109, 66, 95] for further work on skew words.

###### Remark 7.2.

Nowadays, for most authors, only the aperiodic Sturmian words are considered to be ‘Sturmian’. However, from now on, we will use the term ‘Sturmian’ to refer to both aperiodic and periodic Sturmian words. In the context of cutting sequences, the aperiodic (resp. periodic) Sturmian words are precisely those with irrational slope (resp. rational slope).

It is important to note that a finite word is finite Sturmian (i.e., a factor of some Sturmian word) if and only if it is balanced [83, Chapter 2]. Accordingly, the balanced infinite words are precisely the infinite words whose factors are finite Sturmian. This concept was recently generalized in [62] by showing that the set of all infinite words whose factors are finite episturmian consists of the (recurrent) episturmian words and the (non-recurrent) episkew infinite words, as defined in the next section.

### 7.2 Episkew words

Inspired by the skew words of Morse and Hedlund [91], *episkew words*were recently defined in [62] as non-recurrent infinite words, all of whose factors are (finite) episturmian. The following theorem gives a number of equivalent definitions of such words, similar to those for (recurrent) episturmian words.

###### Theorem 7.3.

[62] An infinite word 𝐭 \mathbf{t} with Alph ( 𝐭) = 𝒜 (\mathbf{t})=\mathcal{A} is episkew if equivalently:

1. i)

𝐭 \mathbf{t} is non-recurrent and all of its factors are (finite) episturmian;

2. ii)

there exists an infinite sequence ( 𝐭 ( i)) i ≥ 0 (\mathbf{t}^{(i)})_{i\geq 0} of non-recurrent infinite words and a directive word x 1 x 2 x 3 ⋯ x_{1}x_{2}x_{3}\cdots ( x i ∈ 𝒜) (x_{i}\in\mathcal{A}) such that 𝐭 ( 0) = 𝐭 \mathbf{t}^{(0)}=\mathbf{t}, … \ldots, 𝐭 ′ ( i − 1) = ψ x i ​ ( 𝐭 ( i)) \mathbf{t}^{\prime(i-1)}=\psi_{x_{i}}(\mathbf{t}^{(i)}), where 𝐭 ′ ( i − 1) = 𝐭 ( i − 1) \mathbf{t}^{\prime(i-1)}=\mathbf{t}^{(i-1)} if 𝐭 ( i − 1) \mathbf{t}^{(i-1)} begins with x i x_{i} and 𝐭 ′ ( i − 1) = x i ​ 𝐭 ( i − 1) {\mathbf{t}^{\prime}}^{(i-1)}=x_{i}\mathbf{t}^{(i-1)} otherwise;

3. iii)

there exists a letter x ∈ 𝒜 x\in\mathcal{A} and an epistandard word 𝐬 \mathbf{s} on 𝒜 ∖ { x } \mathcal{A}\setminus\{x\} such that 𝐭 = v ​ μ ​ ( 𝐬) \mathbf{t}=v\mu(\mathbf{s}), where μ \mu is a pure epistandard morphism on 𝒜 \mathcal{A} and v v is a non-empty suffix of μ ⁡ ( 𝐬 p ~ ​ x) \mu(\widetilde{\mathbf{s}_{p}}x) for some p ∈ ℕ p\in\mathbb{N}.

Moreover, 𝐭 \mathbf{t} is said to be strict episkew if 𝐬 \mathbf{s} is strict on 𝒜 ∖ { x } \mathcal{A}\setminus\{x\}, i.e., if each letter in 𝒜 ∖ { x } \mathcal{A}\setminus\{x\} occurs infinitely often in the directive word x 1 x 2 x 3 ⋯ x_{1}x_{2}x_{3}\cdots. ∎

A simple example of an episkew word on more than two letters is the infinite word c 𝐟 = c a b a a b a b a ⋯ c\mathbf{f}=cabaababa\cdots where 𝐟 \mathbf{f} is the Fibonacci word and c c is a letter (see also Example 3.7).

Note that the episkew words on a 2 2 -letter alphabet are precisely the skew words. Certainly, in the Sturmian case, the word 𝐬 ~ p ​ x ​ 𝐬 \widetilde{\mathbf{s}}_{p}x\mathbf{s} reduces to a word of the form a p ​ b ​ a ω a^{p}ba^{\omega}.

###### Remark 7.4.

Thanks to Richomme [104], episkew words actually have the following simpler characterization: an infinite word 𝐭 \mathbf{t} is episkew if and only if 𝐭 = φ ⁡ ( x ​ 𝐬) \mathbf{t}=\varphi(x\mathbf{s}) where 𝐬 \mathbf{s} is an epistandard word, x x is a letter not occurring in 𝐬 \mathbf{s}, and φ \varphi is a pure episturmian morphism.

Episkew words were first alluded to (but not explicated) in the recent paper [60]. Following that paper, these words showed up again in the study of inequalities characterizing finite and infinite episturmian words with respect to lexicographic orderings [62]. In fact, as detailed in the next section, episturmian words have similar extremal properties to Sturmian words. See also [74, 69, 93, 94, 95, 60, 62] for other work in this direction.

### 7.3 Extremal properties

Suppose the alphabet 𝒜 \mathcal{A} is totally ordered by the relation < <. Then we can totally order 𝒜 ∗ \mathcal{A}^{*} by the *lexicographic order*≤ \leq defined as follows. Given two words u u, v ∈ 𝒜 + v\in\mathcal{A}^{+}, we have u ≤ v u\leq v if and only if either u u is a prefix of v v or u = x ​ a ​ u ′ u=xau^{\prime} and v = x ​ b ​ v ′ v=xbv^{\prime}, for some x x, u ′ u^{\prime}, v ′ ∈ 𝒜 ∗ v^{\prime}\in\mathcal{A}^{*} and letters a a, b b with a < b a<b. This is the usual alphabetic ordering in a dictionary. We write u < v u<v when u ≤ v u\leq v and u ≠ v u\neq v, in which case we say that u u is (strictly) *lexicographically smaller*than v v. The notion of lexicographic order naturally extends to infinite words in 𝒜 ω \mathcal{A}^{\omega}. We denote by min ⁡ ( 𝒜) \min(\mathcal{A}) the smallest letter in 𝒜 \mathcal{A} with respect to the given lexicographic order.

Let w w be a finite or infinite word over 𝒜 \mathcal{A} and let k k be a positive integer. We denote by min ⁡ ( w | k) \min(w|k) (resp. max ⁡ ( w | k) \max(w|k)) the lexicographically smallest (resp. greatest) factor of w w of length k k for the given order (where | w | ≥ k |w|\geq k if w w is finite). If w w is infinite, then it is clear that min ⁡ ( w | k) \min(w|k) and max ⁡ ( w | k) \max(w|k) are prefixes of the respective words min ⁡ ( w | k + 1) \min(w|k+1) and max ⁡ ( w | k + 1) \max(w|k+1). So we can define, by taking limits, the following two infinite words (see [94]):

 | min ⁡ ( w) = lim k → ∞ ​ min ​ ( w | k) and max ⁡ ( w) = lim k → ∞ ​ max ​ ( w | k). \min(w)=\underset{k\rightarrow\infty}{\lim}\min(w|k)\hskip 10.00002pt\mbox{and}\hskip 10.00002pt\max(w)=\underset{k\rightarrow\infty}{\lim}\max(w|k). |  |

That is, to any infinite word 𝐭 \mathbf{t} we can associate two infinite words min ⁡ ( 𝐭) \min(\mathbf{t}) and max ⁡ ( 𝐭) \max(\mathbf{t}) such that any prefix of min ⁡ ( 𝐭) \min(\mathbf{t}) (resp. max ⁡ ( 𝐭) \max(\mathbf{t})) is the lexicographically smallest (resp. greatest) amongst the factors of 𝐭 \mathbf{t} of the same length.

For a finite word w w over 𝒜 \mathcal{A} and a given order on 𝒜 \mathcal{A}, min ⁡ ( w) \min(w) denotes min ⁡ ( w | k) \min(w|k) where k k is maximal such that all min ⁡ ( w | j) \min(w|j), j = 1, 2, …, k j=1,2,\dots,k, are prefixes of min ⁡ ( w | k) \min(w|k). In the case 𝒜 = { a, b } \mathcal{A}=\{a,b\}, max ⁡ ( w) \max(w) is defined similarly (see [62]).

In 2003, Pirillo [93] (see also [94]) proved that, for infinite words 𝐬 \mathbf{s} on a 2 2 -letter alphabet { a, b } \{a,b\} with a < b a<b, the inequality

 | a ​ 𝐬 ≤ min ⁡ ( 𝐬) ≤ max ⁡ ( 𝐬) ≤ b ​ 𝐬 a\mathbf{s}\leq\min(\mathbf{s})\leq\max(\mathbf{s})\leq b\mathbf{s} |  | (7.1) |

characterizes standard Sturmian words (aperiodic and periodic). Actually, this result was known much earlier, dating back to the work of P. Veerman [112, 113] in the mid 80’s. Since that time, these ‘Sturmian inequalities’ have been rediscovered numerous times under different guises, as discussed in the forthcoming survey paper [6].

Continuing his work in relation to inequality ( 7.1), Pirillo [94] proved further that, in the case of an arbitrary finite alphabet 𝒜 \mathcal{A}, an infinite word 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega} is epistandard if and only if, for any lexicographic order, we have

 | a ​ 𝐬 ≤ min ⁡ ( 𝐬) where a = min ⁡ ( 𝒜). a\mathbf{s}\leq\min(\mathbf{s})\hskip 10.00002pt\mbox{where $a=\min(\mathcal{A})$}. |  | (7.2) |

Moreover, 𝐬 \mathbf{s} is a strict epistandard word if and only if ( 7.2) holds with strict equality for any order [74].

In a similar spirit, Glen, Justin, and Pirillo [62] recently established new characterizations of finite Sturmian and episturmian words via lexicographic orderings. As a consequence, they were able to characterize by lexicographic order all episturmian and episkew words. Similarly, they characterized by lexicographic order all balanced infinite words on a 2-letter alphabet; in other words, all Sturmian and skew infinite words, the factors of which are (finite) Sturmian. In the finite case:

###### Theorem 7.5.

[62] A finite word w w on 𝒜 \mathcal{A} is episturmian if and only if there exists a finite word u u such that, for any lexicographic order,

 | a ​ u | m | − 1 ≤ m au_{|m|-1}\leq m |  | (7.3) |

where m = min ⁡ ( w) m=\min(w) and a = min ⁡ ( 𝒜) a=\min(\mathcal{A}) for the considered order. ∎

###### Example 7.6.

Consider the finite word w = b ​ a ​ a ​ b ​ a ​ c ​ a ​ b ​ a ​ b ​ a ​ c w=baabacababac. For the different orders on { a, b, c } \{a,b,c\}, we have

- •

a < b < c a<b<c or a < c < b a<c<b: min ⁡ ( w) = a ​ a ​ b ​ a ​ c ​ a ​ b ​ a ​ b ​ a ​ c \min(w)=aabacababac,

- •

b < a < c b<a<c or b < c < a b<c<a: min ⁡ ( w) = b ​ a ​ b ​ a ​ c \min(w)=babac,

- •

c < a < b c<a<b or c < b < a c<b<a: min ⁡ ( w) = c ​ a ​ b ​ a ​ b ​ a ​ c \min(w)=cababac.

It can be verified that a finite word u u satisfying ( 7.3) must begin with a ​ b ​ a aba and one possibility is u = a ​ b ​ a ​ c ​ a ​ a ​ a ​ a ​ a ​ a u=abacaaaaaa; thus w w is a finite episturmian word.

###### Note.

In the above example, any two orders with the same minimum letter give the same min ⁡ ( w) \min(w), which is not true in general.

A corollary of Theorem 7.5 is the following new characterization of finite Sturmian words (i.e., finite balanced words).

###### Corollary 7.7.

[62] A finite word w w on 𝒜 = { a, b } \mathcal{A}=\{a,b\}, a < b a<b, is not Sturmian (in other words, not balanced) if and only if there exists a finite word u u such that a ​ u ​ a aua is a prefix of min ⁡ ( w) \min(w) and b ​ u ​ b bub is a prefix of max ⁡ ( w) \max(w). ∎

In the infinite case, the following characterization of all infinite words whose factors are finite episturmian follows almost immediately from Theorem 7.5.

###### Corollary 7.8.

[62] An infinite word 𝐭 \mathbf{t} on 𝒜 \mathcal{A} is episturmian or episkew if and only if there exists an infinite word 𝐮 \mathbf{u} such that, for any lexicographic order,

 | a ​ 𝐮 ≤ min ⁡ ( 𝐭) where a = min ⁡ ( 𝒜). a\mathbf{u}\leq\min(\mathbf{t})\hskip 10.00002pt\mbox{where $a=\min(\mathcal{A})$.}\vskip-11.38092pt |  |

∎

Consequently, an infinite word 𝐬 \mathbf{s} on { a, b } \{a,b\} ( a < b a<b) is balanced (i.e., Sturmian or skew) if and only if there exists an infinite word 𝐮 \mathbf{u} such that

 | a ​ 𝐮 ≤ min ⁡ ( 𝐬) ≤ max ⁡ ( 𝐬) ≤ b ​ 𝐮. a\mathbf{u}\leq\min(\mathbf{s})\leq\max(\mathbf{s})\leq b\mathbf{u}. |  |

Corollary 7.8 was recently refined in [58] where it was shown that, for any aperiodic episturmian word 𝐭 \mathbf{t}, the infinite word 𝐮 \mathbf{u} (as given in the corollary) is the unique epistandard word with the same set of factors as 𝐭 \mathbf{t}. As an easy consequence, we obtain the following characterization of strict episturmian words that are infinite Lyndon words (Theorem 7.9). Recall that a non-empty finite word w w over 𝒜 \mathcal{A} is a Lyndon word if it is lexicographically smaller than all of its proper suffixes for the given order < < on 𝒜 \mathcal{A}. Equivalently, w w is the lexicographically smallest primitive word in its conjugacy class; that is, w < v ​ u w<vu for all non-empty words u u, v v such that w = u ​ v w=uv. The first of these definitions extends to infinite words: an infinite word over 𝒜 \mathcal{A} is an infinite Lyndon word if and only if it is (strictly) lexicographically smaller than all of its proper suffixes for the given order on 𝒜 \mathcal{A}. That is, a finite or infinite word w w is a Lyndon word if and only if w < T i ​ ( w) w<\mathrm{T}^{i}(w) for all i > 0 i>0.

Assuming that | 𝒜 | > 1 |\mathcal{A}|>1 (since there are no Lyndon words on a 1 1 -letter alphabet), we have:

###### Theorem 7.9.

[58] An 𝒜 \mathcal{A} -strict episturmian word 𝐭 \mathbf{t} is an infinite Lyndon word if and only if 𝐭 = a ​ 𝐬 \mathbf{t}=a\mathbf{s} where a = min ⁡ ( 𝒜) a=\min(\mathcal{A}) for the given order on 𝒜 \mathcal{A} and 𝐬 \mathbf{s} is an (aperiodic) 𝒜 \mathcal{A} -strict epistandard word. Moreover, if Δ = x 1 x 2 ⋯ ∈ 𝒜 ω \Delta=x_{1}x_{2}\cdots\in\mathcal{A}^{\omega} is the directive word of 𝐬 \mathbf{s}, then 𝐭 = a ​ 𝐬 \mathbf{t}=a\mathbf{s} is the unique episturmian word in the subshift of 𝐬 \mathbf{s} directed by the spinned version of Δ \Delta having all spins 1 1, except when x i = a x_{i}=a. ∎

The above theorem is actually a generalization of a result on (aperiodic) Sturmian words given by Borel and Laubie [24] (see also [102]).

Let 𝒜 = { a 1, …, a m } \mathcal{A}=\{a_{1},\ldots,a_{m}\} be an alphabet ordered by a 1 < a 2 < ⋯ < a m a_{1}<a_{2}<\cdots<a_{m}. Then Theorem 7.9 says that an 𝒜 \mathcal{A} -strict episturmian word 𝐭 \mathbf{t} is an infinite Lyndon word if and only if the (normalized) directive word of 𝐭 \mathbf{t} belongs to { a 1, a ¯ 2, …, a ¯ m } ω \{a_{1},\bar{a}_{2},\ldots,\bar{a}_{m}\}^{\omega}. This can be reformulated as a generalization of Proposition 6.4 in [81]:

###### Corollary 7.10.

[58] An 𝒜 \mathcal{A} -strict episturmian word 𝐭 \mathbf{t} is an infinite Lyndon word if and only if it can be infinitely decomposed over the set of morphisms { ψ a, ψ ¯ x ∣ x ∈ 𝒜 ∖ { a } } \{\psi_{a},\bar{\psi}_{x}\mid x\in\mathcal{A}\setminus\{a\}\} where a = min ⁡ ( 𝒜) a=\min(\mathcal{A}) for the given order on 𝒜 \mathcal{A}. ∎

We observe that, contrary to the fact that there exists | 𝒜 |! |\mathcal{A}|! possible orders of a finite alphabet 𝒜 \mathcal{A}, Theorem 7.9 shows that there exist exactly | 𝒜 | |\mathcal{A}| infinite Lyndon words in the subshift of a given 𝒜 \mathcal{A} -strict epistandard word 𝐬 \mathbf{s} (when | 𝒜 | > 1 |\mathcal{A}|>1). That is, for any order with min ⁡ ( 𝒜) = a \min(\mathcal{A})=a, the subshift of 𝐬 \mathbf{s} contains a unique infinite Lyndon word beginning with a a, namely a ​ 𝐬 a\mathbf{s}.

###### Example 7.11.

With Δ = ( a ​ b ​ c) ω \Delta=(abc)^{\omega}, the spinned versions ( a ​ b ¯ ​ c ¯) ω (a\bar{b}\bar{c})^{\omega}, ( a ¯ ​ b ​ c ¯) ω (\bar{a}b\bar{c})^{\omega}, ( a ¯ ​ b ¯ ​ c) ω (\bar{a}\bar{b}c)^{\omega} and their ‘opposites’ (obtained by exchange of spins): ( a ¯ ​ b ​ c) ω (\bar{a}bc)^{\omega}, ( a ​ b ¯ ​ c) ω (a\bar{b}c)^{\omega}, ( a ​ b ​ c ¯) ω (ab\bar{c})^{\omega} direct episturmian words in the subshift of the Tribonacci word 𝐫 \mathbf{r}. Only the first three of these spinned infinite words direct episturmian Lyndon words: a ​ 𝐫 a\mathbf{r}, b ​ 𝐫 b\mathbf{r}, c ​ 𝐫 c\mathbf{r}, respectively.

The above results on strict episturmian Lyndon words have very recently been generalized to all episturmian words by Glen, Levé, and Richomme [64], as follows.

###### Theorem 7.12.

[64] Let 𝒜 = { a 1, …, a m } \mathcal{A}=\{a_{1},\ldots,a_{m}\} be an alphabet ordered by a 1 < a 2 < ⋯ < a m a_{1}<a_{2}<\cdots<a_{m} and, for 1 ≤ i ≤ m 1\leq i\leq m, let ℬ i = { a i, …, a m } \mathcal{B}_{i}=\{a_{i},\ldots,a_{m}\}. An episturmian word 𝐭 \mathbf{t} is an infinite Lyndon word if and only if there exists an integer j j such that 1 ≤ j < m 1\leq j<m and the (normalized) directive word of 𝐰 \mathbf{w} belongs to:

 | ( ℬ ¯ 2 ∗ a 1) ∗ ⋯ ( ℬ ¯ j ∗ a j − 1) ∗ ( ℬ ¯ j + 1 ∗ a j) ∗ ( ℬ ¯ j + 1 + { a j } +) ω. (\bar{\mathcal{B}}_{2}^{*}a_{1})^{*}\cdots(\bar{\mathcal{B}}_{j}^{*}a_{j-1})^{*}(\bar{\mathcal{B}}_{j+1}^{*}a_{j})^{*}(\bar{\mathcal{B}}_{j+1}^{+}\{a_{j}\}^{+})^{\omega}. |  |

∎

###### Note.

In the above theorem, the word *normalized*appears between brackets since one can easily verify from Theorem 4.13 that a spinned infinite word of the given form is the unique directive word of exactly one episturmian word.

###### Example 7.13.

[64] Let 𝒜 = { a, b, c, d } \mathcal{A}=\{a,b,c,d\}. Then the spinned infinite word ( b ¯ ​ c ¯ ​ a) ​ ( d ¯ ​ c ¯ ​ b) 2 ​ ( d ¯ ​ c ​ c) ω (\bar{b}\bar{c}a)(\bar{d}\bar{c}b)^{2}(\bar{d}cc)^{\omega} directs a Lyndon episturmian word, and so does a ​ a ​ ( d ¯ ​ c) ω aa(\bar{d}c)^{\omega}, but c ¯ ​ a ​ b ¯ ​ a ​ d ¯ ​ c ​ d ω \bar{c}a\bar{b}a\bar{d}cd^{\omega} does not (since this spinned word directs a periodic word).

###### Remark 7.14.

Theorems 4.13 and 7.12 show that any episturmian Lyndon word has a unique spinned directive word, but the converse is not true. For example, the regular wavy word ( a ​ b ¯ ​ c) ω (a\bar{b}c)^{\omega} is the unique directive word of the strict episturmian word:

 | lim n → ∞ μ a ​ b ¯ ​ c n ( a) = a c a b a a b a c a b a c a b a a b a c a ⋯ \lim_{n\rightarrow\infty}{\mu_{a\bar{b}c}^{n}(a)}=acabaabacabacabaabaca\cdots |  |

which is clearly not an infinite Lyndon word by Theorem 7.12 and also by the fact that a ​ c ​ a ​ b ​ a ​ a ​ w acabaaw is not a Lyndon word for any order on { a, b, c } \{a,b,c\} and for any word w w.

A key tool used in the proof of Theorem 7.12 was the following result of Richomme, which characterizes episturmian morphisms that preserve Lyndon words. A morphism f f is said to preserve finite (resp. infinite) Lyndon words if for each finite (resp. infinite) Lyndon word w w, f ⁡ ( w) f(w) is a finite (resp. infinite) Lyndon word.

###### Theorem 7.15.

[100, 103] Let 𝒜 = { a 1, …, a m } \mathcal{A}=\{a_{1},\ldots,a_{m}\} be an alphabet ordered by a 1 < a 2 < ⋯ < a m a_{1}<a_{2}<\cdots<a_{m}. Then the following assertions are equivalent for an episturmian morphism:

- •

f f preserves finite Lyndon words;

- •

f f preserves infinite Lyndon words;

- •

f ∈ ( Ψ ¯ { a 2, …, a m } ∗ ​ ψ a 1) ∗ ​ { Ψ ¯ a m } ∗ f\in({\bar{\Psi}}_{\{a_{2},\ldots,a_{m}\}}^{*}\psi_{a_{1}})^{*}\{\bar{\Psi}_{a_{m}}\}^{*} where Ψ ¯ 𝒜 = { ψ ¯ x | x ∈ 𝒜 } \bar{\Psi}_{\mathcal{A}}=\{\bar{\psi}_{x}~|~x\in\mathcal{A}\}. ∎

### 7.4 Imbalance

We now return our attention to the notion of balance.

Episturmian words on three or more letters are generally unbalanced in the sense of 1 1 -balance, except, of course, for those on a 2 2 -letter alphabet, which are precisely the (periodic and aperiodic) Sturmian words. In fact, Cassaigne, Ferenczi, and Zamboni [33] have proved, by construction, that there exists an episturmian word that is not q q -balanced for any q q. Note, however, that the Tribonacci word is 2 2 -balanced, for example. More generally, it can be shown by induction that the k k -bonacci word, directed by ( a 1 a 2 ⋯ a k) ω (a_{1}a_{2}\cdots a_{k})^{\omega}, is ( k − 1) (k-1) -balanced. Even further, one can prove that any linearly recurrent strict episturmian word (or Arnoux-Rauzy sequence) is q q -balanced for some q q. Linearly recurrent Arnoux-Rauzy sequences were completely described in [105, 32]; they are the strict episturmian words for which each letter x x occurs in Δ \Delta with bounded gaps.

Using their main result on return words (Theorem 6.13), Justin and Vuillon [76] proved that episturmian words do in fact satisfy a kind of balance property. Specifically:

###### Theorem 7.16.

[76, Theorem 5.2] Let 𝐬 ∈ 𝒜 ω \mathbf{s}\in\mathcal{A}^{\omega} be an epistandard word and let { d, e } \{d,e\} be a 2 2 -letter subset of 𝒜 \mathcal{A}. Then, for any u u, v ∈ F ⁡ ( 𝐬) ∩ { d, e } ∗ v\in F(\mathbf{s})\cap\{d,e\}^{*} with | u | = | v | |u|=|v|, we have | | u | d − | ​ v | d | ≤ 1 ||u|_{d}-|v|_{d}|\leq 1. ∎

This property of episturmian words reduces to the balance property of Sturmian words when 𝒜 \mathcal{A} is a 2 2 -letter alphabet (in which case it is characteristic); however, the property is far from being characteristic when 𝒜 \mathcal{A} consists of more than two letters.

More recently, Richomme [101] also proved that episturmian words and Arnoux-Rauzy sequences can be characterized via a nice ‘local balance property’. That is:

###### Theorem 7.17.

[101] For a recurrent infinite word 𝐭 ∈ 𝒜 ω \mathbf{t}\in\mathcal{A}^{\omega}, the following assertions are equivalent:

1. i)

𝐭 \mathbf{t} is episturmian;

2. ii)

for each factor u u of 𝐭 \mathbf{t}, there exists a letter a a such that 𝒜 ​ u ​ 𝒜 ∩ F ⁡ ( 𝐭) ⊆ a ​ u ​ 𝒜 ∪ 𝒜 ​ u ​ a \mathcal{A}u\mathcal{A}\cap F(\mathbf{t})\subseteq au\mathcal{A}\cup\mathcal{A}ua;

3. iii)

for each palindromic factor u u of 𝐭 \mathbf{t}, there exists a letter a a such that 𝒜 ​ u ​ 𝒜 ∩ F ⁡ ( 𝐭) ⊆ a ​ u ​ 𝒜 ∪ 𝒜 ​ u ​ a \mathcal{A}u\mathcal{A}\cap F(\mathbf{t})\subseteq au\mathcal{A}\cup\mathcal{A}ua. ∎

Roughly speaking, the above theorem says that for any factor u u of a given episturmian word 𝐭 \mathbf{t}, there exists a unique letter a a such that every occurrence of u u in 𝐭 \mathbf{t} is immediately preceded or followed by a a in 𝐭 \mathbf{t}. When | 𝒜 | = 2 |\mathcal{A}|=2, property OPEN i ​ i) ii) of Theorem 7.17 is equivalent to the definition of balance. Indeed, Coven and Hedlund [37] stated that an infinite word 𝐰 \mathbf{w} over { a, b } \{a,b\} is not balanced if and only if there exists a palindrome u u such that a ​ u ​ a aua and b ​ u ​ b bub are both factors of 𝐰 \mathbf{w}. As pointed out in [101], this property can be rephrased as follows: an infinite word 𝐰 \mathbf{w} is Sturmian if and only if 𝐰 \mathbf{w} is aperiodic and, for any factor u u of 𝐰 \mathbf{w}, the set of factors belonging to 𝒜 ​ u ​ 𝒜 \mathcal{A}u\mathcal{A} is a subset of a ​ u ​ 𝒜 ∪ 𝒜 ​ u ​ a au\mathcal{A}\cup\mathcal{A}ua or a subset of b ​ u ​ 𝒜 ∪ 𝒜 ​ u ​ b bu\mathcal{A}\cup\mathcal{A}ub.

### 7.5 Fraenkel’s conjecture

As discussed previously, the recurrent balanced infinite words on two letters are exactly the Sturmian words (aperiodic and periodic). A natural question to ask is then: “What are the balanced recurrent infinite words on more than two letters?” In this direction, Paquin and Vuillon [92] recently characterized the balanced episturmian words by classifying these words into three families, as follows.

###### Theorem 7.18.

[92] Any balanced standard episturmian sequence 𝐬 \mathbf{s} on a k k -letter alphabet 𝒜 k = { 1, 2, …, k } \mathcal{A}_{k}=\{1,2,\ldots,k\}, k ≥ 3 k\geq 3, belongs to one of the following three families (up to letter permutation):

1. i)

𝐬 = p ⁡ ( k − 1) ​ p ​ ( k ​ p ​ ( k − 1) ​ p) ω \mathbf{s}=p(k-1)p(kp(k-1)p)^{\omega}, with p = P a l ( 1 n 2 ⋯ ( k − 2)) p=Pal(1^{n}2\cdots(k-2));

2. ii)

𝐬 = p ⁡ ( k − 1) ​ p ​ ( k ​ p ​ ( k − 1) ​ p) ω \mathbf{s}=p(k-1)p(kp(k-1)p)^{\omega}, with

 | p = P a l ( 123 ⋯ ( k − ℓ − 1) 1 ( k − ℓ) ⋯ ( k − 2)); p=Pal(123\cdots(k-\ell-1)1(k-\ell)\cdots(k-2)); |  |

3. iii)

𝐬 = [P a l ( 123 ⋯ k)] ω \mathbf{s}=[Pal(123\cdots k)]^{\omega}. ∎

The importance of the above result lies in the fact that it supports Fraenkel’s conjecture [56]: a problem that arose in a number-theoretic context and has remained unsolved for over thirty years. Fraenkel conjectured that, for a fixed k ≥ 3 k\geq 3, there is only one covering of ℤ \mathbb{Z} by k k Beatty sequences of the form ( ⌊ α ​ n + β ⌋) n ≥ 1 (\lfloor\alpha n+\beta\rfloor)_{n\geq 1}, where α \alpha, β \beta are real numbers. A combinatorial interpretation of this conjecture may be stated as follows (taken from [92]). Over a k k -letter alphabet with k ≥ 3 k\geq 3, there is only one recurrent balanced infinite word, up to letter permutation and shifts, that has mutually distinct letter frequencies. This supposedly unique infinite word is called Fraenkel’s sequence and is given by ( F k) ω (F_{k})^{\omega} where the Fraenkel words ( F i) i ≥ 1 (F_{i})_{i\geq 1} are defined recursively by F 1 = 1 F_{1}=1 and F i = F i − 1 ​ i ​ F i − 1 F_{i}=F_{i-1}iF_{i-1} for all i ≥ 2. i\geq 2. (Note that F k = P a l ( 12 ⋯ k) F_{k}=Pal(12\cdots k).) For further details, see for instance [92, 110] and references therein.

Amongst the classes of balanced episturmian words given in Theorem 7.18, only one class has mutually distinct letter frequencies and, up to letter permutation and shifts, corresponds to Fraenkel’s sequence. That is:

###### Theorem 7.19 (Paquin-Vuillon [92]).

Suppose 𝐭 \mathbf{t} is a balanced episturmian word with Alph ​ ( 𝐭) = { 1, 2, …, k } \mbox{{Alph}}(\mathbf{t})=\{1,2,\ldots,k\}, k ≥ 3 k\geq 3. If 𝐭 \mathbf{t} has mutually distinct letter frequencies, then up to letter permutation, 𝐭 \mathbf{t} is a shift of ( F k) ω (F_{k})^{\omega}. ∎

More recently, it was proved in [61] that any recurrent balanced rich infinite word is necessarily episturmian, and hence such words obey Fraenkel’s conjecture (recall that rich words were defined Section 6.2.2).

###### Remark 7.20.

An interesting known fact (e.g., see [68]) is that any balanced recurrent infinite word 𝐱 \mathbf{x} on k ≥ 3 k\geq 3 letters having mutually distinct letter frequencies is necessarily periodic. Certainly, the image of 𝐱 \mathbf{x} under any morphism of the form: ( a ↦ a a\mapsto a, other x ↦ b x\mapsto b) is a Sturmian word. If, for one letter, the corresponding Sturmian word is aperiodic (i.e., 𝐱 \mathbf{x} has irrational slope as a cutting sequence), then we meet impossibility; thus rather easily 𝐱 \mathbf{x} must be periodic.

## 8 Concluding remarks

In closing, we mention a number of very recent works involving episturmian words.

Rigidity:

Krieger [78] has shown that any strict purely morphic epistandard word 𝐬 \mathbf{s} is rigid. That is, all of the morphisms that generate 𝐬 \mathbf{s} are powers of the same unique (epistandard) morphism. Krieger also showed that a certain class of ‘ultimately strict’ purely morphic epistandard words are not rigid, but it remains an open question as to whether or not all strict morphic episturmian words are rigid.

Quasiperiodicity:

A finite or infinite word w w is said to be quasiperiodic if there exists a word u u (with u ≠ w u\neq w for finite w w) such that the occurrences of u u in w w entirely cover w w, i.e., every position of w w falls within some occurrence of u u in w w. Such a word u u is called a quasiperiod of w w. For example, the word w = a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a w=abaababaabaababaaba has quasiperiods a ​ b ​ a aba, a ​ b ​ a ​ a ​ b ​ a abaaba, a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a abaababaaba.

In the last fifteen years, quasiperiodicity and coverings of finite words has been extensively studied (see [9] for a brief survey on quasiperiodicity in ‘strings’). Quasiperiodic finite words were first introduced by Apostolico and Ehrenfeucht in [10]. The notion was later extended to infinite words by Marcus [85] who opened some questions, particularly concerning quasiperiodicity of Sturmian words. After a brief answer to some of these questions in [79], the Sturmian case was fully studied by Levé and Richomme [81] who proved that a Sturmian word is non-quasiperiodic if and only if it is an infinite Lyndon word. The study of quasiperiodicity in Sturmian words was very recently extended to episturmian words by Glen, Levé, and Richomme [58, 64, 80], who have completely described all of the quasiperiods of an episturmian word, yielding a characterization of quasiperiodic episturmian words in terms of their directive words. They have also characterized episturmian morphisms that map any word onto a quasiperiodic one. These results show that, unlike the Sturmian case, there exist non-quasiperiodic episturmian words that are not infinite Lyndon words. Key tools used in the study of quasiperiodicity in episturmian words were episturmian morphisms, normalized directive words (recall Theorem 4.12), and the following equivalent definition of quasiperiodicity in terms of return words introduced by Glen in [58]: a finite word v v is a quasiperiod of an infinite word 𝐰 \mathbf{w} if and only if v v is a recurrent prefix of 𝐰 \mathbf{w} such that all of the returns to v v in 𝐰 \mathbf{w} have length at most | v | |v|.

In [89], Monteil proved that any Sturmian subshift contains a multi-scale quasiperiodic word, i.e., an infinite word having infinitely many quasiperiods. A shorter proof of this fact was provided in [81] and this result has also been proven true for episturmian words in [64].

For more recent work on quasiperiodicity, see for instance [89, 90].

θ \theta -episturmian words:

Recall that an infinite word is episturmian if and only if its set of factors is closed under reversal and it has at most one left special factor of each length. With this definition in mind, Bucci, de Luca, De Luca, and Zamboni [27, 28] have recently introduced and studied a further extension of episturmian words in which the reversal operator is replaced by an arbitrary involutory antimorphism (i.e., a map θ: 𝒜 ∗ → 𝒜 ∗ \theta:\mathcal{A}^{*}\rightarrow\mathcal{A}^{*} such that θ 2 = \theta^{2}= Id and θ ⁡ ( u ​ v) = θ ⁡ ( v) ​ θ ​ ( u) \theta(uv)=\theta(v)\theta(u) for all u u, v ∈ 𝒜 ∗ v\in\mathcal{A}^{*}). More precisely, an infinite word over 𝒜 \mathcal{A} is said to be θ \theta -episturmian if it has at most one left special factor of each length and its set of factors is closed under an involutory antimorphism θ \theta of the free monoid 𝒜 ∗ \mathcal{A}^{*}. Generalizing even further, θ \theta -episturmian words with seed are obtained by requiring the condition on special factors only for sufficiently large lengths (see [28]).

Acknowledgements. The authors would like to thank Jean Berstel and Pierre Arnoux for their helpful comments on a preliminary version of this paper. Many thanks also to the two anonymous referees whose thoughtful suggestions helped to improve the paper.

## References

- [1] B. Adamczewski, Balances for fixed points of primitive substitutions, Theoret. Comput. Sci. 307 (2003) 47–75.
- [2] B. Adamczewski,Y. Bugeaud, Palindromic continued fractions, Ann. Inst. Fourier (Grenoble) 57 (2007) 1557–1574.
- [3] B. Adamczewski, Y. Bugeaud, Transcendence measure for continued fractions involving repetitive or symmetric patterns, J. Eur. Math. Soc., to appear.
- [4] P. Alessandri, V. Berthé, Three distance theorems and combinatorics on words, Enseign. Math. 44 (1998) 103–132.
- [5] J.-P. Allouche, J.L. Davison, M. Queffélec, L.Q. Zamboni, Transcendence of Sturmian or morphic continued fractions, J. Number Theory 91 (2001) 39–66.
- [6] J.-P. Allouche, A. Glen, Extremal properties of (epi)sturmian sequences and distribution modulo 1 1, in preparation.
- [7] J.-P. Allouche, J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, *Cambridge University Press*, UK, 2003.
- [8] P. Ambrož, C. Frougny, Z. Masáková, E. Pelantová, Palindromic complexity of infinite words associated with simple Parry numbers, Ann. Inst. Fourier (Grenoble) 56 (2006) 2131–2160.
- [9] A. Apostolico, M. Crochemore, String pattern matching for a deluge survival kit, in: Handbook of Massive Data Sets, Massive Comput., vol. 4, Kluwer Acad. Publ., Dordrecht, 2002.
- [10] A. Apostolico, A. Ehrenfeucht, Efficient detection of quasiperiodicities in strings, Theoret. Comput. Sci. 119 (1993) 247–265.
- [11] P. Arnoux, S. Ito, Pisot substitutions and Rauzy fractals, Bull. Belg. Math. Soc. Simon Stevin 8 (2001) 181–207.
- [12] P. Arnoux, G. Rauzy, Représentation géométrique de suites de complexité 2 ​ n + 1 2n+1, *Bull. Soc. Math. France*119 (1991) 199–215.
- [13] Yu. Baryshnikov, Complexity of trajectories in rectangular billiards, Comm. Math. Phys. 174 (1995) 43–56.
- [14] J. Berstel, On the index of Sturmian words, in: *Jewels Are Forever*, Springer-Verlag, Berlin, 1999, pp. 287–294.
- [15] J. Berstel, Recent results on extensions of Sturmian words, Internat. J. Algebra Comput. 12 (2002) 371–385.
- [16] J. Berstel, P. Séébold, A characterization of Sturmian morphisms, in: Borzyszkowski, A.M. and Sokolowski, S. ( ( Eds.)), Mathematical Foundations of Computer Science 1993, Lecture Notes in Computer Science, vol. 711, Springer-Verlag, Berlin, 1993, pp. 281–290.
- [17] J. Berstel, P. Séébold, A remark on morphic Sturmian words, Theor. Inform. Appl. 28 (1994) 255–263.
- [18] J. Berstel, L. Vuillon, Coding rotations on intervals, Theoret. Comput. Sci. 281 (2002) 99–107.
- [19] V. Berthé, Fréquences des facteurs des suites sturmiennes, Theoret. Comput. Sci. 165 (1996) 295–309.
- [20] V. Berthé, Autour du système de numération d’Ostrowski, Bull. Belg. Math. Soc. Simon Stevin 8 (2001) 209–239.
- [21] V. Berthé, H. Ei, S. Ito, and H. Rao, On substitution invariant Sturmian words: an application of Rauzy fractals, Theoret. Inform. Appl. 41 (2007) 329–349.
- [22] V. Berthé, S. Ferenczi, L.Q. Zamboni, Interactions between dynamics, arithmetics and combinatorics: the good, the bad, and the ugly, in: Algebraic and topological dynamics, Contemp. Math., vol. 385, Amer. Math. Soc., Providence, RI, 2005, pp. 333–364.
- [23] V. Berthé, C. Holton, L.Q. Zamboni, Initial powers of Sturmian sequences, Acta Arith. 122 (2006) 315–347.
- [24] J.-P. Borel, F. Laubie, Quelques mots sur la droite projective réelle, J. Théor. Nombres Bordeaux 5 (1993) 23–51.
- [25] J.-P. Borel, C. Reutenauer, Palindromic factors of billiard words, Theoret. Comput. Sci. 340 (2005) 334–348.
- [26] S. Brlek, S. Hamel, M. Nivat, C. Reutenauer, On the palindromic complexity of infinite words, Internat. J. Found. Comput. Sci. 15 (2004) 293–306.
- [27] M. Bucci, A. de Luca, A. De Luca, L.Q. Zamboni, On some problems related to palindrome closure, Theor. Inform. Appl. (in press), doi:10.1051/ita:2007064.
- [28] M. Bucci, A. de Luca, A. De Luca, L.Q. Zamboni, On different generalizations of episturmian words, Theoret. Comput. Sci. 393 (2008) 23–36.
- [29] M. Bucci, A. De Luca, A. Glen, L.Q. Zamboni, A connection between palindromic and factor complexity using return words, Adv. in Appl. Math. (in press), doi:10.1016/j.aam.2008.03.005.
- [30] M. Bucci, A. De Luca, A. Glen, L.Q. Zamboni, A new characteristic property of rich words, Preprint, 2008, arXiv:0807.2303.
- [31] J. Cassaigne, Sequences with grouped factors, in: Developments in Language Theory III, Aristotle University of Thessaloniki, 1998, pp. 211–222.
- [32] J. Cassaigne, N. Chekhova, Fonctions de récurrence des suites d’Arnoux-Rauzy et réponse à une question de Morse et Hedlund, Ann. Inst. Fourier (Grenoble) 56 (2006) 2249–2270.
- [33] J. Cassaigne, S. Ferenczi, L.Q. Zamboni, Imbalances in Arnoux-Rauzy sequences, Ann. Inst. Fourier (Grenoble) 50 (2000) 1265–1276.
- [34] M.G. Castelli, F. Mignosi, A. Restivo, Fine and Wilf’s theorem for three periods and a generalization of Sturmian words, Theoret. Comput. Sci. 218 (1999) 83–94.
- [35] N. Chekhova, P. Hubert, A. Messaoudi, Propriétés combinatoires, ergodiques et arithmétiques de la substitution de Tribonacci, J. Théor. Nombres Bordeaux 13 (2001) 371–394.
- [36] E.M. Coven, Sequences with minimal block growth II, Math. Systems Theory 8 (1974) 376–382.
- [37] E.M. Coven, G.A. Hedlund, Sequences with minimal block growth, *Math. Systems Theory*7 (1973) 138–153.
- [38] D. Crisp, W. Moran, A. Pollington, P. Shiue, Substitution invariant cutting sequences, J. Théor. Nombres Bordeaux 5 (1993) 123–137.
- [39] D. Damanik, D. Lenz, The index of Sturmian sequences, *European J. Combin.*23 (2002) 23–29.
- [40] D. Damanik, L.Q. Zamboni, Combinatorial properties of Arnoux-Rauzy subshifts and applications to Schrödinger operators, Rev. Math. Phys. 15 (2003) 745–763.
- [41] A. de Luca, Sturmian words: structure, combinatorics and their arithmetics, *Theoret. Comput. Sci.*183 (1997) 45–82.
- [42] A. de Luca, A. Glen, L.Q. Zamboni, Rich, Sturmian, and trapezoidal words, Theoret. Comput. Sci. (in press), doi:10.1016/j.tcs.2008.06.009.
- [43] X. Droubay, J. Justin, G. Pirillo, Episturmian words and some constructions of de Luca and Rauzy, *Theoret. Comput. Sci.*255 (2001) 539–553.
- [44] X. Droubay, G. Pirillo, Palindromes and Sturmian words, Theoret. Comput. Sci. 223 (1999) 73–85.
- [45] F. Durand, A characterization of substitutive sequences using return words, Discrete Math. 179 (1998) 89–101.
- [46] F. Durand, A generalization of Cobham’s theorem, Theory Comput. Syst. 31 (1998) 169–185.
- [47] F. Durand, Linearly recurrent subshifts have a finite number of non-periodic subshift factors, Ergodic Theory Dynam. Systems 19 (1999) 953–993.
- [48] I. Fagnot, A little more about morphic Sturmian words, Theor. Inform. Appl. 40 (2006) 511–518.
- [49] I. Fagnot, L. Vuillon, Generalized balances in Sturmian words, Discrete Appl. Math. 121 (2002) 83–101.
- [50] S. Ferenczi, Complexity of sequences and dynamical systems, Discrete Math. 206 (1999) 145–154.
- [51] S. Ferenczi, C. Holton, L.Q. Zamboni, Structure of three interval exchange transformations I. An arithmetic study, Ann. Inst. Fourier (Grenoble) 51 (2001) 861–901.
- [52] S. Ferenczi, C. Mauduit, Transcendence of numbers with a low complexity expansion, J. Number Theory 67 (1997) 146–161.
- [53] S. Ferenczi, C. Mauduit, A. Nogueira, Substitutional dynamical systems: algebraic characterization of eigenvalues, Ann. Sci. École Norm. Sup. 29 (1995) 519–533.
- [54] S. Fischler, Palindromic prefixes and episturmian words, J. Combin. Theory Ser. A 113 (2006) 1281–1304.
- [55] S. Fischler, Palindromic prefixes and diophantine approximation, Monatsh. Math. 151 (2007) 11–37.
- [56] A.S. Fraenkel, Complementing and exactly covering sequences. J. Combinatorial Theory Ser. A 14 (1973) 8–20.
- [57] A. Glen, On Sturmian and episturmian words, and related topics, Ph.D. Thesis, The University of Adelaide, Australia, April 2006.
- [58] A. Glen. Order and quasiperiodicity in episturmian words. in: Proceedings of the 6 6 th International Conference on Words, Marseille, France, September 17-21, 2007, pp. 144–158.
- [59] A. Glen, Powers in a class of 𝒜 \mathcal{A} -strict standard episturmian words, Theoret. Comput. Sci. 380 (2007) 330–354.
- [60] A. Glen, A characterization of fine words over a finite alphabet, Theoret. Comput. Sci. 391 (2008) 51–60.
- [61] A. Glen, J. Justin, S. Widmer, L.Q. Zamboni, Palindromic richness, European J. Combin. (in press), doi:10.1016/j.ejc.2008.04.006.
- [62] A. Glen, J. Justin, G. Pirillo, Characterizations of finite and infinite episturmian words via lexicographic orderings, *European J. Combin.*29 (2008) 45–58.
- [63] A. Glen, F. Levé, G. Richomme, Directive words of episturmian words: equivalences and normalization, Preprint, 2008, arXiv:0802.3888.
- [64] A. Glen, F. Levé, G. Richomme, Quasiperiodic and Lyndon episturmian words, Theoret. Comput. Sci., to appear.
- [65] E. Godelle, Représentation par des transvections des groupes dÕartin-tits, Group, Geometry and Dynamics 1 (2007) 111–133.
- [66] A. Heinis, R. Tijdeman, Characterisation of asymptotically Sturmian sequences, *Publ. Math. Debrecen*56 (2000) 415–430.
- [67] C. Holton, L.Q. Zamboni, Descendants of primitive substitutions, Theory Comput. Syst. 32 (1999) 133–157.
- [68] P. Hubert, Suites équilibrés, Theoret. Comput. Sci. 242 (2000) 91–108.
- [69] O. Jenkinson, L.Q. Zamboni, Characterisations of balanced words via orderings, *Theoret. Comput. Sci*310 (2004) 247–271.
- [70] J. Justin, On a paper by Castelli, Mignosi, Restivo, Theor. Inform. Appl. 34 (2000) 373–377.
- [71] J. Justin, Episturmian morphisms and a Galois theorem on continued fractions, Theor. Inform. Appl. 39 (2005) 207–215.
- [72] J. Justin, G. Pirillo, Fractional powers in Sturmian words, *Theoret. Comput. Sci.*255 (2001) 363–376.
- [73] J. Justin, G. Pirillo, Episturmian words and episturmian morphisms, *Theoret. Comput. Sci.*276 (2002) 281–313.
- [74] J. Justin, G. Pirillo, On a characteristic property of Arnoux-Rauzy sequences, Theor. Inform. Appl. 36 (2002) 385–388.
- [75] J. Justin, G. Pirillo, Episturmian words: shifts, morphisms and numeration systems, *Internat. J. Found. Comput. Sci.*15 (2004) 329–348.
- [76] J. Justin, L. Vuillon, Return words in Sturmian and episturmian words, Theor. Inform. Appl. 34 (2000) 343–356.
- [77] T. Komatsu A.J. van der Poorten, Substitution invariant Beatty sequences, Jpn. J. Math. 22 (1996) 349–354.
- [78] D. Krieger, On stabilizers of infinite words, Theoret. Comput. Sci. 400 (2008) 169–181.
- [79] F. Levé, G. Richomme, Quasiperiodic infinite words: some answers, Bull. Eur. Assoc. Theor. Comput. Sci. (EATCS) 84 (2004) 128–138.
- [80] F. Levé, G. Richomme, Quasiperiodic episturmian words, in: Proceedings of the 6 6 th International Conference on Words, Marseille, France, September 17-21, 2007, pp. 201–211.
- [81] F. Levé, G. Richomme, Quasiperiodic Sturmian words and morphisms, Theoret. Comput. Sci. 372 (2007) 15–25.
- [82] M. Lothaire, Combinatorics on Words, vol. 17 of Encyclopedia of Mathematics and its Applications, Addison-Wesley, Reading, Massachusetts, 1983.
- [83] M. Lothaire, *Algebraic Combinatorics on Words*, vol. 90 of Encyclopedia of Mathematics and its Applications, Cambridge University Press, U.K., 2002.
- [84] M. Lothaire, *Applied Combinatorics on Words*, vol. 105 of Encyclopedia of Mathematics and its Applications, Cambridge University Press, U.K., 2005.
- [85] S. Marcus, Quasiperiodic infinite words, Bull. Eur. Assoc. Theor. Comput. Sci. (EATCS) 82 (2004) 170–174.
- [86] F. Mignosi, G. Pirillo. Repetitions in the Fibonacci infinite word, *Theor. Inform. Appl.*26 (1992) 199–204.
- [87] F. Mignosi, P. Séébold, Morphismes Sturmiens et règles de Rauzy, J. Théor. Nombres Bordeaux 5 (1993) 221–233.
- [88] F. Mignosi, L.Q. Zamboni, On the number of Arnoux-Rauzy words, Acta Arith. 101 (2002) 121–129.
- [89] T. Monteil. Illumination dans les billards polygonaux et dynamique symbolique. PhD thesis, Université de la Méditerranée, Faculté des Sciences de Luminy, December 2005.
- [90] T. Monteil, S. Marcus, Quasiperiodic infinite words: multi-scale case and dynamical properties, Theoret. Comput. Sci., to appear, arXiv:math/0603354v1.
- [91] M. Morse, G.A. Hedlund, Symbolic dynamics II. Sturmian trajectories, *Amer. J. Math.*62 (1940) 1–42.
- [92] G. Paquin, L. Vuillon, A characterization of balanced episturmian sequences, Electron. J. Combin. 14 (2007) #R33, pp. 12.
- [93] G. Pirillo, Inequalities characterizing standard Sturmian words, Pure Math. Appl. 14 (2003) 141–144.
- [94] G. Pirillo, Inequalities characterizing standard Sturmian and episturmian words, Theoret. Comput. Sci. 341 (2005) 276–292.
- [95] G. Pirillo, Morse and Hedlund’s skew Sturmian words revisited, Ann. Comb. 12 (2008) 115–121.
- [96] N. Pytheas Fogg, *Substitutions in Dynamics, Arithmetics and Combinatorics*, vol. 1794 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 2002.
- [97] G. Rauzy, Suites à termes dans un alphabet fini, in: Sémin. Théorie des Nombres, Exp. No. 25, pp. 16, Univ. Bordeaux I, Talence, 1982–1983.
- [98] G. Rauzy, Mots infinis en arithmétique, in: M. Nivat, D. Perrin (Eds.), Automata On Infinite Words, Lecture Notes in Computer Science, vol. 192, Springer-Verlag, Berlin, 1985, pp. 165–171.
- [99] G. Richomme, Conjugacy and episturmian morphisms, *Theoret. Comput. Sci.*302 (2003) 1–34.
- [100] G. Richomme, Lyndon morphisms, Bull. Belg. Math. Soc. Simon Stevin 10 (2003) 761–785.
- [101] G. Richomme, A local balance property of episturmian words, in: Proceedings of the 11th International Conference on Developments in Language Theory 2007 (DLT ’07), July 3–6, Turku, Finland, vol. 4588 of Lecture Notes in Computer Science, Springer, Berlin, 2007, pp. 371–381.
- [102] G. Richomme, Conjugacy of morphisms and Lyndon decomposition of standard Sturmian words, Theoret. Comput. Sci. 380 (2007) 393–400.
- [103] G. Richomme, On morphisms preserving infinite Lyndon words, Discrete Math. Theor. Comput. Sci. 9 (2007) 89–108.
- [104] G. Richomme, Private communication, 2007.
- [105] R.N. Risley, L.Q. Zamboni, A generalization of Sturmian sequences: Combinatorial structure and transcendence, *Acta Arith.*95 (2000) 167–184.
- [106] A. Siegel, Pure discrete spectrum dynamical systems and periodic tiling associated with a substitution, Ann. Inst. Fourier (Grenoble) 54 (2004) 341–381.
- [107] B. Tan, Z.-Y. Wen, Some properties of the Tribonacci sequence, European J. Combin. 28 (2007) 1703–1719.
- [108] R. Tijdeman, On complementary triples of Sturmian bisequences, Indag. Math. 7 (1996) 419–424.
- [109] R. Tijdeman, Intertwinings of Sturmian sequences, Indag. Math. 9 (1998) 113–122.
- [110] R. Tijdeman, Fraenkel’s conjecture for six sequences, Discrete Math. 222 (2000) 223–234.
- [111] D. Vandeth, Sturmian words and words with a critical exponent, *Theoret. Comput. Sci.*242 (2000) 283–300.
- [112] P. Veerman, Symbolic dynamics and rotation numbers, Physica A 134 (1986) 543–576.
- [113] P. Veerman, Symbolic dynamics of order-preserving orbits, Physica D 29 (1987) 191–201.
- [114] L. Vuillon, A characterization of Sturmian words by return words, European J. Combin. 22 (2001) 263–275.
- [115] L. Vuillon, Balanced words, Bull. Belg. Math. Soc. Simon Stevin 10 (2003) 787–805.
- [116] Z.-X. Wen, Y. Zhang, Some remarks on invertible substitutions on three letter alphabet, Chinese Sci. Bull. 44 (19) (1999) 1755–1760.
- [117] N. Wozny, L.Q. Zamboni, Frequencies of factors in Arnoux-Rauzy sequences, Acta Arith. 96 (2001) 261–278.
- [118] S.-I. Yasutomi, On Sturmian sequences which are invariant under some substitutions, in: Number theory and its applications (Kyoto, 1997), Kluwer Acad. Publ., Dordrecht, 1999, pp. 347–373.
- [119] L.Q. Zamboni, Une généralisation du théorème de Lagrange sur le développement en fraction continue, C.R. Acad. Sci. Paris Sér. I Math. 327 (1998) 527–530.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/0801.1654
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/0801.1655
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0801.1655
[7]: https://arxiv.org/pdf/0801.1655
[8]: /html/0801.1656
