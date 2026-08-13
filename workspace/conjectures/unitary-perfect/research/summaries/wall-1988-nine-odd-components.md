# Wall (1988), *New unitary perfect numbers have at least nine odd components*

Full text: [[wall-1988-nine-odd-components.full]] (Fibonacci Quarterly 26, no. 4 (1988) 312–317, genuine OCR).

**Setup.** `σ*(p^e) = p^e + 1` for `p` prime, `e ≥ 1`; a number is unitary perfect if `σ*(N) = 2N`. Throughout `N = 2^a m` with `m` odd and `m` having `b` distinct odd prime-power components. Subbarao et al. had shown any *new* UPN must have `a ≥ 10`, `b ≥ 6`; Wall 1987 had shown any new UPN has an odd component `> 2^15` (smallest candidate 32771).

**Result.** Any UPN other than the five known ones has **at least nine odd components** (`b ≥ 9`). The paper establishes this by ruling out `b = 7` (§2) and `b = 8` (§3):

- §2 (seven odd components): Thm 2.1 establishes the four smallest components are exactly `3, 5, 7` with `a ≥ 12`; Thm 2.2 forces `s = 13`; Thm 2.3 forces `v = 67`; Thm 2.4 then shows the configuration `3·5·7·13·67·q·p` is impossible.
- §3 (eight odd components): Thm 3.1 `w,v = 3,5`, `a ≥ 12`; Thm 3.2 `u = 7`, `t = 13 or 19`; Thm 3.3 if `t = 19` then `s = 31`; Thm 3.4 `t = 13`; Corollary: no more components `≡ −1 mod 7`, none `≡ −1 mod 13`; Thm 3.5 `s < 73`; Thm 3.6 `s = 67`; Thm 3.7 then rules out `3·5·7·13·67·r·q·p`.
- Hence no UPN with exactly 7 or 8 odd components.

**Consequence for this run (the reason the source was fetched).** Combined with the workspace-proved 2-adic budget corollary `ω(odd) ≤ a + 1` (see `research/notes/parity-and-2-adic-budget.md`), it yields `a ≥ ω(odd) − 1 ≥ 8` for any sixth UPN — i.e. `2^8 = 256` divides any sixth UPN. That lower bound and its equality-case analysis live in `research/notes/lower-bound-on-a.md` and are computed against the witness set in `code/out/wall1988_budget_lower_bound.captured.txt`.

**Hypotheses / load-bearing care.** The result is stated *for a new UPN* (other than the five known). The four small witnesses 6, 60, 90, 87360 have `ω(odd) ∈ {1,2,2,4} < 9` and fall outside the theorem's scope; the fifth has `ω(odd) = 11 ≥ 9` and `a = 18`, satisfying the bound. Dropping the "other than the five known" hypothesis makes the statement false. The proofs are case analyses presented in outline (labored, repetitive); they are asserted by the source, not re-checked here beyond the five-witness run in `lower-bound-on-a.md`.

```claim
id: wall1988-nine-odd-components
statement: Any unitary perfect number other than the five known ones has at
  least nine odd prime-power components, omega(odd) >= 9.
hypotheses: N = 2^a m unitary perfect, m odd, N not one of the five known;
  the seven- and eight-component case analyses (Theorems 2.1-2.4, 3.1-3.7)
  rule out exactly 7 and exactly 8 odd components
holds-here: yes - applies to any sixth UPN, which is the object the run
  targets; the four small known UPNs (omega_odd < 9) fall outside the
  hypothesis so the statement is not refuted by them
status: asserted (proved in the source by outline case analysis; not
  independently verified here)
bearing: gives the missing lower side that the budget corollary alone cannot;
  combined with omega(odd) <= a+1 it yields a >= 8 (2^8 | sixth UPN), see
  lower-bound-on-a.md
anchor: research/notes/lower-bound-on-a.md; code/out/wall1988_budget_lower_bound.captured.txt
contradicts: (none)
answers: whether-6th-UPN-has-2^8
```
