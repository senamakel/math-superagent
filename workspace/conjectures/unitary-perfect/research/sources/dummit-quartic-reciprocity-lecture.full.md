<!-- source: https://dummit.cos.northeastern.edu/teaching_sp21_4527/4527_lecture_31_quartic_reciprocity.pdf | converted from PDF -->

Math 4527 (Number Theory 2)

Lecture #31 of 37 ∼ April 5, 2021

Cubic and Quartic Reciprocity

Cubic Reciprocity

Arithmetic in Z[i]

The Quartic Residue Symbol

Quartic Reciprocity

This material represents §8.3.4-8.3.5 from the course notes.

The Cubic Residue Symbol

Recall our deﬁnition of our cubic residue symbol:

Deﬁnition
If π is a prime element of O√−3 and N(π) ̸= 3, we deﬁne the

cubic residue symbol [ α
π
 ]
3 ∈ {0, 1, ω, ω2} to be 0 if π|α, and

otherwise to be the unique value among {1, ω, ω2} satisfying[ α
π
 ]

3 ≡ α(N(π)−1)/3 (mod π).

The cubic residue symbol detects cubes, much as the Legendre
symbol detects squares.

Cubic Reciprocity, I

Here is the statement of cubic reciprocity:

Theorem (Cubic Reciprocity in O√−3)

If π and λ are both primary primes in O√−3 with diﬀerent norms
(i.e., with π, λ both congruent to 2 modulo 3, and with

N(π) ̸= N(λ)), then [ π
λ
 ]
3 = [ λ
π
 ]

3.

Some aspects of this result were mentioned by Euler and Gauss,
and results that are essentially equivalent to this one are implied by
some results in Gauss’s papers, but the ﬁrst proof is due to
Eisenstein: indeed, the ring O√−3 is occasionally known as the
Eisenstein integers for this reason.

Cubic Reciprocity, II

The proof is relatively involved and is typically broken into three
cases: when π and λ are both integer primes, when one is an
integer prime, and when both are complex.

The ﬁrst case is trivial, since if p is an integer then [ p
λ
 ]

3 = 1

regardless of the value of λ, as we showed earlier.

The second case requires proving that [ λ
p
 ]

3 = 1 if p is a

prime integer and λ is a prime element, since [ p
λ
 ]
3 = 1 as

noted above.

The third case is the most diﬃcult.

Cubic Reciprocity, III

Example: Verify cubic reciprocity for π = 7 + 3√−3
2 = 5 + 3ω and

λ = 2 + 3√−3 = 5 + 6ω in O√−3.
 We have N(π) = 19 and N(λ) = 31.

By deﬁnition we have[ λ
π
 ]
3 ≡ λ(N(π)−1)/3 ≡ (5 + 6ω)6 ≡ ω2 (mod π).

By deﬁnition we also have[ π
λ
 ]
3 ≡ λ(N(λ)−1)/3 ≡ (5 + 3ω)10 ≡ ω2 (mod λ).

Thus, we see [ λ
π
 ]
3 = [ π
λ
 ]

3, precisely as dictated by cubic

reciprocity.

Cubic Reciprocity, III

Example: Verify cubic reciprocity for π = 7 + 3√−3
2 = 5 + 3ω and

λ = 2 + 3√−3 = 5 + 6ω in O√−3.

We have N(π) = 19 and N(λ) = 31.

By deﬁnition we have[ λ
π
 ]
3 ≡ λ(N(π)−1)/3 ≡ (5 + 6ω)6 ≡ ω2 (mod π).

By deﬁnition we also have[ π
λ
 ]
3 ≡ λ(N(λ)−1)/3 ≡ (5 + 3ω)10 ≡ ω2 (mod λ).

Thus, we see [ λ
π
 ]
3 = [ π
λ
 ]

3, precisely as dictated by cubic

reciprocity.

Cubic Reciprocity, IV

The general approach to most proofs of cubic reciprocity involves
manipulation of Gauss sums.

