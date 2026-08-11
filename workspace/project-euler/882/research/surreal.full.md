<!-- source: https://en.wikipedia.org/wiki/Surreal_number | converted from HTML -->

Surreal number - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Generalization of the real numbers

[1] A visualization of the surreal number tree

In [mathematics][2], the **surreal number**system is a [totally ordered][3] [proper class][4] containing not only the [real numbers][5] but also [infinite][6] and [infinitesimal numbers][7], respectively larger or smaller in [absolute value][8] than any positive real number. Research on the [Go endgame][9] by [John Horton Conway][10] led to the original definition and construction of surreal numbers. Conway's construction was introduced in [Donald Knuth][11] 's 1974 book *Surreal Numbers: How Two Ex-Students Turned On to Pure Mathematics and Found Total Happiness*. [1]

The surreals share many properties with the reals, including the usual arithmetic operations (addition, subtraction, multiplication, and division); as such, they form an [ordered field][12]. [a] If formulated in [von Neumann–Bernays–Gödel set theory][13], the surreal numbers are a universal ordered field in the sense that all other ordered fields, such as the rationals, the reals, the [rational functions][14], the [Levi-Civita field][15], the [superreal numbers][16] (including the [hyperreal numbers][17]) can be realized as subfields of the surreals. [2] The surreals also contain all [transfinite][18] [ordinal numbers][19]; the arithmetic on them is given by the [natural operations][20]. It has also been shown (in von Neumann–Bernays–Gödel set theory) that the maximal class hyperreal field is [isomorphic][21] to the maximal class surreal field.

## History of the concept

[[edit][22]]

Research on the [Go endgame][23] by [John Horton Conway][10] led to the original definition and construction of the surreal numbers. [3] Conway's construction was introduced in [Donald Knuth][11] 's 1974 book *Surreal Numbers: How Two Ex-Students Turned On to Pure Mathematics and Found Total Happiness*. [1] In his book, which takes the form of a dialogue, Knuth coined the term *surreal numbers*for what Conway had called simply *numbers*. Conway later adopted Knuth's term, and used surreals for analyzing games in his 1976 book *[On Numbers and Games][24]*.

A separate route to defining the surreals began in 1907, when [Hans Hahn][25] introduced [Hahn series][26] as a generalization of [formal power series][27], and [Felix Hausdorff][28] introduced certain ordered sets called ****[η α -sets][29] for ordinals α and asked if it was possible to find a compatible ordered group or field structure. In 1962, Norman Alling used a modified form of Hahn series to construct such ordered fields associated to certain ordinals α and, in 1987, he showed that taking α to be the class of all ordinals in his construction gives a class that is an ordered field isomorphic to the surreal numbers. [4]

If the surreals are considered as 'just' a proper-class-sized real closed field, Alling's 1962 paper handles the case of [strongly inaccessible][30] cardinals which can naturally be considered as proper classes by cutting off the [cumulative hierarchy of the universe][31] one stage above the cardinal, and Alling accordingly deserves much credit for the discovery/invention of the surreals in this sense. [*[citation needed][32]*] There is an important additional field structure on the surreals that is not visible through this lens, however, namely the notion of a 'birthday' and the corresponding natural description of the surreals as the result of a cut-filling process along their birthdays given by Conway. This additional structure has become fundamental to a modern understanding of the surreal numbers, and Conway is thus given credit for discovering the surreals as we know them today—Alling himself gives Conway full credit in a 1985 paper preceding his book on the subject. [5]

## Description

[[edit][33]]

### Notation

[[edit][34]]

In the context of surreal numbers, an [ordered pair][35] of sets of surreal numbers, L and R, which is written as (*L*, *R*) in many other mathematical contexts, is instead written { *L*| *R*} including the extra space adjacent to each brace. When L or R is explicitly described by its elements, the pair of braces that encloses the set of surreal elements is often omitted. When L or R is empty, it is often simply omitted. For example, instead of ({0, 1, 2}, {}), which is common notation in other contexts, we typically write { 0, 1, 2 | }, where 0, 1, and 2 are surreal numbers.

### Outline of construction

[[edit][36]]

In the Conway construction, [6] the surreal numbers are constructed in stages, along with an ordering ≤ such that for any two surreal numbers a and b, *a*≤ *b*or *b*≤ *a*. (Both may hold, in which case a and b are equivalent and denote the same number.) Each number is formed from an ordered pair of subsets of numbers already constructed: given subsets L and R of numbers such that all the members of L are strictly less than all the members of R, then the pair { *L*| *R*} represents a number intermediate in value between all the members of L and all the members of R. According to Conway, intermediate values must be governed by his rule of simplicity. That is, numbers born on subsequent birthdays must be the simplest between the new and the prior day. For example, on day 1, -1 and 1 are born. On day 2, the simplest number between 1 and 0 is 1/2; between 0 and -1 is -1/2. Different subsets may end up defining the same number: { *L*| *R*} and { *L ′*| *R ′*} may define the same number even if *L*≠ *L ′*and *R*≠ *R ′*. (A similar phenomenon occurs when [rational numbers][37] are defined as quotients of integers: ⁠ 1 / 2 ⁠ and ⁠ 2 / 4 ⁠ are different representations of the same rational number.) Each surreal number is an [equivalence class][38] of representations of the form { *L*| *R*} that designate the same number, noting that each equivalence class is a [proper class][4] rather than a set.

In the first stage of construction, there are no previously existing numbers so the only representation must use the [empty set][39]: { | }. This representation, where L and R are both empty, is called 0. Subsequent stages yield forms like

\n{{math|1={{mset| 1 {{!}} }} = 2}}<br />\n{{math|1={{mset| 2 {{!}} }} = 3}}"}},"i":0}}]}'>

{ 0 | } = 1

{ 1 | } = 2

{ 2 | } = 3

and

\n{{math|1={{mset| {{!}} −1 }} = −2}}<br />\n{{math|1={{mset| {{!}} −2 }} = −3}}"}},"i":0}}]}'>

{ | 0 } = −1

{ | −1 } = −2

{ | −2 } = −3

The integers are thus contained within the surreal numbers. (The above identities are definitions, in the sense that the right-hand side is a name for the left-hand side. That the names are actually appropriate will be evident when the arithmetic operations on surreal numbers are defined, as in the section below.) Similarly, representations such as

\n{{math|1={{mset| 0 {{!}} {{sfrac|1|2}} }} = {{sfrac|1|4}}}}<br />\n{{math|1={{mset| {{sfrac|1|2}} {{!}} 1 }} = {{sfrac|3|4}}}}"}},"i":0}}]}'>

{ 0 | 1 } = ⁠ 1 / 2 ⁠

{ 0 | ⁠ 1 / 2 ⁠ } = ⁠ 1 / 4 ⁠

{ ⁠ 1 / 2 ⁠ | 1 } = ⁠ 3 / 4 ⁠

arise, so that the [dyadic rationals][40] (rational numbers whose denominators are powers of 2) are contained within the surreal numbers.

After an infinite number of stages, infinite subsets become available, so that any [real number][5] a can be represented by { *L**a*| *R**a*}, where *L**a*is the set of all dyadic rationals less than a and *R**a*is the set of all dyadic rationals greater than a (reminiscent of a [Dedekind cut][41]). Thus the real numbers are also embedded within the surreals.

There are also representations like

\n{{math|1={{mset| 0 {{!}} 1, {{sfrac|1|2}}, {{sfrac|1|4}}, {{sfrac|1|8}}, ... }} = ε}}"}},"i":0}}]}'>

{ 0, 1, 2, 3, ... | } = *ω*
{ 0 | 1, ⁠ 1 / 2 ⁠, ⁠ 1 / 4 ⁠, ⁠ 1 / 8 ⁠, ... } = ε

where ω is a transfinite number greater than all integers and ε is an infinitesimal greater than 0 but less than any positive real number. Moreover, the standard arithmetic operations (addition, subtraction, multiplication, and division) can be extended to these non-real numbers in a manner that turns the collection of surreal numbers into an ordered field, so that one can talk about 2*ω*or *ω*− 1 and so forth.

## Construction

[[edit][42]]

Surreal numbers are [constructed inductively][43] as [equivalence classes][38] of [pairs][35] of sets of surreal numbers, restricted by the condition that each element of the first set is smaller than each element of the second set. The construction consists of three interdependent parts: the construction rule, the comparison rule and the equivalence rule.

### Forms

[[edit][44]]

A *form*is a pair of sets of surreal numbers, called its *left set*and its *right set*. A form with left set L and right set R is written { *L*| *R*}. When L and R are given as lists of elements, the braces around them are omitted.

Either or both of the left and right set of a form may be the empty set. The form { { } | { } } with both left and right set empty is also written { | }.

### Numeric forms and their equivalence classes

[[edit][45]]

**Construction rule**

A form { *L*| *R*} is *numeric*if the intersection of L and R is the empty set and each element of R is greater than every element of L, according to the [order relation][46] ≤ given by the comparison rule below.

The numeric forms are placed in equivalence classes; each such equivalence class is a *surreal number*. The elements of the left and right sets of a form are drawn from the universe of the surreal numbers (not of *forms*, but of their *equivalence classes*).

**Equivalence rule**

Two numeric forms x and y are forms of the same number (lie in the same equivalence class) if and only if both *x*≤ *y*and *y*≤ *x*.

An [ordering relationship][46] must be [antisymmetric][47], i.e., it must have the property that *x*= *y*(i. e., *x*≤ *y*and *y*≤ *x*are both true) only when x and y are the same object. This is not the case for surreal number *forms*, but is true by construction for surreal *numbers*(equivalence classes).

The equivalence class containing { | } is labeled 0; in other words, { | } is a form of the surreal number 0.

### Order

[[edit][48]]

The recursive definition of surreal numbers is completed by defining comparison:

Given numeric forms *x*= { *X**L*| *X**R*} and *y*= { *Y**L*| *Y**R*}, *x*≤ *y*[if and only if][49] both:

- There is no *x**L*∈ *X**L*such that *y*≤ *x**L*. That is, every element in the left part of x is strictly smaller than y.
- There is no *y**R*∈ *Y**R*such that *y**R*≤ *x*. That is, every element in the right part of y is strictly larger than x.

Surreal numbers can be compared to each other (or to numeric forms) by choosing a numeric form from its equivalence class to represent each surreal number.

### Induction

[[edit][50]]

This group of definitions is [recursive][51], and requires some form of [mathematical induction][52] to define the universe of objects (forms and numbers) that occur in them. The only surreal numbers reachable via *finite induction*are the [dyadic fractions][40]; a wider universe is reachable given some form of [transfinite induction][53].

#### Induction rule

[[edit][54]]

- There is a generation *S*0 = { 0 }, in which 0 consists of the single form { | }.
- Given any [ordinal number][19] n, the generation *S**n*is the set of all surreal numbers that are generated by the construction rule from subsets of ⋃ i < n S i {\textstyle \bigcup _{i<n}S_{i}}[image: {\textstyle \bigcup _{i<n}S_{i}}].

The base case is actually a special case of the induction rule, with 0 taken as a label for the "least ordinal". Since there exists no *S**i*with *i*< 0, the expression ⋃ i < 0 S i {\textstyle \bigcup _{i<0}S_{i}}[image: {\textstyle \bigcup _{i<0}S_{i}}] is the empty set; the only subset of the empty set is the empty set, and therefore *S*0 consists of a single surreal form { | } lying in a single equivalence class 0.

For every finite ordinal number n, *S**n*is [well-ordered][55] by the ordering induced by the comparison rule on the surreal numbers.

The first iteration of the induction rule produces the three numeric forms { | 0 } < { | } < { 0 | } (the form { 0 | 0 } is non-numeric because 0 ≤ 0). The equivalence class containing { 0 | } is labeled 1 and the equivalence class containing { | 0 } is labeled −1. These three labels have a special significance in the axioms that define a [ring][56]; they are the additive identity (0), the multiplicative identity (1), and the [additive inverse][57] of 1 (−1). The arithmetic operations defined below are consistent with these labels.

For every *i*< *n*, since every valid form in *S**i*is also a valid form in *S**n*, all of the numbers in *S**i*also appear in *S**n*(as supersets of their representation in *S**i*). (The set union expression appears in our construction rule, rather than the simpler form *S**n*−1, so that the definition also makes sense when n is a [limit ordinal][58].) Numbers in *S**n*that are a superset of some number in *S**i*are said to have been *inherited*from generation i. The smallest value of α for which a given surreal number appears in *S**α*is called its *birthday*. For example, the birthday of 0 is 0, and the birthday of −1 is 1.

A second iteration of the construction rule yields the following ordering of equivalence classes:

\n{{math|1=< {{mset| {{!}} 0 }} = {{mset| {{!}} 0, 1 }}}}<br />\n{{math|1=< {{mset| −1 {{!}} 0 }} = {{mset| −1 {{!}} 0, 1 }}}}<br />\n{{math|1=< {{mset| {{!}} }} = {{mset| −1 {{!}} }} = {{mset| {{!}} 1 }} = {{mset| −1 {{!}} 1 }}}}<br />\n{{math|1=< {{mset| 0 {{!}} 1 }} = {{mset| −1, 0 {{!}} 1 }}}}<br />\n{{math|1=< {{mset| 0 {{!}} }} = {{mset| −1, 0 {{!}} }}}}<br />\n{{math|1=< {{mset| 1 {{!}} }} = {{mset| 0, 1 {{!}} }} = {{mset| −1, 1 {{!}} }} = {{mset| −1, 0, 1 {{!}} }}}}"}},"i":0}}]}'>

{ | −1 } = { | −1, 0 } = { | −1, 1 } = { | −1, 0, 1 }

< { | 0 } = { | 0, 1 }
< { −1 | 0 } = { −1 | 0, 1 }
< { | } = { −1 | } = { | 1 } = { −1 | 1 }
< { 0 | 1 } = { −1, 0 | 1 }
< { 0 | } = { −1, 0 | }

< { 1 | } = { 0, 1 | } = { −1, 1 | } = { −1, 0, 1 | }

Comparison of these equivalence classes is consistent, irrespective of the choice of form. Three observations follow:

