# Verify Barber's balanced-independent-set formula by brute force

Small-n brute force (enumerate all k-subsets of even and odd parity classes,
require independence, balance) to settle which transcription of the odd-n
formula is correct.

Run: `timeout 540 python3 code/out/verify_barber_balanced.py | tee code/out/verify_barber_balanced.captured.txt; echo EXIT_CODE=$?`