Deﬁnition

A multiplicative character on Fp is a function χ : F×
p → C such
that χ(ab) = χ(a)χ(b) for all a, b ∈ F×
p .

Equivalently, a multiplicative character is a group homomorphism
from F×
p to C. The Legendre symbol and the cubic residue symbol
are both examples of multiplicative characters.

Deﬁnition
If χ is a multiplicative character on Fp, we deﬁne the Gauss sum

ga(χ) =
 p−1∑

t=1 χ(t)e2πiat/p ∈ C

Cubic Reciprocity, V

Deﬁnition
If χ is a multiplicative character on Fp, we deﬁne the Gauss sum

ga(χ) =
 p−1∑

t=1 χ(t)e2πiat/p ∈ C

The values of the Gauss sum ga(χ) are essentially the discrete
Fourier transform of the function χ(t).
Thus, the values of the Gauss sum completely encode all of
the information that is contained in the values of the function
χ(t), and we may convert back and forth between the values
of ga(χ) and the values χ(t).
As such, if we can compute the value of the Gauss sum for a
character, then it essentially uniquely determines the value of
the character.

Cubic Reciprocity, VI

Thus, to prove cubic reciprocity, the idea is to consider the Gauss

sums for the cubic character χπ(t) = [ t
π
 ]

3 on Fp, where p = ππ.

Using the deﬁnitions, one may prove various identities involving the
Gauss sums:

1. For any character χ, we have ga(χ) = χ(a)−1g1(χ).

2. For any character χ ̸= 1, we have g1(χ)g1(χ) = p.

3. For the cubic residue character χπ, we have g1(χπ)3 = pπ.

By suitably manipulating these identities, we can then show that
χλ(π) = χπ(λ) for all primary primes λ and π, which establishes
cubic reciprocity.

We will illustrate by working through the second case of the
proof (the third case is more diﬃcult but can be done using a
similar method).

Cubic Reciprocity, VII

Proof (Second Case of Cubic Reciprocity):

Suppose q ≡ 2 (mod 3) is an integer prime and π is a
non-integral prime of O√−3, with ππ = p that is 1 mod 3.

Take the (q2 − 1)/3 power of the Gauss-sum identity
g1(χπ)3 = pπ to obtain
g1(χπ)q2−1 ≡ (pπ)(q2−1)/3 ≡ χq(pπ) = χq(π) (mod q)
because χq is multiplicative and χq(p) = 1 as we showed.

Thus, g1(χπ)q2 ≡ χq(π)g1(χπ) (mod q).

Cubic Reciprocity, VII

Proof (continued):
Since q2 ≡ 1 (mod 3) and the value χπ(t) is zero or a cube
root of unity, we have χπ(t)q2 = χπ(t) for all t.
Also, the qth-power map is additive mod q, so

g1(χπ)
q2 =
 [p−1∑

t=0 χπ(t)e2πit/p]q2

≡
 p−1∑

t=0 χπ(t)q2e2πiq2t/p (mod q)

=
 p−1∑

t=0 χπ(t)e2πiq2t/p = gq2(χπ)

= χπ(q−2)g1(χπ) = χπ(q)g1(χπ)

via the Gauss-sum identity ga(χ) = χ(a)−1g1(χ).

Cubic Reciprocity, VIII

Proof (continued):
So, we have now computed two diﬀerent expressions for the
power g1(χπ)q2 modulo q: they are

g1(χπ)q2 ≡ χq(π)g1(χπ) (mod q)

g1(χπ)q2 ≡ χπ(q)g1(χπ) (mod q)

Multiplying both sides by g1(χπ) and using the Gauss-sum
identity g1(χπ)g1(χπ) = p then yields

χq(π)p ≡ χπ(q)p (mod q).

So, since p is invertible modulo q, we may cancel it to deduce
that χq(π) ≡ χπ(q) (mod q).
At last, this congruence implies the equality χq(π) = χπ(q),
which is exactly cubic reciprocity in this case.