1. *S*2 contains four new surreal numbers. Two contain extremal forms: { | −1, 0, 1 } contains all numbers from previous generations in its right set, and { −1, 0, 1 | } contains all numbers from previous generations in its left set. The others have a form that partitions all numbers from previous generations into two non-empty sets.
2. Every surreal number x that existed in the previous "generation" exists also in this generation, and includes at least one new form: a partition of all numbers *other than*x from previous generations into a left set (all numbers less than x) and a right set (all numbers greater than x).
3. The equivalence class of a number depends on only the maximal element of its left set and the minimal element of the right set.

The informal interpretations of { 1 | } and { | −1 } are "the number just after 1" and "the number just before −1" respectively; their equivalence classes are labeled 2 and −2. The informal interpretations of { 0 | 1 } and { −1 | 0 } are "the simplest number between 0 and 1" and "the simplest number between −1 and 0" respectively; their equivalence classes are labeled ⁠ 1 / 2 ⁠ and − ⁠ 1 / 2 ⁠. These labels will also be justified by the rules for surreal addition and multiplication below.

The equivalence classes at each stage n of induction may be characterized by their n -*complete forms*(each containing as many elements as possible of previous generations in its left and right sets). Either this complete form contains *every*number from previous generations in its left or right set, in which case this is the first generation in which this number occurs; or it contains all numbers from previous generations but one, in which case it is a new form of this one number. We retain the labels from the previous generation for these "old" numbers, and write the ordering above using the old and new labels:

−2 < −1 < − ⁠ 1 / 2 ⁠ < 0 < ⁠ 1 / 2 ⁠ < 1 < 2.

The third observation extends to all surreal numbers with finite left and right sets. (For infinite left or right sets, this is valid in an altered form, since infinite sets might not contain a maximal or minimal element.) The number { 1, 2 | 5, 8 } is therefore equivalent to { 2 | 5 }; one can establish that these are forms of 3 by using the *birthday property*, which is a consequence of the rules above.

#### Birthday property

[[edit][59]]

A form *x*= { *L*| *R*} occurring in generation n represents a number inherited from an earlier generation *i*< *n*if and only if there is some number in *S**i*that is greater than all elements of L and less than all elements of the R. (In other words, if L and R are already separated by a number created at an earlier stage, then x does not represent a new number but one already constructed.) If x represents a number from any generation earlier than n, there is a least such generation i, and between L and R lies exactly one number c that has this least i as its birthday. x is a form of this c. In other words, it lies in the equivalence class in *S**n*that is a superset of the representation of c in generation i.

## Arithmetic

[[edit][60]]

The addition, negation (additive inverse), and multiplication of surreal number *forms**x*= { *X**L*| *X**R*} and *y*= { *Y**L*| *Y**R*} are defined by three recursive formulas.

### Negation

[[edit][61]]

Negation of a given number *x*= { *X**L*| *X**R*} is defined by − x = − { X L ∣ X R } = { − X R ∣ − X L }, {\displaystyle -x=-\{X_{L}\mid X_{R}\}=\{-X_{R}\mid -X_{L}\},}[image: {\displaystyle -x=-\{X_{L}\mid X_{R}\}=\{-X_{R}\mid -X_{L}\},}] where the negation of a set S of numbers is given by the set of the negated elements of S: − S = { − s: s ∈ S }. {\displaystyle -S=\{-s:s\in S\}.}[image: {\displaystyle -S=\{-s:s\in S\}.}]

This formula involves the negation of the surreal *numbers*appearing in the left and right sets of x, which is to be understood as the result of choosing a form of the number, evaluating the negation of this form, and taking the equivalence class of the resulting form. This makes sense only if the result is the same, irrespective of the choice of form of the operand. This can be proved inductively using the fact that the numbers occurring in *X**L*and *X**R*are drawn from generations earlier than that in which the form x first occurs, and observing the special case: − 0 = − { ∣ } = { ∣ } = 0. {\displaystyle -0=-\{{}\mid {}\}=\{{}\mid {}\}=0.}[image: {\displaystyle -0=-\{{}\mid {}\}=\{{}\mid {}\}=0.}]

### Addition

[[edit][62]]

The definition of addition is also a recursive formula: x + y = { X L ∣ X R } + { Y L ∣ Y R } = { X L + y, x + Y L ∣ X R + y, x + Y R }, {\displaystyle x+y=\{X_{L}\mid X_{R}\}+\{Y_{L}\mid Y_{R}\}=\{X_{L}+y,x+Y_{L}\mid X_{R}+y,x+Y_{R}\},}[image: {\displaystyle x+y=\{X_{L}\mid X_{R}\}+\{Y_{L}\mid Y_{R}\}=\{X_{L}+y,x+Y_{L}\mid X_{R}+y,x+Y_{R}\},}] where

X + y = { x ′ + y: x ′ ∈ X }, x + Y = { x + y ′: y ′ ∈ Y } {\displaystyle X+y=\{x'+y:x'\in X\},\quad x+Y=\{x+y':y'\in Y\}}[image: {\displaystyle X+y=\{x'+y:x'\in X\},\quad x+Y=\{x+y':y'\in Y\}}]

This formula involves sums of one of the original operands and a surreal number drawn from the left or right set of the other. It can be proved inductively with the special cases: 0 + 0 = { ∣ } + { ∣ } = { ∣ } = 0 {\displaystyle 0+0=\{{}\mid {}\}+\{{}\mid {}\}=\{{}\mid {}\}=0}[image: {\displaystyle 0+0=\{{}\mid {}\}+\{{}\mid {}\}=\{{}\mid {}\}=0}] x + 0 = x + { ∣ } = { X L + 0 ∣ X R + 0 } = { X L ∣ X R } = x {\displaystyle x+0=x+\{{}\mid {}\}=\{X_{L}+0\mid X_{R}+0\}=\{X_{L}\mid X_{R}\}=x}[image: {\displaystyle x+0=x+\{{}\mid {}\}=\{X_{L}+0\mid X_{R}+0\}=\{X_{L}\mid X_{R}\}=x}] 0 + y = { ∣ } + y = { 0 + Y L ∣ 0 + Y R } = { Y L ∣ Y R } = y {\displaystyle 0+y=\{{}\mid {}\}+y=\{0+Y_{L}\mid 0+Y_{R}\}=\{Y_{L}\mid Y_{R}\}=y}[image: {\displaystyle 0+y=\{{}\mid {}\}+y=\{0+Y_{L}\mid 0+Y_{R}\}=\{Y_{L}\mid Y_{R}\}=y}]

For example:

⁠ 1 / 2 ⁠ + ⁠ 1 / 2 ⁠ = { 0 | 1 } + { 0 | 1 } = { ⁠ 1 / 2 ⁠ | ⁠ 3 / 2 ⁠ },

which by the birthday property is a form of 1. This justifies the label used in the previous section.

#### Subtraction

[[edit][63]]

Subtraction is defined with addition and negation: x − y = { X L ∣ X R } + { − Y R ∣ − Y L } = { X L − y, x − Y R ∣ X R − y, x − Y L }. {\displaystyle x-y=\{X_{L}\mid X_{R}\}+\{-Y_{R}\mid -Y_{L}\}=\{X_{L}-y,x-Y_{R}\mid X_{R}-y,x-Y_{L}\}\,.}[image: {\displaystyle x-y=\{X_{L}\mid X_{R}\}+\{-Y_{R}\mid -Y_{L}\}=\{X_{L}-y,x-Y_{R}\mid X_{R}-y,x-Y_{L}\}\,.}]

### Multiplication

[[edit][64]]

Multiplication can be defined recursively as well, beginning from the special cases involving 0, the [multiplicative identity][65] 1, and its additive inverse −1: x y = { X L ∣ X R } { Y L ∣ Y R } = { X L y + x Y L − X L Y L, X R y + x Y R − X R Y R ∣ X L y + x Y R − X L Y R, x Y L + X R y − X R Y L } {\displaystyle {\begin{aligned}xy&=\{X_{L}\mid X_{R}\}\{Y_{L}\mid Y_{R}\}\\&=\left\{X_{L}y+xY_{L}-X_{L}Y_{L},X_{R}y+xY_{R}-X_{R}Y_{R}\mid X_{L}y+xY_{R}-X_{L}Y_{R},xY_{L}+X_{R}y-X_{R}Y_{L}\right\}\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}xy&=\{X_{L}\mid X_{R}\}\{Y_{L}\mid Y_{R}\}\\&=\left\{X_{L}y+xY_{L}-X_{L}Y_{L},X_{R}y+xY_{R}-X_{R}Y_{R}\mid X_{L}y+xY_{R}-X_{L}Y_{R},xY_{L}+X_{R}y-X_{R}Y_{L}\right\}\\\end{aligned}}}] The formula contains arithmetic expressions involving the operands and their left and right sets, such as the expression X R y + x Y R − X R Y R {\textstyle X_{R}y+xY_{R}-X_{R}Y_{R}}[image: {\textstyle X_{R}y+xY_{R}-X_{R}Y_{R}}] that appears in the left set of the product of x and y. This is understood as { x ′ y + x y ′ − x ′ y ′: x ′ ∈ X R, y ′ ∈ Y R } {\textstyle \left\{x'y+xy'-x'y':x'\in X_{R},~y'\in Y_{R}\right\}}[image: {\textstyle \left\{x'y+xy'-x'y':x'\in X_{R},~y'\in Y_{R}\right\}}], the set of numbers generated by picking all possible combinations of members of X R {\textstyle X_{R}}[image: {\textstyle X_{R}}] and Y R {\textstyle Y_{R}}[image: {\textstyle Y_{R}}], and substituting them into the expression.

For example, to show that the square of ⁠ 1 / 2 ⁠ is ⁠ 1 / 4 ⁠:

⁠ 1 / 2 ⁠ ⋅ ⁠ 1 / 2 ⁠ = { 0 | 1 } ⋅ { 0 | 1 } = { 0 | ⁠ 1 / 2 ⁠ } = ⁠ 1 / 4 ⁠.

### Division

[[edit][66]]

The definition of division is done in terms of the reciprocal and multiplication:

x y = x ⋅ 1 y {\displaystyle {\frac {x}{y}}=x\cdot {\frac {1}{y}}}[image: {\displaystyle {\frac {x}{y}}=x\cdot {\frac {1}{y}}}]

where [6]: 21

1 y = { 0, 1 + ( y R − y) ( 1 y) L y R, 1 + ( y L − y) ( 1 y) R y L | 1 + ( y L − y) ( 1 y) L y L, 1 + ( y R − y) ( 1 y) R y R } {\displaystyle {\frac {1}{y}}=\left\{\left.0,{\frac {1+(y_{R}-y)\left({\frac {1}{y}}\right)_{L}}{y_{R}}},{\frac {1+\left(y_{L}-y\right)\left({\frac {1}{y}}\right)_{R}}{y_{L}}}\,\,\right|\,\,{\frac {1+(y_{L}-y)\left({\frac {1}{y}}\right)_{L}}{y_{L}}},{\frac {1+(y_{R}-y)\left({\frac {1}{y}}\right)_{R}}{y_{R}}}\right\}}[image: {\displaystyle {\frac {1}{y}}=\left\{\left.0,{\frac {1+(y_{R}-y)\left({\frac {1}{y}}\right)_{L}}{y_{R}}},{\frac {1+\left(y_{L}-y\right)\left({\frac {1}{y}}\right)_{R}}{y_{L}}}\,\,\right|\,\,{\frac {1+(y_{L}-y)\left({\frac {1}{y}}\right)_{L}}{y_{L}}},{\frac {1+(y_{R}-y)\left({\frac {1}{y}}\right)_{R}}{y_{R}}}\right\}}]

for positive y. Only positive *y**L*are permitted in the formula, with any nonpositive terms being ignored (and *y**R*are always positive). This formula involves not only recursion in terms of being able to divide by numbers from the left and right sets of y, but also recursion in that the members of the left and right sets of ⁠ 1 /*y*⁠ itself. 0 is always a member of the left set of ⁠ 1 /*y*⁠, and that can be used to find more terms in a recursive fashion. For example, if *y*= 3 = { 2 | }, then we know a left term of ⁠ 1 / 3 ⁠ will be 0. This in turn means ⁠ 1 + (2 − 3)0 / 2 ⁠ = ⁠ 1 / 2 ⁠ is a right term. This means 1 + ( 2 − 3) ( 1 2) 2 = 1 4 {\displaystyle {\frac {1+(2-3)\left({\frac {1}{2}}\right)}{2}}={\frac {1}{4}}}[image: {\displaystyle {\frac {1+(2-3)\left({\frac {1}{2}}\right)}{2}}={\frac {1}{4}}}] is a left term. This means 1 + ( 2 − 3) ( 1 4) 2 = 3 8 {\displaystyle {\frac {1+(2-3)\left({\frac {1}{4}}\right)}{2}}={\frac {3}{8}}}[image: {\displaystyle {\frac {1+(2-3)\left({\frac {1}{4}}\right)}{2}}={\frac {3}{8}}}] will be a right term. Continuing, this gives 1 3 = { 0, 1 4, 5 16, … | 1 2, 3 8, … } {\displaystyle {\frac {1}{3}}=\left\{\left.0,{\frac {1}{4}},{\frac {5}{16}},\ldots \,\right|\,{\frac {1}{2}},{\frac {3}{8}},\ldots \right\}}[image: {\displaystyle {\frac {1}{3}}=\left\{\left.0,{\frac {1}{4}},{\frac {5}{16}},\ldots \,\right|\,{\frac {1}{2}},{\frac {3}{8}},\ldots \right\}}]

For negative y, ⁠ 1 /*y*⁠ is given by 1 y = − ( 1 − y) {\displaystyle {\frac {1}{y}}=-\left({\frac {1}{-y}}\right)}[image: {\displaystyle {\frac {1}{y}}=-\left({\frac {1}{-y}}\right)}]

If *y*= 0, then ⁠ 1 /*y*⁠ is undefined.

### Consistency

[[edit][67]]

It can be shown that the definitions of negation, addition and multiplication are consistent, in the sense that:

- Addition and negation are defined recursively in terms of "simpler" addition and negation steps, so that operations on numbers with birthday n will eventually be expressed entirely in terms of operations on numbers with birthdays less than n;
- Multiplication is defined recursively in terms of additions, negations, and "simpler" multiplication steps, so that the product of numbers with birthday n will eventually be expressed entirely in terms of sums and differences of products of numbers with birthdays less than n;
- As long as the operands are well-defined surreal number forms (each element of the left set is less than each element of the right set), the results are again well-defined surreal number forms;
- The operations can be extended to *numbers*(equivalence classes of forms): the result of negating x or adding or multiplying x and y will represent the same number regardless of the choice of form of x and y; and
- These operations obey the associativity, commutativity, additive inverse, and distributivity axioms in the definition of a [field][68], with additive identity 0 = { | } and multiplicative identity 1 = { 0 | }.

With these rules one can now verify that the numbers found in the first few generations were properly labeled. The construction rule is repeated to obtain more generations of surreals:

*S*0 = { 0 }

*S*1 = { −1 < 0 < 1 }

*S*2 = { −2 < −1 < − ⁠ 1 / 2 ⁠ < 0 < ⁠ 1 / 2 ⁠ < 1 < 2 }

*S*3 = { −3 < −2 < − ⁠ 3 / 2 ⁠ < −1 < − ⁠ 3 / 4 ⁠ < − ⁠ 1 / 2 ⁠ < − ⁠ 1 / 4 ⁠ < 0 < ⁠ 1 / 4 ⁠ < ⁠ 1 / 2 ⁠ < ⁠ 3 / 4 ⁠ < 1 < ⁠ 3 / 2 ⁠ < 2 < 3 }

*S*4 = { −4 < −3 < ... < − ⁠ 1 / 8 ⁠ < 0 < ⁠ 1 / 8 ⁠ < ⁠ 1 / 4 ⁠ < ⁠ 3 / 8 ⁠ < ⁠ 1 / 2 ⁠ < ⁠ 5 / 8 ⁠ < ⁠ 3 / 4 ⁠ < ⁠ 7 / 8 ⁠ < 1 < ⁠ 5 / 4 ⁠ < ⁠ 3 / 2 ⁠ < ⁠ 7 / 4 ⁠ < 2 < ⁠ 5 / 2 ⁠ < 3 < 4 }

### Arithmetic closure

[[edit][69]]

For each [natural number][70] (finite ordinal) n, all numbers generated in *S**n*are [dyadic fractions][71], i.e., can be written as an [irreducible fraction][72] ⁠*a*/ 2*b*⁠, where a and b are [integers][73] and 0 ≤ *b*< *n*.

