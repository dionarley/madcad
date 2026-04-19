#!/usr/bin/env python3
"""
Run pymadcad examples with proper environment setup.
"""

import os
import sys

os.environ.setdefault("LIBGL_ALWAYS_SOFTWARE", "1")

EXAMPLES = {
    "1": ("bearing", "pymadcad/examples/bearing.py", "Bearing with balls"),
    "2": ("nut", "pymadcad/examples/nut.py", "Standard nut"),
    "3": ("axis-holder", "pymadcad/examples/axis-holder.py", "Axis holder"),
    "4": ("universal-joint", "pymadcad/examples/universal-joint.py", "Universal joint"),
    "5": (
        "planetary-gearbox",
        "pymadcad/examples/planetary-gearbox.py",
        "Planetary gearbox",
    ),
    "6": ("text", "pymadcad/examples/text.py", "3D text"),
    "7": (
        "kinematic-planetary",
        "pymadcad/examples/kinematic-planetary.py",
        "Kinematic planetary",
    ),
    "8": ("offscreen", "pymadcad/examples/offscreen.py", "Offscreen rendering"),
}


def main():
    print("=" * 50)
    print("pymadcad Examples Launcher")
    print("=" * 50)
    print()

    for key, (name, path, desc) in EXAMPLES.items():
        print(f"  [{key}] {name}")
        print(f"      {desc}")
        print()

    print("  [a] Run all examples")
    print("  [q] Quit")
    print()

    choice = input("Choose an example: ").strip().lower()

    if choice == "q":
        return 0

    if choice == "a":
        for key, (name, path, desc) in EXAMPLES.items():
            print(f"\n{'=' * 50}")
            print(f"Running: {name}")
            print(f"{'=' * 50}")
            run_example(path)
        return 0

    if choice in EXAMPLES:
        name, path, desc = EXAMPLES[choice]
        print(f"\nRunning: {name}")
        print(f"Description: {desc}")
        print()
        run_example(path)
        return 0

    print(f"Invalid choice: {choice}")
    return 1


def run_example(path):
    """Run a single example."""
    full_path = os.path.join(os.path.dirname(__file__), path)

    if not os.path.exists(full_path):
        print(f"Example not found: {full_path}")
        return

    print(f"Executing: {full_path}")
    print("-" * 30)

    try:
        with open(full_path) as f:
            code = f.read()

        exec(code, {"__file__": full_path, "__name__": "__main__"})
        print("-" * 30)
        print("Done!")

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    sys.exit(main())
