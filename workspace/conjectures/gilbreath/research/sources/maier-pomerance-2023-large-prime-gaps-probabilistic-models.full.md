<!-- source: https://link.springer.com/article/10.1007/s00222-023-01199-0 | converted from HTML -->
<!-- CORRECT AUTHORSHIP: William Banks, Kevin Ford, Terence Tao, "Large prime gaps and probabilistic models", Invent. math. 233 (2023) 1471-1518. The filename says "maier-pomerance" — that is WRONG; the authors are Banks-Ford-Tao. -->

Large prime gaps and probabilistic models | Inventiones mathematicae | Springer Nature Link

Skip to main content

# Large prime gaps and probabilistic models

- [Open access][1]
- Published: 14 June 2023

- Volume 233, pages 1471–1518 ( 2023)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Inventiones mathematicae][5] [Aims and scope][6]

Large prime gaps and probabilistic models

[Download PDF][2]

## Abstract

We introduce a new probabilistic model of the primes consisting of integers that survive the sieving process when a random residue class is selected for every prime modulus below a specific bound. From a rigorous analysis of this model, we obtain heuristic upper and lower bounds for the size of the largest prime gap in the interval \([1,x]\). Our results are stated in terms of the extremal bounds in the interval sieve problem. The same methods also allow us to rigorously relate the validity of the Hardy-Littlewood conjectures for an arbitrary set (such as the actual primes) to lower bounds for the largest gaps within that set.

### Similar content being viewed by others

### [Bounded gaps between primes in short intervals][7]

Article 19 March 2018

### [Primes with restricted digits][8]

Article Open access 04 March 2019

### [Large sieve estimate for multivariate polynomial moduli and applications][9]

Article 08 November 2021

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Combinatorics][10]
- [Computational Number Theory][11]
- [Discrete Mathematics in Computer Science][12]
- [Discrete Mathematics][13]
- [Number Theory][14]
- [Probability Theory][15]
- [Dynamical Systems and Ergodic Theory in Number Theory][16]

## 1 Introduction

In this paper, we introduce a new probabilistic model for the primes which can be analyzed rigorously to make a variety of heuristic predictions. In contrast to the well known prime model of Cramér [[6][17]] and the subsequent refinement of Granville [[16][18]], in which random sets are formed by including positive integers with specific probabilities, the model proposed here is comprised of integers that survive the sieve when a random residue class is selected for every prime modulus below a specific bound. We determine the asymptotic behavior of the largest gap function, , for the set , where for any subset we denote

We conjecture that the primes have similar behavior. Our bounds, given in Theorem [1.1][19] below, are stated in terms of the extremal bounds in the interval sieve problem.

At present, the strongest unconditional lower bound on is due to Ford, Green, Konyagin, Maynard, and Tao [[11][20]], who have shown that Footnote 1

for sufficiently large \(x\), with \(\log _{k} x\) the \(k\) -fold iterated natural logarithm of \(x\), whereas the strongest unconditional upper bound is

a result due to Baker, Harman, and Pintz [[2][21]]. Assuming the Riemann Hypothesis, Cramér [[5][22]] showed that

### 1.1 Cramér’s random model

In 1936, Cramér [[6][17]] introduced a probabilistic model of primes, where each natural number \(n\geqslant 3\) is selected for inclusion in with probability \(1/\log n\), the events being jointly independent in \(n\). By Hoeffding’s inequality (or Lemma [3.3][23] below), for any fixed \(\varepsilon >0\) one has

(1.1)

with probability one. Footnote 2 The analogous statement for primes is equivalent to the Riemann Hypothesis. In 1936, Cramér [[6][17]] proved that almost surely, and remarked: “Obviously we may take this as a suggestion that, for the particular sequence of ordinary prime numbers \(p_{n}\), some similar relation may hold.” Later, Shanks [[40][24]] conjectured the stronger bound , also based on the analysis of a random model very similar to Cramér’s model. This is a natural conjecture in light of the fact that

(1.2)

holds with probability one (although ( [1.2][25]) doesn’t appear to have been observed before). In the literature, the statements and are sometimes referred to as “Cramér’s conjecture.” Several people have made refined conjectures, e.g., Cadwell [[4][26]] has suggested that is well-approximated by \((\log x)(\log x-\log _{2} x)\), a conjecture which is strongly supported by numerical calculations of gaps. We refer the reader to Granville [[16][18]] or Soundararajan [[41][27]] for additional information about the Cramer model and subsequent developments.

Tables of prime gaps have been computed up to \(10^{18}\) and beyond (see [[35][28]]), thus

a consequence of the gap of size 1132 following the prime 1693182318746371. See also Fig. [1][29] for a plot of \(G(x)\) versus various approximations.

**Fig. 1**

[image: Fig. 1]

[Full size image][30]

vs. various approximations

Despite its utility, the Cramér model has several well-documented weaknesses, the most dramatic one being that the model does not predict the expected asymptotics for prime \(k\) -tuples. Indeed, for *any*finite set \(\mathcal{H}\subset \mathbb{Z} \), Cramér’s model gives

with probability one, whereas the analogous assertion for prime numbers is false in general (for example, there is no integer \(n\) such that \(n+h\) is prime for all \(h\in \{0,1,2\}\)). The reason for the disparity is simple: for any prime \(p\), every prime other than \(p\) must lie in one of the residue classes \(\{1,\ldots ,p-1\}\) modulo \(p\) (we refer to this as the *bias*of the primes modulo \(p\)), whereas is equidistributed over *all*residue classes modulo \(p\).

See Pintz [[36][31]] and Sect. [2.5][32] below, for further discussion of flaws in the Cramér model.

### 1.2 Granville’s random model

To correct this flaw in the Cramér model , Granville [[16][18]] altered the model, constructing a random set as follows. For each interval \((x,2x]\) (with \(x\) being a power of two, say), let \(A\) be a parameter such that \(A=\log ^{1-o(1)}x\) as \(x\to \infty \), and put \(Q:=\prod _{p\leqslant A} p\). Discard those \(n\) for which \((n,Q)>1\), and select for inclusion in each of the remaining integers \(n\in (x,2x]\) with probability \(\frac{Q/\phi (Q)}{\log n}\), where \(\phi \) is the Euler totient function, the events being jointly independent in \(n\). Since \(\phi (Q)/Q\) is the density in ℤ of the set of integers coprime to \(Q\), this model captures the correct global distribution of primes; that is, an analog of ( [1.1][33]) holds with replaced by . Unlike Cramér’s model, however, Granville’s model also captures the bias of primes in residue classes modulo the primes \(p\leqslant A\). In particular, for any finite set ℋ of integers, Granville’s set satisfies the appropriate analog of the Hardy-Littlewood conjectures for counts of prime \(k\) -tuples (see ( [1.4][34]) below).

In contrast with the Cramér model, Granville’s random set satisfies

(1.3)

with probability one. Granville establishes ( [1.3][35]) by choosing starting points \(a\) with \(Q\mid a\). If \(y\asymp \log ^{2} x\), then there are about \(y/\log y\) numbers \(n\in [a,a+y]\) that are coprime to every \(p\leqslant A\); this is a factor \(\xi \) smaller than the corresponding quantity for a random starting point \(a\), and it accounts for the difference between ( [1.2][25]) and ( [1.3][35]). We elaborate on this idea in our analysis of .

### 1.3 A new probabilistic model for primes

Hardy and Littlewood [[19][36]] conjectured that the asymptotic relation

(1.4)

holds for any finite set \(\mathcal{H}\subset \mathbb{Z} \), where \(\mathfrak{S} (\mathcal{H})\) is the singular series given by

$$ \mathfrak{S} (\mathcal{H}):=\prod _{p} \bigg(1-\frac{|\mathcal{H}\bmod p|}{p}\bigg) \bigg(1-\frac{1}{p}\bigg)^{-| \mathcal{H}|}. $$

(1.5)

Note that the left side of ( [1.4][34]) is bounded if \(|\mathcal{H}\bmod p|=p\) for some prime \(p\), since then for every integer \(n\), one has \(p\,\mid \,n+h\) for some \(h\in \mathcal{H}\). In this case, \(\mathfrak{S} (\mathcal{H})=0\). We say that ℋ is *admissible*if \(|\mathcal{H}\bmod p|< p\) for every prime \(p\).

To motivate our model set , we first reinterpret ( [1.4][34]) probabilistically. The rapid convergence of the product ( [1.5][37]) implies that \(\mathfrak{S} (\mathcal{H})\) is well approximated by the truncation

$$ \mathfrak{S} _{z}(\mathcal{H}):=\prod _{p \leqslant z}\bigg(1-\frac{|\mathcal{H}\bmod p|}{p}\bigg) \bigg(1-\frac{1}{p}\bigg)^{-|\mathcal{H}|}=V_{\mathcal{H}}(z) \Theta _{z}^{-|\mathcal{H}|}, $$

where

$$ V_{\mathcal{H}}(z):=\prod _{p\leqslant z}\bigg(1- \frac{|\mathcal{H}\bmod p|}{p}\bigg)\qquad \text{and}\qquad \Theta _{z} :=\prod _{p\leqslant z}\bigg(1- \frac{1}{p}\bigg). $$

(1.6)

We interpret \(V_{\mathcal{H}}(z)\) as a product of local densities, and \(\Theta _{z}\) as a kind of global density. In order to match the global density of primes as closely as possible, we take \(z=z(t)\) be the largest prime number for which \(1/\Theta _{z(t)} \leqslant \log t\); this is well-defined for \(t \geqslant e^{2}\), and by the prime number theorem we have

$$ z(t)\sim t^{1/e^{\gamma}}\qquad \text{and}\qquad \Theta _{z(t)}^{-1}= \log t+O(t^{-1/e^{\gamma}}). $$

(1.7)

It follows that the right side of ( [1.4][34]) is

$$ \sim \intop \nolimits _{e^{2}}^{x}V_{\mathcal{H}}(z(t))\, dt. $$

On the other hand, the quantity \(V_{\mathcal{H}}(z)\) can be written probabilistically as

$$ V_{\mathcal{H}}(z)=\mathbb{P}(\mathcal{H}\subset \mathcal{S} _{z}), $$

(1.8)

where ℙ denotes probability over a uniform choice of residue classes \(a_{p}\bmod p\), for every prime \(p\), with the random variables \(a_{p} \bmod p\) being jointly independent in \(p\), and \(\mathcal{S} _{z}\) is the random set

$$ \mathcal{S} _{z}:=\mathbb{Z} \setminus \bigcup _{p\leqslant z} (a_{p}\bmod p). $$

(1.9)

Thus, \(\mathcal{H}\subset \mathcal{S} _{z}\) is the event that ℋ survives sieving by random residue classes modulo primes \(p\leqslant z\). Consequently, for admissible ℋ, ( [1.4][34]) takes the form

Thus, ( [1.4][34]) asserts that the probability that a random shift of ℋ lies in is asymptotically the same as the probability that ℋ lies in a randomly sifted set.

Motivated by this probabilistic interpretation of ( [1.4][34]), we now define

(1.10)

as our random set of integers. Note that the number of primes being sieved out increases as \(n\) increases in order to mimic the slowly decreasing density of the primes. This can be compared with the description of using the sieve of Eratosthenes, in which \(z(n)\) is replaced by \(n^{1/2}\) and the \(a_{p}\) are replaced by 0.

We believe that the random set is a useful model for primes, especially for studying local statistics such as gaps. On the other hand, the analysis of presents more difficulties than the analysis of or , owing to the more complicated coupling between events such as and for \(n_{1} \neq n_{2}\).

### 1.4 Large gaps from the model

The behavior of is intimately tied to extremal properties of the *interval sieve*. To describe this connection, for any \(y \geqslant 2\) let \(W_{y}\) denote the (deterministic) quantity

$$ W_{y} :=\min \big|[0,y]\cap \mathcal{S} _{(y/ \log y)^{1/2}}\big|, $$

(1.11)

where \(\mathcal{S} _{z}\) is defined in ( [1.9][38]) and the minimum in ( [1.11][39]) is taken over all choices of the residue classes \(\{a_{p}\bmod p: p\leqslant (y/\log y)^{1/2}\}\). At present, the sharpest known bounds on \(W_{y}\) are

$$ {(4+o(1)) \frac{y\log _{2}y}{\log ^{2} y} \leqslant } W_{y} \leqslant \frac{y}{\log y}+O\left (\frac{y\log _{2}y}{\log ^{2} y}\right ), $$

(1.12)

the lower bound being a consequence of Iwaniec’s theory (see [[12][40], Theorem 12.14] or [[21][41]]) of the linear sieve, and the upper bound resulting from the particular choice \(a_{p}:=0\bmod p\) for all primes \(p\leqslant (y/\log y)^{1/2}\). There is a folklore conjecture that the upper bound in ( [1.12][42]) is closer to the truth. The problem of bounding \(W_{y}\) belongs to a circle of problems centered on the question about the maximum number of primes in some interval of length \(x\); see e.g., [[20][43]] and [[9][44]].

### Theorem 1.1

Asymptotic for largest gap in the random model

*Put*

$$ g(u) :=\max \{ y : W_{y} \log y \leqslant u \} $$

(1.13)

*and define*\(\xi :=2e^{-\gamma}=1.1229\ldots \). *For any*\(\varepsilon >0\), *with probability one*, *we have*

*for all large*\(x\).

The function \(g(u)\) is evidently increasing, and by ( [1.12][42]) we see that

$$ {(1+o(1)) u \leqslant g(u) \leqslant (1+o(1)) \frac{u\log u}{4\log _{2} u} \qquad (u \to \infty )} $$

(1.14)

and so Theorem [1.1][19] implies that for every \(\varepsilon >0\), almost surely we have

(1.15)

for all large \(x\).

It seems likely that \(g((\xi \pm \varepsilon (x))\log ^{2} x)\sim g(\xi \log ^{2} x)\) whenever \(\varepsilon (x)\) goes to zero as \(x \to \infty \), although we cannot prove this. Assuming this, Theorem [1.1][19] leads us to the following prediction for gaps between primes:

### Conjecture 1.2

Asymptotic for largest gap in the primes

*We have*

Assuming the previously mentioned folklore conjecture that the lower bound in ( [1.14][45]) is asymptotically tight in the sense that \(g(u)\sim u\) as \(u\to \infty \), we are then led to the prediction that

This matches the lower bound ( [1.3][35]) for the gap in the Granville model .

### 1.5 Hardy-Littlewood from the model

It has been conjectured that a much more precise version of ( [1.4][34]) holds (see, e.g., Montgomery and Soundararajan [[28][46]]), namely:

(1.16)

There is some computational evidence for this strong estimate for certain small sets ℋ; see Sect. [2.1][47]. Granville’s model set , by contrast, satisfies the analogous relation with an error term that cannot be made smaller than \(O(x/\log ^{|\mathcal{H}|+1} x)\). This occurs because is only capturing the bias of modulo primes \(p\leqslant A\); that is, the set satisfies the analog of ( [1.16][48]) with \(\mathfrak{S} (\mathcal{H})\) replaced by \(\mathfrak{S} _{A}(\mathcal{H})\).

The model set given by ( [1.10][49]) has been designed with the Hardy-Littlewood conjectures in mind. We establish a uniform analog of ( [1.16][48]) that holds in a wide range of ℋ.

### Theorem 1.3

Hardy-Littlewood conjecture for the random model

*Fix*\(c\in [1/2,1)\)*and*\(\varepsilon >0\). *Almost surely*, *we have*

*uniformly for all admissible tuples*ℋ *satisfying*\(|\mathcal{H}| \leqslant \log ^{c} x\)*and in the range*\(\mathcal{H}\subset [0,\exp ( \frac{\log ^{1-c} x}{\log _{2} x} )]\).

In particular, when \(c=\frac{1}{2}\) the error term is \(O(x^{1/2+o(1)})\), which matches ( [1.16][48]) provided that \(\mathcal{H}\subseteq [0,\exp \{\frac{\log ^{1/2} x}{\log _{2} x} \}]\) and \(|\mathcal{H}|\leqslant \log ^{1/2} x\). As we will invoke the Borel-Cantelli lemma in the proof, the constant implied by the \(O\) -symbol exists almost surely, but we cannot give any uniform bound on it. This remark applies to the next result as well.

For the special case \(\mathcal{H}=\{0\}\) we have the following more precise statement.

### Theorem 1.4

Riemann hypothesis for the random model

*Fix*\(c>3/2\). *Almost surely*, *we have*

Similar results can be obtained for any *fixed*tuple ℋ; we leave this to the interested reader.

### 1.6 Large gaps from Hardy-Littlewood

The results stated above have a partial deterministic converse. We show that *any*set of integers that satisfies a uniform analogue of the Hardy-Littlewood conjecture ( [1.16][48]) has large gaps. The maximal length of the gaps depends on the range of uniformity of ( [1.16][48]), and comes close to order \(\log ^{2} x\) with a strong uniformity assumption. Our result extends a theorem of Gallagher [[14][50]], who showed that if, for every fixed \(k\in \mathbb{N} \) and real \(c>1\), the primes obey the Hardy-Littlewood conjectures uniformly for every admissible \(k\) -tuple \(\mathcal{H}\subset [0,c\log x]\), then the gaps normalized by \(\frac{1}{\log x}\) enjoy an exponential distribution asymptotically. His approach applies to any set in place of the primes .

### Theorem 1.5

Hardy-Littlewood implies large gaps

*Assume*\(\frac{2\log _{2} x}{\log x} \leqslant \kappa \leqslant 1/2\)*and that**satisfies the Hardy*-*Littlewood type conjecture*

(1.17)

*uniformly over all tuples*\(\mathcal{H}\subset [0,\log ^{2} x]\)*with*\(|\mathcal{H}| \leqslant \frac{\kappa \log x}{2\log _{2} x}\). *Then*

*for all large*\(x\), *where the implied constant is absolute*.

We also have the following variant of Theorem [1.5][51], which has a stronger conclusion but requires a uniform Hardy-Littlewood conjecture for larger tuples (of cardinality as large as \(\log x \log _{2} x\)); on the other hand, this conjecture is only needed in a certain averaged sense.

### Theorem 1.6

Averaged Hardy-Littlewood implies large gaps

*Fix*\(0< c<1\). *Suppose that**satisfies the averaged Hardy*-*Littlewood type conjecture*

(1.18)

*uniformly for*\(k \leqslant \frac{Cy}{\log x}\)*and*\(\log x \leqslant y \leqslant (\log ^{2} x) \log _{2} x\), *where*\(C\)*is a sufficiently large absolute constant*. *Then*

*where*\(g\)*is defined in*( [1.13][52]).

One could combine Theorem [1.3][53] with Theorem [1.5][51] (taking \(\kappa :=(\log x)^{c-1+\varepsilon }\) with fixed \(c<1\), say) to obtain results similar to Theorem [1.1][19]. However, the conclusion is considerably weaker than that of Theorem [1.1][19], and it does not appear that this approach is going to come close to recovering the bounds we obtain using a direct argument.

Below we summarize, in rough form, the various results and conjectures for the primes , the various random models for the primes, and for arbitrary sets obeying a Hardy-Littlewood type conjecture:

Set

 |

Hardy-Littlewood conjecture?

 |

Asymptotic largest gap up to *x*

 |

 |

No (singular series is missing)

 |

∼log 2*x*

 |

 |

Yes (with weak error term)

 |

*g*((*ξ*± *o*(1))log 2*x*)

 |

 |

Yes (with error \(O(x^{1-c})\))

 |

*g*((*ξ*± *o*(1))log 2*x*)

 |

 |

Yes (conjecturally)

 |

∼*ξ*log 2*x*(conjecturally)

 |

 |

Assumed (error \(O(x^{1-c})\))

 |

\(\gg c \frac{\log ^{2} x}{\log _{2} x}\)

 |

 |

Assumed on average (error \(O(x^{1-c})\)) for tuples of size up to (log*x*)log 2*x*

 |

≳*g*((*c**ξ*− *o*(1))log 2*x*)

 |

Of course, one can combine this table’s conclusions with the unconditional bounds in ( [1.14][45]), or the conjecture \(g(u) \sim u\), to obtain further rigorous or predicted upper and lower bounds for the largest gap.

### 1.7 Open problems

1. (1)

Improve upon the bounds ( [1.12][42]); alternatively, give some heuristic reason for why the upper bound in ( [1.12][42]) should be closer to the truth.

2. (2)

Show that \(g(a)\sim g(b)\) whenever \(a\sim b\). This will clean up the statement of Theorem [1.1][19].

3. (3)

Analyze the distribution of large gaps between special elements of . For example, what is the largest gap between elements of below \(x\)? This should be a good predictor for the maximal gap between pairs of twin primes and likely will involve a different extremal sieve problem.

### 1.8 Plan of the paper

Following further remarks and background inequalities in Sects. [2][54] and [3][55], we prove Theorems [1.3][53] and [1.4][56] in Sect. [4][57] using first and second moment bounds. Section [5][58] and [6][59] contain probability estimates on \(|[0,y] \cap \mathcal{S} _{w}|\) for various ranges of \(w\). These are then used to prove Theorem [1.1][19] in Sect. [7][60] and Theorems [1.5][51] and [1.6][61] in Sect. [8][62]. In Sect. [2.4][63], we connect the interval sieve problem to the problem of “exceptional zeros,” made explicit in Theorem [2.2][64]; this is proved in Sect. [9][65].

## 2 Background and further remarks

The discussion here is not needed for the proofs of the main theorems and may be omitted on the first reading.

### 2.1 Remarks on the Hardy-Littlewood conjectures

For any \(\mathcal{H}\subseteq [0,y]\), we have \(\mathfrak{S} (\mathcal{H}) \leqslant e^{O(|\mathcal{H}| \log _{2} y)}\) (see Lemma [3.4][66] below), and thus when \(y \leqslant (\log x)^{O(1)}\), the main terms in ( [1.16][48]) and ( [1.17][67]) are smaller than one for \(c_{1} \frac{\log x}{\log _{2} x} \leqslant |\mathcal{H}| \leqslant \exp \{ (\log x)^{c_{2}} \}\), where \(c_{1},c_{2}>0\) are appropriate constants. Therefore, we cannot have a genuine asymptotic when \(|\mathcal{H}| > c_{1} \frac{\log x}{\log _{2} x}\).

In the case of primes, it may be the case that ( [1.16][48]) fails when \(|\mathcal{H}|> \frac{\log x}{\log _{2} x}\) owing to potentially large fluctuations in both the size of \(\mathfrak{S} (\mathcal{H})\) and in the prime counts themselves. We note that Elsholtz [[8][68]] has shown that for any \(c>0\), the left side of ( [1.16][48]) is bounded by

$$ O\left (x \exp \left ( - (\tfrac{1}{4}+o(1)) \frac{\log x \log _{3} x}{\log _{2} x} \right )\right ) $$

when \(|\mathcal{H}|\geqslant c\log x\), where the implied function \(o(1)\) depends on \(c\). On the other hand, there are admissible tuples with \(|\mathcal{H}|\ll \log x\) for which the left side of ( [1.16][48]) is zero (see [[8][68]] for a construction of such ℋ).