The set of all surreal numbers that are generated in some *S**n*for finite n may be denoted as S ∗ = ⋃ n ∈ N S n {\textstyle S_{*}=\bigcup _{n\in N}S_{n}}[image: {\textstyle S_{*}=\bigcup _{n\in N}S_{n}}]. One may form the three classes 0 \\} \\\\\nS_{-} &= \\{ x \\in S_*: x < 0 \\}\n\\end{align}"}}'> 0\}\\S_{-}&=\{x\in S_{*}:x<0\}\end{aligned}}}"> S 0 = { 0 } S + = { x ∈ S ∗: x > 0 } S − = { x ∈ S ∗: x < 0 } {\displaystyle {\begin{aligned}S_{0}&=\{0\}\\S_{+}&=\{x\in S_{*}:x>0\}\\S_{-}&=\{x\in S_{*}:x<0\}\end{aligned}}} 0\}\\S_{-}&=\{x\in S_{*}:x<0\}\end{aligned}}}"/> of which *S**∗*is the union. No individual *S**n*is closed under addition and multiplication (except *S*0), but *S*∗ is; it is the subring of the rationals consisting of all dyadic fractions.

There are infinite ordinal numbers β for which the set of surreal numbers with birthday less than β is closed under the different arithmetic operations. [7] For any ordinal α, the set of surreal numbers with birthday less than *β*= *ω**α*(using powers of ω) is closed under addition and forms a group; for birthday less than ω ω α it is closed under multiplication and forms a ring; [b] and for birthday less than an (ordinal) [epsilon number][74] ε α it is closed under multiplicative inverse and forms a field. The latter sets are also closed under the exponential function as defined by Kruskal and Gonshor. [7] [8]: ch. 10 [7]

However, it is always possible to construct a surreal number that is greater than any member of a set of surreals (by including the set on the left side of the constructor) and thus the collection of surreal numbers is a [proper class][4]. With their ordering and algebraic operations they constitute an [ordered field][12], with the caveat that they do not form a [set][75]. In fact, it is a very special ordered field: the biggest one, in that every ordered field is a subfield of the surreal numbers. [2] The class of all surreal numbers is denoted by the symbol N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }].

## Infinity

[[edit][76]]

Define *S**ω*as the set of all surreal numbers generated by the construction rule from subsets of *S*∗. (This is the same inductive step as before, since the ordinal number ω is the smallest ordinal that is larger than all natural numbers; however, the set union appearing in the inductive step is now an infinite union of finite sets, and so this step can be performed only in a set theory that allows such a union.) A unique infinitely large positive number occurs in *S**ω*: ω = { S ∗ ∣ } = { 1, 2, 3, 4, … ∣ }. {\displaystyle \omega =\{S_{*}\mid {}\}=\{1,2,3,4,\ldots \mid {}\}.}[image: {\displaystyle \omega =\{S_{*}\mid {}\}=\{1,2,3,4,\ldots \mid {}\}.}]*S**ω*also contains objects that can be identified as the [rational numbers][77]. For example, the ω -complete form of the fraction ⁠ 1 / 3 ⁠ is given by: 1 \\}."}}'> 1\}.}"> 1 3 = { y ∈ S ∗: 3 y < 1 ∣ y ∈ S ∗: 3 y > 1 }. {\displaystyle {\tfrac {1}{3}}=\{y\in S_{*}:3y<1\mid y\in S_{*}:3y>1\}.} 1\}.}"/> The product of this form of ⁠ 1 / 3 ⁠ with any form of 3 is a form whose left set contains only numbers less than 1 and whose right set contains only numbers greater than 1; the birthday property implies that this product is a form of 1.

Not only do all the rest of the [rational numbers][77] appear in *S**ω*; the remaining finite [real numbers][5] do too. For example, π = { 3, 25 8, 201 64, … ∣ 4, 7 2, 13 4, 51 16, … }. {\displaystyle \pi =\left\{3,{\tfrac {25}{8}},{\tfrac {201}{64}},\ldots \mid 4,{\tfrac {7}{2}},{\tfrac {13}{4}},{\tfrac {51}{16}},\ldots \right\}.}[image: {\displaystyle \pi =\left\{3,{\tfrac {25}{8}},{\tfrac {201}{64}},\ldots \mid 4,{\tfrac {7}{2}},{\tfrac {13}{4}},{\tfrac {51}{16}},\ldots \right\}.}]

The only infinities in *S**ω*are ω and −*ω*; but there are other non-real numbers in *S**ω*among the reals. Consider the smallest positive number in *S**ω*: 0 \\}"}}'> 0\}}"> ε = { S − ∪ S 0 ∣ S + } = { 0 ∣ 1, 1 2, 1 4, 1 8, … } = { 0 ∣ y ∈ S ∗: y > 0 } {\displaystyle \varepsilon =\{S_{-}\cup S_{0}\mid S_{+}\}=\left\{0\mid 1,{\tfrac {1}{2}},{\tfrac {1}{4}},{\tfrac {1}{8}},\ldots \right\}=\{0\mid y\in S_{*}:y>0\}} 0\}}"/> This number is larger than zero but less than all positive dyadic fractions. It is therefore an [infinitesimal][7] number, often labeled ε. The ω -complete form of ε (respectively −*ε*) is the same as the ω -complete form of 0, except that 0 is included in the left (respectively right) set. The only "pure" infinitesimals in *S**ω*are ε and its additive inverse −*ε*; adding them to any dyadic fraction y produces the numbers *y*± *ε*, which also lie in *S**ω*.

One can determine the relationship between ω and ε by multiplying particular forms of them to obtain:

*ω*· *ε*= { *ε*· *S*+ | *ω*· *S*+ + *S*∗ + *ε*· *S*∗ }.

This expression is well-defined only in a set theory which permits transfinite induction up to *S**ω*2. In such a system, one can demonstrate that all the elements of the left set of *ωS**ω*· ‍*S**ω**ε*are positive infinitesimals and all the elements of the right set are positive infinities, and therefore *ωS**ω*· ‍*S**ω**ε*is the oldest positive finite number, 1. Consequently, ⁠ 1 /*ε*⁠ = *ω*. Some authors systematically use *ω*−1 in place of the symbol ε.

### Contents of *S**ω*

[[edit][78]]

Given any *x*= { *L*| *R*} in *S**ω*, exactly one of the following is true:

- L and R are both empty, in which case *x*= 0;
- R is empty and some integer *n*≥ 0 is greater than every element of L, in which case x equals the smallest such integer n;
- R is empty and no integer n is greater than every element of L, in which case x equals +*ω*;
- L is empty and some integer *n*≤ 0 is less than every element of R, in which case x equals the largest such integer n;
- L is empty and no integer n is less than every element of R, in which case x equals −*ω*;
- L and R are both non-empty, and:

  - Some dyadic fraction y is "strictly between" L and R (greater than all elements of L and less than all elements of R), in which case x equals the oldest such dyadic fraction y;
  - No dyadic fraction y lies strictly between L and R, but some dyadic fraction y ∈ L {\textstyle y\in L}[image: {\textstyle y\in L}] is greater than or equal to all elements of L and less than all elements of R, in which case x equals *y*+ *ε*;
  - No dyadic fraction y lies strictly between L and R, but some dyadic fraction y ∈ R {\textstyle y\in R}[image: {\textstyle y\in R}] is greater than all elements of L and less than or equal to all elements of R, in which case x equals *y*− *ε*;
  - Every dyadic fraction is either greater than some element of R or less than some element of L, in which case x is some real number that has no representation as a dyadic fraction.

*S**ω*is not an algebraic field, because it is not closed under arithmetic operations; consider *ω*+ 1, whose form ω + 1 = { 1, 2, 3, 4,... ∣ } + { 0 ∣ } = { 1, 2, 3, 4, …, ω ∣ } {\displaystyle \omega +1=\{1,2,3,4,...\mid {}\}+\{0\mid {}\}=\{1,2,3,4,\ldots ,\omega \mid {}\}}[image: {\displaystyle \omega +1=\{1,2,3,4,...\mid {}\}+\{0\mid {}\}=\{1,2,3,4,\ldots ,\omega \mid {}\}}] does not lie in any number in *S**ω*. The maximal subset of *S**ω*that is closed under (finite series of) arithmetic operations is the field of real numbers, obtained by leaving out the infinities ±*ω*, the infinitesimals ±*ε*, and the infinitesimal neighbors *y*± *ε*of each nonzero dyadic fraction y.

This construction of the real numbers differs from the [Dedekind cuts][41] of [standard analysis][79] in that it starts from dyadic fractions rather than general rationals and naturally identifies each dyadic fraction in *S**ω*with its forms in previous generations. (The ω -complete forms of real elements of *S**ω*are in one-to-one correspondence with the reals obtained by Dedekind cuts, under the proviso that Dedekind reals corresponding to rational numbers are represented by the form in which the cut point is omitted from both left and right sets.) The rationals are not an identifiable stage in the surreal construction; they are merely the subset Q of *S**ω*containing all elements x such that *x**b*= *a*for some a and some nonzero b, both drawn from *S*∗. By demonstrating that Q is closed under individual repetitions of the surreal arithmetic operations, one can show that it is a field; and by showing that every element of Q is reachable from *S*∗ by a finite series (no longer than two, actually) of arithmetic operations *including multiplicative inversion*, one can show that Q is strictly smaller than the subset of *S**ω*identified with the reals.

The set *S**ω*has the same [cardinality][80] as the real numbers R. This can be demonstrated by exhibiting surjective mappings from *S**ω*to the closed unit interval I of R and vice versa. Mapping *S**ω*onto I is routine; map numbers less than or equal to ε (including −*ω*) to 0, numbers greater than or equal to 1 − *ε*(including ω) to 1, and numbers between ε and 1 − *ε*to their equivalent in I (mapping the infinitesimal neighbors *y*±*ε*of each dyadic fraction y, along with y itself, to y). To map I onto *S**ω*, map the (open) central third ( ⁠ 1 / 3 ⁠, ⁠ 2 / 3 ⁠) of I onto { | } = 0; the central third ( ⁠ 7 / 9 ⁠, ⁠ 8 / 9 ⁠) of the upper third to { 0 | } = 1; and so forth. This maps a nonempty open interval of I onto each element of *S*∗, monotonically. The residue of I consists of the [Cantor set][81]*2**ω*, each point of which is uniquely identified by a partition of the central-third intervals into left and right sets, corresponding precisely to a form { *L*| *R*} in *S**ω*. This places the Cantor set in one-to-one correspondence with the set of surreal numbers with birthday ω.

## Transfinite induction

[[edit][82]]

Continuing to perform [transfinite induction][53] beyond *S**ω*produces more ordinal numbers α, each represented as the largest surreal number having birthday α. (This is essentially a definition of the ordinal numbers resulting from transfinite induction.) The first such ordinal is *ω*+ 1 = { *ω*| }. There is another positive infinite number in generation *ω*+ 1:

*ω*− 1 = { 0, 1, 2, 3, 4, ... | *ω*}.

The surreal number *ω*− 1 is not an ordinal; the ordinal *ω*is not the successor of any ordinal. This is a surreal number with birthday *ω*+ 1, which is labeled *ω*− 1 on the basis that it coincides with the sum of *ω*= { 0, 1, 2, 3, 4, ... | } and −1 = { | 0 }. Similarly, there are two new infinitesimal numbers in generation *ω*+ 1:

\n{{math|1={{sfrac|''ε''|2}} = ''ε'' · {{sfrac|1|2}} = {{mset| 0 {{!}} ''ε'' }}}}."}},"i":0}}]}">

2*ε*= *ε*+ *ε*= { *ε*| 1 + *ε*, ⁠ 1 / 2 ⁠ + *ε*, ⁠ 1 / 4 ⁠ + *ε*, ⁠ 1 / 8 ⁠ + *ε*, ... } and
⁠*ε*/ 2 ⁠ = *ε*· ⁠ 1 / 2 ⁠ = { 0 | *ε*}.

At a later stage of transfinite induction, there is a number larger than *ω*+ *k*for all natural numbers *k*:

2*ω*= *ω*+ *ω*= { *ω*+ 1, *ω*+ 2, *ω*+ 3, *ω*+ 4, ... | }

