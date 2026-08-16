<!-- source: https://zenodo.org/records/20355936/files/ternary_digits.pdf?download=1 | converted from PDF -->

A CARRY-PACKET OBSTRUCTION FOR POWERS OF
TWO WITH TERNARY DIGITS IN {0, 1}

MICHAEL SPENCER

Abstract. We study the intersection between pure dyadic powers and
ternary digit strings whose digits are restricted to 0 and 1. The first
reduction is immediate: every odd power of 2 is congruent to 2 (mod 3),
and therefore ends in ternary digit 2. Hence every nontrivial admissible
value must be a power of 4. Writing

Re = 4
e − 1
3 ,

one has 4e = 3Re + 1.
The map m ↦→ 3m + 1 merely appends a final ternary digit 1, so the
internal ternary digit structure of 4
e is exactly the digit structure of Re.
The sequence Re satisfies the affine recurrence

Re+1 = 4Re + 1.

Thus the problem is transferred to the carry behavior of the affine rail
under quadrupling.
The central mechanism is ternary self-overlap:

4m = m + 3m.

A ternary word must add to its one-place-left shift without leaving an
unresolved digit 2. We classify the primitive carry-admissible packets
and separate local carry admissibility from dyadic admissibility. The 01-
type artifacts carry a persistent 5-cofactor, while the 21-type artifacts
carry a persistent 7-cofactor. Ternary scaling preserves these reduced
cofactors. The only nontrivial dyadically pure carry packet is

21013 = 64,

which gives 21013 · 4 = 1001113 = 256.
Any separated reuse of this packet has value

64(1 + 3
s),

and for s ≥ 2, the factor 1 + 3s has a non-dyadic cofactor. Therefore
the carry packet cannot scale or recur at a higher ternary level. This
gives a proof by admissibility obstruction: every carry-compatible digit
structure outside the trivial packet and the canonical packet has reduced
cofactor greater than 1, and so cannot be a power of 2.

1. Introduction

Let

A = {n ≥ 0 : the ternary expansion of n contains only the digits 0 and 1}.

Equivalently, n ∈ A if and only if

n = ∑

i∈S 3
i

for some finite set S of nonnegative integers. The central question is when
such a finite triadic artifact can also be a pure dyadic power.
The first obstruction is the final ternary digit. Since

