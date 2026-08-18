<!-- source: https://ar5iv.labs.arxiv.org/html/0801.1656 | converted from HTML -->

[0801.1656] PALINDROMIC RICHNESS

# PALINDROMIC RICHNESS

Amy Glen 1 1 1 Corresponding author: LaCIM, Université du Québec à Montréal, C.P. 8888, succursale Centre-ville, Montréal, Québec, CANADA, H3C 3P8 ( amy.glen@gmail.com). Supported by CRM, ISM, and LaCIM. Jacques Justin 2 2 2 LIAFA, Université Paris Diderot - Paris 7, Case 7014, 75205 Paris Cedex 13, FRANCE ( jacjustin@free.fr). Steve Widmer 3 3 3 Department of Mathematics, University of North Texas, P.O. Box 311430, Denton, Texas, TX 76203-1430, USA ( sbw0061@unt.edu). Luca Q. Zamboni 4 4 4 Institut Camille Jordan, Université Claude Bernard Lyon 1, 43 boulevard du 11 novembre 1918, 69622 Villeurbanne Cedex FRANCE ( luca@unt.edu).

###### Abstract

In this paper, we study combinatorial and structural properties of a new class of finite and infinite words that are ‘rich’ in palindromes in the utmost sense. A characteristic property of so-called rich words is that all complete returns to any palindromic factor are themselves palindromes. These words encompass the well-known episturmian words, originally introduced by the second author together with X. Droubay and G. Pirillo in 2001. Other examples of rich words have appeared in many different contexts. Here we present the first unified approach to the study of this intriguing family of words.

Amongst our main results, we give an explicit description of the periodic rich infinite words and show that the recurrent balanced rich infinite words coincide with the balanced episturmian words. We also consider two wider classes of infinite words, namely weakly rich words and almost rich words (both strictly contain all rich words, but neither one is contained in the other). In particular, we classify all recurrent balanced weakly rich words. As a consequence, we show that any such word on at least three letters is necessarily episturmian; hence weakly rich words obey Fraenkel’s conjecture. Likewise, we prove that a certain class of almost rich words obeys Fraenkel’s conjecture by showing that the recurrent balanced ones are episturmian or contain at least two distinct letters with the same frequency.

Lastly, we study the action of morphisms on (almost) rich words with particular interest in morphisms that preserve (almost) richness. Such morphisms belong to the class of P P -morphisms that was introduced by A. Hof, O. Knill, and B. Simon in 1995.

Keywords: palindrome; episturmian word; balanced word; rich word; return word; morphism.

MSC (2000): 68R15.

## 1 Introduction

In recent years there has been growing interest in palindromes in the field of combinatorics on words, especially since the work of A. de Luca [12] and also X. Droubay and G. Pirillo [14], who showed that the well-known Sturmian words are characterized by their palindromic complexity [1, 4, 7]. A strong motivation for the study of palindromes, and in particular infinite words containing arbitrarily long palindromes, stems from their application to the modelling of quasicrystals in theoretical physics (see for instance [11, 19]) and also Diophantine approximation (e.g., see [16]).

In [13], the second author together with X. Droubay and G. Pirillo observed that any finite word w w of length | w | |w| contains at most | w | + 1 |w|+1 distinct palindromes (including the empty word). Even further, they proved that a word w w contains exactly | w | + 1 |w|+1 distinct palindromes if and only if the longest palindromic suffix of any prefix p p of w w occurs exactly once in p p (i.e., every prefix of w w has Property J ​ u Ju [13]). Such words are ‘rich’ in palindromes in the sense that they contain the maximum number of different palindromic factors. Accordingly, we say that a finite word w w is rich if it contains exactly | w | + 1 |w|+1 distinct palindromes (or equivalently, if every prefix of w w has Property J ​ u Ju). Naturally, an infinite word is rich if all of its factors are rich. In independent work, P. Ambrož, C. Frougny, Z. Masáková, E. Pelantová [2] have considered the same class of words which they call full words, following earlier work of S. Brlek, S. Hamel, M. Nivat, and C. Reutenauer in [7].

In [13], the second author together with X. Droubay and G. Pirillo showed that the family of episturmian words [13, 21], which includes the well-known Sturmian words, comprises a special class of rich infinite words. Specifically, they proved that if an infinite word 𝐰 \mathbf{w} is episturmian, then any factor u u of 𝐰 \mathbf{w} contains exactly | u | + 1 |u|+1 distinct palindromic factors. (See [5, 18, 24] for recent surveys on the theory of Sturmian and episturmian words.) Another special class of rich words consists of S. Fischler’s sequences with “abundant palindromic prefixes”, which were introduced and studied in [15] in relation to Diophantine approximation (see also [16]). Other examples of rich words have appeared in many different contexts; they include the complementation-symmetric sequences [1], certain words associated with β \beta -expansions where β \beta is a simple Parry number [2], and a class of words coding r r -interval exchange transformations [4].

In this paper we present the first study of rich words as a whole. Firstly, in Section 2, we prove several fundamental properties of rich words; in particular, we show that rich words are characterized by the property that all complete returns to any palindromic factor are palindromes (Theorem 2.14). We also give a more explicit description of periodic rich infinite words in Section 3 (Theorem 3.1).

In Section 4 we define almost rich words: they are infinite words for which only a finite number of prefixes do not satisfy Property J ​ u Ju. Such words can also be defined in terms of the defect of a finite word w w, which is the difference between | w | + 1 |w|+1 and the number of distinct palindromic factors of w w (see the work of Brlek et al. in [7] where periodic infinite words with bounded defect are characterized). With this concept, rich words are those with defect 0 0 and almost rich words are infinite words with bounded defect. ‘Defective words’ and related notions are studied in Section 4, where we also introduce the family of weakly rich words (which includes all rich words), defined as infinite words with the property that all complete returns to letters are palindromes.

In Section 5 we consider applications to the balance property: an infinite word over a finite alphabet 𝒜 \mathcal{A} is balanced if, for any two factors u u, v v of the same length, the number of x x ’s in each of u u and v v differs by at most 1 1 for each letter x ∈ 𝒜 x\in\mathcal{A}. (Sturmian words are exactly the aperiodic balanced infinite words on two letters.) First we describe the recurrent balanced rich infinite words: they are precisely the balanced episturmian words. We then go much further by classifying all recurrent balanced weakly rich words. As a corollary to our classification, we show that any such word on at least three letters is necessarily episturmian. Consequently, weakly rich words obey Fraenkel’s conjecture [17]. We also prove that a certain class of almost rich words obeys Fraenkel’s conjecture by showing that the recurrent balanced ones are episturmian or contain at least two distinct letters with the same frequency.

Lastly, in Section 6, we study the action of morphisms on (almost) rich words with particular interest in morphisms that preserve (almost) richness. Such morphisms belong to the class of P P -morphisms that was introduced by A. Hof, O. Knill, and B. Simon in [19] (see also the nice survey on palindromic complexity by J.-P. Allouche, M. Baake, J. Cassaigne, and D. Damanik [1]).

### 1.1 Notation and terminology

In what follows, 𝒜 \mathcal{A} denotes a finite alphabet, i.e., a finite non-empty set of symbols called letters. A finite *word*over 𝒜 \mathcal{A} is a finite sequence of letters from 𝒜 \mathcal{A}. The empty word ε \varepsilon is the empty sequence. Under the operation of concatenation, the set 𝒜 ∗ \mathcal{A}^{*} of all finite words over 𝒜 \mathcal{A} is a free monoid with identity element ε \varepsilon and set of generators 𝒜 \mathcal{A}. The set of non-empty words over 𝒜 \mathcal{A} is the free semigroup 𝒜 +:= 𝒜 ∗ ∖ { ε } \mathcal{A}^{+}:=\mathcal{A}^{*}\setminus\{\varepsilon\}.

A (right) *infinite word*𝐱 \mathbf{x} is a sequence indexed by ℕ + \mathbb{N}^{+} with values in 𝒜 \mathcal{A}, i.e., 𝐱 = x 1 x 2 x 3 ⋯ \mathbf{x}=x_{1}x_{2}x_{3}\cdots with each x i ∈ 𝒜 x_{i}\in\mathcal{A}. The set of all infinite words over 𝒜 \mathcal{A} is denoted by 𝒜 ω \mathcal{A}^{\omega}, and we define 𝒜 ∞:= 𝒜 ∗ ∪ 𝒜 ω \mathcal{A}^{\infty}:=\mathcal{A}^{*}\cup\mathcal{A}^{\omega}. An ultimately periodic infinite word can be written as u v ω = u v v v ⋯ uv^{\omega}=uvvv\cdots, for some u u, v ∈ 𝒜 ∗ v\in\mathcal{A}^{*}, v ≠ ε v\neq\varepsilon. If u = ε u=\varepsilon, then such a word is periodic. An infinite word that is not ultimately periodic is said to be aperiodic. For easier reading, infinite words are hereafter typed in boldface to distinguish them from finite words.

Given a finite word w = x 1 x 2 ⋯ x m ∈ 𝒜 + w=x_{1}x_{2}\cdots x_{m}\in\mathcal{A}^{+} with each x i ∈ 𝒜 x_{i}\in\mathcal{A}, the *length*of w w, denoted by | w | |w|, is equal to m m and we denote by | w | a |w|_{a} the number of occurrences of a letter a a in w w. By convention, the empy word is the unique word of length 0 0. We denote by w ~ \tilde{w} the reversal of w w, given by w ~ = x m ⋯ x 2 x 1 \tilde{w}=x_{m}\cdots x_{2}x_{1}. If w = w ~ w=\tilde{w}, then w w is called a palindrome. The empty word ε \varepsilon is assumed to be a palindrome.

A finite word z z is a factor of a finite or infinite word w ∈ 𝒜 ∞ w\in\mathcal{A}^{\infty} if w = u ​ z ​ v w=uzv for some u ∈ 𝒜 ∗ u\in\mathcal{A}^{*}, v ∈ 𝒜 ∞ v\in\mathcal{A}^{\infty}. In the special case u = ε u=\varepsilon (resp. v = ε v=\varepsilon), we call z z a prefix (resp. suffix) of w w. The set of all factors of w w is denoted by F ⁡ ( w) F(w) and the alphabet of w w is Alph ​ ( w):= F ​ ( w) ∩ 𝒜 \textrm{Alph}(w):=F(w)\cap\mathcal{A}. We say that F ⁡ ( w) F(w) is closed under reversal if for any u ∈ F ⁡ ( w) u\in F(w), u ~ ∈ F ⁡ ( w) \tilde{u}\in F(w). When w = p ​ s ∈ 𝒜 + w=ps\in\mathcal{A}^{+}, we often use the notation p − 1 ​ w p^{-1}w (resp. w ​ s − 1 ws^{-1}) to indicate the removal of the prefix p p (resp. suffix s s) of the word w w.

The palindromic (right-)closure of a word u u is the (unique) shortest palindrome u ( +) u^{(+)} having u u as a prefix [12]. That is, u ( +) = u ​ v − 1 ​ u ~ u^{(+)}=uv^{-1}\tilde{u}, where v v is the longest palindromic suffix of u u.

Given an infinite word 𝐱 = x 1 x 2 x 3 ⋯ \mathbf{x}=x_{1}x_{2}x_{3}\cdots, the shift map T \mathrm{T} is defined by T ⁡ ( 𝐱) = ( x i + 1) i ≥ 1 \mathrm{T}(\mathbf{x})=(x_{i+1})_{i\geq 1} and its k k -th iteration is denoted by T k \mathrm{T}^{k}. For finite words w ∈ 𝒜 + w\in\mathcal{A}^{+}, T \mathrm{T} acts circularly, i.e., if w = x ​ v w=xv where x ∈ 𝒜 x\in\mathcal{A}, then T ⁡ ( w) = v ​ x \mathrm{T}(w)=vx. The circular shifts T k ​ ( w) \mathrm{T}^{k}(w) with 1 ≤ k ≤ | w | − 1 1\leq k\leq|w|-1 are called *conjugates*of w w. A finite word is *primitive*if it is different from all of its conjugates (equivalently, if it is not a power of a shorter word).

A factor of an infinite word 𝐱 \mathbf{x} is *recurrent*in 𝐱 \mathbf{x} if it occurs infinitely often in 𝐱 \mathbf{x}, and 𝐱 \mathbf{x} itself is said to be *recurrent*if all of its factors are recurrent in it. Furthermore, 𝐱 \mathbf{x} is *uniformly recurrent*if for all n n there exists a number K ⁡ ( n) K(n) such that any factor of length at least K ⁡ ( n) K(n) contains all factors of length n n in 𝐱 \mathbf{x} (equivalently, if any factor of 𝐱 \mathbf{x} occurs infinitely many times in 𝐱 \mathbf{x} with bounded gaps [10]).

Let 𝒜 \mathcal{A}, ℬ \mathcal{B} be two finite alphabets. A morphism φ \varphi of 𝒜 ∗ \mathcal{A}^{*} into ℬ ∗ \mathcal{B}^{*} is a map φ: 𝒜 ∗ → ℬ ∗ \varphi:\mathcal{A}^{*}\rightarrow\mathcal{B}^{*} such that φ ⁡ ( u ​ v) = φ ⁡ ( u) ​ φ ​ ( v) \varphi(uv)=\varphi(u)\varphi(v) for any words u u, v v over 𝒜 \mathcal{A}. A morphism on 𝒜 \mathcal{A} is a morphism from 𝒜 ∗ \mathcal{A}^{*} into itself. A morphism is entirely defined by the images of letters. All morphisms considered in this paper will be non-erasing, so that the image of any non-empty word is never empty. Hence the action of a morphism φ \varphi on 𝒜 ∗ \mathcal{A}^{*} naturally extends to infinite words; that is, if 𝐱 = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \mathbf{x}=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega}, then φ ( 𝐱) = φ ( x 1) φ ( x 2) φ ( x 3) ⋯ \varphi(\mathbf{x})=\varphi(x_{1})\varphi(x_{2})\varphi(x_{3})\cdots. An infinite word 𝐱 \mathbf{x} can therefore be a fixed point of a morphism φ \varphi, i.e., φ ⁡ ( 𝐱) = 𝐱 \varphi(\mathbf{x})=\mathbf{x}. If φ \varphi is a (non-erasing) morphism such that φ ⁡ ( a) = a ​ w \varphi(a)=aw for some letter a ∈ 𝒜 a\in\mathcal{A} and w ∈ 𝒜 + w\in\mathcal{A}^{+}, then φ \varphi is said to be *prolongable*on a a. In this case, the word φ n ​ ( a) \varphi^{n}(a) is a proper prefix of the word φ n + 1 ​ ( a) \varphi^{n+1}(a) for each n ∈ ℕ n\in\mathbb{N}, and the limit of the sequence ( φ n ​ ( a)) n ≥ 0 (\varphi^{n}(a))_{n\geq 0} is the unique infinite word:

 | 𝐰 = lim n → ∞ φ n ( a) = φ ω ( a) ( = a w φ ( w) φ 2 ( w) φ 3 ( w) ⋯). \mathbf{w}=\underset{n\rightarrow\infty}{\lim}\varphi^{n}(a)=\varphi^{\omega}(a)~(=aw\varphi(w)\varphi^{2}(w)\varphi^{3}(w)\cdots). |  |

Clearly, 𝐰 \mathbf{w} is a fixed point of φ \varphi and we say that 𝐰 \mathbf{w} is *generated*by φ \varphi.

A morphism φ \varphi on 𝒜 \mathcal{A} is said to be primitive if there exists a positive integer k k such that, for all x ∈ 𝒜 x\in\mathcal{A}, φ k ​ ( x) \varphi^{k}(x) contains all of the letters of 𝒜 \mathcal{A}. Any prolongable primitive morphism generates a uniformly recurrent infinite word [27].

For other basic notions and concepts in combinatorics on words, see for instance the Lothaire books [23, 24].

## 2 Definitions and basic properties

In this section, we prove several fundamental properties of rich words. First we recall a number of facts already mentioned in the introduction.

###### Proposition 2.1.

[13, Prop. 2] A word w w has at most | w | + 1 |w|+1 distinct palindromic factors.

###### Definition 2.2.

A word w w is rich if it has exactly | w | + 1 |w|+1 distinct palindromic factors.

###### Definition 2.3.

A factor u u of a word w w is said to be unioccurrent in w w if u u has exactly one occurrence in w w.

###### Proposition 2.4.

[13, Prop. 3] A word w w is rich if and only if all of its prefixes (resp. suffixes) have a unioccurrent palindromic suffix (resp. prefix).

###### Corollary 2.5.

If w w is rich, then:

1. i)

it has exactly one unioccurrent palindromic suffix (or *ups*for short);

2. ii)

all of its factors are rich;

3. iii)

its reversal w ~ \tilde{w} is also rich. ∎

###### Note.

OPEN i) i) is Property J ​ u Ju from [13].

Clearly, if w w has a ups, u u say, then u u is the only ups of w w, and moreover u u is the longest palindromic suffix of w w. So if w = v ​ u w=vu, then w ( +) = v ​ u ​ v ~ w^{(+)}=vu\tilde{v}. Furthermore:

###### Proposition 2.6.

Palindromic closure preserves richness.

###### Proof.

Let w w be rich with ups u u. The case w = u w=u is trivial. Now suppose w = f ​ u w=fu for some (non-empty) word f = f ′ ​ x f=f^{\prime}x, x ∈ 𝒜 x\in\mathcal{A}. Then w ( +) = f ​ u ​ f ~ = f ′ ​ x ​ u ​ x ​ f ~ ′ w^{(+)}=fu\tilde{f}=f^{\prime}xux\tilde{f}^{\prime}. Clearly x ​ u ​ x xux is a ups of f ​ u ​ x fux, so continuing we see that all prefixes of f ​ u ​ f ~ fu\tilde{f} have a ups of the form h ​ u ​ h ~ hu\tilde{h} where h h is a suffix of f f. Thus w ( +) = f ​ u ​ f ~ w^{(+)}=fu\tilde{f} is rich. ∎

###### Proposition 2.7.

If w w and w ′ w^{\prime} are rich with the same set of palindromic factors, then they are abelianly equivalent, i.e., | w | x = | w ′ | x |w|_{x}=|w^{\prime}|_{x} for all letters x ∈ 𝒜 x\in\mathcal{A}.

###### Proof.

Any palindromic factor of w w (resp. w ′ w^{\prime}) ending (and hence beginning) with a letter x ∈ 𝒜 x\in\mathcal{A} is the ups of some prefix of w w (resp. w ′ w^{\prime}). Thus the number of x x ’s in w w (resp. w ′ w^{\prime}) is the number of palindromic factors ending with x x. ∎

###### Proposition 2.8.

Suppose w w is a rich word. Then there exist letters x x, z ∈ Alph ​ ( w) z\in\mbox{{Alph}}(w) such that w ​ x wx and z ​ w zw are rich.

###### Proof.

If w w is rich and not a palindrome, then let u u be its ups with | u | < | w | |u|<|w|. Then u u is preceded by some letter x x in w w, thus w ​ x wx has x ​ u ​ x xux as its ups, and hence w ​ x wx is rich. If, on the contrary, w w is a palindrome, let w = x ​ v w=xv and let u u be the ups of v v. If u = v u=v then v v is a palindrome so w = x ​ v w=xv gives v = x n v=x^{n} for some n n whence w ​ x = x n + 2 wx=x^{n+2} which is rich. If | u | < | v | |u|<|v| then let y y be the letter before u u in v v. Then y ​ u ​ y yuy is ups of v ​ y vy (because u u is the ups of v v). If y ​ u ​ y yuy is not the ups of w ​ y wy then it is a prefix of w w, but then u u is a prefix of v v, and as | u | < | v | |u|<|v|, u u occurs twice in v v, contradiction. Thus y ​ u ​ y yuy is the ups of w ​ y wy and this one is rich.

