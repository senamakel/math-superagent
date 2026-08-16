<!-- source: https://arxiv.org/pdf/1802.08349 | converted from PDF -->

On a dynamical approach to some prime number sequences

Lucas Lacasa1, Bartolo Luque
2, Ignacio G´omez2, and Octavio Miramontes2,3

1School of Mathematical Sciences, Queen Mary University of London, Mile End E14NS London, (United Kingdom)
2Escuela Tecnica Superior de Ingenier´ıa Aeron´autica y del Espacio,
Universidad Polit´ecnica de Madrid, Madrid 28040 (Spain)
3Departamento de Sistemas Complejos, Instituto de F´ısica,
Universidad Nacional Aut´onoma de M´exico, 04510 DF (Mexico)
(Dated: November 8, 2018)

In this paper we show how the cross-disciplinary transfer of techniques from Dynamical Systems
Theory to Number Theory can be a fruitful avenue for research. We illustrate this idea by explor-
ing from a nonlinear and symbolic dynamics viewpoint certain patterns emerging in some residue
sequences generated from the prime number sequence. We show that the sequence formed by the
residues of the primes modulo k are maximally chaotic and, while lacking forbidden patterns, display
a non-trivial spectrum of Renyi entropies which suggest that every block of size m > 1, while admis-
sible, occurs with diﬀerent probability. This non-uniform distribution of blocks for m > 1 contrasts
Dirichlet’s theorem that guarantees equiprobability for m = 1. We then explore in a similar fashion
the sequence of prime gap residues. This sequence is again chaotic (positivity of Kolmogorov-Sinai
entropy), however chaos is weaker as we ﬁnd forbidden patterns for every block of size m > 1. We
relate the onset of these forbidden patterns with the divisibility properties of integers, and estimate
the densities of gap block residues via Hardy-Littlewood k-tuple conjecture. We use this estimation
to argue that the amount of admissible blocks is non-uniformly distributed, what supports the fact
that the spectrum of Renyi entropies is again non-trivial in this case. We complete our analysis by
applying the Chaos Game to these symbolic sequences, and comparing the IFS attractors found for
the experimental sequences with appropriate null models.

I. INTRODUCTION

Number Theory is a millennial branch of pure mathematics devoted to the study of the integers, whose implications
and tentacles -despite the expectations of theorists like Dickson or Hardy- not only pervade today almost all areas
of mathematics but are also at the basis of many technological applications. A particularly interesting and fruitful
bridge to travel is the one linking dynamical systems concepts with number-theoretic ideas, and indeed several
well established subﬁelds in pure mathematics lie at the interface between number theory and dynamics, namely
arithmetic dynamics, dynamics over ﬁnite ﬁelds or Lie groups, symbolic dynamics, to cite some [1, 2].

Quite distant from these in style and focus, physicists have also history of dealing with dynamics, originating in
Classical Mechanics and more recently encompassing areas such as Chaos Theory or Complexity Science. As a matter
of fact, in the last decades physicists with their tools and experimental inclination have started to look at number
theoretic sequences as experimental measurements extracted from some hidden underlying dynamics. Moreover, from
the celebrated coincidence in 1972 between Montgomery’s work on the statistics of the spacings between Riemann
zeta zeros and Dyson’s analogous work on eigenvalues of random matrices in Nuclear Physics [3–5], we have seen,
somewhat unexpectedly, how number theory and physics have built bridges between each other. These connections
range from the reinterpretation of the Riemann zeta function as a partition function [6] or the focus of the Riemann
hypothesis via quantum chaos [7], to multifractality in the distribution of primes [8], computational phase transitions
and criticality originating in combinatoric problems [9–13], or stochastic network models of primes and composites
[14] to cite only a few examples (see [2] for an extensive bibliography).

In this work we aim to illustrate this fertile cross-disciplinary transfer of ideas and tools by tackling from a dynamical
point of view some important sequences that emanate from the prime number sequence, with the aims of exploring
its underlying structure. By using tools originally devised to describe turbulent ﬂuids or to generate fractal patterns,
we ﬁnd that these sequences show compelling signs of chaotic behavior while hiding some unexpected structure. In
an eﬀort to elucidate this dynamical interpretation, we then link these results with the number theoretical properties
of these sequences.

Prime spirals and the residue classes of linear congruences. The Ulam spiral [15] is make by writing
integers in a square spiral and marking the particular position of the prime numbers (see ﬁgure 1 for an illustra-
tion). Using this representation, S. Ulam found that prime numbers tend to distribute and appear mostly on the
diagonals of the spiral. Commonly the primes are marked in a diﬀerent color like in ﬁgure 1 (left) in order toarXiv:1802.08349v1  [math.NT]  22 Feb 2018
2

FIG. 1: (left)The Ulam spiral for the sequence 1, 2 . . . 12, with primes in red. (right) A full 200 x 200 Ulam spiral showing
the primes as individual black dots. Notice the emergent diagonal pattern where the primes tend to accumulate.

distinguish them. The diagonal-like accumulation patterns of primes can be explained by noticing that these corre-
spond to solutions of prime-generating polynomial equations such as the well known Eulerian form f (n) = 4n2 +bn+c.

A simpler spiral that can be constructed to represent the sequence of natural numbers is the so-called diagonal
spiral, where the spiral rotates oﬀ from an initial point and the interval of the distance between successive numbers
is increased by one each two intervals as shown in Figure 2. The resulting spiral accommodates all integer in
four diagonals as shown in Figure 2 (right panel), for N = 100. With the exception of 2, all prime numbers are
accommodated on two opposite diagonals due to the fact that all primes apart besides 2 are odd numbers. As this
spiral is a simple geometric illustration of performing a modular operation (modulo 4), then each arm of the spiral
agglutinates integers of the form 4n + b, with n integer and b = 0, 1, 2, 3. The upper-left spiral arm agglutinates
primes such as {3, 7, 11, 19, 23, 31, ...} of the form 4n + 3, i.e. congruent to 3 modulo 4, and are called Gaussian
primes (this sequence is catalogued as A002145 in OEIS). On the other hand, the bottom-right diagonal agglutinates
the rest of the primes, e.g. {5, 13, 17, 29, 37, 41..} of the form 4n + 1, i.e. congruent to 1 module 4, and are called
Pythagorean primes (sequence A002144 in OEIS). Besides the prime 2, all primes can be expressed as 4n + 1 or
4n + 3 for some n ≥ 0. Our analysis will start by considering a symbolic sequence p(n) mod 4 where p(n) is the n-th
prime, with two symbols {A, B} such that A ≡ p(n) mod 4 = 1, B ≡ p(n) mod 4 = 3 [16]. By virtue of Dirichlet’s
theorem these two symbols occur inﬁnitely often along the prime number sequence.

FIG. 2: (Left panel) The diagonal spiral for the sequence 1, 2 . . . 13, with primes in red. (Right panel) The diagonal spiral for
N = {2 . . . 100}, with primes in blue. The upper-left spiral arm agglutinates primes of the form 4n + 3, called Gaussian primes.
The bottom-right agglutinates the rest of the primes with form 4n + 1, called Pythagorean primes.

Incidentally, note that this initial mapping can be performed with arbitrarily diﬀerent modulus k; i.e. kn + b
with b = 0, 1, 2, ..., k − 1. Suppose that we construct the residue classes formed by taking the primes modulo k.
Dirichlet’s theorem on arithmetic progressions proves that all but a ﬁnite number of primes are congruent with φ(k)

3

