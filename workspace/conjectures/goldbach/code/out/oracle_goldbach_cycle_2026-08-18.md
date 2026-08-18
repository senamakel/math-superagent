# Oracle output

The naive checker in `code/goldbach_oracle.py` was executed. Output:

```text
worked examples: {4: True, 6: True, 8: True, 10: True, 12: True, 2: False}
naive/fast agree for every even n in [4,1000]
```

This is a mechanical check of the definition in `code/lean/Lib/Statement.lean`, not evidence for the conjecture at untested sizes. The naive oracle is exponential only in the sense of the permitted small-instance oracle class; it is bounded at 1000 and is not the run's full-size algorithm.