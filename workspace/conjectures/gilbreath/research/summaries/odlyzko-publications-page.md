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

The Odlyzko 1993 block lemma (a `{0,2}` block of length `n` protecting `≈ n/2`
rows) is **not** given here — only that the paper exists. The exact statement
and its constant remain a pending dependency (`odlyzko-block-lemma-asserted`,
`holds-here: unchecked`). Do not cite this page for anything beyond the
existence/citation of the paper.

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
the Odlyzko 1993 citation so a later fetch can target the exact paper. The
block-lemma gap stands open.
