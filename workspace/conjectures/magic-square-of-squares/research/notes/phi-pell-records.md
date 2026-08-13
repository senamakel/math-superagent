# Phi Pell-record claims — mirrored from code/out/

The claims below are computed facts from this run's own exact programs.
The evidence is in `code/out/pell_records_established.md` and
`code/out/phi_pell_record.md` plus their captures; this note exists because
`research/CLAIMS.md` is derived from notes under `research/` and claim blocks
in `code/out/` alone are invisible to it.

```claim
id: phi-suprema-are-pell-pairs
statement: For f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2 over primitive m > n >= 1,
  the identity f(P_k, P_{k-1}) = 1 - 1/P_{2k-1}^2 holds for k = 2..59 with
  P_{2k-1} = P_k^2 + P_{k-1}^2, equivalently (m^2+n^2)^2 - 4mn(m^2-n^2) = 1 at
  Pell pairs for k = 2..79. A Pell pair attains the maximum of f over every
  box m <= M tested (M = 20, 100, 500, 1000 and M = 30..1920), and f < 1
  throughout m <= 5000, where the maximum is 1 - 1/6625109^2 at (2378, 985).
  The record denominators grow with ratio tending to 3 + 2*sqrt(2). The
  maximiser is NOT unique: ties occur at M <= 60 and M <= 960, and the record
  is not strictly increasing in M, so any uniqueness claim is false.
hypotheses: primitive pairs m > n >= 1; bounds exactly as stated, nothing
  proved beyond m <= 5000
holds-here: yes, computed in this workspace with exact integer arithmetic
status: checked
bearing: bounds Phi strictly below 1 with an explicit rate and identifies the
  extremal structure as the Pell recurrence. Not an impossibility statement,
  so the witness set does not apply. The stated bounds are part of the result
  and must travel with it
anchor: code/out/pell_records_established.md;
  code/out/verify_pell_records.captured.txt;
  code/out/verify_pell_argmax_unique.captured.txt;
  code/out/prove_pell_record.captured.txt;
  code/out/pell_record_seq.captured.txt
source: operator-computation
```

```claim
id: phi-pell-record
statement: For Pell numbers P_k, the consecutive pair (P_k,P_{k-1}) gives
  f(P_k,P_{k-1}) = 4P_k P_{k-1}(P_k^2-P_{k-1}^2)/(P_k^2+P_{k-1}^2)^2 = 1 - 1/P_{2k-1}^2
  in Phi, already reduced; these are exactly the largest values of f over the
  primitive box (argmax scan to m <= 1920). The record denominators P_{2k-1}
  are OEIS A001653 (2t^2-1 a square), recurrence a(n)=6a(n-1)-a(n-2).
hypotheses: primitive m>n>=1; consecutive Pell pairs
holds-here: yes
status: proved (identity, derivation steps 1-4 exact over k=2..200);
  argmax-over-all-M is verified-numerical to m<=1920 (conjectural in general)
bearing: pins the top of the Phi range-clip; the largest Phi element is always
  1-1/P_{2k-1}^2, so the room below 1 in the additive-chain clip q1+q2<1 is
  quantified by odd-index Pell reciprocals; does NOT settle the no-triple
  conjecture (a triple, if one exists, could still involve smaller q's)
anchor: code/out/phi_pell_record.md;
  code/out/prove_pell_record.py;
  code/out/verify_pell_records.py;
  research/summaries/oeis_a001653.md
falsifier: a primitive pair (m,n) with (m^2+n^2)^2 - 4mn(m^2-n^2) != 1 whose f
  exceeds the consecutive-Pell record for its m-band (scanned none through
  m <= 1920)
```