In view of Proposition 2.4, one can similarly show that z ​ w zw is rich for some letter z ∈ Alph ​ ( w) z\in\textrm{Alph}(w). ∎

###### Note.

In the case when w w is rich and not a palindrome, the fact that w ​ x wx is rich for some letter x ∈ Alph ​ ( w) x\in\textrm{Alph}(w) is a direct consequence of Proposition 2.6.

Naturally:

###### Definition 2.9.

An infinite word is rich if all of its factors are rich.

###### Proposition 2.10.

There exist recurrent rich infinite words that are not uniformly recurrent.

###### Proof.

Consider the infinite word 𝐭 \mathbf{t} generated by the morphism ( a ↦ a b a, b ↦ b b) (a\mapsto aba,\ b\mapsto bb) from [9]. It suffices to show (rather easily) that 𝐭 \mathbf{t} is rich. Similarly, the Cantor word of [26], or even a b a b 2 a b a b 3 a b a b 2 a b a b 4 a b a b 2 a b a b 3 a b a b 2 a b a b 5 ⋯ abab^{2}abab^{3}abab^{2}abab^{4}abab^{2}abab^{3}abab^{2}abab^{5}\cdots (fixed point of the morphism: a ↦ a ​ b ​ a ​ b a\mapsto abab, b ↦ b b\mapsto b) are recurrent rich infinite words that are not uniformly recurrent. ∎

###### Proposition 2.11.

A rich infinite word 𝐬 \mathbf{s} is recurrent if and only if its set of factors F ⁡ ( 𝐬) F(\mathbf{s}) is closed under reversal.

The proof of this proposition uses the following lemma. Note that “richness” is not necessary for the “if” part.

###### Lemma 2.12.

A recurrent rich infinite word has infinitely many palindromic prefixes.

###### Proof.

Let v 1 v_{1} be a non-empty prefix of a recurrent rich infinite word 𝐬 \mathbf{s}. Being rich, v 1 v_{1} has a unioccurrent palindromic prefix, u 1 u_{1} say (by Proposition 2.4). Let v 2 v_{2} be a prefix of 𝐬 \mathbf{s} containing a second occurrence of u 1 u_{1}. It has a unioccurrent palindromic prefix, u 2 u_{2} say. Now, u 2 u_{2} is not a prefix of u 1 u_{1} because u 1 u_{1} is not unioccurrent in v 2 v_{2}, thus | u 2 | > | u 1 | |u_{2}|>|u_{1}|. ∎

###### Remark 2.13.

Although the well-known Thue-Morse word 𝐦 \mathbf{m}, which is the fixed point of the morphism μ: a ↦ a ​ b, b ↦ b ​ a \mu:a\mapsto ab,b\mapsto ba beginning with a a, contains arbitrarily long palindromes (see Example 4.10 later), 𝐦 \mathbf{m} is not rich. For instance, the prefix a ​ b ​ b ​ a ​ b ​ a ​ a ​ b ​ b ​ a abbabaabba is not rich (since its longest palindromic suffix a ​ b ​ b ​ a abba is not unioccurrent in it).

###### Proof of Proposition 2.11.

IF: Consider some occurrence of a factor u u in 𝐬 \mathbf{s} and let v v be a prefix of 𝐬 \mathbf{s} containing u u. As F ⁡ ( 𝐬) F(\mathbf{s}) is closed under reversal, v ~ ∈ F ⁡ ( 𝐬) \tilde{v}\in F(\mathbf{s}). Thus, if v v is long enough, there is an occurrence of u ~ \tilde{u} strictly on the right of this particular occurrence of u u in 𝐬 \mathbf{s}. Similarly u u occurs on the right of this u ~ \tilde{u} and thus u u is recurrent in 𝐬 \mathbf{s}.

ONLY IF: As 𝐬 \mathbf{s} is recurrent, it follows from Lemma 2.12 that F ⁡ ( 𝐬) F(\mathbf{s}) is closed under reversal. ∎

###### Theorem 2.14.

For any finite or infinite word w w, the following properties are equivalent:

- i)

w w is rich;

- ii)

for any factor u u of w w, if u u contains exactly two occurrences of a palindrome p p as a prefix and as a suffix only, then u u is itself a palindrome.

###### Proof.

OPEN OPEN i) ⇒ i ​ i) i)\Rightarrow ii): Suppose, on the contrary, OPEN i ​ i) ii) does not hold for rich w w. Then w w contains a non-palindromic factor u u having exactly two occurrences of a palindrome p p as a prefix and as a suffix only. Moreover, these two occurrences of p p in u u cannot overlap. Otherwise u = p ​ v − 1 ​ p u=pv^{-1}p for some word v v such that p = v ​ f = g ​ v = v ~ ​ g ~ = p ~ p=vf=gv=\tilde{v}\tilde{g}=\tilde{p}; whence v = v ~ v=\tilde{v} and u = g ​ v ~ ​ g ~ = g ​ v ​ g ~ u=g\tilde{v}\tilde{g}=gv\tilde{g}, a palindrome. So u = p ​ z ​ p u=pzp where z z is a non-palindromic word. We easily see that u u does not have a ups; thus u u is not rich, a contradiction.

OPEN OPEN i ​ i) ⇒ i) ii)\Rightarrow i): Otherwise, let u u be a factor of w w of minimal length satisfying OPEN i ​ i) ii) and not rich. Trivially | u | > 2 |u|>2, so let u = x ​ v ​ y u=xvy with x, y ∈ 𝒜 x,y\in\mathcal{A}. Then x ​ v xv is rich by the minimality of u u. Since u u is not rich whilst x ​ v xv is rich, the longest palindromic suffix p p of u u occurs more than once in u u. Hence, by OPEN i ​ i) ii) we reach a contradiction to the maximality of p p. ∎

###### Remark 2.15.

Given a finite or infinite word w w and a factor u u of w w, we say that a factor r r of w w is a complete return to u u in w w if r r contains exactly two occurrences of u u, one as a prefix and one as a suffix ( cf. ‘first returns’ in [20]). With this notion, Property OPEN i ​ i) ii) says that all complete returns to any palindromic factor are themselves palindromes. In particular, consecutive occurrences of a letter x x in a rich word are separated by palindromes.

###### Note.

In view of Theorem 2.14, an alternative proof of the richness of episturmian words can be found in the paper [3] where the fourth author, together with V. Anne and I. Zorca, proved that for episturmian words, all complete returns to palindromes are palindromes. See also [22] for further work on ‘return words’ in Sturmian and episturmian words.

## 3 Periodic rich infinite words

Theorem 2.14 provides a characterization of rich infinite words by complete returns to palindromes. We now give a more explicit description of periodic rich infinite words.

###### Theorem 3.1.

For a finite word w w, the following properties are equivalent:

- i)

w ω w^{\omega} is rich;

- ii)

w 2 w^{2} is rich;

- iii)

w w is a product of two palindromes and all of the conjugates of w w (including itself) are rich.

###### Example 3.2.

( a ​ a ​ b ​ b ​ a ​ a ​ b ​ a ​ b) ω (aabbaabab)^{\omega} and ( a ​ b ​ c ​ b ​ a) ω (abcba)^{\omega} are rich.

The proof of Theorem 3.1 requires several lemmas. In what follows, x x and z z always denote letters.

###### Lemma 3.3.

If u u is rich and u ​ x ux has a palindromic suffix r r such that 2 ​ | r | ≥ | u | 2|r|\geq|u|, then u ​ x ux is rich.

###### Proof.

We can suppose r r has maximal length. If r r has another occurrence in u ​ x ux, then, as 2 ​ | r | + 1 ≥ | u ​ x | 2|r|+1\geq|ux|, the two occurrences overlap or are separated by at most one letter. Thus they both form a palindrome which is a suffix of u ​ x ux and is strictly longer than r r, a contradiction. Therefore r r is the ups of u ​ x ux, which is rich. ∎

###### Lemma 3.4.

If w = p ​ q w=pq, p, q p,q palindromes, then w w has a conjugate w ′ = p ′ ​ q ′ w^{\prime}=p^{\prime}q^{\prime}, p ′, q ′ p^{\prime},q^{\prime} palindromes with | | p ′ | − | q ′ | | ≤ 2 ||p^{\prime}|-|q^{\prime}||\leq 2.

###### Proof.

Easy. ∎

###### Lemma 3.5.

If w = p ​ q w=pq, p, q p,q palindromes, is rich and 2 ​ | q | ≥ | w | − 4 2|q|\geq|w|-4 (resp. 2 ​ | p | ≥ | w | − 4 2|p|\geq|w|-4), then p ​ q ​ p pqp (resp. q ​ p ​ q qpq) is rich.

###### Proof.

Suppose 2 ​ | q | ≥ | w | − 4 2|q|\geq|w|-4 (the other case is obtained by reversal as w ~ \tilde{w} is rich). If p ​ q ​ p pqp is not rich, let v ​ z vz, v ∈ 𝒜 ∗ v\in\mathcal{A}^{*}, be the shorter prefix of p p such that p ​ q ​ v ​ z pqvz is not rich. Further, let r r be the longest palindromic suffix of p ​ q ​ v ​ z pqvz. Then, as z ​ v ~ ​ q ​ v ​ z z\tilde{v}qvz is a suffix of p ​ q ​ v ​ z pqvz, we have | r | ≥ | q | + 2 ​ | v | + 2 |r|\geq|q|+2|v|+2; whence 2 ​ | r | ≥ 2 ​ | q | + 4 ​ | v | + 4 ≥ | w | + 4 | v | ≥ | w | 2|r|\geq 2|q|+4|v|+4\geq|w|+4|v|\geq|w|. Then by Lemma 3.3 p ​ q ​ v ​ z pqvz is rich, contradiction. ∎

###### Lemma 3.6.

If w = p ​ q w=pq, p, q p,q palindromes, and p ​ q ​ p, q ​ p ​ q pqp,qpq are rich, then w 2 w^{2} is rich.

###### Proof.

If w 2 = p ​ q ​ p ​ q w^{2}=pqpq is not rich, let v ​ z vz be the shorter prefix of q q such that p ​ q ​ p ​ v ​ z pqpvz is not rich. As q ​ p ​ q qpq is rich, its prefix q ​ p ​ v ​ z qpvz has a ups, r r say. As z ​ v ~ ​ p ​ v ​ z z\tilde{v}pvz is a palindromic suffix of q ​ p ​ v ​ z qpvz, r r must begin in the prefix q q of q ​ p ​ v ​ z qpvz. As r r is not the ups of p ​ q ​ p ​ v ​ z pqpvz, consider its leftmost occurrence in p ​ q ​ p ​ v ​ z pqpvz. If the two occurrences overlap or are separated by at most one letter, both they form a palindromic suffix of p ​ q ​ p ​ v ​ z pqpvz. As this one is not the ups of p ​ q ​ p ​ v ​ z pqpvz, it has another occurrence; whence r r has another occurrence on the left of the leftmost one, contradiction.

Thus, the two considered occurrences of r r do not overlap. This implies that the leftmost occurrence of r r lies in the prefix p ​ q pq of p ​ q ​ p ​ v ​ z pqpvz, but then by reversal r r also occurs in q ​ p qp, hence r r is not the ups of q ​ p ​ v ​ z qpvz, contradiction. ∎

###### Proof of Theorem 3.1.

OPEN OPEN i) ⇒ i ​ i) i)\Rightarrow ii): Trivial.

OPEN OPEN i ​ i) ⇒ i ​ i ​ i) ii)\Rightarrow iii): It suffices to show that w w is a product of two palindromes. Let r r be the ups of w 2 w^{2}. Then, clearly | r | > | w | |r|>|w|, thus r = q ​ w r=qw and w = p ​ q w=pq for some p, q p,q. Therefore r = q ​ p ​ q = q ~ ​ p ~ ​ q ~ r=qpq=\tilde{q}\tilde{p}\tilde{q}, whence p p and q q are palindromes.

OPEN OPEN i ​ i) ⇒ i) ii)\Rightarrow i): We show first that w 3 w^{3} is rich. By OPEN i ​ i ​ i) iii), w 2 w^{2} has a ups q ​ w qw and w = p ​ q w=pq, p, q p,q palindromes. For any u, v u,v such that u ​ v = p uv=p, consider f = w 2 ​ u f=w^{2}u. Observe that f f has a palindromic suffix u ~ ​ q ​ p ​ q ​ u \tilde{u}qpqu which is its ups, otherwise q ​ p ​ q qpq would not be the ups of w 2 w^{2}. Thus all such f f are rich, in particular w 2 ​ p w^{2}p is rich. Now, if e ​ z ez is a prefix of q q, we show by induction on | e | |e| that w 2 ​ p ​ e ​ z w^{2}pez is rich. Let r r be the longest palindromic suffix of w 2 ​ p ​ e ​ z w^{2}pez. As this one has suffix z ​ e ~ ​ p ​ q ​ p ​ e ​ z z\tilde{e}pqpez, we have | r | ≥ 2 ​ | p | + | q | + 2 | e | + 2 |r|\geq 2|p|+|q|+2|e|+2; whence 2 ​ | r | ≥ | w 2 ​ p ​ e ​ z | 2|r|\geq|w^{2}pez|. Thus, by Lemma 3.3, w 2 ​ p ​ e ​ z w^{2}pez is rich, and hence w 3 w^{3} is rich.

Now denote by 𝐬 n \mathbf{s}_{n} the prefix of length n n of 𝐬 = w ω \mathbf{s}=w^{\omega}. We show by induction on n n that w 3 ​ 𝐬 n w^{3}\mathbf{s}_{n} is rich. Let r r be the ups of w 2 ​ 𝐬 n w^{2}\mathbf{s}_{n}. Then r r is also a suffix of w 3 ​ 𝐬 n w^{3}\mathbf{s}_{n}. Clearly these two occurrences of r r overlap, thus both give a palindromic suffix of w 3 ​ 𝐬 n w^{3}\mathbf{s}_{n}. If this one were not the ups of w 3 ​ 𝐬 n w^{3}\mathbf{s}_{n}, there would be another occurrence of r r in w 2 ​ 𝐬 n w^{2}\mathbf{s}_{n}, contradiction. Thus w 3 ​ 𝐬 n w^{3}\mathbf{s}_{n} has a ups and, as w 3 ​ 𝐬 n − 1 w^{3}\mathbf{s}_{n-1} is rich, it is rich too.

OPEN OPEN i ​ i ​ i) ⇒ i) iii)\Rightarrow i): By Lemma 3.4, w w has a (rich) conjugate w ′ = p ′ ​ q ′ w^{\prime}=p^{\prime}q^{\prime} with p ′, q ′ p^{\prime},q^{\prime} palindromes and | | p ′ | − | q ′ | | ≤ 2 ||p^{\prime}|-|q^{\prime}||\leq 2, whence by Lemma 3.5 p ′ ​ q ′ ​ p ′ p^{\prime}q^{\prime}p^{\prime} and q ′ ​ p ′ ​ q ′ q^{\prime}p^{\prime}q^{\prime} are rich. Thus by Lemma 3.6 ( w ′) 2 (w^{\prime})^{2} is rich. So, using part “ OPEN OPEN i ​ i) ⇒ i) ii)\Rightarrow i) ”, ( w ′) ω (w^{\prime})^{\omega} is rich, and so too is w ω w^{\omega}. ∎

###### Remark 3.7.

For OPEN i ​ i ​ i) iii) the hypothesis that all of the conjugates of w w are rich is not sufficient: a ​ b ​ c abc is so, but ( a ​ b ​ c) ω (abc)^{\omega} is not rich. The hypothesis that w w is rich and a product of two palindromes is not sufficient: w = b ​ a 2 ​ b ​ a ​ b 2 ​ a ​ b ​ a 2 ​ b w=ba^{2}bab^{2}aba^{2}b is a rich palindrome, but T ⁡ ( w) = a 2 ​ b ​ a ​ b 2 ​ a ​ b ​ a 2 ​ b 2 \mathrm{T}(w)=a^{2}bab^{2}aba^{2}b^{2} is not rich.

## 4 Some related words

### 4.1 Defects & oddities

The defect [7] of a finite word w w is defined by

 | D ⁡ ( w) = | w | + 1 − | PAL ⁡ ( w) |, D(w)=|w|+1-|\mathrm{PAL}(w)|, |  |

where PAL ⁡ ( w) \mathrm{PAL}(w) denotes the set of distinct palindromic factors of w w (including ε \varepsilon). This definition naturally extends to infinite words 𝐰 ∈ 𝒜 ω \mathbf{w}\in\mathcal{A}^{\omega} by setting D ⁡ ( 𝐰) D(\mathbf{w}) equal to the maximum defect of the factors of 𝐰 \mathbf{w}. In fact, this definition may be refined by observing that if u u is a factor of a word v v, then D ⁡ ( u) ≤ D ⁡ ( v) D(u)\leq D(v) (see [7]); thus

 | D ⁡ ( 𝐰) = max ⁡ { D ⁡ ( u) | u is a prefix of 𝐰 }. D(\mathbf{w})=\max\{D(u)~|~\mbox{$u$ is a prefix of $\mathbf{w}$}\}. |  |

With this notion, finite or infinite rich words are exactly those with defect equal to 0 0 (called full words in [2, 7]). Accordingly, we say that an infinite word with bounded defect is almost rich. Such infinite words contain only a finite number of prefixes that do not have a ups.

###### Notation.

Let 𝐭 n \mathbf{t}_{n} denote the prefix of length n n of a given finite or infinite word 𝐭 \mathbf{t}.

###### Proposition 4.1.

If 𝐭 n \mathbf{t}_{n} has a ups, then D ⁡ ( 𝐭 n) = D ⁡ ( 𝐭 n − 1) D(\mathbf{t}_{n})=D(\mathbf{t}_{n-1}), otherwise D ⁡ ( 𝐭 n) = D ⁡ ( 𝐭 n − 1) + 1 D(\mathbf{t}_{n})=D(\mathbf{t}_{n-1})+1.

###### Proof.

If 𝐭 n \mathbf{t}_{n} has a ups, then 𝐭 n \mathbf{t}_{n} contains one more palindromic factor than 𝐭 n − 1 \mathbf{t}_{n-1}, whence D ⁡ ( 𝐭 n) = D ⁡ ( 𝐭 n − 1) D(\mathbf{t}_{n})=D(\mathbf{t}_{n-1}). On the other hand, if 𝐭 n \mathbf{t}_{n} has no ups, then 𝐭 n \mathbf{t}_{n} has the same number of palindromic factors as 𝐭 n − 1 \mathbf{t}_{n-1}, thus D ⁡ ( 𝐭 n) = D ⁡ ( 𝐭 n − 1) + 1 D(\mathbf{t}_{n})=D(\mathbf{t}_{n-1})+1. ∎

In other words, if 𝐭 \mathbf{t} has defect k k, then there are exactly k k “defective” positions; hence it is appropriate to say that such a word 𝐭 \mathbf{t} has k k defects.

###### Remark 4.2.

A noteworthy fact is that for a given word w w with k k defects, the extension w ​ x wx, with x ∈ Alph ​ ( w) x\in\textrm{Alph}(w), may not have the same number of defects (in particular, the palindromic closure of w w may have greater defect). For example, w = c ​ a ​ c ​ a 2 ​ b ​ c ​ a w=caca^{2}bca has 2 defects, but w ​ x wx has 3 3 defects for x = a x=a, b b, or c c.

Periodic almost rich words have the following simple characterization.

###### Theorem 4.3.

A periodic infinite word w ω w^{\omega} is almost rich if and only if w w is a product of two palindromes.

###### Proof.

