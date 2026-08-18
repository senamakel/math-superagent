<!-- source: https://doi.org/10.1007/s40863-024-00471-2 | converted from HTML -->

From Abel’s differential equations to Hilbert’s 16th problem | São Paulo Journal of Mathematical Sciences | Springer Nature Link

Skip to main content

# From Abel’s differential equations to Hilbert’s 16th problem

- Stability and Bifurcation - Memorial Issue Dedicated to Jorge Sotomayor
- [Open access][1]
- Published: 28 September 2024

- Volume 18, pages 1342–1379 ( 2024)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[São Paulo Journal of Mathematical Sciences][5] [Aims and scope][6] [Submit manuscript][7]

From Abel’s differential equations to Hilbert’s 16th problem

[Download PDF][2]

## Abstract

The study of the limit cycles of planar polynomial differential equations is motivated both by its appearance in many mathematical models of the real-world as for the second part of Hilbert’s 16th problem. In this work we briefly summarize some results on this subject and we will also highlight the important role that the Abel’s differential equations play in its study. In the way, we recall some nice properties of the Riccati’s differential equations.

### Similar content being viewed by others

### [The extended 16th Hilbert problem for a class of discontinuous piecewise differential systems][8]

Article 20 September 2022

### [Some open problems in low dimensional dynamical systems][9]

Article 22 March 2021

### [Chapter 2 Abelian Integrals and Limit Cycles][10]

Chapter © 2024

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Differential Equations][11]
- [Differential Geometry][12]
- [Dynamical Systems][13]
- [Linear Algebra][14]
- [Mathematics][15]
- [Ordinary Differential Equations][16]
- [Dynamical Systems and Bifurcation Theory][17]

## 1 Introduction

The aim of this work is to motivate the study of limit cycles of planar autonomous ordinary differential equations (DEs) and to illustrate the difficulties of their study. To this end, we will present some simple real-world problems where limit cycles appear and we will also recall the Hilbert’s 16th problem.

We will focus our attention on the limit cycles for Abel’s DEs because this family is perhaps the “easiest one” where this question is open. Moreover, it is known that the Hilbert’s problem restricted to the DEs of degree 2 will follow from the full knowledge of Abel’s equations. In the way we will collect related results for linear and Riccati’s DEs.

I first heard of Abel’s equations while I was doing my Ph.D. thesis under the supervision of Jaume Llibre. During that period we collaborated with Jorge Sotomayor and, in Chapter 4 of this thesis, we used them to control the number of limit cycles of a family of planar DEs, see [[59][18], [70][19], [71][20]].

This work is an updated and extended version of my paper [[61][21]], which was published in Catalan, and it was based on the opening lecture of the academic year 2011–2012 at the Department of Mathematics of the Universitat Autònoma de Barcelona. The title of that lesson was “Equacions diferencials d’Abel o el miratge de la simplicitat”, that is *Abel’s differential equations or the mirage of simplicity*.

## 2 Main goal

Polynomial differential equations in the plane often appear as simple models of various phenomena in physics, ecology, chemistry, economics, medicine, and many other disciplines. Let us see a few examples.

Using Ohm’s, Faraday’s, and Kirchhoff’s laws the differential equation that models the state of a RLC (resistor-inductor-capacitor) circuit can be deduced. This equation is today called van der Pol’s equation, since it was studied for first time by Balthasar van der Pol in 1927, see [[83][22], [128][23]]. In dimensionless version it is written as \(\ddot{x}+\mu (x^2-1)\dot{x}+x=0\), or equivalently as the system of cubic DEs in the plane,

$$\begin{aligned} \dot{x}=y,\quad \dot{y}=-x-\mu (x^2-1)y, \end{aligned}$$

where \(\mu\) is a certain positive parameter, *x*gives us the normalized intensity of the circuit and *y*its normalized voltage.

The predator–prey model of Rosenzweig–MacArthur ( [[106][24], [118][25]]) is given by the system of DEs

$$\begin{aligned} \dot{x}=rx\left( 1-\frac{x}{k}\right) -\frac{mxy}{A+x},\quad \dot{y}=-\delta y+\gamma \frac{mxy}{A+x}, \end{aligned}$$

where all the parameters are positive, and \(x\ge 0, y\ge 0\) are the densities of both populations. By introducing a new time *s*such that \(\textrm{d}t/\textrm{d}s=A+x,\) the system is transformed into a system of cubic polynomial differential equations. In fact, in general, the models of population dynamics are written in the so-called *Kolmogorov’s form*

$$\begin{aligned} \dot{x}=xf(x,y),\quad \dot{y}=yg(x,y), \end{aligned}$$

for certain functions *f*and *g*that take into account the interrelation between both populations, giving rise to predator–prey, parasitism, symbiosis or competition models. These functions are often taken as polynomial or rational.

A model, again dimensionless, to study the evolution of chemical reactions is

$$\begin{aligned} \dot{x}=x^2y-x+b,\quad \dot{y}=-x^2y+a, \end{aligned}$$

where *a*and *b*are positive real parameters and *x*and *y*give us the concentrations of the reactants; see [[122][26]]. In fact, this model is often known as *Brusselator*and is a theoretical model for a type of auto-catalytic reaction. Its name is an acronym of “Brussels” and “oscillator.”

Finally, next dimensionless differential equation models the formation of spiral galaxies

$$\begin{aligned} \dot{x}= a(1-x-y)-bxy^2,\quad \dot{y}=-y(1-x-y)+bxy^2, \end{aligned}$$

where the two variables are related with the amount of warm and hot gas, see [[5][27], [86][28]].

**Fig. 1**

[image: Fig. 1]

[Full size image][29]

On the left, a limit cycle in the (*x*, *y*) plane and two orbits tending to it. On the right, the first coordinate \(x=x(t)\) of one of the orbits that tends to the limit cycle

It can be seen that all four models are characterized by the fact that when time increases the solutions tend to a periodic orbit (limit cycle) of the differential equation. This solution tells us how the circuit, or the predator–prey model, or the chemical reaction, or the temperature of the gas, respectively, behaves. In all cases, after a certain transient state, we observe a stable oscillatory behavior of the model, see Fig. [1][30].

Limit cycles are present in many other situations, like for instance in the planar DEs that appear in the Emden–Fowler’s equation of astrophysics [[26][31], [45][32]], the Blasius’ equation of fluid mechanics [[45][32], [130][33]], or in the Selkov’s model of glycolysis [[123][34]].

Of course, there are many other real-world models where the corresponding DEs have more than one limit cycle. For instance the planar predator–prey model, again in dimensionless variables,

$$\begin{aligned} \dot{x}=x\big (x(1-x)-(x+n)y\big ),\quad \dot{y} =y(x+n)(x-m), \end{aligned}$$

has for some values of the parameters at least two limit cycles, see [[5][27], [13][35]]. Two limit cycles also appear for instance in the Holling–Tanner predator–prey model, see [[67][36], [95][37]].

Remember that, in general, given an equation, \(\dot{\textbf{x}}=f(\textbf{x}),\) \(\textbf{x}\in {\mathbb {R}}^n\), a non-constant solution \(\textbf{x}=\phi (t)\) such that \(\phi (t+T)=\phi (t),\) for a certain \(T>0\), is called *periodic orbit*of the equation. The minimum value *T*that satisfies the aforementioned property is called the *period*of the periodic orbit. If this periodic orbit has an open neighborhood in the phase space within which the differential equation does not have other periodic behaviors, then it is called a *limit cycle*.

The above examples, and many others, show that the periodic orbits in general, and the limit cycles in particular, are some of the interesting objects that appear when DEs are studied. This is even more true when we consider DEs in the plane, because in this case the Poincaré–Bendixson theorem assures that the so-called *strange attractors*do not appear and then all limit behaviors are simple. Specifically, these are either equilibrium points (stationary behaviors) or periodic orbits (oscillatory behaviors), or the so-called *graphics*or *polycycles*, which will not be treated in this work; see the nice monographs [[126][38], [127][39]] by Jorge Sotomayor for more details or Roussarie’s book [[120][40]]. In fact, notice that limit behaviors correspond precisely to the solutions of a differential equation observable in real-world models.

Anyway, the motivation to study the limit cycles of planar polynomial DEs is not limited to its applicability for the study of various models. In fact, Hilbert, in his famous list of problems presented in the International Mathematical Conference of 1900, devoted the second part of his 16th problem to propose a question on this matter. It could be summarized as

“Given the family of differential equations in \({\mathbb {R}}^2,\)

$$\begin{aligned} \dot{x}=P_n(x,y),\quad \dot{y}=Q_n(x,y), \end{aligned}$$

(1)

where \(P_n\) and \(Q_n\) are arbitrary polynomials of degree less than or equal to *n*, find out if there is a uniform bound, \({\mathcal {H}}(n)\), for the number of limit cycles that it may have."

The first part of the 16th problem refers to the number and arrangement of the components of a plane algebraic curve, for more details see for instance [[129][41], [134][42]].

Hilbert’s question was probably motivated by the previous studies by Henri Poincaré. It is interesting to read the work [[79][43]] in which it is explained the Poincaré’s answer (of 1908) to the Hilbert’s list of problems.

[image: figure a]

The second part of 16th problem is far from being solved. At the end of the past century there were significant advances. Independently, Écalle and Il’yashenko in [[53][44], [87][45]] asserted that each individual vector field of the form ( [1][46]) has a finite number of limit cycles. Nevertheless, nowadays these proofs are not fully accepted by the mathematical community. According Smale’s words in the year 1998 paper, [[125][47]], these works were not yet been digested by this community. In fact, in the recent preprint [[137][48]] the author shows a gap in Il’yashenko’s proof. At the moment this individual finitude problem, also known as *Dulac’s finitude problem*, begins to be considered again as an open problem.

Recall that, in principle, a monodromic point of a planar polynomial DE can be a center, or a focus, or a point which is an accumulation of limit cycles. This third possibility can be discarded if the answer to the Dulac’s finitude problem is positive. As a consequence of the comments of the above paragraph, the exclusion of this third possibility is also under review.

On the occasion of its centenary, several reviews emerged on the advances in the list of problems. We cite for example [[88][49], [96][50]]; see also [[80][51]]. It is also worth noting that the Smale’s paper quoted above, in a list of problems for this century ( [[125][47]]), again includes the question of the number of cycles of planar polynomial differential equations. Due to the aforementioned difficulty in addressing the general case ( [1][46]), he proposed direct all efforts to a particular case of polynomial DEs in the plane, the so-called *Liénard’s equations*,

$$\begin{aligned} \dot{x}= y-F_n(x),\quad \dot{y}=-x,\end{aligned}$$

(2)

where \(F_n\) is a polynomial of degree *n*. The solution for this particular case has also resisted all the attempts. Lately, there have been small but important advances in regard this issue which show that it is even more difficult than it seemed, see [[46][52], [47][53], [51][54], [76][55], [94][56]].

In fact, during 40 years people tried to prove that the maximum number of limit cycles of ( [2][57]) was \([(n-1)/2],\) where as usual \([\cdot ]\) denotes the integer part function. This lower bound and the conjecture that it is the actual upper bound was formulated in 1977 in [[98][58]] and was known as *Lins–Melo–Pugh’s conjecture*. These limit cycles were obtained by the so-called *Poincaré’s perturbation method*, that consists on consider a differential equation with a continuum of periodic orbits and then perturb it to see how many of them persist with small perturbations, see Sect. [4.2][59] for more details on this approach. In [[51][54]] the authors showed that the conjecture was wrong. Nowadays, it is known that for \(n\ge 6\) these equations have at least \(n-2\) limit cycles, giving the best known lower bound, see [[47][53]]. The examples in [[47][53], [51][54]] with more limit cycles than expected for Eq. ( [2][57]) were obtained by using the geometric theory of *planar slow-fast systems*.

Indeed, as far as the author knows, it is yet an open problem to know if Lins–Melo–Pugh’s conjecture holds for Liénard differential Eq. ( [2][57]) when \(F_n\) is odd, that is \(F_n(-x)=-F_n(x).\) In fact, there are examples with \(F_n\) odd and \([(n-1)/2]\) limit cycles and all the examples with more limit cycles correspond to a non odd \(F_n.\) Moreover, it is known that this result is true for \(n=3,5,\) see [[98][58], [121][60]].

As a personal note, I would like to comment that the first task that, around 1982, my Ph.D. advisor proposed me was to prove Lins–Melo–Pugh’s conjecture. By computing the *Lyapunov quantities*of Eq. ( [2][57]), we were able to show that \([(n-1)/2]\) was also the maximum number of *small-amplitude*limit cycles that can bifurcate from the origin via an *Andronov-Hopf bifurcation*, see [[58][61]]. During the same period the same result was obtained in [[17][62]] and indeed the result was already proved by Zuppa [[143][63]]. In fact, in [[73][64]] it is proved that it is not a coincidence that Poincaré’s perturbation method and the computation of the Lyapunov quantities give rise to the same amount of limit cycles.

Very little is known about the numbers \({\mathcal {H}}(n)\). It is easy to see that planar linear DEs do not have limit cycles, despite being able to present continua of periodic orbits. In consequence, \({\mathcal {H}}(1)=0\). It is not difficult to build a quadratic system of DEs with a limit cycle. For example the equation

$$\begin{aligned} \dot{x}= -y(2+x+y)-(x^2+y^2-1),\quad \dot{y}=x(2+x+y), \end{aligned}$$

has as limit cycle the circumference \(x^2+y^2-1=0.\) Moreover, it is its unique limit cycle, because if we define \(V(x,y)=(2+y)\sqrt{|x^2+y^2-1|}\) it holds that

$$\begin{aligned} \dot{V}(x,y)= \frac{\partial V(x,y)}{\partial x}P(x,y)+\frac{\partial V(x,y)}{\partial y}Q(x,y)=x^2\sqrt{|x^2+y^2-1|}\ge 0. \end{aligned}$$

Therefore, \({\mathcal {H}}(2)\ge 1\). Perhaps it should be noted here that, contrary to this academic example, the most part of the limit cycles appearing in planar DEs cannot be explicitly found in a closed form and, in particular they are not algebraic. It is instructive to read how to prove, for some specific systems, that their limit cycles are not algebraic. See for instance, [[54][65], [56][66], [65][67], [77][68], [107][69]]. In particular the limit cycle of the van der Pol’s equation is not algebraic.

According to Zoladek’s paper [[142][70]], probably the first example of a quadratic system with a limit cycle was given in 1929 by the physicist Sommerfeld and moreover he got two cycles at once. Nowadays it is known that \({\mathcal {H}}(2)\ge 4,\) see [[28][71], [124][72]], and it is thought that \({\mathcal {H}}(2)\) will be 4, but this seemingly simple problem is resisting all the available approaches. In fact, it is not even known if \({\mathcal {H}}(2)\) exists although there are proofs of Bamón and Romanovskii that each individual quadratic differential equation has finitely many limit cycles, see [[11][73], [12][74], [116][75], [117][76]]. These works were preceded by the approach of Chicone and Shafer [[32][77]] where the authors prove the same result, but restricted to any compact region. Similarly it is only known that \({\mathcal {H}}(3)\ge 13\) or that \({\mathcal {H}}(4)\ge 28\), see [[80][51], [92][78], [115][79]].

In fact, there is a point of view called *finite cyclicity method*introduced by Roussarie that gives a procedure to try to prove that \({\mathcal {H}}(n)\) is finite, see [[120][40], Chap. 2]. The idea is to compactify the phase space, as well as the space of polynomial DEs of degree *n*, and in this way a *global*finiteness result will be a consequence of several *local*finiteness results. Then, the problem is reduced to prove the finite cyclicity of the so-called *limit periodic sets*. In short, these sets are invariant compact sets for a given DE (in the compactified phase space) that can be approached by a sequence of limit cycles, being these limit cycles solutions of different DEs that tend to the initial given DE. This approach is developed in more detail for \(n=2\) in [[119][80]], by presenting the list of all possible limit periodic sets, showing for which ones is already known that they have finite cyclicity and which ones remain to be studied. Sometimes this approach for trying to prove that \({\mathcal {H}}(2)\) is finite is also called *Roussarie’s program*.

As for \({\mathcal {H}}(n)\), the best result is that it grows at least as \(O(n^2\log (n)).\) This result was proven in 1995 in [[34][81]]. See also [[3][82], [96][50]]. These lower bounds are very relevant because was the first time where people prove the existence of much more limit cycles than parameters of the differential equation, because the number of parameters increase as \(O(n^2).\)

In fact, Lloyd in [[103][83], p. 198] conjectured that \({\mathcal {H}}(n)\) grows as \(O(n^3).\) In his own words “My reasoning is simply that \(O(n^2)\) critical points can be encircled by limit cycles, and that there are likely to be at most *O*(*n*) limit cycles around each critical point.” It is also plausible to propose an upper bound that grows as \(O(n^4).\) The reason is that there are many situations where \(O(n^2)\) limit cycles surround a single equilibrium point, see for instance [[93][84]] and their references. Of course, what is much more difficult is to see that both quadratic grows happen simultaneously. This point of view is discussed in the recent paper [[24][85]]. Indeed, Smale in [[125][47]] asks if there exists a universal constant *q*such that \({\mathcal {H}}(n)\le n^q.\)

Due to the difficulty of the general Hilbert’s problem, the main objective of this work will be to locate which is the simplest family of DEs for which the problem of the number of limit cycles is still not solved and to give an overview of what is the current knowledge about this family. In fact, we will take an excursion that will start with the linear equations, continue with the Riccati’s equations, and end with the equations of Abel’s type.

Finally, in the last section of this paper we will see that, in fact, Abel’s equations are strongly related to Hilbert’s problem and, more specifically, to the determination of \({\mathcal {H}}(2),\) somehow closing the circle. In that section, we will also consider some more families of autonomous planar DEs for which the study of their limit cycles can be reduced to the study of some Abel’s equations.

The study of the limit cycles for general planar DEs, not necessarily polynomial, is included in most text books on differential equations. Without the aim of being exhaustive we list some monographs where the reader can find much more information over them, [[9][86], [10][87], [31][88], [33][89], [50][90], [112][91], [120][40], [136][92], [141][93]].

After the effort during many years of the mathematical community, unfortunately no universal tool for obtaining an upper bound (realistic or not) of the number of limit cycles of a given planar differential equation is known. As far as the author knows, there are three main approaches that have been widely used, but they only apply to some particular families of equations. These approaches are:

-

The use of the Bendixson–Dulac criterion, see [[30][94], [63][95], [64][96]].

-

Start by transforming the differential equation into a (generalized) Liénard’s differential equation

$$\begin{aligned} \dot{x}= \varphi (y)-F(x),\quad \dot{y}=-g(x), \end{aligned}$$

see for instance the changes of variables and time given in [[60][97]] or [[136][92], pp. 356–57], and afterwards apply some of the criteria created for these equations, see for instance [[29][98], [136][92], [141][93]].

-

Transform the differential equation into a special type of differential equation, like for instance an Abel’s DE, for which some results on the maximum number of limit cycles are known. This is the approach explained and developed in this work.

## 3 From linear to Abel’s differential equations

What a mathematician must do when faced with a problem, such as Hilbert’s 16th, which seems out of reach? Simply look for the apparently easier particular case of the problem that is not known how to solve and try to find an answer for it. Then, the (secret) hope is that the idea that has worked for this very particular case can go beyond.

It is easy to see that DEs in \({\mathbb {R}}\) do not have periodic solutions and hence they do not have limit cycles. We have already seen that DEs in \({\mathbb {R}}^2\) do have. It is natural to wonder ourselves what happens between \({\mathbb {R}}\) and \({\mathbb {R}}^2\)? The smooth equations of the form

$$\begin{aligned} \dot{x}=f(t,x),\end{aligned}$$

(3)

with \(x\in {\mathbb {R}}\) are called *non-autonomous*DEs and informally it is said that “they live in dimension 1.5". Let us study them. Since we are looking for differential equations with periodic solutions, we will impose in addition that *f*is *T*-periodic in *t*. In fact sometimes, changing the time scale, we can assume without loss of generality that \(T=2\pi\). For these non-autonomous equations we can define similarly the notions of periodic orbit and limit cycle.

The existing relations between the period of a non-autonomous DE and the periods of its solutions constitute a very interesting and perhaps not enough known matter. For completeness we state next result, proved in [[38][99]].

### Theorem 3.1

[[38][99]] Consider a *T*-periodic differential equation of class \({\mathcal {C}}^1,\) \(\dot{x} = f(t, x),\) defined on \({\mathbb {R}}\times {\mathbb {R}}^n.\) Let *S*be the (minimal) period of one of its periodic solutions. Then the following holds:

1. (i)

If \(n=1\) then \(T/S\in {\mathbb {N}}.\)

2. (ii)

When \(n\ge 2,\) for any couple of positive real numbers *S*, *T*, there is an *f*, *T*-periodic and of class \({\mathcal {C}}^1,\) having an *S*-periodic solution of the corresponding differential equation.

To satisfy the reader’s curiosity, we present here some concrete examples concerning the previous result.

For \(n=1\) and any \(0<k\in {\mathbb {N}},\) consider the linear *T*-periodic differential equation, with \(T=2\pi ,\)

$$\begin{aligned} \dot{x}=\big (x-\sin (kt)\big )\sin t + k \cos (kt). \end{aligned}$$

Clearly, it has the particular *S*-periodic solution \(x = \sin (kt),\) with \(S=2\pi /k.\) Hence \(T/S = k\) is a positive integer number. Notice that this solution is also a \(2\pi\) -periodic function although this is not its minimal period.

Similarly, for \(n=2\) we can consider the equation that in compact complex notation \(z = x + \textrm{i} y\) writes as

$$\begin{aligned} \dot{z}=\frac{2\pi }{S}\textrm{i}z+(z{\bar{z}}-1)\sin \Big (\frac{2\pi }{T} t\Big ), \end{aligned}$$

with *S*, *T*non-zero arbitrary real numbers. Notice that it is *T*-periodic and has the *S*-periodic solution \(z =\exp ( 2\pi \textrm{i} t/S).\) In fact, this example is essentially the one due to Erugin, see [[113][100], p.10] and highlights a crucial difference between dynamics in dimension one and in higher dimensions. Observe also that the periodic solution lies in the circumference \(z{\bar{z}}-1=0\) where the differential equation is “autonomous”. It can be seen that this property is shared for all periodic solutions which period *S*is such that \(T/S\not \in {\mathbb {Q}},\) see again [[113][100]]. To see that this is not the case when \(T/S=m/k\in {\mathbb {Q}},\) with \((m,k)\in {\mathbb {N}}^2,\) and \(\gcd (m,k)=1,\) consider the *T*-periodic differential equation

$$\begin{aligned} z'=\frac{m}{k} \textrm{i}z+(z^k-\textrm{e}^{\textrm{i}m t})\textrm{e}^{\textrm{i}t}, \end{aligned}$$

with \(T= 2\pi ,\) taken from [[38][99]]. It has the particular periodic solution \(z=\textrm{e}^{\textrm{i}m t/k},\) which has period \(S=2k\pi /m.\) Therefore \(T/S=m/k,\) as we wanted to see.

### Remark 3.2

As a consequence of item (i) of the above theorem we know that to study the number of periodic solutions of a \(2\pi\) -periodic differential equation ( [3][101]) it suffices to look for periodic solutions having also period \(2\pi ,\) which perhaps may not be minimal.

If we call \(x=\phi (t,\rho )\) the solution of ( [3][101]) such that \(\phi (0,\rho )=\rho ,\) the function \(\Pi (\rho ):=\phi (2\pi ,\rho )\) plays a determinant role to know its number of periodic orbits. So, the fixed points of \(\Pi (\rho )\) correspond to periodic orbits of ( [3][101]) and their isolated fixed points are initial conditions that give rise to limit cycles. This map \(\Pi\) is usually called *Poincaré map*, see Fig. [2][102]. Sometimes, and for convenience, we will also refer to constant solutions of the Eq. ( [3][101]), as periodic orbits.

