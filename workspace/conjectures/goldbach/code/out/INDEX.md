# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | The convention for this folder: capture a program's output here verbatim, and put a fenced `claim` block (status: checked) in the note beside it so a verified computation reaches derived/CLAIMS.md. |
| `RUNTIME_NOTE_memory_outage.md` | Records that remember_memory/note_scratch were down (server health check timed out); the Chen-prime finding is safe in chen_goldbach_1e8.md. |
| `chen_goldbach_1e6.txt` | Verbatim output of the 10^6 Chen-prime check: no failure, witness (41, 999959), 0.39 s. |
| `chen_goldbach_1e7.txt` | Verbatim output of the 10^7 Chen-prime check: no failure, witness (29, 9999971), 4.60 s. |
| `chen_goldbach_1e8.md` | Claim note beside the 10^8 output: fenced `claim` block (status: checked) recording that no n ≡ 4 mod 6 in [4, 10^8] lacks a Chen-pair representation. |
| `chen_goldbach_1e8.txt` | Verbatim output of the 10^8 Chen-prime check: no failure, witness (29, 99999971), 63.12 s. |
| `chen_goldbach_1e8_module.err` | Empty stderr from the module-form rerun (exit 0). |
| `chen_goldbach_1e8_module.txt` | Module-form rerun of the 10^8 check after restructuring into code/chen_goldbach/: identical output, 63.38 s. Confirms restructure did not change the computation. |
| `chen_goldbach_all_1e7.txt` | All-even Chen-pair sweep, bound 10^7: first failure 302, 4-mod-6 class none, 4.29 s. Verbatim output. |
| `chen_goldbach_all_1e8.txt` | All-even Chen-pair sweep, bound 10^8: first failure 302, 4-mod-6 class none, 63.98 s. Verbatim output. |
| `chen_goldbach_all_1e9.md` | Claim note beside the all-even outputs: fenced `claim` block (status: checked) — first all-even failure is 302 (n ≡ 2 mod 6), 4-mod-6 class clean through 10^9, 27 failures ≤ 10^6 all ≡ 2 mod 6. |
| `chen_goldbach_all_1e9.txt` | All-even Chen-pair sweep, bound 10^9: first failure 302, 4-mod-6 class none, 800.59 s. Verbatim output. |
| `chen_goldbach_all_census_1e6.txt` | No-stop all-even census ≤ 10^6: 27 failures (all ≡ 2 mod 6), hardest-n diagnostics (largest smallest-witness p = 99991 at n = 884342). |
| `chen_goldbach_all_oracle_check.txt` | Independent trial-division oracle: Chen flags match sieve for p ≤ 200; the oracle's own all-even scan finds first failure 302 with no other failures ≤ 302. |
| `chen_goldbach_all_sympy_crosscheck.txt` | Second-route verification: sympy direct factorisation reproduces the exact same 27-failure list ≤ 10^5 as the sieve method. |
| `chen_goldbach_oracle_check.txt` | Independent trial-division oracle cross-check vs the sieve's Chen flags for every p ≤ 200, plus the Chen primes up to 50. |
| `chen_goldbach_sanity.txt` | Sanity run: ordinary Goldbach reproduced for every even n in [4, 1000], hand classifications p=2,3,7 pass. |
| `commands.log` | Command log of earlier runs in this workspace (import discovery, oracle runs, sympy cross-route). |
| `err.txt` | Scratch error capture from an earlier run; no longer needed. |
| `extend_sp_10m.err` | _(undescribed)_ |
| `extend_sp_10m.txt` | _(undescribed)_ |
| `extend_sp_50000.err` | _(undescribed)_ |
| `extend_sp_50000.txt` | _(undescribed)_ |
| `extend_sp_fast_200000.err` | _(undescribed)_ |
| `extend_sp_fast_200000.txt` | _(undescribed)_ |
| `extend_sp_vec_2000000.err` | _(undescribed)_ |
| `extend_sp_vec_2000000.txt` | _(undescribed)_ |
| `oracle-brute-worked-examples.md` | Captured output of the brute.py oracle run on the worked examples, verbatim, plus the checked claim block (status: checked) recording that all three problem.md examples matched and the hand-counted 4..50 table was reproduced, with the sympy cross-route result. |
| `oracle_goldbach_cycle_2026-08-18.md` | Recorded output of the required small-instance Goldbach oracle and naive/fast cross-check. |
| `oracle_goldbach_reference.md` | Recorded small-instance oracle specification, worked-example reproduction target, and chosen analytic-number-theory method. |
| `run_refute_oracles.py` | _(undescribed)_ |
| `seq_gn.txt` | Unlabeled numeric dump (998 lines) from an earlier run's exploration; no statement recorded, carries no established result. |
| `seq_p_sorted.txt` | Unlabeled numeric dump (17 lines) from an earlier run's exploration; no statement recorded, carries no established result. |
| `seq_rn.txt` | Unlabeled numeric dump (998 lines) from an earlier run's exploration; no statement recorded, carries no established result. |
| `seq_rn_50000.txt` | _(undescribed)_ |
| `seq_sp.txt` | Unlabeled numeric dump (17 lines) from an earlier run's exploration; no statement recorded, carries no established result. |
| `seq_sp_50000.txt` | _(undescribed)_ |
| `seq_sp_eff_200000.txt` | _(undescribed)_ |
| `seq_sp_vec_10000000.txt` | _(undescribed)_ |
| `seq_sp_vec_2000000.txt` | _(undescribed)_ |
| `slices.txt` | _(undescribed)_ |