Cubic Reciprocity, IX

We can use cubic reciprocity to calculate the cubic residue symbol[ α
π
 ]

3, after we ﬁnd the prime factorization of the element α, using

the same “ﬂip-and-invert” procedure we use for evaluating
Legendre symbols.

Explicitly, if we write α = u · (1 − ω)k λ1λ2 · · · λn where the λi
are primary primes, then we only need to compute the cubic

residue symbols [ u
π
 ]
3, [ 1 − ω
π
 ]
3, and [ λi
π
 ]
3.

Cubic Reciprocity, X

It remains to compute the residue symbols [ u
π
 ]
3 and [ 1 − ω
π
 ]
3.

The residue symbol [ u
π
 ]

3 we can compute using the deﬁnition

since u = ±ωk and [ ω
π
 ]
3 = ω(N(π)−1)/3, so [ ω
π
 ]
3 = 1, ω, or

ω2 when N(π) ≡ 1, 4, or 7 modulo 9 (respectively), and[ −1
π
 ]

3 = 1.

The residue symbol [ 1 − ω
π
 ]

3 is more diﬃcult to compute,

but its value can be shown to be equal to ω2(p+1)/3 if π = p
is an integer prime, and it is equal to ω2(a+1)/3 if π = a + bω
is a primary prime.

Arithmetic in Z[i], I

We close with a brief discussion of quartic reciprocity, which (in
analogy with quadratic and cubic reciprocity) gives a reciprocity
law involving fourth powers.

The values of the quartic residue symbol will be fourth roots
of unity, just as the values of the cubic residue symbol are
cube roots of unity, so we will work in the ring Z[i].

Other than having to change a few things to accommodate
the fact that we now have four values for the residue symbol,
quartic reciprocity is quite similar to quadratic and cubic
reciprocity.

Arithmetic in Z[i], II

First, some properties of arithmetic in Z[i]:

Proposition (Arithmetic in Z[i])

Let π be a prime of R = Z[i]. Then the following are true:

1. The quotient ring R/(π) is a ﬁnite ﬁeld with N(π) elements.

2. For any nonzero residue class α modulo π, we have
αN(π)−1 ≡ 1 (mod π).

3. If π is not associate to 1 + i, the elements 1, i, −1, and −i
are distinct modulo π, and N(π) − 1 is divisible by 4.

Arithmetic in Z[i], II

1. The quotient ring R/(π) is a ﬁnite ﬁeld with N(π) elements.
2. For any nonzero residue class α modulo π, we have
αN(π)−1 ≡ 1 (mod π).

Proofs:
These results hold for any prime element π in any quadratic
integer ring.

3. If π is not associate to 1 + i, the elements 1, i, −1, and −i
are distinct modulo π, and N(π) − 1 is divisible by 4.

Proof:
If any of 1, i, −1, −i are equivalent modulo π, then π must
have a common factor with (1 + i)(1 − i) = 2, which it cannot.
The second statement follows from Lagrange’s theorem
applied to the subgroup {1, i, −1, −i} of residues modulo π.

Arithmetic in Z[i], III

Now we can deﬁne the quartic residue symbol by looking at a
factorization, just as with the quadratic and cubic residue symbols.

If π is a prime element of odd norm in Z[i] and π ∤ α, then
since N(π) − 1 is divisible by 4, we can factor the expression
αN(π)−1 − 1 ≡ 0 in Z[i]/π as
(α(N(π)−1)/4 − 1) · (α(N(π)−1)/4 + 1) · (α(N(π)−1)/4 + i) ·
(α(N(π)−1)/4 − i) ≡ 0 (mod π).

Since Z[i]/(π) is an integral domain, this means α(N(π)−1)/4 is
equivalent to one of 1, −1, i, −i modulo π.

Arithmetic in Z[i], IV

Now we can deﬁne the quartic residue symbol:

Deﬁnition
If π is a prime element of Z[i] and N(π) ̸= 2, we deﬁne the
quartic residue symbol [ α
π
 ]