diﬀerent residue classes, where φ(·) is the Euler totient function [1]. For instance, since φ(3) = φ(4) = φ(6) = 2,
this means that for k = 3, 4 and 6 the symbolic sequence constructed from taking the residue classes of primes
modulo k is essentially formed by just two symbols (note however that there is always a ﬁnite transient, for
instance for k = 4 the ﬁrst prime p(1) = 2 is the only prime which is not in the residue classes 1 and 3).
In this sense, the sequence formed by Pythagorean and Gaussian primes is just a convenient particular case
to distinguish both types of primes, but one can do this for arbitrary modulus. For instance, for modulus
k = 5, 8, 10, 12 the totient function is 4, so the resulting sequence will have four symbols in these cases, and so
on.In this work we will only consider prime residue sequences with two symbols obtained via taking the primes
modulo k, with k = 3 and 6 (Dirichlet’s theorem guarantees that the density of both symbols is positive in every case).

FIG. 3: A network representation of the prime numbers sequence and state transitions. Prime sequence can be seen as the
result of a Markov Chain deﬁned over a two-state network with certain transition rates. In ﬁgure 4 we depict an illustration of
such a Markov Chain process.

FIG. 4: Transitions between consecutive primes, labelled in terms of twins, cousins and sexies.

The transitions between Pythagorean and Gaussian primes. Once the sequence of Gaussian and Pythagorean
primes (modulus k = 4) has been extracted, we can consider the sequence of transitions between these two classes.
This new symbolic sequence now has 4 symbols, one per transition, i.e. the set {AA, AB, BA, BB}. We construct

4

this sequence by sliding a block-2 window and assigning to each pair of consecutive symbols a new symbol, for
instance the consecutive primes 3 and 5 map into the symbol AB, because 3 is a Gaussian prime (A) and 5 is a
Pythagorean prime (B). This new sequence will be called the transition sequence. The reason for doing this is
inspired in envisaging primes as the result of a Markov Chain deﬁned over a two-state network with certain transition
rates, which would in this case be equivalent to the frequencies of each block-2 string (see ﬁgure 3).

Residue classes of gaps mod k: twins, cousins and sexies. Two consecutive primes on the integer line
separated by a gap g = 2 are known as twin primes (for example 3, 5 are twins). Consecutive primes on the
integer line separated by a gap g = 4 or 6 are known as cousin primes and sexy primes respectively (for example
7, 11 are cousins and 23, 29 are sexies). An illustration of the occurrence of twin, cousin and sexy prime pairs
is shown in ﬁgure 4. Gaps between primes, ever odd except for the number 2 and 3 the only gap with g = 1,
can grow arbitrarily large, so for the sake of studying the properties of gaps with the tools of dynamical systems
theory we need to make the sequence stationary. Again, we do this by taking modulo k and symbolize the gaps
according to the residue class to which they correspond. For k = 6, one can accordingly classify the gaps into
three families: those congruent with 0 mod 6 will be called sexy-like, those congruent with 2 mod 6 will be
called twin-like, and those congruent with 4 mod 6 will be called cousin-like. Incidentally, note that transitions
between the Pythagorean and Gaussian branches are only due to twin-like and sexy-like gaps. The k-tuple
conjecture by Hardy and Littlewood [17, 18] indeed predicts that all admissible k-tuple of primes occur inﬁnitely
often, hence this conjecture suggests that the density of the residue classes 0, 2 and 4 is positive accordingly. Our
third type of sequence under analysis in this work will be the sequence of gap residues g(n) := (p(n+1)−p(n)) mod 6.

The rest of the paper goes as follows: in section II we recall some important tools originating in dynamical systems
and statistical physics for the description of disordered systems from sequence measurements. In section III we apply
these methods to the three types of sequences described above: (i) the symbolic sequence of prime residues p(n)
mod 4 with symbols A (Pythagorean primes) and B (Gaussian primes), (ii) the transition sequence among them with
four symbols: AA, AB, BA and BB and (iii) the gap sequence g(n) mod 6 wit three symbols, A for sexy primes,
B for twin-like primes, and C for cousin-like primes. And interpret these results from both a dynamical and number
theoretical viewpoint. In section IV we discuss our ﬁndings and conclude.

II. TOOLS FROM NONLINEAR AND SYMBOLIC DYNAMICS

A. Enumerating blocks: Spectrum of Renyi entropies

In this subsection we show how to explore in a quantitative and systematic way the abundance of blocks of symbols
that appear in each symbolic sequence, and its dynamical interpretation. A block of size m constitutes a string of
m consecutive symbols in the sequence: is every possible block appearing in the sequence? If so, with what frequency?

Let us consider a dynamical system xt+1 = F (xt), F : X ⊂ R → X ⊂ R and consider a symbolic sequence
S = (s0, s1, . . . ) extracted from a trajectory x0, F (x0), F 2(x0), . . . of this map via a certain partition of the phase
space P into p symbols. In this inﬁnite sequence we are interested in the statistical properties of a generic block of
m consecutive symbols s = [s1 . . . sm]. To fully describe the statistics of these blocks we shall consider the whole
spectrum of so-called Renyi dynamical entropies h(β), with β ∈ R [20] (Renyi entropies, for short) that weight the
measure, the frequency of each block in diﬀerent ways. There are two particular cases that, given their paramount
importance, should be highlighted before a general formula is introduced.

For β = 0, h(0) is called the topological entropy. If A(m) is the set of all admissible blocks (present in the dynamics)
of length m, then the topological entropy can be deﬁned in terms of |A(m)| as:

|A(m)| ∼ e
mh(0) (1)

In other words, h(0) describes how many new diﬀerent admissible blocks can appear in the symbolic sequence as we
increase its length m. We can compute h(0) as:

h(0) = sup
P lim
m→∞ 1
m log |A(m)|. (2)

There is no metric underlying this quantity, we are only counting admissible blocks, hence the label topological.
This is the symbolic analog of the rate of new trajectories that are admissible in a dynamical system as time increases.

5

For β = 1, h(1) reduces to the symbolic version of the well known Kolmogorov-Sinai entropy:

h(1) = sup
P lim
m→∞ −1
m
 ∑

A(m) P (s) log P (s). (3)

Where the summation goes through all the admissible conﬁgurations s and P(s) is the probability of each one of them.
This entropy weights logarithmically the measure of each type of block, it is thus a metric entropy. A traditional
deﬁnition of a chaotic process is associated with a ﬁnite, positive value of h(1), and under suitable conditions this
quantity is, according to Pesin identity [20], equivalent to the sum of positive Lyapunov exponents of the underlying
(hidden) chaotic system.

For β > 1, h(β) deﬁnes a spectrum of Renyi entropies:

h(β > 1) = sup
P lim
m→∞ 1
1 − β 1
m log ∑

A(m)
P (s)
β. (4)

It is known that h(β) is a monotonically decreasing function of β, such that h(β + 1) ≤ h(β). For some chaotic
processes such as the binary shift map [1, 16], one can show that h(β) is independent of β, one then says that the
spectrum collapses to a single value. If h(β) indeed depends on β we say that the system has a non-trivial spectrum
of Renyi entropies.

Two comments are in order. First, note that h(β) are strictly speaking not simple entropies but entropy rates, that
is, they are intensive quantities in the statistical mechanics sense. For convenience, we will also use the following
notation
 h(β) = lim
m→∞ Hm(β)
m ,

where Hm(β) are the Renyi block entropies, also called partial entropies. These are indeed extensive quantities, and
the entropy rate is taken by normalizing these over the block size. Second, note that all these entropies in general
depend on the partition P performed in the phase space of the underlying dynamical system. If the partition is
performed homogeneously, then this essentially depends on the number of symbols, but this is just a particular subset
of all possible partitions. Strictly speaking, in order to ﬁnd the correct value of h(β) one needs to take the supremum
over all possible partitions. We will obviate this step, relying on the fact that for the so-called generation partitions,
these quantities already reach their maximum and therefore the supremum does not need to be taken.

B. IFS and the Chaos Game

