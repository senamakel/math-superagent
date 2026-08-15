# MathOverflow — "Is there any progress toward solving Gilbreath's conjecture?"

<!-- source: https://mathoverflow.net/questions/34669/is-there-any-progress-toward-solving-gilbreaths-conjecture -->

Canonical MathOverflow "what is known" thread (question 2010, two answers 2010 & 2024,
last activity 2024). Expect no new mathematics; the payload is **which routes
practitioners consider dead and why**, and the independent confirmation that the
run's already-refuted dead routes and its open obstruction are the ones specialists
actually see. Digest is below; full text at
`research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md`.

## What the thread establishes

**Answer 1 — Gjergji Zaimi (Aug 2010).** No published progress except Odlyzko's
numeric verification ("too distant from the rest of mathematics" to be attacked).
Quotes Erdős on the conjecture: *"true but it would be 200 years before anyone
could prove it"* — "I find Erdős's conjecture more interesting than Gilbreath's
conjecture." The 2010-era view holds the result is probably unrelated to primality
and true for "any sequence of appropriate growth rate" — the general-class framing
that problem.md adopts.

**Answer 2 — Terry Tao (Mar 2024).** The only theoretical progress toward the
conjecture is **Chase 2024, *A random analogue of Gilbreath's conjecture*** (Math.
Ann. 388, doi 10.1007/s00208-023-02579-w — already held). Tao's sketch of the proof
mechanism is the valuable nugget:

- Model prime gaps `p_{n+1}-p_n` (beyond the first gap 1) as even, uniform in
  `[2, 2f(n)]`, independently, `f` slowly growing. Chase proves the analogue
  almost surely when `f(n) ≪ (1/100) loglog n / logloglog n`. (Cramér's model,
  by comparison, is ~ `f(n)=log n` with exponential distribution.)
- Proof idea: the **maximum of the row is non-increasing** under the difference
  map, so the only way to get stuck above level `2` is a very long block consisting
  only of `0` and `2d` (for fixed `2d > 2`). For **even `d`** this is ruled out with
  high probability using **differences mod 4** (tractable). For **odd `d`** one works
  harder: a Cauchy–Schwarz argument to force a `0` to occur with reasonably large
  frequency at every row, which makes long `{0, 2d}`-blocks unlikely (the row before
  the block's first appearance would be a long block with no `0`s at all). Tao also
  confirms Proth's claimed proof was a **misreading, since retracted** by its originator.
- Tao's caveat: the uniform-growth-rate analogue is "not yet a fully satisfactory
  heuristic justification towards the conjecture (on the level of ... the twin prime
  conjecture based on Cramér type models), but a good first step."

## Comments (load-bearing small facts)

- **Gerry Myerson:** Odlyzko 1993 Math. Comp. 61 373–380 (MR 93k:11119); the
  conjecture is **problem A10 in Guy, *Unsolved Problems In Number Theory***; Proth
  1878 "claimed to have proved it"; Odlyzko discusses the suggestion that the result
  holds for "any sequence consisting of 2 and odd numbers ... which doesn't increase too
  fast, or have too large gaps"; **"Math Reviews contains no citations of Odlyzko's
  paper"** — independently supports the run's `block-growth-literature-not-covered`
  finding that no one studied block-length growth after Odlyzko.
- **Srilakshmi (2012, the naive Pascal-triangle route):** started by observing row k
  is the signed (k−1)-th forward difference `(n−1)C0·p_n − (n−1)C1·p_{n−1} + ...`,
  and trying to prove it equals 1 — "**then i realised that i forgot about the
  absolute values of the differences**." This is *independently* the run's refuted
  `fwd-diff-identity` (A_k(i) = |signed forward difference| is FALSE on the primes
  from (k,i)=(3,2)). A specialist hit the same dead end in 2012 that this run refuted.
- **tdnoe:** OEIS **A080839** counts how many increasing sequences have the Gilbreath
  property; "doesn't make the primes seem that special" (again the general-class view).

## What this means for the run

- **Confirms the run's dead routes.** The forward-difference/signed-Pascal
  linearization (Srilakshmi's exactly, this run's `fwd-diff-identity-refuted`) and the
  "pure gap-bound general class" (Zaimi's growth-rate remark is the *question*, not an
  answer — Eppstein refutes it) are the routes practitioners consider dead, matching
  the run's own refutations.
- **Confirms the open obstruction is the one everywhere.** Tao's "stuck on a long
  `{0, 2d}` block" is precisely the CHT Theorem 1.6 obstruction (long 0-blocks / long
  shallow `{0,d}`-blocks) that is the run's regeneration problem. The mod-4 control of
  even-d blocks is exactly CHT Lemma 3.10 / Odlyzko eq. 201 (held, and the run proved
  mod 4 is the lift ceiling — `mod4-pascal-invariant` refuted for the exact value).
