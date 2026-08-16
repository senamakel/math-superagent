# Makhnev lecture — Wilbrink order-11 attribution

This note records the single most valuable addition from the Makhnev
"Graphs and automorphisms" lecture note: a traceable primary-source citation
for the **order-11 automorphism exclusion** and the **`|G| | 2·3³·7`** bound,
both previously in the library only as recalled/asserted (the Wilbrink 1984
paper itself is paywalled and unobtainable).

```claim
id: wilbrink-order11-sourced
statement: For a putative srg(99,14,1,2) with automorphism group G, G admits no
  automorphism of order 11, and |G| divides 2*3^3*7. This is attributed by
  Makhnev's lecture to H. Wilbrink "On the (99,14,1,2) strongly regular graph"
  (Papers dedicated to J. J. Seidel, Tech. Report 84-WSK-03, TU/Eindhoven 1984,
  pp. 342-355, [4]).
  Together with Makhnev-Minakova's Theorem 1 (also reproduced in the same
  lecture, [3]), the fixed-point dichotomy for a prime-order automorphism g with
  Delta=Fix(g) is: (1) Delta a single vertex and p=2 or 7; (2) Delta empty and
  p=3 or 11; (3) Delta a triangle and p=3. Also: a putative srg(99,14,1,2) is
  locally 7K2 and has spectrum 14^1, 3^54, -4^44; the projected character is
  chi2(g)=(4*alpha0(g)+alpha1(g)-18)/7. For an involution t, Fix(t) is one of
  seven listed graphs and only the one-vertex case gives integer chi2(t).
hypotheses: existence of the putative srg(99,14,1,2) is assumed; the statements
  are constraints on any such graph and its automorphism group.
holds-here: yes — this is exactly the automorphism-orders question the run asked,
  and it now has a primary-source anchor.
status: asserted-by-source (Makhnev's own lecture note, quoting Makhnev-Minakova
  [3] Theorem 1 and Wilbrink [4]); the order-11 exclusion and divisibility bound
  are on Wilbrink's authority as quoted by Makhnev. Not independently re-computed
  here (they are structural, not oracle-decidable).
bearing: confirms and sources the recalled Makhnev-Minakova/Wilbrink bounds that
  problem.md and earlier recall stated. Combined with Crnkovic-Maksimovic (no
  Z6,S3,Z9,E9) and Cesarz-Woldar (computer-free: 2||G| -> |G||6; 7||G| -> G=Z7),
  the automorphism group if nontrivial is small and the triviality of G is open.
anchor: research/sources/makhnev-symmetric-graphs-automorphisms-lecture.full.md
  (lines 179-301, reference [4] at line 1515)
answers: exact-list-prime-051a
```
