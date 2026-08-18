# Frontier — what this library's own sources cite

Derived from the citations inside every document this run has downloaded, and rewritten on each download. Nothing here has been judged: a row is a lead, not a recommendation.

Ranked by how many of the library's sources cite it, then by how closely the citing sentence matches the goal. A **cited by** count above one means independent sources agree it is the reference for the subject, which is worth more than any single search ranking. A ~~struck-through~~ row is already in the library — do not download it again.

| Cited by | Source | Called | Why it was cited |
| --- | --- | --- | --- |
| 2 | https://www.ams.org/journals/jourhtml/citing.html | Citing articles before they appear in a journal issue (opens in a new tab) | individually soon after proof is returned from authors and before appearing in an issue (most recently published article listed first). [Citing articles before they appear in a journal issue (opens… |
| 2 | https://www.ams.org/arc/ | AMS Author Resource Center | paper should be the [2020 Mathematics Subject Classification][15] representing the primary and secondary subjects of the article. The [AMS Author Resource Center][16] provides TeX Resources, the AMS… |
| 2 | https://ebus.ams.org/ebus/ShoppingCart.aspx | Go to Checkout | Successfully Added to Cart An error was encountered while trying to add the item to the cart. Please try again. Continue Shopping [Go to Checkout][1] OK Please make all selections above before adding… |
| 2 | http://projecteuclid.org | Project Euclid | and Betty Moore Foundation through a grant to the Mathematical Sciences Research Institute. The 1891-1991 archive is also online at [Project Euclid][5]. The digitization of the back issues from 1992… |
| 2 | https://www.ams.org/AMSMathViewer | — | Copy To Clipboard Successfully Copied! --> **Toggle favorite** --> Contents of Issue 63 HTML articles powered by AMS MathViewer **[2] Articles in press Papers are displayed alphabetically by first… |
| 2 | https://www.ams.org/jourhtml/changes.html | AMS policy on making changes to articles after publication (opens in a new tab) | listed Early View PDF articles are an AMS member benefit Recently published articles HTML articles powered by AMS MathViewer **[2] [AMS policy on making changes to articles after publication (opens… |
| 2 | http://www.charlesworthauthorservices.com/~AMathSoc | Language editing services available from Charlesworth Author Services | License will be selected. Authors are encouraged to use **[AMS-prepared style files][20]**in preparing their papers. ## Useful Tools - [Language editing services available from Charlesworth Author… |
| 2 | https://epubs.siam.org/pb-assets/author_guidelines_accessible_mathematics.pdf?__cf_chl_tk=rsjW90GxG8phfd3776do9XToXeOCq.TMNvb8wFWjgZA-1769442789-1.0.1.1-oXbWN.bq0CotosbsSuPPP.avVv48o6Pp4p5BTJaictw | Joint Author Guidelines for Preparing Accessible Mathematics Content | Charlesworth Author Services][21] - [AMS journal article templates from Overleaf][22] - [Permissions][23] - [Preparing graphics][24] - [Joint Author Guidelines for Preparing Accessible Mathematics… |
| 2 | https://www.overleaf.com/org/ams/ | AMS journal article templates from Overleaf | files][20]**in preparing their papers. ## Useful Tools - [Language editing services available from Charlesworth Author Services][21] - [AMS journal article templates from Overleaf][22] -… |
| 2 | https://ams.msp.org/submit_new.php?j=bull | Initial Manuscript Submission form | Manuscript Processing for initial submissions to AMS journals. The preferred method of submission is to upload a PDF file using the [Initial Manuscript Submission form][13]. An alternate method is to… |
| 2 | https://www.ams.org/publications/journals/journalsframework/bull/editorial_history_bull | Past Editorial Board Members | the Electronic PrePress Department, American Mathematical Society, 201 Charles Street, Providence, RI 02904-2213 USA. ## Editorial Board [Past Editorial Board Members][12] - Alejandro Adem Chief… |
| 2 | https://www.ams.org/publications/journals/journalsframework/bulledit | Editor | of the corresponding author - Contact information including email address and mailing address - The author should suggest an appropriate [Editor][14] to review the paper No paper that has been… |
| 2 | https://www.ams.org/publications/pubpermissions | requesting permissions for AMS journal and book content. | reuse portions of AMS publication content are handled by the Copyright Clearance Center. For more information, please visit our page on [requesting permissions for AMS journal and book content.][8]… |
| 2 | https://www.mathjax.org | — | Share this page via the icons above, or by copying the link below: Copy To Clipboard Successfully Copied! [image: Powered by MathJax] [27] Please select which format for which you are requesting… |
| 1 | https://arxiv.org/pdf/math.LA/0103101 | — | (1995). [C-B] W. Crawley-Boevey, On matrices in prescribed conjugacy classes with no common invariant subspace and sum zero, preprint arXiv:math.LA/0103101, 15 March 2001, to appear in Duke Math. J.… |
| 1 | https://arxiv.org/pdf/1312.2518v1 | — | — |
| 1 | https://arxiv.org/pdf/math/0310441v1 | — | — |
| 1 | https://arxiv.org/pdf/math/9804035v1 | — | — |

---

**Working with this ledger.** Sections here are bounded and rows are shortened, so what is above is not all of it. `read_ledger` returns entries in full:

```
read_ledger { ledger: "frontier" }
read_ledger { ledger: "frontier", id: "<one of the ids above>" }
read_ledger { ledger: "frontier", status: "<a status above>" }
read_ledger { ledger: "frontier", query: "<text to search for>" }
```

`list_ledgers` says what fields and statuses this one has, and what else the workspace keeps. To change it: nothing directly — it is derived from the citations in downloaded sources, so `download_document` a source and this re-derives. Editing this file changes nothing — it is re-derived on the next write and your edit goes without a warning.
