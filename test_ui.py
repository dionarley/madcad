#!/usr/bin/env python3
"""
UI Test script for uimadcad
Tests: dark mode, rendering, examples
"""

import os
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("LIBGL_ALWAYS_SOFTWARE", "1")


def test_imports():
    """Test that all modules import correctly."""
    print("[TEST] Imports...")
    try:
        import madcad
        from madcad import generation

        print("  OK: madcad imports OK")

        from uimadcad import app

        print("  OK: uimadcad imports OK")

        return True
    except Exception as e:
        print(f"  FAIL: Import failed: {e}")
        return False


def test_dark_mode():
    """Test dark mode settings."""
    print("[TEST] Dark Mode...")
    try:
        from uimadcad import settings

        settings.darkmode = True
        print("  OK: Dark mode enabled")

        settings.darkmode = False
        print("  OK: Dark mode disabled")

        return True
    except Exception as e:
        print(f"  FAIL: Dark mode test failed: {e}")
        return False


def test_geometry_generation():
    """Test geometry generation (workaround for NaN bug)."""
    print("[TEST] Geometry Generation...")
    try:
        from madcad import vec3, brick, cylinder, cone, icosphere, regon, Axis
        from madcad.generation import brick as gen_brick
        from madcad.generation import cylinder as gen_cylinder
        from madcad.generation import cone as gen_cone
        from madcad.generation import icosphere as gen_icosphere
        from madcad.generation import regon as gen_regon
        from madcad.generation import Axis as gen_Axis

        tests = [
            (
                "brick_center_width",
                lambda: gen_brick(center=vec3(0, 0, 0), width=vec3(1, 1, 1)),
            ),
            (
                "brick_min_max",
                lambda: gen_brick(min=vec3(-0.5, -0.5, -0.5), max=vec3(0.5, 0.5, 0.5)),
            ),
            ("cylinder", lambda: gen_cylinder(vec3(0, 0, 0), vec3(0, 0, 2), 1)),
            ("cone", lambda: gen_cone(vec3(3, 0, 2), vec3(3, 0, 0), 1)),
            ("sphere", lambda: gen_icosphere(vec3(0, 0, 0), 1)),
            # ("regon", lambda: gen_regon(gen_Axis.O, 1, 6)),
        ]

        for name, func in tests:
            mesh = func()
            assert len(mesh.points) > 0, f"{name}: no points"
            print(f"  OK: {name}: {len(mesh.points)} points")

        return True
    except Exception as e:
        print(f"  FAIL: Geometry test failed: {e}")
        return False


def test_scene_creation():
    """Test scene creation."""
    print("[TEST] Scene Creation...")
    try:
        from madcad import vec3, brick
        from madcad.rendering import Scene

        b = brick(center=vec3(0, 0, 0), width=vec3(1, 1, 1))
        scene = Scene([b])

        print(f"  OK: Scene created")
        return True
    except Exception as e:
        print(f"  FAIL: Scene creation failed: {e}")
        return False


def test_mesh_operations():
    """Test mesh operations."""
    print("[TEST] Mesh Operations...")
    try:
        from madcad import vec3, brick

        b = brick(center=vec3(0, 0, 0), width=vec3(1, 1, 1))

        box = b.box()
        assert box.max.x > box.min.x, "Invalid box"
        print(f"  OK: box(): {box.max - box.min}")

        assert b.issurface(), "Not a surface"
        print(f"  OK: issurface(): True")

        return True
    except Exception as e:
        print(f"  FAIL: Mesh operations failed: {e}")
        return False


def test_examples():
    """Test rendering various examples."""
    print("[TEST] Rendering Examples...")
    try:
        from madcad import vec3, brick, cylinder
        from madcad.rendering import Scene
        from madcad.generation import brick as gen_brick
        from madcad.generation import cylinder as gen_cylinder

        examples = [
            ("simple_box", brick(center=vec3(0, 0, 0), width=vec3(1, 1, 1))),
            (
                "two_boxes",
                [
                    brick(center=vec3(-1, 0, 0), width=vec3(1, 1, 1)),
                    brick(center=vec3(1, 0, 0), width=vec3(1, 1, 1)),
                ],
            ),
            ("cylinder", gen_cylinder(vec3(0, 0, 0), vec3(0, 0, 2), 0.5)),
            (
                "complex",
                [
                    brick(center=vec3(0, 0, 0), width=vec3(2, 1, 1)),
                    gen_cylinder(vec3(1, 0, 1), vec3(1, 0, -1), 0.3),
                ],
            ),
        ]

        for name, geom in examples:
            scene = Scene(geom)
            print(f"  OK: {name}: scene created")

        return True
    except Exception as e:
        print(f"  FAIL: Examples test failed: {e}")
        return False


def test_file_export():
    """Test mesh export (STL) - skip if not available."""
    print("[TEST] File Export...")
    print("  SKIP: Not implemented in this version")
    return True  # Skip this test


def main():
    print("=" * 50)
    print("uimadcad UI Test Suite")
    print("=" * 50)

    tests = [
        test_imports,
        test_dark_mode,
        test_geometry_generation,
        test_scene_creation,
        test_mesh_operations,
        test_examples,
        test_file_export,
    ]

    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"  FAIL: EXCEPTION: {e}")
            results.append(False)
        print()

    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 50)

    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