The “if” part follows immediately from [7, Theorem 6]: if p p, q q are palindromes and p ​ q pq is a primitive word, then the defect of ( p ​ q) ω (pq)^{\omega} is bounded by the defect of its prefix of length | p ​ q | + ⌊ | | p | − | q | | 3 ⌋ |pq|+\lfloor\frac{||p|-|q||}{3}\rfloor. Conversely, if w ω w^{\omega} is almost rich, then, for large enough n n, w n w^{n} has a ups. Thus, as in the proof of OPEN OPEN i ​ i) ⇒ i ​ i ​ i) ii)\Rightarrow iii) of Theorem 3.1, we get w = q ​ p w=qp for some palindromes p p, q q. ∎

###### Proposition 4.4.

If an almost rich word 𝐭 \mathbf{t} is recurrent, then F ⁡ ( 𝐭) F(\mathbf{t}) is closed under reversal.

###### Proof.

Let u u be any prefix of 𝐭 \mathbf{t} with the same defect number k k as 𝐭 \mathbf{t}. By recurrence, we can consider another occurrence of u u such that 𝐭 = s u ⋯ \mathbf{t}=su\cdots for some non-empty word s s. Then, any suffix s ′ ​ u s^{\prime}u of s ​ u su has a ups since every prefix v v of 𝐭 \mathbf{t} with | v | > | u | |v|>|u| has a ups (otherwise the defect of 𝐭 \mathbf{t} would be greater than k k, by Proposition 4.1). In particular, s ​ u su has a ups, p p say. Now, p p is not a suffix of u u because u u is not unioccurrent in s ​ u su, so | p | > | u | |p|>|u| and we have p = v ​ u = u ~ ​ v ~ p=vu=\tilde{u}\tilde{v} for some non-empty word v v. Thus u u and u ~ \tilde{u} are both factors of 𝐭 \mathbf{t}, and hence F ⁡ ( 𝐭) F(\mathbf{t}) is closed under reversal. ∎

###### Definition 4.5.

The pair { w, w ~ } \{w,\tilde{w}\} is an oddity of a finite or infinite word 𝐭 \mathbf{t} if either w w or w ~ \tilde{w} (or both!) is a non-palindromic complete return to some non-empty palindromic factor of 𝐭 \mathbf{t} (called the incriminated palindrome).

###### Note.

An oddity of a finite or infinite word 𝐭 \mathbf{t} takes the form p ​ u ​ p pup where p p is the incriminated palindrome and u u is a non-palindromic word. Indeed, non-palindromic complete returns to any palindrome p p are necessarily longer than 2 ​ | p | + 1 2|p|+1 (see the proof of Theorem 2.14).

Let O ⁡ ( 𝐭) O(\mathbf{t}) denote the number of oddities of 𝐭 \mathbf{t}.

###### Proposition 4.6.

O ⁡ ( 𝐭) ≤ D ⁡ ( 𝐭) O(\mathbf{t})\leq D(\mathbf{t}).

###### Proof.

Let w = p ​ u ​ p w=pup be an oddity of 𝐭 \mathbf{t} with p p the incriminated palindrome. Let n n be the minimal integer such that w w or w ~ \tilde{w} occurs in 𝐭 n \mathbf{t}_{n} (thus as a suffix). If 𝐭 n \mathbf{t}_{n} has a ups, q q say, then | q | > | p | |q|>|p|, trivial. If | q | < | w | |q|<|w|, then the prefix p p of q q occurs in the interior of the complete return w = p ​ u ​ p w=pup, impossible. If | q | > | w | |q|>|w| then w ~ \tilde{w} occurs as a prefix of q q, in contradiction with minimality of n n. Thus 𝐭 n \mathbf{t}_{n} does not have a ups, i.e., n n is a defective position. Thus each oddity gives a defect. For achieving the proof we have to show that n n cannot be the same for two different oddities. Suppose 𝐭 n \mathbf{t}_{n} has a second (suffix) oddity w ′ = q ​ v ​ q w^{\prime}=qvq. If | p | = | q | |p|=|q|, clearly w ′ = w w^{\prime}=w. Otherwise let | q | < | p | |q|<|p| for instance, then q q occurs twice in p p, thus w ′ w^{\prime} is a suffix of p p, hence w ~ ′ \tilde{w}^{\prime} is a prefix of p p, contradicting the minimality of n n. ∎

###### Example 4.7.

We may have O ⁡ ( 𝐭) < D ⁡ ( 𝐭) O(\mathbf{t})<D(\mathbf{t}); for instance the periodic word ( a ​ b ​ c ​ a ​ b ​ c ​ a ​ c ​ b ​ a ​ c ​ b) ω (abcabcacbacb)^{\omega} has 3 oddities ( a ​ b ​ c ​ a abca, b ​ c ​ a ​ b bcab, c ​ a ​ b ​ c cabc) ending at positions 4 4, 5 5, 6 6, but 4 defects at positions 4 4, 5 5, 6 6, 7 7. The periodic infinite word ( a ​ b ​ c) ω (abc)^{\omega} has a defect at each position n ≥ 4 n\geq 4 but only three oddities ( a ​ b ​ c ​ a abca, b ​ c ​ a ​ b bcab, c ​ a ​ b ​ c cabc). So infinitely many defects do not necessarily give rise to infinitely many oddities.

###### Proposition 4.8.

A uniformly recurrent infinite word has infinitely many oddities if and only if it has infinitely many palindromic factors and infinitely many defects.

###### Proof.

ONLY IF: Suppose 𝐬 \mathbf{s} is a uniformly recurrent infinite word with infinitely many oddities. Clearly, 𝐬 \mathbf{s} has infinitely many defects as D ⁡ ( 𝐬) ≥ O ⁡ ( 𝐬) D(\mathbf{s})\geq O(\mathbf{s}) by Proposition 4.6. Moreover, 𝐬 \mathbf{s} must have infinitely many palindromic factors. Otherwise, if 𝐬 \mathbf{s} contains only a finite number of palindromes, then each of its palindromic factors has only a finite number of different return words (and hence only a finite number of non-palindromic complete returns) as 𝐬 \mathbf{s} is uniformly recurrent. Hence 𝐬 \mathbf{s} has only finitely many oddities, a contradiction.

IF: Suppose, by way of contradiction, 𝐬 \mathbf{s} is a (uniformly recurrent) infinite word with infinitely many palindromic factors and infinitely many defects, but only a finite number of oddities. Then there are only finitely many palindromic factors of 𝐬 \mathbf{s} that are incriminated by the oddities and the longest of these palindromes has length L L, say. Since 𝐬 \mathbf{s} contains infinitely many palindromes, it has infinitely many ‘non-defective’ positions. Thus there exists an arbitrarily large n n such that n n is a defective position and such that the prefix 𝐬 n + 1 = 𝐬 n ​ x \mathbf{s}_{n+1}=\mathbf{s}_{n}x, with x ∈ 𝒜 x\in\mathcal{A}, has a ups q q, with | q | > L + 2 |q|>L+2. Thus, with q = x ​ q ′ ​ x q=xq^{\prime}x, we see that q ′ q^{\prime} is a palindromic suffix of 𝐬 n \mathbf{s}_{n}. Let r r be the longest palindromic suffix of 𝐬 n \mathbf{s}_{n}. As n n is a defective position, r r has another occurrence in 𝐬 n \mathbf{s}_{n} and r ​ u ​ r rur is a non-palindromic complete return to r r, which is a contradiction since | r | ≥ | q ′ | > L |r|\geq|q^{\prime}|>L. ∎

###### Remark 4.9.

Uniform recurrence is necessary for the “only if” part of the above proposition (but useless for the “if” part). For example, with v 1 = a ​ b ​ c ​ d v_{1}=abcd and v n = v n − 1 ​ ( a ​ b ​ c) n ​ d v_{n}=v_{n-1}(abc)^{n}d for n ≥ 2 n\geq 2, the (non-uniformly) recurrent infinite word v 1 v 2 v 3 ⋯ v_{1}v_{2}v_{3}\cdots has infinitely many oddities, but only five palindromic factors: ε \varepsilon, a a, b b, c c, d d.

###### Example 4.10.

The Thue-Morse word 𝐦 \mathbf{m} has infinitely many oddities. Indeed, since 𝐦 \mathbf{m} is generated by the morphism μ 2: a ↦ a ​ b ​ b ​ a, b ↦ b ​ a ​ a ​ b \mu^{2}:a\mapsto abba,b\mapsto baab, 𝐦 \mathbf{m} clearly contains infinitely many palindromes. Moreover, one can prove by induction that 𝐦 \mathbf{m} has infinitely many defects occurring in runs of length 2 2 ​ n + 1 2^{2n+1} starting at positions 2 2 ​ n + 3 + 1 2^{2n+3}+1 and 2 2 ​ n + 4 + 2 2 ​ n + 3 + 1 2^{2n+4}+2^{2n+3}+1 for n ≥ 0 n\geq 0.

### 4.2 Weakly rich words

We say that an infinite word 𝐰 \mathbf{w} over 𝒜 \mathcal{A} is weakly rich (or simply a WR-word for short) if for every a ∈ 𝒜 a\in\mathcal{A}, all complete returns to a a in 𝐰 \mathbf{w} are palindromes. This class of words contains all rich words but is in fact a much larger class. Clearly every binary word is weakly rich but not necessarily rich. The periodic infinite word ( a ​ a ​ c ​ b ​ c ​ c ​ b ​ c ​ a ​ c ​ b ​ c) ω (aacbccbcacbc)^{\omega} is readily verified to be weakly rich but not rich (since the complete return to a ​ a aa is not a palindrome). Note, however, that the family of weakly rich words neither contains nor is contained in the family of almost rich words. Indeed, the WR-word ( a ​ a ​ c ​ b ​ c ​ c ​ b ​ c ​ a ​ c ​ b ​ c) ω (aacbccbcacbc)^{\omega} has infinite defect (since it does not take the form ( p ​ q) ω (pq)^{\omega} with p p, q q palindromes, and hence contains only finitely many distinct palindromic factors – see Theorem 4.3). There also exist almost rich words that are not weakly rich; for instance, the almost rich word ( a ​ a ​ b ​ a ​ c ​ a ​ b ​ a ​ a ​ c) ω (aabacabaac)^{\omega} (which has only 2 2 defects at positions 10 10 and 11 11) is not weakly rich as c ​ a ​ b ​ a ​ a ​ c cabaac is a non-palindromic complete return to c c.

Our motivation for introducing WR-words will become evident in the next section.

## 5 Applications to balance

A finite or infinite word is said to be balanced if, for any two of its factors u u, v v with | u | = | v | |u|=|v|, we have | | u | x − | ​ v | x | ≤ 1 ||u|_{x}-|v|_{x}|\leq 1 for any letter x x, i.e., the number of x x ’s in each of u u and v v differs by at most 1 1. Sturmian words are precisely the aperiodic balanced infinite words on a 2 2 -letter alphabet.

Fraenkel’s conjecture [17] is a well-known problem related to balance that arose in a number-theoretic context and has remained unsolved for over thirty years. Fraenkel conjectured that, for a fixed k ≥ 3 k\geq 3, there is only one covering of ℤ \mathbb{Z} by k k Beatty sequences of the form ( ⌊ α ​ n + β ⌋) n ≥ 1 (\lfloor\alpha n+\beta\rfloor)_{n\geq 1}, where α \alpha, β \beta are real numbers. A combinatorial interpretation of this conjecture may be stated as follows (taken from [25]). Over a k k -letter alphabet with k ≥ 3 k\geq 3, there is only one recurrent balanced infinite word, up to letter permutation and shifts, that has mutually distinct letter frequencies. This supposedly unique infinite word is called Fraenkel’s sequence and is given by ( F k) ω (F_{k})^{\omega} where the Fraenkel words ( F i) i ≥ 1 (F_{i})_{i\geq 1} are defined recursively by F 1 = 1 F_{1}=1 and F i = F i − 1 ​ i ​ F i − 1 F_{i}=F_{i-1}iF_{i-1} for all i ≥ 2. i\geq 2. For further details, see [25] and references therein.

In [25], Paquin and Vuillon characterized balanced episturmian words by classifying these words into three families. Amongst these classes, only one has mutually distinct letter frequencies and, up to letter permutation and shifts, corresponds to Fraenkel’s sequence. That is:

###### Proposition 5.1.

[25] Suppose 𝐭 \mathbf{t} is a balanced episturmian word with Alph ​ ( 𝐭) = { 1, 2, …, k } \mbox{{Alph}}(\mathbf{t})=\{1,2,\ldots,k\}, k ≥ 3 k\geq 3. If 𝐭 \mathbf{t} has mutually distinct letter frequencies, then up to letter permutation, 𝐭 \mathbf{t} is a shift of ( F k) ω (F_{k})^{\omega}.

In this section, we first show that recurrent balanced rich infinite words are necessarily (balanced) episturmian words. Then, using a special map, we classify all recurrent balanced weakly rich words. As a corollary, we show that any such word (on at least three letters) is necessarily a (balanced) episturmian word. Thus, although WR-words constitute a larger class of words than episturmian words, the subset of those which are balanced coincides with those given by Paquin and Vuillon in [25]. Consequently, WR-words obey Fraenkel’s conjecture. Using techniques similar to those in the rich case, we also prove that a certain class of almost rich words (with only a few oddities) obeys Fraenkel’s conjecture by showing that the recurrent balanced ones are episturmian or contain at least two distinct letters with the same frequency.

Before proceeding, let us recall some useful well-known facts about balance (see for instance the survey [30] and references therein).

- •

In a balanced word, the gaps between successive occurrences of any letter x x belong to a pair { k, k + 1 } \left\{k,k+1\right\} for some integer k ≥ 0 k\geq 0.

- •

Any recurrent balanced infinite word with alphabet 𝒜 \mathcal{A} and | 𝒜 | > 2 |\mathcal{A}|>2 is periodic.

### 5.1 Balanced rich words

The main result of this section is the following theorem.

###### Theorem 5.2.

Recurrent balanced rich infinite words are precisely the balanced episturmian words.

First we prove some lemmas. For a given letter a a, we denote by ψ a \psi_{a} the morphism defined by ψ a: a ↦ a, x ↦ a ​ x \psi_{a}:a\mapsto a,x\mapsto ax for all letters x ≠ a x\neq a. A noteworthy property of ψ a \psi_{a} is that ψ a ​ ( w) ​ a \psi_{a}(w)a is a palindrome if and only if w w is a palindrome. It is well-known that an infinite word is epistandard if and only if it is generated by an infinite composition of the morphisms ψ x \psi_{x}. Moreover, an infinite word 𝐭 \mathbf{t} is episturmian if and only if F ⁡ ( 𝐭) = F ⁡ ( 𝐬) F(\mathbf{t})=F(\mathbf{s}) for some epistandard word 𝐬 \mathbf{s} (see [13, 21]).

###### Lemma 5.3.

Suppose 𝐬 = ψ a ​ ( 𝐭) \mathbf{s}=\psi_{a}(\mathbf{t}) for some letter a a and infinite word 𝐭 \mathbf{t}.

- i)

If 𝐬 \mathbf{s} is rich, then 𝐭 \mathbf{t} is rich.

- ii)

If 𝐬 \mathbf{s} is balanced, then 𝐭 \mathbf{t} is balanced.

###### Proof.

OPEN i) i): If false, let w ​ x ∈ F ⁡ ( 𝐭) wx\in F(\mathbf{t}) be minimal such that w ​ x wx is not rich. If x ≠ a x\neq a then let r r be the ups of ψ a ​ ( w ​ x) \psi_{a}(wx) which is rich by hypothesis. Then a ​ r = ψ a ​ ( h) ar=\psi_{a}(h) where h h is a palindromic suffix (but not a ups) of w ​ x wx. Thus h h has another occurrence in w ​ x wx, which implies r r has another occurrence in ψ a ​ ( w ​ x) \psi_{a}(wx), contradiction.

If x = a x=a we consider the ups of ψ a ​ ( w ​ a) ​ a = ψ a ​ ( w) ​ a ​ a \psi_{a}(wa)a=\psi_{a}(w)aa and by a similar argument we reach a contradiction.

OPEN i ​ i) ii): If 𝐭 \mathbf{t} is not balanced, then it contains two factors u u, v v of the same minimal length such that | | u | x − | ​ v | x | = 2 ||u|_{x}-|v|_{x}|=2 for some x x. Let U = ψ a ​ ( u) U=\psi_{a}(u), V = ψ a ​ ( v) V=\psi_{a}(v), then | U | = 2 ​ | u | − | u | a |U|=2|u|-|u|_{a} and | V | = 2 ​ | v | − | v | a |V|=2|v|-|v|_{a}. By adding to and/or deleting from U, V U,V some a a we get U ′, V ′ U^{\prime},V^{\prime} factors of 𝐬 \mathbf{s} of the same length. If x ≠ a x\neq a then | | U ′ | x − | ​ V ′ | x | = 2 ||U^{\prime}|_{x}-|V^{\prime}|_{x}|=2. If x = a x=a then, as | U | a = | u | = | v | = | V | a |U|_{a}=|u|=|v|=|V|_{a}, we get | | U ′ | a − | ​ V ′ | a | = 2 ||U^{\prime}|_{a}-|V^{\prime}|_{a}|=2. In both cases, 𝐬 \mathbf{s} is not balanced, contradiction. ∎

###### Remark 5.4.

If 𝐬 = ψ a ​ ( 𝐭) \mathbf{s}=\psi_{a}(\mathbf{t}) or 𝐬 = a − 1 ​ ψ a ​ ( 𝐭) \mathbf{s}=a^{-1}\psi_{a}(\mathbf{t}) for some letter a a and infinite word 𝐭 \mathbf{t}, then the letter a a is *separating for 𝐬 \mathbf{s}*and its factors; that is, any factor of 𝐬 \mathbf{s} of length 2 contains the letter a a.

###### Lemma 5.5.

Suppose 𝐭 \mathbf{t} is a recurrent infinite word with separating letter a a and first letter x ≠ a x\neq a. Then 𝐭 \mathbf{t} and a ​ 𝐭 a\mathbf{t} have the same set of factors.

###### Proof.

Clearly F ⁡ ( 𝐭) ⊆ F ⁡ ( a ​ 𝐭) F(\mathbf{t})\subseteq F(a\mathbf{t}). To show that F ⁡ ( a ​ 𝐭) ⊆ F ⁡ ( 𝐭) F(a\mathbf{t})\subseteq F(\mathbf{t}), let u u be any factor of a ​ 𝐭 a\mathbf{t}. If u = a u=a or u u is not a prefix of a ​ 𝐭 a\mathbf{t}, then clearly u ∈ F ⁡ ( 𝐭) u\in F(\mathbf{t}). Otherwise, if u ≠ a u\neq a is a prefix of a ​ 𝐭 a\mathbf{t}, then u u takes the form a ​ x ​ u ′ axu^{\prime} where x ​ u ′ xu^{\prime} is a prefix of 𝐭 \mathbf{t}. As 𝐭 \mathbf{t} is recurrent, x ​ u ′ xu^{\prime} occurs again in 𝐭 \mathbf{t}, and hence u = a ​ x ​ u ′ u=axu^{\prime} must be a factor of 𝐭 \mathbf{t} because the letter a a is separating for 𝐭 \mathbf{t}. ∎

This almost trivial lemma allows us to ignore the cases where the separating letter is not the first letter.

###### Proof of Theorem 5.2.

