<!-- source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture | converted from HTML -->

Erdős–Straus conjecture - Wikipedia

Jump to content

[image: This is a good article. Click here for more information.] [1]

From Wikipedia, the free encyclopedia

On unit fractions adding to 4/n

\\tfrac4n=\\tfrac1x+\\tfrac1y+\\tfrac1z</math> have a positive integer solution for every integer <math>n\\ge 2</math>?"}},"i":2}}]}'>

Unsolved problem in mathematics

Does 4 n = 1 x + 1 y + 1 z {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}[image: {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}] have a positive integer solution for every integer n ≥ 2 {\displaystyle n\geq 2}[image: {\displaystyle n\geq 2}]?

[More unsolved problems in mathematics][2]

The **Erdős–Straus conjecture**is an [unproven statement][3] in [number theory][4]. The conjecture is that, for every [integer][5] n {\displaystyle n}[image: {\displaystyle n}] that is greater than or equal to 2, there exist positive integers x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], and z {\displaystyle z}[image: {\displaystyle z}] for which 4 n = 1 x + 1 y + 1 z. {\displaystyle {\frac {4}{n}}={\frac {1}{x}}+{\frac {1}{y}}+{\frac {1}{z}}.}[image: {\displaystyle {\frac {4}{n}}={\frac {1}{x}}+{\frac {1}{y}}+{\frac {1}{z}}.}] In other words, the number 4 / n {\displaystyle 4/n}[image: {\displaystyle 4/n}] can be written as a sum of three positive [unit fractions][6].

The conjecture is named after [Paul Erdős][7] and [Ernst G. Straus][8], who formulated it in 1948, but it is connected to much more ancient mathematics; sums of unit fractions, like the one in this problem, are known as [Egyptian fractions][9], because of their use in [ancient Egyptian mathematics][10]. The Erdős–Straus conjecture is one of many [conjectures by Erdős][11], and one of many unsolved problems in mathematics concerning [Diophantine equations][12].

Although a solution is not known for all values of n, infinitely many values in certain infinite [arithmetic progressions][13] have simple formulas for their solution, and skipping these known values can speed up searches for [counterexamples][14]. Additionally, these searches need only consider values of n {\displaystyle n}[image: {\displaystyle n}] that are [prime numbers][15], because any composite counterexample would have a smaller counterexample among its [prime factors][16]. Computer searches have verified the truth of the conjecture up to n ≤ 10 17 {\displaystyle n\leq 10^{17}}[image: {\displaystyle n\leq 10^{17}}].

If the conjecture is reframed to allow negative unit fractions, then it is known to be true. Generalizations of the conjecture to fractions with numerator 5 or larger have also been studied.

## Background and history

[[edit][17]]

When a [rational number][18] is expanded into a sum of unit fractions, the expansion is called an [Egyptian fraction][9]. This way of writing fractions dates to the [mathematics of ancient Egypt][19], in which fractions were written this way instead of in the more modern [vulgar fraction][20] form a b {\displaystyle {\tfrac {a}{b}}}[image: {\displaystyle {\tfrac {a}{b}}}] with a numerator a {\displaystyle a}[image: {\displaystyle a}] and denominator b {\displaystyle b}[image: {\displaystyle b}]. The Egyptians produced tables of Egyptian fractions for unit fractions multiplied by two, the numbers that in modern notation would be written 2 n {\displaystyle {\tfrac {2}{n}}}[image: {\displaystyle {\tfrac {2}{n}}}], such as the [Rhind Mathematical Papyrus table][21]; in these tables, most of these expansions use either two or three terms. [1] These tables were needed, because the obvious expansion 2 n = 1 n + 1 n {\displaystyle {\tfrac {2}{n}}={\tfrac {1}{n}}+{\tfrac {1}{n}}}[image: {\displaystyle {\tfrac {2}{n}}={\tfrac {1}{n}}+{\tfrac {1}{n}}}] was not allowed: the Egyptians required all of the fractions in an Egyptian fraction to be different from each other. This same requirement, that all fractions be different, is sometimes imposed in the Erdős–Straus conjecture, but it makes no significant difference to the problem, because for 2"}}'> 2}"> n > 2 {\displaystyle n>2} 2}"/> any solution to 4 n = 1 x + 1 y + 1 z {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}[image: {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}] where the unit fractions are not distinct can be converted into a solution where they are all distinct; see below. [2]

Although the Egyptians did not always find expansions using as few terms as possible, later mathematicians have been interested in the question of how few terms are needed. Every fraction a b {\displaystyle {\tfrac {a}{b}}}[image: {\displaystyle {\tfrac {a}{b}}}] has an expansion of at most a {\displaystyle a}[image: {\displaystyle a}] terms, so in particular 2 n {\displaystyle {\tfrac {2}{n}}}[image: {\displaystyle {\tfrac {2}{n}}}] needs at most two terms, 3 n {\displaystyle {\tfrac {3}{n}}}[image: {\displaystyle {\tfrac {3}{n}}}] needs at most three terms, and 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] needs at most four terms. For 2 n {\displaystyle {\tfrac {2}{n}}}[image: {\displaystyle {\tfrac {2}{n}}}], two terms are always needed, and for 3 n {\displaystyle {\tfrac {3}{n}}}[image: {\displaystyle {\tfrac {3}{n}}}], three terms are sometimes needed, so for both of these numerators, the maximum number of terms that might be needed is known. However, for 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}], it is unknown whether four terms are sometimes needed, or whether it is possible to express all fractions of the form 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] using only three unit fractions; this is the Erdős–Straus conjecture. Thus, the conjecture covers the first unknown case of a more general question, the problem of finding for all a {\displaystyle a}[image: {\displaystyle a}] the maximum number of terms needed in expansions for fractions a b {\displaystyle {\tfrac {a}{b}}}[image: {\displaystyle {\tfrac {a}{b}}}]. [1]

One way to find short (but not always shortest) expansions uses the [greedy algorithm for Egyptian fractions][22], first described in 1202 by [Fibonacci][23] in his book *[Liber Abaci][24]*. This method chooses one unit fraction at a time, at each step choosing the largest possible unit fraction that would not cause the expanded sum to exceed the target number. After each step, the numerator of the fraction that still remains to be expanded decreases, so the total number of steps can never exceed the starting numerator, [1] but sometimes it is smaller. For example, when it is applied to 3 n {\displaystyle {\tfrac {3}{n}}}[image: {\displaystyle {\tfrac {3}{n}}}], the greedy algorithm will use two terms whenever n {\displaystyle n}[image: {\displaystyle n}] is 2 modulo 3, but there exists a two-term expansion whenever n {\displaystyle n}[image: {\displaystyle n}] has a factor that is 2 modulo 3, a weaker condition. For numbers of the form 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}], the greedy algorithm will produce a four-term expansion whenever n {\displaystyle n}[image: {\displaystyle n}] is 1 modulo 4, and an expansion with fewer terms otherwise. [3] Thus, another way of rephrasing the Erdős–Straus conjecture asks whether there exists another method for producing Egyptian fractions, using a smaller maximum number of terms for the numbers 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}]. [1]

The Erdős–Straus conjecture was formulated in 1948 by [Paul Erdős][7] and [Ernst G. Straus][8], and published by Erdős (1950). Richard Obláth also published an early work on the conjecture, a paper written in 1948 and published in 1950, in which he extended earlier calculations of Straus and Harold N. Shapiro in order to verify the conjecture for all n ≤ 10 5 {\displaystyle n\leq 10^{5}}[image: {\displaystyle n\leq 10^{5}}]. [4]

## Formulation

[[edit][25]]

The conjecture states that, for every integer n ≥ 2 {\displaystyle n\geq 2}[image: {\displaystyle n\geq 2}], there exist positive integers x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], and z {\displaystyle z}[image: {\displaystyle z}] such that 4 n = 1 x + 1 y + 1 z. {\displaystyle {\frac {4}{n}}={\frac {1}{x}}+{\frac {1}{y}}+{\frac {1}{z}}.}[image: {\displaystyle {\frac {4}{n}}={\frac {1}{x}}+{\frac {1}{y}}+{\frac {1}{z}}.}] For instance, for n = 5 {\displaystyle n=5}[image: {\displaystyle n=5}], there are two solutions: 4 5 = 1 2 + 1 4 + 1 20 = 1 2 + 1 5 + 1 10. {\displaystyle {\frac {4}{5}}={\frac {1}{2}}+{\frac {1}{4}}+{\frac {1}{20}}={\frac {1}{2}}+{\frac {1}{5}}+{\frac {1}{10}}.}[image: {\displaystyle {\frac {4}{5}}={\frac {1}{2}}+{\frac {1}{4}}+{\frac {1}{20}}={\frac {1}{2}}+{\frac {1}{5}}+{\frac {1}{10}}.}]