Our assumption in Theorem [1.6][61] is more speculative, in light of the above remarks, since we need to deal with tuples ℋ satisfying \(k=|\mathcal{H}| > \log x\). Also, simply considering subsets ℋ of the primes in \((y/2,y]\) (which are automatically admissible), we see that there are at least \((\frac{y}{k\log y})^{k}>(\log x)^{k/2}\) tuples ℋ in the summation, and this means that when \(k>\log x\), ( [1.18][69]) implies a great deal of cancellation in the error terms of ( [1.17][67]) over tuples ℋ.

In a few special cases, e.g., \(\mathcal{H}=\{0,2\}\), \(\mathcal{H}=\{0,2,6\}\), and \(\mathcal{H}=\{0,4,6\}\), there is extensive numerical evidence (cf. [[19][36], pp. 43–44, 62–64], [[32][70]], [[24][71]], [[33][72]], [[34][73]]) in support of the conjecture ( [1.16][48]) with such a strong error term. Footnote 3 Note that the special case of ( [1.16][48]) with \(\mathcal{H}=\{0\}\) is equivalent to the Riemann Hypothesis. Theorem [1.3][53] makes plausible the notion that ( [1.16][48]) may hold uniformly for \(\mathcal{H}\subset [0,Y]\) with \(|\mathcal{H}|\leqslant K\), where \(Y,K\) are appropriate functions of \(x\).

### 2.2 The cutoff \(z(t)\)

In [[37][74]], Pólya suggests using a truncation \(x^{1/e^{\gamma}}\) to justify the Hardy-Littlewood conjectures. The observation that the cutoff \(\sqrt{x}\) leads to erroneous prime counts was made by Hardy and Littlewood [[19][36], Sect. 4.3] and is occasionally referred to as “the Mertens Paradox” (see [[31][75]]). In discussing the probabilistic heuristic for counting the number of primes below \(x\), Hardy and Littlewood write (here \(\varpi \) denotes a prime) “One might well replace \(\varpi <\sqrt{n}\) by \(\varpi < n\), in which case we should obtain a probability half as large. This remark is in itself enough to show the unsatisfactory character of the argument” and later “*Probability*is not a notion of pure mathematics, but of philosophy or physics.”

### 2.3 Connection to Jacobsthal’s function

Any improvement of the lower bound in ( [1.12][42]) leads to a corresponding improvement of the known upper bound on Jacobsthal’s function \(J(w)\), which we define to be the largest gap which occurs in the set of integers that have no prime factor \(\leqslant w\). Equivalently, \(J(w)\) is the largest gap in \(\mathcal{S} _{w}\). Iwaniec [[21][41]] proved that \(J(w)\ll w^{2}\) using his linear sieve bounds. Using Montgomery and Vaughan’s explicit version of the Brun-Titchmarsh inequality [[29][76]], the cardinality of the set \(\mathcal{S} _{w}(y):=[0,y] \cap \mathcal{S} _{w}\) for \(w > (y/\log y)^{1/2}\) can be bounded from below by

$$\begin{aligned} |\mathcal{S} _{w}(y)|&\geqslant | \mathcal{S} _{(y/\log y)^{1/2}}(y)| - \sum _{(y/\log y)^{1/2}< p \leqslant w} |\mathcal{S} _{(y/\log y)^{1/2}}(y) \cap (a_{p} \bmod p)| \\ &\geqslant W_{y}-\sum _{(y/\log y)^{1/2}< p \leqslant w}\frac{2y/p}{\log (2y/p)}. \end{aligned}$$

If the right side is positive, it follows that \(J(w)< y\). Suppose, for example, that \(W_{y} \geqslant \alpha y/\log y\) for large \(y\), where \(0<\alpha \leqslant 1\) is fixed. Mertens’ estimates then imply that

$$ {J(w) \ll w^{1+e^{-\alpha /2}+o(1)} \qquad (w\to \infty )}, $$

which improves Iwaniec’s upper bound.

We remark that all of the unconditional lower bounds on , including the current record [[11][20]], have utilized the simple inequality , where \(y\sim \log x\).

### 2.4 The interval sieve problem and exceptional zeros

The problem of determining \(W_{y}\) asymptotically is connected with the famous problem about exceptional zeros of Dirichlet \(L\) -functions (also known as Siegel zeros or Landau-Siegel zeros); see, e.g., [[7][77], Sects. 14, 20, 21, 22] for background on these and [[22][78]] for further discussion.

### Definition 2.1

We say that *exceptional zeros exist*if there is an infinite set \(\mathcal{E} \subset \mathbb{N} \), such that for every \(q\in \mathcal{E} \) there is a real Dirichlet character \(\chi _{q}\) and a zero \(1-\delta _{q}\) with \(L(1-\delta _{q},\chi _{q})=0\) and \(\delta _{q}=o(1/\log q)\) as \(q\to \infty \).

### Theorem 2.2

*Suppose that exceptional zeros exist*. *Then*

$$ \liminf _{y\to \infty} \frac{W_{y}}{y/\log y}=0 \qquad \textit{and} \qquad \limsup _{u\to \infty} \frac{g(u)}{u}=\infty . $$

*Hence*, *we almost surely have*

*and Conjecture*[1.2][79]*implies that*

Our proof of Theorem [2.2][64], given in Sect. [9][65], is quantitative, exhibiting an upper bound for \(W_{y}\) in terms of the decay of \(\delta _{q}\). Siegel’s theorem [[7][77], Sect. 21] implies that \(\frac{\log 1/\delta _{q}}{\log q} \to 0\), but we cannot say anything about the rate at which this occurs (i.e., the bound is *ineffective*). If the rate of decay to zero is extremely slow, then our proof shows that, infinitely often, \(W_{y}=f(y) \frac{y\log _{2} y}{\log y}\), with \(f(y)\to \infty \) extremely slowly. Consequently, is infinitely often close to the upper bound in ( [1.15][80]).

The related quantity

$$ \widetilde{W}_{y}:=\max | S_{ \sqrt{y}} \cap [0,y] |, $$

is known by the theory of upper bound sieves to satisfy \(\widetilde{W}_{y} \leqslant \frac{2y}{\log y}\) (see, e.g., [[30][81]]), and it is well known that an improvement of the constant two would imply that exceptional zeros do not exist; see, e.g., Selberg’s paper [[39][82]]. Theorem [2.2][64] (in the contrapositive) similarly asserts that an improvement of the constant zero in the trivial lower bound \(W_{y} \geqslant 0\cdot \frac{y}{\log y}\) implies that exceptional zeroes do not exist. Extending our ideas and those of Selberg, Granville [[17][83]] has recently shown that if exceptional zeros exist, then for any real \(r>1\),

$$\begin{aligned} \liminf _{y\to \infty} \frac{\min _{(a_{p})} |[0,y] \cap \mathcal{S} _{y^{1/r}}|}{e^{-\gamma} y/\log y^{1/r}} &=f(r), \\ \limsup _{y\to \infty} \frac{\max _{(a_{p})} |[0,y] \cap \mathcal{S} _{y^{1/r}}|}{e^{-\gamma} y/\log y^{1/r}} &=F(r), \end{aligned}$$

where \(f,F\) are the lower and upper linear sieve functions. In particular, \(f(r)=0\) for \(r\leqslant 2\) and \(f(r)>0\) for \(r>2\).

It is widely believed that exceptional zeros do not exist, and this is a famous unsolved problem. Theorem [2.2][64] indicates that to fully understand \(W_{y}\), it is necessary to solve this problem. Iwaniec’s lectures [[22][78]] give a nice overview of the problem of exceptional zeros, attempts to prove that they do not exist, and various consequences of their existence. In the paper [[10][84]], the second author shows that if there is a sequence of moduli \(q\) with \(\delta _{q}\ll (\log q)^{-2}\), then one can deduce larger lower bounds for \(J(w)\) and than are currently known unconditionally.

### 2.5 Primes in longer intervals

With probability one, the Cramér model also satisfies

(2.1)

as long as \(x\to \infty \), \(y\leqslant x\), and \(y/\log ^{2} x\to \infty \). However, Maier [[25][85]] has shown that the analogous statement for primes is false, namely that for any fixed \(A>1\) one has

$$ \liminf \limits _{x\to \infty} \frac{\pi (x+(\log x)^{A})-\pi (x)}{(\log x)^{A-1}}< 1 \quad \text{and}\quad \limsup \limits _{x\to \infty} \frac{\pi (x+(\log x)^{A})-\pi (x)}{(\log x)^{A-1}}>1. $$

(2.2)

The disparity between ( [2.1][86]) and ( [2.2][87]) again stems from the uniform distribution of in residue classes modulo primes. Both models and satisfy the analogs of ( [2.2][87]); we omit the proofs. Moreover, the ideas behind Theorem [1.1][19] can be used to sharpen ( [2.2][87]), by replacing the right sides of the inequalities by quantities defined in terms of the extremal behavior of \(|[0,y] \cap S_{y^{1/u}}|\) for fixed \(u>1\); we refer the reader to [[23][88], Exercise 30.1] for details. The authors thank Dimitris Koukoulopoulos for this observation.

By contrast, on the Riemann Hypothesis, Selberg [[38][89]] showed that

$$ \pi (x+y)-\pi (x)\sim \frac{y}{\log x} $$

holds for *almost all*\(x\) provided that \(y=y(x) \leqslant x\) satisfies \(y/\log ^{2} x \to \infty \) as \(x \to \infty \).

On a related note, Granville and Lumley [[18][90]] have developed heuristics and conjectures concerning the *maximum*number of primes \(\leqslant x\) lying in intervals of length \(L\), where \(L\) varies between \(\log x\) and \(\log ^{2} x\).

### 2.6 Remarks on the singular series and prime gaps

If \(y\) is small compared to \(x\), the difference is a random variable with (essentially) a binomial distribution. Letting \(y\to \infty \) with \(y/\log x\) fixed, the result is a Poisson distribution: for any real \(\lambda >0\) and any integer \(k\geqslant 0\), we have

(2.3)

with probability one. In particular, using as a model for the primes , this leads to the conjecture that

$$ \lim _{x\to \infty} \pi (x)^{-1}\big|\{p_{n}\leqslant x:p_{n+1}-p_{n} \geqslant \lambda \log p_{n}\}\big| =e^{-\lambda} \qquad (\lambda >0). $$

(2.4)

Gallagher [[14][50]] showed that if the Hardy-Littlewood conjectures ( [1.4][34]) are true uniformly for \(\mathcal{H}\subset [0, \log ^{2} x]\) with fixed cardinality \(|\mathcal{H}|\), then ( [2.4][91]) follows. His analysis relies on the relation

$$ \sum _{\substack{\mathcal{H}\subset [0,y]\\|\mathcal{H}|=k}} \mathfrak{S} (\mathcal{H}) \sim \binom{y}{k}\qquad (y\to \infty ), $$

(2.5)

which asserts that the singular series has an average value of one. Sharper versions of ( [2.5][92]) exist (see, e.g., Montgomery and Soundararajan [[28][46]]); such results, however, are uniform only in a range \(|\mathcal{H}| \ll \log _{2} y\) or so, far too restrictive for our use. Reinterpreting the sum on the left side of ( [2.5][92]) probabilistically, as we have done above, allows us to adequately deal with a much larger range of sizes \(|\mathcal{H}|\). In particular, it is possible to deduce from a uniform version of ( [1.16][48]) a uniform version of ( [2.4][91]), although we have not done so in this paper.

We take this occasion to mention a recent unconditional theorem of Mastrostefano [[26][93], Theorem 1.1], which is related to ( [2.5][92]), and which states that for any integer \(m\geqslant 0\) there is an \(\varepsilon =\varepsilon (m)>0\) so that whenever \(0<\lambda <\varepsilon \), we have

Establishing the Poisson distribution ( [2.3][94]) unconditionally, even for some fixed \(\lambda \), seems very difficult.

### 2.7 The maximal gap in Granville’s model

The claimed bounds in Theorem [1.1][19] are also satisfied by Granville’s random set , i.e., one has

The proof is very short, and we sketch it here as a prelude to the proof of Theorem [1.1][19]. Consider the elements of in \((x,2x]\) for \(x\) a power of two. In accordance with ( [1.14][45]), let \(y\) satisfy \(\log ^{2} x \leqslant y=o(\log ^{2} x \log _{2} x)\) and put \(A:=(y/\log y)^{1/2}\), so that \(A=o(\log x)\). Let \(\theta :=\prod _{p\leqslant A} (1-1/p)^{-1} \sim (e^{\gamma}/2)\log y\) and \(Q:=\prod _{p\leqslant A}p\). For simplicity, we suppose that each \(n\in (x,2x]\) with \((n,Q)=1\) is chosen for inclusion in with probability \(\theta /\log x\); this modification has a negligible effect on the size of the largest gap. Fix \(\varepsilon >0\) arbitrarily small. Let \(X_{m}\) denote the event .

Let \(D_{m}\) denote the number of integers in \((m,m+y]\), all of whose prime factors are larger than \(A\). If we take \(y:=g((\xi +\varepsilon )\log ^{2} x)\), then

$$ \begin{aligned} \mathbb{E}\big|\{x< m\leqslant 2x: X_{m} \}\big| &= \sum _{x< m\leqslant 2x} (1-\theta /\log x)^{{D_{m}}} \\ &\leqslant x (1-\theta /\log x)^{W_{y}} \leqslant x e^{-\theta W_{y}/\log x} \\ &\ll x^{-\varepsilon /2} \end{aligned} $$

by our assumption that \(W_{y}\log y \sim (\xi +\varepsilon )\log ^{2} x\). Summing on \(x\) and applying Borel-Cantelli, we see that almost surely, only finitely many \(X_{m}\) occur.

For the lower bound, we take \(y:=g((\xi -\varepsilon )\log ^{2} x)\) and restrict to special values of \(m\), namely \(m\equiv b \bmod Q\), where \(b\) is chosen so that

$$ {D_{b}=W_{y}.} $$

Let \(\mathcal{M} :=\{x< m \leqslant 2x: m\equiv b\bmod Q\}\) and let \(N\) be the number of \(m\in \mathcal{M} \) for which \(X_{m}\) occurs. By the above argument, we see that

$$ \mathbb{E}N=|\mathcal{M} | (1-\theta /\log x)^{W_{y}}. $$

By assumption, \(|\mathcal{M} |=x^{1-o(1)}\) and hence the right side is \(> x^{\varepsilon /2}\) for large \(x\). Similarly,

$$ \begin{aligned} \mathbb{E}N^{2} &=|\mathcal{M} | (1-\theta /\log x)^{W_{y}}+(| \mathcal{M} |^{2}-|\mathcal{M} |) (1- \theta /\log x)^{2W_{y}} \\ &=(\mathbb{E}N)^{2}+O(\mathbb{E}N). \end{aligned} $$

By Chebyshev’s inequality, \(\mathbb{P}(N < \frac{1}{2} \mathbb{E}N) \ll 1/\mathbb{E}N \ll x^{-\varepsilon /2}\). Considering all \(x\) and using Borel-Cantelli, we conclude that almost surely every sufficiently large dyadic \((x,2x]\) contains an \(m\) for which \(X_{m}\) occurs.

We remark that our lower bound argument above works as well for the Cramér model, showing ( [1.2][25]). We take \(A=Q=\theta =b=1\), and the details are simpler.

## 3 Preliminaries

### 3.1 Notation

The indicator function of any set \(\mathcal{T} \) is denoted \(\mathbf{1}_{\mathcal{T} } (n)\). We select residue classes \(a_{p} \bmod p\) uniformly and independently at random for each prime \(p\), and then for any set of primes \(\mathcal{Q} \) we denote by the ordered tuple \((a_{p}:p\in \mathcal{Q} )\); often we condition our probabilities on for a fixed choice of \(\mathcal{Q} \).

Probability, expectation, and variance are denoted by ℙ, \(\mathbb{E}\), and \(\mathbb{V} \) respectively. We use \(\mathbb{P}_{\mathcal{Q} }\) and \(\mathbb{E}_{\mathcal{Q} }\) to denote the probability and expectation, respectively, with respect to random . When \(\mathcal{Q} \) is the set of primes in \((c,d]\), we write , \(\mathbb{P}_{c,d}\) and \(\mathbb{E}_{c,d}\); if \(\mathcal{Q} \) is the set of primes \(\leqslant c\), we write , \(\mathbb{P}_{c}\) and \(\mathbb{E}_{c}\). In particular, \(\mathbb{P}_{c,d}\) refers to the probability over random , often with conditioning on .

Throughout the paper, any implied constants in symbols \(O\), ≪ and ≫ are *absolute*(independent of any parameter) unless otherwise indicated. The notations \(F\ll G\), \(G\gg F\) and \(F=O(G)\) are all equivalent to the statement that the inequality \(|F|\leqslant c|G|\) holds with some constant \(c>0\). We write \(F\asymp G\) to indicate that \(F\ll G\) and \(G\ll F\) both hold. The notation \(o(1)\) is used to indicate a function that tends to zero as \(x\to \infty \); in expressions like \(1-o(1)\), the function is assumed to be positive. We write \(F \sim G\) when \(F=(1+o(1)) G\) as \(x\to \infty \).

For a set ℋ of integers, we denote \(\mathcal{H}-\mathcal{H}:=\{h-h': h,h'\in \mathcal{H}\}\), and for any integer \(m\), \(\mathcal{H}+m :=\{ h+m:h\in \mathcal{H}\}\).

### 3.2 Various inequalities

We collect here some standard inequalities from sieve theory and probability that are used in the rest of the paper.

### Lemma 3.1

Upper bound sieve, [[30][81], Theorem 3.8]

*For*\(1\leqslant w\leqslant p \leqslant y\), \(p\)*prime*, \(b\in \mathbb{Z} /p\mathbb{Z} \), *and an arbitrary interval*ℐ *of length*\(y\), *we have uniformly*

$$ \big|\{n\in \mathcal{I} : n\equiv b\bmod p,\big(n,\prod _{q \leqslant w} q\big)=1\}\big| \ll \frac{y/p}{1+\min \{\log w,\log (y/p)\}}. $$

### Lemma 3.2

Azuma’s inequality [[1][95]]

*Suppose that*\(X_{0},\ldots ,X_{n}\)*is a martingale with*\(|X_{j+1}-X_{j}|\leqslant c_{j}\)*for each*\(j\). *Then*

$$ \mathbb{P}\left ( |X_{n}-X_{0}| \geqslant t \right ) \leqslant 2 \exp \left \{ - \frac{t^{2}}{2(c_{0}^{2}+\cdots +c_{n-1}^{2})}\right \} \qquad (t>0). $$

### Lemma 3.3

Bennett’s inequality [[3][96]]

*Suppose that*\(X_{1},\ldots ,X_{n}\)*are independent random variables such that for each*\(j\), \(\mathbb{E}X_{j}=0\), *and*\(|X_{j}|\leqslant M\)*holds with probability one*. *Then*

$$ \mathbb{P}\bigg(\bigg|\sum _{1\leqslant j \leqslant n} X_{j}\bigg| \geqslant t \bigg) \leqslant 2\exp \bigg\{ - \frac{\sigma ^{2}}{M^{2}}\,\mathscr{L} \bigg( \frac{Mt}{\sigma ^{2}}\bigg) \bigg\} \qquad (t>0), $$

*where*\(\sigma ^{2}:=\sum _{j} \mathbb{V} X_{j}\), *and*

$$ \mathscr{L} (u):=\intop \nolimits _{1}^{1+u}\log t\,dt=(1+u)\log (1+u)-u. $$

### Lemma 3.4

*For any*\(\mathcal{H}\subset [0,y]\)*with*\(|\mathcal{H}|=k\), *we have*

$$ \mathfrak{S} _{z}(\mathcal{H})=\mathfrak{S} (\mathcal{H}) \bigg(1+O\bigg( \frac{k^{2}}{z} \bigg) \bigg) \qquad {(z>\max (y,k^{2}))} $$

(3.1)

*and*

$$ {\mathfrak{S} (\mathcal{H}) \leqslant e^{O(k \log _{2}(y))}.} $$

(3.2)

### Proof

Estimate ( [3.1][97]) follows from the definition of \(\mathfrak{S} (\mathcal{H})\) and the fact that for \(p>y\), \(|\mathcal{H}\bmod p|=k\). Estimate ( [3.2][98]) is trivial if ℋ is inadmissible, since then \({\mathfrak{S} (\mathcal{H})}=0\), and otherwise ( [3.2][98]) is a special case of [[15][99], (6.16)]. □

### Lemma 3.5

*If*\(\mathcal{H}\subseteq [0,y]\)*is an admissible*\(k\) -*tuple and*\(t\geqslant 2\)*satisfies*\(z(t) > y\)*and*\(k\leqslant t^{1/100}\), *then*

$$ V_{\mathcal{H}}(z(t))=\frac{\mathfrak{S} (\mathcal{H})}{(\log t)^{k}} \big( 1+O(1/t^{0.55}) \big). $$

### Proof

Let \(z:=z(t)\). By ( [1.7][100]), \(z \gg t^{1/e^{\gamma}} \gg t^{0.561}\). Using Lemma [3.4][66] and ( [1.7][100]), we have

$$\begin{aligned} V_{\mathcal{H}}(z(t)) &=\mathfrak{S} _{z}(\mathcal{H}) \Theta _{z}^{k} \\ &=\mathfrak{S} (\mathcal{H}) \left ( 1+O\left ( \frac{k^{2}}{z}\right )\right ) \left ( \frac{1}{\log t}+O(t^{-1/e^{\gamma}}) \right ) ^{k}. \end{aligned}$$

The lemma now follows since \(k\leqslant t^{1/100}\). □

## 4 Uniform Hardy-Littlewood from the model

In this section, we prove Theorems [1.3][53] and [1.4][56] using the first and second moment bounds provided by the following proposition.

### Proposition 4.1

First and second moment bounds

*Suppose that*\(x\)*and*\(y\)*are integers with*\(x\geqslant 3\)*and*\(\sqrt{x}\leqslant y\leqslant x\), *and suppose that*\(0\leqslant D\leqslant \sqrt{x}\). *Let*\(\mathcal{H}\subset [0,D]\)*be an admissible tuple with*\(k:=|\mathcal{H}|\leqslant \frac{\log x}{(\log _{2} x)^{2}}\), *and put*

*Then*

$$ \mathbb{E}\bigg(\sum _{x< n\leqslant x+y} X_{n}\bigg)={ \mathfrak{S} (\mathcal{H}) \intop \nolimits _{x}^{x+y} \frac{dt}{(\log t)^{k}}+O\bigg( \frac{yD}{x}+\frac{y}{x^{0.54}} \bigg).} $$

(4.1)

*Furthermore*,

$$ \mathbb{V} \bigg( \sum _{x< n\leqslant x+y} X_{n} \bigg) \ll y \left ( \frac{D}{x} {+\frac{yD^{2}}{x^{2}}}+ V_{\mathcal{H}}(z(x)){(k^{2}+yD/x)}+V_{\mathcal{H}}(z(x))^{2} F \right ) , $$

(4.2)

*where*

