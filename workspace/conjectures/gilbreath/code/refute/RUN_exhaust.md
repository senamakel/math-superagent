# Run the exhaustive {2,4}-gap search

```
cd /workspace/code/refute && timeout 500 python3 run_exhaust_carved.sh.py 2>&1 | tee /workspace/code/out/refute_exhaust_carved_20.captured.txt; echo EXIT=$?
```
