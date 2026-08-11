# Index — reflections

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0.0/1786464765420_01_learnings.md` | Attempt 1, judged unsolved, 1 learning(s). The run never started—the delegated `goals` agent died on an OpenRouter HTTP 400 and the attempt treated that infrastructure error as fatal, so no file was written and no answer or verification exists. Next time, retry the subagent call (provider 400s are often transient or caused by a model name the provider lacks), and if the same agent keeps failing, do that step inline with another model instead of aborting the whole run. |
| `L0.0/1786473788022_01_learnings.md` | Attempt 1, judged unsolved, 1 learning(s). The reduction "skip worth −1 ⟹ S(n)=ceil(Σ k·g(k))" contradicts the problem's own data — honest ceil(G(5))=20 vs given S(5)=17, and the dyadic derivation shows g(5)=3/2, so the claimed "matches oracle at n=1..5" outputs (which require g(5)=8/5, a non-dyadic) are inconsistent with the described method and must have been lifted from the oracle itself. Next time treat "matches S(5)" as the failure checkpoint it is, and redo the skip semantics from loopy CGT (temperature/pass value, per the `temperature_passing` and `pass_waiting` research) instead of asserting each pass subtracts 1 from the arithmetic sum; do not report an answer whose described method fails the statement's own example. |