2
k ≡
 {
1 (mod 3), k even,
2 (mod 3), k odd,

every odd exponent is excluded immediately. Thus every nontrivial admis-
sible power has the form 22e = 4
e.
For this reason the natural object is

Re = 4e − 1
3 .

Then 4
e = 3Re + 1.
In ternary, this operation appends a final digit 1. It does not change any
internal digit. Therefore
 4e ∈ A ⇐⇒ Re ∈ A.

The problem is therefore equivalent to determining when the affine sequence

Re = 4e − 1
3
contains no ternary digit 2.
The sequence Re satisfies
 Re+1 = 4Re + 1.

Date: May 23, 2026.
 1

2 MICHAEL SPENCER

This affine progression is conjugate to quadrupling by the map m ↦→ 3m + 1,
since 3(4m + 1) + 1 = 4(3m + 1).
Thus the affine rail and the power progression are parallel lattices. A clean
digit string in one corresponds to a clean internal digit string in the other.
The carry mechanism appears in the identity

4m = m + 3m.

In ternary, 3m is the ternary word for m shifted one digit to the left. There-
fore quadrupling is a self-overlap of a ternary word with its shifted copy. A
digit 2 appears when two unresolved contributions land in the same digit
position. Such a digit can disappear only if the surrounding digit structure
forms a carry-admissible packet.
The key distinction is between carry admissibility and dyadic admissibil-
ity. Some digit packets quadruple cleanly into ternary 0, 1-strings but are
not powers of 2. For example,

1013 = 10 = 2 · 5,

so the 01-type artifact carries a non-dyadic 5-cofactor. Likewise,

213 = 7,

so the 21-type artifact carries a non-dyadic 7-cofactor. These cofactors are
invariant under ternary scaling:

core2,3(3
aC) = core2,3(C),

where core2,3(N ) = N
2ν2(N )3ν3(N ) .

Thus placing an artifact higher in the ternary expansion moves the obstruc-
tion, but does not remove it.
The exceptional nontrivial packet is

21013 = 64.

It is both carry-admissible and dyadically pure, and it gives

21013 · 4 = 1001113 = 256.

The packet cannot be reused at a separated ternary scale. A repeated copy
has the form 64(1 + 3s).
For s ≥ 2, the factor 1 + 3s is not a power of 2, and therefore contributes a
non-dyadic reduced cofactor. The adjacent case s = 1 is exactly the known
transition 64 ↦→ 256.
The next quadrupling gives

1001113 · 4 = 11012213,

which contains ternary digit 2.

A CARRY-PACKET OBSTRUCTION FOR POWERS OF TWO WITH TERNARY DIGITS IN {0, 1}3

The proof developed below is therefore a proof by admissibility obstruc-
tion. We identify the primitive carry-admissible packets, compute their re-
duced cofactors, and show that ternary scaling preserves those cofactors.
The only packets that remain dyadically admissible are the trivial packet
13 and the canonical packet 21013 = 64. Consequently the only admitted
outputs under quadrupling are
4 and 256,

with 1 occurring as the initial value.

2. The affine reduction

Let

A = {n ≥ 0 : the ternary expansion of n contains only the digits 0 and 1}.

The problem is to determine the intersection

A ∩ {2
k : k ≥ 0}.

Lemma 2.1 (Parity reduction). If 2k ∈ A and k > 0, then k is even.

Proof. Modulo 3,
 2
k ≡
 {
1 (mod 3), k even,
2 (mod 3), k odd.

If k is odd, the ternary expansion of 2k ends in digit 2. Thus no odd exponent
k > 0 can occur. □

Hence every nontrivial candidate has the form

2k = 4
e.

Define
 Re = 4e − 1
3 .

Then 4
e = 3Re + 1.

In ternary, multiplication by 3 appends one zero, and adding 1 changes that
appended zero into a final 1. Therefore

Re = (ds · · · d1d0)3 =⇒ 4e = (ds · · · d1d01)3.

Lemma 2.2 (Rail equivalence). For every e ≥ 0,

4
e ∈ A ⇐⇒ Re ∈ A.

Proof. The map m ↦→ 3m + 1 appends a final ternary digit 1 and does not
alter any internal digit. Hence 4e = 3Re + 1 contains a ternary digit 2 if and
only if Re contains a ternary digit 2. □

4 MICHAEL SPENCER

The sequence Re satisfies
 Re+1 = 4Re + 1.

Indeed,
 Re+1 = 4e+1 − 1
3 = 4 4e − 1
3 + 1 = 4Re + 1.

3. Parallel lattice conjugacy

Let
 Pe = 4
e, Re = 4e − 1
3 .

Then Pe = 3Re + 1.

The two progressions are

Pe+1 = 4Pe, Re+1 = 4Re + 1.

These are conjugate under the map

Ψ(m) = 3m + 1.

Proposition 3.1 (Parallel lattice conjugacy). For every m,

Ψ(4m + 1) = 4Ψ(m).

Equivalently, 3(4m + 1) + 1 = 4(3m + 1).

Proof. Directly,

Ψ(4m + 1) = 3(4m + 1) + 1 = 12m + 4 = 4(3m + 1) = 4Ψ(m).
 □

Thus the power lattice and the affine rail lattice are not separate phe-
nomena. A ternary 0, 1-survival event in the power lattice is equivalent to
a ternary 0, 1-survival event in the rail lattice:

Pe ∈ A ⇐⇒ Re ∈ A.

The only difference between the two digit strings is the final digit 1 affixed
by 3m + 1.
The known nontrivial alignment is

R4 = 85 = 100113

and P4 = 3R4 + 1 = 256 = 1001113.

A CARRY-PACKET OBSTRUCTION FOR POWERS OF TWO WITH TERNARY DIGITS IN {0, 1}5

4. Digit phases and admissibility masks

For each ternary digit position j ≥ 0, counted from the right, define

ϕj(e) = ⌊ Re
3j
 ⌋ (mod 3).

Thus ϕj(e) is the j-th ternary digit of Re. The forbidden phase is 2. Define

Mj = {e : ϕj(e) = 2}.

Then Re ∈ A ⇐⇒ e /∈ ⋃

0≤j<ℓ(Re) Mj,

where ℓ(Re) denotes the ternary digit length of Re.
Equivalently, define Q0(e) = Re.
At each step, strip the last ternary digit:

Qj+1(e) =
 {
Qj(e)/3, Qj(e) ≡ 0 (mod 3),

(Qj(e) − 1)/3, Qj(e) ≡ 1 (mod 3).

If Qj(e) ≡ 2 (mod 3),
the branch is obstructed. Thus a surviving rail value is one whose digit
stripping path reaches 0 using only residues 0 and 1.

5. Quadrupling as ternary self-overlap

Definition 5.1 (Reduced cofactor). For a positive integer N , define

core2,3(N ) = N
2ν2(N )3ν3(N ) .

The carry obstruction appears in the identity

4m = m + 3m.

In ternary, 3m is the word for m shifted one place to the left. Thus quadru-
pling is ternary self-overlap:
 m ↦−→ m + m03.

A ternary digit 2 appears exactly when a digit position receives two unre-
solved contributions. Such a digit can be removed only if the surrounding
digits form a carry-admissible packet.
We distinguish two notions.

Definition 5.2 (Carry and dyadic admissibility). A ternary packet is called
carry-admissible if its local overlap under

m ↦→ 4m = m + 3m

can resolve into digits 0 and 1.
It is called dyadically admissible if its integer value is a power of 2.

6 MICHAEL SPENCER

Carry admissibility alone is not enough. A packet may resolve locally
under quadrupling while carrying a prime cofactor outside 2 and 3. By
Definition 5.1, a positive integer N is a power of 2 if and only if

ν3(N ) = 0 and core2,3(N ) = 1.

6. The local carry law

The primitive carry packets used below are not chosen by inspection.
They are forced by the local arithmetic of quadrupling. Since

4m = m + 3m,

quadrupling in ternary adds a word to its one-place-left shift. Thus every lo-
cal obstruction is determined by the interaction of a digit with its immediate
neighbor and the resulting carry.
We first record the complete length-three local law. For a ternary word
u, write [u]3 for its value.

Lemma 6.1 (Length-three carry law). Among all three-digit ternary words
u ∈ {0, 1, 2}3, allowing leading zeros, the words for which 4[u]3 has no
ternary digit 2 are exactly

000, 001, 010, 021, 100, 101, 210.

Their quadruples are u 4[u]3
000 0
001 113
010 1103
021 10013
100 11003
101 11113
210 100103.
Every other three-digit ternary word has a quadruple containing the digit 2.

Proof. This is a finite local check. The values of the seven displayed words
are 0, 1, 3, 7, 9, 10, 21,
and direct multiplication by 4 gives

0, 4, 12, 28, 36, 40, 84,

whose ternary expansions are respectively

0, 113, 1103, 10013, 11003, 11113, 100103.

Each contains only the digits 0 and 1.
For the remaining twenty words u ∈ {0, 1, 2}3, direct evaluation of 4[u]3
gives a ternary word containing at least one digit 2. Since quadrupling is the
one-shift overlap m + 3m, this length-three check is the complete primitive
local carry law. □

A CARRY-PACKET OBSTRUCTION FOR POWERS OF TWO WITH TERNARY DIGITS IN {0, 1}7

Corollary 6.2 (Primitive isolated artifacts). The only primitive isolated
carry artifacts are the singleton artifact 1 and the collapse artifact 21, up to
ternary scaling.
More precisely: 001, 010, 100
are ternary shifts of the singleton artifact 1, while

021, 210

are ternary shifts of the collapse artifact 21. The remaining clean three-digit
word 101
is not primitive; it is the separated sum of two singleton artifacts:

1013 = 1 + 32.

Proof. The previous lemma gives the complete list of clean local three-digit
quadruplings. The words 001, 010, 100 have values 1, 3, 9, so they are just
3a-shifts of 1. The words 021 and 210 have values 7 and 21 = 3 · 7, so they
are 3a-shifts of 213 = 7. Finally,

1013 = 1 + 32,

so it is a composite of two singleton artifacts separated by one zero, not a
new primitive carry packet. □

Remark 6.3 (The block 20 is not independently admissible). The block
20 appears inside some longer carry strings, but it is not an independent
admissible artifact. Indeed,

0203 · 2 = 1103, 1103 · 2 = 2203,

so 0203 · 4 = 2203,
which contains the digit 2. Thus any 20-segment is only a carry propagation
segment inside a larger packet; it is not a primitive artifact. The primitive
collapse artifact is 21.

7. Primitive carry artifacts

By Lemma 6.1 and Corollary 6.2, every primitive isolated local artifact
whose quadruple avoids the digit 2 is, up to ternary scaling, either the
singleton artifact 1 or the collapse artifact 21. The word 101 is not a third
primitive artifact; it is the separated composite 1 + 32.
The 01-type artifact is represented by

1013 = 1 + 32 = 10 = 2 · 5.

More generally,

1010 · · · 1013 = 1 + 9 + 9
2 + · · · + 9r = 9r+1 − 1
8 .

8 MICHAEL SPENCER

These artifacts can quadruple into 0, 1-strings. For example,

1013 · 4 = 11113,

and 101013 · 4 = 1111113.
However, for r ≥ 1, the value is not dyadically pure. Already

1013 = 2 · 5.

Thus the 01-type artifact is carry-admissible but not dyadically admissible,
except for the trivial singleton 13.
The 21-artifact satisfies
 213 · 4 = 10013.

But 213 = 7.
Thus the bare 21-artifact is also carry-admissible but not dyadically admis-
sible.
By Remark 6.3, the block 20 is not an independent admissible artifact; it
is only a carry-propagation segment inside a larger coupled packet.
The exceptional anchored packet is

21013 = 2 · 33 + 1 · 32 + 1 = 64.

It is dyadically pure, and it gives

21013 · 4 = 1001113 = 256.

8. Triadic scaling preserves artifact cofactors

Lemma 8.1 (Triadic scaling preserves the reduced cofactor). For every
positive integer C and every a ≥ 0,

core2,3(3
aC) = core2,3(C).

Proof. Since ν3(3
aC) = a + ν3(C)
and ν2(3
aC) = ν2(C),
we have
 core2,3(3
aC) = 3aC
2ν2(C)3a+ν3(C) = C
2ν2(C)3ν3(C) = core2,3(C).
 □

Thus a factor such as 5 in the 101-artifact or 7 in the 21-artifact is not
removed by placing the artifact higher in the ternary expansion. Ternary
scaling changes only the height of the artifact; it does not change its reduced
cofactor.
For example, 3a1013 = 3
a(1 + 32) = 2 · 3a · 5,

A CARRY-PACKET OBSTRUCTION FOR POWERS OF TWO WITH TERNARY DIGITS IN {0, 1}9

so the cofactor 5 persists. Likewise,

3a213 = 7 · 3
a,

so the cofactor 7 persists.
This is exactly the invariance given by Lemma 8.1.

9. Separation classes and the shift-ratio obstruction

A two-hit artifact at ternary positions a < b has value

3a + 3b = 3
a(1 + 3b−a).

Let s = b − a

be the separation. The scale 3a only moves the artifact. The reduced cofac-
tor is controlled by 1 + 3s.

Indeed, core2,3(3
a + 3a+s) = core2,3(1 + 3s).

The equality follows from Lemma 8.1.

Lemma 9.1 (Separation cofactor). For s ≥ 2,

core2,3(1 + 3s) > 1.

Equivalently, 1 + 3s is not a power of 2 for s ≥ 2.

Proof. If s ≥ 2 is even, then
 3
s ≡ 1 (mod 8),

so 1 + 3s ≡ 2 (mod 8).

Since 1 + 3s > 2, it is not a power of 2.
If s > 1 is odd, then

3s + 1 = (3 + 1)(3s−1 − 3s−2 + · · · − 3 + 1).

The second factor is an odd integer greater than 1. Hence 3s + 1 has a
non-dyadic odd cofactor. □

Lemma 9.2 (Canonical packet non-repetition). Let

C = 21013 = 64.

If s ≥ 2, then core2,3(C(1 + 3s)
) > 1.

The only adjacent reuse is
 C(1 + 3) = 256.

10 MICHAEL SPENCER

Proof. Since C = 64 is a power of 2,

core2,3(C(1 + 3s)) = core2,3(1 + 3s).

For s ≥ 2, Lemma 9.1 gives
 core2,3(1 + 3s) > 1.

Thus every separated reuse has nontrivial reduced cofactor. For the adjacent
case, C(1 + 3) = 64 · 4 = 256. □

The only nonzero adjacent separation that is dyadically pure is

s = 1, 1 + 3 = 4.

This is the precise ratio demanded by quadrupling:

m + 3m = 4m.

A repeated packet at separation s has ratio

1 : 3
s.

Quadrupling requires exactly 1 : 3.
Therefore a repeated packet has the required ratio only at

s = 1.

10. Non-repetition of the canonical packet

Let C = 21013 = 64.
A shifted repetition of this packet has the form

C + 3sC = C(1 + 3s) = 64(1 + 3
s).

By Lemma 9.1, the factor 1 + 3s has nontrivial reduced cofactor for s ≥ 2.
Hence Lemma 9.2 applies.
For s ≥ 2, Lemma 9.1 gives

core2,3(64(1 + 3s)) > 1.

Thus the canonical packet cannot be repeated at a separated ternary scale
and remain dyadic.
The adjacent case s = 1 gives

64(1 + 3) = 256,

which is exactly the known nontrivial success:

21013 · 4 = 1001113.

The next forced quadrupling does not remain in A:

1001113 · 4 = 11012213.

A CARRY-PACKET OBSTRUCTION FOR POWERS OF TWO WITH TERNARY DIGITS IN {0, 1}11

Thus the canonical packet is used at the transition

64 ↦−→ 256,

and it does not propagate to the next power.

11. Bridge cofactor obstruction

The difference between consecutive powers of four is

4e+1 − 4e = 3 · 4
e.

Thus any ternary bridge B from 4e to 4e+1 must satisfy

B = 3 · 4
e.

Equivalently, ν3(B) = 1 and core2,3(B) = 1.
This is stricter than being a multiple of 6. A carry-admissible ternary
artifact may preserve the correct congruence class, but unless its bridge has
exactly one triadic factor and no reduced cofactor outside 2, it cannot be
the difference between consecutive powers of four.
For example, 1 + 32 = 10 = 2 · 5
has persistent cofactor 5, and

1 + 33 = 28 = 22 · 7

has persistent cofactor 7. Scaling by powers of 3 changes neither cofactor.
The known nontrivial bridge is

256 − 4 = 252 = 1001003.

Here 252 = 32(1 + 33) = 22 · 32 · 7.
The bridge alone is not dyadic. It becomes admissible only with the fixed
tail 4 = 113,
because 252 + 4 = 256.
Equivalently, 252
4 + 1 = 64 = 43.

This is the terminal-anchor completion.

Lemma 11.1 (Bridge cofactor obstruction). The difference between consec-
utive powers of four is 4
e+1 − 4e = 3 · 4
e.
Thus any bridge B from 4e to 4e+1 must satisfy

ν3(B) = 1 and core2,3(B) = 1.

12 MICHAEL SPENCER

Thus the bridge condition used later is precisely Lemma 11.1: a bridge
may be carry-compatible, but unless its reduced cofactor is 1, it cannot be
the difference between consecutive powers of four.

12. Admissibility obstruction

The preceding lemmas give the following admissibility principle.

Theorem 12.1 (Admissibility obstruction). Let q be a power of 2. If

4q ∈ A,

then q = 1 or q = 64.

Proof. The operation q ↦→ 4q is the ternary self-overlap

q ↦−→ q + 3q.

By Lemma 6.1 and Corollary 6.2, every primitive isolated local component
of q whose quadruple can avoid the digit 2 is, up to ternary scaling, either
the singleton artifact 1 or the collapse artifact 21. The clean word 101 is
not a third primitive packet; it is the separated composite 1 + 32.
The nontrivial singleton composites are carry-admissible but not dyadi-
cally admissible. For example,

1013 = 1 + 32 = 10 = 2 · 5.

By Lemma 8.1, every ternary shift of this artifact has the same reduced
cofactor 5. More generally, separated singleton artifacts have the form

3
a(1 + 3s),

and by Lemma 9.1, every separation s ≥ 2 has nontrivial reduced cofactor.
The collapse artifact is also carry-admissible but not dyadically admissible
in its bare form: 213 = 7.
Again, by Lemma 8.1, every shifted copy 3a213 retains reduced cofactor 7.
The only anchored collapse packet whose entire value is dyadically pure
is 21013 = 64.
It gives 21013 · 4 = 1001113 = 256.
By Lemma 9.2, any separated reuse of this packet has value

64(1 + 3s),

and has nontrivial reduced cofactor for every s ≥ 2. The adjacent case s = 1
is exactly the known transition
 64 ↦→ 256.

Finally, 1001113 · 4 = 11012213 /∈ A,

A CARRY-PACKET OBSTRUCTION FOR POWERS OF TWO WITH TERNARY DIGITS IN {0, 1}13

so the canonical packet does not propagate to the next quadrupling.
Thus every carry-admissible structure other than the trivial packet 13
and the canonical packet 21013 has nontrivial reduced cofactor. Since q is
assumed to be a power of 2, Definition 5.1 forces

q = 1 or q = 64.
 □

13. Final reduction

Theorem 13.1 (Final reduction). The powers of two admitted by the ad-
missibility obstruction are 1, 4, 256.

Proof. Let 2k ∈ A. If k = 0, then 2k = 1.
If k > 0, Lemma 2.1 gives that k is even. Write

k = 2e.

Then 2k = 4
e.
By Lemma 2.2, this is equivalent to the corresponding rail value Re having
no ternary digit 2, but for the final reduction we use the quadrupling form
directly.
If e = 1, this gives 4 = 113.
If e > 1, write 4
e = 4q, q = 4
e−1.
The number q is a power of 2, and 4q ∈ A. By Theorem 12.1,

q = 1 or q = 64.

Therefore 4q = 4 or 4q = 256.
Together with 20 = 1, the admitted values are

1, 4, 256.
 □
