cd /workspace && timeout 120 python3 research/check_candidate2_dictionary.py 2>&1 | tee research/candidate2_dict.captured.txt; echo EXIT_CODE=$?
