# Claim — de Luca's division property of the Fibonacci word

Statement as carried by Fici (2015), "Factorizations of the Fibonacci infinite word",
arXiv:1508.06754, Prop. 10–11, anchored in the library at
`research/sources/fici-factorizations-fibonacci-infinite-word-ar5iv.full.md`
(lines 380–410). The original is A. de Luca, "A division property of the
Fibonacci word", Information Processing Letters 54 (1995) 307–312,
DOI 10.1016/0020-0190(95)00067-M (paywalled; statement verified via Fici's
proof, which cites [5] de Luca directly).

## Convention (checked against the displayed blocks)

Fici indexes the finite Fibonacci words f_1 = 1, f_2 = 0, f_n = f_{n-1}f_{n-2},
so f_3 = 01, f_4 = 010, f_5 = 01001, f_6 = 01001010, f_7 = 0100101001001,
f_8 = 010010100100101001010. This maps to PE1006's S_n (S_0 = 0, S_1 = 01,
S_n = S_{n-1}S_{n-2}) by **f_{n+2} = S_n**. The infinite word f is the S_n limit.

```claim
id: deluca-division-property-fibonacci-word
statement: The infinite Fibonacci word f (PE1006's S_n limit, 0->01, 1->0
convention) is the concatenation of the reversals of the even finite Fibonacci
words: in Fici's indexing f = prod_{n>=2} f~_{2n} = f~_4 . f~_6 . f~_8 ...
= 010 . 01010010 . 010100101001001010010 ...; equivalently in PE1006's S_n
indexing (S_n = f_{n+2}), S_inf = prod_{n>=1} S~_{2n} = S~_2 . S~_4 . S~_6 ...
where S~ is reversal. The odd version: f = 0 . prod_{n>=2} f~_{2n+1}
= 0 . 10010 . 1001001010010 ..., i.e. S_inf = 0 . S~_3 . S~_5 . S~_7 ...
This factorization (de Luca 1995) is minimal in the lexicographic order: any
non-trivial permutation of finitely many of its factors yields an infinite word
strictly greater than f. It is the Crochemore factorization of f (up to the
initial block).
hypotheses: f the infinite Fibonacci word (standard morphism convention);
f~_n the reversal of the n-th finite Fibonacci word in Fici's indexing
(f_1=1, f_2=0); lexicographic order on infinite binary words.
holds-here: yes — this is exactly PE1006's S_n limit word; the even-reversal
block decomposition gives a renormalisation of f by Fibonacci-length blocks.
status: sourced
follows-from: none (primary structural fact; Fici Prop. 10–11 prove it from the
finite-word recurrence and cite de Luca [5])
bearing: Provides a canonical Fibonacci-block decomposition of the infinite
word f itself (not of its factor set). Relevant to any Fibonacci-block
renormalisation attempt for Psi(k): if a fixed-dimensional state aggregates
decimal-window values across such blocks, the division property is the
concatenation identity it would rest on. It is NOT by itself a statement about
the length-k factor set or about decimal-weight moments — those still need the
joint-intercept aggregation (G4).
anchor: research/sources/fici-factorizations-fibonacci-infinite-word-ar5iv.full.md (Prop. 10, 11, lines 380-410)
```

## Corroboration

- Amy Glen's thesis outline (Bull. Austral. Math. Soc. 74 (2006) 155–160, held
  at `research/sources/glen-sturmian-episturmian-words-thesis-2006.full.md`)
  Ch. 7 generalizes de Luca's division property to episturmian words.
- Glen–Justin–Pirillo "Characterizations of finite and infinite episturmian
  words via lexicographic orderings" (EJC 28 (2007)) develops the
  lexicographic-inequality framework (`min(s) <= max(s) <= bs` characterizing
  standard Sturmian words), the setting in which the minimality statement lives.

## Boundary

The division property decomposes f into *reversed* Fibonacci words; the run's
S_n use the *unreversed* recurrence. The relation f~_n = (complement?) of f_n
does not hold — reversals are genuine new blocks (Fici: reversals of Fibonacci
words start with 00 and 11 alternatingly). Any block-state construction must
handle the reversal explicitly. Check any use against the displayed blocks
above; the S_n-indexed form is S_inf = S~_2 . S~_4 . S~_6 . ... and
S_inf = 0 . S~_3 . S~_5 . ...