Multiplying both sides of the equation 4 n = 1 x + 1 y + 1 z {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}[image: {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}] by n x y z {\displaystyle nxyz}[image: {\displaystyle nxyz}] leads to an equivalent [polynomial][26] form 4 x y z = n ( x y + x z + y z) {\displaystyle 4xyz=n(xy+xz+yz)}[image: {\displaystyle 4xyz=n(xy+xz+yz)}] for the problem. [5]

### Distinct unit fractions

[[edit][27]]

Some researchers additionally require that the integers x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], and z {\displaystyle z}[image: {\displaystyle z}] be distinct from each other, as the Egyptians would have, while others allow them to be equal. [1] For n ≥ 3 {\displaystyle n\geq 3}[image: {\displaystyle n\geq 3}], it does not matter whether they are required to be distinct: if there exists a solution with any three integers, then there exists a solution with distinct integers. [2] This is because two identical unit fractions can be replaced through one of the following two expansions: 1 2 r + 1 2 r ⇒ 1 r + 1 + 1 r ( r + 1) 1 2 r + 1 + 1 2 r + 1 ⇒ 1 r + 1 + 1 ( r + 1) ( 2 r + 1) {\displaystyle {\begin{aligned}{\frac {1}{2r}}+{\frac {1}{2r}}&\Rightarrow {\frac {1}{r+1}}+{\frac {1}{r(r+1)}}\\{\frac {1}{2r+1}}+{\frac {1}{2r+1}}&\Rightarrow {\frac {1}{r+1}}+{\frac {1}{(r+1)(2r+1)}}\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}{\frac {1}{2r}}+{\frac {1}{2r}}&\Rightarrow {\frac {1}{r+1}}+{\frac {1}{r(r+1)}}\\{\frac {1}{2r+1}}+{\frac {1}{2r+1}}&\Rightarrow {\frac {1}{r+1}}+{\frac {1}{(r+1)(2r+1)}}\\\end{aligned}}}] (according to whether the repeated fraction has an even or odd denominator) and this replacement can be repeated until no duplicate fractions remain. [6] For n = 2 {\displaystyle n=2}[image: {\displaystyle n=2}], however, the only solutions are permutations of 4 2 = 1 2 + 1 2 + 1 1 {\displaystyle {\tfrac {4}{2}}={\tfrac {1}{2}}+{\tfrac {1}{2}}+{\tfrac {1}{1}}}[image: {\displaystyle {\tfrac {4}{2}}={\tfrac {1}{2}}+{\tfrac {1}{2}}+{\tfrac {1}{1}}}]. [1]

### Negative-number solutions

[[edit][28]]

The Erdős–Straus conjecture requires that all three of x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], and z {\displaystyle z}[image: {\displaystyle z}] be positive. This requirement is essential to the difficulty of the problem. Even without this relaxation, the Erdős–Straus conjecture is difficult only for odd values of n {\displaystyle n}[image: {\displaystyle n}], and if negative values were allowed then the problem could be solved for every odd n {\displaystyle n}[image: {\displaystyle n}] by the following formula: [7] 4 n = 1 ( n − 1) / 2 + 1 ( n + 1) / 2 − 1 n ( n − 1) ( n + 1) / 4. {\displaystyle {\frac {4}{n}}={\frac {1}{(n-1)/2}}+{\frac {1}{(n+1)/2}}-{\frac {1}{n(n-1)(n+1)/4}}.}[image: {\displaystyle {\frac {4}{n}}={\frac {1}{(n-1)/2}}+{\frac {1}{(n+1)/2}}-{\frac {1}{n(n-1)(n+1)/4}}.}]

## Computational results

[[edit][29]]

If the conjecture is false, it could be proven false simply by finding a number 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] that has no three-term representation. In order to check this, various authors have performed [brute-force searches][30] for counterexamples to the conjecture. [8] Searches of this type have confirmed that the conjecture is true for all n {\displaystyle n}[image: {\displaystyle n}] up to 10 17 {\displaystyle 10^{17}}[image: {\displaystyle 10^{17}}]. [9]

In such searches, it is only necessary to look for expansions for numbers 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] where n {\displaystyle n}[image: {\displaystyle n}] is a [prime number][15]. This is because, whenever 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] has a three-term expansion, so does 4 m n {\displaystyle {\tfrac {4}{mn}}}[image: {\displaystyle {\tfrac {4}{mn}}}] for all positive integers m {\displaystyle m}[image: {\displaystyle m}]. To find a solution for 4 m n {\displaystyle {\tfrac {4}{mn}}}[image: {\displaystyle {\tfrac {4}{mn}}}], just divide all of the unit fractions in the solution for 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] by m {\displaystyle m}[image: {\displaystyle m}]: 4 n = 1 x + 1 y + 1 z ⇒ 4 m n = 1 m x + 1 m y + 1 m z. {\displaystyle {\frac {4}{n}}={\frac {1}{x}}+{\frac {1}{y}}+{\frac {1}{z}}\ \Rightarrow \ {\frac {4}{mn}}={\frac {1}{mx}}+{\frac {1}{my}}+{\frac {1}{mz}}.}[image: {\displaystyle {\frac {4}{n}}={\frac {1}{x}}+{\frac {1}{y}}+{\frac {1}{z}}\ \Rightarrow \ {\frac {4}{mn}}={\frac {1}{mx}}+{\frac {1}{my}}+{\frac {1}{mz}}.}] If 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] were a [counterexample][14] to the conjecture, for a [composite number][31] n {\displaystyle n}[image: {\displaystyle n}], every [prime factor][16] p {\displaystyle p}[image: {\displaystyle p}] of n {\displaystyle n}[image: {\displaystyle n}] would also provide a counterexample 4 p {\displaystyle {\tfrac {4}{p}}}[image: {\displaystyle {\tfrac {4}{p}}}] that would have been found earlier by the brute-force search. Therefore, checking the existence of a solution for composite numbers is redundant, and can be skipped by the search. Additionally, the known modular identities for the conjecture (see below) can speed these searches by skipping over other values known to have a solution. For instance, the greedy algorithm finds an expansion with three or fewer terms for every number 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] where n {\displaystyle n}[image: {\displaystyle n}] is not 1 modulo 4, so the searches only need to test values that are 1 modulo 4. One way to make progress on this problem is to collect more modular identities, allowing computer searches to reach higher limits with fewer tests. [9]

The number of distinct solutions to the 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] problem, as a function of n {\displaystyle n}[image: {\displaystyle n}], has also been found by computer searches for small n {\displaystyle n}[image: {\displaystyle n}] and appears to grow somewhat irregularly with n {\displaystyle n}[image: {\displaystyle n}]. Starting with n = 3 {\displaystyle n=3}[image: {\displaystyle n=3}], the numbers of distinct solutions with distinct denominators are

1, 1, 2, 5, 5, 6, 4, 9, 7, 15, 4, 14, 33, 22, 4, 21, 9, ... .

Even for larger n {\displaystyle n}[image: {\displaystyle n}] there can sometimes be relatively few solutions; for instance there are only seven distinct solutions for n = 73 {\displaystyle n=73}[image: {\displaystyle n=73}]. [10]

## Theoretical results

[[edit][32]]

In the form 4 x y z = n ( x y + x z + y z) {\displaystyle 4xyz=n(xy+xz+yz)}[image: {\displaystyle 4xyz=n(xy+xz+yz)}], a [polynomial equation][33] with integer variables, the Erdős–Straus conjecture is an example of a [Diophantine equation][12]. The [Hasse principle][34] for Diophantine equations suggests that these equations should be studied using [modular arithmetic][35]. If a polynomial equation has a solution in the integers, then taking this solution modulo q {\displaystyle q}[image: {\displaystyle q}], for any integer q {\displaystyle q}[image: {\displaystyle q}], provides a solution in modulo- q {\displaystyle q}[image: {\displaystyle q}] arithmetic. In the other direction, if an equation has a solution modulo q {\displaystyle q}[image: {\displaystyle q}] for every [prime power][36] q {\displaystyle q}[image: {\displaystyle q}], then in some cases it is possible to piece together these modular solutions, using methods related to the [Chinese remainder theorem][37], to get a solution in the integers. The power of the Hasse principle to solve some problems is limited by the [Manin obstruction][38], but for the Erdős–Straus conjecture this obstruction does not exist. [11]

