# Rome & Yamagishi, "On the existence of magic squares of powers", arXiv:2406.09364 (2024)

[[rome-yamagishi-magic-squares-of-powers-2024]]

**Status: abstract page only on disk** — the `.full.md` is the arXiv landing page (title, abstract, MSC); the paper body was never downloaded. Everything below is at abstract level.

## What it establishes (abstract-level)

- **Theorem (d-th powers, all large n):** for every `d ≥ 2` there is an integer `n₀(d)` such that an `n × n` magic square of distinct `d`-th powers exists for **all `n ≥ n₀(d)`**.
- **Corollary (squares):** an `n × n` magic square of squares exists for **all `n ≥ 4`**. This **settles a conjecture of Várilly-Alvarado**.
- **Method:** Hardy–Littlewood circle method; the problem reduces to a sufficient number of disjoint linearly independent subsets of the columns of the magic-square equations' coefficient matrix; an optimal (up to constant) lower bound is proved. The v2 note says a revised algorithm makes computer search unnecessary, with proper credit to prior work of Flores.

## What it does NOT say

- **Nothing about n = 3** — the 3×3 case is precisely the open one (LaBar 1984 / Gardner $100). The `n ≥ 4` existence does not bear on `n = 3` either way: it is not a construction that specialises, and it gives no obstruction. The 3×3 case remains open as before (the paper's own abstract is silent on it).

## Implications for this run

- **Context only.** Confirms that the *obstruction is dimension-specific*: squares-of-squares magic arrays are plentiful once `n ≥ 4` but (conjecturally, and by decades of search) absent at `n = 3`. This sharpens the statement of the open problem: the 3×3 case is not an instance of a general scarcity, it is an isolated small-n phenomenon.
- No claim block for the ledger: the abstract-level theorem is about `n ≥ 4` and `holds-here: no` for the 3×3 problem; there is nothing here that constrains or constructs a 3×3 MSS. Recorded so nobody re-fetches this for a 3×3 statement that is not there.
- If the run ever wants the proof method (or the Flores prior work, or the Várilly-Alvarado conjecture statement), the PDF must be fetched; the abstract cannot support it.

## Does not help

For the 3×3 non-existence goal: no theorem, bound, or construction applies to n=3. The only durable value is the negative framing above (scarcity is small-n-specific), which this run already holds from Bremner (the 4×4 Euler MSS and the n≥4 families).