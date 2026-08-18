<!-- source: https://ar5iv.labs.arxiv.org/html/1803.02073 | converted from HTML -->

[1803.02073] Formal intercepts of Sturmian words

# Formal intercepts of Sturmian words

Caïus Wojcik

###### Abstract

We introduce the concept of formal intercept of Sturmian words, defined as an infinite sequence of integers written in Ostrowski expansion. We first recall the combinatorial proofs of basics properties of sturmian words. Then, we study the Rauzy graphs and repetition functions of Sturmian words. In the last part, we define the formal intercept associated to a sturmian word.

Sturmian words are defined as the infinite words having lowest unbounded complexity. They enjoy rich combinatorial structures, that are sometimes difficult to quantify. However, unlike most of other dynamical systems, in the case of sturmian words one can hope to find some explicit combinatorial formulas.

In order to describe the combinatorial properties of Sturmian words, we give here a combinatorial description of the second parameter in the caracterisation of sturmian words. The first parameter, well-known, is the slope, which is an irrational number in ] 0, 1 []0,1[, whose continued fraction expansion describes the set of factors of a sturmian word. The second parameter, the intercept, has been defined dynamicaly in the litterature, but its combinatorial implications in the structure of sturmian words were not well understood in the author’s view.

In this paper, which is the first of two about formal intercepts, we define the formal intercept of a given Sturmian word, and show that there is a natural bijection between Sturmian words of a given slope, and the formal intercepts associated to this slope. Since we insist on the combinatorial properties of such parameters, and for sake of completeness, we start from the bottom about Sturmian words, and give entierely combinatorial proofs of their basic properties.

The paper is organized as follows. In the first section, we recall the proofs of basic properties of sturmian words. In the second part of the paper, we give a description of the factor graph and some links with the repetition function of Sturmian words. In the last part, we define the formal intercept of Sturmian word.

## 1 Basic properties

In this section we give combinatorial proofs of the main properties about sturmian words. All these come from the classical book [1], rewritten in a concise manner.

### 1.1 The Morse-Hedlund theorem

Let A A be a finite set, the alphabet. A finite ord over A A is an element of the union ∪ n A n \cup_{n}A^{n}, and if u ∈ A n u\in A^{n}, we set | u | = n |u|=n and call it its length. For a letter a ∈ A a\in A we note | u | a |u|_{a} the number of occurrences of the letter a a in u u.

An infinite word x = x 1 ​ x 2 ​ x 3 ​ … x=x_{1}x_{2}x_{3}\ldots is an element of A ℕ A^{\mathbb{N}}. A factor of x x is a finite word occurring in x x. For such an infinite word, we note ℙ n ​ ( x) = x 1 ​ x 2 ​ … ​ x n \mathbb{P}_{n}(x)=x_{1}x_{2}\ldots x_{n} its prefix of length n n, and we note T ⁡ ( x) = x 2 ​ x 3 ​ x 4 ​ … T(x)=x_{2}x_{3}x_{4}\ldots the shifted of x x, which consists of the infinite word x x deprived of its first letter. A suffix of x x is an element of the form T k ​ ( x) T^{k}(x) for some k ≥ 1 k\geq 1.

###### Definition 1.

Let x = x 1 ​ x 2 ​ x 3 ​ … x=x_{1}x_{2}x_{3}\ldots be an infinite word. For n ≥ 1 n\geq 1, set

p ⁡ ( x, n) = C ​ a ​ r ​ d ​ { x i ​ x i + 1 ​ … ​ x i + n − 1 | i ≥ 1 } p(x,n)=Card\{x_{i}x_{i+1}\ldots x_{i+n-1}\ |\ i\geq 1\}

and call p ⁡ ( x, ⋅) p(x,\cdot) the complexity function of x x.

###### Theorem 1 (Morse-Hendlund).

Let x x be an infinite word over A A. Then x x is ultimately periodic if and only if there exists n ≥ 1 n\geq 1 such that p ⁡ ( x, n) ≤ n p(x,n)\leq n.

###### Proof.

The condition is clearly necessary, since a ultimately periodic word has bounded complexity function. For the converse, from the increasing of the complexity function and the pigeonhole principle, there exists n ∈ ℕ ∗ n\in\mathbb{N}^{*} such that p ⁡ ( x, n) = p ⁡ ( x, n + 1) p(x,n)=p(x,n+1). That means that every factor u u of x x can be only uniquely extend on the right. Let u u be a factor of x x having two occurrences in x x. The two corresponding suffixes of x x are uniquely determined by u u, and hence are equal, showing that x x is ultimately periodic. ∎

This theorem can be reformulated as follows : if x x is a non-ultimately periodic word, then p ⁡ ( x, n) ≥ n + 1 p(x,n)\geq n+1 for all n ≥ 1 n\geq 1.

###### Definition 2.

An infinite word is said to be Sturmian if

∀ n ≥ 1 \forall n\geq 1, p ⁡ ( x, n) = n + 1 p(x,n)=n+1.

Notice that a Sturmian word x x is a word over a 2 2 -letter alphabet, since p ⁡ ( x, 1) = 2 p(x,1)=2, so we assume from now on that A = { 0, 1 } A=\{0,1\}. Also, notice that since T ⁡ ( x) T(x) is non-ultimately periodic, T ⁡ ( x) T(x) and x x share the same set of factors.

For all n ≥ 1 n\geq 1, there exists a unique factor L n L_{n} of x x of length n n such that both 0 ​ L n 0L_{n} and 1 ​ L n 1L_{n} are factor of x x, called the left special factor of x x of length n n. Similarly, define the right special factor R n R_{n} of x x as the unique factor of x x of length n n such that both R n ​ 0 R_{n}0 and R n ​ 1 R_{n}1 are factors of x x.

### 1.2 Slopes and balanced words

###### Definition 3.

A word over A = { 0, 1 } A=\{0,1\} is said to be balanced if for all pair of factors u, v u,v with | u | = | v | |u|=|v| we have

| | u | 1 − | ​ v | 1 | ≤ 1 ||u|_{1}-|v|_{1}|\leq 1.

###### Lemma 1.

A word x x is balanced if and only if for all palindrome w w, 0 ​ w ​ 0 0w0 and 1 ​ w ​ 1 1w1 are not both factors of x x.

###### Proof.

Note that the direct implication holds for any word w w. For the converse, we take u u and v v of minimal length such that | | u | 1 − | ​ v | 1 | > 1 ||u|_{1}-|v|_{1}|>1, and we show that { u, v } = { 0 ​ w ​ 0, 1 ​ w ​ 1 } \{u,v\}=\{0w0,1w1\} for some palindrome w w.

The minimality hypothesis implies that u u and v v start with different letters, and let w w be the longest common prefix of u ∗ u^{*} and v ∗ v^{*}, where the star denotes a word deprived of its first letter. Write

u = a ​ w ​ c ​ u ′ u=awcu^{\prime} and v = b ​ w ​ d ​ v ′ v=bwdv^{\prime}

with a, b, c, d ∈ { 0, 1 } a,b,c,d\in\{0,1\} and a ≠ b a\neq b. Since the couple ( u ′, v ′) (u^{\prime},v^{\prime}) cannot satisfy the balanced property by minimality, we must have c = a c=a and d = b d=b. From this the words u ′ u^{\prime} and v ′ v^{\prime} must be empty, 0 ​ w ​ 0 0w0 and 1 ​ w ​ 1 1w1 factors of x x.

In order to show that w w is a palindrome, let t t be the longest common prefix of w w and w ~ \tilde{w} where the tilda denotes the reversal of a word and assume by contradiction that t ≠ w t\neq w. Let a a be the letter following t t in w w and a ¯ \bar{a} the opposite letter. If a = 0 a=0 then 0 ​ t ​ 0 0t0 is a prefix of 0 ​ w ​ 0 0w0 and 1 ​ t ~ ​ 1 1\tilde{t}1 is a suffix of 1 ​ w ​ 1 1w1, contradicting the minimality hypothesis. If a = 1 a=1 then writing 0 ​ w ​ 0 = 0 ​ t ​ 1 ​ u ′ 0w0=0t1u^{\prime} and 1 ​ w ​ 1 = v ′ ​ 0 ​ t ~ ​ 1 1w1=v^{\prime}0\tilde{t}1 offers a pair u ′, v ′ u^{\prime},v^{\prime} contradicting the minimality hypothesis. ∎

###### Theorem 2.

1. 1)

An infinite balanced word satisfies ∀ n ∈ ℕ ∗, p ⁡ ( x, n) ≤ n + 1 \forall n\in\mathbb{N}^{*},\ p(x,n)\leq n+1.

2. 2)

An infinite word over A = { 0, 1 } A=\{0,1\} is Sturmian if and only if he is balanced and non-ultimately periodic.

###### Proof.

1) Let x x be a balanced word and suppose that there is n ∈ ℕ ∗ n\in\mathbb{N}^{*} such that p ⁡ ( x, n + 1) ≥ p ⁡ ( x, n) + 2 p(x,n+1)\geq p(x,n)+2. Then x x has two distincts left special factors y y and z z, and let w w be their longest common prefix. Then both 0 ​ w ​ 0 0w0 and 1 ​ w ​ 1 1w1 are factors of x x, in contradiction with the balanced hypothesis.

2) A non-ultimately periodic word satisfy ∀ n ∈ ℕ ∗, p ⁡ ( x, n) ≥ n + 1 \forall n\in\mathbb{N}^{*},\ p(x,n)\geq n+1 by the Morse & Hedlund theorem. Combined with OPEN 1) 1), we get the sufficient condition.

For the converse, we have to show that a Sturmian word x x is necessarily balanced. Arguing by contradiction and using the Lemma, we assume that there is a palindrome w w such that both 0 ​ w ​ 0 0w0 and 1 ​ w ​ 1 1w1 are factors of x x. The word w w is a right special factor of x x, and one of the words 0 ​ w 0w or 1 ​ w 1w is a right special factor, and we assume without loss of generality that 0 ​ w 0w is a right special factor. By the unicity of right special factors of a given length for Sturmian words, 1 ​ w 1w is not a right special factor. So the three words 0 ​ w ​ 0 0w0, 1 ​ w ​ 1 1w1 and 0 ​ w ​ 1 0w1 are factors of x x although 1 ​ w ​ 0 1w0 is not.

Let u = 1 ​ w ​ 1 ​ v u=1w1v be a factor of x x with the prefix 1 ​ w ​ 1 1w1 and | v | = | w | |v|=|w|. We show that the right special factor of x x of length | w | + 1 |w|+1, namely 0 ​ w 0w, is not a factor of u u. Suppose this is the case and write the word u u as :

u = 1 ​ w ​ 1 ​ v = λ ​ 0 ​ w ​ μ u=1w1v=\lambda 0w\mu

and let t t be the word such that u = λ ​ 0 ​ t ​ 1 ​ v u=\lambda 0t1v. The word t t is both a prefix and a suffix of w w, and we also see that t ​ 1 t1 is a prefix of w w and that 0 ​ t 0t is a suffix of w w. But since w w is a palindrome, the ( | t | + 1) t ​ h ¯ (|t|+1)^{\underline{th}} letter of w w is both a 0 and a 1, and that’s a contradiction.

