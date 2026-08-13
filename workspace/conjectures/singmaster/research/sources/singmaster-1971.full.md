<!-- source: https://fermatslibrary.com/s/how-often-does-an-integer-occur-as-a-binomial-coefficient | converted from HTML -->

Fermat's Library | How often does an integer occur as a binomial coefficient? annotated/explained version.

[FERMAT'S LIBRARY][1]

- [Journal Club][2]
- [Librarian][3]
- [Margins][4]
- [Log in][5]

### Comments

**

Ask a question or post a comment about the paper

Join the discussion! Ask questions and share your comments.

[Sign in with Google][6]
[Sign in with Facebook][7]
[Sign in with email][8]

This paper is about the Sigmaster's Conjecture, which to this day s...

To prove the $O( \log a)$ bound we start by defining $N(a)$ as the ...

In 2007, Daniel Kane, a mathematician from Harvard, was able to [im...

3003 occurs twice in its own row, twice in row 78 and twice in rows...

1971] RESEARCH PROBLEMS 385

and so

2

(6)

Z2

<

I

+

2

-

Since X, Y, Z

are

positive integers, inequality (6)

implies that Z can take only

a

finite number of values.

The same

holds for

Y

(on

using (5)) and X (on using

(3) or the relation

X

< Y+Z).

Since X+ Y+Z =,uA,

A

takes only a finite numb er

of values. So do the

sides

a, b, c,

in

view

of relations

(2). Thus

N(O)

is finite

for each positive X>

2.

If

'X

\2

(i.e.,

,Zb 1), we obtain the same conclusion

on using the second

in-

equality

in

(4)

and

proceeding

as before.

We

shall next

show

that

N(X)

=

0 for

X>

V8

(i.e.,

A>

V2).

For such

a

value

of

A

we

have from

(6)

that Z =1. The

relation (5)

then shows

that

Y=

1. Since

X< Y+Z,

we

now

have

X= 1.

Using relations (3)

and

(2),

one obtains

;=

3,

A=V\3,

a=b=c=2.

REMARKS. The remarks made at the beginning

of this note show that

N(1)

=

5

and

N(2)

=1.

Our theorem shows that

N(3)

=

N(4)

=

*

=

0.

It

would be interesting to consider a similar problem

for

a

quadrilateral,

and

in

general,

a

polygon

of

n sides (n> 2).

RESEARCH

PROBLEMS

EDITED By RICHARD

GuY

In

this

Department

the

Monthly

presents easily

stated

research problems dealing

with

notions

ordinarily encountered in

undergraduate mathematics. Each problem should be

accompanied

by relevant references (if any

are

known

to

the author) and by a brief description

of

known

partial

results.

Material should

be

sent to Richard

Guy, Department of

Mathematics, Statis-

tics,

and

Computing Science,

The

University of Calgary, Calgary

44, Alberta,

Canada.

HOW OFTEN DOES

AN

INTEGER OCCUR AS A BINOMIAL

COEFFICIENT?

DAVID

SINGMASTER, Polytechnic of the

South

Bank,

London

Let N(a) be the number

of times a occurs as a binomial

coefficient, (X). We

have

N(1) =oo, N(2) 1,

N(3) =N(4) N(5) =2, N(6) =3,

etc.

Clearly,

for

a>

1, N(a) <

oo.

Below we establish that

N(a)

=

O(log a). We

conjecture that

N(a)

=

0(1), that is, that the

number of solutions of

()

=a is

bounded for a >

1.

Erd6s,

in

a

private

communication, concurs in this conjecture and

states that it

must be very hard. In a later

communication, he suggests trying

to show N(a)

=

O(log log a).

If

we let

M(k)

be the

first integer

a

such that N(a)

=-k,

we

have: M(1) =2,

M(2)

=

3, M(3)

=

6, M(4)

=

10, M(6)

=

120. The next values would

be interesting

to know.

This content downloaded from 128.235.251.160 on Mon, 22 Dec 2014 21:33:41 PM

All use subject to JSTOR Terms and Conditions

386

R. A.

DUKE

[April

PROPOSITION.

N(a)

=

O(log a).

Proof:

Let b be

the

first b

such

that (2)

>

a.

Now

is

monotonically

increasing in

i and

inj;

hence

b+i+b+

)

b

+

b

+

2b

Thus

(+J)

=

a

implies

i

<

b

or

j <

b.

Again

by

monotonicity, for

each value

of

i

(orj),

has at

most one

solution.

Hence

N(a) <

2b.

Now

(>)

_ 2",

so

we have

(

b(b-1)

hence

b

?<log2

a

+ 1,

and

N(a)

?

2

+2

log2

a

=

O(log

a).

Added in

Proof:

I

have

recently

found that

M(8)

=

3003

and

this is the

only

solution to

N(a)

>

8

with

a

<

223.

There

are

six solutions

to

N(a)

=

6

with

a

<

223,

namely:

120,

210,

1540,

7140,

11628, and 24310.

HOW

IS A

GRAPH'S

BETTI

NUMBER

RELATED

TO

ITS

GENUS?

R. A.

DUKE,

University of

Washington

If a

connected

graph G

has v

vertices

and e

edges, the

number

1

-v+e

is

called

the

(1-dimensional)

Betti number

of

G,

denoted

by

:l(G).

This

value,

which is

nonnegative

for

connected

G, was

one of the

first

numerical

characteris-

tics

of

a

graph

studied,

having been

introduced by

von

Staudt [11]

and

Kirch-

hoff

[5]. The

Betti

number

:l(G)

is

also the

rank of

the

fundamental

group

of G

(see

[9],

Ch.

6)

and

is

related

to the

Euler

characteristic of G,

x(G),

by the

equa-

tion

:3(G)

= 1

-X(G).

The

genus of a

graph is

defined in

terms

of its

embeddings in

compact,

closed,

orientable

2-dimensional

manifolds.

Each

such

manifold

can be formed

by

attaching

an

appropriate

number of

"handles" to a

copy of

the

2-sphere.

For

a

manifold M,

the

number of

handles

required

is

called the

genus of

M,

denoted

by

'y(M),

and

is

related to

the Euler

characteristic

of M by

the formula

2'y(M)

=

2-x(M).

Each

graph can

be

embedded

in some

orientable

2-manifold

by

placing

itsvertices on

the

2-sphere and

attaching one

handle to

accommodate

each

edge.

In

general,

however,

such a

construction

yields a

manifold

of

unneces-

This content downloaded from 128.235.251.160 on Mon, 22 Dec 2014 21:33:41 PM

All use subject to JSTOR Terms and Conditions

**

Discussion

3003 occurs twice in its own row, twice in row 78 and twice in rows 14 and 15. $$ \binom{3003}{1} = \binom{78}{2} = \binom{15}{5} = \binom{14}{6} $$ Additionally, it’s the only number known to appear 8 or more times. There are also no known integers which occur in the triangle exactly five or seven times. To prove the $O( \log a)$ bound we start by defining $N(a)$ as the number of solutions of $a=\binom{i+j}{j}=\binom{i+j}{i}$ , with $i,j \geq 1$ (since Pascal's triangle is symmetrical along its central column). Since, $\binom{i+j}{i}$ increases in each of $i$ and $j$ (in other words, if you pick a diagonal and follow it down or pick a column and follow it down the binomial coefficients will always increase), any choice of $i$ or $j$ admits a new solution value for $N(a)$. Now let's suppose that $a$ satisfies $a \leq \binom{2b}{b}$ implies that $i$ or $j < b$, so the solution count $N(a)≤ 2b$. Take the least such $b$. Then $2^{b-1} ≤\binom{2(b−1)}{b−1}≤ a$, $b ≤1+\log_2 a$, and $N(a) ≤ 2 + 2 \log_2 a = O(\log a)$ In 2007, Daniel Kane, a mathematician from Harvard, was able to [improve the result and the current best bound](http://www.emis.de/journals/INTEGERS/papers/h53/h53.pdf) is: $$ N(t) = O\big(\frac{(\log t)(\log \log \log t)}{ (\log \log \ t)^2} \big) $$ This paper is about the Sigmaster's Conjecture, which to this day still remains unsolved. The author, David Singmaster, is an American mathematician who is known for is mathematical puzzles as well as for his mathematical analysis of Rubik's Cube. ![](https://media.springernature.com/original/springer-static/image/art%3A10.1007%2Fs00283-018-9811-9/MediaObjects/283_2018_9811_Figa_HTML.jpg) To understand his conjecture let's first talk about Pascal's Triangle. Pascal's triangle is a number triangle with numbers arranged in staggered rows such that each number is the sum of the two numbers above (starting with 1) and also a binomial coefficient. His conjecture states that we can find a number $a$, so that no value occurs in Pascal’s triangle more than $a$ times ($a \neq 1$). $$ N(a)< \infty $$ ![](https://i.imgur.com/rInVEMh.png)

[FERMAT'S LIBRARY][1]

- team@fermatslibrary.com
1160 Mission Street
San Francisco
California

##### Products

- [Margins][9]
- [Librarian][10]
- [Journal Club][11]

##### Project

- [About][12]
- [Store][13]

[14]

[15]

[16]


## Links

[1]: /
[2]: https://fermatslibrary.com/journal_club
[3]: https://fermatslibrary.com/librarian
[4]: https://fermatslibrary.com/margins
[5]: /users/sign_in
[6]: /users/auth/google_oauth2
[7]: /users/auth/facebook
[8]: /users/sign_in?redirect=https%3A%2F%2Ffermatslibrary.com%2Fp%2Fc27c7b48
[9]: /margins
[10]: /librarian
[11]: /journal_club
[12]: /about
[13]: https://fermatslibrary.com/store
[14]: https://fermatslibrary.com/twitter
[15]: https://fermatslibrary.com/facebook
[16]: https://fermatslibrary.com/instagram
