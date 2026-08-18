<!-- source: https://link.springer.com/article/10.1007/s12346-025-01379-8 | converted from HTML -->

Derivatives of the Separation Function of Generalized Saddle Connections | Qualitative Theory of Dynamical Systems | Springer Nature Link

Skip to main content

# Derivatives of the Separation Function of Generalized Saddle Connections

- [Open access][1]
- Published: 03 October 2025

- Volume 24, article number 227 ( 2025)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Qualitative Theory of Dynamical Systems][5] [Aims and scope][6] [Submit manuscript][7]

Derivatives of the Separation Function of Generalized Saddle Connections

[Download PDF][2]

## Abstract

A classical formula shows that the breaking of a connection between two hyperbolic saddles \(s_0^+\) and \(s_0^-\) can be studied by means of a convergent improper integral that is often called the Melnikov integral. The goal of this paper is to study the applicability of this formula in more general situations, for instance, when the singularities \(s_0^\pm \) are semi-hyperbolic or even nilpotent. We will show that in some of these cases, the improper integral is no longer convergent but nevertheless, under convenient hypothesis, there is a kind of residue that provides the desired information. Our main result, Theorem [A][8], expands the scope of situations in which we can study the breaking of homoclinic or heteroclinic connections. We show that this is indeed the case by analysing three different examples: a heteroclinic connection between nodes, a heteroclinic connection between semi-hyperbolic saddles at infinity and a homoclinic connection in a non-elementary singularity at infinity. As an application of Theorem [A][8] we obtain a general result aimed at studying the breaking of hemicycles and we present several results to analyse the perturbation of unbounded polycycles within a quadratic unfolding that is versal.

### Similar content being viewed by others

### [Two pairs of heteroclinic orbits coined in a new sub-quadratic Lorenz-like system][9]

Article 05 March 2023

### [Revealing the true and pseudo-singularly degenerate heteroclinic cycles][10]

Article 27 April 2023

### [Limit Cycles Near a Centre and a Heteroclinic Loop in a Near–Hamiltonian Differential System][11]

Article 24 March 2022

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Cell-cycle Exit][12]
- [Differential Equations][13]
- [Dynamical Systems][14]
- [Hyperbolic Geometry][15]
- [Ordinary Differential Equations][16]
- [Partial Differential Equations on Manifolds][17]
- [Invariant Manifolds and Dynamical Systems Analysis][18]

## 1 Introduction

Let \(\{X_\mu \}_{\mu \approx \mu _0}\) be a germ of a smooth \(({\mathscr {C}}^\infty \)) family of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N\). Suppose that the vector field \(X_{\mu _0}\) has two hyperbolic saddles, say \(s^\pm _{\mu _0}\in \Omega \), and a solution \(\gamma _{\mu _0}(t)\) with \(\lim _{t\rightarrow \pm \infty }\gamma _{\mu _0}(t)=s_{\mu _0}^\pm \), i.e., there is a saddle connection between \(s^+_{\mu _0}\) and \(s^-_{\mu _0}\). It is clear that \(s^+_{\mu _0}\) and \(s^-_{\mu _0}\) unfold, respectively, into a family of points \(\{s^+_{\mu }\}_{\mu \approx \mu _0}\) and \(\{s^-_{\mu }\}_{\mu \approx \mu _0}\) such that \(s^+_{\mu }\) and \(s^-_{\mu }\) are hyperbolic saddles of \(X_\mu \) for each \(\mu \approx \mu _0.\) Moreover, if we take a smooth family of parametrized transverse sections \({{\sigma _{\mu }}\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma }}_{\mu }\subset \Omega \) to \(X_\mu \) such that \(\sigma _{\mu _0}(0)=p_0\!:=\gamma _{\mu _0}(0)\), then there exist two smooth functions \(d_\pm (\mu )\) for \(\mu \approx \mu _0\) such that the solution \(\gamma ^\pm _\mu (t)\) passing through \(\sigma _\mu (d_\pm (\mu ))\) verifies \(\lim _{t\rightarrow \pm \infty }\gamma ^\pm _{\mu }(t)=s_{\mu }^\pm \), see Figure [1][19]. Thus \(d_\pm (\mu _0)=0\) and the *separation function*of the saddle connection for \(\mu =\mu _0\) is \(d(\mu )\!:=d_+(\mu )-d_-(\mu ).\)

A classical formula asserts that the partial derivatives of \(d(\mu )\) can be computed by means of the (convergent) improper integral

$$\begin{aligned} \partial _{\mu _j}d(\mu _0)= & \frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \int _{-\infty }^{+\infty }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds} \nonumber \\ & \times \big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt. \end{aligned}$$

(1)

Here, and in what follows, we use the wedge product of two vectors \(u,v\in \mathbb {R}^2\) defined by \(u\wedge v=u_1v_2-v_1u_2.\) This type of integral formula for the partial derivatives of the separation function with respect to the parameters was probably known already by Poincaré [[14][20]]. Since then it has been rediscovered independently by several different authors; in the 1953 paper by Duff [[6][21]], in the 1963 paper by Melnikov [[11][22]], in the 1964 thesis by Sotomayor [[17][23]], in the 1964 paper by Arnold [[2][24]] or in the book by Andronov et al. [[1][25]] published in 1966. Despite this history, the integral is now most commonly referred to as the *Melnikov integral*.

The aim of the present paper is to study the applicability of this formula in more general situations, for instance, when the singularities \(s_{\mu _0}^\pm \) are semi-hyperbolic or even nilpotent. We will show that in some of these cases the improper integral is not convergent anymore but nevertheless, under convenient hypothesis, there is a kind of residue that gives the desired information. Our main result is Theorem [A][8], which provides a formula to compute \(\partial _{\mu _j}d(\mu _0)\) in case of a *generalized saddle connection*(see Definition [2.1][26]). In order to relate this new formula with the classical one let us note that, setting

$$\begin{aligned} M_j (\tau )\!:=\int _0^\tau e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt, \end{aligned}$$

(2)

then ( [1][27]) can be written as

$$\begin{aligned} \partial _{\mu _j}d(\mu _0)=\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \left( \lim _{\tau \rightarrow +\infty }M_j(\tau )-\lim _{\tau \rightarrow -\infty }M_j(\tau )\right) . \end{aligned}$$

(3)

If \(s_{\mu _0}^\pm \) is not a hyperbolic saddle then the limit of \(M_j(\tau )\) as \(\tau \rightarrow \pm \infty \) may diverge but, under the assumptions of Theorem [A][8], there is a function \({\mathscr {R}}_j^\pm (\tau )\) such that \(L_\pm =\lim _{\tau \rightarrow \pm \infty }\big (M_j(\tau )-{\mathscr {R}}_j^\pm (\tau )\big )\) exists and is finite. The quantities \(L_\pm \) are a sort of residue that enable to compute the partial derivative.

**Fig. 1**

[image: Fig. 1]

[Full size image][28]

Definition of the separation function \(d(\mu )=d_+(\mu )-d_-(\mu )\) of the saddle connection \(\gamma _{\mu _0}\) between \(s_{\mu _0}^+\) and \(s_{\mu _0}^-\) measured on the transverse section \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu }}\) with \(\sigma _{\mu _0}(0)=\gamma _{\mu _0}(0)=p_0\)

In terms of applicability, if some partial derivative \(\partial _{\mu _j}d(\mu _0)\) is different from zero then one can apply the implicit function theorem to establish the existence of a hypersurface \(\mathcal H\) in the parameter space such that a heteroclinic connection exists in the phase portrait if, and only if, \(\mu \in \mathcal H\) (see for instance [[12][29], Theorem 1]). It is also well-known that the breaking of a saddle connection in a polycycle is related with the bifurcation of limit cycles (see for instance [[15][30], chap. 5] and references therein).

The paper is organized as follows. In Section [2][31] we first propose a generalization of the notions of saddle separatrix and saddle connection, see Definition [2.1][26], and we then state Theorem [A][8], which constitutes our main result. Theorem [A][8] broadens the range of situations in which we can study the breaking of homoclinic or heteroclinic connections. In Section [3][32] we show that this is indeed the case with three different examples. We analyse a heteroclinic connection between two nodes (Example [3.1][33]), a heteroclinic connection between two semi-hyperbolic saddles at infinity (Example [3.3][34]) and a homoclinic connection in a non-elementary singularity at infinity (Example [3.4][35]). Section [4][36] is devoted to demonstrating the validity of the formula ( [1][27]) in the classical setting, as described in the beginning of this section. We do it for completeness because, as a matter of fact, we take advantage of ( [1][27]) in order to prove Theorem [A][8]. Moreover, and this is to be pointed out, the formula that we obtain is slightly more general than the usual one (see for instance [[5][37], §9.1], [[12][29], Lemma 2] or [[13][38], §4.10]), in which the transverse section is assumed to be orthogonal to the saddle connection and not depending on the parameter. Section [5][39] is dedicated to proving Theorem [A][8], which in fact is a direct consequence of Proposition [5.1][40]. Finally in Section [6][41] we illustrate the application of Theorem [A][8] to study the breaking of polycycle connections. We first obtain a general result addressed to hemicycles (Proposition [6.1][42]). Next we show three results to study the perturbation of unbounded polycycles within a quadratic versal unfolding (Propositions [6.2][43], [6.4][44] and [6.5][45]). Following the referees’ suggestions, we provide in Appendix A a geometric interpretation of our main result in terms of 1-forms. We thank the referees for their helpful comments.

## 2 Definitions and Main Result

In this paper we shall sometimes use the notions of push-forward and pull-back of a vector field. Recall that if \({{\phi }\!:{U_1}\rightarrow {U_2}}\) is a diffeomorphism then the *push-forward*of a vector field \(X_1\) on \(U_1\) is the vector field \(\phi _*X_1\) on \(U_2\) defined by \(\big (\phi _*X_1\big )(p)\!:=(D\phi )_{\phi ^{-1}(p)}X_1(\phi ^{-1}(p))\). Similarly, the *pull-back*of a vector field \(X_2\) on \(U_2\) is the vector field \(\phi ^*X_2\) on \(U_1\) defined by \(\big (\phi ^*X_2\big )(p)\!:=(D\phi ^{-1})_{\phi (p)}X_2(\phi (p))\), i.e., \(\phi ^*X_2=(\phi ^{-1})_*X_2.\)

### Definition 2.1

Let \(\mathfrak {X}=\{X_\mu \}_{\mu \approx \mu _0}\) be a germ of a smooth \(({\mathscr {C}}^\infty \)) family of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N\). A family of planar curves \(\{\Gamma _\mu \}_{\mu \approx \mu _0}\) inside \(\Omega \) is a *family of generalized stable*(respectively, *unstable*) *saddle separatrices*for \(\mathfrak {X}\) if \(\Gamma _\mu \) is an orbit of \(X_\mu \) for each \(\mu \approx \mu _0\) and there exist

1. -

an open subset *U*of \(\Omega \times \mathbb {R}^N\),

2. -

a diffeomorphism \(\Phi : U\rightarrow \Phi ( U)\subset \mathbb {R}^2\times \mathbb {R}^N\) of the form \(\Phi (x,y,\mu )=(\phi _\mu (x,y),\mu )\),

3. -

a smooth positive function \(g:\Phi (U)\rightarrow \mathbb {R}\), and

4. -

a germ of a smooth family \(\hat{\mathfrak {X}}=\{{\hat{X}}_\mu \}_{\mu \approx \mu _0}\) of vector fields on an open subset \({\hat{\Omega }}\subset \mathbb {R}^2\),

such that, setting \(U_\mu =\{p\in \mathbb {R}^2:(p,\mu )\in U\}\), the following holds for each \(\mu \approx \mu _0\):

1. (a)

\(g(p;\mu )\big ((\phi _\mu )_*X_\mu \big )(p)={\hat{X}}_\mu (p)\) for all \(p\in \phi _\mu (U_\mu )\cap {\hat{\Omega }}\),

2. (b)

\({\hat{X}}_{\mu _0}\) has a hyperbolic saddle \({\hat{s}}_{\mu _0}\) that unfolds into a family of points \(\{{\hat{s}}_\mu \}_{\mu \approx \mu _0}\) such that \({\hat{s}}_\mu \) is a hyperbolic saddle of \({\hat{X}}_\mu ,\)

3. (c)

there exists a point \(q_\mu \in \Gamma _\mu \cap \phi _\mu ^{-1}({\hat{\Omega }})\) such that its positive (respectively, negative) semiorbit by \(X_\mu \) is contained in \(U_\mu \). Moreover its image \(\phi _\mu (q_\mu )\) is a point inside a stable (respectively, unstable) separatrix of \({\hat{X}}_\mu \) at \({\hat{s}}_\mu \) and, as \(\mu \approx \mu _0\), the positive (respectively, negative) semiorbits of all these points are on the same side of the stable (respectively, unstable) manifold, see Figure [2][46].

Suppose that \(\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) and \(\{\Gamma _\mu ^-\}_{\mu \approx \mu _0}\) are, respectively, a family of generalized stable and unstable saddle separatrices for \(\mathfrak {X}\), i.e., there exist \(U_\mu ^\pm ,\) \(\phi _\mu ^\pm \), \(g^\pm \) and \(\hat{X}_\mu ^\pm \) such that (*a*), (*b*) and (*c*) hold. Then, if \(\Gamma _{\mu _0}^-=\Gamma _{\mu _0}^+=:\Gamma _{\mu _0}\), we say that \(\{\Gamma ^-_\mu \}_{\mu \approx \mu _0}\) and \(\{\Gamma ^+_\mu \}_{\mu \approx \mu _0}\) have a *generalized saddle connection*at \(\Gamma _{\mu _0}.\)

**Fig. 2**

[image: Fig. 2]

[Full size image][47]

Sketch of a generalized stable saddle separatrix \(\Gamma _\mu \) as established in Definition [2.1][26]. On the left we draw the flow of \(X_\mu \) and on the right the flow of \({\tilde{X}}_\mu \), defined as \({\tilde{X}}_\mu =g(\,\cdot ;\mu )(\phi _\mu )_*X_\mu \) on \(\phi _\mu (U_\mu )\) and \({\tilde{X}}_\mu ={\hat{X}}_\mu \) on \({\hat{\Omega }}\), which is a smooth vector field on \(\phi _\mu (U_\mu )\cup {\hat{\Omega }}\)

### Remark 2.2

Let \(\mathfrak {X}=\{X_\mu \}_{\mu \approx \mu _0}\) be a smooth family of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\). Assume that \(X_{\mu _0}\) has a hyperbolic saddle point \(s_{\mu _0}\in \Omega \) that unfolds into a family \(\{s_\mu \}_{\mu \approx \mu _0}\) of hyperbolic saddles of \({\mathfrak {X}}.\) In this case there are two families of stable (respectively, unstable) separatrices of \(\{s_\mu \}_{\mu \approx \mu _0}\), each one arriving from the same side of the stable (respectively, unstable) manifold. Taking \(\Phi =\textrm{Id}\) and \(g\equiv 1\), it is clear that both of them are families of generalized stable (respectively, unstable) saddle separatrices for \(\mathfrak {X}\). Hence, the classical setting outlined in the introduction fits within the framework of Definition [2.1][26].

Another elementary situation that falls within the framework of Definition [2.1][26] occurs when dealing with a smooth family \(\{X_\mu \}_{\mu \approx \mu _0}\) of *polynomial*vector fields such that the Poincaré compactification of \(X_{\mu _0}\) has a hyperbolic saddle \({\hat{s}}_{\mu _0}\) at infinity. (Recall that to study the phase portrait of a polynomial vector field *Y*near infinity we can consider its Poincaré compactification *p*(*Y*), see [[3][48], §5] for instance, which is an analytically equivalent vector field defined on the sphere \(\mathbb {S}^2\). The points at infinity of \(\mathbb {R}^2\) are in bijective correspondence with the points of the equator of \(\mathbb {S}^2\), that we denote by \(\ell _{\infty }\). Moreover the trajectories of *p*(*Y*) in \(\mathbb {S}^2\) are symmetric with respect to the origin and so it suffices to draw its flow in the closed northern hemisphere only, the so called Poincaré disc.) In this case \({\hat{s}}_{\mu _0}\) unfolds into a family \(\{{\hat{s}}_\mu \}_{\mu \approx \mu _0}\), where each \({\hat{s}}_\mu \) is a hyperbolic saddle of \(p(X_\mu )\) at \(\ell _\infty .\) Moreover, since \(\ell _\infty \) is invariant under the flow of \(p(X_\mu )\), each \({\hat{s}}_\mu \) has two finite separatrices \(\Gamma ^1_\mu \) and \(\Gamma ^2_\mu \). It follows then that \(\{\Gamma ^1_\mu \}_{\mu \approx \mu _0}\) and \(\{\Gamma ^2_\mu \}_{\mu \approx \mu _0}\) are two families of generalized saddle separatrices for \(\{X_\mu \}_{\mu \approx \mu _0}\).

The next lemma constitutes in fact a first example of how Definition [2.1][26] enlarges the variety of situations we will be able to study. It shows that certain trajectories arriving to nodes (or even saddle-nodes) form a family generalized saddle separatrices. More precisely, following the notation in the statement, the case \(\lambda _{\mu _0}\lambda _{\mu _0}'>0\) corresponds to a node, whereas the case \(\lambda _{\mu _0}'=0\) applies to any semi-hyperbolic singularity.

### Lemma 2.3

Let \(\mathfrak {X}=\{X_\mu \}_{\mu \approx \mu _0}\) be a smooth family of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\) such that \(X_\mu \) has a singular point at \(s_\mu \in \Omega \) for each \(\mu \). Suppose that \(\mu \mapsto s_\mu \) is smooth and that the eigenvalues \(\lambda _{\mu }\) and \(\lambda _{\mu }'\) of \(DX_{\mu }\) at \(s_{\mu }\) verify, for \(\mu =\mu _0,\) \(\lambda _{\mu _0},\lambda _{\mu _0}'\in \mathbb {R}\) and \(\lambda _{\mu _0}(\lambda _{\mu _0}-\lambda _{\mu _0}')>0\). Then, for each \(\mu \approx \mu _0,\) there are exactly two trajectories of \(X_\mu \) arriving at \(s_\mu \) tangent to the eigenspace of \(\lambda _\mu \) and, as \(\mu \) varies, each one forms a family of generalized saddle separatrices for \(\mathfrak {X}.\) Moreover, following the notation in Definition [2.1][26], we can take \(g\equiv 1\) and \(\phi _\mu (p)=\varphi (p-s_\mu )\), where \(\varphi \) is a directional blow-up not depending on \(\mu .\)

### Proof

Define \(\phi _\mu ^1(p)\!:=p-s_\mu \) and take the linear map \(\phi ^2\), not depending on \(\mu ,\) such that

$$\begin{aligned} (\phi ^2\circ \phi _{\mu _0}^1)_*X_{\mu _0}=\lambda _{\mu _0} x\partial _x+\lambda _{\mu _0}' y\partial _y+\text{ o }(x,y). \end{aligned}$$

Then, by continuity, \(V\!:=\{x\ne 0\}\) contains the image by \(\phi ^2\circ \phi _\mu ^1\) of any trajectory of \(X_\mu \) that arrives at \(s_\mu \) tangent to the eigenspace of \(\lambda _\mu \) for all \(\mu \approx \mu _0.\) Write \((\phi ^2\circ \phi _\mu ^1)_*X_\mu =A_\mu (x,y)\partial _x+B_\mu (x,y)\partial _y\), where observe that \(A_\mu (0,0)=B_\mu (0,0)=0\) for all \(\mu ,\) and perform the blow-up of the origin \(\{x=u,y=vu\}\). In doing so, and setting \(\phi _\mu \!:=\phi ^3\circ \phi ^2\circ \phi _\mu ^1\) with \(\phi ^3(x,y)\!:=(x,\frac{y}{x})\), we get

$$\begin{aligned} {\hat{X}}_\mu \!:=(\phi _\mu )_*(X_\mu )(u,v)=A_\mu (u,uv)\partial _u+\frac{-vA_\mu (u,uv)+B_\mu (u,uv)}{u}\partial _v. \end{aligned}$$

Notice that \(\phi ^3\) is a diffeomorphism that maps *V*onto \(\phi ^3(V)=\{u\ne 0\}\). Moreover \({\hat{X}}_\mu \) is smooth at \(u=0\) and an easy computation shows that \({\hat{X}}_{\mu _0}=\lambda _{\mu _0} u\partial _u+(\lambda '_{\mu _0}-\lambda _{\mu _0})v\partial _v+\text{ o }(u,v)\). Thus, on account of the assumption \(\lambda _{\mu _0}(\lambda _{\mu _0}-\lambda _{\mu _0}')>0\), it turns out that (0, 0) is a hyperbolic saddle of \({\hat{X}}_{\mu _0}\). Hence, by continuity, \({\hat{s}}_{\mu }\!:=(0,0)\) is a hyperbolic saddle of \({\hat{X}}_{\mu }\) for \(\mu \approx \mu _0.\) Consequently, for each \(\mu ,\) there are exactly two trajectories of \(X_\mu \) arriving at \(s_\mu \) tangent to the eigenspace of \(\lambda _\mu \). Taking \(U_\mu =(\phi ^2\circ \phi ^1_\mu )^{-1}(V),\) \(\phi _\mu =\phi ^3\circ \phi ^2\circ \phi _\mu ^1\) and \(g\equiv 1\) (see Definition [2.1][26]), this shows moreover that, as \(\mu \) varies, each trajectory forms a family of generalized saddle separatrices for \(\mathfrak {X}\). \(\square \)

### Definition 2.4

Let \(\{\Gamma _\mu \}_{\mu \approx \mu _0}\) be a *family of generalized stable*(respectively, *unstable*) *saddle separatrices*for \(\mathfrak {X}\). Take a smooth family \(\sigma \!:=\{\sigma _\mu \}_{\mu \approx \mu _0}\) of parametrized transverse sections to \(\mathfrak {X}\) with \(\sigma _{\mu _0}(0)\in \Gamma _{\mu _0}\) and \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \Omega }}\). Then there exists a smooth function \(d_+(\mu )\), respectively, \(d_-(\mu )\), such that, taking \(\varepsilon >0\) small enough,

$$\begin{aligned} \Sigma _\mu \cap \Gamma _\mu =\big \{\sigma _\mu (d_+(\mu ))\big \},\text { respectively, }\Sigma _\mu \cap \Gamma _\mu =\big \{\sigma _\mu (d_-(\mu ))\big \}. \end{aligned}$$

(This follows by firstly applying the local center-stable manifold theorem, see [[8][49], Theorem 1], to the family of hyperbolic saddles \(\hat{s}_\mu \) of \(\hat{X}_\mu \), and secondly appealing to the smooth dependence of the solutions of \(X_\mu \) on initial conditions and parameters.) Note then that \(d_+(\mu _0)=0,\) respectively \(d_-(\mu _0)=0.\)

