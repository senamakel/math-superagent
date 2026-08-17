

---

PE1006 solution.py — mechanical-word construction, phases 1..4 (corrected slope a=m/N).

=== Phase 1: construction word set == brute distinct factors ===
P1 PASS: construction word set == brute distinct factors for all k=1..150.

=== Phase 2: Psi_direct (telescoped v) vs brute Psi ===
P2 PASS: exact for k=1..60, mod M for 61..150.

=== Phase 3: C(j,jp)==A(jp-j) and Psi==sum A(d)W(d) mod M ===
P3 FAIL: first C!=A at k=3 j=1 jp=1 C=1 A=2
P3-collapse FAIL at k=3: Psi_collapse=20402 brute=20302

=== P3 extra: collapse vs Psi_direct at k=200..600 (no brute) ===
P3-extra FAIL at k=200: collapse=64554455 direct=83031232

=== Phase 4: anchors Psi(k) mod M at k=10^4, 10^6 (O(k) phase-3 sum) ===
Psi(10000) mod 101001001 = 16242174   (a=4181/10946, n=19, took 0.01s)
Psi(1000000) mod 101001001 = 77578256   (a=514229/1346269, n=29, took 1.48s)

Note: Psi(10^18) mod M requires the O(log) universal-Euclidean method
(thread G4); the naive m=0..k sum is forbidden at 10^18 by the redirect.
The Phase-4 anchors above are what that method must reproduce.