4 ∈ {0, 1, i, −1, −i} to be 0 if π|α, and

otherwise to be the unique value among {1, i, −1, −i} satisfying[ α
π
 ]

4 ≡ α(N(π)−1)/4 (mod π).

Examples:

1. [ 1+i
3 ]
4 ≡ (1 + i)2 ≡ −i (mod 3), so [ 1+i
3 ]
4 = −i.

2. [ 2+i
4+i ]
4 ≡ (2 + i)4 ≡ −1 (mod 4 + i), so [ 2+i
4+i ]
4 = −1.

Arithmetic in Z[i], V

The quartic residue symbol the same properties as the cubic
residue symbol:

Proposition (Properties of Quartic Residues, I)

Let π be a prime element of Z[i] and N(π) ̸= 2 and let α, β ∈ Z[i].
Then the following hold:

1. If α ≡ β (mod π) then [ α
π
 ]
4 = [ β
π
 ]
4.

2. The symbol is multiplicative: [ αβ
π
 ]
4 = [ α
π
 ]
4
 [ β
π
 ]
4.

3. We have [ α
π
 ]
4 = [ α
π
 ]

4 = [ α
π
 ]3

4 = [ α3

π
 ]

4.

4. If n is an integer not divisible by π, then [ n
π
 ]
4 = 1 or −1.

Proofs: These are straightforward.

Arithmetic in Z[i], VI

The quartic residue symbol has most of the same properties as the
cubic residue symbol:

Proposition (Properties of Quartic Residues, II)

Let π be a prime element of Z[i] and N(π) ̸= 2 and let α, β ∈ Z[i].
Then the following hold:

5. If u is a primitive root modulo π (i.e., an element of order
N(π) − 1 modulo π), then [ u
π
 ]
4 is either i or −i.

6. The quartic residue symbol detects fourth powers and squares:
if α ̸= 0 mod π, then [ α
π
 ]

4 = 1 if and only if α is a quartic

residue modulo π (which is to say, α ≡ β4 (mod π) for some
β), and [ α
π
 ]

4 = −1 if and only if α is a quadratic residue that

is not a quartic residue.

Arithmetic in Z[i], VII

5. If u is a primitive root modulo π (i.e., an element of order
N(π) − 1 modulo π), then [ u
π
 ]
4 is either i or −i.

Proof:
We cannot have u(N(π)−1)/2 ≡ 1 (mod π) since this would
imply u has order at most (N(π) − 1)/2.
6. The quartic residue symbol detects fourth powers and squares:
if α ̸= 0 mod π, then [ α
π ]

4 = 1 if and only if α is a quartic
residue modulo π, and [ α
π ]
4 = −1 if and only if α is a
quadratic residue that is not a quartic residue.

Proof:
By (5), if α = uk then [ α
π ]
4 = (±i)k , which equals +1 if k is
a multiple of 4 and equals −1 if k is even and not a multiple
of 4. These are equivalent to saying α is a quartic residue, and
a quadratic residue that is not a quartic residue, respectively.

Arithmetic in Z[i], VIII

Example: Determine whether 3 + 3i, 6 − i, and 6 are quartic
residues and whether they are quadratic residues modulo
π = 7 + 2i inside Z[i].
 Since N(π) = 53, for 3 + 3i we must calculate the quartic
residue symbol [ 3+3i
7+2i ]
4 ≡ (3 + 3i)(53−1)/4 ≡ (3 + 3i)13 ≡ −i

(mod 7 + 2i). Thus, [ 3+3i
7+2i ]
4 = −i and so 3 + 3i is not a
quartic or quadratic residue modulo 7 + 2i.

Similarly, we have [ 6−i
7+2i ]
4 ≡ (6 − i)13 ≡ 1 (mod 7 + 2i) so
6 − i is a quartic and quadratic residue mod 7 + 2i.

Finally, [ 6
7+2i ]