The so-called Chaos Game [21–23] is a simple iterative method to construct fractals. Originally, one starts with an
initial point x0 inside a p-vertex polygon and builds a new point x1 by selecting at random one of the p vertices of
the polygon, drawing the segment connecting x0 and the vertex, and ﬁnding the location of the point in the segment
whose distance to the vertex is a certain factor of the distance between x0 and the vertex. This transformation is
an aﬃne transformation, whose iteration deﬁnes a so-called Iterated Function System (IFS), a well-known iterative
method to create fractals [21]. For p = 3 (regular triangle) and a factor 1/2, the attractor of this simple iterative
process is the celebrated Sierpinski gasket, whereas for p = 4 (square) and a factor 1/2, the trajectory is space ﬁlling
and the attractor is the whole square (see ﬁgure 5).

Now, suppose that the process of picking new vertices is not at random, but follows a certain pattern. In that case
the attractor of the IFS is typically a subset of the attractor found by making the Chaos Game. For instance, it is
well known that for p = 4 and a factor 1/2, the attractor of the Chaos Game is the whole square, but if restrictions
on what vertices can be selected based on previous history are applied; i.e. if we introduce temporal correlations in
the stochastic process of vertex selection, in several cases the new attractor is a fractal subset of the square. Given a
symbolic sequence, where symbols can take p diﬀerent values, one can therefore apply the IFS deﬁned above where in
each iteration the selected vertex is not chosen at random but is given by the next element in the symbolic sequence.
Non-random sequences will then in general yield an IFS attractor diﬀerent from the one obtained applying the Chaos
Game, and the concrete shape would be given by the precise way we have to prune a random series to obtain the
symbolic sequence we are working with.
 6

This argument provides a way to construct a geometric representation of the patterns underlying non-random symbolic
sequences, which can be disentangled by comparing them with the object retrieved by applying the Chaos Game (that
would be called the null model, see next section for details). In what follows we will explore the geometric shapes we
ﬁnd by applying the Chaos Game not on random sequences but following the speciﬁc sequences extracted from the
primes.

FIG. 5: IFS attractor for (left panel) a type I null model with p = 4 symbols, (middle panel) a type II null model with p = 4
symbols, (right panel) a type I null model with p = 3 symbols.

III. RESULTS

A. Null models: what to expect if primes lack structure?

What should we expect from a null model? Here we are interested in evaluating whether our prime sequences hides
some degree of correlations or, conversely, these sequences cannot be distinguished from a totally random process. As
such, our null model should consist of a random uncorrelated sequence. However, we have several possibilities to do
that.
 1. Type I: Symbols i.i.d. with uniform and non-uniform probability densities

In such a model, s is a random variable extracted at each time independently with a certain probability distribution
from {s1, . . . , sp}, where p is the number of symbols. For instance, in our case one could draw symbols uniformly
from either {A, B} or {AA, AB, BA, BB}. That is, each of the two or four symbols having a probability 1/2 or 1/4
respectively, to generate a random sequence, which would act as a null model for both the prime residue sequence
and the transition sequence respectively. It is easy to prove that in this case, Hm(β) = log p, independently of β and
m, something that was checked numerically for β = 1 in ﬁgure 6. This means that in the this kind of null model,
all blocks of size m are possible and appear in the symbolic sequence with equal probability. The case β = 0 is
trivial to prove, here we give a sketch of the proof for h(1): in the case all blocks of size m are equiprobable, we have
P (s) = 1/|A(m)| and then
 H(1) = ∑

A(m) P (s) log P (s) = log |A(m)|.

In the case that all possible blocks of size m are admissible, the set of admissible sequences is equal to the set of all
possible sequences N (m). We thus have |A(m)| = |N (m)| = p
m hence

h(1) = lim
m→∞ 1
m log(p
m) = log p.

Furthermore, we can also deﬁne a similar stochastic process where now we draw symbols at random from the set of
symbols not in a uniform way, but instead with a probability that indeed matches the empirical one. This would
be a null model that respects marginal distributions. For instance, for primes residues where the symbol set is
{A, B}, while asymptotically P (A) = P (B) = 1/2, for ﬁnite sequences estimations are systematically larger for A,
something known as the Tchebytchev bias. For the transition sequence where the symbol set is {AA, AB, BA, BB},
empirically we ﬁnd P (AB) = P (BA) ≈ 0.30, P (AA) ≈ 0.21, P (BB) ≈ 0.19: this might account for this bias as

7

P (A) = P (AB) + P (AA) > P (BA) + P (BB) = P (B) (note that for convenience we have not made explicit in the
notation the diﬀerence between asymptotic and estimated probabilities).

In these cases, the null model accounts for this non uniformity in the abundance of symbols and generates a sequence
with non-uniform symbol frequencies which, for ﬁnite m, has by construction metric entropies which are smaller or
equal to the uniform counterpart (this holds as a direct consequence of the second Khinchin axiom). Consider the
case β = 1. For blocks of size m = 1 the entropy H1(1) is:

H1(1) = − ∑

A(1) P (s1) log P (s1) ≈ 1.366 < log 4 ≈ 1.386.

This value holds constant ∀m and one can very easily prove that in this case h(1) = limm→∞ Hm(1)/m = H1(1). A
sketch of the proof is as follows: consider for simplicity the case m = 2, in that case:

H2(1) = ∑

A(2) P (s) log P (s) ≡
 p∑

s1=1
 p∑

s2=1 P (s1, s2) log P (s1, s2)

Since the sequence is by deﬁnition uncorrelated we can factorize P (s1, s2) = P (s1)P (s2) and thus

H2(1) =
 p∑

s1=1
 p∑

s2=1 P (s1, s2) log P (s1, s2) =
 p∑

s1=1 P (s1) log P (s1)
 p∑

s2=1 P (s2) +
 p∑

s1=1 P (s1)
 p∑

s2=1 P (s2) log P (s2) = 2H1(1)

A simple induction concludes the proof. Accordingly, the null model for the prime conﬁguration depicted above
yields Hm/m ≈ 1.366 ∀m, and in general h(β) = H1(β) ≤ log 4 (the inequality saturates for β = 0 as in this
case no metric aspects are concerned, whereas for other values of β we expect the upper bound to be reasonably tight).

Now, what type of IFS attractor is produced by a type I null model? If one performs the Chaos Game for a square
(4 vertices) and a contraction factor 1/2, the process is space-ﬁlling, i.e. the attractor is [0, 1]
2 (the attractor is the
interior of a square with all points visited with equal probability). Hence performing the Chaos Game on a type I
null model with p = 4 symbols is a space-ﬁlling IFS (left panel of ﬁgure 5). On the other hand, for p = 3 a type I null
model yields the Sierpinski gasket as the attractor of the IFS (right panel of ﬁgure 5), point out no correlations.

2. Type II: transitions

After a careful thought it is straightforward to see that the preceding null models are reasonable to explore the
lack of correlations in sequences such as the primes or gaps residues, but not for the prime transition sequence, made
out of {AA, AB, BA, BB}. The reason is simple: suppose that in the sequence at some point we ﬁnd the symbol
AB. The subsequent symbol will describe the transition from B to the next prime, and therefore this next symbol
will necessarily start with the letter B (that is, BA or BB), in other words it will never be a symbol starting with
the letter A. This is simply related to the way of constructing the transition sequence (by sliding a window of size 2
with overlap) hence this process builds spurious correlations and forbidden transitions. As an example: the following
transitions are forbidden:
{AA → BA, AA → BB, AB → AA, AB → AB, BA → BA, BA → BB, BB → AA, BB → AB}.

Accordingly, plenty of possible blocks of m symbols are actually forbidden simply by the way the sequence is created,
not necessarily because there is an intrinsic correlation in the prime sequence. In order to ﬁnd out whether this is the
case, the correct null model to explore is as follows:

• Generate a random sequence via a type I null model with two symbols A and B (where asymptotically p(A) =
p(B), however for ﬁnite size series one should account for Tchebytchev bias),

• Then construct the resulting sequence with p = 4 symbols {AA, AB, BA, BB}.

