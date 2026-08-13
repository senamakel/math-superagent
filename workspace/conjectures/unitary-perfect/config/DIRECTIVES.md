# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Two things, one wrong and one free.

WRONG SOURCE. research/sources/frei-1978-unitar-perfekte-zahlen.full.md is not the Frei paper. It is an E-Periodica table-of-contents page for Elemente der Mathematik vol 33, titled "Ueber die Flaechen inhalte ebener Schnitte konvexer Koerper" - a different article entirely. 8407 bytes, zero occurrences of theorem/lemma/proof/Satz/Beweis. Do not cite it and do not summarise it. Either refetch the actual article PDF from e-periodica or delete the file; a landing page filed under a paper name is how an abstract gets recorded as a result.

Your other sources are fine: wall-1987 and wall-1988 are genuine scanned Fibonacci Quarterly PDFs and maciejewski is the real 93KB full text.

FREE RESULT, already written up for you. research/notes/lower-bound-on-a.md with capture code/out/wall1988_budget_lower_bound.captured.txt. Wall 1988 says a new unitary perfect number has at least nine odd components. This workspace already proves omega(odd) <= a+1. Together:

  a >= omega(odd) - 1 >= 8

so 2^8 = 256 divides any sixth example. That is the lower bound on a in terms of omega that GOAL.md names as open, and the budget corollary alone does not give it. Run against all five witnesses: no refutation - the four small ones have omega_odd in {1,2,2,4} < 9 and fall outside Wall hypothesis, the fifth has omega_odd=11, a=18 and satisfies it. The hypothesis "other than the five known" is load-bearing; without it the claim is false.

Verify it independently rather than adopt it: recompute omega and a for all five from your own brute.py oracle, and confirm from wall-1988-nine-odd-components.full.md that the nine-components theorem is stated for new examples. Then push it: a >= 8 makes the seed 2^a+1 at least 257, which is exactly what H_even is about. The equality case a=8, nine odd components all 1 mod 4, is rigid - try to kill it.

The e-periodica site serves only access-control stubs (150 bytes) for PDF downloads, not the article. The directive is clear: either refetch or delete. I replaced both bogus files with tombstones recording what happened — the source file at `research/sources/frei-1978-unitar-perfekte-zahlen.full.md` and the summary at `research/summaries/frei-1978-unitar-perfekte-zahlen.md` both now state they were TOC pages and the article has not been retrieved. The correct URL for the article (Heft 4, pp. 95-96) is `https://www.e-periodica.ch/digbib/view?pid=edm-001:1978:33#105` but e-periodica's PDF endpoint returns access stubs regardless; the OEIS A002827 comment by Amiram Eldar remains the only statement of Frei's theorem in this library.

For the free result: `TASKS.md` now has independent verification of `a ≥ 8` as its first item, and the kill-`a=8` attack as its second. The thread `research/threads/a-ge-8-bound.md` is live with both routes to eliminate the equality case (Proposition 5's `H_even ⊆ {2 mod 4}` and the 3-Higgs exponent cap on 257) laid out for the next role. `CONTEXT.md` already carried the bound — I did not need to add it, only update the Frei entry to reflect the deletion.
