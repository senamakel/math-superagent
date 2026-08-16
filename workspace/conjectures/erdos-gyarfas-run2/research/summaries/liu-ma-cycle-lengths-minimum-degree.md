# Liu & Ma, "Cycle lengths and minimum degree of graphs" — full text

**Source:** Chun-Hung Liu, Jie Ma, arXiv:1508.07912 (2015); published J. Combin.
Theory Ser. B 134 (2019) 36–75, doi:10.1016/j.jctb.2018.05.002.
**Held:** `research/sources/liu-ma-cycle-lengths-minimum-degree.full.md`
(110 KB, arXiv experimental HTML). Abstract only before this cycle; full text
now held.

## What it establishes (primary text) — the interval/congruence machinery at minimum degree

This is the paper `problem.md` names as a lead ("Liu–Ma") and the primary
source of the *minimum-degree* interval machinery — as opposed to the huge-
*average*-degree results (Sudakov–Verstraëte; Liu–Montgomery) which are the
only two that actually force a 2-power. It is the cleanest statement of the
**obstruction the run must beat** at exactly the regime δ ≥ 3.

All results for min degree ≥ k+1:

- **Thm 1.1 (paths, bipartite):** G 2-connected bipartite, all vertices except
  x,y degree ≥ k+1 ⇒ k paths from x to y with the length condition
  (consecutive lengths increasing by 2). Tight: K_{k,n}.
- **Thm 1.2 (cycles, bipartite):** all vertices except v degree ≥ k+1 ⇒ k
  cycles with the length condition. Cor: min-degree-(k+1) bipartite ⇒ k such
  cycles.
- **Thm 1.3 (general):** δ ≥ k+1 ⇒ ⌊k/2⌋ cycles of **consecutive even lengths**
  and (if 2-connected non-bipartite) ⌊k/2⌋ of **consecutive odd lengths**.
  Tight: K_{k+2}.
- **Thm 1.4:** 3-connected non-bipartite, δ ≥ k+1 ⇒ 2⌊(k−1)/2⌋ cycles of
  consecutive lengths (improves Fan 2015; answers Bondy–Vince).
- **Thm 1.5:** 2-connected non-bipartite, δ ≥ k+3 ⇒ k cycles with consecutive
  lengths or the length condition.
- **Thm 1.6:** δ ≥ k+4 ⇒ k cycles with consecutive lengths or the length
  condition.
- **Modulo-k (Thms 1.9–1.11):** settle Thomassen's Conjectures 1.7/1.8 for
  even k (δ ≥ k+1 gives all even lengths modulo k, and all lengths modulo k if
  2-connected non-bipartite); odd k needs δ ≥ k+3 (2-connected non-bip) or
  δ ≥ k+4 (general).
- **Chromatic number (Thms 1.12–1.13):** χ(G) ≤ 2·min{ce(G),co(G)} + 3 and
  χ(G) ≤ c(G) + 4, where ce/co/c count consecutive even/odd/plain cycle
  lengths.

## Why it matters here — the obstruction, from primary text

Every Liu–Ma result produces a *block of consecutive or residue-termed cycle
lengths*, not a cycle at a *prescribed* power of two. At δ = 3 (k = 2),
Theorem 1.3 gives ⌊2/2⌋ = **1 even cycle-length pair** — i.e. two cycles
differing by 2, and a 4- or a 6-cycle — which is exactly Bondy–Vince. It does
**not** force an 8-, 16-, or 32-cycle. The gaps between powers of two double
each step, so a consecutive-length block of length ℓ only forces a 2-power when
ℓ exceeds the largest power of two below it; δ ≥ 3 buys blocks of length ~k
only, far short of that. **Conclusive confirmation, from the primary source,
that interval results cannot settle Erdős–Gyárfás at δ = 3 — the run must
produce a cycle at a prescribed length.**

The relevant Liu–Montgomery result (opening of their separate paper, 2010.15802,
also held) that *does* force a 2-power runs on **average degree ≥ d** for an
absolute constant d ≫ 3 — the contrasting regime. Summary in
`summaries/liu-montgomery-odd-cycle-and-powers-of-two.md`.

## Notes

- References 11/36 list the surrounding literature (Dirac, Voss–Zuluaga,
  Bondy–Vince, Häggkvist–Scott, Verstraëte, Sudakov–Verstraëte, Fan [19],
  Thomassen). Narrows the "adjacent cycle-length machinery" section.

**Claim block (for CLAIMS.md):**

```claim
id: lm-min-degree-interval-results
statement: For δ(G) ≥ k+1, G contains ⌊k/2⌋ cycles of consecutive even lengths (and, if 2-connected non-bipartite, ⌊k/2⌋ of consecutive odd lengths); modular and consecutive-length strengthenings as in Thms 1.4–1.11. No result prescribes a specific power of two.
hypotheses: min degree ≥ k+1 (various connectivity/parity conditions per theorem); simple finite graph
holds-here: yes — the exact regime δ≥3 is k=2, giving a 2-cycle pair differing by 2 (a 4- or 6-cycle), not a 2-power
evidence-class: asserted by source (primary text), a peer-reviewed JCTB paper; not re-derived here
falsifies: any δ≥3 graph with no two cycles differing by 2 (contradicts Bondy–Vince/Thm 1.3 at k=2) — none is known; or any theorem that forces a 2-power from δ≥3, which this paper (and all consecutive/intermodular results) demonstrably does not
source: research/sources/liu-ma-cycle-lengths-minimum-degree.full.md, Thms 1.1–1.13
```