If \(\{\Gamma ^-_\mu \}_{\mu \approx \mu _0}\) and \(\{\Gamma ^+_\mu \}_{\mu \approx \mu _0}\) have a generalized saddle connection at \(\Gamma _{\mu _0}=\Gamma _{\mu _0}^-=\Gamma _{\mu _0}^+\) then we define its *separation function*(measured on the same family of transverse sections \(\sigma \)) as \(d(\mu )\!:=d_+(\mu )-d_-(\mu ).\)

The main goal of the present paper is to prove the following result. Let us recall that the function \(M_j\) in the statement is defined in ( [2][50]).

### Theorem A

Consider a germ \(\{X_\mu \}_{\mu \approx \mu _0}\) of a smooth family of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N\). Let \(\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) and \(\{\Gamma _\mu ^-\}_{\mu \approx \mu _0}\) be, respectively, a family of generalized stable and unstable separatrices having a generalized saddle connection at \(\Gamma _{\mu _0}\!:=\Gamma _{\mu _0}^+=\Gamma _{\mu _0}^-\) and take a smooth family \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \Omega }}\) of transverse sections with \(p_0\!:=\sigma _{\mu _0}(0)\in \Gamma _{\mu _0}\). Let \(\gamma _{\mu _0}(t)\) be the solution of \(X_{\mu _0}\) with initial condition \(\gamma _{\mu _0}(0)=p_0\) and maximal interval of existence \((T_-,T_+)\). Then, for each \(j=1,2,\ldots ,N,\)

$$\begin{aligned} \partial _{\mu _j}d(\mu _0)=\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\left( \lim _{\tau \rightarrow T_+}\big (M_j(\tau )+{\mathscr {R}}_j^+(\tau )\big ) -\lim _{\tau \rightarrow T_-}\big (M_j(\tau )+{\mathscr {R}}_j^-(\tau )\big )\right) , \end{aligned}$$

with

$$\begin{aligned} {\mathscr {R}}_j^\pm (\tau )=\Big (X_{\mu _0}\wedge (D\phi ^\pm _{\mu _0})^{-1}(\partial _{\mu _j}\phi ^\pm _{\mu _0})\Big )(\gamma _{\mu _0}(\tau ))\,e^{-\int _0^\tau \textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}, \end{aligned}$$

(4)

where \(\phi _{\mu _0}^\pm \) are the diffeomorphims in Definition [2.1][26]. In the particular case that \(\partial _{\mu _j}\phi ^\pm _{\mu _0}\equiv 0\) then

$$\begin{aligned} \partial _{\mu _j}d(\mu _0)= & \frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \nonumber \\ & \times \int _{T_-}^{T_+}e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt. \end{aligned}$$

(5)

Theorem [A][8] applied to the classical setting (as described in Remark [2.2][51]) gives the well-known formula ( [1][27]), see also ( [3][52]). We remark that \(\lim _{\tau \rightarrow T_\pm }\big (M_j(\tau )+ {\mathscr {R}}_j^\pm (\tau )\big )\) exists and is finite but the limit of each summand may diverge (see Example [3.1][33]). Let us also point out that the dependence on \(\phi _\mu \) of the formula for \(\partial _{\mu _j}d(\mu _0)\) in Theorem [A][8] is only apparent because the separation function \(d(\mu )\) does not depend on \(\phi _\mu \) (see Definition [2.4][53]). It is also to be quoted here a result by Schecter (see [[16][54], Theorem 1]), where a similar formula for the derivative of the separation function of a homoclinic connection in a saddle-node is obtained.

## 3 Examples

The notion of a generalized saddle connection, as introduced in Definition [2.1][26], broadens the range of situations in which we can study the breaking of a heteroclinic connection. The aim of this section is to illustrate that this is the case with different examples. We first analyse in detail an example of a heteroclinic connection between two nodes that constitutes a generalized saddle connection and compute the partial derivatives of its separation function by applying Theorem [A][8].

### Example 3.1

Let us consider the 5-parametric family \(\{X_\mu \}_{\mu \approx \mu _0}\) of quadratic vector fields

$$\begin{aligned} & X_\mu =(\varepsilon _0-y+xy)\partial _x+(x+Dx^2+Fy^2+\varepsilon _1 y+\varepsilon _2xy)\partial _y \\ & \hbox { where}\ \mu \!:=(D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2) \end{aligned}$$

and take \(\mu _0=(D_0,F_0,0,0,0)\) with \(D_0<-1\) and \(F_0>\frac{1}{2}\). The unperturbed vector field \(X_{\mu _0}\), see Figure [3][55], has two non-radial hyperbolic nodes \(s^\pm _{\mu _0}=\left( 1,{\mp }\sqrt{\frac{D_0+1}{-F_0}}\,\right) \) on the invariant straight line \(\{x=1\}\) that unfold into two families of (also non-radial) hyperbolic nodes \(\{s_\mu ^\pm \}\) of \(X_\mu .\) Indeed, a computation shows that the eigenvalues of the differential matrix \(DX_{\mu _0}(s_{\mu _0}^\pm )\) are \(\lambda _1^{\pm }(\mu _0)={\mp }2F_0\sqrt{\frac{D_0+1}{-F_0}}\) and \(\lambda _2^{\pm }(\mu _0)={\mp }\sqrt{\frac{D_0+1}{-F_0}}\). Since \(F_0>\frac{1}{2}\), the eigenvalue with larger absolute value is \(\lambda _1^{\pm }(\mu _0)\), which has \(\langle (0,1)\rangle \) as eigenspace. Thus, there are exactly two trajectories arriving at \(s_{\mu _0}^\pm \) tangent to \(\langle (0,1)\rangle \), one from above and the other from below. Lemma [2.3][56] shows that, as \(\mu \) varies, each one unfolds a family of generalized saddle separatrices. Let \(\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) (respectively, \(\{\Gamma _\mu ^-\}_{\mu \approx \mu _0}\)) be the one arriving to \(s_{\mu }^+\) (respectively, \(s_{\mu }^-\)) from above (respectively, below), see Figure [3][55] again. Consequently \(\{\Gamma ^-_\mu \}_{\mu \approx \mu _0}\) and \(\{\Gamma ^+_\mu \}_{\mu \approx \mu _0}\) have a generalized saddle connection at \(\Gamma _{\mu _0}=\big \{(1,y)\in \mathbb {R}^2:y^2<-\frac{D_0+1}{F_0}\,\big \}\). To be more precise, following the notation in Definition [2.1][26], Lemma [2.3][56] shows that we can take \(g^\pm \equiv 1\) and \(\phi _\mu ^\pm (p)=\varphi ^\pm (p-s_\mu ^\pm ),\) where \(\varphi ^\pm \) is a directional blow-up not depending on \(\mu \).

**Fig. 3**

[image: Fig. 3]

[Full size image][57]

Phase portrait for \(\mu =\mu _0\) of the generalized saddle connection in Example [3.1][33]. Each trajectory \(\Gamma _\mu ^\pm \) becomes the separatrix of a hyperbolic saddle \({\hat{s}}_\mu ^\pm \) by means of a blow-up \(\phi _\mu ^\pm \)

Let us take the transverse section \(\sigma _\mu (r)=(1+r,0)\) with \(r\approx 0\) and apply Theorem [A][8] to compute the partial derivatives of the corresponding separation function \(d(\mu )\) at \(\mu =\mu _0.\) Following the notation in the statement of that result, \(p_0=\sigma _{\mu _0}(0)=(1,0)\) and \(\gamma _{\mu _0}(t)=(1,y(t)),\) where \(y(0)=0\) and

$$\begin{aligned} \lim _{t\rightarrow \pm \infty }y(t)={\mp }\sqrt{\frac{D_0+1}{-F_0}}. \end{aligned}$$

(6)

On the other hand, since \(\phi ^\pm _\mu (p)=\varphi ^\pm (p-s_\mu ^\pm )\) with \(\varphi ^\pm \) not depending on \(\mu \) by Lemma [2.3][56],

$$\begin{aligned} \left. (D\phi ^\pm _\mu )_z^{-1}(\partial _{\mu _j}\phi ^\pm _\mu )(z)\right| _{z=\gamma _0(t)} =-\partial _{\mu _j}s^\pm _\mu \hbox { for all}\ t\in \mathbb {R}. \end{aligned}$$

Therefore, on account of \(X_{\mu _0}(\gamma _{\mu _0}(t))=\big (0,D_0+1+F_0y(t)^2\big )\), we get that

$$\begin{aligned} & \Big (X_{\mu _0}\wedge (D\phi _\mu ^\pm )^{-1}(\partial _{\mu _j}\phi _{\mu _0}^\pm )\Big )(\gamma _{\mu _0}(\tau )) \nonumber \\ & =-X_{\mu _0}(\gamma _{\mu _0}(\tau ))\wedge \partial _{\mu _j}s^\pm _{\mu _0} =\big (D_0+1+F_0y(\tau )^2\big )\partial _{\mu _j}x^\pm _{\mu _0}, \end{aligned}$$

(7)

where we write \(s^\pm _{\mu }=(x^\pm _\mu ,y^\pm _\mu ).\)

We compute \(\partial _{\mu _j}d(\mu _0)\) for \(j\ne 3\) first. In this case \((X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0})(\gamma _{\mu _0}(t))\equiv 0\) and consequently, from ( [2][50]), \(M_j(\tau )\equiv 0\). Moreover, \(x_\mu ^\pm |_{\mu _3=0}\equiv 1\) because \(\{x=1\}\) is invariant under the flow of any vector field \(X_\mu \) with \(\mu _3=0\). Thus, \(\partial _{\mu _j}x^\pm _{\mu _0}=0\) and, from ( [4][58]) and ( [7][59]), \({\mathscr {R}}_j^\pm (\tau )\equiv 0.\) Then, by applying Theorem [A][8], we get that \(\partial _{\mu _j}d(\mu _0)=0\) for any \(j\ne 3\).

Let us determine \(\partial _{\mu _3}d(\mu _0)\) next. With this aim in view we note first that, due to \(\textrm{div}(X_{\mu _0})=(2F_0+1)y\),

$$\begin{aligned} \exp \left( -\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds\right) =\left( 1+\frac{F_0}{D_0+1}y(t)^2\right) ^{-1-\frac{1}{2F_0}}, \end{aligned}$$

(8)

where we also use that \(\gamma _{\mu _0}(s)=(1,y(s))\) with \(\frac{dy}{ds}=D_0+1+F_0y^2\) and \(y(0)=0\). The above equality, taking \(\big (X_{\mu _0}\wedge \partial _{\varepsilon _0}X_{\mu _0}\big )(\gamma _{\mu _0}(t))=-(D_0+1+F_0y(t)^2)\) also into account, yields

$$\begin{aligned} M_3(\tau )=-\int _0^{y(\tau )}\left( 1+\frac{F_0}{D_0+1}y^2\right) ^{-1-\frac{1}{2F_0}}dy. \end{aligned}$$

On the other hand, \(X_\mu (s_\mu ^\pm )=(0,0)\) implies \(\varepsilon _0+(x_\mu ^\pm -1)y_\mu ^\pm =0\) for all \(\mu \approx \mu _0\). Hence, since \(x_{\mu _0}=1\) and \(y_{\mu _0}^\pm ={\mp }\sqrt{\frac{D_0+1}{-F_0}},\) we get that \(\partial _{\mu _3}x^\pm _{\mu _0}=\pm \sqrt{\frac{-F_0}{D_0+1}}.\) Accordingly, the substition of ( [7][59]) and ( [8][60]) in ( [4][58]) yields

$$\begin{aligned} {\mathscr {R}}^\pm _3(\tau )={\mp }\sqrt{-F_0(D_0+1)}\left( 1+\frac{F_0}{D_0+1}y(\tau )^2\right) ^{-\frac{1}{2F_0}}. \end{aligned}$$

We remark at this point that \(M_3(\tau )\) and \({\mathscr {R}}_3^\pm (\tau )\) tend to infinity as \(\tau \rightarrow \pm \infty \) on account of ( [6][61]) and the assumption \(F_0>\frac{1}{2}.\) That being said, by making the change of variables \(u={\mp } y\sqrt{\frac{-F_0}{D_0+1}}\) in the integral and the substitution \(v={\mp } y(\tau )\sqrt{\frac{-F_0}{D_0+1}}\), we obtain that

$$\begin{aligned} \lim _{\tau \rightarrow \pm \infty }\big (M_3(\tau )+{\mathscr {R}}_3^\pm (\tau )\big )=\pm \sqrt{\frac{D_0+1}{-F_0}}\lim _{v\rightarrow 1}\left( \int _0^v\frac{du}{(1-u^2)^{1+\eta }}-\frac{1}{2\eta }(1-v^2)^{-\eta }\right) , \end{aligned}$$

where \(\eta :=\frac{1}{2F_0}\in (0,1)\). Hence, by applying Theorem [A][8],

$$\begin{aligned} \partial _{\mu _3}d(\mu _0)=2\sqrt{\frac{D_0+1}{-F_0}}\lim _{v\rightarrow 1}\left( \int _0^v\frac{du}{(1-u^2)^{1+\eta }}-\frac{1}{2\eta }(1-v^2)^{-\eta }\right) . \end{aligned}$$

In order to compute this limit we observe that

$$\begin{aligned} & I(v)=\int _0^v\frac{du}{(1-u^2)^{1+\eta }}=\int _0^v\frac{(1-u)du}{(1-u^2)^{1+\eta }} \\ & +\int _0^v\frac{udu}{(1-u^2)^{1+\eta }} =\int _0^v\frac{(1-u)du}{(1-u^2)^{1+\eta }}+\frac{(1-v^2)^{-\eta }-1}{2\eta }. \end{aligned}$$

The integral in the first summand above is convergent as \(v\rightarrow 1\), whereas the divergent term in the second summand cancels out after the substitution of *I*(*v*) in \(\partial _{\mu _3}d(\mu _0)\). By doing this, a straightforward application of the formulas in [[4][62], §6] yields

$$\begin{aligned} \partial _{\mu _3}d(\mu _0)=2\sqrt{\frac{D_0+1}{-F_0}}\left( \int _0^1\frac{(1-u)du}{(1-u^2)^{1+\eta }}-\frac{1}{2\eta }\right) =\sqrt{\frac{\pi (D_0+1)}{-F_0}}\frac{\Gamma (-\frac{1}{2F_0})}{\Gamma (-\frac{1}{2F_0}+\frac{1}{2})}, \end{aligned}$$

where \(\Gamma \) is the Gamma function. Hence \(\partial _{\mu _3}d(\mu _0)\) with \(D_0<-1\) and \(F_0>\frac{1}{2}\) vanishes if, and only if, \(F_0=1\). Since the straight line \(\{x=1\}\) is invariant under the flow of \(X_\mu \) with \(\mu _3=\varepsilon _0=0,\) by applying the Implicit Function Theorem we can assert that \(\mu _3=0\) is the only solution of the equation \(d(\mu )=0\) in a neighbourhood of any \(\mu _0=(D_0,F_0,0,0,0)\) with \(D_0<-1\) and \(F_0\in (\frac{1}{2},+\infty )\setminus \{1\}.\)

### Remark 3.2

Let \(\Gamma \!:=\{\Gamma _\mu \}_{\mu \approx \mu _0}\) be a family of generalized stable (respectively, unstable) saddle separatrices for a smooth family \(\mathfrak {X}\!:=\{X_\mu \}_{\mu \approx \mu _0}\) of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N.\) Let us also consider a family \(\sigma \!:=\{\sigma _\mu \}_{\mu \approx \mu _0}\) of parametrized transverse sections to \(\mathfrak {X}\) with \(\sigma _{\mu _0}(0)\in \Gamma _{\mu _0}\) and \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \Omega }}\). In what follows we will sometimes emphasize the dependence of the function \(d_\pm (\mu )\) on the families \(\mathfrak {X}\), \(\Gamma \) and \(\sigma \) by writing

$$\begin{aligned} d_\pm (\mu ;\mathfrak {X},\Gamma ,\sigma ). \end{aligned}$$

Suppose that *V*is an open subset of \(\mathbb {R}^2\times \mathbb {R}^N\) such that, for each \(\mu \approx \mu _0\), there exists a point \(z_\mu \in \Gamma _\mu \) whose positive (respectively, negative) semiorbit by \(X_\mu \) is contained in \(V_\mu \!:=\{p\in \mathbb {R}^2:(p,\mu )\in V\}\), and denote by \(\Gamma _\mu ^V\) the orbit of \(\left. X_\mu \right| _{V_\mu }\) passing through \(z_\mu .\) In this case, if \(\Psi (x,y,\mu )=(\psi _\mu (x,y),\mu )\) is a diffeomorphism defined on *V*and \({{h}\!:{\Psi (V)}\rightarrow {\mathbb {R}}}\) is a smooth positive function, then \(\Psi (\Gamma )\!:=\{\psi _\mu (\Gamma _\mu ^V)\}_{\mu \approx \mu _0}\) is a family of generalized stable (respectively, unstable) saddle separatrices for \(h\Psi _*\mathfrak {X}\!:=\{h(\,\cdot ;\mu )(\psi _\mu )_*X_\mu \}_{\mu \approx \mu _0}\). If, in addition, \(\sigma _{\mu _0}(0)\in V_{\mu _0}\) then

$$\begin{aligned} d_\pm \big (\mu ;h\Psi _*\mathfrak {X},\Psi (\Gamma ),\Psi \circ \sigma \big )=d_\pm \big (\mu ;\mathfrak {X},\Gamma ,\sigma \big ), \end{aligned}$$

(9)

where \(\Psi \circ \sigma \!:=\{\psi _\mu \circ \sigma _\mu \}_{\mu \approx \mu _0}.\)

Let us further illustrate Definition [2.1][26] and the application of Theorem [A][8] with two more examples. The first one is a quadratic perturbation of a center whose period annulus is unbounded and has a semi-hyperbolic hemicycle as outer boundary.

### Example 3.3

Consider the 2-parametric family \(\{X_\mu \}_{\mu \approx \mu _0}\) of quadratic vector fields

$$\begin{aligned} X_\mu =(\varepsilon -y+xy)\partial _x+(x+Dx^2+y^2)\partial _y \hbox { where}\ \mu \!:=(D,\varepsilon ) \end{aligned}$$

and take \(\mu _0=(D_0,0)\) with any \(D_0>-1\).

**Fig. 4**

[image: Fig. 4]

[Full size image][63]

Gobal phase portrait in the Poincaré disc of the differential system in Example [3.3][34] for \(\mu =\mu _0\). We remark that for convenience we draw the center at the origin shifted to the left, so that the vertical invariant straight line is \(\{x=1\}\)

Figure [4][64] displays the phase portrait of \(X_{\mu _0}\) in the Poincaré disc. Note in particular that the straight line \(\{x=1\}\) is a heteroclinic connection between two semi-hiperbolic singularities that are topological saddles. These singularities exist and are semi-hiperbolic for all \(\mu \approx \mu _0\). Indeed, compactifying \(X_\mu \) by means of \((u,v)=\psi _\pm (x,y)\!:=\big (\pm \frac{1-x}{y},\pm \frac{1}{y}\big )\) we get \((\psi _\pm )_*X_\mu =\pm \frac{1}{v}{\bar{X}}_\mu \) with

$$\begin{aligned} {\bar{X}}_\mu:= & \big (-\varepsilon v^{2}-D u^{3}+ (2 D+1 ) u^{2}v - (D+1 ) uv^{2} \big )\partial _{u} \\ & + v\big (-1-Du^{2} + (2 D+1 ) u v- (D+1 ) v^{2}\big )\partial _{v}. \end{aligned}$$

(Here we take different charts to study the singularities, which in fact are identified in the projective plane.) The linear part of the smooth vector field \(\pm {\bar{X}}_\mu \) at \(s_\mu ^\pm \!:=(0,0)\) has eigenvalues \(\lambda _\mu ={\mp } 1\) and \(\lambda _\mu '=0\), with eigenspaces \(\{u=0\}\) and \(\{v=0\},\) respectively. Then, by Lemma [2.3][56], for each \(\mu \) there exists a unique trajectory of \(X_\mu \) that in forward (respectively, backward) time arrives to the singularity \(s_\mu ^+\) (respectively, \(s_\mu ^-)\) at infinity tangent to \(\{x=1\}\). Moreover, as \(\mu \) varies, it forms a family \(\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) (respectively, \(\{\Gamma _\mu ^-\}_{\mu \approx \mu _0}\)) of generalized stable (respectively, unstable) saddle separatrices of \(\{X_\mu \}_{\mu \approx \mu _0},\) see Remark [3.2][65]. Notice also, and this simplifies a lot the forthcoming computations, that the diffeomorphism \(\phi _\mu ^\pm \) in Definition [2.1][26] does not depend on \(\mu .\) This follows by the last assertion in Lemma [2.3][56], together with the fact that the singular point \(s_\mu ^\pm \) and the compactification \(\psi _\pm \) do not depend on \(\mu .\)

It is clear that \(\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) and \(\{\Gamma _\mu ^-\}_{\mu \approx \mu _0}\) have a generalized saddle connection at \(\Gamma _{\mu _0}=\{x=1\}.\) Taking the parametrized transverse section \(\sigma _\mu (r)=(1-r,0)\) for \(r\approx 0\), let us compute the partial derivatives of the corresponding separation function \(d(\mu ).\) In this regard observe first that \(\partial _{\mu _1}d(\mu _0)=0\) because \(\{x=1\}\) is invariant for all \(\mu =(D,0).\) In order to compute \(\partial _{\mu _2}d(\mu _0)\) by applying Theorem [A][8], let \(\gamma _{\mu _0}(t)=(1,y(t))\) be the solution of \(X_{\mu _0}\) with initial condition \(p_0\!:=\gamma _{\mu _0}(0)=(1,0)\) and maximal interval of existence \((T_-,T_+)\). Then, since \(\phi _\mu ^\pm \) does not depend on \(\mu ,\)

$$\begin{aligned} \partial _{\mu _2}d(\mu _0)= & \frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\\ & \times \int _{T_-}^{T_+}e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _2}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt. \end{aligned}$$

Taking \(\textrm{div}(X_\mu )=3y\) and \(y'(t)=D_0+1+y(t)^2\) into account, an easy computation shows that

$$\begin{aligned} \exp \left( -\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds\right)= & \exp \left( -\int _0^{y(t)}\frac{3y}{D_0+1+y^2}dy\right) \\ = & \left( 1+\frac{y(t)^2}{D_0+1}\right) ^{\frac{-3}{2}}. \end{aligned}$$

Hence, due to \(\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)=-(D_0+1)\) and \(\big (X_{\mu _0}\wedge \partial _{\mu _2} X_{\mu _0}\big )(\gamma _{\mu _0}(t))=-(1+D+y(t)^2)\), we get

