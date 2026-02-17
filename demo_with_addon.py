import bpy
import os

# Get the addon file path
addon_file = "/Users/adityasarna/Downloads/cube_mesh_manager_addon/cube_mesh_manager.py"

print("\n" + "="*60)
print("INSTALLING ADDON...")
print("="*60)

# Install the addon
try:
    bpy.ops.preferences.addon_install(filepath=addon_file)
    print(f"✓ Addon installed from: {addon_file}")
except Exception as e:
    print(f"Note: {e}")

# Enable the addon
addon_name = "cube_mesh_manager"
try:
    bpy.ops.preferences.addon_enable(module=addon_name)
    print(f"✓ Addon '{addon_name}' enabled")
except Exception as e:
    print(f"Note: {e}")

# Save preferences
bpy.ops.wm.save_userpref()
print("✓ Preferences saved")

# Clean scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("\n" + "="*60)
print("CREATING TOUCHING CUBES FOR MERGE DEMO")
print("="*60)

# Create two cubes that TOUCH (share a face)
# Cube 1 at origin
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
cube1 = bpy.context.active_object
cube1.name = "Cube_Left"
print(f"\n✓ Created {cube1.name} at (0, 0, 0) with size=1")

# Cube 2 touching on the right (at X=1)
bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))
cube2 = bpy.context.active_object
cube2.name = "Cube_Right"
print(f"✓ Created {cube2.name} at (1, 0, 0) with size=1")

print("\n✓ These cubes share a face at X = 0.5")

# Deselect all
bpy.ops.object.select_all(action='DESELECT')

# Select both cubes
cube1.select_set(True)
cube2.select_set(True)
bpy.context.view_layer.objects.active = cube1

print("\n" + "="*60)
print("ADDON READY - CUBES SELECTED!")
print("="*60)
print("\n📋 INSTRUCTIONS:")
print("1. Press 'N' to open the sidebar (if not visible)")
print("2. Click on the 'Cube Manager' tab")
print("3. Click 'Compose Mesh' button")
print("\n✨ Expected: Two cubes merge into one seamless object!")
print("="*60 + "\n")
