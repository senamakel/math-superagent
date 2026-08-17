# Approach: Seidel two-graph / switching class of the graph, via regular-two-graph classification

```approach
idea: Reformulate srg(99,14,1,2) as the descendant of a regular two-graph on 100 points, and attack it through the Seidel-matrix / switching-class / regular-two-graph classification theory (Goethals-Seidel, Taylor, Bussemaker-Mathon-Seidel "Tables of two-graphs").
mechanism: The Seidel matrix S = J - I - 2A of the hypothetical graph has spectrum 70^1, (-7)^54, 7^44. The switching class [Gamma] is a two-graph; coning Gamma by an isolated vertex gives a two-graph on 100 points whose Seidel matrix has two eigenvalues -- i.e. a REGULAR two-graph -- and Gamma is recovered as its descendant at that vertex.
status: refuted
killed-by: The central bijection is FALSE. The Goethals-Seidel / Taylor descendant criterion: an SRG(v,k,lambda,mu) is a descendant of a regular two-graph (equivalently, associated with one) IFF k = 2mu, equivalently v = 2(2k - lambda - mu). For srg(99,14,1,2): k=14, mu=2 so k != 2mu (14 != 4), and v=99 != 2(28-1-2)=50. Therefore coning the graph by an isolated vertex does NOT give a regular two-graph on 100 points, and the graph is not a descendant of a regular two-graph under the standard construction. The eigenvalue/Seidel-spectrum computation in the mechanism is internally consistent (trace 70 + 54(-7) + 44(7) = 0 checks), but it describes a two-graph whose regularity condition is violated by these parameters, so the reformulation does not apply. (The inventor computed the wrong quantity: the k=2mu condition that governs descent is not met, and v fails the equivalent v=2(2k-lambda-mu).)
control-test: rook(3)=srg(9,4,1,2): k=4, mu=2, so k=2mu — it IS a descendant of a regular two-graph on 10 points (Paley two-graph). BvLS=srg(243,22,1,2): k=22, mu=2, k!=2mu, so BvLS is NOT a descendant. The two controls therefore sit on opposite sides of the criterion, but neither refutes the refutation: 99 fails the same k=2mu test BvLS fails, so the reformulation is inert for 99 exactly as it is inert for 243.
precedent:
  - Maksimović, "On Some Regular Two-Graphs up to 50 Vertices", Symmetry 15(2) (2023) 408, https://doi.org/10.3390/sym15020408 : states the exact iff criterion v = 2(2k - lambda - mu) for an SRG to be associated with a regular two-graph, and that descendants of a regular two-graph on v vertices are SRG(v-1, k, lambda, k/2). Evaluates (99,14,1,2): 2(28-1-2)=50 != 99.
  - Crnković & Maksimović, "Construction of strongly regular graphs having an automorphism group of composite order", Contributions to Discrete Math. 15(1) (2020), https://doi.org/10.55016/ojs/cdm.v15i1.62323 : states the k = 2mu descendant criterion; notes srg(99,14,1,2) has k=14, mu=2, so k != 2mu.
  - Haemers & Tonchev, "Spreads in Strongly Regular Graphs" (1996): descendant construction; every descendant of a regular two-graph is SRG with mu = k/2; an SRG(v-1,k,lambda,k/2) comes from a regular two-graph, i.e. the descendant relation forces mu=k/2.
  - Kuijken, "A study of incidence structures and codes related to regular two-graphs", Ghent (2003): same k=2mu framework.
  - Goethals & Seidel, "Strongly Regular Graphs Derived from Combinatorial Designs", Canad. J. Math. 22 (1970) 597-614, https://doi.org/10.4153/cjm-1970-067-9 : the classical SRG/two-graph framework.
```