It is easy to enumerate in this null model the number of possible |N |, admissible |A| and forbidden |F| blocks of size
m, with |N (m)| = |A(m)| + |F(m)|, throught the iterations:

|F(m)| = 4|F(m − 1)| + 2|A(m − 1)|, |A(m)| = |N (m)| − |F(m)|.
 8

With |N (m)| = 4
m and |F(1)| = 0 we can solve the preceding equations and ﬁnd:

|F(m)| = 2
m(2m − 2), |A(m)| = 2
m+1 (5)

Accordingly, in this null models the number of forbidden patterns grows exponentially fast (faster than the number
of admissible ones). The topological entropy of this model is analytically solvable:

h(0) = lim
m→∞ 1
m log A(m) = lim
m→∞ m + 1
m log 2 = log 2,

and Hm(0) = log 2 + (log 2)/m. We ﬁnd that this quantity converges to log 2 after a monotonic decrease.

The IFS attractor of a type II (p = 4) is plotted in the middle panel of ﬁgure 5. The attractor is not anymore the
interior of the square (i.e. an attractor of dimension 2), but a fractal of lower dimension. This resulting fractal shape
is the geometrical equivalent of systematically pruning from N (m) the spurious forbidden patterns discussed above.

3. Type III: Cramer null model

There is a third null model than one could. This is the classical Cramer random model [24], which starts by creating
a stochastic version of the prime number sequence by assigning to each integer x a probability of being prime equal
to 1/ log x. This model is inspired after the prime number theorem, which states that the amount of primes under
N is asymptotic with N/ log N . This latter quantity can be therefore understood as the expected number of primes
under x. If the probability of a number only depends on its ordinal in the line, then the average number of primes
under N is
 π(N ) = ∫ N

2
 dx
log x = Li(N ) ∼ N/ log N

where Li(x) is the oﬀset logarithm integral. This model generates a list of pseudo-primes which statistically
conform to the prime number theorem albeit being essentially uncorrelated from each other. Note that in this form,
Cramer model is not applicable in our case, as it is very likely that such model would generate both even and odd
pseudo-primes, therefore not congruent with the correct residue classes. We therefore slightly modify this model and
assume that each even integer x is a pseudo-prime with null probability, whereas each odd integer x is a pseudo-prime
with probability 2/ log x. From the resulting list of pseudoprimes one can reconstruct the pseudo-prime residues,
pseudo-prime transitions and pseudo-prime gap residues sequences.

We won’t give more details at this point. It is just important to highlight that a deterministic process whose statistics
are equivalent to the corresponding null model is totally indistinguishable from a purely random, uncorrelated process.
The main aim of this work is to explore this hypothesis.

4. Some fully chaotic maps

For the sake of comparison with other deterministic processes, we close this section on null models by considering
several fully chaotic maps: the logistic map xt+1 = 4xt(1 − xt), the binary shift map xt+1 = 2xt mod 1 and the tent
map xt+1 = 2 min{xt, 1 − xt} where in every case x ∈ [0, 1]. All these three maps display chaotic behavior and are
topologically conjugated to each other, thus sharing the same entropic spectrum. For a homogeneous partition of
the interval with p = 2 symbols [0, 1] = [0, 1/2) ∪ [1/2, 1], the symbolic sequences of these maps don’t have forbidden
blocks, meaning that h(0) = log 2. It is also well known that this partition is generating (not only that, it is also a
Markov partition) and thus the entropies reach their supremum over all possible partitions. Furthermore, for these
maps all symbol blocks are equiprobable, hence h(β) = log 2, ∀β. In some sense, these maps are fully chaotic as their
p = 2 symbolic representation has strong randomness properties: one cannot distinguish these from a purely random
sequence of two symbols. As a matter of fact for the binary shift there are actually no diﬀerences at all: the symbolic
sequence in these cases not only induces a topological Markov chain but also a standard Markov chain, meaning that
the sequence has no memory on previous states: the probability of a new symbol is 1/2, irrespective of the previous
history.
 9

Now, the transition sequence has p = 4 symbols, hence for the sake of comparison we ﬁrstly consider an homogeneous
partition of p = 4 symbols for the fully chaotic logistic map. Interestingly, in that case we ﬁnd that this symbolic
sequence has an entropic spectrum h(β) → log 2 < log 4, ∀β ≥ 0 as well. That means that we ﬁnd forbidden patterns
in this conﬁguration. Note that this is not unexpected and can be easily proved as follows: since the partition with
two symbols is generating, the block entropy reaches its supremum over all partitions for that case, which is indeed
log 2, thus any other partition should yield entropies smaller or equal than log 2. On the other hand, an homogeneous
partition with p = 4 symbols is a reﬁnement of the partition with p = 2 symbols, therefore invoking the monotonicity
property of entropies over diﬀerent partitions [19] we have that any reﬁnement of the p = 2 partition should yield
an entropy larger or equal to the one for p = 2, namely log 2. Both conditions are only mutually satisﬁed when the
inequality saturates, what concludes the proof.
The dynamical origin of the forbidden patterns in the fully chaotic logistic map for p = 4 symbols can be
explained in terms of the shape of the unimodal map F (x) = 4x(1 − x). We will focus on a particular example
to elucidate this relation. Deﬁne the symbols as the subintervals A = [0, 1/4), B = [1/4, 1/2), C = [1/2, 3/4]
and D = (3/4, 1]. Then for m = 2, the pattern (A, D) is forbidden (there are a total of 8 forbidden blocks
of size 2). This means that in the symbolic sequence of the logistic map with p = 4 symbols, the symbol A
will never precede the symbol D. The reason is simple: as F is continuous it maps intervals into intervals, and
together with the fact that F (0) = 0, F (1/4) = 3/4, this means that that F : [0, 1/4] → [0, 3/4], so starting
from A we will never reach D. Interestingly enough, one can enumerate in this case the forbidden patterns and,
surprisingly, we ﬁnd that for every m the amount of admissible and forbidden patterns exactly matches the formulas
found for the type II null model. This suggests that one can make an enumeration of the forbidden patterns of the
logistic map via a branching process similar to the one used to enumerate these patterns in the type II random process.

Once these synthetic processes have been detailed, let us consider the results obtained for the numerical experiments.

FIG. 6: (Left) Block entropies Hm(1)/m for diﬀerent symbolic sequences. (Right) Renyi block entropies Hm(β)/m for diﬀerent
values of m and β. All curves seem to converge to log 2.

B. Results and interpretation for the transition sequence

Let us start by analysing the transition sequence. In the left panel of ﬁgure 6 we show that, for the transition
sequence with p = 4 symbols, Hm(1)/m → log 2. This tendency is quantitatively similar for other values of β, see
the right panel of the same ﬁgure, suggesting that h(β) = log 2. This means that in the transition sequence there are
forbidden patterns but those admissible occur equally often. This was indeed expected from the type II null model
analysis displayed above. In the same ﬁgure we have plotted the analytical prediction for Hm(0)/m = log 2+(log 2)/m
from the type II null model, which perfectly matches the numerical experiment. We conclude that the transition
sequence shows strong randomness properties and cannot be distinguished from a purely random process.

Applying the chaos game (contraction factor 1/2) to the transition sequence (ﬁgure 7) shows a clearly fractal shape.
Interestingly, this is the same pattern that one ﬁnds for the symbolic sequence (4 symbols) generated by the tent

10

map. As expected, this is diﬀerent from a null model of type I but identical to a null model of type II (see right panel
of ﬁgure 5), on agreement with the conclusion extracted from our entropic analysis.

FIG. 7: IFS chaos game-like attractor for the prime transition sequence. The attractor has a fractal shape instead of being
space-ﬁlling, however a type II null model can account for such shape, as shown in ﬁgure 5.

C. Results and interpretation for the Primes mod k

