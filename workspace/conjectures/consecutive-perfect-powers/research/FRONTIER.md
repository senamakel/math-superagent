# Frontier — who the library's sources cite, and what is screened

Read this before searching. A source several of our documents cite is the standard
reference for the subject. A ~~struck-through~~ row is already held — read the
file it names.

## Held in the library (research/sources/)

| Source | File | What it supplies |
| --- | --- | --- |
| Shokrollahi, "Relative class number of imaginary Abelian fields of prime conductor below 10000", Math. Comp. 68 (1999), doi:10.1090/s0025-5718-99-01139-4 | relative-class-number-analytic.md | Analytic class number formula `h^- = 2p prod (-1/2 B_{1,chi})`; h^- computation to p<10000 |
| Schoof, "Class numbers of real cyclotomic fields of prime conductor", Math. Comp. 72 (2003), doi:10.1090/S0025-5718-02-01432-1 (read server-side from mat.uniroma2.it/~schoof/realcyc.pdf) | relative-class-number-analytic.md | h^+ not known for any p>=71; minus/plus split |
| Ichimura, "A class number formula for the p-cyclotomic field", Arch. Math. 87 (2006), doi:10.1007/s00013-006-1867-7 | relative-class-number-analytic.md, stickelberger-cyclotomic-units.md | Iwasawa index [Z[G]^-:s^-] = h^-; index-2 refinement |
| Hida, UCLA course notes "Elementary Iwasawa theory for cyclotomic fields", math.ucla.edu/~hida/207a.1.18w/Lec1.pdf | stickelberger-cyclotomic-units.md | Stickelberger's theorem (Thm 5.2); Stickelberger element/ideal |
| Sinnott, "On the Stickelberger ideal and the circular units of a cyclotomic field", Ann. Math. 108 (1978), doi:10.2307/1970932 | stickelberger-cyclotomic-units.md | Index [R^-:S^-] and [E+:C+] in terms of h, h+, h^- |
| Thaine, "On Fermat's last theorem and the arithmetic of Z[zeta_p+zeta_p^-1]", J. Number Theory 29 (1988), doi:10.1016/0022-314X(88)90107-2 | zetap-ring-ramification.md | Ring Z[zeta_p], total ramification, coprime ideals off (1-zeta_p), valuation identity |
| Steidl & Tasche, Math. Nachr. 140 (1989), doi:10.1002/mana.19891400116 | zetap-ring-ramification.md | Prime ideal factorisation of cyclotomic values; ramification machinery |

## Screened / refused by the evidence policy (do not re-request)

The published proofs of the challenge equation are treated as "the answer" and
refused at the network boundary:

- **Mihailescu 2002** proof of Catalan's conjecture — refused (published answer).
- **Cassels 1960** "On the equation a^x - b^y = 1" — refused (its exact conclusion
  q|x, p|y is the answer's first step).
- Effective bounds on exponents for THIS equation from linear forms in
  logarithms — refused.
- Pillai / gaps-between-perfect-powers surveys of the specific equation —
  refused.

These remain open gaps (`closing-lemma`, `cassels-divisibility`,
`double-wieferich` in REQUESTS.md); the run must re-derive them from the
technique tier now held.

## Frontier leads worth following (from source citation lists, deduplicated)

- **Washington, "Introduction to Cyclotomic Fields", GTM 83 (2nd ed.)** — the
  canonical reference behind every source above (Thm 4.17 / Cor 4.13 = relative
  class number formula; Stickelberger; cyclotomic units). Cited by Shokrollahi,
  Ichimura, Hirabayashi, Thaine. Highest-value single acquisition when a route
  to the full text opens.
- **Sinnott 1978** (held) → its own "Cited by" is the research front that uses
  Stickelberger/unit indices; candidates for the descent's modern form.
- **Schoof, "Minus class groups of cyclotomic fields of prime conductor"**,
  Math. Comp. 67 (1998), 1225–1245 — direct source for computing the *minus*
  part structurally (the obstruction's computable half).
- **Kimura & Horie, "On the Stickelberger ideal and the relative class number"**,
  Trans. AMS 302 (1987) — cited by both Ichimura and Shokrollahi; another index
  formula.
- **Masley, class numbers of cyclotomic fields** (via Miller/Schoof) — the
  p<=67 unconditional class-number range.