This number may be labeled *ω*+ *ω*both because its birthday is *ω*+ *ω*(the first ordinal number not reachable from *ω*by the successor operation) and because it coincides with the surreal sum of *ω*and *ω*; it may also be labeled 2*ω*because it coincides with the product of *ω*= { 1, 2, 3, 4, ... | } and 2 = { 1 | }. It is the second limit ordinal; reaching it from *ω*via the construction step requires a transfinite induction on ⋃ k < ω S ω + k {\displaystyle \bigcup _{k<\omega }S_{\omega +k}}[image: {\displaystyle \bigcup _{k<\omega }S_{\omega +k}}] This involves an infinite union of infinite sets, which is a "stronger" set theoretic operation than the previous transfinite induction required.

Note that the *conventional*addition and multiplication of ordinals does not always coincide with these operations on their surreal representations. The sum of ordinals 1 + *ω*equals *ω*, but the surreal sum is commutative and produces ''ω''"}},"i":0}}]}'>1 + *ω*= *ω*+ 1 > *ω*. The addition and multiplication of the surreal numbers associated with ordinals coincides with the [natural sum and natural product][20] of ordinals.

Just as 2*ω*is bigger than *ω*+ *n*for any natural number *n*, there is a surreal number ⁠*ω*/ 2 ⁠ that is infinite but smaller than *ω*− *n*for any natural number *n*. That is, ⁠*ω*/ 2 ⁠ is defined by

⁠*ω*/ 2 ⁠ = { *S*∗ | *ω*− *S*∗ }

where on the right hand side the notation *x*− *Y*is used to mean { *x*− *y*: *y*∈ *Y*}. It can be identified as the product of *ω*and the form { 0 | 1 } of ⁠ 1 / 2 ⁠. The birthday of ⁠*ω*/ 2 ⁠ is the limit ordinal *ω*2.

## Powers of *ω*and the Conway normal form

[[edit][83]]

To classify the "orders" of infinite and infinitesimal surreal numbers, also known as [archimedean][84] classes, Conway associated to each surreal number x the surreal number

- *ω**x*= { 0, *r**ω**x*L | *s**ω**x*R },

where r and s range over the positive real numbers. If *x*< *y*then *ω**y*is "infinitely greater" than *ω**x*, in that it is greater than *r**ω**x*for all real numbers r. Powers of ω also satisfy the conditions

