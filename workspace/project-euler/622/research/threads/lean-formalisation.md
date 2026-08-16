# Thread: Lean formalisation of the shuffle and the order-of-2 reduction

```thread
question: How to state, in Lean, the out-shuffle on an even deck and the reduction s(n) = orderOf (2 : (ZMod (n-1))^x), so that both elaborate — statement first, ending in sorry.
status: live
rests-on: none (informal reduction in research/backward/riffle-order-60.md, gap G-shuffle-order)
blocked-by: none
next: lean_prover writes code/lean/Lib/Shuffle.lean (out-shuffle position map: top/bottom fixed, interior i -> (2*i-1) mod (n-1)) and code/lean/Lib/Reduction.lean (s(n) = ord_{n-1}(2) for even n >= 4), each as a theorem ending in `:= by sorry`, then runs lean_check to file a verdict.
```

## Why this direction now

The operator's directive stops library building: METHOD.md is the binding
constraint, nothing has been formalised yet, and a run ending with an answer and
no passing verdict has failed the task. The first deliverable is not a proof but
the correct *statements*, because proving the wrong statement is worse than
proving nothing. Elaboration checked by `lean_check` files a verdict; proofs come
after the statements are settled.
