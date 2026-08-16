# g-input-strictness

```skeleton
goal: CORRECTION (adversarial, tool_builder agent-run-30 readcone_survey_capture.txt): the e_{n-2} exhibition settles S(n) in {0,1} for the PER-WINDOW family h_n = e_{n-2}, NOT for a single fixed infinite string. As n varies, position n-2 covers every index, so no fixed string can carry it (it would be all-ones, density 1). Run-30: for a FIXED single 1 at j, nu2(n) <= j+1 = O(1) so S(n)=Theta(n); for the natural fixed sparse families (ones at 2^m-2 and at 2^m) max|S|/sqrt n GROWS 6.25->62.5 over n=8..4000, both FAIL. The find is an exact closed form: position j is read by depth d iff (n-1-j) bitwise-submask of d, machine-checked on 245344 (n,j) pairs, |C_j(n)| = #{d in [2,n-1] : r subseteq d}, and h reads 1/2^{pc(n-1-j)} of depths. So G-input-strictness as a FIXED-string lemma remains OPEN; the family version is settled. The strictness witness, if it exists, must be growing and boundary-avoiding. This leaves the second-moment-strictly-weaker-than-switch-conclusion resting only on the family version, which does not meet the fixed-string quantifier.
killed-by: settled ONLY in the per-window family sense; fixed-string version open with two natural families falsified
rests-on: read-cone-column-equivalence (position j read iff (d-(n-1-j)) subseteq d); excess-is-negative-character-sum
status: open
```
