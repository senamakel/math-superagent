# PE 351 — sequence structure found by the pattern finder

Data: exact sequences over n = 1..200000 from `code/out/patterns.py`
(H = seq_H.txt, A063985 = seq_A063985.txt, Phi = seq_Phi.txt,
cototient = seq_cototient.txt), plus the stored exact H(10^8).

## What holds exactly over every one of the 200000 stored terms (checked)

```claim
id: pe351-h6a063985-identity
statement: H(n) = 6*A063985(n) = 3n(n+1) - 6*Phi(n) for every n, with
Phi(n) = sum_{k<=n} phi(k) and A063985(n) = sum_{k<=n} (k - phi(k)).
hypotheses: n >= 1.
holds-here: yes — verified by numpy array equality over all n <= 200000 in
code/out/pattern_check.py, and the statement oracles H(5)=30, H(10)=138,
H(1000)=1177848 are reproduced from the stored files.
status: checked (computed identity over the full stored range; catalogued
closed form A216453 = 6*A063985).
bearing: the sequences H, A063985, Phi, cototient are all linked by exact
identities; H carries no information beyond A063985.
anchor: code/out/pattern_check.py
```

```claim
id: pe351-mod12-period4
statement: For every n >= 2, H(n) mod 12 = 6*((n+1)//2 mod 2); equivalently
H(n) mod 12 is periodic with period 4, residues 6,0,0,6 for n = 2,3,4,5 (mod 4).
Derivation: phi(k) is even for all k >= 3, so c(k) = k - phi(k) has
c(1)=0, c(2)=1 and c(k) == k (mod 2) for k >= 3; hence
A063985(n) mod 2 = 1 + floor((n-1)/2) mod 2, and H(n) mod 12 = 6*(A mod 2).
hypotheses: n >= 2.
holds-here: yes — verified over all 2 <= n <= 200000 in
code/out/mod12_independent_check.py by a fresh spf-sieve phi computation
(Route 1), by the parity steps (Route 2), and at the full size:
H(10^8) mod 12 = 0 = 6*((10^8+1)//2 mod 2) (Route 3).
status: checked (verified over the full stored range and at n = 10^8;
the derivation is a proof, the period-4 statement for all n follows
from the parity argument).
bearing: cheap residue prediction; also a consistency check on the final
answer: H(10^8) must be ≡ 0 mod 12.
anchor: code/out/mod12_independent_check.py
```

## What the sequence tools establish (exact over the 40 terms supplied)

- H, A063985, Phi, cototient: no low-degree polynomial fit
  (differences never become constant within 12 levels).
- H, Phi, A063985: no constant-coefficient linear recurrence of order
  <= 8 fits 40 terms (and an earlier exact rank check over 300 terms found
  none of order <= 12). The order-4 recurrence previously found on 8 terms,
  a(n) = (-13/7)a(n-1) + (23/7)a(n-2) + (41/7)a(n-3) + (-46/7)a(n-4),
  is spurious: it predicts H(9) = 222 but H(9) = 102.
- All four are catalogued: H = A216453, A063985 = A063985, Phi = A002088,
  cototient = A051953. So no new sequence was found; the closed forms
  a(n) = 6*(C(n+1,2) - sum phi) and A063985(n) = C(n+1,2) - A002088(n)
  are the catalogued evaluations that make the enumeration unnecessary.

## Subsequence pass (this session, terms extracted from the stored prefixes)

The prior passes ran the sequence tools only on the heads of the full
sequences. This pass extracted and tested the subsequences that were never
examined. Exact tools over the terms supplied; none of the following is a
proof that a pattern continues, and in fact no pattern was found.

- A(2^k), k=0..17: 0,1,4,14,56,204,820,3234,12948,51476,205836,822590,
  3290636,13156918,52626582,210499912,842001490,3367894404.
- H(2^k) = 6·A(2^k): 0,6,24,84,336,1224,4920,19404,77688,308856,1235016,
  4935540,19743816,78941508,315759492,1262999472,5052008940,20207366424.
- A(3^k), k=0..11: 0,2,17,148,1301,11590,104317,938082,8440107,75950324,
  683550231,6151859350.  A(k^2), k=1..20: 0,4,17,56,125,270,471,820,...
- A(2^k·3), k=0..16: 2,9,32,120,464,1850,7298,28980,115888,463126,
  1850990,7401690,29604578,118410200,473623212,1894458998,7577790934.
- A(2^k·5), k=0..15: 5,23,82,330,1274,5074,20128,80582,321488,1285568,
  5139958,20559112,82226576,328911130,1315591226,5262389302.

Results, all exact over the supplied terms:

1. `analyze_sequence` on A(2^k), A(3^k), A(k^2), A(10^k): differences never
   become constant within 11–12 levels — no low-degree polynomial fit.
2. `find_linear_recurrence` (max order 8): no constant-coefficient linear
   recurrence fits A(2^k) (18 terms), H(2^k) (18 terms), A(3^k) (12 terms),
   A(k^2) (20 terms), A(2^k·3) (17 terms), or A(2^k·5) (16 terms).
3. OEIS: H(2^k), A(2^k), A(3^k), A(k^2), A(2^k·3), A(2^k·5) (18/18/12/20/
   17/16 terms) are **not catalogued** — no closed form to look up.
   Exception: **A(10^k) IS catalogued as OEIS A064016 = A063985(10^n)**
   (diagonal of A063985), and its b-file matches the run's computed terms
   exactly for n = 0..8, including A(10^8) = 1960364533634092 (independent
   Chai Wah Wu recursion, `code/out/diag_a064016_check.py`; summary
   `research/summaries/oeis_a064016.md`).
4. Growth: A(2^k·3)/4^k and A(2^k·5)/4^k → 0.19603 = 1/2 − 3/π², the
   known quadratic asymptotics of A(n); not new structure.
5. The mod-12 period-4 law survives inside the subsequences: A(2^k) is odd
   exactly at k=1 (2 mod 4 = 2), even elsewhere; A(3^k) is odd exactly at
   even k >= 2 (3^k mod 4 = 1); A(1)=0 even is the sole n=1 exception.
   Consistent with the law.

**Verdict.** The subsequences carry no exact exploitable structure beyond
the identities already derived (H = 6·A063985, the mod-12 period-4 law, the
prime-power jump dH(p^a) = 6·p^(a-1)). Their ratios only reflect the known
quadratic asymptotics. No new sequence, no new closed form.

## Which regularity is most likely to yield a derivation

The mod-12 period-4 residue pattern (claim pe351-mod12-period4): it is the
only exact periodicity in the data, it is already derived from the
elementary fact that phi(k) is even for k >= 3, and it gives a sanity check
on H(10^8) (must be ≡ 0 mod 12, which it is). The asymptotic
H(n) ~ 3n^2(1 - 6/pi^2) is not an identity and is not offered as one.
