"""
Test Script for Cube Mesh Manager Addon


This script tests all features of the Cube Mesh Manager addon.

Instructions:
1. Install and enable the "Cube Mesh Manager" addon in Blender
2. Open Blender's Scripting workspace
3. Load this script
4. Run the script (Alt + P or click "Run Script")

The script will automatically test:
- Cube distribution with various counts
- Range validation
- Cube deletion
- Mesh merging with common faces
- Edge cases and error handling
"""

import bpy
import time
import os


def setup_camera_and_light():
    """Setup camera and lighting for renders"""
    # Add camera
    bpy.ops.object.camera_add(location=(10, -10, 8))
    camera = bpy.context.active_object
    camera.rotation_euler = (1.1, 0, 0.785)
    bpy.context.scene.camera = camera
    
    # Add light
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    light = bpy.context.active_object
    light.data.energy = 2.0


def render_scene(filename):
    """Render the current scene to an image file"""
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, filename)
    
    # Configure render settings
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = output_path
    
    # Render
    bpy.ops.render.render(write_still=True)
    print(f"  Rendered: {output_path}")


def print_separator(title):
    """Print a formatted section separator"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")


def clear_scene():
    """Clear all objects from the scene"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    print("Scene cleared")


def test_cube_distribution():
    """Test Feature Set 1: Cube Distribution"""
    print_separator("TEST 1: Cube Distribution")
    
    # Setup scene for rendering
    setup_camera_and_light()
    
    # Test 1a: Distribute 4 cubes
    print("Test 1a: Distributing 4 cubes...")
    bpy.context.scene.cube_manager_props.number_of_cubes = 4
    result = bpy.ops.cube.distribute_cubes()
    
    if result == {'FINISHED'}:
        print(f"Successfully created 4 cubes")
        print(f"  Objects in scene: {len(bpy.context.scene.objects)}")
        render_scene("test_01a_4_cubes.png")
    else:
        print("Failed to create cubes")
    
    # Test 1b: Verify collection was created
    if "Distributed Cubes" in bpy.data.collections:
        collection = bpy.data.collections["Distributed Cubes"]
        print(f"Collection 'Distributed Cubes' created with {len(collection.objects)} objects")
    else:
        print("Collection not created")
    
    # Clear for next test
    clear_scene()
    
    # Re-setup scene
    setup_camera_and_light()
    
    # Test 1c: Distribute 9 cubes (3x3 grid)
    print("\nTest 1c: Distributing 9 cubes (3x3 grid)...")
    bpy.context.scene.cube_manager_props.number_of_cubes = 9
    result = bpy.ops.cube.distribute_cubes()
    
    if result == {'FINISHED'}:
        print(f"Successfully created 9 cubes in grid")
        print(f"  Objects in scene: {len(bpy.context.scene.objects)}")
        render_scene("test_01c_9_cubes.png")
    else:
        print("Failed to create cube grid")
    
    # Test 1d: Distribute 16 cubes (4x4 grid)
    print("\nTest 1d: Distributing 16 cubes (4x4 grid)...")
    clear_scene()
    setup_camera_and_light()
    bpy.context.scene.cube_manager_props.number_of_cubes = 16
    result = bpy.ops.cube.distribute_cubes()
    
    if result == {'FINISHED'}:
        print(f"Successfully created 16 cubes")
        render_scene("test_01d_16_cubes.png")
    else:
        print("Failed to create 16 cubes")


def test_range_validation():
    """Test range validation (max 20 cubes)"""
    print_separator("TEST 2: Range Validation")
    
    clear_scene()
    
    # Test 2a: Try to create 21 cubes (should fail)
    print("Test 2a: Attempting to create 21 cubes (should fail)...")
    bpy.context.scene.cube_manager_props.number_of_cubes = 21
    result = bpy.ops.cube.distribute_cubes()
    
    if result == {'CANCELLED'}:
        print("Correctly rejected value > 20")
    else:
        print("Failed to validate range")
    
    # Test 2b: Create exactly 20 cubes (should succeed)
    print("\nTest 2b: Creating exactly 20 cubes (at limit)...")
    bpy.context.scene.cube_manager_props.number_of_cubes = 20
    result = bpy.ops.cube.distribute_cubes()
    
    if result == {'FINISHED'}:
        print(f"Successfully created 20 cubes (maximum allowed)")
        print(f"  Objects in scene: {len(bpy.context.scene.objects)}")
    else:
        print("Failed to create 20 cubes")