We’ve just shown that no factor of u = 1 ​ w ​ 1 ​ v u=1w1v of length n = | w | + 1 n=|w|+1 is a right special factor. Since there is at most n n such factors, and | u | = 2 ​ n |u|=2n, there is a factor ν \nu of length n n in u u that occurs twice. Let’s show that this implies that x x is ultimately periodic, hence proving the theorem. Let’s note y y the suffix of x x beginning at the first occurrence of ν \nu, and z z the suffix of x x beginning at its second occurrence. The two infinite words y y and z z share the same prefix of length n n, but since this prefix is not a right special factor, its following letter in y y and z z is uniquely determined, so that y y and z z share the same prefix of length n + 1 n+1. And the letter following this prefix is also uniquely determined since the preceeding word of length n n appears in u u and so is not a right special factor. This argument goes on and on, so that we must have y = z y=z. There are two suffixes of the infinite word x x, taken at different starting point, that are equal. This shows that x x is ultimately periodic.

∎

The following proposition is an extension of the balanced property.

###### Proposition 1.

A word x x is balanced if and only if for all factors u, v u,v of x x we have

| | u | 1 | u | − | v | 1 | v | | < 1 | u | + 1 | v | \displaystyle\left|\frac{|u|_{1}}{|u|}-\frac{|v|_{1}}{|v|}\right|<\frac{1}{|u|}+\frac{1}{|v|}.

###### Proof.

The sufficient condition is clear by taking two words of the same length. Conversely, we show the result by induction on max ⁡ | u |, | v | \max{|u|,|v|}. If | u | = | v | |u|=|v| then the result follows directly from the balanced property. If | u | > | v | |u|>|v|, write u = s ​ t u=st with | s | = | v | |s|=|v|. From the balanced property on the one hand, and the induction hypothesis on the other, we have :

| | s | 1 | s | − | v | 1 | v | | ≤ 1 | v | \displaystyle\left|\frac{|s|_{1}}{|s|}-\frac{|v|_{1}}{|v|}\right|\leq\frac{1}{|v|}

| | t | 1 | t | − | v | 1 | v | | < 1 | t | + 1 | v | \displaystyle\left|\frac{|t|_{1}}{|t|}-\frac{|v|_{1}}{|v|}\right|<\frac{1}{|t|}+\frac{1}{|v|}

we also have by simple calculation :

| u | 1 | u | − | v | 1 | v | = | s | | u | ​ ( | s | 1 | s | − | v | 1 | v |) + | t | | u | ​ ( | t | 1 | t | − | v | 1 | v |) \displaystyle\frac{|u|_{1}}{|u|}-\frac{|v|_{1}}{|v|}=\frac{|s|}{|u|}\left(\frac{|s|_{1}}{|s|}-\frac{|v|_{1}}{|v|}\right)+\frac{|t|}{|u|}\left(\frac{|t|_{1}}{|t|}-\frac{|v|_{1}}{|v|}\right)

so that

| | u | 1 | u | − | v | 1 | v | | < | s | | u | × 1 | v | + | t | | u | ​ ( 1 | t | + 1 | v |) = 1 | u | + 1 | v | \displaystyle\left|\frac{|u|_{1}}{|u|}-\frac{|v|_{1}}{|v|}\right|<\frac{|s|}{|u|}\times\frac{1}{|v|}+\frac{|t|}{|u|}\left(\frac{1}{|t|}+\frac{1}{|v|}\right)=\frac{1}{|u|}+\frac{1}{|v|}

wich ends the proof. ∎

This proposition shows that the family of numbers ( | u | 1 / | u |) (|u|_{1}/|u|) behave like a Cauchy sequence when u u runs through the factors of a balanced word x x. Hence we can define :

###### Definition 4.

Let x x be a balanced word. We define the slople α \alpha of x x as the number

lim | u | → + ∞ | u | 1 | u | \displaystyle\lim_{|u|\rightarrow+\infty}\frac{|u|_{1}}{|u|}

where the limit is taken over the factors of x x.

By using this definition in the second caracterisation of balanced word, we get the speed relation :

| | u | 1 | u | − α | ≤ 1 | u | \displaystyle\left|\frac{|u|_{1}}{|u|}-\alpha\right|\leq\frac{1}{|u|}

for every factor u u of a balanced word of slope α \alpha.

If a word is ultimately periodic, then its slope is a rational number. The following theorem shows that the converse is true for balanced word.

###### Theorem 3.

1. 1)

A balanced word is Sturmian if and only if its slope is irrational.

2. 2)

Two balanced words of different slope only share a finite number of factors.

3. 3)

Two Sturmian words of same slope have same set of factors.

###### Proof.

1) Suppose that α = p / q \alpha=p/q is the slope of a Sturmian word x x, with p, q p,q integers. Assume first that for every factor u u of x x such that | u | = q |u|=q we have | u | 1 = p |u|_{1}=p. If w w is any factor of x x of length q + 1 q+1, then by assumption, the prefix and suffix of length q q have the same number of 1 1 ’s, so that w w must begin and end with the same letter, showing that x x is ultimately periodic. Suppose now that there is an infinity of factors u u of x x such that | u | = q |u|=q and | u | ≠ p |u|\neq p. By the balanced property and without loss of generality we can assume | u | 1 = p + 1 |u|_{1}=p+1 for an infinity of such factors. Let u u and v v be two non-crossing such factors and w = u ​ z ​ v w=uzv a factor of x x. From the relations :

| | w | 1 − p q ​ | w | | = | 2 + | z | 1 − p q ​ | z | | ≤ 1 \displaystyle\left||w|_{1}-\frac{p}{q}|w|\right|=\left|2+|z|_{1}-\frac{p}{q}|z|\right|\leq 1 and | | z | 1 − p q ​ | z | | ≤ 1 \displaystyle\left||z|_{1}-\frac{p}{q}|z|\right|\leq 1

we get

| z | 1 − p q = − 1 \displaystyle|z|_{1}-\frac{p}{q}=-1

then

| | u | 1 | u | − | z | 1 | z | | = | | u | 1 | u | − p q − ( | z | 1 | z | − p q) | = | 1 q + 1 | z | | = 1 | u | + 1 | z | \displaystyle\left|\frac{|u|_{1}}{|u|}-\frac{|z|_{1}}{|z|}\right|=\left|\frac{|u|_{1}}{|u|}-\frac{p}{q}-\left(\frac{|z|_{1}}{|z|}-\frac{p}{q}\right)\right|=\left|\frac{1}{q}+\frac{1}{|z|}\right|=\frac{1}{|u|}+\frac{1}{|z|}

contradicting the strict inequality in the second caracterisation of balanced words.

2) The speed relation implies that for two distincts slopes α \alpha and β \beta, a finite word that is too long cannot be a common factor of two balanced words of slope α \alpha and β \beta.

3) We first show that two Sturmian words have same set of left special factors. Let x x and y y be two Sturmian words of slope α \alpha. Write L n ​ ( x) L_{n}(x) and L n ​ ( y) L_{n}(y) for the left special factor of length n ≥ 1 n\geq 1 of x x and y y respectively. From the strict inequality

| | u | 1 | u | − α | < 1 | u | \displaystyle\left|\frac{|u|_{1}}{|u|}-\alpha\right|<\frac{1}{|u|}

satisfied by the 2 2 -letters factors

0 ​ L 1 ​ ( x) 0L_{1}(x), 1 ​ L 1 ​ ( x) 1L_{1}(x), 0 ​ L 1 ​ ( y) 0L_{1}(y), 0 ​ L 1 ​ ( y) 0L_{1}(y),

we see that 2 ​ α 2\alpha must lie in the two open balls of radius 1 1 and center | L 1 ​ ( x) | 1 |L_{1}(x)|_{1} and | L 1 ​ ( x) | 1 + 1 |L_{1}(x)|_{1}+1, determining uniquely the number | L 1 ​ ( x) | 1 |L_{1}(x)|_{1} which has to be equal to | L 1 ​ ( y) | 1 |L_{1}(y)|_{1}. Since they are both letters, we have | L 1 ​ ( x) | 1 = | L 1 ​ ( y) | 1 |L_{1}(x)|_{1}=|L_{1}(y)|_{1}. Recall that two left special factors of a Sturmian word are prefix of one another, so that we can prove the result by induction : suppose that L n − 1 ​ ( x) = L n − 1 ​ ( y) L_{n-1}(x)=L_{n-1}(y), and by the same argument we have | L n ​ ( x) | 1 = | L n ​ ( y) | 1 |L_{n}(x)|_{1}=|L_{n}(y)|_{1} and so L n ​ ( x) = L n ​ ( y) L_{n}(x)=L_{n}(y). Let c α = lim L n ​ ( x) = lim L n ​ ( y) c_{\alpha}=\lim L_{n}(x)=\lim L_{n}(y), then c α c_{\alpha} is a balanced word that is not ultimately periodic since its slope is irrationnal, so c α c_{\alpha} is a Sturmian word, and by the cardinality of the sets of factors involved, we see that x x, y y and c α c_{\alpha} share the same set of factors. ∎

###### Definition 5.

For all Sturmian word of slope α \alpha, the sequence ( L n) (L_{n}) of its left special factors defines a Sturmian word :

c α = lim L n c_{\alpha}=\lim L_{n}

which depends only on the slope α \alpha, noted c α c_{\alpha} and called the caracteristic Sturmian word of slope α \alpha.

###### Proposition 2.

Let ( L n) (L_{n}) and ( R n) (R_{n}) be the sequences of left special factors and right special factors respectively of a Sturmian word. Then :

1. 1)

The Sturmian word x x is caracteristic if and only if both 0 ​ x 0x and 1 ​ x 1x are Sturmian.

2. 2)

c α = lim R n ~ c_{\alpha}=\lim\widetilde{R_{n}}

3. 3)

∀ n ∈ ℕ ∗ \forall n\in\mathbb{N}^{*}, R n = L n ~ R_{n}=\widetilde{L_{n}}

4. 4)

The set of factors of a Sturmian word is stable under reversal,

5. 5)

For all Sturmian word x x, at least one of the words 0 ​ x 0x and 1 ​ x 1x is Sturmian

###### Proof.

1) If both 0 ​ x 0x and 1 ​ x 1x are Sturmian, then all the prefixes of x x are left special, so x = lim L n = c α x=\lim L_{n}=c_{\alpha}.

2) Since the right special factors are suffixes of one another, the word c = lim R n ~ c=\lim\widetilde{R_{n}} is well-defined, balanced and of irrational slope, so it is Sturmian. Besides, both 0 ​ c 0c and 1 ​ c 1c are Sturmian, so that c = c α c=c_{\alpha} by 1).

3) Obvious since c α = lim L n = lim R n ~ c_{\alpha}=\lim L_{n}=\lim\widetilde{R_{n}}.

