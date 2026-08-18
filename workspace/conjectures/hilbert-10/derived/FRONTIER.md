# Frontier — what this library's own sources cite

Derived from the citations inside every document this run has downloaded, and rewritten on each download. Nothing here has been judged: a row is a lead, not a recommendation.

Ranked by how many of the library's sources cite it, then by how closely the citing sentence matches the goal. A **cited by** count above one means independent sources agree it is the reference for the subject, which is worth more than any single search ranking. A ~~struck-through~~ row is already in the library — do not download it again.

| Cited by | Source | Called | Why it was cited |
| --- | --- | --- | --- |
| 2 | https://arxiv.org/pdf/1202.6371v1 | — | Math. 465 (1995), 165-182. [Pa] Jennifer Park, A universal ﬁrst order formula deﬁning the ring of in- tegers in a number ﬁeld, arXiv:1202.6371v1 [math.NT] (2012). [P1] Bjorn Poonen, Characterizing… |
| 2 | https://arxiv.org/pdf/1011.3424v1 | — | deﬁnable in various exponential ﬁelds, J. Inst. Math. Jussieu 11(04) (2012), 825-834. [Koe10] Jochen Koenigsmann, Deﬁning Z in Q, arXiv:1011.3424v1 (2010), to appear in Ann. of Math. [KR92] Ki Hang… |
| 1 | https://doi.org/10.1112/jlms.12864 | — | by Date: Friday 2nd February, 2024. This is the accepted version of the following article, which has been published in ﬁnal form at https://doi.org/10.1112/jlms.12864: Nicolas Daans. “Universally… |
| 1 | http://math.berkeley.edu/~poonen/ | — | ↑5 6 Department of Mathematics, University of California, Berkeley, CA 94720-3840, USA Email address: poonen@math.berkeley.edu URL: http://math.berkeley.edu/~poonen/ 7 |
| 1 | https://arxiv.org/pdf/2102.06941 | — | [DDF21] Nicolas Daans, Philip Dittmann, and Arno Fehm. “Existential rank and essential dimension of diophantine sets”. Available as arXiv:2102.06941. 2021. [Dit18] Philip Dittmann. “Irreducibility of… |
| 1 | https://doi.org/10.2307/2266510 | — | I am particularly indebted for his assistance in preparing Section 4. 98 use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510 Downloaded from… |
| 1 | https://arxiv.org/pdf/1011.3424v2 | — | — |
| 1 | https://arxiv.org/pdf/1309.0441v1 | — | — |
| 1 | https://arxiv.org/pdf/2301.02107v2 | — | — |

---

**Working with this ledger.** Sections here are bounded and rows are shortened, so what is above is not all of it. `read_ledger` returns entries in full:

```
read_ledger { ledger: "frontier" }
read_ledger { ledger: "frontier", id: "<one of the ids above>" }
read_ledger { ledger: "frontier", status: "<a status above>" }
read_ledger { ledger: "frontier", query: "<text to search for>" }
```

`list_ledgers` says what fields and statuses this one has, and what else the workspace keeps. To change it: nothing directly — it is derived from the citations in downloaded sources, so `download_document` a source and this re-derives. Editing this file changes nothing — it is re-derived on the next write and your edit goes without a warning.