4 ≡ (6)13 ≡ −1 (mod 7 + 2i) so 6 is a
quadratic but not a quartic residue modulo 7 + 2i.

Arithmetic in Z[i], VIII

Example: Determine whether 3 + 3i, 6 − i, and 6 are quartic
residues and whether they are quadratic residues modulo
π = 7 + 2i inside Z[i].

Since N(π) = 53, for 3 + 3i we must calculate the quartic
residue symbol [ 3+3i
7+2i ]
4 ≡ (3 + 3i)(53−1)/4 ≡ (3 + 3i)13 ≡ −i

(mod 7 + 2i). Thus, [ 3+3i
7+2i ]
4 = −i and so 3 + 3i is not a
quartic or quadratic residue modulo 7 + 2i.

Similarly, we have [ 6−i
7+2i ]
4 ≡ (6 − i)13 ≡ 1 (mod 7 + 2i) so
6 − i is a quartic and quadratic residue mod 7 + 2i.

Finally, [ 6
7+2i ]

4 ≡ (6)13 ≡ −1 (mod 7 + 2i) so 6 is a
quadratic but not a quartic residue modulo 7 + 2i.

Arithmetic in Z[i], IX

Example: Determine whether 2, 3, and 2 + i are quartic residues
modulo 2 + 3i, and also whether they are quadratic residues.
 We compute [ 2
2 + 3i
 ]
4 ≡ 23 ≡ i (mod π). Since this is not 1

or −1, 2 is not a quadratic residue or quartic residue modulo
2 + 3i.

Also, [ 3
2 + 3i
 ]

4 ≡ 33 ≡ 1 (mod π), which means 3 is a

quartic residue (and also a quadratic residue) modulo 2 + 3i.

Finally, [ 2 + i
2 + 3i
 ]

4 ≡ (2 + i)3 ≡ −1 (mod π), which means

2 + i is a quadratic residue but not a quartic residue modulo
2 + 3i.

Arithmetic in Z[i], IX

Example: Determine whether 2, 3, and 2 + i are quartic residues
modulo 2 + 3i, and also whether they are quadratic residues.

We compute [ 2
2 + 3i
 ]
4 ≡ 23 ≡ i (mod π). Since this is not 1

or −1, 2 is not a quadratic residue or quartic residue modulo
2 + 3i.

Also, [ 3
2 + 3i
 ]

4 ≡ 33 ≡ 1 (mod π), which means 3 is a

quartic residue (and also a quadratic residue) modulo 2 + 3i.

Finally, [ 2 + i
2 + 3i
 ]

4 ≡ (2 + i)3 ≡ −1 (mod π), which means

2 + i is a quadratic residue but not a quartic residue modulo
2 + 3i.

Arithmetic in Z[i], X

We can deﬁne a similar notion of a primary prime for Z[i]:

Deﬁnition
A prime element π ∈ Z[i] is primary if it is congruent to 1 modulo
2 + 2i.

Examples:

The primes −3, −7, and 3 + 2i are primary, while 11 and
2 + i are not.

As with the primary elements in O√−3, for all primes except the
primes associate to 1 + i of norm 2, exactly one associate will be
primary.

Arithmetic in Z[i], XI

We can now state quartic reciprocity:

Theorem (Quartic Reciprocity in Z[i])

If π and λ are distinct primes in Z[i] congruent to 1 modulo 2 + 2i,

then [ π
λ
 ]

4 = [ λ
π
 ]

4 · (−1)
 N(π)−1
4 · N(λ)−1
4 .

Some aspects of this result (like the other reciprocity laws) were
conjectured by Euler, and most of it was known to Gauss; a proof
essentially appears in some of his unpublished papers. The ﬁrst
published proof is due to Eisenstein.

Arithmetic in Z[i], XII

Example: Verify quartic reciprocity for π = 3 + 2i and λ = 5 − 4i
in Z[i].
 We have N(π) = 13 and N(λ) = 41.