On the face of it this principle makes little sense for the Erdős–Straus conjecture. For every n {\displaystyle n}[image: {\displaystyle n}], the equation 4 x y z = n ( x y + x z + y z) {\displaystyle 4xyz=n(xy+xz+yz)}[image: {\displaystyle 4xyz=n(xy+xz+yz)}] is easily solvable modulo any prime, or prime power, but there appears to be no way to piece those solutions together to get a [positive integer][39] solution to the equation. Nevertheless, modular arithmetic, and identities based on modular arithmetic, have proven a very important tool in the study of the conjecture. [12]

### Modular identities

[[edit][40]]

For values of n {\displaystyle n}[image: {\displaystyle n}] satisfying certain [congruence relations][35], one can find an expansion for 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] automatically as an instance of a polynomial identity. For instance, whenever n {\displaystyle n}[image: {\displaystyle n}] is 2 modulo 3, 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] has the expansion 4 n = 1 n + 1 ( n + 1) / 3 + 1 n ( n + 1) / 3. {\displaystyle {\frac {4}{n}}={\frac {1}{n}}+{\frac {1}{(n+1)/3}}+{\frac {1}{n(n+1)/3}}.}[image: {\displaystyle {\frac {4}{n}}={\frac {1}{n}}+{\frac {1}{(n+1)/3}}+{\frac {1}{n(n+1)/3}}.}] Here each of the three denominators n {\displaystyle n}[image: {\displaystyle n}], ( n + 1) / 3 {\displaystyle (n+1)/3}[image: {\displaystyle (n+1)/3}], and n ( n + 1) / 3 {\displaystyle n(n+1)/3}[image: {\displaystyle n(n+1)/3}] is a polynomial of n {\displaystyle n}[image: {\displaystyle n}], and each is an integer whenever n {\displaystyle n}[image: {\displaystyle n}] is 2 modulo 3. The [greedy algorithm for Egyptian fractions][22] finds a solution in three or fewer terms whenever n {\displaystyle n}[image: {\displaystyle n}] is not 1 or 17 mod 24, and the 17 mod 24 case is covered by the 2 mod 3 relation, so the only values of n {\displaystyle n}[image: {\displaystyle n}] for which these two methods do not find expansions in three or fewer terms are those congruent to 1 mod 24. [13]

Polynomial identities listed by Mordell (1967) provide three-term Egyptian fractions for 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] whenever n {\displaystyle n}[image: {\displaystyle n}] is one of:

- 2 mod 3 (above),
- 3 mod 4,
- 2 or 3 mod 5,
- 3, 5, or 6 mod 7, or
- 5 mod 8.

Combinations of Mordell's identities can be used to expand 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] for all n {\displaystyle n}[image: {\displaystyle n}] except possibly those that are 1, 121, 169, 289, 361, or 529 mod 840. The smallest prime that these identities do not cover is 1009. By combining larger classes of modular identities, Webb and others showed that the [natural density][41] of potential counterexamples to the conjecture is zero: as a parameter N {\displaystyle N}[image: {\displaystyle N}] goes to infinity, the fraction of values in the interval [1, N] {\displaystyle [1,N]}[image: {\displaystyle [1,N]}] that could be counterexamples tends to zero in the limit. [14]

### Nonexistence of identities

[[edit][42]]

If it were possible to find solutions such as the ones above for enough different moduli, forming a complete [covering system][43] of congruences, the problem would be solved. However, as Mordell (1967) showed, a polynomial identity that provides a solution for values of n {\displaystyle n}[image: {\displaystyle n}] congruent to r {\displaystyle r}[image: {\displaystyle r}] mod p {\displaystyle p}[image: {\displaystyle p}] can exist only when r {\displaystyle r}[image: {\displaystyle r}] is not congruent to a square modulo p {\displaystyle p}[image: {\displaystyle p}]. (More formally, this kind of identity can exist only when r {\displaystyle r}[image: {\displaystyle r}] is not a [quadratic residue][44] modulo p {\displaystyle p}[image: {\displaystyle p}].) For instance, 2 is a non-square mod 3, so Mordell's result allows the existence of an identity for n {\displaystyle n}[image: {\displaystyle n}] congruent to 2 mod 3. However, 1 is a square mod 3 (equal to the square of both 1 and 2 mod 3), so there can be no similar identity for *all*values of n {\displaystyle n}[image: {\displaystyle n}] that are congruent to 1 mod 3. More generally, as 1 is a square mod n {\displaystyle n}[image: {\displaystyle n}] for all 1"}}'> 1}"> n > 1 {\displaystyle n>1} 1}"/>, there can be no complete covering system of modular identities for all n {\displaystyle n}[image: {\displaystyle n}], because 1 will always be uncovered. [15]

Despite Mordell's result limiting the form of modular identities for this problem, there is still some hope of using modular identities to prove the Erdős–Straus conjecture. No prime number can be a square, so by the [Hasse–Minkowski theorem][45], whenever p {\displaystyle p}[image: {\displaystyle p}] is prime, there exists a larger prime q {\displaystyle q}[image: {\displaystyle q}] such that p {\displaystyle p}[image: {\displaystyle p}] is not a quadratic residue modulo q {\displaystyle q}[image: {\displaystyle q}]. One possible approach to proving the conjecture would be to find for each prime p {\displaystyle p}[image: {\displaystyle p}] a larger prime q {\displaystyle q}[image: {\displaystyle q}] and a congruence solving the 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] problem for n {\displaystyle n}[image: {\displaystyle n}] congruent to p {\displaystyle p}[image: {\displaystyle p}] mod q {\displaystyle q}[image: {\displaystyle q}]. If this could be done, no prime p {\displaystyle p}[image: {\displaystyle p}] could be a counterexample to the conjecture and the conjecture would be true. [13]

### The number of solutions

[[edit][46]]

Elsholtz & Tao (2013) showed that the average number of solutions to the 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}] problem (averaged over the prime numbers up to n {\displaystyle n}[image: {\displaystyle n}]) is [upper bounded][47] [polylogarithmically][48] in n {\displaystyle n}[image: {\displaystyle n}]. For some other Diophantine problems, the existence of a solution can be demonstrated through [asymptotic][49] [lower bounds][50] on the number of solutions, but this works best when the number of solutions grows at least polynomially, so the slower growth rate of Elsholtz and Tao's result makes a proof of this type less likely. Elsholtz and Tao classify solutions according to whether one or two of x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], or z {\displaystyle z}[image: {\displaystyle z}] is divisible by n {\displaystyle n}[image: {\displaystyle n}]; for prime n {\displaystyle n}[image: {\displaystyle n}], these are the only possibilities, although (on average) most solutions for composite n {\displaystyle n}[image: {\displaystyle n}] are of other types. Their proof uses the [Bombieri–Vinogradov theorem][51], the [Brun–Titchmarsh theorem][52], and a system of modular identities, valid when n {\displaystyle n}[image: {\displaystyle n}] is congruent to − c {\displaystyle -c}[image: {\displaystyle -c}] or − 1 c {\displaystyle -{\tfrac {1}{c}}}[image: {\displaystyle -{\tfrac {1}{c}}}] modulo 4 a b {\displaystyle 4ab}[image: {\displaystyle 4ab}], where a {\displaystyle a}[image: {\displaystyle a}] and b {\displaystyle b}[image: {\displaystyle b}] are any two [coprime][53] positive integers and c {\displaystyle c}[image: {\displaystyle c}] is any odd factor of a + b {\displaystyle a+b}[image: {\displaystyle a+b}]. For instance, setting a = b = 1 {\displaystyle a=b=1}[image: {\displaystyle a=b=1}] gives one of Mordell's identities, valid when n {\displaystyle n}[image: {\displaystyle n}] is 3 mod 4. [16]

## Generalizations

[[edit][54]]

As with fractions of the form 4 n {\displaystyle {\tfrac {4}{n}}}[image: {\displaystyle {\tfrac {4}{n}}}], it has been conjectured that every fraction 5 n {\displaystyle {\tfrac {5}{n}}}[image: {\displaystyle {\tfrac {5}{n}}}] (for 1"}}'> 1}"> n > 1 {\displaystyle n>1} 1}"/>) can be expressed as a sum of three positive unit fractions. A generalized version of the conjecture states that, for any positive k {\displaystyle k}[image: {\displaystyle k}], all but finitely many fractions k n {\displaystyle {\tfrac {k}{n}}}[image: {\displaystyle {\tfrac {k}{n}}}] can be expressed as a sum of three positive unit fractions. The conjecture for fractions 5 n {\displaystyle {\tfrac {5}{n}}}[image: {\displaystyle {\tfrac {5}{n}}}] was made by [Wacław Sierpiński][55] in a 1956 paper, which went on to credit the full conjecture to Sierpiński's student [Andrzej Schinzel][56]. [17]

