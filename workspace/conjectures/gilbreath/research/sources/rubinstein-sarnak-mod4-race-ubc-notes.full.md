<!-- source: https://personal.math.ubc.ca/~gerg/teaching/613-Winter2023/BDPM4.pdf | converted from PDF -->

BIAS IN THE DISTRIBUTION OF PRIMES MODULO 4

SHUBHRAJIT BHATTACHARYA AND ZHENGHENG BAO

ABSTRACT. In this brief note, we discuss the bias in the distribution of primes modulo 4. First
observed by Chebyshev in 1853, this phenomenon attracted many mathematicians. Rubinstein and
Sarnak first proved [RS94] unconditional results where they attached numerical values to such biases
in general for any modulus q. This article is an overview of the case where we determine that there
are typically more primes 3 (mod 4) than 1 (mod 4). It also discusses why we need to assume the
Generalized Riemann Hypothesis.
 1. INTRODUCTION

The distribution of primes is one of the most mysterious fields of study for number theorists.
Throughout the century, many mathematicians have attempted to study different aspects of it.
Dirichlet [DdS37] proved that for any positive integer q > 1 and (q, a) = 1, there are infin-
itely many primes p ≡ a (mod q). This indicates roughly an equidistribution of primes in every
congruence class modulo any positive integer q > 1. This became mathematically more precise
when Hadamard and de la Vall´ee Poussin proved, in 1890s, the asymptotic formula

π(x; q, a) ∼ 1
φ(q)π(x) ∼ 1
φ(q) x
log x (1.1)

where π(x) and π(x; q, a) denote the number of primes ≤ x and number of primes p ≤ x with
p ≡ a (mod q) for q > 1 and (a, q) = 1 respectively. Since the number of residue classes a
(mod q) with (a, q) = 1 is given by the Euler totient function φ(q), equation (1.1) tells us that for
large x, primes are uniformly distributed across the reduced residue classes modulo any integer
q > 1.
In 1853, Chebyshev noticed that there are more primes in the congruence class 3 (mod 4) than
in 1 (mod 4). The table on the next page (data taken from [GM04, page 1]) presents a com-
parison between the quantities π(x; 4, 1) and π(x; 4, 3) for some x ≤ 50, 000. This table may
lure us to conjecture that π(x; 4, 3) > π(x; 4, 1) for all x ≥ 1; however, Leech [Lee57] found that
π(x; 4, 3) < π(x; 4, 1) for x = 26861 and this is the first such x! Nevertheless, the large size of this
first counter-example still indicates the bias of primes towards the congruence class 3 (mod 4).
But how do we mathematically establish the statement there are more primes p ≡ 3 (mod 4)
than primes p ≡ 1 (mod 4)? According to the Prime Number Theorem of Hadamard/de la Vall´ee
Poussin,
 lim
x→∞ π(x; 4, 3)
π(x; 4, 1) = 1 (1.2)

that says there are asymptotically an equal number of primes in both residue classes as x → ∞.
Therefore, we have to devise stronger measurement techniques. Rubinstein & Sarnak [RS94]
consider the sets Pq;a,b = {x ≥ 2 : π(x; q, a) > π(x; q, b)} for two reduced residue classes a, b
modulo q. With an appropriate notion of size, they prove that P4;3,1 is larger than P4;1,3. In [RS94],

they computed the logarithmic density, which will be defined in the following section, of such sets
and found that the logarithmic density of P4;3,1 equals 0.9959 . . ., which clearly indicates the bias
in the distribution of prime modulo 4!

x Number of primes
4n + 3 up to x Number of primes
4n + 1 up to x
100 13 11
200 24 21
300 32 29
400 40 37
500 50 44
600 57 51
700 65 59
800 71 67
900 79 74
1000 87 80
2000 155 147
3000 218 211
4000 280 269
5000 339 329
6000 399 383
7000 457 442
8000 507 499
9000 562 554
10,000 619 609
20,000 1136 1125
50,000 2583 2549

Table 1. The number of primes of the form 4n + 1 and 4n + 3 up to x.

