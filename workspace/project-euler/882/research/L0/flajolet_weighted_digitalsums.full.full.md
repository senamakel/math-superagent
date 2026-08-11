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

Hugging Face*( [What is Huggingface?][42])*

ScienceCast Toggle

ScienceCast*( [What is ScienceCast?][43])*

Demos

# Demos

Replicate Toggle

Replicate*( [What is Replicate?][44])*

Spaces Toggle

Hugging Face Spaces*( [What is Spaces?][45])*

Spaces Toggle

TXYZ.AI*( [What is TXYZ.AI?][46])*

Related Papers

# Recommenders and Search Tools

Link to Influence Flower

Influence Flower*( [What are Influence Flowers?][47])*

Core recommender toggle

CORE Recommender*( [What is CORE?][48])*

- Author
- Venue
- Institution
- Topic

About arXivLabs

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? ****[Learn more about arXivLabs][49].

[Which authors of this paper are endorsers?][50] | Disable MathJax ( [What is MathJax?][51])


## Links

[1]: https://arxiv.org/search/advanced
[2]: https://arxiv.org/search/cs?searchtype=author&amp;query=Cheung,+Y+K
[3]: https://arxiv.org/search/cs?searchtype=author&amp;query=Flajolet,+P
[4]: https://arxiv.org/search/cs?searchtype=author&amp;query=Golin,+M
[5]: https://arxiv.org/search/cs?searchtype=author&amp;query=Lee,+C+Y+J
[6]: /pdf/1003.0150
[7]: https://arxiv.org/abs/1003.0150
[8]: https://arxiv.org/abs/1003.0150v1
[9]: https://doi.org/10.48550/arXiv.1003.0150
[10]: /show-email/bdb50a11/1003.0150
[11]: /src/1003.0150
[12]: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
[13]: /prevnext?id=1003.0150&amp;function=prev&amp;context=cs.DS
[14]: /prevnext?id=1003.0150&amp;function=next&amp;context=cs.DS
[15]: /list/cs.DS/new
[16]: /list/cs.DS/recent
[17]: /list/cs.DS/2010-03
[18]: /abs/1003.0150?context=cs
[19]: /abs/1003.0150?context=math
[20]: /abs/1003.0150?context=math.CA
[21]: https://ui.adsabs.harvard.edu/abs/arXiv:1003.0150
[22]: https://scholar.google.com/scholar_lookup?arxiv_id=1003.0150
[23]: https://api.semanticscholar.org/arXiv:1003.0150
[24]: https://dblp.uni-trier.de
[25]: https://dblp.uni-trier.de/db/journals/corr/corr1003.html#abs-1003-0150
[26]: https://dblp.uni-trier.de/rec/bibtex/journals/corr/abs-1003-0150
[27]: https://dblp.uni-trier.de/search/author?author=Y.%20K.%20Cheung
[28]: https://dblp.uni-trier.de/search/author?author=Yun%20Kuen%20Cheung
[29]: https://dblp.uni-trier.de/search/author?author=Philippe%20Flajolet
[30]: https://dblp.uni-trier.de/search/author?author=Mordecai%20J.%20Golin
[31]: https://dblp.uni-trier.de/search/author?author=C.%20Y.%20James%20Lee
[32]: http://www.bibsonomy.org/BibtexHandler?requTask=upload&amp;url=https://arxiv.org/abs/1003.0150&amp;description=Multidimensional Divide-and-Conquer and Weighted Digital Sums
[33]: https://reddit.com/submit?url=https://arxiv.org/abs/1003.0150&amp;title=Multidimensional Divide-and-Conquer and Weighted Digital Sums
[34]: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[35]: https://www.connectedpapers.com/about
[36]: https://www.litmaps.co/
[37]: https://www.scite.ai/
[38]: https://alphaxiv.org/
[39]: https://www.catalyzex.com
[40]: https://dagshub.com/
[41]: http://gotit.pub/faq
[42]: https://huggingface.co/huggingface
[43]: https://sciencecast.org/welcome
[44]: https://replicate.com/docs/arxiv/about
[45]: https://huggingface.co/docs/hub/spaces
[46]: https://txyz.ai
[47]: https://influencemap.cmlab.dev/
[48]: https://core.ac.uk/services/recommender
[49]: https://info.arxiv.org/labs/index.html
[50]: /auth/show-endorsers/1003.0150
[51]: https://info.arxiv.org/help/mathjax.html
