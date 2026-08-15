PYTHONPATH=/workspace/code timeout 540 python3 /workspace/code/refute/run_transfer.py 2>&1 | tee /workspace/code/out/transfer_universal.captured.txt; echo EXIT_CODE=$?
