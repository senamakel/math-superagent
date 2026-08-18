# Index — code/g4_symbolic

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `run_experiment.py` | Entry point that runs the cylinder-module falsification experiment. |
| `run_experiment_standalone.py` | Standalone runner for the cylinder-module experiment, importable directly. |
| `test_module.py` | Exact cylinder-atom builder: computes digit tuple, decimal value and square on each atom of the rotation partition cut by {-j·alpha: 0<=j<=k}, and reports rank of accumulated (digits,v,v^2) vectors over a prime — falsification diagnostic for a fixed-dimensional cylinder module. |
