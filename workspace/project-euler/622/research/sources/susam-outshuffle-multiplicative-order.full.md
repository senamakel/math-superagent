<!-- source: https://susam.net/from-out-shuffles-to-multiplicative-order.html | converted from HTML -->

From Out Shuffles to Multiplicative Order - Susam Pal

# From Out Shuffles to Multiplicative Order

By **Susam Pal**on 23 Mar 2011

\( \gdef\ord{\operatorname{ord}} \)

## Out Shuffles

A *perfect riffle shuffle*of a deck of cards involves splitting the deck into two halves (one in each hand) and then alternately dropping one card from each half till all cards have fallen. If the shuffling is done in such a manner that the bottom and the top cards remain preserved at their positions, then it is an *out shuffle*.

## Problem

Here is a problem that a colleague asked me recently while discussing shuffling techniques:

How many out shuffles do we need to perform on a deck of 52 cards to return the deck to its initial state?

## Solution

The solution to this problem is rather long, so it has been split into three parts below.

### Part 1: Congruence Relation

Let us assume that there are \( n \) cards where \( n \) is a positive even integer. Let us denote these cards as \( c_0, c_1, \dots, c_{n-1} \) where \( c_0 \) is the card at index \( 0 \) (top of the deck), \( c_{n - 1} \) is the card at index \( n - 1 \) (bottom of the deck) and \( c_i \) is the card at index \( i \) where \( 0 \le i \le n - 1. \)

For example, if we have \( 8 \) cards, then the cards are denoted as \[ c_0, c_1, c_2, c_3, c_4, c_5, c_6, c_7. \] After the first out shuffle, these cards are now in this order: \[ c_0, c_4, c_1, c_5, c_2, c_6, c_3, c_7. \]

From the problem description and the example above, we see that after a single out shuffle, a card at index \( i \) moves to index \( 2i \bmod (n - 1) \) for \( 0 \le i \lt n - 1 \) and the card at index \( n - 1 \) remains at the same place.

After \( m \) shuffles a card at index \( i \) moves to index \( (2^m i) \bmod (n - 1) \) for \( 0 \le i \lt n - 1. \) The card at index \( n - 1 \) always remains at the same place.

The solution to the problem then is the smallest positive integer \( m \) such that \[ 2^m i \equiv i \pmod{n - 1}. \] for all integers \( i \) that satisfy the inequality \( 0 \le i \lt n - 1. \)

In modular arithmetic, we know that \[ ac \equiv bc \pmod{n} \iff a \equiv b \pmod{n / \gcd(c, n)}. \] where \( a, \) \( b, \) \( c \) and \( n \) are integers. Therefore \[ 2^m i \equiv i \pmod{n - 1} \iff 2^m \equiv 1 \pmod{(n - 1) / \gcd(i, n - 1)}. \] Let \( F_{ni} = \frac{n - 1}{\gcd(i, n - 1)} \) where \( 0 \le i \lt n - 1. \) Now the above congruence relation can be written as \[ 2^m \equiv 1 \pmod{F_{ni}}. \]

### Part 2: Multiplicative Order

The smallest positive integer \( m \) that satisfies the above congruence relation is known as the multiplicative order of \( 2 \) modulo \( F_{ni}. \) It is denoted as \( \ord_{F_{ni}}(2). \)

In general, given an integer \( a \) and a positive integer \( n \) with \( \gcd(a, n) = 1, \) the multiplicative order of \( a \) modulo \( n, \) denoted as \( \ord_{n}(a), \) is the smallest positive integer \( k \) such that \[ a^k \equiv 1 \pmod{n}. \] In this problem, \( n \) is even, so \( n - 1 \) is odd as a result of which \( F_{ni} \) is also odd. As a result, \( \gcd(2, F_{ni}) = 1. \) Therefore, the smallest positive integer \( m \) that satisfies the congruence relation \( 2^m \equiv 1 \pmod{F_{ni}} \) is denoted as \( \ord_{F_{ni}}(2). \)

If \( n = 2, \) \( F_{n0} = F_{n1} = 1, \) therefore \( 2^m \equiv 1 \pmod{F_{ni}} \) for \( 0 \le i \lt n - 1 \) and all positive integers \( m. \) This proves the trivial observation that when there are only two cards \( c_0 \) and \( c_1, \) they remain at index \( 0 \) and index \( 1 \) respectively, after any number of out shuffles, i.e. their positions do not change with out shuffles.

#### Case \( n \ge 4 \)

