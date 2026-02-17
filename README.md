# Blender Cube Mesh Manager# Blender Cube Mesh Manager# Blender Cube Mesh Manager# Cube Mesh Manager - Blender Addon



A Blender addon for distributing cubes in 2D grids and merging meshes with shared faces.



## FeaturesA Blender addon for distributing cubes in 2D grids and merging meshes with shared faces.



### Cube Distribution

- Input validation for 1-20 cubes with error messages for out-of-range values

- Smart grid layout using near-square dimensions (m×n where m = ⌈√N⌉)![Blender Version](https://img.shields.io/badge/Blender-3.0%2B-orange)A Blender addon for distributing cubes in 2D grids and merging meshes with shared faces.A Blender addon for distributing cubes in 2D arrays and merging meshes with common faces.

- Automatic collection management for organized scene hierarchy

- AABB collision detection to prevent overlapping with existing objects![Python](https://img.shields.io/badge/Python-3.x-blue)

- Quick delete tool for selected objects

![License](https://img.shields.io/badge/License-MIT-green)

### Mesh Composition

- Detects meshes sharing common faces using vertex-level comparison

- Merges meshes and removes internal geometry automatically

- Processes multiple mesh pairs in a single operation## Overview![Blender Version](https://img.shields.io/badge/Blender-3.0%2B-orange)## Features

- Uses BMesh for precise face removal with 0.0001 unit tolerance



## Installation

**Cube Mesh Manager** distributes cubes in a 2D grid pattern, avoids overlaps with existing objects, and intelligently merges meshes that share common faces. Perfect for procedural modeling, architectural layouts, and mesh composition workflows.![Python](https://img.shields.io/badge/Python-3.x-blue)

### Method 1: Via Blender Preferences

1. Download `cube_mesh_manager.py`

2. Open Blender and go to Edit → Preferences → Add-ons

3. Click Install and select the downloaded file## Features![License](https://img.shields.io/badge/License-MIT-green)### Feature Set 1: Cube Distribution

4. Enable the addon by checking the checkbox



### Method 2: Manual Installation

1. Download `cube_mesh_manager.py`### Cube Distribution System- **Input Box**: Enter a natural number N (<20) to specify the number of cubes

2. Copy to Blender addons folder:

   - Windows: `%APPDATA%\Blender Foundation\Blender\{version}\scripts\addons\`- **Smart Grid Layout** - Automatically calculates near-square dimensions (m×n where m = ⌈√N⌉)

   - macOS: `~/Library/Application Support/Blender/{version}/scripts/addons/`

   - Linux: `~/.config/blender/{version}/scripts/addons/`- **Input Validation** - Accepts 1-20 cubes with "out of range" error for invalid inputs## 🎯 Overview- **Range Validation**: Pop-up warning if number exceeds 20

3. Restart Blender and enable in Preferences → Add-ons

- **Collection Management** - Organizes cubes in "Distributed Cubes" collection

## Usage

- **Overlap Avoidance** - AABB collision detection with 5×5 position search algorithm- **Smart Distribution**: Cubes are evenly distributed in a 2D array (m × n grid)

### Access Panel

Press `N` in 3D Viewport to open sidebar, then click the "Cube Manager" tab.- **Delete Tool** - Quick removal of selected objects



### Distribute Cubes**Cube Mesh Manager** distributes cubes in a 2D grid pattern, avoids overlaps with existing objects, and intelligently merges meshes that share common faces. Perfect for procedural modeling, architectural layouts, and mesh composition workflows.- **Automatic Collection**: Creates a "Distributed Cubes" collection for organization

1. Enter a number between 1-20 in the "Number of Meshes" field

2. Click "Distribute Cubes" button### Mesh Composition System

3. Cubes appear in a 2D grid with 2.5 unit spacing

- **Common Face Detection** - Vertex-level comparison with 0.0001 tolerance- **Overlap Avoidance**: Algorithm prevents new cubes from overlapping existing objects

### Merge Meshes

1. Position meshes so they share at least one face- **Seamless Merging** - Joins meshes and removes internal geometry

2. Select 2 or more mesh objects

3. Click "Compose Mesh" button- **Multi-Object Support** - Processes multiple mesh pairs automatically## ✨ Features- **Delete Function**: Button to delete selected cubes

4. Meshes merge and internal faces are removed

- **BMesh Integration** - Precise face removal using low-level mesh editing

### Delete Objects

1. Select one or more objects

2. Click "Delete Cubes" button

## Installation

## Testing

### 📦 Cube Distribution System### Feature Set 2: Mesh Composition

Run the test suite from command line:

### Method 1: Quick Install

```bash

/path/to/blender --background --python test_cube_manager.py1. Download [`cube_mesh_manager.py`](cube_mesh_manager.py)- **Smart Grid Layout** - Automatically calculates near-square dimensions (m×n where m = ⌈√N⌉)- **Merge Meshes**: Combines selected meshes with common faces into a single mesh

```

2. Open Blender → Edit → Preferences → Add-ons

Test coverage includes:

- Grid distribution (4, 9, 16, 20 cubes)3. Click **Install...** → Select the file → Enable checkbox- **Input Validation** - Accepts 1-20 cubes with "out of range" error for invalid inputs- **Common Face Detection**: Automatically identifies meshes sharing at least one face

- Input validation

- Basic and complex merging

- Overlap avoidance

- Delete functionality### Method 2: Manual Install- **Collection Management** - Organizes cubes in "Distributed Cubes" collection- **Smart Merging**: Merges common vertices and removes duplicate faces



## Technical Details```bash



### Grid Algorithm# Find your Blender addons folder:- **Overlap Avoidance** - AABB collision detection with 5×5 position search algorithm- **Clean Geometry**: Resulting mesh has no internal faces or duplicate vertices

```python

m = ceil(sqrt(N))      # Grid columns# Windows: %APPDATA%\Blender Foundation\Blender\{version}\scripts\addons\

rows = ceil(N / m)     # Grid rows

spacing = 2.5          # Units between cubes# macOS:   ~/Library/Application Support/Blender/{version}/scripts/addons/- **Delete Tool** - Quick removal of selected objects

```

# Linux:   ~/.config/blender/{version}/scripts/addons/

Examples:

- 4 cubes → 2×2 grid## Requirements

- 9 cubes → 3×3 grid  

- 10 cubes → 4×3 grid# Copy the addon file



### Collision Detectioncp cube_mesh_manager.py /path/to/blender/addons/### 🔗 Mesh Composition System

Uses AABB (Axis-Aligned Bounding Box) method. Two boxes do not overlap if:

``````

new_max_x < min_x OR new_min_x > max_x OR

new_max_y < min_y OR new_min_y > max_y OR- **Common Face Detection** - Vertex-level comparison with 0.0001 tolerance- **Blender Version**: 3.0.0 or higher

new_max_z < min_z OR new_min_z > max_z

```## Usage



If none of these conditions are true, boxes overlap.- **Seamless Merging** - Joins meshes and removes internal geometry- **Python**: Comes bundled with Blender (no external installation needed)



### Face Matching### Access the Panel

1. Convert all vertices to world space

2. Compare faces vertex-by-vertexPress `N` in 3D Viewport → Click **"Cube Manager"** tab- **Multi-Object Support** - Processes multiple mesh pairs automatically- **Operating System**: Windows, macOS, or Linux

3. Vertices match if distance < 0.0001 units

4. Handles different vertex orderings



### Merge Process### Distribute Cubes- **BMesh Integration** - Precise face removal using low-level mesh editing

1. Find common faces before joining

2. Join objects using bpy.ops.object.join()1. Enter number (1-20) in "Number of Meshes"

3. Remove duplicate vertices with remove_doubles(0.0001)

4. Delete internal faces using BMesh2. Click **"Distribute Cubes"**## Installation



## Performance3. Cubes appear in 2D grid with 2.5 unit spacing



- Grid Distribution: O(N) where N = number of cubes## 📥 Installation

- Overlap Check: O(N×M) where M = existing objects

- Face Detection: O(F₁×F₂) where F = faces per object### Merge Meshes

- Memory: Minimal, stores only bounding boxes during distribution

1. Position meshes so they share a face### Method 1: Direct Installation (Recommended)

## Requirements

2. Select 2+ mesh objects

- Blender 3.0 or higher

- Python 3.x (bundled with Blender)3. Click **"Compose Mesh"**### Method 1: Quick Install

- No external dependencies

4. Internal faces automatically removed

## Project Structure

1. Download [`cube_mesh_manager.py`](cube_mesh_manager.py)1. Download the `cube_mesh_manager.py` file

```

cube_mesh_manager_addon/### Delete Objects

├── cube_mesh_manager.py      # Main addon file

├── test_cube_manager.py      # Test suite1. Select one or more objects2. Open Blender → Edit → Preferences → Add-ons2. Open Blender

├── demo_with_addon.py        # Demo script

├── README.md                 # Documentation2. Click **"Delete Cubes"**

├── requirements.txt          # Empty

└── .gitignore               # Git config3. Click **Install...** → Select the file → Enable checkbox3. Go to `Edit` → `Preferences` → `Add-ons`

```

## Testing

## Troubleshooting

4. Click `Install...` button at the top

**"The number is out of range"**  

Enter a value between 1 and 20.Run the complete test suite:



**"No meshes with common faces found"**  ### Method 2: Manual Install5. Navigate to and select `cube_mesh_manager.py`

Ensure meshes are touching. Size 1 cubes need exactly 1 unit spacing.

```bash

**Cubes overlap existing objects**  

Algorithm searches a 5×5 grid for free space. Move existing objects or accept some skipped cubes.# From command line (background mode)```bash6. Enable the addon by checking the checkbox next to "Object: Cube Mesh Manager"



**Panel not visible**  /path/to/blender --background --python test_cube_manager.py

Press N to show sidebar and verify addon is enabled in Preferences.

# Find your Blender addons folder:7. Click the hamburger menu (three lines) and select "Save Preferences" to keep it enabled

## License

# Or install and run interactively

MIT License

# See test_cube_manager.py for 8 comprehensive tests# Windows: %APPDATA%\Blender Foundation\Blender\{version}\scripts\addons\

## Author

```

Aditya Sarna

# macOS:   ~/Library/Application Support/Blender/{version}/scripts/addons/### Method 2: Manual Installation

## Version

**Test Coverage:**

1.0.0 (February 2026)

- Grid distribution (4, 9, 16, 20 cubes)# Linux:   ~/.config/blender/{version}/scripts/addons/

- Input validation (out of range)

- Basic merge (2 cubes)1. Download the `cube_mesh_manager.py` file

- Complex merge (3 cubes, L-shape)

- Overlap avoidance# Copy the addon file2. Locate your Blender addons folder:

- Delete functionality

cp cube_mesh_manager.py /path/to/blender/addons/   - **Windows**: `%APPDATA%\Blender Foundation\Blender\{version}\scripts\addons\`

## Technical Details

```   - **macOS**: `~/Library/Application Support/Blender/{version}/scripts/addons/`

### Grid Distribution Algorithm

```python   - **Linux**: `~/.config/blender/{version}/scripts/addons/`

m = ceil(sqrt(N))      # Grid columns

rows = ceil(N / m)     # Grid rows## 🚀 Usage3. Copy `cube_mesh_manager.py` to the addons folder

spacing = 2.5          # Units between cubes

```4. Open Blender and go to `Edit` → `Preferences` → `Add-ons`



**Examples:**### Access the Panel5. Search for "Cube Mesh Manager"

- 4 cubes → 2×2 grid

- 9 cubes → 3×3 gridPress `N` in 3D Viewport → Click **"Cube Manager"** tab6. Enable the addon by checking the checkbox

- 10 cubes → 4×3 grid

7. Save preferences

### AABB Collision Detection

```python### Distribute Cubes

# Two boxes don't overlap if any of:

new_max_x < min_x  OR  new_min_x > max_x  OR1. Enter number (1-20) in "Number of Meshes"## Usage

new_max_y < min_y  OR  new_min_y > max_y  OR

new_max_z < min_z  OR  new_min_z > max_z2. Click **"Distribute Cubes"**



# If none are true → Overlap detected!3. Cubes appear in 2D grid with 2.5 unit spacing### Accessing the Addon

```



### Face Matching Process

1. Convert vertices to world space coordinates### Merge MeshesAfter installation, access the addon panel:

2. Compare each face vertex-by-vertex

3. Match if distance < 0.0001 units1. Position meshes so they share a face1. Open the 3D Viewport

4. Handle different vertex orderings

2. Select 2+ mesh objects2. Press `N` to open the sidebar (if not already visible)

### Merge Pipeline

1. **Detect** - Find common faces before joining3. Click **"Compose Mesh"**3. Click on the `Cube Manager` tab

2. **Join** - Combine objects with `bpy.ops.object.join()`

3. **Clean** - Remove duplicate vertices (`remove_doubles`)4. Internal faces automatically removed

4. **Remove** - Delete internal faces with BMesh

### Feature Set 1: Distributing Cubes

## Performance

### Delete Objects

- **Grid Distribution:** O(N) where N = number of cubes

- **Overlap Check:** O(N×M) where M = existing objects1. Select one or more objects1. **Set Number of Cubes**:

- **Face Detection:** O(F₁×F₂) where F = faces per object

- **Memory:** Minimal - stores only bounding boxes during distribution2. Click **"Delete Cubes"**   - Enter a number (1-20) in the "Number of Meshes" field



## Requirements   - Numbers above 20 will show an error message



- **Blender:** 3.0 or higher## 🧪 Testing

- **Python:** 3.x (bundled with Blender)

- **Dependencies:** None (uses only built-in `bpy` and `bmesh`)2. **Distribute Cubes**:



## Project StructureRun the complete test suite:   - Click the "Distribute Cubes" button



```   - Cubes will be arranged in an optimal 2D grid pattern

cube_mesh_manager_addon/

├── cube_mesh_manager.py      # Main addon (438 lines)```bash   - Each cube has dimensions of 1×1×1 Blender units

├── test_cube_manager.py      # Test suite with rendering

├── demo_with_addon.py        # Interactive demo launcher# From command line (background mode)   - Cubes are automatically added to "Distributed Cubes" collection

├── README.md                 # Documentation

├── requirements.txt          # Empty (no dependencies)/path/to/blender --background --python test_cube_manager.py   - The algorithm avoids overlapping with existing objects

└── .gitignore               # Git configuration

```



## Troubleshooting# Or install and run interactively3. **Delete Cubes**:



| Issue | Solution |# See test_cube_manager.py for 8 comprehensive tests   - Select the cubes you want to delete in the 3D viewport

|-------|----------|

| "Number is out of range" | Enter value between 1-20 |```   - Click the "Delete Cubes" button

| "No common faces found" | Ensure meshes are touching (size=1 cubes need 1 unit spacing) |

| Cubes overlap existing objects | Algorithm searches 5×5 grid; move objects or accept skipped cubes |   - Selected objects will be removed

| Panel not visible | Press `N` to show sidebar, check addon is enabled |

**Test Coverage:**

## License

-  Grid distribution (4, 9, 16, 20 cubes)### Feature Set 2: Merging Meshes

MIT License - Feel free to use and modify

-  Input validation (out of range)

## Author

-  Basic merge (2 cubes)1. **Select Meshes**:

**Aditya Sarna**

-  Complex merge (3 cubes, L-shape)   - Select 2 or more mesh objects in the 3D viewport

## Version History

-  Overlap avoidance   - Meshes must share at least one common face to be merged

### v1.0.0 (2026-02-17)

- Full feature implementation-  Delete functionality

- 8-test comprehensive suite

- Complete documentation2. **Compose Mesh**:

- Visual proof with rendered images

## 🔧 Technical Details   - Click the "Compose Mesh" button

---

   - The addon will:

**Made with love for Blender 3D**

### Grid Distribution Algorithm     - Detect meshes with common faces

```python     - Merge them into a single object

m = ceil(sqrt(N))      # Grid columns     - Remove duplicate vertices

rows = ceil(N / m)     # Grid rows     - Delete internal (common) faces

spacing = 2.5          # Units between cubes     - Create clean, unified geometry

```

**Note**: For successful merging, two meshes must have at least one face with identical vertex positions.

**Examples:**

- 4 cubes → 2×2 grid## Custom Test Script

- 9 cubes → 3×3 grid

- 10 cubes → 4×3 gridA test script is provided to demonstrate the addon's functionality programmatically.



### AABB Collision Detection### Running the Test Script

```python

# Two boxes don't overlap if any of:1. Open Blender

new_max_x < min_x  OR  new_min_x > max_x  OR2. Make sure the addon is installed and enabled

new_max_y < min_y  OR  new_min_y > max_y  OR3. Switch to the `Scripting` workspace

new_max_z < min_z  OR  new_min_z > max_z4. Open the `test_cube_manager.py` file

5. Click `Run Script` or press `Alt + P`

# If none are true → Overlap detected!

```The test script will:

- Create a distribution of cubes

### Face Matching Process- Select specific cubes

1. Convert vertices to world space coordinates- Merge adjacent cubes with common faces

2. Compare each face vertex-by-vertex- Demonstrate all major features

3. Match if distance < 0.0001 units

4. Handle different vertex orderings### Test Script Code



### Merge Pipeline```python

1. **Detect** - Find common faces before joiningimport bpy

2. **Join** - Combine objects with `bpy.ops.object.join()`

3. **Clean** - Remove duplicate vertices (`remove_doubles`)# Clear existing objects

4. **Remove** - Delete internal faces with BMeshbpy.ops.object.select_all(action='SELECT')

bpy.ops.object.delete()

##  Performance

# Test 1: Distribute 9 cubes

- **Grid Distribution:** O(N) where N = number of cubesprint("Test 1: Distributing 9 cubes...")

- **Overlap Check:** O(N×M) where M = existing objectsbpy.context.scene.cube_manager_props.number_of_cubes = 9

- **Face Detection:** O(F₁×F₂) where F = faces per objectbpy.ops.cube.distribute_cubes()

- **Memory:** Minimal - stores only bounding boxes during distribution

# Test 2: Create two adjacent cubes manually for merging test

## 🛠️ Requirementsprint("Test 2: Creating adjacent cubes for merge test...")

bpy.ops.object.select_all(action='DESELECT')

- **Blender:** 3.0 or higher

- **Python:** 3.x (bundled with Blender)# Create first cube

- **Dependencies:** None (uses only built-in `bpy` and `bmesh`)bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))

cube1 = bpy.context.active_object

##  Project Structurecube1.name = "MergeCube1"



```# Create adjacent cube (shares a face)

cube_mesh_manager_addon/bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))

├── cube_mesh_manager.py      # Main addon (438 lines)cube2 = bpy.context.active_object

├── test_cube_manager.py      # Test suite with renderingcube2.name = "MergeCube2"

├── demo_with_addon.py        # Interactive demo launcher

├── README.md                 # Documentation# Select both cubes

├── requirements.txt          # Empty (no dependencies)cube1.select_set(True)

└── .gitignore               # Git configurationcube2.select_set(True)

```bpy.context.view_layer.objects.active = cube1



##  Troubleshooting# Test 3: Merge the adjacent cubes

print("Test 3: Merging adjacent cubes...")

| Issue | Solution |bpy.ops.cube.compose_mesh()

|-------|----------|

| "Number is out of range" | Enter value between 1-20 |print("All tests completed!")

| "No common faces found" | Ensure meshes are touching (size=1 cubes need 1 unit spacing) |```

| Cubes overlap existing objects | Algorithm searches 5×5 grid; move objects or accept skipped cubes |

| Panel not visible | Press `N` to show sidebar, check addon is enabled |## Technical Details



##  License### Cube Distribution Algorithm



MIT License - Feel free to use and modify- Calculates optimal grid dimensions (m × n) to fit N cubes

- Uses `m = ceil(sqrt(N))` for nearly square arrangements

##  Author- Spacing between cubes: 2.5 Blender units

- Collision detection checks against existing objects

**Aditya Sarna**- Falls back to offset positions if overlaps detected



## Version History### Mesh Merging Algorithm



### v1.0.0 (2026-02-17)1. **Common Face Detection**:

-  Full feature implementation   - Converts vertex positions to world space

-  8-test comprehensive suite   - Compares faces between meshes with tolerance of 0.0001 units

-  Complete documentation   - Identifies matching vertex sets

-  Visual proof with rendered images

2. **Merging Process**:

---   - Joins objects using Blender's join operator

   - Removes duplicate vertices with merge threshold

**Made with  for Blender 3D**   - Identifies and removes internal faces

   - Uses BMesh for precise face removal

### Data Structures

- Uses Blender's native mesh data structures
- BMesh for advanced mesh editing
- World space transformations for accurate comparisons

## Troubleshooting

### Addon Not Visible
- Ensure you saved preferences after enabling
- Check that you're in the 3D Viewport
- Press `N` to toggle sidebar visibility
- Look for "Cube Manager" tab

### "Number is out of range" Error
- Enter a value between 1 and 20
- The field accepts only integers

### Merge Not Working
- Ensure selected objects are mesh objects
- Verify meshes share at least one common face
- Check that faces are perfectly aligned (within 0.0001 units)
- Try applying transformations first (`Ctrl + A` → All Transforms)

### Cubes Overlapping
- The overlap avoidance has a search radius of 5 positions
- If scene is very crowded, some overlap may occur
- Manually adjust positions if needed

## Development

### File Structure
```
cube_mesh_manager/
├── cube_mesh_manager.py    # Main addon file
├── requirements.txt         # Dependencies (none required)
├── README.md               # This file
└── test_cube_manager.py    # Test script
```

### Modifying the Addon

To modify the addon:
1. Edit `cube_mesh_manager.py`
2. In Blender, go to `Edit` → `Preferences` → `Add-ons`
3. Find "Cube Mesh Manager"
4. Click the refresh button or restart Blender
5. Test your changes

### Key Functions

- `CUBE_OT_distribute.execute()`: Handles cube distribution
- `CUBE_OT_compose_mesh.merge_meshes()`: Merges two meshes
- `have_common_face()`: Detects common faces between meshes
- `remove_internal_faces()`: Removes duplicate faces after merge

## License

This addon is provided as-is for educational and practical use in Blender.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review the test script for usage examples
3. Examine the code comments for implementation details

## Version History

- **v1.0.0** (2026-02-02):
  - Initial release
  - Cube distribution with range validation
  - Overlap avoidance algorithm
  - Mesh merging with common face detection
  - Automatic collection management
  - Delete selected cubes functionality

## Credits

Created as a demonstration of Blender addon development with Python.
