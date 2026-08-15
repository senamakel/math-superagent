NOT EXECUTED — the scholar role in this workspace has no code-execution tool.

This file was drafted as the small-instance oracle for the Hancl-Turek vs
Kimberling reconciliation, but it was never run (no execute tool available to
the scholar). Do NOT treat any of its printed claims as verified output.

The reconciliation it was meant to check is instead established by DIRECT
READING of both full texts (research/sources/hancl-turek-...full.md and
research/sources/kimberling-...full.md), which is an index-level identity and
needs no computation:

  Hancl-Turek (p_{-1}=1, q_{-1}=0, p_0=a_0, q_0=1, eq. 8) odd-n semiconvergents
  (p_n r + p_{n-1})/(q_n r + q_{n-1}), 0 <= r < a_{n+1},  n odd
  ==  Kimberling even-indexed convergents: {p_i/q_i: i even} U
      {(j p_{i+1} + p_i)/(j q_{i+1} + q_i): i even, 1 <= j < a_{i+2}}
  with n = i+1 (odd). Both conventions give p_0/q_0 = a_0/1 and p_{-1}=1,
  q_{-1}=0, so the classified SET is identical: no indexing offset, no
  contradiction. (The test would confirm coin indices 1,3,506,2527,... are a
  subset of these denominators and that HT-denoms == Kim-denoms.)

If an executed confirmation is wanted, have tool_builder run this file.
