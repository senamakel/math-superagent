#!/usr/bin/env python3
"""Run the small closure oracles; prints the output."""
from refute.closure_oracle import check_closure_assertions
from refute.closure_analogues import run as run_analogues

if __name__ == '__main__':
    check_closure_assertions(200)
    print('---')
    run_analogues(200)
