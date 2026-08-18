# Contiguous-window Fibonacci-block monoid

```approach
id: pe1006-contiguous-window-fibonacci-block-monoid
status: refuted
```

The rolling identity V_{r+1}=10 V_r-y_r 10^k+y_{r+k} and additive block summaries are exact and verified through k=150, including Psi(3), Psi(10), and the k=10^4 anchor. But the required fixed-dimensional Fibonacci-block closure for the shifted pair orbit (y_r,y_{r+k}) is not established; the backward analysis identifies this as the sole O(log k) lemma and marks it refuted. The implemented route remains O(k), so it cannot evaluate k=10^18.