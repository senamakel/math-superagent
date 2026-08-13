# A002827 — Unitary perfect numbers (OEIS page, internal format) — digest

Full text: [[oeis-a002827-internal-format.full]] (OEIS A002827 internal, #76, Jun 28 2026).

## The entry — exact transcription

> `%S 6, 60, 90, 87360, 146361946186458562560000`
>
> `%N Unitary perfect numbers: numbers k such that usigma(k) - k = k.`
>
> `%C d is a unitary divisor of k if gcd(d,k/d)=1; usigma(k) is their sum (A034448).`
> `%C The prime factors of a unitary perfect number (A002827) are the Higgs primes (A057447). - Paul Muljadi, Oct 10 2005`
> `%C It is not known if a(6) exists. - N. J. A. Sloane, Jul 27 2015`
> `%C Frei proved that if there is a unitary perfect number that is not divisible by 3, then it is divisible by 2^m with m >= 144, it has at least 144 distinct odd prime factors, and it is larger than 10^440. - Amiram Eldar, Mar 05 2019`
> `%C Conjecture: Subsequence of A083207 (Zumkeller numbers). Verified for all present terms. - Ivan N. Ianakiev, Jan 20 2020`
> `%C All unitary perfect numbers are even (for a proof see the LeanGenius link). - Peter Luschny, Jun 05 2026`
> `%F If m is a term and omega(m) = k, then m < 2^(2^k) (Goto, 2007). - Amiram Eldar, Jun 06 2020`
> `%e 6 = 2*3. 60 = 2^2*3*5. 90 = 2*3^2*5. 87360 = 2^6*3*5*7*13.`

## What it establishes for this run

- The **five-term witness set** matches the run's oracle exactly (`6, 60, 90,
  87360, 146361946186458562560000`) with `90 = 2·3^2·5` — so the
  Encyclopedia-of-Math "90 = 2·3^3·5" is a typo (contradiction recorded).
- **Paul Muljadi's comment** (Oct 10 2005): every prime factor of a UPN is a
  3-Higgs prime (A057447). This is the bridge to the `H_even` branch: the 3-Higgs
  primes are exactly the allowed prime divisors of `2^m + 1` for `m ∈ H`.
- **Frei's theorem (1978) as OEIS records it:** a UPN not divisible by 3 needs
  `m ≥ 144` (`2^m | n`), ≥ 144 distinct odd prime factors, and `n > 10^440`.
  Primary text not held (REQUESTS row 1 OPEN); load-bearing for "is 3 | n
  forced?".
- **Goto's bound (2007):** `m < 2^(2^k)` where `k = ω(m)` for a UPN `m`.
  Primary paywalled (REQUESTS row 3 OPEN).
- **Links available:** Subbarao's letter to Sloane (Feb 18 1974) and Wall's
  letter to Hagis (Jan 13 1972) are OEIS-hosted scanned PDFs — the likely
  carriers of the orphan "10^102" search bound; not OCR-able by this tool yet.

```claim
id: oeis-a002827-five-terms-and-higgs-comment
statement: OEIS A002827 lists exactly the five UPNs 6, 60, 90, 87360,
  146361946186458562560000 (90 = 2*3^2*5); records that the prime factors of a
  UPN are the Higgs primes (A057447) (Muljadi 2005); records Frei's theorem
  (1978) that a UPN not divisible by 3 has 2^m | n with m >= 144, >= 144
  distinct odd prime factors, and n > 10^440; records Goto's bound m <
  2^(2^k) for omega(m)=k.
hypotheses: OEIS comments are reliable secondary attribution; Frei 1978 and
  Goto 2007 primaries are not held
holds-here: yes (the five terms are the run's witness set; the Higgs comment
  is the bridge to H_even)
status: catalogued
bearing: fixes the witness set, bridges to A057447, and is the sole carrier of
  the Frei m>=144 bound and Goto bound until those primaries are read
anchor: research/sources/oeis-a002827-internal-format.full.md
contradicts: (none) -- the Encyclopedia-of-Math 90-factorization typo
  (2*3^3*5) is a page-content error, not a claim-level contradiction
answers: whether-3-divisibility-is-forced
```


*[excerpt ends; 1633 characters not shown — see `research/sources/oeis-a002827-internal-format.full.md`]*