$$\begin{aligned} \partial _{\mu _2}d(\mu _0)&=\frac{1}{D_0+1}\int _{T_-}^{T_+}\left( 1+\frac{y(t)^2}{D_0+1}\right) ^{-\frac{3}{2}}(1+D_0+y(t)^2)dt\\&=\frac{1}{D_0+1}\int _{-\infty }^{+\infty }\left( 1+\frac{y^2}{D_0+1}\right) ^{-\frac{3}{2}}dy =\frac{2}{\sqrt{D_0+1}}, \end{aligned}$$

where we also use that \(\lim _{t\rightarrow T_\pm }y(t)=\pm \infty .\) Accordingly \(\partial _{\mu _2}d(\mu _0)\ne 0\) and, by applying the Implicit Function Theorem, \(\mu _2=0\) is the only solution of \(d(\mu )=0\) in a neighbourhood *U*of \(\mu _0.\) Consequently, for all \(\mu \in U,\) the only heteroclinic connection (apart from the one at the line of infinity) between the singular points \(s_\mu ^+\) and \(s_\mu ^-\) is the straight line \(\{x=1\}\), and it occurs for \(\mu _2=\varepsilon =0.\)

The heteroclinic connections studied in the two previous examples occur between elementary singularities (i.e., hyperbolic or semi-hyperbolic). We can thus apply Lemma [2.3][56] directly to show that some specific trajectory arriving to the singularity form, as \(\mu \) varies, a family of generalized saddle separatrices. To this end, see the proof of that lemma, we use a directional blow-up. The aim of this blow-up is not to desingularize the singularity but to “separate” this particular trajectory from the semi-hyperbolic singularity and anchor it on a hyperbolic saddle (cf. Definition [2.1][26]). On the contrary, the blow-up used in the next example is to desingularize the critical point because it is not elementary.

### Example 3.4

Consider the 2-parametric family \(\{X_\mu \}_{\mu \approx \mu _0}\) of quadratic vector fields

$$\begin{aligned} X_\mu =-y(1-x)\partial _x+(x+\varepsilon y+Fy^2)\partial _y \hbox { where}\ \mu =(F,\varepsilon ) \end{aligned}$$

and take \(\mu _0=(F_0,0)\) for any \(F_0\in (\frac{1}{2},+\infty )\setminus \{1\}\). The unperturbed vector field \(X_{\mu _0}\) has a center at (0, 0) with an unbounded period annulus, whose outer boundary is the parabola \(\Gamma _{\mu _0}\!:=\{x=\frac{1-2F_0}{2}y^2+\frac{1}{2F_0}\}\), see Figure [5][66].

**Fig. 5**

[image: Fig. 5]

[Full size image][67]

On the left (respectively, right) global phase portrait in the Poincaré disc of the differential system in Example [3.4][35] for \(\mu =\mu _0\) with \(F_0>1\) (respectively, \(\frac{1}{2}<F_0<1\)). We remark that for convenience we draw the center at the origin shifted to the left, so that the vertical invariant straight line is \(\{x=1\}\)

This parabola is a homoclinic connection of a nilpotent singularity at infinity. The singularity (identified with its antipodal in the Poincaré disc) has four hyperbolic sectors when \(F>1\), and two parabolic sectors, one hyperbolic sector and one elliptic sector when \(F\in (\frac{1}{2},1)\). The homoclinic connection for \(\mu =\mu _0\) is at the boundary of the hyperbolic sector \(\mathcal H_{\mu _0}\) that intersects with the negative *x*-axis. The connection breaks for \(\mu \ne \mu _0\), but the sectorial decomposition of the singularity is the same. Let us show first that the trajectories at the boundary of the hyperbolic sector \(\mathcal H_\mu \) (unfolding \(\mathcal H_{\mu _0}\)) are a family of generalized saddle separatrices for \(\{X_\mu \}_{\mu \approx \mu _0}\). Once we show this, we will define and study its corresponding separation function. With this aim in view we perform the projective change of coordinates given by \((u_1,v_1)=\phi _1(x,y)\!:=\big (\frac{1}{1-x},\frac{y}{1-x}\big )\), that yields

$$\begin{aligned} (\phi _1)_*X_\mu =-\frac{1}{u_1}\Big (v_{1}u_1\partial _{u_1}+ \big (u_1-u_{1}^{2}-\varepsilon u_{1} v_{1}- (F -1 )v_{1}^{2} \big )\partial _{v_1} \Big ). \end{aligned}$$

The vector field \(u_1(\phi _1)_*X_\mu \) has a nilpotent singularity at \(s_\mu \!:=(0,0)\). By applying [[3][48], Theorem 3.5] one can show that the the sectorial decomposition of \(u_1(\phi _1)_*X_\mu \) at \(s_\mu =(0,0)\) is as we described previously. We define \(\Gamma _\mu ^\pm \) to be the orbit of \(X_\mu \) containing \(\{\pm y>0\}\cap \partial \mathcal H_\mu .\) Next we perform two successive blow-ups given by \((u_2,v_2)=\phi _2(u_1,v_1)\!:=\big (\frac{u_1}{v_1},v_1\big )\) and \((u_3,v_3)=\phi _3(u_2,v_2)\!:=\big (u_2,\frac{v_2}{u_2}\big )\). In doing so, a computation shows that \(\big (\phi _3\circ \phi _2\circ \phi _1\big )_*X_\mu =\frac{1}{\pm u_3v_3}{\hat{X}}^\pm _\mu \) where

$$\begin{aligned} {\hat{X}}^\pm _\mu:= & \pm u_3\big (1-F v_{3}-\varepsilon u_{3} v_{3}-u_{3}^{2} v_{3}\big )\partial _{u_3} \\ & \pm v_3\big (-2+(2F -1) v_{3}+2 \varepsilon u_{3} v_{3}+2u_{3}^{2} v_{3}\big )\partial _{v_3}. \end{aligned}$$

Accordingly, and following the notation in Definition [2.1][26], if we take \(\phi _\mu (x,y)\!:=\big (\phi _3\circ \phi _2\circ \phi _1\big )(x,y)=\big (\frac{1}{y},\frac{y^2}{1-x}\big )\) and \(g^\pm (u_3,v_3;\mu )\!:=\pm u_3v_3\) then it turns out that \(g^\pm (\,\cdot ;\mu )\big (\phi _\mu \big )_* X_\mu ={\hat{X}}^\pm _\mu \) is a smooth (in fact, polynomial) vector field which one can verify that it has a hyperbolic saddle at the point \({\hat{s}}^\pm _\mu \!:=\big (0,\frac{2}{2F-1}\big )\) for all \(\mu \). Moreover \(\phi _\mu \) maps \(\Gamma _\mu ^\pm \) to the separatrix of the saddle \({\hat{s}}_\mu ^\pm \) of \({\hat{X}}_\mu ^\pm \) on \(\{\pm u_3>0\}\). Therefore, see Definition [2.1][26], \(\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) and \(\{\Gamma _\mu ^-\}_{\mu \approx \mu _0}\) are, respectively, a family of generalized stable and unstable saddle separatrices of \(\{X_\mu \}_{\mu \approx \mu _0}.\) It is also clear that they have a generalized saddle connection at \(\Gamma _{\mu _0}.\)

Let us take the parametrized transverse section \(\sigma _\mu (r)=(\frac{1}{2F}-r,0)\) for \(r\approx 0\) and study the separation function of the connection at \(\Gamma _{\mu _0}\). Note first that the hyperbola \(\{x=\frac{1-2F}{2}y^2+\frac{1}{2F}\}\) is invariant under the flow of the vector field \(X_\mu \) for any \(\mu \) with \(\varepsilon =0\), and that it intersects \(\{y=0\}\) at \(\sigma _\mu (0)=(\frac{1}{2F},0)\). Thus \(d(\mu )|_{\varepsilon =0}\equiv 0\) and, consequently, \(\partial _Fd(\mu _0)=0.\) In order to compute the partial derivative \(\partial _\varepsilon d(\mu _0)\) we shall apply Theorem [A][8]. To this end notice that the diffeomorphism \(\phi _\mu \) does not depend on \(\mu \) and that, accordingly,

$$\begin{aligned} \partial _{\varepsilon }d(\mu _0)=\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \int _{T_-}^{T_+}e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\varepsilon }X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt. \end{aligned}$$

where \(\gamma _{\mu _0}(t)=(x(t),y(t))\) is the solution of \(X_{\mu _0}\) with initial condition \(\gamma _{\mu _0}(0)=\sigma _{\mu _0}(0)\) and \((T_-,T_+)\) is its maximal interval of existence. Since \(\gamma _{\mu _0}(t)\in \Gamma _{\mu _0}\) for all *t*we have that \(y'(t)=x(t)+F_0y(t)^2=\frac{1}{2}y(t)^2+\frac{1}{2F_0}.\) Hence, by making the change of variables \(u=y(s)\) and taking \(\textrm{div}(X_{\mu _0})=(1+2F_0)y\) into account, we get

$$\begin{aligned} \exp \left( -\int _0^t \textrm{div}\big (X_{\mu _0}\big )(\gamma _{\mu _0}(s))ds\right) =(1+F_0y(t)^2)^{-(1+2F_0)}. \end{aligned}$$

Therefore, on account of \(\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)=\frac{-1}{2F_0}\) and \(X_{\mu _0}\wedge \partial _\varepsilon X_{\mu _0}=-y^2(1-x)\),

$$\begin{aligned} \partial _{\varepsilon }d(\mu _0)=2F_0(2F_0-1)\int _{-\infty }^{+\infty }(1+F_0u^2)^{-1-2F_0}u^2du =\frac{(2F_0-1)\sqrt{\pi }\,\Gamma (2F_0-\frac{1}{2})}{\sqrt{F_0}\,\Gamma (2F_0+1)}, \end{aligned}$$

where in the first equality we make the change of variables \(u=y(t)\) once again and in the second one we use the formulas in [[4][62], §6] about the Gamma function. Accordingly we can assert that \(\partial _{\varepsilon }d(\mu _0)\ne 0\) for all \(\mu _0=(F_0,0)\) with \(F_0\in (\frac{1}{2},+\infty )\setminus \{1\}\).

The case \(F_0=1\) must be treated separately because the line at infinity \(u_1=0\) of \( (\phi _1)_*X_\mu \) is not invariant. Nevertheless the blow-up process is valid and shows that there is also a generalized saddle connection at \(\Gamma _{\mu _0}\) for \(F_0=1.\) Moreover the expressions of the partial derivatives are valid in this case as well.

## 4 The Classical Setting

Let \(\{X_\mu \}_{\mu \approx \mu _0}\) be a germ of a \({\mathscr {C}}^\infty \) family of vector fields on an open subset \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N\). In this section we assume that the vector field \(X_{\mu _0}\) has a hyperbolic saddle \(s^\pm _{\mu _0}\in \Omega \) and a solution \(\gamma _{\mu _0}^\pm (t)\) with \(\lim _{t\rightarrow \pm \infty }\gamma _{\mu _0}^\pm (t)=s_{\mu _0}^\pm \). Then \(s^\pm _{\mu _0}\) unfolds into a family of points \(\{s^\pm _{\mu }\}_{\mu \approx \mu _0}\) such that \(s^\pm _{\mu }\) is a hyperbolic saddle of \(X_\mu \) for each \(\mu \approx \mu _0.\) Moreover, taking a smooth family of parametrized transversal sections \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \Omega }}\) to \(X_\mu \) such that \(\sigma _{\mu _0}(0)=p_0\!:=\gamma ^\pm _{\mu _0}(0)\), there exists a smooth function \(d_\pm (\mu )\) for \(\mu \approx \mu _0\) such that the solution \(\gamma ^\pm _\mu (t)\) with \(\gamma _{\mu }^\pm (0)=\sigma _\mu (d_\pm (\mu ))\) verifies \(\lim _{t\rightarrow \pm \infty }\gamma ^\pm _{\mu }(t)=s_{\mu }^\pm \), see Figure [1][19]. Note that, in particular, \(d_\pm (\mu _0)=0\). The aim of this section is to prove the following formula, cf. ( [1][27]).

### Lemma 4.1

Under the above hypothesis, for each \(j=1,2,\ldots ,N\) we have that

$$\begin{aligned} \partial _{\mu _j}d_\pm (\mu _0)=&\,\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\\&\times \int _{0}^{\pm \infty }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma ^\pm _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma ^\pm _{\mu _0}(t))dt \nonumber \\&-\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}. \end{aligned}$$

### Proof

Let us show the result for the derivative of \(d_+(\mu ),\) the other one follows verbatim. That being said, we claim that, for any \(\mu \approx \mu _0\),

$$\begin{aligned} \delta _j(t,\mu )\!:=\partial _{\mu _j}\gamma ^+_\mu (t)\wedge X_\mu (\gamma ^+_\mu (t)) \end{aligned}$$

(10)

satisfies the linear differential equation

$$\begin{aligned} \partial _t\delta _j(t,\mu )=\textrm{div}(X_\mu )(\gamma ^+_\mu (t))\delta _j(t,\mu )+\big (\partial _{\mu _j} X_\mu \wedge X_\mu \big )(\gamma ^+_\mu (t)). \end{aligned}$$

Indeed, since \(\partial _t\partial _{\mu _j}\gamma ^+_{\mu }(t)=\partial _{\mu _j}\partial _{t}\gamma ^+_{\mu }(t)\) and \(\partial _{t}\gamma ^+_{\mu }(t)=X_{\mu }(\gamma ^+_{\mu }(t)),\)

$$\begin{aligned} \partial _t\delta _j&=\partial _{\mu _j}(\partial _t\gamma ^+_\mu )\wedge X_\mu (\gamma ^+_\mu )+\partial _{\mu _j}\gamma ^+_\mu \wedge \Big (DX_\mu (\gamma ^+_\mu )\partial _t\gamma ^+_\mu \Big ) \\&=\partial _{\mu _j}\big (X_\mu (\gamma ^+_\mu )\big )\wedge X_\mu (\gamma ^+_\mu )+\partial _{\mu _j}\gamma ^+_\mu \wedge \Big (DX_\mu (\gamma ^+_\mu )X_\mu (\gamma ^+_\mu )\Big ) \\&=\Big (\partial _{\mu _j}X_\mu (\gamma ^+_\mu )+DX_\mu (\gamma ^+_\mu )\partial _{\mu _j}\gamma ^+_\mu \Big )\wedge X_\mu (\gamma ^+_\mu ) \\&\quad +\partial _{\mu _j}\gamma ^+_\mu \wedge \Big (DX_\mu (\gamma ^+_\mu )X_\mu (\gamma ^+_\mu )\Big ) \\&=(\partial _{\mu _j}X_\mu \wedge X_\mu )(\gamma ^+_\mu )+\textrm{tr}(DX_\mu )(\gamma ^+_\mu )\delta _j, \end{aligned}$$

where in the last equality we use that \(\det (Au,v)+\det (u,Av)=\textrm{tr}(A)\det (u,v)\) for any \(A\in M_{2\times 2}(\mathbb {R})\) and \(u,v\in \mathbb {R}^2\). This formula generalizes to dimension *n*by using the well-known Liouville’s formula as follows:

$$\begin{aligned} \sum _{k=1}^n\det (u_1,\ldots ,Au_k,\ldots ,u_n)&=\partial _t\det (e^{tA}u_1,\ldots ,e^{tA}u_n)|_{t=0}\\&=\partial _t\det (e^{tA})|_{t=0}\det (u_1,\ldots ,u_n)\\&=\textrm{tr}(A)\det (u_1,\ldots ,u_n). \end{aligned}$$

Therefore, from ( [10][68]),

$$\begin{aligned} \left. \delta _j(t,\mu )e^{-\int _0^t\textrm{div}(X_\mu )(\gamma ^+_\mu (s))ds}\right| _0^T=\int _0^Te^{-\int _0^t\textrm{div}(X_\mu )(\gamma ^+_\mu (s))ds}(\partial _{\mu _j}X_\mu \wedge X_\mu )(\gamma ^+_\mu (t))dt, \nonumber \\ \end{aligned}$$

(11)

for any \(T>0.\) (Here we are using that the image of \(\gamma ^+_\mu \) is a stable separatrix of the saddle \(s_\mu ^+\), so that it is defined for all \(t>0.\)) Taking \(T\rightarrow +\infty \) on both sides of the above equality, the application of Lemma [4.2][69] yields

$$\begin{aligned} \delta _j(0,\mu )=\int _0^{+\infty } e^{-\int _0^t\textrm{div}(X_\mu )(\gamma ^+_\mu (s))ds}(X_\mu \wedge \partial _{\mu _j}X_\mu )(\gamma ^+_\mu (t))dt. \end{aligned}$$

On the other hand, taking \(\gamma ^+_\mu (0)=\sigma _\mu (d_+(\mu ))\) into account again, from ( [10][68]) with \(t=0\) we get

$$\begin{aligned} \delta _j(0,\mu )=\partial _{\mu _j}\big (\sigma _\mu (d_+(\mu ))\big )\wedge X_\mu \big (\sigma _\mu (d_+(\mu ))\big ). \end{aligned}$$

Next we evaluate this equality at \(\mu =\mu _0\) and to this aim we note first that, due to \(d_+(\mu _0)=0\),

$$\begin{aligned} \left. \partial _{\mu _j}\big (\sigma _\mu \big (d_+(\mu ))\big )\right| _{\mu =\mu _0}&= \left. \partial _{\mu _j}\sigma _\mu \big (d_+(\mu )\big ) +\partial _r\sigma _{\mu }\big (d_+(\mu )\big )\partial _{\mu _j}\big (d_+(\mu )\big )\right| _{\mu =\mu _0}\\&=\partial _{\mu _j}\sigma _{\mu _0}(0)+\partial _{\mu _j}d_+(\mu _0)\partial _{r}\sigma _{\mu _0}(0). \end{aligned}$$

Consequently, due to \(\sigma _{\mu _0}(d_+(\mu _0))=\sigma _{\mu _0}(0)=p_0\),

$$\begin{aligned} \delta _j(0,\mu _0)=\partial _{\mu _j} d_+(\mu _0)\Big (\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)\Big )+ \partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0). \end{aligned}$$

Finally, the substitution of this expression in ( [11][70]) with \(\mu =\mu _0\) yields

$$\begin{aligned} \partial _{\mu _j}d_+(\mu _0)=\frac{\delta _j(0,\mu _0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}-\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}, \end{aligned}$$

as desired. \(\square \)

### Lemma 4.2

Let us consider a \({\mathscr {C}}^\infty \) family of vector fields \(\{X_\mu \}_{\mu \approx \mu _0}\) on an open subset \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N\) such that \(X_{\mu _0}\) has a hyperbolic saddle at \(s_{\mu _0}\in \Omega .\) Then \(s_{\mu _0}\) unfolds into a family of points \(\{s_\mu \}_{\mu \approx \mu _0}\) in \(\Omega \) such that \(s_\mu \) is a hyperbolic saddle of \(X_\mu \) for each \(\mu \approx \mu _0.\) If \(\gamma _\mu (t)\) is a solution of \(X_\mu \) with \(\lim _{t\rightarrow +\infty }\gamma _\mu (t)=s_\mu \) then

$$\begin{aligned} \lim _{t\rightarrow +\infty }\delta _j(t,\mu )e^{-\int _0^t\textrm{div}(X_\mu )(\gamma _\mu (s))ds}=0, \end{aligned}$$

where \(\delta _j(t,\mu )=\partial _{\mu _j}\gamma _\mu (t)\wedge X_\mu (\gamma _\mu (t))\).

### Proof

By applying [[9][71], Lemma 4.3] there exist an open neighbourhood *V*of \(\overline{\gamma _{\mu _0}\big ([0,+\infty )\big )}\times \{\mu _0\}\) in \(\mathbb {R}^2\times \mathbb {R}^N\) and a smooth diffeomorphism \(\Psi :V\rightarrow \Psi (V)\subset \mathbb {R}^2\times \mathbb {R}^N\) with \(\Psi (x,y,\mu )=(\psi _\mu (x,y),\mu )\) such that, for each \(\mu ,\) \(\psi _\mu (s_\mu )=(0,0)\) and

$$\begin{aligned} (\psi _\mu )_*X_\mu =xP_\mu (x,y)\partial _x+yQ_\mu (x,y)\partial _y, \end{aligned}$$

where \(P_\mu (x,y)\) and \(Q_\mu (x,y)\) are smooth functions on \(\Psi (V)\) verifying \(P_\mu (x,0)Q_\mu (0,y)\ne 0\). Since \(\psi _\mu \) is a diffeomorphism, the eigenvalues of \(DX_\mu (s_\mu )\) are precisely \(P_\mu (0,0)\) and \(Q_\mu (0,0)\). We assume without loss of generality that \(P_\mu (0,0)<0<Q_\mu (0,0)\) and, consequently,

$$\begin{aligned} \frac{\textrm{div}(X_\mu )(s_\mu )}{P_\mu (0,0)}=1-\lambda (\mu ),\hbox { where}\ \lambda (\mu )\!:=-\frac{Q_\mu (0,0)}{P_\mu (0,0)}>0 \end{aligned}$$

is the hyperbolicity ratio of the saddle \(s_\mu \) of \(X_\mu \). Observe, and this is the key point, that the solution \(\gamma _\mu (t)\) at the stable separatrix of \(s_\mu \) can be written as \(\gamma _\mu (t)=\psi _\mu ^{-1}(x_\mu (t),0)\) where \(\lim _{t\rightarrow +\infty }x_\mu (t)=0\) and

$$\begin{aligned} \partial _tx_\mu (t)=x_\mu (t)P_\mu (x_\mu (t),0). \end{aligned}$$

(12)

On account of this, by making the change of variables \(x=x_\mu (t)\) we get

$$\begin{aligned} I_\mu (t)\!:=\int _0^t\textrm{div}\big (X_\mu \big )(\gamma _\mu (s))ds=\int _{x_\mu (0)}^{x_\mu (t)}\textrm{div}\big (X_\mu \big )(\psi _\mu ^{-1}(x,0))\frac{dx}{xP_\mu (x,0)}. \end{aligned}$$

This integral diverges as \(t\rightarrow +\infty \) due to \(\lim _{t\rightarrow +\infty }x_\mu (t)=0\). For this reason we proceed as follows. Setting \(g_\mu (x)\!:=\frac{\textrm{div}(X_\mu )(\psi _\mu ^{-1}(x,0))}{P_\mu (x,0)}\) we have \(g_\mu (0)=1-\lambda (\mu )\) and we can write

$$\begin{aligned} I_\mu (t)= & \int _{x_\mu (0)}^{x_\mu (t)}g_\mu (0)\frac{dx}{x}+\int _{x_\mu (0)}^{x_\mu (t)}\frac{g_\mu (x)-g_\mu (0)}{x}dx \\= & (1-\lambda (\mu ))\log \left| x_\mu (t)\right| +h_\mu (t), \end{aligned}$$

