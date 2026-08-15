# Odlyzko publications page — bibliography only, no content statements

Source: https://www-users.cse.umn.edu/~odlyzko/doc/old/cnt.html (converted from
HTML). Full text: [[odlyzko-publications-page.full]].

## What it establishes

Nothing usable for this run. It is a bibliography page listing Andrew Odlyzko's
computational number theory papers with links. The only row relevant to
Gilbreath:

> **Iterated absolute values of differences of consecutive primes**, A. M.
> Odlyzko, *Math. Comp.* 61 (1993), pp. 373-380. \[PostScript/PDF/LaTeX links\].

This confirms the paper exists and its pagination/citation, matching the
journal row already cited by encyclopedia-of-math and OEIS A036262. It contains
**no** statement of the block lemma, no verification depth, no proof content.

## What it does not settle

This bibliography page gives only the citation — no content. The block lemma's
exact statement and constant are **NOT read from here**. They are read from the
held primary sources: `research/sources/odlyzko-1993-iterated-differences-latex-source.full.md`
(the author's TeX) and `research/sources/odlyzko-1993-iterated-absolute-differences.full.md`
(PDF), forming the sourced claim `odlyzko-block-lemma`: a leading `{0,2}` block
of length N−1 after a leading 1 protects **N rows** — coefficient exactly 1,
**one row per block entry**, NOT `≈ n/2`. The `≈ n/2` figure is refuted and
appears nowhere in the primary source; do not reintroduce it.

```claim
id: odlyzko-1993-citation-confirmed
statement: Odlyzko's paper "Iterated absolute values of differences of consecutive primes" exists as Math. Comp. 61 (1993) 373-380, per the author's own bibliography page.
hypotheses: the bibliography page is the author's own publication list.
holds-here: yes
status: sourced (bibliography listing)
bearing: confirms the primary source for the block lemma exists and its citation; says nothing about the lemma's content.
anchor: research/sources/odlyzko-publications-page.full.md
answers: does-the-odlyzko-1993-paper-exist
```

## Verdict

**No help for content.** It is one bibliography page; the only value is pinning
the Odlyzko 1993 citation. The block lemma itself — exact constant 1, one row
per `{0,2}` block entry — is established, NOT a gap: it is sourced from the
held Odlyzko 1993 primary text (`odlyzko-block-lemma`) and independently
re-derived by this run. Do not re-open it.
