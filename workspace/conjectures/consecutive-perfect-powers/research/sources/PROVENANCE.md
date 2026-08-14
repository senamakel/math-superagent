# Library provenance and gaps

What the local reference library holds, where each source lives, what was
obtained and what could not be, and why.

## Available locally (research/sources/)

| File | Source | What it establishes | How obtained |
| --- | --- | --- | --- |
| `cassels-1960-II.md` | Cassels, *Math. Proc. Camb. Phil. Soc.* (1960), "On the equation ax − by = 1. II". DOI 10.1017/s0305004100034332 | Scope record: for `x^p − y^q = 1` with `p,q` odd, any solution has `p | y`, `q | x` — the `cassels-divisibility` / `G-Cassels` gap. | Server-side read of the paper's own abstract and reference list via `read_sources`. Full text not obtained (host blocked). |
| `cassels-1953.md` | Cassels, *Amer. J. Math.* **75** (1953), 159–162. DOI 10.2307/2372624 | Technique origin: divisibility structure of `a^x − b^y = 1`; ancestors of the `p|y, q|x` theorem. | Server-side readout via `read_sources`. Full text not obtained (JSTOR blocked). |
| `sinnott-1978-stickelberger-circular-units.md` | Sinnott, *Annals of Math.* **108** (1978). DOI 10.2307/1970932 | Minus-part index `[R-:S-] = h-` and circular-unit index `[E+:C+]` in a cyclotomic field — the class-group machinery named by the hard descent gap. | Server-side read of abstract via `read_sources`. Full text not obtained. |
| `ichimura-2006-class-number-formula-cyclotomic.md` | Ichimura, *Arch. Math.* **87** (2006), 539–545. DOI 10.1007/s00013-006-1867-7 | Stickelberger/class-number index in `Z[ζ_p]`, incl. `p ≡ 3 (mod 4)`, index-2 sub-case. | Server-side read of abstract. Full text not obtained. |

## Could not be obtained, and why — so nobody retries

- **Mihăilescu's proof of Catalan's conjecture (2002), and any survey or text
  stating/deriving the full classification.** The run's evidence policy screens
  material that would supply the published answer to `problem.md`. It is a
  deliberate, enforced boundary, not a network fault. **Do not retry.** The run
  must re-derive the closure steps itself, in-workspace, from the techniques
  the library supplies.
- **Full texts of all four papers above, and every other publisher-hosted
  paper.** The network boundary permits only the search and data APIs; direct
  fetching of publisher/preprint hosts fails regardless of the URL. Retrying
  mirrors fails the same way. For these the run relies on the server-side
  `read_sources` readouts already recorded, and must treat any full statement
  as to-be-re-derived, not as transcribed.
- **Lebesgue-style write-up of `x^p − y^2 = 1` and the effective Tijdeman
  bound**: both queries returned material screened as answer-bearing. The
  exponent-2 cases are elementary and will be re-derived in-workspace (Z and
  Z[i]); the effective bound is a "gathering" item whose exact size the run
  should aim to state from a re-derivation or a non-answer source.

## Where the gaps point next (see REQUESTS.md)

The REQUESTS.md rows already capture the four exact gaps the library was aimed
at: `exact-closing-lemma-b571` (the closing step), `exact-statement-citable-f890`
(Cassels divisibility + double-Wieferich), `exact-statement-mihăilescu-bbf8`
(the descent in the minus class group), `exact-statement-primary-1ad5` (whether
the full goal is proved or open). This library gives those gaps their technique
foundation (Cassels divisibility, Stickelberger/minus-class machinery) but does
**not** supply their answers — the screener prevents it, by design. They remain
open and must be closed by the run's own derivation, with claims logged against
them.