where for each \(\mu \) the function \(h_\mu (t)\!:=-g_\mu (0)\log |x_\mu (0)|+\int _{x_\mu (0)}^{x_\mu (t)}\frac{g_\mu (x)-g_\mu (0)}{x}dx\) is smooth on \((0,+\infty )\) and has finite limit as \(t\rightarrow +\infty .\) Furthermore, following this notation, we can write

$$\begin{aligned} \delta _j(t,\mu )e^{-\int _0^t {\text {div}}(X_{\mu })(\gamma _{\mu }(s))ds}&=\delta _j(t,\mu )e^{-I_\mu (t)}=\delta _j(t,\mu )|x_\mu (t)|^{\lambda (\mu )-1}e^{-h_\mu (t)}\\&=\frac{\delta _j(t,\mu )}{|x_\mu (t)|}|x_\mu (t)|^{\lambda (\mu )} e^{-h_\mu (t)}. \end{aligned}$$

We claim that the quotient \(\frac{\delta _j(t,\mu )}{|x_\mu (t)|}\) is bounded as \(t\rightarrow +\infty \). Note that the result will follow once we prove this. With this aim in view we first observe that

$$\begin{aligned} & X_\mu (p)=\big (\psi _\mu ^{-1}\big )_*\big (P_\mu (x,y)x\partial _x+Q_\mu (x,y)y\partial _y\big )(p) \\ & =\big (D\psi _\mu ^{-1}\big )_{\psi _\mu (p)}\big ((P_\mu (x,y)x\partial _x+Q_\mu (x,y)y\partial _y)\circ \psi _\mu (p)\big ). \end{aligned}$$

Therefore, due to \(\gamma _\mu (t)=\psi _\mu ^{-1}(x_\mu (t),0)\),

$$\begin{aligned} \Vert X_\mu (\gamma _\mu (t))\Vert&=\Vert ( D\psi _\mu ^{-1})_{(x_\mu (t),0)} \big (P_\mu (x_\mu (t),0)x_\mu (t) \partial _x\big )\Vert \\ &\leqslant \Vert (D\psi _\mu ^{-1})_{ (x_\mu (t),0)}\Vert |x_\mu (t)P_\mu ( x_\mu (t),0)|. \end{aligned}$$

Hence

$$\begin{aligned} \frac{\delta _j(t,\mu )}{|x_\mu (t)|}= & \frac{\delta _j(t,\mu )}{\Vert X_\mu (\gamma _\mu (t))\Vert }\frac{\Vert X_\mu (\gamma _\mu (t))\Vert }{|x_\mu (t)|} \\\leqslant & \frac{\delta _j(t,\mu )}{\Vert X_\mu (\gamma _\mu (t))\Vert }\sup _{|x|<\delta }\left( \Vert (D\psi _\mu ^{-1})_{(x,0)}\Vert |P_\mu (x,0)|\right) \end{aligned}$$

for *t*large enough. Recall that, by definition, \(\frac{\delta _j(t,\mu )}{\Vert X_\mu (\gamma _\mu (t))\Vert }=\partial _{\mu _j}\gamma _\mu (t)\wedge \frac{X_\mu }{\Vert X_\mu \Vert }(\gamma _\mu (t))\). Thus, on account of the above upper bound, in order to prove the claim it suffices to show that \(\partial _{\mu _j}\gamma _\mu (t)\) is bounded as \(t\rightarrow +\infty .\) As a matter of fact, one can prove that \(\lim _{t\rightarrow +\infty }\partial _{\mu _j}\gamma _\mu (t)=\partial _{\mu _j}s_\mu .\) Indeed, this is so because

$$\begin{aligned} \partial _{\mu _j}\gamma _\mu (t)=\big (\partial _{\mu _j}\psi ^{-1}_\mu \big )(x_\mu (t),0)+\big (\partial _x\psi ^{-1}_\mu \big )(x_\mu (t),0)\partial _{\mu _j}x_\mu (t) \end{aligned}$$

(13)

where, from ( [12][72]), the partial derivative \(\partial _{\mu _j}x_\mu (t)\) verifies

$$\begin{aligned} \partial _t\partial _{\mu _j}x_\mu (t)=\partial _{\mu _j}x_\mu (t)\underbrace{\partial _x\big (xP_\mu (x,0)\big )|_{x=x_\mu (t)}}_{a(t)}+\underbrace{x\partial _{\mu _j}P_\mu (x,0)|_{x=x_\mu (t)}}_{b(t)}. \end{aligned}$$

The solution of this first order linear differential equation is

$$\begin{aligned} \partial _{\mu _j} x_\mu (t)&=e^{\int _0^ta(s)ds}\left( \partial _{\mu _j}x_\mu (0)+\int _0^tb(s)e^{-\int _0^sa(u)du}ds\right) \\&=e^{\int _{x_\mu (0)}^{x_\mu (t)}\frac{\partial _x\left( xP_\mu (x,0)\right) }{xP_\mu (x,0)}dx}\left( \partial _{\mu _j}x_\mu (0)+\int _{x_\mu (0)}^{x_\mu (t)}\frac{x\partial _{\mu _j}P_\mu (x,0)}{xP_\mu (x,0)} e^{-\int _{x_\mu (0)}^x\frac{\partial _x\left( vP_\mu (v,0)\right) }{vP_\mu (v,0)}dv}dx\right) \\&=\frac{x_\mu (t)P_\mu (x_\mu (t),0)}{x_\mu (0)P_\mu (x_\mu (0),0)}\left( \partial _{\mu _j}x_\mu (0)+\int _{x_\mu (0)}^{x_\mu (t)}\frac{\partial _{\mu _j}P_\mu (x,0)}{P_\mu (x,0)}\frac{x_\mu (0)P_\mu (x_\mu (0),0)}{xP_\mu (x,0)}dx\right) , \end{aligned}$$

where in the second equality we made the change of coordinates \(x=x_\mu (s)\). This shows that \(\partial _{\mu _j} x_\mu (t)\) can be written as

$$\begin{aligned} \partial _{\mu _j} x_\mu (t)=x_\mu (t)f_1(t)+x_\mu (t)f_2(t)\int _{x_\mu (0)}^{x_\mu (t)}\frac{g(x)}{x}dx, \end{aligned}$$

where \(\lim _{t\rightarrow +\infty }f_i(t)\) is finite for \(i=1,2\) and *g*is smooth at \(x=0.\) Exactly as we did previously,

$$\begin{aligned} & x_\mu (t)\int _{x_\mu (0)}^{x_\mu (t)}\frac{g(x)}{x}dx=x_\mu (t)g(0)\log \left( \frac{x_\mu (t)}{x_\mu (0)}\right) \\ & +x_\mu (t)\int _{x_\mu (0)}^{x_\mu (t)}\frac{g(x)-g(0)}{x}dx\rightarrow 0\hbox { as}\ t\rightarrow +\infty \end{aligned}$$

due to \(\lim _{t\rightarrow +\infty }x_\mu (t)=0.\) Consequently, \(\lim _{t\rightarrow +\infty }\partial _{\mu _j}x_\mu (t)=0\), and then from ( [13][73]) we obtain

$$\begin{aligned} \lim _{t\rightarrow +\infty }\partial _{\mu _j}\gamma _\mu (t)=\big (\partial _{\mu _j}\psi ^{-1}_\mu \big )(0,0)=\partial _{\mu _j}s_{\mu } \end{aligned}$$

since \(\psi ^{-1}_\mu (0,0)=s_{\mu }\) for all \(\mu \). This proves the claim and concludes the proof of the result. \(\square \)

## 5 Proof of the Main Result

This section is entirely devoted to the proof of the next result. In its statement we use the functions \(M_j\) and \({\mathscr {R}}_j^\pm \), that were previously defined in ( [2][50]) and ( [4][58]), respectively.

### Proposition 5.1

Let \(\mathfrak {X}=\{X_\mu \}_{\mu \approx \mu _0}\) be a germ of a smooth family of vector fields on \(\Omega \subset \mathbb {R}^2\) with parameter \(\mu \in \mathbb {R}^N\). Suppose that \(\Gamma ^+=\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) (respectively, \(\Gamma ^-=\{\Gamma _\mu ^-\}_{\mu \approx \mu _0})\) is a family of generalized stable (respectively, unstable) separatrices and take a smooth family \(\sigma =\{\sigma _\mu \}_{\mu \approx \mu _0}\) of transverse sections \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \Omega }}\) with \(p_0\!:=\sigma _{\mu _0}(0)\in \Gamma _{\mu _0}^\pm \). Let \(\gamma _{\mu _0}(t)\) be the solution of \(X_{\mu _0}\) with initial condition \(\gamma _{\mu _0}(0)=p_0\) and maximal interval of existence \((T_-,T_+)\). Then, for each \(j=1,2,\ldots ,N,\)

$$\begin{aligned} & \partial _{\mu _j}d_\pm (\mu _0;\mathfrak {X},\Gamma ^\pm ,\sigma ) \\ & =\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\left( \lim _{\tau \rightarrow T_\pm }\big (M_j(\tau )+{\mathscr {R}}^\pm _j(\tau )\big )-\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0) \right) . \end{aligned}$$

Note that Theorem [A][8] is a direct application of Proposition [5.1][40] because, by definition, the separation function is \(d(\mu )=d_+(\mu )-d_-(\mu )\).

### Definition 5.2

Given a germ \(\mathfrak {X}=\{X_\mu \}_{\mu \approx \mu _0}\) of a \({\mathscr {C}}^\infty \) family of vector fields on \(\Omega \subset \mathbb {R}^2\) and a smooth family \(\sigma =\{\sigma _\mu \}_{\mu \approx \mu _0}\) of transverse sections \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \Omega }}\) we define

$$\begin{aligned} \Delta _j(\tau ;\mathfrak {X},\sigma )\!:=&\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \nonumber \\&\times \int _{0}^{\tau }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt \nonumber \\&-\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}. \end{aligned}$$

(14)

where \(\gamma _{\mu _0}(t)\) is the solution of \(X_{\mu _0}\) with initial condition \(p_0\!:=\gamma _{\mu _0}(0)=\sigma _{\mu _0}(0)\) and \(\tau \) belongs to its maximal interval of existence.

For reader’s convenience we next outline the idea of the proof of Proposition [5.1][40] for the partial derivative of \(d_+\) (the case \(d_-\) follows verbatim). Since \(\Gamma ^+=\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) is a family of generalized stable separatrices, there exist an open subset *U*of \(\Omega \times \mathbb {R}^N\), a diffeomorphism \(\Phi : U\rightarrow \Phi ( U)\subset \mathbb {R}^2\times \mathbb {R}^N\) of the form \(\Phi (x,y,\mu )=(\phi _\mu (x,y),\mu )\), a smooth positive function \(g:\Phi (U)\rightarrow \mathbb {R}\), and a germ of a smooth family \(\hat{\mathfrak {X}}=\{{\hat{X}}_\mu \}_{\mu \approx \mu _0}\) of vector fields on an open subset \({\hat{\Omega }}\subset \mathbb {R}^2\), such that (*a*), (*b*) and (*c*) in Definition [2.1][26] hold. We shall prove first that we can assume without loss of generality that \(\gamma _{\mu _0}([0,T_s))\times \{\mu _0\}\) is inside *U*. Then, in doing so, and taking Remark [3.2][65] and Lemma [4.1][74] into account, we will get

$$\begin{aligned} \partial _{\mu _j}d_+(\mu ;\mathfrak {X},\Gamma ^+,\sigma )= & \partial _{\mu _j}d_+(\mu ;g\Phi _*\mathfrak {X},\Phi (\Gamma ^+),\Phi \circ \sigma )\\= & \lim _{\tau \rightarrow +\infty }\Delta _j(\tau ;g\Phi _*\mathfrak {X},\Phi \circ \sigma ). \end{aligned}$$

This is the reason why in our next two lemmas we study how the expression \(\Delta _j(\tau ;\mathfrak {X},\sigma )\) in ( [14][75]) is modified after performing two specific changes in the family \(\mathfrak {X}\) of vector fields.

### Lemma 5.3

Following the notation in Definition [5.2][76], let us consider a neighbourhood *U*of \(\gamma _{\mu _0}\big ([0,\tau ]\big )\times \{\mu _0\}\) in \(\mathbb {R}^2\times \mathbb {R}^N\) and a smooth positive function \({{g}\!:{U}\rightarrow {\mathbb {R}}}\). Then

$$\begin{aligned} \Delta _j\big (\tau ;g\mathfrak {X}|_{U},\sigma \big )=\Delta _j\big (h(\tau );\mathfrak {X},\sigma \big ), \end{aligned}$$

where *h*is the smooth function with \(h(0)=0\) such that \(h'(t)=g\big (\gamma _{\mu _0}(h(t))\big )\) and \(g\mathfrak {X}|_{U}\!:=\left\{ \left. g(\,\cdot ;\mu )X_{\mu }\right| _U\right\} _{\mu \approx \mu _0}.\)

### Proof

Let \({\hat{\gamma }}_{\mu _0}(t)\) be the solution of \(\left. g(\,\cdot ;\mu _0)X_{\mu _0}\right| _U\) passing through \(\sigma _{\mu _0}(0)\) at \(t=0\). It is clear that this solution is a reparametrization of the solution \(\gamma _{\mu _0}\) of \(X_{\mu _0}\) with \(\gamma _{\mu _0}(0)=\sigma _{\mu _0}(0)\). More precisely, we have that \({\hat{\gamma }}_{\mu _0}=\gamma _{\mu _0}\circ h\), where *h*is the unique smooth function with \(h(0)=0\) verifying \(h'(t)=g(\gamma _{\mu _0}(h(t)))\) or, equivalently, \((h^{-1})'(t)=\frac{1}{g(\gamma _{\mu _0}(t))}\). That being said, from ( [14][75]) we get that

$$\begin{aligned} \Delta _j(\tau ;g\mathfrak {X}|_{U},\sigma )=&\,\frac{1}{g(p_0)\big (\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)\big )} \nonumber \\&\times \int _{0}^{\tau }{\underline{E}}(t)\big (g({\hat{\gamma }}_{\mu _0}(t))\big )^2\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )({\hat{\gamma }}_{\mu _0}(t))dt \nonumber \\&-\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}, \end{aligned}$$

(15)

where we set \({\underline{E}}(t)\!:=\exp \left( -\int _0^t\textrm{div}\big (gX_{\mu _0}\big )({\hat{\gamma }}_{\mu _0}(s))ds\right) \) for shortness. In the above equality we take advantage of the multi-linearity of the determinant and use that \(\partial _{\mu _j}(gX_{\mu _0})=g\partial _{\mu _j}X_{\mu _0}+X_{\mu _0}\partial _{\mu _j}g.\) In addition, due to

$$\begin{aligned} \textrm{div}(gX)=\nabla g\cdot X+g\,\textrm{div}(X)=\nabla \log g\cdot (gX)+g\,\textrm{div}(X), \end{aligned}$$

we have that

$$\begin{aligned} \textrm{div}(gX_{\mu _0})({\hat{\gamma }}_{\mu _0}(s))=\partial _s\log g({\hat{\gamma }}_{\mu _0}(s)) +g\big (\gamma _{\mu _0}(h(s))\big )\textrm{div}\big (X_{\mu _0}\big )\big (\gamma _{\mu _0}(h(s))\big ) \end{aligned}$$

and, consequently,

$$\begin{aligned} {\underline{E}}(t)&=\exp \left( -\int _0^t\textrm{div}\big (gX_{\mu _0}\big )\big (\gamma (h(s))\big )ds\right) \\&=\frac{g({\hat{\gamma }}_{\mu _0}(0))}{g({\hat{\gamma }}_{\mu _0}(t))}\exp \left( -\int _0^tg\big (\gamma _{\mu _0}(h(s))\big )\textrm{div}\big (X_{\mu _0}\big )\big (\gamma _{\mu _0}(h(s))\big )ds\right) \\&=\frac{g(p_0)}{g({\hat{\gamma }}_{\mu _0}(t))}\exp \left( -\int _0^{h(t)}\textrm{div}\big (X_{\mu _0}\big )(\gamma _{\mu _0}(v))dv\right) \end{aligned}$$

where we make the change of variables \(v=h(s)\) and take \((h^{-1})'(v)=\frac{1}{g(\gamma _{\mu _0}(v))}=\frac{1}{g(\gamma _{\mu _0}(h(s))}\) into account. Accordingly, from ( [15][77]),

$$\begin{aligned} \Delta _j\big (\tau ;g\mathfrak {X}|_{U},\sigma \big )=&\,\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\int _{0}^{\tau } \!\!e^{-\int _0^{h(t)}\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(v))dv}g\big (\gamma _{\mu _0}(h(t))\big ) \\ &\times \big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(h(t)))dt -\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \\ =&\,\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\\ &\times \int _{0}^{h(\tau )} \!\!e^{-\int _0^{s}\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(v))dv}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(s))ds \\&-\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} =\Delta _j\big (h(\tau );\mathfrak {X},\sigma \big ), \end{aligned}$$

where in the second equality we make the change of variables \(s=h(t)\) and take \((h^{-1})'(s)=\frac{1}{g(\gamma _{\mu _0}(s))}\) into account again. This completes the proof of the result. \(\square \)

We obtain next a formula to compute the divergence of the pull-back of a *n*-dimensional vector field. Recall that, if \({{\phi }\!:{U_1}\rightarrow {U_2}}\) is a diffeomorphism, then *pull-back*of a vector field \(X_2\) on \(U_2\) is the vector field on \(U_1\) given by \(\phi ^*X_2\!:=(\phi ^{-1})_*X_2.\)

### Lemma 5.4

Let *U*be an open subset of \(\mathbb {R}^n\) and consider a diffeomorphism \({{F}\!:{U}\rightarrow {F(U)\subset \mathbb {R}^n}}\). Then

$$\begin{aligned} \textrm{div}({F}^*X)={F}^*(\textrm{div}\big (X)\big )-\nabla \big (\log \det (D{F})\big )\cdot {F}^*X, \end{aligned}$$

for any smooth vector field *X*on *F*(*U*).

### Proof

Let us note first that \(\big (F^*X\big )(p)=\big (DF^{-1}\big )_{F(p)}X(F(p))=\big (DF\big )^{-1}_{p}X(F(p))\). Consequently, taking \((DF)^{-1}=\frac{1}{\det (DF)}\,\text {adj}(DF)\) into account, we get

$$\begin{aligned} \det (D{F}){F}^*X=\text {adj}(DF)X(F)=\left( \sum _{j=1}^na_{1j}X_j(F),\ldots ,\sum _{j=1}^na_{nj}X_j(F)\right) , \end{aligned}$$

(16)

where we write the adjugate of *DF*as \(\textrm{adj}(DF)=(a_{ij})_{1\leqslant i,j\leqslant n}\) and \(X=(X_1,\ldots ,X_n).\) In this regard we claim that

$$\begin{aligned} \sum _{i=1}^n\partial _{x_i}(a_{ij})=0\hbox { for each}\ j=1,2,\ldots ,n. \end{aligned}$$

(17)

Indeed, to show this let us write \(F=(F_1,\ldots ,F_n)\) and fix some \(j\in \{1,2,\ldots ,n\}\). Setting \(v\!:=(F_1,\ldots ,\widehat{F_j},\ldots ,F_n)\), by definition we have that

$$\begin{aligned} a_{ij}=(-1)^{i+j}\det (\partial _{x_1}v,\ldots ,\widehat{\partial _{x_i}v},\ldots ,\partial _{x_n}v). \end{aligned}$$

Consequently \(\sum _{i=1}^n\partial _{x_i}(a_{ij})=(-1)^j\sum _{i,k=1}^n\Delta _{ik}\), where

$$\begin{aligned} \Delta _{ik}=\left\{ \begin{array}{cl} (-1)^i\det (\partial _{x_1}v,\ldots ,\widehat{\partial _{x_i}v},\ldots ,\partial _{x_i}\partial _{x_k}v,\ldots ,\partial _{x_n}v) & \text {if }k>i,\\ 0 & \text {if } i=k ,\\ (-1)^i\det (\partial _{x_1}v,\ldots ,\partial _{x_i}\partial _{x_k}v,\ldots ,\widehat{\partial _{x_i}v},\ldots ,\partial _{x_n}v) & \text {if }k<i. \end{array} \right. \end{aligned}$$

Therefore \(\sum _{i=1}^n\partial _{x_i}(a_{ij})=(-1)^j\sum _{1\leqslant i<k\leqslant n}(\Delta _{ik}+\Delta _{ki})=0\) because one can show that \(\Delta _{ik}+\Delta _{ki}=0\) after swapping \(k-i-1\) columns in the determinant \(\Delta _{ki}\) and using that \(\partial _{x_i}\partial _{x_k}v_j=\partial _{x_k}\partial _{x_i}v_j\). This proves the validity of the claim. Then, from ( [16][78]),

$$\begin{aligned} \textrm{div}\big (\det (D{F}){F}^*X\big )&=\sum _{i=1}^n\sum _{j=1}^n\partial _{x_i}\big (a_{ij}X_j(F)\big ) \\&=\sum _{i,j=1}^n\left( \partial _{x_i}(a_{ij})X_j(F)+a_{ij}\sum _{k=1}^n\big (\partial _{x_k}X_j\big )(F)\partial _{x_i}F_k\right) \\&=\sum _{j=1}^nX_j(F)\sum _{i=1}^n\partial _{x_i}(a_{ij})+\det (DF)\sum _{j,k=1}^n\delta _{kj}(\partial _{x_k}X_j)(F)\\&=\det (DF)\Big (\sum _{j=1}^n\partial _{x_j}X_j\Big )\circ F=\det (DF)F^*\textrm{div}(X), \end{aligned}$$

where in the third equality we use that \(\sum _{i=1}^na_{ij}\partial _{x_i}F_k=\big ((DF)\,\textrm{adj}(DF)\big )_{kj}=\delta _{kj}\det (DF)\) for each fixed \(j,k\in \{1,2,\ldots ,n\}\) and in the fourth one the identity in ( [17][79]). Accordingly

$$\begin{aligned} \textrm{div}(\det (D{F}){F}^*X)=\det (D{F}){F}^*(\textrm{div}(X)). \end{aligned}$$

Now, by applying the identity \(\textrm{div}(fY)=f\textrm{div}(Y)+\nabla f\cdot Y\) on the left hand side of this equality we get

$$\begin{aligned} \det (D{F})\textrm{div}({F}^*X)+\nabla \big (\det (D{F})\big )\cdot F^*X=\det (D{F}){F}^*(\textrm{div}(X)). \end{aligned}$$

From here the result follows after dividing by \(\det (D{F})\) on both sides of this equality. \(\square \)

Next we study how \(\Delta _j(\tau ;\mathfrak {X},\sigma )\) changes if we push-forward \(\mathfrak {X}\) and \(\sigma \) by a diffeomorphism. In short, we obtain an additional term that depends on the partial derivative \(\partial _{\mu _j}\) of the diffeomorphism.

### Lemma 5.5

Following the notation in Definition [5.2][76], consider a neighbourhood *U*of \(\gamma _{\mu _0}\big ([0,\tau ]\big )\times \{\mu _0\}\) in \(\mathbb {R}^2\times \mathbb {R}^N\) and a diffeomorphism \(\Phi : U\rightarrow \Phi ( U)\subset \mathbb {R}^2\times \mathbb {R}^N\) of the form \(\Phi (x,y,\mu )=(\phi _\mu (x,y),\mu )\). If we take the smooth family of vector fields \(\Phi _*\mathfrak {X}|_{U}\!:=\{(\phi _\mu )_*(X_\mu |_U)\}_{\mu \approx \mu _0}\) and the smooth family of transverse sections \(\Phi \circ \sigma \!:=\left\{ \phi _\mu (\sigma _\mu )\right\} _{\mu \approx \mu _0}\) then

$$\begin{aligned} \Delta _j\big (\tau ;\Phi _*\mathfrak {X}|_{U},\Phi \circ \sigma \big )=\Delta _j(\tau ;\mathfrak {X},\sigma )+\frac{{\mathscr {R}}_j(\tau )}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}, \end{aligned}$$

where

$$\begin{aligned} {\mathscr {R}}_j(\tau )=\Big (X_{\mu _0}\wedge (D\phi _{\mu _0})^{-1}(\partial _{\mu _j}\phi _{\mu _0})\Big )(\gamma _{\mu _0}(\tau ))\,e^{-\int _0^\tau \textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}. \end{aligned}$$

### Proof

If we set \({\bar{X}}_{\mu }\!:=(\phi _\mu )_*X_\mu \) and \({\bar{\sigma }}_\mu \!:=\phi _\mu \circ \sigma _\mu \) then, recall Definition [5.2][76],

$$\begin{aligned} \Delta _j\big (\tau ;\Phi _*\mathfrak {X}|_{U},\Phi \circ \sigma \big )=&\,\frac{1}{\partial _r{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)} \nonumber \\&\int _{0}^{\tau }e^{-\int _0^t\textrm{div}({\bar{X}}_{\mu _0})({\bar{\gamma }}_{\mu _0}(s))ds}\big ({\bar{X}}_{\mu _0}\wedge \partial _{\mu _j}{\bar{X}}_{\mu _0}\big )({\bar{\gamma }}_{\mu _0}(t))dt \nonumber \\&-\frac{\partial _{\mu _j}{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)}{\partial _r{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)}, \end{aligned}$$

(18)

where \({\bar{\gamma }}_{\mu _0}(t)\) is the solution of \({\bar{X}}_{\mu _0}=(\phi _{\mu _0})_*X_{\mu _0}\) with \({\bar{\gamma }}_\mu (0)=(\phi _{\mu _0}\circ \sigma _{\mu _0})(0)=\phi _{\mu _0}(p_0)=:{\bar{p}}_0\). It is clear in this regard that \({\bar{\gamma }}_{\mu _0}(t)=\phi _{\mu _0}(\gamma _{\mu _0}(t))\). Moreover, if we denote \(\psi _{\mu }\!:=\phi _{\mu }^{-1}\) then

$$\begin{aligned} \textrm{div}({\bar{X}}_{\mu _0})({\bar{\gamma }}_{\mu _0}(t))&=\textrm{div}\big ((\phi _{\mu _0})_*X_{\mu _0}\big )\big (\phi _{\mu _0}(\gamma _{\mu _0}(t))\big )= \textrm{div}\big ((\psi _{\mu _0})^*X_{\mu _0}\big )\big (\phi _{\mu _0}(\gamma _{\mu _0}(t))\big )\\&=\big ((\psi _{\mu _0})^*\textrm{div}(X_{\mu _0})\big )\big (\phi _{\mu _0}(\gamma _{\mu _0}(t))\big )\\&-\big (\nabla (\log \det (D\psi _{\mu _0}))\cdot (\psi _{\mu _0})^*X_{\mu _0}\big )\big (\phi _{\mu _0}(\gamma _{\mu _0}(t))\big )\\&=\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(t))-\partial _t\big (\log \det (D\psi _{\mu _0})\big )(\phi _{\mu _0}(\gamma _{\mu _0}(t))), \end{aligned}$$

