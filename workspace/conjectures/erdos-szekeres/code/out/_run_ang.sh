cd /workspace && { echo '$ python code/out/wedge_witness_ang.py'; timeout 300 python code/out/wedge_witness_ang.py; echo 'EXIT: '$?; } > code/out/wedge_witness_ang.captured.txt 2>&1