4) Obvious from OPEN 3) 3) and the fact that a Sturmian word and the caracteristic word of same slope share the same set of factors.

5) It is clear if x x is caracteristic. Let u u be a prefix of x x that is not left special. Then by OPEN 4) 4) there is a unique letter a ∈ { 0, 1 } a\in\{0,1\} such that a ​ u au is a factor of x x, and this letter does not depend on u u. The word a ​ x ax is then balanced and non-ultimately periodic, so it is Sturmian. ∎

### 1.3 Caracteristic words and continued fractions

Recall that every irrational number α ∈] 0, 1 [\alpha\in]0,1[can be written uniquely in the form

α = [0; a 1, a 2, …] = 1 a 1 + 1 a 2 + 1 a 3 + … \alpha=[0;a_{1},a_{2},\ldots]=\displaystyle\cfrac{1}{a_{1}+\cfrac{1}{a_{2}+\cfrac{1}{a_{3}+\ldots}}}

with a i ∈ ℕ ∗ a_{i}\in\mathbb{N}^{*} for i ≥ 1 i\geq 1. The coefficient ( a i) (a_{i}) are called the partial quotient of α \alpha.

We define the positive integers p n p_{n} and q n q_{n} as the irreducible quotient

p n q n = [0; a 1, …, a n] \displaystyle\frac{p_{n}}{q_{n}}=[0;a_{1},\ldots,a_{n}]

and we set q − 1 = 0 q_{-1}=0 and q 0 = 1 q_{0}=1. We call the sequence ( q n) (q_{n}) the sequence of continuant of α \alpha. We have the induction relation

q n + 1 = a n + 1 ​ q n + q n − 1 q_{n+1}=a_{n+1}q_{n}+q_{n-1}

for n ≥ 0 n\geq 0. Notice that for all n ≥ 0 n\geq 0, q n + 1 q_{n+1} and q n q_{n} are relatively prime (the induction steps are the steps of Euclide’s algorithm).

###### Theorem 4.

Let α = [0; a 1, a 2, …] \alpha=[0;a_{1},a_{2},\ldots] be an irrational number in ] 0, 1 []0,1[. Define the sequence of words :

s − 1 = 1 s_{-1}=1, s 0 = 0 s_{0}=0, s 1 = s 0 a 1 − 1 ​ s − 1 s_{1}=s_{0}^{a_{1}-1}s_{-1},

s n + 1 = s n a n + 1 ​ s n − 1 s_{n+1}=s_{n}^{a_{n+1}}s_{n-1}

for all n ≥ 1 n\geq 1. Then :

c α = lim s n c_{\alpha}=\lim s_{n}.

###### Proof.

Define the two morphisms

E E: 0 ⟼ 1 1 ⟼ 0 \begin{matrix}0&\longmapsto&1\\ 1&\longmapsto&0\\ \end{matrix} and G G: 0 ⟼ 0 1 ⟼ 01 \begin{matrix}0&\longmapsto&0\\ 1&\longmapsto&01\\ \end{matrix},

they are injective, in the sense that if x x and y y are two infinite words such that G ⁡ ( x) = G ⁡ ( y) G(x)=G(y), then x = y x=y, and the same for E E. We obviously have that x x is sturmian if and only if E ⁡ ( x) E(x) is sturmian. Let’s show now that x x is Sturmian if and only if G ⁡ ( x) G(x) is Sturmian.

Suppose that G ⁡ ( x) G(x) is unbalanced : there exists a palindrome w w such that both 0 ​ w ​ 0 0w0 and 1 ​ w ​ 1 1w1 are factors of G ⁡ ( x) G(x). In view of G G there must exist a word z z such that w = 0 ​ z ​ 0 w=0z0, moreover 01 ​ w ​ 1 = 010 ​ z ​ 01 01w1=010z01 is a factor of G ⁡ ( x) G(x). There must be a word y y such that 0 ​ z = G ⁡ ( y) 0z=G(y) and 01 ​ w ​ 1 = G ⁡ ( 1 ​ y ​ 1) 01w1=G(1y1) so that 1 ​ y ​ 1 1y1 is a factor of x x by injectivity of G G. On the other hand 0 ​ w ​ 0 = 00 ​ z ​ 00 = G ⁡ ( 0 ​ y ​ 0) 0w0=00z00=G(0y0) is a factor of G ⁡ ( x) G(x) and so 1 ​ y ​ 1 1y1 is a factor of x x. Both 0 ​ y ​ 0 0y0 and 1 ​ y ​ 1 1y1 are factors of x x so x x is unbalanced. This shows that if x x is Sturmian then G ⁡ ( x) G(x) is balanced, and it is not hard to see that its slope is irrational, so G ⁡ ( x) G(x) is Sturmian.

Conversely, if G ⁡ ( x) G(x) is Sturmian, then x x is Sturmian. Indeed, suppose that x x is unbalanced, namely let w w be a palindrome such that both 0 ​ w ​ 0 0w0 and 1 ​ w ​ 1 1w1 are factors of x x. Then both 0 ​ G ​ ( w) ​ 0 0G(w)0 and 01 ​ G ​ ( w) ​ 01 01G(w)01 are factors of G ⁡ ( x) G(x). In view of G G, 0 ​ G ​ ( w) ​ 00 0G(w)00 is a prefix of G ⁡ ( 0 ​ w ​ 0 ​ a) G(0w0a) for any letter a a, so that both 0 ​ G ​ ( w) ​ 00 0G(w)00 and 1 ​ G ​ ( w) ​ 01 1G(w)01 are factors of G ⁡ ( x) G(x), showing at once that G ⁡ ( x) G(x) is unbalanced. It is clear from the slopes that if G ⁡ ( x) G(x) is not ultimately periodic, then x x is also not ultimately periodic.

Let m m be the greatest m ≥ 1 m\geq 1 such that 0 m ​ 1 0^{m}1 is a factor of c α c_{\alpha}. Suppose m ≥ 2 m\geq 2, by the balanced property, the words 10 k ​ 1 10^{k}1 for k = 0 ​ … ​ m − 2 k=0\ldots m-2 cannot be factors of c α c_{\alpha}, and we see that 10 m − 1 ​ 1 10^{m-1}1 must be a factor of c α c_{\alpha} for otherwise c α c_{\alpha} would be ultimately periodic. If m = 1 m=1, then we easily see that 11 11 must be a factor of c α c_{\alpha}. So the word 0 m − 1 ​ 1 0^{m-1}1 is left special and hence a prefix of c α c_{\alpha}. All this sums up to the fact that c α c_{\alpha} can be factorised in an infinite concatenation of the two words 0 m − 1 ​ 1 0^{m-1}1 and 0 m − 1 ​ 10 0^{m-1}10 for some m ≥ 1 m\geq 1.

We define the morphisms, for m, n ≥ 1 m,n\geq 1:

θ m = G m − 1 ∘ E ∘ G \theta_{m}=G^{m-1}\circ E\circ G and h n = θ a 1 ∘ θ a 2 ∘ ⋯ ∘ θ a n h_{n}=\theta_{a_{1}}\circ\theta_{a_{2}}\circ\cdots\circ\theta_{a_{n}}.

Since θ m ​ ( 0) = 0 m − 1 ​ 1 \theta_{m}(0)=0^{m-1}1 and θ m ​ ( 1) = 0 m − 1 ​ 10 \theta_{m}(1)=0^{m-1}10, we have seen that c α c_{\alpha} factorises as c α = θ m ​ ( x) c_{\alpha}=\theta_{m}(x) for some x x, that must be Sturmian. For m ≥ 1 m\geq 1, we have θ m ​ ( 0 ​ c α) = 0 m − 1 ​ 1 ​ θ m ​ ( c α) \theta_{m}(0c_{\alpha})=0^{m-1}1\theta_{m}(c_{\alpha}) and θ m ​ ( 1 ​ c α) = 0 m − 1 ​ 10 ​ θ m ​ ( c α) \theta_{m}(1c_{\alpha})=0^{m-1}10\theta_{m}(c_{\alpha}) so that θ m ​ ( c α) \theta_{m}(c_{\alpha}) is caracteristic and, according to the slopes, we have

θ m ​ ( c α) = c 1 m + α \theta_{m}(c_{\alpha})=\displaystyle c_{\frac{1}{m+\alpha}}.

so that for all n ≥ 1 n\geq 1 we have :

h n ​ ( c [0; a n + 1, a n + 2, …]) = c α \displaystyle h_{n}(c_{[0;a_{n+1},a_{n+2},\ldots]})=c_{\alpha}.

Moreover, we have h n ​ ( 0) = s n h_{n}(0)=s_{n} and h n ​ ( 1) = s n ​ s n − 1 h_{n}(1)=s_{n}s_{n-1} as it is easily checked by induction on n ≥ 1 n\geq 1. This shows that s n s_{n} is a prefix of c α c_{\alpha} for all n ≥ 1 n\geq 1, proving the theorem. ∎

### 1.4 Standard and central words

###### Definition 6.

The subset of ( A ∗) 2 (A^{*})^{2} of standard pairs is recursively defined by the rules :

- •

( 0, 1) (0,1) is a standard pair,

- •

if ( u, v) (u,v) is a standard pair, then ( v ​ u, v) (vu,v) and ( u, u ​ v) (u,uv) are standard pairs.

We recall the notation x − x^{-} for a word x x deprived of its last letter. If x x is empty, then we set x − x^{-} to be the empty word.

###### Proposition 3.

Let ( u, v) (u,v) be a standard pair.

1. 1)

( u ​ v) − ⁣ − = ( v ​ u) − ⁣ − (uv)^{--}=(vu)^{--},

2. 2)

if | u | ≥ 2 |u|\geq 2, u u ends with 10 10. If | v | ≥ 2 |v|\geq 2, u u ends with 01 01

3. 3)

u − ⁣ − u^{--} and v − ⁣ − v^{--} are palindromes.

4. 4)

We have | u | ​ | v | 1 − | u | 1 | ​ v | = 1 |u||v|_{1}-|u|_{1}|v|=1.

The proofs of proposition 3 3 are straightforward inductions.

###### Definition 7.

A word is said to be standard if it is a coponent of a central pair.

###### Proposition 4.

1. 1.

If u u is standard, then u − ⁣ − u^{--} is palindromic.

2. 2.

A standard word is primitive (that is, not a non-trivial power of a word).

3. 3.

The words ( s n) (s_{n}) in theorem 4 are standard. The suffix of length 2 2 of s n s_{n} is t n t_{n}, where t n = 10 t_{n}=10 if n n is even, and t n = 01 t_{n}=01 if n n is odd, for n ≥ 2 n\geq 2.

###### Proof.

1) The fact that u − ⁣ − u^{--} is palindromic is trivial from proposition 3 3.

2)The word u u is primitive since by proposition OPEN 3 − 4) 3-4), | u | |u| and | u | 1 |u|_{1} are coprime.