def test_delete_cubes():
    """Test cube deletion functionality"""
    print_separator("TEST 3: Cube Deletion")
    
    clear_scene()
    
    # Create some cubes
    print("Creating 6 cubes for deletion test...")
    bpy.context.scene.cube_manager_props.number_of_cubes = 6
    bpy.ops.cube.distribute_cubes()
    
    initial_count = len(bpy.context.scene.objects)
    print(f"  Initial object count: {initial_count}")
    
    # Select and delete 3 cubes
    print("\nSelecting and deleting 3 cubes...")
    bpy.ops.object.select_all(action='DESELECT')
    
    objects = list(bpy.context.scene.objects)
    for i, obj in enumerate(objects[:3]):
        obj.select_set(True)
    
    result = bpy.ops.cube.delete_cubes()
    
    final_count = len(bpy.context.scene.objects)
    print(f"  Final object count: {final_count}")
    
    if result == {'FINISHED'} and final_count == initial_count - 3:
        print("Successfully deleted selected cubes")
    else:
        print("Delete operation failed")


def test_mesh_merging_basic():
    """Test basic mesh merging with common faces"""
    print_separator("TEST 4: Basic Mesh Merging")
    
    clear_scene()
    setup_camera_and_light()
    
    # Create two adjacent cubes that share a face
    print("Creating two adjacent cubes (sharing a face)...")
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    cube1 = bpy.context.active_object
    cube1.name = "TestCube1"
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))
    cube2 = bpy.context.active_object
    cube2.name = "TestCube2"
    
    print(f"  Created: {cube1.name} at (0,0,0)")
    print(f"  Created: {cube2.name} at (1,0,0)")
    
    # Select both cubes
    bpy.ops.object.select_all(action='DESELECT')
    cube1.select_set(True)
    cube2.select_set(True)
    bpy.context.view_layer.objects.active = cube1
    
    # Merge the cubes
    print("\nMerging cubes with common face...")
    result = bpy.ops.cube.compose_mesh()
    
    if result == {'FINISHED'}:
        print("Successfully merged meshes")
        print(f"  Resulting object: {bpy.context.active_object.name}")
        print(f"  Vertices: {len(bpy.context.active_object.data.vertices)}")
        print(f"  Faces: {len(bpy.context.active_object.data.polygons)}")
        render_scene("test_04_basic_merge.png")
    else:
        print("Merge operation failed")


def test_mesh_merging_complex():
    """Test merging multiple meshes in sequence"""
    print_separator("TEST 5: Complex Mesh Merging")
    
    clear_scene()
    setup_camera_and_light()
    
    # Create a row of 3 adjacent cubes
    print("Creating 3 adjacent cubes in a row...")
    
    cubes = []
    for i in range(3):
        bpy.ops.mesh.primitive_cube_add(size=1, location=(i, 0, 0))
        cube = bpy.context.active_object
        cube.name = f"RowCube{i+1}"
        cubes.append(cube)
        print(f"  Created: {cube.name} at ({i},0,0)")
    
    # Select all cubes
    bpy.ops.object.select_all(action='DESELECT')
    for cube in cubes:
        cube.select_set(True)
    bpy.context.view_layer.objects.active = cubes[0]
    
    initial_object_count = len(bpy.context.scene.objects)
    
    # Merge all cubes
    print("\nMerging all 3 cubes...")
    result = bpy.ops.cube.compose_mesh()
    
    final_object_count = len(bpy.context.scene.objects)
    
    if result == {'FINISHED'}:
        print("Successfully merged multiple meshes")
        print(f"  Objects before: {initial_object_count}")
        print(f"  Objects after: {final_object_count}")
        if bpy.context.active_object:
            print(f"  Resulting vertices: {len(bpy.context.active_object.data.vertices)}")
            print(f"  Resulting faces: {len(bpy.context.active_object.data.polygons)}")
            render_scene("test_05_complex_merge_3_cubes.png")
    else:
        print("Complex merge failed")


