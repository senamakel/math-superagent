# Ramírez & Rubiano — On the k-Fibonacci words

Source: José L. Ramírez, Gustavo N. Rubiano, "On the k-Fibonacci words", Acta
Universitatis Sapientiae, Informatica 5(2) (2013) 212–226, DOI 10.2478/ausi-2014-0011.
Full text: `research/sources/ramirez-rubiano-k-fibonacci-words-docslib.full.md`
(URL recorded in file: https://docslib.org/download/1393306/on-the-k-fibonacci-words).
The earlier journal-landing-page capture `...-k-fibonacci-words.full.md` is
superseded by this full text.

## What it establishes

- Defines the **k-Fibonacci words** over {0,1}: f_{k,0} = 0, f_{k,1} = 0^{k-1}1,
  f_{k,n} = f_{k,n-1} f_{k,n-2} for n ≥ 2. The length satisfies |f_{k,n}| =
  F_{k,n+1}, the (k+1)-step... actually the k-Fibonacci numbers
  F_{k,0}=0, F_{k,1}=1, F_{k,n+1} = k·F_{k,n} + F_{k,n-1}. For k=1 this is the
  standard Fibonacci word (f_{1,0}=0, f_{1,1}=01, f_{1,n}=f_{1,n-1}f_{1,n-2} =
  PE1006's S_n with S_0=0, S_1=01).
- The infinite k-Fibonacci word f_k = lim_n f_{k,n} generalizes the Fibonacci
  word; the paper studies its combinatorial properties (lengths, letter counts,
  structure) and associates a family of curves with fractal patterns.
- Uses the vocabulary of Lothaire and Allouche–Shallit.

## Relevance to PE1006

This is the **adjacent-problem/generalization** source for the exact word the
problem is about (k=1 gives S_n). It is a catalogue/combinatorial source, not a
theorem about decimal second moments; it confirms the standard definitions and
the recurrence. A useful bounded cross-check: the k=1 case reproduces S_n and
|S_n| = F_{n+1} (A000045 convention), which the run's brute oracle already
verifies.

## Claim block

```claim
id: ramirez-rubiano-k-fibonacci-words
statement: The k-Fibonacci words f_{k,n} over {0,1} defined by f_{k,0}=0,
f_{k,1}=0^{k-1}1, f_{k,n}=f_{k,n-1}f_{k,n-2} have length |f_{k,n}|=F_{k,n+1}
where F_{k,0}=0, F_{k,1}=1, F_{k,n+1}=k·F_{k,n}+F_{k,n-1}; the k=1 case is the
classical Fibonacci word (PE1006's S_n), the archetype of a Sturmian word.
hypotheses: k ≥ 1; binary alphabet.
holds-here: true — k=1 gives exactly S_0=0, S_1=01, S_n=S_{n-1}S_{n-2}.
status: sourced
bearing: Generalization/adjacent-problem source fixing the standard definitions
of the word PE1006 is about; confirms |S_n| = F_{n+1}. Not the G4 collapse.
anchor: research/sources/ramirez-rubiano-k-fibonacci-words-docslib.full.md
(https://docslib.org/download/1393306/on-the-k-fibonacci-words)
answers: frontier-k-fibonacci-cluster
```
