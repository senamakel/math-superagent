# Hultman, "Permutation statistics of products of random permutations"
<!-- source: https://arxiv.org/abs/1301.0430 -->

Source: https://arxiv.org/abs/1301.0430 (arXiv:1301.0430, math.CO, Jan 2013; Axel Hultman, Linköping). 9 pages.

## What the source establishes

The paper gives a character-theoretic machine for computing the EXPECTED VALUE of
a permutation statistic on a PRODUCT of t independently chosen permutations from
the uniform distribution on a union Γ of conjugacy classes of S_n.

- Key object: the *mean statistic* s̄, the class function computing the mean of
  s over conjugacy classes. To apply the method one must expand s̄ as a linear
  combination of irreducible S_n characters.
- The paper provides such expansions explicitly for common statistics:
  excedance number, inversion number, descent number, major index, and k-cycle
  number.
- From these, it derives closed-form expected values of said statistics for
  products of t random permutations from Γ.

## What it implies for this problem (Project Euler 903)

Relevance is methodological, not a direct hit — this is the same caveat recorded
in research/report_literature_ranks_powers.md.

- Q(n) = sum_pi sum_i rank(pi^i) has been reduced (news: memory.md) to closed
  forms for A_n = f_n(1) and B_n = slope of f_n(k), where
  f_n(k) = #{(pi,i): (pi^i)(m) < (pi^i)(j), m-j=k}.  Computing A_n, B_n requires
  summing two-point (inversion-type) statistics over pi in S_n and over the
  iterate exponent i, which is naturally organized by conjugacy class / cycle
  type of pi.
- Hultman's technique — write a statistic's mean as a linear combination of
  S_n irreducible characters, then average over a union of conjugacy classes —
  is exactly the tool one would use to evaluate the conjugacy-class sums that
  A_n and B_n break into.  It is the standard replacement for enumerating S_n
  when n is too large (here n = 10^6).
- LIMITATION / NOT a solution: Hultman averages over PRODUCTS of t independent
  class-distributed permutations; it does NOT handle the sum over the cyclic
  subgroup <pi> = {pi^i}, nor lexicographic rank (a non-class statistic — rank
  is a Lehmer/factoradic weight, NOT a class function).  The core unresolved
  piece — sum of factoradic ranks over the iterates pi^i of a single pi — is
  still not in the literature, exactly as recorded in
  research/report_literature_ranks_powers.md §3.

Companion full text (abstract page): research/hultman_products_random_permutations.full.md


<!-- source: https://arxiv.org/abs/1301.0430 | converted from HTML -->

[1301.0430] Permutation statistics of products of random permutations

Skip to main content

Press Enter to search &middot; [Advanced search][1]

-->

# Mathematics > Combinatorics

**arXiv:1301.0430**(math)

[Submitted on 3 Jan 2013]

# Title: Permutation statistics of products of random permutations

Authors: [Axel Hultman][2]

View a PDF of the paper titled Permutation statistics of products of random permutations, by Axel Hultman

[View PDF][3]

Abstract: Given a permutation statistic $s : S_n \to \mathbb{R}$, define the mean statistic $\bar{s}$ as the statistic which computes the mean of $s$ over conjugacy classes. We describe a way to calculate the expected value of $s$ on a product of $t$ independently chosen elements from the uniform distribution on a union of conjugacy classes $\Gamma \subseteq S_n$. In order to apply the formula, one needs to express the class function $\bar{s}$ as a linear combination of irreducible $S_n$-characters. We provide such expressions for several commonly studied permutation statistics, including the excedance number, inversion number, descent number, major index and $k$-cycle number. In particular, this leads to formulae for the expected values of said statistics.

Comments: | 9 pages |

Subjects: | Combinatorics (math.CO) |

Cite as: | [arXiv:1301.0430][4] [math.CO] |

 | (or [arXiv:1301.0430v1][5] [math.CO] for this version)  |

 | [https://doi.org/10.48550/arXiv.1301.0430][6]

Focus to learn more

arXiv-issued DOI via DataCite

 |

## Submission history

From: Axel Hultman [[view email][7]]
**[v1]**Thu, 3 Jan 2013 11:59:50 UTC (10 KB)

Full-text links:

## Access Paper:

View a PDF of the paper titled Permutation statistics of products of random permutations, by Axel Hultman

- [View PDF][3]
- [TeX Source][8]

[view license][9]

### Current browse context:

math.CO

[< prev][10] | [next >][11]

[new][12] | [recent][13] | [2013-01][14]

Change to browse by:

[math][15]

### References & Citations

- [NASA ADS][16]
- [Google Scholar][17]
- [Semantic Scholar][18]

export BibTeX citation Loading...

## BibTeX formatted citation

×

loading...

Data provided by:

### Bookmark

[image: BibSonomy] [19][image: Reddit] [20]

Bibliographic Tools

# Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer*( [What is the Explorer?][21])*

Connected Papers Toggle

Connected Papers*( [What is Connected Papers?][22])*

Litmaps Toggle

Litmaps*( [What is Litmaps?][23])*

scite.ai Toggle

scite Smart Citations*( [What are Smart Citations?][24])*

Code, Data, Media

# Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv*( [What is alphaXiv?][25])*

Links to Code Toggle

CatalyzeX Code Finder for Papers*( [What is CatalyzeX?][26])*

DagsHub Toggle

DagsHub*( [What is DagsHub?][27])*

GotitPub Toggle

Gotit.pub*( [What is GotitPub?][28])*

Huggingface Toggle

Hugging Face*( [What is Huggingface?][29])*

ScienceCast Toggle

ScienceCast*( [What is ScienceCast?][30])*

Demos

# Demos

Replicate Toggle

Replicate*( [What is Replicate?][31])*

Spaces Toggle

Hugging Face Spaces*( [What is Spaces?][32])*

Spaces Toggle

TXYZ.AI*( [What is TXYZ.AI?][33])*

Related Papers

# Recommenders and Search Tools

Link to Influence Flower

Influence Flower*( [What are Influence Flowers?][34])*

Core recommender toggle

CORE Recommender*( [What is CORE?][35])*

- Author
- Venue
- Institution
- Topic

About arXivLabs

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.


*[excerpt ends; 2015 characters not shown — see `research/hultman_products_random_permutations.full.md`]*
