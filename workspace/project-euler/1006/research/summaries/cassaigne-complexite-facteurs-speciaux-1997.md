# Cassaigne — Complexité et facteurs spéciaux (Bull. Belg. Math. Soc. 4, 1997)

**Source:** Julien Cassaigne, "Complexité et facteurs spéciaux",
Bull. Belg. Math. Soc. 4 (1997) 67–88.
Full text: `research/sources/cassaigne-complexite-facteurs-speciaux-1997.full.md`
(from https://emis.muni.cz/journals/BBMS/Bulletin/bul971/cassaigne.pdf,
EMIS mirror of the journal; received 1995, published 1997).

## What this source is

A primary research paper on the *special-factor machinery* of factor complexity.
For an infinite sequence `u` over a finite alphabet, `p(n)` counts the length-`n`
factors. A factor is **right-special** if it extends to the right in more than one
way; **left-special** similarly; **bispecial** if both. The paper shows these two
objects control the first and second differences of `p`:

- for every recurrent sequence, `p(n+1) − p(n)` equals the number of right-special
  factors of length `n`;
- the second difference is governed by the bispecial factors (with a small
  correction depending on the number of extensions).

It then uses this to compute complexity of substitutive sequences (circular
morphisms) and to decide which functions can be complexity functions. The paper's
running example throughout §3.1 is the **Fibonacci word**
`abaababaabaab...` (fixed point of a→ab, b→a) in its right-factor tree (Figure 1).

## Why the library holds it

The run's governing claim `governing-factor-complexity` (Sturmian ⇒ p(k) = k+1)
and the slope-stabilisation argument (`farey-slope-stabilisation`) rest on the
fact that for the Fibonacci word the number of new factors per length is exactly
1 — equivalently, exactly one right-special factor of each length. Cassaigne is
the standard reference for the special-factor ↔ complexity-difference link the
frontier repeatedly cited (Berthé 1996's "≤ 3 frequencies" theory is built on the
same vocabulary). It is the missing *tool* reference behind the count `k+1`:
Morse–Hedlund give the bound, Cassaigne gives the counting machinery.

## Statements extracted (with page references in the .full.md)

1. (p. 68) Sturmian sequences have complexity `p(n) = n + 1` — one of the two
   canonical low-complexity examples (with ultimately periodic).
2. (§3, p. 69–70) For a factorial prolongable language / recurrent sequence,
   `p(n+1) − p(n)` equals the number of right-special factors of length n; this
   is the bridge used to compute complexity from special factors.
3. (p. 68) Classical result recalled: an unbounded complexity function satisfies
   `p(n) ≥ n + 1` for all n (the Morse–Hedlund minimal-complexity theorem).

```claim
id: special-factor-complexity-difference
statement: For a recurrent infinite sequence over a finite alphabet, the first
difference of the factor complexity is exactly the number of right-special factors
of that length: p(n+1) - p(n) = #{right-special factors of length n}. Bispecial
factors govern the second difference. For Sturmian sequences p(n) = n+1, so there
is exactly one right-special factor of each length. Cassaigne develops this
special-factor machinery and applies it to the Fibonacci word (a->ab, b->a
fixed point) as the running example of a substitutive sequence.
hypotheses: recurrent (or factorial prolongable language) infinite word over a
finite alphabet; complexity p(n).
holds-here: yes — the infinite Fibonacci word is recurrent (indeed uniformly
recurrent / minimal), so p(k+1)-p(k) = 1 means exactly one right-special factor
of each length k, matching the k+1 factor count of PE1006.
status: sourced
bearing: Provides the primary counting tool behind the factor count k+1 and the
mechanical construction's single-expansive-factor structure; complements the
Morse–Hedlund bound with a computable counting machinery.
anchor: research/sources/cassaigne-complexite-facteurs-speciaux-1997.full.md
(https://emis.muni.cz/journals/BBMS/Bulletin/bul971/cassaigne.pdf)
```

## Note (obtained / not obtained)

The English DLT'95 companion "Special factors of sequences with linear subword
complexity" (Developments in Language Theory, World Scientific, 1995, 25–34)
is hosted at http://iml.univ-mrs.fr/~cassaign/publis/ferenczi.pdf but that host
refused the connection twice this cycle (http and https), as did a CiteSeerX
mirror. The French 1997 journal version covers the same special-factor tool and
is authoritative for the claims extracted above; the DLT'95 paper's *additional*
content (linear-complexity ⇒ bounded first difference, the Ferenczi-conjecture
proof) is not needed for this run — the factor count k+1 is already sourced from
Morse–Hedlund / Sturmian theory. Non-blocking.