**Fig. 2**

[image: Fig. 2]

[Full size image][103]

The Poincaré map

Similarly, as with the zeros of the polynomials, or analytic functions, the limit cycles of analytic DEs have associated a notion of multiplicity, which is nothing more than the multiplicity of the zero of the *displacement function*, \(\Delta (\rho )=\Pi (\rho )-\rho .\) There are limit cycles of multiplicity 1 (which are called hyperbolic), limit cycles of multiplicity 2, and so on. In this analytic setting, limit cycles of infinite multiplicity do not exist because they belong to a continuum of periodic solutions.

In next sections we will study the number of limit cycles of periodic non-autonomous linear, Riccati’s, and Abel’s equations.

### 3.1 Linear differential equations

We consider linear DEs, \(\dot{x}=a(t)+b(t)x,\) with *a*and *b*differentiable functions and \(2\pi\) -periodic. For example, the equation \(\dot{x}=2\sin t+x\sin t\) has all solutions periodic, but has no limit cycles. This is so because its solutions, with the initial condition \(x(0)=\rho\), are

$$\begin{aligned} x=\phi (t,\rho )=-2+(2+\rho )\textrm{e}^{1-\cos t}, \end{aligned}$$

and clearly all them are \(2\pi\) -periodic. We note that its Poincaré map is \(\Pi (\rho )\equiv \rho\). On the other hand, the equation \(\dot{x}=2\sin t -x\) has a single limit cycle. In this case, the solutions that satisfy \(x(0)=\rho\), are

$$\begin{aligned} x=\phi (t,\rho )=\sin t -\cos t+(1+\rho )\textrm{e}^{-t}. \end{aligned}$$

