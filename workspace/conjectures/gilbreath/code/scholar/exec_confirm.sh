cd /workspace/code/scholar && timeout 540 python3 confirm_contradiction.py 2>&1 | tee /workspace/code/out/scholar_dyadic_contradiction.captured.txt; echo EXIT_CODE=$?
