#!/bin/bash
# Run pymadcad bearing example

export LIBGL_ALWAYS_SOFTWARE=1
cd "$(dirname "$0")/../pymadcad"
python3 examples/bearing.py