Then we have [ 3 + 2i
5 − 4i
 ]
4 ≡ (3 + 2i)(41−1)/4 ≡ (3 + 2i)10 ≡ i

(mod 5 − 4i), so [ 3 + 2i
5 − 4i
 ]

4 = i.

Likewise, [ 5 − 4i
3 + 2i
 ]
4 ≡ (5 − 4i)(13−1)/4 ≡ (5 − 4i)3 ≡ i (mod

3 + 2i), so [ 5 − 4i
3 + 2i
 ]
4 = i as well.

Since N(π) − 1
4 · N(λ) − 1
4 is even, the result [ π
λ
 ]
4 = [ λ
π
 ]

4
is in accordance with quartic reciprocity.

Arithmetic in Z[i], XII

Example: Verify quartic reciprocity for π = 3 + 2i and λ = 5 − 4i
in Z[i].

We have N(π) = 13 and N(λ) = 41.

Then we have [ 3 + 2i
5 − 4i
 ]
4 ≡ (3 + 2i)(41−1)/4 ≡ (3 + 2i)10 ≡ i

(mod 5 − 4i), so [ 3 + 2i
5 − 4i
 ]

4 = i.

Likewise, [ 5 − 4i
3 + 2i
 ]
4 ≡ (5 − 4i)(13−1)/4 ≡ (5 − 4i)3 ≡ i (mod

3 + 2i), so [ 5 − 4i
3 + 2i
 ]
4 = i as well.

Since N(π) − 1
4 · N(λ) − 1
4 is even, the result [ π
λ
 ]
4 = [ λ
π
 ]

4
is in accordance with quartic reciprocity.

Arithmetic in Z[i], XIII

Example: Verify quartic reciprocity for π = 3 + 2i and λ = 7 − 2i
in Z[i].
 We have N(π) = 13 and N(λ) = 53.

Then we have [ 3 + 2i
7 − 2i
 ]
4 ≡ (3 + 2i)(53−1)/4 ≡ (3 + 2i)13 ≡ 1

(mod 7 − 2i), so [ 3 + 2i
7 − 2i
 ]

4 = 1.

Likewise, [ 7 − 2i
3 + 2i
 ]
4 ≡ (7 − 2i)(13−1)/4 ≡ (7 − 2i)3 ≡ −1

(mod 3 + 2i), so [ 7 − 2i
3 + 2i
 ]

4 = −1.

Since N(π) − 1
4 · N(λ) − 1
4 is odd, the result [ π
λ
 ]

4 = − [ λ
π
 ]
4
is in accordance with quartic reciprocity.

Arithmetic in Z[i], XIII

Example: Verify quartic reciprocity for π = 3 + 2i and λ = 7 − 2i
in Z[i].

We have N(π) = 13 and N(λ) = 53.

Then we have [ 3 + 2i
7 − 2i
 ]
4 ≡ (3 + 2i)(53−1)/4 ≡ (3 + 2i)13 ≡ 1

(mod 7 − 2i), so [ 3 + 2i
7 − 2i
 ]

4 = 1.

Likewise, [ 7 − 2i
3 + 2i
 ]
4 ≡ (7 − 2i)(13−1)/4 ≡ (7 − 2i)3 ≡ −1

(mod 3 + 2i), so [ 7 − 2i
3 + 2i
 ]

4 = −1.

Since N(π) − 1
4 · N(λ) − 1
4 is odd, the result [ π
λ
 ]

4 = − [ λ
π
 ]
4
is in accordance with quartic reciprocity.

Arithmetic in Z[i], XIV

Like with cubic reciprocity, we can establish quartic reciprocity by
manipulating the Gauss sums for the quartic character

χπ(t) = [ t
π
 ]
4.

Like with cubic reciprocity, the proof is relatively involved and
is typically broken into three cases: when π and λ are both
integer primes, when one is an integer prime, and when both
are complex.

The case where both primes are integers essentially amounts
to quadratic reciprocity.

