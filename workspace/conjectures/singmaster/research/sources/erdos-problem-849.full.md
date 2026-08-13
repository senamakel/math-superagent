<!-- source: https://www.erdosproblems.com/849 | converted from HTML | accessed 2026-08-13 -->

# Erdős Problem #849 — Singmaster's conjecture (problem database entry)

Maintained by Thomas F. Bloom (erdosproblems.com). Status: **OPEN** — "cannot be
resolved with a finite computation."

## Statement (strong form)

> Is it true that, for every integer t >= 1, there is some integer a such that
> C(n,k) = a (with 1 <= k <= n/2) has exactly t solutions?

Notes from the entry:

- Erdős [Er96b] credits this problem to himself and Gordon "many years ago", but
  it is more commonly known as **Singmaster's conjecture**.
- For t = 3 one could take a = 120; for t = 4 one could take a = 3003.
- **There are no known examples for t >= 5.**
- Both Erdős and Singmaster believed the answer to the question is no, and in
  fact that there exists an **absolute upper bound** on the number of solutions.

## Known progress (as recorded by the entry)

Matomäki, Radziwiłł, Shao, Tao, and Teräväinen [MRSTT22] proved that there are
always at most two solutions if k is restricted to
k >= exp((log n)^{2/3 + epsilon}), assuming a is sufficiently large depending
on epsilon > 0. (This is the interior theorem, arXiv:2106.03335.)

## Reference

[Er96b] P. Erdős, "Some problems I presented or planned to present in my short
talk", in *Analytic Number Theory Vol. 1* (Allerton Park, IL, 1995) (1996),
333–335.

## External data (from the erdosproblems database)

- Formalised statement: yes — google-deepmind/formal-conjectures
  `FormalConjectures/ErdosProblems/849.lean` (stub with sorry).
- Related OEIS sequences: A003016, A003015, A059233, A098565, A090162, A180058,
  A182237.
- 0 comments, 0 claimed proofs on this problem (as of access date).

## Recommended citation (from the site)

T. F. Bloom, Erdős Problem #849, https://www.erdosproblems.com/849, accessed
2026-08-13.

---

## Convention note (this run, not the source)

The strong form counts **solutions (n,k) with 1 <= k <= n/2** — the half-triangle
convention. Under it: 120 has exactly 3 solutions ((120,1), (16,2), (10,3));
3003 has exactly 4 ((3003,1), (78,2), (15,5), (14,6)). This matches this run's
both-mirrors-plus-trivial convention exactly: N(a) = 2×(half-triangle count).
A uniform bound B in the full convention is a bound B/2 in the half-triangle
convention, so "no known examples for t >= 5" is the same fact as "no known
N(a) >= 10".