Let 𝐬 \mathbf{s} be a rich, recurrent and balanced infinite word. If 𝐬 \mathbf{s} has a separating letter, a a say, then 𝐬 = ψ a ​ ( 𝐭) \mathbf{s}=\psi_{a}(\mathbf{t}) or 𝐬 = a − 1 ​ ψ a ​ ( 𝐭) \mathbf{s}=a^{-1}\psi_{a}(\mathbf{t}) for some recurrent infinite word 𝐭 \mathbf{t}, which is also rich and balanced by Lemmas 5.3 and 5.5. If we can continue infinitely in this way then 𝐬 \mathbf{s} is episturmian by the work in [21]. Otherwise we arrive at some recurrent infinite word, rich and balanced, without a separating letter; call it 𝐭 \mathbf{t}. In particular, no x ​ x xx occurs in 𝐭 \mathbf{t} (because x x would be separating). We call such an infinite word without factor x ​ x xx, x ∈ 𝒜 x\in\mathcal{A}, a skeleton. Consider any factor of form x ​ p ​ x xpx of 𝐭 \mathbf{t} with p p x x -free. By Theorem 2.14, p p is a palindrome, and as no square of a letter occurs in it, p p has odd length. If x ​ p 1 ​ x xp_{1}x and x ​ p 2 ​ x xp_{2}x are two such factors of 𝐭 \mathbf{t}, then in view of balance, | p 1 | = | p 2 | |p_{1}|=|p_{2}|. Thus x x occurs in 𝐭 \mathbf{t} with period π x = | p i | + 1 \pi_{x}=|p_{i}|+1. Take for x ∈ 𝒜 x\in\mathcal{A} the letter with minimal π x \pi_{x} (i.e., the letter with the greatest frequency in 𝐭 \mathbf{t}). If y y is any other letter, as π y ≥ π x \pi_{y}\geq\pi_{x}, only one y y may occur in a x ​ p i ​ x xp_{i}x. By symmetry, this y y lies at the centre of p i p_{i}. Thus all p i p_{i} are reduced to their centre, i.e., π x = 2 \pi_{x}=2 and x x is separating, contradiction. So this case is impossible and 𝐬 \mathbf{s} is episturmian. ∎

As an immediate consequence of Proposition 5.1 and Theorem 5.2, we have:

###### Corollary 5.6.

Recurrent balanced rich infinite words with mutually distinct letter frequencies are Sturmian words or have the form given by Fraenkel’s conjecture. ∎

### 5.2 Balanced weakly rich words

We now establish a much stronger result, namely that WR-words obey Fraenkel’s conjecture, by proving that balanced WR-words on at least three letters are necessarily (balanced) episturmian words. First we classify all such words. In order to state our classification, we need the following notation.

Let 𝐱 = x 1 x 2 x 3 ⋯ ∈ 𝒜 ω \mathbf{x}=x_{1}x_{2}x_{3}\cdots\in\mathcal{A}^{\omega} with each x i ∈ 𝒜 x_{i}\in\mathcal{A}, and let a a be a new symbol not in 𝒜 \mathcal{A}. We define σ a: 𝒜 ω → ( 𝒜 ∪ { a }) ω \sigma_{a}:\mathcal{A}^{\omega}\rightarrow(\mathcal{A}\cup\{a\})^{\omega} by

 | σ a ​ ( 𝐱) = a ​ x 1 ​ a ϵ 1 ​ x 2 ​ a ϵ 2 ​ x 3 ​ a ϵ 3 ​ … \sigma_{a}(\mathbf{x})=ax_{1}a^{\epsilon_{1}}x_{2}a^{\epsilon_{2}}x_{3}a^{\epsilon_{3}}\ldots |  |

where ϵ i ∈ { 1, 2 }, \epsilon_{i}\in\{1,2\}, with ϵ i = 2 \epsilon_{i}=2 if and only if x i = x i + 1 x_{i}=x_{i+1}.

###### Theorem 5.7.

Suppose 𝐰 \mathbf{w} is a recurrent balanced WR-word with Alph ​ ( 𝐰) = { 1, 2, …, k } \mbox{{Alph}}(\mathbf{w})=\{1,2,\ldots,k\}, k ≥ 3 k\geq 3. Then, up to letter permutation, 𝐰 \mathbf{w} is either:

- OPEN 1) 1)

a shift of the periodic word

 | ψ 1 n ∘ ψ 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) for some n ≥ 1; \psi_{1}^{n}\circ\psi_{2}\circ\cdots\circ\psi_{k-1}(k^{\omega})\quad\mbox{for some $n\geq 1;$} |  |

- OPEN 2) 2)

or a shift of the periodic word

 | σ 1 ∘ σ 2 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) for some 1 ≤ j ≤ k − 2. \sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega})\quad\mbox{for some $1\leq j\leq k-2$.} |  |

The proof of Theorem 5.7 requires several lemmas. In what follows, we assume that Alph ​ ( 𝐰) = 𝒜 \textrm{Alph}(\mathbf{w})=\mathcal{A} with | 𝒜 | ≥ 3 |\mathcal{A}|\geq 3. For each a ∈ 𝒜 a\in\mathcal{A}, we set g a = sup | u | g_{a}=\sup|u| where the supremum is taken over all factors u u of 𝐰 \mathbf{w} not containing the letter a a.

First we recall a useful lemma from [29].

###### Lemma 5.8.

[29, Lemma 6] Suppose 𝐰 ∈ 𝒜 ω \mathbf{w}\in\mathcal{A}^{\omega} is balanced, and let a ∈ 𝒜 a\in\mathcal{A} be such that the frequency of a a in 𝐰 \mathbf{w} is at least 1 / 3 1/3. Then the word 𝐰 ′ ∈ ( 𝒜 ∖ { a }) ω \mathbf{w}^{\prime}\in(\mathcal{A}\setminus\{a\})^{\omega} obtained from 𝐰 \mathbf{w} by deleting all occurrences of the letter a a in 𝐰 \mathbf{w} is also balanced.

###### Lemma 5.9.

Suppose 𝐰 ∈ 𝒜 ω \mathbf{w}\in\mathcal{A}^{\omega} is a recurrent balanced WR-word, and let a ∈ 𝒜 a\in\mathcal{A} be such that g a ≤ g x g_{a}\leq g_{x} for all x ∈ 𝒜. x\in\mathcal{A}. Then the word 𝐰 ′ ∈ ( 𝒜 ∖ { a }) ω \mathbf{w}^{\prime}\in(\mathcal{A}\setminus\{a\})^{\omega} obtained from 𝐰 \mathbf{w} by deleting all occurrences of the letter a a in 𝐰 \mathbf{w} is also a recurrent balanced WR-word.

###### Proof.

Clearly 𝐰 ′ \mathbf{w}^{\prime} is a recurrent WR-word; in fact, for each letter x ≠ a, x\neq a, every complete return to x x in 𝐰 ′ \mathbf{w}^{\prime} is a complete return to x x in 𝐰 \mathbf{w} with all occurrences of a a deleted. It remains to show that 𝐰 ′ \mathbf{w}^{\prime} is balanced. Since 𝐰 \mathbf{w} is balanced, it follows that if a ​ U ​ a aUa is a complete return to a a in 𝐰, \mathbf{w}, then each x ∈ 𝒜 x\in\mathcal{A} occurs at most once in U. U. Otherwise, if some letter x x occurred more than once in U, U, we would have g x < g a. g_{x}<g_{a}. Moreover, since 𝐰 \mathbf{w} is a WR-word, U U must be a palindrome. Thus | U | ≤ 1 |U|\leq 1, and hence g a = 1. g_{a}=1. It follows that the frequency of a a in 𝐰 \mathbf{w} is at least equal to 1 / 3, 1/3, and hence from Lemma 5.8, we deduce that the word 𝐰 ′ \mathbf{w}^{\prime} obtained from 𝐰 \mathbf{w} by deleting all occurrences of a a is balanced. ∎

###### Lemma 5.10.

Let 𝐰 \mathbf{w} and 𝐰 ′ \mathbf{w}^{\prime} be as in Lemma 5.9. Suppose 𝐰 ′ \mathbf{w}^{\prime} contains the factor b ​ b bb for some b ∈ 𝒜 ∖ { a }. b\in\mathcal{A}\setminus\{a\}. Then 𝐰 \mathbf{w} is a shift of σ a ​ ( 𝐰 ′). \sigma_{a}(\mathbf{w}^{\prime}). In particular, the complete returns to b b in 𝐰 \mathbf{w} are of the form b ​ a ​ a ​ b baab or b ​ a ​ x ​ a ​ b baxab for some x ∈ 𝒜 ∖ { a, b }. x\in\mathcal{A}\setminus\{a,b\}.

###### Proof.

Assume 𝐰 ′ \mathbf{w}^{\prime} contains the word b ​ b. bb. Since 𝐰 ′ \mathbf{w}^{\prime} is balanced (see Lemma 5.9), every factor of 𝐰 ′ \mathbf{w}^{\prime} of length 2 2 must contain at least one occurrence of b, b, and hence 𝐰 ′ \mathbf{w}^{\prime} contains the factor b ​ x ​ b bxb for every x ∈ 𝒜 ∖ { a, b }. x\in\mathcal{A}\setminus\{a,b\}. Since g a = 1 g_{a}=1 (see Lemma 5.9), it follows that 𝐰 \mathbf{w} contains factors of the form b ​ a l ​ b ba^{l}b and b ​ a k ​ x ​ a k ​ b ba^{k}xa^{k}b for every x ∈ 𝒜 ∖ { a, b } x\in\mathcal{A}\setminus\{a,b\} with both l, k ≥ 1. l,k\geq 1. It is readily verified from the balance property that if b ​ a k 1 ​ x ​ a k 1 ​ b ba^{k_{1}}xa^{k_{1}}b and b ​ a k 2 ​ y ​ a k 2 ​ b ba^{k_{2}}ya^{k_{2}}b are both factors of 𝐰 \mathbf{w} with x, y ∈ 𝒜 ∖ { a, b }, x,y\in\mathcal{A}\setminus\{a,b\}, then k 1 = k 2. k_{1}=k_{2}. Again by the balance property it follows that | 2 ​ k + 1 − l | ≤ 1 |2k+1-l|\leq 1 and k ∈ { l, l + 1, l − 1 }. k\in\{l,l+1,l-1\}. If k = l, k=l, then | l + 1 | ≤ 1 |l+1|\leq 1 from which it follows that l = 0, l=0, a contradiction. If k = l + 1, k=l+1, then | l + 3 | ≤ 1, |l+3|\leq 1, again a contradiction. If k = l − 1, k=l-1, then | l − 1 | ≤ 1 |l-1|\leq 1 from which it follows that l = 2 l=2 and k = 1, k=1, for otherwise either l l or k k would equal 0. 0. Thus 𝐰 \mathbf{w} is obtained from 𝐰 ′ \mathbf{w}^{\prime} by inserting one a a between any pair of consecutive distinct letters in 𝐰 ′ \mathbf{w}^{\prime} and two a a ’s between consecutive b b ’s. In other words, 𝐰 \mathbf{w} is a shift of σ a ​ ( 𝐰 ′) \sigma_{a}(\mathbf{w}^{\prime}), as required. ∎

###### Lemma 5.11.

Suppose 𝐰 \mathbf{w} and 𝐰 ′ \mathbf{w}^{\prime} are as in Lemma 5.9 and let b ∈ 𝒜 ∖ { a }. b\in\mathcal{A}\setminus\{a\}. Then b ​ b ​ b bbb is not a factor of 𝐰 ′. \mathbf{w}^{\prime}.

###### Proof.

Suppose 𝐰 ′ \mathbf{w}^{\prime} contains b ​ b ​ b. bbb. Then by Lemma 5.10, 𝐰 \mathbf{w} contains the factors b ​ a ​ a ​ b ​ a ​ a ​ b baabaab and b ​ a ​ c ​ a ​ b bacab for some c ∈ 𝒜 ∖ { a, b }. c\in\mathcal{A}\setminus\{a,b\}. But since 𝐰 \mathbf{w} is balanced, 𝐰 \mathbf{w} cannot contain both a ​ a ​ b ​ a ​ a aabaa and b ​ a ​ c ​ a ​ b. bacab. ∎

###### Proof of Theorem 5.7.

We prove Theorem 5.7 by induction on the number of letters k. k. Suppose 𝐰 \mathbf{w} is a recurrent balanced WR-word on the alphabet 𝒜 3 = { 1, 2, 3 }. \mathcal{A}_{3}=\{1,2,3\}. Without loss of generality we can assume g 1 ≤ g 2 ≤ g 3. g_{1}\leq g_{2}\leq g_{3}. Let 𝐰 ′ ∈ { 2, 3 } ω \mathbf{w}^{\prime}\in\{2,3\}^{\omega} be the word obtained from 𝐰 \mathbf{w} by deleting all occurrences of 1 1 in 𝐰. \mathbf{w}. First suppose 22 22 does not occur in 𝐰 ′. \mathbf{w}^{\prime}. In this case 𝐰 ′ \mathbf{w}^{\prime} is a shift of the periodic word ( 23) ω = ψ 2 ​ ( 3 ω). (23)^{\omega}=\psi_{2}(3^{\omega}). So the only complete return to 2 2 in 𝐰 ′ \mathbf{w}^{\prime} is 232. 232. It follows that there exists an n ≥ 1 n\geq 1 such that the only complete return to 2 2 in 𝐰 ′ \mathbf{w}^{\prime} is 21 n ​ 31 n ​ 2. 21^{n}31^{n}2. Hence 𝐰 = ψ 1 n ∘ ψ 2 ​ ( 3 ω). \mathbf{w}=\psi_{1}^{n}\circ\psi_{2}(3^{\omega}). Next suppose 22 22 occurs in 𝐰 ′. \mathbf{w}^{\prime}. It follows from the above lemmas that the complete returns to 3 3 in 𝐰 ′ \mathbf{w}^{\prime} are of the form 323 323 and 3223. 3223. But if both factors occurred in 𝐰 ′, \mathbf{w}^{\prime}, then by Lemma 5.10, 𝐰 \mathbf{w} would contain both 31213 31213 and 31211213, 31211213, which contradicts the fact that 𝐰 \mathbf{w} is balanced. Thus 𝐰 ′ \mathbf{w}^{\prime} is a shift of the periodic word ( 223) ω = ψ 2 2 ​ ( 3 ω), (223)^{\omega}=\psi_{2}^{2}(3^{\omega}), and hence by Lemma 5.9, 𝐰 \mathbf{w} is a shift of σ 1 ∘ ψ 2 2 ​ ( 3 ω). \sigma_{1}\circ\psi_{2}^{2}(3^{\omega}). Thus, Theorem 5.7 holds for k = 3. k=3.

Next take k > 3 k>3 and suppose that 𝐰 \mathbf{w} is a recurrent balanced WR-word on the alphabet 𝒜 k = { 1, 2, …, k }. \mathcal{A}_{k}=\{1,2,\ldots,k\}. By induction the hypothesis we assume Theorem 5.7 holds for any recurrent balanced WR-word on an alphabet of size k − 1. k-1. Without loss of generality we can assume that g 1 ≤ g 2 ≤ ⋯ ≤ g k. g_{1}\leq g_{2}\leq\cdots\leq g_{k}. Let 𝐰 ′ \mathbf{w}^{\prime} be the word on the alphabet { 2, 3, …, k } \{2,3,\ldots,k\} obtained from 𝐰 \mathbf{w} by deleting all occurrences of 1 1 in 𝐰. \mathbf{w}. It follows from Lemma 5.9 that 𝐰 ′ \mathbf{w}^{\prime} is a recurrent balanced WR-word, and hence by the induction hypothesis, 𝐰 ′ \mathbf{w}^{\prime} is either a shift of ψ 2 n ∘ ψ 3 ∘ ⋯ ∘ ψ k − 1 ( k ω) \psi_{2}^{n}\circ\psi_{3}\circ\cdots\circ\psi_{k-1}(k^{\omega}) for some n ≥ 1, n\geq 1, or else a shift of σ 2 ∘ σ 3 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) \sigma_{2}\circ\sigma_{3}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega}) for some 2 ≤ j ≤ k − 2. 2\leq j\leq k-2.

First suppose that 22 22 does not occur in 𝐰 ′. \mathbf{w}^{\prime}. In this case 𝐰 ′ \mathbf{w}^{\prime} must be a shift of ψ 2 ∘ ψ 3 ∘ ⋯ ∘ ψ k − 1 ( k ω). \psi_{2}\circ\psi_{3}\circ\cdots\circ\psi_{k-1}(k^{\omega}). Thus the complete returns to 2 2 in 𝐰 ′ \mathbf{w}^{\prime} are all of the form 2 ​ x ​ 2 2x2 for some x ∈ { 3, 4, …, k }. x\in\{3,4,\ldots,k\}. Hence there exists an n ≥ 1 n\geq 1 such that each complete return to 2 2 in 𝐰 \mathbf{w} is of the form 21 n ​ x ​ 1 n ​ 2 21^{n}x1^{n}2 where x ∈ { 3, 4, …, k }. x\in\{3,4,\ldots,k\}. Thus in this case 𝐰 \mathbf{w} is a shift of ψ 1 n ∘ ψ 2 ∘ ⋯ ∘ ψ k − 1 ( k ω). \psi_{1}^{n}\circ\psi_{2}\circ\cdots\circ\psi_{k-1}(k^{\omega}).

Next suppose 𝐰 ′ \mathbf{w}^{\prime} contains the factor 22. 22. Then by Lemma 5.11, 𝐰 ′ \mathbf{w}^{\prime} is either a shift of ψ 2 2 ∘ ψ 3 ∘ ⋯ ∘ ψ k − 1 ( k ω), \psi_{2}^{2}\circ\psi_{3}\circ\cdots\circ\psi_{k-1}(k^{\omega}), or a shift of σ 2 ∘ σ 3 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) \sigma_{2}\circ\sigma_{3}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega}) for some 2 ≤ j ≤ k − 2. 2\leq j\leq k-2. It follows from Lemma 5.10 that 𝐰 \mathbf{w} is either a shift of σ 1 ∘ ψ 2 2 ∘ ψ 3 ∘ ⋯ ∘ ψ k − 1 ( k ω), \sigma_{1}\circ\psi_{2}^{2}\circ\psi_{3}\circ\cdots\circ\psi_{k-1}(k^{\omega}), or else a shift of σ 1 ∘ σ 2 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) \sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega}) for some 2 ≤ j ≤ k − 2. 2\leq j\leq k-2. Thus 𝐰 \mathbf{w} is a shift of σ 1 ∘ σ 2 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) \sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega}) for some 1 ≤ j ≤ k − 2 1\leq j\leq k-2, as required. This concludes our proof of Theorem 5.7. ∎

###### Corollary 5.12.

Suppose 𝐰 \mathbf{w} be a recurrent balanced WR-word with Alph ​ ( 𝐰) = { 1, 2, …, k } \mbox{{Alph}}(\mathbf{w})=\{1,2,\ldots,k\}, k ≥ 3. k\geq 3. Then 𝐰 \mathbf{w} is a (balanced) periodic episturmian word.

###### Proof.

Recall that any infinite word generated by an infinite composition of the morphisms ψ i \psi_{i} is episturmian. Thus ψ 1 n ∘ ψ 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) \psi_{1}^{n}\circ\psi_{2}\circ\cdots\circ\psi_{k-1}(k^{\omega}) is a periodic episturmian word. It remains to show that the words described in case 2) of Theorem 5.7 are periodic episturmian words. To do this, we use the Fraenkel words ( F i) i ≥ 1 (F_{i})_{i\geq 1} (defined previously). It is readily verified that if 𝐱 = x 1 ​ x 2 ​ x 3 ​ … \mathbf{x}=x_{1}x_{2}x_{3}\ldots is an infinite word not containing the symbols { 1, 2, …, n }, \{1,2,\ldots,n\}, then

 | σ 1 ∘ σ 2 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ( 𝐱) = F j + 1 2 x 1 F j + 1 2 x 2 F j + 1 2 x 3 … \displaystyle\sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}(\mathbf{x})=F_{j+1}^{2}x_{1}F_{j+1}^{2}x_{2}F_{j+1}^{2}x_{3}\ldots |  | (5.1) |

