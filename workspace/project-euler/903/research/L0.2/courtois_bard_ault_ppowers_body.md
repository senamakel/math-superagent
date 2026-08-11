> **Excerpt only — read this first.** The complete text is one level down at `research/L0.3/courtois_bard_ault_ppowers_body.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://ar5iv.labs.arxiv.org/html/0905.3682 | converted from HTML -->

[0905.3682] Statistics of Random Permutations and the Cryptanalysis Of Periodic Block Ciphers

# Statistics of Random Permutations and the Cryptanalysis Of Periodic Block Ciphers DOI: [xxx][1]

xxx; Received xxx; Revised xxx

###### Abstract

A block cipher is intended to be computationally indistinguishable from a random permutation of appropriate domain and range. But what are the properties of a random permutation? By the aid of exponential and ordinary generating functions, we derive a series of collolaries of interest to the cryptographic community. These follow from the Strong Cycle Structure Theorem of permutations, and are useful in rendering rigorous two attacks on Keeloq, a block cipher in wide-spread use. These attacks formerly had heuristic approximations of their probability of success.

Moreover, we delineate an attack against the (roughly) millionth-fold iteration of a random permutation. In particular, we create a distinguishing attack, whereby the iteration of a cipher a number of times equal to a particularly chosen highly-composite number is breakable, but merely one fewer round is considerably *more*secure. We then extend this to a key-recovery attack in a “Triple-DES” style construction, but using AES-256 and iterating the middle cipher (roughly) a million-fold.

It is hoped that these results will showcase the utility of exponential and ordinary generating functions and will encourage their use in cryptanalytic research.

###### keywords

Generating Functions, EGF, OGF, Random Permutations, Cycle Structure, Cryptanalysis, Iterations of Permutations, Analytic Combinatorics, Keeloq

###### Classification:

05A15, 94A60, 20B35, 11T71

† † firstpage: 1

\headlinetitle

Statistics of Random Permutations and Block Ciphers \authorone Nicolas T. Courtois \addressone University College of London, Gower Street, London, WC1E6BT \countryone UK \emailone n.courtois@ucl.ac.uk \authortwo Gregory V. Bard \addresstwo Fordham University, Department of Mathematics, The Bronx, NY, 10458 \countrytwo USA \emailtwo bard@fordham.edu \authorthree Shaun V. Ault \addressthree Fordham University, Department of Mathematics, The Bronx, NY, 10458 \countrythree USA \emailthree ault@fordham.edu

###### Acknowledgements.

We thank Sebastiaan Indesteege, a graduate student from Katho-lieke Universiteit Leuven in Belgium, for helpful comments; Sean O’Neil, an independent scientist from Ireland, also for helpful comments; Dr. Kenneth Patterson of the Royal Holloway University of London for questions at the 2008 Workshop on Mathematical Cryptography in Santander, Spain, that encouraged us to rigorously describe the attack in Section 5; and Prof. Philippe Flajolet and Prof. Robert Sedgewick, for their excellent text on analytic combinatorics [12].

## 1 Introduction

The technique of using a function of a variable to count objects of various sizes, using the properties of multiplication and addition of series as an aid, is accredited to Pierre-Simon Laplace [12]. Here, we will use this family of techniques, now called “analytic combinatorics” to count permutations of particular types. An ordinary generating series associated with a set of objects assigns as the coefficient of the z i z^{i} th term, the number of objects of size i i. An exponential generating series is merely this, with each term divided by i! i!. In particular, this can be used to describe permutations drawn at random from S n S_{n}, which is the topic of this paper.


*[excerpt ends; 61612 characters not shown — see `research/L0.3/courtois_bard_ault_ppowers_body.full.md`]*
