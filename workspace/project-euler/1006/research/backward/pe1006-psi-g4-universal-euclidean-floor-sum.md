# pe1006-psi-g4-universal-euclidean-floor-sum

```skeleton
next: the directive-10 order, each step RUN and captured: (1) wire the G3 telescoped v through code/lib/ueuclid.py with the joint (m,j) indexing so that Psi(k) is a constant-size monoid product (acceptance step 4); (2) reproduce Psi(k) k=1..150 and Psi(10)=10699667 through that wiring — the literal test of the reduction-indexing (which power of 10 the j-th digit carries); (3) reproduce anchors Psi(10^4)=34432237 and Psi(10^6)=20938836 and capture to code/out; (4) run k=10^18 under two Fibonacci approximants and confirm agreement. A tool_builder can start at step (2) today — the wiring script, mech_psi oracle, and ueuclid are all on disk; failure at any small k pinpoints the indexing error.
status: open
```
