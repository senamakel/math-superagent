<!-- source: https://arxiv.org/pdf/2601.17832 | converted from PDF -->

COMPUTING BOUNDED SOLUTIONS TO LINEAR
DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS

MAX A. ALEKSEYEV

The George Washington University
Washington, DC, USA

Abstract. We propose an efficient computational method for finding all so-
lutions n ≤ U to the Diophantine equation aσ(n) = bn + c, where integer
coefficient a, b, c and an upper bound U are given. Our method is implemented
in SageMath computer algebra system within the framework of recursively
enumerated sets and natively benefits from MapReduce parallelization. We
used it to discover new solutions to many published equations and close gaps in
between the known large solutions, including but not limited to hyperperfect
and f -perfect numbers, as well as to significantly lift the existence bounds in
open questions about quasiperfect and almost-perfect numbers.

1. Introduction

The sum of divisors function, commonly denoted by σ, has fascinated people for
centuries. In particular, it provides elegant characterizations for several important
classes of integers, such as the prime numbers, which are precisely the solutions to
σ(n) = n + 1, and the perfect numbers, defined by the equation σ(n) = 2n, among
others discussed later in the present paper. While the solutions to the former
equation are completely understood, the latter remains solved only partially as the
existence of an odd perfect number is one of the oldest open questions in number
theory. This question is representative of the rich collection of unresolved problems
concerning equations involving σ [6, Section B2].
The aforementioned equations can be seen as partial cases of the Diophantine
equation:

(1) aσ(n) = bn + c,

where a > 0, b, c are fixed integer coefficients with gcd(a, b, c) = 1 and n is an
integer indeterminate. In the present study, we develop an efficient computational
method for finding all solutions to a given equation (1) below a given upper bound
U . Note that the case a = 1 and c = 0 corresponds to multiperfect numbers, more
specifically b-perfect numbers or just perfect numbers when b = 2. This case has
been the subject of extensive theoretical study (see, for example, references in [6,
Section B1]) as well as large-scale computational searches [5]. Although we do
not exclude the case c = 0 from consideration, it is rather special as it admits
additional optimization techniques that are not available for nonzero values of c.

E-mail address: maxal@gwu.edu.
 1arXiv:2601.17832v1  [math.NT]  25 Jan 2026
2 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS
 2=1·2

6=2·3 10=2·5 14=2·718=2·32 50=2·5254=2·33 58=2·29
 1

3=1·3
 4=1·22

5=1·5 7=1·78=1·2^3 9=1·3^2 11=1·1116=1·24 25=1·5227=1·3332=1·25 49=1·72 59=1·59

15=3·5 21=3·7 57=3·19

12=4·3 20=4·5 28=4·736=4·32 44=4·11 52=4·13

35=5·7 55=5·11

30=6·5 42=6·7

24=8·3 40=8·5 56=8·7 45=9·5
 ...

60=12·5

...

48=16·3 ...

Figure 1. The tree TU for U = 60, where some nodes 1 · p, 2 · p,
and 3 · p with prime p are hidden under ellipses.

Another special case b = 0 corresponds to inverting the sum of divisors function, a
problem we addressed in [1], and thus we delegate this case to the corresponding
software. Accordingly, in the present paper we focus on the general case, without
discussion of any special treatments for b = 0 or c = 0.
We apply our method to many equations of the form (1), particularly those
that are present in the Online Encyclopedia of Integer Sequences (OEIS) [14], and
advance the knowledge about their ”small” solutions by discovering new solutions
and putting both newly discovered and already known solutions in order below sig-
nificantly larger search bounds than previously reported. Similarly, for equations
with no known solutions (such as quasiperfect and almost-perfect numbers [6, Sec-
tion B2]), our method can significantly lift the known lower bounds for potential
solutions.
The paper is organized as follows. We introduce the needed notation in Section 2,
describe the proposed method in Section 3 and its implementation in Section 4,
and then present some practical results in Section 5. We conclude the paper with
discussion in Section 6.
 2. Notation

We start by introducing the notation, which we use throughout the paper:
• spf(n) and lpf(n) denote the smallest and largest prime factor of an integer
n > 1, respectively;
• νp(n) denotes the p-adic valuation of n, i.e. the largest exponent k such
that pk | n;
• Ω(n) and ω(n) denote the number of prime factors of n with and without
multiplicities, respectively;
• τ (n) denotes the number of divisors of an integer n;
• p1 = 2, p2 = 3, p3 = 5, . . . denote the prime numbers in their natural
order.
 3. Method outline

