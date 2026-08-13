# Arias de Reyna — Gilbreath's conjecture (blog, July 2020)

**Full text:** `research/sources/arias-de-reyna-gilbreath-blog.full.md` [[arias-de-reyna-gilbreath-blog.full]]
**Source:** https://institucional.us.es/blogimus/en/2020/07/gilbreaths-conjecture/ (J. Arias de Reyna, IMUS blog).

## What it establishes

A survey of GC with two valuable independent observations:

1. **The Proth "failed proof" is a myth (detailed).** Proth published only in Nouv. Corresp. Math. 4 (1878) 236–240; he states the property as a "theorem" with **no proof**, drawing consequences instead; Catalan's editor note: "is it not true that the theorems of Mr. Proth which we have just read are, rather, postulates?". The frequently-cited C.R. 85 (1877) 329–331 is actually **Pepin's** paper; C.R. 87 (1877) 926 is a different primality-criteria note. Nobody has ever seen a wrong proof. Independent confirmation of `proth-myth-retracted`/`proth-citation-correction`.
2. **Kilgrove–Ralston block observation restated:** "if in a row all numbers up to the n-th, except the first which is 1, are 0 or 2 then the next n−1 rows start with a 1" — the block lemma, confirmed again. G(n) definition and Odlyzko's G(π(10^13))=635.
3. **Croft's claim blamed/refuted + Odlyzko's cautious version:** Croft's stronger claim is false; Odlyzko only says a sequence starting 2 + increasing odds with *small random increments* is eventually Gilbreath (matches Chase and the run's framing).
4. **Numerical model experiment:** pseudo-primes a_1=2,a_2=3,a_{n}=a_{n−1}+2u_n, u_n uniform on {1..⌊log n⌋}: out of 10,000 tests, prob of full GC ≈ 0.499, prob that b_n=1 for n>10 ≈ 0.9916, none failed for n>40. (Heuristic — supports "eventually 1" more strongly than "always 1".)
5. **Chase's Theorem 1** (f(n)≤(1/100)logloglog), the {0,1}-halved reduction, and the key lemma P(ultimate iterate is 0) ≥ 1/(200C²) for n≥(200C²)^{2C} (uniform on {0..C−1}) — a digest of Chase 2024.
6. **Erdős's "200 years" quote** also appears here (cf. Houston). Proth context: the journal Nouvelle Correspondance Mathématique, Catalan/Mansion, Proth's primality criteria.

## Hypotheses / bearing

Survey-level, no new theorem. Its value to this run: a clean independent secondary account of the Proth citation tangle and the K–R block lemma, plus an empirical data point for "eventually-GC holds more strongly than always-GC". It does not add statements beyond what Chase 2024 / Killgrove–Ralston / Odlyzko already establish; those primaries are now in the library.

## Claims

```claim
id: arias-block-and-evolution
statement: (survey) if a row has leading 1 and n subsequent entries in {0,2}, the next n−1 rows start with 1; G(π(10^13))=635; a random pseudo-prime model attained GC in ~49.9% of runs but eventual-1 (n>10) in 99.16% with no failures past n=40; Proth's original has no proof and Catalan calls the assertions postulates.
hypotheses: none new; restates K–R/Odlyzko/Chase.
holds-here: yes — agrees with the sourced primaries.
status: asserted (secondary survey; the Proth reading is primary-documented)
bearing: corroborates block lemma, Odlyzko bound, and the Proth-myth retraction with an independent source.
anchor: research/sources/arias-de-reyna-gilbreath-blog.full.md
```
