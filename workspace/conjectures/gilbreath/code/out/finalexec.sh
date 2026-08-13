echo "== FINAL_RUN =="
cd /workspace && timeout 540 python3 code/out/final_run.py 2>&1 | tee code/out/final_run.captured.txt; echo "EXIT=$?"
echo "== FINAL_RUN2 =="
cd /workspace && timeout 540 python3 code/out/final_run2.py 2>&1 | tee code/out/final_run2.captured.txt; echo "EXIT=$?"