$$ F:=\textstyle\begin{cases} (\log x)^{k^{2}} &\quad \textit{if $k\leqslant \frac{(\log x)^{1/2}}{\log _{2} x}$}, \\ y^{\frac{4\varrho ^{2}-1}{4\varrho ^{2}-\varrho}} \exp \Big\{ O\Big( \frac{\log x\log _{3} x}{\log _{2} x}\Big)\Big\} &\quad \textit{if $\frac{(\log x)^{1/2}}{\log _{2} x} \leqslant k=(\log x)^{ \varrho}\leqslant \frac{\log x}{(\log _{2} x)^{2}}$}. \end{cases} $$

Before turning to the proof of the proposition, we first indicate how it is used to prove the two theorems, starting with Theorem [1.4][56].

### Proof of Theorem [1.4][56]

Fix \(c>3/2\). For any integers \(u\geqslant 2\) and \(v\geqslant 0\), we let

We apply Proposition [4.1][101] in the case that \(\mathcal{H}=\{0\}\), \(k= 1\) and \(D= 0\). By ( [4.1][102]), if \(v\geqslant \sqrt{u}\) then

$$ \mathbb{E}\Delta (u,u+v) \ll \frac{v}{u^{0.54}} \ll u^{0.46}. $$

(4.3)

Inequality ( [4.2][103]) implies that

$$ \mathbb{V} \big(\Delta (u,u+v)\big)\ll v \big( V_{\mathcal{H}}(z(u))+V_{\mathcal{H}}(z(u))^{2}\log u \big)\ll \frac{v}{\log u}. $$

Let \(x\) be a large integer. For integers \(h,m\) with \(2\sqrt{x} \leqslant 2^{m} \leqslant x\) and \(0\leqslant h\leqslant x/2^{m}-1\), let \(G_{m,h}\) be the event that

$$ \big|\Delta (x+h\cdot 2^{m},x+(h+1)2^{m})\big| \leqslant x^{1/2}(\log x)^{c-1}. $$

For large \(x\), ( [4.3][104]) implies that

$$ \big| \mathbb{E}\Delta (x+h\cdot 2^{m},x+(h+1)2^{m})\big| \leqslant \frac{x^{1/2} (\log x)^{c-1}}{2}. $$

Hence, Chebyshev’s inequality yields the bound

$$ \mathbb{P}\big( \text{not } G_{h,m} \big) \ll \frac{2^{m}}{x(\log x)^{2c-1}}. $$

Let \(F_{x}\) denote the event that \(G_{h,m}\) holds for all such \(h,m\). By a union bound, we see that \(\mathbb{P}F_{x}=1-O((\log x)^{2-2c})\). On this event \(F_{x}\), for any integer \(y\) with \(1\leqslant y\leqslant x\), we have

$$\begin{aligned} |\Delta (x,x+y)| &=\bigg| \sum _{{2\sqrt{x}} \leqslant 2^{m} \leqslant y} \Delta \Big( x+{ \left \lfloor y/2^{m+1} \right \rfloor } 2^{m+1}, x+{ \left \lfloor y/2^{m} \right \rfloor } 2^{m} \Big) \bigg| {+O(\sqrt{x})} \\ &\leqslant \sum _{{2\sqrt{x}} \leqslant 2^{m} \leqslant y} x^{1/2} ( \log x)^{c-1} {+O(\sqrt{x})} \\ &{\ll} x^{1/2} (\log x)^{c}. \end{aligned}$$

Since \(2c-2>1\), the Borel-Cantelli lemma implies that with probability one, \(F_{2^{s}}\) is true for all large integers \(s\). On this event, \(\Delta (2,x) \ll x^{1/2} (\log x)^{c}\) for all real \(x\geqslant 2\), proving the theorem. □

### Proof of Theorem [1.3][53]

Fix \(c\in [1/2,1)\) and \(\varepsilon >0\). For integers \(a\geqslant 2\), \(b\geqslant 0\) and a tuple ℋ, define

Let

$$ \lambda :=1 - \frac{1-c}{8c^{2}-2c}. $$

Let \(u\) be a large integer in terms of \(c\) and \(\varepsilon \), and let \(F_{u}\) denote the event that

$$ |\Delta (a,a+b;\mathcal{H})| \leqslant u^{\lambda + \varepsilon } $$

for all integers \(a,b\) satisfying \(u\leqslant a \leqslant a+b \leqslant 2u\) and all admissible tuples ℋ satisfying

$$ |\mathcal{H}|=k\leqslant 10(\log u)^{c}, \quad \mathcal{H}\subset \Big[ 0, \exp \Big\{ 10(\log u)^{1-c}/\log _{2} u \big\} \Big]. $$

(4.4)

The number of such ℋ does not exceed \(u^{100/\log _{2} u}=u^{o(1)}\) as \(u\to \infty \).

We again invoke the moment bounds in Proposition [4.1][101]. Assume ℋ satisfies ( [4.4][105]) and that \(u\leqslant a\leqslant 2u\) and \(\sqrt{a}\leqslant b\leqslant a\). It follows from ( [4.1][102]) that

$$ \mathbb{E}\Delta (a,a+b;\mathcal{H}) \ll \frac{b u^{o(1)}}{a}+\frac{b}{a^{0.54}} \ll u^{0.46}, $$

and inequality ( [4.2][103]) implies

$$ {\mathbb{V} \Delta (a,a+b;\mathcal{H})} \ll b^{1+ \frac{4c^{2}-1}{4c^{2}-c}+o(1)} a^{o(1)} \ll b u^{2\lambda -1+o(1)}, $$

where the implied function \(o(1)\) is uniform over all such ℋ, \(a\) and \(b\). For integers \(h,m\) with \(2\sqrt{u} \leqslant 2^{m} \leqslant u\) and \(0\leqslant h \leqslant u/2^{m}-1\), let \(G_{h,m}\) be the event that for all ℋ satisfying ( [4.4][105]),

$$ |\Delta (u+h\cdot 2^{m}, u+(h+1)\cdot 2^{m};\mathcal{H})| \leqslant u^{\lambda +\varepsilon /2}. $$

Again, if \(u\) is large enough, the expectation of the left side is at most \(\frac{1}{2} u^{\lambda +\varepsilon /2}\), uniformly over all \(h,m,\mathcal{H}\). By a union bound and Chebyshev’s inequality,

$$\begin{aligned} \mathbb{P}\big( \cup _{h,m} (\text{not } G_{h,m})\big) & \leqslant \sum _{h,m} \sum _{\mathcal{H}} \mathbb{P}\big(\big|\Delta (u+h \cdot 2^{m},u+(h+1)\cdot 2^{m};\mathcal{H})\big|\geqslant \tfrac{1}{2} u^{\lambda +\varepsilon /2}\big) \\ &\ll \sum _{h,m} \sum _{\mathcal{H}} \frac{2^{m}}{u^{1+\varepsilon +o(1)}} \ll \frac{1}{u^{\varepsilon /2}}. \end{aligned}$$

Furthermore, as in the proof of Theorem [1.4][56], we see that if \(u\) is large enough (in terms of \(c,\varepsilon \)) and if \(G_{h,m}\) holds for all \(h,m\), then \(F_{u}\) holds. Therefore,

$$ \mathbb{P}F_{u}=1 -O\big( 1/u^{\varepsilon /2} \big). $$

By Borel-Cantelli, almost surely \(F_{2^{s}}\) is true for all sufficiently large integers \(s\).

Now assume that we are in the event that \(F_{2^{s}}\) holds for all \(s\geqslant s_{0}\). Let \(x\) be sufficiently large such that \(x \geqslant 2^{3s_{0}+1}\) and \(2^{t-1} < x \leqslant t^{s}\), and let ℋ be an admissible tuple with

$$ k :=|\mathcal{H}| \leqslant (\log x)^{c}, \qquad \mathcal{H}\subseteq \Big[ 0, \exp \Big\{ \frac{(\log x)^{1-c}}{\log _{2} x} \Big\} \Big]. $$

Note that whenever \(x^{1/3} \leqslant u=2^{s} \leqslant x\) we have ( [4.4][105]). Thus, using ( [3.2][98]),

as required for Theorem [1.3][53]. □

The following lemma is needed in the proof of Proposition [4.1][101]. When an admissible tuple ℋ is fixed, define

$$ \psi _{t} :=V_{\mathcal{H}}(z(t)). $$

### Lemma 4.2

*Let*\(2\leqslant u \leqslant v \leqslant 3u\), *and suppose*ℋ *is an admissible tuple with*\(k:=|\mathcal{H}| \geqslant 1\). *Then*

$$ \psi _{u} - \psi _{v} \ll k\psi _{u} \left ( \frac{1}{u^{1/e^{\gamma}}}+ \frac{v-u}{u\log u} \right ) . $$

### Proof

We begin with the simple bound

$$ \begin{aligned} \psi _{u}-\psi _{v} &=\psi _{u}\bigg(1-\prod _{z(u)< p \leqslant z(v)} (1-\nu _{p}/p)\bigg) \\ &\leqslant \psi _{u}\sum _{z(u)< p \leqslant z(v)}\frac{\nu (p)}{p} \\ &\leqslant k\psi _{u}\sum _{z(u)< p \leqslant z(v)}\frac{1}{p}. \end{aligned} $$

(4.5)

By multiple applications of ( [1.7][100]),

$$\begin{aligned} \sum _{z(u)< p\leqslant z(v)}\frac{1}{p} & \leqslant \sum _{z(u)< p\leqslant z(v)} - \log (1-1/p)= \log \bigg( \Theta _{z(u)}/\Theta _{z(v)} \bigg) \\ &=\log \left ( \frac{\log v}{\log u}\Big(1+O(1/z(u)) \Big) \right ) \\ &\ll \frac{1}{z(u)}+\log \left ( 1+ \frac{\log (v/u)}{\log u} \right ) \\ &\ll \frac{1}{z(u)}+\frac{\log (v/u)}{\log u} \\ &\ll \frac{1}{u^{1/e^{\gamma}}}+\frac{v-u}{u\log u}. \end{aligned}$$

This completes the proof. □

### Proof of Proposition [4.1][101]

Suppose that \(\mathcal{H}\subset [0,D]\) with \(k:=|\mathcal{H}| \leqslant \frac{\log x}{(\log _{2} x)^{2}}\). We may assume that \(D\) is an integer. Write \(\nu _{p}:=|\mathcal{H}\bmod p|\) for every prime \(p\). Since \(z(t)\) is increasing and \(\psi _{u}\) is decreasing in \(u\),

$$ \psi _{n+D} \leqslant \mathbb{E}X_{n} \leqslant \psi _{n}. $$

Hence,

$$ \mathbb{E}\sum _{x< n\leqslant x+y} X_{n}=\sum _{x< n \leqslant x+y} \psi _{n}+O\bigg( \sum _{j=1}^{D} \big( \psi _{x+j} - \psi _{x+y+j} \big) \bigg). $$

By Lemma [4.2][106] and the bound \(\psi _{u}\ll 1/\log u\), the big- \(O\) term is

$$ \ll \frac{kD}{\log x} \bigg( \frac{1}{x^{1/e^{\gamma}}}+ \frac{y}{x\log x} \bigg) \ll \frac{kDy}{x\log ^{2} x}, $$

since \(y\geqslant \sqrt{x}\) and \(1/e^{\gamma} > 1/2\). This proves that

$$ \mathbb{E}\sum _{x< n\leqslant x+y} X_{n}=\sum _{x< n \leqslant x+y} \psi _{n}+O\left ( \frac{kDy}{x\log ^{2} x}\right ). $$

(4.6)

Lemma [3.5][107] implies that for each integer \(n\in (x,x+y]\) we have

$$ \psi _{n}=\frac{\mathfrak{S} (\mathcal{H})}{(\log n)^{k}} \left ( 1+O(1/x^{0.55}) \right ) = \mathfrak{S} (\mathcal{H}) \intop \nolimits _{n-1}^{n} \frac{dt}{(\log t)^{k}}+O\left ( \frac{\mathfrak{S} (\mathcal{H})}{x^{0.55}}\right ). $$

Estimate ( [3.2][98]) implies that \(\mathfrak{S} (\mathcal{H}) \leqslant x^{o(1)}\) and this proved the estimate ( [4.1][102]) of the proposition.

For the second moment bound, let \(v\) be a parameter in \([4k,\log x]\) and set \(Q:=\prod _{p\leqslant v} p\). Given integers \(n_{1}\) and \(n_{2}\) with \(x< n_{1} < n_{2} \leqslant x+y\), define \(m\) and \(b\) by

$$ m:=n_{2}-n_{1},\qquad b\equiv m\bmod Q\quad \text{with}\quad b\in [0,Q). $$

We consider separately the primes \(\leqslant v\) and those \(>v\), setting

$$ \psi '_{n}:=\prod _{v< p\leqslant z(n)} \left ( 1-\frac{\nu _{p}}{p}\right ) , \qquad \xi _{b}:=\prod _{p \leqslant v}\left ( 1- \frac{|(\mathcal{H}\cup (\mathcal{H}+b))\bmod p|}{p}\right ) . $$

Then

$$ \begin{aligned} \mathbb{E}X_{n_{1}}X_{n_{2}}&\leqslant \prod _{p \leqslant z(n_{1})}\left ( 1- \frac{|(\mathcal{H}\cup (\mathcal{H}+m)) \bmod p|}{p}\right ) \prod _{z(n_{1})< p \leqslant z(n_{2})}\left ( 1- \frac{\nu _{p}}{p}\right ) \\ &=\frac{\psi '_{n_{2}}}{\psi '_{n_{1}}}\,\xi _{b} \prod _{v< p \leqslant z(n_{1})}\left ( 1- \frac{|(\mathcal{H}\cup (\mathcal{H}+m))\bmod p|}{p}\right ) . \end{aligned} $$

(4.7)

For technical reasons, we use the trivial bound \(\mathbb{E}X_{n_{1}}X_{n_{2}}\leqslant \psi _{n_{1}} \leqslant \psi _{x}\) when \(m\in \mathcal{H}-\mathcal{H}\); the total contribution from such terms is \(\leqslant \psi _{x}k^{2} y\), which is an acceptable error term for ( [4.2][103]).

Now suppose that \(m\notin \mathcal{H}-\mathcal{H}\). For any prime \(p>v\) and integer \(a\in (-p/2,p/2)\), let

$$ \lambda _{a}(p):=|(\mathcal{H}\cap (\mathcal{H}+a))\bmod p|. $$

Then, given \(v< p\leqslant z(x+y)\) and \(m\) we have

$$ |(\mathcal{H}\cup (\mathcal{H}+m))\bmod p|=2\nu _{p}-\lambda _{a}(p), $$

where \(a\) is the unique integer such that

$$ a\equiv m\bmod p\quad \text{and}\quad {|a|< p/2}. $$

Clearly, \(\lambda _{a}(p) \leqslant \nu _{p} \leqslant k\), and \(\lambda _{a}(p)=0\) unless \(a\in (\mathcal{H}-\mathcal{H})\cap (-p/2,p/2)\). In addition,

$$ \sum _{a} \lambda _{a}(p)=\nu _{p}^{2}. $$

(4.8)

Consequently, for any \(p>v\) we have

$$ 1- \frac{|(\mathcal{H}\cup (\mathcal{H}+m))\bmod p|}{p}= \bigg(1- \frac{2\nu _{p}}{p}\bigg)(1+f_{a}(p)) $$

with

$$ f_{a}(p):=\frac{\lambda _{a}(p)}{p-2\nu _{p}} $$

We remark that \(f_{a}(p)\in (0,1]\) since \(p>v\geqslant 4k\geqslant 4\nu _{p} {\geqslant 4\lambda _{a}(p)}\). For a fixed choice of \(a\in \mathcal{H}- \mathcal{H}\) and fixed \(n_{1}\), extend \(f_{a}\) to a multiplicative function supported on squarefree integers whose prime factors all lie in \(I(n_{1},a):=(\max \{v,2|a| \},z(n_{1})]\). If an integer \(r\) has a prime factor outside the interval \(I(n_{1},a)\) or \(r\) is not squarefree, we set \(f_{a}(r):=0\). Then

$$\begin{aligned} &\prod _{v< p\leqslant z(n_{1})}\left ( 1- \frac{|(\mathcal{H}\cup (\mathcal{H}+m))\bmod p|}{p}\right ) \\ &\qquad \qquad =\prod _{v< p\leqslant z(n_{1})} \left ( 1-\frac{2\nu _{p}}{p}\right ) \prod _{a\in \mathcal{H}-\mathcal{H}}~\prod _{ \substack{v< p\leqslant z(n_{1})\\p\,\mid \,m-a}}(1+f_{a}(p)) \\ &\qquad \qquad =\prod _{v< p\leqslant z(n_{1})} \left ( 1-\frac{2\nu _{p}}{p}\right ) \prod _{a\in \mathcal{H}-\mathcal{H}}~\sum _{d_{a}\,\mid \,(m-a)}f_{a}(d_{a}) \end{aligned}$$

(since \(m\notin \mathcal{H}-\mathcal{H}\), we always have \(m-a\ne 0\)). Recalling ( [4.7][108]) we obtain that

$$ \mathbb{E}X_{n_{1}} X_{n_{2}}\leqslant \psi '_{n_{1}}\psi '_{n_{2}} \xi _{b} \prod _{v< p\leqslant z(n_{1})} \left ( \frac{p^{2}-2p\nu _{p}}{(p-\nu _{p})^{2}}\right ) S(n_{1},n_{2}), $$

(4.9)

where

$$ S(n_{1},n_{2}):=\prod _{a \in \mathcal{H}-\mathcal{H}}~\sum _{d_{a}\,\mid \,(m-a)} f_{a}(d_{a}). $$

We now fix \(n_{1}\) and sum over \(n_{2}\). Let

$$\begin{aligned} \mathcal{D} (n_{1}):=\big\{ \mathbf{d}&=(d_{a})_{a\in \mathcal{H}-\mathcal{H}}: \exists \,m\in [1,y]\setminus ( \mathcal{H}-\mathcal{H})~\text{such that}~ \forall \,a,\;~d_{a}\mid (m-a), \\ &\text{ each } d_{a} \text{ is squarefree with all of its prime factors in } I(n_{1},a) \big\} , \end{aligned}$$

i.e., \(\mathcal{D} (n_{1})\) is the set of all possible vectors of the numbers \(d_{a}\). We compute

$$\begin{aligned} \sum _{ \substack{n_{1}< n_{2}\leqslant x+y\\n_{2}-n_{1}\notin \mathcal{H}-\mathcal{H}}} \psi '_{n_{2}}\xi _{b}\,S(n_{1},n_{2}) \leqslant \sum _{ \mathbf{d}\in \mathcal{D} (n_{1})}\Big(\prod _{a}f_{a}(d_{a}) \Big) \sum _{b\bmod Q}\xi _{b}\sum _{ \substack{n_{1}< n_{2}\leqslant x+y\\n_{2}\equiv n_{1}+b\bmod Q\\ \forall a,\;n_{2}\equiv n_{1}+a\bmod{d_{a}}}} \psi '_{n_{2}}, \end{aligned}$$