Then \(\Pi (\rho )=\rho\) gives us the equation \(-1+(1+\rho )\textrm{e}^{-2\pi }=\rho\), which has as a single solution \(\rho =-1\). Therefore, the limit cycle, which is unique and hyperbolic because \(\Pi '(-1)\ne 1,\) is \(\phi (t,-1)=\sin t-\cos t.\) In general, we have the following result.

### Lemma 3.3

Linear periodic differential equations have:

1. (i)

a continuum of periodic solutions; or

2. (ii)

no periodic solutions; or

3. (iii)

a single periodic solution, which is a hyperbolic limit cycle.

### Proof

Without loss of generality we can consider that the period of the DE is \(2\pi .\) Moreover, by Remark [3.2][104] we can restrict our attention to \(2\pi\) -periodic solutions. The solution of \(\dot{x}=a(t)+b(t)x,\) that satisfies \(x(0)=\rho\) is

$$\begin{aligned} x=\phi (t,\rho )=\left( \int _0^ta(s)\textrm{e}^{-B(s)}\,\textrm{d}s+\rho \,\right) \textrm{e}^{B(t)}, \end{aligned}$$

where \(B(s)=\int _0^s b(w)\,\textrm{d}w.\) Therefore the Poincaré map is

$$\begin{aligned} \Pi (\rho )=\phi (2\pi ,\rho )= m +n \rho , \end{aligned}$$

where

$$\begin{aligned} m=\textrm{e}^{B(2\pi )}\int _0^{2\pi }a(s)\textrm{e}^{-B(s)}\,\textrm{d}s\quad \text{ and } \quad n= \textrm{e}^{B(2\pi )}. \end{aligned}$$

The periodic orbits correspond to values of \(\rho\) that are solutions of equation \(\Pi (\rho )= \rho ,\) that in our case is the linear equation \(m+ n \rho = \rho .\) This equation has either a continuum of solutions, or zero, or one solution, depending on the values of *m*and *n*. Moreover, when a limit cycle exists, then it is hyperbolic, because it only happens when \(n\ne 1,\) and the derivative of the displacement function \(\Delta (\rho )=(n-1)\rho +m\) is \(\Delta '(\rho )\equiv n-1\ne 0.\) \(\square\)

Although linear differential equations are very simple they hide a very interesting dynamical property, the so-called *resonances*. In a few words, it is said that a *resonance*appears when a given equation has all its solutions bounded (for instance they are periodic) and when we add to it a periodic term then there appear unbounded solutions.

In most text books resonances are introduced for second order real linear DEs. Let us see that first order linear periodic DEs, but in the complex plane, do present resonances. For \(z\in {\mathbb {C}}\) consider the linear equation

$$\begin{aligned} \dot{z}= \textrm{i}z+a\textrm{i} \textrm{e}^{\textrm{i} \omega t}, \end{aligned}$$

where \(a,\omega \in {\mathbb {R}}\setminus \{0\}.\) Its solution satisfying \(\Phi (0,\rho )=\rho\) is

$$\begin{aligned} z=\phi (t,\rho )=\rho \textrm{e}^{\textrm{i}t}+ {\left\{ \begin{array}{ll} a\dfrac{\textrm{e}^{\textrm{i} \omega t}-\textrm{e}^{\textrm{i}t}}{\omega -1},\quad & \text{ when }\quad \omega \ne 1,\\ a\textrm{i} t\, \textrm{e}^{\textrm{i} t},& \text{ when }\quad \omega = 1. \end{array}\right. } \end{aligned}$$

Hence, when \(\omega \ne 1\) each solution of the differential equation is bounded, while when \(\omega =1\) all the solutions are unbounded. What happens when the period of the non-autonomous part is different to the period of the solutions of the linear autonomous part \(\dot{z}=\textrm{i}z\) (which is \(2\pi\)), is that there are no resonances. On the other hand, when \(\omega =1,\) the periods (or the frequencies of oscillation) coincide and then a resonance appears. These resonances also happen in non-linear DEs. For a survey on the subject, see for instance [[104][105], [109][106]] and their references. Resonances are very important in applications, like for instance in the study of many mechanical or electrical models.

### 3.2 Riccati’s differential equations

The differential equation

$$\begin{aligned} \dot{x} +a x^2=b t^\alpha , \end{aligned}$$

where *a*, *b*and \(\alpha\) are real parameters was studied by Riccati in 1723, although in fact individual cases of that equation were examined earlier by Daniel Bernoulli. D’Alembert was the first to baptize with the name of Riccati the general quadratic differential equations of the form

$$\begin{aligned} \dot{x}=a(t)+b(t)x+c(t)x^2, \end{aligned}$$

in a 1769 letter to Lagrange. Before the Riccati type equations were referred to the equations studied by Count Riccati.

A perhaps not sufficiently known result, but in fact remarkable, is that the study of a Riccati’s equation was one of the key tools in the famous work [[15][107]] of D. Bernoulli. In that work he studied the effects of vaccination in the treatment of the smallpox and, nowadays, it is considered as the beginning of Epidemiology. More specifically, Bernoulli studied the equation

$$\begin{aligned} \dot{x}= \left( \frac{n'(t)}{n(t)}-p \right) x+\frac{p}{m\, n(t)} x^2, \end{aligned}$$

where *n*(*t*) is the number of living people with age *t*, *x*(*t*) is the number of people prone to contracting smallpox at age *t*, *p*is the probability of that a prone individual contracts the disease, and 1/*m*the proportion of those who die for smallpox, see also [[49][108]]. In fact, nowadays, Riccati’s equations also appear in some papers that study the speed of certain infectious diseases, see for example [[114][109]]. These DEs also appear in many other situations, like for instance in geometrical problems, where Sotomayor and his coauthors study the number of isolated and closed principal curvature lines on canal surfaces, see [[57][110]], or in the study of some pendulum-like DEs, see [[110][111]].

[image: figure b]

The periodic Riccati’s equations write as

$$\begin{aligned} \dot{x}=a(t)+b(t)x+c(t)x^2, \end{aligned}$$

(4)

where *a*, *b*, and *c*are differentiable and \(2\pi\) -periodic functions. Recall that it is not restrictive to fix the period of the DE to be \(2\pi .\) Moreover, by Remark [3.2][104] we can restrict our attention to periodic solutions to the \(2\pi\) -periodic ones.

It is easy to construct examples of Riccati’s equations with exactly two limit cycles. Consider the equation

$$\begin{aligned} \dot{x}=1+\sin t +\cos t-\cos ^2t -(1+2\sin t)x+x^2, \end{aligned}$$

that has the two periodic solutions \(x=\sin t\) and \(x=1+\sin t.\) To prove the assertion, we compute the solutions of the DE satisfying \(x(0)=\rho\). We arrive at

$$\begin{aligned} x=\phi (t,\rho )=\sin t+ \frac{\rho }{\rho +(1-\rho )\textrm{e}^t}. \end{aligned}$$

The limit cycles are obtained by imposing that \(\Pi (\rho )=\phi (2\pi ,\rho )=\rho\). This equation is equivalent to \(\rho =\rho (\rho +(1-\rho )\textrm{e}^{2\pi })\), which has only two solutions, \(\rho =0\) and \(\rho =1\). These values are the initial conditions of the two limit cycles given above.

We will see below a simple and well-known proof that this is the maximum number of limit cycles that they can have in general.

### Proposition 3.4

Periodic Riccati’s differential equations ( [4][112]) have:

1. (i)

a continuum of periodic solutions; or

2. (ii)

no periodic solutions; or

3. (iii)

a single periodic solution, that can be a hyperbolic or a double limit cycle; or

4. (iv)

two periodic solutions, that are both hyperbolic with opposite stabilities.

### Proof

If they do not have a periodic orbit, we are done. Suppose they have one, \(x=x_0(t)\). Then doing the change of variables

$$\begin{aligned} y=\frac{1}{x-x_0(t)}, \end{aligned}$$

the Eq. ( [4][112]) is written as

$$\begin{aligned} \dot{y}=-c(t)-(2c(t)x_0(t)+b(t))y, \end{aligned}$$

which is a linear equation and can be solved explicitly. Calculating its solutions, and undoing the change of variables that we have done, we obtain that the solution of ( [4][112]) satisfying \(x(0)=\rho\) is

$$\begin{aligned} x=\phi (t,\rho )=\frac{M(t)+N(t)\rho }{P(t)+Q(t)\rho }, \end{aligned}$$

(5)

for certain functions *M*, *N*, *P*, *Q*that depend on *a*, *b*, *c*, and \(x_0\).

So the Poincaré map is

$$\begin{aligned} \Pi (\rho )=\frac{M(2\pi )+N(2\pi )\rho }{P(2\pi )+Q(2\pi )\rho }=\frac{m+n\rho }{p+q\rho }, \end{aligned}$$

with \(m,n,p\,\,\text{ and }\,\,q\) real numbers. Then, the periodic orbits correspond to the values of \(\rho\) that satisfy \(\Pi (\rho )= \rho ,\) and such that \(\phi (t,\rho )\) is defined for all \(t\in {\mathbb {R}}.\) This equation is

$$\begin{aligned} \frac{m+n\rho }{p+q\rho }=\rho \end{aligned}$$

and it has either zero, one, two, or a continuum of solutions, according to the parameter values. Moreover all the assertions about the multiplicities of the limit cycles follow because they coincide with the multiplicities of the zeroes of the displacement function, which is a quadratic equation in \(\rho .\)

To end the proof it only remains to make some comments about the set where the map \(\Pi\) is defined and to show the existence of examples with all the described possibilities.

First, notice that sometimes \(\Pi\) is not defined on the whole real line because some of the solutions can blow up to infinity and are such that its interval of definition is smaller than \([0,2\pi ].\) In any case, \(\Pi\) is defined in a single open interval and in this interval the map has at most two isolated fixed points, taking into account their multiplicities. They give rise to the limit cycles of the statement, with their corresponding multiplicities.

Finally, we include several examples of Riccati’s equations showing that all the possibilities given in the statement are realizable.

Consider the Riccati’s equation

$$\begin{aligned} \dot{x}= \cos t+P(x-\sin t), \end{aligned}$$

(6)

where *P*is a quadratic polynomial. It is easy to see that its only periodic solutions are \(x= y^*+\sin t,\) where \(y^*\) are the zeroes of \(P(y)=0\) and moreover that the corresponding multiplicities coincide. This is so, because the change of variable \(y=x-\sin t\) transforms ( [6][113]) into \(\dot{y}=P(y),\) and the unique solutions of this autonomous DE satisfying \(y(0)=y(2\pi )\) are \(y(t)\equiv y^*.\)

Therefore we have constructed examples of all the situations of the statement, but the one of a single hyperbolic limit cycle, because in the previous construction if *P*has a single real zero it is double and gives rise to a double limit cycle. To this end consider the Riccati’s equation

$$\begin{aligned} \dot{x}= & 2\cos t - \big (\sin t +\cos t \big )\cos ^2 t\\ & + \big (1-2(\sin t +\cos t )\sin t \big ) x+ (\sin t +\cos t) x ^{2}. \end{aligned}$$

Since \(x=\sin t\) is a particular solution, the general solution with initial condition \(x(0)=\rho\) can be easily obtained and it is

$$\begin{aligned} x=\phi (t,\rho )={\frac{ {\textrm{e}^{-t}}\sin t+\rho \,\cos ^2 t}{\textrm{e}^{-t}-\rho \sin t}}. \end{aligned}$$

Hence, its Poincaré map is \(\Pi (\rho )=\phi (2\pi ,\rho )=\textrm{e}^{2\pi }\rho\) and the Riccati’s equation has only one limit cycle, the one corresponding to \(\rho =0,\) that is precisely \(x=\sin t,\) which is hyperbolic because \(\Pi '(0)\ne 1.\) \(\square\)

Although Riccati’s equations seem fully understood, there is still a problem regarding them that is not resolved. It consists on determining, only in terms of *a*, *b*, and *c*, which of the four options in the proposition is the one that happens. This is not difficult to do when some explicit solution is known, see for instance [[35][114]]. This question and other open problems about Riccati’s and Abel’s equations are collected in [[62][115], Sec. 2.4].

It is also interesting to note that the Poincaré map for Riccati’s equations is a *homography*or, also called, a *Möbius transformation*. Later, we will come back to this point.

Riccati’s equations, not necessarily periodic, are also related with the study of planar linear non-autonomous DEs. More concretely, if we consider the planar differential system

$$\begin{aligned} \left( \begin{array}{ll}\dot{u}\\ \dot{v} \end{array}\right) = \left( \begin{array}{ll} p(t)& q(t)\\ r(t)& s(t) \end{array} \right) \left( \begin{array}{ll}u\\ v \end{array}\right) , \end{aligned}$$

(7)

and we define \(x=u/v\), then easy computations give that

$$\begin{aligned} \dot{x}=q(t)+\big (p(t)-s(t)\big )x -r(t)x^2. \end{aligned}$$

This property if often used in the study of Abelian integrals of the form \(M(h)= \alpha u(h)+\beta v(h),\) because the functions *u*(*h*) and *v*(*h*) usually satisfy the so called Picard-Fuchs differential equations, which are of the form ( [7][116]) with \(t=h\) being the energy of the unperturbed system, see for instance [[120][40], p. 171]. For more details about Abelian integrals and their relation with the Hilbert’s 16th problem, see [[33][89], Part II].

Although we will not consider these situations in this paper, Riccati differential equations have also been studied when \(x\in {\mathbb {C}}\), see for instance [[22][117], [23][118], [101][119], [108][120], [131][121]] or even for *x*being quaternionic-valued functions, see [[132][122]].

In fact, there is also a version of Riccati’s differential equations,

$$\begin{aligned} \dot{X}+XA(t)+D(t)X+XB(t)X-C(t)=0, \end{aligned}$$

where *X*, *A*, *B*, *C*and *D*are square matrices, that appear for instance in control system theory, see [[16][123]].

### 3.3 Abel’s differential equations

In this subsection we will consider Abel’s equations,

$$\begin{aligned} \dot{x}=a(t)+b(t)x+c(t)x^2+d(t)x^3,\end{aligned}$$

(8)

with *a*, *b*, *c*, and *d*differentiable and \(2\pi\) -periodic functions. Before starting to study them, we cannot fail to comment on the importance of the work of the eminent Norwegian mathematician Niels Henrik Abel, done in a very short period of time. An easily accessible paper where many of his contributions are explained is [[84][124]]. Briefly we will say that some of the subjects he studied were: series, functional and algebraic equations, integral equations, and elliptic and hyperelliptic integrals. Riccati’s and what nowadays we call Abel’s equations were studied by him in [[1][125], Chap. IV and V]. More specifically, in Chapter V, Abel studied the integrability of the equation

$$\begin{aligned} \big (y+s(t)\big )\frac{\textrm{d}y}{\textrm{d}t}=-d(t)-c(t)y-b(t)y^2. \end{aligned}$$

When \(s(t)\equiv 0,\) with the variable change \(x=1/y\), this equation is transformed into ( [8][126]) with \(a(t)\equiv 0.\) In general, making the change \(x=1/(y+s(t))\) we reach a similar result. It seems that Kamke, in his famous book on integrability, was the first who gave the name *Abel equation*to the Eq. ( [8][126]) when presented the results of Abel (1881), Liouville (1886), and Appell (1889) on the subject, see [[27][127], [90][128]].

[image: figure c]

As in the case of Riccati’s equations, Abel’s equations often appear in various areas of the science. See for example the works [[14][129], [55][130], [81][131], [138][132]] dealing with models of Ecology, Control Theory for electrical circuits, and Cosmology, respectively.

At this point, no one will be surprised by the assertion that there are equations of Abel’s type with three limit cycles. This is very true, of course, but these equations hold a surprise.

### Theorem 3.5

(Lins-Neto, [[97][133]]) For any \(k\in {\mathbb {N}}\) there is a \(2\pi\) -periodic Abel’s differential equation ( [8][126]) that has at least *k*limit cycles, all of them hyperbolic.

We will give the main ideas of the proof of this result and others properties of Abel’s equations in the next section.

## 4 Some results on Abel’s equations

We will divide this section into two parts. In the first one we will enunciate and prove some results that give, with certain additional hypotheses, upper bounds for the number of limit cycles for Abel’s equations ( [8][126]) and in the second one we will focus on the proof of Theorem [3.5][134].

### 4.1 Results that bound the number of limit cycles for Abel’s differential equations

One of the main differences between Riccati’s or linear equations and Abel’s equations is that, for the latter, neither the flow nor the explicitly associated Poincaré map, \(\Pi ,\) can be found. Fortunately, there is a result of Lloyd [[102][135]] which gives us a very useful expression that relates \(\Pi ',\Pi '',\) and \(\Pi '''\).

### Proposition 4.1

(Lloyd, [[102][135]]) Consider a non-autonomous \(2\pi\) -periodic differential equation ( [3][101]), with *f*of class \({\mathcal {C}}^3\). If \(\Pi\) is its associated Poincaré map, then

$$\begin{aligned} \Pi '(\rho )&=\exp \left( \int _0^{2\pi }\dfrac{\partial }{\partial x}f(t,\phi (t,\rho ))\,\textrm{d}t\right) ,\\ \Pi ''(\rho )&=\Pi '(\rho )\Bigg [ \int _0^{2\pi }\!\!\!\dfrac{\partial ^2 }{\partial x^2}f(t,\phi (t,\rho )) \exp \left( \int _0^{t}\dfrac{\partial }{\partial x}f(s,\phi (s,\rho ))\,\textrm{d}s\right) \textrm{d}t\Bigg ],\\ \Pi '''(\rho )&=\Pi '(\rho )\!\Bigg [\dfrac{3}{2}{\left( \dfrac{\Pi ''(\rho )}{\Pi '(\rho )} \right) }^2\\ &\qquad \qquad + \int _0^{2\pi }\!\!\!\dfrac{\partial ^3 }{\partial x^3}f(t,\phi (t,\rho )) \exp \left( 2\! \int _0^{t}\dfrac{\partial }{\partial x}f(s,\phi (s,\rho ))\,\textrm{d}s\right) \textrm{d}t\Bigg ], \end{aligned}$$

where \(\phi (t,\rho )\) is the solution of ( [3][101]) that satisfies \(\phi (0,\rho )=\rho\).

### Proof

Since \(x=\phi (t,\rho )\) is the solution of ( [3][101]), it holds that

$$\begin{aligned} \frac{\partial }{\partial t} \phi (t,\rho )=f(t,\phi (t,\rho )),\quad \phi (0,\rho )=\rho . \end{aligned}$$

Deriving with respect to \(\rho\) and using the Schwarz rule we have that

$$\begin{aligned} \frac{\partial }{\partial t} \phi '(t,\rho )= \frac{\partial }{\partial x}f(t,\phi (t,\rho ))\,\phi '(t,\rho ), \end{aligned}$$

where for simplicity we use the notation

$$\begin{aligned} \frac{\partial }{\partial \rho }\phi (t,\rho )=\phi '(t,\rho ),\quad \frac{\partial ^2}{\partial \rho ^2}\phi (t,\rho )=\phi ''(t,\rho )\quad \text{ and }\quad \frac{\partial ^3}{\partial \rho ^3}\phi (t,\rho )=\phi '''(t,\rho ).\end{aligned}$$

Therefore,

$$\begin{aligned} \phi '(t,\rho )=\exp \left( \int _0^t \frac{\partial }{\partial x} f(s,\phi (s,\rho ))\,\textrm{d}s\right) , \end{aligned}$$

(9)

and, moreover,

$$\begin{aligned}\frac{\partial }{\partial t}\ln \left( \phi '(t,\rho )\right) =\frac{\partial }{\partial x} f(t,\phi (t,\rho )).\end{aligned}$$

Deriving this equality with respect to \(\rho\) and by using again the Schwarz rule we get

$$\begin{aligned} \frac{\partial }{\partial t}\left( \frac{\phi ''(t,\rho )}{\phi '(t,\rho )}\right) =\frac{\partial ^2}{\partial x^2} f(t,\phi (t,\rho ))\,\phi '(t,\rho ). \end{aligned}$$

(10)

Integrating ( [10][136]), we arrive at

$$\begin{aligned} \frac{\phi ''(t,\rho )}{\phi '(t,\rho )} =\int _0^t\frac{\partial ^2}{\partial x^2} f(s,\phi (s,\rho ))\,\phi '(s,\rho )\,\textrm{d}s. \end{aligned}$$

Since \(\Pi (\rho )=\phi (2\pi ,\rho ),\) substituting \(t=2\pi\) into the above formula and using ( [9][137]), we obtain the expression for \(\Pi ''(\rho )\) given in the statement.

Making one more derivation of ( [10][136]), with respect to \(\rho\), we obtain

$$\begin{aligned}&\frac{\partial }{\partial t}\left( \frac{\phi '''(t,\rho )\phi '(t,\rho )-\phi ''(t ,\rho )^2}{\phi '(t,\rho )^2}\right) \\&\qquad =\frac{\partial ^3}{\partial x^3} f(t,\phi (t,\rho ))\,\phi '(t,\rho )^2+ \frac{\partial ^2}{\partial x^2} f(t,\phi (t,\rho ))\,\phi ''(t,\rho )\\&\qquad =\frac{\partial ^3}{\partial x^3} f(t,\phi (t,\rho ))\,\phi '(t,\rho )^2+\frac{\phi '' (t,\rho )}{\phi '(t,\rho )}\frac{\partial }{\partial t}\left( \frac{\phi ''(t,\rho )}{\phi ' (t,\rho )}\right) \\&\qquad =\frac{\partial ^3}{\partial x^3} f(t,\phi (t,\rho ))\,\phi '(t,\rho )^2+\frac{1}{2}\frac{\partial }{\partial t}\left( \left( \frac{\phi ''(t,\rho )}{\phi '(t,\rho )}\right) ^2\right) . \end{aligned}$$

So

$$\begin{aligned} & \frac{\partial }{\partial t}\left( \frac{\phi '''(t,\rho )\phi '(t,\rho )-\phi ''(t,\rho )^2}{\phi '(t,\rho )^2}-\frac{1}{2} \left. \quad \left( \frac{\phi ''(t,\rho )}{\phi '(t,\rho )}\right) ^2\right) \right. \\ & =\frac{\partial ^3}{\partial x^3} f(t,\phi (t,\rho ))\,\phi '(t,\rho )^2, \end{aligned}$$

from which we deduce that

$$\begin{aligned} \frac{\phi '''(t,\rho )}{\phi '(t,\rho )}-\frac{3}{2}\left( \frac{\phi ''(t,\rho )}{\phi ' (t,\rho )}\right) ^2 =\int _0^t\frac{\partial ^3}{\partial x^3} f(s,\phi (s,\rho ))\,\phi '(s,\rho )^2\,\textrm{d}s. \end{aligned}$$

Substituting \(t=2\pi\) into the previous formula and using again ( [9][137]), we get the desired expression for \(\Pi '''(\rho ).\) \(\square\)

Applying Proposition [4.1][138] we can give for Abel’s equations a similar result to Lemma [3.3][139] and Proposition [3.4][140], but adding an additional hypothesis. This result was proved in [[113][100]], long before the previous proposition. We will also include the original proof and compare it with the one based on Proposition [4.1][138].

### Theorem 4.2

(Pliss, [[113][100]]) The periodic Abel’s differential equation ( [8][126]), with \(d(t)>0\), has:

1. (i)

no periodic solution, or

2. (ii)

one, two, or three limit cycles.

### Proof using Lloyd’s formula

We will use Proposition [4.1][138]. First we note that for our Abel’s equation,

$$\begin{aligned} \frac{\partial ^3 f}{\partial x^3}(t,\phi (t,\rho ))=6 d(t)>0. \end{aligned}$$

Therefore, since in addition \(\Pi '(\rho )>0\), we have that \(\Pi '''(\rho )>0.\) Now suppose, to reach contradiction, that the DE had at least four periodic solutions. Then the displacement function \(\Delta (\rho )=\Pi (\rho )-\rho\), would have at least four zeros and it would be well defined only on an open interval, \({\mathcal {I}}\), containing them all. Applying three times the Rolle’s theorem we would conclude that \(\Delta ', \Delta '',\) and \(\Delta '''\) would have at least 3, 2, and 1 zeroes, respectively, all contained in the same interval \({\mathcal {I}}\). Since \(\Delta '''(\rho )=\Pi '''(\rho )>0\), we have reached the desired contradiction. Therefore, the Abel’s equation with \(d(t)>0\) will have at most three periodic orbits and, if they exist, they must be hyperbolic limit cycles. \(\square\)

### Original proof of Pliss of Theorem 4.2

Suppose, in order to reach contradiction, that the Abel’s equation ( [8][126]) has four \(2\pi\) -periodic solutions, \(x_1(t)<x_2(t)<x_3(t)<x_4(t)\) and consider the positive function

$$\begin{aligned} H(t):=\frac{(x_4(t)-x_1(t))(x_3(t)-x_2(t)) }{(x_3(t)-x_1(t))(x_4(t)- x_2(t)) }. \end{aligned}$$

(11)

This function, for each *t*, gives us the double ratio between the four points \(x_i(t)\), \(i=1,\ldots ,4.\) Calculating, we get that

$$\begin{aligned} \frac{\textrm{d}(\ln (H(t))}{\textrm{d}t}=-d(t) {(x_4(t)-x_3(t))(x_2(t)-x_1(t)) }<0. \end{aligned}$$

(12)

On the other hand,

$$\begin{aligned} \int _0^{2\pi }\frac{\textrm{d}(\ln (H(t))}{\textrm{d}t}\,\textrm{d}t=\ln (H(2\pi ))-\ln (H(0))=0, \end{aligned}$$

since the function *H*is \(2\pi\) -periodic, thus reaching the desired contradiction. Therefore the DE has at most three limit cycles as we wanted to demonstrate. \(\square\)

There are several related results that impose conditions involving the functions *a*, *b*, *c*, *d*of the Abel’s equation to get an upper bound for its number of limit cycles, see for instance [[4][141], [19][142], [66][143], [69][144]]

### Remark 4.3

(i) The two proofs of Theorem [4.2][145] presented can also be adapted to the case where *d*(*t*) does not change sign and vanishes only at isolated points. The case \(d(t)\le 0\) can be reduced to the case \(d(t)\ge 0,\) making the time change \(t\rightarrow 2\pi -t.\)

(ii) Theorem [4.2][145] could also be slightly improved by saying that when *d*(*t*) does not change sign and vanishes only at isolated points, the sum of the multiplicities of all the limit cycles of Abel’s equation is at most 3. This result is a direct consequence of the proof based on Lloyd’s formula, but it cannot be obtained from the proof of Pliss.

(iii) Another advantage of the proof based on Lloyd’s formula is that it easily extends to general periodic DEs, \(\dot{x}=f(t,x),\) not necessarily of Abel’s type, satisfying that \(\frac{\partial ^3 f}{\partial x^3}(t,\phi (t,\rho ))\) does not change sign. In this way we recover for instance the results of [[8][146]].

(iv) Examples of Abel’s equations having between 0 to 3 limit cycles, taking into account their multiplicities and with \(d=1\) can be easily constructed. It suffices to take in ( [6][113]) a monic polynomial *P*of degree 3.

Although the two given proofs are different in appearance, let us see that, in essence, they are very similar. We need to remember the so-called *divided differences*, which are normally used for the effective calculation of interpolating polynomials.

Given a function \(g:{\mathbb {R}}\rightarrow {\mathbb {R}}\) and \(x_1,x_2,\ldots , x_n\) different real numbers, we write \(g_j:=g(x_j)\) and define recursively,

$$\begin{aligned} g_{i_1,i_2,\ldots ,i_{n-1}, i_n}:=\frac{g_{i_2,\ldots ,i_{n-1},i_n}-g_{i_1,i_2,\ldots , i_{n-1}}}{x_{i_n}-x_{i_1}}. \end{aligned}$$

These differences satisfy

$$\begin{aligned} g_{i_1,i_2,\ldots , i_n}=g_{\sigma (i_1),\sigma (i_2),\ldots , \sigma (i_n)}, \end{aligned}$$

where \(\sigma\) is any permutation. Also, when *g*is of class \({\mathcal {C}}^{n-1}\),

$$\begin{aligned} g_{i_1,i_2,\ldots ,i_{n-1}, i_n}=\frac{1}{(n-1)!}\,g^{(n-1)}(\xi ), \end{aligned}$$

(13)

where \(\xi\) is a number that belongs to the interval formed by the points \(x_1,x_2,\ldots , x_n\), see [[89][147]]. Note that when \(n=2\), the expression ( [13][148]) is precisely the mean value theorem.

If we take the Abel’s equation

$$\begin{aligned}\dot{x}=a(t)+b(t)x+c(t)x^2+d(t)x^3:=f(t,x), \end{aligned}$$

and, following Pliss, we take four solutions \(x_1(t)<x_2(t)<x_3(t)<x_4(t)\), we have that

$$\begin{aligned} \frac{\textrm{d}(\ln (H(t))}{\textrm{d}t}&=\frac{f(t,x_4(t))- f(t,x_1(t))}{x_4(t)-x_1( t)}+ \frac{f(t,x_3(t))- f(t,x_2(t))}{x_3(t)-x_2(t)}\\&\quad -\frac{f(t,x_3(t))- f(t,x_1(t))}{x_3(t)-x_1(t)}- \frac{f(t,x_4(t))- f(t,x_2(t))}{x_4(t)-x_2(t)}, \end{aligned}$$

where *H*is given by ( [11][149]). Fix *t*, and to simplify notation, we write \(x_j=x_j(t)\) and we introduce \(g(x_j):=f(t,x_j(t))\). Then, using the above expression, the divided difference notation and its properties, we have

$$\begin{aligned} \frac{\textrm{d}(\ln (H(t))}{\textrm{d}t}&= g_{4,1}+g_{3,2}-g_{3,1}-g_{4,2}= (g_{4,1}-g_{2,4})+(g_{3,2}-g_{1,3})\\ &= g_{2,4,1}(x_1-x_2)+g_{1,3,2}(x_2-x_1)= (g_{1,2,4}-g_{3,1,2})(x_1-x_2)\\ &=g_{3,1,2,4}(x_4-x_3)(x_1-x_2)= -\frac{1}{3!}g'''(\xi )(x_4-x_3)(x_2-x_1)\\ &=-\frac{1}{6} \frac{\partial ^3 f(t,\xi (t))}{\partial x^3} {(x_4(t)-x_3(t))(x_2(t)-x_1(t)) }. \end{aligned}$$

In summary, what we have seen is that the method proposed by Pliss works because \(\frac{\textrm{d}(\ln (H(t))}{\textrm{d}t}\) does not vanish, while the proof based on Lloyd’s formula does so because the same thing happens with \(\frac{\partial ^3 f(t,x)}{\partial x^3}\). Notice that, for Abel’s equations, the two conditions coincide. This idea for proving the “equivalence” between both approaches is inspired on some of the reasoning developed in [[41][150]].

Another promising method to obtain upper bounds for the limit cycles of planar DEs is the use of the Bendixson–Dulac criterion, see [[64][96]] and their references. For the particular case of Abel’s equations it has been seldom used, see for instance [[4][141]].

To conclude this section we will see what consequences we can draw when we apply the results obtained to the Riccati’s equations.

Applying ( [12][151]), since \(d(t)\equiv 0\), we obtain that *H*(*t*) is constant. Hence, given any four solutions of a Riccati’s equation \(x_1(t)<x_2(t)<x_3(t)<x_4(t),\) there exists a constant *K*such that

$$\begin{aligned} \frac{(x_4(t)-x_1(t))(x_3(t)-x_2(t)) }{(x_3(t)-x_1(t))(x_4(t)-x_2(t)) } =K. \end{aligned}$$

(14)

This classic result implies that if three solutions of a Riccati’s equation are known, any other solution can be obtained from these three. In fact, equality ( [14][152]) was surely the one that inspired Pliss for the method that he used for proving his result on Abel’s equations.

Let us see now what Lloyd’s result tells us when we apply it to Riccati’s equations. Applying Proposition [4.1][138] we obtain that the Poincaré map satisfies

$$\begin{aligned} \Pi '''(\rho )=\frac{3}{2} \left( \frac{\Pi ''(\rho )}{\Pi '(\rho )}\right) ^2\!\Pi '(\rho ) \quad \Longleftrightarrow \quad \Pi '''(\rho )=\frac{3}{2} \frac{\left( \Pi ''(\rho )\right) ^2}{\Pi '(\rho )}. \end{aligned}$$

(15)

This differential equation, which by the way is called the *Kummer–Schwarz differential equation,*is very easy to solve and its solutions are precisely the homographies, giving a new proof of the result that appears in the proof of Proposition [3.4][140].

One of the known properties of homographies is that they preserve the double ratio. Remember that fixed *t*, the flow of a Riccati’s equation, \(\phi (t,\rho )\) given in ( [5][153]), is always a homography. Putting both properties together we get a new proof of equality ( [14][152]).

The DE ( [15][154]) can also be written as

$$\begin{aligned} {\mathcal {S}}(\Pi )(\rho ):=\frac{ \Pi '''(\rho )}{\Pi '(\rho )}-\frac{3}{2}{\left( \frac{\Pi ''(\rho )}{\Pi '(\rho )}\right) }^2 \equiv 0.\end{aligned}$$

The operator \({\mathcal {S}}(\Pi )\) is called the *Schwarzian derivative*of \(\Pi\) and plays an important role in complex analysis ( [[82][155]]), in the study of one-dimensional real discrete dynamic systems ( [[105][156]]), or in the study of the limit cycles of certain non-smooth DEs ( [[40][157]]). It was introduced by Hermann Schwarz in 1869, see [[82][155], Chap. 10].

In fact, it is well known that the only meromorphic functions that have zero Schwarzian derivative are the homographies ( [[82][155]]), finding once again the result which characterizes Poincaré maps of Riccati’s equations.

### 4.2 Abel’s differential equations with many limit cycles

In this section we will give the main ideas of the proof of Theorem [3.5][134]. As a corollary, we will see that Theorem [4.2][145] cannot be extended for equations of Abel’s type with “degree” greater than 3. We will also recall a result of [[66][143]], which shows us that for Abel’s type equations it is not easy to know whether its number of limit cycles is bounded or not. Following [[42][158]], we will also state similar results on limit cycles for non-differentiable DEs. Finally, we will comment on how the obtained result can be extended to difference equations of Riccati’s or Abel’s type, see [[18][159]].

### Proof of Theorem 3.5

We start with a simple \(2\pi\) -periodic Riccati’s equation

$$\begin{aligned} \dot{x}=c(t)x^2.\end{aligned}$$

(16)

Their solutions \(x=\phi _0(t,\rho )\) satisfying \(\phi _0(0,\rho )=\rho\) are

$$\begin{aligned} x=\phi _0(t,\rho )=\frac{\rho }{1-\rho C(t)}, \quad \text{ where }\quad C(t)=\int _0^t c(s)\, \textrm{d} s. \end{aligned}$$

Imposing that \(C(2\pi )=0\), we obtain that near \(\rho =0\) the DE has a continuum of periodic solutions. In fact, if \(\overline{C}:=\max _{t\in [0,2\pi ]}|C(t)|\), for \(|\rho |<1/\overline{C},\) the solutions of the DE are \(2\pi\) -periodic because \(\phi _0(2\pi ,\rho )\equiv \rho .\)

In order to obtain an Abel’s equation with at least *k*limit cycles, and following *Poincaré’s perturbation method*, we perturb ( [16][160]) as follows

$$\begin{aligned} \dot{x}=c(t)x^2+\varepsilon d(t)x^3,\end{aligned}$$

(17)

where \(\varepsilon\) is a small parameter. Then, by the smooth dependence theorems on parameters and initial conditions, the solutions of this new DE can be expressed as

$$\begin{aligned} \phi (t,\rho ,\varepsilon ) = \phi _0(t,\rho )+ \psi (t,\rho )\varepsilon + O(\varepsilon ^2). \end{aligned}$$

Let us calculate \(\psi (t,\rho )=\left. \frac{\partial \phi (t,\rho ,\varepsilon )}{\partial \varepsilon }\right| _{\varepsilon =0}\). For simplicity, we write \(\phi (t,\rho ,\varepsilon )= \phi = \phi _0+ \psi \varepsilon + O(\varepsilon ^2),\) \(c=c(t)\) and \(d=d(t)\). We have that

$$\begin{aligned} \frac{\partial }{\partial \,t}\left( \phi _0+ \psi \varepsilon + O(\varepsilon ^2)\right)&=c\left( \phi _0+ \psi \varepsilon + O(\varepsilon ^2)\right) ^2+\varepsilon d\left( \phi _0+ \psi \varepsilon + O(\varepsilon ^2)\right) ^3\\&=c\big (\phi _0^2+ 2\phi _0\psi \varepsilon +O(\varepsilon ^2)\big ) +\varepsilon d\big (\phi _0^3+ O(\varepsilon )\big )\\&=c\phi _0^2+\left( 2c\phi _0\psi +d\phi _0^3\right) \varepsilon +O(\varepsilon ^2). \end{aligned}$$

Therefore \(\psi '=2c\phi _0\psi +d\phi _0^3,\) where \(\psi '=\partial \psi (t,\rho )/\partial t\). Using that \(\phi _0\) is solution of ( [16][160]), this DE is written as \(\psi '=2\phi _0'\psi /\phi _0+d\phi _0^3\) or, equivalently, as \(\left( {\psi }/{\phi _0^2}\right) '= d\phi _0.\) Solving this DE we have

$$\begin{aligned} \psi (t,\rho )=\phi _0(t,\rho )^2\int _0^t d(s)\phi _0(s,\rho )\,\textrm{d}s=\phi _0(t,\rho )^2 \int _0^t \frac{\rho d(s)}{1-\rho C(s)}\,\textrm{d}s. \end{aligned}$$

Recall that the solution starting at \(\rho\) is a limit cycle of the perturbed DE if it is an isolated solution of \(\Delta (\rho ,\varepsilon ):=\phi (2\pi ,\rho ,\varepsilon )-\rho =0.\) For \(|\rho |<1/\overline{C},\) since \(\phi _0(2\pi ,\rho )\equiv \rho ,\) this equation writes as

$$\begin{aligned} \Delta (\rho ,\varepsilon )= \varepsilon \rho ^3\int _0^{2\pi } \frac{d(t)}{1-\rho C(t)}\, \textrm{d}t+O(\varepsilon ^2)=0. \end{aligned}$$

The function

$$\begin{aligned} M(\rho ):= \int _0^{2\pi }\frac{d(t)}{1-\rho C(t)}\,\textrm{d}t\end{aligned}$$

is known as the *Melnikov‘s function*or *Pontryagin’s function*associated to the DE ( [17][161]). From the implicit function theorem applied to \(\Delta (\rho ,\varepsilon )/\varepsilon\) it follows that the not null simple zeros of *M*give rise, for any \(\varepsilon\) sufficiently small, to simple zeroes of the function \(\Delta\). More specifically, if \(\rho =\overline{\rho }\) is such that \(M(\overline{\rho })=0\) and \(M'(\overline{\rho })\ne 0,\) then there exists a differentiable function *g*such that \(g(0)=\overline{\rho }\) and, for \(\varepsilon\) small enough, \(\Delta (g(\varepsilon ),\varepsilon )\equiv 0\). Moreover, it is not difficult to see that the obtained limit cycles are hyperbolic.

In other words, what we have seen is that each one of the simple not null zeros of \(M(\rho )\) gives rise to a hyperbolic limit cycle of the corresponding Abel’s equation, for \(\varepsilon\) small enough. Therefore we have reduced the proof of the theorem to find functions *c*and *d*such that the corresponding function *M*has at least *k*not null simple zeroes.

For any \(k\in {\mathbb {N}}\), we take \(c(t)=\cos t\) and \(d(t)=P(\sin t)\), where *P*is a polynomial of degree *k*to be determined. Then, for \(\rho\) small enough,

$$\begin{aligned} M(\rho ):&= \int _0^{2\pi }\frac{P(\sin t)}{1-\rho \sin t}\,\textrm{d}t=\int _0^{2\pi }\sum _{m=0}^\infty \rho ^mP(\sin t)\sin ^m t\, \textrm{d}t \\&=\sum _{m=0}^{k} \Big (\int _0^{2\pi }P(\sin t)\sin ^m t\,dt\Big )\rho ^m+O\big (\rho ^{k+1}\big )=N(\rho )+O\big (\rho ^{k+1}\big ), \end{aligned}$$

where *N*is a polynomial in \(\rho\) of degree *k*. It is not difficult to see that, in fact, given any polynomial of degree *k*, \({\overline{N}}\), there exists a \({\overline{P}}\) such that its associated Melnikov function \({\overline{M}}\) satisfies \(\overline{M}(\rho )={\overline{N}}(\rho )+O\big (\rho ^{k+1}\big )\). This freedom to fix arbitrarily the first \(k+1\) terms of the Taylor series of *M*at the origin allows to construct a function with *k*non-null zeros and simple ones, as we wanted to show. To formalize a proof of this last assertion it suffices to notice that the proved property implies that the functions \([1,\rho ,\rho ^2,\ldots , \rho ^{k-1},\rho ^k+O(\rho ^{k+1})]\) form a complete Chebyshev system on the interval \((0,\delta ),\) for \(\delta\) small enough, see [[91][162]] for a complete monograph on Chebyshev systems. In fact, from the results of [[6][163], [68][164]] it is also known that \(M(\rho )\) has at most *k*zeros. \(\square\)

A corollary of the previous theorem shows us that for Abel’s type equations, with “degree” \(n>3,\) the number of limit cycles cannot be determined, even if the coefficient of \(x^n\) is positive. Therefore, Theorem [4.2][145] cannot be extended for \(n>3.\)

### Theorem 4.4

Given \(n\in {\mathbb {N}}\) with \(n>3,\) and any \(k\in {\mathbb {N}}\), there is a DE of the form

$$\begin{aligned}\dot{x}=a_0(t)+a_1(t)x+\cdots +a_{n-1}(t)x^{n-1}+a_n(t)x^n,\end{aligned}$$

with \(a_i(t), i=0,1,\ldots ,n,\) \(2\pi\) -periodic functions, and \(a_n(t)>0\) which has at least *k*limit cycles.

### Proof

Following the proof of Theorem [3.5][134] we know that, given any \(k\in {\mathbb {N}}\), there is an Abel equation of the form

$$\begin{aligned} \dot{x}=\cos t\, x^2+\varepsilon P(\sin t)x^3,\end{aligned}$$

with *P*a polynomial of degree *k*, and \(\varepsilon >0\), small enough, that has at least *k*limit cycles. Recall also that these limit cycles are hyperbolic, since they correspond to simple zeros of the displacement application \(\Delta\) associated to the DE. Therefore, they remain by small perturbations of the DE. So if we take the new equation

$$\begin{aligned} \dot{x}=(\cos t)\,x^2+\varepsilon P(\sin t )x^3+\delta x^n,\end{aligned}$$

with \(\delta >0,\) small enough, it also has at least *k*limit cycles and \(a_n(t)\equiv \delta >0\), as we wanted to prove. \(\square\)

The Abel equations or the Abel-type equations considered in Theorem [4.4][165] have been also studied in the complex, see for instance [[100][166], [133][167]].

The following result from [[66][143]], which can be proved similarly to Theorems [3.5][134] and [4.2][145], shows us how complicated Abel’s type equations can be. Part (i) is also proved in [[111][168]].

### Theorem 4.5

Consider the \(2\pi\) -periodic Abel-like differential equations

$$\begin{aligned} \dot{x}=a(t)+b(t)x +c(t) x^2 +x^n,\quad n\in {\mathbb {N}}. \end{aligned}$$

Then:

1. (i)

If \(n\ge 3\) is odd, they have at most 3 limit cycles.

2. (ii)

If \(n\ge 4\) is even, for any \(k\in {\mathbb {N}}\), there is a DE of this type that has at least *k*limit cycles.

For instance, the proof of item (*i*) is exactly the same that the proof for Abel’s equations because when \(n\ge 3\) is odd

$$\begin{aligned} \frac{\partial ^3}{\partial x^3}\big (a(t)+b(t)x +c(t) x^2 +x^n\big )=n(n-1)(n-2)x^{n-3}\ge 0 \end{aligned}$$

and by Proposition [4.1][138], the return map associated to this Abel’s like equation satisfies \(\Pi '''(\rho )>0.\)

All the above results in this section have been obtained by studying the zeroes of the first order Melnikov function. It is worth to comment that higher order Melnikov functions can be obtained for autonomous or non-autonomous DEs. For instance, in [[85][169]] the authors use a second order function to study same Abel’s like differential equations. More in general, the so-called *variational equations*are used in [[43][170]] or the *averaging theory*in [[99][171]] to get them.

To finish this section, we state a couple of results from [[21][172], [42][158], [75][173]] for piecewise linear non-autonomous DEs and we also make some comments about linear, Riccati’s, or Abel’s difference equations.

The first result for piecewise linear DEs is very surprising, specially when we compare it with the corresponding result for linear DEs given in Sect. [3.1][174].

### Theorem 4.6

[[21][172], [42][158]] For any \(k\in {\mathbb {N}}\), there is a piecewise linear differential equation of the form

$$\begin{aligned} \dot{x}=a(t)+b(t)|x|,\end{aligned}$$

(18)

with *a*and *b*trigonometric \(2\pi\) -periodic polynomials, which has at least *k*limit cycles.

The second result is similar to Pliss’ result for Abel’s equations because it covers the case where *b*does not change sign.

### Theorem 4.7

[[75][173]] If *b*does not change sign and *a*has finitely many zeros then the differential equation ( [18][175]) has at most two limit cycles.

Finally, we want to comment that similar results to Lemma [3.3][139], Proposition [3.4][140], and Theorem [3.5][134] for periodic linear, Riccati’s, or Abel’s non-autonomous difference equations also hold, see [[18][159]]. These results are proved in that paper treating both settings, the periodic DEs and the difference equations, under the unified point of view of time scales.

For instance, under this point of view, linear dynamic equations write as

$$\begin{aligned} x^{\Delta }=a(t)+b(t)x, \end{aligned}$$

Riccati’s dynamic equations as

$$\begin{aligned} x^{\Delta }=a(t)+b(t)x+c(t)x x^\sigma , \end{aligned}$$

and Abel’s dynamic equations as

$$\begin{aligned} x^{\Delta }=a(t)+b(t)x+c(t)x x^\sigma +d(t) x^2 x^\sigma , \end{aligned}$$

where the notations \(x^\Delta\) and \(x^\sigma\) are defined in the general theory of time scales. A particular case is when the time scale is \({\mathbb {T}}={\mathbb {R}},\) and then, \(x^\Delta = \dot{x}\) and \(x^\sigma =x,\) recovering the classical DEs. Another one, when \({\mathbb {T}}={\mathbb {N}}\) and then \(t=n,\) \(x(t)=x_n,\) \(x^\Delta (t)=x_{n+1}-x_n,\) and \(x^\sigma (t)=x_{n+1},\) giving rise to the difference equations, see again [[18][159]].

More specifically, the linear and Riccati’s periodic difference equation write respectively as

$$\begin{aligned} x_{n+1}= A_n+B_nx_n,\quad x_{n+1}= \frac{A_n+B_nx_n}{1+C_nx_n}, \end{aligned}$$

(19)

and the Abel’s periodic difference equation as

$$\begin{aligned} x_{n+1}= \frac{A_n+B_nx_n}{1+C_nx_n+D_nx_n^2}, \end{aligned}$$

(20)

for some *M*-periodic sequences \(A_n,B_n,C_n,\) and \(D_n.\) The commented results prove that linear (resp. Riccati’s ) *M*-periodic difference equations ( [19][176]) have either a continuum of periodic solutions, or at most 1 (resp. 2) *M*-periodic solutions, while there are *M*-periodic Abel’s difference equations ( [20][177]) having at least \(M-1\) isolated periodic solutions of period *M*.

With regard to real-world models it is curious to notice that the simplest interesting model for the evolution of a single population given by a DE is the so-called *logistic model*and it is given by a Riccati’s differential equation of the form \(\dot{x}= r x(1-x).\) Similarly, its discrete analogous is the Beverton-Holt’s model \(x_{n+1}= r x_n/(1+x_n/k).\) Observe that it is given by a Riccati’s difference equation. Both equations are easily solvable and their corresponding solutions can be obtained explicitly.

## 5 Some relations between Abel’s equations and Hilbert’s 16th problem

In this section we will study three families of autonomous planar polynomial DEs, the quadratic, the rigid ones, and a family of unbounded degree, for which the study of their limit cycles can be reduced to the study of some Abel’s like equations.

For periodic Abel’s equations a problem similar to the second part of Hilbert’s 16th problem can be posed

“Given the Abel’s family of differential equations

$$\begin{aligned} \dot{x}=bx+c_m(t)x^2+d_n(t)x^3, \end{aligned}$$

(21)

where \(b\in {\mathbb {R}}\) and \(c_m\) and \(d_n\) are \(2\pi\) -periodic trigonometric polynomials and homogeneous of degrees *m*and *n*, respectively, find out if there is a bound, \({\mathcal {A}}(m,n)\), for the number of limit cycles that ( [21][178]) can have."

Again, the existence of \({\mathcal {A}}(m,n)\) is no longer a simple problem to address. For example in [[36][179]] it is shown that, in a similar context but substituting \({\mathbb {R}}\) by \({\mathbb {C}}\), this number does not exist.

We denote as \({\mathcal {A}}_0(m,n)\) the value \({\mathcal {A}}(m,n)\) restricted to the case \(b=0\) in ( [21][178]). Following the proof of Theorem [3.5][134] it can be seen that \({\mathcal {A}}_0(1,n)\ge n+2,\) see [[6][163]]. In that paper it is also proved that \({\mathcal {A}}_0(m,1)\ge 2m+1.\) Both proofs use the first order Melnikov function associated to a perturbation of a DE with a continuum of periodic solutions. In [[85][169]] the study of a second order Melnikov function has been used to improve these lower bounds, showing that \({\mathcal {A}}_0(m,n)\ge 2(m+n)-1.\)

With a different approach based on computing a kind of Lyapunov quantities associated to the solution \(x=0,\) in the papers [[6][163], [85][169]] it is also proved for instance that \({\mathcal {A}}_0(1,3)\ge 7,\) \({\mathcal {A}}_0(2,2)\ge 7\), \({\mathcal {A}}_0(3,1)\ge 8\) or \({\mathcal {A}}_0(1,4)\ge 10\).

In the very recent paper [[135][180]] the authors prove that \({\mathcal {A}}_0(1,1)=3,\) solving Problem 6 of the list of open problems proposed in [[62][115]].

We will prove the following well-known result, which is a consequence of the works of Cherkas [[29][98]] and Lins-Neto [[97][133]]. See also [[45][32]].

### Theorem 5.1

It holds that \({\mathcal {H}}(2)\le 2\,{\mathcal {A}}(3,6)-2.\)

### Proof

First of all, we recall following [[45][32]], the next properties of the periodic orbits of a quadratic DE:

-

They surround a single equilibrium point.

-

The equilibrium point must be a focus.

-

Only two equilibrium points can be simultaneously surrounded by periodic orbits.

-

Periodic orbits are convex.

Since the proofs that periodic orbits satisfy all four properties they are quite similar, we will not demonstrate all them. In fact, it ends up that they are essentially a consequence of the study of the vector field \(X=(P,Q)\) associated with the quadratic differential equation \((\dot{x},\dot{y} )=(P(x,y),Q(x,y))\) on the straight lines passing through its equilibrium points.

We prove the first property. If the DE has only one equilibrium point, there is nothing to be proved. If it has at least two, it is not restrictive to assume that one of them is the origin and that another one is for example the point (1, 0). Then \(\left. \dot{y}\right| _{y=0}=Q(x,0)=ax(x-1).\) If \(a=0\), then the line \(y=0\) is invariant by flow of the DE and therefore no periodic orbit can surround the origin. If \(a\ne 0\), the sign of \(ax(x-1)\) gives us the cutting direction of the orbits that pass through the point (*x*, 0). Since for \(x\in (0,1)\), this sign is opposite to when \(x\in (-\infty ,0)\cup (1,\infty )\), this makes it impossible for a periodic orbit to encircle the two points at the same time, see Fig. [3][181].(i) for the case \(a>0\).

**Fig. 3**

[image: Fig. 3]

[Full size image][182]

Vector field *X*on \(y=0\)

We now prove the second property. As above, it is not restrictive to assume that the equilibrium point surrounded by a periodic orbit is the origin. Suppose that the differential of the field *X*at the origin has a real eigenvalue \(\lambda\), including also the case \(\lambda =0.\) Making a rotation, if necessary, we can also assume that (0, 1) is the eigendirection associated with the eigenvalue \(\lambda\). Then \(Q(x,y)=\lambda y+ax^2+bxy+cy^2.\) Therefore \(\left. \dot{y}\right| _{y=0}=Q(x,0)=ax^2,\) see the case \(a>0\) in Fig. [3][181] (ii). Arguing similarly to the previous case we have that no limit cycle can surround the origin. Therefore, all the eigenvalues of the differential of *X*at (0, 0) are complex or, in other words, the origin is a focus, as we wanted to show.

Therefore, if a quadratic DE has limit cycles, we can assume that each of them surrounds a single equilibrium point, which must be of focus type. By an affine change, and a rescaling of time, this quadratic DE can write like

$$\begin{aligned} x'=P(x,y)=-y+ b x+ P_2(x,y),\quad y'=Q(x,y)=x+ b y +Q_2(x,y), \end{aligned}$$

where the prime denotes the derivative with respect to time, *t*, and \(P_2\) and \(Q_2\) are quadratic homogeneous polynomials. In polar coordinates, \(x=r\cos \theta ,\) \(y=r\sin \theta ,\) this DE writes as

$$\begin{aligned} r'= b r+ f(\theta )r^2,\quad \theta '=1+g(\theta )r, \end{aligned}$$

where *f*and *g*are the cubic homogeneous trigonometric polynomials

$$\begin{aligned} f(\theta )&= P_2(\cos \theta ,\sin \theta )\cos \theta +Q_2(\cos \theta ,\sin \theta )\sin \theta ,\\ g(\theta )&= Q_2(\cos \theta ,\sin \theta )\cos \theta - P_2(\cos \theta ,\sin \theta )\sin \theta . \end{aligned}$$

If we introduce the new variable \(\rho\), given by the Cherkas’ transformation \(\rho =r/(1+g(\theta )r)\), we have

$$\begin{aligned} \rho '=\frac{1}{(1+g(\theta )r)^2}r'-\frac{g'(\theta )r^2}{(1+g(\theta )r)^2} \theta '= \frac{ b r+ f(\theta )r^2}{(1+g(\theta )r)^2}-\frac{g'(\theta )r^2}{1+g(\theta ) r}. \end{aligned}$$

Recall that we know that limit cycles are convex. Therefore, we can assure \(1+g(\theta )r>0\) on them, and the transformation is well defined in an open set that contains all the limit cycles surrounding the origin. As \(r=\rho /(1-g(\theta )\rho )\) and \(1/(1+g(\theta )r)=1-g(\theta )\rho\), we arrive to

$$\begin{aligned} \rho '=(1-g(\theta )\rho )^2\left( b \frac{\rho }{1-g(\theta )\rho } +f(\theta )\frac{\rho ^2}{(1-g(\theta )\rho )^2}\right) -\frac{g'(\theta )\rho ^2}{1-g(\theta )\rho }. \end{aligned}$$

Finally,

$$\begin{aligned} \dot{\rho }&=\frac{\textrm{d}\rho }{\textrm{d}\theta }=(1-g(\theta )\rho )\rho '= b \rho (1-g(\theta )\rho )^2+f(\theta )\rho ^2(1-g(\theta )\rho )-g'(\theta )\rho ^2\\&= b \rho +\left( f(\theta )-2 b g(\theta )-g'(\theta ) \right) \rho ^2+ g(\theta ) ( b g(\theta )-f(\theta ))\rho ^3, \end{aligned}$$

which is an Abel’s equation of the form ( [21][178]), with \(c_m\) and \(d_n\) homogeneous trigonometric polynomials of degrees 3 and 6, respectively.

Therefore, the maximum number of limit cycles surrounding the origin is \({\mathcal {A}}(3,6)-1,\) because \(\rho =0\) does not correspond to an actual limit cycle. Applying the same result to the other equilibrium point that can be surrounded simultaneously by limit cycles, the upper bound is doubled and we obtain the desired result. \(\square\)

### Remark 5.2

In [[140][183]] the author asserts that if a quadratic DE has limit cycles that surround two different foci, then around one of them the maximum number of limit cycles is one. In the 2023 meeting “Advances in Qualitative Theory of Differential Equations, IVth edition” held in Port de Sóller, Mallorca, A. Zegeling gave the talk “Distribution of limit cycles in quadratic systems" where he tried to clarify some points of that paper. In his recent work [[139][184]] the result is fixed. Then \({\mathcal {H}}(2)\le {\mathcal {A}}(3,6).\)

The same idea used to prove Theorem [5.1][185] can also be used to study, by means of Abel’s equations, the number of limit cycles of certain families of polynomial DEs in the plane. One of these families is the one given by the sum of two homogeneous (or quasi homogeneous polynomial DEs), see for instance [[25][186], [41][150]]. For them, a variation of Cherkas’ transformation also works. Other families appear in [[2][187], [20][188], [39][189], [48][190], 70, 71, [72][191], [74][192]].

Abel’s equations have also been useful to study integrability of some DEs, see [[78][193]], or to study the presence of continua of periodic orbits, that is the so-called *center-focus problem*, see for example [[7][194], [37][195]]. In fact, there is a class of Abel’s equations that have a continuum of periodic solutions, the so-called *composition centers*, introduced in [[7][194]]. They provide an interesting class of centers for the corresponding planar differential equations.

We continue studying one of the above families of planar DEs that can be easily transformed into an Abel’s type equation, the one formed by the so-called *rigid systems.*Rigid systems are planar autonomous DEs such that their associated angular DE in polar coordinates is \(\dot{\theta }=1\). They were introduced by Conti [[44][196]] and afterwards they have been studied by many authors. They write as

$$\begin{aligned} x'=-y+xF(x,y),\quad y'=x+yF(x,y), \end{aligned}$$

(22)

where *F*is an arbitrary smooth function. Moreover, when *F*is a polynomial of degree *n*, \(F=F_0+F_1+\cdots + F_n,\) where \(F_j\) are homogeneous polynomials of degree *j*, in polar coordinates they write as the Abel’s type equations

$$\begin{aligned} \dot{r}= \frac{\textrm{d} r}{\textrm{d} \theta }=\sum _{j=0}^n F_j(\cos \theta ,\sin \theta )r^{j+1}. \end{aligned}$$

(23)

When \(n=1,\) it is a Riccati’s equation. Let us prove that then Eq. ( [22][197]) does not have limit cycles. Set \(F(x,y)=F_0+F_1(x,y)=a+bx+cy.\) Then Eq. ( [23][198]) is

$$\begin{aligned} \dot{r} = a r+g(\theta )r^2,\quad \text{ with }\quad g(\theta )=b\cos \theta + c\sin \theta . \end{aligned}$$

By Lemma [3.3][139] we know that it has at most 2 limit cycles. Let us prove that in fact, when \(a\ne 0,\) its only periodic solution is \(r=0,\) and hence, that the corresponding planar DE does not have limit cycles. If it would have another periodic orbit \(r=R(\theta )\) then it would be positive or negative, but in any case \(x=X(\theta ):=1/R(\theta )\) would be a non-vanishing periodic solution of the linear DE obtained via the change of variable \(x=1/r.\) This linear equation is

$$\begin{aligned} \dot{x}= -g(\theta ) -a x. \end{aligned}$$

Since \(a\ne 0,\) by replacing \(x=X(\theta )\) and integrating between 0 and \(2\pi\) we get that

$$\begin{aligned} 0&=X(2\pi )-X(0)=\int _0^{2\pi } X'(\theta )\,\textrm{d}\theta = -\int _0^{2\pi } g(\theta )\,\textrm{d}\theta -a\int _0^{2\pi } X(\theta )\,\textrm{d}\theta \\ &= -a\int _0^{2\pi } X(\theta )\,\textrm{d}\theta \ne 0, \end{aligned}$$

arriving to a contradiction. When \(a=0\) the DE reduces to \(\dot{r}=g(\theta )r^2\) that is of separable variables. It is easy to see that it can not have limit cycles either.

The rigid DE ( [23][198]) when \(n=2\) is precisely an Abel’s equation. If we write the planar system as

$$\begin{aligned} {\left\{ \begin{array}{ll} x'=-y+x(a+bx+cy+dx^2+exy+fy^2),\\ y'=\phantom {-}x+y(a+bx+cy+dx^2+exy+fy^2), \end{array}\right. } \end{aligned}$$

(24)

its expression in polar coordinates is

$$\begin{aligned} \dot{r} = a r+g(\theta )r^2+h(\theta )r^3, \end{aligned}$$

(25)

where

$$\begin{aligned} g(\theta )=b\cos \theta + c\sin \theta \quad \text{ and }\quad h(\theta )=d\cos ^2\theta +e\sin \theta \cos \theta +f \sin ^2\theta . \end{aligned}$$

Following [[72][191]], when *h*does not change sign we can apply Theorem [4.2][145] and Remark [4.3][199] to prove that this Abel’s equation has at most 3 limit cycles, taking into account their multiplicities. Since \(r=0\) is always one of these limit cycles and, by symmetry of the equation, if \(r(\theta )\) is one periodic orbit then \(-r(\theta +\pi )\) is also another one, we get that Eq. ( [25][200]) has at most one positive limit cycle, which has multiplicity one. Hence, when \(e^2-4df\le 0\) (condition that implies that *h*does not change sign) we have proved that Eq. ( [24][201]) has at most one limit cycle and that, when it exists, it is hyperbolic.

In [[72][191]], for some values of the parameters such that \(e^2-4df>0,\) there are examples of ( [24][201]) with at least two limit cycles. They are obtained by computing the first three Lyapunov quantities of the origin and proving that a codimension two Andronov–Hopf bifurcation happens. It is not known if two is the maximum number of limit cycles that Eq. ( [24][201]) can have.

To end the paper we will say a few words about another family of planar DEs. Following [[74][192]] consider

$$\begin{aligned} {\left\{ \begin{array}{ll} x'=x\big (P_{n-1}(x,y) + P_{n+2m-1}(x,y) + P_{n+3m-1}(x, y)\big ) + Q_{n+m}(x, y),\\ y'=x\big (P_{n-1}(x,y) + P_{n+2m-1}(x,y) + P_{n+3m-1}(x, y)\big ) + R_{n+m}(x, y), \end{array}\right. } \end{aligned}$$

(26)

where *n*and *m*are positive natural numbers and \(P_k,Q_k,\) and \(R_k\) are homogeneous polynomials of degree *k*. If we introduce the function

$$\begin{aligned} g_{n+m+1}(\theta )=R_{n+m}(\cos \theta ,\sin \theta )\cos \theta - Q_{n+m}(\cos \theta ,\sin \theta )\sin \theta ,\end{aligned}$$

the following holds.

### Theorem 5.3

[[74][192]] Consider system ( [26][202]). Then:

1. (a)

When \(n + m\) is even it has no limit cycles.

2. (b)

When \(n + m\) is odd:

  1. (i)

If \(g_{n+m+1}\) vanishes it has no limit cycles.

  2. (ii)

If \(P_{n+3m-1}\) does not change sign it has at most three limit cycles counting their multiplicities and this upper bound is sharp.

  3. (iii)

If \(P_{n+3m-1}\) changes sign there are systems having at least four limit cycles.

The proof of items (a) and (b)-(i) simply follows by noticing that, apart from the (0, 0), all the other equilibrium points of the system are on the straight lines \(\theta =\theta ^*\), where \(g_{n+m+1}(\theta ^*)=0,\) which are invariant by the flow. Finally, under the hypotheses of both items, it follows that the set of zeroes of \(g_{n+m+1}\) is non empty.

The proof of item (b)-(ii) is again a consequence of Theorem [4.2][145] and Remark [4.3][199]. In fact, if we write Eq. ( [26][202]), in the modified polar coordinates \(x=r^{1/m}\cos \theta ,\) \(y= r^{1/m}\sin \theta ,\) we get the \(2\pi\) -periodic Abel’s equation

$$\begin{aligned} \dot{r}=\frac{\textrm{d} r}{\textrm{d}\theta }=a(\theta )+b(\theta )r+c(\theta )r^2+d(\theta )r^3,\end{aligned}$$

(27)

where

$$\begin{aligned} a(\theta )=&\frac{m f_{n+1}(\theta )}{g_{n+m+1}(\theta )},&b(\theta )=&\frac{m f_{n+m+1}(\theta )}{g_{n+m+1}(\theta )},\\ c(\theta )=&\frac{m f_{n+2m+1}(\theta )}{g_{n+m+1}(\theta )},&d(\theta )=&\frac{m f_{n+3m+1}(\theta )}{g_{n+m+1}(\theta )}, \end{aligned}$$

with

$$\begin{aligned} f_{n+m+1}(\theta )&= Q_{n+m}(\cos \theta ,\sin \theta )\cos \theta +R_{n+m}(\cos \theta ,\sin \theta )\sin \theta ,\\ f_k(\theta )&= P_{k-1}(\cos \theta ,\sin \theta ),\quad \text{ where }\quad k=n,n+2m, n+3m.\end{aligned}$$

Finally the proof of item (b)-(iii) follows from the computation of a kind of Lyapunov quantities associated to \(r=0.\) In this latter case, it is not known if there is some upper bound for the number of limit cycles of the differential equation.

## References

1.

Abel, N. H.: Oeuvres Complètes II, Lie, S., Sylow, L. (eds.), in French, Christiana, . Capítol IV: Sur l’equation différentielle \(dy+(p+qy+ry^2)dx=0\), oú \(q,q\) et \(r\) sont des fonctions de \(x\) seul. Capítol V: Sur l’equation différentielle \((y+s)dy+(p+qy+ry^2)dx=0\) (1881)

2.

Álvarez, A., Bravo, J.L., Sánchez, F.: Planar systems and Abel equations. Commun. Pure Appl. Anal. **21**(10), 3463–3478 (2022)

[MathSciNet][203] [Google Scholar][204]

3.

Álvarez, M.J., Coll, B., De Maesschalck, P., Prohens, R.: Asymptotic lower bounds on Hilbert numbers using canard cycles. J. Differ. Equ. **268**(7), 3370–3391 (2020)

[MathSciNet][205] [Google Scholar][206]

4.

Álvarez, M.J., Gasull, A., Giacomini, H.: A new uniqueness criterion for the number of periodic orbits of Abel equations. J. Differ. Equ. **234**(1), 161–176 (2007)

[MathSciNet][207] [Google Scholar][208]

5.

Álvarez, M.J., Gasull, A., Prohens, R.: Limit cycles for two families of cubic systems. Nonlinear Anal., Theory Methods Appl. Ser. A, Theory Methods **75**(18), 6402–6417 (2012)

[MathSciNet][209] [Google Scholar][210]

6.

Álvarez, M.J., Gasull, A., Yu, J.: Lower bounds for the number of limit cycles of trigonometric Abel equations. J. Math. Anal. Appl. **342**, 682–693 (2008)

[MathSciNet][211] [Google Scholar][212]

7.

Alwash, M.A.M., Lloyd, N.G.: Non-autonomous equations related to polynomial two-dimensional systems. Proc. R. Soc. Edinb. **105A**, 129–152 (1987)

[Google Scholar][213]

8.

Andersen, K.M., Sandqvist, A.: On the determination of the number of periodic (or closed) solutions of a scalar differential equation with convexity. J. Math. Anal. Appl. **331**, 206–219 (2007)

[MathSciNet][214] [Google Scholar][215]

9.

Andronov, A. A., et al., Qualitative Theory of Second-order Dynamic Systems, (Transl. from the Russian) Wiley, New York (1973)

10.

Andronov, A. A., et al., Theory of Bifurcations of Dynamic Systems on a Plane, (Transl. from the Russian) Wiley, New York (1973)

11.

Bamón, R.: Solution of Dulac’s problem for quadratic vector fields. An. Acad. Bras. Ciênc. **57**, 265–266 (1985)

[MathSciNet][216] [Google Scholar][217]

12.

Bamón, R.: Quadratic vector fields in the plane have a finite number of limit cycles. Publ. Math., Inst. Hautes Étud. Sci. **64**, 111–142 (1986)

[MathSciNet][218] [Google Scholar][219]

13.

Bazykin, A.D., Khibnik, A.I.: Biophysics of complex systems. Rigid regime of excitation of auto-oscillations in a model of the Volterra type. Biophysics **5**, 866–869 (1981)

[Google Scholar][220]

14.

Benardete, D.M., Noonburg, V.W., Pollina, B.: Qualitative tools for studying periodic solutions and bifurcations as applied to the periodically harvested logistic equation. Am. Math. Mon. **115**, 202–219 (2008)

[MathSciNet][221] [Google Scholar][222]

15.

Bernoulli, D.: Essai d’une nouvelle analyse de la mortalité causée par la petite vérole et des avantages de l’inoculation pour la prévenir, in French. Mem. Math. Phys. Acad. Roy. Sci., Paris, 1–45 (1760)

16.

Bittanti, S., Laub, A.J., Willems, J.C. (eds.): The Riccati Equation. Communications and Control Engineering Series, Springer, Berlin (1991)

[Google Scholar][223]

17.

Blows, T.R., Lloyd, N.G.: The number of small-amplitude limit cycles of Liénard equations. Math. Proc. Camb. Philos. Soc. **95**, 359–366 (1984)

[Google Scholar][224]

18.

Bohner, M., Gasull, A., Valls, C.: Periodic solutions of linear, Riccati, and Abel dynamic equations. J. Math. Anal. Appl. **470**(2), 733–749 (2019)

[MathSciNet][225] [Google Scholar][226]

19.

Bravo, J.L., Fernández, M., Gasull, A.: Limit cycles for some Abel equations having coefficients without fixed signs. Int. J. Bifurc. Chaos Appl. Sci. Eng. **19**(11), 3869–3876 (2009)

[MathSciNet][227] [Google Scholar][228]

20.

Bravo, J.L., Fernández, M., Ojeda, I., Sánchez, F.: Uniqueness of limit cycles for quadratic vector fields. Discrete Contin. Dyn. Syst. **39**(1), 483–502 (2019)

[MathSciNet][229] [Google Scholar][230]

21.

Bravo, J.L., Fernández, M., Tineo, A.: Periodic solutions of a periodic scalar piecewise ODE. Commun. Pure Appl. Anal. **6**(1), 213–228 (2007)

[MathSciNet][231] [Google Scholar][232]

22.

Campos, J.: Möbius transformations and periodic solutions of complex Riccati equations Bull. Lond. Math. Soc. **29**(2), 205–215 (1997)

[Google Scholar][233]

23.

Campos, J., Ortega, R.: Nonexistence of periodic solutions of a complex Riccati equation. Differ. Integral Equ. **9**(2), 247–249 (1996)

[MathSciNet][234] [Google Scholar][235]

24.

Cantin, G.: Bifurcations of limit cycles in complex networks of Hamiltonian systems and Lloyd’s conjecture. J. Math. Anal. Appl. **477**(1), 272–293 (2019)

[MathSciNet][236] [Google Scholar][237]

25.

Carbonell, M., Llibre, J.: Limit cycles of a class of polynomial systems. Proc. R. Soc. Edinb. Sect. A **109**, 187–199 (1988)

[MathSciNet][238] [Google Scholar][239]

26.

( Chandrasekhar, S.: An Introduction to the Study of Stellar Structure, Chapter 4. Chicago Univ. Press, 1939 (repr. Dover, New York) (1957)

27.

Cheb-Terrab, E.S., Roche, A.D.: Abel ODEs: Equivalence and integrable classes. Comput. Phys. Commun. **130**, 204–231 (2000)

[Google Scholar][240]

28.

Chen, L., Wang, M.: The relative position and number of limit cycles of the quadratic differential system. Acta Math. Sin. **22**, 751–758 (1979). (**(in Chinese)**)

[MathSciNet][241] [Google Scholar][242]

29.

Cherkas, L.A.: Estimation of the number of limit cycles of autonomous systems. Differ. Equ. **13**, 529–547 (1977)

[Google Scholar][243]

30.

Cherkas, L.A.: Dulac function for polynomial autonomous systems on a plane. Differ. Equ. **33**, 692–701 (1997)

[MathSciNet][244] [Google Scholar][245]

31.

Chicone, C.: Ordinary Differential Equations with Applications. Texts in Applied Mathematics, vol. 34, 2nd edn. Springer, New York (2006)

[Google Scholar][246]

32.

Chicone, C., Shafer, D.S.: Separatrix and limit cycles of quadratic systems and Dulac’s theorem. Trans. Am. Math. Soc. **278**, 585–612 (1983)

[MathSciNet][247] [Google Scholar][248]

33.

Christopher, C.J., Li, C., Torregrosa, J.: Limit Cycles of Differential Equations. Birkhäuser, Cham (2024)

[Google Scholar][249]

34.

Christopher, C.J., Lloyd, N.G.: Polynomial systems: a lower bound for the Hilbert numbers. Proc. R. Soc. Lond. Ser. A **450**, 219–224 (1995)

[MathSciNet][250] [Google Scholar][251]

35.

Cima, A., Gasull, A., Mañosa, V.: Dynamics of some rational discrete dynamical systems via invariants,. Int. J. Bifur. Chaos Appl. Sci. Eng. **16**(3), 631–645 (2006)

[MathSciNet][252] [Google Scholar][253]

36.

Cima, A., Gasull, A., Mañosas, F.: Periodic orbits in complex Abel equations. J. Differ. Equ. **232**, 314–328 (2007)

[MathSciNet][254] [Google Scholar][255]

37.

Cima, A., Gasull, A., Mañosas, F.: A simple solution of some composition conjectures for Abel equations. J. Math. Anal. Appl. **398**, 477–486 (2013)

[MathSciNet][256] [Google Scholar][257]

38.

Cima, A., Gasull, A., Mañosas, F.: Periods of solutions of periodic differential equations. Differ. Integral Equ. **29**(9–10), 905–922 (2016)

[MathSciNet][258] [Google Scholar][259]

39.

Coll, B., Gasull, A., Llibre, J.: Some theorems on the existence, uniqueness, and nonexistence of limit cycles for quadratic systems. J. Differ. Equ. **67**, 372–399 (1987)

[MathSciNet][260] [Google Scholar][261]

40.

Coll, B., Gasull, A., Prohens, R.: Limit cycles for nonsmooth differential equations via Schwarzian derivative. J. Differ. Equ. **132**, 203–221 (1996)

[MathSciNet][262] [Google Scholar][263]

41.

Coll, B., Gasull, A., Prohens, R.: Differential equations defined by the sum of two quasi-homogeneous vector fields. Can. J. Math. **49**, 212–231 (1997)

[MathSciNet][264] [Google Scholar][265]

42.

Coll, B., Gasull, A., Prohens, R.: Simple non-autonomous differential equations with many limit cycles. Commun. Appl. Nonlinear Anal. **15**, 29–34 (2008)

[MathSciNet][266] [Google Scholar][267]

43.

Coll, B., Gasull, A., Prohens, R.: Periodic orbits for perturbed non-autonomous differential equations. Bull. Sci. Math. **136**(7), 803–819 (2012)

[MathSciNet][268] [Google Scholar][269]

44.

Conti, R.: Uniformly isochronous centers of polynomial systems in \({\bf R}^2\). In: Differential Equations, Dynamical Systems, and Control Science, vol. 152 of Lecture Notes in Pure and Appl. Math. Dekker, New York, pp. 21–31 (1994)

45.

Coppel, W.A.: A survey of quadratic systems. J. Differ. Equ. **2**, 293–304 (1966)

[MathSciNet][270] [Google Scholar][271]

46.

De Maesschalck, P., Dumortier, F.: Classical Liénard equations of degree \(n\ge 6\) can have \([(n-1)/2]+2\) limit cycles. J. Differ. Equ. **250**(4), 2162–2176 (2011)

[Google Scholar][272]

47.

De Maesschalck, P., Huzak, R.: Slow divergence integrals in classical Liénard equations near centers. J. Dyn. Differ. Equ. **27**(1), 177–185 (2015)

[Google Scholar][273]

48.

Devlin, J., Lloyd, N.G., Pearson, J.M.: Cubic systems and Abel equations. J. Differ. Equ. **147**, 435–454 (1998)

[MathSciNet][274] [Google Scholar][275]

49.

Dreyer, N., Gabriel, J. P.: Bernouilli et la variole, in French. Bull. de la Soc. des Enseig. Neuchâtelois de Sciences **39 **: 1–13. (The name Bernoulli is misspelled in the title) (2010)

50.

Dumortier, F., Llibre, J., Artés, J.C.: Qualitative Theory of Planar Differential Systems. Universitext, Springer, Berlin (2006)

[Google Scholar][276]

51.

Dumortier, F., Panazzolo, D., Roussarie, R.: More limit cycles than expected in Liénard equations. Proc. Am. Math. Soc. **135**(6), 1895–1904 (2007)

[Google Scholar][277]

52.

Dumortier, F., Roussarie, R., Rousseau, C.: Hilbert’s 16th problem for quadratic vector fields. J. Differ. Equ. **110**(1), 86–133 (1994)

[MathSciNet][278] [Google Scholar][279]

53.

Écalle, J.: Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac, in French. Actualitiées Math, Hermann, Paris (1992)

[Google Scholar][280]

54.

Ferragut, A., Gasull, A.: Non-algebraic oscillations for predator-prey models. Publ. Mat. Extra, pp. 195–207 (2014)

55.

Fossas, E., Olm, J.M., Sira-Ramírez, H.: Iterative approximation of limit cycles for a class of Abel equations. Phys. D **237**, 3159–3164 (2008)

[MathSciNet][281] [Google Scholar][282]

56.

García, I.A.: Transcendental limit cycles via the structure of arbitrary degree invariant algebraic curves of polynomial planar vector fields. Rocky Mt. J. Math. **35**(2), 501–515 (2005)

[MathSciNet][283] [Google Scholar][284]

57.

Garcia, R., Llibre, J., Sotomayor, J.: Lines of principal curvature on canal surfaces in \({\mathbb{R} }^3,\) An. Acad. Bras. Ciênc. **78**(3), 405–415 (2006)

[Google Scholar][285]

58.

Gasull, A.: About the number of limit cycles of a generalized Liénard equation. In: VI Congreso de Ecuaciones Diferenciales y Aplicaciones (VI CEDYA), Jaca, pp. 373–377 (in Spanish) (1983)

59.

Gasull, A.: Qualitative study of some classes of differential equations on the plane, PhD thesis, Universitat Autònoma de Barcelona (1986)

60.

Gasull, A.: Differential equations that can be transformed into equations of Liénard type. In Actas del XVLL Colóquio Brasileiro de Matemática (1989)

61.

Gasull, A.: From Abel’s differential equations to Hilbert’s XVIth problem. Butll. Soc. Catalana Mat. **28**(2), 123–146 (2013). (**(in Catalan)**)

[Google Scholar][286]

62.

Gasull, A.: Some open problems in low dimensional dynamical systems. SeMA J. **78**(3), 233–269 (2021)

[MathSciNet][287] [Google Scholar][288]

63.

Gasull, A., Giacomini, H.: Some applications of the extended Bendixson–Dulac theorem. In: Progress and Challenges in Dynamical Systems, 233-252. Springer (2013)

64.

Gasull, A., Giacomini, H.: Effectiveness of the Bendixson–Dulac theorem. J. Differ. Equ. **305**, 347–367 (2021)

[MathSciNet][289] [Google Scholar][290]

65.

Gasull, A., Giacomini, H., Torregrosa, J.: Explicit non-algebraic limit cycles for polynomial systems. J. Comput. Appl. Math. **200**(1), 448–457 (2007)

[MathSciNet][291] [Google Scholar][292]

66.

Gasull, A., Guillamon, A.: Limit cycles for generalized Abel equations. Int. J. Bifur. Chaos Appl. Sci. Eng. **16**, 3737–3745 (2006)

[MathSciNet][293] [Google Scholar][294]

67.

Gasull, A., Kooij, R.E., Torregrosa, J.: Limit cycles in the Holling–Tanner model. Publ. Mat. **41**(1), 149–167 (1997)

[MathSciNet][295] [Google Scholar][296]

68.

Gasull, A., Li, C., Torregrosa, J.: A new Chebyshev family with applications to Abel equations. J. Differ. Equ. **252**, 1635–1641 (2012)

[MathSciNet][297] [Google Scholar][298]

69.

Gasull, A., Llibre, J.: Limit cycles for a class of Abel equations. SIAM J. Math. Anal. **21**, 1235–1244 (1990)

[MathSciNet][299] [Google Scholar][300]

70.

Gasull, A., Llibre, J., Sotomayor, J.: Limit cycles of vector fields of the form \(X(v) = Av + f (v)Bv\). J. Differ. Equ. **67**, 90–110 (1987)

[MathSciNet][301] [Google Scholar][302]

71.

Gasull, A., Llibre, J., Sotomayor, J.: Further considerations on the number of limit cycles of vector fields of the form \(X(v) = Av + f (v)Bv\). J. Differ. Equ. **68**, 36–40 (1987)

[MathSciNet][303] [Google Scholar][304]

72.

Gasull, A., Prohens, R., Torregrosa, J.: Limit cycles for rigid cubic systems. J. Math. Anal. Appl. **303**, 391–404 (2005)

[MathSciNet][305] [Google Scholar][306]

73.

Gasull, A., Torregrosa, J.: A relation between small amplitude and big limit cycles. Rocky Mt. J. Math. **31**(4), 1277–1303 (2001)

[MathSciNet][307] [Google Scholar][308]

74.

Gasull, A., Zhao, Y.: On a family of polynomial differential equations having at most three limit cycles. Houston J. Math. **3**(1), 191–203 (2013)

[MathSciNet][309] [Google Scholar][310]

75.

Gasull, A., Zhao, Y.: Existence of at most two limit cycles for some non-autonomous differential equations. Commun. Pure Appl. Anal. **22**(3), 970–982 (2023)

[MathSciNet][311] [Google Scholar][312]

76.

Giacomini, H., Neukirch, S.: Number of limit cycles of the Liénard equation. Phys. Rev. E **56**, 3809 (1997)

[MathSciNet][313] [Google Scholar][314]

77.

Giné, J., Grau, M.: Coexistence of algebraic and non-algebraic limit cycles, explicitly given, using Riccati equations. Nonlinearity **19**(8), 1939–1950 (2006)

[MathSciNet][315] [Google Scholar][316]

78.

Giné, J., Llibre, J.: Darboux Integrability and Limit Cycles for a Class of Polynomial Differential Systems, Differential Equations with Symbolic Computation, 55–65. Trends Math, Birkhäuser, Basel (2005)

[Google Scholar][317]

79.

Gray, J., Replies, Poincaré, to Hilbert: On the Future of Mathematics ca.: Math. Intelligencer; 34(2012), 15–29 (1908)

80.

Han, M., Li, C., Li, J.: Limit cycles of planar polynomial vector fields. Scholarpedia 5(8):9648, revision #137138

81.

Harko, T., Mak, M.K.: Relativistic dissipative cosmological models and Abel differential equation. Comput. Math. Appl. **46**, 849–853 (2003)

[MathSciNet][318] [Google Scholar][319]

82.

Hille, E.: Ordinary Differential Equations in the Complex Domain, Reprint of the 1976 original. Dover Publications Inc, Mineola (1997)

[Google Scholar][320]

83.

Hirsch, M.W., Smale, S.: Differential Equations, Dynamical Systems, and Linear Algebra, Pure and Applied Mathematics, vol. 60. Academic Press, New York (1974)

[Google Scholar][321]

84.

Houzel, C.: The Work of Niels Henrik Abel, The Legacy of Niels Henryk Abel-The Abel Bicentennial, Oslo 2002. Springer, Berlin (2004)

[Google Scholar][322]

85.

Huang, J., Torregrosa, J., Villadelprat, J.: On the number of limit cycles in generalized Abel equations. SIAM J. Appl. Dyn. Syst. **19**(4), 2343–2370 (2020)

[MathSciNet][323] [Google Scholar][324]

86.

Ikeuchi, S., Tomita, H.: Cyclic phase changes of interstellar medium. Publ. Astron. Soc. Jpn. **35**, 77–86 (1983)

[Google Scholar][325]

87.

Il’yashenko, Y., Finiteness theorems for limit cycles. Uspekhi Mat. Nauk 45 (1990), no. 2(272), 143–200 (in Russian); translated to English in Russian Math. Surveys 45, 129–203 (1990)

88.

Il’yashenko, Y.: Centennial history of Hilbert’s 16th problem. Bull. Am. Math. Soc. (N.S.) **39**, 301–354 (2002)

[MathSciNet][326] [Google Scholar][327]

89.

Isaacson, E., Keller, H.B.: Analysis of Numerical Methods. Wiley, Hoboken (1966)

[Google Scholar][328]

90.

Kamke, E.: Differentialgleichungen: Lösungsmethoden und Lösungen, in German. Chelsea Publishing Co, New York (1959)

[Google Scholar][329]

91.

Karlin, S., Studden, W. J.: Tchebycheff systems: With applications in analysis and statistics, Pure and Applied Mathematics. Vol. 15. Inderscience Publishers a division of Wiley, New York etc. XVIII (1966)

92.

Li, C., Liu, C., Yang, J.: A cubic system with thirteen limit cycles. J. Differ. Equ. **246**, 3609–3619 (2009)

[MathSciNet][330] [Google Scholar][331]

93.

Li, C., Li, W., Llibre, J., Zhang, Z.: Polynomial systems: a lower bound for the weakened 16th Hilbert problem. Extr. Math. **16**, 441–447 (2001)

[MathSciNet][332] [Google Scholar][333]

94.

Li, C., Llibre, J.: Uniqueness of limit cycles for Liénard differential equations of degree four. J. Differ. Equ. **252**, 3142–3162 (2012)

[Google Scholar][334]

95.

Li, C., Zhu, H.: Canard cycles for predator-prey systems with Holling types of functional response. J. Differ. Equ. **254**, 879–910 (2013)

[MathSciNet][335] [Google Scholar][336]

96.

Li, J.: Hilbert’s 16th problem and bifurcations of planar polynomial vector fields. Int. J. Bifur. Chaos Appl. Sci. Eng. **13**, 47–106 (2003)

[MathSciNet][337] [Google Scholar][338]

97.

Lins Neto, A.: On the number of solutions of the equation \(dx/dt=\sum _{j=0}^{n}a_j(t)x^j\), \(0\le t\le 1\) for which \(x(0)=x(1)\). Inv. Math. **59**, 67–76 (1980)

[Google Scholar][339]

98.

Lins, A., de Melo, W., Pugh, C.C.: On Liénard’s equation, Springer Lecture. Notes **597**, 335–357 (1977)

99.

Llibre, J.: The averaging theory for computing periodic orbits. In: Central Configurations, Periodic Orbits, and Hamiltonian Systems. Advanced Courses in Mathematics - CRM Barcelona. Birkhäuser, Basel (2015)

100.

Lloyd, N.G.: The number of periodic solutions of the equation \(z^{\prime }=z^N+p_1(t)z^{N-1}+\cdots +p_N(t),\). Proc. Lond. Math. Soc. **III**(Ser. 27), 667–700 (1973)

[Google Scholar][340]

101.

Lloyd, N.G.: On a class of differential equations of Riccati type. J. Lond. Math. Soc. **II**(Ser. 10), 1–10 (1975)

[MathSciNet][341] [Google Scholar][342]

102.

Lloyd, N.G.: A note on the number of limit cycles in certain two-dimensional systems. J. Lond. Math. Soc. **20**, 277–286 (1979)

[MathSciNet][343] [Google Scholar][344]

103.

Lloyd, N.G.: Limit cycles of polynomial systems-some recent developments. New directions in dynamical systems. Lond. Math. Soc. Lect. Note Ser. **127**, 192–234 (1988)

[Google Scholar][345]

104.

Mawhin, J.: Resonance and nonlinearity: a survey. Ukr. Math. J. **59**, 197–214 (2007)

[MathSciNet][346] [Google Scholar][347]

105.

de Melo, W.: Bifurcation of unimodal maps. Qual. Theory Dyn. Syst. **4**, 413–424 (2004)

[MathSciNet][348] [Google Scholar][349]

106.

Murray, J.D.: Mathematical Biology. I. An Introduction. Interdisciplinary Applied Mathematics, vol. 17, 3rd edn. Springer, New York (2002)

[Google Scholar][350]

107.

Odani, K.: The limit cycle of the van der Pol equation is not algebraic. J. Differ. Equ. **115**(1), 146–152 (1995)

[MathSciNet][351] [Google Scholar][352]

108.

Ortega, R.: The complex periodic problem for a Riccati equation. Ann. Univ. Buchar. Math. Ser. **3**(61(2)), 219–226 (2012)

[MathSciNet][353] [Google Scholar][354]

109.

Ortega, R., Rojas, D.: Periodic oscillators, isochronous centers and resonance. Nonlinearity **32**(3), 800–832 (2019)

[MathSciNet][355] [Google Scholar][356]

110.

Ortega, R., Tarallo, M.: Degenerate equations of pendulum-type. Commun. Contemp. Math. **2**(2), 127–149 (2000)

[MathSciNet][357] [Google Scholar][358]

111.

Panov, A.A.: The number of periodic solutions of polynomial differential equations. Math. Notes **64**, 622–628 (1998)

[MathSciNet][359] [Google Scholar][360]

112.

Perko, L.: Differential Equations and Dynamical Systems. Texts in Applied Mathematics, vol. 7, 3rd edn. Springer, New York (2001)

[Google Scholar][361]

113.

Pliss, V.A.: Non Local Problems of the Theory of Oscillations. Academic Press, New York (1966)

[Google Scholar][362]

114.

Pollicott, M., Wang, H., Weiss, H.: Extracting the time-dependent transmission rate from infection data via solution of an inverse ODE problem. J. Biol. Dyn. **6**, 509–523 (2012)

[MathSciNet][363] [Google Scholar][364]

115.

Prohens, R., Torregrosa, J.: New lower bounds for the Hilbert numbers using reversible centers. Nonlinearity **32**, 331–355 (2019)

[MathSciNet][365] [Google Scholar][366]

116.

Romanovskii, V. G.: On the number of limit cycles of a second order system of differential equations, (in Russian) Ph.D. thesis, Leningrad State University (1986)

117.

Romanovskii, V. G.: Finiteness of the number of limit cycles of a quadratic system. Differentsial’nye Uravneniya 24, No. 11 (1988), 1904–1911 (in Russian); Differential Equations 24, No.11 (1988), pp. 1271–1277 (English translation)

118.

Rosenzweig, M., MacArthur, R.H.: Graphical representation of stability conditions of predator-prey interactions. Am. Nat. **97**, 209–223 (1963)

[Google Scholar][367]

119.

Roussarie, R.: A note on finite cyclicity property and Hilbert’s 16th problem, Dynamical systems. In: Proc. Symp., Valparaiso, Chile,: Lect. Notes Math. vol. 1331(1988), pp. 161–168 (1986)

120.

Roussarie, R.: Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem. Reprint of the 1998 edn. Modern Birkhäuser Classics, vol. 164. Birkhäuser, Basel

121.

Rychkov, G.S.: The maximum number of limit cycles of the system \(\dot{y}=-x\), \(\dot{y}=y-\sum ^2_{i=0} a_ix^{2i+1}\) is two. Differ. Equ. **11**, 301–302 (1975)

[Google Scholar][368]

122.

Schnakenberg, J.: Simple chemical reaction systems with limit cycle behaviour. J. Theoret. Biol. **81**, 389–400 (1979)

[MathSciNet][369] [Google Scholar][370]

123.

Sel’kov, E.E.: Self-oscillations in glycolysis: a simple kinetic model. Eur. J. Biochem. **4**(1), 79–86 (1968)

[Google Scholar][371]

124.

Shi, S.: A concrete example of the existence of four limit cycles for plane quadratic systems. Sci. Sin. **23**, 153–158 (1980)

[MathSciNet][372] [Google Scholar][373]

125.

Smale, S.: Mathematical problems for the next century. Math. Intell. **20**, 7–15 (1998)

[MathSciNet][374] [Google Scholar][375]

126.

Sotomayor, J.: Lições de Equações Diferenciais Ordinárias, in Portuguese, Projeto Euclides, 11. Rio de Janeiro: Instituto de Matemática Pura e Aplicada, CNPq. XVI (1979)

127.

Sotomayor, J.: Curvas Definidas por Equações Diferenciais no Plano, in Portuguese, \(13^o\) Colóquio Brasileiro de Matemática, Instituto de Matemática Pura e Aplicada, CNPq (1981) Brazil

128.

Van der Pol, B.: On relaxation-oscillations, the London, Edinburgh and Dublin. Phil. Mag. J. Sci. **2**(7), 978–992 (1927)

[Google Scholar][376]

129.

Viro, O.: From the sixteenth Hilbert problem to tropical geometry. Jpn. J. Math. **3**, 185–214 (2008)

[MathSciNet][377] [Google Scholar][378]

130.

Weyl, H.: On the differential equations of the simplest boundary-layer problems. Ann. Math. **43**, 381–407 (1942)

[MathSciNet][379] [Google Scholar][380]

131.

Wilczyński, P.: Planar nonautonomous polynomial equations: the Riccati equation. J. Differ. Equ. **244**(6), 1304–1328 (2008)

[MathSciNet][381] [Google Scholar][382]

132.

Wilczyński, P.: Quaternionic-valued ordinary differential equations. The Riccati equation. J. Differ. Equ. **247**(7), 2163–2187 (2009)

[MathSciNet][383] [Google Scholar][384]

133.

Wilczyński, P.: Planar nonautonomous polynomial equations V. The Abel equation. Opusc. Math. **33**(1), 175–189 (2013)

[MathSciNet][385] [Google Scholar][386]

134.

Wilson, G.: Hilbert’s sixteenth problem. Topology **17**, 53–73 (1978)

[MathSciNet][387] [Google Scholar][388]

135.

Yua X., Huangb J., Liu, C.: Maximum number of limit cycles for Abel equation having coefficients with linear trigonometric functions, Preprint (2023)

136.

Ye, Y. et al., Theory of Limit Cycles, (Transl. from the Chinese) Translations of Mathematical Monographs, vol. 66. American Mathematical Society (AMS), Providence, R.I. (1986)

137.

Yeung, M.: On the monograph “Finiteness Theorems for limit cycles” and a special case of alternant cycles, Preprint (2023)

138.

Yurov, A.V., Yaparova, A.V., Yurov, V.A.: Application of the Abel equation of the 1st kind to inflation analysis of non-exactly solvable cosmological models. Gravit. Cosmol. **20**, 106–115 (2014)

[MathSciNet][389] [Google Scholar][390]

139.

Zegeling, A.: Nests of limit cycles in quadratic systems. Adv. Nonlinear Anal. **13**, 20240012 (2024)

[MathSciNet][391] [Google Scholar][392]

140.

Zhang, P.: On the distribution and number of limit cycles for quadratic systems with two foci. Qual. Theory Dyn. Syst. **3**, 437–463 (2002)

[MathSciNet][393] [Google Scholar][394]

141.

Zhang, Z. et al., Qualitative Theory of Differential Equations, (Transl. from the Chinese) Translations of Mathematical Monographs, Vol. 101. American Mathematical Society (AMS), Providence, RI (1992)

142.

Zoladek, H.: The XVI-th Hilbert problem about limit cycles, Panoramas of mathematics. Colloquia 93–94. Lectures delivered at the Banach Center colloquium in Warsaw, Poland in the academic years 1992/93 and 1993/94. Banach Cent. Publ. **34**, 167–174 (1995)

[MathSciNet][395] [Google Scholar][396]

143.

Zuppa, C.: Order of cyclicity of the singular point of Liénard’s polynomial vector fields. Bol. Soc. Bras. Mat. **12**(2), 105–111 (1981)

[MathSciNet][397] [Google Scholar][398]

[Download references][399]

## Acknowledgements

This work is supported by the Spanish State Research Agency, through the projects PID2022-136613NB-I00 grant and the Severo Ochoa and María de Maeztu Program for Centers and Units of Excellence in R &D (CEX2020-001084-M), and grant 2021-SGR-00113 from AGAUR, Generalitat de Catalunya. The author acknowledges all comments and suggestions received from many colleagues and friends that have improved the preliminary versions of this work.

## Funding

Open Access Funding provided by Universitat Autonoma de Barcelona. Open Access Funding provided by Universitat Autonoma de Barcelona.

## Author information

### Authors and Affiliations

1.

Departament de Matemàtiques, Universitat Autònoma de Barcelona, Edifici C, 08193, Cerdanyola del Vallès, Barcelona, Spain

Armengol Gasull

2.

Centre de Recerca Matemàtica, Edifici C, Campus de Bellaterra, 08193, Cerdanyola del Vallès, Barcelona, Spain

Armengol Gasull

Authors

1. Armengol Gasull

[View author publications][400]

Search author on: [PubMed][401] [Google Scholar][402]

### Corresponding author

Correspondence to [Armengol Gasull][403].

## Ethics declarations

### Conflict of interest

The author declares that he has no conflict of interest.

## Additional information

Communicated by Marco Antonio Teixeira.

*Dedicado a mi profesor y amigo Jorge Sotomayor, quien nos dejó demasiado pronto. Dedicated to my professor and friend Jorge Sotomayor, who left us too soon.*

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][404].

[Reprints and permissions][405]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [406]

### Cite this article

Gasull, A. From Abel’s differential equations to Hilbert’s 16th problem. *São Paulo J. Math. Sci.***18**, 1342–1379 (2024). https://doi.org/10.1007/s40863-024-00471-2

[Download citation][407]

-

Accepted: 02 September 2024

-

Published: 28 September 2024

-

Version of record: 28 September 2024

-

Issue date: December 2024

-

DOI: https://doi.org/10.1007/s40863-024-00471-2

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Polynomial differential equation][408]
- [Periodic orbit][409]
- [Limit cycle][410]
- [Hilbert’s 16 h problem][411]
- [Riccati’s equation][412]
- [Abel’s equation][413]

### Mathematics Subject Classification

- [Primary: 34C07][414]
- [Secondary: 34C25][415]
- [37C27][416]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s40863-024-00471-2.pdf
[3]: /article/10.1007/s40863-024-00471-2/save-research?_csrf=jC9FgE5AXcmSp0GDAKPAW_FKTcPyt6E5
[4]: /saved-research
[5]: /journal/40863
[6]: /journal/40863/aims-and-scope
[7]: https://www.editorialmanager.com/spjm
[8]: https://link.springer.com/10.1007/s11071-022-07891-9?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s40324-021-00244-3?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/978-3-030-59656-9_12?fromPaywallRec=false
[11]: /subjects/differential-equations
[12]: /subjects/differential-geometry
[13]: /subjects/dynamical-systems
[14]: /subjects/linear-algebra
[15]: /subjects/mathematics
[16]: /subjects/ordinary-differential-equations
[17]: /subjects/dynamical-systems-and-bifurcation-theory
[18]: /article/10.1007/s40863-024-00471-2#ref-CR59
[19]: /article/10.1007/s40863-024-00471-2#ref-CR70
[20]: /article/10.1007/s40863-024-00471-2#ref-CR71
[21]: /article/10.1007/s40863-024-00471-2#ref-CR61
[22]: /article/10.1007/s40863-024-00471-2#ref-CR83
[23]: /article/10.1007/s40863-024-00471-2#ref-CR128
[24]: /article/10.1007/s40863-024-00471-2#ref-CR106
[25]: /article/10.1007/s40863-024-00471-2#ref-CR118
[26]: /article/10.1007/s40863-024-00471-2#ref-CR122
[27]: /article/10.1007/s40863-024-00471-2#ref-CR5
[28]: /article/10.1007/s40863-024-00471-2#ref-CR86
[29]: /article/10.1007/s40863-024-00471-2/figures/1
[30]: /article/10.1007/s40863-024-00471-2#Fig1
[31]: /article/10.1007/s40863-024-00471-2#ref-CR26
[32]: /article/10.1007/s40863-024-00471-2#ref-CR45
[33]: /article/10.1007/s40863-024-00471-2#ref-CR130
[34]: /article/10.1007/s40863-024-00471-2#ref-CR123
[35]: /article/10.1007/s40863-024-00471-2#ref-CR13
[36]: /article/10.1007/s40863-024-00471-2#ref-CR67
[37]: /article/10.1007/s40863-024-00471-2#ref-CR95
[38]: /article/10.1007/s40863-024-00471-2#ref-CR126
[39]: /article/10.1007/s40863-024-00471-2#ref-CR127
[40]: /article/10.1007/s40863-024-00471-2#ref-CR120
[41]: /article/10.1007/s40863-024-00471-2#ref-CR129
[42]: /article/10.1007/s40863-024-00471-2#ref-CR134
[43]: /article/10.1007/s40863-024-00471-2#ref-CR79
[44]: /article/10.1007/s40863-024-00471-2#ref-CR53
[45]: /article/10.1007/s40863-024-00471-2#ref-CR87
[46]: /article/10.1007/s40863-024-00471-2#Equ1
[47]: /article/10.1007/s40863-024-00471-2#ref-CR125
[48]: /article/10.1007/s40863-024-00471-2#ref-CR137
[49]: /article/10.1007/s40863-024-00471-2#ref-CR88
[50]: /article/10.1007/s40863-024-00471-2#ref-CR96
[51]: /article/10.1007/s40863-024-00471-2#ref-CR80
[52]: /article/10.1007/s40863-024-00471-2#ref-CR46
[53]: /article/10.1007/s40863-024-00471-2#ref-CR47
[54]: /article/10.1007/s40863-024-00471-2#ref-CR51
[55]: /article/10.1007/s40863-024-00471-2#ref-CR76
[56]: /article/10.1007/s40863-024-00471-2#ref-CR94
[57]: /article/10.1007/s40863-024-00471-2#Equ2
[58]: /article/10.1007/s40863-024-00471-2#ref-CR98
[59]: /article/10.1007/s40863-024-00471-2#Sec9
[60]: /article/10.1007/s40863-024-00471-2#ref-CR121
[61]: /article/10.1007/s40863-024-00471-2#ref-CR58
[62]: /article/10.1007/s40863-024-00471-2#ref-CR17
[63]: /article/10.1007/s40863-024-00471-2#ref-CR143
[64]: /article/10.1007/s40863-024-00471-2#ref-CR73
[65]: /article/10.1007/s40863-024-00471-2#ref-CR54
[66]: /article/10.1007/s40863-024-00471-2#ref-CR56
[67]: /article/10.1007/s40863-024-00471-2#ref-CR65
[68]: /article/10.1007/s40863-024-00471-2#ref-CR77
[69]: /article/10.1007/s40863-024-00471-2#ref-CR107
[70]: /article/10.1007/s40863-024-00471-2#ref-CR142
[71]: /article/10.1007/s40863-024-00471-2#ref-CR28
[72]: /article/10.1007/s40863-024-00471-2#ref-CR124
[73]: /article/10.1007/s40863-024-00471-2#ref-CR11
[74]: /article/10.1007/s40863-024-00471-2#ref-CR12
[75]: /article/10.1007/s40863-024-00471-2#ref-CR116
[76]: /article/10.1007/s40863-024-00471-2#ref-CR117
[77]: /article/10.1007/s40863-024-00471-2#ref-CR32
[78]: /article/10.1007/s40863-024-00471-2#ref-CR92
[79]: /article/10.1007/s40863-024-00471-2#ref-CR115
[80]: /article/10.1007/s40863-024-00471-2#ref-CR119
[81]: /article/10.1007/s40863-024-00471-2#ref-CR34
[82]: /article/10.1007/s40863-024-00471-2#ref-CR3
[83]: /article/10.1007/s40863-024-00471-2#ref-CR103
[84]: /article/10.1007/s40863-024-00471-2#ref-CR93
[85]: /article/10.1007/s40863-024-00471-2#ref-CR24
[86]: /article/10.1007/s40863-024-00471-2#ref-CR9
[87]: /article/10.1007/s40863-024-00471-2#ref-CR10
[88]: /article/10.1007/s40863-024-00471-2#ref-CR31
[89]: /article/10.1007/s40863-024-00471-2#ref-CR33
[90]: /article/10.1007/s40863-024-00471-2#ref-CR50
[91]: /article/10.1007/s40863-024-00471-2#ref-CR112
[92]: /article/10.1007/s40863-024-00471-2#ref-CR136
[93]: /article/10.1007/s40863-024-00471-2#ref-CR141
[94]: /article/10.1007/s40863-024-00471-2#ref-CR30
[95]: /article/10.1007/s40863-024-00471-2#ref-CR63
[96]: /article/10.1007/s40863-024-00471-2#ref-CR64
[97]: /article/10.1007/s40863-024-00471-2#ref-CR60
[98]: /article/10.1007/s40863-024-00471-2#ref-CR29
[99]: /article/10.1007/s40863-024-00471-2#ref-CR38
[100]: /article/10.1007/s40863-024-00471-2#ref-CR113
[101]: /article/10.1007/s40863-024-00471-2#Equ3
[102]: /article/10.1007/s40863-024-00471-2#Fig2
[103]: /article/10.1007/s40863-024-00471-2/figures/2
[104]: /article/10.1007/s40863-024-00471-2#FPar2
[105]: /article/10.1007/s40863-024-00471-2#ref-CR104
[106]: /article/10.1007/s40863-024-00471-2#ref-CR109
[107]: /article/10.1007/s40863-024-00471-2#ref-CR15
[108]: /article/10.1007/s40863-024-00471-2#ref-CR49
[109]: /article/10.1007/s40863-024-00471-2#ref-CR114
[110]: /article/10.1007/s40863-024-00471-2#ref-CR57
[111]: /article/10.1007/s40863-024-00471-2#ref-CR110
[112]: /article/10.1007/s40863-024-00471-2#Equ4
[113]: /article/10.1007/s40863-024-00471-2#Equ6
[114]: /article/10.1007/s40863-024-00471-2#ref-CR35
[115]: /article/10.1007/s40863-024-00471-2#ref-CR62
[116]: /article/10.1007/s40863-024-00471-2#Equ7
[117]: /article/10.1007/s40863-024-00471-2#ref-CR22
[118]: /article/10.1007/s40863-024-00471-2#ref-CR23
[119]: /article/10.1007/s40863-024-00471-2#ref-CR101
[120]: /article/10.1007/s40863-024-00471-2#ref-CR108
[121]: /article/10.1007/s40863-024-00471-2#ref-CR131
[122]: /article/10.1007/s40863-024-00471-2#ref-CR132
[123]: /article/10.1007/s40863-024-00471-2#ref-CR16
[124]: /article/10.1007/s40863-024-00471-2#ref-CR84
[125]: /article/10.1007/s40863-024-00471-2#ref-CR1
[126]: /article/10.1007/s40863-024-00471-2#Equ8
[127]: /article/10.1007/s40863-024-00471-2#ref-CR27
[128]: /article/10.1007/s40863-024-00471-2#ref-CR90
[129]: /article/10.1007/s40863-024-00471-2#ref-CR14
[130]: /article/10.1007/s40863-024-00471-2#ref-CR55
[131]: /article/10.1007/s40863-024-00471-2#ref-CR81
[132]: /article/10.1007/s40863-024-00471-2#ref-CR138
[133]: /article/10.1007/s40863-024-00471-2#ref-CR97
[134]: /article/10.1007/s40863-024-00471-2#FPar7
[135]: /article/10.1007/s40863-024-00471-2#ref-CR102
[136]: /article/10.1007/s40863-024-00471-2#Equ10
[137]: /article/10.1007/s40863-024-00471-2#Equ9
[138]: /article/10.1007/s40863-024-00471-2#FPar8
[139]: /article/10.1007/s40863-024-00471-2#FPar3
[140]: /article/10.1007/s40863-024-00471-2#FPar5
[141]: /article/10.1007/s40863-024-00471-2#ref-CR4
[142]: /article/10.1007/s40863-024-00471-2#ref-CR19
[143]: /article/10.1007/s40863-024-00471-2#ref-CR66
[144]: /article/10.1007/s40863-024-00471-2#ref-CR69
[145]: /article/10.1007/s40863-024-00471-2#FPar10
[146]: /article/10.1007/s40863-024-00471-2#ref-CR8
[147]: /article/10.1007/s40863-024-00471-2#ref-CR89
[148]: /article/10.1007/s40863-024-00471-2#Equ13
[149]: /article/10.1007/s40863-024-00471-2#Equ11
[150]: /article/10.1007/s40863-024-00471-2#ref-CR41
[151]: /article/10.1007/s40863-024-00471-2#Equ12
[152]: /article/10.1007/s40863-024-00471-2#Equ14
[153]: /article/10.1007/s40863-024-00471-2#Equ5
[154]: /article/10.1007/s40863-024-00471-2#Equ15
[155]: /article/10.1007/s40863-024-00471-2#ref-CR82
[156]: /article/10.1007/s40863-024-00471-2#ref-CR105
[157]: /article/10.1007/s40863-024-00471-2#ref-CR40
[158]: /article/10.1007/s40863-024-00471-2#ref-CR42
[159]: /article/10.1007/s40863-024-00471-2#ref-CR18
[160]: /article/10.1007/s40863-024-00471-2#Equ16
[161]: /article/10.1007/s40863-024-00471-2#Equ17
[162]: /article/10.1007/s40863-024-00471-2#ref-CR91
[163]: /article/10.1007/s40863-024-00471-2#ref-CR6
[164]: /article/10.1007/s40863-024-00471-2#ref-CR68
[165]: /article/10.1007/s40863-024-00471-2#FPar15
[166]: /article/10.1007/s40863-024-00471-2#ref-CR100
[167]: /article/10.1007/s40863-024-00471-2#ref-CR133
[168]: /article/10.1007/s40863-024-00471-2#ref-CR111
[169]: /article/10.1007/s40863-024-00471-2#ref-CR85
[170]: /article/10.1007/s40863-024-00471-2#ref-CR43
[171]: /article/10.1007/s40863-024-00471-2#ref-CR99
[172]: /article/10.1007/s40863-024-00471-2#ref-CR21
[173]: /article/10.1007/s40863-024-00471-2#ref-CR75
[174]: /article/10.1007/s40863-024-00471-2#Sec4
[175]: /article/10.1007/s40863-024-00471-2#Equ18
[176]: /article/10.1007/s40863-024-00471-2#Equ19
[177]: /article/10.1007/s40863-024-00471-2#Equ20
[178]: /article/10.1007/s40863-024-00471-2#Equ21
[179]: /article/10.1007/s40863-024-00471-2#ref-CR36
[180]: /article/10.1007/s40863-024-00471-2#ref-CR135
[181]: /article/10.1007/s40863-024-00471-2#Fig3
[182]: /article/10.1007/s40863-024-00471-2/figures/3
[183]: /article/10.1007/s40863-024-00471-2#ref-CR140
[184]: /article/10.1007/s40863-024-00471-2#ref-CR139
[185]: /article/10.1007/s40863-024-00471-2#FPar20
[186]: /article/10.1007/s40863-024-00471-2#ref-CR25
[187]: /article/10.1007/s40863-024-00471-2#ref-CR2
[188]: /article/10.1007/s40863-024-00471-2#ref-CR20
[189]: /article/10.1007/s40863-024-00471-2#ref-CR39
[190]: /article/10.1007/s40863-024-00471-2#ref-CR48
[191]: /article/10.1007/s40863-024-00471-2#ref-CR72
[192]: /article/10.1007/s40863-024-00471-2#ref-CR74
[193]: /article/10.1007/s40863-024-00471-2#ref-CR78
[194]: /article/10.1007/s40863-024-00471-2#ref-CR7
[195]: /article/10.1007/s40863-024-00471-2#ref-CR37
[196]: /article/10.1007/s40863-024-00471-2#ref-CR44
[197]: /article/10.1007/s40863-024-00471-2#Equ22
[198]: /article/10.1007/s40863-024-00471-2#Equ23
[199]: /article/10.1007/s40863-024-00471-2#FPar13
[200]: /article/10.1007/s40863-024-00471-2#Equ25
[201]: /article/10.1007/s40863-024-00471-2#Equ24
[202]: /article/10.1007/s40863-024-00471-2#Equ26
[203]: http://www.ams.org/mathscinet-getitem?mr=4484088
[204]: http://scholar.google.com/scholar_lookup?amp;title=Planar%20systems%20and%20Abel%20equations&amp;journal=Commun.%20Pure%20Appl.%20Anal.&amp;volume=21&amp;issue=10&amp;pages=3463-3478&amp;publication_year=2022&amp;author=%C3%81lvarez%2CA&amp;author=Bravo%2CJL&amp;author=S%C3%A1nchez%2CF
[205]: http://www.ams.org/mathscinet-getitem?mr=4053594
[206]: http://scholar.google.com/scholar_lookup?amp;title=Asymptotic%20lower%20bounds%20on%20Hilbert%20numbers%20using%20canard%20cycles&amp;journal=J.%20Differ.%20Equ.&amp;volume=268&amp;issue=7&amp;pages=3370-3391&amp;publication_year=2020&amp;author=%C3%81lvarez%2CMJ&amp;author=Coll%2CB&amp;author=Maesschalck%2CP&amp;author=Prohens%2CR
[207]: http://www.ams.org/mathscinet-getitem?mr=2298969
[208]: http://scholar.google.com/scholar_lookup?amp;title=A%20new%20uniqueness%20criterion%20for%20the%20number%20of%20periodic%20orbits%20of%20Abel%20equations&amp;journal=J.%20Differ.%20Equ.&amp;volume=234&amp;issue=1&amp;pages=161-176&amp;publication_year=2007&amp;author=%C3%81lvarez%2CMJ&amp;author=Gasull%2CA&amp;author=Giacomini%2CH
[209]: http://www.ams.org/mathscinet-getitem?mr=2965226
[210]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20for%20two%20families%20of%20cubic%20systems&amp;journal=Nonlinear%20Anal.%2C%20Theory%20Methods%20Appl.%20Ser.%20A%2C%20Theory%20Methods&amp;volume=75&amp;issue=18&amp;pages=6402-6417&amp;publication_year=2012&amp;author=%C3%81lvarez%2CMJ&amp;author=Gasull%2CA&amp;author=Prohens%2CR
[211]: http://www.ams.org/mathscinet-getitem?mr=2440830
[212]: http://scholar.google.com/scholar_lookup?amp;title=Lower%20bounds%20for%20the%20number%20of%20limit%20cycles%20of%20trigonometric%20Abel%20equations&amp;journal=J.%20Math.%20Anal.%20Appl.&amp;volume=342&amp;pages=682-693&amp;publication_year=2008&amp;author=%C3%81lvarez%2CMJ&amp;author=Gasull%2CA&amp;author=Yu%2CJ
[213]: http://scholar.google.com/scholar_lookup?amp;title=Non-autonomous%20equations%20related%20to%20polynomial%20two-dimensional%20systems&amp;journal=Proc.%20R.%20Soc.%20Edinb.&amp;volume=105A&amp;pages=129-152&amp;publication_year=1987&amp;author=Alwash%2CMAM&amp;author=Lloyd%2CNG
[214]: http://www.ams.org/mathscinet-getitem?mr=2305999
[215]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20determination%20of%20the%20number%20of%20periodic%20%28or%20closed%29%20solutions%20of%20a%20scalar%20differential%20equation%20with%20convexity&amp;journal=J.%20Math.%20Anal.%20Appl.&amp;volume=331&amp;pages=206-219&amp;publication_year=2007&amp;author=Andersen%2CKM&amp;author=Sandqvist%2CA
[216]: http://www.ams.org/mathscinet-getitem?mr=832735
[217]: http://scholar.google.com/scholar_lookup?amp;title=Solution%20of%20Dulac%E2%80%99s%20problem%20for%20quadratic%20vector%20fields&amp;journal=An.%20Acad.%20Bras.%20Ci%C3%AAnc.&amp;volume=57&amp;pages=265-266&amp;publication_year=1985&amp;author=Bam%C3%B3n%2CR
[218]: http://www.ams.org/mathscinet-getitem?mr=876161
[219]: http://scholar.google.com/scholar_lookup?amp;title=Quadratic%20vector%20fields%20in%20the%20plane%20have%20a%20finite%20number%20of%20limit%20cycles&amp;journal=Publ.%20Math.%2C%20Inst.%20Hautes%20%C3%89tud.%20Sci.&amp;volume=64&amp;pages=111-142&amp;publication_year=1986&amp;author=Bam%C3%B3n%2CR
[220]: http://scholar.google.com/scholar_lookup?amp;title=Biophysics%20of%20complex%20systems.%20Rigid%20regime%20of%20excitation%20of%20auto-oscillations%20in%20a%20model%20of%20the%20Volterra%20type&amp;journal=Biophysics&amp;volume=5&amp;pages=866-869&amp;publication_year=1981&amp;author=Bazykin%2CAD&amp;author=Khibnik%2CAI
[221]: http://www.ams.org/mathscinet-getitem?mr=2395031
[222]: http://scholar.google.com/scholar_lookup?amp;title=Qualitative%20tools%20for%20studying%20periodic%20solutions%20and%20bifurcations%20as%20applied%20to%20the%20periodically%20harvested%20logistic%20equation&amp;journal=Am.%20Math.%20Mon.&amp;volume=115&amp;pages=202-219&amp;publication_year=2008&amp;author=Benardete%2CDM&amp;author=Noonburg%2CVW&amp;author=Pollina%2CB
[223]: http://scholar.google.com/scholar_lookup?amp;title=The%20Riccati%20Equation&amp;publication_year=1991
[224]: http://scholar.google.com/scholar_lookup?amp;title=The%20number%20of%20small-amplitude%20limit%20cycles%20of%20Li%C3%A9nard%20equations&amp;journal=Math.%20Proc.%20Camb.%20Philos.%20Soc.&amp;volume=95&amp;pages=359-366&amp;publication_year=1984&amp;author=Blows%2CTR&amp;author=Lloyd%2CNG
[225]: http://www.ams.org/mathscinet-getitem?mr=3870586
[226]: http://scholar.google.com/scholar_lookup?amp;title=Periodic%20solutions%20of%20linear%2C%20Riccati%2C%20and%20Abel%20dynamic%20equations&amp;journal=J.%20Math.%20Anal.%20Appl.&amp;volume=470&amp;issue=2&amp;pages=733-749&amp;publication_year=2019&amp;author=Bohner%2CM&amp;author=Gasull%2CA&amp;author=Valls%2CC
[227]: http://www.ams.org/mathscinet-getitem?mr=2583153
[228]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20for%20some%20Abel%20equations%20having%20coefficients%20without%20fixed%20signs&amp;journal=Int.%20J.%20Bifurc.%20Chaos%20Appl.%20Sci.%20Eng.&amp;volume=19&amp;issue=11&amp;pages=3869-3876&amp;publication_year=2009&amp;author=Bravo%2CJL&amp;author=Fern%C3%A1ndez%2CM&amp;author=Gasull%2CA
[229]: http://www.ams.org/mathscinet-getitem?mr=3918182
[230]: http://scholar.google.com/scholar_lookup?amp;title=Uniqueness%20of%20limit%20cycles%20for%20quadratic%20vector%20fields&amp;journal=Discrete%20Contin.%20Dyn.%20Syst.&amp;volume=39&amp;issue=1&amp;pages=483-502&amp;publication_year=2019&amp;author=Bravo%2CJL&amp;author=Fern%C3%A1ndez%2CM&amp;author=Ojeda%2CI&amp;author=S%C3%A1nchez%2CF
[231]: http://www.ams.org/mathscinet-getitem?mr=2276339
[232]: http://scholar.google.com/scholar_lookup?amp;title=Periodic%20solutions%20of%20a%20periodic%20scalar%20piecewise%20ODE&amp;journal=Commun.%20Pure%20Appl.%20Anal.&amp;volume=6&amp;issue=1&amp;pages=213-228&amp;publication_year=2007&amp;author=Bravo%2CJL&amp;author=Fern%C3%A1ndez%2CM&amp;author=Tineo%2CA
[233]: http://scholar.google.com/scholar_lookup?amp;title=M%C3%B6bius%20transformations%20and%20periodic%20solutions%20of%20complex%20Riccati%20equations%20Bull&amp;journal=Lond.%20Math.%20Soc.&amp;volume=29&amp;issue=2&amp;pages=205-215&amp;publication_year=1997&amp;author=Campos%2CJ
[234]: http://www.ams.org/mathscinet-getitem?mr=1364046
[235]: http://scholar.google.com/scholar_lookup?amp;title=Nonexistence%20of%20periodic%20solutions%20of%20a%20complex%20Riccati%20equation&amp;journal=Differ.%20Integral%20Equ.&amp;volume=9&amp;issue=2&amp;pages=247-249&amp;publication_year=1996&amp;author=Campos%2CJ&amp;author=Ortega%2CR
[236]: http://www.ams.org/mathscinet-getitem?mr=3950039
[237]: http://scholar.google.com/scholar_lookup?amp;title=Bifurcations%20of%20limit%20cycles%20in%20complex%20networks%20of%20Hamiltonian%20systems%20and%20Lloyd%E2%80%99s%20conjecture&amp;journal=J.%20Math.%20Anal.%20Appl.&amp;volume=477&amp;issue=1&amp;pages=272-293&amp;publication_year=2019&amp;author=Cantin%2CG
[238]: http://www.ams.org/mathscinet-getitem?mr=952336
[239]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20of%20a%20class%20of%20polynomial%20systems&amp;journal=Proc.%20R.%20Soc.%20Edinb.%20Sect.%20A&amp;volume=109&amp;pages=187-199&amp;publication_year=1988&amp;author=Carbonell%2CM&amp;author=Llibre%2CJ
[240]: http://scholar.google.com/scholar_lookup?amp;title=Abel%20ODEs%3A%20Equivalence%20and%20integrable%20classes&amp;journal=Comput.%20Phys.%20Commun.&amp;volume=130&amp;pages=204-231&amp;publication_year=2000&amp;author=Cheb-Terrab%2CES&amp;author=Roche%2CAD
[241]: http://www.ams.org/mathscinet-getitem?mr=559742
[242]: http://scholar.google.com/scholar_lookup?amp;title=The%20relative%20position%20and%20number%20of%20limit%20cycles%20of%20the%20quadratic%20differential%20system&amp;journal=Acta%20Math.%20Sin.&amp;volume=22&amp;pages=751-758&amp;publication_year=1979&amp;author=Chen%2CL&amp;author=Wang%2CM
[243]: http://scholar.google.com/scholar_lookup?amp;title=Estimation%20of%20the%20number%20of%20limit%20cycles%20of%20autonomous%20systems&amp;journal=Differ.%20Equ.&amp;volume=13&amp;pages=529-547&amp;publication_year=1977&amp;author=Cherkas%2CLA
[244]: http://www.ams.org/mathscinet-getitem?mr=1616471
[245]: http://scholar.google.com/scholar_lookup?amp;title=Dulac%20function%20for%20polynomial%20autonomous%20systems%20on%20a%20plane&amp;journal=Differ.%20Equ.&amp;volume=33&amp;pages=692-701&amp;publication_year=1997&amp;author=Cherkas%2CLA
[246]: http://scholar.google.com/scholar_lookup?amp;title=Ordinary%20Differential%20Equations%20with%20Applications&amp;publication_year=2006&amp;author=Chicone%2CC
[247]: http://www.ams.org/mathscinet-getitem?mr=701513
[248]: http://scholar.google.com/scholar_lookup?amp;title=Separatrix%20and%20limit%20cycles%20of%20quadratic%20systems%20and%20Dulac%E2%80%99s%20theorem&amp;journal=Trans.%20Am.%20Math.%20Soc.&amp;volume=278&amp;pages=585-612&amp;publication_year=1983&amp;author=Chicone%2CC&amp;author=Shafer%2CDS
[249]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20Cycles%20of%20Differential%20Equations&amp;publication_year=2024&amp;author=Christopher%2CCJ&amp;author=Li%2CC&amp;author=Torregrosa%2CJ
[250]: http://www.ams.org/mathscinet-getitem?mr=1349062
[251]: http://scholar.google.com/scholar_lookup?amp;title=Polynomial%20systems%3A%20a%20lower%20bound%20for%20the%20Hilbert%20numbers&amp;journal=Proc.%20R.%20Soc.%20Lond.%20Ser.%20A&amp;volume=450&amp;pages=219-224&amp;publication_year=1995&amp;author=Christopher%2CCJ&amp;author=Lloyd%2CNG
[252]: http://www.ams.org/mathscinet-getitem?mr=2228837
[253]: http://scholar.google.com/scholar_lookup?amp;title=Dynamics%20of%20some%20rational%20discrete%20dynamical%20systems%20via%20invariants%2C&amp;journal=Int.%20J.%20Bifur.%20Chaos%20Appl.%20Sci.%20Eng.&amp;volume=16&amp;issue=3&amp;pages=631-645&amp;publication_year=2006&amp;author=Cima%2CA&amp;author=Gasull%2CA&amp;author=Ma%C3%B1osa%2CV
[254]: http://www.ams.org/mathscinet-getitem?mr=2281199
[255]: http://scholar.google.com/scholar_lookup?amp;title=Periodic%20orbits%20in%20complex%20Abel%20equations&amp;journal=J.%20Differ.%20Equ.&amp;volume=232&amp;pages=314-328&amp;publication_year=2007&amp;author=Cima%2CA&amp;author=Gasull%2CA&amp;author=Ma%C3%B1osas%2CF
[256]: http://www.ams.org/mathscinet-getitem?mr=2990073
[257]: http://scholar.google.com/scholar_lookup?amp;title=A%20simple%20solution%20of%20some%20composition%20conjectures%20for%20Abel%20equations&amp;journal=J.%20Math.%20Anal.%20Appl.&amp;volume=398&amp;pages=477-486&amp;publication_year=2013&amp;author=Cima%2CA&amp;author=Gasull%2CA&amp;author=Ma%C3%B1osas%2CF
[258]: http://www.ams.org/mathscinet-getitem?mr=3513586
[259]: http://scholar.google.com/scholar_lookup?amp;title=Periods%20of%20solutions%20of%20periodic%20differential%20equations&amp;journal=Differ.%20Integral%20Equ.&amp;volume=29&amp;issue=9%E2%80%9310&amp;pages=905-922&amp;publication_year=2016&amp;author=Cima%2CA&amp;author=Gasull%2CA&amp;author=Ma%C3%B1osas%2CF
[260]: http://www.ams.org/mathscinet-getitem?mr=884276
[261]: http://scholar.google.com/scholar_lookup?amp;title=Some%20theorems%20on%20the%20existence%2C%20uniqueness%2C%20and%20nonexistence%20of%20limit%20cycles%20for%20quadratic%20systems&amp;journal=J.%20Differ.%20Equ.&amp;volume=67&amp;pages=372-399&amp;publication_year=1987&amp;author=Coll%2CB&amp;author=Gasull%2CA&amp;author=Llibre%2CJ
[262]: http://www.ams.org/mathscinet-getitem?mr=1422117
[263]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20for%20nonsmooth%20differential%20equations%20via%20Schwarzian%20derivative&amp;journal=J.%20Differ.%20Equ.&amp;volume=132&amp;pages=203-221&amp;publication_year=1996&amp;author=Coll%2CB&amp;author=Gasull%2CA&amp;author=Prohens%2CR
[264]: http://www.ams.org/mathscinet-getitem?mr=1447489
[265]: http://scholar.google.com/scholar_lookup?amp;title=Differential%20equations%20defined%20by%20the%20sum%20of%20two%20quasi-homogeneous%20vector%20fields&amp;journal=Can.%20J.%20Math.&amp;volume=49&amp;pages=212-231&amp;publication_year=1997&amp;author=Coll%2CB&amp;author=Gasull%2CA&amp;author=Prohens%2CR
[266]: http://www.ams.org/mathscinet-getitem?mr=2379379
[267]: http://scholar.google.com/scholar_lookup?amp;title=Simple%20non-autonomous%20differential%20equations%20with%20many%20limit%20cycles&amp;journal=Commun.%20Appl.%20Nonlinear%20Anal.&amp;volume=15&amp;pages=29-34&amp;publication_year=2008&amp;author=Coll%2CB&amp;author=Gasull%2CA&amp;author=Prohens%2CR
[268]: http://www.ams.org/mathscinet-getitem?mr=2972562
[269]: http://scholar.google.com/scholar_lookup?amp;title=Periodic%20orbits%20for%20perturbed%20non-autonomous%20differential%20equations&amp;journal=Bull.%20Sci.%20Math.&amp;volume=136&amp;issue=7&amp;pages=803-819&amp;publication_year=2012&amp;author=Coll%2CB&amp;author=Gasull%2CA&amp;author=Prohens%2CR
[270]: http://www.ams.org/mathscinet-getitem?mr=196182
[271]: http://scholar.google.com/scholar_lookup?amp;title=A%20survey%20of%20quadratic%20systems&amp;journal=J.%20Differ.%20Equ.&amp;volume=2&amp;pages=293-304&amp;publication_year=1966&amp;author=Coppel%2CWA
[272]: http://scholar.google.com/scholar_lookup?amp;title=Classical%20Li%C3%A9nard%20equations%20of%20degree%20%24%24n%5Cge%206%24%24%20n%20%E2%89%A5%206%20can%20have%20%24%24%5B%28n-1%29%2F2%5D%2B2%24%24%20%5B%20%28%20n%20-%201%20%29%20%2F%202%20%5D%20%2B%202%20limit%20cycles&amp;journal=J.%20Differ.%20Equ.&amp;volume=250&amp;issue=4&amp;pages=2162-2176&amp;publication_year=2011&amp;author=Maesschalck%2CP&amp;author=Dumortier%2CF
[273]: http://scholar.google.com/scholar_lookup?amp;title=Slow%20divergence%20integrals%20in%20classical%20Li%C3%A9nard%20equations%20near%20centers&amp;journal=J.%20Dyn.%20Differ.%20Equ.&amp;volume=27&amp;issue=1&amp;pages=177-185&amp;publication_year=2015&amp;author=Maesschalck%2CP&amp;author=Huzak%2CR
[274]: http://www.ams.org/mathscinet-getitem?mr=1633961
[275]: http://scholar.google.com/scholar_lookup?amp;title=Cubic%20systems%20and%20Abel%20equations&amp;journal=J.%20Differ.%20Equ.&amp;volume=147&amp;pages=435-454&amp;publication_year=1998&amp;author=Devlin%2CJ&amp;author=Lloyd%2CNG&amp;author=Pearson%2CJM
[276]: http://scholar.google.com/scholar_lookup?amp;title=Qualitative%20Theory%20of%20Planar%20Differential%20Systems&amp;publication_year=2006&amp;author=Dumortier%2CF&amp;author=Llibre%2CJ&amp;author=Art%C3%A9s%2CJC
[277]: http://scholar.google.com/scholar_lookup?amp;title=More%20limit%20cycles%20than%20expected%20in%20Li%C3%A9nard%20equations&amp;journal=Proc.%20Am.%20Math.%20Soc.&amp;volume=135&amp;issue=6&amp;pages=1895-1904&amp;publication_year=2007&amp;author=Dumortier%2CF&amp;author=Panazzolo%2CD&amp;author=Roussarie%2CR
[278]: http://www.ams.org/mathscinet-getitem?mr=1275749
[279]: http://scholar.google.com/scholar_lookup?amp;title=Hilbert%E2%80%99s%2016th%20problem%20for%20quadratic%20vector%20fields&amp;journal=J.%20Differ.%20Equ.&amp;volume=110&amp;issue=1&amp;pages=86-133&amp;publication_year=1994&amp;author=Dumortier%2CF&amp;author=Roussarie%2CR&amp;author=Rousseau%2CC
[280]: http://scholar.google.com/scholar_lookup?amp;title=Introduction%20aux%20fonctions%20analysables%20et%20preuve%20constructive%20de%20la%20conjecture%20de%20Dulac%2C%20in%20French&amp;publication_year=1992&amp;author=%C3%89calle%2CJ
[281]: http://www.ams.org/mathscinet-getitem?mr=2514940
[282]: http://scholar.google.com/scholar_lookup?amp;title=Iterative%20approximation%20of%20limit%20cycles%20for%20a%20class%20of%20Abel%20equations&amp;journal=Phys.%20D&amp;volume=237&amp;pages=3159-3164&amp;publication_year=2008&amp;author=Fossas%2CE&amp;author=Olm%2CJM&amp;author=Sira-Ram%C3%ADrez%2CH
[283]: http://www.ams.org/mathscinet-getitem?mr=2135581
[284]: http://scholar.google.com/scholar_lookup?amp;title=Transcendental%20limit%20cycles%20via%20the%20structure%20of%20arbitrary%20degree%20invariant%20algebraic%20curves%20of%20polynomial%20planar%20vector%20fields&amp;journal=Rocky%20Mt.%20J.%20Math.&amp;volume=35&amp;issue=2&amp;pages=501-515&amp;publication_year=2005&amp;author=Garc%C3%ADa%2CIA
[285]: http://scholar.google.com/scholar_lookup?amp;title=Lines%20of%20principal%20curvature%20on%20canal%20surfaces%20in%20%24%24%7B%5Cmathbb%7BR%7D%20%7D%5E3%2C%24%24%20R%203%20%2C%20An&amp;journal=Acad.%20Bras.%20Ci%C3%AAnc.&amp;volume=78&amp;issue=3&amp;pages=405-415&amp;publication_year=2006&amp;author=Garcia%2CR&amp;author=Llibre%2CJ&amp;author=Sotomayor%2CJ
[286]: http://scholar.google.com/scholar_lookup?amp;title=From%20Abel%E2%80%99s%20differential%20equations%20to%20Hilbert%E2%80%99s%20XVIth%20problem&amp;journal=Butll.%20Soc.%20Catalana%20Mat.&amp;volume=28&amp;issue=2&amp;pages=123-146&amp;publication_year=2013&amp;author=Gasull%2CA
[287]: http://www.ams.org/mathscinet-getitem?mr=4297215
[288]: http://scholar.google.com/scholar_lookup?amp;title=Some%20open%20problems%20in%20low%20dimensional%20dynamical%20systems&amp;journal=SeMA%20J.&amp;volume=78&amp;issue=3&amp;pages=233-269&amp;publication_year=2021&amp;author=Gasull%2CA
[289]: http://www.ams.org/mathscinet-getitem?mr=4330162
[290]: http://scholar.google.com/scholar_lookup?amp;title=Effectiveness%20of%20the%20Bendixson%E2%80%93Dulac%20theorem&amp;journal=J.%20Differ.%20Equ.&amp;volume=305&amp;pages=347-367&amp;publication_year=2021&amp;author=Gasull%2CA&amp;author=Giacomini%2CH
[291]: http://www.ams.org/mathscinet-getitem?mr=2276844
[292]: http://scholar.google.com/scholar_lookup?amp;title=Explicit%20non-algebraic%20limit%20cycles%20for%20polynomial%20systems&amp;journal=J.%20Comput.%20Appl.%20Math.&amp;volume=200&amp;issue=1&amp;pages=448-457&amp;publication_year=2007&amp;author=Gasull%2CA&amp;author=Giacomini%2CH&amp;author=Torregrosa%2CJ
[293]: http://www.ams.org/mathscinet-getitem?mr=2295352
[294]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20for%20generalized%20Abel%20equations&amp;journal=Int.%20J.%20Bifur.%20Chaos%20Appl.%20Sci.%20Eng.&amp;volume=16&amp;pages=3737-3745&amp;publication_year=2006&amp;author=Gasull%2CA&amp;author=Guillamon%2CA
[295]: http://www.ams.org/mathscinet-getitem?mr=1461648
[296]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20in%20the%20Holling%E2%80%93Tanner%20model&amp;journal=Publ.%20Mat.&amp;volume=41&amp;issue=1&amp;pages=149-167&amp;publication_year=1997&amp;author=Gasull%2CA&amp;author=Kooij%2CRE&amp;author=Torregrosa%2CJ
[297]: http://www.ams.org/mathscinet-getitem?mr=2853554
[298]: http://scholar.google.com/scholar_lookup?amp;title=A%20new%20Chebyshev%20family%20with%20applications%20to%20Abel%20equations&amp;journal=J.%20Differ.%20Equ.&amp;volume=252&amp;pages=1635-1641&amp;publication_year=2012&amp;author=Gasull%2CA&amp;author=Li%2CC&amp;author=Torregrosa%2CJ
[299]: http://www.ams.org/mathscinet-getitem?mr=1062402
[300]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20for%20a%20class%20of%20Abel%20equations&amp;journal=SIAM%20J.%20Math.%20Anal.&amp;volume=21&amp;pages=1235-1244&amp;publication_year=1990&amp;author=Gasull%2CA&amp;author=Llibre%2CJ
[301]: http://www.ams.org/mathscinet-getitem?mr=878253
[302]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20of%20vector%20fields%20of%20the%20form%20%24%24X%28v%29%20%3D%20Av%20%2B%20f%20%28v%29Bv%24%24%20X%20%28%20v%20%29%20%3D%20A%20v%20%2B%20f%20%28%20v%20%29%20B%20v&amp;journal=J.%20Differ.%20Equ.&amp;volume=67&amp;pages=90-110&amp;publication_year=1987&amp;author=Gasull%2CA&amp;author=Llibre%2CJ&amp;author=Sotomayor%2CJ
[303]: http://www.ams.org/mathscinet-getitem?mr=885813
[304]: http://scholar.google.com/scholar_lookup?amp;title=Further%20considerations%20on%20the%20number%20of%20limit%20cycles%20of%20vector%20fields%20of%20the%20form%20%24%24X%28v%29%20%3D%20Av%20%2B%20f%20%28v%29Bv%24%24%20X%20%28%20v%20%29%20%3D%20A%20v%20%2B%20f%20%28%20v%20%29%20B%20v&amp;journal=J.%20Differ.%20Equ.&amp;volume=68&amp;pages=36-40&amp;publication_year=1987&amp;author=Gasull%2CA&amp;author=Llibre%2CJ&amp;author=Sotomayor%2CJ
[305]: http://www.ams.org/mathscinet-getitem?mr=2122224
[306]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20for%20rigid%20cubic%20systems&amp;journal=J.%20Math.%20Anal.%20Appl.&amp;volume=303&amp;pages=391-404&amp;publication_year=2005&amp;author=Gasull%2CA&amp;author=Prohens%2CR&amp;author=Torregrosa%2CJ
[307]: http://www.ams.org/mathscinet-getitem?mr=1895296
[308]: http://scholar.google.com/scholar_lookup?amp;title=A%20relation%20between%20small%20amplitude%20and%20big%20limit%20cycles&amp;journal=Rocky%20Mt.%20J.%20Math.&amp;volume=31&amp;issue=4&amp;pages=1277-1303&amp;publication_year=2001&amp;author=Gasull%2CA&amp;author=Torregrosa%2CJ
[309]: http://www.ams.org/mathscinet-getitem?mr=3056437
[310]: http://scholar.google.com/scholar_lookup?amp;title=On%20a%20family%20of%20polynomial%20differential%20equations%20having%20at%20most%20three%20limit%20cycles&amp;journal=Houston%20J.%20Math.&amp;volume=3&amp;issue=1&amp;pages=191-203&amp;publication_year=2013&amp;author=Gasull%2CA&amp;author=Zhao%2CY
[311]: http://www.ams.org/mathscinet-getitem?mr=4550206
[312]: http://scholar.google.com/scholar_lookup?amp;title=Existence%20of%20at%20most%20two%20limit%20cycles%20for%20some%20non-autonomous%20differential%20equations&amp;journal=Commun.%20Pure%20Appl.%20Anal.&amp;volume=22&amp;issue=3&amp;pages=970-982&amp;publication_year=2023&amp;author=Gasull%2CA&amp;author=Zhao%2CY
[313]: http://www.ams.org/mathscinet-getitem?mr=1476640
[314]: http://scholar.google.com/scholar_lookup?amp;title=Number%20of%20limit%20cycles%20of%20the%20Li%C3%A9nard%20equation&amp;journal=Phys.%20Rev.%20E&amp;volume=56&amp;publication_year=1997&amp;author=Giacomini%2CH&amp;author=Neukirch%2CS
[315]: http://www.ams.org/mathscinet-getitem?mr=2250800
[316]: http://scholar.google.com/scholar_lookup?amp;title=Coexistence%20of%20algebraic%20and%20non-algebraic%20limit%20cycles%2C%20explicitly%20given%2C%20using%20Riccati%20equations&amp;journal=Nonlinearity&amp;volume=19&amp;issue=8&amp;pages=1939-1950&amp;publication_year=2006&amp;author=Gin%C3%A9%2CJ&amp;author=Grau%2CM
[317]: http://scholar.google.com/scholar_lookup?amp;title=Darboux%20Integrability%20and%20Limit%20Cycles%20for%20a%20Class%20of%20Polynomial%20Differential%20Systems%2C%20Differential%20Equations%20with%20Symbolic%20Computation%2C%2055%E2%80%9365&amp;publication_year=2005&amp;author=Gin%C3%A9%2CJ&amp;author=Llibre%2CJ
[318]: http://www.ams.org/mathscinet-getitem?mr=2020443
[319]: http://scholar.google.com/scholar_lookup?amp;title=Relativistic%20dissipative%20cosmological%20models%20and%20Abel%20differential%20equation&amp;journal=Comput.%20Math.%20Appl.&amp;volume=46&amp;pages=849-853&amp;publication_year=2003&amp;author=Harko%2CT&amp;author=Mak%2CMK
[320]: http://scholar.google.com/scholar_lookup?amp;title=Ordinary%20Differential%20Equations%20in%20the%20Complex%20Domain%2C%20Reprint%20of%20the%201976%20original&amp;publication_year=1997&amp;author=Hille%2CE
[321]: http://scholar.google.com/scholar_lookup?amp;title=Differential%20Equations%2C%20Dynamical%20Systems%2C%20and%20Linear%20Algebra%2C%20Pure%20and%20Applied%20Mathematics&amp;publication_year=1974&amp;author=Hirsch%2CMW&amp;author=Smale%2CS
[322]: http://scholar.google.com/scholar_lookup?amp;title=The%20Work%20of%20Niels%20Henrik%20Abel%2C%20The%20Legacy%20of%20Niels%20Henryk%20Abel-The%20Abel%20Bicentennial%2C%20Oslo%202002&amp;publication_year=2004&amp;author=Houzel%2CC
[323]: http://www.ams.org/mathscinet-getitem?mr=4165513
[324]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20limit%20cycles%20in%20generalized%20Abel%20equations&amp;journal=SIAM%20J.%20Appl.%20Dyn.%20Syst.&amp;volume=19&amp;issue=4&amp;pages=2343-2370&amp;publication_year=2020&amp;author=Huang%2CJ&amp;author=Torregrosa%2CJ&amp;author=Villadelprat%2CJ
[325]: http://scholar.google.com/scholar_lookup?amp;title=Cyclic%20phase%20changes%20of%20interstellar%20medium&amp;journal=Publ.%20Astron.%20Soc.%20Jpn.&amp;volume=35&amp;pages=77-86&amp;publication_year=1983&amp;author=Ikeuchi%2CS&amp;author=Tomita%2CH
[326]: http://www.ams.org/mathscinet-getitem?mr=1898209
[327]: http://scholar.google.com/scholar_lookup?amp;title=Centennial%20history%20of%20Hilbert%E2%80%99s%2016th%20problem&amp;journal=Bull.%20Am.%20Math.%20Soc.%20%28N.S.%29&amp;volume=39&amp;pages=301-354&amp;publication_year=2002&amp;author=Il%E2%80%99yashenko%2CY
[328]: http://scholar.google.com/scholar_lookup?amp;title=Analysis%20of%20Numerical%20Methods&amp;publication_year=1966&amp;author=Isaacson%2CE&amp;author=Keller%2CHB
[329]: http://scholar.google.com/scholar_lookup?amp;title=Differentialgleichungen%3A%20L%C3%B6sungsmethoden%20und%20L%C3%B6sungen%2C%20in%20German&amp;publication_year=1959&amp;author=Kamke%2CE
[330]: http://www.ams.org/mathscinet-getitem?mr=2515170
[331]: http://scholar.google.com/scholar_lookup?amp;title=A%20cubic%20system%20with%20thirteen%20limit%20cycles&amp;journal=J.%20Differ.%20Equ.&amp;volume=246&amp;pages=3609-3619&amp;publication_year=2009&amp;author=Li%2CC&amp;author=Liu%2CC&amp;author=Yang%2CJ
[332]: http://www.ams.org/mathscinet-getitem?mr=1897762
[333]: http://scholar.google.com/scholar_lookup?amp;title=Polynomial%20systems%3A%20a%20lower%20bound%20for%20the%20weakened%2016th%20Hilbert%20problem&amp;journal=Extr.%20Math.&amp;volume=16&amp;pages=441-447&amp;publication_year=2001&amp;author=Li%2CC&amp;author=Li%2CW&amp;author=Llibre%2CJ&amp;author=Zhang%2CZ
[334]: http://scholar.google.com/scholar_lookup?amp;title=Uniqueness%20of%20limit%20cycles%20for%20Li%C3%A9nard%20differential%20equations%20of%20degree%20four&amp;journal=J.%20Differ.%20Equ.&amp;volume=252&amp;pages=3142-3162&amp;publication_year=2012&amp;author=Li%2CC&amp;author=Llibre%2CJ
[335]: http://www.ams.org/mathscinet-getitem?mr=2990054
[336]: http://scholar.google.com/scholar_lookup?amp;title=Canard%20cycles%20for%20predator-prey%20systems%20with%20Holling%20types%20of%20functional%20response&amp;journal=J.%20Differ.%20Equ.&amp;volume=254&amp;pages=879-910&amp;publication_year=2013&amp;author=Li%2CC&amp;author=Zhu%2CH
[337]: http://www.ams.org/mathscinet-getitem?mr=1965270
[338]: http://scholar.google.com/scholar_lookup?amp;title=Hilbert%E2%80%99s%2016th%20problem%20and%20bifurcations%20of%20planar%20polynomial%20vector%20fields&amp;journal=Int.%20J.%20Bifur.%20Chaos%20Appl.%20Sci.%20Eng.&amp;volume=13&amp;pages=47-106&amp;publication_year=2003&amp;author=Li%2CJ
[339]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20solutions%20of%20the%20equation%20%24%24dx%2Fdt%3D%5Csum%20_%7Bj%3D0%7D%5E%7Bn%7Da_j%28t%29x%5Ej%24%24%20d%20x%20%2F%20d%20t%20%3D%20%E2%88%91%20j%20%3D%200%20n%20a%20j%20%28%20t%20%29%20x%20j%20%2C%20%24%240%5Cle%20t%5Cle%201%24%24%200%20%E2%89%A4%20t%20%E2%89%A4%201%20for%20which%20%24%24x%280%29%3Dx%281%29%24%24%20x%20%28%200%20%29%20%3D%20x%20%28%201%20%29&amp;journal=Inv.%20Math.&amp;volume=59&amp;pages=67-76&amp;publication_year=1980&amp;author=Lins%20Neto%2CA
[340]: http://scholar.google.com/scholar_lookup?amp;title=The%20number%20of%20periodic%20solutions%20of%20the%20equation%20%24%24z%5E%7B%5Cprime%20%7D%3Dz%5EN%2Bp_1%28t%29z%5E%7BN-1%7D%2B%5Ccdots%20%2Bp_N%28t%29%2C%24%24%20z%20%E2%80%B2%20%3D%20z%20N%20%2B%20p%201%20%28%20t%20%29%20z%20N%20-%201%20%2B%20%E2%8B%AF%20%2B%20p%20N%20%28%20t%20%29%20%2C&amp;journal=Proc.%20Lond.%20Math.%20Soc.&amp;volume=III&amp;issue=Ser.%2027&amp;pages=667-700&amp;publication_year=1973&amp;author=Lloyd%2CNG
[341]: http://www.ams.org/mathscinet-getitem?mr=367373
[342]: http://scholar.google.com/scholar_lookup?amp;title=On%20a%20class%20of%20differential%20equations%20of%20Riccati%20type&amp;journal=J.%20Lond.%20Math.%20Soc.&amp;volume=II&amp;issue=Ser.%2010&amp;pages=1-10&amp;publication_year=1975&amp;author=Lloyd%2CNG
[343]: http://www.ams.org/mathscinet-getitem?mr=551455
[344]: http://scholar.google.com/scholar_lookup?amp;title=A%20note%20on%20the%20number%20of%20limit%20cycles%20in%20certain%20two-dimensional%20systems&amp;journal=J.%20Lond.%20Math.%20Soc.&amp;volume=20&amp;pages=277-286&amp;publication_year=1979&amp;author=Lloyd%2CNG
[345]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20of%20polynomial%20systems-some%20recent%20developments.%20New%20directions%20in%20dynamical%20systems&amp;journal=Lond.%20Math.%20Soc.%20Lect.%20Note%20Ser.&amp;volume=127&amp;pages=192-234&amp;publication_year=1988&amp;author=Lloyd%2CNG
[346]: http://www.ams.org/mathscinet-getitem?mr=2356022
[347]: http://scholar.google.com/scholar_lookup?amp;title=Resonance%20and%20nonlinearity%3A%20a%20survey&amp;journal=Ukr.%20Math.%20J.&amp;volume=59&amp;pages=197-214&amp;publication_year=2007&amp;author=Mawhin%2CJ
[348]: http://www.ams.org/mathscinet-getitem?mr=2129727
[349]: http://scholar.google.com/scholar_lookup?amp;title=Bifurcation%20of%20unimodal%20maps&amp;journal=Qual.%20Theory%20Dyn.%20Syst.&amp;volume=4&amp;pages=413-424&amp;publication_year=2004&amp;author=Melo%2CW
[350]: http://scholar.google.com/scholar_lookup?amp;title=Mathematical%20Biology.%20I.%20An%20Introduction&amp;publication_year=2002&amp;author=Murray%2CJD
[351]: http://www.ams.org/mathscinet-getitem?mr=1308609
[352]: http://scholar.google.com/scholar_lookup?amp;title=The%20limit%20cycle%20of%20the%20van%20der%20Pol%20equation%20is%20not%20algebraic&amp;journal=J.%20Differ.%20Equ.&amp;volume=115&amp;issue=1&amp;pages=146-152&amp;publication_year=1995&amp;author=Odani%2CK
[353]: http://www.ams.org/mathscinet-getitem?mr=3034975
[354]: http://scholar.google.com/scholar_lookup?amp;title=The%20complex%20periodic%20problem%20for%20a%20Riccati%20equation&amp;journal=Ann.%20Univ.%20Buchar.%20Math.%20Ser.&amp;volume=3&amp;issue=61%282%29&amp;pages=219-226&amp;publication_year=2012&amp;author=Ortega%2CR
[355]: http://www.ams.org/mathscinet-getitem?mr=3909067
[356]: http://scholar.google.com/scholar_lookup?amp;title=Periodic%20oscillators%2C%20isochronous%20centers%20and%20resonance&amp;journal=Nonlinearity&amp;volume=32&amp;issue=3&amp;pages=800-832&amp;publication_year=2019&amp;author=Ortega%2CR&amp;author=Rojas%2CD
[357]: http://www.ams.org/mathscinet-getitem?mr=1759787
[358]: http://scholar.google.com/scholar_lookup?amp;title=Degenerate%20equations%20of%20pendulum-type&amp;journal=Commun.%20Contemp.%20Math.&amp;volume=2&amp;issue=2&amp;pages=127-149&amp;publication_year=2000&amp;author=Ortega%2CR&amp;author=Tarallo%2CM
[359]: http://www.ams.org/mathscinet-getitem?mr=1691214
[360]: http://scholar.google.com/scholar_lookup?amp;title=The%20number%20of%20periodic%20solutions%20of%20polynomial%20differential%20equations&amp;journal=Math.%20Notes&amp;volume=64&amp;pages=622-628&amp;publication_year=1998&amp;author=Panov%2CAA
[361]: http://scholar.google.com/scholar_lookup?amp;title=Differential%20Equations%20and%20Dynamical%20Systems&amp;publication_year=2001&amp;author=Perko%2CL
[362]: http://scholar.google.com/scholar_lookup?amp;title=Non%20Local%20Problems%20of%20the%20Theory%20of%20Oscillations&amp;publication_year=1966&amp;author=Pliss%2CVA
[363]: http://www.ams.org/mathscinet-getitem?mr=2897887
[364]: http://scholar.google.com/scholar_lookup?amp;title=Extracting%20the%20time-dependent%20transmission%20rate%20from%20infection%20data%20via%20solution%20of%20an%20inverse%20ODE%20problem&amp;journal=J.%20Biol.%20Dyn.&amp;volume=6&amp;pages=509-523&amp;publication_year=2012&amp;author=Pollicott%2CM&amp;author=Wang%2CH&amp;author=Weiss%2CH
[365]: http://www.ams.org/mathscinet-getitem?mr=3893729
[366]: http://scholar.google.com/scholar_lookup?amp;title=New%20lower%20bounds%20for%20the%20Hilbert%20numbers%20using%20reversible%20centers&amp;journal=Nonlinearity&amp;volume=32&amp;pages=331-355&amp;publication_year=2019&amp;author=Prohens%2CR&amp;author=Torregrosa%2CJ
[367]: http://scholar.google.com/scholar_lookup?amp;title=Graphical%20representation%20of%20stability%20conditions%20of%20predator-prey%20interactions&amp;journal=Am.%20Nat.&amp;volume=97&amp;pages=209-223&amp;publication_year=1963&amp;author=Rosenzweig%2CM&amp;author=MacArthur%2CRH
[368]: http://scholar.google.com/scholar_lookup?amp;title=The%20maximum%20number%20of%20limit%20cycles%20of%20the%20system%20%24%24%5Cdot%7By%7D%3D-x%24%24%20y%20%CB%99%20%3D%20-%20x%20%2C%20%24%24%5Cdot%7By%7D%3Dy-%5Csum%20%5E2_%7Bi%3D0%7D%20a_ix%5E%7B2i%2B1%7D%24%24%20y%20%CB%99%20%3D%20y%20-%20%E2%88%91%20i%20%3D%200%202%20a%20i%20x%202%20i%20%2B%201%20is%20two&amp;journal=Differ.%20Equ.&amp;volume=11&amp;pages=301-302&amp;publication_year=1975&amp;author=Rychkov%2CGS
[369]: http://www.ams.org/mathscinet-getitem?mr=558661
[370]: http://scholar.google.com/scholar_lookup?amp;title=Simple%20chemical%20reaction%20systems%20with%20limit%20cycle%20behaviour&amp;journal=J.%20Theoret.%20Biol.&amp;volume=81&amp;pages=389-400&amp;publication_year=1979&amp;author=Schnakenberg%2CJ
[371]: http://scholar.google.com/scholar_lookup?amp;title=Self-oscillations%20in%20glycolysis%3A%20a%20simple%20kinetic%20model&amp;journal=Eur.%20J.%20Biochem.&amp;volume=4&amp;issue=1&amp;pages=79-86&amp;publication_year=1968&amp;author=Sel%E2%80%99kov%2CEE
[372]: http://www.ams.org/mathscinet-getitem?mr=574405
[373]: http://scholar.google.com/scholar_lookup?amp;title=A%20concrete%20example%20of%20the%20existence%20of%20four%20limit%20cycles%20for%20plane%20quadratic%20systems&amp;journal=Sci.%20Sin.&amp;volume=23&amp;pages=153-158&amp;publication_year=1980&amp;author=Shi%2CS
[374]: http://www.ams.org/mathscinet-getitem?mr=1631413
[375]: http://scholar.google.com/scholar_lookup?amp;title=Mathematical%20problems%20for%20the%20next%20century&amp;journal=Math.%20Intell.&amp;volume=20&amp;pages=7-15&amp;publication_year=1998&amp;author=Smale%2CS
[376]: http://scholar.google.com/scholar_lookup?amp;title=On%20relaxation-oscillations%2C%20the%20London%2C%20Edinburgh%20and%20Dublin&amp;journal=Phil.%20Mag.%20J.%20Sci.&amp;volume=2&amp;issue=7&amp;pages=978-992&amp;publication_year=1927&amp;author=Pol%2CB
[377]: http://www.ams.org/mathscinet-getitem?mr=2465564
[378]: http://scholar.google.com/scholar_lookup?amp;title=From%20the%20sixteenth%20Hilbert%20problem%20to%20tropical%20geometry&amp;journal=Jpn.%20J.%20Math.&amp;volume=3&amp;pages=185-214&amp;publication_year=2008&amp;author=Viro%2CO
[379]: http://www.ams.org/mathscinet-getitem?mr=6294
[380]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20differential%20equations%20of%20the%20simplest%20boundary-layer%20problems&amp;journal=Ann.%20Math.&amp;volume=43&amp;pages=381-407&amp;publication_year=1942&amp;author=Weyl%2CH
[381]: http://www.ams.org/mathscinet-getitem?mr=2396500
[382]: http://scholar.google.com/scholar_lookup?amp;title=Planar%20nonautonomous%20polynomial%20equations%3A%20the%20Riccati%20equation&amp;journal=J.%20Differ.%20Equ.&amp;volume=244&amp;issue=6&amp;pages=1304-1328&amp;publication_year=2008&amp;author=Wilczy%C5%84ski%2CP
[383]: http://www.ams.org/mathscinet-getitem?mr=2560053
[384]: http://scholar.google.com/scholar_lookup?amp;title=Quaternionic-valued%20ordinary%20differential%20equations.%20The%20Riccati%20equation&amp;journal=J.%20Differ.%20Equ.&amp;volume=247&amp;issue=7&amp;pages=2163-2187&amp;publication_year=2009&amp;author=Wilczy%C5%84ski%2CP
[385]: http://www.ams.org/mathscinet-getitem?mr=3008031
[386]: http://scholar.google.com/scholar_lookup?amp;title=Planar%20nonautonomous%20polynomial%20equations%20V.%20The%20Abel%20equation&amp;journal=Opusc.%20Math.&amp;volume=33&amp;issue=1&amp;pages=175-189&amp;publication_year=2013&amp;author=Wilczy%C5%84ski%2CP
[387]: http://www.ams.org/mathscinet-getitem?mr=498591
[388]: http://scholar.google.com/scholar_lookup?amp;title=Hilbert%E2%80%99s%20sixteenth%20problem&amp;journal=Topology&amp;volume=17&amp;pages=53-73&amp;publication_year=1978&amp;author=Wilson%2CG
[389]: http://www.ams.org/mathscinet-getitem?mr=3215707
[390]: http://scholar.google.com/scholar_lookup?amp;title=Application%20of%20the%20Abel%20equation%20of%20the%201st%20kind%20to%20inflation%20analysis%20of%20non-exactly%20solvable%20cosmological%20models&amp;journal=Gravit.%20Cosmol.&amp;volume=20&amp;pages=106-115&amp;publication_year=2014&amp;author=Yurov%2CAV&amp;author=Yaparova%2CAV&amp;author=Yurov%2CVA
[391]: http://www.ams.org/mathscinet-getitem?mr=4756845
[392]: http://scholar.google.com/scholar_lookup?amp;title=Nests%20of%20limit%20cycles%20in%20quadratic%20systems&amp;journal=Adv.%20Nonlinear%20Anal.&amp;volume=13&amp;publication_year=2024&amp;author=Zegeling%2CA
[393]: http://www.ams.org/mathscinet-getitem?mr=2020695
[394]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20distribution%20and%20number%20of%20limit%20cycles%20for%20quadratic%20systems%20with%20two%20foci&amp;journal=Qual.%20Theory%20Dyn.%20Syst.&amp;volume=3&amp;pages=437-463&amp;publication_year=2002&amp;author=Zhang%2CP
[395]: http://www.ams.org/mathscinet-getitem?mr=1374347
[396]: http://scholar.google.com/scholar_lookup?amp;title=The%20XVI-th%20Hilbert%20problem%20about%20limit%20cycles%2C%20Panoramas%20of%20mathematics.%20Colloquia%2093%E2%80%9394.%20Lectures%20delivered%20at%20the%20Banach%20Center%20colloquium%20in%20Warsaw%2C%20Poland%20in%20the%20academic%20years%201992%2F93%20and%201993%2F94&amp;journal=Banach%20Cent.%20Publ.&amp;volume=34&amp;pages=167-174&amp;publication_year=1995&amp;author=Zoladek%2CH
[397]: http://www.ams.org/mathscinet-getitem?mr=688192
[398]: http://scholar.google.com/scholar_lookup?amp;title=Order%20of%20cyclicity%20of%20the%20singular%20point%20of%20Li%C3%A9nard%E2%80%99s%20polynomial%20vector%20fields&amp;journal=Bol.%20Soc.%20Bras.%20Mat.&amp;volume=12&amp;issue=2&amp;pages=105-111&amp;publication_year=1981&amp;author=Zuppa%2CC
[399]: https://citation-needed.springer.com/v2/references/10.1007/s40863-024-00471-2?format=refman&amp;flavour=references
[400]: /search?sortBy=newestFirst&amp;contributor=Armengol%20Gasull
[401]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Armengol%20Gasull
[402]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Armengol%20Gasull%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[403]: mailto:armengol.gasull@uab.cat
[404]: http://creativecommons.org/licenses/by/4.0/
[405]: https://s100.copyright.com/AppDispatchServlet?title=From%20Abel%E2%80%99s%20differential%20equations%20to%20Hilbert%E2%80%99s%2016th%20problem&amp;author=Armengol%20Gasull&amp;contentID=10.1007%2Fs40863-024-00471-2&amp;copyright=The%20Author%28s%29&amp;publication=1982-6907&amp;publicationDate=2024-09-28&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[406]: https://crossmark.crossref.org/dialog/?doi=10.1007/s40863-024-00471-2
[407]: https://citation-needed.springer.com/v2/references/10.1007/s40863-024-00471-2?format=refman&amp;flavour=citation
[408]: /search?query=Polynomial%20differential%20equation&amp;facet-discipline=#34;Mathematics&#34;
[409]: /search?query=Periodic%20orbit&amp;facet-discipline=#34;Mathematics&#34;
[410]: /search?query=Limit%20cycle&amp;facet-discipline=#34;Mathematics&#34;
[411]: /search?query=Hilbert%E2%80%99s%2016%C2%A0h%20problem&amp;facet-discipline=#34;Mathematics&#34;
[412]: /search?query=Riccati%E2%80%99s%20equation&amp;facet-discipline=#34;Mathematics&#34;
[413]: /search?query=Abel%E2%80%99s%20equation&amp;facet-discipline=#34;Mathematics&#34;
[414]: /search?query=Primary%3A%2034C07&amp;facet-discipline=#34;Mathematics&#34;
[415]: /search?query=Secondary%3A%2034C25&amp;facet-discipline=#34;Mathematics&#34;
[416]: /search?query=37C27&amp;facet-discipline=#34;Mathematics&#34;
