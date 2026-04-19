#!/bin/bash
# Run pymadcad nut example

export LIBGL_ALWAYS_SOFTWARE=1
cd "$(dirname "$0")/../pymadcad"
python3 examples/nut.py