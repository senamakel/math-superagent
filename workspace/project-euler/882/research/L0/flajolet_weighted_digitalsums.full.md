> **Excerpt only — read this first.** The complete text is one level down at `research/L0/flajolet_weighted_digitalsums.full.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/abs/1003.0150 | converted from HTML -->

[1003.0150] Multidimensional Divide-and-Conquer and Weighted Digital Sums

Skip to main content

Press Enter to search &middot; [Advanced search][1]

-->

# Computer Science > Data Structures and Algorithms

**arXiv:1003.0150**(cs)

[Submitted on 28 Feb 2010]

# Title: Multidimensional Divide-and-Conquer and Weighted Digital Sums

Authors: [Y. K. Cheung][2], [Philippe Flajolet][3], [Mordecai Golin][4], [C. Y. James Lee][5]

View a PDF of the paper titled Multidimensional Divide-and-Conquer and Weighted Digital Sums, by Y. K. Cheung and 3 other authors

[View PDF][6]

Abstract: This paper studies three types of functions arising separately in the analysis of algorithms that we analyze exactly using similar Mellin transform techniques. The first is the solution to a Multidimensional Divide-and-Conquer (MDC) recurrence that arises when solving problems on points in $d$-dimensional space. The second involves weighted digital sums. Write $n$ in its binary representation $n=(b_i b_{i-1}... b_1 b_0)_2$ and set $S_M(n) = \sum_{t=0}^i t^{\bar{M}} b_t 2^t$. We analyze the average $TS_M(n) = \frac{1}{n}\sum_{j<n} S_M(j)$. The third is a different variant of weighted digital sums. Write $n$ as $n=2^{i_1} + 2^{i_2} + ... + 2^{i_k}$ with $i_1 > i_2 > ... > i_k\geq 0$ and set $W_M(n) = \sum_{t=1}^k t^M 2^{i_t}$. We analyze the average $TW_M(n) = \frac{1}{n}\sum_{j<n} W_M(j)$.
We show that both the MDC functions and $TS_M(n)$ (with $d=M+1$) have solutions of the form $\lambda_d n \lg^{d-1}n + \sum_{m=0}^{d-2}(n\lg^m n)A_{d,m}(\lg n) + c_d,$ where $\lambda_d,c_d$ are constants and $A_{d,m}(u)$'s are periodic functions with period one (given by absolutely convergent Fourier series). We also show that $TW_M(n)$ has a solution of the form $n G_M(\lg n) + d_M \lg^M n + \sum_{d=0}^{M-1}(\lg^d n)G_{M,d}(\lg n),$ where $d_M$ is a constant, $G_M(u)$ and $G_{M,d}(u)$'s are again periodic functions with period one (given by absolutely convergent Fourier series).

Comments: | 44 pages, 8 figures |

Subjects: | Data Structures and Algorithms (cs.DS); Classical Analysis and ODEs (math.CA) |

Cite as: | [arXiv:1003.0150][7] [cs.DS] |

 | (or [arXiv:1003.0150v1][8] [cs.DS] for this version)  |

 | [https://doi.org/10.48550/arXiv.1003.0150][9]

Focus to learn more

arXiv-issued DOI via DataCite

 |

## Submission history

From: Yun Kuen Cheung [[view email][10]]
**[v1]**Sun, 28 Feb 2010 05:20:30 UTC (874 KB)

Full-text links:

## Access Paper:

View a PDF of the paper titled Multidimensional Divide-and-Conquer and Weighted Digital Sums, by Y. K. Cheung and 3 other authors

- [View PDF][6]
- [TeX Source][11]

[view license][12]

### Current browse context:

cs.DS

[< prev][13] | [next >][14]

[new][15] | [recent][16] | [2010-03][17]

Change to browse by:

[cs][18]
[math][19]
[math.CA][20]

### References & Citations

- [NASA ADS][21]
- [Google Scholar][22]
- [Semantic Scholar][23]

### [DBLP][24] - CS Bibliography

[listing][25] | [bibtex][26]

[Y. K. Cheung][27]
[Yun Kuen Cheung][28]
[Philippe Flajolet][29]
[Mordecai J. Golin][30]
[C. Y. James Lee][31]

export BibTeX citation Loading...

## BibTeX formatted citation

×

loading...

Data provided by:

### Bookmark

[image: BibSonomy] [32][image: Reddit] [33]

Bibliographic Tools

# Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer*( [What is the Explorer?][34])*

Connected Papers Toggle

Connected Papers*( [What is Connected Papers?][35])*

Litmaps Toggle

Litmaps*( [What is Litmaps?][36])*

scite.ai Toggle

scite Smart Citations*( [What are Smart Citations?][37])*

Code, Data, Media

# Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv*( [What is alphaXiv?][38])*

Links to Code Toggle

CatalyzeX Code Finder for Papers*( [What is CatalyzeX?][39])*

DagsHub Toggle

DagsHub*( [What is DagsHub?][40])*

GotitPub Toggle

Gotit.pub*( [What is GotitPub?][41])*

Huggingface Toggle


*[excerpt ends; 3821 characters not shown — see `research/L0/flajolet_weighted_digitalsums.full.full.md`]*
