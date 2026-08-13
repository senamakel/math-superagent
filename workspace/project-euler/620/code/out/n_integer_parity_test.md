# Parity filter of the n_t meshing model is vacuous (checked)

`claim`
id: parity_filter_vacuous_nt_model
statement: In the n_t integer meshing model for PE620 (n_t(d) = [(c-t)*beta +
(s+t)*mu]/pi, valid iff n_p, n_q in Z), the parity filter n_p - n_q == p - q
(mod 2) rejects NO candidate: over all 205 valid-d solutions of the 22 G(20)
tuples, zero violate the parity condition.  Removing the filter leaves every
per-tuple g unchanged and G(20) = 205 either way.
hypotheses: c = s + p + q (all G-sum tuples satisfy this); the model identity
n_p(d) + n_q(d) = c + s holds at every interior d (confirmed to ~1e-13 at
arbitrary d, not only at solutions).
holds-here: yes
status: checked
bearing: the odd-c+s question is moot -- no tuple changes, so the parity
  filter is (a) vacuous, not (b) load-bearing.  This strengthens the
  simplified single-condition view of the model (n_p in Z with the other
  condition automatic), in agreement with the durable note that
  n_p+n_q = c+s for every d.
anchor: code/out/n_integer_parity_test.txt (+ the direct 205-solution parity
  audit in this run's verification command), code/pattern/n_integer_noparity.py
`endclaim`

## Procedure

1. Ran `code/pattern/n_integer_count.py` as-is: byte-identical to
   `code/out/n_integer_model.txt` (g(16,5,5,6)=9, G(16)=9, G(20)=205, all 22
   per-tuple g values).  Confirms the oracle harness still stands.
2. Wrote `code/pattern/n_integer_noparity.py` -- same model, same
   fixed grid (N = 2^20+1), same degenerate-endpoint exclusion, with a
   `use_parity` switch.  Ran all 22 tuples both ways.
3. Separately audited every no-parity solution for filter rejection and for
   the n_p+n_q = s+c identity.

## Results (code/out/n_integer_parity_test.txt)

- g(16,5,5,6): 9 with filter, 9 without.
- Per-tuple G(20): the 22 g values are identical in both runs
  (e.g. g(16,5,5,6)=9, ..., g(20,9,5,6)=12); NO tuple changes.
- G(20) with parity = 205, without parity = 205.
- 14 of the 22 tuples have c+s odd; none of them changed, so the change set
  is NOT the odd-c+s set -- but the question collapses: nothing changes at all.
- 205 solutions audited: 0 parity rejections (well, the filter would have
  rejected none), and n_p+n_q = s+c at every valid d of every tuple
  (min 21 = 16+5, max 29 = 20+9 -- each tuple's own s+c = 2s+p+q).

## Why the filter cannot reject anything (algebra)

The observed identity n_p(d) + n_q(d) = c + s holds for arbitrary interior d
(verified at 11 d-values to ~1e-13; the flagship interval only exists for
d >= d_min ~ 0.1592).  Given c = s + p + q, for any solution with integer
values:

    n_p - n_q = 2 n_p - (c + s)  ≡  c + s  =  2s + p + q  ≡  p + q  ≡  p - q  (mod 2)

so the parity condition is an identity, i.e. option (a) -- vacuous.

## What was searched to try to break it

- All 22 G(20) tuples, both filter settings, N = 2^20+1-point d-grid each
  (the same resolution that reproduced the 9/9/205 oracles).
- Direct check that among the 205 no-parity solutions, none violates the
  parity condition or the sum identity (the only way the filter could matter
  is a candidate with n_p, n_q both near integers while n_p+n_q deviates from
  c+s by >= 0.5; the identity is exact to ~1e-13, excluding that).

## Consequence

The model simplifies: g(c,s,p,q) = #{k in Z : n_p(d_min) < k < n_p(d_max)}
with n_p monotone increasing -- the two-integer condition collapses to the
single condition n_p in Z, consistent with the flagged durable memory and with
`winner_refine.py`'s high-precision verification of the flagship.