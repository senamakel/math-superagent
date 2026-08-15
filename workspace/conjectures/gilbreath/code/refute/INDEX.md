# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_run_check.py` | _(undescribed)_ |
| `cb_dying_pair.p` | _(undescribed)_ |
| `cb_dying_pair_statement.md` | Records the located internal contradiction in the open gap CB-dying-pair: the dying row's b=1 claim contradicts the dying condition (b must be 0). |
| `check_cb_dying_pair.py` | Reference script reproducing the CB-dying-pair reasoning on delete-7/delete-5/delete-11 failing triangles. |
| `g_balance.p` | TPTP numeric fragment of the per-event G-balance claim (two events separated by two erosions), used with find_counterexample. Note: the naive encoding collapses to a trivial domain, so find_counterexample's answer is not a meaningful second route. |
| `g_balance_check.py` | Verifies the strong per-event form of G-balance (j >= d at every (2,4)-event) against blocks_depth1000.json; documents the refutation by counting every j<d event. |
| `g_balance_numeric.p` | _(undescribed)_ |
