# Proth 1878 — Sur la série des nombres premiers

**Full text obtained?** No — the scan is image-based and bot-protected; see "Obtainability" below. What we hold is a **record** (metadata + two independent scholarly reader accounts).
**Source record URL:** https://www.deutsche-digitale-bibliothek.de/item/4DYEX3OYX5FMYSCZDNW777LNIZMENRFT (GDZ digitization, Public Domain Mark 1.0; Göttingen SUB, shelfmark 8 MATH I, 1180:4)
**Bibliographic data:** F. Proth, *Sur la série des nombres premiers*, Nouvelle Correspondance Mathématique 4 (1878), 236–240. (Journal: Brussels, F. Hayez, edited by E. Catalan and P. Mansion.)
**Library files:**
- `research/sources/proth-1878-ncm-vol4.md` — GDZ HTML stub (empty; the volume is image-only, JS-rendered)
- `research/sources/proth-1878-ncm-vol4-googlebooks.md` — Google Books vol. 4 page (OCR keyword cloud + ToC only; the article **is** in this volume per the ToC)
- `research/sources/arias-de-reyna-gilbreath-blog.full.md` — Juan Arias de Reyna (Univ. of Sevilla), July 2020, who read the article: quotes its content and the editor's note
- `research/sources/chase-2024-random-analogue-gilbreath.full.md` — Zachary Chase, *Math. Ann.* 388 (2024) 2611–2625, §7 "A historical remark", with the retraction

## What the article actually is (per two independent readers)

- **Proth states the property as a "theorem"** — that repeatedly taking absolute differences of the primes leaves a leading 1 — **and gives no proof**. He draws consequences from it instead.
- **The editor reacts.** At the end of the article a note signed "E. C." (Eugène Catalan) asks "is it not true that the theorems of Mr. Proth which we have just read are, rather, postulates?" (quote via Arias de Reyna 2020).
- **The "faulty proof" claim is a retracted myth.** H. C. Williams, the origin of the widely repeated statement (in *Édouard Lucas and Primality Testing*, Wiley 1998, p. 123: "Proth claimed to prove... his proof was faulty"), said in email 2020 (quoted in Chase 2024 §7): "On rereading his actual paper... I can find no support for my assertion... My apologies for seeming to have started a myth."
- **Citation history is messy.** Many sources citing Proth's "discussion of Gilbreath's conjecture" give *Théorèmes sur les nombres premiers*, C. R. Acad. Sci. Paris **85** (1877) 329–331 — which is actually Pépin's paper (C.R. 85, 329–331, "Sur la formule 2^(2^n)+1"), unrelated; or C.R. **87** (1877) 329–331 which doesn't discuss the conjecture at all. The only location where Proth discusses it is Nouv. Corresp. Math. 4 (1878) 236–240 (Chase 2024 §7; Arias de Reyna 2020).

## Claims

```claim
id: proth-1878-no-proof
statement: Proth's "Sur la série des nombres premiers" (Nouv. Corresp. Math. 4 (1878) 236–240) states the Gilbreath property as a theorem but contains no proof; editor E. Catalan appended a note suggesting the assertions are "rather postulates". The claim that Proth gave a faulty proof is unsupported and was retracted by its originator H. C. Williams (email 2020).
hypotheses: two independent accounts (Arias de Reyna 2020, who read the paper; Chase 2024 §7, who cites Williams' retraction).
holds-here: yes — GOAL.md's "located error in Proth's 1878 claimed proof" is based on the myth; the corrected finding is the retraction itself. There is no flawed proof step to locate because there is no proof.
status: sourced (secondary-but-direct: two scholars who read the original; primary scan unobtainable as text — see below)
bearing: the deliverable "a located error in Proth's claimed proof" must be reframed: the library now establishes that no such proof exists, and that the standard citation is a myth started by Williams (1998) and retracted by him (2020).
anchor: research/sources/chase-2024-random-analogue-gilbreath.full.md (Sect. 7); research/sources/arias-de-reyna-gilbreath-blog.full.md
```

```claim
id: proth-citation-correction
statement: The citation "Théorèmes sur les nombres premiers, C. R. Acad. Sci. Paris 85 (1877) 329–331" attached to Proth's Gilbreath claim is wrong on two counts: those pages are Pépin's paper, and C.R. 87 (1877) does not discuss the conjecture; Proth's only discussion is Nouv. Corresp. Math. 4 (1878) 236–240.
hypotheses: — (a bibliographic correction, verified against both independent accounts).
holds-here: yes — prevents the run from citing the wrong Proth paper.
status: sourced (Chase 2024 §7; Arias de Reyna 2020)
bearing: bibliography hygiene; the run must cite Proth as Nouv. Corresp. Math. 4 (1878) 236–240.
anchor: research/sources/chase-2024-random-analogue-gilbreath.full.md
```

## Obtainability (so nobody retries)

- **GDZ** (gdz.sub.uni-goettingen.de, PPN598948236_0004): page images are JS-rendered; the downloader captured only navigation stubs. The per-page PDF endpoint returned 500.
- **Deutsche Digitale Bibliothek** (item 4DYEX3OYX5FMYSCZDNW777LNIZMENRFT): Anubis proof-of-work bot-block.
- **Gallica**: search endpoint bot-check ("Vérification de sécurité"). No ark/bpt6 identifier for this journal surfaced in any search.
- **archive.org**: advancedsearch returns 0 results for the journal title; only vols 1 & 5 (as `nouvellecorresp01*`, `nouvellecorresp00*`) exist there — vol 4 does not.
- **HathiTrust**: catalog search 403 Forbidden.
- **Google Books** (id=10A0AQAAMAAJ): vol. 4 viewable; the converter fetched only the ToC + OCR keyword cloud (the article pages are in the volume but the page-image content did not convert to text).

The content gap is **covered** by the two reader accounts above; a fresh transcription of Proth's 5 pages would add primary granularity (exactly which consequences he drew, the Catalan note's wording) but is not needed to settle the myth/retraction question. If a future tool can render GDZ's JS viewer, the direct scan is `https://gdz.sub.uni-goettingen.de/id/PPN598948236_0004`.