# Fishkin 2010 — Math-Net.Ru and Semantic Scholar records (no mathematics)

## Math-Net.Ru attempts (this cycle)

Three Math-Net.Ru fetches returned journal navigation pages, not the Fishkin
paper:

1. `research/sources/fishkin-perturbed-center-mathnet.full.md` — paper id 580
   of Trudy Moskovskogo Matematicheskogo Obshchestva is actually Lerman &
   Markova, "On symplectic dynamics near a homoclinic orbit to 1-elliptic
   fixed point" (2015) — a different paper. No Fishkin abstract here.
2. `research/sources/fishkin-mathnet-search.full.md` — a Math-Net journal
   search for "Fishkin" in mmo returned only the journal general-information
   page, no paper hits.
3. `research/sources/fishkin-mathnet-vol71.full.md` — the Math-Net archive
   listing skips volume 71 in its English view (jumps 2011/vol 72 →
   1995/vol 56), so the 2010 volume is not reachable through that route.

None of these establish mathematics. They are recorded so nobody re-fetches
them.

## Semantic Scholar record

`research/sources/fishkin-semanticscholar.full.md` — the S2 API record for
DOI 10.1090/s0077-1554-2010-00181-1 has `"abstract": null` and
`"openAccessPdf": {status: BRONZE}` pointing back to the AMS DOI. Confirms
only that no abstract is available there either.

## Bearing on the run

The only obtainable abstract for Fishkin 2010 is the OpenAlex inverted index
(`research/sources/fishkin-openalex.full.md`, reconstructed in
`research/findings/fishkin-abstract-reconstruction-2026-08-18.md`). The
specific exponents quoted in earlier run reports (10⁷²/10⁷⁷/δ^{−33}) are in
no held source and remain UNVERIFIED. The upgrade path is the AMS free-archive
PDF (vol 71, >5 years old), which returned 429 rate-limit this cycle.
