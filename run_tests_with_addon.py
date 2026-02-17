
import bpy
import sys
import os

# Get the addon directory
addon_dir = os.path.dirname(os.path.abspath(__file__))
addon_file = os.path.join(addon_dir, "cube_mesh_manager.py")

print(f"Installing addon from: {addon_file}")

# Install the addon
try:
    bpy.ops.preferences.addon_install(filepath=addon_file)
    print("Addon installed")
except Exception as e:
    print(f"Install failed: {e}")
    sys.exit(1)

# Enable the addon
addon_module = "cube_mesh_manager"
try:
    bpy.ops.preferences.addon_enable(module=addon_module)
    print(f"Addon '{addon_module}' enabled")
except Exception as e:
    print(f"Enable failed: {e}")
    sys.exit(1)

# Now run the test script
test_script = os.path.join(addon_dir, "test_cube_manager.py")
print(f"\n{'='*60}")
print("Running tests...")
print('='*60)

with open(test_script, 'r') as f:
    test_code = f.read()

exec(test_code)
