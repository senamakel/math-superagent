# Károlyi & Tóth, "Erdős–Szekeres Theorem for Point Sets with Forbidden Subconfigurations" (DCG 2012)

<!-- source: https://link.springer.com/article/10.1007/s00454-012-9424-6 | full text: research/sources/karolyi-toth-2012-ES-forbidden-subconfigurations-springer.full.md -->
Discrete & Computational Geometry 48 (2012) 441–452. Authors: Gyula Károlyi, Géza Tóth.
Full text held (via Springer article page; includes Introduction, Sections 2–4 with all theorems and proofs).
This paper records the **fifth restricted class** this run's library had documented
but could never hold: ES with a *forbidden order type* (subconfiguration).

## The abstraction

ES is re-read adversarially. Fix a non-convex order type 𝒯 (i.e. not all points in
convex position). Define
- **F_𝒯(n)** = least N such that every order type of size ≥ N that does NOT contain 𝒯
  contains n points in convex position.
- **f_𝒯(N)** = the largest n such that every N-point set avoiding 𝒯 contains n convex
  points.

Motivated by the Erdős–Hajnal problem in graph Ramsey theory (Kalai/Solymosi
suggestion): does forbidding a fixed configuration improve the Θ(log N) convex-positions
bound? Károlyi–Solymosi (JCTA 2005) had earlier shown the graph-Ramsey analogue *breaks*
here: there is an order type 𝒯 with F_𝒯(n) > 2^{n−2}, i.e. f_𝒯(N) = Θ(log N) still,
but their construction was non-explicit (via Nešetřil–Valtr). **This paper's novelty is
explicit 𝒯.**

## Main results (all proved in the paper)

**Theorem 1** — For the order types 𝒜 (3 vertices of a triangle + 3 points near the
midpoints of its sides) and 𝒫 (regular pentagon + its center):
> F_𝒜(n) > 2^{n/2−1}  and  F_𝒫(n) > 2^{n/2−1}.

So forbidding these still leaves exponential convex-position freedom. Proved via the
**separation property** + the **twin construction** T_n:

- Lemma 2: T_n (|T_n| = 2^n) contains no 2^n+1 points in convex position.
- **Lemma 3 (the key separation lemma)**: if order type 𝒮 has the *separation
  property* (any two of its points can be separated by a line through two other points),
  then **F_𝒮(2n+1) > 2^n** — because T_n avoids 𝒮. Both 𝒜 and 𝒫 have the separation
  property.

**Erdős–Hajnal property** (F_𝒯 polynomially bounded) — Theorem 4: every order type
ℱ_k (k ≥ 3) has it; Theorem 5: every 𝒢_{k;l,m} (k ≥ 4, l,m ≥ 0, not both 0) has it.
Proofs use Dilworth's theorem + the cups-caps lemma f(a,b)=C(a+b−4,a−2)+1 (Lemma 6),
and the Bárány–Valtr same-type lemma (Lemma 7).

**Triangular convex hull trichotomy** — Theorem 8: Let 𝒯 be an order type of ≥ 4 points
whose convex hull has three vertices:
1. If 𝒯 = ℰ_k (k ≥ 1): F_𝒯(n) is linearly bounded.
2. If 𝒯 = ℱ_k (k ≥ 3): F_𝒯(n) is at least quadratic, at most polynomial.
3. Otherwise: F_𝒯(n) grows exponentially.
No other possibilities. The exponential side uses the RH_n / LH_n sets (binarised
doubling constructions, both twin constructions, hence no 2^n+1 convex points by
Lemma 2) and the six-point Lemma 9 classification.

## Why it matters to this run

- This is the **concrete restricted-class** and structural-counterexample machinery
  GOAL 1 asks for: fixing a forbidden non-convex order type and asking how large a set
  can get before an n-gon is forced. It is exactly the "Ramsey-type, forbidden
  subconfiguration" instrument the problem's method guidance names.
- The **twin construction** T_n is a genuine alternative to the ES lower-bound
  construction: |T_n| = 2^n with no 2^n+1 convex points — a different family of
  near-extremal sets. Relevant to GOAL 2 (what an extremal 2^{n−2}-point set must look
  like): the separation property is a tangible structural obstruction.
- The **separation property** is a concrete local property to test with the run's
  exact oracle on candidate lower-bound sets.

## Claims

```claim
id: karolyi-toth-forbidden-exponential-T1
statement: For the six-point order types 𝒜 (triangle + 3 near-edge interior points)
  and 𝒫 (pentagon + center), F_𝒜(n) > 2^{n/2−1} and F_𝒫(n) > 2^{n/2−1}. For any order
  type 𝒮 with the separation property, F_𝒮(2n+1) > 2^n.
hypotheses: convex hull of 𝒮 has ≥3 vertices and 𝒮 has the separation property (any
  two points separated by a line through two other points).
holds-here: yes — these are realizable planar order types, the same objects the run
  works over; the exponential freedom survives forbidding these non-convex types.
status: asserted-by-source (proved in paper).
bearing: restricted-class instrument (GOAL 1); separation property is a local
  obstruction to test on candidate extremal sets (GOAL 2).
anchor: research/summaries/karolyi-toth-2012-ES-forbidden-subconfigurations-springer.md
```

```claim
id: karolyi-toth-triangular-trichotomy-T8
statement: For an order type 𝒯 of ≥4 points with a 3-vertex convex hull, F_𝒯(n) is
  (i) linear iff 𝒯=ℰ_k, (ii) quadratic-to-polynomial iff 𝒯=ℱ_k (k≥3), (iii) exponential
  otherwise; no other growth is possible.
hypotheses: realizable order type, ≥4 points, convex hull = triangle.
holds-here: yes — realizable planar order types.
status: asserted-by-source.
bearing: a classification of how bad a forbidden subconfig can make the ES bound; the
  phantom phenomenon (linear/quadratic/exponential are the only regimes).
anchor: same file.
```

```claim
id: karolyi-toth-twin-construction
statement: For every n there is a twin-construction set T_n with |T_n|=2^n which
  contains no 2^n+1 points in convex position and whose order type avoids any
  separation-property order type.
hypotheses: realizable via arbitrarily small twins about a previous set; direction of
  the twin line chosen recursively.
holds-here: yes — realizable; an alternative near-extremal family to the ES construction.
status: asserted-by-source (Lemma 2, 3 proved).
bearing: GOAL 2 — a second family whose structure is explicit enough to test conjectures about extremal sets. NOTE THE SCALE: |T_n| = 2^n with no 2^n+1 convex points is near-extremal in the sense of F_𝒮(2n+1) > 2^n (Lemma 3), NOT an n-avoiding set at the ES 2^{n-2} scale; to compare with es_construct at equal N, use T_{n−2} (size 2^{n-2}, no 2^{n-2}+1 convex — still not n-avoiding, so the twin is an alternative near-extremal family, not a second ES-witness family).
anchor: same file.
```

## Relationship to the rest of the library

- Complements the Goaoc–Welzl survey (§1.3.5), which covers the counting side of the
  same forbidden-pattern program; this is the primary constructive side (explicit 𝒯,
  exponential F_𝒯).
- The paywalled companion: Károlyi–Solymosi JCTA 2005 ("Erdős–Szekeres theorem with
  forbidden order types", DOI 10.1016/j.jcta.2005.04.006) whose ScienceDirect PDF is
  403-blocked; its non-explicit F_𝒯(n)>2^{n−2} result is the ancestor of Theorem 1.
  Re-fetch only if a specific statement from it is needed.
