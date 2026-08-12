#!/usr/bin/env sh
# Run the Bremner II Category III six-square / K3 rational-point checks.
cd "$(dirname "$0")" && python3 k3_surface_checks.py | tee k3_surface_checks_output.txt