where we have dropped the condition \(n_{2}-n_{1}\notin \mathcal{H}-\mathcal{H}\) on the right side. A crucial observation is that for every \(\mathbf{d}\in \mathcal{D} (n_{1})\), the components \(d_{a}\) are pairwise coprime. Indeed, if \(a,a'\) are two distinct elements of \(\mathcal{H}-\mathcal{H}\) and a prime \(p>\max \{v,2|a|,2|a'|\}\) divides both \(d_{a}\) and \(d_{a'}\), then there is some \(m\in [1,y]\setminus (\mathcal{H}-\mathcal{H})\) so that \(p\,\mid \,d_{a}\,\mid \,(m-a)\) and \(p\,\mid \,d_{a'}\,\mid \,(m-a')\). This implies \(a\equiv a'\pmod{p}\), a contradiction. Hence, the innermost sum is a sum over a single residue class modulo \(d:=Q\prod _{a} d_{a}\). For any \(e\in \mathbb{Z} \) we have by ( [4.5][109]) that

$$\begin{aligned} \sum _{ \substack{n_{1}< n\leqslant x+y \\ n\equiv e\bmod d}} \psi '_{n} &= \sum _{ \substack{n_{1}< n\leqslant x+y \\ n\equiv e\bmod d}} \bigg[ \frac{1}{d}(\psi '_{n}+\cdots +\psi '_{n+d-1})+O\bigg( k\psi '_{x} \sum _{z(n)< p\leqslant z(n+d)} \frac{1}{p} \bigg) \bigg] \\ &=O(\psi '_{x})+\frac{1}{d} \sum _{n_{1}< n\leqslant x+y} \psi '_{n}, \end{aligned}$$

where we used that \(k\leqslant \log x\) and

$$ \sum _{z(x) < p \leqslant z(x+y+d)} \frac{1}{p} \ll \frac{1}{\log x}. $$

Therefore,

$$ \begin{aligned} \sum _{ \substack{n_{1}< n_{2}\leqslant x+y\\n_{2}-n_{1}\notin \mathcal{H}-\mathcal{H}}} \psi '_{n_{2}}\xi _{b}\,S(n_{1},n_{2}) &\leqslant \frac{1}{Q} \sum _{b\bmod Q} \xi _{b} \sum _{ \substack{{n_{1}< n_{2}\leqslant x+y}}} \psi '_{n_{2}} \sum _{\mathbf{d}\in \mathcal{D} (n_{1})} \prod _{a} \frac{f_{a}(d_{a})}{d_{a}} \\ &\qquad +O\bigg( \psi '_{x} \sum _{b\bmod Q} \xi _{b} \sum _{ \mathbf{d}\in \mathcal{D} (n_{1})} \prod _{a} f_{a}(d_{a}) \bigg). \end{aligned} $$

(4.10)

Now ( [4.8][110]) implies that

$$ \begin{aligned} \sum _{b\bmod Q} \xi _{b} &=\prod _{p\leqslant v} \sum _{c=0}^{p-1} \left ( 1-\frac{|(\mathcal{H}\cup (\mathcal{H}+c))\bmod p|}{p} \right ) \\ &=\prod _{p\leqslant v} \bigg( p - 2\nu _{p}+ \frac{1}{p} \sum _{a} \lambda _{a}(p) \bigg) \\ &=Q \prod _{p\leqslant v}\left ( 1- \frac{\nu _{p}}{p}\right ) ^{2}. \end{aligned} $$

Hence, combining ( [4.9][111]) and ( [4.10][112]), and reinserting terms with \(n_{2}-n_{1}\in \mathcal{H}-\mathcal{H}\), for each \(n_{1}\) we obtain that

$$ \begin{aligned} &\mathbb{E}\sum _{n_{1}< n_{2}\leqslant x+y} X_{n_{1}} X_{n_{2}} \\ &\quad \leqslant \psi _{n_{1}} \sum _{n_{1}< n_{2} \leqslant x+y} \psi _{n_{2}} \prod _{v< p \leqslant z(n_{1})} \left ( \frac{p^{2}-2p\nu _{p}}{(p-\nu _{p})^{2}}\right ) \sum _{\mathbf{d} \in \mathcal{D} (n_{1})} \prod _{a} \frac{f_{a}(d_{a})}{d_{a}} \\ &\qquad +O\Bigg( \psi _{x}^{2} Q \sum _{\mathbf{d}\in \mathcal{D} (n_{1})} \prod _{a} f_{a}(d_{a})+\psi _{x} k^{2} \Bigg). \end{aligned} $$

Extending the first sum over \(\mathbf{d}\) to all pairwise coprime tuples \(\mathbf{d}\) composed of prime factors in \((v,z(n_{1})]\), and applying ( [4.8][110]) again, we find that

$$ \begin{aligned} \sum _{\mathbf{d}\in \mathcal{D} (n_{1})}\prod _{a} \frac{f_{a}(d_{a})}{d_{a}} &\leqslant \prod _{v< p \leqslant z(n_{1})}\left ( 1+\sum _{a} \frac{f_{a}(p)}{p}\right ) \\ &= \prod _{v< p\leqslant z(n_{1})}\left ( 1+ \frac{\nu _{p}^{2}}{p(p-2\nu _{p})}\right ) . \end{aligned} $$

Finally, summing over \(n_{1}\) we conclude that

$$\begin{aligned} \mathbb{E}\sum _{x< n_{1}< n_{2}\leqslant x+y} X_{n_{1}} X_{n_{2}} &\leqslant \sum _{x< n_{1}< n_{2} \leqslant x+y} \psi _{n_{1}} \psi _{n_{2}}+ O(\psi _{x} k^{2}y+\psi _{x}^{2}QTy), \end{aligned}$$

where

$$ T:=\max _{n_{1}} \sum _{\mathbf{d}\in \mathcal{D} (n_{1})} \prod _{a} f_{a}(d_{a}) . $$

Since \(X_{n}^{2}=X_{n}\) we arrive at

$$ \mathbb{E}\bigg( \sum _{x< n\leqslant x+y} X_{n} \bigg)^{2} \leqslant \mathbb{E}\sum _{x< n\leqslant x+y} X_{n}+ \sum _{ \substack{x< n_{1},n_{2} \leqslant x+y \\ n_{1}\ne n_{2}}} \psi _{n_{1}} \psi _{n_{2}}+ O(\psi _{x} k^{2}y+\psi _{x}^{2}QTy), $$

Comparing this with ( [4.6][113]), it follows that the variance in question satisfies

$$ \begin{aligned} \mathbb{V} \sum _{x< n\leqslant x+y} X_{n} & \leqslant \sum _{x< n\leqslant x+y} \big( \psi _{n} - \psi _{n}^{2} \big)+O\big( \psi _{x} k^{2}y+\psi _{x}^{2}QTy \big)+ \\ &\qquad \qquad \qquad +O\bigg(\frac{yD}{x}\sum _{x< n \leqslant x+y} \psi _{n}+\frac{y^{2}D^{2}}{x^{2}}+ \frac{yD}{x}\bigg) \\ &\ll y \psi _{x}+k^{2} y \psi _{x}+\psi _{x}^{2} QTy+ \frac{y^{2} D}{x}\psi _{x}+\frac{y^{2}D^{2}}{x^{2}}+\frac{yD}{x} \\ &\ll k^{2} y \psi _{x}+\psi _{x}^{2} QTy+\frac{yD}{x}\Big[ 1+y(\psi _{x}+D/x) \Big]. \end{aligned} $$

(4.11)

To bound \(T\), we consider two cases. First, suppose that \(k\leqslant (\log x)^{1/2} / \log _{2} x\), and let \(v:=4k\). In this case, we argue crudely, using ( [4.8][110]) and \(\nu _{p}\leqslant k\) for all \(p\), obtaining

$$\begin{aligned} T&\leqslant \prod _{v< p\leqslant z(2x)} \Big( 1+\sum _{|a|< p/2}f_{a}(p) \Big) \\ &=\prod _{4k< p\leqslant z(2x)}\left ( 1+ \frac{k^{2}}{p-2k}\right ) \\ &\leqslant \exp \big(k^{2}(\log _{2}x-\log _{2} k+O(1)) \big) \ll e^{-k^{2}}(\log x)^{k^{2}}. \end{aligned}$$

The prime number theorem implies that \(\log Q \ll v\) and thus \(QT \ll (\log x)^{k^{2}}\). Therefore, ( [4.11][114]) implies ( [4.2][103]).

Next, suppose that

$$ \frac{(\log x)^{1/2}}{\log _{2} x} \leqslant k \leqslant \frac{\log x}{(\log _{2} x)^{2}}, \qquad \text{with}\quad k=(\log x)^{\varrho}, $$

(4.12)

and put

$$ v:=\frac{4\log x}{\log _{2} x}, $$

(4.13)

so that \(v\geqslant 4k\) and \(Q=x^{o(1)}\). For a parameter \(U\leqslant x^{5}\), to be chosen later, let

$$\begin{aligned} \mathcal{D} ^{-}_{U}&:=\big\{ \mathbf{d}\in \mathcal{D} (n_{1}): \textstyle \prod d_{a}\leqslant U\big\} , \\ \mathcal{D} ^{+}_{U}&:=\big\{ \mathbf{d}\in \mathcal{D} (n_{1}): \textstyle \prod d_{a}>U\big\} . \end{aligned}$$

We begin with \(\mathcal{D} _{U}^{-}\). For any parameter \(\alpha > 0\) we have, by ( [4.8][110]),

$$\begin{aligned} \sum _{\mathbf{d}\in \mathcal{D} _{U}^{-}}\prod _{a}f_{a}(d_{a}) &\leqslant U^{\alpha} \sum _{\mathbf{d}\in \mathcal{D} _{U}^{-}}\prod _{a} \frac{f_{a}(d_{a})}{d_{a}^{\alpha}} \\ &\leqslant U^{\alpha} \prod _{v< p \leqslant z(2x)}\left ( 1+ \frac{k^{2}}{p^{\alpha}(p-2k)}\right ) \\ &\leqslant U^{\alpha}\exp \bigg\{ 2k^{2} \sum _{v< p \leqslant z(2x)}\frac{1}{p^{1+\alpha}}\bigg\} \\ &\leqslant U^{\alpha}\exp \bigg\{ O\bigg( \frac{k^{2}}{\alpha v^{\alpha}\log v}\bigg)\bigg\} . \end{aligned}$$

Let

$$ \alpha :=2\varrho -1+\frac{3\log _{3}x}{\log _{2}x}, $$

so that \(\frac{\log _{3} x}{\log _{2} x} \leqslant \alpha \leqslant 1\) by ( [4.12][115]). Recalling ( [4.13][116]), we see that

$$ \alpha v^{\alpha }\log v \gg \alpha (\log _{2} x)^{1-\alpha} (\log x)^{ \alpha} \gg (\log x)^{\alpha} =k^{2}(\log _{2} x)^{3}/\log x, $$

hence it follows that

$$ \sum _{\mathbf{d}\in \mathcal{D} _{U}^{-}} \prod _{a} f_{a}(d_{a}) \leqslant U^{2\varrho -1} \exp \bigg\{ O\bigg( \frac{\log x\log _{3} x}{\log _{2} x} \bigg) \bigg\} . $$

(4.14)

Next, we turn to \(\mathcal{D} _{U}^{+}\), and make use of the special structure of \(\mathcal{D} (n_{1})\). For any parameter \(\beta \in [0,1)\) we have

$$\begin{aligned} \sum _{\mathbf{d}\in \mathcal{D} _{U}^{+}}\prod _{a}f_{a}(d_{a})& \leqslant U^{-\beta} \sum _{\mathbf{d}\in \mathcal{D} (n_{1})}\prod _{a}(f_{a}(d_{a})d_{a}^{\beta}) \\ &\leqslant U^{-\beta}\sum _{ \substack{1\leqslant m\leqslant y\\m\notin \mathcal{H}-\mathcal{H}}} ~\sum _{ \substack{\mathbf{d}\in \mathcal{D} (n_{1})\\\forall a,\;d_{a}\,\mid \,(m-a)}} \prod _{a}(f_{a}(d_{a})d_{a}^{\beta}) \\ &\leqslant U^{-\beta}\sum _{ \substack{1\leqslant m\leqslant y\\m\notin \mathcal{H}-\mathcal{H}}} \prod _{a\in \mathcal{H}-\mathcal{H}}~\prod _{ \substack{p\,\mid \,m-a\\\max \{v,2|a|\}< p\leqslant z(2x)}} \bigg(1+\frac{\lambda _{a}(p)p^{\beta}}{p-2\nu _{p}}\bigg). \end{aligned}$$

Note that each prime \(p\) can appear at most once in the double product, since \(p\mid (m-a)\) and \(p\mid (m-a')\) implies \(p\mid (a-a')\), which forces \(a=a'\). We split the last product into two pieces according to whether \(p\leqslant w\) or \(p>w\), where \(w\) is a parameter to be chosen later. For any \(m\notin \mathcal{H}-\mathcal{H}\) we have

$$\begin{aligned} \prod _{a\in \mathcal{H}-\mathcal{H}}~\prod _{ \substack{p\,\mid \,m-a\\\max \{v,2|a|\}< p\leqslant w}} \bigg(1+\frac{\lambda _{a}(p) p^{\beta}}{p-2\nu _{p}}\bigg) & \leqslant \prod _{v< p\leqslant w} \left ( 1+2k p^{\beta -1}\right ) \\ &\leqslant \exp \big\{ 2k w^{\beta }\log _{2} x \big\} \end{aligned}$$

for large \(x\). We bound the contribution of larger primes trivially using the fact that any integer \(m-a\) is divisible by \(\ll \frac{\log x}{\log _{2} x}\) such primes (here, it is crucial that \(m\ne a\)). Thus, for any \(m\notin \mathcal{H}-\mathcal{H}\) we have

$$ \prod _{a\in \mathcal{H}-\mathcal{H}}~\prod _{ \substack{p\,\mid \,m-a\\\max \{w,2|a|\}< p\leqslant z(2x)}} \bigg(1+\frac{\lambda _{a}(p)p^{\beta}}{p-2\nu _{p}}\bigg) \leqslant \exp \bigg\{ O\bigg(k^{3} w^{\beta -1} \frac{\log x}{\log _{2} x}\bigg)\bigg\} . $$

We now put

$$ w:=k^{2} \log x\qquad \text{and}\qquad \beta :=\frac{1-\varrho - 2 \frac{\log _{3} x}{\log _{2} x}}{2\varrho +1}. $$

By ( [4.12][115]) we have \(\beta \geqslant 0\), and clearly \(\beta <1\). It follows that

$$ \sum _{\mathbf{d}\in \mathcal{D} _{U}^{+}} \prod _{a} f_{a}(d_{a}) \leqslant y U^{- \frac{1-\varrho}{2\varrho +1}} \exp \bigg\{ O\Big( \frac{\log x\,\log _{3} x}{\log _{2} x} \Big) \bigg\} . $$

(4.15)

Comparing ( [4.14][117]) with ( [4.15][118]), we choose \(U\) so that \(U^{2\varrho -1}=yU^{-\frac{1-\varrho}{2\varrho +1}}\), that is,

$$ U:=y^{\frac{2\varrho +1}{4\varrho ^{2}-\varrho}}. $$

Since \(1/2+o(1) \leqslant \rho \leqslant 1+o(1)\), the exponent of \(y\) is \(\leqslant 4+o(1) \leqslant 5\) for large \(x\). This gives

$$ T \leqslant y^{ \frac{4\varrho ^{2}-1}{4\varrho ^{2}-\varrho}} \exp \bigg\{ O\Big( \frac{\log x\log _{3} x}{\log _{2} x} \Big) \bigg\} . $$

Inserting this into ( [4.11][114]) yields the inequality ( [4.2][103]), and completes the proof of Proposition [4.1][101]. □

## 5 Random sieving by small primes

Throughout the sequel, we employ the notation

$$ \Theta _{z}:=\prod _{p\leqslant z}\bigg(1- \frac{1}{p}\bigg)\qquad \text{and}\qquad \Theta _{z_{1},z_{2}}:=\prod _{z_{1}< p\leqslant z_{2}} \bigg(1-\frac{1}{p}\bigg) =\frac{\Theta _{z_{2}}}{\Theta _{z_{1}}}. $$

(5.1)

Throughout this section, we assume that \(x\) and \(y\) are large real numbers that satisfy

$$ W_{y}\log y\in [\alpha (\log x)^{2},\beta (\log x)^{2}], $$

(5.2)

where \(W_{y}\) is given by ( [1.11][39]), and \(\alpha ,\beta \) are fixed with \(0<\alpha <\beta \). Note that ( [1.12][42]) and ( [5.2][119]) yield the estimates

$$ (\log x)^{2}\ll y\ll \frac{\log _{2}x}{\log _{3}x}(\log x)^{2}. $$

(5.3)

We adopt the convention that any constants implied by \(O\) and ≪ may depend on \(\alpha ,\beta \) but are independent of other parameters.

We define

$$ \mathcal{S} _{w}(y) :=[0,y] \cap \mathcal{S} _{w} $$

and when the value of \(y\) is clear from context we put

$$ S_{w}:=|\mathcal{S} _{w}(y)|. $$

Using a variety of tools, we give sharp probability bounds for \(S_{w}\) at five different “checkpoint” values \(w_{1}< w_{2}< w_{3}< w_{4}< w_{5}\) (defined below), with each \(S_{w_{i+1}}\) controlled in terms of \(S_{w_{i}}\) for \(i=1,2,3,4\). Our arguments are summarized as follows, where the range is a range of primes:

Range

 |

Estimation technique

 |

\([2,w_{1}]\)

 |

Lower bound by \(W_{y}\) ( [5.4][120])

 |

\((w_{1},w_{2}]\)

 |

Buchstab identity, sieve upper bound (Lemma [5.1][121])

 |

\((w_{2},w_{3}]\)

 |

Buchstab identity, large sieve, Bennett inequality (Lemma [5.2][122])

 |

\((w_{3},w_{4}]\)

 |

Martingale interpretation, Azuma inequality (Lemma [5.3][123])

 |

\((w_{4},w_{5}]\)

 |

Graph interpretation, combinatorial expansion (Lemma [6.1][124])

 |

\((w_{5},z]\)

 |

Combinatorial expansion (Lemmas [6.3][125], [6.5][126], Corollary [6.4][127])

 |

The most delicate part of the argument is dealing with primes \(p\) near \(\log x\), that is, \(w_{1} \leqslant p\leqslant w_{3}\) (see Lemmas [5.1][121] and [5.2][122]). To initialize the argument, we observe from definition ( [1.11][39]) of \(W_{y}\) that we have the lower bound

$$ S_{w_{1}} \geqslant W_{y}. $$

(5.4)

Now we successively increase the sieving range from \(S_{w_{1}}\) to \(S_{w_{2}}\), and so on, up to \(S_{w_{5}}\).

### Lemma 5.1

Sieving for \(w_{1} \,{<}\, p \,{\leqslant}\, w_{2}\)

*Let*\(w_{1}:=(y/\log y)^{1/2}\)*and*\(w_{2}:=\log x\,\log _{3}x\). *With probability one*, *we have*

$$ S_{w_{2}}=\bigg(1+O\bigg(\frac{\log _{4} x}{\log _{3} x}\bigg)\bigg)S_{w_{1}}. $$

### Proof

In this section and the next one, we adopt the notation \(R_{p}\) for the residue class \(a_{p}\bmod p\). From the Buchstab identity

$$ S_{w_{2}}=S_{w_{1}} - \sum _{w_{1} < p \leqslant w_{2}} | \mathcal{S} _{p-1}(y)\cap R_{p}| $$

we have

$$ S_{w_{1}}\geqslant S_{w_{2}}\geqslant S_{w_{1}}- \sum _{w_{1}< p\leqslant w_{2}}|\mathcal{S} _{w_{1}}(y) \cap R_{p}|. $$

(5.5)

The sieve upper bound (Lemma [3.1][128]) and Mertens’ theorem together imply that

$$ \sum _{w_{1}< p\leqslant w_{2}}|\mathcal{S} _{w_{1}}(y) \cap R_{p}| \ll \frac{y}{\log y}\log \Big( \frac{\log w_{2}}{\log w_{1}}\Big) =S_{w_{1}}C_{y}\log \Big( \frac{\log w_{2}}{\log w_{1}}\Big), $$

(5.6)

where

$$ C_{y}:=\frac{y}{S_{w_{1}}\log y}. $$

By ( [5.2][119]) and ( [5.3][129]) we have

$$ C_{y}\leqslant \frac{y}{W_{y}\log y}\ll \frac{\log _{2}x}{\log _{3}x}. $$

(5.7)

Using ( [5.2][119]) and the lower bound \(w_{1}^{2}=S_{w_{1}}C_{y}\geqslant W_{y}C_{y}\) we see that

$$ \log w_{1}\geqslant \log _{2}x-\tfrac{1}{2}(\log _{2}y- \log C_{y})+O(1), $$

hence

$$\begin{aligned} \log \Big(\frac{\log w_{2}}{\log w_{1}}\Big) &\leqslant \log \bigg( \frac{\log _{2}x+\log _{4}x}{\log _{2}x-\tfrac{1}{2}(\log _{2}y-\log C_{y})+O(1)}\bigg) \\ &\ll \frac{\log _{2}y-\log C_{y}}{\log _{2}x}\ll \frac{\log _{3}x-\log C_{y}}{\log _{2}x}. \end{aligned}$$

Inserting this bound into ( [5.6][130]) we find that

$$ \sum _{w_{1}< p\leqslant w_{2}}|\mathcal{S} _{w_{1}}(y) \cap R_{p}| \ll S_{w_{1}} \frac{C_{y}(\log _{3}x-\log C_{y})}{\log _{2}x}. $$

The function \(z(\log _{3} x-\log z)\) is increasing for \(z\leqslant e^{-1}\log _{2} x\), hence by ( [5.7][131]) we have

$$ \sum _{w_{1}< p\leqslant w_{2}}|\mathcal{S} _{w_{1}}(y) \cap R_{p}| \ll S_{w_{1}}\frac{\log _{4}x}{\log _{3}x} $$

and the stated result follows from ( [5.5][132]). □

### Lemma 5.2

Sieving for \(w_{2} < p \leqslant w_{3}\)

*Let*\(w_{2}:=\log x\,\log _{3}x\)*and*\(w_{3}:= \log x\,(\log _{2}x)^{2}\). *Conditional on**satisfying*\(S_{w_{2}} \geqslant \frac{1}{2} W_{y}\), *we have*

$$ \mathbb{P}_{w_{2},w_{3}}\bigg(S_{w_{3}}\leqslant \bigg(1- \frac{1}{\log _{3}x}\bigg)S_{w_{2}}\bigg) \ll x^{-100}. $$

### Proof

As in the previous lemma, we start with

$$ S_{w_{3}} \geqslant S_{w_{2}} - \sum _{w_{2}< p \leqslant w_{3}} |\mathcal{S} _{w_{2}}(y) \cap R_{p}|. $$

(5.8)

Let \(X_{p}:=|\mathcal{S} _{w_{2}}(y)\cap R_{p}|-p^{-1}S_{w_{2}}\) for each prime \(p\in (w_{2},w_{3}]\). The variables \(X_{p}\) are independent and have a mean value of zero, and by the sieve upper bound (Lemma [3.1][128]) it follows that

$$ |X_{p}|\ll \frac{y}{p\log y}\ll \frac{y}{w_{2}\log _{2}x}, $$

hence

$$ |X_{p}|\leqslant M:=\frac{c\,y}{\log x\,\log _{2}x\,\log _{3}x}\qquad (w_{2}< p \leqslant w_{3}) $$

(5.9)

for some absolute constant \(c>0\). Using Montgomery’s Large Sieve inequality (see [[12][40], Equation (9.18)] or [[27][133]]),

$$\begin{aligned} \sum _{w_{2}< p\leqslant w_{3}}p^{2}\, \mathbb{V} X_{p}&=\sum _{w_{2}< p\leqslant w_{3}}p \sum _{a\in \mathbb{Z} /p\mathbb{Z} }\bigg( \big|\mathcal{S} _{w_{2}}(y)\cap (a\bmod p)\big| -p^{-1}S_{w_{2}} \bigg)^{2} \\ &\leqslant 2w_{3}^{2}\,S_{w_{2}}, \end{aligned}$$

which implies that

$$ \sigma ^{2}:=\sum _{w_{2}< p\leqslant w_{3}} \mathbb{V} X_{p}\leqslant 2w_{2}^{-2}w_{3}^{2} \,S_{w_{2}} \ll \frac{(\log _{2}x)^{4}}{(\log _{3}x)^{2}}S_{w_{2}}. $$

(5.10)

We apply Bennett’s inequality (Lemma [3.3][23]) with \(t:=S_{w_{2}}/(2\log _{3}x)\). By ( [5.9][134]), ( [5.10][135]) and ( [5.3][129]), we have

$$ \frac{Mt}{\sigma ^{2}}\gg \frac{y}{\log x\,(\log _{2}x)^{5}} \gg \frac{\log x}{(\log _{2} x)^{5}}, $$

and therefore

$$ \frac{\sigma ^{2}}{M^{2}}\mathscr{L} \Big( \frac{Mt}{\sigma ^{2}}\Big) \gg \frac{t}{M}\log \Big( \frac{Mt}{\sigma ^{2}}\Big) \gg \frac{S_{w_{2}}\log x\,(\log _{2}x)^{2}}{y}\gg \log x\,\log _{3}x, $$

where the last bound follows from ( [1.12][42]) and our assumption that \(S_{w_{2}}\geqslant \tfrac{1}{2}W_{y}\). Lemma [3.3][23] now shows that for some constant \(c'>0\),

$$ \mathbb{P}\bigg(\bigg|\sum _{w_{2}< p\leqslant w_{3}}X_{p} \bigg|\geqslant \frac{S_{w_{2}}}{2\log _{3}x}\bigg) \leqslant 2\exp \big\{ -c'\log x\,\log _{3}x\big\} \ll x^{-100}. $$

Thus, with probability at least \(1-O(x^{-100})\) we have

$$ \sum _{w_{2}< p\leqslant w_{3}}\big| \mathcal{S} _{w_{2}}(y)\cap R_{p}\big| \leqslant S_{w_{2}} \bigg(\frac{1}{2\log _{3}x}+\sum _{w_{2}< p \leqslant w_{3}}\frac{1}{p}\bigg) \leqslant \frac{S_{w_{2}}}{\log _{3}x} $$

for sufficiently large \(x\). Recalling ( [5.8][136]), the proof is complete. □

### Lemma 5.3

Sieving for \(w_{3} < p \leqslant w_{4}\)

*Let*\(w_{3}:=\log x\,(\log _{2}x)^{2}\)*and*\(w_{4}:=y^{4/3}\). *Conditional on**satisfying*\(S_{w_{3}}\geqslant \frac{1}{4}W_{y}\), *we have*

$$ \mathbb{P}_{w_{3},w_{4}}\bigg(\big|S_{w_{4}}-\tfrac{3}{8}S_{w_{3}}\big| \geqslant \frac{S_{w_{3}}}{(\log _{2}x)^{1/2}}\bigg) \ll x^{-100}. $$

### Proof

Let \(p_{0}:=w_{3}\) and let \(p_{1} < \cdots <p_{m}\) be the primes in \((w_{3},w_{4}]\). Using the notation ( [5.1][137]), we define random variables by

$$ X_{j}:=\Theta _{w_{3},p_{j}}^{-1}S_{p_{j}}\qquad (j=0,1, \ldots ,m). $$

The sequence \(X_{0}, X_{1},\ldots ,X_{m}\) is a martingale since

Note that

$$ X_{0}=S_{w_{3}}\geqslant \tfrac{1}{4}W_{y}\gg \frac{y\log _{3}x}{(\log _{2}x)^{2}}, $$

(5.11)

where we have used ( [1.12][42]) in the last step.

We apply Azuma’s inequality (Lemma [3.2][138]). If \(p_{j+1}>y\), then \(|X_{j+1}-X_{j}|\ll 1\) since \(\Theta _{w_{3},p_{j}}^{-1}\ll 1\). In the case that \(p_{j+1} \leqslant y\), Lemma [3.1][128] shows that for any value of \(R_{p_{j+1}}\) we have

$$\begin{aligned} |X_{j+1}-X_{j}|&=\Theta _{w_{3},p_{j}}^{-1} \big|\left ( 1-p_{j+1}^{-1} \right ) ^{-1}S_{p_{j+1}}-S_{p_{j}} \big| \ll \frac{S_{p_{j+1}}}{p_{j+1}}+S_{p_{j}} - S_{p_{j+1}} \\ &=\frac{S_{p_{j+1}}}{p_{j+1}}+\big|\mathcal{S} _{p_{j}}(y) \cap R_{p_{j+1}}\big| \ll \frac{y/p_{j+1}}{1+\log (y/p_{j+1})}. \end{aligned}$$

Consequently,

$$ \sum _{j=0}^{m-1}|X_{j+1}-X_{j}|^{2} \ll \frac{y^{2}}{w_{3}\log w_{3} \log ^{2} y}+y^{4/3} \ll \frac{y^{2}}{\log x\, \log ^{5}_{2}x}. $$

Thus, if \(c>0\) is sufficiently small, then Lemma [3.2][138] shows that

$$ \mathbb{P}_{w_{3},w_{4}}\bigg(|X_{m}-X_{0}|\geqslant \frac{X_{0}}{(\log _{2}x)^{1/2}}\bigg) {\ll} \exp \biggl\{ - \frac{c\,X_{0}^{2}\log x\,(\log _{2}x)^{4}}{y^{2}}\biggr\} {\ll}\, x^{-100} $$

(5.12)

since by ( [5.11][139]) we have

$$ \frac{X_{0}^{2}\log x\,(\log _{2}x)^{4}}{y^{2}}\gg \log x\,(\log _{3}x)^{2}. $$

Using ( [5.1][137]) and ( [5.3][129]) we write

$$ \lambda :=\Theta _{w_{3},w_{4}}^{-1}=\tfrac{8}{3}(1+r_{x}) \qquad \text{with}\quad r_{x}\ll \frac{\log _{3} x}{\log _{2}x}; $$

then noting that

$$ \big|S_{w_{4}}-\tfrac{3}{8}S_{w_{3}}\big|= \big|\lambda ^{-1}X_{m}- \tfrac{3}{8}X_{0}\big|= \lambda ^{-1}|X_{m}-(1+r_{x})X_{0}|, $$

for any \(Z>0\) we have

$$ \mathbb{P}_{w_{3},w_{4}}\big(\big|S_{w_{4}}-\tfrac{3}{8}S_{w_{3}}\big| \geqslant Z\big) \leqslant \mathbb{P}_{w_{3},w_{4}} \big(\big|X_{m}-X_{0}\big|\geqslant \lambda Z-r_{x}X_{0} \big). $$

In view of ( [5.12][140]) this implies that

$$ \mathbb{P}_{w_{3},w_{4}}\big(\big|S_{w_{4}}-\tfrac{3}{8}S_{w_{3}}\big| \geqslant Z\big) \ll x^{-100} $$

holds provided that

$$ \lambda Z-r_{x}X_{0}\geqslant \frac{X_{0}}{(\log _{2}x)^{1/2}}. $$

The result follows by taking \(Z:=\frac{X_{0}}{(\log _{2} x)^{1/2}} = \frac{S_{w_{3}}}{(\log _{2} x)^{1/2}}\) and noting that \(\lambda \geqslant 2\). □

## 6 Random sieving by large primes

In this section, we adopt the notation

$$ S_{w}:=|\mathcal{S} _{w}(y)|=|[0,y] \cap \mathcal{S} _{w}| $$

from the previous section; however, we *do not*assume inequalities ( [5.2][119]) and ( [5.3][129]), except in Corollary [6.2][141] below. We do assume that \(y\) is sufficiently large. Sieving by large primes ( \(p>y^{4}\), say) is easier because there is a relatively low probability that \(\mathcal{S} \cap R_{p}\ne \varnothing \) and we are able to deploy combinatorial methods.

### Lemma 6.1

Sieving for \(w_{4} < p \leqslant w_{5}\)

*Let*\(v\)*be a real number greater than*\(w_{4}:=y^{4/3}\), *and let*\(\vartheta \in [y^{-1/4},1)\). *Conditional on *, *we have*

$$ \mathbb{P}_{w_{4},v} \Big(\big|S_{v}-\Theta _{w_{4},v}S_{w_{4}}\big| \geqslant \vartheta S_{w_{4}} \Big) \leqslant \exp \{-0.1\vartheta ^{2} S_{w_{4}}\}. $$

### Proof

Put \(\mathcal{S} :=\mathcal{S} _{w_{4}}(y)\), \(\ell :=|\mathcal{S} |=S_{w_{4}}\), and let \(\mathcal {P}\) be the set of primes in \((w_{4},v]\). The random residue classes \(\{R_{p}:p\in \mathcal {P}\}\) give rise to a bipartite graph \(\mathcal {G}\) that has vertex sets \(\mathcal{S} \) and \(\mathcal {P}\), with edges connecting the vertices \(s\in \mathcal{S} \) and \(p\in \mathcal {P}\) if and only if \(s\in R_{p}\) (i.e., \(s\equiv a_{p}\bmod p\)). Since \(0 \leqslant s\leqslant y < w_{4}\), for every \(p\) there is at most one vertex \(s\) joined to it. For any \(s\in \mathcal{S} \), let \(d(s)\) be its degree,

$$ d(s):=\big|\{p\in \mathcal {P}:s\in R_{p}\}\big|, $$

and let \(\mathcal{S} ^{+}\) be the set of vertices in \(\mathcal{S} \) of positive degree:

$$ \mathcal{S} ^{+}:=\{s\in \mathcal{S} :d(s)>0\} =\bigcup _{p\in \mathcal {P}}( \mathcal{S} \cap R_{p}). $$

Finally, we denote by \(\mathbf {d}\) the vector \(\big\langle d(s):s\in \mathcal{S} ^{+}\big\rangle \). In this manner, the random residue classes \(\{R_{p}:p\in \mathcal {P}\}\) determine a subset \(\mathcal{S} ^{+}\subset \mathcal{S} \) and a vector \(\mathbf {d}\).

For any subset \(\mathcal{T} =\{t_{1},\ldots ,t_{m}\}\) in \(\mathcal{S} \) and a vector \(\mathbf {r}=\langle r_{1},\ldots ,r_{m}\rangle \) whose entries are positive integers, let \(E(\mathcal{T} ,\mathbf {r})\) be the event that the random graph \(\mathcal {G}\) described above has \(\mathcal{S} ^{+}=\mathcal{T} \) and \(\mathbf {d}=\mathbf {r}\). Since \(\mathcal{S} \subset [0,y]\) and \(w_{4}>y\), we have \(|\mathcal{S} \cap R_{p}|\leqslant 1\) for all \(p\in \mathcal {P}\), and thus

$$ h:=r_{1}+\cdots +r_{m}=\sum _{s\in \mathcal{S} ^{+}}d(s) =\big|\{p\in \mathcal {P}: \mathcal{S} \cap R_{p}\ne \varnothing \}\big|. $$

Fixing the primes \(p_{1},\ldots ,p_{h}\in \mathcal {P}\) with \(R_{p} \cap \mathcal{S} \ne \varnothing \), there are \(\binom{h}{r_{1}\, \ldots \, r_{m}}\) ways to choose the graph’s edges connecting the \(p_{i}\) to \(\mathcal{T} \). Consequently,

$$\begin{aligned} &\mathbb{P}_{w_{4},v}(E(\mathcal{T} ,\mathbf {r})) =\sum _{ \substack{p_{1},\ldots ,p_{h}\in \mathcal {P}\\p_{1}< \cdots < p_{h}}} \frac{1}{p_{1}\cdots p_{h}} \binom{h}{r_{1}\;r_{2}\;\cdots \;r_{m}} \prod _{p\in \mathcal {P}\setminus \{p_{1},\ldots ,p_{h}\}}\bigg(1- \frac{\ell}{p}\bigg) \\ &\qquad \qquad =\binom{h}{r_{1}\;r_{2}\;\cdots \;r_{m}} \prod _{p\in \mathcal {P}}\bigg(1-\frac{\ell}{p}\bigg) \sum _{ \substack{p_{1},\ldots ,p_{h}\in \mathcal {P}\\p_{1}< \cdots < p_{h}}} \prod _{j=1}^{h} \frac{1}{p_{j}-\ell}. \end{aligned}$$

(6.1)

Relaxing the conditions on the last sum in ( [6.1][142]), we find that

$$ \mathbb{P}_{w_{4},v}(E(\mathcal{T} ,\mathbf {r})) \leqslant \frac{V U^{h}}{r_{1}!\cdots r_{m}!}\qquad \text{with}\quad V:=\prod _{p \in \mathcal {P}}\Big( 1-\frac{\ell}{p}\Big)\quad \text{and}\quad U:=\sum _{p\in \mathcal {P}}\frac{1}{p-\ell}. $$

For fixed \(m\), there are \(\binom{\ell}{m}\) choices for \(\mathcal{T} \); thus, summing over all \(r_{1},\ldots ,r_{m}\) we conclude that

$$ \mathbb{P}_{w_{4},v}(S_{w_{4}}-S_{v}=m) \leqslant V \binom{\ell}{m}(e^{U}-1)^{m}. $$

(6.2)

The complete sum over \(m\) of the right side of ( [6.2][143]) is equal to \(V e^{U\ell}\), and the peak occurs when \(m=(1-e^{-U})\ell +O(1)\). We also have

$$ 1-e^{-U}=1-\Theta _{w_{4},v}\bigg( 1+O\bigg( \frac{\ell}{w_{4}\log w_{4}}\bigg)\bigg), $$

(6.3)

Standard large-deviation results for the binomial distribution (such as Lemma [3.2][138]) imply that for any \(\delta >0\),

$$ e^{-U\ell} \sum _{|m-(1-e^{-U}) \ell | \geqslant \delta \ell} \binom{\ell}{m} (e^{U}-1)^{m} \leqslant 2 e^{- \delta ^{2} \ell /2}. $$

Recalling that \(\ell :=S_{w_{4}}\), we see that the inequality

$$ \big|S_{v}-\Theta _{w_{4},v}\ell |\geqslant \vartheta \ell $$

implies via ( [6.3][144]) that

$$\begin{aligned} |m-{(1-e^{-U})} \ell | &\geqslant \vartheta \ell - |e^{-U}-\,\Theta _{w_{4},v}|\ell \geqslant \vartheta \ell - O(y^{-1/3}\ell ) \geqslant \vartheta \ell /2 \end{aligned}$$

for all large \(x\) since \({w_{4}}:=y^{4/3}\) and \(\ell \leqslant y\). Combining our results above, we conclude that

$$ \begin{aligned} \mathbb{P}_{w_{4},v}\left ( \big|S_{v}-\Theta _{w_{4},v} \ell \big|\geqslant \vartheta \ell \right ) &\ll{V e^{U\ell } e^{-\vartheta ^{2} \ell /8}} \\ &\ll{e^{-\vartheta ^{2}\ell /8+O(\ell ^{2}/w_{4})}} \\ &\leqslant e^{-\vartheta ^{2}\ell /10} \end{aligned} $$

for all large \(x\), and the proof is complete. □

Combining Lemmas [5.1][121], [5.2][122], [5.3][123] and [6.1][124] (with \(v:=y^{8}\) and \(\vartheta :=y^{-1/10}\)) we obtain the following result.

### Corollary 6.2

Sieving for \(w_{1} < p \leqslant w_{5}\)

*Assume*( [5.2][119]), *let*\(w_{1}:=(y/\log y)^{1/2}\)*and*\(w_{5}:=y^{8}\). *Conditional on*, *we have with probability*\(1-O(x^{-100})\)*that*

$$ \left |S_{w_{5}}-\frac{S_{w_{1}}}{16}\right |\ll _{\alpha ,\beta} \frac{\log _{4} x}{\log _{3} x}S_{w_{1}}. $$

Our next result is a very general tool for handling primes larger than \(y^{4}\).

### Lemma 6.3

Sieving for \(w_{5} < p \leqslant z\), I

*Let*\(w\geqslant y^{4}\)*and*\(\mathcal {P}\)*be a set of primes larger than*\(w\)*such that*\(\sum _{p\in \mathcal {P}} 1/p \geqslant 1/10\). *Let*\(\mathcal{S} \subseteq \mathcal{S} _{w}\)*with*\(|\mathcal{S} | \leqslant 10y\), *and such that for all*\(p\in \mathcal {P}\), \(\mathcal{S} \)*is distinct modulo*\(p\). *Conditional on*, *we have for all*\(0\leqslant g\leqslant | \mathcal{S} |\):

$$ \mathbb{P}_{\mathcal {P}}\left ( \Big|\mathcal{S}\setminus \bigcup _{p\in \mathcal {P}} R_{p}\Big|=g\right ) = (1- \Theta )^{|\mathcal{S} |-g}\Theta ^{g} \binom{|\mathcal{S} |}{g}(1+O(y^{2}/w)), $$

*where*

$$ \Theta :=\prod _{p\in \mathcal {P}} (1-1/p). $$

### Proof

Put \(\ell :=|\mathcal{S} |\), and assume that \(\ell \geqslant 1\) (the case \(\ell :=0\) being trivial). Take \(m:=\ell -g\), and let \(\mathcal{T} \), \(\mathbf {r}\), \(E(\mathcal{T} ,\mathbf {r})\) and \(h\) be defined as in Lemma [6.1][124] with \(|\mathcal{T} |=m=\ell -g\). As before (see ( [6.1][142])) we have

$$ \mathbb{P}_{\mathcal {P}}(E(\mathcal{T} ,\mathbf {r})) = \binom{h}{r_{1}\;r_{2}\;\cdots \;r_{m}} \prod _{p\in \mathcal {P}}\bigg(1- \frac{\ell}{p}\bigg) \sum _{ \substack{p_{1},\ldots ,p_{h}\in \mathcal {P}\\p_{1}< \cdots < p_{h}}} \prod _{j=1}^{h} \frac{1}{p_{j}-\ell}. $$

(6.4)

For any prime \(p\in \mathcal {P}\) the elements of \(\mathcal{S} \) lie in distinct residue classes modulo \(p\); this implies that \(\mathbb{P}_{\mathcal {P}}(E(\mathcal{T} ,\mathbf {r}))\) can only be nonzero when \(m=h\) in ( [6.4][145]) (that is, every \(r_{j}:=1\)). Let \(T_{h}\) be the sum over \(p_{1},\ldots ,p_{h}\) in ( [6.4][145]). Then

$$ \begin{aligned} T_{h}&=\frac{1}{h!}\bigg(\sum _{p\in \mathcal{P}}\frac{1}{p-\ell }{+O \left (\frac{h}{w}\right )}\bigg)^{h} \\ &=\frac{1}{h!}\bigg(\sum _{p\in \mathcal{P}}\frac{1}{p} +O\bigg( \frac{\ell }{{w}}\bigg)\bigg)^{h} \\ &=\frac{(-\log \Theta +O(y/w))^{h}}{h!}. \end{aligned} $$

Also, note that

$$ V:=\prod _{p\in \mathcal {P}}\Big(1-\frac{\ell}{p}\Big)= \Theta ^{\ell}(1+O(y^{2}/w)). $$

Hence, summing over all vectors \(\mathbf {r}\), we find that

$$\begin{aligned} &{ \mathbb{P}_{\mathcal {P}}\big(\big| \mathcal{S} \setminus \cup _{p \in \mathcal {P}} R_{p} \big|=\ell -m \big)} \\ &\qquad = \sum _{ \substack{\mathcal{T} \subset \mathcal{S} \\|\mathcal{T} |=m}} \sum _{h} \sum _{r_{1}+\cdots +r_{m}=h} \binom{h}{r_{1} \, \ldots \, r_{m}} V T_{h} \\ &\qquad =(1+O(y^{2}/w))\Theta ^{\ell }\sum _{ \substack{\mathcal{T} \subset \mathcal{S} \\|\mathcal{T} |=m}} \sum _{r_{1},\ldots ,r_{m}\geqslant 1} \frac{(-\log \Theta +O(y/w))^{r_{1}+\cdots +r_{m}}}{r_{1}! \cdots r_{m}!} \\ &\qquad =(1+O(y^{2}/w))\binom{\ell}{m}\Theta ^{\ell }\big(e^{-\log \Theta +O(y/w)}-1 \big)^{m} \\ &\qquad =(1+O(y^{2}/w))\binom{\ell}{m}\Theta ^{\ell }\big(\Theta ^{-1}-1 \big)^{\ell -g}. \end{aligned}$$

This completes the proof. □

### Corollary 6.4

Sieving for \(w_{5} < p \leqslant z\), II

*Uniformly for*\(z^{1/2} \geqslant w \geqslant y^{4}\), *we have*

$$ \mathbb{E}_{w,z} \binom{S_{z}}{k}=\Theta _{w,z}^{k}\binom{S_{w}}{k}(1+O(y^{2}/w)). $$

### Proof

Let \(\Theta :=\Theta _{w,z}\). By Lemma [6.3][125] with \(\mathcal{S} :=\mathcal{S} _{w}\cap [0,y]\) and \(\mathcal {P}\) the set of primes in \((w,z]\), we have

$$\begin{aligned} \mathbb{E}_{w,z}\binom{S_{z}}{k}&=(1+O(y^{2}/w))\sum _{g=k}^{S_{w}} (1- \Theta )^{S_{w}-g}\Theta ^{g} \binom{S_{w}}{g}\binom{g}{k} \\ &=(1+O(y^{2}/w))\Theta ^{k}\binom{S_{w}}{k}\sum _{j=0}^{S_{w}-k} (1- \Theta )^{S_{w}-k-j}\Theta ^{j} \binom{S_{w}-k}{S_{w}-k-j} \\ &=(1+O(y^{2}/w))\Theta ^{k}\binom{S_{w}}{k}. \end{aligned}$$

□

The next lemma has a weaker conclusion than Lemma [6.3][125] but is more general and is needed for a second moment argument below in which we derive a lower bound for the largest prime gap in \([0,x]\).

### Lemma 6.5

Sieving for \(w_{5} < p \leqslant z\), III

*Let*\(w\)*and*\(z\)*be real numbers for which*\(z^{1/2}\geqslant w\geqslant y^{8}\). *Let*\(\mathcal{S} \subset \mathcal{S} _{w} \cap [0,e^{y}]\)*with*\(|\mathcal{S} |\leqslant y\)*and such that for every prime*\(p>w\), *no more than two numbers in*\(\mathcal{S} \)*lie in any given residue class modulo*\(p\). *Then*

$$ \mathbb{P}_{w,z}\bigg(\mathcal{S} \cap \mathcal{S} _{z}= \varnothing \bigg)= (1-\Theta _{w,z})^{|\mathcal{S} |}(1+O(y^{4}/w)). $$

### Proof

Put \(\ell :=|\mathcal{S} |\), and let \(\mathcal {P}\) be the set of primes in \((w,z]\), and put

$$ \mathcal{Q} :=\big\{ p \in \mathcal {P}:p\mid s-s'~\text{for some}~s,s'\in \mathcal{S} , s\ne s'\big\} . $$

Note that the bound

$$ {|\mathcal{Q} |\leqslant \frac{\ell ^{2} y}{\log w} \leqslant y^{3}} $$

(6.5)

holds if \(y\) is large enough.

By assumption, for every \(p\in \mathcal{Q} \), \(| \mathcal{S} \cap R_{p}| \leqslant 2\). Let \(E_{m}\) be the event that for \(\mathcal{S} \cap R_{p}\ne \varnothing \) holds for precisely \(m\) primes \(p\in \mathcal{Q} \). Since for any prime \(p\in \mathcal {P}\) the probability that \(\mathcal{S} \cap R_{p}\ne \varnothing \) does not exceed \(\ell /p\), using ( [6.5][146]) we have

$$ \mathbb{P}_{\mathcal{Q} }(E_{m})\leqslant \frac{1}{m!} \bigg(\sum _{p\in \mathcal{Q} } \frac{\ell}{p}\bigg)^{m} \leqslant \left ( \frac{e\ell |\mathcal{Q} |}{mw}\right )^{m} \leqslant {(ey^{4}/w)^{m}}\qquad (m \geqslant 1). $$

(6.6)

Assume the event \(E_{m}\) occurs, and fix . If \(\mathcal{S} \) has precisely \(n\) elements covered by \(\bigcup _{p\in \mathcal{Q} }R_{p}\), then \(0\leqslant n\leqslant 2m\), the upper bound being a consequence of our hypothesis on \(\mathcal{S} \). Put

$$ \mathcal{S} ':=\big\{ s \in \mathcal{S} :s\notin R_{p}~\text{for all}~p\in \mathcal{Q} \big\} , $$

so that \(|\mathcal{S} '|=\ell -n\). Lemma [6.3][125] implies that

$$\begin{aligned} \mathbb{P}_{\mathcal {P}\setminus \mathcal{Q} } \bigg( \mathcal{S} '\subset \bigcup _{p\in \mathcal {P}\setminus \mathcal{Q} }R_{p}\bigg) &=(1+O(y^{2}/w))\Big(1-\Theta _{w,z} \prod _{p\in \mathcal{Q} }\big(1-p^{-1}\big)^{-1}\Big)^{ \ell -n} \\ &=(1+O(y^{4}/w))\Big(1-\Theta _{w,z}\Big)^{\ell -n} \\ &\ll \Big(1-\Theta _{w,z}\Big)^{\ell -2m}, \end{aligned}$$

since

$$ \prod _{p\in \mathcal{Q} }\big(1-p^{-1}\big)^{-1}=1+O(| \mathcal{Q} |/w)=1+O(y^{3}/w) $$

by ( [6.5][146]). Now \(\mathbb{P}_{\mathcal{Q} }(E_{0})=1-O(y^{4}/w)\) by ( [6.6][147]), so we conclude that

$$\begin{aligned} &\mathbb{P}_{w,z}\bigg(\mathcal{S} \subset \bigcup _{p\in \mathcal {P}}R_{p} \bigg) =\sum _{m=0}^{|\mathcal{Q} |}\mathbb{P}_{ \mathcal{Q} }(E_{m}) \cdot \mathbb{E}_{\mathcal{Q} } \bigg(\mathbb{P}_{\mathcal {P}\setminus \mathcal{Q} }\bigg( \mathcal{S} '\subset \bigcup _{p\in \mathcal {P}\setminus \mathcal{Q} }R_{p}\bigg)\Big|E_{m}\bigg) \\ &\qquad =(1+O(y^{4}/w))\big(1-\Theta _{w,z}\big)^{\ell }+O\bigg(\sum _{m \geqslant 1}{(ey^{4}/w)^{m}} \big(1-\Theta _{w,z} \big)^{\ell -2m}\bigg) \\ &\qquad =(1+O(y^{4}/w))\big(1-\Theta _{w,z}\big)^{\ell}. \end{aligned}$$

This completes the proof. □

## 7 The behavior of the largest gap

In this section we use the estimates from the previous section to complete the proof of Theorem [1.1][19]. In Theorems [7.1][148] and [7.2][149] below, we suppose that

$$ \varepsilon =\varepsilon (x):={ \frac{1}{(\log _{3} x)^{1/3}}}. $$

(7.1)

We also note that

$$ u < W_{g(u)+1}\log (g(u)+1) \leqslant (W_{g(u)}+1)\log (g(u)+1), $$

and hence

$$ W_{g(u)} \log g(u)=u+O(\log u). $$

(7.2)

### Theorem 7.1

Probabilistic upper bound for gap

*For large*\(x\),

### Theorem 7.2

Probabilistic lower bound for gap

*If*\(x\)*is large then*

### Proof of Theorem [7.1][148]

Let \(y:=g((1+\varepsilon )\xi (\log \tfrac{x}{2})^{2})\), so that by ( [7.2][150]) we have

$$ W_{y} \log y=(1+\varepsilon )\xi (\log x)^{2}+O(\log x). $$

(7.3)

We also have by ( [1.12][42]) the bounds

$$ \log ^{2} x \ll y \ll (\log ^{2} x)\log _{2} x. $$

Let \(z:=z(x)\). The probability that has a gap of size \(\geqslant y\) does not exceed the probability that \(\mathcal{S} _{z}\cap [0,x]\) has a gap of size \(\geqslant y\), which in turn is at most

$$ \mathbb{E}\big|\{n\leqslant x:[n,n+y]\cap \mathcal{S} _{z}=\varnothing \}\big| \leqslant x\cdot \mathbb{P}(\mathcal{S} _{z}=0). $$

Let \(w_{1}:=(y/\log y)^{1/2}\) and \(w_{5}:=y^{8}\) as before. Also put \(\eta :=\frac{\log _{4} x}{\log _{3} x}\). Applying Corollary [6.2][141] together with ( [7.3][151]), it follows that with probability \(1-O(x^{-100})\) we have

$$ \begin{aligned} S_{w_{5}}&=(1+O(\eta ))\frac{S_{w_{1}}}{16} \geqslant (1+O( \eta ))\frac{W_{y}}{16} \\ &\geqslant \frac{(1+\varepsilon +O(\eta ))\,\xi (\log x)^{2}}{32\log _{2}x} \\ &\geqslant \frac{(1+2\varepsilon /3)\,\xi (\log x)^{2}}{32\log _{2}x} \end{aligned} $$

using ( [7.1][152]) in the final step. Fix so that \(S_{w_{5}}\) satisfies this inequality. Taking into account that

$$ \Theta _{w_{5},z}=\frac{32\log _{2}x}{\xi \log x}\left ( 1+O \left (\frac{1}{\log _{2} x}\right )\right ) , $$

Lemma [6.3][125] now shows that

$$ \mathbb{P}_{w_{5},z}(S_{z}=0)\ll (1-\Theta _{w_{5},z})^{{S_{w_{5}}}} \ll x^{-1-\varepsilon /2}, $$

as required. □

### Proof of Theorem [7.2][149]

Set \(y:=g((1-\varepsilon )\xi (\log 2x)^{2})\), so that

$$ W_{y} \log y=(1-\varepsilon )\xi \log ^{2} x+O(\log x). $$

(7.4)

Again, ( [1.12][42]) implies that

$$ \log ^{2} x \ll y \ll (\log ^{2} x) \frac{\log _{2} x}{\log _{3} x}. $$

Let \(z:=z(x/2)\), \(w_{1}:=(y/\log y)^{1/2}\), \(w_{5}:=y^{8}\) and \(\eta :=\frac{\log _{4} x}{\log _{3} x}\). In particular, \(z\sim (x/2)^{1/e^{\gamma}}\) by ( [1.7][100]), and

$$ w_{1} \ll \frac{\log x}{(\log _{3} x)^{1/2}}. $$

(7.5)

It suffices to show that with high probability, \(\mathcal{S} _{z}\cap (x/2,x]\) has a gap of size \(\geqslant y\), for this implies that has a gap of size \(\geqslant y\) within \([0,x]\). For the sake of brevity we write

$$ \mathcal{F} (u,v) :=[u,u+y] \setminus \bigcup _{p\leqslant v} R_{p}, \qquad F(u,v) :=|\mathcal{F} (u,v)|. $$

That is, \(F(u,v)\) counts the number of elements in \([u,u+y]\) sieved by the primes \(\leqslant v\). In particular, \(S_{w}=F(0,w)\). There is some vector \((b_{p})_{p\in w_{1}}\) so that there are exactly \(W_{y}\) integers in \([0,y]\) that avoid the residue classes \((b_{p} \bmod p)_{p\leqslant w_{1}}\). Setting

$$ Q:=\prod _{p\leqslant w_{1}}p, $$

for any , there is a progression \(b\bmod Q\) such that

$$ F(u,w_{1})=W_{y} \qquad \text{whenever}\quad u\equiv b\bmod Q. $$

Specifically, choose \(b\) such that \(b\equiv a_{p}-b_{p}\bmod p\) for all primes \(p\leqslant w_{1}\). Let \(\mathcal{U} \) be the set of integers \(u\equiv b\bmod Q\) such that \([u,u+y]\subset (x/2,x]\). We show that with high probability, \(F(u,z)=0\) for at least one \(u\in \mathcal{U} \).

By Corollary [6.2][141], with probability at least \(1-O(x^{-100})\), we have for any given \(u\in \mathcal{U} \) the bound

$$ F(u,w_{5})=(\tfrac{1}{16}+O(\eta )) F(u,w_{1})=(\tfrac{1}{16}+O(\eta )) W_{y}. $$

(7.6)

Let \(E\) be the event that this bound holds for *every*\(u\in \mathcal{U} \). By the union bound, \(\mathbb{P}_{w_{1},w_{5}}(E)\geqslant 1-O(x^{-99})\). Conditioning on \(E\), we denote

$$ \mathcal{U} _{r}:=\{u\in \mathcal{U} :F(u,w_{5})=r \}\qquad (r \geqslant 0). $$

The sets \(\mathcal{U} _{r}\) depend only on , and \(\mathcal{U} _{r}=\varnothing \) unless \(r=(\tfrac{1}{16}+O(\eta ))W_{y}\) by ( [7.6][153]). Rather than work with all \(r\), we focus on a popular value of \(r\); thus, let \(\ell \) be fixed with the property that \(|\mathcal{U} _{\ell}|\geqslant | \mathcal{U} _{r}|\) for all \(r\). By ( [7.5][154]), we have

$$ |\mathcal{U} _{\ell}|\gg \frac{|\mathcal{U} |}{\eta W_{y}} \gg \frac{x}{QW_{y}} =x e^{-O(w_{1})}\gg x^{1-O((\log _{3} x)^{-1/2})}. $$

(7.7)

Combining ( [7.4][155]) with ( [7.6][153]) and ( [7.1][152]), we have

$$ \ell \leqslant (\tfrac{1}{16}+O(\eta ))W_{y} \leqslant \frac{(1-(2/3)\varepsilon )\xi (\log x)^{2}}{32\log _{2}x}. $$

(7.8)

Next, let

$$ M:=\big|\{u\in \mathcal{U} _{\ell}:F(u,z)=0 \}\big|, $$

which counts those intervals indexed by \(u\in \mathcal{U} _{\ell}\) for which \(\mathcal{F} (u,w_{5})\) is covered by \(\bigcup _{w_{5}< p\leqslant z} R_{p}\). We analyze \(M\) using first and second moments. Firstly, by Lemma [6.3][125],

$$ \mathbb{E}_{w_{5},z}M=\sum _{u\in \mathcal{U} _{\ell}} \mathbb{P}_{w_{5},z}(F(u,z)=0) =|\mathcal{U} _{\ell}|(1-\Theta )^{\ell}(1+O(y^{2}/w_{5})), $$

where

$$ \Theta :=\Theta _{w_{5},z}= \frac{32\log _{2}x}{\xi \log x} \left ( 1+O\left ( \frac{1}{\log _{2} x}\right )\right ) . $$

(7.9)

To bound the second moment of \(M\), apply Lemma [6.5][126] with \(\mathcal{S} :=\mathcal{F} (u,w_{5}) \cup \mathcal{F} (u',w_{5})\), where \(u\) and \(u'\) are distinct elements of \(\mathcal{U} _{\ell}\). The hypotheses of Lemma [6.5][126] are satisfied as any prime \(p>w_{5}>y\) can divide at most two elements of \(\mathcal{S} \). We obtain

$$\begin{aligned} \mathbb{E}_{w_{5},z} M^{2} &=\mathbb{E}_{w_{5},z} M+\sum _{ \substack{u,u'\in \mathcal{U} _{\ell }\\ u \ne u'}} \mathbb{P}_{w_{5},z} \left ( F(u,z)=F(u',z)=0 \right ) \\ &=|\mathcal{U} _{\ell}|^{2}(1-\Theta )^{2\ell} (1+O(y^{4}/w_{5}))+O \big(|\mathcal{U} _{\ell}|(1-\Theta )^{\ell}\big). \end{aligned}$$

By ( [7.7][156]), ( [7.8][157]) and ( [7.9][158]) we have

$$ |\mathcal{U} _{\ell}|(1-\Theta )^{\ell} \geqslant x^{2\varepsilon /3 - O((\log _{3} x)^{-1/2})} \geqslant x^{\varepsilon /2} $$

for large \(x\), and hence we bound the variance by

$$ \sigma ^{2}:=\mathbb{V} _{w_{5},z}M= \mathbb{E}_{w_{5},z} M^{2}-(\mathbb{E}_{w_{5},z} M)^{2} \ll |\mathcal{U} _{\ell}|^{2}(1- \Theta )^{2\ell}y^{4}/w_{5}. $$

Thus, Chebyshev’s inequality implies

$$ \mathbb{P}_{w_{5},z} \left ( M \geqslant \tfrac{1}{2} | \mathcal{U} _{\ell}| (1-\Theta )^{\ell } \right ) \geqslant 1-O(y^{4}/w_{5})=1-O(1/y^{4}). $$

In particular, with probability at least \(1-O(y^{-4})=1-O((\log x)^{-8})\) there is an interval \([u,u+y]\) in \((x/2,x]\) completely sieved out by . □

### Proof of Theorem [1.1][19]

Let \(x_{j}:=2^{j}\) vary over positive integers \(j\), and let \(\varepsilon >0\) be fixed. Theorem [7.1][148] implies that for large \(j\) we have

The convergence of \(\sum _{j} x_{j}^{-\varepsilon /2}\) implies, via the Borel-Cantelli lemma, that almost surely there is a \(J\) so that

As and \(g\) are both increasing functions, the above relation implies that for all \(x_{j-1} < x \leqslant x_{j}\) and \(j>J\) we have

In a similar manner, Theorem [7.2][149] and Borel-Cantelli imply that almost surely there is a \(J\) so that

As before, this implies that

□

## 8 Large gaps from Hardy-Littlewood

To prove Theorems [1.5][51] and [1.6][61], we start with a simple inclusion-exclusion result (a special case of the Bonferroni inequalities or the “Brun pure sieve”).

### Lemma 8.1

Brun’s sieve

*Suppose that*\(y \geqslant 1\), *let**be sets of positive integers*, *and put*

*and*

*Then*, *for any even*\(K\)*we have*\(T\leqslant U_{K}\), *and for any odd*\(K\)*we have*\(T\geqslant U_{K}\).

### Proof

For any integers \(K,m\geqslant 0\) let

$$ \delta _{K}(m):=\sum _{k=0}^{K}(-1)^{k} \binom{m}{k}\qquad \text{and}\qquad \delta (m):=\textstyle\begin{cases} 1&\quad \text{if $m=0$}, \\ 0&\quad \text{if $m\geqslant 1$}. \end{cases} $$

Observe that

$$ \delta (m)\leqslant \delta _{K}(m)\quad \text{($K$ even)}\qquad \text{and}\qquad \delta (m) \geqslant \delta _{K}(m)\quad \text{($K$ odd)}; $$

hence, taking we have

$$ T=\sum _{n\in \mathcal{N} }\delta (A(n))=\sum _{n\in \mathcal{N} } \delta _{K}(A(n))+\theta , $$

where \(\theta \geqslant 0\) if \(K\) is even and \(\theta \leqslant 0\) if \(K\) is odd. Also,

$$ \sum _{n\in \mathcal{N} } \delta _{K}(A(n)) =\sum _{k=0}^{K}(-1)^{k} \sum _{n\in \mathcal{N} }\binom{A(n)}{k}=U_{K} $$

since

and the lemma is proved. □

### Proof of Theorem [1.5][51]

Although Theorem [1.5][51] concerns the behavior of a specific set , our first task is to express the gap-counting function for in terms of the random quantities with which we have been working in the past few sections.

First, observe that ( [1.17][67]) with \(\mathcal{H}=\{0\}\) implies that

and it follows trivially that . Therefore, by adjusting the implied constant in the conclusion of the theorem, we may assume that

$$ \kappa \geqslant D \frac{\log _{2} x}{\log x} $$

(8.1)

for a sufficiently large constant \(D\).

Let \(x\) be a large real number, put \(\mathcal{N} :=[x/2,x]\) and let \(y,K\) be integer parameters to be chosen later, with \(K\) odd and with \(K\leqslant \frac{\kappa \log x}{2\log _{2} x}\). Define \(T\) and \(U_{K}\) as in Lemma [8.1][159]. Since \(T\geqslant U_{K}\) by Lemma [8.1][159], our aim is to show that \(U_{K}\geqslant 1\). Using ( [1.17][67]) we see that

$$ U_{K}=\sum _{k=0}^{K}(-1)^{k}\intop \nolimits _{x/2}^{x} \frac{1}{(\log t)^{k}} \sum _{\substack{\mathcal{H}\subset [0,y]\\|\mathcal{H}|=k}} \mathfrak{S} (\mathcal{H})\,dt+O(E), $$

where

$$ E:=Kx^{1-\kappa}\binom{y+1}{K}. $$

By Lemma [3.5][107], replacing \(\mathfrak{S} (\mathcal{H})/\log ^{k} t\) with \(V_{\mathcal{H}}(z(t))\) induces an additive error of size \(O(E)\) since \(\kappa \leqslant 1/2\). Also, ( [1.8][160]) implies that

$$ \sum _{\substack{\mathcal{H}\subset [0,y]\\|\mathcal{H}|=k}}V_{\mathcal{H}}(z(t)) =\mathbb{E}_{z(t)} \binom{S_{z(t)}}{k}, $$

and we get

$$ U_{K}=\intop \nolimits _{x/2}^{x}\mathbb{E}_{z(t)}\sum _{k=0}^{K}(-1)^{k} \binom{S_{z(t)}}{k}\, dt+O(E). $$

Since \(K\) is odd, the sum on \(k\) is a lower bound for \(\mathbb{P}(S_{z(t)}=0)\); adding the term \(k=K+1\) switches the inequality (cf. the proof of Lemma [8.1][159]) and thus

$$ U_{K} \geqslant \intop \nolimits _{x/2}^{x} \mathbb{P}(S_{z(t)}=0) - \mathbb{E}_{z(t)}\binom{S_{z(t)}}{K+1}\, dt+O(E). $$

(8.2)

Let

$$ w:=y^{4},\qquad z:=z(x/2). $$

The upper bound sieve (Lemma [3.1][128]) implies the crude bound \(S_{w} \leqslant Cy/\log y\) for some absolute constant \(C\). We now put

$$ y:=\frac{\kappa \,\xi \log ^{2} x}{400 C \log _{2}x} \qquad \text{and} \qquad K:=2{ \left \lfloor \frac{100 C y}{\log x} \right \rfloor } -1. $$

(8.3)

With these choices, \(K \leqslant \frac{\kappa \log x}{2\log _{2} x}\) and, using ( [8.1][161]), we have

$$ y \geqslant \frac{D}{400C}\log x. $$

(8.4)

It also follows that

$$ E \ll x^{1-\kappa} (\log x)^{K} \ll x^{1-\kappa +\kappa \,\xi /2}\ll x^{1- \kappa /3} $$

for all large \(x\). Corollary [6.4][127] and the crude bound \(\Theta _{w,z} \leqslant 8\frac{\log y}{\log x}\) imply that

$$ \begin{aligned} \mathbb{E}_{z(t)}\binom{S_{z(t)}}{K+1} &\leqslant \mathbb{E}_{z}\binom{S_{z}}{K+1} \\ &\ll \Theta _{w,z}^{K+1} \mathbb{E}_{w} \binom{S_{w}}{K+1} \\ &\ll \left ( \Theta _{w,z} \frac{eCy}{K\log y} \right ) ^{K+1} \\ &\ll e^{-K} \ll e^{-200Cy/\log x}, \end{aligned} $$

where we used ( [8.3][162]) in the last step. It remains to show that \(\mathbb{P}_{z(t)}(S_{z(t)}=0)\) is substantially larger. Lemma [6.3][125] implies immediately that

$$ \begin{aligned} \mathbb{P}_{z}(S_{z(t)}=0) &\geqslant \mathbb{P}_{z} (S_{z}=0) \gg (1-\Theta _{w,z})^{S_{w}} \\ &\gg e^{-\Theta _{w,z} (Cy/\log y)} \geqslant e^{-8C y/ \log x}, \end{aligned} $$

as required. Combining these estimates with ( [8.2][163]) gives

$$ U_{K} \gg x e^{-8C y/\log x}+O(xe^{-200Cy/\log x}+x^{1-c/3}) \gg x e^{-8C y/\log x}, $$

the last inequality following from ( [8.4][164]), the fact that \(D\) is sufficiently large, and that \(y/\log x \ll \kappa /\log _{2} x\). This completes the proof of Theorem [1.5][51]. □

### Proof of Theorem [1.6][61]

Let \(x\) be large, let \(\varepsilon >0\), and let \(y:=g((1-\varepsilon )c\,\xi \log ^{2} x)\). By ( [7.2][150]),

$$ W_{y} \log y=(1-\varepsilon )c\,\xi \log ^{2} x+O_{c}(\log _{2} x). $$

(8.5)

In particular, ( [5.2][119]) holds, with \(\alpha ,\beta \) depending on \(c\). Also, from ( [1.12][42]) we have

$$ (c/2) \log ^{2} x \leqslant y=o((\log ^{2} x)\log _{2} x). $$

(8.6)

Let

$$ w_{1} :=(y/\log y)^{1/2}, \qquad w_{5}:=y^{8}, \qquad z:=z(x/2). $$

Again, let \(\mathcal{N} :=(x/2,x]\), and define \(C\) as in the previous proof. We apply Lemma [8.1][159] with

$$ K:=2{ \left \lfloor \frac{100Cy}{\log x} \right \rfloor } -1, $$

so that \(K\leqslant \frac{200 C y}{\log x}\). Similarly to ( [8.2][163]) we get that

$$ U_{K} \geqslant \intop \nolimits _{x/2}^{x} \mathbb{P}(S_{z(t)}=0) - \mathbb{E}_{z(t)}\binom{S_{z(t)}}{K+1}\, dt+O(E), $$

(8.7)

where, because the function \(\mathfrak{S} _{z(t)}(\mathcal{H})\) appears already in ( [1.18][69]), as does the averaging over ℋ, we have

$$ E \ll K x^{1-c} \ll x^{1-c}\log ^{2} x. $$

(8.8)

By the same reasoning as in the proof of Theorem [1.5][51], we get that

$$ \mathbb{E}_{z(t)}\binom{S_{z(t)}}{K+1} \ll e^{-K} \ll x^{-10c}, $$

(8.9)

where we used ( [8.6][165]) in the last step.

Let \(w:=y^{8}\) and fix . By Lemma [6.3][125] we have

$$ \mathbb{P}_{w,z}(S_{z}=0)=(1-\Theta _{w,z})^{S_{w}}(1+O(y^{-6})). $$

(8.10)

Now put \(w_{1}:=(y/\log y)^{1/2}\), and let be fixed such that \(S_{w_{1}}=W_{y}\). This occurs with probability \(\geqslant x^{-o(1)}\), since \((y/\log y)^{1/2}=o(\log x)\) by ( [8.6][165]). Conditional on , Corollary [6.2][141] implies that with probability at least \(1-O(x^{-100})\) we have

$$ S_{w}=(\tfrac{1}{16}+O(\eta ))S_{w_{1}}=(\tfrac{1}{16}+O(\eta ))W_{y}, $$

where \(\eta :=\frac{\log _{4} x}{\log _{3} x}\) as before and the implied constants may depend on \(c\). Now fix \(w\) such that the above holds. Since

$$ \Theta _{w,z}=(1+O(\eta )) \frac{16\log y}{\xi \log x}, $$

( [8.5][166]) implies that

$$ \Theta _{w,z}S_{w}=(1+O(\eta )) (1-\varepsilon ) c \log x, $$

where we have used ( [8.5][166]) in the last step. Inserting this last estimate into ( [8.10][167]), we conclude that

$$ \mathbb{P}_{z}(S_{z}=0) \gg e^{-(1+O(\eta ))(1-\varepsilon )c\log x} \gg x^{-(1- \varepsilon /2)c} $$

(8.11)

In particular, the right side of ( [8.11][168]) has larger order than the right sides in ( [8.8][169]) and ( [8.9][170]). Thus, inserting ( [8.8][169]), ( [8.9][170]) and ( [8.11][168]) into ( [8.7][171]), we conclude that \(U_{K}\geqslant 1\) if \(x\) is sufficiently large depending on \(\varepsilon \). By a simple diagonalization argument, the same claim then holds for some \(\varepsilon =\varepsilon (x)=o(1)\) going to zero sufficiently slowly as \(x \to \infty \). This completes the proof of Theorem [1.6][61]. □

## 9 The influence of exceptional zeros

In this section, we show that the existence of exceptional zeros implies that \(W_{y}\) is rather smaller than the upper bound in ( [1.12][42]) infinitely often.

### Theorem 9.1

*Let*\(q\in \mathbb{N} \), *and suppose that there is a real Dirichlet character*\(\chi _{q}\)*mod*\(q\)*such that*\(L(1-\delta _{q},\chi _{q})=0\)*and*\(0<\delta _{q} \leqslant \frac{c}{\log q}\), *where*\(c:=1/11^{2}\). *For*

$$ y:=\exp \bigg\{ \left (\frac{\log q}{\delta _{q}} \right )^{1/2} \bigg\} $$

(9.1)

*we have*

$$ W_{y} \ll \delta _{q} y {=\frac{y\log q}{\log ^{2} y}. } $$

### Proof

Denote by \(\pi (x;q,a)\) the number of primes \(p\leqslant x\) lying in the progression \(a\bmod q\). By hypothesis, \(qy \geqslant q^{1+1/\sqrt{c}}=q^{12}\), therefore we may apply [[42][172], Corollary 1.4], obtaining

$$\begin{aligned} \pi (qy+1;q,1) &\leqslant \sqrt{y/q}+ \frac{2}{\log (qy)} \sum _{ \substack{\sqrt{qy}< p\leqslant qy \\ p\equiv 1\pmod{q}}} \log p \\ &\ll \sqrt{y/q}+\frac{\lambda qy}{\phi (q) \log (qy)}, \end{aligned}$$

where

$$ \lambda :=1 - (qy)^{-\delta _{q}}/(1-\delta _{q}) \ll \delta _{q} \log (qy). $$

By Siegel’s Theorem [[7][77], §21], for any \(\varepsilon >0\), \(\delta _{q} \gg _{\varepsilon }q^{-\varepsilon }\). We conclude that

$$ \pi (qy+1;q,1) \ll \frac{\delta _{q} qy}{\phi (q)}. $$

This may also be deduced from Gallagher’s prime number theorem [[13][173], Theorem 7].

Define the residue classes \(a_{p}\) by \(qa_{p}+1\equiv 0\bmod{p}\) when \(p\nmid q\). Let \(\mathcal{T} \) denote the set of \(n\leqslant y\) with \(n\not \equiv a_{p}\bmod{p}\) for all \(p\nmid q\) such that \(p\leqslant \sqrt{y/\log y}\). Then for any \(n\in \mathcal{T} \), \(qn+1\) is either prime or the product of two primes \(>\sqrt{y/\log y}\). Then we make a greedy choice of \(a_{p}\) for \(p\mid q\), choosing successively \(a_{p}\) so that \(a_{p}\bmod p\) covers a proportion at least \(1/p\) of the remaining elements of \(\mathcal{T} \). This shows that

$$\begin{aligned} W_{y} &\leqslant \frac{\phi (q)}{q} | \mathcal{T} | \\ &\leqslant \frac{\phi (q)}{q} \bigg[ \pi (qy+1;q,1)+ \sum _{\sqrt{y/\log y} < p \leqslant \sqrt{qy+1}} \pi \left ( \frac{qy+1}{p};q,\overline{p} \right ) \bigg], \end{aligned}$$

where \(\overline{p}\) is the inverse of \(p\) modulo \(q\). Siegel’s theorem implies that \(\log y \leqslant q^{o(1)}\). Applying the Brun-Titchmarsh theorem to the sum over \(p\), we see that

$$\begin{aligned} W_{y} \ll \frac{\phi (q)}{q} \bigg[ \frac{qy\delta _{q}}{\phi (q)}+ \frac{qy\log (q\log y)}{\phi (q)\log ^{2} y}\bigg] \ll y \Big[ \delta _{q}+\frac{\log q}{\log ^{2} y} \Big] \ll \delta _{q} y. \end{aligned}$$

This completes the proof. □

### Proof of Theorem [2.2][64]

Let \(q\in Q\), and apply Theorem [9.1][174] with \(y=y_{q}\) defined by ( [9.1][175]). By assumption, \(\frac{\log y_{q}}{\log q} \to \infty \) as \(q\to \infty \), and hence that

$$ \delta _{q}=\frac{\log q}{\log ^{2} y_{q}}=o\left ( \frac{1}{\log y_{q}}\right ). $$

This shows that \(W_{y_{q}}=o (y_{q}/\log y_{q})\), and the remaining parts of Theorem [2.2][64] follow immediately. □

## Notes

1.

See Sect. [3.1][176] for the asymptotic notation used in this paper.

2.

See also [[6][17], Eq. (5)] for a more precise version of ( [1.1][33]).

3.

Most of this work appears only on web pages, rather than in books or journals.

## References

1.

Azuma, K.: Weighted sums of certain dependent random variables. Tohoku Math. J. **19**, 357–367 (1967)

[Article][177] [MathSciNet][178] [MATH][179] [Google Scholar][180]

2.

Baker, R.C., Harman, G., Pintz, J.: The difference between consecutive primes. II. Proc. Lond. Math. Soc. (3) **83**(3), 532–562 (2001)

[Article][181] [MathSciNet][182] [MATH][183] [Google Scholar][184]

3.

Bennett, G.: Probability inequalities for the sum of independent random variables. J. Am. Stat. Assoc. **57**, 33–45 (1962)

[Article][185] [MATH][186] [Google Scholar][187]

4.

Cadwell, J.H.: Large intervals between consecutive primes. Math. Comput. **25**, 909–913 (1971)

[Article][188] [MathSciNet][189] [MATH][190] [Google Scholar][191]

5.

Cramér, H.: Some theorems concerning prime numbers. Ark. Mat. Astron. Fys. **15**(5), 1–32 (1920)

[Google Scholar][192]

6.

Cramér, H.: On the order of magnitude of the difference between consecutive prime numbers. Acta Arith. **2**(1), 23–46 (1936)

[Article][193] [MATH][194] [Google Scholar][195]

7.

Davenport, H.: Multiplicative Number Theory, 3rd edn. Graduate Texts in Mathematics, vol. 74. Springer, New York (2000)

[MATH][196] [Google Scholar][197]

8.

Elsholtz, C.: Upper bounds for prime \(k\) -tuples of size \(\log N\) and oscillations. Arch. Math. (Basel) **82**, 33–39 (2004)

[Article][198] [MathSciNet][199] [MATH][200] [Google Scholar][201]

9.

Erdős, P., Richards, I.: Density functions for prime and relatively prime numbers. Monatshefte Math. **83**, 99–112 (1977)

[Article][202] [MathSciNet][203] [MATH][204] [Google Scholar][205]

10.

Ford, K.: Large prime gaps and progressions with few primes. Riv. Mat. Univ. Parma **12**(1), 41–47 (2021). Proceedings of Second Symposium on Analytic Number Theory Cetraro, Italy, July 8–12, 2019.

[MathSciNet][206] [MATH][207] [Google Scholar][208]

11.

Ford, K., Green, B., Konyagin, S., Maynard, J., Tao, T.: Long gaps between primes. J. Am. Math. Soc. **31**(1), 65–105 (2018)

[Article][209] [MathSciNet][210] [MATH][211] [Google Scholar][212]

12.

Friedlander, J., Iwaniec, H.: Opera de Cribro. Am. Math. Soc., Providence (2010)

[Book][213] [MATH][214] [Google Scholar][215]

13.

Gallagher, P.X.: A large sieve density estimate near \(\sigma =1\). Invent. Math. **11**, 329–339 (1970)

[Article][216] [MathSciNet][217] [MATH][218] [Google Scholar][219]

14.

Gallagher, P.X.: On the distribution of primes in short intervals. Mathematika **23**(1), 4–9 (1976)

[Article][220] [MathSciNet][221] [MATH][222] [Google Scholar][223]

15.

Goldston, D.A., Pintz, J., Yıldırım, C.Y.: Primes in tuples I. Ann. Math. **170**, 819–862 (2009)

[Article][224] [MathSciNet][225] [MATH][226] [Google Scholar][227]

16.

Granville, A.: Harald Cramér and the distribution of prime numbers, Harald Cramér Symposium, Stockholm, 1993. Scand. Actuar. J. **1**, 12–28 (1995)

[Article][228] [MATH][229] [Google Scholar][230]

17.

Granville, A.: Sieving intervals and Siegel zeros. Acta Arith. **205**(1), 1–19 (2022)

[Article][231] [MathSciNet][232] [MATH][233] [Google Scholar][234]

18.

Granville, A., Lumley, A.: Primes in short intervals: Heuristics and calculations, preprint. [arXiv:2009.05000][235]

19.

Hardy, G.H., Littlewood, J.E.: Some problems of Partitio numerorum (III): on the expression of a number as a sum of primes. Acta Math. **44**(1), 1–70 (1922)

[MathSciNet][236] [MATH][237] [Google Scholar][238]

20.

Hensley, D., Richards, I.: Primes in intervals. Acta Arith. **25**, 375–391 (1973/74)

21.

Iwaniec, H.: On the error term in the linear sieve. Acta Arith. **19**, 1–30 (1971)

[Article][239] [MathSciNet][240] [MATH][241] [Google Scholar][242]

22.

Iwaniec, H.: Conversations on the exceptional character. In: Perelli, A., Viola, C. (eds.) Analytic Number Theory, lectures given at the C.I.M.E. summer school in Cetraro, Italy. Lecture Notes in Mathematics, vol. 1891, pp. 97–132. Springer, Berlin (2002)

[Chapter][243] [Google Scholar][244]

23.

Koukoulopoulos, D.: The distribution of prime numbers. To be published

24.

Leikauf, P., Waldvogel, J.: Finding clusters of primes, I, preprint. [https://www.sam.math.ethz.ch/~waldvoge/Projects/clprimes03.pdf][245]

25.

Maier, H.: Primes in short intervals. Mich. Math. J. **32**(2), 221–225 (1985)

[Article][246] [MathSciNet][247] [MATH][248] [Google Scholar][249]

26.

Mastrostefano, D.: Positive proportion of short intervals containing a prescribed number of primes. Bull. Aust. Math. Soc. **100**(3), 378–387 (2019)

[Article][250] [MathSciNet][251] [MATH][252] [Google Scholar][253]

27.

Montgomery, H.L.: A note on the large sieve. J. Lond. Math. Soc. **43**, 93–98 (1968)

[Article][254] [MathSciNet][255] [MATH][256] [Google Scholar][257]

28.

Montgomery, H.L., Soundararajan, K.: Primes in short intervals. Commun. Math. Phys. **252**(1–3), 589–617 (2004)

[Article][258] [MathSciNet][259] [MATH][260] [Google Scholar][261]

29.

Montgomery, H.L., Vaughan, R.C.: The large sieve. Mathematika **20**, 119–135 (1973)

[Article][262] [MathSciNet][263] [MATH][264] [Google Scholar][265]

30.

Montgomery, H.L., Vaughan, R.C.: Multiplicative Number Theory I. Classical Theory. Cambridge Studies in Advanced Mathematics, vol. 97. Cambridge University Press, Cambridge (2007)

[MATH][266] [Google Scholar][267]

31.

Montgomery, H.L., Wagon, S.: A heuristic for the prime number theorem. Math. Intell. **28**(3), 6–9 (2006)

[Article][268] [MathSciNet][269] [MATH][270] [Google Scholar][271]

32.

Nicely, T.R.: Enumeration to \(10^{14}\) of the twin primes and Brun’s constant. Va. J. Sci. **46**(3), 195–204 (1995)

[MathSciNet][272] [Google Scholar][273]

33.

Nicely, T.R.: New evidence for the infinitude of some prime constellations, preprint. [http://www.trnicely.net/ipc/ipc1d.html][274]

34.

Nicely, T.R.: Prime constellations research project, web pages: [http://www.trnicely.net/counts.html][275]

35.

Nicely, T.R.: First occurrence prime gaps, web page: [http://www.trnicely.net/gaps/gaplist.html][276]

36.

Pintz, J.: Cramér vs. Cramér. On Cramér’s probabilistic model for primes. Funct. Approx. Comment. Math. **37**(2), 361–376 (2007)

[Article][277] [MathSciNet][278] [MATH][279] [Google Scholar][280]

37.

Pólya, G.: Heuristic reasoning in the theory of numbers. Am. Math. Mon. **66**, 375–384 (1959)

[Article][281] [MathSciNet][282] [MATH][283] [Google Scholar][284]

38.

Selberg, A.: On the normal density of primes in small intervals, and the difference between consecutive primes. Arch. Math. Naturvidensk. **47**(6), 87–105 (1943)

[MathSciNet][285] [MATH][286] [Google Scholar][287]

39.

Selberg, A.: Remarks on sieves. In: Proc. 1972 Number Theory Conference, University of Colorado at Boulder, August 14–18, pp. 205–216 (1972)

[Google Scholar][288]

40.

Shanks, D.: On maximal gaps between successive primes. Math. Comput. **18**, 646–651 (1964)

[Article][289] [MathSciNet][290] [MATH][291] [Google Scholar][292]

41.

Soundararajan, K.: The distribution of prime numbers. In: Equidistribution in Number Theory, An Introduction. NATO Sci. Ser. II Math. Phys. Chem., vol. 237, pp. 59–83. Springer, Dordrecht (2007)

[Chapter][293] [Google Scholar][294]

42.

Thorner, J., Zaman, A.: Refinements to the prime number theorem for arithmetic progressions, preprint. [arXiv:2108.10878][295]

[Download references][296]

## Acknowledgements

The authors thank Andrew Granville, Ben Green, D. R. Heath-Brown, Henryk Iwaniec, Dimitris Koukoulopoulos, James Maynard, Carl Pomerance and Joni Teräväinen for useful discussions, especially concerning the interval sieve problem.

## Funding

The first author was supported by a grant from the University of Missouri Research Board. The second author was supported by National Science Foundation grants DMS-1501982 and DMS-1802139. The third author was supported by a Simons Investigator grant, the James and Carol Collins Chair, the Mathematical Analysis & Application Research Fund Endowment, and by NSF grant DMS-1764034. Part of the work was accomplished during a visit of the second author to the University of Missouri (August 2017), UCLA (November 2018), the University of Cambridge (March 2019), the University of Oxford (March-June, 2019) and the Institute of Mathematics of the Bulgarian Academy of Sciences (June-July, 2019). He thanks them all for their support.

## Author information

### Authors and Affiliations

1.

Department of Mathematics, University of Missouri, Columbia, MO, 65211, USA

William Banks

2.

Department of Mathematics, University of Illinois, 1409 West Green St, Urbana, IL, 61801, USA

Kevin Ford

3.

Department of Mathematics, UCLA, 405 Hilgard Ave, Los Angeles, CA, 90095, USA

Terence Tao

Authors

1. William Banks

[View author publications][297]

Search author on: [PubMed][298] [Google Scholar][299]

2. Kevin Ford

[View author publications][300]

Search author on: [PubMed][301] [Google Scholar][302]

3. Terence Tao

[View author publications][303]

Search author on: [PubMed][304] [Google Scholar][305]

### Corresponding author

Correspondence to [Terence Tao][306].

## Additional information

### Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][307].

[Reprints and permissions][308]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [309]

### Cite this article

Banks, W., Ford, K. & Tao, T. Large prime gaps and probabilistic models. *Invent. math.***233**, 1471–1518 (2023). https://doi.org/10.1007/s00222-023-01199-0

[Download citation][310]

-

Received: 22 August 2019

-

Accepted: 03 May 2023

-

Published: 14 June 2023

-

Version of record: 14 June 2023

-

Issue date: September 2023

-

DOI: https://doi.org/10.1007/s00222-023-01199-0

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Mathematics Subject Classification

- [11N05][311]
- [11B83][312]

### Profiles

1. Terence Tao [View author profile][313]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s00222-023-01199-0.pdf
[3]: /article/10.1007/s00222-023-01199-0/save-research?_csrf=qUxcY58bofuZd2ehbFwjdcpEVM3UbtyW
[4]: /saved-research
[5]: /journal/222
[6]: /journal/222/aims-and-scope
[7]: https://link.springer.com/10.1007/s40993-018-0109-y?fromPaywallRec=false
[8]: https://link.springer.com/10.1007/s00222-019-00865-6?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s00605-021-01641-6?fromPaywallRec=false
[10]: /subjects/combinatorics
[11]: /subjects/computational-number-theory
[12]: /subjects/discrete-mathematics-in-computer-science
[13]: /subjects/discrete-mathematics
[14]: /subjects/number-theory
[15]: /subjects/probability-theory
[16]: /subjects/dynamical-systems-and-ergodic-theory-in-number-theory
[17]: /article/10.1007/s00222-023-01199-0#ref-CR6
[18]: /article/10.1007/s00222-023-01199-0#ref-CR16
[19]: /article/10.1007/s00222-023-01199-0#FPar1
[20]: /article/10.1007/s00222-023-01199-0#ref-CR11
[21]: /article/10.1007/s00222-023-01199-0#ref-CR2
[22]: /article/10.1007/s00222-023-01199-0#ref-CR5
[23]: /article/10.1007/s00222-023-01199-0#FPar11
[24]: /article/10.1007/s00222-023-01199-0#ref-CR40
[25]: /article/10.1007/s00222-023-01199-0#Equ2
[26]: /article/10.1007/s00222-023-01199-0#ref-CR4
[27]: /article/10.1007/s00222-023-01199-0#ref-CR41
[28]: /article/10.1007/s00222-023-01199-0#ref-CR35
[29]: /article/10.1007/s00222-023-01199-0#Fig1
[30]: /article/10.1007/s00222-023-01199-0/figures/1
[31]: /article/10.1007/s00222-023-01199-0#ref-CR36
[32]: /article/10.1007/s00222-023-01199-0#Sec15
[33]: /article/10.1007/s00222-023-01199-0#Equ1
[34]: /article/10.1007/s00222-023-01199-0#Equ4
[35]: /article/10.1007/s00222-023-01199-0#Equ3
[36]: /article/10.1007/s00222-023-01199-0#ref-CR19
[37]: /article/10.1007/s00222-023-01199-0#Equ5
[38]: /article/10.1007/s00222-023-01199-0#Equ9
[39]: /article/10.1007/s00222-023-01199-0#Equ11
[40]: /article/10.1007/s00222-023-01199-0#ref-CR12
[41]: /article/10.1007/s00222-023-01199-0#ref-CR21
[42]: /article/10.1007/s00222-023-01199-0#Equ12
[43]: /article/10.1007/s00222-023-01199-0#ref-CR20
[44]: /article/10.1007/s00222-023-01199-0#ref-CR9
[45]: /article/10.1007/s00222-023-01199-0#Equ14
[46]: /article/10.1007/s00222-023-01199-0#ref-CR28
[47]: /article/10.1007/s00222-023-01199-0#Sec11
[48]: /article/10.1007/s00222-023-01199-0#Equ16
[49]: /article/10.1007/s00222-023-01199-0#Equ10
[50]: /article/10.1007/s00222-023-01199-0#ref-CR14
[51]: /article/10.1007/s00222-023-01199-0#FPar5
[52]: /article/10.1007/s00222-023-01199-0#Equ13
[53]: /article/10.1007/s00222-023-01199-0#FPar3
[54]: /article/10.1007/s00222-023-01199-0#Sec10
[55]: /article/10.1007/s00222-023-01199-0#Sec18
[56]: /article/10.1007/s00222-023-01199-0#FPar4
[57]: /article/10.1007/s00222-023-01199-0#Sec21
[58]: /article/10.1007/s00222-023-01199-0#Sec22
[59]: /article/10.1007/s00222-023-01199-0#Sec23
[60]: /article/10.1007/s00222-023-01199-0#Sec24
[61]: /article/10.1007/s00222-023-01199-0#FPar6
[62]: /article/10.1007/s00222-023-01199-0#Sec25
[63]: /article/10.1007/s00222-023-01199-0#Sec14
[64]: /article/10.1007/s00222-023-01199-0#FPar8
[65]: /article/10.1007/s00222-023-01199-0#Sec26
[66]: /article/10.1007/s00222-023-01199-0#FPar12
[67]: /article/10.1007/s00222-023-01199-0#Equ17
[68]: /article/10.1007/s00222-023-01199-0#ref-CR8
[69]: /article/10.1007/s00222-023-01199-0#Equ18
[70]: /article/10.1007/s00222-023-01199-0#ref-CR32
[71]: /article/10.1007/s00222-023-01199-0#ref-CR24
[72]: /article/10.1007/s00222-023-01199-0#ref-CR33
[73]: /article/10.1007/s00222-023-01199-0#ref-CR34
[74]: /article/10.1007/s00222-023-01199-0#ref-CR37
[75]: /article/10.1007/s00222-023-01199-0#ref-CR31
[76]: /article/10.1007/s00222-023-01199-0#ref-CR29
[77]: /article/10.1007/s00222-023-01199-0#ref-CR7
[78]: /article/10.1007/s00222-023-01199-0#ref-CR22
[79]: /article/10.1007/s00222-023-01199-0#FPar2
[80]: /article/10.1007/s00222-023-01199-0#Equ15
[81]: /article/10.1007/s00222-023-01199-0#ref-CR30
[82]: /article/10.1007/s00222-023-01199-0#ref-CR39
[83]: /article/10.1007/s00222-023-01199-0#ref-CR17
[84]: /article/10.1007/s00222-023-01199-0#ref-CR10
[85]: /article/10.1007/s00222-023-01199-0#ref-CR25
[86]: /article/10.1007/s00222-023-01199-0#Equ19
[87]: /article/10.1007/s00222-023-01199-0#Equ20
[88]: /article/10.1007/s00222-023-01199-0#ref-CR23
[89]: /article/10.1007/s00222-023-01199-0#ref-CR38
[90]: /article/10.1007/s00222-023-01199-0#ref-CR18
[91]: /article/10.1007/s00222-023-01199-0#Equ22
[92]: /article/10.1007/s00222-023-01199-0#Equ23
[93]: /article/10.1007/s00222-023-01199-0#ref-CR26
[94]: /article/10.1007/s00222-023-01199-0#Equ21
[95]: /article/10.1007/s00222-023-01199-0#ref-CR1
[96]: /article/10.1007/s00222-023-01199-0#ref-CR3
[97]: /article/10.1007/s00222-023-01199-0#Equ24
[98]: /article/10.1007/s00222-023-01199-0#Equ25
[99]: /article/10.1007/s00222-023-01199-0#ref-CR15
[100]: /article/10.1007/s00222-023-01199-0#Equ7
[101]: /article/10.1007/s00222-023-01199-0#FPar16
[102]: /article/10.1007/s00222-023-01199-0#Equ26
[103]: /article/10.1007/s00222-023-01199-0#Equ27
[104]: /article/10.1007/s00222-023-01199-0#Equ28
[105]: /article/10.1007/s00222-023-01199-0#Equ29
[106]: /article/10.1007/s00222-023-01199-0#FPar19
[107]: /article/10.1007/s00222-023-01199-0#FPar14
[108]: /article/10.1007/s00222-023-01199-0#Equ32
[109]: /article/10.1007/s00222-023-01199-0#Equ30
[110]: /article/10.1007/s00222-023-01199-0#Equ33
[111]: /article/10.1007/s00222-023-01199-0#Equ34
[112]: /article/10.1007/s00222-023-01199-0#Equ35
[113]: /article/10.1007/s00222-023-01199-0#Equ31
[114]: /article/10.1007/s00222-023-01199-0#Equ36
[115]: /article/10.1007/s00222-023-01199-0#Equ37
[116]: /article/10.1007/s00222-023-01199-0#Equ38
[117]: /article/10.1007/s00222-023-01199-0#Equ39
[118]: /article/10.1007/s00222-023-01199-0#Equ40
[119]: /article/10.1007/s00222-023-01199-0#Equ42
[120]: /article/10.1007/s00222-023-01199-0#Equ44
[121]: /article/10.1007/s00222-023-01199-0#FPar22
[122]: /article/10.1007/s00222-023-01199-0#FPar24
[123]: /article/10.1007/s00222-023-01199-0#FPar26
[124]: /article/10.1007/s00222-023-01199-0#FPar28
[125]: /article/10.1007/s00222-023-01199-0#FPar31
[126]: /article/10.1007/s00222-023-01199-0#FPar35
[127]: /article/10.1007/s00222-023-01199-0#FPar33
[128]: /article/10.1007/s00222-023-01199-0#FPar9
[129]: /article/10.1007/s00222-023-01199-0#Equ43
[130]: /article/10.1007/s00222-023-01199-0#Equ46
[131]: /article/10.1007/s00222-023-01199-0#Equ47
[132]: /article/10.1007/s00222-023-01199-0#Equ45
[133]: /article/10.1007/s00222-023-01199-0#ref-CR27
[134]: /article/10.1007/s00222-023-01199-0#Equ49
[135]: /article/10.1007/s00222-023-01199-0#Equ50
[136]: /article/10.1007/s00222-023-01199-0#Equ48
[137]: /article/10.1007/s00222-023-01199-0#Equ41
[138]: /article/10.1007/s00222-023-01199-0#FPar10
[139]: /article/10.1007/s00222-023-01199-0#Equ51
[140]: /article/10.1007/s00222-023-01199-0#Equ52
[141]: /article/10.1007/s00222-023-01199-0#FPar30
[142]: /article/10.1007/s00222-023-01199-0#Equ53
[143]: /article/10.1007/s00222-023-01199-0#Equ54
[144]: /article/10.1007/s00222-023-01199-0#Equ55
[145]: /article/10.1007/s00222-023-01199-0#Equ56
[146]: /article/10.1007/s00222-023-01199-0#Equ57
[147]: /article/10.1007/s00222-023-01199-0#Equ58
[148]: /article/10.1007/s00222-023-01199-0#FPar37
[149]: /article/10.1007/s00222-023-01199-0#FPar38
[150]: /article/10.1007/s00222-023-01199-0#Equ60
[151]: /article/10.1007/s00222-023-01199-0#Equ61
[152]: /article/10.1007/s00222-023-01199-0#Equ59
[153]: /article/10.1007/s00222-023-01199-0#Equ64
[154]: /article/10.1007/s00222-023-01199-0#Equ63
[155]: /article/10.1007/s00222-023-01199-0#Equ62
[156]: /article/10.1007/s00222-023-01199-0#Equ65
[157]: /article/10.1007/s00222-023-01199-0#Equ66
[158]: /article/10.1007/s00222-023-01199-0#Equ67
[159]: /article/10.1007/s00222-023-01199-0#FPar42
[160]: /article/10.1007/s00222-023-01199-0#Equ8
[161]: /article/10.1007/s00222-023-01199-0#Equ68
[162]: /article/10.1007/s00222-023-01199-0#Equ70
[163]: /article/10.1007/s00222-023-01199-0#Equ69
[164]: /article/10.1007/s00222-023-01199-0#Equ71
[165]: /article/10.1007/s00222-023-01199-0#Equ73
[166]: /article/10.1007/s00222-023-01199-0#Equ72
[167]: /article/10.1007/s00222-023-01199-0#Equ77
[168]: /article/10.1007/s00222-023-01199-0#Equ78
[169]: /article/10.1007/s00222-023-01199-0#Equ75
[170]: /article/10.1007/s00222-023-01199-0#Equ76
[171]: /article/10.1007/s00222-023-01199-0#Equ74
[172]: /article/10.1007/s00222-023-01199-0#ref-CR42
[173]: /article/10.1007/s00222-023-01199-0#ref-CR13
[174]: /article/10.1007/s00222-023-01199-0#FPar46
[175]: /article/10.1007/s00222-023-01199-0#Equ79
[176]: /article/10.1007/s00222-023-01199-0#Sec19
[177]: https://doi.org/10.2748%2Ftmj%2F1178243286
[178]: http://www.ams.org/mathscinet-getitem?mr=221571
[179]: http://www.emis.de/MATH-item?0178.21103
[180]: http://scholar.google.com/scholar_lookup?amp;title=Weighted%20sums%20of%20certain%20dependent%20random%20variables&amp;journal=Tohoku%20Math.%20J.&amp;doi=10.2748%2Ftmj%2F1178243286&amp;volume=19&amp;pages=357-367&amp;publication_year=1967&amp;author=Azuma%2CK.
[181]: https://doi.org/10.1112%2Fplms%2F83.3.532
[182]: http://www.ams.org/mathscinet-getitem?mr=1851081
[183]: http://www.emis.de/MATH-item?1016.11037
[184]: http://scholar.google.com/scholar_lookup?amp;title=The%20difference%20between%20consecutive%20primes.%20II&amp;journal=Proc.%20Lond.%20Math.%20Soc.%20%283%29&amp;doi=10.1112%2Fplms%2F83.3.532&amp;volume=83&amp;issue=3&amp;pages=532-562&amp;publication_year=2001&amp;author=Baker%2CR.C.&amp;author=Harman%2CG.&amp;author=Pintz%2CJ.
[185]: https://doi.org/10.1080%2F01621459.1962.10482149
[186]: http://www.emis.de/MATH-item?0104.11905
[187]: http://scholar.google.com/scholar_lookup?amp;title=Probability%20inequalities%20for%20the%20sum%20of%20independent%20random%20variables&amp;journal=J.%20Am.%20Stat.%20Assoc.&amp;doi=10.1080%2F01621459.1962.10482149&amp;volume=57&amp;pages=33-45&amp;publication_year=1962&amp;author=Bennett%2CG.
[188]: https://doi.org/10.1090%2FS0025-5718-1971-0299567-6
[189]: http://www.ams.org/mathscinet-getitem?mr=299567
[190]: http://www.emis.de/MATH-item?0229.10024
[191]: http://scholar.google.com/scholar_lookup?amp;title=Large%20intervals%20between%20consecutive%20primes&amp;journal=Math.%20Comput.&amp;doi=10.1090%2FS0025-5718-1971-0299567-6&amp;volume=25&amp;pages=909-913&amp;publication_year=1971&amp;author=Cadwell%2CJ.H.
[192]: http://scholar.google.com/scholar_lookup?amp;title=Some%20theorems%20concerning%20prime%20numbers&amp;journal=Ark.%20Mat.%20Astron.%20Fys.&amp;volume=15&amp;issue=5&amp;pages=1-32&amp;publication_year=1920&amp;author=Cram%C3%A9r%2CH.
[193]: https://doi.org/10.4064%2Faa-2-1-23-46
[194]: http://www.emis.de/MATH-item?62.1147.01
[195]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20order%20of%20magnitude%20of%20the%20difference%20between%20consecutive%20prime%20numbers&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa-2-1-23-46&amp;volume=2&amp;issue=1&amp;pages=23-46&amp;publication_year=1936&amp;author=Cram%C3%A9r%2CH.
[196]: http://www.emis.de/MATH-item?1002.11001
[197]: http://scholar.google.com/scholar_lookup?amp;title=Multiplicative%20Number%20Theory&amp;publication_year=2000&amp;author=Davenport%2CH.
[198]: https://link.springer.com/doi/10.1007/s00013-003-4780-3
[199]: http://www.ams.org/mathscinet-getitem?mr=2034468
[200]: http://www.emis.de/MATH-item?1057.11042
[201]: http://scholar.google.com/scholar_lookup?amp;title=Upper%20bounds%20for%20prime%20k%20%24k%24%20-tuples%20of%20size%20log%20N%20%24%5Clog%20N%24%20and%20oscillations&amp;journal=Arch.%20Math.%20%28Basel%29&amp;doi=10.1007%2Fs00013-003-4780-3&amp;volume=82&amp;pages=33-39&amp;publication_year=2004&amp;author=Elsholtz%2CC.
[202]: https://link.springer.com/doi/10.1007/BF01534631
[203]: http://www.ams.org/mathscinet-getitem?mr=439785
[204]: http://www.emis.de/MATH-item?0355.10034
[205]: http://scholar.google.com/scholar_lookup?amp;title=Density%20functions%20for%20prime%20and%20relatively%20prime%20numbers&amp;journal=Monatshefte%20Math.&amp;doi=10.1007%2FBF01534631&amp;volume=83&amp;pages=99-112&amp;publication_year=1977&amp;author=Erd%C5%91s%2CP.&amp;author=Richards%2CI.
[206]: http://www.ams.org/mathscinet-getitem?mr=4284772
[207]: http://www.emis.de/MATH-item?1480.11111
[208]: http://scholar.google.com/scholar_lookup?amp;title=Large%20prime%20gaps%20and%20progressions%20with%20few%20primes&amp;journal=Riv.%20Mat.%20Univ.%20Parma&amp;volume=12&amp;issue=1&amp;pages=41-47&amp;publication_year=2021&amp;author=Ford%2CK.
[209]: https://doi.org/10.1090%2Fjams%2F876
[210]: http://www.ams.org/mathscinet-getitem?mr=3718451
[211]: http://www.emis.de/MATH-item?1392.11071
[212]: http://scholar.google.com/scholar_lookup?amp;title=Long%20gaps%20between%20primes&amp;journal=J.%20Am.%20Math.%20Soc.&amp;doi=10.1090%2Fjams%2F876&amp;volume=31&amp;issue=1&amp;pages=65-105&amp;publication_year=2018&amp;author=Ford%2CK.&amp;author=Green%2CB.&amp;author=Konyagin%2CS.&amp;author=Maynard%2CJ.&amp;author=Tao%2CT.
[213]: https://doi.org/10.1090%2Fcoll%2F057
[214]: http://www.emis.de/MATH-item?1226.11099
[215]: http://scholar.google.com/scholar_lookup?amp;title=Opera%20de%20Cribro&amp;doi=10.1090%2Fcoll%2F057&amp;publication_year=2010&amp;author=Friedlander%2CJ.&amp;author=Iwaniec%2CH.
[216]: https://link.springer.com/doi/10.1007/BF01403187
[217]: http://www.ams.org/mathscinet-getitem?mr=279049
[218]: http://www.emis.de/MATH-item?0219.10048
[219]: http://scholar.google.com/scholar_lookup?amp;title=A%20large%20sieve%20density%20estimate%20near%20%CF%83%20%3D%201%20%24%5Csigma%20%3D1%24&amp;journal=Invent.%20Math.&amp;doi=10.1007%2FBF01403187&amp;volume=11&amp;pages=329-339&amp;publication_year=1970&amp;author=Gallagher%2CP.X.
[220]: https://doi.org/10.1112%2FS0025579300016442
[221]: http://www.ams.org/mathscinet-getitem?mr=409385
[222]: http://www.emis.de/MATH-item?0346.10024
[223]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20distribution%20of%20primes%20in%20short%20intervals&amp;journal=Mathematika&amp;doi=10.1112%2FS0025579300016442&amp;volume=23&amp;issue=1&amp;pages=4-9&amp;publication_year=1976&amp;author=Gallagher%2CP.X.
[224]: https://doi.org/10.4007%2Fannals.2009.170.819
[225]: http://www.ams.org/mathscinet-getitem?mr=2552109
[226]: http://www.emis.de/MATH-item?1207.11096
[227]: http://scholar.google.com/scholar_lookup?amp;title=Primes%20in%20tuples%20I&amp;journal=Ann.%20Math.&amp;doi=10.4007%2Fannals.2009.170.819&amp;volume=170&amp;pages=819-862&amp;publication_year=2009&amp;author=Goldston%2CD.A.&amp;author=Pintz%2CJ.&amp;author=Y%C4%B1ld%C4%B1r%C4%B1m%2CC.Y.
[228]: https://doi.org/10.1080%2F03461238.1995.10413946
[229]: http://www.emis.de/MATH-item?0833.01018
[230]: http://scholar.google.com/scholar_lookup?amp;title=Harald%20Cram%C3%A9r%20and%20the%20distribution%20of%20prime%20numbers&amp;journal=Scand.%20Actuar.%20J.&amp;doi=10.1080%2F03461238.1995.10413946&amp;volume=1&amp;pages=12-28&amp;publication_year=1995&amp;author=Granville%2CA.
[231]: https://doi.org/10.4064%2Faa201002-25-6
[232]: http://www.ams.org/mathscinet-getitem?mr=4485979
[233]: http://www.emis.de/MATH-item?1504.11089
[234]: http://scholar.google.com/scholar_lookup?amp;title=Sieving%20intervals%20and%20Siegel%20zeros&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa201002-25-6&amp;volume=205&amp;issue=1&amp;pages=1-19&amp;publication_year=2022&amp;author=Granville%2CA.
[235]: http://arxiv.org/abs/arXiv:2009.05000
[236]: http://www.ams.org/mathscinet-getitem?mr=1555183
[237]: http://www.emis.de/MATH-item?48.0143.04
[238]: http://scholar.google.com/scholar_lookup?amp;title=Some%20problems%20of%20Partitio%20numerorum%20%28III%29%3A%20on%20the%20expression%20of%20a%20number%20as%20a%20sum%20of%20primes&amp;journal=Acta%20Math.&amp;volume=44&amp;issue=1&amp;pages=1-70&amp;publication_year=1922&amp;author=Hardy%2CG.H.&amp;author=Littlewood%2CJ.E.
[239]: https://doi.org/10.4064%2Faa-19-1-1-30
[240]: http://www.ams.org/mathscinet-getitem?mr=296043
[241]: http://www.emis.de/MATH-item?0222.10050
[242]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20error%20term%20in%20the%20linear%20sieve&amp;journal=Acta%20Arith.&amp;doi=10.4064%2Faa-19-1-1-30&amp;volume=19&amp;pages=1-30&amp;publication_year=1971&amp;author=Iwaniec%2CH.
[243]: https://link.springer.com/doi/10.1007/978-3-540-36364-4_3
[244]: http://scholar.google.com/scholar_lookup?amp;title=Conversations%20on%20the%20exceptional%20character&amp;doi=10.1007%2F978-3-540-36364-4_3&amp;pages=97-132&amp;publication_year=2002&amp;author=Iwaniec%2CH.
[245]: https://www.sam.math.ethz.ch/~waldvoge/Projects/clprimes03.pdf
[246]: https://doi.org/10.1307%2Fmmj%2F1029003189
[247]: http://www.ams.org/mathscinet-getitem?mr=783576
[248]: http://www.emis.de/MATH-item?0569.10023
[249]: http://scholar.google.com/scholar_lookup?amp;title=Primes%20in%20short%20intervals&amp;journal=Mich.%20Math.%20J.&amp;doi=10.1307%2Fmmj%2F1029003189&amp;volume=32&amp;issue=2&amp;pages=221-225&amp;publication_year=1985&amp;author=Maier%2CH.
[250]: https://doi.org/10.1017%2FS0004972719000467
[251]: http://www.ams.org/mathscinet-getitem?mr=4028185
[252]: http://www.emis.de/MATH-item?1469.11368
[253]: http://scholar.google.com/scholar_lookup?amp;title=Positive%20proportion%20of%20short%20intervals%20containing%20a%20prescribed%20number%20of%20primes&amp;journal=Bull.%20Aust.%20Math.%20Soc.&amp;doi=10.1017%2FS0004972719000467&amp;volume=100&amp;issue=3&amp;pages=378-387&amp;publication_year=2019&amp;author=Mastrostefano%2CD.
[254]: https://doi.org/10.1112%2Fjlms%2Fs1-43.1.93
[255]: http://www.ams.org/mathscinet-getitem?mr=224585
[256]: http://www.emis.de/MATH-item?0254.10043
[257]: http://scholar.google.com/scholar_lookup?amp;title=A%20note%20on%20the%20large%20sieve&amp;journal=J.%20Lond.%20Math.%20Soc.&amp;doi=10.1112%2Fjlms%2Fs1-43.1.93&amp;volume=43&amp;pages=93-98&amp;publication_year=1968&amp;author=Montgomery%2CH.L.
[258]: https://link.springer.com/doi/10.1007/s00220-004-1222-4
[259]: http://www.ams.org/mathscinet-getitem?mr=2104891
[260]: http://www.emis.de/MATH-item?1124.11048
[261]: http://scholar.google.com/scholar_lookup?amp;title=Primes%20in%20short%20intervals&amp;journal=Commun.%20Math.%20Phys.&amp;doi=10.1007%2Fs00220-004-1222-4&amp;volume=252&amp;issue=1%E2%80%933&amp;pages=589-617&amp;publication_year=2004&amp;author=Montgomery%2CH.L.&amp;author=Soundararajan%2CK.
[262]: https://doi.org/10.1112%2FS0025579300004708
[263]: http://www.ams.org/mathscinet-getitem?mr=374060
[264]: http://www.emis.de/MATH-item?0296.10023
[265]: http://scholar.google.com/scholar_lookup?amp;title=The%20large%20sieve&amp;journal=Mathematika&amp;doi=10.1112%2FS0025579300004708&amp;volume=20&amp;pages=119-135&amp;publication_year=1973&amp;author=Montgomery%2CH.L.&amp;author=Vaughan%2CR.C.
[266]: http://www.emis.de/MATH-item?1142.11001
[267]: http://scholar.google.com/scholar_lookup?amp;title=Multiplicative%20Number%20Theory%20I.%20Classical%20Theory&amp;publication_year=2007&amp;author=Montgomery%2CH.L.&amp;author=Vaughan%2CR.C.
[268]: https://link.springer.com/doi/10.1007/BF02986877
[269]: http://www.ams.org/mathscinet-getitem?mr=2253186
[270]: http://www.emis.de/MATH-item?1159.11032
[271]: http://scholar.google.com/scholar_lookup?amp;title=A%20heuristic%20for%20the%20prime%20number%20theorem&amp;journal=Math.%20Intell.&amp;doi=10.1007%2FBF02986877&amp;volume=28&amp;issue=3&amp;pages=6-9&amp;publication_year=2006&amp;author=Montgomery%2CH.L.&amp;author=Wagon%2CS.
[272]: http://www.ams.org/mathscinet-getitem?mr=1401560
[273]: http://scholar.google.com/scholar_lookup?amp;title=Enumeration%20to%2010%2014%20%2410%5E%7B14%7D%24%20of%20the%20twin%20primes%20and%20Brun%E2%80%99s%20constant&amp;journal=Va.%20J.%20Sci.&amp;volume=46&amp;issue=3&amp;pages=195-204&amp;publication_year=1995&amp;author=Nicely%2CT.R.
[274]: http://www.trnicely.net/ipc/ipc1d.html
[275]: http://www.trnicely.net/counts.html
[276]: http://www.trnicely.net/gaps/gaplist.html
[277]: https://doi.org/10.7169%2Ffacm%2F1229619660
[278]: http://www.ams.org/mathscinet-getitem?mr=2363833
[279]: http://www.emis.de/MATH-item?1226.11096
[280]: http://scholar.google.com/scholar_lookup?amp;title=Cram%C3%A9r%20vs.%20Cram%C3%A9r.%20On%20Cram%C3%A9r%E2%80%99s%20probabilistic%20model%20for%20primes&amp;journal=Funct.%20Approx.%20Comment.%20Math.&amp;doi=10.7169%2Ffacm%2F1229619660&amp;volume=37&amp;issue=2&amp;pages=361-376&amp;publication_year=2007&amp;author=Pintz%2CJ.
[281]: https://doi.org/10.1080%2F00029890.1959.11989304
[282]: http://www.ams.org/mathscinet-getitem?mr=104639
[283]: http://www.emis.de/MATH-item?0092.04901
[284]: http://scholar.google.com/scholar_lookup?amp;title=Heuristic%20reasoning%20in%20the%20theory%20of%20numbers&amp;journal=Am.%20Math.%20Mon.&amp;doi=10.1080%2F00029890.1959.11989304&amp;volume=66&amp;pages=375-384&amp;publication_year=1959&amp;author=P%C3%B3lya%2CG.
[285]: http://www.ams.org/mathscinet-getitem?mr=12624
[286]: http://www.emis.de/MATH-item?0063.06869
[287]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20normal%20density%20of%20primes%20in%20small%20intervals%2C%20and%20the%20difference%20between%20consecutive%20primes&amp;journal=Arch.%20Math.%20Naturvidensk.&amp;volume=47&amp;issue=6&amp;pages=87-105&amp;publication_year=1943&amp;author=Selberg%2CA.
[288]: http://scholar.google.com/scholar_lookup?amp;title=Remarks%20on%20sieves&amp;pages=205-216&amp;publication_year=1972&amp;author=Selberg%2CA.
[289]: https://doi.org/10.1090%2FS0025-5718-1964-0167472-8
[290]: http://www.ams.org/mathscinet-getitem?mr=167472
[291]: http://www.emis.de/MATH-item?0128.04203
[292]: http://scholar.google.com/scholar_lookup?amp;title=On%20maximal%20gaps%20between%20successive%20primes&amp;journal=Math.%20Comput.&amp;doi=10.1090%2FS0025-5718-1964-0167472-8&amp;volume=18&amp;pages=646-651&amp;publication_year=1964&amp;author=Shanks%2CD.
[293]: https://link.springer.com/doi/10.1007/978-1-4020-5404-4_4
[294]: http://scholar.google.com/scholar_lookup?amp;title=The%20distribution%20of%20prime%20numbers&amp;doi=10.1007%2F978-1-4020-5404-4_4&amp;pages=59-83&amp;publication_year=2007&amp;author=Soundararajan%2CK.
[295]: http://arxiv.org/abs/arXiv:2108.10878
[296]: https://citation-needed.springer.com/v2/references/10.1007/s00222-023-01199-0?format=refman&amp;flavour=references
[297]: /search?sortBy=newestFirst&amp;contributor=William%20Banks
[298]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=William%20Banks
[299]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22William%20Banks%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[300]: /search?sortBy=newestFirst&amp;contributor=Kevin%20Ford
[301]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Kevin%20Ford
[302]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Kevin%20Ford%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[303]: /search?sortBy=newestFirst&amp;contributor=Terence%20Tao
[304]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Terence%20Tao
[305]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Terence%20Tao%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[306]: mailto:tao@math.ucla.edu
[307]: http://creativecommons.org/licenses/by/4.0/
[308]: https://s100.copyright.com/AppDispatchServlet?title=Large%20prime%20gaps%20and%20probabilistic%20models&amp;author=William%20Banks%20et%20al&amp;contentID=10.1007%2Fs00222-023-01199-0&amp;copyright=The%20Author%28s%29&amp;publication=0020-9910&amp;publicationDate=2023-06-14&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[309]: https://crossmark.crossref.org/dialog/?doi=10.1007/s00222-023-01199-0
[310]: https://citation-needed.springer.com/v2/references/10.1007/s00222-023-01199-0?format=refman&amp;flavour=citation
[311]: /search?query=11N05&amp;facet-discipline=#34;Mathematics&#34;
[312]: /search?query=11B83&amp;facet-discipline=#34;Mathematics&#34;
[313]: /researchers/83952554SN