The previous results suggest that the apparent lack of total randomness found in the transitions between
Pythagorean and Gaussian primes was only due to the way the sequence was constructed, as a null model of type
II found the same quantitative results. In order to gain a better understanding, we now consider the symbolic
sequences generated via congruences of primes modulo k, where k is such that φ(k) = 2, and we start by computing
the spectrum of Renyi entropies h(β) for diﬀerent k and diﬀerent values of β, results are summarized in ﬁgure 8. In

FIG. 8: (Left) Block entropies Hm(0)/m for symbolic sequences primes mod k, with diﬀerent values of k. We ﬁnd that the
topological entropy is always log 2, suggesting that there are no forbidden patterns in primes modulo k. (Middle) Empirical
Renyi block entropies Hm(β)/m for diﬀerent values of m and β, extracted from the primes modulo 4. The spectrum does not
collapse into a single value.(Right) Empirical Renyi block entropies Hm(β)/m for diﬀerent values of m and β, extracted from
the fully chaotic logistic map xt+1 = 4xt(1 − xt) after symbolization with p = 2 symbols. Results have been computed over a
symbolic sequence of N = 10
6 points, the same size as the one for the primes in the middle and left panels. The spectrum in
this case collapses h(β) = log 2, ∀β as expected according to the topological conjugacy of the fully chaotic logistic map with
the binary shift.

the left panel we consider the topological entropy for k = 3, 4 and 6, for which there are two residue classes with
inﬁnite primes (two symbols). In every case we ﬁnd a smooth convergence with the block size m to an asymptotic

11

value h(0) ≈ log 2, suggesting that there are no forbidden patterns in these sequences as expected. Incidentally, the
reason why H1(0) = log 3 for k = 3, 4 and log 4 for k = 6, and that log 2 is only reached asymptotically in every
case is because depending on k, there are a few initial primes that do not fall into the residue classes with positive
density: for k = 4, 2 ≡ 2(mod 4) ̸= 1, 3; analogously for k = 3, 3 ≡ 0(mod 3) ̸= 1, 2; and ﬁnally for k = 6 as
this is a primorial with two factors we have two primes oﬀ the main residue classes 2 ≡ 2(mod 6), 3 ≡ 3(mod 6) ̸= 1, 5).

On the other hand, in the middle panel of the same ﬁgure we explore the spectrum of Renyi entropies for a particular
modulo k = 4 (results are analogous for k = 3, 6). As the set of transient symbols is ﬁnite, in the case of the KS
and the rest of Renyi entropies that take into account the frequencies of each block this eﬀect is smeared out. The
ﬁrst important observation is that for β = 1, the KS entropy converges to a value 0.685 slightly below log 2 ≈ 0.693.
This small shift could be due to the fact that the density of A’s and B’s, while being asymptotically identical
p(A) = p(B) = 1/2 (Dirichlet), is diﬀerent almost surely for any ﬁnite length sequence: again the famous Tchebytchev
bias. Accordingly, a null model for this case does not yield an entropy equal to log 2 but −p(A) log p(A)−p(B) log p(B).
To check whether this eﬀect is simply a result of the Tchebychev bias, we have also run a type I null model where each
symbol is drawn non-uniformly according to the empirical estimations of p(A) and p(B) for our experimental series.
We ﬁnd p(A) ≈ 0.4998, p(B) ≈ 0.5002 and h(1) ≈ 0.693, which is too close to log 2 to give account for the deviation
observed for the KS entropy. Using a Cramer null model (type III) we also ﬁnd the same result ∀β, h(β) ≈ 0.69. The
only possible solution is that, while there are no forbidden patterns and all blocks of size m are admissible, they don’t
appear equally often and as m increases this heterogeneity builds up stronger.
If that was actually happening, then we should expect that this non-uniformity gets more pronounced for higher values
of β. As a matter of fact, and at odds with what we ﬁnd for the binary shift map and the null models, we indeed
ﬁnd that h(β) for the prime residues seems to be a monotonically decreasing function on β: for higher order values
of m even if all blocks are admissible, they are not equiprobable. To check that this is not a ﬁnite size eﬀect, we have
reproduced the same computation on a symbolic sequence of the same size extracted from the fully chaotic logistic
map with p = 2 symbols -which is known to yield h(β) = log 2 when ﬁnite size eﬀects are absent-. The spectrum in
this case collapses to h(β) = log 2, ∀β as expected according to the topological conjugacy of the fully chaotic logistic
map with the binary shift, and no relevant ﬁnite size eﬀects are appreciated. Note that the Tchebytchev bias alone is
not able as well to explain this systematic decrease (a non-uniform null model of type I gives h(β) ≈ 0.693 ∀β). This
conﬁrms that in the case of the prime residues modulo k, we indeed have a nontrivial spectrum of Renyi entropies due
to the diﬀerent rates of appearance of every block of size m. For m = 1 this systematic non-uniformity is precluded
by virtue of the Dirichlet theorem, that assigns the same density for all admissible residue classes, so this is a higher
order pattern.
We use a proxy to h(β) ≈ H10(β)/10 and we plot this value as a function of β in ﬁgure. We deduce that metric does
indeed play a substantial role, at odds of what was perceived in the {AA, AB, BA, BB} symbolization. The reason
for the uneven appearance of each block will be elucidated in the next section, where we consider the gaps residues.

FIG. 9: Spectrum of Renyi entropies associated to the primes modulo 4.
 12

D. Results and interpretation for the gaps residue sequence

Here we focus on the sequence of prime gaps, with gap(n) = p(n + 1) − p(n). In some sense gaps are the derivative
of the primes. As it happens in complex chaotic systems such as turbulent ﬂuids, it is not position but velocity (the
derivative ﬁeld) the observable which shows a richer structure.
Gaps are always even numbers and as there exist arbitrarily large gaps, in order to make the gap sequence stationary
we consider this sequence modulo 6. Remember that the choice of the modulus is not arbitrary here, as the residue
classes classify gaps into three big families: 2 mod 6 (twin-like), 4 mod 6 (cousin-like) and 0 mod 6 (sexy-like).

1. Entropic analysis

In principle, a null model for this sequence should be of the type I, yielding for the uniform case h(β) ≈ log 3. For
the more realistic case where the empirical frequencies of the residue classes are considered, we have observed that
for the sequence of the ﬁrst 106 gaps,
 p(0) ≈ 0.43, p(2) ≈ p(4) ≈ 0.28. (6)

For these frequencies, we ﬁnd H1(1) ≈ 1.075. The null model predicts h(β) = H1(β), so the ﬁrst partial entropy
should be enough to extrapolate the asymptotic value. Using a Cramer null model we also ﬁnd the same result.
However, the actual spectrum is shown in ﬁgure 10, pointing out two unexpected features: (i) the convergence of
Renyi entropies to ﬁnite, positive values smaller than those predicted by the null models. This happens even for
β = 0, pointing out to the presence of forbidden patterns in this sequence: blocks of m symbols that appear in the
null models but are forbidden in the prime gaps. And (ii) there seems to be a non-trivial, monotonic dependence on
β which is not found in the null models. In what follows we discuss both results.

Explaining forbidden patterns. Some observed low order forbidden patterns are enumerated in table I. The ﬁrst
forbidden pattern is for a block of size m = 2 and consists in (4, 4). A forbidden pattern in the gaps residue sequence
such as (4, 4) actually relates to an inﬁnite set of forbidden patterns in the prime sequence. First, all gap pairs (f, f ′)
with f = 6n + 4, f ′ = 6n′ + 4, ∀n, n
′ are congruent to (4, 4), that is, consecutive gaps such as (4, 4), (4, 10), (4, 16),
(10, 4), etc are all forbidden. In the prime sequence, each of these forbidden gap pairs is associated with a forbidden
prime triple of the form (q, q + f, q + f ′), with q prime.

m F(m) |F(m)|