3) We see by the definition of the sequence ( s n) (s_{n}) that ( s 2 ​ n, s 2 ​ n − 1) (s_{2n},s_{2n-1}) and ( s 2 ​ n, s 2 ​ n + 1) (s_{2n},s_{2n+1}) are standard pairs for all n ≥ 0 n\geq 0. The remaining part of the assertion is clear by proposition 3 3. ∎

###### Definition 8.

We define the set of central words by one of the following equivalent definitions :

1. (i)

a word w w is central if and only if there exists a standard word u u such that w = u − ⁣ − w=u^{--},

2. (ii)

the set of central words is inductively defined as follows :

  - •

powers of a letter are central words

  - •

if p p and q q are central, and p ​ 01 ​ q p01q is a palindrome, then p ​ 01 ​ q p01q is central

3. (iii)

a word w w is central if and only if it is a power of a letter, or a palindrome of the form p ​ 01 ​ q p01q with p p, q q palindromes,

4. (iv)

a word is central if and only if it is a prefix palindrome of a caracteristic word.

The decomposition w = p ​ 01 ​ q w=p01q with p p, q q palindrome of a central word that is not a power of a letter is then unique.

###### Proof.

( i ​ i) (ii) -central ⇔ \Leftrightarrow ( i ​ i ​ i) (iii) -central : It is clear from the definition ( i ​ i) (ii) that ( i ​ i) (ii) -central words are palindromes, so that ( i ​ i) (ii) -central ⇒ \Rightarrow ( i ​ i ​ i) (iii) -central. For the converse, it is sufficient to show that if w = p ​ 01 ​ q w=p01q is a palindrome with p p and q q palindrome is ( i ​ i ​ i) (iii) -central, then p p and q q are ( i ​ i ​ i) (iii) -central. We cannot have | p | = | q | |p|=|q| since w w is a palindrome, and we can assume that | p | ≤ | q | − 1 |p|\leq|q|-1. If | p | = | q | − 1 |p|=|q|-1 then q = p ​ 0 = 0 ​ p q=p0=0p and p p, q q are powers of letters. If | p | = | q | − 2 |p|=|q|-2 then q = p ​ 01 ​ u q=p01u and since w = p ​ 01 ​ u ~ ​ 10 ​ p w=p01\tilde{u}10p is a palindrome, u u is a palindrome and q q is ( i ​ i ​ i) (iii) -central. By continuing this argument with q q in the place of w w, we see that there exists a unique N ≥ 1 N\geq 1 such that q = ( p ​ 01) N ​ t q=(p01)^{N}t with | t | ≤ | p | − 1 |t|\leq|p|-1, so that p ​ 01 ​ t p01t is ( i ​ i ​ i) (iii) -central with | t | ≤ | p | − 1 |t|\leq|p|-1, and in this situation we have seen that p p is ( i ​ i ​ i) (iii) -central.

( i ​ i) (ii) -central ⇒ \Rightarrow ( i) (i) -central : The case of powers of letters being obvious, we show by induction on | w | |w| that if w = p ​ 01 ​ q w=p01q with p p, q q and w w ( i ​ i) (ii) -central, then ( q ​ 10, p ​ 01) (q10,p01) is a standard pair. We can assume | p | ≤ | q | |p|\leq|q| without loss of generality. If | p | = | q | − 1 |p|=|q|-1, then p ​ 0 = q = 0 ​ p = 0 | q | p0=q=0p=0^{|q|} and ( 0 | q | ​ 10, 0 | q | ​ 1) (0^{|q|}10,0^{|q|}1) is a standard pair. If | p | ≤ | q | − 2 |p|\leq|q|-2, then q = p ​ 01 ​ u q=p01u for some palindrome u u. Since q q is ( i ​ i) (ii) -central, it is ( i ​ i ​ i) (iii) -central and from the preceeding proof we know that u u is ( i ​ i ​ i) (iii) -central, and so u u is ( i ​ i) (ii) -central. By the induction hypothesis, ( u ​ 10, p ​ 01) (u10,p01) is a standard pair, and so is ( p ​ 01 ​ u ​ 10, p ​ 01) = ( q ​ 10, p ​ 01) (p01u10,p01)=(q10,p01). Since ( q ​ 10, p ​ 01) (q10,p01) is a standard pair, ( p ​ 01 ​ q ​ 10, p ​ 01) (p01q10,p01) is also and w = ( p ​ 01 ​ q ​ 10) − ⁣ − w=(p01q10)^{--} is ( i) (i) -central.

( i) (i) -central ⇒ \Rightarrow ( i ​ i ​ i) (iii) -central : Let w = u − ⁣ − w=u^{--} with ( u, v) (u,v) a standard pair. Write u = w ​ 01 = y ​ x u=w01=yx for a standard pair ( x, y) (x,y), x = q ​ 10 x=q10 and y = p ​ 01 y=p01, with p p and q q palindromes. Then w = p ​ 01 ​ q w=p01q and w w is ( i ​ i ​ i) (iii) -central.

( i) (i) -central ⇒ \Rightarrow ( i ​ v) (iv) -central : We know that a ( i) (i) -central word is a palindrome. Let Γ: ( u, v) ∈ ( A ∗) 2 ↦ ( u, u ​ v) ∈ ( A ∗) 2 \Gamma:(u,v)\in(A^{*})^{2}\mapsto(u,uv)\in(A^{*})^{2} and Δ: ( u, v) ∈ ( A ∗) 2 ↦ ( v ​ u, v) ∈ ( A ∗) 2 \Delta:(u,v)\in(A^{*})^{2}\mapsto(vu,v)\in(A^{*})^{2}. Let w = u − ⁣ − w=u^{--} with ( u, v) = Γ a k ∘ Δ a k − 1 ∘ ⋯ ∘ Δ a 2 ∘ Γ a 1 − 1 ( 0, 1) (u,v)=\Gamma^{a_{k}}\circ\Delta^{a_{k-1}}\circ\cdots\circ\Delta^{a_{2}}\circ\Gamma^{a_{1}-1}(0,1), with a i ∈ ℕ ∗ a_{i}\in\mathbb{N}^{*} for i = 1 ​ … ​ k i=1\ldots k. Then w = s k − ⁣ − w=s_{k}^{--} for any caracteristic word having slope whose partial quotients begins with a 1, a 2, …, a k a_{1},a_{2},\ldots,a_{k}, with the sequence ( s n) (s_{n}) defined as in theorem 4, so that w w is ( i ​ v) (iv) -central. The case where w = v − ⁣ − w=v^{--} with ( u, v) (u,v) standard is similar.

( i ​ v) (iv) -central ⇒ \Rightarrow ( i ​ i ​ i) (iii) -central : In view of the preceeding proof, any ( i ​ v) (iv) -central word is a prefix of a ( i) (i) -central word, and so a prefix of a ( i ​ i ​ i) (iii) -central word. Let w w be a palindrome prefix of a palindrome p ​ 01 ​ q p01q with p p and q q palindromes. We may assume | p | ≤ | q | |p|\leq|q| and by induction on | p ​ 01 ​ q | |p01q| we may assume | w | > | q | |w|>|q| since otherwise w w is a prefix of the ( i ​ i ​ i) (iii) -central word q q. If | w | = | q | + 1 |w|=|q|+1 then w = q ​ 1 = 1 ​ q w=q1=1q and w w is a power of a letter. If | w | ≥ | q | + 2 |w|\geq|q|+2 then write w = q ​ 10 ​ t w=q10t, and since w w is a prefix of q ​ 10 ​ p q10p, t t is a prefix of p p, and so is also a prefix of q q. The word t t is a suffix and a prefix of the palindromic word w w, and so is palindromic, and w = q ​ 10 ​ t w=q10t with q q and t t palindromes, as required.

Unicity of decomposition : Let w = p ​ 01 ​ q = s ​ 01 ​ t = u − ⁣ − w=p01q=s01t=u^{--} be a central word, with p p, q q, s s and t t palindrome and u ​ 10 u10 standard, and assume that | s | > | p | |s|>|p|. We cannot have | s | = | p | + 1 |s|=|p|+1, so write s = p ​ 01 ​ λ s=p01\lambda and see that q = λ ​ 01 ​ t q=\lambda 01t so that u = w ​ 10 = q ​ 10 ​ p ​ 10 = λ ​ 01 ​ t ​ 10 ​ p ​ 10 = t ​ 10 ​ s ​ 10 = t ​ 10 ​ p ​ 01 ​ λ ​ 10 u=w10=q10p10=\lambda 01t10p10=t10s10=t10p01\lambda 10, and the two words λ ​ 01 \lambda 01 and t ​ 10 ​ p ​ 10 t10p10 commute. The primitive word u u is a product of two non-empty commuting words, hence a contradiction.

∎

## 2 Repetition function and Rauzy graphs of Sturmian words

We recall the following notations. The dynamical map T T is the shift, which removes the first letter of an infinite word. For any word x x and integer n ≥ 1 n\geq 1, we note ℙ n ​ ( x) \mathbb{P}_{n}(x) the prefix of length n n of x x.

### 2.1 Definitions

In [8] a new complexity function is introduced, also called the repetition function. We define here a similar function and still call it the repetition function, since the two are linked by a simple formula. Namely, if r 0 ​ ( x, n) r_{0}(x,n) is Bugeaud and Kim’s repetition function, then we have r 0 ​ ( x, n) = n + r ⁡ ( x, n) r_{0}(x,n)=n+r(x,n).

###### Definition 9 (Repetition function).

Let x x be an infinite word over a finite alphabet A A. We define, for an integer m > 0 m>0:

r ( x, m) = max { k ∈ ℕ | ℙ m ( x), ℙ m ( T ( x)), …, ℙ m ( T k − 1 ( x)) are all distincts } r(x,m)=\max\{k\in\mathbb{N}\ |\ \mathbb{P}_{m}(x),\mathbb{P}_{m}(T(x)),\ldots,\mathbb{P}_{m}(T^{k-1}(x))\text{ are all distincts }\}.

The function r ⁡ ( x, ⋅) r(x,\cdot) is called the repetition function of x x.

###### Proposition 5.

Let x x be an infinite word.

- •

∀ m > 0 \forall m>0, r ⁡ ( x, m) ≤ p ⁡ ( x, m) r(x,m)\leq p(x,m).

- •

if x x is Sturmian we have ∀ m > 0 \forall m>0, r ⁡ ( x, m) ≤ m + 1 r(x,m)\leq m+1

###### Definition 10 (Rauzy graph).

Let x x be an infinite word over an alphabet A A. For every integer m > 0 m>0, we define the factor graph, or Rauzy graph, of x x of degree m m as the directed graph having :

- •

vertexes as the factors of x x of length m m

- •

an arrow s → t s\rightarrow t if and only if there exists a factor r r of x x of length m + 1 m+1 such that s s is a prefix of r r and t t a suffix of r r.

Given a path s 1 → s 2 → … → s k s_{1}\rightarrow s_{2}\rightarrow\ldots\rightarrow s_{k} in this graph, we set k − 1 k-1 to be its length. The path defined by x x in G m G_{m} is the infinite path

