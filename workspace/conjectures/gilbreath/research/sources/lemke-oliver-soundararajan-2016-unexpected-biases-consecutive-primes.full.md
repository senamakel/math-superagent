<!-- source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4978288/ | converted from HTML -->

Unexpected biases in the distribution of consecutive primes - PMC Skip to main content

**Official websites use .gov**
A **.gov**website belongs to an official government organization in the United States.

**Secure .gov websites use HTTPS**
A **lock**( Lock Locked padlock icon ) or **https://**means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.

[1]

[image: PMC search open icon][image: PMC search close ison]

- [Journal List][2]
- [User Guide][3]

- [image: Open resources icon]
- [image: View on publisher site icon] [4]
- [image: Download PDF icon] [5]
- [image: Collections icon][image: Collections icon]
- [image: Cite icon]
- [image: Show article permalink icon]

## PERMALINK

[image: Copy icon] Copy

[image: Open article navigation icon]

As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with, the contents by NLM or the National Institutes of Health.
Learn more: [PMC Disclaimer][6] | [PMC Copyright Notice][7]

[image: Proceedings of the National Academy of Sciences of the United States of America logo]

Proc Natl Acad Sci U S A

. 2016 Jul 14;113(31):E4446–E4454. doi: [10.1073/pnas.1605366113][4]

# Unexpected biases in the distribution of consecutive primes

[Robert J Lemke Oliver][8]

### Robert J Lemke Oliver

a Department of Mathematics, Stanford University, Stanford, CA 94305;

b Department of Mathematics, Tufts University, Medford, MA 02155

Find articles by [Robert J Lemke Oliver][8]

a, b, 1, [Kannan Soundararajan][9]

### Kannan Soundararajan

a Department of Mathematics, Stanford University, Stanford, CA 94305;

Find articles by [Kannan Soundararajan][9]

a, 1

- Author information
- Article notes
- Copyright and License information

a Department of Mathematics, Stanford University, Stanford, CA 94305;

b Department of Mathematics, Tufts University, Medford, MA 02155

1

To whom correspondence may be addressed. Email: robert.lemke_oliver@tufts.edu or ksound@stanford.edu.

Edited by Kenneth A. Ribet, University of California, Berkeley, CA, and approved May 13, 2016 (received for review April 1, 2016)

Author contributions: R.J.L.O. and K.S. wrote the paper.

### Series information

PNAS Plus

Issue date 2016 Aug 2.

[PMC Copyright notice][7]

PMCID: PMC4978288 PMID: [27418603][10]

See " [PNAS Plus Significance Statements][11] " on page 8574.

## Significance

Prime numbers play a central role in analytic number theory, and are well known to be very well distributed among the reduced residue classes ( mod q). Surprisingly, the same does not appear to be true for sequences of consecutive primes, with different patterns occurring with wildly different frequencies. We formulate a precise conjecture, based on the Hardy−Littlewood conjectures, which explains this phenomenon. In particular, we predict that all patterns do occur their fair share of the time in the limit, but that there are secondary terms only very slowly tending to zero that create the observed biases.

**Keywords:**prime numbers, consecutive primes, Hardy–Littlewood conjectures, singular series

## Abstract

Although the sequence of primes is very well distributed in the reduced residue classes ( mod q), the distribution of pairs of consecutive primes among the permissible *ϕ*(*q*) 2 pairs of reduced residue classes ( mod q) is surprisingly erratic. This paper proposes a conjectural explanation for this phenomenon, based on the Hardy−Littlewood conjectures. The conjectures are then compared with numerical data, and the observed fit is very good.

## 1. Introduction

The prime number theorem in arithmetic progressions shows that the sequence of primes is equidistributed among the reduced residue classes ( mod q). If the Generalized Riemann Hypothesis is true, then this holds in the more precise form

π ( x; q, a) = li ( x) ϕ ( q) + O ( x 1 / 2 + ϵ), where li ( x) ≔ ∫ 2 x d t log ⁡ t, |

and π ( x; q, a) denotes the number of primes up to *x*lying in the reduced residue class a ( mod q). Nevertheless, it was noticed by Chebyshev that certain residue classes seem to be slightly preferred; for example, among the first million primes, we find that

π ( x 0; 3,1) = 499,829 and π ( x 0; 3,2) = 500,170, π ( x 0) = 10 6. |

Chebyshev’s bias is beautifully explained by the work of Rubinstein and Sarnak ( 1) (see ref. 2 for a survey of related work), who showed (in a certain sense and under some natural conjectures) that π ( x; 3,2) > π ( x; 3,1) for 99.9 % of all positive *x*.

What happens if we consider the patterns of residues ( mod q) among strings of consecutive primes? Let p n denote the sequence of primes in ascending order. Let r ≥ 1 be an integer, and let a = ( a 1, a 2, …, a r) denote an *r*-tuple of reduced residue classes ( mod q). Define

π ( x; q, a) ≔ #{ p n ≤ x: p n + i − 1 ≡ a i ( mod q) for each 1 ≤ i ≤ r }, |

which counts the number of occurrences of the pattern a ( mod q) among *r*consecutive primes the least of which is below *x*. When r ≥ 2, little is known about the distribution of such patterns among the primes. When r = 2 and ϕ ( q) = 2 (thus q = 3, 4, or 6), Knapowski and Turán ( 3) observed that all of the four possible patterns of length 2 appear infinitely many times. The main significant result in this direction is due to Shiu ( 4), who established that, for any q ≥ 3, a reduced residue class a ( mod q), and any r ≥ 2, the pattern ( a, a, …, a) occurs infinitely often. Recent progress in sieve theory has led to a new proof of Shiu’s result (see ref. 5), and, moreover, Maynard ( 6) has shown that π ( x; q, ( a, …, a)) ≫ π ( x).

Despite the lack of understanding of π ( x; q, a), any model based on the randomness of the primes would suggest strongly that every permissible pattern of *r*consecutive primes appears roughly equally often; that is, if a is an *r*-tuple of reduced residue classes ( mod q), then π ( x; q, a) ∼ π ( x) / ϕ ( q) r. However, a look at the data might shake that belief! For example, among the first million primes (for convenience, restricting to those greater than 3), we find

π ( x 0; 3, ( 1,1)) = 215,873, π ( x 0; 3, ( 1,2)) = 283,957, π ( x 0; 3, ( 2,1)) = 283,957, and π ( x 0; 3, ( 2,2)) = 216,213. |

These numbers show substantial deviations from the expectation that all four quantities should be roughly 250,000. Further, Chebyshev’s bias ( mod 3) might have suggested a slight preference for the pattern ( 2,2) over the other possibilities, and this is clearly not the case.

The discrepancy observed above persists for larger *x*, and also exists for other moduli *q*. For example, among the first hundred million primes modulo 10, there is substantial deviation from the prediction that each of the 16 pairs ( a, b) should have about 6.25 million occurrences. Specifically, with π ( x 0) = 10 8, we find the following.

[image: graphic file with name pnas.1605366113t01.jpg] |

[Open in a new tab][12]

Apart from the fact that the entries vary dramatically (much more than in Chebyshev’s bias), the key feature to be observed in these data is that the diagonal classes ( a, a) occur significantly less often than the nondiagonal classes. Chebyshev’s bias ( mod 10) states that the residue classes 3 and 7 ( mod 10) very often contain slightly more primes than the residue classes 1 and 9 ( mod 10), but curiously in our data the patterns ( 3,3) and ( 7,7) appear less frequently than ( 1,1) and ( 9,9); this suggests again that a different phenomenon is at play here.

The purpose of this paper is to develop a heuristic, based on the Hardy−Littlewood prime *k*-tuples conjecture, which explains the biases seen above. We are led to conjecture that although the primes counted by π ( x; q, a) do have density 1 / ϕ ( q) r in the limit, there are large secondary terms in the asymptotic formula which create biases toward and against certain patterns. The dominant factor in this bias is determined by the number of *i*for which a i + 1 ≡ a i ( mod q), but there are also lower-order terms that do not have an easy description.

