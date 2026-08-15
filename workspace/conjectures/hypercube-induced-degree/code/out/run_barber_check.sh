#!/bin/sh
timeout 540 python3 code/out/check_barber_balanced2.py 2>&1 | tee code/out/check_barber_balanced.captured.txt; echo EXIT_CODE=$?