At its core, our approach to solving (1) for n ≤ U is based on representing the
positive integers not exceeding U as the nodes of a tree TU rooted at 1, where
each node n > 1 has the parent n/pνp(n) with p := lpf(n) (Fig. 1). To search for
the solutions, we perform the (restricted) depth-first traversal of TU with a few
important optimization techniques making it efficient, which we describe in the
follow-up subsections. We therefore refer to the nodes of TU as the search space
and to U as the search bound.

LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS 3

Note that the descendants of node m have form mn′, where spf(n
′) > lpf(m)
(thus gcd(m, n
′) = 1) and n
′ ≤ U ′ := U/m satisfies the equation a
′σ(n
′) = b′n′ +
c′ with the coefficients (a′, b
′, c
′) obtained from (aσ(m), bm, c) by canceling their
common factor (see also Section 4.2). That is, at node m, we are essentially solving
the equation (1) with (a, b, c, U ) = (a
′, b
′, c
′, U ′) for n = n
′ with an additional
constraint spf(n′) > lpf(m).

3.1. Shortcuts. Under a shortcut we understand a way to determine the solutions
n = mn′ with Ω(n
′) ≤ 2 or ω(n
′) = 1 among the descendants of a node m in TU ,
without traversing all those descendants. There are two cases to consider.

Case n′ = p
k with k ≥ 1 and prime p ∈ (lpf(m), U ′1/k]. The equation (1) here
takes the form a
′ pk+1−1
p−1 = b
′p
k + c
′, implying that prime p divides a
′ − c′. If a
′ ̸= c
′,
we factor a′ − c′ and try its prime factors as candidate values for p, for each of
which we then determine suitable values of the exponent k. Otherwise, if a′ = c′,
then gcd(a′, b
′) = 1 and ((a′ − b′)p + b′)p(k − 1) = a′, implying that
• for k = 1 and a
′ ̸= b
′, there are no solutions;
• for k = 1 and a
′ = b
′ (thus a′ = b
′ = c
′), any prime p > lpf(m) gives a
solution mp (in our implementation, the case a
′ = b
′ = c
′ does not appear
as it is addressed in pre-processing as explained in Section 4.2);
• for k ≥ 2, we have that pk−1 | a
′ and furthermore k − 1 = νp(a′), that is,
the candidate values for (p, k) are derived from the prime power factors of
a
′.
Among the identified solutions we may or may not discard those with p > U ′1/k, a
choice we discuss in Section 4.5.
An explicit partial case of this shortcut for (a, b, c) = (1, 2, d) is given by the
following easily verifiable claim, which was discovered and stated by multiple people
in the corresponding OEIS sequences (see Section 5.1):

Theorem 3.1 (OEIS [14]). For integers d and ℓ > 0, the number n = 2ℓ−1(2ℓ −
d − 1) is a solution to σ(n) = 2n + d whenever 2
ℓ − d − 1 is prime.

Indeed, here we have m = 2ℓ−1, giving (a′, b
′, c
′) = (σ(m), 2m, d) = (2ℓ −1, 2ℓ, d),
and if p := a
′ − c
′ = 2
ℓ − 1 − d is prime, then the shortcut produces a solution
mp = 2
ℓ−1(2
ℓ − d − 1) stated in Theorem 3.1.

