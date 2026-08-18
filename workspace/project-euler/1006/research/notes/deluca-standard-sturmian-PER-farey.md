# Standard Sturmian words and the PER/Farey structure (de Luca 1997)

Source: de Luca, "Sturmian words: structure, combinatorics, and their arithmetics",
Theoretical Computer Science 183 (1997) 45–82, DOI 10.1016/S0304-3975(96)00310-6.
Full+intro captured at `research/sources/deluca-sturmian-words-structure-arithmetics-1997-docslib.full.md`
(https://docslib.org/doc/3630572); summary at
`research/summaries/deluca-sturmian-words-structure-arithmetics-1997.md`.

This is the finite/standard-word side of the factor structure that the run's
directive 1 rotation argument (at k = F_n − 1 the k+1 factors are the F_n
conjugates of the truncated standard word) rests on. It complements the
infinite-word side already held (Berstel DLT'95/2007, Lothaire C2,
Perrin–Restivo).

```claim
id: standard-sturmian-PER-farey-construction
statement: A standard Sturmian word s is built from a sequence of positive integers
q_0>0, q_i>0 by s_0=b, s_1=a, s_{n+1}=s_n^{q_n-1}s_{n-1}; every standard Sturmian word
arises so. The set PER of words with two coprime periods p,q and |w|=p+q-2 satisfies
w∈PER iff (aw)^(-),(bw)^(-)∈PER under palindrome left-closure, and PER is the smallest
such set over {ε}. PER bijects to the irreducible fractions p/q (Farey correspondence);
the length-n suffixes of A_n={w∈PER: ||w||=p/q, q≤n+1, p+q−2≥n} coincide with the
right-special length-n factors of the finite Sturmian words St.
hypotheses: binary alphabet; p,q coprime; standard (origin-starting) Sturmian word.
holds-here: yes — at k=F_n−1 the k+1 distinct length-k factors are the F_n rotations of
the standard word q_n, which are elements of the standard-Sturmian/PER structure; the
Fibonacci word is the all-partial-quotients-1 case (q_n = {a,b}, every q_i = 1).
status: sourced
bearing: Anchors the finite standard-word construction directive 1's rotation argument
uses, and the special-factor/right-special description of the k+1 factors that the
factor count k+1 already fixes.
anchor: research/sources/deluca-sturmian-words-structure-arithmetics-1997-docslib.full.md
(Introduction: definitions of Sturmian, standard Sturmian via q_n recursion, PER set,
palindrome left-closure, Farey correspondence to irreducible fractions and to the
right-special factors SR(n)).
```

The captured text is only the abstract + full Introduction (body pages did not
convert on this mirror); each structural item above is stated in the captured
part and proved there, but the numbered proofs are on the journal pages not in
this capture. Full proofs of the same results are on disk in the Berstel DLT'95
and 2007 surveys and Lothaire C2 chapter.
