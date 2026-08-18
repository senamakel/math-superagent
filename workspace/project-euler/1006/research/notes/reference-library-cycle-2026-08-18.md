# Reference-library cycle — 2026-08-18

## Search and sources

Searches covered the official PE1006 statement, Sturmian/mechanical-word theory, weighted Euclidean floor sums, and Fibonacci subword algorithms. The official page was downloaded as `research/summaries/projecteuler-1006-official.html.md` from https://projecteuler.net/problem=1006. It records the exact recursive definition, the k+1 factor fact, Ψ(3)=20302, and Ψ(10) mod 101001001=10699667.

`research/sources/sturmian-words-beta-shifts-arxiv-0308140.html.full.md` was downloaded from https://doi.org/10.48550/arxiv.math/0308140. It is a secondary theoretical source connecting Sturmian words, mechanical words, irrational rotations, and factor complexity.

`research/sources/fibonacci-word-factor-location-2010.html.full.md` was downloaded from https://apacz.matinf.uj.edu.pl/publikacje/6252-a_simple_representation_of_subwords_of_the_fibonacci_word. It is a bibliographic/landing-page source for the 2010 Information Processing Letters paper, DOI https://doi.org/10.1016/j.ipl.2010.08.006, relevant to representations and location of Fibonacci factors.

`research/sources/rytters-subword-graphs-docslib.html.full.md` was downloaded from the search-result URL https://docslib.org/doc/6989481/the-structure-of-subword-graphs-and-suffix-trees-of-fibonacci-words. It provides an accessible copy/digest of Rytter's structural treatment: factor occurrence sets reduce to occurrences in a shortest truncated Fibonacci word, and Fibonacci subword graphs/DAWGs have an explicit recursive structure.

Citation graphs were run for DOI 10.1016/j.ipl.2010.08.006, arXiv 0308140, and the existing Lothaire book DOI 10.1017/CBO9781107326019. The resulting leads were added to `derived/FRONTIER.md`; no published Project Euler solution was searched or downloaded.

## Established local theory

The principal governing theory remains Sturmian-word theory: the infinite Fibonacci word (limit of S_n) is a characteristic Sturmian/mechanical word of slope 1/φ², and an irrational Sturmian word has factor complexity p(k)=k+1. The efficient numerical reduction already present in this workspace uses the floor-difference mechanical representation and a universal-Euclidean weighted floor-sum monoid carrying zeroth, first, and second geometric moments. The AtCoder/Euclidean recursion has O(log denominator/parameters) structural cost, not O(k). Existing local sources include Perrin's mechanical-word lecture, Lothaire's Sturmian chapter, AtCoder's floor_sum implementation, and the universal-Euclidean references listed in `research/notes/reference-library-report.md`.

The new Rytter source is useful as an independent structural cross-check for factor occurrence/location, but it does not establish the final Project Euler residue and is not cited as such.

## Retrieval limitation

The first `remember_memory` attempt failed because the memory server health check timed out. This note is the durable workspace record; retry Cognee storage in a later cycle when the service is healthy.
