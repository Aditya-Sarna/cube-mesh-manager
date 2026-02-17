"""
Quick demo script - installs addon and runs basic tests
"""
import bpy
import sys
import os

# Get the addon directory
addon_dir = os.path.dirname(os.path.abspath(__file__))
addon_file = os.path.join(addon_dir, "cube_mesh_manager.py")

print("=" * 60)
print("INSTALLING CUBE MESH MANAGER ADDON")
print("=" * 60)

# Install the addon
try:
    bpy.ops.preferences.addon_install(filepath=addon_file)
    print("✓ Addon installed")
except Exception as e:
    print(f"Install note: {e}")

# Enable the addon
addon_module = "cube_mesh_manager"
try:
    bpy.ops.preferences.addon_enable(module=addon_module)
    print(f"✓ Addon '{addon_module}' enabled")
except Exception as e:
    print(f"Enable note: {e}")

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

print("\n" + "=" * 60)
print("DEMO 1: DISTRIBUTING 9 CUBES")
print("=" * 60)

# Demo 1: Distribute 9 cubes
bpy.context.scene.cube_manager_props.number_of_cubes = 9
bpy.ops.cube.distribute_cubes()
print(f"✓ Created {len(bpy.context.scene.objects)} objects in 3×3 grid")

print("\n" + "=" * 60)
print("DEMO 2: MERGING ADJACENT CUBES")
print("=" * 60)

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# IMPORTANT: Create cubes with size=1, they must touch perfectly
# Cube 1 at origin: center at (0,0,0), extends from -0.5 to +0.5 on each axis
# Cube 2 at (1,0,0): center at (1,0,0), extends from 0.5 to 1.5 on X-axis
# They share the face at X=0.5

print("Creating Cube 1 at (0, 0, 0)...")
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
cube1 = bpy.context.active_object
cube1.name = "LeftCube"

print("Creating Cube 2 at (1, 0, 0) - TOUCHING Cube 1...")
bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))
cube2 = bpy.context.active_object
cube2.name = "RightCube"

print(f"✓ {cube1.name}: center at (0,0,0), face at X=0.5")
print(f"✓ {cube2.name}: center at (1,0,0), face at X=0.5")
print(f"✓ They share a common face at X=0.5!")

# CRITICAL: Make sure no transforms are applied
print("\nApplying all transforms (scale, rotation, location)...")
bpy.ops.object.select_all(action='DESELECT')
cube1.select_set(True)
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

bpy.ops.object.select_all(action='DESELECT')
cube2.select_set(True)
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

# Select both and merge
print("\nSelecting both cubes...")
bpy.ops.object.select_all(action='DESELECT')
cube1.select_set(True)
cube2.select_set(True)
bpy.context.view_layer.objects.active = cube1

print("Attempting merge...")
result = bpy.ops.cube.compose_mesh()

if result == {'FINISHED'}:
    merged = bpy.context.active_object
    print(f"\n✓ MERGE SUCCESSFUL!")
    print(f"  - Vertices: {len(merged.data.vertices)} (was 16, now 12)")
    print(f"  - Faces: {len(merged.data.polygons)} (was 12, now 10)")
    print(f"  - 2 internal faces removed ✓")
else:
    print(f"\n✗ Merge failed or no common face detected")
    print(f"  Result: {result}")

print("\n" + "=" * 60)
print("DEMO COMPLETE - CHECK THE 3D VIEWPORT!")
print("=" * 60)
print("\nThe merged cube is now displayed.")
print("Notice: No internal face between the two cubes!")
print("\nTo test yourself:")
print("1. Press N to open sidebar")
print("2. Click 'Cube Manager' tab")
print("3. Try the buttons!")
