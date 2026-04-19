# AGENTS.md - MadCAD Setup Repository

## Project Overview

This is a utility repository for setting up **pymadcad** (Python 3D geometry library with OpenGL). The main artifact is `script.sh` for automated Ubuntu/Debian installation.

**This is NOT the pymadcad source code itself.**

---

## Build/Test Commands

```bash
# Run the setup script
chmod +x script.sh && ./script.sh

# Or run directly
bash script.sh
```

### Testing Installation

```bash
# Activate virtual environment
source venv/bin/activate

# Basic import test
python -c "from madcad import *; print('OK')"

# Headless test (no display required)
xvfb-run -a python -c "from madcad import Mesh, show; print('OK')"

# Full 3D rendering test
python -c "from madcad import *; show([brick()])"
```

---

## Code Style Guidelines

### Shell Script Style (script.sh)

```bash
#!/usr/bin/env bash
set -e          # Exit on errors
set -u          # Exit on undefined variables

echo "[+] Creating environment..."
python3 -m venv venv
source venv/bin/activate

# Always quote variables: "$VAR" not $VAR
echo "[+] Installing: $PACKAGE"
```

### Python Code Style

If Python code is added to this repository:

**General:**
- Write clean, readable, maintainable code
- Prefer explicit over implicit
- Follow PEP 8 style conventions

**Imports:**
```python
import os
import sys
from typing import Optional, List

import numpy as np
from madcad import Mesh, brick
```

**Formatting:**
- Line length: 88 characters (Black default)
- Indentation: 4 spaces
- Use Black for formatting, isort for import sorting

**Naming:**
```python
# Variables/functions: snake_case
def calculate_area(width, height):
    return width * height

# Classes: PascalCase
class MeshRenderer:
    pass

# Constants: SCREAMING_SNAKE_CASE
MAX_VERTICES = 10000
```

**Type Hints:**
```python
def process_mesh(mesh: Mesh, quality: float = 1.0) -> Optional[Mesh]:
    if mesh is None:
        return None
    return mesh
```

**Error Handling:**
```python
try:
    result = operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise CustomError("Failed") from e
```

**Documentation:**
```python
def function(arg1: str, arg2: int) -> bool:
    """Short one-line summary.

    Extended description if needed.

    Args:
        arg1: Description.
        arg2: Description.

    Returns:
        Description.

    Raises:
        ValueError: When invalid.
    """
    pass
```

---

## pymadcad Specific Guidelines

```python
from madcad import *

# Create mesh
mesh = Mesh([
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)  # vertices
], [
    (0, 1, 2), (0, 2, 3)  # faces
])

# Display
show(mesh)

# Geometry creation
b = brick()              # unit cube
b = brick(width=2)       # with dimensions
b = brick(width=2, height=3, depth=4)

# Transformations
transformed = b.rotateX(math.pi/4).translate((1, 0, 0))
```

---

## Troubleshooting

```bash
# OpenGL software rendering fallback
export LIBGL_ALWAYS_SOFTWARE=1

# Check OpenGL info
glxinfo | grep "OpenGL version"

# Headless testing
sudo apt install xvfb
xvfb-run -a python your_script.py
```

---

## Notes for Agents

- Main deliverable is `script.sh` for environment setup
- No test framework exists in this repository
- If bugs are found in pymadcad itself, report to upstream project
- Test script.sh changes in a clean Ubuntu/Debian environment