and

 | ψ 1 ∘ ψ 2 ∘ ⋯ ∘ ψ j + 1 ∘ ψ 1 ( 𝐱) = F j + 1 2 x 1 F j + 1 2 x 2 F j + 1 2 x 3 … \displaystyle\psi_{1}\circ\psi_{2}\circ\cdots\circ\psi_{j+1}\circ\psi_{1}(\mathbf{x})=F_{j+1}^{2}x_{1}F_{j+1}^{2}x_{2}F_{j+1}^{2}x_{3}\ldots |  |

It follows that

 | σ 1 ∘ σ 2 ∘ ⋯ ∘ σ j ∘ ψ j + 1 2 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω) = ψ 1 ∘ ψ 2 ∘ ⋯ ∘ ψ j ∘ ψ j + 1 ∘ ψ 1 ∘ ψ j + 2 ∘ ⋯ ∘ ψ k − 1 ( k ω). \sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{j}\circ\psi_{j+1}^{2}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega})=\psi_{1}\circ\psi_{2}\circ\cdots\circ\psi_{j}\circ\psi_{j+1}\circ\psi_{1}\circ\psi_{j+2}\circ\cdots\circ\psi_{k-1}(k^{\omega}). |  |

Since the right hand side above is an infinite periodic episturmian word, it follows that the periodic infinite words listed in Theorem 5.7 are episturmian words. ∎

Hence, by Proposition 5.1, WR-words obey Fraenkel’s conjecture; in fact, we can show this rather easily without the use of Proposition 5.1.

###### Corollary 5.13.

Suppose 𝐰 \mathbf{w} is a recurrent balanced WR-word with Alph ​ ( 𝐰) = { 1, 2, …, k } \mbox{{Alph}}(\mathbf{w})=\{1,2,\ldots,k\}, k ≥ 3 k\geq 3. If 𝐰 \mathbf{w} has mutually distinct letter frequencies, then up to letter permutation, 𝐰 \mathbf{w} is a shift of ( F k) ω. (F_{k})^{\omega}.

###### Proof.

By Theorem 5.7, 𝐰 \mathbf{w} is isomorphic to a shift of one of the two types of periodic words listed in the statement of the theorem. We note that except for the extreme case of j = k − 2 j=k-2 in case OPEN 2) 2) of Theorem 5.7, the frequency of the symbols k k and k − 1 k-1 are equal. Thus, under the added hypothesis that distinct letters occurring in 𝐰 \mathbf{w} have distinct frequencies, we deduce that 𝐰 \mathbf{w} is isomorphic to a shift of

 | σ 1 ∘ σ 2 ∘ ⋯ ∘ σ k − 2 ∘ ψ k − 1 2 ( k ω). \sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{k-2}\circ\psi_{k-1}^{2}(k^{\omega}). |  |

By ( 5.1), we have

 | σ 1 ∘ σ 2 ∘ ⋯ ∘ σ k − 2 ∘ ψ k − 1 2 ( k ω) = ( F k − 1 2 k) ω = F k − 1 ( F k ω) \sigma_{1}\circ\sigma_{2}\circ\cdots\circ\sigma_{k-2}\circ\psi_{k-1}^{2}(k^{\omega})=(F_{k-1}^{2}k)^{\omega}=F_{k-1}(F_{k}^{\omega}) |  |

which is clearly a shift of the Fraenkel sequence ( F k) ω. (F_{k})^{\omega}. ∎

### 5.3 Balanced almost rich words

We now extend our study to words having only a few oddities. In the spirit of Lemma 5.3, we first prove the following result (see also Theorem 6.26 to follow).

###### Proposition 5.14.

If 𝐬 = ψ a ​ ( 𝐭) \mathbf{s}=\psi_{a}(\mathbf{t}), then D ⁡ ( 𝐬) ≥ D ⁡ ( 𝐭) D(\mathbf{s})\geq D(\mathbf{t}); in particular, if 𝐬 \mathbf{s} is almost rich then 𝐭 \mathbf{t} is almost rich.

###### Example 5.15.

The periodic infinite word 𝐭 = ( a ​ b ​ c ​ b ​ a ​ c) ω \mathbf{t}=(abcbac)^{\omega} has 1 1 defect and 𝐬 = ψ a ​ ( 𝐭) = ( a 2 ​ b ​ a ​ c ​ a ​ b ​ a 2 ​ c) ω \mathbf{s}=\psi_{a}(\mathbf{t})=(a^{2}bacaba^{2}c)^{\omega} has 2 2 defects. More generally, for any k ≥ 1 k\geq 1, 𝐭 = ( a k ​ b ​ a k − 1 ​ c ​ a k − 1 ​ b ​ a k ​ c) ω \mathbf{t}=(a^{k}ba^{k-1}ca^{k-1}ba^{k}c)^{\omega} has k k defects (see [7]), so applying ψ a \psi_{a} to 𝐭 \mathbf{t} gives a periodic infinite word with k + 1 k+1 defects.

###### Proof of Proposition 5.14.

If 𝐬 \mathbf{s} is rich, then 𝐭 \mathbf{t} is rich (by Lemma 5.3), and hence D ⁡ ( 𝐬) = D ⁡ ( 𝐭) = 0 D(\mathbf{s})=D(\mathbf{t})=0. So now suppose that 𝐭 \mathbf{t} has at least one defect. Consider any prefix 𝐭 m \mathbf{t}_{m} of 𝐭 \mathbf{t} corresponding to a defect, i.e., 𝐭 m \mathbf{t}_{m} does not have a ups. Let 𝐭 m = 𝐭 m − 1 ​ x \mathbf{t}_{m}=\mathbf{t}_{m-1}x where x x is a letter. We show that if x ≠ a x\neq a (resp. x = a x=a), then ψ a ​ ( 𝐭 m) \psi_{a}(\mathbf{t}_{m}) (resp. ψ a ​ ( 𝐭 m) ​ a \psi_{a}(\mathbf{t}_{m})a) has no ups and thus gives a defect in 𝐬 \mathbf{s}. Let q q be the longest palindromic suffix of 𝐭 m \mathbf{t}_{m} which is not unioccurrent in 𝐭 m \mathbf{t}_{m} since 𝐭 m \mathbf{t}_{m} has no ups.

Case x ≠ a x\neq a: p = a − 1 ​ ψ a ​ ( q) p=a^{-1}\psi_{a}(q) is the longest palindromic suffix of ψ a ​ ( 𝐭 m) \psi_{a}(\mathbf{t}_{m}), which is not unioccurrent in it, otherwise q q has another occurrence in 𝐭 m \mathbf{t}_{m}, a contradiction.

Case x = a x=a: Similar to the above case, but with ψ a ​ ( 𝐭 m) ​ a \psi_{a}(\mathbf{t}_{m})a and its longest palindromic suffix given by p = ψ a ​ ( q) ​ a p=\psi_{a}(q)a. ∎

###### Note.

Proposition 5.14 can be extended without difficulty to oddities; that is, if 𝐬 = ψ a ​ ( 𝐭) \mathbf{s}=\psi_{a}(\mathbf{t}), then O ⁡ ( 𝐬) ≥ O ⁡ ( 𝐭) O(\mathbf{s})\geq O(\mathbf{t}).

The main result of this section is the following:

###### Theorem 5.16.

Suppose 𝐬 \mathbf{s} is a recurrent balanced infinite word with alphabet 𝒜 \mathcal{A}, | 𝒜 | > 2 |\mathcal{A}|>2, and less than | 𝒜 | |\mathcal{A}| oddities. Then 𝐬 \mathbf{s} is either episturmian or two of its letters have the same frequency.

###### Proof.

The proof relies on two lemmas, which are stated and proved below. As in the proof of Theorem 5.2, we decompose 𝐬 \mathbf{s} as much as possible using morphisms ψ x \psi_{x}, x ∈ 𝒜 x\in\mathcal{A}. If we can continue infinitely, then 𝐬 \mathbf{s} is episturmian. Otherwise we halt at some skeleton 𝐭 \mathbf{t} without a separating letter and with alphabet ℬ \mathcal{B}. If | ℬ | < 3 |\mathcal{B}|<3, 𝐭 \mathbf{t} is Sturmian and hence has a separating letter, a contradiction. If | ℬ | > 2 |\mathcal{B}|>2 then by Lemma 5.17 O ⁡ ( 𝐭) < | ℬ | O(\mathbf{t})<|\mathcal{B}|. Moreover, by Lemma 5.18, as 𝐭 \mathbf{t} has no separating letter, it takes the following form (up to a shift): 𝐭 = ( x ​ ( a ​ b) n ​ a ​ x ​ ( b ​ a) n ​ b) ω \mathbf{t}=(x(ab)^{n}ax(ba)^{n}b)^{\omega}, for some n ≥ 1 n\geq 1.

If the decomposition from 𝐬 \mathbf{s} to 𝐭 \mathbf{t} uses neither ψ a \psi_{a} nor ψ b \psi_{b}, then a a and b b have same frequencies in 𝐬 \mathbf{s} (as in 𝐭 \mathbf{t}), as claimed. Otherwise we have for instance 𝐬 = μ 1 ​ ψ a ​ μ 2 ​ ( 𝐭) \mathbf{s}=\mu_{1}\psi_{a}\mu_{2}(\mathbf{t}) with ψ a \psi_{a}, ψ b \psi_{b} not occurring in μ 2 \mu_{2}. Then considering factors x ​ a ​ b xab and b ​ a ​ b bab of 𝐭 \mathbf{t} we have μ 2 ​ ( x ​ a ​ b) = f ​ x ​ g ​ a ​ g ​ b \mu_{2}(xab)=fxgagb and μ 2 ​ ( b ​ a ​ b) = g ​ b ​ g ​ a ​ g ​ b \mu_{2}(bab)=gbgagb for some { a, b } \left\{a,b\right\} -free words f f, g g; whence ψ a ​ ( x ​ g ​ a ​ g ​ b) = a ​ x ​ h ​ a ​ h ​ a ​ b \psi_{a}(xgagb)=axhahab and ψ a ​ ( b ​ g ​ a ​ g ​ b) = a ​ b ​ h ​ a ​ h ​ a ​ b \psi_{a}(bgagb)=abhahab where h = ψ a ​ ( g) h=\psi_{a}(g), showing the unbalance a ​ x ​ h ​ a ​ h ​ a, b ​ h ​ a ​ h ​ a ​ b axhaha,bhahab. Thus 𝐬 \mathbf{s} in not balanced, a contradiction. ∎

###### Lemma 5.17.

Let 𝐦 = ψ c ​ ( 𝐫) \mathbf{m}=\psi_{c}(\mathbf{r}) and suppose 𝐦 \mathbf{m} is balanced with alphabet 𝒜 \mathcal{A}, | 𝒜 | > 2 |\mathcal{A}|>2, and less than | 𝒜 | |\mathcal{A}| oddities. Then, if 𝐫 \mathbf{r} has alphabet ℬ = 𝒜 ∖ { c } \mathcal{B}=\mathcal{A}\setminus\left\{c\right\}, 𝐫 \mathbf{r} is a (balanced) skeleton with less than | ℬ | |\mathcal{B}| oddities.

###### Proof.

If w = x 1 x 2 ⋯ x n w=x_{1}x_{2}\cdots x_{n} is an oddity in 𝐫 \mathbf{r} then x 1 c x 2 ⋯ c x n x_{1}cx_{2}\cdots cx_{n} and c x 1 ⋯ c x n c cx_{1}\cdots cx_{n}c are oddities in 𝐦 \mathbf{m}, thus 2 ​ O ​ ( 𝐫) = O ⁡ ( 𝐦) < | 𝒜 | 2O(\mathbf{r})=O(\mathbf{m})<|\mathcal{A}|, which implies O ⁡ ( 𝐫) < | ℬ | O(\mathbf{r})<|\mathcal{B}| if | 𝒜 | ≥ 3 |\mathcal{A}|\geq 3. It is also clear that if 𝐫 \mathbf{r} is not a skeleton, then it contains some a ​ a aa, whence a ​ c ​ a ∈ F ⁡ ( 𝐦) aca\in F(\mathbf{m}). As | 𝒜 | > 2 |\mathcal{A}|>2, there is another letter b b in Alph ​ ( 𝐦) \textrm{Alph}(\mathbf{m}), and hence c ​ b ​ c ∈ F ⁡ ( 𝐦) cbc\in F(\mathbf{m}). Thus 𝐦 \mathbf{m} is not balanced, a contradiction. ∎

###### Lemma 5.18.

Let 𝐭 \mathbf{t} be a recurrent balanced skeleton with alphabet ℬ \mathcal{B}, | ℬ | > 2 |\mathcal{B}|>2, and less than | ℬ | |\mathcal{B}| oddities and without any separating letter. Then, up to a shift, 𝐭 \mathbf{t} takes the form ( x ​ ( a ​ b) n ​ a ​ x ​ ( b ​ a) n ​ b) ω (x(ab)^{n}ax(ba)^{n}b)^{\omega} for some n ≥ 1 n\geq 1.

###### Proof.

As O ⁡ ( 𝐭) < | ℬ | O(\mathbf{t})<|\mathcal{B}| there is some letter, x x say, such that all of the complete returns to x x are palindromes (of the same odd length); call them x ​ v ​ x xvx, x ​ v ′ ​ x xv^{\prime}x, x ​ v ′′ ​ x xv^{\prime\prime}x, … \ldots and write v = u ​ z ​ u ~ v=uz\tilde{u}, v ′ = u ′ ​ z ′ ​ u ~ ′ v^{\prime}=u^{\prime}z^{\prime}\tilde{u}^{\prime} and so on. We have | u | > 0 |u|>0 (otherwise x x is separating in 𝐭 \mathbf{t}). Consider a factor x ​ v ​ x ​ v ′ ​ x xvxv^{\prime}x. Suppose firstly that u = u ′ u=u^{\prime}. If u u is not a palindrome, let u = e a ⋯ b e ~ u=ea\cdots b\tilde{e}, a ≠ b a\neq b. Then we have factors b ​ e ~ ​ z ​ e ​ b b\tilde{e}zeb and a ​ e ~ ​ x ​ e ​ a a\tilde{e}xea, contradicting the balance property. Thus u u is an (odd) palindrome, say u = w ​ y ​ w ~ u=wy\tilde{w}. By the same argument, w w is a palindrome and so on. Thus u u has the form w n w_{n} for some n n, with w i + 1 = w i ​ y i ​ w i w_{i+1}=w_{i}y_{i}w_{i} and w 1 w_{1}, y i ∈ ℬ y_{i}\in\mathcal{B}.

If all u u, u ′ u^{\prime}, … \ldots are equal, then the letter w 1 w_{1} is separating in 𝐭 \mathbf{t}, a contradiction. Thus we have for instance u ≠ u ′ u\neq u^{\prime}. Then u = ⋯ a e u=\cdots ae, u ′ = ⋯ b e u^{\prime}=\cdots be with e ∈ F ⁡ ( 𝐭) e\in F(\mathbf{t}) and a a, b ∈ ℬ b\in\mathcal{B}. The factors a ​ e ​ z ​ e ~ ​ a aez\tilde{e}a and b ​ e ​ z ′ ​ e ~ ​ b bez^{\prime}\tilde{e}b give z = b z=b, z ′ = a z^{\prime}=a. Clearly, a a and b b do not occur in e e, otherwise we have for instance a ​ f ​ b ​ f ~ ​ a afb\tilde{f}a and a ​ f ​ a ​ f ~ ​ a afa\tilde{f}a being factors of 𝐭 \mathbf{t} with f f a a -free. So, by the gap property for a a, | f | ≥ 2 ​ | f | |f|\geq 2|f|; whence f = ε f=\varepsilon. But then a ​ a aa is a factor of 𝐭 \mathbf{t}, a contradiction. Now observe that u u, u ′ u^{\prime} have the following property.

Let u ⁡ ( i) u(i), u ′ ​ ( i) u^{\prime}(i) be the i i -th letter of u u, u ′ u^{\prime}, respectively. If u ⁡ ( i) ∉ { a, b } u(i)\not\in\{a,b\}, then u ′ ​ ( i) = u ​ ( i) u^{\prime}(i)=u(i). On the other hand, if u ⁡ ( i) ∈ { a, b } u(i)\in\left\{a,b\right\}, then u ′ ​ ( i) ∈ { a, b } u^{\prime}(i)\in\left\{a,b\right\}. The proof is easy using u ​ b ​ u ~ ub\tilde{u} and u ′ ​ a ​ u ~ ′ u^{\prime}a\tilde{u}^{\prime}. Thus we can write

 | u = f 0 c 0 f 1 c 1 ⋯ f n c n e, u ′ = f 0 c 0 ′ f 1 c 1 ′ ⋯ f n c n ′ e, f i ∈ ℬ ∖ { a, b }, c i, c i ′ ∈ { a, b }. u=f_{0}c_{0}f_{1}c_{1}\cdots f_{n}c_{n}e,\ u^{\prime}=f_{0}c^{\prime}_{0}f_{1}c^{\prime}_{1}\cdots f_{n}c^{\prime}_{n}e,\ f_{i}\in\mathcal{B}\setminus\left\{a,b\right\},\ c_{i},c^{\prime}_{i}\in\left\{a,b\right\}. |  |

We easily see that f 0 = e ~ f_{0}=\tilde{e} and f i = f ~ n + 1 − i f_{i}=\tilde{f}_{n+1-i}, using u ~ ​ x ​ u ′ \tilde{u}xu^{\prime} and u ​ b ​ u ~ ub\tilde{u}. Now consider c 0 ​ e ~ ​ x ​ e ​ c 0 ′ c_{0}\tilde{e}xec^{\prime}_{0} in u ~ ​ x ​ u ′ \tilde{u}xu^{\prime}. If c 0 = c 0 ′ = a c_{0}=c^{\prime}_{0}=a for instance, then as b b does not occur in it, b b has a gap greater than 2 ​ | e | + 2 2|e|+2, a contradiction. Thus c 0 = a c_{0}=a, c 0 ′ = b c^{\prime}_{0}=b for instance. But now for the same reason we have the factor b ​ a ​ e ~ ​ x ​ e ​ b ​ a ba\tilde{e}xeba, i.e., f 1 = f n = ε f_{1}=f_{n}=\varepsilon. It follows that a a and b b have the same gaps: 2 ​ | e | + 1 2|e|+1, 2 ​ | e | + 2 2|e|+2; moreover a a and b b alternate in u u, u ′ u^{\prime}. Thus

 | u = e ~ a b f 2 a ⋯ b a e, u ′ = e ~ b a f 2 b ⋯ a b e u=\tilde{e}abf_{2}a\cdots bae,\ u^{\prime}=\tilde{e}baf_{2}b\cdots abe |  | (5.2) |

or

 | u = e ~ b a f 2 a ⋯ b a e, u ′ = e ~ a b f 2 a ⋯ a b e. u=\tilde{e}baf_{2}a\cdots bae,\ u^{\prime}=\tilde{e}abf_{2}a\cdots abe. |  | (5.3) |

Consider the first case (the second one is similar). The factor b ​ a ​ e ​ b ​ e ~ ​ a ​ b baeb\tilde{e}ab in u ​ b ​ u ~ ub\tilde{u} shows that | a ​ e | |ae| is a gap for b b, and hence | e | + 1 ≥ 2 ​ | e | + 1 |e|+1\geq 2|e|+1. Thus e = ε e=\varepsilon and we have

 | u = a b f 2 a ⋯ b a, u ′ = b a f 2 b ⋯ a b. u=abf_{2}a\cdots ba,\ u^{\prime}=baf_{2}b\cdots ab. |  | (5.4) |

Now 1 + | f i | 1+|f_{i}| is a gap for a a with 1 + | f i | ≤ 2 1+|f_{i}|\leq 2; thus f i ∈ ℬ f_{i}\in\mathcal{B} or f i = ε f_{i}=\varepsilon. Moreover, considering f i ​ a ​ f i + 1 f_{i}af_{i+1} for instance, we have | f i | + 1 + | f i + 1 | ≤ 2 |f_{i}|+1+|f_{i+1}|\leq 2; thus if f i f_{i} is a letter, then f i − 1 f_{i-1} and f i + 1 f_{i+1} are empty.