ℙ m ​ ( x) → ℙ m ​ ( T ⁡ ( x)) → … → ℙ m ​ ( T k ​ ( x)) → … \mathbb{P}_{m}(x)\rightarrow\mathbb{P}_{m}(T(x))\rightarrow\ldots\rightarrow\mathbb{P}_{m}(T^{k}(x))\rightarrow\ldots.

For a Sturmian word x x and m > 0 m>0, G m G_{m} has m + 1 m+1 vertexes. The vertex L m L_{m} has in-degree 2 2 and the vertex R m R_{m} has out-degree 2 2 (notice that they may be equal). Every vertex that is neither L m L_{m} nor R m R_{m} has in-degree 1 1 and out-degree 1 1. Therefore, G m G_{m} is the fusion of two cycles, sharing a common path. The following proposition explains how to read the repetition function on the factor graph of x x. A Hamiltonian path in a directed graph is a path that does not visit a vertex more that twice.

###### Proposition 6.

Let x x be a Sturmian word, m > 0 m>0 and G m G_{m} its Rauzy graph of degree m m. Then r ⁡ ( x, m) r(x,m) is the length of the longest Hamiltonian finite path

ℙ m ​ ( x) → ℙ m ​ ( T ⁡ ( x)) → … → ℙ m ​ ( T k − 1 ​ ( x)) \mathbb{P}_{m}(x)\rightarrow\mathbb{P}_{m}(T(x))\rightarrow\ldots\rightarrow\mathbb{P}_{m}(T^{k-1}(x)).

in the infinite path defined by x x.

### 2.2 Repetition function of caracteristic words

###### Theorem 5.

Let x x be a Sturmian word and m ≥ 2 m\geq 2. The following statements are equivalents :

1. i)

r ⁡ ( x, m) = m + 1 r(x,m)=m+1

2. ii)

r ⁡ ( x, m) ≠ r ⁡ ( x, m − 1) r(x,m)\neq r(x,m-1)

###### Proof.

The implication ( i) ⇒ ( i) (i)\Rightarrow(i) is clear since r ⁡ ( x, m − 1) ≤ m r(x,m-1)\leq m. For the converse, let A m A_{m} and B m B_{m} be the two distinct vertexes of G m G_{m} such that

R m → A m R_{m}\rightarrow A_{m} and R m → B m R_{m}\rightarrow B_{m}.

Consider the path

ℙ m − 1 ​ ( x) → ℙ m − 1 ​ ( T ⁡ ( x)) → … → ℙ m − 1 ​ ( T r ⁡ ( x, m − 1) ​ ( x)) \mathbb{P}_{m-1}(x)\rightarrow\mathbb{P}_{m-1}(T(x))\rightarrow\ldots\rightarrow\mathbb{P}_{m-1}(T^{r(x,m-1)}(x)).

in G m − 1 G_{m-1}. There exists a unique integer 0 ≤ j < r ⁡ ( x, m − 1) 0\leq j<r(x,m-1) such that ℙ m − 1 ​ ( T r ⁡ ( x, m − 1) ​ ( x)) = ℙ m − 1 ​ ( T j ​ ( x)) \mathbb{P}_{m-1}(T^{r(x,m-1)}(x))=\mathbb{P}_{m-1}(T^{j}(x)). In G m G_{m}, we cannot have ℙ m ​ ( T r ⁡ ( x, m − 1) ​ ( x)) = ℙ m ​ ( T j ​ ( x)) \mathbb{P}_{m}(T^{r(x,m-1)}(x))=\mathbb{P}_{m}(T^{j}(x)) because this would imply r ⁡ ( x, m) = r ⁡ ( x, m − 1) r(x,m)=r(x,m-1), which by assumption is not the case. We then have ℙ m ​ ( T r ⁡ ( x, m − 1) ​ ( x)) ≠ ℙ m ​ ( T j ​ ( x)) \mathbb{P}_{m}(T^{r(x,m-1)}(x))\neq\mathbb{P}_{m}(T^{j}(x)) and these two words differ only by their last letters. This shows that

{ A m, B m } = { ℙ m ​ ( T r ⁡ ( x, m − 1) ​ ( x)), ℙ m ​ ( T j ​ ( x)) } \{A_{m},B_{m}\}=\{\mathbb{P}_{m}(T^{r(x,m-1)}(x)),\mathbb{P}_{m}(T^{j}(x))\}

so that the path

ℙ m ​ ( x) → ℙ m ​ ( T ⁡ ( x)) → … → ℙ m ​ ( T r ⁡ ( x, m) − 1 ​ ( x)) \mathbb{P}_{m}(x)\rightarrow\mathbb{P}_{m}(T(x))\rightarrow\ldots\rightarrow\mathbb{P}_{m}(T^{r(x,m)-1}(x)).

passes on the two vertexes A m A_{m} and B m B_{m}. This path is the longest Hamiltonian path that starts at ℙ m ​ ( x) \mathbb{P}_{m}(x) in the path defined by x x, so we can see that it must pass by all the m + 1 m+1 vertexes of G m G_{m}. This shows that r ⁡ ( x, m) = m + 1 r(x,m)=m+1. ∎

###### Lemma 2.

Let c α c_{\alpha} be a caracteristic Sturmian word. Then we have

ℙ m ​ ( T r ⁡ ( c α, m) ​ ( c α)) = ℙ m ​ ( c α) = L m \mathbb{P}_{m}(T^{r(c_{\alpha},m)}(c_{\alpha}))=\mathbb{P}_{m}(c_{\alpha})=L_{m}

for all m > 0 m>0.

###### Proof.

The second equality comes from the definition of c α c_{\alpha}. Let 0 ≤ j < r ⁡ ( c α, m) 0\leq j<r(c_{\alpha},m) be the only integer such that ℙ m ​ ( T r ⁡ ( c α, m) ​ ( c α)) = ℙ m ​ ( T j ​ ( c α)) \mathbb{P}_{m}(T^{r(c_{\alpha},m)}(c_{\alpha}))=\mathbb{P}_{m}(T^{j}(c_{\alpha})) and assume j ≠ 0 j\neq 0. Then ℙ m ​ ( T r ⁡ ( c α, m) − 1 ​ ( x)) ≠ ℙ m ​ ( T j − 1 ​ ( c α)) \mathbb{P}_{m}(T^{r(c_{\alpha},m)-1}(x))\neq\mathbb{P}_{m}(T^{j-1}(c_{\alpha})) and these two words differ only by their first letters. This shows that ℙ m ​ ( T j ​ ( c α)) \mathbb{P}_{m}(T^{j}(c_{\alpha})) is left special, so that j = 0 j=0 and this is a contradiction. ∎

We define r ⁡ ( z, m) r(z,m) for a finite word z z and m > 0 m>0, provided z z admits a factor of length m m that occurs at least twice, as r ⁡ ( x, m) r(x,m) for any infinite word x x such that z z is a prefix of x x.

###### Lemma 3.

Let z = p ​ 01 ​ q z=p01q be a central word with | p | ≤ | q | |p|\leq|q|. Then

r ⁡ ( z, | p | + 1) = | p | + 2 r(z,|p|+1)=|p|+2.

###### Proof.

Let c α c_{\alpha} be a caracteristic word having z z as a prefix. Then by the preceeding lemma we have ℙ | p | + 1 ​ ( T r ⁡ ( z, | p | + 1) ​ ( c α)) = p ​ 0 \mathbb{P}_{|p|+1}(T^{r(z,|p|+1)}(c_{\alpha}))=p0

We prove the result by induction on | z | |z|. Since | z | |z| is palindromic we cannot have | p | = | q | |p|=|q| and if | p | = | q | − 1 |p|=|q|-1 then q = p ​ 0 = 0 ​ p q=p0=0p so z = 0 | p | + 1 ​ 10 | p | + 1 z=0^{|p|+1}10^{|p|+1} and the result is clear. Assume that | p | ≤ | q | − 2 |p|\leq|q|-2 and write q = p ​ 01 ​ u q=p01u, u u is palindromic since z = q ​ 10 ​ p = p ​ 01 ​ u ​ 10 ​ p z=q10p=p01u10p is palindromic so that q = p ​ 01 ​ u q=p01u is the decomposition of q q as a central word.

If | p | ≤ | u | |p|\leq|u| then we are done by induction. Assume that | u | ≤ | p | |u|\leq|p| so that r ⁡ ( z, | u | + 1) = r ⁡ ( q, | u | + 1) = | u | + 2 r(z,|u|+1)=r(q,|u|+1)=|u|+2 by induction. Since r ⁡ ( z, | u | + 1) ≤ r ⁡ ( z, | p |) ≤ | u | + 2 r(z,|u|+1)\leq r(z,|p|)\leq|u|+2 we have r ⁡ ( z, | p |) = | u | + 2 r(z,|p|)=|u|+2. But z = u ​ 10 ​ p ​ 10 ​ p z=u10p10p so that u ​ 10 ​ p ​ 0 u10p0 is not a prefix of z z and we must have r ⁡ ( z, | p | + 1) > r ⁡ ( z, | u | + 1) = | u | + 2 = r ⁡ ( z, | p |) r(z,|p|+1)>r(z,|u|+1)=|u|+2=r(z,|p|), and hence ( z, | p | + 1) ≠ r ⁡ ( z, | p |) (z,|p|+1)\neq r(z,|p|). By theorem 5, we have r ⁡ ( z, | p | + 1) = | p | + 2 r(z,|p|+1)=|p|+2. ∎

###### Corollary 1.

Let c α c_{\alpha} be the caracteristic Sturmian word of slope α \alpha, and let ( q n) (q_{n}) be the sequence of continuant of α \alpha. Then for all n ≥ 0 n\geq 0 we have

r ⁡ ( c α) = q n r(c_{\alpha})=q_{n} for all q n − 1 ≤ m ≤ q n + 1 − 2 q_{n}-1\leq m\leq q_{n+1}-2. ( m ≠ 0) (m\neq 0)

###### Proof.

Let ( s n) (s_{n}) be the sequence associated to α \alpha defined as in theorem 4 4, so that c α = lim s n c_{\alpha}=\lim s_{n}. It is easily checked that | s n | = q n |s_{n}|=q_{n} for n ≥ 0 n\geq 0. We have

c α = lim s n + 2 = lim s n + 1 ​ s n = lim s n + 1 ​ s n − ⁣ − = lim s n − ⁣ − ​ t n ​ s n + 1 − ⁣ − c_{\alpha}=\lim s_{n+2}=\lim s_{n+1}s_{n}=\lim s_{n+1}s_{n}^{--}=\lim s_{n}^{--}t_{n}s_{n+1}^{--}

where t n = 10 t_{n}=10 if n ≥ 2 n\geq 2 is even and t n = 01 t_{n}=01 if n ≥ 2 n\geq 2 is odd. The words s n − ⁣ − ​ t n ​ s n + 1 − ⁣ − s_{n}^{--}t_{n}s_{n+1}^{--} are the central prefixes of c α c_{\alpha} and we have r ⁡ ( c α, | s n − ⁣ − | + 1) = | s n − ⁣ − | + 2 = | s n | r(c_{\alpha},|s_{n}^{--}|+1)=|s_{n}^{--}|+2=|s_{n}| and since r ⁡ ( c α, | s n + 1 − ⁣ − |) ≤ | s n | r(c_{\alpha},|s_{n+1}^{--}|)\leq|s_{n}|, we have