Even if the generalized conjecture is false for any fixed value of k {\displaystyle k}[image: {\displaystyle k}], then the number of fractions k n {\displaystyle {\tfrac {k}{n}}}[image: {\displaystyle {\tfrac {k}{n}}}] with n {\displaystyle n}[image: {\displaystyle n}] in the range from 1 to N {\displaystyle N}[image: {\displaystyle N}] that do not have three-term expansions must grow only sublinearly as a function of N {\displaystyle N}[image: {\displaystyle N}]. [14] In particular, if the Erdős–Straus conjecture itself (the case k = 4 {\displaystyle k=4}[image: {\displaystyle k=4}]) is false, then the number of counterexamples grows only sublinearly. Even more strongly, for any fixed k {\displaystyle k}[image: {\displaystyle k}], only a sublinear number of values of n {\displaystyle n}[image: {\displaystyle n}] need more than two terms in their Egyptian fraction expansions. [18] The generalized version of the conjecture is equivalent to the statement that the number of unexpandable fractions is not just sublinear but finite. [19]

When n {\displaystyle n}[image: {\displaystyle n}] is an [odd number][57], by analogy to the problem of [odd greedy expansions][58] for Egyptian fractions, one may ask for solutions to k n = 1 x + 1 y + 1 z {\displaystyle {\tfrac {k}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}[image: {\displaystyle {\tfrac {k}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}] in which x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], and z {\displaystyle z}[image: {\displaystyle z}] are distinct positive odd numbers. Solutions to this equation are known to always exist for the case in which *k*= 3. [20]

## See also

[[edit][59]]

- [List of sums of reciprocals][60]

## Notes

[[edit][61]]

1. 1 2 3 4 5 6 Graham (2013).
2. 1 2 Eppstein (1995), [conflict resolution section][62].
3. ↑ Eppstein (1995).
4. ↑ Obláth (1950); Elsholtz & Tao (2013)
5. ↑ See e.g. Sander (1994) for a simpler Diophantine formulation using more specific assumptions about which of x {\displaystyle x}[image: {\displaystyle x}], y {\displaystyle y}[image: {\displaystyle y}], and z {\displaystyle z}[image: {\displaystyle z}] are divisible by n {\displaystyle n}[image: {\displaystyle n}].
6. ↑ See the [conflict resolution][62] section of Eppstein (1995) for a proof that a closely related replacement process (with a different expansion for even denominators that reduces the number of fractions) always terminates with a non-repeating expansion.
7. ↑ Jaroma (2004).
8. ↑ Obláth (1950); Rosati (1954); Kiss (1959); Bernstein (1962); Yamamoto (1965); Terzi (1971); Jollensten (1976); Kotsireas (1999).
9. 1 2 Salez (2014).
10. ↑ [Sloane, N. J. A.][63] (ed.), ["Sequence A073101"][64], *The [On-Line Encyclopedia of Integer Sequences][65]*, OEIS Foundation
11. ↑ Bright & Loughran (2020).
12. ↑ Elsholtz & Tao (2013).
13. 1 2 Ionascu & Wilson (2011).
14. 1 2 Webb (1970); Vaughan (1970); Li (1981); Yang (1982); Ahmadi & Bleicher (1998); Elsholtz (2001).
15. ↑ Mordell (1967).
16. ↑ [On the number of solutions to 4/p = 1/n_1 + 1/n_2 + 1/n_3][66], [Terence Tao][67], "What's new", July 7, 2011; [Counting the number of solutions to the Erdös-Straus equation on unit fractions][68], [Terence Tao][67], July 31, 2011.
17. ↑ Sierpiński (1956); Vaughan (1970).
18. ↑ Hofmeister & Stoll (1985).
19. ↑ Vaughan (1970).
20. ↑ Schinzel (1956); Suryanarayana & Rao (1965); Hagedorn (2000).

## References

[[edit][69]]

m/n=1/x+1/y+1/z</math>, insbesondere im Fall <math>m=4</math>"},"volume":{"wt":"211"},"year":{"wt":"1962"},"doi":{"wt":"10.1515/crll.1962.211.1"},"s2cid":{"wt":"118098315"}},"i":2}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last1":{"wt":"Bright"},"first1":{"wt":"Martin"},"last2":{"wt":"Loughran"},"first2":{"wt":"Daniel"},"doi":{"wt":"10.1112/blms.12374"},"issue":{"wt":"4"},"journal":{"wt":"Bulletin of the London Mathematical Society"},"mr":{"wt":"4171399"},"pages":{"wt":"746–761"},"title":{"wt":"Brauer–Manin obstruction for Erdős–Straus surfaces"},"volume":{"wt":"52"},"year":{"wt":"2020"},"arxiv":{"wt":"1908.02526"},"s2cid":{"wt":"218959757"}},"i":3}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Elsholtz"},"first":{"wt":"Christian"},"title":{"wt":"Sums of <math>k</math> unit fractions"},"journal":{"wt":"[[Transactions of the American Mathematical Society]]"},"volume":{"wt":"353"},"issue":{"wt":"8"},"pages":{"wt":"3209–3227"},"year":{"wt":"2001"},"mr":{"wt":"1828604"},"doi":{"wt":"10.1090/S0002-9947-01-02782-9"},"doi-access":{"wt":"free"}},"i":4}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last1":{"wt":"Elsholtz"},"first1":{"wt":"Christian"},"last2":{"wt":"Tao"},"first2":{"wt":"Terence"},"author2-link":{"wt":"Terence Tao"},"arxiv":{"wt":"1107.1010"},"issue":{"wt":"1"},"journal":{"wt":"Journal of the Australian Mathematical Society"},"mr":{"wt":"3101397"},"pages":{"wt":"50–105"},"title":{"wt":"Counting the number of solutions to the Erdős–Straus equation on unit fractions"},"url":{"wt":"https://terrytao.files.wordpress.com/2011/07/egyptian-count13.pdf"},"volume":{"wt":"94"},"year":{"wt":"2013"},"doi":{"wt":"10.1017/S1446788712000468"},"s2cid":{"wt":"17233943"}},"i":5}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Eppstein"},"first":{"wt":"David"},"authorlink":{"wt":"David Eppstein"},"issue":{"wt":"2"},"journal":{"wt":"Mathematica in Education and Research"},"pages":{"wt":"5–15"},"title":{"wt":"Ten algorithms for Egyptian fractions"},"volume":{"wt":"4"},"year":{"wt":"1995"}},"i":6}},". See in particular the [https://www.ics.uci.edu/~eppstein/numth/egypt/smallnum.html \"Small numerators\"] section\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Erdős"},"first":{"wt":"Paul"},"authorlink":{"wt":"Paul Erdős"},"title":{"wt":"Az <math>\\tfrac1{x_1}+\\tfrac1{x_2}+\\cdots+\\tfrac1{x_n}=\\tfrac{a}{b}</math> egyenlet egész számú megoldásairól (On a Diophantine Equation)"},"language":{"wt":"Hungarian"},"journal":{"wt":"Mat. Lapok."},"volume":{"wt":"1"},"pages":{"wt":"192–210"},"year":{"wt":"1950"},"url":{"wt":"https://www.renyi.hu/~p_erdos/1950-02.pdf"},"mr":{"wt":"0043117"}},"i":7}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Graham"},"first":{"wt":"Ronald L."},"author-link":{"wt":"Ronald Graham"},"editor1-last":{"wt":"Lovász"},"editor1-first":{"wt":"László"},"editor1-link":{"wt":"László Lovász"},"editor2-last":{"wt":"Ruzsa"},"editor2-first":{"wt":"Imre Z."},"editor2-link":{"wt":"Imre Z. Ruzsa"},"editor3-last":{"wt":"Sós"},"editor3-first":{"wt":"Vera T."},"editor3-link":{"wt":"Vera T. Sós"},"contribution":{"wt":"Paul Erdős and Egyptian fractions"},"contribution-url":{"wt":"https://www.math.ucsd.edu/~ronspubs/13_03_Egyptian.pdf"},"doi":{"wt":"10.1007/978-3-642-39286-3_9"},"location":{"wt":"Budapest"},"mr":{"wt":"3203600"},"pages":{"wt":"289–309"},"publisher":{"wt":"[[János Bolyai Mathematical Society]]"},"series":{"wt":"Bolyai Society Mathematical Studies"},"title":{"wt":"Erdös Centennial"},"volume":{"wt":"25"},"year":{"wt":"2013"},"isbn":{"wt":"978-3-642-39285-6"}},"i":8}},"\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"authorlink":{"wt":"Richard K. Guy"},"last":{"wt":"Guy"},"first":{"wt":"Richard K."},"title":{"wt":"Unsolved Problems in Number Theory"},"edition":{"wt":"3rd"},"publisher":{"wt":"[[Springer Verlag]]"},"year":{"wt":"2004"},"isbn":{"wt":"0-387-20860-7"},"pages":{"wt":"D11"}},"i":9}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Hagedorn"},"first":{"wt":"Thomas R."},"title":{"wt":"A proof of a conjecture on Egyptian fractions"},"journal":{"wt":"[[American Mathematical Monthly]]"},"volume":{"wt":"107"},"pages":{"wt":"62–63"},"year":{"wt":"2000"},"mr":{"wt":"1745572"},"doi":{"wt":"10.2307/2589381"},"issue":{"wt":"1"},"publisher":{"wt":"Mathematical Association of America"},"jstor":{"wt":"2589381"}},"i":10}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last1":{"wt":"Hofmeister"},"first1":{"wt":"Gerd"},"last2":{"wt":"Stoll"},"first2":{"wt":"Peter"},"mr":{"wt":"809971"},"journal":{"wt":"Journal für die Reine und Angewandte Mathematik"},"pages":{"wt":"141–145"},"title":{"wt":"Note on Egyptian fractions"},"volume":{"wt":"362"},"year":{"wt":"1985"}},"i":11}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last1":{"wt":"Ionascu"},"first1":{"wt":"Eugen J."},"last2":{"wt":"Wilson"},"first2":{"wt":"Andrew"},"arxiv":{"wt":"1001.1100"},"issue":{"wt":"1"},"journal":{"wt":"Revue Roumaine de Mathématiques Pures et Appliquées"},"mr":{"wt":"2848047"},"pages":{"wt":"21–30"},"title":{"wt":"On the Erdös–Straus conjecture"},"volume":{"wt":"56"},"year":{"wt":"2011"}},"i":12}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Jaroma"},"first":{"wt":"John H."},"issue":{"wt":"1"},"journal":{"wt":"[[Crux Mathematicorum]]"},"pages":{"wt":"36–37"},"title":{"wt":"On expanding <math>4/n</math> into three Egyptian fractions"},"url":{"wt":"https://cms.math.ca/publications/crux/issue/?volume=30&issue=1"},"volume":{"wt":"30"},"year":{"wt":"2004"}},"i":13}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Jollensten"},"first":{"wt":"Ralph W."},"contribution":{"wt":"A note on the Egyptian problem"},"mr":{"wt":"0429735"},"location":{"wt":"Winnipeg, Man."},"pages":{"wt":"351–364"},"publisher":{"wt":"Utilitas Math."},"series":{"wt":"Congressus Numerantium"},"title":{"wt":"Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory, and Computing (Louisiana State Univ., Baton Rouge, La., 1976)"},"volume":{"wt":"XVII"},"year":{"wt":"1976"}},"i":14}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Kiss"},"first":{"wt":"Ernest"},"mr":{"wt":"0125069"},"journal":{"wt":"Acad. R. P. Romîne Fil. Cluj Stud. Cerc. Mat."},"pages":{"wt":"59–62"},"title":{"wt":"Quelques remarques sur une équation diophantienne"},"language":{"wt":"Romanian"},"volume":{"wt":"10"},"year":{"wt":"1959"}},"i":15}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Kotsireas"},"first":{"wt":"Ilias"},"contribution":{"wt":"The Erdős-Straus conjecture on Egyptian fractions"},"mr":{"wt":"1901903"},"location":{"wt":"Budapest"},"pages":{"wt":"140–144"},"publisher":{"wt":"János Bolyai Math. Soc."},"title":{"wt":"Paul Erdős and his mathematics (Budapest, 1999)"},"year":{"wt":"1999"}},"i":16}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Li"},"first":{"wt":"Delang"},"title":{"wt":"On the equation <math>4/n=1/x+1/y+1/z</math>"},"journal":{"wt":"[[Journal of Number Theory]]"},"volume":{"wt":"13"},"issue":{"wt":"4"},"pages":{"wt":"485–494"},"year":{"wt":"1981"},"mr":{"wt":"0642923"},"doi":{"wt":"10.1016/0022-314X(81)90039-1"},"doi-access":{"wt":"free"}},"i":17}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Mordell"},"first":{"wt":"Louis J."},"authorlink":{"wt":"Louis Mordell"},"title":{"wt":"Diophantine Equations"},"publisher":{"wt":"Academic Press"},"year":{"wt":"1967"},"pages":{"wt":"287–290"}},"i":18}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Obláth"},"first":{"wt":"Richard"},"mr":{"wt":"0038999"},"journal":{"wt":"[[Mathesis (journal)|Mathesis]]"},"quote":{"wt":"M. Strauss [sic] a vérifié l'hypothèse de M. Erdős pour toute valeur de n < 5.000, et M. Shapiro pour n < 20.000. Nos théorèmes donnent la solution pour tout nombre < 106.128"},"pages":{"wt":"308–316"},"title":{"wt":"Sur l'équation diophantienne <math>\\tfrac4n=\\tfrac1{x_1}+\\tfrac1{x_2}+\\tfrac1{x_3}</math>"},"language":{"wt":"French"},"volume":{"wt":"59"},"year":{"wt":"1950"}},"i":19}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Rosati"},"first":{"wt":"Luigi Antonio"},"mr":{"wt":"0060526"},"journal":{"wt":"Boll. Un. Mat. Ital. (3)"},"language":{"wt":"Italian"},"pages":{"wt":"59–63"},"title":{"wt":"Sull'equazione diofantea <math>4/n=1/x_1+1/x_2+1/x_3</math>"},"volume":{"wt":"9"},"year":{"wt":"1954"}},"i":20}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Salez"},"first":{"wt":"Serge E."},"title":{"wt":"The Erdős-Straus conjecture New modular equations and checking up to <math>N=10^{17}</math>"},"arxiv":{"wt":"1406.6307"},"year":{"wt":"2014"},"bibcode":{"wt":"2014arXiv1406.6307S"}},"i":21}},"\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Sander"},"first":{"wt":"J. W."},"doi":{"wt":"10.1006/jnth.1994.1008"},"issue":{"wt":"2"},"journal":{"wt":"Journal of Number Theory"},"mr":{"wt":"1269248"},"pages":{"wt":"123–136"},"title":{"wt":"On <math>4/n=1/x+1/y+1/z</math> and Iwaniec' half-dimensional sieve"},"volume":{"wt":"46"},"year":{"wt":"1994"},"doi-access":{"wt":"free"}},"i":22}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Schinzel"},"first":{"wt":"André"},"authorlink":{"wt":"Andrzej Schinzel"},"mr":{"wt":"0080683"},"journal":{"wt":"[[Mathesis (journal)|Mathesis]]"},"language":{"wt":"French"},"pages":{"wt":"219–222"},"title":{"wt":"Sur quelques propriétés des nombres <math>3/n</math> et <math>4/n</math>, où <math>n</math> est un nombre impair"},"volume":{"wt":"65"},"year":{"wt":"1956"}},"i":23}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Sierpiński"},"first":{"wt":"Wacław"},"authorlink":{"wt":"Wacław Sierpiński"},"title":{"wt":"Sur les décompositions de nombres rationnels en fractions primaires"},"language":{"wt":"French"},"journal":{"wt":"[[Mathesis (journal)|Mathesis]]"},"year":{"wt":"1956"},"volume":{"wt":"65"},"pages":{"wt":"16–32"},"mr":{"wt":"0078385"}},"i":24}},". Reprinted with additional annotations in ",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Sierpiński"},"first":{"wt":"Wacław"},"location":{"wt":"Warsaw"},"mr":{"wt":"0414302"},"pages":{"wt":"169–184"},"publisher":{"wt":"PWN—Éditions Scientifiques de Pologne"},"title":{"wt":"Oeuvres Choisies"},"volume":{"wt":"I"},"year":{"wt":"1974"}},"i":25}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last1":{"wt":"Suryanarayana"},"first1":{"wt":"D."},"last2":{"wt":"Rao"},"first2":{"wt":"N. Venkateswara"},"mr":{"wt":"0202659"},"journal":{"wt":"J. Indian Math. Soc."},"series":{"wt":"New Series"},"pages":{"wt":"165–167"},"title":{"wt":"On a paper of André Schinzel"},"volume":{"wt":"29"},"year":{"wt":"1965"}},"i":26}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Terzi"},"first":{"wt":"D. G."},"doi":{"wt":"10.1007/BF01934370"},"mr":{"wt":"0297703"},"journal":{"wt":"Nordisk Tidskr. Informationsbehandling"},"pages":{"wt":"212–216"},"title":{"wt":"On a conjecture by Erdős-Straus"},"issue":{"wt":"2"},"volume":{"wt":"11"},"year":{"wt":"1971"},"s2cid":{"wt":"124845157"}},"i":27}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Vaughan"},"first":{"wt":"R. C."},"author-link":{"wt":"Bob Vaughan"},"doi":{"wt":"10.1112/S0025579300002886"},"mr":{"wt":"0289409"},"issue":{"wt":"2"},"journal":{"wt":"[[Mathematika]]"},"pages":{"wt":"193–198"},"title":{"wt":"On a problem of Erdős, Straus and Schinzel"},"volume":{"wt":"17"},"year":{"wt":"1970"}},"i":28}},"\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Webb"},"first":{"wt":"William A."},"title":{"wt":"On <math>4/n=1/x_1+1/x_2+1/x_3</math>"},"journal":{"wt":"[[Proceedings of the American Mathematical Society]]"},"volume":{"wt":"25"},"issue":{"wt":"3"},"pages":{"wt":"578–584"},"year":{"wt":"1970"},"mr":{"wt":"0256984"},"doi":{"wt":"10.2307/2036647"},"publisher":{"wt":"American Mathematical Society"},"jstor":{"wt":"2036647"}},"i":29}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Yamamoto"},"first":{"wt":"Koichi"},"mr":{"wt":"0177945"},"journal":{"wt":"Memoirs of the Faculty of Science. Kyushu University. Series A. Mathematics"},"pages":{"wt":"37–47"},"title":{"wt":"On the Diophantine equation <math>\\tfrac4n=\\tfrac1x+\\tfrac1y+\\tfrac1z</math>"},"volume":{"wt":"19"},"year":{"wt":"1965"},"doi":{"wt":"10.2206/kyushumfs.19.37"},"doi-access":{"wt":"free"}},"i":30}},".\n*",{"template":{"target":{"wt":"citation\n ","href":"./Template:Citation"},"params":{"last":{"wt":"Yang"},"first":{"wt":"Xun Qian"},"doi":{"wt":"10.2307/2044050"},"mr":{"wt":"660589"},"issue":{"wt":"4"},"journal":{"wt":"Proceedings of the American Mathematical Society"},"pages":{"wt":"496–498"},"title":{"wt":"A note on <math>\\tfrac4n=\\tfrac1x+\\tfrac1y+\\tfrac1z</math>"},"volume":{"wt":"85"},"year":{"wt":"1982"},"jstor":{"wt":"2044050"}},"i":31}},".\n",{"template":{"target":{"wt":"refend","href":"./Template:Refend"},"params":{},"i":32}}]}'>

- Ahmadi, M. H.; Bleicher, M. N. (1998), "On the conjectures of Erdős and Straus, and Sierpiński on Egyptian fractions", *International Journal of Mathematical and Statistical Sciences*, **7**(2): 169– 185, [MR][70] [1666363][71].
- Bernstein, Leon (1962), "Zur Lösung der diophantischen Gleichung m / n = 1 / x + 1 / y + 1 / z {\displaystyle m/n=1/x+1/y+1/z}[image: {\displaystyle m/n=1/x+1/y+1/z}], insbesondere im Fall m = 4 {\displaystyle m=4}[image: {\displaystyle m=4}] ", *Journal für die Reine und Angewandte Mathematik*(in German), **211**: 1– 10, [doi][72]: [10.1515/crll.1962.211.1][73], [MR][70] [0142508][74], [S2CID][75] [118098315][76].
- Bright, Martin; Loughran, Daniel (2020), "Brauer–Manin obstruction for Erdős–Straus surfaces", *Bulletin of the London Mathematical Society*, **52**(4): 746– 761, [arXiv][77]: [1908.02526][78], [doi][72]: [10.1112/blms.12374][79], [MR][70] [4171399][80], [S2CID][75] [218959757][81].
- Elsholtz, Christian (2001), "Sums of k {\displaystyle k}[image: {\displaystyle k}] unit fractions", *[Transactions of the American Mathematical Society][82]*, **353**(8): 3209– 3227, [doi][72]: [10.1090/S0002-9947-01-02782-9][83], [MR][70] [1828604][84].
- Elsholtz, Christian; [Tao, Terence][67] (2013), ["Counting the number of solutions to the Erdős–Straus equation on unit fractions"][85] (PDF), *Journal of the Australian Mathematical Society*, **94**(1): 50– 105, [arXiv][77]: [1107.1010][86], [doi][72]: [10.1017/S1446788712000468][87], [MR][70] [3101397][88], [S2CID][75] [17233943][89].
- [Eppstein, David][90] (1995), "Ten algorithms for Egyptian fractions", *Mathematica in Education and Research*, **4**(2): 5– 15. See in particular the ["Small numerators"][91] section
- [Erdős, Paul][7] (1950), [image: {\displaystyle {\tfrac {1}{x_{1}}}+{\tfrac {1}{x_{2}}}+\cdots +{\tfrac {1}{x_{n}}}={\tfrac {a}{b}}}] ["Az 1 x 1 + 1 x 2 + ⋯ + 1 x n = a b {\displaystyle {\tfrac {1}{x_{1}}}+{\tfrac {1}{x_{2}}}+\cdots +{\tfrac {1}{x_{n}}}={\tfrac {a}{b}}} egyenlet egész számú megoldásairól (On a Diophantine Equation)"][92] (PDF), *Mat. Lapok.*(in Hungarian), **1**: 192– 210, [MR][70] [0043117][93].
- [Graham, Ronald L.][94] (2013), ["Paul Erdős and Egyptian fractions"][95] (PDF), in [Lovász, László][96]; [Ruzsa, Imre Z.][97]; [Sós, Vera T.][98] (eds.), *Erdös Centennial*, Bolyai Society Mathematical Studies, vol. 25, Budapest: [János Bolyai Mathematical Society][99], pp. 289– 309, [doi][72]: [10.1007/978-3-642-39286-3_9][100], [ISBN][101] [978-3-642-39285-6][102], [MR][70] [3203600][103]
- [Guy, Richard K.][104] (2004), *Unsolved Problems in Number Theory*(3rd ed.), [Springer Verlag][105], pp. D11, [ISBN][101] [0-387-20860-7][106].
- Hagedorn, Thomas R. (2000), "A proof of a conjecture on Egyptian fractions", *[American Mathematical Monthly][107]*, **107**(1), Mathematical Association of America: 62– 63, [doi][72]: [10.2307/2589381][108], [JSTOR][109] [2589381][110], [MR][70] [1745572][111].
- Hofmeister, Gerd; Stoll, Peter (1985), "Note on Egyptian fractions", *Journal für die Reine und Angewandte Mathematik*, **362**: 141– 145, [MR][70] [0809971][112].
- Ionascu, Eugen J.; Wilson, Andrew (2011), "On the Erdös–Straus conjecture", *Revue Roumaine de Mathématiques Pures et Appliquées*, **56**(1): 21– 30, [arXiv][77]: [1001.1100][113], [MR][70] [2848047][114].
- Jaroma, John H. (2004), [image: {\displaystyle 4/n}] ["On expanding 4 / n {\displaystyle 4/n} into three Egyptian fractions"][115], *[Crux Mathematicorum][116]*, **30**(1): 36– 37.
- Jollensten, Ralph W. (1976), "A note on the Egyptian problem", *Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory, and Computing (Louisiana State Univ., Baton Rouge, La., 1976)*, Congressus Numerantium, vol. XVII, Winnipeg, Man.: Utilitas Math., pp. 351– 364, [MR][70] [0429735][117].
- Kiss, Ernest (1959), "Quelques remarques sur une équation diophantienne", *Acad. R. P. Romîne Fil. Cluj Stud. Cerc. Mat.*(in Romanian), **10**: 59– 62, [MR][70] [0125069][118].
- Kotsireas, Ilias (1999), "The Erdős-Straus conjecture on Egyptian fractions", *Paul Erdős and his mathematics (Budapest, 1999)*, Budapest: János Bolyai Math. Soc., pp. 140– 144, [MR][70] [1901903][119].
- Li, Delang (1981), "On the equation 4 / n = 1 / x + 1 / y + 1 / z {\displaystyle 4/n=1/x+1/y+1/z}[image: {\displaystyle 4/n=1/x+1/y+1/z}] ", *[Journal of Number Theory][120]*, **13**(4): 485– 494, [doi][72]: [10.1016/0022-314X(81)90039-1][121], [MR][70] [0642923][122].
- [Mordell, Louis J.][123] (1967), *Diophantine Equations*, Academic Press, pp. 287– 290.
- Obláth, Richard (1950), "Sur l'équation diophantienne 4 n = 1 x 1 + 1 x 2 + 1 x 3 {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x_{1}}}+{\tfrac {1}{x_{2}}}+{\tfrac {1}{x_{3}}}}[image: {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x_{1}}}+{\tfrac {1}{x_{2}}}+{\tfrac {1}{x_{3}}}}] ", *[Mathesis][124]*(in French), **59**: 308– 316, [MR][70] [0038999][125], M. Strauss [sic] a vérifié l'hypothèse de M. Erdős pour toute valeur de n < 5.000, et M. Shapiro pour n < 20.000. Nos théorèmes donnent la solution pour tout nombre < 106.128.
- Rosati, Luigi Antonio (1954), "Sull'equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 {\displaystyle 4/n=1/x_{1}+1/x_{2}+1/x_{3}}[image: {\displaystyle 4/n=1/x_{1}+1/x_{2}+1/x_{3}}] ", *Boll. Un. Mat. Ital. (3)*(in Italian), **9**: 59– 63, [MR][70] [0060526][126].
- Salez, Serge E. (2014), *The Erdős-Straus conjecture New modular equations and checking up to N = 10 17 {\displaystyle N=10^{17}}[image: {\displaystyle N=10^{17}}]*, [arXiv][77]: [1406.6307][127], [Bibcode][128]: [2014arXiv1406.6307S][129]
- Sander, J. W. (1994), "On 4 / n = 1 / x + 1 / y + 1 / z {\displaystyle 4/n=1/x+1/y+1/z}[image: {\displaystyle 4/n=1/x+1/y+1/z}] and Iwaniec' half-dimensional sieve", *Journal of Number Theory*, **46**(2): 123– 136, [doi][72]: [10.1006/jnth.1994.1008][130], [MR][70] [1269248][131].
- [Schinzel, André][56] (1956), "Sur quelques propriétés des nombres 3 / n {\displaystyle 3/n}[image: {\displaystyle 3/n}] et 4 / n {\displaystyle 4/n}[image: {\displaystyle 4/n}], où n {\displaystyle n}[image: {\displaystyle n}] est un nombre impair", *[Mathesis][124]*(in French), **65**: 219– 222, [MR][70] [0080683][132].
- [Sierpiński, Wacław][55] (1956), "Sur les décompositions de nombres rationnels en fractions primaires", *[Mathesis][124]*(in French), **65**: 16– 32, [MR][70] [0078385][133]. Reprinted with additional annotations in Sierpiński, Wacław (1974), *Oeuvres Choisies*, vol. I, Warsaw: PWN—Éditions Scientifiques de Pologne, pp. 169– 184, [MR][70] [0414302][134].
- Suryanarayana, D.; Rao, N. Venkateswara (1965), "On a paper of André Schinzel", *J. Indian Math. Soc.*, New Series, **29**: 165– 167, [MR][70] [0202659][135].
- Terzi, D. G. (1971), "On a conjecture by Erdős-Straus", *Nordisk Tidskr. Informationsbehandling*, **11**(2): 212– 216, [doi][72]: [10.1007/BF01934370][136], [MR][70] [0297703][137], [S2CID][75] [124845157][138].
- [Vaughan, R. C.][139] (1970), "On a problem of Erdős, Straus and Schinzel", *[Mathematika][140]*, **17**(2): 193– 198, [doi][72]: [10.1112/S0025579300002886][141], [MR][70] [0289409][142]
- Webb, William A. (1970), "On 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 {\displaystyle 4/n=1/x_{1}+1/x_{2}+1/x_{3}}[image: {\displaystyle 4/n=1/x_{1}+1/x_{2}+1/x_{3}}] ", *[Proceedings of the American Mathematical Society][143]*, **25**(3), American Mathematical Society: 578– 584, [doi][72]: [10.2307/2036647][144], [JSTOR][109] [2036647][145], [MR][70] [0256984][146].
- Yamamoto, Koichi (1965), "On the Diophantine equation 4 n = 1 x + 1 y + 1 z {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}[image: {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}] ", *Memoirs of the Faculty of Science. Kyushu University. Series A. Mathematics*, **19**: 37– 47, [doi][72]: [10.2206/kyushumfs.19.37][147], [MR][70] [0177945][148].
- Yang, Xun Qian (1982), "A note on 4 n = 1 x + 1 y + 1 z {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}[image: {\displaystyle {\tfrac {4}{n}}={\tfrac {1}{x}}+{\tfrac {1}{y}}+{\tfrac {1}{z}}}] ", *Proceedings of the American Mathematical Society*, **85**(4): 496– 498, [doi][72]: [10.2307/2044050][149], [JSTOR][109] [2044050][150], [MR][70] [0660589][151].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Erdős–Straus_conjecture&oldid=1367560126][152] "

