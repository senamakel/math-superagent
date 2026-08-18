<!-- source: https://arxiv.org/pdf/2603.02621 | converted from HTML -->

[2603.02621] GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of Goldbach's Conjecture

Skip to main content

Press Enter to search &middot; [Advanced search][1]

-->

# Computer Science > Mathematical Software

**arXiv:2603.02621**(cs)

[Submitted on 2 Mar 2026]

# Title: GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of Goldbach's Conjecture

Authors: [Isaac Llorente-Saguer][2]

View a PDF of the paper titled GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of Goldbach's Conjecture, by Isaac Llorente-Saguer

[View PDF][3] [HTML (experimental)][4]

Abstract: We present GoldbachGPU, an open-source framework for large-scale computational verification of Goldbach's conjecture using commodity GPU hardware. Prior GPU-based approaches reported a hard memory ceiling near 10^11 due to monolithic prime-table allocation. We show that this limitation is architectural rather than fundamental: a dense bit-packed prime representation provides a 16x reduction in memory footprint, and a segmented double-sieve design removes the VRAM ceiling entirely. By inverting the verification loop and combining a GPU fast-path with a multi-phase primality oracle, the framework achieves exhaustive verification up to 10^12 on a single NVIDIA RTX 3070 (8 GB VRAM), with no counterexamples found. Each segment requires 14 MB of VRAM, yielding O(N) wall-clock time and O(1) memory in N. A rigorous CPU fallback guarantees mathematical completeness, though it was never invoked in practice. An arbitrary-precision checker using GMP and OpenMP extends single-number verification to 10^10000 via a synchronised batch-search strategy. The segmented architecture also exhibits clean multi-GPU scaling on data-centre hardware (tested on 8 x H100). All code is open-source, documented, and reproducible on both commodity and high-end hardware.

Comments: | 11 pages, 7 tables, 2 figures. Accompanies the v1.1.0 release of GoldbachGPU (Zenodo DOI: [this https URL][5]) |

Subjects: | Mathematical Software (cs.MS); Distributed, Parallel, and Cluster Computing (cs.DC); Performance (cs.PF); Number Theory (math.NT) |

Cite as: | [arXiv:2603.02621][6] [cs.MS] |

 | (or [arXiv:2603.02621v1][7] [cs.MS] for this version)  |

 | [https://doi.org/10.48550/arXiv.2603.02621][8]

Focus to learn more

arXiv-issued DOI via DataCite

 |

## Submission history

From: Isaac Llorente-Saguer [[view email][9]]
**[v1]**Mon, 2 Mar 2026 15:51:57 UTC (12 KB)

Full-text links:

## Access Paper:

View a PDF of the paper titled GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of Goldbach's Conjecture, by Isaac Llorente-Saguer

- [View PDF][3]
- [HTML (experimental)][4]
- [TeX Source][10]

[image: license icon] [view license][11]

### Current browse context:

cs.MS

[< prev][12] | [next >][13]

[new][14] | [recent][15] | [2026-03][16]

Change to browse by:

[cs][17]
[cs.DC][18]
[cs.PF][19]
[math][20]
[math.NT][21]

### References & Citations

- [NASA ADS][22]
- [Google Scholar][23]
- [Semantic Scholar][24]

export BibTeX citation Loading...

## BibTeX formatted citation

×

loading...

Data provided by:

### Bookmark

[image: BibSonomy] [25][image: Reddit] [26]

Bibliographic Tools

# Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer*( [What is the Explorer?][27])*

Connected Papers Toggle

Connected Papers*( [What is Connected Papers?][28])*

Litmaps Toggle

Litmaps*( [What is Litmaps?][29])*

scite.ai Toggle

scite Smart Citations*( [What are Smart Citations?][30])*

Code, Data, Media

# Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv*( [What is alphaXiv?][31])*

Links to Code Toggle

CatalyzeX Code Finder for Papers*( [What is CatalyzeX?][32])*

DagsHub Toggle

DagsHub*( [What is DagsHub?][33])*

GotitPub Toggle

Gotit.pub*( [What is GotitPub?][34])*

Huggingface Toggle

Hugging Face*( [What is Huggingface?][35])*

ScienceCast Toggle

ScienceCast*( [What is ScienceCast?][36])*

Demos

# Demos

Replicate Toggle

Replicate*( [What is Replicate?][37])*

Spaces Toggle

Hugging Face Spaces*( [What is Spaces?][38])*

Spaces Toggle

TXYZ.AI*( [What is TXYZ.AI?][39])*

Related Papers

# Recommenders and Search Tools

Link to Influence Flower

Influence Flower*( [What are Influence Flowers?][40])*

Core recommender toggle

CORE Recommender*( [What is CORE?][41])*

- Author
- Venue
- Institution
- Topic

About arXivLabs

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? ****[Learn more about arXivLabs][42].

[Which authors of this paper are endorsers?][43] | Disable MathJax ( [What is MathJax?][44])


## Links

[1]: https://arxiv.org/search/advanced
[2]: https://arxiv.org/search/cs?searchtype=author&amp;query=Llorente-Saguer,+I
[3]: /pdf/2603.02621
[4]: https://arxiv.org/html/2603.02621v1
[5]: https://zenodo.org/records/18837081
[6]: https://arxiv.org/pdf/2603.02621
[7]: https://arxiv.org/pdf/2603.02621v1
[8]: https://doi.org/10.48550/arXiv.2603.02621
[9]: /show-email/59f727e7/2603.02621
[10]: /src/2603.02621
[11]: http://creativecommons.org/licenses/by/4.0/
[12]: /prevnext?id=2603.02621&amp;function=prev&amp;context=cs.MS
[13]: /prevnext?id=2603.02621&amp;function=next&amp;context=cs.MS
[14]: /list/cs.MS/new
[15]: /list/cs.MS/recent
[16]: /list/cs.MS/2026-03
[17]: /abs/2603.02621?context=cs
[18]: /abs/2603.02621?context=cs.DC
[19]: /abs/2603.02621?context=cs.PF
[20]: /abs/2603.02621?context=math
[21]: /abs/2603.02621?context=math.NT
[22]: https://ui.adsabs.harvard.edu/abs/arXiv:2603.02621
[23]: https://scholar.google.com/scholar_lookup?arxiv_id=2603.02621
[24]: https://api.semanticscholar.org/arXiv:2603.02621
[25]: http://www.bibsonomy.org/BibtexHandler?requTask=upload&amp;url=https://arxiv.org/abs/2603.02621&amp;description=GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of Goldbach#39;s Conjecture
[26]: https://reddit.com/submit?url=https://arxiv.org/abs/2603.02621&amp;title=GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of Goldbach#39;s Conjecture
[27]: https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer
[28]: https://www.connectedpapers.com/about
[29]: https://www.litmaps.co/
[30]: https://www.scite.ai/
[31]: https://alphaxiv.org/
[32]: https://www.catalyzex.com
[33]: https://dagshub.com/
[34]: http://gotit.pub/faq
[35]: https://huggingface.co/huggingface
[36]: https://sciencecast.org/welcome
[37]: https://replicate.com/docs/arxiv/about
[38]: https://huggingface.co/docs/hub/spaces
[39]: https://txyz.ai
[40]: https://influencemap.cmlab.dev/
[41]: https://core.ac.uk/services/recommender
[42]: https://info.arxiv.org/labs/index.html
[43]: /auth/show-endorsers/2603.02621
[44]: https://info.arxiv.org/help/mathjax.html