r ⁡ ( c α, m) = | s n | = q n r(c_{\alpha},m)=|s_{n}|=q_{n}

for n ≥ 2 n\geq 2 and q n − 1 ≤ m ≤ q n + 1 − 2 q_{n}-1\leq m\leq q_{n+1}-2.

If a 1 ≥ 3 a_{1}\geq 3, then it is easily checked that the formula still holds for 1 ≤ m ≤ q 2 − 2 1\leq m\leq q_{2}-2. If a 1 = 2 a_{1}=2, or a 1 = 1 a_{1}=1 and a 2 ≥ 2 a_{2}\geq 2, then the formulas hold but the set of integer m m such that 1 ≤ m ≤ q 1 − 2 1\leq m\leq q_{1}-2 is empty. If a 1 = 1 a_{1}=1 and a 2 = 2 a_{2}=2 then the formulas hold, but the sets of integers m m such that 1 ≤ m ≤ q 1 − 2 1\leq m\leq q_{1}-2 or q 1 − 1 ≤ m ≤ q 2 − 2 q_{1}-1\leq m\leq q_{2}-2 are empty. ∎

### 2.3 Rauzy graph of Sturmian words

Let x x be a Sturmian word of slope α \alpha whose sequence of continuant is ( q n) (q_{n}).

Notations :

- •

In the remaining part of the article, we make the abuse of notation of noting [a, b] [a,b] the integer interval of integers m m such that a ≤ m ≤ b a\leq m\leq b.

- •

We define the integer intervals I n I_{n}, for n ≥ 0 n\geq 0,

I n = [q n − 1, q n + 1 − 2] I_{n}=[q_{n}-1,q_{n+1}-2]

I n 0 = [q n − 1, q n + q n − 1 − 2] I_{n}^{0}=[q_{n}-1,q_{n}+q_{n-1}-2]

and for 1 ≤ l ≤ a n + 1 − 1 1\leq l\leq a_{n+1}-1,

I n l = [l ​ q n + q n − 1 − 1, ( l + 1) ​ q n + q n − 1 − 2] I_{n}^{l}=[lq_{n}+q_{n-1}-1,(l+1)q_{n}+q_{n-1}-2].

If a 1 = 1 a_{1}=1 or a 1 = 2 a_{1}=2 then I 0 I_{0} is empty. If a 1 = 1 a_{1}=1 and a 2 = 1 a_{2}=1, then both I 0 I_{0} and I 1 I_{1} are empty.

- •

An Eulerian path in a directed graph is a path that does not pass twice on the same arrow. A cycle in a directed graph is an Eulerian path s 1 → s 2 → … → s k s_{1}\rightarrow s_{2}\rightarrow\ldots\rightarrow s_{k} such that s 1 = s k s_{1}=s_{k} and we set k k to be its length.

We recall the notation u ∗ u^{*} for a finite word u u, denoting the suffix of length | u | − 1 |u|-1 of u u, which is u u deprived of its first letter.

###### Proposition 7.

Let m ∈ I n l m\in I_{n}^{l} for n ≥ 0 n\geq 0 and 1 ≤ l ≤ a n + 1 − 1 1\leq l\leq a_{n+1}-1, then :

1. 1.

one of the two cycles of G m G_{m} is of length q n q_{n}. It is called the referent cycle.

2. 2.

the other cycle is of length l ​ q n + q n − 1 lq_{n}+q_{n-1}.

3. 3.

The arrow R m → R m ∗ ​ t n − 1 − R_{m}\rightarrow R_{m}^{*}t_{n-1}^{-} belongs to the referent cycle, and the arrow R m → R m ∗ ​ t n − R_{m}\rightarrow R_{m}^{*}t_{n}^{-} belongs to the non-referent cycle. These two arrows do not belong to the same cycle.

###### Proof.

1) Since two infinite words sharing the same set of factors also share the same Rauzy graphs, we can reduce to the case x = c α x=c_{\alpha}. Since r ⁡ ( c α, m) = q n r(c_{\alpha},m)=q_{n} by Corollary 2 2, by definition of the repetition function the path

ℙ m ​ ( c α) → ℙ m ​ ( T ⁡ ( c α)) → … → ℙ m ​ ( T r ⁡ ( c α, m) ​ ( c α)) \mathbb{P}_{m}(c_{\alpha})\rightarrow\mathbb{P}_{m}(T(c_{\alpha}))\rightarrow\ldots\rightarrow\mathbb{P}_{m}(T^{r(c_{\alpha},m)}(c_{\alpha}))

defines a cycle of length q n q_{n}.

2) The common part of the two cycles is the shortest path that starts at the vertex L m L_{m} and ends at the vertex R m R_{m}. The finite word w w defined by this path is left and right special, so it is the shortest central word of length | w | ≥ m |w|\geq m, and this length is equal to ( l + 1) ​ q n + q n − 1 − 2 (l+1)q_{n}+q_{n-1}-2 and has ( l + 1) ​ q n + q n − 1 − 1 (l+1)q_{n}+q_{n-1}-1 vertexes. The path so defined is of length ( l + 1) ​ q n + q n − 1 − 2 − m (l+1)q_{n}+q_{n-1}-2-m. Since the sum of the length of the two cycles equals the sum of the number of vertexes of G m G_{m} and the number of vertexes in the common part, we get that the other cycle is of length μ \mu where

q n + μ = m + 1 + ( l + 1) ​ q n + q n − 1 − 1 − m q_{n}+\mu=m+1+(l+1)q_{n}+q_{n-1}-1-m

so that μ = l ​ q n + q n − 1 \mu=lq_{n}+q_{n-1}.

Since q n q_{n} and l ​ q n + q n − 1 lq_{n}+q_{n-1} are coprime, the referent cycle is well-determined by its length.

3) The common path L m → … → R m L_{m}\rightarrow\ldots\rightarrow R_{m} corresponds to the central word of length ( l + 1) ​ q n + q n − 1 − 2 (l+1)q_{n}+q_{n-1}-2, namely s n l + 1 ​ s n − 1 − ⁣ − s_{n}^{l+1}s_{n-1}^{--}. The referent cycle is the cycle

ℙ m ​ ( c α) → ℙ m ​ ( T ⁡ ( c α)) → … → ℙ m ​ ( T r ⁡ ( c α, m) ​ ( c α)) \mathbb{P}_{m}(c_{\alpha})\rightarrow\mathbb{P}_{m}(T(c_{\alpha}))\rightarrow\ldots\rightarrow\mathbb{P}_{m}(T^{r(c_{\alpha},m)}(c_{\alpha}))

so we only have to see that s n l + 1 ​ s n − 1 − s_{n}^{l+1}s_{n-1}^{-} is a prefix of c α c_{\alpha} since s n − 1 s_{n-1} ends with t n − 1 t_{n-1}. But this is obvious, s n − 1 s_{n-1} is a prefix of s n s_{n}, and s n + 1 = s n a n + 1 ​ s n − 1 s_{n+1}=s_{n}^{a_{n+1}}s_{n-1}, so that indeed the arrow R m → R m ∗ ​ t n − 1 − R_{m}\rightarrow R_{m}^{*}t_{n-1}^{-} belongs to the referent cycle. The fact that R m → R m ∗ ​ t n − R_{m}\rightarrow R_{m}^{*}t_{n}^{-} belongs to the non-referent cycle comes from the fact that s n l + 1 ​ s n − 1 − ⁣ − ​ t n s_{n}^{l+1}s_{n-1}^{--}t_{n} is not a prefix of c α c_{\alpha}. It is obvious that the two arrows leaving the right special factor R m R_{m} cannot be on the same cycle.

∎

###### Definition 11.

- •

We say x x turns around a cycle of length k k in G m G_{m} when r ⁡ ( x, m) = k r(x,m)=k and the path ℙ m ​ ( x) → ℙ m ​ ( T ⁡ ( x)) → … → ℙ m ​ ( T k ​ ( x)) \mathbb{P}_{m}(x)\rightarrow\mathbb{P}_{m}(T(x))\rightarrow\ldots\rightarrow\mathbb{P}_{m}(T^{k}(x)) shares the same arrow as this cycle.

- •

We say x x turns d d times around a cycle of length k k if for all i = 0 ​ … ​ d − 1 i=0\ldots d-1, T i ​ k ​ ( x) T^{ik}(x) turns around this cycle.

For a Sturmian word x x, since the two cycles of its Rauzy graph G m G_{m} have different length, x x turns around a cycle of length k k if and only if r ⁡ ( x, m) = k r(x,m)=k.

###### Theorem 6.

For m ∈ I n l m\in I_{n}^{l}, the caracteristic word c α c_{\alpha} turns around the referent cycle a n + 1 − l a_{n+1}-l times, and no more.

###### Proof.

We first consider the case where l = 0 l=0. Then the central word s n − ⁣ − s_{n}^{--} is a strict prefix of L m L_{m} and L m L_{m} is a strict prefix of the central word s n − ⁣ − ​ t n ​ s n − 1 − ⁣ − s_{n}^{--}t_{n}s_{n-1}^{--}. The word z = s n + 1 ​ s n − ⁣ − = s n a n + 1 + 1 ​ s n − 1 − ⁣ − z=s_{n+1}s_{n}^{--}=s_{n}^{a_{n+1}+1}s_{n-1}^{--} is central and so we have

r ⁡ ( z, m) = q n = r ⁡ ( T q n ​ ( z), m) = … = r ⁡ ( T ( a n + 1 − 1) ​ q n ​ ( c α), m) r(z,m)=q_{n}=r(T^{q_{n}}(z),m)=\ldots=r(T^{(a_{n+1}-1)q_{n}}(c_{\alpha}),m),

showing that c α c_{\alpha} turns at least a n + 1 a_{n+1} times around the referent cycle.

Since s n + 1 ​ s n s_{n+1}s_{n} is a prefix of c α c_{\alpha}, s n + 1 ​ s n = z ​ t n = s n a n + 1 + 1 ​ s n − 1 − ⁣ − ​ t n s_{n+1}s_{n}=zt_{n}=s_{n}^{a_{n+1}+1}s_{n-1}^{--}t_{n} is a prefix of c α c_{\alpha} and s n ​ s n − 1 − ⁣ − ​ t n s_{n}s_{n-1}^{--}t_{n} is a prefix of T a n + 1 ​ q n ​ ( c α) T^{a_{n+1}q_{n}}(c_{\alpha}) and from this we easily see that the word T a n + 1 ​ q n ​ ( c α) T^{a_{n+1}q_{n}}(c_{\alpha}) passes by the arrow R m → R m ∗ ​ t n − R_{m}\rightarrow R_{m}^{*}t_{n}^{-} before passing by the arrow R m → R m ∗ ​ t n − 1 − R_{m}\rightarrow R_{m}^{*}t_{n-1}^{-}. This shows that c α c_{\alpha} does not turn a n + 1 + 1 a_{n+1}+1 times around the referent cycle.