[Categories][153]:

- [Conjectures][154]
- [Unsolved problems in number theory][155]
- [Egyptian fractions][156]
- [Diophantine equations][157]
- [Paul Erdős][158]

Hidden categories:

- [Articles with short description][159]
- [Short description is different from Wikidata][160]
- [Good articles][161]
- [CS1 German-language sources (de)][162]
- [CS1 Hungarian-language sources (hu)][163]
- [CS1 Romanian-language sources (ro)][164]
- [CS1 French-language sources (fr)][165]
- [CS1 Italian-language sources (it)][166]

Search

Erdős–Straus conjecture

16 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Wikipedia:Good_articles*
[2]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[3]: https://en.wikipedia.org/wiki/Open_problem
[4]: https://en.wikipedia.org/wiki/Number_theory
[5]: https://en.wikipedia.org/wiki/Integer
[6]: https://en.wikipedia.org/wiki/Unit_fraction
[7]: https://en.wikipedia.org/wiki/Paul_Erdős
[8]: https://en.wikipedia.org/wiki/Ernst_G._Straus
[9]: https://en.wikipedia.org/wiki/Egyptian_fraction
[10]: https://en.wikipedia.org/wiki/Ancient_Egyptian_mathematics
[11]: https://en.wikipedia.org/wiki/Erdős_conjecture
[12]: https://en.wikipedia.org/wiki/Diophantine_equation
[13]: https://en.wikipedia.org/wiki/Arithmetic_progression
[14]: https://en.wikipedia.org/wiki/Counterexample
[15]: https://en.wikipedia.org/wiki/Prime_number
[16]: https://en.wikipedia.org/wiki/Prime_factor
[17]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=1
[18]: https://en.wikipedia.org/wiki/Rational_number
[19]: https://en.wikipedia.org/wiki/Egyptian_mathematics
[20]: https://en.wikipedia.org/wiki/Vulgar_fraction
[21]: https://en.wikipedia.org/wiki/Rhind_Mathematical_Papyrus_2/n_table
[22]: https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions
[23]: https://en.wikipedia.org/wiki/Fibonacci
[24]: https://en.wikipedia.org/wiki/Liber_Abaci
[25]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=2
[26]: https://en.wikipedia.org/wiki/Polynomial
[27]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=3
[28]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=4
[29]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=5
[30]: https://en.wikipedia.org/wiki/Brute-force_search
[31]: https://en.wikipedia.org/wiki/Composite_number
[32]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=6
[33]: https://en.wikipedia.org/wiki/Polynomial_equation
[34]: https://en.wikipedia.org/wiki/Hasse_principle
[35]: https://en.wikipedia.org/wiki/Modular_arithmetic
[36]: https://en.wikipedia.org/wiki/Prime_power
[37]: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
[38]: https://en.wikipedia.org/wiki/Manin_obstruction
[39]: https://en.wikipedia.org/wiki/Natural_number
[40]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=7
[41]: https://en.wikipedia.org/wiki/Natural_density
[42]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=8
[43]: https://en.wikipedia.org/wiki/Covering_system
[44]: https://en.wikipedia.org/wiki/Quadratic_residue
[45]: https://en.wikipedia.org/wiki/Hasse–Minkowski_theorem
[46]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=9
[47]: https://en.wikipedia.org/wiki/Upper_bound
[48]: https://en.wikipedia.org/wiki/Polylogarithmic
[49]: https://en.wikipedia.org/wiki/Asymptotic
[50]: https://en.wikipedia.org/wiki/Lower_bound
[51]: https://en.wikipedia.org/wiki/Bombieri–Vinogradov_theorem
[52]: https://en.wikipedia.org/wiki/Brun–Titchmarsh_theorem
[53]: https://en.wikipedia.org/wiki/Coprime
[54]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=10
[55]: https://en.wikipedia.org/wiki/Wacław_Sierpiński
[56]: https://en.wikipedia.org/wiki/Andrzej_Schinzel
[57]: https://en.wikipedia.org/wiki/Odd_number
[58]: https://en.wikipedia.org/wiki/Odd_greedy_expansion
[59]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=11
[60]: https://en.wikipedia.org/wiki/List_of_sums_of_reciprocals
[61]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=12
[62]: https://www.ics.uci.edu/~eppstein/numth/egypt/conflict.html
[63]: https://en.wikipedia.org/wiki/Neil_Sloane
[64]: https://oeis.org/A073101
[65]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[66]: https://terrytao.wordpress.com/2011/07/07/on-the-number-of-solutions-to-4p-1n_1-1n_2-1n_3/
[67]: https://en.wikipedia.org/wiki/Terence_Tao
[68]: https://terrytao.wordpress.com/2011/07/31/counting-the-number-of-solutions-to-the-erdos-straus-equation-on-unit-fractions/
[69]: /w/index.php?title=Erd%C5%91s%E2%80%93Straus_conjecture&amp;action=edit&amp;section=13
[70]: https://en.wikipedia.org/wiki/MR_(identifier)
[71]: https://mathscinet.ams.org/mathscinet-getitem?mr=1666363
[72]: https://en.wikipedia.org/wiki/Doi_(identifier)
[73]: https://doi.org/10.1515%2Fcrll.1962.211.1
[74]: https://mathscinet.ams.org/mathscinet-getitem?mr=0142508
[75]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[76]: https://api.semanticscholar.org/CorpusID:118098315
[77]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[78]: https://arxiv.org/abs/1908.02526
[79]: https://doi.org/10.1112%2Fblms.12374
[80]: https://mathscinet.ams.org/mathscinet-getitem?mr=4171399
[81]: https://api.semanticscholar.org/CorpusID:218959757
[82]: https://en.wikipedia.org/wiki/Transactions_of_the_American_Mathematical_Society
[83]: https://doi.org/10.1090%2FS0002-9947-01-02782-9
[84]: https://mathscinet.ams.org/mathscinet-getitem?mr=1828604
[85]: https://terrytao.files.wordpress.com/2011/07/egyptian-count13.pdf
[86]: https://arxiv.org/abs/1107.1010
[87]: https://doi.org/10.1017%2FS1446788712000468
[88]: https://mathscinet.ams.org/mathscinet-getitem?mr=3101397
[89]: https://api.semanticscholar.org/CorpusID:17233943
[90]: https://en.wikipedia.org/wiki/David_Eppstein
[91]: https://www.ics.uci.edu/~eppstein/numth/egypt/smallnum.html
[92]: https://www.renyi.hu/~p_erdos/1950-02.pdf
[93]: https://mathscinet.ams.org/mathscinet-getitem?mr=0043117
[94]: https://en.wikipedia.org/wiki/Ronald_Graham
[95]: https://www.math.ucsd.edu/~ronspubs/13_03_Egyptian.pdf
[96]: https://en.wikipedia.org/wiki/László_Lovász
[97]: https://en.wikipedia.org/wiki/Imre_Z._Ruzsa
[98]: https://en.wikipedia.org/wiki/Vera_T._Sós
[99]: https://en.wikipedia.org/wiki/János_Bolyai_Mathematical_Society
[100]: https://doi.org/10.1007%2F978-3-642-39286-3_9
[101]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[102]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-39285-6
[103]: https://mathscinet.ams.org/mathscinet-getitem?mr=3203600
[104]: https://en.wikipedia.org/wiki/Richard_K._Guy
[105]: https://en.wikipedia.org/wiki/Springer_Verlag
[106]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-20860-7
[107]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[108]: https://doi.org/10.2307%2F2589381
[109]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[110]: https://www.jstor.org/stable/2589381
[111]: https://mathscinet.ams.org/mathscinet-getitem?mr=1745572
[112]: https://mathscinet.ams.org/mathscinet-getitem?mr=0809971
[113]: https://arxiv.org/abs/1001.1100
[114]: https://mathscinet.ams.org/mathscinet-getitem?mr=2848047
[115]: https://cms.math.ca/publications/crux/issue/?volume=30&amp;issue=1
[116]: https://en.wikipedia.org/wiki/Crux_Mathematicorum
[117]: https://mathscinet.ams.org/mathscinet-getitem?mr=0429735
[118]: https://mathscinet.ams.org/mathscinet-getitem?mr=0125069
[119]: https://mathscinet.ams.org/mathscinet-getitem?mr=1901903
[120]: https://en.wikipedia.org/wiki/Journal_of_Number_Theory
[121]: https://doi.org/10.1016%2F0022-314X%2881%2990039-1
[122]: https://mathscinet.ams.org/mathscinet-getitem?mr=0642923
[123]: https://en.wikipedia.org/wiki/Louis_Mordell
[124]: https://en.wikipedia.org/wiki/Mathesis_(journal)
[125]: https://mathscinet.ams.org/mathscinet-getitem?mr=0038999
[126]: https://mathscinet.ams.org/mathscinet-getitem?mr=0060526
[127]: https://arxiv.org/abs/1406.6307
[128]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[129]: https://ui.adsabs.harvard.edu/abs/2014arXiv1406.6307S
[130]: https://doi.org/10.1006%2Fjnth.1994.1008
[131]: https://mathscinet.ams.org/mathscinet-getitem?mr=1269248
[132]: https://mathscinet.ams.org/mathscinet-getitem?mr=0080683
[133]: https://mathscinet.ams.org/mathscinet-getitem?mr=0078385
[134]: https://mathscinet.ams.org/mathscinet-getitem?mr=0414302
[135]: https://mathscinet.ams.org/mathscinet-getitem?mr=0202659
[136]: https://doi.org/10.1007%2FBF01934370
[137]: https://mathscinet.ams.org/mathscinet-getitem?mr=0297703
[138]: https://api.semanticscholar.org/CorpusID:124845157
[139]: https://en.wikipedia.org/wiki/Bob_Vaughan
[140]: https://en.wikipedia.org/wiki/Mathematika
[141]: https://doi.org/10.1112%2FS0025579300002886
[142]: https://mathscinet.ams.org/mathscinet-getitem?mr=0289409
[143]: https://en.wikipedia.org/wiki/Proceedings_of_the_American_Mathematical_Society
[144]: https://doi.org/10.2307%2F2036647
[145]: https://www.jstor.org/stable/2036647
[146]: https://mathscinet.ams.org/mathscinet-getitem?mr=0256984
[147]: https://doi.org/10.2206%2Fkyushumfs.19.37
[148]: https://mathscinet.ams.org/mathscinet-getitem?mr=0177945
[149]: https://doi.org/10.2307%2F2044050
[150]: https://www.jstor.org/stable/2044050
[151]: https://mathscinet.ams.org/mathscinet-getitem?mr=0660589
[152]: https://en.wikipedia.org/w/index.php?title=Erdős–Straus_conjecture&amp;oldid=1367560126
[153]: /wiki/Help:Category
[154]: /wiki/Category:Conjectures
[155]: /wiki/Category:Unsolved_problems_in_number_theory
[156]: /wiki/Category:Egyptian_fractions
[157]: /wiki/Category:Diophantine_equations
[158]: /wiki/Category:Paul_Erd%C5%91s
[159]: /wiki/Category:Articles_with_short_description
[160]: /wiki/Category:Short_description_is_different_from_Wikidata
[161]: /wiki/Category:Good_articles
[162]: /wiki/Category:CS1_German-language_sources_(de)
[163]: /wiki/Category:CS1_Hungarian-language_sources_(hu)
[164]: /wiki/Category:CS1_Romanian-language_sources_(ro)
[165]: /wiki/Category:CS1_French-language_sources_(fr)
[166]: /wiki/Category:CS1_Italian-language_sources_(it)