We will establish the result in one special case, as an
illustration, taking as given the Gauss-sum identities
ga(χ) = χ(a)−1g1(χ), g1(χπ)g1(χπ) = p, and g1(χπ)4 = π3π.

Arithmetic in Z[i], XV

Proof (Second Case):

Let q be a prime congruent to 3 modulo 4 (so that −q is the
primary element associate to q) and π be a non-integral
primary prime with ππ = p.

First, taking the (q + 1)/4th power of the third Gauss-sum
identity g1(χπ)4 = π3π yields g1(χπ)q+1 = (π3π)(q+1)/4.

Since πq ≡ π (mod q), as can be seen by taking the qth
power of (a + bi)q, we see that

g1(χπ)
q+1 ≡ π(q+1)(q+3)/4 (mod q)

= π(q2−1)/4πq+1

≡ χq(π)ππ ≡ χq(π)p (mod q)

by the deﬁnition of the quartic residue symbol.

Arithmetic in Z[i], XVI

Proof (Second Case, continued):
Also note that χπ(t) is a fourth root of unity, so since q ≡ 3
(mod 4) the qth power is the same as the complex conjugate
Since the qth-power map is additive mod q, we have

g1(χπ)
q ≡
 [p−1∑

t=1 χπ(t)e2πit/p]q
 (mod q)

≡
 p−1∑

t=1 χπ(t)
qe2πiqt/p (mod q)

≡
 p−1∑

t=1 χπ(t)e2πiqt/p

≡ gq(χπ) (mod q).

again by the deﬁnition of the Gauss sum.

Arithmetic in Z[i], XVII

Proof (Second Case, continued):

But by the ﬁrst Gauss-sum identity, we have
gq(χπ) = χπ(q)−1g1(χπ) = χπ(−q)g1(χπ) since χπ(q) is a
root of unity.

Putting all of this together yields
χq(π)p ≡ g1(χπ)q+1 ≡ χπ(−q)g1(χπ)g1(χπ) ≡ χπ(−q)p
(mod q) using the second Gauss-sum identity.

Finally, cancelling the factor of p yields χπ(−q) ≡ χq(π) (mod
q), and this congruence implies the equality χπ(−q) = χq(π),
which is the statement of quartic reciprocity in this case.

Closing Remarks, I

We have now discussed quadratic, cubic, and quartic reciprocity
laws.

It is quite reasonable to wonder, then: what about for higher
powers? Is there (for example) a quintic reciprocity law?

The direct answer is: yes, such laws exist, but require more
intricate arguments inside the cyclotomic extension Z[ζp],
where ζn = e2πi/n is a primitive nth root of unity.

For example, quintic reciprocity involves primes from the ring
Z[ζ5]. One proof of the classical version of quintic reciprocity
relies on the geometry of the hyperelliptic curve
y 2 = x 5 + 1/4.

In fact, Eisenstein’s original proofs for cubic and quartic
reciprocity used elliptic functions, and these arguments can be
reformulated to use elliptic curves.

Closing Remarks, II

There are many other classical questions that we have just
scratched the surface of.
For example, we established classiﬁcations of the integers that
can be written in the form a2 + b2, a2 + 2b2, a2 + ab + b2,
and a2 + 3b2.
One may, more generally, ask about representations by
arbitrary quadratic forms (i.e., arbitrary homogeneous
quadratic polynomials in a, b) – this leads into quite deep
directions, and answering this question in full requires
developing class ﬁeld theory.
These various reciprocity laws we have discussed can be
generalized and extended, as was done by Kummer (in
establishing Kummer reciprocity), Hilbert (via his deﬁnition of
the Hilbert symbol), and Artin (who formulated a very general
law known as Artin reciprocity).

Summary

We outlined the proof of the cubic reciprocity law using properties
of Gauss sums.

We developed the quartic residue symbol and established some of
its properties.

We outlined the proof of the quartic reciprocity law using
properties of Gauss sums.

Next lecture: The geometry of numbers.