### Main Conjecture.

*With notation as above, we have*

π ( x; q, a) = li ( x) ϕ ( q) r ( 1 + c 1 ( q; a) log log x log x + c 2 ( q; a) 1 log x + O ( 1 ( log x) 7 / 4)), |

*where*

c 1 ( q; a) = ϕ ( q) 2 ( r − 1 ϕ ( q) − #{ 1 ≤ i < r: a i ≡ a i + 1 ( m o d q) }). |

*When*r = 2*, the constant*c 2 ( q; a)*is given in***[2.23]**. *If*r ≥ 3*, it is given by*

c 2 ( q; a) = ∑ i = 1 r − 1 c 2 ( q; ( a i, a i + 1)) + ϕ ( q) 2 ∑ j = 1 r − 2 1 j ( r − 1 − j ϕ ( q) − #{ i: a i ≡ a i + j + 1 ( m o d q) }). |

In general, the quantity c 2 ( q; a) seems complicated, but there are some situations where it simplifies. For example, if a = ( a, a) for a reduced residue class a ( mod q), then, regardless of the choice of *a*, we have

c 2 ( q; ( a, a)) = ϕ ( q) log ( q / 2 π) + log ⁡ 2 ⁡ π 2 − ϕ ( q) 2 ∑ p | q log ⁡ p p − 1. | [1.1] |

We can also show that c 2 ( q; ( a, b)) = c 2 ( q; ( − b, − a)) for any two reduced residue classes *a*and b ( mod q). Moreover, although c 2 ( q; ( a, b)) seems involved, the symmetric quantity c 2 ( q; ( a, b)) + c 2 ( q; ( b, a)) simplifies nicely: For distinct reduced residue classes *a*, b ( mod q), we have

c 2 ( q; ( a, b)) + c 2 ( q; ( b, a)) = log ( 2 π) − ϕ ( q) Λ ( q / ( q, b − a)) ϕ ( q / ( q, b − a)), | [1.2] |

where Λ denotes the von Mangoldt function. In particular, this expression depends only on the difference b − a.

**Conjecture 1.1.***If a and b are distinct reduced residue classes*( m o d q), *then*π ( x; q, ( a, b)) + π ( x; q, ( b, a))*equals*

2 li ( x) ϕ ( q) 2 ( 1 + log ⁡ log x 2 ⁡ log x + ( log ( 2 π) − ϕ ( q) Λ ( q / ( q, b − a)) ϕ ( q / ( q, b − a))) 1 2 ⁡ log x + O ( 1 ( log x) 7 / 4)), |

*whereas*π ( x; q, ( a, a))*equals*

li ( x) ϕ ( q) 2 ( 1 − ϕ ( q) − 1 2 log ⁡ log x log x + ( ϕ ( q) log q 2 π + log ⁡ 2 ⁡ π − ϕ ( q) ∑ p | q log ⁡ p p − 1) 1 2 ⁡ log x + O ( 1 ( log x) 7 / 4)). |

We give a few amusing consequences of the Main Conjecture. The famous biases π ( x) < li ( x), or π ( x; 3,1) < π ( x; 3,2), or π ( x; 4,1) < π ( x; 4, − 1) are known to be false infinitely often. However, we conjecture that the robust biases in pairs of consecutive primes ( mod 3) or ( mod 4) may hold always and from the very start!

**Conjecture 1.2.***Let*q = 3*or*4, *and let a be either*1 ( m o d q)*or*− 1 ( m o d q). *Then, for all*x ≥ 5, *we have*

π ( x; q, ( a, − a)) > π ( x; q, ( a, a)). |

*Indeed, for large x, we have*

π ( x; q, ( a, − a)) − π ( x; q, ( a, a)) = x 4 ( log x) 2 log ( 2 π q log x) + O ( x ( log x) 11 / 4). |

Given a prime *q*, the product of two consecutive primes prefers to be a quadratic nonresidue rather than a quadratic residue.

**Conjecture 1.3.***Let q be a fixed odd prime. For large x, we have*

∑ p n ≤ x ( p n q) ( p n + 1 q) = − x 2 ( log x) 2 log ( 2 π ⁡ log x q) + O ( x ( log x) 11 / 4). |

The constants in the Main Conjecture also simplify dramatically if one only cares about patterns exhibited by p n and p n + k for k ≥ 2.

**Conjecture 1.4.***If*k ≥ 2*and a and b are distinct reduced residues*( m o d q), *then*

#{ p n ≤ x: p n ≡ a ( m o d q), p n + k ≡ b ( m o d q) } = li ( x) ϕ ( q) 2 ( 1 + 1 2 ( k − 1) 1 log x + O ( 1 ( log x) 7 / 4)), |

*while*

#{ p n ≤ x: p n ≡ p n + k ≡ a ( m o d q) } = li ( x) ϕ ( q) 2 ( 1 − ϕ ( q) − 1 2 ( k − 1) 1 log x + O ( 1 ( log x) 7 / 4)). |

Form a ϕ ( q) × ϕ ( q) transition matrix (with rows and columns indexed by reduced residue classes) and the ( a, b) th entry being the probability that a prime p n ≡ a ( mod q) is followed by p n + 1 ≡ b ( mod q). Then Conjecture 1.4 shows that the corresponding transition matrix going from p n to p n + 2 is not the square of the transition matrix going from p n to p n + 1. Thus, the primes ( mod q) are not Markovian, and this may also be seen directly from the Main Conjecture by the formula given for c 2 ( q; a) when r ≥ 3 (which is used to derive Conjecture 1.4).

The ideas that lead to the Main Conjecture imply that there will be symmetries between the number of occurrences of different patterns.

**Conjecture 1.5.***Given*a*and q as above, define*a opp = ( − a r, − a r − 1, …, − a 1). *For large x, we have*

π ( x; q, a) = π ( x; q, a opp) + O ( x 1 / 2 + ϵ). |

*Example*. We find

π ( 10 11; 7, ( 1,6,3)) = 24,344,117 |

and

π ( 10 11; 7, ( 4,1,6)) = 24,349,025, |

while the nearest number of occurrences of another pattern is

π ( 10 11; 7, ( 6,2,1)) = 24,570,765. |

If the modulus is a prime power, there are additional symmetries.

**Conjecture 1.6.***Let q be a prime and let*v ≥ 2. *If*a = ( a 1, …, a r)*and*b = ( b 1, …, b r)*are such that*a 1 ≡ b 1 ( m o d q)*and*a i + 1 − a i ≡ b i + 1 − b i ( m o d q v)*for each*1 ≤ i < r, *then*

π ( x; q v, a) = π ( x; q v, b) + O ( x 1 / 2 + ϵ). |

*In particular, if a is odd, then, up to an error*O ( x 1 / 2 + ϵ), π ( x; 2 v, ( a, b))*depends only on*b − a ( m o d 2 v).

*Example*. We find

π ( 10 11; 8, ( 1,3)) = 278,676,326, π ( 10 11; 8, ( 3,5)) = 278,696,997, π ( 10 11; 8, ( 5,7)) = 278,692,843, and π ( 10 11; 8, ( 7,1)) = 278,681,776. |

In the direction of these conjectures, the earliest work we found is the paper of Knapowski and Turán ( 3), who “guess” that the events p n ≡ a ( mod 4) and p n + 1 ≡ b ( mod 4) for the four possibilities of *a*and *b*are “not equally probable.” However, Knapowski and Turán go on to suggest that π ( x; 4, ( 1,1)) = o ( π ( x)), which is now definitively false by Maynard’s work ( 6). The paper ( 3) was published after the death of both authors, and perhaps they had something else in mind, maybe along the lines of our Conjecture 1.2 above? More recently, in Ko ( 7), numerical results observing the biases in the distribution of consecutive primes for small moduli are given. The paper by Ash, Beltis, Gross, and Sinnott ( 8) again observes these biases in pairs of consecutive primes and initiates an attempt toward understanding them based on the Hardy−Littlewood conjectures. The heuristic expression in ref. 8 is a large sum of singular series, and, as the authors note, it is unclear from that expression whether π ( x; q, ( a, b)) tends to π ( x) / ϕ ( q) 2 for large *x*. They also note symmetries akin to Conjectures 1.5 and 1.6 for pairs of consecutive primes.

In the Main Conjecture, we expect that the remainder term O ( ( log x) − 7 / 4) is given by a sum involving the zeros of Dirichlet *L*-functions ( mod q). The main terms given in the Main Conjecture are the same for all repeating patterns ( a, a, …, a); nevertheless, numerically, one observes some deviations in the counts of such patterns, and we expect the lower-order fluctuations to account for these deviations. In addition to the contributions from zeros, which we expect to be oscillating, there also appear to be nonoscillating lower-order terms of size ( log log x / log x) 2, which may play a bigger role for the computable ranges of *x*. We hope to understand these lower-order terms in future work.

An initial guess for why there is a bias against the repeating patterns might be that, after a prime occurs that is a ( mod q), all other classes have a chance to represent a prime before *a*occurs again. However, a straightforward application of the Selberg sieve shows that the number of primes for which p n + 1 − p n < q is O ( x / log 2 x), which is of a smaller order of magnitude than the bias predicted by the Main Conjecture.

Although we do not pursue this here, it should be possible to prove unconditional analogs of the Main Conjecture in other settings, for example, to numbers free of small prime factors or for squarefree integers (in the latter case, the biases will be manifested already at the level of the constant in the main term). More generally, analogous biases seem to arise for many other sifted sets, for example, in the sums of two squares. We also mention two other settings in which large biases are seen: the distribution of prime geodesics for compact hyperbolic surfaces into various homology classes (see the discussion at the end of ref. 1) and the recent work of Dummit, Granville, and Kisilevsky ( 9) concerning the distribution of numbers that are products of two primes.

## 2. The Heuristic for r = 2

In this section, we develop a heuristic explanation of the Main Conjecture in the case r = 2. The heuristic (like several other conjectures about the primes; see, for example, refs. 10 – 14) is based upon the Hardy−Littlewood prime *k*-tuples conjecture. We begin by reviewing quickly the Hardy−Littlewood conjectures and some related results, before proceeding to develop an analog suitable for understanding π ( x; q, a).

### 2.1. The Hardy−Littlewood Conjectures.

Let ℋ be a finite subset of Z, and let 1 P denote the characteristic function of the primes. In a strong form, the Hardy−Littlewood conjecture asserts that

∑ n ≤ x ∏ h ∈ ℋ 1 P ( n + h) = S ( ℋ) ∫ 2 x d y ( log y) | ℋ | + O ( x 1 / 2 + ϵ), |

where the singular series S ( ℋ) is given by

S ( ℋ) = ∏ p ( 1 − #( ℋ mod p) p) ( 1 − 1 p) − | ℋ |. |

In our calculations, it will be important to understand the behavior of the singular series “on average.” Here, Gallagher ( 10) established that, for any k ≥ 1 and as h → ∞,

∑ ℋ ⊆ [1, h] | ℋ | = k S ( ℋ) ∼ ( h k) ∼ h k k!, | [2.1] |

so that the singular series is 1 on average. A refined version of this asymptotic was established by Montgomery and Soundararajan ( 13), who introduced the modified singular series

S 0 ( ℋ) = ∑ T ⊂ ℋ ( − 1) | ℋ \ T | S ( T), so that S ( ℋ) = ∑ T ⊂ ℋ S 0 ( T), |

with S ( ∅) = S 0 ( ∅) = 1. The modified singular series S 0 arises naturally in the following version of the Hardy−Littlewood conjecture (thinking of the elements of ℋ as being small in comparison with *x*):

∑ n ≤ x ∏ h ∈ ℋ ( 1 P ( n + h) − 1 log ⁡ n) = S 0 ( ℋ) ∫ 2 x d y ( log y) | ℋ | + O ( x 1 / 2 + ϵ), |

and the term 1 / log ⁡ n that is subtracted above arises naturally as the probability that the “random number” n + h is prime. Montgomery and Soundararajan showed that

∑ ℋ ⊆ [1, h] | ℋ | = k S 0 ( ℋ) = μ k k! ( − h ⁡ log ⁡ h + A h) k / 2 + O k ( h k / 2 − 1 / ( 7 k) + ϵ), | [2.2] |

where μ k is the *k*th moment of the standard Gaussian (in particular, μ k = 0 if *k*is odd) and *A*is a constant independent of *k*. This refines Gallagher’s asymptotic **[2.1]**, and shows that S 0 ( ℋ) exhibits roughly square-root cancellation in each variable.

### 2.2. Modified Hardy−Littlewood Conjectures.

We need a slight modification of the Hardy−Littlewood conjecture, taking into account congruence conditions ( mod q). For any integer q ≥ 1 and a finite subset ℋ of the integers, we define the singular series at the primes away from *q*by

S q ( ℋ) ≔ ∏ p ∤ q ( 1 − #( ℋ mod p) p) ( 1 − 1 p) − | ℋ |. |

If a ( mod q) is such that ( h + a, q) = 1 for all h ∈ ℋ, then we expect that

∑ n < x n ≡ a ( mod q) ∏ h ∈ ℋ 1 P ( n + h) ∼ S q ( ℋ) ( q ϕ ( q)) | ℋ | 1 q ∫ 2 x d y ( log y) | ℋ |, | [2.3] |

where the factor ( q / ϕ ( q)) | ℋ | arises because h + a is conditioned to be coprime to *q*for all h ∈ ℋ, and the factor 1 / q arises because we are restricting *n*to one residue class ( mod q). In analogy with S 0, it is also useful to define S q, 0 ( ℋ) ≔ ∑ T ⊆ ℋ ( − 1) | ℋ \ T | S q ( T), so that S q ( ℋ) = ∑ T ⊆ ℋ S q, 0 ( T). Once again, the quantity S q, 0 arises naturally in the asymptotic [conditioning ( h + a, q) = 1 for all h ∈ ℋ]

∑ n ≤ x n ≡ a ( mod q) ∏ h ∈ ℋ ( 1 P ( n + h) − q ϕ ( q) log ⁡ n) ∼ S q, 0 ( ℋ) ( q ϕ ( q)) | ℋ | 1 q ∫ 2 x d y ( log y) | ℋ |, | [2.4] |

where the term q / ( ϕ ( q) log ⁡ n) being subtracted arises naturally as the probability that n + h is prime, conditioned on the fact that n + h is coprime to *q*.

### 2.3. First Steps Toward the Conjecture.

Let *a*and *b*be two reduced residue classes ( mod q), and let *h*be a positive integer with h ≡ b − a ( mod q). We now formulate a conjecture for the number of primes n ≤ x with n ≡ a ( mod q) and such that the next prime after *n*is n + h. The gaps between consecutive primes are conjectured to be distributed like a Poisson process with mean ∼ log x (and Gallagher showed that this follows from the Hardy−Littlewood conjectures), and so *h*should be thought of as a parameter on the scale of log x. With this in mind, we are interested in

∑ n ≤ x n ≡ a ( mod q) 1 P ( n) 1 P ( n + h) ∏ 0 < t < h ( t + a, q) = 1 ( 1 − 1 P ( n + t)) = ∑ n ≤ x n ≡ a ( mod q) 1 P ( n) 1 P ( n + h) ∏ 0 < t < h ( t + a, q) = 1 ( 1 − q ϕ ( q) log ( n + t) − 1 ˜ P ( n + t)), | [2.5] |

where, for a variable *n*conditioned to be coprime to *q*, we set 1 ˜ P ( n) = 1 P ( n) − q / ( ϕ ( q) log ⁡ n). Write also 1 P ( n) = q / ( ϕ ( q) log ⁡ n) + 1 ˜ P ( n) and similarly for 1 P ( n + h), and then expand out the product in **[2.5]**; thus we arrive at [ignoring the small differences between log ⁡ n, log ( n + h) or log ( n + t)]

∑ A ⊂ { 0, h } ∑ T ⊂ [1, h − 1] ( t + a, q) = 1 ∀ t ∈ T ( − 1) | T | ∑ n ≤ x n ≡ a ( mod q) ( q ϕ ( q) log ⁡ n) 2 − | A | ∏ t ∈ [1, h − 1] ( t + a, q) = 1 t ∈ T ( 1 − q ϕ ( q) log ⁡ n) ∏ t ∈ A ∪ T 1 ˜ P ( n + t). | [2.6] |

Given reduced residue classes *a*and *b*, and a positive h ≡ b − a ( mod q), we may write

#{ 0 < t < h: ( t + a, q) = 1 } = ϕ ( q) q h + ϵ q ( a, b), | [2.7] |

where ϵ q ( a, b) is independent of *h*. We also write, for convenience,

α ( y) = 1 − q ϕ ( q) log y. | [2.8] |

Appealing now to the conjectured relation **[2.4]**, we are led to hypothesize that the quantity in **[2.5]**(and **[2.6]**) is

∼ ∑ A ⊂ { 0, h } ∑ T ⊂ [1, h − 1] ( t + a, q) = 1 ∀ t ∈ T ( − 1) | T | S q, 0 ( A ∪ T) ( 1 q ∫ 2 x ( q ϕ ( q) log y) 2 + | T | α ( y) h ϕ ( q) / q + ϵ q ( a, b) − | T | d y). | [2.9] |

Before proceeding further, a few points are in order. Note that α ( x) h ϕ ( q) / q is about e − h / log x, and this exponential decay in *h*is in keeping with the conjecture that gaps between consecutive primes are distributed like a Poisson process. Secondly, by replacing A and T above with h − A and h − T, and noting also that ϵ q ( a, b) = ϵ q ( − b, − a), we may see that the quantity **[2.9]**above does not change if we replace ( a, b) by ( − b, − a); this is an example of the symmetry between π ( x; q, a) and π ( x; q, a opp) noted in Conjecture 1.5. Similarly, under the hypotheses of Conjecture 1.6, the conditions satisfied by *h*and T are exactly the same for π ( x; q, a) and π ( x; q, b). Lastly, in arriving at **[2.9]**, we have paid no attention to error terms, and, moreover, have used a uniform version of the Hardy−Littlewood conjecture both in terms of the size of the parameters in the set A ∪ T (this is relatively minor) and in terms of the size of the set A ∪ T. To mitigate the last point, we note that, in expanding out the inclusion−exclusion product in **[2.5]**, we may obtain upper and lower bounds by stopping after an odd or an even number of steps (as in Brun’s sieve, for example); in this manner, only a mildly uniform version of the Hardy−Littlewood conjectures seems needed. For the present, we ignore these details, but it would be desirable to place the conjecture **[2.9]**on a firmer footing.

With conjecture **[2.9]**in hand, we have a conjecture for π ( x; q, ( a, b)): Namely, we sum the quantity in **[2.9]**over all positive integers h ≡ b − a ( mod q). Thus, we expect that

π ( x; q, ( a, b)) ∼ 1 q ∫ 2 x α ( y) ϵ q ( a, b) ( q ϕ ( q) log y) 2 D ( a, b; y) d y, | [2.10] |

say, where

D ( a, b; y) = ∑ h > 0 h ≡ b − a ( mod q) ∑ A ⊂ { 0, h } ∑ T ⊂ [1, h − 1] ( t + a, q) = 1 ∀ t ∈ T ( − 1) | T | S q, 0 ( A ∪ T) ( q ϕ ( q) α ( y) log y) | T | α ( y) h ϕ ( q) / q. | [2.11] |

### 2.4. Discarding Singular Series Involving Sets with Three or More Elements.

We now conjecture that only terms with A = T = ∅ [which gives rise to the main term of li ( x) / ϕ ( q) 2 for π ( x; q, ( a, b))] and | A | + | T | = 2 give significant contributions leading to the Main Conjecture, and that all other terms contribute to π ( x; q, ( a, b)) an amount O ( x ( log log x) 2 / ( log x) 3). To argue this, we will use as a guide the work of Montgomery and Soundararajan ( 13), in particular **[2.2]**above, which shows that sums over singular series exhibit square-root cancellation in each variable.

Suppose, for example, that A = ∅ and | T | = ℓ ≥ 4 in **[2.11]**. After summing over the variable *h*, these terms may be thought of as ( log y) 1 − ℓ times an average of S q, 0 ( T) over ℓ element sets T whose elements are all of size about log ⁡ y. The estimate **[2.2]**now suggests that this contribution is ≪ ( log log y) ℓ / 2 ( log y) 1 − ℓ / 2, and, because ℓ ≥ 4, the final contribution to π ( x; q, ( a, b)) is O ( x ( log log x) 2 / ( log x) 3). If ℓ = 3, then the same argument—drawing on **[2.2]**with k = 3 there, so that the main term there vanishes and the bound is O ( h 3 / 2 − 1 / 21 + ϵ) —indicates that such terms contribute to π ( x; q, ( a, b)) an amount O ( x ( log x) − 5 / 2 − 1 / 21 + ϵ) that is already smaller than the secondary main terms claimed in the Main Conjecture. We believe that, when *k*is odd, the work of Montgomery and Soundararajan ( 13) can be refined, and the actual size of the sum in **[2.2]**is h ( k − 1) / 2 ( log ⁡ h) ( k + 1) / 2. This expectation suggests that the terms with A = ∅ and | T | = 3 also make a contribution of O ( x ( log log x) 2 / ( log x) 3).

When A = { 0 } or { h }, then a similar heuristic to the above shows that terms with | T | ≥ 2 make a contribution to π ( x; q, ( a, b)) of O ( x ( log log x) 2 / ( log x) 3). Finally, if A = { 0, h } and | T | = ℓ ≥ 1, then the contribution to **[2.11]**may be roughly thought of as ( log y) − ℓ times an average of singular series S q, 0 ( { 0 } ∪ T +) where T + (standing for T ∪ { h }) runs over ℓ + 1 element sets with elements of size log y. Because the singular series S q, 0 is translation-invariant, one can think of this last sum as being 1 / ( log y) times the average over ℓ + 2 element sets with all elements of size log y. After making this observation, we can draw on **[2.2]**(with its proposed refinement for odd *k*) as earlier, and this leads to the prediction that the contribution to π ( x; q, ( a, b)) of terms with A = { 0, h } and any nonempty T is O ( x ( log log x) 2 / ( log x) 3).

Thus, discarding all terms with | A | + | T | ≥ 3, we now replace the density D ( a, b; y) in **[2.11]**with

D ( a, b; y) = D 0 ( a, b; y) + D 1 ( a, b; y) + D 2 ( a, b; y), | [2.12] |

where (keeping in mind that S q, 0 is 1 for the empty set and 0 for a singleton)

D 0 ( a, b; y) = ∑ h > 0 h ≡ b − a ( mod q) ( 1 + S q, 0 ( { 0, h })) α ( y) h ϕ ( q) / q, | [2.13] |

D 1 ( a, b; y) = − q ϕ ( q) α ( y) log y ∑ h > 0 h ≡ b − a ( mod q) ∑ t ∈ [1, h − 1] ( t + a, q) = 1 ( S q, 0 ( { 0, t }) + S q, 0 ( { t, h }) α ( y) h ϕ ( q) / q), | [2.14] |

and

D 2 ( a, b; y) = ( q ϕ ( q) α ( y) log y) 2 ∑ h > 0 h ≡ b − a ( mod q) ∑ 1 ≤ t 1 < t 2 < h ( t 1 + a, q) = ( t 2 + a, q) = 1 S q, 0 ( { t 1, t 2 }) α ( y) h ϕ ( q) / q. | [2.15] |

Inserting this in **[2.10]**, we thus conjecture that, up to O ( x ( log log x) 2 / ( log x) 3), there holds

π ( x; q, ( a, b)) = q ϕ ( q) 2 ∫ 2 x α ( y) ϵ q ( a, b) ( log y) 2 ( D 0 + D 1 + D 2) ( a, b; y) d y. | [2.16] |

### 2.5. The Main Proposition.

To evaluate the sums over two-term singular series above, we invoke the following proposition whose proof we defer to *Section 3*, *Proof of the Proposition*.

**Proposition 2.1.***Let*q ≥ 2, *and let*v ( m o d q) be any residue *class*. *For any positive real number H*, *define*

S 0 ( q, v; H) = ∑ h > 0 h ≡ v ( m o d q) S q, 0 ( { 0, h }) e − h / H. |

*Then we may write*

S 0 ( q, 0; H) = − ϕ ( q) 2 q log ⁡ H + S 0 c ( q, 0) + Z q, 0 ( H) + O ( H − 1 + ϵ), |

*where*

S 0 c ( q, 0) = ϕ ( q) 2 q log q 2 π − ϕ ( q) 2 q ∑ p | q log ⁡ p p − 1 + 1 2, |

*and, for any*v ( m o d q), *the quantity*Z q, v ( H)*is described in***[3.2]***below*, *satisfies the bound*Z q, v ( H) = O ( H − 1 / 2 + ϵ), *and which we conjecture to be*O ( H − 3 / 4). *Further*, *if*( v, q) = d*with*d < q, *then*

S 0 ( q, v; H) = S 0 c ( q, v) + Z q, v ( H) + O ( H − 1 + ϵ), |

*where*

S 0 c ( q, v) = − ϕ ( q) 2 q ⋅ Λ ( q / d) ϕ ( q / d) − B q ( v) + 1 ϕ ( q / d) ∑ χ ≠ χ 0 ( m o d q / d) χ ¯ ( v / d) L ( 0, χ) L ( 1, χ) A q, χ, |

*with*B q ( v) = 1 / 2 − v / q*for*1 ≤ v ≤ q*and extended periodically for all v*, *and*

A q, χ = ∏ p | q ( 1 − χ ( p) p) ∏ p ∤ q ( 1 − ( 1 − χ ( p)) 2 ( p − 1) 2). |

### 2.6. Completing the Heuristic.

Returning to our heuristic calculation, we will apply Proposition 2.1 with

H = H ( y) ≔ − q ϕ ( q) ⋅ 1 log ⁡ α ( y) = log y − q 2 ϕ ( q) + O ( 1 log y). | [2.17] |

We begin by simplifying a bit the expressions for D 0, D 1, and D 2, discarding terms of size O ( log log y / log y), which are negligible for the Main Conjecture. Thus, after summing the geometric series and using **[2.17]**,

D 0 = S 0 ( q, b − a; H) + ∑ h ≡ b − a ( mod q) e − h / H = S 0 ( q, b − a; H) + H q + B q ( b − a) + O ( 1 H) = log y q + S 0 ( q, b − a; H) + B q ( b − a) − 1 2 ϕ ( q) + O ( 1 log y). | [2.18] |

The definition of D 1 involves two singular series, S q, 0 ( { 0, t }) and S q, 0 ( { t, h }). Consider the terms arising from the second case. Replace S q, 0 ( { t, h }) by S q, 0 ( { 0, r }) where r = h − t also lies in [1, h − 1] and note that the condition ( t + a, q) = 1 becomes ( r − b, q) = 1. Thus, ignoring terms of size O ( log log y / log y), the second case in D 1 contributes

− q ϕ ( q) α ( y) log y ∑ r > 0 ( r − b, q) = 1 S q, 0 ( { 0, r }) ∑ h > r h ≡ b − a ( mod q) e − h / H = − 1 ϕ ( q) ∑ v ( mod q) ( v − b, q) = 1 S 0 ( q, v; H). |

Arguing similarly with the first case, we conclude that

D 1 = − 1 ϕ ( q) ∑ v ( mod q) ( v + a, q) = 1 S 0 ( q, v; H) − 1 ϕ ( q) ∑ v ( mod q) ( v − b, q) = 1 S 0 ( q, v; H) + O ( log log y log y). | [2.19] |

Finally, note that

∑ h ≡ b − a ( mod q) e − h / H ∑ 1 ≤ t 1 < t 2 < h ( t 1 + a, q) = 1 ( t 2 + a, q) = 1 S q, 0 ( { t 1, t 2 }) = ∑ 1 ≤ t 1 < t 2 < h ( t 1 + a, q) = 1 ( t 2 + a, q) = 1 S q, 0 ( { 0, t 2 − t 1 }) ∑ h ≡ b − a ( mod q) h > t 2 e − h / H = H 2 q 2 ∑ v 1, v 2 ( mod q) ( v 1, q) = 1 ( v 2, q) = 1 S 0 ( q, v 2 − v 1; H) + O ( H log H), |

so that

D 2 = 1 ϕ ( q) 2 ∑ v 1, v 2 ( mod q) ( v 1, q) = 1 ( v 2, q) = 1 S 0 ( q, v 2 − v 1; H) + O ( log log y log y). | [2.20] |

Using Proposition 2.1 to evaluate **[2.18]**, **[2.19]**, and **[2.20]**and then inserting that in **[2.10]**leads to the Main Conjecture. The term involving c 1 ( q; ( a, b)) arises from terms involving S 0 ( q, 0; H), which has a leading term of size log ⁡ H whereas all other S 0 ( q, v; H) are only of constant size. Thus, isolating the − [ϕ ( q) / 2 q] log ⁡ H leading contribution to S 0 ( q, 0; H) and tracking its appearance in our expressions for D 0, D 1 and D 2 gives

− ϕ ( q) 2 q ( log H) δ ( a = b) − 2 ϕ ( q) ( − ϕ ( q) 2 q log H) + 1 ϕ ( q) ( − ϕ ( q) 2 q log H) = ϕ ( q) 2 q ( log log y) ( 1 ϕ ( q) − δ ( a = b)) + O ( log log y log y). |

The term involving c 2 ( q; ( a, b)) is complicated, but follows straightforwardly from our work above. Having already treated the − [ϕ ( q) / 2 q] log ⁡ H term arising in S 0 ( q, 0), the contributions leading to c 2 ( q; ( a, b)) come from the S 0 c ( q, v) terms in Proposition 2.1. We thus have

c 2 ( q; a) q = − ε q ( a, b) ϕ ( q) + S 0 c ( q, b − a) + B q ( b − a) − 1 2 ϕ ( q) − 1 ϕ ( q) ∑ v ( mod q) ( v + a, q) = 1 S 0 c ( q, v) − 1 ϕ ( q) ∑ v ( mod q) ( v − b, q) = 1 S 0 c ( q, v) + 1 ϕ ( q) 2 ∑ v 1, v 2 ( mod q) ( v 1, q) = 1 ( v 2, q) = 1 S 0 c ( q, v 2 − v 1). | [2.21] |

With C q, χ = L ( 0, χ) L ( 1, χ) A q, χ (which is zero unless *χ*is an odd character), we may also derive the following alternative expression:

c 2 ( q; a) q = log ⁡ 2 ⁡ π 2 q + S 0 c ( q, b − a) + B q ( b − a) − 1 ϕ ( q) ∑ d | q d > 1 1 ϕ ( d) ∑ χ ( mod d) χ ( − 1) = − 1 C q, χ ( ∑ u ( mod d) ( u q / d + a, q) = 1 + ∑ u ( mod d) ( u q / d − b, q) = 1) χ ¯ ( u). | [2.22] |

If *χ*is induced by the primitive character χ ∗, then, writing χ = χ 0, m χ *for some *m*coprime to the conductor of χ ∗, we have

C q, χ = C q, χ ∗ ∏ p | m ( 1 − χ ∗ ( p)). |

Further, it is helpful to write q = q 0 2 r with q 0 odd. If now *χ*is a character to an odd modulus and *q*is even, then

C q, χ = χ ¯ ( 2) 2 C q 0, χ. |

Using these facts, it is possible to simplify the formula in **[2.22]**further, and obtain

c 2 ( q; ( a, b)) = log ⁡ 2 ⁡ π 2 + q S 0 c ( q, b − a) + q B q ( b − a) − q 0 ϕ ( q 0) ∑ d | q 0 μ ( d) ϕ ( d) ∑ χ ( mod d) C q 0, χ ( χ ¯ ( b) − χ ¯ ( a)). | [2.23] |

For example, if *q*is prime and a ≠ b, then

c 2 ( q; ( a, b)) = 1 2 log 2 π q + q ϕ ( q) ∑ χ ≠ χ 0 C q, χ ( χ ¯ ( b − a) + 1 ϕ ( q) ( χ ¯ ( b) − χ ¯ ( a))). |

This completes our discussion of the Main Conjecture in the case r = 2, and the other conjectures follow as simple consequences.

## 3. Proof of the Proposition

The proof follows along standard lines, and the closely related case of evaluating asymptotically ∑ h ≤ H S 0 ( { 0, h }) ( H − h) is mentioned in ref. 15 and treated in detail in ref. 16. We will therefore be brief. Let *χ*be a Dirichlet character modulo m | q; possibly, *χ*could be imprimitive, or the principal character. Define, for Re ( s) > 1,

F q, χ ( s) ≔ ∑ h ≥ 1 χ ( h) h s S q ( { 0, h }) = ∏ p | q ( 1 − χ ( p) p s) − 1 ∏ p ∤ q ( 1 − 1 ( p − 1) 2 + χ ( p) p s ( 1 − 1 p) − 1 ( 1 − χ ( p) p s) − 1), |

so that

∑ h ≥ 1 χ ( h) S q ( { 0, h }) e − h / H = 1 2 π i ∫ ( 2) F q, χ ( s) H s Γ ( s) d s. | [3.1] |

We now note that

F q, χ ( s) = L ( s, χ) ∏ p ∤ q ( 1 − 1 ( p − 1) 2 + χ ( p) p s − 1 ( p − 1) 2) = L ( s, χ) L ( s + 1, χ) ∏ p | q ( 1 − χ ( p) p s + 1) ∏ p ∤ q ( 1 − ( 1 − χ ( p) / p s) 2 ( p − 1) 2), |

which furnishes a meromorphic continuation of F q, χ ( s) to Re ( s) > − 1 / 2 with possible poles at s = 0 or s = 1 in case *χ*is principal. We may also express the above as

F q, χ ( s) = L ( s, χ) L ( s + 1, χ) L ( 2 s + 2, χ 2) ∏ p | q ( 1 + χ ( p) p s + 1) − 1 ∏ p ∤ q ( 1 − 1 ( p − 1) 2 + 2 p χ ( p) ( p − 1) 2 ( p s + 1 + χ ( p))), |

and now the final product above is analytic in Re ( s) > − 1, but for which the line Re ( s) = − 1 forms a natural boundary.

If *χ*is nonprincipal, then, by shifting the line of integration to Re ( s) = − 1 / 2 + ϵ, we find that the quantity in **[3.1]**is L ( 0, χ) L ( 1, χ) A q, χ + O ( H − 1 2 + ϵ), with the main term coming from the pole of Γ ( s) at s = 0. Moreover, we may even shift the line of integration to Re ( s) = − 1 + ε at the cost of picking up residues from the zeros of L ( 2 s + 2, χ 2). The contribution from these zeros is

Z q, χ ( H) ≔ ∑ ρ, Re ( ρ) > 0 L ( ρ, χ 2) = 0 Res s = ρ / 2 − 1 ( F q, χ ( s) H s Γ ( s)). |

If we suppose that GRH holds for L ( s, χ 2), that its zeros are simple, and that | L ′ ( ρ, χ 2) | is not too small so that [in view of the exponential decay of Γ ( s)] the sum over residues is absolutely convergent, then we would expect that Z q, χ ( H) is an oscillating term of size H − 3 / 4.

If *χ*is principal, but m > 1, then F q, χ ( s) has a pole at s = 1 with residue ϕ ( m) / m, but there is no pole of F q, χ at s = 0 because L ( s, χ 0) = s Λ ( m) + O ( s 2) for *s*near 0. Therefore, in this situation, we find

∑ h ≥ 1 χ 0 ( h) e − h / H S q ( { 0, h }) = ϕ ( m) m H − ϕ ( q) 2 q Λ ( m) + Z q, χ 0 ( H) + O ( H − 1 + ϵ). |

Finally, if m = 1 (and *χ*is naturally principal), the corresponding F q, χ ( s) has a simple pole at s = 0 in addition to the pole at s = 1. Thus, there is a double pole of the integrand in **[3.1]**, and, computing residues, we obtain that

∑ h ≥ 1 e − h / H S q ( { 0, h }) = H − ϕ ( q) 2 q [log 2 π H + ∑ p | q log p p − 1] + Z q, ζ ( H) + O ( H − 1 + ϵ). |

Because

∑ h ≡ v ( mod q) e − h / H S q ( { 0, h }) = S 0 ( q, v; H) + H q + B q ( v) + O ( 1 H), |

our proposition follows, with

Z q, v ( H) = 1 ϕ ( q / d) ∑ χ ( mod q / d) χ ¯ ( v / d) Z q, χ ( H / d). | [3.2] |

## 4. Modifications to the Heuristic When r ≥ 3

The ideas leading to the general case of the Main Conjecture are similar to those for r = 2, and so we just give a brief sketch. For r ≥ 3 and a = ( a 1, …, a r), we start by writing π ( x; q, a) as

∑ n ≤ x n ≡ a 1 ( mod q) ∑ h 1, …, h r − 1 > 0 h i ≡ a i + 1 − a i ( mod q) 1 P ( n) ∏ i = 1 r − 1 [1 P ( n + h 1 + … + h i) × ∏ 0 < t < h i ( t + a i, q) = 1 ( 1 − 1 P ( n + h 1 + … + h i − 1 + t))]. |

As before, we expand this out, invoke the Hardy−Littlewood conjectures, and then discard all singular series terms except for the empty set and sets with two elements. This leads to

π ( x; q, a) = ∫ 2 x q r − 1 ϕ ( q) r ( 1 − q ϕ ( q) log y) ε q ( a) ( D 0 + D 1 + D 2) ( a; y) d y ( log y) r + O ( x ( log log x) 2 ( log x) 3), |

where ε q ( a) = ε q ( a 1, a 2) + … + ε q ( a r − 1, a r) and D 0, D 1, and D 2 are certain smooth sums of singular series. For D 0, we have [with H = H ( y) as before]

D 0 = ∑ h 1, …, h r − 1 > 0 h i ≡ a i + 1 − a i ( mod q) e − ( h 1 + … + h r − 1) / H ( 1 + ∑ 0 ≤ i < j ≤ r − 1 S q, 0 ( { 0, h i + 1 + … + h j })). |

Notice that, if j = i + 1 in the inner summation, the resulting expression is ( H / q) r − 2 times the analogous D 0 term in our calculation for π ( x; q, ( a j, a j + 1)). If j − i > 1, we will need to consider sums of the form

S 0 k ( q, v; H) ≔ ∑ h ≡ v ( mod q) h k e − h / H S q, 0 ( { 0, h }), |

where k = j − i − 1. This can be understood via contour integration as in Proposition 2.1; a key difference is that, for k ≥ 1, we have S 0 k ( q, v; H) = O ( H k − 1 / 2) unless v = 0, in which case S 0 k ( q, 0; H) = − [ϕ ( q) / 2 q] Γ ( k) H k + O ( H k − 1 / 2). Using this to evaluate D 0, we find that it is [up to O ( H r − 3)]

H r − 1 q r − 1 + H r − 2 q r − 2 ∑ i = 1 r − 1 [S 0 ( q, a i + 1 − a i; H) + B q ( a i + 1 − a i) + ∑ k = 1 r − i − 1 S 0 k ( q, a i + k + 1 − a i; H) k! H k] ∼ H r − 1 q r − 1 + H r − 2 q r − 2 ∑ i = 1 r − 1 [S 0 ( q, a i + 1 − a i; H) + B q ( a i + 1 − a i) − ϕ ( q) 2 q ∑ k = 1 r − i − 1 δ ( a i = a i + k + 1) k], |

and it is this last term that creates the additional bias [in c 2 ( q; a)] against patterns with a nonimmediate repetition.

For D 1, up to O ( H r − 2), we obtain a contribution of ( H / q) r − 1 ( 1 − [φ ( q) / q] log y) − 1 times

∑ j = 1 r − 1 [( ∑ ( v + a j, q) = 1 + ∑ ( v − a j + 1, q) = 1) S 0 ( q, v; H) + ∑ k = 1 j − 1 ∑ ( v, q) = 1 S 0 k ( q, v − a j − k; H) k! H k + ∑ k = 1 r − 1 − j ∑ ( v, q) = 1 S 0 k ( q, v + a j + 1 + k; H) k! H k] ∼ ∑ j = 1 r − 1 ( ∑ ( v + a j, q) = 1 + ∑ ( v − a j + 1, q) = 1) S 0 ( q, v; H) − ϕ ( q) q ∑ k = 1 r − 2 r − 1 − k k. |

Finally, from D 2, we obtain ( H / q) r ( 1 − [ϕ ( q) / q] log y) − 2 times

∑ j = 1 r − 1 ( ∑ ( v 1, q) = 1 ( v 2, q) = 1 S 0 ( q, v 2 − v 1; H) + ∑ k = 1 r − 1 − j ∑ ( v 1, q) = 1 ( v 2, q) = 1 S 0 k ( q, v 1 + v 2; H) k! H k) ∼ ( r − 1) ∑ ( v 1, q) = 1 ( v 2, q) = 1 S 0 ( q, v 2 − v 1; H) − ϕ ( q) 2 2 q ∑ k = 1 r − 2 r − 1 − k k. |

Assembling these contributions yields the Main Conjecture.

## 5. Comparison of the Conjecture with Numerical Data

We begin by comparing the Main Conjecture with the data for r = 2 and q = 3 or 4. In each of these cases, our conjecture is that

π ( x; q, a) = li ( x) 4 ( 1 ± 1 2 ⁡ log x log ( 2 π ⁡ log x q)) + O ( x ( log x) 11 / 4), | [5.1] |

with the sign being negative if a 1 ≡ a 2 ( mod q) and positive if not. However, to obtain **[5.1]**in such a clean form, a number of asymptotic approximations were used throughout *Section 2*, *The Heuristic for r*= 2, and it is reasonable to expect that the unsimplified integral expression **[2.16]**for π ( x; q, a) would provide a better fit to the data. Indeed, we find the following.

[image: graphic file with name pnas.1605366113t02.jpg] |

[Open in a new tab][13]

Going forward, we will present only the comparison of π ( x; q, a) against **[2.16]**, so we explain briefly how we compute this approximation. In **[2.18]**, **[2.19]**, and **[2.20]**, we determined D 0, D 1, and D 2 in terms of S 0 ( q, v; H) and, in the process, replaced geometric progressions in *h*with suitable approximations. Of course, the geometric progressions could just be computed exactly. We keep the exact but messy expressions so obtained and, for S 0 ( q, v; H), use the main terms described in Proposition 2.1. This yields an expression for π ( x; q, a) as an explicit integral, which we computed numerically in Sage. The actual values of π ( x; q, a) were computed in C++ using the primesieve library. Code for both computations can be found on the first author’s website.

Next we consider q = 8. Here too the constants simplify, with c 2 ( 8; ( a, b)) depending only on the difference b − a ( mod 8) (a fact reflected in the data, as predicted by Conjecture 1.6). Explicitly, we have c 2 ( 8; ( a, a)) = ( 5 ⁡ log ⁡ 2 − 3 ⁡ log ⁡ π) / 2, c 2 ( 8; ( a, a + 2)) = c 2 ( 8; ( a, a + 6)) = ( log ⁡ π − log ⁡ 2) / 2, and c 2 ( 8; ( a, a + 4)) = ( log ⁡ π − 3 ⁡ log ⁡ 2) / 2. Thus, we should expect that, among the nondiagonal patterns, those with b − a = 4 should be the least frequent, and those with b − a = 2 and 6 should be rather close. Indeed, we find the following.

[image: graphic file with name pnas.1605366113t03.jpg] |

[Open in a new tab][14]

We now turn to the patterns ( mod 12). Here, the quadratic character χ ( mod 3) plays a role for those patterns ( a, b) with a ≠ b ( mod 3). In particular, it does not play a role in the diagonal patterns, for which c 2 ( 12; a) is given by **[1.1]**. For nondiagonal patterns, we have the following.

[image: graphic file with name pnas.1605366113t04.jpg] |

[Open in a new tab][15]

[The other values of c 2 ( 12; a) are determined by c 2 ( 12; a opp).]

Here, A 12, χ ≈ 1.036, so that c 2 ( 12; ( 5,7)) and c 2 ( 12; ( 11,1)) are the largest of these. Moreover, as in the ( mod 8) case, there are symmetries between patterns with the same difference b − a. We find the following.

[image: graphic file with name pnas.1605366113t05.jpg] |

[Open in a new tab][16]

We close by considering q = 5 (which amounts to considering the last decimal digit of primes). Essentially, no simplifications can be made for the constants c 2 ( q; a). For any nondiagonal pattern ( a, b), we find

c 2 ( 5; ( a, b)) = log ( 2 π / 5) 2 + 5 2 Re ( L ( 0, χ) L ( 1, χ) A 5, χ [χ ¯ ( b − a) + χ ¯ ( b) − χ ¯ ( a) 4]), |

where *χ*is either of the complex characters ( mod 5). Apart from the understood symmetry c 2 ( 5; ( a, b)) = c 2 ( 5; ( − b, − a)), the value of c 2 determines the pattern. Thus, we might expect significant variation between the various patterns and, in particular, no additional symmetries like we saw ( mod 8) and ( mod 12). We find the following, presenting only the first of ( a, b) and ( − b, − a),

[image: graphic file with name pnas.1605366113t06.jpg] |

[Open in a new tab][17]

An interesting feature to be observed here is that, initially, π ( x; 5, ( 1,2)) is larger than π ( x; 5, ( 1,3)), despite our conjecture predicting the opposite ordering. In fact, this is true for all *x*between 41,231 and 5.076 ⋅ 10 11. However, at about 5.082 ⋅ 10 11, π ( x; 5, ( 1,3)) becomes consistently larger, seemingly forever, exactly as our conjecture would predict. We take this as reasonable evidence for our speculation that there are even more lower-order terms [e.g., on the order of x ( log log x) 2 / ( log x) 3], which, in this case, apparently conspire to point in the opposite direction than the bias in the Main Conjecture.

## Acknowledgments

We thank Tadashi Tokieda, whose lecture on “Rock, paper, scissors in probability” inspired the present work; James Maynard for drawing our attention to ref. 3; Paul Abbott for pointing us to ref. 7; and Alexandra Florea, Andrew Granville, and Peter Sarnak for helpful comments. The first author is partially supported by National Science Foundation (NSF) postdoctoral fellowship Division of Mathematical Sciences 1303913. The second author is partially supported by the NSF, and by a Simons Investigator Award from the Simons Foundation.

## Footnotes

The authors declare no conflict of interest.

This article is a PNAS Direct Submission.

## References

- 1. Rubinstein M, Sarnak P. Chebyshev’s bias. Exp Math. 1994;3(3):173–197. [[Google Scholar][18]]
- 2. Granville A, Martin G. Prime number races. Am Math Mon. 2006;113(1):1–33. [[Google Scholar][19]]
- 3. Knapowski S, Turán P. Number Theory and Algebra. Academic; New York: 1977. On prime numbers ≡ 1 resp. 3mod 4; pp. 157–165. [[Google Scholar][20]]
- 4. Shiu DKL. Strings of congruent primes. J Lond Math Soc. 2000;61(2):359–373. [[Google Scholar][21]]
- 5. Banks WD, Freiberg T, Turnage-Butterbaugh CL. Consecutive primes in tuples. Acta Arith. 2015;167(3):261–266. [[Google Scholar][22]]
- 6. Maynard J. 2014. Dense clusters of primes in subsets. arXiv:14052953.
- 7. Ko C-M. Distribution of the units digit of primes. Chaos Solitons Fractals. 2002;13(6):1295–1302. [[Google Scholar][23]]
- 8. Ash A, Beltis L, Gross R, Sinnott W. Frequencies of successive pairs of prime residues. Exp Math. 2011;20(4):400–411. [[Google Scholar][24]]
- 9. Dummit D, Granville A, Kisilevsky H. Big biases amongst products of two primes. Mathematika. 2016;62(2):502–507. [[Google Scholar][25]]
- 10. Gallagher PX. On the distribution of primes in short intervals. Mathematika. 1976;23(1):4–9. [[Google Scholar][26]]
- 11. Goldston DA, Ledoan AH. The jumping champion conjecture. Mathematika. 2015;61(3):719–740. [[Google Scholar][27]]
- 12. Granville A, van de Lune J, te Riele HJJ. Checking the Goldbach conjecture on a vector computer. In: Mollin RA, editor. Number Theory and Applications. Kluwer; Dordrecht, The Netherlands: 1989. pp. 423–433. [[Google Scholar][28]]
- 13. Montgomery HL, Soundararajan K. Primes in short intervals. Commun Math Phys. 2004;252(1-3):589–617. [[Google Scholar][29]]
- 14. Odlyzko A, Rubinstein M, Wolf M. Jumping champions. Exp Math. 1999;8(2):107–118. [[Google Scholar][30]]
- 15. Goldston DA. Linnik’s theorem on Goldbach numbers in short intervals. Glasg Math J. 1990;32(3):285–297. [[Google Scholar][31]]
- 16. Montgomery HL, Soundararajan K. 2002. Beyond pair correlation. Paul Erdős and His Mathematics, I (Budapest, 1999), Bolyai Society Mathematical Studies (János Bolyai Math Soc, Budapest), Vol 11, pp 507–514.

[image: Close]

## ACTIONS

- [image: View on publisher site icon] [View on publisher site][4]
- [image: Download PDF icon] [PDF (941.7 KB)][5]
- [image: Cite icon] Cite
- [image: Collections icon][image: Collections icon] Collections
- [image: Permalink icon] Permalink

## PERMALINK

[image: Copy icon] Copy

## RESOURCES

### Similar articles

### Cited by other articles

### Links to NCBI Databases

## Cite

[image: Close icon]

- [image: Copy icon] Copy
- [image: Download icon] Download .nbib.nbib
-

Format: AMA APA MLA NLM

## Add to Collections

Back to Top[image: back to top icon]


## Links

[1]: /
[2]: /journals/
[3]: /about/userguide/
[4]: https://doi.org/10.1073/pnas.1605366113
[5]: pdf/pnas.201605366.pdf
[6]: /about/disclaimer/
[7]: /about/copyright/
[8]: https://pubmed.ncbi.nlm.nih.gov/?term="Lemke%20Oliver%20RJ"[Author]
[9]: https://pubmed.ncbi.nlm.nih.gov/?term="Soundararajan%20K"[Author]
[10]: https://pubmed.ncbi.nlm.nih.gov/27418603/
[11]: /articles/PMC4978266/
[12]: table/unt01/
[13]: table/unt02/
[14]: table/unt03/
[15]: table/unt04/
[16]: table/unt05/
[17]: table/unt06/
[18]: https://scholar.google.com/scholar_lookup?journal=Exp%20Math&amp;title=Chebyshev%E2%80%99s%20bias&amp;author=M%20Rubinstein&amp;author=P%20Sarnak&amp;volume=3&amp;issue=3&amp;publication_year=1994&amp;pages=173-197&amp;
[19]: https://scholar.google.com/scholar_lookup?journal=Am%20Math%20Mon&amp;title=Prime%20number%20races&amp;author=A%20Granville&amp;author=G%20Martin&amp;volume=113&amp;issue=1&amp;publication_year=2006&amp;pages=1-33&amp;
[20]: https://scholar.google.com/scholar_lookup?title=Number%20Theory%20and%20Algebra&amp;author=S%20Knapowski&amp;author=P%20Tur%C3%A1n&amp;publication_year=1977&amp;
[21]: https://scholar.google.com/scholar_lookup?journal=J%20Lond%20Math%20Soc&amp;title=Strings%20of%20congruent%20primes&amp;author=DKL%20Shiu&amp;volume=61&amp;issue=2&amp;publication_year=2000&amp;pages=359-373&amp;
[22]: https://scholar.google.com/scholar_lookup?journal=Acta%20Arith&amp;title=Consecutive%20primes%20in%20tuples&amp;author=WD%20Banks&amp;author=T%20Freiberg&amp;author=CL%20Turnage-Butterbaugh&amp;volume=167&amp;issue=3&amp;publication_year=2015&amp;pages=261-266&amp;
[23]: https://scholar.google.com/scholar_lookup?journal=Chaos%20Solitons%20Fractals&amp;title=Distribution%20of%20the%20units%20digit%20of%20primes&amp;author=C-M%20Ko&amp;volume=13&amp;issue=6&amp;publication_year=2002&amp;pages=1295-1302&amp;
[24]: https://scholar.google.com/scholar_lookup?journal=Exp%20Math&amp;title=Frequencies%20of%20successive%20pairs%20of%20prime%20residues&amp;author=A%20Ash&amp;author=L%20Beltis&amp;author=R%20Gross&amp;author=W%20Sinnott&amp;volume=20&amp;issue=4&amp;publication_year=2011&amp;pages=400-411&amp;
[25]: https://scholar.google.com/scholar_lookup?journal=Mathematika&amp;title=Big%20biases%20amongst%20products%20of%20two%20primes&amp;author=D%20Dummit&amp;author=A%20Granville&amp;author=H%20Kisilevsky&amp;volume=62&amp;issue=2&amp;publication_year=2016&amp;pages=502-507&amp;
[26]: https://scholar.google.com/scholar_lookup?journal=Mathematika&amp;title=On%20the%20distribution%20of%20primes%20in%20short%20intervals&amp;author=PX%20Gallagher&amp;volume=23&amp;issue=1&amp;publication_year=1976&amp;pages=4-9&amp;
[27]: https://scholar.google.com/scholar_lookup?journal=Mathematika&amp;title=The%20jumping%20champion%20conjecture&amp;author=DA%20Goldston&amp;author=AH%20Ledoan&amp;volume=61&amp;issue=3&amp;publication_year=2015&amp;pages=719-740&amp;
[28]: https://scholar.google.com/scholar_lookup?title=Number%20Theory%20and%20Applications&amp;author=A%20Granville&amp;author=J%20van%20de%20Lune&amp;author=HJJ%20te%20Riele&amp;publication_year=1989&amp;
[29]: https://scholar.google.com/scholar_lookup?journal=Commun%20Math%20Phys&amp;title=Primes%20in%20short%20intervals&amp;author=HL%20Montgomery&amp;author=K%20Soundararajan&amp;volume=252&amp;issue=1-3&amp;publication_year=2004&amp;pages=589-617&amp;
[30]: https://scholar.google.com/scholar_lookup?journal=Exp%20Math&amp;title=Jumping%20champions&amp;author=A%20Odlyzko&amp;author=M%20Rubinstein&amp;author=M%20Wolf&amp;volume=8&amp;issue=2&amp;publication_year=1999&amp;pages=107-118&amp;
[31]: https://scholar.google.com/scholar_lookup?journal=Glasg%20Math%20J&amp;title=Linnik%E2%80%99s%20theorem%20on%20Goldbach%20numbers%20in%20short%20intervals&amp;author=DA%20Goldston&amp;volume=32&amp;issue=3&amp;publication_year=1990&amp;pages=285-297&amp;