Now consider x ​ v ​ x ​ v ′ ​ x ​ v ′′ ​ x xvxv^{\prime}xv^{\prime\prime}x. If u ′ = u ′′ u^{\prime}=u^{\prime\prime} then factors b ​ x ​ b bxb and a ​ b ​ a aba contradict the balance property. Thus u ′ ≠ u ′′ u^{\prime}\neq u^{\prime\prime} and easily u ′′ = u u^{\prime\prime}=u, z ′′ = z = b z^{\prime\prime}=z=b; whence, up to a shift, 𝐭 = ( x ​ u ​ b ​ u ~ ​ x ​ u ′ ​ a ​ u ~ ′) ω \mathbf{t}=(xub\tilde{u}xu^{\prime}a\tilde{u}^{\prime})^{\omega}.

Any letter y = f i ∈ ℬ ∖ { x, a, b } y=f_{i}\in\mathcal{B}\setminus\left\{x,a,b\right\} gives rise to two oddities, namely a ​ f i ​ b ​ a af_{i}ba and b ​ f i ​ a ​ b bf_{i}ab, and the left-most occurrence of y y in u u gives an oddity: y a ⋯ x ⋯ b y ya\cdots x\cdots by for instance. Also a ​ b ​ x ​ a abxa and b ​ a ​ x ​ b baxb are oddities. Therefore O ⁡ ( 𝐭) ≥ 3 ​ ( | ℬ | − 3) + 2 = 3 ​ | ℬ | − 7 O(\mathbf{t})\geq 3(|\mathcal{B}|-3)+2=3|\mathcal{B}|-7 and, as O ⁡ ( 𝐭) < | ℬ | O(\mathbf{t})<|\mathcal{B}|, this gives | ℬ | ≤ 3 |\mathcal{B}|\leq 3. Thus all f i f_{i} are empty and, for some k ≥ 0 k\geq 0, u = ( a ​ b) k ​ a u=(ab)^{k}a and v = ( a ​ b) 2 ​ k + 1 ​ a v=(ab)^{2k+1}a. Similarly, the form of equation ( 5.3) gives v = ( a ​ b) 2 ​ k ​ a v=(ab)^{2k}a, k ≥ 1 k\geq 1. Hence, up to a shift, 𝐭 = ( x ​ ( a ​ b) n ​ a ​ x ​ ( b ​ a) n ​ b) ω \mathbf{t}=(x(ab)^{n}ax(ba)^{n}b)^{\omega} for some n > 0 n>0 and letter x x. ∎

Thus we get another class of infinite words, wider than “rich”, that obey Fraenkel’s conjecture.

## 6 Action of morphisms

In this section, we study the action of morphisms on (almost) rich words, with particular interest in morphisms that “preserve” (almost) richness. We say that a morphism φ \varphi on 𝒜 \mathcal{A} preserves (resp. strictly preserves) a property P P of (finite or infinite) words if w ∈ 𝒜 ∞ w\in\mathcal{A}^{\infty} has property P ⇒ φ ⁡ ( w) P\Rightarrow\varphi(w) has property P P (resp. w ∈ 𝒜 ∞ w\in\mathcal{A}^{\infty} has property P ⇔ φ ⁡ ( w) P\Leftrightarrow\varphi(w) has property P P).

###### Note.

For “richness”, finite or infinite words give the same definition for “preserves” (but not for “strictly preserves”). For “almost richness” the definition has meaning only for infinite words.

### 6.1 Various results

Part OPEN i) i) of Lemma 5.3 works in the opposite sense; thus we have:

###### Proposition 6.1.

Let 𝐬 = ψ a ​ ( 𝐭) \mathbf{s}=\psi_{a}(\mathbf{t}). Then 𝐬 \mathbf{s} is rich if and only if 𝐭 \mathbf{t} is rich.

###### Proof.

It suffices to show the “if” part. If 𝐬 \mathbf{s} is not rich, then let w ​ x wx be the shortest prefix of 𝐭 \mathbf{t} such that ψ a ​ ( w ​ x) \psi_{a}(wx) is not rich. We show first that ψ a ​ ( w) ​ a \psi_{a}(w)a is rich. Let p p be the ups of w w. Then ψ a ​ ( w) ​ a \psi_{a}(w)a ends with the palindrome ψ a ​ ( p) ​ a \psi_{a}(p)a. If this one has another occurrence in ψ a ​ ( w) ​ a \psi_{a}(w)a then ψ a ​ ( w) ​ a = g ​ ψ a ​ ( p) ​ a ​ h ​ a \psi_{a}(w)a=g\psi_{a}(p)aha, h ∈ 𝒜 ∗ h\in\mathcal{A}^{*} whence w = g ′ ​ p ​ h ′ w=g^{\prime}ph^{\prime}, g = ψ a ​ ( g ′) g=\psi_{a}(g^{\prime}), a ​ h = ψ a ​ ( h ′) ah=\psi_{a}(h^{\prime}), thus h ′ ≠ ε h^{\prime}\neq\varepsilon and p p is not unioccurrent in w w, a contradiction.

Now if x = a x=a the proof is over, otherwise it remains to show that ψ a ​ ( w ​ x) = ψ a ​ ( w) ​ a ​ x \psi_{a}(wx)=\psi_{a}(w)ax has a ups. Suppose q q is the ups of w ​ x wx (which exists since w ​ x wx is rich). Then q q begins and ends with x ≠ a x\neq a, and hence a − 1 ​ ψ a ​ ( q) a^{-1}\psi_{a}(q) is a palindromic suffix of ψ a ​ ( w ​ x) \psi_{a}(wx). As previously, we easily see that it is unioccurrent in ψ a ​ ( w ​ x) \psi_{a}(wx). ∎

###### Remark 6.2.

The “if and only if” part of Proposition 6.1 does not extend to finite words. For instance, with v = a ​ b ​ c ​ a v=abca, ψ a ​ ( v) = a ​ a ​ b ​ a ​ c ​ a \psi_{a}(v)=aabaca is rich while v v is not rich.

###### Corollary 6.3.

Episturmian morphisms strictly preserve richness of infinite words.

###### Proof.

Proposition 6.1 and Lemma 5.5 show that any elementary epistandard morphism ψ a \psi_{a}, as well as its conjugate ψ ¯ a: a ↦ a, x ↦ x ​ a \bar{\psi}_{a}:a\mapsto a,x\mapsto xa, strictly preserve richness of infinite words. Consequently, episturmian morphisms [13, 21] strictly preserve richness of infinite words as the monoid of all such morphisms is generated by all the ψ a \psi_{a}, ψ ¯ a \bar{\psi}_{a}, and permutations of the alphabet. ∎

###### Proposition 6.4.

For a fixed letter a ∈ 𝒜 a\in\mathcal{A}, the ‘insertion’ morphism φ a \varphi_{a}, defined by φ a: x ↦ x ​ a \varphi_{a}:x\mapsto xa for all x ∈ 𝒜 x\in\mathcal{A}, preserves richness.

###### Proof.

Let p p be the ups of a rich word u u. If p ≠ u p\neq u then a ​ φ a ​ ( p) a\varphi_{a}(p) is clearly a ups of φ a ​ ( u) \varphi_{a}(u), but we also have to show that φ a ​ ( u) ​ a − 1 \varphi_{a}(u)a^{-1} has a ups: this one is φ a ​ ( p) ​ a − 1 \varphi_{a}(p)a^{-1}. Now if p = u p=u then φ a ​ ( u) ​ a − 1 \varphi_{a}(u)a^{-1} is its own ups. Also let u = y ​ t u=yt with y ∈ 𝒜 y\in\mathcal{A} and let q q be the ups of y y. If t t is a palindrome, then u = a n u=a^{n} for some n n, a trivial case. Otherwise, let q q be the ups of t t. Then r = a ​ φ a ​ ( q) r=a\varphi_{a}(q) is the ups of a ​ φ a ​ ( t) a\varphi_{a}(t) and it cannot be a prefix of φ a ​ ( u) \varphi_{a}(u) because otherwise, as q q is a prefix of u u, we get q = a n q=a^{n} for some n n; whence easily we have a contradiction. ∎

The next proposition deals with a transformation which is not a morphism in general. Let w w be a finite or infinite word. For any letter a ∈ Alph ​ ( w) a\in\textrm{Alph}(w), if a k ​ x a^{k}x is a prefix of w w (or x ​ a k xa^{k} is a suffix) or y ​ a k ​ x ya^{k}x occurs in w w with x, y ≠ a x,y\neq a, we say that k k is an exponent of a a in w w. Let k 1 < k 2 < ⋯ k_{1}<k_{2}<\cdots be the sequence of the exponents of a a in w w and let h 1 < h 2 < ⋯ h_{1}<h_{2}<\cdots be another sequence of positive integers of the same length with h i ≤ k i h_{i}\leq k_{i} for all i i. Let π a ​ ( w) \pi_{a}(w) be the word obtained by replacing every exponent k i k_{i} by h i h_{i} in w w. Then:

###### Proposition 6.5.

π a ​ ( w) \pi_{a}(w) is rich if and only if w w is rich.

###### Proof.

Suppose w w is rich. Then by Theorem 2.14 the complete returns to any palindromic factor of w w are also palindromes. The same is true for π a ​ ( w) \pi_{a}(w) since π a \pi_{a} strictly preserves palindromes (i.e., a finite word u u is a palindrome if and only if π a ​ ( u) \pi_{a}(u) is a palindrome). Hence π a ​ ( w) \pi_{a}(w) is rich (again by Theorem 2.14). The converse is proved similarly. ∎

###### Proposition 6.6.

If φ \varphi preserves richness and is prolongable on a ∈ 𝒜 a\in\mathcal{A}, then φ ω ​ ( a) \varphi^{\omega}(a) is a rich infinite word.

###### Proof.

This is a trivial consequence of the fact that, for all n ≥ 1 n\geq 1, φ n ​ ( a) \varphi^{n}(a) is a rich word, since φ ⁡ ( a) \varphi(a) is a rich word and φ \varphi preserves richness. ∎

###### Note.

The converse does not hold. For example, the morphism δ: a ↦ a ​ b ​ a \delta:a\mapsto aba, b ↦ b ​ c ​ b b\mapsto bcb, c ↦ c ​ b ​ c c\mapsto cbc generates rich infinite words, beginning with a a, b b, and c c as easily seen; however, δ \delta does not preserve richness (e.g., δ ⁡ ( a ​ c ​ b) = a ​ b ​ a ​ c ​ b ​ c ​ b ​ c ​ b \delta(acb)=abacbcbcb has a defect at the second occurrence of the letter b b).

Clearly, a morphism φ \varphi on 𝒜 \mathcal{A} preserves palindromes if and only if φ ⁡ ( x) \varphi(x) is a palindrome for all x ∈ 𝒜 x\in\mathcal{A}.

###### Proposition 6.7.

Suppose φ \varphi is a morphism on 𝒜 \mathcal{A}, with | 𝒜 | > 1 |\mathcal{A}|>1. If φ \varphi strictly preserves palindromes, then φ \varphi is injective.

###### Proof.

Suppose φ \varphi strictly preserves palindromes and assume φ ⁡ ( u) = φ ⁡ ( v) \varphi(u)=\varphi(v) for some non-empty words u u, v ∈ 𝒜 ∗ v\in\mathcal{A}^{*}. Then, with p = u ​ u ~ p=u\tilde{u} and q = v ​ v ~ q=v\tilde{v}, φ ⁡ ( p) = φ ⁡ ( q) \varphi(p)=\varphi(q) is a palindrome. Indeed, both φ ⁡ ( p) \varphi(p) and φ ⁡ ( q) \varphi(q) are palindromes since φ \varphi preserves palindromes, and moreover

 | φ ⁡ ( p) = φ ⁡ ( u) ​ φ ​ ( u ~) = φ ⁡ ( v) ​ φ ⁡ ( u) ~ = φ ⁡ ( v) ​ φ ⁡ ( v) ~ = φ ⁡ ( v) ​ φ ​ ( v ~) = φ ⁡ ( q). \varphi(p)=\varphi(u)\varphi(\tilde{u})=\varphi(v)\widetilde{\varphi(u)}=\varphi(v)\widetilde{\varphi(v)}=\varphi(v)\varphi(\tilde{v})=\varphi(q). |  |

Whence φ ⁡ ( p ​ q) = φ ​ ( p) 2 \varphi(pq)=\varphi(p)^{2} is a palindrome and p ​ q pq too (since φ \varphi strictly preserves palindromes). Therefore p ​ q = q ​ p pq=qp, and hence p p and q q are powers of a common word (e.g., see Lothaire [23]), i.e., p = w m p=w^{m} and q = w n q=w^{n}. Therefore, since φ ⁡ ( p) = φ ⁡ ( q) \varphi(p)=\varphi(q), we must have m = n m=n; whence u = v u=v. Thus φ \varphi is injective. ∎

###### Example 6.8.

The non-injective morphism φ: a ↦ a ​ b ​ a \varphi:a\mapsto aba, b ↦ b ​ c ​ b b\mapsto bcb, c ↦ a ​ b ​ a c\mapsto aba preserves palindromes, but not strictly as φ ⁡ ( a ​ b ​ c) = a ​ b ​ a ​ b ​ c ​ b ​ a ​ b ​ a \varphi(abc)=ababcbaba is a palindrome whereas the preimage a ​ b ​ c abc is not.

The letter-doubling morphism φ d \varphi_{d} defined by φ d: x ↦ x ​ x \varphi_{d}:x\mapsto xx for all x ∈ 𝒜 x\in\mathcal{A} strictly preserves palindromes; it also preserves almost richness. More precisely, we easily have:

###### Proposition 6.9.

If 𝐭 \mathbf{t} has finite defect k k, then φ d ​ ( 𝐭) \varphi_{d}(\mathbf{t}) has defect 2 ​ k 2k. More precisely, if p 1 p_{1}, …, p k p_{k} are the k k defective positions in 𝐭 \mathbf{t}, then the defective positions in φ d ​ ( 𝐭) \varphi_{d}(\mathbf{t}) are 2 ​ p i − 1 2p_{i}-1, 2 ​ p i 2p_{i} for 1 ≤ i ≤ k 1\leq i\leq k. ∎

###### Example 6.10.

The periodic infinite word 𝐭 = ( a 2 ​ b ​ a ​ c ​ a ​ b ​ a 2 ​ c) ω \mathbf{t}=(a^{2}bacaba^{2}c)^{\omega} has only 2 defects at positions 10 10 and 11 11, and φ ⁡ ( 𝐭) = ( a 4 ​ b 2 ​ a 2 ​ c 2 ​ a 2 ​ b 2 ​ a 4 ​ c 2) ω \varphi(\mathbf{t})=(a^{4}b^{2}a^{2}c^{2}a^{2}b^{2}a^{4}c^{2})^{\omega} has 4 4 defects at positions 19, 20, 21, 22 19,20,21,22.

A simple example of a morphism that does not preserve almost richness is φ: a ↦ a ​ c, b ↦ b, c ↦ c \varphi:a\mapsto ac,b\mapsto b,c\mapsto c. For instance, consider the (rich) Fibonacci word 𝐟 \mathbf{f}, which is generated by the morphism: a ↦ a ​ b, b ↦ a a\mapsto ab,b\mapsto a. We easily see that the image of 𝐟 \mathbf{f} by φ \varphi has only six unique palindromic factors ( ε, a, b, c, a ​ c ​ a, c ​ a ​ c \varepsilon,a,b,c,aca,cac), and hence φ ⁡ ( 𝐟) \varphi(\mathbf{f}) has infinite defect.

### 6.2 Class P P morphisms

We now slightly extend the definition of “class P P ” morphisms introduced by Hof, Knill, and Simon [19] (see also [1]).

###### Definition 6.11 (Class P P morphisms).

- i)

A morphism φ \varphi on 𝒜 \mathcal{A} is said to be a standard morphism of class P P (or a standard P P -morphism) if there exists a palindrome p p (possibly empty) such that, for all x ∈ 𝒜 x\in\mathcal{A}, φ ⁡ ( x) = p ​ q x \varphi(x)=pq_{x} where the q x q_{x} are palindromes. If p p is non-empty, then some (or all) of the palindromes q x q_{x} may be empty or may even take the form q x = π x − 1 q_{x}=\pi_{x}^{-1} with π x \pi_{x} a proper palindromic suffix of p p.

- ii)

A morphism ψ \psi on 𝒜 \mathcal{A} is said to be a morphism of class P P (or a P P -morphism) if there exists a standard P P -morphism φ \varphi, with φ ⁡ ( x) = p ​ q x \varphi(x)=pq_{x} for all x ∈ 𝒜 x\in\mathcal{A}, such that, for some factorization p = p ′ ​ p ′′ p=p^{\prime}p^{\prime\prime}, we have ψ ⁡ ( x) = p ′′ ​ q x ​ p ′ \psi(x)=p^{\prime\prime}q_{x}p^{\prime} for all x ∈ 𝒜 x\in\mathcal{A}. That is, ψ = T i ​ ( φ) \psi=\mathrm{T}^{i}(\varphi) for some 0 ≤ i ≤ | p | 0\leq i\leq|p|.

###### Remark 6.12.

Part OPEN i ​ i) ii) of Definition 6.11 tells us that any P P -morphism is a conjugate of a standard one. Let us also observe that any P P -morphism as defined in part OPEN i ​ i) ii) may also be a standard P P -morphism, or a “dual” of a standard P P -morphism (of the form x ↦ q x ​ p x\mapsto q_{x}p) for other p p and q x q_{x}, because for instance if | p ′ | ≤ | p ′′ | |p^{\prime}|\leq|p^{\prime\prime}|, then p ′′ ​ q x ​ p ′ = ( p ′′ ​ p ~ ′ − 1) ​ ( p ~ ′ ​ q x ​ p ′) p^{\prime\prime}q_{x}p^{\prime}=(p^{\prime\prime}\tilde{p}^{\prime-1})(\tilde{p}^{\prime}q_{x}p^{\prime}) which has form r ​ m x rm_{x}, where r r, m x m_{x} are palindromes. Indeed, the interest of part OPEN i ​ i) ii) is mainly in view of Definition 6.15 hereafter.

###### Note.

The class of P P -morphisms (resp. standard P P -morphisms) is closed under composition, i.e., it is a monoid of morphisms.

For our purposes, it suffices to consider standard P P -morphisms in view of the following trivial property.

###### Proposition 6.13.

Suppose φ \varphi is a standard P P -morphism with φ ⁡ ( x) = p ​ q x \varphi(x)=pq_{x} for all x ∈ 𝒜 x\in\mathcal{A} and let ψ = T i ​ ( φ) \psi=\mathrm{T}^{i}(\varphi) for some i i, 0 ≤ i ≤ | p | 0\leq i\leq|p|. Then, for any recurrent infinite word 𝐭 \mathbf{t}, ψ ⁡ ( 𝐭) \psi(\mathbf{t}) and φ ⁡ ( 𝐭) \varphi(\mathbf{t}) have the same set of factors. ∎

###### Example 6.14.

The morphism τ: a ↦ b ​ a ​ a \tau:a\mapsto baa, b ↦ b ​ a ​ b ​ a b\mapsto baba is standard P P (and its first conjugate T ⁡ ( τ): a ↦ a ​ a ​ b \mathrm{T}(\tau):a\mapsto aab, b ↦ a ​ b ​ a ​ b b\mapsto abab is of class P P). It generates a rich infinite word as does T ⁡ ( τ) \mathrm{T}(\tau). This follows easily from the fact that τ = φ 1 ∘ φ 2 \tau=\varphi_{1}\circ\varphi_{2} with φ 1: a ↦ a, b ↦ b ​ a \varphi_{1}:a\mapsto a,b\mapsto ba and φ 2: a ↦ b ​ a, b ↦ b ​ b \varphi_{2}:a\mapsto ba,b\mapsto bb, where the latter two morphisms preserve richness: the first one is episturmian and the second one is an insertion morphism (see Corollary 6.3 and Proposition 6.4).

