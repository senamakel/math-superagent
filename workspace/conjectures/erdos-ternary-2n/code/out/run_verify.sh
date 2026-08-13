cd /workspace/code/out && timeout 300 python3 verify_al.py 2>&1 | tee verify_al.captured.txt; echo EXIT_CODE=$?
