# Check the Alon–Tarsi certificate's direction

Candidate 3 (`alon-tarsi-coefficient-certificate`) claims: if a graph has an
orientation D with max out-degree ≤ 3 and EE(D) ≠ EO(D), then G is NOT
4-colourable, and proposes calibrating on K4 (expect: no such orientation),
K5 (expect: one such orientation exists), Moser spindle (expect: none).

The literature (Hefetz 0911.2099 restatement of Alon–Tarsi 1992) instead
says: an orientation with out-degree < k for every vertex AND unbalanced
Eulerian-subgraph parity (sum of (-1)^{e(H)} over Eulerian subdigraphs ≠ 0)
certifies AT(G) ≤ k, i.e. it is a CHOOSABILITY UPPER BOUND — a *positive*
(colorable) certificate, not a negative one.

So the direction is suspect, and the K5 calibration the candidate proposes
would fail: K5 is not 4-choosable, so no orientation with max out-degree ≤ 3
can have unbalanced parity (that would certify ch(K5) ≤ 4). Verify by
brute force over all 2^{10} orientations of K5.
