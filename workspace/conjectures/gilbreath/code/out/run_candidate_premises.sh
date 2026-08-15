cd /workspace && timeout 120 python3 code/out/_run_candidate_premises.py 2>&1 | tee code/out/check_candidate_premises.captured.txt; echo EXIT_CODE=$?
