# Tasks

- [x] Write /workspace/brute.py brute-force oracle (naive, exact integer).
- [x] Write /workspace/pointcount.py independent point-count validation.
- [x] Validate point-count on cubes A and B (both OK).
- [x] Run brute for n=1..6,10; all oracle values match; save brute_output.txt.
- [x] Identify governing theory (orthogonal equal-norm integer triples; Ehrhart / Ionascu Thm 3.1) with sources.
- [x] Validate the frame-based efficient method via /workspace/frame_method.py against the oracle for n=1,2,4,5,10,50 (all OK).
- [x] Collect primitive-frame growth data (n=10..200).
- [x] Derive the O(1)-per-frame summation (power-sum / Faulhaber) so cost stops growing with n.
- [x] Implement /workspace/solution_power.py: O(1)-per-frame Faulhaber power-sum
      summation (reuses frame_method enumeration unchanged via import).
- [x] Validate power-sum vs oracle (C/S for n=1,2,4,5,10,50 all OK) and
      bit-for-bit equality vs direct t-loop at n=50 (assert). Evidence in
      /workspace/power_validate.txt.
- [ ] Implement full solution.py (canonical primitive-frame enumeration via primary Hurwitz quaternions) agreeing with brute; compute S(5000) mod 10^9 and verify.
