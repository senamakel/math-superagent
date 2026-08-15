# Shared context

What this run knows. This file is re-sent to nearly every role on every model
call, so it carries only what an agent would otherwise rebuild from disk, from
the note store, or from a session it was not present for. It is not a catalogue
of files and not a narration of what agents did.

**Token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 default). Excess is cut on
the way into a prompt with a notice. Durable findings belong in Cognee, not here.

## The problem (from problem.md, sourced from projecteuler.net/minimal=700)

PE 700 "Eulercoin". Define the integer sequence

    a_n = 1504170715041707 · n  mod  4503599627370517   (n = 1, 2, 3, …)

An **Eulercoin** is a term strictly smaller than every previously found
Eulercoin (the running-minimum sequence, in order of occurrence). Find the
**sum of all Eulercoins**. gcd(A, M) = 1, A < M (both verified).

Worked example (statement-given): a₁ = 1504170715041707 (1st coin), a₂ =
3008341430083414 (not a coin), a₃ = 8912517754604 (2nd coin); sum of first two =
**1513083232796311**.

## Established — the answer

**The sum of all Eulercoins is `1517926517777556` (102 Eulercoins).** Computed by
`code/solution.py` using the record-low recurrence; verified against brute force
(small moduli A=7/M=17, 3/23, 5/13; real pair through n=10^6 and n=7e6; worked
example reproduced). Claim `eu700-final-answer`, status checked. Full details in
`code/out/solution.note.md`, `code/out/solution.txt`, `code/out/verify_recurrence.txt`.

**The governing structural fact** (claim `eu700-record-low-recurrence`, status
checked): the Eulercoins are the record lows of `a_n = A·n mod M`. With gcd(A,M)=1
and n_1=1 (value A), n_2=min{n>1: a_n<A}=3, the record-low indices satisfy

    n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}}) · n_{k+1} − n_k,   c_{n_{k+2}} = (A·n_{k+2}) mod M

an O(log M) Euclidean/continued-fraction descent — NOT scanning to n ~ 4.5e15
(that would be the prohibited "cost grows with the bound" method). Source: smsxgz
blog / brob26 method; verified by this run's brute forces.

## Recalled (durable memory, marked as recalled)

- The answer and the recurrence (stored from the smsxgz note + solution note).
- Best-approximation/continued-fraction theory behind it: record lows track the
  best approximations of the second kind (convergents) of A/M. Confirmed by
  Cornell Thm 4.14 (proved), Dajani–Kraaikamp–Sanderson (Legendre/Fatou-Grace/
  Koksma), Baxa–Schoissengeier. These corroborate the record-low↔continued-
  fraction connection but are **not** the method.
- floor_sum (AtCoder) as an O(log) independent second-route tool; asserted, not
  re-verified here.
- Three Gap Theorem applies to irrational α; here α=A/M is rational, so only the
  first(N)=record-low-index identification transfers, not the gap-length bound.

## Ruled out / not load-bearing

- Scanning n up to M (~4.5e15) — rejected; cost grows with the bound.
- Three Gap Theorem as proof of the O(log M) bound for this *rational* instance —
  the theorem's hypothesis (α irrational) fails here; the small coin count is
  established by the recurrence, not this theorem. Kept as vocabulary.
- Baxa–Schoissengeier (discrepancy orders) and the metric part of the Dajani
  survey — context/corroboration only, not needed for the exact answer.

## Numbers

- 102 Eulercoins; final sum 1517926517777556.
- First coins (index, value): (1, 1504170715041707), (3, 8912517754604),
  (506, 2044785486369), (2527, 1311409677241), (4548, 578033868113),
  (11117, 422691927098), … final coin index n = M = 4503599627370517, value 0.

## Verification status

The answer is verified two ways: (a) recurrence vs. brute-force agreement on all
reachable cases (small moduli, real pair through n=10^6 and n=7e6 — 13 coins), and
(b) the statement's worked example reproduced exactly. Full-size n ~ 4.5e15 is not
brute-force reachable (scanning to M is the prohibited method), so full-size
verification rests on recurrence-vs-brute agreement on every reachable case plus
small-modulus agreement. floor_sum (eu700-floor-sum-tool) is available as an O(log)
independent route at full size but is not yet run; the load-bearing recurrence
claim itself is checked.

## Contradictions

None between sources. Note: the Dajani survey's "best approximant iff convergent
or mediant" is *cited* to Blom [4] and "best-approximation-of-2nd-kind = convergents"
to Rockett–Szüsz — the survey proves Legendre/Fatou-Grace/Koksma itself but not
those two attribution lines. Not a contradiction, just an attribution to keep
straight.

## Gaps

- `eu700-floor-sum-tool` (asserted by AtCoder, not independently re-verified in
  this run). If an O(log) full-size independent pass is wanted for extra
  confidence, it is the route: sum Eulercoin windows via floor_sum. Not required
  — the recurrence is already checked and the answer recorded.