However, results in [RS94] are under the assumption of the Generalized Riemann Hypothesis
(GRH) and the Linear Independence hypothesis (LI), which will be defined later. The uncondi-
tional results known so far was proved, before Rubinstein & Sarnak’s results, by Littlewood [Lit14]
that both sets P4;3,1 and P4;1,3 are unbounded.
Even if there are huge biases for small q, they disappear as q → ∞. Rubinstein & Sarnak [RS94]
prove that limq→∞ max(a,q)=(b,q)=1 |δ(Pq;a,b) − 1/2| = 0. In this note, we confine ourselves to the
modulo 4 race, first studied by Chebyshev, that gave birth to this fascinating subject in number
theory, now known as The Chebyshev Bias / The Prime Number Race!

2. PRELIMINARIES

A Dirichlet character modulo q is a group homomorphism χ : (Z/qZ)
× −→ C×, which is ex-
tended to χ : Z → C
× by assigning χ(n) = 0 for (n, q) > 1. To any such Dirichlet character χ,
one attaches an L-function, known as the Dirichlet L-function,

L(s, χ) =
 ∞∑

n=1
 χ(n)
ns , (2.1)

2

which is absolutely convergent for ℜ(s) > 1. It can be shown that it has an analytic continuation
to C, with at most one pole at s = 1. These L-functions are the most important objects while
counting primes in a specific congruence class modulo an integer q > 1. For the trivial character
χ0 modulo 1, we get the famous Riemann zeta function L(χ0, s) = ζ(s). The Riemann Zeta ζ(s)
has some trivial zeros: ζ(−2) = ζ(−4) = ζ(−6) = · · · = 0. Other zeros lie in the critical strip
0 < ℜ(s) < 1, and contribute to the counting of primes. After playing around with his creations,
Riemann conjectured that the nontrivial zeros of ζ all lie on the line ℜ(s) = 1/2. This is known as
the Riemann Hypothesis, and is still wide open! After studying these L-functions, mathematicians
expect this to happen for all Dirichlet L-functions.

Conjecture 2.1 (The Generalized Riemann Hypothesis (GRH)). Let L(s, χ) be a Dirichlet L-
function. If σ + it is a complex number with σ ∈ (0, 1] and L(σ + it, χ) = 0, then σ = 1/2.

The key step in Rubinstein & Sarnak’s paper is to consider the logarithmic density (definition
(2.2)), which will be used to measure the sets P4;3,1. Wintner [Win41] did some investigations with
the remainder term in the prime number theory and from his work, it is evident that logarithmic
density is a good way to measure Pq;a,b in general, which is done in [RS94].

Definition 2.2 ([RS94]). Let P be a set of real numbers. Define the upper and lower logarithmic
densities δ(P ) and δ(P ) respectively as

δ(P ) = lim sup
X→∞ 1
log X
 ˆ

t∈P ∩[2,X]
 dt
t , δ(P ) = lim inf
X→∞ 1
log X
 ˆ

t∈P ∩[2,X]
 dt
t (2.2)

and the logarithmic density of P exists and equals δ(P ) = δ(P ) = δ(P ) if the latter two are equal.

Rubinstein & Sarnak’s work was stimulated by Davidoff’s 1994 paper [Dav94] which consid-
ered the race between quadratic residue and nonresidue primes modulo q. An integer a is said to be
a quadratic residue if x2 ≡ a (mod q) has a solution, and a nonresidue otherwise. Both Davidoff
and Rubinstein & Sarnak considered the case when q = pα, 2pα, 4 for some odd prime p. This is
because of the existence of primitive roots of unity modulo these integers. In this note, we also
assume that q ∈ {pα, 2pα, 4} for odd primes p.
Following [RS94], define πR(x; q) to be the number of primes p ≤ x such that p is a quadratic
residue modulo q. Similarly, πN (x; q) will denote the number of primes p ≤ x which are quadratic
nonresidues modulo q. Also, define

Pq;N,R = {x ≥ 2 : πN (x; q) > πR(x; q)}, Pq;R,N = {x ≥ 2 : πR(x; q) > πN (x; q)}

According to the computations in Rubinstein & Sarnak [RS94], we see that there is always a
bias toward nonresidues. For q = 4, the integer 3 is the only quadratic nonresidue and 1 is the only
quadratic residue. Therefore, P4;N,R = P4;3,1 and we will see that δ(P4;3,1) = 0.9959..., which
numerically establishes Chebyshev’s observations.
Here we take a moment to introduce the arithmetic functions we will need for the rest of this
note. 3

