# Searching for and characterizing abundancy outlaws — Weiner & Holdener (poster)

Source: https://biology.kenyon.edu/HHMI/posters_2014/weinerz.pdf — `[[weiner_searching_outlaws.full]]`

## What it establishes

- Review of the abundancy index I(n)=σ(n)/n, perfect = 2, multiperfect = integers; abundant/deficient split.
- **Odd-perfect equivalence (Theorem, traced to Holdener 2006).** An odd perfect number exists iff there are p,n,α, p≡α≡1 mod 4, p prime ∤ n, with I(n) = 2p^α(p−1)/(p^{α+1}−1). In particular if any n has I(n)=5/3, then 5n is an odd perfect number.
- **Erdős outlaw criterion:** if (k,m)=1 and m<k<σ(m), then k/m is an outlaw (the same Property 2.3, here attributed to Erdős).
- Search technique for outlaws of the form (σ(N)+t)/N with positive t: three theorems giving t-bounds (e.g. t < σ(m)/p for odd α≥1 under a prime q|p+1 condition) under which (σ(p^α m)+t)/p^α m is an outlaw.

## Does not help this problem (and why)

Like the companion JIS paper, this is about showing rationals are *outlaws* (fail to be abundancies). PE 241 needs the *indices* that ARE attained (k+1/2), and the parity fact is already available more directly. The 5/3 discussion is about the potential odd-perfect connection, not about enumerating k+1/2. Nothing here bounds or enumerates candidates for the run; it is the wrong direction. Record as a dead-end source so nobody re-reads it for the method.

## What it confirms

Re-statement of the parity/denominator-divides fact (any I(n)=r/s in lowest terms has s|n), corroborating [[holdener_stanton_outlaws]] Property 2.2, which is the piece the run uses.

```claim
id: weiner-outlaw-no-bound
statement: The abundancy-outlaw search techniques (odd-perfect equivalence, t-bounds for (sigma(N)+t)/N) classify rationals that fail to be abundancy indices; they do not enumerate n attaining a given k+1/2.
hypotheses: none needed beyond the classification direction
holds-here: no
status: sourced
bearing: not usable for the run's enumeration; parity corroboration only
anchor: research/sources/weiner_searching_outlaws.full.md
```
