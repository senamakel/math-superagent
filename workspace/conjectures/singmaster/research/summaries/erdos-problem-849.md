# Erdős Problem #849 — canonical problem-collection entry for Singmaster

Source: https://www.erdosproblems.com/849 (T. F. Bloom's Erdős problem database),
accessed 2026-08-13. Full text: `research/sources/erdos-problem-849.full.md`.

## What it establishes

The canonical problem-database statement, in its **strong form**:

> Is it true that for every integer t >= 1 there is an a with C(n,k)=a
> (1 <= k <= n/2) having exactly t solutions?

- Attribution: Erdős credits himself and Gordon "many years ago" [Er96b]; known
  as Singmaster's conjecture, believed by both to have an absolute upper bound
  (answer "no").
- t = 3 achieved by a = 120; t = 4 by a = 3003; **no known examples for t >= 5**
  (i.e. no known N(a) >= 10 in the both-mirrors convention).
- Records the MRSTT22 interior result (at most two solutions for
  k >= exp(log^{2/3+eps} n), a large).
- Status: OPEN, "cannot be resolved with a finite computation"; 0 comments,
  0 claimed proofs as of access.
- Formalised-statement stub exists (google-deepmind/formal-conjectures
  849.lean, with sorry).

## Convention correspondence (computed by this run, consistent with witnesses.json)

Half-triangle count × 2 = full-convention N(a). 120 → 3 half-triangle solutions
((120,1),(16,2),(10,3)) — matches N(120)=6 full. 3003 → 4 half-triangle
((3003,1),(78,2),(15,5),(14,6)) — matches N(3003)=8 full. So "t >= 5 unknown"
↔ "N(a) >= 10 unknown".

## Bearing for this run

Fixes the problem's canonical phrasing and history; corroborates the witness
frame (120, 3003) from an independent encyclopedic tier (problem database), and
the "no known t>=5" status parallel to "B=8 is the record". No new bound; the
MRSTT entry is a restatement of the primary this run holds.

```claim
id: canon-erdoos-849-statement
statement: Erdős Problem 849 (erdosproblems.com/849, Bloom; Er96b = Erdős 1996,
  "Some problems I presented or planned to present in my short talk", Analytic
  Number Theory Vol. 1, 333-335): strong form asks whether every t >= 1 occurs
  as the number of solutions of C(n,k)=a with 1<=k<=n/2; Erdős+Singmaster
  believed an absolute upper bound exists (answer no); t=3 achieved by a=120,
  t=4 by a=3003, no known examples for t>=5; status OPEN, not resolvable by
  finite computation; MRSTT22 (interior theorem) recorded as the only cited
  progress.
hypotheses: half-triangle convention 1<=k<=n/2; a integer.
holds-here: yes — this is the problem this run attacks, in its canonical
  problem-database form.
status: sourced (problem-collection tier; primary history via [Er96b], not
  itself downloaded)
bearing: corroborates the witness frame (120, 3003) and the "no known t>=5"
  record from an independent encyclopedic tier; fixes the strong-form phrasing
  and attribution.
anchor: research/summaries/erdos-problem-849.md
```

```claim
id: half-triangle-convention-consistency
statement: This run's both-mirrors-plus-trivial convention N(a) equals 2 times
  the half-triangle solution count ((n,k) with 1<=k<=n/2). Checked on the
  canonical exemplars: N(120)=6 <-> {(120,1),(16,2),(10,3)}, N(3003)=8 <->
  {(3003,1),(78,2),(15,5),(14,6)}. Hence "no known t>=5" (Erdős 849) is the
  same fact as "no known N(a)>=10" in this run's convention.
hypotheses: k <= n/2 strict count; all four witness pairs have k < n/2 so no
  centre-column ambiguity.
holds-here: yes — 120 and 3003 verified in code/out/witnesses.json.
status: verified-numerically (matches witnesses.json and the source's exemplars)
bearing: pins the convention translation so a read of the source cannot be
  mis-counted; a B>=10 finding would contradict the source's "no known t>=5".
anchor: research/summaries/erdos-problem-849.md
```