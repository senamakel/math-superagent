# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

multiset_census_n20.txt is priority 1 done right -- a census of WHICH sets A = M_d sym-diff M_d' occur, with size, diameter, run count and run-length profile, not just sizes. Keep that shape and push it to the largest n you can enumerate exactly, stating the n.

Now read your own diameter column, because it cuts against problem.md and you must not inherit my error. I wrote that small symmetric differences imply short-range structure. Your census shows that is FALSE. At n=20 the sets have |A| = 6 to 12 but diameter 10 to 18 -- small sets spread across nearly the whole index range, up to 8 runs, run_lengths mostly [1,1,1,1,1,1,1,1]. Eight isolated singletons spanning diameter 14 is small and maximally NON-local. It couples positions at opposite ends of the string.

So size is the wrong statistic, and the O(n) distance enumerator does not say what I claimed. The question turns on DIAMETER and run structure, not cardinality. Restate it:

1. Tabulate the joint distribution of (|A|, diam A, #runs A) over all d,d' at every n you can reach. That is the object that decides this.
2. Sharp form: is there a bound R, uniform in n, with every occurring A a union of at most R runs of bounded length? Your data already suggests NO. Report max-runs and max-diameter as functions of n. If max-runs grows with n, the collapse as I framed it is FALSE -- say so plainly and early.
3. This makes the witness hunt MORE likely to succeed. Isolated singletons at large separation are exactly what separates two strings with identical pair correlations. Prioritise finding an explicit A of that shape and building h, h' around it.

problem.md is not authoritative -- three values I seeded in the previous workspace were wrong and computation caught all three. Print the stated claim beside your measurement whenever they disagree. Fenced claim block on the census with its n range.

Closed the single open task `collapse-decision` as done — its two steps (witness fiber test n≤16 and census n≤128) are already carried out and verified — and replaced it with four open tasks in steer-1's order: push the which-sets census to the largest exactly-enumerable n, tabulate the joint (|A|, diam, #runs) distribution, report max-runs(n)/max-diam(n) to test the uniform bound R, and prioritize the witness hunt around isolated-singleton A. I opened `research/threads/diameter-run-structure.md` (marking the cardinality reading dead as steer-1 established) and rewrote CONTEXT.md's problem line, Numbers, Ruled out, and Gaps sections so every role now sees the diameter/run-structure reorientation and the non-authority of problem.md. I deliberately did not file the directive's mathematical claims as claims, and I flagged steer-1's sharper caution: long-span support alone does not refute collapse (the decision is C_K-fiber constancy), so "max-runs grows" kills the framing, not the statement.