- **No named dead route beyond what the library records.** The thread names no
  approach "nobody wrote a paper about" that is not already closed in
  research/APPROACHES.md. The fetch-and-close target is satisfied: nothing here
  contradicts the library, and the existing dead-end records are independently confirmed.

```claim
id: mo-thread-practitioner-confirms-fwd-diff-dead-route
statement: A 2012 MathOverflow comment (Srilakshmi) independently hit the run's refuted dead route: trying to prove the Gilbreath triangle's entries are the signed forward differences of the primes, and abandoning it on "I forgot about the absolute values of the differences". This is the same fwd-diff-identity that this run disproved (first violation at (k,i)=(3,2)).
hypotheses: none (a historical claim about a practitioner's attempted route).
holds-here: yes
status: asserted-by-source (the comment itself; the mathematical refutation is this run's checked claim fwd-diff-identity-refuted)
bearing: independent confirmation that the signed-forward-difference linearization is a known dead route, already recorded.
anchor: research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md
```

```claim
id: mo-thread-tao-chase-cannot-be-general-class-proof
statement: Tao's 2024 MO answer characterises Chase 2024 as the only theoretical progress, establishes its modest scope (f(n) ≪ (1/100) loglog n/logloglog n, the Cramér analogue needs f ~ log n), and states the obstruction: the row maximum is non-increasing, so one is stuck only if a very long {0,2d}-block forms - ruled out for even d by differences mod 4, harder for odd d. Nothing here is (or claims to be) a proof for the primes.
hypotheses: none; a sourced statement of the state of the art (2024).
holds-here: yes
status: asserted-by-source (Tao's answer; the underlying Chase result is held and proved)
bearing: independently confirms this run's finding (block-growth-literature-not-covered) that no work after Odlyzko studies block-length growth for the primes, and matches the CHT 2026 {0,d}-block obstruction as the open regeneration content.
anchor: research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md
```

```claim
id: mo-thread-proth-misreading-retraction-confirmed
statement: Tao's MO answer independently confirms the Proth 1878 "proof" was a misreading of the text, "since retracted by its originator" - matching the run's held claim proth-myth-retracted (nothing to locate an error in beyond the retraction itself).
hypotheses: none.
holds-here: yes
status: asserted-by-source
bearing: closes off "locate the error in Proth's proof" as a partial-result direction; the corrected result is the retraction.
anchor: research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md
```

```claim
id: mo-thread-no-new-dead-route
statement: The canonical MO "what is known" thread (answers 2010, 2024) names no approach "nobody wrote a paper about" beyond what research/APPROACHES.md already records as refuted or spent; its general-class framing and {0,2d}-block obstruction duplicate the run's own records. Fetch-and-close target satisfied with no new mathematics.
hypotheses: none.
holds-here: yes
status: asserted-by-source (librarian judgement, not mathematics)
bearing: closes REQUESTS.md's named fetch (Directive 47); confirms the library's dead-end records are the ones specialists actually see.
anchor: research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md
```
