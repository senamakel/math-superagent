# Bhat–Cobeli–Zaharescu 2023 — "Filtered rays over iterated absolute differences on layers of integers"

**Source:** https://arxiv.org/abs/2309.03922 · Chaos, Solitons & Fractals 178 (2024) 114315 · doi 10.1016/j.chaos.2023.114315
**Full text:** `research/sources/bhat-cobeli-zaharescu-2023-filtered-rays-iterated-abs-diffs.full.md`
**Downloaded:** this cycle (librarian). The arXiv abstract page was downloaded; the PDF/HTML body is reachable at the links on that page. Claims below are asserted by the abstract/front matter.

## What it establishes (precedent for the `window-range-bound` approach)

The paper studies the iterated-absolute-difference triangle generated from a top row of non-negative integers (in their notation, a *P-G / Pascal-Generalized* triangle). It introduces an extension to a growing hexagonal covering of the plane (a helicoidal surface).

**Left-edge stabilization phenomenon (the part relevant to candidate 1).** As high-order absolute differences are iterated, the left-edge sequence `w = {b_j}` (b_0 = a_0, b_j = d(j)_0) "tend[s] to stabilize, taking at most two values — one possibly zero, the other a nonzero integer — provided the initial growth of u is not too rapid." In the binary case (u takes only 0 or a), the left edge contains only 0 or a. This is a **deterministic** (not random-analogue) restricted-class result about the same operator the run studies: the left edge is a two-valued ({0,a}-type) set under a stated mild-growth hypothesis on the generating sequence.

**Theorem 2** describes an involution-like relationship between the top sequence `u` and the left-edge sequence `w` via the operator `Υ(u) = w` (the western edge / left ray of the generated triangle).

## Hypotheses held here?

The paper's deterministic classes are **ultimately binary sequences with a special header** and, as the abstract says, "many ultimately binary sequences with a special header." The *primes* are NOT ultimately binary — but the *row-1 halved gaps* are not binary either, and the paper is the nearest *deterministic-class* treatment of left-edge stabilisation under a growth hypothesis. It states a phenomenon, not a rate or a regeneration theorem; it does not bound the (2,4)-event rate, does not treat the block/intruder boundary the run tracks, and does not address the primes specifically.

## Bearing on the run's candidate 1 (window-range-bound)

- The paper is the closest held **deterministic** precedent that iterated absolute differences **stabilize the left edge to a two-valued set under a growth hypothesis** — the same shape of claim candidate 1 makes (a conditional theorem under a gap-range hypothesis).
- It is **not** the run's object: the run's question is the *regeneration rate* of the leading {0,2} block (the (2,4)-event arrival rate), and BCZ give no rate, no block/intruder analysis, no bound on time-to-two-valuedness for the primes.
- So BCZ is a *supporting* precedent for the "left edge stabilises under growth" framing, but it does not resolve the event-rate bound in the REQUESTS open row.

## Claims

```claim
id: bcz-2023-left-edge-stabilization
statement: In the iterated-absolute-difference triangle (P-G triangle) of a non-negative integer top row u, the left-edge sequence w stabilizes to at most two values (one zero, one nonzero) provided u does not grow too fast; in the binary-u case (0 or a) the left edge is entirely {0,a}. Theorem 2: an involution between u and w = Υ(u).
hypotheses: u of non-negative integers with moderate growth; the stated classes are ultimately binary sequences (or with a special header).
holds-here: yes for the framing — a deterministic restricted-class two-valued-stabilization statement for the same operator; no for the primes' actual growth (primes not ultimately binary) and no for the event-rate question.
status: asserted by source (abstract/front matter); not checked here.
bearing: supports the conditional-class direction of window-range-bound (left edge → two-valued set under a growth hypothesis); does NOT bound the regeneration rate, which remains the open REQUESTS row.
anchor: research/sources/bhat-cobeli-zaharescu-2023-filtered-rays-iterated-abs-diffs.full.md
```
