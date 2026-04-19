#!/bin/bash
# Kill madcad/uimadcad processes

echo "Looking for madcad processes..."

# Find processes (exclude this script and terminal)
ps aux | grep -i madcad | grep -v grep | grep -v "$0" | grep -v alacritty | grep -v kitty

# Kill them
pids=$(pgrep -f "python.*madcad" 2>/dev/null)

if [ -z "$pids" ]; then
    echo "No madcad processes found"
else
    echo "Killing: $pids"
    kill -9 $pids 2>/dev/null
    echo "Done"
fi

# Also kill Python processes running examples
python_pids=$(pgrep -f "bearing.py|elliptic-gearbox|examples/" 2>/dev/null)
if [ -z "$python_pids" ]; then
    echo "No example processes found"
else
    echo "Killing examples: $python_pids"
    kill -9 $python_pids 2>/dev/null
fi

echo "Cleanup complete"