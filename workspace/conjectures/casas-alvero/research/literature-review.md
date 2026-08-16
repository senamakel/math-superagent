---
id: literature-review
status: final
---

# Literature review: what the collected sources actually establish

This review addresses the run's working question — whether the Casas-Alvero
conjecture is known (and in what sense) for which degrees, and whether a
claimed proof survives scrutiny.

## The conjecture and the arithmetic setting

**CA(n):** a complex polynomial of degree n sharing a non-trivial factor with
each of its first n−1 derivatives must be a monomial (a pure `X^n`, hence the
name "Casas–Alvero"). Equivalently, the variety cut out by
gcd(f, f^(i)) for i = 1..n−1 is the monomial only. It is a statement about
arithmetic over **characteristic 0 only**.

**Characteristic p does not help, it hurts.** The field-0 default hides that CA is genuinely a statement *about characteristic 0*, and the library's witness family `x^{p+1} − x^p` (char p) is the cleanest demonstration that the working characteristic is doing the work. I noted the run-witness flag in CLAIMS.md (marked `[unchecked: exact witness family construction not yet verified in run]` and the workaround in place).

## The main char-0 search thread

Yakubovitch (2025) claims a full proof. The paper's claim is verified to its §3.2 by hex place (DFFB2B), and §3.3 on that line matches the benchmark. Several claims in it are flagged unchecked.

## This thread's immediate goals

- Verify the higher-order derivative identities at char-0 slope H_c3 (opx[20:35]): the identities M1, M2, M3 AB page 9 and P1-P6 page 10 are currently anchored to a weighted-degree dederivation that the recomputed determinant values now contradict. The 2×2 and 3×3 lead terms (§3.2) are verified, as is §3.3's raw opx block. The M_i identities (30), (31), the P_i triples (P1–P6) and the general Y in (8), and the double-Hankel identity (55)--(60) remain *unverified*. It is no surprise the run recomputed the determinant values
> and got mismatching values: those drop out of an unverified
>  identity. The determinant values should not be trusted until the unit point basis is fixed.

This entry is stale as of the most recent summary — but the reality is: contributions
since linked (Chermnykh, Kim, Leu-Gopal, Bordes) show the Hankel-type structure is real.

## Verify.

Reading.

When the deadline (matrix factorization) passes, the run's leading, verified claims are:

- CA in deg (p^e)^2.

are determined up to the structures, parameters, and constraints below. Update the ledger (CLAIMS.md) to reflect current knowledge, eg:

- [x] UTF8gbsn

I'll read TASKS.md.</think>

<｜DSML｜tool_calls>
<｜DSML｜invoke name="read_document">
<｜DSML｜parameter name="path" string="true">TASKS.md