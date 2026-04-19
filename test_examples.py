#!/usr/bin/env python3
"""
Test all pymadcad examples and log results.
"""

import os
import sys
import subprocess
from datetime import datetime

os.environ.setdefault("LIBGL_ALWAYS_SOFTWARE", "1")

EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), "pymadcad/examples")


def get_examples():
    """Get list of example files."""
    if not os.path.exists(EXAMPLES_DIR):
        print(f"Examples dir not found: {EXAMPLES_DIR}")
        return []

    files = []
    for f in os.listdir(EXAMPLES_DIR):
        if f.endswith(".py") and not f.startswith("_"):
            files.append(f)
    return sorted(files)


def run_example(filename):
    """Run a single example and capture output."""
    fullpath = os.path.join(EXAMPLES_DIR, filename)

    result = {
        "file": filename,
        "status": "unknown",
        "output": "",
        "error": "",
    }

    try:
        proc = subprocess.run(
            ["python3", fullpath],
            capture_output=True,
            text=True,
            timeout=15,
            env={**os.environ, "LIBGL_ALWAYS_SOFTWARE": "1"},
        )

        result["status"] = "ok" if proc.returncode == 0 else "error"
        result["output"] = proc.stdout[:2000]
        result["error"] = proc.stderr[:2000]

    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["output"] = "Timeout (window likely opened)"

    except Exception as e:
        result["status"] = "exception"
        result["error"] = str(e)[:500]

    return result


def main():
    print("=" * 60)
    print("pymadcad Examples Test Suite")
    print("=" * 60)

    examples = get_examples()
    print(f"Found {len(examples)} examples\n")

    results = []
    for i, example in enumerate(examples, 1):
        print(f"[{i}/{len(examples)}] Testing: {example}")
        result = run_example(example)
        results.append(result)

        status_symbol = {
            "ok": "✅",
            "error": "❌",
            "timeout": "⏱️ ",
            "exception": "⚠️ ",
            "unknown": "❓",
        }.get(result["status"], "?")

        print(f"  {status_symbol} {result['status']}")

        if result["error"]:
            # Extract error type
            err_lines = result["error"].split("\n")
            for line in err_lines:
                if "Error:" in line or "NameError" in line or "Traceback" in line:
                    print(f"     {line[:80]}")

    # Write log file
    log_file = "/home/dnly/stage/madcad/examples_test.log"
    with open(log_file, "w") as f:
        f.write(f"# pymadcad Examples Test Log\n")
        f.write(f"# Date: {datetime.now().isoformat()}\n")
        f.write(f"# Total: {len(examples)} examples\n")
        f.write("=" * 60 + "\n\n")

        for r in results:
            f.write(f"## {r['file']}\n")
            f.write(f"Status: {r['status']}\n")
            f.write("-" * 40 + "\n")

            if r["error"]:
                f.write(f"Error:\n{r['error']}\n")
            if r["output"]:
                f.write(f"Output:\n{r['output']}\n")
            f.write("\n")

    print(f"\nLog written to: {log_file}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    by_status = {}
    for r in results:
        s = r["status"]
        by_status[s] = by_status.get(s, 0) + 1

    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")

    print(f"\nTotal: {len(results)} examples")

    # Extract common errors
    print("\n" + "=" * 60)
    print("COMMON ERRORS")
    print("=" * 60)

    errors_seen = {}
    for r in results:
        if r["error"]:
            # Extract first error line
            for line in r["error"].split("\n"):
                if "NameError:" in line:
                    err = line.strip()
                    errors_seen[err] = errors_seen.get(err, 0) + 1
                elif "Error:" in line and ":" in line:
                    err = line.strip()[:60]
                    errors_seen[err] = errors_seen.get(err, 0) + 1

    for err, count in sorted(errors_seen.items(), key=lambda x: -x[1]):
        print(f"  [{count}x] {err}")


if __name__ == "__main__":
    sys.exit(main())
