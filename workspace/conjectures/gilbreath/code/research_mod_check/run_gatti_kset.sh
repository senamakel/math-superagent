#!/usr/bin/env bash
# Verify Gatti 2020 Cor 1 / Lemma 4 claims about K_S for S = {2,3,5}.
cd /workspace
echo "--- verify_gatti_kset.py ---"
timeout 60 python3 code/research_mod_check/verify_gatti_kset.py 2>&1 | tee code/out/gatti_kset_check.captured.txt
echo "EXIT_CODE=$?"