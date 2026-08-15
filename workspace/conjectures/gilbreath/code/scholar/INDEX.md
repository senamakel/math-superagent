# Index — code/scholar

Scholar's verification scripts. These are prior-cycle artifacts whose captures
live under `code/out/*.captured.txt`; the advisory-cycle handoff is called out.

| File | Purpose |
| --- | --- |
| `verify_countermodel_only.py` | **THIS CYCLE.** Numeric restatement (handoff for tool_builder) of the linchpin claim `g-supply-switch-count-not-one-point`: balanced one-point mod-4 marginals do not pin the consecutive-pair switch count, since the ordering [1,…,1,3,…,3] is consistent with them and achieves exactly one switch. Logical proof-by-inspection; run is for the record. Capture: `code/out/verify_two_point_countermodel.captured.txt` (run by tool_builder). |
| `run_verify_countermodel.py` | Thin runner for the above (no executable logic). |
| `exec_verify.sh`, `exec_oracle.sh`, `exec_verify` (overwritten) | Prior-cycle shell runners. |
| `verify_two_point_countermodel.py` | Dated draft of the countermodel check (superseded by `verify_countermodel_only.py`). |
| `verify_two_point.py`, `verify_supply_transfer_independent.py`, `verify_malyshev_bound.py`, `direct_confirm*.py`, `confirm_contradiction.py`, `digest_audit.py`, `run_confirm*.py`, `run_inline*.py`, `scholar_dyadic_collapse_check.py`, `run_scholar_dyadic.py`, `final_exec.sh` | Prior-cycle scholar verification runners / audits; captures under `code/out/`. |
| `_placeholder.py` | Cruft created this cycle; cleared (no logic). |
