timeout 540 python3 check_constant_blocks.py 2>&1 | tee ../out/block_constancy.captured.txt
echo EXIT_CODE=$?