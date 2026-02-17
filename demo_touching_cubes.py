import bpy

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
print(f"  This cube extends from -0.5 to +0.5 on all axes")

# Cube 2 touching on the right (at X=1)
bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))
cube2 = bpy.context.active_object
cube2.name = "Cube_Right"
print(f"\n✓ Created {cube2.name} at (1, 0, 0) with size=1")
print(f"  This cube extends from 0.5 to 1.5 on X axis")

print("\n" + "-"*60)
print("SHARED FACE DETAILS:")
print("-"*60)
print(f"Cube_Left right face is at X = 0.5")
print(f"Cube_Right left face is at X = 0.5")
print(f"✓ These faces are at THE SAME LOCATION - they share a face!")

# Deselect all
bpy.ops.object.select_all(action='DESELECT')

# Select both cubes
cube1.select_set(True)
cube2.select_set(True)
bpy.context.view_layer.objects.active = cube1

print("\n" + "="*60)
print("READY TO MERGE!")
print("="*60)
print("\nNow you can:")
print("1. Look in the sidebar (press N if not visible)")
print("2. Go to the 'Cube Manager' tab")
print("3. Click 'Compose Mesh' button")
print("\nExpected result:")
print("- The two cubes will merge into one object")
print("- The shared face between them will be deleted")
print("- You'll see a seamless merged object")
print("="*60 + "\n")
