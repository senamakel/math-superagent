<!-- source: https://www.renyi.hu/~p_erdos/1979-22.pdf | Erdős, "Some unconventional problems in number theory", Mathematics Magazine 52(2) (1979) -->

# Erdős 1979, "Some unconventional problems in number theory" — the primary statement

Source: Mathematics Magazine 52, no. 2 (March 1979), pp. 67–70. Full text: `research/sources/erdos-1979-unconventional-problems-number-theory.full.md`. (The rènyi.hu/~p_erdos archive scan is the Mathematics-Magazine version.)

## The conjecture, stated in Erdős's own words

From the **Factorial Powers** section (lines ~35):

> I conjecture that for **k > 8, 2^k is not the sum of distinct powers of 3.** (However, 2^8 = 256 = 3^5 + 3^2 + 3 + 1.) This conjecture would imply that for k > 9, (2^2k ... ) ≡ ... but as far as I see there is **no method at our disposal to attack this conjecture.**

This is the primary fixing of the statement: "2^k is not a sum of distinct powers of 3 for k > 8"; "sum of distinct powers of 3" ⟺ base-3 expansion uses only digits 0 and 1 (no digit 2). Erdős himself flags it as hopeless with current methods ("no method at our disposal").

## Context in the paper

It sits in the "Factorial Powers" / binomial-coefficient theme: Erdős is discussing `(2n choose n)` divisibility, notes `(2n choose n) ≡ 0 (mod 4)` except when n is a power of 2, and for the missing 2-part case the goal is to show `(2^2k choose 2^k)` is divisible by the square of an odd prime — which connects to the digit-2-in-ternary reformulation (via the Kummer carry reformulation the run already holds: no digit 2 in (2^k)_3 ⟺ the self-sum of 2^k has no carries). The conjecture here is stated in the "sum of distinct powers of 3" form.

Also appears: Erdős remarks "there is no doubt that for n > n_0(k,a), (2n choose n) ≡ 0 (mod p^a) for some p > k", and "for p > 2, ... there is a good chance that (171 choose 342?) is the greatest (2n) with this property", i.e. for n > 171, (2n choose n) is perhaps divisible by the square of an odd prime.

## Relevance

Holds the **primary statement and author's own assessment**. The conjecture is confirmed as: (a) from 1979, (b) about "sum of distinct powers of 3" (digit-2-free ternary), (c) with exceptions {2^0, 2^2, 2^8} implicit (2^8 given explicitly as 256 = 3^5+3^2+3+1), (d) believed true but with "no method at our disposal" per Erdős.

## Status

Primary source, on disk. This is the origin paper the whole library's statements trace to; every later claim (Dimitrov–Howe, Saye, Lagarias, Narkiewicz) cites this or its companions. The run now holds the canonical fixing statement directly rather than via surveys.

```claim
id: ERDOS-1979-PRIMARY-STATEMENT
statement: (Erdős, Math. Mag. 52(2) 1979) 'I conjecture that for k > 8, 2^k is
  not the sum of distinct powers of 3. (However, 2^8 = 256 = 3^5+3^2+3+1.) ...
  there is no method at our disposal to attack this conjecture.' This is the
  primary statement of the ternary conjecture: 'sum of distinct powers of 3'
  iff base-3 expansion has no digit 2.
hypotheses: k > 8 (a positive integer exponent, k the exponent of 2).
holds-here: yes — this is precisely the conjecture the run is attacking, stated
  in Erdős's own words with the 2^8 witness.
status: sourced (primary; Math. Mag. 52(2), 1979)
bearing: fixes the statement and the author's own assessment that no known
  method reaches it. The k>8 and the three witnesses {0,2,8} come from here.
  Anchor of the whole claim tree — the run now holds the origin directly.
anchor: research/summaries/erdos-1979-unconventional-problems-number-theory.md
```
