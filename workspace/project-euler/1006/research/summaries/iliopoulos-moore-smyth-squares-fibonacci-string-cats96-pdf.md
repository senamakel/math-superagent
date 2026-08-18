# Iliopoulos, Moore & Smyth — A linear algorithm for computing all the squares of a Fibonacci string

Source: Costas S. Iliopoulos, Dennis Moore, W.F. Smyth, "A linear algorithm for
computing all the squares of a Fibonacci string", Proceedings of CATS '96
(Computing: The Australasian Theory Symposium, Melbourne, January 1996); the
journal version is *A characterization of the squares in a Fibonacci string*,
Theoretical Computer Science 172 (1997) 281–291.
Full text (OCR-heavy scanned PDF): `research/sources/iliopoulos-moore-smyth-squares-fibonacci-string-cats96-pdf.full.md`
(URL recorded in file:
https://researchportal.murdoch.edu.au/view/pdfCoverPage?download=true&filePid=13136928880007891&instCode=61MUN_INST).
The earlier landing-page-only capture `...-cats96.full.md` is superseded by this.

## What it establishes

- Fibonacci strings F_n: F_0 = b, F_1 = a, F_n = F_{n-1}F_{n-2}; the infinite
  Fibonacci string F contains every F_n as a prefix.
- **Characterization of all squares in F** (hence in every F_n): squares occur
  in consecutive **runs** — each run consists of cyclic rotations of a
  Fibonacci string F_k; the number of runs in F_n is Θ(f_n).
- This yields a Θ(f_n)-time algorithm specifying all squares of F_n in an
  appropriate encoding (a triple (i,p,k) per primitive-rooted square), versus
  Θ(f_n log f_n) for the general repetition algorithms.
- The square runs at adjacent positions are precisely cyclic rotations of the
  same Fibonacci word — the structural fact the run's claim
  `fibonacci-squares-conjugate-finite-word` cites from
  Du–Mousavi–Schaeffer–Shallit.

## Relevance to PE1006

This is the primary for "**squares in the Fibonacci word are cyclic rotations
of Fibonacci words**", the square-structure theorem behind the k = F_n − 1
conjugate/rotation picture the run sums over (directive 1, Chuan moments).
It confirms that the square structure is run-based — consistent with the
run's finding that the right-special factors and extension recurrences are
run-structured (Lmin(k) = k + NextFib(k) − 1). It does not give the decimal
second-moment collapse.

## Claim block

```claim
id: iliopoulos-moore-smyth-squares-runs-cyclic-rotations
statement: All squares of the infinite Fibonacci string F (limit of
F_0=b, F_1=a, F_n=F_{n-1}F_{n-2}) occur in consecutive runs; each run consists
of cyclic rotations of a Fibonacci string F_k, and F_n has Θ(f_n) such runs.
This characterisation gives a Θ(f_n) algorithm enumerating all squares of F_n
in triples (i,p,k), improving on the general Θ(f_n log f_n) bound.
hypotheses: F_n Fibonacci strings over {a,b}; squares = uu with u primitive-rooted.
holds-here: true — PE1006's S_n (0→01, 1→0) is the letter-renamed F_n (a→0, b→1
complemented); square runs are cyclic-rotation runs.
status: sourced
bearing: Primary for the squares-are-cyclic-rotations structure the k=F_n−1
conjugate/rotation sum rests on; run-based square structure matches the run's
Lmin/right-special run findings. Not the G4 collapse.
anchor: research/sources/iliopoulos-moore-smyth-squares-fibonacci-string-cats96-pdf.full.md
(https://researchportal.murdoch.edu.au/view/pdfCoverPage?download=true&filePid=13136928880007891&instCode=61MUN_INST)
answers: frontier-square-structure-cluster
```
