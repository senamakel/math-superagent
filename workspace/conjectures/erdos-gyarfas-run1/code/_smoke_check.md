# Smoke-check note

Verify that code/brute.py still imports and runs after the has_power_of_two_cycle
consolidation (local def removed in favour of the shelved lib.oracle copy).

**RESOLVED, tool_builder this cycle**: `cd /workspace/code && python brute.py` runs to
exit 0 — K4 min degree 3, cycles [3,4]; K3,3 min degree 3, cycles [4,6]; Petersen
min degree 3, cycles [5,6,8,9]; cube Q3 min degree 3, cycles [4,6,8]; graph6
round-trip of K4 ("C~") equals the hand-built K4. Any doubt about the import
consolidation is gone, and the module is an importable, executable path again.
