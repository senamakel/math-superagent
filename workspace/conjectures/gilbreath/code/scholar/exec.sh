cd /workspace/code/scholar && timeout 540 python3 run_scholar_dyadic.py 2>&1 | tee /workspace/code/out/scholar_dyadic_collapse_check.captured.txt; echo EXIT_CODE=$?