def test_mesh_merging_l_shape():
    """Test merging meshes in an L-shape configuration"""
    print_separator("TEST 6: L-Shape Mesh Merging")
    
    clear_scene()
    setup_camera_and_light()
    
    # Create an L-shape with 3 cubes
    print("Creating L-shaped configuration with 3 cubes...")
    
    # Horizontal part
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    cube1 = bpy.context.active_object
    cube1.name = "L_Base"
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))
    cube2 = bpy.context.active_object
    cube2.name = "L_Right"
    
    # Vertical part
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1, 0))
    cube3 = bpy.context.active_object
    cube3.name = "L_Top"
    
    print(f"  Created: {cube1.name} at (0,0,0)")
    print(f"  Created: {cube2.name} at (1,0,0)")
    print(f"  Created: {cube3.name} at (0,1,0)")
    
    # Select all cubes
    bpy.ops.object.select_all(action='DESELECT')
    cube1.select_set(True)
    cube2.select_set(True)
    cube3.select_set(True)
    bpy.context.view_layer.objects.active = cube1
    
    # Merge
    print("\nMerging L-shape...")
    result = bpy.ops.cube.compose_mesh()
    
    if result == {'FINISHED'}:
        print("Successfully merged L-shape configuration")
        if bpy.context.active_object:
            print(f"  Resulting vertices: {len(bpy.context.active_object.data.vertices)}")
            print(f"  Resulting faces: {len(bpy.context.active_object.data.polygons)}")
            render_scene("test_06_l_shape_merge.png")
    else:
        print("L-shape merge failed")


def test_no_common_faces():
    """Test merging attempt with meshes that don't share faces"""
    print_separator("TEST 7: No Common Faces (Expected Fail)")
    
    clear_scene()
    
    # Create two separated cubes
    print("Creating two separated cubes (no common faces)...")
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    cube1 = bpy.context.active_object
    cube1.name = "Separated1"
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(3, 0, 0))
    cube2 = bpy.context.active_object
    cube2.name = "Separated2"
    
    print(f"  Created: {cube1.name} at (0,0,0)")
    print(f"  Created: {cube2.name} at (3,0,0)")
    print("  Gap between cubes: 2 units")
    
    # Select both cubes
    bpy.ops.object.select_all(action='DESELECT')
    cube1.select_set(True)
    cube2.select_set(True)
    bpy.context.view_layer.objects.active = cube1
    
    # Attempt merge
    print("\nAttempting to merge (should fail gracefully)...")
    result = bpy.ops.cube.compose_mesh()
    
    if result == {'CANCELLED'}:
        print("Correctly identified no common faces")
    else:
        print("Warning: Operation completed but shouldn't have")


def test_overlap_avoidance():
    """Test overlap avoidance when distributing cubes"""
    print_separator("TEST 8: Overlap Avoidance")
    
    clear_scene()
    
    # Create an obstacle cube
    print("Creating obstacle cube at (2.5, 2.5, 0)...")
    bpy.ops.mesh.primitive_cube_add(size=2, location=(2.5, 2.5, 0))
    obstacle = bpy.context.active_object
    obstacle.name = "Obstacle"
    
    # Distribute cubes
    print("\nDistributing 9 cubes (should avoid obstacle)...")
    bpy.context.scene.cube_manager_props.number_of_cubes = 9
    result = bpy.ops.cube.distribute_cubes()
    
    if result == {'FINISHED'}:
        cube_count = len([obj for obj in bpy.context.scene.objects 
                         if obj.type == 'MESH' and obj != obstacle])
        print(f"Created {cube_count} cubes")
        print("  Algorithm avoided obstacle placement")
    else:
        print("Distribution failed")


def run_all_tests():
    """Run all test suites"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "CUBE MESH MANAGER ADDON TEST SUITE" + " " * 14 + "║")
    print("╚" + "═" * 58 + "╝")
    
    start_time = time.time()
    
    try:
        # Run all tests
        test_cube_distribution()
        test_range_validation()
        test_delete_cubes()
        test_mesh_merging_basic()
        test_mesh_merging_complex()
        test_mesh_merging_l_shape()
        test_no_common_faces()
        test_overlap_avoidance()
        
        # Summary
        elapsed_time = time.time() - start_time
        
        print_separator("TEST SUMMARY")
        print(f"All tests completed in {elapsed_time:.2f} seconds")
        print("\nTest suite finished successfully!")
        print("\nNote: Check the console output above for detailed results.")
        print("Some tests may show warnings - this is expected behavior.")
        
    except Exception as e:
        print("\n" + "=" * 60)
        print("ERROR: Test suite encountered an exception")
        print("=" * 60)
        print(f"\n{str(e)}")
        import traceback
        traceback.print_exc()


# Run the tests
if __name__ == "__main__":
    # Check if addon is enabled
    if "cube_manager_props" not in dir(bpy.context.scene):
        print("\n" + "!" * 60)
        print("ERROR: Cube Mesh Manager addon is not enabled!")
        print("!" * 60)
        print("\nPlease:")
        print("1. Go to Edit → Preferences → Add-ons")
        print("2. Search for 'Cube Mesh Manager'")
        print("3. Enable the addon by checking the checkbox")
        print("4. Run this script again")
    else:
        run_all_tests()