###### Definition 6.15.

We say that a standard P P -morphism σ \sigma is special if: 1) all σ ⁡ ( x) = p ​ q x \sigma(x)=pq_{x} end with different letters, and 2) whenever σ ⁡ ( x) ​ p = p ​ q x ​ p \sigma(x)p=pq_{x}p, with x ∈ 𝒜 x\in\mathcal{A}, occurs in some σ ( y 1 y 2 ⋯ y n) p \sigma(y_{1}y_{2}\cdots y_{n})p, then this occurrence is σ ⁡ ( y m) ​ p \sigma(y_{m})p for some m m with 1 ≤ m ≤ n 1\leq m\leq n. A P P -morphism is special if the corresponding standard P P -morphism is special.

###### Remark 6.16.

When p = ε p=\varepsilon, 2) means that the code σ ⁡ ( 𝒜) \sigma(\mathcal{A}) is comma-free (see [6]). Observe also that the elementary epistandard morphisms { ψ x ∣ x ∈ 𝒜 } \{\psi_{x}\mid x\in\mathcal{A}\} satisfy this definition. Moreover, as the monoid of epistandard morphisms is generated by all the ψ x \psi_{x} and permutations on 𝒜 \mathcal{A} (see [13, 21]), any such morphism is a special P P -morphism. For example, ψ a ∘ ψ b \psi_{a}\circ\psi_{b} is the special (standard) P P -morphism with p = a ​ b ​ a p=aba, q a = ε q_{a}=\varepsilon, q b = a − 1 q_{b}=a^{-1}.

###### Theorem 6.17.

Suppose σ \sigma is a special standard P P -morphism and let 𝐭 = x 1 x 2 x 3 ⋯ \mathbf{t}=x_{1}x_{2}x_{3}\cdots be a rich infinite word. Let h h be minimal such that all palindromic factors of 𝐭 \mathbf{t} of length at most 2 2 occur in the prefix 𝐭 h \mathbf{t}_{h}. Then σ ⁡ ( 𝐭) \sigma(\mathbf{t}) is rich if (and only if) σ ⁡ ( 𝐭 h) ​ p \sigma(\mathbf{t}_{h})p is rich.

###### Proof.

By induction, we suppose σ ⁡ ( 𝐭 n − 1) ​ p \sigma(\mathbf{t}_{n-1})p is rich for some n > h n>h and show that σ ⁡ ( 𝐭 n) ​ p = σ ⁡ ( 𝐭 n − 1) ​ p ​ q x n ​ p \sigma(\mathbf{t}_{n})p=\sigma(\mathbf{t}_{n-1})pq_{x_{n}}p is rich. Let r r be the ups of 𝐭 n \mathbf{t}_{n}. Then R = σ ⁡ ( r) ​ p R=\sigma(r)p is ups of σ ⁡ ( 𝐭 n) ​ p \sigma(\mathbf{t}_{n})p. Indeed, if R R has another occurrence in σ ⁡ ( 𝐭 n) ​ p \sigma(\mathbf{t}_{n})p, then by Definition 6.15 this occurrence is σ ( x i ⋯ x j) p \sigma(x_{i}\cdots x_{j})p with x i ⋯ x j = r x_{i}\cdots x_{j}=r and 1 ≤ i ≤ j < n 1\leq i\leq j<n. This implies that r r has another occurrence in 𝐭 n \mathbf{t}_{n}, a contradiction. We have also to show that for any factorization e ​ f = q x n ​ p ef=q_{x_{n}}p with e, f ≠ ε e,f\neq\varepsilon, σ ⁡ ( 𝐭 n) ​ p ​ f − 1 \sigma(\mathbf{t}_{n})pf^{-1} has a ups. With r = x n ​ r ′ ​ x n r=x_{n}r^{\prime}x_{n}, σ ⁡ ( 𝐭 n) ​ p ​ f − 1 \sigma(\mathbf{t}_{n})pf^{-1} has a palindromic suffix R ′ = f ~ − 1 ​ R ​ f − 1 = e ~ ​ R ′ ​ e R^{\prime}=\tilde{f}^{-1}Rf^{-1}=\tilde{e}R^{\prime}e. Clearly r ′ ≠ ε r^{\prime}\neq\varepsilon, thus if R ′ R^{\prime} has another occurrence in σ ⁡ ( 𝐭 n) ​ p ​ f − 1 \sigma(\mathbf{t}_{n})pf^{-1} then it is e ~ σ ( x i ⋯ x j) p e \tilde{e}\sigma(x_{i}\cdots x_{j})pe. As e ≠ ε e\neq\varepsilon, we have x i − 1 = x j + 1 = x n x_{i-1}=x_{j+1}=x_{n} and x i − 1 ⋯ x j + 1 = r x_{i-1}\cdots x_{j+1}=r, a contradiction. ∎

###### Corollary 6.18.

Suppose σ \sigma is a special standard P P -morphism prolongable on a a and let 𝐬 k \mathbf{s}_{k} be the shortest prefix of 𝐬 = σ ω ​ ( a) \mathbf{s}=\sigma^{\omega}(a) that contains all palindromic factors of 𝐬 \mathbf{s} of length at most 2 2. Then 𝐬 \mathbf{s} is rich if (and only if) σ ⁡ ( 𝐬 k) ​ p \sigma(\mathbf{s}_{k})p is rich. ∎

This can be extended to defective words.

###### Theorem 6.19.

Let σ \sigma be a special standard P P -morphism and 𝐭 \mathbf{t} be an infinite word with finite defect k k. Let h h be minimal such that the prefix 𝐭 h \mathbf{t}_{h} has defect k k and all palindromic factors of 𝐭 \mathbf{t} of length at most 2 2 occur in 𝐭 h \mathbf{t}_{h}. Then σ ⁡ ( 𝐭) \sigma(\mathbf{t}) is almost rich and its defect is equal to that of σ ⁡ ( 𝐭 h) ​ p \sigma(\mathbf{t}_{h})p.

###### Proof.

Clearly all prefixes 𝐭 n \mathbf{t}_{n} of 𝐭 \mathbf{t} with n > h n>h have a ups of length at least 3 3. Thus, as in the proof of Theorem 6.17, we find that all prefixes of σ ⁡ ( 𝐭) \sigma(\mathbf{t}) longer than σ ⁡ ( 𝐭 h) ​ p \sigma(\mathbf{t}_{h})p have a ups. ∎

###### Remark 6.20.

Naturally one might suspect that if σ \sigma is a special P P -morphism prolongable on a a, then σ ω ​ ( a) \sigma^{\omega}(a) is almost rich. This is not true, as the following proposition shows.

###### Proposition 6.21.

The special P P -morphism σ \sigma: a ↦ a ​ b ​ a a\mapsto aba, b ↦ b ​ c ​ b b\mapsto bcb, c ↦ c ​ a ​ c c\mapsto cac generates 𝐬 = a b a b c b a b a ⋯ \mathbf{s}=ababcbaba\cdots which has infinitely many defects.

###### Proof.

Let p n = σ n ​ ( a) p_{n}=\sigma^{n}(a) and let w n w_{n} be the prefix of 𝐬 \mathbf{s} of length ( 3 n + 1) / 2 (3^{n}+1)/2, i.e., w n = 𝐬 ( 3 n + 1) / 2 w_{n}=\mathbf{s}_{(3^{n}+1)/2}. Then w n w_{n} ends with some letter, x x say, which is in the middle of p n p_{n}. We show by induction that x x is the one palindromic suffix of w n w_{n}. Easily w n + 1 ​ x = σ ⁡ ( w n) w_{n+1}x=\sigma(w_{n}), thus w n + 1 w_{n+1} ends with y y such that x ​ y ​ x = σ ⁡ ( x) xyx=\sigma(x). If w n + 1 w_{n+1} has a palindromic suffix q q other than y y, then easily | q | > 4 |q|>4. So it follows by 2) of Definition 6.15 that q = y ​ x ​ σ ​ ( u) ​ x ​ y q=yx\sigma(u)xy for some factor u u of 𝐬 \mathbf{s}. Hence σ ⁡ ( x ​ u ​ x) \sigma(xux) is a palindromic suffix of w n + 1 ​ x w_{n+1}x, and therefore x ​ u ​ x xux is a palindromic suffix of w n w_{n}, contradicting the induction hypothesis. ∎

Indeed we have more generally:

###### Proposition 6.22.

Suppose σ \sigma is a special standard P P -morphism prolongable on a a and let 𝐬 h \mathbf{s}_{h} be the shortest prefix of 𝐬 = σ ω ​ ( a) \mathbf{s}=\sigma^{\omega}(a) that contains all palindromic factors of 𝐬 \mathbf{s} of length at most 2 2. Then 𝐬 \mathbf{s} has infinite defect if and only if σ ⁡ ( 𝐬 h) ​ p \sigma(\mathbf{s}_{h})p is not rich.

###### Proof.

ONLY IF: If 𝐬 \mathbf{s} has infinite defect, then σ ⁡ ( 𝐬 h) ​ p \sigma(\mathbf{s}_{h})p is not rich; otherwise, by Corollary 6.18, 𝐬 \mathbf{s} would be rich, which is a contradiction.

IF: Clearly 𝐬 \mathbf{s} has at least one defect as σ ⁡ ( 𝐬 h) ​ p \sigma(\mathbf{s}_{h})p is not rich. To show that 𝐬 \mathbf{s} has infinitely many defects, we suppose by way of contradiction that 𝐬 \mathbf{s} has finite defect k ≥ 1 k\geq 1. Let 𝐬 m \mathbf{s}_{m} be the shortest prefix of 𝐬 \mathbf{s} that has defect k k. By the minimality of m m, 𝐬 n \mathbf{s}_{n} has a ups for all n ≥ m n\geq m and 𝐬 m = x 1 x 2 ⋯ x m \mathbf{s}_{m}=x_{1}x_{2}\cdots x_{m} does not have a ups. But the latter implies that σ ⁡ ( 𝐬 m) ​ p \sigma(\mathbf{s}_{m})p does not have a ups. Indeed, if σ ⁡ ( 𝐬 m) ​ p \sigma(\mathbf{s}_{m})p has a ups, R R say, then R R begins and ends with σ ⁡ ( x m) ​ p \sigma(x_{m})p. Moreover, as σ \sigma is injective, R = σ ( x i ⋯ x m) p R=\sigma(x_{i}\cdots x_{m})p for some i ≤ m i\leq m where r = x i ⋯ x m r=x_{i}\cdots x_{m} is a palindromic suffix of 𝐬 m \mathbf{s}_{m}. But then r r must be unioccurrent in 𝐬 m \mathbf{s}_{m}, otherwise R R is not unioccurrent in σ ⁡ ( 𝐬 m) ​ p \sigma(\mathbf{s}_{m})p, a contradiction. Therefore σ ⁡ ( 𝐬 m) ​ p \sigma(\mathbf{s}_{m})p does not have a ups (i.e., 𝐬 \mathbf{s} has a defect at position | σ ⁡ ( 𝐬 m) ​ p | > m |\sigma(\mathbf{s}_{m})p|>m), a contradiction. ∎

###### Example 6.23.

Consider the special standard P P -morphism φ: a ↦ a ​ a ​ b 2 ​ a ​ a, b ↦ b ​ a ​ b \varphi:a\mapsto aab^{2}aa,b\mapsto bab. By Proposition 6.22, the infinite words φ ω ​ ( a) \varphi^{\omega}(a) and φ ω ​ ( b) \varphi^{\omega}(b) have infinitely many defects since their respective prefixes φ ⁡ ( a ​ a ​ b ​ b) = a ​ a ​ b ​ b ​ a ​ a ​ a ​ a ​ b ​ b ​ a ​ a ​ b ​ a ​ b ​ b ​ a ​ b \varphi(aabb)=aabbaaaabbaababbab and φ ⁡ ( b ​ a ​ b ​ a ​ a ​ b ​ b) = b ​ a ​ b ​ a ​ a ​ b ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ b ​ a ​ a ​ a ​ a ​ b ​ b ​ a ​ a ​ b ​ a ​ b ​ b ​ a ​ b \varphi(babaabb)=babaabbaababaabbaaaabbaababbab are not rich (defects at the two penultimate positions in each case). However, if we consider for instance the (rich) Fibonacci word 𝐟 \mathbf{f}, then φ ⁡ ( 𝐟) \varphi(\mathbf{f}) is a rich infinite word. To show this, we need only use Theorem 6.17: the shortest prefix of 𝐟 \mathbf{f} containing all of its palindromic factors of length at most 2 2 is a ​ b ​ a ​ a abaa and φ ⁡ ( a ​ b ​ a ​ a) = a ​ a ​ b ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ b ​ a ​ a ​ a ​ a ​ b ​ b ​ a ​ a \varphi(abaa)=aabbaababaabbaaaabbaa is rich; whence φ ⁡ ( 𝐟) \varphi(\mathbf{f}) is rich. This provides a good example of a non-periodic rich infinite word that is different from a Sturmian word. It was inspired by the family of rich periodic words: ( a ​ a ​ b k ​ a ​ a ​ b ​ a ​ b) ω (aab^{k}aabab)^{\omega} with k ≥ 0 k\geq 0, given in [7].

###### Remark 6.24.

From Proposition 6.22, we see that special P P -morphisms generate either rich infinite words or infinite words with infinitely many defective positions. Moreover, as any (primitive) special P P -morphism generates a uniformly recurrent infinite word with infinitely many palindromic factors, those with infinite defect also have infinitely many oddities (by Proposition 4.8).

###### Example 6.25.

Using Corollary 6.18, one can easily verify that the following special standard P P -morphism generates a rich infinite word: a ↦ a ​ b ​ b a\mapsto abb, b ↦ a ​ c b\mapsto ac, c ↦ a c\mapsto a.

There is a kind of converse for Theorems 6.17 and 6.19 ( cf. Proposition 5.14).

###### Theorem 6.26.

Suppose 𝐬 = φ ⁡ ( 𝐭) \mathbf{s}=\varphi(\mathbf{t}) where φ \varphi is a special standard P P -morphism. Then D ⁡ ( 𝐬) ≥ D ⁡ ( 𝐭) D(\mathbf{s})\geq D(\mathbf{t}); in particular, if 𝐬 \mathbf{s} is rich, then 𝐭 \mathbf{t} is rich.

###### Proof.

It suffices to show that if 𝐭 = x 1 x 2 x 3 ⋯ \mathbf{t}=x_{1}x_{2}x_{3}\cdots has a defect at position n n, then 𝐬 \mathbf{s} has a defect at position h = | φ ⁡ ( 𝐭 n) ​ p | h=|\varphi(\mathbf{t}_{n})p|. Otherwise, 𝐬 h = φ ⁡ ( 𝐭 n) ​ p \mathbf{s}_{h}=\varphi(\mathbf{t}_{n})p has a ups R R beginning and ending with φ ⁡ ( x n) ​ p \varphi(x_{n})p. Thus, as φ \varphi is a special P P -morphism, R = φ ( x i ⋯ x n) p R=\varphi(x_{i}\cdots x_{n})p for some i ≤ n i\leq n where r = x i ⋯ x n r=x_{i}\cdots x_{n} is a palindromic suffix of 𝐭 n \mathbf{t}_{n}. Now, r r must be unioccurrent in 𝐭 n \mathbf{t}_{n}, otherwise R R is not unioccurrent in 𝐬 h \mathbf{s}_{h}, a contradiction. ∎

###### Remark 6.27.

Notice that property 1) in Definition 6.15 is too strong here; it suffices that φ \varphi is injective, i.e., φ ⁡ ( 𝒜) \varphi(\mathcal{A}) is a code.

From Theorems 6.19 and 6.26, we immediately see that special P P -morphisms strictly preserve almost richness. That is:

###### Theorem 6.28.

Suppose 𝐬 = σ ⁡ ( 𝐭) \mathbf{s}=\sigma(\mathbf{t}) with σ \sigma a special P P -morphism. Then 𝐬 \mathbf{s} is almost rich if and only if 𝐭 \mathbf{t} is almost rich. ∎

Using the following easy lemmas, some of which are well-known, we end this section by proving a theorem which brings us one step closer to a characterization of morphisms preserving richness.

###### Lemma 6.29.

If p, q, p ′, q ′ p,\ q,\ p^{\prime},\ q^{\prime} are non-empty palindromes and p ​ q = p ′ ​ q ′ pq=p^{\prime}q^{\prime} is primitive, then p = p ′, q = q ′ p=p^{\prime},\ q=q^{\prime}. If p ​ q pq is a primitive palindrome with p p, q q palindromes, then p p or q q is empty.

###### Lemma 6.30.

If p ​ q ​ r pqr is a palindrome with p p, q q, r r palindromes, then ( p ​ q) h = ( r ​ q) k (pq)^{h}=(rq)^{k}, for some h, k ∈ ℕ, ( h, k) ≠ ( 0, 0) h,k\in\mathbb{N},(h,k)\neq(0,0).

###### Lemma 6.31.

If X ​ q ​ p Xqp is a prefix of ( p ​ q) ω (pq)^{\omega}, p ​ q pq primitive, p p, q q palindromes, then X = ( p ​ q) h ​ p X=(pq)^{h}p, for some h ≥ 0 h\geq 0.

###### Lemma 6.32.

The morphism θ: a ↦ a n \theta:a\mapsto a^{n}, x ↦ x x\mapsto x for all letter x ≠ a x\neq a strictly preserves richness.

###### Theorem 6.33.

Suppose φ \varphi is a non-erasing morphism on 𝒜 \mathcal{A} such that:

- •

φ ⁡ ( x) ≠ φ ⁡ ( y) \varphi(x)\neq\varphi(y) for all letters x ≠ y x\neq y;

- •

φ ⁡ ( x) \varphi(x) is a primitive word for any letter x ∈ 𝒜 x\in\mathcal{A};

- •

for any three distinct letters a, b, c a,b,c,

 | φ ​ ( a) α ​ φ ​ ( b) β ​ φ ​ ( c) γ = ε, α, β, γ ∈ ℤ ⇒ α ​ β ​ γ = 0. \varphi(a)^{\alpha}\varphi(b)^{\beta}\varphi(c)^{\gamma}=\varepsilon,\ \alpha,\beta,\gamma\in\mathbb{Z}\ \Rightarrow\alpha\beta\gamma=0. |  | (6.1) |

Then if φ \varphi preserves richness, it is of class P P.

###### Proof.

Let us denote the images of the letters by φ i \varphi_{i}, 1 ≤ i ≤ | 𝒜 | 1\leq i\leq|\mathcal{A}|. We first show that φ ⁡ ( a) = φ 1 \varphi(a)=\varphi_{1} and φ ⁡ ( b) = φ 2 \varphi(b)=\varphi_{2} have the form given by the definition of class P P. As a ω a^{\omega} is rich, φ 1 ​ ( a) ω \varphi_{1}(a)^{\omega} is rich, so by Theorem 3.1 φ 1 = p 1 ​ q 1 \varphi_{1}=p_{1}q_{1} with p 1 p_{1}, q 1 q_{1} palindromes. Similarly φ 2 = p 2 ​ q 2 \varphi_{2}=p_{2}q_{2} with p 2 p_{2}, q 2 q_{2} palindromes. Now, as ( a m ​ b ​ a m) ω (a^{m}ba^{m})^{\omega} is rich for any m m, by the same argument as above, we have φ 1 m ​ φ 2 ​ φ 1 m = P ​ Q \varphi_{1}^{m}\varphi_{2}\varphi_{1}^{m}=PQ for some palindromes P, Q P,\ Q. We shall suppose first that both φ 1 \varphi_{1} and φ 2 \varphi_{2} are not palindromes. There are three cases according to the place of the separation between P P and Q Q.