If \( n \ge 4, \) we know that there exists at least one integer between \( 1 \) and \( n - 1 \) that is coprime to \( n - 1 \) because \( \varphi(n) \ge 2 \) for \( n \ge 4 \) where \( \varphi(n) \) represents Euler's totient of \( n. \)

##### Subcase \( i \) is coprime to \( n - 1 \)

For any arbitrary \( n \ge 4, \) let \( i \) be an integer that is coprime to \( n - 1 \) such that \( 1 \lt i \lt n - 1. \) Now \( \gcd(i, n - 1 ) = 1, \) so \( F_{ni} = \frac{n - 1}{\gcd(i, n - 1)} = n - 1. \) As a result, \( \ord_{F_{ni}}(2) = \ord_{n - 1}({2}). \) This shows that any card at index \( i \) such that \( i \) is coprime to \( n - 1 \) requires a minimum of \( \ord_{n - 1}(2) \) out shuffles to return to its initial place.

##### Subcase \( i \) is *not*coprime to \( n - 1 \)

For any arbitrary \( n \ge 4, \) now let us consider the case of a card at index \( i \) such that \( i \) is not coprime to \( n - 1. \) Since \( n - 1 \) is odd, we have \( \gcd(2, n - 1) = 1. \) Therefore, by definition of multiplicative order, \[ 2^{\ord_{n - 1}(2)} \equiv 1 \pmod{n - 1}. \] Since \( F_{ni} \mid n - 1, \) we get, \[ 2^{\ord_{n - 1}(2)} \equiv 1 \pmod{F_{ni}}. \] This shows that a card at index \( i \) such that \( i \) is not coprime to \( n - 1 \) also return to its initial place after \( \ord_{n - 1}(2) \) out shuffles. Actually, it takes only \( \ord_{F_{ni}}(2) \) out shuffles to return the card to its initial place. But \( \ord_{F_{ni}}(2) \mid \ord_{n - 1}(2), \) so \( \ord_{n - 1}(2) = c \ord_{F_{ni}}(2) \) for some positive integer \( c. \) Therefore performing \( \ord_{n - 1}(2) \) out shuffles is same as repeating \( \ord_{F_{ni}}(2) \) out shuffles \( c \) times. Every \( \ord_{F_{ni}}(2) \) brings back the card to its initial position, so repeating it \( c \) times also brings it back to its initial position.

We have shown that a card at index \( i \) such that \( i \) is coprime to \( n - 1 \) takes a minimum of \( \ord_{n - 1}(2) \) out shuffles to return to its initial place. We have also shown that a card at other indices also return to its initial place after the same number of out shuffles. Therefore, it takes a minimum of \( \ord_{n - 1}{2} \) out shuffles to return the deck of cards to its initial state.

#### Case \( n = 2 \)

When there are only \( 2 \) cards in the deck, every out shuffle trivially returns the deck to its initial state. In other words, it takes only \( 1 \) out shuffle to return the deck to its initial state. Indeed \( \ord_{n - 1}(2) = \ord_{1}(2) = 1. \)

We have now shown that for any positive even integer \( n, \) a deck of \( n \) cards returns to its initial state after \( \ord_{n - 1}(2) \) out shuffles.

### Part 3: Computing Multiplicative Order

For a deck of \( 52 \) cards, we have \( n = 52. \) A minimum of \( \ord_{51}(2) \) out shuffles are required to return the deck to its initial state. To compute \( \ord_{51}(2) \) we first enumerate the powers of \( 2 \) modulo \( 51 \): \begin{alignat*}{2} 2^0 & \equiv 1 && \pmod{51}, \\ 2^1 & \equiv 2 && \pmod{51}, \\ 2^2 & \equiv 4 && \pmod{51}, \\ 2^3 & \equiv 8 && \pmod{51}, \\ 2^4 & \equiv 16 && \pmod{51}, \\ 2^5 & \equiv 32 && \pmod{51}, \\ 2^6 & \equiv 13 && \pmod{51}, \\ 2^7 & \equiv 26 && \pmod{51}, \\ 2^8 & \equiv 1 && \pmod{51}. \end{alignat*} The smallest positive integer \( k \) such that \( 2^k \equiv 1 \pmod{51} \) is 8, so \( \ord_51(2) = 8. \) We need \( 8 \) out shuffles to return a deck of \( 52 \) cards to its initial state.

[Comments][1] | [#mathematics][2] | [#combinatorics][3] | [#puzzle][4]


## Links

[1]: ./comments/from-out-shuffles-to-multiplicative-order.html
[2]: ./tag/mathematics.html
[3]: ./tag/combinatorics.html
[4]: ./tag/puzzle.html
