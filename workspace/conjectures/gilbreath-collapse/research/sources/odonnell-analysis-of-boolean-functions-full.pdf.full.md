<!-- source: http://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf | converted from PDF -->

ANALYSIS OF BOOLEAN FUNCTIONS

Ryan O’Donnell

May 2021 arXiv Edition.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Originally published April 2014 by Cambridge University Press.

Cover illustration by A. A. Williams.

Single paper or electronic copies for noncommercial personal use may be made without explicit permission from the

author or publisher. All other rights reserved.
 To Zeynep,

for her unending support and encouragement.

Contents

Prefaces ix

List of Notation xiii

Chapter 1. Boolean functions and the Fourier expansion 19

§1.1. On analysis of Boolean functions 19

§1.2. The “Fourier expansion”: functions as multilinear polynomials 20

§1.3. The orthonormal basis of parity functions 23

§1.4. Basic Fourier formulas 25

§1.5. Probability densities and convolution 28

§1.6. Highlight: Almost linear functions and the BLR Test 31

§1.7. Exercises and notes 33

Chapter 2. Basic concepts and social choice 43

§2.1. Social choice functions 43

§2.2. Inﬂuences and derivatives 46

§2.3. Total inﬂuence 49

§2.4. Noise stability 53

§2.5. Highlight: Arrow’s Theorem 57

§2.6. Exercises and notes 61

Chapter 3. Spectral structure and learning 69

§3.1. Low-degree spectral concentration 69

§3.2. Subspaces and decision trees 71

§3.3. Restrictions 74

v

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

vi Contents

§3.4. Learning theory 78

§3.5. Highlight: the Goldreich–Levin Algorithm 82

§3.6. Exercises and notes 85

Chapter 4. DNF formulas and small-depth circuits 93

§4.1. DNF formulas 93

§4.2. Tribes 96

§4.3. Random restrictions 98

§4.4. Håstad’s Switching Lemma and the spectrum of DNFs 100

§4.5. Highlight: LMN’s work on constant-depth circuits 103

§4.6. Exercises and notes 107

Chapter 5. Majority and threshold functions 113

§5.1. Linear threshold functions and polynomial threshold functions 113

§5.2. Majority, and the Central Limit Theorem 118

§5.3. The Fourier coefﬁcients of Majority 121

§5.4. Degree-1 weight 124

§5.5. Highlight: Peres’s Theorem and uniform noise stability 130

§5.6. Exercises and notes 134

Chapter 6. Pseudorandomness and F 2-polynomials 143

§6.1. Notions of pseudorandomness 143

§6.2. F 2-polynomials 148

§6.3. Constructions of various pseudorandom functions 151

§6.4. Applications in learning and testing 155

§6.5. Highlight: Fooling F 2-polynomials 160

§6.6. Exercises and notes 163

Chapter 7. Property testing, PCPPs, and CSPs 173

§7.1. Dictator testing 173

§7.2. Probabilistically Checkable Proofs of Proximity 178

§7.3. CSPs and computational complexity 183

§7.4. Highlight: Håstad’s hardness theorems 190

§7.5. Exercises and notes 195

Chapter 8. Generalized domains 207

§8.1. Fourier bases for product spaces 207

§8.2. Generalized Fourier formulas 211

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Contents vii

§8.3. Orthogonal decomposition 216

§8.4. p-biased analysis 220

§8.5. Abelian groups 227

§8.6. Highlight: Randomized decision tree complexity 229

§8.7. Exercises and notes 235

Chapter 9. Basics of hypercontractivity 247

§9.1. Low-degree polynomials are reasonable 248

§9.2. Small subsets of the hypercube are noise-sensitive 252

§9.3. (2, q)- and (p, 2)-hypercontractivity for a single bit 256

§9.4. Two-function hypercontractivity and induction 259

§9.5. Applications of hypercontractivity 262

§9.6. Highlight: The Kahn–Kalai–Linial Theorem 264

§9.7. Exercises and notes 270

Chapter 10. Advanced hypercontractivity 283

§10.1. The Hypercontractivity Theorem for uniformly random bits 283

§10.2. Hypercontractivity of general random variables 287

§10.3. Applications of general hypercontractivity 292

§10.4. More on randomization/symmetrization 297

§10.5. Highlight: General sharp threshold theorems 304

§10.6. Exercises and notes 312

Chapter 11. Gaussian space and Invariance Principles 327

§11.1. Gaussian space and the Gaussian noise operator 328

§11.2. Hermite polynomials 336

§11.3. Borell’s Isoperimetric Theorem 340

§11.4. Gaussian surface area and Bobkov’s Inequality 343

§11.5. The Berry–Esseen Theorem 350

§11.6. The Invariance Principle 357

§11.7. Highlight: Majority Is Stablest Theorem 364

§11.8. Exercises and notes 370

Some tips 389

Bibliography 391

Index 413

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Prefaces

Preface to the arXiv edition

The purpose of this May 2021 revision is to ﬁx 100+ small typos and er-
rors present in the ﬁrst edition, and to make the result available on arXiv.
The numbering of all theorems, deﬁnitions, exercises, etc. is unchanged; there
are only slight pagination differences. Essentially no new mathematical con-
tent has been added, despite plenty of progress in the ﬁeld; the book can be
considered a “snapshot” of analysis of Boolean functions circa 2014.

Preface to the ﬁrst edition

The subject of this textbook is the analysis of Boolean functions. Roughly
speaking, this refers to studying Boolean functions f : {0, 1}n → {0, 1} via their
Fourier expansion and other analytic means. Boolean functions are perhaps
the most basic object of study in theoretical computer science, and Fourier
analysis has become an indispensable tool in the ﬁeld. The topic has also
played a key role in several other areas of mathematics, from combinatorics,
random graph theory, and statistical physics, to Gaussian geometry, met-
ric/Banach spaces, and social choice theory.

The intent of this book is both to develop the foundations of the ﬁeld and
to give a wide (though far from exhaustive) overview of its applications. Each
chapter ends with a “highlight” showing the power of analysis of Boolean
functions in different subject areas: property testing, social choice, cryptog-
raphy, circuit complexity, learning theory, pseudorandomness, hardness of
approximation, concrete complexity, and random graph theory.
 ix

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

x Prefaces

The book can be used as a reference for working researchers or as the basis
of a one-semester graduate-level course. The author has twice taught such a
course at Carnegie Mellon University, attended mainly by graduate students
in computer science and mathematics but also by advanced undergraduates,
postdocs, and researchers in adjacent ﬁelds. In both years most of Chapters 1–
5 and 7 were covered, along with parts of Chapters 6, 8, 9, and 11, and
some additional material on additive combinatorics. Nearly 500 exercises are
provided at the ends of the book’s chapters.

Acknowledgments

My foremost acknowledgment is to all of the people who have taught me
analysis of Boolean functions, especially Guy Kindler and Elchanan Mossel.
I also learned a tremendous amount from my advisor Madhu Sudan, and my
coauthors and colleagues Per Austrin, Eric Blais, Nader Bshouty, Ilias Di-
akonikolas, Irit Dinur, Uri Feige, Ehud Friedgut, Parikshit Gopalan, Venkat
Guruswami, Johan Håstad, Gil Kalai, Daniel Kane, Subhash Khot, Adam
Klivans, James Lee, Assaf Naor, Joe Neeman, Krzysztof Oleszkiewicz, Yuval
Peres, Oded Regev, Mike Saks, Oded Schramm, Rocco Servedio, Amir Shpilka,
Jeff Steif, Benny Sudakov, Li-Yang Tan, Avi Wigderson, Karl Wimmer, John
Wright, Yi Wu, Yuan Zhou, and many others. Ideas from all of them have
strongly informed this book.

Many thanks to my PhD students who suffered from my inattention dur-
ing the completion of this book: Eric Blais, Yuan Zhou, John Wright, and
David Witmer. I’d also like to thank the students who took my 2007 and 2012
courses on analysis of Boolean functions; special thanks to Deepak Bal, Carol
Wang, and Patrick Xia for their very helpful course writing projects.

Thanks to my editor Lauren Cowles for her patience and encouragement,
to the copyediting team of David Anderson and Rishi Gupta, and to Cam-
bridge University Press for welcoming the free online publication of this book.
Thanks also to Amanda Williams for the use of the cover image.

I’m very grateful to everyone who pointed out errors in earlier drafts of
this work: Amirali Abdullah, Stefan Alders, anon, Arda Antikacıo ˘glu, Albert
Atserias, Per Austrin, Deepak Bal, Paul Beame, Tim Black, Ravi Boppana,
Clément Canonne, Yongzhi Cao, Sankardeep Chakraborty, Bireswar Das, An-
drew Drucker, Kirill Elagin, John Engbers, Diodato Ferraioli, Magnus Find,
Michael Forbes, Malin Forsström, Matt Franklin, David Gajser, David García
Soriano, Dmitry Gavinsky, Daniele Gewurz, Mrinalkanti Ghosh, Sivakanth
Gopi, Tom Gur, Zachary Hamaker, Sean Harrap, Prahladh Harsha, Justin
Hilyard, Dmitry Itsykson, Hamidreza Jahanjou, Mitchell Johnston, Gautam

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Prefaces xi

Kamath, Shiva Kaul, Brian Kell, Ohad Klein, Pravesh Kothari, Chin Ho
Lee, Euiwoong Lee, Holden Lee, Jerry Li, Noam Lifshitz, Chengyu Lin, Yang
Liu, Tengyu Ma, Mladen Mikša, Alexey Milovanov, Sidhanth Mohanty, Ash-
ley Montanaro, Tobias Müller, Aleksandar Nikolov, Krzysztof Oleszkiewicz,
Pavithra KS, David Pritchard, Juspreet Sandhu, Swagato Sanyal, Pranav
Senthilnathan, Igor Shinkar, Lior Silberman, Marla Slusky, Dmitry Sokolov,
Aravind Srinivasan, Jeffrey Steif, Avishay Tal, Li-Yang Tan, Roei Tell, Suresh
Venkatasubramanian, Marc Vinyals, Emanuele Viola, Poorvi Vora, Amos Wa-
terland, Jake Wellens, Ryan Williams, Karl Wimmer, Chung Hoi Wong, Xi
Wu, Yi Wu, Mingji Xia, Yuichi Yoshida, Shengyu Zhang, Yu Zhao, and Art-
sem Zhuk. Special thanks in this group to Matt Franklin and Li-Yang Tan;
extra-special thanks in this group to Noam Lifshitz and Jeff Steif.

I’m grateful to Denis Thérien for inviting me to lecture at the Barbados
Complexity Workshop, to Cynthia Dwork and the STOC 2008 PC for inviting
me to give a tutorial, and to the Simons Foundation who arranged for me
to co-organize a symposium together with Elchanan Mossel and Krzysztof
Oleskiewicz, all on the topic of analysis of Boolean functions. These opportu-
nities greatly helped me to crystallize my thoughts on the topic.

I worked on this book while visiting the Institute for Advanced Study in
2010–2011 (supported by the Von Neumann Fellowship and in part by NSF
grants DMS-0835373 and CCF-0832797); I’m very grateful to them for having
me and for the wonderful working environment they provided. The remain-
der of the work on this book was done at Carnegie Mellon; I’m of course very
thankful to my colleagues there and to the Department of Computer Science.
“Reasonable” random variables were named after the department’s “Reason-
able Person Principle”. I was also supported in this book-writing endeavor
by the National Science Foundation, speciﬁcally grants CCF-0747250 and
CCF-1116594. As usual: “This material is based upon work supported by the
National Science Foundation under grant numbers listed above. Any opinions,
ﬁndings and conclusions or recommendations expressed in this material are
those of the author and do not necessarily reﬂect the views of the National
Science Foundation (NSF).”

Finally, I’d like to thank all of my colleagues, friends, and relatives who
encouraged me to write and to ﬁnish the book, Zeynep most of all.

– Ryan O’Donnell
Pittsburgh
October 2013

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

List of Notation

◦ entry-wise multiplication of vectors

∇ the gradient: ∇ f (x) = (D1 f (x), . . . , Dn f (x))

¬ logical NOT

∋ S ∋ i is equivalent to i ∈ S

⊕ logical XOR (exclusive-or)
ˆ∥ f ˆ∥p (
∑
γ∈ ̂F n
2 | ̂f (γ)|p)
1/p

△ symmetric difference of sets;
i.e., S△T = {i : i is in exactly one of S, T}

∨ logical OR

∧ logical AND

∗ the convolution operator

[zk]F(z) coefﬁcient on zk in the power series F(z)

1A 0-1 indicator function for A

1B 0-1 indicator random variable for event B

2A the set of all subsets of A

#α if α is a multi-index, denotes the number of nonzero com-
ponents of α

|α| if α is a multi-index, denotes ∑i αi

ANDn the logical AND function on n bits: False unless all inputs
are True

A⊥ {γ : γ · x = 0 for all x ∈ A}

Aut( f ) the group of automorphisms of Boolean function f
 xiii

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

xiv List of Notation

BitsToGaussiansd
M on input the bit matrix x ∈ {−1, 1}d×M, has output z ∈ R d

equal to 1pM times the column-wise sum of x; if d is omitted
it’s taken to be 1

C the complex numbers

χ(b) when b ∈ F n
2 , denotes (−1)b ∈ R

χS(x) when x ∈ R n, denotes ∏i∈S xi, where S ⊆ [n]; when x ∈ F n
2 ,
denotes (−1)
∑i∈S xi

codim H for a subspace H ≤ F n, denotes n − dim H

Cov[ f , g] the covariance of f and g, Cov[ f ] = E[ f g] − E[ f ] E[g]

Di the ith discrete derivative: Di f (x) = f (x(i7→1))− f (x(i7→−1))
2
dχ2(ϕ, 1) chi-squared distance of the distribution with density ϕ from
the uniform distribution

deg( f ) the degree of f ; the least k such that f is a real linear
combination of k-juntas

degF 2( f ) for Boolean-valued f , the degree of its F 2-polynomial rep-
resentation

∆(x, y) the Hamming distance, #{i : xi ̸= yi}

∆
(π)( f ) the expected number of queries made by the best decision
tree computing f when the input bits are chosen from the
distribution π

δ(π)( f ) the revealment of f ; i.e., min{maxi δ(π)
i (T ) : T computes f }

∆
(π)(T ) the expected number of queries made by randomized deci-
sion tree T when the input bits are chosen from the distri-
bution π

δ(π)
i (T ) the probability randomized decision tree T queries coor-
dinate i when the input bits are chosen from the distribu-
tion π

∆y f for f : F n
2 → F 2, the function F n
2 → F 2 deﬁned by ∆y f (x) =
f (x + y) − f (x)

dist(g, h) the relative Hamming distance; i.e., the fraction of inputs
on which g and h disagree

DNFsize( f ) least possible size of a DNF formula computing f

DNFwidth( f ) least possible width of a DNF formula computing f

DT( f ) least possible depth of a decision tree computing f

DTsize( f ) least possible size of a decision tree computing f

dTV(ϕ, ψ) total variation distance between the distributions with den-
sities ϕ, ψ

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

List of Notation xv

Ei the ith expectation operator:
Ei f (x) = Exi [ f (x1, . . . , xi−1, xi, xi+1, . . . , xn))]

EI the expectation over coordinates I operator

Ent[ f ] for a nonnegative function on a probability space, denotes
E[ f ln f ] − E[ f ] ln E[ f ]

Eπp [·] an abbreviation for Ex∼π⊗n
p [·]

f ⊕ g if f : {−1, 1}m → {−1, 1} and g : {−1, 1}n → {−1, 1}, denotes
the function h : {−1, 1}m+n → {−1, 1} deﬁned by h(x, y) =
f (x)g(y)

f ⊗ g if f : {−1, 1}m → {−1, 1} and g : {−1, 1}n → {−1, 1}, denotes the
function h : {−1, 1}mn → {−1, 1} deﬁned by h(x(1), . . . , x(m)) =
f (g(x(1)), . . . , g(x(m)))

f ⊗d if f : {−1, 1}n → {−1, 1}, then f ⊗d : {−1, 1}nd → {−1, 1} is de-
ﬁned inductively by f ⊗1 = f , f ⊗(d+1) = f ⊗ f ⊗d

f ∗n the n-fold convolution, f ∗ f ∗ · · · ∗ f

f † the Boolean dual deﬁned by f †(x) = − f (−x)

f +z if f : F n
2 → R , z ∈ F n
2 , denotes the function f +z(x) = f (x + z)

f +z
H denotes ( f +z)H
F 2 the ﬁnite ﬁeld of size 2
̂F n
2 the group (vector space) indexing the Fourier characters of
functions f : F n
2 → R

f even the even part of f , ( f (x) + f (−x))/2

〈 f , g〉 Ex[ f (x)g(x)]

f H if f : F n
2 → R , H ≤ F n
2 , denotes the restriction of f to H

̂f (i) shorthand for ̂f ({i}) when i ∈ N

f ⊆J the function (depending only on the J coordinates) deﬁned
by f ⊆J(x) = Ex′
J [ f (xJ, x′
J)]; in particular, it’s ∑S⊆J ̂f (S)χS
when f : {−1, 1}n → R

f|z if f : Ωn → R , J ⊆ [n], and z ∈ ΩJ, denotes the restriction of
f given by ﬁxing the coordinates in J to z

f J|z if f : Ωn → R , J ⊆ [n], and z ∈ ΩJ, denotes the restriction
of f given by ﬁxing the coordinates in J to z

f =k ∑
|S|=k ̂f (S) χS

f ≤k ∑
|S|≤k ̂f (S) χS

f odd the odd part of f , ( f (x) − f (−x))/2

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

xvi List of Notation

F pℓ for p prime and ℓ ∈ N +, denotes the ﬁnite ﬁeld of pℓ ele-
ments
̂f (S) the Fourier coefﬁcient of f on character χS
FS|J f (z) for S ⊆ J ⊆ [n], denotes ̂f J|z(S)

̃f the randomization/symmetrization of f , deﬁned by ̃f (r, x) =
∑S rS f =S(x)

γ
+(∂A) the Gaussian Minkowski content of ∂A

G (v, p) the Erd˝os–Rényi random graph distribution, π⊗(v
2)
p

h j the jth (normalized) Hermite polynomial, h j = 1p j! H j

hα for α ∈ N n a multi-index, the n-variate (normalized) Her-
mite polynomial hα(z) = ∏n
j=1 hα j (z j)

H j the jth probabilists’ Hermite polynomial, deﬁned by exp(tz−
1
2 t2) = ∑∞
j=0 1
j! H j(z)t j

Infi[ f ] the inﬂuence of coordinate i on f

Inf(ρ)
i [ f ] the ρ-stable inﬂuence, Stabρ[Di f ]

˜InfJ[ f ] the coalitional inﬂuence of J ⊆ [n] on f : {−1, 1}n → {−1, 1},
namely Prz∼{−1,1}J [ f J|z is not constant]

˜Inf b
J[ f ] for b ∈ {−1, 1}, equals Prz∼{−1,1}J [ f J|z ̸≡ −b] − Pr[ f = b]

J if J ⊆ [n], denotes [n] \ J

L2({−1, 1}n) denotes L2({−1, 1}n, π⊗n
1/2)

L2(G n) if G is a ﬁnite abelian group, denotes the complex inner
product space of functions G n → R with inner product 〈 f , g〉 =
Ex∼G n [ f (x)g(x)]

L2(Ω, π) the inner product space of (square-integrable) functions
Ω → R with inner product 〈 f , g〉 = Ex∼π[ f (x)g(x)]

Λρ(α, β) Pr[z1 ≤ t, z2 ≤ t′], where z1, z2 are standard Gaussians
with correlation E[z1 z2] = ρ, and t = Φ−1(α), t′ = Φ−1(β)

Λρ(α) denotes Λρ(α, α)

L f the Laplacian operator applied to the Boolean function f ,
deﬁned by L f = ∑n
i=1 Li f (or, the Ornstein–Uhlenbeck oper-
ator if f is a function on Gaussian space)

Li the ith coordinate Laplacian operator: Li f = f − Ei f

ln x loge x

log x log2 x

Majn the majority function on n bits

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

List of Notation xvii

MaxInf[ f ] maxi{Infi[ f ]}

[n] {1, 2, 3, . . . , n}

N {0, 1, 2, 3, . . . }

N + {1, 2, 3, . . . }

N <m {0, 1, . . . , m − 1}

Nρ(x) when x ∈ {−1, 1}n, denotes the probability distribution gen-
erating a string ρ-correlated to x

Nρ(z) when z ∈ R n, denotes the probability distribution of ρz +
√
1 − ρ2 g where g ∼ N(0, 1)n

NSδ[ f ] the noise sensitivity of f at δ; i.e., 1
2 − 1
2 Stab1−2δ[ f ]

N(0, 1) the standard Gaussian distribution

N(0, 1)d the distribution of d independent standard Gaussians; i.e.,
N(0, I d×d)

N(µ, Σ) for µ ∈ R d and Σ ∈ R d×d positive semideﬁnite, the d-variate
Gaussian distribution with mean µ and covariance ma-
trix Σ

ORn the logical OR function on n bits: True unless all inputs are
False

φ the standard Gaussian pdf, φ(z) = 1p
2π e−z2/2

Φ the standard Gaussian cdf, Φ(t) = ∫ t
−∞ φ(z) dz

Φ the standard Gaussian complementary cdf, Φ(t) = ∫ ∞
t φ(z) dz

ϕA the density function for the uniform probability distribu-
tion on A; i.e., 1A/ E[1A]

φα given functions φ0, . . . , φm−1 and a multi-index α, denotes
∏n
i=1 φαi
π⊗n if π is a probability distribution on Ω, denotes the associ-
ated product probability distribution on Ωn

π1/2 the uniform distribution on {−1, 1}

πp the “p-biased” distribution on bits: πp(−1) = p, πp(1) = 1− p

Prπp [·] an abbreviation for Prx∼π⊗n
p [·]

R the real numbers

R ≥0 the nonnegative real numbers

RDT( f ) the zero-error randomized decision tree complexity of f

RSA(δ) the rotation sensitivity of A at δ; i.e., Pr[1A(z) ̸= 1A(z′)] for
a cos δ-correlated pair (z, z′)

sens f (x) the number of pivotal coordinates for f at x

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

xviii List of Notation

sgn(t) +1 if t ≥ 0, −1 if t < 0

Sn the symmetric group on [n]

sparsity( f ) Prx[ f (x) ̸= 0]

sparsity( ̂f ) |supp( ̂f )|

Stabρ[ f ] the noise stability of f at ρ: E[ f (x) f (y)] where x, y are a
ρ-correlated pair

supp(α) if α is a multi-index, denotes {i : αi ̸= 0}

supp( f ) if f is a function, denotes the set of inputs where f is
nonzero

Tρ the noise operator: Tρ f (x) = Ey∼Nρ(x)[ f (y)]

Ti
ρ the operator deﬁned by Ti
ρ f (x) = ρ f + (1 − ρ)Ei f

Tr for r ∈ R n, denotes the operator deﬁned by T
1
r1T2
r2 · · · Tn
r n
U the Gaussian isoperimetric function, U = φ ◦ Φ−1

Uρ the Gaussian noise operator: Uρ f (z) = Ez′∼Nρ(z)[ f (z′)]

Var[ f ] the variance of f , Var[ f ] = E[ f 2] − E[ f ]
2

Vari the operator deﬁned by
Vari f (x) = Varxi [ f (x1, . . . , xi−1, xi, xi+1, . . . , xn))]

volγ(A) Prz∼N(0,1)n [z ∈ A], the Gaussian volume of A

Wk[ f ] the Fourier weight of f at degree k

W
>k[ f ] the Fourier weight of f at degrees above k

x(i7→b) the string (x1, . . . , xi−1, b, xi+1, . . . , xn)

x⊕i (x1, . . . , xi−1, −xi, xi+1, . . . , xn)

x ∼ ϕ the random variable x is chosen from the probability distri-
bution with density ϕ

xS ∏i∈S xi, with the convention x; = 1

x ∼ A the random variable x is chosen uniformly from the set A

x ∼ {−1, 1}n the random variable x is chosen uniformly from {−1, 1}n

(y, z) if J ⊆ [n], y ∈ {−1, 1}J, z ∈ {−1, 1}J, denotes the natural com-
posite string in {−1, 1}n

Z the additive group of integers modulo m
̂Z n
m the group indexing the Fourier characters of functions f :
Z n
m → C

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 1

Boolean functions and
the Fourier expansion

In this chapter we describe the basics of analysis of Boolean functions. We
emphasize viewing the Fourier expansion of a Boolean function as its repre-
sentation as a real multilinear polynomial. The viewpoint based on harmonic
analysis over F n
2 is mostly deferred to Chapter 3. We illustrate the use of basic
Fourier formulas through the analysis of the Blum–Luby–Rubinfeld linearity
test.

1.1. On analysis of Boolean functions

This is a book about Boolean functions,

f : {0, 1}n → {0, 1}.

Here f maps each length-n binary vector, or string, into a single binary value,
or bit. Boolean functions arise in many areas of computer science and mathe-
matics. Here are some examples:

• In circuit design, a Boolean function may represent the desired behavior
of a circuit with n inputs and one output.

• In graph theory, one can identify v-vertex graphs G with length-(v
2
)

strings indicating which edges are present. Then f may represent a
property of such graphs; e.g., f (G) = 1 if and only if G is connected.

• In extremal combinatorics, a Boolean function f can be identiﬁed with
a “set system” F on [n] = {1, 2, . . . , n}, where sets X ⊆ [n] are identiﬁed
with their 0-1 indicators and X ∈ F if and only if f (X ) = 1.
 19

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

20 1. Boolean functions and the Fourier expansion

• In coding theory, a Boolean function might be the indicator function for
the set of messages in a binary error-correcting code of length n.

• In learning theory, a Boolean function may represent a “concept” with n
binary attributes.

• In social choice theory, a Boolean function can be identiﬁed with a “vot-
ing rule” for an election with two candidates named 0 and 1.

We will be quite ﬂexible about how bits are represented. Sometimes we
will use True and False; sometimes we will use −1 and 1, thought of as real
numbers. Other times we will use 0 and 1, and these might be thought of as
real numbers, as elements of the ﬁeld F 2 of size 2, or just as symbols. Most
frequently we will use −1 and 1, so a Boolean function will look like

f : {−1, 1}n → {−1, 1}.

But we won’t be dogmatic about the issue.

We refer to the domain of a Boolean function, {−1, 1}n, as the Hamming
cube (or hypercube, n-cube, Boolean cube, or discrete cube). The name “Ham-
ming cube” emphasizes that we are often interested in the Hamming distance
between strings x, y ∈ {−1, 1}n, deﬁned by

∆(x, y) = #{i : xi ̸= yi}.

Here we’ve used notation that will arise constantly: x denotes a bit string,
and xi denotes its ith coordinate.

Suppose you have a problem involving Boolean functions with the follow-
ing two characteristics:

• the Hamming distance is relevant;

• you are counting strings, or the uniform probability distribution on
{−1, 1}n is involved.

These are the hallmarks of a problem for which analysis of Boolean functions
may help. Roughly speaking, this means deriving information about Boolean
functions by analyzing their Fourier expansion.

1.2. The “Fourier expansion”: functions as multilinear
polynomials

The Fourier expansion of a Boolean function f : {−1, 1}n → {−1, 1} is simply
its representation as a real, multilinear polynomial. (Multilinear means that
no variable xi appears squared, cubed, etc.) For example, suppose n = 2 and

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.2. The “Fourier expansion”: functions as multilinear polynomials 21

f = max2, the “maximum” function on 2 bits:

max2(+1, +1) = +1,
max2(−1, +1) = +1,
max2(+1, −1) = +1,
max2(−1, −1) = −1.

Then max2 can be expressed as a multilinear polynomial,

max2(x1, x2) = 1
2 + 1
2 x1 + 1
2 x2 − 1
2 x1x2; (1.1)

this is the “Fourier expansion” of max2. As another example, consider the
majority function on 3 bits, Maj3 : {−1, 1}
3 → {−1, 1}, which outputs the ±1 bit
occurring more frequently in its input. Then it’s easy to verify the Fourier
expansion
 Maj3(x1, x2, x3) = 1
2 x1 + 1
2 x2 + 1
2 x3 − 1
2 x1x2x3. (1.2)

The functions max2 and Maj3 will serve as running examples in this chapter.

Let’s see how to obtain such multilinear polynomial representations in
general. Given an arbitrary Boolean function f : {−1, 1}n → {−1, 1} there is a
familiar method for ﬁnding a polynomial that interpolates the 2n values that
f assigns to the points {−1, 1}n ⊂ R n. For each point a = (a1, . . . , an) ∈ {−1, 1}n

the indicator polynomial

1{a}(x) = ( 1+a1 x1
2
 ) ( 1+a2 x2
2
 ) · · · ( 1+an xn
2
 )

takes value 1 when x = a and value 0 when x ∈ {−1, 1}n \ {a}. Thus f has the
polynomial representation

f (x) = ∑

a∈{−1,1}n f (a)1{a}(x).

Illustrating with the f = max2 example again, we have

max2(x) = (+1) ( 1+x1
2
 ) ( 1+x2
2
 )

+ (+1) ( 1−x1
2
 ) ( 1+x2
2
 ) (1.3)

+ (+1) ( 1+x1
2
 ) ( 1−x2
2
 )

+ (−1) ( 1−x1
2
 ) ( 1−x2
2
 ) = 1
2 + 1
2 x1 + 1
2 x2 − 1
2 x1x2.

Let us make two remarks about this interpolation procedure. First, it works
equally well in the more general case of real-valued Boolean functions, f :
{−1, 1}n → R . Second, since the indicator polynomials are multilinear when
expanded out, the interpolation always produces a multilinear polynomial.
Indeed, it makes sense that we can represent functions f : {−1, 1}n → R with
multilinear polynomials: since we only care about inputs x where xi = ±1, any
factor of x2
i can be replaced by 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

22 1. Boolean functions and the Fourier expansion

We have illustrated that every f : {−1, 1}n → R can be represented by a
real multilinear polynomial; as we will see in Section 1.3, this representation
is unique. The multilinear polynomial for f may have up to 2n terms, corre-
sponding to the subsets S ⊆ [n]. We write the monomial corresponding to S
as
 xS = ∏

i∈S xi (with x; = 1 by convention),

and we use the following notation for its coefﬁcient:

̂f (S) = coefﬁcient on monomial xS in the multilinear representation of f .

This discussion is summarized by the Fourier expansion theorem:

Theorem 1.1. Every function f : {−1, 1}n → R can be uniquely expressed as a
multilinear polynomial, f (x) = ∑

S⊆[n] ̂f (S) xS. (1.4)

This expression is called the Fourier expansion of f , and the real number ̂f (S)
is called the Fourier coefﬁcient of f on S. Collectively, the coefﬁcients are
called the Fourier spectrum of f .

As examples, from (1.1) and (1.2) we obtain:

…max2(;) = 1
2 , …max2({1}) = 1
2 , …max2({2}) = 1
2 , …max2({1, 2}) = − 1
2 ;

†Maj3({1}), †Maj3({2}), †Maj3({3}) = 1
2 , †Maj3({1, 2, 3}) = − 1
2 , †Maj3(S) = 0 else.

We ﬁnish this section with some notation. It is convenient to think of the
monomial xS as a function on x = (x1, . . . , xn) ∈ R n; we write it as

χS(x) = ∏

i∈S xi.

Thus we sometimes write the Fourier expansion of f : {−1, 1}n → R as

f (x) = ∑

S⊆[n] ̂f (S) χS(x).

So far our notation makes sense only when representing the Hamming cube
by {−1, 1}n ⊆ R n. The other frequent representation we will use for the cube
is F n
2 . We can deﬁne the Fourier expansion for functions f : F n
2 → R by
“encoding” input bits 0, 1 ∈ F 2 by the real numbers −1, 1 ∈ R . We choose the
encoding χ : F 2 → R deﬁned by

χ(0F 2) = +1, χ(1F 2) = −1.

This encoding is not so natural from the perspective of Boolean logic; e.g., it
means the function max2 we have discussed represents logical AND. But it’s
mathematically natural because for b ∈ F 2 we have the formula χ(b) = (−1)b.
We now extend the χS notation:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.3. The orthonormal basis of parity functions 23

Deﬁnition 1.2. For S ⊆ [n] we deﬁne χS : F n
2 → R by

χS(x) = ∏

i∈S χ(xi) = (−1)
∑i∈S xi ,

which satisﬁes χS(x + y) = χS(x)χS(y). (1.5)

In this way, given any function f : F n
2 → R it makes sense to write its
Fourier expansion as f (x) = ∑

S⊆[n] ̂f (S) χS(x).

In fact, if we are really thinking of F n
2 the n-dimensional vector space over
F 2, it makes sense to identify subsets S ⊆ [n] with vectors γ ∈ F n
2 . This will
be discussed in Chapter 3.2.

1.3. The orthonormal basis of parity functions

For x ∈ {−1, 1}n, the number χS(x) = ∏i∈S xi is in {−1, 1}. Thus χS : {−1, 1}n →
{−1, 1} is a Boolean function; it computes the logical parity, or exclusive-or
(XOR), of the bits (xi)i∈S. The parity functions play a special role in the
analysis of Boolean functions: the Fourier expansion

f = ∑

S⊆[n] ̂f (S) χS (1.6)

shows that any f can be represented as a linear combination of parity func-
tions (over the reals).

It’s useful to explore this idea further from the perspective of linear alge-
bra. The set of all functions f : {−1, 1}n → R forms a vector space V , since we
can add two functions (pointwise) and we can multiply a function by a real
scalar. The vector space V is 2n-dimensional: if we like we can think of the
functions in this vector space as vectors in R 2n , where we stack the 2n values
f (x) into a tall column vector (in some ﬁxed order). Here we illustrate the
Fourier expansion (1.1) of the max2 function from this perspective:

max2 =
 






+1
+1
+1
−1






 = (1/2)
 






+1
+1
+1
+1





 + (1/2)
 






+1
−1
+1
−1





 + (1/2)
 






+1
+1
−1
−1





 + (−1/2)
 






+1
−1
−1
+1






 . (1.7)

More generally, the Fourier expansion (1.6) shows that every function
f : {−1, 1}n → R in V is a linear combination of the parity functions; i.e., the
parity functions are a spanning set for V . Since the number of parity functions
is 2n = dim V , we can deduce that they are in fact a linearly independent basis
for V . In particular this justiﬁes the uniqueness of the Fourier expansion
stated in Theorem 1.1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

24 1. Boolean functions and the Fourier expansion

We can also introduce an inner product on pairs of function f , g : {−1, 1}n →
R in V . The usual inner product on R 2n would correspond to ∑x∈{−1,1}n f (x)g(x),
but it’s more convenient to scale this by a factor of 2
−n, making it an average
rather than a sum. In this way, a Boolean function f : {−1, 1}n → {−1, 1} will
have 〈 f , f 〉 = 1, i.e., be a “unit vector”.

Deﬁnition 1.3. We deﬁne an inner product 〈·, ·〉 on pairs of function f , g :
{−1, 1}n → R by

〈 f , g〉 = 2−n ∑

x∈{−1,1}n f (x)g(x) = E
x∼{−1,1}n [ f (x)g(x)] . (1.8)

We also use the notation ∥ f ∥2 = √〈 f , f 〉, and more generally,

∥ f ∥p = E[| f (x)|p]
1/p.

Here we have introduced probabilistic notation that will be used heavily
throughout the book:

Notation 1.4. We write x ∼ {−1, 1}n to denote that x is a uniformly chosen ran-
dom string from {−1, 1}n. Equivalently, the n coordinates xi are independently
chosen to be +1 with probability 1/2 and −1 with probability 1/2. We always
write random variables in boldface. Probabilities Pr and expectations E will
always be with respect to a uniformly random x ∼ {−1, 1}n unless otherwise
speciﬁed. Thus we might write the expectation in (1.8) as Ex[ f (x)g(x)] or
E[ f (x)g(x)] or even E[ f g].

Returning to the basis of parity functions for V , the crucial fact underlying
all analysis of Boolean functions is that this is an orthonormal basis.

Theorem 1.5. The 2n parity functions χS : {−1, 1}n → {−1, 1} form an orthonor-
mal basis for the vector space V of functions {−1, 1}n → R ; i.e.,

〈χS, χT 〉 =
 {
1 if S = T,

0 if S ̸= T.

Recalling the deﬁnition 〈χS, χT 〉 = E[χS(x)χT (x)], Theorem 1.5 follows imme-
diately from two facts:

Fact 1.6. For x ∈ {−1, 1}n it holds that χS(x)χT (x) = χS△T (x), where S△T
denotes symmetric difference.

Proof. χS(x)χT (x) = ∏

i∈S xi ∏

i∈T xi = ∏

i∈S△T xi ∏

i∈S∩T x2
i = ∏

i∈S△T xi = χS△T (x). □

Fact 1.7. E[χS(x)] = E
[ ∏

i∈S xi] =
 {
1 if S = ;,

0 if S ̸= ;.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.4. Basic Fourier formulas 25

Proof. If S = ; then E[χS(x)] = E[1] = 1. Otherwise,

E
[ ∏

i∈S xi] = ∏

i∈S E[xi]

because the random bits x1, . . . , xn are independent. But each of the factors
E[xi] in the above (nonempty) product is (1/2)(+1) + (1/2)(−1) = 0. □

1.4. Basic Fourier formulas

As we have seen, the Fourier expansion of f : {−1, 1}n → R can be thought
of as the representation of f over the orthonormal basis of parity functions
(χS)S⊆[n]. In this basis, f has 2n “coordinates”, and these are precisely the
Fourier coefﬁcients of f . The “coordinate” of f in the χS “direction” is 〈 f , χS〉;
i.e., we have the following formula for Fourier coefﬁcients:

Proposition 1.8. For f : {−1, 1}n → R and S ⊆ [n], the Fourier coefﬁcient of f
on S is given by ̂f (S) = 〈 f , χS〉 = E
x∼{−1,1}n[ f (x)χS(x)].

We can verify this formula explicitly:

〈 f , χS〉 =
 〈 ∑

T⊆[n] ̂f (T) χT , χS
〉
 = ∑

T⊆[n] ̂f (T)〈χT , χS〉 = ̂f (S), (1.9)

where we used the Fourier expansion of f , the linearity of 〈·, ·〉, and ﬁnally
Theorem 1.5. This formula is the simplest way to calculate the Fourier coef-
ﬁcients of a given function; it can also be viewed as a streamlined version of
the interpolation method illustrated in (1.3). Alternatively, this formula can
be taken as the deﬁnition of Fourier coefﬁcients.

The orthonormal basis of parities also lets us measure the squared “length”
(2-norm) of f : {−1, 1}n → R efﬁciently: it’s just the sum of the squares of f ’s
“coordinates” – i.e., Fourier coefﬁcients. This simple but crucial fact is called
Parseval’s Theorem.

Parseval’s Theorem. For any f : {−1, 1}n → R ,

〈 f , f 〉 = E
x∼{−1,1}n[ f (x)
2] = ∑

S⊆[n] ̂f (S)2.

In particular, if f : {−1, 1}n → {−1, 1} is Boolean-valued then
∑

S⊆[n] ̂f (S)
2 = 1.

As examples we can recall the Fourier expansions of max2 and Maj3:

max2(x) = 1
2 + 1
2 x1 + 1
2 x2 − 1
2 x1x2, Maj3(x) = 1
2 x1 + 1
2 x2 + 1
2 x3 − 1
2 x1x2x3.

In both cases the sum of squares of Fourier coefﬁcients is 4 × (1/4) = 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

26 1. Boolean functions and the Fourier expansion

More generally, given two functions f , g : {−1, 1}n → R , we can compute
〈 f , g〉 by taking the “dot product” of their coordinates in the orthonormal basis
of parities. The resulting formula is called Plancherel’s Theorem.

Plancherel’s Theorem. For any f , g : {−1, 1}n → R ,

〈 f , g〉 = E
x∼{−1,1}n[ f (x)g(x)] = ∑

S⊆[n] ̂f (S) ̂g(S).

We can verify this formula explicitly as we did in (1.9):

〈 f , g〉 = 〈 ∑

S⊆[n] ̂f (S) χS, ∑

T⊆[n] ̂g(T) χT 〉 = ∑

S,T⊆[n] ̂f (S) ̂g(T)〈χS, χT 〉 = ∑

S⊆[n] ̂f (S) ̂g(S).

Now is a good time to remark that for Boolean-valued functions f , g :
{−1, 1}n → {−1, 1}, the inner product 〈 f , g〉 can be interpreted as a kind of “cor-
relation” between f and g, measuring how similar they are. Since f (x)g(x) = 1
if f (x) = g(x) and f (x)g(x) = −1 if f (x) ̸= g(x), we have:

Proposition 1.9. If f , g : {−1, 1}n → {−1, 1},

〈 f , g〉 = Pr[ f (x) = g(x)] − Pr[ f (x) ̸= g(x)] = 1 − 2dist( f , g).

Here we are using the following deﬁnition:

Deﬁnition 1.10. Given f , g : {−1, 1}n → {−1, 1}, we deﬁne their (relative Ham-
ming) distance to be dist( f , g) = Pr
x [ f (x) ̸= g(x)],

the fraction of inputs on which they disagree.

With a number of Fourier formulas now in hand we can begin to illustrate
a basic theme in the analysis of Boolean functions: interesting combinatorial
properties of a Boolean function f can be “read off ” from its Fourier coefﬁ-
cients. Let’s start by looking at one way to measure the “bias” of f :

Deﬁnition 1.11. The mean of f : {−1, 1}n → R is E[ f ]. When f has mean 0 we
say that it is unbiased, or balanced. In the particular case that f : {−1, 1}n →
{−1, 1} is Boolean-valued, its mean is

E[ f ] = Pr[ f = 1] − Pr[ f = −1];

thus f is unbiased if and only if it takes value 1 on exactly half of the points
of the Hamming cube.

Fact 1.12. If f : {−1, 1}n → R then E[ f ] = ̂f (;).

This formula holds simply because E[ f ] = 〈 f , 1〉 = ̂f (;) (taking S = ; in
Proposition 1.8). In particular, a Boolean function is unbiased if and only if
its empty-set Fourier coefﬁcient is 0.

Next we obtain a formula for the variance of a real-valued Boolean func-
tion (thinking of f (x) as a real-valued random variable):

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.4. Basic Fourier formulas 27

Proposition 1.13. The variance of f : {−1, 1}n → R is

Var[ f ] = 〈 f − E[ f ], f − E[ f ]〉 = E[ f 2] − E[ f ]2 = ∑

S̸=; ̂f (S)
2.

The above Fourier formula follows immediately from Parseval’s Theorem and
Fact 1.12. We also have:

Fact 1.14. For f : {−1, 1}n → {−1, 1},

Var[ f ] = 1 − E[ f ]
2 = 4 Pr[ f (x) = 1] Pr[ f (x) = −1] ∈ [0, 1].

In particular, a Boolean-valued function f has variance 1 if it’s unbiased
and variance 0 if it’s constant. More generally, the variance of a Boolean-
valued function is proportional to its “distance from being constant”.

Proposition 1.15. Let f : {−1, 1}n → {−1, 1}. Then 2ϵ ≤ Var[ f ] ≤ 4ϵ, where

ϵ = min{dist( f , 1), dist( f , −1)}.

The proof of Proposition 1.15 is an exercise. See also Exercise 1.17.

By using Plancherel in place of Parseval, we get a generalization of Propo-
sition 1.13 for covariance:

Proposition 1.16. The covariance of f , g : {−1, 1}n → R is

Cov[ f , g] = 〈 f − E[ f ], g − E[g]〉 = E[ f g] − E[ f ] E[g] = ∑

S̸=; ̂f (S) ̂g(S).

We end this section by discussing the Fourier weight distribution of Boolean
functions.

Deﬁnition 1.17. The (Fourier) weight of f : {−1, 1}n → R on set S is deﬁned
to be the squared Fourier coefﬁcient, ̂f (S)2.

Although we lose some information about the Fourier coefﬁcients when
we square them, many Fourier formulas only depend on the weights of f .
For example, Proposition 1.13 says that the variance of f equals its Fourier
weight on nonempty sets. Studying Fourier weights is particularly pleasant
for Boolean-valued functions f : {−1, 1}n → {−1, 1} since Parseval’s Theorem
says that they always have total weight 1. In particular, they deﬁne a proba-
bility distribution on subsets of [n].

Deﬁnition 1.18. Given f : {−1, 1}n → {−1, 1}, the spectral sample for f , de-
noted S f , is the probability distribution on subsets of [n] in which the set S
has probability ̂f (S)2. We write S ∼ S f for a draw from this distribution.

For example, the spectral sample for the max2 function is the uniform
distribution on all four subsets of [2]; the spectral sample for Maj3 is the
uniform distribution on the four subsets of [3] with odd cardinality.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

28 1. Boolean functions and the Fourier expansion

Given a Boolean function it can be helpful to try to keep a mental picture
of its weight distribution on the subsets of [n], partially ordered by inclu-
sion. Figure 1.1 is an example for the Maj3 function, with the white circles
indicating weight 0 and the shaded circles indicating weight 1/4.

[3]

{1,3} {2,3}{1,2}

{1} {2} {3}

Figure 1.1. Fourier weight distribution of the Maj3 function

Finally, as suggested by the diagram we often stratify the subsets S ⊆ [n]
according to their cardinality (also called “height” or “level”). Equivalently,
this is the degree of the associated monomial xS.

Deﬁnition 1.19. For f : {−1, 1}n → R and 0 ≤ k ≤ n, the (Fourier) weight of f
at degree k is Wk[ f ] = ∑

S⊆[n]
|S|=k
 ̂f (S)
2.

If f : {−1, 1}n → {−1, 1} is Boolean-valued, an equivalent deﬁnition is

Wk[ f ] = Pr
S∼S f [|S| = k].

By Parseval’s Theorem, Wk[ f ] = ∥ f =k∥
2
2 where

f =k = ∑

|S|=k ̂f (S) χS

is called the degree k part of f . We will also sometimes use notation like
W>k[ f ] = ∑
|S|>k ̂f (S)2 and f ≤k = ∑|S|≤k ̂f (S) χS.

1.5. Probability densities and convolution

For variety’s sake, in this section we write the Hamming cube as F n
2 rather
than {−1, 1}n. In developing the Fourier expansion, we have generalized from
Boolean-valued Boolean functions f : F n
2 → {−1, 1} to real-valued Boolean func-
tions f : F n
2 → R . Boolean-valued functions arise more often in combinatorial
problems, but there are important classes of real-valued Boolean functions.
One example is probability densities.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.5. Probability densities and convolution 29

Deﬁnition 1.20. A (probability) density function on the Hamming cube F n
2
is any nonnegative function ϕ : F n
2 → R ≥0 satisfying

E
x∼F n
2 [ϕ(x)] = 1.

We write y ∼ ϕ to denote that y is a random string drawn from the associated
probability distribution, deﬁned by

Pr
y∼ϕ
[y = y] = ϕ(y) 1
2n ∀y ∈ F n
2 .

Here you should think of ϕ(y) as being the relative density of y with
respect to the uniform distribution on F n
2 . For example, we have:

Fact 1.21. If ϕ is a density function and g : F n
2 → R , then

E
y∼ϕ
[g(y)] = 〈ϕ, g〉 = E
x∼F n
2 [ϕ(x)g(x)].

The simplest example of a probability density is just the constant func-
tion 1, which corresponds to the uniform probability distribution on F n
2 . The
most common case arises from the uniform distribution over some subset
A ⊆ F n
2 .

Deﬁnition 1.22. If A ⊆ F n
2 we write 1A : F n
2 → {0, 1} for the 0-1 indicator
function of A; i.e.,
 1A(x) =
 {1 if x ∈ A,

0 if x ∉ A.

Assuming A ̸= ; we write ϕA for the density function associated to the uni-
form distribution on A; i.e.,
 ϕA = 1
E[1A] 1A.

We typically write y ∼ A rather than y ∼ ϕA.

A simple but useful example is when A is the singleton set A = {0}. (Here 0
is denoting the vector (0, 0, . . . , 0) ∈ F n
2 .) In this case the function ϕ{0} takes
value 2n on input 0 ∈ F n
2 and is zero elsewhere on F n
2 . In Exercise 1.1 you will
verify the Fourier expansion of ϕ{0}:

Fact 1.23. Every Fourier coefﬁcient of ϕ{0} is 1; i.e., its Fourier expansion is

ϕ{0}(y) = ∑

S⊆[n] χS(y).

We now introduce an operation on functions that interacts particularly
nicely with density functions, namely, convolution.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

30 1. Boolean functions and the Fourier expansion

Deﬁnition 1.24. Let f , g : F n
2 → R . Their convolution is the function f ∗ g :
F n
2 → R deﬁned by

( f ∗ g)(x) = E
y∼F n
2 [ f (y)g(x − y)] = E
y∼F n
2 [ f (x − y)g(y)].

Since subtraction is equivalent to addition in F n
2 we may also write

( f ∗ g)(x) = E
y∼F n
2 [ f (y)g(x + y)] = E
y∼F n
2 [ f (x + y)g(y)].

If we were representing the Hamming cube by {−1, 1}n rather than F n
2 we
would replace x + y with x ◦ y, where ◦ denotes entry-wise multiplication.

Exercise 1.25 asks you to verify that convolution is associative and com-
mutative: f ∗ (g ∗ h) = ( f ∗ g) ∗ h, f ∗ g = g ∗ f .

Using Fact 1.21 we can deduce the following two simple results:

Proposition 1.25. If ϕ is a density function on F n
2 and g : F n
2 → R then

ϕ ∗ g(x) = E
y∼ϕ
[g(x − y)] = E
y∼ϕ
[g(x + y)].

In particular, Ey∼ϕ[g(y)] = ϕ ∗ g(0).

Proposition 1.26. If g = ψ is itself a probability density function then so is
ϕ ∗ ψ; it represents the distribution on x ∈ F n
2 given by choosing y ∼ ϕ and
z ∼ ψ independently and setting x = y + z.

The most important theorem about convolution is that it corresponds to
multiplication of Fourier coefﬁcients:

Theorem 1.27. Let f , g : F n
2 → R . Then for all S ⊆ [n],

†f ∗ g(S) = ̂f (S) ̂g(S).

Proof. We have

†f ∗ g(S) = E
x∼F n
2 [( f ∗ g)(x)χS(x)] (the Fourier formula)

= E
x∼F n
2
 [ E
y∼F n
2 [ f (y)g(x − y)]χS(x)
] (by deﬁnition)

= E
y,z∼F n
2
independently

[ f (y)g(z)χS(y + z)] (as x − y is uniform on F n
2 ∀x)

= E
y,z∼F n
2 [ f (y)χS(y)g(z)χS(z)] (by identity (1.5))

= ̂f (S) ̂g(S) (Fourier formula, independence),

as claimed. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.6. Highlight: Almost linear functions and the BLR Test 31

1.6. Highlight: Almost linear functions and the BLR Test

In linear algebra there are two equivalent deﬁnitions of what it means for a
function to be linear:

Deﬁnition 1.28. A function f : F n
2 → F 2 is linear if either of the following
equivalent conditions hold:

(1) f (x + y) = f (x) + f (y) for all x, y ∈ F n
2 ;

(2) f (x) = a · x for some a ∈ F n
2 ; i.e., f (x) = ∑i∈S xi for some S ⊆ [n].

Exercise 1.26 asks you to verify that the conditions are indeed equivalent.
If we encode the output of f by ±1 ∈ R in the usual way then the “linear”
functions f : F n
2 → {−1, 1} are precisely the 2n parity functions (χS)S⊆[n].

Let’s think of what it might mean for a function f : F n
2 → F 2 to be approx-
imately linear. Deﬁnition 1.28 suggests two possibilities:

(1
′) f (x + y) = f (x) + f (y) for almost all pairs x, y ∈ F n
2 ;

(2
′) there is some S ⊆ [n] such that f (x) = ∑i∈S xi for almost all x ∈ F n
2 .

Are these equivalent? The proof of (2) =⇒ (1) in Deﬁnition 1.28 is “robust”: it
easily extends to show (2
′) =⇒ (1
′) (see Exercise 1.26). But the natural proof
of (1) =⇒ (2) in Deﬁnition 1.28 does not have this robustness property. The
goal of this section is to show that (1
′) =⇒ (2
′) nevertheless holds.

Motivation for this problem comes from an area of theoretical computer
science called property testing, which we will discuss in more detail in Chap-
ter 7. Imagine that you have “black-box” access to a function f : F n
2 → F 2,
meaning that the function f is unknown to you but you can “query” its value
on inputs x ∈ F n
2 of your choosing. The function f is “supposed” to be a linear
function, and you would like to try to verify this.

The only way you can be certain f is indeed a linear function is to query
its value on all 2n inputs; unfortunately, this is very expensive. The idea
behind “property testing” is to try to verify that f has a certain property – in
this case, linearity – by querying its value on just a few random inputs. In
exchange for efﬁciency, we need to be willing to only approximately verify the
property.

Deﬁnition 1.29. If f and g are Boolean-valued functions we say they are
ϵ-close if dist( f , g) ≤ ϵ; otherwise we say they are ϵ-far. If P is a (nonempty)
property of n-bit Boolean functions we deﬁne dist( f , P ) = ming∈P {dist( f , g)}.
We say that f is ϵ-close to P if dist( f , P ) ≤ ϵ; i.e., f is ϵ-close to some g
satisfying P .
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

32 1. Boolean functions and the Fourier expansion

In particular, in property testing we take property (2
′) above to be the no-
tion of “approximately linear”: we say f is ϵ-close to being linear if dist( f , g) ≤ ϵ
for some truly linear g(x) = ∑i∈S xi.

In 1990 Blum, Luby, and Rubinfeld [BLR90] showed that indeed (1
′) =⇒
(2′) holds, giving the following “test” for the property of linearity that makes
just 3 queries:

BLR Test. Given query access to f : F n
2 → F 2:

• Choose x ∼ F n
2 and y ∼ F n
2 independently.

• Query f at x, y, and x + y.

• “Accept” if f (x) + f (y) = f (x + y).

We now show that if the BLR Test accepts f with high probability then
f is close to being linear. The proof works by directly relating the acceptance
probability to the quantity ∑S ̂f (S)
3; see equation (1.10) below.

Theorem 1.30. Suppose the BLR Test accepts f : F n
2 → F 2 with probability
1 − ϵ. Then f is ϵ-close to being linear.

Proof. In order to use the Fourier transform we encode f ’s output by ±1 ∈ R ;
thus the acceptance condition of the BLR Test becomes f (x) f (y) = f (x + y).
Since
 1
2 + 1
2 f (x) f (y) f (x + y) =
 {
1 if f (x) f (y) = f (x + y),

0 if f (x) f (y) ̸= f (x + y),

we conclude

1 − ϵ = Pr[BLR accepts f ] = E
x,y[ 1
2 + 1
2 f (x) f (y) f (x + y)]

= 1
2 + 1
2 E
x [ f (x) · E
y [ f (y) f (x + y)]]

= 1
2 + 1
2 E
x [ f (x) · ( f ∗ f )(x)] (by deﬁnition)

= 1
2 + 1
2 ∑

S⊆[n] ̂f (S) †f ∗ f (S) (Plancherel)

= 1
2 + 1
2 ∑

S⊆[n] ̂f (S)3 (Theorem 1.27).

We rearrange this equality and then continue:

1 − 2ϵ = ∑

S⊆[n] ̂f (S)
3 (1.10)

≤ max
S⊆[n]{ ̂f (S)} · ∑

S⊆[n] ̂f (S)
2

= max
S⊆[n]{ ̂f (S)} (Parseval).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.7. Exercises and notes 33

But ̂f (S) = 〈 f , χS〉 = 1 − 2dist( f , χS) (Proposition 1.9). Hence there exists some
S∗ ⊆ [n] such that 1−2ϵ ≤ 1−2dist( f , χS∗); i.e., f is ϵ-close to the linear function
χS∗. □

In fact, for small ϵ one can show that f is more like (ϵ/3)-close to linear,
and this is sharp. See Exercise 1.28.

The BLR Test shows that given black-box access to f : F n
2 → {−1, 1}, we can
“test” whether f is close to some linear function χS using just 3 queries. The
test does not reveal which linear function χS is close to (indeed, determining
this takes at least n queries; see Exercise 1.27). Nevertheless, we can still
determine the value of χS(x) with high probability for every x ∈ F n
2 of our
choosing using just 2 queries. This property is called local correctability of
linear functions.

Proposition 1.31. Suppose f : F n
2 → {−1, 1} is ϵ-close to the linear function χS.
Then for every x ∈ F n
2 , the following algorithm outputs χS(x) with probability
at least 1 − 2ϵ:

• Choose y ∼ F n
2 .

• Query f at y and x + y.

• Output f (y) f (x + y).

We emphasize the order of quantiﬁers here: if we just output f (x) then this
will equal χS(x) for most x; however, the above “local correcting” algorithm
determines χS(x) (with high probability) for every x.

Proof. Since y and x + y are both uniformly distributed on F n
2 (though not
independently) we have Pr[ f (y) ̸= χS(y)] ≤ ϵ and Pr[ f (x + y) ̸= χS(x + y)] ≤ ϵ
by assumption. By the union bound, the probability of either event occurring
is at most 2ϵ; when neither occurs,

f (y) f (x + y) = χS(y)χS(x + y) = χS(x)

as desired. □

1.7. Exercises and notes

1.1 Compute the Fourier expansions of the following functions:
(a) min2 : {−1, 1}
2 → {−1, 1}, the minimum function on 2 bits (also known
as the logical OR function);
(b) min3 : {−1, 1}
3 → {−1, 1} and max3 : {−1, 1}
3 → {−1, 1};
(c) the indicator function 1{a} : F n
2 → {0, 1}, where a ∈ F n
2 ;
(d) the density function ϕ{a} : F n
2 → R ≥0, where a ∈ F n
2 ;
(e) the density function ϕ{a,a+e i} : F n
2 → R ≥0, where a ∈ F n
2 and e i =
(0, . . . , 0, 1, 0, . . . , 0) with the 1 in the ith coordinate;

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

34 1. Boolean functions and the Fourier expansion

(f ) the density function corresponding to the product probability distri-
bution on {−1, 1}n in which each coordinate has mean ρ ∈ [−1, 1];
(g) the inner product mod 2 function, IP2n : F 2n
2 → {−1, 1} deﬁned by
IP2n(x1, . . . , xn, y1, . . . , yn) = (−1)x·y;
(h) the equality function Equn : {−1, 1}n → {0, 1}, deﬁned by Equn(x) = 1 if
and only if x1 = x2 = · · · = xn;
(i) the not-all-equal function NAEn : {−1, 1}n → {0, 1}, deﬁned by NAEn(x) =
1 if and only if the bits x1, . . . , xn are not all equal;
(j) the selection function, Sel : {−1, 1}
3 → {−1, 1}, which outputs x2 if x1 =
−1 and outputs x3 if x1 = 1;
(k) mod3 : F 3
2 → {0, 1}, which is 1 if and only if the number of 1’s in the
input is divisible by 3;
(l) OXR : F 3
2 → {0, 1} deﬁned by OXR(x1, x2, x3) = x1 ∨ (x2 ⊕ x3). Here ∨ de-
notes logical OR, ⊕ denotes logical XOR;
(m) the sortedness function Sort4 : {−1, 1}
4 → {−1, 1}, deﬁned by Sort4(x) =
−1 if and only if x1 ≤ x2 ≤ x3 ≤ x4 or x1 ≥ x2 ≥ x3 ≥ x4;
(n) the hemi-icosahedron function HI : {−1, 1}
6 → {−1, 1} (also known as
the Kushilevitz function), deﬁned to be the number of facets labeled
(+1, +1, +1) in Figure 1.2, minus the number of facets labeled (−1, −1, −1),
modulo 3.
 Figure 1.2. The hemi-icosahedron

(Hint: First compute the real multilinear interpolation of the ana-
logue HI : {0, 1}
6 → {0, 1}.)
(o) the majority functions Maj5 : {−1, 1}
5 → {−1, 1} and Maj7 : {−1, 1}
7 →
{−1, 1};
(p) the complete quadratic function CQn : F n
2 → {−1, 1} deﬁned by CQn(x) =
χ(∑
1≤i< j≤n xi x j). (Hint: Determine CQn(x) as a function of the num-
ber of 1’s in the input modulo 4. You’ll want to distinguish whether n
is even or odd.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.7. Exercises and notes 35

1.2 How many Boolean functions f : {−1, 1}n → {−1, 1} have exactly 1 nonzero
Fourier coefﬁcient?

1.3 Let f : F n
2 → {0, 1}, n > 1, and suppose #{x : f (x) = 1} is odd. Prove that all
of f ’s Fourier coefﬁcients are nonzero.

1.4 Let f : {−1, 1}n → R have Fourier expansion f (x) = ∑S⊆[n] ̂f (S) xS. Let F :
R n → R be the extension of f which is also deﬁned by F(x) = ∑S⊆[n] ̂f (S) xS.
Show that if µ = (µ1, . . . , µn) ∈ [−1, 1]n then

F(µ) = E
y [ f (y)],

where y is the random string in {−1, 1}n deﬁned by having E[yi] = µi
independently for all i ∈ [n].

1.5 Prove that any f : {−1, 1}n → {−1, 1} has at most one Fourier coefﬁcient
with magnitude exceeding 1/2. Is this also true for any f : {−1, 1}n → R
with ∥ f ∥2 = 1?

1.6 Use Parseval’s Theorem to prove uniqueness of the Fourier expansion.

1.7 Let f : {−1, 1}n → {−1, 1} be a random function (i.e., each f (x) is ±1 with
probability 1/2, independently for all x ∈ {−1, 1}n). Show that for each
S ⊆ [n], the random variable ̂f (S) has mean 0 and variance 2−n. (Hint:
Parseval.)

1.8 The (Boolean) dual of f : {−1, 1}n → R is the function f † deﬁned by f †(x) =
− f (−x). The function f is said to be odd if it equals its dual; equivalently,
if f (−x) = − f (x) for all x. The function f is said to be even if f (−x) = f (x)
for all x. Given any function f : {−1, 1}n → R , its odd part is the function
f odd : {−1, 1}n → R deﬁned by f odd(x) = ( f (x) − f (−x))/2, and its even part
is the function f even : {−1, 1}n → R deﬁned by f even(x) = ( f (x) + f (−x))/2.
(a) Express ̂f †(S) in terms of ̂f (S).
(b) Verify that f = f odd + f even and that f is odd (respectively, even) if and
only if f = f odd (respectively, f = f even).
(c) Show that

f odd = ∑

S⊆[n]
|S| odd
 ̂f (S) χS, f even = ∑

S⊆[n]
|S| even
 ̂f (S) χS.

1.9 In this problem we consider representing False,True as 0, 1 ∈ R .
(a) Using the interpolation method from Section 1.2, show that every f :
{False,True}n → {False,True} can be represented as a real multilinear
polynomial
 q(x) = ∑

S⊆[n] cS ∏

i∈S xi, (1.11)

“over {0, 1}”, meaning mapping {0, 1}n → {0, 1}.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

36 1. Boolean functions and the Fourier expansion

(b) Show that this representation is unique. (Hint: If q as in (1.11) has
at least one nonzero coefﬁcient, consider q(a) where a ∈ {0, 1}n is the
indicator vector of a minimal S with cS ̸= 0.)
(c) Show that all coefﬁcients cS in the representation (1.11) will be inte-
gers in the range [−2n, 2n].
(d) Let f : {False,True}n → {False,True}. Let p(x) be f ’s multilinear rep-
resentation when False,True are 1, −1 ∈ R (i.e., p is the Fourier ex-
pansion of f ) and let q(x) be f ’s multilinear representation when
False,True are 0, 1 ∈ R . Show that q(x) = 1
2 − 1
2 p(1 − 2x1, . . . , 1 − 2xn).

1.10 Let f : {−1, 1}n → R be not identically 0. The (real) degree of f , denoted
deg( f ), is deﬁned to be the degree of its multilinear (Fourier) expansion;
i.e., max{|S| : ̂f (S) ̸= 0}.
(a) Show that deg( f ) = deg(a + b f ) for any a, b ∈ R (assuming b ̸= 0, a +
b f ̸= 0).
(b) Show that deg( f ) ≤ k if and only if f is a real linear combination of
functions g1, . . . , gs, each of which depends on at most k input coordi-
nates.
(c) Which functions in Exercise 1.1 have “nontrivial” degree? (Here f :
{−1, 1}n → R has “nontrivial” degree if deg( f ) < n.)

1.11 Suppose that f : {−1, 1}n → {−1, 1} has deg( f ) = k ≥ 1.
(a) Show that f ’s real multilinear representation over {0, 1} (see Exer-
cise 1.9), call it q(x), also has deg(q) = k.
(b) Using Exercise 1.9(c),(d), deduce that f ’s Fourier spectrum is “21−k-
granular”, meaning each ̂f (S) is an integer multiple of 2
1−k.
(c) Show that ∑S⊆[n] | ̂f (S)| ≤ 2k−1.

1.12 A Hadamard Matrix is any N × N real matrix with ±1 entries and orthog-
onal rows. Particular examples are the Walsh–Hadamard Matrices HN ,

inductively deﬁned for N = 2n as follows: H1 = [
1]
, H2n+1 = [H2n H2n
H2n −H2n
 ]
.

(a) Let’s index the rows and columns of H2n by the integers {0, 1, 2, . . . , 2n−
1} rather than [2n]. Further, let’s identify such an integer i with its
binary expansion (i0, i1, . . . , i n−1) ∈ F n
2 , where i0 is the least signiﬁcant
bit and i n−1 the most. For example, if n = 3, we identify the index
i = 6 with (0, 1, 1). Now show that the (γ, x) entry of H2n is (−1)
γ·x.
(b) Show that if f : F n
2 → R is represented as a column vector in R 2n (ac-
cording to the indexing scheme from part (a)) then 2
−nH2n f = ̂f . Here
we think of ̂f as also being a function F n
2 → R , identifying subsets
S ⊆ {0, 1, . . . , n − 1} with their indicator vectors.
(c) Show how to compute H2n f using just n2n additions and subtractions
(rather than 2
2n additions and subtractions as the usual matrix-vector
multiplication algorithm would require). This computation is called

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.7. Exercises and notes 37

the Fast Walsh–Hadamard Transform and is the method of choice
for computing the Fourier expansion of a generic function f : F n
2 → R
when n is large.
(d) Show that taking the Fourier transform is essentially an “involution”:
̂̂f = 2−n f (using the notations from part (b)).

1.13 Let f : {−1, 1}n → R and let 0 < p ≤ q < ∞. Show that ∥ f ∥p ≤ ∥ f ∥q. (Hint:
Use Jensen’s inequality with the convex function t 7→ tq/p.) Extend the in-
equality to the case q = ∞, where ∥ f ∥∞ is deﬁned to be maxx∈{−1,1}n {| f (x)|}.

1.14 Compute the mean and variance of each function from Exercise 1.1.

1.15 Let f : {−1, 1}n → R . Let K ⊆ [n] and let z ∈ {−1, 1}K . Suppose g : {−1, 1}
[n]\K →
R is the subfunction of f gotten by restricting the K-coordinates to be z.
Show that E[g] = ∑T⊆K ̂f (T) zT .

1.16 If f : {−1, 1}n → {−1, 1}, show that Var[ f ] = 4·dist( f , 1)·dist( f , −1). Deduce
Proposition 1.15.

1.17 Extend Fact 1.14 by proving the following: If F is a {−1, 1}-valued random
variable with mean µ then

Var[F] = E[(F − µ)
2] = 1
2 E[(F − F′)
2] = 2 Pr[F ̸= F′] = E[|F − µ|],

where F′ is an independent copy of F. (The ﬁrst two equalities do not
require F to be {−1, 1}-valued.)

1.18 For any f : {−1, 1}n → R , show that

〈 f =k, f =ℓ〉 =
 {
Wk[ f ] if k = ℓ,

0 if k ̸= ℓ.

1.19 Let f : {−1, 1}n → {−1, 1}.
(a) Suppose W1[ f ] = 1. Show that f (x) = ±χS for some |S| = 1.
(b) Suppose W≤1[ f ] = 1. Show that f depends on at most 1 input coordi-
nate.
(c) Suppose W≤2[ f ] = 1. Must f depend on at most 2 input coordinates?
At most 3 input coordinates? What if we assume W
2[ f ] = 1?

1.20 Let f : {−1, 1}n → R satisfy f = f =1. Show that Var[ f 2] = 2 ∑i̸= j ̂f (i)
2 ̂f ( j)2.

1.21 Prove that there are no functions f : {−1, 1}n → {−1, 1} with exactly 2
nonzero Fourier coefﬁcients. What about exactly 3 nonzero Fourier coefﬁ-
cients?

1.22 Verify Propositions 1.25 and 1.26.

1.23 In this exercise you will prove some basic facts about “distances” between
probability distributions. Let ϕ and ψ be probability densities on F n
2 .
(a) Show that the total variation distance between ϕ and ψ, deﬁned by

dTV(ϕ, ψ) = max
A⊆F n
2
 {∣
∣
∣ Pr
y∼ϕ
[y ∈ A] − Pr
y∼ψ
[y ∈ A]
∣
∣
∣}
,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

38 1. Boolean functions and the Fourier expansion

is equal to 1
2 ∥ϕ − ψ∥1.
(b) Show that the collision probability of ϕ, deﬁned to be

Pr
y,y′∼ϕ
independently

[y = y′],

is equal to ∥ϕ∥2
2/2n.
(c) The χ
2-distance of ϕ from ψ is deﬁned by

dχ2(ϕ, ψ) = E
y∼ψ

[( ϕ(y)

ψ(y) − 1)2]
,

assuming ψ has full support. Show that the χ
2-distance of ϕ from
uniform is equal to Var[ϕ].
(d) Show that the total variation distance of ϕ from uniform is at most
1
2 √
Var[ϕ].

1.24 Let A ⊆ {−1, 1}n have “volume” δ, meaning E[1A] = δ. Suppose ϕ is a
probability density supported on A, meaning ϕ(x) = 0 when x ∉ A. Show
that ∥ϕ∥
2
2 ≥ 1/δ with equality if ϕ = ϕA, the uniform density on A.

1.25 Show directly from the deﬁnition that the convolution operator is associa-
tive and commutative.

1.26 Verify that (1) ⇐⇒ (2) in Deﬁnition 1.28.

1.27 Suppose an algorithm is given query access to a linear function f : F n
2 →
F 2 and its task is to determine which linear function f is. Show that
querying f on n inputs is necessary and sufﬁcient.

1.28 (a) Generalize Exercise 1.5 as follows: Let f : F n
2 → {−1, 1} and suppose
that dist( f , χS∗) = δ. Show that | ̂f (S)| ≤ 2δ for all S ̸= S∗. (Hint: Use
the union bound.)
(b) Deduce that the BLR Test rejects f with probability at least 3δ −
10δ2 + 8δ3.
(c) Show that this lower bound cannot be improved to cδ − O(δ2) for any
c > 3.

1.29 (a) We call f : F n
2 → F 2 an afﬁne function if f (x) = a · x + b for some a ∈ F n
2 ,
b ∈ F 2. Show that f is afﬁne if and only if f (x)+ f (y)+ f (z) = f (x+ y+ z)
for all x, y, z, ∈ F n
2
(b) Let f : F n
2 → R . Suppose we choose x, y, z ∼ F n
2 independently and
uniformly. Show that E[ f (x) f (y) f (z) f (x + y + z)] = ∑S ̂f (S)4.
(c) Give a 4-query test for a function f : F n
2 → F 2 with the following prop-
erty: if the test accepts with probability 1 − ϵ then f is ϵ-close to being
afﬁne. All four query inputs should have the uniform distribution
on F n
2 (but of course need not be independent).
(d) Give an alternate 4-query test for being afﬁne in which three of the
query inputs are uniformly distributed and the fourth is not random.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.7. Exercises and notes 39

(Hint: Show that f is afﬁne if and only if f (x) + f (y) + f (0) = f (x + y)
for all x, y ∈ F n
2 .)

1.30 Permutations π ∈ Sn act on strings x ∈ {−1, 1}n in the natural way: (xπ)i =
xπ(i). They also act on functions f : {−1, 1}n → R via f π(x) = f (xπ) for all x ∈
{−1, 1}n. We say that functions g, h : {−1, 1}n → {−1, 1} are (permutation-
)isomorphic if g = hπ for some π ∈ Sn. We call Aut( f ) = {π ∈ Sn : f π = f }
the (permutation-)automorphism group of f .

(a) Show that ̂f π(S) = ̂f (π−1(S)) for all S ⊆ [n].

For future reference, when we write ( ̂f (S))|S|=k, we mean the sequence
of degree-k Fourier coefﬁcients of f , listed in lexicographic order of the
k-sets S.
Given complete truth tables of some g and h we might wish to deter-
mine whether they are isomorphic. One way to do this would be to deﬁne
a canonical form can( f ) : {−1, 1}n → {−1, 1} for each f : {−1, 1}n → {−1, 1},
meaning that: (i) can( f ) is isomorphic to f ; (ii) if g is isomorphic to h then
can(g) = can(h). Then we can determine whether g is isomorphic to h by
checking whether can(g) = can(h). Here is one possible way to deﬁne a
canonical form for f :
1. Set P0 = Sn.
2. For each k = 1, 2, 3, . . . , n,
3. Deﬁne Pk to be the set of all π ∈ Pk−1 that make the sequence
(̂f π(S))|S|=k maximal in lexicographic order on R (n
k).
4. Let can( f ) = f π for (any) π ∈ Pn.
(b) Show that this is well-deﬁned, meaning that can( f ) is the same func-
tion for any choice of π ∈ Pn.
(c) Show that can( f ) is indeed a canonical form; i.e., it satisﬁes (i) and (ii)
above.
(d) Show that if ̂f ({1}), . . . , ̂f ({n}) are distinct numbers then can( f ) can be
computed in ̃O(2n) time.
(e) We could more generally consider g, h : {−1, 1}n → {−1, 1} to be isomor-
phic if g(x) = h(±xπ(1), . . . , ±xπ(n)) for some permutation π on [n] and
some choice of signs. Extend the results of this exercise to handle this
deﬁnition.

Notes. The Fourier expansion for real-valued Boolean functions dates back
to Walsh [Wal23] who introduced a complete orthonormal basis for L2([0, 1])
consisting of ±1-valued functions, constant on dyadic intervals. Using the or-
dering introduced by Paley [Pal32], the nth Walsh basis function wn : [0, 1] →
{−1, 1} is deﬁned by wn(x) = ∏∞
i=0 r i(x)ni , where n = ∑∞
i=0 ni2i and r i(x) (the
“ith Rademacher function at x”) is deﬁned to be (−1)xi , with x = ∑∞
i=0 xi2
−(i+1)

for non-dyadic x ∈ [0, 1]. Walsh’s interest was in comparing and contrasting

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

40 1. Boolean functions and the Fourier expansion

the properties of this basis with the usual basis of trigonometric polynomials
and also Haar’s basis [Haa10].

The ﬁrst major study of the Walsh functions came in the remarkable paper
of Paley [Pal32], which included strong results on the L p-norms of truncations
of Walsh series. Sadly, Paley died in an avalanche one year later (at age 26)
while skiing near Banff. The next major development in the study of Walsh
series was conceptual, with Vilenkin [Vil47] and Fine [Fin49] independently
suggesting the more natural viewpoint of the Walsh functions as characters
of the discrete group Z n
2 . There was signiﬁcant subsequent work in the 1950s
and 1960s, but it’s somewhat unnatural from our point of view because it
relies fundamentally on ordering the Rademacher and Walsh functions ac-
cording to binary expansions. Bonami [Bon68] and Kiener [Kie69] seem to
have been the ﬁrst authors to take our viewpoint, treating bits x1, x2, x3, . . .
symmetrically and ordering Fourier characters χS according to |S| rather
than max(S). Bonami also obtained the ﬁrst hypercontractivity result for the
Boolean cube. This proved to be a crucial tool for analysis of Boolean func-
tions; see Chapter 9. For an early survey on Walsh series, see Balashov and
Rubinshtein [BR73].

Turning to Boolean functions and computer science, the idea of using
Boolean logic to study “switching functions” (as engineers originally called
Boolean functions) dates to the late 1930s and is usually credited to Naka-
shima [Nak35], Shannon [Sha37], and Shestakov [She38]. Muller [Mul54b]
seems to be the ﬁrst to have used Fourier coefﬁcients in the study of Boolean
functions; he mentions computing them while classifying all functions f :
{0, 1}
4 → {0, 1} up to certain equivalences. The ﬁrst publication devoted to
Boolean Fourier coefﬁcients was by Ninomiya [Nin58], who expanded on
Muller’s use of Fourier coefﬁcients for the classiﬁcation of Boolean functions
up to various isomorphisms. Golomb [Gol59] independently pursued the
same project (his work is the content of Exercise 1.30); he was also the ﬁrst to
recognize the connection to Walsh series. The use of “Fourier–Walsh analysis”
in the study of Boolean functions quickly became well known in the early
1960s. Several symposia on applications of Walsh functions took place in the
early 1970s, with Lechner’s 1971 monograph [Lec71] and Karpovsky’s 1976
book [Kar76] becoming the standard references. However, the use of Boolean
analysis in theoretical computer science seemed to wane until 1988, when the
outstanding work of Kahn, Kalai, and Linial [KKL88] ushered in a new area
of sophistication.

The original analysis by Blum, Luby, and Rubinfeld [BLR90] for their
linearity test was combinatorial; our proof of Theorem 1.30 is the elegant an-
alytic one due to Bellare, Coppersmith, Håstad, Kiwi, and Sudan [BCH+96].
In fact, the essence of this analysis appears already in the 1953 work of

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

1.7. Exercises and notes 41

Roth [Rot53] (in the context of the cyclic group Z N rather than F n
2 ). The
work of Bellare et al. also gives additional analysis improving the results of
Theorem 1.30 and Exercise 1.28. See also the work of Kaufman, Litsyn, and
Xie [KLX10] for further slight improvement.

In Exercise 1.1, the sortedness function was introduced by Ambainis [Amb03,
LLS06]; the hemi-icosahedron function was introduced by Kushilevitz [NW95].
The fast algorithm for computing the Fourier transform mentioned in Exer-
cise 1.12 is due to Lechner [Lec63].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 2

Basic concepts and
social choice

In this chapter we introduce a number of important basic concepts including
inﬂuences and noise stability. Many of these concepts are nicely motivated
using the language of social choice. The chapter is concluded with Kalai’s
Fourier-based proof of Arrow’s Theorem.

2.1. Social choice functions

In this section we describe some rudiments of the mathematics of social choice,
a topic studied by economists, political scientists, mathematicians, and com-
puter scientists. The fundamental question in this area is how best to ag-
gregate the opinions of many agents. Examples where this problem arises
include citizens voting in an election, committees deciding on alternatives,
and independent computational agents making collective decisions. Social
choice theory also provides very appealing interpretations for a number of
important functions and concepts in the analysis of Boolean functions.

A Boolean function f : {−1, 1}n → {−1, 1} can be thought of as a voting rule
or social choice function for an election with 2 candidates and n voters; it
maps the votes of the voters to the winner of the election. Perhaps the most
familiar voting rule is the majority function:

Deﬁnition 2.1. For n odd, the majority function Majn : {−1, 1}n → {−1, 1} is
deﬁned by Majn(x) = sgn(x1 + x2 + · · · + xn). (Occasionally, for n even we say
that f is a majority function if f (x) equals the sign of x1 + · · · + xn whenever
this number is nonzero.)
 43

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

44 2. Basic concepts and social choice

The Boolean AND and OR functions correspond to voting rules in which
a certain candidate is always elected unless all voters are unanimously op-
posed. Recalling our somewhat nonintuitive convention that −1 represents
True and +1 represents False:

Deﬁnition 2.2. The function ANDn : {−1, 1}n → {−1, 1} is deﬁned by ANDn(x) =
+1 unless x = (−1, −1, . . . , −1). The function ORn : {−1, 1}n → {−1, 1} is deﬁned
by ORn(x) = −1 unless x = (+1, +1, . . . , +1).

Another voting rule commonly encountered in practice:

Deﬁnition 2.3. The ith dictator function χi : {−1, 1}n → {−1, 1} is deﬁned by
χi(x) = xi.

Here we are simplifying notation for the singleton monomial from χ{i} to
χi. Even though they are extremely simple functions, the dictators play a very
important role in analysis of Boolean functions; to highlight this we prefer
the colorful terminology “dictator functions” to the more mathematically staid
“projection functions”. Generalizing:

Deﬁnition 2.4. A function f : {−1, 1}n → {−1, 1} is called a k-junta for k ∈ N
if it depends on at most k of its input coordinates; i.e., f (x) = g(xi1, . . . , xi k ) for
some g : {−1, 1}k → {−1, 1} and i1, . . . , i k ∈ [n]. Informally, we say that f is a
“junta” if it depends on only a “constant” number of coordinates.

For example, the number of functions f : {−1, 1}n → {−1, 1} which are 1-juntas
is precisely 2n+2: the n dictators, the n negated-dictators, and the 2 constant
functions ±1.

The European Union’s Council of Ministers adopts decisions based on a
weighted majority voting rule:

Deﬁnition 2.5. A function f : {−1, 1}n → {−1, 1} is called a weighted majority
or (linear) threshold function if it is expressible as f (x) = sgn(a0 + a1x1 + · · · +
an xn) for some a0, a1, . . . , an ∈ R .

Exercise 2.2 has you verify that majority, AND, OR, dictators, and constants
are all linear threshold functions.

The leader of the United States (and many other countries) is elected via
a kind of “two-level majority”. We make a natural deﬁnition along these lines:

Deﬁnition 2.6. The depth-d recursive majority of n function, denoted Maj
⊗d
n ,
is the Boolean function of nd bits deﬁned inductively as follows: Maj
⊗1
n =
Majn, and Maj
⊗(d+1)
n (x(1), . . . , x(n)) = Majn(Maj
⊗d
n (x(1)), . . . , Maj
⊗d
n (x(n))) for x(i) ∈
{−1, 1}nd .
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.1. Social choice functions 45

In our last example of a 2-candidate voting rule, the voters are divided into
“tribes” of equal size and the outcome is True if and only if at least one tribe is
unanimously in favor of True. This rule is only somewhat plausible in practice,
but it plays a very important role in the analysis of Boolean functions:

Deﬁnition 2.7. The tribes function of width w and size s, Tribesw,s : {−1, 1}sw →
{−1, 1}, is deﬁned by Tribesw,s(x(1), . . . , x(s)) = ORs(ANDw(x(1)), . . . , ANDw(x(s))),
where x(i) ∈ {−1, 1}w.

Here are some natural properties of 2-candidate social choice functions
which may be considered desirable:

Deﬁnition 2.8. We say that a function f : {−1, 1}n → {−1, 1} is:

• monotone if f (x) ≤ f (y) whenever x ≤ y coordinate-wise;

• odd if f (−x) = − f (x);

• unanimous if f (1, . . . , 1) = 1 and f (−1, . . . , −1) = −1;

• symmetric if f (xπ) = f (x) for all permutations π ∈ Sn (using the notation
from Exercise 1.30); i.e., f (x) only depends on the number of 1’s in x.

The deﬁnitions of monotone, odd, and symmetric are also natural for f :
{−1, 1}n → R .

Example 2.9. The majority function (for n odd) has all four properties in
Deﬁnition 2.8; indeed, May’s Theorem (Exercise 2.3) states that it is the only
monotone, odd, symmetric function. The dictator functions have the ﬁrst
three properties above, as do recursive majority functions. The AND and OR
functions are monotone, unanimous, and symmetric, but not odd. The tribes
functions are monotone and unanimous; although they are not symmetric
they have an important weaker property:

Deﬁnition 2.10. A function f : {−1, 1}n → {−1, 1} is transitive-symmetric if for
all i, i′ ∈ [n] there exists a permutation π ∈ Sn taking i to i′ such f (xπ) = f (x)
for all x ∈ {−1, 1}n.

Intuitively, a function is transitive-symmetric if any two coordinates i, j ∈ [n]
are “equivalent”.

One more natural desirable property of a 2-candidate voting rule is that
it be unbiased as deﬁned in Chapter 1.4, i.e., “equally likely” to elect ±1. Of
course, this presupposes the uniform probability distribution on votes.

Deﬁnition 2.11. The impartial culture assumption is that the n voters’ pref-
erences are independent and uniformly random.

Although this assumption might seem somewhat unrealistic, it gives a
good basis for comparing voting rules in the absence of other information.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

46 2. Basic concepts and social choice

One might also consider it as a model for the votes of just the “undecided” or
“party-independent” voters.

2.2. Inﬂuences and derivatives

Given a voting rule f : {−1, 1}n → {−1, 1} it’s natural to try to measure the
“inﬂuence” or “power” of the ith voter. One can deﬁne this to be the “probability
that the ith vote affects the outcome”.

Deﬁnition 2.12. We say that coordinate i ∈ [n] is pivotal for f : {−1, 1}n →
{−1, 1} on input x if f (x) ̸= f (x⊕i). Here we have used the notation x⊕i for the
string (x1, . . . , xi−1, −xi, xi+1, . . . , xn).

Deﬁnition 2.13. The inﬂuence of coordinate i on f : {−1, 1}n → {−1, 1} is de-
ﬁned to be the probability that i is pivotal for a random input:

Infi[ f ] = Pr
x∼{−1,1}n[ f (x) ̸= f (x⊕i)].

Inﬂuences can be equivalently deﬁned in terms of “geometry” of the Ham-
ming cube:

Fact 2.14. For f : {−1, 1}n → {−1, 1}, the inﬂuence Infi[ f ] equals the fraction
of dimension-i edges in the Hamming cube which are boundary edges. Here
(x, y) is a dimension-i edge if y = x⊕i; it is a boundary edge if f (x) ̸= f (y).

Figure 2.1. Boundary edges of the Maj3 function

Example 2.15. For the ith dictator function χi we have that coordinate i
is pivotal for every input x; hence Infi[χi] = 1. On the other hand, if j ̸= i
then coordinate j is never pivotal; hence Inf j[χi] = 0 for j ̸= i. Note that
the same two statements are true about the negated-dictator functions. For
the constant functions ±1, all inﬂuences are 0. For the ORn function, coordi-
nate 1 is pivotal for exactly two inputs, (−1, 1, 1, . . . , 1) and (1, 1, 1, . . . , 1); hence
Inf1[ORn] = 21−n. Similarly, Infi[ORn] = Infi[ANDn] = 21−n for all i ∈ [n].
The Maj3 is depicted in Figure 2.1; the points where it’s +1 are colored gray
and the points where it’s −1 are colored white. Its boundary edges are high-
lighted in black; there are 2 of them in each of the 3 dimensions. Since there

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.2. Inﬂuences and derivatives 47

are 4 total edges in each dimension, we conclude Infi[Maj3] = 2/4 = 1/2 for all
i ∈ [3]. For majority in higher dimensions, Infi[Majn] equals the probability

that among n − 1 random bits, exactly half of them are 1. This is roughly p
2/πpn
for large n; see Exercise 2.22 or Chapter 5.2.

Inﬂuences can also be deﬁned more “analytically” by introducing the de-
rivative operators.

Deﬁnition 2.16. The ith (discrete) derivative operator Di maps the function
f : {−1, 1}n → R to the function Di f : {−1, 1}n → R deﬁned by

Di f (x) = f (x(i7→1)) − f (x(i7→−1))
2 .

Here we have used the notation x(i7→b) = (x1, . . . , xi−1, b, xi+1, . . . , xn). Notice
that Di f (x) does not actually depend on xi. The operator Di is a linear opera-
tor: i.e., Di( f + g) = Di f + Di g.

If f : {−1, 1}n → {−1, 1} is Boolean-valued then

Di f (x) =
 {
0 if coordinate i is not pivotal for x,

±1 if coordinate i is pivotal for x. (2.1)

Thus Di f (x)2 is the 0-1 indicator for whether i is pivotal for x and we con-
clude that Infi[ f ] = E[Di f (x)2]. We take this formula as a deﬁnition for the
inﬂuences of real-valued Boolean functions.

Deﬁnition 2.17. We generalize Deﬁnition 2.13 to functions f : {−1, 1}n → R
by deﬁning the inﬂuence of coordinate i on f to be

Infi[ f ] = E
x∼{−1,1}n[Di f (x)2] = ∥Di f ∥
2
2.

Deﬁnition 2.18. We say that coordinate i ∈ [n] is relevant for f : {−1, 1}n → R
if and only if Infi[ f ] > 0; i.e., f (x(i7→1)) ̸= f (x(i7→−1)) for at least one x ∈ {−1, 1}n.

The discrete derivative operators are quite analogous to the usual partial
derivatives. For example, f : {−1, 1}n → R is monotone if and only if Di f (x) ≥ 0
for all i and x. Further, Di acts like formal differentiation on Fourier expan-
sions:

Proposition 2.19. Let f : {−1, 1}n → R have the multilinear expansion f (x) =
∑S⊆[n] ̂f (S) xS. Then Di f (x) = ∑

S⊆[n]
S∋i
 ̂f (S) xS\{i}. (2.2)

Proof. Since Di is a linear operator, the claim follows immediately from the
observation that
 Di xS =
 {xS\{i} if i ∈ S,

0 if i ̸∈ S. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

48 2. Basic concepts and social choice

By applying Parseval’s Theorem to the Fourier expansion (2.2), we obtain
a Fourier formula for inﬂuences:

Theorem 2.20. For f : {−1, 1}n → R and i ∈ [n],

Infi[ f ] = ∑

S∋i ̂f (S)2.

In other words, the inﬂuence of coordinate i on f equals the sum of f ’s
Fourier weights on sets containing i. This is another good example of being
able to “read off ” an interesting combinatorial property of a Boolean function
from its Fourier expansion. In the special case that f : {−1, 1}n → {−1, 1} is
monotone there is a much simpler way to read off its inﬂuences: they are the
degree-1 Fourier coefﬁcients. In what follows, we write ̂f (i) in place of ̂f ({i}).

Proposition 2.21. If f : {−1, 1}n → {−1, 1} is monotone, then Infi[ f ] = ̂f (i).

Proof. By monotonicity, the ±1 in (2.1) is always 1; i.e., Di f (x) is the 0-1
indicator that i is pivotal for x. Hence Infi[ f ] = E[Di f ] = ̂Di f (;) = ̂f (i), where
the third equality used Proposition 2.19. □

This formula allows us a neat proof that for any 2-candidate voting rule
that is monotone and transitive-symmetric, all of the voters have small inﬂu-
ence:

Proposition 2.22. Let f : {−1, 1}n → {−1, 1} be transitive-symmetric and mono-
tone. Then Infi[ f ] ≤ 1/
pn for all i ∈ [n].

Proof. Transitive-symmetry of f implies that ̂f (i) = ̂f (i′) for all i, i′ ∈ [n]
(using Exercise 1.30(a)); thus by monotonicity, Infi[ f ] = ̂f (i) = ̂f (1) for all
i ∈ [n]. But by Parseval, 1 = ∑S ̂f (S)2 ≥ ∑n
i=1 ̂f (i)2 = n ̂f (1)2; hence ̂f (1) ≤
1/
pn. □

This bound is slightly improved in Proposition 2.58 and Exercise 2.24.

The derivative operators are very convenient for functions deﬁned on
{−1, 1}n. However they are less natural if we think of the Hamming cube
as {True,False}n; for the more general domains we’ll look at in Chapter 8
they don’t even make sense. We end this section by introducing some useful
deﬁnitions that will generalize better later.

Deﬁnition 2.23. The ith expectation operator Ei is the linear operator on
functions f : {−1, 1}n → R deﬁned by

Ei f (x) = E
xi[ f (x1, . . . , xi−1, xi, xi+1, . . . , xn)].

Whereas Di f isolates the part of f depending on the ith coordinate, Ei f
isolates the part not depending on the ith coordinate. Exercise 2.15 asks you
to verify the following:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.3. Total inﬂuence 49

Proposition 2.24. For f : {−1, 1}n → R ,

• Ei f (x) = f (x(i7→1)) + f (x(i7→−1))
2 ,

• Ei f (x) = ∑

S̸∋i ̂f (S) xS,

• f (x) = xiDi f (x) + Ei f (x).

Note that in the decomposition f = xiDi f + Ei f , neither Di f nor Ei f de-
pends on xi. This decomposition is very useful for proving facts about Boolean
functions by induction on n.

Finally, we will also deﬁne an operator very similar to Di called the ith
Laplacian:

Deﬁnition 2.25. The ith coordinate Laplacian operator Li is deﬁned by

Li f = f − Ei f .

Notational warning: Elsewhere you might see the negated deﬁnition, Ei f − f .

Exercise 2.16 asks you to verify the following:

Proposition 2.26. For f : {−1, 1}n → R ,

• Li f (x) = f (x) − f (x⊕i)
2 ,

• Li f (x) = xiDi f (x) = ∑

S∋i ̂f (S) xS,

• 〈 f , Li f 〉 = 〈Li f , Li f 〉 = Infi[ f ].

2.3. Total inﬂuence

A very important quantity in the analysis of a Boolean function is the sum of
its inﬂuences.

Deﬁnition 2.27. The total inﬂuence of f : {−1, 1}n → R is deﬁned to be

I[ f ] = n∑

i=1 Infi[ f ].

For Boolean-valued functions f : {−1, 1}n → {−1, 1} the total inﬂuence has
several additional interpretations. First, it is often referred to as the average
sensitivity of f because of the following proposition:

Proposition 2.28. For f : {−1, 1}n → {−1, 1}

I[ f ] = E
x [sens f (x)],

where sens f (x) is the sensitivity of f at x, deﬁned to be the number of pivotal
coordinates for f on input x.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

50 2. Basic concepts and social choice

Proof.

I[ f ] = n∑

i=1 Infi[ f ] = n∑

i=1 Pr
x [ f (x) ̸= f (x⊕i)]

= n∑

i=1 E
x [1 f (x)̸= f (x⊕i)] = E
x
 [ n∑

i=1 1 f (x)̸= f (x⊕i)
]
 = E
x [sens f (x)]. □

The total inﬂuence of f : {−1, 1}n → {−1, 1} is also closely related to the size
of its edge boundary; from Fact 2.14 we deduce:

Fact 2.29. The fraction of edges in the Hamming cube {−1, 1}n which are
boundary edges for f : {−1, 1}n → {−1, 1} is equal to 1
n I[ f ].

Example 2.30. (Recall Example 2.15.) For Boolean-valued functions f :
{−1, 1}n → {−1, 1} the total inﬂuence ranges between 0 and n. It is minimized
by the constant functions ±1 which have total inﬂuence 0. It is maximized by
the parity function χ[n] and its negation which have total inﬂuence n; every
coordinate is pivotal on every input for these functions. The dictator functions
(and their negations) have total inﬂuence 1. The total inﬂuence of ORn and
ANDn is very small: n21−n. On the other hand, the total inﬂuence of Majn is
fairly large: roughly p
2/πpn for large n.

By virtue of Proposition 2.21 we have another interpretation for the total
inﬂuence of monotone functions:

Proposition 2.31. If f : {−1, 1}n → {−1, 1} is monotone, then

I[ f ] = n∑

i=1 ̂f (i).

This sum of the degree-1 Fourier coefﬁcients has a natural interpretation
in social choice:

Proposition 2.32. Let f : {−1, 1}n → {−1, 1} be a voting rule for a 2-candidate
election. Given votes x = (x1, . . . , xn), let w be the number of votes that agree
with the outcome of the election, f (x). Then

E[w] = n
2 + 1
2
 n∑

i=1 ̂f (i).

Proof. By the formula for Fourier coefﬁcients,

n∑

i=1 ̂f (i) = n∑

i=1 E
x [ f (x)xi] = E
x [ f (x)(x1 + x2 + · · · + xn)]. (2.3)

Now x1 + · · · + xn equals the difference between the number of votes for can-
didate 1 and the number of votes for candidate −1. Hence f (x)(x1 + · · · + xn)
equals the difference between the number of votes for the winner and the
number of votes for the loser; i.e., w − (n − w) = 2w − n. The result follows. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.3. Total inﬂuence 51

Rousseau [Rou62] suggested that the ideal voting rule is one which max-
imizes the number of votes that agree with the outcome. Here we show that
the majority rule has this property (at least when n is odd):

Theorem 2.33. The unique maximizers of ∑n
i=1 ̂f (i) among all f : {−1, 1}n →
{−1, 1} are the majority functions. In particular, I[ f ] ≤ I[Majn] = p
2/πpn +
O(n−1/2) for all monotone f .

Proof. From (2.3),

n∑

i=1 ̂f (i) = E
x [ f (x)(x1 + x2 + · · · + xn)] ≤ E
x [|x1 + x2 + · · · + xn|],

since f (x) ∈ {−1, 1} always. Equality holds if and only if f (x) = sgn(x1 + · · · + xn)
whenever x1 + · · · + xn ̸= 0. The second statement of the theorem follows from
Proposition 2.31 and Exercise 2.22. □

Let’s now take a look at more analytic expressions for the total inﬂuence.
By deﬁnition, if f : {−1, 1}n → R , then

I[ f ] = n∑

i=1 Infi[ f ] = n∑

i=1 E
x [Di f (x)2] = E
x
 [ n∑

i=1 Di f (x)
2]
 . (2.4)

This motivates the following deﬁnition:

Deﬁnition 2.34. The (discrete) gradient operator ∇ maps the function f :
{−1, 1}n → R to the function ∇ f : {−1, 1}n → R n deﬁned by

∇ f (x) = (D1 f (x), D2 f (x), . . . , Dn f (x)).

Note that for f : {−1, 1}n → {−1, 1} we have ∥∇ f (x)∥2
2 = sens f (x), where ∥·∥2
is the usual Euclidean norm in R n. In general, from (2.4) we deduce:

Proposition 2.35. For f : {−1, 1}n → R ,

I[ f ] = E
x [∥∇ f (x)∥
2
2].

An alternative analytic deﬁnition involves introducing the Laplacian:

Deﬁnition 2.36. The Laplacian operator L is the linear operator on functions
f : {−1, 1}n → R deﬁned by L = ∑n
i=1 Li.

Exercise 2.17 asks you to verify the following:

Proposition 2.37. For f : {−1, 1}n → R ,

• L f (x) = (n/2)( f (x) − avg
i∈[n]
{ f (x⊕i)}
)
,

• L f (x) = f (x) · sens f (x) if f : {−1, 1}n → {−1, 1},

• L f = ∑

S⊆[n] |S| ̂f (S) χS,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

52 2. Basic concepts and social choice

• 〈 f , L f 〉 = I[ f ].

We can obtain a Fourier formula for the total inﬂuence of a function using
Theorem 2.20; when we sum that theorem over all i ∈ [n] the Fourier weight
̂f (S)
2 is counted exactly |S| times. Hence:

Theorem 2.38. For f : {−1, 1}n → R ,

I[ f ] = ∑

S⊆[n] |S| ̂f (S)2 = n∑

k=0 k · Wk[ f ]. (2.5)

For f : {−1, 1}n → {−1, 1} we can express this using the spectral sample:

I[ f ] = E
S∼S f [|S|].

Thus the total inﬂuence of f : {−1, 1}n → {−1, 1} also measures the average
“height” or degree of its Fourier weights.

Finally, from Proposition 1.13 we have Var[ f ] = ∑k>0 Wk[ f ]; comparing
this with (2.5) we immediately deduce a simple but important fact called the
Poincaré Inequality.

Poincaré Inequality. For any f : {−1, 1}n → R , Var[ f ] ≤ I[ f ].

Equality holds in the Poincaré Inequality if and only if all of f ’s Fourier
weight is at degrees 0 and 1; i.e., W≤1[ f ] = E[ f 2]. For Boolean-valued f :
{−1, 1}n → {−1, 1}, Exercise 1.19 tells us this can only occur if f = ±1 or f = ±χi
for some i.

For Boolean-valued f : {−1, 1}n → R , the Poincaré Inequality can be viewed
as an (edge-)isoperimetric inequality, or (edge-)expansion bound, for the Ham-
ming cube. If we think of f as the indicator function for a set A ⊆ {−1, 1}n

of “measure” α = |A|/2n, then Var[ f ] = 4α(1 − α) (Fact 1.14) whereas I[ f ] is n
times the (fractional) size of A’s edge boundary. In particular, the Poincaré
Inequality says that subsets A ⊆ {−1, 1}n of measure α = 1/2 must have edge
boundary at least as large as those of the dictator sets.

For α ∉ {0, 1/2, 1} the Poincaré Inequality is not sharp as an edge-isoperimetric
inequality for the Hamming cube; for small α even the asymptotic depen-
dence is not optimal. Precisely optimal edge-isoperimetric results (and also
vertex-isoperimetric results) are known for the Hamming cube. The following
simpliﬁed theorem is optimal for α of the form 2
−i:

Theorem 2.39. For f : {−1, 1}n → {−1, 1} with α = min{Pr[ f = 1], Pr[ f = −1]},

2α log(1/α) ≤ I[ f ].

This result illustrates an important recurring concept in the analysis of
Boolean functions: The Hamming cube is a “small-set expander”. Roughly
speaking, this is the idea that “small” subsets A ⊆ {−1, 1}n have unusually
large “boundary size”.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.4. Noise stability 53

2.4. Noise stability

Suppose f : {−1, 1}n → {−1, 1} is a voting rule for a 2-candidate election. Mak-
ing the impartial culture assumption, the n voters independently and uni-
formly randomly choose their votes x = (x1, . . . , xn). Now imagine that when
each voter goes to the ballot box there is some chance that their vote is mis-
recorded. Speciﬁcally, say that each vote is correctly recorded with probability
ρ ∈ [0, 1] and is garbled – i.e., changed to a random bit – with probability
1 − ρ. Writing y = (y1, . . . , yn) for the votes that are ﬁnally recorded, we may
ask about the probability that f (x) = f (y), i.e., whether the misrecorded votes
affected the outcome of the election. This has to do with the noise stability
of f .

Deﬁnition 2.40. Let ρ ∈ [0, 1]. For ﬁxed x ∈ {−1, 1}n we write y ∼ Nρ(x) to
denote that the random string y is drawn as follows: for each i ∈ [n] indepen-
dently,
 yi =
 {xi with probability ρ,

uniformly random with probability 1 − ρ.

We extend the notation to all ρ ∈ [−1, 1] as follows:

yi =
 {xi with probability 1
2 + 1
2 ρ,

−xi with probability 1
2 − 1
2 ρ.

We say that y is ρ-correlated to x.

Deﬁnition 2.41. If x ∼ {−1, 1}n is drawn uniformly at random and then
y ∼ Nρ(x), we say that (x, y) is a ρ-correlated pair of random strings. This def-
inition is symmetric in x and y; it is equivalent to saying that independently
for each i ∈ [n], the pair of random bits (xi, yi) satisﬁes E[xi] = E[yi] = 0 and
E[xi yi] = ρ.

With these deﬁnitions in hand we can now deﬁne the important concept
of noise stability, which measures the correlation between f (x) and f (y) when
(x, y) is a ρ-correlated pair.

Deﬁnition 2.42. For f : {−1, 1}n → R and ρ ∈ [−1, 1], the noise stability of f at
ρ is Stabρ[ f ] = E
(x,y)
ρ-correlated

[ f (x) f (y)].

If f : {−1, 1}n → {−1, 1} we have

Stabρ[ f ] = Pr
(x,y)
ρ-correlated
[ f (x) = f (y)] − Pr
(x,y)
ρ-correlated
[ f (x) ̸= f (y)]

= 2 Pr
(x,y)
ρ-correlated
[ f (x) = f (y)] − 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

54 2. Basic concepts and social choice

In the voting scenario described above, the probability that the misrecord-
ing of votes doesn’t affect the election outcome is 1
2 + 1
2 Stabρ[ f ].

When ρ is close to 1 (i.e., the “noise” is small) it’s sometimes more natu-
ral to ask about the probability that reversing a small fraction of the votes
reverses the outcome of the election.

Deﬁnition 2.43. For f : {−1, 1}n → {−1, 1} and δ ∈ [0, 1] we write NSδ[ f ] for
noise sensitivity of f at δ, deﬁned to be the probability that f (x) ̸= f (y) when
x ∼ {−1, 1}n is uniformly random and y is formed from x by reversing each bit
independently with probability δ. In other words,

NSδ[ f ] = 1
2 − 1
2 Stab1−2δ[ f ].

Example 2.44. The constant functions ±1 have noise stability 1 for ev-
ery ρ. The dictator functions χi satisfy Stabρ[χi] = ρ for all ρ (equivalently,
NSδ[χi] = δ for all δ). More generally,

Stabρ[χS] = E
(x,y)
ρ-correlated

[xS yS] = E
 [ ∏

i∈S(xi yi)

]
 = ∏

i∈S E[xi yi] = ∏

i∈S ρ = ρ|S|,

where we used the fact that the bit pairs (xi, yi) are independent across i to
convert the expectation of a product to a product of an expectation.

There is no convenient expression for the noise stability of the major-
ity function Stabρ[Majn]. However, for a ﬁxed noise rate, the noise stabil-
ity/sensitivity tends to a nice limit as n → ∞:

Theorem 2.45. For any ρ ∈ [−1, 1],

lim
n→∞
n odd Stabρ[Majn] = 2
π arcsin ρ = 1 − 2
π arccos ρ.

Equivalently, for δ ∈ [0, 1],

lim
n→∞
n odd NSδ[Majn] = 1
π arccos(1 − 2δ).

Using cos(z) = 1 − 1
2 z2 + O(z4), hence arccos(1 − 2δ) = 2
p
δ + O(δ3/2), we deduce

lim
n→∞
n odd NSδ[Majn] = 2
π p
δ + O(δ3/2).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.4. Noise stability 55

Figure 2.2. Plot of 2
π arcsin ρ as a function of ρ

We prove Theorem 2.45 in Chapter 5.2.

There is a simple Fourier formula for the noise stability of a Boolean
function; it’s one of the most powerful links between the combinatorics of
Boolean functions and their Fourier spectra. To determine it, we begin by
introducing the most important operator in analysis of Boolean functions: the
noise operator, denoted Tρ for historical reasons.

Deﬁnition 2.46. For ρ ∈ [−1, 1], the noise operator with parameter ρ is the
linear operator Tρ on functions f : {−1, 1}n → R deﬁned by

Tρ f (x) = E
y∼Nρ(x)
[ f (y)].

Proposition 2.47. For f : {−1, 1}n → R , the Fourier expansion of Tρ f is given
by
 Tρ f = ∑

S⊆[n] ρ|S| ̂f (S) χS = n∑

k=0 ρk f =k.

Proof. Since Tρ is a linear operator, it sufﬁces to verify that TρχS = ρ|S|χS:

TρχS(x) = E
y∼Nρ(x)
[yS] = ∏

i∈S E
y∼Nρ(x)[yi] = ∏

i∈S(ρxi) = ρ|S|χS(x).

Here we used the fact that for y ∼ Nρ(x) the bits yi are independent and
satisfy E[yi] = ρxi. □

Exercise 2.25 gives an alternate way of looking at this proof. Yet another proof
using probability densities and convolution is outlined in Exercise 2.30.

The connection between Tρ and noise stability is that

Stabρ[ f ] = E
x∼{−1,1}n
y∼Nρ(x)
 [ f (x) f (y)] = E
x
 [ f (x) E
y∼Nρ(x)[ f (y)]
] ;

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

56 2. Basic concepts and social choice

hence:

Fact 2.48. Stabρ[ f ] = 〈 f , Tρ f 〉.

From Plancherel’s Theorem and Proposition 2.47 we deduce the Fourier
formula for noise stability:

Theorem 2.49. For f : {−1, 1}n → R ,

Stabρ[ f ] = ∑

S⊆[n] ρ|S| ̂f (S)
2 = n∑

k=0 ρk · Wk[ f ].

Hence for f : {−1, 1}n → {−1, 1} we have

Stabρ[ f ] = E
S∼S f [ρ|S|], (2.6)

NSδ[ f ] = 1
2
 n∑

k=0
(1 − (1 − 2δ)k) · Wk[ f ]. (2.7)

Thus the noise stability of f at ρ is equal to the sum of its Fourier weights,
attenuated by a factor which decreases exponentially with degree. A simple
but important corollary is that dictators (and their negations) maximize noise
stability:

Proposition 2.50. Let ρ ∈ (0, 1). If f : {−1, 1}n → {−1, 1} is unbiased, then
Stabρ[ f ] ≤ ρ, with equality if and only if f = ±χi for some i ∈ [n].

Proof. For unbiased f we have W
0[ f ] = 0 and hence Stabρ[ f ] = ∑k≥1 ρkWk[ f ].
Since ρk < ρ for all k > 1, noise stability is maximized if all of f ’s Fourier
weight is on degree 1. This occurs if and only if f = ±χi, by Exercise 1.19(a).
□

For a ﬁxed function f , it’s often interesting to see how Stabρ[ f ] varies
as a function of ρ. From Theorem 2.49 we see that Stabρ[ f ] is a (univari-
ate) polynomial with nonnegative coefﬁcients; in particular, it’s an increasing
function of ρ on [0, 1]. The derivatives of this polynomial at 0 and 1 have nice
interpretations, as can be immediately deduced from Theorem 2.49:

Proposition 2.51. For f : {−1, 1}n → R ,

d
dρ Stabρ[ f ] ∣
∣
∣ρ=0 = W
1[ f ],

d
dρ Stabρ[ f ] ∣
∣
∣ρ=1 = I[ f ].

For f : {−1, 1}n → {−1, 1} we have that NSδ[ f ] is an increasing function of δ on
[0, 1/2], and the second identity is equivalent to

d
dδ NSδ[ f ] ∣
∣
∣
δ=0= I[ f ].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.5. Highlight: Arrow’s Theorem 57

We conclude this section by introducing a version of inﬂuences that also
incorporates noise.

Deﬁnition 2.52. For f : {−1, 1}n → R , ρ ∈ [0, 1] and i ∈ [n], the ρ-stable inﬂu-
ence of i on f is
 Inf(ρ)
i [ f ] = Stabρ[Di f ] = ∑

S∋i ρ|S|−1 ̂f (S)2,

with 0
0 interpreted as 1. We also deﬁne I
(ρ)[ f ] = ∑n
i=1 Inf(ρ)
i [ f ].

Exercise 2.40 asks you to verify the following:

Fact 2.53. I
(ρ)[ f ] = d
dρ Stabρ[ f ] = ∑n
k=1 kρk−1 · Wk[ f ].

The ρ-stable inﬂuence Inf
(ρ)
i [ f ] increases from ̂f (i)2 up to Infi[ f ] as ρ
increases from 0 to 1. For 0 < ρ < 1 there isn’t an especially natural combi-
natorial interpretation for Inf(ρ)
i [ f ] beyond Stabρ[Di f ]; however, we will see
later that the stable inﬂuences are technically very useful. One reason for
this is that every function f : {−1, 1}n → {−1, 1} has at most “constantly” many
“stably-inﬂuential” coordinates:

Proposition 2.54. Suppose f : {−1, 1}n → R has Var[ f ] ≤ 1. Given 0 < δ, ϵ ≤ 1,
let J = {i ∈ [n] : Inf
(1−δ)
i [ f ] ≥ ϵ}. Then |J| ≤ 1
δϵ .

Proof. Certainly |J| ≤ I(1−δ)[ f ]/ϵ so it remains to verify I(1−δ)[ f ] ≤ 1/δ. Com-
paring Fact 2.53 with Var[ f ] = ∑k̸=0 Wk[ f ] term by term, it sufﬁces to show
that (1 − δ)k−1k ≤ 1/δ for all k ≥ 1. This is the easy Exercise 2.45. □

It’s good to think of the set J in this proposition as the “notable” coor-
dinates for function f . Had we used the usual inﬂuences in place of stable
inﬂuences, we would not have been guaranteed a bounded number of “notable”
coordinates (since, e.g., the parity function χ[n] has all n of its inﬂuences equal
to 1).

2.5. Highlight: Arrow’s Theorem

When there are just 2 candidates, the majority function possesses all of the
mathematical properties that seem desirable in a voting rule (e.g., May’s
Theorem and Theorem 2.33). Unfortunately, as soon as there are 3 (or more)
candidates the problem of social choice becomes much more difﬁcult. For
example, suppose we have candidates a, b, and c, and each of n voters has
a ranking of them. How should we aggregate these preferences to produce a
winning candidate?

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

58 2. Basic concepts and social choice

In his 1785 Essay on the Application of Analysis to the Probability of Ma-
jority Decisions [dC85], Condorcet suggested using the voters’ preferences to
conduct the three possible pairwise elections, a vs. b, b vs. c, and c vs. a. This
calls for the use of a 2-candidate voting rule f : {−1, 1}n → {−1, 1}; Condorcet
suggested f = Majn but we might consider any such rule. Thus a “3-candidate
Condorcet election” using f is conducted as follows:

Voters’ Preferences
#1 #2 #3 · · · Societal Aggregation
a (+1) vs. b (−1) +1 +1 −1 · · · = x f (x)
b (+1) vs. c (−1) +1 −1 +1 · · · = y f (y)
c (+1) vs. a (−1) −1 −1 +1 · · · = z f (z)

In the above example, voter #1 ranked the candidates a > b > c, voter #2
ranked them a > c > b, voter #3 ranked them b > c > a, etc. Note that the ith
voter has one of 3! = 6 possible rankings, and these translate into a triple of
bits (xi, yi, zi) from the following set:
{
(+1, +1, −1), (+1, −1, −1), (−1, +1, −1), (−1, +1, +1), (+1, −1, +1), (−1, −1, +1)}
.

These are precisely the triples satisfying the not-all-equal predicate NAE3
(see Exercise 1.1(i)).

In the example above, if n = 3 and f = Maj3 then the societal outcome
would be (+1, +1, −1), meaning that society elects a over b, b over c, and
a over c. In this case it is only natural to declare a the overall winner.

Deﬁnition 2.55. In an election employing Condorcet’s method with voting
rule f : {−1, 1}n → {−1, 1}, we say that a candidate is a Condorcet winner if it
wins all of the pairwise elections in which it participates.

Unfortunately, as Condorcet himself noted, there may not be a Condorcet
winner. In the example above, if voter #2’s ranking was instead c > a > b
(corresponding to (+1, −1, +1)), we would obtain the “paradoxical” outcome
(+1, +1, +1): society prefers a over b, b over c, and c over a! This lack of a
Condorcet winner is termed Condorcet’s Paradox; it occurs when the outcome
( f (x), f (y), f (z)) is one of the two “all-equal” triples {(−1, −1, −1), (+1, +1, +1)}.

One might wonder if the Condorcet Paradox can be avoided by using a
voting rule f : {−1, 1}n → {−1, 1} other than majority. However, in 1950 Ar-
row [Arr50] famously showed that the only means of avoidance is an unap-
pealing one:

Arrow’s Theorem. Suppose f : {−1, 1}n → {−1, 1} is a unanimous voting rule
used in a 3-candidate Condorcet election. If there is always a Condorcet winner,
then f must be a dictatorship.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.5. Highlight: Arrow’s Theorem 59

(In fact, Arrow’s Theorem is slightly stronger than this; see Exercise 2.51.)

In 2002 Kalai gave a new proof of Arrow’s Theorem; it takes its cue from
the title of Condorcet’s work and computes the probability of a Condorcet
winner. This is done under the “impartial culture assumption” for 3-candidate
elections: each voter independently chooses one of the 6 possible rankings
uniformly at random.

Theorem 2.56. Consider a 3-candidate Condorcet election using f : {−1, 1}n →
{−1, 1}. Under the impartial culture assumption, the probability of a Condorcet
winner is precisely 3
4 − 3
4 Stab−1/3[ f ].

Proof. Let x, y, z ∈ {−1, 1}n be the votes for the elections a vs. b, b vs. c, and
c vs. a, respectively. Under impartial culture, the bit triples (xi, yi, zi) are
independent and each is drawn uniformly from the 6 triples satisfying the
not-all-equal predicate NAE3 : {−1, 1}
3 → {0, 1}. There is a Condorcet winner if
and only if NAE3( f (x), f (y), f (z)) = 1. Hence

Pr[∃ Condorcet winner] = E[NAE3( f (x), f (y), f (z))]. (2.8)

The multilinear (Fourier) expansion of NAE3 is

NAE3(w1, w2, w3) = 3
4 − 1
4 w1w2 − 1
4 w1w3 − 1
4 w2w3;

thus (2.8) = 3
4 − 1
4 E[ f (x) f (y)] − 1
4 E[ f (x) f (z)] − 1
4 E[ f (y) f (z)].

In the joint distribution of x, y the n bit pairs (xi, yi) are independent. Further,
by inspection we see that E[xi] = E[yi] = 0 and that E[xi yi] = (2/6)(+1) +
(4/6)(−1) = −1/3. Hence E[ f (x) f (y)] is precisely Stab−1/3[ f ]. Similarly we
have E[ f (x) f (z)] = E[ f (y) f (z)] = Stab−1/3[ f ] and the proof is complete. □

Arrow’s Theorem is now an easy corollary:

Proof of Arrow’s Theorem. By assumption, the probability of a Condorcet
winner is 1; hence

1 = 3
4 − 3
4 Stab−1/3[ f ] = 3
4 − 3
4
 n∑

k=0
(−1/3)kWk[ f ].

Since (−1/3)k ≥ −1/3 for all k, the equality above can only occur if all of f ’s
Fourier weight is on degree 1; i.e., W
1[ f ] = 1. By Exercise 1.19(a) this implies
that f is either a dictator or a negated-dictator. Since f is unanimous, it must
in fact be a dictator. □

An advantage of Kalai’s analytic proof of Arrow’s Theorem is that we can
deduce several more interesting results about the probability of a Condorcet
winner. For example, combining Theorem 2.56 with Theorem 2.45 we get
Guilbaud’s Formula:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

60 2. Basic concepts and social choice

Guilbaud’s Formula. In a 3-candidate Condorcet election using Majn, the
probability of a Condorcet winner tends to

3
2π arccos(−1/3) ≈ 91.2%.

as n → ∞.

This is already a fairly high probability. Unfortunately, if we want to
improve on it while still using a reasonably fair election scheme, we can only
set our hopes higher by a sliver:

Theorem 2.57. In a 3-candidate Condorcet election using an f : {−1, 1}n →
{−1, 1} with all ̂f (i) equal, the probability of a Condorcet winner is at most
7
9 + 4
9π + on(1) ≈ 91.9%.

The condition in Theorem 2.57 seems like it would be satisﬁed by most
reasonably fair voting rules f : {−1, 1}n → {−1, 1} (e.g., it is satisﬁed if f is
transitive-symmetric or is monotone with all inﬂuences equal). In fact, we will
show that Theorem 2.57’s hypothesis can be relaxed in Chapter 5.4; we will
further show in Chapter 11.7 that 7
9 + 4
9π can be improved to the tight value
3
2π arccos(−1/3) of majority. To return to Theorem 2.57, it is an immediate
consequence of the following two results, the ﬁrst being Exercise 2.24 and the
second being an easy corollary of Theorem 2.56.

Proposition 2.58. Suppose f : {−1, 1}n → {−1, 1} has all ̂f (i) equal. Then
W1[ f ] ≤ 2/π + on(1).

Corollary 2.59. In a 3-candidate Condorcet election using f : {−1, 1}n →
{−1, 1}, the probability of a Condorcet winner is at most 7
9 + 2
9 W
1[ f ].

Proof. From Theorem 2.56, the probability is

3
4 − 3
4 Stab−1/3[ f ] = 3
4 − 3
4 (W
0[ f ] − 1
3 W
1[ f ] + 1
9 W2[ f ] − 1
27 W
3[ f ] + · · · )

≤ 3
4 + 1
4 W
1[ f ] + 1
36 W
3[ f ] + 1
324 W
5[ f ] + · · ·

≤ 3
4 + 1
4 W
1[ f ] + 1
36 (W3[ f ] + W5[ f ] + · · · )

≤ 3
4 + 1
4 W
1[ f ] + 1
36 (1 − W1[ f ]) = 7
9 + 2
9 W1[ f ]. □

Finally, using Corollary 2.59 we can prove a “robust” version of Arrow’s
Theorem, showing that a Condorcet election is almost paradox-free only if it
is almost a dictatorship (possibly negated).

Corollary 2.60. Suppose that in a 3-candidate Condorcet election using f :
{−1, 1}n → {−1, 1}, the probability of a Condorcet winner is 1 − ϵ. Then f is
O(ϵ)-close to ±χi for some i ∈ [n].

Proof. From Corollary 2.59 we obtain that W1[ f ] ≥ 1 − 9
2 ϵ. The conclusion
now follows from the FKN Theorem. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.6. Exercises and notes 61

Friedgut–Kalai–Naor (FKN) Theorem. Suppose f : {−1, 1}n → {−1, 1} has
W1[ f ] ≥ 1 − δ. Then f is O(δ)-close to ±χi for some i ∈ [n].

We will see the proof of the FKN Theorem in Chapter 9.1. We’ll also show
in Chapter 5.4 that the O(δ) closeness can be improved to δ/4 + O(δ2 log(2/δ)).

2.6. Exercises and notes

2.1 For each function in Exercise 1.1, determine if it is odd, transitive-symmetric,
and/or symmetric.

2.2 Show that the n-bit functions majority, AND, OR, ±χi, and ±1 are all
linear threshold functions.

2.3 Prove May’s Theorem:
(a) Show that f : {−1, 1}n → {−1, 1} is symmetric and monotone if and only
if it can be expressed as a weighted majority with a1 = a2 = · · · = an =
1.
(b) Suppose f : {−1, 1}n → {−1, 1} is symmetric, monotone, and odd. Show
that n must be odd, and that f = Majn.

2.4 Subset A ⊆ {−1, 1}n is called a Hamming ball if A = {x : ∆(x, z) < r} for some
z ∈ {−1, 1}n and real r. Show that f : {−1, 1}n → {−1, 1} is the indicator of a
Hamming ball if and only if it’s expressible as a linear threshold function
f (x) = sgn(a0 + a1x1 + · · · + an xn) with |a1| = |a2| = · · · = |an|.

2.5 Let f : {−1, 1}n → {−1, 1} and i ∈ [n]. We say that f is unate in the ith direc-
tion if either f (x(i7→−1)) ≤ f (x(i7→1)) for all x (monotone in the ith direction)
or f (x(i7→−1)) ≥ f (x(i7→1)) for all x (antimonotone in the ith direction). We
say that f is unate if it is unate in all n directions.
(a) Show that | ̂f (i)| ≤ Infi[ f ] with equality if and only if f is unate in the
ith direction.
(b) Show that the second statement of Theorem 2.33 holds even for all
unate f .

2.6 Show that linear threshold functions are unate.

2.7 For each function f in Exercise 1.1, compute Inf1[ f ].

2.8 Let f : {−1, 1}n → {−1, 1}. Without using Fourier formulas, show that
Infi[ f ] ≤ Var[ f ] for each i ∈ [n]. (Hint: Show Infi[ f ] ≤ 2 min{Pr[ f =
−1], Pr[ f = 1]}.)

2.9 Let f : {0, 1}
6 → {−1, 1} be given by the weighted majority f (x) = sgn(−58 +
31x1 + 31x2 + 28x3 + 21x4 + 2x5 + 2x6). Compute Infi[ f ] for all i ∈ [6].

2.10 Given b ∈ {−1, 1}, say that coordinate i is b-pivotal for f : {−1, 1}n → {−1, 1}
on input x if f (x) = b and f (x⊕i) ̸= b. Show that Prx[i is b-pivotal on x] =
1
2 Infi[ f ]. Deduce that I[ f ] = 2 Ex[# b-pivotal coordinates on x].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

62 2. Basic concepts and social choice

2.11 Let f : {−1, 1}n → {−1, 1} and suppose ̂f (S) ̸= 0. Show that each coordinate
i ∈ S is relevant for f .

2.12 Let f : {−1, 1}n → {−1, 1} be a random function (as in Exercise 1.7). Com-
pute E[Inf1[ f ]] and E[I[ f ]].

2.13 Let w ∈ N , n = w2w, and write f for Tribesw,2w : {−1, 1}n → {−1, 1}.
(a) Compute E[ f ] and Var[ f ], and estimate them asymptotically in terms
of n.
(b) Describe the function D1 f .
(c) Compute Inf1[ f ] and I[ f ] and estimate them asymptotically.

2.14 Let f : {−1, 1}n → R , and write g = | f |. Show that |Di g| ≤ |Di f | pointwise.
Deduce that Infi[g] ≤ Infi[ f ] and I[g] ≤ I[ f ].

2.15 Prove Proposition 2.24.

2.16 Prove Proposition 2.26.

2.17 Prove Proposition 2.37.

2.18 Let f : {−1, 1}n → R . Show that

L f (x) = d
dρ Tρ f (x)∣
∣
∣
ρ=1 = − d
dt Te−t f (x)
∣
∣
∣t=0.

2.19 Suppose f , g : {−1, 1}n → R have the property that f does not depend on
the ith coordinate and g does not depend on the jth coordinate (i ̸= j).
Show that E[xi x j f (x)g(x)] = E[D j f (x)Di g(x)].

2.20 For f : {−1, 1}n → {−1, 1} we have that E[sens f (x)] = ES∼S f [|S|]. Show that
also E[sens f (x)2] = E[|S|2]. (Hint: Use Proposition 2.37.) Is it true that
E[sens f (x)3] = E[|S|3]?

2.21 Let f : {−1, 1}n → R and i ∈ [n].
(a) Deﬁne Vari f : {−1, 1}n → R by

Vari f (x) = Var
xi [ f (x1, . . . , xi−1, xi, xi+1, . . . , xn)].

Show that Infi[ f ] = Ex[Vari f (x)].
(b) Show that
 Infi[ f ] = 1
2 E
xi,x′
i∼{−1,1}
independent
 [∥
∥
∥ f|xi − f|x′
i
 ∥
∥
∥
2

2
] ,

where f|b denotes the function of n − 1 variables gotten by ﬁxing the
ith input of f to bit b.

2.22 (a) Show that Infi[Majn] = (n−1
n−1
2
 )
2
1−n for all i ∈ [n].

(b) Show that Inf1[Majn] is a decreasing function of (odd) n.
(c) Use Stirling’s Formula m! = (m/e)m(
p
2πm + O(m−1/2)) to deduce that
Inf1[Majn] = p
2/πpn + O(n−3/2). (Here the O(·) terms are nonnegative.)

(d) Deduce that 2/π ≤ W1[Majn] ≤ 2/π + O(n−1).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.6. Exercises and notes 63

(e) Deduce that p
2/πpn ≤ I[Majn] ≤ p
2/πpn + O(n−1/2).
(f ) Suppose n is even and f : {−1, 1}n → {−1, 1} is a majority function.
Show that I[ f ] = I[Majn−1] = p
2/πpn + O(n−1/2).

2.23 Using only Cauchy–Schwarz and Parseval, give a very simple proof of the
following weakening of Theorem 2.33: If f : {−1, 1}n → {−1, 1} is monotone
then I[ f ] ≤ pn. Extend also to the case of f unate (see Exercise 2.5).

2.24 Prove Proposition 2.58 with O(n−1) in place of on(1). (Hint: Show ̂f (i) ≤
p
2/πpn + O(n−3/2) using Theorem 2.33.)

2.25 Deduce Tρ f (x) = ∑S ρ|S| ̂f (S) xS using Exercise 1.4.

2.26 For each function f in Exercise 1.1, compute I[ f ].

2.27 Which functions f : {−1, 1}n → {−1, 1} with #{x : f (x) = 1} = 3 maximize I[ f ]?

2.28 Suppose f : {−1, 1}n → R is an even function (recall Exercise 1.8). Show
the improved Poincaré Inequality Var[ f ] ≤ 1
2 I[ f ].

2.29 Let f : {−1, 1}n → {−1, 1} be unbiased, E[ f ] = 0, and let MaxInf[ f ] denote
maxi∈[n]{Infi[ f ]}.
(a) Use the Poincaré Inequality to show MaxInf[ f ] ≥ 1/n.
(b) Prove that I[ f ] ≥ 2 − nMaxInf[ f ]2. (Hint: Prove I[ f ] ≥ W1[ f ] + 2(1 −
W1[ f ]) and use Exercise 2.5.) Deduce that MaxInf[ f ] ≥ 2
n − 4
n2 .

2.30 Use Exercises 1.1(e),(f ) to deduce the formulas Ei f = ∑S̸∋i ̂f (S) χS and
Tρ f = ∑S ρ|S| ̂f (S) χS.

2.31 Show that Tρ is positivity-preserving for ρ ∈ [−1, 1]; i.e., f ≥ 0 =⇒ Tρ f ≥ 0.
Show that Tρ is positivity-improving for ρ ∈ (−1, 1); i.e., f ≥ 0, f ̸= 0 =⇒
Tρ f > 0.

2.32 Show that Tρ satisﬁes the semigroup property: Tρ1Tρ2 = Tρ1ρ2.

2.33 For ρ ∈ [−1, 1], show that Tρ is a contraction on L p({−1, 1}n) for all p ≥ 1;
i.e., ∥Tρ f ∥p ≤ ∥ f ∥p for all f : {−1, 1}n → R .

2.34 Show that |Tρ f | ≤ Tρ| f | pointwise for any f : {−1, 1}n → R . Further show
that for −1 < ρ < 1, equality occurs if and only if f is everywhere nonneg-
ative or everywhere nonpositive.

2.35 For i ∈ [n] and ρ ∈ R , let Ti
ρ be the operator on functions f : {−1, 1}n → R
deﬁned by
 Ti
ρ f = ρ f + (1 − ρ)Ei f = Ei f + ρLi f .

(a) Show that for ρ ∈ [−1, 1] we have

Ti
ρ f (x) = E
yi∼Nρ(xi)[ f (x1, . . . , xi−1, yi, xi+1, . . . , xn)].

(b) Show that Ti
ρ1Ti
ρ2 = Ti
ρ1ρ2 (cf. Exercise 2.32) and that any two opera-

tors Ti
ρ and T j
ρ′ commute.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

64 2. Basic concepts and social choice

(c) For (ρ1, . . . , ρn) ∈ R n we deﬁne T(ρ1,...,ρn) = T1
ρ1T2
ρ2 · · · Tn
ρn . Show that
T(ρ,...,ρ) is simply Tρ and that T(1,...,1,ρ,1,...,1) (with the ρ in the ith
position) is Ti
ρ.
(d) For ρ1, . . . , ρn ∈ [−1, 1], show that T(ρ1,...,ρn) is a contraction on L p({−1, 1}n)
for all p ≥ 1 (cf. Exercise 2.33).

2.36 Show that Stab−ρ[ f ] = −Stabρ[ f ] if f is odd and Stab−ρ[ f ] = Stabρ[ f ] if
f is even.

2.37 For each function f in Exercise 1.1, compute Stabρ[ f ].

2.38 Compute Stabρ[Tribesw,s].

2.39 Suppose f : {−1, 1}n → {−1, 1} has min(Pr[ f = 1], Pr[ f = −1]) = α. Show
that NSδ[ f ] ≤ 2α for all δ ∈ [0, 1].

2.40 Verify Fact 2.53.

2.41 Fix f : {−1, 1}n → R . Show that Stabρ[ f ] is a convex function of ρ on [0, 1].

2.42 Let f : {−1, 1}n → {−1, 1}. Show that NSδ[ f ] ≤ δI[ f ] for all δ ∈ [0, 1].

2.43 (a) Deﬁne the average inﬂuence of f : {−1, 1}n → R to be EEE [ f ] = 1
n I[ f ]. Now
for f : {−1, 1}n → {−1, 1}, show

EEE [ f ] = Pr
x∼{−1,1}n
i∼[n]
 [ f (x) ̸= f (x⊕i)] and 1−e−2
2 EEE [ f ] ≤ NS1/n[ f ] ≤ EEE [ f ].

(b) Given f : {−1, 1}n → {−1, 1} and integer k ≥ 2, deﬁne

Ak = 1
k (W≥1[ f ] + W≥2[ f ] + · · · + W≥k[ f ]),

the “average of the ﬁrst k tail weights”. Generalizing the second
statement in part (a), show that 1−e−2
2 Ak ≤ NS1/k[ f ] ≤ Ak.

2.44 Suppose f1, . . . , f s : {−1, 1}n → {−1, 1} satisfy NSδ[ f i] ≤ ϵi. Let g : {−1, 1}s →
{−1, 1} and deﬁne h : {−1, 1}n → {−1, 1} by h = g( f1, . . . , f s). Show that
NSδ[h] ≤ ∑s
i=1 ϵi.

2.45 Complete the proof of Proposition 2.54 by showing that (1 − δ)k−1k ≤ 1/δ
for all 0 < δ ≤ 1 and k ∈ N +. (Hint: Compare both sides with 1 + (1 − δ) +
(1 − δ)
2 + · · · + (1 − δ)k−1.)

2.46 Fixing f : {−1, 1}n → R , show the following Lipschitz bound for Stabρ[ f ]
when 0 ≤ ρ − ϵ ≤ ρ < 1:

∣
∣Stabρ[ f ] − Stabρ−ϵ[ f ]
∣
∣ ≤ ϵ · 1
1 − ρ · Var[ f ].

(Hint: Use the Mean Value Theorem and Exercise 2.45.)

2.47 Let f : {−1, 1}n → {−1, 1} be a transitive-symmetric function; in the nota-
tion of Exercise 1.30, this means the group Aut( f ) acts transitively on [n].
Show that Prπ∼Aut( f )[π(i) = j] = 1/n for all i, j ∈ [n].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.6. Exercises and notes 65

2.48 Suppose that F is a functional on functions f : {−1, 1}n → R expressible
as F[ f ] = ∑S cS ̂f (S)
2 where cS ≥ 0 for all S ⊆ [n]. (Examples include Var,
Wk, Infi, I, Inf
(1−δ)
i , and Stabρ for ρ ≥ 0.) Show that F is convex, meaning
F[λ f + (1 − λ)g] ≤ λ F[ f ] + (1 − λ) F[g] for all f , g, and λ ∈ [0, 1].

2.49 Extend the FKN Theorem as follows: Suppose f : {−1, 1}n → {−1, 1} has
W≤1[ f ] ≥ 1 − δ. Show that f is O(δ)-close to a 1-junta. (Hint: Consider
g(x0, x) = x0 f (x0x).)

2.50 Compute the precise probability of a Condorcet winner (under impartial
culture) in a 3-candidate, 3-voter election using f = Maj3.

2.51 (a) Arrow’s Theorem for 3 candidates is slightly more general than what
we stated: it allows for three different unanimous functions f , g, h :
{−1, 1}n → {−1, 1} to be used in the three pairwise elections. But show
that if using f , g, h always gives rise to a Condorcet winner then
f = g = h. (Hint: First show g(x) = − f (−x) for all x by using the fact
that x, y = −x, and z = ( f (x), . . . , f (x)) is always a valid possibility for
the votes.)
(b) Extend Arrow’s Theorem to the case of Condorcet elections with more
than 3 candidates.

2.52 The polarizations of f : {−1, 1}n → R (also known as compressions, down-
shifts, or two-point rearrangements) are deﬁned as follows. For i ∈ [n],
the i-polarization of f is the function f σi : {−1, 1}n → R deﬁned by

f σi (x) =
 {
max{ f (x(i7→+1)), f (x(i7→−1))} if xi = +1,

min { f (x(i7→+1)), f (x(i7→−1))} if xi = −1.

(a) Show that E[ f σi ] = E[ f ] and ∥ f σi ∥p = ∥ f ∥p for all p.
(b) Show that Inf j[ f σi ] ≤ Inf j[ f ] for all j ∈ [n].
(c) Show that Stabρ[ f σi ] ≥ Stabρ[ f ] for all 0 ≤ ρ ≤ 1.
(d) Show that f σi is monotone in the ith direction (recall Exercise 2.5).
Further, show that if f is monotone in the jth direction for some
j ∈ [n] then f σi is still monotone in the jth direction.
(e) Let f ∗ = f σ1σ2···σn . Show that f ∗ is monotone, E[ f ∗] = E[ f ], Inf j[ f ∗] ≤
Inf j[ f ] for all j ∈ [n], and Stabρ[ f ∗] ≥ Stabρ[ f ] for all 0 ≤ ρ ≤ 1.

2.53 The Hamming distance ∆(x, y) = #{i : xi ̸= yi} on the discrete cube {−1, 1}n

is an example of an ℓ1 metric space. For D ≥ 1, we say that the discrete
cube can be embedded into ℓ2 with distortion D if there is a mapping
F : {−1, 1}n → R m for some m ∈ N such that:

∥F(x) − F(y)∥2 ≥ ∆(x, y) for all x, y; (“no contraction”)

∥F(x) − F(y)∥2 ≤ D · ∆(x, y) for all x, y. (“expansion at most D”)

In this exercise you will show that the least distortion possible is D = pn.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

66 2. Basic concepts and social choice

(a) Recalling the deﬁnition of f odd from Exercise 1.8, show that for any
f : {−1, 1}n → R we have ∥ f odd∥
2
2 ≤ I[ f ] and hence

E
x [( f (x) − f (−x))2] ≤ n∑

i=1 E
x
 [( f (x) − f (x⊕i))2]
.

(b) Suppose F : {−1, 1}n → R m, and write F(x) = ( f1(x), f2(x), . . . , f m(x)) for
functions f i : {−1, 1}n → R . By summing the above inequality over
i ∈ [m], show that any F with no contraction must have expansion at
least pn.
(c) Show that there is an embedding F achieving distortion pn.

2.54 Give a Fourier-free proof of the Poincaré Inequality by induction on n.

2.55 Let V be a vector space with norm ∥ · ∥ and ﬁx w1, . . . , wn ∈ V . Deﬁne
g : {−1, 1}n → R by g(x) = ∥ ∑n
i=1 xiwi∥.
(a) Show that Lg ≤ g pointwise. (Hint: Triangle inequality.)
(b) Deduce 2 Var[g] ≤ E[g2] and thus the following Khintchine–Kahane
Inequality:

E
x
 [∥
∥
∥
∥
 n∑

i=1 xiwi
∥
∥
∥
∥

] ≥ 1
p
2 · E
x
 [∥
∥
∥
∥
 n∑

i=1 xiwi
∥
∥
∥
∥

2]1/2 .

(Hint: Exercise 2.28.)
(c) Show that the constant 1p
2 above is optimal, even if V = R .

2.56 In the correlation distillation problem, a source chooses x ∼ {−1, 1}n uni-
formly at random and broadcasts it to q parties. We assume that the
transmissions suffer from some kind of noise, and therefore the players
receive imperfect copies y(1), . . . , y(q) of x. The parties are not allowed to
communicate, and despite having imperfectly correlated information they
wish to agree on a single random bit. In other words, the jth party will
output a bit f j(y( j)) ∈ {−1, 1}, and the goal is to ﬁnd functions f1, . . . , f q that
maximize the probability that f1(y(1)) = f2(y(2)) = · · · = f q(y(q)). To avoid
trivial deterministic solutions, we insist that E[ f j(y( j))] be 0 for all j ∈ [q].
(a) Suppose q = 2, ρ ∈ (0, 1), and y( j) ∼ Nρ(x) independently for each j.
Show that the optimal solution is f1 = f2 = ±χi for some i ∈ [n]. (Hint:
You’ll need Cauchy–Schwarz.)
(b) Show the same result for q = 3.
(c) Let q = 2 and ρ ∈ ( 1
2 , 1). Suppose that y(1) = x exactly, but y(2) ∈

{−1, 0, 1}n has erasures: it’s formed from x by setting y(2)
i = xi with

probability ρ and y(2)
i = 0 with probability 1 − ρ, independently for
all i ∈ [n]. Show that the optimal success probability is 1
2 + 1
2 ρ and
there is an optimal solution in which f1 = ±χi for any i ∈ [n]. (Hint:
Eliminate the source, and introduce a ﬁctitious party 1
′. . . )

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

2.6. Exercises and notes 67

(d) Consider the previous scenario but with ρ ∈ (0, 1
2 ). Show that if n is
sufﬁciently large, then the optimal solution does not have f1 = ±χi.

2.57 (a) Let g : {−1, 1}n → R ≥0 have E[g] = δ. Show that for any ρ ∈ [0, 1],

ρ n∑

j=1 | ̂g( j)| ≤ δ + n∑

k=2 ρk∥g=k∥∞.

(Hint: Exercise 2.31.)
(b) Assume further that g : {−1, 1}n → {0, 1}. Show that ∥g=k∥∞ ≤ p
δ√(n
k)
.

(Hint: First bound ∥g=k∥
2
2.) Deduce ρ ∑n
j=1 | ̂g( j)| ≤ δ + 2ρ2p
δn, assum-

ing ρ ≤ 1
2
pn .

(c) Show that ∑n
j=1 | ̂g( j)| ≤ 2
p
2δ3/4pn (assuming δ ≤ 1/4). Deduce W
1[g] ≤

2p
2 · δ7/4pn. (Hint: show | ̂g( j)| ≤ δ for all j.)
(d) Suppose f : {−1, 1}n → {−1, 1} is monotone and MaxInf[ f ] ≤ δ. Show
W2[ f ] ≤ p
2 · δ3/4 · I[ f ] · pn.
(e) Suppose further that f is unbiased. Show that MaxInf[ f ] ≤ o(n−2/3)
implies I[ f ] ≥ 3− o(1); conclude MaxInf[ f ] ≥ 3
n − o(1/n). (Hint: Extend
Exercise 2.29.) Use Exercise 2.52 to remove the assumption that f is
monotone for these statements.

2.58 Let V be a vector space (over R ) with norm ∥ · ∥V . If f : {−1, 1}n → V we
can deﬁne its Fourier coefﬁcients ̂f (S) ∈ V by the usual formula ̂f (S) =
Ex∈{−1,1}n [ f (x)xS]. We may also deﬁne ∥ f ∥p = Ex∈{−1,1}n [∥ f (x)∥p
V ]1/p. Fi-
nally, if the norm ∥ · ∥V arises from an inner product 〈·, ·〉V on V we
can deﬁne an inner product on functions f , g : {−1, 1}n → V by 〈 f , g〉 =
Ex∈{−1,1}n [〈 f (x), g(x)〉V ]. The material developed so far in this book has
used V = R with 〈·, ·〉V being multiplication. Explore the extent to which
this material extends to the more general setting.

Notes. The mathematical study of social choice began in earnest in the late
1940s; see Riker [Rik61] for an early survey or the compilation [BGR09]
for some modern results. Arrow’s Theorem was the ﬁeld’s ﬁrst major re-
sult; Arrow proved it in 1950 [Arr50] under the extra assumption of mono-
tonicity (and with a minor error [Bla57]), with the reﬁned version appearing
in 1963 [Arr63]. He was awarded the Nobel Prize for this work in 1972.
May’s Theorem is from 1952 [May52]. Guilbaud’s Formula is also from
1952 [Gui52], though Guilbaud only stated it in a footnote and wrote that it is
computed “by the usual means in combinatorial analysis”. The ﬁrst published
proof appears to be due to Garman and Kamien [GK68]; they also introduced
the impartial culture assumption. The term “junta” appears to have been
introduced by Parnas, Ron, and Samorodnitsky [PRS01].

The notion of inﬂuence Infi[ f ] was originally introduced by the geneticist
Penrose [Pen46], who observed that Infi[Majn] ∼ p
2/πpn . It was rediscovered

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

68 2. Basic concepts and social choice

by the lawyer Banzhaf in 1965 [Ban65]; he sued the Nassau County (NY)
Board after proving that the voting system it used (the one in Exercise 2.9)
gave some towns zero inﬂuence. Inﬂuence is sometimes referred to as the
Banzhaf, Penrose–Banzhaf, or Banzhaf–Coleman index (Coleman being an-
other rediscoverer [Col71]). Inﬂuences were ﬁrst studied in the computer
science literature by Ben-Or and Linial [BL85]; they introduced also intro-
duced “tribes” as an example of a function with constant variance yet small
inﬂuences. The Fourier formulas for inﬂuence may have ﬁrst appeared in the
work of Chor and Geréb-Graus [CGG87].

Total inﬂuence of Boolean functions has long been studied in combina-
torics, since it is equivalent to edge-boundary size for subsets of the Ham-
ming cube. For example, the edge-isoperimetric inequality was ﬁrst proved
by Harper in 1964 [Har64]. In the context of Boolean functions, Karpovsky
[Kar76] proposed I[ f ] as a measure of the computational complexity of f ,
and Hurst, Miller, and Muzio [HMM82] gave the Fourier formula ∑S |S| ̂f (S)
2.
The terminology “Poincaré Inequality” comes from the theory of functional
inequalities and Markov chains; the inequality is equivalent to the spectral
gap for the discrete cube graph.

The noise stability of Boolean functions was ﬁrst studied explicitly by
Benjamini, Kalai, and Schramm in 1999 [BKS99], though it plays an impor-
tant role in the earlier work of Håstad [Hås97]. See O’Donnell [O’D03] for a
survey. The noise operator was introduced by Bonami [Bon70] and indepen-
dently by Beckner [Bec75], who used the notation Tρ which was standardized
by Kahn, Kalai, and Linial [KKL88]. For nonnegative noise rates it’s often
natural to use the alternate parameterization Te−t for t ∈ [0, ∞].

The Fourier approach to Arrow’s Theorem is due to Kalai [Kal02]; he
also proved Theorem 2.57 and Corollary 2.60. The FKN Theorem is due to
Friedgut, Kalai, and Naor [FKN02]; the observation from Exercise 2.49 is
due to Kindler.

The polarizations from Exercise 2.52 originate in Kleitman [Kle66]. Exer-
cise 2.53 is a theorem of Enﬂo from 1970 [Enf70]. Exercise 2.55 is a theorem
of Latała and Oleszkiewicz [LO94]. In Exercise 2.56, part (b) is due to Mos-
sel and O’Donnell [MO05]; part (c) was conjectured by Yang [Yan04] and
proved by O’Donnell and Wright [OW12]. Exercise 2.57 is a polishing of the
1987 work by Chor and Geréb-Graus [CGG87, CGG88], a precursor of the
KKL Theorem. The weaker Exercise 2.29 is also due to them and Noga Alon
independently.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 3

Spectral structure and
learning

One reasonable way to assess the “complexity” of a Boolean function is in
terms how complex its Fourier spectrum is. For example, functions with
sufﬁciently simple Fourier spectra can be efﬁciently learned from examples.
This chapter will be concerned with understanding the location, magnitude,
and structure of a Boolean function’s Fourier spectrum.

3.1. Low-degree spectral concentration

One way a Boolean function’s Fourier spectrum can be “simple” is for it to be
mostly concentrated at small degree.

Deﬁnition 3.1. We say that the Fourier spectrum of f : {−1, 1}n → R is ϵ-
concentrated on degree up to k if

W
>k[ f ] = ∑

S⊆[n]
|S|>k
 ̂f (S)2 ≤ ϵ.

For f : {−1, 1}n → {−1, 1} we can express this condition using the spectral
sample: PrS∼S f [|S| > k] ≤ ϵ.

It’s possible to show such a concentration result combinatorially by show-
ing that a function has small total inﬂuence:

Proposition 3.2. For any f : {−1, 1}n → R and ϵ > 0, the Fourier spectrum of
f is ϵ-concentrated on degree up to I[ f ]/ϵ.
 69

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

70 3. Spectral structure and learning

Proof. This follows immediately from Theorem 2.38, I[ f ] = ∑n
k=0 k · Wk[ f ].
For f : {−1, 1}n → {−1, 1}, this is Markov’s inequality applied to the cardinality
of the spectral sample. □

For example, in Exercise 2.13 you showed that I[Tribesw,2w ] ≤ O(log n),
where n = w2w; thus this function’s spectrum is .01-concentrated on degree
up to O(log n), a rather low level. Proving this by explicitly calculating Fourier
coefﬁcients would be quite painful.

Another means of showing low-degree spectral concentration is through
noise stability/sensitivity:

Proposition 3.3. For any f : {−1, 1}n → {−1, 1} and δ ∈ (0, 1/2], the Fourier
spectrum of f is ϵ-concentrated on degree up to 1/δ for

ϵ = 2
1−e−2 NSδ[ f ] ≤ 3NSδ[ f ].

Proof. Using the Fourier formula from Theorem 2.49,

2NSδ[ f ] = E
S∼S f [1 − (1 − 2δ)
|S|]

≥ (1 − (1 − 2δ)
1/δ) · Pr
S∼S f [|S| ≥ 1/δ]

≥ (1 − e−2) · Pr
S∼S f [|S| ≥ 1/δ],

where the ﬁrst inequality used that 1−(1−2δ)k is a nonnegative nondecreasing
function of k. The claim follows. □

As an example, Theorem 2.45 tells us that for δ > 0 sufﬁciently small and n
sufﬁciently large (as a function of δ), NSδ[Majn] ≤ p
δ. Hence the Fourier
spectrum of Majn is 3p
δ-concentrated on degree up to 1/δ; equivalently, it
is ϵ-concentrated on degree up to 9/ϵ2. (We will give sharp constants for
majority’s spectral concentration in Chapter 5.3.) This example also shows
there is no simple converse to Proposition 3.2; although Majn has its spectrum
.01-concentrated on degree up to O(1), its total inﬂuence is Θ(
pn).

Finally, suppose a function f : {−1, 1}n → {−1, 1} has its Fourier spectrum
0-concentrated up to degree k; in other words, f has real degree deg( f ) ≤ k. In
this case f must be somewhat simple; indeed, if k is a constant, then f is a
junta:

Theorem 3.4. Suppose f : {−1, 1}n → {−1, 1} has deg( f ) ≤ k. Then f is a k2k−1-
junta.

The bound k2k−1 cannot be signiﬁcantly improved; see Exercise 3.24. The
key to proving Theorem 3.4 is the following lemma, the proof of which is
outlined in Exercise 3.4:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.2. Subspaces and decision trees 71

Lemma 3.5. Suppose deg( f ) ≤ k, where f : {−1, 1}n → R is not identically 0.
Then Pr[ f (x) ̸= 0] ≥ 2−k.

Since deg(Di f ) ≤ k − 1 when deg( f ) ≤ k (by the “differentiation” formula)
and since Infi[ f ] = Pr[Di f (x) ̸= 0] for Boolean-valued f , we immediately infer:

Proposition 3.6. If f : {−1, 1}n → {−1, 1} has deg( f ) ≤ k then Infi[ f ] is either 0
or at least 21−k for all i ∈ [n].

We can now give the proof of Theorem 3.4. From Proposition 3.6 the
number of coordinates which have nonzero inﬂuence on f is at most I[ f ]/2
1−k,
and this in turn is at most k2k−1 by the following fact:

Fact 3.7. For f : {−1, 1}n → {−1, 1}, I[ f ] ≤ deg( f ).

Fact 3.7 is immediate from the Fourier formula for total inﬂuence.

We remark that the FKN Theorem (stated in Chapter 2.5) is a “robust”
version of Theorem 3.4 for k = 1. In Chapter 9.6 we will see Friedgut’s Junta
Theorem, a related robust result showing that if I[ f ] ≤ k then f is ϵ-close to a
2O(k/ϵ)-junta.

3.2. Subspaces and decision trees

In this section we will treat the domain of a Boolean function as F n
2 , an n-
dimensional vector space over the ﬁeld F 2. As mentioned in Chapter 1.2, it
can be natural to index the Fourier characters χS : F n
2 → {−1, 1} not by subsets
S ⊆ [n] but by their 0-1 indicator vectors γ ∈ F n
2 ; thus

χγ(x) = (−1)γ·x,

with the dot product γ·x being carried out in F n
2 . For example, in this notation
we’d write χ0 for the constantly 1 function and χe i for the ith dictator. Fact 1.6
now becomes
 χβχγ = χβ+γ ∀β, γ. (3.1)

Thus the characters form a group under multiplication, which is isomorphic
to the group F n
2 under addition. To distinguish this group from the input
domain we write it as ̂F n
2 ; we also tend to identify the character with its index.
Thus the Fourier expansion of f : F n
2 → R can be written as

f (x) = ∑

γ∈ ̂F n
2
 ̂f (γ)χγ(x).

The Fourier transform of f can be thought of as a function ̂f : ̂F n
2 → R . We
can measure its complexity with various norms.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

72 3. Spectral structure and learning

Deﬁnition 3.8. The Fourier (or spectral) p-norm of f : {−1, 1}n → R is

ˆ∥ f ˆ∥p =
 

 ∑

γ∈ ̂F n
2
 | ̂f (γ)|p



1/p
 .

Note that we use the “counting measure” on ̂F n
2 , and hence we have a nice
rephrasing of Parseval’s Theorem: ∥ f ∥2 = ˆ∥ f ˆ∥2. We make two more deﬁnitions
relating to the simplicity of ̂f :

Deﬁnition 3.9. The Fourier (or spectral) sparsity of f : {−1, 1}n → R is

sparsity( ̂f ) = |supp( ̂f )| = #{
γ ∈ ̂F n
2 : ̂f (γ) ̸= 0}
.

Deﬁnition 3.10. We say that ̂f is ϵ-granular if ̂f (γ) is an integer multiple
of ϵ for all γ ∈ ̂F n
2 .

To gain some practice with this notation, let’s look at the Fourier trans-
forms of some indicator functions 1A : F n
2 → {0, 1} and probability density
functions ϕA, where A ⊆ F n
2 . First, suppose A ≤ F n
2 is a subspace. Then one
way to characterize A is by its perpendicular subspace A⊥:

A⊥ = {γ ∈ ̂F n
2 : γ · x = 0 for all x ∈ A}.

It holds that dim A⊥ = n − dim A (this is called the codimension of A) and that
A = (A⊥)
⊥.

Proposition 3.11. If A ≤ F n
2 has codim A = dim A⊥ = k, then

1A = ∑

γ∈A⊥ 2−kχγ, ϕA = ∑

γ∈A⊥ χγ.

Proof. Let γ1, . . . , γk form a basis of A⊥. Since A = (A⊥)
⊥ it follows that x ∈ A
if and only if χγi (x) = 1 for all i ∈ [k]. We therefore have

1A(x) = k∏

i=1
( 1
2 + 1
2 χγi (x)) = 2
−k ∑

γ∈span{γ1,...,γk} χγ(x)

as claimed, where the last equality used (3.1). The Fourier expansion of ϕA
follows because E[1A] = 2−k. □

More generally, suppose A is afﬁne subspace (or coset) of F n
2 ; i.e., A = H +a
for some H ≤ F n
2 and a ∈ F n
2 , or equivalently

A = {x ∈ F n
2 : γ · x = γ · a for all γ ∈ H⊥}.

Then it is easy (Exercise 3.11) to extend Proposition 3.11 to:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.2. Subspaces and decision trees 73

Proposition 3.12. If A = H + a is an afﬁne subspace of codimension k, then

̂1A(γ) =
 {
χγ(a)2
−k if γ ∈ H⊥

0 else;

hence ϕA = ∑
γ∈H⊥ χγ(a)χγ. We have sparsity( ̂1A) = 2k, ̂1A is 2−k-granular,
ˆ∥1A ˆ∥∞ = 2−k, and ˆ∥1A ˆ∥1 = 1.

In computer science terminology, any f : F n
2 → {0, 1} that is a conjunction
of parity conditions is the indicator of an afﬁne subspace (or the zero function).
In the simple case that the parity conditions are all of the form “xi = ai”, the
function is a logical AND of literals, and we call the afﬁne subspace a subcube.

Another class of Boolean functions with simple Fourier spectra are the
ones computable by simple decision trees:

Deﬁnition 3.13. A decision tree T is a representation of a Boolean function
f : F n
2 → R . It consists of a rooted binary tree in which the internal nodes are
labeled by coordinates i ∈ [n], the outgoing edges of each internal node are
labeled 0 and 1, and the leaves are labeled by real numbers. We insist that no
coordinate i ∈ [n] appears more than once on any root-to-leaf path.

On input x ∈ F n
2 , the tree T constructs a computation path from the root
node to a leaf. Speciﬁcally, when the computation path reaches an internal
node labeled by coordinate i ∈ [n] we say that T queries xi; the computation
path then follows the outgoing edge labeled by xi. The output of T (and
hence f ) on input x is the label of the leaf reached by the computation path.
We often identify a tree with the function it computes.

For decision trees, a picture is worth a thousand words; see Figure 3.1.

Figure 3.1. Decision tree computing Sort3

(It’s traditional to write xi rather than i for the internal node labels.) For
example, the computation path of the above tree on input x = (0, 1, 0) ∈ F 3
2
starts at the root, queries x1, proceeds left, queries x3, proceeds left, queries

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

74 3. Spectral structure and learning

x2, proceeds right, and reaches a leaf labeled 0. In fact, this tree computes the
function Sort3 deﬁned by Sort3(x) = 1 if and only if x1 ≤ x2 ≤ x3 or x1 ≥ x2 ≥ x3.

Deﬁnition 3.14. The size s of a decision tree T is the total number of leaves.
The depth k of T is the maximum length of any root-to-leaf path. For decision
trees over F n
2 we have k ≤ n and s ≤ 2k. Given f : F n
2 → R we write DT( f )
(respectively, DTsize( f )) for the least depth (respectively, size) of a decision
tree computing f . (Note that these are not necessarily achieved by the same
tree.)

The example decision tree above has size 6 and depth 3.

Let T be a decision tree computing f : F n
2 → R and let P be one of its
root-to-leaf paths. The set of inputs x that follow computation path P in T is
precisely a subcube of F n
2 , call it CP . The function f is constant on CP ; we
will call its value there f (P). Further, since every input x follows a unique
path in T, the subcubes {CP : P a path in T} form a partition of F n
2 . These
observations yield the following “spectral simplicity” results for decision trees:

Fact 3.15. Let f : F n
2 → R be computed by a decision tree T. Then

f = ∑

paths P of T f (P) · 1CP .

Proposition 3.16. Let f : F n
2 → R be computed by a decision tree T of size s
and depth k. Then:

• deg( f ) ≤ k;

• sparsity( ̂f ) ≤ s2k ≤ 4k;

• ˆ∥ f ˆ∥1 ≤ ∥ f ∥∞ · s ≤ ∥ f ∥∞ · 2k;

• ̂f is 2
−k-granular assuming f : F n
2 → Z .

Proposition 3.17. Let f : F n
2 → {−1, 1} be computable by a decision tree of
size s and let ϵ ∈ (0, 1]. Then the spectrum of f is ϵ-concentrated on degree up
to log(s/ϵ).

You are asked to prove these propositions in Exercises 3.21 and 3.22. Sim-
ilar spectral simplicity results hold for some generalizations of the decision
tree representation (“subcube partitions”, “parity decision trees”); see Exer-
cise 3.26.

3.3. Restrictions

A common operation on Boolean functions f : {−1, 1}n → R is restriction to
subcubes. Suppose [n] is partitioned into two sets, J and J = [n] \ J. If the
inputs bits in J are ﬁxed to constants, the result is a function {−1, 1}J → R .
For example, if we take the function Maj5 : {−1, 1}
5 → {−1, 1} and restrict the

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.3. Restrictions 75

4th and 5th coordinates to be 1 and −1 respectively, we obtain the function
Maj3 : {−1, 1}
3 → {−1, 1}. If we further restrict the 3rd coordinate to be −1, we
obtain the two-bit function which is 1 if and only if both input bits are 1.

We introduce following notation:

Deﬁnition 3.18. Let f : {−1, 1}n → R and let (J, J) be a partition of [n]. Let
z ∈ {−1, 1}J. Then we write f J|z : {−1, 1}J → R (pronounced “the restriction
of f to J using z”) for the subfunction of f given by ﬁxing the coordinates
in J to the bit values z. When the partition (J, J) is understood we may
write simply f|z. If y ∈ {−1, 1}J and z ∈ {−1, 1}J we will sometimes write (y, z)
for the composite string in {−1, 1}n, even though y and z are not literally
concatenated; with this notation, f J|z(y) = f (y, z).

Let’s examine how restrictions affect the Fourier transform by considering
an example.

Example 3.19. Let f : {−1, 1}
4 → {−1, 1} be the function deﬁned by

f (x) = 1 ⇐⇒ x3 = x4 = −1 or x1 ≥ x2 ≥ x3 ≥ x4 or x1 ≤ x2 ≤ x3 ≤ x4.
(3.2)
You can check that f has the Fourier expansion

f (x) = + 1
8 − 1
8 x1 + 1
8 x2 − 1
8 x3 − 1
8 x4

+ 3
8 x1x2 + 1
8 x1x3 − 3
8 x1x4 + 3
8 x2x3 − 1
8 x2x4 + 5
8 x3x4 (3.3)

+ 1
8 x1x2x3 + 1
8 x1x2x4 − 1
8 x1x3x4 + 1
8 x2x3x4 − 1
8 x1x2x3x4.

Consider the restriction x3 = 1, x4 = −1, and let f ′ = f{1,2}|(1,−1) be the restricted
function of x1 and x2. From the original deﬁnition (3.2) of f we see that
f ′(x1, x2) is 1 if and only if x1 = x2 = 1. This is the min2 function of x1 and x2,
which we know has Fourier expansion

f ′(x1, x2) = min2(x1, x2) = − 1
2 + 1
2 x1 + 1
2 x2 + 1
2 x1x2. (3.4)

We can of course obtain this expansion simply by plugging x3 = 1, x4 = −1
into (3.3). Now suppose we only wanted to know the coefﬁcient on x1 in the
Fourier expansion of f ′. We can ﬁnd it as follows: Consider all monomials
in (3.3) that contain x1 and possibly also x3, x4; substitute x3 = 1, x4 = −1 into
the associated terms; and sum the results. The relevant terms in (3.3) are
− 1
8 x1, + 1
8 x1x3, − 3
8 x1x4, − 1
8 x1x3x4, and substituting in x3 = 1, x4 = −1 gives us
− 1
8 + 1
8 + 3
8 + 1
8 = 1
2 , as expected from (3.4).

Now we work out these ideas more generally. In the setting of Deﬁni-
tion 3.18 the restricted function f J|z has {−1, 1}J as its domain. Thus its
Fourier coefﬁcients are indexed by subsets of J. Let’s introduce notation for
the Fourier coefﬁcients of a restricted function:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

76 3. Spectral structure and learning

Deﬁnition 3.20. Let f : {−1, 1}n → R and let (J, J) be a partition of [n]. Let
S ⊆ J. Then we write FS|J f : {−1, 1}J → R for the function ̂f J|•(S); i.e.,

FS|J f (z) = ̂f J|z(S).

When the partition (J, J) is understood we may write simply FS| f .

In Example 3.19 we considered J = {3, 4}, S = {1}, and z = (1, −1). See
Figure 3.2 for an illustration of a typical restriction scenario.

Figure 3.2. Notation for a typical restriction scenario. Note that J and J
need not be literally contiguous.

In general, for a ﬁxed partition (J, J) of [n] and a ﬁxed S ⊆ J, we may wish
to know what ̂f J|z(S) is as a function of z ∈ {−1, 1}J. This is precisely asking for

the Fourier transform of FS|J f . Since the function FS|J f has domain {−1, 1}J,

its Fourier transform has coefﬁcients indexed by subsets of J. The formula
for this Fourier transform generalizes the computation we used at the end of
Example 3.19:

Proposition 3.21. In the setting of Deﬁnition 3.20 we have the Fourier expan-
sion
 FS|J f (z) = ∑

T⊆J
 ̂f (S ∪ T)zT ;

i.e., …FS|J f (T) = ̂f (S ∪ T).

Proof. (The S = ; case here is Exercise 1.15.) Every U ⊆ [n] indexing f ’s
Fourier coefﬁcients can be written as a disjoint union U = S ∪ T, where S ⊆ J
and T ⊆ J. We can also decompose any x ∈ {−1, 1}n into two substrings y ∈
{−1, 1}J and z ∈ {−1, 1}J. We have x
U = yS zT and so

f (x) = ∑

U⊆[n] ̂f (U) x
U = ∑

S⊆J
T⊆J
 ̂f (S ∪ T) yS zT = ∑

S⊆J
( ∑

T⊆J
 ̂f (S ∪ T) zT )yS.

Thus when z is ﬁxed, the resulting function of y indeed has ∑T⊆J ̂f (S ∪ T) zT

as its Fourier coefﬁcient on the monomial yS. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.3. Restrictions 77

Corollary 3.22. Let f : {−1, 1}n → R , let (J, J) be a partition of [n], and ﬁx
S ⊆ J. Suppose z ∼ {−1, 1}J is chosen uniformly at random. Then

E
z [ ̂f J|z(S)] = ̂f (S),

E
z [ ̂f J|z(S)
2] = ∑

T⊆J
 ̂f (S ∪ T)
2.

Proof. The ﬁrst statement is immediate from Proposition 3.21, taking T = ;
and unraveling the deﬁnition. As for the second statement,

E
z [ ̂f J|z(S)2] = E
z [FS|J f (z)2] (by deﬁnition)

= ∑

T⊆J
 …FS|J f (T)
2 (Parseval)

= ∑

T⊆J
 ̂f (S ∪ T)2 (Proposition 3.21) □

We move on to discussing a more general kind of restriction; namely,
restricting a function f : F n
2 → R to an afﬁne subspace H + z. This generalizes
restriction to subcubes as we’ve seen so far, by considering H = span{e i : i ∈ J}
for a given subset J ⊆ [n]. For restrictions to a subspace H ≤ F n
2 we have a
natural deﬁnition:

Deﬁnition 3.23. If f : F n
2 → R and H ≤ F n
2 is a subspace, we write f H : H → R
for the restriction of f to H.

For restrictions to afﬁne subspaces, we run into difﬁculties if we try to
extend our notation for restrictions to subcubes. Unlike in the subcube case
of H = span{e i : i ∈ J}, we don’t in general have a canonical isomorphism
between H and a coset H + z. Thus it’s not natural to introduce notation
such as f H|z : H → R for the function h 7→ f (h + z), because such a deﬁnition
depends on the choice of representative for H + z. As an example consider
H = {(0, 0), (1, 1)} ≤ F 2
2, a 1-dimensional subspace (which satisﬁes H⊥ = H).
Here the nontrivial coset is H + (1, 0) = H + (0, 1) = {(1, 0), (0, 1)}, which has no
canonical representative.

To get around this difﬁculty we can view restriction to a coset H + z as
consisting of two steps: ﬁrst, translation of the domain by a ﬁxed representa-
tive z, and then restriction to the subspace H. Let’s introduce some notation
for the ﬁrst operation:

Deﬁnition 3.24. Let f : F n
2 → R and let z ∈ F n
2 . We deﬁne the function
f +z : F n
2 → R by f +z(x) = f (x + z).

By substituting x = x + z into the Fourier expansion of f , we deduce:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

78 3. Spectral structure and learning

Fact 3.25. The Fourier coefﬁcients of f +z are given by ̂f +z(γ) = (−1)
γ·z ̂f (γ); i.e.,

f +z(x) = ∑

γ∈ ̂F n
2
 χγ(z) ̂f (γ) χγ(x).

(This fact also follows by noting that f +z = ϕ{z} ∗ f ; see Exercise 3.31.)

We can now give notation for the restriction of a function to an afﬁne
subspace:

Deﬁnition 3.26. Let f : F n
2 → R , z ∈ F n
2 , H ≤ F n
2 . We write f +z
H : H → R
for the function ( f +z)H; namely, the restriction of f to coset H + z with the
representative z made explicit.

Finally, we would like to consider Fourier coefﬁcients of restricted func-
tions f +z
H . These can be indexed by the cosets of H⊥ in ̂F n
2 . However, we again
have a notational difﬁculty since the only coset with a canonical representa-
tive is H⊥ itself, with representative 0. There is no need to introduce extra
notation for ̂f +z
H (0), the average value of f on coset H + z, since it is just

E
h∼H[ f (h + z)] = 〈ϕH, f +z〉.

Applying Plancherel on the right-hand side, as well as Proposition 3.11 and
Fact 3.25, we deduce the following classical fact:

Poisson Summation Formula. Let f : F n
2 → R , H ≤ F n
2 , z ∈ F n
2 . Then

E
h∼H[ f (h + z)] = ∑

γ∈H⊥ χγ(z) ̂f (γ).

3.4. Learning theory

Computational learning theory is an area of algorithms research devoted to
the following task: Given a source of “examples” (x, f (x)) from an unknown
function f , compute a “hypothesis” function h that is good at predicting f (y)
on future inputs y. In this book we will focus on just one possible formulation
of the task:

Deﬁnition 3.27. In the model of PAC (“Probably Approximately Correct”)
learning under the uniform distribution on {−1, 1}n, a learning problem is
identiﬁed with a concept class C , which is just a collection of functions f :
{−1, 1}n → {−1, 1}. A learning algorithm A for C is a randomized algorithm
which has limited access to an unknown target function f ∈ C . The two access
models, in increasing order of strength, are:

• random examples, meaning A can draw pairs (x, f (x)) where x ∈ {−1, 1}n

is uniformly random;

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.4. Learning theory 79

• queries, meaning A can request the value f (x) for any x ∈ {−1, 1}n of its
choice.

In addition, A is given as input an accuracy parameter ϵ ∈ [0, 1/2]. The output
of A is required to be (the circuit representation of) a hypothesis function
h : {−1, 1}n → {−1, 1}. We say that A learns C with error ϵ if for any f ∈ C ,
with high probability A outputs an h which is ϵ-close to f : i.e., satisﬁes
dist( f , h) ≤ ϵ.

In the above deﬁnition, the phrase “with high probability” can be ﬁxed
to mean, say, “except with probability at most 1/10”. (As is common with
randomized algorithms, the choice of constant 1/10 is unimportant; see Exer-
cise 3.40.)

For us, the main desideratum of a learning algorithm is efﬁcient running
time. One can easily learn any function f to error 0 in time ̃O(2n) (see Exer-
cise 3.33); however, this is not very efﬁcient. If the concept class C contains
very complex functions, then such exponential running time is necessary;
however, if C contains only relatively “simple” functions, then more efﬁcient
learning may be possible. For example, the results of Section 3.5 show that
the concept class
 C = { f : F n
2 → {−1, 1} | DTsize( f ) ≤ s}

can be learned with queries to error ϵ by an algorithm whose running time is
poly(s, n, 1/ϵ).

A common way of trying to learn an unknown target f : {−1, 1}n → {−1, 1}
is by discovering “most of” its Fourier spectrum. To formalize this, let’s gener-
alize Deﬁnition 3.1:

Deﬁnition 3.28. Let F be a collection of subsets S ⊆ [n]. We say that the
Fourier spectrum of f : {−1, 1}n → R is ϵ-concentrated on F if
∑

S⊆[n]
S∉F
 ̂f (S)
2 ≤ ϵ.

For f : {−1, 1}n → {−1, 1} we can express this condition using the spectral
sample: PrS∼S f [S ∉ F ] ≤ ϵ.

Most functions don’t have their Fourier spectrum concentrated on a small
collection (see Exercise 3.35). But for those that do, we may hope to discover
“most of” their Fourier coefﬁcients. The main result of this section is a kind of
“meta-algorithm” for learning an unknown target f . It reduces the problem of
learning f to the problem of identifying a collection of characters on which f ’s
Fourier spectrum is concentrated.

Theorem 3.29. Assume learning algorithm A has (at least) random example
access to target f : {−1, 1}n → {−1, 1}. Suppose that A can – somehow – identify a

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

80 3. Spectral structure and learning

collection F of subsets on which f ’s Fourier spectrum is ϵ/2-concentrated. Then
using poly(|F |, n, 1/ϵ) additional time, A can with high probability output a
hypothesis h that is ϵ-close to f .

The idea of the theorem is that A will estimate all of f ’s Fourier coefﬁ-
cients in F , obtaining a good approximation to f ’s Fourier expansion. Then
A’s hypothesis will be the sign of this approximate Fourier expansion.

The ﬁrst tool we need to prove Theorem 3.29 is the ability to accurately
estimate any ﬁxed Fourier coefﬁcient:

Proposition 3.30. Given access to random examples from f : {−1, 1}n →
{−1, 1}, there is a randomized algorithm which takes as input S ⊆ [n], 0 <
δ, ϵ ≤ 1/2, and outputs an estimate ̃f (S) for ̂f (S) that satisﬁes

| ̃f (S) − ̂f (S)| ≤ ϵ

except with probability at most δ. The running time is poly(n, 1/ϵ) · log(1/δ).

Proof. We have ̂f (S) = Ex[ f (x)χS(x)]. Given random examples (x, f (x)), the
algorithm can compute f (x)χS(x) ∈ {−1, 1} and therefore empirically estimate
Ex[ f (x)χS(x)]. A standard application of the Chernoff bound implies that
O(log(1/δ)/ϵ2) examples are sufﬁcient to obtain an estimate within ±ϵ with
probability at least 1 − δ. □

The second observation we need to prove Theorem 3.29 is the following:

Proposition 3.31. Suppose that f : {−1, 1}n → {−1, 1} and g : {−1, 1}n → R
satisfy ∥ f − g∥
2
2 ≤ ϵ. Let h : {−1, 1}n → {−1, 1} be deﬁned by h(x) = sgn(g(x)),
with sgn(0) chosen arbitrarily from {−1, 1}. Then dist( f , h) ≤ ϵ.

Proof. Since | f (x) − g(x)|2 ≥ 1 whenever f (x) ̸= sgn(g(x)), we conclude

dist( f , h) = Pr
x [ f (x) ̸= h(x)] = E
x [1 f (x)̸=sgn(g(x))] ≤ E
x [| f (x)− g(x)|2] = ∥ f − g∥
2
2. □

(See Exercise 3.34 for an improvement to this argument.)

We can now prove Theorem 3.29:

Proof of Theorem 3.29. For each S ∈ F the algorithm uses Proposition 3.30
to produce an estimate ̃f (S) for ̂f (S) which satisﬁes | ̃f (S)− ̂f (S)| ≤ p
ϵ/(2
p
|F |)
except with probability at most 1/(10|F |). Overall this requires poly(|F |, n, 1/ϵ)
time, and by the union bound, except with probability at most 1/10 all |F |
estimates have the desired accuracy. Finally, A forms the real-valued function
g = ∑S∈F ̃f (S)χS and outputs hypothesis h = sgn(g). By Proposition 3.31, it

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.4. Learning theory 81

sufﬁces to show that ∥ f − g∥
2
2 ≤ ϵ. And indeed,

∥ f − g∥
2
2 = ∑

S⊆[n] †f − g(S)2 (Parseval)

= ∑

S∈F ( ̂f (S) − ̃f (S))2 + ∑

S∉F ̂f (S)
2

≤ ∑

S∈F
 ( p
ϵ

2p
|F |
 )2 + ϵ/2 (estimates, concentration assumption)

= ϵ/4 + ϵ/2 ≤ ϵ,

as desired. □

As we described, Theorem 3.29 reduces the algorithmic task of learning f
to the algorithmic task of identifying a collection F on which f ’s Fourier
spectrum is concentrated. In Section 3.5 we will describe the Goldreich–Levin
algorithm, a sophisticated way to ﬁnd such an F assuming query access to f .
For now, though, we observe that for several interesting concept classes we
don’t need to do any algorithmic searching for F ; we can just take F to be
all sets of small cardinality. This works whenever all functions in C have
low-degree spectral concentration.

The “Low-Degree Algorithm”. Let k ≥ 1 and let C be a concept class for
which every function f : {−1, 1}n → {−1, 1} in C is ϵ/2-concentrated up to de-
gree k. Then C can be learned from random examples only with error ϵ in time
poly(nk, 1/ϵ).

Proof. Apply Theorem 3.29 with F = {S ⊆ [n] : |S| ≤ k}. We have |F | =
∑k
j=0 (n
j) ≤ O(nk). □

The Low-Degree Algorithm reduces the algorithmic problem of learning C
from random examples to the analytic task of showing low-degree spectral
concentration for the functions in C . Using the results of Section 3.1 we can
quickly obtain some learning-theoretic results. For example:

Corollary 3.32. For t ≥ 1, let C = { f : {−1, 1}n → {−1, 1} | I[ f ] ≤ t}. Then C is
learnable from random examples with error ϵ in time nO(t/ϵ).

Proof. Use the Low-Degree Algorithm with k = 2t/ϵ; the result follows from
Proposition 3.2. □

Corollary 3.33. Let C = { f : {−1, 1}n → {−1, 1} | f is monotone}. Then C is
learnable from random examples with error ϵ in time nO(pn/ϵ).

Proof. Follows from the previous corollary and Theorem 2.33. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

82 3. Spectral structure and learning

You might be concerned that a running time such as nO(pn) does not
seem very efﬁcient. Still, it’s much better than the trivial running time of
̃O(2n). Further, as we will see in the next section, learning algorithms are
sometimes used in attacks on cryptographic schemes, and in this context even
subexponential-time algorithms are considered dangerous.

Continuing with applications of the Low-Degree Algorithm:

Corollary 3.34. For δ ∈ (0, 1/2], let C = { f : {−1, 1}n → {−1, 1} | NSδ[ f ] ≤ ϵ/6}.
Then C is learnable from random examples with error ϵ in time poly(n1/δ, 1/ϵ).

Proof. Follows from Proposition 3.3. □

Corollary 3.35. Let C = { f : {−1, 1}n → {−1, 1} | DTsize( f ) ≤ s}. Then C is
learnable from random examples with error ϵ in time nO(log(s/ϵ)).

Proof. Follows from Proposition 3.17. □

With a slight extra twist one can also exactly learn the class of degree-k
functions in time poly(nk); see Exercise 3.36:

Theorem 3.36. Let k ≥ 1 and let C = { f : {−1, 1}n → {−1, 1} | deg( f ) ≤ k} (e.g., C
contains all depth-k decision trees). Then C is learnable from random exam-
ples with error 0 in time nk · poly(n, 2k).

3.5. Highlight: the Goldreich–Levin Algorithm

We close this chapter by brieﬂy describing a topic which is in some sense the
“opposite” of learning theory: cryptography. At the highest level, cryptography
is concerned with constructing functions which are computationally easy to
compute but computationally difﬁcult to invert. Intuitively, think about the
task of encrypting secret messages: You would like a scheme where it’s easy
to take any message x and produce an encrypted version e(x), but where it’s
hard for an adversary to compute x given e(x). Indeed, even with examples
e(x(1)), . . . , e(x(m)) of several encryptions, it should be hard for an adversary
to learn anything about the encrypted messages, or to predict (“forge”) the
encryption of future messages.

A basic task in cryptography is building stronger cryptographic functions
from weaker ones. Often the ﬁrst example in “Cryptography 101” is the
Goldreich–Levin Theorem, which is used to build a “pseudorandom generator”
from a “one-way permutation”. We sketch the meaning of these terms and
the analysis of the construction in Exercise 3.45; for now, sufﬁce it to say that
the key to the analysis of Goldreich and Levin’s construction is a learning
algorithm. Speciﬁcally, the Goldreich–Levin learning algorithm solves the
following problem: Given query access to a target function f : F n
2 → F 2, ﬁnd

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.5. Highlight: the Goldreich–Levin Algorithm 83

all of the linear functions (in the sense of Chapter 1.6) with which f is at
least slightly correlated. Equivalently, ﬁnd all of the noticeably large Fourier
coefﬁcients of f .

Goldreich–Levin Theorem. Given query access to a target f : {−1, 1}n →
{−1, 1} as well as input 0 < τ ≤ 1, there is a poly(n, 1/τ)-time algorithm that
with high probability outputs a list L = {U1, . . . ,Uℓ} of subsets of [n] such that:

• | ̂f (U)| ≥ τ =⇒ U ∈ L;

• U ∈ L =⇒ | ̂f (U)| ≥ τ/2.

(By Parseval’s Theorem, the second guarantee implies that |L| ≤ 4/τ2.)

Although the Goldreich–Levin Theorem was originally developed for cryp-
tography, it was soon put to use for learning theory. Recall that the “meta-
algorithm” of Theorem 3.29 reduces learning an unknown target f : {−1, 1}n →
{−1, 1} to identifying a collection F of sets on which f ’s Fourier spectrum is
ϵ/2-concentrated. Using the Goldreich–Levin Algorithm, a learner with query
access to f can “collect up” its largest Fourier coefﬁcients until only ϵ/2 Fourier
weight remains unfound. This strategy straightforwardly yields the following
result (see Exercise 3.39):

Theorem 3.37. Let C be a concept class such that every f : {−1, 1}n → {−1, 1}
in C has its Fourier spectrum ϵ/4-concentrated on a collection of at most M
sets. Then C can be learned using queries with error ϵ in time poly(M, n, 1/ϵ).

The algorithm of Theorem 3.37 is often called the Kushilevitz–Mansour Al-
gorithm. Much like the Low-Degree Algorithm, it reduces the computational
problem of learning C (using queries) to the analytic problem of proving that
the functions in C have concentrated Fourier spectra. The advantage of the
Kushilevitz–Mansour Algorithm is that it works so long as the Fourier spec-
trum of f is concentrated on some small collection of sets; the Low-Degree
Algorithm requires that the concentration speciﬁcally be on the low-degree
characters. The disadvantage of the Kushilevitz–Mansour Algorithm is that
it requires query access to f , rather than just random examples. An example
concept class for which the Kushilevitz–Mansour Algorithm works well is the
set of all f for which ˆ∥ f ˆ∥1 is not too large:

Theorem 3.38. Let C = { f : {−1, 1}n → {−1, 1} | ˆ∥ f ˆ∥1 ≤ s} (e.g., C contains
any f computable by a decision tree of size at most s). Then C is learnable
from queries with error ϵ in time poly(n, s, 1/ϵ).

This is proved in Exercise 3.38.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

84 3. Spectral structure and learning

Let’s now return to the Goldreich–Levin Algorithm itself, which seeks
the Fourier coefﬁcients ̂f (U) with magnitude at least τ. Given any candi-
date U ⊆ [n], Proposition 3.30 lets us easily distinguish whether the associ-
ated coefﬁcient is large, | ̂f (U)| ≥ τ, or small, | ̂f (U)| ≤ τ/2. The trouble is that
there are 2n potential candidates. The Goldreich–Levin Algorithm overcomes
this difﬁculty using a divide-and-conquer strategy that measures the Fourier
weight of f on various collections of sets. Let’s make a deﬁnition:

Deﬁnition 3.39. Let f : {−1, 1}n → R and S ⊆ J ⊆ [n]. We write

WS|J[ f ] = ∑

T⊆J
 ̂f (S ∪ T)2

for the Fourier weight of f on sets whose restriction to J is S.

The crucial tool for the Goldreich–Levin Algorithm is Corollary 3.22,
which says that
 WS|J[ f ] = E
z∼{−1,1}J[ ̂f J|z(S)
2]. (3.5)

This identity lets a learning algorithm with query access to f efﬁciently esti-
mate any WS|J[ f ] of its choosing. Intuitively, query access to f allows query
access to f J|z for any z ∈ {−1, 1}J; with this one can estimate any ̂f J|z(S) and
hence (3.5). More precisely:

Proposition 3.40. For any S ⊆ J ⊆ [n] an algorithm with query access to
f : {−1, 1}n → {−1, 1} can compute an estimate of WS|J[ f ] that is accurate to
within ±ϵ (except with probability at most δ) in time poly(n, 1/ϵ) · log(1/δ).

Proof. From (3.5),

WS|J[ f ] = E
z∼{−1,1}J[ ̂f J|z(S)
2] = E
z∼{−1,1}J
 [
 E
y∼{−1,1}J[ f (y, z)χS(y)]2]

= E
z∼{−1,1}J E
y,y′∼{−1,1}J[ f (y, z)χS(y) · f (y′, z)χS(y′)],

where y, y′ are independent. As in Proposition 3.30, f (y, z)χS(y)· f (y′, z)χS(y′)
is a ±1-valued random variable that the algorithm can sample from using
queries to f . A Chernoff bound implies that O(log(1/δ)/ϵ2) samples are sufﬁ-
cient to estimate its mean with accuracy ϵ and conﬁdence 1 − δ. □

We’re now ready to prove the Goldreich–Levin Theorem.

Proof of the Goldreich–Levin Theorem. We begin with an overview of
how the algorithm works. Initially, all 2n sets U are (implicitly) put in a
single “bucket”. The algorithm then repeats the following loop:

• Select any bucket B containing 2m sets, m ≥ 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.6. Exercises and notes 85

• Split it into two buckets B1, B2 of 2m−1 sets each.

• “Weigh” each Bi, i = 1, 2; i.e., estimate ∑
U∈Bi ̂f (U)
2.

• Discard B1 or B2 if its weight estimate is at most τ2/2.

The algorithm stops once all buckets contain just 1 set; it then outputs the
list of these sets.

We now ﬁll in the details. First we argue the correctness of the algorithm,
assuming all weight estimates are accurate (this assumption is removed later).
On one hand, any set U with | ̂f (U)| ≥ τ will never be discarded, since it
always contributes weight at least τ2 ≥ τ2/2 to the bucket it’s in. On the other
hand, no set U with | ̂f (U)| ≤ τ/2 can end up in a singleton bucket because
such a bucket, when created, would have weight only τ2/4 ≤ τ2/2 and thus
be discarded. Notice that this correctness proof does not rely on the weight
estimates being exact; it sufﬁces for them to be accurate to within ±τ2/4.

The next detail concerns running time. Note that any “active” (undis-
carded) bucket has weight at least τ2/4, even assuming the weight estimates
are only accurate to within ±τ2/4. Therefore Parseval tells us there can only
ever be at most 4/τ2 active buckets. Since a bucket can be split only n times, it
follows that the algorithm repeats its main loop at most 4n/τ2 times. Thus as
long as the buckets can be maintained and accurately weighed in poly(n, 1/τ)
time, the overall running time will be poly(n, 1/τ) as claimed.

Finally, we describe the bucketing system. The buckets are indexed (and
thus maintained implicitly) by an integer 0 ≤ k ≤ n and a subset S ⊆ [k]. The
bucket Bk,S is deﬁned by

Bk,S = {S ∪ T : T ⊆ {k + 1, k + 2, . . . , n}
}
.

Note that |Bk,S| = 2n−k. The initial bucket is B0,;. The algorithm always
splits a bucket Bk,S into the two buckets Bk+1,S and Bk+1,S∪{k+1}. The
ﬁnal singleton buckets are of the form Bn,S = {S}. Finally, the weight of
bucket Bk,S is precisely WS|{k+1,...,n}[ f ]. Thus it can be estimated to accuracy
±τ2/4 with conﬁdence 1− δ in time poly(n, 1/τ)·log(1/δ) using Proposition 3.40.
Since the main loop is executed at most 4n/τ2 times, the algorithm overall
needs to make at most 8n/τ2 weighings; by setting δ = τ2/(80n) we ensure that
all weighings are accurate with high probability (at least 9/10). The overall
running time is therefore indeed poly(n, 1/τ). □

3.6. Exercises and notes

3.1 Let M : F n
2 → F n
2 be an invertible linear transformation. Given f : F n
2 → R ,
let f ◦ M : F n
2 → R be deﬁned by f ◦ M(x) = f (Mx). Show that …f ◦ M(γ) =

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

86 3. Spectral structure and learning

̂f (M−⊤γ). What if M is an invertible afﬁne transformation? What if M is
not invertible?

3.2 Show that 2
1−e−2 is smallest constant (not depending on δ or n) that can
be taken in Proposition 3.3.

3.3 Generalize Proposition 3.3 by showing that any f : {−1, 1}n → R is ϵ-
concentrated on degree up to 1/δ for ϵ = (E[ f 2] − Stab1−δ[ f ])/(1 − 1/e).

3.4 Prove Lemma 3.5 by induction on n. (Hint: If one of the subfunctions
f (x1, . . . , xn, ±1) is identically 0, show that the other has degree at most k−
1.)

3.5 Verify for all p ∈ [1, ∞] that ˆ∥· ˆ∥p is a norm on the vector space of functions
f : F n
2 → R .

3.6 Show that ˆ∥ f g ˆ∥1 ≤ ˆ∥ f ˆ∥1 ˆ∥g ˆ∥1 for all f , g : F n
2 → R .

3.7 Let f : {−1, 1}n → R and let J ⊆ [n], z ∈ {−1, 1}J.
(a) Show that restriction reduces spectral 1-norm: ˆ∥ f J|z ˆ∥1 ≤ ˆ∥ f ˆ∥1.
(b) Show that it also reduces Fourier sparsity: sparsity( ̂f J|z) ≤ sparsity( ̂f ).

3.8 Let f : {−1, 1}n → R and let 0 < p ≤ q ≤ ∞. Show that ˆ∥ f ˆ∥p ≥ ˆ∥ f ˆ∥q. (Cf. Ex-
ercise 1.13.)

3.9 Let f : {−1, 1}n → R . Show that ˆ∥ f ˆ∥∞ ≤ ∥ f ∥1 and ∥ f ∥∞ ≤ ˆ∥ f ˆ∥1. (These are
easy special cases of the Hausdorff–Young Inequality.)

3.10 Suppose f : {−1, 1}n → {−1, 1} is monotone. Show that | ̂f (S)| ≤ ̂f (i) when-
ever i ∈ S ⊆ [n]. Deduce that ˆ∥ f ˆ∥∞ = maxS{| ̂f (S)|} is achieved by an S of
cardinality 0 or 1. (Hint: Apply the previous exercise to f ’s derivatives.)

3.11 Prove Proposition 3.12.

3.12 Verify Parseval’s Theorem for the Fourier expansion of subspaces given
in Proposition 3.11.

3.13 Let f : F n
2 → {0, 1} be the indicator of A ⊆ F n
2 . We know that ˆ∥ f ˆ∥1 = 1 if A
is an afﬁne subspace. So assume that A is not an afﬁne subspace.
(a) Show that there exists an afﬁne subspace B of dimension 2 on which f
takes the value 1 exactly 3 times.
(b) Let b be the point in B where f is 0 and let ψ = ϕB − (1/2)ϕb. Show
that ˆ∥ψˆ∥∞ = 1/2.
(c) Show that 〈ψ, f 〉 = 3/4 and deduce ˆ∥ f ˆ∥1 ≥ 3/2.

3.14 Suppose f : {−1, 1}n → R satisﬁes E[ f 2] ≤ 1. Show that ˆ∥ f ˆ∥1 ≤ 2n/2, and
show that for any even n the upper bound can be achieved by a function
f : {−1, 1}n → {−1, 1}.

3.15 Given f : F n
2 → R , deﬁne its (fractional) sparsity to be

sparsity( f ) = |supp( f )|/2n = Pr
x∈F n
2 [ f (x) ̸= 0].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.6. Exercises and notes 87

In this exercise you will prove the uncertainty principle: If f is nonzero,
then sparsity( f ) · sparsity( ̂f ) ≥ 1.
(a) Show that we may assume ∥ f ∥1 = 1.
(b) Suppose F = {γ : ̂f (γ) ̸= 0}. Show that ˆ∥ f ˆ∥
2
2 ≤ |F |.
(c) Suppose G = {x : f (x) ̸= 0}. Show that ∥ f ∥2
2 ≥ 2n/|G |, and deduce the
uncertainty principle.
(d) Identify all cases of equality.

3.16 Let f : {−1, 1}n → R and let ϵ > 0. Show that f is ϵ-concentrated on a
collection F ⊆ 2[n] with |F | ≤ ˆ∥ f ˆ∥
2
1/ϵ.

3.17 Suppose the Fourier spectrum of f : {−1, 1}n → R is ϵ1-concentrated on F
and that g : {−1, 1}n → R satisﬁes ∥ f − g∥
2
2 ≤ ϵ2. Show that the Fourier
spectrum of g is 2(ϵ1 + ϵ2)-concentrated on F .

3.18 Show that every function f : F n
2 → R is computed by a decision tree with
depth at most n and size at most 2n.

3.19 Let f : F n
2 → R be computable by a decision tree of size s and depth k
Show that − f and the Boolean dual f † are also computable by decision
trees of size s and depth k.

3.20 For each function in Exercise 1.1 with 4 or fewer inputs, give a decision
tree computing it. Try primarily to use the least possible depth, and
secondarily to use the least possible size.

3.21 Prove Proposition 3.16.

3.22 Let f : F n
2 → {−1, 1} be computed by a decision tree T of size s and let ϵ ∈
(0, 1]. Suppose each path in T is truncated (if necessary) so that its length
does not exceed log(s/ϵ); new leaves with labels −1 and 1 may be created
in an arbitrary way as necessary. Show that the resulting decisions tree
T′ computes a function that is ϵ-close to f . Deduce Proposition 3.17.

3.23 A decision list is a decision tree in which every internal node has an
outgoing edge to at least one leaf. Show that any function computable by
a decision list is a linear threshold function.

3.24 A read-once decision tree is one in which every internal node queries a
distinct variable. Bearing this in mind, show that the bound k2k−1 in
Theorem 3.4 cannot be reduced below 2k − 1.

3.25 Suppose that f is computed by a read-once decision tree in which every
root-to-leaf path has length k and every internal node at the deepest level
has one child (leaf) labeled −1 and one child labeled 1. Compute the
inﬂuence of each coordinate on f , and compute I[ f ].

3.26 The following are generalizations of decision trees:
Subcube partition: This is deﬁned by a collection C1, . . . , Cs of sub-
cubes that form a partition of F n
2 , along with values b1, . . . , bs ∈ R . It

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

88 3. Spectral structure and learning

computes the function f : F n
2 → R which has value bi on all inputs in Ci.
The subcube partition’s size is s and its “codimension” k (analogous to
depth) is the maximum codimension of the cubes Ci.
Parity decision tree: This is similar to a decision tree except that
the internal nodes are labeled by vectors γ ∈ F n
2 . At such a node the
computation path on input x follows the edge labeled γ · x. We insist that
for each root-to-leaf path, the vectors appearing in its internal nodes are
linearly independent. Size s and depth k are deﬁned as with normal
decision trees.
Afﬁne subspace partition: This is similar to a subcube partition except
the subcubes Ci may be arbitrary afﬁne subspaces.
(a) Show that subcube partition size/codimension and parity decision
tree size/depth generalize normal decision tree size/depth, and are
generalized by afﬁne subspace partition size/codimension.
(b) Show that Proposition 3.16 holds also for the generalizations, except
that the statement about degree need not hold for parity decision
trees and afﬁne subspace partitions.
(c) Show that the class of functions with afﬁne subspace partition size at
most s is learnable from queries with error ϵ in time poly(n, s, 1/ϵ).

3.27 Deﬁne Equ3 : {−1, 1}
3 → {−1, 1} by Equ3(x) = −1 if and only if x1 = x2 = x3.
(a) Show that deg(Equ3) = 2.
(b) Show that DT(Equ3) = 3.
(c) Show that Equ3 is computable by a parity decision tree of codimen-
sion 2.
(d) For d ∈ N , deﬁne f {−1, 1}
3d → {−1, 1} by f = Equ⊗d
3 (using the notation
from Deﬁnition 2.6). Show that deg( f ) = 2d but DT( f ) = 3d.

3.28 Let f : {−1, 1}n → R and J ⊆ [n]. Deﬁne f ⊆J : {−1, 1}n → R by f (x) =
Ey∼{−1,1}J [ f (xJ, y)], where xJ ∈ {−1, 1}J is the projection of x to coordi-
nates J. Verify the Fourier expansion

f ⊆J = ∑

S⊆J ̂f (S) χS.

3.29 Let ϕ : F n
2 → R ≥0 be a probability density function corresponding to prob-
ability distribution φ on F n
2 . Let J ⊆ [n].
(a) Consider the marginal probability distribution of φ on coordinates J.
What is its probability density function (a function F J
2 → R ≥0) in
terms of ϕ?
(b) Consider the probability distribution of φ conditioned on a substring
z ∈ F J
2 . Assuming it’s well deﬁned, what is its probability density
function in terms of ϕ?

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.6. Exercises and notes 89

3.30 Suppose f : {−1, 1}n → R is computable by a decision tree that has a leaf
at depth k labeled b. Show that ˆ∥ f ˆ∥∞ ≥ |b|/2k. (Hint: You may ﬁnd
Exercise 3.28 helpful.)

3.31 Prove Fact 3.25 by using Theorem 1.27 and Exercise 1.1(d).

3.32 (a) Suppose f : F n
2 → R has sparsity( ̂f ) < 2n. Show that for any γ ∈
supp( ̂f ) there exists nonzero β ∈ ̂F n
2 such that fβ⊥ has ̂f (γ) as a Fourier
coefﬁcient.
(b) Prove by induction on n that if f : F n
2 → {−1, 1} has sparsity( ̂f ) = s > 1
then ̂f is 21−⌊log s⌋-granular. (Hint: Distinguish the cases s = 2n and
s < 2n. In the latter case use part (a).)
(c) Prove that there are no functions f : {−1, 1}n → {−1, 1} with sparsity( ̂f ) ∈
{2, 3, 5, 6, 7, 9}.

3.33 Show that one can learn any target f : {−1, 1}n → {−1, 1} with error 0 from
random examples only in time ̃O(2n).

3.34 Improve Proposition 3.31 as follows. Suppose f : {−1, 1}n → {−1, 1} and
g : {−1, 1}n → R satisfy ∥ f − g∥1 ≤ ϵ. Pick θ ∈ [−1, 1] uniformly at ran-
dom and deﬁne h : {−1, 1}n → {−1, 1} by h(x) = sgn(g(x) − θ). Show that
E[dist( f , h)] ≤ ϵ/2.

3.35 (a) For n even, ﬁnd a function f : {−1, 1}n → {−1, 1} such that f is not 1/2-
concentrated on any F ⊆ 2[n] with |F | < 2n−1. (Hint: Exercise 1.1.)
(b) Let f : {−1, 1}n → {−1, 1} be a random function as in Exercise 1.7. Show
that with probability at least 1/2, f is not 1/4-concentrated on degree
up to ⌊n/2⌋.

3.36 Prove Theorem 3.36. (Hint: In light of Exercise 1.11 you may round off
certain estimates with conﬁdence.)

3.37 Show that each of the following classes C (ordered by inclusion) can be
learned exactly (i.e., with error 0) using queries in time poly(n, 2k):
(a) C = { f : {−1, 1}n → {−1, 1} | f is a k-junta}. (Hint: Estimate inﬂuences.)
(b) C = { f : {−1, 1}n → {−1, 1} | DT( f ) ≤ k}.
(c) C = { f : {−1, 1}n → {−1, 1} | sparsity( ̂f ) ≤ 2O(k)}. (Hint: Exercise 3.32.)

3.38 Prove Theorem 3.38. (Hint: Exercise 3.16.)

3.39 Deduce Theorem 3.37 from the Goldreich–Levin Algorithm.

3.40 Suppose A learns C from random examples with error ϵ/2 in time T –
with probability at least 9/10.
(a) After producing hypothesis h on target f : {−1, 1}n → {−1, 1}, show that
A can “check” whether h is a good hypothesis in time poly(n, T, 1/ϵ) ·
log(1/δ). Speciﬁcally, except with probability at most δ, A should out-
put ‘YES’ if dist( f , h) ≤ ϵ/2 and ‘NO’ if dist( f , h) > ϵ. (Hint: Time poly(T)
may be required for A to evaluate h(x).)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

90 3. Spectral structure and learning

(b) Show that for any δ ∈ (0, 1/2], there is a learning algorithm that learns
C with error ϵ in time poly(n, T, ϵ) · log(1/δ) – with probability at least
1 − δ.

3.41 (a) Our description of the Low-Degree Algorithm with degree k and er-
ror ϵ involved using a new batch of random examples to estimate each
low-degree Fourier coefﬁcient. Show that one can instead simply draw
a single batch E of poly(nk, 1/ϵ) examples and use E to estimate each
of the low-degree coefﬁcients.
(b) Show that when using the above form of the Low-Degree Algorithm,
the ﬁnal hypothesis h : {−1, 1}n → {−1, 1} is of the form

h(y) = sgn
 ( ∑

(x, f (x))∈E w(∆(y, x)) · f (x)
)
 ,

for some function w : {0, 1, . . . , n} → R . In other words, the hypothe-
sis on a given y is equal to a weighted vote over all examples seen,
where an example’s weight depends only on its Hamming distance
to y. Simplify your expression for w as much as you can.

3.42 Extend the Goldreich–Levin Algorithm so that it works also for functions
f : {−1, 1}n → [−1, 1]. (The learning model for targets f : {−1, 1}n → [−1, 1]
assumes that f (x) is always a rational number expressible by poly(n)
bits.)

3.43 (a) Assume γ, γ
′ ∈ ̂F n
2 are distinct. Show that Prx[γ · x = γ
′ · x] = 1/2.
(b) Fix γ ∈ ̂F n
2 and suppose x(1), . . . , x(m) ∼ F n
2 are drawn uniformly and
independently. Show that if m = Cn for C a sufﬁciently large constant
then with high probability, the only γ
′ ∈ ̂F n
2 satisfying γ
′ · x(i) = γ · x(i)

for all i ∈ [m] is γ
′ = γ.
(c) Essentially improve on Exercise 1.27 by showing that the concept
class of all linear functions F n
2 → F 2 can be learned from random
examples only, with error 0, in time poly(n). (Remark: If ω ∈ R is such
that n × n matrix multiplication can be done in O(nω) time, then the
learning algorithm also requires only O(nω) time.)

3.44 Let τ ≥ 1/2 + ϵ for some constant ϵ > 0. Give an algorithm simpler than
Goldreich and Levin’s that solves the following problem with high proba-
bility: Given query access to f : {−1, 1}n → {−1, 1}, in time poly(n, 1/ϵ) ﬁnd
the unique U ⊆ [n] such that | ̂f (U)| ≥ τ, assuming it exists. (Hint: Use
Proposition 1.31 and Exercise 1.27.)

3.45 Informally: a “one-way permutation” is a bijective function f : F n
2 → F n
2
that is easy to compute on all inputs but hard to invert on more than a
negligible fraction of inputs; a “pseudorandom generator” is a function g :
F k
2 → F m
2 for m > k whose output on a random input “looks unpredictable”
to any efﬁcient algorithm. Goldreich and Levin proposed the following

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

3.6. Exercises and notes 91

construction of the latter from the former: for k = 2n, m = 2n + 1, deﬁne

g(r, s) = (r, f (s), r · s),

where r, s ∈ F n
2 . When g’s input (r, s) is uniformly random, then so is the
ﬁrst 2n bits of its output (using the fact that f is a bijection). The key to
the analysis is showing that the ﬁnal bit, r · s, is highly unpredictable to
efﬁcient algorithms even given the ﬁrst 2n bits (r, f (s)). This is proved by
contradiction.
(a) Suppose that an adversary has a deterministic, efﬁcient algorithm A
good at predicting the bit r · s:

Pr
r,s∼F n
2 [A(r, f (s)) = r · s] ≥ 1
2 + γ.

Show there exists B ⊆ F n
2 with |B|/2n ≥ 1
2 γ such that

Pr
r∼F n
2 [A(r, f (s)) = r · s] ≥ 1
2 + 1
2 γ

for all s ∈ B.
(b) Switching to ±1 notation in the output, deduce …A| f (s)(s) ≥ γ for all
s ∈ B.
(c) Show that the adversary can efﬁciently compute s given f (s) (with
high probability) for any s ∈ B. If γ is nonnegligible, this contradicts
the assumption that f is “one-way”. (Hint: Use the Goldreich–Levin
Algorithm.)
(d) Deduce the same conclusion even if A is a randomized algorithm.

Notes. The fact that the Fourier characters χγ : F n
2 → {−1, 1} form a group
isomorphic to F n
2 is not a coincidence; the analogous result holds for any ﬁnite
abelian group and is a special case of the theory of Pontryagin duality in
harmonic analysis. We will see further examples of this in Chapter 8.

Regarding spectral structure, Karpovsky [Kar76] proposed sparsity( ̂f )
as a measure of complexity for the function f . Brandman’s thesis [Bra87]
(see also [BOH90]) is an early work connecting decision tree and subcube
partition complexity to Fourier analysis. The notation introduced for restric-
tions in Section 3.3 is not standard; unfortunately there is no standard nota-
tion. The uncertainty principle from Exercise 3.15 dates back to Matolcsi and
Szücs [MS73]. The result of Exercise 3.13 is due to Green and Sanders [GS08],
with inspiration from Saeki [Sae68]. The main result of Green and Sanders
is the sophisticated theorem that any f : F n
2 → {0, 1} with ˆ∥ f ˆ∥1 ≤ s can be

expressed as ∑L
i=1 ±1Hi , where L ≤ 22
poly(s) and each Hi ≤ F n
2 .

Theorem 3.4 is due to Nisan and Szegedy [NS94]. That work also showed
a nontrivial kind of converse to the ﬁrst statement in Proposition 3.16: Any f :
{−1, 1}n → {−1, 1} is computable by a decision tree of depth at most poly(deg( f )).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

92 3. Spectral structure and learning

The best upper bound currently known is deg( f )3 due to Midrij ¯anis [Mid04].
Nisan and Szegedy also gave the example in Exercise 3.27 showing the depen-
dence cannot be linear.

The ﬁeld of computational learning theory was introduced by Valiant
in 1984 [Val84]; for a good survey with focus on learning under the uni-
form distribution, see the thesis by Jackson [Jac95]. Linial, Mansour, and
Nisan [LMN93] pioneered the Fourier approach to learning, developing the
Low-Degree Algorithm. We present their strong results on constant-depth
circuits in Chapter 4. The noise sensitivity approach to the Low-Degree Al-
gorithm is from Klivans, O’Donnell, and Servedio [KOS04]. Corollary 3.33
is due to Bshouty and Tamon [BT96] who also gave certain matching lower
bounds. Goldreich and Levin’s work dates from 1989 [GL89]. Besides its
applications to cryptography and learning, it is important in coding theory
and complexity as a local list-decoding algorithm for the Hadamard code. The
Kushilevitz–Mansour algorithm is from their 1993 paper [KM93]; they also
are responsible for the results of Exercise 3.37(b) and 3.38. The results of
Exercise 3.32 and 3.37(c) are from Gopalan et al. [GOS
+11].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 4

DNF formulas and
small-depth circuits

In this chapter we investigate Boolean functions representable by small DNF
formulas and constant-depth circuits; these are signiﬁcant generalizations
of decision trees. Besides being natural from a computational point of view,
these representation classes are close to the limit of what complexity theorists
can “understand” (e.g., prove explicit lower bounds for). One reason for this is
that functions in these classes have strong Fourier concentration properties.

4.1. DNF formulas

One of the commonest ways of representing a Boolean function f : {0, 1}n →
{0, 1} is by a DNF formula:

Deﬁnition 4.1. A DNF (disjunctive normal form) formula over Boolean vari-
ables x1, . . . , xn is deﬁned to be a logical OR of terms, each of which is a logi-
cal AND of literals. A literal is either a variable xi or its logical negation xi.
We insist that no term contains both a variable and its negation. The number
of literals in a term is called its width. We often identify a DNF formula with
the Boolean function f : {0, 1}n → {0, 1} it computes.

Example 4.2. Recall the function Sort3, deﬁned by Sort3(x1, x2, x3) = 1 if and
only if x1 ≤ x2 ≤ x3 or x1 ≥ x2 ≥ x3. We can represent it by a DNF formula as
follows:
 Sort3(x1, x2, x3) = (x1 ∧ x2) ∨ (x2 ∧ x3) ∨ (x1 ∧ x3) ∨ (x1 ∧ x3).
 93

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

94 4. DNF formulas and small-depth circuits

The DNF representation says that the bits are sorted if either the ﬁrst two
bits are 1, or the last two bits are 0, or the ﬁrst bit is 0 and the last bit is 1, or
the ﬁrst bit is 1 and the last bit is 0.

The complexity of a DNF formula is measured by its size and width:

Deﬁnition 4.3. The size of a DNF formula is its number of terms. The width
is the maximum width of its terms. Given f : {−1, 1}n → {−1, 1} we write
DNFsize( f ) (respectively, DNFwidth( f )) for the least size (respectively, width)
of a DNF formula computing f .

The DNF formula for Sort3 from Example 4.2 has size 3 and width 2.
Every function f : {0, 1}n → {0, 1} can be computed by a DNF of size at most 2n

and width at most n (Exercise 4.1).

There is also a “dual” notion to DNF formulas:

Deﬁnition 4.4. A CNF (conjunctive normal form) formulas is a logical AND
of clauses, each of which is a logical OR of literals. Size and width are deﬁned
as for DNFs.

Some functions can be represented much more compactly by CNFs than
DNFs (see Exercise 4.14). On the other hand, if we take a CNF computing f
and switch its ANDs and ORs, the result is a DNF computing the dual func-
tion f † (see Exercises 1.8 and 4.2). Since f and f † have essentially the same
Fourier expansion, there isn’t much difference between CNFs and DNFs when
it comes to Fourier analysis. We will therefore focus mainly on DNFs.

DNFs and CNFs are more powerful than decision trees for representing
Boolean-valued functions, as the following proposition shows:

Proposition 4.5. Let f : {0, 1}n → {0, 1} be computable by a decision tree T of
size s and depth k. Then f is computable by a DNF (and also a CNF) of size
at most s and width at most k.

Proof. Take each path in T from the root to a leaf labeled 1 and form the
logical AND of the literals describing the path. These are the terms of the
required DNF. (For the CNF clauses, take paths to label 0 and negate all
literals describing the path.) □

Example 4.6. If we perform this conversion on the decision tree computing
Sort3 in Figure 3.1 we get the DNF

(x1 ∧ x3 ∧ x2) ∨ (x1 ∧ x3) ∨ (x1 ∧ x2 ∧ x3) ∨ (x2 ∧ x3).

This has size 4 (indeed at most the decision tree size 6) and width 3 (indeed
at most the decision tree depth 3). It is not as simple as the equivalent DNF
from Example 4.2, though; DNF representation is not unique.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.1. DNF formulas 95

The class of functions computable by small DNFs is intensively studied
in learning theory. This is one reason why the problem of analyzing spectral
concentration for DNFs is important. Let’s begin with the simplest method
for this: understanding low-degree concentration via total inﬂuence. We will
switch to ±1 notation.

Proposition 4.7. Suppose that f : {−1, 1}n → {−1, 1} has DNFwidth( f ) ≤ w.
Then I[ f ] ≤ 2w.

Proof. We use Exercise 2.10, which states that

I[ f ] = 2 E
x∼{−1,1}n[# (−1)-pivotal coordinates for f on x],

where coordinate i is “(−1)-pivotal” on input x if f (x) = −1 (logical True) but
f (x⊕i) = 1 (logical False). It thus sufﬁces to show that on every input x there
are at most w coordinates which are (−1)-pivotal. To have any (−1)-pivotal
coordinates at all on x we must have f (x) = −1 (True); this means that at least
one term T in f ’s width-w DNF representation must be made True by x. But
now if i is a (−1)-pivotal coordinate then either xi or xi must appear in T;
otherwise, T would still be made true by x⊕i. Thus the number of (−1)-pivotal
coordinates on x is at most the number of literals in T, which is at most w. □

Since I[ f †] = I[ f ] the proposition is also true for CNFs of width at most w.
The proposition is very close to being tight: The parity function χ[w] : {−1, 1}n →
{−1, 1} has I[χ[w]] = w and DNFwidth(χ[w]) ≤ w (the latter being true for all w-
juntas). In fact, the proposition can be improved to give the tight upper
bound w (Exercise 4.17).

Using Proposition 3.2 we deduce:

Corollary 4.8. Let f : {−1, 1}n → {−1, 1} have DNFwidth( f ) ≤ w. Then for ϵ > 0,
the Fourier spectrum of f is ϵ-concentrated on degree up to 2w/ϵ.

The dependence here on w is of the correct order (by the example of the
parity χ[w] again), but the dependence on ϵ can be signiﬁcantly improved as
we will see in Section 4.4.

There’s usually more interest in DNF size than in DNF width; for example,
learning theorists are often interested in the class of n-variable DNFs of size
poly(n). The following fact (similar to Exercise 3.22) helps relate the two,
suggesting O(log n) as an analogous width bound:

Proposition 4.9. Let f : {−1, 1}n → {−1, 1} be computable by a DNF (or CNF)
of size s and let ϵ ∈ (0, 1]. Then f is ϵ-close to a function g computable by a
DNF of width log(s/ϵ).

Proof. Take the DNF computing f and delete all terms with more than log(s/ϵ)
literals; let g be the function computed by the resulting DNF. For any deleted

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

96 4. DNF formulas and small-depth circuits

term T, the probability a random input x ∼ {−1, 1}n makes T true is at most
2− log(s/ϵ) = ϵ/s. Taking a union bound over the (at most s) such terms shows
that Pr[g(x) ̸= f (x)] ≤ ϵ. (A similar proof works for CNFs.) □

By combining Proposition 4.9 and Corollary 4.8 we can deduce (using Exer-
cise 3.17) that DNFs of size s have Fourier spectra ϵ-concentrated up to degree
O(log(s/ϵ)/ϵ). Again, the dependence on ϵ will be improved in Section 4.4. We
will also later show in Section 4.3 that size-s DNFs have total inﬂuence at
most O(log s), something we cannot deduce immediately from Proposition 4.7.

In light of the Kushilevitz–Mansour learning algorithm it would also be
nice to show that poly(n)-size DNFs have their Fourier spectra concentrated
on small collections (not necessarily low-degree). In Section 4.4 we will show
they are ϵ-concentrated on collections of size nO(log log n) for any constant ϵ > 0.
It has been conjectured that this can be improved to poly(n):

Mansour’s Conjecture. Let f : {−1, 1}n → {−1, 1} be computable by a DNF
of size s > 1 and let ϵ ∈ (0, 1/2]. Strong conjecture: f ’s Fourier spectrum is ϵ-
concentrated on a collection F with |F | ≤ sO(log(1/ϵ)). Weaker conjecture: if s ≤
poly(n) and ϵ > 0 is any ﬁxed constant, then we have the bound |F | ≤ poly(n).

4.2. Tribes

In this section we study the tribes DNF formulas, which serve as an important
examples and counterexamples in analysis of Boolean functions. Perhaps the
most notable feature of the tribes function is that (for a suitable choice of
parameters) it is essentially unbiased and yet all of its inﬂuences are quite
tiny.

Recall from Chapter 2.1 that the function Tribesw,s : {−1, 1}sw → {−1, 1} is
deﬁned by its width-w, size-s DNF representation:

Tribesw,s(x1, . . . , xw, . . . , x(s−1)w+1, . . . , xsw)

= (x1 ∧ · · · ∧ xw) ∨ · · · ∨ (x(s−1)w+1 ∧ · · · ∧ xsw).

(We are using the notation where −1 represents logical True and 1 represents
logical False.) As is computed in Exercise 2.13 we have:

Fact 4.10. Prx[Tribesw,s(x) = −1] = 1 − (1 − 2
−w)s.

The most interesting setting of parameters makes this probability as close
to 1/2 as possible (a slightly different choice than the one in Exercise 2.13):

Deﬁnition 4.11. For w ∈ N +, let s = sw be the largest integer such that
1 − (1 − 2−w)s ≤ 1/2. Then for n = nw = sw we deﬁne Tribesn : {−1, 1}n → {−1, 1}
to be Tribesw,s. Note this is only deﬁned only for certain n: 1, 4, 15, 40, . . .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.2. Tribes 97

Here s ≈ ln(2)2w, hence n ≈ ln(2)w2w and therefore w ≈ log n − log ln n and
s ≈ n/ log n. A slightly more careful accounting (Exercise 4.5) yields:

Proposition 4.12. For the Tribesn function as in Deﬁnition 4.11:

• s = ln(2)2w − Θw(1);

• n = ln(2)w2w − Θ(w), thus nw+1 = (2 + o(1))nw;

• w = log n − log ln n + on(1), and 2w = n
ln n (1 + on(1));

• Pr[Tribesn(x) = −1] = 1/2 − O ( log n
n
 ).

Thus with this setting of parameters Tribesn is essentially unbiased. Re-
garding its inﬂuences:

Proposition 4.13. Infi[Tribesn] = ln n
n (1 ± o(1)) for each i ∈ [n] and hence
I[Tribesn] = (ln n)(1 ± o(1)).

Proof. Thinking of Tribesn = Tribesw,s as a voting rule, voter i is pivotal if
and only if: (a) all other voters in i’s “tribe” vote −1 (True); (b) all other tribes
produce the outcome 1 (False). The probability of this is indeed

2−(w−1) · (1 − 2−w)s−1 = 2
2w−1 · Pr[Tribesn = 1] = ln n
n (1 ± o(1)),

where we used Fact 4.10 and then Proposition 4.12. □

Thus if we are interested in (essentially) unbiased voting rules in which
every voter has small inﬂuence, Tribesn is a much stronger example than
Majn where each voter has inﬂuence Θ(1/pn). You may wonder if the max-
imum inﬂuence can be even smaller than Θ
( ln n
n ) for unbiased voting rules.
Certainly it can’t be smaller than 1
n , since the Poincaré Inequality says that
I[ f ] ≥ 1 for unbiased f . In fact the famous KKL Theorem shows that the
Tribesn example is tight up to constants:

Kahn–Kalai–Linial (KKL) Theorem. For any f : {−1, 1}n → {−1, 1},

MaxInf[ f ] = max
i∈[n] {Infi[ f ]} ≥ Var[ f ] · Ω( log n
n
 ).

We prove the KKL Theorem in Chapter 9.

We conclude this section by recording a formula for the Fourier coefﬁcients
of Tribesw,s. The proof is Exercise 4.6.

Proposition 4.14. Suppose we index the Fourier coefﬁcients of the function
Tribesw,s{−1, 1}sw → {−1, 1} by sets T = (T1, . . . , Ts) ⊆ [sw], where Ti is the in-
tersection of T with the ith “tribe”. Then

áTribesw,s(T) =
 {
2(1 − 2
−w)s − 1 if T = ;,

2(−1)k+|T|2
−kw(1 − 2−w)s−k if k = #{i : Ti ̸= ;} > 0.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

98 4. DNF formulas and small-depth circuits

4.3. Random restrictions

In this section we describe the method of applying random restrictions. This is
a very “Fourier-friendly” way of simplifying a Boolean function. As motivation,
let’s consider the problem of bounding total inﬂuence for size-s DNFs. One
plan is to use the results from Section 4.1: size-s DNFs are .01-close to width-
O(log s) DNFs, which in turn have total inﬂuence O(log s). This suggests that
size-s DNFs themselves have total inﬂuence O(log s). To prove this though
we’ll need to reverse the steps of the plan; instead of truncating DNFs to a
ﬁxed width and arguing that a random input is unlikely to notice, we’ll ﬁrst
pick a random (partial) input and argue that this is likely to make the width
small.

Let’s formalize the notion of a random partial input, or restriction:

Deﬁnition 4.15. For δ ∈ [0, 1], we say that J is a δ-random subset of N if it
is formed by including each element of N independently with probability δ.
We deﬁne a δ-random restriction on {−1, 1}n to be a pair (J | z), where ﬁrst
J is chosen to be a δ-random subset of [n] and then z ∼ {−1, 1}J is chosen
uniformly at random. We say that coordinate i ∈ [n] is free if i ∈ J and is ﬁxed
if i ∉ J. An equivalent deﬁnition is that each coordinate i is (independently)
free with probability δ and ﬁxed to ±1 with probability (1 − δ)/2 each.

Given f : {−1, 1}n → R and a random restriction (J | z), we can form the re-
stricted function f J|z : {−1, 1}J → R as usual. However, it’s inconvenient that
the domain of this function depends on the random restriction. Thus when
dealing with random restriction we usually invoke the following convention:

Deﬁnition 4.16. Given f : {−1, 1}n → R , I ⊆ [n], and z ∈ {−1, 1}I , we may iden-
tify the restricted function f I|z : {−1, 1}I → R with its extension f I|z : {−1, 1}n →
R in which the input coordinates {−1, 1}I are ignored.

As mentioned, random restrictions interact nicely with Fourier expan-
sions:

Proposition 4.17. Fix f : {−1, 1}n → R and S ⊆ [n]. Then if (J | z) is a δ-
random restriction on {−1, 1}n,

E[ ̂f J|z(S)] = Pr[S ⊆ J] · ̂f (S) = δ|S| ̂f (S),

and
 E[ ̂f J|z(S)2] = ∑

U⊆[n] Pr[U ∩ J = S] · ̂f (U)
2 = ∑

U⊇S δ|S|(1 − δ)|U\S| ̂f (U)
2,

where we are treating f J|z as a function {−1, 1}n → R .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.3. Random restrictions 99

Proof. Suppose ﬁrst that J ⊆ [n] is ﬁxed. When we think of restricted func-
tions f J|z as having domain {−1, 1}n, Corollary 3.22 may be stated as saying
that for any S ⊆ [n],
 E
z∼{−1,1}J[ ̂f J|z(S)] = ̂f (S) · 1S⊆J,

E
z∼{−1,1}J[ ̂f J|z(S)2] = ∑

U⊆[n] ̂f (U)2 · 1U∩J=S.

The proposition now follows by taking the expectation over J. □

Corollary 4.18. Fix f : {−1, 1}n → R and i ∈ [n]. If (J | z) is a δ-random
restriction, then E[Infi[ f J|z]] = δInfi[ f ]. Hence also E[I[ f J|z]] = δI[ f ].

Proof. We have

E[Infi[ f J|z]] = E
 [ ∑

S∋i ̂f J|z(S)2]
 = ∑

S∋i
 ∑

U⊆[n] Pr[U ∩ J = S] ̂f (U)2

= ∑

U⊆[n] Pr[U ∩ J ∋ i] ̂f (U)
2 = ∑

U∋i δ ̂f (U)
2 = δInfi[ f ],

where the second equality used Proposition 4.17. □

(Proving Corollary 4.18 via Proposition 4.17 is a bit more elaborate than
necessary; see Exercise 4.9.)

Corollary 4.18 lets us bound the total inﬂuence of a function f by bounding
the (expected) total inﬂuence of a random restriction of f . This is useful if f
is computable by a DNF formula of small size, since a random restriction is
very likely to make this DNF have small width. This is a consequence of the
following lemma:

Lemma 4.19. Let T be a DNF term over {−1, 1}n and ﬁx w ∈ N +. Let (J | z) be
a (1/2)-random restriction on {−1, 1}n. Then Pr[width(TJ|z) ≥ w] ≤ (3/4)w.

Proof. We may assume the initial width of T is at least w, as otherwise its
restriction under (J | z) cannot have width at least w. Now if any literal
appearing in T is ﬁxed to False by the random restriction, the restricted term
TJ|z will be constantly False and thus have width 0 < w. Each literal is ﬁxed
to False with probability 1/4; hence the probability no literal in T is ﬁxed to
False is at most (3/4)w. □

We can now bound the total inﬂuence of small DNF formulas.

Theorem 4.20. Let f : {−1, 1}n → {−1, 1} be computable by a DNF of size s.
Then I[ f ] ≤ O(log s).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

100 4. DNF formulas and small-depth circuits

Proof. Let (J | z) be a (1/2)-random restriction on {−1, 1}n and write w =
DNFwidth( f J|z). By a union bound and Lemma 4.19 we have that Pr[w ≥ w] ≤
s(3/4)w. Hence

E[w] = ∞∑

w=1 Pr[w ≥ w] ≤ 3 log s + ∑

w>3 log s s(3/4)w

≤ 3 log s + 4s(3/4)
3 log s ≤ 3 log s + 4/s0.2 = O(log s).

From Proposition 4.7 we obtain E[I[ f J|z]] ≤ 2 · O(log s) = O(log s). And so from
Corollary 4.18 we conclude I[ f ] = 2 E[I[ f J|z]] ≤ O(log s). □

4.4. Håstad’s Switching Lemma and the spectrum of DNFs

Let’s further investigate how random restrictions can simplify DNF formulas.
Suppose f is computable by a DNF formula of width w, and we apply to it a
δ-random restriction with δ ≪ 1/w. For each term T in the DNF, one of three
things may happen to it under the random restriction. First and by far most
likely, one of its literals may be ﬁxed to False, allowing us to delete it. If this
doesn’t happen, the second possibility is that all of T’s literals are made True,
in which case the whole DNF reduces to the constantly True function. With
δ ≪ 1/w, this is in turn much more likely than the third possibility, which is
that at least one of T’s literals is left free, but all the ﬁxed literals are made
True. Only in this third case is T not trivialized by the random restriction.

This reasoning might suggest that f is likely to become a constant func-
tion under the random restriction. Indeed, this is true, as the following theo-
rem shows:

Baby Switching Lemma. Let f : {−1, 1}n → {−1, 1} be computable by a DNF
or CNF of width at most w and let (J | z) be a δ-random restriction. Then

Pr[ f J|z is not a constant function] ≤ 5δw.

This is in fact the k = 1 case of the following much more powerful theorem:

Håstad’s Switching Lemma. Let f : {−1, 1}n → {−1, 1} be computable by a
DNF or CNF of width at most w and let (J | z) be a δ-random restriction. Then
for any k ∈ N , Pr[DT( f J|z) ≥ k] ≤ (5δw)k.

What is remarkable about this result is that it has no dependence on the
size of the DNF, or on n. In words, Håstad’s Switching Lemma says that when
δ ≪ 1/w, it’s exponentially unlikely (in k) that applying a δ-random restriction
to a width-w DNF does not convert (“switch”) it to a decision tree of depth
less than k. The result is called a “lemma” for historical reasons; in fact, its
proof requires some work. You are asked to prove the Baby Switching Lemma

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.4. Håstad’s Switching Lemma and the spectrum of DNFs 101

in Exercise 4.19; for Håstad’s Switching Lemma, consult Håstad’s original
proof [Hås87] or the alternate proof of Razborov [Raz93, Bea94].

Since we have strong results about the Fourier spectra of decision trees
(Proposition 3.16), and since we know random restrictions interact nicely with
Fourier coefﬁcients (Proposition 4.17), Håstad’s Switching Lemma allows us
to prove some strong results about Fourier concentration of narrow DNF
formulas. We start with an intermediate result which will be of use:

Lemma 4.21. Let f : {−1, 1}n → {−1, 1} and let (J | z) be a δ-random restriction,
δ > 0. Fix k ∈ N + and write ϵ = Pr[DT( f J|z) ≥ k]. Then the Fourier spectrum of
f is 3ϵ-concentrated on degree up to 3k/δ.

Proof. The key observation is that DT( f J|z) < k implies deg( f J|z) < k (Propo-
sition 3.16), in which case the Fourier weight of f J|z at degree k and above
is 0. Since this weight at most 1 in all cases we conclude

E
(J|z)
[ ∑

S⊆[n]
|S|≥k
 ̂f J|z(S)2] ≤ ϵ.

Using Proposition 4.17 we have

E
(J|z)
[ ∑

S⊆[n]
|S|≥k
 ̂f J|z(S)
2] = ∑

S⊆[n]
|S|≥k
 E
(J|z)[ ̂f J|z(S)2] = ∑

U⊆[n] Pr
(J|z)[|U ∩ J| ≥ k] · ̂f (U)
2.

The distribution of random variable |U ∩ J| is Binomial(|U|, δ). When |U| ≥
3k/δ this random variable has mean at least 3k, and a Chernoff bound shows
Pr[|U ∩ J| < k] ≤ exp(− 2
3 k) ≤ 2/3. Thus

ϵ ≥ ∑

U⊆[n] Pr
(J|z)[|U ∩ J| ≥ k] · ̂f (U)
2 ≥ ∑

|U|≥3k/δ(1 − 2/3) · ̂f (U)2

and hence ∑
|U|≥3k/δ ̂f (U)
2 ≤ 3ϵ as claimed. □

We can now improve the dependence on ϵ in Corollary 4.8’s low-degree
spectral concentration for DNFs:

Theorem 4.22. Suppose f : {−1, 1}n → {−1, 1} is computable by a DNF of
width w. Then f ’s Fourier spectrum is ϵ-concentrated on degree up to O(w log(1/ϵ)).

Proof. This follows immediately from Håstad’s Switching Lemma together
with Lemma 4.21, taking δ = 1
10w and k = C log(1/ϵ) for a sufﬁciently large
constant C. □

In Lemma 4.21, instead of using the fact that depth-k decision trees have
no Fourier weight above degree k, we could have used the fact that their
Fourier 1-norm is at most 2k. As you are asked to show in Exercise 4.11, this
would yield:
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

102 4. DNF formulas and small-depth circuits

Lemma 4.23. Let f : {−1, 1}n → {−1, 1} and let (J | z) be a δ-random restriction.
Then ∑

U⊆[n] δ|U| · | ̂f (U)| ≤ E
(J|z)[2
DT( f J|z)].

We can combine this with the Switching Lemma to deduce that width-w
DNFs have small Fourier 1-norm at low degree:

Theorem 4.24. Suppose f : {−1, 1}n → {−1, 1} is computable by a DNF of
width w. Then for any k, ∑

|U|≤k | ̂f (U)| ≤ 2 · (20w)k.

Proof. Apply Håstad’s Switching Lemma to f with δ = 1
20w to deduce

E
(J|z)[2
DT( f J|z)] ≤ ∞∑

d=0
( 5
20 )d · 2d = 2.

Thus from Lemma 4.23 we get

2 ≥ ∑

U⊆[n]
( 1
20w )|U| · | ̂f (U)| ≥ ( 1
20w )k · ∑

|U|≤k | ̂f (U)|,

as needed. □

Our two theorems about the Fourier structure of DNF are almost enough
to prove Mansour’s Conjecture:

Theorem 4.25. Let f : {−1, 1}n → {−1, 1} be computable by a DNF of width w ≥
2. Then for any ϵ ∈ (0, 1/2], the Fourier spectrum of f is ϵ-concentrated on a
collection F with |F | ≤ wO(w log(1/ϵ)).

Proof. Let k = Cw log(4/ϵ) and let g = f ≤k. If C is a large enough constant,
then Theorem 4.22 tells us that ∥ f − g∥
2
2 ≤ ϵ/4. Furthermore, Theorem 4.24
gives ˆ∥g ˆ∥1 ≤ wO(w log(1/ϵ)). By Exercise 3.16, g is (ϵ/4)-concentrated on some
collection F with |F | ≤ 4ˆ∥g ˆ∥2
1/ϵ ≤ wO(w log(1/ϵ)). And so by Exercise 3.17, f is
ϵ-concentrated on this same collection. □

For the interesting case of DNFs of width O(log n) and constant ϵ, we get
concentration on a collection of cardinality O(log n)O(log n) = nO(log log n), nearly
polynomial. Using Proposition 4.9 (and Exercise 3.17) we get the same deduc-
tion for DNFs of size poly(n); more generally, for size s we have ϵ-concentration
on a collection of cardinality at most (s/ϵ)
O(log log(s/ϵ) log(1/ϵ)).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.5. Highlight: LMN’s work on constant-depth circuits 103

4.5. Highlight: LMN’s work on constant-depth circuits

Having derived strong results about the Fourier spectrum of small DNFs and
CNFs, we will now extend to the case of constant-depth circuits. We begin
by describing how Håstad applied his Switching Lemma to constant-depth
circuits. We then describe some Fourier-theoretic consequences coming from
a very early (1989) work in analysis of Boolean functions by Linial, Mansour,
and Nisan (LMN).

To deﬁne constant-depth circuits it is best to start with a picture. Here is
an example of a depth-3 circuit:

Figure 4.1. Example of a depth-3 circuit, with the layer 0 nodes at the
bottom and the layer 3 node at the top

This circuit computes the function

x1x2 ∧ (x1x3 ∨ x3x4) ∧ (x3x4 ∨ x2),

where we suppressed the ∧ in concatenated literals. To be precise:

Deﬁnition 4.26. For an integer d ≥ 2, we deﬁne a depth-d circuit over
Boolean variables x1, . . . , xn as follows: It is a directed acyclic graph in which
the nodes (“gates”) are arranged in d + 1 layers, with all arcs (“wires”) going
from layer j − 1 to layer j for some j ∈ [d]. There are exactly 2n nodes in
layer 0 (the “inputs”) and exactly 1 node in layer d (the “output”). The nodes
in layer 0 are labeled by the 2n literals. The nodes in layers 1, 3, 5, etc. have
the same label, either ∧ or ∨, and the nodes in layers 2, 4, 6, etc. have the
other label. Each node “computes” a function {−1, 1}n → {−1, 1}: the literals
compute themselves and the ∧ (respectively, ∨) nodes compute the logical
AND (respectively, OR) of the functions computed by their incoming nodes.
The circuit itself is said to compute the function computed by its output node.

In particular, DNFs and CNFs are depth-2 circuits. We extend the deﬁni-
tions of size and width appropriately:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

104 4. DNF formulas and small-depth circuits

Deﬁnition 4.27. The size of a depth-d circuit is deﬁned to be the number of
nodes in layers 1 through d − 1. Its width is the maximum in-degree of any
node at layer 1. (As with DNFs and CNFs, we insist that no node at layer 1 is
connected to a variable or its negation more than once.)

The layering we assume in our deﬁnition of depth-d circuits can be achieved
with a factor-2d size overhead for any “unbounded fan-in AND/OR/NOT cir-
cuit”. We will not discuss any other type of Boolean circuit in this section.

We now show that Håstad’s Switching Lemma can be usefully applied not
just to DNFs and CNFs but more generally to constant-depth circuits:

Lemma 4.28. Let f : {−1, 1}n → {−1, 1} be computable by a depth-d circuit of
size s and width w, and let ϵ ∈ (0, 1]. Set

δ = 1
10w
 ( 1
10ℓ
 )d−2 , where ℓ = log(2s/ϵ).

Then if (J | z) is a δ-random restriction, Pr[DT( f J|z) ≥ log(2/ϵ)] ≤ ϵ.

Proof. The d = 2 case is immediate from Håstad’s Switching Lemma, so we
assume d ≥ 3.

The ﬁrst important observation is that random restrictions “compose”.
That is, making a δ1-random restriction followed by a δ2-random restriction
to the free coordinates is equivalent to making a δ1δ2-random restriction.
Thus we can think of (J | z) as being produced as follows:

(1) make a 1
10w -random restriction;

(2) make d − 3 subsequent 1
10ℓ -random restrictions;

(3) make a ﬁnal 1
10ℓ -random restriction.

Without loss of generality, assume the nodes at layer 2 of the circuit are
labeled ∨. Thus any node g at layer 2 computes a DNF of width at most w.
By Håstad’s Switching Lemma, after the initial 1
10w -random restriction g can
be replaced by a decision tree of depth at most ℓ except with probability at
most 2
−ℓ. In particular, it can be replaced by a CNF of width at most ℓ, using
Proposition 4.5. If we write s2 for the number of nodes at layer 2, a union
bound lets us conclude:

Pr
1
10w -random
restriction
 [not all nodes at layer 2 replaceable by width-ℓ CNFs] ≤ s2 · 2−ℓ.

(4.1)

We now come to the second important observation: If all nodes at layer 2
can be switched to width-ℓ CNFs, then layers 2 and 3 can be “compressed”,
producing a depth-(d − 1) circuit of width at most ℓ. More precisely, we can
form an equivalent circuit by shortening all length-2 paths from layer 1 to

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.5. Highlight: LMN’s work on constant-depth circuits 105

layer 3 into single arcs, and then deleting the nodes at layer 2. We give an
illustration of this in Figure 4.2:

Figure 4.2. At top is the initial circuit. Under the restriction ﬁxing x3 =
True, all three DNFs at layer 2 may be replaced by CNFs of width at most 2.
Finally, the nodes at layers 2 and 3 may be compressed.

Assuming the event in (4.1) does not occur, the initial 1
10w -random restric-
tion reduces the circuit to having depth-(d − 1) and width at most ℓ. The
number of ∧-nodes at the new layer 2 is at most s3, the number of nodes at
layer 3 in the original circuit.

Next we make a 1
10ℓ -random restriction. As before, by Håstad’s Switching
Lemma this reduces all width-ℓ CNFs at the new layer 2 to depth-ℓ decision
trees (hence width-ℓ DNFs), except with probability at most s3 · 2−ℓ. We may
then compress layers and reduce depth again.

Proceeding for all 1
10ℓ -random restrictions except the ﬁnal one, a union
bound gives

Pr
1
10w ( 1
10ℓ )d−3-random
restriction
 [circuit does not reduce to depth 2 and width ℓ]

≤ s2 · 2−ℓ + s3 · 2−ℓ + · · · + sd−1 · 2−ℓ ≤ s · 2−ℓ = ϵ/2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

106 4. DNF formulas and small-depth circuits

Assuming the event above does not occur, Håstad’s Switching Lemma tells us
that the ﬁnal 1
10ℓ -random restriction reduces the circuit to a decision tree of
depth less than log(2/ϵ) except with probability at most ϵ/2. This completes
the proof. □

We may now obtain the main theorem of Linial, Mansour, and Nisan:

LMN Theorem. Let f : {−1, 1}n → {−1, 1} be computable by a depth-d circuit
of size s > 1 and let ϵ ∈ (0, 1/2]. Then f ’s Fourier spectrum is ϵ-concentrated up
to degree O(log(s/ϵ))d−1 · log(1/ϵ).

Proof. If the circuit for f also had width at most w, we would be able to
deduce 3ϵ-concentration up to degree 30w·(10 log(2s/ϵ))d−2 ·log(2/ϵ) by combin-
ing Lemma 4.28 with Lemma 4.21. But if we simply delete all layer-1 nodes
of width at least log(s/ϵ), the resulting circuit computes a function which is
ϵ-close to f , as in the proof of Proposition 4.9. Thus (using Exercise 3.17) f ’s
spectrum is O(ϵ)-concentrated up to degree O(log(2s/ϵ))d−1 · log(2/ϵ), and the
result follows by adjusting constants. □

Remark 4.29. Håstad [Hås01a] has slightly sharpened the degree in the
LMN Theorem to O(log(s/ϵ))d−2 · log(s) · log(1/ϵ).

In Exercise 4.20 you are asked to use a simpler version of this proof, along
the lines of Theorem 4.20, to show the following:

Theorem 4.30. Let f : {−1, 1}n → {−1, 1} be computable by a depth-d circuit of
size s. Then I[ f ] ≤ O(log s)d−1.

These rather strong Fourier concentration results for constant-depth cir-
cuits have several applications. By introducing the Low-Degree Algorithm for
learning, Linial–Mansour–Nisan gave as their main application:

Theorem 4.31. Let C be the class of functions f : {−1, 1}n → {−1, 1} computable
depth-d poly(n)-size circuits. Then C can be learned from random examples
with error any ϵ = 1/poly(n) in time nO(log n)d .

In complexity theory the class of poly-size, constant-depth circuits is re-
ferred to as AC0. Thus the above theorem may be summarized as “AC0 is
learnable in quasipolynomial time”. In fact, under a strong enough assump-
tion about the intractability of factoring certain integers, it is known that
quasipolynomial time is required to learn AC0 circuits, even with query ac-
cess [Kha93].

The original motivation of the line of work leading to Håstad’s Switching
Lemma was to show that the parity function χ[n] cannot be computed in AC0.
Håstad even showed that AC0 cannot even approximately compute parity. We
can derive this result from the LMN Theorem:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.6. Exercises and notes 107

Corollary 4.32. Fix any constant ϵ0 > 0. Suppose C is a depth-d circuit
over {−1, 1}n with Prx[C(x) = χ[n](x)] ≥ 1/2 + ϵ0. Then the size of C is at least
2Ω(n1/(d−1)).

Proof. The hypothesis on C implies ̂C([n]) ≥ 2ϵ0. The result then follows by
taking ϵ = 2ϵ2
0 in the LMN Theorem. □

This corollary is close to being tight, since the parity χ[n] can be com-
puted by a depth-d circuit of size n2n1/(d−1) for any d ≥ 2; see Exercise 4.12.
The simpler result Theorem 4.30 is often handier for showing that certain
functions can’t be computed by AC0 circuits. For example, we know that
I[Majn] = Θ(
pn); hence any constant-depth circuit computing Majn must have
size at least 2nΩ(1).

Finally, Linial, Mansour, and Nisan gave an application to cryptography.
Informally, a function f : {−1, 1}m ×{−1, 1}n → {−1, 1} is said to be a “pseudoran-
dom function generator with seed length m” if, for any efﬁcient algorithm A,
∣
∣
∣
∣ Pr
s∼{−1,1}m[A( f (s, ·)) = “accept”] − Pr
g∼{−1,1}{−1,1}n [A(g) = “accept”]
∣
∣
∣
∣ ≤ 1/nω(1).

Here the notation A(h) means that A has query access to target function h,
and g ∼ {−1, 1}
{−1,1}n means that g is a uniformly random n-bit function. In
other words, for almost all “seeds” s the function f (s, ·) : {−1, 1}n → {−1, 1} is
nearly indistinguishable (to efﬁcient algorithms) from a truly random func-
tion. Theorem 4.30 shows that pseudorandom function generators cannot be
computed by AC0 circuits. To see this, consider the algorithm A(h) which
chooses x ∼ {−1, 1}n and i ∈ [n] uniformly at random, queries h(x) and h(x⊕i),
and accepts if these values are unequal. If h is a uniformly random function,
A(h) will accept with probability 1/2. In general, A(h) accepts with probability
I[h]/n. Thus Theorem 4.30 implies that if h is computable in AC0 then A(h)
accepts with probability at most polylog(n)/n ≪ 1/2.

4.6. Exercises and notes

4.1 Show that every function f : {0, 1}n → {0, 1} can be represented by a DNF
formula of size at most 2n and width at most n.

4.2 Suppose we have a certain CNF computing f : {0, 1}n → {0, 1}. Switch
ANDs with ORs in the CNF. Show that the result is a DNF computing the
Boolean dual f † : {0, 1}n → {0, 1}.

4.3 A DNF formula is said to be monotone if its terms contain only unnegated
variables. Show that monotone DNFs compute monotone functions and
that any monotone function can be computed by a monotone DNF, but
that a nonmonotone DNF may compute a monotone function.

4.4 Let f : {−1, 1}n → {−1, 1} be computable by a DNF of size s.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

108 4. DNF formulas and small-depth circuits

(a) Show there exists S ⊆ [n] with |S| ≤ log(s) + O(1) and | ̂f (S)| ≥ Ω(1/s).
(Hint: Use Proposition 4.9 and Exercise 3.30.)
(b) Let C be the concept class of functions : {−1, 1}n → {−1, 1} computable
by DNF formulas of size at most s. Show that C is learnable using
queries with error 1
2 − Ω(1/s) in time poly(n, s). (Such a result, with
error bounded away from 1
2 , is called weak learning.)

4.5 Verify Proposition 4.12.

4.6 Verify Proposition 4.14.

4.7 For each n that is an input length for Tribesn, show that there exists a
function f : {−1, 1}n → {−1, 1} that is truly unbiased (E[ f ] = 0) and has
Infi[ f ] ≤ O( log n
n ) for all i ∈ [n].

4.8 Suppose f : {−1, 1}n → {−1, 1} is computed by a read-once DNF (mean-
ing no variable is involved in more than one term) in which all terms
have width exactly w. Compute ˆ∥ f ˆ∥1 exactly. Deduce that ˆ∥Tribesn ˆ∥1 =
2
 n
log n (1±o(1)) and that there are n-variable width-2 DNFs with Fourier 1-
norm Ω(p
3/2n).

4.9 Give a direct (Fourier-free) proof of Corollary 4.18. (Hint: Condition on
whether i ∈ J.)

4.10 Tighten the constant factor on log s in Theorem 4.20 as much as you can
(avenues of improvement include the argument in Lemma 4.19, the choice
of δ, and Exercise 4.17).

4.11 Prove Lemma 4.23.

4.12 (a) Show that the parity function χ[n] : {−1, 1}n → {−1, 1} can be computed
by a DNF (or a CNF) of size 2n−1.
(b) Show that the bound 2n−1 above is exactly tight. (Hint: Show that
every term must have width exactly n.)
(c) Show that there is a depth-3 circuit of size O(n1/2)·2n1/2 computing χ[n].
(Hint: Break up the input into n1/2 blocks of size n1/2 and use (a) twice.
How can you compress the result from depth 4 to depth 3?)
(d) More generally, show there is a depth-d circuit of size O(n1−1/(d−1)) ·
2n1/(d−1) computing χ[n].

4.13 In this exercise we deﬁne the most standard class of Boolean circuits. A
(De Morgan) circuit C over Boolean variables x1, . . . , xn is a directed acyclic
graph in which each node (“gate”) is labeled with either an xi or with ∧,
∨, or ¬ (logical NOT). Each xi is used as label exactly once; the associated
nodes are called “input” gates and must have in-degree 0. Each ∧ and ∨
node must have in-degree 2, and each ¬ node must have in-degree 1. Each
node “computes” a Boolean function of the inputs as in Deﬁnition 4.26.
Finally, one node of C is designated as the “output” gate, and C itself is

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.6. Exercises and notes 109

said to compute the function computed by the output node. For this type
of circuit we deﬁne its size, denoted size(C), to be the number of nodes.
Show that each of the following n-input functions can be computed by
De Morgan circuits of size O(n):
(a) The logical AND function.
(b) The parity function.
(c) The complete quadratic function from Exercise 1.1.

4.14 Show that computing Tribesw,s by a CNF formula requires size at least ws.

4.15 Show that there is a universal constant ϵ0 > 0 such that the following
holds: Every 3
4 n-junta g : {−1, 1}n → {−1, 1} is ϵ0-far from Tribesn (assum-
ing n > 1). (Hint: Letting J denote the coordinates on which g depends,
show that if J has non-full intersection with at least 1
4 of the tribes/terms
then when x ∼ {−1, 1}J, there is a constant chance that Var[ f|x] ≥ Ω(1).)

4.16 Using the KKL Theorem, show that if f : {−1, 1}n → {−1, 1} is a transitive-
symmetric function with Var[ f ] ≥ Ω(1), then I[ f ] ≥ Ω(log n).

4.17 Let f : {True,False}n → {True,False} be computable by a CNF C of width w
over variables x1, . . . , xn. In this exercise you will show that I[ f ] ≤ w.
Consider the following algorithm A , which takes as input a permu-
tation π ∈ Sn and a “seed” r ∈ {True,False}n, and which “tries” to output a
string z satisfying C:
A (π, r) :
For i = π(1), π(2), . . . , π(n):
If C contains the clause (xi) and the clause (xi), abort.
Else if C contains just the clause (xi), set zi = True.
Else if C contains just the clause (xi), set zi = False.
Else set zi = r i and say coordinate i was “unforced”.
Syntactically simplify C under the restriction xi = zi.
Output z.
We write F j(π, r) for the 0-1 indicator that coordinate j was forced in the
execution of A (π, r).
(a) Show that if A (π, r) does not abort, then its output z satisﬁes C.
(b) Fix any y satisfying C and write p(y) = Prπ,r[A (π, r) = y], where π
and r are uniformly random. Show that p(y) = Eπ[
∏n
j=1(1/2)
1−F j(π,y)].
(c) Deduce 2n p(y) ≥ 2 ∑n
j=1 Eπ[F j(π, y)].

(d) Suppose further that y⊕ j does not satisfy C. Show Eπ[F j(π, y)] ≥ 1/w.
(e) Deduce I[ f ] ≤ w.

4.18 Given Boolean variables x1, . . . , xn, a “random monotone term of width w ∈
N +” is deﬁned to be the logical AND of xi1, . . . , xiw , where i1, . . . , iw are
chosen independently and uniformly at random from [n]. (If the i j’s are
not all distinct then the resulting term will in fact have width strictly
less than w.) A “random monotone DNF of width w and size s” is deﬁned

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

110 4. DNF formulas and small-depth circuits

to be the logical OR of s independent random monotone terms. For this
exercise we assume n is a sufﬁciently large perfect square, and we let ϕ
be a random monotone DNF of width pn and size 2
pn.
(a) Fix an input x ∈ {−1, 1}n and deﬁne u = (∑n
i=1 xi)/pn ∈ [−
pn, pn].
Let V j be the event that the jth term of ϕ is made 1 (logical False)
by x. Compute Pr[V j] and Pr[ϕ(x) = 1], and show that the latter is
at least 10
−9 assuming |u| ≤ 2.
(b) Let U j be the event that the jth term of ϕ has exactly one 1 on input x.
Show that Pr[U j | V j] ≥ Ω(w2−w) assuming |u| ≤ 2.
(c) Suppose we condition on ϕ(x) = 1; i.e., ∩ jV j. Argue that the events U j
are independent. Further, argue that for the U j’s that do occur, the
indices of their uniquely-1 variables are independent and uniformly
random among the 1’s of x.
(d) Show that Pr[sensϕ(x) ≥ cpn | ϕ(x) = 1] ≥ 1 − 10−10 for c > 0 a sufﬁ-
ciently small constant.
(e) Show that Prx[|(∑n
i=1 xi)/pn| ≤ 2] ≥ Ω(1).
(f ) Deduce that there exists a monotone function f : {−1, 1}n → {−1, 1}
with the property that Prx[sens f (x) ≥ c′pn] ≥ c′ for some universal
constant c′ > 0.
(g) Both Majn and the function f from the previous exercise have average
sensitivity Θ(
pn). Contrast the “way” in which this occurs for the two
functions.

4.19 In this exercise you will prove the Baby Switching Lemma with constant 3
in place of 5. Let φ = T1 ∨ T2 ∨ · · · ∨ Ts be a DNF of width w ≥ 1 over
variables x1, . . . , xn. We may assume δ ≤ 1/3, else the theorem is trivial.
(a) Suppose R = (J | z) is a “bad” restriction, meaning that φJ|z is not a
constant function. Let i be minimal such that (Ti)J|z is neither con-
stantly True or False, and let j be minimal such that x j or x j appears in
this restricted term. Show there is a unique restriction R′ = (J\{ j} | z′)
extending R that doesn’t falsify Ti.
(b) Suppose we enumerate all bad restrictions R, and for each we write
the associated R′ as in (a). Show that no restriction is written more
than w times.
(c) If (J | z) is a δ-random restriction and R and R′ are as in (a), show
that Pr[(J | z) = R] = 2δ
1−δ Pr[(J | z) = R′].
(d) Complete the proof by showing Pr[(J | z) is bad] ≤ 3δw.

4.20 In this exercise you will prove Theorem 4.30. Say that a “(d, w, s′)-circuit”
is a depth-d circuit with width at most w and with at most s′ nodes at
layers 2 through d (i.e., excluding layers 0 and 1).
(a) Show by induction on d ≥ 2 that any f : {−1, 1}n → {−1, 1} computable
by a (d, w, s′)-circuit satisﬁes I[ f ] ≤ wO(log s′)d−2.
(b) Deduce Theorem 4.30.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

4.6. Exercises and notes 111

Notes. Mansour’s Conjecture dates from 1994 [Man94]. Even the weaker
version would imply that the Kushilevitz–Mansour algorithm learns the class
of poly(n)-size DNF with any constant error, using queries, in time poly(n). In
fact, this learning result was subsequently obtained in a celebrated work of
Jackson [Jac97], using a different method (which begins with Exercise 4.4).
Nevertheless, the Mansour Conjecture remains important for learning theory
since Gopalan, Kalai, and Klivans [GKK08] have shown that it implies the
same learning result in the more challenging and realistic model of “agnostic
learning”. Theorems 4.24 and 4.25 are also due to Mansour [Man95].

The method of random restrictions dates back to Subbotovskaya [Sub61].
Håstad’s Switching Lemma [Hås87] and his Lemma 4.28 are the culmina-
tion of a line of work due to Furst, Saxe, and Sipser [FSS84], Ajtai [Ajt83],
and Yao [Yao85]. Linial, Mansour, and Nisan [LMN89, LMN93] proved
Lemma 4.21, which allowed them to deduce the LMN Theorem and its con-
sequences. An additional cryptographic application of the LMN Theorem
is found in Goldmann and Russell [GR00]. The strongest lower bound cur-
rently known for approximately computing parity in AC0 is due to Impagli-
azzo, Matthews, and Paturi [IMP12] and independently to Håstad [Hås12].

Theorem 4.20 and its generalization Theorem 4.30 are from the work of
Boppana [Bop97]; Linial, Mansour, and Nisan had given the weaker bound
O(log s)d. Exercise 4.17 is due to Amano [Ama11], and Exercise 4.18 is due
to Talagrand [Tal96].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 5

Majority and threshold
functions

This chapter is devoted to linear threshold functions, their generalization
to higher degrees, and their exemplar the majority function. The study of
LTFs leads naturally to the introduction of the Central Limit Theorem and
Gaussian random variables – important tools in analysis of Boolean functions.
We will ﬁrst use these tools to analyze the Fourier spectrum of the Majn
function, which in some sense “converges” as n → ∞. We’ll then extend to
analyzing the degree-1 Fourier weight, noise stability, and total inﬂuence of
general linear threshold functions.

5.1. Linear threshold functions and polynomial threshold
functions

Recall from Chapter 2.1 that a linear threshold function (abbreviated LTF) is
a Boolean-valued function f : {−1, 1}n → {−1, 1} that can be represented as

f (x) = sgn(a0 + a1x1 + · · · + an xn) (5.1)

for some constants a0, a1, . . . , an ∈ R . (For deﬁniteness we’ll take sgn(0) = 1.
If we’re using the representation f : {−1, 1}n → {0, 1}, then f is an LTF if it
can be represented as f (x) = 1{a0+a1 x1+···+an xn>0}.) Examples include majority,
AND, OR, dictators, and decision lists (Exercise 3.23). Besides representing
“weighted majority” voting schemes, LTFs play an important role in learning
theory and in circuit complexity.

There is also a geometric perspective on LTFs. Writing ℓ(x) = a0 + a1x1 +
· · · + an xn, we can think of ℓ as an afﬁne function R n → R . Then sgn(ℓ(x)) is

113

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

114 5. Majority and threshold functions

the ±1-indicator of a halfspace in R n. A Boolean LTF is thus the restriction of
such a halfspace-indicator to the discrete cube {−1, 1}n ⊂ R n. Equivalently, a
function f : {−1, 1}n → {−1, 1} is an LTF if and only if it has a “linear separator”;
i.e., a hyperplane in R n that separates the points f labels 1 from the points f
labels −1.

An LTF f : {−1, 1}n → {−1, 1} can have several different representations
as in (5.1) – in fact it always has inﬁnitely many. This is clear from the
geometric viewpoint; any small enough perturbation to a linear separator will
not change the way it partitions the discrete cube. Because we can make
these perturbations, we may ensure that a0 + a1x1 + · · · + an xn ̸= 0 for every
x ∈ {−1, 1}n. We’ll usually insist that LTF representations have this property
so that the nuisance of sgn(0) doesn’t arise. We also observe that we can scale
all of the coefﬁcients in an LTF representation by the same positive constant
without changing the LTF. These observations can be used to show it’s always
possible to take the ai’s to be integers (Exercise 5.1). However, we will most
often scale so that ∑n
i=1 a2
i = 1; this is convenient when using the Central
Limit Theorem.

The most elegant result connecting LTFs and Fourier expansions is Chow’s
Theorem, which says that a Boolean LTF is completely determined by its
degree-0 and degree-1 Fourier coefﬁcients. In fact, it’s determined not just
within the class of LTFs but within the class of all Boolean functions:

Theorem 5.1. Let f : {−1, 1}n → {−1, 1} be an LTF and let g : {−1, 1}n → {−1, 1}
be any function. If ̂g(S) = ̂f (S) for all |S| ≤ 1, then g = f .

Proof. Let f (x) = sgn(ℓ(x)), where ℓ : {−1, 1}n → R has degree at most 1 and
is never 0 on {−1, 1}n. For any x ∈ {−1, 1}n we have f (x)ℓ(x) = |ℓ(x)| ≥ g(x)ℓ(x),
with equality if and only if f (x) = g(x) (here we use ℓ(x) ̸= 0). Using this
observation along with Plancherel’s Theorem (twice) we have
∑

|S|≤1 ̂f (S) ̂ℓ(S) = E[ f (x)ℓ(x)] ≥ E[g(x)ℓ(x)] = ∑

|S|≤1 ̂g(S) ̂ℓ(S).

But by assumption, the left-hand and right-hand sides above are equal. Thus
the inequality must be an equality for every value of x; i.e., f (x) = g(x) ∀x. □

In light of Chow’s Theorem, the n +1 numbers ̂g(;), ̂g({1}), . . . , ̂g({n}) are some-
times called the Chow parameters of the Boolean function g.

As we will show in Section 5.5, linear threshold functions are very noise-
stable; hence they have a lot of their Fourier weight at low degrees. Here is a
simple result along these lines:

Theorem 5.2. Let f : {−1, 1}n → {−1, 1} be an LTF. Then W
≤1[ f ] ≥ 1/2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.1. Linear threshold functions and polynomial threshold functions 115

Proof. Writing f (x) = sgn(ℓ(x)) we have

∥ℓ∥1 = E[|ℓ(x)|] = 〈 f , ℓ〉 = 〈 f ≤1, ℓ〉 ≤ ∥ f ≤1∥2∥ℓ∥2 = √
W≤1[ f ] · ∥ℓ∥2,

where the third equality follows from Plancherel and the inequality is Cauchy–
Schwarz. Assume ﬁrst that ℓ(x) = a1x1 + · · · + an xn (i.e., ℓ(x) has no constant
term). The Khintchine–Kahane Inequality (Exercise 2.55) states that ∥ℓ∥1 ≥
1p
2 ∥ℓ∥2, and hence we deduce

1p
2 ∥ℓ∥2 ≤ √
W≤1[ f ] · ∥ℓ∥2.

The conclusion W
≤1[ f ] ≥ 1/2 follows immediately (since ∥ℓ∥2 cannot be 0). The
case when ℓ(x) has a constant term is handled in Exercise 5.5. □

From Exercise 2.22 we know that W≤1[Majn] = W1[Majn] ≥ 2/π for all n;
it is reasonable to conjecture that majority is extremal for Theorem 5.2. This
is an open problem.

Conjecture 5.3. Let f : {−1, 1}n → {−1, 1} be an LTF. Then W≤1[ f ] ≥ 2/π.

A natural generalization of linear threshold functions is polynomial thresh-
old functions:

Deﬁnition 5.4. A function f : {−1, 1}n → {−1, 1} is called a polynomial thresh-
old function (PTF) of degree at most k if it is expressible as f (x) = sgn(p(x))
for some real polynomial p : {−1, 1}n → R of degree at most k.

Example 5.5. Let f : {−1, 1}
4 → {−1, 1} be the 4-bit equality function, which
is 1 if and only if all input bits are equal. Then f is a degree-2 PTF because it
has the representation f (x) = sgn(−3 + x1x2 + x1x3 + x1x4 + x2x3 + x2x4 + x3x4).

Every Boolean function f : {−1, 1}n → {−1, 1} is a PTF of degree at most n,
since we can take the sign of its Fourier expansion. Thus we are usually
interested in the case when the degree k is “small”, say, k = On(1). Low-
degree PTFs arise frequently in learning theory, for example, as hypotheses
in the Low-Degree Algorithm and many other practical learning algorithms.
Indeed, any function with low noise sensitivity is close to being a low-degree
PTF; by combining Propositions 3.3 and 3.31 we immediately obtain:

Proposition 5.6. Let f : {−1, 1}n → {−1, 1} and let δ ∈ (0, 1/2]. Then f is
(3NSδ[ f ])-close to a PTF of degree 1/δ.

For a kind of converse to this proposition, see Section 5.5.

PTFs also arise in circuit complexity, wherein a PTF representation

f (x) = sgn
 ( s∑

i=1 ai xTi )

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

116 5. Majority and threshold functions

is thought of as a “threshold-of-parities circuit”: i.e., a depth-2 circuit with s
“parity gates” xTi at layer 1 and a single “(linear) threshold gate” at layer 2.
From this point of view, the size of the circuit corresponds to the sparsity of
the PTF representation:

Deﬁnition 5.7. We say a PTF representation f (x) = sgn(p(x)) has sparsity at
most s if p(x) is a multilinear polynomial with at most s terms.

For example, the PTF representation of the 4-bit equality function from Ex-
ample 5.5 has sparsity 7.

Let’s extend the two theorems about LTFs we proved above to the case of
PTFs. The generalization of Chow’s Theorem is straightforward; its proof is
left as Exercise 5.9:

Theorem 5.8. Let f : {−1, 1}n → {−1, 1} be a PTF of degree at most k and let
g : {−1, 1}n → {−1, 1} be any function. If ̂g(S) = ̂f (S) for all |S| ≤ k, then g = f .

We also have the following extension of Theorem 5.2:

Theorem 5.9. Let f : {−1, 1}n → {−1, 1} be a degree-k PTF. Then W
≤k[ f ] ≥ e−2k.

Proof. Writing f (x) = sgn(p(x)) for p of degree k, we again have

∥p∥1 = E[|p(x)|] = 〈 f , p〉 = 〈 f ≤k, p〉 ≤ ∥ f ≤k∥2∥p∥2 = √W≤k[ f ] · ∥p∥2.

To complete the proof we need the fact that ∥p∥2 ≤ ek∥p∥1 for any degree-k
polynomial p : {−1, 1}n → R . We will prove this much later in Theorem 9.22 of
Chapter 9 on hypercontractivity. □

The e−2k in this theorem cannot be improved beyond 2
1−k; see Exercise 5.11.

We close this section by discussing PTF sparsity. We begin with a (simpler)
variant of Theorem 5.9, which is useful for proving PTF sparsity lower bounds:

Theorem 5.10. Let f : {−1, 1}n → {−1, 1} be expressible as a PTF over the
collection of monomials F ⊆ 2[n]; i.e., f (x) = sgn(p(x)) for some polynomial
p(x) = ∑S∈F ̂p(S)xS. Then ∑S∈F | ̂f (S)| ≥ 1.

Proof. Deﬁne g : {−1, 1}n → R by g(x) = ∑S∈F ̂f (S) xS. Since ˆ∥p ˆ∥∞ ≤ ∥p∥1
(Exercise 3.9) we have

ˆ∥p ˆ∥∞ ≤ ∥p∥1 = E[ f (x)p(x)] = ∑

S⊆[n] ̂f (S) ̂p(S) = ∑

S∈F ̂g(S) ̂p(S) ≤ ˆ∥g ˆ∥1 ˆ∥p ˆ∥∞,

and hence ˆ∥g ˆ∥1 ≥ 1 as claimed. □

We can use this result to show that the “inner product mod 2 function”
(see Exercise 1.1) requires huge threshold-of-parities circuits:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.1. Linear threshold functions and polynomial threshold functions 117

Corollary 5.11. Any PTF representation of the inner product mod 2 function
IP2n : F 2n
2 → {−1, 1} has sparsity at least 2n.

Proof. This follows immediately from Theorem 5.10 and the fact that |̂IP2n(S)| =
2−n for all S ⊆ [2n] (Exercise 1.1). □

We can also show that any function f : {−1, 1}n → {−1, 1} with small Fourier
1-norm ˆ∥ f ˆ∥1 has a sparse PTF representation. In fact a stronger result holds:
such a function can be additively approximated by a sparse polynomial:

Theorem 5.12. Let f : {−1, 1}n → R be nonzero, let δ > 0, and let s ≥ 4nˆ∥ f ˆ∥
2
1/δ2

be an integer. Then there is a multilinear polynomial q : {−1, 1}n → R of spar-
sity at most s such that ∥ f − q∥∞ < δ.

Proof. The proof is by the probabilistic method. Let T ⊆ [n] be randomly

chosen according to the distribution Pr[T = T] = | ̂f (T)|
ˆ∥ f ˆ∥1 . Let T1, . . . , T s be inde-
pendent draws from this distribution and deﬁne the multilinear polynomial

p(x) = s∑

i=1 sgn( ̂f (T i)) xT i .

When x ∈ {−1, 1}n is ﬁxed, each monomial sgn( ̂f (T i)) xT i becomes a ±1-valued
random variable with expectation
∑

T⊆[n]
 | ̂f (T)|
ˆ∥ f ˆ∥1 · sgn( ̂f (T)) xT = 1
ˆ∥ f ˆ∥1
 ∑

T⊆[n] ̂f (T) xT = f (x)
ˆ∥ f ˆ∥1 .

Thus by a Chernoff bound, for any ϵ > 0,

Pr
T1,...,T s
 [∣
∣
∣p(x) − f (x)
ˆ∥ f ˆ∥1 s∣
∣
∣ ≥ ϵs] ≤ 2 exp(−ϵ2s/2).

Selecting ϵ = δ/ˆ∥ f ˆ∥1 and using s ≥ 4nˆ∥ f ˆ∥
2
1/δ2, the above probability is at most
2 exp(−2n) < 2−n. Taking a union bound over all 2n choices of x ∈ {−1, 1}n,
we conclude that there exists some p(x) = ∑s
i=1 sgn( ̂f (Ti)) xTi such that for all
x ∈ {−1, 1}n,
∣
∣
∣p(x) − f (x)
ˆ∥ f ˆ∥1 s∣
∣
∣ < ϵs = δ
ˆ∥ f ˆ∥1 s =⇒ ∣
∣
∣ ˆ∥ f ˆ∥1
s · p(x) − f (x)
∣
∣
∣ < δ.

Thus we may take q = ˆ∥ f ˆ∥1
s · p. □

Corollary 5.13. Let f : {−1, 1}n → {−1, 1}. Then f is expressible as a PTF of
sparsity at most s = ⌈4nˆ∥ f ˆ∥
2
1⌉. Indeed, f can be represented as a majority of s
parities or negated-parities.

Proof. Apply the previous theorem with δ = 1; we then have f (x) = sgn(q(x)).
Since this is also equivalent to sgn(p(x)), the terms sgn( ̂f (Ti)) xTi are the
required parities/negated-parities. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

118 5. Majority and threshold functions

Though functions computable by small DNFs need not have small Fourier
1-norm, it is a further easy corollary that they can be computed by sparse
PTFs: see Exercise 5.13. We also remark that there is no good converse to
Corollary 5.13: the Majn function has a PTF (indeed, an LTF) of sparsity n
but has exponentially large Fourier 1-norm (Exercise 5.26).

5.2. Majority, and the Central Limit Theorem

Majority is one of the more important functions in Boolean analysis, and
its study motivates the introduction of one of the more important tools: the
Central Limit Theorem (CLT). In this section we will show how the CLT can be
used to estimate the total inﬂuence and the noise stability of Majn. Though
we already determined I[Majn] ∼ p
2/πpn in Exercise 2.22 using binomial
coefﬁcients and Stirling’s Formula, computations using the CLT are more
ﬂexible and extend to other linear threshold functions.

We begin with a reminder about the CLT. Suppose X 1, . . . , X n are indepen-
dent random variables and S = X 1 + · · · + X n. Roughly speaking, the CLT says
that so long as no X i is too dominant in terms of variance, the distribution
of S is close to that of a Gaussian random variable with the same mean and
variance. Recall:

Notation 5.14. We write Z ∼ N(0, 1) denote that Z is a standard Gaussian
random variable. We use the notation

ϕ(z) = 1p
2π e−z2/2, Φ(t) = ∫ t

−∞ φ(z) dz, Φ(t) = Φ(−t) = ∫ ∞

t φ(z) dz

for the pdf, cdf, and complementary cdf of this random variable. More gen-
erally, if µ ∈ R d and Σ ∈ R d×d is a positive semideﬁnite matrix, we write
Z ∼ N(µ, Σ) to denote that Z is a d-dimensional random vector with mean µ
and covariance matrix Σ.

We give a precise statement of the CLT below in the form of the Berry–
Esseen Theorem. The CLT also extends to the multidimensional case (sums
of independent random vectors); we give a precise statement in Exercise 5.33.
In Chapter 11 we will show one way to prove such CLTs.

Let’s see how we can use the CLT to obtain the estimate I[Majn] ∼ p
2/πpn.
Recall the proof of Theorem 2.33, which shows that Majn maximizes ∑n
i=1 ̂f (i)
among all f : {−1, 1}n → {−1, 1}. In it we saw that

I[Majn] = n∑

i=1 …Majn(i) = E
x [Majn(x)(∑

i xi)] = E
x [| ∑

i xi|]. (5.2)

When using the CLT, it’s convenient to deﬁne majority (equivalently) as

Majn(x) = sgn
( n∑

i=1
 1pn xi)
.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.2. Majority, and the Central Limit Theorem 119

This motivates writing (5.2) as

I[Majn] = pn · E
x∼{−1,1}n[| ∑

i
 1pn xi|]. (5.3)

If we introduce S = ∑n
i=1 1pn xi, then S has mean 0 and variance ∑i(1/
pn)
2 = 1.
Thus the CLT tells us that the distribution of S is close (for large n) to that of
a standard Gaussian, Z ∼ N(0, 1). So as n → ∞ we have

E
x [|S|] ∼ E
Z∼N(0,1)
[|Z|] = 2 ∫ ∞

0 z · 1p
2π e−z2/2 dz = −
p
2/πe−z2/2 ∣
∣
∣∞

0 = p
2/π, (5.4)

which when combined with (5.3) gives us the estimate I[Majn] ∼ p
2/πpn.

To make this kind of estimate more precise we state the Berry–Esseen
Theorem, which is a strong version of the CLT giving explicit error bounds
rather than just limiting statements.

Berry–Esseen (Central Limit) Theorem. Let X 1, . . . , X n be independent
random variables with E[X i] = 0 and Var[X i] = σ2
i , and assume ∑n
i=1 σ2
i = 1.
Let S = ∑n
i=1 X i and let Z ∼ N(0, 1) be a standard Gaussian. Then for all u ∈ R ,

| Pr[S ≤ u] − Pr[Z ≤ u]| ≤ cγ,

where
 γ = n∑

i=1 ∥X i∥3
3

and c is a universal constant. (For deﬁniteness, c = .56 is acceptable.)

Remark 5.15. If all of the X i’s satisfy |X i| ≤ ϵ with probability 1, then we
can use the bound

γ = n∑

i=1 E[|X i|3] ≤ ϵ · n∑

i=1 E[|X i|2] = ϵ · n∑

i=1 σ2
i = ϵ.

See Exercises 5.16 and 5.17 for some additional observations.

Our most frequent use of the Berry–Esseen Theorem will be in analyzing
random sums
 S = n∑

i=1 ai xi,

where x ∼ {−1, 1}n and the constants ai ∈ R are normalized so that ∑i a2
i = 1.
For majority, all of the ai’s were equal to 1pn . But from Remark 5.15 we see
that S is close in distribution to a standard Gaussian so long as each |ai| is
small. For example, in Exercise 5.31 you are asked to show the following:

Theorem 5.16. Let a1, . . . , an ∈ R satisfy ∑i a2
i = 1 and |ai| ≤ ϵ for all i. Then
∣
∣
∣
∣ E
x∼{−1,1}n[| ∑

i ai xi|] − p
2/π∣
∣
∣
∣ ≤ Cϵ,

where C is a universal constant.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

120 5. Majority and threshold functions

Theorem 5.16 justiﬁes (5.4) with an error bound of O(1/pn), yielding the
more precise estimate I[Majn] = p
2/πpn ± O(1) (cf. Exercise 2.22, which gives
an even better error bound).

Now let’s turn to the noise stability of majority. Theorem 2.45 stated the
formula lim
n→∞ Stabρ[Majn] = 2
π arcsin ρ = 1 − 2
π arccos ρ. (5.5)

Let’s now spend some time justifying this using the multidimensional CLT.
(For complete details, see Exercise 5.33.) By deﬁnition,

Stabρ[Majn] = E
(x,y)
ρ-correlated

[Majn(x) · Majn(y)] = E
(x,y)
ρ-correlated

[sgn(
∑

i
 1pn xi) · sgn(
∑

i
 1pn yi)]. (5.6)

For each i ∈ [n] let’s stack 1pn xi and 1pn yi into a 2-dimensional vector and
then write
 ⃗S = n∑

i=1
 [ 1pn xi
1pn yi
]
 ∈ R 2. (5.7)

We are summing n independent random vectors, so the multidimensional CLT
tells us that the distribution of ⃗S is close to that of a 2-dimensional Gaussian
⃗Z with the same mean and covariance matrix, namely (see Exercise 5.19)

⃗Z ∼ N ([
0
0
] , [1 ρ
ρ 1
]) .

Continuing from (5.6),

Stabρ[Majn] = E[sgn(⃗S1) · sgn(⃗S2)]

= Pr[sgn(⃗S1) = sgn(⃗S2)] − Pr[sgn(⃗S1) ̸= sgn(⃗S2)]

= 2 Pr[sgn(⃗S1) = sgn(⃗S2)] − 1 = 4 Pr[⃗S ∈ Q−−] − 1,

where Q−− denotes the lower-left quadrant of R 2 and the last step uses the
symmetry Pr[⃗S ∈ Q++] = Pr[⃗S ∈ Q−−]. Since Q−− is convex, the 2-dimensional
CLT lets us deduce
 lim
n→∞ Pr[⃗S ∈ Q−−] = Pr[⃗Z ∈ Q−−].

So to justify the noise stability formula (5.5) for majority, it remains to verify

4 Pr[⃗Z ∈ Q−−] − 1 = 1 − 2
π arccos ρ ⇐⇒ Pr[⃗Z ∈ Q−−] = 1
2 − 1
2 arccos ρ

π .

And this in turn is a 19th-century identity known as Sheppard’s Formula:

Sheppard’s Formula. Let z1, z2 be standard Gaussian random variables
with correlation E[z1 z2] = ρ ∈ [−1, 1]. Then

Pr[z1 ≤ 0, z2 ≤ 0] = 1
2 − 1
2 arccos ρ

π .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.3. The Fourier coefﬁcients of Majority 121

Proving Sheppard’s Formula is a nice exercise using the rotational symmetry
of a pair of independent standard Gaussians; we defer the proof till Exam-
ple 11.19 in Chapter 11.1. This completes the justiﬁcation of formula (5.5) for
the limiting noise stability of majority.

You may have noticed that once we applied the 2-dimensional CLT to (5.6),
the remainder of the derivation had nothing to do with majority. In fact,
the same analysis works for any linear threshold function sgn(a1x1 + · · · +
an xn), the only difference being the “error term” arising from the CLT. As in
Theorem 5.16, this error is small so long as no coefﬁcient ai is too dominant:

Theorem 5.17. Let f : {−1, 1}n → {−1, 1} be an unbiased LTF, f (x) = sgn(a1x1 +
· · · + an xn) with ∑i a2
i = 1 and |ai| ≤ ϵ for all i. Then for any ρ ∈ (−1, 1),
∣
∣
∣Stabρ[ f ] − 2
π arcsin ρ∣
∣
∣ ≤ O( ϵp
1−ρ2
 ).

You are asked to prove Theorem 5.17 in Exercise 5.33. In the particular
case of Majn where ai = 1pn for all i we can make a slightly stronger claim
(see Exercise 5.23):

Theorem 5.18. For any ρ ∈ [0, 1), Stabρ[Majn] is a decreasing function of n,
with 2
π arcsin ρ ≤ Stabρ[Majn] ≤ 2
π arcsin ρ + O( 1p
1−ρ2pn
 ).

We end this section by mentioning another way in which the majority
function is extremal: among all unbiased functions with small inﬂuences, it
has (essentially) the largest noise stability.

Majority Is Stablest Theorem. Fix ρ ∈ (0, 1). Then for any f : {−1, 1}n →
[−1, 1] with E[ f ] = 0 and MaxInf[ f ] ≤ τ,

Stabρ[ f ] ≤ 2
π arcsin ρ + oτ(1) = 1 − 2
π arccos ρ + oτ(1).

For sufﬁciently small ρ, we’ll prove this in Section 5.4. The proof of the full
Majority Is Stablest Theorem will have to wait until Chapter 11.

5.3. The Fourier coefﬁcients of Majority

In this section we will analyze the Fourier coefﬁcients of Majn. In fact, we
give an explicit formula for them in Theorem 5.19 below. But most of the time
this formula is not too useful; instead, it’s better to understand the Fourier
coefﬁcients of Majn asymptotically as n → ∞.

Let’s begin with a few basic observations. First, Majn is a symmetric func-
tion and hence …Majn(S) only depends on |S| (Exercise 1.30). Second, Majn is
an odd function and hence …Majn(S) = 0 whenever |S| is even (Exercise 1.8).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

122 5. Majority and threshold functions

It remains to determine the Fourier coefﬁcients …Majn(S) for |S| odd. By sym-
metry, …Majn(S)2 = Wk[Majn]/(n
k) for all |S| = k, so if we are content to know
the magnitudes of Majn’s Fourier coefﬁcients, it sufﬁces to determine the
quantities Wk(Majn).

In fact, for each k ∈ N the quantity Wk(Majn) converges to a ﬁxed constant
as n → ∞. We can deduce this using our analysis of the noise stability of
majority. From the previous section we know that for all |ρ| ≤ 1,

lim
n→∞ Stabρ[Majn] = 2
π arcsin ρ = 2
π
 (ρ + 1
6 ρ3 + 3
40 ρ5 + 5
112 ρ7 + · · · ), (5.8)

where we have used the power series for arcsin,

arcsin z = ∑

k odd
 2

k2k
 (k − 1
k−1
2
 )
 · zk, (5.9)

valid for |ρ| ≤ 1 (see Exercise 5.18). Comparing (5.8) with the formula

Stabρ[Majn] = ∑

k≥0 Wk[Majn] · ρk

suggests the following: For each ﬁxed k ∈ N ,

lim
n→∞ Wk[Majn] = [ρk]( 2
π arcsin ρ) =
 { 4
πk2k (k−1
k−1
2
 ) if k odd,

0 if k even. (5.10)

(Here [zk]F(z) denotes the coefﬁcient on zk in power series F(z).) Indeed, we
prove this identity below in Theorem 5.22. The noise stability method that
suggests it can also be made formal (Exercise 5.25).

Identity (5.10) is one way to formulate precisely the statement that the
“Fourier spectrum of Majn converges”. Introducing notation such as “Wk(Maj)”
for the quantity in (5.10), we have the further asymptotics

for k odd, Wk(Maj) ∼ ( 2
π )3/2 k−3/2,

W
>k(Maj) ∼ ( 2
π )3/2 k−1/2 as k → ∞. (5.11)

(See Exercise 5.27.) The estimates (5.11), together with the precise value
W1(Maj) = 2
π , are usually all you need to know about the Fourier coefﬁcients
of majority.

Nevertheless, let’s now compute the Fourier coefﬁcients of Majn exactly.

Theorem 5.19. If |S| is even, then …Majn(S) = 0. If |S| = k is odd,

…Majn(S) = (−1) k−1
2
 ( n−1
2
k−1
2
 )

(n−1
k−1) · 2
2n (n−1
n−1
2
 ).

Proof. The ﬁrst statement holds because Majn is an odd function; henceforth
we assume |S| = k is odd. The trick will be to compute the Fourier expansion of

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.3. The Fourier coefﬁcients of Majority 123

majority’s derivative DnMajn = Halfn−1 : {−1, 1}n−1 → {0, 1}, the 0-1 indicator of
the set of (n − 1)-bit strings with exactly half of their coordinates equal to −1.
By the derivative formula and the fact that Majn is symmetric, …Majn(S) =
áHalfn−1(T) for any T ⊆ [n − 1] with |T| = k − 1. So writing n − 1 = 2m and
k − 1 = 2 j, it sufﬁces to show

áHalf2m([2 j]) = (−1) j (m
j )

(2m
2 j ) · 1
22m (2m
m )
. (5.12)

By the probabilistic deﬁnition of Tρ, for any ρ ∈ [−1, 1] we have

TρHalf2m(1, 1, . . . , 1) = E
x∼Nρ((1,1,...,1))
[Half2m(x)] = Pr[x has m 1’s and m −1’s],

where each coordinate of x is 1 with probability 1
2 + 1
2 ρ. Thus

TρHalf2m(1, 1, . . . , 1) = (2m
m )
( 1
2 + 1
2 ρ)m( 1
2 − 1
2 ρ)m = 1
22m (2m
m )
(1 − ρ2)m. (5.13)

On the other hand, by the Fourier formula for Tρ and the fact that Half2m is
symmetric we have

TρHalf2m(1, 1, . . . , 1) = ∑

U⊆[2m] áHalf2m(U)ρ|U| = 2m∑

i=0
 (2m
i )áHalf2m([i])ρ i. (5.14)

Since we have equality (5.13) = (5.14) between two degree-2m polynomials
of ρ on all of [−1, 1], we can equate coefﬁcients. In particular, for i = 2 j we
have (2m
2 j )áHalf2m([2 j]) = 1
22m (2m
m ) · [ρ2 j](1 − ρ2)m = 1
22m (2m
m ) · (−1) j(m
j )
,

conﬁrming (5.12). □

You are asked to prove the following corollaries in Exercises 5.20, 5.22:

Corollary 5.20. …Majn(S) = (−1) n−1
2 …Majn(T) whenever |S| + |T| = n + 1. Hence
also Wn−k+1[Majn] = k
n−k+1 Wk[Majn].

Corollary 5.21. For any odd k, Wk[Majn] is a strictly decreasing function
of n (for n ≥ k odd).

We can now prove the identity (5.10):

Theorem 5.22. For each ﬁxed odd k,

Wk[Majn] ↘ [ρk]( 2
π arcsin ρ) = 4
πk2k (k−1
k−1
2
 )

as n ≥ k tends to ∞ (through the odd numbers). Further, we have the error
bound
 [ρk]( 2
π arcsin ρ) ≤ Wk[Majn] ≤ (1 + 2k/n) · [ρk]( 2
π arcsin ρ) (5.15)

for all k < n/2. (For k > n/2 you can use Corollary 5.20.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

124 5. Majority and threshold functions

Proof. Corollary 5.21 tells us that Wk[Majn] is decreasing in n; hence we
only need to justify (5.15). Using the formula from Theorem 5.19 we have

Wk[Majn]

[ρk]( 2
π arcsin ρ) =
 (n
k) 4
22n (n−1
n−1
2
 )2 ( n−1
2
k−1
2
 )2∕(n−1
k−1)2

4
πk2k (k−1
k−1
2
 ) = π
2 n · 2k−n(n−k
n−k
2
 ) · 21−n(n−1
n−1
2
 )
,

where the second identity is veriﬁed by expanding all binomial coefﬁcients

to factorials. By Stirling’s approximation we have 2
−m( m
m/2
) ↗ √ 2
πm , meaning
that the ratio of the left side to the right side increases to 1 as m → ∞. Thus

Wk[Majn]

[ρk]( 2
π arcsin ρ) ↗ n
pn − kpn − 1 = (1 − k+1
n + k
n2 )−1/2,

and the right-hand side is at most 1+2k/n for 1 ≤ k ≤ n/2 by Exercise 5.24. □

Finally, we can deduce the asymptotics (5.11) from this theorem (see Ex-
ercise 5.27):

Corollary 5.23. Let k ∈ N be odd and assume n = n(k) ≥ 2k2. Then

Wk(Majn) = ( 2
π )3/2 k−3/2 · (1 ± O(1/k)),

W
>k(Majn) = ( 2
π )3/2 k−1/2 · (1 ± O(1/k)),

and hence the Fourier spectrum of Majn is ϵ-concentrated on degree up to
8
π3 ϵ−2 + Oϵ(1).

5.4. Degree-1 weight

In this section we prove two theorems about the degree-1 Fourier weight of
Boolean functions:
 W1[ f ] = n∑

i=1 ̂f (i)
2.

This important quantity can be given a combinatorial interpretation thanks
to the noise stability formula Stabρ[ f ] = ∑k≥0 ρk · Wk[ f ]:

For f : {−1, 1}n → R , W
1[ f ] = d
dρ Stabρ[ f ] ∣
∣
∣ρ=0 .

Thinking of ∥ f ∥2 as constant and ρ → 0, the noise stability formula implies

Stabρ[ f ] = E[ f ]2 + W
1[ f ]ρ ± O(ρ2),

or equivalently,
 Cov
(x,y)
ρ-correlated

[ f (x), f (y)] = W1[ f ]ρ ± O(ρ2).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.4. Degree-1 weight 125

In other words, for f : {−1, 1}n → {−1, 1} the degree-1 weight quantiﬁes the
extent to which Pr[ f (x) = f (y)] increases when x and y go from being uncor-
related to being slightly correlated.

There is an additional viewpoint if we think of f as the indicator of a
subset A ⊆ {−1, 1}n and its noise sensitivity NSδ[ f ] as a notion of A’s “surface
area”, or “noisy boundary size”. For nearly maximal noise rates – i.e., δ =
1
2 − 1
2 ρ where ρ is small – we have that A’s noisy boundary size is “small” if
and only if W
1[ f ] is “large” (vis-à-vis A’s measure).

Two examples suggest themselves when thinking of subsets of the Ham-
ming cube with small “boundary”: subcubes and Hamming balls.

Proposition 5.24. Let f : F n
2 → {0, 1} be the indicator of a subcube of codimen-
sion k ≥ 1 (e.g., the ANDk function). Then E[ f ] = 2−k, W
1[ f ] = k2−2k.

Proposition 5.25. Fix t ∈ R . Consider the sequence of LTFs f n : {−1, 1}n →
{0, 1} deﬁned by f n(x) = 1 if and only if ∑n
i=1 1pn xi > t. (That is, f n is the

indicator of the Hamming ball {x : ∆(x, (1, . . . , 1)) < n
2 − t
2 pn}.) Then

lim
n→∞ E[ f n] = Φ(t), lim
n→∞ W1[ f n] = φ(t)
2.

You are asked to verify these facts in Exercises 5.29, 5.30. Regarding
Proposition 5.25, it’s natural for φ(t) to arise since W
1[ f n] is related to the in-
ﬂuences of f n, and coordinates are inﬂuential for f n if and only if ∑n
i=1 1pn xi≈ t.
If we write α = limn→∞ E[ f n] then this proposition can be thought of as saying
that W1[ f n] → U (α)
2, where U is deﬁned as follows:

Deﬁnition 5.26. The Gaussian isoperimetric function U : [0, 1] → [0, 1p
2π ] is

deﬁned by U = φ ◦ Φ−1. This function is symmetric about 1/2; i.e., U = φ ◦ Φ−1.

The name of this function will be explained when we study the Gaussian
Isoperimetric Inequality in Chapter 11.4. For now we’ll just use the following
fact:

Proposition 5.27. For α → 0
+, U (α) ∼ α
p
2 ln(1/α).

Proof. Write α = Φ(t), where t → ∞. We use the well-known fact that Φ(t) ∼
φ(t)/t. Thus
 α ∼ 1p
2πt exp(−t2/2) =⇒ t ∼ √
2 ln(1/α),

φ(t) ∼ Φ(t) · t =⇒ U (α) ∼ α · t ∼ α
√
2 ln(1/α). □

Given Propositions 5.24 and 5.25, let’s consider the degree-1 Fourier
weight of subcubes and Hamming balls asymptotically as their “volume”
α = E[ f ] tends to 0. For the subcubes we have W1[ f ] = α
2 log(1/α). For the

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

126 5. Majority and threshold functions

Hamming balls we have W1[ f n] → U (α)2 ∼ 2α
2 ln(1/α). So in both cases we
have an upper bound of O(α
2 log(1/α)).

You should think of this upper bound O(α
2 log(1/α)) as being unusually
small. The obvious a priori upper bound, given that f : {−1, 1}n → {0, 1} has
E[ f ] = α, is W
1[ f ] ≤ Var[ f ] = α(1 − α) ∼ α.

Yet subcubes and Hamming balls have degree-1 weight which is almost quadrat-
ically smaller. In fact the ﬁrst theorem we will show in this section is the
following:

Level-1 Inequality. Let f : {−1, 1}n → {0, 1} have mean E[ f ] = α ≤ 1/2. Then

W1[ f ] ≤ O(α
2 log(1/α)).

(For the case α ≥ 1/2, replace f by 1 − f .)

Thus all small subsets of {−1, 1}n have unusually small W1[ f ]; or equiva-
lently (in some sense), unusually large “noisy boundary”. This is another key
illustration of the idea that the Hamming cube is a “small-set expander”.

Remark 5.28. The bound in the Level-1 Inequality has a sharp form, W
1[ f ] ≤
2α
2 ln(1/α). Thus Hamming balls are in fact the “asymptotic maximizers” of
W
1[ f ] among sets of small volume α. Also, the inequality holds more generally
for f : {−1, 1}n → [−1, 1] with α = E[| f |].

Remark 5.29. The name “Level-1 Inequality” is not completely standard;
e.g., in additive combinatorics the result would be called Chang’s Inequality.
We use this name because we will also generalize to “Level-k Inequalities” in
Chapter 9.5.

So far we considered maximizing degree-1 weight among subsets of the
Hamming cube of a ﬁxed small volume, α. The second theorem in this section
is concerned with what happens when there is no volume constraint. In
this case, maximizing examples tend to have volume α = 1/2; switching the
notation to f : {−1, 1}n → {−1, 1}, this corresponds to f being unbiased (E[ f ] =
0). The unbiased Hamming ball is Majn, which we know has W1[Majn] → 2
π .
This is quite large. But unbiased subcubes are just the dictators χi and their
negations; these have W1[±χi] = 1 which is obviously maximal.

Thus the question of which f : {−1, 1}n → {−1, 1} maximizes W1[ f ] has a
trivial answer. But this answer is arguably unsatisfactory, since dictators
(and their negations) are not “really” functions of n bits. Indeed, when we
studied social choice in Chapter 2 we were motivated to rule out functions f
having a coordinate with unfairly large inﬂuence. And in fact Proposition 2.58
showed that if all ̂f (i) are equal (and hence small) then W
1[ f ] ≤ 2
π + on(1). The
second theorem of this section signiﬁcantly generalizes Proposition 2.58:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.4. Degree-1 weight 127

The 2
π Theorem. Let f : {−1, 1}n → {−1, 1} satisfy | ̂f (i)| ≤ ϵ for all i ∈ [n]. Then

W
1[ f ] ≤ 2
π + O(ϵ). (5.16)

Further, if W1[ f ] ≥ 2
π − ϵ, then f is O(
p
ϵ)-close to the LTF sgn( f =1).

Functions f with | ̂f (i)| ≤ ϵ for all i ∈ [n] are called (ϵ, 1)-regular; see Chap-
ter 6.1. So the 2
π Theorem says (roughly speaking) that within the class of
(ϵ, 1)-regular functions, the maximal degree-1 weight is 2
π , and any function
achieving this is an unbiased LTF. Further, from Theorem 5.17 we know that
all unbiased LTFs which are (ϵ, 1)-regular achieve this.

Remark 5.30. Since we have Stabρ[ f ] ≈ W
1[ f ]ρ and 2
π arcsin ρ ≈ 2
π ρ when ρ
is small, the 2
π Theorem gives the Majority Is Stablest Theorem in the limit
ρ → 0+.

Let’s now discuss how we’ll prove our two theorems about degree-1 weight.
Let f : {−1, 1}n → {0, 1} and α = E[ f ]; we think of α as small for the Level-1
Inequality and α = 1/2 for the 2
π Theorem. By Plancherel, W
1[ f ] = E[ f (x)L(x)],
where L(x) = f =1(x) = ̂f (1)x1 + · · · + ̂f (n)xn.

To upper-bound E[ f (x)L(x)], consider that as x varies the real number L(x)
may be rather large or small, but f (x) is always 0 or 1. Given that f (x) is 1
on only a α fraction of x’s, the “worst case” for E[ f (x)L(x)] would be if f (x)
were 1 precisely on the α fraction of x’s where L(x) is largest. In other words,

W1[ f ] = E[ f (x)L(x)] ≤ E[1{L(x)≥t} · L(x)], (5.17)

where t is chosen so that Pr[L(x) ≥ t] ≈ α. (5.18)

But now we can analyze (5.17) quite effectively using tools such as Hoeffding’s
bound and the CLT, since L(x) is just a linear combination of independent ±1
random bits. In particular L(x) has mean 0 and standard deviation σ =√W1[ f ] so by the CLT it acts like the Gaussian Z ∼ N(0, σ2), at least if we
assume all | ̂f (i)| are small. If we are thinking of α = 1/2, then t = 0 and we get

σ2 = W1[ f ] ≤ E[1{L(x)≥0} · L(x)] ≈ E[1{Z≥0} · Z] = 1p
2π σ;

This implies σ2 ⪅ 1
2π , as claimed in the 2
π Theorem (after adjusting f ’s range
to {−1, 1}). If we are instead thinking of α as small then (5.18) suggest taking
t ∼ σp
2 ln(1/α) so that Pr[Z ≥ t] ≈ α. Then a calculation akin to the one in
Proposition 5.27 implies

W1[ f ] ≤ E[1{L(x)≥t} · L(x)] ≈ α · σ√
2 ln(1/α),

from which the Level-1 Inequality follows. In fact, we don’t even need all | ̂f (i)|
small for this latter analysis; for large t it’s possible to upper-bound (5.17)
using only Hoeffding’s bound:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

128 5. Majority and threshold functions

Lemma 5.31. Let ℓ(x) = a1x1 + · · · + an xn, where ∑i a2
i = 1. Then for any s ≥ 1,

E[1{|ℓ(x)|>s} · |ℓ(x)|] ≤ (2s + 2) exp(− s2
2 ).

Proof. We have

E[1{|ℓ(x)|>s} · |ℓ(x)|] = s Pr[|ℓ(x)| > s] + ∫ ∞

s Pr[|ℓ(x)| > u] du

≤ 2s exp(− s2
2 ) + ∫ ∞

s 2 exp(− u2
2 ) du,

using Hoeffding’s bound. But for s ≥ 1,
∫ ∞

s 2 exp(− u2
2 ) du ≤ ∫ ∞

s u · 2 exp(− u2
2 ) du = 2 exp(− s2
2 ). □

We now give formal proofs of the two theorems, commenting that rather
than L(x) it’s more convenient to work with

ℓ(x) = 1
σ f =1(x) = ̂f (1)
σ x1 + · · · + ̂f (n)
σ xn.

Proof of the Level-1 Inequality. Following Remark 5.28 we let f : {−1, 1}n →
[−1, 1] and α = E[| f |]. We may assume σ = √
W1[ f ] > 0. Writing ℓ = 1
σ f =1 we
have 〈 f , ℓ〉 = 1
σ 〈 f , f =1〉 = 1
σ W1[ f ] = σ and hence

σ = 〈 f , ℓ〉 = E[1{|ℓ(x)|≤s} · f (x)ℓ(x)] + E[1{|ℓ(x)|>s} · f (x)ℓ(x)]

holds for any s ≥ 1. The ﬁrst expectation above is at most E[s| f (x)|] = αs, and
the second is at most (2+2s) exp(−s2/2) ≤ 4s exp(−s2/2) by Lemma 5.31. Hence

σ ≤ αs + 4s exp(−s2/2).

The optimal choice of s is s = (
p
2 + oα(1))
p
ln(1/α), yielding

σ ≤ (p
2 + o(1))α
√
ln(1/α).

Squaring this establishes the claim σ2 ≤ (2 + oα(1))α
2 ln(1/α). □

Proof of the 2
π Theorem. We may assume σ = √
W1[ f ] ≥ 1/2: for the theo-
rem’s ﬁrst statement this is because otherwise there is nothing to prove; for
the theorem’s second statement this is because we may assume ϵ sufﬁciently
small.

We start by proving (5.16). Let ℓ = 1
σ f =1, so ∥ℓ∥2 = 1 and | ̂ℓ(i)| ≤ 2ϵ for all
i ∈ [n]. We have
 σ = 〈 f , ℓ〉 ≤ E[|ℓ|] ≤ √ 2
π + Cϵ (5.19)

for some constant C, where we used Theorem 5.16. Squaring this proves (5.16).
We observe that (5.16) therefore holds even for f : {−1, 1}n → [−1, 1].

Now suppose we also have W1[ f ] ≥ 2
π − ϵ; i.e.,

σ ≥ √ 2
π − ϵ ≥ √ 2
π − 2ϵ.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.4. Degree-1 weight 129

Thus the ﬁrst inequality in (5.19) must be close to tight; speciﬁcally,

(C + 2)ϵ ≥ E[|ℓ|] − 〈 f , ℓ〉 = E[(sgn(ℓ(x)) − f (x)) · ℓ(x)]. (5.20)

By the Berry–Esseen Theorem (and Remark 5.15, Exercise 5.16),

Pr[|ℓ| ≤ Kp
ϵ] ≤ Pr[|N(0, 1)| ≤ Kp
ϵ] + .56 · 2ϵ ≤ 1p
2π · 2Kp
ϵ + 1.12ϵ ≤ 2Kp
ϵ

for any constant K ≥ 1. We therefore have the implication

Pr[ f ̸= sgn(ℓ)] ≥ 3Kp
ϵ =⇒ Pr[ f (x) ̸= sgn(ℓ(x)) ∧ |ℓ(x)| > Kp
ϵ] ≥ Kp
ϵ

=⇒ E[(sgn(ℓ(x)) − f (x)) · ℓ(x)] ≥ Kp
ϵ · 2(Kp
ϵ) = 2K 2ϵ.

This contradicts (5.20) for K = pC + 2, say. Thus Pr[ f ̸= sgn(ℓ)] ≤ 3pC + 2p
ϵ,
completing the proof. □

For an interpolation between these two theorems, see Exercise 5.44.

We conclude this section with an application of the Level-1 Inequality.
First, a quick corollary which we leave for Exercise 5.37:

Corollary 5.32. Let f : {−1, 1}n → {−1, 1} have | E[ f ]| ≥ 1−δ ≥ 0. Then W
1[ f ] ≤
4δ2 log(2/δ).

In Chapter 2.5 we stated the FKN Theorem, which says that if f : {−1, 1}n →
{−1, 1} has W1[ f ] ≥ 1 − δ then it must be O(δ)-close to a dictator or negated-
dictator. The following theorem shows that once the FKN Theorem is proved,
it can be strengthened to give an essentially optimal (Exercise 5.36) closeness
bound:

Theorem 5.33. Suppose the FKN Theorem holds with closeness bound Cδ,
where C ≥ 1 is a universal constant. Then in fact it holds with bound δ/4 + η,
where η = 16C2δ2 max(log(1/Cδ), 1).

Proof. Suppose f : {−1, 1}n → {−1, 1} has W1[ f ] ≥ 1 − δ ≥ 0. By assumption f
is Cδ-close to ±χi for some i ∈ [n], say i = n. Thus we have

| ̂f (n)| ≥ 1 − 2Cδ

and our task is to show that in fact | ̂f (n)| ≥ 1−δ/2−2η. We may assume δ ≤ 1
10C
as otherwise 1 − δ/2 − 2η < 0 (Exercise 5.38) and there is nothing to prove. By
employing the trick from Exercise 2.49 we may also assume E[ f ] = 0.

Consider the restriction of f given by ﬁxing coordinate n to b ∈ {−1, 1};
i.e., f[n−1]|b. For both choices of b we have | E[ f[n−1]|b]| ≥ 1 − 2Cδ and so Corol-
lary 5.32 implies W1[ f[n−1]|b] ≤ 16C2δ2 log(1/Cδ). Thus

16C2δ2 log(1/Cδ) ≥ E
b [W1[ f[n−1]|b]] = ∑

j<n( ̂f ({ j})
2 + ̂f ({ j, n})
2) ≥ ∑

j<n ̂f ( j)
2,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

130 5. Majority and threshold functions

by Corollary 3.22. It follows that

̂f (n)
2 = W
1[ f ] − ∑

j<n ̂f ( j)2 ≥ 1 − δ − 16C2δ2 log(1/Cδ),

and the proof is completed by the fact that

1 − δ − 16C2δ2 log(1/Cδ) ≥ (1 − δ/2 − 2η)2

when δ ≤ 1
10C (Exercise 5.38). □

5.5. Highlight: Peres’s Theorem and uniform noise stability

Theorem 5.17 says that if f is an unbiased linear threshold function f (x) =
sgn(a1x1 + · · · + an xn) in which all ai’s are “small”, then the noise stability
Stabρ[ f ] is at least (roughly) 2
π arcsin ρ. Rephrasing in terms of noise sen-
sitivity, this means NSδ[ f ] is at most (roughly) 2
π p
δ + O(δ3/2) (see the state-
ment of Theorem 2.45). On the other hand, if some ai were particularly large
then f would be pushed in the direction of the dictator function χi, which has
NSδ[χi] = δ ≪ p
δ. This observation suggests that all unbiased LTFs f should
have NSδ[ f ] ≤ O(p
δ). The unbiasedness assumption also seems inessential,
since biasing a function should tend to decrease its noise sensitivity.

Indeed, the idea here is correct, as was shown by Peres in 1999:

Peres’s Theorem. Let f : {−1, 1}n → {−1, 1} be any linear threshold function.
Then NSδ[ f ] ≤ O(
p
δ).

Pleasantly, the proof is quite simple and uses no heavy tools like the
Central Limit Theorem. Before getting to it, let’s make some remarks. First,
Peres’s Theorem shows that the class of all linear threshold functions is what’s
called uniformly noise-stable.

Deﬁnition 5.34. Let B be a class of Boolean-valued functions. We say that
B is uniformly noise-stable if there exists ϵ : [0, 1/2] → [0, 1] with ϵ(δ) → 0 as
δ → 0
+ such that NSδ[ f ] ≤ ϵ(δ) holds for all f ∈ B.

This deﬁnition is only interesting for inﬁnite classes B. (Any class con-
taining functions of only ﬁnitely many input lengths is vacuously uniformly
noise-stable; see Exercise 5.34.) By Proposition 5.6 we see that functions
in a uniformly noise-stable class have “almost all of their Fourier weight at
constant degree”; i.e., for all ϵ > 0 there is a k ∈ N such that W>k[ f ] ≤ ϵ for
all f ∈ B. In particular, from Corollary 3.34 we get that if B is a uniformly
noise-stable class then its restriction to n-input functions is learnable from
random examples to any constant error in poly(n) time.

Let’s make these observations more concrete in the context of linear
threshold functions. Peres’s Theorem immediately gives that LTFs have their
Fourier spectrum ϵ-concentrated up to degree O(1/ϵ2) (Proposition 3.3) and

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.5. Highlight: Peres’s Theorem and uniform noise stability 131

hence the class of LTFs is learnable from random examples with error ϵ in
time nO(1/ϵ2) (Corollary 3.34). The latter result is not too impressive since
it’s been long known that LTFs are learnable in time poly(n, 1/ϵ) using linear
programming. However, the noise sensitivity approach is much more ﬂexible.
Consider the concept class

C = {h = g( f1, . . . , f s) | f1, . . . , f s : {−1, 1}n → {−1, 1} are LTFs}.

For each h : {−1, 1}n → {−1, 1} in C , Peres’s Theorem and a union bound (Ex-
ercise 2.44) imply that NSδ[h] ≤ O(sp
δ). Thus from Corollary 3.34 we get
that the class C is learnable in time nO(s2/ϵ2). This is the only known way of
showing even that an AND of two LTFs is learnable with error .01 in time
poly(n).

The trick for proving Peres’s Theorem is to employ a fairly general tech-
nique for bounding noise sensitivity using average sensitivity (total inﬂuence):

Theorem 5.35. Let δ ∈ (0, 1/2] and let A : N + → R . Let B be a class of Boolean-
valued functions closed under negation and identiﬁcation of input variables.
Suppose that each f ∈ B with domain {−1, 1}n has I[ f ] ≤ A(n). Then each
f ∈ B has NSδ[ f ] ≤ 1
m A(m), where m = ⌊1/δ⌋.

Proof. Fix any f : {−1, 1}n → {−1, 1} from B. Since noise sensitivity is an
increasing function of the noise parameter (see the discussion surround-
ing Proposition 2.51) we may replace δ by 1/m. Thus our task is to upper-
bound NS1/m[ f ] = Pr[ f (x) ̸= f (y)] where x ∼ {−1, 1}n is uniformly random and
y ∈ {−1, 1}n is formed from x by negating each bit independently with proba-
bility 1/m. The rough idea of the proof is that this is equivalent to randomly
partitioning x’s bits into m parts and then negating a randomly chosen part.

More precisely, let z ∈ {−1, 1}n and let π : [n] → [m] be a partition of [n]
into m parts. Deﬁne

g z,π : {−1, 1}m → {−1, 1}, g z,π(w) = f (z ◦ wπ),

where ◦ denotes entry-wise multiplication and wπ = (wπ(1), . . . , wπ(n)) ∈ {−1, 1}n.
Since g z,π is derived from f by negating and identifying input variables it
follows that g z,π ∈ B. So by assumption g z,π has total inﬂuence I[g z,π] ≤ A(m)
and hence average inﬂuence EEE [g z,π] ≤ 1
m A(m) (see Exercise 2.43(a)).

Now suppose z ∼ {−1, 1}n and π : [n] → [m] are chosen uniformly at ran-
dom. We certainly have
 E
z,π
[EEE [g z,π]] ≤ 1
m A(m).

To complete the proof we will show that the left-hand side above is precisely
NS1/m[ f ]. Recall that in the experiment for average inﬂuence EEE [g] we choose

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

132 5. Majority and threshold functions

w ∼ {−1, 1}m and j ∼ [m] uniformly at random and check if g(w) ̸= g(w⊕ j).
Thus

E
z,π
[EEE [g z,π]] = Pr
z,π,w, j[g z,π(w) ̸= g z,π(w⊕ j)] = Pr
w,π, j,z[ f (z ◦ wπ) ̸= f (z ◦ (w⊕ j)
π)].

It is not hard to see that the joint distribution of z ◦ wπ, z ◦(w⊕ j)
π is the same
as that of x, y. To be precise, deﬁne J = π
−1( j), distributed as a random
subset of [n] in which each coordinate is included with probability 1/m, and
deﬁne λ ∈ {−1, 1}n by λi = −1 if and only if i ∈ J. Then

Pr
w,π, j,z[ f (z ◦ wπ) ̸= f (z ◦ (w⊕ j)π)] = Pr
w,π, j,z[ f (z ◦ wπ) ̸= f (z ◦ wπ ◦ λ)].

But for every outcome of w, π, j (and hence J, λ), we may replace z with
z ◦ wπ since they have the same distribution, namely uniform on {−1, 1}n.
Then the above becomes

Pr
w,π, j,z[ f (z) ̸= f (z ◦ λ)] = NS1/m[ f ],

as claimed. □

Peres’s Theorem is now a simple corollary of Theorem 5.35.

Proof of Peres’s Theorem. Let B be the class of all linear threshold func-
tions. This class is indeed closed under negating and identifying variables.
Since each linear threshold function on m bits is unate (i.e., monotone up to
negation of some input coordinates, see Exercises 2.5, 2.6), its total inﬂuence
is at most pm (see Exercise 2.23). Applying Theorem 5.35 we get that for any
LTF f and any δ ∈ (0, 1/2],

NSδ[ f ] ≤ 1
m pm = 1/
pm (for m = ⌊1/δ⌋)

≤ O(p
δ). □

Remark 5.36. Our proof of Peres’s Theorem attains the upper bound √
1/⌊1/δ⌋.
This is at most p
3/2
p
δ for all δ ∈ (0, 1/2] and it’s also p
δ + O(δ3/2) for small δ.
To further improve the constant we can use Theorem 2.33 in place of Exer-
cise 2.23; it implies that all unate m-bit functions have total inﬂuence at mostp
2/πpm + O(m−1/2). This lets us obtain the bound NSδ[ f ] ≤ p
2/πp
δ + O(δ3/2)
for all LTF f .

Recall from Theorem 2.45 that NSδ[Majn] ∼ 2
π p
δ for large n. Thus the
constant p
2/π in the bound from Remark 5.36 is fairly close to optimal. It
seems quite likely that majority’s 2
π is the correct constant here. There is
still slack in Peres’s proof because the random functions g z,π arising in Theo-
rem 5.35 are unlikely to be majorities, even if f is. The most elegant possible
result in this direction would be to prove the following conjecture of Benjamini,
Kalai, and Schramm:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.5. Highlight: Peres’s Theorem and uniform noise stability 133

Majority Is Least Stable Conjecture. Let f : {−1, 1}n → {−1, 1} be a linear
threshold function, n odd. Then for all ρ ∈ [0, 1], Stabρ[ f ] ≥ Stabρ[Majn].

(This is a precise statement about majority’s noise stability within the class
of LTFs; the Majority Is Stablest Theorem refers to its noise stability within
the class of small-inﬂuence functions.) However, Sivakanth Gopi and others
found a counterexample to the above conjecture, already for n = 5. A plausible
replacement would be to conjecture that Stabρ[ f ] ≥ 2
π arcsin ρ for all linear
threshold functions f .

A challenging problem in this area is to extend Peres’s Theorem to poly-
nomial threshold functions. Let

P n,k = { f : {−1, 1}n → {−1, 1} | f is a PTF of degree at most k}, P k = ⋃

n P n,k.

Peres’s Theorem shows that the class P 1 (i.e., LTFs) is uniformly noise-stable.
Is the same true of P 2? What about P 100? More quantitatively, what upper
bound can we prove on NSδ[ f ] for f ∈ P k? Since P k is closed under negating
and identifying variables, a natural approach to bounding the noise sensitivity
of PTFs is to again use Theorem 5.35. For example, if we could show that
I[ f ] = o(n) for all f ∈ P k we could conclude that NSδ[ f ] = oδ(1) for all f ∈ P k;
i.e., that P k is uniformly noise-stable. (In fact, the total inﬂuence approach
to bounding noise sensitivity is not just sufﬁcient but is also necessary; see
Exercise 5.40.) More ambitiously, if we could show that I[ f ] ≤ Ok(1)pn for
all f ∈ P n,k then it would follow that NSδ[ f ] ≤ Ok(1)
p
δ for all f ∈ P k, strictly
generalizing Peres’s Theorem. In fact, a conjecture of Gotsman and Linial
dating back to 1990 proposes an even more reﬁned bound:

Gotsman–Linial Conjecture. Let f ∈ P n,k. Then I[ f ] ≤ Ok(1)pn. More
strongly, I[ f ] ≤ O(k)
pn. Most strongly, the f ∈ P n,k of maximal total inﬂuence
is the symmetric one f (x) = sgn(p(x1+· · ·+xn)), where p is a degree-k univariate
polynomial which alternates sign on the k + 1 values of x1 + · · · + xn closest to 0.

The strongest form of the Gotsman–Linial Conjecture is true when k = 1,
by Theorem 2.33. However, even for k = 2 there was no progress on the con-
jecture for close to 20 years. At that point two independent works [DHK
+10,
HKM10] showed that every f ∈ P n,k satisﬁes both I[ f ] ≤ O(n1−1/2k ) and
I[ f ] ≤ 2O(k)n1−1/O(k). The former (essentially weaker) bound has the advan-
tage of an elementary proof; see Exercise 5.45. It also sufﬁces to show that P k,
the class of degree-k PTFs, is indeed uniformly noise-stable. This gives a nice
kind of converse to Proposition 5.6, which showed that every function in a
uniformly noise-stable class is close to being a constant-degree PTF.

The latest progress on the Gotsman–Linial Conjecture is the following
theorem of Kane [Kan12], which comes quite close to proving it:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

134 5. Majority and threshold functions

Theorem 5.37. Every f ∈ P n,k satisﬁes I[ f ] ≤ pn · (2k log n)
O(k log k). It follows
(via Theorem 5.35) that for a ﬁxed k ∈ N +, every f ∈ P k satisﬁes NSδ[ f ] ≤p
δ · polylog(1/δ).

5.6. Exercises and notes

5.1 (a) Suppose f : {−1, 1}n → {−1, 1} is an LTF. Show that it can be expressed
as f (x) = sgn(a0 + a1x1 + · · · an xn) where the ai’s are integers. (Hint:
First obtain rational ai’s by a perturbation.)
(b) Show also that a degree-d PTF has a representation in which all of
the degree-d polynomial’s coefﬁcients are integers.

5.2 Let f (x) = sgn(a0 + a1x1 + · · · an xn) be an LTF.
(a) Show that if a0 = 0, then E[ f ] = 0. (Hint: Show that f is in fact an
odd function.)
(b) Show that if a0 ≥ 0, then E[ f ] ≥ 0. Show that the converse need not
hold.
(c) Suppose g : {−1, 1}n → {−1, 1} is an LTF with E[g] = 0. Show that g
can be represented as g(x) = sgn(c1x1 + · · · + cn xn).

5.3 Suppose f (x) = sgn(a0 + a1x1 + · · · an xn) is an LTF with |a1| ≥ |a2| ≥ · · · ≥
|an|. Show that Inf1[ f ] ≥ Inf2[ f ] ≥ · · · ≥ Infn[ f ]. (Hint: Why does it sufﬁce
to prove this for n = 2?)

5.4 (a) Show that the number of functions f : {−1, 1}n → {−1, 1} that are LTFs
is at most 2n2+O(n). (Hint: Chow’s Theorem.)
(b) More generally, show that the number of functions f : {−1, 1}n →
{−1, 1} that are degree-k PTFs is at most 2nk+1+O(n).

5.5 (a) Suppose ℓ : {−1, 1}n → R is deﬁned by ℓ(x) = a0 + a1x1 + · · · + an xn.
Deﬁne ̃ℓ : {−1, 1}n+1 → R by ̃ℓ(x0, . . . , xn) = a0x0 + a1x1 + · · · an xn. Show
that ∥ ̃ℓ∥1 = ∥ℓ∥1 and ∥ ̃ℓ∥
2
2 = ∥ℓ∥
2
2.
(b) Complete the proof of Theorem 5.2.

5.6 Let f : {−1, 1}n → {−1, 1} be an unbiased linear threshold function. Show
that Infi[ f ] ≥ 1p
2n for some i ∈ [n], improving the KKL Theorem for LTFs.

5.7 Consider the following “correlation distillation” problem (cf. Exercise 2.56).
For each i ∈ [n] there is a number ρ i ∈ [−1, 1] and an independent se-
quence of pairs of ρ i-correlated bits, (a(1)
i , b(1)
i ), (a(2)
i , b(2)
i ), (a(3)
i , b(3)
i ), etc.
Party A on Earth has access to the stream of n-bit strings a(1), a(2),
a(3), . . . and a party B on Venus has access to the stream b(1), b(2), b(3), . . . .
Neither party knows the numbers ρ1, . . . , ρn. The goal is for B to estimate
these correlations. To assist in this, A can send a small number of bits
to B. A reasonable strategy is for A to send f (a(1)), f (a(2)), f (a(3)), . . . to B,
where f : {−1, 1}n → {−1, 1} is some Boolean function. Using this informa-
tion B can try to estimate E[ f (a)bi] for each i.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.6. Exercises and notes 135

(a) Show that E[ f (a)bi] = ̂f (i)ρ i.
(b) This motivates choosing an f for which all ̂f (i) are large. If we also
insist all ̂f (i) be equal, show that majority functions f maximize this
common value.

5.8 For n ≥ 2, let f : {−1, 1}n → {−1, 1} be a randomly chosen function (as in
Exercise 1.7). Show that ˆ∥ f ˆ∥∞ ≤ 2pn2−n/2 except with probability at
most 2
−n.

5.9 Prove Theorem 5.8.

5.10 (a) Give as simple a proof as you can that the parity function χ[n] : {−1, 1}n →
{−1, 1} is not a PTF of degree n − 1.
(b) Show that if f : {−1, 1}n → {−1, 1} is not ±χ[n], then it is a PTF of
degree n − 1. (Hint: Consider f ≤n−1.)

5.11 For each k ∈ N +, show that there is a degree-k PTF f with W
≤k[ f ] < 2
1−k.

5.12 In this exercise you will show that threshold-of-parities circuits can be
effectively simulated by threshold-of-threshold circuits, but not the con-
verse.
(a) Let f : {−1, 1}n → {−1, 1} be a symmetric function. Show that f is
computable as the sum of at most 2n LTFs, plus a constant.
(b) Deduce that if f : {−1, 1}n → {−1, 1} is computable by a size-s threshold-
of-parities circuit, then it is also computable by a size-2ns threshold-
of-thresholds circuit.
(c) Show that the complete quadratic function CQn : F n
2 → {−1, 1} (see Ex-
ercise 1.1) is computable by a size-2n threshold-of-thresholds circuit.
(d) Assume n even. Show that any threshold-of-parities circuit for CQn
requires size 2n/2.

5.13 Let f : {−1, 1}n → {−1, 1} be computable by a DNF of size s. Show that
f has a PTF representation of sparsity O(ns3). (Hint: Approximate the
ANDs using Theorem 5.12.) Can you improve this bound to O(ns2)?

5.14 In contrast to the previous exercise, show that there is a function f :
{−1, 1}n → {−1, 1} computable by a depth-3 AC0 circuit (see Chapter 4.5)
but requiring threshold-of-parities circuits of size at least nlog n. (Hint:
Involve the inner product mod 2 function and Exercise 4.12.)

5.15 Let F be a nonempty collection of subsets S ⊆ [n]. For each a ∈ {−1, 1}n,
write 1{a} : {−1, 1}n → {0, 1} for the indicator of {a}, write 1F
{a} : {−1, 1}n → R

for ∑S∈F ̂1{a}(S) χS, and write ψa = 2n
|F | · 1F
{a}.

(a) Show that ψa(a) = 1 and E[ψ2
a] = 1
|F | . Show also that for all x ∈

{−1, 1}n, ψa(x) = ψx(a) and ∑a:a̸=x ψa(x)
2 = 2n
|F | − 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

136 5. Majority and threshold functions

(b) Fix 0 < ϵ < 1 and suppose |F | ≥ (1 − ϵ2
6n )2n. Let f : {−1, 1}n → {−1, 1} be
a random function as in Exercise 1.7. Show that for each x ∈ {−1, 1}n,
except with probability at most 4
−n we have | ∑a:a̸=x f (a)ψa(x)| < ϵ.
(c) Deduce that for all but a 2
−n fraction of functions f : {−1, 1}n → {−1, 1},
there a multilinear polynomial q : {−1, 1}n → R supported on the mono-
mials {χS : S ∈ F } such that ∥ f − q∥∞ < ϵ.
(d) Deduce that all but a 2−n fraction of functions f : {−1, 1}n → {−1, 1}
have PTF representation of degree at most n/2 + O(
√n log n).

5.16 (a) Show that in the Berry–Esseen Theorem we can also conclude

| Pr[S < u] − Pr[Z < u]| ≤ cγ.

(Hint: You’ll need that limδ→0+ Pr[Z ≤ u − δ] = Pr[Z ≤ u].)
(b) Deduce that if I ⊆ R is any interval, we can also conclude

| Pr[S ∈ I] − Pr[Z ∈ I]| ≤ 2cγ.

5.17 Show that the assumptions E[X i] = 0 and ∑n
i=1 Var[X i] = 1 in the Berry–
Esseen Theorem are not restrictive, as follows. Let X 1, . . . , X n be indepen-
dent random variables with ﬁnite means and variances. Let S = ∑n
i=1 X i
and let Z ∼ N(µ, σ2), where µ = ∑n
i=1 E[X i] and σ2 = ∑n
i=1 Var[X i]. Assum-
ing σ2 > 0, show that for all u ∈ R ,

| Pr[S ≤ u] − Pr[Z ≤ u]| ≤ cϵ/σ3,

where
 ϵ = n∑

i=1 ∥X i − E[X i]∥
3
3.

5.18 (a) Use the generalized Binomial Theorem to compute the power series
for (1 − z2)
−1/2, valid for |z| < 1.
(b) Integrate to obtain the power series for arcsin z given in (5.9), valid
for |z| < 1.
(c) Conﬁrm that equality holds also for z = ±1.

5.19 Verify that the random vector ⃗S deﬁned in (5.7) has E[⃗S1] = E[⃗S2] = 0,

E[⃗S2
1] = E[⃗S2
2] = 1, E[⃗S1⃗S2] = ρ; i.e., E[⃗S] = [
0
0
] and Cov[⃗S] = [1 ρ
ρ 1
]
.

5.20 Prove Corollary 5.20.

5.21 Fix n odd. Using Theorem 5.19 show that |…Majn(S)| is a decreasing func-
tion of |S| for odd 1 ≤ |S| ≤ n−1
2 . Deduce (using also Corollary 5.20) that
ˆ∥Majn ˆ∥∞ = Majn({1}) ∼ p
2/πpn .

5.22 Prove Corollary 5.21.

5.23 Prove Theorem 5.18. (Hint: Corollary 5.21.)

5.24 Complete the proof of Theorem 5.22 by showing that (1 − k+1
n + k
n2 )−1/2 ≤
1 + 2k/n for all 1 ≤ k ≤ n/2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.6. Exercises and notes 137

5.25 Using just the facts that Stabρ[Majn] → 2
π arcsin ρ for all ρ ∈ [−1, 1] and
that Stabρ[Majn] = ∑k≥0 Wk[Majn]ρk, deduce that limn→∞ Wk[Majn] →
[ρk]( 2
π arcsin ρ) for all k ∈ N . (Hint: By induction on k, always taking ρ
“small enough”.)

5.26 (a) For 0 ≤ j ≤ m integers, show that ˆ∥Maj
=2 j+1
2m+1 ˆ∥1 = (m
j ) 1
2 j+1 · 2m+1
22m (2m
m )
.

(b) Deduce ˆ∥Maj2m+1 ˆ∥1 = E [ 1
2X +1 ]
· 2m+1
2m (2m
m )
, where X ∼ Binomial(m, 1/2).
(c) Deduce ˆ∥Majn ˆ∥1 ∼ 2p
π 1pn 2n/2.

5.27 (a) Show that for each odd k ∈ N ,
( 2
π )3/2 k−3/2 ≤ [ρk]( 2
π arcsin ρ) ≤ ( 2
π )3/2 k−3/2(1 + O(1/k)).

(Hint: Stirling’s approximation.)
(b) Prove Corollary 5.23. (Hint: For the second statement you’ll need to
approximate the sum ∑
odd j>k ( 2
π )3/2 j−3/2 by an integral.)

5.28 For integer 0 ≤ j ≤ n, deﬁne K j : {−1, 1}n → R by K j(x) = ∑
|S|= j xS. Since
K j is symmetric, the value K j(x) depends only on the number z of −1’s
in x; or equivalently, on ∑n
i=1 xi. Thus we may deﬁne K j : {0, 1, . . . , n} → R
by K j(z) = K j(x) for any x with ∑i xi = n − 2z.
(a) Show that K j(z) can be expressed as a degree- j polynomial in z. It
is called the Kravchuk (or Krawtchouk) polynomial of degree j. (The
dependence on n is usually implicit.)
(b) Show that ∑n
j=0 K j(x) = 2n · 1(1,...,1)(x).

(c) Show for ρ ∈ [−1, 1] that ∑n
j=0 K j(x)ρ j = 2n Pr[y = (1, . . . , 1)], where y =
Nρ(x).
(d) Deduce the generating function identity K j(z) = [ρ j]((1−ρ)z(1+ρ)n−z).

5.29 Prove Proposition 5.24.

5.30 Prove Proposition 5.25 using the Central Limit Theorem. (Hint for W
1[ f n]:
use symmetry to show it equals the square of E[ f n(x) ∑ 1pn xi].)

5.31 Consider the setting of Theorem 5.16. Let S = ∑i ai xi where x ∼ {−1, 1}n,
and let Z ∼ N(0, 1).
(a) Show that Pr[|S| ≥ t], Pr[|Z| ≥ t] ≤ 2 exp(−t2/2) for all t ≥ 0.
(b) Recalling E[|Y |] = ∫ ∞
0 Pr[|Y | ≥ t] dt for any random variable Y , use
the Berry–Esseen Theorem (and Remark 5.15, Exercise 5.16) to show
∣
∣
∣E[|S|] − E[|Z|]
∣
∣
∣ ≤ O(ϵT + exp(−T2/2))

for any T ≥ 1.
(c) Deduce | E[|S|] − p
2/π| ≤ O(ϵ√log(1/ϵ)).
(d) Improve O(ϵ√
log(1/ϵ)) to the bound O(ϵ) stated in Theorem 5.16 by
using the nonuniform Berry–Esseen Theorem, which states that the
bound cγ in the Berry–Esseen Theorem can be improved to Cγ · 1
1+|u|3
for some constant C.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

138 5. Majority and threshold functions

5.32 Consider the sequence of LTFs deﬁned in Proposition 5.25. Show that

lim
n→∞ Stabρ[ f n] = Λρ(µ).

Here µ = Φ(t) and Λρ(µ) is the Gaussian quadrant probability deﬁned
by Λρ(µ) = Pr[z1 > t, z2 > t], where z1, z2 are standard Gaussians with
correlation E[z1 z2] = ρ. Verify also that Λρ(α) = Pr[z1 ≤ t, z2 ≤ t] where
α = Φ(t).

5.33 In this exercise you will complete the justiﬁcation of Theorem 5.17 using
the following multidimensional Berry-Esseen Theorem:

Theorem 5.38. Let X 1, . . . , X n be independent R d-valued random vectors,
each having mean zero. Write S = ∑n
i=1 X i and assume Σ = Cov[S] is
invertible. Let Z ∼ N(0, Σ) be a d-dimensional Gaussian with the same
mean and covariance matrix as S. Then for all convex sets U ⊆ R d,

| Pr[S ∈ U] − Pr[Z ∈ U]| ≤ Cd1/4γ,

where C is a universal constant, γ = ∑n
i=1 E[∥Σ−1/2 X i∥
3
2], and ∥ · ∥2 denotes
the Euclidean norm on R d.

(a) Let Σ = [1 ρ
ρ 1
] where ρ ∈ (−1, 1). Show that

Σ−1 = [
1 −ρ
0 1
 ] [1 0
0 (1 − ρ2)−1
] [ 1 0
−ρ 1
] .

(b) Compute y
⊤Σ−1 y for y = [
±a
±a
] ∈ R 2.

(c) Complete the proof of Theorem 5.17.

5.34 Let B be a class of Boolean-valued functions, all of input length at most n.
Show that NSδ[ f ] ≤ nδ for all f ∈ B and hence B is uniformly noise-stable
(in a sense, vacuously). (Hint: Exercise 2.42.)

5.35 Give a simple proof of the following fact, which is a robust form of the
edge-isoperimetric inequality (for volume 1/2) and a weak form of the
FKN Theorem: If f : {−1, 1}n → {−1, 1} has E[ f ] = 0 and I[ f ] ≤ 1+δ, then f
is O(δ)-close to ±χi for some i ∈ [n]. In fact, you should be able to achieve
δ-closeness (which can be further improved using Theorem 5.33). (Hint:
Upper- and lower-bound ∑i ̂f (i)2 ≤ (maxi | ̂f (i)|)(∑i | ̂f (i)|) using Proposi-
tion 3.2 and Exercise 2.5(a).)

5.36 Show that Theorem 5.33 is essentially optimal by exhibiting functions
f : {−1, 1}n → {−1, 1} with ̂f (1) = 1 − δ/2 and W1[ f ] ≥ 1 − δ + Ω(δ2 log(1/δ)),
for a sequence of δ tending to 0.

5.37 Prove Corollary 5.32.

5.38 Fill in the details of the proof of Theorem 5.33.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.6. Exercises and notes 139

5.39 Show that if f : {−1, 1}n → {−1, 1} is an LTF, then d
dδ NSδ[ f ] ≤ O(1/p
δ).
(Hint: The only fact needed about LTFs is the corollary of Peres’s Theorem
that W≥k[ f ] ≤ O(1/pk) for all k.)

5.40 As discussed in Section 5.5, Theorem 5.35 implies that an upper bound on
the total inﬂuence of degree-k PTFs is sufﬁcient to derive an upper bound
on their noise sensitivity. This exercise asks you to show necessity as well.
More precisely, suppose NSδ[ f ] ≤ ϵ(δ) for all f ∈ P k. Show that I[ f ] ≤
O(ϵ(1/n) · n) for all f ∈ P n,k. Deduce that P k is uniformly noise-stable if
and only if I[ f ] = o(n) for all f ∈ P n,k and that NSδ[ f ] ≤ O(kp
δ) for all f ∈
P k if and only if I[ f ] ≤ O(kpn) for all f ∈ P n,k. (Hint: Exercise 2.43(a).)

5.41 Estimate carefully the asymptotics of I[ f ], where f ∈ PTFn,k is as in the
strongest form of the Gotsman–Linial Conjecture.

5.42 Let A ⊆ {−1, 1}n have cardinality α2n, α ≤ 1/2. Thinking of {−1, 1}n ⊂ R n,
let µA ∈ R n be the center of mass of A. Show that µA is close to the origin
in Euclidean distance: ∥µA∥2 ≤ O(√
log(1/α)).

5.43 Show that the Gaussian isoperimetric function satisﬁes U ′′ = −1/U on
(0, 1). Deduce that U is concave.

5.44 Fix α ∈ (0, 1/2). Let f : {−1, 1}n → [−1, 1] satisfy E[| f |] ≤ α and | ̂f (i)| ≤ ϵ
for all i ∈ [n]. Show that W1[ f ] ≤ U (α)2 + Cϵ, where U is the Gaussian
isoperimetric function and where the constant C may depend on α. (Hint:
You will need the nonuniform Berry–Esseen Theorem from Exercise 5.31.)

5.45 In this exercise you will show by induction on k that Inf[ f ] ≤ 2n1−1/2k for
all degree-k PTFs f : {−1, 1}n → {−1, 1}. The k = 0 case is trivial. So for
k > 0, suppose f = sgn(p) where p : {−1, 1}n → R is a degree-k polynomial
that is never 0.
(a) Show for i ∈ [n] that E[ f (x)xisgn(Di p(x))] = Infi[ f ]. (Hint: First use
the decomposition f = xiDi f + Ei f to reach E[Di f · sgn(Di p)]; then
show that Di f = sgn(Di p) whenever Di f ̸= 0.)
(b) Conclude that I[ f ] ≤ E[| ∑i xisgn(Di p(x))|]. Remark: When k = 2 and
thus each sgn(Di p) is an LTF, it is conjectured that this bound is
still O(
pn).
(c) Apply Cauchy–Schwarz and deduce

I[ f ] ≤ √n + ∑

i̸= j E[xi x jsgn(Di p(x))sgn(D j p(x))].

(d) Use Exercise 2.19 and the AM-GM inequality to obtain

I[ f ] ≤ √n + ∑

i I[sgn(Di p)].

(e) Complete the induction.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

140 5. Majority and threshold functions

(f ) Finally, deduce that the class of degree-k PTFs is uniformly noise-
stable, speciﬁcally, that every degree-k PTF f satisﬁes NSδ[ f ] ≤ 3δ1/2k

for all δ ∈ (0, 1/2]. (Hint: Theorem 5.35.)

Notes. Chow’s Theorem was proved by independently by Chow [Cho61] and
by Tannenbaum [Tan61] in 1961; see also Elgot [Elg61]. The generaliza-
tion to PTFs (Theorem 5.8) is due to Bruck [Bru90], as is Theorem 5.10 and
Exercise 5.12. Theorems 5.2 and 5.9 are from Gotsman and Linial [GL94]
and may be called the Gotsman–Linial Theorems; this work also contains the
Gotsman–Linial Conjecture and Exercise 5.11. Conjecture 5.3 should be con-
sidered folklore. Corollary 5.13 was proved by Bruck and Smolensky [BS92];
they also essentially proved Theorem 5.12 (but see [SB91]). Exercise 5.13
is usually credited to Krause and Pudlák [KP97]. The upper bound in Exer-
cise 5.4 is asymptotically sharp [Zue89]. Exercise 5.15 is from O’Donnell and
Servedio [OS08].

Theorem 2.33 and Proposition 2.58, discussed in Section 5.2, were essen-
tially proved by Titsworth in 1962 [Tit62]; see also [Tit63]. More precisely,
Titsworth solved a version of the problem from Exercise 5.7. His motivation
was in fact the construction of “interplanetary ranging systems” for measuring
deep space distances, e.g., the distance from Earth to Venus. The connection
between ranging systems and Boolean functions was suggested by his advisor,
Solomon Golomb. Titsworth [Tit62] was also the ﬁrst to compute the Fourier
expansion of Majn. His approach involved generating functions and contour
integration. Other approaches have used special properties of binomial co-
efﬁcients [Bra87] or of Kravchuk polynomials [Kal02]. The asymptotics of
Wk[Majn] described in Section 5.3 may have ﬁrst appeared in Kalai [Kal02],
with the error bounds being from O’Donnell [O’D03]. Kravchuk polynomials
were introduced by Kravchuk [Kra29].

The Berry–Esseen Theorem is due independently to Berry [Ber41] and
Esseen [Ess42]. Shevtsova [She13] has the record for the smallest known con-
stant B that works therein: roughly .5514. The nonuniform version described
in Exercise 5.31 is due to Bikelis [Bik66]. The multidimensional version
Theorem 5.38 stated in Exercise 5.33 is due to Bentkus [Ben04]. Sheppard
proved his formula in 1899 [She99]. The results of Theorem 5.18 may have
appeared ﬁrst in O’Donnell [O’D04, O’D03].

The Level-1 Inequality should probably be considered folklore; it was per-
haps ﬁrst published in Talagrand [Tal96] and we have followed his proof.
The ﬁrst half of the 2
π Theorem is from Khot et al. [KKMO07]; the second
half is from Matulef et al. [MORS10]. Theorem 5.33, which improves the
FKN Theorem to achieve “closeness” δ/4, was independently obtained by Jen-
drej, Oleszkiewicz, and Wojtaszczyk [JOW12], as was Exercise 5.36 showing
optimality of this closeness. The closeness achieved in the original proof of

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

5.6. Exercises and notes 141

the FKN Theorem [FKN02] was δ/2; that proof (like ours) relies on having
a separate proof of closeness O(δ). Kindler and Safra [KS02, Kin02] gave
a self-contained proof of the δ/2 bound relying only on the Hoeffding bound.
The content of Exercise 5.35 was communicated to the author by Eric Blais.
The result of Exercise 5.44 is from [KKMO07]; Exercise 5.42 was suggested
by Rocco Servedio.

Peres’s Theorem was published in 2004 [Per04] but was mentioned as
early as 1999 by Benjamini, Kalai, and Schramm [BKS99]. The work [BKS99]
introduced the deﬁnition of uniform noise stability and showed that the class
of all LTFs satisﬁes it; however, their upper bound on the noise sensitivity
of LTFs was O(δ1/4), worse than Peres’s. The proof of Peres’s Theorem that
we presented is a simpliﬁcation due to Parikshit Gopalan and incorporates
an idea of Diakonikolas et al. [DHK
+10, HKM10]. Regarding the total in-
ﬂuence of PTFs, the work of Kane [Kan12] shows that every degree-k PTF
on n variables has I[ f ] ≤ poly(k)n1−1/O(k), which is better than Theorem 5.37
for certain superconstant values of k. Exercise 5.39 was suggested by Nitin
Saurabh.
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 6

Pseudorandomness and
F 2-polynomials

In this chapter we discuss various notions of pseudorandomness for Boolean
functions; by this we mean properties of a ﬁxed Boolean function that are
in some way characteristic of randomly chosen functions. We will see some
deterministic constructions of pseudorandom probability density functions
with small support; these have algorithmic application in the ﬁeld of deran-
domization. Finally, several of the results in the chapter will involve interplay
between the representation of f : {0, 1}n → {0, 1} as a polynomial over the reals
and its representation as a polynomial over F 2.

6.1. Notions of pseudorandomness

The most obvious spectral property of a truly random function f : {−1, 1}n →
{−1, 1} is that all of its Fourier coefﬁcients are very small (as we saw in Exer-
cise 5.8). Let’s switch notation to f : {−1, 1}n → {0, 1}; in this case f (;) will not
be very small but rather very close to 1/2. Generalizing:

Proposition 6.1. Let n > 1 and let f : {−1, 1}n → {0, 1} be a p-biased random
function; i.e., each f (x) is 1 with probability p and 0 with probability 1 − p,
independently for all x ∈ {−1, 1}n. Then except with probability at most 2
−n, all
of the following hold:

|̂f (;) − p| ≤ 2pn2
−n/2, ∀S ̸= ; |̂f (S)| ≤ 2pn2−n/2.

Proof. We have ̂f (S) = ∑x 1
2n xS f (x), where the random variables f (x) are
independent. If S = ;, then the coefﬁcients 1
2n xS sum to 1 and the mean

143

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

144 6. Pseudorandomness and F 2-polynomials

of ̂f (S) is p; otherwise the coefﬁcients sum to 0 and the mean of ̂f (S) is 0.
Either way we may apply the Hoeffding bound to conclude that

Pr[|̂f (S) − E[̂f (S)]| ≥ t] ≤ 2 exp(−t2 · 2n−1)

for any t > 0. Selecting t = 2pn2−n/2, the above bound is 2 exp(−2n) ≤ 4−n.
The result follows by taking a union bound over all S ⊆ [n]. □

This proposition motivates the following basic notion of “pseudorandom-
ness”:

Deﬁnition 6.2. A function f : {−1, 1}n → R is ϵ-regular (sometimes called
ϵ-uniform) if | ̂f (S)| ≤ ϵ for all S ̸= ;.

Remark 6.3. By Exercise 3.9, every function f is ϵ-regular for ϵ = ∥ f ∥1. We
are often concerned with f : {−1, 1}n → [−1, 1], in which case we focus on ϵ ≤ 1.

Example 6.4. Proposition 6.1 states that a random p-biased function is
(2pn2−n/2)-regular with very high probability. A function is 0-regular if and
only if it is constant (even though you might not think of a constant func-
tion as very “random”). If A ⊆ F n
2 is an afﬁne subspace of codimension k
then 1A is 2−k-regular (Proposition 3.12). For n even the inner product
mod 2 function and the complete quadratic function, IPn, CQn : F n
2 → {0, 1},
are 2−n/2−1-regular (Exercise 1.1). On the other hand, the parity functions
χS : {−1, 1}n → {−1, 1} are not ϵ-regular for any ϵ < 1 (except for S = ;). By
Exercise 5.21, Majn is 1pn -regular.

The notion of regularity can be particularly useful for probability density
functions; in this case it is traditional to use an alternate name:

Deﬁnition 6.5. If ϕ : F n
2 → R ≥0 is a probability density which is ϵ-regular,
we call it an ϵ-biased density. Equivalently, ϕ is an ϵ-biased density if and
only if | Ex∼ϕ[χγ(x)]| ≤ ϵ for all γ ∈ ̂F n
2 \ {0}; thus one can think of “ϵ-biased” as
meaning “at most ϵ-biased on subspaces”. Note that the marginal of such a
distribution on any set of coordinates J ⊆ [n] is also ϵ-biased. If ϕ is ϕA =
1A/ E[1A] for some A ⊆ F n
2 we call A an ϵ-biased set.

Example 6.6. For ϕ a probability density we have ∥ϕ∥1 = E[ϕ] = 1, so every
density is 1-biased. The density corresponding to the uniform distribution
on F n
2 , namely ϕ ≡ 1, is the only 0-biased density. Densities corresponding to
the uniform distribution on smaller afﬁne subspaces are “maximally biased”:
if A ⊆ F n
2 is an afﬁne subspace of dimension less than n, then ϕA is not ϵ-
biased for any ϵ < 1 (Proposition 3.12 again). If E = {(0, . . . , 0), (1, . . . , 1)}, then
E is a 1/2-biased set (an easy computation, see also Exercise 1.1(h)).

There is a “combinatorial” property of functions f that is roughly equiv-
alent to ϵ-regularity. Recall from Exercise 1.29 that ˆ∥ f ˆ∥
4
4 has an equivalent

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.1. Notions of pseudorandomness 145

non-Fourier formula: Ex,y,z[ f (x) f (y) f (z) f (x+ y+ z)]. We show (roughly speak-
ing) that f is regular if and only if this expectation is not much bigger than
E[ f ]
4 = Ex,y,z,w[ f (x) f (y) f (z) f (w)]:

Proposition 6.7. Let f : F n
2 → R . Then

(1) If f is ϵ-regular, then ˆ∥ f ˆ∥
4
4 − E[ f ]4 ≤ ϵ2 · Var[ f ].

(2) If f is not ϵ-regular, then ˆ∥ f ˆ∥
4
4 − E[ f ]4 ≥ ϵ4.

Proof. If f is ϵ-regular, then

ˆ∥ f ˆ∥
4
4 − E[ f ]
4 = ∑

S̸=; ̂f (S)4 ≤ max
S̸=; { ̂f (S)
2} · ∑

S̸=; ̂f (S)
2 ≤ ϵ2 · Var[ f ].

On the other hand, if f is not ϵ-regular, then | ̂f (T)| ≥ ϵ for some T ̸= ;; hence
ˆ∥ f ˆ∥
4
4 is at least ̂f (;)
4 + ̂f (T)4 ≥ E[ f ]
4 + ϵ4. □

The condition of ϵ-regularity – that all non-empty-set coefﬁcients are
small – is quite strong. As we saw when investigating the 2
π Theorem in
Chapter 5.4 it’s also interesting to consider f that merely have | ̂f (i)| ≤ ϵ for
all i ∈ [n]; for monotone f this is the same as saying Infi[ f ] ≤ ϵ for i. This
suggests two weaker possible notions of pseudorandomness: having all low-
degree Fourier coefﬁcients small, and having all inﬂuences small. We will
consider both possibilities, starting with the second.

Now a randomly chosen f : {−1, 1}n → {−1, 1} will not have all of its inﬂu-
ences small; in fact as we saw in Exercise 2.12, each Infi[ f ] is 1/2 in expec-
tation. However, for any δ > 0 it will have all of its (1 − δ)-stable inﬂuences
exponentially small (recall Deﬁnition 2.52). In Exercise 6.2 you will show:

Fact 6.8. Fix δ ∈ [0, 1] and let f : {−1, 1}n → {−1, 1} be a randomly chosen
function. Then for any i ∈ [n],

E[Inf
(1−δ)
i [ f ]] = (1 − δ/2)n

2 − δ .

This motivates a very important notion of pseudorandomness in the anal-
ysis of Boolean functions: having all stable-inﬂuences small. Recalling the
discussion surrounding Proposition 2.54, we can also describe this as having
no “notable” coordinates.

Deﬁnition 6.9. We say that f : {−1, 1}n → R has (ϵ, δ)-small stable inﬂuences,
or no (ϵ, δ)-notable coordinates, if Inf
(1−δ)
i [ f ] ≤ ϵ for each i ∈ [n]. This condition
gets stronger as ϵ and δ decrease: when δ = 0, meaning Infi[ f ] ≤ ϵ for all i,
we simply say f has ϵ-small inﬂuences.

Example 6.10. Besides random functions, important examples of Boolean-
valued functions with no notable coordinates are constants, majority, and

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

146 6. Pseudorandomness and F 2-polynomials

large parities. Constant functions are the ultimate in this regard: they have
(0, 0)-small stable inﬂuences. (Indeed, constant functions are the only ones
with 0-small inﬂuences.) The Majn function has 1pn -small inﬂuences. To see
the distinction between inﬂuences and stable inﬂuences, consider the parity
functions χS. Any parity function χS (with S ̸= ;) has at least one coordinate
with maximal inﬂuence, 1. But if |S| is “large” then all of its stable inﬂuences
will be small: We have Inf
(1−δ)
i [χS] equal to (1 − δ)|S|−1 when i ∈ S and equal
to 0 otherwise; i.e., χS has ((1−δ)
|S|−1, δ)-small stable inﬂuences. In particular,
χS has (ϵ, δ)-small stable inﬂuences whenever |S| ≥ ln(e/ϵ)
δ .

The prototypical example of a function f : {−1, 1}n → {−1, 1} that does not
have small stable inﬂuences is an unbiased k-junta. Such a function has
Var[ f ] = 1 and hence from Fact 2.53 the sum of its (1 − δ)-stable inﬂuences is
at least (1 − δ)k−1. Thus Inf(1−δ)
i [ f ] ≥ (1 − δ)k−1/k for at least one i; hence f
does not have ((1 − δ)k/k, δ)-small stable inﬂuences for any δ ∈ (0, 1). A some-
what different example is the function f (x) = x0Majn(x1, . . . , xn), which has
Inf(1−δ)
0 [ f ] ≥ 1 − p
δ; see Exercise 6.5(d).

Let’s return to considering the interesting condition that | ̂f (i)| ≤ ϵ for all
i ∈ [n]. We will call this condition (ϵ, 1)-regularity. It is equivalent to saying
that f ≤1 is ϵ-regular, or that f has at most ϵ “correlation” with every dictator:
|〈 f , ±χi〉| ≤ ϵ for all i. Our third notion of pseudorandomness extends this
condition to higher degrees:

Deﬁnition 6.11. A function f : {−1, 1}n → R is (ϵ, k)-regular if | ̂f (S)| ≤ ϵ for all
0 < |S| ≤ k; equivalently, if f ≤k is ϵ-regular. For k = n (or k = ∞), this condition
coincides with ϵ-regularity. When ϕ : F n
2 → R ≥0 is an (ϵ, k)-regular probability
density, it is more usual to call ϕ (and the associated probability distribution)
(ϵ, k)-wise independent.

Below we give two alternate characterizations of (ϵ, k)-regularity; how-
ever, they are fairly “rough” in the sense that they have exponential losses
on k. This can be acceptable if k is thought of as a constant. The ﬁrst char-
acterization is that f is (ϵ, k)-regular if and only if ﬁxing k input coordinates
changes f ’s mean by at most O(ϵ). The second characterization is the condi-
tion that f has O(ϵ) covariance with every k-junta.

Proposition 6.12. Let f : {−1, 1}n → R and let ϵ ≥ 0, k ∈ N .

(1) If f is (ϵ, k)-regular then any restriction of at most k coordinates changes f ’s
mean by at most 2kϵ.

(2) If f is not (ϵ, k)-regular then some restriction to at most k coordinates
changes f ’s mean by more than ϵ.

Proposition 6.13. Let f : {−1, 1}n → R and let ϵ ≥ 0, k ∈ N .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.1. Notions of pseudorandomness 147

(1) If f is (ϵ, k)-regular, then Cov[ f , h] ≤ ˆ∥hˆ∥1ϵ for any h : {−1, 1}n → R with
deg(h) ≤ k. In particular, Cov[ f , h] ≤ 2k/2ϵ for any k-junta h : {−1, 1}n →
{−1, 1}.

(2) If f is not (ϵ, k)-regular, then Cov[ f , h] > ϵ for some k-junta h : {−1, 1}n →
{−1, 1}.

We will prove Proposition 6.12, leaving the proof of Proposition 6.13 to the
exercises.

Proof of Proposition 6.12. For the ﬁrst statement, suppose f is (ϵ, k)-regular
and let J ⊆ [n], z ∈ {−1, 1}J, where |J| ≤ k. Then the statement holds because

E[ f J|z] = ̂f (;) + ∑

;̸=T⊆J ̂f (T) zT

(Exercise 1.15) and each of the at most 2k terms | ̂f (T) zT | = | ̂f (T)| is at most ϵ.

For the second statement, suppose that | ̂f (J)| > ϵ, where 0 < |J| ≤ k. Then
a given restriction z ∈ {−1, 1}J changes f ’s mean by

h(z) = ∑

;̸=T⊆J ̂f (T) zT .

We need to show that ∥h∥∞ > ϵ, and this follows from

∥h∥∞ = ∥hχJ∥∞ ≥ | E[hχJ]| = |̂h(J)| = | ̂f (J)| > ϵ. □

Taking ϵ = 0 in the above two propositions we obtain:

Corollary 6.14. For f : {−1, 1}n → R , the following are equivalent:

(1) f is (0, k)-regular.

(2) Every restriction of at most k coordinates leaves f ’s mean unchanged.

(3) Cov[ f , h] = 0 for every k-junta h : {−1, 1}n → {−1, 1}.

If f is a probability density, condition (3) is equivalent to Ex∼ f [h(x)] = E[h] for
every k-junta h : {−1, 1}n → {−1, 1}.

For such functions, additional terminology is used:

Deﬁnition 6.15. If f : {−1, 1}n → {−1, 1} is (0, k)-regular, it is also called kth-
order correlation immune. If f is in addition unbiased, then it is called k-
resilient. Finally, if ϕ : F n
2 → R ≥0 is a (0, k)-regular probability density, then
we call ϕ (and the associated probability distribution) k-wise independent.

Example 6.16. Any parity function χS : {−1, 1}n → {−1, 1} with |S| = k + 1
is k-resilient. More generally, so is χS · g for any g : {−1, 1}n → {−1, 1} that
does not depend on the coordinates in S. For a good example of a correlation
immune function that is not resilient, consider h : {−1, 1}
3m → {−1, 1} deﬁned
by h = χ{1,...,2m} ∧ χ{m+1,...,3m}. This h is not unbiased, being True on only a

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

148 6. Pseudorandomness and F 2-polynomials

1/4-fraction of inputs. However, its bias does not change unless at least 2m
input bits are ﬁxed; hence h is (2m − 1)th-order correlation immune.

We conclude this section with Figure 6.1, indicating how our various no-
tions of pseudorandomness compare:

Figure 6.1. Comparing notions of pseudorandomness: arrows go from
stronger notions to (strictly) weaker ones

For precise quantitative statements, counterexamples showing that no other
relationships are possible, and explanations for why these notions essentially
coincide for monotone functions, see Exercise 6.5.

6.2. F 2-polynomials

We began our study of Boolean functions in Chapter 1.2 by considering their
polynomial representations over the real ﬁeld. In this section we take a
brief look at their polynomial representations over the ﬁeld F 2, with False,
True being represented by 0, 1 ∈ F 2 as usual. Note that in the ﬁeld F 2, the
arithmetic operations + and · correspond to logical XOR and logical AND,
respectively.

Example 6.17. Consider the logical parity (XOR) function on n bits, χ[n].
To represent it over the reals (as we have done so far) we encode False,True
by ±1 ∈ R ; then χ[n] : {−1, 1}n → {−1, 1} has the polynomial representation
χ[n](x) = x1x2 · · · xn. Suppose instead we encode False,True by 0, 1 ∈ F 2; then
χ[n] : F n
2 → F 2 has the polynomial representation χ[n](x) = x1 + x2 + · · · + xn.
Notice this polynomial has degree 1, whereas the representation over the
reals has degree n.

In general, let f : F n
2 → F 2 be any Boolean function. Just as in Chapter 1.2
we can ﬁnd a (multilinear) polynomial representation for it by interpolation.
The indicator function 1{a} : F n
2 → F 2 for a ∈ F n
2 can be written as

1{a}(x) = ∏

i:ai=1 xi ∏

i:ai=0
(1 − xi), (6.1)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.2. F 2-polynomials 149

a degree-n multilinear polynomial. (We could have written 1 + xi rather than
1− xi since these are the same in F 2.) Hence f has the multilinear polynomial
expression f (x) = ∑

a∈F n
2 f (a)1{a}(x). (6.2)

After simpliﬁcation, this may be put in the form

f (x) = ∑

S⊆[n] cS xS, (6.3)

where xS = ∏i∈S xi as usual, and each coefﬁcient cS is in F 2. We call (6.3)
the F 2-polynomial representation of f . As an example, if f = χ[3] is the parity
function on 3 bits, its interpolation is

χ[3](x) = (1 − x1)(1 − x2)x3 + (1 − x1)x2(1 − x3) + x1(1 − x2)(1 − x3) + x1x2x3

= x1 + x2 + x3 − 2(x1x2 + x1x3 + x2x3) + 4x1x2x3 (6.4)

= x1 + x2 + x3

as expected. We also have uniqueness of the F 2-polynomial representation;
the quickest way to see this is to note that there are 22n functions F n
2 → F 2
and also 2
2n possible choices for the coefﬁcients cS. Summarizing:

Proposition 6.18. Every f : F n
2 → F 2 has a unique F 2-polynomial represen-
tation as in (6.3).

Example 6.19. The logical AND function ANDn : F n
2 → F 2 has the simple
expansion ANDn(x) = x1x2 · · · xn. The inner product mod 2 function has the
degree-2 expansion IP2n(x1, . . . , xn, y1, . . . , yn) = x1 y1 + x2 y2 + · · · + xn yn.

Since the F 2-polynomial representation is unique we may deﬁne F 2-
degree:

Deﬁnition 6.20. The F 2-degree of a Boolean function f : {False,True}n →
{False,True}, denoted degF 2( f ), is the degree of its F 2-polynomial representa-
tion. We reserve the notation deg( f ) for the degree of f ’s Fourier expansion.

We can also give a formula for the coefﬁcients of the F 2-polynomial repre-
sentation:

Proposition 6.21. Suppose f : F n
2 → F 2 has F 2-polynomial representation
f (x) = ∑S⊆[n] cS xS. Then cS = ∑
supp(x)⊆S f (x).

Corollary 6.22. Let f : {False,True}n → {False,True}. Then degF 2( f ) = n if and
only if f (x) = True for an odd number of inputs x.

The proof of Proposition 6.21 is left for Exercise 6.10; Corollary 6.22 is just the
case S = [n]. You can also directly see that c[n] = ∑x f (x) by observing what
happens with the monomial x1x2 · · · xn in the interpolation (6.1), (6.2).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

150 6. Pseudorandomness and F 2-polynomials

Given a generic Boolean function f : {False,True}n → {False,True} it’s nat-
ural to ask about the relationship between its Fourier expansion (i.e., poly-
nomial representation over R ) and its F 2-polynomial representation. In fact
you can easily derive the F 2-representation from the R -representation. Sup-
pose p(x) is the Fourier expansion of f ; i.e., f ’s R -multilinear representa-
tion when we interpret False, True as ±1 ∈ R . From Exercise 1.9, q(x) =
1
2 − 1
2 p(1 − 2x1, . . . , 1 − 2xn) is the unique R -multilinear representation for f
when we interpret False, True as 0, 1 ∈ R . But we can also obtain q(x) by car-
rying out the interpolation in (6.1), (6.2) over Z . Thus the F 2 representation
of f is obtained simply by reducing q(x)’s (integer) coefﬁcients modulo 2.

We saw an example of this derivation above with χ[3]. The ±1-representation
is x1x2x3. The representation over {0, 1} ∈ Z ⊆ R is 1
2 − 1
2 (1 − 2x1)(1 − 2x2)(1 −
2x3), which when expanded equals (6.4) and has integer coefﬁcients. Finally,
we obtain the F 2 representation x1 +x2 +x3 by reducing the coefﬁcients of (6.4)
modulo 2.

One thing to note about this transformation from Fourier expansion to F 2-
representation is that it can only decrease degree. As noted in Exercise 1.11,
the ﬁrst step, forming q(x) = 1
2 − 1
2 p(1 − 2x1, . . . , 1 − 2xn), does not change the
degree at all (except if p(x) ≡ 1, q(x) ≡ 0). And the second step, reducing q’s
coefﬁcients modulo 2, cannot increase the degree. We conclude:

Proposition 6.23. Let f : {−1, 1}n → {−1, 1}. Then degF 2( f ) ≤ deg( f ).

Here is an interesting consequence of this proposition. Suppose that f :
{−1, 1}n → {−1, 1} is k-resilient; i.e., ̂f (S) = 0 for all |S| ≤ k < n. Let g = χ[n] · f ;
thus ̂g(S) = ̂f ([n] \ S) and hence deg(g) ≤ n − k − 1. From Proposition 6.23
we deduce degF 2(g) ≤ n − k − 1. But if we interpret f , g : F n
2 → F 2, then g =
x1+· · ·+xn+ f and hence degF 2(g) = degF 2( f ) (unless f is parity or its negation).
Thus:

Proposition 6.24. Let f : {−1, 1}n → {−1, 1} be k-resilient, k < n − 1. Then
degF 2( f ) ≤ n − k − 1.

This proposition was shown by Siegenthaler, a cryptographer who was
studying stream ciphers; his motivation is discussed further in the notes in
Section 6.6. More generally, Siegenthaler proved the following result (the
proof does not require Fourier analysis):

Siegenthaler’s Theorem. Proposition 6.24 holds. Further, if f is merely
kth-order correlation immune, then we still have degF 2( f ) ≤ n − k (for k < n).

Proof. Pick any monomial xJ of maximal degree d = degF 2( f ) in f ’s F 2-
polynomial representation; we may assume d > 1 else we are done. Make

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.3. Constructions of various pseudorandom functions 151

an arbitrary restriction to the n − d coordinates outside of J, forming func-
tion g : F J
2 → F 2. The monomial xJ still appears in g’s F 2-polynomial repre-
sentation; thus by Corollary 6.22, g is 1 for an odd number of inputs.

Let us ﬁrst show Proposition 6.24. Assuming f is k-resilient, it is unbi-
ased. But g is 1 for an odd number of inputs so it cannot be unbiased (since
2d−1 is even for d > 1). Thus the restriction changed f ’s bias, and we must
have n − d > k, hence d ≤ n − k − 1.

Suppose now f is merely kth-order correlation immune. Pick an arbi-
trary input coordinate for g and suppose its two possible restrictions give
subfunctions g0 and g1. Since g has an odd number of 1’s, one of g0 has
an odd number of 1’s and the other has an even number. In particular, g0
and g1 have different biases. One of these biases must differ from f ’s. Thus
n − d + 1 > k, hence d ≤ n − k. □

We end this section by mentioning another bound related to correlation
immunity:

Theorem 6.25. Suppose f : {−1, 1}n → {−1, 1} is kth-order correlation immune
but not k-resilient (i.e., E[ f ] ̸= 0). Then k + 1 ≤ 2
3 n.

The proof of this theorem (left to Exercise 6.14) uses the Fourier expan-
sion rather than the F 2-representation. The bounds in both Siegenthaler’s
Theorem and Theorem 6.25 can be sharp in many cases; see Exercise 6.15.

6.3. Constructions of various pseudorandom functions

In this section we give some constructions of Boolean functions with strong
pseudorandomness properties. We begin by discussing bent functions:

Deﬁnition 6.26. A function f : F n
2 → {−1, 1} (with n even) is called bent if
| ̂f (γ)| = 2
−n/2 for all γ ∈ ̂F n
2 .

Bent functions are 2−n/2-regular. If the deﬁnition of ϵ-regularity were
changed so that even | ̂f (0)| needed to be at most ϵ, then bent functions would
be the most regular possible functions. This is because ∑
γ ̂f (γ)
2 = 1 for any f :
F n
2 → {−1, 1} and hence at least one | ̂f (γ)| must be at least 2
−n/2. In particular,
bent functions are those that are maximally distant from the class of afﬁne
functions, {±χγ : γ ∈ ̂F n
2 }.

We have encountered some bent functions already. The canonical example
is the inner product mod 2 function, IPn(x) = χ(x1xn/2+1 +x2xn/2+2 +· · ·+xn/2xn).
(Recall the notation χ(b) = (−1)b.) For n = 2 this is just the AND2 function
1
2 + 1
2 x1 + 1
2 x2 − 1
2 x1x2, which is bent by inspection. For general n, the bentness
is a consequence of the following fact (proved in Exercise 6.16):

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

152 6. Pseudorandomness and F 2-polynomials

Proposition 6.27. Let f : F n
2 → {−1, 1} and g : F n′
2 → {−1, 1} be bent. Then
f ⊕ g : F n+n′
2 → {−1, 1} deﬁned by ( f ⊕ g)(x, x′) = f (x)g(x′) is also bent.

Another example of a bent function is the complete quadratic function
CQn(x) = χ(∑1≤i< j≤n xi x j) from Exercise 1.1. Actually, in some sense it is the
“same” example, as we now explain.

Proposition 6.28. Let f : F n
2 → {−1, 1} be bent. Then ±χγ · f is bent for any

γ ∈ ̂F n
2 , as is f ◦ M for any invertible linear transformation M : F n
2 → F n
2 .

Proof. Multiplying by −1 does not change bentness, and both χγ · f and f ◦ M
have the same Fourier coefﬁcients as f up to a permutation (see Exercise 3.1).
□

We claim that CQn arises from f = IPn as in Proposition 6.28. In the
case n = 4, this is because ∑1≤i< j≤4 xi x j = (x1 + x3)(x2 + x3)+(x1 + x2 + x3)x4 + x3
over F 2; thus

CQ4(x) = IP4(Mx) · χ(0,0,1,0)(x), where M =
 






1 0 1 0
1 1 1 0
0 1 1 0
0 0 0 1






 is invertible.

The general case is left to Exercise 6.20. In fact, every bent f with degF 2( f ) ≤ 2
arises by applying Proposition 6.28 to the inner product mod 2 function; see
Exercise 6.19. There are other large families of bent functions; however,
the problem of classifying all bent functions is open and seems difﬁcult. We
content ourselves by describing one more family:

Proposition 6.29. Let f : F 2n
2 → {−1, 1} be deﬁned by f (x, y) = IP2n(x, y)g(y)
where g : {−1, 1}n → {−1, 1} is arbitrary. Then f is bent.

Proof. We will think of y ∈ ̂F n
2 , so IP2n(x, y) = χy(x). We’ll also write a generic

γ ∈ ̂F 2n
2 as (γ1, γ2). Then indeed

̂f (γ) = E
x,y[χy(x)g(y)χ(γ1,γ2)(x, y)] = E
y
 [g(y)χγ2(y) E
x [χy+γ1(x)]]

= E
y [g(y)χγ2(y)1{y+γ1=0}] = 2−n g(γ1)χγ2(γ1) = ±2
−n. □

We next discuss explicit constructions of small ϵ-biased sets, which are of
considerable use in the ﬁeld of algorithmic derandomization. The most basic
step in a randomized algorithm is drawing a string x ∼ F n
2 from the uniform
distribution; however, this has the “cost” of generating n independent, random
bits. But sometimes it’s not necessary that x precisely have the uniform
distribution; it may sufﬁce that x be drawn from an ϵ-biased density. If we
can deterministically ﬁnd an ϵ-biased (multi-)set A of cardinality, say, 2
ℓ, then

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.3. Constructions of various pseudorandom functions 153

we can generate x ∼ ϕA using just ℓ independent random bits. We will see
some example derandomizations of this nature in Section 6.4; for now we
discuss constructions.

Fix ℓ ∈ N + and recall that there exists a ﬁnite ﬁeld F 2ℓ with exactly 2ℓ

elements. It is easy to ﬁnd an explicit representation for F 2ℓ – a complete
addition and multiplication table, say – in time 2
O(ℓ). (In fact, one can compute
within F 2ℓ even in deterministic poly(ℓ) time.) The ﬁeld elements x ∈ F 2ℓ are
naturally encoded by distinct ℓ-bit vectors; we will write enc : F 2ℓ → F ℓ
2 for
this encoding. The encoding is linear; i.e., it satisﬁes enc(0) = (0, . . . , 0) and
enc(x + y) = enc(x) + enc(y) for all x, y ∈ F 2ℓ.

Theorem 6.30. There is a deterministic algorithm that, given n ≥ 1 and 0 <
ϵ ≤ 1/2, runs in poly(n/ϵ) time and outputs a multiset A ⊆ F n
2 of cardinality at
most 16(n/ϵ)2 with the property that ϕA is an ϵ-biased density.

Proof. It sufﬁces to obtain cardinality (n/ϵ)2 under the assumption that
ϵ = 2−t and n = 2ℓ−t are integer powers of 2. We will describe a probabil-
ity density ϕ on F n
2 by giving a procedure for drawing a string y ∼ ϕ which
uses 2ℓ independent random bits. A will be the multiset of 22ℓ = (n/ϵ)2 possi-
ble outcomes for y. It will be clear that A can be generated in deterministic
polynomial time. The goal will be to show that ϕ is 2
−t-biased.

To draw y ∼ ϕ, ﬁrst choose r, s ∼ F 2ℓ independently and uniformly. This
uses 2ℓ independent random bits. Then deﬁne the ith coordinate of y by

yi = 〈enc(r i), enc(s)〉, i ∈ [n],

where the inner product 〈·, ·〉 takes place in F ℓ
2. Fixing γ ∈ ̂F n
2 \ {0}, we need to
argue that | E[χγ(y)]| ≤ 2−t. Now over F ℓ
2,

〈γ, y〉 = n∑

i=1 γi〈enc(r i), enc(s)〉 = 〈 n∑

i=1 γienc(r i), enc(s)〉 = 〈enc( n∑

i=1 γi r i), enc(s)〉,

where the last step used linearity of enc. Thus

E[χγ(y)] = E[(−1)
〈γ,y〉] = E
r
 [
E
s [(−1)
〈enc(pγ(r)),enc(s)〉]] , (6.5)

where pγ : F 2ℓ → F 2ℓ is the polynomial a 7→ γ1a + γ2a2 + · · · + γnan. This poly-
nomial is of degree at most n, and is nonzero since γ ̸= 0. Hence it has at
most n roots (zeroes) over the ﬁeld F 2ℓ. Whenever r is one of these roots,
enc(pγ(r)) = 0 and the inner expectation in (6.5) is 1. But whenever r is not
a root of pγ we have enc(pγ(r)) ̸= 0 and so the inner expectation is 0. (We are
using Fact 1.7 here.) We deduce that

0 ≤ E[χγ(y)] ≤ Pr[r is a root of pγ] ≤ n

2ℓ = 2−t,

which is stronger than what we need. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

154 6. Pseudorandomness and F 2-polynomials

The bound of O(n/ϵ)2 in this theorem is fairly close to being optimally
small; see Exercise 6.24 and the notes for this chapter.

Another useful tool in derandomization is that of k-wise independent dis-
tributions. Sometimes a randomized algorithm using n independent random
bits will still work assuming only that every subset of k of the bits is indepen-
dent. Thus as with ϵ-biased sets, it’s worthwhile to come up with deterministic
constructions of small sets A ⊂ F n
2 such that the density function ϕA is k-wise
independent (i.e., (0, k)-regular). The best known examples have the addi-
tional pleasant feature that A is a linear subspace of F n
2 ; in this case, k-wise
independence is easy to characterize:

Proposition 6.31. Let H be an m × n matrix over F 2 and let A ≤ F n
2 be the
span of H’s rows. Then ϕA is k-wise independent if and only if any sum of at
most k columns of H is nonzero in F m
2 . (We exclude the “empty” sum.)

Proof. Since ϕA = ∑γ∈A⊥ χγ (Proposition 3.11), ϕA is k-wise independent if
and only if |γ| > k for every γ ∈ A⊥ \ {0}. But γ ∈ A⊥ if and only if Hγ = 0. □

Here is a simple construction of such a matrix with m ∼ k log n:

Theorem 6.32. Let k, ℓ ∈ N + and assume n = 2
ℓ ≥ k. Then for m = (k − 1)ℓ + 1,
there is a matrix H ∈ F m×n
2 such that any sum of at most k columns of H is
nonzero in F m
2 .

Proof. Write α1, . . . , αn for the elements of the ﬁnite ﬁeld F n, and consider
the following matrix H′ ∈ F k×n
n :

H′ =
 








 1 1 · · · 1
α1 α2 · · · αn
α
2
1 α
2
2 · · · α
2
n
... ... . . . ...
αk−1
1 αk−1
2 · · · αk−1
n
 








 .

Any submatrix of H′ formed by choosing k columns is a Vandermonde matrix
and is therefore nonsingular. Hence any subset of k columns of H′ is linearly
independent in F k
n. In particular, any sum of at most k columns of H′ is
nonzero in F k
n. Now form H ∈ F m×n
2 from H′ by replacing each entry αi
j (i > 0)

with enc(αi
j), thought of as a column vector in F ℓ
2. Since enc is a linear map we
may conclude that any sum of at most k columns of H is nonzero in F m
2 . □

Corollary 6.33. There is a deterministic algorithm that, given integers 1 ≤
k ≤ n, runs in poly(nk) time and outputs a subspace A ≤ F n
2 of cardinality at
most 2knk−1 such that ϕA is k-wise independent.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.4. Applications in learning and testing 155

Proof. It sufﬁces to assume n = 2
ℓ is a power of 2 and then obtain cardinality
2nk−1 = 2
(k−1)ℓ+1. In this case, the algorithm constructs H as in Theorem 6.32
and takes A to be the span of its rows. The fact that ϕA is k-wise independent
is immediate from Proposition 6.31. □

For constant k this upper bound of O(nk−1) is close to optimal. It can be
improved to O(n⌊k/2⌋), but there is a lower bound of Ω(n⌊k/2⌋) for constant k;
see Exercises 6.27, 6.28.

We conclude this section by noting that taking an ϵ-biased density within
a k-wise independent subspace yields an (ϵ, k)-wise independent density:

Lemma 6.34. Suppose H ∈ F m×n
2 is such that any sum of at most k columns
of H is nonzero in F m
2 . Let ϕ be an ϵ-biased density on F m
2 . Consider drawing
y ∼ ϕ and setting z = y⊤H ∈ F n
2 . Then the density of z is (ϵ, k)-wise indepen-
dent.

Proof. Suppose γ ∈ ̂F n
2 has 0 < |γ| ≤ k. Then Hγ is nonzero by assumption

and hence | E[χγ(z)]| = | Ey∼ϕ[(−1)y⊤Hγ]| ≤ ϵ since ϕ is ϵ-biased. □

As a consequence, combining the constructions of Theorem 6.30 and The-
orem 6.32 gives an (ϵ, k)-wise independent distribution that can be sampled
from using only O(log k + log log(n) + log(1/ϵ)) independent random bits:

Theorem 6.35. There is a deterministic algorithm that, given integers 1 ≤ k ≤
n and also 0 < ϵ ≤ 1/2, runs in time poly(n/ϵ) and outputs a multiset A ⊆ F n
2 of
cardinality O(k log(n)/ϵ)
2 (a power of 2) such that ϕA is (ϵ, k)-wise independent.

6.4. Applications in learning and testing

In this section we describe some applications of our study of pseudorandom-
ness.

We begin with a notorious open problem from learning theory, that of
learning juntas. Let C = { f : F n
2 → F 2 | f is a k-junta}; we will always assume
that k ≤ O(log n). In the query access model, it is quite easy to learn C exactly
(i.e., with error 0) in poly(n) time (Exercise 3.37(a)). However, in the model of
random examples, it’s not obvious how to learn C more efﬁciently than in the
nk · poly(n) time required by the Low-Degree Algorithm (see Theorem 3.36).
Unfortunately, this is superpolynomial as soon as k > ω(1). The state of
affairs is the same in the case of depth-k decision trees (a superclass of C ),
and is similar in the case of poly(n)-size DNFs and CNFs. Thus if we wish to
learn, say, poly(n)-size decision trees or DNFs from random examples only, a
necessary prerequisite is doing the same for O(log n)-juntas.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

156 6. Pseudorandomness and F 2-polynomials

Whether or not ω(1)-juntas can be learned from random examples in poly-
nomial time is a longstanding open problem. Here we will show a modest
improvement on the nk-time algorithm:

Theorem 6.36. For k ≤ O(log n), the class C = { f : F n
2 → F 2 | f is a k-junta}
can be exactly learned from random examples in time n(3/4)k · poly(n).

(The 3/4 in this theorem can in fact be replaced by ω/(ω + 1), where ω is any
number such that n × n matrices can be multiplied in time O(nω).)

The ﬁrst observation we will use to prove Theorem 6.36 is that to learn k-
juntas, it sufﬁces to be able to identify a single coordinate that is relevant (see
Deﬁnition 2.18). The proof of this is fairly simple and is left for Exercise 6.31:

Lemma 6.37. Theorem 6.36 follows from the existence of a learning algorithm
that, given random examples from a nonconstant k-junta f : F n
2 → F 2, ﬁnds
at least one relevant coordinate for f (with probability at least 1 − δ) in time
n(3/4)k · poly(n) · log(1/δ).

Assume then that we have random example access to a (nonconstant)
k-junta f : F n
2 → F 2. As in the Low-Degree Algorithm we will estimate the
Fourier coefﬁcients ̂f (S) for all 1 ≤ |S| ≤ d, where d ≤ k is a parameter to
be chosen later. Using Proposition 3.30 we can ensure that all estimates
are accurate to within (1/3)2−k, except with probability most δ/2, in time
nd · poly(n) · log(1/δ). (Recall that 2k ≤ poly(n).) Since f is a k-junta, all of
its Fourier coefﬁcients are either 0 or at least 2−k in magnitude; hence we
can exactly identify the sets S for which ̂f (S) ̸= 0. For any such S, all of the
coordinates i ∈ S are relevant for f (Exercise 2.11). So unless ̂f (S) = 0 for all
1 ≤ |S| ≤ d, we can ﬁnd a relevant coordinate for f in time nd · poly(n) · log(1/δ)
(except with probability at most δ/2).

To complete the proof of Theorem 6.36 it remains to handle the case that
̂f (S) = 0 for all 1 ≤ |S| ≤ d; i.e., f is dth-order correlation immune. In this case,
by Siegenthaler’s Theorem we know that degF 2( f ) ≤ k − d. (Note that d < k
since f is not constant.) But there is a learning algorithm running in time
O(n)3ℓ · log(1/δ) that exactly learns any F 2-polynomial of degree at most ℓ
(except with probability at most δ/2). Roughly speaking, the algorithm draws
O(n)
ℓ random examples and then solves an F 2-linear system to determine the
coefﬁcients of the unknown polynomial; see Exercise 6.30 for details. Thus in
time n3(k−d) · poly(n) · log(1/δ) this algorithm will exactly determine f , and in
particular ﬁnd a relevant coordinate.

By choosing d = ⌈ 3
4 k⌉ we balance the running time of the two algorithms.
Regardless of whether f is dth-order correlation immune, at least one of the
two algorithms will ﬁnd a relevant coordinate for f (except with probability
at most δ/2 + δ/2 = δ) in time n(3/4)k · poly(n) · log(1/δ). This completes the proof
of Theorem 6.36.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.4. Applications in learning and testing 157

Our next application of pseudorandomness involves using ϵ-biased dis-
tributions to give a deterministic version of the Goldreich–Levin Algorithm
(and hence the Kushilevitz–Mansour learning algorithm) for functions f with
small ˆ∥ f ˆ∥1. We begin with a basic lemma showing that you can get a good
estimate for the mean of such functions using an ϵ-biased distribution:

Lemma 6.38. If f : {−1, 1}n → R and ϕ : {−1, 1}n → R is an ϵ-biased density,
then ∣
∣
∣
∣ E
x∼ϕ
[ f (x)] − E[ f ]∣
∣
∣
∣ ≤ ˆ∥ f ˆ∥1ϵ.

This lemma follows from Proposition 6.13.(1), but we provide a separate proof:

Proof. By Plancherel,

E
x∼ϕ
[ f (x)] = 〈ϕ, f 〉 = ̂f (;) + ∑

S̸=; ̂ϕ(S) ̂f (S),

and the difference of this from E[ f ] = ̂f (;) is, in absolute value, at most
∑

S̸=; | ̂ϕ(S)| · | ̂f (S)| ≤ ϵ · ∑

S̸=; | ̂f (S)| ≤ ˆ∥ f ˆ∥1ϵ. □

Since ˆ∥ f 2 ˆ∥1 ≤ ˆ∥ f ˆ∥2
1 (Exercise 3.6), we also have the following immediate
corollary:

Corollary 6.39. If f : {−1, 1}n → R and ϕ : {−1, 1}n → R is an ϵ-biased density,
then ∣
∣
∣
∣ E
x∼ϕ
[ f (x)2] − E[ f 2]∣
∣
∣
∣ ≤ ˆ∥ f ˆ∥
2
1ϵ.

We can use the ﬁrst lemma to get a deterministic version of Proposi-
tion 3.30, the learning algorithm that estimates a speciﬁed Fourier coefﬁcient.

Proposition 6.40. There is a deterministic algorithm that, given query access
to a function f : {−1, 1}n → R as well as U ⊆ [n], 0 < ϵ ≤ 1/2, and s ≥ 1, outputs
an estimate ̃f (U) for ̂f (U) satisfying

| ̃f (U) − ̂f (U)| ≤ ϵ,

provided ˆ∥ f ˆ∥1 ≤ s. The running time is poly(n, s, 1/ϵ).

Proof. It sufﬁces to handle the case U = ; because for general U, the algo-
rithm can simulate query access to f ·χU with poly(n) overhead, and …f · χU (;) =
̂f (U). The algorithm will use Theorem 6.30 to construct an (ϵ/s)-biased den-
sity ϕ that is uniform over a (multi-)set of cardinality O(n2s2/ϵ2). By enumer-
ating over this set and using queries to f , it can deterministically output the
estimate ̃f (;) = Ex∼ϕ[ f (x)] in time poly(n, s, 1/ϵ). The error bound now follows
from Lemma 6.38. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

158 6. Pseudorandomness and F 2-polynomials

The other key ingredient needed for the Goldreich–Levin Algorithm was
Proposition 3.40, which let us estimate

WS|J[ f ] = ∑

T⊆J
 ̂f (S ∪ T)2 = E
z∼{−1,1}J[ ̂f J|z(S)
2] (6.6)

for any S ⊆ J ⊆ [n]. Observe that for any z ∈ {−1, 1}J we can use Proposi-
tion 6.40 to deterministically estimate ̂f J|z(S) to accuracy ±ϵ. The reason
is that we can simulate query access to the restricted function ̂f J|z, the
(ϵ/s)-biased density ϕ remains (ϵ/s)-biased on {−1, 1}J, and most importantly
ˆ∥ f J|z ˆ∥1 ≤ ˆ∥ f ˆ∥1 ≤ s by Exercise 3.7. It is not much more difﬁcult to determinis-
tically estimate (6.6):

Proposition 6.41. There is a deterministic algorithm that, given query access
to a function f : {−1, 1}n → {−1, 1} as well as S ⊆ J ⊆ [n], 0 < ϵ ≤ 1/2, and s ≥ 1,
outputs an estimate β for WS|J[ f ] that satisﬁes

|WS|J[ f ] − β| ≤ ϵ,

provided ˆ∥ f ˆ∥1 ≤ s. The running time is poly(n, s, 1/ϵ).

Proof. Recall the notation FS|J f from Deﬁnition 3.20; by (6.6), the algo-

rithm’s task is to estimate Ez∼{−1,1}J [(FS|J f )2(z)]. If ϕ : {−1, 1}J → R ≥0 is an
ϵ
4s2 -biased density, Corollary 6.39 tells us that
∣
∣
∣ E
z∼ϕ
[(FS|J f )
2(z)] − E
z∼{−1,1}J[(FS|J f )
2(z)]∣
∣
∣ ≤ ˆ∥FS|J f ˆ∥
2
1 · ϵ
4s2 ≤ ˆ∥ f ˆ∥
2
1 · ϵ
4s2 ≤ ϵ
4 , (6.7)

where the second inequality is immediate from Proposition 3.21. We now
show the algorithm can approximately compute Ez∼ϕ[(FS|J f )2(z)]. For each

z ∈ {−1, 1}J, the algorithm can use ϕ to deterministically estimate (FS|J f )(z) =
̂f J|z(S) to within ±s · ϵ
4s2 ≤ ϵ
4 in poly(n, s, 1/ϵ) time, just as was described in

the text following (6.6). Since | ̂f J|z(S)| ≤ 1, the square of this estimate is
within, say, 3ϵ
4 of (FS|J f )
2(z). Hence by enumerating over the support of ϕ, the
algorithm can in deterministic poly(n, s, 1/ϵ) time estimate Ez∼ϕ[(FS|J f )2(z)]

to within ± 3ϵ
4 , which by (6.7) gives an estimate to within ±ϵ of the desired
quantity Ez∼{−1,1}J [(FS|J f )2(z)]. □

Propositions 6.40 and 6.41 are the only two ingredients needed for a de-
randomization of the Goldreich–Levin Algorithm. We can therefore state a
derandomized version of its corollary Theorem 3.38 on learning functions with
small Fourier 1-norm:

Theorem 6.42. Let C = { f : {−1, 1}n → {−1, 1} | ˆ∥ f ˆ∥1 ≤ s}. Then C is determin-
istically learnable from queries with error ϵ in time poly(n, s, 1/ϵ).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.4. Applications in learning and testing 159

Since any f : {−1, 1}n → {−1, 1} with sparsity( ̂f ) ≤ s also has ˆ∥ f ˆ∥1 ≤ s, we
may also deduce from Exercise 3.37(c):

Theorem 6.43. Let C = { f : {−1, 1}n → {−1, 1} | sparsity( ̂f ) ≤ 2O(k)}. Then C is
deterministically learnable exactly (0 error) from queries in time poly(n, 2k).

Example functions that fall into the concept classes of these theorems are deci-
sion trees of size at most s, and decision trees of depth at most k, respectively.

We conclude this section by discussing a derandomized version of the
Blum–Luby–Rubinfeld linearity test from Chapter 1.6:

Derandomized BLR Test. Given query access to f : F n
2 → F 2:

(1) Choose x ∼ F n
2 and y ∼ ϕ, where ϕ is an ϵ-biased density.

(2) Query f at x, y, and x + y.

(3) “Accept” if f (x) + f (y) = f (x + y).

Whereas the original BLR Test required exactly 2n independent random
bits, the above derandomized version needs only n + O(log(n/ϵ)). This is very
close to minimum possible; a test using only, say, .99n random bits would only
be able to inspect a 2
−.01n fraction of f ’s values.

If f is F 2-linear then it is still accepted by the Derandomized BLR Test
with probability 1. As for the approximate converse, we’ll have to make a
slight concession: We’ll show that any function accepted with probability
close to 1 must be close to an afﬁne function, i.e., satisfy degF 2( f ) ≤ 1. This
concession is necessary: the function f : F n
2 → F 2 might be 1 everywhere
except on the (tiny) support of ϕ. In that case the acceptance criterion f (x) +
f (y) = f (x + y) will almost always be 1 + 0 = 1; yet f is very far from every
linear function. It is, however, very close to the afﬁne function 1.

Theorem 6.44. Suppose the Derandomized BLR Test accepts f : F n
2 → F 2
with probability 1
2 + 1
2 θ. Then f has correlation at least p
θ2 − ϵ with some

afﬁne g : F n
2 → F 2; i.e., dist( f , g) ≤ 1
2 − 1
2 p
θ2 − ϵ.

Remark 6.45. The bound in this theorem works well both when θ is close to 0
and when θ is close to 1; e.g., for θ = 1 − 2δ we get that if f is accepted with
probability 1 − δ, then f is nearly δ-close to an afﬁne function, provided ϵ ≪ δ.

Proof. As in the analysis of the BLR Test (Theorem 1.30) we encode f ’s
outputs by ±1 ∈ R . Using the ﬁrst few lines of that analysis we see that our
hypothesis is equivalent to

θ ≤ E
x∼F n
2
y∼ϕ [ f (x) f (y) f (x + y)] = E
y∼ϕ
[ f (y) · ( f ∗ f )(y)].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

160 6. Pseudorandomness and F 2-polynomials

By Cauchy–Schwarz,

E
y∼ϕ
[ f (y) · ( f ∗ f )(y)] ≤ √ E
y∼ϕ
[ f (y)2]√ E
y∼ϕ
[( f ∗ f )2(y)] = √ E
y∼ϕ
[( f ∗ f )2(y)],

and hence

θ2 ≤ E
y∼ϕ
[( f ∗ f )
2(y)] ≤ E[( f ∗ f )
2] + ˆ∥ f ∗ f ˆ∥1ϵ = ∑

γ∈ ̂F n
2
 ̂f (γ)
4 + ϵ,

where the inequality is Corollary 6.39 and we used †f ∗ f (γ) = ̂f (γ)2. The
conclusion of the proof is as in the original analysis (cf. Proposition 6.7, Exer-
cise 1.29):
 θ2 − ϵ ≤ ∑

γ∈ ̂F n
2
 ̂f (γ)4 ≤ max
γ∈ ̂F n
2 { ̂f (γ)
2} · ∑

γ∈ ̂F n
2
 ̂f (γ)2 = max
γ∈ ̂F n
2 { ̂f (γ)
2},

and hence there exists γ
∗ such that | ̂f (γ
∗)| ≥ p
θ2 − ϵ. □

6.5. Highlight: Fooling F 2-polynomials

Recall that a density ϕ is said to be ϵ-biased if its correlation with every F 2-
linear function f is at most ϵ in magnitude. In the lingo of pseudorandomness,
one says that ϕ fools the class of F 2-linear functions:

Deﬁnition 6.46. Let ϕ : F n
2 → R ≥0 be a density function and let C be a class
of functions F n
2 → R . We say that ϕ ϵ-fools C if
∣
∣
∣ E
y∼ϕ
[ f (y)] − E
x∼F n
2 [ f (x)]
∣
∣
∣ ≤ ϵ

for all f ∈ C .

Theorem 6.30 implies that using just O(log(n/ϵ)) independent random
bits, one can generate a density that ϵ-fools the class of f : F n
2 → {−1, 1} with
degF 2( f ) ≤ 1. A natural problem in the ﬁeld of derandomization is: How
many independent random bits are needed to generate a density which ϵ-fools
all functions of F 2-degree at most d? A naive hope might be that ϵ-biased
densities automatically fool functions of F 2-degree d > 1. The next example
shows that this hope fails badly, even for d = 2:

Example 6.47. Recall the inner product mod 2 function, IPn : F n
2 → {0, 1},
which has F 2-degree 2. Let ϕ : F n
2 → R ≥0 be the density of the uniform dis-
tribution on the support of IPn. Now IPn is an extremely regular function
(see Example 6.4), and indeed ϕ is a roughly 2−n/2-biased density (see Exer-
cise 6.7). But ϕ is very bad at fooling at least one function of F 2-degree 2,
namely IPn itself:
 E
x∼F n
2 [IPn(x)] ≈ 1/2, E
y∼ϕ
[IPn(y)] = 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.5. Highlight: Fooling F 2-polynomials 161

The problem of using few random bits to fool n-bit, F 2-degree-d functions
was ﬁrst taken up by Luby, Veliˇckovi´c, and Wigderson [LVW93]. They showed
how to generate a fooling distribution using exp(O(√d log(n/d) + log(1/ϵ))) in-
dependent random bits. There was no improvement on this for 14 years, at
which point Bogdanov and Viola [BV07] achieved O(log(n/ϵ)) random bits for
d = 2 and O(log n) + exp(poly(1/ϵ)) random bits for d = 3. In general, they
suggested that F 2-degree-d functions might be fooled by the sum of d inde-
pendent draws from a small-bias distribution. Soon thereafter Lovett [Lov08]
showed that a sum of 2d independent draws from a small-bias distribu-
tion sufﬁces, implying that F 2-degree-d functions can be fooled using just
2O(d) · log(n/ϵ) random bits. More precisely, if ϕ is any ϵ-biased density on F n
2 ,
Lovett showed that
∣
∣
∣ E
y(1),...,y(2d )∼ϕ
[ f (y(1) + · · · + y(2d))] − E
x∼F n
2 [ f (x)]
∣
∣
∣ ≤ O(ϵ1/4d ).

In other words, the 2d-fold convolution ϕ
∗2d density fools functions of F 2-
degree d.

The current state of the art for this problem is Viola’s Theorem [Vio09b],
which shows that the original idea of Bogdanov and Viola [BV07] works:
Summing d independent draws from an ϵ-biased distribution fools F 2-degree-
d polynomials.

Viola’s Theorem. Let ϕ be any ϵ-biased density on F n
2 , 0 ≤ ϵ ≤ 1. Let d ∈ N +

and deﬁne ϵd = 9ϵ1/2d−1. Then the class of all f : F n
2 → {−1, 1} with degF 2( f ) ≤ d
is ϵd-fooled by the d-fold convolution ϕ
∗d; i.e.,
∣
∣
∣ E
y(1),...,y(d)∼ϕ
[ f (y(1) + · · · + y(d))] − E
x∼F n
2 [ f (x)]∣
∣
∣ ≤ 9ϵ1/2d−1.

In light of Theorem 6.30, Viola’s Theorem implies that one can ϵ-fool n-bit
functions of F 2-degree d using only O(d log n) + O(d2d log(1/ϵ)) independent
random bits.

The proof of Viola’s Theorem is an induction on d. To reduce the case
of degree d + 1 to degree d, Viola makes use of a simple concept: directional
derivatives.

Deﬁnition 6.48. Let f : F n
2 → F 2 and let y ∈ F n
2 . The directional derivative
∆y f : F n
2 → F 2 is deﬁned by

∆y f (x) = f (x + y) − f (x).

Over F 2 we may equivalently write ∆y f (x) = f (x + y) + f (x).

As expected, taking a derivative reduces degree by 1:

Fact 6.49. For any f : F n
2 → F 2 and y ∈ F n
2 we have degF 2(∆y f ) ≤ degF 2( f ) − 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

162 6. Pseudorandomness and F 2-polynomials

In fact, we’ll prove a slightly stronger statement:

Proposition 6.50. Let f : F n
2 → F 2 have degF 2( f ) = d and ﬁx y, y′ ∈ F n
2 . Deﬁne
g : F n
2 → F 2 by g(x) = f (x + y) − f (x + y′). Then degF 2(g) ≤ d − 1.

Proof. In passing from the F 2-polynomial representation of f (x) to that
of g(x), each monomial xS of maximal degree d is replaced by (x+ y)S −(x+ y′)S.
Upon expansion the monomials xS cancel, leaving a polynomial of degree at
most d − 1. □

We are now ready to give the proof of Viola’s Theorem.

Proof of Viola’s Theorem. The proof is by induction on d. The d = 1 case is
immediate (even without the factor of 9) because ϕ is ϵ-biased. Assume that
the theorem holds for general d ≥ 1 and let f : F n
2 → {−1, 1} have degF 2( f ) ≤
d + 1. We split into two cases, depending on whether the bias of f is large or
small.

Case 1: E[ f ]2 > ϵd. In this case,
p
ϵd · ∣
∣
∣ E
z∼ϕ∗(d+1)[ f (z)] − E
x∼F n
2 [ f (x)]∣
∣
∣

< | E[ f ]| · ∣
∣
∣ E
z∼ϕ∗(d+1)[ f (z)] − E
x∼F n
2 [ f (x)]∣
∣
∣

= ∣
∣
∣ E
x′∼F n
2 ,z∼ϕ∗(d+1)[ f (x′) f (z)] − E
x′,x∼F n
2 [ f (x′) f (x)]∣
∣
∣

= ∣
∣
∣ E
y∼F n
2 ,z∼ϕ∗(d+1)[ f (z + y) f (z)] − E
y,x∼F n
2 [ f (x + y) f (x)]∣
∣
∣

= ∣
∣
∣ E
y∼F n
2 ,z∼ϕ∗(d+1)[∆y f (z)] − E
y,x∼F n
2 [∆y f (x)]
∣
∣
∣

≤ E
y∼F n
2
 [∣
∣
∣ E
z∼ϕ∗(d+1)[∆y f (z)] − E
x∼F n
2 [∆y f (x)
∣
∣
∣]
.

For each outcome y = y the directional derivative ∆y f has F 2-degree at most d
(Fact 6.49). By induction we know that ϕ
∗d ϵd-fools any such polynomial, and
it follows from Exercise 6.29 that ϕ
∗(d+1) does too. Thus each quantity in the
expectation over y is at most ϵd, and we conclude
∣
∣
∣ E
z∼ϕ∗(d+1)[ f (z)] − E
x∼F n
2 [ f (x)]∣
∣
∣ ≤ ϵd
p
ϵd = p
ϵd = 1
3 ϵd+1 ≤ ϵd+1.

Case 2: E[ f ]2 ≤ ϵd. In this case we want to show that Ew∼ϕ∗(d+1)[ f (w)]2 is
nearly as small. By Cauchy–Schwarz,

E
w∼ϕ∗(d+1)[ f (w)]2 = E
z∼ϕ∗d
[ E
y∼ϕ
[ f (z + y)]]2 ≤ E
z∼ϕ∗d
[ E
y∼ϕ
[ f (z + y)]2]

= E
z∼ϕ∗d
[ E
y,y′∼ϕ
[ f (z + y) f (z + y′)]
] = E
y,y′∼ϕ

[ E
z∼ϕ∗d[ f (z + y) f (z + y′)]]
.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.6. Exercises and notes 163

For each outcome of y = y, y′ = y′, the function f (z + y) f (z + y′) is of F 2-degree
at most d in the variables z, by Proposition 6.50. Hence by induction we have

E
y,y′∼ϕ

[ E
z∼ϕ∗d[ f (z + y) f (z + y′)]
] ≤ E
y,y′∼ϕ

[ E
x∼F n
2 [ f (x + y) f (x + y′)]] + ϵd

= E
x∼F n
2 [(ϕ ∗ f )(x)
2] + ϵd

= ∑

γ∈ ̂F n
2
 ̂ϕ(γ)2 ̂f (γ)
2 + ϵd

≤ ̂f (0)2 + ϵ2 ∑

γ̸=0 ̂f (γ)
2 + ϵd

≤ 2ϵd + ϵ2,

where the last step used the hypothesis of Case 2. We have thus shown

E
w∼ϕ∗(d+1)[ f (w)]2 ≤ 2ϵd + ϵ2 ≤ 3ϵd ≤ 4ϵd,

and hence | E[ f (w)]| ≤ 2p
ϵd. Since we are in Case 2, | E[ f ]| ≤ p
ϵd, and so
∣
∣
∣ E
w∼ϕ∗(d+1)[ f (w)] − E[ f ]∣
∣
∣ ≤ 3p
ϵd = ϵd+1,

as needed. □

We end this section by discussing the tightness of parameters in Viola’s
Theorem. First, if we ignore the error parameter, then the result is sharp: a
counting argument (see [BV07]) shows that the d-fold convolution of ϵ-biased
densities cannot in general fool functions of F 2-degree d + 1. More explicitly,
for any d ∈ N +, ℓ ≥ 2d + 1, Lovett and Tzur [LT09] gave an explicit ℓ
2n -biased
density on F (ℓ+1)n
2 and an explicit function f : F (ℓ+1)n
2 → {−1, 1} of degree d + 1
for which ∣
∣
∣ E
w∼ϕ∗d[ f (w)] − E[ f ]∣
∣
∣ ≥ 1 − 2d
2n .

Regarding the error parameter in Viola’s Theorem, it is not known whether
the quantity ϵ1/2d−1 can be improved, even in the case d = 2. However, ob-
taining even a modest improvement to ϵ1/1.99d (for d as large as log n) would
constitute a major advance since it would imply progress on the notorious
problem of “correlation bounds for polynomials”; see Viola [Vio09a].

6.6. Exercises and notes

6.1 Let f be chosen as in Proposition 6.1. Compute Var[̂f (S)] for each S ⊆ [n].

6.2 Prove Fact 6.8.

6.3 Show that any nonconstant k-junta has Inf(1−δ)
i [ f ] ≥ (1/2−δ/2)k−1/k for at
least one coordinate i.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

164 6. Pseudorandomness and F 2-polynomials

6.4 Let ϕ : F n
2 → R ≥0 be an ϵ-biased density. For each d ∈ N + show that the
d-fold convolution ϕ
∗d is an ϵd-biased density.

6.5 (a) Show that if f : {−1, 1}n → R has ϵ-small inﬂuences, then it is p
ϵ-
regular.
(b) Show that for all even n there exists f : {−1, 1}n → {−1, 1} that is 2
−n/2-
regular but does not have ϵ-small inﬂuences for any ϵ < 1/2.
(c) Show that there is a function f : {−1, 1}n → {−1, 1} with ((1 − δ)n−1, δ)-
small stable inﬂuences that is not ϵ-regular for any ϵ < 1.
(d) Verify that the function f (x) = x0Majn(x1, . . . , xn) from Example 6.10
satisﬁes Inf(1−δ)
0 [ f ] = Stab1−δ[Majn] for δ ∈ (0, 1), and thus does not
have (ϵ, δ)-small stable inﬂuences unless ϵ ≥ 1 − p
δ.
(e) Show that the function f : {−1, 1}n+1 → {−1, 1} from part (d) is 1pn -
regular.
(f ) Suppose f : {−1, 1}n → R has (ϵ, δ)-small stable inﬂuences. Show that
f is (η, k)-regular for η = √
ϵ/(1 − δ)k−1.
(g) Show that f has (ϵ, 1)-small stable inﬂuences if and only if f is (
p
ϵ, 1)-
regular.
(h) Let f : {−1, 1}n → {−1, 1} be monotone. Show that if f is (ϵ, 1)-regular
then f is ϵ-regular and has ϵ-small inﬂuences.

6.6 (a) Let f : {−1, 1}n → R . Let (J, J) be a partition of [n] and let z ∈ {−1, 1}J.
For z ∼ {−1, 1}J uniformly random, give a formula for Varz[E[ f J|z]]
in terms of f ’s Fourier coefﬁcients. (Hint: Direct application of Corol-
lary 3.22.)
(b) Using the above formula and the probabilistic method, give an alter-
nate proof of the second statement of Proposition 6.12.

6.7 Let ϕ : F n
2 → R ≥0 be the density corresponding to the uniform distribution
on the support of IPn : F n
2 → {0, 1}. Show that ϕ is ϵ-biased for ϵ = 2
−n/2/(1−
2
−n/2), but not for smaller ϵ.

6.8 Prove Proposition 6.13.

6.9 Compute the F 2-polynomial representation of the equality function Equn :
{0, 1}n → {0, 1}, deﬁned by Equn(x) = 1 if and only if x1 = x2 = · · · = xn.

6.10 (a) Let f : {0, 1}n → R and let q(x) = ∑S⊆[n] cS xS be the (unique) multilin-
ear polynomial representation of f over R . Show that

cS = ∑

R⊆S(−1)
|S|−|R| f (R),

where we identify R ⊆ [n] with its 0-1 indicator string. This formula
is sometimes called Möbius inversion.
(b) Prove Proposition 6.21.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.6. Exercises and notes 165

6.11 (Cf. Lemma 3.5.) Let f : F n
2 → F 2 be nonzero and suppose degF 2( f ) ≤ k.
Show that Pr[ f (x) ̸= 0] ≥ 2−k. (Hint: As in the similar Exercise 3.4, use
induction on n.)

6.12 Let f : {−1, 1}n → {0, 1}.
(a) Show that degF 2( f ) ≤ log(sparsity( ̂f )). (Hint: You will need Exer-
cise 3.7, Corollary 6.22, and Exercise 1.3.)
(b) Suppose ̂f is 2
−k-granular. Show that degF 2( f ) ≤ k. (This is a stronger
result than part (a), by Exercise 3.32.)

6.13 Let f : {−1, 1}n → {−1, 1} be bent, n > 2. Show that degF 2( f ) ≤ n/2. (Note
that the upper bound n/2 + 1 follows from Exercise 6.12(b).)

6.14 In this exercise you will prove Theorem 6.25.
(a) Suppose p(x) = c0 + cS xS + r(x) is a real multilinear polynomial over
x1, . . . , xn with c0, cS ̸= 0, |S| > 2
3 n, and |T| > 2
3 n for all monomials
xT appearing in r(x). Show that after expansion and multilinear
reduction (meaning x2
i 7→ 1), p(x)
2 contains the term 2c0 cS xS.
(b) Deduce Theorem 6.25.

6.15 In this exercise you will explore the sharpness of Siegenthaler’s Theorem
and Theorem 6.25.
(a) For all n and k < n − 1, ﬁnd an f : {0, 1}n → {0, 1} that is k-resilient and
has degF 2( f ) = n − k − 1.
(b) For all n ≥ 3, ﬁnd an f : {0, 1}n → {0, 1} that is 1st-order correlation
immune and has degF 2( f ) = n − 1.
(c) For all n divisible by 3, ﬁnd a biased f : {0, 1}n → {0, 1} that is ( 2
3 n−1)th-
order correlation immune.

6.16 Prove Proposition 6.27.

6.17 Bent functions come in pairs: Show that if f : F n
2 → {−1, 1} is bent, then
2n/2 ̂f is also a bent function (with domain ̂F n
2 ).

6.18 Extend Proposition 6.29 to show that if π is any permutation on F n
2 , then
f (x, y) = IP2n(x, π(y))g(y) is bent.

6.19 Dickson’s Theorem says the following: Any polynomial p : F n
2 → F 2 of
degree at most 2 can be expressed as

p(x) = ℓ0(x) + k∑

j=1 ℓ j(x)ℓ′
j(x), (6.8)

where ℓ0 is an afﬁne function and ℓ1, ℓ′
1, . . . , ℓk, ℓ′
k are linearly indepen-
dent linear functions. Here k depends only on p and is called the “rank” of
p. Show that for n even, g : F n
2 → {−1, 1} deﬁned by g(x) = χ(p(x)) is bent if
and only if k = n/2, if and only if g arises from IPn as in Proposition 6.28.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

166 6. Pseudorandomness and F 2-polynomials

6.20 Without appealing to Dickson’s Theorem, prove that the complete qua-
dratic x 7→ ∑1≤i< j≤n xi x j can be expressed as in (6.8), with k = ⌊n/2⌋. (Hint:
Induction on n, with different steps depending on the parity of n.)

6.21 Deﬁne mod3 : {−1, 1}n → {0, 1} by mod3(x) = 1 if and only if ∑n
j=1 xi is divis-
ible by 3. Derive the Fourier expansion

mod3(x) = 1
3 + 2
3 (−1/2)n ∑

S⊆[n]
|S| even
(−1)
(|S| mod 4)/2p
3
|S|xS

and conclude that mod3 is 2
3 ( p
3
2 )n-regular. (Hint: Consider ∏n
j=1(− 1
2 +
p
−3
2 )x j.)

6.22 In Theorem 6.30, show that given r, s any ﬁxed bit yi can be obtained in
deterministic poly(ℓ) time.

6.23 (a) Slightly modify the construction in Theorem 6.30 to obtain a (2−t −
2
−ℓ)-biased density. (Hint: Arrange for pγ to have degree at most n −
1.)
(b) Since F 2ℓ is a dimension-ℓ vector space over F 2, it has some basis
v1, . . . , vℓ. Suppose we modify the construction in Theorem 6.30 so that
ϕ is a density on F nℓ
2 , with yi j = 〈enc(v j r i), enc(s)〉 for i ∈ [n], j ∈ [ℓ].
Show that ϕ remains 2
−t-biased.

6.24 Fix ϵ ∈ (0, 1) and n ∈ N . Let A ⊆ F n
2 be a randomly chosen multiset in
which ⌈Cn/ϵ2⌉ elements are included, independently and uniformly. Show
that if C is a large enough constant, then A is ϵ-biased except with proba-
bility at most 2
−n.

6.25 Consider the problem of computing the matrix multiplication C = AB,
where A, B ∈ F n×n
2 . There is an algorithm [LG14] for solving this problem
in time O(nω), where ω < 2.373; however, the algorithm is very compli-
cated. Suppose you are given A, B, and the outcome C′ of running this
algorithm; you want to test that indeed C′ = AB.
(a) Give an algorithm using n random bits and time O(n2) with the fol-
lowing property: If C′ = AB, then the algorithm “accepts” with prob-
ability 1; if C′ ̸= AB, then the algorithm “accepts” with probability at
most 1/2. (Hint: Compute C′x and ABx for a random x ∈ F n
2 .)
(b) Show how to reduce the number of random bits used to O(log n) at the
expense of making the false acceptance probability 2/3, while keeping
the running time O(n2). (You may use the fact that in Theorem 6.30,
the time required to compute y given r and s is n · polylog(ℓ).)

6.26 Simplify the exposition and analysis of Theorem 6.32 and Corollary 6.33
in the case of k = 2, and show that you can take m to be one less (i.e.,
m = ℓ).
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.6. Exercises and notes 167

6.27 Consider the matrix H′ ∈ F k×n
n constructed in Theorem 6.32, and suppose
we delete all rows corresponding to even (nonzero) powers of the α j’s.
Show that H′ retains the property that any sum of at most k columns
of H′ is nonzero in F k
n. (Hint: Prove and use that (
∑ j β j)2 = ∑ j β
2
j for any
sequence of β j ∈ F n.) Deduce that the cardinality of A in Corollary 6.33
can be decreased to 2(2n)
⌊k/2⌋.

6.28 Let A ⊆ {−1, 1}n be a multiset and suppose that the probability density φA
is k-wise independent. In this exercise you will prove the lower bound
|A| ≥ Ω(n⌊k/2⌋) (for k constant).
(a) Suppose F ⊆ 2[n] is a collection of subsets of [n] such that |S ∪ T| ≤ k
for all S, T ∈ F . For each S ∈ F deﬁne χA
S ∈ {−1, 1}
|A| ⊆ R |A| to be the
real vector with entries indexed by A whose ath entry is aS = ∏i∈S ai.
Show that the set of vectors { 1p
|A| χA
S : S ∈ F } is orthonormal and hence

|A| ≥ |F |.
(b) Show that we can ﬁnd F satisfying |F | ≥ ∑k/2
j=0 (n
j) if k is even and

|F | ≥ ∑(k−1)/2
j=0 (n
j) + ( n−1
(k−1)/2
) if k is odd.

6.29 Let C be a class of functions F n
2 → R that is closed under translation; i.e.,
f +z ∈ C whenever f ∈ C and z ∈ F n
2 (recall Deﬁnition 3.24). An example is
the class of functions of F 2-degree at most d. Show that if ψ is a density
that ϵ-fools C , then ψ ∗ ϕ also ϵ-fools C for any density ϕ.

6.30 Fix an integer ℓ ≥ 1. In this exercise you will generalize Exercise 3.43 by
showing how to exactly learn F 2-polynomials of degree at most ℓ.
(a) Fix p : F n
2 → F 2 with degF 2(p) ≤ ℓ and suppose that x(1), . . . , x(m) ∼ F n
2
are drawn uniformly and independently from F n
2 . Assume that m ≥
C · 2ℓ(nℓ + log(1/δ)) for 0 < δ ≤ 1/2 and C a sufﬁciently large constant.
Show that except with probability at most δ, the only q : F n
2 → F 2
with degF 2(q) ≤ ℓ that satisﬁes q(x(i)) = p(x(i)) for all i ∈ [m] is q = p.
(Hint: Exercise 6.11 with q − p.)
(b) Show that the concept class of all polynomials F n
2 → F 2 of degree
at most ℓ can be learned from random examples only, with error 0,
in time O(n)3ℓ. (Remark: As in Exercise 3.43, since the key step is
solving a linear system, the learning algorithm can also be done in
O(n)ωℓ time, assuming matrix multiplication can be done in O(nω)
time.)
(c) Extend this learning algorithm so that in running time O(n)
3ℓ·log(1/δ)
it achieves success probability at least 1 − δ. (Hint: Similar to Exer-
cise 3.40.)

6.31 In this exercise you will prove Lemma 6.37.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

168 6. Pseudorandomness and F 2-polynomials

(a) Give a poly(n, 2k)·log(1/δ)-time learning algorithm that, given random
examples from a k-junta F n
2 → F 2, determines (except with probabil-
ity at most δ) if f is a constant function, and if so, which one.
(b) Given access to random examples from a k-junta f : F n
2 → F 2, let
P ⊆ [n] be a set of relevant coordinates for f and let z ∈ F P
2 . Show
how to obtain M independent random examples from the (k − |P|)-
junta fP|z in time poly(n, 2k) · M · log(1/δ) (except with probability at
most δ).
(c) Complete the proof of Lemma 6.37. (Hint: Build a depth-k decision
tree for f .)

6.32 (a) Improve the bound in Lemma 6.38 to ˆ∥ f ˆ∥1ϵ − | ̂f (;)|ϵ and the bound in
Corollary 6.39 to ˆ∥ f ˆ∥
2
1ϵ − ∥ f ∥
2
2ϵ.
(b) Improve the bound in Theorem 6.44 to p
θ2 − ϵ/
p
1 − ϵ.

6.33 Improve on Theorem 6.44 by a factor of roughly 2 in the case of acceptance
probability near 1. Speciﬁcally, show that if f passes the Derandomized
BLR Test with probability 1 − δ, then there exists γ
∗ ∈ ̂F n
2 with | ̂f (γ
∗)| ≥
p
1 − 2δ − ϵ/
p
1 − ϵ.

6.34 Fix an integer k ∈ N +. Let ( f s)s∈{0,1}k be a collection of functions indexed
by length-k binary sequences, each f s : F n
2 → R . Deﬁne the kth Gowers
“inner product” 〈( f s)s〉U k ∈ R by

〈( f s)s〉U k = E
x,y1,...,yk
 [ ∏

s∈{0,1}k f s(x + ∑

i:si=1 yi)
]
 ,

where the k+1 random vectors x, y1, . . . , yk are independent and uniformly
distributed on F n
2 . Deﬁne the kth Gowers norm of a function f : F n
2 → R
by
 ∥ f ∥U k = 〈( f , f , . . . , f )〉1/2k

U k ,

where ( f , f , . . . , f ) denotes that all 2k functions in the collection equal f .
(You will later verify that 〈( f , f , . . . , f )〉U k is always nonnegative.)
(a) Check that 〈 f0, f1〉U 1 = E[ f0] E[ f1] and therefore ∥ f ∥
2
U 1 = E[ f ]2.
(b) Check that

〈 f00, f10, f01, f11〉U 2 = ∑

γ∈ ̂F n
2
 ̂f00(γ) ̂f10(γ) ̂f01(γ) ̂f11(γ)

and therefore ∥ f ∥
4
U 2 = ˆ∥ f ˆ∥
4
4. (Cf. Exercise 1.29(b).)
(c) Show that

〈( f s)s〉U k = E
y1,...,yk−1
 [
E
x
 [ ∏

s:sk=0 f s(x + ∑

i:si=1 yi)
]
 · E
x′
 [ ∏

s:sk=1 f s(x′ + ∑

i:si=1 yi)

]]
 ,

(6.9)
where x′ is independent of x, y1, . . . , yk−1 and uniformly distributed.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.6. Exercises and notes 169

(d) Show that 〈( f , f , . . . , f )〉U k is always nonnegative, as promised.
(e) Using (6.9) and Cauchy–Schwarz, show that

〈( f s)s〉U k ≤ √
〈( f(s1,...,sk−1,0))S〉U k √〈( f(s1,...,sk−1,1))s〉U k .

(f ) Show that
 〈( f s)s〉U k ≤ ∏

s∈{0,1}k ∥ f s∥U k . (6.10)

(g) Fixing f : F n
2 → R , show that ∥ f ∥U k ≤ ∥ f ∥U k+1. (Hint: Consider
( f s)s∈{0,1}k+1 deﬁned by f s = f if sk+1 = 0 and f s = 1 if sk+1 = 1.)
(h) Show that ∥ · ∥U k satisﬁes the triangle inequality and is therefore a
seminorm. (Hint: First show that

∥ f0 + f1∥
2k

U k = ∑

S⊆{0,1}k〈( f1[s∈S])s∈{0,1}k 〉U k

and then use (6.10).)
(i) Show that ∥·∥U k is in fact a norm for all k ≥ 2; i.e., ∥ f ∥U k = 0 =⇒ f = 0.

Notes. The F 2-polynomial representation of a Boolean function f is often
called its algebraic normal form. It seems to have ﬁrst been explicitly intro-
duced by Zhegalkin in 1927 [Zhe27].

For functions f : Z n → R , the idea of ϵ-regularity as a pseudorandomness
notion dates back to Chung and Graham [CG92], as does the equivalent com-
binatorial condition Proposition 6.7. (In the context of quasirandom graphs,
the ideas date further back to Thomason [Tho87] and to Chung, Graham,
and Wilson [CGW89].) The idea of treating functions with small (stable) in-
ﬂuences as being “generic” has its origins in the work of Kahn, Kalai, and
Linial [KKL88]. The notion was brought to the fore in work on hardness of ap-
proximation – implicitly, by Håstad [Hås96, Hås99], and later more explicitly
by Khot, Kindler, Mossel, and O’Donnell [KKMO07].

The notion of ϵ-biased sets (and also (ϵ, k)-wise independent distributions)
was introduced by Naor and Naor [NN93] (see also the independent work of
Peralta [Per90]). The construction in Theorem 6.30 is due to Alon, Goldre-
ich, Håstad, and Peralta [AGHP92] (as is Exercise 6.23). As noted by Naor
and Naor [NN93], ϵ-biased sets are closely related to error-correcting codes
over F 2; indeed, they are equivalent to linear error-correcting in which all
pairs of codewords have relative distance in [ 1
2 − 1
2 ϵ, 1
2 + 1
2 ϵ]. In particular, the
construction in Theorem 6.30 is the concatenation of the well-known Reed–
Solomon and Hadamard codes (see, e.g., MacWilliams and Sloane [MS77]
for deﬁnitions). The nonconstructive upper bound in Exercise 6.24 is essen-
tially the Gilbert–Varshamov bound and is close to known lower bound of
Ω( n
ϵ2 log(1/ϵ) ) (assuming ϵ ≥ 2−Ω(n)), which follows from the work of McEliece,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

170 6. Pseudorandomness and F 2-polynomials

Rodemich, Rumsey, and Welch [MRRW77] (see [MS77]). Additionally, con-
structive upper bounds of O( n
ϵ3 ) and O( n5/4

ϵ5/2 ) are known using tools from coding
theory; see the work of Ben-Aroya and Ta-Shma [BT09] and Matthews and
Peachey [MP11].

The probabilistic notion of correlation immunity – i.e., condition (2) of
Corollary 6.14 – was ﬁrst introduced by Siegenthaler [Sie84]; we further dis-
cuss his work below. Independently and shortly thereafter, Chor, Friedman,
Goldreich, Håstad, Rudich, and Smolensky [CFG
+85] introduced the deﬁni-
tion of resilience and also connected it to (0, k)-regularity of the Fourier spec-
trum; i.e., they proved Corollary 6.14. (In the cryptography literature, Corol-
lary 6.14 is called the Xiao–Massey Theorem [XM88].) The work [CFG
+85]
also essentially contains Theorem 6.25 and the relevant function from Exam-
ple 6.16; cf. the work of Mossel et al. [MOS04].

The problem of constructing explicit k-wise distributions of small support
arose in different guises in different areas – in the study of orthogonal arrays
(in statistics), error-correcting codes, and algorithmic derandomization. Alon,
Babai, and Itai [ABI85] gave the construction in Theorem 6.32 – in fact, the
stronger one from Exercise 6.27 – based on the analysis of dual BCH codes
in MacWilliams and Sloane [MS77]. The lower bound from Exercise 6.28
is essentially due to Rao [Rao47]; see also independent proofs [CFG
+85,
ABI85].

Siegenthaler’s Theorem dates from 1984 [Sie84]. His motivation was the
study of cryptographic stream ciphers in cryptography. In this application, a
short random sequence of bits (“secret key”) is transformed via some scheme
into a very long sequence of pseudorandom bits (“keystream”), which can then
be used as a one-time pad for encryption. A basic component of most schemes
is a linear feedback shift register (LFSR), which can efﬁciently generate long,
fairly statistically-uniform sequences. However, due to its F 2-linearity, it
suffers from some simple cryptanalytic attacks. An early idea for combating
this is to take n independent LFSR streams and combine them via some
function f : F n
2 → F 2. Effective attacks are possible in such a scheme if f is
correlated with any of its input bits – or indeed (as Siegenthaler pointed out)
any input pair, triple, etc. This led Siegenthaler to deﬁne the probabilistic
notion of correlation-immunity. Although χ[n] is the maximally correlation-
immune function, it is not suitable as a LFSR combining function precisely
because of its F 2-linearity; the same is true of any function of low F 2-degree.
Siegenthaler precisely captured this tradeoff between correlation-immunity
and F 2-degree in his theorem.

Bent functions were named and ﬁrst studied by Rothaus around 1966;
he didn’t publish the notion until 1976, however [Rot76], at which point

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

6.6. Exercises and notes 171

there were already several works on subject, see, e.g., [Dil72]. Bent func-
tions have application in cryptography and coding theory; see, e.g., Carlet’s
survey [Car10]. The basic constructions presented in Section 6.3 are due
to Rothaus; the class of bent functions described in Exercise 6.18 is called
the Maiorana–McFarland family. Dickson’s Theorem is from a 1901 publica-
tion [Dic01, Theorem 199]; see also MacWilliams and Sloane [MS77, Theo-
rem 15.4].

Theorem 6.36 is from Mossel et al. [MOS04]; there is an improved al-
gorithm for learning k-juntas that runs in time roughly n.6024kpoly(n), due
to Gregory Valiant [Val12]. Avrim Blum offers a prize of $1,000 for solv-
ing the case of k = log log n in poly(n) time [Blu03]. Theorem 6.42 is due to
Kushilevitz and Mansour [KM93]. The Derandomized BLR Test and The-
orem 6.44 (and Exercise 6.32) are due to Ben-Sasson, Sudan, Vadhan, and
Wigderson [BSSVW03].

The result of Exercise 6.11 is due to Muller [Mul54a, Theorem 6]; deriving
Exercise 6.30 from it and from Blumer et al. [BEHW87] is folklore. The result
of Exercise 6.12(a) is due to Bernasconi and Codenotti [BC99]; Exercise 6.13
is from MacWilliams and Sloane [MS77]. In Exercise 6.25, part (a) is due
to Freivalds [Fre79] and part (b) to Naor and Naor [NN93]. The Gowers
norm and results of Exercise 6.34 are from Gowers [Gow01]. Our proof of the
second statement in Proposition 6.12 was suggested by Noam Lifshitz.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 7

Property testing,
PCPPs, and CSPs

In this chapter we study several closely intertwined topics: property testing,
probabilistically checkable proofs of proximity (PCPPs), and constraint sat-
isfaction problems (CSPs). All of our work will be centered around the task
of testing whether an unknown Boolean function is a dictator. We begin by
extending the BLR Test to give a 3-query property testing algorithm for the
class of dictator functions. This in turn allows us to give a 3-query testing
algorithm for any property, so long as the right “proof” is provided. We then in-
troduce CSPs, which are in fact identical to string testing algorithms. Finally,
we explain how dictator tests can be translated into computational complex-
ity results for CSPs, and we sketch the proofs of some of Håstad’s optimal
inapproximability results.

7.1. Dictator testing

In Chapter 1.6 we described the BLR property testing algorithm: Given query
access to an unknown function f : {0, 1}n → {0, 1}, this algorithm queries f on a
few random inputs and approximately determines whether f has the property
of being linear over F 2. The ﬁeld of property testing for Boolean functions is
concerned with coming up with similar algorithms for other properties. In
general, a “property” can be any collection C of n-bit Boolean functions; it’s
the same as the notion of “concept class” from learning theory. Indeed, before
running an algorithm to try to learn an unknown f ∈ C , one might ﬁrst run a
property testing algorithm to try to verify that indeed f ∈ C .
 173

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

174 7. Property testing, PCPPs, and CSPs

Let’s encapsulate the key aspects of the BLR linearity test with some
deﬁnitions:

Deﬁnition 7.1. An r-query function testing algorithm for Boolean functions
f : {0, 1}n → {0, 1} is a randomized algorithm that:

• chooses r (or fewer) strings x(1), . . . , x(r) ∈ {0, 1}n according to some prob-
ability distribution;

• queries f (x(1)), . . . , f (x(r));

• based on the outcomes, decides (deterministically) whether to “accept” f .

Deﬁnition 7.2. Let C be a “property” of n-bit Boolean functions, i.e., a collec-
tion of functions {0, 1}n → {0, 1}. We say a function testing algorithm is a local
tester for C (with rejection rate λ > 0) if it satisﬁes the following:

• If f ∈ C , then the tester accepts with probability 1.

• For all 0 ≤ ϵ ≤ 1, if dist( f , C ) > ϵ (in the sense of Deﬁnition 1.29), then
the tester rejects f with probability greater than λ · ϵ.

Equivalently, if the tester accepts f with probability at least 1 − λ · ϵ,
then f is ϵ-close to C ; i.e., ∃g ∈ C such that dist( f , g) ≤ ϵ.

By taking ϵ = 0 in the above deﬁnition you see that any local tester gives
a characterization of C : a function is in C if and only if it is accepted by
the tester with probability 1. But a local tester furthermore gives a “robust”
characterization: Any function accepted with probability close to 1 must be
close to satisfying C .

Example 7.3. By Theorem 1.30, the BLR Test is a 3-query local tester for the
property C = { f : F n
2 → F 2 | f is linear} (with rejection rate 1).

Remark 7.4. To be pedantic, the BLR linearity test is actually a family of
local testers, one for each value of n. This is a common scenario: We will
usually be interested in testing natural families of properties (C n)n∈N +, where
C n contains functions {0, 1}n → {0, 1}. In this case we need to describe a family
of testers, one for each n. Generally, these testers will “act the same” for
all values of n and will have the property that the rejection rate λ > 0 is a
universal constant independent of n.

There are a number of standard variations of Deﬁnition 7.2 that one could
consider. One variation is to allow for an adaptive testing algorithm, mean-
ing that the algorithm can decide how to generate x(t) based on the query
outcomes f (x(1)), . . . , f (x(t−1)). However, in this book we will only consider
nonadaptive testing. Another variation is to relax the requirement that ϵ-far
functions be rejected with probability Ω(ϵ); one could allow for smaller rates
such as Ω(ϵ2), or Ω(ϵ/ log n). For simplicity, we will stick with the strict de-
mand that the rejection probability be linear in ϵ. Finally, the most common

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.1. Dictator testing 175

deﬁnition of property testing allows the number of queries to be a function
r(ϵ) of ϵ but requires that any function ϵ-far from C be rejected with proba-
bility at least 1/2. This is easier to achieve than satisfying Deﬁnition 7.2; see
Exercise 7.1.

So far we have seen that the property of being linear over F 2 is locally
testable. We’ll now spend some time discussing local testability of an even sim-
pler property, the property of being a dictator. In other words, we’ll consider
the property
 D = { f : {0, 1}n → {0, 1} | f (x) = xi for some i ∈ [n]}.

As we will see, dictatorship is in some ways the most important property to
be able to test.

We begin with a reminder: Even though D is a subclass of the linear
functions and we have a local tester for linearity, this doesn’t mean we auto-
matically have a local tester for dictatorship. (This is in contrast to learning
theory, where a learning algorithm for a concept class automatically works for
any subclass.) The reason is that the non-dictator linear functions – i.e., χS
for |S| ̸= 1 – are at distance 1
2 from D but are accepted by any linearity test
with probability 1.

Still, we could use a linearity test as a ﬁrst component of a test for dicta-
torship; this essentially reduces the problem to testing if an unknown lin-
ear function is a dictator. Historically, the ﬁrst local testers for dictator-
ship [BGS95, PRS01] worked this way; after testing linearity, they chose
x, y ∼ {0, 1}n uniformly and independently, set z = x ∧ y (the bitwise logical
AND), and tested whether f (z) = f (x) ∧ f (y). The idea is that the only parity
functions that satisfy this “AND test” with probability 1 are the dictators (and
the constant 0). The analysis of the test takes a bit of work; see Exercise 7.8
for details.

Here we will describe a simpler dictatorship test. Recall we have already
seen an important result that characterizes dictatorship: Arrow’s Theorem,
from Chapter 2.5. Furthermore the robust version of Arrow’s Theorem (Corol-
lary 2.60) involves evaluating a 3-candidate Condorcet election under the
impartial culture assumption, and this is the same as querying the election
rule f on 3 correlated random inputs. This suggests a dictatorship testing
component we call the “NAE Test”:

NAE Test. Given query access to f : {−1, 1}n → {−1, 1}:

• Choose x, y, z ∈ {−1, 1}n by letting each triple (xi, yi, zi) be drawn inde-
pendently and uniformly at random from among the 6 triples satisfying
the not-all-equal predicate NAE3 : {−1, 1}
3 → {0, 1}.

• Query f at x, y, z.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

176 7. Property testing, PCPPs, and CSPs

• Accept if NAE3( f (x), f (y), f (z)) is satisﬁed.

The NAE Test by itself is almost a 3-query local tester for the property of
being a dictator. Certainly if f is a dictator then the NAE Test accepts with
probability 1. Furthermore, in Chapter 2.5 we proved:

Theorem 7.5 (Restatement of Corollary 2.60). If the NAE Test accepts f with
probability 1 − ϵ, then W
1[ f ] ≥ 1 − 9
2 ϵ, and hence f is O(ϵ)-close to ±χi for some
i ∈ [n] by the FKN Theorem.

There are two slightly unsatisfactory aspects to this theorem. First, it
gives a local tester only for the property of being a dictator or a negated-
dictator. Second, though the deduction W1[ f ] ≥ 1 − 9
2 ϵ requires only simple
Fourier analysis, the conclusion that f is close to a (negated-)dictator relies
on the non-trivial FKN Theorem. Fortunately we can ﬁx both issues simply
by adding in the BLR Test:

Theorem 7.6. Given query access to f : {−1, 1}n → {−1, 1}, perform both the
BLR Test and the NAE Test. This is a 6-query local tester for the property of
being a dictator (with rejection rate .1).

Proof. The ﬁrst condition in Deﬁnition 7.2 is easy to check: If f : {−1, 1}n →
{−1, 1} is a dictator, then both tests accept f with probability 1. To check
the second condition, ﬁx 0 ≤ ϵ ≤ 1 and assume the overall test accepts f with
probability at least 1−.1ϵ. Our goal is to show that f is ϵ-close to some dictator.

Since the overall test accepts with probability at least 1−.1ϵ, both the BLR
and the NAE tests must individually accept f with probability at least 1 − .1ϵ.
By the analysis of the NAE Test we deduce that W1[ f ] ≥ 1 − 9
2 · .1ϵ = 1 − .45ϵ.
By the analysis of the BLR Test (Theorem 1.30) we deduce that f is .1ϵ-close
to some parity function; i.e., ̂f (S∗) ≥ 1 − .2ϵ for some S∗ ⊆ [n]. Now if |S∗| ̸= 1
we would have

1 = n∑

k=0 Wk[ f ] ≥ (1 − .45ϵ) + (1 − .2ϵ)
2 ≥ 2 − .85ϵ > 1,

a contradiction. Thus we must have |S∗| = 1 and hence f is .1ϵ-close to the
dictator χS∗, stronger than what we need. □

As you can see, we haven’t been particularly careful about obtaining the
largest possible rejection rate. Instead, we will be more interested in using as
few queries as possible (while maintaining some positive constant rejection
rate). Indeed we now show a small trick which lets us reduce our 6-query
local tester for dictatorship down to a 3-query one. This is best possible since
dictatorship can’t be locally tested with 2 queries (see Exercise 7.6).

BLR+NAE Test. Given query access to f : {−1, 1}n → {−1, 1}:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.1. Dictator testing 177

• With probability 1/2, perform the BLR Test on f .

• With probability 1/2, perform the NAE Test on f .

Theorem 7.7. The BLR+NAE Test is a 3-query local tester for the property of
being a dictator (with rejection rate .05).

Proof. The only observation we need to make is that if the BLR+NAE Test
accepts with probability 1−.05ϵ then both the BLR and the NAE tests individ-
ually must accept f with probability at least 1 − .1ϵ. The result then follows
from the analysis of Theorem 7.6. □

Remark 7.8. In general, this trick lets us take the maximum of the query
complexities when we combine tests, rather than the sum (at the expense
of worsening the rejection rate). Suppose we wish to combine t = O(1) dif-
ferent testing algorithms, where the ith tester uses r i queries. We make
an overall test that performs each subtest with probability 1/t. This gives a
max(r1, . . . , r t)-query testing algorithm with the following guarantee: If the
overall test accepts f with probability 1 − λ
t ϵ then every subtest must accept f
with probability at least 1 − λϵ.

We can now explain one reason why dictatorship is a particularly impor-
tant property to be able to test locally. Given the BLR Test for linear functions
it still took us a little thought to ﬁnd a local test for the subclass D of dictators.
But given our dictatorship test, it’s easy to give a 3-query local tester for any
subclass of D. (On a related note, Exercise 7.15 asks you to give a 3-query
local tester for any afﬁne subspace of the linear functions.)

Theorem 7.9. Let S be any subclass of n-bit dictators; i.e., let S ⊆ [n] and let

S = {χi : {0, 1}n → {0, 1} | i ∈ S}.

Then there is a 3-query local tester for S (with rejection rate .01).

Proof. Let 1S ∈ {0, 1}n denote the indicator string for the subset S. Given
access to f : {0, 1}n → {0, 1}, the test is as follows:

• With probability 1/2, perform the BLR+NAE Test on f .

• With probability 1/2, apply the local correcting routine of Proposition 1.31
to f on string 1S; accept if and only if the output value is 1.

This test always makes either 2 or 3 queries, and whenever f ∈ S it accepts
with probability 1. Now let 0 ≤ ϵ ≤ 1 and suppose the test accepts f with
probability at least 1 − λϵ, where λ = .01. Our goal will be to show that f is
ϵ-close to a dictator χi with i ∈ S.

Since the overall test accepts f with probability at least 1−λϵ, the BLR+NAE
Test must accept f with probability at least 1 − 2λϵ. By Theorem 7.7 we may

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

178 7. Property testing, PCPPs, and CSPs

deduce that f is 40λϵ-close to some dictator χi. Our goal is to show that i ∈ S;
this will complete the proof because 40λϵ ≤ ϵ (by our choice of λ = .01).

So suppose by way of contradiction that i ̸∈ S; i.e., χi(1S) = 0. Since f is
40λϵ-close to the parity function χi, Proposition 1.31 tells us that

Pr[locally correcting f on input 1S produces the output χi(1S) = 0] ≥ 1−80λϵ.

On the other hand, since the overall test accepts f with probability at least
1− λϵ, the second subtest must accept f with probability at least 1− 2λϵ. This
means

Pr[locally correcting f on input 1S produces the output 0] ≤ 2λϵ.

But this is a contradiction, since 2λϵ < 1 − 80λϵ for all 0 ≤ ϵ ≤ 1 (by our choice
of λ = .01). Hence i ∈ S as desired. □

7.2. Probabilistically Checkable Proofs of Proximity

In the previous section we saw that every subproperty of the dictatorship
property has a 3-query local tester. In this section we will show that any
property whatsoever has a 3-query local tester – if an appropriate “proof ” is
provided.

To make sense of this statement let’s ﬁrst generalize the setting in which
we study property testing. Deﬁnitions 7.1 and 7.2 are concerned with testing a
Boolean function f : {0, 1}n → {0, 1} by querying its values on various inputs. If
we think of f ’s truth table as a Boolean string of length N = 2n, then a testing
algorithm simply queries various coordinates of this string. It makes sense to
generalize to the notion of testing properties of N-bit strings, for any length N.
Here a property C will just be a collection C ⊆ {0, 1}N of strings, and we’ll be
concerned with relative Hamming distance dist(w, w′) = 1
N ∆(w, w′) between
strings. For simplicity, we’ll begin to write n instead of N.

Deﬁnition 7.10. An r-query string testing algorithm for strings w ∈ {0, 1}n is
a randomized algorithm that:

• chooses r (or fewer) indices i1, . . . , ir ∈ [n] according to some probability
distribution;

• queries wi1, . . . , wir ;

• based on the outcomes, decides (deterministically) whether to “accept” w.

We may also generalize this deﬁnition to testing strings w ∈ Ωn over ﬁnite
alphabets Ω of cardinality larger than 2.

Deﬁnition 7.11. Let C ⊆ {0, 1}n be a “property” of n-bit Boolean strings. We
say a string testing algorithm is a local tester for C (with rejection rate λ > 0)
if it satisﬁes the following:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.2. Probabilistically Checkable Proofs of Proximity 179

• If w ∈ C , then the tester accepts with probability 1.

• For all 0 ≤ ϵ ≤ 1, if dist(w, C ) > ϵ, then the tester rejects w with probabil-
ity greater than λ · ϵ.

Equivalently, if the tester accepts w with probability at least 1 − λ · ϵ,
then w is ϵ-close to C ; i.e., ∃w′ ∈ C such that dist(w, w′) ≤ ϵ.

Example 7.12. Let Z = {(0, 0, . . . , 0)} ⊆ {0, 1}n be the property of being the all-
zeroes string. Then the following is a 1-query local tester for Z (with rejection
rate 1): Pick a uniformly random index i and accept if wi = 0.

Let E = {(0, 0, . . . , 0), (1, 1, . . . , 1)} ⊆ {0, 1}n be the property of having all co-
ordinates equal. Then the following is a 2-query local tester for E : Pick two
independent and uniformly random indices i and j and accept if wi = w j.
In Exercise 7.4 you are asked to show that if dist(w, E ) = ϵ, then this tester
rejects w with probability 1
2 − 1
2 (1 − 2ϵ)
2 ≥ ϵ.

Let O = {w ∈ F n
2 : w has an odd number of 1’s}. This property does not
have a local tester making few queries. In fact, in Exercise 7.5 you are
asked to show that any local tester for O must make the maximum number
of queries, n.

As the last example shows, not every property has a local tester making a
small number of queries; indeed, most properties of n-bit strings do not. This
is rather too bad: Imagine that for any large n and any complicated property
C ⊆ {0, 1}n there were an O(1)-query local tester. Then if anyone supplied you
with a string w claiming it satisﬁed C , you wouldn’t have to laboriously check
this yourself, nor would you have to trust the supplier; you could simply spot-
check w in a constant number of coordinates and become convinced that w is
(close to being) in C .

But what if, in addition to w ∈ {0, 1}n, you could require the supplier to
give you some additional side information Π ∈ {0, 1}
ℓ about w so as to assist
you in testing that w ∈ C ? One can think of Π as a kind of “proof ” that w
satisﬁes C . In this case it’s possible that you can spot-check w and Π together
in a constant number of coordinates and become convinced that w is (close
to being) in C – all without having to “trust” the supplier of the string w
and the purported proof Π. These ideas lead to the notion of probabilistically
checkable proofs of proximity (PCPPs).

Deﬁnition 7.13. Let C ⊆ {0, 1}n be a property of n-bit Boolean strings and
let ℓ ∈ N . We say that C has an r-query, length-ℓ probabilistically checkable
proof of proximity (PCPP) system (with rejection rate λ > 0) when the following
holds: There exists an r-query testing algorithm T for (n + ℓ)-bit strings,
thought of as pairs w ∈ {0, 1}n and Π ∈ {0, 1}
ℓ, such that:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

180 7. Property testing, PCPPs, and CSPs

• (“Completeness.”) If w ∈ C , then there exists a “proof ” Π ∈ {0, 1}
ℓ such
that T accepts with probability 1.

• (“Soundness.”) For all 0 ≤ ϵ ≤ 1, if dist(w, C ) > ϵ, then for every “proof ”
Π ∈ {0, 1}
ℓ the tester T rejects with probability greater than λ · ϵ.

Equivalently, if there exists Π ∈ {0, 1}
ℓ that causes T to accept with
probability at least 1 − λ · ϵ, then w must be ϵ-close to C .

PCPP systems are also known as assisted testers, locally testable proofs, or
assignment testers.

Remark 7.14. A word on the three parameters: We are usually interested in
ﬁxing the number of queries r to a very small universal constant (such as 3)
while trying to keep the proof length ℓ = ℓ(n) relatively small (e.g., poly(n) is
a good goal). We are usually not very concerned with the rejection rate λ so
long as it’s a positive universal constant (independent of n).

Example 7.15. In Example 7.12 we stated that O = {w ∈ F n
2 : w1 +· · ·+ wn = 1}
has no local tester making fewer than n queries. But it’s easy to give a 3-query
PCPP system for O with proof length n − 1 (and rejection rate 1). The idea is
to require the proof string Π to contain the partial sums of w:

Π j =
 j+1∑

i=1 wi (mod 2).

The tester will perform one of the following checks, uniformly at random:

Π1 = w1 + w2
Π2 = Π1 + w3
Π3 = Π2 + w4

· · ·

Πn−1 = Πn−2 + wn
Πn−1 = 1

Evidently the tester always makes at most 3 queries. Further, in the “com-
pleteness” case w ∈ O , if Π is a correct list of partial sums then the tester will
accept with probability 1. It remains to analyze the “soundness” case, w ̸∈ O .
Here we are signiﬁcantly aided by the fact that dist(w, O ) must be exactly 1/n
(since every string is at Hamming distance either 0 or 1 from O ). Thus to
conﬁrm the claimed rejection rate of 1, we only need to observe that if w ̸∈ O
then at least one of the tester’s n checks must fail.

This example generalizes to give a very efﬁcient PCPP system for testing
that w satisﬁes any ﬁxed F 2-linear equation. What about testing that w
satisﬁes a ﬁxed system of F 2-linear equations? This interesting question is
explored in Exercise 7.16, which serves as a good warmup for our next result.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.2. Probabilistically Checkable Proofs of Proximity 181

We now extend Theorem 7.9 to show the rather remarkable fact that
any property of n-bit strings has a 3-query PCPP system. (The proof length,
however, is enormous.)

Theorem 7.16. Let C ⊆ {0, 1}n be any class of strings. Then there is a 3-query,
length-22n PCPP system for C (with rejection rate .001).

Proof. Let N = 2n and ﬁx an arbitrary bijection ι : {0, 1}n → [N]. The tester
will interpret the string w ∈ {0, 1}n to be tested as an index ι(w) ∈ [N] and will
interpret the 2N -length proof Π as a function Π : {0, 1}N → {0, 1}. The idea
is for the tester to require that Π be the dictator function corresponding to
index ι(w); i.e., χι(w) : {0, 1}N → {0, 1}.

Now under the identiﬁcation ι, we can think of the string property C as a
subclass of all N-bit dictators, namely

C ′ = {χι(w′) : {0, 1}N → {0, 1} | w′ ∈ C }.

In particular, C ′ is a property of N-bit functions. We can now state the twofold
goal of the tester:

(1) check that Π ∈ C ′;

(2) given that Π is indeed some dictator χι(w′) : {0, 1}N → {0, 1} with w′ ∈ C ,
check that w′ = w.

To accomplish the latter the tester would like to check w j = w′
j for a random
j ∈ [n]. The tester can query any w j directly but accessing w′
j requires a little
thought. The trick is to prepare the string

X ( j) ∈ {0, 1}N deﬁned by X ( j)
ι(y) = yj.

and then to locally correct Π on X ( j) (using Proposition 1.31).

Thus the tester is deﬁned as follows:

(1) With probability 1/2, locally test the function property C ′ using Theo-
rem 7.9.

(2) With probability 1/2, pick j ∼ [n] uniformly at random; locally correct Π
on the string X ( j) and accept if the outcome equals w j.

Note that the tester makes 3 queries in both of the subtests.

Verifying “completeness” of this PCPP system is easy: if w ∈ C and Π is
indeed the (truth table of) χι(w) : {0, 1}N → {0, 1} then the test will accept with
probability 1. It remains to verify the “soundness” condition. Fix w ∈ {0, 1}n,
Π : {0, 1}N → {0, 1}, and 0 ≤ ϵ ≤ 1 and suppose that the tester accepts (w, Π)
with probability at least 1 − λϵ, where λ = .001. Our goal is to show that w is
ϵ-close to some string w′ ∈ C .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

182 7. Property testing, PCPPs, and CSPs

Since the overall test accepts with probability at least 1 − λϵ, subtest (1)
above accepts with probability at least 1 − 2λϵ. Thus by Theorem 7.9, Π must
be 200λϵ-close to some dictator χι(w′) with w′ ∈ C . Since dictators are parity
functions, Proposition 1.31 tells us that

∀ j, Pr[locally correcting Π on X ( j) produces χι(w′)(X ( j)) = w′
j] ≥ 1−400λϵ ≥ 1/2,
(7.1)
where we used 400λϵ < 400λ ≤ 1/2 by the choice λ = .001.

On the other hand, since the overall test accepts with probability at least
1 − λϵ, subtest (2) above rejects with probability at most 2λϵ. This means

E
j∼[n]
 [
Pr[locally correcting Π on X ( j) doesn’t produce w j]
] ≤ 2λϵ.

By Markov’s inequality we deduce that except for at most a 4λϵ fraction of
coordinates j ∈ [n] we have

Pr[locally correcting Π on X ( j) doesn’t produce w j] < 1/2.

Combining this information with (7.1) we deduce that w j = w′
j except for at
most a 4λϵ ≤ ϵ fraction of coordinates j ∈ [n]. Since w′ ∈ C we conclude that
dist(w, C) ≤ ϵ, as desired. □

You may feel that the doubly-exponential proof length 2
2n in this theorem
is quite bad, but bear in mind there are 22n different properties C . Actually,
giving a PCPP system for every property is a bit overzealous since most prop-
erties are not interesting or natural. A more reasonable goal would be to give
efﬁcient PCPP systems for all “explicit” properties. A good way to formalize
this is to consider properties decidable by polynomial-size circuits. Here we
use the deﬁnition of general (De Morgan) circuits from Exercise 4.13. Given
an n-variable circuit C we consider the set of strings which it “accepts” to be
a property, C = {w ∈ {0, 1}n : C(w) = 1}. (7.2)

For properties computed by modest-sized circuits C we may hope for PCPP
systems with proof length much less than 22n . We saw such a case in Exam-
ple 7.15.

Another advantage of considering “explicit” properties is that we can de-
ﬁne a notion of constructing a PCPP system, “given” a property. A theorem
of the form “for each explicit property C there exists an efﬁcient PCPP sys-
tem. . . ” may not be useful, practically speaking, if its proof is nonconstructive.
We can formalize the issue as follows:

Deﬁnition 7.17. A PCPP reduction is an algorithm which takes as input a
circuit C and outputs the description of a PCPP system for the string prop-
erty C decided by C as in (7.2), where n is the number of inputs to C. If the
output PCPP system always makes r queries, has proof length ℓ(n, size(C))

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.3. CSPs and computational complexity 183

(for some function ℓ), and has rejection rate λ > 0, we say that the PCPP
reduction has the same parameters. Finally, the PCPP reduction should run
in time poly(size(C), ℓ).

(We haven’t precisely speciﬁed what it means to output the description of
a PCPP system; this will be explained more carefully in Section 7.3. In brief
it means to list – for each possible outcome of the tester’s randomness – which
bits are queried and what predicate of them is used to decide acceptance.)

Looking back at the results on testing subclasses of dictatorship (Theo-
rem 7.9) and PCPPs for any property (Theorem 7.16) we can see they have
the desired sort of “constructive” proofs. In Theorem 7.9 the local tester’s de-
scription depends in a very simple way on the input 1S. As for Theorem 7.16,
it sufﬁces to note that given an n-input circuit C we can write down its truth
table (and hence the property it decides) in time poly(size(C))·2n, whereas the
allowed running time is at least poly(size(C), 22n ). Hence we may state:

Theorem 7.18. There exists a 3-query PCPP reduction with proof length 22n

(and rejection rate .001).

In Exercise 7.18 you are asked to improve this result as follows:

Theorem 7.19. There exists a 3-query PCPP reduction with proof length
2poly(size(C)) (and positive rejection rate).

(The fact that we again have just 3 queries is explained by Exercise 7.12;
there is a generic reduction from any constant number of queries down to 3.)

Indeed, there is a much more dramatic improvement:

The PCPP Theorem. There exists a 3-query PCPP reduction with proof
length poly(size(C)) (and positive rejection rate).

This is (a slightly strengthened version of) the famous “PCP Theorem”
[FGL
+96, AS98, ALM+98] from the ﬁeld of computational complexity, which
is discussed later in this chapter. Though the PCPP Theorem is far stronger
than Theorem 7.18, the latter is not unnecessary; it’s actually an ingredient
in Dinur’s proof of the PCP Theorem [Din07], being applied only to circuits of
“constant” size. The current state of the art for PCPP length [Din07, BS08]
is highly efﬁcient:

Theorem 7.20. There exists a 3-query PCPP reduction with proof length
size(C) · polylog(size(C)) (and positive rejection rate).

7.3. CSPs and computational complexity

This section is about the computational complexity of constraint satisfaction
problems (CSPs), a fertile area of application for analysis of Boolean functions.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

184 7. Property testing, PCPPs, and CSPs

To study it we need to introduce a fair bit of background material; in fact, this
section will mainly consist of deﬁnitions.

In brief, a CSP is an algorithmic task in which a large number of “vari-
ables” must be assigned “labels” so as to satisfy given “local constraints”. We
start by informally describing some examples:

Example 7.21.

• In the “Max-3-Sat” problem, given is a CNF formula of width at most 3
over Boolean variables x1, . . . , xn. The task is to ﬁnd a setting of the
inputs that satisﬁes (i.e., makes True) as many clauses as possible.

• In the “Max-Cut” problem, given is an undirected graph G = (V , E). The
task is to ﬁnd a “cut” – i.e., a partition of V into two parts – so that as
many edges as possible “cross the cut”.

• In the “Max-E3-Lin” problem, given is a system of linear equations
over F 2, each equation involving exactly 3 variables. The system may in
general be overdetermined; the task is to ﬁnd a solution which satisﬁes
as many equations as possible.

• In the “Max-3-Coloring” problem, given is an undirected graph G =
(V , E). The task is to color each vertex either red, green, or blue so as to
make as many edges as possible bichromatic.

Let’s rephrase the last two of these examples so that the descriptions
have more in common. In Max-E3-Lin we have a set of variables V , to be
assigned labels from the domain Ω = F 2. Each constraint is of the form
v1 + v2 + v3 = 0 or v1 + v2 + v3 = 1, where v1, v2, v3 ∈ V . In Max-3-Coloring
we have a set of variables (vertices) V to be assigned labels from the domain
Ω = {red, green, blue}. Each constraint (edge) is a pair of variables, constrained
to be labeled by unequal colors.

We now make formal deﬁnitions which encompass all of the above exam-
ples:

Deﬁnition 7.22. A constraint satisfaction problem (CSP) over domain Ω
is deﬁned by a ﬁnite set of predicates (“types of constraints”) Ψ, with each
ψ ∈ Ψ being of the form ψ : Ωr → {0, 1} for some arity r (possibly different for
different predicates). We say that the arity of the CSP is the maximum arity
of its predicates.

Such a CSP is associated with an algorithmic task called “Max-CSP(Ψ)”,
which we will deﬁne below. First, though, let us see how the CSPs from
Example 7.21 ﬁt into the above deﬁnition.

• Max-3-Sat: Domain Ω = {True,False}; Ψ contains 14 predicates: the 8
logical OR functions on 3 literals (variables/negated-variables), the 4

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.3. CSPs and computational complexity 185

logical OR functions on 2 literals, and the 2 logical OR functions on 1
literal.

• Max-Cut: Domain Ω = {−1, 1}; Ψ = {̸=}, where ̸=: {−1, 1}
2 → {0, 1} is the
“not-equal” predicate.

• Max-E3-Lin: Domain Ω = F 2; Ψ contains the two 3-ary predicates
(x1, x2, x3) 7→ x1 + x2 + x3 and (x1, x2, x3) 7→ x1 + x2 + x3 + 1.

• Max-3-Coloring: Domain Ω = {red, green, blue}; Ψ contains just the sin-
gle not-equal predicate ̸=: Ω2 → {0, 1}.

Remark 7.23. Let us add a few words about traditional CSP terminology.
Boolean CSPs refer to the case |Ω| = 2. If ψ : {−1, 1}r → {0, 1} is a Boolean pred-
icate we sometimes write “Max-ψ” to refer to the CSP where all constraints
are of the form ψ applied to literals; i.e., Ψ = {ψ(±v1, . . . , ±vr)}. As an example,
Max-E3-Lin could also be called Max-χ[3]. The “E3” in the name Max-E3-Lin
refers to the fact that all constraints involve “E”xactly 3 variables. Thus e.g.
Max-3-Lin is the generalization in which 1- and 2-variable equations are al-
lowed. Conversely, Max-E3-Sat is the special case of Max-3-Sat where each
clause must be of width exactly 3 (a CSP which could also be called Max-OR3).

To formally deﬁne the algorithmic task Max-CSP(Ψ), we begin by deﬁning
its input:

Deﬁnition 7.24. An instance (or input) P of Max-CSP(Ψ) over variable set V
is a list (multiset) of constraints. Each constraint C ∈ P is a pair C = (S, ψ),
where ψ ∈ Ψ and where the scope S = (v1, . . . , vr) is a tuple of distinct variables
from V , with r being the arity of ψ. We always assume that each v ∈ V
participates in at least one constraint scope. The size of an instance is the
number of bits required to represent it; writing n = |V | and treating |Ω|, |Ψ|
and the arity of Ψ as constants, the size is between n and O(|P | log n).

Remark 7.25. Let’s look at how the small details of Deﬁnition 7.24 affect
input graphs for Max-Cut. Since an instance is a multiset of constraints, this
means we allow graphs with parallel edges. Since each scope must consist
of distinct variables, this means we disallow graphs with self-loops. Finally,
since each variable must participate in at least one constraint, this means in-
put graphs must have no isolated vertices (though they may be disconnected).

Given an assignment of labels for the variables, we are interested in the
number of constraints that are “satisﬁed”. The reason we explicitly allow
duplicate constraints in an instance is that we may want some constraints
to be more important than others. In fact it’s more convenient to normalize
by looking at the fraction of satisﬁed constraints, rather than the number.
Equivalently, we can choose a constraint C ∼ P uniformly at random and look
at the probability that it is satisﬁed. It will actually be quite useful to think

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

186 7. Property testing, PCPPs, and CSPs

of a CSP instance P as a probability distribution on constraints. (Indeed, we
could have more generally deﬁned weighted CSPs in which the constraints
are given arbitrary nonnegative weights summing to 1; however, we don’t
want to worry about the issue of representing, say, irrational weights with
ﬁnitely many bits.)

Deﬁnition 7.26. An assignment (or labeling) for instance P of Max-CSP(Ψ)
is just a mapping F : V → Ω. For constraint C = (S, ψ) ∈ P we say that F
satisﬁes C if ψ(F(S)) = 1. Here we use shorthand notation: if S = (v1, . . . , vr)
then F(S) denotes (F(v1), . . . , F(vr)). The value of F, denoted ValP (F), is the
fraction of constraints in P that F satisﬁes:

ValP (F) = E
(S,ψ)∼P [ψ(F(S))] ∈ [0, 1]. (7.3)

The optimum value of P is

Opt(P ) = max
F:V →Ω{ValP (F)}.

If Opt(P ) = 1, we say that P is satisﬁable.

Remark 7.27. In the literature on CSPs there is sometimes an unfortunate
blurring between a variable and its assignment. For example, a Max-E3-Lin
instance may be written as
 x1 + x2 + x3 = 0

x1 + x5 + x6 = 0

x3 + x4 + x6 = 1;

then a particular assignment x1 = 0, x2 = 1, x3 = 0, x4 = 1, x5 = 1, x6 = 1 may be
given. Now there is confusion: Does x2 represent the name of a variable or
does it represent 1? Because of this we prefer to display CSP instances with
the name of the assignment F present in the constraints. That is, the above
instance would be described as ﬁnding F : {x1, . . . , x6} → F 2 so as to satisfy as
many as possible of the following:

F(x1) + F(x2) + F(x3) = 0

F(x1) + F(x5) + F(x6) = 0

F(x3) + F(x4) + F(x6) = 1,

Finally, we deﬁne the algorithmic task associated with a CSP:

Deﬁnition 7.28. The algorithmic task Max-CSP(Ψ) is deﬁned as follows: The
input is an instance P . The goal is to output an assignment F with as large
a value as possible.

Having deﬁned CSPs, let us make a connection to the notion of a string
testing algorithm from the previous section. The connection is this: CSPs

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.3. CSPs and computational complexity 187

and string testing algorithms are the same object. Indeed, consider a CSP
instance P over domain Ω with n variables V . Fix an assignment F : V →
Ω; we can also think of F as a string in Ωn (under some ordering of V ).
Now think of a testing algorithm which chooses a constraint (S, ψ) ∼ P at
random, “queries” the string entry F(v) for each v ∈ S, and accepts if and only
if the predicate ψ(F(S)) is satisﬁed. This is indeed an r-query string testing
algorithm, where r is the arity of the CSP; the probability the tester accepts
is precisely ValP (F).

Conversely, let T be some randomized testing algorithm for strings in Ωn.
Assume for simplicity that T’s randomness comes from the uniform distribu-
tion over some sample space U. Now suppose we enumerate all outcomes
in U, and for each we write the tuple of indices S that T queries and the
predicate ψ : Ω|S| → {0, 1} that T uses to make its subsequent accept/reject
decision. Then this list of scope/predicates pairs is precisely an instance of
an n-variable CSP over Ω. The arity of the CSP is equal to the (maximum)
number of queries that T makes and the predicates for the CSP are precisely
those used by the tester in making its accept/reject decisions. Again, the
probability that T accepts a string F ∈ Ωn is equal to the value of F as an
assignment for the CSP. (Our actual deﬁnition of string testers allowed any
form of randomness, including, say, irrational probabilities; thus technically
not every string tester can be viewed as a CSP. However, it does little harm
to ignore this technicality.)

In particular, this equivalence between string testers and CSPs lets us
properly deﬁne “outputting the description of a PCPP system” as in Deﬁni-
tion 7.17 of PCPP reductions.

Example 7.29. The PCPP system for O = {w ∈ F 2 : w1 + · · · + wn = 1} given in
Example 7.15 can be thought of as an instance of the Max-3-Lin CSP over the
2n − 1 variables {w1, . . . , wn, Π1, . . . , Πn−1}. The BLR linearity test for functions
F n
2 → F 2 can also be thought of as instance of Max-3-Lin over 2n variables
(recall that function testers are string testers). In this case we identify the
variable set with F n
2 ; if n = 2 then the variables are named (0, 0), (0, 1), (1, 0),
and (1, 1); and, if we write F : F 2
2 → F 2 for the assignment, the instance is

F(0, 0) + F(0, 0) + F(0, 0) = 0 F(0, 1) + F(0, 0) + F(0, 1) = 0 F(1, 0) + F(0, 0) + F(1, 0) = 0 F(1, 1) + F(0, 0) + F(1, 1) = 0

F(0, 0) + F(0, 1) + F(0, 1) = 0 F(0, 1) + F(0, 1) + F(0, 0) = 0 F(1, 0) + F(0, 1) + F(1, 1) = 0 F(1, 1) + F(0, 1) + F(1, 0) = 0

F(0, 0) + F(1, 0) + F(1, 0) = 0 F(0, 1) + F(1, 0) + F(1, 1) = 0 F(1, 0) + F(1, 0) + F(0, 0) = 0 F(1, 1) + F(1, 0) + F(0, 1) = 0

F(0, 0) + F(1, 1) + F(1, 1) = 0 F(0, 1) + F(1, 1) + F(1, 0) = 0 F(1, 0) + F(1, 1) + F(0, 1) = 0 F(1, 1) + F(1, 1) + F(0, 0) = 0.

Cf. Remark 7.27; also, note the duplicate constraints.

We end this section by discussing the computational complexity of ﬁnding
high-value assignments for a given CSP – equivalently, ﬁnding strings that
make a given string tester accept with high probability. Consider, for example,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

188 7. Property testing, PCPPs, and CSPs

the task of Max-Cut on n-vertex graphs. Of course, given a Max-Cut instance
one can always ﬁnd the optimal solution in time roughly 2n, just by trying all
possible cuts. Unfortunately, this is not very efﬁcient, even for slightly large
values of n. In computational complexity theory, an algorithm is generally
deemed “efﬁcient” if it runs in time poly(n). For some subfamilies of graphs
there are poly(n)-time algorithms for ﬁnding the maximum cut, e.g., bipartite
graphs (Exercise 7.14) or planar graphs. However, it seems very unlikely
that there is a poly(n)-time algorithm that is guaranteed to ﬁnd an optimal
Max-Cut assignment given any input graph. This statement is formalized by
a basic theorem from the ﬁeld of computational complexity:

Theorem 7.30. The task of ﬁnding the maximum cut in a given input graph
is “NP-hard”.

We will not formally deﬁne NP-hardness in this book (though see Exer-
cise 7.13 for some more explanation). Roughly speaking it means “at least as
hard as the Circuit-Sat problem”, where “Circuit-Sat” is the following task:
Given an n-variable Boolean circuit C, decide whether or not C is satisﬁable
(i.e., there exists w ∈ {0, 1}n such that C(w) = 1). It is widely believed that
Circuit-Sat does not have a polynomial-time algorithm (this is the “P ̸= NP”
conjecture). In fact it is also believed that Circuit-Sat does not have a 2o(n)-
time algorithm.

For essentially all CSPs, including Max-E3-Sat, Max-E3-Lin, and Max-3-
Coloring, ﬁnding an optimal solution is NP-hard. This motivates considering
a relaxed goal:

Deﬁnition 7.31. Let 0 ≤ α ≤ β ≤ 1. We say that algorithm A is an (α, β)-
approximation algorithm for Max-CSP(Ψ) (pronounced “α out of β approxima-
tion”) if it has the following guarantee: on any instance with optimum value
at least β, algorithm A outputs an assignment of value at least α. In case A is
a randomized algorithm, we only require that its output has value at least α
in expectation.

A mnemonic here is that when the βest assignment has value β, the αlgorithm
gets value α.

Example 7.32. Consider the following algorithm for Max-E3-Lin: Given
an instance, output either the assignment F ≡ 0 or the assignment F ≡ 1,
whichever has higher value. Since either 0 or 1 occurs on at least half of the
instance’s “right-hand sides”, the output assignment will always have value
at least 1
2 . Thus this is an efﬁcient ( 1
2 , β)-approximation algorithm for any β.
In the case β = 1 one can do better: performing Gaussian elimination is an
efﬁcient (1, 1)-approximation algorithm for Max-E3-Lin (or indeed Max-r-Lin
for any r).
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.3. CSPs and computational complexity 189

As a far more sophisticated example, Goemans and Williamson [GW95]
showed that there is an efﬁcient (randomized) algorithm which (.878β, β)-
approximates Max-Cut for every β.

Not only is ﬁnding the optimal solution of a Max-E3-Sat instance NP-hard,
it’s even NP-hard on satisﬁable instances. In other words:

Theorem 7.33. (1, 1)-approximating Max-E3Sat is NP-hard. The same is true
of Max-3-Coloring.

On the other hand, it’s easy to (1, 1)-approximate Max-3-Lin (Example 7.32)
or Max-Cut (Exercise 7.14). Nevertheless, the “textbook” NP-hardness results
for these problems imply the following:

Theorem 7.34. (β, β)-approximating Max-E3-Lin is NP-hard for any ﬁxed
β ∈ ( 1
2 , 1). The same is true of Max-Cut.

In some ways, saying that (1, 1)-distinguishing Max-E3-Sat is NP-hard is
not necessarily that disheartening. For example, if (1 − δ, 1)-approximating
Max-E3-Sat were possible in polynomial time for every δ > 0, you might con-
sider that “good enough”. Unfortunately, such a state of affairs is very likely
ruled out:

Theorem 7.35. There exists a positive universal constant δ0 > 0 such that
(1 − δ0, 1)-approximating Max-E3-Sat is NP-hard.

In fact, Theorem 7.35 is equivalent to the “PCP Theorem” mentioned in
Section 7.2. It follows straightforwardly from the PCPP Theorem, as we now
sketch:

Proof sketch. Let δ0 be the rejection rate in the PCPP Theorem. We want
to show that (1 − δ0, 1)-approximating Max-E3-Sat is at least as hard as the
Circuit-Sat problem. Equivalently, we want to show that if there is an efﬁcient
algorithm A for (1−δ0, 1)-approximating Max-E3-Sat then there is an efﬁcient
algorithm B for Circuit-Sat. So suppose A exists and let C be a Boolean
circuit given as input to B. Algorithm B ﬁrst applies to C the PCPP reduction
given by the PCPP Theorem. The output is some arity-3 CSP instance P
over variables w1, . . . , wn, Π1, . . . , Πℓ, where ℓ ≤ poly(size(C)). By Exercise 7.12
we may assume that P is an instance of Max-E3-Sat. From the deﬁnition
of a PCPP system, it is easy to check (Exercise 7.19) the following: If C is
satisﬁable then Opt(P ) = 1; and, if C is not satisﬁable then Opt(P ) < 1 − δ0.
Algorithm B now runs the supposed (1 − δ0, 1)-approximation algorithm A
on P and outputs “C is satisﬁable” if and only if A ﬁnds an assignment of
value at least 1 − δ0. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

190 7. Property testing, PCPPs, and CSPs

7.4. Highlight: Håstad’s hardness theorems

In Theorem 7.35 we saw that it is NP-hard to (1 − δ0, 1)-approximate Max-
E3Sat for some positive but inexplicit constant δ0. You might wonder how
large δ0 can be. The natural limit here is 1
8 because there is a very simple
algorithm that satisﬁes a 7
8 -fraction of the constraints in any Max-E3Sat
instance:

Proposition 7.36. Consider the Max-E3-Sat algorithm that outputs a uni-
formly random assignment F. This is a ( 7
8 , β)-approximation for any β.

Proof. In instance P , each constraint is a logical OR of exactly 3 literals
and will therefore be satisﬁed by F with probability exactly 7
8 . Hence in
expectation the algorithm will satisfy a 7
8 -fraction of the constraints. □

(It’s also easy to “derandomize” this algorithm, giving a deterministic guaran-
tee of at least 7
8 of the constraints; see Exercise 7.21.)

This algorithm is of course completely brainless – it doesn’t even “look
at” the instance it is trying to approximately solve. But rather remarkably,
it achieves the best possible approximation guarantee among all efﬁcient
algorithms (assuming P ̸= NP). This is a consequence of the following 1997
theorem of Håstad [Hås01b], improving signiﬁcantly on Theorem 7.35:

Håstad’s 3-Sat Hardness. For any constant δ > 0, it is NP-hard to ( 7
8 + δ, 1)-
approximate Max-E3-Sat.

Håstad gave similarly optimal hardness-of-approximation results for sev-
eral other problems, including Max-E3-Lin:

Håstad’s 3-Lin Hardness. For any constant δ > 0, it is NP-hard to ( 1
2 + δ, 1 −
δ)-approximate Max-E3-Lin.

In this hardness theorem, both the “α” and “β” parameters are optimal;
as we saw in Example 7.32 one can efﬁciently ( 1
2 , β)-approximate and also
(1, 1)-approximate Max-E3-Lin.

The goal of this section is to sketch the proof of the above theorems, mainly
Håstad’s 3-Lin Hardness Theorem. Let’s begin by considering the 3-Sat hard-
ness result. If our goal is to increase the inexplicit constant δ0 in Theo-
rem 7.35, it makes sense to look at how the constant arises. From the proof
of Theorem 7.35 we see that it’s just the rejection rate in the PCPP Theorem.
We didn’t prove that theorem, but let’s consider its length-2
2n analogue, Theo-
rem 7.18. The key ingredient in the proof of Theorem 7.18 is the dictator test.
Indeed, if we strip away the few local correcting and consistency checks, we
see that the dictator test component controls both the rejection rate and the
type of predicates output by the PCPP reduction. This observation suggests

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.4. Highlight: Håstad’s hardness theorems 191

that to get a strong hardness-of-approximation result for, say, Max-E3-Lin,
we should seek a local tester for dictatorship which (a) has a large rejection
rate, and (b) makes its accept/reject decision using 3-variable linear equation
predicates.

This approach (which of course needs to be integrated with efﬁcient “PCPP
technology”) was suggested in a 1995 paper of Bellare, Goldreich, and Su-
dan [BGS95]. Using it, they managed to prove NP-hardness of (1 − δ0, 1)-
approximating Max-E3-Sat with the explicit constant δ0 = .026. Håstad’s
key conceptual contribution (originally from [Hås96]) was showing that given
known PCPP technology, it sufﬁces to construct a certain kind of relaxed
dictator test. Roughly speaking, dictators should still be accepted with prob-
ability 1 (or close to 1), but only functions which are “very unlike” dictators
need to be rejected with substantial probability. Since this is a weaker re-
quirement than in the standard deﬁnition of a local tester, we can potentially
achieve a much higher rejection rate, and hence a much stronger hardness-of-
approximation result.

For these purposes, the most useful formalization of being “very unlike
a dictator” turns out to be “having no notable coordinates” in the sense of
Deﬁnition 6.9. We make the following deﬁnition which is appropriate for
Boolean CSPs.

Deﬁnition 7.37. Let Ψ be a ﬁnite set of predicates over the domain Ω =
{−1, 1}. Let 0 < α < β ≤ 1 and let λ : [0, 1] → [0, 1] satisfy λ(ϵ) → 0 as ϵ → 0.
Suppose that for each n ∈ N + there is a local tester for functions f : {−1, 1}n →
{−1, 1} with the following properties:

• If f is a dictator then the test accepts with probability at least β.

• If f has no (ϵ, ϵ)-notable coordinates – i.e., Inf
(1−ϵ)
i [ f ] ≤ ϵ for all i ∈ [n] –
then the test accepts with probability at most α + λ(ϵ).

• The tester’s accept/reject decision uses predicates from Ψ; i.e., the tester
can be viewed as an instance of Max-CSP(Ψ).

Then, abusing terminology, we call this family of testers an (α, β)-Dictator-vs.-
No-Notables test using predicate set Ψ.

Remark 7.38. For very minor technical reasons, the above deﬁnition should
actually be slightly amended. In this section we freely ignore the amendments,
but for the sake of correctness we state them here. One is a strengthening,
one is a weakening.

• The second condition should be required even for functions f : {−1, 1}n →
[−1, 1]; what this means is explained in Exercise 7.22.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

192 7. Property testing, PCPPs, and CSPs

• When the tester makes accept/reject decisions by applying ψ ∈ Ψ to
query results f (x(1)), . . . , f (x(r)), it is allowed that the query strings are
not all distinct. (See Exercise 7.31.)

Remark 7.39. It’s essential in this deﬁnition that the “error term” λ(ϵ) = oϵ(1)
be independent of n. On the other hand, we otherwise care very little about
the rate at which it tends to 0; this is why we didn’t mind using the same
parameter ϵ in the “(ϵ, ϵ)-notable” hypothesis.

Just as the dictator test was the key component in our PCPP reduction
(Theorem 7.18), Dictator-vs.-No-Notables tests are the key to obtaining strong
hardness-of-approximation results. The following result (essentially proved
in Khot et al. [KKMO07]) lets you obtain hardness results from Dictator-vs.-
No-Notables tests in a black-box way:

Theorem 7.40. Fix a CSP over domain Ω = {−1, 1} with predicate set Ψ. Sup-
pose there exists an (α, β)-Dictator-vs.-No-Notables test using predicate set Ψ.
Then for all δ > 0, it is “UG-hard” to (α + δ, β − δ)-approximate Max-CSP(Ψ).

In other words, the distinguishing parameters of a Dictator-vs.-No-Notables
test automatically translate to the distinguishing parameters of a hardness
result (up to an arbitrarily small δ).

The advantage of Theorem 7.40 is that it reduces a problem about compu-
tational complexity to a purely Fourier-analytic problem, and a constructive
one at that. The theorem has two disadvantages, however. The ﬁrst is that
instead of NP-hardness – the gold standard in complexity theory – it merely
gives “UG-hardness”, which roughly means “at least as hard as the Unique-
Games problem”. We leave the deﬁnition of the Unique-Games problem to
Exercise 7.27, but sufﬁce it to say it’s not as universally believed to be hard
as Circuit-Sat is. The second disadvantage of Theorem 7.40 is that it only
has β − δ rather than β. This can be a little disappointing, especially when
you are interested in hardness for satisﬁable instances (β = 1), as in Håstad’s
3-Sat Hardness. In his work, Håstad showed that both disadvantages can
be erased provided you construct something similar to, but more complicated
than, an (α, β)-Dictator-vs.-No-Notables test. This is how the Håstad 3-Sat
and 3-Lin Hardness Theorems are proved. Describing this extra complica-
tion is beyond the scope of this book; therefore we content ourselves with the
following theorems:

Theorem 7.41. For any 0 < δ < 1
8 , there exists a ( 7
8 + δ, 1)-Dictator-vs.-No-
Notables test which uses logical OR functions on 3 literals as its predicates.

Theorem 7.42. For any 0 < δ < 1
2 , there exists a ( 1
2 , 1 − δ)-Dictator-vs.-No-
Notables test using 3-variable F 2-linear equations as its predicates.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.4. Highlight: Håstad’s hardness theorems 193

Theorem 7.42 will be proved below, while the proof of Theorem 7.41 is
left for Exercise 7.29. By applying Theorem 7.40 we immediately deduce the
following weakened versions of Håstad’s Hardness Theorems:

Corollary 7.43. For any δ > 0, it is UG-hard to ( 7
8 + δ, 1 − δ)-approximate
Max-E3-Sat.

Corollary 7.44. For any δ > 0, it is UG-hard to ( 1
2 + δ, 1 − δ)-approximate
Max-E3-Lin.

Remark 7.45. For Max-E3-Lin, we don’t mind the fact that Theorem 7.40
has β − δ instead of β because our Dictator-vs.-No-Notables test only accepts
dictators with probability 1 − δ anyway. Note that the 1 − δ in Theorem 7.42
cannot be improved to 1; see Exercise 7.7.)

To prove a result like Theorem 7.42 there are two components: the design
of the test, and its analysis. We begin with the design. Since we are looking
for a test using 3-variable linear equation predicates, the BLR Test naturally
suggests itself; indeed, all of its checks are of the form f (x) + f (y) + f (z) = 0.
It also accepts dictators with probability 1. Unfortunately it’s not true that
it accepts functions with no notable coordinates with probability close to 1
2 .
There are two problems: the constant 0 function and “large” parity functions
are both accepted with probability 1, despite having no notable coordinates.
The constant 1 function is easy to deal with: we can replace the BLR Test by
the “Odd BLR Test”.

Odd BLR Test. Given query access to f : F n
2 → F 2:

• Choose x ∼ F n
2 and y ∼ F n
2 independently.

• Choose b ∼ F 2 uniformly at random and set z = x + y + (b, b, . . . , b) ∈ F n
2 .

• Accept if f (x) + f (y) + f (z) = b.

Note that this test uses both kinds of 3-variable linear equations as its
predicates. For the test’s analysis, we as usual switch to ±1 notation and
think of testing f (x) f (y) f (z) = b. It is easy to show the following (see the
proof of Theorem 7.42, or Exercise 7.15 for a generalization):

Proposition 7.46. The Odd BLR Test accepts f : {−1, 1}n → {−1, 1} with prob-
ability 1
2 + 1
2 ∑

S⊆[n]
|S| odd
 ̂f (S)
3 ≤ 1
2 + 1
2 max
S⊆[n]
|S| odd

{ ̂f (S)}.

This twist rules out the constant 1 function; it passes the Odd BLR Test
with probability 1
2 . It remains to deal with large parity functions. Håstad’s
innovation here was to add a small amount of noise to the Odd BLR Test.
Speciﬁcally, given a small δ > 0 we replace z in the above test with z′ ∼

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

194 7. Property testing, PCPPs, and CSPs

N1−δ(z); i.e., we ﬂip each of its bits with probability δ/2. If f is a dictator, then
there is only a δ/2 chance this will affect the test. On the other hand, if f is a
parity of large cardinality, the cumulative effect of the noise will destroy its
chance of passing the linearity test. Note that parities of small odd cardinality
will also pass the test with probability close to 1; however, we don’t need to
worry about them since they have notable coordinates. We can now present
Håstad’s Dictator-vs.-No-Notables test for Max-E3-Lin.

Proof of Theorem 7.42. Given a parameter 0 < δ < 1, deﬁne the following
test, which uses Max-E3-Lin predicates:

Håstadδ Test. Given query access to f : {−1, 1}n → {−1, 1}:

• Choose x, y ∼ {−1, 1}n uniformly and independently.

• Choose bit b ∼ {−1, 1} uniformly and set z = b · (x ◦ y) ∈ {−1, 1}n (where ◦
denotes entry-wise multiplication).

• Choose z′ ∼ N1−δ(z).

• Accept if f (x) f (y) f (z′) = b.

We will show that this is a ( 1
2 , 1 − δ/2)-Dictator-vs.-No-Notables test. First,
let us analyze the test assuming b = 1.

Pr[Håstadδ Test accepts f | b = 1] = E[ 1
2 + 1
2 f (x) f (y) f (z′)]

= 1
2 + 1
2 E[ f (x) · f (y) · T1−δ f (x ◦ y)]]

= 1
2 + 1
2 E
x [ f (x) · ( f ∗ T1−δ f )(x)]

= 1
2 + 1
2 ∑

S⊆[n] ̂f (S) · áf ∗ T1−δ f (S)

= 1
2 + 1
2 ∑

S⊆[n](1 − δ)|S| ̂f (S)
3.

On the other hand, when b = −1 we take the expectation of 1
2 − 1
2 f (x) f (y) f (z′)
and note that z′ is distributed as N−(1−δ)(x ◦ y). Thus

Pr[Håstadδ Test accepts f | b = −1] = 1
2 − 1
2 ∑

S⊆[n](−1)
|S|(1 − δ)
|S| ̂f (S)3.

Averaging the above two results we deduce

Pr[Håstadδ Test accepts f ] = 1
2 + 1
2 ∑

|S| odd
(1 − δ)|S| ̂f (S)3. (7.4)

(Incidentally, by taking δ = 0 here we obtain the proof of Proposition 7.46.)

From (7.4) we see that if f is a dictator, f = χS with |S| = 1, then it is
accepted with probability 1 − δ/2. (It’s also easy to see this directly from the
deﬁnition of the test.) To complete the proof that we have a ( 1
2 , 1−δ/2)-Dictator-
vs.-No-Notables test, we need to bound the probability that f is accepted given

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.5. Exercises and notes 195

that it has (ϵ, ϵ)-small stable inﬂuences. More precisely, assuming

Inf
(1−ϵ)
i [ f ] = ∑

S∋i(1 − ϵ)|S|−1 ̂f (S)2 ≤ ϵ for all i ∈ [n] (7.5)

we will show that

Pr[Håstadδ Test accepts f ] ≤ 1
2 + 1
2 p
ϵ, provided ϵ ≤ δ. (7.6)

This is sufﬁcient because we can take λ(ϵ) in Deﬁnition 7.37 to be

λ(ϵ) =
 { 1
2 p
ϵ for ϵ ≤ δ,

1
2 for ϵ > δ.

Now to obtain (7.6), we continue from (7.4):

Pr[Håstadδ Test accepts f ] ≤ 1
2 + 1
2 max
|S| odd
{(1 − δ)
|S| ̂f (S)} · ∑

|S| odd ̂f (S)2

≤ 1
2 + 1
2 max
|S| odd
{(1 − δ)
|S| ̂f (S)}

≤ 1
2 + 1
2
 √ max
|S| odd
{(1 − δ)2|S| ̂f (S)2}

≤ 1
2 + 1
2
 √ max
|S| odd
{(1 − δ)|S|−1 ̂f (S)2}

≤ 1
2 + 1
2
 √
max
i∈[n] {Inf(1−δ)
i [ f ]},

where we used that |S| odd implies S nonempty. And the above is indeed at
most 1
2 + 1
2 p
ϵ provided ϵ ≤ δ, by (7.5). □

7.5. Exercises and notes

7.1 Suppose there is an r-query local tester for property C with rejection
rate λ. Show that there is a testing algorithm that, given inputs 0 <
ϵ, δ ≤ 1/2, makes O( r log(1/δ)
λϵ ) (nonadaptive) queries to f and satisﬁes the
following:
• If f ∈ C , then the tester accepts with probability 1.
• If f is ϵ-far from C , then the tester accepts with probability at
most δ.

7.2 Let M = {(x, y) ∈ {0, 1}
2n : x = y}, the property that a string’s ﬁrst half
matches its second half. Give a 2-query local tester for M with rejection
rate 1. (Hint: Locally test that x ⊕ y = (0, 0, . . . , 0).)

7.3 Reduce the proof length in Example 7.15 to n − 2.

7.4 Verify the claim from Example 7.12 regarding the 2-query tester for the
property that a string has all its coordinates equal. (Hint: Use ±1 nota-
tion.)
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

196 7. Property testing, PCPPs, and CSPs

7.5 Let O = {w ∈ F n
2 : w has an odd number of 1’s}. Let T be any (n − 1)-query
string testing algorithm that accepts every w ∈ O with probability 1. Show
that T in fact accepts every string v ∈ F n
2 with probability 1 (even though
dist(w, O ) = 1
n > 0 for half of all strings w). Thus locally testing O re-
quires n queries.

7.6 Let T be a 2-query testing algorithm for functions {−1, 1}n → {−1, 1}. Sup-
pose that T accepts every dictator with probability 1. Show that it also
accepts Majn′ with probability 1 for every odd n′ ≤ n. This shows that
there is no 2-query local tester for dictatorship assuming n > 2. (Hint:
You’ll need to enumerate all predicates on up to 2 bits.)

7.7 For every α < 1, show that there is no (α, 1)-Dictator-vs.-No-Notables test
using Max-E3-Lin predicates. (Hint: Consider large odd parities.)

7.8 (a) Consider the following 3-query testing algorithm for f : {0, 1}n → {0, 1}.
Let x, y ∼ {0, 1}n be independent and uniformly random, deﬁne z ∈
{0, 1}n by zi = xi ∧ yi for each i ∈ [n], and accept if f (x) ∧ f (y) = f (z).
Let pk be the probability that this test accepts a parity function χS :
{0, 1}n → {0, 1} with |S| = k. Show that p0 = p1 = 1 and that in general
pk ≤ 1
2 + 2−|S|. In fact, you might like to show that pk = 1
2 + ( 3
4 −
1
4 (−1)k)2−k. (Hint: It sufﬁces to consider k = n and then compute the
correlation of χ{1,...,n} ∧ χ{n+1,...,2n} with the bent function IP2n.)
(b) Show how to obtain a 3-query local tester for dictatorship by combin-
ing the following subtests: (i) the Odd BLR Test; (ii) the test from
part (a).

7.9 Obtain the largest explicit rejection rate in Theorem 7.7 that you can. You
might want to return to the Fourier expressions arising in Theorem 1.30
and 2.56, as well as Exercise 1.28. Can you improve your bound by doing
the BLR and NAE Tests with probabilities other than 1/2, 1/2?

7.10 (a) Say that A is an (α, β)-distinguishing algorithm for Max-CSP(Ψ) if
it outputs ‘YES’ on instances with value at least β and outputs ‘NO’
on instances with value strictly less than α. (On each instance with
value in [α, β), algorithm A may have either output.) Show that if
there is an efﬁcient (α, β)-approximation algorithm for Max-CSP(Ψ),
then there is also an efﬁcient (α, β)-distinguishing algorithm for Max-
CSP(Ψ).
(b) Consider Max-CSP(Ψ), where Ψ be a class of predicates that is closed
under restrictions (to nonconstant functions); e.g., Max-3-Sat. Show
that if there is an efﬁcient (1, 1)-distinguishing algorithm, then there
is also an efﬁcient (1, 1)-approximation algorithm. (Hint: Try out all
labels for the ﬁrst variable and use the distinguisher.)

7.11 (a) Let φ be a CNF of size s and width w ≥ 3 over variables x1, . . . , xn.
Show that there is an “equivalent” CNF φ′ of size at most (w −2)s and

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.5. Exercises and notes 197

width 3 over the variables x1, . . . , xn plus auxiliary variables Π1, . . . , Πℓ,
with ℓ ≤ (w − 3)s. Here “equivalent” means that for every x such that
φ(x) = True there exists Π such that φ′(x, Π) = True; and, for every x
such that φ(x) = False we have φ′(x, Π) = False for all Π.
(b) Extend the above so that every clause in φ′ has width exactly 3 (the
size may increase by O(s)).

7.12 Suppose there exists an r-query PCPP reduction R1 with rejection rate λ.
Show that there exists a 3-query PCPP reduction R2 with rejection rate
at least λ/(r2r). The proof length of R2 should be at most r2r · m plus the
proof length of R1 (where m is the description-size of R1’s output) and
the predicates output by the reduction should all be logical ORs applied
to exactly three literals. (Hint: Exercises 4.1, 7.11.)

7.13 (a) Give a polynomial-time algorithm R that takes as input a general
Boolean circuit C and outputs a width-3 CNF formula φ with the
following guarantee: C is satisﬁable if and only if φ is satisﬁable.
(Hint: Introduce a variable for each gate in C.)
(b) The previous exercise in fact formally justiﬁes the following state-
ment: “(1, 1)-distinguishing Max-3-Sat is NP-hard”. (See Exercise 7.10
for the deﬁnition of (1, 1)-distinguishing.) Argue that, indeed, if (1, 1)-
distinguishing (or (1, 1)-approximating) Max-3-Sat is in polynomial
time, then so is Circuit-Sat.
(c) Prove Theorem 7.33. (Hint: Exercise 7.11(b).)

7.14 Describe an efﬁcient (1, 1)-approximation algorithm for Max-Cut.

7.15 (a) Let H be any subspace of F n
2 and let H = {χγ : F n
2 → {−1, 1} | γ ∈ H⊥}.
Give a 3-query local tester for H with rejection rate 1. (Hint: Similar
to BLR, but with 〈ϕH ∗ f , f ∗ f 〉.)
(b) Generalize to the case that H is any afﬁne subspace of F n
2 .

7.16 Let A be any afﬁne subspace of F n
2 . Construct a 3-query, length-2n PCPP
system for A with rejection rate a positive universal constant. (Hint:
Given w ∈ F n
2 , the tester should expect the proof Π ∈ {−1, 1}
2n to encode
the truth table of χw. Use Exercise 7.15 and also a consistency check
based on local correcting of Π at e i, where i ∈ [n] is uniformly random.)

7.17 (a) Give a 3-query, length-O(n) PCPP system (with rejection rate a posi-
tive universal constant) for the class {w ∈ F n
2 : IPn(w) = 1}, where IPn
is the inner product mod 2 function (n even).
(b) Do the same for the complete quadratic function CQn from Exer-
cise 1.1. (Hint: Exercise 4.13.)

7.18 In this exercise you will prove Theorem 7.19.
(a) Let D ∈ F n×n
2 be a nonzero matrix and suppose x, y ∼ F n
2 are uniformly
random and independent. Show that Pr[y⊤Dx ̸= 0] ≥ 1
4 .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

198 7. Property testing, PCPPs, and CSPs

(b) Let γ ∈ F n
2 and Γ ∈ F n×n
2 . Suppose x, y ∼ F n
2 are uniformly random and
independent. Show that Pr[(γ
⊤x)(γ
⊤ y) = Γ • (x y⊤)] is 1 if Γ = γγ
⊤ and
is at most 3
4 otherwise. Here we use the notation B • C = ∑i, j Bi jCi j
for matrices B, C ∈ F n×n
2 .
(c) Suppose you are given query access to two functions ℓ : F n
2 → F 2 and
q : F n×n
2 → F 2. Give a 4-query testing algorithm with the following
two properties (for some universal constant λ > 0): (i) if ℓ = χγ and
q = χγγ⊤ for some γ ∈ F n
2 , the test accepts with probability 1; (ii) for
all 0 ≤ ϵ ≤ 1, if the test accepts with probability at least 1 − γ · ϵ, then
there exists some γ ∈ F n
2 such that ℓ is ϵ-close to χγ and q is ϵ-close
to χγγ⊤. (Hint: Apply the BLR Test to ℓ and q, and use part (b) with
local correcting on q.)
(d) Let L be a list of homogenous degree-2 polynomial equations over vari-
ables w1, . . . , wn ∈ F 2. (Each equation is of the form ∑n
i, j=1 ci jwiw j = b

for constants b, ci j ∈ F 2; we remark that w2
i = wi.) Deﬁne the string
property L = {w ∈ F n
2 : w satisﬁes all equations in L}. Give a 4-query,

length-(2n + 2n2) PCPP system for L (with rejection rate a positive
universal constant). (Hint: The tester should expect the truth table of
χw and χww⊤. You will need part (c) as well as Exercise 7.15 applied
to “q”.)
(e) Complete the proof of Theorem 7.19. (Hints: given w ∈ {0, 1}n, the
tester should expect a proof consisting of all gate values ¯w ∈ {0, 1}
size(C)

in C’s computation on w, as well as truth tables of χ ¯w and χ ¯w ¯w⊤.
Show that ¯w being a valid computation of C is encodable with a list
of homogeneous degree-2 polynomial equations. Add a consistency
check between w and ¯w using local correcting, and reduce the number
of queries to 3 using Exercise 7.12.)

7.19 Verify the connection between Opt(P ) and C’s satisﬁability stated in the
proof sketch of Theorem 7.35. (Hint: Every string w is 1-far from the
empty property.)

7.20 A randomized assignment for an instance P of a CSP over domain Ω is a
mapping F that labels each variable in V with a probability distribution
over domain elements. Given a constraint (S, ψ) with S = (v1, . . . , vr), we
write ψ(F(S)) ∈ [0, 1] for the expected value of ψ(F(v1), . . . , F(vr)). This is
simply the probability that ψ is satisﬁed when one actually draws from
the domain-distributions assigned by F. Finally, we deﬁne the value of F
to be ValP (F) = E(S,ψ)∼P [ψ(F(S))].
(a) Suppose that A is a deterministic algorithm that produces a random-
ized assignment of value α on a given instance P . Show a simple
modiﬁcation to A that makes it a randomized algorithm that pro-
duces a (normal) assignment whose value is α in expectation. (Thus,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.5. Exercises and notes 199

in constructing approximation algorithms we may allow ourselves to
output randomized assignments.)
(b) Let A be the deterministic Max-E3-Sat algorithm that on every in-
stance outputs the randomized assignment that assigns the uniform
distribution on {0, 1} to each variable. Show that this is a ( 7
8 , β)-
approximation algorithm for any β. Show also that the same algo-
rithm is a ( 1
2 , β)-approximation algorithm for Max-3-Lin.
(c) When the domain Ω is {−1, 1}, we may model a randomized assign-
ment as a function f : V → [−1, 1]; here f (v) = µ is interpreted as the
unique probability distribution on {−1, 1} which has mean µ. Now
given a constraint (S, ψ) with S = (v1, . . . , vr), show that the value of
f on this constraint is in fact ψ( f (v1), . . . , f (vr)), where we identify
ψ : {−1, 1}r → {0, 1} with its multilinear (Fourier) expansion. (Hint:
Exercise 1.4.)
(d) Let Ψ be a collection of predicates over domain {−1, 1}, and deﬁne
ν = minψ∈Ψ{ ̂ψ(;)}. Show that outputting the randomized assignment
f ≡ 0 is an efﬁcient (ν, β)-approximation algorithm for Max-CSP(Ψ).

7.21 Let F be a randomized assignment of value α for CSP instance P (as
in Exercise 7.20). Give an efﬁcient deterministic algorithm that outputs
a usual assignment F of value at least α. (Hint: Try all possible label-
ings for the ﬁrst variable and compute the expected value that would be
achieved if F were used for the remaining variables. Pick the best label
for the ﬁrst variable and repeat.)

7.22 Given a local tester for functions f : {−1, 1}n → {−1, 1}, we can interpret
it also as a tester for functions f : {−1, 1}n → [−1, 1]; simply view the
tester as a CSP and view the acceptance probability as the value of
f when treated as a randomized assignment (as in Exercise 7.20(c)).
Equivalently, whenever the tester “queries” f (x), imagine that what is re-
turned is a random bit b ∈ {−1, 1} whose mean is f (x). This interpretation
completes Deﬁnition 7.37 of Dictator-vs.-No-Notables tests for functions
f : {−1, 1}n → [−1, 1] (see Remark 7.38). Given this deﬁnition, verify that
the Håstadδ Test is indeed a ( 1
2 , 1−δ)-Dictator-vs.-No-Notables test. (Hint:
Show that (7.4) still holds for functions f : {−1, 1}n → [−1, 1]. There is only
one subsequent inequality that uses that f ’s range is {−1, 1}, and it still
holds with range [−1, 1].)

7.23 Let Ψ be a ﬁnite set of predicates over domain Ω = {−1, 1} that is closed
under negating variables. (An example is the scenario of Max-ψ from Re-
mark 7.23.) In this exercise you will show that Dictator-vs.-No-Notables
tests using Ψ may assume f : {−1, 1}n → [−1, 1] is odd without loss of
generality.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

200 7. Property testing, PCPPs, and CSPs

(a) Let T be an (α, β)-Dictator-vs.-No-Notables test using predicate set Ψ
that works under the assumption that f : {−1, 1}n → [−1, 1] is odd.
Modify T as follows: Whenever it is about to query f (x), with proba-
bility 1
2 let it use f (x) and with probability 1
2 let it use − f (−x). Call
the modiﬁed test T′. Show that the probability T′ accepts an arbitrary
f : {−1, 1}n → [−1, 1] is equal to the probability T accepts f odd (recall
Exercise 1.8).
(b) Prove that T′ is an (α, β)-Dictator-vs.-No-Notables test using predi-
cate set Ψ for functions f : {−1, 1}n → [−1, 1].

7.24 This problem is similar to Exercise 7.23 in that it shows you may assume
that Dictator-vs.-No-Notables tests are testing “smoothed” functions of
the form T1−δh for h : {−1, 1}n → [−1, 1], so long as you are willing to
lose O(δ) in the probability that dictators are accepted.
(a) Let U be an (α, β)-Dictator-vs.-No-Notables test using an arity-r pred-
icate set Ψ (over domain {−1, 1}) which works under the assumption
that the function f : {−1, 1}n → [−1, 1] being tested is of the form T1−δh
for h : {−1, 1}n → [−1, 1]. Modify U as follows: whenever it is about
to query f (x), let it draw y ∼ N1−δ(x) and use f (y) instead. Call the
modiﬁed test U ′. Show that the probability U ′ accepts an arbitrary
h : {−1, 1}n → [−1, 1] is equal to the probability U accepts T1−δh.
(b) Prove that U ′ is an (α, β − rδ/2)-Dictator-vs.-No-Notables test using
predicate set Ψ.

7.25 Give a slightly alternate proof of Theorem 7.42 by using the original
BLR Test analysis and applying Exercises 7.23, 7.24.

7.26 Show that when using Theorem 7.40, it sufﬁces to have a “Dictators-
vs.-No-Inﬂuentials test”, meaning replacing Inf(1−ϵ)
i [ f ] in Deﬁnition 7.37
with just Infi[ f ]. (Hint: Exercise 7.24.)

7.27 For q ∈ N +, Unique-Games(q) refers to the arity-2 CSP with domain Ω =
[q] in which all q! “bijective” predicates are allowed; here ψ is “bijective” if
there is a bijection π : [q] → [q] such that ψ(i, j) = 1 iff π( j) = i. Show that
(1, 1)-approximating Unique-Games(q) can be done in polynomial time.
(The Unique Games Conjecture of Khot [Kho02] states that for all δ > 0
there exists q ∈ N + such that (δ, 1 − δ)-approximating Unique-Games(q)
is NP-hard.)

7.28 In this problem you will show that Corollary 7.43 actually follows directly
from Corollary 7.44.
(a) Consider the F 2-linear equation v1 + v2 + v3 = 0. Exhibit a list of 4
clauses (i.e., logical ORs of literals) over the variables such that if the
equation is satisﬁed, then so are all 4 clauses, but if the equation is
not satisﬁed, then at most 3 of the clauses are. Do the same for the
equation v1 + v2 + v3 = 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.5. Exercises and notes 201

(b) Suppose that for every δ > 0 there is an efﬁcient algorithm for ( 7
8 +
δ, 1 − δ)-approximating Max-E3-Sat. Give, for every δ > 0, an efﬁcient
algorithm for ( 1
2 + δ, 1 − δ)-approximating Max-E3-Lin.
(c) Alternatively, show how to transform any (α, β)-Dictator-vs.-No-Notables
test using Max-E3-Lin predicates into a ( 3
4 + 1
4 α, β)-Dictator-vs.-No-
Notables test using Max-E3-Sat predicates.

7.29 In this exercise you will prove Theorem 7.41.
(a) Recall the predicate OXR from Exercise 1.1. Fix a small 0 < δ < 1. The
remainder of the exercise will be devoted to constructing a ( 3
4 + δ/4, 1)-
Dictator-vs.-No-Notables test using Max-OXR predicates. Show how
to convert this to a ( 7
8 +δ/8, 1)-Dictator-vs.-No-Notables test using Max-
E3-Sat predicates. (Hint: Similar to Exercise 7.28(c).)
(b) By Exercise 7.23, it sufﬁces to construct a ( 3
4 + δ/4, 1)-Dictator-vs.-No-
Notables test using the OXR predicate assuming f : {−1, 1}n → [−1, 1]
is odd. Håstad tests OXR( f (x), f (y), f (z)) where x, y, z ∈ {−1, 1}n are
chosen randomly as follows: For each i ∈ [n] (independently), with
probability 1 − δ choose (xi, yi, zi) uniformly subject to xi yi zi = −1,
and with probability δ choose (xi, yi, zi) uniformly subject to yi zi = −1.
Show that the probability this test accepts an odd f : {−1, 1}n → [−1, 1]
is
 3
4 − 1
4 Stab−δ[ f ] − 1
4 ∑

S⊆[n] ̂f (S)
2 E
J⊆1−δS[(−1)
|J| ̂f (J)], (7.7)

where J ⊆1−δ S denotes that J is a (1 − δ)-random subset of S in
the sense of Deﬁnition 4.15. In particular, show that dictators are
accepted with probability 1.
(c) Upper-bound (7.7) by

3
4 + δ/4 + 1
4 √
(1 − δ)t + 1
4 ∑

|S|≤t ̂f (S)
2 E
J⊆1−δS[| ̂f (J)|],

or something stronger. (Hint: Cauchy–Schwarz.)
(d) Complete the proof that this is a ( 3
4 + δ/4, 1)-Dictator-vs.-No-Notables
test, assuming f is odd.

7.30 In this exercise you will prove Theorem 7.40. Assume there exists an
(α, β)-Dictator-vs.-No-Notables test T using predicate set Ψ over domain
{−1, 1}. We deﬁne a certain efﬁcient algorithm R, which takes as input
an instance G of Unique-Games(q) and outputs an instance P of Max-
CSP(Ψ). For simplicity we refer to the variables V of the Unique-Games
instance G as “vertices” and its constraints as “edges”. We also assume
that when G is viewed as an undirected graph, it is regular. (By a result of
Khot–Regev [KR08] this assumption is without loss of generality for the
purposes of the Unique Games Conjecture.) The Max-CSP(Ψ) instance P
output by algorithm R will have variable set V × {−1, 1}q, and we write

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

202 7. Property testing, PCPPs, and CSPs

assignments for it as collections of functions ( fv)v∈V , where f : {−1, 1}q →
{−1, 1}. The draw of a random of constraint for P is deﬁned as follows:
• Choose u ∈ V uniformly at random.
• Draw a random constraint from the test T; call it ψ( f (x(1)), . . . , f (x(r))).
• Choose r random “neighbors” v1, . . . , vr of u in G , independently
and uniformly. (By a neighbor of u, we mean a vertex v such that
either (u, v) or (v, u) is the scope of a constraint in G .) Since G ’s
constraints are bijective, we may assume that the associated scopes
are (u, v1), . . . , (u, vr) with bijections π1, . . . , πr : [q] → [q].
• Output the constraint ψ( f π1
v1 (x(1)), . . . , ψ( f πr
vr (x(r))), where we use
the permutation notation f π from Exercise 1.30.
(a) Suppose Opt(G ) ≥ 1 − δ. Show that there is an assignment for P with
value at least β − O(δ) in which each fv is a dictator. (You will use
regularity of G here.) Thus Opt(P ) ≥ β − O(δ).
(b) Given an assignment F = ( fv)v∈V for P , introduce for each u ∈ V the
function gu : {−1, 1}q → [−1, 1] deﬁned by g(x) = Ev[ f π
v (x)], where v is
a random neighbor of u in G and π is the associated constraint’s per-
mutation. Show that ValP (F) = Eu∈V [ValT (gu)] (using the deﬁnition
from Exercise 7.22).
(c) Fix an ϵ > 0 and suppose that ValP (F) ≥ s + 2λ(ϵ), where λ is the
“rejection rate” associated with T. Show that for at least a λ(ϵ)-fraction
of vertices u ∈ V , the set NbrNotableu = {i ∈ [q] : Inf(1−ϵ)
i [gu] > ϵ} is
nonempty.
(d) Show that for any u ∈ V , i ∈ [q] we have E[Inf(1−ϵ)
π−1(i)[ fv]] ≥ Inf(1−ϵ)
i [gu],
where v is a random neighbor of u and π is the associated constraint’s
permutation. (Hint: Exercise 2.48.)
(e) For v ∈ V , deﬁne also the set Notableu = {i ∈ [q] : Inf
(1−ϵ)
i [ fv] ≥ ϵ/2}.
Show that if i ∈ NbrNotableu, then Prv[π
−1(i) ∈ Notablev] ≥ ϵ/2, where
v and π are as in the previous part.
(f ) Show that for every u ∈ V we have |Notableu ∪NbrNotableu| ≤ O(1/ϵ2).
(Hint: Proposition 2.54.)
(g) Consider the following randomized assignment for G (see Exericse 7.20):
for each u ∈ V , give it the uniform distribution on Notableu∪NbrNotableu
(if this set is nonempty; otherwise, give it an arbitrary labeling). Show
that this randomized assignment has value Ω(λ(ϵ)ϵ5).
(h) Conclude Theorem 7.40, where “UG-hard” means “NP-hard assuming
the Unique Games Conjecture”.

7.31 Technically, Exercise 7.30 has a small bug: Since a Dictator-vs.-No-Notables
test using predicate set Ψ is allowed to use duplicate query strings in its
predicates (see Remark 7.38), the reduction in the previous exercise does
not necessarily output instances of Max-CSP(Ψ) because our deﬁnition
of CSPs requires that each scope consist of distinct variables. In this

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.5. Exercises and notes 203

exercise you will correct this bug. Let M ∈ N + and suppose we modify
the algorithm R from Exercise 7.30 to a new algorithm R′, producing an
instance P ′ with variable set V × [M] × {−1, 1}q. We now think of assign-
ments to P ′ as M-tuples of functions f 1
v , . . . , f M
v , one tuple for each v ∈ V .
Further, thinking of P as a function tester, we have P ′ act as follows:
Whenever P is about to query fv(x), we have P ′ instead query f j
v (x) for
a uniformly random j ∈ [M].
(a) Show that Opt(P ) = Opt(P ′).
(b) Show that if we delete all constraints in P ′ for which the scope con-
tains duplicates, then Opt(P ′) changes by at most r2/M, where r is
the maximum arity of a constraint in Ψ.
(c) Show that the deleted version of P ′ is a genuine instance of Max-
CSP(Ψ). Since the constant r2/M can be arbitrarily small, this cor-
rects the bug in Exercise 7.30’s proof of Theorem 7.40.

Notes. The study of property testing was initiated by Rubinfeld and Su-
dan [RS96] and signiﬁcantly expanded by Goldreich, Goldwasser, and Ron
[GGR98]; the stricter notion of local testability was introduced (in the context
of error-correcting codes) by Friedl and Sudan [FS95]. The ﬁrst local tester
for dictatorship was given by Bellare, Goldreich, and Sudan [BGS95, BGS98]
(as in Exercise 7.8); it was later rediscovered by Parnas, Ron, and Samorod-
nitsky [PRS01, PRS02]. The relevance of Arrow’s Theorem to testing dicta-
torship was pointed out by Kalai [Kal02].

The idea of assisting testers by providing proofs grew out of complexity-
theoretic research on interactive proofs and PCPs; see the early work Ergün,
Kumar, and Rubinfeld [EKR99] and the references therein. The speciﬁc
deﬁnition of PCPPs was introduced independently by Ben-Sasson, Goldreich,
Harsha, Sudan, and Vadhan [BSGH
+04] and by Dinur and Reingold [DR04]
in 2004. Both of these works obtained the PCPP Theorem, relying on the
fact that previous literature essentially already gave PCPP reductions of
exponential (or greater) proof length: Ben-Sasson et al. [BSGH+04] observed
that Theorem 7.19 can be obtained from Arora et. al. [ALM
+98] (their proof is
Exercise 7.18), while Dinur and Reingold [DR04] pointed out that the slightly
easier Theorem 7.18 can be extracted from the work of Bellare, Goldreich,
and Sudan [BGS98]. The proof we gave for Theorem 7.16 is inspired by the
presentation in Dinur [Din07].

The PCP Theorem and its stronger forms (the PCPP Theorem and Theo-
rem 7.20) have a somewhat remarkable consequence. Suppose a researcher
claims to prove a famous mathematical conjecture, say, “P ̸= NP”. To ensure
maximum conﬁdence in correctness, a journal might request the researcher
submit a formalized proof, suitable for a mechanical proof-checking system.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

204 7. Property testing, PCPPs, and CSPs

If the submitted formalized proof w is a Boolean string of length n, the proof-
checker will be implementable by a circuit C of size O(n). Notice that the
string property C decided by C is nonempty if and only if there exists a
(length-n) proof of P ̸= NP. Suppose the journal applies Theorem 7.20 to C and
requires the researcher submit the additional proof Π of length n · polylog(n).
Now the journal can run a rather amazing testing algorithm, which reads
just 3 bits of the submitted proof (w, Π). If the researcher’s proof of P ̸= NP
is correct then the test will accept with probability 1. On the other hand, if
the test accepts with probability at least 1 − γ (where γ is the rejection rate
in Theorem 7.20), then w must be 1-close to the set of strings accepted by C.
This doesn’t necessarily mean that w is a correct proof of P ̸= NP – but it does
mean that C is nonempty, and hence a correct proof of P ̸= NP exists! By
querying a larger constant number of bits from (w, Π) as in Exercise 7.1, say,
⌈30/γ⌉ bits, the journal can become 99.99% convinced that indeed P ̸= NP.

CSPs are very widely studied in computer science; it is impossible to sur-
vey the topic here. In the case of Boolean CSPs various monographs [CKS01,
KSTW01] contain useful background regarding complexity theory and ap-
proximation algorithms. The notion of approximation algorithms and the de-
randomized ( 7
8 , 1)-approximation algorithm for Max-E3-Sat (Proposition 7.36,
Exercise 7.21) are due to Johnson [Joh74]. Incidentally, there is also an
efﬁcient ( 7
8 , 1)-approximation algorithm for Max-3-Sat [KZ97], but both the
algorithm and its analysis are extremely difﬁcult, the latter requiring com-
puter assistance [Zwi02].

Håstad’s hardness theorems appeared in 2001 [Hås01b], building on ear-
lier work [Hås96, Hås99]. Håstad [Hås01b] also proved NP-hardness of
( 1
p + δ, 1 − δ)-approximating Max-E3-Lin(mod p) (for p prime) and of ( 7
8 , 1)-
approximating Max-CSP({NAE4}), both of which are optimal. Using tools due
to Trevisan et al. [TSSW00], Håstad also showed NP-hardness of ( 11
16 + δ, 3
4 )-
approximating Max-Cut, which is still the best known such result. The
best known inapproximability result for Unique-Games(q) is NP-hardness of
( 3
8 + q−Θ(1), 1
2 )-approximation [OW12]. Khot’s inﬂuential Unique Games Con-
jecture dates from 2002 [Kho02]; the peculiar name has its origins in a work
of Feige and Lovász [FL92]. The generic Theorem 7.40, giving UG-hardness
from Dictator-vs.-No-Notables tests, is essentially from Khot et al. [KKMO07];
the ﬁrst explicit proof appearing in print may be due to Austrin [Aus08]. (We
remark that the terminology “Dictator-vs.-No-Notables test” is not standard.)
If one is willing to assume the Unique Games Conjecture, there is an almost-
complete theory of optimal inapproximability due to Raghavendra [Rag09].
Many more inapproximability results, with and without the Unique Games
Conjecture, are known; for some surveys, see those of Khot [Kho05, Kho10a,
Kho10b].
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

7.5. Exercises and notes 205

As mentioned, Exercise 7.8 is due to Bellare, Goldreich, and Sudan [BGS95]
and to Parnas, Ron, and Samorodnitsky [PRS01]. The technique described in
Exercise 7.21 is known as the Method of Conditional Expectations. The trick
in Exercise 7.23 is closely related to the notion of “folding” from the theory of
PCPs. The bug described in Exercise 7.31 is rarely addressed in the literature;
the trick used to overcome it appears in, e.g., Arora et al. [ABH+05].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 8

Generalized domains

So far we have studied functions f : {0, 1}n → R . What about, say, f : {0, 1, 2}n →
R ? In fact, very little of what we’ve done so far depends on the domain be-
ing {0, 1}n; what it has mostly depended on is our viewing the domain as a
product probability distribution. Indeed, much of analysis of Boolean func-
tions carries over to the case of functions f : Ω1 × · · · × Ωn → R where the
domain has a product probability distribution π1 ⊗ · · · ⊗ πn. There are two
main exceptions: the “derivative” operator Di does not generalize to the case
when |Ωi| > 2 (though the Laplacian operator Li does), and the important
notion of hypercontractivity (introduced in Chapter 9) depends strongly on
the probability distributions πi.

In this chapter we focus on the case where all the Ωi’s are the same, as
are the πi’s. (This is just to save on notation; it will be clear that everything
we do holds in the more general setting.) Important classic cases include
functions on the p-biased hypercube (Section 8.4) and functions on abelian
groups (Section 8.5). For the issue of generalizing the range of functions – e.g.,
studying functions f : {0, 1, 2}n → {0, 1, 2} – see Exercise 8.33.

8.1. Fourier bases for product spaces

We will now begin to discuss functions on (ﬁnite) product probability spaces.

Deﬁnition 8.1. Let (Ω, π) be a ﬁnite probability space with |Ω| ≥ 2 and as-
sume π has full support. For n ∈ N + we write L2(Ωn, π⊗n) for the (real) inner
product space of functions f : Ωn → R , with inner product

〈 f , g〉 = E
x∼π⊗n[ f (x)g(x)].

Here π⊗n denotes the product probability distribution on Ωn.
 207

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

208 8. Generalized domains

Example 8.2. A simple example to keep in mind is Ω = {a, b, c} with π(a) =
π(b) = π(c) = 1/3. Here a, b, and c are simply abstract set elements.

We can (and will) generalize to nondiscrete probability spaces, and to
complex inner product spaces. However, we will keep to the above deﬁnition
for now.

Notation 8.3. We will write π1/2 for the uniform probability distribution
on {−1, 1}. Thus so far in this book we have been studying functions in
L2({−1, 1}n, π⊗n
1/2). For simplicity, we will write this as L2({−1, 1}n).

Notation 8.4. Much of the notation we used for L2({−1, 1}n) extends naturally
to the case of L2(Ωn, π⊗n): e.g., ∥ f ∥p = Ex∼π⊗n [| f (x)|p]1/p, or the restriction
notation from Chapter 3.3.

As we described in Chapter 1.4, the essence of Boolean Fourier analysis
is in deriving combinatorial properties of a Boolean function f : {−1, 1}n →
R from its coefﬁcients over a particular basis of L2({−1, 1}n), the basis of
parity functions. We would like to achieve the same thing more generally for
functions in L2(Ωn, π⊗n). We begin by considering vector space bases more
generally.

Deﬁnition 8.5. Let |Ω| = m. The indicator basis (or standard basis) for
L2(Ω, π) is just the set of m indicator functions (1x)x∈Ω, where

1x(y) =
 {
1 if y = x,

0 if y ̸= x.

Fact 8.6. The indicator basis is indeed a basis for L2(Ω, π) since the functions
(1x)x∈Ω are nonzero, spanning, and orthogonal. Hence dim(L2(Ω, π)) = m.

We will usually ﬁx Ω and π and then consider L2(Ωn, π⊗n) for n ∈ N +.
Applying the above deﬁnition gives us an indicator basis (1x)x∈Ωn for the mn-
dimensional space L2(Ωn, π⊗n). The representation of f ∈ L2(Ω, π) in this
basis is just f = ∑x∈Ω f (x)1x. This is not very interesting; the coefﬁcients are
just the values of f so they don’t tell us anything new about the function. We
would like a different basis that will generate useful “Fourier formulas” as in
Chapter 1.4.

For inspiration, let’s look critically at the familiar case of L2({−1, 1}n).
Here we used the basis of all parity functions, χS(x) = ∏i∈S xi. It will be
helpful to think of the basis function χS : {−1, 1}n → R as follows: Identify S
with its 0-1 indicator vector and write

χS(x) = n∏

i=1 φSi (xi), where φ0 ≡ 1, φ1 = id.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.1. Fourier bases for product spaces 209

(Here id is just the identity map id(b) = b.) We will identify three properties
of this basis which we’d like to generalize.

First, the parity basis is a product basis. We can break down its “prod-
uct structure” as follows: For each coordinate i ∈ [n] of the product domain
{−1, 1}n, the set {1, id} is a basis for the 2-dimensional space L2({−1, 1}, π1/2).
We then get a basis for the 2n-dimensional product space L2({−1, 1}n) by tak-
ing all possible n-fold products. More generally, suppose we are given an
inner product space L2(Ω, π) with |Ω| = m. Let φ0, . . . , φm−1 be any basis for
this space. Then the set of all products φi1 φi2 · · · φi n (0 ≤ i j < m) forms a basis
for the space L2(Ωn, π⊗n).

Second, it is convenient that the parity basis is orthonormal. We will later
check that if a basis φ0, . . . , φm−1 for L2(Ω, π) is orthonormal, then so too is
the associated product basis for L2(Ωn, π⊗n). This relies on the fact that π⊗n

is the product distribution. For example, the parity basis for L2({−1, 1}n)
is orthonormal because the basis {1, id} for L2({−1, 1}, π1/2) is orthonormal:
E[12] = E[x2
i ] = 1, E[1 · xi] = 0. Orthonormality is the property that makes
Parseval’s Theorem hold; in the general context, this means that if f ∈ L2(Ω, π)
has the representation ∑m−1
i=0 ciφi then E[ f 2] = ∑m−1
i=0 c2
i .

Finally, the parity basis contains the constant function 1. This fact leads
to several of our pleasant Fourier formulas. In particular, when you take
an orthonormal basis φ0, . . . , φm−1 for L2(Ω, π) which has φ0 ≡ 1, then 0 =
〈φ0, φi〉 = Ex∼π[φi(x)] for all i > 0. Hence if f ∈ L2(Ω, π) has the expansion
f = ∑m−1
i=0 ciφi, then E[ f ] = c0 and Var[ f ] = ∑i>0 c2
i .

We encapsulate the second and third properties with a deﬁnition:

Deﬁnition 8.7. A Fourier basis for an inner product space L2(Ω, π) is an
orthonormal basis φ0, . . . , φm−1 with φ0 ≡ 1.

Example 8.8. For each n ∈ N +, the 2n parity functions (χS)S⊆[n] form a
Fourier basis for L2({−1, 1}n, π⊗n
1/2).

Remark 8.9. A Fourier basis for L2(Ω, π) always exists because you can ex-
tend the set {1} to a basis and then perform the Gram–Schmidt process. On the
other hand, Fourier bases are not unique. Even in the case of L2({−1, 1}, π1/2)
there are two possibilities: the basis {1, id} and the basis {1, −id}.

Example 8.10. In the case of Ω = {a, b, c} with π(a) = π(b) = π(c) = 1/3, one
possible Fourier basis (see Exercise 8.4) is

φ0 ≡ 1, φ1(a) = +
p
2
φ1(b) = −
p
2/2
φ1(c) = −
p
2/2,
 φ2(a) = 0
φ2(b) = +
p
6/2,
φ2(c) = −
p
6/2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

210 8. Generalized domains

As mentioned, given a Fourier basis for L2(Ω, π) you can construct a
Fourier basis for any L2(Ωn, π⊗n) by “taking all n-fold products”. To make
this precise we need some notation.

Deﬁnition 8.11. An n-dimensional multi-index is a tuple α ∈ N n. We write

supp(α) = {i : αi ̸= 0}, #α = |supp(α)|, |α| = n∑

i=1 αi.

We may write α ∈ N n
<m when we want to emphasize that each αi ∈ {0, 1, . . . , m−
1}.

Deﬁnition 8.12. Given functions φ0, . . . , φm−1 ∈ L2(Ω, π) and a multi-index
α ∈ N n
<m, we deﬁne φα ∈ L2(Ωn, π⊗n) by

φα(x) = n∏

i=1 φαi (xi).

Now we can show that products of Fourier bases are Fourier bases.

Proposition 8.13. Let φ0, . . . , φm−1 be a Fourier basis for L2(Ω, π). Then the
collection (φα)α∈N n
<m is a Fourier basis for L2(Ωn, π⊗n) (with the understanding
that α = (0, 0, . . . , 0) indexes the constant function 1).

Proof. First we check orthonormality. For any multi-indices α, β ∈ N n
<m we
have

〈φα, φβ〉 = E
x∼π⊗n[φα(x) · φβ(x)]

= E
x∼π⊗n
[ n∏

i=1 φαi (xi) · n∏

i=1 φβi (xi)]

= n∏

i=1 E
xi∼π[φαi (xi) · φβi (xi)] (since π⊗n is a product distribution)

= n∏

i=1 1{αi=βi} (since {φ0, . . . , φm−1} is orthonormal)

= 1{α=β}.

This conﬁrms that the collection (φα)α∈N n
<m is orthonormal, and consequently
linearly independent. It is therefore also a basis because it has cardinality mn,
which we know is the dimension of L2(Ωn, π⊗n) (see Fact 8.6). □

Given a product Fourier basis as in Proposition 8.13, we can express any
f ∈ L2(Ωn, π⊗n) as a linear combination of basis functions. We will write ̂f (α)
for the “Fourier coefﬁcient” on φα in this expression.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.2. Generalized Fourier formulas 211

Deﬁnition 8.14. Having ﬁxed a Fourier basis φ0, . . . , φm−1 for L2(Ω, π), every
f ∈ L2(Ωn, π⊗n) is uniquely expressible as

f = ∑

α∈N n
<m
 ̂f (α)φα.

This is the Fourier expansion of f with respect to the basis. The real number
̂f (α) is called the Fourier coefﬁcient of f on α and it satisﬁes

̂f (α) = 〈 f , φα〉.

Example 8.15. Fix the Fourier basis as in Example 8.10. Let f : {a, b, c}
2 →
{0, 1} be the function which is 1 if and only if both inputs are c. Then you can
check (Exercise 8.5) that

f = 1
9 − p
2
18 φ(1,0)− p
6
18 φ(2,0)− p
2
18 φ(0,1)− p
6
18 φ(0,2)+ 1
18 φ(1,1)+ p
12
36 φ(2,1)+ p
12
36 φ(1,2)+ 1
6 φ(2,2).

The notation ̂f (α) may seem poorly chosen because it doesn’t show the de-
pendence on the basis. However, the Fourier formulas we develop in the next
section will have the property that they are the same for every product Fourier
basis. We will show a basis-independent way of developing the formulas in
Section 8.3.

8.2. Generalized Fourier formulas

In this section we will revisit a number of combinatorial/probabilistic no-
tions and show that for functions f ∈ L2(Ωn, π⊗n), these notions have familiar
Fourier formulas that don’t depend on the Fourier basis.

The orthonormality of Fourier bases gives us some formulas almost imme-
diately:

Proposition 8.16. Let f , g ∈ L2(Ωn, π⊗n). Then for any ﬁxed product Fourier
basis, the following formulas hold:

E[ f ] = ̂f (0)

E[ f 2] = ∑

α∈N n
<m
 ̂f (α)2 (Parseval)

Var[ f ] = ∑

α̸=0 ̂f (α)
2

〈 f , g〉 = ∑

α∈N n
<m
 ̂f (α) ̂g(α) (Plancherel)

Cov[ f , g] = ∑

α̸=0 ̂f (α) ̂g(α).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

212 8. Generalized domains

Proof. We verify Plancherel’s Theorem, from which the other identities follow
(Exercise 8.6):
 〈 f , g〉 = 〈 ∑

α∈N n
<m
 ̂f (α)φα, ∑

β∈N n
<m ̂g(β)φβ〉

= ∑

α,β∈N n
<m
 ̂f (α) ̂g(β)〈φα, φβ〉

= ∑

α∈N n
<m
 ̂f (α) ̂g(α)

by orthonormality of (φα)α∈N n
<m . □

We now give the key deﬁnition for developing basis-independent Fourier
expansions. In the case of L2({−1, 1}) this deﬁnition appeared already in
Exercise 3.28.

Deﬁnition 8.17. Let J ⊆ [n] and write J = [n] \ J. Given f ∈ L2(Ωn, π⊗n), the
projection of f on coordinates J is the function f ⊆J ∈ L2(Ωn, π⊗n) deﬁned by

f ⊆J(x) = E
x′∼π⊗J[ f (xJ, x′)],

where xJ ∈ ΩJ denotes the values of x in the J-coordinates. In other words,
f ⊆J(x) is the expectation of f when the J-coordinates of x are rerandomized.
Note that we take f ⊆J to have Ωn as its domain, even though it only depends
on the coordinates in J.

Forming f ⊆J is indeed the application of a projection linear operator to f ,
namely the expectation over J operator, EJ. We take this as the deﬁnition of
the operator: EJ f = f ⊆J. When J = {i} is a singleton we write simply Ei.

Remark 8.18. This deﬁnition of Ei is consistent with Deﬁnition 2.23. You
are asked to verify that EJ is indeed a projection, self-adjoint linear operator
in Exercise 8.7.

Proposition 8.19. Let J ⊆ [n] and f ∈ L2(Ωn, π⊗n). Then for any ﬁxed product
Fourier basis, f ⊆J = ∑

α∈N n
<m
supp(α)⊆J
 ̂f (α) φα.

Proof. Since EJ is a linear operator, it sufﬁces to verify for all α that

φ⊆J
α =
 {
φα if supp(α) ⊆ J,

0 otherwise.

If supp(α) ⊆ J, then φα does not depend on the coordinates J; hence indeed
φ⊆J
α = φα. So suppose supp(α) ̸⊆ J. Since φα(x) = (∏i∈J φαi (xi))(∏i∈J φαi (xi))
,
we can write φα = φαJ · φαJ , where φαJ depends only on the coordinates in J,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.2. Generalized Fourier formulas 213

φαJ depends only on the coordinates in J, and E[φαJ ] = 0 precisely because
supp(α) ̸⊆ J. Thus for every x ∈ Ωn,

φ⊆J
α (x) = E
x′∼π⊗J[φαJ (xJ)φαJ (x′)] = φαJ (xJ) · E
x′∼π⊗J[φαJ (x′)] = 0

as needed. □

Corollary 8.20. Let f ∈ L2(Ωn, π⊗n) and ﬁx a product Fourier basis. If f
depends only on the coordinates in J ⊆ [n] then ̂f (α) = 0 whenever supp(α) ̸⊆ J.

Proof. This follows from Proposition 8.19 because f = f ⊆J. □

Corollary 8.21. Let i ∈ [n] and f ∈ L2(Ωn, π⊗n). Then for any ﬁxed product
Fourier basis, Ei f = ∑

α:αi=0 ̂f (α) φα.

Let us now deﬁne inﬂuences for functions f ∈ L2(Ωn, π⊗n). In the case of
Ω = {−1, 1}, our deﬁnition of Infi[ f ] from Chapter 2.2 was E[(Di f )
2]. However,
the notion of a derivative operator does not make sense for more general
domains Ω. In fact, even in the case of Ω = {−1, 1} it isn’t a basis-invariant

notion: the choice of f (x(i7→1))− f (x(i7→−1))
2 rather than f (x(i7→−1))− f (x(i7→1))
2 is inherently
arbitrary. Instead we can fall back on the Laplacian operators, and take the
identity Infi[ f ] = 〈 f , Li f 〉 from Proposition 2.26 as a deﬁnition.

Deﬁnition 8.22. Let i ∈ [n] and f ∈ L2(Ωn, π⊗n). The ith coordinate Laplacian
operator Li is the self-adjoint, projection linear operator deﬁned by

Li f = f − Ei f .

The inﬂuence of coordinate i on f is deﬁned to be

Infi[ f ] = 〈 f , Li f 〉 = 〈Li f , Li f 〉.

The total inﬂuence of f is deﬁned to be I[ f ] = ∑n
i=1 Infi[ f ].

You can think of Li f as “the part of f which depends on the ith coordinate”.

Proposition 8.23. Let i ∈ [n] and f ∈ L2(Ωn, π⊗n). Then for any ﬁxed product
Fourier basis,

Li f = ∑

α:αi̸=0 ̂f (α) φα, Infi[ f ] = ∑

α:αi̸=0 ̂f (α)
2, I[ f ] = ∑

α #α · ̂f (α)
2,

Proof. The ﬁrst formula is immediate from Corollary 8.21, the second from
Plancherel, and the third from summing over i. □

Exercise 8.9 asks you to verify the following formulas (cf. Exercise 2.21),
which are often useful for computations:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

214 8. Generalized domains

Proposition 8.24. Let i ∈ [n] and f ∈ L2(Ωn, π⊗n). Then

Infi[ f ] = E
x∼π⊗n[Var
x′
i∼π[ f (x1, . . . , xi−1, x′
i, xi+1, . . . , xn)]].

If furthermore f ’s range is {−1, 1}, then

Infi[ f ] = E[|Li f |] = 2 Pr
x∼π⊗n
x′
i∼π
 [ f (x) ̸= f (x1, . . . , xi−1, x′
i, xi+1, . . . , xn)].

Example 8.25. Let’s continue Example 8.15, in which {a, b, c} has the uniform
distribution and f : {a, b, c}
2 → {0, 1} is 1 if and only if both inputs are c. We
compute Inf1[ f ] two ways. Using Proposition 8.24 we have Var[ f (x1, a)] =
Var[ f (x1, b)] = 0 and Var[ f (x1, c)] = 1
3 · 2
3 = 2
9 (because f (x1, c) is Bernoulli with
parameter 1
3 ); thus Inf1[ f ] = 1
3 · 2
9 = 2
27 . Alternatively, using the formula from
Proposition 8.23 as well as the Fourier expansion from Example 8.15, we can
compute Inf1[ f ] = (− p
2
18 )
2 + (− p
6
18 )2 + ( 1
18 )
2 + ( p
12
36 )
2 + ( p
12
36 )
2 + ( 1
6 )
2 = 2
27 .

Next, we straightforwardly extend our deﬁnitions of the noise operator
and noise stability to general product spaces.

Deﬁnition 8.26. Fix a ﬁnite product probability space (Ωn, π⊗n). For ρ ∈ [0, 1]
and x ∈ Ωn we write y ∼ Nρ(x) to denote that y ∈ Ωn is randomly chosen as
follows: For each i ∈ [n] independently,

yi =
 {xi with probability ρ,

drawn from π with probability 1 − ρ.

If x ∼ π⊗n and y ∼ Nρ(x), we say that (x, y) is a ρ-correlated pair under π⊗n.
(This deﬁnition is symmetric in x and y.)

Deﬁnition 8.27. For a ﬁxed space L2(Ωn, π⊗n) and ρ ∈ [0, 1], the noise oper-
ator with parameter ρ is the linear operator Tρ on functions f ∈ L2(Ωn, π⊗n)
deﬁned by
 Tρ f (x) = E
y∼Nρ(x)
[ f (y)].

The noise stability of f at ρ is

Stabρ[ f ] = 〈 f , Tρ f 〉 = E
(x,y) ρ-correlated
under π⊗n [ f (x) f (y)].

Proposition 8.28. Let ρ ∈ [0, 1] and let f ∈ L2(Ωn, π⊗n). Then for any ﬁxed
product Fourier basis,

Tρ f = ∑

α∈N n
<m ρ#α ̂f (α) φα, Stabρ[ f ] = ∑

α∈N n
<m ρ#α ̂f (α)
2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.2. Generalized Fourier formulas 215

Proof. Let J denote a ρ-random subset of [n]; i.e., J is formed by including
each i ∈ [n] independently with probability ρ. Then by deﬁnition Tρ f (x) =
EJ[ f ⊆J(x)], and so from Proposition 8.19 we get

Tρ f (x) = E
J [ f ⊆J(x)] = E
J
 [ ∑

α∈N n
<m
supp(α)⊆J
 ̂f (α) φα(x)] = ∑

α∈N n
<m ρ#α ̂f (α) φα(x),

since for a ﬁxed α, the probability of supp(α) ⊆ J is ρ#α. The formula for
Stabρ[ f ] now follows from Plancherel. □

Remark 8.29. The ﬁrst formula in this proposition may be used to extend
the deﬁnition of Tρ f to values of ρ outside [0, 1].

We also deﬁne ρ-stable inﬂuences. The factor of ρ−1 in our deﬁnition is
for consistency with the L2({−1, 1}n) case.

Deﬁnition 8.30. For f ∈ L2(Ωn, π⊗n), ρ ∈ (0, 1], and i ∈ [n], the ρ-stable inﬂu-
ence of i on f is
 Inf
(ρ)
i [ f ] = ρ−1Stabρ[Li f ] = ∑

α:αi̸=0 ρ#α−1 ̂f (α)
2.

We also deﬁne I(ρ)[ f ] = ∑n
i=1 Inf
(ρ)
i [ f ].

Just as in the case of L2({−1, 1}n) we can use stable inﬂuences to deﬁne
the “notable” coordinates of a function, of which there is a bounded quantity.
A verbatim repetition of the proof of Proposition 2.54 yields the following
generalization:

Proposition 8.31. Suppose f ∈ L2(Ωn, π⊗n) has Var[ f ] ≤ 1. Given 0 < δ < 1,
0 < ϵ ≤ 1, let J = {i ∈ [n] : Inf(1−δ)
i [ f ] ≥ ϵ}. Then |J| ≤ 1
δϵ .

We end this section by discussing the “degree” of functions on general
product spaces. For f ∈ L2({−1, 1}n) the Fourier expansion is a real polynomial;
this yields an obvious deﬁnition for degree. But for general f ∈ L2(Ωn, π⊗n)
the domain is just an abstract set so we need to look for a more intrinsic
deﬁnition. We take our cue from Exercise 1.10(b):

Deﬁnition 8.32. Let f ∈ L2(Ωn, π⊗n) be nonzero. The degree of f , written
deg( f ), is the least k ∈ N such that f is a sum of k-juntas (functions depending
on at most k coordinates).

Proposition 8.33. Let f ∈ L2(Ωn, π⊗n) be nonzero. Then for any ﬁxed product
Fourier basis we have deg( f ) = max{#α : ̂f (α) ̸= 0}.

Proof. The inequality deg( f ) ≤ max{#α : ̂f (α) ̸= 0} is immediate from the
Fourier expansion: f = ∑

α: ̂f (α)̸=0 ̂f (α) φα

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

216 8. Generalized domains

and each function ̂f (α) φα depends on at most #α coordinates. For the reverse
inequality, suppose f = g1 + · · · + gm where each g i depends on at most k
coordinates. By Corollary 8.20 each g i has its Fourier support on functions φα
with #α ≤ k. But ̂f (α) = ̂g1(α) + · · · + ̂gm(α), so the same is true of f . □

8.3. Orthogonal decomposition

In this section we describe a basis-free kind of “Fourier expansion” for func-
tions on general product domains. We will refer to it as the orthogonal decom-
position of f ∈ L2(Ωn, π⊗n), though it goes by several other names in the liter-
ature: e.g., Hoeffding decomposition, Efron–Stein decomposition, or ANOVA
decomposition. The general idea is to express

f = ∑

S⊆[n] f =S (8.1)

where each function f =S ∈ L2(Ωn, π⊗n) gives the “contribution to f coming
from coordinates S (but not from any subset of S)”.

To make this more precise, let’s start with the familiar case of f : {−1, 1}n →
R . Here it is possible to deﬁne the functions f =S : {−1, 1}n → R simply by
f =S = ̂f (S) χS. (Later we will give an equivalent deﬁnition that doesn’t in-
volve the Fourier basis.) This deﬁnition satisﬁes (8.1) as well as the following
two properties:

(1) f =S depends only on the coordinates in S.

(2) If T ⊊ S and g is a function depending only on the coordinates in T,
then 〈 f =S, g〉 = 0.

These properties describe what we mean precisely when we say that f =S is
the “contribution to f coming from coordinates S (but not from any subset
of S)”. Furthermore, decomposition (8.1) is orthogonal, meaning 〈 f =S, f =T 〉 =
0 whenever S ̸= T.

To make this deﬁnition basis-free, recall the “projection of f onto coordi-
nates J”, f ⊆J, from Exercise 3.28 and Deﬁnition 8.17. You can think of f ⊆J

as the “contribution to f coming from coordinates J (collectively)”. It has a
probabilistic deﬁnition not depending on any basis, and with the deﬁnition
f =S = ̂f (S) χS we have from Exercise 3.28 or Proposition 8.19 that

f ⊆J = ∑

S⊆J f =S. (8.2)

It is precisely by inverting (8.2) that we can give a basis-free deﬁnition of the
functions f =S.

Let’s do this inversion for a general f ∈ L2(Ωn, π⊗n). The projection func-
tions f ⊆J ∈ L2(Ωn, π⊗n) can be deﬁned as in Deﬁnition 8.17. If we want (8.2)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.3. Orthogonal decomposition 217

to hold for J = ; then we should deﬁne

f =; = f ⊆;

(which is the constant function equal to E[ f ]). Given this, if we want (8.2) to
hold for singleton sets J = { j}, then we need

f ⊆{ j} = f =; + f ={ j} ⇐⇒ f ={ j} = f ⊆{ j} − f ⊆;.

In other words,
 f ={ j}(x) = E
x∼π⊗n[ f | x j = x j] − E
x∼π⊗n[ f (x)].

Notice this function only depends on the input value x j; it measures the
change in expectation of f if you know the value x j. Moving on to sets of
cardinality 2, if we want (8.2) to hold for J = {i, j}, then we need

f ⊆{i, j} = f =; + f ={i} + f ={ j} + f ={i, j}

= f ⊆; + ( f ⊆{i} − f ⊆;) + ( f ⊆{ j} − f ⊆;) + f ={i, j}

and hence
 f ={i, j} = f ⊆{i, j} − f ⊆{i} − f ⊆{ j} + f ⊆;.

It’s clear that we can continue this and deﬁne all the functions f =S by the
principle of inclusion-exclusion. To show this deﬁnition leads to an orthogonal
decomposition we will need the following lemma:

Lemma 8.34. Let f , g ∈ L2(Ωn, π⊗n). Assume that f does not depend on any
coordinate outside I ⊆ [n], and g does not depend on any coordinate outside
J ⊆ [n]. Then 〈 f , g〉 = 〈 f ⊆I∩J, g⊆I∩J〉.

Proof. We may assume without loss of generality that I ∪ J = [n]. Given any
x ∈ Ωn we can break it into the parts (xI∩J, xI\J, xJ\I ). We then have

〈 f , g〉 = E
xI∩J ,xI\J ,xJ\I[ f (xI∩J, xI\J) · g(xI∩J, xJ\I )],

where we have abused notation slightly by writing f and g as functions just
of the coordinates on which they actually depend. Since xI\J and xJ\I are
independent, the above equals

E
xI∩J
 [ E
xI\J[ f (xI∩J, xI\J)] · E
xJ\I[g(xI∩J, xJ\I )]] .

But now ExI\J [ f (xI∩J, xI\J)] is nothing more than f ⊆I∩J(xI∩J), and similarly
ExJ\I [g(xI∩J, xJ\I )] = g⊆I∩J(xI∩J). Thus the above equals

E
xI∩J[ f ⊆I∩J(xI∩J) · g⊆I∩J(xI∩J)] = 〈 f ⊆I∩J, g⊆I∩J〉. □

We can now give the main theorem on orthogonal decomposition:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

218 8. Generalized domains

Theorem 8.35. Let f ∈ L2(Ωn, π⊗n). Then f has a unique decomposition as

f = ∑

S⊆[n] f =S

where the functions f =S ∈ L2(Ωn, π⊗n) satisfy the following:

(1) f =S depends only on the coordinates in S.

(2) If T ⊊ S and g ∈ L2(Ωn, π⊗n) depends only on the coordinates in T, then
〈 f =S, g〉 = 0.

This decomposition has the following additional properties:

(3) Condition (2) additionally holds whenever S ̸⊆ T.

(4) The decomposition is orthogonal: 〈 f =S, f =T 〉 = 0 for S ̸= T.

(5) ∑S⊆T f =S = f ⊆T .

(6) For each S ⊆ [n], the mapping f 7→ f =S is a linear operator.

Proof. We ﬁrst show the existence of a decomposition satisfying (1)–(6). We
then show uniqueness for decompositions satisfying (1) and (2). As suggested
above, for each S ⊆ [n] we deﬁne

f =S = ∑

J⊆S(−1)
|S|−|J| f ⊆J,

where the functions f ⊆J ∈ L2(Ωn, π⊗n) are as in Deﬁnition 8.17. Since each f ⊆J

depends only on the coordinates in J, condition (1) certainly holds. It is also
immediate that condition (5) holds by inclusion-exclusion; you are asked to
prove this explicitly in Exercise 8.14. Condition (6) also follows because each
f 7→ f ⊆J is a linear operator, as discussed after Deﬁnition 8.17.

We now verify (2). Assume T ⊊ S and that g ∈ L2(Ωn, π⊗n) only depends
on the coordinates in T. We have

〈 f =S, g〉 = ∑

J⊆S(−1)
|S|−|J|〈 f ⊆J, g〉. (8.3)

Take any i ∈ S \ T and pair up the summands in (8.3) as J′, J′′, where J′ ̸∋ i
and J′′ = J′ ∪ {i}. By Lemma 8.34 we have

〈 f ⊆J′′, g〉 = 〈 f ⊆J′′∩T , g⊆T 〉 = 〈 f ⊆J′∩T , g⊆T 〉,

the latter equality using i ̸∈ T. But the signs (−1)|S|−|J′| and (−1)|S|−|J′′| are
opposite, so the summands in (8.3) cancel in pairs. This shows the sum is 0,
conﬁrming (2).

We complete the existence proof by noting that (2) =⇒ (3) =⇒ (4) (as-
suming (1)). The ﬁrst implication is because 〈 f =S, g〉 = 〈 f =S, g⊆S∩T 〉 when
g depends only on the coordinates in T (Lemma 8.34), and S ∩ T ⊊ S when
S ̸⊆ T. The second implication is because S ̸= T implies either S ̸⊆ T or T ̸⊆ S.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.3. Orthogonal decomposition 219

It remains to prove the uniqueness statement. Suppose f has two repre-
sentations satisfying (1) and (2). By subtracting them we get a decomposition
of the 0 function that satisﬁes (1) and (2); our goal is to show that each func-
tion in this decomposition is the 0 function. We can do this by showing that
any decomposition satisfying (1) and (2) also satisﬁes “Parseval’s Theorem”:
〈 f , f 〉 = ∑S⊆[n] ∥ f =S∥
2
2. But this is an easy consequence of (4), which we just
noted is itself a consequence of (1) and (2). □

We can connect the orthogonal decomposition of f to its expansion under
Fourier bases as follows:

Proposition 8.36. Let f ∈ L2(Ωn, π⊗n) have orthogonal decomposition f =
∑S⊆[n] f =S. Fix any Fourier basis φ0, . . . , φm−1 for L2(Ω, π). Then

f =S = ∑

α∈N n
<m
supp(α)=S
 ̂f (α) φα. (8.4)

Proof. This follows easily from the uniqueness part of Theorem 8.35. If we
take (8.4) as the deﬁnition of functions f =S, it is immediate that ∑S f =S = f
and that f =S depends only on the coordinates in S. Further, if g depends
only on coordinates T ⊊ S, then f =S and g have disjoint Fourier support by
Corollary 8.20; hence 〈 f =S, g〉 = 0 by Plancherel (Proposition 8.16). □

Example 8.37. Let’s compute the orthogonal decomposition of the function
f : {a, b, c}
2 → {0, 1} from Example 8.15. Recall that in this example {a, b, c}
has the uniform distribution and f (x1, x2) = 1 if and only if x1 = x2 = c. First,

f =; = E[ f ] = 1
9 .

Next, for i = 1, 2 we have that f ⊆{i}(x) is 1
3 if xi = c and 0 otherwise; hence

f ={i}(x1, x2) =
 {
+ 2
9 if xi = c,

− 1
9 else.

Finally, it’s easiest to compute f ={1,2} as f − f =; − f ={1} − f ={2}; this yields

f ={1,2}(x1, x2) =
 



+ 4
9 if x1 = x2 = c,

− 2
9 if exactly one of x1, x2 is c,

+ 1
9 if x1, x2 ̸= c.

You can check (Exercise 8.20) that this is consistent with Proposition 8.36 and
the Fourier expansion from Example 8.15.

We can write all of the Fourier formulas from Section 8.2 in terms of the
orthogonal decomposition; e.g.,

〈 f , g〉 = ∑

S⊆[n]
〈 f =S, g=S〉, Infi[ f ] = ∑

S∋i ∥ f =S∥
2
2, Tρ f = ∑

S⊆[n] ρ|S| f =S.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

220 8. Generalized domains

These formulas can be proved either by using the connection from Proposi-
tion 8.36 or by reasoning directly from the deﬁning Theorem 8.35; see Ex-
ercise 8.18. The orthogonal decomposition also gives us the natural way of
stratifying f by degree; we end this section by generalizing some more deﬁni-
tions from Chapter 1.4:

Deﬁnition 8.38. For f ∈ L2(Ωn, π⊗n) and k ∈ N we deﬁne the degree k part
of f to be f =k = ∑
|S|=k f =S and the weight of f at degree k to be Wk[ f ] = ∥ f =k∥
2
2.
We also use notation like f ≤k = ∑
|S|≤k f =S and W
>k[ f ] = ∑
|S|>k ∥ f =S∥
2
2.

8.4. p-biased analysis

Perhaps the most common generalized domain in analysis of Boolean func-
tions is the case of the hypercube with “biased” bits. In this setting we think of
a random input in {−1, 1}n as having each bit independently equal to −1 (True)
with probability p ∈ (0, 1) and equal to 1 (False) with probability q = 1 − p.
(We could also consider different parameters pi for each coordinate; see Ex-
ercise 8.24.) In the notation of the chapter this means L2(Ωn, π⊗n
p ), where
Ω = {−1, 1} and πp is the distribution on Ω deﬁned by πp(−1) = p, πp(1) = q.
This context is often referred to as p-biased Fourier analysis, though it would
be more consistent with our terminology if it were called “µ-biased”, where

µ = E
xi∼πp[xi] = q − p = 1 − 2p.

One of the more interesting features of the setting is that we can ﬁx a combi-
natorial Boolean function f : {−1, 1}n → {−1, 1} and then consider its properties
for various p between 0 and 1; we will discuss this further later in this sec-
tion. We will also sometimes use the abbreviated notation Prπp [·] in place of
Prx∼π⊗n
p [·], and similarly Eπp [·].

The p-biased hypercube is one of the generalized domains where it can
pay to look at an explicit Fourier basis. In fact, since we have |Ω| = 2 there is
a unique Fourier basis {φ0, φ1} (up to negating φ1). For notational simplicity
we’ll write φ instead of φ1 and use “set notation” rather than multi-index
notation:

Deﬁnition 8.39. In the context of p-biased Fourier analysis we deﬁne the
basis function φ : {−1, 1} → R by

φ(xi) = xi − µ

σ ,

where

µ = E
xi∼πp[xi] = q − p = 1 − 2p, σ = stddev
xi∼πp [xi] = √
4pq = 2
pp√
1 − p.

Note that σ2 = 1 − µ2. We also have the formula φ(1) = √p/q, φ(−1) = −
√q/p.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.4. p-biased analysis 221

We will use the notation µ and σ throughout this section. It’s clear that
{1, φ} is indeed a Fourier basis for L2({−1, 1}, πp) because E[φ(xi)] = 0 and
E[φ(xi)
2] = 1 by design.

Deﬁnition 8.40. In the context of L2({−1, 1}n, π⊗n
p ) we deﬁne the product
Fourier basis functions (φS)S⊆[n] by

φS(x) = ∏

i∈S φ(xi).

Given f ∈ L2({−1, 1}n, π⊗n
p ) we write ̂f (S) for the associated Fourier coefﬁcient;
i.e., ̂f (S) = E
x∼π⊗n
p [ f (x) φS(x)].

Thus we have the biased Fourier expansion

f (x) = ∑

S⊆[n] ̂f (S) φS(x).

Although the notation is very similar to that of the classic uniform-distribution
Fourier analysis, we caution that in general,

φSφT ̸= φS△T .

Example 8.41. Let χi ∈ L2({−1, 1}n, π⊗n
p ) be the ith dictator function, χi(x) =
xi, viewed under the p-biased distribution. We have

φ(xi) = xi − µ

σ =⇒ xi = µ + σφ(xi),

and the latter is evidently f ’s (biased) Fourier expansion. That is,

̂χi(;) = µ, ̂χi({i}) = σ, ̂χi(S) = 0 otherwise.

This example lets us see a link between a function’s “usual” Fourier expan-
sion and its biased Fourier expansion. (For more on this, see Exercise 8.25.)
Let’s abuse notation a little by writing simply φi instead of φ(xi). We have
the formulas φi = xi − µ

σ ⇐⇒ xi = µ + σφi, (8.5)

and we can go from the usual Fourier expansion to the biased Fourier expan-
sion simply by plugging in the latter.

Example 8.42. Recall the “selection function” Sel : {−1, 1}
3 → {−1, 1} from
Exercise 1.1(j); Sel(x1, x2, x3) outputs x2 if x1 = −1 and outputs x3 if x1 = 1.
The usual Fourier expansion of Sel is

Sel(x1, x2, x3) = 1
2 x2 + 1
2 x3 − 1
2 x1x2 + 1
2 x1x3.

Using the substitution from (8.5) we get

Sel(x1, x2, x3) = 1
2 (µ + σφ2) + 1
2 (µ + σφ3) − 1
2 (µ + σφ1)(µ + σφ2) + 1
2 (µ + σφ1)(µ + σφ3)

= µ + ( 1
2 − 1
2 µ)σ φ2 + ( 1
2 + 1
2 µ)σ φ3 − 1
2 σ2 φ1φ2 + 1
2 σ2 φ1φ3. (8.6)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

222 8. Generalized domains

Thus if we write Sel
(p) for the selection function thought of as an element of
L2({−1, 1}
3, π⊗3
p ), we have

…Sel
(p)(;) = µ, …Sel
(p)(2) = ( 1
2 − 1
2 µ)σ, …Sel
(p)(3) = ( 1
2 + 1
2 µ)σ,

…Sel
(p)({1, 2}) = − 1
2 σ2, …Sel
(p)({1, 3}) = 1
2 σ2, …Sel
(p)(S) = 0 else.

By the Fourier formulas of Section 8.2 we can deduce, e.g., that E[Sel
(p)] = µ,
Inf1[Sel
(p)] = (− 1
2 σ2)2 + ( 1
2 σ2)
2 = 1
2 σ4, etc.

Let’s codify a piece of notation from this example:

Notation 8.43. Let f : {−1, 1}n → R and let p ∈ (0, 1). We write f (p) for the
function when viewed as an element of L2({−1, 1}n, π⊗n
p ).

We now discuss derivative operators. We would like to deﬁne an opera-
tor Di on L2({−1, 1}n, π⊗n
p ) that acts like differentiation on the biased Fourier
expansion. For example, referring to (8.6) we would like to have

D3Sel
(p) = ( 1
2 + 1
2 µ)σ + 1
2 σ2 φ1.

In general we are seeking ∂
∂φi which, by basic calculus and the relation-
ship (8.5), satisﬁes ∂

∂φi = ∂xi
∂φi · ∂

∂xi = σ · ∂

∂xi .

Recognizing ∂
∂xi as the “usual” ith derivative operator, we are led to the fol-
lowing:

Deﬁnition 8.44. For i ∈ [n], the ith (discrete) derivative operator Di on
L2({−1, 1}n, π⊗n
p ) is deﬁned by

Di f (x) = σ · f (x(i7→1)) − f (x(i7→−1))
2 .

Note that this deﬁnes a different operator for each value of p. We sometimes
write the above deﬁnition as
 Dφi = σ · Dxi .

With respect to the biased Fourier expansion of f ∈ L2({−1, 1}n, π⊗n
p ) the oper-
ator Di satisﬁes
 Di f = ∑

S∋i ̂f (S) φS\{i}. (8.7)

Given this deﬁnition we can derive some additional formulas for inﬂu-
ences, including a generalization of Proposition 2.21:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.4. p-biased analysis 223

Proposition 8.45. Suppose f ∈ L2({−1, 1}n, π⊗n
p ) is Boolean-valued (i.e., has
range {−1, 1}). Then
 Infi[ f ] = σ2 Pr
x∼π⊗n
p [ f (x) ̸= f (x⊕i)]

for each i ∈ [n], and I[ f ] = σ2 E
x∼π⊗n
p [sens f (x)].

If furthermore f is monotone, then Infi[ f ] = σ ̂f (i).

Proof. Using Deﬁnition 8.44’s notation we have

Infi[ f ] = E
πp[(Dφi f )2] = σ2 E
πp[(Dxi f )
2].

Since (Dxi f )2 is the 0-1 indicator that i is pivotal for f , the ﬁrst formula
follows. The second formula follows by summing over i. Finally, when f is
monotone we furthermore have that (Dxi f )2 = Dxi f and hence

Infi[ f ] = σ2 E
πp[Dxi f ] = σ E
πp[Dφi f ] = σ ̂f (i),

as claimed. □

The remainder of this section is devoted to the topic of threshold phenom-
ena in Boolean functions. Much of the motivation for this comes from theory
of random graphs, which we now brieﬂy introduce.

Deﬁnition 8.46. Given an undirected graph G on v ≥ 2 vertices, we identify
it with the string in {True,False}(v
2) which indicates which edges are present
(True) and which are absent (False). We write G (v, p) for the distribution

π⊗(v
2)
p ; this is called the Erd˝os–Rényi random graph model. Note that if we
permute the v vertices of a graph, this induces a permutation on the (v
2
) edges.

A (v-vertex) graph property is a Boolean function f : {True,False}(v
2) → {True,False}
that is invariant under all v! such permutations of its input; colloquially, this
means that f “does not depend on the names of the vertices”.

Graph properties are always transitive-symmetric functions in the sense of
Deﬁnition 2.10.

Example 8.47. The following are all v-vertex graph properties:

Conn(G) = True if G is connected;

3Col(G) = True if G is 3-colorable;

Cliquek(G) = True if G is contains a clique on at least k vertices;

Majn(G) = True (assuming n = (v
2
) is odd) if G has at least (v
2)
/2 edges;

χ[n](G) = True if G has an odd number of edges.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

224 8. Generalized domains

Note that each of these actually deﬁnes a family of Boolean functions, one
for each value of v; this is the typical situation in the study of graph proper-
ties. An example of a function f : {True,False}(v
2) → {True,False} that is not a
graph property is the one deﬁned by f (G) = True if vertex #1 has at least one
neighbor; this f is not invariant under permuting the vertices.

Graph properties which are monotone are particularly nice to study; these
are the ones for which adding edges can never make the property go from True
to False. The properties Conn, Cliquek, and Majn deﬁned above are all mono-
tone, as is ¬3Col. Now suppose we take a monotone graph property, say, Conn.
A typical question in random graph theory would be, “how many edges does a
graph need to have before it is likely to be connected?” Or more precisely, how
does PrG∼G (v,p)[Conn(G) = True] vary as p increases from 0 to 1?

There’s no need to ask this question just for graph properties. Given any
monotone Boolean function f : {True,False}n → {True,False} it is intuitively
clear that when p increases from 0 to 1 this causes Prπp [ f (x) = True] to in-
crease from 0 to 1 (unless f is a constant function). As illustration, we show a
plot of Prπp [ f (x) = True] versus p for the dictator function, AND2, and Maj101.

Figure 8.1. Plot of Prπp [ f (x) = True] versus p for f a dictator (dotted),
f = AND2 (dashed), and f = Maj101 (solid)

The Margulis–Russo Formula quantiﬁes the rate at which Prπp [ f (x) =
True] increases with p; speciﬁcally, it relates the slope of the curve at p to the
total inﬂuence of f under π⊗n
p . To prove the formula we switch to ±1 notation.

Margulis–Russo Formula. Let f : {−1, 1}n → R . Recalling Notation 8.43
and the relation µ = 1 − 2p, we have

d
dµ E[ f (p)] = 1

σ · n∑

i=1 ̂f (p)(i). (8.8)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.4. p-biased analysis 225

In particular, if f : {−1, 1}n → {−1, 1} is monotone, then

d
d p Pr
x∼π⊗n
p [ f (x) = −1] = d
dµ E[ f (p)] = 1

σ2 · I[ f (p)]. (8.9)

Proof. Treating f as a multilinear polynomial over x1, . . . , xn we have

E[ f (p)] = Tµ f (1, . . . , 1) = f (µ, . . . , µ)

(this also follows from Exercise 1.4). By basic calculus,

d
dµ f (µ, . . . , µ) = n∑

i=1 Dxi f (µ, . . . , µ).

But
 Dxi f (µ, . . . , µ) = E[Dxi f (p)] = 1

σ E[Dφi f (p)] = 1

σ ̂f (p)(i),

completing the proof of (8.8). As for (8.9), the second equality follows immedi-
ately from Proposition 8.45. The ﬁrst equality holds because µ = 1 − 2p and
E[ f ] = 1 − 2 Pr[ f = −1]; the two factors of −2 cancel. □

Remark 8.48. If f : {True,False}n → {True,False} is a nonconstant monotone
function, the Margulis–Russo Formula implies that Prπp [ f (x) = True] is a
strictly increasing function of p, because I[ f (p)] is always positive.

Looking again at Figure 8.1 we see that the plot for Maj101 looks very
much like a step function, jumping from nearly 0 to nearly 1 around the
critical value p = 1/2. For Majn, this “sharp threshold at p = 1/2” becomes
more and more pronounced as n increases. This is clearly suggested by the
Margulis–Russo Formula: the derivative of the curve at p = 1/2 is equal to
I[Majn] (the usual, uniform-distribution total inﬂuence), which has the very
large value Θ(pn) (Theorem 2.33). Such sharp thresholds exist for many
Boolean functions; we give some examples:

Example 8.49. In Exercise 8.23 you are asked to show that for every ϵ > 0
there is a C such that

Pr
π1/2−C/pn[Majn = True] ≤ ϵ, Pr
π1/2+C/pn[Majn = True] ≥ 1 − ϵ.

Regarding the Erd˝os–Rényi graph model, the following facts are known:

Pr
G∼G (v,p)[Cliquelog v(G) = True] −−−−→
v→∞
 {
0 if p < 1/4,

1 if p > 1/4.

Pr
G∼G (v,p)[Conn(G) = True] −−−−→
v→∞
 {
0 if p < ln v
v (1 − log log v
log v ),

1 if p > ln v
v (1 + log log v
log v ).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

226 8. Generalized domains

In the above examples you can see that the “jump” occurs at various values
of p. To investigate this phenomenon, we ﬁrst single out the value for which
Prπp [ f (x) = True] = 1/2:

Deﬁnition 8.50. Let f : {True,False}n → {True,False} be monotone and non-
constant. The critical probability for f , denoted pc, is the unique value
in (0, 1) for which Prx∼π⊗n
p [ f (x) = True] = 1/2. We also write qc = 1 − pc,

µc = qc − pc = 1 − 2pc, and σc = √
4pc qc.

In Exercise 8.27 you are asked to verify that pc is well deﬁned.

Looking at the connectivity property from Example 8.49 we see that not
only does Prπp [Conn = True] jump from near 0 to near 1 in an interval of
the form pc ± o(1), it actually makes the jump in an interval of the form
pc(1 ± o(1)). This latter phenomenon is (roughly speaking) what is meant
by a “sharp threshold”. To investigate this further, suppose that f is a (non-
constant) monotone function and ∆ is the derivative of Prπp [ f (x) = True] at
p = pc. Intuitively, we would expect Prπp [ f (x) = True] to jump from near 0 to
near 1 in an interval of around pc of width about 1/∆. Thus a “sharp thresh-
old” should roughly correspond to the case that 1/∆ is small even compared
to min(pc, qc). The Margulis–Russo Formula says that ∆ = 1
σ2
c I[ f (pc)], and

since min(pc, qc) is proportional to 4pc qc = σ2
c it follows that 1/∆ is “small”
compared to min(pc, qc) if and only if I[ f (pc)] is “large”. Thus we have a neat
criterion:

Sharp threshold principle: Let f : {True,False}n → {True,False} be monotone.
Then, roughly speaking, Prπp [ f (x) = True] has a “sharp threshold” if and only
if f has “large” (“superconstant”) total inﬂuence under its critical probability
distribution.

Of course this should all be made a bit more precise; see Exercise 8.28
for details. In light of this principle, we may try to prove that a given f
has a sharp threshold by proving that I[ f (pc)] is not “small”. In turn, this
strongly motivates the problem of “characterizing” Boolean-valued functions
f ∈ L2({−1, 1}n, π⊗n
p ) for which I[ f ] is small. Friedgut’s Junta Theorem, men-
tioned at the end of Chapter 3.1 and proved in Chapter 9.6, tells us that in
the uniform distribution case p = 1/2, the only way I[ f ] can be small is if f
is close to a junta. In particular, any monotone graph property with pc = 1/2
must have a very large derivative d
d p Prπp [ f = True] at p = pc: since the func-
tion is transitive-symmetric, all n coordinates are equally inﬂuential and it
can’t be close to a junta. These results also hold so long as p is bounded
away from 0 and 1; see Chapter 10.3. However, many interesting monotone
graph properties have pc very close to 0: e.g., connectivity, as we saw in Ex-
ample 8.49. Characterizing the functions f ∈ L2({−1, 1}n, π⊗n
p ) with small I[ f ]

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.5. Abelian groups 227

when p = on(1) is a trickier task; see the work of Friedgut, Bourgain, and
Hatami described in Chapter 10.5.

8.5. Abelian groups

The previous section covered the case of f ∈ L2(Ωn, π⊗n) with |Ω| = 2; there,
we saw it could be helpful to look at explicit Fourier bases. When |Ω| ≥ 3
this is often not helpful, especially if the only “operation” on the domain is
equality. For example, if f : {Red ,Green ,Blue }n → R , then it’s best to just work
abstractly with the orthogonal decomposition. However, if there is a notion
of, say, “addition” in Ω, then there is a natural, canonical Fourier basis for
L2(Ω, π) when π is the uniform distribution.

More precisely, suppose the domain Ω is a ﬁnite abelian group G, with
operation + and identity 0. We will consider the domain G under the uni-
form probability distribution π; this is quite natural because π is translation-
invariant: π(X ) = π(t + X ) for any X ⊆ G, t ∈ G. In this setting it is more
convenient to allow functions with range the complex numbers; thus we come
to the following deﬁnition:

Deﬁnition 8.51. Let G be a ﬁnite abelian group with operation + and iden-
tity 0. For n ∈ N + we write L2(G n) for the complex inner product space of
functions f : G n → C , with inner product

〈 f , g〉 = E
x∼G n[ f (x)g(x)].

Here and throughout this section x ∼ G n denotes that x is drawn from the
uniform distribution on G n.

Everything we have done in this chapter for the real inner product space
L2(Ωn, π⊗n) generalizes easily to the case of a complex inner product; the main
difference is that Plancherel’s Theorem becomes

〈 f , g〉 = ∑

α∈N n
<m
 ̂f (α) ̂g(α) = ∑

S⊆[n]〈 f =S, g=S〉.

See Exercise 8.32 for more.

A natural Fourier basis for L2(G) comes from a natural family of functions
G → C , namely the characters. These are deﬁned to be the group homomor-
phisms from G to C ×, where C × is the abelian group of nonzero complex
numbers under multiplication.

Deﬁnition 8.52. A character of the (ﬁnite) group G is a function χ : G → C ×

which is a homomorphism; i.e., satisﬁes χ(x + y) = χ(x)χ(y). Since G is ﬁnite
there is some m ∈ N + such that 0 = x+ x+· · ·+ x (m times) for each x ∈ G. Thus
1 = χ(0) = χ(x)m, meaning the range of χ is in fact contained in the mth roots
of unity. In particular, |χ(x)| = 1 for all x ∈ G.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

228 8. Generalized domains

We have the following easy facts:

Fact 8.53. If χ and φ are characters of G, then so are χ and φ · χ.

Proposition 8.54. Let χ be a character of G. Then either χ ≡ 1 or E[χ] = 0.

Proof. If χ ̸≡ 1, pick some y ∈ G such that χ(y) ̸= 1. Since x + y is uniformly
distributed on G when x ∼ G,

E
x∼G[χ(x)] = E
x∼G[χ(x + y)] = E
x∼G[χ(x)χ(y)] = χ(y) E
x∼G[χ(x)].

Since χ(y) ̸= 1 it follow that E[χ(x)] must be 0. □

Proposition 8.55. The set of all characters of G is orthonormal. (As a conse-
quence, G has at most dim(L2(G)) = |G| characters.)

Proof. First, if χ is a character, then 〈χ, χ〉 = E[|χ|2] = 1 because |χ| ≡ 1. Next,
if φ is another character distinct from χ then 〈φ, χ〉 = E[φ · χ]. But φ · χ is a
character by Fact 8.53, and φ · χ = φ/χ ̸≡ 1 because φ and χ are distinct; here
we used χ = 1/χ because |χ| ≡ 1. Thus 〈φ, χ〉 = 0 by Proposition 8.54. □

As we will see next, G in fact has exactly |G| characters. It thus follows
from Proposition 8.55 that the set of all characters (which includes the con-
stant 1 function) constitutes a Fourier basis for L2(G).

To check that each ﬁnite abelian group G has |G| distinct characters, we
begin with the case of a cyclic group, Z m for some m. In this case we know
that every character’s range will be contained in the mth roots of unity.

Deﬁnition 8.56. Fix an integer m ≥ 2 and write ω for the mth root of unity
exp(2πi/m). For 0 ≤ j < m, we deﬁne χ j : Z m → C by χ j(x) = ω jx. It is easy to
see that these are distinct characters of Z m.

Thus the functions χ0 ≡ 1, χ1, . . . , χm−1 form a Fourier basis for L2(Z m).
Furthermore, Proposition 8.13 tells us that we can get a Fourier basis for
L2(Z n
m) by taking all products of these functions.

Deﬁnition 8.57. Continuing Deﬁnition 8.56, let n ∈ N +. For α ∈ N n
<m we
deﬁne χα : Z n
m → C by
 χα(x) = n∏

j=1 χα j (x j).

These functions are easily seen to be (all of the) characters of the group Z n
m,
and they constitute a Fourier basis of L2(Z n
m).

Most generally, by the Fundamental Theorem of Finitely Generated Abelian
Groups we know that any ﬁnite abelian G is a direct product of cyclic groups
of prime-power order. In Exercise 8.35 you are asked to check that you get all
of the characters of G – and hence a Fourier basis for L2(G) – by taking all

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.6. Highlight: Randomized decision tree complexity 229

products of the associated cyclic groups’ characters. In the remainder of the
section we mostly stick to groups of the form Z n
m for simplicity.

Returning to the characters χ0, . . . , χm−1 from Deﬁnition 8.56, it is easy
to see (using ωm = 1) that they satisfy χ j · χ j′ = χ j+ j′ (mod m) and also 1/χ j =
χ j = χ− j (mod m). Thus the characters themselves form a group under mul-
tiplication, isomorphic to Z m. As in Chapter 3.2, we index them using the
notation ̂Z m. More generally, indexing the Fourier basis/characters of L2(Z n
m)
by ̂Z n
m instead of multi-indices, we have:

Fact 8.58. The characters (χα)
α∈̂Z n
m of Z n
m form a group under multiplication:

• χα · χβ = χα+β,

• 1/χα = χα = χ−α.

As mentioned, the salient feature of L2(G) distinguishing it from other
spaces L2(Ω, π) is that there is a notion of addition on the domain. This
means that convolution plays a major role in its analysis. We generalize the
deﬁnition from the setting of F n
2 :

Deﬁnition 8.59. Let f , g ∈ L2(G). Their convolution is the function f ∗ g ∈
L2(G) deﬁned by

( f ∗ g)(x) = E
y∼G[ f (y)g(x − y)] = E
y∼G[ f (x − y)g(y)].

Exercise 8.36 asks you to check that convolution is associative and com-
mutative, and that the following generalization of Theorem 1.27 holds:

Theorem 8.60. Let f , g ∈ L2(G). Then †f ∗ g(α) = ̂f (α) ̂g(α).

We conclude this section by mentioning vector space domains. When
doing Fourier analysis over the group Z n
m, it is natural for subgroups to arise.
Things are simplest when the only subgroups of Z m are the trivial ones, {0}
and Z m; in this case, all subgroups will be isomorphic to Z n′
m for some n′ ≤
n. Of course, this simple situation occurs if and only if m is equal to some
prime p. In that case, Z p can be thought of as a ﬁeld, Z n
p as an n-dimensional
vector space over this ﬁeld, and its subgroups as subspaces. We use the
notation F n
p in this setting and write ̂F n
p to index the Fourier basis/characters;
this generalizes the notation introduced for p = 2 in Chapter 3.2. Indeed, all
of the notions from Chapters 3.2 and 3.3 regarding afﬁne subspaces and
restrictions thereto generalize easily to L2(F n
p).

8.6. Highlight: Randomized decision tree complexity

A decision tree T for f : {−1, 1}n → {−1, 1} can be thought of as a deterministic
algorithm which, given adaptive query access to the bits of an unknown string

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

230 8. Generalized domains

x ∈ {−1, 1}n, outputs f (x). For example, to describe a natural decision tree for
f = Maj3 in words: “Query x1, then x2. If they are equal, output their value;
otherwise, query and output x3.” For a worst-case input (one where x1 ̸= x2)
this algorithm has a cost of 3, meaning it makes 3 queries. The cost of the
worst-case input is the depth of the decision tree.

As is often the case with algorithms it can be advantageous to allow ran-
domization. For example, consider using the following randomized query
algorithm for Maj3: “Choose two distinct input coordinates at random and
query them. If they are equal, output their value; otherwise, query and out-
put the third input coordinate.” Now for every input there is at least a 1/3
chance that the algorithm will ﬁnish after only 2 queries. Indeed, if we deﬁne
the cost of an input x to be the expected number of queries the algorithm
makes on it, it is easy to see that the worst-case inputs for this algorithm
have cost (1/3) · 2 + (2/3) · 3 = 8/3 < 3.

Let’s formalize the notion of a randomized decision tree:

Deﬁnition 8.61. Given f : {−1, 1}n → R , a (zero-error) randomized decision
tree T computing f is formally deﬁned to be a probability distribution over
(deterministic) decision trees that compute f . The cost of T on input x ∈
{−1, 1}n is deﬁned to be the expected number of queries T makes on x when
T ∼ T . The cost of T itself is deﬁned to be the maximum cost of any input.
Finally, the (zero-error) randomized decision tree complexity of f , denoted
RDT( f ), is the minimum cost of a randomized decision tree computing f .

We can get further savings from randomization if we are willing to assume
that the input x is chosen randomly. For example, if x ∼ {−1, 1}
3 is uniformly
random then any of the deterministic decision trees for Maj3 will make 2
queries with probability 1/2 and 3 queries with probability 1/2, for an overall
expected 5/2 < 8/3 < 3 queries.

Deﬁnition 8.62. Let T be a randomized decision tree. We deﬁne

δi(T ) = Pr
x∼{−1,1}n,
T∼T
 [T queries xi],

∆(T ) = n∑

i=1 δi(T ) = E
x∼{−1,1}n,
T∼T
 [# of coordinates queried by T on x]. (8.10)

Given f : {−1, 1}n → R , we deﬁne ∆( f ) to be the minimum of ∆(T ) over all
randomized decision trees T computing f .

We can also generalize these deﬁnitions for functions f ∈ L2(Ω, π⊗n). A
deterministic decision tree over domain Ω is the natural generalization in
which each internal query node has |Ω| outgoing edges, labeled by the ele-
ments of Ω. We write δ(π)
i (T ), ∆
(π)(T ), ∆
(π)( f ) for the generalizations to trees

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.6. Highlight: Randomized decision tree complexity 231

over Ω; in the case of L2({−1, 1}n, π⊗n
p ) we use the superscript (p) instead of
(πp) for brevity.

It follows immediately from the deﬁnitions that for any f ∈ L2(Ωn, π⊗n),

∆
(π)( f ) ≤ RDT( f ) ≤ DT( f ).

Remark 8.63. In the deﬁnition of ∆
(π)( f ) it is equivalent if we only allow
deterministic decision trees; this is because in (8.10) we can always choose
the “best” deterministic T in the support of T .

Example 8.64. It follows from our discussions that RDT(Maj3) ≤ 8/3 and
∆(Maj3) ≤ 5/2; indeed, it’s not hard to show that both of these bounds are
equalities. In Exercise 8.38 you are asked to generalize to the recursive
majority of 3 function on n = 3d inputs; it satisﬁes DT(Maj
⊗d
3 ) = 3d = n, but

RDT(Maj
⊗d
3 ) ≤ (8/3)d = nlog3(8/3) ≈ n.89,

∆(Maj
⊗d
3 ) ≤ (5/2)d = nlog3(5/2) ≈ n.83.

Incidentally, these bounds are not asymptotically sharp; estimating RDT(Maj
⊗d
3 )
in particular is a well-studied open problem.

Example 8.65. In Exercise 8.39 you are asked to show that for the logical OR
function, ∆
(p)(ORn) = 1−(1−p)n

p , which is roughly 2 for p = 1/2 but is asymptotic
to n/(2 ln 2) at the critical probability pc.

Example 8.64 illustrates a mildly surprising phenomenon: using random-
ness it’s possible to evaluate certain unbiased n-bit functions f while reading
only a 1/nΘ(1) fraction of the input bits. This is even more interesting when f
is transitive-symmetric like Maj
⊗d
3 . In that case it’s not hard to show (Exer-
cise 8.37) that any randomized decision tree T computing f can be converted
to one where ∆(T ) remains the same but all δi(T ) are equal to ∆( f )/n. Then f
can be evaluated despite the fact that each input bit is only queried with prob-
ability 1/nΘ(1).

In this section we explore the limits of this phenomenon. In particular,
a longstanding conjecture of Yao [Yao77] says that this is not possible for
monotone graph properties:

Yao’s Conjecture. Let f : {−1, 1}n → {−1, 1} be a nonconstant monotone v-
vertex graph property, where n = (v
2
)
. Then RDT( f ) ≥ Ω(n).

Toward this conjecture we will present a lower bound due to O’Donnell,
Saks, Schramm, and Servedio [OSSS05]. (Two other incomparable bounds
are discussed in the notes for this chapter.) It has the advantages that it
works for the more general class of transitive-symmetric functions and that
it even lower-bounds ∆
(pc)( f ):

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

232 8. Generalized domains

Theorem 8.66. Let f : {−1, 1}n → {−1, 1} be a nonconstant monotone transitive-
symmetric function with critical probability pc. Then

∆
(pc)( f ) ≥ (n/σc)2/3.

Theorem 8.66 is essentially sharp in several interesting cases. Whenever
the critical probability pc is Θ(1/n) or 1 − Θ(1/n) then σc = Θ(1/pn) and The-
orem 8.66 gives the strongest possible bound, ∆
(pc)( f ) ≥ Ω(n). This occurs,
e.g., for the ORn function (Example 8.65). Furthermore, Theorem 8.66 can
be tight up to a logarithmic factor when pc = 1/2 as the following theorem of
Benjamini, Schramm, and Wilson shows:

Theorem 8.67. [BSW05]. There exists an inﬁnite family of monotone transitive-
symmetric functions f n : {−1, 1}n → {−1, 1} with critical probability pc = 1/2 and
∆( f ) ≤ O(n2/3 log n).

Theorem 8.66 follows easily from two inequalities [OS06, OS07], [OSSS05],
which we now present:

OS Inequality. Let f ∈ L2({−1, 1}n, π⊗n
p ). Then ∑n
i=1 ̂f (i) ≤ ∥ f ∥2 · √
∆(p)( f ).

In particular, if f has range {−1, 1} and is monotone, then I[ f ] ≤ σ√
∆(p)( f ).

OSSS Inequality. Let f ∈ L2(Ωn, π⊗n) have range {−1, 1} and let T be any
randomized decision tree computing f . Then

Var[ f ] ≤ n∑

i=1 δ(π)
i (T ) · Infi[ f ].

Remark 8.68. An interesting corollary of the OSSS Inequality is that

MaxInf[ f ] ≥ Var[ f ]/∆
(π)( f ) ≥ Var[ f ]/DT( f ) ≥ Var[ f ]/ deg( f )
3,

the last inequality assuming Ω = {−1, 1}. See Exercise 8.44.

These two inequalities can be thought of as strengthenings of basic Fourier
inequalities which take into account the decision tree complexity of f . The
OS Inequality essentially generalizes the result that majority functions maxi-
mizes ∑n
i=1 ̂f (i); i.e., Theorem 2.33. The OSSS Inequality is a generalization
of the Poincaré Inequality, discounting the inﬂuences of coordinates that are
rarely read.

We will ﬁrst derive the query complexity lower bound Theorem 8.66 from
the OS and OSSS Inequalities. We will then prove the latter two inequalities.

Proof of Theorem 8.66. We consider f to be an element of L2({−1, 1}n, π⊗n
pc ).
Let T be a randomized decision tree achieving ∆
(pc)( f ). In the OSSS Inequal-
ity, we have Var[ f ] = 1 since pc is the critical probability and Infi[ f ] = I[ f ]/n

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.6. Highlight: Randomized decision tree complexity 233

for each i ∈ [n] since f is transitive-symmetric. Thus

1 ≤ ∑

i=1 δ(pc)
i (T ) · I[ f ]
n =⇒ n ≤ ∆
(pc)( f ) · I[ f ] ≤ σ∆
(pc)( f )3/2,

where we used the OS Inequality. The theorem follows by rearranging. □

Now we prove the OS and OSSS Inequalities, starting with the latter. We
will need a simple lemma that uses the decomposition f = Ei f + Li f .

Lemma 8.69. Let f , g ∈ L2(Ωn, π⊗n) and let j ∈ [n]. Given ω ∈ Ω, write f|ω
for the restriction of f in which the jth coordinate is ﬁxed to value ω, and
similarly for g. Then

Cov[ f , g] = E
ω,ω′∼π
independent

[Cov[ f|ω, g|ω′]] + 〈L j f , L j g〉.

Proof. Since the covariances and Laplacians are unchanged when constants
are added, we may assume without loss of generality that E[ f ] = E[g] = 0.
Then Cov[ f , g] = 〈 f , g〉 and

E
ω,ω′[Cov[ f|ω, g|ω′]] = E
ω,ω′[〈 f|ω, g|ω′〉 − E[ f|ω] E[g|ω′]]

= E
ω,ω′[〈 f|ω, g|ω′〉] − E[ f ] E[g] = E
ω,ω′[〈 f|ω, g|ω′〉] = 〈E j f , E j g〉.

Thus the stated equality reduces to the basic (Exercise 8.8) identity

〈 f , g〉 = 〈E j f , E j g〉 + 〈L j f , L j g〉. □

Proof of the OSSS Inequality. More generally we show that if g : {−1, 1}n →
{−1, 1} is also an element of L2(Ωn, π⊗n), then

Cov[ f , g] ≤ n∑

i=1 δ(π)
i (T ) · Infi[g]. (8.11)

The result then follow by taking g = f . We may also assume that T = T is a
single deterministic tree computing f ; this is because (8.11) is linear in the
quantities δ(π)
i (T ). We prove (8.11) by induction on the structure of T. If T is
depth-0, then f must be a constant function; hence Cov[ f , g] = 0 and (8.11) is
trivial. Otherwise, let j ∈ [n] be the coordinate queried at the root of T. For
each ω ∈ Ω, write Tω for the subtree of T given by the ω-labeled child of the
root. By applying Lemma 8.69 and induction (noting that Tω computes the

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

234 8. Generalized domains

restricted function f|ω), we get

Cov[ f , g] = E
ω,ω′∼π
independent

[Cov[ f|ω, g|ω′]] + 〈L j f , L j g〉

≤ E
ω,ω′∼π
[∑

i̸= j δ(π)
i (Tω) · Infi[gω′]
] + 〈L j f , L j g〉

= ∑

i̸= j δ(π)
i (T) · Infi[g] + 〈 f , L j g〉 (in part since E[L j g] = 0)

≤ ∑

i̸= j δ(π)
i (T) · Infi[g] + E[|L j g|] (since | f | ≤ 1)

= n∑

i=1 δ(π)
i (T) · Infi[g],

where the last step used δ(π)
j (T) = 1 and Proposition 8.24. This completes the
inductive proof of (8.11). □

Finally, we prove the OS Inequality. For this we require a deﬁnition.

Deﬁnition 8.70. Let (Ω, π) be a ﬁnite probability space and T a deterministic
decision tree over Ω. The decision tree process associated to T generates
a random string x distributed according to π (and some additional random
variables), as follows:

(1) Start at the root node of T; say it queries coordinate j1. Choose x j1 ∼ π
and follow the outgoing edge labeled by the outcome.

(2) Suppose the node of T which is reached queries coordinate j2. Choose
x j2 ∼ π and follow the outgoing edge labeled by the outcome.

(3) Repeat until a leaf node is reached. Then, deﬁne J = { j1, j2, j3, . . . } ⊆ [n]
to be the set of coordinates queried.

(4) Draw the as-yet-unqueried coordinates, denoted xJ, from π⊗J.

Despite the fact that the coordinates xi are drawn in a random, dependent
order, it’s not hard to see (Exercise 8.42) that the ﬁnal string x = (xJ, xJ) is
distributed according the product distribution π⊗n.

Proof of the OS Inequality. We will prove the claim ∑n
i=1 ̂f (i) ≤ ∥ f ∥2·√∆(p)( f );
the “in particular” statement follows immediately from Proposition 8.45. Fix
a deterministic decision tree T achieving ∆
(p)( f ) (see Remark 8.63) and let
x = (xJ, xJ) be drawn from the associated decision tree process. Using the
notation φ from Deﬁnition 8.39 we have

n∑

i=1 ̂f (i) = E
J,xJ ,xJ[ f (x) n∑

i=1 φ(xi)] = E
J,xJ[ f (xJ) E
xJ[ n∑

i=1 φ(xi)]].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.7. Exercises and notes 235

Here we abused notation slightly by writing f (xJ); in the decision tree process,
f ’s value is determined once xJ is. Since E[φ(xi)] = 0 for each i ̸∈ J we may
continue:

E
J,xJ[ f (xJ) E
xJ[ n∑

i=1 φ(xi)]] = E
J,xJ[ f (xJ) n∑

i=1 1{i∈J}φ(xi)]

≤ √ E
J,xJ[ f (xJ)2]

√
 E
J,xJ
 [( n∑

i=1 1{i∈J}φ(xi))2]
,

by Cauchy–Schwarz. Now √
EJ,xJ [ f (xJ)2] is simply ∥ f ∥2 since T computes f .
To complete the proof it sufﬁces to show that

E
J,xJ
 [( n∑

i=1 1{i∈J}φ(xi))2] = ∆
(p)( f ).

To see this, expand the square:

E
J,xJ
 [( n∑

i=1 1{i∈J}φ(xi)
)2] = n∑

i=1 E
J,xJ[1{i∈J}φ(xi)2] + ∑

i̸=i′ E
J,xJ[1{i,i′∈J}φ(xi)φ(xi′)].

Conditioned on i ∈ J the quantity E[φ(xi)2] is simply 1. Thus

n∑

i=1 E
J,xJ[1{i∈J}φ(xi)2] = n∑

i=1 Pr[i ∈ J] = ∆
(p)( f ).

It remains to show that EJ,xJ [1{i,i′∈J}φ(xi)φ(xi′)] = 0 whenever i ̸= i′. Sup-
pose we condition on the event that i, i′ ∈ J and we further condition on i
being queried before i′ is queried. Certainly this may affect the conditional
distribution of xi, but the conditional distribution of xi′ remains πp; hence
E[φ(xi′)] = 0 under this conditioning. Of course the same argument holds
when we condition on i′ being queried before i. From this it follows that
EJ,xJ [1{i,i′∈J}φ(xi)φ(xi′)] is indeed 0, completing the proof. □

8.7. Exercises and notes

8.1 Explain how to generalize the deﬁnitions and results in Sections 8.1
and 8.2 to general ﬁnite product spaces L2(Ω1 × · · · × Ωn, π1 × · · · × πn).

8.2 Verify that Deﬁnition 8.1 indeed deﬁnes a real inner product space. (Where
is the fact that π has full support used?)

8.3 Verify the formula for ̂f (α) in Deﬁnition 8.14.

8.4 Verify that φ0, φ1, φ2 from Example 8.10 indeed constitute a Fourier basis
for Ω = {a, b, c} with the uniform distribution.

8.5 Verify the Fourier expansion in Example 8.15.

8.6 Complete the proof of Proposition 8.16.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

236 8. Generalized domains

8.7 Prove that the expectation over I operator, EI , is a linear operator on
L2(Ωn, π⊗n) (i.e., EI ( f + g) = EI f +EI g), a projection (i.e., EI ◦EI = EI ), and
self-adjoint (i.e., 〈 f , EI g〉 = 〈EI f , g〉). Deduce that Tρ is also self-adjoint.

8.8 Show for any f , g ∈ L2(Ωn, π⊗n) and j ∈ [n] that f = E j f + L j f and that
〈 f , g〉 = 〈E j f , E j g〉 + 〈L j f , L j g〉.

8.9 Prove Proposition 8.24. (Hint: Exercise 1.17.)

8.10 Let f ∈ L2(Ωn, π⊗n) have range {−1, 1}. Proposition 8.24 tells us that
∥Li f ∥1 = ∥Li f ∥
2
2 = Infi[ f ].
(a) Show that ∥Li f ∥p
p ≤ 2pInfi[ f ] for any p ≥ 1.
(b) In case 1 ≤ p ≤ 2, show that in fact ∥Li f ∥p
p ≤ Infi[ f ]. (Hint: Use the
general form of Hölder’s inequality to bound ∥Li f ∥p in terms of ∥Li f ∥1
and ∥Li f ∥2.)

8.11 Generalize all of Exercise 2.35 to the setting of L2(Ωn, π⊗n). Caution: the
two statements referring to ρ ∈ [−1, 1] should refer only to ρ ∈ [0, 1] in this
more general setting.

8.12 Assume |Ω| = m and let π denote the uniform distribution on Ω.
(a) For x ∈ Ωn and y ∼ Nρ(x), write a formula for Pr[yi = ω] in terms of ρ
(there are two cases depending on whether or not xi = ω).
(b) Verify that your formula deﬁnes a valid probability distribution on Ω
even when − 1
m−1 ≤ ρ < 0. We may therefore extend the deﬁnition of
Nρ to this case. (Cf. the second half of Deﬁnition 2.40.)
(c) Verify that for x ∼ π⊗n and y ∼ Nρ(x), the distribution of (x, y) is
symmetric in x and y.
(d) Show that when y ∼ N− 1
m−1 (x), each yi is uniformly distributed on
Ω \ {xi}.
(e) Verify that the formula for Tρ from Proposition 8.28 continues to hold
for − 1
m−1 ≤ ρ < 0. (Hint: Use the fact that it holds for ρ ∈ [0, 1] and
that the formula in part (a) is a polynomial in ρ.)

8.13 Show that Deﬁnition 8.30 extends by continuity to

Inf(0)
i [ f ] = ∑

#α=1
αi̸=0
 ̂f (α)2.

Extend also Proposition 8.31 to the case of δ = 1.

8.14 Prove explicitly that condition 5 holds in Theorem 8.35.

8.15 Prove that condition 6 must hold in Theorem 8.35 directly from the
uniqueness statement (i.e., without appealing to the explicit construc-
tion).

8.16 Let f ∈ L2(Ωn, π⊗n). Prove directly from the deﬁning Theorem 8.35 that
( f =S)
⊆T is equal to f =S if S ⊆ T and is equal to 0 otherwise.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.7. Exercises and notes 237

8.17 Let f ∈ L2(Ωn, π⊗n) and let x ∼ π⊗n. In this exercise you should think
about how the (conditional) expectation of f changes as the random vari-
ables x1, . . . , xn are revealed one at a time.
(a) Recalling that f ⊆[t](x) depends only on x1, . . . , xt, show that the se-
quence of random variables ( f ⊆[t](x))t=0...n is a martingale (where
f ⊆[0] denotes f ;); i.e.,

E[ f ⊆[t](x) | f ⊆[0](x), . . . , f ⊆[t−1](x)] = f ⊆[t−1](x) ∀t ∈ [n].

(This is the Doob martingale for f .)
(b) For each t ∈ [n] deﬁne

dt f = f ⊆[t] − f ⊆[t−1] = ∑

S⊆[n]
max(S)=t
 f =S.

Show that E[dt f (x) | f ⊆[0](x), . . . , f ⊆[t−1](x)] = 0. (Here (dt f )t=1...n is
the martingale difference sequence for f .)

8.18 For f , g ∈ L2(Ωn, π⊗n), prove the following directly from Theorem 8.35:

〈 f , g〉 = ∑

S⊆[n]
〈 f =S, g=S〉

Infi[ f ] = ∑

S∋i ∥ f =S∥
2
2

I[ f ] = n∑

k=0 k · Wk[ f ]

Tρ( f =S) = (Tρ f )
=S = ρk f =S

Stabρ[ f ] = n∑

k=0 ρk · Wk[ f ].

8.19 Let f ∈ L2(Ωn, π⊗n) and let S ⊆ [n]. Show that ∥ f =S∥∞ ≤ 2
|S|∥ f ∥∞.

8.20 Explicitly verify that Proposition 8.36 holds for the function in Exam-
ples 8.15 and 8.37.

8.21 Let f ∈ L2(Ωn, π⊗n) and let i ∈ S ⊆ [n]. Suppose we take f =S and restrict
its ith coordinate to have value ωi, forming the subfunction g = ( f =S)|ωi .
Show that g = g=S\{i}. In particular, E[g] = 0 assuming |S| ≥ 2.

8.22 Let f ∈ L2(Ωn, π⊗n) be a symmetric function. Show that if 1 ≤ |S| ≤ |T| ≤ n,
then 1
|S| Var[ f ⊆S] ≤ 1
|T| Var[ f ⊆T ].

8.23 Prove the sharp threshold statement about the majority function made
in Example 8.49. (Hint: Chernoff bound.) In the social choice literature,
this fact is known as the Condorcet Jury Theorem.

8.24 Let p1, . . . , pn ∈ (0, 1) and let π = πp1 ⊗ · · · πpn be the associated product dis-
tribution on {−1, 1}n. Write µi = 1−2pi and σi = 2
ppi√
1 − pi. Generalize
Proposition 8.45 to the setting of L2({−1, 1}n, π).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

238 8. Generalized domains

8.25 Let f : {−1, 1}n → R and consider the general product distribution setting
of Exercise 8.24.
(a) For S = {i1, . . . , i k} ⊆ [n], write DφS for Dφi1 ◦· · ·◦Dφik and similarly DxS .
Show that DφS = ∏i∈S σi · DxS .
(b) Writing f (µ) for the function f viewed as an element of L2({−1, 1}n, π),
show that ̂f (p)(S) = ∏

i∈S σi · DxS f (µ1, . . . , µn).

(c) Show that ˆ∥ f (p) ˆ∥∞ ≤ ∏i∈S σi · ∥ f ∥∞.

8.26 (a) Generalize Exercise 2.10 by showing that for f ∈ L2({−1, 1}n, π⊗n
p ) with
range {−1, 1},

Pr
x∼π⊗n
p [i is b-pivotal for f on x] = πp(b)Infi[ f ]

for i ∈ [n] and b ∈ {−1, 1}.
(b) Generalize Proposition 4.7 by showing that if f : {−1, 1}n → {−1, 1} has
DNFwidth( f ) ≤ w, then I[ f (p)] ≤ 4qw ≤ 4w, and if f has CNFwidth( f ) ≤ w,
then I[ f (p)] ≤ 4pw ≤ 4w.

8.27 Fix any α ∈ (0, 1). Let f : {True,False}n → {True,False} be a nonconstant
monotone function. Show that there exists p ∈ (0, 1) such that Prπp [ f (x) =
True] = α. (Hint: Intermediate Value Theorem.)

8.28 Fix a small constant 0 < ϵ < 1/2. Let f : {True,False}n → {True,False}
be a nonconstant monotone function. Let p0 (respectively, pc, p1) be
the unique value of p ∈ (0, 1) such that Prπp [ f (x) = True] = ϵ (respec-
tively, 1/2, 1 − ϵ). (This is a valid deﬁnition by Exercise 8.27.) Deﬁne
also σ2
c = 4pc(1 − pc). The threshold interval for f is deﬁned to be [p0, p1],
and δ = p1 − p0 is the threshold width. Now let ( f n)n∈N be a sequence
of nonconstant monotone Boolean functions (usually “naturally related”,
with f n’s input length an increasing function of n). Deﬁne the sequences
p0(n), pc(n), p1(n), σ2
c(n), δ(n). We say that the family ( f n) has a sharp
threshold if δ(n)/σ2
c(n) → 0 as n → ∞; otherwise, we say it has a coarse
threshold. (Note: If pc(n) ≤ 1/2 for all n, this is the same as saying that
δ(n)/pc(n) → 0.) Show that if ( f n) has a coarse threshold, then there
exists C < ∞, an inﬁnite sequence n1 < n2 < n3 < · · · , and a sequence
(p(ni))i∈N such that:
• ϵ < Prπp(ni )[ f ni (x) = True] < 1 − ϵ for all i;

• I[ f (p(ni))
ni ] ≤ C for all i.
(Hint: Margulis–Russo and the Mean Value Theorem.)

8.29 Let f : {−1, 1}n → {−1, 1} be a nonconstant monotone function and let
F : [0, 1] → [0, 1] be the (strictly increasing) function deﬁned by F(p) =
Prπp [ f (x) = −1]. Let pc be the critical probability such that F(pc) = 1/2.
Assume that pc ≤ 1/2. (This is without loss of generality since we can

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.7. Exercises and notes 239

replace f by f †. We often think of pc ≪ 1/2.) The goal of this exercise is to
show a weak kind of threshold result: roughly speaking, F(p) = o(1) when
p = o(pc) and F(p) = 1 − o(1) when p = ω(pc).
(a) Using the Margulis–Russo Formula and the Poincaré Inequality show
that for all 0 < p < 1,

F ′(p) ≥ F(p)(1 − F(p))
p(1 − p) .

(b) Show that for all p ≤ pc we have F ′(p) ≥ F(p)
2p and hence d
d p ln F(p) ≥

1
2p .

(c) Deduce that for any 0 ≤ p0 ≤ pc we have F(p0) ≤ 1
2 √p0/pc; i.e., F(p0) ≤
ϵ if p0 ≤ (2ϵ)
2 pc.
(d) Show that the factor (2ϵ)2 can be improved to Θ(τ)ϵ1+τ for any small
constant τ > 0. (Hint: The quadratic dependence on ϵ arose because
we used 1 − F(p) ≥ 1/2 for p ≤ pc; but from part (c) we have the im-
proved bound 1 − F(p) ≥ 1 − τ once p ≤ (2τ)2 pc.)
(e) In the other direction, show that so long as p1 = 1
(2ϵ)2 pc ≤ 1/2, we have
F(p1) ≥ 1 − ϵ. (Hint: Work with ln(1 − F(p)).) In case p1 ≤ 1/2 does not
hold, show that we at least have F(1/2) ≥ 1 − √pc/2.
(f ) The bounds in part (e) are not very interesting when pc is close to 1/2.
Show that we also have F(1 − δ) ≥ 1 − p
δ/2 (even when pc = 1/2).

8.30 Consider the sequence of functions f n : {True,False}n → {True,False} de-
ﬁned for odd n ≥ 3 as follows: f n(x1, . . . , xn) = Maj3(x1, x2, Majn−2(x3, . . . , xn)).
(a) Show that f n is monotone and has critical probability pc = 1/2.
(b) Sketch a plot of Prπp [ f n(x) = True] versus p (assuming n very large).
(c) Show that I[ f n] = Θ(pn).
(d) Show that the sequence f n has a coarse threshold as deﬁned in Exer-
cise 8.28 (assuming ϵ < 1/4).

8.31 (a) Consider the following probability distributions on strings x ∈ F n
2 :
(1) First choose k ∼ {0, 1, 2, . . . , n} uniformly. Then choose x uni-
formly from the set of all strings of Hamming weight k.
(2) First choose a uniformly random “path π from (0, 0, . . . , 0) up
to (1, 1, . . . , 1)”; i.e., let π be a uniformly random permutation
from Sn and let π
≤i ∈ F n
2 denote the string whose jth coordi-
nate is 1 if and only if π( j) ≤ i. Then choose k ∼ {0, 1, 2, . . . , n}
uniformly and let x be the “kth string on the path”, namely π
≤k.
(3) First choose p ∼ [0, 1]. Then choose x ∼ π⊗n
p .
Show that these are in fact the same distribution. (Hint: Imagine
choosing n + 1 indistinguishable points uniformly from [0, 1] and then
randomly assigning them the labels “p”, 1, 2, . . . , n.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

240 8. Generalized domains

(b) We denote by νn the distribution on F [n]
2 from part (a); more generally,
we use the notation νN for the distribution on F N
2 where N is an
abstract set of cardinality n. Given a nonempty J ⊆ [n], show that if
x ∼ νn and xJ ∈ F J
2 denotes the restriction of x to coordinates J, then
xJ has the distribution νJ.
(c) Let f : F n
2 → R and ﬁx i ∈ [n]. The ith Shapley value of f is deﬁned to
be
 Shapi[ f ] = E
x∼νn[ f (x(i7→1)) − f (x(i7→0))].

Show that ∑n
i=1 Shapi[ f ] = f (1, 1, . . . , 1) − f (0, 0, . . . , 0).

(d) Suppose f : F n
2 → {0, 1} is monotone. Show Shapi[ f ] = 4 ∫ 1
0 Infi[ f (p)] d p.

8.32 Explain how to generalize the deﬁnitions and results in Sections 8.1, 8.2
to the case of the complex inner product space L2(Ωn, π⊗n). In particular,
verify the following formulas from Proposition 8.16:

E[ f ] = ̂f (0)

E[| f |2] = E[〈 f , f 〉] = ∑

α∈N n
<m〈 ̂f (α), ̂f (α)〉 = ∑

α∈N n
<m | ̂f (α)|2

Var[ f ] = 〈 f − E[ f ], f − E[ f ]〉 = ∑

α̸=0 | ̂f (α)|2

〈 f , g〉 = ∑

α∈N n
<m〈 ̂f (α), ̂g(α)〉 = ∑

α∈N n
<m
 ̂f (α) ̂g(α)

Cov[ f , g] = 〈 f − E[ f ], g − E[g]〉 = ∑

α̸=0 ̂f (α) ̂g(α).

8.33 (a) As in Exercise 2.58, explain how to generalize the deﬁnitions and
results in Sections 8.1, 8.2 to the case of functions f : Ωn → V , where
V is a real inner product space with inner product 〈·, ·〉V . Here the
Fourier coefﬁcients ̂f (α) will be elements of V , and 〈 f , g〉 is deﬁned
to be Ex∼π⊗n [〈 f (x), g(x)〉V ]. In particular, verify the formulas from
Proposition 8.16, including Placherel: 〈 f , g〉 = ∑
α〈 ̂f (α), ̂g(α)〉V .
(b) For Σ a ﬁnite set we write △Σ for the set of all probability distributions
over Σ (cf. Exercise 7.22). Writing |Σ| = m, we also identify △Σ with
the standard convex simplex in R m, namely {µ ∈ R m : µ1 + · · · + µm =
1, µi ≥ 0 ∀i} (where we assume some ﬁxed ordering of Σ). Finally,
we identify the m elements of Σ with the constant distributions in
△Σ; equivalently, the vertices of the form (0, . . . , 0, 1, 0, . . . , 0). Given a
function f : Ωn → Σ, often the most useful way to treat it analytically
is to interpret it as a function f : Ωn → △Σ ⊂ R m and then use the
setting described in part (a), with V = R m. Using this idea, show that
if f : Ωn → Σ and π is a distribution on Ω, then

Stabρ[ f ] = Pr
x∼π⊗n,y∼Nρ(x)[ f (x) = f (y)].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.7. Exercises and notes 241

(Here in Stabρ[ f ] we are interpreting f ’s range as △Σ ⊂ R m, whereas
in the expression f (x) = f (y) we are treating f ’s range as the abstract
set Σ.)

8.34 We say a function f ∈ L2(Ωn, π⊗n) is a linear threshold function if it is
expressible as f (x) = sgn(ℓ(x)), where ℓ : Ωn → R has degree at most 1 (in
the sense of Deﬁnition 8.32).
(a) Given ω(+1), ω(−1) ∈ Ωn and x ∈ {−1, 1}n, we introduce the notation ω(x)

for the string (ω(x1)
1 , . . . , ω(xn)
n ) ∈ Ωn. Show that if ω(+1), ω(−1) ∼ π⊗n are
drawn independently and (x, y) ∼ {−1, 1}n × {−1, 1}n is a ρ-correlated
pair of binary strings, then (ω(x), ω(y)) is a ρ-correlated pair under
π⊗n.
(b) Let f ∈ L2(Ωn, π⊗n) be a linear threshold function. Given a pair
ω(+1), ω(−1) ∈ Ωn, deﬁne gω(+1),ω(−1) : {−1, 1}n → {−1, 1} by gω(+1),ω(−1)(x) =
f (ω(x)). Show that gω(+1),ω(−1) is a linear threshold function in the
“usual” sense.
(c) Prove that Peres’s Theorem (from Chapter 5.5) applies to linear thresh-
old functions in L2(Ωn, π⊗n), with the same bounds.

8.35 Let G be a ﬁnite abelian group. We know by the Fundamental Theorem
of Finitely Generated Abelian Groups that G ∼= Z m1 × · · ·Z mn where each
m j is a prime power.
(a) Given α ∈ G, deﬁne χα : G → C by

χα(x) = n∏

j=1 exp(2πiα j x j/m j).

Show χα is a character of G and that the χα’s are distinct functions
for distinct α’s. Deduce that the set of all χα’s forms a Fourier basis
for L2(G).
(b) Show that this set of characters forms a group under multiplication
and that this group is isomorphic to G; i.e., generalize Fact 8.58. This
is called the dual group of G and it is written ̂G. We also identify the
characters in ̂G with their indices α.

8.36 Verify that the convolution operation on L2(G) is associative and commu-
tative, and that it satisﬁes †f ∗ g(α) = ̂f (α) ̂g(α) for all α ∈ ̂G. (See Exer-
cise 8.35 for the deﬁnition of ̂G.)

8.37 (a) Let f ∈ L2(Ωn, π⊗n) be any transitive-symmetric function and let T
be a randomized decision tree computing f . Show that there exists
a randomized decision tree T ′ computing f with ∆
(π)(T ′) = ∆
(π)(T )
and such that δ(π)
i (T ′) is the same for all i ∈ [n]. (Hint: Randomize
over the automorphism group Aut( f ) and use Exercise 2.47.)
(b) Given a randomized decision tree T , let δ(π)(T ) = maxi∈[n]{δ(π)
i (T )}.
Given f ∈ L2({−1, 1}n, π⊗n), deﬁne δ(π)( f ) to be the minimum value of

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

242 8. Generalized domains

δ(π)(T ) over all T which compute f ; this is called the revealment of f .
Show that if f is transitive-symmetric, then δ(π)( f ) = 1
n ∆
(π)( f ).

8.38 (a) Show that DT(Maj
⊗d
3 ) = 3d, RDT(Maj
⊗d
3 ) ≤ (8/3)d, and ∆(Maj
⊗d
3 ) ≤
(5/2)d.
(b) Show that RDT(Maj
⊗2
3 ) < (8/3)
2. How small can you make your upper
bound?

8.39 (a) Show that for every deterministic decision tree T computing the logi-
cal OR function on n bits,

∆
(p)(T) = p · 1 + (1 − p)p · 2 + (1 − p)
2 p · 3 + · · ·

· · · + (1 − p)n−2 p · (n − 1) + (1 − p)n−1 · n = 1 − (1 − p)n

p .

Deduce ∆
(p)(ORn) = 1−(1−p)n

p .

(b) Show that ∆
(pc)(ORn) ∼ n/(2 ln 2) as n → ∞, where pc denotes the
critical probability for ORn.

8.40 Let NAND : {True,False}
2 → {True,False} be the function that outputs True
unless both its inputs are True.
(a) Show that for d even, NAND
⊗d = Tribes
⊗d/2
2,2 . (Thus the recursive
NAND function is sometimes known as the AND-OR tree.)
(b) Show that DT(NAND
⊗d) = 2d.
(c) Show that RDT(NAND) = 2.
(d) For b ∈ {True,False} and T a randomized decision tree computing
a function f , let RDTb(T ) denote the maximum cost of T among
inputs x with f (x) = b. Show that there is a randomized decision
tree T computing NAND with RDTFalse(T ) = 3/2.
(e) Show that RDT(NAND
⊗2) ≤ 3.
(f ) Show that there is a family of randomized decision trees (Td)d∈N +,
with Td computing NAND
⊗d, satisfying the inequalities

RDTFalse(Td) ≤ 2RDTTrue(Td−1)

RDTTrue(Td) ≤ RDTFalse(Td−1) + (1/2)RDTTrue(Td−1).

(g) Deduce RDT(NAND
⊗d) ≤ ( 1+
p
33
4 )d ≈ n.754, where n = 2d.

8.41 Let C = {monotone f : {−1, 1}n → {−1, 1} | DT( f ) ≤ k}. Show that C is learn-
able from random examples with error ϵ in time nO(pk/ϵ). (Hint: OS In-
equality and Corollary 3.32.)

8.42 Verify that the decision tree process described in Deﬁnition 8.70 indeed
generates strings distributed according to π⊗n. (Hint: Induction on the
structure of the tree.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.7. Exercises and notes 243

8.43 Let T be a deterministic decision tree of size s. Show that ∆(T) ≤ log s.
(Hint: Let P be a random root-to-leaf path chosen as in the decision tree
process. How can you bound the entropy of the random variable P?)

8.44 Let f ∈ L2(Ωn, π⊗n) be a nonconstant function with range {−1, 1}.
(a) Show that MaxInf[ f ] ≥ Var[ f ]/∆
(π)( f ) (cf. the KKL Theorem from
Chapter 4.2).
(b) In case Ω = {−1, 1} show that MaxInf[ f ] ≥ Var[ f ]/ deg( f )
3. (You should
use the result of Midrij ¯anis mentioned in the notes in Chapter 3.6.)
(c) Show that I[ f ] ≥ Var[ f ]/δ(π)( f ), where δ(π)( f ) is the revealment of f ,
deﬁned in Exercise 8.37(b).

8.45 Let f ∈ L2(Ωn, π⊗n) have range {−1, 1}.
(a) Let T be a randomized decision computing f and let i ∈ [n]. Show
that Infi[ f ] ≤ δ(π)
i (T ). (Hint: The decision tree process.)
(b) Suppose f is transitive-symmetric. Show that ∆
(π)( f ) ≥ √
Var[ f ] · n.
(Hint: Exercise 8.37(b).) This result can be sharp up to an O(√
log n)
factor even for an f : {−1, 1}n → {−1, 1} with Var[ f ] = 1; see [BSW05].

8.46 In this exercise you will give an alternate proof of the OSSS Inequality
that is sharp when Var[ f ] = 1 and is weaker by only a factor of 2 when
Var[ f ] is small. Let f ∈ L2(Ωn, π⊗n) have range {−1, 1}. Given a random-
ized decision tree T we write err(T ) = Prx∼π⊗n [T (x) ̸= f (x)].
(a) Let T be a depth-k deterministic decision tree (not necessarily com-
puting f ) whose root queries coordinate i. Let T be the distribution
over deterministic trees of depth at most k − 1 given by following
a random outgoing edge from T’s root (according to π). Show that
err(T ) ≤ err(T) + 1
2 Infi[ f ].
(b) Let T be a randomized decision tree of depth 0. Show that err(T ) ≥
min{Pr[ f (x) = 1], Pr[ f (x) = −1]}.
(c) Prove by induction on depth that if T is any randomized decision tree,
then 1
2 ∑n
i=1 δ(π)
i (T )·Infi[ f ] ≥ min{Pr[ f (x) = 1], Pr[ f (x) = −1]}−err(T ).
Verify that this yields the OSSS Inequality when Var[ f ] = 1 and in
general yields the OSSS Inequality up to a factor of 2.

8.47 Show that the OSSS Inequality fails for functions f : {−1, 1}n → R . (Hint:
The simplest counterexample uses a decision tree with the shape in Fig-
ure 8.2.)
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

244 8. Generalized domains

Figure 8.2. The basis for a counterexample to the OSSS Inequality when
f : {−1, 1}n → R

Can you make the ratio of the left-hand side to the right-hand side
equal to 130+20
p
3
157 ? Larger?

Notes. The origins of the orthogonal decomposition described in Section 8.3
date back to the work of Hoeffding [Hoe48] (see also von Mises [vM47]). Ho-
effding’s work introduced U-statistics, i.e., functions f of independent random
variables X 1, . . . , X n of the form avg1≤i1<···<i k≤n g(X i1, . . . , X i k ), where g : R k →
R is a symmetric function. Such functions are themselves symmetric. For
these functions, Hoeffding introduced f ⊆S (which, by symmetry, depends only
on |S|) and proved certain inequalities (e.g., those in Exercise 8.22) relating
Var[ f ] to the quantities ∥ f ⊆S∥2
2, ∥ f =S∥
2
2. Nonsymmetric functions f were
considered only rarely in the subsequent three decades of statistics research.
One notable exception comes in the work of Hájek [Háj68], who effectively
introduced f ≤1, known as the Hájek projection of f . Also, a work of Bour-
gain [Bou79] essentially describes the decomposition f = ∑k f =k. The ﬁrst
work that mentions the general orthogonal decomposition for not-necessarily-
symmetric functions appears to be that of Efron and Stein [ES81] from the
late 1970s. Efron and Stein’s description is brief; the subsequent work of
Karlin and Rinott [KR82] gives a more thorough development. Efron and
Stein’s main result was a proof of the statement Var[ f ] ≤ I[ f ] for symmet-
ric f ; in the statistics literature this is known as the Efron–Stein Inequality.
Steele [Ste86a] extended this to the case of nonsymmetric f by a simple proof
that used the Fourier basis approach to orthogonal decomposition. This ap-
proach via Fourier bases originated in the work of Rubin and Vitale [RV80];
see also Takemura [Tak83] and Vitale [Vit84]. The terminology “Fourier
basis” we use is not standard.

The p-biased hypercube distribution is strongly motivated by the Erd˝os–
Rényi [ER59] theory of random graphs (see e.g., Bollobás and Riordan [BR08]
for history) and by percolation theory (introduced in Broadbent and Hammer-
sley [BH57]). Inﬂuences under the p-biased distribution – and their connec-
tion to threshold phenomena – were studied by Russo [Rus81, Rus82]. The
former work proved the Margulis–Russo formula independently of Margulis,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

8.7. Exercises and notes 245

who had proven it earlier [Mar74]. Fourier analysis under the p-biased distri-
bution seems to have been ﬁrst introduced to the theoretical computer science
literature by Furst, Jackson, and Smith [FJS91], who extended the LMN
learning algorithm for AC0 to this setting. Talagrand [Tal93, Tal94] devel-
oped p-biased Fourier for the study of threshold phenomena, strengthening
Margulis and Russo’s work and proving the KKL Theorem in the p-biased
setting. Similar results were obtained by Friedgut and Kalai [FK96] using
an earlier work of Bourgain, Kahn, Kalai, Linial, and Katznelson [BKK
+92]
that proved a version of the KKL Theorem in the setting of general product
spaces. The statements about sharp thresholds for cliques and connectivity
in Example 8.49 are essentially due to Matula and to Erd˝os–Rényi, respec-
tively; see, e.g., Bollobás [Bol01]. Weak threshold results similar to the ones
in Exercise 8.29 were proved by Bollobás and Thomason [BT87], using the
Kruskal–Katona Theorem rather than the Poincaré Inequality.

Fourier analysis on ﬁnite abelian groups – and more generally, on locally
compact abelian groups – is an enormous subject upon which we have touched
only brieﬂy. We cannot survey it here but refer instead to the standard text-
book of Rudin [Rud62] and to the reader-friendly textbook of Terras [Ter99],
which focuses on ﬁnite groups.

One of the earliest works on randomized decision tree complexity is that
of Saks and Wigderson [SW86]; they proved the contents of Exercise 8.40.
(We note that RDT( f ) is usually denoted R( f ) in the literature, and DT( f ) is
usually denoted D( f ).) One basic lower bound in the area is that RDT( f ) ≥√DT( f ) for any f : {−1, 1}n → {−1, 1}; in fact, this lower bound holds even
for “nondeterministic decision tree complexity”, as proved in [BI87, Tar89].
Yao’s Conjecture is also sometimes attributed to Richard Karp. Regarding
the recursive majority-of-3 function, Ravi Boppana was the ﬁrst to point out
that RDT(Maj
⊗d
3 ) = o(3d) even though DT(Maj
⊗d
3 ) = 3d. Saks and Wigderson
noted the bound RDT(Maj
⊗d
3 ) ≤ (8/3)d and also that it is not optimal. Fol-
lowing subsequent works [JKS03, She08] the best known upper bound is
O(2.65d) [MNSX11] and the best known lower bound is Ω(2.55d) [Leo12].

The proof of the OSSS Inequality we presented is essentially Lee’s [Lee10];
the alternate proof from Exercise 8.46 is due to Jain and Zhang [JZ11].
The Condorcet Jury Theorem (see Exercise 8.23) is from [dC85]. The Shap-
ley value described in Exercise 8.31 was introduced by the Nobelist Shap-
ley [Sha53]; for more, see Roth [Rot88]. Exercise 8.34 is from Blais, O’Donnell,
and Wimmer [BOW10]. Exercises 8.37(a) and 8.45 are from the work of
Benjamini, Schramm, and Wilson [BSW05]; the term “revealment” was intro-
duced by Schramm and Steif [SS10]. Exercise 8.47 is from [OSSS05]. Related
to this, it is extremely interesting to ask whether something like the result of

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

246 8. Generalized domains

Exercise 8.44(b) holds for functions f : {−1, 1}n → [−1, 1]. It has been suggested
that the answer is yes:

Aaronson–Ambainis Conjecture. [Aar08, AA11] Let f : {−1, 1}n → [−1, 1].
Then MaxInf[ f ] ≥ poly(Var[ f ]/ deg( f )).

If true, this conjecture would have signiﬁcant consequences for the limitations
of efﬁcient quantum computation; see Aaronson and Ambainis [AA11]. The
best result in the direction of the conjecture, due to Dinur et al. [DFKO07], is
the lower bound MaxInf[ f ] ≥ poly(Var[ f ]/2deg( f )).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 9

Basics of
hypercontractivity

In 1970, Bonami proved the following central result:

The Hypercontractivity Theorem. Let f : {−1, 1}n → R and let 1 ≤ p ≤ q ≤ ∞.

Then ∥Tρ f ∥q ≤ ∥ f ∥p for 0 ≤ ρ ≤ √ p−1
q−1 .

As stated, this theorem may look somewhat opaque. In this chapter we
consider some special cases of it that are easier to understand, easier to prove,
and that encompass almost all of the theorem’s uses. The proof of the full
theorem is deferred to Chapter 10. The special cases in this chapter are the
following:

Bonami Lemma. Let f : {−1, 1}n → R have degree k. Then ∥ f ∥4 ≤ p
3k∥ f ∥2.

The fundamental idea of this statement is that if x ∼ {−1, 1}n and f : {−1, 1}n →
R has low degree then the random variable f (x) is quite “reasonable”; e.g.,
it is “nicely” distributed around its mean. The Bonami Lemma has a very
easy inductive proof and is already powerful enough to obtain many of the
well-known applications of “hypercontractivity”, including the KKL Theorem
(proven at the end of this chapter) and the Invariance Principle.

(2, q)-Hypercontractivity Theorem. Let f : {−1, 1}n → R and let 2 ≤ q ≤ ∞.
Then ∥T1/pq−1 f ∥q ≤ ∥ f ∥2. As a consequence, if f has degree at most k then

∥ f ∥q ≤ √q − 1k∥ f ∥2.

This theorem quantiﬁes the extent to which Tρ is a “smoothing” operator;
equivalently, it gives even more control over the “reasonableness” of low-
degree polynomials. Its consequences include a generalization of the Level-1

247

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

248 9. Basics of hypercontractivity

Inequality (from Chapter 5.4) to “Level-k Inequalities”, as well as a Chernoff-
like tail bound for low-degree polynomials of random bits.

(p, 2)-Hypercontractivity Theorem. Let f : {−1, 1}n → R and let 1 ≤ p ≤ 2.
Then ∥Tpp−1 f ∥2 ≤ ∥ f ∥p. Equivalently, Stabρ[ f ] ≤ ∥ f ∥
2
1+ρ for 0 ≤ ρ ≤ 1.

This theorem is actually “equivalent” to the (2, q)-Hypercontractivity Theorem
by virtue of Hölder’s inequality. When specialized to the case of f : {−1, 1}n →
{0, 1} it gives a precise quantiﬁcation of the fact that the “noisy hypercube
graph” is a “small-set expander”. Qualitatively, this means that if A ⊆ {−1, 1}n

is “small”, x ∼ A, and y ∼ Nρ(x), then y is very unlikely to be in A.

9.1. Low-degree polynomials are reasonable

As anyone who has worked in probability knows, a random variable can some-
times behave in rather “unreasonable” ways. It may be never close to its
expectation. It might exceed its expectation almost always, or almost never.
It might have ﬁnite 1st, 2nd, and 3rd moments, but an inﬁnite 4th moment.
All of this poor behavior can cause a lot of trouble – wouldn’t it be nice to have
a class of “reasonable” random variables?

A very simple condition on a random variable that guarantees some good
behavior is that its 4th moment is not too large compared to its 2nd moment.

Deﬁnition 9.1. For a real number B ≥ 1, we say that the real random variable
X is B-reasonable if E[X 4] ≤ B E[X 2]2. (Equivalently, if ∥X ∥4 ≤ B1/4∥X ∥2.)

The smaller B is, the more “reasonable” X is. This deﬁnition is scale-
invariant (i.e., cX is B-reasonable if and only if X is, for c ̸= 0) but not
translation-invariant (c + X and X may not be equally reasonable). The latter
fact can sometimes be awkward, a point we’ll address further in Section 9.3.
Indeed, we’ll later encounter a few alternative conditions that also capture
“reasonableness”. For example, in Chapter 11 we’ll consider the analogous
3rd moment condition, E[|X |3] ≤ B E[X 2]3/2. Strictly speaking, the 4th mo-
ment condition is stronger: if X is B-reasonable, then

E[|X |3] = E[|X | · X 2] ≤ √
E[X 2]
√E[X 4] ≤ pB E[X 2]
3/2;

on the other hand, there exist random variables with ﬁnite 3rd moment and
inﬁnite 4th moment. However, such unusual random variables almost never
arise for us, and morally speaking the 4th and 3rd moment conditions are
about equally good proxies for reasonableness.

Example 9.2. If x ∼ {−1, 1} is uniformly random then x is 1-reasonable. If
g ∼ N(0, 1) is a standard Gaussian, then E[g4] = 3, so g is 3-reasonable. If
u ∼ [−1, 1] is uniform, then you can calculate that it is 9
5 -reasonable. In all

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.1. Low-degree polynomials are reasonable 249

of these examples B is a “small” constant, and we think of these random
variables simply as “reasonable”. An example of an “unreasonable” random
variable would be highly biased Bernoulli random variable; say, Pr[y = 1] =
2−n, Pr[y = 0] = 1 − 2−n, where n is large. This y is not B-reasonable unless
B ≥ 2n.

Let’s give a few illustrations of why reasonable random variables are nice
to work with. First, they have slightly better tail bounds than what you would
get out of the Chebyshev inequality:

Proposition 9.3. Let X ̸≡ 0 be B-reasonable. Then Pr[|X | ≥ t∥X ∥2] ≤ B/t4 for
all t > 0.

Proof. This is immediate from Markov’s inequality:

Pr[|X | ≥ t∥X ∥2] = Pr[X 4 ≥ t4∥X ∥
4
2] ≤ E[X 4]

t4 E[X 2]2 ≤ B
t4 . □

More interestingly, they also satisfy anticoncentration bounds; e.g., you
can upper-bound the probability that they are near 0.

Proposition 9.4. Let X ̸≡ 0 be B-reasonable. Then Pr[|X | > t∥X ∥2] ≥ (1 −
t2)
2/B for all t ∈ [0, 1].

Proof. Applying the Paley–Zygmund inequality (also called the “second mo-
ment method”) to X 2, we get

Pr[|X | ≥ t∥X ∥2] = Pr[X 2 ≥ t2 E[X 2]] ≥ (1 − t2)
2 E[X 2]2

E[X 4] ≥ (1 − t2)
2

B . □

For a generalization of this proposition, see Exercise 9.12.

For a discrete random variable X , a simple condition that guarantees
reasonableness is that X takes on each of its values with nonnegligible prob-
ability:

Proposition 9.5. Let X be a discrete random variable with probability mass
function π. Write λ = min(π) = min
x∈range(X ){Pr[X = x]}.

Then X is (1/λ)-reasonable.

Proof. Let M = ∥X ∥∞. Since Pr[|X | = M] ≥ λ we get

E[X 2] ≥ λM2 =⇒ M2 ≤ E[X 2]/λ.

On the other hand,
 E[X 4] = E[X 2 · X 2] ≤ M2 · E[X 2],

and thus E[X 4] ≤ (1/λ) E[X 2]2 as required. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

250 9. Basics of hypercontractivity

The converse to Proposition 9.5 is certainly not true. For example, if
X = 1pn x1 + · · · + 1pn xn where x ∼ {−1, 1}n, then X is very close to a standard
Gaussian random variable (for n large) and is, unsurprisingly, 3-reasonable.
On the other hand, the “λ” for this X is tiny, 2
−n.

This discussion raises the issue of how you might try to construct an
unreasonable random variable out of independent uniform ±1 bits. By Propo-
sition 9.5, at the very least you must use a lot of them. Furthermore, it also
seems that they must be combined in a high-degree way. For example, to
construct the unreasonable random variable y from Example 9.2 requires
degree n: y = (1 + x1)(1 + x2) · · · (1 + xn)/2n.

Indeed, the idea that high degree is required for unreasonableness is
correct, as the following crucial result shows:

The Bonami Lemma. For each k, if f : {−1, 1}n → R has degree at most k
and x1, . . . , xn are independent, uniformly random ±1 bits, then the random
variable f (x) is 9k-reasonable, i.e.,

E[ f 4] ≤ 9k E[ f 2]
2 ⇐⇒ ∥ f ∥4 ≤ p
3k∥ f ∥2.

In other words, low-degree polynomials of independent uniform ±1 bits are
reasonable. As we will explain later, the Bonami Lemma is a special case of
more general results in the theory of “hypercontractivity”. However, many key
theorems using hypercontractivity – e.g., the KKL Theorem, the Invariance
Principle – really need only the simple Bonami Lemma. (We should also note
that the name “Bonami Lemma” is not standard; however, the result was ﬁrst
proved by Bonami and it’s often used as a lemma, so the name ﬁts. See the
discussion in the notes in Section 9.7.)

One pleasant thing about the Bonami Lemma is that once you decide
to prove it by induction on n, the proof practically writes itself. The only
“non-automatic” step is an application of Cauchy–Schwarz.

Proof of the Bonami Lemma. We assume k ≥ 1 as otherwise f must be
constant and the claim is trivial. The proof is by induction on n. Again,
if n = 0, then f must be constant and the claim is trivial. For n ≥ 1 we
can use the decomposition f (x) = xnDn f (x) + En f (x) (Proposition 2.24), where
deg(Dn f ) ≤ k − 1, deg(En f ) ≤ k, and the polynomials Dn f (x) and En f (x) don’t
depend on xn. For brevity we write f = f (x), d = Dn f (x), and e = En f (x). Now

E[ f 4] = E[(xnd + e)
4]

= E[x4
nd4] + 4 E[x3
nd3 e] + 6 E[x2
nd2 e2] + 4 E[xnde3] + E[e4]

= E[x4
n] E[d4] + 4 E[x3
n] E[d3 e] + 6 E[x2
n] E[d2 e2] + 4 E[xn] E[de3] + E[e4].

In the last step we used the fact that xn is independent of d and e, since Dn f
and En f do not depend on xn. We now use E[xn] = E[x3
n] = 0 and E[x2
n] =

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.1. Low-degree polynomials are reasonable 251

E[x4
n] = 1 to deduce
 E[ f 4] = E[d4] + 6 E[d2 e2] + E[e4]. (9.1)

A similar (and simpler) sequence of steps shows that

E[ f 2] = E[d2] + E[e2]. (9.2)

To upper-bound (9.1), recall that d = Dn f (x) where Dn f is a multilinear
polynomial of degree at most k − 1 depending on n − 1 variables. Thus we
can apply the induction hypothesis to deduce E[d4] ≤ 9k−1 E[d2]2. Similarly,
E[e4] ≤ 9k E[e2]2 since deg(En f ) ≤ k. To bound E[d2 e2] we apply Cauchy–
Schwarz, getting √
E[d4]
√E[e4] and letting us use induction again. Thus we
have
 E[ f 4] ≤ 9k−1 E[d2]
2 + 6
√9k−1 E[d2]2√9k E[e2]2 + 9k E[e2]
2

≤ 9k(E[d2]
2 + 2 E[d2] E[e2] + E[e2]2) = 9k(E[d2] + E[e2]
)2,

where we used 9k−1 E[d2]2 ≤ 9k E[d2]2. In light of (9.2), this completes the
proof. □

Some aspects of the sharpness of the Bonami Lemma are explored in
Exercises 9.2, 9.3, 9.37, and 9.38. Here we make one more observation. At
the end of the proof we used the wasteful-looking inequality 9k−1 E[d2]2 ≤
9k E[d2]2. Tracing back through the proof, it’s easy to see that it would still
be valid even if we just had E[x4
i ] ≤ 9 rather than E[x4
i ] = 1. For example,
the Bonami Lemma holds not just if the xi’s are random bits, but if they are
standard Gaussians, or are uniform on [−1, 1], or there are some of each. We
leave the following as Exercise 9.4.

Corollary 9.6. Let x1, . . . , xn be independent, not necessarily identically dis-
tributed, random variables satisfying E[xi] = E[x3
i ] = 0. (This holds if, e.g.,
each −xi has the same distribution as xi.) Assume also that each xi is B-
reasonable. Let f = F(x1, . . . , xn), where F is a multilinear polynomial of degree
at most k. Then f is max(B, 9)k-reasonable.

As a ﬁrst application of the Bonami Lemma, let us combine it with Propo-
sition 9.4 to show that a low-degree function is not too concentrated around
its mean:

Theorem 9.7. Let f : {−1, 1}n → R be a nonconstant function of degree at
most k; write µ = E[ f ] and σ = √
Var[ f ]. Then

Pr
x∼{−1,1}
[| f (x) − µ| > 1
2 σ] ≥ 1
16 91−k.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

252 9. Basics of hypercontractivity

Proof. Let g = 1
σ ( f −µ), a function of degree at most k satisfying ∥g∥2 = 1. By
the Bonami Lemma, g is 9k-reasonable. The result now follows by applying
Proposition 9.4 to g with t = 1
2 . □

Using this theorem, we can give a short proof of the FKN Theorem from
Chapter 2.5: If f : {−1, 1}n → {−1, 1} has W1[ f ] = 1 − δ then f is O(δ)-close to
±χi for some i ∈ [n].

Proof of the FKN Theorem. Write ℓ = f =1, so E[ℓ2] = 1 − δ by assumption.
We may assume without loss of generality that δ ≤ 1
1600 . The goal of the proof
is to show that Var[ℓ2] is small; speciﬁcally we’ll show that Var[ℓ2] ≤ 6400δ.
This will complete the proof because (using Exercise 1.20 for the ﬁrst equality
below)
 1
2 Var[ℓ2] = ∑

i̸= j ̂f (i)
2 ̂f ( j)
2 = ( n∑

i=1 ̂f (i)
2)2 − n∑

i=1 ̂f (i)
4

= (1 − δ)2 − n∑

i=1 ̂f (i)4 ≥ (1 − 2δ) − n∑

i=1 ̂f (i)4

and hence Var[ℓ2] ≤ 6400δ implies

1 − 3202δ ≤ n∑

i=1 ̂f (i)
4 ≤ max
i { ̂f (i)2} n∑

i=1 ̂f (i)2 ≤ max
i { ̂f (i)
2} ≤ max
i {| ̂f (i)|},

as required.

To bound Var[ℓ2] we ﬁrst apply Theorem 9.7 to the degree-2 function ℓ2;
this yields
 Pr[∣
∣ℓ2 − (1 − δ)∣
∣ ≥ 1
2 √
Var[ℓ2]
] ≥ 1
16 91−2 = 1
144 .

Now suppose by way of contradiction that Var[ℓ2] > 6400δ; then the above
implies
 1
144 ≤ Pr[∣
∣ℓ2 − (1 − δ)
∣
∣ > 40
p
δ] ≤ Pr
[∣
∣ℓ2 − 1∣
∣ > 39
p
δ]. (9.3)

This says that |ℓ| is frequently far from 1. Since | f | = 1 always, we can deduce
that | f − ℓ|2 is frequently large. More precisely, a short calculation (Exer-
cise 9.5) shows that ( f −ℓ)
2 ≥ 169δ whenever |ℓ2 −1| > 39
p
δ. But now (9.3) im-
plies E[( f −ℓ)
2] ≥ 1
144 ·169δ > δ, a contradiction since E[( f −ℓ)
2] = 1−W
1[ f ] = δ
by assumption. □

9.2. Small subsets of the hypercube are noise-sensitive

An immediate consequence of the Bonami Lemma is that for any f : {−1, 1}n →
R and k ∈ N ,
 ∥T1/
p
3 f =k∥4 = 1
p
3k ∥ f =k∥4 ≤ ∥ f =k∥2. (9.4)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.2. Small subsets of the hypercube are noise-sensitive 253

This is a special case of the (2, 4)-Hypercontractivity Theorem (whose name
will be explained shortly), which says that the assumption of degree-k homo-
geneity is not necessary:

(2, 4)-Hypercontractivity Theorem. Let f : {−1, 1}n → R . Then

∥T1/
p
3 f ∥4 ≤ ∥ f ∥2.

It almost looks as though you could prove this theorem simply by sum-
ming (9.4) over k. In fact that proof strategy can be made to work given a
few extra tricks (see Exercise 9.6), but it’s just as easy to repeat the induction
technique used for the Bonami Lemma.

Proof. We’ll prove E[T1/
p
3 f (x)4] ≤ E[ f (x)2]2 using the same induction as in
the Bonami Lemma. Retaining the notation d and e, and using the shorthand
T = T1/p
3, we have
 T f = xn · 1p
3 Td + Te.

Similar computations to those in the Bonami Lemma proof yield

E[(T f )
4] = ( 1p
3 )4 E[(Td)
4] + 6
( 1p
3 )2 E[(Td)
2(Te)
2] + E[(Te)
4]

≤ E[(Td)4] + 2 E[(Td)
2(Te)
2] + E[(Te)
4]

≤ E[(Td)4] + 2√
E[(Td)4]
√
E[(Te)4] + E[(Te)
4]

≤ E[d2]
2 + 2 E[d2] E[e2] + E[e2]
2

= (
E[d2] + E[e2]
)2 = E[ f 2]
2,

where the second inequality is Cauchy–Schwarz, the third is induction, and
the ﬁnal equality is a simple computation analogous to (9.2). □

The name “hypercontractivity” in this theorem describes the fact that not
only is T1/p
3 a “contraction” on L2({−1, 1}n) – meaning ∥T1/p
3 f ∥2 ≤ ∥ f ∥2 for
all f (Exercise 2.33) – it’s even a contraction when viewed as an operator from
L2({−1, 1}n) to L4({−1, 1}n). You should think of hypercontractivity theorems
as quantifying the extent to which Tρ is a “smoothing”, or “reasonable-izing”
operator.

Unfortunately the quantity ∥T1/
p
3 f ∥4 in the (2, 4)-Hypercontractivity The-
orem does not have an obvious combinatorial meaning. On the other hand,
the quantity

∥T1/p
3 f ∥2 = √
〈T1/
p
3 f , T1/
p
3 f 〉 = √
〈 f , T1/p
3T1/p
3 f 〉 = √
Stab1/3[ f ],

does have a nice combinatorial meaning. And we can make this quantity
appear in the Hypercontractivity Theorem via a simple trick from analysis,
just using the fact that T1/
p
3 is a self-adjoint operator. We “ﬂip the norms
across 2” using Hölder’s inequality:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

254 9. Basics of hypercontractivity

(4/3, 2)-Hypercontractivity Theorem. Let f : {−1, 1}n → R . Then

∥T1/
p
3 f ∥2 ≤ ∥ f ∥4/3;

i.e., Stab1/3[ f ] ≤ ∥ f ∥
2
4/3. (9.5)

Proof. Writing T = T1/
p
3 for brevity we have

∥T f ∥
2
2 = 〈T f , T f 〉 = 〈 f , TT f 〉 ≤ ∥ f ∥4/3∥TT f ∥4 ≤ ∥ f ∥4/3∥T f ∥2 (9.6)

by Hölder’s inequality and the (2, 4)-Hypercontractivity Theorem. Dividing
through by ∥T f ∥2 (which we may assume is nonzero) completes the proof. □

In the inequality (9.5) the left-hand side is a natural quantity. The right-
hand side is just 1 when f : {−1, 1}n → {−1, 1}, which is not very interesting.
But if we instead look at f : {−1, 1}n → {0, 1} we get something very interesting:

Corollary 9.8. Let A ⊆ {−1, 1}n have volume α; i.e., let 1A : {−1, 1}n → {0, 1}
satisfy E[1A] = α. Then

Stab1/3[1A] = Pr
x∼{−1,1}n
y∼N1/3(x)
[x ∈ A, y ∈ A] ≤ α
3/2.

Equivalently (for α > 0),
 Pr
x∼A
y∼N1/3(x)[y ∈ A] ≤ α
1/2.

Proof. This is immediate from inequality (9.5), since

∥1A∥
2
4/3 =
( E
x [|1A(x)|4/3]3/4)2 = E
x [1A(x)]3/2 = α
3/2. □

See Section 9.5 for the generalization of this corollary to noise rates other
than 1/3.

Example 9.9. Assume α = 2
−k, k ∈ N +, and A is a subcube of codimension k;
e.g., 1A : F n
2 → {0, 1} is the logical AND function on the ﬁrst k coordinates.
For every x ∈ A, when we form y ∼ N1/3(x) we’ll have y ∈ A if and only if the
ﬁrst k coordinates of x do not change, which happens with probability (2/3)k =
(2/3)log(1/α) = α
log(3/2) ≈ α
.585 ≤ α
1/2. In fact, the bound α
1/2 in Corollary 9.8 is
essentially sharp when A is a Hamming ball; see Exercise 9.24.

We can phrase Corollary 9.8 in terms of the expansion in a certain graph:

Deﬁnition 9.10. For n ∈ N + and ρ ∈ [−1, 1], the n-dimensional ρ-stable hy-
percube graph is the edge-weighted, complete directed graph on vertex set
{−1, 1}n in which the weight on directed edge (x, y) ∈ {−1, 1}n × {−1, 1}n is equal
to Pr[(x, y) = (x, y)] when (x, y) is a ρ-correlated pair. If ρ = 1 − 2δ for δ ∈ [0, 1],
we also call this the δ-noisy hypercube graph. Here the weight on (x, y) is

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.2. Small subsets of the hypercube are noise-sensitive 255

Pr[(x, y) = (x, y)] where x ∼ {−1, 1}n is uniform and y is formed from x by
negating each coordinate independently with probability δ.

Remark 9.11. The edge weights in this graph are nonnegative and sum to 1.
The graph is also “regular” in the sense that for each x ∈ {−1, 1}n the sum of
all the edge weight leaving (or entering) x is 2−n. You can also consider the
graph to be undirected, since the weight on (x, y) is the same as the weight
on (y, x); in this viewpoint, the weight on the undirected edge (x, y) would be
21−nδ∆(x,y)(1 − δ)n−∆(x,y). In fact, the graph is perhaps best thought of as the
discrete-time Markov chain on state space {−1, 1}n in which a step from state
x ∈ {−1, 1}n consists of moving to state y ∼ Nρ(x). This is a reversible chain
with the uniform stationary distribution. Each discrete step is equivalent to
running the “usual” continuous-time Markov chain on the hypercube for time
t = ln(1/ρ) (assuming ρ ∈ [0, 1]).

With this deﬁnition in place, we can see Corollary 9.8 as saying that the
1/3-stable (equivalently, 1/3-noisy) hypercube graph is a “small-set expander”:
given any small α-fraction of the vertices A, almost all of the edge weight
touching A is on its boundary. More precisely, if we choose a random vertex
x ∈ A and take a random edge out of x (with probability proportional to its
edge weight), we end up outside A with probability at least 1 − α
1/2. You
can compare this with the discussion surrounding the Level-1 Inequality in
Section 5.4, which is the analogous statement for the ρ-stable hypercube
graph “in the limit ρ → 0+”. The appropriate statement for general ρ is
appears in Section 9.5 as the “Small-Set Expansion Theorem”.

Corollary 9.8 would apply equally well if 1A were replaced by a function g :
{−1, 1}n → {−1, 0, 1}, with α denoting Pr[g ̸= 0] = E[|g|] = E[g2]. This situation
occurs naturally when g = Di f for some Boolean-valued f : {−1, 1}n → {−1, 1}.
In this case Stab1/3[g] = Inf(1/3)
i [ f ], the 1/3-stable inﬂuence of i on f . We
conclude that for a Boolean-valued function, if the inﬂuence of i is small then
its 1/3-stable inﬂuence is much smaller:

Corollary 9.12. Let f : {−1, 1}n → {−1, 1}. Then Inf(1/3)
i [ f ] ≤ Infi[ f ]
3/2 for all i.

We remark that the famous KKL Theorem (stated in Chapter 4.2) more or
less follows by summing the above inequality over i ∈ [n]; if you’re impatient
to see its proof you can skip directly to Section 9.6 now.

Let’s take one more look at the “small-set expansion result”, Corollary 9.8.
Since noise stability roughly measures how “low” a function’s Fourier weight
is, this corollary implies that a function f : {−1, 1}n → {0, 1} with small mean α
cannot have much of its Fourier weight at low degree. More precisely, for any

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

256 9. Basics of hypercontractivity

k ∈ N we have

α
3/2 ≥ Stab1/3[ f ] ≥ (1/3)kW≤k[ f ] =⇒ W≤k[ f ] ≤ 3kα
3/2. (9.7)

For k = 1 this gives W≤1[ f ] ≤ 3α
3/2, which is nontrivial but not as strong
as the Level-1 Inequality from Section 5.4. But (9.7) also gives us “level-k
inequalities” for larger values of k. For example,

W≤.25 log(1/α)[ f ] ≤ α
−.25 log 3+3/2 ≤ α
1.1 ≪ α = ∥ f ∥2
2;

i.e., almost all of f ’s Fourier weight is above degree .25 log(1/α). We will give
slightly improved versions of these level-k inequalities in Section 9.5.

9.3. (2, q)- and (p, 2)-hypercontractivity for a single bit

Although you can get a lot of mileage out of studying the 4-norm of random
variables, it’s also natural to consider other norms. For example, we would
get improved versions of our concentration and anticoncentration results,
Propositions 9.3 and 9.4, if we could bound the higher norms of a random
variable in terms of its 2-norm. As we’ll see, we can also get stronger “level-k
inequalities” by bounding the (2+ϵ)-norm of a Boolean function for small ϵ > 0.

We started with the 4-norm due to the simplicity of the proofs of the
Bonami Lemma and the (2, 4)-Hypercontractivity Theorem. To generalize
these results to other norms it’s a bit more elegant to work with the latter.
Partly this is because it’s “formally stronger” (see Theorem 9.21). But the
main reason is that the hypercontractivity version alleviates the inelegant
issue that being “B-reasonable” is not translation-invariant. Thus instead of
generalizing the condition that ∥ρ X ∥4 ≤ ∥X ∥2 (“X is ρ−4-reasonable”) we’ll
generalize the condition that ∥a + ρbX ∥4 ≤ ∥a + bX ∥2 (cf. the n = 1 case of the
(2, 4)-Hypercontractivity Theorem).

Deﬁnition 9.13. Let 1 ≤ p ≤ q ≤ ∞ and let 0 ≤ ρ < 1. We say that a real
random variable X (with ∥X ∥q < ∞) is (p, q, ρ)-hypercontractive if

∥a + ρbX ∥q ≤ ∥a + bX ∥p for all constants a, b ∈ R .

Remark 9.14. By homogeneity, it sufﬁces to check the condition for a = 1,
b ∈ R or for a ∈ R , b = 1 (cf. Exercise 9.9(a)). It’s also true (Exercise 9.11) that
if X is (p, q, ρ)-hypercontractive then it is (p, q, ρ′)-hypercontractive for ρ′ < ρ
as well.

In Exercise 9.10 you will show that if X is hypercontractive then E[X ]
must be 0. Thus hypercontractivity, like reasonableness, is not a translation-
invariant notion. Nevertheless, the fact that the deﬁnition involves transla-
tion by an arbitrary a greatly facilitates proofs by induction. For example, an
elegant property we gain from the deﬁnition is the following (Exercise 10.2):

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.3. (2, q)- and (p, 2)-hypercontractivity for a single bit 257

Proposition 9.15. Let X and Y be independent (p, q, ρ)-hypercontractive ran-
dom variables. Then X + Y is also (p, q, ρ)-hypercontractive.

The n = 1 case of our (2, 4)-Hypercontractivity Theorem precisely says that
a single uniformly random ±1 bit x is (2, 4, 1/p
3)-hypercontractive;
the (4/3, 2)-Hypercontractivity Theorem says that the bit x is also (4/3, 2, 1/
p
3)-
hypercontractive. We’ll spend the remainder of this section generalizing these
facts to (2, q, ρ)- and (p, 2, ρ)-hypercontractivity for other values of p and q.
We remark that in our study of hypercontractivity we’ll focus mainly on the
cases of p = 2 or q = 2. The study of hypercontractivity for p, q ̸= 2 and for
random variables other than uniform ±1 bits is deferred to Chapter 10.

We now consider hypercontractivity of a uniformly random ±1 bit x. We
know that x is (2, q, 1/
p
3)-hypercontractive for q = 4; what about other values
of q? Things are most pleasant when q is an even integer because then you
don’t need to take the absolute value when computing ∥a +ρbX ∥q. So let’s try
q = 6.

Proposition 9.16. For x a uniform ±1 bit, we have ∥a + ρbx∥6 ≤ ∥a + bx∥2 for
all a, b ∈ R if (and only if) ρ ≤ 1/
p
5. That is, x is (2, 6, 1/
p
5)-hypercontractive.

Proof. Raising the inequality to the 6th power, we need to show

E[(a + ρbx)6] ≤ E[(a + bx)2]3. (9.8)

The result is trivial when a = 0; otherwise, we may assume a = 1 by homo-
geneity. We expand both quantities inside expectations and use the fact that
E[xk] is 0 when k is odd and 1 when k is even. Thus (9.8) is equivalent to

1 + 15ρ2b2 + 15ρ4b4 + ρ6b6 ≤ (1 + b2)3 = 1 + 3b2 + 3b4 + b6. (9.9)

Comparing the two sides term-by-term we see that the coefﬁcient on b2 is
the limiting factor: in order for (9.9) to hold for all b ∈ R it is sufﬁcient that
15ρ2 ≤ 3; i.e., ρ ≤ 1/p
5. By considering b → 0 it’s also easy to see that this
condition is necessary. □

If you repeat this analysis for the case of q = 8 you’ll ﬁnd that again the
limiting factor is the coefﬁcient on b2, and that x is (2, 8, ρ)-hypercontractive
if (and only if) (8
2)
ρ2 ≤ (4
1
); i.e., ρ ≤ 1/p
7. In light of this it is natural to guess
that the following is true:

Theorem 9.17. Let x be a uniform ±1 bit and let q ∈ (2, ∞]. Then ∥a+ρbx∥q ≤
∥a + bx∥2 for all a, b ∈ R assuming ρ ≤ 1/
√q − 1.

Equivalent statements are that ∥a + (1/√q − 1)bx∥
2
q ≤ a2 + b2, that x is
(2, q, 1/√q − 1)-hypercontractive, and that ∥T1/
pq−1 f ∥q ≤ ∥ f ∥2 holds for any

f : {−1, 1} → R .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

258 9. Basics of hypercontractivity

For q an even integer it is not hard (see Exercise 9.36) to prove Theo-
rem 9.17 just as we did for q = 6. Indeed, the proof works even under more
general moment conditions on x, as in Corollary 9.6. Unfortunately, obtaining
Theorem 9.17 for all real q > 2 takes some more tricks. A natural idea is to try
forging ahead as in Proposition 9.16, using the series expansions for (1+ρbx)q

and (1+ b2)q/2 provided by the Generalized Binomial Theorem. However, even
when |b| < 1 (so that convergence is not an issue) there is a difﬁculty because
the coefﬁcients in the expansion of (1 + b2)q/2 are sometimes negative.

Luckily, this issue of negative coefﬁcients in the series expansion goes
away if you try to prove the analogous (p, 2, ρ)-hypercontractivity statement.
Thus the slick proof of Theorem 9.17 proceeds by ﬁrst proving that statement,
then “ﬂipping the norms across 2”.

Theorem 9.18. Let x be a uniform ±1 bit and let 1 ≤ p < 2. Then ∥a+ρbx∥2 ≤
∥a + bx∥p for all a, b ∈ R assuming 0 ≤ ρ ≤ √p − 1. That is, x is (p, 2, √p − 1)-
hypercontractive.

Proof. By Remark 9.14 we may assume a = 1 and ρ = √p − 1. By Exercise 9.7
we may also assume without loss of generality that 1 + bx ≥ 0 for x ∈ {−1, 1};
i.e., that |b| ≤ 1. It then sufﬁces to prove the result for all |b| < 1 because the
|b| = 1 case follows by continuity. Writing b = ϵ for the sake of intuition, we
need to show
 ∥1 + √p − 1 · ϵx∥p
2 ≤ ∥1 + ϵx∥p
p

⇐⇒ E[(1 + √p − 1 · ϵx)
2]p/2 ≤ E[(1 + ϵx)p]. (9.10)

Here we were able to drop the absolute value on the right-hand side because
|ϵ| < 1. The left-hand side of (9.10) is

(1 + (p − 1)ϵ2)p/2 ≤ 1 + p(p−1)
2 ϵ2, (9.11)

where we used the inequality (1 + t)θ ≤ 1 + θt for t ≥ 0 and 0 ≤ θ ≤ 1 (easily
proved by comparing derivatives in t). As for the right-hand side of (9.10),
since |ϵx| < 1 we may use the Generalized Binomial Theorem to show it equals

E [1 + pϵx + p(p−1)
2! ϵ2x2 + p(p−1)(p−2)
3! ϵ3x3 + p(p−1)(p−2)(p−3)
4! ϵ4x4 + · · · ]

= 1 + pϵ E[x] + p(p−1)
2! ϵ2 E[x2] + p(p−1)(p−2)
3! ϵ3 E[x3] + p(p−1)(p−2)(p−3)
4! ϵ4 E[x4] + · · ·

= 1 + p(p−1)
2 ϵ2 + p(p−1)(p−2)(p−3)
4! ϵ4 + p(p−1)(p−2)(p−3)(p−4)(p−5)
6! ϵ6 + · · · .

In light of (9.11), to verify (9.10) it sufﬁces to note that each “post-quadratic”
term above, p(p−1)(p−2)(p−3)···(p−(2k−1))
(2k)! ϵ2k,

is nonnegative. This follows from 1 ≤ p ≤ 2: the numerator has two positive
factors and an even number of negative factors. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.4. Two-function hypercontractivity and induction 259

To deduce Theorem 9.17 from Theorem 9.18 we again just need to ﬂip the
norms across 2 using the fact that Tρ is self-adjoint. This is accomplished
by taking Ω = {−1, 1}, π = π1/2, q = 2, T = Tpp−1, and C = 1 in the following

proposition (and noting that 1/
√p′ − 1 = √p − 1):

Proposition 9.19. Let T be a self-adjoint operator on L2(Ω, π), let 1 ≤ p, q ≤
∞, and let p′, q′ be their conjugate Hölder indices. Assume ∥T f ∥q ≤ C∥ f ∥p for
all f . Then ∥T g∥p′ ≤ C∥g∥q′ for all g.

Proof. This follows from

∥T g∥p′ = sup
∥ f ∥p=1
〈 f , T g〉 = sup
∥ f ∥p=1〈T f , g〉 ≤ sup
∥ f ∥p=1 ∥T f ∥q∥g∥q′ ≤ C∥g∥q′,

where the ﬁrst equality is the sharpness of Hölder’s inequality, the second
equality holds because T is self-adjoint, the subsequent inequality is Hölder’s,
and the ﬁnal inequality uses the hypothesis ∥T f ∥q ≤ C∥ f ∥p. □

At this point we have established that if x is a uniform ±1 bit, then it
is (2, q, 1/
√q − 1)-hypercontractive and (p, 2, √p − 1)-hypercontractive. In the
next section we will give a very simple induction which transforms these
facts into the full (2, q)- and (p, 2)-Hypercontractivity Theorems stated at the
beginning of the chapter.

9.4. Two-function hypercontractivity and induction

At this point we have established that if f : {−1, 1} → R then for any p ≤ 2 ≤ q,

∥Tpp−1 f ∥2 ≤ ∥ f ∥p, ∥T1/
pq−1 f ∥q ≤ ∥ f ∥2.

We would like to extend these facts to the case of general f : {−1, 1}n → R ;
i.e., establish the (p, 2)- and (2, q)-Hypercontractivity Theorems stated at the
beginning of the chapter. A natural approach is induction.

In analysis of Boolean functions, there are two methods for proving state-
ments about f : {−1, 1}n → R by induction on n. One method, which might be
called “induction by derivatives”, uses the decomposition f (x) = xnDn f (x) +
En f (x). We saw this approach in our inductive proof of the Bonami Lemma.
The other method, which might be called “induction by restrictions”, goes via
the subfunctions f±1 obtained by restricting the nth coordinate of f to ±1. We
saw this approach in our proof of the OSSS Inequality in Chapter 8.6. In both
methods we reduce inductively from one function f to two functions: either
Dn f and En f , or f−1 and f+1. Because of this, when trying to prove a fact
by induction on n it’s often helpful to try proving a generalized fact about
two functions. Our proof of the OSSS Inequality gives a good example of this
technique.
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

260 9. Basics of hypercontractivity

So to facilitate induction, let’s ﬁnd a two-function version of the hypercon-
tractivity statements we’ve proven so far. Perhaps the most natural statement
we’ve seen is the noise-stability rephrasing of the (4/3, 2)-Hypercontractivity
Theorem, namely Stab1/3[ f ] ≤ ∥ f ∥
2
4/3. At least in the case n = 1, our work in
the previous section (Theorem 9.18) generalizes this to Stabp−1[ f ] ≤ ∥ f ∥
2
p for
1 ≤ p ≤ 2. I.e., Stabρ[ f ] = E
(x,y)
ρ-correlated
[ f (x) f (y)] ≤ ∥ f ∥
2
1+ρ

for 0 ≤ ρ ≤ 1. Looking at this, you might naturally guess a (correct) general-
ization for two functions f , g : {−1, 1}n → R , namely

E
(x,y)
ρ-correlated
[ f (x)g(y)] ≤ ∥ f ∥1+ρ∥g∥1+ρ. (9.12)

We have a nice interpretation of this inequality when f , g : {−1, 1}n → {0, 1}
are indicators of subsets A, B ⊆ {−1, 1}n as in Corollary 9.8; it gives an upper
bound on the probability of going from A to B in one step on the ρ-stable
hypercube graph. This bound is sharp when A and B have the same volume,
but for A and B of different sizes you might imagine it’s helpful to measure f
and g by different norms in (9.12). To see what we can expect, let’s break up
the ρ-correlation in (9.12) into two parts; say, write

ρ = prs, 0 ≤ r, s ≤ 1,

and use E
(x,y)prs-correlated

[ f (x)g(y)] = E[Tpr f · Tps g].

Then Cauchy–Schwarz implies

E
(x,y)
ρ-correlated
[ f (x)g(y)] = E[Tpr f · Tps g] ≤ ∥Tpr f ∥2∥Tps g∥2 ≤ ∥ f ∥1+r∥g∥1+s,

(9.13)
where the last step used (p, 2)-hypercontractivity – which we have so far
only proven in the case n = 1 (Theorem 9.18). The inequality (9.13), restated
below, is precisely the desired two-function version of the (2, q)- and (p, 2)-
Hypercontractive Theorems.

(Weak) Two-Function Hypercontractivity Theorem. Let f , g : {−1, 1}n →
R , let 0 ≤ r, s ≤ 1, and assume 0 ≤ ρ ≤ prs ≤ 1. Then

E
(x,y)
ρ-correlated

[ f (x)g(y)] ≤ ∥ f ∥1+r∥g∥1+s.

We call this the “Weak” Two-Function Hypercontractivity Theorem be-
cause the hypothesis r, s ≤ 1 is not actually necessary; see Chapter 10.1. As
mentioned, we have so far established this theorem in the case n = 1. However,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.4. Two-function hypercontractivity and induction 261

the beauty of hypercontractivity in this form is that it extends to general n
by an almost trivial induction. The form of the induction is “induction by
restrictions”. (It’s also possible – but a little trickier – to extend the (2, q)-
Hypercontractivity Theorem from n = 1 to general n via “induction by deriva-
tives”; see Exercise 9.16.) For future use, we will write the induction in more
general notation.

Two-Function Hypercontractivity Induction Theorem. Let 0 ≤ ρ ≤ 1
and assume that E
(x,y)
ρ-correlated

[ f (x)g(y)] ≤ ∥ f ∥p∥g∥q

holds for every f , g ∈ L2(Ω, π). Then the inequality also holds for every f , g ∈
L2(Ωn, π⊗n).

Proof. The proof is by induction on n, with the n = 1 case holding by assump-
tion. For n > 1, let f , g ∈ L2(Ωn, π⊗n) and let (x, y) denote a ρ-correlated pair
under π⊗n. We’ll use the notation x = (x′, xn) where x′ = (x1, . . . , xn−1), and
similar notation for y. Note that (x′, y′) and (xn, yn) are both ρ-correlated
pairs (of length n−1 and 1, respectively). We’ll also write f xn = f[n−1]|xn for the
restriction of f in which the last coordinate is ﬁxed to value xn, and similarly
for g. Now

E
(x,y)[ f (x)g(y)] = E
(xn,yn) E
(x′,y′)
[ f xn (x′)g yn (y′)] ≤ E
(xn,yn)[∥ f xn ∥p∥g yn ∥q]

by induction. If we write F ∈ L2(Ω, π) for the function xn 7→ ∥ f xn ∥p and simi-
larly write G(yn) = ∥g yn ∥q, then we may continue the above as

E
(xn,yn)[∥ f xn ∥p∥g yn ∥q] = E
(xn,yn)
[F(xn)G(yn)] ≤ ∥F∥p,xn ∥G∥q,yn ,

where we used the base case of the induction. Finally,

∥F∥p,xn = E
xn[|F(xn)|p]
1/p = E
xn[∥ f xn ∥p
p]
1/p = (E
xn E
x′ | f xn (x′)|p])1/p = ∥ f ∥p

by deﬁnition, and similarly for ∥G∥q,yn . Thus we have established E[ f (x)g(y)] ≤
∥ f ∥p∥g∥q, completing the induction. □

Remark 9.20. More generally, if we assume the inequality holds over each
of (Ω1, π1), . . . , (Ωn, πn), then it also holds over (Ω1 × · · · × Ωn, π1 ⊗ · · · ⊗ πn); the
only change needed to the proof is notational.

At this point, we have fully established the Weak Two-Function Hyper-
contractivity Theorem. By taking g = f and r = s = ρ in the theorem we
obtain the full (p, 2)-Hypercontractivity Theorem stated at the beginning of
the chapter. Finally, by applying Proposition 9.19 we also obtain the (2, q)-
Hypercontractivity Theorem for all f : {−1, 1}n → R .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

262 9. Basics of hypercontractivity

9.5. Applications of hypercontractivity

With the (2, q)- and (p, 2)-Hypercontractivity Theorems in hand, let’s revisit
some applications we saw in Sections 9.1 and 9.2. We begin by deducing a
generalization of the Bonami Lemma:

Theorem 9.21. Let f : {−1, 1}n → R have degree at most k. Then ∥ f ∥q ≤
√q − 1k∥ f ∥2 for any q ≥ 2.

Proof. We have
 ∥ f ∥
2
q = ∥T1/
pq−1Tpq−1 f ∥
2
q ≤ ∥Tpq−1 f ∥
2
2

using the (2, q)-Hypercontractivity Theorem. (Here we are extending the
deﬁnition of Tρ to ρ > 1 via Tρ f = ∑ j ρ j f = j; see also Remark 8.29.) The result
now follows since

∥Tpq−1 f ∥
2
2 = k∑

j=0(q − 1) jW j[ f ] ≤ (q − 1)k k∑

j=0 W j[ f ] = (q − 1)k∥ f ∥
2
2. □

Using a trick similar to the one in our proof of the (4/3, 2)-Hypercontractivity
Theorem you can use this to deduce ∥ f ∥2 ≤ (1/√p − 1)k∥ f ∥p when f has de-
gree k for any 1 ≤ p ≤ 2; see Exercise 9.14. However, a different trick yields a
strictly better result, including a ﬁnite bound for p = 1:

Theorem 9.22. Let f : {−1, 1}n → R have degree at most k. Then ∥ f ∥2 ≤ ek∥ f ∥1.

More generally, for 1 ≤ p ≤ 2 it holds that ∥ f ∥2 ≤ (e
 2
p −1)k∥ f ∥p.

Proof. We prove the statement about the 1-norm, leaving the case of general
1 ≤ p ≤ 2 to Exercise 9.15. For ϵ > 0, let 0 < θ < 1 be the solution of 1
2 = θ
1 + 1−θ
2+ϵ
(namely, θ = 1
2 ϵ
1+ϵ ). Applying the general version of Hölder’s inequality and
then Theorem 9.21, we get

∥ f ∥2 ≤ ∥ f ∥
1−θ
2+ϵ ∥ f ∥
θ
1 ≤ p
1 + ϵk(1−θ)∥ f ∥
1−θ
2 ∥ f ∥θ
1.

Dividing by ∥ f ∥1−θ
2 (which we may assume is nonzero) and then raising the
result to the power of 1/θ yields

∥ f ∥2 ≤ ((1 + ϵ) 1−θ
2θ )k ∥ f ∥1 = ((1 + ϵ) 1
ϵ + 1
2 )k ∥ f ∥1.

The result follows by taking the limit as ϵ → 0. □

In the linear case of k = 1, Theorems 9.21 and 9.22 taken together show
that c p∥ ∑i ai xi∥2 ≤ ∥ ∑i ai xi∥p ≤ C p∥ ∑i ai xi∥2 for some constants 0 < c p < C p
depending only on p ∈ [1, ∞). This fact is known as Khintchine’s Inequality.

Theorem 9.21 can be used to get a strong concentration bound for degree-k
Boolean functions. Chernoff tells us that the probability a linear form ∑ ai xi

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.5. Applications of hypercontractivity 263

exceeds t standard deviations decays like exp(−Θ(t2)). The following theorem
generalizes this to degree-k forms, with decay exp(−Θ(t2/k)):

Theorem 9.23. Let f : {−1, 1}n → R have degree at most k. Then for any

t ≥ p
2ek we have
 Pr
x∼{−1,1}n[| f (x)| ≥ t∥ f ∥2] ≤ exp (
− k
2e t2/k) .

Proof. We may assume ∥ f ∥2 = 1 without loss of generality. Let q ≥ 2 be a
parameter to be chosen later. By Markov’s inequality,

Pr[| f (x)| ≥ t] = Pr[| f (x)|q ≥ tq] ≤ E[| f (x)|q]
tq .

By Theorem 9.21 we have

E[| f (x)|q] ≤ (√q − 1k)q∥ f ∥q
2 = (q − 1)
(k/2)q ≤ q(k/2)q.

Thus Pr[| f (x)| ≥ t] ≤ (qk/2/t)q. It’s not hard to see that the q that minimizes
this expression should be just slightly less than t2/k. Speciﬁcally, by choosing
q = t2/k/e ≥ 2 we get

Pr[| f (x)| ≥ t] ≤ exp(−(k/2)q) = exp (− k
2e t2/k)

as claimed. □

We can use Theorem 9.22 to get a “one-sided” analogue of Theorem 9.7,
showing that a low-degree function exceeds its mean with noticeable proba-
bility:

Theorem 9.24. Let f : {−1, 1}n → R be a nonconstant function of degree at
most k. Then
 Pr
x∼{−1,1}n[ f (x) > E[ f ]] ≥ 1
4 e−2k.

Proof. We may assume E[ f ] = 0 without loss of generality. We then have

1
2 ∥ f ∥1 = 1
2 (
E[ f · 1{ f (x)>0}] − E[ f · (1 − 1{ f (x)>0})]) = E[ f · 1{ f (x)>0}];

hence,

1
4 ∥ f ∥
2
1 = E[ f · 1{ f (x)>0}]
2 ≤ E[ f 2] · E[1
2
{ f (x)>0}] ≤ e2k∥ f ∥
2
1 · Pr[ f (x) > 0]

using Cauchy–Schwarz and Theorem 9.22. The result follows. □

Next we turn to noise stability. Using the (p, 2)-Hypercontractivity Theo-
rem we can immediately deduce the following generalization of Corollary 9.8:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

264 9. Basics of hypercontractivity

Small-Set Expansion Theorem. Let A ⊆ {−1, 1}n have volume α; i.e., let
1A : {−1, 1}n → {0, 1} satisfy E[1A] = α. Then for any 0 ≤ ρ ≤ 1,

Stabρ[1A] = Pr
x∼{−1,1}n
y∼Nρ(x)
 [x ∈ A, y ∈ A] ≤ α
 2
1+ρ .

Equivalently (for α > 0),
 Pr
x∼A
y∼Nρ(x)
[y ∈ A] ≤ α
 1−ρ
1+ρ .

In other words, the δ-noisy hypercube is a small-set expander for any δ > 0:
the probability that one step from a random x ∼ A stays inside A is at most
α
δ/(1−δ). It’s also possible to derive a “two-set” generalization of this fact using
the Two-Function Hypercontractivity Theorem; we defer the discussion to
Chapter 10.1 since the most general result requires the non-weak form of the
theorem. We can also obtain the generalization of Corollary 9.12:

Corollary 9.25. Let f : {−1, 1}n → {−1, 1}. Then for any 0 ≤ ρ ≤ 1 we have

Inf(ρ)
i [ f ] ≤ Infi[ f ]
 2
1+ρ for all i.

Finally, from the Small-Set Expansion Theorem we see that indicators
of small-volume sets are not very noise-stable and hence can’t have much
of their Fourier weight at low levels. Indeed, using hypercontractivity we
can deduce the Level-1 Inequality from Chapter 5.4 and also generalize it to
higher degrees.

Level-k Inequalities. Let f : {−1, 1}n → {0, 1} have mean E[ f ] = α and let
k ∈ N + be at most 2 ln(1/α). Then

W
≤k[ f ] ≤ ( 2e
k ln(1/α))k α
2.

Proof. By the Small-Set Expansion Theorem,

W≤k[ f ] ≤ ρ−kStabρ[ f ] ≤ ρ−kα
2/(1+ρ) ≤ ρ−kα
2(1−ρ)

for any 0 < ρ ≤ 1. Basic calculus shows the right-hand side is minimized when
ρ = k
2 ln(1/α) ≤ 1; substituting this into ρ−kα
2(1−ρ) yields the claim. □

For the case k = 1, a slightly different argument gives the sharp Level-1
Inequality W
1[ f ] ≤ 2α
2 ln(1/α); see Exercise 9.18.

9.6. Highlight: The Kahn–Kalai–Linial Theorem

Recalling the social choice setting of Chapter 2.1, consider a 2-candidate, n-
voter election using a monotone voting rule f : {−1, 1}n → {−1, 1}. We assume
the impartial culture assumption (that the votes are independent and uni-
formly random), but with a twist: one of the candidates, say b ∈ {−1, 1}, is able

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.6. Highlight: The Kahn–Kalai–Linial Theorem 265

to secretly bribe k voters, ﬁxing their votes to b. (Since f is monotone, this is
always the optimal way for the candidate to ﬁx the bribed votes.) How much
can this inﬂuence the outcome of the election? This question was posed by
Ben-Or and Linial in a 1985 work [BL85, BL90]; more precisely, they were
interested in designing (unbiased) voting rules f that minimize the effect of
any bribed k-coalition.

Let’s ﬁrst consider k = 1. If voter i is bribed to vote for candidate b
(but all other votes remain uniformly random), this changes the bias of f by
b ̂f (i) = bInfi[ f ]. Here we used the assumption that f is monotone (i.e., Propo-
sition 2.21). This led Ben-Or and Linial to the question of which unbiased
f : {−1, 1}n → {−1, 1} has the least possible maximum inﬂuence:

Deﬁnition 9.26. Let f : {−1, 1}n → R . The maximum inﬂuence of f is

MaxInf[ f ] = max{Infi[ f ] : i ∈ [n]}.

Ben-Or and Linial constructed the (nearly) unbiased Tribesn : {−1, 1}n →
{−1, 1} function (from Chapter 4.2) and noted that MaxInf[Tribesn] = O( log n
n ).

They further conjectured every unbiased function f has MaxInf[ f ] = Ω( log n
n ).
This conjecture was famously proved by Kahn, Kalai, and Linial [KKL88]:

Kahn–Kalai–Linial (KKL) Theorem. For any f : {−1, 1}n → {−1, 1},

MaxInf[ f ] ≥ Var[ f ] · Ω( log n
n
 ).

Notice that the theorem says something sensible even for very biased
functions f , i.e., those with low variance. The variance of f is indeed the right
“scaling factor” since 1
n Var[ f ] ≤ MaxInf[ f ] ≤ Var[ f ]

holds trivially, by the Poincaré Inequality and Exercise 2.8.

Before proving the KKL Theorem, let’s see an additional consequence for
Ben-Or and Linial’s problem.

Proposition 9.27. Let f : {−1, 1}n → {−1, 1} be monotone and assume E[ f ] ≥
−.99. Then there exists a subset J ⊆ [n] with |J| ≤ O(n/ log n) that if “bribed to
vote 1” causes the outcome to be 1 almost surely; i.e.,

E[ f J|(1,...,1)] ≥ .99. (9.14)

Similarly, if E[ f ] ≤ .99 there exists J ⊆ [n] with |J| ≤ O(n/ log n) such that
E[ f J|(−1,...,−1)] ≤ −.99.

Proof. By symmetry it sufﬁces to prove the result regarding bribery by can-
didate +1. The candidate executes the following strategy: First, bribe the
voter i1 with the largest inﬂuence on f0 = f ; then bribe the voter i2 with

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

266 9. Basics of hypercontractivity

the largest inﬂuence on f1 = f (i17→1); then bribe the voter i3 with the largest
inﬂuence on f2 = f (i1,i27→1); etc. For each t ∈ N we have

E[ f t+1] ≥ E[ f t] + MaxInf[ f t].

If after t bribes the candidate has not yet achieved (9.14) we have −.99 ≤
E[ f t] < .99; thus Var[ f t] ≥ Ω(1) and the KKL Theorem implies MaxInf[ f t] ≥
Ω( log n
n ). Thus the candidate will achieve a bias of at least .99 after bribing at

most (.99 − (−.99))/Ω( log n
n ) = O(n/ log n) voters. □

Thus in any monotone election scheme, there is always a candidate b ∈
{−1, 1} and a o(1)-fraction of the voters that b can bribe such that the election
becomes 99%-biased in b’s favor. And if the election scheme was not terribly
biased to begin with, then both candidates have this ability. For a more
precise version of this result, see Exercise 9.27; for a nonmonotone version,
see Exercise 9.28. Note also that although the Tribesn function is essentially
optimal for standing up to a single bribed voter, it is quite bad at standing
up to bribed coalitions: by bribing just a single tribe (DNF term) – about
log n voters – the outcome can be completely forced to True. Nevertheless,
Proposition 9.27 is close to sharp: Ajtai and Linial [AL93] constructed an
unbiased monotone function f : {−1, 1}n → {−1, 1} such that bribing any set of
at most ϵn/ log2 n voters changes the expectation by at most O(ϵ).

The remainder of this section is devoted to the proof of the KKL The-
orem and some variants. As mentioned earlier, the proof quickly follows
from summing Corollary 9.12 over all coordinates; but let’s give a more
leisurely description. We’ll focus on the main case of interest: showing that
MaxInf[ f ] ≥ Ω( log n
n ) when f is unbiased (i.e., Var[ f ] = 1). If f ’s total inﬂu-

ence is at least, say, .1 log n, then even the average inﬂuence is Ω( log n
n ). So we
may as well assume I[ f ] ≤ .1 log n.

This leads us to the problem of characterizing (unbiased) functions with
small total inﬂuence. (This is the same issue that arose at the end of Chap-
ter 8.4 when studying sharp thresholds.) It’s helpful to think about the case
that the total inﬂuence is very small – say I[ f ] ≤ K where K = 10 or K = 100,
though we eventually want to handle K = .1 log n. Let’s think of f as the indi-
cator of a volume-1/2 set A ⊂ {−1, 1}n, so I[ f ]
n is the fraction of Hamming cube
edges on the boundary of A. The edge-isoperimetric inequality (or Poincaré
Inequality) tells us that I[ f ] ≥ 1: at least a 1
n fraction of the cube’s edges must
be on A’s boundary, with dictators and negated-dictators being the minimiz-
ers. Now what can we say if I[ f ] ≤ K; i.e., A’s boundary has only K times
more edges than the minimum? Must f be “somewhat similar” to a dictator
or negated-dictator? Kahn, Kalai, and Linial showed that the answer is yes:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.6. Highlight: The Kahn–Kalai–Linial Theorem 267

f must have a coordinate with inﬂuence at least 2−O(K). This should be con-
sidered very large (and dictator-like), since a priori all of the inﬂuences could
have been equal to K
n .

KKL Edge-Isoperimetric Theorem. Let f : {−1, 1}n → {−1, 1} be noncon-
stant and let ̃I[ f ] = I[ f ]/ Var[ f ] ≥ 1 (which is just I[ f ] if f is unbiased). Then

MaxInf[ f ] ≥ ( 9
̃I[ f ]2 ) · 9−̃I[ f ].

This theorem is sharp for ̃I[ f ] = 1 (cf. Exercises 1.19, 5.35), and it’s non-
trivial (in the unbiased case) for I[ f ] as large as Θ(log n). This last fact lets us
complete the proof of the KKL Theorem as originally stated:

Proof of the KKL Theorem from the Edge-Isoperimetric version.
We may assume f is nonconstant. If ̃I[ f ] = I[ f ]/ Var[ f ] ≥ .1 log n, then we
are done: the total inﬂuence is at least .1 Var[ f ]·log n and hence MaxInf[ f ] ≥
.1 Var[ f ] · log n
n . Otherwise, the KKL Edge-Isoperimetric Theorem implies

MaxInf[ f ] ≥ Ω ( 1
log
2 n
 ) · 9
−.1 log n = ̃Ω(n−.1 log 9) = Ω(n−.317) ≫ Var[ f ] · Ω ( log n
n
 ) .
□

(You are asked to be careful about the constant factors in Exercise 9.30.)

We now turn to proving the KKL Edge-Isoperimetric Theorem. The high-
level idea is to look at the contrapositive: supposing all of f ’s inﬂuences are
small, we want to show its total inﬂuence must be large. The assumption here
is that each derivative Di f is a {−1, 0, 1}-valued function which is nonzero only
on a “small” set. Hence “small-set expansion” implies that each derivative has
“unusually large” noise sensitivity. (We are really just repeating Corollary 9.12
in words here.) In turn this means that for each i ∈ [n], the Fourier weight
of f on coefﬁcients containing i must be quite “high up”. Since this holds for
all i we deduce that all of f ’s Fourier weight must be quite “high up” – hence
f must have “large” total inﬂuence. We now make this story formal:

Proof of the KKL Edge-Isoperimetric Theorem. We treat only the case
that f is unbiased, leaving the general case to Exercise 9.29 (see also the ver-
sion for product space domains in Chapter 10.3). The theorem is an immediate
consequence of the following chain of inequalities:

3 · 3−I[ f ] (a)
≤ 3Stab1/3[ f ] (b)
≤ I(1/3)[ f ] (c)
≤ n∑

i=1 Infi[ f ]
3/2 (d)
≤ MaxInf[ f ]
1/2 · I[ f ].

The key inequality is (c), which comes from summing Corollary 9.12 over all
coordinates i ∈ [n]. Inequality (d) is immediate from Infi[ f ]
3/2 ≤ MaxInf[ f ]
1/2·

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

268 9. Basics of hypercontractivity

Infi[ f ]. Inequality (b) is trivial from the Fourier formulas (recall Fact 2.53):

I(1/3)[ f ] = ∑

|S|≥1 |S|(1/3)|S|−1 ̂f (S)2 ≥ 3 ∑

|S|≥1
(1/3)|S| ̂f (S)
2 = 3Stab1/3[ f ]

(the last equality using ̂f (;) = 0). Finally, inequality (a) is quickly proved
using the spectral sample: for S ∼ S f we have

3Stab1/3[ f ] = 3 ∑

S⊆[n](1/3)|S| ̂f (S)
2 = 3 E[3
−|S|] ≥ 3 · 3
− E[|S|] = 3 · 3
−I[ f ], (9.15)

the inequality following from convexity of s 7→ 3−s. □

We end this chapter by deriving an even stronger version of the KKL Edge-
Isoperimetric Theorem, and deducing Friedgut’s Junta Theorem (from the end
of Chapter 3.1) as a consequence. The KKL Edge-Isoperimetric Theorem tells
us that if f is unbiased and I[ f ] ≤ K then f must look somewhat like a 1-junta,
in the sense of having a coordinate with inﬂuence at least 2−O(K). Friedgut’s
Junta Theorem shows that in fact f must essentially be a 2O(K)-junta. To
obtain this conclusion, you really just have to sum Corollary 9.12 only over
the coordinates which have small inﬂuence on f . It’s also possible to get
even stronger conclusions if f is known to have particularly good low-degree
Fourier concentration. In aid of this, we’ll start by proving the following
somewhat technical-looking result:

Theorem 9.28. Let f : {−1, 1}n → {−1, 1}. Given 0 < ϵ ≤ 1 and k ≥ 0, deﬁne

τ = ϵ2

I[ f ]2 9−k, J = { j ∈ [n] : Inf j[ f ] ≥ τ}, so |J| ≤ (I[ f ]
3/ϵ2)9k.

Then f ’s Fourier spectrum is ϵ-concentrated on

F = {S : S ⊆ J} ∪ {S : |S| > k}.

In particular, suppose f ’s Fourier spectrum is also ϵ-concentrated on degree up
to k. Then f ’s Fourier spectrum is 2ϵ-concentrated on

F ′ = {S : S ⊆ J, |S| ≤ k},

and f is ϵ-close to a |J|-junta h : {−1, 1}J → {−1, 1}.

Proof. Summing Corollary 9.12 just over i ̸∈ J we obtain
∑

i̸∈J Inf
(1/3)
i [ f ] ≤ ∑

i̸∈J Infi[ f ]
3/2 ≤ max
i̸∈J {Infi[ f ]
1/2} · ∑

i̸∈J Infi[ f ] ≤ τ1/2 · I[ f ] ≤ 3
−kϵ,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.6. Highlight: The Kahn–Kalai–Linial Theorem 269

where the last two inequalities used the deﬁnitions of J and τ, respectively.
On the other hand,
∑

i̸∈J Inf(1/3)
i [ f ] = ∑

i̸∈J
 ∑

S∋i(1/3)|S|−1 ̂f (S)2 = ∑

S |S ∩ J| · 31−|S| ̂f (S)
2

≥ ∑

S̸∈F |S ∩ J| · 31−|S| ̂f (S)2 ≥ 3−k ∑

S̸∈F ̂f (S)2.

Here the last inequality used that S ̸∈ F implies |S ∩ J| ≥ 1 and 31−|S| ≥ 3−k.
Combining these two deductions yields ∑S̸∈F ̂f (S)
2 ≤ ϵ, as claimed.

As for the second part of the theorem, when f ’s Fourier spectrum is 2ϵ-
concentrated on F ′ it follows from Proposition 3.31 that f is 2ϵ-close to the
Boolean-valued |J|-junta sgn( f ⊆J). From Exercise 3.34 we may deduce that f
is in fact ϵ-close to some h : {−1, 1}J → {−1, 1}. □

Remark 9.29. As you are asked to show in Exercise 9.31, by using Corol-
lary 9.25 in place of Corollary 9.12, we can achieve junta size (I[ f ]2+η/ϵ1+η) ·
C(η)k in Theorem 9.28 for any η > 0, where C(η) = (2/η + 1)
2.

In Theorem 9.28 we may always take k = I[ f ]/ϵ, by the “Markov argument”
Proposition 3.2. Thus we obtain as a corollary:

Friedgut’s Junta Theorem. Let f : {−1, 1}n → {−1, 1} and let 0 < ϵ ≤ 1. Then
f is ϵ-close to an exp(O(I[ f ]/ϵ))-junta. Indeed, there is a set J ⊆ [n] with
|J| ≤ exp(O(I[ f ]/ϵ)) such that f ’s Fourier spectrum is 2ϵ-concentrated on {S ⊆
J : |S| ≤ I[ f ]/ϵ}.

As mentioned, we can obtain stronger results for functions f that are ϵ-
concentrated up to degree much less than I[ f ]/ϵ. Width-w DNFs, for example,
are ϵ-concentrated on degree up to O(w log(1/ϵ)) (by Theorem 4.22). Thus:

Corollary 9.30. Any width-w DNF is ϵ-close to a (1/ϵ)O(w)-junta.

Uniformly noise-stable functions do even better. From Peres’s Theorem we
know that linear threshold functions are ϵ-concentrated up to degree O(1/ϵ2).
Thus Theorem 9.28 and Remark 9.29 imply:

Corollary 9.31. Let f : {−1, 1}n → {−1, 1} be a linear threshold function and
let 0 < ϵ, η ≤ 1/2. Then f is ϵ-close to a junta on I[ f ]2+η · (1/η)
O(1/ϵ2) coordinates.

Assuming ϵ is a small universal constant we can take η = 1/ log(O(I[ f ])) and
deduce that every LTF is ϵ-close to a junta on I[ f ]2 · polylog(I[ f ]) coordinates.
This is essentially best possible since I[Majn] = Θ(pn), but Majn is not even
.1-close to any o(n)-junta. By virtue of Theorem 5.37 on the uniform noise
stability of PTFs, we can also get this conclusion for any constant-degree PTF.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

270 9. Basics of hypercontractivity

One more interesting fact we may derive is that every Boolean function
has a Fourier coefﬁcient that is at least inverse-exponential in the square of
its total inﬂuence:

Corollary 9.32. Assume f : {−1, 1}n → {−1, 1} satisﬁes Var[ f ] ≥ 1/2. Then
there exists S ⊆ [n] with 0 < |S| ≤ O(I[ f ]) such that ̂f (S)2 ≥ exp(−O(I[ f ]
2)).

Proof. Taking ϵ = 1/8 in Friedgut’s Junta Theorem we get a set of coordinates
J with |J| ≤ exp(O(I[ f ])) such that f has Fourier weight at least 1 − 2ϵ =
3/4 on F = {S ⊆ J : |S| ≤ 8I[ f ]}. Since ̂f (;)2 = 1 − Var[ f ] ≤ 1/2 we conclude
that f has Fourier weight at least 1/4 on F ′ = F \ {;}. But |F ′| ≤ |J|8I[ f ] =
exp(O(I[ f ]
2)), so the result follows by the Pigeonhole Principle. (Here we used
that (1/4) exp(−O(I[ f ]
2)) = exp(−O(I[ f ]
2)) because I[ f ] ≥ Var[ f ] ≥ 1
2 .) □

Remark 9.33. Of course, if Var[ f ] < 1/2, then f has a large empty Fourier
coefﬁcient: ̂f (;)2 ≥ 1/2. For a more reﬁned version of Corollary 9.32, see
Exercise 9.32.

It is an open question whether Corollary 9.32 can be improved to give a
Fourier coefﬁcient satisfying ̂f (S)
2 ≥ exp(−O(I[ f ])) (but see Exercise 9.33).

9.7. Exercises and notes

9.1 For every 1 < b < B show that there is a b-reasonable random variable X
such that 1 + X is not B-reasonable.

9.2 For k = 1, improve the 9 in the Bonami Lemma to 3. More precisely,
suppose f : {−1, 1}n → R has degree at most 1 and that x1, . . . , xn are
independent 3-reasonable random variables satisfying E[xi] = E[x3
i ] = 0.
(For example, the xi’s may be uniform ±1 bits.) Show that f (x) is also
3-reasonable. (Hint: By direct computation, or by running through the
Bonami Lemma proof with k = 1 more carefully.)

9.3 Let k be a positive multiple of 3 and let n ≥ 2k be an integer. Deﬁne
f : {−1, 1}n → R by f (x) = ∑

S⊆[n]
|S|=k
 xS.

(a) Show that
 E[ f 4] ≥
 ( n
k/3, k/3, k/3, k/3, k/3, k/3, n−2k)

(n
k)2 E[ f 2]
2,

where the numerator of the fraction is a multinomial coefﬁcient –
speciﬁcally, the number of ways of choosing six disjoint size-k/3 sub-
sets of [n]. (Hint: Given such size-k/3 subsets, consider quadruples of
size-k subsets that hit each size-k/3 subset twice.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.7. Exercises and notes 271

(b) Using Stirling’s Formula, show that

lim
n→∞
 ( n
k/3, k/3, k/3, k/3, k/3, k/3, n−2k)

(n
k)2 = Θ(k−29k).

Deduce the following lower bound for the Bonami Lemma: ∥ f ∥4 ≥
Ω(k−1/2) · p
3k∥ f ∥2. (In fact, ∥ f ∥4 = Θ(k−1/4) · p
3k∥ f ∥2 and such an
upper bound holds for all f homogeneous of degree k; see Exercise
and 9.38(f ).)

9.4 Prove Corollary 9.6.

9.5 Let 0 ≤ δ ≤ 1
1600 and let f , ℓ be real numbers satisfying |ℓ2 − 1| > 39p
δ
and | f | = 1. Show that | f − ℓ|2 ≥ 169δ. (This is a loose estimate; stronger
ones are possible.)

9.6 Theorem 9.21 shows that the (2, 4)-Hypercontractivity Theorem implies
the Bonami Lemma. In this exercise you will show the reverse implication.

(a) Let f : {−1, 1}n → R . For a ﬁxed δ ∈ (0, 1), use the Bonami Lemma to
show that

∥T(1−δ)/p
3 f ∥4 ≤ ∞∑

k=0
(1 − δ)k∥ f =k∥2 ≤ 1
δ ∥ f ∥2.

(b) For g : {−1, 1}n → R and d ∈ N +, let g⊕d : {−1, 1}dn → R be the function
deﬁned by g⊕d(x(1), . . . , x(d)) = g(x(1))g(x(2)) · · · g(x(d)) (where each x(i) ∈
{−1, 1}n). Show that ∥Tρ(g⊕d)∥p = ∥Tρ g∥d
p holds for every p ∈ R + and
ρ ∈ [−1, 1]. Note the special case ρ = 1.
(c) Deduce from parts (a) and (b) that in fact ∥T(1−δ)/
p
3 f ∥4 ≤ ∥ f ∥2. (Hint:
Apply part (a) to f ⊕d for larger and larger d.)
(d) Deduce that in fact ∥T1/p
3 f ∥4 ≤ ∥ f ∥2; i.e., the (2, 4)-Hypercontractivity
Theorem follows from the Bonami Lemma. (Hint: Take the limit as
δ → 0
+.)

9.7 Suppose we wish to show that ∥Tρ f ∥q ≤ ∥ f ∥p for all f : {−1, 1}n → R . Show
that it sufﬁces to show this for all nonnegative f . (Hint: Exercise 2.34.)

9.8 Fix k ∈ N . The goal of this exercise is to show that “projection to degree k
is a bounded operator in all L p norms, p > 1”. Let f : {−1, 1}n → R .

(a) Let q ≥ 2. Show that ∥ f ≤k∥q ≤ √q − 1k∥ f ∥q. (Hint: Use Theorem 9.21

to show the stronger statement ∥ f ≤k∥q ≤ √q − 1k∥ f ∥2.)
(b) Let 1 < q ≤ 2. Show that ∥ f ≤k∥q ≤ (1/√q − 1)k∥ f ∥q. (Hint: Either
give a similar direct proof using the (p, 2)-Hypercontractivity Theo-
rem, or explain how this follows from part (a) using the dual norm
Proposition 9.19.)

9.9 Let X be (p, q, ρ)-hypercontractive.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

272 9. Basics of hypercontractivity

(a) Show that cX is (p, q, ρ)-hypercontractive for any c ∈ R .
(b) Show that ρ ≤ ∥X ∥p
∥X ∥q .

9.10 Let X be (p, q, ρ)-hypercontractive. (For simplicity you may want to as-
sume X is a discrete random variable.)
(a) Show that E[X ] must be 0. (Hint: Taylor expand ∥1 + ρϵX ∥r to one
term around ϵ = 0; note that ρ < 1 by deﬁnition.)

(b) Show that ρ ≤ √ p−1
q−1 . (Hint: Taylor expand ∥1 + ρϵX ∥r to two terms
around ϵ = 0.)

9.11 (a) Suppose E[X ] = 0. Show that X is (q, q, 0)-hypercontractive for all
q ≥ 1. (Hint: Use monotonicity of norms to reduce to the case q = 1.)
(b) Show further that X is (q, q, ρ)-hypercontractive for all 0 ≤ ρ < 1.
(Hint: Write (a + ρ X ) = (1 − ρ)a + ρ(a + X ) and employ the triangle
inequality for ∥ · ∥q.)
(c) Show that if X is (p, q, ρ)-hypercontractive, then it is also (p, q, ρ′)-
hypercontractive for all 0 ≤ ρ′ < ρ. (Hint: Use the previous exercise
along with Exercise 9.10(a).)

9.12 Let X be a (nonconstant) (2, 4, ρ)-hypercontractive random variable. The
goal of this exercise is to show the following anticoncentration result: For
all θ ∈ R and 0 < t < 1,

Pr[|X − θ| > t∥X ∥2] ≥ (1 − t2)2ρ4.

(a) Reduce to the case ∥X ∥2 = 1.
(b) Letting Y = (X − θ)
2, show that E[Y ] = 1 + θ2 and E[Y 2] ≤ (ρ−2 + θ2)
2.
(c) Using the Paley–Zygmund inequality, show that

Pr[|X − θ| > t] ≥ ( ρ2(1 − t2) + ρ2θ2

1 + ρ2θ2
 )2 .

(d) Show that the right-hand side above is minimized for θ = 0, thereby
completing the proof.

9.13 Let m ∈ N + and let f : {−1, 1}n → [m] be “unbiased”, meaning Pr[ f (x) =
i] = 1
m for all i ∈ [m]. Let 0 ≤ ρ ≤ 1 and let (x, y) be a ρ-correlated pair.
Show that Pr[ f (x) = f (y)] ≤ (1/m)(1−ρ)/(1+ρ). (More generally, you might
show that this is an upper bound on Stabρ[ f ] for all f : {−1, 1}n → △m
with E[ f ] = ( 1
m , . . . , 1
m ); see Exercise 8.33.)

9.14 (a) Let f : {−1, 1}n → R have deg( f ) ≤ k. Prove that ∥ f ∥2 ≤ (1/
√p − 1)k∥ f ∥p
for any 1 ≤ p ≤ 2 using the Hölder inequality strategy from our proof of
the (4/3, 2)-Hypercontractivity Theorem, together with Theorem 9.21.
(b) Verify that exp( 2
p − 1) < 1/√p − 1 for all 1 ≤ p < 2; i.e., the trickier
Theorem 9.22 strictly improves on the bound from part (a).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.7. Exercises and notes 273

9.15 Prove Theorem 9.22 in full generality. (Hint: Let θ be the solution of
1
2 = θ
p + 1−θ
2+ϵ . You will need to show that 1−θ
2θ = ( 2
p − 1) 1
ϵ + ( 1
p − 1
2 ).)

9.16 As mentioned, it’s possible to deduce the (2, q)-Hypercontractivity The-
orem from the n = 1 case using induction by derivatives. From this
one can also obtain the (p, 2)-Hypercontractivity Theorem via Proposi-
tion 9.19. Employing the notation x = (x′, xn), T = T1/pq−1, d = Dn f (x′),

and e = En f (x′), ﬁll in details and justiﬁcations for the following proof
sketch:

∥T1/pq−1 f ∥
2
q = E
x′
[E
xn
[
|Te + (1/√q − 1)xnTd|q]]2/q ≤ E
x′[
((Te)
2 + (Td)
2)q/2]2/q

= ∥(Te)
2+(Td)2∥q/2 ≤ ∥(Te)
2∥q/2+∥(Td)2∥q/2 = ∥Te∥
2
q+∥Td∥
2
q ≤ ∥e∥
2
2+∥d∥2
2 = ∥ f ∥
2
2.

9.17 Deduce the p < 2 < q cases of the Hypercontractivity Theorem from the
(2, q)- and (p, 2)-Hypercontractivity Theorems. (Hint: Use the semigroup
property of Tρ, Exercise 2.32.)

9.18 Let f : {−1, 1}n → {0, 1} have E[ f ] = α.
(a) Show that W1[ f ] ≤ 1
ρ (α
2/(1+ρ) − α
2) for any 0 < ρ ≤ 1.

(b) Deduce the sharp Level-1 Inequality W
1[ f ] ≤ 2α
2 ln(1/α). (Hint: Take
the limit ρ → 0+.)

9.19 For f : {−1, 1}n → {0, 1} with E[ f ] = α, show that W≤k[ f ] = o(α) (as α → 0)
provided k ≤ .373 ln(1/α).

9.20 Show that the KKL Theorem fails for functions f : {−1, 1}n → [−1, 1], even
under the assumption Var[ f ] ≥ Ω(1). (Hint: f (x) = trunc[−1,1]( x1+···+xnpn ).)

9.21 (a) Show C = { f : {−1, 1}n → {−1, 1} | I[ f ] ≤ O(√
log n)} is learnable from
queries to any constant error ϵ > 0 in time poly(n). (Hint: Theo-
rem 9.28.)
(b) Show C = {monotone f : {−1, 1}n → {−1, 1} | I[ f ] ≤ O(√log n)} is learn-
able from random examples to any constant error ϵ > 0 in time poly(n).
(c) Show that C = {monotone f : {−1, 1}n → {−1, 1} | DTsize( f ) ≤ poly(n)}
is learnable from random examples to any constant error ϵ > 0 in
time poly(n). (Hint: the OS Inequality and Exercise 8.43.)

9.22 Deduce the following generalization of the (2, q)-Hypercontractivity The-
orem: Let f : {−1, 1}n → R , q ≥ 2, and assume 0 ≤ ρ ≤ 1 satisﬁes ρλ ≤
1/
√q − 1 for some 0 ≤ λ ≤ 1. Then

∥Tρ f ∥q ≤ ∥Tρ f ∥
1−λ
2 ∥ f ∥
λ
2 .

(Hint: Show ∥Tρ f ∥2
q ≤ ∑S(ρ2|S| ̂f (S)
2)
1−λ · ( ̂f (S)
2)
λ and use Hölder.)

9.23 Let f : {−1, 1}n → [−1, 1], let 0 ≤ ϵ ≤ 1, and assume q ≥ 2 + 2ϵ. Show that

∥T1−ϵ f ∥q
q ≤ ∥T 1p
1+2ϵ f ∥q
q ≤ (∥ f ∥
2
2)
1+ϵ.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

274 9. Basics of hypercontractivity

9.24 Recall the Gaussian quadrant probability Λρ(µ) deﬁned in Exercise 5.32
by Λρ(µ) = Pr[z1 > t, z2 > t], where z1, z2 are standard Gaussians with
correlation E[z1 z2] = ρ and t is deﬁned by Φ(t) = µ. The goal of this
exercise is to show that for ﬁxed 0 < ρ < 1 we have the estimate

Λρ(µ) = ̃Θ(µ
 2
1+ρ ) (9.16)

as µ → 0. In light of Exercise 5.32, this will show that the Small-Set
Expansion Theorem for the ρ-stable hypercube graph is essentially sharp
due to the example of Hamming balls of volume µ.
(a) First let’s do an imprecise “heuristic” calculation. We have Pr[z1 >
t] = Pr[z1 ≥ t] = µ by deﬁnition. Conditioned on a Gaussian being
at least t it is unlikely to be much more than t, so let’s just pretend
that z1 = t. Then the conditional distribution of z2 is ρt + √
1 − ρ2 y,
where y ∼ N(0, 1) is an independent Gaussian. Using the fact that

Φ(u) ∼ φ(u)/u as u → ∞, deduce that Pr[z2 > t | z1 = t] = ̃Θ(µ
 1−ρ
1+ρ ) and
“hence” (9.16) holds.
(b) Let’s now be rigorous. Recall that we are treating 0 < ρ < 1 as ﬁxed
and letting µ → 0 (hence t → ∞). Let φρ(z1, z2) denote the joint pdf of
z1, z2 so that
 Λρ(µ) = ∫ ∞

t
 ∫ ∞

t φρ(z1, z2) dz1 dz2.

Derive the following similar-looking integral:

∫ ∞

t
 ∫ ∞

t (z2 −ρz1)(z1 −ρt)φρ(z1, z2) dz1 dz2 = (1 − ρ2)
3/2

2π exp (− 2
1 + ρ t2

2
 ) (9.17)

and show that the right-hand side is ̃Θ(µ
 2
1+ρ ).
(c) Show that
 Pr [z1 > t−1
ρ
 ] = ∫ ∞

t−1
ρ φ(z1) dz1 = ̃Θ(µ
 1
ρ2 ),

and that this is asymptotically smaller than ̃Θ(µ
 2
1+ρ ).
(d) Deduce (9.16). (Hint: Try to arrange that the extraneous factors
(z2 − ρz1), (z1 − ρt) in (9.17) are both at least 1.)

9.25 Let f : {−1, 1}n → {−1, 1}, let J ⊆ [n], and write J = [n] \ J. Deﬁne the
coalitional inﬂuence of J on f to be

˜InfJ[ f ] = Pr
z∼{−1,1}J[ f J|z is not constant].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.7. Exercises and notes 275

Furthermore, for b ∈ {−1, +1} deﬁne the coalitional inﬂuence toward b of J
on f to be
˜Inf b
J[ f ] = Pr
z∼{−1,1}J[ f J|z can be made b] − Pr[ f = b]

= Pr
z∼{−1,1}J[ f J|z ̸≡ −b] − Pr[ f = b].

For brevity, we’ll sometimes write ˜Inf ±
J [ f ] rather than ˜Inf ±1
J [ f ].
(a) Show that for coalitions of size 1 we have Infi[ f ] = ˜Inf{i}[ f ] = 2˜Inf ±
{i}[ f ].

(b) Show that 0 ≤ ˜Inf ±
J [ f ] ≤ 1.
(c) Show that ˜InfJ[ f ] = ˜Inf +
J [ f ] + ˜Inf −
J [ f ].
(d) Show that if f is monotone, then

˜Inf b
J[ f ] = Pr[ f J|(b,...,b) = b] − Pr[ f = b].

(e) Show that ˜InfJ[χ[n]] = 1 for all J ̸= ;.
(f ) Supposing we write t = |J|/
pn, show that ˜Inf ±
J [Majn] = Φ(t) − 1
2 ± o(1)
and hence ˜InfJ[Majn] = 2Φ(t) − 1 ± o(1). Thus ˜InfJ[Majn] = o(1) if
|J| = o(pn) and ˜InfJ[Majn] = 1 − o(1) if |J| = ω(pn). (Hint: Central
Limit Theorem.)
(g) Show that max{˜InfTrue
J [Tribesn] : |J| ≤ log n} = 1/2 + Θ( log n
n ). On the

other hand, show that max{˜InfFalse
J [Tribesn] : |J| ≤ k} ≤ k · O( log n
n ). De-
duce that for some positive constant c we have max{˜InfJ[Tribesn] :
|J| ≤ cn/ log n} ≤ .51. (Hint: Refer to Proposition 4.12.)

9.26 Show that the exponential dependence on I[ f ] in Friedgut’s Junta Theo-
rem is necessary. (Hint: Exercise 4.15.)

9.27 Let f : {−1, 1}n → {−1, 1} be a monotone function with Var[ f ] ≥ δ > 0, and
let 0 < ϵ < 1/2 be given.
(a) Improve Proposition 9.27 as follows: Show that there exists J ⊆ [n]
with |J| ≤ O(log 1
ϵδ ) · n
log n such that E[ f J|(1,...,1)] ≥ 1 − ϵ. (Hint: How
many bribes are required to move f ’s mean outside the interval [1 −
2η, 1 − η]?)
(b) Show that there exists J ⊆ [n] with |J| ≤ O(log 1
ϵδ ) · n
log n such that
˜InfJ[ f ] ≥ 1 − ϵ. (Hint: Use Exercise 9.25(d) and take the union of two
inﬂuential sets.)

9.28 Let f : {−1, 1}n → {−1, 1}.
(a) Let f ∗ : {−1, 1}n → {−1, 1} be the “monotonization” of f as deﬁned in

Exercise 2.52. Show that ˜Inf b
J[ f ∗] ≤ ˜Inf b
J[ f ] for all J ⊆ [n] and b ∈
{−1, 1}, and hence also ˜InfJ[ f ∗] ≤ ˜InfJ[ f ].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

276 9. Basics of hypercontractivity

(b) Let Var[ f ] ≥ δ > 0 and let 0 < ϵ < 1/2 be given. Show that there
exists J ⊆ [n] with |J| ≤ O(log 1
ϵδ ) · n
log n such that ˜InfJ[ f ] ≥ 1 − ϵ. (Hint:
Combine part (a) with Exercise 9.27(b).)

9.29 Establish the general-variance case of the KKL Edge-Isoperimetric Theo-
rem. (Hint: You’ll need to replace (9.15) with

3 ∑

|S|≥1
(1/3)|S| ̂f (S)
2 ≥ 3 Var[ f ] · 3−I[ f ]/ Var[ f ].

Use the same convexity argument, but applied to the random variable S
that takes on each outcome ; ̸= S ⊆ [n] with probability ̂f (S)
2/ Var[ f ].)

9.30 The goal of this exercise is to attain the best known constant factor in the
statement of the KKL Theorem.
(a) By using Corollary 9.25 in place of Corollary 9.12, obtain the follow-
ing generalization of the KKL Edge-Isoperimetric Theorem: For any
(nonconstant) f : {−1, 1}n → {−1, 1} and 0 < δ < 1,

MaxInf[ f ] ≥ ( 1+δ
1−δ
 ) 1
δ ( 1
̃I[ f ]
 ) 1
δ · ( 1−δ
1+δ
 ) 1
δ ̃I[ f ] ,

where ̃I[ f ] denotes I[ f ]/ Var[ f ]. (Hint: Write ρ = 1−δ
1+δ .) Deduce that
for any constant C > e2 we have

MaxInf[ f ] ≥ ̃Ω(C−̃I[ f ]).

(b) More carefully, show that by taking δ = 1
2̃I[ f ]1/3 we can achieve

MaxInf[ f ] ≥ exp(−2̃I[ f ]) · e2 · ( 1
̃I[ f ]
 )2̃I[ f ]
1/3 · exp(− 1
4̃I[ f ]1/3).

(Hint: Establish ( 1−δ
1+δ
 ) 1
δ ≥ exp(−2 − δ2) for 0 < δ ≤ 1/2.)

(c) By distinguishing whether or not ̃I[ f ] ≥ 1
2 (ln n − √
log n), establish the
following form of the KKL Theorem: For any f : {−1, 1}n → {−1, 1},

MaxInf[ f ] ≥ 1
2 Var[ f ] · ln n
n (1 − on(1)).

9.31 Establish the claim in Remark 9.29.

9.32 Show that if f : {−1, 1}n → {−1, 1} is nonconstant, then there exists S ⊆ [n]
with 0 < |S| ≤ O(I[ f ]/ Var[ f ]) such that ̂f (S)2 ≥ exp(−O(I[ f ]2/ Var[ f ]2)).
(Hint: By mimicking Corollary 9.32’s proof you should be able to establish
the lower bound Ω(Var[ f ]) · exp(−O(I[ f ]2/ Var[ f ]2)). To show that this
quantity is also exp(−O(I[ f ]
2/ Var[ f ]
2)), use Theorem 2.39.)

9.33 Let f : {−1, 1}n → {−1, 1} be a nonconstant monotone function. Improve
on Corollary 9.32 by showing that there exists S ̸= ; satisfying ̂f (S)2 ≥
exp(−O(I[ f ]/ Var[ f ])). (Hint: You can even get |S| ≤ 1; use the KKL Edge-
Isoperimetric Theorem and Proposition 2.21.)

9.34 Let f : {−1, 1}n → R . Prove that ∥ f ∥4 ≤ sparsity( ̂f )
1/4∥ f ∥2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.7. Exercises and notes 277

9.35 Let q = 2r be a positive even integer, let ρ = 1/√q − 1, and let f1, . . . , f r :
{−1, 1}n → R . Generalize the (2, q)-Hypercontractivity Theorem by show-
ing that
 E
 [ r∏

i=1
(Tρ f i)
2]
 ≤ r∏

i=1 E[ f 2
i ].

(Hint: Hölder’s inequality.)

9.36 In this exercise you will give a simpler, stronger version of Theorem 9.17
under the assumption that q = 2r is a positive even integer.
(a) Using the idea of Proposition 9.16, show that if x is a uniformly
random ±1 bit then x is (2, q, ρ)-hypercontractive if and only if ρ ≤
1/
√q − 1.
(b) Show the same statement for any random variable x satisfying E[x2] =
1 and

E[x2 j−1
i ] = 0, E[x2 j
i ] ≤ (2r − 1) j (r
j)

(2r
2 j) for all integers 1 ≤ j ≤ r.

(c) Show that none of the even moment conditions in part (b) can be
relaxed.

9.37 Let q = 2r be a positive even integer and let f : {−1, 1}n → R be homoge-
neous of degree k ≥ 1 (i.e., f = f =k). The goal of this problem is to improve
slightly on the generalized Bonami Lemma, Theorem 9.21.
(a) Show that

E[ f q] = ∑ ̂f (S1) · · · ̂f (Sq) ≤ ∑ | ̂f (S1)| · · · | ̂f (Sq)|, (9.18)

where the sum is over all tuples S1, . . . , Sk satisfying S1△ · · · △Sq = ;.
(b) Let G denote the complete q-partite graph over vertex sets V1, . . . , Vq,
each of cardinality k. Let M denote the set of all perfect matchings
in G. Show that the right-hand side of (9.18) is equal to

1
(k!)q ∑

M∈M
 ∑

ℓ:M→[n] | ̂f (T1(M, ℓ))| · · · | ̂f (Tq(M, ℓ))|, (9.19)

where T j(M, ℓ) denotes ⋃{ℓ(e) : e ∈ M, e ∩ Vj ̸= ;}.
(c) Show that (9.19) is equal to

1
(rk)! · (k!)q ∑

M∈M
 n∑

i1=1
 n∑

i2=1 · · · n∑

i rk=1 | ̂f (U1(M, i1, . . . , i rk))| · · · | ̂f (Uq(M, i1, . . . , i rk))|,

(9.20)
where M is the set of ordered perfect matchings of G, and now
U j(M, i1, . . . , i rk) denotes ⋃{i t : M(t) ∩ Vj ̸= ;}.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

278 9. Basics of hypercontractivity

(d) Show that for any M ∈ M we have

n∑

i1=1
 n∑

i2=1 · · · n∑

i rk=1 | ̂f (U1(M, i1, . . . , i rk))| · · · | ̂f (Uq(M, i1, . . . , i rk))|

≤
 ( n∑

j1,..., jk=1 ̂f ({ j1, . . . , jk})2)r

(Hint: Use Cauchy–Schwarz rk times.)
(e) Deduce that ∥ f ∥q
q ≤ 1
(rk)!·(k!)q · |M | · (k!)r∥ f ∥
2r
2 and hence

∥ f ∥q ≤ |M |1/q
pk! ∥ f ∥2.

9.38 The goal of this problem is to estimate |M | from Exercise 9.37 so as to
give a concrete improvement on Theorem 9.21.
(a) Show that for q = 4, k = 2 we have |M | = 60.
(b) Show that |M | ≤ (qk − 1)!!. (Hint: Show that (qk − 1)!! is the number
of perfect matchings in the complete graph on qk vertices.) Deduce
∥ f ∥q ≤ pqk∥ f ∥2.
(c) Show that |M | ≤ ( 2r−1
r )rk(rk)!2, and thereby deduce

∥ f ∥q ≤ Cq,k · √q − 1k∥ f ∥2,

where Cq,k = ( (rk)!
k!r rrk )1/q. (Hint: Suppose that the ﬁrst t edges of the

perfect matching have been chosen; show that there are ( 2r−1
r )(rk− t)
2

choices for the next edge. The worst case is if the vertices used up so
far are spread equally among the q parts.)
(d) Give a simple proof that Cq,k ≤ 1, thereby obtaining Theorem 9.21.
(e) Show that in fact Cq,k = Θ(1) · k−1/4+1/(2q). (Hint: Stirling’s Formula.)
(f ) Can you obtain the improved estimate

|M |1/q
pk! = Θq(1) · k−1/4 · √q − 1k?

(Hint: First exactly count – then estimate – the number of perfect
matchings with exactly e i j edges between parts i and j. Then sum
your estimate over a range of the most likely values for e i j.)

Notes. The history of the Hypercontractivity Theorem is complicated. Its
earliest roots are in the work of Paley [Pal32] from 1932; he showed that for
1 < p < ∞ there are constants 0 < c p < C p < ∞ such that c p∥S f ∥p ≤ ∥ f ∥p ≤

C p∥S f ∥p holds for any f : {−1, 1}n → R . Here S f = ∑n
t=1
 √∑n
t=1(dt f )2 is the

“square function” of f , and dt f = ∑S:max(S)=t ̂f (S) χS is the martingale differ-
ence sequence for f deﬁned in Exercise 8.17. The main task in Paley’s work
is to prove the statement when p is an even integer; other values of p follow

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.7. Exercises and notes 279

by the Riesz(–Thorin) interpolation theorem. Using this result, Paley showed
the following hypercontractivity result: If f : {−1, 1}n → R is homogeneous of
degree 2, then c′
p∥ f ∥2 ≤ ∥ f ∥p ≤ C′
p∥ f ∥2 for any p ∈ R +. Some extensions of
Paley’s work are in [Wat64].

In 1968 Bonami [Bon68] stated the following variant of Theorem 9.21:
If f : {−1, 1}n → R is homogeneous of degree k, then for all q ≥ 2, ∥ f ∥q ≤
ckpq∥ f ∥2, where the constant ck may be taken to be 1 if q is an even integer.
She remarks that this theorem can be deduced from Paley’s result but with a
much worse (exponential) dependence on q. The proof she gives is combinato-
rial and actually only treats the case k = 2 and q an even integer; it is similar
to Exercise 9.37.

Independently in 1969, Kiener [Kie69] published his Ph.D. thesis, which
extended Paley’s hypercontractivity result as follows: If f : {−1, 1}n → R is
homogeneous of degree k, then c p,k∥ f ∥2 ≤ ∥ f ∥p ≤ C p,k∥ f ∥2 for any p ∈ R +.
The proof is an induction on k, and again the bulk of the work is the case of
even integer p. Kiener also gave a long combinatorial proof showing that if
f : {−1, 1}n → R is homogeneous of degree 2, then E[ f 4] ≤ 51 E[ f 2]2. (Exer-
cise 9.38(a) improves this 51 to 15.)

Also independently in 1969, Schreiber [Sch69] considered multilinear
polynomials f over a general orthonormal sequence x1, . . . , xn of centered real
(or complex) random variables. He showed that if f has degree at most k,
then for any even integer q ≥ 4 it holds that ∥ f ∥q ≤ C∥ f ∥2, where C depends
only on k, q, and the q-norms of the xi’s. Again, the proof is very similar to
Exercise 9.37; Schreiber does not estimate his analogue of |M | but merely
notes that it’s ﬁnite. Schreiber was interested mainly in the case that the xi’s
are Gaussian; indeed, his 1969 work [Sch69] is a generalization of his earlier
work [Sch67] speciﬁc to the Gaussian case.

In 1970, Bonami published her Ph.D. thesis [Bon70], which contains the
full Hypercontractivity Theorem as stated at the beginning of the chapter. Her
proof follows the standard template seen in essentially all proofs of hypercon-
tractivity: ﬁrst an elementary proof for the case n = 1 and then an induction
to extend to general n. She also gives the sharper combinatorial result appear-
ing in Exercises 9.37 and 9.38(c). (The stronger bound from Exercise 9.38(f )
is due to Janson [Jan97, Remark 5.20].) As in Corollary 9.6, Bonami notes
that her combinatorial proof can be extended to a general sequence of sym-
metric orthonormal random variables, at the expense of including factors of
∥xi∥q into the bound. She points out that this includes the Gaussian case
independently studied by Schreiber.

Bonami’s work was published in French, and it remained unknown to
most English-language mathematicians for about a decade. In the late 1960s
and early 1970s, researchers in quantum ﬁeld theory developed the theory

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

280 9. Basics of hypercontractivity

of hypercontractivity for the Gaussian analogue of Tρ, namely, the Ornstein–
Uhlenbeck operator Uρ. This is now recognized as essentially being a special
case of hypercontractivity for bits, in light of the fact that x1+···+xnpn tends
to a Gaussian as n → ∞ by the CLT (see Chapter 11.1). We summarize
here some of the work in this setting. In 1966 Nelson [Nel66] showed that
∥U
1/pq−1 f ∥q ≤ Cq∥ f ∥2 for all q ≥ 2. Glimm [Gli68] gave the alternative result

that for each q ≥ 2 there is a sufﬁciently small ρ q > 0 such that ∥Uρ q f ∥q ≤ ∥ f ∥2.
Segal [Seg70] observed that hypercontractive results can be proved by induc-
tion on the dimension n. In 1973 Nelson [Nel73] gave the full Hypercon-
tractivity Theorem in the Gaussian setting: ∥Up
(p−1)/(q−1) f ∥q ≤ ∥ f ∥p for all

1 ≤ p < q ≤ ∞. He also proved the combinatorial Exercise 9.37. The equiva-
lence to the Two-Function Hypercontractivity Theorem is from the work of
Neveu [Nev76].

In 1975 Gross [Gro75] introduced the notion of Log-Sobolev Inequalities
(see Exercise 10.23) and showed how to deduce hypercontractivity inequalities
from them. He established the Log-Sobolev Inequality for 1-bit functions, used
induction (citing Segal) to obtain it for n-bit functions, and then used the CLT
to transfer results to the Gaussian setting. (For some earlier results along
these lines, see the works of Federbush and Gross [Fed69, Gro72].) This gave
a new proof of Nelson’s result and also independently established Bonami’s
full Hypercontractivity Theorem. Also in 1975, Beckner [Bec75] published his
Ph.D. thesis, which proved a sharp form of the hypercontractive inequality for
purely complex ρ. (It is unfortunate that the inﬂuential paper of Kahn, Kalai,
and Linial [KKL88] miscredited the Hypercontractivity Theorem to Beckner.)
The case of general complex ρ was subsequently treated by Weissler [Wei79],
with the sharp result being obtained by Epperson [Epp89]. Weissler [Wei80]
also appears to have been the ﬁrst to make the connection between this line
of work and Bonami’s thesis.

Independently of all this work, the (q, 2)-Hypercontractivity Theorem was
reproved (without sharp constant) in the Banach spaces community by Rosen-
thal [Ros76] in 1975, using methods similar to those of Paley and Kiener. For
additional early references, see Müller [Mül05, Chapter 1].

The term “hypercontractivity” was introduced in a work of Simon and
Høegh-Krohn [SHK72]; Deﬁnition 9.13 of a hypercontractive random vari-
able is due to Krakowiak and Szulga [KS88]. The short inductive proof
of the Bonami Lemma may have appeared ﬁrst in Mossel, O’Donnell, and
Oleszkiewicz [MOO05a]. Theorems 9.22 and 9.24 appear in Janson [Jan97].
Theorem 9.23 dates back to Pisier and Zinn and to Borell [PZ78, Bor79].
As discussed further in the notes to Chapter 10, the Small-Set Expansion
Theorem originates in the work of Ahlswede and Gács [AG76]. The Level-k
Inequalities appear in several places but can probably be fairly credited to

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

9.7. Exercises and notes 281

Kahn, Kalai, and Linial [KKL88]. The optimal constants for Khintchine’s
Inequality were established by Haagerup [Haa82]; see also Nazarov and Pod-
korytov [NP00]. They always occur either when ∑i ai xi is just 1p
2 x1 + 1p
2 x2
or in the limiting Gaussian case of ai ≡ 1pn , n → ∞.

Ben-Or and Linial’s work [BL85, BL90] was motivated both by game
theory and by the Byzantine Generals problem [LSP82] from distributed
computing; the content of Exercise 9.25 is theirs. In turn it motivated the
watershed paper by Kahn, Kalai, and Linial [KKL88]. (See also the intermedi-
ate work of Chor and Geréb-Graus [CGG87].) The “KKL Edge-Isoperimetric
Theorem” (which is essentially a strengthening of the basic KKL Theorem)
was ﬁrst explicitly proved by Talagrand [Tal94] (possibly independently of
Kahn, Kalai, and Linial [KKL88]?); he also treated the p-biased case. There
is no known combinatorial proof of the KKL Theorem (i.e., one which does not
involve real-valued functions). However, several slightly different analytic
proofs are known; see Falik and Samorodnitsky [FS07], Rossignol [Ros06],
and O’Donnell and Wimmer [OW13]. The explicit lower bound on the “KKL
constant” achieved in Exercise 9.30 is the best known; it appeared ﬁrst in
Falik and Samorodnitsky [FS07]. It is still a factor of 2 away from the best
known upper bound, achieved by the tribes function.

Friedgut’s Junta Theorem dates from 1998 [Fri98]. The observation that
its junta size can be improved for functions which have Wk[ f ] ≤ ϵ for k ≪ I[ f ]/ϵ
was independently made by Li-Yang Tan in 2011; so was the consequence
Corollary 9.31 and its extension to constant-degree PTFs. A stronger result
than Corollary 9.31 is known: Diakonikolas and Servedio [DS09] showed
that every LTF is ϵ-close to a I[ f ]2poly(1/ϵ)-junta. As for Corollary 9.30, it’s
incomparable with a result from Gopalan, Meka, and Reingold [GMR12],
which shows that every width-w DNF is ϵ-close to a (w log(1/ϵ))O(w)-junta.

Exercise 9.3 was suggested to the author by Krzysztof Oleszkiewicz.
Exercise 9.12 is from Gopalan et al. [GOWZ10]. Exercise 9.21 appears in
O’Donnell and Servedio [OS07]; Exercise 9.22 appears in O’Donnell and Wu
[OW09]. The estimate in Exercise 9.24 is from de Klerk, Pasechnik, and
Warners [dKPW04] (see also works of Rinott and Rotar’ [RR01] and Khot
et al. [KKMO07]). Exercises 9.27 and 9.28 are due to Kahn, Kalai, and
Linial [KKL88]. Exercise 9.34 was suggested to the author by John Wright.
Exercise 9.36 appears in Kauers et al. [KOTZ16].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 10

Advanced
hypercontractivity

In this chapter we complete the proof of the Hypercontractivity Theorem for
uniform ±1 bits. We then generalize the (p, 2) and (2, q) statements to the
setting of arbitrary product probability spaces, proving the following:

The General Hypercontractivity Theorem. Let (Ω1, π1), . . . , (Ωn, πn) be
ﬁnite probability spaces, in each of which every outcome has probability at
least λ. Let f ∈ L2(Ω1 × · · · × Ωn, π1 ⊗ · · · ⊗ πn). Then for any q > 2 and 0 ≤ ρ ≤
1pq−1 · λ
1/2−1/q,
 ∥Tρ f ∥q ≤ ∥ f ∥2 and ∥Tρ f ∥2 ≤ ∥ f ∥q′.

(And in fact, the upper bound on ρ can be slightly relaxed to the value stated
in Theorem 10.18.)

We can thereby extend all the consequences of the basic Hypercontrac-
tivity Theorem for f : {−1, 1}n → R to functions f ∈ L2(Ωn, π⊗n), except with
quantitatively worse parameters depending on “λ”. We also introduce the tech-
nique of randomization/symmetrization and show how it can sometimes elim-
inate this dependence on λ. For example, it’s used to prove Bourgain’s Sharp
Threshold Theorem, a characterization of Boolean-valued f ∈ L2(Ωn, π⊗n) with
low total inﬂuence that has no dependence at all on π.

10.1. The Hypercontractivity Theorem for uniformly random
bits

In this section we’ll prove the full Hypercontractivity Theorem for uniform ±1
bits stated at the beginning of Chapter 9:
 283

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

284 10. Advanced hypercontractivity

The Hypercontractivity Theorem. Let f : {−1, 1}n → R and let 1 ≤ p ≤ q ≤ ∞.

Then ∥Tρ f ∥q ≤ ∥ f ∥p for 0 ≤ ρ ≤ √ p−1
q−1 .

Actually, when neither p nor q is 2, the following equivalent form of
theorem seems easier to interpret:

Two-Function Hypercontractivity Theorem. Let f , g : {−1, 1}n → R , let
r, s ≥ 0, and assume 0 ≤ ρ ≤ prs ≤ 1. Then

E
(x,y)
ρ-correlated

[ f (x)g(y)] ≤ ∥ f ∥1+r∥g∥1+s.

As a reminder, the only difference between this theorem and its “weak” form
(proven in Chapter 9.4) is that we don’t assume r, s ≤ 1. Below we will show
that the two theorems are equivalent, via Hölder’s inequality. Given the
Two-Function Hypercontractivity Induction Theorem from Chapter 9.4, this
implies that to prove the Hypercontractivity Theorem for general n we only
need to prove it for n = 1. This is an elementary but technical inequality,
which we defer to the end of the section.

Before carrying out these proofs, let’s take some time to interpret the
Two-Function Hypercontractivity Theorem. One interpretation is simply as
a generalization of Hölder’s inequality. Consider the case that the strings x
and y in the theorem are fully correlated; i.e., ρ = 1. Then the theorem states
that
 E[ f (x)g(x)] ≤ ∥ f ∥1+r∥g∥1+1/r (10.1)

because the condition prs = 1 is equivalent to s = 1/r. This statement is
identical to Hölder’s inequality, since (1 + r)′ = 1 + 1/r. Hölder’s inequality is
often used to “break the correlation” between two random variables; in the
absence of any information about how f and g correlate then we can at least
bound E[ f (x)g(x)] by the product of certain norms of f and g. (If f and g
have different “sizes”, then Hölder lets us choose different norms for them; if f
and g have roughly the same “size”, then we can take r = s = 1 and get Cauchy–
Schwarz.) Now suppose we are considering E[ f (x)g(y)] for ρ-correlated x, y
with ρ < 1. In this case we might hope to improve (10.1) by using smaller
norms on the right-hand side; in the extreme case of independent x, y (i.e.,
ρ = 0) we can use E[ f (x)g(y)] = E[ f ] E[g] ≤ ∥ f ∥1∥g∥1. The Two-Function
Hypercontractivity Theorem gives a precise interpolation between these two
cases; the smaller the correlation ρ is, the smaller the norms we may take on
the right-hand side.

In the case that f and g have range {0, 1}, these ideas yield another inter-
pretation of the Two-Function Hypercontractivity Theorem, namely a two-set
generalization of the Small-Set Expansion Theorem:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.1. The Hypercontractivity Theorem for uniformly random bits 285

Generalized Small-Set Expansion Theorem. Let 0 ≤ ρ ≤ 1. Let A, B ⊆
{−1, 1}n have volumes exp(− a2
2 ), exp(− b2
2 ) and assume 0 ≤ ρa ≤ b ≤ a. Then

Pr
(x,y)
ρ-correlated

[x ∈ A, y ∈ B] ≤ exp (− 1
2 a2−2ρab+b2

1−ρ2 ) .

Proof. Apply the Two-Function Hypercontractivity Theorem with f = 1A,
g = 1B and minimize the right-hand side by selecting r = ρ b−ρa
a−ρb , s = ρ a−ρb
b−ρa . □

Remark 10.1. When a and b are not too close the optimal choice of s in the
proof exceeds 1. Thus the Generalized Small-Set Expansion Theorem really
needs the full (non-weak) Two-Function Hypercontractivity Theorem; equiv-
alently, the full Hypercontractivity Theorem. Also note that the assumption
b ≥ ρa is needed to prevent r < 0.

Remark 10.2. This theorem is essentially sharp in the case that A and B
are concentric Hamming balls; see Exercise 10.5. In the case b = a we recover
the Small-Set Expansion Theorem. In the case b = ρa we get only the trivial
bound that Pr[x ∈ A, y ∈ B] ≤ exp(− a2
2 ) = Pr[x ∈ A]. However, not much better
than this can be expected; in the concentric Hamming ball case it indeed holds
that Pr[x ∈ A, y ∈ B] ∼ Pr[x ∈ A] whenever b < ρa.

Remark 10.3. There is also a reverse form of the Hypercontractivity Theorem
and its Two-Function version; see Exercises 10.6–10.9. It directly implies the
following:

Reverse Small-Set Expansion Theorem. Let 0 ≤ ρ ≤ 1. Let A, B ⊆ {−1, 1}n

have volumes exp(− a2
2 ), exp(− b2
2 ), where a, b ≥ 0. Then

Pr
(x,y)
ρ-correlated

[x ∈ A, y ∈ B] ≥ exp (− 1
2 a2+2ρab+b2

1−ρ2 ) .

We now turn to the proofs. We begin by showing that the Hypercontrac-
tivity Theorem and the Two-Function version are indeed equivalent. This is
a consequence of the following general fact (take T = Tρ, p = 1 + r, q = 1 + 1/s):

Proposition 10.4. Let T be an operator on L2(Ω, π) and let 1 ≤ p, q ≤ ∞. Then

∥T f ∥q ≤ ∥ f ∥p (10.2)

holds for all f ∈ L2(Ω, π) if and only if

〈T f , g〉 ≤ ∥ f ∥p∥g∥q′ (10.3)

holds for all f , g ∈ L2(Ω, π).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

286 10. Advanced hypercontractivity

Proof. For the “only if” statement, 〈T f , g〉 ≤ ∥T f ∥q∥g∥q′ ≤ ∥ f ∥p∥g∥q′ by Hölder’s
inequality and (10.2). As for the “if” statement, by Hölder’s inequality and (10.3)
we have
 ∥T f ∥q = sup
∥g∥q′ =1〈T f , g〉 ≤ sup
∥g∥q′ =1 ∥ f ∥p∥g∥q′ = ∥ f ∥p. □

Now suppose we prove the Hypercontractivity Theorem in the case n = 1.
By the above proposition we deduce the Two-Function version in the case
n = 1. Then the Two-Function Hypercontractivity Induction Theorem from
Chapter 9.4 yields the general-n case of the Two-Function Hypercontractivity
Theorem. Finally, applying the above proposition again we get the general-n
case of the Hypercontractivity Theorem, thereby completing all needed proofs.
These observations all hold in the context of more general product spaces, so
let’s record the following for future use:

Hypercontractivity Induction Theorem. Let 0 ≤ ρ ≤ 1, 1 ≤ p, q ≤ ∞, and
assume that ∥Tρ f ∥q ≤ ∥ f ∥p holds for every f ∈ L2(Ω1, π1), . . . , L2(Ωn, πn). Then
it also holds for every f ∈ L2(Ω1 × · · · × Ωn, π1 ⊗ · · · ⊗ πn).

Remark 10.5. In traditional proofs of the Hypercontractivity Theorem for ±1
bits, this theorem is proven directly; it’s a slightly tricky induction by deriva-
tives (see Exercise 10.3). For more general product spaces the same direct
induction strategy also works but the notation becomes quite complicated.

Our remaining task, therefore, is to prove the Hypercontractivity Theorem
in the case n = 1; in other words, to show that a uniformly random ±1 bit is
(p, q, √
(p − 1)/(q − 1))-hypercontractive. This fact is often called the “Two-
Point Inequality” because (for ﬁxed p, q, and ρ) it’s just an “elementary”
inequality about two real variables.

Two-Point Inequality. Let 1 ≤ p ≤ q ≤ ∞ and let 0 ≤ ρ ≤ √
(p − 1)/(q − 1).
Then ∥Tρ f ∥q ≤ ∥ f ∥p for any f : {−1, 1} → R . Equivalently (for ρ ̸= 1), a uni-
formly random bit x ∼ {−1, 1} is (p, q, ρ)-hypercontractive; i.e., ∥a + ρbx∥q ≤
∥a + bx∥p for all a, b ∈ R .

Proof. As in Section 9.3, our main task will be to prove the inequality for
1 ≤ p < q ≤ 2. Having done this, the 2 ≤ p < q ≤ ∞ cases follow from Propo-
sition 9.19, the p < 2 < q cases follow using the semigroup property of Tρ
(Exercise 9.17), and the p = q cases follow from Exercise 2.33 (or continuity).
The proof for 1 ≤ p < q ≤ 2 will be very similar to that of Theorem 9.18 (the
q = 2 case). As in that proof we may reduce to the case that ρ = √(p − 1)/(q − 1),

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.2. Hypercontractivity of general random variables 287

a = 1, and b = ϵ satisﬁes |ϵ| < 1. It then sufﬁces to show

∥1 + ρϵx∥p
q ≤ ∥1 + ϵx∥p
p

⇐⇒ ( 1
2 (1 + ρϵ)q + 1
2 (1 − ρϵ)q)p/q ≤ 1
2 (1 + ϵ)p + 1
2 (1 − ϵ)p

⇐⇒
 (
1 + ∞∑

k=1
 ( q
2k)
ρ2kϵ2k)p/q ≤ 1 + ∞∑

k=1
 ( p
2k)
ϵ2k. (10.4)

Again we used |ϵ| < 1 to drop the absolute value signs and justify the Gen-
eralized Binomial Theorem. For each of the binomial coefﬁcients on the left
in (10.4) we have
( q
2k) = q(q−1)(q−2)(q−3)···(q−(2k−2))(q−(2k−1))
(2k)! = q(q−1)(2−q)(3−q)···((2k−2)−q)((2k−1)−q)
(2k)! ≥ 0.

(Here we reversed an even number of signs, since 1 ≤ q ≤ 2. We will later do
the same when expanding ( p
2k)
.) Thus we can again employ the inequality
(1+ t)
θ ≤ 1+ θt for t ≥ 0 and 0 ≤ θ ≤ 1 to deduce that the left-hand side of (10.4)
is at most
 1 + ∞∑

k=1
 p
q ( q
2k)
ρ2kϵ2k = 1 + ∞∑

k=1
 p
q
 ( p−1
q−1
 )k ( q
2k)
ϵ2k.

We can now complete the proof of (10.4) by showing the following term-by-
term inequality: for all k ≥ 1,
 p
q
 ( p−1
q−1
 )k ( q
2k) ≤ ( p
2k)

⇐⇒ p
q
 ( p−1
q−1
 )k q(q−1)(2−q)···((2k−1)−q)
(2k)! ≤ p(p−1)(2−p)···((2k−1)−p)
(2k)!

⇐⇒ 2−qpq−1 · 3−qpq−1 · · · (2k−1)−qpq−1 ≤ 2−ppp−1 · 3−ppp−1 · · · (2k−1)−ppp−1 .

And indeed this inequality holds factor-by-factor. This is because p < q and
j−r
pr−1 is a decreasing function of r ≥ 1 for all j ≥ 2, as is evident from d
dr j−r
pr−1 =

− j−2+r
2(r−1)3/2 . □

Remark 10.6. The upper-bound ρ ≤ √
(p − 1)/(q − 1) in this theorem is best
possible; see Exercise 9.10(b).

10.2. Hypercontractivity of general random variables

Let’s now study hypercontractivity for general random variables. By the end
of this section we will have proved the General Hypercontractivity Theorem
stated at the beginning of the chapter.

Recall Deﬁnition 9.13 which says that X is (p, q, ρ)-hypercontractive if
E[|X |q] < ∞ and

∥a + ρbX ∥q ≤ ∥a + bX ∥p for all constants a, b ∈ R .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

288 10. Advanced hypercontractivity

(By homogeneity, it’s sufﬁcient to check this either with a ﬁxed to 1 or with b
ﬁxed to 1.) Let’s also collect some additional basic facts regarding the concept:

Fact 10.7. Suppose X is (p, q, ρ)-hypercontractive (1 ≤ p ≤ q ≤ ∞, 0 ≤ ρ < 1).
Then:

(1) E[X ] = 0 (Exercise 9.10).

(2) cX is (p, q, ρ)-hypercontractive for any c ∈ R (Exercise 9.9).

(3) X is (p, q, ρ′)-hypercontractive for any 0 ≤ ρ′ < ρ (Exercise 9.11).

(4) ρ ≤ √ p−1
q−1 and ρ ≤ ∥X ∥p
∥X ∥q (Exercises 9.10, 9.9).

Proposition 10.8. Let X be (2, q, ρ)-hypercontractive. Then X is also (q′, 2, ρ)-
hypercontractive, where q′ is the conjugate Hölder index of q.

Proof. The deduction is essentially the same as (9.6) from Chapter 9.2. Since
E[X ] = 0 (Fact 10.7(1)) we have

∥a + ρbX ∥
2
2 = E[a2 + 2ρabX + ρ2b2 X 2] = E[(a + bX )(a + ρ2bX )].

By Hölder’s inequality and then the (2, q, ρ)-hypercontractivity of X this is at
most
 ∥a + bX ∥q′∥a + ρ2bX ∥q ≤ ∥a + bX ∥q′∥a + ρbX ∥2.

Dividing through by ∥a + ρbX ∥2 (which can’t be 0 unless X ≡ 0) gives ∥a +
ρbX ∥2 ≤ ∥a + bX ∥q′ as needed. □

Remark 10.9. The converse does not hold; see Exercise 10.4.

Remark 10.10. As mentioned in Proposition 9.15, the sum of independent
hypercontractive random variables is equally hypercontractive. Furthermore,
low-degree polynomials of independent hypercontractive random variables
are “reasonable”. See Exercises 10.2 and 10.3.

Given X , p, and q, computing the largest ρ for which X is (p, q, ρ)-
hypercontractive can often be quite a chore. However, if you’re not overly
concerned about constant factors then things become much easier. Let’s focus
on the most useful case, p = 2 and q > 2. By Fact 10.7(2) we may assume
∥X ∥2 = 1. Then we can ask:

Question 10.11. Let E[X ] = 0, ∥X ∥2 = 1, and assume ∥X ∥q < ∞. For what ρ
is X (2, q, ρ)-hypercontractive?

In this section we’ll answer the question by showing that ρ = Θq(1/∥X ∥q)
is sufﬁcient. By the second part of Fact 10.7(4), ρ ≤ 1/∥X ∥q is also necessary.
So for a mean-zero random variable X , the largest ρ for which X is (2, q, ρ)-
hypercontractive is always within a constant (depending only on q) of ∥X ∥2
∥X ∥q .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.2. Hypercontractivity of general random variables 289

Let’s arrive at this result in steps, introducing the useful techniques of
symmetrization and randomization along the way. When studying hypercon-
tractivity of a random variable X , things are much more convenient if X is
a symmetric random variable, meaning −X has the same distribution as X .
One advantage of symmetric random variables X is that they have E[X k] = 0
for all odd k ∈ N . Using this it is easy to prove (Exercise 10.11) the following
fact, similar to Corollary 9.6. (The proof similar to that of Proposition 9.16.)

Proposition 10.12. Let X be a symmetric random variable with ∥X ∥2 = 1.
Assume that ∥X ∥4 = C (and hence X is “C4-reasonable”). Then X is (2, 4, ρ)-
hypercontractive if and only if ρ ≤ min( 1p
3 , 1
C ).

Given a symmetric random variable X , the randomization trick is to
replace X by the identically distributed random variable r X , where r ∼ {−1, 1}
is an independent uniformly random bit. This trick sometimes lets you reduce
a probabilistic statement about X to a related one about r.

Theorem 10.13. Let X be a symmetric random variable with ∥X ∥2 = 1 and
let ∥X ∥q = C, where q > 2. Then X is (2, q, ρ)-hypercontractive for ρ = 1
Cpq−1 .

Proof. Let r ∼ {−1, 1} be uniformly random and let ̃X denote X /C. Then for
any a ∈ R ,

∥a + ρ X ∥2
q = ∥a + ρr X ∥
2
q (by symmetry of X )

= E
X
 [
E
r [|a + ρr X |q]]2/q

≤ E
X
 [
E
r [|a + 1
C r X |2]q/2]2/q (r is (2, q, 1pq−1 )-hypercontractive)

= E
X [(a2 + ̃X 2)q/2]2/q (Parseval)

= ∥a2 + ̃X 2∥q/2 (norm with respect to X )

≤ a2 + ∥ ̃X 2∥q/2 (triangle inequality for ∥ · ∥q/2)

= a2 + ∥ ̃X ∥
2
q

= a2 + 1 = a2 + E[X 2] = ∥a + X ∥
2
2,

where the last step also used E[X ] = 0. □

Next, if X is not symmetric then we can use a symmetrization trick to
make it so. One way to do this is to replace X with the symmetric random
variable X − X ′, where X ′ is an independent copy of X . In general X − X ′

has similar properties to X . In particular, if E[X ] = 0 we can compare norms
using the following one-sided bound:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

290 10. Advanced hypercontractivity

Lemma 10.14. Let X be a random variable satisfying E[X ] = 0 and ∥X ∥q < ∞,
where q ≥ 1. Then for any a ∈ R ,

∥a + X ∥q ≤ ∥a + X − X ′∥q,

where X ′ denotes an independent copy of X .

Proof. We have
 ∥a + X ∥q
q = E[|a + X |q] = E[|a + X − E[X ′]|q],

where we used the fact that E[X ′ | X ] ≡ 0. But now

E[|a + X − E[X ′]|q] = E[| E[a + X − X ′]|q] ≤ E[|a + X − X ′|q] = ∥a + X − X ′∥q
q,

where we used convexity of t 7→ |t|q. □

A combination of the randomization and symmetrization tricks is to re-
place an arbitrary random variable X by r X , where r ∼ {−1, 1} is an indepen-
dent uniformly random bit. This often lets you extend results about symmet-
ric random variables to the case of general mean-zero random variables. For
example, the following hypercontractivity lemma lets us reduce to the case of
a symmetric random variable while only “spending” a factor of 1
2 :

Lemma 10.15. Let X be a random variable satisfying E[X ] = 0 and ∥X ∥q < ∞,
where q ≥ 1. Then for any a ∈ R ,

∥a + 1
2 X ∥q ≤ ∥a + r X ∥q,

where r ∼ {−1, 1} is an independent uniformly random bit.

Proof. Letting X ′ be an independent copy of X we have

∥a + 1
2 X ∥q ≤ ∥a + 1
2 X − 1
2 X ′∥q (Lemma 10.14 applied to 1
2 X )

= ∥a + r( 1
2 X − 1
2 X ′)∥q (since 1
2 X − 1
2 X ′ is symmetric)

= ∥ 1
2 a + 1
2 r X + 1
2 a − 1
2 r X ′∥q

≤ ∥ 1
2 a + 1
2 r X ∥q + ∥ 1
2 a − 1
2 r X ′∥q (triangle inequality for ∥ · ∥q)

= ∥ 1
2 a + 1
2 r X ∥q + ∥ 1
2 a + 1
2 r X ′∥q (−r distributed as r)

= ∥a + r X ∥q. □

By employing these randomization/symmetrization techniques we obtain
a (2, q)-hypercontractivity statement for all mean-zero random variables X
with ∥X ∥q
∥X ∥2 bounded, giving a good answer to Question 10.11:

Theorem 10.16. Let X satisfy E[X ] = 0, ∥X ∥2 = 1, ∥X ∥q = C, where q > 2.
Then X is (2, q, 1
2 ρ)-hypercontractive for ρ = 1
Cpq−1 . (If X is symmetric, then

the factor of 1
2 may be omitted.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.2. Hypercontractivity of general random variables 291

Proof. By Lemma 10.15 we have

∥a + 1
2 ρ X ∥
2
q ≤ ∥a + ρr X ∥
2
q.

Since r X is a symmetric random variable satisfying ∥r X ∥2 = 1, ∥r X ∥q = C,
Theorem 10.13 implies

∥a + ρr X ∥
2
q ≤ ∥a + r X ∥
2
2 = a2 + 1 = ∥a + X ∥2
2.

This completes the proof. □

If X is a discrete random variable then instead of computing ∥X ∥2
∥X ∥q it can
sometimes be convenient to use a bound based on the minimum value of
X ’s probability mass function. The following is a simple generalization of
Proposition 9.5, whose proof is left for Exercise 10.17:

Proposition 10.17. Let X be a discrete random variable with probability
mass function π. Write

λ = min(π) = min
x∈range(X ){Pr[X = x]}.

Then for any q > 2 we have ∥X ∥q ≤ (1/λ)1/2−1/q · ∥X ∥2.

As a consequence of Theorem 10.16, if in addition E[X ] = 0 then X
is (2, q, 1
2 ρ)-hypercontractive for ρ = 1pq−1 · λ
1/2−1/q, and X is also (q′, 2, 1
2 ρ)-

hypercontractive by Proposition 10.8. (If X is symmetric then the factor of 1
2
may be omitted.)

For each q > 2, the value ρ = Θq(λ
1/2−1/q) in Proposition 10.17 has the
optimal dependence on λ, up to a constant. In fact, a perfectly sharp version
of Proposition 10.17 is known. The most important case is when X is a
λ-biased bit; more precisely, when X = φ(xi) for xi ∼ πλ in the notation of
Deﬁnition 8.39. In that case, the below theorem (whose very technical proof
is left to Exercises 10.19–10.21) is due to Latała and Oleszkiewicz [LO00].
The case of general discrete random variables is a reduction to the two-valued
case due to Wolff [Wol07].

Theorem 10.18. Let X be a mean-zero discrete random variable and let
λ < 1/2 be the least value of its probability mass function, as in Proposi-
tion 10.17. Then for q > 2 it holds that X is (2, q, ρ)-hypercontractive and
(q′, 2, ρ)-hypercontractive for

ρ =
 √ exp(u/q) − exp(−u/q)
exp(u/q′) − exp(−u/q′) =
 √ sinh(u/q)
sinh(u/q′) , with u deﬁned by exp(−u) = λ
1−λ .

(10.5)
This value of ρ is optimal, even under the assumption that X is two-valued.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

292 10. Advanced hypercontractivity

Remark 10.19. It’s not hard to see that for λ → 1/2 (hence u → 0) we get

ρ → √ 1/q−(−1/q)
1/q′−(−1/q′) = 1pq−1 , consistent with the Two-Point Inequality from Sec-

tion 10.1. Also, for λ → 0 (hence u → ∞) we get ρ ∼ √ λ−1/q

λ−1/q′ = λ
1/2−1/q, showing
that Proposition 10.17 is sharp up to a q-dependent constant. Exercise 10.18
asks you to investigate the function deﬁning ρ in (10.5) more carefully. In
particular, you’ll show that ρ ≥ 1pq−1 · λ
1/2−1/q holds for all λ. Hence we can

omit the factor of 1
2 from the simpler bound in Proposition 10.17 even for
nonsymmetric random variables.

Corollary 10.20. Let (Ω, π) be a ﬁnite probability space, |Ω| ≥ 2, in which
every outcome has probability at least λ. Let f ∈ L2(Ω, π). Then for any q > 2
and 0 ≤ ρ ≤ 1pq−1 · λ
1/2−1/q,

∥Tρ f ∥q ≤ ∥ f ∥2 and ∥Tρ f ∥2 ≤ ∥ f ∥q′.

Proof. Recalling Chapter 8.3, this follows from the decomposition f (x) =
f ; + f ={1}, under which Tρ f = f ; + ρ f ={1}. Note that for x ∼ π the random
variable f ={1}(x) has mean zero, and the least value of its probability mass
function is at least λ. □

The General Hypercontractivity Theorem stated at the beginning of the chap-
ter now follows by applying the Hypercontractivity Induction Theorem from
Section 10.1.

10.3. Applications of general hypercontractivity

In this section we will collect some applications of the General Hypercontrac-
tivity Theorem, including generalizations of the facts from Section 9.5. We
begin by bounding the q-norms of low-degree functions. The proof is essen-
tially the same as that of Theorem 9.21; see Exercise 10.28.

Theorem 10.21. In the setting of the General Hypercontractivity Theorem,
if f has degree at most k, then

∥ f ∥q ≤ (√q − 1 · λ
1/q−1/2)k∥ f ∥2.

Next we turn to an analogue of Theorem 9.22, getting a relationship
between the 2-norm and the 1-norm for low-degree functions. The proof (Ex-
ercise 10.31) needs (2, q, ρ)-hypercontractivity with q tending to 2, so to get
the most elegant statement requires appealing to the sharp bound from Theo-
rem 10.18:
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.3. Applications of general hypercontractivity 293

Theorem 10.22. In the setting of the General Hypercontractivity Theorem, if
f has degree at most k, then

∥ f ∥2 ≤ c(λ)k∥ f ∥1, where c(λ) = √ 1−λ
λ
 1/(1−2λ).

We have c(λ) ∼ 1/
p
λ as λ → 0, c(λ) → e as λ → 1
2 , and in general, c(λ) ≤ e/
p
2λ.

Just as in Chapter 9.5 we obtain (Exercise 10.32) the following as a corol-
lary:

Theorem 10.23. In the setting of the General Hypercontractivity Theorem, if
f is a nonconstant function of degree at most k, then

Pr
x∼π⊗n[ f (x) > E[ f ]
] ≥ 1
4 (e2/2λ)−k ≥ (15/λ)
−k.

Extending Theorem 9.23, the concentration bound for degree-k functions,
is straightforward (see Exercise 10.33). We again get that the probability of
exceeding t standard deviations decays like exp(−Θ(t2/k)), though the constant
in the Θ(·) is linear in λ:

Theorem 10.24. In the setting of the General Hypercontractivity Theorem, if

f has degree at most k, then for any t ≥ p
2e/λk,

Pr
x∼π⊗n[| f (x)| ≥ t∥ f ∥2] ≤ λk exp (− k
2e λt2/k) .

Next, we give a generalization of the Small-Set Expansion Theorem, the
proof being left for Exercise 10.34.

Theorem 10.25. Let (Ω, π) be a ﬁnite probability space, |Ω| ≥ 2, in which every
outcome has probability at least λ. Let A ⊆ Ωn have “volume” α; i.e., suppose
Prx∼π⊗n [x ∈ A] = α. Let q ≥ 2. Then for any

0 ≤ ρ ≤ 1
q−1 · λ
1−2/q

(or even ρ as large as the square of the quantity in Theorem 10.18) we have

Stabρ[1A] = Pr
x∼π⊗n
y∼Nρ(x)[x ∈ A, y ∈ A] ≤ α
2−2/q.

Similarly, we can generalize Corollary 9.25, bounding the stable inﬂuence of
a coordinate by a power of the usual inﬂuence:

Theorem 10.26. In the setting of Theorem 10.25, if f : Ωn → {−1, 1}, then

ρInf(ρ)
i [ f ] ≤ Infi[ f ]
2−2/q.

for all i ∈ [n]. In particular, by selecting q = 4 we get
∑

S∋i(
p
λ/3)|S|∥ f =S∥
2
2 ≤ Infi[ f ]
3/2. (10.6)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

294 10. Advanced hypercontractivity

Proof. Applying the General Hypercontractivity Theorem to Li f and squar-
ing we get ∥Tp
ρLi f ∥
2
2 ≤ ∥Li f ∥
2
q′.

By deﬁnition, the left-hand side is ρInf(ρ)
i [ f ]. The right-hand side is

(∥Li f ∥q′

q′)
2−2/q, and ∥Li f ∥q′

q′ ≤ Infi[ f ] by Exercise 8.10(b). □

The KKL Edge-Isoperimetic Theorem in this setting now follows by an
almost verbatim repetition of the proof from Chapter 9.6.

KKL Isoperimetric Theorem for general product space domains. In
the setting of the General Hypercontractivity Theorem, suppose f has range
{−1, 1} and is nonconstant. Let ̃I[ f ] = I[ f ]/ Var[ f ] ≥ 1. Then

MaxInf[ f ] ≥ 1
̃I[ f ]2 · (9/λ)
−̃I[ f ].

As a consequence, MaxInf[ f ] ≥ Ω( 1
log(1/λ) ) · Var[ f ] · log n
n .

Proof. (Cf. Exercise 9.29.) The proof is essentially identical to the one in
Chapter 9.6, but using (10.6) from Theorem 10.26. Summing this inequality
over all i ∈ [n] yields

∑

S⊆[n] |S|(p
λ/3)|S|∥ f =S∥
2
2 ≤ n∑

i=1 Infi[ f ]
3/2 ≤ MaxInf[ f ]
1/2 · I[ f ]. (10.7)

On the left-hand side above we will drop the factor of |S| for |S| > 0. We also in-
troduce a set-valued random variable S deﬁned by Pr[S = S] = ∥ f =S∥
2
2/ Var[ f ]
for S ̸= ;. Note that E[|S|] = ̃I[ f ]. Thus

LHS(10.7) ≥ Var[ f ] · E
S [(p
λ/3)|S|] ≥ Var[ f ] · (
p
λ/3)E[|S|] = Var[ f ] · (
p
λ/3)
̃I[ f ],

where we used that s 7→ (
p
λ/3)s is convex. The ﬁrst statement of the theorem
now follows after rearrangement. As for the second statement, there is some
universal c > 0 such that

̃I[ f ] ≤ c · 1
log(1/λ) · log n =⇒ 1
̃I[ f ]2 · (9/λ)
−̃I[ f ] = O(1/λ)
−̃I[ f ] ≥ 1
pn ,

say, in which case our lower bound for MaxInf[ f ] is 1pn ≫ log n
n . On the other
hand,
 ̃I[ f ] ≥ c · 1
log(1/λ) · log n =⇒ I[ f ] ≥ Ω( 1
log(1/λ) ) · Var[ f ] · log n,

in which case even the average inﬂuence of f is Ω( 1
log(1/λ) ) · Var[ f ] · log n
n . □

Similarly, essentially no extra work is required to generalize Theorem 9.28
and Friedgut’s Junta Theorem to general product space domains; see Exer-
cise 10.35. For example, we have:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.3. Applications of general hypercontractivity 295

Friedgut’s Junta Theorem for general product space domains. In the
setting of the General Hypercontractivity Theorem, if f has range {−1, 1} and
0 < ϵ ≤ 1, then f is ϵ-close to a (1/λ)O(I[ f ]/ϵ)-junta h : Ωn → {−1, 1} (that is,
Prx∼π⊗n [ f (x) ̸= h(x)] ≤ ϵ).

We conclude this section by establishing “sharp thresholds” – in the sense
of Chapter 8.4 – for monotone transitive-symmetric functions with critical
probability in the range [1/no(1), 1 − 1/no(1)]. Let f : {−1, 1}n → {−1, 1} be a
nonconstant monotone function and deﬁne the (strictly increasing) curve
F : [0, 1] → [0, 1] by F(p) = Prx∼π⊗n
p [ f (x) = −1]. Recall that the critical proba-
bility pc is deﬁned to be the value such that F(pc) = 1/2; equivalently, such
that Var[ f (pc)] = 1. Recall also the Margulis–Russo Formula, which says that

d
d p F(p) = 1

σ2 · I[ f (p)],

where
 σ2 = σ2(p) = Var
πp [xi] = 4p(1 − p) = Θ(min(p, 1 − p)).

Remark 10.27. Since we will not be concerned with constant factors, it’s
helpful in the following discussion to mentally replace σ2 with min(p, 1 − p).
In fact it’s even more helpful to always assume p ≤ 1/2 and replace σ2 with p.

Now suppose f is a transitive-symmetric function, e.g., a graph property.
This means that all of its inﬂuences are the same, i.e.,

Infi[ f (p)] = MaxInf[ f (p)] = 1
n I[ f (p)]

for all i ∈ [n]. It thus follows from the KKL Theorem for general product
spaces that I[ f (p)] ≥ Ω( 1
log(1/ min(p,1−p)) ) · Var[ f (p)] · log n;

hence d
d p F(p) ≥ Var[ f (p)] · Ω( 1
σ2 ln(e/σ2) ) · log n. (10.8)

(As mentioned in Remark 10.27, assuming p ≤ 1/2 you can read σ2 ln(e/σ2) as
p log(1/p).)

If we take p = pc in inequality (10.8) we conclude that F(p) has a large
derivative at its critical probability: F ′(pc) ≥ Ω( 1
pc log(1/pc) ) · log n, assuming

pc ≤ 1/2. In particular if log(1/pc) ≪ log n – that is, pc > 1/no(1) – then F ′(pc) =
ω( 1
pc ). This suggests that f has a “sharp threshold”; i.e., F(p) jumps from
near 0 to near 1 in an interval of the form pc(1 ± o(1)). However, largeness of
F ′(pc) is not quite enough to establish a sharp threshold (see Exercise 8.30);
we need to have F ′(p) large throughout the range of p near pc where Var[ f (p)]
is large. Happily, inequality (10.8) provides precisely this.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

296 10. Advanced hypercontractivity

Remark 10.28. Even if we are only concerned about monotone functions f
with pc = 1/2, we still need the KKL Theorem for general product spaces to
establish a sharp threshold. Though F ′(1/2) ≥ Ω(log n) can be derived using
just the uniform-distribution KKL Theorem from Chapter 9.6, we also need
to know that F ′(p) ≥ Ω(log n) continues to hold for p = 1/2 ± O(1/ log n).

Making the above ideas precise, we can establish the following result of
Friedgut and Kalai [FK96] (cf. Exercises 8.28, 8.29):

Theorem 10.29. Let f : {−1, 1}n → {−1, 1} be a nonconstant, monotone, transitive-
symmetric function and let F : [0, 1] → [0, 1] be the strictly increasing function
deﬁned by F(p) = Prx∼π⊗n
p [ f (x) = −1]. Let pc be the critical probability such
that F(pc) = 1/2 and assume without loss of generality that pc ≤ 1/2. Fix
0 < ϵ < 1/4 and let
 η = B log(1/ϵ) · log(1/pc)
log n ,

where B > 0 is a certain universal constant. Then assuming η ≤ 1/2,

F(pc · (1 − η)) ≤ ϵ, F(pc · (1 + η)) ≥ 1 − ϵ.

Proof. Let p be in the range pc · (1 ± η). By the assumption η ≤ 1/2 we also
have 1
2 pc ≤ p ≤ 3
2 pc ≤ 3
4 . It follows that the quantity σ2 ln(e/σ2) in the KKL
corollary (10.8) is within a universal constant factor of pc log(1/pc). Thus for
all p in the range pc · (1 ± η) we obtain

F ′(p) ≥ Var[ f (p)] · Ω( 1
pc log(1/pc) ) · log n.

Using Var[ f (p)] = 4F(p)(1 − F(p)), the deﬁnition of η, and a suitable choice
of B, this is equivalent to

F ′(p) ≥ 2 ln(1/2ϵ)

ηpc F(p)(1 − F(p)). (10.9)

We now show that (10.9) implies that F(pc −ηpc) ≤ ϵ and leave the implication
F(pc + ηpc) ≥ 1 − ϵ to Exercise 10.36. For p ≤ pc we have 1 − F(p) ≥ 1/2 and
hence
 F ′(p) ≥ ln(1/2ϵ)

ηpc F(p) =⇒ d
d p ln F(p) = F ′(p)
F(p) ≥ ln(1/2ϵ)

ηpc .

It follows that

ln F(pc − ηpc) ≤ ln F(pc) − ln(1/2ϵ) = ln(1/2) − ln(1/2ϵ) = ln ϵ;

i.e., F(pc − ηpc) ≤ ϵ as claimed. □

This proof establishes that every monotone transitive-symmetric func-
tion with critical probability at least 1/no(1) (and at most 1 − 1/no(1)) has a
sharp threshold. Unfortunately, the restriction on the critical probability
can’t be removed. The simplest example illustrating this is the logical OR

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.4. More on randomization/symmetrization 297

function ORn : {True,False}n → {True,False} (equivalently, the graph property
of containing an edge), which has critical probability pc ∼ ln 2
n . Even though
ORn is transitive-symmetric, it has constant total inﬂuence at its critical
probability, I[OR
(pc)
n ] ∼ 2 ln 2. Indeed, ORn doesn’t have a sharp threshold;
i.e., it’s not true that Prπp [ORn(x) = True] = 1 − o(1) for p = pc(1 + o(1)). For
example, if x is drawn from the (2pc)-biased distribution we still just have
Pr[ORn(x) = True] ≈ 3/4. On the other hand, most “interesting” monotone
transitive-symmetric functions do have a sharp threshold; in Section 10.5
we’ll derive a more sophisticated method for establishing this.

10.4. More on randomization/symmetrization

In Section 10.3 we collected a number of consequences of the General Hy-
percontractivity Theorem for functions f ∈ L2(Ωn, π⊗n). All of these had a
dependence on “λ”, the least probability of an outcome under π. This can
sometimes be quite expensive; for example, the KKL Theorem and its conse-
quence Theorem 10.29 are trivialized when λ = 1/nΘ(1).

However, as mentioned in Section 10.2, when working with symmetric
random variables X , the “randomization” trick sometimes lets us reduce
to the analysis of uniformly random ±1 bits (which have λ = 1/2). Further,
Lemma 10.15 suggests a way of “symmetrizing” general mean-zero random
variables (at least if we don’t mind applying T 1
2 ). In this section we will de-
velop the randomization/symmetrization technique more thoroughly and see
an application: bounding the L p → L p norm of the “low-degree projection”
operator.

Informally, applying the randomization/symmetrization technique to f ∈
L2(Ωn, π⊗n) means introducing n independent uniformly random bits r =
(r1, . . . , rn) ∼ {−1, 1}n and then “multiplying the ith input to f by r i”. Of course
Ω is just an abstract set so this doesn’t quite make sense. What we really
mean is “multiplying Li f , the ith part of f ’s Fourier expansion (orthogonal
decomposition), by r i”. Let’s see some examples:

Example 10.30. Let f : {−1, 1}n → R be a usual Boolean function with Fourier
expansion f (x) = ∑

S⊆[n] ̂f (S) ∏

i∈S xi.

Its randomization/symmetrization will be the function

̃f (r, x) = ∑

S⊆[n] ̂f (S) ∏

i∈S r i xi = ∑

S⊆[n] ̂f (S) xS rS.

The key observation is that for random inputs x, r ∼ {−1, 1}n, the random
variables f (x) and ̃f (r, x) are identically distributed. This is simply because
xi is a symmetric random variable, so it has the same distribution as r i xi.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

298 10. Advanced hypercontractivity

Example 10.31. Let’s return to Examples 8.10 and 8.15 from Chapter 8.1.
Here we had Ω = {a, b, c} with π the uniform distribution, and we deﬁned a
certain Fourier basis {φ0 ≡ 1, φ1, φ2}. A typical f : Ω3 → R here might look like

f (x1, x2, x3) = 1
3 − 1
4 · φ1(x1) + 3
2 · φ2(x1) + ·φ1(x2) + 1
2 · φ2(x2) − 2
3 · φ2(x3)

+ 1
6 · φ1(x1) · φ2(x3) + 1
8 · φ1(x2) · φ1(x3)

− 1
10 · φ1(x1) · φ2(x2) · φ3(x3) + 1
5 · φ2(x1) · φ2(x2) · φ2(x3).

The randomization/symmetrization of this function would be the following
function ̃f ∈ L2({−1, 1}
3 × Ω3, π⊗3
1/2 ⊗ π⊗3):

̃f (r, x) = 1
3 − 1
4 φ1(x1) · r1 + 3
2 φ2(x1) · r1 + φ1(x2) · r2 + 1
2 φ2(x2) · r2 − 2
3 φ2(x3) · r3

+ 1
6 φ1(x1) · φ2(x3) · r1r3 + 1
8 φ1(x2) · φ1(x3) · r2r3

− 1
10 φ1(x1) · φ2(x2) · φ3(x3) · r1r2r3 + 1
5 φ2(x1) · φ2(x2) · φ2(x3) · r1r2r3.

There’s no obvious way to compare the distributions of f (x) and ̃f (r, x). How-
ever, looking carefully at Example 8.10 we see that the basis function φ2 has
the property that φ2(xi) is a symmetric real random variable when xi ∼ π.
In particular, r i · φ2(xi) has the same distribution as φ2(xi). Therefore if
g ∈ L2(Ωn, π⊗n) has the lucky property that its Fourier expansion happens
to only use φ2 and never uses φ1, then we do have that g(x) and ̃g(r, x) are
identically distributed.

Let’s give a formal deﬁnition of randomization/symmetrization.

Deﬁnition 10.32. Let f ∈ L2(Ωn, π⊗n). The randomization/symmetrization
of f is the function ̃f ∈ L2({−1, 1}n × Ωn, π⊗n
1/2 ⊗ π⊗n) deﬁned by

̃f (r, x) = ∑

S⊆[n] rS f =S(x), (10.10)

where we recall the notation rS = ∏i∈S r i.

Remark 10.33. Another way of deﬁning ̃f is to stipulate that for each x ∈ Ωn,
the function ̃f|x : {−1, 1}n → R is deﬁned to be the Boolean function whose
Fourier coefﬁcient on S is f =S(x). (This is more evident from (10.10) if you
swap the positions of rS and f =S(x).)

In light of this remark, the basic Parseval formula for Boolean functions
implies that for all x ∈ Ωn,
 ∥ ̃f|x∥
2
2,r = ∑

S⊆[n] f =S(x)2.

(The notation ∥ · ∥2,r emphasizes that the norm is computed with respect to
the random inputs r.) If we take the expectation of the above over x ∼ π⊗n,
the left-hand side becomes ∥ ̃f ∥
2
2,r,x and the right-hand side becomes ∥ f ∥
2
2,x,

by Parseval’s formula for L2(Ωn, π⊗n). Thus:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.4. More on randomization/symmetrization 299

Proposition 10.34. Let f ∈ L2(Ωn, π⊗n). Then ∥ ̃f ∥2 = ∥ f ∥2.

Thus randomization/symmetrization doesn’t change 2-norms. What about
q-norms for q ̸= 2? As discussed in Examples 10.30 and 10.31, there may be
cases where f ’s Fourier expansion is already symmetric; in such cases ̃f (r, x)
and f (x) will have identical distributions, so their q-norms will be identical.
The essential feature of the randomization/symmetrization technique is that
even for general f the q-norms don’t change much – if you are willing to apply
Tρ for some constant ρ:

Theorem 10.35. For f ∈ L2(Ωn, π⊗n) and q > 1,

∥T 1
2 f ∥q ≤ ∥ ̃f ∥q ≤ ∥Tc−1
q f ∥q. (10.11)

Equivalently, ∥ ‡Tcq f ∥q ≤ ∥ f ∥q ≤ ∥ ˜T2 f ∥q.

Here 0 < cq ≤ 1 is a constant depending only on q; in particular, we may take
c4 = c4/3 = 2
5 .

The two inequalities in (10.11) are not too difﬁcult to prove; for example,
you might already correctly guess that the left-hand inequality follows from
our ﬁrst randomization/symmetrization Lemma 10.15 and an induction. We’ll
give the proofs at the end of this section. But ﬁrst, let’s illustrate how you
might use them by solving the following basic problem concerning low-degree
projections:

Question 10.36. Let k ∈ N , let 1 < q < ∞, and let f ∈ L2(Ωn, π⊗n). Can
∥ f ≤k∥q be much larger than ∥ f ∥q? To put the question in reverse, suppose
g ∈ L2(Ωn, π⊗n) has degree at most k; is it possible to make the q-norm of g
much smaller by adding terms of degree exceeding k to its Fourier expansion?

The question has a simple answer if q = 2: in this case we have ∥ f ≤k∥2 ≤
∥ f ∥2 always. This follows from Paresval:

∥ f ≤k∥2
2 = k∑

j=0 W j[ f ] ≤ n∑

j=0 W j[ f ] = ∥ f ∥
2
2. (10.12)

When q ̸= 2 things are not so simple, so let’s ﬁrst consider the most familiar
setting of Ω = {−1, 1}, π = π1/2. In this case we can relate the q-norm and the
2-norm via the Hypercontractivity Theorem:

Proposition 10.37. Let k ∈ N and let g : {−1, 1}n → R . Then for q ≥ 2 we have

∥g≤k∥q ≤ √q − 1k∥g∥q and for 1 < q ≤ 2 we have ∥g≤k∥q ≤ (1/√q − 1)k∥g∥q.

This proposition is an easy consequence of the Hypercontractivity Theo-
rem and already appeared as Exercise 9.8. The simplest case, q = 4, follows

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

300 10. Advanced hypercontractivity

from the Bonami Lemma alone:

∥g≤k∥4 ≤ p
3k∥g≤k∥2 ≤ p
3k∥g∥2 ≤ p
3k∥g∥4. (10.13)

Now let’s consider functions f ∈ L2(Ωn, π⊗n) on general product spaces;
for simplicity, we’ll continue to focus on the case q = 4. One possibility is to
repeat the above proof using the General Hypercontractivity Theorem (more

speciﬁcally, Theorem 10.21). This would give us ∥ f ≤k∥4 ≤ p
3/λk∥ f ∥4. How-
ever, we will see that it’s possible to get a bound completely independent of λ
– i.e., independent of (Ω, π) – using randomization/symmetrization.

First, suppose we are in the lucky case described in Example 10.31 in
which f ’s Fourier spectrum only uses symmetric basis functions. In this case
f ≤k(x) and ˜f ≤k(r, x) have the same distribution for any k, and we can leverage
the L2({−1, 1}) bound (10.13) to get the same result for f . First,

∥ f ≤k∥4 = ∥ ˜f ≤k∥4 = ∥
∥
∥ ∥ ˜f ≤k|x(r)∥4,r ∥
∥
∥
4,x .

For each outcome x = x, the inner function g(r) = ˜f ≤k|x(r) is a degree-k func-
tion of r ∈ {−1, 1}n. Therefore we can apply (10.13) with this g to deduce
∥
∥
∥ ∥ ˜f ≤k|x(r)∥4,r ∥
∥
∥
4,x ≤ ∥
∥
∥ p
3k∥ ̃f|x(r)∥4,r ∥
∥
∥
4,x = p
3k∥ ̃f ∥4 = p
3k∥ f ∥4.

Thus we see that we can deduce (10.13) “automatically” for these luckily sym-
metric f , with no dependence on “λ”. We’ll now show that we can get some-
thing similar for a completely general f using the randomization/symmetrization
Theorem 10.35. This will cause us to lose a factor of (2 · 5
2 )k, due to application
of T2 and T 5
2 ; to prepare for this, we ﬁrst extend the calculation in (10.13)
slightly.

Lemma 10.38. Let k ∈ N and let g : {−1, 1}n → R . Then for any 0 < ρ ≤ 1,

∥g≤k∥4 ≤ (
p
3/ρ)k∥Tρ g∥4.

Proof. We have

∥g≤k∥4 ≤ p
3k∥g≤k∥2 ≤ (
p
3/ρ)k∥Tρ g∥2 ≤ (
p
3/ρ)k∥Tρ g∥4.

Here the ﬁrst inequality is Bonami’s Lemma and the second is because

∥g≤k∥
2
2 = k∑

j=0 W j[ f ] ≤ (1/ρ2)k k∑

j=0 ρ2 jW j[ f ] ≤ (1/ρ2)k n∑

j=0 ρ2 jW j[ f ] = (1/ρ2)k∥Tρ g∥
2
2.

□

We can now give a good answer to Question 10.36, showing that low-
degree projection doesn’t substantially increase any q-norm:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.4. More on randomization/symmetrization 301

Theorem 10.39. Let k ∈ N and let f ∈ L2(Ωn, π⊗n). Then for q > 1 we have
∥ f ≤k∥q ≤ Ck
q∥ f ∥q. Here Cq is a constant depending only on q; in particular we
may take C4, C4/3 = 5p
3 ≤ 9.

Proof. We will give the proof for q = 4; the other cases are left for Exer-
cise 10.16. Using the randomization/symmetrization Theorem 10.35,

∥ f ≤k∥4 ≤ ∥âT2 f ≤k∥4 = ∥
∥
∥ ∥âT2 f ≤k|x(r)∥4,r ∥
∥
∥
4,x .

For a given outcome x = x, let’s write g = ˜T2 f |x : {−1, 1}n → R , so that we have
∥g≤k(r)∥4 on the inside above. For clarity, we remark that g is the Boolean
function whose Fourier coefﬁcient on S is 2
|S| f =S(x). We apply Lemma 10.38
to this g, with ρ = 1
5 . Note that Tρ g is then the Boolean function whose
Fourier coefﬁcient on S is ( 2
5 )|S| f =S(x); i.e., it is ‡T 2
5 f |x. Thus we deduce

∥
∥
∥ ∥âT2 f ≤k|x(r)∥4,r ∥
∥
∥
4,x ≤ ∥
∥
∥ (5
p
3)k∥‡T 1
5 f |x(r)∥4,r ∥
∥
∥
4,x = (5
p
3)k∥‡T 2
5 f ∥4 ≤ (5p
3)k∥ f ∥4,

where the last step is the “un-randomization/symmetrization” inequality from
Theorem 10.35. □

The remainder of this section is devoted to the proof of Theorem 10.35,
which lets us compare norms of a function and its randomization/symmetrization.
It will help to view randomization/symmetrization from an operator perspec-
tive. To do this, we need to slightly extend our Tρ notation, allowing for
“different noise rates on different coordinates”.

Deﬁnition 10.40. For i ∈ [n] and ρ ∈ R , let Ti
ρ be the operator on L2(Ωn, π⊗n)
deﬁned by

Ti
ρ f = ρ f + (1 − ρ)Ei f = Ei f + ρLi f = ∑

S̸∋i f =S + ρ ∑

S∋i f =S. (10.14)

Furthermore, for r = (r1, . . . , r n) ∈ R n, let Tr be the operator on L2(Ωn, π⊗n)
deﬁned by Tr = T1
r1T
2
r2 · · · Tn
r n . From the third formula in (10.14) we have

Tr f = ∑

S⊆[n] rS f =S, (10.15)

where we use the notation rS = ∏i∈S r i. In particular, T(ρ,...,ρ) is the usual Tρ
operator. We remark that when r ∈ [0, 1]n we have

Tr f (x) = E
y1∼Nr1 (x1),...,yn∼Nrn (xn)[ f (y1, . . . , yn)].

These generalizations of the noise operator behave the way you would ex-
pect; you are referred to Exercise 8.11 for some basic properties. Now compar-
ing (10.15) and (10.10) reveals the connection to randomization/symmetrization:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

302 10. Advanced hypercontractivity

Fact 10.41. For f ∈ L2(Ωn, π⊗n), x ∈ Ωn, and r ∈ {−1, 1}n,

̃f (r, x) = Tr f (x).

In other words, randomization/symmetrization of f means applying
T(±1,±1,...,±1) to f for a random choice of signs. We use this viewpoint to prove
Theorem 10.35, which we do in two steps:

Theorem 10.42. Let f ∈ L2(Ωn, π⊗n). Then for any q ≥ 1,

∥T 1
2 f (x)∥q,x ≤ ∥Tr f (x)∥q,r,x (10.16)

for x ∼ π⊗n, r ∼ {−1, 1}n. In other words, ∥T 1
2 f ∥q ≤ ∥ ̃f ∥q.

Proof. In brief, the result follows from our ﬁrst randomization/symmetrization
result, Lemma 10.15, and an induction. To ﬁll in the details, we begin by
showing that if h ∈ L2(Ω, π) is any one-input function and ω ∼ π, b ∼ {−1, 1},
then ∥T 1
2 h(ω)∥q,ω ≤ ∥Tbh(ω)∥q,b,ω. (10.17)

This follows immediately from Lemma 10.15 because h={1}(x) is a mean-zero
random variable (cf. the proof of Corollary 10.20). Next, we show that for any
g ∈ L2(Ωn, π⊗n) and any i ∈ [n],

∥Ti
1
2 g(x)∥q,x ≤ ∥Ti
r i g(x)∥q,r i,x. (10.18)

Assuming i = 1 for notational simplicity, and writing x = (x1, x′) where x′ =
(x2, . . . , xn), we have

∥Ti
1
2 g(x)∥q,x = ∥
∥
∥
∥ ∥Ti
1
2 g(x1, x′)∥q,x1
 ∥
∥
∥
∥q,x′ = ∥
∥
∥ ∥(T 1
2 g|x′)(x1)∥q,x1 ∥
∥
∥q,x′ .

(You are asked to carefully justify the second equality here in Exercise 10.10.)
Now for each outcome of x′ we can apply (10.17) with h = g|x′ to deduce
∥
∥
∥ ∥(T 1
2 g|x′)(x1)∥q,x1 ∥
∥
∥q,x′ ≤ ∥
∥ ∥(Tr1 g|x′)(x1)∥q,x1,r1 ∥
∥q,x′ = ∥Ti
r i g(x)∥q,r i,x.

Finally, we illustrate the ﬁrst step of the induction. For distinct indices i, j,

∥Ti
1
2 T j
1
2 f (x)∥q,x ≤ ∥Ti
r i T j
1
2 f (x)∥q,r i,x

by applying (10.18) with g = T j
1
2 f . Then

∥Ti
r i T j
1
2 f (x)∥q,r i,x = ∥
∥
∥
∥ ∥Ti
r i T j
1
2 f (x)∥q,x
 ∥
∥
∥
∥q,r i = ∥
∥
∥
∥ ∥T j
1
2 Ti
r i f (x)∥q,x
 ∥
∥
∥
∥q,r i ,

where we used that Ti
ρ i and T j
ρ j commute. Now for each outcome of r i we can
apply (10.18) with g = Ti
r i f to get
∥
∥
∥
∥ ∥T j
1
2 Ti
r i f (x)∥q,x
 ∥
∥
∥
∥q,r i ≤ ∥
∥
∥ ∥T j
r j Ti
r i f (x)∥q,r j,x ∥
∥
∥q,r i = ∥Ti
r i T j
r j f (x)∥q,r i,r j,x.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.4. More on randomization/symmetrization 303

Thus we have shown

∥Ti
1
2 T j
1
2 f (x)∥q,x ≤ ∥Ti
r i T j
r j f (x)∥q,r i,r j,x.

Continuing the induction in the same way completes the proof. □

To prove the “un-randomization/symmetrization” inequality in Theorem
10.35, we ﬁrst establish an elementary lemma about mean-zero random vari-
ables:

Lemma 10.43. Let q ≥ 2. Then there is a small enough 0 < cq ≤ 1 such that

∥a − cq X ∥q ≤ ∥a + X ∥q

for any a ∈ R and any random variable X satisfying E[X ] = 0 and ∥X ∥q < ∞.
In particular we may take c4 = 2
5 .

Proof. We will only prove the statement for q = 4; you are asked to establish
the general case in Exercise 10.13. By homogeneity we may assume a = 1;
then raising the inequality to the 4th power we need to show

E[(1 − cX )4] ≤ E[(1 + X )4]

for small enough c. Expanding both sides and using E[X ] = 0, this is equiva-
lent to
 E[(1 − c4)X 4 + (4 + 4c3)X 3 + (6 − 6c2)X 2] ≥ 0. (10.19)

It sufﬁces to ﬁnd c such that

(1 − c4)x2 + (4 + 4c3)x + (6 − 6c2) ≥ 0 ∀x ∈ R ; (10.20)

then we can multiply (10.20) by x2 and take expectations to obtain (10.19).
This last problem is elementary, and Exercise 10.14 asks you to ﬁnd the
largest c that works (the answer is c ≈ .435). To see that c = 2
5 sufﬁces, we
use the fact that x ≥ − 2
9 x2 − 9
8 for all x (because the difference of the left- and
right-hand sides is 1
72 (4x + 9)
2). Putting this into (10.20), it remains to ensure

( 1
9 − 8
9 c3 − c4)x2 + ( 3
2 − 6c2 − 9
2 c3) ≥ 0 ∀x ∈ R ,

and when c = 2
5 this is the trivially true statement 161
5625 x2 + 63
250 ≥ 0. □

Theorem 10.44. Let f ∈ L2(Ωn, π⊗n). Then for any q > 1,

∥Tcq r f (x)∥q,r,x ≤ ∥ f (x)∥q,x

for x ∼ π⊗n, r ∼ {−1, 1}n. In other words, ∥ ‡Tcq f ∥q ≤ ∥ f ∥q. Here 0 < cq ≤ 1 is a
constant depending only on q; in particular we may take c4, c4/3 = 2
5 .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

304 10. Advanced hypercontractivity

Proof. In fact, we can show that for every outcome r = r ∈ {−1, 1}n we have

∥Tcq r f (x)∥q,x ≤ ∥ f (x)∥q,x

for sufﬁciently small cq > 0. Note that on the left-hand side we have

∥T1
±cq T
2
±cq · · · Tn
±cq f (x)∥q,x.

We know that Ti
ρ is a contraction in Lq for any ρ ≥ 0 (Exercise 8.11). Hence it
sufﬁces to show that Ti
−cq is a contraction in Lq, i.e., that

∥Ti
−cq g(x)∥q,x ≤ ∥g(x)∥q,x (10.21)

for all g ∈ L2(Ωn, π⊗n). Similar to the proof of Theorem 10.42, it sufﬁces to
show ∥T−cq h∥q ≤ ∥h∥q (10.22)

for all one-input functions h ∈ L2(Ω, π), because then (10.21) holds point-
wise for all outcomes of x1, . . . , xi−1, xi+1, . . . , xn. By Proposition 9.19, if we
prove (10.22) for some q, then the same constant cq works for the conjugate
Hölder index q′; thus we may restrict attention to q ≥ 2. Now the result
follows from Lemma 10.43 by taking a = h=; and X = h={1}(x). □

10.5. Highlight: General sharp threshold theorems

In Chapter 8.4 we described the problem of “threshold phenomena” for mono-
tone functions f : {−1, 1}n → {−1, 1}. As p increases from 0 to 1, we are inter-
ested in whether Prx∼π⊗n
p [ f (x) = −1] has a “sharp threshold”, jumping quickly
from near 0 to near 1 around the critical probability p = pc. The “sharp
threshold principle” tells us that this occurs (roughly speaking) if and only
if the total inﬂuence of f under its critical distribution, I[ f (pc)], is ω(1). (See
Exercise 8.28 for more precise statements.) This motivates ﬁnding a charac-
terization of functions with small total inﬂuence. Indeed, ﬁnding such a char-
acterization is a perfectly natural question even for not-necessarily-monotone
Boolean-valued functions f ∈ L2(Ωn, π⊗n).

For the usual uniform distribution on {−1, 1}n, Friedgut’s Junta Theorem
from Chapter 9.6 provides a very good characterization: f : {−1, 1}n → {−1, 1}
can only have O(1) total inﬂuence if it’s (close to) an O(1)-junta. By the
version of Friedgut’s Junta Theorem for general product spaces (Section 10.3),
the same holds for Boolean-valued f ∈ L2({−1, 1}n, π⊗n
p ) so long as p is not too
close to 0 or to 1. However, for p as small as 1/nΘ(1), the “junta”-size promised
by Friedgut’s Junta Theorem may be larger than n. (Cf. the breakdown of
Friedgut and Kalai’s sharp threshold result Theorem 10.29 for p ≤ 1/nΘ(1).)
This is a shame, as many natural graph properties for which we’d like to show
a sharp threshold – e.g., (non-)3-colorability – have p = 1/nΘ(1). At a technical
level, the reason for the breakdown for very small p is the dependence on the

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.5. Highlight: General sharp threshold theorems 305

“λ” parameter in the General Hypercontractivity Theorem. But there’s a more
fundamental reason for its failure, as suggested by the example at the end of
Section 10.3: Friedgut’s Junta Theorem simply isn’t true for such small p.

Example 10.45. Here are some examples of Friedgut’s Junta Theorem failing
for small p:

• The logical OR function ORn : {−1, 1}n → {−1, 1} has critical probabil-
ity pc ∼ ln 2
n , and its total inﬂuence at this probability is I[OR
(pc)
n ] ∼ 2 ln 2,
a small constant. Yet it’s easy to see that under the pc-biased distri-
bution, ORn is not even, say, .1-close to any junta on o(n) coordinates.
(That is, for every o(n)-junta h, Prx∼π⊗n
pc [ f (x) ̸= h(x)] > .1.)

• Consider the function f : {−1, 1}n → {−1, 1} that is True (−1) if and only
if there exists a “run” of three consecutive −1’s in its input. (We allow
runs to “wrap around”, thus making f a transitive-symmetric function.)
It’s not hard to show that the critical probability for this f satisﬁes pc =
Θ(1/n1/3). Furthermore, since f is a computable by a DNF of width 3,
Exercise 8.26(b) shows that I[ f (pc)] ≤ 12, a small constant. But again,
this f is not close to any o(n)-junta under the pc-biased distribution.
A similar example is Clique3 : {True,False}(v
2) → {True,False}, the graph
property of containing a triangle.

We see from these examples that for p very small, we can’t hope to show
that low-inﬂuence functions are close to juntas. However, these counterex-
ample functions still have low complexity in a weaker sense – they are com-
putable by narrow DNFs. Indeed, Friedgut [Fri99] suggests this as a charac-
terization:

Friedgut’s Conjecture. There is a function w : R + × (0, 1) → R + such that
the following holds: If f : {True,False}n → {True,False} is a monotone function,
0 < p ≤ 1/2, and I[ f (p)] ≤ K, then f is ϵ-close under π⊗n
p to a monotone DNF of
width at most w(K, ϵ).

The assumption of monotonicity is essential in this conjecture; see Exer-
cise 10.38.

Short of proving his conjecture, Friedgut managed to show:

Friedgut’s Sharp Threshold Theorem. The above conjecture holds when
f is a graph property.

This gives a very good characterization of monotone graph properties with
low total inﬂuence, one that works no matter how small p is. Friedgut also
extended his result to monotone hypergraph properties; this was sufﬁcient
for him to show that several interesting hypergraph (or hypergraph-like)
properties have sharp thresholds – for example, the property of a random

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

306 10. Advanced hypercontractivity

3-uniform hypergraph containing a perfect matching, or the property of a
random width-3 DNF formula being a tautology. (Interestingly, for neither
of these properties do we know precisely where the critical probability pc
is; nevertheless, we know there is a sharp threshold around it.) Roughly
speaking one needs to show that at the critical probability, these properties
can’t be well-approximated by narrow DNFs because they are almost surely
not determined just by “local” information about the (hyper)graph. This kind
of deduction takes some effort in random graph theory and we won’t discuss
it further here beyond Exercise 10.42; for a survey, see Friedgut [Fri05].

Friedgut’s proof is rather long and it relies heavily on the function being a
graph or hypergraph property. Following Friedgut’s work, Bourgain [Bou99]
gave a shorter proof of an alternative characterization. Bourgain’s characteri-
zation is not as strong as Friedgut’s for monotone graph properties; however,
it has the advantage that it works for low-inﬂuence functions on any product
probability space. (In particular, there is no monotonicity assumption since
the domain need not be {True,False}n.) We ﬁrst make a quick deﬁnition and
then state Bourgain’s theorem.

Deﬁnition 10.46. Let f ∈ L2(Ωn, π⊗n) be {−1, 1}-valued. For T ⊆ [n], y ∈ ΩT ,
and τ > 0, we say that the restriction yT is a τ-booster if f ⊆T (y) ≥ E[ f ] + τ.
(Recall that f ⊆T (y) = E[ fT|y].) In case τ < 0 we say that yT is a τ-booster if

f ⊆T (y) ≤ E[ f ] − |τ|.

Bourgain’s Sharp Threshold Theorem. Let f ∈ L2(Ωn, π⊗n) be {−1, 1}-
valued with I[ f ] ≤ K. Assume Var[ f ] ≥ .01. Then there is some τ (either
positive or negative) with |τ| ≥ exp(−O(K 2)) such that

Pr
x∼π⊗n[∃T ⊆ [n], |T| ≤ O(K) such that xT is a τ-booster] ≥ |τ|.

(We emphasize that here and throughout, the constants hidden in the O(·) are
absolute and do not depend on Ω or π.)

Thinking of K as an absolute constant, the above theorem says that for a
typical input string x, there is a large chance that it contains a constant-sized
substring that is an Ω(1)-booster for f . In the particular case of monotone
f ∈ L2({True,False}n, π⊗n
p ) with p small, it’s not hard to deduce (Exercise 10.40)
that in fact there exists a T with |T| ≤ O(K) such that restricting all coordi-
nates in T to be True increases Prπ⊗n
p [ f = True] by exp(−O(K 2)). This is a
qualitatively weaker conclusion than what you get from Friedgut’s Sharp
Threshold Theorem when f is a graph property with I[ f ] ≤ O(1) – in that case,
by taking T to be any of the width-O(1) terms in the approximating DNF one
can increase Prπ⊗n
p [ f = True] not just by Ω(1) but up to almost 1. Nevertheless,
Bourgain’s theorem apparently sufﬁces to deduce any of the sharp thresholds
results obtainable from Friedgut’s theorem [Fri05]. For a very high-level

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.5. Highlight: General sharp threshold theorems 307

sketch of how Bourgain’s theorem would apply in the case of 3-colorability of
random graphs, see Exercise 10.42.

The last part of this section will be devoted to proving Bourgain’s Sharp
Threshold Theorem. Before doing this, we add a remark. Hatami [Hat12] has
signiﬁcantly generalized Bourgain’s work, establishing the following charac-
terization of Boolean-valued functions with low total inﬂuence:

Hatami’s Theorem. Let f ∈ L2(Ωn, π⊗n) be a {−1, 1}-valued function with
I[ f ] ≤ K. Then for every ϵ > 0, the function f is ϵ-close (under π⊗n) to an
exp(O(K 3/ϵ3))-“pseudo-junta” h : Ωn → {−1, 1}.

The term “pseudo-junta” is deﬁned in Exercise 10.39. A K-pseudo-junta h
has the property that I[h] ≤ 4K; thus Hatami’s Theorem shows that having
O(1) total inﬂuence is essentially equivalent to being an O(1)-pseudo-junta.
A downside of the result, however, is that being a K-pseudo-junta is not a
“syntactic” property; it depends on the probability distribution π⊗n.

Let’s now turn to proving Bourgain’s Sharp Threshold Theorem. In fact,
Bourgain proved the theorem as a corollary of the following main result:

Theorem 10.47. Let (Ω, π) be a ﬁnite probability space and let f : Ωn → {−1, 1}.
Let 0 < ϵ < 1/2 and write k = I[ f ]/ϵ. Then for each x ∈ Ωn it’s possible to deﬁne
a set of “notable coordinates” Jx ⊆ [n] satisfying |Jx| ≤ exp(O(k)) such that

E
x∼π⊗n
 [ ∑

S̸∈Fx f =S(x)2]
 ≤ 2ϵ.

Here Fx = {S : S ⊆ Jx, |S| ≤ k}, a collection always satisfying |Fx| ≤ exp(O(k2)).

You may notice that this theorem looks extremely similar to Friedgut’s
Junta Theorem from Chapter 9.6 (and the exp(−O(I[ f ]2)) quantity in Bour-
gain’s Sharp Threshold Theorem looks similar to the Fourier coefﬁcient lower
bound in Corollary 9.32). Indeed, the only difference between Theorem 10.47
and Friedgut’s Junta Theorem is that in the latter, the “notable coordinates” J
can be “named in advance” – they’re simply the coordinates j with Inf j[ f ] =
∑S∋ j ̂f (S)2 large. By contrast, in Theorem 10.47 the notable coordinates de-
pend on the input x. As we will see in the proof, they are precisely the
coordinates j such that ∑S∋ j f =S(x)2 is large. Of course, in the setting of
f : {−1, 1}n → {−1, 1} we have f =S(x)2 = ̂f (S)2 for all x, so the two deﬁnitions
coincide. But in the general setting of f ∈ L2(Ωn, π⊗n) it makes sense that
we can’t name the notable coordinates in advance and rather have to “wait
until x is chosen”. For example, for the ORn function as in Example 10.45,
there are no notable coordinates to be named in advance, but once x is chosen
the few coordinates on which x takes the value True (if any exist) will be the
notable ones.
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

308 10. Advanced hypercontractivity

The proof of Theorem 10.47 mainly consists of adding the randomiza-
tion/symmetrization technique to the proof of Friedgut’s Junta Theorem (more
precisely, Theorem 9.28) to avoid dependence on the minimum probability of π.
This randomization/symmetrization is applied to what are essentially the key
inequalities in that proof:

∥T 1p
3 Li f ∥
2
2 ≤ ∥Li f ∥
2
4/3 = ∥Li f ∥
2/3
4/3 · ∥Li f ∥
4/3
4/3 ≤ ∥Li f ∥
2/3
4/3 · Infi[ f ].

(The last inequality here is Exercise 8.10(b).) The overall proof needs one
more minor twist: since we work on a “per-x” basis and not in expectation, it’s
possible that the set of notable coordinates can be improbably large. (Think
again about the example of ORn; for x ∼ π⊗n
1/n we expect only a constant number
of coordinates of x to be True, but it’s not always uniformly bounded.) This
is combated using the principle that low-degree functions are “reasonable”
(together with randomization/symmetrization).

Proof of Theorem 10.47. By the simple “Markov argument” (see Proposi-
tion 3.2) we have
E
x∼π⊗n
 [ ∑

|S|>k f =S(x)2]
 = ∑

|S|>k ∥ f =S∥
2
2 ≤ I[ f ]/k = ϵ.

Thus it sufﬁces to deﬁne the sets Jx so that

E
x∼π⊗n
 [ ∑

|S|≤k, S̸⊆Jx f =S(x)2]
 ≤ ϵ. (10.23)

We’ll ﬁrst deﬁne “notable coordinate” sets J′
x ⊆ [n] which almost do the trick:

J′
x =
 {
 j ∈ [n] : ∑

S∋ j f =S(x)2 ≥ τ
}
 , τ = c−k.

(where c > 1 is a universal constant). Using this deﬁnition, the main effort of
the proof will be to show
E
x∼π⊗n
 [ ∑

|S|≤k, S̸⊆J′
x f =S(x)
2]
 ≤ ϵ/2. (10.24)

This looks better than (10.23); the only problem is that the sets J′
x don’t always
satisfy |J′
x| ≤ exp(O(k)) as needed. However, “in expectation” |J′
x| ought not be
much larger than 1/τ = ck. Thus we introduce the event

“J′
x is too big” ⇐⇒ |J′
x| ≥ Ck

(where C > c is another universal constant) and deﬁne

Jx =
 {J′
x if J′
x is not too big,

; if J′
x is too big.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.5. Highlight: General sharp threshold theorems 309

The last part of the proof will be to show that

E
x∼π⊗n
 [
1[J′
x is too big] · ∑

0<|S|≤k f =S(x)
2]
 ≤ ϵ/2. (10.25)

Together, (10.25) and (10.24) establish (10.23). We will ﬁrst prove (10.24) and
then prove (10.25). As a small aside, we’ll see that for both inequalities we
could obtain a bound much less than ϵ/2 if desired.

To prove (10.24), we mimic the proof of Theorem 9.28 but add in random-
ization/symmetrization. The key step is encapsulated in the following lemma.
Note that the lemma also holds with the more natural deﬁnition g = Li f ; the
additional T 2
5 is to facilitate future “un-randomization/symmetrization”.

Lemma 10.48. Fix x ∈ Ωn and i ̸∈ J′
x. Then writing g = T 2
5 Li f we have

∥T 1p
3 ̃g|x∥
2
2 ≤ τ1/3∥ ̃g|x∥
4/3
4/3.

Proof. Here ̃g is the randomization/symmetrization of g, so ̃g|x = ̃g|x(r) is a
function on the uniform-distribution hypercube. Applying the basic (4/3, 2)-
Hypercontractivity Theorem we have

∥T 1p
3 ̃g|x∥
2
2 ≤ ∥ ̃g|x∥
2
4/3 = (∥ ̃g|x∥2
4/3)
1/3 · ∥ ̃g|x∥
4/3
4/3 ≤ (∥ ̃g|x∥
2
2)1/3 · ∥ ̃g|x∥4/3
4/3.

But by the usual Parseval Theorem,

∥ ̃g|x∥
2
2 = ∑

S⊆[n] g=S(x)
2 = ∑

S∋i(2/5)
2|S| f =S(x)
2 ≤ ∑

S∋i f =S(x)
2 ≤ τ,

the last inequality due to the assumption that i ̸∈ J′
x. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

310 10. Advanced hypercontractivity

We now establish (10.24):

E
x
 [ ∑

|S|≤k, S̸⊆J′
x f =S(x)
2]
 ≤ (5p
3/2)
2k · E
x
 [ ∑

S̸⊆J′
x(T 2
5
p
3 f =S)(x)
2]

≤ 20k · E
x
 [ ∑

i̸∈J′
x
 ∑

S∋i(T 2
5p
3 f =S)(x)2]

= 20k · E
x
 [ ∑

i̸∈J′
x ∥T 1p
3 ̃gi|x∥
2
2
]
 (for gi = T 2
5 Li f )

≤ 20kτ1/3 · E
x
 [ ∑

i̸∈J′
x ∥̃gi|x∥
4/3
4/3
]
 (Lemma 10.48)

≤ 20kτ1/3 · n∑

i=1 ∥Li f ∥
4/3
4/3 (Theorem 10.35)

≤ 20kτ1/3 · n∑

i=1 Infi[ f ] (Exercise 8.10(b))

= 20kτ1/3 · I[ f ] = (20c−1/3)kkϵ ≤ ϵ/2,

the last inequality because (20c−1/3)kk ≤ 1/2 for all k ≥ 0 once c is a large
enough constant.

The last task in the proof is to establish (10.25). Using Cauchy–Schwarz,

E
x∼π⊗n
 [
1[J′
x is too big] · ∑

0<|S|≤k f =S(x)
2]

≤ √
E
x [
1[J′
x is too big]2]
√
√
√
√E
x
 [
( ∑

0<|S|≤k f =S(x)2)2]

. (10.26)

For the ﬁrst factor on the right of (10.26) we use Markov’s inequality:

E
x [
1[J′
x is too big]
2] = Pr
x [J′
x is too big] = Pr
x [|J′
x| ≥ Ck]

≤ C−k E
x [|J′
x|] ≤ C−k E
x
 [( n∑

i=1
 ∑

S∋i f =S(x)2)/τ
]
 = C−k ck · I[ f ]. (10.27)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.5. Highlight: General sharp threshold theorems 311

As for the second factor on the right of (10.26), let’s write h = T 2
5 ( f − f =;). (We

are being slightly ﬁnicky about f =; just in case it’s very large.) Then

E
x
 [
( ∑

0<|S|≤k f =S(x)
2)2]
 ≤ (5/2)4k · E
x
 [( ∑

S̸=;
(T 2
5 f =S)(x)
2)2]

= (5/2)4k · E
x [
∥̃h|x∥
4
2]

≤ 40k · E
x [
∥̃h|x∥4
4]

≤ 40k · ∥ f − f =;∥
4
4 (Theorem 10.35)

≤ 40k · 2
2 E
x [( f − f =;)2] (since | f − f =;| ≤ 2 always)

= 4 · 40k · Var[ f ] ≤ 4 · 40k · I[ f ]. (10.28)

Substituting (10.27) and (10.28) into (10.26) gives

E
x∼π⊗n
 [
1[J′
x is too big] · ∑

0<|S|≤k f =S(x)
2]

≤ √C−k ck · 4 · 40k · I[ f ] = 2( 40c
C )k/2kϵ ≤ ϵ/2,

the last inequality again holding for all k ≥ 0 once C is chosen large enough
compared to c. □

We end this chapter by deducing Bourgain’s Sharp Threshold Theorem
from Theorem 10.47.

Proof of Bourgain’s Sharp Threshold Theorem. We take ϵ = .001 in The-
orem 10.47 and obtain the associated collections of subsets Fx, where each
|Fx| ≤ exp(O(K 2)) and each S ∈ Fx satisﬁes |S| ≤ O(K). Using the fact that
f =;(x)
2 = 1 − Var[ f ] ≤ .99 for each x we get

E
x∼π⊗n
 [ ∑

S∈Fx\{;} f =S(x)2]
 ≥ 1 − 2ϵ − .99 = .008.

We always have |Fx \ {;}| ≤ exp(O(K 2)), and there’s also no harm in assuming
|Fx \ {;}| > 0. It follows that

E
x∼π⊗n
 [ max
S∈Fx\{;}
{ f =S(x)
2}
] ≥ .008
exp(O(K 2)) = exp(−O(K 2)).

Thus for each x we can deﬁne a set Sx with 0 < |Sx| ≤ O(K) such that

E
x∼π⊗n
 [ f =Sx (x)2] ≥ exp(−O(K 2)). (10.29)

By Exercise 8.19 we have | f =Sx (x)| ≤ 2
|Sx| ≤ 2
O(K) and hence f =Sx (x)
2 ≤ exp(O(K))
always. It follows from (10.29) that we must have

Pr
x∼π⊗n
 [ f =Sx (x)
2 ≥ exp(−O(K 2))] ≥ exp(−O(K 2)).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

312 10. Advanced hypercontractivity

We will complete the proof by showing that whenever f =Sx (x)
2 ≥ exp(−O(K 2))
occurs, there exists T ⊆ Sx such that xT is a ± exp(−O(K 2))-booster for f . So
we either have a + exp(−O(K 2))-booster with probability at least 1
2 exp(−O(K 2)),
or a − exp(−O(K 2))-booster with probability at least 1
2 exp(−O(K 2)); either way,
the proof will be complete.

Assume then that f =Sx (x)2 ≥ exp(−O(K 2)); equivalently,

| f =Sx (x)| ≥ exp(−O(K 2)).

Let’s now work with g = f − E[ f ]. Of course g=T = f =T for all T ̸= ;; since
Sx ̸= ; the above inequality tells us that |g=Sx (x)| ≥ exp(−O(K 2)). Recall the
formula
 g=Sx (x) = ∑

;̸=T⊆Sx(−1)
|Sx|−|T| g⊆T (x);

we dropped the T = ; term since it’s 0. As there are only 2
|Sx| − 1 = exp(O(K))
terms in the above sum, we deduce there must exist some T ⊆ Sx with 0 <
|T| ≤ O(K) such that

|g⊆T (x)| ≥ exp(−O(K 2))/ exp(O(K)) = exp(−O(K 2)).

But g⊆T = f ⊆T − E[ f ], so the above gives us | f ⊆T (x) − E[ f ]| ≥ exp(−O(K 2)).
This precisely says that xT is a ± exp(−O(K 2))-booster, as desired. □

For a relaxation of the assumption Var[ f ] ≥ .01 in this theorem, see Exer-
cise 10.41.

10.6. Exercises and notes

10.1 Let X be a random variable and let 1 ≤ r ≤ ∞. Recall that the triangle
(Minkowski) inequality implies that for real-valued functions f1, f2,

∥ f1(X ) + f2(X )∥r ≤ ∥ f1(X )∥r + ∥ f2(X )∥r.

More generally, if w1, . . . , wm are nonnegative reals f1, . . . , f m are real func-
tions, then

∥w1 f1(X ) + · · · + wm f m(X )∥r ≤ w1∥ f1(X )∥r + · · · + wm∥ f m(X )∥r.

Still more generally, if Y is a random variable independent of X and
f (X , Y ) is a (measurable) real-valued function, then it holds that
∥
∥E
Y [ f (X , Y )]
∥
∥r,X ≤ E
Y [∥ f (X , Y )∥r,X ].

Using this last fact, show that whenever 0 < p ≤ q ≤ ∞,
∥
∥ ∥ f (X , Y )∥p,Y ∥
∥q,X ≤ ∥
∥ ∥ f (X , Y )∥q,X ∥
∥p,Y .

(Hint: Raise the inequality to the power of p and use r = q/p.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 313

10.2 The goal of this exercise is to prove Proposition 9.15: If X and Y are
independent (p, q, ρ)-hypercontractive random variables, then so is X +Y .
Let a, b ∈ R .
(a) First obtain

∥a + ρb(X + Y )∥q,X ,Y ≤ ∥
∥ ∥a + ρbX + bY ∥p,Y ∥
∥q,X .

(b) Next, upper-bound this by
∥
∥ ∥a + bY + ρbX ∥q,X ∥
∥p,Y .

(Hint: Exercise 10.1.)
(c) Finally, upper-bound this by
∥
∥ ∥a + bY + bX ∥p,X ∥
∥p,Y = ∥a + b(X + Y )∥p,X ,Y .

10.3 Let X 1, . . . , X n be independent (p, q, ρ)-hypercontractive random variables.
Let F(x) = ∑S⊆[n] ̂F(S)xS be an n-variate multilinear polynomial. Deﬁne
formally the multilinear polynomial Tρ F(x) = ∑S⊆[n] ρ|S| ̂F(S)xS. The goal
of this exercise is to show

∥Tρ F(X 1, . . . , X n)∥q ≤ ∥F(X 1, . . . , X n)∥p. (10.30)

Note that this result yields an alternative deduction of the Hypercontrac-
tivity Theorem for ±1 bits from the Two-Point Inequality. A (notationally
intense) generalization of this exercise can also be used as an alternative
inductive strategy for deducing the General Hypercontractivity Theorem
from Proposition 10.17 or Theorem 10.18.
(a) Why is Exercise 10.2 a special case of (10.30)?
(b) Begin the inductive proof of (10.30) by showing that the base case
n = 0 is trivial.
(c) For the case of general n, ﬁrst establish

∥Tρ F(X )∥q ≤ ∥
∥
∥ ∥T′
ρ E(X ′) + X nT′
ρ D(X ′)∥p,X n ∥
∥
∥q,X ′ ,

where we are using the notation x′ = (x1, . . . , xn−1), F(x) = E(x′) +
xnD(x′), and T′
ρ for the operator acting formally on (n − 1)-variate
multilinear polynomials.
(d) Complete the inductive step, using steps similar to Exercises 10.2(b),(c).
(Hint: For X n a real constant, why is T′
ρ E(X ′) + X nT′
ρ D(X ′) = T′
ρ(E +
X nD)(X ′)?)

10.4 This exercise is concerned with the possibility of a converse for Proposi-
tion 10.8.
(a) In our proof of the Two-Point Inequality we used Proposition 9.19 to
deduce that a uniform bit x ∼ {−1, 1} is (p, q, ρ)-hypercontractivity if
it’s (q′, p′, ρ)-hypercontractive. Why can’t we use Proposition 9.19 to
deduce this for a general random variable X ?

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

314 10. Advanced hypercontractivity

(b) For each 1 < p < 2, exhibit a random variable X that is (p, 2, ρ)-
hypercontractive (for some ρ) but not (2, p′, ρ)-hypercontractive.

10.5 (a) Regarding Remark 10.2, heuristically justify (in the manner of Exer-
cise 9.24(a)) the following statement: If A, B ⊆ {−1, 1}n are concentric
Hamming balls with volumes exp(− a2
2 ) and exp(− b2
2 ) and ρa ≤ b ≤ a
(where 0 < ρ < 1), then

Pr
(x,y)
ρ-correlated

[x ∈ A, y ∈ B] ⪆ exp (− 1
2 a2−2ρab+b2

1−ρ2 ) ;

and further, if b < ρa, then Pr[x ∈ A, y ∈ B] ∼ Pr[x ∈ A]. Here you
should treat ρ as ﬁxed and a, b → ∞.
(b) Similarly, heuristically justify that the Reverse Small-Set Expansion
Theorem is essentially sharp by considering diametrically opposed
Hamming balls.

10.6 The goal of this exercise (and Exercise 10.7) is to prove the Reverse Hy-
percontractivity Theorem and its equivalent Two-Function version:

Reverse Hypercontractivity Theorem. Let f : {−1, 1}n → R ≥0 be a
nonnegative function and let −∞ ≤ q < p ≤ 1. Then ∥Tρ f ∥q ≥ ∥ f ∥p for
0 ≤ ρ ≤ √(1 − p)/(1 − q).

Reverse Two-Function Hypercontractivity Theorem. Let
f , g : {−1, 1}n → R ≥0 be nonnegative, let r, s ≤ 0, and assume 0 ≤ ρ ≤ prs ≤
1. Then
 E
(x,y)
ρ-correlated

[ f (x)g(y)] ≥ ∥ f ∥1+r∥g∥1+s.

Recall that for −∞ < p < 0 and for positive functions f ∈ L2(Ω, π) the
“norm” ∥ f ∥p retains the deﬁnition E[ f p]
−1/p. (The cases of p = −∞, p = 0,
and nonnegative functions are deﬁned by appropriate limits; in particular
∥ f ∥−∞ is the minimum of f ’s values, ∥ f ∥0 is the geometric mean of f ’s
values, and ∥ f ∥p is 0 whenever f is not everywhere positive. We also
deﬁne p′ by 1
p + 1
p′ = 1, with 0
′ = 0.)
The Reverse Two-Function Hypercontractivity Theorem can be thought
of as a generalization of the lesser known “reverse Hölder inequality” in
the setting of L2({−1, 1}n, π⊗n
1/2):

Reverse Hölder inequality. Let f ∈ L2(Ω, π) be a positive function. Then
for any p < 1,
 ∥ f ∥p = inf {E[ f g] : g > 0, ∥g∥p′ = 1}.

In particular, for r < 0 and f , g > 0 we have E[ f g] ≥ ∥ f ∥1+r∥g∥1+1/r.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 315

(a) Show that to prove these two Reverse Hypercontractivity Theorems it
sufﬁces to consider the case of f , g : {−1, 1}n → R +, i.e., strictly positive
functions.
(b) Show that the Reverse Two-Function Hypercontractivity Theorem is
equivalent (via the reverse Hölder inequality) to the Reverse Hyper-
contractivity Theorem.
(c) Reduce the Reverse Two-Function Hypercontractivity Theorem to the
n = 1 case. (Hint: Virtually identical to the Two-Function Hypercon-
tractivity Induction.) Further reduce to following:

Reverse Two-Point Inequality. Let −∞ ≤ q < p ≤ 1 and let 0 ≤ ρ ≤√(1 − p)/(1 − q). Then ∥Tρ f ∥q ≥ ∥ f ∥p for any f : {−1, 1} → R +.

10.7 The goal of this exercise is to prove the Reverse Two-Point Inequality.
(a) Similar to the non-reverse case, the main effort is proving the inequal-
ity assuming that 0 < q < p ≤ 1 and that ρ = √(1 − p)/(1 − q). Do this
by mimicking the proof of the Two-Point Inequality. (Hint: You will
need the inequality (1+ t)
θ ≥ 1+θt for θ ≥ 1, and you will need to show
that j−r
p
1−r is an increasing function of r on [0, 1) for all j ≥ 2.)

(b) Extend to the case of 0 ≤ ρ ≤ √
(1 − p)/(1 − q). (Hint: Use the fact that
for any f : {−1, 1}n → R ≥0 and −∞ ≤ p ≤ q ≤ ∞ we have ∥ f ∥p ≤ ∥ f ∥q.
You can prove this generalization of Exercise 1.13 by reducing to the
case of negative p and q to the case of positive p and q.)
(c) Establish the q = −∞ case of the Reverse Two-Point Inequality.
(d) Show that the cases −∞ < q < p < 0 follow by “duality”. (Hint: Like
Proposition 9.19 but with the reverse Hölder inequality.)
(e) Show that the cases q < 0 < p follow by the semigroup property of Tρ.
(f ) Finally, treat the cases of p = 0 or q = 0.

10.8 Give a simple proof of the n = 1 case of the Reverse Two-Function Hyper-
contractivity Theorem when r = s = −1/2. (Hint: Replace f and g by f 2

and g2; then you don’t even need to assume f and g are nonnegative.)
Can you also give a simple proof when r = s = −1 + 1/k for integers k > 2?

10.9 By selecting “r” = −ρ ρa+b
a+ρb and “s” = −ρ a+ρb
ρa+b , prove the Reverse Small-
Set Expansion Theorem mentioned in Remark 10.3. (Hint: The negative
norm of a 0-1-indicator is 0, so be sure to verify no negative norms arise.)

10.10 Let g ∈ L2(Ωn, π⊗n). Writing x = (x1, x′), where x′ = (x2, . . . , xn), carefully
justify the following identity of one-input functions: (T1
ρ g)|x′ = Tρ(g|x′).
(Hint: You may want to refer to Exercise 8.21.)

10.11 Prove Proposition 10.12.

10.12 Let X be a random variable and let Y denote its symmetrization X − X ′,
where X ′ is an independent copy of X . Show for any t, θ ∈ R that Pr[|Y | ≥
t] ≤ 2 Pr[|X − θ| ≥ t/2].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

316 10. Advanced hypercontractivity

10.13 The goal of this exercise is to establish Lemma 10.43.
(a) Show that we may take c2 = 1 (and that equality holds). Henceforth
assume q > 2.
(b) By following the idea of our q = 4 proof, reduce to showing that there
exists 0 < cq < 1 such that

|1 − cq x|q + cq qx − 1 ≤ |1 + x|q − qx − 1 ∀x ∈ R .

(c) Further reduce to showing there exists 0 < cq < 1 such that

|1 − cq x|q + cq qx − 1

x2 ≤ |1 + x|q − qx − 1
x2 ∀x ∈ R . (10.31)

Here you should also establish that both sides are continuous func-
tions of x ∈ R once the value at x = 0 is deﬁned appropriately.
(d) Show that there exists M > 0 such that for every 0 < cq < 1
2 , inequal-
ity (10.31) holds once |x| ≥ M. (Hint: Consider the limit of both sides
as |x| → ∞.)
(e) Argue that it sufﬁces to show that

|1 + x|q − qx − 1
x2 ≥ η (10.32)

for some universal positive constant η > 0. (Hint: A uniform continu-
ity argument for (x, cq) ∈ [−M, M] × [0, 1
2 ].)
(f ) Establish (10.32). (Hint: The best possible η is 1, but to just achieve
some positive η, argue using Bernoulli’s inequality that |1+x|q−qx−1
x2 is
everywhere positive and then observe that it tends to ∞ as |x| → ∞.)
(g) Possibly using a different argument, what is the best asymptotic
bound you can achieve for cq? Is cq ≥ Ω( log q
q ) possible?

10.14 Show that the largest c for which inequality (10.20) holds is the smaller
real root of c4 − 2c3 − 2c + 1 = 0, namely, c ≈ .435.

10.15 (a) Show that 1 + 6c2x2 + c4x4 ≤ 1 + 6x2 + 4x3 + x4 holds for all x ∈ R when
c = 1/2. (Can you also establish it for c ≈ .5269?)
(b) Show that if X is a random variable satisfying E[X ] = 0 and ∥X ∥4 <
∞, then ∥a + 1
2 r X ∥4 ≤ ∥a + X ∥4 for all a ∈ R , where r ∼ {−1, 1} is a
uniformly random bit independent of X . (Cf. Lemma 10.15.)
(c) Establish the following improvement of Theorem 10.44 in the case of
q = 4: for all f ∈ L2(Ωn, π⊗n),

∥T 1
2 r f (x)∥4,r,x ≤ ∥ f (x)∥4,x

(where x ∼ π⊗n, r ∼ {−1, 1}n).

10.16 Complete the proof of Theorem 10.39. (Hint: You’ll need to rework Exer-
cise 9.8 as in Lemma 10.38.)

10.17 Prove Proposition 10.17.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 317

10.18 Recall from (10.5) the function ρ = ρ(λ) deﬁned for λ ∈ (0, 1/2) (and ﬁxed
q > 2) by
 ρ = ρ(λ) =
 √ exp(u/q) − exp(−u/q)
exp(u/q′) − exp(−u/q′) =
 √ sinh(u/q)
sinh(u/q′) ,

where u = u(λ) is deﬁned by exp(−u) = λ
1−λ .
(a) Show that ρ is an increasing function of λ. (Hint: One route is to
reduce to showing that ρ2 is a decreasing function of u ∈ (0, ∞), reduce
to showing that q tanh(u/q) is an increasing function of q ∈ (1, ∞),
reduce to showing tanh r
r is a decreasing function of r ∈ (0, ∞), and
reduce to showing sinh(2r) ≥ 2r.)
(b) Verify the following statements from Remark 10.19:

for ﬁxed q and λ → 1/2, ρ → 1
√q − 1 ;

for ﬁxed q and λ → 0, ρ ∼ λ
1/2−1/q.

Also show:

for ﬁxed λ and q → ∞, ρ ∼ √ u
sinh u
 √ 1
q ,

and √ u
sinh u ∼ p
2λ ln(1/λ) for λ → 0.

(c) Show that ρ ≥ 1pq−1 λ
1/2−1/q holds for all λ.

10.19 Let (Ω, π) be a ﬁnite probability space, |Ω| ≥ 2, in which every outcome
has probability at least λ. Let 1 < p < 2 and 0 < ρ < 1. The goal of this
exercise is to prove the result of Wolff [Wol07] that, subject to ∥Tρ f ∥2 = 1,
every f ∈ L2(Ω, π) that minimizes ∥ f ∥p takes on at most two values (and
there is at least one minimizing f ).
(a) We consider the equivalent problem of minimizing F( f ) = ∥ f ∥p
p subject
to G( f ) = ∥Tρ f ∥2
2 = 1. Show that both F( f ) and G( f ) are C 1 function-
als (identifying functions f with points in R Ω).
(b) Argue from continuity that the minimum value for ∥ f ∥p
p subject to
∥Tρ f ∥2
2 = 1 is attained. Henceforth write f0 to denote any minimizer;
the goal is to show that f0 takes on at most two values.
(c) Show that f0 is either everywhere nonnegative or everywhere nonpos-
itive. (Hint: By homogeneity our problem is equivalent to maximizing
∥Tρ f ∥2 subject to ∥ f ∥p = 1; now use Exercise 2.34.) Replacing f0 by
| f0| if necessary, henceforth assume f0 is nonnegative.
(d) Show that ∇F( f0) = π · p f p−1
0 and ∇G( f0) = π · 2Tρ2 f0. Here π · g signi-
ﬁes the pointwise product of functions on Ω, with π thought of as a
function Ω → R ≥0. (Hint: For the latter, write G( f ) = 〈Tρ2 f , f 〉.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

318 10. Advanced hypercontractivity

(e) Use the method of Lagrange Multipliers to show that c f p−1
0 = Tρ2 f0
for some c ∈ R +. (Hint: You’ll need to note that ∇G( f0) ̸= 0.)
(f ) Writing µ = E[ f0], argue that each value y = f (ω) satisﬁes the equa-
tion
 c yp−1 = ρ2 y + (1 − ρ2)µ. (10.33)

(g) Show that (10.33) has at most two solutions for y ∈ R +, thereby com-
pleting the proof that f0 takes on at most two values. (Hint: Strict
concavity of yp−1.)
(h) Suppose q > 2. By slightly modifying the above argument, show that
subject to ∥g∥2 = 1, every g ∈ L2(Ω, π) that maximizes ∥Tρ g∥q takes
on at most two values (and there is at least one maximizing g). (Hint:
At some point you might want to make the substitution g = Tρ f ; note
that g is two-valued if f is.)

10.20 Fix 1 < p < 2 and 0 < λ < 1/2. Let Ω = {−1, 1} and π = πλ, meaning π(−1) =
λ, π(1) = 1 − λ. The goal of this exercise is to show the result of Latała
and Oleszkiewicz [LO00]: the largest value of ρ for which ∥Tρ f ∥2 ≤ ∥ f ∥p
holds for all f ∈ L2(Ω, π) is as given in Theorem 10.18; i.e., it satisﬁes

ρ2 = r∗ = exp(u/p′) − exp(−u/p′)
exp(u/p) − exp(−u/p) , (10.34)

where u is deﬁned by exp(−u) = λ
1−λ . (Here we are using p = q′ to facili-
tate the proof; we get the (2, q)-hypercontractivity statement by Proposi-
tion 9.19.)
(a) Let’s introduce the notation α = λ
1/p, β = (1 − λ)
1/p. Show that

r∗ = αpβ
2−p − α
2−pβp

α2 − β2 .

(b) Let f ∈ L2(Ω, π). Write µ = E[ f ] and δ = D1 f = ˆf (1). Our goal will be
to show
 µ2 + δ2r∗ = ∥Tpr∗ f ∥
2
2 ≤ ∥ f ∥
2
p. (10.35)

In the course of doing this, we’ll also exhibit a nonconstant function f
that makes the above inequality sharp. Why does this establish that
no larger value of ρ is possible?
(c) Show that without loss of generality we may assume

f (−1) = 1 + y

α , f (1) = 1 − y

β

for some −1 < y < 1. (Hint: First use Exercise 2.34 and a continuity
argument to show that we may assume f > 0; then use homogeneity
of (10.35).)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 319

(d) The left-hand side of (10.35) is now a quadratic function of y. Show
that our r∗ is precisely such that

LHS(10.35) = A y2 + C

for some constants A, C; i.e., r∗ makes the linear term in y drop
out. (Hint: Work exclusively with the α, β notation and recall from
Deﬁnition 8.44 that δ2 = λ(1 − λ)( f (1) − f (−1))
2 = αpβp( f (1) − f (−1))
2.)
(e) Compute that
 A = 2 βp−1 − αp−1

β − α . (10.36)

(Hint: You’ll want to multiply the above expression by αp + βp = 1.)
(f ) Show that
 RHS(10.35) = ((1 + y)p + (1 − y)p)
2/p.

Why does it now sufﬁce to show (10.35) just for 0 ≤ y < 1?
(g) Let y
∗ = β−α
β+α > 0. Show that if y = −y∗, then f is a constant function

and both sides of (10.35) are equal to 4
(α+β)2 .

(h) Deduce that both sides of (10.35) are equal to 4
(α+β)2 for y = y
∗. Verify
that after scaling, this yields the following nonconstant function for
which (10.35) is sharp: f (x) = exp(−xu/p).
(i) Write y = pz for 0 ≤ z < 1. By now we have reduced to showing

Az + C ≤ ((1 + pz)p + (1 − pz)p)
2/p,

knowing that both sides are equal when pz = y∗. Calling the expres-
sion on the right φ(z), show that

d
dz φ(z)
∣
∣
∣pz=y∗ = A.

(Hint: You’ll need αp + βp = 1, as well as the fact from part (h) that
φ(z) = 4
(α+β)2 when pz = y∗.) Deduce that we can complete the proof
by showing that φ(z) is convex for z ∈ [0, 1).
(j) Show that φ is indeed convex on [0, 1) by showing that its derivative
is a nondecreasing function of z. (Hint: Use the Generalized Binomial
Theorem as well as 1 < p < 2 to show that (1 + pz)p + (1 − pz)p is
expressible as ∑∞
j=0 b j z j where each b j is positive.)

10.21 Complete the proof of Theorem 10.18. (Hint: Besides Exercises 10.19
and 10.20, you’ll also need Exercise 10.18(a).)

10.22 (a) Let Φ : [0, ∞) → R be deﬁned by Φ(x) = x ln x, where we take 0 ln 0 = 0.
Verify that Φ is a smooth, strictly convex function.
(b) Consider the following:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

320 10. Advanced hypercontractivity

Deﬁnition 10.49. Let g ∈ L2(Ω, π) be a nonnegative function. The
entropy of g is deﬁned by

Ent[g] = E
x∼π[Φ(g(x))] − Φ( E
x∼π[g(x)]
).

Verify that Ent[g] ≥ 0 always, that Ent[g] = 0 if and only if g is
constant, and that Ent[c g] = cEnt[g] for any constant c ≥ 0.
(c) Suppose ϕ is a probability density on {−1, 1}n (recall Deﬁnition 1.20).
Show that Ent[ϕ] = DKL(ϕ ∥ π⊗n
1/2), the Kullback–Leibler divergence of
the uniform distribution from ϕ (more precisely, the distribution with
density ϕ).

10.23 The goal of this exercise is to establish:

The Log-Sobolev Inequality. Let f : {−1, 1}n → R . Then 1
2 Ent[ f 2] ≤ I[ f ].

(a) Writing ρ = e−t, the (p, 2)-Hypercontractivity Theorem tells us that

∥Te−t f ∥
2
2 ≤ ∥ f ∥
2
1+exp(−2t)

for all t ≥ 0. Denote the left- and right-hand sides as LHS(t), RHS(t).
Verify that these are smooth functions of t ∈ [0, ∞) and that LHS(0) =
RHS(0). Deduce that LHS
′(0) ≤ RHS
′(0).
(b) Compute LHS
′(0) = −2I[ f ]. (Hint: Pass through the Fourier represen-
tation; cf. Exercise 2.18.)
(c) Compute RHS
′(0) = −Ent[ f 2], thereby deducing the Log-Sobolev In-
equality. (Hint: As an intermediate step, deﬁne F(t) = E[| f |1+exp(−2t)]
and show that RHS
′(0) = F(0) ln F(0) + F ′(0).)

10.24 (a) Let f : {−1, 1}n → R . Show that Ent[(1 + ϵ f )
2] ∼ 2 Var[ f ]ϵ2 as ϵ → 0.
(b) Deduce the Poincaré Inequality for f from the Log-Sobolev Inequality.

10.25 (a) Deduce from the Log-Sobolev Inequality that for f : {−1, 1}n → {−1, 1}
with α = min{Pr[ f = 1], Pr[ f = −1]},

2α ln(1/α) ≤ I[ f ]. (10.37)

This is off by a factor of ln 2 from the optimal edge-isoperimetric in-
equality Theorem 2.39. (Hint: Apply the inequality to either 1
2 − 1
2 f
or 1
2 + 1
2 f .)
(b) Give a more streamlined direct derivation of (10.37) by differentiating
the Small-Set Expansion Theorem.

10.26 This exercise gives a direct proof of the Log-Sobolev Inequality.
(a) The ﬁrst step is to establish the n = 1 case. Toward this, show that we
may assume f : {−1, 1} → R is nonnegative and has mean 1. (Hints:
Exercise 2.14, Exercise 10.22(b).)
(b) Thus it remains to establish 1
2 Ent[(1 + bx)
2] ≤ b2 for b ∈ [−1, 1]. Show
that g(b) = b2− 1
2 Ent[(1+bx)
2] is smooth on [−1, 1] and satisﬁes g(0) =

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 321

0, g′(0) = 0, and g′′(b) = 2b2

1+b2 + ln 1+b2

1−b2 ≥ 0 for b ∈ (−1, 1). Explain why
this completes the proof of the n = 1 case of the Log-Sobolev Inequality.
(c) Show that for any two functions f+, f− : {−1, 1}n → R ,
( p
E[ f 2
+]−
p
E[ f 2
−]
2
 )2 ≤ E [( f+− f−
2
 )2] .

(Hint: The triangle inequality for ∥ · ∥2.)
(d) Prove the Log-Sobolev Inequality via “induction by restrictions” (as
described in Section 9.4). (Hint: For the right-hand side, establish
Inf[ f ] = E[( f+− f−
2 )2] + 1
2 I[ f+] + 1
2 I[ f−]. For the left-hand side, apply
induction, then the n = 1 base case, then part (c).)

10.27 (a) By following the strategy of Exercise 10.23, establish the following:

Log-Sobolev Inequality for general product space domains.
Let f ∈ L2(Ωn, π⊗n) and write λ = min(π), λ
′ = 1 − λ, exp(−u) = λ
λ′ .
Then 1
2 ϱEnt[ f 2] ≤ I[ f ], where

ϱ = ϱ(λ) = tanh(u/2)
u/2 = 2 λ
′ − λ
ln λ′ − ln λ .

(b) Show that ϱ(λ) ∼ 2/ ln(1/λ)) as λ → 0.
(c) Let f : {−1, 1}n → {−1, 1} and treat {−1, 1}n as having the p-biased
distribution π⊗n
p . Write q = 1 − p. Show that if α = min{Prπp [ f =
1], Prπp [ f = −1]}, then

4 q − p
ln q − ln p α ln(1/α) ≤ I[ f (p)]

and hence, for p → 0,

α logp α ≤ (1 + o p(1))p · E
x∼π⊗n
p [sens f (x)]. (10.38)

We remark that (10.38) is known to hold without the o p(1) for all
p ≤ 1/2.

10.28 Prove Theorem 10.21. (Hint: Recall Proposition 8.28.)

10.29 Let X 1, . . . , X n be independent (2, q, ρ)-hypercontractive random variables
and let F(x) = ∑
|S|≤k ̂F(S) xS be an n-variate multilinear polynomial of
degree at most k. Show that

∥F(X 1, . . . , X n)∥q ≤ (1/ρ)k∥F(X 1, . . . , X n)∥2.

(Hint: You’ll need Exercise 10.3.)

10.30 Let 0 < λ ≤ 1/2 and let (Ω, π) be a ﬁnite probability space in which some
outcome ω0 ∈ Ω has π(ω0) = λ. (For example, Ω = {−1, 1}, π = πλ.) Deﬁne
f ∈ L2(Ω, π) by setting f (ω0) = 1, f (ω) = 0 for ω ̸= ω0. For q ≥ 2, com-
pute ∥ f ∥q/∥ f ∥2 and deduce (in light of the proof of Theorem 10.21) that
Corollary 10.20 cannot hold for ρ > λ
1/2−1/q.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

322 10. Advanced hypercontractivity

10.31 Prove Theorem 10.22.

10.32 Prove Theorem 10.23.

10.33 Prove Theorem 10.24. (Hint: Immediately worsen q−1 to q so that ﬁnding
the optimal choice of q is easier.)

10.34 Prove Theorem 10.25.

10.35 Prove Friedgut’s Junta Theorem for general product spaces as stated in
Section 10.3.

10.36 Show that (10.9) implies F(pc + ηpc) ≥ 1 − ϵ in the proof of Theorem 10.29.
(Hint: Consider d
d p ln(1 − F(p)).)

10.37 Justify the various calculations and observations in Example 10.45.

10.38 (a) Let p = 1
n and let f ∈ L2({−1, 1}n, π⊗n
p ) be any Boolean-valued function.
Show that I[ f ] ≤ 4. (Hint: Proposition 8.45.)
(b) Let us specialize to the case f = χ[n]. Show that f is not .1-close
to any width-O(1) DNF (under the 1
n -biased distribution, for n sufﬁ-
ciently large). This shows that the assumption of monotonicity can’t
be removed from Friedgut’s Conjecture. (Hint: Show that ﬁxing any
constant number of coordinates cannot change the bias of χ[n] very
much.)

10.39 A function h : Ωn → Σ is said to expressed as a pseudo-junta if the follow-
ing hold: There are “juntas” f1, . . . , f m : Ωn → {True,False} with domains
J1, . . . , Jm ⊆ [n] respectively. Further, g : (Ω ∪ {∗})n → Σ, where ∗ is a new
symbol not in Ω. Finally, for each input x ∈ Ωn we have h(x) = g(y), where
for j ∈ [n],
 yj =
 {x j if j ∈ Ji for some i with f i(x) = True,

∗ else.

An alternative explanation is that on input x, the junta f i decides whether
the coordinates in its domain are “notable”; then, h(x) must be determined
based only on the set of all notable coordinates. Finally, if π is a distribu-
tion on Ω, we say that the pseudo-junta has width-k under π⊗n if

E
x∼π⊗n[#{ j : y j ̸= ∗}] ≤ k;

in other words, the expected number of notable coordinates is at most k.
For h ∈ L2(Ωn, π⊗n) we simply say that h is a k-pseudo-junta. Show that
if such a k-pseudo-junta h is {−1, 1}-valued, then I[ f ] ≤ 4k. (Hint: Re-
ferring to the second statement in Proposition 8.24, consider the notable
coordinates for both x and x′ = (xi, . . . , xi−1, x′
i, xi+1, . . . , xn).)

10.40 Establish the following further consequence of Bourgain’s Sharp Thresh-
old Theorem: Let f : {True,False}n → {True,False} be a monotone function
with I[ f (p)] ≤ K. Assume Var[ f ] ≥ .01 and 0 < p ≤ exp(−cK 2), where c is a

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 323

large universal constant. Then there exists T ⊆ [n] with |T| ≤ O(K) such
that

Pr
x∼π⊗n
p [ f (x) = True | xi = True for all i ∈ T] ≥ Pr
x∼π⊗n
p [ f (x) = True] + exp(−O(K 2)).

(Hint: Bourgain’s Sharp Threshold Theorem yields a booster either to-
ward True or toward False. In the former case you’re easily done; to rule
out the latter case, use the fact that p|T| ≪ exp(−O(K 2)).)

10.41 Suppose that in Bourgain’s Sharp Threshold Theorem we drop the as-
sumption that Var[ f ] ≥ .01. (Assume at least that f is nonconstant.)
Show that there is some τ with |τ| ≥ stddev[ f ] · exp(−O(I[ f ]2/ Var[ f ]2))
such that

Pr
x∼π⊗n[∃T ⊆ [n], |T| ≤ O(I[ f ]/ Var[ f ]) such that xT is a τ-booster] ≥ |τ|.

(Cf. Exercise 9.32.)

10.42 In this exercise we give the beginnings of the idea of how Bourgain’s Sharp
Threshold Theorem can be used to show sharp thresholds for interesting
monotone properties. We will consider ¬3Col, the property of a random
v-vertex graph G ∼ G (v, p) being non-3-colorable.
(a) Prove that the critical probability pc satisﬁes pc ≤ O(1/v); i.e., estab-
lish that there is a universal constant C such that

Pr[G ∼ G (v, C/v) is 3-colorable] = on(1).

(Hint: Union-bound over all potential 3-colorings.)
(b) Toward showing (non-)3-colorability has a sharp threshold, suppose
the property had constant total inﬂuence at the critical probability.
Bourgain’s Sharp Threshold Theorem would imply that there is a τ
of constant magnitude such that for G ∼ G (v, pc), there is a |τ| chance
that G contains a τ-boosting induced subgraph GT . There are two
cases, depending on the sign of τ. It’s easy to rule out that the boost
is in favor of 3-colorability; the absence of a few edges shouldn’t in-
crease the probability of 3-colorability by much (cf. Exercise 10.40).
On the other hand, it might seem plausible that the presence of a
certain constant number of edges chould boost the probability of non-
3-colorability by a lot. For example, the presence of a 4-clique imme-
diately boosts the probability to 1. However, the point is that at the
critical probability it is very unlikely that G contains a 4-clique (or in-
deed, any “local” witness to non-3-colorability). Short of showing this,
prove at least that the expected number of 4-cliques in G ∼ G (v, p) is
ov(1) unless p = Ω(v−2/3) ≫ pc.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

324 10. Advanced hypercontractivity

Notes. As mentioned, the standard template introduced by Bonami [Bon70]
for proving the Hypercontractivity Theorem for ±1 bits is to ﬁrst prove the
Two-Point Inequality, and then do the induction described in Exercise 10.3.
Bonami’s original proof of the Two-Point Inequality reduced to the 1 ≤ p < q ≤
2 case as we did, but then her calculus was a little more cumbersome. We fol-
lowed the proof of the Two-Point Inequality appearing in Janson [Jan97]. An-
other approach to proving the Hypercontractivity Theorem is to derive it from
the Log-Sobolev Inequality (Exercise 10.23), as was done by Gross [Gro75].

Our use of two-function hypercontractivity theorems to facilitate an in-
ductive proof (and avoid the use of Exercise 10.1) follows the communica-
tion/coding theory viewpoint of Ahlswede and Gács [AG76]. (We were also
inspired by Mossel et al. [MOR
+06], Barak et al. [BBH
+12], and Kauers
et al. [KOTZ16].) Ahlswede and Gács established the close connection be-
tween hypercontractivity and small-set expansion in general product spaces,
and independently obtained the sharp Hypercontractivity Theorem for ±1
bits, relying in part on a result of Witsenhausen [Wit75].

Our statement of the Generalized Small-Set Expansion Theorem is mod-
eled after the almost identical Reverse Small-Set Expansion Theorem, ﬁrst
proved by Mossel et al. [MOR
+06]. The Reverse Hypercontractivity Inequal-
ity itself is due to Borell [Bor82]; the presentation in Exercises 10.6–10.9
follows Mossel et al. [MOR
+06]. For more on reverse hypercontractivity, in-
cluding the very surprising fact that the Reverse Hypercontractivity Inequal-
ity holds with no change in constants for every product probability space, see
Mossel, Oleszkiewicz, and Sen [MOS12].

As mentioned in Chapter 9 the deﬁnition of a hypercontractive random
variable is due to Krakowiak and Szulga [KS88]. Many of the basic facts from
Section 10.2 (and also Exercise 10.2) are from this work and the earlier work of
Borell [Bor84]; see also various other works [KW92, Jan97, Szu98, MOO10].
As mentioned, the main part of Theorem 10.18 (the case of biased bits) is es-
sentially from Latała and Oleszkiewicz [LO00]; see also Oleszkiewicz [Ole03].
Our Exercise 10.20 ﬂeshes out (and slightly simpliﬁes) their computations but
introduces no new idea. Earlier works [BKK
+92, Tal94, FK96, Fri98] had
established forms of the General Hypercontractivity Theorem for λ-biased
bits, giving as applications KKL-type theorems in this setting with the correct
asymptotic dependence on λ. We should also mention that the sharp Log-
Sobolev Inequality for product space domains (mentioned in Exercise 10.27)
was derived independently of Latała and Oleszkiewicz’s work by Higuchi and
Yoshida [HY95] (without proof), by Diaconis and Saloff-Coste [DSC96] (with
proof), and possibly also by Oscar Rothaus (see [BL98]). Unlike in the case of

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

10.6. Exercises and notes 325

uniform ±1 bits, it’s not known how to derive Latała and Oleszkiewicz’s opti-
mal biased hypercontractive inequality from the optimal biased Log-Sobolev
Inequality.

Kahane [Kah68] has been credited with pioneering the randomization/
symmetrization trick for random variables. The entirety of Section 10.4 is
due to Bourgain [Bou79], though our presentation was signiﬁcantly informed
by the expertise of Krzysztof Oleszkiewicz (and our proof of Lemma 10.43 is
slightly different). Like Bourgain, we don’t give any explicit dependence for
the constant Cq in Theorem 10.39; however, Kwapie ´n [Kwa10] has shown
that one may take Cq′ = Cq = O(q/ log q) for q ≥ 2. Our proof of Bourgain’s
Theorem 10.47 follows the original [Bou99] extremely closely, though we also
valued the easier-to-read version of Bal [Bal13].

The biased edge-isoperimetric inequality (10.38) from Exercise 10.27 was
proved by induction on n, without the additional o p(1) error, by Russo [Rus82]
(and also independently by Kahn and Kalai [KK07]). We remark that this
work and the earlier [Rus81] already contain the germ of the idea that
monotone functions with small inﬂuences have sharp thresholds. Regarding
the sharp threshold for 3-colorability discussed in Exercise 10.42, Alon and
Spencer [AS08] contains a nice elementary proof of the fact that at the critical
probability for 3-colorability, every subgraph on ϵv vertices is 3-colorable, for
some universal ϵ > 0. The existence of a sharp threshold for k-colorability was
proven by Achlioptas and Friedgut [AF99], with Achlioptas and Naor [AN05]
essentially determining the location.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Chapter 11

Gaussian space and
Invariance Principles

The ﬁnal destination of this chapter is a proof of the following theorem due to
Mossel, O’Donnell, and Oleszkiewicz [MOO05b, MOO10], ﬁrst mentioned in
Chapter 5.2:

Majority Is Stablest Theorem. Fix ρ ∈ (0, 1). Let f : {−1, 1}n → [−1, 1] have
E[ f ] = 0. Then, assuming MaxInf[ f ] ≤ ϵ, or more generally that f has no
(ϵ, ϵ)-notable coordinates,

Stabρ[ f ] ≤ 1 − 2
π arccos ρ + oϵ(1).

This bound is tight; recalling Theorem 2.45, the bound 1− 2
π arccos ρ is achieved
by taking f = Majn, the volume- 1
2 Hamming ball indicator, for n → ∞. More
generally, in Section 11.7 we’ll prove the General-Volume Majority Is Stablest
Theorem, which shows that for any ﬁxed volume, “Hamming ball indicators
have maximal noise stability among small-inﬂuence functions”.

There are two main ideas underlying this theorem. The ﬁrst is that “func-
tions on Gaussian space” are a special case of small-inﬂuence Boolean func-
tions. In other words, a Boolean function may always be a “Gaussian function
in disguise”. This motivates analysis of Gaussian functions, the topic intro-
duced in Sections 11.1 and 11.2. It also means that a prerequisite for proving
the (General-Volume) Majority Is Stablest Theorem is proving its Gaussian
special cases, namely, Borell’s Isoperimetric Theorem (Section 11.3) and the
Gaussian Isoperimetric Inequality (Section 11.4). In many ways, working
in the Gaussian setting is nicer because tools like rotational symmetry and
differentiation are available.
 327

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

328 11. Gaussian space and Invariance Principles

The second idea is the converse to the ﬁrst: In Section 11.6 we prove the
Invariance Principle, a generalization of the Berry–Esseen Central Limit The-
orem, which shows that any low-degree (or uniformly noise-stable) Boolean
function with small inﬂuences is approximable by a Gaussian function. In
fact, the Invariance Principle roughly shows that given such a Boolean func-
tion, if you plug any independent mean-0, variance-1 random variables into
its Fourier expansion, the distribution doesn’t change much. In Section 11.7
we use the Invariance Principle to prove the Majority Is Stablest Theorem by
reducing to its Gaussian special case, Borell’s Isoperimetric Theorem.

11.1. Gaussian space and the Gaussian noise operator

We begin with a few deﬁnitions concerning Gaussian space.

Notation 11.1. Throughout this chapter we write ϕ for the pdf of a standard
Gaussian random variable, ϕ(z) = 1p
2π exp(− 1
2 z2). We also write Φ for its cdf,

and Φ for the complementary cdf Φ(t) = 1 − Φ(t) = Φ(−t). We write z ∼ N(0, 1)n

to denote that z = (z1, . . . , zn) is a random vector in R n whose components zi
are independent Gaussians. Perhaps the most important property of this
distribution is that it’s rotationally symmetric; this follows because the pdf
at z is 1
(2π)n/2 exp(− 1
2 (z2
1 + · · · + z2
n)), which depends only on the length ∥z∥
2
2 of z.

Deﬁnition 11.2. For n ∈ N + and 1 ≤ p ≤ ∞ we write L p(R n, γ) for the space
of Borel functions f : R n → R that have ﬁnite pth moment ∥ f ∥p
p under the
Gaussian measure (the “γ” stands for Gaussian). Here for a function f on
Gaussian space we use the notation

∥ f ∥p = E
z∼N(0,1)n[| f (z)|p]1/p.

All functions f : R n → R and sets A ⊆ R n are henceforth assumed to be Borel
without further mention.

Notation 11.3. When it’s clear from context that f is a function on Gaussian
space we’ll use shorthand notation like E[ f ] = Ez∼N(0,1)n [ f (z)]. If f = 1A is the
0-1 indicator of a subset A ⊆ R n we’ll also write

volγ(A) = E[1A] = Pr
z∼N(0,1)n[z ∈ A]

for the Gaussian volume of A.

Notation 11.4. For f , g ∈ L2(R n, γ) we use the inner product notation 〈 f , g〉 =
E[ f g], under which L2(R n, γ) is a separable Hilbert space.

If you’re only interested in Boolean functions f : {−1, 1}n → {−1, 1} you
might wonder why it’s necessary to study Gaussian space. As discussed at the
beginning of the chapter, the reason is that functions on Gaussian space are

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.1. Gaussian space and the Gaussian noise operator 329

special cases of Boolean functions. Conversely, even if you’re only interested
in studying functions of Gaussian random variables, sometimes the easiest
proof technique involves “simulating” the Gaussians using sums of random
bits. Let’s discuss this in a little more detail. Recall that the Central Limit
Theorem tells us that for x ∼ {−1, 1}M, the distribution of 1pM (x1 + · · · + xM)
approaches that of a standard Gaussian as M → ∞. This is the sense in
which a standard Gaussian random variable z ∼ N(0, 1) can be “simulated” by
random bits. If we want d independent Gaussians we can simulate them by
summing up M independent d-dimensional vectors of random bits.

Deﬁnition 11.5. The function BitsToGaussiansM : {−1, 1}M → R is deﬁned by

BitsToGaussiansM(x) = 1pM (x1 + · · · + xM).

More generally, the function BitsToGaussiansd
M : {−1, 1}dM → R d is deﬁned on
an input x ∈ {−1, 1}d×M, thought of as a matrix of column vectors ⃗x1, . . . ,⃗xM ∈
{−1, 1}d, by
 BitsToGaussiansd
M(x) = 1pM (⃗x1 + · · · +⃗xM).

Although M needs to be large for this simulation to be accurate, many of
the results we’ve developed in the analysis of Boolean functions f : {−1, 1}M →
R are independent of M. A further key point is that this simulation preserves
polynomial degree: if p(z1, . . . , zd) is a degree-k polynomial applied to d inde-
pendent standard Gaussians, the “simulated version” p ◦ BitsToGaussiansd
M :
{−1, 1}dM → R is a degree-k Boolean function. These facts allow us to transfer
many results from the analysis of Boolean functions to the analysis of Gauss-
ian functions. On the other hand, it also means that to fully understand
Boolean functions, we need to understand the “special case” of functions on
Gaussian space: a Boolean function may essentially be a function on Gaussian
space “in disguise”. For example, as we saw in Chapter 5.3, there is a sense in
which the majority function Majn “converges” as n → ∞; what it’s converging
to is the sign function on 1-dimensional Gaussian space, sgn ∈ L1(R , γ).

We’ll begin our study of Gaussian functions by developing the analogue
of the most important operator on Boolean functions, namely the noise oper-
ator Tρ. Suppose we take a pair of ρ-correlated M-bit strings (x, x′) and use
them to form approximate Gaussians,

y = BitsToGaussiansM(x), y′ = BitsToGaussiansM(x′).

For each M it’s easy to compute that E[y] = E[y′] = 0, Var[y] = Var[y′] = 1,
and E[yy′] = ρ. As noted in Chapter 5.2, a multidimensional version of the
Central Limit Theorem (see, e.g., Exercises 5.33, 11.46) tells us that the joint
distribution of (y, y′) converges to a pair of Gaussian random variables with
the same properties. We call these ρ-correlated Gaussians.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

330 11. Gaussian space and Invariance Principles

Deﬁnition 11.6. For −1 ≤ ρ ≤ 1, we say that the random variables (z, z′) are
ρ-correlated (standard) Gaussians if they are jointly Gaussian and satisfy
E[z] = E[z′] = 0, Var[z] = Var[z′] = 1, and E[zz′] = ρ. In other words, if

(z, z′) ∼ N ([
0
0

] , [1 ρ
ρ 1
]) .

Note that the deﬁnition is symmetric in z, z′ and that each is individually
distributed as N(0, 1).

Fact 11.7. An equivalent deﬁnition is to say that z = 〈⃗u,⃗g〉 and z′ = 〈⃗v,⃗g〉,
where ⃗g ∼ N(0, 1)d and ⃗u,⃗v ∈ R d are any two unit vectors satisfying 〈⃗u,⃗v〉 = ρ.
In particular we may choose d = 2, ⃗u = (1, 0), and ⃗v = (ρ, √
1 − ρ2), thereby
deﬁning z = g1 and z′ = ρ g1 + √1 − ρ2 g2.

Remark 11.8. In Fact 11.7 it’s often convenient to write ρ = cos θ for some
θ ∈ R , in which case we may deﬁne the ρ-correlated Gaussians as z = 〈⃗u,⃗g〉
and z′ = 〈⃗v,⃗g〉 for any unit vectors ⃗u,⃗v making an angle of θ; e.g., ⃗u = (1, 0),
⃗v = (cos θ, sin θ).

Deﬁnition 11.9. For a ﬁxed z ∈ R we say random variable z′ is a Gaussian
ρ-correlated to z, written z′ ∼ Nρ(z), if z′ is distributed as ρz+√1 − ρ2 g where
g ∼ N(0, 1). By Fact 11.7, if we draw z ∼ N(0, 1) and then form z′ ∼ Nρ(z), we
obtain a ρ-correlated pair of Gaussians (z, z′).

Deﬁnition 11.10. For −1 ≤ ρ ≤ 1 and n ∈ N + we say that the R n-valued
random variables (z, z′) are ρ-correlated n-dimensional Gaussian random
vectors if each component pair (z1, z′
1), . . . , (zn, z′
n) is a ρ-correlated pair of
Gaussians, and the n pairs are mutually independent. We also naturally
extend the deﬁnition of z′ ∼ Nρ(z) to the case of z ∈ R n; this means z′ =

ρz + √1 − ρ2 g for g ∼ N(0, 1)n.

Remark 11.11. Thus, if z ∼ N(0, 1)n and then z′ ∼ Nρ(z) we obtain a ρ-
correlated n-dimensional pair (z, z′). It follows from this that (z, z′) has the
same distribution as (Q z,Q z′) for any rotation Q on R n.

Now we can introduce the Gaussian analogue of the noise operator.

Deﬁnition 11.12. For ρ ∈ [−1, 1], the Gaussian noise operator Uρ is the linear
operator deﬁned on the space of functions f ∈ L1(R n, γ) by

Uρ f (z) = E
z′∼Nρ(z)[ f (z′)] = E
g∼N(0,1)n[ f (ρz + √
1 − ρ2 g)].

Fact 11.13. (Exercise 11.3.) If f ∈ L1(R n, γ) is an n-variate multilinear poly-
nomial, then Uρ f (z) = f (ρz).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.1. Gaussian space and the Gaussian noise operator 331

Remark 11.14. Our terminology is nonstandard. The Gaussian noise op-
erators are usually collectively referred to as the Ornstein–Uhlenbeck semi-
group (or sometimes as the Mehler transforms). They are typically deﬁned for
ρ = e−t ∈ [0, 1] (i.e., for t ∈ [0, ∞]) by

Pt f (z) = E
g∼N(0,1)n[ f (e−t z + √1 − e−2t g)] = Ue−t f (z).

The term “semigroup” refers to the fact that the operators satisfy Pt1Pt2 =
Pt1+t2, i.e., Uρ1Uρ2 = Uρ1ρ2 (which holds for all ρ1, ρ2 ∈ [−1, 1]; see Exer-
cise 11.4).

Before going further let’s check that Uρ is a bounded operator on all of
L p(R n, γ) for p ≥ 1; in fact, it’s a contraction (cf. Exercise 2.33):

Proposition 11.15. For each ρ ∈ [−1, 1] and 1 ≤ p ≤ ∞ the operator Uρ is a
contraction on L p(R n, γ); i.e., ∥Uρ f ∥p ≤ ∥ f ∥p.

Proof. The proof for p = ∞ is easy; otherwise, the result follows from Jensen’s
inequality, using that t 7→ |t|p is convex:

∥Uρ f ∥p
p = E
z∼N(0,1)n[|Uρ f (z)|p] = E
z∼N(0,1)n
 [∣
∣
∣
∣ E
z′∼Nρ(z)[ f (z′)]∣
∣
∣
∣
p]

≤ E
z∼N(0,1)n
 [ E
z′∼Nρ(z)[| f (z′)|p]
] = ∥ f ∥p
p. □

As in the Boolean case, you should think of the Gaussian noise operator
as having a “smoothing” effect on functions. As ρ goes from 1 down to 0,
Uρ f involves averaging f ’s values over larger and larger neighborhoods. In
particular U1 is the identity operator, U1 f = f , and U0 f = E[ f ], the constant
function. In Exercises 11.5, 11.6 you are asked to verify the following facts,
which say that for any f , as ρ → 1− we get a sequence of smooth (i.e., C ∞)
functions Uρ f that tend to f .

Proposition 11.16. Let f ∈ L1(R n, γ) and let −1 < ρ < 1. Then Uρ f is a
smooth function.

Proposition 11.17. Let f ∈ L1(R n, γ). As ρ → 1− we have ∥Uρ f − f ∥1 → 0.

Having deﬁned the Gaussian noise operator, we can also make the natural
deﬁnition of Gaussian noise stability (for which we’ll use the same notation
as in the Boolean case):

Deﬁnition 11.18. For f ∈ L2(R n, γ) and ρ ∈ [−1, 1], the Gaussian noise stabil-
ity of f at ρ is deﬁned to be

Stabρ[ f ] = E
(z,z′) n-dimensional
ρ-correlated Gaussians

[ f (z) f (z′)] = 〈 f , Uρ f 〉 = 〈Uρ f , f 〉.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

332 11. Gaussian space and Invariance Principles

(Here we used that (z′, z) has the same distribution as (z, z′) and hence Uρ is
self-adjoint.)

Example 11.19. Let f : R → {0, 1} be the 0-1 indicator of the nonpositive
halﬂine: f = 1(−∞,0]. Then

Stabρ[ f ] = E
(z,z′) ρ-correlated
standard Gaussians

[ f (z) f (z′)] = Pr[z ≤ 0, z′ ≤ 0] = 1
2 − 1
2 arccos ρ

π ,

(11.1)
with the last equality being Sheppard’s Formula, which we stated in Sec-
tion 5.2 and now prove.

Proof of Sheppard’s Formula. Since (−z, −z′) has the same distribution
as (z, z′), proving (11.1) is equivalent to proving

Pr[z ≤ 0, z′ ≤ 0 or z > 0, z′ > 0] = 1 − arccos ρ

π .

The complement of the above event is the event that f (z) ̸= f (z′) (up to mea-
sure 0); thus it’s further equivalent to prove

Pr
(z,z′)
cos θ-correlated

[ f (z) ̸= f (z′)] = θ
π (11.2)

for all θ ∈ [0, π]. As in Remark 11.8, this suggests deﬁning z = 〈⃗u,⃗g〉, z′ = 〈⃗v,⃗g〉,
where ⃗u,⃗v ∈ R 2 is some ﬁxed pair of unit vectors making an angle of θ, and
⃗g ∼ N(0, 1)
2. Thus we want to show

Pr
⃗g∼N(0,1)2[〈⃗u,⃗g〉 ≤ 0 & 〈⃗v,⃗g〉 > 0 or vice versa] = θ
π .

But this last identity is easy: If we look at the diameter of the unit circle that
is perpendicular to ⃗g, then the event above is equivalent (up to measure 0)
to the event that this diameter “splits” ⃗u and ⃗v. By the rotational symmetry
of ⃗g, the probability is evidently θ (the angle between ⃗u,⃗v) divided by π (the
range of angles for the diameter). □

Corollary 11.20. Let H ⊂ R n be any halfspace (open or closed) with boundary
hyperplane containing the origin. Let h = ±1H. Then Stabρ[h] = 1 − 2
π arccos ρ.

Proof. We may assume H is open (since its boundary has measure 0). By
the rotational symmetry of correlated Gaussians (Remark 11.11), we may
rotate H to the form H = {z ∈ R n : z1 > 0}. Then it’s clear that the noise
stability of h = ±1H doesn’t depend on n, i.e., we may assume n = 1. Thus
h = sgn = 1 − 2 f , where f = 1(−∞,0] as in Example 11.19. Now if (z, z′) denote
ρ-correlated standard Gaussians, it follows from (11.1) that

Stabρ[h] = E[h(z)h(z′)] = E[(1 − 2 f (z))(1 − 2 f (z′))]

= 1 − 4 E[ f ] + 4Stabρ[ f ] = 1 − 2
π arccos ρ. □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.1. Gaussian space and the Gaussian noise operator 333

Remark 11.21. The quantity Stabρ[sgn] = 1 − 2
π arccos ρ is also precisely the
limiting noise stability of Majn, as stated in Theorem 2.45 and justiﬁed in
Chapter 5.2.

We’ve deﬁned the key Gaussian noise operator Uρ and seen (Proposi-
tion 11.15) that it’s a contraction on all L p(R n, γ). Is it also hypercontractive?
In fact, we’ll now show that the Hypercontractivity Theorem for uniform ±1
bits holds identically in the Gaussian setting. The proof is simply a reduction
to the Boolean case, and it will use the following standard fact (see Jan-
son [Jan97, Theorem 2.6] or Teuwen [Teu12, Section 1.3] for the proof in
case of L2; to extend to other L p you can use Exercise 11.1):

Theorem 11.22. For each n ∈ N +, the set of multivariate polynomials is dense
in L p(R n, γ) for all 1 ≤ p < ∞.

Gaussian Hypercontractivity Theorem. Let f , g ∈ L1(R n, γ), let r, s ≥ 0,
and assume 0 ≤ ρ ≤ prs ≤ 1. Then

〈 f , Uρ g〉 = 〈Uρ f , g〉 = E
(z,z′) ρ-correlated
n-dimensional Gaussians

[ f (z)g(z′)] ≤ ∥ f ∥1+r∥g∥1+s.

Proof. (We give a sketch; you are asked to ﬁll in the details in Exercise 11.2.)
We may assume that f ∈ L1+r(R n, γ) and g ∈ L1+s(R n, γ). We may also assume
f , g ∈ L2(R n, γ) by a truncation and monotone convergence argument; thus the
left-hand side is ﬁnite by Cauchy–Schwarz. Finally, we may assume that f
and g are multivariate polynomials, using Theorem 11.22. For ﬁxed M ∈
N + we consider “simulating” (z, z′) using bits. More speciﬁcally, let (x, x′) ∈
{−1, 1}nM ×{−1, 1}nM be a pair ρ-correlated random strings and deﬁne the joint
R n-valued random variables y, y′ by

y = BitsToGaussiansn
M(x), y′ = BitsToGaussiansn
M(x′).

By a multidimensional Central Limit Theorem we have that

E[ f (y)g(y′)] M→∞
−−−−→ E
(z,z′)
ρ-correlated
[ f (z)g(z′)].

(Since f and g are polynomials, we can even reduce to a Central Limit Theo-
rem for bivariate monomials.) We further have

E[| f (y)|1+r]1/(1+r) M→∞
−−−−→ E
z∼N(0,1)n[| f (z)|1+r]1/(1+r)

and similarly for g. (This can also be proven by the multidimensional Central
Limit Theorem, or by the one-dimensional Central Limit Theorem together
with some tricks.) Thus it sufﬁces to show

E[ f (y)g(y′)] ≤ E[| f (y)|1+r]
1/(1+r) E[|g(y′)|1+s]
1/(1+s)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

334 11. Gaussian space and Invariance Principles

for any ﬁxed M. But we can express f (y) = F(x) and g(y′) = G(x′) for some
F,G : {−1, 1}nM → R and so the above inequality holds by the Two-Function
Hypercontractivity Theorem (for ±1 bits). □

An immediate corollary, using the proof of Proposition 10.4, is the stan-
dard one-function form of hypercontractivity:

Theorem 11.23. Let 1 ≤ p ≤ q ≤ ∞ and let f ∈ L p(R n, γ). Then ∥Uρ f ∥q ≤ ∥ f ∥p

for 0 ≤ ρ ≤ √ p−1
q−1 .

We conclude this section by discussing the Gaussian space analogue of
the discrete Laplacian operator. Taking our cue from Exercise 2.18 we make
the following deﬁnition:

Deﬁnition 11.24. The Ornstein–Uhlenbeck operator L (also called the in-
ﬁnitesimal generator of the Ornstein–Uhlenbeck semigroup, or the number
operator) is the linear operator acting on functions f ∈ L2(R n, γ) by

L f = d
dρ Uρ f ∣
∣
∣ρ=1 = − d
dt Ue−t f ∣
∣
∣t=0

(provided L f exists in L2(R n, γ)). Notational warning: It is common to see
this as the deﬁnition of −L.

Remark 11.25. We will not be completely careful about the domain of the
operator L in this section; for precise details, see Exercise 11.18.

Proposition 11.26. Let f ∈ L2(R n, γ) be in the domain of L, and further
assume for simplicity that f is C 3. Then we have the formula

L f (x) = x · ∇ f (x) − ∆ f (x),

where ∆ denotes the usual Laplacian differential operator, · denotes the dot
product, and ∇ denotes the gradient.

Proof. We give the proof in the case n = 1, leaving the general case to Exer-
cise 11.7. We have

L f (x) = − lim
t→0+ Ez∼N(0,1)[ f (e−tx + p
1 − e−2t z)] − f (x)

t . (11.3)

Applying Taylor’s theorem to f we have

f (e−tx + √1 − e−2t z) ≈ f (e−tx) + f ′(e−tx)
√
1 − e−2t z + 1
2 f ′′(e−t x)(1 − e−2t)z2,

where the ≈ denotes that the two quantities differ by at most C(1− e−2t)
3/2|z|3

in absolute value, for some constant C depending on f and x. Substituting

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.1. Gaussian space and the Gaussian noise operator 335

this into (11.3) and using E[z] = 0, E[z2] = 1, and that E[|z|3] is an absolute
constant, we get

L f (x) = − lim
t→0+
 ( f (e−tx) − f (x)
t +
 1
2 f ′′(e−tx)(1 − e−2t)

t
 )
 ,

using the fact that (1−e−2t)3/2
t → 0. But this is easily seen to be x f ′(x) − f ′′(x), as
claimed. □

An easy consequence of the semigroup property is the following:

Proposition 11.27. The following equivalent identities hold:

d
dρ Uρ f = ρ−1LUρ f = ρ−1UρL f ,

d
dt Ue−t f = −LUe−t f = −Ue−t L f .

Proof. This follows from
d
dt Ue−t f (x) = lim
δ→0 Ue−t−δ f (x) − Ue−t f (x)

δ

= lim
δ→0 Ue−δUe−t f (x) − Ue−t f (x)

δ = lim
δ→0 Ue−t Ue−δ f (x) − Ue−t f (x)

δ . □

We also have the following formula:

Proposition 11.28. Let f , g ∈ L2(R n, γ) be in the domain of L, and further
assume for simplicity that they are C 3. Then

〈 f , Lg〉 = 〈L f , g〉 = 〈∇ f , ∇g〉. (11.4)

Proof. It sufﬁces to prove the inequality on the right of (11.4). We again
treat only the case of n = 1, leaving the general case to Exercise 11.8. Using
Proposition 11.26,

〈L f , g〉 = ∫
R (x f ′(x) − f ′′(x))g(x)ϕ(x) dx

= ∫
R x f ′(x)g(x)ϕ(x) dx + ∫
R f ′(x)(gϕ)′(x) dx (integration by parts)

= ∫
R x f ′(x)g(x)ϕ(x) dx + ∫
R f ′(x)(g′(x)ϕ(x) + g(x)ϕ
′(x)) dx

= ∫
R f ′(x)g′(x)ϕ(x) dx,

using the fact that ϕ
′(x) = −xϕ(x). □

Finally, by differentiating the Gaussian Hypercontractivity Inequality we
obtain the Gaussian Log-Sobolev Inequality (see Exercise 10.23; the proof is
the same as in the Boolean case):

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

336 11. Gaussian space and Invariance Principles

Gaussian Log-Sobolev Inequality. Let f ∈ L2(R n, γ) be in the domain of L.
Then
 1
2 Ent[ f 2] ≤ E[∥∇ f ∥
2].

It’s tempting to use the notation I[ f ] for E[∥∇ f ∥
2]; however, you have to
be careful because this quantity is not equal to ∑n
i=1 E[Varzi [ f ]] unless f is a
multilinear polynomial. See Exercise 11.13.

11.2. Hermite polynomials

Having deﬁned the basic operators of importance for functions on Gaussian
space, it’s useful to also develop the analogue of the Fourier expansion. To
do this we’ll proceed as in Chapter 8.1, looking for a complete orthonormal
“Fourier basis” for L2(R , γ), which we can extend to L2(R n, γ) by taking prod-
ucts. It’s natural to start with polynomials; by Theorem 11.22 we know that
the collection (φ j) j∈N , φ j(z) = z j is a complete basis for L2(R , γ). To get an
orthonormal (“Fourier”) basis we can simply perform the Gram–Schmidt pro-
cess. Calling the resulting basis (h j) j∈N (with “h” standing for “Hermite”), we
get
 h0(z) = 1, h1(z) = z, h2(z) = z2 − 1
p
2 , h3(z) = z3 − 3z
p
6 , . . . (11.5)

Here, e.g., we obtained h3(z) in two steps. First, we made φ3(z) = z3 orthogo-
nal to h0, . . . , h2 as

z3 − 〈z3, 1〉 · 1 − 〈z3, z〉 · z − 〈z3, z2−1p
2 〉 · z2−1p
2 = z3 − 3z,

where z ∼ N(0, 1) and we used the fact that z3 and z3 · z2−1p
2 are odd functions

and hence have Gaussian expectation 0. Then we deﬁned h3(z) = z3−3zp
6 after

determining that E[(z3 − 3z)
2] = 6.

Let’s develop a more explicit deﬁnition of these Hermite polynomials. The
computations involved in the Gram–Schmidt process require knowledge of
the moments of a Gaussian random variable z ∼ N(0, 1). It’s most convenient
to understand these moments through the moment generating function of z,
namely

E[exp(tz)] = 1p
2π
 ∫
R etz e− 1
2 z2 dz = e 1
2 t2 1p
2π
 ∫
R e− 1
2 (z−t)2 dz = exp( 1
2 t2). (11.6)

In light of our interest in the Uρ operators, and the fact that orthonormality
involves pairs of basis functions, we’ll in fact study the moment generating
function of a pair (z, z′) of ρ-correlated standard Gaussians. To compute it,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.2. Hermite polynomials 337

assume (z, z′) are generated as in Fact 11.7 with ⃗u,⃗v unit vectors in R 2. Then

E
(z,z′)
ρ-correlated

[exp(sz + tz′)] = E
g1,g2∼N(0,1)
independent
 [exp(s(u1 g1 + u2 g2) + t(v1 g1 + v2 g2))]

= E
g1∼N(0,1)[exp((su1 + tv1)g1)] E
g2∼N(0,1)[exp((su2 + tv2)g2)]

= exp( 1
2 (su1 + tv1)
2) exp( 1
2 (su2 + tv2)2)

= exp( 1
2 ∥⃗u∥
2
2s2 + 〈⃗u,⃗v〉st + 1
2 ∥⃗v∥
2
2t2)

= exp( 1
2 (s2 + 2ρst + t2)),

where the third equality used (11.6). Dividing by exp( 1
2 (s2 + t2)) it follows that

E
(z,z′)
ρ-correlated

[exp(sz − 1
2 s2) exp(tz′ − 1
2 t2)] = exp(ρst) = ∞∑

j=0
 ρ j

j! s j t j. (11.7)

Inside the expectation above we essentially have the expression exp(tz − 1
2 t2)
appearing twice. It’s easy to see that if we take the power series in t for
this expression, the coefﬁcient on t j will be a polynomial in z with leading
term 1
j! z j. Let’s therefore write

exp(tz − 1
2 t2) = ∞∑

j=0
 1
j! H j(z)t j, (11.8)

where H j(z) is a monic polynomial of degree j. Now substituting this into (11.7)
yields ∞∑

j,k=0
 1
j!k! E
(z,z′)
ρ-correlated

[H j(z)Hk(z′)]s j tk = ∞∑

j=0
 ρ j

j! s j t j.

Equating coefﬁcients, it follows that we must have

E
(z,z′)
ρ-correlated
[H j(z)Hk(z′)] =
 { j!ρ j if j = k,

0 if j ̸= k.

In particular (taking ρ = 1),

〈H j, Hk〉 =
 { j! if j = k,

0 if j ̸= k; (11.9)

i.e., the polynomials (H j) j∈N are orthogonal. Furthermore, since H j is monic
and of degree j, it follows that the H j’s are precisely the polynomials that
arise in the Gram–Schmidt orthogonalization of {1, z, z2, . . . }. We also see
from (11.9) that the orthonormalized polynomials (h j) j∈N are obtained by
setting h j = 1p j! H j.

Let’s summarize and introduce the terminology for what we’ve deduced.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

338 11. Gaussian space and Invariance Principles

Deﬁnition 11.29. The probabilists’ Hermite polynomials (H j) j∈N are the
univariate polynomials deﬁned by the identity (11.8). An equivalent deﬁnition
(Exercise 11.9) is
 H j(z) = (−1) j

ϕ(z) · d j

dz j ϕ(z). (11.10)

The normalized Hermite polynomials (h j) j∈N are deﬁned by h j = 1p j! H j; the

ﬁrst four are given explicitly in (11.5). For brevity we’ll simply refer to the
h j’s as the “Hermite polynomials”, though this is not standard terminology.

Proposition 11.30. The Hermite polynomials (h j) j∈N form a complete or-
thonormal basis for L2(R , γ). They are also a “Fourier basis”, since h0 = 1.

Proposition 11.31. For any ρ ∈ [−1, 1] we have

E
(z,z′)
ρ-correlated

[h j(z)hk(z′)] = 〈h j, Uρ hk〉 = 〈Uρ h j, hk〉 =
 {
ρ j if j = k,

0 if j ̸= k.

From this “Fourier basis” for L2(R , γ) we can construct a “Fourier basis”
for L2(R n, γ) just by taking products, as in Proposition 8.13.

Deﬁnition 11.32. For a multi-index α ∈ N n we deﬁne the (normalized multi-
variate) Hermite polynomial hα : R n → R by

hα(z) = n∏

j=1 hα j (z j).

Note that the total degree of hα is |α| = ∑ j α j. We also identify a subset S ⊆ [n]
with its indicator α deﬁned by α j = 1 j∈S; thus hS(z) denotes zS = ∏ j∈S z j.

Proposition 11.33. The Hermite polynomials (hα)α∈N n form a complete or-
thonormal (Fourier) basis for L2(R n, γ). Further, for any ρ ∈ [−1, 1] we have

E
(z,z′)
ρ-correlated

[hα(z)hβ(z′)] = 〈hα, Uρ hβ〉 = 〈Uρ hα, hβ〉 =
 {
ρ|α| if α = β,

0 if α ̸= β.

We can now deﬁne the “Hermite expansion” of Gaussian functions.

Deﬁnition 11.34. Every f ∈ L2(R n, γ) is uniquely expressible as

f = ∑

α∈N n ̂f (α)hα,

where the real numbers ̂f (α) are called the Hermite coefﬁcients of f and the
convergence is in L2(R n, γ); i.e.,
∥
∥
∥
∥
∥ f − ∑

|α|≤k ̂f (α)hα
∥
∥
∥
∥
∥
2 → 0 as k → ∞.

This is called the Hermite expansion of f .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.2. Hermite polynomials 339

Remark 11.35. If f : R n → R is a multilinear polynomial, then it “is its own
Hermite expansion”:

f (z) = ∑

S⊆[n] ̂f (S)zS = ∑

S⊆[n] ̂f (S)hS(z) = ∑

α1,...,αn≤1 ̂f (α)hα(z).

Proposition 11.36. The Hermite coefﬁcients of f ∈ L2(R n, γ) satisfy the for-
mula ̂f (α) = 〈 f , hα〉,

and for f , g ∈ L2(R n, γ) we have the Plancherel formula

〈 f , g〉 = ∑

α∈N n ̂f (α) ̂g(α).

From this we may deduce:

Proposition 11.37. For f ∈ L2(R n, γ), the function Uρ f has Hermite expan-
sion Uρ f = ∑

α∈N n ρ|α| ̂f (α)hα

and hence Stabρ[ f ] = ∑

α∈N n ρ|α| ̂f (α)
2.

Proof. Both statements follow from Proposition 11.36, with the ﬁrst using

†Uρ f (α) = 〈Uρ f , hα〉 = 〈
∑

β Uρ ̂f (β)hβ, hα〉 = ∑

β ̂f (β)〈Uρ hβ, hα〉 = ρ|α| ̂f (α);

we also used Proposition 11.33 and the fact that Uρ is a contraction in L2(R n, γ).
□

Remark 11.38. When f : R n → R is a multilinear polynomial, this formula
for Uρ f agrees with the formula f (ρz) given in Fact 11.13.

Remark 11.39. In a sense it’s not very important to know the explicit for-
mulas for the Hermite polynomials, (11.5), (11.8); it’s usually enough just to
know that the formula for Uρ f from Proposition 11.37 holds.

Finally, by differentiating the formula in Proposition 11.37 at ρ = 1 we de-
duce the following formula for the Ornstein–Uhlenbeck operator (explaining
why it’s sometimes called the number operator):

Proposition 11.40. For f ∈ L2(R n, γ) in the domain of L we have

L f = ∑

α∈N n |α| ̂f (α)hα.

(Actually, Exercise 11.18 asks you to formally justify this and the fact that
f is in the domain of L if and only if ∑
α |α|2 ̂f (α)2 < ∞.) For additional facts
about Hermite polynomials, see Exercises 11.9–11.14.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

340 11. Gaussian space and Invariance Principles

11.3. Borell’s Isoperimetric Theorem

If we believe that the Majority Is Stablest Theorem should be true, then
we also have to believe in its “Gaussian special case”. Let’s see what this
Gaussian special case is. Suppose f : R n → [−1, 1] is a “nice” function (smooth,
say, with all derivatives bounded) having E[ f ] = 0. You’re encouraged to
think of f as (a smooth approximation to) the indicator ±1A of some set
A ⊆ R n of Gaussian volume volγ(A) = 1
2 . Now consider the Boolean function
g : {−1, 1}nM → {−1, 1} deﬁned by

g = f ◦ BitsToGaussiansn
M.

Using the multidimensional Central Limit Theorem, for any ρ ∈ (0, 1) we
should have
 Stabρ[g] M→∞
−−−−→ Stabρ[ f ],

where on the left we have Boolean noise stability and on the right we have
Gaussian noise stability. Using E[g] → E[ f ] = 0, the Majority Is Stablest
Theorem would tell us that

Stabρ[g] ≤ 1 − 2
π arccos ρ + oϵ(1),

where ϵ = MaxInf[g]. But ϵ = ϵ(M) → 0 as M → ∞. Thus we should simply
have the Gaussian noise stability bound

Stabρ[ f ] ≤ 1 − 2
π arccos ρ. (11.11)

(By a standard approximation argument this extends from “nice” f : R n →
[−1, 1] with E[ f ] = 0 to any measurable f : R n → [−1, 1] with E[ f ] = 0.) Note
that the upper bound (11.11) is achieved when f is the ±1-indicator of any
halfspace through the origin; see Corollary 11.20. (Note also that if n = 1 and
f = sgn, then the function g is simply MajM.)

The “isoperimetric inequality” (11.11) is indeed true, and is a special case
of a theorem ﬁrst proved by Borell [Bor85].

Borell’s Isoperimetric Theorem (volume- 1
2 case). Fix ρ ∈ (0, 1). Then for
any f ∈ L2(R n, γ) with range [−1, 1] and E[ f ] = 0,

Stabρ[ f ] ≤ 1 − 2
π arccos ρ,

with equality if f is the ±1-indicator of any halfspace through the origin.

Remark 11.41. In Borell’s Isoperimetric Theorem, nothing is lost by restrict-
ing attention to functions with range {−1, 1}, i.e., by considering only f = ±1A
for A ⊆ R n. This is because the case of range [−1, 1] follows straightforwardly
from the case of range {−1, 1}, essentially because √
Stabρ[ f ] = ∥Up
ρ f ∥2 is a
convex functional of f ; see Exercise 11.25.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.3. Borell’s Isoperimetric Theorem 341

More generally, Borell showed that for any ﬁxed volume α ∈ [0, 1], the
maximum Gaussian noise stability of a set of volume α is no greater than that
of a halfspace of volume α. We state here the more general theorem, using
range {0, 1} rather than range {−1, 1} for future notational convenience (and
with Remark 11.41 applying equally):

Borell’s Isoperimetric Theorem. Fix ρ ∈ (0, 1). Then for any f ∈ L2(R n, γ)
with range [0, 1] and E[ f ] = α,

Stabρ[ f ] ≤ Λρ(α).

Here Λρ(α) is the Gaussian quadrant probability function, discussed in Exer-
cises 5.32 and 11.19, and equal to Stabρ[1H] for any (every) halfspace H ⊆ R n

having Gaussian volume volγ(H) = α.

We’ve seen that the volume- 1
2 case of Borell’s Isoperimetric Theorem is a
special case of the Majority Is Stablest Theorem, and similarly, the general
version of Borell’s theorem is a special case of the General-Volume Majority
Is Stablest Theorem mentioned at the beginning of the chapter. As a conse-
quence, proving Borell’s Isoperimetric Theorem is a prerequisite for proving
the General-Volume Majority Is Stablest Theorem. In fact, our proof in Sec-
tion 11.7 of the latter will be a reduction to the former.

The proof of Borell’s Isoperimetric Theorem itself is not too hard; one of
ﬁve known proofs, the one due to Mossel and Neeman [MN12], is outlined in
Exercises 11.26–11.29. If our main goal is just to prove the basic Majority Is
Stablest Theorem, then we only need the volume- 1
2 case of Borell’s Isoperi-
metric Inequality. Luckily, there’s a very simple proof of this volume- 1
2 case
for “many” values of ρ, as we will now explain.

Let’s ﬁrst slightly rephrase the statement of Borell’s Isoperimetric Theo-
rem in the volume- 1
2 case. By Remark 11.41 we can restrict attention to sets;
then the theorem asserts that among sets of Gaussian volume 1
2 , halfspaces
through the origin have maximal noise stability, for each positive value of ρ.
Equivalently, halfspaces through the origin have minimal noise sensitivity
under correlation cos θ, for θ ∈ (0, π
2 ). The formula for this minimal noise sen-
sitivity was given as (11.2) in our proof of Sheppard’s Formula. Thus we have:

Equivalent statement of the volume- 1
2 Borell Isoperimetric Theorem.
Fix θ ∈ (0, π
2 ). Then for any A ⊂ R n with volγ(A) = 1
2 ,

Pr
(z,z′)
cos θ-correlated

[1A(z) ̸= 1A(z′)] ≥ θ
π ,

with equality if A is any halfspace through the origin.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

342 11. Gaussian space and Invariance Principles

In the remainder of this section we’ll show how to prove this formulation
of the theorem whenever θ = π
2ℓ , where ℓ is a positive integer. This gives
the volume- 1
2 case of Borell’s Isoperimetric Inequality for all ρ of the form
arccos π
2ℓ , ℓ ∈ N +; in particular, for an inﬁnite sequence of ρ’s tending to 1. To
prove the theorem for these values of θ, it’s convenient to introduce notation
for the following noise sensitivity variant:

Deﬁnition 11.42. For A ⊆ R n and δ ∈ R (usually δ ∈ [0, π]) we write RSA(δ)
for the rotation sensitivity of A at δ, deﬁned by

RSA(δ) = Pr
(z,z′)
cos δ-correlated

[1A(z) ̸= 1A(z′)].

The key property of this deﬁnition is the following:

Theorem 11.43. For any A ⊆ R n the function RSA(δ) is subadditive; i.e.,

RSA(δ1 + · · · + δℓ) ≤ RSA(δ1) + · · · + RSA(δℓ).

In particular, for any δ ∈ R and ℓ ∈ N +,

RSA(δ) ≤ ℓ · RSA(δ/ℓ).

Proof. Let g, g′ ∼ N(0, 1)n be drawn independently and deﬁne z(θ) = (cos θ)g+
(sin θ)g′. Geometrically, as θ goes from 0 to π
2 the random vectors z(θ) trace
from g to g′ along the origin-centered ellipse passing through these two points.
The random vectors z(θ) are jointly normal, with each individually distributed
as N(0, 1)n. Further, for each ﬁxed θ, θ′ ∈ R the pair (z(θ), z(θ′)) constitute ρ-
correlated Gaussians with

ρ = cos θ cos θ′ + sin θ sin θ′ = cos(θ′ − θ).

Now consider the sequence θ0, . . . , θℓ deﬁned by the partial sums of the δi’s,
i.e., θ j = ∑ j
i=1 δi. We get that z(θ0) and z(θℓ) are cos(δ1 + · · · + δℓ)-correlated,
and that z(θ j−1) and z(θ j) are cos δ j-correlated for each j ∈ [ℓ]. Thus

RSA(δ1 + · · · + δℓ) = Pr[1A(z(θ0)) ̸= 1A(z(θℓ))]

≤ ℓ∑

j=1 Pr[1A(z(θ j)) ̸= 1A(z(θ j−1))] = ℓ∑

j=1 RSA(δ j), (11.12)

where the inequality is the union bound. □

With this subadditivity result in hand, it’s indeed easy to prove the equiv-
alent statement of the volume- 1
2 Borell Isoperimetric Theorem for any θ ∈
{ π
4 , π
6 , π
8 , π
10 , . . . }. As we’ll see in Section 11.7, the case of θ = π
4 can be used to
give an excellent UG-hardness result for the Max-Cut CSP.

Corollary 11.44. The equivalent statement of the volume- 1
2 Borell Isoperimet-
ric Theorem holds whenever θ = π
2ℓ for ℓ ∈ N +.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.4. Gaussian surface area and Bobkov’s Inequality 343

Proof. The exact statement we need to show is RSA( π
2ℓ ) ≥ 1
2ℓ . This follows
by taking δ = π
2 in Theorem 11.43 because

RSA( π
2 ) = Pr
(z,z′)
0-correlated

[1A(z) ̸= 1A(z′)] = 1
2 ,

using that 0-correlated Gaussians are independent and that volγ(A) = 1
2 . □

Remark 11.45. Although Sheppard’s Formula already tells us that equality
holds in this corollary when A is a halfspace through the origin, it’s also
not hard to derive this directly from the proof. The only inequality in the
proof, (11.12), is an equality when A is a halfspace through the origin, because
the elliptical arc can only cross such a halfspace 0 or 1 times.

Remark 11.46. Suppose that A ⊆ R n not only has volume 1
2 , it has the
property that x ∈ A if and only if −x ̸∈ A; in other words, the ±1-indicator
of A is an odd function. (In both statements, we allow a set of measure 0 to
be ignored.) An example set with this property is any halfspace through the
origin. Then RSA(π) = 1, and hence we can establish Corollary 11.44 more
generally for any θ ∈ { π
1 , π
2 , π
3 , π
4 , π
5 , . . . } by taking δ = π in the proof.

11.4. Gaussian surface area and Bobkov’s Inequality

This section is devoted to studying the Gaussian Isoperimetric Inequality.
This inequality is a special case of the Borell Isoperimetric Inequality (and
hence also a special case of the General-Volume Majority Is Stablest Theorem);
in particular, it’s the special case arising from the limit ρ → 1−.

Restating Borell’s theorem using rotation sensitivity we have that for any
A ⊆ R n, if H ⊆ R n is a halfspace with the same Gaussian volume as A then
for all ϵ, RSA(ϵ) ≥ RSH(ϵ).

Since RSA(0) = RSH(0) = 0, it follows that

RS
′
A(0
+) ≥ RS
′
H(0
+).

(Here we are considering the one-sided derivatives at 0, which can be shown
to exist, though RS
′
A(0+) may equal +∞; see the notes at the end of this
chapter.) As will be explained shortly, RS
′
A(0+) is precisely p
2/π · surfγ(A),
where surfγ(A) denotes the “Gaussian surface area” of A. Therefore the above
inequality is equivalent to the following:

Gaussian Isoperimetric Inequality. Let A ⊆ R n have volγ(A) = α and let
H ⊆ R n be any halfspace with volγ(H) = α. Then surfγ(A) ≥ surfγ(H).

Remark 11.47. As shown in Proposition 11.49 below, the right-hand side
in this inequality is equal to U (α), where U is the Gaussian isoperimetric
function, encountered earlier in Deﬁnition 5.26 and deﬁned by U = ϕ ◦ Φ−1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

344 11. Gaussian space and Invariance Principles

Let’s now discuss the somewhat technical question of how to properly
deﬁne surfγ(A), the Gaussian surface area of a set A. Perhaps the most
natural deﬁnition would be to equate it with the Gaussian Minkowski content
of the boundary ∂A of A,

γ
+(∂A) = lim inf
ϵ→0+ volγ({z : dist(z, ∂A) < ϵ/2})

ϵ . (11.13)

(Relatedly, one might also consider the surface integral over ∂A of the Gauss-
ian pdf ϕ.) Under the “ofﬁcial” deﬁnition of surfγ(A) we give below in Deﬁni-
tion 11.48, we’ll indeed have surfγ(A) = γ
+(∂A) whenever A is sufﬁciently nice
– say, a disjoint union of closed, full-dimensional, convex sets. However, the
Minkowski content deﬁnition is not a good one in general because it’s possible
to have γ
+(∂A1) ̸= γ
+(∂A2) for some sets A1 and A2 that are equivalent up to
measure 0. (For more information, see Exercise 11.15 and the notes at the
end of this chapter.)

As mentioned above, one “correct” deﬁnition is surfγ(A) = p
π/2 · RS
′
A(0+).
This deﬁnition has the advantage of being insensitive to measure-0 changes
to A. To connect this unusual-looking deﬁnition with Minkowski content,
let’s heuristically interpret RS
′
A(0+). We start by thinking of it as RSA(ϵ)
ϵ for
“inﬁnitesimal ϵ”. Now RSA(ϵ) can be thought of as the probability that the line
segment ℓ joining two cos ϵ-correlated Gaussians crosses ∂A. Since sin ϵ ≈ ϵ,
cos ϵ ≈ 1 up to O(ϵ2), we can think of these correlated Gaussians as g and
g + ϵg′ for independent g, g′ ∼ N(0, 1)n. When g lands near ∂A, the length
of ℓ in the direction perpendicular to ∂A will, in expectation, be ϵ E[|N(0, 1)|] =p
2/πϵ. Thus RSA(ϵ) should essentially be 1
2 volγ({z : dist(z, ∂A) < p
2/πϵ}) and
we have heuristically justiﬁed

p
π/2 · RS
′
A(0
+) = p
π/2 · lim
ϵ→0+ RSA(ϵ)

ϵ
 ?
= γ
+(∂A). (11.14)

One more standard idea for the deﬁnition of surfγ(A) is “E[∥∇1A∥]”. This
doesn’t quite make sense since 1A ∈ L1(R n, γ) is not actually differentiable.
However, we might consider replacing it with the limit of E[∥∇ f m∥] for a
sequence ( f m) of smooth functions approximating 1A. To see why this notion
should agree with the Gaussian Minkowski content γ
+(∂A) for nice enough A,
let’s suppose we have a smooth approximator f to 1A that agrees with 1A on
{z : dist(z, ∂A) ≥ ϵ/2} and is (essentially) a linear function on {z : dist(z, ∂A) <
ϵ/2}. Then ∥∇ f ∥ will be 0 on the former set and (essentially) constantly 1/ϵ
on the latter (since it must climb from 0 to 1 over a distance of ϵ). Thus we
indeed have
 E[∥∇ f ∥] ≈ volγ({z : dist(z, ∂A) < ϵ/2})

ϵ ≈ γ
+(∂A),

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.4. Gaussian surface area and Bobkov’s Inequality 345

as desired. We summarize the above technical discussion with the following
deﬁnition/theorem, which is discussed further in the notes at the end of this
chapter:

Deﬁnition 11.48. For any A ⊆ R n, we deﬁne its Gaussian surface area to be

surfγ(A) = p
π/2 · RS
′
A(0
+) ∈ [0, ∞].

An equivalent deﬁnition is

surfγ(A) = inf {
lim inf
m→∞ E
z∼N(0,1)n[∥∇ f m(z)∥]} ,

where the inﬁmum is over all sequences ( f m)m∈N of smooth f m : R n → [0, 1]
with ﬁrst partial derivatives in L2(R n, γ) such that ∥ f m − 1A∥1 → 0. Further-
more, this inﬁmum is actually achieved by taking f m = Uρm f for any sequence
ρm → 1−. Finally, the equality surfγ(A) = γ
+(∂A) with Gaussian Minkowski
content holds if A is a disjoint union of closed, full-dimensional, convex sets.

To get further acquainted with this deﬁnition, let’s describe the Gaussian
surface area of some basic sets. We start with halfspaces, which as men-
tioned in Remark 11.47 have Gaussian surface area given by the Gaussian
isoperimetric function.

Proposition 11.49. Let H ⊆ R n be any halfspace (open or closed) with volγ(H) =
α ∈ (0, 1). Then surfγ(H) = U (α) = ϕ(Φ−1(α)). In particular, if α = 1/2 – i.e., H’s
boundary contains the origin – then surfγ(H) = 1p
2π .

Proof. Just as in the proof of Corollary 11.20, by rotational symmetry we
may assume H is a 1-dimensional halﬂine, H = (−∞, t]. Since volγ(H) = α, we
have t = Φ−1(α). Then surfγ(H) is equal to

γ
+(∂H) = lim
ϵ→0+ volγ({z ∈ R : dist(z, ∂H) < ϵ
2 })

ϵ = lim
ϵ→0+
 ∫ t+ϵ/2
t−ϵ/2 ϕ(s) ds

ϵ = ϕ(t) = U (α).

□

Here are some more Gaussian surface area bounds:

Example 11.50. In Exercise 11.16 you are asked to generalize the above
computation and show that if A ⊆ R is the union of disjoint nondegenerate in-
tervals [t1, t2], [t3, t4], . . . , [t2m−1, t2m] then surfγ(A) = ∑2m
i=1 ϕ(ti). Perhaps the
next easiest example is when A ⊆ R n is an origin-centered ball; Ball [Bal93]
gave an explicit formula for surfγ(A) in terms of the dimension and radius,

one which is always less than √ 2
π (see Exercise 11.17). This upper bound
was extended to non-origin-centered balls in Klivans et al. [KOS08]. Ball also
showed that every convex set A ⊆ R n satisﬁes surfγ(A) ≤ O(n1/4); Nazarov
[Naz03] showed that this bound is tight up to the constant, using a construc-
tion highly reminiscent of Talagrand’s Exercise 4.18. As noted in Klivans

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

346 11. Gaussian space and Invariance Principles

et al. [KOS08], Nazarov’s work also immediately implies that an intersection
of k halfspaces has Gaussian surface area at most O(
√
log k) (tight for appro-
priately sized cubes in R k), and that any cone in R n with apex at the origin
has Gaussian surface area at most 1. Finally, by proving the “Gaussian spe-
cial case” of the Gotsman–Linial Conjecture, Kane [Kan11] established that
if A ⊆ R n is a degree-k “polynomial threshold function” – i.e., A = {z : p(z) > 0}
for p an n-variate degree-k polynomial – then surfγ(A) ≤ kp
2π . This is tight
for every k (even when n = 1).

Though we’ve shown that the Gaussian Isoperimetric Inequality follows
from Borell’s Isoperimetric Theorem, we now discuss some alternative proofs.
In the special case of sets of Gaussian volume 1
2 , we can again get a very
simple proof using the subadditivity property of Gaussian rotation sensitivity,
Theorem 11.43. That result easily yields the following kind of “concavity
property” concerning Gaussian surface area:

Theorem 11.51. Let A ⊆ R n. Then for any δ > 0,

p
π/2 · RSA(δ)

δ ≤ surfγ(A).

Proof. For δ > 0 and ϵ = δ/ℓ, ℓ ∈ N +, Theorem 11.43 is equivalent to

RSA(δ)

δ ≤ RSA(ϵ)

ϵ .

Taking ℓ → ∞ hence ϵ → 0+, the right-hand side becomes RS
′
A(0+) = p
2/π ·
surfγ(A). □

If we take δ = π/2 in this theorem, the left-hand side becomes
p
2/π Pr
z,z′∼N(0,1)n
independent
[1A(z) ̸= 1A(z′)] = 2
p
2/π · volγ(A)(1 − volγ(A)).

Thus we obtain a simple proof of the following result, which includes the
Gaussian Isoperimetric Inequality in the volume- 1
2 case:

Theorem 11.52. Let A ⊆ R n. Then

2
p
2/π · volγ(A)(1 − volγ(A)) ≤ surfγ(A).

In particular, if volγ(A) = 1
2 , then we get the tight Gaussian Isoperimetric
Inequality statement surfγ(A) ≥ 1p
2π = U ( 1
2 ).

As for the full Gaussian Isoperimetric Inequality, it’s a pleasing fact that
it can be derived by pure analysis of Boolean functions. This was shown
by Bobkov [Bob97], who proved the following very interesting isoperimetric
inequality about Boolean functions:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.4. Gaussian surface area and Bobkov’s Inequality 347

Bobkov’s Inequality. Let f : {−1, 1}n → [0, 1]. Then

U (E[ f ]) ≤ E
x∼{−1,1}n [∥(U ( f (x)), ∇ f (x))∥] . (11.15)

Here ∇ f is the discrete gradient (as in Deﬁnition 2.34) and ∥ · ∥ is the usual
Euclidean norm (in R n+1). Thus to restate the inequality,

U (E[ f ]) ≤ E
x∼{−1,1}n
 [√

U ( f (x))2 + n∑

i=1 Di f (x)2]
 .

In particular, suppose f = 1A is the 0-1 indicator of a subset A ⊆ {−1, 1}n. Then
since U (0) = U (1) = 0 we obtain U (E[1A]) ≤ E[∥∇1A∥].

As Bobkov noted, by the usual Central Limit Theorem argument one can
straightforwardly obtain inequality (11.15) in the setting of functions f ∈
L2(R n, γ) with range [0, 1], provided f is sufﬁciently smooth (for example, if f
is in the domain of L; see Exercise 11.18). Then given A ⊆ R n, by taking a
sequence of smooth approximations to 1A as in Deﬁnition 11.48, the Gaussian
Isoperimetric Inequality U (E[1A]) ≤ surfγ(A) is recovered.

Given A ⊆ {−1, 1}n we can write the quantity E[∥∇1A∥] appearing in
Bobkov’s Inequality as

E[∥∇1A∥] = 1
2 · E
x∼{−1,1}n[√
sensA(x)]
, (11.16)

using the fact that for 1A : {−1, 1}n → {0, 1} we have

Di1A(x)
2 = 1
4 · 1[coordinate i is pivotal for 1A on x].

The quantity in (11.16) – (half of) the expected square-root of the number of
pivotal coordinates – is an interesting possible notion of “Boolean surface area”
for sets A ⊆ {−1, 1}n. It was ﬁrst essentially proposed by Talagrand [Tal93].
By Cauchy–Schwarz it’s upper-bounded by (half of) the square-root of our
usual notion of boundary size, average sensitivity:

E[∥∇1A∥] ≤ √E[∥∇1A∥2] = √I[1A]. (11.17)

(Note that I[1A] here is actually one quarter of the average sensitivity of A,
because we’re using 0-1 indicators as opposed to ±1). But the inequality
in (11.17) is often far from sharp. For example, while the majority function has
average sensitivity Θ(pn), the expected square-root of its sensitivity is Θ(1)
because a Θ(1/
pn)-fraction of strings have sensitivity ⌈n/2⌉ and the remainder
have sensitivity 0.

Let’s turn to the proof of Bobkov’s Inequality. As you are asked to show
in Exercise 11.20, the general-n case of Bobkov’s Inequality follows from the
n = 1 case by a straightforward “induction by restrictions”. Thus just as in
the proof of the Hypercontractivity Theorem, it sufﬁces to prove the n = 1
“two-point inequality”, an elementary inequality about two real numbers:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

348 11. Gaussian space and Invariance Principles

Bobkov’s Two-Point Inequality. Let f : {−1, 1} → [0, 1]. Then

U (E[ f ]) ≤ E[∥(U ( f ), ∇ f )∥].

Writing f (x) = a + bx, this is equivalent to saying that provided a ± b ∈ [0, 1],

U (a) ≤ 1
2 ∥(U (a + b), b)∥ + 1
2 ∥(U (a − b), b)∥.

Remark 11.53. The only property of U used in proving this inequality is
that it satisﬁes (Exercise 5.43) the differential equation U U ′′ = −1 on (0, 1).

Bobkov’s proof of the two-point inequality was elementary but somewhat
long and hard to motivate. In contrast, Barthe and Maurey [BM00] gave
a fairly short proof of the inequality, but it used methods from stochastic
calculus, namely Itô’s Formula. We present here an elementary discretization
of the Barthe–Maurey proof.

Proof of Bobkov’s Two-Point Inequality. By symmetry and continuity we
may assume δ ≤ a − b < a + b ≤ 1 − δ for some δ > 0. Let τ = τ(δ) > 0 be a small
quantity to be chosen later such that b/τ is an integer. Let y0, y1, y2, . . . be
a random walk within [a − b, a + b] that starts at y0 = a, takes independent
equally likely steps of ±τ, and is absorbed at the endpoints a ± b. Finally, for
t ∈ N , deﬁne zt = ∥(U (yt), τpt)∥. The key claim for the proof is:

Claim 11.54. Assuming τ = τ(δ) > 0 is small enough, (zt)t is a submartingale
with respect to (yt)t, i.e., E[zt+1 | y0, . . . , yt] = E[zt+1 | yt] ≥ zt.

Let’s complete the proof given the claim. Let T be the stopping time at
which yt ﬁrst reaches a ± b. By the Optional Stopping Theorem we have
E[z0] ≤ E[zT ]; i.e.,
 U (a) ≤ E[∥(U (zT ), τpT)∥]. (11.18)

In the expectation above we can condition on whether the walk stopped at
a+ b or a− b. By symmetry, both events occur with probability 1/2 and neither
changes the conditional distribution of T. Thus we get

U (a) ≤ 1
2 E[∥(U (a + b), τpT)∥] + 1
2 E[∥(U (a − b), τpT)∥]

≤ 1
2 ∥(U (a + b), √
E[τ2T])∥ + 1
2 ∥(U (a − b), √
E[τ2T])∥,

with the second inequality using concavity of v 7→ pu2 + v. But it’s a well-
known fact (following immediately from Exercise 11.22) that E[T] = (b/τ)2.
Substituting this into the above completes the proof.

It remains to verify Claim 11.54. Actually, although the claim is true
as stated (see Exercise 11.23) it will be more natural to prove the following
slightly weaker claim: E[zt+1 | yt] ≥ zt − Cδτ3 (11.19)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.4. Gaussian surface area and Bobkov’s Inequality 349

for some constant Cδ depending only on δ. This is still enough to com-
plete the proof: Applying the Optional Stopping Theorem to the submartin-
gale (zt + Cδτ3t)t we get that (11.18) holds up to an additive Cδτ3 E[T] =
Cδb2τ. Then continuing with the above we deduce Bobkov’s Inequality up
to Cδb2τ, and we can make τ arbitrarily small.

Even though we only need to prove (11.19), let’s begin a proof of the
original Claim 11.54 anyway. Fix t ∈ N + and condition on yt = y. If y is a ± b,
then the walk is stopped and the claim is clear. Otherwise, yt+1 is y ± τ with
equal probability, and we want to verify the following inequality (assuming
τ > 0 is sufﬁciently small as a function of δ, independent of y):

∥(U (y), τpt)∥ ≤ 1
2 ∥(U (y + τ), τpt + 1)∥ + 1
2 ∥(U (y − τ), τpt + 1)∥ (11.20)

= 1
2 ∥
∥
(√U (y + τ)2 + τ2, τpt)∥
∥ + 1
2 ∥
∥
(√
U (y − τ)2 + τ2, τpt)∥
∥.

By the triangle inequality, it’s sufﬁcient to show

U (y) ≤ 1
2
 √U (y + τ)2 + τ2 + 1
2
 √
U (y − τ)2 + τ2,

and this is actually necessary too, being the t = 0 case of (11.20). (In fact,
this is identical to Bobkov’s Two-Point Inequality itself, except now we may
assume τ is sufﬁciently small.) Finally, since we actually only need the weak-
ened submartingale statement (11.19), we’ll instead establish

U (y) − Cδτ3 ≤ 1
2
 √
U (y + τ)2 + τ2 + 1
2
 √U (y − τ)2 + τ2 (11.21)

for some constant Cδ depending only on δ and for every τ ≤ δ
2 . We do this
using Taylor’s theorem. Write Vy(τ) for the function of τ on the right-hand
side of (11.21). For any y ∈ [a − b, a + b] the function Vy is smooth on [0, δ
2 ]
because U is a smooth, positive function on [ δ
2 , 1 − δ
2 ]. Thus

Vy(τ) = Vy(0) + V ′
y(0)τ + 1
2 V ′′
y (0)τ2 + 1
6 V ′′′
y (ξ)τ3

for some ξ between 0 and τ. The magnitude of V ′′′
y (ξ) is indeed bounded by
some Cδ depending only on δ, using the fact that U is smooth and positive on
[ δ
2 , 1 − δ
2 ]. But Vy(0) = U (y), and it’s straightforward to calculate that

V ′
y(0) = 0, V ′′
y (0) = U ′′(y) + 1/U (y) = 0,

the last identity used the key property U ′′ = −1/U mentioned in Remark 11.53.
Thus we conclude Vy(τ) ≥ U (y) − Cδτ3, verifying (11.21) and completing the
proof. □

As a matter of fact, by a minor adjustment (Exercise 11.24) to this ran-
dom walk argument we can establish the following generalization of Bobkov’s
Inequality:
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

350 11. Gaussian space and Invariance Principles

Theorem 11.55. Let f : {−1, 1}n → [0, 1]. Then E[∥(U (Tρ f ), ∇Tρ f )∥] is an
increasing function of ρ ∈ [0, 1]. We recover Bobkov’s Inequality by considering
ρ = 0, 1.

We end this section by remarking that De, Mossel, and Neeman [DMN13]
have given a “Bobkov-style” Boolean inductive proof that yields both Borell’s
Isoperimetric Theorem and also the Majority Is Stablest Theorem (albeit with
some aspects of the Invariance Principle-based proof appearing in the latter
case); see Exercise 11.30 and the notes at the end of this chapter.

11.5. The Berry–Esseen Theorem

Now that we’ve built up some results concerning Gaussian space, we’re mo-
tivated to try reducing problems involving Boolean functions to problems
involving Gaussian functions. The key tool for this is the Invariance Princi-
ple, discussed at the beginning of the chapter. As a warmup, this section is
devoted to proving (a form of) the Berry–Esseen Theorem. As discussed in
Chapter 5.2, the Berry–Esseen Theorem is a quantitative form of the Central
Limit Theorem for ﬁnite sums of independent random variables. We restate
it here:

Berry–Esseen Theorem. Let X 1, . . . , X n be independent random variables
with E[X i] = 0 and Var[X i] = σ2
i , and assume ∑n
i=1 σ2
i = 1. Let S = ∑n
i=1 X i
and let Z ∼ N(0, 1) be a standard Gaussian. Then for all u ∈ R ,

| Pr[S ≤ u] − Pr[Z ≤ u]| ≤ cγ,

where
 γ = n∑

i=1 ∥X i∥
3
3

and c is a universal constant. (For deﬁniteness, c = .56 is acceptable.)

In this traditional statement of Berry–Esseen, the error term γ is a little
opaque. To say that γ is small is to simultaneously say two things: the random
variables X i are all “reasonable” (as in Chapter 9.1); and, none is too domi-
nant in terms of variance. In Chapter 9.1 we discussed several related notions
of “reasonableness” for a random variable X . It was convenient there to use
the deﬁnition that ∥X ∥
4
4 is not much larger than ∥X ∥
4
2. For the Berry–Esseen
Theorem it’s more convenient (and slightly stronger) to use the analogous
condition for the 3rd moment. (For the Invariance Principle it will be more
convenient to use (2, 3, ρ)- or (2, 4, ρ)-hypercontractivity.) The implication for
Berry–Esseen is the following:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.5. The Berry–Esseen Theorem 351

Remark 11.56. In the Berry–Esseen Theorem, if all of the X i’s are “reason-
able” in the sense that ∥X i∥
3
3 ≤ B∥X i∥
3
2 = Bσ3
i , then we can use the bound

γ ≤ B · max
i {σi}, (11.22)

as this is a consequence of

γ = n∑

i=1 ∥X i∥
3
3 ≤ B n∑

i=1 σ3
i ≤ B · max
i {σi} · n∑

i=1 σ2
i = B · max
i {σi}.

(Cf. Remark 5.15.) Note that some “reasonableness” condition must hold if
S = ∑i X i is to behave like a Gaussian. For example, if each X i is the “unrea-
sonable” random variable which is ±
pn with probability 1
2n2 each and 0 other-
wise, then S = 0 except with probability at most 1
n – quite unlike a Gaussian.
Further, even assuming reasonableness we still need a condition like (11.22)
ensuring that no X i is too dominant (“inﬂuential”) in terms of variance. For
example, if X 1 ∼ {−1, 1} is a uniformly random bit and X 2, . . . , X n ≡ 0, then
S ≡ X 1, which is again quite unlike a Gaussian.

There are several known ways to prove the Berry–Esseen Theorem; for ex-
ample, using characteristic functions (i.e., “real” Fourier analysis), or Stein’s
Method. We’ll use the “Replacement Method” (also known as the Lindeberg
Method, and similar to the “Hybrid Method” in theoretical cryptography). Al-
though it doesn’t always give the sharpest results, it’s a very ﬂexible technique
which generalizes easily to higher-degree polynomials of random variables (as
in the Invariance Principle) and random vectors. The Replacement Method
suggests itself as soon as the Berry–Esseen Theorem is written in a slightly
different form: Instead of trying to show

X 1 + X 2 + · · · + X n ≈ Z, (11.23)

where Z ∼ N(0, 1), we’ll instead try to show the equivalent statement

X 1 + X 2 + · · · + X n ≈ Z1 + Z2 + · · · + Z n, (11.24)

where the Z i’s are independent Gaussians with Z i ∼ N(0, σ2
i ). The state-
ments (11.23) and (11.24) really are identical, since the sum of independent
Gaussians is Gaussian, with the variances adding. The Replacement Method
proves (11.24) by replacing the X i’s with Z i’s one by one. Roughly speaking,
we introduce the “hybrid” random variables

H t = Z1 + · · · + Z t + X t+1 + · · · + X n,

show that H t−1 ≈ H t for each t ∈ [n], and then simply add up the n errors.

As a matter of fact, the Replacement Method doesn’t really have anything
to do with Gaussian random variables. It actually seeks to show that

X 1 + X 2 + · · · + X n ≈ Y 1 + Y 2 + · · · + Y n

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

352 11. Gaussian space and Invariance Principles

whenever X 1, . . . , X n, Y 1, . . . , Y n are independent random variables with “match-
ing ﬁrst and second moments”, meaning E[X i] = E[Y i] and E[X 2
i ] = E[Y 2
i ] for
each i ∈ [n]. (The error will be proportional to ∑i(∥X i∥
3 + ∥Y i∥
3
3).) Another
way of putting it (roughly speaking) is that the linear form x1 + · · · + xn is in-
variant to what independent random variables you substitute in for x1, . . . , xn,
so long as you always use the same ﬁrst and second moments. The fact that
we can take the Y i’s to be Gaussians (with Y i ∼ N(E[X i], Var[X i])) and then
in the end use the fact that the sum of Gaussians is Gaussian to derive the
simpler-looking
 S = n∑

i=1 X i ≈ N(E[S], Var[S])

is just a pleasant bonus (and one that we’ll no longer get once we look at
nonlinear polynomials of random variables in Section 11.6). Indeed, the re-
mainder of this section will be devoted to showing that

S X = X 1 + · · · + X n is “close” to SY = Y 1 + · · · + Y n

whenever the X i’s and Y i’s are independent, “reasonable” random variables
with matching ﬁrst and second moments.

To do this, we’ll ﬁrst have to discuss in more detail what it means for two
random variables to be “close”. A traditional measure of closeness between
two random variables S X and SY is the “cdf-distance” used in the Berry–
Esseen Theorem: Pr[S X ≤ u] ≈ Pr[SY ≤ u] for every u ∈ R . But there are
other natural measures of closeness too. We might want to know that the
absolute moments of S X and SY are close; for example, that ∥S X ∥1 ≈ ∥SY ∥1.
Or, we might like to know that S X and SY stray from the interval [−1, 1]
by about the same amount: E[dist[−1,1](S X )] ≈ E[dist[−1,1](SY )]. Here we are
using:

Deﬁnition 11.57. For any interval ; ̸= I ⊊ R the function distI : R → R ≥0 is
deﬁned to measure the distance of a point from I; i.e., distI (s) = infu∈I {|s − u|}.

All of the closeness measures just described can be put in a common frame-
work: they are requiring E[ψ(S X )] ≈ E[ψ(SY )] for various “test functions” (or
“distinguishers”) ψ : R → R .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.5. The Berry–Esseen Theorem 353

Figure 11.1. The test functions ψ used for judging Pr[S X ≤ u] ≈ Pr[SY ≤
u], ∥S X ∥1 ≈ ∥SY ∥1, and E[dist[−1,1](S X )] ≈ E[dist[−1,1](SY )], respectively

It would be nice to prove a version of the Berry–Esseen Theorem that
showed closeness for all the test functions ψ depicted in Figure 11.1, and
more. What class of tests might we able to handle? On one hand, we can’t be
too ambitious. For example, suppose each X i ∼ {−1, 1}, each Y i ∼ N(0, 1), and
ψ(s) = 1s∈Z . Then E[ψ(S X )] = 1 because S X is supported on the integers, but
E[ψ(SY )] = 0 because SY ∼ N(0, n) is a continuous random variable. On the
other hand, there are some simple kinds of tests ψ for which we have exact
equality. For example, if ψ(s) = s, then E[ψ(S X )] = E[ψ(SY )]; this is by the
assumption of matching ﬁrst moments, E[X i] = E[Y i] for all i. Similarly, if
ψ(s) = s2, then

E[ψ(S X )] = E
[(∑

i X i)2] = ∑

i E[X 2
i ] + ∑

i̸= j E[X i X j]

= ∑

i E[X 2
i ] + ∑

i̸= j E[X i] E[X j] (11.25)

(using independence of the X i’s); and also

E[ψ(SY )] = ∑

i E[Y 2
i ] + ∑

i̸= j E[Y i] E[Y j]. (11.26)

The quantities (11.25) and (11.26) are equal because of the matching ﬁrst and
second moment conditions.

As a consequence of these observations we have E[ψ(S X )] = E[ψ(SY )] for
any quadratic polynomial ψ(s) = a + bs + cs2. This suggests that to handle
a general test ψ we try to approximate it by a quadratic polynomial up to
some error; in other words, consider its 2nd-order Taylor expansion. For this
to make sense the function ψ must have a continuous 3rd derivative, and
the error we incur will involve the magnitude of this derivative. Indeed, we
will now prove a variant of the Berry–Esseen Theorem for the class of C 3

test functions ψ with ψ
′′′ uniformly bounded. You might be concerned that
this class doesn’t contain any of the interesting test functions depicted in
Figure 11.1. But we’ll be able to handle even those test functions with some
loss in the parameters by using a simple “hack” – approximating them by
smooth functions, as suggested in Figure 11.2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

354 11. Gaussian space and Invariance Principles

Figure 11.2. The step function ψ(s) = 1s≤u can be smoothed out on the
interval [u − η, u + η] so that the resulting function ̃ψη satisﬁes ∥ ̃ψ′′′
η ∥∞ ≤

O(1/η3). Similarly, we can smooth out ψ(s) = dist[−1,1](s) to a function ̃ψη
satisfying ∥ψ − ̃ψ∥∞ ≤ η and ∥ ̃ψ′′′
η ∥∞ ≤ O(1/η2).

Invariance Principle for Sums of Random Variables. Let X 1, . . . , X n,
Y 1, . . . , Y n be independent random variables with matching 1st and 2nd mo-
ments; i.e., E[X k
i ] = E[Y k
i ] for i ∈ [n], k ∈ {1, 2}. Write S X = ∑i X i and SY =
∑i Y i. Then for any ψ : R → R with continuous third derivative,
∣
∣E[ψ(S X )] − E[ψ(SY )]∣
∣ ≤ 1
6 ∥ψ′′′∥∞ · γX Y ,

where γX Y = ∑i(∥X i∥3
3 + ∥Y i∥
3
3).

Proof. The proof is by the Replacement Method. For 0 ≤ t ≤ n, deﬁne the
“hybrid” random variable

H t = Y 1 + · · · + Y t + X t+1 + · · · + X n,

so S X = H0 and SY = H n. Thus by the triangle inequality,
∣
∣E[ψ(S X )] − E[ψ(SY )]∣
∣ ≤ n∑

t=1
 ∣
∣E[ψ(H t−1)] − E[ψ(H t)]∣
∣ .

Given the deﬁnition of γX Y , we can complete the proof by showing that for
each t ∈ [n],

1
6 ∥ψ
′′′∥∞ · (E[|X t|3] + E[|Y t|3]) ≥ ∣
∣E[ψ(H t−1)] − E[ψ(H t)]∣
∣

= ∣
∣E[ψ(H t−1) − ψ(H t)]∣
∣

= ∣
∣E[ψ(U t + X t) − ψ(U t + Y t)]
∣
∣ , (11.27)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.5. The Berry–Esseen Theorem 355

where
 U t = Y 1 + · · · + Y t−1 + X t+1 + · · · + X n.

Note that U t is independent of X t and Y t. We are now comparing ψ’s values
at U t + X t and U t +Y t, with the presumption that X t and Y t are rather small
compared to U t. This clearly suggests the use of Taylor’s theorem: For all
u, δ ∈ R ,
 ψ(u + δ) = ψ(u) + ψ
′(u)δ + 1
2 ψ′′(u)δ2 + 1
6 ψ
′′′(u∗)δ3,

for some u∗ = u∗(u, δ) between u and u + δ. Applying this pointwise with
u = U t, δ = X t, Y t yields

ψ(U t + X t) = ψ(U t) + ψ
′(U t)X t + 1
2 ψ
′′(U t)X 2
t + 1
6 ψ′′′(U ∗
t )X 3
t

ψ(U t + Y t) = ψ(U t) + ψ′(U t)Y t + 1
2 ψ
′′(U t)Y 2
t + 1
6 ψ
′′′(U ∗∗
t )Y 3
t

for some random variables U ∗
t ,U ∗∗
t . Referring back to our goal of (11.27),
what happens when we subtract these two identities and take expectations?
The ψ(U t) terms cancel. The next difference is

E[ψ′(U t)(X t − Y t)] = E[ψ′(U t)] · E[X t − Y t] = E[ψ
′(U t)] · 0 = 0,

where the ﬁrst equality used that U t is independent of X t and Y t, and the
second equality used the matching 1st moments of X t and Y t. An identical
argument, using matching 2nd moments, shows that the shows that the dif-
ference of the quadratic terms disappears in expectation. Thus we’re left only
with the “error term”:
∣
∣E[ψ(U t + X t) − ψ(U t + Y t)]
∣
∣ = 1
6 ∣
∣E[ψ′′′(U ∗
t )X 3
t − ψ
′′′(U ∗∗
t )Y 3
t ]
∣
∣

≤ 1
6 ∥ψ
′′′∥∞ · (E[|X t|3] + E[|Y t|3]),

where the last step used the triangle inequality. This conﬁrms (11.27) and
completes the proof. □

We can now give a Berry–Esseen-type corollary by taking the Y i’s to be
Gaussians:

Variant Berry–Esseen Theorem. In the setting of the Berry–Esseen Theo-
rem, for all C 3 functions ψ : R → R ,

∣
∣E[ψ(S)] − E[ψ(Z)]∣
∣ ≤ 1
6 (1 + 2√ 2
π )∥ψ′′′∥∞ · γ ≤ .433∥ψ
′′′∥∞ · γ.

Proof. Applying the preceding theorem with Y i ∼ N(0, σ2
i ) (and hence SY ∼
N(0, 1)), it sufﬁces to show that

γX Y = n∑

i=1(∥X i∥3
3 + ∥Y i∥
3
3) ≤ (1 + 2√ 2
π ) · γ = (1 + 2
√ 2
π ) · n∑

i=1 ∥X i∥
3
3. (11.28)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

356 11. Gaussian space and Invariance Principles

In particular, we just need to show that ∥Y i∥
3
3 ≤ 2√ 2
π ∥X i∥
3
3 for each i. This
holds because Gaussians are extremely reasonable; by explicitly computing
3rd absolute moments we indeed obtain

∥Y i∥
3
3 = σ3
i ∥N(0, 1)∥3
3 = 2√ 2
π σ3
i = 2√ 2
π ∥X i∥
3
2 ≤ 2√ 2
π ∥X i∥
3
3. □

This version of the Berry–Esseen Theorem is incomparable with the stan-
dard version. Sometimes it can be stronger; for example, if for some reason
we wanted to show E[cos S] ≈ E[cos Z] then the Variant Berry–Esseen Theo-
rem gives this with error .433γ, whereas it can’t be directly deduced from the
standard Berry–Esseen at all. On the other hand, as we’ll see shortly, we can
only obtain the standard Berry–Esseen conclusion from the Variant version
with an error bound of O(γ
1/4) rather than O(γ).

We end this section by describing the “hacks” which let us extend the
Variant Berry–Esseen Theorem to cover certain non-C 3 tests ψ. As mentioned
the idea is to smooth them out, or “mollify” them:

Proposition 11.58. Let ψ : R → R be c-Lipschitz. Then for any η > 0 there
exists ̃ψη : R → R satisfying ∥ψ − ̃ψη∥∞ ≤ cη and ∥ ̃ψ
(k)
η ∥∞ ≤ Ck c/ηk−1 for each

k ∈ N +. Here Ck is a constant depending only on k, and ̃ψ(k)
η denotes the kth
derivative of ̃ψη.

The proof of this proposition is straightforward, taking ̃ψη(s) = E
g∼N(0,1)
[ψ(s +

ηg)]; see Exercise 11.38.

As η → 0 this gives a better and better smooth approximation to ψ, but
also a larger and larger value of ∥ ̃ψ
′′′
η ∥∞. Trading these off gives the following:

Corollary 11.59. In the setting of the Invariance Principle for Sums of Ran-
dom Variables, if we merely have that ψ : R → R is c-Lipschitz, then
∣
∣E[ψ(S X )] − E[ψ(SY )]∣
∣ ≤ O(c) · γ
1/3
X Y .

Proof. Applying the Invariance Principle for Sums of Random Variables with
the test ̃ψη from Proposition 11.58 we get
∣
∣E[ ̃ψη(S X )] − E[ ̃ψη(SY )]
∣
∣ ≤ O(c/η
2) · γX Y .

But ∥ ̃ψη − ψ∥∞ ≤ cη implies
∣
∣E[ ̃ψη(S X )] − E[ψ(S X )]∣
∣ ≤ E[| ̃ψη(S X ) − ψ(S X )|] ≤ cη

and similarly for SY . Thus we get
∣
∣E[ψ(S X )] − E[ψ(SY )]∣
∣ ≤ O(c) · (η + γX Y /η
2)

which yields the desired bound by taking η = γ
1/3
X Y . □

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.6. The Invariance Principle 357

Remark 11.60. It’s obvious that the dependence on c in this theorem should
be linear in c; in fact, since we can always divide ψ by c it would have sufﬁced
to prove the theorem assuming c = 1.

This corollary covers all Lipschitz tests, which sufﬁces for the functions
ψ(s) = |s| and ψ(s) = dist[−1,1](s) from Figure 11.1. However, it still isn’t
enough for the test ψ(s) = 1s≤u – i.e., for establishing cdf-closeness as in the
usual Berry–Esseen Theorem. Of course, we can’t hope for a smooth approxi-
mator ̃ψη satisfying | ̃ψη(s)−1s≤u| ≤ η for all s because of the discontinuity at u.
However, as suggested in Figure 11.2, if we’re willing to exclude s ∈ [u−η, u+η]
we can get an approximator with third derivative bound O(1/η
3), and thereby
obtain (Exercises 11.41, 11.42):

Corollary 11.61. In the setting of the Invariance Principle for Sums of Ran-
dom Variables, for all u ∈ R we have

Pr[SY ≤ u − ϵ] − ϵ ≤ Pr[S X ≤ u] ≤ Pr[SY ≤ u + ϵ] + ϵ

for ϵ = O(γ
1/4
X Y ); i.e., S X and SY have Lévy distance dL(S X , SY ) ≤ O(γ
1/4
X Y ).

Finally, in the Berry–Esseen setting where SY ∼ N(0, 1), we can appeal to
the “anticoncentration” of Gaussians:

Pr[N(0, 1) ≤ u+ϵ] = Pr[N(0, 1) ≤ u]+Pr[u < N(0, 1) ≤ u+ϵ] ≤ Pr[N(0, 1) ≤ u]+ ϵp
2π ,

and similarly for Pr[N(0, 1) ≤ u − ϵ]. This lets us convert the Lévy distance
bound into a cdf-distance bound. Recalling (11.28), we immediately deduce
the following weaker version of the classical Berry–Esseen Theorem:

Corollary 11.62. In the setting of the Berry–Esseen Theorem, for all u ∈ R ,

|Pr[S ≤ u] − Pr[Z ≤ u| ≤ O(γ
1/4),

where the O(·) hides a universal constant.

Although the error bound here is weaker than necessary by a power of 1/4,
this weakness will be more than made up for by the ease with which the
Replacement Method generalizes to other settings. In the next section we’ll
see it applied to nonlinear polynomials of independent random variables. Ex-
ercise 11.46 outlines how to use it to give a Berry–Esseen theorem for sums
of independent random vectors; as you’ll see, other than replacing Taylor’s
theorem with its multivariate form, hardly a symbol in the proof changes.

11.6. The Invariance Principle

Let’s summarize the Variant Berry–Esseen Theorem and proof from the pre-
ceding section, using slightly different notation. (Speciﬁcally, we’ll rewrite
X i = ai xi where Var[xi] = 1, so ai = ±σi.) We showed that if x1, . . . , xn, y1, . . . , yn

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

358 11. Gaussian space and Invariance Principles

are independent mean-0, variance-1 random variables, reasonable in the
sense of having third absolute moment at most B, and if a1, . . . , an are real
constants assumed for normalization to satisfy ∑i a2
i = 1, then

a1x1 + · · · + an xn ≈ a1 y1 + · · · + an yn,

with error bound proportional to B max{|ai|}.

We think of this as saying that the linear form a1x1 + · · · + an xn is (roughly)
invariant to what independent mean-0, variance-1, reasonable random vari-
ables are substituted for the xi’s, so long as all |ai|’s are “small” (compared to
the overall variance). In this section we generalize this statement to degree-
k multilinear polynomial forms, ∑|S|≤k aS xS. The appropriate generaliza-
tion of the condition that “all |ai|’s are small” is the condition that all “in-
ﬂuences” ∑S∋i a2
S are small. We refer to these nonlinear generalizations of
Berry–Esseen as Invariance Principles.

In this section we’ll develop the most basic Invariance Principle, which
involves replacing bits by Gaussians for a single Boolean function f . We’ll
show that this doesn’t change the distribution of f much provided f has small
inﬂuences and provided that f is of “constant degree” – or at least, provided f
is uniformly noise-stable so that it’s “close to having constant degree”. In-
variance Principles in much more general settings are possible – for example
Exercises 11.48 and 11.49 describe variants which handle several functions
applied to correlated inputs, and functions on general product spaces. Here
we’ll just focus on the simplest possible Invariance Principle, which is already
sufﬁcient for the proof of the Majority Is Stablest Theorem in Section 11.7.

Let’s begin with some notation.

Deﬁnition 11.63. Let F be a formal multilinear polynomial over the sequence
of indeterminates x = (x1, . . . , xn):

F(x) = ∑

S⊆[n] ̂F(S) ∏

i∈S xi,

where the coefﬁcients ̂F(S) are real numbers. We introduce the notation

Var[F] = ∑

S̸=; ̂F(S)2, Infi[F] = ∑

S∋i ̂F(S)2.

Remark 11.64. To justify this notation, we remark that we’ll always con-
sider F applied to a sequence z = (z1, . . . , zn) independent random variables
satisfying E[zi] = 0, E[z2
i ] = 1. Under these circumstances the collection of
monomial random variables ∏i∈S zi is orthonormal and so it’s easy to see
(cf. Chapter 8.2) that

E[F(z)] = ̂F(;), E[F(z)2] = ∑

S⊆[n] ̂F(S)2, Var[F(z)] = Var[F] = ∑

S̸=; ̂F(S)2.

We also have E[Varzi [F(z)]] = Infi[F] = ∑S∋i ̂F(S)
2, though we won’t use this.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.6. The Invariance Principle 359

As in the Berry–Esseen Theorem, to get good error bounds we’ll need our
random variables zi to be “reasonable”. Sacriﬁcing generality for simplicity
in this section, we’ll take the bounded 4th-moment notion from Deﬁnition 9.1
which will allow us to use the basic Bonami Lemma (more precisely, Corol-
lary 9.6):

Hypothesis 11.65. The random variable zi satisﬁes E[zi] = 0, E[z2
i ] = 1,
E[z3
i ] = 0, and is “9-reasonable” in the sense of Deﬁnition 9.1; i.e., E[z4
i ] ≤ 9.

The main examples we have in mind are that each zi is either a uniform ±1
random bit or a standard Gaussian. (There are other possibilities, though;
e.g., zi could be uniform on the interval [−
p
3, p
3].)

We can now prove the most basic Invariance Principle, for low-degree
multilinear polynomials of random variables:

Basic Invariance Principle. Let F be a formal n-variate multilinear poly-
nomial of degree at most k ∈ N ,

F(x) = ∑

S⊆[n],|S|≤k ̂F(S) ∏

i∈S xi.

Let x = (x1, . . . , xn) and y = (y1, . . . , yn) be sequences of independent random
variables, each satisfying Hypothesis 11.65. Assume ψ : R → R is C 4 with
∥ψ
′′′′∥∞ ≤ C. Then

∣
∣E[ψ(F(x))] − E[ψ(F(y))]
∣
∣ ≤ C
12 · 9k · n∑

t=1 Inft[F]2. (11.29)

Remark 11.66. The proof will be very similar to the one we used for Berry–
Esseen except that we’ll take a 3rd-order Taylor expansion rather than a
2nd-order one (so that we can use the easy Bonami Lemma). As you are asked
to show in Exercise 11.47, had we only required that ψ be C 3 and that the
xi’s and yi’s be (2, 3, ρ)-hypercontractive with 2nd moment equal to 1, then
we could obtain

∣
∣E[ψ(F(x))] − E[ψ(F(y))]
∣
∣ ≤ ∥ψ
′′′∥∞
3 · (1/ρ)
3k · n∑

t=1 Inft[F]3/2.

Proof. The proof uses the Replacement Method. For 0 ≤ t ≤ n we deﬁne

H t = F(y1, . . . , yt, xt+1, . . . , xn),

so F(x) = H0 and F(y) = H n. We will show that
∣
∣E[ψ(H t−1) − ψ(H t)]∣
∣ ≤ C
12 · 9k · Inft[F]2; (11.30)

as in our proof of the Berry–Esseen Theorem, this will complete the proof
after summing over t and using the triangle inequality. To analyze (11.30)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

360 11. Gaussian space and Invariance Principles

we separate out the part of F(x) that depends on xt; i.e., we write F(x) =
EtF(x) + xtDtF(x), where the formal polynomials EtF and DtF are deﬁned by

EtF(x) = ∑

S̸∋t ̂F(S) ∏

i∈S xi, DtF(x) = ∑

S∋t ̂F(S) ∏

i∈S\{t} xi.

Note that neither EtF nor DtF depends on the indeterminate xt; thus we can
deﬁne
 U t = EtF(y1, . . . , yt−1, ·, xt+1, . . . , xn),

∆∆∆t = DtF(y1, . . . , yt−1, ·, xt+1, . . . , xn),

so that H t−1 = U t +∆∆∆t xt, H t = U t +∆∆∆t yt.

We now use a 3rd-order Taylor expansion to bound (11.30):

ψ(H t−1) = ψ(U t) + ψ
′(U t)∆∆∆txt + 1
2 ψ
′′(U t)∆∆∆
2
t x2
t + 1
6 ψ
′′′(U t)∆∆∆
3
t x3
t + 1
24 ψ′′′′(U ∗
t )∆∆∆
4
t x4
t

ψ(H t) = ψ(U t) + ψ′(U t)∆∆∆t yt + 1
2 ψ
′′(U t)∆∆∆
2
t y2
t + 1
6 ψ′′′(U t)∆∆∆
3
t y3
t + 1
24 ψ′′′′(U ∗∗
t )∆∆∆
4
t y4
t

for some random variables U ∗
t and U ∗∗
t . As in the proof of the Berry–Esseen
Theorem, when we subtract these and take the expectation there are signiﬁ-
cant simpliﬁcations. The 0th-order terms cancel. As for the 1st-order terms,

E[ψ
′(U t)∆∆∆txt−ψ
′(U t)∆∆∆t yt] = E[ψ
′(U t)∆∆∆t·(xt− yt)] = E(ψ′(U t)∆∆∆t]·E[xt− yt] = 0.

The second equality here crucially uses the fact that xt, yt are independent of
U t, ∆∆∆t. The ﬁnal equality only uses the fact that xt and yt have matching 1st
moments (and not the stronger assumption that both of these 1st moments
are 0). The 2nd- and 3rd-order terms will similarly cancel, using the fact that
xt and yt have matching 2nd and 3rd moments. Finally, for the “error” term
we’ll just use |ψ
′′′′(U ∗
t )|, |ψ
′′′′(U ∗∗
t )| ≤ C and the triangle inequality; we thus
obtain ∣
∣E[ψ(H t−1) − ψ(H t)]∣
∣ ≤ C
24 · (E[(∆∆∆txt)
4] + E[(∆∆∆t yt)4]).

To complete the proof of (11.30) we now just need to bound

E[(∆∆∆txt)4], E[(∆∆∆t yt)
4] ≤ 9k · Inft[F]
2,

which we’ll do using the Bonami Lemma. We’ll give the proof for E[(∆∆∆txt)4],
the case of E[(∆∆∆t yt)
4] being identical. We have

∆∆∆txt = LtF(y1, . . . , yt−1, xt, xt+1, . . . , xn),

where LtF(x) = xtDtF(x) = ∑

S∋t ̂F(S) ∏

i∈S xi.

Since LtF has degree at most k we can apply the Bonami Lemma (more
precisely, Corollary 9.6) to obtain

E[(∆∆∆txt)
4] ≤ 9k E[LtF(y1, . . . , yt−1, xt, xt+1, . . . , xn)2]
2.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.6. The Invariance Principle 361

But since y1, . . . , yt−1, xt, . . . , xn are independent with mean 0 and 2nd mo-
ment 1, we have (see Remark 11.64)

E[LtF(y1, . . . , yt−1, xt, xt+1, . . . , xn)
2] = ∑

S⊆[n] ̂LtF(S)2 = ∑

S∋t ̂F(S)2 = Inft[F].

Thus we indeed have E[(∆∆∆txt)
4] ≤ 9k · Inft[F]
2, and the proof is complete. □

Corollary 11.67. In the setting of the preceding theorem, if we furthermore
have Var[F] ≤ 1 and Inft[F] ≤ ϵ for all t ∈ [n], then
∣
∣E[ψ(F(x))] − E[ψ(F(y))]
∣
∣ ≤ C
12 · k9k · ϵ.

Proof. We have ∑t Inft[F]
2 ≤ ϵ ∑t Inft[F] ≤ ϵ ∑S |S| ̂F(S)
2 ≤ ϵk Var[F]. □

Corollary 11.68. In the setting of the preceding corollary, if we merely have
that ψ : R → R is c-Lipschitz (rather than C 4), then
∣
∣E[ψ(F(x))] − E[ψ(F(y))]
∣
∣ ≤ O(c) · 2kϵ1/4.

Proof. Just as in the proof of Corollary 11.59, by using ̃ψη from Proposi-
tion 11.58 (which has ∥ ̃ψ
′′′′
η ∥∞ ≤ O(c/η
3)) we obtain
∣
∣E[ψ(F(x))] − E[ψ(F(y))]
∣
∣ ≤ O(c) · (η + k9kϵ/η
3).

The proof is completed by taking η = 4√k9kϵ ≤ 2kϵ1/4. □

Let’s connect this last corollary back to the study of Boolean functions.
Suppose f : {−1, 1}n → R has ϵ-small inﬂuences (in the sense of Deﬁnition 6.9)
and degree at most k. Letting g = (g1, . . . , gn) be a sequence of independent
standard Gaussians, Corollary 11.68 tells us that for any Lipschitz ψ we have
∣
∣
∣
∣ E
x∼{−1,1}n[ψ( f (x))] − E
g∼N(0,1)n[ψ( f (g))]
∣
∣
∣
∣ ≤ O(2kϵ1/4). (11.31)

Here the expression “ f (g)” is an abuse of notation indicating that the real
numbers g1, . . . , gn are substituted into f ’s Fourier expansion (multilinear
polynomial representation).

At ﬁrst it may seem peculiar to substitute arbitrary real numbers into the
Fourier expansion of a Boolean function. Actually, if all the numbers being
substituted are in the range [−1, 1] then there’s a natural interpretation: as
you were asked to show in Exercise 1.4, if µ ∈ [−1, 1]n, then f (µ) = E[ f (y)]
where y ∼ {−1, 1}n is drawn from the product distribution in which E[yi] = µi.
On the other hand, there doesn’t seem to be any obvious meaning when real
numbers outside the range [−1, 1] are substituted into f ’s Fourier expansion,
as may certainly occur when we consider f (g).

Nevertheless, (11.31) says that when f is a low-degree, small-inﬂuence
function, the distribution of the random variable f (g) will be close to that
of f (x). Now suppose f : {−1, 1}n → {−1, 1} is Boolean-valued and unbiased.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

362 11. Gaussian space and Invariance Principles

Then (11.31) might seem impossible; how could the continuous random vari-
able f (g) essentially be −1 with probability 1/2 and +1 with probability 1/2?
The solution to this mystery is that there are no low-degree, small-inﬂuence,
unbiased Boolean-valued functions. This is a consequence of the OSSS In-
equality – more precisely, Exercise 8.44(b) – which shows that in this setting
we will always have ϵ ≥ 1/k3 in (11.31), rendering the bound very weak. If the
Aaronson–Ambainis Conjecture holds (see the notes in Chapter 8.7), a similar
statement is true even for functions with range [−1, 1].

The reason (11.31) is still useful is that we can apply it to small-inﬂuence,
low-degree functions which are almost {−1, 1}-valued, or [−1, 1]-valued. Such
functions can arise from truncating a very noise-stable Boolean-valued func-
tion to a large but constant degree. For example, we might proﬁtably ap-
ply (11.31) to f = Maj
≤k
n and then deduce some consequences for Majn(x) using
the fact that E[(Maj
≤k
n (x)−Majn(x))
2] = W
>k[Majn] ≤ O(1/
pk) (Corollary 5.23).
Let’s consider this sort of idea more generally:

Corollary 11.69. Let f : {−1, 1}n → R have Var[ f ] ≤ 1. Let k ≥ 0 and suppose
f ≤k has ϵ-small inﬂuences. Then for any c-Lipschitz ψ : R → R we have
∣
∣
∣
∣ E
x∼{−1,1}n[ψ( f (x))] − E
g∼N(0,1)n[ψ( f (g))]
∣
∣
∣
∣ ≤ O(c) · (
2kϵ1/4 + ∥ f >k∥2)
. (11.32)

In particular, suppose h : {−1, 1}n → R has Var[h] ≤ 1 and no (ϵ, δ)-notable
coordinates (we assume ϵ ≤ 1, δ ≤ 1
20 ). Then
∣
∣
∣
∣ E
x∼{−1,1}n[ψ(T1−δh(x))] − E
g∼N(0,1)n[ψ(T1−δh(g))]
∣
∣
∣
∣ ≤ O(c) · ϵδ/3.

Proof. For the ﬁrst statement we simply decompose f = f ≤k + f >k. Then the
left-hand side of (11.32) can be written as
∣
∣
∣E[ψ( f ≤k(x) + f >k(x))] − E[ψ( f ≤k(g) + f >k(g))]
∣
∣
∣

≤ ∣
∣
∣E[ψ( f ≤k(x))] − E[ψ( f ≤k(g))]
∣
∣
∣ + c E[| f >k(x)|] + c E[| f >k(g)|],

using the fact that ψ is c-Lipschitz. The ﬁrst quantity is at most O(c) · 2kϵ1/4,
by Corollary 11.68 (even if k is not an integer). As for the other two quantities,
Cauchy–Schwarz implies

E[| f >k(x)|] ≤ √
E[ f >k(x)2] = √ ∑

|S|>k ̂f (S)2 = ∥ f >k∥2,

and the same bound also holds for E[| f >k(g)|]; this uses the fact that E[ f >k(g)
2] =
∑|S|>k ̂f (S)
2 just as in Remark 11.64. This completes the proof of (11.32).

As for the second statement of the corollary, let f = T1−δh. The assump-
tions on h imply that Var[ f ] ≤ 1 and that f ≤k has ϵ-small inﬂuences for any k;

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.6. The Invariance Principle 363

the latter is true because

Infi[ f ≤k] = ∑

|S|≤k,S∋i(1 − δ)2|S| ̂h(S)2 ≤ ∑

S∋i(1 − δ)|S|−1 ̂h(S)2 = Inf(1−δ)
i [h] ≤ ϵ

since h has no (ϵ, δ)-notable coordinate. Furthermore,

∥ f >k∥
2
2 = ∑

|S|>k(1 − δ)2|S| ̂h(S)2 ≤ (1 − δ)
2k Var[h] ≤ (1 − δ)2k ≤ exp(−2kδ)

for any k ≥ 1; i.e., ∥ f >k∥2 ≤ exp(−kδ). So applying the ﬁrst part of the corollary
gives ∣
∣E[ψ( f (x))] − E[ψ( f (g))]
∣
∣ ≤ O(c) · (
2kϵ1/4 + exp(−kδ)) (11.33)

for any k ≥ 0. Choosing k = 1
3 ln(1/ϵ), the right-hand side of (11.33) becomes

O(c) · (ϵ−(1/3) ln 2ϵ1/4 + ϵδ/3) ≤ O(c) · ϵδ/3,

where the inequality uses the assumption δ ≤ 1
20 (numerically, 1
4 − 1
3 ln 2 ≈ 1
53 ).
This completes the proof of the second statement of the corollary. □

Finally, if we think of the Basic Invariance Principle as the nonlinear
analogue of our Variant Berry–Esseen Theorem, it’s natural to ask for the
nonlinear analogue of the Berry–Esseen Theorem itself, i.e., a statement
showing cdf-closeness of F(x) and F(g). It’s straightforward to obtain a Lévy
distance bound just as in the degree-1 case, Corollary 11.61; Exercise 11.44
asks you to show the following:

Corollary 11.70. In the setting of Corollary 11.67 we have the Lévy distance
bound dL(F(x), F(y)) ≤ O(2kϵ1/5). In the setting of Remark 11.66 we have the
bound dL(F(x), F(y)) ≤ (1/ρ)O(k)ϵ1/8.

Suppose we now want actual cdf-closeness in the case that y ∼ N(0, 1)n.
In the degree-1 (Berry–Esseen) case we used the fact that degree-1 polyno-
mials of independent Gaussians have good anticoncentration. The analogous
statement for higher-degree polynomials of Gaussians is not so easy to prove;
however, Carbery and Wright [CW01, Theorem 8] have obtained the following
essentially optimal result:

Carbery–Wright Theorem. Let p : R n → R be a polynomial (not necessarily
multilinear) of degree at most k, let g ∼ N(0, 1)n, and assume E[p(g)2] = 1.
Then for all ϵ > 0,
 Pr[|p(g)| ≤ ϵ] ≤ O(kϵ1/k),

where the O(·) hides a universal constant.

Using this theorem it’s not hard (see Exercise 11.45) to obtain:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

364 11. Gaussian space and Invariance Principles

Theorem 11.71. Let f : {−1, 1}n → R be of degree at most k, with ϵ-small
inﬂuences and Var[ f ] = 1. Then for all u ∈ R ,

|Pr[ f (x) ≤ u] − Pr[ f (g) ≤ u]| ≤ O(k) · ϵ1/(4k+1),

where the O(·) hides a universal constant.

11.7. Highlight: Majority Is Stablest Theorem

The Majority Is Stablest Theorem (to be proved at the end of this section) was
originally conjectured in 2004 [KKMO04, KKMO07]. The motivation came
from studying the approximability of the Max-Cut CSP. Recall that Max-Cut
is perhaps the simplest possible constraint satisfaction problem: the domain
of the variables is Ω = {−1, 1} and the only constraint allowed is the binary
non-equality predicate, ̸=: {−1, 1}
2 → {0, 1}. As we mentioned brieﬂy in Chap-
ter 7.3, Goemans and Williamson [GW95] gave a very sophisticated efﬁcient
algorithm using “semideﬁnite programming” which (cGWβ, β)-approximates
Max-Cut for every β, where cGW ≈ .8786 is a certain trigonometric constant.

Turning to hardness of approximation, we know from Theorem 7.40 (devel-
oped in [KKMO04]) that to prove UG-hardness of (α + δ, β − δ)-approximating
Max-Cut, it sufﬁces to construct an (α, β)-Dictator-vs.-No-Notables test which
uses the predicate ̸=. As we’ll see in this section, the quality of the most nat-
ural such test can be easily inferred from the Majority Is Stablest Theorem.
Assuming that theorem (as Khot et al. [KKMO04] did), we get a surprising
conclusion: It’s UG-hard to approximate the Max-Cut CSP any better than the
Goemans–Williamson Algorithm does. In other words, the peculiar approxi-
mation guarantee of Goemans and Williamson on the very simple Max-Cut
problem is optimal (assuming the Unique Games Conjecture).

Let’s demystify this somewhat, starting with a description of the Goemans–
Williamson Algorithm. Let G = (V , E) be an n-vertex input graph for the algo-
rithm; we’ll write (v, w) ∼ E to denote that (v, w) is a uniformly random edge
(i.e., ̸=-constraint) in the graph. The ﬁrst step of the Goemans–Williamson
Algorithm is to solve following optimization problem:

maximize E
(v,w)∼E
 [ 1
2 − 1
2 〈⃗U(v), ⃗U(w)〉]

subject to ⃗U : V → Sn−1. (SDP)

Here Sn−1 denotes the set of all unit vectors in R n. Somewhat surprisingly,
since this optimization problem is a “semideﬁnite program” it can be solved
in polynomial time using the Ellipsoid Algorithm. (Technically, it can only be
solved up to any desired additive tolerance ϵ > 0, but we’ll ignore this point.)
Let’s write SDPOpt(G) for the optimum value of (SDP), and Opt(G) for the

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.7. Highlight: Majority Is Stablest Theorem 365

optimum Max-Cut value for G. We claim that (SDP) is a relaxation of the
Max-Cut CSP on input G, and therefore

SDPOpt(G) ≥ Opt(G).

To see this, simply note that if F ∗ : V → {−1, 1} is an optimal assignment
(“cut”) for G then we can deﬁne ⃗U(v) = (F ∗(v), 0, . . . , 0) ∈ Sn−1 for each v ∈ V
and achieve the optimal cut value ValG(F ∗) in (SDP).

The second step of the Goemans–Williamson Algorithm might look famil-
iar from Fact 11.7 and Remark 11.8. Let ⃗U ∗ : V → Sn−1 be the optimal solu-
tion for (SDP), achieving SDPOpt(G); abusing notation we’ll write ⃗U ∗(v) =⃗v.
The algorithm now chooses ⃗g ∼ N(0, 1)n at random and outputs the assign-
ment (cut) F : V → {−1, 1} deﬁned by F(v) = sgn(〈⃗v,⃗g〉). Let’s analyze the
(expected) quality of this assignment. The probability the algorithm’s assign-
ment F cuts a particular edge (v, w) ∈ E is

Pr
⃗g∼N(0,1)n[sgn(〈⃗v,⃗g〉) ̸= sgn(〈⃗w,⃗g〉)].

This is precisely the probability that sgn(z) ̸= sgn(z′) when (z, z′) is a pair
of 〈⃗v, ⃗w〉-correlated 1-dimensional Gaussians. Writing ∠(⃗v, ⃗w) ∈ [0, π] for the
angle between the unit vectors ⃗v, ⃗w, we conclude from Sheppard’s Formula
(see (11.2)) that
 Pr
⃗g [F cuts edge (v, w)] = ∠(⃗v, ⃗w)

π .

By linearity of expectation we can compute the expected value of the algo-
rithm’s assignment F:

E
⃗g [ValG(F)] = E
(v,w)∼E
 [
∠(⃗v, ⃗w)/π] . (11.34)

On the other hand, by deﬁnition we have

SDPOpt(G) = E
(v,w)∼E
 [ 1
2 − 1
2 cos∠(⃗v, ⃗w)
] . (11.35)

It remains to compare (11.34) and (11.35). Deﬁne

cGW = min
θ∈[0,π]
 { θ/π

1
2 − 1
2 cos θ
 }
 ≈ .8786. (11.36)

Then from (11.34) and (11.35) we immediately get

E
⃗g [ValG(F)] ≥ cGW · SDPOpt(G) ≥ cGW · Opt(G);

i.e., in expectation the Goemans–Williamson Algorithm delivers a cut of
value at least cGW times the Max-Cut. In other words, it’s a (cGWβ, β)-
approximation algorithm, as claimed. By being a little bit more careful about
this analysis (Exercise 11.33) you can show following additional result:

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

366 11. Gaussian space and Invariance Principles

Theorem 11.72. [GW95]. Let θ ∈ [θ∗, π], where θ∗ ≈ .74π is the minimizing θ
in (11.36) (also deﬁnable as the positive solution of tan(θ/2) = θ). Then on any
graph G with SDPOpt(G) ≥ 1
2 − 1
2 cos θ, the Goemans–Williamson Algorithm
produces a cut of (expected) value at least θ/π. In particular, the algorithm is
a (θ/π, 1
2 − 1
2 cos θ)-approximation algorithm for Max-Cut.

Example 11.73. Consider the Max-Cut problem on the 5-vertex cycle graph Z 5.
The best bipartition of this graph cuts 4 out of the 5 edges; hence Opt(Z 5) = 4
5 .
Exercise 11.32 asks you to show that taking

⃗U(v) = (cos 4πv
5 , sin 4πv
5 ), v ∈ Z 5,

in the semideﬁnite program (SDP) establishes that SDPOpt(Z 5) ≥ 1
2 − 1
2 cos 4π
5 .
(These are actually unit vectors in R 2 rather than in R 5 as (SDP) requires,
but we can pad out the last three coordinates with zeroes.) This exam-
ple shows that the Goemans–Williamson analysis in Theorem 11.72 lower-
bounding Opt(G) in terms of SDPOpt(G) cannot be improved (at least when
SDPOpt(G) = 4
5 ). This is termed an optimal integrality gap. In fact, Theo-
rem 11.72 also implies that SDPOpt(Z 5) must equal 1
2 − 1
2 cos 4π
5 , for if it were
greater, the theorem would falsely imply that Opt(Z 5) > 4
5 . Note that the
Goemans–Williamson Algorithm actually ﬁnds the maximum cut when run
on the cycle graph Z 5. For a related example, see Exercise 11.35.

Now we explain the result of Khot et al. [KKMO04], that the Majority Is
Stablest Theorem implies it’s UG-hard to approximate Max-Cut better than
the Goemans–Williamson Algorithm does:

Theorem 11.74. [KKMO04]. Let θ ∈ ( π
2 , π). Then for any δ > 0 it’s UG-hard
to (θ/π + δ, 1
2 − 1
2 cos θ)-approximate Max-Cut.

Proof. It follows from Theorem 7.40 that we just need to construct a (θ/π, 1
2 −
1
2 cos θ)-Dictator-vs.-No-Notables test using the predicate ̸=. (See Exercise 11.36
for an extremely minor technical point.) It’s very natural to try the following,
with β = 1
2 − 1
2 cos θ ∈ ( 1
2 , 1):

β-Noise Sensitivity Test. Given query access to f : {−1, 1}n → {−1, 1}:

• Choose x ∼ {−1, 1}n and form x′ by reversing each bit of x independently
with probability β = 1
2 − 1
2 cos θ. In other words let (x, x′) be a pair of
cos θ-correlated strings. (Note that cos θ < 0.)

• Query f at x, x′.

• Accept if f (x) ̸= f (x′).

By design,

Pr[the test accepts f ] = NSβ[ f ] = 1
2 − 1
2 Stabcos θ[ f ]. (11.37)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.7. Highlight: Majority Is Stablest Theorem 367

(We might also express this as “RS f (θ)”.) In particular, if f is a dictator,
it’s accepted with probability exactly β = 1
2 − 1
2 cos θ. To complete the proof
that this is a (θ/π, 1
2 − 1
2 cos θ)-Dictator-vs.-No-Notables test, let’s suppose f :
{−1, 1}n → [−1, 1] has no (ϵ, ϵ)-notable coordinates and show that (11.37) is at
most θ/π + oϵ(1). (Regarding f having range [−1, 1], recall Remark 7.38.)

At ﬁrst it might look like we can immediately apply the Majority Is Sta-
blest Theorem; however, the theorem’s inequality goes the “wrong way” and
the correlation parameter ρ = cos θ is negative. These two difﬁculties actually
cancel each other out. Note that

Pr[the test accepts f ] = 1
2 − 1
2 Stabcos θ[ f ]

= 1
2 − 1
2
 n∑

k=0
(cos θ)kWk[ f ]

≤ 1
2 + 1
2 ∑

k odd(− cos θ)kWk[ f ] (since cos θ < 0)

= 1
2 + 1
2 Stab− cos θ[ f odd], (11.38)

where f odd : {−1, 1}n → [−1, 1] is the odd part of f (see Exercise 1.8) deﬁned by

f odd(x) = 1
2 ( f (x) − f (−x)) = ∑

|S| odd ̂f (S) xS.

Now we’re really in a position to apply the Majority Is Stablest Theorem
to f odd, because − cos θ ∈ (0, 1), E[ f odd] = 0, and f odd has no (ϵ, ϵ)-notable coor-
dinates (since it’s formed from f by just dropping some terms in the Fourier
expansion). Using − cos θ = cos(π − θ), the result is that

Stab− cos θ[ f odd] ≤ 1 − 2
π arccos(cos(π − θ)) + oϵ(1) = 2θ/π − 1 + oϵ(1).

Putting this into (11.38) yields

Pr[the test accepts f ] ≤ 1
2 + 1
2 (2θ/π − 1 + oϵ(1)) = θ/π + oϵ(1),

as needed. □

Remark 11.75. There’s actually still a mismatch between the algorithmic
guarantee of Theorem 11.72 and the UG-hardness result Theorem 11.74, con-
cerning the case of θ ∈ ( π
2 , θ∗). In fact, for these values of θ – i.e., 1
2 ≤ β ⪅ .8446
– neither result is sharp; see O’Donnell and Wu [OW08].

Remark 11.76. If we want to prove UG-hardness of (θ′/π + δ, 1
2 − 1
2 cos θ′)-
approximating Max-Cut, we don’t need the full version of Borell’s Isoperi-
metric Theorem; we only need the volume- 1
2 case with parameter θ = π − θ′.
Corollary 11.44 gave a simple proof of this result for θ = π
4 , hence θ′ = 3
4 π.
This yields UG-hardness of ( 3
4 + δ, 1
2 + 1
2p
2 )-approximating Max-Cut. The ratio
between α and β here is approximately .8787, very close to the Goemans–
Williamson constant cGW ≈ .8786.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

368 11. Gaussian space and Invariance Principles

Finally, we will prove the General-Volume Majority Is Stablest Theorem,
by using the Invariance Principle to reduce it to Borell’s Isoperimetric Theo-
rem.

General-Volume Majority Is Stablest Theorem. Let f : {−1, 1}n → [0, 1].
Suppose that MaxInf[ f ] ≤ ϵ, or more generally, that f has no (ϵ, 1
log(1/ϵ) )-notable
coordinates. Then for any 0 ≤ ρ < 1,

Stabρ[ f ] ≤ Λρ(E[ f ]) + O( log log(1/ϵ)
log(1/ϵ) ) · 1
1−ρ . (11.39)

(Here the O(·) bound has no dependence on ρ.)

Proof. The proof involves using the Basic Invariance Principle twice (in the
form of Corollary 11.69). To facilitate this we introduce f ′ = T1−δ f , where
(with foresight) we choose
 δ = 3 log log(1/ϵ)
log(1/ϵ) ≥ 1
log(1/ϵ) .

(We may assume ϵ is sufﬁciently small so that 0 < δ ≤ 1
20 .) Note that E[ f ′] =
E[ f ] and that

Stabρ[ f ′] = ∑

S⊆[n] ρ|S|(1 − δ)2|S| ̂f (S)2 = Stabρ(1−δ)2[ f ].

But
∣
∣Stabρ(1−δ)2[ f ] − Stabρ[ f ]
∣
∣ ≤ (ρ − ρ(1 − δ)2) · 1
1−ρ · Var[ f ] ≤ 2δ · 1
1−ρ (11.40)

by Exercise 2.46, and with our choice of δ this can be absorbed into the error
of (11.39). Thus it sufﬁces to prove (11.39) with f ′ in place of f .

Let Sq : R → R be the continuous function which agrees with t 7→ t2 for t ∈
[0, 1] and is constant outside [0, 1]. Note that Sq is 2-Lipschitz. We will apply
the second part of Corollary 11.69 with “h” set to Tp
ρ f (and thus T1−δh =
Tp
ρ f ′). This is valid since the variance and (1 − δ)-stable inﬂuences of h are
only smaller than those of f . Thus
∣
∣
∣
∣ E
x∼{−1,1}n[Sq(Tp
ρ f ′(x))] − E
g∼N(0,1)n[Sq(Tp
ρ f ′(g))]
∣
∣
∣
∣ ≤ O(ϵδ/3) = O( 1
log(1/ϵ) )
,

(11.41)
using our choice of δ. (In fact, it’s trading off this error with (11.40) that led
to our choice of δ.) Now Tp
ρ f ′(x) = T(1−δ)p
ρ f (x) is always bounded in [0, 1], so

Sq(Tp
ρ f ′(x)) = (Tp
ρ f ′(x))2 =⇒ E
x∼{−1,1}n[Sq(Tp
ρ f ′(x))] = Stabρ[ f ′].

Furthermore, Tp
ρ f ′(g) is the same as Up
ρ f ′(g) because f ′ is a multilinear
polynomial. (Both are equal to f ′(ρ g); see Fact 11.13.) Thus in light of (11.41),
to complete the proof of (11.39) it sufﬁces to show

E
g∼N(0,1)n[Sq(Up
ρ f ′(g))] ≤ Λρ(E[ f ′]) + O( 1
log(1/ϵ) ). (11.42)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.7. Highlight: Majority Is Stablest Theorem 369

Deﬁne the function F : R n → [0, 1] by

F(g) = trunc[0,1]( f ′(g)) =
 




0 if f ′(g) < 0,

f ′(g) if f ′(g) ∈ [0, 1],

1 if f ′(g) > 1.

We will establish the following two inequalities, which together imply (11.42):
∣
∣
∣
∣ E
g∼N(0,1)n[Sq(Up
ρ f ′(g))] − E
g∼N(0,1)n[Sq(Up
ρ F(g))]
∣
∣
∣
∣ ≤ O( 1
log(1/ϵ) )
, (11.43)

E
g∼N(0,1)n[Sq(Up
ρ F(g))] ≤ Λρ(E[ f ′]) + O( 1
log(1/ϵ) )
. (11.44)

Both of these inequalities will in turn follow from

E
g∼N(0,1)n[| f ′(g) − F(g)|] = E
g∼N(0,1)n[dist[0,1]( f ′(g))] ≤ O( 1
log(1/ϵ) )
. (11.45)

Let’s show how (11.43) and (11.44) follow from (11.45), leaving the proof
of (11.45) to the end. For (11.43),
∣
∣
∣E[Sq(Up
ρ f ′(g))] − E[Sq(Up
ρ F(g))]
∣
∣
∣ ≤ 2 E[|Up
ρ f ′(g) − Up
ρ F(g)|]

≤ 2 E[| f ′(g) − F(g)|] ≤ O( 1
log(1/ϵ) )
,

where the ﬁrst inequality used that Sq is 2-Lipschitz, the second inequality
used the fact that Up
ρ is a contraction on L1(R n, γ), and the third inequality
was (11.45). As for (11.44), Up
ρ F is bounded in [0, 1] since F is. Thus

E[Sq(Up
ρ F(g))] = E[(Up
ρ F(g))2] = Stabρ[F] ≤ Λρ(E[F(g)]),

where we used Borell’s Isoperimetric Theorem. But | E[F(g)] − E[ f ′(g)]| ≤
O( 1
log(1/ϵ) ) by (11.45), and Λρ is easily shown to be 2-Lipschitz (Exercise 11.19(e)).
This establishes (11.44).

It therefore remains to show (11.45), which we do by applying the Invari-
ance Principle one more time. Taking ψ to be the 1-Lipschitz function dist[0,1]
in Corollary 11.69 we deduce
∣
∣
∣
∣ E
g∼N(0,1)n[dist[0,1]( f ′(g))] − E
x∼{−1,1}n[dist[0,1]( f ′(x))]∣
∣
∣
∣ ≤ O(ϵδ/3) = O( 1
log(1/ϵ) )
.

But E[dist[0,1] f ′(x)] = 0 since f ′(x) = T1−δ f (x) ∈ [0, 1] always. This estab-
lishes (11.45) and completes the proof. □

We conclude with one more application of the Majority Is Stablest Theo-
rem. Recall Kalai’s version of Arrow’s Theorem from Chapter 2.5, i.e., Theo-
rem 2.56. It states that in a 3-candidate Condorcet election using the voting
rule f : {−1, 1}n → {−1, 1}, the probability of having a Condorcet winner – often
called a rational outcome – is precisely 3
4 − 3
4 Stab−1/3[ f ]. As we saw in the
proof of Theorem 11.74 near (11.38), this is in turn at most 3
4 + 3
4 Stab1/3[ f odd],
with equality if f is already odd. It follows from the Majority Is Stablest

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

370 11. Gaussian space and Invariance Principles

Theorem that among all voting rules with ϵ-small inﬂuences (a condition all
reasonable voting rules should satisfy), majority rule is the “most rational”.
Thus we see that the principle of representative democracy can be derived
using analysis of Boolean functions.

11.8. Exercises and notes

11.1 Let A be the set of all functions f : R n → R which are ﬁnite linear combi-
nations of indicator functions of boxes. Prove that A is dense in L1(R n, γ).

11.2 Fill in proof details for the Gaussian Hypercontractivity Theorem.

11.3 Prove Fact 11.13. (Cf. Exercise 2.25.)

11.4 Show that Uρ1Uρ2 = Uρ1ρ2 for all ρ1, ρ2 ∈ [−1, 1]. (Cf. Exercise 2.32.)

11.5 Prove Proposition 11.16. (Hint: For ρ ̸= 0, write g(z) = Uρ f (z) and show
that g(z/ρ) is a smooth function using the relationship between convolu-
tion and derivatives.)

11.6 (a) Prove Proposition 11.17. (Hint: First prove it for bounded continu-
ous f ; then make an approximation and use Proposition 11.15.)
(b) Deduce more generally that for f ∈ L1(R n, γ) the map ρ 7→ Uρ f is
“strongly continuous” on [0, 1], meaning that for any ρ ∈ [0, 1] we have
∥Uρ′ f − Uρ f ∥1 → 0 as ρ′ → ρ. (Hint: Use Exercise 11.4.)

11.7 Complete the proof of Proposition 11.26 by establishing the case of gen-
eral n.

11.8 Complete the proof of Proposition 11.28 by establishing the case of gen-
eral n.

11.9 (a) Establish the alternative formula (11.10) for the probabilists’ Hermite
polynomials H j(z) given in Deﬁnition 11.29; equivalently, establish
the formula

H j(z) = (−1) j exp( 1
2 z2) · ( d
dz
 ) j exp(− 1
2 z2).

(Hint: Complete the square on the left-hand side of (11.8); then differ-
entiate j times with respect to t and evaluate at 0.)
(b) Establish the recursion

H j(z) = (z − d
dz )H j−1(z) ⇐⇒ h j(z) = 1p j · (z − d
dz )h j−1(z)

for j ∈ N +, and hence the formula H j(z) = (z − d
dz ) j1.
(c) Show that h j(z) is an odd function of z if j is odd and an even function
of z if j is even.

11.10 (a) Establish the derivative formula for Hermite polynomials:

H′
j(z) = j · H j−1(z) ⇐⇒ h′
j(z) = √ j · h j−1(z).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 371

(b) By combining this with the other formula for H′
j(z) implicit in Exer-
cise 11.9(b), deduce the recursion

H j+1(z) = zH j(z) − jH j−1(z).

(c) Show that H j(z) satisﬁes the second-order differential equation

jH j(z) = zH′
j(z) − H′′
j (z).

(It’s equivalent to say that h j(z) satisﬁes it.) Observe that this is
consistent with Propositions 11.26 and 11.40 and says that H j (equiv-
alently, h j) is an eigenfunction of the Ornstein–Uhlenbeck operator L,
with eigenvalue j.

11.11 Prove that
 H j(x + y) =
 j∑

i=0
 ( j
i
)
x j−i Hi(y),

and, relatedly, that for p + q = 1 we have

hk(
ppx + pq y) = ∑

i+ j=k
 √( k
i, j)pi q j hi(x)h j(y).

11.12 (a) By equating both sides of (11.8) with

E
g∼N(0,1)
[exp(t(z + i g))]

(where i = p
−1), show that

H j(z) = E
g∼N(0,1)
[(z + i g) j].

(b) Establish the explicit formulas

H j(z) =
 ⌊ j/2⌋∑

k=0(−1)k( j
2k
)
 E
g∼N(0,1)
[g2k]z j−2k

= j! · ( z j

0!! · j! − z j−2

2!! · ( j − 2)! + z j−4

4!! · ( j − 4)! − z j−6

6!! · ( j − 6)! + · · · ) .

11.13 (a) Establish the formula

E[∥∇ f ∥
2] = ∑

α∈N n |α| ̂f (α)
2

for all f ∈ L2(R n, γ) (or at least for all n-variate polynomials f ).
(b) For f ∈ L2(R n, γ), establish the formula

n∑

i=1 E[Var
zi [ f ]] = ∑

α∈N n(#α) ̂f (α)
2.

11.14 Show that for all j ∈ N and all z ∈ R we have

(n
j)−1/2 · K (n)
j
 ( n
2 − z pn
2
 ) n→∞
−−−−→ h j(z),

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

372 11. Gaussian space and Invariance Principles

where K (n)
j is the Kravchuk polynomial of degree j from Exercise 5.28
(with its dependence on n indicated in the superscript).

11.15 Recall the deﬁnition (11.13) of the Gaussian Minkowski content of the
boundary ∂A of a set A ⊆ R n. Sometimes the following very similar
deﬁnition is also proposed for the Gaussian surface area of A:

M(A) = lim inf
ϵ→0+ volγ({z : dist(z, A) < ϵ}) − volγ(A)

ϵ .

Consider the following subsets of R :

A1 = ;, A2 = {0}, A3 = (−∞, 0), A4 = (−∞, 0], A5 = R \ {0}, A6 = R .

(a) Show that

γ
+(A1) = 0 M(A1) = 0 surfγ(A1) = 0

γ
+(A2) = 1p
2π M(A2) = √ 2
π surfγ(A2) = 0

γ
+(A3) = 1p
2π M(A3) = 1p
2π surfγ(A3) = 1p
2π
γ
+(A4) = 1p
2π M(A4) = 1p
2π surfγ(A4) = 1p
2π
γ
+(A5) = 1p
2π M(A5) = 0 surfγ(A5) = 0

γ
+(A6) = 0 M(A6) = 0 surfγ(A6) = 0.

(b) For A ⊆ R n, the essential boundary (or measure-theoretic boundary)
of A is deﬁned to be

∂∗ A = {x ∈ R n : lim
δ→0+ volγ(A ∩ Bδ(x))

volγ(Bδ(x)) ̸= 0, 1
} ,

where Bδ(x) denotes the ball of radius δ centered at x. In other words,
∂∗ A is the set of points where the “local density of A” is strictly be-
tween 0 and 1. Show that if we replace ∂A with ∂∗ A in the deﬁni-
tion (11.13) of the Gaussian Minkowski content of the boundary of A,
then we have the identity γ
+(∂∗ A i) = surfγ(A i) for all 1 ≤ i ≤ 6. Re-
mark: In fact, the equality γ
+(∂∗ A) = surfγ(A) is known to hold for
every set A such that ∂∗ A is “rectiﬁable”.

11.16 Justify the formula for the Gaussian surface area of unions of intervals
stated in Example 11.50.

11.17 (a) Let Br ⊂ R n denote the ball of radius r > 0 centered at the origin.
Show that surfγ(Br) = n

2n/2(n/2)! rn−1 e−r2/2. (11.46)

(b) Show that (11.46) is maximized when r = pn − 1. (In case n = 1, this
should be interpreted as r → 0+.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 373

(c) Let S(n) denote this maximizing value, i.e., the value of (11.46) with

r = pn − 1. Show that S(n) decreases from √ 2
π to a limit of 1p
π as n
increases from 1 to ∞.

11.18 (a) For f ∈ L2(R n, γ), show that L f is deﬁned, i.e.,

lim
t→0 f − Ue−t f
t

exists in L2(R n, γ), if and only if ∑
α∈N n |α|2 ̂f (α)
2 < ∞. (Hint: Proposi-
tion 11.37.)
(b) Formally justify Proposition 11.40.
(c) Let f ∈ L2(R n, γ). Show that Uρ f is in the domain of L for any ρ ∈
(−1, 1).
Remark: It can be shown that the C 3 hypothesis in Propositions 11.26
and 11.28 is not necessary (provided the derivatives are interpreted in
the distributional sense); see, e.g., Bogachev [Bog98, Chapter 1] for more
details.

11.19 This exercise is concerned with (a generalization of) the function appear-
ing in Borell’s Isoperimetric Theorem.

Deﬁnition 11.77. For ρ ∈ [−1, 1] we deﬁne the Gaussian quadrant prob-
ability function Λρ : [0, 1]
2 → [0, 1] by

Λρ(α, β) = Pr
(z,z′) ρ-correlated
standard Gaussians

[z ≤ t, z′ ≤ t′],

where t and t′ are deﬁned by Φ(t) = α, Φ(t′) = β. This is a slight reparametriza-
tion of the bivariate Gaussian cdf. We also use the shorthand notation

Λρ(α) = Λρ(α, α),

which we encountered in Borell’s Isoperimetric Theorem (and also in Ex-
ercises 5.32 and 9.24, with a different, but equivalent, deﬁnition).

(a) Conﬁrm the statement from Borell’s Isoperimetric Theorem, that for
every halfspace H ⊆ R n with volγ(H) = α we have Stabρ[1H] = Λρ(α).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

374 11. Gaussian space and Invariance Principles

(b) Verify the following formulas:

Λρ(α, β) = Λρ(β, α),

Λ0(α, β) = αβ,

Λ1(α, β) = min(α, β),

Λ−1(α, β) = max(α + β − 1, 0),

Λρ(α, 0) = Λρ(0, α) = 0,

Λρ(α, 1) = Λρ(1, α) = α,

Λ−ρ(α, β) = α − Λρ(α, 1 − β) = β − Λρ(1 − α, β),

Λρ( 1
2 , 1
2 ) = 1
2 − 1
2 arccos ρ
π .

(c) Prove that Λρ(α, β) ≷ αβ according as ρ ≷ 0, for all 0 < α, β < 1.
(d) Establish

d
dα Λρ(α, β) = Φ
 ( t′ − ρt
√
1 − ρ2
 )
 , d
dβ Λρ(α, β) = Φ
 ( t − ρt′
√
1 − ρ2
 )
 ,

where t = Φ−1(α), t′ = Φ−1(β) as usual.
(e) Show that
 |Λρ(α, β) − Λρ(α
′, β
′)| ≤ |α − α
′| + |β − β
′|,

and hence Λρ(α) is a 2-Lipschitz function of α.

11.20 Show that the general-n case of Bobkov’s Inequality follows by induction
from the n = 1 case.

11.21 Let f : {−1, 1}n → {−1, 1} and let α = min{Pr[ f = 1], Pr[ f = −1]}. Deduce
I[ f ] ≥ 4U (α)
2 from Bobkov’s Inequality. Show that this recovers the edge-
isoperimetric inequality for the Boolean cube (Theorem 2.39) up to a
constant factor. (Hint: For the latter problem, use Proposition 5.27.)

11.22 Let d1, d2 ∈ N . Suppose we take a simple random walk on Z , starting
from the origin and moving by ±1 at each step with equal probability.
Show that the expected time it takes to ﬁrst reach either −d1 or +d2 is
d1d2.

11.23 Prove Claim 11.54. (Hint: For the function Vy(τ) appearing in the proof
of Bobkov’s Two-Point Inequality, you’ll want to establish that V ′′′
y (0) = 0

and that V ′′′′
y (0) = 2+10U ′(y)2

U (y)3 > 0.)

11.24 Prove Theorem 11.55. (Hint: Have the random walk start at y0 = a ± ρb
with equal probability, and deﬁne zt = ∥(U (yt), ρb, τpt)∥. You’ll need the
full generality of Exercise 11.22.)

11.25 Justify Remark 11.41 (in the general-volume context) by showing that
Borell’s Isoperimetric Theorem for all functions in K = { f : R n → [0, 1] |
E[ f ] = α} can be deduced from the case of functions in ∂K = { f : R n →

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 375

{0, 1} | E[ f ] = α}. (Hint: As stated in the remark, the intuition is that
√
Stabρ[ f ] is a norm and that K is a convex set whose extreme points
are ∂K. To make this precise, you may want to use Exercise 11.1.)

11.26 The goal of this exercise and Exercises 11.27–11.29 is to give the proof of
Borell’s Isoperimetric Theorem due to Mossel and Neeman [MN12]. In
fact, their proof gives the following natural “two-set” generalization of
the theorem (Borell’s original work [Bor85] proved something even more
general):

Two-Set Borell Isoperimetric Theorem. Fix ρ ∈ (0, 1) and α, β ∈ [0, 1].
Then for any A, B ⊆ R n with volγ(A) = α, volγ(B) = β,

Pr
(z,z′) ρ-correlated
n-dimensional Gaussians

[z ∈ A, z′ ∈ B] ≤ Λρ(α, β). (11.47)

By deﬁnition of Λρ(α, β), equality holds if A and B are parallel halfs-
paces. Taking β = α and B = A in this theorem gives Borell’s Isoperimet-
ric Theorem as stated in Section 11.3 (in the case of range {0, 1}, at least,
which is equivalent by Exercise 11.25). It’s quite natural to guess that
parallel halfspaces should maximize the “joint Gaussian noise stability”
quantity on the left of (11.47), especially in light of Remark 10.2 from
Chapter 10.1 concerning the analogous Generalized Small-Set Expansion
Theorem. Just as our proof of the Small-Set Expansion Theorem passed
through the Two-Function Hypercontracitivity Theorem to facilitate in-
duction, so too does the Mossel–Neeman proof pass through the following
“two-function version” of Borell’s Isoperimetric Theorem:

Two-Function Borell Isoperimetric Theorem. Fix ρ ∈ (0, 1) and let
f , g ∈ L2(R n, γ) have range [0, 1]. Then

E
(z,z′) ρ-correlated
n-dimensional Gaussians

[Λρ( f (z), g(z′))] ≤ Λρ (E[ f ], E[g]) .

(a) Show that the Two-Function Borell Isoperimetric Theorem implies
the Two-Set Borell Isoperimetric Theorem and the Borell Isoperimet-
ric Theorem (for functions with range [0, 1]). (Hint: You may want to
use facts from Exercise 11.19.)
(b) Show conversely that the Two-Function Borell Isoperimetric Theorem
(in dimension n) is implied by the Two-Set Borell Isoperimetric Theo-
rem (in dimension n +1). (Hint: Given f : R n → [0, 1], deﬁne A ⊆ R n+1

by (z, t) ∈ A ⇐⇒ f (z) ≥ Φ(t).)
(c) Let ℓ1, ℓ2 : R n → R be deﬁned by ℓi(z) = 〈a, z〉 + bi for some a ∈ R n,
b1, b2 ∈ R . Show that equality occurs in the Two-Function Borell
Isoperimetric Theorem if f (z) = 1ℓ1(z)≥0, g(z) = 1ℓ2(z)≥0 or if f (z) =
Φ(ℓ1(z)), g(z) = Φ(ℓ2(z)).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

376 11. Gaussian space and Invariance Principles

11.27 Show that the inequality in the Two-Function Borell Isoperimetric The-
orem “tensorizes” in the sense that if it holds for n = 1, then it holds for
all n. Your proof should not use any property of the function Λρ, nor any
property of the ρ-correlated n-dimensional Gaussian distribution besides
the fact that it’s a product distribution. (Hint: Induction by restrictions as
in the proof of the Two-Function Hypercontractivity Induction Theorem
from Chapter 9.4.)

11.28 Let I1, I2 ⊆ R be open intervals and let F : I1 × I2 → R be C 2. For ρ ∈ R ,
deﬁne the matrix
 HρF = (HF ) ◦ [1 ρ
ρ 1
] ,

where HF denotes the Hessian of F and ◦ is the entrywise (Hadamard)
product. We say that F is ρ-concave (this terminology introduced by
Ledoux [Led13]) if HρF is everywhere negative semideﬁnite. Note that
the ρ = 1 case corresponds to the usual notion of concavity, and the ρ = 0
case corresponds to concavity separately along the two coordinates. The
goal of this exercise is to show that the Gaussian quadrant probability Λρ
function is ρ-concave for all ρ ∈ (0, 1).
(a) Extending Exercise 11.19(d), show that for any ρ ∈ (−1, 1),

d2

dα2 Λρ(α, β) = − ρ
√
1 − ρ2 · 1

φ(t) · φ
 ( t′ − ρt
√
1 − ρ2
 )
 ,

and deduce a similar formula for d2

dβ2 Λρ(α, β).
(b) Show that

d2

dα dβ Λρ(α, β) = 1
√
1 − ρ2 · 1

φ(t′) · φ
 ( t′ − ρt
√1 − ρ2
 )
 ,

and deduce a similar (in fact, equal) formula for d2
dβ dα Λρ(α, β).

(c) Show that det(HρΛρ) = 0 on all of (0, 1)
2.

(d) Show that if ρ ∈ (0, 1), then d2

dα2 Λρ, d2

dβ2 Λρ < 0 on (0, 1)2. Deduce that
Λρ is ρ-concave.

11.29 This exercise is devoted to Mossel and Neeman’s proof [MN12] of the
Two-Function Borell Isoperimetric Theorem in the case n = 1. For an-
other approach, see Exercise 11.30. By Exercise 11.27, this is sufﬁcient
to establish the case of general n. (Actually, the proof in this exercise
works essentially verbatim in the general n case, but we stick to n = 1 for
simplicity.)
(a) More generally, we intend to prove that for f , g : R → [0, 1],

λ(σ) = E
(z,z′) ρ-correlated
standard Gaussians

[Λρ(Uσ f (z), Uσ g(z′))]

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 377

is a nonincreasing function of 0 < σ < 1 (cf. Theorem 11.55). Obtain
the desired conclusion by taking σ → 0+, 1−. (Hint: You’ll need Exer-
cises 11.6 and 11.19(e).)
(b) Write fσ = Uσ f , gσ = Uσ g for brevity, and write ∂iΛρ (i = 1, 2) for the
partial derivatives of Λρ. Also let h1, h2 denote independent standard
Gaussians. Use the Chain Rule and Proposition 11.27 to establish

σλ
′(σ) = E[(∂1Λρ)( fσ(h1), gσ(ρh1 + √
1 − ρ2h2)) · L fσ(h1)] (11.48)

+ E[(∂2Λρ)( fσ(ρh2 + √1 − ρ2h1), gσ(h2)) · Lgσ(h2)]. (11.49)

(c) Use Proposition 11.28 to show that the ﬁrst expectation (11.48) equals

E[(∂11Λρ f )( fσ, gσ) · ( f ′
σ)
2 + ρ · (∂21Λρ f )( fσ, gσ) · f ′
σ · g′
σ],

where fσ, f ′
σ are evaluated at h1 and gσ, g′
σ are evaluated at ρh1 +√1 − ρ2h2. Give a similar formula for (11.49).
(d) Deduce that

σλ
′(σ) = E
(z,z′) ρ-correlated
standard Gaussians
 [
[ f ′
σ(z) g′
σ(z′)] · (HρΛρ)( fσ(z), gσ(z′)) · [ f ′
σ(z)
g′
σ(z′)

]] ,

where Hρ is as in Exercise 11.28, and that indeed λ is a nonincreasing
function.

11.30 (a) Suppose the Two-Function Borell Isoperimetric Theorem were to hold
for 1-bit functions, i.e., for f , g : {−1, 1} → [0, 1]. Then the easy in-
duction of Exercise 11.27 would extend the result to n-bit functions
f , g : {−1, 1}n → [0, 1]; in turn, this would yield the Two-Function
Borell Isoperimetric Theorem for 1-dimensional Gaussian functions
(i.e., Exercise 11.29), by the usual Central Limit Theorem argument.
Show, however, that dictator functions provide a counterexample to a
potential “1-bit Two-Function Borell Isoperimetric Theorem”.
(b) Nevertheless, the idea can be salvaged by proving a weakened version
of the inequality for 1-bit functions that has an “error term” that is a
superlinear function of f and g’s “inﬂuences”. Fix ρ ∈ (0, 1) and some
small ϵ > 0. Let f , g : {−1, 1} → [ϵ, 1 − ϵ]. Show that

E
(x,x′)
ρ-correlated

[Λρ( f (x), g(x′))] ≤ Λρ(E[ f ], E[g]) + Cρ,ϵ · (E[|D1 f |3] + E[|D1 g|3]),

where Cρ,ϵ is a constant depending only on ρ and ϵ. (Hint: Perform a
2nd-order Taylor expansion of Λρ around (E[ f ], E[g]); in expectation,
the quadratic term should be

[
D1 f D1 g] · (HρΛρ)(E[ f ], E[g]) · [D1 f
D1 g
] .

As in Exercise 11.29, show this quantity is nonpositive.)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

378 11. Gaussian space and Invariance Principles

(c) Extend the previous result by induction to obtain the following theo-
rem of De, Mossel, and Neeman [DMN13]:

Theorem 11.78. For each ρ ∈ (0, 1) and ϵ > 0, there exists a con-
stant Cρ,ϵ such that the following holds: If f , g : {−1, 1}n → [ϵ, 1 − ϵ],
then

E
(x,x′)
ρ-correlated

[Λρ( f (x), g(x′))] ≤ Λρ(E[ f ], E[g]) + Cρ,ϵ · (∆n[ f ] + ∆n[g]).

Here we using the following inductive notation: ∆1[ f ] = E[| f − E[ f ]|3],
and ∆n[ f ] = E
xn∼{−1,1}
 [
∆n−1[ f|xn ]
] + ∆1[ f ⊆{n}].

(d) Prove by induction that ∆n[ f ] ≤ 8 ∑n
i=1 ∥Di f ∥
3
3.
(e) Suppose that f , g ∈ L2(R , γ) have range [ϵ, 1 − ϵ] and are c-Lipschitz.
Show that for any M ∈ N +, the Two-Function Borell Isoperimetric
Theorem holds for f , g with an additional additive error of O(M−1/2),
where the constant in the O(·) depends only on ρ, ϵ, and c. (Hint: Use
BitsToGaussiansM.)
(f ) By an approximation argument, deduce the Two-Function Borell Isoperi-
metric Theorem for general f , g ∈ L2(R , γ) with range [0, 1]; i.e., prove
Exercise 11.29.

11.31 Fix 0 < ρ < 1 and suppose f ∈ L1(R , γ) is nonnegative and satisﬁes E[ f ] =
1. Note that E[Uρ f ] = 1 as well. The goal of this problem is to show that
Uρ f satisﬁes an improved Markov inequality: Pr[Uρ f > t] = O( 1
tp
ln t ) =

o( 1
t ) as t → ∞. This gives a quantitative sense in which Uρ is a “smoothing
operator”: Uρ f can never look too much like like a step function (the tight
example for Markov’s inequality).
(a) For simplicity, let’s ﬁrst assume ρ = 1/p
2. Given t > p
2, select h > 0
such that ϕ(h) = 1/(p
πt). Show that h ∼ p
2 ln t.
(b) Let H = {z : Uρ f (z) > t}. Show that if H ⊆ (−∞, −h] ∪ [h, ∞), then we

have Pr[Uρ f > t] ≲ p
2/π
tp
ln t , as desired. (Hint: You’ll need Φ(u) < ϕ(u)/u.
(c) Otherwise, we wish to get a contradiction. First, show that there
exists y ∈ (−h, h) and δ0 > 0 such that Uρ f (z) > t for all t ∈ (y − δ0, y +
δ0). (Hint: You’ll need that Uρ f is continuous; see Exercise 11.5.)
(d) For 0 < δ < δ0, deﬁne g ∈ L1(R , γ) by g(z) = 1
2δ 1(y−δ,y+δ). Show that
0 ≤ Uρ g ≤ 1p
π pointwise. (Hint: Why is Uρ g(z) maximized at p
2y?)

(e) Show that 1p
π ≥ 〈 f , Uρ g〉 > t E[g].
(f ) Derive a contradiction by taking δ → 0, thereby showing that indeed
Pr[Uρ f > t] ≲ p
2/π
tp
ln t .
(g) Show that this result is tight by constructing an appropriate f .

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 379

(h) Generalize the above to show that for any ﬁxed 0 < ρ < 1 we have
Pr[Uρ f > t] ≲ 1p
π(1−ρ2) 1
tp
ln t .

11.32 As described in Example 11.73, show that SDPOpt(Z 5) ≥ 1
2 − 1
2 cos 4π
5 =

5
8 + p
5
8 .

11.33 Prove Theorem 11.72.

11.34 Consider the generalization of the Max-Cut CSP in which the variable
set is V , the domain is {−1, 1}, and each constraint is an equality of two
literals, i.e., it’s of the form bF(v) = b′F(v′) for for some v, v′ ∈ V and
b, b′ ∈ {−1, 1}. This CSP is traditionally called Max-E2-Lin. Given an
instance P , write (v, v′, b, b′) ∼ P to denote a uniformly chosen constraint.
The natural SDP relaxation (which can also be solved efﬁciently) is the
following:
 maximize E
(v,v′,b,b′)∼P
 [ 1
2 + 1
2 〈b ⃗U(v), b′ ⃗U(v′)〉]

subject to ⃗U : V → Sn−1.

Show that the Goemans–Williamson algorithm, when using this SDP, is
a (cGWβ, β)-approximation algorithm for Max-E2Lin, and that it also has
the same reﬁned guarantee as in Theorem 11.72.

11.35 This exercise builds on Exercise 11.34. Consider the following instance P
of Max-E2-Lin: The variable set is Z 4 and the constraints are

F(0) = F(1), F(1) = F(2), F(2) = F(3), F(3) = −F(0).

(a) Show that Opt(P ) = 3
4 .
(b) Show that SDPOpt(P ) ≥ 1
2 + 1
2
p
2 . (Hint: Very similar to Exercise 11.32;

you can use four unit vectors at 45
◦ angles in R 2.)
(c) Deduce that SDPOpt(P ) = 1
2 + 1
2p
2 and that this is an optimal SDP
integrality gap for Max-E2Lin. (Cf. Remark 11.76.)

11.36 In our proof of Theorem 11.74 it’s stated that showing the β-Noise Sensi-
tivity Test is a (θ/π, 1
2 − 1
2 cos θ)-Dictator-vs.-No-Notables test implies the
desired UG-hardness of (θ/π + δ, 1
2 − 1
2 cos θ)-approximating Max-Cut (for
any constant δ > 0). There are two minor technical problems with this:
First, the test can only actually be implemented when β is a rational
number. Second, even ignoring this, Theorem 7.40 only directly yields
hardness of (θ/π + δ, 1
2 − 1
2 cos θ − δ)-approximation. Show how to overcome
both technicalities. (Hint: Continuity.)

11.37 Use Corollary 11.59 (and (11.28)) to show that in the setting of the Berry–
Esseen Theorem, |∥S∥1 − p
2/π| ≤ O(γ
1/3). (Cf. Exercise 5.31.)

11.38 The goal of this exercise is to prove Proposition 11.58.
(a) Reduce to the case c = 1.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

380 11. Gaussian space and Invariance Principles

(b) Reduce to the case η = 1. (Hint: Dilate the input by a factor of η.)
(c) Assuming henceforth that c = η = 1, we deﬁne ̃ψ(s) = E[ψ(s + g)] for
g ∼ N(0, 1) as suggested; i.e., ̃ψ = ψ ∗ ϕ, where ϕ is the Gaussian pdf.
Show that indeed ∥ ̃ψ − ψ∥∞ ≤ p
2/π ≤ 1.
(d) To complete the proof we need to show that for all s ∈ R and k ∈ N +

we have | ̃ψ
(k)(s)| ≤ Ck. Explain why, in proving this, we may assume
ψ(s) = 0. (Hint: This requires k ≥ 1.)
(e) Assuming ψ(s) = 0, show | ̃ψ
(k)(s)| = |ψ ∗ ϕ
(k)(s)| ≤ Ck. (Hint: Show
that ϕ
(k)(s) = p(s)ϕ(s) for some polynomial p(s) and use the fact that
Gaussians have ﬁnite absolute moments.)

11.39 Establish the following multidimensional generalization of Proposition 11.58:

Proposition 11.79. Let ψ : R d → R be c-Lipschitz. Then for any η > 0
there exists ̃ψη : R d → R satisfying ∥ψ − ̃ψη∥∞ ≤ cpdη and ∥∂
β ̃ψη∥∞ ≤
C|β| cpd/η
|β|−1 for each multi-index β ∈ N d with |β| = ∑i βi ≥ 1, where Ck
is a constant depending only on k.

11.40 In Exercise 11.38 we “molliﬁed” a function ψ by convolving it with the
(smooth) pdf of a Gaussian random variable. It’s sometimes helpful to
instead use a random variable with bounded support (but still with a
smooth pdf on all of R ). Here we construct such a random variable. Deﬁne
b : R → R by
 b(x) =
 {
exp (− 1
1−x2 ) if −1 < x < 1,

0 else.

(a) Verify that b(x) ≥ 0 for all x and that b(−x) = b(x).
(b) Prove the following statement by induction on k ∈ N : On (−1, 1), the
kth derivative of b at x is of the form p(x)(1 − x2)
−2k · b(x), where p(x)
is a polynomial.
(c) Deduce that b is a smooth (C ∞) function on R .
(d) Verify that C = ∫ 1
−1 b(x) dx satisﬁes 0 < C < ∞ and that we can there-
fore deﬁne a real random variable y, symmetric and supported on
(−1, 1), with the smooth pdf ̃b(y) = b(y)/C. Show also that for k ∈ N ,
the numbers ck = ∥̃b(k)∥∞ are ﬁnite and positive, where ̃b(k) denotes
the kth derivative of ̃b.
(e) Give an alternate proof of Exercise 11.38 using y in place of g.

11.41 Fix u ∈ R , ψ(s) = 1s≤u, and 0 < η < 1/2.
(a) Suppose we approximate ψ by a smooth function ̃ψη as in Exercise 11.38,
i.e., we deﬁne ̃ψη(s) = E[ψ(s + ηg)] for g ∼ N(0, 1). Show that ̃ψη satis-
ﬁes the following properties:
• ̃ψη is a decreasing function with ̃ψη(s) < ψ(s) for s < u and
̃ψη(s) > ψ(s) for s > u.
• | ̃ψη(s) − ψ(s)| ≤ η provided |s − u| ≥ O(η
√log(1/η)).

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 381

• ∥ ̃ψ
(k)
η ∥∞ ≤ Ck/ηk for each k ∈ N , where Ck depends only on k.
(b) Suppose we instead approximate ψ by the function ̃ψη(s) = E[ψ(s +
ηy)], where y is the random variable from Exercise 11.40. Show
that ̃ψη satisﬁes the following slightly nicer properties:
• ̃ψη is a nonincreasing function which agrees with ψ on (∞, u−η]
and on [u + η, ∞).
• ̃ψη is smooth and satisﬁes ∥ ̃ψ
(k)
η ∥∞ ≤ Ck/ηk for each k ∈ N , where Ck
depends only on k.

11.42 Prove Corollary 11.61 by ﬁrst proving

Pr[SY ≤ u − 2η] − O(η
−3)γX Y ≤ Pr[S X ≤ u] ≤ Pr[SY ≤ u + 2η] + O(η
−3)γX Y .

(Hint: Obtain Pr[S X ≤ u − η] ≤ E[ ̃ψη(S X )] ≈ E[ ̃ψη(SY )] ≤ Pr[SY ≤ u + η]
using properties from Exercise 11.41. Then replace u with u +2η and also
interchange S X and SY .)

11.43 (a) Fix q ∈ N . Establish the existence of a smooth function f q : R → R
that is 0 on (−∞, − 1
2 ] and that agrees with some polynomial of degree
exactly q on [ 1
2 , ∞). (Hint: Induction on q; the base case q = 0 is
essentially Exercise 11.41, and the induction step can be achieved by
integration.)
(b) Deduce that for any prescribed sequence a0, a1, a2, . . . that is eventu-
ally constantly 0, there is a smooth function g : R → R that is 0 on
(−∞, − 1
2 ] and has g(k)( 1
2 ) = ak for all k ∈ N .
(c) Fix a univariate polynomial p : R → R . Show that there is a smooth
function ̃ψ : R → R that agrees with p on [−1, 1] and is identically 0
on (−∞, −2] ∪ [2, ∞).

11.44 Establish Corollary 11.70.

11.45 Prove Theorem 11.71.

11.46 (a) By following our proof of the d = 1 case and using the multivariate
Taylor theorem, establish the following:

Invariance Principle for Sums of Random Vectors. Let ⃗X 1, . . . , ⃗X n,
⃗Y 1, . . . ,⃗Y n be independent R d-valued random variables with match-
ing means and covariance matrices; i.e., E[⃗X t] = E[⃗Y t] and Cov[⃗X t] =
Cov[⃗Y t] for all t ∈ [n]. (Note that the d individual components of
a particular ⃗X t or ⃗Y t are not required to be independent.) Write
⃗S X = ∑n
t=1 ⃗X t and ⃗SY = ∑n
t=1 ⃗Y t. Then for any C 3 function ψ : R d → R
satisfying ∥∂
βψ∥∞ ≤ C for all |β| = 3,

∣
∣
∣E[ψ(⃗S X )] − E[ψ(⃗SY )]
∣
∣
∣ ≤ Cγ⃗X ⃗Y ,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

382 11. Gaussian space and Invariance Principles

where
 γ⃗X ⃗Y = ∑

β∈N d

|β|=3
 1

β!
 n∑

t=1
(
E[|⃗X β
t |] + E[|⃗Y β
t |]
)
.

(b) Show that γ⃗X ⃗Y satisﬁes

γ⃗X ⃗Y ≤ d2

6
 n∑

t=1
 d∑

i=1

(
E[|⃗X 3e i
t |] + E[|⃗Y 3e i
t |]
)
.

Here ⃗X 3e i
t denotes the cube of the ith component of vector ⃗X t, and
similarly for ⃗Y t. (Hint: abc ≤ 1
3 (a3 + b3 + c3) for a, b, c ≥ 0.)
(c) Deduce multivariate analogues of the Variant Berry–Esseen Theorem,
Remark 11.56, and Corollary 11.59 (using Proposition 11.79).

11.47 Justify Remark 11.66. (Hint: You’ll need Exercise 10.29.)

11.48 (a) Prove the following:

Multifunction Invariance Principle. Let F (1), . . . , F (d) be formal
n-variate multilinear polynomials each of degree at most k ∈ N . Let
⃗x1, . . . ,⃗xn and ⃗y1, . . . ,⃗yn be independent R d-valued random variables
such that E[⃗xt] = E[⃗yt] = 0 and Mt = Cov[⃗xt] = Cov[⃗yt] for each t ∈ [n].
Assume each Mt has all its diagonal entries equal to 1 (i.e., each of
the d components of ⃗xt has variance 1, and similarly for ⃗yt). Fur-
ther assume each component random variable ⃗x( j)
t and ⃗y( j)
t is (2, 3, ρ)-
hypercontractive (t ∈ [n], j ∈ [d]). Then for any C 3 function ψ : R d → R
satisfying ∥∂
βψ∥∞ ≤ C for all |β| = 3,

∣
∣
∣E[ψ(⃗F(⃗x))] − E[ψ(⃗F(⃗y))]
∣
∣
∣ ≤ Cd2
3 · (1/ρ)3k · n∑

t=1
 d∑

j=1 Inft[F ( j)]3/2.

Here we are using the following notation: If ⃗z = (⃗z1, . . . ,⃗zn) is a se-
quence of R d-valued random variables, ⃗F(⃗z) denotes the vector in R d

whose jth component is F ( j)(⃗z( j)
1 , . . . ,⃗z( j)
n ).

(Hint: Combine the proofs of the Basic Invariance Principle and the
Invariance Principle for Sums of Random Vectors, Exercise 11.46. The
only challenging part should be notation.)
(b) Show that if we further have Var[F ( j)] ≤ 1 and Inft[F ( j)] ≤ ϵ for all
j ∈ [d], t ∈ [n], then
∣
∣
∣E[ψ(⃗F(⃗x))] − E[ψ(⃗F(⃗y))]
∣
∣
∣ ≤ Cd3
3 · k(1/ρ)3k · ϵ1/2.

11.49 (a) Prove the following:

Invariance Principle in general product spaces. Let (Ω, π) be
a ﬁnite probability space, |Ω| = m ≥ 2, in which every outcome has

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 383

probability at least λ. Suppose f ∈ L2(Ωn, π⊗n) has degree at most k;
thus, ﬁxing some Fourier basis φ0, . . . , φm−1 for L2(Ω, π), we have

f = ∑

α∈N n
<m
#α≤k
 ̂f (α)φα.

Introduce indeterminates x = (xi, j)i∈[n], j∈[m−1] and let F be the formal
(m − 1)n-variate polynomial of degree at most k deﬁned by

F(x) = ∑

#α≤k ̂f (α) ∏

i∈supp(α) xi,αi .

Then for any ψ : R → R that is C 3 and satisﬁes ∥ψ′′′∥∞ ≤ C we have
∣
∣
∣
∣ E
x∼{−1,1}(m−1)n[ψ(F(x))] − E
ω∼π⊗n[ψ( f (ω))]
∣
∣
∣
∣ ≤ C
3 · (2
p
2/λ)k · n∑

i=1 Infi[ f ]
3/2.

(Hint: For 0 ≤ t ≤ n, deﬁne ht ∈ L2(Ωt×{−1, 1}
(m−1)(n−t), π⊗t⊗π⊗(m−1)(n−t)
1/2 )
via

ht(ω1, . . . , ωt, xt+1,1, . . . , xn,m−1) = ∑

#α≤k ̂f (α) ∏

i∈supp(α)
i≤t
 φαi (ωi) ∏

i∈supp(α)
i>t
 xi,αi .

Express
 ht = Etht + Ltht = Etht + m∑

j=1 D j · φ j(ωt)

where
 D j = ∑

α:αt= j ̂f (α) ∏

i∈supp(α)
i<t
 φαi (ωi) ∏

i∈supp(α)
i>t
 xi,αi ,

and note that ht−1 = Etht + ∑m
j=1 D j · xt, j.)
(b) In the setting of the previous theorem, show also that
∣
∣
∣
∣ E
g∼N(0,1)(m−1)n[ψ(F(g))] − E
ω∼π⊗n[ψ( f (ω))]
∣
∣
∣
∣ ≤ 2C
3 · (2
p
2/λ)k · n∑

i=1 Infi[ f ]3/2.

(Hint: Apply the Basic Invariance Principle in the form of Exer-
cise 11.47. How can you bound the (m − 1)n inﬂuences of F in terms
of the n inﬂuences of f ?)

11.50 Prove the following version of the General-Volume Majority Is Stablest
Theorem in the setting of general product spaces:

Theorem 11.80. Let (Ω, π) be a ﬁnite probability space in which each out-
come has probability at least λ. Let f ∈ L2(Ωn, π⊗n) have range [0, 1]. Sup-
pose that f has no (ϵ, 1
log(1/ϵ) )-notable coordinates. Then for any 0 ≤ ρ < 1,

Stabρ[ f ] ≤ Λρ(E[ f ]) + O( log log(1/ϵ)
log(1/ϵ) ) · log(1/λ)
1−ρ .

(Hint: Naturally, you’ll need Exercise 11.49(b).)

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

384 11. Gaussian space and Invariance Principles

Notes. The subject of Gaussian space is too enormous to be surveyed here;
some recommended texts include Janson [Jan97] and Bogachev [Bog98], the
latter having an extremely thorough bibliography. The Ornstein–Uhlenbeck
semigroup dates back to the work of Uhlenbeck and Ornstein [UO30] whose
motivation was to reﬁne Einstein’s theory of Brownian motion [Ein05] to
take into account the inertia of the particle. The relationship between the
action of Uρ on functions and on Hermite expansions (i.e., Proposition 11.31)
dates back even further, to Mehler [Meh66]. Hermite polynomials were ﬁrst
deﬁned by Laplace [Lap11], and then studied by Chebyshev [Che60] and Her-
mite [Her64]. See Lebedev [Leb72, Chapter 4.15] for a proof of the pointwise
convergence of a piecewise-C 1 function’s Hermite expansion.

As mentioned in Chapter 9.7, the Gaussian Hypercontractivity Theorem
is originally due to Nelson [Nel66] and now has many known proofs. The idea
behind the proof we presented – ﬁrst proving the Boolean hypercontractivity
result and then deducing the Gaussian case by the Central Limit Theorem
– is due to Gross [Gro75] (see also Trotter [Tro58]). Gross actually used
the idea to prove his Gaussian Log-Sobolev Inequality, and thereby deduced
the Gaussian Hypercontractivity Theorem. Direct proofs of the Gaussian
Hypercontractivity Theorem have been given by Neveu [Nev76] (using sto-
chastic calculus), Brascamp and Lieb [BL76] (using rearrangement), and
Ledoux [Led13] (using a variation on Exercises 11.26–11.29); direct proofs of
the Gaussian Log-Sobolev Inequality have been given by Adams and Clarke
[AC79], by Bakry and Émery [BÉ85], and by Ledoux [Led92], the latter two
using semigroup techniques. Bakry’s survey [Bak94] on these topics is also
recommended.

The Gaussian Isoperimetric Inequality was ﬁrst proved independently
by Borell [Bor75] and by Sudakov and Tsirel’son [ST78]. Both works de-
rived the result by taking the isoperimetric inequality on the sphere (due
to Lévy [Lév22] and Schmidt [Sch48], see also Figiel, Lindenstrauss, and
Milman [FLM77]) and then taking “Poincaré’s limit” – i.e., viewing Gaussian
space as a projection of the sphere of radius pn in n dimensions, with n → ∞
(see Lévy [Lév22], McKean [McK73], and Diaconis and Freedman [DF87]).
Ehrhard [Ehr83] gave a different proof using a symmetrization argument
intrinsic to Gaussian space. This may be compared to the alternate proof of
the spherical isoperimetric inequality [Ben84] based on the “two-point sym-
metrization” of Baernstein and Taylor [BT76] (analogous to Riesz rearrange-
ment in Euclidean space and to the polarization operation from Exercise 2.52).

To carefully deﬁne Gaussian surface area for a broad class of sets re-
quires venturing into the study of geometric measure theory and functions
of bounded variation. For a clear and comprehensive development in the Eu-
clidean setting (including the remark in Exercise 11.15(b)), see the book by

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 385

Ambrosio, Fusco, and Pallara [AFP00]. There’s not much difference between
the Euclidean and ﬁnite-dimensional Gaussian settings; research on Gauss-
ian perimeter tends to focus on the trickier inﬁnite-dimensional case. For a
thorough development of surface area in this latter setting (which of course
includes ﬁnite-dimensional Gaussian space as a special case) see the work of
Ambrosio, Miranda, Maniglia, and Pallara [AMMP10]; in particular, Theo-
rem 4.1 in that work gives several additional equivalent deﬁnitions for surfγ
besides those in Deﬁnition 11.48. Regarding the fact that RS′
A(0+) is an
equivalent deﬁnition, the Euclidean analogue of this statement was proven in
Miranda et al. [MPPP07] and the statement itself follows similarly [Mir13]
using Ambrosio et al. [AFR13]. (Our heuristic justiﬁcation of (11.14) is simi-
lar to the one given by Kane [Kan11].) Additional related results can be found
in Hino [Hin10] (which includes the remark about convex sets at the end of
Deﬁnition 11.48), Ambrosio and Figalli [AF11], Miranda et al. [MNP12], and
Ambrosio et al. [AFR13].

The inequality of Theorem 11.51 is explicit in Ledoux [Led94] (see also
the excellent survey [Led96]); he used it to deduce the Gaussian Isoperimet-
ric Inequality. He also noted that it’s essentially deducible from an earlier
inequality of Pisier and Maurey [Pis86, Theorem 2.2]. Theorem 11.43, which
expresses the subadditivity of rotation sensitivity, can be viewed as a dis-
cretization of the Pisier–Maurey inequality. This theorem appeared in work
of Kindler and O’Donnell [KO12], which also made the observations about
the volume- 1
2 case of Borell’s Isoperimetric Theorem at the end of Section 11.3
and in Remark 11.76.

Bobkov’s Inequality [Bob97] in the special case of Gaussian space had
already been implicitly established by Ehrhard [Ehr84]; the striking nov-
elty of Bobkov’s work (partially inspired by Talagrand [Tal93]) was his re-
duction to the two-point Boolean inequality. The proof of this inequality
which we presented is, as mentioned a discretization of the stochastic cal-
culus proof of Barthe and Maurey [BM00]. (In turn, they were extending
the stochastic calculus proof of Bobkov’s Inequality in the Gaussian setting
due to Capitaine, Hsu, and Ledoux [CHL97].) The idea that it’s enough
to show that Claim 11.54 is “nearly true” by computing two derivatives
– as opposed to showing it’s exactly true by computing four derivatives –
was communicated to the author by Yuval Peres. Following Bobkov’s pa-
per, Bakry and Ledoux [BL96] established Theorem 11.55 in very general
inﬁnite-dimensional settings including Gaussian space; Ledoux [Led98] fur-
ther pointed out that the Gaussian version of Bobkov’s Inequality has a very
short and direct
semigroup-based proof. See also Bobkov and Götze [BG99] and Tillich and
Zémor [TZ00] for results similar to Bobkov’s Inequality in other discrete set-
tings.
 Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

386 11. Gaussian space and Invariance Principles

Borell’s Isoperimetric Theorem is from Borell [Bor85]. Borell’s proof used
“Ehrhard symmetrization” and actually gave much stronger results – e.g.,
that if f , g ∈ L2(R n, γ) are nonnegative and q ≥ 1, then 〈(Uρ f )q, g〉 can only
increase under simultaneous Ehrhard symmetrization of f and g. There are
at least four other known proofs of the basic Borell Isoperimetric Theorem.
Beckner [Bec92] observed that the analogous isoperimetric theorem on the
sphere follows from two-point symmetrization; this yields the Gaussian result
via Poincaré’s limit (for details, see Carlen and Loss [CL90]). (This proof is
perhaps the conceptually simplest one, though carrying out all the technical
details is a chore.) Mossel and Neeman [MN12] gave the proof based on
semigroup methods outlined in Exercises 11.26–11.29, and later together
with De [DMN12] gave a “Bobkov-style” Boolean proof (see Exercise 11.30).
Finally, Eldan [Eld13] gave a proof using stochastic calculus.

As mentioned in Section 11.5 there are several known ways to prove the
Berry–Esseen Theorem. Aside from the original method (characteristic func-
tions), there is also Stein’s Method [Ste72, Ste86b]; see also, e.g., [Bol84,
BH84, CGS11]. The Replacement Method approach we presented originates
in the work of Lindeberg [Lin22]. The molliﬁcation techniques used (e.g.,
those in Exercise 11.40) are standard. The Invariance Principle as presented
in Section 11.6 is from Mossel, O’Donnell, and Oleszkiewicz [MOO10]. Fur-
ther extensions (e.g., Exercise 11.48) appear in the work of Mossel [Mos10].
In fact the Invariance Principle dates back to the 1971 work of Rotar’ [Rot73,
Rot74]; therein he essentially proved the Invariance Principle for degree-2
multilinear polynomials (even employing the term “inﬂuence” as we do for
the quantity in Deﬁnition 11.63). Earlier work on extending the Central
Limit Theorem to higher-degree polynomials had focused on obtaining sufﬁ-
cient conditions for polynomials (especially quadratics) to have a Gaussian
limit distribution; this is the subject of U-statistics. Rotar’ emphasized the
idea of invariance and of allowing any (quadratic) polynomial with low in-
ﬂuences. Rotar’ also credited Girko [Gir73] with related results in the case
of positive deﬁnite quadratic forms. In 1975, Rotar’ [Rot75] generalized his
results to handle multilinear polynomials of any constant degree, and also
random vectors (as in Exercise 11.48). (Rotar’ also gave further reﬁnements
in 1979 [Rot79].)

The difference between the results of Rotar’ [Rot75] and the results of
Mossel et al. [MOO10] comes in the treatment of the error bounds. It’s some-
what difﬁcult to extract simple-to-state error bounds from Rotar’ [Rot75], as
the error there is presented as a sum over i ∈ [n] of expressions E[F(x)1|F(x)|>ui ],
where ui involves Infi[F]. (Partly this is so as to generalize the statement
of the Lindeberg CLT.) Nevertheless, the work of Rotar’ implies a Lévy dis-
tance bound as in Corollary 11.70, with some inexplicit function oϵ(1) in place
of (1/ρ)O(k)ϵ1/8. By contrast, the work of Mossel et al. [MOO10] shows that

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

11.8. Exercises and notes 387

a straightforward combination of the Replacement Method and hypercon-
tractivity yields good, explicit error bounds. Regarding the Carbery–Wright
Theorem [CW01], an alternative exposition appears in Nazarov, Sodin, and
Vol’berg [NSV02].

Regarding the Majority Is Stablest Theorem (conjectured in Khot, Kindler,
Mossel, and O’Donnell [KKMO04] and proved originally in Mossel, O’Donnell,
and Oleszkiewicz [MOO05b]), it can be added that additional motivation for
the conjecture came from Kalai [Kal02]. The fact that (SDP) is an efﬁciently
computable relaxation for the Max-Cut problem dates back to the 1990 work
of Delorme and Poljak [DP93]; however, they were unable to give an anal-
ysis relating its value to the optimum cut value. In fact, they conjectured
that the case of the 5-cycle from Example 11.73 had the worst ratio of Opt(G)
to SDPOpt(G). Goemans and Williamson [GW94] were the ﬁrst to give a
sharp analysis of the SDP (Theorem 11.72), at least for θ ≥ θ∗. Feige and
Schechtman [FS02] showed an optimal integrality gap for the SDP for all
values θ ≥ θ∗ (in particular, showing an integrality gap ratio of cGW); inter-
estingly, their construction essentially involved proving Borell’s Isoperimetric
Inequality (though they did it on the sphere rather than in Gaussian space).
Both before and after the Khot et al. [KKMO04] UG-hardness result for
Max-Cut there was a long line of work [Kar99, Zwi99, AS00, ASZ02, CW04,
KV05, FL06, KO06] devoted to improving the known approximation algo-
rithms and UG-hardness results, in particular for θ < θ∗. This culminated
in the results from O’Donnell and Wu [OW08] (mentioned in Remark 11.75),
which showed explicit matching (α, β)-approximation algorithms, integral-
ity gaps, and UG-hardness results for all 1
2 < β < 1. The fact that the best
integrality gaps matched the best UG-hardness results proved not to be a co-
incidence; in contemporaneous work, Raghavendra [Rag08] showed that for
any CSP, any SDP integrality gap could be turned into a matching Dictator-
vs.-No-Notables test. This implies the existence of matching efﬁcient (α, β)-
approximation algorithms and UG-hardness results for every CSP and ev-
ery β. See Raghavendra’s thesis [Rag09] for full details of his earlier publica-
tion [Rag08] (including some Invariance Principle extensions building further
on Mossel [Mos10]); see also Austrin’s work [Aus07, Aus10] for precursors
to the Raghavendra theory.

Exercise 11.31 concerns a problem introduced by Talagrand [Tal89]. Tala-
grand offers a $1,000 prize [Tal06] for a solution to the following Boolean ver-
sion of the problem: Show that for any ﬁxed 0 < ρ < 1 and for f : {−1, 1}n → R ≥0

with E[ f ] = 1 it holds that Pr[Tρ f > t] = o(1/t) as t → ∞. (The rate of decay
may depend on ρ but not, of course, on n; in fact, a bound of the form O( 1
tp
log t )

is expected.) The result outlined in Exercise 11.31 (obtained together with
James Lee) is for the very special case of 1-dimensional Gaussian space; Ball,

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

388 11. Gaussian space and Invariance Principles

Barthe, Bednorz, Oleszkiewicz, and Wolff [BBB
+13] obtained the same result
and also showed a bound of O( log log t

tp
log t ) for d-dimensional Gaussian space (but

with the constant in the O(·) depending on d).

The Multifunction Invariance Principle (Exercise 11.48 and its special
case Exercise 11.46) are from Mossel [Mos10]; the version for general product
spaces (Exercise 11.49) is from Mossel, O’Donnell, and Oleszkiewicz [MOO10].

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Some tips

• You might try using analysis of Boolean functions whenever you’re faced
with a problems involving Boolean strings in which both the uniform
probability distribution and the Hamming graph structure play a role.
More generally, the tools may still apply when studying functions on (or
subsets of) product probability spaces.

• If you’re mainly interested in unbiased functions, or subsets of volume 1
2 ,
use the representation f : {−1, 1}n → {−1, 1}. If you’re mainly interested
in subsets of small volume, use the representation f : {−1, 1}n → {0, 1}.

• As for the domain, if you’re interested in the operation of adding two
strings (modulo 2), use F n
2 . Otherwise use {−1, 1}n.

• If you have a conjecture about Boolean functions:
– Test it on dictators, majority, parity, tribes (and maybe recursive
majority of 3). If it’s true for these functions, it’s probably true.
– Try to prove it by induction on n.
– Try to prove it in the special case of functions on Gaussian space.

• Try not to prove any bound on Boolean functions f : {−1, 1}n → {−1, 1}
that involves the parameter n.

• Analytically, the only multivariate polynomials we really know how to
control are degree-1 polynomials. Try to reduce to this case if you can.

• Hypercontractivity is useful in two ways: (i) It lets you show that low-
degree functions of independent random variables behave “reasonably”.
(ii) It implies that the noisy hypercube graph is a small-set expander.

• Almost any result about functions on the hypercube extends to the case
of the p-biased cube, and more generally, to the case of functions on
products of discrete probability spaces in which every outcome has prob-
ability at least p – possibly with a dependence on p, though.

• Every Boolean function consists of a junta part and Gaussian part.
 389

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography

[AA11] Scott Aaronson and Andris Ambainis. The need for structure in quantum
speedups. In Proceedings of the 2nd Annual Innovations in Theoretical Computer
Science conference, pages 338–352, 2011.

[Aar08] Scott Aaronson. How to solve longstanding open problems in quantum computing
using only Fourier Analysis. Lecture at Banff International Research Station,
2008. http://www.scottaaronson.com/talks/openqc.ppt .

[ABH+05] Sanjeev Arora, Eli Berger, Elad Hazan, Guy Kindler, and Muli Safra. On non-
approximability for quadratic programs. In Proceedings of the 46th Annual IEEE
Symposium on Foundations of Computer Science, pages 206–215, 2005.

[ABI85] Noga Alon, László Babai, and Alon Itai. A fast and simple randomized algorithm
for the maximal independent set problem. Journal of Algorithms, 7(4):567–583,
1985.

[AC79] Robert Adams and Frank Clarke. Gross’s logarithmic Sobolev inequality: a simple
proof. American Journal of Mathematics, 101(6):1265–1269, 1979.

[AF99] Dimitris Achlioptas and Ehud Friedgut. A sharp threshold for k-colorability. Ran-
dom Structures & Algorithms, 14(1):63–70, 1999.

[AF11] Luigi Ambrosio and Alessio Figalli. Surface measures and convergence of the
Ornstein–Uhlenbeck semigroup in Wiener spaces. Annales de la faculté des sci-
ences de Toulouse Mathématiques (série 6), 20(2):407–438, 2011.

[AFP00] Luigi Ambrosio, Nicola Fusco, and Diego Pallara. Functions of bounded variation
and free discontinuity problems. Oxford University Press, 2000.

[AFR13] Luigi Ambrosio, Alessio Figalli, and Eris Runa. On sets of ﬁnite perimeter in
Wiener spaces: reduced boundary and convergence to halfspaces. Atti della Ac-
cademia Nazionale dei Lincei. Classe di Scienze Fisiche, Matematiche e Naturali.
Rendiconti Lincei. Serie IX. Matematica e Applicazioni, 24(1):111–122, 2013.

[AG76] Rudolf Ahlswede and Péter Gács. Spreading of sets in product spaces and hy-
percontraction of the Markov operator. The Annals of Probability, 4(6):925–939,
1976.

[AGHP92] Noga Alon, Oded Goldreich, Johan Håstad, and René Peralta. Simple construc-
tions of almost k-wise independent random variables. Random Structures & Al-
gorithms, 3(3):289–304, 1992.
 391

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

392 Bibliography

[Ajt83] Miklós Ajtai. Σ1
1-formulae on ﬁnite structures. Annals of Pure and Applied Logic,
24(1):1–48, 1983.

[AL93] Miklós Ajtai and Nathal Linial. The inﬂuence of large coalitions. Combinatorica,
13(2):129–145, 1993.

[ALM+98] Sanjeev Arora, Carsten Lund, Rajeev Motwani, Madhu Sudan, and Mario
Szegedy. Proof veriﬁcation and the hardness of approximation problems. Jour-
nal of the ACM, 45(3):501–555, 1998.

[Ama11] Kazuyuki Amano. Tight bounds on the average sensitivity of k-CNF. Theory of
Computing, 7(1):45–48, 2011.

[Amb03] Andris Ambainis. Polynomial degree vs. quantum query complexity. In Proceed-
ings of the 44th Annual IEEE Symposium on Foundations of Computer Science,
pages 230–239, 2003.

[AMMP10] Luigi Ambrosio, Michele Miranda Jr., Stefania Maniglia, and Diego Pallara. BV
functions in abstract Wiener spaces. Journal of Functional Analysis, 258(3):785–
813, 2010.

[AN05] Dimitris Achlioptas and Assaf Naor. The two possible values of the chromatic
number of a random graph. Annals of Mathematics, 162(3):1335–1351, 2005.

[Arr50] Kenneth Arrow. A difﬁculty in the concept of social welfare. The Journal of Politi-
cal Economy, 58(4):328–346, 1950.

[Arr63] Kenneth Arrow. Social choice and individual values. Cowles Foundation, 1963.

[AS98] Sanjeev Arora and Shmuel Safra. Probabilistic checking of proofs: A new charac-
terization of NP. Journal of the ACM, 45(1):70–122, 1998.

[AS00] Noga Alon and Benjamin Sudakov. Bipartite subgraphs and the smallest eigen-
value. Combinatorics, Probability and Computing, 9(1):1–12, 2000.

[AS08] Noga Alon and Joel Spencer. The Probabilistic Method. Wiley–Interscience, third
edition, 2008.

[ASZ02] Noga Alon, Benny Sudakov, and Uri Zwick. Constructing worst case instances
for semideﬁnite programming based approximation algorithms. SIAM Journal on
Discrete Mathematics, 15(1):58–72, 2002.

[Aus07] Per Austrin. Balanced Max-2Sat might not be hardest. In Proceedings of the 39th
Annual ACM Symposium on Theory of Computing, pages 189–197, 2007.

[Aus08] Per Austrin. Conditional Inapproximability and Limited Independence. PhD the-
sis, KTH Royal Institute of Technology, 2008.

[Aus10] Per Austrin. Towards sharp inapproximability for any 2-CSP. SIAM Journal On
Computing, 39(6):2430–2463, 2010.

[Bak94] Dominique Bakry. L’hypercontractivité et son utilisation en théorie des semi-
groupes. In Lectures on probability theory (Saint-Flour, 1992), volume 1581 of
Lecture Notes in Mathematics, pages 1–114. Springer, Berlin, 1994.

[Bal93] Keith Ball. The reverse isoperimetric problem for Gaussian measure. Discrete
and Computational Geometry, 10(4):411–420, 1993.

[Bal13] Deepak Bal. On sharp thresholds of monotone properties: Bourgain’s proof revis-
ited. Technical Report 1302.1162, arXiv, 2013.

[Ban65] John Banzhaf. Weighted voting doesn’t work: A mathematical analysis. Rutgers
Law Review, 19:317–343, 1965.

[BBB+13] Keith Ball, Franck Barthe, Witold Bednorz, Krzysztof Oleszkiewicz, and
Paweł Wolff. L1-smoothing for the Ornstein–Uhlenbeck semigroup. Mathematika,
59(1):160–168, 2013.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 393

[BBH+12] Boaz Barak, Fernando Brandão, Aram Harrow, Jonathan Kelner, David Steurer,
and Yuan Zhou. Hypercontractivity, sum-of-squares proofs, and their applications.
In Proceedings of the 44th Annual ACM Symposium on Theory of Computing,
pages 307–326, 2012.

[BC99] Anna Bernasconi and Bruno Codenotti. Spectral analysis of Boolean functions
as a graph eigenvalue problem. IEEE Transactions on Computers, 48(3):345–351,
1999.

[BCH+96] Mihir Bellare, Don Coppersmith, Johan Håstad, Marcos Kiwi, and Madhu Sudan.
Linearity testing in characteristic two. IEEE Transactions on Information Theory,
42(6):1781–1795, 1996.

[BÉ85] Dominiques Bakry and Michel Émery. Diffusions hypercontractives. In Séminaire
de Probabilités, XIX, volume 1123 of Lecture Notes in Mathematics, pages 177–
206. Springer, Berlin, 1985.

[Bea94] Paul Beame. A switching lemma primer. Technical Report UW-CSE-95-07-01,
University of Washington, 1994.

[Bec75] William Beckner. Inequalities in Fourier analysis. Annals of Mathematics,
102:159–182, 1975.

[Bec92] William Beckner. Sobolev inequalities, the Poisson semigroup, and analysis on the
sphere Sn. Proceedings of the National Academy of Sciences, 89(11):4816–4819,
1992.

[BEHW87] Anselm Blumer, Andrzej Ehrenfeucht, David Haussler, and Manfred Warmuth.
Occam’s razor. Information Processing Letters, 24(6):377–380, 1987.

[Ben84] Yoav Benyamini. Two-point symmetrization, the isoperimetric inequality on the
sphere and some applications. In Texas functional analysis seminar, 1983–1984,
volume 1984, pages 53–76, 1984.

[Ben04] Vidmantas Bentkus. A Lyapunov type bound in Rd. Rossi˘ıskaya Akademiya
Nauk. Teoriya Veroyatnoste˘ı i ee Primeneniya, 49(2):400–410, 2004.

[Ber41] Andrew Berry. The accuracy of the Gaussian approximation to the sum of indepen-
dent variates. Transactions of the American Mathematical Society, 49(1):122–139,
1941.

[BG99] Sergey Bobkov and Friedrich Götze. Discrete isoperimetric and Poincaré-type
inequalities. Probability Theory and Related Fields, 114(2):245–277, 1999.

[BGR09] Steven Brams, William Gehrlein, and Fred Roberts, editors. The Mathematics of
Preference, Choice and Order. Springer, 2009.

[BGS95] Mihir Bellare, Oded Goldreich, and Madhu Sudan. Free bits, PCPs, and non-
approximability – towards tight results. Technical Report TR95-024, Electronic
Colloquium on Computational Complexity, 1995.

[BGS98] Mihir Bellare, Oded Goldreich, and Madhu Sudan. Free bits, PCPs, and non-
approximability – towards tight results. SIAM Journal of Computing, 27(3):804–
915, 1998.

[BH57] Simon Broadbent and John Hammersley. Percolation processes I. Crystals
and mazes. Mathematical Proceedings of the Cambridge Philosophical Society,
53(3):629–641, 1957.

[BH84] Andrew Barbour and Peter Hall. Stein’s method and the Berry–Esseen theorem.
Australian Journal of Statistics, 26(1):8–15, 1984.

[BI87] Manuel Blum and Russell Impagliazzo. Generic oracles and oracle classes. In
Proceedings of the 28th Annual IEEE Symposium on Foundations of Computer
Science, pages 118–126, 1987.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

394 Bibliography

[Bik66] Algimantas Bikelis. Estimates of the remainder in a combinatorial central limit
theorem. Litovskii Matematicheskii Sbornik, 6(3):323–346, 1966.

[BKK+92] Jean Bourgain, Jeff Kahn, Gil Kalai, Yitzhak Katznelson, and Nathan Linial. The
inﬂuence of variables in product spaces. Israel Journal of Mathematics, 77(1):55–
64, 1992.

[BKS99] Itai Benjamini, Gil Kalai, and Oded Schramm. Noise sensitivity of Boolean func-
tions and applications to percolation. Publications Mathématiques de l’IHÉS,
90(1):5–43, 1999.

[BL76] Herm Brascamp and Elliott Lieb. Best constants in Young’s inequality, its con-
verse, and its generalization to more than three functions. Advances in Mathe-
matics, 20(2):151–173, 1976.

[BL85] Michael Ben-Or and Nathan Linial. Collective coin ﬂipping, robust voting
schemes and minima of Banzhaf values. In Proceedings of the 26th Annual IEEE
Symposium on Foundations of Computer Science, pages 408–416, 1985.

[BL90] Michael Ben-Or and Nathan Linial. Collective coin ﬂipping. In Silvio Micali and
Franco Preparata, editors, Randomness and Computation, volume 5 of Advances
in Computing Research: A research annual, pages 91–115. JAI Press, 1990.

[BL96] Dominique Bakry and Michel Ledoux. Lévy–Gromov’s isoperimetric inequal-
ity for an inﬁnite dimensional diffusion generator. Inventiones mathematicae,
123(1):259–281, 1996.

[BL98] Sergey Bobkov and Michel Ledoux. On modiﬁed logarithmic Sobolev inequalities
for Bernoulli and Poisson measures. Journal of Functional Analysis, 156(2):347–
365, 1998.

[Bla57] Julian Blau. The existence of social welfare functions. Econometrica, 25(2):302–
313, 1957.

[BLR90] Manuel Blum, Michael Luby, and Ronitt Rubinfeld. Self-testing/correcting with
applications to numerical problems. In Proceedings of the 22nd Annual ACM
Symposium on Theory of Computing, pages 73–83, 1990.

[Blu03] Avrim Blum. Learning a function of r relevant variables. In Bernhard Schölkopf
and Manfred Warmuth, editors, Proceedings of the 16th Annual Conference on
Learning Theory, volume 2777 of Lecture Notes in Computer Science, pages 731–
733. Springer, 2003.

[BM00] Franck Barthe and Bernard Maurey. Some remarks on isoperimetry of Gaussian
type. Annales de l’Institut Henri Poincaré. Probabilités et Statistiques, 36(4):419–
434, 2000.

[Bob97] Sergey Bobkov. An isoperimetric inequality on the discrete cube and an elemen-
tary proof of the isoperimetric inequality in Gauss space. Annals of Probability,
25(1):206–214, 1997.

[Bog98] Vladimir Bogachev. Gaussian Measures. Mathematical Series and Monographs.
American Mathematical Society, 1998.

[BOH90] Yigal Brandman, Alon Orlitsky, and John Hennessy. A spectral lower bound
technique for the size of decision trees and two-level AND/OR circuits. IEEE
Transactions on Computers, 39(2):282–287, 1990.

[Bol84] Erwin Bolthausen. An estimate of the remainder in a combinatorial central limit
theorem. Probability Theory and Related Fields, 66(3):379–386, 1984.

[Bol01] Béla Bollobás. Random Graphs. Cambridge Studies in Advanced Mathematics,
Cambridge University Press, Cambridge, 2001.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 395

[Bon68] Aline Bonami. Ensembles Λ(p) dans le dual de D∞. Annales de l’Institut Fourier,
18(2):193–204, 1968.

[Bon70] Aline Bonami. Étude des coefﬁcients Fourier des fonctions de L p(G). Annales de
l’Institut Fourier, 20(2):335–402, 1970.

[Bop97] Ravi Boppana. The average sensitivity of bounded-depth circuits. Information
Processing Letters, 63(5):257–261, 1997.

[Bor75] Christer Borell. The Brunn–Minkowski inequality in Gauss space. Inventiones
Mathematicae, 30(2):207–216, 1975.

[Bor79] Christer Borell. On the integrability of Banach space valued Walsh polynomials.
In Séminaire de Probabilités, XIII, volume 721 of Lecture Notes in Mathematics,
pages 1–3. Springer, Berlin, 1979.

[Bor82] Christer Borell. Positivity improving operators and hypercontractivity. Mathema-
tische Zeitschrift, 180(2):225–234, 1982.

[Bor84] Christer Borell. On polynomial chaos and integrability. Probabability and Mathe-
matical Statistics, 3(2):191–203, 1984.

[Bor85] Christer Borell. Geometric bounds on the Ornstein–Uhlenbeck velocity process.
Probability Theory and Related Fields, 70(1):1–13, 1985.

[Bou79] Jean Bourgain. Walsh subspaces of l p product spaces. In Séminaire D’Analyse
Fonctionnelle, pages IV.1–IV.9. École Polytechnique, Centre De Mathématiques,
1979.

[Bou99] Jean Bourgain. On sharp thresholds of monotone properties. Journal of the Amer-
ican Mathematical Society, 12(4):1046–1053, 1999. Appendix to the main paper,
Sharp thresholds of graph properties, and the k-sat problem by Ehud Friedgut.

[BOW10] Eric Blais, Ryan O’Donnell, and Karl Wimmer. Polynomial regression under arbi-
trary product distributions. Machine Learning, 80(2):273–294, 2010.

[BR73] Leonid Balashov and Aleksandr Rubinshtein. Series with respect to the Walsh
system and their generalizations. Journal of Soviet Mathematics, 1(6):727–763,
1973.

[BR08] Béla Bollobás and Oliver Riordan. Random graphs and branching processes. In
Béla Bollobás, Robert Kozma, and Dezs˝o Miklós, editors, Handbook of large-scale
random networks, pages 15–116. Springer, 2008.

[Bra87] Yigal Brandman. Spectral lower-bound techniques for logic circuits. PhD thesis,
Stanford University, 1987.

[Bru90] Jehoshua Bruck. Harmonic analysis of polynomial threshold functions. SIAM
Journal on Discrete Mathematics, 3(2):168–177, 1990.

[BS92] Jehoshua Bruck and Roman Smolensky. Polynomial threshold functions, AC0

functions and spectral norms. SIAM Journal on Computing, 21(1):33–42, 1992.

[BS08] Eli Ben-Sasson and Madhu Sudan. Short PCPs with polylog query complexity.
SIAM Journal on Computing, 38(2):551–607, 2008.

[BSGH+04] Eli Ben-Sasson, Oded Goldreich, Prahladh Harsha, Madhu Sudan, and Salil
Vadhan. Robust PCPs of proximity, shorter PCPs and applications to coding. In
Proceedings of the 36th Annual ACM Symposium on Theory of Computing, pages
1–10, 2004.

[BSSVW03] Eli Ben-Sasson, Madhu Sudan, Salil Vadhan, and Avi Wigderson. Randomness-
efﬁcient low degree tests and short PCPs via epsilon-biased sets. In Proceedings
of the 35th Annual ACM Symposium on Theory of Computing, pages 612–621,
2003.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

396 Bibliography

[BSW05] Itai Benjamini, Oded Schramm, and David Wilson. Balanced Boolean functions
that can be evaluated so that every input bit is unlikely to be read. In Proceedings
of the 37th Annual ACM Symposium on Theory of Computing, pages 244–250,
2005.

[BT76] Albert Baernstein and Bert Taylor. Spherical rearrangements, subharmonic func-
tions, and ∗-functions in n-space. Duke Mathematical Journal, 43(2):245–268,
1976.

[BT87] Béla Bollobás and Andrew Thomason. Threshold functions. Combinatorica,
7(1):35–38, 1987.

[BT96] Nader Bshouty and Christino Tamon. On the Fourier spectrum of monotone
functions. Journal of the ACM, 43(4):747–770, 1996.

[BT09] Avraham Ben-Aroya and Amnon Ta-Shma. Constructing small-bias sets from
algebraic-geometric codes. In Proceedings of the 50th Annual IEEE Symposium
on Foundations of Computer Science, pages 191–197, 2009.

[BV07] Andrej Bogdanov and Emanuele Viola. Pseudorandom bits for polynomials. In
Proceedings of the 48th Annual IEEE Symposium on Foundations of Computer
Science, pages 41–51, 2007.

[Car10] Claude Carlet. Boolean functions for cryptography and error-correcting codes. In
Yves Crama and Peter Hammer, editors, Boolean models and methods in mathe-
matics, computer science, and engineering, pages 257–397. Cambridge University
Press, 2010.

[CFG+85] Benny Chor, Joel Friedman, Oded Goldreich, Johan Håstad, Steven Rudich, and
Roman Smolensky. The bit extraction problem or t-resilient functions. In Proceed-
ings of the 26th Annual IEEE Symposium on Foundations of Computer Science,
pages 396–407, 1985.

[CG92] Fan Chung and Ronald Graham. Quasi-random subsets of Zn. Journal of Combi-
natorial Theory, Series A, 61:64–86, 1992.

[CGG87] Benny Chor and Mihály Geréb-Graus. On the inﬂuence of single participant in
coin ﬂipping schemes. Technical report, Harvard University, 1987.

[CGG88] Benny Chor and Mihály Geréb-Graus. On the inﬂuence of single participant
in coin ﬂipping schemes. SIAM Journal on Discrete Mathematics, 1(4):411–415,
1988.

[CGS11] Louis Chen, Larry Goldstein, and Qi-Man Shao. Normal approximation by Stein’s
method. Springer, 2011.

[CGW89] Fan Chung, Ronald Graham, and Richard Wilson. Quasi-random graphs. Combi-
natorica, 9(4):345–362, 1989.

[Che60] Pafnuty Chebyshev. Sur le développement des fonctions à une seule variable.
Bulletin de l’Académie impériale des sciences de St.-Pétersbourg, 1:193–200, 1860.

[CHL97] Mireille Capitaine, Elton Hsu, and Michel Ledoux. Martingale representation
and a simple proof of logarithmic Sobolev inequalities on path spaces. Electronic
Communications in Probability, 2:71–81, 1997.

[Cho61] Chao-Kong Chow. On the characterization of threshold functions. In Proceedings
of the 2nd Annual Symposium on Switching Circuit Theory and Logical Design
(FOCS), pages 34–38, 1961.

[CKS01] Nadia Creignou, Sanjeev Khanna, and Madhu Sudan. Complexity classiﬁcations
of Boolean constraint satisfaction problems. Society for Industrial and Applied
Mathematics, 2001.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 397

[CL90] Eric Carlen and Michael Loss. Extremals of functionals with competing symme-
tries. Journal of Functional Analysis, 88(2):437–456, 1990.

[Col71] John Coleman. Control of collectivities and the power of a collectivity to act. In
Bernhardt Lieberman, editor, Social Choice. Gordon and Breach, 1971.

[CW01] Anthony Carbery and James Wright. Distributional and Lq norm inequalities for
polynomials over convex bodies in Rn. Mathematical Research Letters, 8(3):233–
248, 2001.

[CW04] Moses Charikar and Anthony Wirth. Maximizing quadratic programs: extending
Grothendieck’s Inequality. In Proceedings of the 45th Annual IEEE Symposium
on Foundations of Computer Science, pages 54–60, 2004.

[dC85] Nicolas de Condorcet. Essai sur l’application de l’analyse à la probabilité des
décisions rendues à la pluralité des voix. Paris, de l’imprimerie royale, 1785.

[DF87] Persi Diaconis and David Freedman. A dozen de Finetti-style results in search of
a theorem. Annales de l’Institut Henri Poincaré (B), 23(S2):397–423, 1987.

[DFKO07] Irit Dinur, Ehud Friedgut, Guy Kindler, and Ryan O’Donnell. On the Fourier
tails of bounded functions over the discrete cube. Israel Journal of Mathematics,
160(1):389–412, 2007.

[DHK+10] Ilias Diakonikolas, Prahladh Harsha, Adam Klivans, Raghu Meka, Prasad
Raghavendra, Rocco Servedio, and Li-Yang Tan. Bounding the average sensi-
tivity and noise sensitivity of polynomial threshold functions. In Proceedings of
the 42nd Annual ACM Symposium on Theory of Computing, pages 533–542, 2010.

[Dic01] Leonard Dickson. Linear groups with an exposition of Galois ﬁeld theory. B. G.
Teubner, 1901.

[Dil72] John Dillon. A survey of bent functions. NSA Technical Journal, pages 191–215,
1972.

[Din07] Irit Dinur. The PCP Theorem by gap ampliﬁcation. Journal of the ACM, 54(3):1–
44, 2007.

[dKPW04] Etienne de Klerk, Dmitrii Pasechnik, and Johannes Warners. On approximate
graph colouring and MAX-k-CUT algorithms based on the ϑ-function. Journal of
Combinatorial Optimization, 8(3):267–294, 2004.

[DMN12] Anindya De, Elchanan Mossel, and Joe Neeman. Majority is Stablest : discrete
and SoS. Technical Report 1211.1001, arXiv, 2012.

[DMN13] Anindya De, Elchanan Mossel, and Joe Neeman. Majority is Stablest : Discrete
and SoS. In Proceedings of the 45th Annual ACM Symposium on Theory of Com-
puting, 2013.

[DP93] Charles Delorme and Svatopluk Poljak. Laplacian eigenvalues and the maximum
cut problem. Mathematical Programming, 62(1–3):557–574, 1993.

[DR04] Irit Dinur and Omer Reingold. Assignment testers: Towards a combinatorial
proof of the PCP Theorem. In Proceedings of the 45th Annual IEEE Symposium
on Foundations of Computer Science, pages 155–164, 2004.

[DS09] Ilias Diakonikolas and Rocco Servedio. Improved approximation of linear thresh-
old functions. In Proceedings of the 24th Annual Computational Complexity Con-
ference, pages 161–172, 2009.

[DSC96] Persi Diaconis and Laurent Saloff-Coste. Logarithmic Sobolev inequalities for
ﬁnite Markov chains. Annals of Applied Probability, 6(3):695–750, 1996.

[Ehr83] Antoine Ehrhard. Symétrisation dans l’espace de gauss. Mathematica Scandinav-
ica, 53:281–301, 1983.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

398 Bibliography

[Ehr84] Antoine Ehrhard. Inégalités isopérimétriques et intégrales de Dirichlet gaussi-
ennes. Annales Scientiﬁques de l’École Normale Supérieure. Quatrième Série,
17(2):317–332, 1984.

[Ein05] Albert Einstein. Über die von der molekularkinetischen Theorie der Wärme
geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen. An-
nalen der physik, 322(8):549–560, 1905.

[EKR99] Funda Ergün, Ravi Kumar, and Ronitt Rubinfeld. Fast approximate PCPs. In
Proceedings of the 31st Annual ACM Symposium on Theory of Computing, pages
41–50, 1999.

[Eld13] Ronen Eldan. A two-sided estimate for the Gaussian noise stability deﬁcit. Tech-
nical Report 1307.2781, arXiv, 2013.

[Elg61] Calvin Elgot. Truth functions realizable by single threshold organs. In Proceed-
ings of the 2nd Annual Symposium on Switching Circuit Theory and Logical
Design (FOCS), pages 225–245, 1961.

[Enf70] Per Enﬂo. On the nonexistence of uniform homeomorphisms between l p-spaces.
Arkiv för matematik, 8(2):103–105, 1970.

[Epp89] Jay Epperson. The hypercontractive approach to exactly bounding an operator
with complex Gaussian kernel. Journal of Functional Analysis, 87(1):1–30, 1989.

[ER59] Paul Erd˝os and Alfréd Rényi. On random graphs I. Publicationes Mathematicae
Debrecen, 6:290–297, 1959.

[ES81] Bradley Efron and Charles Stein. The jackknife estimate of variance. Annals of
Statistics, 9(3):586–596, 1981.

[Ess42] Carl-Gustav Esseen. On the Liapounoff limit of error in the theory of probability.
Arkiv för matematik, astronomi och fysik, 28(9):1–19, 1942.

[Fed69] Paul Federbush. Partially alternate derivation of a result of Nelson. Journal of
Mathematical Physics, 10:50–52, 1969.

[FGL+96] Uriel Feige, Shaﬁ Goldwasser, László Lovász, Shmuel Safra, and Mario Szegedy.
Interactive proofs and the hardness of approximating cliques. Journal of the ACM,
43(2):268–292, 1996.

[Fin49] Nathan Fine. On the Walsh functions. Transactions of the American Mathemati-
cal Society, 65(3):372–414, 1949.

[FJS91] Merrick Furst, Jeffrey Jackson, and Sean Smith. Improved learning of AC0 func-
tions. In Proceedings of the 4th Annual Conference on Learning Theory, pages
317–325, 1991.

[FK96] Ehud Friedgut and Gil Kalai. Every monotone graph property has a sharp thresh-
old. Proceedings of the American Mathematical Society, 124(10):2993–3002, 1996.

[FKN02] Ehud Friedgut, Gil Kalai, and Assaf Naor. Boolean functions whose Fourier trans-
form is concentrated on the ﬁrst two levels and neutral social choice. Advances in
Applied Mathematics, 29(3):427–437, 2002.

[FL92] Uriel Feige and Lászlo Lovász. Two-prover one-round proof systems, their power
and their problems. In Proceedings of the 24th Annual ACM Symposium on Theory
of Computing, pages 733–744, 1992.

[FL06] Uriel Feige and Michael Langberg. The RPR2 rounding technique for semideﬁnite
programs. Journal of Algorithms, 60(1):1–23, 2006.

[FLM77] Tadeusz Figiel, Joram Lindenstrauss, and Vitali Milman. The dimension of al-
most spherical sections of convex bodies. Acta Mathematica, 139(1-2):53–94, 1977.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 399

[Fre79] R ¯usin, š Freivalds. Fast probabilistic algorithms. In Proceedings of the 4th Annual
International Symposium on Mathematical Foundations of Computer Science,
pages 57–69, 1979.

[Fri98] Ehud Friedgut. Boolean functions with low average sensitivity depend on few
coordinates. Combinatorica, 18(1):27–36, 1998.

[Fri99] Ehud Friedgut. Sharp thresholds of graph properties, and the k-SAT problem.
Journal of the American Mathematical Society, 12(4):1017–1054, 1999.

[Fri05] Ehud Friedgut. Hunting for sharp thresholds. Random Structures & Algorithms,
26(1-2):37–51, 2005.

[FS95] Katalin Friedl and Madhu Sudan. Some improvements to total degree tests. In
Proceedings of the 3rd Annual Israel Symposium on Theory of Computing Systems,
pages 190–198, 1995.

[FS02] Uriel Feige and Gideon Schechtman. On the optimality of the random hyperplane
rounding technique for Max-Cut. Randoom Structures and Algorithms, 20(3):403–
440, 2002.

[FS07] Dvir Falik and Alex Samorodnitsky. Edge-isoperimetric inequalities and inﬂu-
ences. Combinatorics, Probability and Computing, 16(5):693–712, 2007.

[FSS84] Merrick Furst, James Saxe, and Michael Sipser. Parity, circuits, and the
polynomial-time hierarchy. Mathematical Systems Theory, 17(1):13–27, 1984.

[GGR98] Oded Goldreich, Shaﬁ Goldwasser, and Dana Ron. Property testing and its connec-
tions to learning and approximation. Journal of the ACM, 45(4):653–750, 1998.

[Gir73] Vyacheslav Girko. Limit theorems for random quadratic forms. Izdat. Naukova
Dumka, pages 14–30, 1973.

[GK68] Mark Garman and Morton Kamien. The paradox of voting: probability calcula-
tions. Behavioral Science, 13(4):306–316, 1968.

[GKK08] Parikshit Gopalan, Adam Kalai, and Adam Klivans. Agnostically learning de-
cision trees. In Proceedings of the 40th Annual ACM Symposium on Theory of
Computing, pages 527–536, 2008.

[GL89] Oded Goldreich and Leonid Levin. A hard-core predicate for all one-way functions.
In Proceedings of the 21st Annual ACM Symposium on Theory of Computing,
pages 25–32, 1989.

[GL94] Craig Gotsman and Nathan Linial. Spectral properties of threshold functions.
Combinatorica, 14(1):35–50, 1994.

[Gli68] James Glimm. Boson ﬁelds with nonlinear selﬁnteraction in two dimensions.
Communications in Mathematical Physics, 8(1):12–25, 1968.

[GMR12] Parikshit Gopalan, Raghu Meka, and Omer Reingold. DNF sparsiﬁcation and
a faster deterministic counting algorithm. In Proceedings of the 27th Annual
Computational Complexity Conference, pages 126–135, 2012.

[Gol59] Solomon Golomb. On the classiﬁcation of Boolean functions. IRE Transactions on
Circuit Theory, 6(5):176–186, 1959.

[GOS+11] Parikshit Gopalan, Ryan O’Donnell, Rocco Servedio, Amir Shpilka, and Karl Wim-
mer. Testing Fourier dimensionality and sparsity. SIAM Journal on Computing,
40(4):1075–1100, 2011.

[Gow01] W. Timothy Gowers. A new proof of Szemerédi’s theorem. Geometric and Func-
tional Analysis, 11(3):465–588, 2001.

[GOWZ10] Parikshit Gopalan, Ryan O’Donnell, Yi Wu, and David Zuckerman. Fooling func-
tions of halfspaces under product distributions. In Proceedings of the 25th Annual
Computational Complexity Conference, pages 223–234, 2010.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

400 Bibliography

[GR00] Mikael Goldmann and Alexander Russell. Spectral bounds on general hard core
predicates. In Proceedings of the 17th Annual Symposium on Theoretical Aspects
of Computer Science, pages 614–625, 2000.

[Gro72] Leonard Gross. Existence and uniqueness of physical ground states. Journal of
Functional Analysis, 10:52–109, 1972.

[Gro75] Leonard Gross. Logarithmic Sobolev inequalities. American Journal of Mathe-
matics, 97(4):1061–1083, 1975.

[GS08] Ben Green and Tom Sanders. Boolean functions with small spectral norm. Geo-
metric and Functional Analysis, 18(1):144–162, 2008.

[Gui52] George-Théodule Guilbaud. Les théories de l’intérêt général et le problème
logique de l’agrégation. Economie appliquée, V(4):501–551, 1952.

[GW94] Michel Goemans and David Williamson. A 0.878 approximation algorithm for
MAX-2SAT and MAX-CUT. In Proceedings of the 26th Annual ACM Symposium
on Theory of Computing, pages 422–431, 1994.

[GW95] Michel Goemans and David Williamson. Improved approximation algorithms
for maximum cut and satisﬁability problems using semideﬁnite programming.
Journal of the ACM, 42:1115–1145, 1995.

[Haa10] Alfréd Haar. Zur Theorie der orthogonalen Funktionensysteme. Mathematische
Annalen, 69(3):331–371, 1910.

[Haa82] Uffe Haagerup. The best constants in the Khinchine inequality. Studia Mathe-
matica, 70(3):231–283, 1982.

[Háj68] Jaroslav Hájek. Asymptotic normality of simple linear rank statistics under al-
ternatives. Annals of Mathematical Statistics, 39(2):325–346, 1968.

[Har64] Lawrence Harper. Optimal assignments of numbers to vertices. Journal of the
Society for Industrial and Applied Mathematics, 12(1):131–135, 1964.

[Hås87] Johan Håstad. Computational Limitations for Small Depth Circuits. MIT Press,
1987.

[Hås96] Johan Håstad. Testing of the long code and hardness for clique. In Proceedings of
the 28th Annual ACM Symposium on Theory of Computing, pages 11–19, 1996.

[Hås97] Johan Håstad. Some optimal inapproximability results. In Proceedings of the 29th
Annual ACM Symposium on Theory of Computing, pages 1–10, 1997.

[Hås99] Johan Håstad. Clique is hard to approximate within n1−ϵ. Acta Mathematica,
182(1):105–142, 1999.

[Hås01a] Johan Håstad. A slight sharpening of LMN. Journal of Computer and System
Sciences, 63(3):498–508, 2001.

[Hås01b] Johan Håstad. Some optimal inapproximability results. Journal of the ACM,
48(4):798–859, 2001.

[Hås12] Johan Håstad. On the correlation of parity and small-depth circuits. Technical
Report TR12-137, Electronic Colloquium on Computational Complexity, 2012.

[Hat12] Hamed Hatami. A structure theorem for Boolean functions with small total inﬂu-
ences. Annals of Mathematics, 176(1):509–533, 2012.

[Her64] Charles Hermite. Sur un nouveau développement en série des fonctions. Comptes
rendus de l’Académie des sciences, 58(2):93–100, 266–273, 1864.

[Hin10] Masanori Hino. Sets of ﬁnite perimeter and the Hausdorff-Gauss measure on the
Wiener space. Journal of Functional Analysis, 258(5):1656–1681, 2010.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 401

[HKM10] Prahladh Harsha, Adam Klivans, and Raghu Meka. Bounding the sensitivity of
polynomial threshold functions. In Proceedings of the 42nd Annual ACM Sympo-
sium on Theory of Computing, pages 533–542, 2010.

[HMM82] Stanley Hurst, D. Michael Miller, and Jon Muzio. Spectral method of Boolean
function complexity. Electronics Letters, 18(13):572–574, 1982.

[Hoe48] Wassily Hoeffding. A class of statistics with asymptotically normal distribution.
Annals of Mathematical Statistics, 19(3):293–325, 1948.

[HY95] Yasunari Higuchi and Nobuo Yoshida. Analytic conditions and phase transition
for Ising models. Unpublished lecture notes (in Japanese), 1995.

[IMP12] Russell Impagliazzo, William Matthews, and Ramamohan Paturi. A satisﬁability
algorithm for AC0. In Proceedings of the 23rd Annual ACM-SIAM Symposium on
Discrete Algorithms, pages 961–972, 2012.

[Jac95] Jeffrey Jackson. The Harmonic Sieve: a novel application of Fourier analysis to
machine learning theory and practice. PhD thesis, Carnegie Mellon University,
1995.

[Jac97] Jeffrey Jackson. An efﬁcient membership-query algorithm for learning DNF with
respect to the uniform distribution. Journal of Computer and System Sciences,
55(3):414–440, 1997.

[Jan97] Svante Janson. Gaussian Hilbert Spaces. Cambridge University Press, 1997.

[JKS03] T. S. Jayram, Ravi Kumar, and D. Sivakumar. Two applications of information
complexity. In Proceedings of the 35th Annual ACM Symposium on Theory of
Computing, pages 673–682, 2003.

[Joh74] David Johnson. Approximation algorithms for combinatorial problems. Journal
of Computer and System Sciences, 9(3):256–278, 1974.

[JOW12] Jacek Jendrej, Krzysztof Oleszkiewicz, and Jakub Wojtaszczyk. On some exten-
sions of the FKN theorem. Manuscript, 2012.

[JZ11] Rahul Jain and Shengyu Zhang. The inﬂuence lower bound via query elimination.
Theory of Computing, 7(1):147–153, 2011.

[Kah68] Jean-Pierre Kahane. Some random series of functions. D. C. Heath & Co., 1968.

[Kal02] Gil Kalai. A Fourier-theoretic perspective on the Condorcet paradox and Arrow’s
theorem. Advances in Applied Mathematics, 29(3):412–426, 2002.

[Kan11] Daniel Kane. On Elliptic Curves, the ABC Conjecture, and Polynomial Threshold
Functions. PhD thesis, Harvard University, 2011.

[Kan12] Daniel Kane. The correct exponent for the Gotsman–Linial conjecture. Technical
Report 1210.1283, arXiv, 2012.

[Kar76] Mark Karpovsky. Finite orthogonal series in the design of digital devices: analysis,
synthesis, and optimization. Wiley, 1976.

[Kar99] Howard Karloff. How good is the Goemans–Williamson MAX CUT algorithm?
SIAM Journal of Computing, 29(1):336–350, 1999.

[Kha93] Michael Kharitonov. Cryptographic hardness of distribution-speciﬁc learning. In
Proceedings of the 25th Annual ACM Symposium on Theory of Computing, pages
372–381, 1993.

[Kho02] Subhash Khot. On the power of unique 2-prover 1-round games. In Proceedings of
the 34th Annual ACM Symposium on Theory of Computing, pages 767–775, 2002.

[Kho05] Subhash Khot. Inapproximability results via Long Code based PCPs. ACM
SIGACT News, 36(2):25–42, 2005.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

402 Bibliography

[Kho10a] Subhash Khot. Inapproximability of NP-complete problems, discrete Fourier anal-
ysis, and geometry. In Proceedings of the International Congress of Mathemati-
cians, volume 901, pages 2676–2697, 2010.

[Kho10b] Subhash Khot. On the Unique Games Conjecture. In Proceedings of the 25th
Annual Computational Complexity Conference, pages 99–121, 2010.

[Kie69] Konrad Kiener. Über Produkte von quadratisch integrierbaren Funktionen
endlicher Vielfalt. PhD thesis, Universität Innsbruck, 1969.

[Kin02] Guy Kindler. Property Testing, PCP, and juntas. PhD thesis, Tel Aviv University,
2002.

[KK07] Jeff Kahn and Gil Kalai. Thresholds and expectation thresholds. Combinatorics,
Probability and Computing, 16(3):495–502, 2007.

[KKL88] Jeff Kahn, Gil Kalai, and Nathan Linial. The inﬂuence of variables on Boolean
functions. In Proceedings of the 29th Annual IEEE Symposium on Foundations of
Computer Science, pages 68–80, 1988.

[KKMO04] Subhash Khot, Guy Kindler, Elchanan Mossel, and Ryan O’Donnell. Optimal in-
approximability results for MAX-CUT and other 2-variable CSPs? In Proceedings
of the 45th Annual IEEE Symposium on Foundations of Computer Science, pages
146–154, 2004.

[KKMO07] Subhash Khot, Guy Kindler, Elchanan Mossel, and Ryan O’Donnell. Optimal
inapproximability results for Max-Cut and other 2-variable CSPs? SIAM Journal
on Computing, 37(1):319–357, 2007.

[Kle66] Daniel Kleitman. Families of non-disjoint subsets. Journal of Combinatorial The-
ory, 1(1):153–155, 1966.

[KLX10] Tali Kaufman, Simon Litsyn, and Ning Xie. Breaking the ϵ-soundness bound
of the linearity test over GF(2). SIAM Journal on Computing, 39(5):1988–2003,
2010.

[KM93] Eyal Kushilevitz and Yishay Mansour. Learning decision trees using the Fourier
spectrum. SIAM Journal on Computing, 22(6):1331–1348, 1993.

[KO06] Subhash Khot and Ryan O’Donnell. SDP gaps and UGC-hardness for Max-Cut-
Gain. In Proceedings of the 47th Annual IEEE Symposium on Foundations of
Computer Science, pages 217–226, 2006.

[KO12] Guy Kindler and Ryan O’Donnell. Gaussian noise sensitivity and Fourier tails.
In Proceedings of the 27th Annual Computational Complexity Conference, pages
137–147, 2012.

[KOS04] Adam Klivans, Ryan O’Donnell, and Rocco Servedio. Learning intersections and
thresholds of halfspaces. Journal of Computer and System Sciences, 68(4):808–
840, 2004.

[KOS08] Adam Klivans, Ryan O’Donnell, and Rocco Servedio. Learning geometric concepts
via Gaussian surface area. In Proceedings of the 49th Annual IEEE Symposium
on Foundations of Computer Science, pages 541–550, 2008.

[KOTZ16] Manuel Kauers, Ryan O’Donnell, Li-Yang Tan, and Yuan Zhou. Hypercontractive
inequalities via SOS, and the Frankl-Rödl graph. Discrete Analysis, 4, 2016.

[KP97] Matthias Krause and Pavel Pudlák. On the computational power of depth-2 cir-
cuits with threshold and modulo gates. Theoretical Computer Science, 174(1–
2):137–156, 1997.

[KR82] Samuel Karlin and Yosef Rinott. Applications of ANOVA type decompositions
for comparisons of conditional variance statistics including jackknife estimates.
Annals of Statistics, 10(2):485–501, 1982.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 403

[KR08] Subhash Khot and Oded Regev. Vertex Cover might be hard to approximate to
within 2 − ϵ. Journal of Computer and System Sciences, 74(3):335–349, 2008.

[Kra29] Mikahil (Krawtchouk) Kravchuk. Sur une généralisation des polynomes
d’Hermite. Comptes rendus de l’Académie des sciences, 189:620–622, 1929.

[KS88] Wiesław Krakowiak and Jerzy Szulga. Hypercontraction principle and random
multilinear forms. Probability Theory and Related Fields, 77(3):325–342, 1988.

[KS02] Guy Kindler and Shmuel Safra. Noise-resistant Boolean functions are juntas.
Manuscript, 2002.

[KSTW01] Sanjeev Khanna, Madhu Sudan, Luca Trevisan, and David Williamson. The
approximability of constraint satisfaction problems. SIAM Journal on Computing,
30(6):1863–1920, 2001.

[KV05] Subhash Khot and Nisheeth Vishnoi. The Unique Games Conjecture, integral-
ity gap for cut problems and embeddability of negative type metrics into ℓ1. In
Proceedings of the 46th Annual IEEE Symposium on Foundations of Computer
Science, pages 53–62, 2005.

[KW92] Stanisław Kwapie ´n and Wojbor Woyczy ´nski. Random series and stochastic inte-
grals: Single and multiple. Probability and Its Applications. Birkhäuser, 1992.

[Kwa10] Stanisław Kwapie ´n. On Hoeffding decomposition in l p. Illinois Journal of Mathe-
matics, 54(3):1205–1211, 2010.

[KZ97] Howard Karloff and Uri Zwick. A 7/8-approximation algorithm for MAX 3SAT?
In Proceedings of the 38th Annual IEEE Symposium on Foundations of Computer
Science, pages 406–415, 1997.

[Lap11] Pierre-Simon Laplace. Mémoire sur les intégrales déﬁnies et leur application aux
probabilités, et spécialement à la recherche du milieu qu’il faut choisir entre les
résultats des observations. Mémoires de la Classe des Sciences Mathématiques et
Physiques de l’Institut Impérial de France, Année 1810, 58:279–347, 1811.

[Leb72] Nikola˘ı Lebedev. Special functions & their applications. Dover Publications, 1972.

[Lec63] Robert Lechner. Afﬁne equivalence of switching functions. PhD thesis, Harvard
University, 1963.

[Lec71] Robert Lechner. Harmonic analysis of switching functions. In Amar Mukhophad-
hay, editor, Recent developments in switching theory, pages 121–228. Academic
Press, 1971.

[Led92] Michel Ledoux. On an integral criterion for hypercontractivity of diffusion semi-
groups and extremal functions. Journal of Functional Analysis, 105(2):444–465,
1992.

[Led94] Michel Ledoux. Semigroup proofs of the isoperimetric inequality in Euclidean
and Gauss space. Bulletin des Sciences Mathématiques, 118(6):485–510, 1994.

[Led96] Michel Ledoux. Isoperimetry and Gaussian analysis. In Pierre Bernard, editor,
Lectures on Probability Theory and Statistics, volume XXIV of Lecture Notes in
Mathematics 1648, pages 165–294. Springer, 1996.

[Led98] Michel Ledoux. A short proof of the Gaussian isoperimetric inequality. In High
dimensional probability (Oberwolfach, 1996), volume 43 of Progress in Probability,
pages 229–232. Birkhäuser, Basel, 1998.

[Led13] Michel Ledoux. Remarks on noise sensitivity, Brascamp–Lieb and Slepian in-
equalities. http://perso.math.univ-toulouse.fr/ledoux/files/2013/11/
noise.pdf , 2013.

[Lee10] Homin Lee. Decision trees and inﬂuence: an inductive proof of the OSSS Inequal-
ity. Theory of Computing, 6(1):81–84, 2010.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

404 Bibliography

[Leo12] Nikos Leonardos. An improved lower bound for the randomized decision tree com-
plexity of recursive majority. Technical Report TR12-099, Electronic Colloquium
on Computational Complexity, 2012.

[Lév22] Paul Lévy. Leçons d’Analyse Fonctionnelle. Gauthier-Villars, 1922.

[LG14] François Le Gall. Powers of tensors and fast matrix multiplication. Technical
Report 1401.7714, arXiv, 2014.

[Lin22] Jarl Lindeberg. Eine neue Herleitung des Exponentialgesetzes in der Wahrschein-
lichkeitsrechnung. Mathematische Zeitschrift, 15(1):211–225, 1922.

[LLS06] Sophie Laplante, Troy Lee, and Mario Szegedy. The quantum adversary method
and classical formula size lower bounds. Computational Complexity, 15(2):163–
196, 2006.

[LMN89] Nathan Linial, Yishay Mansour, and Noam Nisan. Constant depth circuits,
Fourier transform and Learnability. In Proceedings of the 30th Annual IEEE
Symposium on Foundations of Computer Science, pages 574–579, 1989.

[LMN93] Nathan Linial, Yishay Mansour, and Noam Nisan. Constant depth circuits,
Fourier transform and learnability. Journal of the ACM, 40(3):607–620, 1993.

[LO94] Rafał Latała and Krzysztof Oleszkiewicz. On the best constant in the Khintchine–
Kahane inequality. Studia Mathematica, 109(1):101–104, 1994.

[LO00] Rafal Latała and Krzysztof Oleszkiewicz. Between Sobolev and Poincaré. In Vitali
Milman and Gideon Schechtman, editors, Geometric aspects of functional analysis,
pages 147–168. Springer, 2000.

[Lov08] Shachar Lovett. Unconditional pseudorandom generators for low degree polyno-
mials. In Proceedings of the 40th Annual ACM Symposium on Theory of Comput-
ing, pages 557–562, 2008.

[LSP82] Leslie Lamport, Robert Shostak, and Marshall Pease. The Byzantine generals
problem. ACM Transactions on Programming Languages and Systems, 4(3):382–
401, 1982.

[LT09] Shachar Lovett and Yoav Tzur. Explicit lower bound for fooling polynomials by
the sum of small-bias generators. In Electronic Colloquium on Computational
Complexity TR09-088, 2009.

[LVW93] Michael Luby, Boban Veliˇckovi´c, and Avi Wigderson. Deterministic approximate
counting of depth-2 circuits. In Proceedings of the 2nd Annual Israel Symposium
on Theory of Computing Systems, pages 18–24, 1993.

[Man94] Yishay Mansour. Learning Boolean functions via the Fourier Transform. In Vwani
Roychowdhury, Kai-Yeung Siu, and Alon Orlitsky, editors, Theoretical Advances in
Neural Computation and Learning, chapter 11, pages 391–424. Kluwer Academic
Publishers, 1994.

[Man95] Yishay Mansour. An O(nlog log n) learning algorithm for DNF under the uniform
distribution. Journal of Computer and System Sciences, 50(3):543–550, 1995.

[Mar74] Grigory Margulis. Probabilistic characteristics of graphs with large connectivity.
Problemy Peredaˇci Informacii, 10(2):101–108, 1974.

[May52] Kenneth May. A set of independent necessary and sufﬁcient conditions for simple
majority decisions. Econometrica, 20(4):680–684, 1952.

[McK73] Henry McKean. Geometry of differential space. Annals of Probability, 1(2):197–
206, 1973.

[Meh66] F. Gustav Mehler. Ueber die Entwicklung einer Function von beliebig vielen
Variablen nach Laplaceschen Functionen höherer ordnung. Journal für die reine
und angewandte Mathematik, 66:161–176, 1866.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 405

[Mid04] Gatis Midrij ¯anis. Exact quantum query complexity for total Boolean functions.
arXiv:quant-ph/0403168, 2004.

[Mir13] Michele Miranda Jr. Personal communication to the author, October 2013.

[MN12] Elchanan Mossel and Joe Neeman. Robust optimality of Gaussian noise stability.
Technical Report 1210.4126, arXiv, 2012.

[MNP12] Michele Miranda Jr., Matteo Novaga, and Diego Pallara. An introduction to BV
functions in Wiener spaces. Technical Report 1212.5926, arXiv, 2012.

[MNSX11] Frédéric Magniez, Ashwin Nayak, Miklos Santha, and David Xiao. Improved
bounds for the randomized decision tree complexity of recursive majority. In Pro-
ceedings of the 38th Annual International Colloquium on Automata, Languages
and Programming, pages 317–329, 2011.

[MO05] Elchanan Mossel and Ryan O’Donnell. Coin ﬂipping from a cosmic source: On
error correction of truly random bits. Random Structures & Algorithms, 26(4):418–
436, 2005.

[MOO05a] Elchanan Mossel, Ryan O’Donnell, and Krzysztof Oleszkiewicz. Noise stability
of functions with low inﬂuences: invariance and optimality. In Proceedings of the
46th Annual IEEE Symposium on Foundations of Computer Science, pages 21–30,
2005.

[MOO05b] Elchanan Mossel, Ryan O’Donnell, and Krzysztof Oleszkiewicz. Noise stability
of functions with low inﬂuences: invariance and optimality. Technical Report
math/0503503, arXiv, 2005.

[MOO10] Elchanan Mossel, Ryan O’Donnell, and Krzysztof Oleszkiewicz. Noise stability of
functions with low inﬂuences: invariance and optimality. Annals of Mathematics,
171(1):295–341, 2010.

[MOR+06] Elchanan Mossel, Ryan O’Donnell, Oded Regev, Jeffrey Steif, and Benjamin Su-
dakov. Non-interactive correlation distillation, inhomogeneous Markov chains,
and the reverse Bonami–Beckner inequality. Israel Journal of Mathematics,
154:299–336, 2006.

[MORS10] Kevin Matulef, Ryan O’Donnell, Ronitt Rubinfeld, and Rocco Servedio. Testing
halfspaces. SIAM Journal on Computing, 39(5):2004–2047, 2010.

[MOS04] Elchanan Mossel, Ryan O’Donnell, and Rocco Servedio. Learning functions of
k relevant variables. Journal of Computer and System Sciences, 69(3):421–434,
2004.

[Mos10] Elchanan Mossel. Gaussian bounds for noise correlation of functions. Geometric
and Functional Analysis, 19(6):1713–1756, 2010.

[MOS12] Elchanan Mossel, Krzysztof Oleszkiewicz, and Arnab Sen. On reverse hypercon-
tractivity. Technical Report 1108.1210, arXiv, 2012.

[MP11] Gretchen Matthews and Justin Peachey. Small-bias sets from extended norm-
trace codes. Manuscript, 2011.

[MPPP07] Michele Miranda Jr., Diego Pallara, Fabio Paronetto, and Marc Preunkert. Short-
time heat ﬂow and functions of bounded variation in RN . Annales de la Faculté
des Sciences de Toulouse. Mathématiques. Série 6, 16(1):125–145, 2007.

[MRRW77] Robert McEliece, Eugene Rodemich, Howard Rumsey, and Lloyd Welch. New
upper bounds on the rate of a code via the Delsarte–MacWilliams inequalities.
IEEE Transactions on Information Theory, 23(2):157–166, 1977.

[MS73] Tamás Matolcsi and József Szücs. Intersection des mesures spectrales conjuguées.
Comptes rendus de l’Académie des sciences, 277:841–843, 1973.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

406 Bibliography

[MS77] F. Jessie MacWilliams and Neil Sloane. The theory of error-correcting codes. North-
Holland, 1977.

[Mul54a] David Muller. Application of Boolean algebra to switching circuit design and to
error detection. IRE Transactions on Electronic Computers, 3(6):6–12, 1954.

[Mul54b] David Muller. Boolean algebras in electric circuit design. The American Mathe-
matical Monthly, 61(7):27–28, 1954.

[Mül05] Paul Müller. Isomorphisms between H1 spaces, volume 66 of Monograﬁe Matem-
atyczne. Birkhäuser Verlag, 2005.

[Nak35] Akira Nakashima. The theory of relay circuit composition. The Journal of the
Institute of Telegraph and Telephone Engineers of Japan, 150:731–752, September
1935.

[Naz03] Fedor Nazarov. On the maximal perimeter of a convex set in Rn with respect to
a Gaussian measure. In Geometric Aspects of Functional Analysis, volume 1807,
pages 169–187. Israel Seminar, 2003.

[Nel66] Edward Nelson. A quartic interaction in two dimensions. In Mathematical Theory
of Elementary Particles, pages 69–73. MIT Press, 1966.

[Nel73] Edward Nelson. The free Markoff ﬁeld. Journal of Functional Analysis, 12:211–
227, 1973.

[Nev76] Jacques Neveu. Sur l’espérance conditionnelle par rapport à un mouvement
brownien. Annales de l’Institut Henri Poincaré (B), 12(2):105–109, 1976.

[Nin58] Ichizo Ninomiya. A theory of the coordinate representations of switching func-
tions. Memoirs of the Faculty of Engineering, Nagoya University, 10:175–190,
1958.

[NN93] Joseph Naor and Moni Naor. Small-bias probability spaces: efﬁcient constructions
and applications. SIAM Journal on Computing, 22(4):838–856, 1993.

[NP00] Fedor Nazarov and Anatoliy Podkorytov. Ball, Haagerup, and distribution func-
tions. Complex Analysis, Operators, and Related Topics. Operator Theory: Ad-
vances and Applications, 113:247–267, 2000.

[NS94] Noam Nisan and Mario Szegedy. On the degree of Boolean functions as real
polynomials. Computational Complexity, 4(4):301–313, 1994.

[NSV02] Fedor Nazarov, Mikhail Sodin, and Alexander Vol’berg. The geometric Kannan–
Lovász–Simonovits lemma, dimension-free estimates for volumes of sublevel sets
of polynomials, and distribution of zeros of random analytic functions. Algebra i
Analiz, 14(2):214–234, 2002.

[NW95] Noam Nisan and Avi Wigderson. On rank vs. communication complexity. Combi-
natorica, 15(4):557–565, 1995.

[O’D03] Ryan O’Donnell. Computational applications of noise sensitivity. PhD thesis, Mas-
sachusetts Institute of Technology, 2003.

[O’D04] Ryan O’Donnell. Hardness ampliﬁcation within NP. Journal of Computer and
System Sciences, 69(1):68–94, 2004.

[Ole03] Krzysztof Oleszkiewicz. On a nonsymmetric version of the Khinchine–Kahane
inequality. In Evarist Giné, Christian Houdré, and David Nualart, editors, Sto-
chastic inequalities and applications, volume 56, pages 157–168. Birkhäuser,
2003.

[OS06] Ryan O’Donnell and Rocco Servedio. Learning monotone decision trees in polyno-
mial time. In Proceedings of the 21st Annual Computational Complexity Confer-
ence, pages 213–225, 2006.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 407

[OS07] Ryan O’Donnell and Rocco Servedio. Learning monotone decision trees in polyno-
mial time. SIAM Journal on Computing, 37(3):827–844, 2007.

[OS08] Ryan O’Donnell and Rocco Servedio. Extremal properties of polynomial threshold
functions. Journal of Computer and System Sciences, 74(3):298–312, 2008.

[OSSS05] Ryan O’Donnell, Michael Saks, Oded Schramm, and Rocco Servedio. Every de-
cision tree has an inﬂuential variable. In Proceedings of the 46th Annual IEEE
Symposium on Foundations of Computer Science, pages 31–39, 2005.

[OW08] Ryan O’Donnell and Yi Wu. An optimal SDP algorithm for Max-Cut, and equally
optimal Long Code tests. In Proceedings of the 40th Annual ACM Symposium on
Theory of Computing, pages 335–344, 2008.

[OW09] Ryan O’Donnell and Yi Wu. 3-Bit dictator testing: 1 vs. 5/8. In Proceedings of
the 20th Annual ACM-SIAM Symposium on Discrete Algorithms, pages 365–373,
2009.

[OW12] Ryan O’Donnell and John Wright. A new point of NP-hardness for Unique-Games.
In Proceedings of the 44th Annual ACM Symposium on Theory of Computing,
pages 289–306, 2012.

[OW13] Ryan O’Donnell and Karl Wimmer. Sharpness of KKL on Schreier graphs. Elec-
tronic Communications in Probability, 18:1–12, 2013.

[Pal32] Raymond Paley. A remarkable series of orthogonal functions (I). Proceedings of
the London Mathematical Society, 2(1):241–264, 1932.

[Pen46] Lionel Penrose. The elementary statistics of majority voting. Journal of the Royal
Statistical Society, 109(1):53–57, 1946.

[Per90] René Peralta. On the randomness complexity of algorithms. Technical Report
90-1, University of Wisconsin, Milwaukee, 1990.

[Per04] Yuval Peres. Noise stability of weighted majority. arXiv:math/0412377, 2004.

[Pis86] Gilles Pisier. Probabilistic methods in the geometry of Banach spaces. In Probabil-
ity and analysis (Varenna, 1985), volume 1206 of Lecture Notes in Mathematics,
pages 167–241. Springer, Berlin, 1986.

[PRS01] Michal Parnas, Dana Ron, and Alex Samorodnitsky. Proclaiming dictators and
juntas or testing Boolean formulae. In Proceedings of the 5th Annual International
Workshop on Randomized Techniques in Computation, pages 273–284, 2001.

[PRS02] Michal Parnas, Dana Ron, and Alex Samorodnitsky. Testing basic Boolean formu-
lae. SIAM Journal on Discrete Mathematics, 16(1):20–46, 2002.

[PZ78] Gilles Pisier and Joel Zinn. On the limit theorems for random variables with
values in the spaces l p (2 ≤ p < ∞). Zeitschrift für Wahrscheinlichkeitstheorie und
Verwandte Gebiete, 41(4):289–304, 1978.

[Rag08] Prasad Raghavendra. Optimal algorithms and inapproximability results for every
CSP? In Proceedings of the 40th Annual ACM Symposium on Theory of Computing,
pages 245–254, 2008.

[Rag09] Prasad Raghavendra. Approximating NP-hard problems: efﬁcient algorithms and
their limits. PhD thesis, University of Washington, 2009.

[Rao47] Calyampudi Rao. Factorial experiments derivable from combinatorial arrange-
ments of arrays. Journal of the Royal Statistical Society, 9(1):128–139, 1947.

[Raz93] Alexander Razborov. Bounded arithmetic and lower bounds in boolean complexity.
In Peter Clote and Jeffrey Remmel, editors, Feasible Mathematics II, pages 344–
386. Birkhäuser, 1993.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

408 Bibliography

[Rik61] William Riker. Voting and the summation of preferences: An interpretive biblio-
graphic review of selected developments during the last decade. American Politi-
cal Science Review, 55(4):900–911, 1961.

[Ros76] Haskell Rosenthal. Convolution by a biased coin. In The Altgeld Book 1975/1976,
pages II.1–II.17. University of Illinois, 1976.

[Ros06] Raphaël Rossignol. Threshold for monotone symmetric properties through a loga-
rithmic Sobolev inequality. Annals of Probability, 34(5):1707–1725, 2006.

[Rot53] Klaus Roth. On certain sets of integers. Journal of the London Mathematical
Society, 28(1):104–109, 1953.

[Rot73] Vladimir Rotar’. Some limit theorems for polynomials of second order. Teoriya
Veroyatnostei i ee Primeneniya, 18(3):527–534, 1973.

[Rot74] Vladimir Rotar’. Some limit theorems for polynomials of second degree. Theory of
Probability and its Applications, 18(3):499–507, 1974.

[Rot75] Vladimir Rotar’. Limit theorems for multilinear forms and quasipolynomial func-
tions. Teoriya Veroyatnostei i ee Primeneniya, 20(3):527–546, 1975.

[Rot76] Oscar Rothaus. On “bent” functions. Journal of Combinatorial Theory, Series A,
20(3):300–305, 1976.

[Rot79] Vladimir Rotar’. Limit theorems for polylinear forms. Journal of Multivariate
Analysis, 9(4):511–530, 1979.

[Rot88] Alvin Roth, editor. The Shapley value: essays in honor of Lloyd S. Shapley. Cam-
bridge University Press, 1988.

[Rou62] Jean-Jacques Rousseau. Du Contrat Social. Marc-Michel Rey, 1762.

[RR01] Yosef Rinott and Vladimir Rotar’. A remark on quadrant normal probabilities in
high dimensions. Statistics & Probability Letters, 51(1):47–51, 2001.

[RS96] Ronitt Rubinfeld and Madhu Sudan. Robust characterizations of polynomials
with applications to program testing. SIAM Journal on Computing, 25(2):252–
271, 1996.

[Rud62] Walter Rudin. Fourier analysis on groups. John Wiley & Sons, 1962.

[Rus81] Lucio Russo. On the critical percolation probabilities. Zeitschrift für Wahrschein-
lichkeitstheorie und verwandte Gebiete, 56(2):229–237, 1981.

[Rus82] Lucio Russo. An approximate zero-one law. Zeitschrift für Wahrscheinlichkeitsthe-
orie und verwandte Gebiete, 61(1):129–139, 1982.

[RV80] Herman Rubin and Richard Vitale. Asymptotic distribution of symmetric statis-
tics. Annals of Statistics, 8(1):165–170, 1980.

[Sae68] Sadahiro Saeki. On norms of idempotent measures. Proceedings of the American
Mathematical Society, 19(3):600–602, 1968.

[SB91] Kai-Yeung Siu and Jehoshua Bruck. On the power of threshold circuits with small
weights. SIAM Journal on Discrete Mathematics, 4(3):423–435, 1991.

[Sch48] Erhard Schmidt. Die Brunn-Minkowskische Ungleichung und ihr Spiegelbild
sowie die isoperimetrische Eigenschaft der Kugel in der euklidischen und nich-
teuklidischen Geometrie. I. Mathematische Nachrichten, 1:81–157, 1948.

[Sch67] Michel Schreiber. Fermeture en probabilité des chaos de Wiener. Comptes Rendus
Hebdomadaires des Séances de l’Académie des Sciences, Séries A, 265:859–861,
1967.

[Sch69] Michel Schreiber. Fermeture en probabilité de certains sous-espaces d’un espace
L2. Application aux chaos de Wiener. Zeitschrift für Wahrscheinlichkeitstheorie
und Verwandte Gebiete, 14:36–48, 1969.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 409

[Seg70] Irving Segal. Construction of non-linear local quantum processes: I. Annals of
Mathematics, 92:462–481, 1970.

[Sha37] Claude Shannon. A symbolic analysis of relay and switching circuits. Master’s
thesis, Massachusetts Institute of Technology, 1937.

[Sha53] Lloyd Shapley. A value for n-person games. In Harold Kuhn and Albert Tucker, ed-
itors, Contributions in the Theory of Games, volume II, pages 307–317. Princeton
University Press, 1953.

[She99] William Sheppard. On the application of the theory of error to cases of normal dis-
tribution and normal correlation. Philosophical Transactions of the Royal Society
of London, Series A, 192:101–167, 531, 1899.

[She38] Victor Shestakov. Some Mathematical Methods for the Construction and Simpli-
ﬁcation of Two-Terminal Electrical Networks of Class A. PhD thesis, Lomonosov
State University, 1938.

[She08] Jonah Sherman. The randomized decision tree complexity of the recursive major-
ity of three function on 3n inputs is at least 2.5n. Unpublished, 2008.

[She13] Irina Shevtsova. On the absolute constants in the Berry–Esseen inequality and
its structural and nonuniform improvements. Informatika i Ee Primeneniya,
7(1):124–125, 2013.

[SHK72] Barry Simon and Raphael Høegh-Krohn. Hypercontractive semigroups and two
dimensional self-coupled Bose ﬁelds. Journal of Functional Analysis, 9:121–180,
1972.

[Sie84] Thomas Siegenthaler. Correlation-immunity of nonlinear combining functions for
cryptographic applications. IEEE Transactions on Information Theory, 30(5):776–
780, 1984.

[SS10] Oded Schramm and Jeffrey Steif. Quantitative noise sensitivity and exceptional
times for percolation. Annals of Mathematics, 171(2):619–672, 2010.

[ST78] Vladimir Sudakov and Boris Tsirel’son. Extremal properties of half-spaces
for spherically invariant measures. Journal of Soviet Mathematics, 9(1):9–18,
1978. Originally published in Zap. Nauchn. Sem. Leningrad. Otdel. Math. Inst.
Steklova., 41:14–21, 1974.

[Ste72] Charles Stein. A bound for the error in the normal approximation to the distribu-
tion of a sum of dependent random variables. In Proceedings of the 6th Berkeley
Symposium on Mathematical Statistics and Probability, pages 583–602. Univer-
sity of California Press, 1972.

[Ste86a] J. Michael Steele. An Efron–Stein inequality for nonsymmetric statistics. Annals
of Statistics, 14(2):753–758, 1986.

[Ste86b] Charles Stein. Approximate computation of expectations. Institute of Mathemati-
cal Statistics Lecture Notes. Institute of Mathematical Statistics, Hayward, CA,
1986.

[Sub61] Bella Subbotovskaya. Realizations of linear functions by formulas using ∨, &, .
Doklady Akademii Nauk SSSR, 136(3):553–555, 1961.

[SW86] Michael Saks and Avi Wigderson. Probabilistic Boolean decision trees and the
complexity of evaluating game trees. In Proceedings of the 27th Annual IEEE
Symposium on Foundations of Computer Science, pages 29–38, 1986.

[Szu98] Jerzy Szulga. Introduction to random chaos. Chapman & Hall, 1998.

[Tak83] Akimichi Takemura. Tensor analysis of ANOVA decomposition. Journal of the
American Statistical Association, 78(384):894–900, 1983.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

410 Bibliography

[Tal89] Michel Talagrand. A conjecture on convolution operators, and a non-Dunford–
Pettis operator on L1. Israel Journal of Mathematics, 68(1):82–88, 1989.

[Tal93] Michel Talagrand. Isoperimetry, logarithmic Sobolev inequalities on the discrete
cube and Margulis’ graph connectivity theorem. Geometric And Functional Anal-
ysis, 3(3):298–314, 1993.

[Tal94] Michel Talagrand. On Russo’s approximate zero-one law. Annals of Probability,
22(3):1576–1587, 1994.

[Tal96] Michel Talagrand. How much are increasing sets positively correlated? Combina-
torica, 16(2):243–258, 1996.

[Tal06] Michel Talagrand. Regularization from l1 by convolution. http://www.math.
jussieu.fr/~talagran/prizes/convolution.pdf , 2006.

[Tan61] Meyer Tannenbaum. The establishment of a unique representation for a linearly
separable function. Technical report, Lockheed Missiles and Space Company,
1961. Threshold Switching Techniques, 20:1–5.

[Tar89] Gábor Tardos. Query complexity, or why is it difﬁcult to separate NPA ∩ coNPA

from PA by random oracles? Combinatorica, 9(4):385–392, 1989.

[Ter99] Audrey Terras. Fourier Analysis on Finite Groups and Applications. Cambridge
University Press, 1999.

[Teu12] Jonas Teuwen. A cornucopia of Hermite polynomials. http://fa.its.tudelft.
nl/~teuwen/Writings/Proof-of-competency.pdf , 2012.

[Tho87] Andrew Thomason. Pseudo-random graphs. Annals of Discrete Mathematics,
144:307–331, 1987.

[Tit62] Robert Titsworth. Correlation properties of cyclic sequences. PhD thesis, Califor-
nia Institute of Technology, 1962.

[Tit63] Robert Titsworth. Optimal ranging codes. Technical Report 32-411, Jet Propulsion
Laboratory, 1963.

[Tro58] Hale Trotter. Approximation of semi-groups of operators. Paciﬁc Journal of Math-
ematics, 8:887–919, 1958.

[TSSW00] Luca Trevisan, Gregory Sorkin, Madhu Sudan, and David Williamson. Gad-
gets, approximation, and linear programming. SIAM Journal on Computing,
29(6):2074–2097, 2000.

[TZ00] Jean-Pierre Tillich and Gilles Zémor. Discrete isoperimetric inequalities and
the probability of a decoding error. Combinatorics, Probability and Computing,
9(5):465–479, 2000.

[UO30] George Uhlenbeck and Leonard Ornstein. On the theory of the Brownian motion.
Physical Review, 36(5):823–841, 1930.

[Val84] Leslie Valiant. A theory of the learnable. Communications of the ACM,
27(11):1134–1142, 1984.

[Val12] Gregory Valiant. Finding correlations in subquadratic time, with applications to
learning parities and juntas with noise. Technical Report TR12-006, Electronic
Colloquium on Computational Complexity, 2012.

[Vil47] Naum Vilenkin. On a class of complete orthonormal systems. Izvestiya Rossiiskoi
Akademii Nauk, Seriya Matematicheskaya, 11(4):363–400, 1947.

[Vio09a] Emanuele Viola. Correlation bounds for polynomials over {0, 1}. SIGACT News,
40(1):27–44, 2009.

[Vio09b] Emanuele Viola. The sum of d small-bias generators fools polynomials of degree
d. Computational Complexity, 18(2):209–217, 2009.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Bibliography 411

[Vit84] Richard Vitale. An expansion for symmetric statistics and the Efron–Stein in-
equality. In Inequalities in Statistics and Probability, volume 5 of Lecture Notes—
Monograph Series, pages 112–114. Institute of Mathematical Statistics, 1984.

[vM47] Richard von Mises. On the asymptotic distribution of differentiable statistical
functions. Annals of Mathematical Statistics, 18(3):309–348, 1947.

[Wal23] Joseph Walsh. A closed set of normal orthogonal functions. American Journal of
Mathematics, 45(1):5–24, 1923.

[Wat64] Chinami Watari. Multipliers for Walsh–Fourier series. Tôhoku Mathematical
Journal, Second Series, 16(3):239–251, 1964.

[Wei79] Fred Weissler. Two-point inequalities, the Hermite semigroup, and the Gauss–
Weierstrass semigroup. Journal of Functional Analysis, 32(1):102–121, 1979.

[Wei80] Fred Weissler. Logarithmic Sobolev inequalities and hypercontractive estimates
on the circle. Journal of Functional Analysis, 37(2):218–234, 1980.

[Wit75] Hans Witsenhausen. On sequences of pairs of dependent random variables. SIAM
Journal on Applied Mathematics, 28(1):100–113, 1975.

[Wol07] Paweł Wolff. Hypercontractivity of simple random variables. Studia Mathematica,
180(3):219–236, 2007.

[XM88] Guozhen Xiao and James Massey. A spectral characterization of correlation-
immune combining functions. IEEE Transactions on Information Theory,
34(3):569–571, 1988.

[Yan04] Ke Yang. On the (im)possibility of non-interactive correlation distillation. In Pro-
ceedings of the 6th Annual Latin American Informatics Symposium, pages 222–
231, 2004.

[Yao77] Andrew Yao. Probabilistic computations: Towards a uniﬁed measure of complexity.
In Proceedings of the 9th Annual ACM Symposium on Theory of Computing, pages
222–227, 1977.

[Yao85] Andrew Yao. Separating the polynomial time hierarchy by oracles. In Proceedings
of the 26th Annual IEEE Symposium on Foundations of Computer Science, pages
1–10, 1985.

[Zhe27] Ivan Zhegalkin. On a technique of calculating propositions in symbolic logic.
Matematicheskii Sbornik, 43:9–28, 1927.

[Zue89] Yuri Zuev. Asymptotics of the logarithm of the number of threshold functions of
the algebra of logic. Doklady Akademii Nauk SSSR, 39(3):512–513, 1989.

[Zwi99] Uri Zwick. Outward rotations: A tool for rounding solutions of semideﬁnite pro-
gramming relaxations, with applications to MAX CUT and other problems. In
Proceedings of the 31st Annual ACM Symposium on Theory of Computing, pages
679–687, 1999.

[Zwi02] Uri Zwick. Computer assisted proof of optimal approximability results. In Proceed-
ings of the 13th Annual ACM-SIAM Symposium on Discrete Algorithms, pages
496–505, 2002.

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Index

(2, 4)-hypercontractivity, see Bonami
Lemma, 253, 271
(2, q)-hypercontractivity, see
hypercontractivity, (2, q)- and (p, 2)-
3-Lin, see Max-3-Lin
3-Sat, see Max-3-Sat
k-wise independent, 154–155, 170
0-1 multilinear representation, 35
2
π Theorem, 127

Aaronson–Ambainis Conjecture, 246
AC0, see constant-depth circuits
afﬁne function, 38
afﬁne subspace, 72
algebraic normal form, see F 2-polynomial
representation
almost k-wise independent, see (ϵ, k)-wise
independent
(α, β)-approximation algorithm, 188
(α, β)-distinguishing algorithm, 196
Ambainis function, see sortedness function
analysis of Boolean functions, 19–388
analysis of Gaussian functions, 328–350
AND function, 44
ANOVA decomposition, see orthogonal
decomposition
anticoncentration, 249, 272
Gaussians, 357
polynomials of Gaussians, see
Carbery–Wright Theorem
approximating polynomial, 117, 136
approximation algorithm, see
(α, β)-approximation algorithm
 arity (CSP), 184
Arrow’s Theorem, 58, 175, 369
assignment (CSP), 186
assignment tester, see PCPP
assisted proof, see PCPP
attenuated inﬂuence, see stable inﬂuence
automorphism group, 39, 64, 241
average sensitivity, see total inﬂuence

B-reasonable, see reasonable random
variable
balanced, see unbiased
bent functions, 151–152, 170
Berry–Esseen Theorem, 119, 350–357,
386
multidimensional, 138
multivariate, 357, see Invariance
Principle for sums of random vectors
nonuniform, 137
Variant, 355, 357
biased Fourier analysis, 220
bit, 19, 20
BLR (Blum–Luby–Rubinfeld) Test, 32,
174, 176, 197
derandomized, 159, 171
BLR+NAE Test, 176
Bobkov’s Inequality, 346–350, 374, 385
Bonami Lemma, 247, 250, 271
Boolean cube, see cube, Hamming
Boolean function, 19
real-valued, 21, 28
Boolean-valued function, 28
 413

414 Index

Borell’s Isoperimetric Theorem, 327,
340–343, 369, 373–378, 385
volume- 1
2 case, 340–342, 367
Bourgain’s Sharp Threshold Theorem,
306–312

Carbery–Wright Theorem, 363, 387
Central Limit Theorem, 118, 119, 329, 350
multidimensional, 120, 138
Chang’s Inequality, see Level-1 Inequality
character, 227–229
chi-squared distance, 38
Chow parameters, 114
Chow’s Theorem, 114
for polynomial threshold functions, 116
Circuit-Sat, 188
circuits, see also constant-depth circuits
circuits (De Morgan), 108
CLT, see Central Limit Theorem
CNF, 94
codimension, 72
collision probability, 38
complete quadratic function, 34, 109, 135,
144, 152, 197
compression, see polarization
concentration, spectral, 69, 79
Condorcet Paradox, 57–58, 369
constant-depth circuits, 103–107, 135
learning, 106
spectrum, 106
constraint satisfaction problem, see CSP
convolution, 29–30, 229
correlated Gaussians, 330
vectors, 330
correlated strings, 53
correlation distillation, 66, 134
correlation immune, 147, 170
coset, see afﬁne subspace
covariance, 27
cryptography, 82, 90, 107
CSP, 183–193
equivalence with testing, 186–187
cube, Hamming, 20

decision list, 87
decision tree, 73, 229
depth, 74
expected depth, 230
Fourier spectrum, 74
learning, 82, 89, 159, 242, 273
product space domains, 230
randomized, 230, 242
 read-once, 87
size, 74
decision tree process, 234
degree, 28, 36, 149, 150
product space domains, 215
degree-1 Fourier weight, see Fourier
weight, degree-1
degree k part, 28
general product space, 220
density function, see probability density
derandomization, 157–160
derivative operator, 47
biased Fourier analysis, 222
Dickson’s Theorem, 165
dictator, 44
biased Fourier analysis, 221
dictator testing, see testing, dictatorship
Dictator-vs.-No-Notables test, 191, 366
connection with hardness, 192, 364
for Max-E3-Lin, 193–195
directional derivative, 161
discrete cube, see cube, Hamming
discrete derivative, see derivative operator
discrete gradient, see gradient operator
distance, relative Hamming, 26
DNF, 93
Fourier spectrum, 96, 101–102, 108
read-once, 108
size, 94
width, 94, 269
domain (CSP), 184
dual group, 229, 241
dual norm, 259
dual, Boolean, 35

edge boundary, 46, 50
Efron–Stein decomposition, see orthogonal
decomposition
Efron–Stein Inequality, see Poincaré
Inequality
entropy functional, 319
(ϵ, δ)-small stable inﬂuences, 145, 191
(ϵ, k)-regular, 146
(ϵ, k)-wise independent, 146, 155
ϵ-biased set, see probability density,
ϵ-biased density
ϵ-close, 31
ϵ-fools, see fooling
ϵ-regular, 144
ϵ-uniform, see ϵ-regular
equality function, 34, 164

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Index 415

Erd˝os–Rényi random graph, see random
graph
even function, 35
exclusive-or, see parity
expansion, 52
small-set, 52, 126, 255, 263, 267, 284,
320
expectation operator, 48, 212

F 2-degree, 149, 150, 160
F 2-polynomial representation, 148–150,
169
learning, 167
F 2ℓ (ﬁnite ﬁeld), 153
Fast Walsh–Hadamard Transform, 37
FKN Theorem, 61, 129, 252
folding, 199
fooling, 160
Fourier analysis of Boolean functions, see
analysis of Boolean functions
Fourier basis, 209, 336, 338
Fourier coefﬁcient, 22
formula, 25
product space domains, 211
Fourier expansion, 20–23
product space domains, 211
Fourier norm, 72
1-, 36, 83, 86, 87, 91, 157–159
4-, 38, 145, 160, 168
Fourier sparsity, 72, 89, 276
Fourier spectrum, 22
Fourier weight, 27
degree-1, 60, 124–125, 139
general product space, 220
F p (ﬁnite ﬁeld), 229
Friedgut’s Conjecture, 305
Friedgut’s Junta Theorem, 268–269, 307
product space domains, 294, 304
Friegut’s Sharp Threshold Theorem, 305

Gaussian isoperimetric function, 125, 139,
343
Gaussian Isoperimetric Inequality,
343–347, 384–385
Gaussian Minkowski content, see
Gaussian surface area
Gaussian noise operator, 330, 384
Gaussian quadrant probability, 120, 138,
274, 373, 376
Gaussian random variable, 118, 119
simulated by bits, 329
Gaussian space, 328, 384
 Gaussian surface area, 343–347, 372, 384
Gaussian volume, 328
General Hypercontractivity Theorem, see
Hypercontractivity Theorem, General
Goemans–Williamson Algorithm, 189,
364–366, 379
Goldreich–Levin Algorithm, 82–85,
157–159
Gotsman–Linial Conjecture, 133, 346
Gotsman–Linial Theorem, 114, 116
Gowers norm, 168
gradient operator, 51
granularity, Fourier spectrum, 36, 72–74,
89, 165
graph property, 223, 295
monotone, 224, 305
Guilbaud’s Formula, 59

Hadamard Matrix, 36
halfspace, see linear threshold function
Hamming ball, 61
degree-1 weight, 125
Hamming cube, see cube, Hamming
Hamming distance, 20
harmonic analysis of Boolean functions,
see analysis of Boolean functions
Hatami’s Theorem, 307
Hausdorff–Young Inequality, 86
hemi-icosahedron function, 34
Hermite expansion, 338
Hermite polynomials, 336–338, 370–372,
384
multivariate, 338
Hoeffding decomposition, see orthogonal
decomposition
Hölder inequality, 253
hypercontractivity, 40, 116, 256–257, 273,
278–281, 283, 287–292, 324
(2, q)- and (p, 2)-, 257–261
(2, q)- and (p, 2)−, 247
biased bits, 291
general product probability spaces,
316–319
induction, 259–261, 286, 313
preserved by sums, 256, 313
Hypercontractivity Theorem, 247, 273,
283–287
Gaussian, 333–334, 384
General, 283, 292
Reverse, 324
Two-Function, 259–261, 280, 284–286,
375

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

416 Index

Hypercontractivity Theory
Reverse, 314
hypercube, see cube, Hamming

impartial culture assumption, 45
indicator basis, 208
indicator function, 29, 33
indicator polynomial, 21
induction, 259
inﬂuence, 46–48
ρ-stable, see stable inﬂuence
average, 64, 131
biased Fourier analysis, 222
coalitional, 274
maximum, 265
product space domains, 213–214
inner product, 24
inner product mod 2 function, 34, 117,
144, 149, 151, 160, 197
instance (CSP), 185
Invariance Principle, 386
basic, 359, 368
for sums of random variables, 354
for sums of random vectors, 381
general product spaces, 382
multifunction, 382
Invariance Principles, 357–364, 381–383
isomorphic, 39
isoperimetric inequality
Hamming cube, 52, 138, 266, 320, 347
Itô’s Formula, 348

junta, 44, 269
learning, 89, 155–156, 167, 171

k-wise independent, 147
Kahn–Kalai–Linial Theorem, see KKL
Theorem
Khintchine(–Kahane) Inequality, 66, 115,
262
KKL Theorem, 97, 265–268, 281
edge-isoperimetric version, 267
product space domains, 294
Kravchuk polynomials, 137, 371
Krawtchouk polynomials, see Kravchuk
polynomials
Kushilevitz function, see
hemi-icosahedron function
Kushilevitz–Mansour Algorithm, see
Goldreich–Levin Algorithm

L2, 207
Lévy distance, 357, 363
 Laplacian operator, 51
ith coordinate, 49, 213
learning theory, 78–82, 130, 157–159
Level-k Inequalities, 256, 264
level-1 Fourier weight, see Fourier weight,
degree-1
Level-1 Inequality, 126, 264, 273
Lindeberg Method, see Replacement
Method
linear (over F 2), 31
linear threshold function, 44, 113–114,
269
Fourier weight, 114–115
learning, 130
noise stability, 121, 130–133, 138
literal, 93
LMN Theorem, 106
locally correctable, 33
locally testable proof, see PCPP
Log-Sobolev Inequality, 280, 320–321
Gaussian, 335, 384
product space domains, 321
Low-Degree Algorithm, 81, 90
low-degree projection, see projection,
low-degree
LTF, see linear threshold function

Möbius inversion, 164
majority, 21, 34, 43
Fourier coefﬁcients, 122
Fourier weight, 121–124
noise stability, 54, 120–121, 136, 138
total inﬂuence, 51, 118–119
Majority Is Least Stable Conjecture, 133
Majority Is Stablest Theorem, 121, 127,
327, 358, 364, 368–369
general product spaces, 383
Mansour’s Conjecture, 96
Margulis–Russo Formula, 224, 239, 295
martingale
Doob, 237
martingale difference sequence, 237, 278
Max-2-Lin, 379
Max-3-Coloring, 184, 185
Max-3-Lin, 184, 185, 188, see also
Dictator-vs.-No-Notables test for
Max-E3-Lin
Håstad’s hardness for, 190
Max-3-Sat, 184, 185, 190, 197
Håstad’s hardness for, 190
Max-ψ, 185
Max-CSP(Ψ), 184–186

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Index 417

Max-Cut, 184, 185, 189, 364–368
May’s Theorem, 45
mean, 26, 146
Mehler transform, see Gaussian noise
operator
Minkowski content, see Gaussian
Minkowski content
mod 3 function, 34, 166
molliﬁcation, 356, 379–381
monotone
DNF, 107
monotone function, 45
learning, 81, 273
monotone graph property, see graph
property, monotone
multi-index, 210
multilinear polynomial, 20

n-cube, see cube, Hamming
NAE Test, 175
noise operator, 55
applied to individual coordinates, 301
Gaussian, see Gaussian noise operator
product space domains, 214
noise sensitivity, 54, 366
Gaussian, see rotation sensitivity
vs. total inﬂuence, 131
Noise Sensitivity Test, 366
noise stability, 53–57
product space domains, 214
uniform, see uniformly noise-stable
noisy hypercube graph, 254, 274
noisy inﬂuence, see stable inﬂuence
norm, 24
normal random variable, see Gaussian
random variable
not-all-equal (NAE) function, 34, 58
notable coordinates, 57, 145, 191
NP-hard, 188, 197
number operator, see Ornstein–Uhlenbeck
operator

odd function, 35, 45
optimum value (CSP), 186
OR function, 44, 305
Ornstein–Uhlenbeck operator, 334, 339
Ornstein–Uhlenbeck semigroup, see
Gaussian noise operator
orthogonal complement, see perpendicular
subspace
orthogonal decomposition, 216–219, 244
orthonormal, 24, 209
 OS Inequality, 232, 273
OSSS Inequality, 232, 243, 362
OXR function, 34, 201

p-biased Fourier analysis, see biased
Fourier analysis
(p, 2)-hypercontractivity, see
hypercontractivity, (2, q)- and (p, 2)-
PAC learning, see learning theory
Paley–Zygmund inequality, 249
parity, 23, 106, 108, 109, 148
parity decision tree, 88
Parseval’s Theorem, 25, 211, 339
complex case, 240
PCP Theorem, 183, 189
PCPP, 179–182
PCPP reduction, 182–183
Peres’s Theorem, 130, 269
perpendicular subspace, 72
pivotal, 46, 61, 238
Plancherel’s Theorem, 26, 211, 339
complex case, 227, 240
Poincaré Inequality, 52, 266, 320
Poisson summation formula, 78
polarization, 65, 275
polynomial linear threshold function
Fourier spectrum, 116
polynomial threshold function, 115–116,
269
degree, 136
Fourier spectrum, 116
noise stability, 133, 139
sparsity, 116, 117, 136
total inﬂuence, 133–134, 139
predicates (CSP), 184
probabilistically checkable proof of
proximity, see PCPP
probability density, 29
ϵ-biased, 144, 152–154
probability density, ϵ-biased, 169
probability density,ϵ-biased, 157
product basis, 209, 338
product probability space, 207
product space domains, 207–220
projection
low-degree, 271, 299–301
projection onto coordinates, 88, 212
property testing, see testing
local tester, 174, 178
pseudo-junta, 307, 322
PTF, see polynomial threshold function

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

418 Index

Rademacher functions, 39
random function, 35, 62, 89, 135, 136, 143,
163
random graph, 223, 323
random subset, 98
randomization/symmetrization, 289–291,
297–304, 308, 315, 316, 325
randomized assignment, 198
reasonable random variable, 248, 289,
350, 359
recursive majority, 44, 231, 242
regular, see ϵ-regular
relevant coordinate, 47
Replacement Method, 351, 359
resilient, 147, 170
restriction, 74–77
Fourier, 76
random, 98–100
to subspaces, 77–78
revealment, 230, 231, 242, 243
Reverse Hypercontractivity Theorem, see
Hypercontractivity Theorem, Reverse
Reverse Small-Set Expansion Theorem,
see Small-Set Expansion Theorem,
Reverse
ρ-correlated Gaussians, see correlated
Gaussians
ρ-correlated strings, see correlated strings
ρ-stable hypercube graph, see noisy
hypercube graph
rotation sensitivity, 342, 385
subadditivity, 342, 346
Russo–Margulis Formula, see
Margulis–Russo Formula

satisﬁable, 186
SDP, see semideﬁnite programming
second moment method, see
Paley–Zygmund inequality
selection function, 34
semideﬁnite programming, 364
semigroup property, 63, 273, 331, 370
sensitivity, 49
set system, 19
Shapley value, 239
Shapley–Shubik index, see Shapley value
sharp threshold, see threshold, sharp
Sheppard’s Formula, 120, 332
shifting, see polarization
Siegenthaler’s Theorem, 150–151, 156,
170
 small stable inﬂuences, see (ϵ, δ)-small
stable inﬂuences
Small-Set Expansion Theorem, 263, 274
generalized, 284, 324, 375
product space domains, 293
Reverse, 285, 314, 315, 324
social choice, 43
social choice function, 43
sortedness function, 34
sparsity (fractional), 86
spectral concentration, see concentration,
spectral
spectral norm, see Fourier norm
spectral sparsity, see Fourier sparsity
stable inﬂuence, 57, 145, 255, 264
product space domains, 215, 293
Stirling’s Formula, 62
string, 19
subcube, 73
degree-1 weight, 125
subcube partition, 87
subspaces, 72
Switching Lemma
Baby, 100, 110
Håstad’s, 100, 104–106
symmetric function, 45
symmetric random variable, 289

Tρ, see noise operator
tensorization, see hypercontractivity,
induction
term (DNF), 93
test functions, 352
Lipschitz, 356
testing, 31, 173–175
dictatorship, 175
linearity, 32
threshold function, see linear threshold
function
threshold phenomena, 223
threshold, sharp, 225, 226, 238, 295–297,
304, 306, 323
threshold-of-parities circuit, 116, 135
total inﬂuence, 49–52
DNF formulas, 95, 99, 109, 238
monotone functions, 51
product space domains, 213, 304
total variation distance, 37
transitive-symmetric function, 45, 64, 223,
241, 295
decision tree complexity, 231
tribes function, 45, 62, 68, 96–97, 108, 265

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.

Index 419

Two-Point Inequality, 286
Reverse, 315

Uρ, see Gaussian noise operator
UG-hardness, 192, 201, 364
unate, 61, 132
unbiased, 26
uncertainty principle, 87
uniform distribution, 24
uniform distribution on A, 29
uniformly noise-stable, 130, 269, 358
Unique-Games, 192, 200, 204, 364

value (CSP), 186
variance, 26
Viola’s Theorem, 161
voting rule, see social choice function

Walsh functions, 39
Walsh–Hadmard Matrix, 36
weight, see Fourier weight
weighted majority, see linear threshold
function

XOR, see parity

Yao’s Conjecture, 231

Copyright © Ryan O’Donnell, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021.