- •

Case P = φ 1 m ​ X P=\varphi_{1}^{m}X, Q = Y ​ φ 1 m Q=Y\varphi_{1}^{m}, X ​ Y = φ 2 XY=\varphi_{2}, X, Y ∈ 𝒜 ∗ X,Y\in\mathcal{A}^{*}. If m m is large, p 1 ​ q 1 ​ X p_{1}q_{1}X is a suffix of P P, thus X ~ ​ q 1 ​ p 1 \tilde{X}q_{1}p_{1} is a prefix of φ 1 m \varphi_{1}^{m}. By Lemma 6.31 X ~ = p 1 ​ ( q 1 ​ p 1) α \tilde{X}=p_{1}(q_{1}p_{1})^{\alpha}. Similarly, Y = ( q 1 ​ p 1) β ​ q 1 Y=(q_{1}p_{1})^{\beta}q_{1}. Thus φ 2 = p 1 ​ ( q 1 ​ p 1) α + β ​ q 1 = φ 1 α + β + 1 \varphi_{2}=p_{1}(q_{1}p_{1})^{\alpha+\beta}q_{1}=\varphi_{1}^{\alpha+\beta+1} which is impossible.

- •

Case P ​ X = φ 1 m PX=\varphi_{1}^{m}, Q = X ​ φ 2 ​ φ 1 m Q=X\varphi_{2}\varphi_{1}^{m}, X ∈ 𝒜 ∗ X\in\mathcal{A}^{*}. Thus X ​ φ 2 ​ P ​ X = Q X\varphi_{2}PX=Q; whence X X is a palindrome and also φ 2 ​ P \varphi_{2}P, i.e., p 2 ​ q 2 ​ P p_{2}q_{2}P. By Lemma 6.30 and as p 2 ​ q 2 p_{2}q_{2} is primitive, we have P ​ q 2 = ( p 2 ​ q 2) ( μ + 1) Pq_{2}=(p_{2}q_{2})^{(\mu+1)}, and therefore P = ( p 2 ​ q 2) μ ​ p 2 P=(p_{2}q_{2})^{\mu}p_{2}. Consider two subcases.

  - –

Case | P | ≥ | p 1 ​ q 1 | |P|\geq|p_{1}q_{1}|. As P P is a (palindromic) prefix of φ 1 m \varphi_{1}^{m} ending with q 1 ​ p 1 q_{1}p_{1}, it has the form ( p 1 ​ q 1) λ ​ p 1 (p_{1}q_{1})^{\lambda}p_{1}, whence

 | ( p 1 ​ q 1) λ ​ p 1 = ( p 2 ​ q 2) μ ​ p 2, λ, μ ≥ 0 (p_{1}q_{1})^{\lambda}p_{1}=(p_{2}q_{2})^{\mu}p_{2},\ \lambda,\ \mu\geq 0 |  | (6.2) |

.

  - –

Case | P | < | p 1 ​ q 1 | |P|<|p_{1}q_{1}|. In this case, | X | |X| is large and, as it is a palindromic suffix of φ 1 m \varphi_{1}^{m}, X = ( q 1 ​ p 1) α ​ q 1 X=(q_{1}p_{1})^{\alpha}q_{1}. Thus, since P ​ X = φ 1 m PX=\varphi_{1}^{m}, we get P = ( p 1 ​ q 1) m − α − 1 ​ p 1 P=(p_{1}q_{1})^{m-\alpha-1}p_{1}, and hence P = p 1 P=p_{1}. So we again get equation ( 6.2) with λ = 0 \lambda=0.

Now let p = ( p 1 ​ q 1) λ ​ p 1 = ( p 2 ​ q 2) μ ​ p 2 p=(p_{1}q_{1})^{\lambda}p_{1}=(p_{2}q_{2})^{\mu}p_{2}. Then φ 1 = p 1 ​ q 1 = p ​ q a \varphi_{1}=p_{1}q_{1}=pq_{a} with q a = ( ( p 1 ​ q 1) λ − 1 ​ p 1) − 1 q_{a}=((p_{1}q_{1})^{\lambda-1}p_{1})^{-1} and φ 2 = p 2 ​ q 2 = p ​ q b \varphi_{2}=p_{2}q_{2}=pq_{b} with q b = ( ( p 2 ​ q 2) μ − 1 ​ p 2) − 1 q_{b}=((p_{2}q_{2})^{\mu-1}p_{2})^{-1}.

- •

Case P = φ 1 m ​ φ 2 ​ X P=\varphi_{1}^{m}\varphi_{2}X, X ​ Q = φ 1 m XQ=\varphi_{1}^{m}, X, Y ∈ 𝒜 ∗ X,\ Y\in\mathcal{A}^{*}. By symmetry we get

 | ( q 1 ​ p 1) λ ​ q 1 = ( q 2 ​ p 2) μ ​ q 2 = p, λ, μ ≥ 0, (q_{1}p_{1})^{\lambda}q_{1}=(q_{2}p_{2})^{\mu}q_{2}=p,\ \lambda,\ \mu\geq 0, |  | (6.3) |

and φ 1 = q a ​ p \varphi_{1}=q_{a}p, φ 2 = q b ​ p \varphi_{2}=q_{b}p.

Now suppose for instance that φ 1 \varphi_{1} is a palindrome (but not φ 2 \varphi_{2}). Then it is easily seen that equation ( 6.2) (resp. equation ( 6.3)) also holds with p 1 = φ 1 p_{1}=\varphi_{1}, q 1 = ε q_{1}=\varepsilon (resp. p 1 = ε p_{1}=\varepsilon, q 1 = φ 1 q_{1}=\varphi_{1}). Let us also observe that the pair ( λ, μ) (\lambda,\ \mu) in equation ( 6.2) or ( 6.3) is unique. Indeed if λ ′ > λ \lambda^{\prime}>\lambda and μ ′ > μ \mu^{\prime}>\mu also work, we get φ 1 λ ′ − λ = φ 2 μ ′ − μ \varphi_{1}^{\lambda^{\prime}-\lambda}=\varphi_{2}^{\mu^{\prime}-\mu}; whence easily φ 1 = φ 2 \varphi_{1}=\varphi_{2}, a contradiction.

Thus the ‘shape’ of class P P is satisfied for letters a, b a,\ b, a ≠ b a\neq b. It remains to pass to 𝒜 \mathcal{A} in totality. Suppose first, with notations as before, that 𝒜 \mathcal{A} contains at least two different letters, a a, b b with φ 1 ≠ φ 2 \varphi_{1}\neq\varphi_{2} both non-palindromes. Let c c be any other letter and φ ⁡ ( c) = φ 3 = p 3 ​ q 3 \varphi(c)=\varphi_{3}=p_{3}q_{3}. Consider the three pairs of letters.

- •

First case:

Using ( a, b) (a,b): φ 1 = p ​ q a \varphi_{1}=pq_{a}, φ 2 = p ​ q b \varphi_{2}=pq_{b};

Using ( a, c) (a,c): φ 1 = r ​ s a \varphi_{1}=rs_{a}, φ 3 = r ​ s c \varphi_{3}=rs_{c};

Using ( b, c) (b,c): φ 2 = t ​ u b \varphi_{2}=tu_{b}, φ 3 = t ​ u c \varphi_{3}=tu_{c}.

Here, p p, q q, r r are given by equation ( 6.2) and similar ones. Suppose for instance | p | ≥ | r | ≥ | t | |p|\geq|r|\geq|t|. Then we get p = φ 1 α ​ r p=\varphi_{1}^{\alpha}r, r = φ 3 β ​ t r=\varphi_{3}^{\beta}t p = φ 2 γ ​ t p=\varphi_{2}^{\gamma}t for some α \alpha, β \beta, γ \gamma. Thus, φ 1 α ​ φ 3 β ​ t = φ 2 γ ​ t \varphi_{1}^{\alpha}\varphi_{3}^{\beta}t=\varphi_{2}^{\gamma}t. This gives α ​ β ​ γ = 0 \alpha\beta\gamma=0 by condition ( 6.1); whence p = r p=r or r = t r=t or p = t p=t. The case r = t r=t for instance gives φ 1 = r ​ s a \varphi_{1}=rs_{a}, φ 2 = r ​ u b \varphi_{2}=ru_{b}, φ 3 = r ​ s c \varphi_{3}=rs_{c}. But, by the observation above, r = p r=p.

- •

Second case: the same for ( a, b) (a,b) and ( a, c) (a,c), but ( b, c) (b,c) gives φ 2 = u b ​ t \varphi_{2}=u_{b}t, φ 3 = u c ​ t \varphi_{3}=u_{c}t and t t is given by an equation of form ( 6.3). We deduce p = φ 1 ξ ​ r p=\varphi_{1}^{\xi}r, p ​ t = φ 2 η pt=\varphi_{2}^{\eta}, r ​ t = φ 3 τ rt=\varphi_{3}^{\tau} for some ξ \xi, η \eta, τ \tau; whence φ 2 η = φ 1 ξ ​ φ 3 τ \varphi_{2}^{\eta}=\varphi_{1}^{\xi}\varphi_{3}^{\tau}. Clearly, p ​ t, r ​ t ≠ ε pt,\ rt\neq\varepsilon. Thus by ( 6.1), ξ = 0 \xi=0, r = p r=p.

In conclusion, φ \varphi is a P P -morphism.

Now suppose 𝒜 \mathcal{A} contains exactly one letter, a a, whose image φ 1 \varphi_{1} is not a palindrome and consider any other two letters b b, c c.

- •

First case:

Using ( a, b) (a,b): φ 1 = p ​ q a \varphi_{1}=pq_{a}, φ 2 = p ​ q b \varphi_{2}=pq_{b};

Using ( a, c) (a,c): φ 1 = r ​ s a \varphi_{1}=rs_{a}, φ 3 = r ​ s c \varphi_{3}=rs_{c}.

Here, p p, r r, are given by equation ( 6.2) and a similar one. Suppose for instance | p | ≥ | r | |p|\geq|r|. We have p = ( p 1 ​ q 1) λ ​ p 1 = φ 2 μ p=(p_{1}q_{1})^{\lambda}p_{1}=\varphi_{2}^{\mu} and r = ( p 1 ​ q 1) λ ′ ​ p 1 = φ 2 μ ′ r=(p_{1}q_{1})^{\lambda^{\prime}}p_{1}=\varphi_{2}^{\mu^{\prime}}; whence φ 1 λ ′ − λ = φ 2 μ ′ − μ \varphi_{1}^{\lambda^{\prime}-\lambda}=\varphi_{2}^{\mu^{\prime}-\mu}. As φ 1 ≠ φ 2 \varphi_{1}\neq\varphi_{2} are primitive, λ ′ − λ = 0 \lambda^{\prime}-\lambda=0, r = p r=p.

- •

Second case: the same for ( a, b) (a,b), but ( a, c) (a,c) gives φ 1 = s a ​ r \varphi_{1}=s_{a}r, φ 3 = s c ​ r \varphi_{3}=s_{c}r with r = ( q 1 ​ p 1) θ ​ q 1 = φ 3 ν r=(q_{1}p_{1})^{\theta}q_{1}=\varphi_{3}^{\nu}, and hence p ​ r = φ 1 λ + θ + 1 = φ 2 μ ​ φ 3 ν pr=\varphi_{1}^{\lambda+\theta+1}=\varphi_{2}^{\mu}\varphi_{3}^{\nu}. As λ + θ + 1 > 0 \lambda+\theta+1>0 this gives μ ​ ν = 0 \mu\nu=0 by ( 6.1), which is impossible.

Lastly, if all images of letters are palindromes, then φ \varphi is trivially of class P P. ∎

###### Remark 6.34.

Condition ( 6.1) of Theorem 6.33 is satisfied if φ \varphi is injective, or if it strictly preserves richness (using the property that a x ​ b y ​ c z ​ a x a^{x}b^{y}c^{z}a^{x} is not rich). The theorem could be extended to non-primitive φ ⁡ ( x) \varphi(x) using Lemma 6.32 but conditions should be formulated accordingly.

Now let us recall from Theorem 4.3 that periodic almost rich words are of the form u ω u^{\omega} where u u is a product of two palindromes and that only this property is used in proof of Theorem 6.33. Thus we also have:

###### Theorem 6.35.

Suppose φ \varphi is a morphism satisfying the conditions of Theorem 6.33. Then if φ \varphi preserves almost richness, it is of class P P. ∎

Furthermore, it is not too difficult to see that ‘preserves almost richness’ could be replaced by ‘preserves infiniteness of palindromic factors’. This is related to the following long-standing open question posed by Hof, Knill, and Simon in [19]: are there (uniformly recurrent) infinite words containing arbitrarily long palindromes that arise from primitive morphisms, none of which belongs to class P P? The answer is believed to be no. Up to now, it has only been shown to hold in the periodic case (see [1]) and also in the 2 2 -letter case (see [28]).

## 7 Concluding remarks

To end, we mention a particularly relevant result that gives a good estimate of the palindromic complexity of uniformly recurrent infinite words in terms of the factor complexity. Let us first recall that the palindromic complexity function 𝒫 ⁡ ( n) \mathcal{P}(n) (resp. factor complexity function 𝒞 ⁡ ( n) \mathcal{C}(n)) of a given infinite word counts the number of different palindromic factors (resp. number of different factors) of length n n for each n ≥ 0 n\geq 0. In [4], Baláži et al. proved that for uniformly recurrent infinite words with factors closed under reversal,

 | 𝒫 ⁡ ( n) + 𝒫 ⁡ ( n + 1) ≤ 𝒞 ⁡ ( n + 1) − 𝒞 ⁡ ( n) + 2 for all n ∈ ℕ. \mathcal{P}(n)+\mathcal{P}(n+1)\leq\mathcal{C}(n+1)-\mathcal{C}(n)+2\quad\mbox{for all $n\in\mathbb{N}$}. |  | (7.1) |

Infinite words for which 𝒫 ⁡ ( n) + 𝒫 ⁡ ( n + 1) \mathcal{P}(n)+\mathcal{P}(n+1) always reaches the upper bound given in relation ( 7.1) can be viewed as words containing the maximum number of palindromes. Naturally one would conjecture that all such words are rich. Indeed, this assertion is true – it was recently proved by the first and fourth authors together with M. Bucci and A. De Luca in [8]. Interestingly, its proof relies upon another new characterization of rich words, which is useful for establishing the key part of the proof, namely that the so-called super reduced Rauzy graph is a tree.

## References

- [1] J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, Palindrome complexity, Theoret. Comput. Sci. 292 (2003) 9–31.
- [2] P. Ambrož, C. Frougny, Z. Masáková, E. Pelantová, Palindromic complexity of infinite words associated with simple Parry numbers, Ann. Inst. Fourier (Grenoble) 56 (2006) 2131–2160.
- [3] V. Anne, L.Q. Zamboni, I. Zorca, Palindromes and pseudo-palindromes in episturmian and pseudo-palindromic infinite words, in: Proceedings of the Fifth International Conference on Words (Montréal, Canada), September 13–17, 2005. Publications du LaCIM 36 (2005) 91–100.
- [4] P. Baláži, Z. Masáková, E. Pelantová, Factor versus palindromic complexity of uniformly recurrent infinite words, Theoret. Comput. Sci. 380 (2007) 266–275.
- [5] J. Berstel, Sturmian and episturmian words (A survey of some recent results), in: Proceedings of CAI 2007, Lecture Notes in Computer Science, vol. 4728, 2007, pp. 23–47.
- [6] J. Berstel, D. Perrin, *Theory of codes*, vol. 117 of Pure and Applied Mathematics, Academic Press Inc., Orlando, FL, 1985.
- [7] S. Brlek, S. Hamel, M. Nivat, C. Reutenauer, On the palindromic complexity of infinite words, Internat. J. Found. Comput. Sci. 15 (2004) 293–306.
- [8] M. Bucci, A. De Luca, A. Glen, L.Q. Zamboni, A connection between palindromic and factor complexity using return words, Adv. in Appl. Math., to appear, arXiv:0802.1332.
- [9] J. Cassaigne, Complexité et facteurs spéciaux, Bull. Belg. Math. Soc. Simon Stevin 4 (1997) 67–88.
- [10] E.M. Coven, G.A. Hedlund, Sequences with minimal block growth, *Math. Systems Theory*7 (1973) 138–153.
- [11] D. Damanik, L.Q. Zamboni, Combinatorial properties of Arnoux-Rauzy subshifts and applications to Schrödinger operators, Rev. Math. Phys. 15 (2003) 745–763.
- [12] A. de Luca, Sturmian words: structure, combinatorics and their arithmetics, *Theoret. Comput. Sci.*183 (1997) 45–82.
- [13] X. Droubay, J. Justin, G. Pirillo, Episturmian words and some constructions of de Luca and Rauzy, *Theoret. Comput. Sci.*255 (2001) 539–553.
- [14] X. Droubay, G. Pirillo, Palindromes and Sturmian words, Theoret. Comput. Sci. 223 (1999) 73–85.
- [15] S. Fischler, Palindromic prefixes and episturmian words, J. Combin. Theory Ser. A 113 (2006) 1281–1304.
- [16] S. Fischler, Palindromic prefixes and diophantine approximation, Monatsh. Math. 151 (2007) 11–37.
- [17] A.S. Fraenkel, Complementing and exactly covering sequences, J. Combin. Theory Ser. A 14 (1973) 8–20.
- [18] A. Glen, J. Justin, Episturmian words: a survey, Preprint, 2007, arXiv:0801.1655.
- [19] A. Hof, O. Knill, B. Simon, Singular continuous spectrum for palindromic Schrödinger operators, Commun. Math. Phys. 174 (1995) 149–159.
- [20] C. Holton, L.Q. Zamboni, Descendants of primitive substitutions, Theory Comput. Syst. 32 (1999) 133–157.
- [21] J. Justin, G. Pirillo, Episturmian words and episturmian morphisms, *Theoret. Comput. Sci.*276 (2002) 281–313.
- [22] J. Justin, L. Vuillon, Return words in Sturmian and episturmian words, Theoret. Inform. Appl. 34 (2000) 343–356.
- [23] M. Lothaire, Combinatorics On Words, vol. 17 of Encyclopedia of Mathematics and its Applications, Addison-Wesley, Reading, Massachusetts, 1983.
- [24] M. Lothaire, *Algebraic Combinatorics On Words*, vol. 90 of Encyclopedia of Mathematics and its Applications, Cambridge University Press, U.K., 2002.
- [25] G. Paquin, L. Vuillon, A characterization of balanced episturmian sequences, Electron. J. Combin. 14 (2007) #R33, pp. 12.
- [26] N. Pytheas Fogg, Substitutions In Dynamics, Arithmetics And Combinatorics, vol. 1794 of Lecture Notes in Mathematics, Springer-Verlag, Berlin, 2002.
- [27] M. Queffélec, *Substitution dynamical systems – spectral analysis*, vol. 1924 of Lecture Notes in Mathematics, Springer-Verlag, New York, 1987.
- [28] B. Tan, Mirror substitutions and palindromic sequences, Theoret. Comput. Sci. 389 (2007) 118–124.
- [29] R. Tijdeman, Exact covers of balanced sequences and Fraenkel’s conjecture, in: Algebraic Number Theory and Diophantine Analysis (Graz, 1998 1998), de Gruyter, Berlin, 200, pp. 467–483.
- [30] L. Vuillon, Balanced words, Bull. Belg. Math. Soc. Simon Stevin 10 (2003) 787–805.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/0801.1655
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/0801.1656
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0801.1656
[7]: https://arxiv.org/pdf/0801.1656
[8]: /html/0801.1657