Case n′ = pq with distinct primes p, q, both greater than lpf(m), and pq ≤ U ′.
Here the equation (1) takes the form a
′(p + 1)(q + 1) = b
′pq + c, which we rewrite as
Apq + Bp + Bq + C = 0 with coefficients A := a
′ − b′, B := a′, and C := a′ − c′ (in
practice, we also cancel their common factor to have gcd(A, B, C) = 1). If A = 0,
we check if B | C, in which case we obtain the suitable (p, q) by iterating p over
the primes in the interval (lpf(m), min(D/2, √U ′) with D := −C/B, and testing
q := D − p for primality. Otherwise, when A ̸= 0, we complete the rectangle (the
technique that was known to Brahmagupta born 598 AD [3, Chapter XIII]), i.e.
rewrite the equation as
 (Ap + B)(Aq + B) = B2 − AC,

which allows us to quickly obtain suitable prime pairs (p, q) by factoring and iter-
ating over the divisors of B2 − AC. In the exceptional case B2 − AC = 0, solutions

4 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS

exist only if p := −B/A is a prime satisfying p > lpf(m), and then we report that
any prime q > lpf(m) different from p gives a solution mpq.
Again, here we may obtain some solutions greater than U , and decide whether
or not to report them.

3.2. Pruning with prime wheel. At each node m of TU , the shortcuts described
in the previous section provide us with the solutions n = mn′ satisfying Ω(n
′) ≤ 2
or ω(n′) = 1, and so it remains to focus on finding those with Ω(n
′) ≥ 3 and
ω(n
′) ≥ 2. It immediately follows that spf(n′) ≤ U ′1/3, however, we do not need
this bound as our approach relies on more accurate dynamic bounds as described
below.
Our goal is to generate a set Q containing all feasible prime powers, that is, for
any solution n′ of interest and p := spf(n′), we should have p
νp(n′) ∈ Q. Since Q
defines the set of children {mq : q ∈ Q} of the node m to visit, we want Q to be
as small as possible. We will need the following theorem, which can be seen as a
refinement of Lemma 1 in [7]:

Theorem 3.2. Let n, U , and S be positive integers such that n ≤ U , σ(n) ≥ S,
and spf(n) = pk for some index k. Then for a positive integer ℓ:

• if ℓ ≤ ω(n), then
 ℓ∏

i=1 pk+i−1 ≤ U ;

• if ℓ ≥ ω(n), then
 ℓ∏

i=1
 pk+i−1
pk+i−1 − 1 ≥ S
U .

Proof. Let’s start with the case ℓ = ω(n). Since spf(n) = pk, the ℓ distinct prime
factors of n in increasing order are bounded from below by pk, pk+1, . . . , pk+ℓ−1,
respectively, and therefore

(2)
 ℓ∏

i=1 pk+i−1 ≤ n ≤ U.

For the fraction σ(n)
n , we have the following upper bound:

σ(n)
n = ∏

prime p|n(1 + p + · · · + p
−νp(n)) ≤ ∏

prime p|n
 p
p − 1 .

Since p
p−1 is a decreasing function of p, the following inequality holds:

(3)
 ℓ∏

i=1
 pk+i−1
pk+i−1 − 1 ≥ σ(n)
n ≥ S
U .

The theorem statement now follows from the observation that for a fixed k, the left-
hand sides of the inequalities (2) and (3) represent increasing functions of ℓ. □

We construct the set Q by keeping track of an accurate lower bound ℓ ≤ ω(n′)
(initially ℓ = 2) and an ℓ-tuple of consecutive primes W := (pk, pk+1, . . . , pk+ℓ−1),

LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS 5

starting with W1 = pk (initially pk is the next prime after lpf(m)).1 We refer to W
as the prime wheel of length |W | = ℓ. It supports two operations:2

rolling: corresponds to incrementing k, when the tuple W changes by remov-
ing the first element and appending the next prime (= pk+ℓ) after the last
element of W ;
length increment: is done by appending the next prime (= pk+ℓ) after the
last element of W .
Along with the wheel W , we keep track of the products

Pκ(W ) := ∏

p∈W (p − κ), κ ∈ {0, 1}.

From |W | ≤ ω(n′) and W1 ≤ spf(n
′), it follows that P0(W ) ≤ n′ ≤ U ′, and thus
a
′ σ(n
′)
n′ = b
′ + c′
n′ is bounded from below by

L(W ) :=
 {
b′ + c′
U ′ if c′ ≥ 0;
b′ + c′
P0(W ) if c′ < 0.

For each state of the wheel W , we test the following conditions:
• if P0(W ) > U ′, then by Theorem 3.2 no solutions with spf(n′) ≥ W1 exist,
and we stop the wheel;
• if a′ P0(W )
P1(W ) < L(W ), then by Theorem 3.2 there are no solutions with
ω(n
′) = |W |, and we increment the wheel length.
If neither of the two conditions holds, then we consider p := W1 as a candidate for
spf(n
′). Since ω(n
′) ≥ |W |, the power pt in n
′ must satisfy the inequality p
t P0(W )
p ≤

U ′, and so we add to Q the powers pt for t in the interval [1, 1+⌊logp U ′
P0(W ) ⌋]. Then
we continue with rolling the wheel.
Since P0(W ) grows as the wheel W rolls or grows in length, and sooner or later
the wheel stops. By that time, the set Q captures all feasible prime powers as we
prove in the following theorem:

Theorem 3.3. Let a
′, b
′, c
′, U ′ be defined as above. Suppose n′ ≤ U ′ is a solution
to a′σ(n
′) = b
′n′ + c′ with ω(n′) ≥ 2 and spf(n
′) = pt > lpf(m) for some index
t. Then at a certain point the prime wheel reaches the state with |W | ≤ ω(n′) and
W1 = pt.

Proof. The wheel W starts at length |W | = 2 and W1 being the next prime after
lpf(m). Hence, at the beginning we have W1 ≤ pt and |W | ≤ ω(n
′). Let W ′ :=
(pt, pt+1, . . . , pt+ω(n′)−1). Suppose that W1 ≤ pt. We have:
• if |W | ≤ ω(n′), then

P0(W ) ≤ P0(W ′) ≤ n′ ≤ U ′;

• if |W | = ω(n
′), then again P0(W ) ≤ P0(W ′), which together with Theo-
rem 3.2 further implies

L(W ) ≤ L(W ′) ≤ a′ σ(n
′)
n′ ≤ a
′ P0(W ′)
P1(W ′) ≤ a
′ P0(W )
P1(W ) .

1We do not track the actual value of index k, and we use indices just to underline the relation-
ship between primes in W .
2In practice, both operations on the wheel are done by using a single generator of consecutive
primes.

6 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS

By induction on W1, it now follows that while W1 ≤ pt, the wheel W does not stop
(since P0(W ) ≤ U ′) and cannot grow in length above ω(n′) (since L(W ) ≤ a′ P0(W )
P1(W ) ).
That is, eventually W reaches the state with |W | ≤ ω(n
′) and W1 = pt. □

For the sake of simplicity, we did not include the lower bound for Ω(n′) in the
wheel description and analysis above. In fact, knowing that Ω(n
′) ≥ ℓΩ for some
ℓΩ ≥ 3 provides us with a better lower bound for n′, which is n′ ≥ W ℓΩ−|W |
1 P0(W )
instead of just P0(W ), and thus P0(W ) should be replaced with W ℓΩ−|W |
1 P0(W ) in
the wheel exit condition and the definition of L(W ).

3.3. Case of odd σ. We recognize the case when both a′ and b′ + c
′ are odd. In
this case, for any odd solution n′, we have

σ(n
′) ≡ a
′σ(n
′) = b
′n′ + c′ ≡ b
′ + c′ ≡ 1 (mod 2),

implying that n
′ is an odd square. We take this observation into an account by
adjusting the pruning and construction of the set Q described above. In particular,
when p := spf(n
′) > 2 and hence n′ is an odd square, the wheel stop condition
W ℓΩ−|W |
1 P0(W ) > U ′ changes to W ℓΩ−2|W |
1 P0(W )
2 > U ′, and we restrict our at-
tention only to even exponents t while adding powers pt to Q. Additionally, from
a
′σ(p
t)σ(n
′/pt) = b′n′ + c, it follows that for any prime q | σ(p
t), −b
′c
′ ≡ (b
′)2n′

(mod q), i.e., −b
′c′ is a square residue modulo q. We test this condition by com-

paring Legendre symbol ( −b
′c
′
q ) to −1, and discard t if the equality holds for any
such q.
Similarly, sometimes we can recognize the oddness of σ(n
′) irrespectively of the
parity of n′, e.g., when a
′ and c′ are odd while b′ is even. In this case, n′ can be a
square or twice a square. Correspondingly, we extend the test described above to
p = 2 by computing Legendre symbol ( −2
tb′c
′
q ) = ( −2
t mod 2b′c′
q ). In particular, this
test automatically eliminates the possibility of even solutions for the quasiperfect
numbers satisfying σ(n) = 2n + 1 (see Section 5.1) since for any exponent t ≥ 1,
σ(2
t) = 2
t+1 − 1 has a prime factor q congruent to 3 modulo 4, giving Legendre

symbol ( −2
tb′c′
q ) = ( −2
t+1
q ) = ( −1
q ) = −1.

We also recognize the squareness of n′ when we additionally know the value of
τ (n′) (see Section 4.4) and this value is odd.

3.4. Case of gcd(a
′, c
′) > 1. From gcd(a′, b
′, c
′) = 1, it follows that g := gcd(a
′, c
′)
divides any solution n
′. Suppose that g > 1. If gcd(g, m) > 1, then there are no
solutions as n′ is coprime to m. However, if gcd(g, m) = 1, the prime factors of g
give valid prime factors of n′. In this case, instead of rolling the wheel in search
for spf(n′), we pick the largest prime power pe from the prime factorization of g
and define Q = {p
t : t = e, e + 1, . . . , e + ⌊logp U ′
g ⌋}. Jumping from m to a node
m′ := mq for q ∈ Q facilitates a more narrowed search for n
′.
Since solutions of the form n = m
′n′′ do not have to satisfy the restriction
spf(n
′′) > lpf(m
′) anymore, to properly incorporate such jumps into the search,
we introduce and maintain a lower bound lp for spf(n
′) independent of lpf(m)
(e.g., lp does not change when we jump from m to m
′). Also, to guarantee that
gcd(m, n
′) = 1, we make the prime wheel roll over the set primes exluding the
prime factors of m.

LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS 7

4. SageMath implementation

4.1. RES framework. The described traversal of TU fits nicely the framework of
recursively enumerated set (RES) in SageMath computer algebra system [12]. It
allows efficient traversal the nodes of a forest (tree TU in our case) by specifying
seeds (i.e., the root of TU ) and defining a function succ(t) that computes the set
of successors of a given node t. To simplify computations, we define t as a tuple
(a′, b
′, c
′, m, lp, aux), where the first five elements have the same meaning as in the
previous section, and aux is a dictionary with additional constraints (see Section 4.4
below). So, the tuple t may be viewed as the configuration of node m in TU .

4.2. Configurations reduction. In order to better handle configurations, we de-
fine a local function reduce abc(t), which reduces the given configuration t (e.g.,
by canceling the common factor of a
′, b
′, c
′) and returns the resulting reduced con-
figuration. It recognizes some cases when the given t has no solutions and returns
None, indicating that traversal of the subtree rooted at t should be avoided. For
example, gcd(a
′, b
′, c
′) = 1 but gcd(a
′, c
′) having a prime factor (which has to divide
n′) below lp is such a case.
Another special case recognized by reduce abc is a′ = b
′ = c
′, where any prime
p would be a solution. However, in view of the given m and lp, primes p in the
solution must be restricted to p ≥ lp and p ∤ m. Function reduce abc(t) prints a
message describing the corresponding infinite series of solutions, and avoids solving
this equation by returning None as above. We show an example of an equation with
an infinite series of solutions in Section 5.1 below.
As certain equations of the form (1) have already received significant effort in
computing their solutions, our implementation supports optional referencing to
those ”core” equations (parameter refs) and the corresponding OEIS sequences.
When refs=True, once a configuration t is identified as corresponding to a core
equation, a message with a reference to the corresponding OEIS sequence is printed
and no processing of t takes place. In particular, equations (a′, b
′) = (1, 2) and small
even c′ (discussed in Section 5.1) can be referenced this way as their solutions below
1020 can be queried from the OEIS.

4.3. MapReduce parallelization. The primary benefit of the RES framework is
a readily-available parallelization via the MapReduce mechanism [8] present in
SageMath. Besides the parallelized traversal, it supports parallel processing of
each visited node t via a user-defined function proc(t), which computes the result
(e.g., set of solutions) for node t, and those results then can be combined over
all visited nodes. In our case, while the prime wheel (that computes successors)
is implemented inside succ(t) function, computing the shortcuts (that produces
actual solutions) are conveniently implemented inside proc(t).

4.4. Additional constraints. It is possible to further narrow the traversal by
enforcing additional constraints. Our implementation supports the following con-
straints via optional parameters:
• squarefreeness of n (parameter squarefree);
• evenness of n (parameter even only);
• coprimality to a given integer (parameter coprime to);
• bounds for ω(n) and Ω(n) (parameters omega and bigomega, respectively);
• a prescribed value for τ (n) (parameter numdiv).

8 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS

Nontrivial constraints, whether they are derived from the given parameters or ob-
tained while rolling the prime wheel in succ() function, are passed (in aux dic-
tionary) from a parent node to its children to propagate a narrowed search. Also,
such constraints can save time while computing shortcuts in proc() function: for
example, a bound like ω(n′) ≥ 2 implies that the case n
′ = pk is impossible and
can be skipped, and similarly a bound like Ω(n′) ≥ 3 implies that the case n = pq
is impossible.

4.5. Solutions above U . As we already noted, the shortcuts described in Sec-
tion 3.1 can potentially produce some solutions above U . In our implementation,
we have control over whether to ignore or report such large solutions (parameter
strict). In our computational experiments, some of which are described in the next
section, large solutions—whether previously known or newly discovered—happen
to inspire us to increase the search bound and thus eventually place those solutions
in order. Unfortunately, some of the discovered solutions, such as the greater of
two 2772-hyperperfect numbers reported in Section 5.2, are too large and remain
inaccessible as a search bound.

4.6. Availability. Our implementation is available from the following GitHub
repository: https://github.com/maxale/multiplicative_functions
Our method is accessible via function res solve sigma abc() in the code file
sigma linear eq.sage. It expects from a caller the required arguments a, b, c,
and U , and also supports optional parameters, some of which are described above.
A full list of supported parameters and their format can be seen directly in the
code.
 5. Applications

In this section, we present some practical results obtained with our method for
various equations of interest.

5.1. Numbers with a small abundance. The abundance of a number n is de-
fined as σ(n) − 2n. The perfect numbers have abundance 0, so the abundance of n
can be viewed as the ”distance” from n to being a perfect number.
The next two famous cases are the numbers with abundance 1 called quasiperfect
numbers, and the numbers with abundance −1 called almost-perfect numbers. Ex-
istence of quasiperfect numbers is an open question. It is known that quasiperfect
numbers must be odd squares greater than 1035 [7]. With our method, we lift this
bound to 1045, which was established in about 440 core-hours (specifically, about 11
hours on a 40-core machine).
3 As we explained in Section 3.3, the squareness and
oddness of the possible solutions is automatically detected and taken into account
by our method.
The only known almost-perfect numbers are the powers of 2. The existing lit-
erature on almost-perfect numbers does not seem to give an explicit lower bound
on almost-perfect non-powers of 2, but focuses on the possible structure of such
numbers (e.g., see [9]). With our method, we establish that no other almost-perfect

3We define core-hours as the wall-clock time in hours taken by the computation times the
number of used cores. Most experiments were run on Intel Xeon 2.40GHz or AMD EPYC 2.2GHz
CPUs.
 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS 9

Abundance OEIS Search bound Core-hours
-2 A191363 1024 42
2 A088831 1024 46
6 A087167 1.5 · 1023 1720
10 A223609 9.6 · 1024 340
14 A141546 1024 40
18 A223610 1.5 · 1023 1440
-22 A223606 1.5 · 1026 436
-24 A385255 1.5 · 1023 246
90 A389703 1.5 · 1023 1805

Table 1. Selected fixed-abundance sequences in the OEIS, along
with the achieved search bounds and the approximate running time
taken by the search.

k 2 4 6 12 18 2772 31752
OEIS A007593 A220290 A028499 A028500 A028501 A028502 A034916

Table 2. The sequences of k-hyperperfect numbers (other than
perfect ones) that are present in the OEIS.

numbers exist below 1033, which took about 6540 core-hours. For the odd almost-
perfect number other than 1, we establish that none exist below 1047, which took
about 1272 core-hours.
In general, numbers with an odd abundance are much sparser than those of
even abundance, since an odd abundance of n implies the oddness of σ(n), and
thus n must be a square or twice a square. The Online Encyclopedia of Integer
Sequences [14] contains sequences for each even abundance in the interval [−32, 32]
as well as for abundances in {−42, −54, ±64, ±90, 128}. With our method, we have
routinely completed these sequences with all terms below 1020. For some of them
we actually reached a larger bound, typically chosen to match some term discovered
by the shortcuts (e.g., a term produced by Theorem 3.1). In Table 1, we list some
of largest bounds we achieved and the corresponding running time in core-hours.
We remark that the numbers of abundance 12 contain an infinite subsequence
(6pk)k≥3 and thus the corresponding OEIS sequence A141545 is mostly composed
of small terms from this subsequence. Our method correctly identifies this infinite
subsequence (by printing a message about it) and focuses on searching sporadic
solutions outside it. Those sporadic solutions can seen as a subsequence of the
OEIS sequence A234238, which lists sporadic solutions to a more general congruence
σ(n) ≡ 6 (mod n) and which we solved below 10
24.

5.2. Hyperperfect numbers. Hyperperfect numbers represent another gener-
alization of perfect numbers [6, Section B2]. A positive integer n is called k-
hyperperfect for some integer k if n = 1 + k(σ(n) − n − 1), where σ(n) − n − 1 can be
seen as the sum of divisors of n other than 1 and n. The 1-hyperperfect numbers
are exactly the perfect ones. McCranie [10] tabulated hyperperfect numbers below
1011 and identified a few values of k of particular interest. Besides the perfect
numbers, the OEIS contains sequences of k-hyperperfect numbers listed in Table 2.

10 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS

Noting that the defining equation for k-hyperperfect numbers has the form (1)
with (a, b, c) = (k, k+1, k−1), we apply our method for determining all terms in the
cited sequences below bounds of at least 10
20. Besides pushing the search bounds
and putting known terms in order, we discovered some previously unknown hyper-
perfect numbers, such as the following two 2772-hyperperfect numbers composed
of 3 and 4 primes, respectively:

47268697363953913 = 2791 · 411409 · 41166127

and
 186690534609915040044368953 = 5237 · 6173 · 128669 · 44881723181837.

While the former number is below our search bound and is proved to be the fifth
2772-hyperperfect number in order, the latter one currently remains out of reach
and thus its order number is unknown.
While 2-hyperperfect numbers satisfy the equation 2σ(n) = 3n + 1, the OEIS
sequence A063906 lists solutions to a similar equation 2σ(n) = 3n + 3, which can
be also written as σ(n) = 3
2 (n + 1) to somewhat resemble perfect numbers. We
determined all solutions to this equation below 3.7 · 10
23, which took us 6336 core-
hours, as well as discovered some previously unknown terms above that bound.

5.3. f -perfect numbers. For a given arithmetic function f , f -perfect numbers are
defined [11] as integers n satisfying 2f (n) = ∑

d|n f (d). For the identity function
f , they are exactly the perfect numbers, and thus f -perfect numbers represent yet
another generalization of the perfect numbers. The OEIS contains a few sequences
listing f -perfect numbers, including f (x) = x + 1 (sequence A066229) and f (x) =
x − 1 (sequence A066230).
Note that when f is a linear function, say f (n) = un + v with integer coefficients
u, v, then the defining equation of f -perfect numbers becomes 2(un + v) = uσ(n) +
vτ (n). For a fixed value of τ (n) = d it takes the form (1) with (a, b, c) = (u, 2u, v(2−
d)), for which we can run our method with the additional constraint τ (n) = d (see
Section 4.4). We identify the feasible values of τ (n) as follows.
The bound n ≤ U implies an upper bound for τ (n). For U < 10480, an accurate
bound can be obtained from data present in the OEIS sequence A002182 of highly
composite numbers, which are the numbers k such that τ (k) > τ (ℓ) for all ℓ < k.
Namely, if k is the largest such number with D := τ (k) ≤ U , then for any n ≤ U ,
we have τ (n) ≤ D. We can further quickly identify feasible values of d in the
interval [1, D] by checking if the smallest number m with τ (m) = d (OEIS sequence
A005179) does not exceed U .
Following this route, we determined all (x + 1)-perfect numbers below 1.5 · 1023,
including the following newly discovered term with a rich prime factorization:

20055918935605248255 = 3 · 5 · 73 · 17 · 101 · 719 · 991 · 3186283.

Similarly, we determined all (x − 1)-perfect numbers below 5.9 · 10
20.

6. Concluding remarks

It is hard to come up with an accurate complexity analysis for the proposed
algorithm, but our computational experiments show that it is very efficient in prac-
tice and can reach much larger search bounds than the previously reported in the
literature. They also show (e.g., in Table 1) that its running time is sensitive to the

LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS 11

given coefficients as it may vary significantly for the coefficients the same magnitude
and the same upper bound U .
Empirically, within the explored search bounds, the running time as a function
of U for many equations seems to grow as Θ(rlog10 U ) with a constant r (depending
on the equation coefficients) in the interval [2, 4], although there exist outliers with
smaller and larger values of r. Also, our computations tend to scale up well with
the number of cores (e.g., using 80 cores reduces the running time by a factor
close to 2 as compared to 40 cores). Unfortunately, the performance of the current
MapReduce functionality in SageMath may drastically degrade as the number of
cores gets close or exceeds a hundred,
4 and to be on a safe side in our computational
experiments we used at most 80 cores.
We took a great care about crafting our algorithm at the high level (minimizing
the number of nodes of TU to visit) and fitting it into the RES/MapReduce
framework, but we did not do much about optimization at the lower level. Since
SageMath is Python-based, it does not provide the best performance out of the
box. We expect that cythonization of our implementation or re-implementing it in
a parallelization-aware mid-level programming language (such as Cilk extension of
C++) can bring some- or even many-fold speedup. This is something we plan to
explore in future.
Another possibility for scaling up our method is using parallelization not only
within the cores of a single computer, but also across multiple computers. We
believe it is well amenable to distributing across multiple nodes of a computational
cluster as well as across a variety of computers in a crowd-computing project,
although we did not pursue that in practice.
An obvious drawback of our method is its inability to extend the search from
an already achieved search bound to a larger one. In order to increase the search
bound, the whole computation should be started from scratch.
Recently we used Theorem 1 and a similar computational approach within the
collaborative effort [13] proving that the largest n such that Ln := lcm(1, 2, . . . , n)
is highly abundant is n = 169. In practice, our approach is able to determine if Ln
is highly abundant for n up to a few hundred (surely including all n ≤ 169).
The tree structure on the positive integers (described in Section 3) is somewhat
similar to the one used by Fang [4], although they use multiplication by single
primes rather than prime powers while going down along the tree. Both our and
their search algorithms can be seen as instances of the reverse search [2]. While their
target is not the equation (1) and thus direct comparison of the two approaches is
not possible, they claim that their algorithm and pruning strategy ”can be adapted
to search for ... odd almost-perfect numbers”. However, since their approach was
designed for a different problem, it understandably misses some techniques (e.g.,
what we refer to as shortcuts) that we found essential to the efficient search for odd
almost-perfect numbers.
With a suitable adjustment of the shortcut and pruning techniques, our method
can be used for linear equations with other multiplicative functions. In particular,
we already have an efficient solver for linear equations with Euler’s totient function;
the manuscript describing it is currently in preparation.

4See SageMath’s issue #41115: https://github.com/sagemath/sage/issues/41115

12 LINEAR DIOPHANTINE EQUATIONS WITH THE SUM OF DIVISORS

References

[1] M. A. Alekseyev. Computing the inverses, their power sums, and extrema for Euler’s totient
and other multiplicative functions. Journal of Integer Sequences, 19(5):Article 16.5.2, 2016.
[2] D. Avis and K. Fukuda. Reverse search for enumeration. Discrete Applied Mathematics,
65(1):21–46, 1996. First International Colloquium on Graphs and Optimization. doi:10.
1016/0166-218X(95)00026-N.
[3] L. E. Dickson. History of the Theory of Numbers. Volume II: Diophantine Analysis. Carnegie
Institution of Washington, Washington, DC, 1920.
[4] W. Fang. Searching on the boundary of abundance for odd weird numbers. Preprint
arXiv:2207.12906 [math.NT], 2022. doi:10.48550/arXiv.2207.12906.
[5] A. Flammenkamp. The multiply perfect numbers page. https://wwwhomes.uni-bielefeld.
de/achim/mpn.html, 2023.
[6] R. K. Guy. Unsolved problems in number theory. Problem Books in Mathematics. Springer,
New York, NY, 3rd edition, 2004. doi:10.1007/978-0-387-26677-0.
[7] P. Hagis and G. L. Cohen. Some results concerning quasiperfect numbers. Journal of the
Australian Mathematical Society. Series A. Pure Mathematics and Statistics, 33(2):275–286,
1982. doi:10.1017/S1446788700018401.
[8] F. Hivert. High performance computing experiments in enumerative and algebraic com-
binatorics. In Proceedings of the International Workshop on Parallel Symbolic Computa-
tion, PASCO 2017, New York, NY, USA, 2017. Association for Computing Machinery.
doi:10.1145/3115936.3115938.
[9] M. Kishore. On odd perfect, quasiperfect, and odd almost perfect numbers. Mathematics of
Computation, 36(154):583–586, 1981. doi:10.2307/2007662.
[10] J. S. McCranie. A study of hyperperfect numbers. J. Int. Seqs., 3:Article 00.1.3, 2000.
[11] J. L. Pe. On a generalization of perfect numbers. J. Rec. Math., 31(3):168–172, 2002.
[12] SageMath. version 10.8, 2025. https://www.sagemath.org.
[13] T. Tao et al. Is the least common multiple sequence lcm(1, 2, . . . , n) a subset of the highly
abundant numbers? MathOverflow. https://mathoverflow.net/q/501203 (version: 2025-10-
10).
[14] The OEIS Foundation. The On-Line Encyclopedia of Integer Sequences. http://oeis.org,
2026.