where in the third equality we apply Lemma [5.4][80] and in the fourth one we use that, due to the definition of the pull-back of a function, \(\psi _{\mu _0}^*(\textrm{div}(X_{\mu _0}))=(\textrm{div}(X_{\mu _0}))\circ \psi _{\mu _0}\), together with the fact that \(\phi _{\mu _0}(\gamma _{\mu _0}(t))\) is a solution of \((\phi _{\mu _0})_*X_{\mu _0}=(\psi _{\mu _0})^*X_{\mu _0}.\) Consequently

$$\begin{aligned} & \exp \left( -\int _0^t\textrm{div}({\bar{X}}_{\mu _0})({\bar{\gamma }}_{\mu _0}(s))ds\right) \nonumber \\ & =\frac{\det \big (D\psi _{\mu _0}\big )(\phi _{\mu _0}(\gamma _{\mu _0}(t)))}{\det \big (D\psi _{\mu _0}\big )(\phi _{\mu _0}(p_0))} \exp \left( -\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds\right) , \end{aligned}$$

(19)

where observe that \(\det \big (D\psi _{\mu _0}\big )(\phi _{\mu _0}(p_0))=\frac{1}{\det (D\phi _{\mu _0})(p_0)}\) due to \(\phi _{\mu _0}=\psi _{\mu _0}^{-1}.\)

Our next task is to express the derivative \(\partial _{\mu _j}{\bar{X}}_{\mu _0}\) that appears in integrand of the expression ( [18][81]) in terms of derivatives of \(X_\mu \) and \(\psi _\mu \). On account of \({\bar{X}}_{\mu }(p)=\big ((\phi _\mu )_*X_\mu \big )(p)=(D\psi _\mu )^{-1}_pX_\mu (\psi _\mu (p))\), some easy computations show that

$$\begin{aligned} \partial _{\mu _j}{\bar{X}}_{\mu }(p)=(D\psi _\mu )^{-1}_p \left. \Big ( \partial _{\mu _j}X_{\mu }(z) +\big (DX_{\mu }\big )_z(\partial _{\mu _j}\psi _{\mu })(p) -\big (D\partial _{\mu _j}\psi _{\mu }\big )_p\big (D\psi _{\mu }\big )^{-1}_pX_{\mu }(z) \Big )\right| _{z=\psi _\mu (p)}, \end{aligned}$$

where the last term is obtained by making the partial derivative \(\partial _{\mu _j}\) on both sides of the matrix identity \((D\psi _\mu )^{-1}_p(D\psi _\mu )_p=\textrm{Id}.\) Accordingly, since \(\psi _{\mu }^{-1}=\phi _\mu ,\)

$$\begin{aligned} & \big ({\bar{X}}_{\mu }\wedge \partial _{\mu _j}{\bar{X}}_{\mu }\big )(\phi _{\mu }(z))\\ & = \frac{X_\mu (z)\wedge \Big ( \partial _{\mu _j}X_{\mu }(z) +\big (DX_{\mu }\big )_z(\partial _{\mu _j}\psi _{\mu })(\phi _{\mu }(z)) -\big (D\partial _{\mu _j}\psi _{\mu }\big )_{\phi _{\mu }(z)}\big (D\phi _{\mu }\big )_zX_{\mu }(z) \Big )}{\det \big (D\psi _\mu \big )(\phi _{\mu }(z))}. \end{aligned}$$

Consequently, setting \(\Theta (t)\!:=\big ((\partial _{\mu _j}\psi _{\mu _0})\circ \phi _{\mu _0}\big )(\gamma _{\mu _0}(t))\) and using that \(\gamma _{\mu _0}'(t)=X_{\mu _0}(\gamma _{\mu _0}(t)),\) we obtain

$$\begin{aligned} \big ({\bar{X}}_{\mu _0}\wedge \partial _{\mu _j}{\bar{X}}_{\mu _0}\big )\big ({\bar{\gamma }}_{\mu _0}(t)\big )&= \big ({\bar{X}}_{\mu _0}\wedge \partial _{\mu _j}{\bar{X}}_{\mu _0}\big )\big (\phi _{\mu _0}(\gamma _{\mu _0}(t))\big )=\\&=\frac{\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))}{\det \big (D\psi _{\mu _0}\big )(\phi _{\mu _0}(\gamma _{\mu _0}(t)))}\\&+\frac{X_{\mu _0}(\gamma _{\mu _0}(t))\wedge \big ((DX_{\mu _0})_{\gamma _{\mu _0}(t)}\Theta (t)-\Theta '(t)\big )}{\det \big (D\psi _{\mu _0}\big )(\phi _{\mu _0}(\gamma _{\mu _0}(t)))}. \end{aligned}$$

The combination of this equality with the one in ( [19][82]) shows that

$$\begin{aligned} Z_1\!:=&\,\frac{1}{\partial _r{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)}\int _{0}^{\tau }e^{-\int _0^t\textrm{div}({\bar{X}}_{\mu _0})({\bar{\gamma }}_{\mu _0}(s))ds}\big ({\bar{X}}_{\mu _0}\wedge \partial _{\mu _j}{\bar{X}}_{\mu _0}\big )({\bar{\gamma }}_{\mu _0}(t))dt\\ =&\,\frac{\det (D\phi _{\mu _0})(p_0)}{\partial _r{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)} \int _{0}^{\tau }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt\\&\,+\frac{\det (D\phi _{\mu _0})(p_0)}{\partial _r{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)} \int _{0}^{\tau }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds} \Big (X_{\mu _0}(\gamma _{\mu _0}(t))\wedge \\&\big ((DX_{\mu _0})_{\gamma _{\mu _0}(t)}\Theta (t)-\Theta '(t)\big )\Big )dt\\ =&\,\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \int _{0}^{\tau }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt\\&\,+\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\underbrace{ e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (\Theta (t)\wedge X_{\mu _0}(\gamma _{\mu _0}(t))\big ) }_{\Omega (t)} \Big |_{t=0}^{t=\tau }\\ =&\,\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \int _{0}^{\tau }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt\\&\,+\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\\&\times \left( e^{-\int _0^\tau \textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (\Theta (\tau )\wedge X_{\mu _0}(\gamma _{\mu _0}(\tau ))\big ) -\big (\Theta (0)\wedge X_{\mu _0}(p_0)\big ) \right) , \end{aligned}$$

where in the second equality we also use that \(\big (D\psi _{\mu _0}\big )_{\phi _{\mu _0}(p_0)}=(D\phi _{\mu _0})^{-1}_{p_0}\). In the third equality we use that \(\partial _r{\bar{\sigma }}_{\mu _0}(0)=\left. \partial _r\big (\phi _{\mu _0}(\sigma _{\mu _0}(r))\big )\right| _{r=0}=\big (D\phi _{\mu _0}\big )_{p_0}\partial _r\sigma _{\mu _0}(0)\) and that, by definition,

$$\begin{aligned} {\bar{X}}_{\mu _0}({\bar{p}}_0)=\big ((\phi _{\mu _0})_*X_{\mu _0}\big )({\bar{p}}_0)=\big (D\phi _{\mu _0}\big )_{\phi _{\mu _0}^{-1}({\bar{p}}_0)}X_{\mu _0}(\phi ^{-1}_{\mu _0}({\bar{p}}_0))=\big (D\phi _{\mu _0}\big )_{p_0}X_{\mu _0}(p_0). \end{aligned}$$

We use moreover that the function \(\Omega (t)\) is a primitive of the integrand in the second summand. Indeed, on account of \(\gamma _{\mu _0}'(t)=X_{\mu _0}(\gamma _{\mu _0}(t))\), and using also that \(\det (Au,v)+\det (u,Av)=\textrm{tr}(A)\det (u,v)\) for any \(A\in M_{2\times 2}(\mathbb {R})\) and \(u,v\in \mathbb {R}^2\), one can easily verify that

$$\begin{aligned} \Omega '(t)=e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds} \Big (X_{\mu _0}(\gamma _{\mu _0}(t))\wedge \big ((DX_{\mu _0})_{\gamma _{\mu _0}(t)}\Theta (t)-\Theta '(t)\big )\Big ). \end{aligned}$$

On the other hand, using that \([\partial _{\mu _j}\bar{\sigma }_{ \mu _0}(0)=\partial _{\mu _j}(\phi _\mu \circ \sigma _\mu (0))|_{\mu =\mu _0}=(D\phi _{\mu _0})_{p_ 0}\partial _{\mu _j}\sigma _{\mu _ 0}(0)+(\partial _{\mu _j}\phi _{\ mu_0})(\sigma _{\mu _0}(0))]\) together with \(\partial _r{\bar{\sigma }}_{\mu _0}(0)=\big (D\phi _{\mu _0}\big )_{p_0} \partial _r\sigma _{\mu _0}(0)\) and \({\bar{X}}_{\mu _0}({\bar{p}}_0)=\big (D\phi _{\mu _0}\big )_{p_0}X_{\mu _0}(p_0)\) once again, we obtain

$$\begin{aligned} Z_2\!:=\frac{\partial _{\mu _j}{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)}{\partial _r{\bar{\sigma }}_{\mu _0}(0)\wedge {\bar{X}}_{\mu _0}({\bar{p}}_0)}&=\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)}\\&\quad +\frac{(D\phi _{\mu _0})_{p_0}^{-1}\partial _{\mu _j}\phi _{\mu _0}(p_0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)}\\&=\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)} -\frac{\Theta (0)\wedge X_{\mu _0}(p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)}, \end{aligned}$$

where in the third equality we use that \(\Theta (t)=\partial _{\mu _j}\psi _{\mu _0}(\phi _{\mu _0}(z))|_{z=\gamma _{\mu _0}(t)}=-(D\phi _{\mu _0})_{z}^{-1}\partial _{\mu _j}\phi _{\mu _0}(z)|_{z=\gamma _{\mu _0}(t)}\) with \(t=0\), which in turn is a consequence of \(\partial _{\mu _j}(\phi _\mu \circ \psi _\mu )\equiv 0\). Since \(\Delta _j\big (\tau ;\Phi _*\mathfrak {X}|_{U},\Phi \circ \sigma \big )=Z_1-Z_2\), see ( [18][81]), we can assert that

$$\begin{aligned}&\Delta _j\big (\tau ;\Phi _*\mathfrak {X}|_{U},\Phi \circ \sigma \big )\\ =&\,\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \int _{0}^{\tau }e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\big (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt\\&\,-\frac{\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}( p_0)} +\frac{\Theta (\tau )\wedge X_{\mu _0}(\gamma _{\mu _0}(\tau ))}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} e^{-\int _0^\tau \textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\\ =&\,\Delta _j(\tau ;\mathfrak {X},\sigma )+\frac{{\mathscr {R}}_j(\tau )}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}, \end{aligned}$$

where in the second equality we use \(\Theta (t)=-(D\phi _{\mu _0})_{z}^{-1}\partial _{\mu _j}\phi _{\mu _0}(z)|_{z=\gamma _{\mu _0}(t)}\) again and the definition of \({\mathscr {R}}_j(\tau )\). This concludes the proof of the result. \(\square \)

**Fig. 6**

[image: Fig. 6]

[Full size image][83]

Sketch for the proof of Proposition [5.1][40] where, for \(i=1,2\), we draw \({\hat{W}}_i=W_i\cap \{\mu =\mu _0\}\)

**Proof of Proposition**[5.1][40] We show the result only for \(\partial _{\mu _j}d_+(\mu _0)\) because for \(\partial _{\mu _j}d_-(\mu _0)\) follows verbatim. Since \(\Gamma ^+=\{\Gamma _\mu ^+\}_{\mu \approx \mu _0}\) is a family of generalized stable separatrices, there exist an open subset *U*of \(\Omega \times \mathbb {R}^N\), a diffeomorphism \({{\Phi }\!:{U}\rightarrow {\Phi ( U)\subset \mathbb {R}^2\times \mathbb {R}^N}}\) of the form \(\Phi (x,y,\mu )=(\phi _\mu (x,y),\mu )\), a smooth positive function \({{g}\!:{\Phi (U)}\rightarrow {\mathbb {R}}}\), and a germ of a smooth family \(\hat{\mathfrak {X}}=\{{\hat{X}}_\mu \}_{\mu \approx \mu _0}\) of vector fields on an open subset \({\hat{\Omega }}\subset \mathbb {R}^2\), such that (*a*), (*b*) and (*c*) in Definition [2.1][26] hold.

We claim that we can assume without loss of generality that \(\gamma _{\mu _0}([0,T_+))\times \{\mu _0\}\) is inside *U*. If \(\gamma _{\mu _0}(t)\in U_{\mu _0}\) for all \(t\geqslant 0\), there is nothing to be proved. So let us suppose the contrary and recall, see (*c*) in Definition [2.1][26], that there exists \(q_{\mu _0}\in \Gamma ^+_{\mu _0}\cap \phi _{\mu _0}^{-1}({\hat{\Omega }})\) such that its positive semiorbit by \(X_{\mu _0}\) is contained in \(U_{\mu _0}\), see Figure [6][84]. Then \(q_{\mu _0}=\gamma _{\mu _0}(t_\star )\) for some \(t_\star >0\) and we consider a small neighbourhood \(\underline{{\hat{\Omega }}}\) of \({\hat{s}}_{\mu _0}\) inside \({\hat{\Omega }}\) such that \(\phi _{\mu _0}^{-1}(\underline{{\hat{\Omega }}})\) does not intersect \(\gamma _{\mu _0}([0,t_\star ]).\) Next we take two open neighbourhoods \(W_1\) and \(W_2\) in \(\Omega \times \mathbb {R}^N\) such that \(\gamma _{\mu _0}([0,t_\star ])\times \{\mu _0\}\subset W_1\subset {\overline{W}}_1\subset W_2\), \({\overline{W}}_1\) is compact and \(\phi _{\mu _0}^{-1}(\underline{{\hat{\Omega }}})\times \{\mu _0\}\subset W_2^c\), together with a bump function \({{\rho }\!:{\Omega \times \mathbb {R}^N}\rightarrow {[0,1]}}\) verifying \(\rho |_{W_1}\equiv 1\) and \(\rho |_{W_2^c}\equiv 0.\) We consider also the vector field \(Y\!:=(X_\mu ,0,\ldots ,0)\) on \(\Omega \times \mathbb {R}^N\) and observe that \(\rho Y\) is complete. For each \((p,\mu )\in \Omega \times \mathbb {R}^N,\) let \(\varphi (t,(p,\mu ))\) be the solution of \(\rho Y\) with \(\varphi (0,(p,\mu ))=(p,\mu ).\) We then define \({\underline{\Phi }}(p,\mu )\!:=\Phi (\varphi (t_\star ,(p,\mu ))\), which is clearly a diffeomorphism on \({\underline{U}}\!:=\{(p,\mu )\in \Omega \times \mathbb {R}^N:\varphi (t_\star ,(p,\mu ))\in U\}\) of the form \(\underline{\Phi }(x,y,\mu )=(\underline{\phi }\,_{\!\mu }(x,y),\mu )\). Notice also that \({\underline{\Phi }}|_{U\cap W_2^c}=\Phi \) and \({\underline{\Phi }}({\underline{U}})=\Phi (U).\) Moreover, on account of \(\gamma _{\mu _0}([t_\star ,T_+))\times \{\mu _0\}\subset U\), by construction we have that \(\gamma _{\mu _0}([0,T_+))\times \{\mu _0\}\subset {\underline{U}}\). Taking \(\underline{\hat{\mathfrak {X}}}\!:=\hat{\mathfrak {X}}\) and \({\underline{g}}\!:=g,\) this proves the validity of the claim.

Accordingly we can suppose that the diffeomorphism \(\Phi (x,y,\mu )=(\phi _\mu (x,y),\mu )\) is defined on a neighbourhood of \(\gamma _{\mu _0}([0,T_+))\times \{\mu _0\}\), which is a key point in what follows. In doing so we can assert that

$$\begin{aligned} \partial _{\mu _j}d_+\big (\mu _0;\mathfrak {X},\Gamma ,\sigma \big )&\overset{(1)}{=}\partial _{\mu _j}d_+\big (\mu _0;g\Phi _*\mathfrak {X},\Phi (\Gamma ),\Phi \circ \sigma \big )\\&\overset{(2)}{=}\partial _{\mu _j}d_+\big (\mu _0;\tilde{\mathfrak {X}},\Phi (\Gamma ),\Phi \circ \sigma \big )\\&\overset{(3)}{=}\lim _{\eta \rightarrow +\infty }\Delta _j\big (\eta ;\tilde{\mathfrak {X}},\Phi \circ \sigma \big ) \overset{(4)}{=}\lim _{\eta \rightarrow +\infty }\Delta _j\big (\eta ;g\Phi _*\mathfrak {X},\Phi \circ \sigma \big )\\&\overset{(5)}{=}\lim _{\eta \rightarrow +\infty }\Delta _j\big (h(\eta );\Phi _*\mathfrak {X},\Phi \circ \sigma \big ) \overset{(6)}{=}\lim _{\tau \rightarrow T_+}\Delta _j\big (\tau ;\Phi _*\mathfrak {X},\Phi \circ \sigma \big )\\&\overset{(7)}{=}\lim _{\tau \rightarrow T_+}\left( \Delta _j(\tau ;\mathfrak {X},\sigma )+\frac{{\mathscr {R}}_j^+(\tau )}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)}\right) \\&\overset{(8)}{=}\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \\&\quad \times \left( \lim _{\tau \rightarrow T_+}\big (M_j(\tau )+{\mathscr {R}}_j^+(\tau )\big )-\partial _{\mu _j}\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0) \right) . \end{aligned}$$

Here (1) follows by applying the equality ( [9][85]) in Remark [3.2][65] and taking \(\sigma _{\mu _0}(0)\in U_{\mu _0}\) into account, whereas in (2) we take the smooth family of vector fields \(\tilde{\mathfrak {X}}=\{{\tilde{X}}_\mu \}_{\mu \approx \mu _0}\) given by

