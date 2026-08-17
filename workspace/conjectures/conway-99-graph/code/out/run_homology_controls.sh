#!/bin/bash
cd /workspace
PYTHONPATH=/workspace/code python code/out/homology_controls.py > code/out/homology_controls.captured.txt 2>&1