1 ∅ 0
2 {(4,4)} 1
3 {(0, 2, 2), (0, 4, 4), (2, 0, 2), (2, 2, 0), (2, 2, 2), (2, 4, 4), (4, 0, 4), (4, 2, 2), (4, 4, 0), (4, 4, 2), (4, 4, 4)} 11
4 {(0, 0, 2, 2), (0, 0, 4, 4), (0, 2, 0, 2), (0, 2, 2, 0), (0, 2, 2, 2), (0, 2, 2, 4), (0, 2, 4, 4), (0, 4, 0, 4), (0, 4, 2, 2), (0, 4, 4, 0), 49
(0, 4, 4, 2), (0, 4, 4, 4), (2, 0, 0, 2), (2, 0, 2, 0), (2, 0, 2, 2), (2, 0, 2, 4), (2, 0, 4, 4), (2, 2, 0, 0), (2, 2, 0, 2), (2, 2, 0, 4),
(2, 2, 2, 0), (2, 2, 2, 2), (2, 2, 2, 4), (2, 2, 4, 0), (2, 2, 4, 4), (2, 4, 0, 4), (2, 4, 2, 2), (2, 4, 4, 0), (2, 4, 4, 2), (2, 4, 4, 4),
(4, 0, 0, 4), (4, 0, 2, 2), (4, 0, 4, 0), (4, 0, 4, 2), (4, 0, 4, 4), (4, 2, 0, 2), (4, 2, 2, 0), (4, 2, 2, 2), (4, 2, 2, 4), (4, 2, 4, 4),
(4, 4, . . . , . . . )}

TABLE I: Set of forbidden blocks F(m) = {(s1 . . . sm), si ∈ {0, 2, 4}} of size m = 1, 2, 3, 4 in the sequence of gap residues
modulo 6.

From a dynamical systems viewpoint, these results suggest that the gap residue sequence manifests chaotic behavior
(as the amount of admissible blocks grows exponentially with m and thus the KS entropy is positive), but of weaker
intensity as h(0) < log p. According to Pesin identity [20], for symbolic dynamics with positive KS entropy, this
quantity is equal to the Lyapunov exponent of the underlying dynamical system, this latter quantity being responsible
for the exponentially fast separation of initially close trajectories. In a system with p symbols, information could be
erased at least as fast as log p per time step (in Information Theory both the topological and KS entropies are usually
deﬁned in base 2 rather than in base e, and in this setting information can be erased as fast as log2 2 = 1 bit per
iteration). In any case, for the gaps residue sequence modulo 6 we have p = 3, so the dynamics is chaotic albeit
information is lost at a slower pace as h(0) → log 2 < log 3.
 13

FIG. 10: (Left panel) Hm(β)/m associated to the primes gaps modulo 6. (Right panel) Spectrum of Renyi entropies associated
to the primes gaps modulo 6.

Why is this the case? Why is the dynamics underlying the prime gap residue sequence ’less chaotic’ than a shift of
ﬁnite type or a purely random process? In other words: what is the nature of these forbidden blocks? Consider for
instance the block (2, 2), which is not forbidden as it appears at least once in the prime progression 3, 5, 7. It is easy
to show that such progression is actually the only possibility. The proof consists in studying the divisibility properties
of q, q + 2 and q + 4. It turns out that in this progression there is always an element which is not prime because it is
a multiple of three. Assume for a contradiction that this is not the case, and consider the remainder of the integer
division q mod 3. If q is not a multiple of three, the remainder should either be 1 or 2. If the remainder is 1, then
q + 2 is a multiple of three. If the remainder is 2, then q + 4 is a multiple of three. The only case where there is no
contradiction is when q = 3 (a prime which is multiple of three), what ﬁnishes the proof.
Note that this proof also certiﬁes that no progression q mod 6, (q + 2) mod 6, (q + 4) mod 6 other than 3, 5, 7 is
possible, i.e. this holds not just for a twin triplet but for any twin-like triplet of the type q, q + 6n + 2, q + 6n′ + 4
where n′ ≥ n.
The origin of forbidden blocks can be thus directly linked to the divisibility properties of the integers. Actually,
it is well-known that a block of m consecutive gaps (2g1, . . . , 2gm), which gives rise to a prime block of the type
q, q + 2g1, q + 2g1 + 2g2, . . . , q + ∑m
i=1 2gi is forbidden if and only if one can ﬁnd a prime r for which each all and every
partial series ∑t≤m
i=1 gi is congruent to a diﬀerent residue from 1, 2, . . . , r − 1. For instance, in the case above of a gap
duple (2, 2) that generates a prime sequence of the form q, q + 2, q + 4, 2 ≡ 2 mod 3 and 4 ≡ 1 mod 3. For (4, 4)
again all residues for r = 3 are ticked, thus (4, 4) is forbidden. Using this principle one can therefore systematically
enumerate these forbidden patterns. For a generic m one ﬁnds

|A(m)| = 2
m+1; |F(m)| = 3
m − 2
m+1

from which we derive the partial entropies Hm(0) for the topological entropy

Hm(0)
m = 1
m log |A(m)| = (1 + 1
m
 ) log 2 (7)

for m ≥ 2 and H1(0) = log 3. This monotonic decay is in good agreement with the experiment (see the left panel of
ﬁgure 10). Interestingly, the number of admissible blocks of size m -which is here related to the divisibility properties of
the integers- precisely coincides with the number of admissible blocks in the type II null model, see eq. 5. Altogether,

h(0) = lim
m→∞ Hm(0)
m = log 2

Monotonic dependence on β and the distribution of blocks. In order to ﬁnd an analytical expression for
h(β > 0) which would allow us to elucidate whether the Renyi spectrum is indeed non-trivial or, on the contrary,
whether this is just a ﬁnite size eﬀect which while not present in the null models might be present for ﬁnite size
statistics of gaps residue sequences but vanish asymptotically. We would need to be able to ﬁnd an analytical
expression for the frequencies of each admissible block.
 14

Let us start by considering a Cramer null model. According to this model any large integer q has roughly a
probability 1/ log q of being a prime, then assuming probability independence the probability that an m-tuple of
integers is prime is simply 1/(log q)
m+1. However, obviously the Cramer model predicts the same probability for
every m-tuple, that is, in a Cramer random model every gap block of size m would be equiprobable and therefore
the frequency of each admissible block of size m is simply 1/|A(m)|. Under this situation it is easy to show that
Hm(β) = Hm(0) = log |A(m)|: a Cramer null model does not explain the dependence on β found in the gap residue
sequence.
Fortunately however, a well-known conjecture in number theory comes to save the day. First, let us deﬁne a prime
m-tuple as a sequence of consecutive primes of the form p, p + 2g1, p + 2g2, . . . , p + 2gm. Such a prime m-tuple is
trivially associated to a gap block (2g1, . . . , 2gm) (of course, in our case many diﬀerent gap blocks have the same
associated residue block). The diameter of a prime m-tuple is the diﬀerence of its largest and smallest element,
i.e. 2gm. For a ﬁxed m, the m-tuple with smallest diameter is called a prime constellation. For instance, for a
prime duple (p, p + 2g1) one can ﬁnd twin primes (g1 = 1), cousin primes (g1 = 2), sexy primes (g1 = 3) and so on,
all associated to a gap block (2g1). The smallest diameter is for g1 = 1 and therefore for m = 1 the only prime
constellation consist of twin primes. For gap blocks of size m = 2, the smaller diameter is 2g2 = 6, and there are two
possible constellations for that, associated with the gap blocks (2, 4) (≡ (2, 4) mod 6) and (4, 2) (≡ (4, 2) mod 6).
An example of the former is the prime triple (5, 7, 11) whereas for the latter the smallest constellation is (7, 11, 13).
It is clear that prime constellations generate only a subset of our gap residue blocks, but still an inﬁnite subset, and
more importantly, for a ﬁxed m there is in general more than one constellation. Now, the celebrated m-tuple conjec-
ture by Hardy and Littlewood [17] states that the frequencies of these prime constellations can be computed explicitly:

Prime m-tuple conjecture.
The amount of prime constellations [p, p + 2g1, . . . , p + 2gm] found for p ≤ x is given asymptotically by

πg1,g2,...,gm(x) ∼ C(g1, . . . , gm) ∫ x

2
 dt
(log t)m+1 ,

where
 C(g1, . . . , gm) = 2
m ∏

q>2
 1 − ω(q; g1, . . . , gm)/q
(1 − 1/q)m+1

are the so-called Hardy-Littlewood constants, the product runs over odd primes q > 2 and the function ω(q; g1, . . . , gm)
denotes the number of distinct residues in 0, g1, . . . , gm mod q.
Incidentally, note that for readability we have used the symbol m to be consistent with the previous exposition,
however this conjecture is usually stated as the k-tuple conjecture. Remarkably, these probabilities are proportional
to the Cramer model but, contrary to the Cramer model, do indeed depend on the particular block type via the
Hardy-Littlewood constants. This enables us to explore the uneven distribution of blocks via this conjecture:

For m = 1, we are considering pairs of primes. The prime constellation in this case, as we know, is for g1 = 1,
therefore the conjecture predicts that the amount of twin primes below x is

π2(x) ∼ C(1) ∫ x

2
 dt
(log t)2 ,

where
 C(1) = 2 ∏

q prime >2
 1 − 2/q
(1 − 1/q)2 ≈ 1.320324

The formula given by Hardy and Littlewood can actually be used to estimate the amount of any prime m-tuples, not
necessarily only those with smaller diameter. For instance, still for m = 1 we can work out the case for which g1 = 2
(cousin primes) and g1 = 3 (sexy primes), ﬁnding

C(2) = C(1), C(3) = 2C(2), C(g1) = C(1) · ∏

q|g1
 q − 1
q − 2 .

From this ﬁrst analysis it is straightforward that sexy pairs are, asymptotically, twice more frequent than twins and
cousins, what already suggests for m = 1 that we have a non-uniform distribution of blocks.
 15

The uneven distribution of blocks can be further assessed by enumerating for a given size m all the |A(m)| Hardy-
Littlewood constants {C(g1, . . . , gm)}. This is in principle possible but is a formidable exercise in practice. An
additional technical issue to have in mind is that here we deal with blocks of prime gap residues, so for a given m we
need to sum over all indices congruent with a given residue block. Let us consider again the case m = 1. The amount
of gaps congruent to 0 mod 6 (sexy primes) is given by taking into account gaps 6, 12, 18, etc so g1 = 3, 6, 9, etc.
Accordingly, this amount is associate to ∑∞
i=1 C(3i). Formally, if we deﬁne the normalization factor Z as:

Z =
 ∞∑

i=1 C(3i) +
 ∞∑

i=0 C(3i + 1) +
 ∞∑

i=0 C(3i + 2)

the densities of each gap residues is therefore:

p(0) = 1
Z
 ∞∑

i=1 C(3i), p(2) = 1
Z
 ∞∑

i=0 C(3i + 1), p(4) = 1
Z
 ∞∑

i=0 C(3i + 2)

Truncating these series at order i accounts for the gaps of size at most 2i. For instance, for third order (accounting
for gaps up to size 18) we have an approximation:

p(0) ≈ C(3) + C(6) + C(9)
∑9
i=1 C(i) ≈ 0.479, p(2) ≈ C(1) + C(4) + C(7)
∑9
i=1 C(i) ≈ 0.255, p(4) ≈ C(2) + C(5) + C(8)
∑9
i=1 C(i) ≈ 0.266,

which is still reasonable far away from the empirical frequencies (eq. 6) (at order four p(0) ≈ 0.471 so convergence is
slow). Still, this analytical approximation already certiﬁes that the three possible gap residue blocks of size m = 1
are not uniformly represented. Formally, one can express, assuming Hardy-Littlewood conjecture, the asymptotic
probability of an admissible gap residue block of size m (2g1, 2g2, . . . , 2gm) ∈ A(m), where gi ∈ {0, 1, 2} as

p(g1, g2, . . . , gm) = 1
Z
 ∑

i1
 ∑

i2 · · · ∑

im C(3i1 + g1, 3i2 + g2, . . . , 3im + gm) (8)

where the summation in ij runs between ij−1 and ∞ when gj = 1, 2 and gj−1 = 0 and between 1 + ij−1 and ∞
otherwise, and Z is the normalization factor. Eq. 8, together with eqs. 3 and 4 constitute the formal solution to the
problem.

Let us consider the case m = 2, for which there are 8 admissible blocks. To prove non-uniformity for m = 2 we
only need to ﬁnd that two diﬀerent blocks have diﬀerent frequencies: for convenience we will concentrate on the ﬁrst
two ones, namely (2g1, 2g2) = (0, 0) in mod 6 (which gathers all prime triples whose gaps are a multiple of 6) and
(2g1, 2g2) = (0, 2). Eq. 8 reduces in these cases to:

p(0, 0) = 1
Z
 ∞∑

i1=1
 ∞∑

i2=i1+1 C(3i1, 3i2) and p(0, 2) = 1
Z
 ∞∑

i1=1
 ∞∑

i2=i1 C(3i1, 3i2 + 1)

where

Z =
 ∞∑

i1=1
 ∞∑

i2=i1+1 C(3i1, 3i2) +
 ∞∑

i1=1
 ∞∑

i2=i1 C(3i1, 3i2 + 1) +
 ∞∑

i1=1
 ∞∑

i2=i1 C(3i1, 3i2 + 2) +
 ∞∑

i1=0
 ∞∑

i2=i1+1 C(3i1 + 1, 3i2)

+
 ∞∑

i1=0
 ∞∑

i2=i1+1 C(3i1 + 1, 3i2 + 1) +
 ∞∑

i1=0
 ∞∑

i2=i1+1 C(3i1 + 1, 3i2 + 2) +
 ∞∑

i1=0
 ∞∑

i2=i1+1 C(3i1 + 2, 3i2)

+
 ∞∑

i1=0
 ∞∑

i2=i1+1 C(3i1 + 2, 3i2 + 1)

is the normalization sum. At second order in ij,

p(0, 0) ≈ C(3, 6) + C(3, 9) + C(6, 9) + C(6, 12)
Z|2 ,
 16

and
 p(0, 2) ≈ C(3, 4) + C(3, 7) + C(6, 7) + C(6, 10)
Z|2 ,

where Z|2 is the normalization sum truncated at order two. At this point we can make use of Hardy-Littlewood’s
conjecture one more time. If we label
 a := ∏

q prime ≥5
 1 − 2/q
(1 − 1/q)3

and
 b := ∏

q prime ≥5
 1 − 3/q
(1 − 1/q)3 ,

then after a lengthy but trivial computation we get C(3, 6) = 9b, C(3, 9) = 9b, C(6, 9) = 9b, C(6, 12) = 9b hence

p(0, 0) ≈ 1
Z|2 36b

whereas C(3, 4) = 9b/2, C(3, 7) = 45b/8, C(6, 7) = 45b/8, C(6, 10) = 27b/4 thus

p(0, 2) ≈ 1
Z|2
 1
2 45b ̸= p(0, 0),

which is enough to conclude non-uniformity in the approximation of the frequencies of blocks of size m = 2. This is
a clear support to the apparence monotonic dependence on β of the Renyi entropies. A full proof would require to
perform the inﬁnite summations in each case, what appears to be a quite challenging endeavor and is left as an open
problem.
 2. IFS

The analysis performed a la IFS is shown in ﬁgure 11, where we also plot the result of a type I null model. We
ﬁnd that the prime gaps selects a subset of the attractor generated by the null model. This particular subset could
be put in correspondence with the subset of admissible sequences found above, and in some sense the IFS attractor
plays the geometric role of the distribution of forbidden patterns.

