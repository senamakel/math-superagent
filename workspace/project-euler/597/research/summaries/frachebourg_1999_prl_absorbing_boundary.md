> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/frachebourg_1999_prl_absorbing_boundary.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/cond-mat/9808077 | converted from PDF -->

arXiv:cond-mat/9808077v1  7 Aug 1998
Exact solution of the one-dimensional ballistic aggregation

L. Frachebourg

Institut de Physique Th´eorique

Ecole Polytechnique F´ed´erale de Lausanne

CH-1015 Lausanne, Switzerland

Abstract

An exact expression for the mass distribution ρ(M, t) of the ballistic ag-

gregation model in one dimension is derived in the long time regime. It is

shown that it obeys scaling ρ(M, t) = t−4/3F (M/t2/3) with a scaling function

F (z) ∼ z−1/2 for z ≪ 1 and F (z) ∼ exp(−z3/12) for z ≫ 1. Relevance of

these results to Burgers turbulence is discussed.

Ballistic aggregation provides a simple model of nonequilibrium statistical physics which

is a natural version of a dissipative gas of hard spheres where particles follow the basic laws

of mechanics. It consists in a one-dimensional gas of point-like massive particles which move

freely until they collide. The perfectly inelastic collision of two masses conserves the total

mass and momentum, while dissipation occurs as kinetic energy is loss in each collision. One

can anticipate the formation of more and more massive while slower and slower aggregates.

This model was introduced by Carnevale, Pomeau and Young [1] where they conjectured,

based on scaling arguments and numerical simulations, an asymptotic scaling regime for

the mass distribution ρ(M, t) = F (M/⟨M⟩t)/⟨M⟩2
t . The average mass per aggregate was

supposed to grow algebraically with time as ⟨M⟩t ∼ t
2/3 and the scaling function had a simple

universal exponential form F (z) = exp(−z) independent of the initial conditions. Later,

this conjecture was reinforced by Piasecki [2] where he solved the hierarchy of dynamical

1

equations governing the system inside a mean-ﬁeld approximation scheme.

This system, in its continuous limit, was also studied as a simpliﬁed astronomical model

for the agglomeration of cosmic dust into macroscopic objects [3]. In the ballistic aggregation

model, the aggregates interact only through their collisions. An aggregation model where

gravitational interactions are present has been studied in [4].

It is important to mention the connection between this model and some solutions of the

Burgers equation. At very high Reynolds number, the asymptotic solution of the Burgers

equation consists of a train of shock waves. The laws of motion which govern the dynamics

of these shock waves are found to be equivalent to a ballistic aggregation system (see [5]).

In this letter, I verify the scaling hypothesis for the mass distribution and ﬁnd in an

exact calculation an explicit form for the scaling function. It happens to be diﬀerent from

the conjectured simple exponential.

Rather than solving the set of partial diﬀerential equations governing the evolution of

the system, I exploit the fact that, once the initial state of the system is given, the dynamics

is completely deterministic. Our approach will thus be based on a statistical study of the

initial conditions and is largely inspired by the work of Martin and Piasecki [6].

Initially, particles having all the same mass m are regularly placed on a line with the same

inter-particle distance a. Initial mass density is thus ρ0 = m/a. The initial momentum of the

thermalized particles are not correlated and are distributed according to the same Gaussian

distribution φ(p) = √
β/(2πm) exp(−βp2/(2m)) where I now choose β = 1/2 without loss

of generality.

I compute now the density distribution ρm(X, M, P, t) where ρm(X, M, P, t)dM dP dX

is the number of aggregates located in (X, X + dX) with momentum in (P, P + dP ) and

mass in (M, M + dM) at time t.

When the coordinates (X, M, P, t) of an aggregate are given, they uniquely deﬁne the

number n = M/m as well as the initial positions X − P t/M − M/(2ρ0) ≤ xi ≤ X − P t/M +

M/(2ρ0) (i = 1, . . . , n) of its constituents. A crucial point is that an aggregate, once formed,


*[excerpt ends; 11700 characters not shown — see `research/sources/frachebourg_1999_prl_absorbing_boundary.full.md`]*