$$\begin{aligned} {\tilde{X}}_\mu (p)\!:=\left\{ \begin{array}{ll} g(p;\mu )\big ((\phi _\mu )_*X_\mu \big )(p) & \hbox { if}\ p\in \phi _\mu (U_\mu ), \\ {\hat{X}}_\mu (p) & \hbox { if}\ p\in {\hat{\Omega }}. \end{array} \right. \end{aligned}$$

The equality in (3) follows by applying Lemma [4.1][74] and taking Definition [5.2][76] into account. We remark in this regard, recall Definition [2.1][26], that \({\hat{s}}^+_{\mu _0}\) is a hyperbolic saddle of \({\tilde{X}}_{\mu _0}.\) Next, in order to obtain (4) we use that the integrand in \(\Delta _j\big (\eta ;\tilde{\mathfrak {X}},\Phi \circ \sigma \big )\) is evaluated on a solution \({\tilde{\gamma }}_{\mu _0}(t)\) of \(g(\,\cdot ;\mu _0)(\phi _{\mu _0})_*X_{\mu _0}.\) The equality in (5) is a consequence of Lemma [5.3][86], where *h*is the unique function with \(h(0)=0\) such that \({\tilde{\gamma }}_{\mu _0}(t)=\phi _{\mu _0}\big (\gamma _{\mu _0}(h(t))\big ).\) In order to obtain (6) we use that \(\lim _{\eta \rightarrow +\infty }h(\eta )=T_+\) because the maximal interval of existence of \(\gamma _{\mu _0}\) is \((T_-,T_+).\) The equality in (7) follows by applying Lemma [5.5][87] and, finally, to obtain the one in (8) we express \(\Delta _j(\tau ;\mathfrak {X},\sigma )\) in terms of the function \(M_j(\tau )\), see ( [2][50]). This completes the proof of the result. \(\square \)

## 6 Applications

In this section we illustrate the application of Theorem [A][8] (and Definition [2.1][26]) with some nontrivial examples. In the first one we study the breaking of an invariant straight line that connects two (antipodal) singularities at infinity, see Figure [7][88].

**Fig. 7**

[image: Fig. 7]

[Full size image][89]

Phase portrait in the Poincaré disc of the breaking connection studied in Proposition [6.1][42]. On the left, the unperturbed vector field \(X_{\mu _0}\) and on the right the perturbation \(X_{\mu }\) for \(\mu \approx \mu _0\)

### Proposition 6.1

Let us consider the family of polynomial differential equations of (even) degree \(n\geqslant 2\)

$$\begin{aligned} X_\mu \quad \left\{ \! \begin{array}{l} \dot{x}=P(x,y), \\[2pt] \dot{y}=yq(x,y)+\mu _1+\mu _2x+\cdots +\mu _{n+1}x^n, \end{array} \right. \end{aligned}$$

satisfying \(P(x,0)\ne 0\) for all \(x\in \mathbb {R}\) and \(P_n(1,0)(P_n(1,0)-q_{n-1}(1,0))<0\), where \(P_n\) and \(q_{n-1}\) are the homogeneous parts of *P*and *q*of degrees *n*and \(n-1\), respectively. Setting \(\mu =(\mu _1,\ldots ,\mu _{n+1})\), the vector field \(X_{\mu _0}\) with \(\mu _0\!:=(0,\ldots ,0)\) has an invariant straight line \(\Gamma _{\mu _0}\!:=\{y=0\}\) that connects two antipodal hyperbolic saddles \({\hat{s}}_{\mu _0}^\pm \) at infinity of its Poincaré compactification \(p(X_{\mu _0})\). Each singularity unfolds a family of hyperbolic saddles \(\{{\hat{s}}_\mu ^\pm \}_{\mu \approx \mu _0}\) of \(p(X_\mu )\) at \(\ell _\infty \). Let us consider the separation function \(d(\mu )\) between their stable and unstable separatrices measured on the transverse section \({{\sigma _\mu }\!:{(-\varepsilon ,\varepsilon )}\rightarrow {\Sigma _\mu \subset \{x=0\}}}\) given by \(\sigma _\mu (r)=(0,r)\). Then, for each \(j=1,2,\ldots ,n+1,\) its partial derivative at \(\mu =\mu _0\) is

$$\begin{aligned} \partial _{\mu _j}d(\mu _0)=-\int _{-\infty }^{+\infty }\frac{x^{j-1} e^{-\int _0^x\frac{q(u,0)}{P(u,0)}du}}{|P(x,0)|}dx. \end{aligned}$$

In particular, \(\partial _{\mu _j}d(\mu _0)<0\) when *j*is odd.

### Proof

We consider two diffeomorphisms \((u,v)=\phi _\mu ^\pm (x,y)\!:=\left( \pm \frac{1}{x},\frac{y}{x}\right) \) from the half-plane \(U_\pm \!:=\{\pm x>0\}\) onto the half-plane \(\phi _\mu ^\pm (U_\pm )=\{ u>0\}\). A computation shows that the positive function \({{g}\!:{\{u>0\}}\rightarrow {\mathbb {R}}}\) given by \(g(u,v)= u^{n-1}\) satisfies

$$\begin{aligned} g(u,v)\big ((\phi _\mu ^\pm )_*X_\mu \big )(u,v)= & \textstyle {\mp } u^{n} \big (P\big (\pm \frac{1}{u},\pm \frac{v}{u}\big )u\partial _u \\ & +\big (P\big (\pm \frac{1}{u},\pm \frac{v}{u}\big )v-Q_\mu \big (\pm \frac{1}{u},\pm \frac{v}{u}\big )\big )\partial _v\big ), \end{aligned}$$

where we set \(Q_\mu (x,y)\!:=yq(x,y)+\mu _1+\mu _2x+\cdots +\mu _{n+1}x^n\) for the sake of shortness. Since \(X_\mu \) has degree *n*, the above vector field extends to a smooth vector field \({\hat{X}}_\mu ^\pm \) at \(u=0\) for each \(\mu .\) One can check in addition that \({\hat{s}}^\pm _{\mu _0}\!:=(0,0)\) is a singular point of \({\hat{X}}_\mu ^\pm \) and that the eigenvalues of differential matrix \(D{\hat{X}}_{\mu _0}^\pm \) at \({\hat{s}}^\pm _{\mu _0}\) are \(\lambda _1={\mp } P_n(\pm 1,0)={\mp } P_n(1,0)\) and

$$\begin{aligned} \lambda _2={\mp }(P_{n}(\pm 1,0){\mp } q_{n-1}(\pm 1,0))={\mp }(P_{n}(1,0)-q_{n-1}(1,0)), \end{aligned}$$

where we use that *n*is even. Thus, the assumption on *P*and *q*implies \(\lambda _1\lambda _2<0\) and so \({\hat{s}}_{\mu _0}\) is a hyperbolic saddle of \({\hat{X}}_{\mu _0}^\pm .\)

Let \(\gamma _{\mu _0}(t)=(x(t),0)\) be the solution of \(X_{\mu _0}\) with initial condition \(p_0\!:=\gamma _{\mu _0}(0)=\sigma _{\mu _0}(0)=(0,0)\) and maximal interval of existence \((T_-,T_+)\). Let us assume first that \(P(x,0)>0\) for all \(x\in \mathbb {R}\), so that

$$\begin{aligned} \lim _{t\rightarrow T_\pm }x(t)=\pm \infty . \end{aligned}$$

(20)

This easily implies that \(\lim _{t\rightarrow T_\pm }\phi _{\mu _0}^\pm (\gamma _{\mu _0}(t))=(0,0)={\hat{s}}_{\mu _0}^\pm \). It is clear on the other hand that \({\hat{s}}_{\mu _0}^\pm \) unfolds a family of points \(\{{\hat{s}}_\mu ^\pm \}_{\mu \approx \mu _0}\) such that each \({\hat{s}}_\mu ^\pm \) is a hyperbolic saddle of \({\hat{X}}_\mu ^\pm \) on \(\ell _\infty .\) Here we use the hyperbolicity of \({\hat{s}}_{\mu _0}^\pm \) and the invariance of \(\ell _\infty \) for all the family \(\{{\hat{X}}_\mu ^\pm \}_{\mu \approx \mu _0}.\) Accordingly (see Definition [2.1][26]) the stable separatrix of \({\hat{s}}_\mu ^+\) and the unstable separatrix of \({\hat{s}}_\mu ^-\) form, as we vary \(\mu \approx \mu _0\), a family of generalized stable and unstable separatrices for \(\{X_\mu \}_{\mu \approx \mu _0}\), respectively. It is clear moreover that the invariant straight line \(\Gamma _{\mu _0}\!:=\{y=0\}\) of \(X_{\mu _0}\) is a generalized saddle connection. We can thus apply Theorem [A][8]. To this end let us point out that the diffeomorphisms \(\phi _\mu ^\pm \) do not depend on \(\mu ,\) which simplifies a lot the computations because the summands \({\mathscr {R}}^\pm (\tau )\) in ( [4][58]) are identically zero. That being said, we note first that

$$\begin{aligned} \exp \left( -\int _{0}^t\textrm{div}(X_{0})(\gamma _{\mu _0}(s))ds\right)&=\exp \left( -\int _{0}^{x(t)}\left( \frac{\partial _xP+q}{P}\right) (u,0)du\right) \\&=\frac{P(0,0)}{P(x(t),0)}\exp \left( -\int _{0}^{x(t)}\frac{q(u,0)}{P(u,0)}du\right) , \end{aligned}$$

where in the first equality we make the change of variables \(u=x(s)\) taking \(x'(s)=P(x(s),0)\) into account. Then, on account of

$$\begin{aligned} \partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(0,0)=-P(0,0)\text { and } (X_{\mu _0}\wedge \partial _{\mu _j}X_{\mu _0})(x,0)=x^{j-1}P(x,0), \end{aligned}$$

we obtain that

$$\begin{aligned} \partial _{\mu _j}d(\mu _0)&=\frac{1}{\partial _r\sigma _{0}(0)\wedge X_{0}(0,0)}\int _{T_-}^{T_+}e^{-\int _{0}^t\textrm{div}(X_{0})(\gamma _{\mu _0}(s))ds}\big (X_{0}\wedge \partial _{\mu _j}X_{0}\big )(\gamma _{\mu _0}(t))dt\\&=-\frac{1}{P(0,0)}\int _{-\infty }^{+\infty } x^{j-1}P(x,0)\frac{P(0,0)}{P(x,0)}e^{-\int _{\mu _0}^x\frac{q(u,0)}{P(u,0)}du}\frac{dx}{P(x,0)} \\&=-\int _{-\infty }^{+\infty } \frac{x^{j-1}e^{-\int _{\mu _0}^x\frac{q(u,0)}{P(u,0)}du}}{P(x,0)}dx, \end{aligned}$$

where in the second equality we make the change of variables \(x=x(t)\) and take ( [20][90]) into account. This proves the result when \(P(x,0)>0\) for all \(x\in \mathbb {R}\). The case \(P(x,0)<0\) for all \(x\in \mathbb {R}\) follows exactly the same way using that, instead of ( [20][90]), we have \(\lim _{t\rightarrow T_\pm }x(t)={\mp }\infty \), which yields to the absolute value in the integrand. This completes the proof of the result. \(\square \)

With regard to the assumptions in Proposition [6.1][42], let us note that the stronger conditions \(P_n(1,0)\ne 0\) and \(P(x,0)(P_n(x,y)-xq_{n-1}(x,y))<0\) for all \((x,y)\ne (0,0)\) imply that the boundaries of the half-planes \(\{\pm y>0\}\) in the Poincaré disc are hyperbolic *hemicycles*of \(X_{\mu _0}.\) This is a particular bicycle for which one of the two saddle connections is inside \(\ell _\infty \), so that it remains unbroken along the perturbation. Let us also comment that Proposition [6.1][42] generalizes Lemma B.2 in [[10][91]], where we point out that we take a definition of separation function that has opposite sign to the one used here.

The remaining examples deal with the quadratic perturbations of the so-called Loud’s centers

$$\begin{aligned} Y=y(x-1)\partial _x+(x+D_0x^2+F_0y^2)\partial _y, \end{aligned}$$

which constitutes one of the four different families of quadratic centers. Let us set \(\mu \!:=(D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2)\) and note that the family of vector fields \(\{X_\mu \}_{\mu \approx \mu _0}\) given by

$$\begin{aligned} X_\mu \quad \left\{ \! \begin{array}{l} \dot{x}=\varepsilon _0+y(x-1), \\[2pt] \dot{y}=x+Dx^2+Fy^2+\varepsilon _1y+\varepsilon _2xy, \end{array} \right. \end{aligned}$$

(21)

with \(\mu _0\!:=(D_0,F_0,0,0,0)\) unfolds *Y*. It turns out that this unfolding of *Y*is *versal*provided that \(F_0\ne 1\). Indeed, see [[10][91], Lemma 3.1], any quadratic differential system which is close (in the topology of coefficients) to *Y*for some \((D_0,F_0)\in \mathbb {R}^2\) with \(F_0\ne 1\) can be brought by means of an affine change of coordinates and a constant rescaling of time to \(\{X_\mu \}_{\mu \approx \mu _0}\). The idea of the proof is that the map *F*from \(\mathbb {R}\times \textrm{Aff}(\mathbb {R}^2)\times \mathbb {R}^5\) to the space of quadratic vector fields defined by \(F(k,g,\mu )=kg^*X_\mu \) is a local diffeomorphism at \((1,\textrm{Id},\mu _0)\) because its differential matrix is invertible when \(F_0\ne 1.\)

Recall that the period annulus \({\mathscr {P}}\) of a center is its largest punctured neighbourhood foliated by periodic orbits. Compactifying *Y*to the Poincaré disc, the boundary of \({\mathscr {P}}\) has two connected boundaries, the center itself and a polycycle. We next analyse how this polycycle breaks when *Y*is perturbed inside the versal unfolding \(\{X_\mu \}_{\mu \approx \mu _0}\) given in ( [21][92]). We consider different cases that are depicted in Figure [8][93].

**Fig. 8**

[image: Fig. 8]

[Full size image][94]

Phase portrait of \(Y=y(x-1)\partial _x+(x+D_0x^2+F_0y^2)\partial _y\) in the Poincaré disc for (1) \(D_0\in (-1,0)\) and \(F_0\in (0,1)\), (2) \(-F_0<D_0<-1\), (3) \(D_0\in (-1,0)\) and \(F_0>1\), and (4) \(D_0=-F_0<-1\). We remark that for convenience we draw the center at the origin shifted to the left, so that the vertical invariant straight line is \(\{x=1\}\)

We remark that in all the cases the polycycle is hyperbolic, i.e., the singularities at its vertices are hyperbolic saddles of the compactified vector field *p*(*Y*). Since the hyperbolicity is preserved by a smooth perturbation, each saddle separatrix of *p*(*Y*) unfolds into a family of saddle separatrices of \(\{p(X_\mu )\}_{\mu \approx \mu _0}.\) Thus, see Definition [2.1][26], each finite saddle separatrix of *p*(*Y*) unfolds into a family of generalized saddle separatrices of \(\{X_\mu \}_{\mu \approx \mu _0}.\)

In the next proposition we study the case (1) in Figure [8][93].

### Proposition 6.2

If \(D_0\in (-1,0)\) and \(F_0\in (0,1)\) then \(\Gamma _{\mu _0}=\{x=1\}\) is a generalized saddle connection for the quadratic versal unfolding \(\{X_\mu \}_{\mu \approx \mu _0}\) in ( [21][92]). Moreover its separation function \(d(\mu )\), measured on the transverse section \(\Sigma _\mu \subset \{y=0\}\) parametrized by \(\sigma _\mu (r)=(1-r,0)\) with \(r\approx 0\), can be written as \(d(\mu )=\varepsilon _0\delta (\mu )\), where \(\delta \) is a smooth function in a neighbourhood of \(\mu _0\) such that \(\delta (\mu _0)>0.\)

### Proof

Recall that \(\mu =(D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2)\) and \(\mu _0=(D_0,F_0,0,0,0)\). Since \(\{x=1\}\) is invariant under the flow of \(\left. X_\mu \right| _{\varepsilon _0=0}\), see ( [21][92]), it is clear that \(d(\mu )=\varepsilon _0\delta (\mu )\) for some smooth function \(\delta \) in a neighbourhood of \(\mu _0\). In order to compute \(\delta (\mu _0)=\partial _{\mu _3}d(\mu _0)\) we will apply Proposition [6.1][42]. To this end we consider the affine transformation \(\psi (x,y)=(y,1-x)\), which one can verify it yields to

$$\begin{aligned} \psi _*X_\mu =\big (D+1-(2D+1)y+(\varepsilon _1+\varepsilon _2)x+Fx^2-\varepsilon _2xy+Dy^2\big )\partial _x+(yx-\varepsilon _0)\partial _y \end{aligned}$$

and \((\phi \circ \sigma _\mu )(r)=(0,r)\). Note then that \(\psi _*X_\mu \) verifies the assumptions in Proposition [6.1][42] with \(n=2,\) \(P(x,0)=D_0+1+F_0x^2>0\), \(P_2(1,0)=F_0>0\), \(q(x,y)=q_1(x,y)=x\) and \(P_2(1,0)-q_1(1,0)=F_0-1<0\). We can thus apply that result and in doing so we get

$$\begin{aligned} \partial _{\varepsilon _0}d(\mu _0;\phi _*\mathfrak {X},\phi \circ \sigma )=\int _{-\infty }^{+\infty }\frac{\left( 1+\frac{F_0}{D_0+1}x^2\right) ^{\frac{-1}{2F_0}}}{D_0+1+F_0x^2}dx>0 \end{aligned}$$

due to \(D_0\in (-1,0)\) and \(F_0\in (0,1)\). On the other hand, recall Remark [3.2][65], \(d(\mu ;\mathfrak {X},\sigma )=d(\mu ;\psi _*\mathfrak {X},\psi \circ \sigma )\). Consequently we can assert that \(\partial _{\mu _3}d(\mu _0;\mathfrak {X},\sigma )=\partial _{\mu _3}d(\mu _0;\psi _*\mathfrak {X},\psi \circ \sigma )>0\). Since all the other partial derivatives are equal to zero it follows that \(d(\mu )\) factorizes as \(d(\mu )=\varepsilon _0\delta (\mu )\) for \(\mu \approx \mu _0\) with \(\delta (\mu _0)>0.\) This completes the proof of the result. \(\square \)

The following result is an easy application of Proposition [6.2][43]. Related with it, let us note that in [[7][95]] it is proved that the simultaneous cyclicity of the two period annuli in (1) of Figure [8][93] is exactly 2 in the particular case \((D_0,F_0)=(-\frac{1}{2},\frac{1}{2})\).

### Corollary 6.3

For any \(D_0\in (-1,0)\) and \(F_0\in (0,1)\) there exists a sequence of parameters \(\{\mu _n\}_{n\ge 1}\) with \(\lim _{n\rightarrow +\infty }\mu _n=(D_0,F_0,0,0,0)\) such that the vector field \(X_{\mu _n}\) in ( [21][92]) has two non-nested limit cycles.

### Proof

The unperturbed vector field \(X_{\mu _0}\) has two non-degenerated centers, located at (0, 0) and \((-\frac{1}{D_0},0)\), which unfold into two families of foci \(\{c_\mu \}_{\mu \approx \mu _0}\) and \(\{c'_\mu \}_{\mu \approx \mu _0}\), respectively, verifying \(c_\mu =(0,\varepsilon _0)+\text{ o }(\Vert \mu -\mu _0\Vert )\text { and }[\textstyle c'_\mu =\Big (-\frac{1}{D_0}+\frac{1}{D_0^2}(D-D_0),\) \(\frac{D_0}{D_0+1}\varepsilon _0\Big )+\text{ o }(\Vert \mu -\mu _0\Vert )]\).

**Fig. 9**

[image: Fig. 9]

[Full size image][96]

Phase portrait in the Poincaré disc of \(X_\mu \) when \(d(\mu )>0\), \(\textrm{tr}\big (DX_\mu (c_\mu )\big )>0\) and \(\textrm{tr}\big (DX_\mu (c'_\mu )\big )<0\) with \(\mu \) close enough to \(\mu _0.\) As usual we draw the center at the origin shifted to the left

Moreover, an easy computation shows that the trace of the differential matrix of \(X_\mu \) at \(c_\mu \) and \(c'_\mu \) are

$$\begin{aligned} \textrm{tr}\big (DX_\mu (c_\mu )\big )&=(2F_0+1)\varepsilon _0+\varepsilon _1+\text{ o }(\Vert \mu -\mu _0\Vert ) \end{aligned}$$

and

$$\begin{aligned} \textrm{tr}\big (DX_\mu (c'_\mu )\big )&=\textstyle \frac{D_0(2F_0+1)}{D_0+1}\varepsilon _0+\varepsilon _1-\frac{1}{D_0}\varepsilon _2+\text{ o }(\Vert \mu -\mu _0\Vert ), \end{aligned}$$

respectively. We know on the other hand by Proposition [6.2][43] that the separation function \(d(\mu )\) of the generalized saddle connection \(\Gamma _{\mu _0}=\{x=1\}\), measured on the transverse section \(\Sigma \) given by \(\sigma _\mu (r)=(1-r,0)\) with \(r\approx 0\), can be written as \(d(\mu )=\varepsilon _0\delta (\mu )\) with \(\delta (\mu _0)>0.\) One can verify then that the gradients of \(d(\mu )\), \(\textrm{tr}\big (DX_\mu (c_\mu )\big )\) and \(\textrm{tr}\big (DX_\mu (c'_\mu )\big )\) at \(\mu =\mu _0\) are linearly independent vectors. We can thus think that these three quantities are free parameters. On the other hand, see Figure [9][97], if \(d(\mu )>0\) then there exist two disjoint compact sets \(K_\mu \) and \(K_\mu '\) containing \(c_\mu \) and \(c_\mu '\), respectively, such that \(K_\mu \) is positively invariant and \(K_\mu '\) is negatively invariant. Since the traces control the stability of the foci, by applying the Poincaré-Bendixson Theorem we deduce the existence of at least one limit cycle contained in each compact set by choosing conveniently \(\mu \approx \mu _0\) so that \(d(\mu )>0\), \(\textrm{tr}\big (DX_\mu (c_\mu )\big )>0\) and \(\textrm{tr}\big (DX_\mu (c'_\mu )\big )<0\). Figure [9][97] displays the phase portrait in the Poincaré disc of \(X_\mu \) in case that exactly two limit cycles \(\gamma _\mu \) and \(\gamma _\mu '\) exist. This proves the result. \(\square \)

In the next result we study the cases (2) and (3) in Figure [8][93]. For the parameter values under consideration it turns out that the hyperbola \(\{y^2=Q(x;D_0,F_0)\}\), with

$$\begin{aligned} Q(x;D_0,F_0)\!:=\frac{D_0 }{1- F_0}x^{2}+\frac{2\left( D_0-F_0 +1\right) }{\left( 1-F_0\right) \left( 1-2 F_0 \right) }x+\frac{F_0 -D_0-1}{ F \left( 1-F \right) \left( 1-2 F \right) }, \end{aligned}$$

is invariant under the flow of the vector field *Y*. We also define \(\left[ x_\mu \!:=\frac{F(D-F+1)+\ sqrt{F(F-1)(D+F)(F-D-1)}}{DF( 2F-1)}\right] \), which is the smallest real root of \(Q(x;D,F)=0\).

### Proposition 6.4

If \(D_0<0\) and \(F_0>\max (-D_0,1)\) then the branch of hyperbola

$$\begin{aligned} \Gamma _{\mu _0}=\big \{(x,y)\in \mathbb {R}^2 : y^{2}=Q(x;D_0,F_0),\;x\leqslant x_{\mu _0}\big \} \end{aligned}$$

is a generalized saddle connection for the quadratic versal unfolding \(\{X_\mu \}_{\mu \approx \mu _0}\) in ( [21][92]). Moreover its separation function \(d(\mu )\), measured on the transverse section \(\Sigma _\mu \subset \{y=0\}\) parametrized by \(\sigma _\mu (r)=(x_\mu -r,0)\) with \(r\approx 0\), satisfies \(\partial _Dd(\mu _0)=\partial _Fd(\mu _0)=0\), \(\partial _{\varepsilon _0}d(\mu _0)<0\) and \(\partial _{\varepsilon _1}d(\mu _0)>0\).

### Proof

In this case, following the notation in Definition [2.1][26], one can verify that if we take the diffeomorphism \((u,v)=\phi _\mu (x,y)\!:=(\frac{1}{1-x},\frac{y}{1-x})\) from \(U_\mu =\{x<1\}\) onto \(\phi _\mu (U_\mu )=\{u>0\}\) and the positive function \({{g}\!:{\{u>0\}}\rightarrow {\mathbb {R}}}\) given by \(g(u,v)\!:=u\) then \(g(\phi _\mu )_*X_\mu \) extends to a polynomial vector field \({\hat{X}}_\mu .\) One can check moreover that \({\hat{X}}_{\mu _0}\) has two hyperbolic saddles \({\hat{s}}_{\mu _0}^\pm \) at \(\phi _{\mu _0}(\Gamma _{\mu _0})\cap \{u=0,\pm v>0\}.\) Hence \({\hat{s}}_{\mu _0}^\pm \) unfolds a family of points \(\{{\hat{s}}_\mu ^\pm \}_{\mu \approx \mu _0}\) such that each \({\hat{s}}_\mu ^\pm \) is a hyperbolic saddle of \({\hat{X}}_\mu \) on \(\ell _\infty .\) Thus, see Definition [2.1][26], the stable separatrix of \({\hat{s}}_\mu ^+\) and the unstable separatrix of \({\hat{s}}_\mu ^-\) form, as \(\mu \approx \mu _0\), a family of generalized stable and unstable separatrices for \(\{X_\mu \}_{\mu \approx \mu _0}\), respectively. Furthermore they have a generalized saddle connection at the branch of hyperbola \(\Gamma _{\mu _0}\).

Since the hyperbola \(\{y^2=Q(x;D,F)\}\) is a invariant under the flow of any \(X_\mu \) with \(\varepsilon _0=\varepsilon _1=\varepsilon _2=0\) and, on the other hand, \(\sigma _\mu (0)\in \{y^2=Q(x;D,F)\}\), it turns out that \(d(\mu )=0\) for all \(\mu =(D,F,0,0,0)\). Consequently, \(\partial _Dd(\mu _0)=\partial _Fd(\mu _0)=0\). In order to compute the other partial derivatives, note that we can apply the formula in ( [5][98]) because \(\phi _\mu =\phi _\mu ^\pm \) does not depend on \(\mu \). Hence

$$\begin{aligned} \partial _{\varepsilon _i}d(\mu _0) & =\frac{1}{\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)} \int _{T_-}^{T_+}e^{-\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds}\nonumber \\ & \quad \times \big (X_{\mu _0}\wedge \partial _{\varepsilon _i}X_{\mu _0}\big )(\gamma _{\mu _0}(t))dt. \end{aligned}$$

(22)

where \(\gamma _{\mu _0}(t)=(x(t),y(t))\) is the solution of \(X_{\mu _0}=y(x-1)\partial _x+(x+D_0x^2+F_0y^2)\partial _y\) passing through the point \(p_0\!:=\sigma _{\mu _0}(0)=(x_{\mu _0},0)\in \Gamma _{\mu _0}\) at \(t=0\) and \((T_-,T_+)\) is its maximal interval of existence. Due to \(\textrm{div}(X_{\mu _0})=(2F_0+1)y\), we get that

$$\begin{aligned} \exp \left( -\int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}(s))ds\right) & =\exp \left( -(2F_0+1)\int _{x_{\mu _0}}^{x(t)}\frac{y dx}{y(x-1)}\right) \\ & =\left( \frac{1-x_{\mu _0}}{1-x(t)}\right) ^{2F_0+1}, \end{aligned}$$

where in the first equality we make the change of coordinates \(x=x(s)\) taking \(x'=y(x-1)\) into account. An easy computation shows that

$$\begin{aligned} & \left[ \big (X_{\mu _0}\wedge \partial _ {\varepsilon _0}X_{\mu _0}\big )( \gamma _0(t))=x(t)+D_0x(t)^2+F_ 0y(t)^2=y'(t)>0\right] \\ & \hbox { for all}\ t\in (T_-,T_+). \end{aligned}$$

Since \(\partial _r\sigma _{\mu _0}(0)\wedge X_{\mu _0}(p_0)=-x_{\mu _0}(1+D_0x_{\mu _0})<0\), from ( [22][99]) we get that \(\partial _{\varepsilon _0}d(\mu _0)<0\). Similarly, one can verify that \(\big (X_{\mu _0}\wedge \partial _{\varepsilon _1}X_{\mu _0}\big )(\gamma _0(t))=y^2(t)\big (x(t)-1\big )<0\) for all \(t\in (T_-,T_+)\), which implies \(\partial _{\varepsilon _1}d(\mu _0)>0.\) This concludes the proof of the result. \(\square \)

The partial derivative \(\partial _{\varepsilon _2}d(\mu _0)\) not given in Proposition [6.4][44] can be expressed in terms of hypergeometric functions and it changes sign on \(\big \{D_0<0,\ F_0>\max (-D_0,1)\big \}\). We prefer not to include this computation for the sake of shortness.

Finally we study the case (4) in Figure [8][93], in which two different generalized saddle connections occur.

### Proposition 6.5

If \(D_0=-F_0\) and \(D_0<-1\) then each half-line

$$\begin{aligned} \Gamma _{\mu _0}^\pm \!:=\{(x,y)\in \mathbb {R}^2:\pm \sqrt{D_0(D_0+1)}\,y=D_0x+1>0\} \end{aligned}$$

is a generalized saddle connection for the quadratic versal unfolding \(\{X_\mu \}_{\mu \approx \mu _0}\) in ( [21][92]). Its separation function \(d^\pm (\mu )\), measured on the transverse section \(\Sigma _\mu ^\pm \subset \{x=0\}\) parametrized by \(\sigma ^\pm _\mu (r)=\left( 0,\frac{\pm 1}{\sqrt{D(D+1)}}{\mp } r\right) \) with \(r\approx 0\), satisfies \({\mp }\partial _Dd^\pm (\mu _0)={\mp }\partial _Fd^\pm (\mu _0)>0\), \(\partial _{\varepsilon _0}d^\pm (\mu _0)>0\), \(\partial _{\varepsilon _1}d^\pm (\mu _0)<0\) and \(\partial _{\varepsilon _2}d^\pm (\mu _0)=0.\)

### Proof

One can verify that the vector field \(X_{\mu _0}\) has a hyperbolic saddle at \(s_{\mu _0}^0\!:=(-1/D_0,0)\), which unfolds a family of points \(\{s_{\mu }^0\}_{\mu \approx \mu _0}\) such that \(s_{\mu }^0\) is a hyperbolic saddle of \(X_\mu \) for each \(\mu .\) On the other hand, an easy computation shows that the diffeomorphism \((u,v)=\phi _\mu (x,y)\!:=(\frac{1}{1-x},\frac{y}{1-x})\) defined on \(U=\{x<1\}\) and the positive function \({{g}\!:{\phi (U)=\{u>0\}}\rightarrow {\mathbb {R}}}\) given by \(g(u,v)\!:=u\) satisfy \(g(\phi _\mu )_*X_\mu ={\hat{X}}_\mu \) with

$$\begin{aligned} & {\hat{X}}_\mu \!:=(-v+\varepsilon _0u^2)u\partial _u\\ & +\left( D-(2D+1)u-\varepsilon _2v+(D+1)u^2+(\varepsilon _1+\varepsilon _2)uv-(1-F)v^2+\varepsilon _0u^2v\right) \partial _v. \end{aligned}$$

In addition, \({\hat{X}}_{\mu _0}\) has two hyperbolic saddles at \({\hat{s}}_{\mu _0}^\pm \!:=\left( 0,\pm \frac{\sqrt{-D}}{\sqrt{F-1}}\,\right) \in \ell _\infty \), which in turn unfold two families of hyperbolic saddles \(\{{\hat{s}}_{\mu }^\pm \}_{\mu \approx \mu _0}\) at infinity for \(\{{\hat{X}}_\mu \}_{\mu \approx \mu _0}.\) The families of stable and unstable (finite) separatrices of \(\{{\hat{s}}_{\mu }^+\}_{\mu \approx \mu _0}\) and \(\{{\hat{s}}_{\mu }^-\}_{\mu \approx \mu _0}\) constitute, respectively, two families \(\{\Gamma _{\mu }^+\}_{\mu \approx \mu _0}\) and \(\{\Gamma _{\mu }^-\}_{\mu \approx \mu _0}\) of generalized stable and unstable saddle separatrices of \(\{X_\mu \}_{\mu \approx \mu _0}.\) Moreover, the half-line \(\Gamma _{\mu _0}^+\) (respectively, \(\Gamma _{\mu _0}^-\)) is a generalized saddle connection between \({\hat{s}}_\mu ^+\) (respectively, \({\hat{s}}_{\mu _0}^-\)) and \(s_{\mu _0}^0\).

Next we apply Theorem [A][8] to compute the partial derivatives of each separation function \(d^\pm (\mu ).\) Since the diffeomorphism \(\phi _\mu \) does not depend on \(\mu \), we can apply the formula in ( [5][98]). With this aim in view, let \(\gamma _{\mu _0}^\pm (t)=(x^\pm (t),y^\pm (t))\) be the solution of \(X_{\mu _0}=y(x-1)\partial _x+(x+D_0x^2+F_0y^2)\partial _y\) passing through the point \(p_0^\pm \!:=\sigma _{\mu _0}^\pm (0)\in \Gamma _{\mu _0}^\pm \) at \(t=0\). Since \(X_{\mu _0}\) is reversible with respect to the straight line \(\{y=0\}\), it turns out that \(x^-(t)=x^+(-t)\) and \(y^-(t)=-y^+(-t)\). Moreover,

$$\begin{aligned} \lim _{t\rightarrow {\mp }\infty } x^\pm (t)=-1/D_0\text { and }\lim _{t\rightarrow T_\pm } x^\pm (t)=-\infty . \end{aligned}$$

(23)

On the other hand, due to \(\textrm{div}(X_{\mu _0})=(1-2D_0)y\),

$$\begin{aligned} \int _0^t\textrm{div}(X_{\mu _0})(\gamma _{\mu _0}^\pm (s))ds=(1-2D_0)\int _{0}^{x^\pm (t)}\frac{ydx}{y(x-1)}=(1-2D_0)\log \left( 1-x^\pm (t)\right) , \end{aligned}$$

where we perform the change of variables \(x=x^\pm (s).\) In addition, we easily get that \(\partial _DX_{\mu _0}=(x^2-y^2)\partial _y,\) \(\partial _F X_{\mu _0}=y^2\partial _y,\) \(\partial _{\varepsilon _0}X_{\mu _0}=\partial _x,\) \(\partial _{\varepsilon _1}X_{\mu _0}=y\partial _y\) and \(\partial _{\varepsilon _2}X_{\mu _0}=xy\partial _y\), so that

$$\begin{aligned} X_{\mu _0}\wedge \partial _\nu X_{\mu _0}= \left\{ \begin{array}{ll} x^2y(1-x) & \text {if }\nu =D,\\ y^3(1-x) & \text {if }\nu =F,\\ -x-D_0(x^2-y^2) & \text {if }\nu =\varepsilon _0,\\ y^2(1-x) & \text {if }\nu =\varepsilon _1,\\ xy^2(1-x) & \text {if }\nu =\varepsilon _2. \end{array} \right. \end{aligned}$$

(24)

Taking \(\partial _r\sigma ^\pm _{\mu _0}(0)\wedge X_{\mu _0}(p^\pm _0) =-\frac{1}{\sqrt{D_0(D_0+1)}}\) also into account, the application of ( [5][98]) in Theorem [A][8] yields

$$\begin{aligned} \partial _\nu d^\pm (\mu _0) ={\mp }\sqrt{D_0(D_0+1)}\int _{-1/D_0}^{-\infty }(1-x)^{2D_0-1} \frac{X_{\mu _0}\wedge \partial _\nu X_{\mu _0}}{y(x-1)}\Big |_{y=\pm \frac{D_0x+1}{\sqrt{D_0(D_0+1)}}}dx, \end{aligned}$$

where we make the change of variables \(x=x^\pm (t)\) again and take ( [23][100]) into account. From this expression, and using ( [24][101]) in each case, some easy computations show that

$$\begin{aligned} \partial _Dd^\pm (\mu _0)= \partial _F d^\pm (\mu _0)={\mp } \frac{\left( 1+\frac{1}{D_0}\right) ^{2D_0+\frac{1}{2}}}{2D_0(2D_0+1)},\quad \partial _{\varepsilon _1}d^\pm (\mu _0)= \frac{\left( 1+\frac{1}{D_0}\right) ^{2D_0+1}}{2(2D_0+1)}, \end{aligned}$$

\(\partial _{\varepsilon _0}d^\pm (\mu _0)= \frac{1}{2}\left( 1+\frac{1}{D_0}\right) ^{2D_0}\) and \(\partial _{\varepsilon _2}d^\pm (\mu _0)=0.\) This concludes the proof of the result. \(\square \)

**Fig. 10**

[image: Fig. 10]

[Full size image][102]

Symbolic picture in the 5-dimensional space with coordinates \((D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2)\). The dotted varieties represent the two surfaces defined by the equations \(\{F=-D{\mp }\varepsilon _1\sqrt{D(D+1)},\ \varepsilon _0=0,\ \varepsilon _2=D\varepsilon _1\}\), which are contained in the hypersurfaces \(\{d^\pm (\mu )=0\}\), respectively. The surface defined by \(\{F+D=0\), \(\varepsilon _0=0\), \(\varepsilon _1=0\}\) is contained in 3-dimensional variety \(\{d^+(\mu )=d^-(\mu )=0\}\), which locally coincides with the graph of a smooth function \((F,\varepsilon _0)=g(D,\varepsilon _1,\varepsilon _2)\)

We conclude the paper by making some comments regarding this last result. First of all, and this is a general property of the family \(\{X_\mu \}_{\mu \approx \mu _0}\) in ( [21][92]), one can verify \(\phi _*X_\mu =-X_{\tau (\mu )}\) where \(\phi (x,y)\!:=(x,-y)\) and \(\tau (D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2)\!:=(D,F,-\varepsilon _0,-\varepsilon _1,-\varepsilon _2)\). Since \(\phi _\mu (\Gamma ^\pm _{\mu _0})=\Gamma ^{\mp }_{\mu _0}\) and \(\phi \circ \sigma _\mu ^\pm =\sigma _\mu ^{\mp }\), we deduce that

$$\begin{aligned} d^\pm (\mu )=d(\mu ,\mathfrak {X},\Gamma ^\pm ,\sigma ^\pm )=d(\tau ,-\mathfrak {X},\Gamma ^{\mp },\sigma ^{\mp }) & =-d(\tau (\mu ),\mathfrak {X},\Gamma ^{\mp },\sigma ^{\mp })\\ & =-d^{\mp }(\tau (\mu )). \end{aligned}$$

Accordingly, \(\partial _\nu d^\pm (\mu _0)=-\partial _\nu d^{\mp }(\mu _0)\partial _\nu \tau (\mu _0)\) for each \(\nu \in \{D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2\}\). On the other hand, \(d^\pm ({\hat{\mu }})=0\) for any \({\hat{\mu }}=(D,-D,0,0,-\varepsilon _2)\) because the invariant straight-line

$$\begin{aligned} \left\{ y=\frac{\varepsilon _2\pm \sqrt{4D(D+1)+\varepsilon _2^2}}{2(D+1)}\left( x+\frac{1}{D}\right) \right\} \end{aligned}$$

of \(X_{{\hat{\mu }}}\) contains a saddle connection. Similarly, \(d^\pm ({\bar{\mu }})=0\) for any \({\bar{\mu }}=(D,-D{\mp }\varepsilon _1\sqrt{D(D+1)},0,\varepsilon _1,D\varepsilon _1)\) because an easy computation shows that

$$\begin{aligned} \left\{ y=\pm \frac{Dx+1}{\sqrt{D(D+1)}}\right\} \end{aligned}$$

is an invariant straight-line of \(X_{{\bar{\mu }}}\) that contains a saddle connection as well. Note finally that the differential matrix of the map \(\mu \mapsto \big (d^+(\mu ),d^-(\mu )\big )\) at \(\mu =\mu _0\) has a \(2\times 2\) minor different from zero. Indeed, it follows by Proposition [6.5][45] that \(\partial _F d^+(\mu _0)\partial _{\varepsilon _0}d^-(\mu _0)-\partial _{\varepsilon _0}d^+(\mu _0)\partial _Fd^-(\mu _0)<0\) for any \(\mu _0=(D_0,-D_0,0,0,0)\) with \(D_0<-1\). Consequently, by the implicit function theorem, there exists a neighbourhood *U*of \(\mu _0\) in \(\mathbb {R}^5\) and a smooth function *g*such that both connections remain unbroken for \(X_\mu \) with \(\mu =(D,F,\varepsilon _0,\varepsilon _1,\varepsilon _2)\in U\) if, and only if, \((F,\varepsilon _0)=g(D,\varepsilon _1,\varepsilon _2).\) In other words, for \(\mu \in U\), the intersection \(\{d^+(\mu )=0\}\cap \{d^-(\mu )=0\}\) is the graph of *g*, see Figure [10][103]. In addition, the involution \(\tau \) exchanges the hypersurfaces \(\{d^+(\mu )=0\}\) and \(\{d^-(\mu )=0\}\).

## Data Availability

No datasets were generated or analysed during the current study.

## References

1.

Andronov, A.A., Leontovich, E.A., Gordon, I.I., Maier, A.G.: “Theory of bifurcations of dynamical systems on a plane”, Halsted Press [John Wiley & Sons], New York-Toronto; Israel Program for Scientific Translations, Jerusalem-London, (1973)

2.

Arnold, V.I.: Instability of dynamical systems with several degrees of freedom. Soviet Math. Dokl. **5**, 581–585 (1964)

[Google Scholar][104]

3.

Artés, J.C., Dumortier, F., Llibre, J.: Qualitative theory of planar differential systems. Universitext, Springer-Verlag, Berlin (2006)

[Google Scholar][105]

4.

Abramowitz, M., Stegun, I.A.: “Handbook of mathematical functions with formulas, graphs, and mathematical tables”, Dover, NewYork, (1992), reprint of the 1972 edition

5.

Chicone, C.: “Ordinary Differential Equations with Applications”, Texts Appl. Math., **34**, Springer, New York, (2024)

6.

Duff, G.F.D.: Limit cycles and rotated vector fields. Ann. of Math. **2**(67), 15–31 (1953)

[Article][106] [MathSciNet][107] [Google Scholar][108]

7.

Françoise, J.-P., Gavrilov, L.: Perturbation theory of the quadratic Lotka-Volterra double center. Commun. Contemp. Math. **24**(5), 2150064 (2022)

[Article][109] [MathSciNet][110] [Google Scholar][111]

8.

Kelley, A.: The stable, center-stable, center, center-unstable, unstable manifolds. J. Differential Equations **3**, 546–570 (1967)

[Article][112] [MathSciNet][113] [Google Scholar][114]

9.

Marín, D., Villadelprat, J.: Asymptotic expansion of the dulac map and time for unfoldings of hyperbolic saddles: general setting. J. Differential Equations **275**, 684–732 (2021)

[Article][115] [MathSciNet][116] [Google Scholar][117]

10.

Marín, D., Villadelprat, J.: The cyclicity of hyperbolic hemicycles. J. Differential Equations **433**, 113281 (2025)

[Article][118] [MathSciNet][119] [Google Scholar][120]

11.

Melnikov, V.K.: On the stability of the center for time periodic perturbations. Trans. Moscow Math. Soc. **12**, 1–57 (1963)

[MathSciNet][121] [Google Scholar][122]

12.

Perko, L.M.: Homoclinic loop and multiple limit cycle bifurcation surfaces. Trans. Amer. Math. Soc. **344**, 101–130 (1994)

[Article][123] [MathSciNet][124] [Google Scholar][125]

13.

Perko, L.M.: “Differential equations and dynamical systems”, Texts Appl. Math., **7**, Springer-Verlag, New York, (2001)

14.

Poincaré, H.: Sur les équations de la dynamique et le problème des trois corps. Acta Math. **13**, 1–270 (1890)

[Google Scholar][126]

15.

Roussarie, R.: “Bifurcations of planar vector fields and Hilbert’s sixteenth problem’’ [2013] reprint of the, 1998th edn. Modern Birkhäuser Classics. Birkhäuser/Springer, Basel (1998)

[Book][127] [Google Scholar][128]

16.

Schecter, S.: The saddle-node separatrix-loop bifurcation. SIAM J. Math. Anal. **18**, 1142–1156 (1987)

[Article][129] [MathSciNet][130] [Google Scholar][131]

17.

Sotomayor, J.: “Estabilidade estrutural de primeira ordem e variedades de Banach”, Doctoral thesis, IMPA, Brazil, (1964)

[Download references][132]

## Funding

Open Access Funding provided by Universitat Autonoma de Barcelona.

## Author information

### Authors and Affiliations

1.

Autonomous University of Barcelona, Cerdanyola del Vallès, Spain

D. Marín & J. Villadelprat

Authors

1. D. Marín

[View author publications][133]

Search author on: [PubMed][134] [Google Scholar][135]

2. J. Villadelprat

[View author publications][136]

Search author on: [PubMed][137] [Google Scholar][138]

### Contributions

D.M. and J.V. equally contributed in all the process giving rise to the manuscript

### Corresponding author

Correspondence to [D. Marín][139].

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This work has been partially funded by the Ministry of Science, Innovation and Universities of Spain through the grants PID2021-125625NB-I00 and PID2022-136613NB-I00, and by the Agency for Management of University and Research Grants of Catalonia through the grants 2021SGR00113 and 2021SGR01015.

## A Reformulation of the Melnikov Integral in Terms of Forms

### A Reformulation of the Melnikov Integral in Terms of Forms

We consider a vector field \(X=A\partial _x+B\partial _y\) on \(\mathbb {R}^2\) and its dual 1-form \(\omega =i_X\Omega =-Bdx+Ady\), where \(\Omega =dx\wedge dy\) is the area 2-form and \(i_X\Omega \) is the 1-form defined by \((i_X\Omega )(W)=\Omega (X,W)\). The divergence \(\textrm{div}(X)=\partial _xA+\partial _yB\) of *X*satisfies \(d\omega = \textrm{div}(X)\Omega \).

Let \(\Gamma \) be a non-periodic orbit of *X*and let \(\Sigma \) be a transverse section to \(\Gamma \). Given any \(p\in \Sigma \), we denote by \(t\mapsto \gamma _p(t)\) the solution of *X*passing through \(\gamma _p(0)=p\). We define a function *f*on an open neighborhood of \(\Gamma \) as follows: given any \(q\in \textrm{Im}(\gamma _p)\) we take a flow box *B*of *X*with \(p,q\in B\) and, for any \((x,y)\in B,\) we define

$$\begin{aligned} f(x,y)=\exp \left( -\int _0^{t(x,y)}\textrm{div}(X)\circ \gamma _{p(x,y)}(s)ds\right) , \end{aligned}$$

where \(p(x,y)\in \Sigma \) and \(t(x,y)\in \mathbb {R}\) are uniquely defined satisfying \(\gamma _{p(x,y)}(t(x,y))=(x,y)\). We claim that *f*is an integrating factor of *X*with \(f|_\Sigma \equiv 1\). To see this note first that, by definition,

$$\begin{aligned} f\circ \gamma _p(t)=\exp \left( -\int _0^t \textrm{div}(X)\circ \gamma _p(s)\,ds\right) \end{aligned}$$

for all \(p\in \Sigma \) and *t*in its maximal interval of existence. In particular, \(f|_\Sigma \equiv 1\). If \(q=\gamma _p(t_0)\) then

$$\begin{aligned} X(-\log f)(q)=\left. \partial _t(-\log f\circ \gamma _p(t))\right| _{t=t_0}=\textrm{div}(X)\circ \gamma _p(t_0)=\textrm{div}(X)(q), \end{aligned}$$

so that, \(\frac{df}{f}(X)+\textrm{div}(X)=0\). Let \(Y=C\partial _x+D\partial _y\) be a vector field defined outside the singular locus of *X*verifying that

$$\begin{aligned} 1=\Omega (X,Y)=AD-BC=\omega (Y). \end{aligned}$$

On account of \(\omega (X)=0\), we have that \(\left( \frac{df}{f}\wedge \omega \right) (X,Y)=\frac{df}{f}(X)\,\omega (Y)=\frac{df}{f}(X)=-\textrm{div}(X)=-d\omega (X,Y).\) Since \(\{X,Y\}\) is a basis of \(\mathbb {R}^2\) outside the singular locus of *X*we deduce that

$$\begin{aligned} \frac{df}{f}\wedge \omega +d\omega =0 \end{aligned}$$

and, consequently, \(d(f\omega )=df\wedge \omega +f d\omega =f\left( \frac{df}{f}\wedge \omega +d\omega \right) =0.\) This proves the claim.

Let us consider any other vector field \(Z=P\partial _x+Q\partial _y\) and let \(\nu =i_Z\Omega =-Qdx+Pdy\) be its dual 1-form. Note that

$$\begin{aligned} \Omega (X,Z)=X\wedge Z=AQ-BP=-\nu (X). \end{aligned}$$

Therefore, if \(t\mapsto \gamma (t)\) is a solution of *X*with \(\gamma (0)\in \Sigma \) and maximal interval of existence \((T_-,T_+)\) then, setting \(\Gamma =\text {Im}(\gamma )\),

$$\begin{aligned} \int _\Gamma f\nu&=\int _{T_-}^{T_+}(f\circ \gamma )(t)\nu _{\gamma (t)}(\gamma '(t))dt \\ &=\int _{T_-}^{T_+}\exp \left( -\int _0^t\textrm{div}(X)\circ \gamma (s)\,ds\right) \nu _{\gamma (t)}\big (X(\gamma (t))\big )dt\\&=-\int _{T_-}^{T_+}\exp \left( -\int _0^t\textrm{div}(X)\circ \gamma (s)\,ds\right) \big (X\wedge Z\big )\circ \gamma (t)\,dt. \end{aligned}$$

Let \(\{X_\varepsilon \}_{\varepsilon \approx 0}\) be a smooth family of vector fields on \(\mathbb {R}^2\) with families of generalized stable and unstable separatrices having a generalized saddle connection at \(\Gamma \). Assume in addition that \(\partial _\varepsilon \phi _0^\pm \equiv 0\). In this case the application of the above equality with \(Z=\partial _{\varepsilon }X_\varepsilon |_{\varepsilon =0}\) shows that we can rewrite ( [5][98]) in Theorem [A][8] as

$$\begin{aligned} \partial _\varepsilon d(0)=\frac{-1}{\Omega (\partial _r\sigma (0),X_0(p_0))}\int _\Gamma fi_{\partial _\varepsilon X_\varepsilon |_{\varepsilon =0}}\Omega , \end{aligned}$$

(25)

where *f*is an integrating factor of \(i_{X_0}\Omega \) in a neighbourhood of \(\Gamma \) such that \(f|_{\Sigma }\equiv 1\). We note that, in a “flow-box neighbourhood” of \(\Gamma \), such an integrating factor *f*always exists and it is also unique because the quotient of two integrating factors is a first integral.

On the other hand, if \({\hat{\Omega }}=k(x,y)\Omega \) with \(k(x,y)\ne 0\) is another area form and \({\hat{f}}\) is the integrating factor of \(i_X{\hat{\Omega }}\) such that \({\hat{f}}|_{\Sigma }\equiv 1\) then \({\hat{f}}=fh/k\), where *h*is the first integral of \(X_0\) such that \(h|_{\Sigma }=k|_{\Sigma }\). Moreover

$$\begin{aligned} -\int _\Gamma {\hat{f}}i_Z{\hat{\Omega }}=-\int _\Gamma {\hat{f}}k i_Z\Omega =-\int _\Gamma hf i_Z\Omega =-h(p_0)\int _\Gamma fi_Z\Omega =-k(p_0)\int _\Gamma fi_Z\Omega \end{aligned}$$

and, consequently,

$$\begin{aligned} -\frac{1}{{\hat{\Omega }}(\sigma '(0),X_0(p_0))}\int _\Gamma {\hat{f}} i_Z{\hat{\Omega }}=-\frac{1}{\Omega (\sigma '(0),X_0(p_0))}\int _\Gamma fi_Z\Omega , \end{aligned}$$

where \(Z=\partial _{\varepsilon }X_\varepsilon |_{\varepsilon =0}\).

Finally, let *S*be an *orientable*surface with area form \(\Omega _S\) and let \(\{X_\varepsilon \}_{\varepsilon \approx 0}\) be a smooth family of vector fields on *S*satisfying the previous conditions. Since the generalized saddle connection \(\mathbb {R}\simeq \Gamma \subset S\) is contractible, there exists an open neighborhood of \(\Gamma \) in *S*diffeomorphic to \(\mathbb {R}^2\) where we can write \(\Omega _S=k(x,y) dx\wedge dy\) with \(k(x,y)\ne 0\). Hence the derivative of the separation function of \(\Gamma \) in this more general context is also given by the expression in ( [25][140]).

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][141].

[Reprints and permissions][142]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [143]

### Cite this article

Marín, D., Villadelprat, J. Derivatives of the Separation Function of Generalized Saddle Connections. *Qual. Theory Dyn. Syst.***24**, 227 (2025). https://doi.org/10.1007/s12346-025-01379-8

[Download citation][144]

-

Received: 08 May 2025

-

Accepted: 15 September 2025

-

Published: 03 October 2025

-

Version of record: 03 October 2025

-

DOI: https://doi.org/10.1007/s12346-025-01379-8

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Saddle connection][145]
- [Separation function][146]
- [Polycycle][147]

### Mathematics Subject Classification

- [34C37][148]
- [34C07][149]
- [34C23][150]

### Profiles

1. D. Marín [View author profile][151]
2. J. Villadelprat [View author profile][152]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s12346-025-01379-8.pdf
[3]: /article/10.1007/s12346-025-01379-8/save-research?_csrf=yHZs92MlVMJCr-mQmUuQYOFe26oFVBjg
[4]: /saved-research
[5]: /journal/12346
[6]: /journal/12346/aims-and-scope
[7]: https://submission.nature.com/new-submission/12346/3
[8]: /article/10.1007/s12346-025-01379-8#FPar6
[9]: https://link.springer.com/10.1140/epjb/s10051-023-00491-5?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s12648-023-02689-w?fromPaywallRec=false
[11]: https://link.springer.com/10.1007/s10884-022-10152-3?fromPaywallRec=false
[12]: /subjects/cell-cycle-exit
[13]: /subjects/differential-equations
[14]: /subjects/dynamical-systems
[15]: /subjects/hyperbolic-geometry
[16]: /subjects/ordinary-differential-equations
[17]: /subjects/partial-differential-equations-on-manifolds
[18]: /subjects/invariant-manifolds-and-dynamical-systems-analysis
[19]: /article/10.1007/s12346-025-01379-8#Fig1
[20]: /article/10.1007/s12346-025-01379-8#ref-CR14
[21]: /article/10.1007/s12346-025-01379-8#ref-CR6
[22]: /article/10.1007/s12346-025-01379-8#ref-CR11
[23]: /article/10.1007/s12346-025-01379-8#ref-CR17
[24]: /article/10.1007/s12346-025-01379-8#ref-CR2
[25]: /article/10.1007/s12346-025-01379-8#ref-CR1
[26]: /article/10.1007/s12346-025-01379-8#FPar1
[27]: /article/10.1007/s12346-025-01379-8#Equ1
[28]: /article/10.1007/s12346-025-01379-8/figures/1
[29]: /article/10.1007/s12346-025-01379-8#ref-CR12
[30]: /article/10.1007/s12346-025-01379-8#ref-CR15
[31]: /article/10.1007/s12346-025-01379-8#Sec2
[32]: /article/10.1007/s12346-025-01379-8#Sec3
[33]: /article/10.1007/s12346-025-01379-8#FPar7
[34]: /article/10.1007/s12346-025-01379-8#FPar9
[35]: /article/10.1007/s12346-025-01379-8#FPar10
[36]: /article/10.1007/s12346-025-01379-8#Sec4
[37]: /article/10.1007/s12346-025-01379-8#ref-CR5
[38]: /article/10.1007/s12346-025-01379-8#ref-CR13
[39]: /article/10.1007/s12346-025-01379-8#Sec5
[40]: /article/10.1007/s12346-025-01379-8#FPar15
[41]: /article/10.1007/s12346-025-01379-8#Sec6
[42]: /article/10.1007/s12346-025-01379-8#FPar23
[43]: /article/10.1007/s12346-025-01379-8#FPar25
[44]: /article/10.1007/s12346-025-01379-8#FPar29
[45]: /article/10.1007/s12346-025-01379-8#FPar31
[46]: /article/10.1007/s12346-025-01379-8#Fig2
[47]: /article/10.1007/s12346-025-01379-8/figures/2
[48]: /article/10.1007/s12346-025-01379-8#ref-CR3
[49]: /article/10.1007/s12346-025-01379-8#ref-CR8
[50]: /article/10.1007/s12346-025-01379-8#Equ2
[51]: /article/10.1007/s12346-025-01379-8#FPar2
[52]: /article/10.1007/s12346-025-01379-8#Equ3
[53]: /article/10.1007/s12346-025-01379-8#FPar5
[54]: /article/10.1007/s12346-025-01379-8#ref-CR16
[55]: /article/10.1007/s12346-025-01379-8#Fig3
[56]: /article/10.1007/s12346-025-01379-8#FPar3
[57]: /article/10.1007/s12346-025-01379-8/figures/3
[58]: /article/10.1007/s12346-025-01379-8#Equ4
[59]: /article/10.1007/s12346-025-01379-8#Equ7
[60]: /article/10.1007/s12346-025-01379-8#Equ8
[61]: /article/10.1007/s12346-025-01379-8#Equ6
[62]: /article/10.1007/s12346-025-01379-8#ref-CR4
[63]: /article/10.1007/s12346-025-01379-8/figures/4
[64]: /article/10.1007/s12346-025-01379-8#Fig4
[65]: /article/10.1007/s12346-025-01379-8#FPar8
[66]: /article/10.1007/s12346-025-01379-8#Fig5
[67]: /article/10.1007/s12346-025-01379-8/figures/5
[68]: /article/10.1007/s12346-025-01379-8#Equ10
[69]: /article/10.1007/s12346-025-01379-8#FPar13
[70]: /article/10.1007/s12346-025-01379-8#Equ11
[71]: /article/10.1007/s12346-025-01379-8#ref-CR9
[72]: /article/10.1007/s12346-025-01379-8#Equ12
[73]: /article/10.1007/s12346-025-01379-8#Equ13
[74]: /article/10.1007/s12346-025-01379-8#FPar11
[75]: /article/10.1007/s12346-025-01379-8#Equ14
[76]: /article/10.1007/s12346-025-01379-8#FPar16
[77]: /article/10.1007/s12346-025-01379-8#Equ15
[78]: /article/10.1007/s12346-025-01379-8#Equ16
[79]: /article/10.1007/s12346-025-01379-8#Equ17
[80]: /article/10.1007/s12346-025-01379-8#FPar19
[81]: /article/10.1007/s12346-025-01379-8#Equ18
[82]: /article/10.1007/s12346-025-01379-8#Equ19
[83]: /article/10.1007/s12346-025-01379-8/figures/6
[84]: /article/10.1007/s12346-025-01379-8#Fig6
[85]: /article/10.1007/s12346-025-01379-8#Equ9
[86]: /article/10.1007/s12346-025-01379-8#FPar17
[87]: /article/10.1007/s12346-025-01379-8#FPar21
[88]: /article/10.1007/s12346-025-01379-8#Fig7
[89]: /article/10.1007/s12346-025-01379-8/figures/7
[90]: /article/10.1007/s12346-025-01379-8#Equ20
[91]: /article/10.1007/s12346-025-01379-8#ref-CR10
[92]: /article/10.1007/s12346-025-01379-8#Equ21
[93]: /article/10.1007/s12346-025-01379-8#Fig8
[94]: /article/10.1007/s12346-025-01379-8/figures/8
[95]: /article/10.1007/s12346-025-01379-8#ref-CR7
[96]: /article/10.1007/s12346-025-01379-8/figures/9
[97]: /article/10.1007/s12346-025-01379-8#Fig9
[98]: /article/10.1007/s12346-025-01379-8#Equ5
[99]: /article/10.1007/s12346-025-01379-8#Equ22
[100]: /article/10.1007/s12346-025-01379-8#Equ23
[101]: /article/10.1007/s12346-025-01379-8#Equ24
[102]: /article/10.1007/s12346-025-01379-8/figures/10
[103]: /article/10.1007/s12346-025-01379-8#Fig10
[104]: http://scholar.google.com/scholar_lookup?amp;title=Instability%20of%20dynamical%20systems%20with%20several%20degrees%20of%20freedom&amp;journal=Soviet%20Math.%20Dokl.&amp;volume=5&amp;pages=581-585&amp;publication_year=1964&amp;author=Arnold%2CVI
[105]: http://scholar.google.com/scholar_lookup?amp;title=Qualitative%20theory%20of%20planar%20differential%20systems&amp;publication_year=2006&amp;author=Art%C3%A9s%2CJC&amp;author=Dumortier%2CF&amp;author=Llibre%2CJ
[106]: https://doi.org/10.2307%2F1969724
[107]: http://www.ams.org/mathscinet-getitem?mr=53301
[108]: http://scholar.google.com/scholar_lookup?amp;title=Limit%20cycles%20and%20rotated%20vector%20fields&amp;journal=Ann.%20of%20Math.&amp;doi=10.2307%2F1969724&amp;volume=2&amp;issue=67&amp;pages=15-31&amp;publication_year=1953&amp;author=Duff%2CGFD
[109]: https://doi.org/10.1142%2FS0219199721500644
[110]: http://www.ams.org/mathscinet-getitem?mr=4435964
[111]: http://scholar.google.com/scholar_lookup?amp;title=Perturbation%20theory%20of%20the%20quadratic%20Lotka-Volterra%20double%20center&amp;journal=Commun.%20Contemp.%20Math.&amp;doi=10.1142%2FS0219199721500644&amp;volume=24&amp;issue=5&amp;publication_year=2022&amp;author=Fran%C3%A7oise%2CJ-P&amp;author=Gavrilov%2CL
[112]: https://doi.org/10.1016%2F0022-0396%2867%2990016-2
[113]: http://www.ams.org/mathscinet-getitem?mr=221044
[114]: http://scholar.google.com/scholar_lookup?amp;title=The%20stable%2C%20center-stable%2C%20center%2C%20center-unstable%2C%20unstable%20manifolds&amp;journal=J.%20Differential%20Equations&amp;doi=10.1016%2F0022-0396%2867%2990016-2&amp;volume=3&amp;pages=546-570&amp;publication_year=1967&amp;author=Kelley%2CA
[115]: https://doi.org/10.1016%2Fj.jde.2020.11.020
[116]: http://www.ams.org/mathscinet-getitem?mr=4191338
[117]: http://scholar.google.com/scholar_lookup?amp;title=Asymptotic%20expansion%20of%20the%20dulac%20map%20and%20time%20for%20unfoldings%20of%20hyperbolic%20saddles%3A%20general%20setting&amp;journal=J.%20Differential%20Equations&amp;doi=10.1016%2Fj.jde.2020.11.020&amp;volume=275&amp;pages=684-732&amp;publication_year=2021&amp;author=Mar%C3%ADn%2CD&amp;author=Villadelprat%2CJ
[118]: https://doi.org/10.1016%2Fj.jde.2025.113281
[119]: http://www.ams.org/mathscinet-getitem?mr=4890774
[120]: http://scholar.google.com/scholar_lookup?amp;title=The%20cyclicity%20of%20hyperbolic%20hemicycles&amp;journal=J.%20Differential%20Equations&amp;doi=10.1016%2Fj.jde.2025.113281&amp;volume=433&amp;publication_year=2025&amp;author=Mar%C3%ADn%2CD&amp;author=Villadelprat%2CJ
[121]: http://www.ams.org/mathscinet-getitem?mr=156048
[122]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20stability%20of%20the%20center%20for%20time%20periodic%20perturbations&amp;journal=Trans.%20Moscow%20Math.%20Soc.&amp;volume=12&amp;pages=1-57&amp;publication_year=1963&amp;author=Melnikov%2CVK
[123]: https://doi.org/10.1090%2FS0002-9947-1994-1227092-6
[124]: http://www.ams.org/mathscinet-getitem?mr=1227092
[125]: http://scholar.google.com/scholar_lookup?amp;title=Homoclinic%20loop%20and%20multiple%20limit%20cycle%20bifurcation%20surfaces&amp;journal=Trans.%20Amer.%20Math.%20Soc.&amp;doi=10.1090%2FS0002-9947-1994-1227092-6&amp;volume=344&amp;pages=101-130&amp;publication_year=1994&amp;author=Perko%2CLM
[126]: http://scholar.google.com/scholar_lookup?amp;title=Sur%20les%20%C3%A9quations%20de%20la%20dynamique%20et%20le%20probl%C3%A8me%20des%20trois%20corps&amp;journal=Acta%20Math.&amp;volume=13&amp;pages=1-270&amp;publication_year=1890&amp;author=Poincar%C3%A9%2CH
[127]: https://link.springer.com/doi/10.1007/978-3-0348-8798-4
[128]: http://scholar.google.com/scholar_lookup?amp;title=%E2%80%9CBifurcations%20of%20planar%20vector%20fields%20and%20Hilbert%E2%80%99s%20sixteenth%20problem%E2%80%9D%20%5B2013%5D%20reprint%20of%20the&amp;doi=10.1007%2F978-3-0348-8798-4&amp;publication_year=1998&amp;author=Roussarie%2CR
[129]: https://doi.org/10.1137%2F0518083
[130]: http://www.ams.org/mathscinet-getitem?mr=892493
[131]: http://scholar.google.com/scholar_lookup?amp;title=The%20saddle-node%20separatrix-loop%20bifurcation&amp;journal=SIAM%20J.%20Math.%20Anal.&amp;doi=10.1137%2F0518083&amp;volume=18&amp;pages=1142-1156&amp;publication_year=1987&amp;author=Schecter%2CS
[132]: https://citation-needed.springer.com/v2/references/10.1007/s12346-025-01379-8?format=refman&amp;flavour=references
[133]: /search?sortBy=newestFirst&amp;contributor=D.%20Mar%C3%ADn
[134]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=D.%20Mar%C3%ADn
[135]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22D.%20Mar%C3%ADn%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[136]: /search?sortBy=newestFirst&amp;contributor=J.%20Villadelprat
[137]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=J.%20Villadelprat
[138]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22J.%20Villadelprat%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[139]: mailto:David.Marin@uab.cat
[140]: /article/10.1007/s12346-025-01379-8#Equ25
[141]: http://creativecommons.org/licenses/by/4.0/
[142]: https://s100.copyright.com/AppDispatchServlet?title=Derivatives%20of%20the%20Separation%20Function%20of%20Generalized%20Saddle%20Connections&amp;author=D.%20Mar%C3%ADn%20et%20al&amp;contentID=10.1007%2Fs12346-025-01379-8&amp;copyright=The%20Author%28s%29&amp;publication=1575-5460&amp;publicationDate=2025-10-03&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[143]: https://crossmark.crossref.org/dialog/?doi=10.1007/s12346-025-01379-8
[144]: https://citation-needed.springer.com/v2/references/10.1007/s12346-025-01379-8?format=refman&amp;flavour=citation
[145]: /search?query=Saddle%20connection&amp;facet-discipline=#34;Mathematics&#34;
[146]: /search?query=Separation%20function&amp;facet-discipline=#34;Mathematics&#34;
[147]: /search?query=Polycycle&amp;facet-discipline=#34;Mathematics&#34;
[148]: /search?query=34C37&amp;facet-discipline=#34;Mathematics&#34;
[149]: /search?query=34C07&amp;facet-discipline=#34;Mathematics&#34;
[150]: /search?query=34C23&amp;facet-discipline=#34;Mathematics&#34;
[151]: /researchers/18273437SN
[152]: /researchers/83335204SN