IV. DISCUSSION

The cross-disciplinary transfer of concepts and tools has always been a fruitful strategy for ﬁnding unexpected and
unorthodox ways of addressing problems, which has usually generated new knowledge. In this work we have tried to
illustrate this idea by making using the concepts, focus and techniques used traditionally in nonlinear dynamics and
complexity science to explore the structure of certain sequences appearing in number theory. We have considered
three types of sequences that emanate from the prime number sequence: the transition between Pythagorean and
Gaussian primes (transition sequence), the sequence of prime residues modulo k (with φ(k) = 2) and the sequence of
prime gap residues modulo 6 (inducing three symbols that can be associated with twin-like, cousin-like and sexy-like
pairs). All these sequences are stationary and it is easy to prove using Dirichlet’s theorem for arithmetic progressions
that each symbol appears inﬁnitely often, hence they are amenable to a symbolic dynamics analysis. We have thus
considered these symbol sequences as if they were generated by a hidden dynamical system whose trajectories were
symbolized via some unknown partition of the system’s phase space and have consequently explored some dynamical
properties of the system via a symbolic analysis of the sequences.

First, in every sequence we have found compelling evidence of chaotic behavior, as given by a positive KS entropy. In
the case of the transition sequence, we have found that the sequence has a lower entropy than expected from a purely
random process or a shift of ﬁnite type but we have shown that this decrease is due to the onset of spurious forbidden
patterns, not associated to the underlying dynamics but to the way of deﬁning transitions between primes. The IFS

17

FIG. 11: (Left panel) IFS chaos game-like attractor for the type I null model with p = 3 symbols. In this case the attractor
is the Sierpinski triangle. (Right panel) IFS chaos game-like attractor for the prime gap sequence and a symbolic sequence
extracted from other chaotic maps. The IFS associated to the prime gap sequence is a subset of the attractor. The similarity
with the tent map is again notable, where in this case the attractor of the tent map is a subset of the attractor of the prime
gap sequence. As a comparison, we have included a diﬀerent chaotic map (the Gauss map) which shows no similarities with
the gaps.

attractor generated following the transition sequence is a fractal that coincides with the equivalent attractor for the
tent map and for a properly deﬁned null model, concluding that this transition sequence has strong randomness
properties, as expected.

As for the residues of the primes modulo k, we have found that this sequence is maximally chaotic in the sense that
its topological entropy matches the analogous one found for the binary shift map. While lacking forbidden patterns
and at odds with the behavior of the binary shift map, we have found that this sequence displays a non-trivial
spectrum of Renyi entropies which unexpectedly suggest that every symbol block of size m > 1, while admissible,
occurs with diﬀerent probability. This non-uniform distribution of blocks for m > 1 contrasts Dirichlet’s theorem
that guarantees equiprobability for m = 1.

Finally, we have explored in a similar fashion the sequence of prime gap residues. This sequence is again chaotic
(positivity of Kolmogorov-Sinai entropy), however chaos is weaker in this case as we have found non-spurious forbidden
patterns for every block of size m > 1 that yield entropies lower than those for a null model or a shift of ﬁnite type
with the same number of symbols. We were able to relate the onset of these forbidden patterns with the divisibility
properties of integers. Interestingly, the amount of admissible blocks is precisely the same, for a given block size,
than both the type II null model and the fully chaotic logistic map with p = 4 symbols. This suggests that a
systematic enumeration of admissible sequences in the gap sequence could be ﬁgured out without resorting to any
number-theoretic properties, something that is left as an open problem. We have also given a geometric visualization
of this phenomenon by showing that the IFS attractor associated to this sequence is only a subset of the Sierpinski
triangle, which is the attractor for a three-vertex Chaos Game.
Moreover, we have found again that this sequence displays a monotonically decreasing spectrum of Renyi entropies,
which suggests that gap block residues of size m > 1 are not equiprobable. A Cramer random model cannot explain this
apparent dependence on β as for that model, given m each block of size m is by construction equiprobable. However,
the frequencies of these blocks can be computed explicitly assuming Hardy-Littlewood’s k-tuple conjecture. We have
built on this relation to give analytical arguments and approximations that support the monotonic dependence of
the Renyi entropies on β, however an exact and closed form expression for these entropies has remained elusive and
constitutes an interesting open problem.

[1] M. Schroeder, Number Theory in Science and Communication, 5th ed. (Springer Verlag, Berlin Heidelberg 2009).
[2] http://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/physics.htm
 18

[3] F.J. Dyson, A Brownian Motion Model for the Eigenvalues of a Random Matrix J. Math. Phys. 3, 1191 (1962).
[4] H.L. Montgomery, The pair correlation of zeros of the zeta function, Analytic number theory, Proc. Sympos. Pure Math.,
XXIV, Providence, R.I.: American Mathematical Society, pp. 181-193 (1973).
[5] A.M. Odlyzko, On the distribution of spacings between zeros of the zeta function, Mathematics of Computation, American
Mathematical Society 48(177): 273-308 (1999).
[6] B.L. Julia, Statistical theory of Numbers, Number Theory and Physics. (Springer Verlag, Berlin 1990).
[7] M.V. Berry and J.P. Keating, Siam Rev 41, 2 (1999).
[8] M. Wolf, Physica A 160, 236 (1989).
[9] S. Mertens, Phys. Rev. Lett. 81, 4281 (1998).
[10] B. Luque, L. Lacasa and O. Miramontes, Phase transition in a stochastic prime number generator, Phys. Rev. E 76,
010103R (2007).
[11] B. Luque, O. Miramontes and L. Lacasa, Number theoretic example of scale-free topology inducing self-organized criticality,
Phys. Rev. Lett 101, 158702 (2008).
[12] L. Lacasa and B. Luque, Phase transition in the Countdown problem Lucas Lacasa, Bartolo Luque Phys. Rev. E 86,
010105R (2012)
[13] B. Luque, I.G. Torre and L. Lacasa, Phase transitions in Number Theory: from the Birthday Problem to Sidon Sets, Phys.
Rev. E 88, 052119 (2013)
[14] Guillermo Garcia-Perez, M. Angeles Serrano, and Marian Boguna, Complex architecture of primes and natural numbers,
Phys. Rev. E 90 022806 (2014).
[15] ML Stein, S Ulam, MB Wells, A Visual Display of Some Properties of the Distribution of Primes, American Mathematical
Monthly 71 (1964) 516-520.
[16] Bai-Lin Hao and Wei-Mou Zheng, Applied Symbolic Dynamics and Chaos. (World Scientiﬁc Pub Co Inc, 1998).
[17] GH Hardy and JE Littlewood, Some Problems of ’Partitio Numerorum.’ III. On the Expression of a Number as a Sum of
Primes, Acta Math. 44 (1923), pp. 1-70.
[18] S Ares and M Castro, 2006. Hidden structure in the randomness of the prime number sequence?. Physica A: Statistical
Mechanics and its Applications, 360(2), pp.285-296.
[19] J. Jost, Dynamical Systems: Examples of Complex Behavior (Springer-Verlag, Berlin 2005)
[20] C Beck and F Schlogl, Thermodynamics of chaotic systems (Cambridge University Press 1993).
[21] M Barnsley, Fractals everywhere (1988). Academic Press, USA.
[22] HO Peitgen, H Jurgens. and D Saupe, 1992. The Chaos Game: How Randomness Creates Deterministic Shapes. In Chaos
and Fractals (pp. 297-352). Springer New York.
[23] HJ Jeﬀrey. Chaos game visualization of sequences. Computers & Graphics. 1992 Jan 1;16(1):25-33.
[24] H Cram´er, 1936. On the order of magnitude of the diﬀerence between consecutive prime numbers. Acta Arithmetica, 2:
23-9646.