The case l > 0 l>0 is similar. ∎

###### Lemma 4.

Let x x be a Sturmian word of slope α \alpha, and let m > 0 m>0. Then x x does not turn twice around the non-referent cycle.

###### Proof.

Since the set of factors of a Sturmian word is stable under reversal, we see that if s → t s\rightarrow t is an arrow of G m G_{m}, then t ~ → s ~ \tilde{t}\rightarrow\tilde{s} is an arrow of G m G_{m}. Since the two cycles of G m G_{m} are of different length, we can derive from the fact that only one of the two arrows

R m → R m ∗ ​ t n − 1 − R_{m}\rightarrow R_{m}^{*}t_{n-1}^{-} and R m → R m ∗ ​ t n − R_{m}\rightarrow R_{m}^{*}t_{n}^{-}

belongs to the referent cycle the fact that only one of the two arrows

0 ​ L m − → L m 0L_{m}^{-}\rightarrow L_{m} and 1 ​ L m − → L m 1L_{m}^{-}\rightarrow L_{m}

belongs to the referent cycle. The two words 0 ​ c α 0c_{\alpha} and 1 ​ c α 1c_{\alpha} are Sturmian, and so there is a unique word u u of length q n q_{n} such that u ​ c α uc_{\alpha} is Sturmian and turns around the referent cycle. Since c α c_{\alpha} always turns at least once around the referent cycle, u ​ c α uc_{\alpha} turns twice around the referent cycle.

If there is a Sturmian word x x that turns twice around the non-referent cycle, wee see from the preceeding argument that the central word w w defined by the common part of G m G_{m} is such that the four word 0 ​ w ​ 0 0w0, 1 ​ w ​ 0 1w0, 0 ​ w ​ 1 0w1 and 1 ​ w ​ 1 1w1 are factors of x x. But this contradicts the balanced property of Sturmian words. ∎

## 3 Formal Intercepts of Sturmian words

We still consider a slope α \alpha with continuants ( q n) (q_{n}).

###### Proposition 8.

Let N = ∑ i = 0 k − 1 b i + 1 ​ q i \displaystyle N=\sum_{i=0}^{k-1}b_{i+1}q_{i} with b i ≥ 0 b_{i}\geq 0 for all i ≥ 2 i\geq 2 and n ≥ 1 n\geq 1. Then the following statements are equivalent :

1. i)

∀ l = 1 ​ … ​ k \forall l=1\ldots k, ∑ i = 0 l − 1 b i + 1 ​ q i < q l \displaystyle\sum_{i=0}^{l-1}b_{i+1}q_{i}<q_{l}

2. ii)

We have :

  - •

0 ≤ b 1 ≤ a 1 − 1 0\leq b_{1}\leq a_{1}-1

  - •

∀ i ≥ 1 \forall i\geq 1, 0 ≤ b i ≤ a i 0\leq b_{i}\leq a_{i}

  - •

∀ i ≥ 1 \forall i\geq 1, b i + 1 = a i + 1 ⇒ b i = 0 b_{i+1}=a_{i+1}\Rightarrow b_{i}=0

###### Proof.

OPEN OPEN i) ⇒ i ​ i) i)\Rightarrow ii): Since q 1 = a 1 q_{1}=a_{1}, the first line of OPEN i ​ i) ii) is easily checked. Let j ≥ 1 j\geq 1, then if b j > a j b_{j}>a_{j} we have b j ​ q j − 1 ​ ∑ i = 0 j − 1 b i + 1 ​ q i < q j = a j ​ q j − 1 + q j − 2 ≤ ( a j + 1) ​ q j − 1 b_{j}q_{j-1}\sum_{i=0}^{j-1}b_{i+1}q_{i}<q_{j}=a_{j}q_{j-1}+q_{j-2}\leq(a_{j}+1)q_{j-1} which is absurd. If b j + 1 = a j + 1 b_{j+1}=a_{j+1} then from ∑ i = 0 j b i + 1 ​ q i < q j + 1 = a j + 1 ​ q j + q j − 1 \sum_{i=0}^{j}b_{i+1}q_{i}<q_{j+1}=a_{j+1}q_{j}+q_{j-1} we get ∑ i = 0 j − 1 b i + 1 ​ q i < q j − 1 \sum_{i=0}^{j-1}b_{i+1}q_{i}<q_{j-1} which clearly implies b j = 0 b_{j}=0.

OPEN OPEN i ​ i) ⇒ i) ii)\Rightarrow i): The result is clear for l = 1 l=1 and we prove the result by induction on l l. Assume ∑ i = 0 l − 1 b i + 1 ​ q i < q l \sum_{i=0}^{l-1}b_{i+1}q_{i}<q_{l}. If b l + 1 < a l + 1 b_{l+1}<a_{l+1} then ∑ i = 0 l b i + 1 ​ q i < q l + b l + 1 ​ q l ≤ a l + 1 ​ q l < q l + 1 \sum_{i=0}^{l}b_{i+1}q_{i}<q_{l}+b_{l+1}q_{l}\leq a_{l+1}q_{l}<q_{l+1}. If b l + 1 = a l + 1 b_{l+1}=a_{l+1} then by assumption b l = 0 b_{l}=0 so that ∑ i = 0 l − 1 b i + 1 ​ q i < q l − 1 \sum_{i=0}^{l-1}b_{i+1}q_{i}<q_{l-1} and ∑ i = 0 l b i + 1 ​ q i < q l − 1 + a l + 1 ​ q l = q l + 1 \sum_{i=0}^{l}b_{i+1}q_{i}<q_{l-1}+a_{l+1}q_{l}=q_{l+1}. ∎

For a sequence ( b i) i ≥ 1 (b_{i})_{i\geq 1}, we call the conditions of Proposition 8 8 as the Ostrowski conditions.

###### Proposition 9.

