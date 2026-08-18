# Frontier — what this library's own sources cite

Derived from the citations inside every document this run has downloaded, and rewritten on each download. Nothing here has been judged: a row is a lead, not a recommendation.

Ranked by how many of the library's sources cite it, then by how closely the citing sentence matches the goal. A **cited by** count above one means independent sources agree it is the reference for the subject, which is worth more than any single search ranking. A ~~struck-through~~ row is already in the library — do not download it again.

| Cited by | Source | Called | Why it was cited |
| --- | --- | --- | --- |
| 2 | https://strauss.hosted.uark.edu/papers/survey.pdf | https://strauss.hosted.uark.edu/papers/survey.pdf | in *Discrete Comput. Geom.*, 10.1007/s00454-020-00254-4, 2020. - [3]. C. Goodman-Strauss. Open Questions in Tiling. Available online at [https://strauss.hosted.uark.edu/papers/survey.pdf][17], 2000.… |
| 1 | https://doi.org/10.1016/j.crma.2015.05.002 | DOI | Heesch number for multiple prototiles is unbounded. C. R. Math. Acad. Sci. Paris. 2015;353:665–667. doi: 10.1016/j.crma.2015.05.002. [[DOI][15]] [[Google Scholar][16]] - [2]. B. Bašić and A.… |
| 1 | https://pubmed.ncbi.nlm.nih.gov/?term="Ba%C5%A1i%C4%87%20B"[Author] | Bojan Bašić | . 2021 Jan 18;43(3):50–53. doi: [10.1007/s00283-020-10034-w][4] # A Figure with Heesch Number 6: Pushing a Two-Decade-Old Boundary [Bojan Bašić][8] ### Bojan Bašić 1 Department of Mathematics and… |
| 1 | https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&amp;p=PMC3&amp;id=7812982_283_2020_10034_Fig2_HTML.jpg | — | for C 6). ### Figure 1. [image: Figure 1] [Open in a new tab][10] A figure with Heesch number 6. ### Figure 2. [image: Figure 2] [11] [Open in a new tab][12] (a) The 169 congruent figures comprising… |
| 1 | http://www.ics.uci.edu/˜eppstein/junkyard/ | — | of the sphere with isosceles triangles (to appear in Discrete Comput. Geom.). 3. D. Epstein, Heesch’s problem, The Geometry Junkyard, http://www.ics.uci.edu/˜eppstein/junkyard/ heesch/ 4. A.… |
| 1 | https://pubmed.ncbi.nlm.nih.gov/34934265/ | 34934265 | of the World Health Organization (WHO) declaration of COVID-19 as a global pandemic. [PMC Copyright notice][7] PMCID: PMC7812982 PMID: [34934265][9] --- Problems about tilings arise in recreational… |
| 1 | https://www.polyomino.org.uk/mathematics/polyform-tiling/ | — | of edge-marked polyforms. Experimental Mathematics, 25(3):281–294, 2016. [9] Joesph Myers. Polyomino, polyhex and polyiamond tiling. https://www.polyomino.org.uk/mathematics/polyform-tiling/, 2019.… |
| 1 | https://arxiv.org/pdf/2105.09438v1 | — | surrounded. The other three can be fully surrounded by copies, but in the rightmost shape the copies will necessarily enclose a hole. 1arXiv:2105.09438v1 [cs.CG] 20 May 2021 Figure 2: A 23-omino that… |
| 1 | https://doi.org/10.1007/s00283-020-10034-w | — | PMC search close ison] - [Journal List][2] - [User Guide][3] - [image: Open resources icon] - [image: View on publisher site icon] [4] - [image: Download PDF icon] [5] - [image: Collections… |
| 1 | https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&amp;p=PMC3&amp;id=7812982_283_2020_10034_Fig3_HTML.jpg | — | straightforward (though not too elegant; it reduces to considering a few cases), and we omit it here. ### Figure 3. [image: Figure 3] [13] [Open in a new tab][14] The tiles must match these… |

---

**Working with this ledger.** Sections here are bounded and rows are shortened, so what is above is not all of it. `read_ledger` returns entries in full:

```
read_ledger { ledger: "frontier" }
read_ledger { ledger: "frontier", id: "<one of the ids above>" }
read_ledger { ledger: "frontier", status: "<a status above>" }
read_ledger { ledger: "frontier", query: "<text to search for>" }
```

`list_ledgers` says what fields and statuses this one has, and what else the workspace keeps. To change it: nothing directly — it is derived from the citations in downloaded sources, so `download_document` a source and this re-derives. Editing this file changes nothing — it is re-derived on the next write and your edit goes without a warning.
