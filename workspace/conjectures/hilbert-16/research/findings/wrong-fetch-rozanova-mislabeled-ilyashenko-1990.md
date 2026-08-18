# Wrong-fetch record: Rozanova PDE paper mislabeled as Ilyashenko 1990

**This file is a mistake record, not a source.**

On 2026-08-19 the librarian guessed a mathnet paperid (`4668`) for Ilyashenko's
1990 "Finiteness theorems for limit cycles" (Russian Math. Surveys 45:2) and
fetched `https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=4668&what=fullteng&option_lang=eng`.
That record is **O. S. Rozanova, "On the unboundedness of solutions of a system
of partial differential equations", Communications of the Moscow Mathematical
Society** — an unrelated PDE paper. The URL was a guess, not a seen search
result, and it produced exactly the failure mode the librarian policy forbids:
a fetch of an invented address storing the wrong paper under a name it wanted.

## What the correct record is

The genuine Ilyashenko 1990 survey (Uspekhi Mat. Nauk 45:2 (1990), 143-200;
Russian Math. Surveys 45:2, 129-203) is at mathnet paperid **rm4718**, found via
a cited reference in a 2025 Dolov/Morozov article that gives
`https://www.mathnet.ru/rus/rm4718`. It is now held at
`research/sources/ilyashenko-1990-finiteness-theorems-rms-primary.full.md`
(3.4 MB source, 163 KB converted), verified by first lines: "Finiteness
theorems for limit cycles / Yu.S. Il'yashenko", contents, and Theorem I–IV.

## Lesson

Never guess a mathnet paperid. The paperid is not derivable from the DOI. Get
it from a citation that already carries the URL (`mathnet.ru/rus/rmNNNN`), then
fetch `getFT.phtml?jrnid=...&paperid=NNNN&what=fullteng&option_lang=eng`. Verify
the first lines of the landing text against the expected title before treating a
fetch as the paper.

The mislabeled file `research/sources/ilyashenko-1990-finiteness-theorems-rms-fulltext.full.md`
(and its digest) is being deleted so it cannot be cited.