```claim
id: seidel-twograph-descendant-closed-checked
statement: The two-graph descendant reformulation of srg(99,14,1,2) is CLOSED by
  exact code arithmetic (code/out/verify_twograph_gate.captured.txt, verified
  through lib.srg.is_srg): an SRG is a descendant of a REGULAR two-graph iff
  k = 2*mu (equiv. v = 2(2k-lambda-mu)). At (99,14,1,2): k=14 != 2*mu=4 and
  v=99 != 2(28-1-2)=50, so coning by an isolated vertex does NOT give a regular
  two-graph — the reformulation is inert for 99. Controls: rook(3)=srg(9,4,1,2)
  passes (k=4=2mu, n=10, the Paley two-graph on 10 points); BvLS=srg(243,22,1,2)
  fails (k=22 != 4) exactly like 99. The looser claim "BvLS descends from a
  244-point two-graph" concerns a NON-regular two-graph (its Seidel matrix has
  three distinct eigenvalues), not a regular one — so it does not contradict the
  gate. The Seidel spectrum 70^1,(-7)^54,7^44 is correctly derived; only the
  two-graph-regularity step fails.
hypotheses: standard regular-two-graph descendant criterion (Goethals-Seidel,
  Taylor; Maksimovic states v=2(2k-lambda-mu) iff criterion and evaluates
  (99,14,1,2): 50 != 99).
holds-here: yes — the arithmetic gate is the decisive fact and is verified in
  code at the exact (99,14,1,2) parameters and both controls.
status: checked (exact integer arithmetic through lib.srg.is_srg; capture
  code/out/verify_twograph_gate.captured.txt, script exit 0, all asserts passed).
bearing: the regular-two-graph/switching-class route is a closed dead end for 99
  (k != 2mu, same failure as 243); no further work should cone 99 to a regular
  two-graph. Answers task verify-twograph-gate (done).
anchor: code/out/verify_twograph_gate.captured.txt, research/approaches/seidel-twograph-descendant.md
contradicts: none (the loose BvLS-244-point claim is about a non-regular
  two-graph and is reconciled, not contradicted)
answers: verify-twograph-gate
```

## Why this is now refuted

The reformulation is a change of representation (graph -> switching class -> regular two-graph), and it would be a legitimate one *if* the parameters satisfied the descendant criterion. They do not: the descendant/associated relationship with a *regular* two-graph is controlled by k = 2μ (equivalently v = 2(2k−λ−μ)), and srg(99,14,1,2) has k=14, μ=2 (so k=7μ), and v=99 (≠50). Five independent sources state the criterion; two of them evaluate (99,14,1,2) explicitly and conclude it fails. The Seidel spectral computation was not the error — the misstep was assuming that coning a *regular* graph by an isolated vertex produces a *regular* two-graph regardless of parameters, which is only true in the k=2μ case (the cone's Seidel matrix then has two distinct eigen/nontrivial eigenvalues). Outside that case the cone's Seidel matrix has three distinct eigenvalues, so it is not a regular two-graph and the descendant bijection does not hold.

## What the mechanism got right (kept for the record)

- The Seidel spectrum is correctly derived: on the all-ones vector S1 = (v−1−2k)1 = 70·1; on the r=3 eigenspace (orthogonal to 1) S = −I−2A gives (−1−2·3)=−7; on the s=−4 eigenspace (−1−2·(−4))=+7. Trace 70+54(−7)+44(7) = 0 ✓. It matches the problem's own 3^54, −4^44. So the *eigenvalue* content is right; the *two-graph regularity* claim is what fails.

## Discipline note

This refutation is evidence-based, not by absence: the criterion is stated precisely, evaluated at the exact parameters, and agrees across five sources including one that computes the 99 case explicitly. It is not merely "not found in the literature." No further work should propose coning srg(99,14,1,2) to a regular two-graph as a route, because the parameters fail the named necessary-and-sufficient condition.

Directive 21 (method correction): this line was opened to literature search (agent-run-60: exa_search + read_sources, 60s and 99s model calls) before the one-line arithmetic gate was run — which is why no capture appeared for ~22 minutes. The arithmetic here is operator-recalled and must be verified in code first (task `verify-twograph-gate`), not imported from recall; search only if the check passes.
