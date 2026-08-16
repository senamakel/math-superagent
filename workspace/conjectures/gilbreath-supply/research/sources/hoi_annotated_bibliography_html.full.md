<!-- source: https://arxiv.org/html/2309.08729v3 | converted from HTML -->

An annotated bibliography for comparative prime number theory

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-NC-ND 4.0][2]

arXiv:2309.08729v3 [math.NT] 11 Dec 2024

\assignrefcontextentries

*[sorting=ynt]*

# An annotated bibliography for
comparative prime number theory

Greg Martin, Pu Justin Scarfy Yang, Aram Bahrini, Prajeet Bajpai,
Kübra Benli, Jenna Downey, Yuan Yuan Li, Xiaoxuan Liang,
Amir Parvardi, Reginald Simpson, Ethan Patrick White, and Chi Hoi Yip Address: University of British Columbia
Department of Mathematics
Room 121
1984 Mathematics Road
Vancouver, BC Canada V6T 1Z2 Email address: [gerg@math.ubc.ca][3]

###### Abstract.

The goal of this annotated bibliography is to record every publication on the topic of comparative prime number theory together with a summary of its results. We use a unified system of notation for the quantities being studied and for the hypotheses under which results are obtained.

###### 2010 Mathematics Subject Classification

11N13 (11Y35)

## 1. Introduction

Comparative prime number theory is the study of number-theoretic quantities, such as functions that count primes with particular properties, and how they compare to one another. It certainly includes (but is not limited to) “prime number races”, which examine inequalities between the counting functions of primes in arithmetic progressions to the same modulus; indeed, Chebyshev observing the apparent preponderance of primes of the form 4 ​ k + 3 4k+3 over those of the form 4 ​ k + 1 4k+1 was the historical beginning of comparative prime number theory. Studying inequalities between two functions can be rephrased as studying the sign of their difference, and so the methods of comparative prime number theory also extend to studying the sign (and changes of sign) of other number-theoretic quantities that are less directly related to prime-counting functions.

The phrase “comparative prime number theory” goes back at least as far as the title of a long sequence of papers of Knapowski and Turán, beginning with [1172]. That paper begins with a list of several questions that can be interpreted as an attempt to define the scope of the field, as does the first paper [1185] in a sequel series by the same authors. Other surveys of these topics include papers by Kaczorowski [1322] and by Ford and Konyagin [1333], as well as an expository introduction to the field by Granville and the first author [1351].

This being said, there is no ironclad definition of what is and is not comparative prime number theory. Most quantities in this field have “explicit formulas” that express them as sums of oscillatory functions indexed by the zeros of L L -functions of some type (including the Riemann zeta-function). As such, suitably normalized versions of these quantities are expected to have limiting (logarithmic) distribution functions, which are measures that record the frequencies with which the normalized quantities take values in various intervals in the limit (“continuous histograms” of their values). In our view, the existence of such a limiting distribution is one of the main criteria for deciding whether a topic does or does not belong to the field of comparative prime number theory.

The purpose of this annotated bibliography is to provide a single exhaustive resource that lists every publication in the field of comparative prime number theory, and provides a summary of the results of each publication included. Like any human endeavour, the fulfillment of that goal will be imperfect. More specifically, we have aimed for completeness for all publications through 2023, as well as an incomplete list of sources from 2024.

The publications in comparative prime number theory over the 170 years of its existence have understandably used a wide variety of notations for the same objects. Another purpose of this work is to propose a unified system of notation for referring to the functions and quantities that are the main objects of study in comparative prime number theory, as well as uniform terminology for the assumptions on zeros of L L -functions that arise repeatedly when trying to prove theorems about these quantities. In particular, in our summaries of each publication, we have translated the results into this modern unified notation whenever possible, rather than preserving the notation used by the authors. In this respect, this work is more of a scientific resource than a historical document, although of course we hope it has some utility in the latter role (and we have included authors’ exact words on a few occasions, particularly when problems or conjectures were first proposed).

Section 2 is therefore a long section presenting this system of notation for elementary functions, prime counting functions and other summatory functions of number-theoretic quantities, their error terms (both normalized and unnormalized), weighted and averaged versions of these quantities, analogues of these quantities over number fields and function fields, functions that count the number of sign changes of these quantities, and (natural and logarithmic) limiting densities and limiting distribution functions. Section 3, beginning on page 3, describes objects and theorems that frequently arise in this field, such as Dirichlet characters and L L -functions, Landau’s theorem, explicit formulas, the power-sum method, k k -functions, and various hypotheses on the zeros of L L -functions. Section 4, beginning on page 4, enumerates the types of questions that comparative number theory studies about the quantities from Section 2. The annotated bibliography proper begins on page Chronological bibliography.

The origin of this manuscript was a literature survey project by the first two authors in 2012; since then, the other authors have contributed significantly and have greatly expanded the extent of this bibliography and the accompanying material.

## 2. Notation related to number theory and real analysis

We use ℕ {\mathbb{N}} to denote the set of positive integers, and similarly ℤ {\mathbb{Z}}, ℝ {\mathbb{R}}, and ℂ {\mathbb{C}} to denote the sets of integers, real numbers, and complex numbers, respectively. We reserve the letter p p to denote prime numbers, and sums and products such as ∑ p \sum_{p} and ∏ p | q \prod_{p\mid q} are restricted to prime values of p p.

We use the following standard conventions regarding magnitudes of complex-valued functions f f and g g, real-valued functions h h, and nonnegative real-valued functions r r and s s (of a complex or real argument z z):

- •

f ⁡ ( z) ≪ s ⁡ ( z) f(z)\ll s(z) (due to Vinogradov) means that there exists a constant C > 0 C>0 such that | f ⁡ ( z) | ≤ C ​ s ​ ( z) |f(z)|\leq Cs(z) for all values of z z under consideration;

- •

O ⁡ ( s ⁡ ( z)) O(s(z)) (due to Bachmann) represents an unspecified function f ⁡ ( z) f(z) with the property that f ⁡ ( z) ≪ s ⁡ ( z) f(z)\ll s(z);

- •

r ⁡ ( z) ≍ s ⁡ ( z) r(z)\asymp s(z) (due to Hardy) means that both r ⁡ ( z) ≪ s ⁡ ( z) r(z)\ll s(z) and s ⁡ ( z) ≪ r ⁡ ( z) s(z)\ll r(z) are true;

- •

f ⁡ ( z) ∼ g ⁡ ( z) f(z)\sim g(z) (also due to Hardy) means that lim f ⁡ ( z) / g ⁡ ( z) = 1 \lim f(z)/g(z)=1, where the location of the limit is taken from context (often as z → ∞ z\to\infty through real numbers);

- •

f ⁡ ( z) = o ⁡ ( s ⁡ ( z)) f(z)=o(s(z)) (due to Landau) means that lim f ⁡ ( z) / s ⁡ ( z) = 0 \lim f(z)/s(z)=0;

- •

f ⁡ ( z) = Ω ⁡ ( s ⁡ ( z)) f(z)=\Omega(s(z)) (due to Hardy and Littlewood) is the negation of f ⁡ ( z) = o ⁡ ( s ⁡ ( z)) f(z)=o(s(z)), or equivalently the statement lim sup | f ⁡ ( z) | / s ⁡ ( z) > 0 \limsup|f(z)|/s(z)>0;

- •

h ⁡ ( z) = Ω + ​ ( s ⁡ ( z)) h(z)=\Omega_{+}(s(z)) and h ⁡ ( z) = Ω − ​ ( s ⁡ ( z)) h(z)=\Omega_{-}(s(z)) (due in this form to Landau) mean, respectively, that lim sup h ⁡ ( z) / s ⁡ ( z) > 0 \limsup h(z)/s(z)>0 and lim inf h ⁡ ( z) / s ⁡ ( z) < 0 \liminf h(z)/s(z)<0, either of which implies h ⁡ ( z) = Ω ⁡ ( s ⁡ ( z)) h(z)=\Omega(s(z));

- •

h ⁡ ( z) = Ω ± ​ ( s ⁡ ( z)) h(z)=\Omega_{\pm}(s(z)) means that both h ⁡ ( z) = Ω + ​ ( s ⁡ ( z)) h(z)=\Omega_{+}(s(z)) and h ⁡ ( z) = Ω − ​ ( s ⁡ ( z)) h(z)=\Omega_{-}(s(z)) are true.

### 2.1. Elementary functions

As is standard in number theory, we use ϕ ⁡ ( n) \phi(n) to denote the Euler totient function, which is the number of reduced residue classes modulo n n. We use ω ⁡ ( n) \omega(n) to denote the number of distinct prime factors of n n and Ω ⁡ ( n) \Omega(n) to denote the number of prime factors of n n counted with multiplicity. We let μ ⁡ ( n) \mu(n) and Λ ⁡ ( n) \Lambda(n) denote the Möbius and von Mangoldt functions, respectively:

 | μ ⁡ ( n) = { ( − 1) ω ⁡ ( n), if n is squarefree, 0, otherwise; Λ ⁡ ( n) = { log ⁡ p, if n = p r for some r ∈ ℕ, 0, otherwise. \mu(n)=\begin{cases}(-1)^{\omega(n)},&\text{if $n$ is squarefree},\\ 0,&\text{otherwise;}\end{cases}\hskip 23.49976pt\Lambda(n)=\begin{cases}\log p,&\text{if $n=p^{r}$ for some $r\in{\mathbb{N}}$},\\ 0,&\text{otherwise.}\end{cases} |  |

We use ( a, q) (a,q) as a shorthand for gcd ⁡ ( a, q) \gcd(a,q). For any ( a, q) = 1 (a,q)=1, we define

 | c q ​ ( a) = #⁡ { b ​ (mod q): b 2 ≡ a ​ (mod q) } c_{q}(a)=\#\{b{\text{\rm\ (mod~$q$)}}\colon b^{2}\equiv a{\text{\rm\ (mod~$q$)}}\} |  |

to be the number of “square roots” of a a modulo q q. For brevity we write c q = c q ​ ( 1) c_{q}=c_{q}(1), which is also the number of real Dirichlet characters (mod q q), or equivalently the index [( ℤ / q ℤ) ×: ( ( ℤ / q ℤ) ×) 2] \bigl[({\mathbb{Z}}/q{\mathbb{Z}})^{\times}:\bigl(({\mathbb{Z}}/q{\mathbb{Z}})^{\times}\bigr)^{2}\bigr]; it turns out that c q = 2 ω ⁡ ( q) + η c_{q}=2^{\omega(q)+\eta} where η ∈ { − 1, 0, 1 } \eta\in\{-1,0,1\} depends upon the power of 2 2 dividing n n. For ( a, q) = 1 (a,q)=1, it is the case that c q ​ ( a) c_{q}(a) equals c q c_{q} if a a is a square (mod q q) and 0 0 otherwise. (Many sources define c ⁡ ( q, a) c(q,a) to be c q ​ ( a) − 1 c_{q}(a)-1, which is more convenient for some purposes and less convenient for others.)

We define two closely related logarithmic integrals

 | li ( x) \displaystyle\mathop{\rm li}(x) | = lim ε → 0 + ( ∫ 0 1 − ε d ​ t log ⁡ t + ∫ 1 + ε x d ​ t log ⁡ t) = ∑ k = 1 K ( k − 1)! ​ x ( log ⁡ x) k + O K ​ ( x ( log ⁡ x) K + 1) \displaystyle=\lim_{\varepsilon\to 0+}\bigg(\int_{0}^{1-\varepsilon}\frac{dt}{\log t}+\int_{1+\varepsilon}^{x}\frac{dt}{\log t}\bigg)=\sum_{k=1}^{K}\frac{(k-1)!x}{(\log x)^{k}}+O_{K}\bigg(\frac{x}{(\log x)^{K+1}}\bigg) |  |

 | Li ( x) \displaystyle\mathop{\rm Li}(x) | = ∫ 2 x d ​ t log ⁡ t = li ( x) − li ( 2) ≈ li ( x) − 1.04516378. \displaystyle=\int_{2}^{x}\frac{dt}{\log t}=\mathop{\rm li}(x)-\mathop{\rm li}(2)\approx\mathop{\rm li}(x)-1.04516378. |  |

### 2.2. Prime counting functions

We use the standard notation for the prime counting functions

 | π ⁡ ( x) = #{ p ≤ x } = ∑ p ≤ x 1 Π ⁡ ( x) = ∑ n ≤ x Λ ⁡ ( n) log ⁡ n = ∑ p k ≤ x 1 k = ∑ k = 1 ∞ π ⁡ ( x 1 / k) k θ ⁡ ( x) = ∑ p ≤ x log ⁡ p ψ ⁡ ( x) = ∑ n ≤ x Λ ⁡ ( n) = ∑ p k ≤ x log ⁡ p = ∑ p ≤ x ⌊ log ⁡ x log ⁡ p ⌋ ​ log ⁡ p = ∑ k = 1 ∞ θ ⁡ ( x 1 / k) k. \begin{split}\pi(x)&=\#\{p\leq x\}=\sum_{p\leq x}1\\ \Pi(x)&=\sum_{n\leq x}\frac{\Lambda(n)}{\log n}=\sum_{p^{k}\leq x}\frac{1}{k}=\sum_{k=1}^{\infty}\frac{\pi(x^{1/k})}{k}\\ \theta(x)&=\sum_{p\leq x}\log p\\ \psi(x)&=\sum_{n\leq x}\Lambda(n)=\sum_{p^{k}\leq x}\log p=\sum_{p\leq x}\bigg\lfloor\frac{\log x}{\log p}\bigg\rfloor\log p=\sum_{k=1}^{\infty}\frac{\theta(x^{1/k})}{k}.\end{split} |  |

We may replace the cutoff variable x x with any set S S of real numbers, so that for example

 | ψ ⁡ ( S) = ∑ n ∈ S Λ ⁡ ( n) and Π ⁡ ( ( 0, x]) = Π ⁡ ( x) and θ ⁡ ( ( x, y]) = θ ⁡ ( y) − θ ⁡ ( x). \psi(S)=\sum_{n\in S}\Lambda(n)\hskip 11.74988pt\text{and}\hskip 11.74988pt\Pi\big((0,x]\big)=\Pi(x)\hskip 11.74988pt\text{and}\hskip 11.74988pt\theta\big((x,y]\big)=\theta(y)-\theta(x). |  |

All of these functions have analogues for prime powers restricted to arithmetic progressions:

 | π ⁡ ( x, q, a) \displaystyle\pi(x;q,a) | = #⁡ { p ≤ x: p ≡ a ​ (mod q) } = ∑ p ≤ x p ≡ a ​ (mod q) 1 \displaystyle=\#\{p\leq x\colon p\equiv a{\text{\rm\ (mod~$q$)}}\}=\sum_{\begin{subarray}{c}p\leq x\\ p\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}1 |  |

 | Π ⁡ ( x, q, a) \displaystyle\Pi(x;q,a) | = ∑ n ≤ x n ≡ a ​ (mod q) Λ ⁡ ( n) log ⁡ n = ∑ p k ≤ x p k ≡ a ​ (mod q) 1 k \displaystyle=\sum_{\begin{subarray}{c}n\leq x\\ n\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\frac{\Lambda(n)}{\log n}=\sum_{\begin{subarray}{c}p^{k}\leq x\\ p^{k}\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\frac{1}{k} |  |

 | θ ⁡ ( x, q, a) \displaystyle\theta(x;q,a) | = ∑ p ≤ x p ≡ a ​ (mod q) log ⁡ p \displaystyle=\sum_{\begin{subarray}{c}p\leq x\\ p\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\log p |  |

 | ψ ⁡ ( x, q, a) \displaystyle\psi(x;q,a) | = ∑ n ≤ x n ≡ a ​ (mod q) Λ ⁡ ( n) = ∑ p k ≤ x p k ≡ a ​ (mod q) log ⁡ p. \displaystyle=\sum_{\begin{subarray}{c}n\leq x\\ n\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\Lambda(n)=\sum_{\begin{subarray}{c}p^{k}\leq x\\ p^{k}\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\log p. |  |

These counting functions are interesting only in the case ( a, q) = 1 (a,q)=1, a restriction that we will usually not state explicitly. Here too we may replace the first argument with a set, so that for example π ⁡ ( S, q, a) = #⁡ { p ∈ S: p ≡ a ​ (mod q) } \pi(S;q,a)=\#\{p\in S\colon p\equiv a{\text{\rm\ (mod~$q$)}}\}.

When the third argument is a set rather than an integer, the function counts prime powers that are congruent modulo q q to any element of that set; for example, θ ⁡ ( x, q, { 1, 2 }) = θ ⁡ ( x, q, 1) + θ ⁡ ( x, q, 2) \theta(x;q,\{1,2\})=\theta(x;q,1)+\theta(x;q,2). In this context, ℛ {\mathcal{R}} and 𝒩 {\mathcal{N}} always refer to the quadratic residues and nonresidues, respectively, among the reduced residues modulo q q, so that for example

 | π ⁡ ( x, q, ℛ) \displaystyle\pi(x;q,{\mathcal{R}}) | = #⁡ { p ≤ x: p ​ is a quadratic residue (mod q) } \displaystyle=\#\{p\leq x\colon p\text{ is a quadratic residue}{\text{\rm\ (mod~$q$)}}\} |  |

 | π ⁡ ( x, q, 𝒩) \displaystyle\pi(x;q,{\mathcal{N}}) | = #⁡ { p ≤ x: p ​ is a quadratic nonresidue (mod q) }. \displaystyle=\#\{p\leq x\colon p\text{ is a quadratic nonresidue}{\text{\rm\ (mod~$q$)}}\}. |  |

Note that ℛ {\mathcal{R}} contains ϕ ⁡ ( q) / c q \phi(q)/c_{q} residue classes (mod q q) and 𝒩 {\mathcal{N}} contains the other ϕ ⁡ ( q) ​ ( 1 − 1 / c q) \phi(q)(1-1/{c_{q}}) residue classes. We use 𝒜 = 𝒩 ∪ ℛ {\mathcal{A}}={\mathcal{N}}\cup{\mathcal{R}} to refer to the set of all reduced residue classes.

When these prime counting functions for arithmetic progressions appear with four arguments instead of three, the function is the difference of the counts for the two indicated arithmetic progressions; for example, ψ ⁡ ( x, q, a, 1) = ψ ⁡ ( x, q, a) − ψ ⁡ ( x, q, 1) \psi(x;q,a,1)=\psi(x;q,a)-\psi(x;q,1). (Warning: some authors use Δ \Delta for differences of this type, but we give a different meaning to Δ \Delta below in Section 2.4.) When these final two arguments are sets, we make the convention that the two counting functions being subtracted are individually normalized by the number of distinct reduced residue classes in each set; for example,

 | θ ⁡ ( x, 7, { 1, 2 }, { 3, 4, 5 }) \displaystyle\theta(x;7,\{1,2\},\{3,4,5\}) | = 1 2 ​ θ ​ ( x, 7, { 1, 2 }) − 1 3 ​ θ ​ ( x, 7, { 3, 4, 5 }) \displaystyle=\tfrac{1}{2}\theta(x;7,\{1,2\})-\tfrac{1}{3}\theta(x;7,\{3,4,5\}) |  |

(2.1) |  | Π ⁡ ( x, q, 𝒩, ℛ) \displaystyle\Pi(x;q,{\mathcal{N}},{\mathcal{R}}) | = 1 ϕ ⁡ ( q) − c q ​ Π ​ ( x, q, 𝒩) − 1 c q ​ Π ​ ( x, q, ℛ). \displaystyle=\frac{1}{\phi(q)-c_{q}}\Pi(x;q,{\mathcal{N}})-\frac{1}{c_{q}}\Pi(x;q,{\mathcal{R}}). |  |

(This convention is consistent with the four-argument notation when the last two arguments are single integers, although these is some dissonance between this convention and the three-argument notation when the last argument is a set, since that function is not normalized in this way.) There is no need for the notation to admit the possibility of two different moduli, since such a difference can always be written using residue classes of the least common multiple of the moduli: for example,

 | π ⁡ ( x, 8, 1) − π ⁡ ( x, 5, 2) = 4 ​ π ​ ( x, 40, { 1, 9, 17, 33 }, { 7, 17, 27, 37 }) = 3 ​ π ​ ( x, 40, { 1, 9, 33 }, { 7, 27, 37 }). \pi(x;8,1)-\pi(x;5,2)=4\pi\big(x;40,\{1,9,17,33\},\{7,17,27,37\}\big)=3\pi\big(x;40,\{1,9,33\},\{7,27,37\}\big). |  |

The residue class 1 ​ (mod q) 1{\text{\rm\ (mod~$q$)}} is special in some ways, and it is thus helpful to define the notation

 | π ⁡ ( x, q, 1, max) = π ⁡ ( x, q, 1) − max a ∈ ( ℤ / q ​ ℤ) × a ≢ 1 ​ (mod q) ⁡ π ⁡ ( x, q, a), π ⁡ ( x, q, 1, min) = π ⁡ ( x, q, 1) − min a ∈ ( ℤ / q ​ ℤ) × a ≢ 1 ​ (mod q) ⁡ π ⁡ ( x, q, a), \pi(x;q,1,\max)=\pi(x;q,1)-\max_{\begin{subarray}{c}a\in({\mathbb{Z}}/q{\mathbb{Z}})^{\times}\\ a\not\equiv 1{\text{\rm\ (mod~$q$)}}\end{subarray}}\pi(x;q,a),\hskip 11.74988pt\pi(x;q,1,\min)=\pi(x;q,1)-\min_{\begin{subarray}{c}a\in({\mathbb{Z}}/q{\mathbb{Z}})^{\times}\\ a\not\equiv 1{\text{\rm\ (mod~$q$)}}\end{subarray}}\pi(x;q,a), |  |

and similarly for other prime counting functions.

### 2.3. Prime ideal classes

For any number field K K (finite extension of ℚ {\mathbb{Q}}), we say that α ∈ K \alpha\in K is totally positive if α \alpha maps to a positive real number under all embeddings of K K in ℂ {\mathbb{C}}. We call ideals 𝔞 \mathfrak{a} and 𝔟 \mathfrak{b} of a number field K K congruent modulo another ideal 𝔣 ⊂ K \mathfrak{f}\subset K if both 𝔞 \mathfrak{a} and 𝔟 \mathfrak{b} are coprime to 𝔣 \mathfrak{f} and there exist totally positive algebraic integers α \alpha and β \beta in K K with α ≡ β ≡ 1 ​ (mod 𝔣) \alpha\equiv\beta\equiv 1{\text{\rm\ (mod~$\mathfrak{f}$)}} such that α ​ 𝔞 = β ​ 𝔟 \alpha\mathfrak{a}=\beta\mathfrak{b}. The equivalence classes of ideals modulo 𝔣 \mathfrak{f} form a group under ideal multiplication, with the principal ideal class 𝔎 0 \mathfrak{K}_{0} as its identity element. For a character χ \chi of this group, we abuse notation slightly by defining χ ⁡ ( 𝔞) \chi(\mathfrak{a}) on ideals 𝔞 \mathfrak{a} directly: if 𝔞 \mathfrak{a} is coprime to 𝔣 \mathfrak{f} then we set χ ⁡ ( 𝔞) = χ ⁡ ( [𝔞]) \chi(\mathfrak{a})=\chi([\mathfrak{a}]), where [𝔞] [\mathfrak{a}] is the ideal class (mod 𝔣 \mathfrak{f}) containing 𝔞 \mathfrak{a}, and if 𝔞 \mathfrak{a} is not coprime to 𝔣 \mathfrak{f} then we set χ ⁡ ( 𝔞) = 0 \chi(\mathfrak{a})=0. We can now define the Hecke–Landau zeta-function ζ ⁡ ( s, χ) \zeta(s,\chi) to be the Dirichlet series

 | ζ ⁡ ( s, χ) = ∑ 𝔞 χ ⁡ ( 𝔞) 𝔑 ​ 𝔞 s, \zeta(s,\chi)=\sum_{\mathfrak{a}}\frac{\chi(\mathfrak{a})}{\mathfrak{Na}^{s}}, |  |

Finally, for an ideal class 𝔎 \mathfrak{K}, we define prime ideal counting functions such as

 | π ⁡ ( x, 𝔎) = ∑ 𝔑 ​ 𝔭 ≤ x 𝔭 ∈ 𝔎 𝔭 ​ prime ideal 1, ψ ⁡ ( x, 𝔎) = ∑ 𝔑 ​ 𝔭 m ≤ x 𝔭 m ∈ 𝔎 𝔭 ​ prime ideal log ⁡ 𝔑 ​ 𝔭. \pi(x,\mathfrak{K})=\sum_{\begin{subarray}{c}\mathfrak{Np}\leq x\\ \mathfrak{p}\in\mathfrak{K}\\ \mathfrak{p}\,\textbf{prime ideal}\end{subarray}}1,\hskip 23.49976pt\psi(x,\mathfrak{K})=\sum_{\begin{subarray}{c}\mathfrak{Np}^{m}\leq x\\ \mathfrak{p}^{m}\in\mathfrak{K}\\ \mathfrak{p}\,\textbf{prime ideal}\end{subarray}}\log\mathfrak{Np}. |  |

### 2.4. Error terms for prime counting functions

These prime counting functions have well-known main terms, and it is useful to have a standard notation to refer to the error terms obtained by subtracting these main terms, as well as normalized versions of such error terms. We use Δ \Delta to denote error terms for the standard prime counting functions:

 | Δ ψ ​ ( x) = ψ ⁡ ( x) − x, Δ θ ​ ( x) = θ ⁡ ( x) − x, Δ Π ​ ( x) = Π ⁡ ( x) − li ( x), Δ π ​ ( x) = π ⁡ ( x) − li ( x). \Delta^{\psi}(x)=\psi(x)-x,\hskip 11.74988pt\Delta^{\theta}(x)=\theta(x)-x,\hskip 11.74988pt\Delta^{\Pi}(x)=\Pi(x)-\mathop{\rm li}(x),\hskip 11.74988pt\Delta^{\pi}(x)=\pi(x)-\mathop{\rm li}(x). |  |

(In this document’s article summaries, we will use the above normalizations even when an article subtracts a slightly different main term: we do not distinguish here between li ( x) \mathop{\rm li}(x) and Li ( x) \mathop{\rm Li}(x) and ∑ 2 ≤ n ≤ x 1 / log ⁡ n \sum_{2\leq n\leq x}1/\log n, for example.) We also use E E for normalized versions of these error terms:

 | E ψ ​ ( x) = Δ ψ ​ ( x) x, E θ ​ ( x) = Δ θ ​ ( x) x, E Π ​ ( x) = Δ Π ​ ( x) x / log ⁡ x, E π ​ ( x) = Δ π ​ ( x) x / log ⁡ x. E^{\psi}(x)=\frac{\Delta^{\psi}(x)}{\sqrt{x}},\hskip 11.74988ptE^{\theta}(x)=\frac{\Delta^{\theta}(x)}{\sqrt{x}},\hskip 11.74988ptE^{\Pi}(x)=\frac{\Delta^{\Pi}(x)}{\sqrt{x}/\log x},\hskip 11.74988ptE^{\pi}(x)=\frac{\Delta^{\pi}(x)}{\sqrt{x}/\log x}. |  |

While there is not a formula for starting with a general function f f and determining the correct denominator to use when defining E f E^{f}, the normalization factor chosen is the one for which the resulting E E function is expected to have a limiting logarithmic distribution.

It’s not uncommon to integrate these error terms: for a function f f such as π \pi, Π \Pi, θ \theta, or ψ \psi, we define 𝔄 0 f ​ ( x) = Δ f ​ ( x) {\mathfrak{A}}^{f}_{0}(x)=\Delta^{f}(x) and, for m ≥ 1 m\geq 1,

 | 𝔄 m f ​ ( x) = ∫ 0 x 𝔄 m − 1 f ​ ( t) ​ 𝑑 t. {\mathfrak{A}}^{f}_{m}(x)=\int_{0}^{x}{\mathfrak{A}}^{f}_{m-1}(t)\,dt. |  |

(Again, we ignore the fact that some articles might use a different lower endpoint for such integrals.) This operation has a predictable effect on summatory functions and explicit formulas: for example, 𝔄 m ψ ​ ( x) = ∑ n ≤ x ( Λ ⁡ ( n) − 1) ​ ( x − n) m / m! {\mathfrak{A}}_{m}^{\psi}(x)=\sum_{n\leq x}(\Lambda(n)-1)(x-n)^{m}/m! has an explicit formula containing terms of the form x ρ + m / ρ ( ρ + 1) ⋯ ( ρ + m) x^{\rho+m}/\rho(\rho+1)\cdots(\rho+m). For repeated integration of the absolute error, we also define 𝔄 | 0 | f ​ ( x) = | 𝔄 f ​ ( x) | {\mathfrak{A}}^{f}_{|0|}(x)=|{\mathfrak{A}}^{f}(x)| and, for m ≥ 1 m\geq 1,

 | 𝔄 | m | f ​ ( x) = ∫ 0 x 𝔄 | m − 1 | f ​ ( t) ​ 𝑑 t. {\mathfrak{A}}^{f}_{|m|}(x)=\int_{0}^{x}{\mathfrak{A}}^{f}_{|m-1|}(t)\,dt. |  |

There are similar logarithmic integration operators: we define A 0 f ​ ( x) = Δ f ​ ( x) A^{f}_{0}(x)=\Delta^{f}(x) and, for m ≥ 1 m\geq 1,

 | A m f ​ ( x) = ∫ 0 x A m − 1 f ​ ( t) ​ d ​ t t. A^{f}_{m}(x)=\int_{0}^{x}A^{f}_{m-1}(t)\,\frac{dt}{t}. |  |

This operation also predictably affects summatory functions and explicit formulas: for example, A m ψ ​ ( x) = ∑ n ≤ x ( Λ ⁡ ( n) − 1) ​ ( log ⁡ x n) m A_{m}^{\psi}(x)=\sum_{n\leq x}(\Lambda(n)-1)(\log\frac{x}{n})^{m} has an explicit formula containing terms of the form x ρ / ρ m + 1 x^{\rho}/\rho^{m+1}. We also use the notation A | m | f ​ ( x) A^{f}_{|m|}(x) for repeated logarithmic integration of the absolute error.

When we count primes in arithmetic progressions, the error terms Δ \Delta include a factor of ϕ ⁡ ( q) \phi(q) for simplicity: for example,

 | Δ ψ ​ ( x, q, a) = ϕ ⁡ ( q) ​ ψ ​ ( x, q, a) − x and Δ π ​ ( x, q, a) = ϕ ⁡ ( q) ​ π ​ ( x, q, a) − li ( x). \Delta^{\psi}(x;q,a)=\phi(q)\psi(x;q,a)-x\hskip 11.74988pt\text{and}\hskip 11.74988pt\Delta^{\pi}(x;q,a)=\phi(q)\pi(x;q,a)-\mathop{\rm li}(x). |  |

The normalized error terms E E are then derived from these Δ \Delta as before: for example,

 | E ψ ​ ( x, q, a) = Δ ψ ​ ( x, q, a) x and E π ​ ( x, q, a) = Δ π ​ ( x, q, a) x / log ⁡ x. E^{\psi}(x;q,a)=\frac{\Delta^{\psi}(x;q,a)}{\sqrt{x}}\hskip 11.74988pt\text{and}\hskip 11.74988ptE^{\pi}(x;q,a)=\frac{\Delta^{\pi}(x;q,a)}{\sqrt{x}/\log x}. |  |

It is convenient at times to use a prime counting function itself as the main term, and such error terms are denoted by the symbol Δ ̊ \mathord{\mathring{\Delta}}: for example,

 | Δ ̊ ψ ​ ( x, q, a) = ϕ ⁡ ( q) ​ ψ ​ ( x, q, a) − ψ ⁡ ( x) and Δ ̊ π ​ ( x, q, a) = ϕ ⁡ ( q) ​ π ​ ( x, q, a) − π ⁡ ( x). \mathord{\mathring{\Delta}}^{\psi}(x;q,a)=\phi(q)\psi(x;q,a)-\psi(x)\hskip 11.74988pt\text{and}\hskip 11.74988pt\mathord{\mathring{\Delta}}^{\pi}(x;q,a)=\phi(q)\pi(x;q,a)-\pi(x). |  |

(Typically this modification results in the same explicit formula with the principal character removed.) The corresponding normalized error terms are denoted by E ̊ \mathord{\mathring{E}}: for example,

 | E ̊ ψ ​ ( x, q, a) = Δ ̊ ψ ​ ( x, q, a) x and E ̊ π ​ ( x, q, a) = Δ ̊ π ​ ( x, q, a) x / log ⁡ x. \mathord{\mathring{E}}^{\psi}(x;q,a)=\frac{\mathord{\mathring{\Delta}}^{\psi}(x;q,a)}{\sqrt{x}}\hskip 11.74988pt\text{and}\hskip 11.74988pt\mathord{\mathring{E}}^{\pi}(x;q,a)=\frac{\mathord{\mathring{\Delta}}^{\pi}(x;q,a)}{\sqrt{x}/\log x}. |  |

We extend our convention regarding counting functions in arithmetic progressions: for example,

 | Δ ψ ​ ( x, q, a, b) = Δ ψ ​ ( x, q, a) − Δ ψ ​ ( x, q, b) and E π ​ ( x, q, a, b) = E π ​ ( x, q, a) − E π ​ ( x, q, b). \Delta^{\psi}(x;q,a,b)=\Delta^{\psi}(x;q,a)-\Delta^{\psi}(x;q,b)\hskip 11.74988pt\text{and}\hskip 11.74988ptE^{\pi}(x;q,a,b)=E^{\pi}(x;q,a)-E^{\pi}(x;q,b). |  |

Note that functions of the first type are almost redundant, since (for example) Δ ψ ​ ( x, q, a, b) = ϕ ⁡ ( q) ​ ψ ​ ( x, q, a, b) \Delta^{\psi}(x;q,a,b)=\phi(q)\psi(x;q,a,b) exactly. (And recall that some authors use Δ \Delta to mean this difference function without the factor ϕ ⁡ ( q) \phi(q).) However, there will be situations where each notation is useful to us; furthermore, this new use of Δ \Delta already follows from existing notational conventions.

It can also be convenient to define this notation for the function ψ ⁡ ( x, χ) = ∑ n ≤ x Λ ⁡ ( n) ​ χ ​ ( n) \psi(x,\chi)=\sum_{n\leq x}\Lambda(n)\chi(n), for any Dirichlet character χ \chi (see Section 3.1), in the following way:

 | Δ ψ ​ ( x, χ) = ψ ⁡ ( x, χ) − { x, if ​ χ = χ 0, 0, if ​ χ ≠ χ 0, E ψ ​ ( x, χ) = Δ ψ ​ ( x, χ) x. \Delta^{\psi}(x,\chi)=\psi(x,\chi)-\begin{cases}x,&\text{if }\chi=\chi_{0},\\ 0,&\text{if }\chi\neq\chi_{0},\end{cases}\hskip 23.49976ptE^{\psi}(x,\chi)=\frac{\Delta^{\psi}(x,\chi)}{\sqrt{x}}. |  |

All of the functions in this section so far have been real-valued (except for the last paragraph where the functions are potentially complex-valued); in the context of primes in arithmetic progressions, it is often helpful to consider vector-valued functions. We use subscripts to indicate the modulus and residue classes—for example,

 | π q; a 1, …, a r ​ ( x) = ( π ⁡ ( x, q, a 1), …, π ⁡ ( x, q, a r)) and E ̊ q; a 1, …, a r ψ ​ ( x) = ( E ̊ ψ ​ ( x, q, a 1), …, E ̊ ψ ​ ( x, q, a r)). \pi_{q;a_{1},\dots,a_{r}}(x)=\bigl(\pi(x;q,a_{1}),\dots,\pi(x;q,a_{r})\bigr)\hskip 11.74988pt\text{and}\hskip 11.74988pt\mathord{\mathring{E}}^{\psi}_{q;a_{1},\dots,a_{r}}(x)=\bigl(\mathord{\mathring{E}}^{\psi}(x;q,a_{1}),\dots,\mathord{\mathring{E}}^{\psi}(x;q,a_{r})\bigr). |  |

### 2.5. Weighted versions of prime counting functions

It is common to vary these prime counting functions by attaching a weight to each term in the sum, changing for example ∑ n ≤ x Λ ⁡ ( n) \sum_{n\leq x}\Lambda(n) to ∑ n ≤ x Λ ⁡ ( n) ​ g ​ ( n) \sum_{n\leq x}\Lambda(n)g(n). We use the following consistent notation for the most common of these variants.

As is standard, the subscript 0 0, as in the example ψ 0 ​ ( x) = 1 2 ​ ( ψ ⁡ ( x −) + ψ ⁡ ( x +)) \psi_{0}(x)=\frac{1}{2}\big(\psi(x-)+\psi(x+)\big), represents a modification of a function’s value at a jump discontinuity to equal the average of the left- and right-hand limits.

The subscript r r represents weighting by a reciprocal factor (often resulting in a “Mertens sum”); for example,

 | π r ( x) = ∑ p ≤ x 1 p, θ r ( x) = ∑ p ≤ x log ⁡ p p, and ψ r ( x; q, a) = ∑ n ≤ x n ≡ a ​ (mod q) Λ ⁡ ( n) n. \pi_{r}(x)=\sum_{p\leq x}\frac{1}{p},\hskip 11.74988pt\theta_{r}(x)=\sum_{p\leq x}\frac{\log p}{p},\hskip 11.74988pt\text{and}\hskip 11.74988pt\psi_{r}(x;q,a)=\sum_{\begin{subarray}{c}n\leq x\\ n\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\frac{\Lambda(n)}{n}. |  |

If we wish to modify one of these Mertens sums at its jump discontinuities as above, we concatenate the two subscripts: for example, π r ​ 0 ​ ( x) = 1 2 ​ ( π r ​ ( x −) + π r ​ ( x +)) \pi_{r0}(x)=\frac{1}{2}\big(\pi_{r}(x-)+\pi_{r}(x+)\big). Indeed all of our previous notational variants can apply to these sums as well—for example,

 | Δ π r ​ ( x) = π r ​ ( x) − ( log ⁡ log ⁡ x + B) and E π r ​ ( x) = x ​ log ⁡ x ⋅ Δ π r ​ ( x) \Delta^{\pi_{r}}(x)=\pi_{r}(x)-(\log\log x+B)\hskip 11.74988pt\text{and}\hskip 11.74988ptE^{\pi_{r}}(x)=\sqrt{x}\log x\cdot\Delta^{\pi_{r}}(x) |  |

for the appropriate constant B B.

The subscript e e represents weighting by an exponentially decaying function of x x rather than cutting off abruptly at x x; for example,

 | π e ( x) = ∑ p e − p / x and ψ e ( x; q, a) = ∑ n ≥ 1 n ≡ a ​ (mod q) Λ ( n) e − n / x. \pi_{e}(x)=\sum_{p}e^{-p/x}\hskip 11.74988pt\text{and}\hskip 11.74988pt\psi_{e}(x;q,a)=\sum_{\begin{subarray}{c}n\geq 1\\ n\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\Lambda(n)e^{-n/x}. |  |

In terms of their asymptotics, these exponentially weighted sums usually act like their abrupt-cutoff versions; for example, π e ​ ( x) \pi_{e}(x) has a similar size to π ⁡ ( x) \pi(x). However, their oscillations are typically damped, often resulting in rather different properties when comparing two such functions to each other (such as the exponentially weighted version having a bias for one sign while the unweighted version exhibits oscillations of sign).

The subscript l l represents weighting by a certain exponential factor with a squared logarithm, scaled by a second parameter r r: for example,

 | π l ​ ( x, r) = ∑ p e − 1 r ​ ( log ⁡ p x) 2 and ψ l ​ ( x, r, q, a) = ∑ n ≥ 1 n ≡ a ​ (mod q) Λ ⁡ ( n) ​ e − 1 r ​ ( log ⁡ n x) 2. \pi_{l}(x,r)=\sum_{p}e^{-\frac{1}{r}(\log\frac{p}{x})^{2}}\hskip 11.74988pt\text{and}\hskip 11.74988pt\psi_{l}(x,r;q,a)=\sum_{\begin{subarray}{c}n\geq 1\\ n\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\Lambda(n)e^{-\frac{1}{r}(\log\frac{n}{x})^{2}}. |  |

In asymptotic terms, this weighting is similar to restricting the range of summation to approximately [e − r ​ x, e r ​ x] [e^{-\sqrt{r}}x,e^{\sqrt{r}}x]; again, the oscillatory nature of the weighted sum can be rather different.

When the weight function is a Dirichlet character χ \chi (see Section 3.1), we follow the tradition of putting χ \chi as an extra argument rather than a subscript; for example,

 | θ ⁡ ( x, χ) = ∑ p ≤ x χ ⁡ ( p) ​ log ⁡ p. \theta(x,\chi)=\sum_{p\leq x}\chi(p)\log p. |  |

### 2.6. Summatory functions

Certain summatory functions of multiplicative functions have been analyzed using the techniques of comparative prime number theory. Two notable examples are the sums of the Möbius and Liouville functions, which are denoted by

 | M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) and L ⁡ ( x) = ∑ n ≤ x ( − 1) Ω ⁡ ( n), M(x)=\sum_{n\leq x}\mu(n)\hskip 11.74988pt\text{and}\hskip 11.74988ptL(x)=\sum_{n\leq x}(-1)^{\Omega(n)}, |  |

respectively. (The Liouville function is typically denoted by λ ⁡ ( n) = ( − 1) Ω ⁡ ( n) \lambda(n)=(-1)^{\Omega(n)}, but we avoid that notation herein to free the symbol λ \lambda for other uses.) Two conjectures that motivated substantial work in comparative prime number theory are the “Mertens conjecture”, the assertion that | M ⁡ ( x) | < x |M(x)|<\sqrt{x}, and the “Pólya problem”, the assertion that L ⁡ ( x) ≤ 0 L(x)\leq 0. (The latter assertion is often mistakenly named “Pólya’s conjecture”, but Pólya only posed and studied the problem rather than making a definitive conjecture and indeed probably found it unlikely to be true.) Both assertions have been disproved (in [1282] and [1152], respectively), although research continues into the distribution of these two functions. The weak Mertens conjecture, namely the assertion that M ⁡ ( x) ≪ x M(x)\ll\sqrt{x}, is still unresolved, although it was shown in [1136] to be incompatible with the pair of conjectures RH and LI (see Section 3.6).

The notational conventions from the previous sections are used for weighted versions of these summary functions as well; for example,

 | M ⁡ ( x, q, a) = ∑ n ≤ x n ≡ a ​ (mod q) μ ⁡ ( n) and L r ​ ( x) = ∑ n ≤ x ( − 1) Ω ⁡ ( n) n; M(x;q,a)=\sum_{\begin{subarray}{c}n\leq x\\ n\equiv a{\text{\rm\ (mod~$q$)}}\end{subarray}}\mu(n)\hskip 11.74988pt\text{and}\hskip 11.74988ptL_{r}(x)=\sum_{n\leq x}\frac{(-1)^{\Omega(n)}}{n}; |  |

the conjecture that the latter is always nonnegative (often attributed to Turán, though again he only studied the problem rather than asserting a conjecture) was also disproved in [1152]. We also define the notation Δ M ​ ( x) = M ​ ( x) \Delta^{M}(x)=M(x) and Δ L ​ ( x) = L ​ ( x) \Delta^{L}(x)=L(x) and Δ L r ​ ( x) = L r ​ ( x) \Delta^{L_{r}}(x)=L_{r}(x); while unprofitable on their own, these definitions allow us to employ the notation for repeated averaging described in Section 2.4, as well as the notation E M ​ ( x) = M ⁡ ( x) / x E^{M}(x)=M(x)/\sqrt{x} and E L ​ ( x) = L ⁡ ( x) / x E^{L}(x)=L(x)/\sqrt{x} and E L r ​ ( x) = L r ​ ( x) ​ x E^{L_{r}}(x)=L_{r}(x)\sqrt{x}.

We also introduce some standard notation for k k -free numbers, which are numbers not divisible by the k k th power of any prime, so that squarefree numbers are the case k = 2 k=2. Let Q k ​ ( x) Q_{k}(x) denote the number of k k -free integers up to x x, and define Δ Q k ​ ( x) = Q k ​ ( x) − x / ζ ⁡ ( k) \Delta^{Q_{k}}(x)=Q_{k}(x)-x/\zeta(k). For integers k ≥ 2 k\geq 2, the generalized Möbius function μ k ​ ( n) \mu_{k}(n) is defined to be μ k ​ ( n) = ( − 1) Ω ⁡ ( n) \mu_{k}(n)=(-1)^{\Omega(n)} if n n is k k -free and μ k ​ ( n) = 0 \mu_{k}(n)=0 otherwise. Note that these functions interpolate between μ 2 ​ ( n) = μ ​ ( n) \mu_{2}(n)=\mu(n) and lim k → ∞ μ k ​ ( n) = ( − 1) Ω ⁡ ( n) \lim_{k\to\infty}\mu_{k}(n)=(-1)^{\Omega(n)}. These quantities are related by the identity Q k ​ ( x) = ∑ n ≤ x μ k 2 ​ ( n) Q_{k}(x)=\sum_{n\leq x}\mu_{k}^{2}(n).

Another summatory function studied using techniques that overlap with those of comparative prime number theory is

 | D ( x) = ∑ n ≤ x τ ( n), where τ ( n) = #{ d: d ∣ n } = ∑ d | n 1. D(x)=\sum_{n\leq x}\tau(n),\text{ where }\tau(n)=\#\{d\colon d\mid n\}=\sum_{d\mid n}1. |  |

It was first proven by Dirichlet (see [1117] for a discussion of the history) that

 | D ⁡ ( x) = x ​ log ⁡ x + ( 2 ​ C 0 − 1) ​ x + O ⁡ ( x), D(x)=x\log x+(2C_{0}-1)x+O(\sqrt{x}), |  |

where C 0 C_{0} is Euler’s constant. The study of the error term Δ D ​ ( x) = D ⁡ ( x) − x ​ log ⁡ x − ( 2 ​ C 0 − 1) ​ x \Delta^{D}(x)=D(x)-x\log x-(2C_{0}-1)x is intertwined with comparative prime number theory, and one early result by Hardy [1117] demonstrates that the techniques of comparative prime theory are often applicable to the study of this error term.

### 2.7. Counting sign changes

We use the letter W W generally to denote the function that counts the number of sign changes of another function on an interval. To be pedantic, if h h is a function from ( 1, ∞) (1,\infty) to ℝ {\mathbb{R}}, then we define

 | W ( h; T) = max { n ≥ 0: there exist 1 < t 0 < t 1 < ⋯ < t n < T with h ( t j − 1) h ( t j) < 0 for all 1 ≤ j ≤ n }. W(h;T)=\max\big\{n\geq 0\colon\text{there exist }1<t_{0}<t_{1}<\cdots<t_{n}<T\\ \text{ with }h(t_{j-1})h(t_{j})<0\text{ for all }1\leq j\leq n\big\}. |  |

(One could quibble over whether taking the value 0 0 counts as a sign change regardless of its neighboring values; the results in this subject tend not to require this loophole.) We can demand large oscillations to go along with our sign changes by adding a function as an additional argument:

 | W ( h; T; S ( t)) = max { n ≥ 0: there exist 1 < t 0 < t 1 < ⋯ < t n < T with h ( t j − 1) h ( t j) < 0 for all 1 ≤ j ≤ n and | h ( t j) | > S ( t j) for all 0 ≤ j ≤ n }. W\big(h;T;S(t)\big)=\max\big\{n\geq 0\colon\text{there exist }1<t_{0}<t_{1}<\cdots<t_{n}<T\\ \text{ with }h(t_{j-1})h(t_{j})<0\text{ for all }1\leq j\leq n\text{ and }|h(t_{j})|>S(t_{j})\text{ for all }0\leq j\leq n\big\}. |  |

Given functions f f and g g from ( 1, ∞) (1,\infty) to ℝ {\mathbb{R}}, we further define W ⁡ ( f, g, T) = W ⁡ ( f − g, T) W(f,g;T)=W(f-g;T) to be the counting function of sign changes of the difference f ⁡ ( x) − g ⁡ ( x) f(x)-g(x). Certain special cases of this notation deserve a shorthand notation: we define W π ( T) = W ( π, li; T) W^{\pi}(T)=W(\pi,\mathop{\rm li};T) and W Π ( T) = W ( Π, li; T) W^{\Pi}(T)=W(\Pi,\mathop{\rm li};T), and also W θ ​ ( T) = W ⁡ ( θ, x, T) W^{\theta}(T)=W(\theta,x;T) and W ψ ​ ( T) = W ⁡ ( ψ, x, T) W^{\psi}(T)=W(\psi,x;T) where x x denotes the identity function. (As before, we do not distinguish in our summaries between li ( x) \mathop{\rm li}(x) and Li ( x) \mathop{\rm Li}(x) and ∑ 2 ≤ n ≤ x 1 / log ⁡ n \sum_{2\leq n\leq x}1/\log n in this context.) The bare notation W ⁡ ( T) W(T) is a further shorthand for W π ​ ( T) W^{\pi}(T).

In addition, given a positive integer q q and distinct reduced residues a a and b ​ (mod q) b{\text{\rm\ (mod~$q$)}}, we define W q; a, b ψ ​ ( T) = W ⁡ ( ψ ⁡ ( x, q, a), ψ ⁡ ( x, q, b), T) W^{\psi}_{q;a,b}(T)=W\big(\psi(x;q,a),\psi(x;q,b);T\big), and similarly with ψ \psi replaced by θ \theta, Π \Pi, or π \pi; we further shorten W q; a, b π ​ ( T) W^{\pi}_{q;a,b}(T) to W q; a, b ​ ( T) W_{q;a,b}(T). We may add a function as an additional argument as above to indicate large oscillations, as in W q; a, b ​ ( T, S ​ ( t)) W_{q;a,b}(T;S(t)) for example; similarly, we may replace single residue classes with sets of residue classes, as in W q; 𝒩, ℛ ​ ( T) W_{q;{\mathcal{N}},{\mathcal{R}}}(T).

### 2.8. Densities

The natural density of a set 𝒮 {\mathcal{S}} of positive real numbers is

 | 𝔡 ( 𝒮) = lim x → ∞ meas ( { 0 < t ≤ x: t ∈ 𝒮 }) x = lim x → ∞ 1 x ∫ 0 < t < x t ∈ 𝒮 d t, \mathfrak{d}({\mathcal{S}})=\lim_{x\to\infty}\frac{\mathop{\rm meas}\big(\{0<t\leq x\colon t\in{\mathcal{S}}\}\big)}{x}=\lim_{x\to\infty}\frac{1}{x}\int\limits_{\begin{subarray}{c}0<t<x\\ t\in{\mathcal{S}}\end{subarray}}dt, |  |

where “meas” denotes Lebesgue measure on ℝ {\mathbb{R}}. On the other hand, the logarithmic density of a set 𝒮 ⊂ ( 1, ∞) {\mathcal{S}}\subset(1,\infty) is

 | δ ⁡ ( 𝒮) = lim x → ∞ 1 log ⁡ x ​ ∫ 1 < t < x t ∈ 𝒮 d ​ t t. \delta({\mathcal{S}})=\lim_{x\to\infty}\frac{1}{\log x}\int\limits_{\begin{subarray}{c}1<t<x\\ t\in{\mathcal{S}}\end{subarray}}\frac{dt}{t}. |  |

An easy change of variables shows that the logarithmic density of 𝒮 {\mathcal{S}} equals the natural density of the set log ⁡ 𝒮 = { log ⁡ t: t ∈ 𝒮 } \log{\mathcal{S}}=\{\log t\colon t\in{\mathcal{S}}\}. Moreover, a partial summation argument shows that if the natural density 𝔡 ⁡ ( 𝒮) \mathfrak{d}({\mathcal{S}}) exists, then the logarithmic density δ ⁡ ( 𝒮) \delta({\mathcal{S}}) also exists and has the same value. However, there are sets whose natural density does not exist but whose logarithmic density does exist; for example, the union (over k ∈ ℕ k\in{\mathbb{N}}) of the intervals [10 2 ​ k − 1, 10 2 ​ k) [10^{2k-1},10^{2k}) has logarithmic density equal to 1 2 \frac{1}{2} but does not have a natural density.

We will use many variants of this logarithmic density notation. If f 1, …, f r f_{1},\ldots,f_{r} are functions from ( 1, ∞) (1,\infty) to ℝ {\mathbb{R}}, then we define the shorthand notation

 | δ ⁡ ( f 1, f 2, …, f r) = δ ⁡ ( { x > 1: f 1 ​ ( x) > f 2 ​ ( x) > ⋯ > f r ​ ( x) }). \delta(f_{1},f_{2},\ldots,f_{r})=\delta\big(\{x>1\colon f_{1}(x)>f_{2}(x)>\cdots>f_{r}(x)\}\big). |  |

For example, δ ( li, π) \delta(\mathop{\rm li},\pi) is the logarithmic density of the set of real numbers x > 1 x>1 for which li ( x) > π ⁡ ( x) \mathop{\rm li}(x)>\pi(x). Certain special cases of this notation can be even further abbreviated. For example, let q q be a positive integer, and let a 1, …, a r a_{1},\ldots,a_{r} be distinct reduced residues (mod q q). Then we define

 | δ q; a 1, …, a r = δ ⁡ ( π ⁡ ( x, q, a 1), …, π ⁡ ( x, q, a r)) = δ ⁡ ( { x > 1: π ⁡ ( x, q, a 1) > ⋯ > π ⁡ ( x, q, a r) }). \delta_{q;a_{1},\ldots,a_{r}}=\delta\big(\pi(x;q,a_{1}),\ldots,\pi(x;q,a_{r})\big)=\delta\big(\{x>1\colon\pi(x;q,a_{1})>\cdots>\pi(x;q,a_{r})\}\big). |  |

We also define

 | δ q; 𝒩, ℛ = δ ⁡ ( π ⁡ ( x, q, 𝒩), π ⁡ ( x, q, ℛ)) = δ ⁡ ( { x > 1: π ⁡ ( x, q, 𝒩) > π ⁡ ( x, q, ℛ) }) \delta_{q;{\mathcal{N}},{\mathcal{R}}}=\delta\big(\pi(x;q,{\mathcal{N}}),\pi(x;q,{\mathcal{R}})\big)=\delta\big(\{x>1\colon\pi(x;q,{\mathcal{N}})>\pi(x;q,{\mathcal{R}})\}\big) |  |

and similarly for δ q; ℛ, 𝒩 \delta_{q;{\mathcal{R}},{\mathcal{N}}} (these definitions are sensible when q q has primitive roots).

Finally, we define the upper and lower logarithmic densities of 𝒮 {\mathcal{S}} (which always exist) as

 | δ ¯ ​ ( 𝒮) = lim sup x → ∞ 1 log ⁡ x ​ ∫ 1 < t < x t ∈ 𝒮 d ​ t t, δ ¯ ​ ( 𝒮) = lim inf x → ∞ 1 log ⁡ x ​ ∫ 1 < t < x t ∈ 𝒮 d ​ t t, \overline{\delta}({\mathcal{S}})=\limsup_{x\to\infty}\frac{1}{\log x}\int\limits_{\begin{subarray}{c}1<t<x\\ t\in{\mathcal{S}}\end{subarray}}\frac{dt}{t},\hskip 11.74988pt\underline{\delta}({\mathcal{S}})=\liminf_{x\to\infty}\frac{1}{\log x}\int\limits_{\begin{subarray}{c}1<t<x\\ t\in{\mathcal{S}}\end{subarray}}\frac{dt}{t}, |  |

so that δ ⁡ ( 𝒮) \delta({\mathcal{S}}) exists if and only if δ ¯ ​ ( 𝒮) = δ ¯ ​ ( 𝒮) \overline{\delta}({\mathcal{S}})=\underline{\delta}({\mathcal{S}}). This notation propagates through our shorthand notations as well; for instance, δ ¯ q; 𝒩, ℛ = δ ¯ ​ ( { x > 1: π ⁡ ( x, q, 𝒩) > π ⁡ ( x, q, ℛ) }) \underline{\delta}_{q;{\mathcal{N}},{\mathcal{R}}}=\underline{\delta}\big(\{x>1\colon\pi(x;q,{\mathcal{N}})>\pi(x;q,{\mathcal{R}})\}\big).

### 2.9. Limiting distributions and density functions

Given a function h: [0, ∞) → ℝ h\colon[0,\infty)\to{\mathbb{R}}, the limiting (or asymptotic) cumulative distribution function of h h is the nondecreasing function

 | lim T → ∞ meas { t ∈ [0, T]: h ⁡ ( t) ≤ a } T = lim T → ∞ ( 1 T ∫ 0 ≤ t ≤ T h ⁡ ( t) ≤ a d t) \lim_{T\to\infty}\frac{\mathop{\rm meas}\{t\in[0,T]\colon h(t)\leq a\}}{T}=\lim_{T\to\infty}\biggl(\frac{1}{T}\int\limits_{\begin{subarray}{c}0\leq t\leq T\\ h(t)\leq a\end{subarray}}\,dt\biggr) |  |

if the limit exists (except at jump discontinuities, of which there are only a countable number). More common in comparative prime number theory is the limiting logarithmic cumulative distribution function, with the analogous definition

 | κ h ​ ( α) = lim U → ∞ 1 log ⁡ U ​ ( ∫ 1 ≤ u ≤ U h ⁡ ( u) ≤ α d ​ u u), \kappa^{h}(\alpha)=\lim_{U\to\infty}\frac{1}{\log U}\biggl(\int\limits_{\begin{subarray}{c}1\leq u\leq U\\ h(u)\leq\alpha\end{subarray}}\,\frac{du}{u}\biggr), |  |

which equivalently is the cumulative distribution function of h ⁡ ( e t) h(e^{t}). There is a corresponding limiting logarithmic density μ h \mu^{h}, which is the measure satisfying

 | μ h ​ ( ( α, β]) = ∫ α β κ h ​ ( x) ​ 𝑑 x \mu^{h}\bigl((\alpha,\beta]\bigr)=\int_{\alpha}^{\beta}\kappa^{h}(x)\,dx |  |

for any real numbers α < β \alpha<\beta. It has the property that for any bounded continuous function f ⁡ ( x) f(x),

 | lim U → ∞ 1 log ⁡ U ​ ( ∫ 1 U f ⁡ ( h ⁡ ( u)) ​ d ​ u u) = ∫ ℝ f ⁡ ( x) ​ d ​ μ h ​ ( x), \lim_{U\to\infty}\frac{1}{\log U}\biggl(\int_{1}^{U}f\bigl(h(u)\bigr)\,\frac{du}{u}\biggr)=\int_{{\mathbb{R}}}f(x)\,d\mu^{h}(x), |  |

and the continuity assumption can be omitted if μ h \mu^{h} is absolutely continuous with respect to Lebesgue measure. These logarithmic densities are probability measures and thus can be viewed as the densities of random variables. Vector-valued functions have analogous logarithmic cumulative distribution functions and logarithmic densities on ℝ r {\mathbb{R}}^{r}.

## 3. Notation related to complex analysis

As is usual in analytic number theory, we often use s = σ + i ​ t s=\sigma+it to denote a complex variable and its real and imaginary parts; its argument will be denoted by arg ⁡ ( s) \arg(s), so that s = | s | ​ e i ​ arg ⁡ s s=|s|e^{i\arg s}. If ρ \rho is a nontrivial zero of a Dirichlet (or other) L L -function, including the Riemann zeta-function, we write ρ = β + i ​ γ \rho=\beta+i\gamma to refer to its real and imaginary parts.

### 3.1. Dirichlet characters and Dirichlet L L -functions

As usual, a Dirichlet character with modulus q q is a completely multiplicative function on ℤ {\mathbb{Z}} with period q q whose support is the set of integers coprime to q q. We call characters real, complex, quadratic, (im)primitive, and induced with their standard meanings; the conductor of a character χ \chi is the modulus of the primitive character χ ∗ \chi^{*} that induces it.

We use χ 0 \chi_{0} to denote the principal character (the modulus being understood from context). When D ≠ 1 D\neq 1 is a fundamental discriminant, we let χ D \chi_{D} denote the associated quadratic character, which is a primitive character of conductor | D | |D| that is even if D > 0 D>0 and odd if D < 0 D<0. When q q is prime, we use the shorthand χ ± q \chi_{\pm q} to mean χ q \chi_{q} if q ≡ 1 ​ (mod 4) q\equiv 1{\text{\rm\ (mod~$4$)}} and χ − q \chi_{-q} if q ≡ 3 ​ (mod 4) q\equiv 3{\text{\rm\ (mod~$4$)}}. On the other hand, by χ 1 \chi_{1} we mean a hypothetical quadratic character with an exceptional zero β 1 \beta_{1}.

Every Dirichlet character gives rise to a Dirichlet L L -function L ⁡ ( s, χ) = ∑ n = 1 ∞ χ ⁡ ( n) ​ n − s L(s,\chi)=\sum_{n=1}^{\infty}\chi(n)n^{-s}. Like the Riemann zeta-function (which is the special case q = 1 q=1 and χ = χ 0 \chi=\chi_{0}), Dirichlet L L -functions have infinitely many nontrivial zeros ρ = β + i ​ γ \rho=\beta+i\gamma in the critical strip 0 < β < 1 0<\beta<1. These zeros are counted by the function

 | N ( T, χ) = #{ ρ: L ( ρ, χ) = 0, 0 < β < 1, | γ | ≤ T }. N(T,\chi)=\#\{\rho\colon L(\rho,\chi)=0,\,0<\beta<1,\,|\gamma|\leq T\}. |  |

Note the slight dissonance with the traditional notation

 | N ( T) = #{ ρ: ζ ( ρ) = 0, 0 < β < 1, 0 ≤ γ ≤ T } N(T)=\#\{\rho\colon\zeta(\rho)=0,\,0<\beta<1,\,0\leq\gamma\leq T\} |  |

which counts only nontrivial zeros of ζ ⁡ ( s) \zeta(s) in the upper half-plane: this suffices for ζ ⁡ ( s) \zeta(s) due to the Schwarz reflection principle, but Dirichlet L L -functions do not all possess that symmetry.

Sums over zeros of Dirichlet L L -functions (of the type that arise in explicit formulas, for example) often do not converge absolutely, and therefore we adopt the standing convention that sums over nontrivial zeros are limits of their symmetric truncations:

 | ∑ ρ f ⁡ ( ρ) = lim T → ∞ ∑ L ⁡ ( ρ, χ) = 0 0 < β < 1 | γ | ≤ T f ⁡ ( ρ). \sum_{\rho}f(\rho)=\lim_{T\to\infty}\sum_{\begin{subarray}{c}L(\rho,\chi)=0\\ 0<\beta<1\\ |\gamma|\leq T\end{subarray}}f(\rho). |  |

### 3.2. Landau’s theorem

For a real-valued function A ⁡ ( x) A(x), define

 | g ⁡ ( s) = ∫ 1 ∞ A ⁡ ( x) x s ​ 𝑑 x g(s)=\int_{1}^{\infty}\frac{A(x)}{x^{s}}\,dx |  |

Typically there will be a real number σ 0 \sigma_{0} such that this integral converges when σ > σ 0 \sigma>\sigma_{0} and diverges when σ < σ 0 \sigma<\sigma_{0}. Landau proved that if A ⁡ ( x) A(x) is eventually positive or eventually negative, then g ⁡ ( s) g(s) has a singularity at s = σ 0 s=\sigma_{0} (that is, g ⁡ ( s) g(s) must have a rightmost singularity on the real axis).

The contrapositive of this theorem is a useful tool in comparative prime number theory: Suppose that g ⁡ ( s) g(s) has no singularities on the subray { σ ∈ ℝ: σ > σ 1 } \{\sigma\in{\mathbb{R}}\colon\sigma>\sigma_{1}\} of the real axis (that is, g ⁡ ( s) g(s) is analytic on a neighborhood of that ray), but g ⁡ ( s) g(s) is not analytic in the half-plane { s ∈ ℂ: σ > σ 1 } \{s\in{\mathbb{C}}\colon\sigma>\sigma_{1}\}. Then A ⁡ ( x) A(x) has arbitrarily large sign changes.

### 3.3. Explicit formulas

As mentioned earlier, one of the defining characteristics of comparative prime number theory is the presence of an “explicit formula”. There is no precise definition of that term, but typically an explicit formula contains a sum over the (nontrivial) zeros of some L L -function. The prototypical example is the explicit formula

 | ψ 0 ​ ( x) = x − ∑ ρ x ρ ρ − log ⁡ 2 ​ π − 1 2 ​ log ⁡ ( 1 − 1 x 2) \psi_{0}(x)=x-\sum_{\rho}\frac{x^{\rho}}{\rho}-\log 2\pi-\frac{1}{2}\log\bigg(1-\frac{1}{x^{2}}\bigg) |  |

for the Chebyshev function ψ ⁡ ( x) \psi(x) modified at its jump discontinuities; the fact that this is an exact equality for all x > 1 x>1 is one of the most beautiful statements in analytic number theory.

Explicit formulas for prime-counting functions yield explicit formulas for their normalized error terms; for example, assuming the generalized Riemann hypothesis,

 | E θ ( x; q, a, b) = c q ( b) − c q ( a) − ∑ χ ​ (mod q) ( χ ¯ ( a) − χ ¯ ( b)) ∑ γ ∈ ℝ L ⁡ ( 1 / 2 + i ​ γ, χ) = 0 x i ​ γ 1 2 + i ​ γ + O q ( x − 1 / 6). E^{\theta}(x;q,a,b)=c_{q}(b)-c_{q}(a)-\sum_{\chi{\text{\rm\ (mod~$q$)}}}\big(\overline{\chi}(a)-\overline{\chi}(b)\big)\sum_{\begin{subarray}{c}\gamma\in{\mathbb{R}}\\ L(1/2+i\gamma,\chi)=0\end{subarray}}\frac{x^{i\gamma}}{\frac{1}{2}+i\gamma}+O_{q}(x^{-1/6}). |  |

This formula is helpful for studying when E θ ​ ( x, q, a, b) > 0 E^{\theta}(x;q,a,b)>0, or equivalently when θ ⁡ ( x, q, a) > θ ⁡ ( x, q, b) \theta(x;q,a)>\theta(x;q,b). Note that each summand in the inner sum oscillates around a circle of fixed radius (one that decreases as γ \gamma increases); while this inner sum is not literally bounded, it is bounded on average over x x and possesses a limiting logarithmic distribution. Therefore E θ ​ ( x, q, a, b) E^{\theta}(x;q,a,b) has a limiting logarithmic distribution with mean c q ​ ( b) − c q ​ ( a) c_{q}(b)-c_{q}(a), the sign of which depends on whether a a and b b are quadratic residues or nonresidues modulo q q.

### 3.4. The power-sum method

A great deal of early progress in comparative prime number theory, particularly the unconditional results, relied on the study of linear combinations of powers of complex numbers, namely sums of the shape

 | s v = ∑ j = 1 n b j ​ z j v. s_{v}=\sum_{j=1}^{n}b_{j}z_{j}^{v}. |  |

Lower bounds for such sums were systematically developed by Turán and Sós. While there are many variants of these lower bounds that have been obtained, they can be grouped into two main categories.

The “first main theorem” is a type of result that applies when the z j z_{j} are large. For example, suppose that z 1, …, z n z_{1},\ldots,z_{n} are distinct complex numbers with | z n | ≥ 1 |z_{n}|\geq 1 for all n n. For any nonnegative integer m m, there exists an integer m + 1 ≤ v ≤ m + n m+1\leq v\leq m+n such that

 | | s v | ≥ ( n A ⁡ ( m + n)) n ​ | s 0 |, |s_{v}|\geq\bigg(\frac{n}{A(m+n)}\bigg)^{n}|s_{0}|, |  |

where A A is an absolute constant.

The “second main theorem” is a type of result that applies when the z j z_{j} are small. For example, suppose that z 1, …, z n z_{1},\ldots,z_{n} are distinct complex numbers with 1 ≥ | z 1 | ≥ ⋯ ≥ | z n | 1\geq|z_{1}|\geq\cdots\geq|z_{n}|. For any nonnegative integer m m, there exists an integer m + 1 ≤ v ≤ m + n m+1\leq v\leq m+n such that

 | | s v | ≥ ( n B ⁡ ( m + n)) n ​ min 1 ≤ j ≤ n ​ | ∑ n = 1 j b n |, |s_{v}|\geq\bigg(\frac{n}{B(m+n)}\bigg)^{n}\min_{1\leq j\leq n}\bigg|\sum_{n=1}^{j}b_{n}\bigg|, |  |

where B B is an absolute constant.

Instead of restricting the candidate exponents v v to an interval of exactly n n consecutive integers, we may allow candidates from a longer range of exponents. For example, in the “second main theorem” (so that 1 ≥ | z 1 | ≥ ⋯ ≥ | z n | 1\geq|z_{1}|\geq\cdots\geq|z_{n}|), let m ≥ N ≥ n m\geq N\geq n; then there exists an integer m + 1 ≤ v ≤ m + N m+1\leq v\leq m+N such that

 | | s v | ≥ ( N B ​ m) N ​ min 1 ≤ j ≤ n ​ | ∑ n = 1 j b n |. |s_{v}|\geq\bigg(\frac{N}{Bm}\bigg)^{N}\min_{1\leq j\leq n}\bigg|\sum_{n=1}^{j}b_{n}\bigg|. |  |

For the “second main theorem”, one can also obtain better conclusions by adding an “argument restriction”, that is, the assumption that each | arg ⁡ z j | ≥ ε |\arg z_{j}|\geq\varepsilon for some fixed ε > 0 \varepsilon>0. Stronger results can also be obtained by assuming that each b j b_{j} is a nonnegative real number, and strengthened further by restricting to the special case b 1 = ⋯ = b n = 1 b_{1}=\cdots=b_{n}=1.

Note that these results show that some s v s_{v} is large in modulus but gives no information about its argument. Turán (somewhat unhelpfully) calls these results “two-sided” theorems. There exist analogous results where the lower bound applies not just to | s v | |s_{v}| but to ℜ ⁡ s v \Re s_{v} or − ℜ ⁡ s v -\Re s_{v}; Turán calls such results “one-sided” theorems.

### 3.5. k k -functions

A great deal of the work of Kaczorowski involves certain functions called k k -functions, which are superficially similar to sums that appear in explicit formulas for ψ ⁡ ( x, χ) \psi(x,\chi). For ℑ ⁡ z > 0 \Im z>0, define

 | k ⁡ ( z, χ) = ∑ γ > 0 e ρ ​ z and K ⁡ ( z, χ) = ∑ γ > 0 e ρ ​ z ρ, \displaystyle k(z,\chi)=\sum_{\gamma>0}e^{\rho z}\hskip 11.74988pt\text{and}\hskip 11.74988ptK(z,\chi)=\sum_{\gamma>0}\frac{e^{\rho z}}{\rho}, |  |

where the sums are over zeros of L ⁡ ( s, χ) L(s,\chi) in the upper half-plane.

These functions can be regarded as having their domain equal to ℳ {\mathcal{M}}, the Riemann surface for log ⁡ z \log z; every point on the surface can be uniquely written as r ​ e i ​ a re^{ia} where r > 0 r>0 and a ∈ ℝ a\in{\mathbb{R}}. Let z c z^{c} denote the natural extension of complex conjugation to ℳ {\mathcal{M}}, namely ( r ​ e i ​ a) c = r ​ e − i ​ a (re^{ia})^{c}=re^{-ia}; also let z ∗ z^{*} denote an extension of multiplication by − 1 -1 to ℳ {\mathcal{M}}, namely ( r ​ e i ​ a) ∗ = r ​ e i ⁡ ( a − π) (re^{ia})^{*}=re^{i(a-\pi)}.

Certain functions appear frequently in connection to k k -functions: define

 | D ( z, χ) = − ∑ β > 0 L ⁡ ( β, χ) = 0 e β ​ z + 1 e 2 ​ z − 1 { e 3 ​ z + e 2 ​ z − 1, if ​ χ = χ 0, e z, if ​ χ ≠ χ 0 ​ and ​ χ ​ ( − 1) = 1, e 2 ​ z, if ​ χ ​ ( − 1) = − 1. D(z,\chi)=-\sum_{\begin{subarray}{c}\beta>0\\ L(\beta,\chi)=0\end{subarray}}e^{\beta z}+\frac{1}{e^{2z}-1}\begin{cases}e^{3z}+e^{2z}-1,&\text{if }\chi=\chi_{0},\\ e^{z},&\text{if }\chi\neq\chi_{0}\text{ and }\chi(-1)=1,\\ e^{2z},&\text{if }\chi(-1)=-1.\end{cases} |  |

Further define

 | F ⁡ ( x, χ) = lim y → 0 + ( K ⁡ ( x + i ​ y, χ) + K ⁡ ( x + i ​ y, χ ¯) ¯) \displaystyle F(x,\chi)=\lim_{y\to 0^{+}}\bigg(K(x+iy,\chi)+\overline{K(x+iy,\overline{\chi})}\bigg) |  |

and

 | R 1 ​ ( x) = 1 2 ​ log ⁡ ( 1 − e − 2 ​ x), R − 1 ​ ( x) = 1 2 ​ log ⁡ e x − 1 e x + 1. R_{1}(x)=\frac{1}{2}\log(1-e^{-2x}),\hskip 11.74988ptR_{-1}(x)=\frac{1}{2}\log\frac{e^{x}-1}{e^{x}+1}. |  |

Certain constants also appear frequently: define

 | B ⁡ ( χ) = ∑ β > 0 L ⁡ ( β, χ) = 0 1 β − C 0 2 − 1 2 ​ log ⁡ π q + F ⁡ ( 0, χ) − { 1, if ​ χ = χ 0, 0, if ​ χ ≠ χ 0 ​ and ​ χ ​ ( − 1) = 1, log ⁡ 2, if ​ χ ​ ( − 1) = − 1 B(\chi)=\sum_{\begin{subarray}{c}\beta>0\\ L(\beta,\chi)=0\end{subarray}}\frac{1}{\beta}-\frac{C_{0}}{2}-\frac{1}{2}\log\frac{\pi}{q}+F(0,\chi)-\begin{cases}1,&\text{if }\chi=\chi_{0},\\ 0,&\text{if }\chi\neq\chi_{0}\text{ and }\chi(-1)=1,\\ \log 2,&\text{if }\chi(-1)=-1\end{cases} |  |

(note that B ⁡ ( χ) B(\chi) is not the same as a constant of the same name related to the Hadamard product expansion of L ⁡ ( s, χ) L(s,\chi)) and C ⁡ ( χ) = B ⁡ ( χ) + C 0 + log ⁡ 2 ​ π q C(\chi)=B(\chi)+C_{0}+\log\frac{2\pi}{q}.

### 3.6. Hypotheses on zeros

It is extremely difficult to obtain unconditional results in comparative prime number theory, particularly where limiting logarithmic distributions and densities are concerned. Certain assumptions on the zeros of Dirichlet L L -functions therefore arise repeatedly in this subject. The most famous of these is the generalized Riemann hypothesis (GRH), sometimes called the Riemann–Piltz conjecture, which asserts that all nontrivial zeros of all Dirichlet L L -functions have real part equal to 1 2 \frac{1}{2}. We use σ 0 \sigma_{0} -GRH to denote the weaker (but still currently inaccessible) assertion that L ⁡ ( σ + i ​ t, χ) L(\sigma+it,\chi) does not vanish when σ > σ 0 \sigma>\sigma_{0}, so that 1 1 -GRH is trivial and 1 2 \frac{1}{2} -GRH is the same as the full GRH.

Given a nonempty set X X of Dirichlet L L -functions (or, abusing notation slightly, Dirichlet characters), we let Θ ⁡ ( X) \Theta(X) denote the supremum of the real parts of their zeros, that is, the smallest real number such that Θ ⁡ ( X) \Theta(X) -GRH holds. We use the abbreviation Θ ⁡ ( q) \Theta(q) when X X is the set of all Dirichlet characters modulo q q, as well as Θ ⁡ ( χ) \Theta(\chi) when X X consists of the single Dirichlet character χ \chi. The assertion that some Dirichlet L L -function in X X has a zero with real part exactly equal to Θ ⁡ ( X) \Theta(X) is abbreviated SA for “supremum attained” (and sometimes referred to as “Ingham’s condition”). We may write SA ( X) (X) to emphasize that we are considering a specific set of Dirichlet L L -functions, but the set is often inferred from context (this remark applies similarly to the remainder of the notation in this section). We note that GRH implies SA but that Θ ⁡ ( X) = 1 \Theta(X)=1 is inconsistent with SA.

Regarding the vertical distributions of the zeros, we use HC to denote the “Haselgrove condition” that no Dirichlet character (in the set under discussion) vanishes on the segment 0 < σ < 1 0<\sigma<1 of the real axis. Such a real zero would create a non-oscillatory term in relevant explicit formulas, one that could result in an unexpected source of bias. By continuity, HC implies that there exists a positive constant E k E_{k} such that these L ⁡ ( s, χ) L(s,\chi) are nonzero on the rectangle { 0 < σ < 1, | t | ≤ E k } \{0<\sigma<1,\,|t|\leq E_{k}\}; we write HC ( E k) (E_{k}) if we need to refer to this parameter.

The notation GRH ( H) (H) (sometimes called the “finite Riemann–Piltz” conjecture) denotes the generalized Riemann hypothesis “up to height H H ”, namely the statement that if ρ \rho is a nontrivial zero of L ⁡ ( s, χ) L(s,\chi) with | γ | ≤ H |\gamma|\leq H, then β = 1 2 \beta=\frac{1}{2}. Note that HC ( E k) (E_{k}) implies GRH ( H) (H) if E k ≥ H E_{k}\geq H; on the other hand, GRH ( H) (H) gives no constraint at all upon zeros on the critical line. We therefore use the notation GRH ( H, E k) (H,E_{k}) to denote the combination of GRH ( H) (H) and HC ( E k) (E_{k}), the latter of which constrains only the zeros on the critical line when E k < H E_{k}<H. Note also that GRH ( 0) (0) is almost the same as HC, except that GRH ( 0) (0) allows for the possibility of a zero at s = 1 2 s=\frac{1}{2}.

The arithmetic nature of the imaginary parts (ordinates) of zeros of L ⁡ ( s, χ) L(s,\chi) is also significant in comparative prime number theory. We write LI (sometimes called GSH for the “grand simplicity hypothesis”) to denote the “linear independence” assertion that the multiset of nonnegative ordinates of zeros of the relevant Dirichlet L L -functions is linearly independent over the rational numbers. In particular, LI implies that all zeros are simple and that L ⁡ ( 1 2, χ) ≠ 0 L(\frac{1}{2},\chi)\neq 0. We use LI ( σ) (\sigma) to denote the corresponding linear independence conjecture restricted to the zeros with real parts greater than or equal to σ \sigma.

For the Riemann zeta-function, the Riemann hypothesis (RH) is the assertion that all nontrivial zeros of ζ ⁡ ( s) \zeta(s) have real part equal to 1 2 \frac{1}{2}. Almost all of the other notation above would be used in the same form when referring to ζ ⁡ ( s) \zeta(s), although Θ ⁡ ( { ζ ⁡ ( s) }) \Theta(\{\zeta(s)\}) is abbreviated simply to Θ \Theta. These same abbreviations are also used for analogous hypotheses on zeros of other L L -functions that should be clear from context.

## 4. Types of questions

Given two functions f, g: ( 1, ∞) → ℝ f,g\colon(1,\infty)\to{\mathbb{R}} that are asymptotic to each other, such as π ⁡ ( x) \pi(x) and li ( x) \mathop{\rm li}(x) or π ⁡ ( x, 4, 1) \pi(x;4,1) and π ⁡ ( x, 4, 3) \pi(x;4,3), the questions that comparative prime number theory tends to ask about the pair of functions are:

1. (1)

Are there arbitrarily large values of x x for which f ⁡ ( x) > g ⁡ ( x) f(x)>g(x), and arbitrarily large values of x x for which g ⁡ ( x) < f ⁡ ( x) g(x)<f(x)? In other words, does the difference f ⁡ ( x) − g ⁡ ( x) f(x)-g(x) change signs infinitely often? (These are not quite mathematically identical because of the possibility of plentiful or carefully arranged ties f ⁡ ( x) = g ⁡ ( x) f(x)=g(x), so implicit in this question is asking whether such ties are rare.) The other alternative is that one of the functions exceeds the other for all sufficiently large x x.

2. (2)

How large and positive can the difference f ⁡ ( x) − g ⁡ ( x) f(x)-g(x) get? How large and negative can it get?

3. (3)

More generally, what is the distribution of values of f ⁡ ( x) − g ⁡ ( x) f(x)-g(x)? Is it possible that some suitably normalized version of this difference, such as ( f ⁡ ( x) − g ⁡ ( x)) / x (f(x)-g(x))/\sqrt{x}, actually has a limiting distribution or a limiting logarithmic distribution?

4. (4)

How often does the difference f ⁡ ( x) − g ⁡ ( x) f(x)-g(x) change sign? How many sign changes are there in ( 1, X) (1,X) as a function of X X? How close can we take Y = Y ⁡ ( X) Y=Y(X) to X X to ensure that there is always a sign change in [X, Y] [X,Y]?

5. (5)

What is the natural density of the set of real numbers x > 1 x>1 for which f ⁡ ( x) > g ⁡ ( x) f(x)>g(x)? What is its logarithmic density δ ⁡ ( f, g) \delta(f,g)? (Typically we believe that the natural densities of such sets do not exist in prime number races, but that their logarithmic densities do exist.)

6. (6)

Given a family of races, such as π ⁡ ( x, q, 𝒩) \pi(x;q,{\mathcal{N}}) versus π ⁡ ( x, q, ℛ) \pi(x;q,{\mathcal{R}}): how do answers to the above questions, such as δ q; 𝒩, ℛ \delta_{q;{\mathcal{N}},{\mathcal{R}}}, depend upon the member of the family ( q q in this case)? Do the distributions of the members of the family tend to some limit, such as a normal distribution?

Some of the above questions have analogues for several functions f 1, …, f r: ( 1, ∞) → ℝ f_{1},\ldots,f_{r}\colon(1,\infty)\to{\mathbb{R}} considered together:

1. (7)

Are there arbitrarily large values of x x for which f 1 ​ ( x) > ⋯ > f r ​ ( x) f_{1}(x)>\cdots>f_{r}(x)? Does this remain true no matter how we permute the f j f_{j}?

2. (8)

More generally, what is the distribution of values of the vector ( f 1 ​ ( x), …, f r ​ ( x)) ∈ ℝ r \big(f_{1}(x),\ldots,f_{r}(x)\big)\in{\mathbb{R}}^{r}? Is it possible that some suitably normalized version of this difference actually has a limiting distribution or a limiting logarithmic distribution?

3. (9)

What is the natural density of the set of real numbers x > 1 x>1 for which f 1 ​ ( x) > ⋯ > f r ​ ( x) f_{1}(x)>\cdots>f_{r}(x)? What is its logarithmic density δ ⁡ ( f 1, …, f r) \delta(f_{1},\ldots,f_{r})? (As before, we believe that the natural densities of such sets do not exist in prime number races, but that their logarithmic densities do exist.)

4. (10)

Given a family of such r r -way races, how do answers to the above questions depend upon the member of the family? Do the distributions of the members of the family tend to some limit, such as a multivariate normal distribution?

The articles [1172] and [1185] by Knapowski and Turán present organized schema for problems in comparative prime number theory, as do surveys of these topics by Kaczorowski [1322] and by Ford and Konyagin [1333], although several of the questions listed above had not yet been investigated sufficiently deeply to make some of their lists.

## Acknowledgments

We gratefully thank Devang Agarwal, Alexandre Bailleul, Michael Coons, Alia Hamieh, Elchin Hasanalizade, Daniel R. Johnston, Farid Jokar, Florent Jouve, Shin-ya Koyama, L a T e X Stack Exchange user “moewe”, Michael J. Mossinghoff, Nathan Ng, and Alan Xiang for their contributions to this manuscript. We also thank the anonymous referees for their thorough readings and detailed suggestions for corrections and improvements. Many authors’ research was supported by the Natural Science and Engineering Research Council of Canada.

## Chronological bibliography

The annotated bibliography begins here, with all of the sources cited and summarized listed in chronological order; items in this chronological list are labeled by their number alone, such as [123]. Following the annotated bibliography is a second list, in alphabetical order by author, of the same set of sources but without annotations; items in this alphabetical list have been given labels that are numbers following the letter “A” (for “alphabetical”), such as [A45], to distinguish them from the labels in the main list. Each entry in the second bibliography links to its corresponding entry and annotation in the first bibliography.

Our goal has been to describe the results using a single system of notation, both to avoid the need to define notation in individual annotations and to propose a unified notation for current and future practitioners of comparative prime number theory. Any notation in a summary that is not defined there can be found or deduced from the detailed material in Sections 2–3.

## References

- [1] A. Akbary, N. Ng and M. Shahabi “Limiting distributions of the classical error terms of prime number theory” In *Q. J. Math.*65.3, 2014, pp. 743–780 DOI: [10.1093/qmath/hat059][4]
- [2] Emre Alkan “Biased behavior of weighted Mertens sums” In *Int. J. Number Theory*16.3, 2020, pp. 547–577 DOI: [10.1142/S1793042120500281][5]
- [3] Emre Alkan “Variations on criteria of Pólya and Turán for the Riemann hypothesis” In *J. Number Theory*225, 2021, pp. 90–124 DOI: [10.1016/j.jnt.2021.01.004][6]
- [4] R.. Anderson and H.. Stark “Oscillation theorems” In *Analytic number theory (Philadelphia, Pa., 1980)*899, Lecture Notes in Math. Springer, Berlin-New York, 1981, pp. 79–106
- [5] Miho Aoki and Shin-ya Koyama “Chebyshev’s bias against splitting and principal primes in global fields” In *J. Number Theory*245, 2023, pp. 233–262 DOI: [10.1016/j.jnt.2022.10.005][7]
- [6] Christian Axler “New estimates for some integrals of functions defined over primes” In *Funct. Approx. Comment. Math.*68.2, 2023, pp. 207–229 DOI: [10.7169/facm/2049][8]
- [7] Marco Aymone “A note on prime number races and zero free regions for L L functions” In *Int. J. Number Theory*18.1, 2022, pp. 1–8 DOI: [10.1142/S1793042122500014][9]
- [8] Alexandre Bailleul “Chebyshev’s bias in dihedral and generalized quaternion Galois groups” In *Algebra Number Theory*15.4, 2021, pp. 999–1041 DOI: [10.2140/ant.2021.15.999][10]
- [9] Alexandre Bailleul “Explicit Kronecker–Weyl theorems and applications to prime number races” In *Res. Number Theory*8.3, 2022, pp. Paper No. 4334 DOI: [10.1007/s40993-022-00349-2][11]
- [10] Alexandre Bailleul, Lucile Devin, Daniel Keliher and Wanlin Li “Exceptional biases in counting primes over function fields” In *J. Lond. Math. Soc. (2)*109.3, 2024, pp. Paper No. e1287632 DOI: [10.1112/jlms.12876][12]
- [11] E.. Balanzario and S. Hernández “On the number of large oscillations of some arithmetical power series” In *Arch. Math. (Basel)*81.3, 2003, pp. 285–290 DOI: [10.1007/s00013-003-4704-2][13]
- [12] R. Balasubramanian, K. Ramachandra and M.. Subbarao “On the error function in the asymptotic formula for the counting function of k k -full numbers” In *Acta Arith.*50.2, 1988, pp. 107–118 DOI: [10.4064/aa-50-2-107-118][14]
- [13] K.. Bartz “On some complex explicit formulae connected with the Möbius function. I, II” In *Acta Arith.*57.4, 1991, pp. 283–293295–305 DOI: [10.4064/aa-57-4-283-293][15]
- [14] P.. Bateman, J.. Brown, R.. Hall, K.. Kloss and Rosemarie. Stemmler “Linear relations connecting the imaginary parts of the zeros of the zeta function” In *Computers in number theory (Proc. Sci. Res. Council Atlas Sympos. No. 2, Oxford, 1969)*Academic Press, London, 1971, pp. 11–19
- [15] Paul. Bateman and Emil Grosswald “On a theorem of Erdös and Szekeres” In *Illinois J. Math.*2, 1958, pp. 88–98 URL: [http://projecteuclid.org/euclid.ijm/1255380836][16]
- [16] C. Bays, K. Ford, R.. Hudson and M. Rubinstein “Zeros of Dirichlet L L -functions near the real axis and Chebyshev’s bias” In *J. Number Theory*87.1, 2001, pp. 54–76 DOI: [10.1006/jnth.2000.2601][17]
- [17] C. Bays and R.. Hudson “The segmented sieve of Eratosthenes and primes in arithmetic progressions to 10 12 10^{12} ” In *Nordisk Tidskr. Informationsbehandling (BIT)*17.2, 1977, pp. 121–127 DOI: [10.1007/bf01932283][18]
- [18] C. Bays and R.. Hudson “Details of the first region of integers x x with π 3, 2 ​ ( x) < π 3, 1 ​ ( x) \pi_{3,2}(x)<\pi_{3,1}(x) ” In *Math. Comp.*32.142, 1978, pp. 571–576 DOI: [10.2307/2006165][19]
- [19] C. Bays and R.. Hudson “Numerical and graphical description of all axis crossing regions for the moduli 4 4 and 8 8 which occur before 10 12 10^{12} ” In *Internat. J. Math. Math. Sci.*2.1, 1979, pp. 111–119 DOI: [10.1155/S0161171279000119][20]
- [20] C. Bays and R.. Hudson “Zeroes of Dirichlet L L -functions and irregularities in the distribution of primes” In *Math. Comp.*69.230, 2000, pp. 861–866 DOI: [10.1090/S0025-5718-99-01105-9][21]
- [21] Carter Bays and Richard. Hudson “On the fluctuations of Littlewood for primes of the form 4 ​ n ± 1 4n\pm 1 ” In *Math. Comp.*32.141, 1978, pp. 281–286 DOI: [10.2307/2006277][22]
- [22] Carter Bays and Richard. Hudson “The appearance of tens of billions of integers x x with π 24, 13 ​ ( x) < π 24, 1 ​ ( x) \pi_{24,13}(x)<\pi_{24,1}(x) in the vicinity of 10 12 10^{12} ” In *J. Reine Angew. Math.*299/300, 1978, pp. 234–237 DOI: [10.1515/crll.1978.299-300.234][23]
- [23] Carter Bays and Richard. Hudson “The cyclic behavior of primes in the arithmetic progressions modulo 11 11 ” In *J. Reine Angew. Math.*339, 1983, pp. 215–220 DOI: [10.1515/crll.1983.339.215][24]
- [24] Carter Bays and Richard. Hudson “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Math. Comp.*69.231, 2000, pp. 1285–1296
- [25] H.-J. Bentz “Discrepancies in the distribution of prime numbers” In *J. Number Theory*15.2, 1982, pp. 252–274 DOI: [10.1016/0022-314X(82)90030-0][25]
- [26] H.-J. Bentz and J. Pintz “Quadratic residues and the distribution of prime numbers” In *Monatsh. Math.*90.2, 1980, pp. 91–100 DOI: [10.1007/BF01303260][26]
- [27] H.-J. Bentz and J. Pintz “Über das Tschebyschef-Problem” In *Resultate Math.*5.1, 1982, pp. 1–5 DOI: [10.1007/bf03323296][27]
- [28] Hans-J. Bentz and János Pintz “Über eine Verallgemeinerung des Tschebyschef-Problems” In *Math. Z.*174.1, 1980, pp. 35–41 DOI: [10.1007/BF01215079][28]
- [29] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. I” In *J. Reine Angew. Math.*307/308, 1979, pp. 411–417 DOI: [10.1515/crll.1979.307-308.411][29]
- [30] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. II” In *J. Reine Angew. Math.*313, 1980, pp. 52–58 DOI: [10.1515/crll.1980.313.52][30]
- [31] D.. Best and T.. Trudgian “Linear relations of zeroes of the zeta-function” In *Math. Comp.*84.294, 2015, pp. 2047–2058 DOI: [10.1090/S0025-5718-2014-02916-5][31]
- [32] Gautami Bhowmik, Olivier Ramaré and Jan-Christoph Schlage–Puchta “Tauberian oscillation theorems and the distribution of Goldbach numbers” In *J. Théor. Nombres Bordeaux*28.2, 2016, pp. 291–299
- [33] Peter Borwein, Ron Ferguson and Michael. Mossinghoff “Sign changes in sums of the Liouville function” In *Math. Comp.*77.263, 2008, pp. 1681–1694 DOI: [10.1090/S0025-5718-08-02036-X][32]
- [34] R.. Brent and Jan van Lune “A note on Pólya’s observation concerning Liouville’s function” In *Herman J. J. te Riele Liber Amicorum*, CWI, 2011, pp. 92–97 URL: [https://arxiv.org/abs/1112.4911][33]
- [35] Richard. Brent “Irregularities in the distribution of primes and twin primes” Collection of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday In *Math. Comp.*29, 1975, pp. 43–56 DOI: [10.2307/2005460][34]
- [36] Hung. Bui, Alexandra Florea and Micah. Milinovich “Negative discrete moments of the derivative of the Riemann zeta-function” In *Bull. Lond. Math. Soc.*56.8, 2024, pp. 2680–2703
- [37] J. Büthe “On the first sign change in Mertens’ theorem” In *Acta Arith.*171.2, 2015, pp. 183–195 DOI: [10.4064/aa171-2-5][35]
- [38] Jan Büthe “An analytic method for bounding ψ ⁡ ( x) \psi(x) ” In *Math. Comp.*87.312, 2018, pp. 1991–2009 DOI: [10.1090/mcom/3264][36]
- [39] B Cha and B.-H. Im “Chebyshev’s bias in Galois extensions of global function fields” In *J. Number Theory*131.10, 2011, pp. 1875–1886 DOI: [10.1016/j.jnt.2011.03.011][37]
- [40] B. Cha, D. Fiorilli and F. Jouve “Prime number races for elliptic curves over function fields” In *Ann. Sci. Éc. Norm. Supér. (4)*49.5, 2016, pp. 1239–1277 DOI: [10.24033/asens.2308][38]
- [41] Byungchul Cha “Chebyshev’s bias in function fields” In *Compos. Math.*144.6, 2008, pp. 1351–1374 DOI: [10.1112/S0010437X08003631][39]
- [42] Byungchul Cha “The summatory function of the Möbius function in function fields” In *Acta Arith.*179.4, 2017, pp. 375–395 DOI: [10.4064/aa8590-1-2017][40]
- [43] Byungchul Cha and Seick Kim “Biases in the prime number race of function fields” In *J. Number Theory*130.4, 2010, pp. 1048–1055 DOI: [10.1016/j.jnt.2009.09.015][41]
- [44] Kuok Chao and Roger Plymen “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Int. J. Number Theory*6.3, 2010, pp. 681–690 DOI: [10.1142/S1793042110003125][42]
- [45] Sneha Chaubey, Melinda Lanius and Alexandru Zaharescu “Irrational factor races” In *Proc. Indian Acad. Sci. Math. Sci.*124.4, 2014, pp. 471–479 DOI: [10.1007/s12044-014-0198-z][43]
- [46] P. Chebyshev “Lettre de M. le professeur Tchébychev a M. Fuss, sur un nouveau théorème relatif aux nombres premiers contenus dans la formes 4 ​ n + 1 4n+1 et 4 ​ n + 3 4n+3 ” In *Bull. de la Classe phys. math. de l’Acad. Imp. des Sciences St. Petersburg*11, 1853, pp. 208
- [47] W… Chen “On the error term of the prime number theorem and the difference between the number of primes in the residue classes modulo 4 4 ” In *J. London Math. Soc. (2)*23.1, 1981, pp. 24–40 DOI: [10.1112/jlms/s2-23.1.24][44]
- [48] A.. Cohen and M… Mayhew “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Proc. London Math. Soc. (3)*18, 1968, pp. 691–713 DOI: [10.1112/plms/s3-18.4.691][45]
- [49] Harald Cramér “Ein Mittelwertsatz in der Primzahltheorie” In *Math. Z.*12.1, 1922, pp. 147–153 DOI: [10.1007/BF01482072][46]
- [50] S. Dancs and P. Turán “Investigations in the powersum theory. I” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*16, 1973, pp. 47–52 (1974)
- [51] Marc Deléglise, Pierre Dusart and Xavier-François Roblot “Counting primes in residue classes” In *Math. Comp.*73.247, 2004, pp. 1565–1575 DOI: [10.1090/S0025-5718-04-01649-7][47]
- [52] Lucile Devin “Chebyshev’s bias for analytic L-functions” In *Math. Proc. Cambridge Philos. Soc.*169.1, 2020, pp. 103–140 DOI: [10.1017/s0305004119000100][48]
- [53] Lucile Devin “Limiting properties of the distribution of primes in an arbitrarily large number of residue classes” In *Canad. Math. Bull.*63.4, 2020, pp. 837–849 DOI: [10.4153/s0008439520000089][49]
- [54] Lucile Devin “Discrepancies in the distribution of Gaussian primes”, 2021 URL: [https://arxiv.org/abs/2105.02492][50]
- [55] Lucile Devin and Xianchang Meng “Chebyshev’s bias for products of irreducible polynomials” In *Adv. Math.*392, 2021, pp. Paper No. 10804045 DOI: [10.1016/j.aim.2021.108040][51]
- [56] H.. Diamond “Two oscillation theorems” In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 113–118. Lecture Notes in Math.Vol. 251
- [57] H.. Diamond and J. Pintz “Oscillation of Mertens’ product formula” In *J. Théor. Nombres Bordeaux*21.3, 2009, pp. 523–533 URL: [http://jtnb.cedram.org/item?id=JTNB_2009__21_3_523_0][52]
- [58] Harold. Diamond “Changes of sign of π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Enseignement Math. (2)*21.1, 1975, pp. 1–14
- [59] D. Dummit, A. Granville and B. Kisilevsky “Big biases amongst products of two primes” In *Mathematika*62.2, 2016, pp. 502–507 DOI: [10.1112/S0025579315000339][53]
- [60] William Ellison and Fern Ellison “Prime numbers”, A Wiley-Interscience Publication John Wiley & Sons, Inc., New York; Hermann, Paris, 1985, pp. xii+417
- [61] William Ellison “Les nombres premiers” En collaboration avec Michel Mendès France; Publications de l’Institut de Mathématique de l’Université de Nancago, No. IX; Actualités Scientifiques et Industrielles, No. 1366 Hermann, Paris, 1975, pp. xiv+442
- [62] C… Evelyn and E.. Linfoot “On a problem in the additive theory of numbers” In *Ann. of Math. (2)*32.2, 1931, pp. 261–270 DOI: [10.2307/1968190][54]
- [63] A.. Fawaz “The explicit formula for L 0 ​ ( x) L_{0}(x) ” In *Proc. London Math. Soc. (3)*1, 1951, pp. 86–103 DOI: [10.1112/plms/s3-1.1.86][55]
- [64] A.. Fawaz “On an unsolved problem in the analytic theory of numbers” In *Quart. J. Math. Oxford Ser. (2)*3, 1952, pp. 282–295 DOI: [10.1093/qmath/3.1.282][56]
- [65] A. Feuerverger and G. Martin “Biases in the Shanks-Rényi prime number race” In *Experiment. Math.*9.4, 2000, pp. 535–570 URL: [http://projecteuclid.org/euclid.em/1045759521][57]
- [66] D. Fiorilli “Irrégularités dans la distribution des nombres premiers et des suites plus générales dans les progressions arithmétiques” Thesis (Ph.D.)–Université de Montréal ProQuest LLC, Ann Arbor, MI, 2011
- [67] D. Fiorilli “Elliptic curves of unbounded rank and Chebyshev’s bias” In *Int. Math. Res. Not. IMRN*, 2014, pp. 4997–5024 DOI: [10.1093/imrn/rnt103][58]
- [68] D. Fiorilli “Highly biased prime number races” In *Algebra Number Theory*8.7, 2014, pp. 1733–1767 DOI: [10.2140/ant.2014.8.1733][59]
- [69] D. Fiorilli “The distribution of the variance of primes in arithmetic progressions” In *Int. Math. Res. Not. IMRN*, 2015, pp. 4421–4448 DOI: [10.1093/imrn/rnu074][60]
- [70] D. Fiorilli and G. Martin “Inequities in the Shanks-Rényi prime number race: an asymptotic formula for the densities” In *J. Reine Angew. Math.*676, 2013, pp. 121–212
- [71] Daniel Fiorilli and Florent Jouve “Unconditional Chebyshev biases in number fields” In *J. Éc. polytech. Math.*9, 2022, pp. 671–679 DOI: [10.5802/jep.19][61]
- [72] Daniel Fiorilli and Florent Jouve “Distribution of Frobenius elements in families of Galois extensions” In *J. Inst. Math. Jussieu*23.3, 2024, pp. 1169–1258 DOI: [10.1017/S1474748023000154][62]
- [73] Daniel Fiorilli and Greg Martin “Disproving Hooley’s conjecture” In *J. Eur. Math. Soc. (JEMS)*25.12, 2023, pp. 4791–4812 DOI: [10.4171/jems/1291][63]
- [74] K. Ford and S. Konyagin “Chebyshev’s conjecture and the prime number race” In *IV International Conference “Modern Problems of Number Theory and its Applications”: Current Problems, Part II (Russian) (Tula, 2001)*Mosk. Gos. Univ. im. Lomonosova, Mekh.-Mat. Fak., Moscow, 2002, pp. 67–91
- [75] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line” In *Duke Math. J.*113.2, 2002, pp. 313–330 DOI: [10.1215/S0012-7094-02-11324-6][64]
- [76] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line. II” In *Proceedings of the Session in Analytic Number Theory and Diophantine Equations*360, Bonner Math. Schriften Univ. Bonn, Bonn, 2003, pp. 40
- [77] K. Ford, Y. Lamzouri and S. Konyagin “The prime number race and zeros of Dirichlet L L -functions off the critical line: Part III” In *Q. J. Math.*64.4, 2013, pp. 1091–1098 DOI: [10.1093/qmath/has021][65]
- [78] K. Ford and J. Sneed “Chebyshev’s bias for products of two primes” In *Experiment. Math.*19.4, 2010, pp. 385–398 DOI: [10.1080/10586458.2010.10390630][66]
- [79] Kevin Ford, Adam. Harper and Youness Lamzouri “Extreme biases in prime number races with many contestants” In *Math. Ann.*374.1-2, 2019, pp. 517–551 DOI: [10.1007/s00208-019-01810-x][67]
- [80] Kevin Ford and Richard. Hudson “Sign changes in π q, a ​ ( x) − π q, b ​ ( x) \pi_{q,a}(x)-\pi_{q,b}(x) ” In *Acta Arith.*100.4, 2001, pp. 297–314 DOI: [10.4064/aa100-4-1][68]
- [81] A. Fujii “Some generalizations of Chebyshev’s conjecture” In *Proc. Japan Acad. Ser. A Math. Sci.*64.7, 1988, pp. 260–263 URL: [http://projecteuclid.org/euclid.pja/1195513180][69]
- [82] Akio Fujii “An additive problem of prime numbers. III” In *Proc. Japan Acad. Ser. A Math. Sci.*67.8, 1991, pp. 278–283 URL: [http://projecteuclid.org/euclid.pja/1195511989][70]
- [83] P.. Gallagher “Some consequences of the Riemann hypothesis” In *Acta Arith.*37, 1980, pp. 339–343 DOI: [10.4064/aa-37-1-339-343][71]
- [84] Peng Gao and Liangyi Zhao “Lower bounds for negative moments of ζ ′ ​ ( ρ) \zeta^{\prime}(\rho) ” In *Mathematika*69.4, 2023, pp. 1081–1103
- [85] S. Gonek “The second moment of the reciprocal of the Riemann zeta function and its derivative”, 1999 URL: [https://www.slmath.org/workshops/101/schedules/25626][72]
- [86] S.. Gonek “On negative moments of the Riemann zeta-function” In *Mathematika*36.1, 1989, pp. 71–88 DOI: [10.1112/S0025579300013589][73]
- [87] I.. Good and R.. Churchhouse “The Riemann hypothesis and pseudorandom features of the Möbius sequence” In *Math. Comp.*22, 1968, pp. 857–861 DOI: [10.2307/2004584][74]
- [88] Ofir Gorodetsky “Sums of two squares are strongly biased towards quadratic residues” In *Algebra Number Theory*17.3, 2023, pp. 775–804 DOI: [10.2140/ant.2023.17.775][75]
- [89] A. Granville and G. Martin “Prime number races” In *Amer. Math. Monthly*113.1, 2006, pp. 1–33 DOI: [10.2307/27641834][76]
- [90] Emil Grosswald “On some generalizations of theorems by Landau and Pólya” In *Israel J. Math.*3, 1965, pp. 211–220 DOI: [10.1007/BF03008399][77]
- [91] Emil Grosswald “Oscillation theorems of arithmetical functions” In *Trans. Amer. Math. Soc.*126, 1967, pp. 1–28 DOI: [10.2307/1994409][78]
- [92] Emil Grosswald “Oscillation theorems” Lecture Notes in Math., Vol. 251 In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 141–168
- [93] M. Grześkowiak, J. Kaczorowski, Ł. Pańkowski and M. Radziejewski “On the sign changes of ψ ⁡ ( x) − x \psi(x)-x ”, 2024 URL: [https://arxiv.org/abs/2408.10399][79]
- [94] Hansraj Gupta “On a table of values of L ⁡ ( n) L(n) ” In *Proc. Indian Acad. Sci., Sect. A.*12, 1940, pp. 407–409
- [95] Alia Hamieh, Habiba Kadiri, Greg Martin and Nathan Ng “Comparative prime number theory problem list”, 2024 URL: [https://arxiv.org/abs/2407.03530][80]
- [96] G.. Hardy “On Dirichlet’s divisor problem” In *Proc. London Math. Soc. (2)*15, 1916, pp. 1–25 DOI: [10.1112/plms/s2-15.1.1][81]
- [97] G.. Hardy and J.. Littlewood “On an assertion of Tchebychef” In *Proc. London Math. Soc. (2)*14, 1915, pp. xv–xvi
- [98] G.. Hardy and J.. Littlewood “Contributions to the theory of the Riemann zeta-function and the theory of the distribution of primes” In *Acta Math.*41.1, 1916, pp. 119–196
- [99] Adam. Harper and Youness Lamzouri “Orderings of weakly correlated random variables, and prime number races with many contestants” In *Probab. Theory Related Fields*170.3-4, 2018, pp. 961–1010 DOI: [10.1007/s00440-017-0800-2][82]
- [100] C.. Haselgrove “A disproof of a conjecture of Pólya” In *Mathematika*5, 1958, pp. 141–145 DOI: [10.1112/S0025579300001480][83]
- [101] Shehzad Hathi and Ethan. Lee “Mertens’ third theorem for number fields: a new proof, Cramér’s inequality, oscillations, and bias”, 2022 URL: [https://arxiv.org/abs/2112.02166][84]
- [102] Mounir Hayani “On the influence of the Galois group structure on the Chebyshev bias in number fields”, 2024 URL: [https://arxiv.org/abs/2404.06804][85]
- [103] Winston Heap, Junxian Li and Jing Zhao “Lower bounds for discrete negative moments of the Riemann zeta function” In *Algebra Number Theory*16.7, 2022, pp. 1589–1625 DOI: [10.2140/ant.2022.16.1589][86]
- [104] D.. Heath-Brown “The distribution and moments of the error term in the Dirichlet divisor problem” In *Acta Arith.*60.4, 1992, pp. 389–415 DOI: [10.4064/aa-60-4-389-415][87]
- [105] Dennis. Hejhal “On the distribution of log ⁡ | ζ ′ ​ ( 1 2 + i ​ t) | \log|\zeta^{\prime}(\frac{1}{2}+it)| ” In *Number theory, trace formulas and discrete groups (Oslo, 1987)*Academic Press, Boston, MA, 1989, pp. 343–370
- [106] C. Hooley “On the Barban-Davenport-Halberstam theorem. VII” In *J. London Math. Soc. (2)*16.1, 1977, pp. 1–8 DOI: [10.1112/jlms/s2-16.1.1][88]
- [107] Patrick Hough “A lower bound for biases amongst products of two primes” In *Res. Number Theory*3, 2017, pp. Art. 1911 DOI: [10.1007/s40993-017-0083-9][89]
- [108] Daniel Hu, Ikuya Kaneko, Spencer Martin and Carl Schildkraut “On a Mertens-type conjecture for number fields”, 2023 URL: [https://arxiv.org/abs/2109.06665][90]
- [109] Richard. Hudson “A common combinatorial principle underlies Riemann’s formula, the Chebyshev phenomenon, and other subtle effects in comparative prime number theory. I” In *J. Reine Angew. Math.*313, 1980, pp. 133–150 DOI: [10.1515/crll.1980.313.133][91]
- [110] Richard. Hudson “Averaging effects on irregularities in the distribution of primes in arithmetic progressions” In *Math. Comp.*44.170, 1985, pp. 561–571 DOI: [10.2307/2007974][92]
- [111] Richard. Hudson and Carter Bays “The mean behavior of primes in arithmetic progressions” In *J. Reine Angew. Math.*296, 1977, pp. 80–99 DOI: [10.1515/crll.1977.296.80][93]
- [112] Peter Humphries “The distribution of weighted sums of the Liouville function and Pólya’s conjecture” In *J. Number Theory*133.2, 2013, pp. 545–582 DOI: [10.1016/j.jnt.2012.08.011][94]
- [113] Peter Humphries “On the Mertens conjecture for elliptic curves over finite fields” In *Bull. Aust. Math. Soc.*89.1, 2014, pp. 19–32 DOI: [10.1017/S0004972712001116][95]
- [114] Peter Humphries “On the Mertens conjecture for function fields” In *Int. J. Number Theory*10.2, 2014, pp. 341–361 DOI: [10.1142/S1793042113500978][96]
- [115] Peter Humphries, Snehal. Shekatkar and Tian Wong “Biases in prime factorizations and Liouville functions for arithmetic progressions” In *J. Théor. Nombres Bordeaux*31.1, 2019, pp. 1–25 URL: [http://jtnb.cedram.org/item?id=JTNB_2019__31_1_1_0][97]
- [116] Greg Hurst “Computations of the Mertens function and improved bounds on the Mertens conjecture” In *Math. Comp.*87.310, 2018, pp. 1013–1028 DOI: [10.1090/mcom/3275][98]
- [117] A.. Ingham “The distribution of prime numbers” Cambridge Tracts in Mathematics and Mathematical Physics. 30. London: Cambridge University Press, 1932
- [118] A.. Ingham “A note on the distribution of primes” In *Acta Arith.*1, 1936, pp. 201–211
- [119] A.. Ingham “On two conjectures in the theory of numbers” In *Amer. J. Math.*64, 1942, pp. 313–319 DOI: [10.2307/2371685][99]
- [120] A.. Ingham “The distribution of prime numbers”, Cambridge Tracts in Mathematics and Mathematical Physics, No. 30 Stechert-Hafner, Inc., New York, 1964, pp. v+114
- [121] B. Jessen and A. Wintner “Distribution functions and the Riemann zeta function” In *Trans. Amer. Math. Soc.*38.1, 1935, pp. 48–88 DOI: [10.2307/1989728][100]
- [122] Daniel. Johnston “On the average value of π ⁡ ( t) − li ⁡ ( t) \pi(t)-{\rm li}(t) ” In *Canad. Math. Bull.*66.1, 2023, pp. 185–195 DOI: [10.4153/S0008439522000212][101]
- [123] W. Jurkat and A. Peyerimhoff “A constructive approach to Kronecker approximations and its application to the Mertens conjecture” In *J. Reine Angew. Math.*286(287), 1976, pp. 322–340 DOI: [10.1515/crll.1976.286-287.322][102]
- [124] W.. Jurkat “On the Mertens conjecture and related general Ω \Omega -theorems” In *Analytic number theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972)*Amer. Math. Soc., Providence, R.I., 1973, pp. 147–158
- [125] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. I” In *Acta Arith.*44.4, 1984, pp. 365–377 DOI: [10.4064/aa-44-4-365-377][103]
- [126] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. II” In *Acta Arith.*45.1, 1985, pp. 65–74 DOI: [10.4064/aa-45-1-65-74][104]
- [127] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. III” In *Acta Arith.*48.4, 1987, pp. 347–371 DOI: [10.4064/aa-48-4-347-371][105]
- [128] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. IV” In *Acta Arith.*50.1, 1988, pp. 15–21 DOI: [10.4064/aa-50-1-15-21][106]
- [129] J. Kaczorowski “The k k -functions in multiplicative number theory. I. On complex explicit formulae” In *Acta Arith.*56.3, 1990, pp. 195–211 DOI: [10.4064/aa-56-3-195-211][107]
- [130] J. Kaczorowski “The k k -functions in multiplicative number theory. II. Uniform distribution of zeta zeros” In *Acta Arith.*56.3, 1990, pp. 213–224 DOI: [10.4064/aa-56-3-213-224][108]
- [131] J. Kaczorowski “The k k -functions in multiplicative number theory. III. Uniform distribution of zeta zeros; discrepancy” In *Acta Arith.*57.3, 1991, pp. 199–210 DOI: [10.4064/aa-57-3-199-210][109]
- [132] J. Kaczorowski “The k k -functions in multiplicative number theory. IV. On a method of A. E. Ingham” In *Acta Arith.*57.3, 1991, pp. 231–244 DOI: [10.4064/aa-57-3-231-244][110]
- [133] J. Kaczorowski “The k k -functions in multiplicative number theory. V. Changes of sign of some arithmetical error terms” In *Acta Arith.*59.1, 1991, pp. 37–58 DOI: [10.4064/aa-59-1-37-58][111]
- [134] J. Kaczorowski “A contribution to the Shanks-Rényi race problem” In *Quart. J. Math. Oxford Ser. (2)*44.176, 1993, pp. 451–458 DOI: [10.1093/qmath/44.4.451][112]
- [135] J. Kaczorowski “On the Shanks-Rényi race problem” In *Acta Arith.*74.1, 1996, pp. 31–46 DOI: [10.4064/aa-74-1-31-46][113]
- [136] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. I” In *Acta Math. Hungar.*48.1-2, 1986, pp. 173–185 DOI: [10.1007/BF01949062][114]
- [137] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. II” In *Acta Math. Hungar.*49.3-4, 1987, pp. 441–453 DOI: [10.1007/BF01951008][115]
- [138] J. Kaczorowski and W. Staś “On the number of sign changes in the remainder-term of the prime-ideal theorem” In *Colloq. Math.*56.1, 1988, pp. 185–197 DOI: [10.4064/cm-56-1-185-197][116]
- [139] Jerzy Kaczorowski “Results on the distribution of primes” In *J. Reine Angew. Math.*446, 1994, pp. 89–113 DOI: [10.1515/crll.1994.446.89][117]
- [140] Jerzy Kaczorowski “On the distribution of primes (mod 4 4)” In *Analysis*15.2, 1995, pp. 159–171 DOI: [10.1524/anly.1995.15.2.159][118]
- [141] Jerzy Kaczorowski “On the Shanks-Rényi race problem mod 5 5 ” In *J. Number Theory*50.1, 1995, pp. 106–118 DOI: [10.1006/jnth.1995.1006][119]
- [142] Jerzy Kaczorowski “Boundary values of Dirichlet series and the distribution of primes” In *European Congress of Mathematics, Vol. I (Budapest, 1996)*168, Progr. Math. Birkhäuser, Basel, 1998, pp. 237–254
- [143] Jerzy Kaczorowski “Results on the Möbius function” In *J. Lond. Math. Soc. (2)*75.2, 2007, pp. 509–521 DOI: [10.1112/jlms/jdm006][120]
- [144] Jerzy Kaczorowski “On the distribution of irreducible algebraic integers” In *Monatsh. Math.*156.1, 2009, pp. 47–71 DOI: [10.1007/s00605-008-0559-8][121]
- [145] Jerzy Kaczorowski “ Ω \Omega -estimates related to irreducible algebraic integers” In *Math. Nachr.*283.9, 2010, pp. 1291–1303 DOI: [10.1002/mana.200710158][122]
- [146] Jerzy Kaczorowski and Olivier Ramaré “Almost periodicity of some error terms in prime number theory” In *Acta Arith.*106.3, 2003, pp. 277–297 DOI: [10.4064/aa106-3-6][123]
- [147] Jerzy Kaczorowski and Włodzimierz Staś “On the number of sign-changes in the remainder-term of the prime-ideal theorem” In *Discuss. Math.*9, 1988, pp. 83–102 (1989)
- [148] Jerzy Kaczorowski and Kazimierz Wiertelak “ Ω \Omega -estimates for a class of arithmetic error terms” In *Math. Proc. Cambridge Philos. Soc.*142.3, 2007, pp. 385–394 DOI: [10.1017/S0305004107000035][124]
- [149] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of a given size of some arithmetic error terms” In *Trans. Amer. Math. Soc.*361.9, 2009, pp. 5023–5039 DOI: [10.1090/S0002-9947-09-04803-X][125]
- [150] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of the remainder term related to the Euler totient function” In *J. Number Theory*130.12, 2010, pp. 2683–2700 DOI: [10.1016/j.jnt.2010.06.010][126]
- [151] Jerzy Kaczorowski and Kazimierz Wiertelak “Smoothing arithmetic error terms: the case of the Euler ϕ \phi function” In *Math. Nachr.*283.11, 2010, pp. 1637–1645 DOI: [10.1002/mana.200810048][127]
- [152] Ikuya Kaneko and Shin-ya Koyama “A new aspect of Chebyshev’s bias for elliptic curves over function fields” In *Proc. Amer. Math. Soc.*151.12, 2023, pp. 5059–5068 DOI: [10.1090/proc/16461][128]
- [153] Ikuya Kaneko, Shin-ya Koyama and Nobushige Kurokawa “Towards the Deep Riemann Hypothesis for GL n \mathrm{GL}_{n} ”, 2023 URL: [https://arxiv.org/abs/2206.02612][129]
- [154] A.. Karatsuba “Behavior of the function R 1 ​ ( x) R_{1}(x) and of its mean value” In *Dokl. Akad. Nauk*404.4, 2005, pp. 439–442
- [155] A.. Karatsuba “On the approximation of π ⁡ ( x) \pi(x) ” In *Chebyshevskii Sb.*5.4(12), 2005, pp. 5–20
- [156] A.. Karatsuba “On the number of sign changes of the function R 1 ​ ( x) R_{1}(x) and its mean values” In *Chebyshevskii Sb.*6.2(14), 2005, pp. 163–183
- [157] I. Kátai “Eine Bemerkung zur “Comparative prime-number theory I-VIII” von S. Knapowski und P. Turán” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*7, 1964, pp. 33–40
- [158] I. Kátai “Comparative theory of prime numbers” In *Acta Math. Acad. Sci. Hungar*18, 1967, pp. 133–149 DOI: [10.1007/BF02020967][130]
- [159] I. Kátai “On investigations in the comparative prime number theory” In *Acta Math. Acad. Sci. Hungar.*18, 1967, pp. 379–391 DOI: [10.1007/BF02280297][131]
- [160] I. Kátai “On oscillations of number-theoretic functions” In *Acta Arith.*13, 1967/1968, pp. 107–122 DOI: [10.4064/aa-13-1-107-122][132]
- [161] I. Kátai “On oscillation of the number of primes in an arithmetical progression.” In *Acta Sci. Math. (Szeged)*29, 1968, pp. 271–282
- [162] Imre Kátai “The Ω \Omega -estimation of the arithmetic mean of the Möbius function” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*15, 1965, pp. 15–18
- [163] Imre Kátai “Omega-type investigations in prime number theory” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*16, 1966, pp. 369–396
- [164] Jaeyoon Kim “Prime running functions” In *Exp. Math.*31.4, 2022, pp. 1291–1313 DOI: [10.1080/10586458.2020.1786863][133]
- [165] H. Kisilevsky and M.. Rubinstein “Chebotarev sets” In *Acta Arith.*171.2, 2015, pp. 97–124 DOI: [10.4064/aa171-2-1][134]
- [166] S. Knapowski “On prime numbers in an arithmetical progression” In *Acta Arith.*4, 1958, pp. 57–70 DOI: [10.4064/aa-4-1-57-70][135]
- [167] S. Knapowski “On the Möbius function” In *Acta Arith.*4, 1958, pp. 209–216 DOI: [10.4064/aa-4-3-209-216][136]
- [168] S. Knapowski “On the mean values of certain functions in prime number theory” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 375–390. (unbound insert)
- [169] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. I” In *Acta Arith.*6, 1960/1961, pp. 415–434 DOI: [10.4064/aa-6-4-415-434][137]
- [170] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. II” In *Acta Arith*7, 1961/1962, pp. 325–335 DOI: [10.4064/aa-7-4-325-335][138]
- [171] S. Knapowski “Mean-value estimations for the Möbius function. I” In *Acta Arith.*7, 1961, pp. 121–130 DOI: [10.4064/aa-7-2-121-130][139]
- [172] S. Knapowski “Mean-value estimations for the Möbius function. II” In *Acta Arith.*7, 1961, pp. 337–343 DOI: [10.4064/aa-7-4-337-343][140]
- [173] S. Knapowski “On sign-changes in the remainder-term in the prime-number formula” In *J. London Math. Soc.*36, 1961, pp. 451–460 DOI: [10.1112/jlms/s1-36.1.451][141]
- [174] S. Knapowski “On sign-changes of the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x ” In *Acta Arith.*7, 1961/1962, pp. 107–119 DOI: [10.4064/aa-7-2-107-119][142]
- [175] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. III” In *Acta Arith*8, 1962/1963, pp. 97–105 DOI: [10.4064/aa-8-1-97-105][143]
- [176] S. Knapowski “On oscillations of certain means formed from the Möbius series. I” In *Acta Arith.*8, 1962/1963, pp. 311–320 DOI: [10.4064/aa-8-3-311-320][144]
- [177] S. Knapowski “On oscillations of certain means formed from the Möbius series. II” In *Acta Arith.*10, 1964, pp. 377–386 DOI: [10.4064/aa-10-4-377-386][145]
- [178] S. Knapowski and W. Staś “A note on a theorem of Hardy and Littlewood” In *Acta Arith.*7, 1961/1962, pp. 161–166 DOI: [10.4064/aa-7-2-161-166][146]
- [179] S. Knapowski and P. Turán “Comparative prime-number theory. I. Introduction” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 299–314 DOI: [10.1007/BF02020796][147]
- [180] S. Knapowski and P. Turán “Comparative prime-number theory. II. Comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k, l ≢ 1 {\rm mod}\ k,\,l\not\equiv 1 mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 315–342 DOI: [10.1007/BF02020797][148]
- [181] S. Knapowski and P. Turán “Comparative prime-number theory. III. Continuation of the study of comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 343–364 DOI: [10.1007/BF02020798][149]
- [182] S. Knapowski and P. Turán “Comparative prime-number theory. IV. Paradigma to the general case, k = 8 k=8 and 5 5 ” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 31–42 DOI: [10.1007/BF01901928][150]
- [183] S. Knapowski and P. Turán “Comparative prime-number theory. V. Some theorems concerning the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 43–63 DOI: [10.1007/BF01901929][151]
- [184] S. Knapowski and P. Turán “Comparative prime-number theory. VI. Continuation of the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 65–78 DOI: [10.1007/BF01901930][152]
- [185] S. Knapowski and P. Turán “Comparative prime-number theory. VII. The problem of sign-changes in the general case” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 241–250 DOI: [10.1007/BF01895712][153]
- [186] S. Knapowski and P. Turán “Comparative prime-number theory. VIII. Chebyshev’s problem for k = 8 k=8 ” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 251–268 DOI: [10.1007/BF01895713][154]
- [187] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. I” In *Acta Arith.*9, 1964, pp. 23–40 DOI: [10.4064/aa-9-1-23-40][155]
- [188] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. II. A modification of Chebyshev’s assertion” In *Acta Arith.*10, 1964, pp. 293–313 DOI: [10.4064/aa-10-3-293-313][156]
- [189] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. III” In *Acta Arith.*11, 1965, pp. 115–127 DOI: [10.4064/aa-11-1-115-127][157]
- [190] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. IV” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 147–161 DOI: [10.4064/aa-11-2-193-202][158]
- [191] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. V” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 193–202 DOI: [10.4064/aa-11-2-193-202][158]
- [192] S. Knapowski and P. Turán “On an assertion of Čebyšev” In *J. Analyse Math.*14, 1965, pp. 267–274 DOI: [10.1007/BF02806393][159]
- [193] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. VI. Accumulation theorems for residue-classes representing quadratic residues mod ​ k {\rm mod}\,k ” In *Acta Arith.*12, 1966, pp. 85–96 DOI: [10.4064/aa-12-1-85-96][160]
- [194] S. Knapowski and P. Turán “Über einige Fragen der vergleichenden Primzahltheorie” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 157–171
- [195] S. Knapowski and P. Turán “Further developments in the comparative prime number theory. VII” In *Acta Arith.*21, 1972, pp. 193–201 DOI: [10.4064/aa-21-1-193-201][161]
- [196] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). I” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 153–169. Colloq. Math. Soc. János BolyaiVol. 13
- [197] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” In *Monatsh. Math.*82.2, 1976, pp. 163–175 DOI: [10.1007/BF01305997][162]
- [198] S. Knapowski and P. Turán “On prime numbers ≡ 1 \equiv 1 resp. 3 ​ (mod 4) 3{\text{\rm\ (mod~$4$)}} ” In *Number theory and algebra*Academic Press, New York, 1977, pp. 157–165
- [199] G. Kolesnik and E.. Straus “On the sum of powers of complex numbers” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 427–442
- [200] Tadej Kotnik “The prime-counting function and its analytic approximations: π ⁡ ( x) \pi(x) and its approximations” In *Adv. Comput. Math.*29.1, 2008, pp. 55–70 DOI: [10.1007/s10444-007-9039-2][163]
- [201] Tadej Kotnik and Jan van Lune “On the order of the Mertens function” In *Experiment. Math.*13.4, 2004, pp. 473–481
- [202] Tadej Kotnik and Herman te Riele “The Mertens conjecture revisited” In *Algorithmic number theory*4076, Lecture Notes in Comput. Sci. Springer, Berlin, 2006, pp. 156–167
- [203] Emmanuel Kowalski “The large sieve, monodromy, and zeta functions of algebraic curves. II. Independence of the zeros” In *Int. Math. Res. Not. IMRN*, 2008, pp. Art. ID rnn 09157
- [204] Shin-ya Koyama and Nobushige Kurokawa “Chebyshev’s bias for Ramanujan’s τ \tau -function via the deep Riemann hypothesis” In *Proc. Japan Acad. Ser. A Math. Sci.*98.6, 2022, pp. 35–39 DOI: [10.3792/pjaa.98.007][164]
- [205] Matthias Kunik and Lutz. Lucht “Power series with the von Mangoldt function” In *Funct. Approx. Comment. Math.*47.part 1, 2012, pp. 15–33 DOI: [10.7169/facm/2012.47.1.2][165]
- [206] Y. Lamzouri “Large deviations of the limiting distribution in the Shanks–Rényi prime number race” In *Math. Proc. Cambridge Philos. Soc.*153.1, 2012, pp. 147–166 DOI: [10.1017/S030500411200014X][166]
- [207] Y. Lamzouri “The Shanks-Rényi prime number race with many contestants” In *Math. Res. Lett.*19.3, 2012, pp. 649–666 DOI: [10.4310/MRL.2012.v19.n3.a11][167]
- [208] Y. Lamzouri “Prime number races with three or more competitors” In *Math. Ann.*356.3, 2013, pp. 1117–1162 DOI: [10.1007/s00208-012-0874-1][168]
- [209] Y. Lamzouri “A bias in Mertens’ product formula” In *Int. J. Number Theory*12.1, 2016, pp. 97–109 DOI: [10.1142/S1793042116500068][169]
- [210] Youness Lamzouri and Bruno Martin “On the race between primes with an odd versus an even sum of the last k k binary digits” In *Funct. Approx. Comment. Math.*61.1, 2019, pp. 7–25 DOI: [10.7169/facm/1687][170]
- [211] E. Landau “Über einen Satz von Tschebyschef” In *Math. Ann.*61.4, 1906, pp. 527–550 DOI: [10.1007/BF01449495][171]
- [212] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” Leipzig und Berlin, B. G. Teubner, 1909, pp. xviii+pp. 1–564ix+pp. 565–961
- [213] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 1–24 DOI: [10.1007/BF01203613][172]
- [214] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 213–219 DOI: [10.1007/BF01203613][172]
- [215] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” 2d ed; With an appendix by Paul T. Bateman Chelsea Publishing Co., New York, 1953, pp. xviii+pp. 1–564ix+pp. 565–1001
- [216] Yuk-Kam Lau “On the existence of limiting distributions of some number-theoretic error terms” In *J. Number Theory*94.2, 2002, pp. 359–374 DOI: [10.1006/jnth.2001.2734][173]
- [217] J. Lay “Sign changes in Mertens’ first and second theorems”, 2015 URL: [https://arxiv.org/abs/1505.03589][174]
- [218] P. Leboeuf “Prime correlations and fluctuations” In *Ann. Henri Poincaré*4.suppl. 2, 2003, pp. S727–S752 DOI: [10.1007/s00023-003-0958-2][175]
- [219] J. Leech “Note on the distribution of prime numbers” In *J. London Math. Soc.*32, 1957, pp. 56–58 DOI: [10.1112/jlms/s1-32.1.56][176]
- [220] R.. Lehman “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Acta Arith.*11, 1966, pp. 397–410 DOI: [10.4064/aa-11-4-397-410][177]
- [221] R. Lehman “On Liouville’s function” In *Math. Comp.*14, 1960, pp. 311–320 DOI: [10.2307/2003890][178]
- [222] D.. Lehmer and S. Selberg “A sum involving the function of Möbius” In *Acta Arith.*6, 1960, pp. 111–114 DOI: [10.4064/aa-6-1-111-114][179]
- [223] R.. Lemke and K. Soundararajan “Unexpected biases in the distribution of consecutive primes” In *Proc. Natl. Acad. Sci. USA*113.31, 2016, pp. E4446–E4454 DOI: [10.1073/pnas.1605366113][180]
- [224] Robert. Lemke and Kannan Soundararajan “The distribution of consecutive prime biases and sums of sawtooth random variables” In *Math. Proc. Cambridge Philos. Soc.*168.1, 2020, pp. 149–169 DOI: [10.1017/s0305004118000592][181]
- [225] N. Levinson “On the number of sign changes of π ⁡ ( x) − li x \pi(x)-\mathop{\rm li}x ” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 171–177. Colloq. Math. Soc. János BolyaiVol. 13
- [226] J.. Lichtman, G. Martin and C. Pomerance “Primes in prime number races” In *Proc. Amer. Math. Soc.*147.9, 2019, pp. 3743–3757
- [227] Jiawei Lin and Greg Martin “Densities in certain three-way prime number races” In *Canad. J. Math.*74.1, 2022, pp. 232–265 DOI: [10.4153/S0008414X20000747][182]
- [228] J.. Littlewood “Sur la distribution des nombres premiers” In *Comptes Rendus de l’Acad. Sci. Paris*158, 1914, pp. 1869–1872
- [229] J.. Littlewood “Mathematical Notes: 3; on a Theorem Concerning the Distribution of Prime Numbers” In *J. London Math. Soc.*2.1, 1927, pp. 41–45 DOI: [10.1112/jlms/s1-2.1.41][183]
- [230] J.. Littlewood “Mathematical Notes (12): An Inequality for a Sum of Cosines” In *J. London Math. Soc.*12.3, 1937, pp. 217–221 DOI: [10.1112/jlms/s1-12.2.217][184]
- [231] Kamalakshya Mahatab and Anirban Mukhopadhyay “Measure-theoretic aspects of oscillations of error terms” In *Acta Arith.*187.3, 2019, pp. 201–217 DOI: [10.4064/aa170126-23-4][185]
- [232] E. Makai “On a minimum problem. II” In *Acta Math. Acad. Sci. Hungar.*15, 1964, pp. 63–66 DOI: [10.1007/BF01897022][186]
- [233] G. Martin “Asymmetries in the Shanks-Rényi prime number race” In *Number theory for the millennium, II (Urbana, IL, 2000)*A K Peters, Natick, MA, 2002, pp. 403–415
- [234] Greg Martin, Michael Mossinghoff and Timothy Trudgian “Fake mu’s” In *Proc. Amer. Math. Soc.*151.8, 2023, pp. 3229–3244 DOI: [10.1090/proc/16186][187]
- [235] Greg Martin and Nathan Ng “Inclusive prime number races” In *Trans. Amer. Math. Soc.*373.5, 2020, pp. 3561–3607 DOI: [10.1090/tran/7996][188]
- [236] Barry Mazur “Finding meaning in error terms” In *Bull. Amer. Math. Soc. (N.S.)*45.2, 2008, pp. 185–228 DOI: [10.1090/S0273-0979-08-01207-X][189]
- [237] X. Meng “The distribution of k k -free numbers and the derivative of the Riemann zeta-function” In *Math. Proc. Cambridge Philos. Soc.*162.2, 2017, pp. 293–317 DOI: [10.1017/S0305004116000554][190]
- [238] X. Meng “Chebyshev’s bias for products of k k primes” In *Algebra Number Theory*12.2, 2018, pp. 305–341 DOI: [10.2140/ant.2018.12.305][191]
- [239] X. Meng “Large bias for integers with prime factors in arithmetic progressions” In *Mathematika*64.1, 2018, pp. 237–252
- [240] Xianchang Meng “Number of prime factors over arithmetic progressions” In *Q. J. Math.*71.1, 2020, pp. 97–121 DOI: [10.1093/qmathj/haz040][192]
- [241] F. Mertens “Über eine zahlentheoretische Funktion” In *Sitzungsberichte Akad. Wien*106, 1897, pp. 761–830
- [242] Micah. Milinovich and Nathan Ng “A note on a conjecture of Gonek” In *Funct. Approx. Comment. Math.*46, 2012, pp. 177–187 DOI: [10.7169/facm/2012.46.2.3][193]
- [243] William Monach “Numerical Investigation of Several Problems in Number Theory” Thesis (Ph.D.)–University of Michigan) ProQuest LLC, Ann Arbor, MI, 1980 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:8106192][194]
- [244] H.. Montgomery “The zeta function and prime numbers” In *Proceedings of the Queen’s Number Theory Conference, 1979 (Kingston, Ont., 1979)*54, Queen’s Papers in Pure and Appl. Math. Queen’s Univ., Kingston, Ont., 1980, pp. 1–31
- [245] Hugh. Montgomery “Ten lectures on the interface between analytic number theory and harmonic analysis” 84, CBMS Regional Conference Series in Mathematics Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1994, pp. xiv+220 DOI: [10.1090/cbms/084][195]
- [246] Hugh. Montgomery and Ulrike.. Vorhauer “Changes of sign of the error term in the prime number theorem” In *Funct. Approx. Comment. Math.*35, 2006, pp. 235–247 DOI: [10.7169/facm/1229442626][196]
- [247] Pieter Moree “Chebyshev’s bias for composite numbers with restricted prime divisors” In *Math. Comp.*73.245, 2004, pp. 425–449 DOI: [10.1090/S0025-5718-03-01536-9][197]
- [248] Thomas Morrill, Dave Platt and Tim Trudgian “Sign changes in the prime number theorem” In *Ramanujan J.*57.1, 2022, pp. 165–173 DOI: [10.1007/s11139-021-00398-8][198]
- [249] Michael. Mossinghoff, Tomás Oliveira and Timothy. Trudgian “The distribution of k k -free numbers” In *Math. Comp.*90.328, 2021, pp. 907–929 DOI: [10.1090/mcom/3581][199]
- [250] Michael. Mossinghoff and Timothy. Trudgian “Between the problems of Pólya and Turán” In *J. Aust. Math. Soc.*93.1–2, 2012, pp. 157–171 DOI: [10.1017/S1446788712000201][200]
- [251] Michael. Mossinghoff and Timothy. Trudgian “The Liouville function and the Riemann hypothesis” In *Exploring the Riemann zeta function*Springer, Cham, 2017, pp. 201–221
- [252] Michael. Mossinghoff and Timothy. Trudgian “A tale of two omegas” In *75 years of mathematics of computation*754, Contemp. Math. Amer. Math. Soc., [Providence], RI, 2020, pp. 343–364
- [253] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in weighted arithmetic sums” In *Int. J. Number Theory*17.7, 2021, pp. 1697–1716 DOI: [10.1142/S1793042121500561][201]
- [254] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in the Goldbach conjecture” In *J. Théor. Nombres Bordeaux*34.1, 2022, pp. 295–307 DOI: [10.5802/jtnb.120][202]
- [255] Yo̵ichi Motohashi “The binary additive divisor problem” In *Ann. Sci. École Norm. Sup. (4)*27.5, 1994, pp. 529–572 URL: [http://www.numdam.org/item?id=ASENS_1994_4_27_5_529_0][203]
- [256] C. Myerscough “Application of an accurate remainder term in the calculation of residue class distributions”, 2013 URL: [https://arxiv.org/abs/1301.1434][204]
- [257] Władysław Narkiewicz “The development of prime number theory”, Springer Monographs in Mathematics Springer-Verlag, Berlin, 2000, pp. xii+448 DOI: [10.1007/978-3-662-13157-2][205]
- [258] Gerhard Neubauer “Eine empirische Untersuchung zur Mertensschen Funktion” In *Numer. Math.*5, 1963, pp. 1–13 DOI: [10.1007/BF01385874][206]
- [259] N. Ng “Limiting Distributions and Zeros of Artin L L -Functions” Thesis (Ph.D.)–University of British Columbia, 2000 URL: [http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf][207]
- [260] N. Ng “The distribution of the summatory function of the Möbius function” In *Proc. London Math. Soc. (3)*89.2, 2004, pp. 361–389 DOI: [10.1112/S0024611504014741][208]
- [261] A.. Odlyzko and H… te Riele “Disproof of the Mertens conjecture” In *J. Reine Angew. Math.*357, 1985, pp. 138–160 DOI: [10.1515/crll.1985.357.138][209]
- [262] O.. Petrushov “Asymptotic estimates of functions based on the behavior of their Laplace transforms near singular points” In *Math. Notes*93.5–6, 2013, pp. 906–916 DOI: [10.1134/S0001434613050283][210]
- [263] P. Phragmén “Sur le logarithme intégral et la fonction f ⁡ ( x) f(x) de Riemann” In *Öfversigt af Kongl. Vetenskaps–Akademiens Föhandlingar.*48, 1891, pp. 599–616
- [264] A. Piltz “Über die Häufigkeit der Primzahlen in arithmetischen Progressionen und über verwandte Gesetze” In *Habilitationsschrift, Friedrich–Schiller–Universität Jena*, 1884
- [265] J. Pintz “Bemerkungen zur Arbeit: “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” (Monatsh. Math. 82 (1976), no. 2, 163–175) von S. Knapowski und P. Turán” In *Monatsh. Math.*82.3, 1976, pp. 199–206 DOI: [10.1007/BF01526326][211]
- [266] J. Pintz “On the remainder term of the prime number formula. III. Sign changes of π ⁡ ( x) − li ​ x \pi(x)-{\rm li}x ” In *Studia Sci. Math. Hungar.*12.3-4, 1977, pp. 345–369 (1980)
- [267] J. Pintz “On the sign changes of π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}(x) ” In *Journées Arithmétiques de Caen (Univ. Caen, Caen, 1976)*Soc. Math. France, Paris, 1977, pp. 255–265. Astérisque No. 41–42
- [268] J. Pintz “On the remainder term of the prime number formula. IV. Sign changes of π ⁡ ( x) − li x \pi(x)-{\mathop{\rm li}}x ” In *Studia Sci. Math. Hungar.*13.1-2, 1978, pp. 29–42 (1981)
- [269] J. Pintz “On the remainder term of the prime number formula. I. On a problem of Littlewood” In *Acta Arith.*36.4, 1980, pp. 341–365 DOI: [10.4064/aa-36-4-341-365][212]
- [270] J. Pintz “On the remainder term of the prime number formula. II. On a theorem of Ingham” In *Acta Arith.*37, 1980, pp. 209–220 DOI: [10.4064/aa-37-1-209-220][213]
- [271] J. Pintz “On the remainder term of the prime number formula. V. Effective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 215–223
- [272] J. Pintz “On the remainder term of the prime number formula. VI. Ineffective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 225–230
- [273] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). II” In *Studia Sci. Math. Hungar.*15.4, 1980, pp. 491–496
- [274] J. Pintz “On the sign changes of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n) ” In *Analysis*1.3, 1981, pp. 191–195 DOI: [10.1524/anly.1981.1.3.191][214]
- [275] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). I” In *Acta Arith.*42.1, 1982, pp. 49–55 DOI: [10.4064/aa-42-1-49-55][215]
- [276] J. Pintz “On the distribution of square-free numbers” In *J. London Math. Soc. (2)*28.3, 1983, pp. 401–405 DOI: [10.1112/jlms/s2-28.3.401][216]
- [277] J. Pintz “Oscillatory properties of the remainder term of the prime number formula” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 551–560
- [278] J. Pintz “On the partial sums of the Möbius function” In *Topics in classical number theory, Vol. I, II (Budapest, 1981)*34, Colloq. Math. Soc. János Bolyai North-Holland, Amsterdam, 1984, pp. 1229–1250
- [279] J. Pintz “On the remainder term of the prime number formula and the zeros of Riemann’s zeta-function” In *Number theory, Noordwijkerhout 1983 (Noordwijkerhout, 1983)*1068, Lecture Notes in Math. Springer, Berlin, 1984, pp. 186–197
- [280] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). III” In *Acta Arith.*43.2, 1984, pp. 105–113 DOI: [10.4064/aa-43-2-105-113][217]
- [281] J. Pintz “An effective disproof of the Mertens conjecture” In *Astérisque*, 1987, pp. 325–333346
- [282] J. Pintz “On an assertion of Riemann concerning the distribution of prime numbers” In *Acta Math. Hungar.*58.3-4, 1991, pp. 383–387 DOI: [10.1007/BF01903967][218]
- [283] J. Pintz and S. Salerno “Irregularities in the distribution of primes in arithmetic progressions. II” In *Arch. Math. (Basel)*43.4, 1984, pp. 351–357 DOI: [10.1007/BF01196659][219]
- [284] J. Pintz and S. Salerno “On the comparative theory of primes” In *Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4)*11.2, 1984, pp. 245–260 URL: [http://www.numdam.org/item?id=ASNSP_1984_4_11_2_245_0][220]
- [285] J. Pintz and S. Salerno “Accumulation theorems for primes in arithmetic progressions” In *Acta Math. Hungar.*46.1-2, 1985, pp. 151–172 DOI: [10.1007/BF01961016][221]
- [286] J. Pintz and S. Salerno “Some consequences of the general Riemann hypothesis in the comparative theory of primes” In *J. Number Theory*23.2, 1986, pp. 183–194 DOI: [10.1016/0022-314X(86)90088-0][222]
- [287] János Pintz and Saverio Salerno “Irregularities in the distribution of primes in arithmetic progressions. I” In *Arch. Math. (Basel)*42.5, 1984, pp. 439–447 DOI: [10.1007/BF01190694][223]
- [288] D.. Platt and T.. Trudgian “On the first sign change of θ ⁡ ( x) − x \theta(x)-x ” In *Math. Comp.*85.299, 2016, pp. 1539–1547 DOI: [10.1090/mcom/3021][224]
- [289] Dave Platt and Tim Trudgian “Fujii’s development on Chebyshev’s conjecture” In *Int. J. Number Theory*15.3, 2019, pp. 639–644 DOI: [10.1142/S1793042119500337][225]
- [290] Roger Plymen “The Great Prime Number Race” 92, Student Mathematical Library American Mathematical Society, Providence, RI, 2020, pp. 138
- [291] G. Pólya “Verschiedene Bemerkungen zur Zahlentheorie” In *Jahresbericht der deutschen Math.–Vereinigung*28, 1919, pp. 31–40
- [292] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahltheorie” In *Gött. Nachr.*, 1930, pp. 19–27
- [293] G. Pólya “On polar singularities of power series and of Dirichlet series” In *Proc. London Math. Soc. (2)*33.2, 1931, pp. 85–101 DOI: [10.1112/plms/s2-33.1.85][226]
- [294] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahlsatz” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 233–244
- [295] Sam Porritt “Character sums over products of prime polynomials”, 2020 URL: [https://arxiv.org/abs/2003.12002][227]
- [296] Karl Prachar “Primzahlverteilung” Springer-Verlag, Berlin-Göttingen-Heidelberg, 1957, pp. x+415 pp.
- [297] J.-C. Puchta “On large oscillations of the remainder of the prime number theorems” In *Acta Math. Hungar.*87.3, 2000, pp. 213–227
- [298] Maciej Radziejewski “On the distribution of algebraic numbers with prescribed factorization properties” In *Acta Arith.*116.2, 2005, pp. 153–171 DOI: [10.4064/aa116-2-4][228]
- [299] Maciej Radziejewski “Oscillations of error terms associated with certain arithmetical functions” In *Monatsh. Math.*144.2, 2005, pp. 113–130 DOI: [10.1007/s00605-003-0147-x][229]
- [300] Maciej Radziejewski “Oscillatory properties of real functions with weakly bounded Mellin transform” In *Q. J. Math.*65.1, 2014, pp. 249–266 DOI: [10.1093/qmath/has036][230]
- [301] H… te Riele “Computations concerning the conjecture of Mertens” In *J. Reine Angew. Math.*311(312), 1979, pp. 356–360 DOI: [10.1515/crll.1979.311-312.356][231]
- [302] Herman.. te Riele “On the sign of the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Math. Comp.*48.177, 1987, pp. 323–328 DOI: [10.2307/2007893][232]
- [303] Herman.. te Riele “The Mertens conjecture” In *The legacy of Bernhard Riemann after one hundred and fifty years. Vol. II*35.2, Adv. Lect. Math. (ALM) Int. Press, Somerville, MA, 2016, pp. 703–718
- [304] G. Robin “Sur l’ordre maximum de la fonction somme des diviseurs” In *Seminar on number theory, Paris 1981–82 (Paris, 1981/1982)*38, Progr. Math. Birkhäuser Boston, Boston, MA, 1983, pp. 233–244
- [305] Guy Robin “Irrégularités dans la distribution des nombres premiers dans les progressions arithmétiques” In *Ann. Fac. Sci. Toulouse Math. (5)*8.2, 1986, pp. 159–173 URL: [http://www.numdam.org/item?id=AFST_1986-1987_5_8_2_159_0][233]
- [306] J. Rosser and Lowell Schoenfeld “Approximate formulas for some functions of prime numbers” In *Illinois J. Math.*6, 1962, pp. 64–94
- [307] M. Rubinstein and P. Sarnak “Chebyshev’s bias” In *Experiment. Math.*3.3, 1994, pp. 173–197 URL: [http://projecteuclid.org/euclid.em/1048515870][234]
- [308] Imre. Ruzsa “Consecutive primes modulo 4” In *Indag. Math. (N.S.)*12.4, 2001, pp. 489–503 DOI: [10.1016/S0019-3577(01)80038-0][235]
- [309] J.. Ryan “One more “many-more” assertion” In *Amer. Math. Monthly*74.1, 1967, pp. 19–24 DOI: [10.2307/2314046][236]
- [310] Bahman Saffari “Sur la fausseté de la conjecture de Mertens. (With discussion.)” In *C. R. Acad. Sci. Paris Sér. A-B*271, 1970, pp. A1097–A1101
- [311] A. Sankaranarayanan “On the sign changes in the remainder term of an asymptotic formula for the number of squarefree numbers” In *Arch. Math. (Basel)*60.1, 1993, pp. 51–57 DOI: [10.1007/BF01194239][237]
- [312] Yannick Saouter and Patrick Demichel “A sharp region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*79.272, 2010, pp. 2395–2405 DOI: [10.1090/S0025-5718-10-02351-3][238]
- [313] Yannick Saouter and Herman te Riele “Improved results on the Mertens conjecture” In *Math. Comp.*83.285, 2014, pp. 421–433 DOI: [10.1090/S0025-5718-2013-02716-0][239]
- [314] Yannick Saouter, Timothy Trudgian and Patrick Demichel “A still sharper region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*84.295, 2015, pp. 2433–2446 DOI: [10.1090/S0025-5718-2015-02930-5][240]
- [315] P. Sarnak “Letter to Barry Mazur on ‘Chebyshev’s bias’ for τ ⁡ ( p) \tau(p) ”, 2007 URL: [http://web.math.princeton.edu/sarnak/MazurLtrMay08.PDF][241]
- [316] J.-C. Schlage–Puchta “Sign changes of π ⁡ ( x, q, 1) − π ⁡ ( x, q, a) \pi(x,q,1)-\pi(x,q,a) ” In *Acta Math. Hungar.*102.4, 2004, pp. 305–320 DOI: [10.1023/B:AMHU.0000024681.23784.d1][242]
- [317] J.-C. Schlage–Puchta “Oscillations of the error term in the prime number theorem” In *Acta Math. Hungar.*156.2, 2018, pp. 303–308 DOI: [10.1007/s10474-018-0884-x][243]
- [318] Erhard Schmidt “Über die Anzahl der Primzahlen unter gegebener Grenze” In *Math. Ann.*57.2, 1903, pp. 195–204 DOI: [10.1007/BF01444344][244]
- [319] Youssef Sedrati “Inequities in the Shanks–Renyi prime number race over function fields” In *Mathematika*68.3, 2022, pp. 840–895 DOI: [10.1112/mtk.12150][245]
- [320] D. Shanks “Quadratic residues and the distribution of primes” In *Math. Tables Aids Comput.*13, 1959, pp. 272–284
- [321] Daniel Shanks and Mohan Lal “Bateman’s constants reconsidered and the distribution of cubic residues” In *Math. Comp.*26, 1972, pp. 265–285 DOI: [10.2307/2004737][246]
- [322] A. Shchebetov “Chebyshev’s bias visualizer”, 2021 URL: [http://math101.guru/en/downloads-2/repository/][247]
- [323] Arshay Sheth “Euler products at the centre and applications to Chebyshev’s bias”, 2024 URL: [https://arxiv.org/abs/2405.01512][248]
- [324] S. Skewes “On the Difference π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}\,(x) (I)” In *J. London Math. Soc.*8.4, 1933, pp. 277–283 DOI: [10.1112/jlms/s1-8.4.277][249]
- [325] S. Skewes “On the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x. II” In *Proc. London Math. Soc. (3)*5, 1955, pp. 48–70 DOI: [10.1112/plms/s3-5.1.48][250]
- [326] J.. Sneed “Prime and quasi-prime number races” Thesis (Ph.D.)–University of Illinois at Urbana-Champaign ProQuest LLC, Ann Arbor, MI, 2009 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:3411454][251]
- [327] Vera. Sós and P. Turán “On some new theorems in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*6, 1955, pp. 241–255 DOI: [10.1007/BF02024389][252]
- [328] Robert Spira “Zeros of sections of the zeta function. II” In *Math. Comp.*22, 1968, pp. 163–173 DOI: [10.2307/2004774][253]
- [329] “Stanisław Knapowski (19. V. 1931–28. IX. 1967)” In *Colloq. Math.*23, 1971, pp. 309–310
- [330] H.. Stark “On the asymptotic density of the k k -free integers” In *Proc. Amer. Math. Soc.*17, 1966, pp. 1211–1214 DOI: [10.2307/2036123][254]
- [331] H.. Stark “A problem in comparative prime number theory” In *Acta Arith.*18, 1971, pp. 311–320 DOI: [10.4064/aa-18-1-311-320][255]
- [332] W. Staś “Über die Umkehrung eines Satzes von Ingham” In *Acta Arith.*6, 1960/1961, pp. 435–446 DOI: [10.4064/aa-6-4-435-446][256]
- [333] W. Staś “Some remarks on a series of Ramanujan” In *Acta Arith.*10, 1964/1965, pp. 359–368 DOI: [10.4064/aa-10-4-359-368][257]
- [334] W. Staś and K. Wiertelak “Further applications of Turán’s methods to the distribution of prime ideals in ideal classes (mod f f)” In *Acta Arith.*31.2, 1976, pp. 153–165 DOI: [10.4064/aa-31-2-153-165][258]
- [335] Włodzimierz Staś “On sign-changes in the remainder term of the prime ideal formula” In *Funct. Approx. Comment. Math.*13, 1982, pp. 159–166
- [336] S.. Stechkin and A.. Popov “Asymptotic distribution of prime numbers in the mean” In *Uspekhi Mat. Nauk*51.6(312), 1996, pp. 21–88 DOI: [10.1070/RM1996v051n06ABEH003000][259]
- [337] J. Steinig “The changes of sign of certain arithmetical error-terms” In *Comment. Math. Helv.*44, 1969, pp. 385–400 DOI: [10.1007/BF02564539][260]
- [338] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 0 0 bis 150000 150000 ” In *Sitzungsberichte Akad. Wiss. Wien IIa*106, 1897, pp. 835–1024
- [339] R.. von Sterneck “Bemerkung über die Summierung einiger zahlen-theoretischen Functionen” In *Monatsh. Math. Phys.*9.1, 1898, pp. 43–45 DOI: [10.1007/BF01707854][261]
- [340] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 150000 150000 bis 500000 500000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*110, 1901, pp. 1053–1102
- [341] R.. von Sterneck “Die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) bis zur Grenze 5000000 5000000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*121, 1912, pp. 1083–1096
- [342] R.. von Sterneck “Neue empirische Daten über die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) ” In *Proc. 5th International Congress of Mathematicians*1 Cambridge University Press, 1913, pp. 341–343
- [343] T.. Stieltjes “Correspondance d’Hermite et de Stieltjes” Gauthier–Villars, Imprimeur–Libraire, Paris, 1905, pp. xxi+pp. 1–477
- [344] Douglas. Stoll and Patrick Demichel “The impact of ζ ⁡ ( s) \zeta(s) complex zeros on π ⁡ ( x) \pi(x) for x < 10 10 13 x<10^{10^{13}} ” In *Math. Comp.*80.276, 2011, pp. 2381–2394 DOI: [10.1090/S0025-5718-2011-02477-4][262]
- [345] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. I” In *Math. Ann.*283, 1989, pp. 139–149
- [346] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. II” In *Math. Ann.*283, 1989, pp. 151–163
- [347] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. III” In *Monatsh. Math.*108, 1989, pp. 325–336
- [348] Bogdan Szydło “On oscillations in the additive divisor problem. I” In *Acta Arith.*66.1, 1994, pp. 63–69 DOI: [10.4064/aa-66-1-63-69][263]
- [349] Minoru Tanaka “A numerical investigation on cumulative sum of the Liouville function” In *Tokyo J. Math.*3.1, 1980, pp. 187–189 DOI: [10.3836/tjm/1270216093][264]
- [350] Minoru Tanaka “On the Möbius and allied functions” In *Tokyo J. Math.*3.2, 1980, pp. 215–218 DOI: [10.3836/tjm/1270472994][265]
- [351] Heinrich Tietze “Einige Tabellen zur Verteilung der Primzahlen auf Untergruppen der teilerfremden Restklassen nach gegebenem Modul” In *Abh. Bayer. Akad. Wiss. Math.-Nat. Abt. (N.F.)*1944.55, 1944, pp. 31
- [352] E.. Titchmarsh “The Theory of the Riemann Zeta-Function” Oxford, at the Clarendon Press, 1951, pp. vi+346
- [353] E.. Titchmarsh “The theory of the Riemann zeta-function” Edited and with a preface by D. R. Heath-Brown The Clarendon Press, Oxford University Press, New York, 1986, pp. x+412
- [354] P. Turán “On the remainder-term of the prime-number formula. II” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 155–166 DOI: [10.1007/BF02021308][266]
- [355] P. Turán “Nachtrag zu meiner Abhandlung “On some approximative Dirichlet polynomials in the theory of zeta-function of Riemann”” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 277–298 (unbound insert) DOI: [10.1007/BF02024493][267]
- [356] P. Turán “On some further one-sided theorems of new type in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*12, 1961, pp. 455–468 DOI: [10.1007/BF02023928][268]
- [357] P. Turán “On a comparative theory of primes” In *Proc. Fourth All-Union Math. Congr (Leningrad, 1961) (Russian), Vol. II*Izdat. “Nauka”, Leningrad, 1964, pp. 137–142
- [358] Paul Turán “On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann” In *Danske Vid. Selsk. Mat.-Fys. Medd.*24.17, 1948, pp. 36
- [359] Paul Turán “On the remainder-term of the prime-number formula. I” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 48–63 DOI: [10.1007/BF02022552][269]
- [360] Paul Turán “Eine neue Methode in der Analysis und deren Anwendungen” Akadémiai Kiadó, Budapest, 1953
- [361] Paul Turán “Commemoration on Stanisław Knapowski” In *Colloq. Math.*23, 1971, pp. 310–318 DOI: [10.4064/cm-23-2-309-321][270]
- [362] Paul Turán “On a new method of analysis and its applications”, Pure and Applied Mathematics (New York) John Wiley & Sons, Inc., New York, 1984, pp. xvi+584
- [363] A. Wintner “On the asymptotic distribution of the remainder term of the prime-number theorem” In *Amer. J. Math.*57.3, 1935, pp. 534–538 DOI: [10.2307/2371183][271]
- [364] A. Wintner “Asymptotic distributions and infinite convolutions” In *Lecture notes distributed by the Institute for Advanced Study (Princeton)*, 1938
- [365] A. Wintner “On the distribution function of the remainder term of the prime number theorem” In *Amer. J. Math.*63, 1941, pp. 233–248 DOI: [10.2307/2371519][272]
- [366] Aurel Wintner “A note on Mertens’ hypothesis” In *Rev. Ci. (Lima)*50, 1948, pp. 181–184
- [367] Aurel Wintner “On the λ \lambda -variant of Mertens’ μ \mu -hypothesis” In *Amer. J. Math.*80, 1958, pp. 639–642

## References

- [368] P. Chebyshev “Lettre de M. le professeur Tchébychev a M. Fuss, sur un nouveau théorème relatif aux nombres premiers contenus dans la formes 4 ​ n + 1 4n+1 et 4 ​ n + 3 4n+3 ” In *Bull. de la Classe phys. math. de l’Acad. Imp. des Sciences St. Petersburg*11, 1853, pp. 208
- [369] A. Piltz “Über die Häufigkeit der Primzahlen in arithmetischen Progressionen und über verwandte Gesetze” In *Habilitationsschrift, Friedrich–Schiller–Universität Jena*, 1884
- [370] P. Phragmén “Sur le logarithme intégral et la fonction f ⁡ ( x) f(x) de Riemann” In *Öfversigt af Kongl. Vetenskaps–Akademiens Föhandlingar.*48, 1891, pp. 599–616
- [371] F. Mertens “Über eine zahlentheoretische Funktion” In *Sitzungsberichte Akad. Wien*106, 1897, pp. 761–830
- [372] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 0 0 bis 150000 150000 ” In *Sitzungsberichte Akad. Wiss. Wien IIa*106, 1897, pp. 835–1024
- [373] R.. von Sterneck “Bemerkung über die Summierung einiger zahlen-theoretischen Functionen” In *Monatsh. Math. Phys.*9.1, 1898, pp. 43–45 DOI: [10.1007/BF01707854][261]
- [374] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 150000 150000 bis 500000 500000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*110, 1901, pp. 1053–1102
- [375] Erhard Schmidt “Über die Anzahl der Primzahlen unter gegebener Grenze” In *Math. Ann.*57.2, 1903, pp. 195–204 DOI: [10.1007/BF01444344][244]
- [376] T.. Stieltjes “Correspondance d’Hermite et de Stieltjes” Gauthier–Villars, Imprimeur–Libraire, Paris, 1905, pp. xxi+pp. 1–477
- [377] E. Landau “Über einen Satz von Tschebyschef” In *Math. Ann.*61.4, 1906, pp. 527–550 DOI: [10.1007/BF01449495][171]
- [378] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” Leipzig und Berlin, B. G. Teubner, 1909, pp. xviii+pp. 1–564ix+pp. 565–961
- [379] R.. von Sterneck “Die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) bis zur Grenze 5000000 5000000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*121, 1912, pp. 1083–1096
- [380] R.. von Sterneck “Neue empirische Daten über die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) ” In *Proc. 5th International Congress of Mathematicians*1 Cambridge University Press, 1913, pp. 341–343
- [381] J.. Littlewood “Sur la distribution des nombres premiers” In *Comptes Rendus de l’Acad. Sci. Paris*158, 1914, pp. 1869–1872
- [382] G.. Hardy and J.. Littlewood “On an assertion of Tchebychef” In *Proc. London Math. Soc. (2)*14, 1915, pp. xv–xvi
- [383] G.. Hardy “On Dirichlet’s divisor problem” In *Proc. London Math. Soc. (2)*15, 1916, pp. 1–25 DOI: [10.1112/plms/s2-15.1.1][81]
- [384] G.. Hardy and J.. Littlewood “Contributions to the theory of the Riemann zeta-function and the theory of the distribution of primes” In *Acta Math.*41.1, 1916, pp. 119–196
- [385] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 1–24 DOI: [10.1007/BF01203613][172]
- [386] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 213–219 DOI: [10.1007/BF01203613][172]
- [387] G. Pólya “Verschiedene Bemerkungen zur Zahlentheorie” In *Jahresbericht der deutschen Math.–Vereinigung*28, 1919, pp. 31–40
- [388] Harald Cramér “Ein Mittelwertsatz in der Primzahltheorie” In *Math. Z.*12.1, 1922, pp. 147–153 DOI: [10.1007/BF01482072][46]
- [389] J.. Littlewood “Mathematical Notes: 3; on a Theorem Concerning the Distribution of Prime Numbers” In *J. London Math. Soc.*2.1, 1927, pp. 41–45 DOI: [10.1112/jlms/s1-2.1.41][183]
- [390] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahltheorie” In *Gött. Nachr.*, 1930, pp. 19–27
- [391] C… Evelyn and E.. Linfoot “On a problem in the additive theory of numbers” In *Ann. of Math. (2)*32.2, 1931, pp. 261–270 DOI: [10.2307/1968190][54]
- [392] G. Pólya “On polar singularities of power series and of Dirichlet series” In *Proc. London Math. Soc. (2)*33.2, 1931, pp. 85–101 DOI: [10.1112/plms/s2-33.1.85][226]
- [393] A.. Ingham “The distribution of prime numbers” Cambridge Tracts in Mathematics and Mathematical Physics. 30. London: Cambridge University Press, 1932
- [394] S. Skewes “On the Difference π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}\,(x) (I)” In *J. London Math. Soc.*8.4, 1933, pp. 277–283 DOI: [10.1112/jlms/s1-8.4.277][249]
- [395] B. Jessen and A. Wintner “Distribution functions and the Riemann zeta function” In *Trans. Amer. Math. Soc.*38.1, 1935, pp. 48–88 DOI: [10.2307/1989728][100]
- [396] A. Wintner “On the asymptotic distribution of the remainder term of the prime-number theorem” In *Amer. J. Math.*57.3, 1935, pp. 534–538 DOI: [10.2307/2371183][271]
- [397] A.. Ingham “A note on the distribution of primes” In *Acta Arith.*1, 1936, pp. 201–211
- [398] J.. Littlewood “Mathematical Notes (12): An Inequality for a Sum of Cosines” In *J. London Math. Soc.*12.3, 1937, pp. 217–221 DOI: [10.1112/jlms/s1-12.2.217][184]
- [399] A. Wintner “Asymptotic distributions and infinite convolutions” In *Lecture notes distributed by the Institute for Advanced Study (Princeton)*, 1938
- [400] Hansraj Gupta “On a table of values of L ⁡ ( n) L(n) ” In *Proc. Indian Acad. Sci., Sect. A.*12, 1940, pp. 407–409
- [401] A. Wintner “On the distribution function of the remainder term of the prime number theorem” In *Amer. J. Math.*63, 1941, pp. 233–248 DOI: [10.2307/2371519][272]
- [402] A.. Ingham “On two conjectures in the theory of numbers” In *Amer. J. Math.*64, 1942, pp. 313–319 DOI: [10.2307/2371685][99]
- [403] Heinrich Tietze “Einige Tabellen zur Verteilung der Primzahlen auf Untergruppen der teilerfremden Restklassen nach gegebenem Modul” In *Abh. Bayer. Akad. Wiss. Math.-Nat. Abt. (N.F.)*1944.55, 1944, pp. 31
- [404] Paul Turán “On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann” In *Danske Vid. Selsk. Mat.-Fys. Medd.*24.17, 1948, pp. 36
- [405] Aurel Wintner “A note on Mertens’ hypothesis” In *Rev. Ci. (Lima)*50, 1948, pp. 181–184
- [406] P. Turán “On the remainder-term of the prime-number formula. II” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 155–166 DOI: [10.1007/BF02021308][266]
- [407] Paul Turán “On the remainder-term of the prime-number formula. I” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 48–63 DOI: [10.1007/BF02022552][269]
- [408] A.. Fawaz “The explicit formula for L 0 ​ ( x) L_{0}(x) ” In *Proc. London Math. Soc. (3)*1, 1951, pp. 86–103 DOI: [10.1112/plms/s3-1.1.86][55]
- [409] E.. Titchmarsh “The Theory of the Riemann Zeta-Function” Oxford, at the Clarendon Press, 1951, pp. vi+346
- [410] A.. Fawaz “On an unsolved problem in the analytic theory of numbers” In *Quart. J. Math. Oxford Ser. (2)*3, 1952, pp. 282–295 DOI: [10.1093/qmath/3.1.282][56]
- [411] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” 2d ed; With an appendix by Paul T. Bateman Chelsea Publishing Co., New York, 1953, pp. xviii+pp. 1–564ix+pp. 565–1001
- [412] Paul Turán “Eine neue Methode in der Analysis und deren Anwendungen” Akadémiai Kiadó, Budapest, 1953
- [413] S. Skewes “On the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x. II” In *Proc. London Math. Soc. (3)*5, 1955, pp. 48–70 DOI: [10.1112/plms/s3-5.1.48][250]
- [414] Vera. Sós and P. Turán “On some new theorems in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*6, 1955, pp. 241–255 DOI: [10.1007/BF02024389][252]
- [415] J. Leech “Note on the distribution of prime numbers” In *J. London Math. Soc.*32, 1957, pp. 56–58 DOI: [10.1112/jlms/s1-32.1.56][176]
- [416] Karl Prachar “Primzahlverteilung” Springer-Verlag, Berlin-Göttingen-Heidelberg, 1957, pp. x+415 pp.
- [417] Paul. Bateman and Emil Grosswald “On a theorem of Erdös and Szekeres” In *Illinois J. Math.*2, 1958, pp. 88–98 URL: [http://projecteuclid.org/euclid.ijm/1255380836][16]
- [418] C.. Haselgrove “A disproof of a conjecture of Pólya” In *Mathematika*5, 1958, pp. 141–145 DOI: [10.1112/S0025579300001480][83]
- [419] S. Knapowski “On prime numbers in an arithmetical progression” In *Acta Arith.*4, 1958, pp. 57–70 DOI: [10.4064/aa-4-1-57-70][135]
- [420] S. Knapowski “On the Möbius function” In *Acta Arith.*4, 1958, pp. 209–216 DOI: [10.4064/aa-4-3-209-216][136]
- [421] Aurel Wintner “On the λ \lambda -variant of Mertens’ μ \mu -hypothesis” In *Amer. J. Math.*80, 1958, pp. 639–642
- [422] S. Knapowski “On the mean values of certain functions in prime number theory” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 375–390. (unbound insert)
- [423] D. Shanks “Quadratic residues and the distribution of primes” In *Math. Tables Aids Comput.*13, 1959, pp. 272–284
- [424] P. Turán “Nachtrag zu meiner Abhandlung “On some approximative Dirichlet polynomials in the theory of zeta-function of Riemann”” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 277–298 (unbound insert) DOI: [10.1007/BF02024493][267]
- [425] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. I” In *Acta Arith.*6, 1960/1961, pp. 415–434 DOI: [10.4064/aa-6-4-415-434][137]
- [426] R. Lehman “On Liouville’s function” In *Math. Comp.*14, 1960, pp. 311–320 DOI: [10.2307/2003890][178]
- [427] D.. Lehmer and S. Selberg “A sum involving the function of Möbius” In *Acta Arith.*6, 1960, pp. 111–114 DOI: [10.4064/aa-6-1-111-114][179]
- [428] W. Staś “Über die Umkehrung eines Satzes von Ingham” In *Acta Arith.*6, 1960/1961, pp. 435–446 DOI: [10.4064/aa-6-4-435-446][256]
- [429] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. II” In *Acta Arith*7, 1961/1962, pp. 325–335 DOI: [10.4064/aa-7-4-325-335][138]
- [430] S. Knapowski “Mean-value estimations for the Möbius function. I” In *Acta Arith.*7, 1961, pp. 121–130 DOI: [10.4064/aa-7-2-121-130][139]
- [431] S. Knapowski “Mean-value estimations for the Möbius function. II” In *Acta Arith.*7, 1961, pp. 337–343 DOI: [10.4064/aa-7-4-337-343][140]
- [432] S. Knapowski “On sign-changes in the remainder-term in the prime-number formula” In *J. London Math. Soc.*36, 1961, pp. 451–460 DOI: [10.1112/jlms/s1-36.1.451][141]
- [433] S. Knapowski “On sign-changes of the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x ” In *Acta Arith.*7, 1961/1962, pp. 107–119 DOI: [10.4064/aa-7-2-107-119][142]
- [434] S. Knapowski and W. Staś “A note on a theorem of Hardy and Littlewood” In *Acta Arith.*7, 1961/1962, pp. 161–166 DOI: [10.4064/aa-7-2-161-166][146]
- [435] P. Turán “On some further one-sided theorems of new type in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*12, 1961, pp. 455–468 DOI: [10.1007/BF02023928][268]
- [436] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. III” In *Acta Arith*8, 1962/1963, pp. 97–105 DOI: [10.4064/aa-8-1-97-105][143]
- [437] S. Knapowski “On oscillations of certain means formed from the Möbius series. I” In *Acta Arith.*8, 1962/1963, pp. 311–320 DOI: [10.4064/aa-8-3-311-320][144]
- [438] S. Knapowski and P. Turán “Comparative prime-number theory. I. Introduction” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 299–314 DOI: [10.1007/BF02020796][147]
- [439] S. Knapowski and P. Turán “Comparative prime-number theory. II. Comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k, l ≢ 1 {\rm mod}\ k,\,l\not\equiv 1 mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 315–342 DOI: [10.1007/BF02020797][148]
- [440] S. Knapowski and P. Turán “Comparative prime-number theory. III. Continuation of the study of comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 343–364 DOI: [10.1007/BF02020798][149]
- [441] J. Rosser and Lowell Schoenfeld “Approximate formulas for some functions of prime numbers” In *Illinois J. Math.*6, 1962, pp. 64–94
- [442] S. Knapowski and P. Turán “Comparative prime-number theory. IV. Paradigma to the general case, k = 8 k=8 and 5 5 ” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 31–42 DOI: [10.1007/BF01901928][150]
- [443] S. Knapowski and P. Turán “Comparative prime-number theory. V. Some theorems concerning the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 43–63 DOI: [10.1007/BF01901929][151]
- [444] S. Knapowski and P. Turán “Comparative prime-number theory. VI. Continuation of the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 65–78 DOI: [10.1007/BF01901930][152]
- [445] S. Knapowski and P. Turán “Comparative prime-number theory. VII. The problem of sign-changes in the general case” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 241–250 DOI: [10.1007/BF01895712][153]
- [446] S. Knapowski and P. Turán “Comparative prime-number theory. VIII. Chebyshev’s problem for k = 8 k=8 ” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 251–268 DOI: [10.1007/BF01895713][154]
- [447] Gerhard Neubauer “Eine empirische Untersuchung zur Mertensschen Funktion” In *Numer. Math.*5, 1963, pp. 1–13 DOI: [10.1007/BF01385874][206]
- [448] A.. Ingham “The distribution of prime numbers”, Cambridge Tracts in Mathematics and Mathematical Physics, No. 30 Stechert-Hafner, Inc., New York, 1964, pp. v+114
- [449] I. Kátai “Eine Bemerkung zur “Comparative prime-number theory I-VIII” von S. Knapowski und P. Turán” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*7, 1964, pp. 33–40
- [450] S. Knapowski “On oscillations of certain means formed from the Möbius series. II” In *Acta Arith.*10, 1964, pp. 377–386 DOI: [10.4064/aa-10-4-377-386][145]
- [451] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. I” In *Acta Arith.*9, 1964, pp. 23–40 DOI: [10.4064/aa-9-1-23-40][155]
- [452] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. II. A modification of Chebyshev’s assertion” In *Acta Arith.*10, 1964, pp. 293–313 DOI: [10.4064/aa-10-3-293-313][156]
- [453] E. Makai “On a minimum problem. II” In *Acta Math. Acad. Sci. Hungar.*15, 1964, pp. 63–66 DOI: [10.1007/BF01897022][186]
- [454] W. Staś “Some remarks on a series of Ramanujan” In *Acta Arith.*10, 1964/1965, pp. 359–368 DOI: [10.4064/aa-10-4-359-368][257]
- [455] P. Turán “On a comparative theory of primes” In *Proc. Fourth All-Union Math. Congr (Leningrad, 1961) (Russian), Vol. II*Izdat. “Nauka”, Leningrad, 1964, pp. 137–142
- [456] Emil Grosswald “On some generalizations of theorems by Landau and Pólya” In *Israel J. Math.*3, 1965, pp. 211–220 DOI: [10.1007/BF03008399][77]
- [457] Imre Kátai “The Ω \Omega -estimation of the arithmetic mean of the Möbius function” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*15, 1965, pp. 15–18
- [458] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. III” In *Acta Arith.*11, 1965, pp. 115–127 DOI: [10.4064/aa-11-1-115-127][157]
- [459] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. IV” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 147–161 DOI: [10.4064/aa-11-2-193-202][158]
- [460] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. V” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 193–202 DOI: [10.4064/aa-11-2-193-202][158]
- [461] S. Knapowski and P. Turán “On an assertion of Čebyšev” In *J. Analyse Math.*14, 1965, pp. 267–274 DOI: [10.1007/BF02806393][159]
- [462] Imre Kátai “Omega-type investigations in prime number theory” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*16, 1966, pp. 369–396
- [463] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. VI. Accumulation theorems for residue-classes representing quadratic residues mod ​ k {\rm mod}\,k ” In *Acta Arith.*12, 1966, pp. 85–96 DOI: [10.4064/aa-12-1-85-96][160]
- [464] R.. Lehman “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Acta Arith.*11, 1966, pp. 397–410 DOI: [10.4064/aa-11-4-397-410][177]
- [465] H.. Stark “On the asymptotic density of the k k -free integers” In *Proc. Amer. Math. Soc.*17, 1966, pp. 1211–1214 DOI: [10.2307/2036123][254]
- [466] Emil Grosswald “Oscillation theorems of arithmetical functions” In *Trans. Amer. Math. Soc.*126, 1967, pp. 1–28 DOI: [10.2307/1994409][78]
- [467] I. Kátai “Comparative theory of prime numbers” In *Acta Math. Acad. Sci. Hungar*18, 1967, pp. 133–149 DOI: [10.1007/BF02020967][130]
- [468] I. Kátai “On investigations in the comparative prime number theory” In *Acta Math. Acad. Sci. Hungar.*18, 1967, pp. 379–391 DOI: [10.1007/BF02280297][131]
- [469] I. Kátai “On oscillations of number-theoretic functions” In *Acta Arith.*13, 1967/1968, pp. 107–122 DOI: [10.4064/aa-13-1-107-122][132]
- [470] J.. Ryan “One more “many-more” assertion” In *Amer. Math. Monthly*74.1, 1967, pp. 19–24 DOI: [10.2307/2314046][236]
- [471] A.. Cohen and M… Mayhew “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Proc. London Math. Soc. (3)*18, 1968, pp. 691–713 DOI: [10.1112/plms/s3-18.4.691][45]
- [472] I.. Good and R.. Churchhouse “The Riemann hypothesis and pseudorandom features of the Möbius sequence” In *Math. Comp.*22, 1968, pp. 857–861 DOI: [10.2307/2004584][74]
- [473] I. Kátai “On oscillation of the number of primes in an arithmetical progression.” In *Acta Sci. Math. (Szeged)*29, 1968, pp. 271–282
- [474] Robert Spira “Zeros of sections of the zeta function. II” In *Math. Comp.*22, 1968, pp. 163–173 DOI: [10.2307/2004774][253]
- [475] S. Knapowski and P. Turán “Über einige Fragen der vergleichenden Primzahltheorie” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 157–171
- [476] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahlsatz” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 233–244
- [477] J. Steinig “The changes of sign of certain arithmetical error-terms” In *Comment. Math. Helv.*44, 1969, pp. 385–400 DOI: [10.1007/BF02564539][260]
- [478] Bahman Saffari “Sur la fausseté de la conjecture de Mertens. (With discussion.)” In *C. R. Acad. Sci. Paris Sér. A-B*271, 1970, pp. A1097–A1101
- [479] P.. Bateman, J.. Brown, R.. Hall, K.. Kloss and Rosemarie. Stemmler “Linear relations connecting the imaginary parts of the zeros of the zeta function” In *Computers in number theory (Proc. Sci. Res. Council Atlas Sympos. No. 2, Oxford, 1969)*Academic Press, London, 1971, pp. 11–19
- [480] “Stanisław Knapowski (19. V. 1931–28. IX. 1967)” In *Colloq. Math.*23, 1971, pp. 309–310
- [481] H.. Stark “A problem in comparative prime number theory” In *Acta Arith.*18, 1971, pp. 311–320 DOI: [10.4064/aa-18-1-311-320][255]
- [482] Paul Turán “Commemoration on Stanisław Knapowski” In *Colloq. Math.*23, 1971, pp. 310–318 DOI: [10.4064/cm-23-2-309-321][270]
- [483] H.. Diamond “Two oscillation theorems” In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 113–118. Lecture Notes in Math.Vol. 251
- [484] Emil Grosswald “Oscillation theorems” Lecture Notes in Math., Vol. 251 In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 141–168
- [485] S. Knapowski and P. Turán “Further developments in the comparative prime number theory. VII” In *Acta Arith.*21, 1972, pp. 193–201 DOI: [10.4064/aa-21-1-193-201][161]
- [486] Daniel Shanks and Mohan Lal “Bateman’s constants reconsidered and the distribution of cubic residues” In *Math. Comp.*26, 1972, pp. 265–285 DOI: [10.2307/2004737][246]
- [487] S. Dancs and P. Turán “Investigations in the powersum theory. I” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*16, 1973, pp. 47–52 (1974)
- [488] W.. Jurkat “On the Mertens conjecture and related general Ω \Omega -theorems” In *Analytic number theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972)*Amer. Math. Soc., Providence, R.I., 1973, pp. 147–158
- [489] Richard. Brent “Irregularities in the distribution of primes and twin primes” Collection of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday In *Math. Comp.*29, 1975, pp. 43–56 DOI: [10.2307/2005460][34]
- [490] Harold. Diamond “Changes of sign of π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Enseignement Math. (2)*21.1, 1975, pp. 1–14
- [491] William Ellison “Les nombres premiers” En collaboration avec Michel Mendès France; Publications de l’Institut de Mathématique de l’Université de Nancago, No. IX; Actualités Scientifiques et Industrielles, No. 1366 Hermann, Paris, 1975, pp. xiv+442
- [492] W. Jurkat and A. Peyerimhoff “A constructive approach to Kronecker approximations and its application to the Mertens conjecture” In *J. Reine Angew. Math.*286(287), 1976, pp. 322–340 DOI: [10.1515/crll.1976.286-287.322][102]
- [493] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). I” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 153–169. Colloq. Math. Soc. János BolyaiVol. 13
- [494] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” In *Monatsh. Math.*82.2, 1976, pp. 163–175 DOI: [10.1007/BF01305997][162]
- [495] N. Levinson “On the number of sign changes of π ⁡ ( x) − li x \pi(x)-\mathop{\rm li}x ” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 171–177. Colloq. Math. Soc. János BolyaiVol. 13
- [496] J. Pintz “Bemerkungen zur Arbeit: “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” (Monatsh. Math. 82 (1976), no. 2, 163–175) von S. Knapowski und P. Turán” In *Monatsh. Math.*82.3, 1976, pp. 199–206 DOI: [10.1007/BF01526326][211]
- [497] W. Staś and K. Wiertelak “Further applications of Turán’s methods to the distribution of prime ideals in ideal classes (mod f f)” In *Acta Arith.*31.2, 1976, pp. 153–165 DOI: [10.4064/aa-31-2-153-165][258]
- [498] C. Bays and R.. Hudson “The segmented sieve of Eratosthenes and primes in arithmetic progressions to 10 12 10^{12} ” In *Nordisk Tidskr. Informationsbehandling (BIT)*17.2, 1977, pp. 121–127 DOI: [10.1007/bf01932283][18]
- [499] C. Hooley “On the Barban-Davenport-Halberstam theorem. VII” In *J. London Math. Soc. (2)*16.1, 1977, pp. 1–8 DOI: [10.1112/jlms/s2-16.1.1][88]
- [500] Richard. Hudson and Carter Bays “The mean behavior of primes in arithmetic progressions” In *J. Reine Angew. Math.*296, 1977, pp. 80–99 DOI: [10.1515/crll.1977.296.80][93]
- [501] S. Knapowski and P. Turán “On prime numbers ≡ 1 \equiv 1 resp. 3 ​ (mod 4) 3{\text{\rm\ (mod~$4$)}} ” In *Number theory and algebra*Academic Press, New York, 1977, pp. 157–165
- [502] J. Pintz “On the remainder term of the prime number formula. III. Sign changes of π ⁡ ( x) − li ​ x \pi(x)-{\rm li}x ” In *Studia Sci. Math. Hungar.*12.3-4, 1977, pp. 345–369 (1980)
- [503] J. Pintz “On the sign changes of π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}(x) ” In *Journées Arithmétiques de Caen (Univ. Caen, Caen, 1976)*Soc. Math. France, Paris, 1977, pp. 255–265. Astérisque No. 41–42
- [504] C. Bays and R.. Hudson “Details of the first region of integers x x with π 3, 2 ​ ( x) < π 3, 1 ​ ( x) \pi_{3,2}(x)<\pi_{3,1}(x) ” In *Math. Comp.*32.142, 1978, pp. 571–576 DOI: [10.2307/2006165][19]
- [505] Carter Bays and Richard. Hudson “On the fluctuations of Littlewood for primes of the form 4 ​ n ± 1 4n\pm 1 ” In *Math. Comp.*32.141, 1978, pp. 281–286 DOI: [10.2307/2006277][22]
- [506] Carter Bays and Richard. Hudson “The appearance of tens of billions of integers x x with π 24, 13 ​ ( x) < π 24, 1 ​ ( x) \pi_{24,13}(x)<\pi_{24,1}(x) in the vicinity of 10 12 10^{12} ” In *J. Reine Angew. Math.*299/300, 1978, pp. 234–237 DOI: [10.1515/crll.1978.299-300.234][23]
- [507] J. Pintz “On the remainder term of the prime number formula. IV. Sign changes of π ⁡ ( x) − li x \pi(x)-{\mathop{\rm li}}x ” In *Studia Sci. Math. Hungar.*13.1-2, 1978, pp. 29–42 (1981)
- [508] C. Bays and R.. Hudson “Numerical and graphical description of all axis crossing regions for the moduli 4 4 and 8 8 which occur before 10 12 10^{12} ” In *Internat. J. Math. Math. Sci.*2.1, 1979, pp. 111–119 DOI: [10.1155/S0161171279000119][20]
- [509] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. I” In *J. Reine Angew. Math.*307/308, 1979, pp. 411–417 DOI: [10.1515/crll.1979.307-308.411][29]
- [510] H… te Riele “Computations concerning the conjecture of Mertens” In *J. Reine Angew. Math.*311(312), 1979, pp. 356–360 DOI: [10.1515/crll.1979.311-312.356][231]
- [511] H.-J. Bentz and J. Pintz “Quadratic residues and the distribution of prime numbers” In *Monatsh. Math.*90.2, 1980, pp. 91–100 DOI: [10.1007/BF01303260][26]
- [512] Hans-J. Bentz and János Pintz “Über eine Verallgemeinerung des Tschebyschef-Problems” In *Math. Z.*174.1, 1980, pp. 35–41 DOI: [10.1007/BF01215079][28]
- [513] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. II” In *J. Reine Angew. Math.*313, 1980, pp. 52–58 DOI: [10.1515/crll.1980.313.52][30]
- [514] P.. Gallagher “Some consequences of the Riemann hypothesis” In *Acta Arith.*37, 1980, pp. 339–343 DOI: [10.4064/aa-37-1-339-343][71]
- [515] Richard. Hudson “A common combinatorial principle underlies Riemann’s formula, the Chebyshev phenomenon, and other subtle effects in comparative prime number theory. I” In *J. Reine Angew. Math.*313, 1980, pp. 133–150 DOI: [10.1515/crll.1980.313.133][91]
- [516] William Monach “Numerical Investigation of Several Problems in Number Theory” Thesis (Ph.D.)–University of Michigan) ProQuest LLC, Ann Arbor, MI, 1980 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:8106192][194]
- [517] H.. Montgomery “The zeta function and prime numbers” In *Proceedings of the Queen’s Number Theory Conference, 1979 (Kingston, Ont., 1979)*54, Queen’s Papers in Pure and Appl. Math. Queen’s Univ., Kingston, Ont., 1980, pp. 1–31
- [518] J. Pintz “On the remainder term of the prime number formula. I. On a problem of Littlewood” In *Acta Arith.*36.4, 1980, pp. 341–365 DOI: [10.4064/aa-36-4-341-365][212]
- [519] J. Pintz “On the remainder term of the prime number formula. II. On a theorem of Ingham” In *Acta Arith.*37, 1980, pp. 209–220 DOI: [10.4064/aa-37-1-209-220][213]
- [520] J. Pintz “On the remainder term of the prime number formula. V. Effective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 215–223
- [521] J. Pintz “On the remainder term of the prime number formula. VI. Ineffective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 225–230
- [522] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). II” In *Studia Sci. Math. Hungar.*15.4, 1980, pp. 491–496
- [523] Minoru Tanaka “A numerical investigation on cumulative sum of the Liouville function” In *Tokyo J. Math.*3.1, 1980, pp. 187–189 DOI: [10.3836/tjm/1270216093][264]
- [524] Minoru Tanaka “On the Möbius and allied functions” In *Tokyo J. Math.*3.2, 1980, pp. 215–218 DOI: [10.3836/tjm/1270472994][265]
- [525] R.. Anderson and H.. Stark “Oscillation theorems” In *Analytic number theory (Philadelphia, Pa., 1980)*899, Lecture Notes in Math. Springer, Berlin-New York, 1981, pp. 79–106
- [526] W… Chen “On the error term of the prime number theorem and the difference between the number of primes in the residue classes modulo 4 4 ” In *J. London Math. Soc. (2)*23.1, 1981, pp. 24–40 DOI: [10.1112/jlms/s2-23.1.24][44]
- [527] J. Pintz “On the sign changes of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n) ” In *Analysis*1.3, 1981, pp. 191–195 DOI: [10.1524/anly.1981.1.3.191][214]
- [528] H.-J. Bentz “Discrepancies in the distribution of prime numbers” In *J. Number Theory*15.2, 1982, pp. 252–274 DOI: [10.1016/0022-314X(82)90030-0][25]
- [529] H.-J. Bentz and J. Pintz “Über das Tschebyschef-Problem” In *Resultate Math.*5.1, 1982, pp. 1–5 DOI: [10.1007/bf03323296][27]
- [530] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). I” In *Acta Arith.*42.1, 1982, pp. 49–55 DOI: [10.4064/aa-42-1-49-55][215]
- [531] Włodzimierz Staś “On sign-changes in the remainder term of the prime ideal formula” In *Funct. Approx. Comment. Math.*13, 1982, pp. 159–166
- [532] Carter Bays and Richard. Hudson “The cyclic behavior of primes in the arithmetic progressions modulo 11 11 ” In *J. Reine Angew. Math.*339, 1983, pp. 215–220 DOI: [10.1515/crll.1983.339.215][24]
- [533] G. Kolesnik and E.. Straus “On the sum of powers of complex numbers” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 427–442
- [534] J. Pintz “On the distribution of square-free numbers” In *J. London Math. Soc. (2)*28.3, 1983, pp. 401–405 DOI: [10.1112/jlms/s2-28.3.401][216]
- [535] J. Pintz “Oscillatory properties of the remainder term of the prime number formula” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 551–560
- [536] G. Robin “Sur l’ordre maximum de la fonction somme des diviseurs” In *Seminar on number theory, Paris 1981–82 (Paris, 1981/1982)*38, Progr. Math. Birkhäuser Boston, Boston, MA, 1983, pp. 233–244
- [537] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. I” In *Acta Arith.*44.4, 1984, pp. 365–377 DOI: [10.4064/aa-44-4-365-377][103]
- [538] J. Pintz “On the partial sums of the Möbius function” In *Topics in classical number theory, Vol. I, II (Budapest, 1981)*34, Colloq. Math. Soc. János Bolyai North-Holland, Amsterdam, 1984, pp. 1229–1250
- [539] J. Pintz “On the remainder term of the prime number formula and the zeros of Riemann’s zeta-function” In *Number theory, Noordwijkerhout 1983 (Noordwijkerhout, 1983)*1068, Lecture Notes in Math. Springer, Berlin, 1984, pp. 186–197
- [540] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). III” In *Acta Arith.*43.2, 1984, pp. 105–113 DOI: [10.4064/aa-43-2-105-113][217]
- [541] J. Pintz and S. Salerno “Irregularities in the distribution of primes in arithmetic progressions. II” In *Arch. Math. (Basel)*43.4, 1984, pp. 351–357 DOI: [10.1007/BF01196659][219]
- [542] J. Pintz and S. Salerno “On the comparative theory of primes” In *Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4)*11.2, 1984, pp. 245–260 URL: [http://www.numdam.org/item?id=ASNSP_1984_4_11_2_245_0][220]
- [543] János Pintz and Saverio Salerno “Irregularities in the distribution of primes in arithmetic progressions. I” In *Arch. Math. (Basel)*42.5, 1984, pp. 439–447 DOI: [10.1007/BF01190694][223]
- [544] Paul Turán “On a new method of analysis and its applications”, Pure and Applied Mathematics (New York) John Wiley & Sons, Inc., New York, 1984, pp. xvi+584
- [545] William Ellison and Fern Ellison “Prime numbers”, A Wiley-Interscience Publication John Wiley & Sons, Inc., New York; Hermann, Paris, 1985, pp. xii+417
- [546] Richard. Hudson “Averaging effects on irregularities in the distribution of primes in arithmetic progressions” In *Math. Comp.*44.170, 1985, pp. 561–571 DOI: [10.2307/2007974][92]
- [547] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. II” In *Acta Arith.*45.1, 1985, pp. 65–74 DOI: [10.4064/aa-45-1-65-74][104]
- [548] A.. Odlyzko and H… te Riele “Disproof of the Mertens conjecture” In *J. Reine Angew. Math.*357, 1985, pp. 138–160 DOI: [10.1515/crll.1985.357.138][209]
- [549] J. Pintz and S. Salerno “Accumulation theorems for primes in arithmetic progressions” In *Acta Math. Hungar.*46.1-2, 1985, pp. 151–172 DOI: [10.1007/BF01961016][221]
- [550] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. I” In *Acta Math. Hungar.*48.1-2, 1986, pp. 173–185 DOI: [10.1007/BF01949062][114]
- [551] J. Pintz and S. Salerno “Some consequences of the general Riemann hypothesis in the comparative theory of primes” In *J. Number Theory*23.2, 1986, pp. 183–194 DOI: [10.1016/0022-314X(86)90088-0][222]
- [552] Guy Robin “Irrégularités dans la distribution des nombres premiers dans les progressions arithmétiques” In *Ann. Fac. Sci. Toulouse Math. (5)*8.2, 1986, pp. 159–173 URL: [http://www.numdam.org/item?id=AFST_1986-1987_5_8_2_159_0][233]
- [553] E.. Titchmarsh “The theory of the Riemann zeta-function” Edited and with a preface by D. R. Heath-Brown The Clarendon Press, Oxford University Press, New York, 1986, pp. x+412
- [554] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. III” In *Acta Arith.*48.4, 1987, pp. 347–371 DOI: [10.4064/aa-48-4-347-371][105]
- [555] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. II” In *Acta Math. Hungar.*49.3-4, 1987, pp. 441–453 DOI: [10.1007/BF01951008][115]
- [556] J. Pintz “An effective disproof of the Mertens conjecture” In *Astérisque*, 1987, pp. 325–333346
- [557] Herman.. te Riele “On the sign of the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Math. Comp.*48.177, 1987, pp. 323–328 DOI: [10.2307/2007893][232]
- [558] R. Balasubramanian, K. Ramachandra and M.. Subbarao “On the error function in the asymptotic formula for the counting function of k k -full numbers” In *Acta Arith.*50.2, 1988, pp. 107–118 DOI: [10.4064/aa-50-2-107-118][14]
- [559] A. Fujii “Some generalizations of Chebyshev’s conjecture” In *Proc. Japan Acad. Ser. A Math. Sci.*64.7, 1988, pp. 260–263 URL: [http://projecteuclid.org/euclid.pja/1195513180][69]
- [560] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. IV” In *Acta Arith.*50.1, 1988, pp. 15–21 DOI: [10.4064/aa-50-1-15-21][106]
- [561] J. Kaczorowski and W. Staś “On the number of sign changes in the remainder-term of the prime-ideal theorem” In *Colloq. Math.*56.1, 1988, pp. 185–197 DOI: [10.4064/cm-56-1-185-197][116]
- [562] Jerzy Kaczorowski and Włodzimierz Staś “On the number of sign-changes in the remainder-term of the prime-ideal theorem” In *Discuss. Math.*9, 1988, pp. 83–102 (1989)
- [563] S.. Gonek “On negative moments of the Riemann zeta-function” In *Mathematika*36.1, 1989, pp. 71–88 DOI: [10.1112/S0025579300013589][73]
- [564] Dennis. Hejhal “On the distribution of log ⁡ | ζ ′ ​ ( 1 2 + i ​ t) | \log|\zeta^{\prime}(\frac{1}{2}+it)| ” In *Number theory, trace formulas and discrete groups (Oslo, 1987)*Academic Press, Boston, MA, 1989, pp. 343–370
- [565] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. I” In *Math. Ann.*283, 1989, pp. 139–149
- [566] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. II” In *Math. Ann.*283, 1989, pp. 151–163
- [567] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. III” In *Monatsh. Math.*108, 1989, pp. 325–336
- [568] J. Kaczorowski “The k k -functions in multiplicative number theory. I. On complex explicit formulae” In *Acta Arith.*56.3, 1990, pp. 195–211 DOI: [10.4064/aa-56-3-195-211][107]
- [569] J. Kaczorowski “The k k -functions in multiplicative number theory. II. Uniform distribution of zeta zeros” In *Acta Arith.*56.3, 1990, pp. 213–224 DOI: [10.4064/aa-56-3-213-224][108]
- [570] K.. Bartz “On some complex explicit formulae connected with the Möbius function. I, II” In *Acta Arith.*57.4, 1991, pp. 283–293295–305 DOI: [10.4064/aa-57-4-283-293][15]
- [571] Akio Fujii “An additive problem of prime numbers. III” In *Proc. Japan Acad. Ser. A Math. Sci.*67.8, 1991, pp. 278–283 URL: [http://projecteuclid.org/euclid.pja/1195511989][70]
- [572] J. Kaczorowski “The k k -functions in multiplicative number theory. III. Uniform distribution of zeta zeros; discrepancy” In *Acta Arith.*57.3, 1991, pp. 199–210 DOI: [10.4064/aa-57-3-199-210][109]
- [573] J. Kaczorowski “The k k -functions in multiplicative number theory. IV. On a method of A. E. Ingham” In *Acta Arith.*57.3, 1991, pp. 231–244 DOI: [10.4064/aa-57-3-231-244][110]
- [574] J. Kaczorowski “The k k -functions in multiplicative number theory. V. Changes of sign of some arithmetical error terms” In *Acta Arith.*59.1, 1991, pp. 37–58 DOI: [10.4064/aa-59-1-37-58][111]
- [575] J. Pintz “On an assertion of Riemann concerning the distribution of prime numbers” In *Acta Math. Hungar.*58.3-4, 1991, pp. 383–387 DOI: [10.1007/BF01903967][218]
- [576] D.. Heath-Brown “The distribution and moments of the error term in the Dirichlet divisor problem” In *Acta Arith.*60.4, 1992, pp. 389–415 DOI: [10.4064/aa-60-4-389-415][87]
- [577] J. Kaczorowski “A contribution to the Shanks-Rényi race problem” In *Quart. J. Math. Oxford Ser. (2)*44.176, 1993, pp. 451–458 DOI: [10.1093/qmath/44.4.451][112]
- [578] A. Sankaranarayanan “On the sign changes in the remainder term of an asymptotic formula for the number of squarefree numbers” In *Arch. Math. (Basel)*60.1, 1993, pp. 51–57 DOI: [10.1007/BF01194239][237]
- [579] Jerzy Kaczorowski “Results on the distribution of primes” In *J. Reine Angew. Math.*446, 1994, pp. 89–113 DOI: [10.1515/crll.1994.446.89][117]
- [580] Hugh. Montgomery “Ten lectures on the interface between analytic number theory and harmonic analysis” 84, CBMS Regional Conference Series in Mathematics Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1994, pp. xiv+220 DOI: [10.1090/cbms/084][195]
- [581] Yo̵ichi Motohashi “The binary additive divisor problem” In *Ann. Sci. École Norm. Sup. (4)*27.5, 1994, pp. 529–572 URL: [http://www.numdam.org/item?id=ASENS_1994_4_27_5_529_0][203]
- [582] M. Rubinstein and P. Sarnak “Chebyshev’s bias” In *Experiment. Math.*3.3, 1994, pp. 173–197 URL: [http://projecteuclid.org/euclid.em/1048515870][234]
- [583] Bogdan Szydło “On oscillations in the additive divisor problem. I” In *Acta Arith.*66.1, 1994, pp. 63–69 DOI: [10.4064/aa-66-1-63-69][263]
- [584] Jerzy Kaczorowski “On the distribution of primes (mod 4 4)” In *Analysis*15.2, 1995, pp. 159–171 DOI: [10.1524/anly.1995.15.2.159][118]
- [585] Jerzy Kaczorowski “On the Shanks-Rényi race problem mod 5 5 ” In *J. Number Theory*50.1, 1995, pp. 106–118 DOI: [10.1006/jnth.1995.1006][119]
- [586] J. Kaczorowski “On the Shanks-Rényi race problem” In *Acta Arith.*74.1, 1996, pp. 31–46 DOI: [10.4064/aa-74-1-31-46][113]
- [587] S.. Stechkin and A.. Popov “Asymptotic distribution of prime numbers in the mean” In *Uspekhi Mat. Nauk*51.6(312), 1996, pp. 21–88 DOI: [10.1070/RM1996v051n06ABEH003000][259]
- [588] Jerzy Kaczorowski “Boundary values of Dirichlet series and the distribution of primes” In *European Congress of Mathematics, Vol. I (Budapest, 1996)*168, Progr. Math. Birkhäuser, Basel, 1998, pp. 237–254
- [589] S. Gonek “The second moment of the reciprocal of the Riemann zeta function and its derivative”, 1999 URL: [https://www.slmath.org/workshops/101/schedules/25626][72]
- [590] C. Bays and R.. Hudson “Zeroes of Dirichlet L L -functions and irregularities in the distribution of primes” In *Math. Comp.*69.230, 2000, pp. 861–866 DOI: [10.1090/S0025-5718-99-01105-9][21]
- [591] Carter Bays and Richard. Hudson “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Math. Comp.*69.231, 2000, pp. 1285–1296
- [592] A. Feuerverger and G. Martin “Biases in the Shanks-Rényi prime number race” In *Experiment. Math.*9.4, 2000, pp. 535–570 URL: [http://projecteuclid.org/euclid.em/1045759521][57]
- [593] Władysław Narkiewicz “The development of prime number theory”, Springer Monographs in Mathematics Springer-Verlag, Berlin, 2000, pp. xii+448 DOI: [10.1007/978-3-662-13157-2][205]
- [594] N. Ng “Limiting Distributions and Zeros of Artin L L -Functions” Thesis (Ph.D.)–University of British Columbia, 2000 URL: [http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf][207]
- [595] J.-C. Puchta “On large oscillations of the remainder of the prime number theorems” In *Acta Math. Hungar.*87.3, 2000, pp. 213–227
- [596] C. Bays, K. Ford, R.. Hudson and M. Rubinstein “Zeros of Dirichlet L L -functions near the real axis and Chebyshev’s bias” In *J. Number Theory*87.1, 2001, pp. 54–76 DOI: [10.1006/jnth.2000.2601][17]
- [597] Kevin Ford and Richard. Hudson “Sign changes in π q, a ​ ( x) − π q, b ​ ( x) \pi_{q,a}(x)-\pi_{q,b}(x) ” In *Acta Arith.*100.4, 2001, pp. 297–314 DOI: [10.4064/aa100-4-1][68]
- [598] Imre. Ruzsa “Consecutive primes modulo 4” In *Indag. Math. (N.S.)*12.4, 2001, pp. 489–503 DOI: [10.1016/S0019-3577(01)80038-0][235]
- [599] K. Ford and S. Konyagin “Chebyshev’s conjecture and the prime number race” In *IV International Conference “Modern Problems of Number Theory and its Applications”: Current Problems, Part II (Russian) (Tula, 2001)*Mosk. Gos. Univ. im. Lomonosova, Mekh.-Mat. Fak., Moscow, 2002, pp. 67–91
- [600] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line” In *Duke Math. J.*113.2, 2002, pp. 313–330 DOI: [10.1215/S0012-7094-02-11324-6][64]
- [601] Yuk-Kam Lau “On the existence of limiting distributions of some number-theoretic error terms” In *J. Number Theory*94.2, 2002, pp. 359–374 DOI: [10.1006/jnth.2001.2734][173]
- [602] G. Martin “Asymmetries in the Shanks-Rényi prime number race” In *Number theory for the millennium, II (Urbana, IL, 2000)*A K Peters, Natick, MA, 2002, pp. 403–415
- [603] E.. Balanzario and S. Hernández “On the number of large oscillations of some arithmetical power series” In *Arch. Math. (Basel)*81.3, 2003, pp. 285–290 DOI: [10.1007/s00013-003-4704-2][13]
- [604] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line. II” In *Proceedings of the Session in Analytic Number Theory and Diophantine Equations*360, Bonner Math. Schriften Univ. Bonn, Bonn, 2003, pp. 40
- [605] Jerzy Kaczorowski and Olivier Ramaré “Almost periodicity of some error terms in prime number theory” In *Acta Arith.*106.3, 2003, pp. 277–297 DOI: [10.4064/aa106-3-6][123]
- [606] P. Leboeuf “Prime correlations and fluctuations” In *Ann. Henri Poincaré*4.suppl. 2, 2003, pp. S727–S752 DOI: [10.1007/s00023-003-0958-2][175]
- [607] Marc Deléglise, Pierre Dusart and Xavier-François Roblot “Counting primes in residue classes” In *Math. Comp.*73.247, 2004, pp. 1565–1575 DOI: [10.1090/S0025-5718-04-01649-7][47]
- [608] Tadej Kotnik and Jan van Lune “On the order of the Mertens function” In *Experiment. Math.*13.4, 2004, pp. 473–481
- [609] Pieter Moree “Chebyshev’s bias for composite numbers with restricted prime divisors” In *Math. Comp.*73.245, 2004, pp. 425–449 DOI: [10.1090/S0025-5718-03-01536-9][197]
- [610] N. Ng “The distribution of the summatory function of the Möbius function” In *Proc. London Math. Soc. (3)*89.2, 2004, pp. 361–389 DOI: [10.1112/S0024611504014741][208]
- [611] J.-C. Schlage–Puchta “Sign changes of π ⁡ ( x, q, 1) − π ⁡ ( x, q, a) \pi(x,q,1)-\pi(x,q,a) ” In *Acta Math. Hungar.*102.4, 2004, pp. 305–320 DOI: [10.1023/B:AMHU.0000024681.23784.d1][242]
- [612] A.. Karatsuba “Behavior of the function R 1 ​ ( x) R_{1}(x) and of its mean value” In *Dokl. Akad. Nauk*404.4, 2005, pp. 439–442
- [613] A.. Karatsuba “On the approximation of π ⁡ ( x) \pi(x) ” In *Chebyshevskii Sb.*5.4(12), 2005, pp. 5–20
- [614] A.. Karatsuba “On the number of sign changes of the function R 1 ​ ( x) R_{1}(x) and its mean values” In *Chebyshevskii Sb.*6.2(14), 2005, pp. 163–183
- [615] Maciej Radziejewski “On the distribution of algebraic numbers with prescribed factorization properties” In *Acta Arith.*116.2, 2005, pp. 153–171 DOI: [10.4064/aa116-2-4][228]
- [616] Maciej Radziejewski “Oscillations of error terms associated with certain arithmetical functions” In *Monatsh. Math.*144.2, 2005, pp. 113–130 DOI: [10.1007/s00605-003-0147-x][229]
- [617] A. Granville and G. Martin “Prime number races” In *Amer. Math. Monthly*113.1, 2006, pp. 1–33 DOI: [10.2307/27641834][76]
- [618] Tadej Kotnik and Herman te Riele “The Mertens conjecture revisited” In *Algorithmic number theory*4076, Lecture Notes in Comput. Sci. Springer, Berlin, 2006, pp. 156–167
- [619] Hugh. Montgomery and Ulrike.. Vorhauer “Changes of sign of the error term in the prime number theorem” In *Funct. Approx. Comment. Math.*35, 2006, pp. 235–247 DOI: [10.7169/facm/1229442626][196]
- [620] Jerzy Kaczorowski “Results on the Möbius function” In *J. Lond. Math. Soc. (2)*75.2, 2007, pp. 509–521 DOI: [10.1112/jlms/jdm006][120]
- [621] Jerzy Kaczorowski and Kazimierz Wiertelak “ Ω \Omega -estimates for a class of arithmetic error terms” In *Math. Proc. Cambridge Philos. Soc.*142.3, 2007, pp. 385–394 DOI: [10.1017/S0305004107000035][124]
- [622] P. Sarnak “Letter to Barry Mazur on ‘Chebyshev’s bias’ for τ ⁡ ( p) \tau(p) ”, 2007 URL: [http://web.math.princeton.edu/sarnak/MazurLtrMay08.PDF][241]
- [623] Peter Borwein, Ron Ferguson and Michael. Mossinghoff “Sign changes in sums of the Liouville function” In *Math. Comp.*77.263, 2008, pp. 1681–1694 DOI: [10.1090/S0025-5718-08-02036-X][32]
- [624] Byungchul Cha “Chebyshev’s bias in function fields” In *Compos. Math.*144.6, 2008, pp. 1351–1374 DOI: [10.1112/S0010437X08003631][39]
- [625] Tadej Kotnik “The prime-counting function and its analytic approximations: π ⁡ ( x) \pi(x) and its approximations” In *Adv. Comput. Math.*29.1, 2008, pp. 55–70 DOI: [10.1007/s10444-007-9039-2][163]
- [626] Emmanuel Kowalski “The large sieve, monodromy, and zeta functions of algebraic curves. II. Independence of the zeros” In *Int. Math. Res. Not. IMRN*, 2008, pp. Art. ID rnn 09157
- [627] Barry Mazur “Finding meaning in error terms” In *Bull. Amer. Math. Soc. (N.S.)*45.2, 2008, pp. 185–228 DOI: [10.1090/S0273-0979-08-01207-X][189]
- [628] H.. Diamond and J. Pintz “Oscillation of Mertens’ product formula” In *J. Théor. Nombres Bordeaux*21.3, 2009, pp. 523–533 URL: [http://jtnb.cedram.org/item?id=JTNB_2009__21_3_523_0][52]
- [629] Jerzy Kaczorowski “On the distribution of irreducible algebraic integers” In *Monatsh. Math.*156.1, 2009, pp. 47–71 DOI: [10.1007/s00605-008-0559-8][121]
- [630] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of a given size of some arithmetic error terms” In *Trans. Amer. Math. Soc.*361.9, 2009, pp. 5023–5039 DOI: [10.1090/S0002-9947-09-04803-X][125]
- [631] J.. Sneed “Prime and quasi-prime number races” Thesis (Ph.D.)–University of Illinois at Urbana-Champaign ProQuest LLC, Ann Arbor, MI, 2009 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:3411454][251]
- [632] Byungchul Cha and Seick Kim “Biases in the prime number race of function fields” In *J. Number Theory*130.4, 2010, pp. 1048–1055 DOI: [10.1016/j.jnt.2009.09.015][41]
- [633] Kuok Chao and Roger Plymen “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Int. J. Number Theory*6.3, 2010, pp. 681–690 DOI: [10.1142/S1793042110003125][42]
- [634] K. Ford and J. Sneed “Chebyshev’s bias for products of two primes” In *Experiment. Math.*19.4, 2010, pp. 385–398 DOI: [10.1080/10586458.2010.10390630][66]
- [635] Jerzy Kaczorowski “ Ω \Omega -estimates related to irreducible algebraic integers” In *Math. Nachr.*283.9, 2010, pp. 1291–1303 DOI: [10.1002/mana.200710158][122]
- [636] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of the remainder term related to the Euler totient function” In *J. Number Theory*130.12, 2010, pp. 2683–2700 DOI: [10.1016/j.jnt.2010.06.010][126]
- [637] Jerzy Kaczorowski and Kazimierz Wiertelak “Smoothing arithmetic error terms: the case of the Euler ϕ \phi function” In *Math. Nachr.*283.11, 2010, pp. 1637–1645 DOI: [10.1002/mana.200810048][127]
- [638] Yannick Saouter and Patrick Demichel “A sharp region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*79.272, 2010, pp. 2395–2405 DOI: [10.1090/S0025-5718-10-02351-3][238]
- [639] R.. Brent and Jan van Lune “A note on Pólya’s observation concerning Liouville’s function” In *Herman J. J. te Riele Liber Amicorum*, CWI, 2011, pp. 92–97 URL: [https://arxiv.org/abs/1112.4911][33]
- [640] B Cha and B.-H. Im “Chebyshev’s bias in Galois extensions of global function fields” In *J. Number Theory*131.10, 2011, pp. 1875–1886 DOI: [10.1016/j.jnt.2011.03.011][37]
- [641] D. Fiorilli “Irrégularités dans la distribution des nombres premiers et des suites plus générales dans les progressions arithmétiques” Thesis (Ph.D.)–Université de Montréal ProQuest LLC, Ann Arbor, MI, 2011
- [642] Douglas. Stoll and Patrick Demichel “The impact of ζ ⁡ ( s) \zeta(s) complex zeros on π ⁡ ( x) \pi(x) for x < 10 10 13 x<10^{10^{13}} ” In *Math. Comp.*80.276, 2011, pp. 2381–2394 DOI: [10.1090/S0025-5718-2011-02477-4][262]
- [643] Matthias Kunik and Lutz. Lucht “Power series with the von Mangoldt function” In *Funct. Approx. Comment. Math.*47.part 1, 2012, pp. 15–33 DOI: [10.7169/facm/2012.47.1.2][165]
- [644] Y. Lamzouri “Large deviations of the limiting distribution in the Shanks–Rényi prime number race” In *Math. Proc. Cambridge Philos. Soc.*153.1, 2012, pp. 147–166 DOI: [10.1017/S030500411200014X][166]
- [645] Y. Lamzouri “The Shanks-Rényi prime number race with many contestants” In *Math. Res. Lett.*19.3, 2012, pp. 649–666 DOI: [10.4310/MRL.2012.v19.n3.a11][167]
- [646] Micah. Milinovich and Nathan Ng “A note on a conjecture of Gonek” In *Funct. Approx. Comment. Math.*46, 2012, pp. 177–187 DOI: [10.7169/facm/2012.46.2.3][193]
- [647] Michael. Mossinghoff and Timothy. Trudgian “Between the problems of Pólya and Turán” In *J. Aust. Math. Soc.*93.1–2, 2012, pp. 157–171 DOI: [10.1017/S1446788712000201][200]
- [648] D. Fiorilli and G. Martin “Inequities in the Shanks-Rényi prime number race: an asymptotic formula for the densities” In *J. Reine Angew. Math.*676, 2013, pp. 121–212
- [649] K. Ford, Y. Lamzouri and S. Konyagin “The prime number race and zeros of Dirichlet L L -functions off the critical line: Part III” In *Q. J. Math.*64.4, 2013, pp. 1091–1098 DOI: [10.1093/qmath/has021][65]
- [650] Peter Humphries “The distribution of weighted sums of the Liouville function and Pólya’s conjecture” In *J. Number Theory*133.2, 2013, pp. 545–582 DOI: [10.1016/j.jnt.2012.08.011][94]
- [651] Y. Lamzouri “Prime number races with three or more competitors” In *Math. Ann.*356.3, 2013, pp. 1117–1162 DOI: [10.1007/s00208-012-0874-1][168]
- [652] C. Myerscough “Application of an accurate remainder term in the calculation of residue class distributions”, 2013 URL: [https://arxiv.org/abs/1301.1434][204]
- [653] O.. Petrushov “Asymptotic estimates of functions based on the behavior of their Laplace transforms near singular points” In *Math. Notes*93.5–6, 2013, pp. 906–916 DOI: [10.1134/S0001434613050283][210]
- [654] A. Akbary, N. Ng and M. Shahabi “Limiting distributions of the classical error terms of prime number theory” In *Q. J. Math.*65.3, 2014, pp. 743–780 DOI: [10.1093/qmath/hat059][4]
- [655] Sneha Chaubey, Melinda Lanius and Alexandru Zaharescu “Irrational factor races” In *Proc. Indian Acad. Sci. Math. Sci.*124.4, 2014, pp. 471–479 DOI: [10.1007/s12044-014-0198-z][43]
- [656] D. Fiorilli “Elliptic curves of unbounded rank and Chebyshev’s bias” In *Int. Math. Res. Not. IMRN*, 2014, pp. 4997–5024 DOI: [10.1093/imrn/rnt103][58]
- [657] D. Fiorilli “Highly biased prime number races” In *Algebra Number Theory*8.7, 2014, pp. 1733–1767 DOI: [10.2140/ant.2014.8.1733][59]
- [658] Peter Humphries “On the Mertens conjecture for elliptic curves over finite fields” In *Bull. Aust. Math. Soc.*89.1, 2014, pp. 19–32 DOI: [10.1017/S0004972712001116][95]
- [659] Peter Humphries “On the Mertens conjecture for function fields” In *Int. J. Number Theory*10.2, 2014, pp. 341–361 DOI: [10.1142/S1793042113500978][96]
- [660] Maciej Radziejewski “Oscillatory properties of real functions with weakly bounded Mellin transform” In *Q. J. Math.*65.1, 2014, pp. 249–266 DOI: [10.1093/qmath/has036][230]
- [661] Yannick Saouter and Herman te Riele “Improved results on the Mertens conjecture” In *Math. Comp.*83.285, 2014, pp. 421–433 DOI: [10.1090/S0025-5718-2013-02716-0][239]
- [662] D.. Best and T.. Trudgian “Linear relations of zeroes of the zeta-function” In *Math. Comp.*84.294, 2015, pp. 2047–2058 DOI: [10.1090/S0025-5718-2014-02916-5][31]
- [663] J. Büthe “On the first sign change in Mertens’ theorem” In *Acta Arith.*171.2, 2015, pp. 183–195 DOI: [10.4064/aa171-2-5][35]
- [664] D. Fiorilli “The distribution of the variance of primes in arithmetic progressions” In *Int. Math. Res. Not. IMRN*, 2015, pp. 4421–4448 DOI: [10.1093/imrn/rnu074][60]
- [665] H. Kisilevsky and M.. Rubinstein “Chebotarev sets” In *Acta Arith.*171.2, 2015, pp. 97–124 DOI: [10.4064/aa171-2-1][134]
- [666] J. Lay “Sign changes in Mertens’ first and second theorems”, 2015 URL: [https://arxiv.org/abs/1505.03589][174]
- [667] Yannick Saouter, Timothy Trudgian and Patrick Demichel “A still sharper region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*84.295, 2015, pp. 2433–2446 DOI: [10.1090/S0025-5718-2015-02930-5][240]
- [668] Gautami Bhowmik, Olivier Ramaré and Jan-Christoph Schlage–Puchta “Tauberian oscillation theorems and the distribution of Goldbach numbers” In *J. Théor. Nombres Bordeaux*28.2, 2016, pp. 291–299
- [669] B. Cha, D. Fiorilli and F. Jouve “Prime number races for elliptic curves over function fields” In *Ann. Sci. Éc. Norm. Supér. (4)*49.5, 2016, pp. 1239–1277 DOI: [10.24033/asens.2308][38]
- [670] D. Dummit, A. Granville and B. Kisilevsky “Big biases amongst products of two primes” In *Mathematika*62.2, 2016, pp. 502–507 DOI: [10.1112/S0025579315000339][53]
- [671] Y. Lamzouri “A bias in Mertens’ product formula” In *Int. J. Number Theory*12.1, 2016, pp. 97–109 DOI: [10.1142/S1793042116500068][169]
- [672] R.. Lemke and K. Soundararajan “Unexpected biases in the distribution of consecutive primes” In *Proc. Natl. Acad. Sci. USA*113.31, 2016, pp. E4446–E4454 DOI: [10.1073/pnas.1605366113][180]
- [673] D.. Platt and T.. Trudgian “On the first sign change of θ ⁡ ( x) − x \theta(x)-x ” In *Math. Comp.*85.299, 2016, pp. 1539–1547 DOI: [10.1090/mcom/3021][224]
- [674] Herman.. te Riele “The Mertens conjecture” In *The legacy of Bernhard Riemann after one hundred and fifty years. Vol. II*35.2, Adv. Lect. Math. (ALM) Int. Press, Somerville, MA, 2016, pp. 703–718
- [675] Byungchul Cha “The summatory function of the Möbius function in function fields” In *Acta Arith.*179.4, 2017, pp. 375–395 DOI: [10.4064/aa8590-1-2017][40]
- [676] Patrick Hough “A lower bound for biases amongst products of two primes” In *Res. Number Theory*3, 2017, pp. Art. 1911 DOI: [10.1007/s40993-017-0083-9][89]
- [677] X. Meng “The distribution of k k -free numbers and the derivative of the Riemann zeta-function” In *Math. Proc. Cambridge Philos. Soc.*162.2, 2017, pp. 293–317 DOI: [10.1017/S0305004116000554][190]
- [678] Michael. Mossinghoff and Timothy. Trudgian “The Liouville function and the Riemann hypothesis” In *Exploring the Riemann zeta function*Springer, Cham, 2017, pp. 201–221
- [679] Jan Büthe “An analytic method for bounding ψ ⁡ ( x) \psi(x) ” In *Math. Comp.*87.312, 2018, pp. 1991–2009 DOI: [10.1090/mcom/3264][36]
- [680] Adam. Harper and Youness Lamzouri “Orderings of weakly correlated random variables, and prime number races with many contestants” In *Probab. Theory Related Fields*170.3-4, 2018, pp. 961–1010 DOI: [10.1007/s00440-017-0800-2][82]
- [681] Greg Hurst “Computations of the Mertens function and improved bounds on the Mertens conjecture” In *Math. Comp.*87.310, 2018, pp. 1013–1028 DOI: [10.1090/mcom/3275][98]
- [682] X. Meng “Chebyshev’s bias for products of k k primes” In *Algebra Number Theory*12.2, 2018, pp. 305–341 DOI: [10.2140/ant.2018.12.305][191]
- [683] X. Meng “Large bias for integers with prime factors in arithmetic progressions” In *Mathematika*64.1, 2018, pp. 237–252
- [684] J.-C. Schlage–Puchta “Oscillations of the error term in the prime number theorem” In *Acta Math. Hungar.*156.2, 2018, pp. 303–308 DOI: [10.1007/s10474-018-0884-x][243]
- [685] Kevin Ford, Adam. Harper and Youness Lamzouri “Extreme biases in prime number races with many contestants” In *Math. Ann.*374.1-2, 2019, pp. 517–551 DOI: [10.1007/s00208-019-01810-x][67]
- [686] Peter Humphries, Snehal. Shekatkar and Tian Wong “Biases in prime factorizations and Liouville functions for arithmetic progressions” In *J. Théor. Nombres Bordeaux*31.1, 2019, pp. 1–25 URL: [http://jtnb.cedram.org/item?id=JTNB_2019__31_1_1_0][97]
- [687] Youness Lamzouri and Bruno Martin “On the race between primes with an odd versus an even sum of the last k k binary digits” In *Funct. Approx. Comment. Math.*61.1, 2019, pp. 7–25 DOI: [10.7169/facm/1687][170]
- [688] J.. Lichtman, G. Martin and C. Pomerance “Primes in prime number races” In *Proc. Amer. Math. Soc.*147.9, 2019, pp. 3743–3757
- [689] Kamalakshya Mahatab and Anirban Mukhopadhyay “Measure-theoretic aspects of oscillations of error terms” In *Acta Arith.*187.3, 2019, pp. 201–217 DOI: [10.4064/aa170126-23-4][185]
- [690] Dave Platt and Tim Trudgian “Fujii’s development on Chebyshev’s conjecture” In *Int. J. Number Theory*15.3, 2019, pp. 639–644 DOI: [10.1142/S1793042119500337][225]
- [691] Emre Alkan “Biased behavior of weighted Mertens sums” In *Int. J. Number Theory*16.3, 2020, pp. 547–577 DOI: [10.1142/S1793042120500281][5]
- [692] Lucile Devin “Chebyshev’s bias for analytic L-functions” In *Math. Proc. Cambridge Philos. Soc.*169.1, 2020, pp. 103–140 DOI: [10.1017/s0305004119000100][48]
- [693] Lucile Devin “Limiting properties of the distribution of primes in an arbitrarily large number of residue classes” In *Canad. Math. Bull.*63.4, 2020, pp. 837–849 DOI: [10.4153/s0008439520000089][49]
- [694] Robert. Lemke and Kannan Soundararajan “The distribution of consecutive prime biases and sums of sawtooth random variables” In *Math. Proc. Cambridge Philos. Soc.*168.1, 2020, pp. 149–169 DOI: [10.1017/s0305004118000592][181]
- [695] Greg Martin and Nathan Ng “Inclusive prime number races” In *Trans. Amer. Math. Soc.*373.5, 2020, pp. 3561–3607 DOI: [10.1090/tran/7996][188]
- [696] Xianchang Meng “Number of prime factors over arithmetic progressions” In *Q. J. Math.*71.1, 2020, pp. 97–121 DOI: [10.1093/qmathj/haz040][192]
- [697] Michael. Mossinghoff and Timothy. Trudgian “A tale of two omegas” In *75 years of mathematics of computation*754, Contemp. Math. Amer. Math. Soc., [Providence], RI, 2020, pp. 343–364
- [698] Roger Plymen “The Great Prime Number Race” 92, Student Mathematical Library American Mathematical Society, Providence, RI, 2020, pp. 138
- [699] Sam Porritt “Character sums over products of prime polynomials”, 2020 URL: [https://arxiv.org/abs/2003.12002][227]
- [700] Emre Alkan “Variations on criteria of Pólya and Turán for the Riemann hypothesis” In *J. Number Theory*225, 2021, pp. 90–124 DOI: [10.1016/j.jnt.2021.01.004][6]
- [701] Alexandre Bailleul “Chebyshev’s bias in dihedral and generalized quaternion Galois groups” In *Algebra Number Theory*15.4, 2021, pp. 999–1041 DOI: [10.2140/ant.2021.15.999][10]
- [702] Lucile Devin “Discrepancies in the distribution of Gaussian primes”, 2021 URL: [https://arxiv.org/abs/2105.02492][50]
- [703] Lucile Devin and Xianchang Meng “Chebyshev’s bias for products of irreducible polynomials” In *Adv. Math.*392, 2021, pp. Paper No. 10804045 DOI: [10.1016/j.aim.2021.108040][51]
- [704] Michael. Mossinghoff, Tomás Oliveira and Timothy. Trudgian “The distribution of k k -free numbers” In *Math. Comp.*90.328, 2021, pp. 907–929 DOI: [10.1090/mcom/3581][199]
- [705] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in weighted arithmetic sums” In *Int. J. Number Theory*17.7, 2021, pp. 1697–1716 DOI: [10.1142/S1793042121500561][201]
- [706] A. Shchebetov “Chebyshev’s bias visualizer”, 2021 URL: [http://math101.guru/en/downloads-2/repository/][247]
- [707] Marco Aymone “A note on prime number races and zero free regions for L L functions” In *Int. J. Number Theory*18.1, 2022, pp. 1–8 DOI: [10.1142/S1793042122500014][9]
- [708] Alexandre Bailleul “Explicit Kronecker–Weyl theorems and applications to prime number races” In *Res. Number Theory*8.3, 2022, pp. Paper No. 4334 DOI: [10.1007/s40993-022-00349-2][11]
- [709] Daniel Fiorilli and Florent Jouve “Unconditional Chebyshev biases in number fields” In *J. Éc. polytech. Math.*9, 2022, pp. 671–679 DOI: [10.5802/jep.19][61]
- [710] Shehzad Hathi and Ethan. Lee “Mertens’ third theorem for number fields: a new proof, Cramér’s inequality, oscillations, and bias”, 2022 URL: [https://arxiv.org/abs/2112.02166][84]
- [711] Winston Heap, Junxian Li and Jing Zhao “Lower bounds for discrete negative moments of the Riemann zeta function” In *Algebra Number Theory*16.7, 2022, pp. 1589–1625 DOI: [10.2140/ant.2022.16.1589][86]
- [712] Jaeyoon Kim “Prime running functions” In *Exp. Math.*31.4, 2022, pp. 1291–1313 DOI: [10.1080/10586458.2020.1786863][133]
- [713] Shin-ya Koyama and Nobushige Kurokawa “Chebyshev’s bias for Ramanujan’s τ \tau -function via the deep Riemann hypothesis” In *Proc. Japan Acad. Ser. A Math. Sci.*98.6, 2022, pp. 35–39 DOI: [10.3792/pjaa.98.007][164]
- [714] Jiawei Lin and Greg Martin “Densities in certain three-way prime number races” In *Canad. J. Math.*74.1, 2022, pp. 232–265 DOI: [10.4153/S0008414X20000747][182]
- [715] Thomas Morrill, Dave Platt and Tim Trudgian “Sign changes in the prime number theorem” In *Ramanujan J.*57.1, 2022, pp. 165–173 DOI: [10.1007/s11139-021-00398-8][198]
- [716] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in the Goldbach conjecture” In *J. Théor. Nombres Bordeaux*34.1, 2022, pp. 295–307 DOI: [10.5802/jtnb.120][202]
- [717] Youssef Sedrati “Inequities in the Shanks–Renyi prime number race over function fields” In *Mathematika*68.3, 2022, pp. 840–895 DOI: [10.1112/mtk.12150][245]
- [718] Miho Aoki and Shin-ya Koyama “Chebyshev’s bias against splitting and principal primes in global fields” In *J. Number Theory*245, 2023, pp. 233–262 DOI: [10.1016/j.jnt.2022.10.005][7]
- [719] Christian Axler “New estimates for some integrals of functions defined over primes” In *Funct. Approx. Comment. Math.*68.2, 2023, pp. 207–229 DOI: [10.7169/facm/2049][8]
- [720] Daniel Fiorilli and Greg Martin “Disproving Hooley’s conjecture” In *J. Eur. Math. Soc. (JEMS)*25.12, 2023, pp. 4791–4812 DOI: [10.4171/jems/1291][63]
- [721] Peng Gao and Liangyi Zhao “Lower bounds for negative moments of ζ ′ ​ ( ρ) \zeta^{\prime}(\rho) ” In *Mathematika*69.4, 2023, pp. 1081–1103
- [722] Ofir Gorodetsky “Sums of two squares are strongly biased towards quadratic residues” In *Algebra Number Theory*17.3, 2023, pp. 775–804 DOI: [10.2140/ant.2023.17.775][75]
- [723] Daniel Hu, Ikuya Kaneko, Spencer Martin and Carl Schildkraut “On a Mertens-type conjecture for number fields”, 2023 URL: [https://arxiv.org/abs/2109.06665][90]
- [724] Daniel. Johnston “On the average value of π ⁡ ( t) − li ⁡ ( t) \pi(t)-{\rm li}(t) ” In *Canad. Math. Bull.*66.1, 2023, pp. 185–195 DOI: [10.4153/S0008439522000212][101]
- [725] Ikuya Kaneko and Shin-ya Koyama “A new aspect of Chebyshev’s bias for elliptic curves over function fields” In *Proc. Amer. Math. Soc.*151.12, 2023, pp. 5059–5068 DOI: [10.1090/proc/16461][128]
- [726] Ikuya Kaneko, Shin-ya Koyama and Nobushige Kurokawa “Towards the Deep Riemann Hypothesis for GL n \mathrm{GL}_{n} ”, 2023 URL: [https://arxiv.org/abs/2206.02612][129]
- [727] Greg Martin, Michael Mossinghoff and Timothy Trudgian “Fake mu’s” In *Proc. Amer. Math. Soc.*151.8, 2023, pp. 3229–3244 DOI: [10.1090/proc/16186][187]
- [728] Alexandre Bailleul, Lucile Devin, Daniel Keliher and Wanlin Li “Exceptional biases in counting primes over function fields” In *J. Lond. Math. Soc. (2)*109.3, 2024, pp. Paper No. e1287632 DOI: [10.1112/jlms.12876][12]
- [729] Hung. Bui, Alexandra Florea and Micah. Milinovich “Negative discrete moments of the derivative of the Riemann zeta-function” In *Bull. Lond. Math. Soc.*56.8, 2024, pp. 2680–2703
- [730] Daniel Fiorilli and Florent Jouve “Distribution of Frobenius elements in families of Galois extensions” In *J. Inst. Math. Jussieu*23.3, 2024, pp. 1169–1258 DOI: [10.1017/S1474748023000154][62]
- [731] M. Grześkowiak, J. Kaczorowski, Ł. Pańkowski and M. Radziejewski “On the sign changes of ψ ⁡ ( x) − x \psi(x)-x ”, 2024 URL: [https://arxiv.org/abs/2408.10399][79]
- [732] Alia Hamieh, Habiba Kadiri, Greg Martin and Nathan Ng “Comparative prime number theory problem list”, 2024 URL: [https://arxiv.org/abs/2407.03530][80]
- [733] Mounir Hayani “On the influence of the Galois group structure on the Chebyshev bias in number fields”, 2024 URL: [https://arxiv.org/abs/2404.06804][85]
- [734] Arshay Sheth “Euler products at the centre and applications to Chebyshev’s bias”, 2024 URL: [https://arxiv.org/abs/2405.01512][248]

## Alphabetic bibliography

\localrefcontext

[sorting=nyt, labelprefix=A]

## References

- [735] A. Akbary, N. Ng and M. Shahabi “Limiting distributions of the classical error terms of prime number theory” In *Q. J. Math.*65.3, 2014, pp. 743–780 DOI: [10.1093/qmath/hat059][4]
- [736] Emre Alkan “Biased behavior of weighted Mertens sums” In *Int. J. Number Theory*16.3, 2020, pp. 547–577 DOI: [10.1142/S1793042120500281][5]
- [737] Emre Alkan “Variations on criteria of Pólya and Turán for the Riemann hypothesis” In *J. Number Theory*225, 2021, pp. 90–124 DOI: [10.1016/j.jnt.2021.01.004][6]
- [738] R.. Anderson and H.. Stark “Oscillation theorems” In *Analytic number theory (Philadelphia, Pa., 1980)*899, Lecture Notes in Math. Springer, Berlin-New York, 1981, pp. 79–106
- [739] Miho Aoki and Shin-ya Koyama “Chebyshev’s bias against splitting and principal primes in global fields” In *J. Number Theory*245, 2023, pp. 233–262 DOI: [10.1016/j.jnt.2022.10.005][7]
- [740] Christian Axler “New estimates for some integrals of functions defined over primes” In *Funct. Approx. Comment. Math.*68.2, 2023, pp. 207–229 DOI: [10.7169/facm/2049][8]
- [741] Marco Aymone “A note on prime number races and zero free regions for L L functions” In *Int. J. Number Theory*18.1, 2022, pp. 1–8 DOI: [10.1142/S1793042122500014][9]
- [742] Alexandre Bailleul “Chebyshev’s bias in dihedral and generalized quaternion Galois groups” In *Algebra Number Theory*15.4, 2021, pp. 999–1041 DOI: [10.2140/ant.2021.15.999][10]
- [743] Alexandre Bailleul “Explicit Kronecker–Weyl theorems and applications to prime number races” In *Res. Number Theory*8.3, 2022, pp. Paper No. 4334 DOI: [10.1007/s40993-022-00349-2][11]
- [744] Alexandre Bailleul, Lucile Devin, Daniel Keliher and Wanlin Li “Exceptional biases in counting primes over function fields” In *J. Lond. Math. Soc. (2)*109.3, 2024, pp. Paper No. e1287632 DOI: [10.1112/jlms.12876][12]
- [745] E.. Balanzario and S. Hernández “On the number of large oscillations of some arithmetical power series” In *Arch. Math. (Basel)*81.3, 2003, pp. 285–290 DOI: [10.1007/s00013-003-4704-2][13]
- [746] R. Balasubramanian, K. Ramachandra and M.. Subbarao “On the error function in the asymptotic formula for the counting function of k k -full numbers” In *Acta Arith.*50.2, 1988, pp. 107–118 DOI: [10.4064/aa-50-2-107-118][14]
- [747] K.. Bartz “On some complex explicit formulae connected with the Möbius function. I, II” In *Acta Arith.*57.4, 1991, pp. 283–293295–305 DOI: [10.4064/aa-57-4-283-293][15]
- [748] P.. Bateman, J.. Brown, R.. Hall, K.. Kloss and Rosemarie. Stemmler “Linear relations connecting the imaginary parts of the zeros of the zeta function” In *Computers in number theory (Proc. Sci. Res. Council Atlas Sympos. No. 2, Oxford, 1969)*Academic Press, London, 1971, pp. 11–19
- [749] Paul. Bateman and Emil Grosswald “On a theorem of Erdös and Szekeres” In *Illinois J. Math.*2, 1958, pp. 88–98 URL: [http://projecteuclid.org/euclid.ijm/1255380836][16]
- [750] C. Bays, K. Ford, R.. Hudson and M. Rubinstein “Zeros of Dirichlet L L -functions near the real axis and Chebyshev’s bias” In *J. Number Theory*87.1, 2001, pp. 54–76 DOI: [10.1006/jnth.2000.2601][17]
- [751] C. Bays and R.. Hudson “The segmented sieve of Eratosthenes and primes in arithmetic progressions to 10 12 10^{12} ” In *Nordisk Tidskr. Informationsbehandling (BIT)*17.2, 1977, pp. 121–127 DOI: [10.1007/bf01932283][18]
- [752] C. Bays and R.. Hudson “Details of the first region of integers x x with π 3, 2 ​ ( x) < π 3, 1 ​ ( x) \pi_{3,2}(x)<\pi_{3,1}(x) ” In *Math. Comp.*32.142, 1978, pp. 571–576 DOI: [10.2307/2006165][19]
- [753] C. Bays and R.. Hudson “Numerical and graphical description of all axis crossing regions for the moduli 4 4 and 8 8 which occur before 10 12 10^{12} ” In *Internat. J. Math. Math. Sci.*2.1, 1979, pp. 111–119 DOI: [10.1155/S0161171279000119][20]
- [754] C. Bays and R.. Hudson “Zeroes of Dirichlet L L -functions and irregularities in the distribution of primes” In *Math. Comp.*69.230, 2000, pp. 861–866 DOI: [10.1090/S0025-5718-99-01105-9][21]
- [755] Carter Bays and Richard. Hudson “On the fluctuations of Littlewood for primes of the form 4 ​ n ± 1 4n\pm 1 ” In *Math. Comp.*32.141, 1978, pp. 281–286 DOI: [10.2307/2006277][22]
- [756] Carter Bays and Richard. Hudson “The appearance of tens of billions of integers x x with π 24, 13 ​ ( x) < π 24, 1 ​ ( x) \pi_{24,13}(x)<\pi_{24,1}(x) in the vicinity of 10 12 10^{12} ” In *J. Reine Angew. Math.*299/300, 1978, pp. 234–237 DOI: [10.1515/crll.1978.299-300.234][23]
- [757] Carter Bays and Richard. Hudson “The cyclic behavior of primes in the arithmetic progressions modulo 11 11 ” In *J. Reine Angew. Math.*339, 1983, pp. 215–220 DOI: [10.1515/crll.1983.339.215][24]
- [758] Carter Bays and Richard. Hudson “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Math. Comp.*69.231, 2000, pp. 1285–1296
- [759] H.-J. Bentz “Discrepancies in the distribution of prime numbers” In *J. Number Theory*15.2, 1982, pp. 252–274 DOI: [10.1016/0022-314X(82)90030-0][25]
- [760] H.-J. Bentz and J. Pintz “Quadratic residues and the distribution of prime numbers” In *Monatsh. Math.*90.2, 1980, pp. 91–100 DOI: [10.1007/BF01303260][26]
- [761] H.-J. Bentz and J. Pintz “Über das Tschebyschef-Problem” In *Resultate Math.*5.1, 1982, pp. 1–5 DOI: [10.1007/bf03323296][27]
- [762] Hans-J. Bentz and János Pintz “Über eine Verallgemeinerung des Tschebyschef-Problems” In *Math. Z.*174.1, 1980, pp. 35–41 DOI: [10.1007/BF01215079][28]
- [763] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. I” In *J. Reine Angew. Math.*307/308, 1979, pp. 411–417 DOI: [10.1515/crll.1979.307-308.411][29]
- [764] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. II” In *J. Reine Angew. Math.*313, 1980, pp. 52–58 DOI: [10.1515/crll.1980.313.52][30]
- [765] D.. Best and T.. Trudgian “Linear relations of zeroes of the zeta-function” In *Math. Comp.*84.294, 2015, pp. 2047–2058 DOI: [10.1090/S0025-5718-2014-02916-5][31]
- [766] Gautami Bhowmik, Olivier Ramaré and Jan-Christoph Schlage–Puchta “Tauberian oscillation theorems and the distribution of Goldbach numbers” In *J. Théor. Nombres Bordeaux*28.2, 2016, pp. 291–299
- [767] Peter Borwein, Ron Ferguson and Michael. Mossinghoff “Sign changes in sums of the Liouville function” In *Math. Comp.*77.263, 2008, pp. 1681–1694 DOI: [10.1090/S0025-5718-08-02036-X][32]
- [768] R.. Brent and Jan van Lune “A note on Pólya’s observation concerning Liouville’s function” In *Herman J. J. te Riele Liber Amicorum*, CWI, 2011, pp. 92–97 URL: [https://arxiv.org/abs/1112.4911][33]
- [769] Richard. Brent “Irregularities in the distribution of primes and twin primes” Collection of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday In *Math. Comp.*29, 1975, pp. 43–56 DOI: [10.2307/2005460][34]
- [770] Hung. Bui, Alexandra Florea and Micah. Milinovich “Negative discrete moments of the derivative of the Riemann zeta-function” In *Bull. Lond. Math. Soc.*56.8, 2024, pp. 2680–2703
- [771] J. Büthe “On the first sign change in Mertens’ theorem” In *Acta Arith.*171.2, 2015, pp. 183–195 DOI: [10.4064/aa171-2-5][35]
- [772] Jan Büthe “An analytic method for bounding ψ ⁡ ( x) \psi(x) ” In *Math. Comp.*87.312, 2018, pp. 1991–2009 DOI: [10.1090/mcom/3264][36]
- [773] B Cha and B.-H. Im “Chebyshev’s bias in Galois extensions of global function fields” In *J. Number Theory*131.10, 2011, pp. 1875–1886 DOI: [10.1016/j.jnt.2011.03.011][37]
- [774] B. Cha, D. Fiorilli and F. Jouve “Prime number races for elliptic curves over function fields” In *Ann. Sci. Éc. Norm. Supér. (4)*49.5, 2016, pp. 1239–1277 DOI: [10.24033/asens.2308][38]
- [775] Byungchul Cha “Chebyshev’s bias in function fields” In *Compos. Math.*144.6, 2008, pp. 1351–1374 DOI: [10.1112/S0010437X08003631][39]
- [776] Byungchul Cha “The summatory function of the Möbius function in function fields” In *Acta Arith.*179.4, 2017, pp. 375–395 DOI: [10.4064/aa8590-1-2017][40]
- [777] Byungchul Cha and Seick Kim “Biases in the prime number race of function fields” In *J. Number Theory*130.4, 2010, pp. 1048–1055 DOI: [10.1016/j.jnt.2009.09.015][41]
- [778] Kuok Chao and Roger Plymen “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Int. J. Number Theory*6.3, 2010, pp. 681–690 DOI: [10.1142/S1793042110003125][42]
- [779] Sneha Chaubey, Melinda Lanius and Alexandru Zaharescu “Irrational factor races” In *Proc. Indian Acad. Sci. Math. Sci.*124.4, 2014, pp. 471–479 DOI: [10.1007/s12044-014-0198-z][43]
- [780] P. Chebyshev “Lettre de M. le professeur Tchébychev a M. Fuss, sur un nouveau théorème relatif aux nombres premiers contenus dans la formes 4 ​ n + 1 4n+1 et 4 ​ n + 3 4n+3 ” In *Bull. de la Classe phys. math. de l’Acad. Imp. des Sciences St. Petersburg*11, 1853, pp. 208
- [781] W… Chen “On the error term of the prime number theorem and the difference between the number of primes in the residue classes modulo 4 4 ” In *J. London Math. Soc. (2)*23.1, 1981, pp. 24–40 DOI: [10.1112/jlms/s2-23.1.24][44]
- [782] A.. Cohen and M… Mayhew “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Proc. London Math. Soc. (3)*18, 1968, pp. 691–713 DOI: [10.1112/plms/s3-18.4.691][45]
- [783] Harald Cramér “Ein Mittelwertsatz in der Primzahltheorie” In *Math. Z.*12.1, 1922, pp. 147–153 DOI: [10.1007/BF01482072][46]
- [784] S. Dancs and P. Turán “Investigations in the powersum theory. I” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*16, 1973, pp. 47–52 (1974)
- [785] Marc Deléglise, Pierre Dusart and Xavier-François Roblot “Counting primes in residue classes” In *Math. Comp.*73.247, 2004, pp. 1565–1575 DOI: [10.1090/S0025-5718-04-01649-7][47]
- [786] Lucile Devin “Chebyshev’s bias for analytic L-functions” In *Math. Proc. Cambridge Philos. Soc.*169.1, 2020, pp. 103–140 DOI: [10.1017/s0305004119000100][48]
- [787] Lucile Devin “Limiting properties of the distribution of primes in an arbitrarily large number of residue classes” In *Canad. Math. Bull.*63.4, 2020, pp. 837–849 DOI: [10.4153/s0008439520000089][49]
- [788] Lucile Devin “Discrepancies in the distribution of Gaussian primes”, 2021 URL: [https://arxiv.org/abs/2105.02492][50]
- [789] Lucile Devin and Xianchang Meng “Chebyshev’s bias for products of irreducible polynomials” In *Adv. Math.*392, 2021, pp. Paper No. 10804045 DOI: [10.1016/j.aim.2021.108040][51]
- [790] H.. Diamond “Two oscillation theorems” In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 113–118. Lecture Notes in Math.Vol. 251
- [791] H.. Diamond and J. Pintz “Oscillation of Mertens’ product formula” In *J. Théor. Nombres Bordeaux*21.3, 2009, pp. 523–533 URL: [http://jtnb.cedram.org/item?id=JTNB_2009__21_3_523_0][52]
- [792] Harold. Diamond “Changes of sign of π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Enseignement Math. (2)*21.1, 1975, pp. 1–14
- [793] D. Dummit, A. Granville and B. Kisilevsky “Big biases amongst products of two primes” In *Mathematika*62.2, 2016, pp. 502–507 DOI: [10.1112/S0025579315000339][53]
- [794] William Ellison and Fern Ellison “Prime numbers”, A Wiley-Interscience Publication John Wiley & Sons, Inc., New York; Hermann, Paris, 1985, pp. xii+417
- [795] William Ellison “Les nombres premiers” En collaboration avec Michel Mendès France; Publications de l’Institut de Mathématique de l’Université de Nancago, No. IX; Actualités Scientifiques et Industrielles, No. 1366 Hermann, Paris, 1975, pp. xiv+442
- [796] C… Evelyn and E.. Linfoot “On a problem in the additive theory of numbers” In *Ann. of Math. (2)*32.2, 1931, pp. 261–270 DOI: [10.2307/1968190][54]
- [797] A.. Fawaz “The explicit formula for L 0 ​ ( x) L_{0}(x) ” In *Proc. London Math. Soc. (3)*1, 1951, pp. 86–103 DOI: [10.1112/plms/s3-1.1.86][55]
- [798] A.. Fawaz “On an unsolved problem in the analytic theory of numbers” In *Quart. J. Math. Oxford Ser. (2)*3, 1952, pp. 282–295 DOI: [10.1093/qmath/3.1.282][56]
- [799] A. Feuerverger and G. Martin “Biases in the Shanks-Rényi prime number race” In *Experiment. Math.*9.4, 2000, pp. 535–570 URL: [http://projecteuclid.org/euclid.em/1045759521][57]
- [800] D. Fiorilli “Irrégularités dans la distribution des nombres premiers et des suites plus générales dans les progressions arithmétiques” Thesis (Ph.D.)–Université de Montréal ProQuest LLC, Ann Arbor, MI, 2011
- [801] D. Fiorilli “Elliptic curves of unbounded rank and Chebyshev’s bias” In *Int. Math. Res. Not. IMRN*, 2014, pp. 4997–5024 DOI: [10.1093/imrn/rnt103][58]
- [802] D. Fiorilli “Highly biased prime number races” In *Algebra Number Theory*8.7, 2014, pp. 1733–1767 DOI: [10.2140/ant.2014.8.1733][59]
- [803] D. Fiorilli “The distribution of the variance of primes in arithmetic progressions” In *Int. Math. Res. Not. IMRN*, 2015, pp. 4421–4448 DOI: [10.1093/imrn/rnu074][60]
- [804] D. Fiorilli and G. Martin “Inequities in the Shanks-Rényi prime number race: an asymptotic formula for the densities” In *J. Reine Angew. Math.*676, 2013, pp. 121–212
- [805] Daniel Fiorilli and Florent Jouve “Unconditional Chebyshev biases in number fields” In *J. Éc. polytech. Math.*9, 2022, pp. 671–679 DOI: [10.5802/jep.19][61]
- [806] Daniel Fiorilli and Florent Jouve “Distribution of Frobenius elements in families of Galois extensions” In *J. Inst. Math. Jussieu*23.3, 2024, pp. 1169–1258 DOI: [10.1017/S1474748023000154][62]
- [807] Daniel Fiorilli and Greg Martin “Disproving Hooley’s conjecture” In *J. Eur. Math. Soc. (JEMS)*25.12, 2023, pp. 4791–4812 DOI: [10.4171/jems/1291][63]
- [808] K. Ford and S. Konyagin “Chebyshev’s conjecture and the prime number race” In *IV International Conference “Modern Problems of Number Theory and its Applications”: Current Problems, Part II (Russian) (Tula, 2001)*Mosk. Gos. Univ. im. Lomonosova, Mekh.-Mat. Fak., Moscow, 2002, pp. 67–91
- [809] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line” In *Duke Math. J.*113.2, 2002, pp. 313–330 DOI: [10.1215/S0012-7094-02-11324-6][64]
- [810] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line. II” In *Proceedings of the Session in Analytic Number Theory and Diophantine Equations*360, Bonner Math. Schriften Univ. Bonn, Bonn, 2003, pp. 40
- [811] K. Ford, Y. Lamzouri and S. Konyagin “The prime number race and zeros of Dirichlet L L -functions off the critical line: Part III” In *Q. J. Math.*64.4, 2013, pp. 1091–1098 DOI: [10.1093/qmath/has021][65]
- [812] K. Ford and J. Sneed “Chebyshev’s bias for products of two primes” In *Experiment. Math.*19.4, 2010, pp. 385–398 DOI: [10.1080/10586458.2010.10390630][66]
- [813] Kevin Ford, Adam. Harper and Youness Lamzouri “Extreme biases in prime number races with many contestants” In *Math. Ann.*374.1-2, 2019, pp. 517–551 DOI: [10.1007/s00208-019-01810-x][67]
- [814] Kevin Ford and Richard. Hudson “Sign changes in π q, a ​ ( x) − π q, b ​ ( x) \pi_{q,a}(x)-\pi_{q,b}(x) ” In *Acta Arith.*100.4, 2001, pp. 297–314 DOI: [10.4064/aa100-4-1][68]
- [815] A. Fujii “Some generalizations of Chebyshev’s conjecture” In *Proc. Japan Acad. Ser. A Math. Sci.*64.7, 1988, pp. 260–263 URL: [http://projecteuclid.org/euclid.pja/1195513180][69]
- [816] Akio Fujii “An additive problem of prime numbers. III” In *Proc. Japan Acad. Ser. A Math. Sci.*67.8, 1991, pp. 278–283 URL: [http://projecteuclid.org/euclid.pja/1195511989][70]
- [817] P.. Gallagher “Some consequences of the Riemann hypothesis” In *Acta Arith.*37, 1980, pp. 339–343 DOI: [10.4064/aa-37-1-339-343][71]
- [818] Peng Gao and Liangyi Zhao “Lower bounds for negative moments of ζ ′ ​ ( ρ) \zeta^{\prime}(\rho) ” In *Mathematika*69.4, 2023, pp. 1081–1103
- [819] S. Gonek “The second moment of the reciprocal of the Riemann zeta function and its derivative”, 1999 URL: [https://www.slmath.org/workshops/101/schedules/25626][72]
- [820] S.. Gonek “On negative moments of the Riemann zeta-function” In *Mathematika*36.1, 1989, pp. 71–88 DOI: [10.1112/S0025579300013589][73]
- [821] I.. Good and R.. Churchhouse “The Riemann hypothesis and pseudorandom features of the Möbius sequence” In *Math. Comp.*22, 1968, pp. 857–861 DOI: [10.2307/2004584][74]
- [822] Ofir Gorodetsky “Sums of two squares are strongly biased towards quadratic residues” In *Algebra Number Theory*17.3, 2023, pp. 775–804 DOI: [10.2140/ant.2023.17.775][75]
- [823] A. Granville and G. Martin “Prime number races” In *Amer. Math. Monthly*113.1, 2006, pp. 1–33 DOI: [10.2307/27641834][76]
- [824] Emil Grosswald “On some generalizations of theorems by Landau and Pólya” In *Israel J. Math.*3, 1965, pp. 211–220 DOI: [10.1007/BF03008399][77]
- [825] Emil Grosswald “Oscillation theorems of arithmetical functions” In *Trans. Amer. Math. Soc.*126, 1967, pp. 1–28 DOI: [10.2307/1994409][78]
- [826] Emil Grosswald “Oscillation theorems” Lecture Notes in Math., Vol. 251 In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 141–168
- [827] M. Grześkowiak, J. Kaczorowski, Ł. Pańkowski and M. Radziejewski “On the sign changes of ψ ⁡ ( x) − x \psi(x)-x ”, 2024 URL: [https://arxiv.org/abs/2408.10399][79]
- [828] Hansraj Gupta “On a table of values of L ⁡ ( n) L(n) ” In *Proc. Indian Acad. Sci., Sect. A.*12, 1940, pp. 407–409
- [829] Alia Hamieh, Habiba Kadiri, Greg Martin and Nathan Ng “Comparative prime number theory problem list”, 2024 URL: [https://arxiv.org/abs/2407.03530][80]
- [830] G.. Hardy “On Dirichlet’s divisor problem” In *Proc. London Math. Soc. (2)*15, 1916, pp. 1–25 DOI: [10.1112/plms/s2-15.1.1][81]
- [831] G.. Hardy and J.. Littlewood “On an assertion of Tchebychef” In *Proc. London Math. Soc. (2)*14, 1915, pp. xv–xvi
- [832] G.. Hardy and J.. Littlewood “Contributions to the theory of the Riemann zeta-function and the theory of the distribution of primes” In *Acta Math.*41.1, 1916, pp. 119–196
- [833] Adam. Harper and Youness Lamzouri “Orderings of weakly correlated random variables, and prime number races with many contestants” In *Probab. Theory Related Fields*170.3-4, 2018, pp. 961–1010 DOI: [10.1007/s00440-017-0800-2][82]
- [834] C.. Haselgrove “A disproof of a conjecture of Pólya” In *Mathematika*5, 1958, pp. 141–145 DOI: [10.1112/S0025579300001480][83]
- [835] Shehzad Hathi and Ethan. Lee “Mertens’ third theorem for number fields: a new proof, Cramér’s inequality, oscillations, and bias”, 2022 URL: [https://arxiv.org/abs/2112.02166][84]
- [836] Mounir Hayani “On the influence of the Galois group structure on the Chebyshev bias in number fields”, 2024 URL: [https://arxiv.org/abs/2404.06804][85]
- [837] Winston Heap, Junxian Li and Jing Zhao “Lower bounds for discrete negative moments of the Riemann zeta function” In *Algebra Number Theory*16.7, 2022, pp. 1589–1625 DOI: [10.2140/ant.2022.16.1589][86]
- [838] D.. Heath-Brown “The distribution and moments of the error term in the Dirichlet divisor problem” In *Acta Arith.*60.4, 1992, pp. 389–415 DOI: [10.4064/aa-60-4-389-415][87]
- [839] Dennis. Hejhal “On the distribution of log ⁡ | ζ ′ ​ ( 1 2 + i ​ t) | \log|\zeta^{\prime}(\frac{1}{2}+it)| ” In *Number theory, trace formulas and discrete groups (Oslo, 1987)*Academic Press, Boston, MA, 1989, pp. 343–370
- [840] C. Hooley “On the Barban-Davenport-Halberstam theorem. VII” In *J. London Math. Soc. (2)*16.1, 1977, pp. 1–8 DOI: [10.1112/jlms/s2-16.1.1][88]
- [841] Patrick Hough “A lower bound for biases amongst products of two primes” In *Res. Number Theory*3, 2017, pp. Art. 1911 DOI: [10.1007/s40993-017-0083-9][89]
- [842] Daniel Hu, Ikuya Kaneko, Spencer Martin and Carl Schildkraut “On a Mertens-type conjecture for number fields”, 2023 URL: [https://arxiv.org/abs/2109.06665][90]
- [843] Richard. Hudson “A common combinatorial principle underlies Riemann’s formula, the Chebyshev phenomenon, and other subtle effects in comparative prime number theory. I” In *J. Reine Angew. Math.*313, 1980, pp. 133–150 DOI: [10.1515/crll.1980.313.133][91]
- [844] Richard. Hudson “Averaging effects on irregularities in the distribution of primes in arithmetic progressions” In *Math. Comp.*44.170, 1985, pp. 561–571 DOI: [10.2307/2007974][92]
- [845] Richard. Hudson and Carter Bays “The mean behavior of primes in arithmetic progressions” In *J. Reine Angew. Math.*296, 1977, pp. 80–99 DOI: [10.1515/crll.1977.296.80][93]
- [846] Peter Humphries “The distribution of weighted sums of the Liouville function and Pólya’s conjecture” In *J. Number Theory*133.2, 2013, pp. 545–582 DOI: [10.1016/j.jnt.2012.08.011][94]
- [847] Peter Humphries “On the Mertens conjecture for elliptic curves over finite fields” In *Bull. Aust. Math. Soc.*89.1, 2014, pp. 19–32 DOI: [10.1017/S0004972712001116][95]
- [848] Peter Humphries “On the Mertens conjecture for function fields” In *Int. J. Number Theory*10.2, 2014, pp. 341–361 DOI: [10.1142/S1793042113500978][96]
- [849] Peter Humphries, Snehal. Shekatkar and Tian Wong “Biases in prime factorizations and Liouville functions for arithmetic progressions” In *J. Théor. Nombres Bordeaux*31.1, 2019, pp. 1–25 URL: [http://jtnb.cedram.org/item?id=JTNB_2019__31_1_1_0][97]
- [850] Greg Hurst “Computations of the Mertens function and improved bounds on the Mertens conjecture” In *Math. Comp.*87.310, 2018, pp. 1013–1028 DOI: [10.1090/mcom/3275][98]
- [851] A.. Ingham “The distribution of prime numbers” Cambridge Tracts in Mathematics and Mathematical Physics. 30. London: Cambridge University Press, 1932
- [852] A.. Ingham “A note on the distribution of primes” In *Acta Arith.*1, 1936, pp. 201–211
- [853] A.. Ingham “On two conjectures in the theory of numbers” In *Amer. J. Math.*64, 1942, pp. 313–319 DOI: [10.2307/2371685][99]
- [854] A.. Ingham “The distribution of prime numbers”, Cambridge Tracts in Mathematics and Mathematical Physics, No. 30 Stechert-Hafner, Inc., New York, 1964, pp. v+114
- [855] B. Jessen and A. Wintner “Distribution functions and the Riemann zeta function” In *Trans. Amer. Math. Soc.*38.1, 1935, pp. 48–88 DOI: [10.2307/1989728][100]
- [856] Daniel. Johnston “On the average value of π ⁡ ( t) − li ⁡ ( t) \pi(t)-{\rm li}(t) ” In *Canad. Math. Bull.*66.1, 2023, pp. 185–195 DOI: [10.4153/S0008439522000212][101]
- [857] W. Jurkat and A. Peyerimhoff “A constructive approach to Kronecker approximations and its application to the Mertens conjecture” In *J. Reine Angew. Math.*286(287), 1976, pp. 322–340 DOI: [10.1515/crll.1976.286-287.322][102]
- [858] W.. Jurkat “On the Mertens conjecture and related general Ω \Omega -theorems” In *Analytic number theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972)*Amer. Math. Soc., Providence, R.I., 1973, pp. 147–158
- [859] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. I” In *Acta Arith.*44.4, 1984, pp. 365–377 DOI: [10.4064/aa-44-4-365-377][103]
- [860] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. II” In *Acta Arith.*45.1, 1985, pp. 65–74 DOI: [10.4064/aa-45-1-65-74][104]
- [861] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. III” In *Acta Arith.*48.4, 1987, pp. 347–371 DOI: [10.4064/aa-48-4-347-371][105]
- [862] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. IV” In *Acta Arith.*50.1, 1988, pp. 15–21 DOI: [10.4064/aa-50-1-15-21][106]
- [863] J. Kaczorowski “The k k -functions in multiplicative number theory. I. On complex explicit formulae” In *Acta Arith.*56.3, 1990, pp. 195–211 DOI: [10.4064/aa-56-3-195-211][107]
- [864] J. Kaczorowski “The k k -functions in multiplicative number theory. II. Uniform distribution of zeta zeros” In *Acta Arith.*56.3, 1990, pp. 213–224 DOI: [10.4064/aa-56-3-213-224][108]
- [865] J. Kaczorowski “The k k -functions in multiplicative number theory. III. Uniform distribution of zeta zeros; discrepancy” In *Acta Arith.*57.3, 1991, pp. 199–210 DOI: [10.4064/aa-57-3-199-210][109]
- [866] J. Kaczorowski “The k k -functions in multiplicative number theory. IV. On a method of A. E. Ingham” In *Acta Arith.*57.3, 1991, pp. 231–244 DOI: [10.4064/aa-57-3-231-244][110]
- [867] J. Kaczorowski “The k k -functions in multiplicative number theory. V. Changes of sign of some arithmetical error terms” In *Acta Arith.*59.1, 1991, pp. 37–58 DOI: [10.4064/aa-59-1-37-58][111]
- [868] J. Kaczorowski “A contribution to the Shanks-Rényi race problem” In *Quart. J. Math. Oxford Ser. (2)*44.176, 1993, pp. 451–458 DOI: [10.1093/qmath/44.4.451][112]
- [869] J. Kaczorowski “On the Shanks-Rényi race problem” In *Acta Arith.*74.1, 1996, pp. 31–46 DOI: [10.4064/aa-74-1-31-46][113]
- [870] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. I” In *Acta Math. Hungar.*48.1-2, 1986, pp. 173–185 DOI: [10.1007/BF01949062][114]
- [871] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. II” In *Acta Math. Hungar.*49.3-4, 1987, pp. 441–453 DOI: [10.1007/BF01951008][115]
- [872] J. Kaczorowski and W. Staś “On the number of sign changes in the remainder-term of the prime-ideal theorem” In *Colloq. Math.*56.1, 1988, pp. 185–197 DOI: [10.4064/cm-56-1-185-197][116]
- [873] Jerzy Kaczorowski “Results on the distribution of primes” In *J. Reine Angew. Math.*446, 1994, pp. 89–113 DOI: [10.1515/crll.1994.446.89][117]
- [874] Jerzy Kaczorowski “On the distribution of primes (mod 4 4)” In *Analysis*15.2, 1995, pp. 159–171 DOI: [10.1524/anly.1995.15.2.159][118]
- [875] Jerzy Kaczorowski “On the Shanks-Rényi race problem mod 5 5 ” In *J. Number Theory*50.1, 1995, pp. 106–118 DOI: [10.1006/jnth.1995.1006][119]
- [876] Jerzy Kaczorowski “Boundary values of Dirichlet series and the distribution of primes” In *European Congress of Mathematics, Vol. I (Budapest, 1996)*168, Progr. Math. Birkhäuser, Basel, 1998, pp. 237–254
- [877] Jerzy Kaczorowski “Results on the Möbius function” In *J. Lond. Math. Soc. (2)*75.2, 2007, pp. 509–521 DOI: [10.1112/jlms/jdm006][120]
- [878] Jerzy Kaczorowski “On the distribution of irreducible algebraic integers” In *Monatsh. Math.*156.1, 2009, pp. 47–71 DOI: [10.1007/s00605-008-0559-8][121]
- [879] Jerzy Kaczorowski “ Ω \Omega -estimates related to irreducible algebraic integers” In *Math. Nachr.*283.9, 2010, pp. 1291–1303 DOI: [10.1002/mana.200710158][122]
- [880] Jerzy Kaczorowski and Olivier Ramaré “Almost periodicity of some error terms in prime number theory” In *Acta Arith.*106.3, 2003, pp. 277–297 DOI: [10.4064/aa106-3-6][123]
- [881] Jerzy Kaczorowski and Włodzimierz Staś “On the number of sign-changes in the remainder-term of the prime-ideal theorem” In *Discuss. Math.*9, 1988, pp. 83–102 (1989)
- [882] Jerzy Kaczorowski and Kazimierz Wiertelak “ Ω \Omega -estimates for a class of arithmetic error terms” In *Math. Proc. Cambridge Philos. Soc.*142.3, 2007, pp. 385–394 DOI: [10.1017/S0305004107000035][124]
- [883] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of a given size of some arithmetic error terms” In *Trans. Amer. Math. Soc.*361.9, 2009, pp. 5023–5039 DOI: [10.1090/S0002-9947-09-04803-X][125]
- [884] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of the remainder term related to the Euler totient function” In *J. Number Theory*130.12, 2010, pp. 2683–2700 DOI: [10.1016/j.jnt.2010.06.010][126]
- [885] Jerzy Kaczorowski and Kazimierz Wiertelak “Smoothing arithmetic error terms: the case of the Euler ϕ \phi function” In *Math. Nachr.*283.11, 2010, pp. 1637–1645 DOI: [10.1002/mana.200810048][127]
- [886] Ikuya Kaneko and Shin-ya Koyama “A new aspect of Chebyshev’s bias for elliptic curves over function fields” In *Proc. Amer. Math. Soc.*151.12, 2023, pp. 5059–5068 DOI: [10.1090/proc/16461][128]
- [887] Ikuya Kaneko, Shin-ya Koyama and Nobushige Kurokawa “Towards the Deep Riemann Hypothesis for GL n \mathrm{GL}_{n} ”, 2023 URL: [https://arxiv.org/abs/2206.02612][129]
- [888] A.. Karatsuba “Behavior of the function R 1 ​ ( x) R_{1}(x) and of its mean value” In *Dokl. Akad. Nauk*404.4, 2005, pp. 439–442
- [889] A.. Karatsuba “On the approximation of π ⁡ ( x) \pi(x) ” In *Chebyshevskii Sb.*5.4(12), 2005, pp. 5–20
- [890] A.. Karatsuba “On the number of sign changes of the function R 1 ​ ( x) R_{1}(x) and its mean values” In *Chebyshevskii Sb.*6.2(14), 2005, pp. 163–183
- [891] I. Kátai “Eine Bemerkung zur “Comparative prime-number theory I-VIII” von S. Knapowski und P. Turán” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*7, 1964, pp. 33–40
- [892] I. Kátai “Comparative theory of prime numbers” In *Acta Math. Acad. Sci. Hungar*18, 1967, pp. 133–149 DOI: [10.1007/BF02020967][130]
- [893] I. Kátai “On investigations in the comparative prime number theory” In *Acta Math. Acad. Sci. Hungar.*18, 1967, pp. 379–391 DOI: [10.1007/BF02280297][131]
- [894] I. Kátai “On oscillations of number-theoretic functions” In *Acta Arith.*13, 1967/1968, pp. 107–122 DOI: [10.4064/aa-13-1-107-122][132]
- [895] I. Kátai “On oscillation of the number of primes in an arithmetical progression.” In *Acta Sci. Math. (Szeged)*29, 1968, pp. 271–282
- [896] Imre Kátai “The Ω \Omega -estimation of the arithmetic mean of the Möbius function” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*15, 1965, pp. 15–18
- [897] Imre Kátai “Omega-type investigations in prime number theory” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*16, 1966, pp. 369–396
- [898] Jaeyoon Kim “Prime running functions” In *Exp. Math.*31.4, 2022, pp. 1291–1313 DOI: [10.1080/10586458.2020.1786863][133]
- [899] H. Kisilevsky and M.. Rubinstein “Chebotarev sets” In *Acta Arith.*171.2, 2015, pp. 97–124 DOI: [10.4064/aa171-2-1][134]
- [900] S. Knapowski “On prime numbers in an arithmetical progression” In *Acta Arith.*4, 1958, pp. 57–70 DOI: [10.4064/aa-4-1-57-70][135]
- [901] S. Knapowski “On the Möbius function” In *Acta Arith.*4, 1958, pp. 209–216 DOI: [10.4064/aa-4-3-209-216][136]
- [902] S. Knapowski “On the mean values of certain functions in prime number theory” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 375–390. (unbound insert)
- [903] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. I” In *Acta Arith.*6, 1960/1961, pp. 415–434 DOI: [10.4064/aa-6-4-415-434][137]
- [904] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. II” In *Acta Arith*7, 1961/1962, pp. 325–335 DOI: [10.4064/aa-7-4-325-335][138]
- [905] S. Knapowski “Mean-value estimations for the Möbius function. I” In *Acta Arith.*7, 1961, pp. 121–130 DOI: [10.4064/aa-7-2-121-130][139]
- [906] S. Knapowski “Mean-value estimations for the Möbius function. II” In *Acta Arith.*7, 1961, pp. 337–343 DOI: [10.4064/aa-7-4-337-343][140]
- [907] S. Knapowski “On sign-changes in the remainder-term in the prime-number formula” In *J. London Math. Soc.*36, 1961, pp. 451–460 DOI: [10.1112/jlms/s1-36.1.451][141]
- [908] S. Knapowski “On sign-changes of the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x ” In *Acta Arith.*7, 1961/1962, pp. 107–119 DOI: [10.4064/aa-7-2-107-119][142]
- [909] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. III” In *Acta Arith*8, 1962/1963, pp. 97–105 DOI: [10.4064/aa-8-1-97-105][143]
- [910] S. Knapowski “On oscillations of certain means formed from the Möbius series. I” In *Acta Arith.*8, 1962/1963, pp. 311–320 DOI: [10.4064/aa-8-3-311-320][144]
- [911] S. Knapowski “On oscillations of certain means formed from the Möbius series. II” In *Acta Arith.*10, 1964, pp. 377–386 DOI: [10.4064/aa-10-4-377-386][145]
- [912] S. Knapowski and W. Staś “A note on a theorem of Hardy and Littlewood” In *Acta Arith.*7, 1961/1962, pp. 161–166 DOI: [10.4064/aa-7-2-161-166][146]
- [913] S. Knapowski and P. Turán “Comparative prime-number theory. I. Introduction” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 299–314 DOI: [10.1007/BF02020796][147]
- [914] S. Knapowski and P. Turán “Comparative prime-number theory. II. Comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k, l ≢ 1 {\rm mod}\ k,\,l\not\equiv 1 mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 315–342 DOI: [10.1007/BF02020797][148]
- [915] S. Knapowski and P. Turán “Comparative prime-number theory. III. Continuation of the study of comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 343–364 DOI: [10.1007/BF02020798][149]
- [916] S. Knapowski and P. Turán “Comparative prime-number theory. IV. Paradigma to the general case, k = 8 k=8 and 5 5 ” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 31–42 DOI: [10.1007/BF01901928][150]
- [917] S. Knapowski and P. Turán “Comparative prime-number theory. V. Some theorems concerning the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 43–63 DOI: [10.1007/BF01901929][151]
- [918] S. Knapowski and P. Turán “Comparative prime-number theory. VI. Continuation of the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 65–78 DOI: [10.1007/BF01901930][152]
- [919] S. Knapowski and P. Turán “Comparative prime-number theory. VII. The problem of sign-changes in the general case” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 241–250 DOI: [10.1007/BF01895712][153]
- [920] S. Knapowski and P. Turán “Comparative prime-number theory. VIII. Chebyshev’s problem for k = 8 k=8 ” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 251–268 DOI: [10.1007/BF01895713][154]
- [921] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. I” In *Acta Arith.*9, 1964, pp. 23–40 DOI: [10.4064/aa-9-1-23-40][155]
- [922] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. II. A modification of Chebyshev’s assertion” In *Acta Arith.*10, 1964, pp. 293–313 DOI: [10.4064/aa-10-3-293-313][156]
- [923] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. III” In *Acta Arith.*11, 1965, pp. 115–127 DOI: [10.4064/aa-11-1-115-127][157]
- [924] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. IV” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 147–161 DOI: [10.4064/aa-11-2-193-202][158]
- [925] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. V” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 193–202 DOI: [10.4064/aa-11-2-193-202][158]
- [926] S. Knapowski and P. Turán “On an assertion of Čebyšev” In *J. Analyse Math.*14, 1965, pp. 267–274 DOI: [10.1007/BF02806393][159]
- [927] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. VI. Accumulation theorems for residue-classes representing quadratic residues mod ​ k {\rm mod}\,k ” In *Acta Arith.*12, 1966, pp. 85–96 DOI: [10.4064/aa-12-1-85-96][160]
- [928] S. Knapowski and P. Turán “Über einige Fragen der vergleichenden Primzahltheorie” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 157–171
- [929] S. Knapowski and P. Turán “Further developments in the comparative prime number theory. VII” In *Acta Arith.*21, 1972, pp. 193–201 DOI: [10.4064/aa-21-1-193-201][161]
- [930] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). I” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 153–169. Colloq. Math. Soc. János BolyaiVol. 13
- [931] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” In *Monatsh. Math.*82.2, 1976, pp. 163–175 DOI: [10.1007/BF01305997][162]
- [932] S. Knapowski and P. Turán “On prime numbers ≡ 1 \equiv 1 resp. 3 ​ (mod 4) 3{\text{\rm\ (mod~$4$)}} ” In *Number theory and algebra*Academic Press, New York, 1977, pp. 157–165
- [933] G. Kolesnik and E.. Straus “On the sum of powers of complex numbers” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 427–442
- [934] Tadej Kotnik “The prime-counting function and its analytic approximations: π ⁡ ( x) \pi(x) and its approximations” In *Adv. Comput. Math.*29.1, 2008, pp. 55–70 DOI: [10.1007/s10444-007-9039-2][163]
- [935] Tadej Kotnik and Jan van Lune “On the order of the Mertens function” In *Experiment. Math.*13.4, 2004, pp. 473–481
- [936] Tadej Kotnik and Herman te Riele “The Mertens conjecture revisited” In *Algorithmic number theory*4076, Lecture Notes in Comput. Sci. Springer, Berlin, 2006, pp. 156–167
- [937] Emmanuel Kowalski “The large sieve, monodromy, and zeta functions of algebraic curves. II. Independence of the zeros” In *Int. Math. Res. Not. IMRN*, 2008, pp. Art. ID rnn 09157
- [938] Shin-ya Koyama and Nobushige Kurokawa “Chebyshev’s bias for Ramanujan’s τ \tau -function via the deep Riemann hypothesis” In *Proc. Japan Acad. Ser. A Math. Sci.*98.6, 2022, pp. 35–39 DOI: [10.3792/pjaa.98.007][164]
- [939] Matthias Kunik and Lutz. Lucht “Power series with the von Mangoldt function” In *Funct. Approx. Comment. Math.*47.part 1, 2012, pp. 15–33 DOI: [10.7169/facm/2012.47.1.2][165]
- [940] Y. Lamzouri “Large deviations of the limiting distribution in the Shanks–Rényi prime number race” In *Math. Proc. Cambridge Philos. Soc.*153.1, 2012, pp. 147–166 DOI: [10.1017/S030500411200014X][166]
- [941] Y. Lamzouri “The Shanks-Rényi prime number race with many contestants” In *Math. Res. Lett.*19.3, 2012, pp. 649–666 DOI: [10.4310/MRL.2012.v19.n3.a11][167]
- [942] Y. Lamzouri “Prime number races with three or more competitors” In *Math. Ann.*356.3, 2013, pp. 1117–1162 DOI: [10.1007/s00208-012-0874-1][168]
- [943] Y. Lamzouri “A bias in Mertens’ product formula” In *Int. J. Number Theory*12.1, 2016, pp. 97–109 DOI: [10.1142/S1793042116500068][169]
- [944] Youness Lamzouri and Bruno Martin “On the race between primes with an odd versus an even sum of the last k k binary digits” In *Funct. Approx. Comment. Math.*61.1, 2019, pp. 7–25 DOI: [10.7169/facm/1687][170]
- [945] E. Landau “Über einen Satz von Tschebyschef” In *Math. Ann.*61.4, 1906, pp. 527–550 DOI: [10.1007/BF01449495][171]
- [946] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” Leipzig und Berlin, B. G. Teubner, 1909, pp. xviii+pp. 1–564ix+pp. 565–961
- [947] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 1–24 DOI: [10.1007/BF01203613][172]
- [948] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 213–219 DOI: [10.1007/BF01203613][172]
- [949] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” 2d ed; With an appendix by Paul T. Bateman Chelsea Publishing Co., New York, 1953, pp. xviii+pp. 1–564ix+pp. 565–1001
- [950] Yuk-Kam Lau “On the existence of limiting distributions of some number-theoretic error terms” In *J. Number Theory*94.2, 2002, pp. 359–374 DOI: [10.1006/jnth.2001.2734][173]
- [951] J. Lay “Sign changes in Mertens’ first and second theorems”, 2015 URL: [https://arxiv.org/abs/1505.03589][174]
- [952] P. Leboeuf “Prime correlations and fluctuations” In *Ann. Henri Poincaré*4.suppl. 2, 2003, pp. S727–S752 DOI: [10.1007/s00023-003-0958-2][175]
- [953] J. Leech “Note on the distribution of prime numbers” In *J. London Math. Soc.*32, 1957, pp. 56–58 DOI: [10.1112/jlms/s1-32.1.56][176]
- [954] R.. Lehman “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Acta Arith.*11, 1966, pp. 397–410 DOI: [10.4064/aa-11-4-397-410][177]
- [955] R. Lehman “On Liouville’s function” In *Math. Comp.*14, 1960, pp. 311–320 DOI: [10.2307/2003890][178]
- [956] D.. Lehmer and S. Selberg “A sum involving the function of Möbius” In *Acta Arith.*6, 1960, pp. 111–114 DOI: [10.4064/aa-6-1-111-114][179]
- [957] R.. Lemke and K. Soundararajan “Unexpected biases in the distribution of consecutive primes” In *Proc. Natl. Acad. Sci. USA*113.31, 2016, pp. E4446–E4454 DOI: [10.1073/pnas.1605366113][180]
- [958] Robert. Lemke and Kannan Soundararajan “The distribution of consecutive prime biases and sums of sawtooth random variables” In *Math. Proc. Cambridge Philos. Soc.*168.1, 2020, pp. 149–169 DOI: [10.1017/s0305004118000592][181]
- [959] N. Levinson “On the number of sign changes of π ⁡ ( x) − li x \pi(x)-\mathop{\rm li}x ” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 171–177. Colloq. Math. Soc. János BolyaiVol. 13
- [960] J.. Lichtman, G. Martin and C. Pomerance “Primes in prime number races” In *Proc. Amer. Math. Soc.*147.9, 2019, pp. 3743–3757
- [961] Jiawei Lin and Greg Martin “Densities in certain three-way prime number races” In *Canad. J. Math.*74.1, 2022, pp. 232–265 DOI: [10.4153/S0008414X20000747][182]
- [962] J.. Littlewood “Sur la distribution des nombres premiers” In *Comptes Rendus de l’Acad. Sci. Paris*158, 1914, pp. 1869–1872
- [963] J.. Littlewood “Mathematical Notes: 3; on a Theorem Concerning the Distribution of Prime Numbers” In *J. London Math. Soc.*2.1, 1927, pp. 41–45 DOI: [10.1112/jlms/s1-2.1.41][183]
- [964] J.. Littlewood “Mathematical Notes (12): An Inequality for a Sum of Cosines” In *J. London Math. Soc.*12.3, 1937, pp. 217–221 DOI: [10.1112/jlms/s1-12.2.217][184]
- [965] Kamalakshya Mahatab and Anirban Mukhopadhyay “Measure-theoretic aspects of oscillations of error terms” In *Acta Arith.*187.3, 2019, pp. 201–217 DOI: [10.4064/aa170126-23-4][185]
- [966] E. Makai “On a minimum problem. II” In *Acta Math. Acad. Sci. Hungar.*15, 1964, pp. 63–66 DOI: [10.1007/BF01897022][186]
- [967] G. Martin “Asymmetries in the Shanks-Rényi prime number race” In *Number theory for the millennium, II (Urbana, IL, 2000)*A K Peters, Natick, MA, 2002, pp. 403–415
- [968] Greg Martin, Michael Mossinghoff and Timothy Trudgian “Fake mu’s” In *Proc. Amer. Math. Soc.*151.8, 2023, pp. 3229–3244 DOI: [10.1090/proc/16186][187]
- [969] Greg Martin and Nathan Ng “Inclusive prime number races” In *Trans. Amer. Math. Soc.*373.5, 2020, pp. 3561–3607 DOI: [10.1090/tran/7996][188]
- [970] Barry Mazur “Finding meaning in error terms” In *Bull. Amer. Math. Soc. (N.S.)*45.2, 2008, pp. 185–228 DOI: [10.1090/S0273-0979-08-01207-X][189]
- [971] X. Meng “The distribution of k k -free numbers and the derivative of the Riemann zeta-function” In *Math. Proc. Cambridge Philos. Soc.*162.2, 2017, pp. 293–317 DOI: [10.1017/S0305004116000554][190]
- [972] X. Meng “Chebyshev’s bias for products of k k primes” In *Algebra Number Theory*12.2, 2018, pp. 305–341 DOI: [10.2140/ant.2018.12.305][191]
- [973] X. Meng “Large bias for integers with prime factors in arithmetic progressions” In *Mathematika*64.1, 2018, pp. 237–252
- [974] Xianchang Meng “Number of prime factors over arithmetic progressions” In *Q. J. Math.*71.1, 2020, pp. 97–121 DOI: [10.1093/qmathj/haz040][192]
- [975] F. Mertens “Über eine zahlentheoretische Funktion” In *Sitzungsberichte Akad. Wien*106, 1897, pp. 761–830
- [976] Micah. Milinovich and Nathan Ng “A note on a conjecture of Gonek” In *Funct. Approx. Comment. Math.*46, 2012, pp. 177–187 DOI: [10.7169/facm/2012.46.2.3][193]
- [977] William Monach “Numerical Investigation of Several Problems in Number Theory” Thesis (Ph.D.)–University of Michigan) ProQuest LLC, Ann Arbor, MI, 1980 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:8106192][194]
- [978] H.. Montgomery “The zeta function and prime numbers” In *Proceedings of the Queen’s Number Theory Conference, 1979 (Kingston, Ont., 1979)*54, Queen’s Papers in Pure and Appl. Math. Queen’s Univ., Kingston, Ont., 1980, pp. 1–31
- [979] Hugh. Montgomery “Ten lectures on the interface between analytic number theory and harmonic analysis” 84, CBMS Regional Conference Series in Mathematics Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1994, pp. xiv+220 DOI: [10.1090/cbms/084][195]
- [980] Hugh. Montgomery and Ulrike.. Vorhauer “Changes of sign of the error term in the prime number theorem” In *Funct. Approx. Comment. Math.*35, 2006, pp. 235–247 DOI: [10.7169/facm/1229442626][196]
- [981] Pieter Moree “Chebyshev’s bias for composite numbers with restricted prime divisors” In *Math. Comp.*73.245, 2004, pp. 425–449 DOI: [10.1090/S0025-5718-03-01536-9][197]
- [982] Thomas Morrill, Dave Platt and Tim Trudgian “Sign changes in the prime number theorem” In *Ramanujan J.*57.1, 2022, pp. 165–173 DOI: [10.1007/s11139-021-00398-8][198]
- [983] Michael. Mossinghoff, Tomás Oliveira and Timothy. Trudgian “The distribution of k k -free numbers” In *Math. Comp.*90.328, 2021, pp. 907–929 DOI: [10.1090/mcom/3581][199]
- [984] Michael. Mossinghoff and Timothy. Trudgian “Between the problems of Pólya and Turán” In *J. Aust. Math. Soc.*93.1–2, 2012, pp. 157–171 DOI: [10.1017/S1446788712000201][200]
- [985] Michael. Mossinghoff and Timothy. Trudgian “The Liouville function and the Riemann hypothesis” In *Exploring the Riemann zeta function*Springer, Cham, 2017, pp. 201–221
- [986] Michael. Mossinghoff and Timothy. Trudgian “A tale of two omegas” In *75 years of mathematics of computation*754, Contemp. Math. Amer. Math. Soc., [Providence], RI, 2020, pp. 343–364
- [987] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in weighted arithmetic sums” In *Int. J. Number Theory*17.7, 2021, pp. 1697–1716 DOI: [10.1142/S1793042121500561][201]
- [988] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in the Goldbach conjecture” In *J. Théor. Nombres Bordeaux*34.1, 2022, pp. 295–307 DOI: [10.5802/jtnb.120][202]
- [989] Yo̵ichi Motohashi “The binary additive divisor problem” In *Ann. Sci. École Norm. Sup. (4)*27.5, 1994, pp. 529–572 URL: [http://www.numdam.org/item?id=ASENS_1994_4_27_5_529_0][203]
- [990] C. Myerscough “Application of an accurate remainder term in the calculation of residue class distributions”, 2013 URL: [https://arxiv.org/abs/1301.1434][204]
- [991] Władysław Narkiewicz “The development of prime number theory”, Springer Monographs in Mathematics Springer-Verlag, Berlin, 2000, pp. xii+448 DOI: [10.1007/978-3-662-13157-2][205]
- [992] Gerhard Neubauer “Eine empirische Untersuchung zur Mertensschen Funktion” In *Numer. Math.*5, 1963, pp. 1–13 DOI: [10.1007/BF01385874][206]
- [993] N. Ng “Limiting Distributions and Zeros of Artin L L -Functions” Thesis (Ph.D.)–University of British Columbia, 2000 URL: [http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf][207]
- [994] N. Ng “The distribution of the summatory function of the Möbius function” In *Proc. London Math. Soc. (3)*89.2, 2004, pp. 361–389 DOI: [10.1112/S0024611504014741][208]
- [995] A.. Odlyzko and H… te Riele “Disproof of the Mertens conjecture” In *J. Reine Angew. Math.*357, 1985, pp. 138–160 DOI: [10.1515/crll.1985.357.138][209]
- [996] O.. Petrushov “Asymptotic estimates of functions based on the behavior of their Laplace transforms near singular points” In *Math. Notes*93.5–6, 2013, pp. 906–916 DOI: [10.1134/S0001434613050283][210]
- [997] P. Phragmén “Sur le logarithme intégral et la fonction f ⁡ ( x) f(x) de Riemann” In *Öfversigt af Kongl. Vetenskaps–Akademiens Föhandlingar.*48, 1891, pp. 599–616
- [998] A. Piltz “Über die Häufigkeit der Primzahlen in arithmetischen Progressionen und über verwandte Gesetze” In *Habilitationsschrift, Friedrich–Schiller–Universität Jena*, 1884
- [999] J. Pintz “Bemerkungen zur Arbeit: “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” (Monatsh. Math. 82 (1976), no. 2, 163–175) von S. Knapowski und P. Turán” In *Monatsh. Math.*82.3, 1976, pp. 199–206 DOI: [10.1007/BF01526326][211]
- [1000] J. Pintz “On the remainder term of the prime number formula. III. Sign changes of π ⁡ ( x) − li ​ x \pi(x)-{\rm li}x ” In *Studia Sci. Math. Hungar.*12.3-4, 1977, pp. 345–369 (1980)
- [1001] J. Pintz “On the sign changes of π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}(x) ” In *Journées Arithmétiques de Caen (Univ. Caen, Caen, 1976)*Soc. Math. France, Paris, 1977, pp. 255–265. Astérisque No. 41–42
- [1002] J. Pintz “On the remainder term of the prime number formula. IV. Sign changes of π ⁡ ( x) − li x \pi(x)-{\mathop{\rm li}}x ” In *Studia Sci. Math. Hungar.*13.1-2, 1978, pp. 29–42 (1981)
- [1003] J. Pintz “On the remainder term of the prime number formula. I. On a problem of Littlewood” In *Acta Arith.*36.4, 1980, pp. 341–365 DOI: [10.4064/aa-36-4-341-365][212]
- [1004] J. Pintz “On the remainder term of the prime number formula. II. On a theorem of Ingham” In *Acta Arith.*37, 1980, pp. 209–220 DOI: [10.4064/aa-37-1-209-220][213]
- [1005] J. Pintz “On the remainder term of the prime number formula. V. Effective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 215–223
- [1006] J. Pintz “On the remainder term of the prime number formula. VI. Ineffective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 225–230
- [1007] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). II” In *Studia Sci. Math. Hungar.*15.4, 1980, pp. 491–496
- [1008] J. Pintz “On the sign changes of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n) ” In *Analysis*1.3, 1981, pp. 191–195 DOI: [10.1524/anly.1981.1.3.191][214]
- [1009] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). I” In *Acta Arith.*42.1, 1982, pp. 49–55 DOI: [10.4064/aa-42-1-49-55][215]
- [1010] J. Pintz “On the distribution of square-free numbers” In *J. London Math. Soc. (2)*28.3, 1983, pp. 401–405 DOI: [10.1112/jlms/s2-28.3.401][216]
- [1011] J. Pintz “Oscillatory properties of the remainder term of the prime number formula” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 551–560
- [1012] J. Pintz “On the partial sums of the Möbius function” In *Topics in classical number theory, Vol. I, II (Budapest, 1981)*34, Colloq. Math. Soc. János Bolyai North-Holland, Amsterdam, 1984, pp. 1229–1250
- [1013] J. Pintz “On the remainder term of the prime number formula and the zeros of Riemann’s zeta-function” In *Number theory, Noordwijkerhout 1983 (Noordwijkerhout, 1983)*1068, Lecture Notes in Math. Springer, Berlin, 1984, pp. 186–197
- [1014] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). III” In *Acta Arith.*43.2, 1984, pp. 105–113 DOI: [10.4064/aa-43-2-105-113][217]
- [1015] J. Pintz “An effective disproof of the Mertens conjecture” In *Astérisque*, 1987, pp. 325–333346
- [1016] J. Pintz “On an assertion of Riemann concerning the distribution of prime numbers” In *Acta Math. Hungar.*58.3-4, 1991, pp. 383–387 DOI: [10.1007/BF01903967][218]
- [1017] J. Pintz and S. Salerno “Irregularities in the distribution of primes in arithmetic progressions. II” In *Arch. Math. (Basel)*43.4, 1984, pp. 351–357 DOI: [10.1007/BF01196659][219]
- [1018] J. Pintz and S. Salerno “On the comparative theory of primes” In *Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4)*11.2, 1984, pp. 245–260 URL: [http://www.numdam.org/item?id=ASNSP_1984_4_11_2_245_0][220]
- [1019] J. Pintz and S. Salerno “Accumulation theorems for primes in arithmetic progressions” In *Acta Math. Hungar.*46.1-2, 1985, pp. 151–172 DOI: [10.1007/BF01961016][221]
- [1020] J. Pintz and S. Salerno “Some consequences of the general Riemann hypothesis in the comparative theory of primes” In *J. Number Theory*23.2, 1986, pp. 183–194 DOI: [10.1016/0022-314X(86)90088-0][222]
- [1021] János Pintz and Saverio Salerno “Irregularities in the distribution of primes in arithmetic progressions. I” In *Arch. Math. (Basel)*42.5, 1984, pp. 439–447 DOI: [10.1007/BF01190694][223]
- [1022] D.. Platt and T.. Trudgian “On the first sign change of θ ⁡ ( x) − x \theta(x)-x ” In *Math. Comp.*85.299, 2016, pp. 1539–1547 DOI: [10.1090/mcom/3021][224]
- [1023] Dave Platt and Tim Trudgian “Fujii’s development on Chebyshev’s conjecture” In *Int. J. Number Theory*15.3, 2019, pp. 639–644 DOI: [10.1142/S1793042119500337][225]
- [1024] Roger Plymen “The Great Prime Number Race” 92, Student Mathematical Library American Mathematical Society, Providence, RI, 2020, pp. 138
- [1025] G. Pólya “Verschiedene Bemerkungen zur Zahlentheorie” In *Jahresbericht der deutschen Math.–Vereinigung*28, 1919, pp. 31–40
- [1026] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahltheorie” In *Gött. Nachr.*, 1930, pp. 19–27
- [1027] G. Pólya “On polar singularities of power series and of Dirichlet series” In *Proc. London Math. Soc. (2)*33.2, 1931, pp. 85–101 DOI: [10.1112/plms/s2-33.1.85][226]
- [1028] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahlsatz” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 233–244
- [1029] Sam Porritt “Character sums over products of prime polynomials”, 2020 URL: [https://arxiv.org/abs/2003.12002][227]
- [1030] Karl Prachar “Primzahlverteilung” Springer-Verlag, Berlin-Göttingen-Heidelberg, 1957, pp. x+415 pp.
- [1031] J.-C. Puchta “On large oscillations of the remainder of the prime number theorems” In *Acta Math. Hungar.*87.3, 2000, pp. 213–227
- [1032] Maciej Radziejewski “On the distribution of algebraic numbers with prescribed factorization properties” In *Acta Arith.*116.2, 2005, pp. 153–171 DOI: [10.4064/aa116-2-4][228]
- [1033] Maciej Radziejewski “Oscillations of error terms associated with certain arithmetical functions” In *Monatsh. Math.*144.2, 2005, pp. 113–130 DOI: [10.1007/s00605-003-0147-x][229]
- [1034] Maciej Radziejewski “Oscillatory properties of real functions with weakly bounded Mellin transform” In *Q. J. Math.*65.1, 2014, pp. 249–266 DOI: [10.1093/qmath/has036][230]
- [1035] H… te Riele “Computations concerning the conjecture of Mertens” In *J. Reine Angew. Math.*311(312), 1979, pp. 356–360 DOI: [10.1515/crll.1979.311-312.356][231]
- [1036] Herman.. te Riele “On the sign of the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Math. Comp.*48.177, 1987, pp. 323–328 DOI: [10.2307/2007893][232]
- [1037] Herman.. te Riele “The Mertens conjecture” In *The legacy of Bernhard Riemann after one hundred and fifty years. Vol. II*35.2, Adv. Lect. Math. (ALM) Int. Press, Somerville, MA, 2016, pp. 703–718
- [1038] G. Robin “Sur l’ordre maximum de la fonction somme des diviseurs” In *Seminar on number theory, Paris 1981–82 (Paris, 1981/1982)*38, Progr. Math. Birkhäuser Boston, Boston, MA, 1983, pp. 233–244
- [1039] Guy Robin “Irrégularités dans la distribution des nombres premiers dans les progressions arithmétiques” In *Ann. Fac. Sci. Toulouse Math. (5)*8.2, 1986, pp. 159–173 URL: [http://www.numdam.org/item?id=AFST_1986-1987_5_8_2_159_0][233]
- [1040] J. Rosser and Lowell Schoenfeld “Approximate formulas for some functions of prime numbers” In *Illinois J. Math.*6, 1962, pp. 64–94
- [1041] M. Rubinstein and P. Sarnak “Chebyshev’s bias” In *Experiment. Math.*3.3, 1994, pp. 173–197 URL: [http://projecteuclid.org/euclid.em/1048515870][234]
- [1042] Imre. Ruzsa “Consecutive primes modulo 4” In *Indag. Math. (N.S.)*12.4, 2001, pp. 489–503 DOI: [10.1016/S0019-3577(01)80038-0][235]
- [1043] J.. Ryan “One more “many-more” assertion” In *Amer. Math. Monthly*74.1, 1967, pp. 19–24 DOI: [10.2307/2314046][236]
- [1044] Bahman Saffari “Sur la fausseté de la conjecture de Mertens. (With discussion.)” In *C. R. Acad. Sci. Paris Sér. A-B*271, 1970, pp. A1097–A1101
- [1045] A. Sankaranarayanan “On the sign changes in the remainder term of an asymptotic formula for the number of squarefree numbers” In *Arch. Math. (Basel)*60.1, 1993, pp. 51–57 DOI: [10.1007/BF01194239][237]
- [1046] Yannick Saouter and Patrick Demichel “A sharp region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*79.272, 2010, pp. 2395–2405 DOI: [10.1090/S0025-5718-10-02351-3][238]
- [1047] Yannick Saouter and Herman te Riele “Improved results on the Mertens conjecture” In *Math. Comp.*83.285, 2014, pp. 421–433 DOI: [10.1090/S0025-5718-2013-02716-0][239]
- [1048] Yannick Saouter, Timothy Trudgian and Patrick Demichel “A still sharper region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*84.295, 2015, pp. 2433–2446 DOI: [10.1090/S0025-5718-2015-02930-5][240]
- [1049] P. Sarnak “Letter to Barry Mazur on ‘Chebyshev’s bias’ for τ ⁡ ( p) \tau(p) ”, 2007 URL: [http://web.math.princeton.edu/sarnak/MazurLtrMay08.PDF][241]
- [1050] J.-C. Schlage–Puchta “Sign changes of π ⁡ ( x, q, 1) − π ⁡ ( x, q, a) \pi(x,q,1)-\pi(x,q,a) ” In *Acta Math. Hungar.*102.4, 2004, pp. 305–320 DOI: [10.1023/B:AMHU.0000024681.23784.d1][242]
- [1051] J.-C. Schlage–Puchta “Oscillations of the error term in the prime number theorem” In *Acta Math. Hungar.*156.2, 2018, pp. 303–308 DOI: [10.1007/s10474-018-0884-x][243]
- [1052] Erhard Schmidt “Über die Anzahl der Primzahlen unter gegebener Grenze” In *Math. Ann.*57.2, 1903, pp. 195–204 DOI: [10.1007/BF01444344][244]
- [1053] Youssef Sedrati “Inequities in the Shanks–Renyi prime number race over function fields” In *Mathematika*68.3, 2022, pp. 840–895 DOI: [10.1112/mtk.12150][245]
- [1054] D. Shanks “Quadratic residues and the distribution of primes” In *Math. Tables Aids Comput.*13, 1959, pp. 272–284
- [1055] Daniel Shanks and Mohan Lal “Bateman’s constants reconsidered and the distribution of cubic residues” In *Math. Comp.*26, 1972, pp. 265–285 DOI: [10.2307/2004737][246]
- [1056] A. Shchebetov “Chebyshev’s bias visualizer”, 2021 URL: [http://math101.guru/en/downloads-2/repository/][247]
- [1057] Arshay Sheth “Euler products at the centre and applications to Chebyshev’s bias”, 2024 URL: [https://arxiv.org/abs/2405.01512][248]
- [1058] S. Skewes “On the Difference π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}\,(x) (I)” In *J. London Math. Soc.*8.4, 1933, pp. 277–283 DOI: [10.1112/jlms/s1-8.4.277][249]
- [1059] S. Skewes “On the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x. II” In *Proc. London Math. Soc. (3)*5, 1955, pp. 48–70 DOI: [10.1112/plms/s3-5.1.48][250]
- [1060] J.. Sneed “Prime and quasi-prime number races” Thesis (Ph.D.)–University of Illinois at Urbana-Champaign ProQuest LLC, Ann Arbor, MI, 2009 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:3411454][251]
- [1061] Vera. Sós and P. Turán “On some new theorems in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*6, 1955, pp. 241–255 DOI: [10.1007/BF02024389][252]
- [1062] Robert Spira “Zeros of sections of the zeta function. II” In *Math. Comp.*22, 1968, pp. 163–173 DOI: [10.2307/2004774][253]
- [1063] “Stanisław Knapowski (19. V. 1931–28. IX. 1967)” In *Colloq. Math.*23, 1971, pp. 309–310
- [1064] H.. Stark “On the asymptotic density of the k k -free integers” In *Proc. Amer. Math. Soc.*17, 1966, pp. 1211–1214 DOI: [10.2307/2036123][254]
- [1065] H.. Stark “A problem in comparative prime number theory” In *Acta Arith.*18, 1971, pp. 311–320 DOI: [10.4064/aa-18-1-311-320][255]
- [1066] W. Staś “Über die Umkehrung eines Satzes von Ingham” In *Acta Arith.*6, 1960/1961, pp. 435–446 DOI: [10.4064/aa-6-4-435-446][256]
- [1067] W. Staś “Some remarks on a series of Ramanujan” In *Acta Arith.*10, 1964/1965, pp. 359–368 DOI: [10.4064/aa-10-4-359-368][257]
- [1068] W. Staś and K. Wiertelak “Further applications of Turán’s methods to the distribution of prime ideals in ideal classes (mod f f)” In *Acta Arith.*31.2, 1976, pp. 153–165 DOI: [10.4064/aa-31-2-153-165][258]
- [1069] Włodzimierz Staś “On sign-changes in the remainder term of the prime ideal formula” In *Funct. Approx. Comment. Math.*13, 1982, pp. 159–166
- [1070] S.. Stechkin and A.. Popov “Asymptotic distribution of prime numbers in the mean” In *Uspekhi Mat. Nauk*51.6(312), 1996, pp. 21–88 DOI: [10.1070/RM1996v051n06ABEH003000][259]
- [1071] J. Steinig “The changes of sign of certain arithmetical error-terms” In *Comment. Math. Helv.*44, 1969, pp. 385–400 DOI: [10.1007/BF02564539][260]
- [1072] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 0 0 bis 150000 150000 ” In *Sitzungsberichte Akad. Wiss. Wien IIa*106, 1897, pp. 835–1024
- [1073] R.. von Sterneck “Bemerkung über die Summierung einiger zahlen-theoretischen Functionen” In *Monatsh. Math. Phys.*9.1, 1898, pp. 43–45 DOI: [10.1007/BF01707854][261]
- [1074] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 150000 150000 bis 500000 500000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*110, 1901, pp. 1053–1102
- [1075] R.. von Sterneck “Die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) bis zur Grenze 5000000 5000000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*121, 1912, pp. 1083–1096
- [1076] R.. von Sterneck “Neue empirische Daten über die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) ” In *Proc. 5th International Congress of Mathematicians*1 Cambridge University Press, 1913, pp. 341–343
- [1077] T.. Stieltjes “Correspondance d’Hermite et de Stieltjes” Gauthier–Villars, Imprimeur–Libraire, Paris, 1905, pp. xxi+pp. 1–477
- [1078] Douglas. Stoll and Patrick Demichel “The impact of ζ ⁡ ( s) \zeta(s) complex zeros on π ⁡ ( x) \pi(x) for x < 10 10 13 x<10^{10^{13}} ” In *Math. Comp.*80.276, 2011, pp. 2381–2394 DOI: [10.1090/S0025-5718-2011-02477-4][262]
- [1079] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. I” In *Math. Ann.*283, 1989, pp. 139–149
- [1080] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. II” In *Math. Ann.*283, 1989, pp. 151–163
- [1081] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. III” In *Monatsh. Math.*108, 1989, pp. 325–336
- [1082] Bogdan Szydło “On oscillations in the additive divisor problem. I” In *Acta Arith.*66.1, 1994, pp. 63–69 DOI: [10.4064/aa-66-1-63-69][263]
- [1083] Minoru Tanaka “A numerical investigation on cumulative sum of the Liouville function” In *Tokyo J. Math.*3.1, 1980, pp. 187–189 DOI: [10.3836/tjm/1270216093][264]
- [1084] Minoru Tanaka “On the Möbius and allied functions” In *Tokyo J. Math.*3.2, 1980, pp. 215–218 DOI: [10.3836/tjm/1270472994][265]
- [1085] Heinrich Tietze “Einige Tabellen zur Verteilung der Primzahlen auf Untergruppen der teilerfremden Restklassen nach gegebenem Modul” In *Abh. Bayer. Akad. Wiss. Math.-Nat. Abt. (N.F.)*1944.55, 1944, pp. 31
- [1086] E.. Titchmarsh “The Theory of the Riemann Zeta-Function” Oxford, at the Clarendon Press, 1951, pp. vi+346
- [1087] E.. Titchmarsh “The theory of the Riemann zeta-function” Edited and with a preface by D. R. Heath-Brown The Clarendon Press, Oxford University Press, New York, 1986, pp. x+412
- [1088] P. Turán “On the remainder-term of the prime-number formula. II” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 155–166 DOI: [10.1007/BF02021308][266]
- [1089] P. Turán “Nachtrag zu meiner Abhandlung “On some approximative Dirichlet polynomials in the theory of zeta-function of Riemann”” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 277–298 (unbound insert) DOI: [10.1007/BF02024493][267]
- [1090] P. Turán “On some further one-sided theorems of new type in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*12, 1961, pp. 455–468 DOI: [10.1007/BF02023928][268]
- [1091] P. Turán “On a comparative theory of primes” In *Proc. Fourth All-Union Math. Congr (Leningrad, 1961) (Russian), Vol. II*Izdat. “Nauka”, Leningrad, 1964, pp. 137–142
- [1092] Paul Turán “On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann” In *Danske Vid. Selsk. Mat.-Fys. Medd.*24.17, 1948, pp. 36
- [1093] Paul Turán “On the remainder-term of the prime-number formula. I” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 48–63 DOI: [10.1007/BF02022552][269]
- [1094] Paul Turán “Eine neue Methode in der Analysis und deren Anwendungen” Akadémiai Kiadó, Budapest, 1953
- [1095] Paul Turán “Commemoration on Stanisław Knapowski” In *Colloq. Math.*23, 1971, pp. 310–318 DOI: [10.4064/cm-23-2-309-321][270]
- [1096] Paul Turán “On a new method of analysis and its applications”, Pure and Applied Mathematics (New York) John Wiley & Sons, Inc., New York, 1984, pp. xvi+584
- [1097] A. Wintner “On the asymptotic distribution of the remainder term of the prime-number theorem” In *Amer. J. Math.*57.3, 1935, pp. 534–538 DOI: [10.2307/2371183][271]
- [1098] A. Wintner “Asymptotic distributions and infinite convolutions” In *Lecture notes distributed by the Institute for Advanced Study (Princeton)*, 1938
- [1099] A. Wintner “On the distribution function of the remainder term of the prime number theorem” In *Amer. J. Math.*63, 1941, pp. 233–248 DOI: [10.2307/2371519][272]
- [1100] Aurel Wintner “A note on Mertens’ hypothesis” In *Rev. Ci. (Lima)*50, 1948, pp. 181–184
- [1101] Aurel Wintner “On the λ \lambda -variant of Mertens’ μ \mu -hypothesis” In *Amer. J. Math.*80, 1958, pp. 639–642

## References

- [1102] P. Chebyshev “Lettre de M. le professeur Tchébychev a M. Fuss, sur un nouveau théorème relatif aux nombres premiers contenus dans la formes 4 ​ n + 1 4n+1 et 4 ​ n + 3 4n+3 ” In *Bull. de la Classe phys. math. de l’Acad. Imp. des Sciences St. Petersburg*11, 1853, pp. 208
- [1103] A. Piltz “Über die Häufigkeit der Primzahlen in arithmetischen Progressionen und über verwandte Gesetze” In *Habilitationsschrift, Friedrich–Schiller–Universität Jena*, 1884
- [1104] P. Phragmén “Sur le logarithme intégral et la fonction f ⁡ ( x) f(x) de Riemann” In *Öfversigt af Kongl. Vetenskaps–Akademiens Föhandlingar.*48, 1891, pp. 599–616
- [1105] F. Mertens “Über eine zahlentheoretische Funktion” In *Sitzungsberichte Akad. Wien*106, 1897, pp. 761–830
- [1106] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 0 0 bis 150000 150000 ” In *Sitzungsberichte Akad. Wiss. Wien IIa*106, 1897, pp. 835–1024
- [1107] R.. von Sterneck “Bemerkung über die Summierung einiger zahlen-theoretischen Functionen” In *Monatsh. Math. Phys.*9.1, 1898, pp. 43–45 DOI: [10.1007/BF01707854][261]
- [1108] R.. von Sterneck “Empirische Untersuchung über den Verlauf der zahlentheoretischen Funktion σ ⁡ ( n) = ∑ x = 1 x = n μ ⁡ ( x) \sigma(n)=\sum_{x=1}^{x=n}\mu(x) im Intervalle von 150000 150000 bis 500000 500000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*110, 1901, pp. 1053–1102
- [1109] Erhard Schmidt “Über die Anzahl der Primzahlen unter gegebener Grenze” In *Math. Ann.*57.2, 1903, pp. 195–204 DOI: [10.1007/BF01444344][244]
- [1110] T.. Stieltjes “Correspondance d’Hermite et de Stieltjes” Gauthier–Villars, Imprimeur–Libraire, Paris, 1905, pp. xxi+pp. 1–477
- [1111] E. Landau “Über einen Satz von Tschebyschef” In *Math. Ann.*61.4, 1906, pp. 527–550 DOI: [10.1007/BF01449495][171]
- [1112] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” Leipzig und Berlin, B. G. Teubner, 1909, pp. xviii+pp. 1–564ix+pp. 565–961
- [1113] R.. von Sterneck “Die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) bis zur Grenze 5000000 5000000 ” In *Sitzungsberichte Kais. Akad. Wissensch. Wien IIa*121, 1912, pp. 1083–1096
- [1114] R.. von Sterneck “Neue empirische Daten über die zahlentheoretische Funktion σ ⁡ ( n) \sigma(n) ” In *Proc. 5th International Congress of Mathematicians*1 Cambridge University Press, 1913, pp. 341–343
- [1115] J.. Littlewood “Sur la distribution des nombres premiers” In *Comptes Rendus de l’Acad. Sci. Paris*158, 1914, pp. 1869–1872
- [1116] G.. Hardy and J.. Littlewood “On an assertion of Tchebychef” In *Proc. London Math. Soc. (2)*14, 1915, pp. xv–xvi
- [1117] G.. Hardy “On Dirichlet’s divisor problem” In *Proc. London Math. Soc. (2)*15, 1916, pp. 1–25 DOI: [10.1112/plms/s2-15.1.1][81]
- [1118] G.. Hardy and J.. Littlewood “Contributions to the theory of the Riemann zeta-function and the theory of the distribution of primes” In *Acta Math.*41.1, 1916, pp. 119–196
- [1119] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 1–24 DOI: [10.1007/BF01203613][172]
- [1120] E. Landau “Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie” In *Math. Z.*1.2-3, 1918, pp. 213–219 DOI: [10.1007/BF01203613][172]
- [1121] G. Pólya “Verschiedene Bemerkungen zur Zahlentheorie” In *Jahresbericht der deutschen Math.–Vereinigung*28, 1919, pp. 31–40
- [1122] Harald Cramér “Ein Mittelwertsatz in der Primzahltheorie” In *Math. Z.*12.1, 1922, pp. 147–153 DOI: [10.1007/BF01482072][46]
- [1123] J.. Littlewood “Mathematical Notes: 3; on a Theorem Concerning the Distribution of Prime Numbers” In *J. London Math. Soc.*2.1, 1927, pp. 41–45 DOI: [10.1112/jlms/s1-2.1.41][183]
- [1124] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahltheorie” In *Gött. Nachr.*, 1930, pp. 19–27
- [1125] C… Evelyn and E.. Linfoot “On a problem in the additive theory of numbers” In *Ann. of Math. (2)*32.2, 1931, pp. 261–270 DOI: [10.2307/1968190][54]
- [1126] G. Pólya “On polar singularities of power series and of Dirichlet series” In *Proc. London Math. Soc. (2)*33.2, 1931, pp. 85–101 DOI: [10.1112/plms/s2-33.1.85][226]
- [1127] A.. Ingham “The distribution of prime numbers” Cambridge Tracts in Mathematics and Mathematical Physics. 30. London: Cambridge University Press, 1932
- [1128] S. Skewes “On the Difference π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}\,(x) (I)” In *J. London Math. Soc.*8.4, 1933, pp. 277–283 DOI: [10.1112/jlms/s1-8.4.277][249]
- [1129] B. Jessen and A. Wintner “Distribution functions and the Riemann zeta function” In *Trans. Amer. Math. Soc.*38.1, 1935, pp. 48–88 DOI: [10.2307/1989728][100]
- [1130] A. Wintner “On the asymptotic distribution of the remainder term of the prime-number theorem” In *Amer. J. Math.*57.3, 1935, pp. 534–538 DOI: [10.2307/2371183][271]
- [1131] A.. Ingham “A note on the distribution of primes” In *Acta Arith.*1, 1936, pp. 201–211
- [1132] J.. Littlewood “Mathematical Notes (12): An Inequality for a Sum of Cosines” In *J. London Math. Soc.*12.3, 1937, pp. 217–221 DOI: [10.1112/jlms/s1-12.2.217][184]
- [1133] A. Wintner “Asymptotic distributions and infinite convolutions” In *Lecture notes distributed by the Institute for Advanced Study (Princeton)*, 1938
- [1134] Hansraj Gupta “On a table of values of L ⁡ ( n) L(n) ” In *Proc. Indian Acad. Sci., Sect. A.*12, 1940, pp. 407–409
- [1135] A. Wintner “On the distribution function of the remainder term of the prime number theorem” In *Amer. J. Math.*63, 1941, pp. 233–248 DOI: [10.2307/2371519][272]
- [1136] A.. Ingham “On two conjectures in the theory of numbers” In *Amer. J. Math.*64, 1942, pp. 313–319 DOI: [10.2307/2371685][99]
- [1137] Heinrich Tietze “Einige Tabellen zur Verteilung der Primzahlen auf Untergruppen der teilerfremden Restklassen nach gegebenem Modul” In *Abh. Bayer. Akad. Wiss. Math.-Nat. Abt. (N.F.)*1944.55, 1944, pp. 31
- [1138] Paul Turán “On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann” In *Danske Vid. Selsk. Mat.-Fys. Medd.*24.17, 1948, pp. 36
- [1139] Aurel Wintner “A note on Mertens’ hypothesis” In *Rev. Ci. (Lima)*50, 1948, pp. 181–184
- [1140] P. Turán “On the remainder-term of the prime-number formula. II” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 155–166 DOI: [10.1007/BF02021308][266]
- [1141] Paul Turán “On the remainder-term of the prime-number formula. I” In *Acta Math. Acad. Sci. Hungar.*1, 1950, pp. 48–63 DOI: [10.1007/BF02022552][269]
- [1142] A.. Fawaz “The explicit formula for L 0 ​ ( x) L_{0}(x) ” In *Proc. London Math. Soc. (3)*1, 1951, pp. 86–103 DOI: [10.1112/plms/s3-1.1.86][55]
- [1143] E.. Titchmarsh “The Theory of the Riemann Zeta-Function” Oxford, at the Clarendon Press, 1951, pp. vi+346
- [1144] A.. Fawaz “On an unsolved problem in the analytic theory of numbers” In *Quart. J. Math. Oxford Ser. (2)*3, 1952, pp. 282–295 DOI: [10.1093/qmath/3.1.282][56]
- [1145] E. Landau “Handbuch der Lehre von der Verteilung der Primzahlen. 2 Bände” 2d ed; With an appendix by Paul T. Bateman Chelsea Publishing Co., New York, 1953, pp. xviii+pp. 1–564ix+pp. 565–1001
- [1146] Paul Turán “Eine neue Methode in der Analysis und deren Anwendungen” Akadémiai Kiadó, Budapest, 1953
- [1147] S. Skewes “On the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x. II” In *Proc. London Math. Soc. (3)*5, 1955, pp. 48–70 DOI: [10.1112/plms/s3-5.1.48][250]
- [1148] Vera. Sós and P. Turán “On some new theorems in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*6, 1955, pp. 241–255 DOI: [10.1007/BF02024389][252]
- [1149] J. Leech “Note on the distribution of prime numbers” In *J. London Math. Soc.*32, 1957, pp. 56–58 DOI: [10.1112/jlms/s1-32.1.56][176]
- [1150] Karl Prachar “Primzahlverteilung” Springer-Verlag, Berlin-Göttingen-Heidelberg, 1957, pp. x+415 pp.
- [1151] Paul. Bateman and Emil Grosswald “On a theorem of Erdös and Szekeres” In *Illinois J. Math.*2, 1958, pp. 88–98 URL: [http://projecteuclid.org/euclid.ijm/1255380836][16]
- [1152] C.. Haselgrove “A disproof of a conjecture of Pólya” In *Mathematika*5, 1958, pp. 141–145 DOI: [10.1112/S0025579300001480][83]
- [1153] S. Knapowski “On prime numbers in an arithmetical progression” In *Acta Arith.*4, 1958, pp. 57–70 DOI: [10.4064/aa-4-1-57-70][135]
- [1154] S. Knapowski “On the Möbius function” In *Acta Arith.*4, 1958, pp. 209–216 DOI: [10.4064/aa-4-3-209-216][136]
- [1155] Aurel Wintner “On the λ \lambda -variant of Mertens’ μ \mu -hypothesis” In *Amer. J. Math.*80, 1958, pp. 639–642
- [1156] S. Knapowski “On the mean values of certain functions in prime number theory” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 375–390. (unbound insert)
- [1157] D. Shanks “Quadratic residues and the distribution of primes” In *Math. Tables Aids Comput.*13, 1959, pp. 272–284
- [1158] P. Turán “Nachtrag zu meiner Abhandlung “On some approximative Dirichlet polynomials in the theory of zeta-function of Riemann”” In *Acta Math. Acad. Sci. Hungar.*10, 1959, pp. 277–298 (unbound insert) DOI: [10.1007/BF02024493][267]
- [1159] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. I” In *Acta Arith.*6, 1960/1961, pp. 415–434 DOI: [10.4064/aa-6-4-415-434][137]
- [1160] R. Lehman “On Liouville’s function” In *Math. Comp.*14, 1960, pp. 311–320 DOI: [10.2307/2003890][178]
- [1161] D.. Lehmer and S. Selberg “A sum involving the function of Möbius” In *Acta Arith.*6, 1960, pp. 111–114 DOI: [10.4064/aa-6-1-111-114][179]
- [1162] W. Staś “Über die Umkehrung eines Satzes von Ingham” In *Acta Arith.*6, 1960/1961, pp. 435–446 DOI: [10.4064/aa-6-4-435-446][256]
- [1163] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. II” In *Acta Arith*7, 1961/1962, pp. 325–335 DOI: [10.4064/aa-7-4-325-335][138]
- [1164] S. Knapowski “Mean-value estimations for the Möbius function. I” In *Acta Arith.*7, 1961, pp. 121–130 DOI: [10.4064/aa-7-2-121-130][139]
- [1165] S. Knapowski “Mean-value estimations for the Möbius function. II” In *Acta Arith.*7, 1961, pp. 337–343 DOI: [10.4064/aa-7-4-337-343][140]
- [1166] S. Knapowski “On sign-changes in the remainder-term in the prime-number formula” In *J. London Math. Soc.*36, 1961, pp. 451–460 DOI: [10.1112/jlms/s1-36.1.451][141]
- [1167] S. Knapowski “On sign-changes of the difference π ⁡ ( x) − li ​ x \pi(x)-{\rm li}\,x ” In *Acta Arith.*7, 1961/1962, pp. 107–119 DOI: [10.4064/aa-7-2-107-119][142]
- [1168] S. Knapowski and W. Staś “A note on a theorem of Hardy and Littlewood” In *Acta Arith.*7, 1961/1962, pp. 161–166 DOI: [10.4064/aa-7-2-161-166][146]
- [1169] P. Turán “On some further one-sided theorems of new type in the theory of Diophantine approximations” In *Acta Math. Acad. Sci. Hungar.*12, 1961, pp. 455–468 DOI: [10.1007/BF02023928][268]
- [1170] S. Knapowski “Contributions to the theory of the distribution of prime numbers in arithmetical progressions. III” In *Acta Arith*8, 1962/1963, pp. 97–105 DOI: [10.4064/aa-8-1-97-105][143]
- [1171] S. Knapowski “On oscillations of certain means formed from the Möbius series. I” In *Acta Arith.*8, 1962/1963, pp. 311–320 DOI: [10.4064/aa-8-3-311-320][144]
- [1172] S. Knapowski and P. Turán “Comparative prime-number theory. I. Introduction” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 299–314 DOI: [10.1007/BF02020796][147]
- [1173] S. Knapowski and P. Turán “Comparative prime-number theory. II. Comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k, l ≢ 1 {\rm mod}\ k,\,l\not\equiv 1 mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 315–342 DOI: [10.1007/BF02020797][148]
- [1174] S. Knapowski and P. Turán “Comparative prime-number theory. III. Continuation of the study of comparison of the progressions ≡ 1 \equiv 1 mod ​ k {\rm mod}\ k and ≡ l \equiv l mod ​ k {\rm mod}\ k ” In *Acta Math. Acad. Sci. Hungar.*13, 1962, pp. 343–364 DOI: [10.1007/BF02020798][149]
- [1175] J. Rosser and Lowell Schoenfeld “Approximate formulas for some functions of prime numbers” In *Illinois J. Math.*6, 1962, pp. 64–94
- [1176] S. Knapowski and P. Turán “Comparative prime-number theory. IV. Paradigma to the general case, k = 8 k=8 and 5 5 ” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 31–42 DOI: [10.1007/BF01901928][150]
- [1177] S. Knapowski and P. Turán “Comparative prime-number theory. V. Some theorems concerning the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 43–63 DOI: [10.1007/BF01901929][151]
- [1178] S. Knapowski and P. Turán “Comparative prime-number theory. VI. Continuation of the general case” In *Acta Math. Acad. Sci. Hungar.*14, 1963, pp. 65–78 DOI: [10.1007/BF01901930][152]
- [1179] S. Knapowski and P. Turán “Comparative prime-number theory. VII. The problem of sign-changes in the general case” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 241–250 DOI: [10.1007/BF01895712][153]
- [1180] S. Knapowski and P. Turán “Comparative prime-number theory. VIII. Chebyshev’s problem for k = 8 k=8 ” In *Acta Math. Acad. Sci. Hungar*14, 1963, pp. 251–268 DOI: [10.1007/BF01895713][154]
- [1181] Gerhard Neubauer “Eine empirische Untersuchung zur Mertensschen Funktion” In *Numer. Math.*5, 1963, pp. 1–13 DOI: [10.1007/BF01385874][206]
- [1182] A.. Ingham “The distribution of prime numbers”, Cambridge Tracts in Mathematics and Mathematical Physics, No. 30 Stechert-Hafner, Inc., New York, 1964, pp. v+114
- [1183] I. Kátai “Eine Bemerkung zur “Comparative prime-number theory I-VIII” von S. Knapowski und P. Turán” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*7, 1964, pp. 33–40
- [1184] S. Knapowski “On oscillations of certain means formed from the Möbius series. II” In *Acta Arith.*10, 1964, pp. 377–386 DOI: [10.4064/aa-10-4-377-386][145]
- [1185] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. I” In *Acta Arith.*9, 1964, pp. 23–40 DOI: [10.4064/aa-9-1-23-40][155]
- [1186] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. II. A modification of Chebyshev’s assertion” In *Acta Arith.*10, 1964, pp. 293–313 DOI: [10.4064/aa-10-3-293-313][156]
- [1187] E. Makai “On a minimum problem. II” In *Acta Math. Acad. Sci. Hungar.*15, 1964, pp. 63–66 DOI: [10.1007/BF01897022][186]
- [1188] W. Staś “Some remarks on a series of Ramanujan” In *Acta Arith.*10, 1964/1965, pp. 359–368 DOI: [10.4064/aa-10-4-359-368][257]
- [1189] P. Turán “On a comparative theory of primes” In *Proc. Fourth All-Union Math. Congr (Leningrad, 1961) (Russian), Vol. II*Izdat. “Nauka”, Leningrad, 1964, pp. 137–142
- [1190] Emil Grosswald “On some generalizations of theorems by Landau and Pólya” In *Israel J. Math.*3, 1965, pp. 211–220 DOI: [10.1007/BF03008399][77]
- [1191] Imre Kátai “The Ω \Omega -estimation of the arithmetic mean of the Möbius function” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*15, 1965, pp. 15–18
- [1192] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. III” In *Acta Arith.*11, 1965, pp. 115–127 DOI: [10.4064/aa-11-1-115-127][157]
- [1193] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. IV” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 147–161 DOI: [10.4064/aa-11-2-193-202][158]
- [1194] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. V” In *Acta Arith. 11 (1965), 147-161; ibid.*11, 1965, pp. 193–202 DOI: [10.4064/aa-11-2-193-202][158]
- [1195] S. Knapowski and P. Turán “On an assertion of Čebyšev” In *J. Analyse Math.*14, 1965, pp. 267–274 DOI: [10.1007/BF02806393][159]
- [1196] Imre Kátai “Omega-type investigations in prime number theory” In *Magyar Tud. Akad. Mat. Fiz. Oszt. Közl.*16, 1966, pp. 369–396
- [1197] S. Knapowski and P. Turán “Further developments in the comparative prime-number theory. VI. Accumulation theorems for residue-classes representing quadratic residues mod ​ k {\rm mod}\,k ” In *Acta Arith.*12, 1966, pp. 85–96 DOI: [10.4064/aa-12-1-85-96][160]
- [1198] R.. Lehman “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Acta Arith.*11, 1966, pp. 397–410 DOI: [10.4064/aa-11-4-397-410][177]
- [1199] H.. Stark “On the asymptotic density of the k k -free integers” In *Proc. Amer. Math. Soc.*17, 1966, pp. 1211–1214 DOI: [10.2307/2036123][254]
- [1200] Emil Grosswald “Oscillation theorems of arithmetical functions” In *Trans. Amer. Math. Soc.*126, 1967, pp. 1–28 DOI: [10.2307/1994409][78]
- [1201] I. Kátai “Comparative theory of prime numbers” In *Acta Math. Acad. Sci. Hungar*18, 1967, pp. 133–149 DOI: [10.1007/BF02020967][130]
- [1202] I. Kátai “On investigations in the comparative prime number theory” In *Acta Math. Acad. Sci. Hungar.*18, 1967, pp. 379–391 DOI: [10.1007/BF02280297][131]
- [1203] I. Kátai “On oscillations of number-theoretic functions” In *Acta Arith.*13, 1967/1968, pp. 107–122 DOI: [10.4064/aa-13-1-107-122][132]
- [1204] J.. Ryan “One more “many-more” assertion” In *Amer. Math. Monthly*74.1, 1967, pp. 19–24 DOI: [10.2307/2314046][236]
- [1205] A.. Cohen and M… Mayhew “On the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Proc. London Math. Soc. (3)*18, 1968, pp. 691–713 DOI: [10.1112/plms/s3-18.4.691][45]
- [1206] I.. Good and R.. Churchhouse “The Riemann hypothesis and pseudorandom features of the Möbius sequence” In *Math. Comp.*22, 1968, pp. 857–861 DOI: [10.2307/2004584][74]
- [1207] I. Kátai “On oscillation of the number of primes in an arithmetical progression.” In *Acta Sci. Math. (Szeged)*29, 1968, pp. 271–282
- [1208] Robert Spira “Zeros of sections of the zeta function. II” In *Math. Comp.*22, 1968, pp. 163–173 DOI: [10.2307/2004774][253]
- [1209] S. Knapowski and P. Turán “Über einige Fragen der vergleichenden Primzahltheorie” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 157–171
- [1210] G. Pólya “Über das Vorzeichen des Restgliedes im Primzahlsatz” In *Number Theory and Analysis (Papers in Honor of Edmund Landau)*Plenum, New York, 1969, pp. 233–244
- [1211] J. Steinig “The changes of sign of certain arithmetical error-terms” In *Comment. Math. Helv.*44, 1969, pp. 385–400 DOI: [10.1007/BF02564539][260]
- [1212] Bahman Saffari “Sur la fausseté de la conjecture de Mertens. (With discussion.)” In *C. R. Acad. Sci. Paris Sér. A-B*271, 1970, pp. A1097–A1101
- [1213] P.. Bateman, J.. Brown, R.. Hall, K.. Kloss and Rosemarie. Stemmler “Linear relations connecting the imaginary parts of the zeros of the zeta function” In *Computers in number theory (Proc. Sci. Res. Council Atlas Sympos. No. 2, Oxford, 1969)*Academic Press, London, 1971, pp. 11–19
- [1214] “Stanisław Knapowski (19. V. 1931–28. IX. 1967)” In *Colloq. Math.*23, 1971, pp. 309–310
- [1215] H.. Stark “A problem in comparative prime number theory” In *Acta Arith.*18, 1971, pp. 311–320 DOI: [10.4064/aa-18-1-311-320][255]
- [1216] Paul Turán “Commemoration on Stanisław Knapowski” In *Colloq. Math.*23, 1971, pp. 310–318 DOI: [10.4064/cm-23-2-309-321][270]
- [1217] H.. Diamond “Two oscillation theorems” In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 113–118. Lecture Notes in Math.Vol. 251
- [1218] Emil Grosswald “Oscillation theorems” Lecture Notes in Math., Vol. 251 In *The theory of arithmetic functions (Proc. Conf., Western Michigan Univ., Kalamazoo, Mich., 1971)*Springer, Berlin, 1972, pp. 141–168
- [1219] S. Knapowski and P. Turán “Further developments in the comparative prime number theory. VII” In *Acta Arith.*21, 1972, pp. 193–201 DOI: [10.4064/aa-21-1-193-201][161]
- [1220] Daniel Shanks and Mohan Lal “Bateman’s constants reconsidered and the distribution of cubic residues” In *Math. Comp.*26, 1972, pp. 265–285 DOI: [10.2307/2004737][246]
- [1221] S. Dancs and P. Turán “Investigations in the powersum theory. I” In *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*16, 1973, pp. 47–52 (1974)
- [1222] W.. Jurkat “On the Mertens conjecture and related general Ω \Omega -theorems” In *Analytic number theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972)*Amer. Math. Soc., Providence, R.I., 1973, pp. 147–158
- [1223] Richard. Brent “Irregularities in the distribution of primes and twin primes” Collection of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday In *Math. Comp.*29, 1975, pp. 43–56 DOI: [10.2307/2005460][34]
- [1224] Harold. Diamond “Changes of sign of π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Enseignement Math. (2)*21.1, 1975, pp. 1–14
- [1225] William Ellison “Les nombres premiers” En collaboration avec Michel Mendès France; Publications de l’Institut de Mathématique de l’Université de Nancago, No. IX; Actualités Scientifiques et Industrielles, No. 1366 Hermann, Paris, 1975, pp. xiv+442
- [1226] W. Jurkat and A. Peyerimhoff “A constructive approach to Kronecker approximations and its application to the Mertens conjecture” In *J. Reine Angew. Math.*286(287), 1976, pp. 322–340 DOI: [10.1515/crll.1976.286-287.322][102]
- [1227] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). I” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 153–169. Colloq. Math. Soc. János BolyaiVol. 13
- [1228] S. Knapowski and P. Turán “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” In *Monatsh. Math.*82.2, 1976, pp. 163–175 DOI: [10.1007/BF01305997][162]
- [1229] N. Levinson “On the number of sign changes of π ⁡ ( x) − li x \pi(x)-\mathop{\rm li}x ” In *Topics in number theory (Proc. Colloq., Debrecen, 1974)*North-Holland, Amsterdam, 1976, pp. 171–177. Colloq. Math. Soc. János BolyaiVol. 13
- [1230] J. Pintz “Bemerkungen zur Arbeit: “On the sign changes of ( π ⁡ ( x) − li ​ x) (\pi(x)-{\rm li}\ x). II” (Monatsh. Math. 82 (1976), no. 2, 163–175) von S. Knapowski und P. Turán” In *Monatsh. Math.*82.3, 1976, pp. 199–206 DOI: [10.1007/BF01526326][211]
- [1231] W. Staś and K. Wiertelak “Further applications of Turán’s methods to the distribution of prime ideals in ideal classes (mod f f)” In *Acta Arith.*31.2, 1976, pp. 153–165 DOI: [10.4064/aa-31-2-153-165][258]
- [1232] C. Bays and R.. Hudson “The segmented sieve of Eratosthenes and primes in arithmetic progressions to 10 12 10^{12} ” In *Nordisk Tidskr. Informationsbehandling (BIT)*17.2, 1977, pp. 121–127 DOI: [10.1007/bf01932283][18]
- [1233] C. Hooley “On the Barban-Davenport-Halberstam theorem. VII” In *J. London Math. Soc. (2)*16.1, 1977, pp. 1–8 DOI: [10.1112/jlms/s2-16.1.1][88]
- [1234] Richard. Hudson and Carter Bays “The mean behavior of primes in arithmetic progressions” In *J. Reine Angew. Math.*296, 1977, pp. 80–99 DOI: [10.1515/crll.1977.296.80][93]
- [1235] S. Knapowski and P. Turán “On prime numbers ≡ 1 \equiv 1 resp. 3 ​ (mod 4) 3{\text{\rm\ (mod~$4$)}} ” In *Number theory and algebra*Academic Press, New York, 1977, pp. 157–165
- [1236] J. Pintz “On the remainder term of the prime number formula. III. Sign changes of π ⁡ ( x) − li ​ x \pi(x)-{\rm li}x ” In *Studia Sci. Math. Hungar.*12.3-4, 1977, pp. 345–369 (1980)
- [1237] J. Pintz “On the sign changes of π ⁡ ( x) − li ⁡ ( x) \pi(x)-{\rm li}(x) ” In *Journées Arithmétiques de Caen (Univ. Caen, Caen, 1976)*Soc. Math. France, Paris, 1977, pp. 255–265. Astérisque No. 41–42
- [1238] C. Bays and R.. Hudson “Details of the first region of integers x x with π 3, 2 ​ ( x) < π 3, 1 ​ ( x) \pi_{3,2}(x)<\pi_{3,1}(x) ” In *Math. Comp.*32.142, 1978, pp. 571–576 DOI: [10.2307/2006165][19]
- [1239] Carter Bays and Richard. Hudson “On the fluctuations of Littlewood for primes of the form 4 ​ n ± 1 4n\pm 1 ” In *Math. Comp.*32.141, 1978, pp. 281–286 DOI: [10.2307/2006277][22]
- [1240] Carter Bays and Richard. Hudson “The appearance of tens of billions of integers x x with π 24, 13 ​ ( x) < π 24, 1 ​ ( x) \pi_{24,13}(x)<\pi_{24,1}(x) in the vicinity of 10 12 10^{12} ” In *J. Reine Angew. Math.*299/300, 1978, pp. 234–237 DOI: [10.1515/crll.1978.299-300.234][23]
- [1241] J. Pintz “On the remainder term of the prime number formula. IV. Sign changes of π ⁡ ( x) − li x \pi(x)-{\mathop{\rm li}}x ” In *Studia Sci. Math. Hungar.*13.1-2, 1978, pp. 29–42 (1981)
- [1242] C. Bays and R.. Hudson “Numerical and graphical description of all axis crossing regions for the moduli 4 4 and 8 8 which occur before 10 12 10^{12} ” In *Internat. J. Math. Math. Sci.*2.1, 1979, pp. 111–119 DOI: [10.1155/S0161171279000119][20]
- [1243] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. I” In *J. Reine Angew. Math.*307/308, 1979, pp. 411–417 DOI: [10.1515/crll.1979.307-308.411][29]
- [1244] H… te Riele “Computations concerning the conjecture of Mertens” In *J. Reine Angew. Math.*311(312), 1979, pp. 356–360 DOI: [10.1515/crll.1979.311-312.356][231]
- [1245] H.-J. Bentz and J. Pintz “Quadratic residues and the distribution of prime numbers” In *Monatsh. Math.*90.2, 1980, pp. 91–100 DOI: [10.1007/BF01303260][26]
- [1246] Hans-J. Bentz and János Pintz “Über eine Verallgemeinerung des Tschebyschef-Problems” In *Math. Z.*174.1, 1980, pp. 35–41 DOI: [10.1007/BF01215079][28]
- [1247] H.-J. Besenfelder “Über eine Vermutung von Tschebyschef. II” In *J. Reine Angew. Math.*313, 1980, pp. 52–58 DOI: [10.1515/crll.1980.313.52][30]
- [1248] P.. Gallagher “Some consequences of the Riemann hypothesis” In *Acta Arith.*37, 1980, pp. 339–343 DOI: [10.4064/aa-37-1-339-343][71]
- [1249] Richard. Hudson “A common combinatorial principle underlies Riemann’s formula, the Chebyshev phenomenon, and other subtle effects in comparative prime number theory. I” In *J. Reine Angew. Math.*313, 1980, pp. 133–150 DOI: [10.1515/crll.1980.313.133][91]
- [1250] William Monach “Numerical Investigation of Several Problems in Number Theory” Thesis (Ph.D.)–University of Michigan) ProQuest LLC, Ann Arbor, MI, 1980 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:8106192][194]
- [1251] H.. Montgomery “The zeta function and prime numbers” In *Proceedings of the Queen’s Number Theory Conference, 1979 (Kingston, Ont., 1979)*54, Queen’s Papers in Pure and Appl. Math. Queen’s Univ., Kingston, Ont., 1980, pp. 1–31
- [1252] J. Pintz “On the remainder term of the prime number formula. I. On a problem of Littlewood” In *Acta Arith.*36.4, 1980, pp. 341–365 DOI: [10.4064/aa-36-4-341-365][212]
- [1253] J. Pintz “On the remainder term of the prime number formula. II. On a theorem of Ingham” In *Acta Arith.*37, 1980, pp. 209–220 DOI: [10.4064/aa-37-1-209-220][213]
- [1254] J. Pintz “On the remainder term of the prime number formula. V. Effective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 215–223
- [1255] J. Pintz “On the remainder term of the prime number formula. VI. Ineffective mean value theorems” In *Studia Sci. Math. Hungar.*15.1-3, 1980, pp. 225–230
- [1256] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). II” In *Studia Sci. Math. Hungar.*15.4, 1980, pp. 491–496
- [1257] Minoru Tanaka “A numerical investigation on cumulative sum of the Liouville function” In *Tokyo J. Math.*3.1, 1980, pp. 187–189 DOI: [10.3836/tjm/1270216093][264]
- [1258] Minoru Tanaka “On the Möbius and allied functions” In *Tokyo J. Math.*3.2, 1980, pp. 215–218 DOI: [10.3836/tjm/1270472994][265]
- [1259] R.. Anderson and H.. Stark “Oscillation theorems” In *Analytic number theory (Philadelphia, Pa., 1980)*899, Lecture Notes in Math. Springer, Berlin-New York, 1981, pp. 79–106
- [1260] W… Chen “On the error term of the prime number theorem and the difference between the number of primes in the residue classes modulo 4 4 ” In *J. London Math. Soc. (2)*23.1, 1981, pp. 24–40 DOI: [10.1112/jlms/s2-23.1.24][44]
- [1261] J. Pintz “On the sign changes of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n) ” In *Analysis*1.3, 1981, pp. 191–195 DOI: [10.1524/anly.1981.1.3.191][214]
- [1262] H.-J. Bentz “Discrepancies in the distribution of prime numbers” In *J. Number Theory*15.2, 1982, pp. 252–274 DOI: [10.1016/0022-314X(82)90030-0][25]
- [1263] H.-J. Bentz and J. Pintz “Über das Tschebyschef-Problem” In *Resultate Math.*5.1, 1982, pp. 1–5 DOI: [10.1007/bf03323296][27]
- [1264] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). I” In *Acta Arith.*42.1, 1982, pp. 49–55 DOI: [10.4064/aa-42-1-49-55][215]
- [1265] Włodzimierz Staś “On sign-changes in the remainder term of the prime ideal formula” In *Funct. Approx. Comment. Math.*13, 1982, pp. 159–166
- [1266] Carter Bays and Richard. Hudson “The cyclic behavior of primes in the arithmetic progressions modulo 11 11 ” In *J. Reine Angew. Math.*339, 1983, pp. 215–220 DOI: [10.1515/crll.1983.339.215][24]
- [1267] G. Kolesnik and E.. Straus “On the sum of powers of complex numbers” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 427–442
- [1268] J. Pintz “On the distribution of square-free numbers” In *J. London Math. Soc. (2)*28.3, 1983, pp. 401–405 DOI: [10.1112/jlms/s2-28.3.401][216]
- [1269] J. Pintz “Oscillatory properties of the remainder term of the prime number formula” In *Studies in pure mathematics*Birkhäuser, Basel, 1983, pp. 551–560
- [1270] G. Robin “Sur l’ordre maximum de la fonction somme des diviseurs” In *Seminar on number theory, Paris 1981–82 (Paris, 1981/1982)*38, Progr. Math. Birkhäuser Boston, Boston, MA, 1983, pp. 233–244
- [1271] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. I” In *Acta Arith.*44.4, 1984, pp. 365–377 DOI: [10.4064/aa-44-4-365-377][103]
- [1272] J. Pintz “On the partial sums of the Möbius function” In *Topics in classical number theory, Vol. I, II (Budapest, 1981)*34, Colloq. Math. Soc. János Bolyai North-Holland, Amsterdam, 1984, pp. 1229–1250
- [1273] J. Pintz “On the remainder term of the prime number formula and the zeros of Riemann’s zeta-function” In *Number theory, Noordwijkerhout 1983 (Noordwijkerhout, 1983)*1068, Lecture Notes in Math. Springer, Berlin, 1984, pp. 186–197
- [1274] J. Pintz “Oscillatory properties of M ⁡ ( x) = ∑ n ≤ x μ ⁡ ( n) M(x)=\sum_{n\leq x}\mu(n). III” In *Acta Arith.*43.2, 1984, pp. 105–113 DOI: [10.4064/aa-43-2-105-113][217]
- [1275] J. Pintz and S. Salerno “Irregularities in the distribution of primes in arithmetic progressions. II” In *Arch. Math. (Basel)*43.4, 1984, pp. 351–357 DOI: [10.1007/BF01196659][219]
- [1276] J. Pintz and S. Salerno “On the comparative theory of primes” In *Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4)*11.2, 1984, pp. 245–260 URL: [http://www.numdam.org/item?id=ASNSP_1984_4_11_2_245_0][220]
- [1277] János Pintz and Saverio Salerno “Irregularities in the distribution of primes in arithmetic progressions. I” In *Arch. Math. (Basel)*42.5, 1984, pp. 439–447 DOI: [10.1007/BF01190694][223]
- [1278] Paul Turán “On a new method of analysis and its applications”, Pure and Applied Mathematics (New York) John Wiley & Sons, Inc., New York, 1984, pp. xvi+584
- [1279] William Ellison and Fern Ellison “Prime numbers”, A Wiley-Interscience Publication John Wiley & Sons, Inc., New York; Hermann, Paris, 1985, pp. xii+417
- [1280] Richard. Hudson “Averaging effects on irregularities in the distribution of primes in arithmetic progressions” In *Math. Comp.*44.170, 1985, pp. 561–571 DOI: [10.2307/2007974][92]
- [1281] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. II” In *Acta Arith.*45.1, 1985, pp. 65–74 DOI: [10.4064/aa-45-1-65-74][104]
- [1282] A.. Odlyzko and H… te Riele “Disproof of the Mertens conjecture” In *J. Reine Angew. Math.*357, 1985, pp. 138–160 DOI: [10.1515/crll.1985.357.138][209]
- [1283] J. Pintz and S. Salerno “Accumulation theorems for primes in arithmetic progressions” In *Acta Math. Hungar.*46.1-2, 1985, pp. 151–172 DOI: [10.1007/BF01961016][221]
- [1284] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. I” In *Acta Math. Hungar.*48.1-2, 1986, pp. 173–185 DOI: [10.1007/BF01949062][114]
- [1285] J. Pintz and S. Salerno “Some consequences of the general Riemann hypothesis in the comparative theory of primes” In *J. Number Theory*23.2, 1986, pp. 183–194 DOI: [10.1016/0022-314X(86)90088-0][222]
- [1286] Guy Robin “Irrégularités dans la distribution des nombres premiers dans les progressions arithmétiques” In *Ann. Fac. Sci. Toulouse Math. (5)*8.2, 1986, pp. 159–173 URL: [http://www.numdam.org/item?id=AFST_1986-1987_5_8_2_159_0][233]
- [1287] E.. Titchmarsh “The theory of the Riemann zeta-function” Edited and with a preface by D. R. Heath-Brown The Clarendon Press, Oxford University Press, New York, 1986, pp. x+412
- [1288] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. III” In *Acta Arith.*48.4, 1987, pp. 347–371 DOI: [10.4064/aa-48-4-347-371][105]
- [1289] J. Kaczorowski and J. Pintz “Oscillatory properties of arithmetical functions. II” In *Acta Math. Hungar.*49.3-4, 1987, pp. 441–453 DOI: [10.1007/BF01951008][115]
- [1290] J. Pintz “An effective disproof of the Mertens conjecture” In *Astérisque*, 1987, pp. 325–333346
- [1291] Herman.. te Riele “On the sign of the difference π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) ” In *Math. Comp.*48.177, 1987, pp. 323–328 DOI: [10.2307/2007893][232]
- [1292] R. Balasubramanian, K. Ramachandra and M.. Subbarao “On the error function in the asymptotic formula for the counting function of k k -full numbers” In *Acta Arith.*50.2, 1988, pp. 107–118 DOI: [10.4064/aa-50-2-107-118][14]
- [1293] A. Fujii “Some generalizations of Chebyshev’s conjecture” In *Proc. Japan Acad. Ser. A Math. Sci.*64.7, 1988, pp. 260–263 URL: [http://projecteuclid.org/euclid.pja/1195513180][69]
- [1294] J. Kaczorowski “On sign-changes in the remainder-term of the prime-number formula. IV” In *Acta Arith.*50.1, 1988, pp. 15–21 DOI: [10.4064/aa-50-1-15-21][106]
- [1295] J. Kaczorowski and W. Staś “On the number of sign changes in the remainder-term of the prime-ideal theorem” In *Colloq. Math.*56.1, 1988, pp. 185–197 DOI: [10.4064/cm-56-1-185-197][116]
- [1296] Jerzy Kaczorowski and Włodzimierz Staś “On the number of sign-changes in the remainder-term of the prime-ideal theorem” In *Discuss. Math.*9, 1988, pp. 83–102 (1989)
- [1297] S.. Gonek “On negative moments of the Riemann zeta-function” In *Mathematika*36.1, 1989, pp. 71–88 DOI: [10.1112/S0025579300013589][73]
- [1298] Dennis. Hejhal “On the distribution of log ⁡ | ζ ′ ​ ( 1 2 + i ​ t) | \log|\zeta^{\prime}(\frac{1}{2}+it)| ” In *Number theory, trace formulas and discrete groups (Oslo, 1987)*Academic Press, Boston, MA, 1989, pp. 343–370
- [1299] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. I” In *Math. Ann.*283, 1989, pp. 139–149
- [1300] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. II” In *Math. Ann.*283, 1989, pp. 151–163
- [1301] B. Szydło “Über Vorzeichenwechsel einiger arithmetischer Funktionen. III” In *Monatsh. Math.*108, 1989, pp. 325–336
- [1302] J. Kaczorowski “The k k -functions in multiplicative number theory. I. On complex explicit formulae” In *Acta Arith.*56.3, 1990, pp. 195–211 DOI: [10.4064/aa-56-3-195-211][107]
- [1303] J. Kaczorowski “The k k -functions in multiplicative number theory. II. Uniform distribution of zeta zeros” In *Acta Arith.*56.3, 1990, pp. 213–224 DOI: [10.4064/aa-56-3-213-224][108]
- [1304] K.. Bartz “On some complex explicit formulae connected with the Möbius function. I, II” In *Acta Arith.*57.4, 1991, pp. 283–293295–305 DOI: [10.4064/aa-57-4-283-293][15]
- [1305] Akio Fujii “An additive problem of prime numbers. III” In *Proc. Japan Acad. Ser. A Math. Sci.*67.8, 1991, pp. 278–283 URL: [http://projecteuclid.org/euclid.pja/1195511989][70]
- [1306] J. Kaczorowski “The k k -functions in multiplicative number theory. III. Uniform distribution of zeta zeros; discrepancy” In *Acta Arith.*57.3, 1991, pp. 199–210 DOI: [10.4064/aa-57-3-199-210][109]
- [1307] J. Kaczorowski “The k k -functions in multiplicative number theory. IV. On a method of A. E. Ingham” In *Acta Arith.*57.3, 1991, pp. 231–244 DOI: [10.4064/aa-57-3-231-244][110]
- [1308] J. Kaczorowski “The k k -functions in multiplicative number theory. V. Changes of sign of some arithmetical error terms” In *Acta Arith.*59.1, 1991, pp. 37–58 DOI: [10.4064/aa-59-1-37-58][111]
- [1309] J. Pintz “On an assertion of Riemann concerning the distribution of prime numbers” In *Acta Math. Hungar.*58.3-4, 1991, pp. 383–387 DOI: [10.1007/BF01903967][218]
- [1310] D.. Heath-Brown “The distribution and moments of the error term in the Dirichlet divisor problem” In *Acta Arith.*60.4, 1992, pp. 389–415 DOI: [10.4064/aa-60-4-389-415][87]
- [1311] J. Kaczorowski “A contribution to the Shanks-Rényi race problem” In *Quart. J. Math. Oxford Ser. (2)*44.176, 1993, pp. 451–458 DOI: [10.1093/qmath/44.4.451][112]
- [1312] A. Sankaranarayanan “On the sign changes in the remainder term of an asymptotic formula for the number of squarefree numbers” In *Arch. Math. (Basel)*60.1, 1993, pp. 51–57 DOI: [10.1007/BF01194239][237]
- [1313] Jerzy Kaczorowski “Results on the distribution of primes” In *J. Reine Angew. Math.*446, 1994, pp. 89–113 DOI: [10.1515/crll.1994.446.89][117]
- [1314] Hugh. Montgomery “Ten lectures on the interface between analytic number theory and harmonic analysis” 84, CBMS Regional Conference Series in Mathematics Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1994, pp. xiv+220 DOI: [10.1090/cbms/084][195]
- [1315] Yo̵ichi Motohashi “The binary additive divisor problem” In *Ann. Sci. École Norm. Sup. (4)*27.5, 1994, pp. 529–572 URL: [http://www.numdam.org/item?id=ASENS_1994_4_27_5_529_0][203]
- [1316] M. Rubinstein and P. Sarnak “Chebyshev’s bias” In *Experiment. Math.*3.3, 1994, pp. 173–197 URL: [http://projecteuclid.org/euclid.em/1048515870][234]
- [1317] Bogdan Szydło “On oscillations in the additive divisor problem. I” In *Acta Arith.*66.1, 1994, pp. 63–69 DOI: [10.4064/aa-66-1-63-69][263]
- [1318] Jerzy Kaczorowski “On the distribution of primes (mod 4 4)” In *Analysis*15.2, 1995, pp. 159–171 DOI: [10.1524/anly.1995.15.2.159][118]
- [1319] Jerzy Kaczorowski “On the Shanks-Rényi race problem mod 5 5 ” In *J. Number Theory*50.1, 1995, pp. 106–118 DOI: [10.1006/jnth.1995.1006][119]
- [1320] J. Kaczorowski “On the Shanks-Rényi race problem” In *Acta Arith.*74.1, 1996, pp. 31–46 DOI: [10.4064/aa-74-1-31-46][113]
- [1321] S.. Stechkin and A.. Popov “Asymptotic distribution of prime numbers in the mean” In *Uspekhi Mat. Nauk*51.6(312), 1996, pp. 21–88 DOI: [10.1070/RM1996v051n06ABEH003000][259]
- [1322] Jerzy Kaczorowski “Boundary values of Dirichlet series and the distribution of primes” In *European Congress of Mathematics, Vol. I (Budapest, 1996)*168, Progr. Math. Birkhäuser, Basel, 1998, pp. 237–254
- [1323] S. Gonek “The second moment of the reciprocal of the Riemann zeta function and its derivative”, 1999 URL: [https://www.slmath.org/workshops/101/schedules/25626][72]
- [1324] C. Bays and R.. Hudson “Zeroes of Dirichlet L L -functions and irregularities in the distribution of primes” In *Math. Comp.*69.230, 2000, pp. 861–866 DOI: [10.1090/S0025-5718-99-01105-9][21]
- [1325] Carter Bays and Richard. Hudson “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Math. Comp.*69.231, 2000, pp. 1285–1296
- [1326] A. Feuerverger and G. Martin “Biases in the Shanks-Rényi prime number race” In *Experiment. Math.*9.4, 2000, pp. 535–570 URL: [http://projecteuclid.org/euclid.em/1045759521][57]
- [1327] Władysław Narkiewicz “The development of prime number theory”, Springer Monographs in Mathematics Springer-Verlag, Berlin, 2000, pp. xii+448 DOI: [10.1007/978-3-662-13157-2][205]
- [1328] N. Ng “Limiting Distributions and Zeros of Artin L L -Functions” Thesis (Ph.D.)–University of British Columbia, 2000 URL: [http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf][207]
- [1329] J.-C. Puchta “On large oscillations of the remainder of the prime number theorems” In *Acta Math. Hungar.*87.3, 2000, pp. 213–227
- [1330] C. Bays, K. Ford, R.. Hudson and M. Rubinstein “Zeros of Dirichlet L L -functions near the real axis and Chebyshev’s bias” In *J. Number Theory*87.1, 2001, pp. 54–76 DOI: [10.1006/jnth.2000.2601][17]
- [1331] Kevin Ford and Richard. Hudson “Sign changes in π q, a ​ ( x) − π q, b ​ ( x) \pi_{q,a}(x)-\pi_{q,b}(x) ” In *Acta Arith.*100.4, 2001, pp. 297–314 DOI: [10.4064/aa100-4-1][68]
- [1332] Imre. Ruzsa “Consecutive primes modulo 4” In *Indag. Math. (N.S.)*12.4, 2001, pp. 489–503 DOI: [10.1016/S0019-3577(01)80038-0][235]
- [1333] K. Ford and S. Konyagin “Chebyshev’s conjecture and the prime number race” In *IV International Conference “Modern Problems of Number Theory and its Applications”: Current Problems, Part II (Russian) (Tula, 2001)*Mosk. Gos. Univ. im. Lomonosova, Mekh.-Mat. Fak., Moscow, 2002, pp. 67–91
- [1334] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line” In *Duke Math. J.*113.2, 2002, pp. 313–330 DOI: [10.1215/S0012-7094-02-11324-6][64]
- [1335] Yuk-Kam Lau “On the existence of limiting distributions of some number-theoretic error terms” In *J. Number Theory*94.2, 2002, pp. 359–374 DOI: [10.1006/jnth.2001.2734][173]
- [1336] G. Martin “Asymmetries in the Shanks-Rényi prime number race” In *Number theory for the millennium, II (Urbana, IL, 2000)*A K Peters, Natick, MA, 2002, pp. 403–415
- [1337] E.. Balanzario and S. Hernández “On the number of large oscillations of some arithmetical power series” In *Arch. Math. (Basel)*81.3, 2003, pp. 285–290 DOI: [10.1007/s00013-003-4704-2][13]
- [1338] K. Ford and S. Konyagin “The prime number race and zeros of L L -functions off the critical line. II” In *Proceedings of the Session in Analytic Number Theory and Diophantine Equations*360, Bonner Math. Schriften Univ. Bonn, Bonn, 2003, pp. 40
- [1339] Jerzy Kaczorowski and Olivier Ramaré “Almost periodicity of some error terms in prime number theory” In *Acta Arith.*106.3, 2003, pp. 277–297 DOI: [10.4064/aa106-3-6][123]
- [1340] P. Leboeuf “Prime correlations and fluctuations” In *Ann. Henri Poincaré*4.suppl. 2, 2003, pp. S727–S752 DOI: [10.1007/s00023-003-0958-2][175]
- [1341] Marc Deléglise, Pierre Dusart and Xavier-François Roblot “Counting primes in residue classes” In *Math. Comp.*73.247, 2004, pp. 1565–1575 DOI: [10.1090/S0025-5718-04-01649-7][47]
- [1342] Tadej Kotnik and Jan van Lune “On the order of the Mertens function” In *Experiment. Math.*13.4, 2004, pp. 473–481
- [1343] Pieter Moree “Chebyshev’s bias for composite numbers with restricted prime divisors” In *Math. Comp.*73.245, 2004, pp. 425–449 DOI: [10.1090/S0025-5718-03-01536-9][197]
- [1344] N. Ng “The distribution of the summatory function of the Möbius function” In *Proc. London Math. Soc. (3)*89.2, 2004, pp. 361–389 DOI: [10.1112/S0024611504014741][208]
- [1345] J.-C. Schlage–Puchta “Sign changes of π ⁡ ( x, q, 1) − π ⁡ ( x, q, a) \pi(x,q,1)-\pi(x,q,a) ” In *Acta Math. Hungar.*102.4, 2004, pp. 305–320 DOI: [10.1023/B:AMHU.0000024681.23784.d1][242]
- [1346] A.. Karatsuba “Behavior of the function R 1 ​ ( x) R_{1}(x) and of its mean value” In *Dokl. Akad. Nauk*404.4, 2005, pp. 439–442
- [1347] A.. Karatsuba “On the approximation of π ⁡ ( x) \pi(x) ” In *Chebyshevskii Sb.*5.4(12), 2005, pp. 5–20
- [1348] A.. Karatsuba “On the number of sign changes of the function R 1 ​ ( x) R_{1}(x) and its mean values” In *Chebyshevskii Sb.*6.2(14), 2005, pp. 163–183
- [1349] Maciej Radziejewski “On the distribution of algebraic numbers with prescribed factorization properties” In *Acta Arith.*116.2, 2005, pp. 153–171 DOI: [10.4064/aa116-2-4][228]
- [1350] Maciej Radziejewski “Oscillations of error terms associated with certain arithmetical functions” In *Monatsh. Math.*144.2, 2005, pp. 113–130 DOI: [10.1007/s00605-003-0147-x][229]
- [1351] A. Granville and G. Martin “Prime number races” In *Amer. Math. Monthly*113.1, 2006, pp. 1–33 DOI: [10.2307/27641834][76]
- [1352] Tadej Kotnik and Herman te Riele “The Mertens conjecture revisited” In *Algorithmic number theory*4076, Lecture Notes in Comput. Sci. Springer, Berlin, 2006, pp. 156–167
- [1353] Hugh. Montgomery and Ulrike.. Vorhauer “Changes of sign of the error term in the prime number theorem” In *Funct. Approx. Comment. Math.*35, 2006, pp. 235–247 DOI: [10.7169/facm/1229442626][196]
- [1354] Jerzy Kaczorowski “Results on the Möbius function” In *J. Lond. Math. Soc. (2)*75.2, 2007, pp. 509–521 DOI: [10.1112/jlms/jdm006][120]
- [1355] Jerzy Kaczorowski and Kazimierz Wiertelak “ Ω \Omega -estimates for a class of arithmetic error terms” In *Math. Proc. Cambridge Philos. Soc.*142.3, 2007, pp. 385–394 DOI: [10.1017/S0305004107000035][124]
- [1356] P. Sarnak “Letter to Barry Mazur on ‘Chebyshev’s bias’ for τ ⁡ ( p) \tau(p) ”, 2007 URL: [http://web.math.princeton.edu/sarnak/MazurLtrMay08.PDF][241]
- [1357] Peter Borwein, Ron Ferguson and Michael. Mossinghoff “Sign changes in sums of the Liouville function” In *Math. Comp.*77.263, 2008, pp. 1681–1694 DOI: [10.1090/S0025-5718-08-02036-X][32]
- [1358] Byungchul Cha “Chebyshev’s bias in function fields” In *Compos. Math.*144.6, 2008, pp. 1351–1374 DOI: [10.1112/S0010437X08003631][39]
- [1359] Tadej Kotnik “The prime-counting function and its analytic approximations: π ⁡ ( x) \pi(x) and its approximations” In *Adv. Comput. Math.*29.1, 2008, pp. 55–70 DOI: [10.1007/s10444-007-9039-2][163]
- [1360] Emmanuel Kowalski “The large sieve, monodromy, and zeta functions of algebraic curves. II. Independence of the zeros” In *Int. Math. Res. Not. IMRN*, 2008, pp. Art. ID rnn 09157
- [1361] Barry Mazur “Finding meaning in error terms” In *Bull. Amer. Math. Soc. (N.S.)*45.2, 2008, pp. 185–228 DOI: [10.1090/S0273-0979-08-01207-X][189]
- [1362] H.. Diamond and J. Pintz “Oscillation of Mertens’ product formula” In *J. Théor. Nombres Bordeaux*21.3, 2009, pp. 523–533 URL: [http://jtnb.cedram.org/item?id=JTNB_2009__21_3_523_0][52]
- [1363] Jerzy Kaczorowski “On the distribution of irreducible algebraic integers” In *Monatsh. Math.*156.1, 2009, pp. 47–71 DOI: [10.1007/s00605-008-0559-8][121]
- [1364] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of a given size of some arithmetic error terms” In *Trans. Amer. Math. Soc.*361.9, 2009, pp. 5023–5039 DOI: [10.1090/S0002-9947-09-04803-X][125]
- [1365] J.. Sneed “Prime and quasi-prime number races” Thesis (Ph.D.)–University of Illinois at Urbana-Champaign ProQuest LLC, Ann Arbor, MI, 2009 URL: [http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&res_dat=xri:pqdiss&rft_dat=xri:pqdiss:3411454][251]
- [1366] Byungchul Cha and Seick Kim “Biases in the prime number race of function fields” In *J. Number Theory*130.4, 2010, pp. 1048–1055 DOI: [10.1016/j.jnt.2009.09.015][41]
- [1367] Kuok Chao and Roger Plymen “A new bound for the smallest x x with π ⁡ ( x) > li ( x) \pi(x)>\mathop{\rm li}(x) ” In *Int. J. Number Theory*6.3, 2010, pp. 681–690 DOI: [10.1142/S1793042110003125][42]
- [1368] K. Ford and J. Sneed “Chebyshev’s bias for products of two primes” In *Experiment. Math.*19.4, 2010, pp. 385–398 DOI: [10.1080/10586458.2010.10390630][66]
- [1369] Jerzy Kaczorowski “ Ω \Omega -estimates related to irreducible algebraic integers” In *Math. Nachr.*283.9, 2010, pp. 1291–1303 DOI: [10.1002/mana.200710158][122]
- [1370] Jerzy Kaczorowski and Kazimierz Wiertelak “Oscillations of the remainder term related to the Euler totient function” In *J. Number Theory*130.12, 2010, pp. 2683–2700 DOI: [10.1016/j.jnt.2010.06.010][126]
- [1371] Jerzy Kaczorowski and Kazimierz Wiertelak “Smoothing arithmetic error terms: the case of the Euler ϕ \phi function” In *Math. Nachr.*283.11, 2010, pp. 1637–1645 DOI: [10.1002/mana.200810048][127]
- [1372] Yannick Saouter and Patrick Demichel “A sharp region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*79.272, 2010, pp. 2395–2405 DOI: [10.1090/S0025-5718-10-02351-3][238]
- [1373] R.. Brent and Jan van Lune “A note on Pólya’s observation concerning Liouville’s function” In *Herman J. J. te Riele Liber Amicorum*, CWI, 2011, pp. 92–97 URL: [https://arxiv.org/abs/1112.4911][33]
- [1374] B Cha and B.-H. Im “Chebyshev’s bias in Galois extensions of global function fields” In *J. Number Theory*131.10, 2011, pp. 1875–1886 DOI: [10.1016/j.jnt.2011.03.011][37]
- [1375] D. Fiorilli “Irrégularités dans la distribution des nombres premiers et des suites plus générales dans les progressions arithmétiques” Thesis (Ph.D.)–Université de Montréal ProQuest LLC, Ann Arbor, MI, 2011
- [1376] Douglas. Stoll and Patrick Demichel “The impact of ζ ⁡ ( s) \zeta(s) complex zeros on π ⁡ ( x) \pi(x) for x < 10 10 13 x<10^{10^{13}} ” In *Math. Comp.*80.276, 2011, pp. 2381–2394 DOI: [10.1090/S0025-5718-2011-02477-4][262]
- [1377] Matthias Kunik and Lutz. Lucht “Power series with the von Mangoldt function” In *Funct. Approx. Comment. Math.*47.part 1, 2012, pp. 15–33 DOI: [10.7169/facm/2012.47.1.2][165]
- [1378] Y. Lamzouri “Large deviations of the limiting distribution in the Shanks–Rényi prime number race” In *Math. Proc. Cambridge Philos. Soc.*153.1, 2012, pp. 147–166 DOI: [10.1017/S030500411200014X][166]
- [1379] Y. Lamzouri “The Shanks-Rényi prime number race with many contestants” In *Math. Res. Lett.*19.3, 2012, pp. 649–666 DOI: [10.4310/MRL.2012.v19.n3.a11][167]
- [1380] Micah. Milinovich and Nathan Ng “A note on a conjecture of Gonek” In *Funct. Approx. Comment. Math.*46, 2012, pp. 177–187 DOI: [10.7169/facm/2012.46.2.3][193]
- [1381] Michael. Mossinghoff and Timothy. Trudgian “Between the problems of Pólya and Turán” In *J. Aust. Math. Soc.*93.1–2, 2012, pp. 157–171 DOI: [10.1017/S1446788712000201][200]
- [1382] D. Fiorilli and G. Martin “Inequities in the Shanks-Rényi prime number race: an asymptotic formula for the densities” In *J. Reine Angew. Math.*676, 2013, pp. 121–212
- [1383] K. Ford, Y. Lamzouri and S. Konyagin “The prime number race and zeros of Dirichlet L L -functions off the critical line: Part III” In *Q. J. Math.*64.4, 2013, pp. 1091–1098 DOI: [10.1093/qmath/has021][65]
- [1384] Peter Humphries “The distribution of weighted sums of the Liouville function and Pólya’s conjecture” In *J. Number Theory*133.2, 2013, pp. 545–582 DOI: [10.1016/j.jnt.2012.08.011][94]
- [1385] Y. Lamzouri “Prime number races with three or more competitors” In *Math. Ann.*356.3, 2013, pp. 1117–1162 DOI: [10.1007/s00208-012-0874-1][168]
- [1386] C. Myerscough “Application of an accurate remainder term in the calculation of residue class distributions”, 2013 URL: [https://arxiv.org/abs/1301.1434][204]
- [1387] O.. Petrushov “Asymptotic estimates of functions based on the behavior of their Laplace transforms near singular points” In *Math. Notes*93.5–6, 2013, pp. 906–916 DOI: [10.1134/S0001434613050283][210]
- [1388] A. Akbary, N. Ng and M. Shahabi “Limiting distributions of the classical error terms of prime number theory” In *Q. J. Math.*65.3, 2014, pp. 743–780 DOI: [10.1093/qmath/hat059][4]
- [1389] Sneha Chaubey, Melinda Lanius and Alexandru Zaharescu “Irrational factor races” In *Proc. Indian Acad. Sci. Math. Sci.*124.4, 2014, pp. 471–479 DOI: [10.1007/s12044-014-0198-z][43]
- [1390] D. Fiorilli “Elliptic curves of unbounded rank and Chebyshev’s bias” In *Int. Math. Res. Not. IMRN*, 2014, pp. 4997–5024 DOI: [10.1093/imrn/rnt103][58]
- [1391] D. Fiorilli “Highly biased prime number races” In *Algebra Number Theory*8.7, 2014, pp. 1733–1767 DOI: [10.2140/ant.2014.8.1733][59]
- [1392] Peter Humphries “On the Mertens conjecture for elliptic curves over finite fields” In *Bull. Aust. Math. Soc.*89.1, 2014, pp. 19–32 DOI: [10.1017/S0004972712001116][95]
- [1393] Peter Humphries “On the Mertens conjecture for function fields” In *Int. J. Number Theory*10.2, 2014, pp. 341–361 DOI: [10.1142/S1793042113500978][96]
- [1394] Maciej Radziejewski “Oscillatory properties of real functions with weakly bounded Mellin transform” In *Q. J. Math.*65.1, 2014, pp. 249–266 DOI: [10.1093/qmath/has036][230]
- [1395] Yannick Saouter and Herman te Riele “Improved results on the Mertens conjecture” In *Math. Comp.*83.285, 2014, pp. 421–433 DOI: [10.1090/S0025-5718-2013-02716-0][239]
- [1396] D.. Best and T.. Trudgian “Linear relations of zeroes of the zeta-function” In *Math. Comp.*84.294, 2015, pp. 2047–2058 DOI: [10.1090/S0025-5718-2014-02916-5][31]
- [1397] J. Büthe “On the first sign change in Mertens’ theorem” In *Acta Arith.*171.2, 2015, pp. 183–195 DOI: [10.4064/aa171-2-5][35]
- [1398] D. Fiorilli “The distribution of the variance of primes in arithmetic progressions” In *Int. Math. Res. Not. IMRN*, 2015, pp. 4421–4448 DOI: [10.1093/imrn/rnu074][60]
- [1399] H. Kisilevsky and M.. Rubinstein “Chebotarev sets” In *Acta Arith.*171.2, 2015, pp. 97–124 DOI: [10.4064/aa171-2-1][134]
- [1400] J. Lay “Sign changes in Mertens’ first and second theorems”, 2015 URL: [https://arxiv.org/abs/1505.03589][174]
- [1401] Yannick Saouter, Timothy Trudgian and Patrick Demichel “A still sharper region where π ⁡ ( x) − li ( x) \pi(x)-\mathop{\rm li}(x) is positive” In *Math. Comp.*84.295, 2015, pp. 2433–2446 DOI: [10.1090/S0025-5718-2015-02930-5][240]
- [1402] Gautami Bhowmik, Olivier Ramaré and Jan-Christoph Schlage–Puchta “Tauberian oscillation theorems and the distribution of Goldbach numbers” In *J. Théor. Nombres Bordeaux*28.2, 2016, pp. 291–299
- [1403] B. Cha, D. Fiorilli and F. Jouve “Prime number races for elliptic curves over function fields” In *Ann. Sci. Éc. Norm. Supér. (4)*49.5, 2016, pp. 1239–1277 DOI: [10.24033/asens.2308][38]
- [1404] D. Dummit, A. Granville and B. Kisilevsky “Big biases amongst products of two primes” In *Mathematika*62.2, 2016, pp. 502–507 DOI: [10.1112/S0025579315000339][53]
- [1405] Y. Lamzouri “A bias in Mertens’ product formula” In *Int. J. Number Theory*12.1, 2016, pp. 97–109 DOI: [10.1142/S1793042116500068][169]
- [1406] R.. Lemke and K. Soundararajan “Unexpected biases in the distribution of consecutive primes” In *Proc. Natl. Acad. Sci. USA*113.31, 2016, pp. E4446–E4454 DOI: [10.1073/pnas.1605366113][180]
- [1407] D.. Platt and T.. Trudgian “On the first sign change of θ ⁡ ( x) − x \theta(x)-x ” In *Math. Comp.*85.299, 2016, pp. 1539–1547 DOI: [10.1090/mcom/3021][224]
- [1408] Herman.. te Riele “The Mertens conjecture” In *The legacy of Bernhard Riemann after one hundred and fifty years. Vol. II*35.2, Adv. Lect. Math. (ALM) Int. Press, Somerville, MA, 2016, pp. 703–718
- [1409] Byungchul Cha “The summatory function of the Möbius function in function fields” In *Acta Arith.*179.4, 2017, pp. 375–395 DOI: [10.4064/aa8590-1-2017][40]
- [1410] Patrick Hough “A lower bound for biases amongst products of two primes” In *Res. Number Theory*3, 2017, pp. Art. 1911 DOI: [10.1007/s40993-017-0083-9][89]
- [1411] X. Meng “The distribution of k k -free numbers and the derivative of the Riemann zeta-function” In *Math. Proc. Cambridge Philos. Soc.*162.2, 2017, pp. 293–317 DOI: [10.1017/S0305004116000554][190]
- [1412] Michael. Mossinghoff and Timothy. Trudgian “The Liouville function and the Riemann hypothesis” In *Exploring the Riemann zeta function*Springer, Cham, 2017, pp. 201–221
- [1413] Jan Büthe “An analytic method for bounding ψ ⁡ ( x) \psi(x) ” In *Math. Comp.*87.312, 2018, pp. 1991–2009 DOI: [10.1090/mcom/3264][36]
- [1414] Adam. Harper and Youness Lamzouri “Orderings of weakly correlated random variables, and prime number races with many contestants” In *Probab. Theory Related Fields*170.3-4, 2018, pp. 961–1010 DOI: [10.1007/s00440-017-0800-2][82]
- [1415] Greg Hurst “Computations of the Mertens function and improved bounds on the Mertens conjecture” In *Math. Comp.*87.310, 2018, pp. 1013–1028 DOI: [10.1090/mcom/3275][98]
- [1416] X. Meng “Chebyshev’s bias for products of k k primes” In *Algebra Number Theory*12.2, 2018, pp. 305–341 DOI: [10.2140/ant.2018.12.305][191]
- [1417] X. Meng “Large bias for integers with prime factors in arithmetic progressions” In *Mathematika*64.1, 2018, pp. 237–252
- [1418] J.-C. Schlage–Puchta “Oscillations of the error term in the prime number theorem” In *Acta Math. Hungar.*156.2, 2018, pp. 303–308 DOI: [10.1007/s10474-018-0884-x][243]
- [1419] Kevin Ford, Adam. Harper and Youness Lamzouri “Extreme biases in prime number races with many contestants” In *Math. Ann.*374.1-2, 2019, pp. 517–551 DOI: [10.1007/s00208-019-01810-x][67]
- [1420] Peter Humphries, Snehal. Shekatkar and Tian Wong “Biases in prime factorizations and Liouville functions for arithmetic progressions” In *J. Théor. Nombres Bordeaux*31.1, 2019, pp. 1–25 URL: [http://jtnb.cedram.org/item?id=JTNB_2019__31_1_1_0][97]
- [1421] Youness Lamzouri and Bruno Martin “On the race between primes with an odd versus an even sum of the last k k binary digits” In *Funct. Approx. Comment. Math.*61.1, 2019, pp. 7–25 DOI: [10.7169/facm/1687][170]
- [1422] J.. Lichtman, G. Martin and C. Pomerance “Primes in prime number races” In *Proc. Amer. Math. Soc.*147.9, 2019, pp. 3743–3757
- [1423] Kamalakshya Mahatab and Anirban Mukhopadhyay “Measure-theoretic aspects of oscillations of error terms” In *Acta Arith.*187.3, 2019, pp. 201–217 DOI: [10.4064/aa170126-23-4][185]
- [1424] Dave Platt and Tim Trudgian “Fujii’s development on Chebyshev’s conjecture” In *Int. J. Number Theory*15.3, 2019, pp. 639–644 DOI: [10.1142/S1793042119500337][225]
- [1425] Emre Alkan “Biased behavior of weighted Mertens sums” In *Int. J. Number Theory*16.3, 2020, pp. 547–577 DOI: [10.1142/S1793042120500281][5]
- [1426] Lucile Devin “Chebyshev’s bias for analytic L-functions” In *Math. Proc. Cambridge Philos. Soc.*169.1, 2020, pp. 103–140 DOI: [10.1017/s0305004119000100][48]
- [1427] Lucile Devin “Limiting properties of the distribution of primes in an arbitrarily large number of residue classes” In *Canad. Math. Bull.*63.4, 2020, pp. 837–849 DOI: [10.4153/s0008439520000089][49]
- [1428] Robert. Lemke and Kannan Soundararajan “The distribution of consecutive prime biases and sums of sawtooth random variables” In *Math. Proc. Cambridge Philos. Soc.*168.1, 2020, pp. 149–169 DOI: [10.1017/s0305004118000592][181]
- [1429] Greg Martin and Nathan Ng “Inclusive prime number races” In *Trans. Amer. Math. Soc.*373.5, 2020, pp. 3561–3607 DOI: [10.1090/tran/7996][188]
- [1430] Xianchang Meng “Number of prime factors over arithmetic progressions” In *Q. J. Math.*71.1, 2020, pp. 97–121 DOI: [10.1093/qmathj/haz040][192]
- [1431] Michael. Mossinghoff and Timothy. Trudgian “A tale of two omegas” In *75 years of mathematics of computation*754, Contemp. Math. Amer. Math. Soc., [Providence], RI, 2020, pp. 343–364
- [1432] Roger Plymen “The Great Prime Number Race” 92, Student Mathematical Library American Mathematical Society, Providence, RI, 2020, pp. 138
- [1433] Sam Porritt “Character sums over products of prime polynomials”, 2020 URL: [https://arxiv.org/abs/2003.12002][227]
- [1434] Emre Alkan “Variations on criteria of Pólya and Turán for the Riemann hypothesis” In *J. Number Theory*225, 2021, pp. 90–124 DOI: [10.1016/j.jnt.2021.01.004][6]
- [1435] Alexandre Bailleul “Chebyshev’s bias in dihedral and generalized quaternion Galois groups” In *Algebra Number Theory*15.4, 2021, pp. 999–1041 DOI: [10.2140/ant.2021.15.999][10]
- [1436] Lucile Devin “Discrepancies in the distribution of Gaussian primes”, 2021 URL: [https://arxiv.org/abs/2105.02492][50]
- [1437] Lucile Devin and Xianchang Meng “Chebyshev’s bias for products of irreducible polynomials” In *Adv. Math.*392, 2021, pp. Paper No. 10804045 DOI: [10.1016/j.aim.2021.108040][51]
- [1438] Michael. Mossinghoff, Tomás Oliveira and Timothy. Trudgian “The distribution of k k -free numbers” In *Math. Comp.*90.328, 2021, pp. 907–929 DOI: [10.1090/mcom/3581][199]
- [1439] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in weighted arithmetic sums” In *Int. J. Number Theory*17.7, 2021, pp. 1697–1716 DOI: [10.1142/S1793042121500561][201]
- [1440] A. Shchebetov “Chebyshev’s bias visualizer”, 2021 URL: [http://math101.guru/en/downloads-2/repository/][247]
- [1441] Marco Aymone “A note on prime number races and zero free regions for L L functions” In *Int. J. Number Theory*18.1, 2022, pp. 1–8 DOI: [10.1142/S1793042122500014][9]
- [1442] Alexandre Bailleul “Explicit Kronecker–Weyl theorems and applications to prime number races” In *Res. Number Theory*8.3, 2022, pp. Paper No. 4334 DOI: [10.1007/s40993-022-00349-2][11]
- [1443] Daniel Fiorilli and Florent Jouve “Unconditional Chebyshev biases in number fields” In *J. Éc. polytech. Math.*9, 2022, pp. 671–679 DOI: [10.5802/jep.19][61]
- [1444] Shehzad Hathi and Ethan. Lee “Mertens’ third theorem for number fields: a new proof, Cramér’s inequality, oscillations, and bias”, 2022 URL: [https://arxiv.org/abs/2112.02166][84]
- [1445] Winston Heap, Junxian Li and Jing Zhao “Lower bounds for discrete negative moments of the Riemann zeta function” In *Algebra Number Theory*16.7, 2022, pp. 1589–1625 DOI: [10.2140/ant.2022.16.1589][86]
- [1446] Jaeyoon Kim “Prime running functions” In *Exp. Math.*31.4, 2022, pp. 1291–1313 DOI: [10.1080/10586458.2020.1786863][133]
- [1447] Shin-ya Koyama and Nobushige Kurokawa “Chebyshev’s bias for Ramanujan’s τ \tau -function via the deep Riemann hypothesis” In *Proc. Japan Acad. Ser. A Math. Sci.*98.6, 2022, pp. 35–39 DOI: [10.3792/pjaa.98.007][164]
- [1448] Jiawei Lin and Greg Martin “Densities in certain three-way prime number races” In *Canad. J. Math.*74.1, 2022, pp. 232–265 DOI: [10.4153/S0008414X20000747][182]
- [1449] Thomas Morrill, Dave Platt and Tim Trudgian “Sign changes in the prime number theorem” In *Ramanujan J.*57.1, 2022, pp. 165–173 DOI: [10.1007/s11139-021-00398-8][198]
- [1450] Michael. Mossinghoff and Timothy. Trudgian “Oscillations in the Goldbach conjecture” In *J. Théor. Nombres Bordeaux*34.1, 2022, pp. 295–307 DOI: [10.5802/jtnb.120][202]
- [1451] Youssef Sedrati “Inequities in the Shanks–Renyi prime number race over function fields” In *Mathematika*68.3, 2022, pp. 840–895 DOI: [10.1112/mtk.12150][245]
- [1452] Miho Aoki and Shin-ya Koyama “Chebyshev’s bias against splitting and principal primes in global fields” In *J. Number Theory*245, 2023, pp. 233–262 DOI: [10.1016/j.jnt.2022.10.005][7]
- [1453] Christian Axler “New estimates for some integrals of functions defined over primes” In *Funct. Approx. Comment. Math.*68.2, 2023, pp. 207–229 DOI: [10.7169/facm/2049][8]
- [1454] Daniel Fiorilli and Greg Martin “Disproving Hooley’s conjecture” In *J. Eur. Math. Soc. (JEMS)*25.12, 2023, pp. 4791–4812 DOI: [10.4171/jems/1291][63]
- [1455] Peng Gao and Liangyi Zhao “Lower bounds for negative moments of ζ ′ ​ ( ρ) \zeta^{\prime}(\rho) ” In *Mathematika*69.4, 2023, pp. 1081–1103
- [1456] Ofir Gorodetsky “Sums of two squares are strongly biased towards quadratic residues” In *Algebra Number Theory*17.3, 2023, pp. 775–804 DOI: [10.2140/ant.2023.17.775][75]
- [1457] Daniel Hu, Ikuya Kaneko, Spencer Martin and Carl Schildkraut “On a Mertens-type conjecture for number fields”, 2023 URL: [https://arxiv.org/abs/2109.06665][90]
- [1458] Daniel. Johnston “On the average value of π ⁡ ( t) − li ⁡ ( t) \pi(t)-{\rm li}(t) ” In *Canad. Math. Bull.*66.1, 2023, pp. 185–195 DOI: [10.4153/S0008439522000212][101]
- [1459] Ikuya Kaneko and Shin-ya Koyama “A new aspect of Chebyshev’s bias for elliptic curves over function fields” In *Proc. Amer. Math. Soc.*151.12, 2023, pp. 5059–5068 DOI: [10.1090/proc/16461][128]
- [1460] Ikuya Kaneko, Shin-ya Koyama and Nobushige Kurokawa “Towards the Deep Riemann Hypothesis for GL n \mathrm{GL}_{n} ”, 2023 URL: [https://arxiv.org/abs/2206.02612][129]
- [1461] Greg Martin, Michael Mossinghoff and Timothy Trudgian “Fake mu’s” In *Proc. Amer. Math. Soc.*151.8, 2023, pp. 3229–3244 DOI: [10.1090/proc/16186][187]
- [1462] Alexandre Bailleul, Lucile Devin, Daniel Keliher and Wanlin Li “Exceptional biases in counting primes over function fields” In *J. Lond. Math. Soc. (2)*109.3, 2024, pp. Paper No. e1287632 DOI: [10.1112/jlms.12876][12]
- [1463] Hung. Bui, Alexandra Florea and Micah. Milinovich “Negative discrete moments of the derivative of the Riemann zeta-function” In *Bull. Lond. Math. Soc.*56.8, 2024, pp. 2680–2703
- [1464] Daniel Fiorilli and Florent Jouve “Distribution of Frobenius elements in families of Galois extensions” In *J. Inst. Math. Jussieu*23.3, 2024, pp. 1169–1258 DOI: [10.1017/S1474748023000154][62]
- [1465] M. Grześkowiak, J. Kaczorowski, Ł. Pańkowski and M. Radziejewski “On the sign changes of ψ ⁡ ( x) − x \psi(x)-x ”, 2024 URL: [https://arxiv.org/abs/2408.10399][79]
- [1466] Alia Hamieh, Habiba Kadiri, Greg Martin and Nathan Ng “Comparative prime number theory problem list”, 2024 URL: [https://arxiv.org/abs/2407.03530][80]
- [1467] Mounir Hayani “On the influence of the Galois group structure on the Chebyshev bias in number fields”, 2024 URL: [https://arxiv.org/abs/2404.06804][85]
- [1468] Arshay Sheth “Euler products at the centre and applications to Chebyshev’s bias”, 2024 URL: [https://arxiv.org/abs/2405.01512][248]

*


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:gerg@math.ubc.ca
[4]: https://dx.doi.org/10.1093/qmath/hat059
[5]: https://dx.doi.org/10.1142/S1793042120500281
[6]: https://dx.doi.org/10.1016/j.jnt.2021.01.004
[7]: https://dx.doi.org/10.1016/j.jnt.2022.10.005
[8]: https://dx.doi.org/10.7169/facm/2049
[9]: https://dx.doi.org/10.1142/S1793042122500014
[10]: https://dx.doi.org/10.2140/ant.2021.15.999
[11]: https://dx.doi.org/10.1007/s40993-022-00349-2
[12]: https://dx.doi.org/10.1112/jlms.12876
[13]: https://dx.doi.org/10.1007/s00013-003-4704-2
[14]: https://dx.doi.org/10.4064/aa-50-2-107-118
[15]: https://dx.doi.org/10.4064/aa-57-4-283-293
[16]: http://projecteuclid.org/euclid.ijm/1255380836
[17]: https://dx.doi.org/10.1006/jnth.2000.2601
[18]: https://dx.doi.org/10.1007/bf01932283
[19]: https://dx.doi.org/10.2307/2006165
[20]: https://dx.doi.org/10.1155/S0161171279000119
[21]: https://dx.doi.org/10.1090/S0025-5718-99-01105-9
[22]: https://dx.doi.org/10.2307/2006277
[23]: https://dx.doi.org/10.1515/crll.1978.299-300.234
[24]: https://dx.doi.org/10.1515/crll.1983.339.215
[25]: https://dx.doi.org/10.1016/0022-314X(82)90030-0
[26]: https://dx.doi.org/10.1007/BF01303260
[27]: https://dx.doi.org/10.1007/bf03323296
[28]: https://dx.doi.org/10.1007/BF01215079
[29]: https://dx.doi.org/10.1515/crll.1979.307-308.411
[30]: https://dx.doi.org/10.1515/crll.1980.313.52
[31]: https://dx.doi.org/10.1090/S0025-5718-2014-02916-5
[32]: https://dx.doi.org/10.1090/S0025-5718-08-02036-X
[33]: https://arxiv.org/pdf/1112.4911
[34]: https://dx.doi.org/10.2307/2005460
[35]: https://dx.doi.org/10.4064/aa171-2-5
[36]: https://dx.doi.org/10.1090/mcom/3264
[37]: https://dx.doi.org/10.1016/j.jnt.2011.03.011
[38]: https://dx.doi.org/10.24033/asens.2308
[39]: https://dx.doi.org/10.1112/S0010437X08003631
[40]: https://dx.doi.org/10.4064/aa8590-1-2017
[41]: https://dx.doi.org/10.1016/j.jnt.2009.09.015
[42]: https://dx.doi.org/10.1142/S1793042110003125
[43]: https://dx.doi.org/10.1007/s12044-014-0198-z
[44]: https://dx.doi.org/10.1112/jlms/s2-23.1.24
[45]: https://dx.doi.org/10.1112/plms/s3-18.4.691
[46]: https://dx.doi.org/10.1007/BF01482072
[47]: https://dx.doi.org/10.1090/S0025-5718-04-01649-7
[48]: https://dx.doi.org/10.1017/s0305004119000100
[49]: https://dx.doi.org/10.4153/s0008439520000089
[50]: https://arxiv.org/pdf/2105.02492
[51]: https://dx.doi.org/10.1016/j.aim.2021.108040
[52]: http://jtnb.cedram.org/item?id=JTNB_2009__21_3_523_0
[53]: https://dx.doi.org/10.1112/S0025579315000339
[54]: https://dx.doi.org/10.2307/1968190
[55]: https://dx.doi.org/10.1112/plms/s3-1.1.86
[56]: https://dx.doi.org/10.1093/qmath/3.1.282
[57]: http://projecteuclid.org/euclid.em/1045759521
[58]: https://dx.doi.org/10.1093/imrn/rnt103
[59]: https://dx.doi.org/10.2140/ant.2014.8.1733
[60]: https://dx.doi.org/10.1093/imrn/rnu074
[61]: https://dx.doi.org/10.5802/jep.19
[62]: https://dx.doi.org/10.1017/S1474748023000154
[63]: https://dx.doi.org/10.4171/jems/1291
[64]: https://dx.doi.org/10.1215/S0012-7094-02-11324-6
[65]: https://dx.doi.org/10.1093/qmath/has021
[66]: https://dx.doi.org/10.1080/10586458.2010.10390630
[67]: https://dx.doi.org/10.1007/s00208-019-01810-x
[68]: https://dx.doi.org/10.4064/aa100-4-1
[69]: http://projecteuclid.org/euclid.pja/1195513180
[70]: http://projecteuclid.org/euclid.pja/1195511989
[71]: https://dx.doi.org/10.4064/aa-37-1-339-343
[72]: https://www.slmath.org/workshops/101/schedules/25626
[73]: https://dx.doi.org/10.1112/S0025579300013589
[74]: https://dx.doi.org/10.2307/2004584
[75]: https://dx.doi.org/10.2140/ant.2023.17.775
[76]: https://dx.doi.org/10.2307/27641834
[77]: https://dx.doi.org/10.1007/BF03008399
[78]: https://dx.doi.org/10.2307/1994409
[79]: https://arxiv.org/pdf/2408.10399
[80]: https://arxiv.org/pdf/2407.03530
[81]: https://dx.doi.org/10.1112/plms/s2-15.1.1
[82]: https://dx.doi.org/10.1007/s00440-017-0800-2
[83]: https://dx.doi.org/10.1112/S0025579300001480
[84]: https://arxiv.org/pdf/2112.02166
[85]: https://arxiv.org/pdf/2404.06804
[86]: https://dx.doi.org/10.2140/ant.2022.16.1589
[87]: https://dx.doi.org/10.4064/aa-60-4-389-415
[88]: https://dx.doi.org/10.1112/jlms/s2-16.1.1
[89]: https://dx.doi.org/10.1007/s40993-017-0083-9
[90]: https://arxiv.org/pdf/2109.06665
[91]: https://dx.doi.org/10.1515/crll.1980.313.133
[92]: https://dx.doi.org/10.2307/2007974
[93]: https://dx.doi.org/10.1515/crll.1977.296.80
[94]: https://dx.doi.org/10.1016/j.jnt.2012.08.011
[95]: https://dx.doi.org/10.1017/S0004972712001116
[96]: https://dx.doi.org/10.1142/S1793042113500978
[97]: http://jtnb.cedram.org/item?id=JTNB_2019__31_1_1_0
[98]: https://dx.doi.org/10.1090/mcom/3275
[99]: https://dx.doi.org/10.2307/2371685
[100]: https://dx.doi.org/10.2307/1989728
[101]: https://dx.doi.org/10.4153/S0008439522000212
[102]: https://dx.doi.org/10.1515/crll.1976.286-287.322
[103]: https://dx.doi.org/10.4064/aa-44-4-365-377
[104]: https://dx.doi.org/10.4064/aa-45-1-65-74
[105]: https://dx.doi.org/10.4064/aa-48-4-347-371
[106]: https://dx.doi.org/10.4064/aa-50-1-15-21
[107]: https://dx.doi.org/10.4064/aa-56-3-195-211
[108]: https://dx.doi.org/10.4064/aa-56-3-213-224
[109]: https://dx.doi.org/10.4064/aa-57-3-199-210
[110]: https://dx.doi.org/10.4064/aa-57-3-231-244
[111]: https://dx.doi.org/10.4064/aa-59-1-37-58
[112]: https://dx.doi.org/10.1093/qmath/44.4.451
[113]: https://dx.doi.org/10.4064/aa-74-1-31-46
[114]: https://dx.doi.org/10.1007/BF01949062
[115]: https://dx.doi.org/10.1007/BF01951008
[116]: https://dx.doi.org/10.4064/cm-56-1-185-197
[117]: https://dx.doi.org/10.1515/crll.1994.446.89
[118]: https://dx.doi.org/10.1524/anly.1995.15.2.159
[119]: https://dx.doi.org/10.1006/jnth.1995.1006
[120]: https://dx.doi.org/10.1112/jlms/jdm006
[121]: https://dx.doi.org/10.1007/s00605-008-0559-8
[122]: https://dx.doi.org/10.1002/mana.200710158
[123]: https://dx.doi.org/10.4064/aa106-3-6
[124]: https://dx.doi.org/10.1017/S0305004107000035
[125]: https://dx.doi.org/10.1090/S0002-9947-09-04803-X
[126]: https://dx.doi.org/10.1016/j.jnt.2010.06.010
[127]: https://dx.doi.org/10.1002/mana.200810048
[128]: https://dx.doi.org/10.1090/proc/16461
[129]: https://arxiv.org/pdf/2206.02612
[130]: https://dx.doi.org/10.1007/BF02020967
[131]: https://dx.doi.org/10.1007/BF02280297
[132]: https://dx.doi.org/10.4064/aa-13-1-107-122
[133]: https://dx.doi.org/10.1080/10586458.2020.1786863
[134]: https://dx.doi.org/10.4064/aa171-2-1
[135]: https://dx.doi.org/10.4064/aa-4-1-57-70
[136]: https://dx.doi.org/10.4064/aa-4-3-209-216
[137]: https://dx.doi.org/10.4064/aa-6-4-415-434
[138]: https://dx.doi.org/10.4064/aa-7-4-325-335
[139]: https://dx.doi.org/10.4064/aa-7-2-121-130
[140]: https://dx.doi.org/10.4064/aa-7-4-337-343
[141]: https://dx.doi.org/10.1112/jlms/s1-36.1.451
[142]: https://dx.doi.org/10.4064/aa-7-2-107-119
[143]: https://dx.doi.org/10.4064/aa-8-1-97-105
[144]: https://dx.doi.org/10.4064/aa-8-3-311-320
[145]: https://dx.doi.org/10.4064/aa-10-4-377-386
[146]: https://dx.doi.org/10.4064/aa-7-2-161-166
[147]: https://dx.doi.org/10.1007/BF02020796
[148]: https://dx.doi.org/10.1007/BF02020797
[149]: https://dx.doi.org/10.1007/BF02020798
[150]: https://dx.doi.org/10.1007/BF01901928
[151]: https://dx.doi.org/10.1007/BF01901929
[152]: https://dx.doi.org/10.1007/BF01901930
[153]: https://dx.doi.org/10.1007/BF01895712
[154]: https://dx.doi.org/10.1007/BF01895713
[155]: https://dx.doi.org/10.4064/aa-9-1-23-40
[156]: https://dx.doi.org/10.4064/aa-10-3-293-313
[157]: https://dx.doi.org/10.4064/aa-11-1-115-127
[158]: https://dx.doi.org/10.4064/aa-11-2-193-202
[159]: https://dx.doi.org/10.1007/BF02806393
[160]: https://dx.doi.org/10.4064/aa-12-1-85-96
[161]: https://dx.doi.org/10.4064/aa-21-1-193-201
[162]: https://dx.doi.org/10.1007/BF01305997
[163]: https://dx.doi.org/10.1007/s10444-007-9039-2
[164]: https://dx.doi.org/10.3792/pjaa.98.007
[165]: https://dx.doi.org/10.7169/facm/2012.47.1.2
[166]: https://dx.doi.org/10.1017/S030500411200014X
[167]: https://dx.doi.org/10.4310/MRL.2012.v19.n3.a11
[168]: https://dx.doi.org/10.1007/s00208-012-0874-1
[169]: https://dx.doi.org/10.1142/S1793042116500068
[170]: https://dx.doi.org/10.7169/facm/1687
[171]: https://dx.doi.org/10.1007/BF01449495
[172]: https://dx.doi.org/10.1007/BF01203613
[173]: https://dx.doi.org/10.1006/jnth.2001.2734
[174]: https://arxiv.org/pdf/1505.03589
[175]: https://dx.doi.org/10.1007/s00023-003-0958-2
[176]: https://dx.doi.org/10.1112/jlms/s1-32.1.56
[177]: https://dx.doi.org/10.4064/aa-11-4-397-410
[178]: https://dx.doi.org/10.2307/2003890
[179]: https://dx.doi.org/10.4064/aa-6-1-111-114
[180]: https://dx.doi.org/10.1073/pnas.1605366113
[181]: https://dx.doi.org/10.1017/s0305004118000592
[182]: https://dx.doi.org/10.4153/S0008414X20000747
[183]: https://dx.doi.org/10.1112/jlms/s1-2.1.41
[184]: https://dx.doi.org/10.1112/jlms/s1-12.2.217
[185]: https://dx.doi.org/10.4064/aa170126-23-4
[186]: https://dx.doi.org/10.1007/BF01897022
[187]: https://dx.doi.org/10.1090/proc/16186
[188]: https://dx.doi.org/10.1090/tran/7996
[189]: https://dx.doi.org/10.1090/S0273-0979-08-01207-X
[190]: https://dx.doi.org/10.1017/S0305004116000554
[191]: https://dx.doi.org/10.2140/ant.2018.12.305
[192]: https://dx.doi.org/10.1093/qmathj/haz040
[193]: https://dx.doi.org/10.7169/facm/2012.46.2.3
[194]: http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&amp;rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&amp;res_dat=xri:pqdiss&amp;rft_dat=xri:pqdiss:8106192
[195]: https://dx.doi.org/10.1090/cbms/084
[196]: https://dx.doi.org/10.7169/facm/1229442626
[197]: https://dx.doi.org/10.1090/S0025-5718-03-01536-9
[198]: https://dx.doi.org/10.1007/s11139-021-00398-8
[199]: https://dx.doi.org/10.1090/mcom/3581
[200]: https://dx.doi.org/10.1017/S1446788712000201
[201]: https://dx.doi.org/10.1142/S1793042121500561
[202]: https://dx.doi.org/10.5802/jtnb.120
[203]: http://www.numdam.org/item?id=ASENS_1994_4_27_5_529_0
[204]: https://arxiv.org/pdf/1301.1434
[205]: https://dx.doi.org/10.1007/978-3-662-13157-2
[206]: https://dx.doi.org/10.1007/BF01385874
[207]: http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf
[208]: https://dx.doi.org/10.1112/S0024611504014741
[209]: https://dx.doi.org/10.1515/crll.1985.357.138
[210]: https://dx.doi.org/10.1134/S0001434613050283
[211]: https://dx.doi.org/10.1007/BF01526326
[212]: https://dx.doi.org/10.4064/aa-36-4-341-365
[213]: https://dx.doi.org/10.4064/aa-37-1-209-220
[214]: https://dx.doi.org/10.1524/anly.1981.1.3.191
[215]: https://dx.doi.org/10.4064/aa-42-1-49-55
[216]: https://dx.doi.org/10.1112/jlms/s2-28.3.401
[217]: https://dx.doi.org/10.4064/aa-43-2-105-113
[218]: https://dx.doi.org/10.1007/BF01903967
[219]: https://dx.doi.org/10.1007/BF01196659
[220]: http://www.numdam.org/item?id=ASNSP_1984_4_11_2_245_0
[221]: https://dx.doi.org/10.1007/BF01961016
[222]: https://dx.doi.org/10.1016/0022-314X(86)90088-0
[223]: https://dx.doi.org/10.1007/BF01190694
[224]: https://dx.doi.org/10.1090/mcom/3021
[225]: https://dx.doi.org/10.1142/S1793042119500337
[226]: https://dx.doi.org/10.1112/plms/s2-33.1.85
[227]: https://arxiv.org/pdf/2003.12002
[228]: https://dx.doi.org/10.4064/aa116-2-4
[229]: https://dx.doi.org/10.1007/s00605-003-0147-x
[230]: https://dx.doi.org/10.1093/qmath/has036
[231]: https://dx.doi.org/10.1515/crll.1979.311-312.356
[232]: https://dx.doi.org/10.2307/2007893
[233]: http://www.numdam.org/item?id=AFST_1986-1987_5_8_2_159_0
[234]: http://projecteuclid.org/euclid.em/1048515870
[235]: https://dx.doi.org/10.1016/S0019-3577(01)80038-0
[236]: https://dx.doi.org/10.2307/2314046
[237]: https://dx.doi.org/10.1007/BF01194239
[238]: https://dx.doi.org/10.1090/S0025-5718-10-02351-3
[239]: https://dx.doi.org/10.1090/S0025-5718-2013-02716-0
[240]: https://dx.doi.org/10.1090/S0025-5718-2015-02930-5
[241]: http://web.math.princeton.edu/sarnak/MazurLtrMay08.PDF
[242]: https://dx.doi.org/10.1023/B:AMHU.0000024681.23784.d1
[243]: https://dx.doi.org/10.1007/s10474-018-0884-x
[244]: https://dx.doi.org/10.1007/BF01444344
[245]: https://dx.doi.org/10.1112/mtk.12150
[246]: https://dx.doi.org/10.2307/2004737
[247]: http://math101.guru/en/downloads-2/repository/
[248]: https://arxiv.org/pdf/2405.01512
[249]: https://dx.doi.org/10.1112/jlms/s1-8.4.277
[250]: https://dx.doi.org/10.1112/plms/s3-5.1.48
[251]: http://gateway.proquest.com/openurl?url_ver=Z39.88-2004&amp;rft_val_fmt=info:ofi/fmt:kev:mtx:dissertation&amp;res_dat=xri:pqdiss&amp;rft_dat=xri:pqdiss:3411454
[252]: https://dx.doi.org/10.1007/BF02024389
[253]: https://dx.doi.org/10.2307/2004774
[254]: https://dx.doi.org/10.2307/2036123
[255]: https://dx.doi.org/10.4064/aa-18-1-311-320
[256]: https://dx.doi.org/10.4064/aa-6-4-435-446
[257]: https://dx.doi.org/10.4064/aa-10-4-359-368
[258]: https://dx.doi.org/10.4064/aa-31-2-153-165
[259]: https://dx.doi.org/10.1070/RM1996v051n06ABEH003000
[260]: https://dx.doi.org/10.1007/BF02564539
[261]: https://dx.doi.org/10.1007/BF01707854
[262]: https://dx.doi.org/10.1090/S0025-5718-2011-02477-4
[263]: https://dx.doi.org/10.4064/aa-66-1-63-69
[264]: https://dx.doi.org/10.3836/tjm/1270216093
[265]: https://dx.doi.org/10.3836/tjm/1270472994
[266]: https://dx.doi.org/10.1007/BF02021308
[267]: https://dx.doi.org/10.1007/BF02024493
[268]: https://dx.doi.org/10.1007/BF02023928
[269]: https://dx.doi.org/10.1007/BF02022552
[270]: https://dx.doi.org/10.4064/cm-23-2-309-321
[271]: https://dx.doi.org/10.2307/2371183
[272]: https://dx.doi.org/10.2307/2371519