Every integer N ∈ [0, q n [N\in[0,q_{n}[can be written uniquely in the form

N = ∑ i = 0 n − 1 b i + 1 ​ q i \displaystyle N=\sum_{i=0}^{n-1}b_{i+1}q_{i}

where the integers ( b i) (b_{i}) satisfy the Ostrowski conditions.

###### Proof.

We proceed by induction on N N. Write N = b n ​ q n − 1 + c N=b_{n}q_{n-1}+c with c ∈ [0, q n − 1 [c\in[0,q_{n-1}[. By induction, c c can be written uniquely in the form c = ∑ i = 0 n − 2 b i + 1 ​ q i c=\sum_{i=0}^{n-2}b_{i+1}q_{i} where the coefficient ( b i) i = 1 n − 1 (b_{i})_{i=1}^{n-1} satisfy the Ostrowski conditions. It is obvious that b n ≤ a n b_{n}\leq a_{n}. If b n = a n b_{n}=a_{n}, then we must have c < q n − 2 c<q_{n-2} and by induction on the unicity we must have b n − 1 = 0 b_{n-1}=0 so that the sequence ( b i) (b_{i}) indeed satisfy the Ostrowski conditions. ∎

###### Definition 12.

We define the set :

ℐ α = { ( k n) n > 0 ∈ ∏ n > 0 [0, q n [| ∀ n ≥ 0, k n = k n + 1*[mod*q n*]*} \displaystyle\mathcal{I}_{\alpha}=\left\{\left.(k_{n})_{n>0}\in\prod_{n>0}[0,q_{n}[\ \right|\ \forall n\geq 0,\ k_{n}=k_{n+1}\text{{\emph{[mod}} }q_{n}\text{{\emph{]}}}\right\}

of formal intercepts of the slope α \alpha.

###### Remark 1.

In view of proposition 8 and 9, if ρ = ( ρ n) n ≥ 0 \rho=(\rho_{n})_{n\geq 0} is a formal intercept, there is a unique sequence of integers ( b i) i ≥ 1 (b_{i})_{i\geq 1}, satisfying the Ostrowski conditions, such that

ρ n = ∑ i = 0 n − 1 b i + 1 ​ q i \displaystyle\rho_{n}=\sum_{i=0}^{n-1}b_{i+1}q_{i}

for all n ≥ 0 n\geq 0. In this case, we directly write :

ρ = ∑ i = 0 + ∞ b i + 1 ​ q i \displaystyle\rho=\sum_{i=0}^{+\infty}b_{i+1}q_{i}.

###### Remark 2.

For n > 0 n>0, we define :

Ψ n n + 1 \Psi_{n}^{n+1}: [0, q n + 1 [⟼ [0, q n [k ⟼ k ​ [mod q n] \begin{matrix}[0,q_{n+1}[&\longmapsto&[0,q_{n}[\\ k&\longmapsto&k${ [mod $q_{n}$]}$\\ \end{matrix}

and for integers m ≥ n > 0 m\geq n>0:

Ψ n m = Ψ n n + 1 ∘ Ψ n + 1 n + 2 ∘ ⋯ ∘ Ψ m − 1 m: [0, q m [→ [0, q n [\Psi_{n}^{m}=\Psi_{n}^{n+1}\circ\Psi_{n+1}^{n+2}\circ\cdots\circ\Psi_{m-1}^{m}\ :\ [0,q_{m}[\ \rightarrow[0,q_{n}[

then

ℐ α = lim ⟵ [0, q n [= { ( k n) n > 0 ∈ ∏ n > 0 [0, q n [| n ≤ m ⇒ Ψ n m ( k m) = k n } \displaystyle\mathcal{I}_{\alpha}=\lim_{\longleftarrow}[0,q_{n}[=\left\{\left.(k_{n})_{n>0}\in\prod_{n>0}[0,q_{n}[\ \right|\ n\leq m\Rightarrow\Psi_{n}^{m}(k_{m})=k_{n}\right\}

may be viewed as the projective limit of the sets [0, q n [[0,q_{n}[endowed with the functions Ψ n m \Psi_{n}^{m}.

###### Proposition 10.

Let ρ = ∑ i ≥ 0 b i + 1 ​ q i \rho=\sum_{i\geq 0}b_{i+1}q_{i} be a formal intercept of the slope α \alpha, and n ≥ 1 n\geq 1. Let λ n = q n + 1 + q n − ρ n + 1 − 2 \lambda_{n}=q_{n+1}+q_{n}-\rho_{n+1}-2, then

1. 1.

The words T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha}) and T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}) share the same prefix of length λ n \lambda_{n}.

2. 2.

If b n + 1 ≠ 0 b_{n+1}\neq 0, then λ n \lambda_{n} is the length of the longest common prefix of T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha}) and T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}),

3. 3.

the increasing sequence ( λ n) n ≥ 1 (\lambda_{n})_{n\geq 1} is unbounded.

###### Proof.

1) Let m = q n − 1 ∈ I n 0 m=q_{n}-1\in I_{n}^{0}. By theorem 6 6, the word T b n + 1 ​ q n ​ ( c α) T^{b_{n+1}q_{n}}(c_{\alpha}) turns a n + 1 − b n + 1 a_{n+1}-b_{n+1} times around the referent cycle, and then turns around the non-referent cycle. This shows that the words

T b n + 1 ​ q n ​ ( c α) T^{b_{n+1}q_{n}}(c_{\alpha}) and c α c_{\alpha}

share the same prefix of length

m + ( a n + 1 − b n + 1) ​ q n + r m+(a_{n+1}-b_{n+1})q_{n}+r

where r r is the length of the common part of the two cycles of G m G_{m}. Since m = q n − 1 m=q_{n}-1, every vertex of the non-referent cycle belongs to the referent cycle. This implies that r = q n − 1 − 1 r=q_{n-1}-1, and the two words T b n + 1 ​ q n ​ ( c α) T^{b_{n+1}q_{n}}(c_{\alpha}) and c α c_{\alpha} share the same prefix of length m + ( a n + 1 − b n + 1) ​ q n + r = q n − 1 + ( a n + 1 − b n + 1) ​ q n + q n − 1 − 1 m+(a_{n+1}-b_{n+1})q_{n}+r=q_{n}-1+(a_{n+1}-b_{n+1})q_{n}+q_{n-1}-1. This shows that the two words

T ρ n ​ ( T b n + 1 ​ q n ​ ( c α)) = T ρ n + 1 ​ ( c α) T^{\rho_{n}}(T^{b_{n+1}q_{n}}(c_{\alpha}))=T^{\rho_{n+1}}(c_{\alpha}) and T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha})

share the same prefix of length q n + ( a n + 1 − b n + 1) ​ q n + q n − 1 − 2 − ρ n = q n + 1 + q n − ρ n + 1 − 2 = λ n q_{n}+(a_{n+1}-b_{n+1})q_{n}+q_{n-1}-2-\rho_{n}=q_{n+1}+q_{n}-\rho_{n+1}-2=\lambda_{n}.

2) If b n + 1 ≠ 0 b_{n+1}\neq 0 then the longest common prefix of the words T b n + 1 ​ q n ​ ( c α) T^{b_{n+1}q_{n}}(c_{\alpha}) and c α c_{\alpha} has length q n − 1 + ( a n + 1 − b n + 1) ​ q n + q n − 1 − 1 q_{n}-1+(a_{n+1}-b_{n+1})q_{n}+q_{n-1}-1. So that the length of the longest common prefix of T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}) and T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha}) indeed equals λ n \lambda_{n}.

3) We have λ n + 1 − λ n = q n + 2 + q n + 1 − q n + 1 − q n − ( ρ n + 2 − ρ n + 1) = ( a n + 2 − b n + 2) ​ q n + 1 ≥ 0 \lambda_{n+1}-\lambda_{n}=q_{n+2}+q_{n+1}-q_{n+1}-q_{n}-(\rho_{n+2}-\rho_{n+1})=(a_{n+2}-b_{n+2})q_{n+1}\geq 0 so that the sequence ( λ n) (\lambda_{n}) is increasing. Since ρ n + 1 < q n + 1 \rho_{n+1}<q_{n+1}, we get :

λ n ≥ q n − 1 \lambda_{n}\geq q_{n}-1

and this shows that λ n → + ∞ \lambda_{n}\rightarrow+\infty when n → + ∞ n\rightarrow+\infty. ∎

###### Remark 3.

Notice that in the case where ρ n + 1 = q n + 1 − 1 \rho_{n+1}=q_{n+1}-1 then λ n = q n − 1 \lambda_{n}=q_{n}-1 and the lower bound for ( λ n) (\lambda_{n}) found in the proof of 𝑂𝑃𝐸𝑁 3) 3) is optimal. However, the sequence ( q n − 1) n ≥ 1 (q_{n}-1)_{n\geq 1} does not defines a formal intercept.

###### Definition 13.

Let ρ \rho be a formal intercept of the slope α \alpha. We define the Sturmian word T ρ ​ ( c α) T^{\rho}(c_{\alpha}) of slope α \alpha and formal intercept ρ \rho as the word

T ρ ​ ( c α) = lim T ρ n ​ ( c α) T^{\rho}(c_{\alpha})=\lim T^{\rho_{n}}(c_{\alpha})

having the same prefix of length q n − 1 q_{n}-1 as T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha}) for all n ≥ 1 n\geq 1.

###### Proposition 11.

Let ρ \rho be a formal intercept of the slope α \alpha ans n ≥ 1 n\geq 1. Then the length of the longest common prefix of the words

T ρ ​ ( c α) T^{\rho}(c_{\alpha}) and T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha})

equals λ N \lambda_{N}, where N N is the smallest integer N ≥ n N\geq n such that b N + 1 ≠ 0 b_{N+1}\neq 0. If no such N N exists, then they are equal.

###### Proof.

This is clear, since ρ n = ρ k \rho_{n}=\rho_{k} for all n ≤ k ≤ N n\leq k\leq N if such a N N exists, and ρ n = ρ k \rho_{n}=\rho_{k} for all n ≤ k n\leq k in the second case. ∎

###### Proposition 12.

Let x x be a Sturmian word of slope α \alpha. Then there exist a unique formal intercept ρ \rho of the slope α \alpha such that x = T ρ ​ ( c α) x=T^{\rho}(c_{\alpha}).

###### Proof.

We consider the sequence, defined for n ≥ 0 n\geq 0 as :

ρ n = min ⁡ { k ≥ 0 | x ​ and ​ T k ​ ( c α) ​ share the same prefix of length ​ q n − 1 } \rho_{n}=\min\{k\geq 0\ |\ x\text{ and }T^{k}(c_{\alpha})\text{ share the same prefix of length }q_{n}-1\}

and show that ρ = ( ρ n) n ≥ 1 \rho=(\rho_{n})_{n\geq 1} is a formal intercept. Let n ≥ 1 n\geq 1 and m = q n − 1 ∈ I n 0 m=q_{n}-1\in I_{n}^{0}. Since the referent cycle is of length q n = m + 1 q_{n}=m+1, every vertex of G m G_{m} is in the referent cycle. This shows that 0 ≤ ρ n < q n 0\leq\rho_{n}<q_{n}. Since T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}), T ρ n ​ ( c α) T^{\rho_{n}}(c_{\alpha}) and x x share the same prefix of length q n − 1 q_{n}-1, the paths they define start at the same vertex.

Write ρ n + 1 = b ​ q n + c \rho_{n+1}=bq_{n}+c with c < q n c<q_{n}. Since ρ n + 1 = b ​ q n + c < q n + 1 = a n + 1 ​ q n + q n − 1 \rho_{n+1}=bq_{n}+c<q_{n+1}=a_{n+1}q_{n}+q_{n-1}, we have b ≤ a n + 1 b\leq a_{n+1} and if b = a n + 1 b=a_{n+1} then c < q n − 1 c<q_{n-1}. Since the caracteristic word c α c_{\alpha} turns a n + 1 a_{n+1} times around the referent cycle, if b < a n + 1 b<a_{n+1} then T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}) and T c ​ ( c α) T^{c}(c_{\alpha}) start at the same vertex, and hence share the same prefix of length q n − 1 q_{n}-1. Since the referent cycle is of length q n q_{n}, and that ρ n < q n \rho_{n}<q_{n} we must have c = ρ n c=\rho_{n}. In the case where b = a n + 1 b=a_{n+1}, then c < q n − 1 c<q_{n-1} so that T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}) starts in the common part of the two cycles of G m G_{m}, T ρ n + 1 ​ ( c α) T^{\rho_{n+1}}(c_{\alpha}) and T c ​ ( c α) T^{c}(c_{\alpha}) start at the same vertex, which is on the referent cycle, and we again must have ρ n = c \rho_{n}=c. Thus ρ n = ρ n + 1 \rho_{n}=\rho_{n+1} [mod q n q_{n}] and we are done.

For unicity, notice that since for m = q n − 1 m=q_{n}-1 the referent cycle is of length q n q_{n}, there must be only one k < q n k<q_{n} such that T k ​ ( c α) T^{k}(c_{\alpha}) and T ρ ​ ( c α) T^{\rho}(c_{\alpha}) share the same prefix of length q n − 1 q_{n}-1, and since ρ n \rho_{n} is such a k k, every formal intercept γ \gamma such that x = T γ ​ ( c α) x=T^{\gamma}(c_{\alpha}) must satisfy γ n = ρ n \gamma_{n}=\rho_{n}. ∎

Example : One can compute easily that the infinite words 0 ​ c α 0c_{\alpha} and 1 ​ c α 1c_{\alpha} have respective formal intercepts ∑ i ≥ 0 a 2 ​ i + 2 ​ q 2 ​ i + 1 \sum_{i\geq 0}a_{2i+2}q_{2i+1} and ( a 1 − 1) + ∑ i ≥ 1 a 2 ​ i + 1 ​ q 2 ​ i (a_{1}-1)+\sum_{i\geq 1}a_{2i+1}q_{2i}.

Remark : In a future paper we will investigate more properties of formal intercepts.

## References

- [1] M. Lothaire, Algebraic Combinatorics on words, (2000) ISBN : 9781107326019
- [2] J.-P. Allouche, J. O. Shallit, Automatic Sequences : Theory, Applications, Generalizations, (2002) ISBN : 9780521823326
- [3] D. E. Knuth, Fibonacci multiplication, Appl. Math. Lett., 1 (1988), pp. 57-60
- [4] P. Arnoux, Some remarks about Fibonacci multiplication, Appl. Math. Lett., 2 (1989), pp. 319-320
- [5] V. Berthé, Autour du système d’énumération d’Ostrowski, Bull. Belg. Math. Soc. 8 (2001), pp. 209-238
- [6] V. Berthé, Fréquences des facteurs des suites sturmiennes, Theoretical Computer Science, Volume 165, Issue 2, 1996, pp. 295-309, ISSN 0304-3975, https://doi.org/10.1016/0304-3975(95)00224-3.
- [7] V. Berthé, C Holton, Luca Q. Zamboni, Initial powers of Sturmian sequences, Acta Arithmetica, Instytut Matematyczny PAN, 2006, 122, pp.315-347. lirmm-00123046
- [8] Y. Bugeaud, D. H. Kim, A new complexity function, repetitions in sturmian words, arXiv:1510.00279 [math.NT]
- [9] M. Mayero, The Three Gap Theorem, arXiv:cs/0609124 [cs.LO]
- [10] A. Siegel, Théoréme des trois longueurs et suites sturmiennes : mots d’agencement des longueurs, ACTA ARITHMETICA XCVII.3 (2001)
- [11] L. Ramshaw, On the discrepancy of the sequence formed by the multiples of an irrational number, Journal of Number Theory, Volume 13, Issue 2, 1981, pp. 138-175, ISSN 0022-314X, https://doi.org/10.1016/0022-314X(81)90002-0.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1803.02072
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1803.02073
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1803.02073
[7]: https://arxiv.org/pdf/1803.02073
[8]: /html/1803.02074
