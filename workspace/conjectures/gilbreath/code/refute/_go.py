#!/usr/bin/env python3
import sys
sys.path.insert(0, '/workspace/code')
from refute.leftmost_decides import main
sys.argv = ['leftmost_decides.py', '5', '45']
main()
