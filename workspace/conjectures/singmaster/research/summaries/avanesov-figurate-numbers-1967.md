# Avanesov 1967 — "Solution of a problem on figurate numbers" (Acta Arith. 12)

Source: Э. Аванесов (E. T. Avanesov), "Решение одной проблемы фигурных чисел"
(Solution of a problem on figurate numbers), Acta Arithmetica 12 (1967)
409–420, DOI 10.4064/aa-12-4-409-420.

## What is held

- **Landing page** (Russian, CC-BY freeshare notice):
  `research/sources/avanesov-figurate-numbers-1967.full.md` — the DOI,
  author, pages, and free-download link.
- **The article PDF is NOT readable in this workspace**: the freeshare
  download (`/shop/en/publication/transaction/download/product/96317`)
  parses as PDF with no extractable text layer — a 1967 scanned Russian
  article without OCR. The body cannot be read by `download_document`.

## What the (2,3) problem is, and what is attested

- **Result (attested by two independent held full texts)**: the Diophantine
  equation C(x,3) = C(y,2) (triangular = tetrahedral numbers) has exactly five
  positive-integer solutions: (x,y) = (3,2), (5,5), (10,16), (22,56), (36,120).
  - Kiss 1988 (Fibonacci Quart. 26(2) 127–130, full text held): "Avanesov proved
    that this holds only in the cases (x;y) = (3;2), (5;5), (10;16), (22;56),
    and (36;120)", and cites this Acta Arith. paper as [2].
  - GRKTU 2020 (arXiv:1904.11369, full text held): "In 1966, Avanesov [1]
    found all integral solutions of equation (1) with (k,l)=(2,3)."
- **Arithmetic re-verified this run**:
  C(5,3)=10=C(5,2); C(10,3)=120=C(16,2); C(22,3)=1540=C(56,2);
  C(36,3)=7140=C(120,2); (3,2) degenerate row. The values 120, 1540, 7140 are
  three of the six N=6 witnesses — the list is the check oracle any (2,3)
  computation (e.g. the Matveev-2000 effective constant task) must reproduce.

## Bearing

- The five-pair list is **attested, not read from the primary** (primary body
  unreadable here). Treat the list as sourced-through-two-full-texts
  (Kiss + GRKTU), arithmetic checked, primary citation now precise. If a later
  run needs the primary body itself, obtain an OCR'd copy from another
  archive; do not re-download the IMPAN scan expecting a text layer.

```claim
id: avanesov-1967-cx3-cy2-complete
statement: Avanesov 1967 (Acta Arith. 12, 409-420; primary PDF unreadable -
  scanned, no text layer) solved the triangular=tetrahedral equation
  C(x,3)=C(y,2): all positive integer solutions are (x,y)=(3,2),(5,5),(10,16),
  (22,56),(36,120), i.e. the nontrivial equal values 120, 1540, 7140 (=C(16,2),
  C(56,2), C(120,2)) plus degenerate (3,2)=1. Attested by two independent full
  texts held in this library (Kiss 1988 p.127; GRKTU 2020 introduction);
  arithmetic re-verified this run.
hypotheses: none.
holds-here: yes - the (2,3) curve C(x,2)=C(y,3) is genus 1 (the run's closed
  form g(2,3)=1), the only small pair with 3003-type structure; the five-pair
  list is the oracle any (2,3) effective computation must reproduce.
status: attested through two held full texts + arithmetic check; primary body
  not readable this run (recorded, not retried)
bearing: (2,3) complete solution list; constrains any effective height bound
  computation on the (2,3) curve (BACKWARD.md matveev-explicit-2-3 thread) as
  its finite-list check.
anchor: research/summaries/avanesov-figurate-numbers-1967.md
```