Definition 2.3. We define

Λ(n) =
 {
log p n = pa

0 otherwise ψ(x, χ) = ∑

n≤x χ(n)Λ(n) (2.3)

ψ(x; q, a) = ∑

n≤x
n≡a (mod q)
 Λ(n) θ(x; q, a) = ∑

p≤x
p≡a (mod q)
 log p (2.4)

Here, Λ(n) is known as Von Manglodt’s function, and θ and ψ are variants of Chebyshev’s θ and
ψ functions.

In order to compute the logarithmic densities of Pq;N,R (respectively Pq;R,N ), [RS94] proved
the existence of limiting logarithmic distributions of the normalized functions Eq;N,R (respectively
Eq;R,N ) defined by
 Eq;N,R(x) = log x
√x (πN (x, q) − πR(x, q)) . (2.5)

By a limiting logarithmic distribution, we mean a measure µq;N,R such that

lim
X→∞ 1
log X
 ˆ X

2 f (Eq;N,R(x))dx
x = ˆ

R f (x)dµq;N,R(x) (2.6)

for any bounded continuous function f on R. Note that if f is absolutely continuous then δ(Pq;N,R) =
µq;N,R({x ∈ R : x > 0}). But even GRH does not guarantee the existence of the densities
δ(Pq;N,R). The proof of [RS94, Theorem 1.1] may not be true for characteristic functions of
nice sets like {x ∈ R : x > 0}. Instead, they constructed similar measures, defined in terms
of the nontrivial zeros of the Dirichlet L-functions L(s, χ), that estimate the measures µq;N,R. One
more assumption is made about the nontrivial zeros of Dirichlet L-functions, known as the Linear
Independence(LI) hypothesis/Grand Simplicity Hypothesis (GSH) [Dav13].

Conjecture 2.4. The set γ ≥ 0 such that L(1/2 + iγ, χ) = 0, as χ runs through the set of primitive
Dirichlet characters, is linearly independent over Q.

Two of the immediate consequences of LI are that 0 can’t be the imaginary part of a nontrivial
zero (in other words, L(1/2, χ) ̸= 0) and that all the zeros are simple. GRH and LI together give
the following explicit formula for the Fourier transform of µq;N,R ((3.4) in [RS94]):

ˆµq;R,N (ξ) = eiξ ∏

γχ1>0 J0
 

 2ξ
√
1/4 + γ2
χ1
 

 (2.7)

where χ1 is the real nontrivial character modulo q and J0 is the Bessel function defined as

J0(z) =
 ∞∑

m=0
 (−1)
m( 1
2z)
2m

(m!)2 . (2.8)

4

Observe that χ1(a) = 1 (respectively −1) when a is a quadratic residue (respectively nonresidue)
modulo q. Therefore,

log x
√
x
 ∑

p≤x χ1(p) = log x
√x (πR(x; q) − πN (x; q)) = −Eq;N,R(x). (2.9)

Under GRH and LI, the limiting distribution ˜µq;N,R of the normalized function Eq;N,R/
√
log q
converges in measure to the Gaussian (2π)
−1/2e−x2/2 dx as q → ∞ [RS94, Theorem 1.6]
Before sketching the method of computing the densities δ(Pq;N,R), we briefly describe the role
of GRH in Rubinstein & Sarnak’s work [RS94].

3. CONTRIBUTIONS OF THE GENERALIZED RIEMANN HYPOTHESIS

As we know, the Generalized Riemann Hypothesis proved to be shockingly important in number
theory and many other branches of mathematics. Assuming GRH, mathematicians have proved
many interesting results. Although the Generalized Riemann Hypothesis is widely believed to be
true, no proof is known to us yet, even for the Riemann Hypothesis, which is a special case of the
Generalized Riemann Hypothesis.

Right now, when we tackle problems without knowing the truth of the Riemann
hypothesis, it’s as if we have a screwdriver. But when we have it, it’ll be more like a
bulldozer. [Kla00] Peter Sarnak

The main tool for establishing the existence of the densities µq;N,R, as done in [RS94], is the
explicit formula for the prime counting function π(x), sometimes called Riemann’s Revolutionary
Formula ([GM04]), that states

´ x
2 dt
log t − π(x)
√
x/ log x ≈ 1 + 2 ×
 



 ∑

γ>0
ζ(1/2+iγ)=0
 sin(γ log x)
γ
 



 (3.1)

As an analog of this for π(x; q, a), [RS94] considered ψ(x, χ) for a Dirichlet character χ modulo
q, as defined in the previous section. As is shown in [Dav13, pp. 115–120], if χ ̸= χ0, x ≥ 2 and
X ≥ 1 we have
 ψ(x, χ) = − ∑

|γχ|≤X
 xρ

ρ + O ( x log2(xX)
X + log x) , (3.2)

where ρ = βχ + iγχ runs over the zeros of L(s, χ) in 0 < Re(s) < 1, and the implied O-constant
depends on q. Therefore, under GRH, we have βχ = 1
2 and equation (3.2) becomes

ψ(x, χ) = −
√x ∑

|γχ|≤X
 xiγχ

1
2 + iγχ + O ( x log2(xX)
X + log x) . (3.3)

Define 5

E(x; q, a) = (φ(q)π(x; q, a) − π(x)) log x/
√x (3.4)

c(q, a) = −1 + ∑

b2≡a (mod q)
1≤b≤q−1
 1. (3.5)

Then [RS94] proves the following formula:

E(x, q, a) = −c(q, a) + ∑

χ̸=χ0 ¯χ(a)ψ(x, χ)
√
x + O ( 1
log x
) . (3.6)

When q ∈ {pα, 2pα, 4} for odd primes p (in other words, there are primitive roots modulo q) and
a is a quadratic residue then c(q, a) = 1, and c(q, a) = −1 when a is a quadratic nonresidue
modulo q. This shows that the constant term −c(q, a) in equation (3.6) is responsible for the bias
toward nonresidues. For the case q = 4, note that πN (x; 4) = π(x; 4, 3) and πR(x; 4) = π(x; 4, 1)
since 1 and 3 are the only quadratic residue and nonresidue modulo 4 respectively. Therefore,
E(x; 4, 3) − E(x; 4, 1) = 2E4;3,1(x).
We have skipped most of the technical details/proof in this note but we would like to sketch a
proof of expression (3.6) since this formula along with GRH indicates the reason behind the bias.
As defined in equation (2.4), we may write π(x; q, a) as the Riemann-Stieltjes integral

π(x, q, a) = ˆ x

2
 dθ(t, q, a)
log t ; (3.7)

from the prime theorem in arithmetic progressions,

ψ(x, q, a) = θ(x, q, a) +
 

 ∑

b2≡a(q) 1



 √x
φ(q) + O ( √
x
log x
 ) . (3.8)

Solving for θ(x, q, a) and combining with the fact that

ψ(x, q, a) = 1
φ(q)
 ∑

χ mod q ¯χ(a) ∑

n≤x Λ(n)χ(n) = 1
φ(q)
 ∑

χ mod q ¯χ(a)ψ(x, χ), (3.9)

we get 6

ˆ x

2
 dθ(t, q, a)
log t = 1
φ(q)
 ˆ x

2
 dψ(t)
log t + 1
φ(q)
 ∑

χ̸=χ0 ¯χ(a) ˆ x

2
 dψ(t, χ)
log t − 1
φ(q)
 

 ∑

b2≡a(q) 1



 √x
log x

+ O ( √
x
log2 x
 )

= 1
φ(q)
 (π(x) + √x
log x
) + 1
φ(q)
 ∑

χ̸=χ0 ¯χ(a)ψ(x, χ)
log x − 1
φ(q)
 

 ∑

b2≡a(q) 1



 √
x
log x

+ O
 ( ∑

χ̸=χ0
 ∣
∣
∣
∣
ˆ x

2
 ψ(t, χ)
t log2 t dt
∣
∣
∣
∣ + √
x
log2 x
 )

= π(x)
φ(q) + 1
φ(q)
 ∑

χ̸=χ0 ¯χ(a)ψ(x, χ)
log x − c(q, a)
φ(q)
 √
x
log x

+ O
 ( ∑

χ̸=χ0
 ∣
∣
∣
∣
ˆ x

2
 ψ(t, χ)
t log2 t dt
∣
∣
∣
∣ + √
x
log2 x
 )
 . (3.10)

As shown in the proof of in [RS94, Lemma 2.1], the error term in equation (3.10) becomes
O(√
x/ log2 x) and hence it gives us the following

π(x, q, a) − π(x)
φ(q) = −c(q, a)
φ(q)
 √x
log x + 1
φ(q) log x
 ∑

χ̸=χ0 ¯χ(a)ψ(x, χ) + O ( √
x
log2 x
 ) . (3.11)

Combining equation (3.6) with equation (3.3) we get, for T ≥ 1 and 2 ≤ x ≤ X,

E(x, q, a) = −c(q, a) − ∑

χ̸=χ0 ¯χ(a) ∑

|γχ|≤T
 xiγχ

1
2 + iγχ + εa(x, T, X). (3.12)

After estimating the term εa(x, T, x), the existence of the limiting distributions is established. From
this discussion, we get a sense of how [RS94] uses GRH in a crucial way. As we mentioned earlier,
LI is equally important but we skip that discussion here. One may consult Rubinstein & Sarnak’s
original paper [RS94, Section 3] for details.

4. COMPUTING δ(P4;3,1)

In [RS94, Section 4] the following densities are computed. They show that the accuracy is at
least 20 decimal digits, though we are only showing the first 4 digits.

δ (P3;N ;R) = 0.9990 . . .

δ (P4;N ;R) = 0.9959 . . .

δ (P5;N ;R) = 0.9954 . . .

δ (P7;N ;R) = 0.9782 . . .

δ (P11;N ;R) = 0.9167 . . .

δ (P13;N ;R) = 0.9443 . . .
7

Table 2. Densities of Pq;N,R for q = 3, 4, 5, 7, 11, 13

We follow [RS94] to give an overview of the computations.
Recall that
 ˆµq;R,N (ξ) = eiξ ∏

γχ1>0 J0
 

 2ξ
√
1/4 + γ2
χ1
 

 (4.1)

where χ1 is the real nontrivial character modulo q and J0 is the Bessel function defined in equation
(2.8). Let fq;N,R(t) denote the density function of µq;R,N and g(t) = fq;N,R(t − 1). Since J0 is
an even function, so is the above product for ˆµ. So µq;R,N is symmetric about t = −1. So g is
symmetric about t = 0 (which is easier than f to work), and its Fourier transform, which we denote
by ˆω, is
 ˆω(ξ) = ∏

γ>0 J0
 ( 2ξ
√
1/4 + γ2
 )
 . (4.2)

Notice that δ(Pq;N,R) = ´ 1
−∞ dωq;R,N (t). By symmetry of gq;R,N about t = 0, we know that

δ(Pq;N,R) = 1
2
 (ˆ 1

−∞ + ˆ ∞

1
 ) dωq;R,N (t) (4.3)

= 1
2 + 1
2
 ˆ 1

−1 dωq;R,N (t) (4.4)

= 1
2 + 1
2π
 ˆ ∞

−∞
 sin u
u ˆωq;R,N (u)du (4.5)

Here, the middle equality is because the integral from −∞ to ∞ of the ωq;R,N , which is a proba-
bility measure, is 1; and the last equality is by the Fourier inversion formula of the characteristic
function χ[−1,1]. Now we have expressed δ(Pq;N,R) in terms of ˆωq;R,N , and we have the formula
(4.2) for ˆωq;R,N . The integral (4.3) is estimated in [RS94] in three steps. We only sketch the first
step here, which is to replace the integral with a sum, according to [RS94, p. 189].
The way to replace the integral with a sum is to use the Poisson summation formula. The Poisson
formula tells us that
 ε ∑

n∈Z ϕ(εn) = ∑

n∈Z ˆϕ (n
ε
 ) = ˆϕ(0) + ∑

n∈Z,n̸=0 ˆϕ (n
ε
 ) (4.6)

for any continuous and rapidly decreasing function ϕ. We apply this formula to

ϕ(u) = 1
2π sin u
u ˆω(u),

obtaining
 ˆϕ(x) = 1
2
 ˆ x+1

x−1 g(u)du = 1
2
 ˆ x+1

x−1 dω(u). (4.7)

8

The fact that ϕ satisfies the conditions for applying the Poisson summation formula follows from
[Wat48] and [SW71]. We skip the details here. Hence

1
2π
 ˆ ∞

−∞
 sin u
u ˆω(u)du = ˆϕ(0)

= ε ∑

n∈Z ϕ(εn) − ∑

n∈Z,n̸=0 ˆϕ (n
ε
 )

= 1
2π
 ∑

n∈Z εsin εn
εn ˆω(εn) − ∑

n∈Z,n̸=0 ˆϕ (n
ε
 ) . (4.8)

Define Rγ = 2√1/4+γ2 . Now we go to our special case q = 4 for this paper. By calculations with

computer, we know that when q = 4, all positive γ’s are greater than 2. Then γ > 2 implies that
Rγ < 1, so for any λ ≥ 0, there is an X such that

0 ≤ λ − 2 ∑

0<γ≤X Rγ < 2.

[Mon80] shows that
 ω
 [
2 ∑

0<γ≤X Rγ, ∞
)
 ≤ exp
 


−3
4
 (∑

0<γ≤X Rγ)2

∑
γ>X R2
γ
 


 .

Combining these two formulas, we get

ω[λ, ∞) ≤ exp
 (

−3
4 (1/2(λ − 2))
2
∑
γ>0 R2
γ
)
 .

Note that ∑

γ>0 R2
γ can be computed in terms of L(1, χ1) and L′(1, χ1). When q = 3, we have
(∑

γ>0 R2
γ)−1 > 0.98 by some computer calculations, see for example, [RS94, Table 2 on p.

193]. So ω[λ, ∞) ≤ exp(−1/6(λ − 2)2) by some computation. Hence for n ≥ 1 with n
ε − 1 ≥ 2,
equation (4.7) gives

ˆϕ ( n
ε
 ) = 1
2
 ˆ n
ε +1

n
ε −1 g(u)du ≤ 1
2 ω [ n
ε − 1, ∞) ≤ 1
2 exp (
−1
6
 ( n
ε − 3
)2) .

By choosing ε = 1/20, we get ∑

n∈Z,n̸=0 ˆϕ (n
ε
 ) < 10
−20.617....

This gives
 δ(Pq;N,R) = 1
2 + 1
2π
 ∑

n∈Z ε sin εn
εn ˆωq;R,N (εn) + error

where ε = 1/20 and |error| < 10
−20. This is an infinite sum. Further investigations are made in
[RS94] to truncate it to a finite sum −C < nε < C, where Rubinstein and Sarnak showed that C
can be taken to be 25 for the case q = 4 so that the error term becomes negligible. The modified
formula with a finite sum for δ(P4;3,1) [RS94, p. 192] gives us δ(P4;3,1) = 0.9959....
9

REFERENCES

[Dav94] G Davido. Some experimental results on a generalization of littlewood’s theorem. preprint, Mount Holyoke
College, 1994.
[Dav13] Harold Davenport. Multiplicative number theory, volume 74. Springer Science & Business Media, 2013.
[DdS37] L Dirichlet and Beweis des Satzes. da jede unbegrenzte arithmetische progression::: unendlich viele
primzahlen enth alt”, abh. k onig. Preuss. Akad, 34:45–81, 1837.
[GM04] Andrew Granville and Greg Martin. Prime number races, 2004.
[Kla00] Erica Klarreich. Prime time: Will we ever solve the riemann hypothesis?, Nov 2000.
[Lee57] John Leech. Note on the distribution of prime numbers. Journal of The London Mathematical Society-second
Series, pages 56–58, 1957.
[Lit14] J. E. Littlewood. Distribution des nombres premiers, 1914.
[Mon80] H. L. Montgomery. The zeta function and prime numbers. Proceedings of the Queen’s Number Theory
Conference, pages 13–24, 1980.
[RS94] Michael Rubinstein and Peter Sarnak. Chebyshev’s bias. Experimental Mathematics, 3(3):173 – 197, 1994.
[SW71] E. Stein and G. Weiss. Introduction to Fourier Analysis on Euclidean Spaces. Princeton University Press,
1971.
[Wat48] G. N. Watson. A Treatise on the Theory of Bessel Functions, volume (2nd ed.). Cambridge University Press,
1948.
[Win41] Aurel Wintner. On the distribution function of the remainder term of the prime number theorem. American
Journal of Mathematics, 63(2):233–248, 1941.
 10
