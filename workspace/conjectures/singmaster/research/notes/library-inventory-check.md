# Library inventory check — Singmaster's conjecture

Status: **complete and verified**. ROOT.md passes the phase-1 exit test. Run by
librarian to (a) verify nothing load-bearing is missing and (b) close any open
request row. Conclusion: no fetchable gap remains; all request rows are
blocked-with-reason or compute tasks.

## Primaries held (verified present, not tombstones)

- MRSTT 2021, arXiv:2106.03335 — `research/sources/mrstt-fulltext.full.md`.
  Thm 1.3: at most two interior solutions; effective per Remark 1.7 (verbatim,
  grep-confirmed).
- Yamada 2020, arXiv:2002.07043 — `binomial-collisions-necessary-conditions-2020.full.md`.
  Thm 1.1 boundary necessary condition — the one quantitative hold on the
  MRSTT-open edge.
- Kiss 1988, FQ 26(2) — `kiss-1988-cx2-cyp.full.md`. C(x,2)=C(y,p) effective
  finiteness; the same paper the frontier flags (DOI 10.1080/00150517.1988.12429639).
- Goetgheluck 1998, Math. Comp. 67 — `goetgheluck-ratio2-1998.full.md`.
  Ratio-2 families (the one request row marked "not sought" — already held).
- Jenkins 2014, Beukers-Shorey-Tijdeman 1999, Matveev 2000, BST 1999,
  Lane Clark 2010, Abbott-Erdos-Hanson 1974, Kane 2004/2007, de Weger
  1995/1997, BMSST 2008, Stroeker-de Weger 1999, GRKTU 2020
  (arXiv:1904.11369), Bazso-Mezzo-Pinter-Tengely 2023 (Stirling analogue).

## Blocked (verified; do NOT re-fetch)

- **Singmaster 1971 AMM** — paywalled (JSTOR/DOI 10.2307/2316907); attested by
  the held 1975 FQ primary. The existing `singmaster-1971.full.md` is a
  tombstone (Fermat's Library comments) — do not quote a constant from it.
- **Avanesov 1966/67** — IMPAN scan is PDF with no text layer; list attested
  through Kiss 1988 + GRKTU 2020.
- **Tian 2025 MDPI** — 403-blocked.
- **Shirshov, Kvant Selecta I** — AMS paywalled.

## Verification points reported by ROOT.md

- N(3003)=8 (both-mirrors + trivial convention), `code/out/witnesses.json`.
- No a <= 2^48 with N(a) >= 8 except 3003; Blokhuis-Brouwer-de Weger 2017:
  no unknown collisions for n <= 10^6 or value <= 10^60.
- Genus closed form g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2 PROVED via
  Riemann-Hurwitz; verified 171 pairs. Any bound B < 8 is refuted.
- Counting convention fixed throughout: N(a) counts BOTH mirrors AND the
  trivial pair.

## Note on Cognee

The memory server (remember_memory) was unresponsive during this check (health
report timed out; not a problem-specific failure). The durable catalogue is
`research/ROOT.md` + the ledgers, which hold the above; Cognee recall is a
secondary layer. Record the verified inventory there again if memory recovers.
