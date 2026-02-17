# Blender Cube Mesh Manager

A Blender addon for distributing cubes in 2D grids and merging meshes with shared faces.

## Features
- Distribute 1-20 cubes in a 2D grid with input validation
- Prevents overlap with existing objects using collision detection
- Organizes cubes in a separate collection
- Merge selected meshes that share a common face, removing internal faces
- Simple UI panel for all actions in the 3D Viewport sidebar

## Installation
1. Download `cube_mesh_manager.py`
2. Open Blender, go to Edit > Preferences > Add-ons
3. Click Install, select the file, and enable the addon

## Usage
- Press `N` in the 3D Viewport, open the "Cube Manager" tab
- Enter a number (1-20) and click "Distribute Cubes"
- Select cubes and click "Delete Cubes" to remove them
- Select two or more touching cubes and click "Compose Mesh" to merge

## Technical Details
- Grid: m = ceil(sqrt(N)), n = ceil(N/m), spacing = 2.5 units
- Overlap: Axis-Aligned Bounding Box (AABB) collision detection
- Merge: Finds and removes shared faces using vertex comparison (tolerance 0.0001)
- Uses only Blender's built-in Python API (bpy, bmesh)

## Testing
Run all tests with:
```
/path/to/blender --background --python test_cube_manager.py
```

## Troubleshooting
- "Number is out of range": Enter 1-20
- "No meshes with common faces found": Ensure cubes are exactly touching
- Panel not visible: Press `N` and check addon is enabled

## Requirements
- Blender 3.0 or higher
- Python 3.x (bundled with Blender)

## Author
Aditya Sarna

## License
MIT License