- *ω**x**ω**y*= *ω**x*+*y*,
- *ω*−*x*= ⁠ 1 /*ω**x*⁠,

so they behave the way one would expect powers to behave.

Each power of ω also has the redeeming feature of being the *simplest*surreal number in its archimedean class; conversely, every archimedean class within the surreal numbers contains a unique simplest member. Thus, for every positive surreal number x there will always exist some positive real number r and some surreal number y so that *x*− *rω**y*is "infinitely smaller" than x. The exponent y is the "base ω logarithm" of x, defined on the positive surreals; it can be demonstrated that log*ω*maps the positive surreals onto the surreals and that

log*ω*(*xy*) = log*ω*(*x*) + log*ω*(*y*).

This gets extended by transfinite induction so that every surreal number has a "normal form" analogous to the [Cantor normal form][85] for ordinal numbers. This is the Conway normal form: Every surreal number x may be uniquely written as

*x*= *r*0*ω**y*0 + *r*1*ω**y*1 + ...,

where every *r**α*is a nonzero real number and the *y**α*s form a strictly decreasing sequence of surreal numbers. This "sum", however, may have infinitely many terms, and in general has the length of an arbitrary ordinal number. (Zero corresponds of course to the case of an empty sequence, and is the only surreal number with no leading exponent.)

Looked at in this manner, the surreal numbers resemble a [power series field][27], except that the decreasing sequences of exponents must be bounded in length by an ordinal and are not allowed to be as long as the class of ordinals. This is the basis for the formulation of the surreal numbers as a Hahn series.

## Gaps and continuity

[[edit][86]]

In contrast to the real numbers, a (proper) subset of the surreal numbers does not have a least upper (or lower) bound unless it has a maximal (minimal) element. Conway defines [6] a gap as { *L*| *R*} such that every element of *L*is less than every element of *R*, and L ∪ R = N o {\textstyle L\cup R=\mathbb {No} }[image: {\textstyle L\cup R=\mathbb {No} }]; this is not a number because at least one of the sides is a proper class. Though similar, gaps are not quite the same as [Dedekind cuts][41], [c] but we can still talk about a completion N o D {\textstyle \mathbb {No} _{\mathfrak {D}}}[image: {\textstyle \mathbb {No} _{\mathfrak {D}}}] of the surreal numbers with the natural ordering which is a (proper class-sized) [linear continuum][87]. [9]

For instance there is no least positive infinite surreal, but the gap

n \\}"}}'> n\}}"> { x: ∃ n ∈ N: x < n ∣ x: ∀ n ∈ N: x > n } {\displaystyle \{x:\exists n\in \mathbb {N} :x<n\mid x:\forall n\in \mathbb {N} :x>n\}} n\}}"/>

is greater than all real numbers and less than all positive infinite surreals, and is thus the least upper bound of the reals in N o D {\textstyle \mathbb {No} _{\mathfrak {D}}}[image: {\textstyle \mathbb {No} _{\mathfrak {D}}}]. Similarly the gap O n = { N o ∣ } {\textstyle \mathbb {On} =\{\mathbb {No} \mid {}\}}[image: {\textstyle \mathbb {On} =\{\mathbb {No} \mid {}\}}] is larger than all surreal numbers. (This is an [esoteric pun][88]: In the general construction of ordinals, α "is" the set of ordinals smaller than α, and we can use this equivalence to write *α*= { *α*| } in the surreals; O n {\textstyle \mathbb {On} }[image: {\textstyle \mathbb {On} }] denotes the class of ordinal numbers, and because O n {\textstyle \mathbb {On} }[image: {\textstyle \mathbb {On} }] is [cofinal][89] in N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }] we have { N o ∣ } = { O n ∣ } = O n {\textstyle \{\mathbb {No} \mid {}\}=\{\mathbb {On} \mid {}\}=\mathbb {On} }[image: {\textstyle \{\mathbb {No} \mid {}\}=\{\mathbb {On} \mid {}\}=\mathbb {On} }] by extension.)

With a bit of set-theoretic care, [d] N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }] can be equipped with a topology where the [open sets][90] are unions of open intervals (indexed by proper sets) and continuous functions can be defined. [9] An equivalent of [Cauchy sequences][91] can be defined as well, although they have to be indexed by the class of ordinals; these will always converge, but the limit may be either a number or a gap that can be expressed as ∑ α ∈ N o r α ω a α {\displaystyle \sum _{\alpha \in \mathbb {No} }r_{\alpha }\omega ^{a_{\alpha }}}[image: {\displaystyle \sum _{\alpha \in \mathbb {No} }r_{\alpha }\omega ^{a_{\alpha }}}] with *a**α*decreasing and having no lower bound in N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }]. (All such gaps can be understood as Cauchy sequences themselves, but there are other types of gap that are not limits, such as ∞ and O n {\textstyle \mathbb {On} }[image: {\textstyle \mathbb {On} }]). [9]

## Exponential function

[[edit][92]]

Based on unpublished work by [Kruskal][93], a construction (by [transfinite induction][53]) that extends the real [exponential function][94] exp(*x*) (with base [e][95]) to the surreals was carried through by Gonshor. [8]: ch. 10

### Other exponentials

[[edit][96]]

The powers of ω function is also an exponential function, but does not have the properties desired for an extension of the function on the reals. It will, however, be needed in the development of the base- e exponential, and it is this function that is meant whenever the notation ω x is used in the following.

When y is a dyadic fraction, the [power function][97] x ∈ N o {\textstyle x\in \mathbb {No} }[image: {\textstyle x\in \mathbb {No} }], *x*↦ *x**y*may be composed from multiplication, multiplicative inverse and square root, all of which can be defined inductively. Its values are completely determined by the basic relation *x**y*+*z*= *x y*· *x z*, and where defined it necessarily agrees with any other [exponentiation][98] that can exist.

### Basic induction

[[edit][99]]

The induction steps for the surreal exponential are based on the series expansion for the real exponential, exp ⁡ x = ∑ n ≥ 0 x n n! {\displaystyle \exp x=\sum _{n\geq 0}{\frac {x^{n}}{n!}}}[image: {\displaystyle \exp x=\sum _{n\geq 0}{\frac {x^{n}}{n!}}}] more specifically those partial sums that can be shown by basic algebra to be positive but less than all later ones. For x positive these are denoted [*x*]*n*and include all [partial sums][100]; for x negative but finite, [*x*] 2*n*+1 denotes the odd steps in the series starting from the first one with a positive real part (which always exists). For x negative infinite the odd-numbered partial sums are strictly decreasing and the [*x*] 2*n*+1 notation denotes the empty set, but it turns out that the corresponding elements are not needed in the induction.

The relations that hold for real *x*< *y*are then

exp *x*· [*y*– *x*]*n*< exp *y*

and

exp *y*· [*x*– *y*] 2*n*+ 1 < exp *x*,

and this can be extended to the surreals with the definition

exp ⁡ z = { 0, exp ⁡ z L ⋅ [z − z L] n, exp ⁡ z R ⋅ [z − z R] 2 n + 1 ∣ exp ⁡ z R / [z R − z] n, exp ⁡ z L / [z L − z] 2 n + 1 }. {\displaystyle \exp z=\{0,\exp z_{L}\cdot [z-z_{L}]_{n},\exp z_{R}\cdot [z-z_{R}]_{2n+1}\mid \exp z_{R}/[z_{R}-z]_{n},\exp z_{L}/[z_{L}-z]_{2n+1}\}.}[image: {\displaystyle \exp z=\{0,\exp z_{L}\cdot [z-z_{L}]_{n},\exp z_{R}\cdot [z-z_{R}]_{2n+1}\mid \exp z_{R}/[z_{R}-z]_{n},\exp z_{L}/[z_{L}-z]_{2n+1}\}.}]

This is well-defined for all surreal arguments (the value exists and does not depend on the choice of z L and z R).

### Results

[[edit][101]]

Using this definition, the following hold: [e]

- exp is a strictly increasing positive function, *x*< *y*⇒ 0 < exp *x*< exp *y*
- exp satisfies exp(*x*+ *y*) = exp *x*· exp *y*
- exp is a [surjection][102] (onto N o + {\textstyle \mathbb {No} _{+}}[image: {\textstyle \mathbb {No} _{+}}]) and has a well-defined inverse, log = exp –1
- exp coincides with the usual exponential function on the reals (and thus exp 0 = 1, exp 1 = *e*)
- For x infinitesimal, the value of the formal power series ( [Taylor expansion][103]) of exp is well defined and coincides with the inductive definition

  - When x is given in Conway normal form, the set of exponents in the result is well-ordered and the coefficients are finite sums, directly giving the normal form of the result (which has a leading 1)
  - Similarly, for x infinitesimally close to 1, log *x*is given by power series expansion of *x*– 1

- For positive infinite x, exp *x*is infinite as well

  - If x has the form ω α ( 0"}},"i":0}}]}'>*α*> 0), exp *x*has the form ω ω β where β is a strictly increasing function of α. In fact there is an inductively defined bijection g: N o + → N o: α ↦ β {\textstyle g:\mathbb {No} _{+}\to \mathbb {No}:\alpha \mapsto \beta } [image: {\textstyle g:\mathbb {No} _{+}\to \mathbb {No} :\alpha \mapsto \beta }] whose inverse can also be defined inductively
  - If x is "pure infinite" with normal form *x*= Σ*α*<*β**r**α**ω**a**α*where all 0"}},"i":0}}]}'>*a**α*> 0, then exp *x*= *ω*Σ*α*<*β**r**α**ω**g*(*a**α*)
  - Similarly, for *x*= *ω*Σ*α*<*β**r**α**ω**b**α*, the inverse is given by log *x*= Σ*α*<*β**r**α**ω**g*–1 (*b**α*)

- Any surreal number can be written as the sum of a pure infinite, a real and an infinitesimal part, and the exponential is the product of the partial results given above

  - The normal form can be written out by multiplying the infinite part (a single power of ω) and the real exponential into the power series resulting from the infinitesimal
  - Conversely, dividing out the leading term of the normal form will bring any surreal number into the form (*ω*Σ*γ*<*δ**t**γ**ω**b**γ*)·*r*·(1 + Σ*α*<*β**s**α**ω**a**α*), for *a**α*< 0, where each factor has a form for which a way of calculating the logarithm has been given above; the sum is then the general logarithm

    - While there is no general inductive definition of log (unlike for exp), the partial results are given in terms of such definitions. In this way, the logarithm can be calculated explicitly, without reference to the fact that it's the inverse of the exponential.

- The exponential function is much greater than any finite power

  - For any positive infinite x and any finite n, exp(*x*)/*x**n*is infinite
  - For any integer n and surreal ''n''{{sup|2}}"}},"i":0}}]}'>*x*> *n*2, ''x''{{sup|''n''}}"}},"i":0}}]}'>exp(*x*) > *x**n*. This stronger constraint is one of the Ressayre axioms for the real [exponential field][104] [7]

- exp satisfies all the Ressayre axioms for the real exponential field [7]

  - The surreals with exponential is an [elementary extension][105] of the real exponential field
  - For *ε**β*an ordinal epsilon number, the set of surreal numbers with birthday less than *ε**β*constitutes a field that is closed under exponentials, and is likewise an elementary extension of the real exponential field

### Examples

[[edit][106]]

The surreal exponential is essentially given by its behaviour on positive powers of ω, i.e., the function ⁠ g ( a) {\displaystyle g(a)}[image: {\displaystyle g(a)}] ⁠ [*[clarification needed][107]*], combined with well-known behaviour on finite numbers. Only examples of the former will be given. In addition, ⁠ g ( a) = a {\displaystyle g(a)=a}[image: {\displaystyle g(a)=a}] ⁠ holds for a large part of its range, for instance for any finite number with positive real part and any infinite number that is less than some iterated power of ω ( ω ω · · ω for some number of levels).

- exp *ω*= *ω**ω*
- exp *ω*1/*ω*= *ω*and log *ω*= *ω*1/*ω*
- exp (*ω*· log *ω*) = exp (*ω*· *ω*1/*ω*) = *ω**ω*1 + 1/*ω*

  - This shows that the "power of ω " function is not compatible with exp, since compatibility would demand a value of ω ω here

- exp *ε*0 = *ω**ω**ε*0 + 1
- log *ε*0 = *ε*0 / *ω*

### Exponentiation

[[edit][108]]

A general exponentiation can be defined as *x y*= exp(*y*· log *x*), giving an interpretation to expressions like 2*ω*= exp(*ω*· log 2) = *ω*log 2 · *ω*. Again it is essential to distinguish this definition from the "powers of ω " function, especially if ω may occur as the base.

## Surcomplex numbers

[[edit][109]]

A **surcomplex number**is a number of the form *a*+ *b*i, where a and b are surreal numbers and i is the square root of −1. [10] [11] The surcomplex numbers form an [algebraically closed field][110] (except for being a proper class), [isomorphic][111] to the [algebraic closure][112] of the field generated by extending the [rational numbers][37] by a [proper class][4] of [algebraically independent][113] [transcendental][114] elements. [Up to][115] field [isomorphism][116], this fact characterizes the field of surcomplex numbers within any fixed set theory. [6]: Th.27

## Games

[[edit][117]]

Main article: [Combinatorial game theory][118]

The definition of surreal numbers contained one restriction: each element of L must be strictly less than each element of R. If this restriction is dropped we can generate a more general class known as **games**. All games are constructed according to this rule:

Construction rule If L and R are two sets of games then { *L*| *R*} is a game.

Addition, negation, and comparison are all defined the same way for both surreal numbers and games.

Every surreal number is a game, but not all games are surreal numbers, e.g. the game ********[{ 0 | 0 }][119] is not a surreal number. The class of games is more general than the surreals, and has a simpler definition, but lacks some of the nicer properties of surreal numbers. The class of surreal numbers forms a [field][68], but the class of games does not. The surreals have a [total order][3]: given any two surreals, they are either equal, or one is greater than the other. The games have only a [partial order][120]: there exist pairs of games that are neither equal, greater than, nor less than each other. Each surreal number is either positive, negative, or zero. Each game is either positive, negative, *[zero][121]*, or *[fuzzy][122]*(incomparable with zero, such as {1 | −1}).

A move in a game involves the player whose move it is choosing a game from those available in L (for the left player) or R (for the right player) and then passing this chosen game to the other player. A player who cannot move because the choice is from the empty set has lost. A positive game represents a win for the left player, a negative game for the right player, a zero game for the second player to move, and a [fuzzy game][122] for the first player to move.

If x, y, and z are surreals, and *x*= *y*, then *x**z*= *y**z*. However, if x, y, and z are games, and *x*= *y*, then it is not always true that *x**z*= *y**z*. Note that " = " here means equality, not identity.

## Application to combinatorial game theory

[[edit][123]]

The surreal numbers were originally motivated by studies of the game [Go][124], [3] and there are numerous connections between popular games and the surreals. In this section, we will use a capitalized *Game*for the mathematical object { *L*| *R*}, and the lowercase *game*for recreational games like [Chess][125] or [Go][124].

We consider games with these properties:

- Two players (named *Left*and *Right*)
- [Deterministic][126] (the game at each step will completely depend on the choices the players make, rather than a random factor)
- No hidden information (such as cards or tiles that a player hides)
- Players alternate taking turns (the game may or may not allow multiple moves in a turn)
- Every game must end in a finite number of moves
- As soon as there are no legal moves left for a player, the game ends, and that player loses

For most games, the initial board position gives no great advantage to either player. As the game progresses and one player starts to win, board positions will occur in which that player has a clear advantage. For analyzing games, it is useful to associate a Game with every board position. The value of a given position will be the Game {L|R}, where L is the set of values of all the positions that can be reached in a single move by Left. Similarly, R is the set of values of all the positions that can be reached in a single move by Right.

The zero Game (called 0) is the Game where L and R are both empty, so the player to move next ( L or R) immediately loses. The sum of two Games G = { L1 | R1 } and H = { L2 | R2 } is defined as the Game G + H = { L1 + H, G + L2 | R1 + H, G + R2 } where the player to move chooses which of the Games to play in at each stage, and the loser is still the player who ends up with no legal move. One can imagine two chess boards between two players, with players making moves alternately, but with complete freedom as to which board to play on. If G is the Game {L | R}, −G is the Game {−R | −L}, i.e. with the role of the two players reversed. It is easy to show G − G = 0 for all Games G (where G − H is defined as G + (−H)).

This simple way to associate Games with games yields a very interesting result. Suppose two perfect players play a game starting with a given position whose associated Game is x. We can classify all Games into four classes as follows:

- If 0"}},"i":0}}]}'>*x*> 0 then Left will win, regardless of who plays first.
- If *x*< 0 then Right will win, regardless of who plays first.
- If *x*= 0 then the player who goes second will win.
- If *x*|| 0 then the player who goes first will win.

More generally, we can define H"}},"i":0}}]}'>G > H as 0"}},"i":0}}]}'>G − H > 0, and similarly for <, = and ||.

The notation G || H means that G and H are incomparable. G || H is equivalent to G − H || 0, i.e. that H"}},"i":0}}]}'>G > H, G < H and G = H are all false. Incomparable games are sometimes said to be *confused*with each other, because one or the other may be preferred by a player depending on what is added to it. A game confused with zero is said to be [fuzzy][122], as opposed to [positive, negative, or zero][127]. An example of a fuzzy game is [star (*)][119].

Sometimes when a game nears the end, it will decompose into several smaller games that do not interact, except in that each player's turn allows moving in only one of them. For example, in Go, the board will slowly fill up with pieces until there are just a few small islands of empty space where a player can move. Each island is like a separate game of Go, played on a very small board. It would be useful if each subgame could be analyzed separately, and then the results combined to give an analysis of the entire game. This doesn't appear to be easy to do. For example, there might be two subgames where whoever moves first wins, but when they are combined into one big game, it is no longer the first player who wins. Fortunately, there is a way to do this analysis. The following theorem can be applied:

If a big game decomposes into two smaller games, and the small games have associated Games of x and y, then the big game will have an associated Game of *x*+ *y*.

A game composed of smaller games is called the [disjunctive sum][128] of those smaller games, and the theorem states that the method of addition we defined is equivalent to taking the disjunctive sum of the addends.

Historically, Conway developed the theory of surreal numbers in the reverse order of how it has been presented here. He was analyzing [Go endgames][129], and realized that it would be useful to have some way to combine the analyses of non-interacting subgames into an analysis of their [disjunctive sum][128]. From this he invented the concept of a Game and the addition operator for it. From there he moved on to developing a definition of negation and comparison. Then he noticed that a certain class of Games had interesting properties; this class became the surreal numbers. Finally, he developed the multiplication operator, and proved that the surreals are actually a field, and that it includes both the reals and ordinals.

## Alternative realizations

[[edit][130]]

Alternative approaches to the surreal numbers complement the original exposition by Conway in terms of games.

### Sign expansion

[[edit][131]]

#### Definitions

[[edit][132]]

In what is now called the *sign-expansion*or *sign-sequence*of a surreal number, a surreal number is a [function][133] whose [domain][134] is an [ordinal][19] and whose [codomain][135] is { −1, +1 }. [8]: ch. 2 This notion has been introduced by Conway himself in the equivalent formulation of L-R sequences. [6]

Define the binary predicate "simpler than" on numbers by: x is simpler than y if x is a [proper subset][136] of y, i.e. if dom(*x*) < dom(*y*) and *x*(*α*) = *y*(*α*) for all *α*< dom(*x*).

For surreal numbers, define the binary relation < to be lexicographic order (with the convention that "undefined values" are greater than −1 and less than 1). So *x*< *y*if one of the following holds:

- x is simpler than y and *y*(dom(*x*)) = +1;
- y is simpler than x and *x*(dom(*y*)) = −1;
- there exists a number z such that z is simpler than x, z is simpler than y, *x*(dom(*z*)) = −1 and *y*(dom(*z*)) = +1.

Equivalently, let *δ*(*x*,*y*) = min({ dom(*x*), dom(*y*)} ∪ { *α*:*α*< dom(*x*) ∧ *α*< dom(*y*) ∧ *x*(*α*) ≠ *y*(*α*) }), so that *x*= *y*if and only if *δ*(*x*,*y*) = dom(*x*) = dom(*y*). Then, for numbers x and y, *x*< *y*if and only if one of the following holds:

- *δ*(*x*,*y*) = dom(*x*) ∧ *δ*(*x*,*y*) < dom(*y*) ∧ *y*(*δ*(*x*,*y*)) = +1;
- *δ*(*x*,*y*) < dom(*x*) ∧ *δ*(*x*,*y*) = dom(*y*) ∧ *x*(*δ*(*x*,*y*)) = −1;
- *δ*(*x*,*y*) < dom(*x*) ∧ *δ*(*x*,*y*) < dom(*y*) ∧ *x*(*δ*(*x*,*y*)) = −1 ∧ *y*(*δ*(*x*,*y*)) = +1.

For numbers x and y, *x*≤ *y*if and only if *x*< *y*∨ *x*= *y*, and ''y''"}},"i":0}}]}'>*x*> *y*if and only if *y*< *x*. Also *x*≥ *y*if and only if *y*≤ *x*.

The relation < is [transitive][137], and for all numbers x and y, exactly one of *x*< *y*, *x*= *y*, ''y''"}},"i":0}}]}'>*x*> *y*, holds (law of [trichotomy][138]). This means that < is a [linear order][139] (except that < is a proper class).

For sets of numbers L and R such that ∀*x*∈ *L*∀*y*∈ *R*(*x*< *y*), there exists a unique number z such that

- ∀*x*∈ *L*(*x*< *z*) ∧ ∀*y*∈ *R*(*z*< *y*),
- For any number w such that ∀*x*∈ *L*(*x*< *w*) ∧ ∀*y*∈ *R*(*w*< *y*), *w*= *z*or z is simpler than w.

Furthermore, z is constructible from L and R by transfinite induction. z is the simplest number between L and R. Let the unique number z be denoted by *σ*(*L*, ‍*R*).

For a number x, define its left set *L*(*x*) and right set *R*(*x*) by

- *L*(*x*) = {*x*|*α*: *α*< dom(*x*) ∧ *x*(*α*) = +1};
- *R*(*x*) = {*x*|*α*: *α*< dom(*x*) ∧ *x*(*α*) = −1},

then *σ*(*L*(*x*),*R*(*x*)) = *x*.

One advantage of this alternative realization is that equality is identity, not an inductively defined relation. Unlike Conway's original realization of the surreal numbers, however, the sign-expansion requires a prior construction of the ordinals, while in Conway's realization, the ordinals are constructed as particular cases of surreals.

However, similar definitions can be made that eliminate the need for prior construction of the ordinals. For instance, we could let the surreals be the (recursively-defined) class of functions whose domain is a subset of the surreals satisfying the transitivity rule ∀*g*∈ dom *f*(∀*h*∈ dom *g*(*h*∈ dom *f*)) and whose range is { −, + }. "Simpler than" is very simply defined now: x is simpler than y if *x*∈ dom *y*. The total ordering is defined by considering x and y as sets of ordered pairs (as a function is normally defined): Either *x*= *y*, or else the surreal number *z*= *x*∩ *y*is in the domain of x or the domain of y (or both, but in this case the signs must disagree). We then have *x*< *y*if *x*(*z*) = − or *y*(*z*) = + (or both). Converting these functions into sign sequences is a straightforward task; arrange the elements of dom *f*in order of simplicity (i.e., inclusion), and then write down the signs that *f*assigns to each of these elements in order. The ordinals then occur naturally as those surreal numbers whose range is { + }.

#### Addition and multiplication

[[edit][140]]

The sum *x*+ *y*of two numbers x and y is defined by induction on dom(*x*) and dom(*y*) by *x*+ *y*= *σ*(*L*, ‍*R*), where

- *L*= { *u*+ *y*: *u*∈ *L*(*x*) } ∪ { *x*+ *v*: *v*∈ *L*(*y*) },
- *R*= { *u*+ *y*: *u*∈ *R*(*x*) } ∪ { *x*+ *v*: *v*∈ *R*(*y*) }.

The additive identity is given by the number 0 = { }, i.e. the number 0 is the unique function whose domain is the ordinal 0, and the additive inverse of the number x is the number −*x*, given by dom(−*x*) = dom(*x*), and, for *α*< dom(*x*), (−*x*)(*α*) = −1 if *x*(*α*) = +1, and (−*x*)(*α*) = +1 if *x*(*α*) = −1.

It follows that a number x is [positive][141] if and only if 0 < dom(*x*) and *x*(0) = +1, and x is [negative][142] if and only if 0 < dom(*x*) and *x*(0) = −1.

The product xy of two numbers, x and y, is defined by induction on dom(*x*) and dom(*y*) by *xy*= *σ*(*L*, ‍*R*), where

- *L*= { *uy*+ *xv*− *uv*: *u*∈ *L*(*x*), *v*∈ *L*(*y*) } ∪ { *uy*+ *xv*− *uv*: *u*∈ *R*(*x*), *v*∈ *R*(*y*) }
- *R*= { *uy*+ *xv*− *uv*: *u*∈ *L*(*x*), *v*∈ *R*(*y*) } ∪ { *uy*+ *xv*− *uv*: *u*∈ *R*(*x*), *v*∈ *L*(*y*) }

The multiplicative identity is given by the number 1 = { (0, +1) }, i.e. the number 1 has domain equal to the ordinal 1, and 1(0) = +1.

#### Correspondence with Conway's realization

[[edit][143]]

The map from Conway's realization to sign expansions is given by *f*({ *L*| *R*}) = *σ*(*M*, ‍*S*), where *M*= { *f*(*x*): *x*∈ *L*} and *S*= { *f*(*x*): *x*∈ *R*}.

The [inverse map][144] from the alternative realization to Conway's realization is given by *g*(*x*) = { *L*| *R*}, where *L*= { *g*(*y*): *y*∈ *L*(*x*) } and *R*= { *g*(*y*): *y*∈ *R*(*x*) }.

### Axiomatic approach

[[edit][145]]

In another approach to the surreals, given by Alling, [11] explicit construction is bypassed altogether. Instead, a set of axioms is given that any particular approach to the surreals must satisfy. Much like the [axiomatic approach][146] to the reals, these axioms guarantee uniqueness [up to][115] isomorphism.

A triple ⟨ N o, <, b ⟩ {\textstyle \langle \mathbb {No} ,\mathrm {<} ,b\rangle }[image: {\textstyle \langle \mathbb {No} ,\mathrm {<} ,b\rangle }] is a surreal number system if and only if the following hold:

- < is a [total order][3] over N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }]
- b is a function from N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }] [onto][147] the class of all ordinals ( b is called the "birthday function" on N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }]).
- Let A and B be subsets of N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }] such that for all *x*∈ *A*and *y*∈ *B*, *x*< *y*(using Alling's terminology, 〈 *A*, *B*〉 is a "Conway cut" of N o {\textstyle \mathbb {No} }[image: {\textstyle \mathbb {No} }]). Then there exists a unique z ∈ N o {\textstyle z\in \mathbb {No} }[image: {\textstyle z\in \mathbb {No} }] such that *b*(*z*) is minimal and for all *x*∈ *A*and all *y*∈ *B*, *x*< *z*< *y*. (This axiom is often referred to as "Conway's Simplicity Theorem".)
- Furthermore, if an ordinal α is greater than *b*(*x*) for all *x*∈ *A*, *B*, then *b*(*z*) ≤ *α*. (Alling calls a system that satisfies this axiom a "full surreal number system".)

Both Conway's original construction and the sign-expansion construction of surreals satisfy these axioms.

Given these axioms, Alling [11] derives Conway's original definition of ≤ and develops surreal arithmetic.

### Simplicity hierarchy

[[edit][148]]

A construction of the surreal numbers as a maximal binary pseudo-tree with simplicity (ancestor) and ordering relations is due to Philip Ehrlich. [12] The difference from the usual definition of a tree is that the set of ancestors of a vertex is [well-ordered][55], but may not have a [maximal element][149] (immediate predecessor); in other words the order type of that set is a general ordinal number, not just a natural number. This construction fulfills Alling's axioms as well and can easily be mapped to the sign-sequence representation. Ehrlich additionally constructed an isomorphism between Conway's maximal surreal number field and the maximal [hyperreals][150] in [von Neumann–Bernays–Gödel set theory][13]. [12]

### Hahn series

[[edit][151]]

Alling [11]: th. 6.55, p. 246 also proves that the field of surreal numbers is isomorphic (as an ordered field) to the field of [Hahn series][26] with real coefficients on the value group of surreal numbers themselves (the series representation corresponding to the normal form of a surreal number, as defined above). This provides a connection between surreal numbers and more conventional mathematical approaches to ordered field theory.

Note that the support of the Hahn series must be a set, not a proper class; for instance, the Hahn series ω − α {\displaystyle \omega ^{-\alpha }}[image: {\displaystyle \omega ^{-\alpha }}] summed over all ordinals *α*has no surreal counterpart.

This isomorphism makes the surreal numbers into a [valued field][152] where the valuation is the additive inverse of the exponent of the leading term in the Conway normal form, e.g., *ν*(*ω*) = −1. The [valuation ring][153] then consists of the finite surreal numbers (numbers with a real and/or an infinitesimal part). The reason for the sign inversion is that the exponents in the Conway normal form constitute a reverse well-ordered set, whereas Hahn series are formulated in terms of (non-reversed) well-ordered subsets of the value group.

## See also

[[edit][154]]

- [image: icon] [155] [Mathematics portal][156]

- [Hyperreal number][17]
- [Non-standard analysis][157]

## Notes

[[edit][158]]

1. ↑ In the original formulation using [von Neumann–Bernays–Gödel set theory][13], the surreals form a proper class, rather than a set, so the term [field][68] is not precisely correct; where this distinction is important, some authors use Field or FIELD to refer to a proper class that has the arithmetic properties of a field. One can obtain a true field by limiting the construction to a [Grothendieck universe][159], yielding a set with the cardinality of some [strongly inaccessible cardinal][160], or by using a form of set theory in which constructions by [transfinite recursion][161] stop at some countable ordinal such as [epsilon nought][162].
2. ↑ The set of dyadic fractions constitutes the simplest non-trivial group and ring of this kind; it consists of the surreal numbers with birthday less than *ω*= *ω*1 = *ω**ω*0.
3. ↑ The definition of a gap omits the conditions of a Dedekind cut that *L*and *R*be non-empty and that *L*not have a largest element, and also the identification of a cut with the smallest element in *R*if one exists.
4. ↑ Importantly, there is no claim that the collection of Cauchy sequences constitutes a class in NBG set theory.
5. ↑ Even the most trivial-looking of these equalities may involve transfinite induction and constitute a separate theorem.

## References

[[edit][163]]

1. 1 2 [Knuth, Donald][11] (1974). **[Surreal Numbers: How Two Ex-Students Turned on to Pure Mathematics and Found Total Happiness][164]. [ISBN][165] [0-201-03812-9][166]. Archived from [the original][167] on 2023-03-07.
2. 1 2 Bajnok, Béla (2013). **[An Invitation to Abstract Mathematics][168]. Springer. p. 362. [doi][169]: [10.1007/978-1-4614-6636-9_24][170]. [ISBN][165] [9781461466369][171]. Theorem 24.29. The surreal number system is the largest ordered field
3. 1 2 O'Connor, J.J.; Robertson, E.F. (June 2004). ["John Horton Conway"][172]. *School of Mathematics and Statistics*. University of St Andrews, Scotland. Archived from [the original][173] on 14 March 2008. Retrieved 2008-01-24.
4. ↑ Alling, Norman L. (1962). ******["On the existence of real-closed fields that are η α -sets of power ℵ α "][174]. *Transactions of the American Mathematical Society*. **103**: 341– 352. [doi][169]: [10.1090/S0002-9947-1962-0146089-X][174]. [MR][175] [0146089][176].
5. ↑ Alling, Norman (January 1985). ["Conway's Field of surreal numbers"][177] (PDF). *Transactions of the American Mathematical Society*. **287**(1): 365– 386. [doi][169]: [10.1090/s0002-9947-1985-0766225-7][178]. Retrieved 2019-03-05.
6. 1 2 3 4 5 Conway, John H. (2000-12-11) [1976]. **[On Numbers and Games][179] (2 ed.). CRC Press. [ISBN][165] [9781568811277][180].
7. 1 2 3 4 5 van den Dries, Lou; Ehrlich, Philip (January 2001). ["Fields of surreal numbers and exponentiation"][181]. *Fundamenta Mathematicae*. **167**(2). Warszawa: Institute of Mathematics of the Polish Academy of Sciences: 173– 188. [doi][169]: [10.4064/fm167-2-3][181]. [ISSN][182] [0016-2736][183].
8. 1 2 3 Gonshor, Harry (1986). *An Introduction to the Theory of Surreal Numbers*. London Mathematical Society Lecture Note Series. Vol. 110. Cambridge University Press. [doi][169]: [10.1017/CBO9780511629143][184]. [ISBN][165] [9780521312059][185].
9. 1 2 3 Rubinstein-Salzedo, Simon; Swaminathan, Ashvin (2015-05-19). "Analysis on Surreal Numbers". [arXiv][186]: [1307.7392v3][187] [[math.CA][188]].
10. ↑ Propp, James (August 22, 1994). ["Surreal vectors and the game of Cutblock"][189].
11. 1 2 3 4 Alling, Norman L. (1987). *Foundations of Analysis over Surreal Number Fields*. Mathematics Studies 141. North-Holland. [ISBN][165] [0-444-70226-1][190].
12. 1 2 [Ehrlich, Philip][191] (2012). ["The absolute arithmetic continuum and the unification of all numbers great and small"][192] (PDF). *The Bulletin of Symbolic Logic*. **18**(1): 1– 45. [doi][169]: [10.2178/bsl/1327328438][193]. [S2CID][194] [18683932][195]. Archived from [the original][196] (PDF) on 2017-10-07. Retrieved 2017-06-08.

## Further reading

[[edit][197]]

- An update of the classic 1976 book defining the surreal numbers, and exploring their connections to games: John Conway, *On Numbers And Games*, 2nd ed., 2001, [ISBN][165] [1-56881-127-6][198].
- An update of the first part of the 1981 book that presented surreal numbers and the analysis of games to a broader audience: Berlekamp, Conway, and Guy, *Winning Ways for Your Mathematical Plays*, vol. 1, 2nd ed., 2001, [ISBN][165] [1-56881-130-6][199].
- [Martin Gardner][200], *Penrose Tiles to Trapdoor Ciphers,*W. H. Freeman & Co., 1989, [ISBN][165] [0-7167-1987-8][201], Chapter 4. A non-technical overview; reprint of the 1976 *Scientific American*article.
- Polly Shulman, ["Infinity Plus One, and Other Surreal Numbers"][202], *[Discover][203]*, December 1995.
- A detailed treatment of surreal numbers: Norman L. Alling, *Foundations of Analysis over Surreal Number Fields*, 1987, [ISBN][165] [0-444-70226-1][190].
- A treatment of surreals based on the sign-expansion realization: Harry Gonshor, *An Introduction to the Theory of Surreal Numbers*, 1986, [ISBN][165] [0-521-31205-1][204].
- A detailed philosophical development of the concept of surreal numbers as a most general concept of number: [Alain Badiou][205], *Number and Numbers*, New York: Polity Press, 2008, [ISBN][165] [0-7456-3879-1][206] (paperback), [ISBN][165] [0-7456-3878-3][207] (hardcover).
- The Univalent Foundations Program (2013). **[Homotopy Type Theory: Univalent Foundations of Mathematics][208]. Princeton, NJ: [Institute for Advanced Study][209]. [MR][175] [3204653][210]. The surreal numbers are studied in the context of [homotopy type theory][211] in section 11.6.

## External links

[[edit][212]]

[image: Wikiversity logo] [213]

[Wikiversity][214] discusses ***[surreal numbers][215]***

[image: Wikibooks logo] [216]

[Wikibooks][217] has a book about ***[surreal numbers][218]***

- [Hackenstrings, and the 0.999...?= 1 FAQ, by A. N. Walker][219], an archive of the disappeared original
- [A gentle yet thorough introduction by Claus Tøndering][220]
- [Good Math, Bad Math: Surreal Numbers][221], a series of articles about surreal numbers and their variations
- [Conway's Mathematics after Conway][222], survey of Conway's accomplishments in the AMS Notices, with a section on surreal numbers

- [v][223]
- [t][224]
- [e][225]

[Infinity][6] ( [∞][226])

 |

History |

- [Ananta (infinite)][227]
- [Apeiron][228]
- [Controversy over Cantor's theory][229]
- [Galileo's paradox][230]
- [Hilbert's paradox of the Grand Hotel][231]
- [Infinity (philosophy)][232]
- [Paradoxes of infinity][233]
- [Paradoxes of set theory][234]

 |

Branches of mathematics |

- [Complex analysis][235]
- [Internal set theory][236]
- [Nonstandard analysis][237]
- [Set theory][238]
- [Synthetic differential geometry][239]

 |

Formalizations of infinity |

- [0.999...][240]
- [Absolute infinite][241]
- [Actual infinity][242]
- [Aleph number][243]
- [Beth number][244]
- [Cardinal numbers][245]
- [Cardinality of the continuum][246]
- [Dedekind-infinite set][247]
- [Division by zero][248] (Complex infinity)
- [Epsilon number][249]
- [Gimel function][250]
- [Hilbert space][251]
- [Hyperreal numbers][17]
- [Infinite set][252]
- [Infinitesimal][7]
- [Ordinal numbers][19]
- [Point at infinity][253]
- [Large cardinal][254]
- [Sphere at infinity][255] (Kleinian group)
- [Supertask][256]
- [Surreal numbers][257]
- [Transfinite numbers][18]

 |

Geometries |

- [Differential geometry of surfaces][258]
- [Möbius plane][259]
- [Möbius transformation][260]
- [Riemannian manifold][261]

 |

Mathematicians |

- [Georg Cantor][262]
- [David Hilbert][263]
- [Gottfried Wilhelm Leibniz][264]
- [August Ferdinand Möbius][265]
- [Bernhard Riemann][266]
- [Abraham Robinson][267]

 |

- [v][268]
- [t][269]
- [e][270]

[Number][271] systems

 |

Sets of [definable numbers][272] |

- [Natural numbers][70] ( N {\displaystyle \mathbb {N} }[image: {\displaystyle \mathbb {N} }])
- [Integers][73] ( Z {\displaystyle \mathbb {Z} }[image: {\displaystyle \mathbb {Z} }])
- [Rational numbers][77] ( Q {\displaystyle \mathbb {Q} }[image: {\displaystyle \mathbb {Q} }])
- [Constructible numbers][273]
- [Algebraic numbers][274] ( A {\displaystyle \mathbb {A} }[image: {\displaystyle \mathbb {A} }])
- [Closed-form numbers][275]
- [Periods][276] ( P {\displaystyle {\mathcal {P}}}[image: {\displaystyle {\mathcal {P}}}])
- [Computable numbers][277]
- [Arithmetical numbers][278]
- [Set-theoretically definable numbers][279]
- [Gaussian integers][280]

  - [Gaussian rationals][281]

- [Eisenstein integers][282]

 |

[Composition algebras][283] |

- [Division algebras][284]: [Real numbers][5] ( R {\displaystyle \mathbb {R} }[image: {\displaystyle \mathbb {R} }])
- [Complex numbers][285] ( C {\displaystyle \mathbb {C} }[image: {\displaystyle \mathbb {C} }])
- [Quaternions][286] ( H {\displaystyle \mathbb {H} }[image: {\displaystyle \mathbb {H} }])
- [Octonions][287] ( O {\displaystyle \mathbb {O} }[image: {\displaystyle \mathbb {O} }])

 |

Split
types |

- Over R {\displaystyle \mathbb {R} }[image: {\displaystyle \mathbb {R} }]:
- [Split-complex numbers][288]
- [Split-quaternions][289]
- [Split-octonions][290]
Over C {\displaystyle \mathbb {C} }[image: {\displaystyle \mathbb {C} }]:
- [Bicomplex numbers][291]
- [Biquaternions][292]
- [Bioctonions][293]

 |

Other [hypercomplex][294] |

- [Dual numbers][295]
- [Dual quaternions][296]
- [Dual-complex numbers][297]
- [Hyperbolic quaternions][298]
- [Sedenions][299] ( S {\displaystyle \mathbb {S} }[image: {\displaystyle \mathbb {S} }])
- [Trigintaduonions][300] ( T {\displaystyle \mathbb {T} }[image: {\displaystyle \mathbb {T} }])
- [Split-biquaternions][301]
- [Multicomplex numbers][302]
- [Geometric algebra][303] / [Clifford algebra][304]

  - [Algebra of physical space][305]
  - [Spacetime algebra][306]
  - [Plane-based geometric algebra][307]

 |

[Infinities][6] and [infinitesimals][7] |

- [Cardinal numbers][245]
- [Extended natural numbers][308]
- [Extended real numbers][309]

  - [Projective][310]

- [Extended complex numbers][311]
- [Hyperreal numbers][17]
- [Levi-Civita field][15]
- [Ordinal numbers][19]
- [Supernatural numbers][312]
- [Surreal numbers][257]
- [Superreal numbers][16]

 |

Other types |

- [Irrational numbers][313]
- [Fuzzy numbers][314]
- [Transcendental numbers][315]
- **[p -adic numbers][316] (**[p -adic solenoids][317])
- [Profinite integers][318]
- [Normal numbers][319]

 |

- [Classification][320]
- [List][321]

 |

- [v][322]
- [t][323]
- [e][324]

[Infinitesimals][7]

 |

History |

- [Adequality][325]
- [Leibniz's notation][326]
- [Integral symbol][327]
- [Criticism of nonstandard analysis][328]
- *[The Analyst][329]*
- *[The Method of Mechanical Theorems][330]*
- [Cavalieri's principle][331]

 |

[332]

 |

Related branches |

- [Nonstandard analysis][237]
- [Nonstandard calculus][333]
- [Internal set theory][236]
- [Synthetic differential geometry][239]
- [Smooth infinitesimal analysis][334]
- [Constructive nonstandard analysis][335]
- [Infinitesimal strain theory (physics)][336]

 |

Formalizations |

- [Differentials][337]
- [Hyperreal numbers][17]
- [Dual numbers][295]
- [Surreal numbers][257]

 |

Individual concepts |

- [Standard part function][338]
- [Transfer principle][339]
- [Hyperinteger][340]
- [Increment theorem][341]
- [Monad][342]
- [Internal set][343]
- [Levi-Civita field][15]
- [Hyperfinite set][344]
- [Law of continuity][345]
- [Overspill][346]
- [Microcontinuity][347]
- [Transcendental law of homogeneity][348]

 |

Mathematicians |

- [Gottfried Wilhelm Leibniz][264]
- [Abraham Robinson][267]
- [Pierre de Fermat][349]
- [Augustin-Louis Cauchy][350]
- [Leonhard Euler][351]

 |

Textbooks |

- [Analyse des Infiniment Petits][352]
- [Elementary Calculus][353]
- [Cours d'analyse][354]

 |

[Authority control databases][355][image: Edit this at Wikidata] [356]

 |

International |

- [GND][357]
- [FAST][358]

 |

National |

- [United States][359]
- [France][360]
- [BnF data][361]
- [Israel][362]

 |

Other |

- [IdRef][363]
- [Yale LUX][364]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Surreal_number&oldid=1363274242][365] "

[Categories][366]:

- [Combinatorial game theory][367]
- [Mathematical logic][368]
- [Infinity][369]
- [Real closed field][370]
- [John Horton Conway][371]
- [Nonstandard analysis][372]
- [Numbers][373]

Hidden categories:

- [Articles with short description][374]
- [Short description is different from Wikidata][375]
- [All articles with unsourced statements][376]
- [Articles with unsourced statements from October 2025][377]
- [Wikipedia articles needing clarification from February 2026][378]
- [Pages that use a deprecated format of the math tags][379]

Search

Surreal number

25 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Surreal_number_tree.svg
[2]: https://en.wikipedia.org/wiki/Mathematics
[3]: https://en.wikipedia.org/wiki/Total_order
[4]: https://en.wikipedia.org/wiki/Proper_class
[5]: https://en.wikipedia.org/wiki/Real_number
[6]: https://en.wikipedia.org/wiki/Infinity
[7]: https://en.wikipedia.org/wiki/Infinitesimal
[8]: https://en.wikipedia.org/wiki/Absolute_value
[9]: https://en.wikipedia.org/wiki/Go_endgame
[10]: https://en.wikipedia.org/wiki/John_Horton_Conway
[11]: https://en.wikipedia.org/wiki/Donald_Knuth
[12]: https://en.wikipedia.org/wiki/Ordered_field
[13]: https://en.wikipedia.org/wiki/Von_Neumann–Bernays–Gödel_set_theory
[14]: https://en.wikipedia.org/wiki/Rational_function
[15]: https://en.wikipedia.org/wiki/Levi-Civita_field
[16]: https://en.wikipedia.org/wiki/Superreal_number
[17]: https://en.wikipedia.org/wiki/Hyperreal_number
[18]: https://en.wikipedia.org/wiki/Transfinite_number
[19]: https://en.wikipedia.org/wiki/Ordinal_number
[20]: https://en.wikipedia.org/wiki/Ordinal_arithmetic#Natural_operations
[21]: https://en.wikipedia.org/wiki/Isomorphic
[22]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=1
[23]: https://en.wikipedia.org/wiki/Go_strategy_and_tactics
[24]: https://en.wikipedia.org/wiki/On_Numbers_and_Games
[25]: https://en.wikipedia.org/wiki/Hans_Hahn_(mathematician)
[26]: https://en.wikipedia.org/wiki/Hahn_series
[27]: https://en.wikipedia.org/wiki/Formal_power_series
[28]: https://en.wikipedia.org/wiki/Felix_Hausdorff
[29]: https://en.wikipedia.org/wiki/Η_set
[30]: https://en.wikipedia.org/wiki/Inaccessible_cardinal
[31]: https://en.wikipedia.org/wiki/Von_Neumann_universe
[32]: https://en.wikipedia.org/wiki/Wikipedia:Citation_needed
[33]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=2
[34]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=3
[35]: https://en.wikipedia.org/wiki/Ordered_pair
[36]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=4
[37]: https://en.wikipedia.org/wiki/Rational_numbers
[38]: https://en.wikipedia.org/wiki/Equivalence_class
[39]: https://en.wikipedia.org/wiki/Empty_set
[40]: https://en.wikipedia.org/wiki/Dyadic_rational
[41]: https://en.wikipedia.org/wiki/Dedekind_cut
[42]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=5
[43]: https://en.wikipedia.org/wiki/Inductive_definition
[44]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=6
[45]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=7
[46]: https://en.wikipedia.org/wiki/Order_theory
[47]: https://en.wikipedia.org/wiki/Antisymmetric_relation
[48]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=8
[49]: https://en.wikipedia.org/wiki/If_and_only_if
[50]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=9
[51]: https://en.wikipedia.org/wiki/Recursion
[52]: https://en.wikipedia.org/wiki/Mathematical_induction
[53]: https://en.wikipedia.org/wiki/Transfinite_induction
[54]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=10
[55]: https://en.wikipedia.org/wiki/Well-order
[56]: https://en.wikipedia.org/wiki/Ring_(mathematics)
[57]: https://en.wikipedia.org/wiki/Additive_inverse
[58]: https://en.wikipedia.org/wiki/Limit_ordinal
[59]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=11
[60]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=12
[61]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=13
[62]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=14
[63]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=15
[64]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=16
[65]: https://en.wikipedia.org/wiki/Multiplicative_identity
[66]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=17
[67]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=18
[68]: https://en.wikipedia.org/wiki/Field_(mathematics)
[69]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=19
[70]: https://en.wikipedia.org/wiki/Natural_number
[71]: https://en.wikipedia.org/wiki/Dyadic_fraction
[72]: https://en.wikipedia.org/wiki/Irreducible_fraction
[73]: https://en.wikipedia.org/wiki/Integer
[74]: https://en.wikipedia.org/wiki/Epsilon_number_(mathematics)
[75]: https://en.wikipedia.org/wiki/Set_(mathematics)
[76]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=20
[77]: https://en.wikipedia.org/wiki/Rational_number
[78]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=21
[79]: https://en.wikipedia.org/wiki/Real_analysis
[80]: https://en.wikipedia.org/wiki/Cardinality
[81]: https://en.wikipedia.org/wiki/Cantor_set
[82]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=22
[83]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=23
[84]: https://en.wikipedia.org/wiki/Archimedean_property
[85]: https://en.wikipedia.org/wiki/Ordinal_arithmetic#Cantor_normal_form
[86]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=24
[87]: https://en.wikipedia.org/wiki/Linear_continuum
[88]: https://en.wikipedia.org/wiki/Mathematical_joke
[89]: https://en.wikipedia.org/wiki/Cofinal_(mathematics)
[90]: https://en.wikipedia.org/wiki/Open_set
[91]: https://en.wikipedia.org/wiki/Cauchy_sequence
[92]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=25
[93]: https://en.wikipedia.org/wiki/Martin_David_Kruskal
[94]: https://en.wikipedia.org/wiki/Exponential_function
[95]: https://en.wikipedia.org/wiki/E_(mathematical_constant)
[96]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=26
[97]: https://en.wikipedia.org/wiki/Power_function
[98]: https://en.wikipedia.org/wiki/Exponentiation
[99]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=27
[100]: https://en.wikipedia.org/wiki/Partial_sum
[101]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=28
[102]: https://en.wikipedia.org/wiki/Surjection
[103]: https://en.wikipedia.org/wiki/Taylor_expansion
[104]: https://en.wikipedia.org/wiki/Exponential_field
[105]: https://en.wikipedia.org/wiki/Elementary_extension
[106]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=29
[107]: https://en.wikipedia.org/wiki/Wikipedia:Please_clarify
[108]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=30
[109]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=31
[110]: https://en.wikipedia.org/wiki/Algebraically_closed_field
[111]: https://en.wikipedia.org/wiki/Isomorphic_(mathematics)
[112]: https://en.wikipedia.org/wiki/Algebraic_closure
[113]: https://en.wikipedia.org/wiki/Algebraically_independent
[114]: https://en.wikipedia.org/wiki/Transcendental_(mathematics)
[115]: https://en.wikipedia.org/wiki/Up_to
[116]: https://en.wikipedia.org/wiki/Isomorphism
[117]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=32
[118]: https://en.wikipedia.org/wiki/Combinatorial_game_theory
[119]: https://en.wikipedia.org/wiki/Star_(game_theory)
[120]: https://en.wikipedia.org/wiki/Partial_order
[121]: https://en.wikipedia.org/wiki/Zero_game
[122]: https://en.wikipedia.org/wiki/Fuzzy_game
[123]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=33
[124]: https://en.wikipedia.org/wiki/Go_(board_game)
[125]: https://en.wikipedia.org/wiki/Chess
[126]: https://en.wikipedia.org/wiki/Deterministic
[127]: https://en.wikipedia.org/wiki/Sign_(mathematics)
[128]: https://en.wikipedia.org/wiki/Disjunctive_sum
[129]: https://en.wikipedia.org/wiki/Go_terms#Yose
[130]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=34
[131]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=35
[132]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=36
[133]: https://en.wikipedia.org/wiki/Function_(mathematics)
[134]: https://en.wikipedia.org/wiki/Domain_of_a_function
[135]: https://en.wikipedia.org/wiki/Codomain
[136]: https://en.wikipedia.org/wiki/Subset
[137]: https://en.wikipedia.org/wiki/Transitive_relation
[138]: https://en.wikipedia.org/wiki/Trichotomy_(mathematics)
[139]: https://en.wikipedia.org/wiki/Linear_order
[140]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=37
[141]: https://en.wikipedia.org/wiki/Positive_number
[142]: https://en.wikipedia.org/wiki/Negative_number
[143]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=38
[144]: https://en.wikipedia.org/wiki/Inverse_map
[145]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=39
[146]: https://en.wikipedia.org/wiki/Real_numbers#Axiomatic_approach
[147]: https://en.wikipedia.org/wiki/Onto
[148]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=40
[149]: https://en.wikipedia.org/wiki/Maximal_element
[150]: https://en.wikipedia.org/wiki/Hyperreal_field
[151]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=41
[152]: https://en.wikipedia.org/wiki/Valued_field
[153]: https://en.wikipedia.org/wiki/Valuation_ring
[154]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=42
[155]: https://en.wikipedia.org/wiki/File:Square_root_of_x.svg
[156]: https://en.wikipedia.org/wiki/Portal:Mathematics
[157]: https://en.wikipedia.org/wiki/Non-standard_analysis
[158]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=43
[159]: https://en.wikipedia.org/wiki/Grothendieck_universe
[160]: https://en.wikipedia.org/wiki/Strongly_inaccessible_cardinal
[161]: https://en.wikipedia.org/wiki/Transfinite_recursion
[162]: https://en.wikipedia.org/wiki/Epsilon_numbers_(mathematics)
[163]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=44
[164]: https://web.archive.org/web/20230307045844/https://www.cs.stanford.edu/~knuth/sn.html
[165]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[166]: https://en.wikipedia.org/wiki/Special:BookSources/0-201-03812-9
[167]: https://www.cs.stanford.edu/~knuth/sn.html
[168]: https://books.google.com/books?id=cNFzKnvxXoAC&amp;q=%22surreal+numbers%22
[169]: https://en.wikipedia.org/wiki/Doi_(identifier)
[170]: https://doi.org/10.1007%2F978-1-4614-6636-9_24
[171]: https://en.wikipedia.org/wiki/Special:BookSources/9781461466369
[172]: https://web.archive.org/web/20080314152337/http://www-history.mcs.st-andrews.ac.uk/Biographies/Conway.html
[173]: http://www-history.mcs.st-andrews.ac.uk/Biographies/Conway.html
[174]: https://doi.org/10.1090%2FS0002-9947-1962-0146089-X
[175]: https://en.wikipedia.org/wiki/MR_(identifier)
[176]: https://mathscinet.ams.org/mathscinet-getitem?mr=0146089
[177]: https://www.ams.org/journals/tran/1985-287-01/S0002-9947-1985-0766225-7/S0002-9947-1985-0766225-7.pdf
[178]: https://doi.org/10.1090%2Fs0002-9947-1985-0766225-7
[179]: https://books.google.com/books?id=tXiVo8qA5PQC
[180]: https://en.wikipedia.org/wiki/Special:BookSources/9781568811277
[181]: https://doi.org/10.4064%2Ffm167-2-3
[182]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[183]: https://search.worldcat.org/issn/0016-2736
[184]: https://doi.org/10.1017%2FCBO9780511629143
[185]: https://en.wikipedia.org/wiki/Special:BookSources/9780521312059
[186]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[187]: https://arxiv.org/abs/1307.7392v3
[188]: https://arxiv.org/archive/math.CA
[189]: http://jamespropp.org/surreal/text.ps.gz
[190]: https://en.wikipedia.org/wiki/Special:BookSources/0-444-70226-1
[191]: https://en.wikipedia.org/wiki/Philip_Ehrlich?action=edit&amp;redlink=1
[192]: https://web.archive.org/web/20171007095144/http://www.ohio.edu/people/ehrlich/Unification.pdf
[193]: https://doi.org/10.2178%2Fbsl%2F1327328438
[194]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[195]: https://api.semanticscholar.org/CorpusID:18683932
[196]: http://www.ohio.edu/people/ehrlich/Unification.pdf
[197]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=45
[198]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-127-6
[199]: https://en.wikipedia.org/wiki/Special:BookSources/1-56881-130-6
[200]: https://en.wikipedia.org/wiki/Martin_Gardner
[201]: https://en.wikipedia.org/wiki/Special:BookSources/0-7167-1987-8
[202]: https://www.discovermagazine.com/the-sciences/infinity-plus-one-and-other-surreal-numbers
[203]: https://en.wikipedia.org/wiki/Discover_(magazine)
[204]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-31205-1
[205]: https://en.wikipedia.org/wiki/Alain_Badiou
[206]: https://en.wikipedia.org/wiki/Special:BookSources/0-7456-3879-1
[207]: https://en.wikipedia.org/wiki/Special:BookSources/0-7456-3878-3
[208]: http://homotopytypetheory.org/book/
[209]: https://en.wikipedia.org/wiki/Institute_for_Advanced_Study
[210]: https://mathscinet.ams.org/mathscinet-getitem?mr=3204653
[211]: https://en.wikipedia.org/wiki/Homotopy_type_theory
[212]: /w/index.php?title=Surreal_number&amp;action=edit&amp;section=46
[213]: https://en.wikipedia.org/wiki/File:Wikiversity_logo_2017.svg
[214]: https://en.wikipedia.org/wiki/Wikiversity
[215]: https://en.wikiversity.org/wiki/Surreal%20number
[216]: https://en.wikipedia.org/wiki/File:Wikibooks-logo.svg
[217]: https://en.wikipedia.org/wiki/Wikibooks
[218]: https://en.wikibooks.org/wiki/Surreal%20Numbers%20and%20Games
[219]: https://web.archive.org/web/20011224163817/http://www.maths.nott.ac.uk/personal/anw/Research/Hack/
[220]: https://www.tondering.dk/download/sur.pdf
[221]: http://www.goodmath.org/blog/category/good-math/numbers/surreal-numbers/
[222]: https://doi.org/10.1090/noti2513
[223]: https://en.wikipedia.org/wiki/Template:Infinity
[224]: https://en.wikipedia.org/wiki/Template_talk:Infinity
[225]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Infinity
[226]: https://en.wikipedia.org/wiki/Infinity_symbol
[227]: https://en.wikipedia.org/wiki/Ananta_(infinite)
[228]: https://en.wikipedia.org/wiki/Apeiron
[229]: https://en.wikipedia.org/wiki/Controversy_over_Cantor's_theory
[230]: https://en.wikipedia.org/wiki/Galileo's_paradox
[231]: https://en.wikipedia.org/wiki/Hilbert's_paradox_of_the_Grand_Hotel
[232]: https://en.wikipedia.org/wiki/Infinity_(philosophy)
[233]: https://en.wikipedia.org/wiki/Paradoxes_of_infinity
[234]: https://en.wikipedia.org/wiki/Paradoxes_of_set_theory
[235]: https://en.wikipedia.org/wiki/Complex_analysis
[236]: https://en.wikipedia.org/wiki/Internal_set_theory
[237]: https://en.wikipedia.org/wiki/Nonstandard_analysis
[238]: https://en.wikipedia.org/wiki/Set_theory
[239]: https://en.wikipedia.org/wiki/Synthetic_differential_geometry
[240]: https://en.wikipedia.org/wiki/0.999...
[241]: https://en.wikipedia.org/wiki/Absolute_infinite
[242]: https://en.wikipedia.org/wiki/Actual_infinity
[243]: https://en.wikipedia.org/wiki/Aleph_number
[244]: https://en.wikipedia.org/wiki/Beth_number
[245]: https://en.wikipedia.org/wiki/Cardinal_number
[246]: https://en.wikipedia.org/wiki/Cardinality_of_the_continuum
[247]: https://en.wikipedia.org/wiki/Dedekind-infinite_set
[248]: https://en.wikipedia.org/wiki/Division_by_zero
[249]: https://en.wikipedia.org/wiki/Epsilon_number
[250]: https://en.wikipedia.org/wiki/Gimel_function
[251]: https://en.wikipedia.org/wiki/Hilbert_space
[252]: https://en.wikipedia.org/wiki/Infinite_set
[253]: https://en.wikipedia.org/wiki/Point_at_infinity
[254]: https://en.wikipedia.org/wiki/Large_cardinal
[255]: https://en.wikipedia.org/wiki/Sphere_at_infinity
[256]: https://en.wikipedia.org/wiki/Supertask
[257]: https://en.wikipedia.org/wiki/Surreal_number
[258]: https://en.wikipedia.org/wiki/Differential_geometry_of_surfaces
[259]: https://en.wikipedia.org/wiki/Möbius_plane
[260]: https://en.wikipedia.org/wiki/Möbius_transformation
[261]: https://en.wikipedia.org/wiki/Riemannian_manifold
[262]: https://en.wikipedia.org/wiki/Georg_Cantor
[263]: https://en.wikipedia.org/wiki/David_Hilbert
[264]: https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz
[265]: https://en.wikipedia.org/wiki/August_Ferdinand_Möbius
[266]: https://en.wikipedia.org/wiki/Bernhard_Riemann
[267]: https://en.wikipedia.org/wiki/Abraham_Robinson
[268]: https://en.wikipedia.org/wiki/Template:Number_systems
[269]: https://en.wikipedia.org/wiki/Template_talk:Number_systems
[270]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Number_systems
[271]: https://en.wikipedia.org/wiki/Number
[272]: https://en.wikipedia.org/wiki/Definable_number
[273]: https://en.wikipedia.org/wiki/Constructible_number
[274]: https://en.wikipedia.org/wiki/Algebraic_number
[275]: https://en.wikipedia.org/wiki/Closed-form_expression#Closed-form_number
[276]: https://en.wikipedia.org/wiki/Period_(algebraic_geometry)
[277]: https://en.wikipedia.org/wiki/Computable_number
[278]: https://en.wikipedia.org/wiki/Definable_real_number#Definability_in_arithmetic
[279]: https://en.wikipedia.org/wiki/Definable_real_number#Definability_in_models_of_ZFC
[280]: https://en.wikipedia.org/wiki/Gaussian_integer
[281]: https://en.wikipedia.org/wiki/Gaussian_rational
[282]: https://en.wikipedia.org/wiki/Eisenstein_integer
[283]: https://en.wikipedia.org/wiki/Composition_algebra
[284]: https://en.wikipedia.org/wiki/Division_algebra
[285]: https://en.wikipedia.org/wiki/Complex_number
[286]: https://en.wikipedia.org/wiki/Quaternion
[287]: https://en.wikipedia.org/wiki/Octonion
[288]: https://en.wikipedia.org/wiki/Split-complex_number
[289]: https://en.wikipedia.org/wiki/Split-quaternion
[290]: https://en.wikipedia.org/wiki/Split-octonion
[291]: https://en.wikipedia.org/wiki/Bicomplex_number
[292]: https://en.wikipedia.org/wiki/Biquaternion
[293]: https://en.wikipedia.org/wiki/Bioctonion
[294]: https://en.wikipedia.org/wiki/Hypercomplex_number
[295]: https://en.wikipedia.org/wiki/Dual_number
[296]: https://en.wikipedia.org/wiki/Dual_quaternion
[297]: https://en.wikipedia.org/wiki/Dual-complex_number
[298]: https://en.wikipedia.org/wiki/Hyperbolic_quaternion
[299]: https://en.wikipedia.org/wiki/Sedenion
[300]: https://en.wikipedia.org/wiki/Trigintaduonion
[301]: https://en.wikipedia.org/wiki/Split-biquaternion
[302]: https://en.wikipedia.org/wiki/Multicomplex_number
[303]: https://en.wikipedia.org/wiki/Geometric_algebra
[304]: https://en.wikipedia.org/wiki/Clifford_algebra
[305]: https://en.wikipedia.org/wiki/Algebra_of_physical_space
[306]: https://en.wikipedia.org/wiki/Spacetime_algebra
[307]: https://en.wikipedia.org/wiki/Plane-based_geometric_algebra
[308]: https://en.wikipedia.org/wiki/Extended_natural_numbers
[309]: https://en.wikipedia.org/wiki/Extended_real_number_line
[310]: https://en.wikipedia.org/wiki/Projectively_extended_real_line
[311]: https://en.wikipedia.org/wiki/Riemann_sphere
[312]: https://en.wikipedia.org/wiki/Supernatural_number
[313]: https://en.wikipedia.org/wiki/Irrational_number
[314]: https://en.wikipedia.org/wiki/Fuzzy_number
[315]: https://en.wikipedia.org/wiki/Transcendental_number
[316]: https://en.wikipedia.org/wiki/P-adic_number
[317]: https://en.wikipedia.org/wiki/Solenoid_(mathematics)#p-adic_solenoids
[318]: https://en.wikipedia.org/wiki/Profinite_integer
[319]: https://en.wikipedia.org/wiki/Normal_number
[320]: https://en.wikipedia.org/wiki/Number#Main_classification
[321]: https://en.wikipedia.org/wiki/List_of_types_of_numbers
[322]: https://en.wikipedia.org/wiki/Template:Infinitesimals
[323]: https://en.wikipedia.org/wiki/Template_talk:Infinitesimals
[324]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Infinitesimals
[325]: https://en.wikipedia.org/wiki/Adequality
[326]: https://en.wikipedia.org/wiki/Leibniz's_notation
[327]: https://en.wikipedia.org/wiki/Integral_symbol
[328]: https://en.wikipedia.org/wiki/Criticism_of_nonstandard_analysis
[329]: https://en.wikipedia.org/wiki/The_Analyst
[330]: https://en.wikipedia.org/wiki/The_Method_of_Mechanical_Theorems
[331]: https://en.wikipedia.org/wiki/Cavalieri's_principle
[332]: https://en.wikipedia.org/wiki/File:German_integral.gif
[333]: https://en.wikipedia.org/wiki/Nonstandard_calculus
[334]: https://en.wikipedia.org/wiki/Smooth_infinitesimal_analysis
[335]: https://en.wikipedia.org/wiki/Constructive_nonstandard_analysis
[336]: https://en.wikipedia.org/wiki/Infinitesimal_strain_theory
[337]: https://en.wikipedia.org/wiki/Differential_(mathematics)
[338]: https://en.wikipedia.org/wiki/Standard_part_function
[339]: https://en.wikipedia.org/wiki/Transfer_principle
[340]: https://en.wikipedia.org/wiki/Hyperinteger
[341]: https://en.wikipedia.org/wiki/Increment_theorem
[342]: https://en.wikipedia.org/wiki/Monad_(nonstandard_analysis)
[343]: https://en.wikipedia.org/wiki/Internal_set
[344]: https://en.wikipedia.org/wiki/Hyperfinite_set
[345]: https://en.wikipedia.org/wiki/Law_of_continuity
[346]: https://en.wikipedia.org/wiki/Overspill
[347]: https://en.wikipedia.org/wiki/Microcontinuity
[348]: https://en.wikipedia.org/wiki/Transcendental_law_of_homogeneity
[349]: https://en.wikipedia.org/wiki/Pierre_de_Fermat
[350]: https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy
[351]: https://en.wikipedia.org/wiki/Leonhard_Euler
[352]: https://en.wikipedia.org/wiki/Analyse_des_Infiniment_Petits_pour_l'Intelligence_des_Lignes_Courbes
[353]: https://en.wikipedia.org/wiki/Elementary_Calculus:_An_Infinitesimal_Approach
[354]: https://en.wikipedia.org/wiki/Cours_d'analyse
[355]: https://en.wikipedia.org/wiki/Help:Authority_control
[356]: https://www.wikidata.org/wiki/Q875333#identifiers
[357]: https://d-nb.info/gnd/4439590-5
[358]: https://id.worldcat.org/fast/1139537
[359]: https://id.loc.gov/authorities/sh87000053
[360]: https://catalogue.bnf.fr/ark:/12148/cb12269146s
[361]: https://data.bnf.fr/ark:/12148/cb12269146s
[362]: https://www.nli.org.il/en/authorities/987007534216205171
[363]: https://www.idref.fr/031485111
[364]: https://lux.collections.yale.edu/view/concept/568613b5-f810-4531-bd86-4cb623e1d60d
[365]: https://en.wikipedia.org/w/index.php?title=Surreal_number&amp;oldid=1363274242
[366]: /wiki/Help:Category
[367]: /wiki/Category:Combinatorial_game_theory
[368]: /wiki/Category:Mathematical_logic
[369]: /wiki/Category:Infinity
[370]: /wiki/Category:Real_closed_field
[371]: /wiki/Category:John_Horton_Conway
[372]: /wiki/Category:Nonstandard_analysis
[373]: /wiki/Category:Numbers
[374]: /wiki/Category:Articles_with_short_description
[375]: /wiki/Category:Short_description_is_different_from_Wikidata
[376]: /wiki/Category:All_articles_with_unsourced_statements
[377]: /wiki/Category:Articles_with_unsourced_statements_from_October_2025
[378]: /wiki/Category:Wikipedia_articles_needing_clarification_from_February_2026
[379]: /wiki/Category:Pages_that_use_a_deprecated_format_of_the_math_tags
