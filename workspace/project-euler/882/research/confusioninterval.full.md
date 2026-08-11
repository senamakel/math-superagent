> **Excerpt only — read this first.** The complete text is beside it at `research/confusioninterval.full.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://doi.org/10.48550/arxiv.1911.04268 | converted from HTML -->

[1911.04268] Universal almost optimal compression and Slepian-Wolf coding in probabilistic polynomial time

Skip to main content

arXiv is now an independent nonprofit! [Learn more][1] ×

Press Enter to search &middot; [Advanced search][2]

-->

# Computer Science > Information Theory

**arXiv:1911.04268**(cs)

[Submitted on 11 Nov 2019]

# Title: Universal almost optimal compression and Slepian-Wolf coding in probabilistic polynomial time

Authors: [Bruno Bauwens][3], [Marius Zimand][4]

View a PDF of the paper titled Universal almost optimal compression and Slepian-Wolf coding in probabilistic polynomial time, by Bruno Bauwens and 1 other authors

[View PDF][5]

Abstract: In a lossless compression system with target lengths, a compressor ${\cal C}$ maps an integer $m$ and a binary string $x$ to an $m$-bit code $p$, and if $m$ is sufficiently large, a decompressor ${\cal D}$ reconstructs $x$ from $p$. We call a pair $(m,x)$ $\textit{achievable}$ for $({\cal C},{\cal D})$ if this reconstruction is successful. We introduce the notion of an optimal compressor ${\cal C}_\text{opt}$, by the following universality property: For any compressor-decompressor pair $({\cal C}, {\cal D})$, there exists a decompressor ${\cal D}'$ such that if $(m,x)$ is achievable for $({\cal C},{\cal D})$, then $(m+\Delta, x)$ is achievable for $({\cal C}_\text{opt}, {\cal D}')$, where $\Delta$ is some small value called the overhead. We show that there exists an optimal compressor that has only polylogarithmic overhead and works in probabilistic polynomial time. Differently said, for any pair $({\cal C}, {\cal D})$, no matter how slow ${\cal C}$ is, or even if ${\cal C}$ is non-computable, ${\cal C}_{\text{opt}}$ is a fixed compressor that in polynomial time produces codes almost as short as those of ${\cal C}$. The cost is that the corresponding decompressor is slower.
We also show that each such optimal compressor can be used for distributed compression, in which case it can achieve optimal compression rates, as given in the Slepian-Wolf theorem, and even for the Kolmogorov complexity variant of this theorem. Moreover, the overhead is logarithmic in the number of sources, and unlike previous implementations of Slepian-Wolf coding, meaningful compression can still be achieved if the number of sources is much larger than the length of the compressed strings.

Comments: | 26 pages |

Subjects: | Information Theory (cs.IT) |

MSC classes: | 68Q30, 94A24, 94A15 |

ACM classes: | F.2.3 |

Cite as: | [arXiv:1911.04268][6] [cs.IT] |

 | (or [arXiv:1911.04268v1][7] [cs.IT] for this version)  |

 | [https://doi.org/10.48550/arXiv.1911.04268][8]

Focus to learn more

arXiv-issued DOI via DataCite

 |

## Submission history

From: Bruno Bauwens [[view email][9]]
**[v1]**Mon, 11 Nov 2019 13:50:25 UTC (47 KB)

Full-text links:

## Access Paper:

View a PDF of the paper titled Universal almost optimal compression and Slepian-Wolf coding in probabilistic polynomial time, by Bruno Bauwens and 1 other authors

- [View PDF][5]
- [TeX Source][10]

[view license][11]

### Current browse context:

cs.IT

[< prev][12] | [next >][13]

[new][14] | [recent][15] | [2019-11][16]

Change to browse by:

[cs][17]
[math][18]
[math.IT][19]

### References & Citations

- [NASA ADS][20]
- [Google Scholar][21]
- [Semantic Scholar][22]

### [DBLP][23] - CS Bibliography

[listing][24] | [bibtex][25]

[Bruno Bauwens][26]
[Marius Zimand][27]

export BibTeX citation Loading...

## BibTeX formatted citation

×

loading...

Data provided by:

### Bookmark

[image: BibSonomy] [28][image: Reddit] [29]

Bibliographic Tools

# Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer*( [What is the Explorer?][30])*

Connected Papers Toggle

Connected Papers*( [What is Connected Papers?][31])*

Litmaps Toggle

Litmaps*( [What is Litmaps?][32])*

scite.ai Toggle


*[excerpt ends; 3963 characters not shown — see `research/confusioninterval.full.full.md`]*
