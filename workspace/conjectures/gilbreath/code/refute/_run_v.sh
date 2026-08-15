PYTHONPATH=/workspace/code timeout 540 python3 /workspace/code/refute/verify_transfer_refutation.py 2>&1 | tee /workspace/code/out/transfer_refutation.captured.txt; echo EXIT_CODE=$?
