# Verification checklist for Girgensohn (2011) — for tool_builder to run

The librarian filed research/trollopedelange.md (and .full.md) and records these sourced claims,
but the librarian has no code-execution tool. Before any formula from this source is quoted
numerically, run this with a quick script (all in plain Python/sympy, no pip needed):

1. ones summatory S(n)=sum_{j=0}^{n-1} popcount(j) must satisfy (for all small n):
   S(2n) = 2S(n) + n
   S(n+p(n)) = S(n) + S(p(n)) + p(n)      [p(n)=largest power of 2 <= n]
   S(n+2p(n)) = S(n) + S(2p(n)) + n
   S(2^e) = e*2^(e-1)
2. Exact Trollope–Delange (formula 35): S(n) = (n/2)log2(p(n)) + p(n)*F(x),
   x=(n-p(n))/p(n), reconstructed via G(n)=(1/p(n))(S(n) - (n/p(n))S(p(n))), F(x(n))=G(n).
   Check it equals S(n) to machine precision for n in 1..100.
3. zero-count S0(n) (with the paper's s^(0)(0):=-1 convention) satisfies the analogous
   recurrence S0(2n) = 2S0(n) + n  (same as ones, per the paper's normalisation), and
   ones+zeros = total_bits + 1 over j=0..n-1 (offset from the s0(0)=-1 convention).
4. Recurrences here must agree with the A000788 / A059015 recurrences already in
   bitcount.md / zerocount.md (same unweighted engine, different presentation).

Do NOT delete this file: it is the hand-off that the numerical claims were actually checked.
