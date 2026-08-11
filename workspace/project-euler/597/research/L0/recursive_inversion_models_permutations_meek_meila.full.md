> **Excerpt only — read this first.** The complete text is one level down at `research/L0/recursive_inversion_models_permutations_meek_meila.full.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://papers.neurips.cc/paper_files/paper/2014/file/d157fbe354aeead90fe6287cbc4a04ca-Paper.pdf | converted from PDF -->

Recursive Inversion Models for Permutations

Christopher Meek
Microsoft Research
Redmond, Washington 98052
meek@microsoft.com
 Marina Meil˘a
University of Washington
Seattle, Washington 98195
mmp@stat.washington.edu

Abstract

We develop a new exponential family probabilistic model for permutations that
can capture hierarchical structure and that has the Mallows and generalized Mal-
lows models as subclasses. We describe how to do parameter estimation and pro-
pose an approach to structure search for this class of models. We provide experi-
mental evidence that this added ﬂexibility both improves predictive performance
and enables a deeper understanding of collections of permutations.

1 Introduction

Among the many probabilistic models over permutations, models based on penalizing inversions
with respect to a reference permutation have proved particularly elegant, intuitive, and useful. Typi-
cally these generative models “construct” a permutation in stages by inserting one item at each stage.
An example of such models are the Generalized Mallows Models (GMMs) of Fligner and Verducci
(1986). In this paper, we propose a superclass of the GMM, which we call the recursive inversion
model (RIM), which allows more ﬂexibility than the original GMM, while preserving its elegant and
useful properties of compact parametrization, tractable normalization constant, and interpretability
of parameters. Essentially, while the GMM constructs a permutation sequentially by a stochastic
insertion sort process, the RIM constructs one by a stochastic merge sort. In this sense, the RIM is a
compactly parametrized Rifﬂe Independence (RI) model (Huang & Guestrin, 2012) deﬁned in terms
of inversions rather than independence.

2 Recursive Inversion Models

We are interested in probabilistic models of permutations of a set of elements E = {e1, ..., en}. We
use π ∈ SE to denote a permutation (a total ordering) of the elements in E, and use ei <π ej to
denote that two elements are ordered. We deﬁne an n × n (lower diagonal) discrepancy matrix Dij
that captures the discrepancies between two permutations.

Dij(π, π0) = { 1 i <π j ∧ j <π0 i
0 otherwise (1)

We call the ﬁrst argument of Dij(·, ·) the test permutation (typically π) and the second argument the
reference permutation (typically π0).

Two classic models for permutations are the Mallows and the generalized Mallows models. The
Mallows model is deﬁned in terms of the inversion distance d(π, π0) = ∑

ij Dij(π, π0) which
is the total number of inversions between π and π0 (Mallows, 1957). The Mallows models is
then P (π|π0, θ) = 1
Z(θ) exp(−θd(π, π0)), θ ∈ R. Note that the normalization constant does
not depend on π0 but only on the concentration parameter θ. The Generalized Mallows model
(GMM) of Fligner and Verducci (1986) extends the Mallows model by introducing a parame-
ter for each of the elements in E and decomposes the inversion distance into a per element dis-

1

tance
1. In particular, we deﬁne vj(π, π0) to be the number of inversions for element j in π
with respect to π0 is vj(π, π0) = ∑

i>π0 j Dij(π, π0). In this case, the GMM is deﬁned as
P (π|π0, θ) = 1
Z(θ) exp(− ∑

e∈E θeve) θ ∈ Rn. The GMM can be thought of as a stagewise
model in which each of the elements in E are inserted according to the reference permutation π0
into a list where the parameter θe controls how likely the insertion of element e will yield an inver-
sion with respect to the reference permutation. For both of these models the normalization constant
can be computed in closed form

Our RIMs generalize the GMM by replacing the sequence of single element insertions with a se-
quence of recursive merges of subsequences where the relative order within the subsequences is pre-
served. For example, the sequence [a, b, c, d, e] can be obtained by merging the two subsequences

*[excerpt ends; 27519 characters not shown — see `research/L0/recursive_inversion_models_permutations_meek_meila.full.full.md`]*
