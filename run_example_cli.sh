#!/bin/bash
# Wrapper para rodar exemplos do pymadcad no CLI com Dark mode

export LIBGL_ALWAYS_SOFTWARE=1

EXAMPLE=$1
EXAMPLE_NAME=$(basename "$EXAMPLE" .py)

if [ -z "$EXAMPLE" ]; then
    echo "Usage: $0 <example.py> [dark-theme]"
    echo "Themes: grey-orange, dark-red, dark-green"
    exit 1
fi

THEME=${2:-dark-green}

echo "Running $EXAMPLE_NAME with theme $THEME..."

python3 -u << PYEOF
import sys
import os
os.environ['LIBGL_ALWAYS_SOFTWARE'] = '1'

from PyQt5.QtWidgets import QApplication
from uimadcad import settings

print("Creating QApp...")
app = QApplication(sys.argv)
print("Setting theme...")
settings.use_color_preset('$THEME')
print("Theme: $THEME")

print("Loading example...")
with open("$EXAMPLE") as f:
    exec(f.read())

print("$EXAMPLE_NAME loaded - window should open")
sys.exit(app.exec_())
PYEOF
echo "Script finished"