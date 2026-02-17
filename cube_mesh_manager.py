bl_info = {
    "name": "Cube Mesh Manager",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Cube Manager",
    "description": "Distribute cubes in 2D array and merge meshes with common faces",
    "category": "Object",
}

import bpy
import bmesh
import math
from bpy.props import IntProperty
from bpy.types import Panel, Operator, PropertyGroup




class CubeManagerProperties(PropertyGroup):
    """Properties for the Cube Manager addon"""
    
    number_of_cubes: IntProperty(
        name="Number of Meshes",
        description="Number of cubes to distribute (max 20)",
        default=4,
        min=1,
        max=20
    )




class CUBE_OT_distribute(Operator):
    """Distribute N cubes in a 2D array"""
    bl_idname = "cube.distribute_cubes"
    bl_label = "Distribute Cubes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.cube_manager_props
        n = props.number_of_cubes
        
        # Validate input
        if n > 20:
            self.report({'ERROR'}, "The number is out of range")
            return {'CANCELLED'}
        
        # Calculate grid dimensions (as square as possible)
        m = math.ceil(math.sqrt(n))
        cols = m
        rows = math.ceil(n / m)
        
        # Create or get collection
        collection_name = "Distributed Cubes"
        if collection_name in bpy.data.collections:
            collection = bpy.data.collections[collection_name]
        else:
            collection = bpy.data.collections.new(collection_name)
            context.scene.collection.children.link(collection)
        
        # Get existing objects to avoid overlap
        existing_bounds = []
        for obj in context.scene.objects:
            if obj.type == 'MESH':
                existing_bounds.append(self.get_object_bounds(obj))
        
        # Create cubes
        spacing = 2.5  # Space between cubes
        created_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if created_count >= n:
                    break
                
                # Calculate position
                x = j * spacing
                y = i * spacing
                z = 0
                
                # Check for overlap with existing objects
                position = (x, y, z)
                if self.check_overlap(position, 1.0, existing_bounds):
                    # Try to find a non-overlapping position
                    position = self.find_non_overlapping_position(
                        x, y, z, 1.0, existing_bounds, spacing
                    )
                    if position is None:
                        continue
                    x, y, z = position
                
                # Create cube
                bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))
                cube = context.active_object
                cube.name = f"Cube.{created_count:03d}"
                
                # Add to collection
                if cube.name in context.scene.collection.objects:
                    context.scene.collection.objects.unlink(cube)
                if cube.name not in collection.objects:
                    collection.objects.link(cube)
                
                # Add to existing bounds
                existing_bounds.append(self.get_object_bounds(cube))
                
                created_count += 1
            
            if created_count >= n:
                break
        
        self.report({'INFO'}, f"Created {created_count} cubes in {rows}x{cols} grid")
        return {'FINISHED'}
    
    def get_object_bounds(self, obj):
        """Get the bounding box of an object in world space"""
        if obj.type != 'MESH':
            return None
        
        bbox_corners = [obj.matrix_world @ mathutils.Vector(corner) 
                       for corner in obj.bound_box]
        
        min_x = min(v.x for v in bbox_corners)
        max_x = max(v.x for v in bbox_corners)
        min_y = min(v.y for v in bbox_corners)
        max_y = max(v.y for v in bbox_corners)
        min_z = min(v.z for v in bbox_corners)
        max_z = max(v.z for v in bbox_corners)
        
        return (min_x, max_x, min_y, max_y, min_z, max_z)
    
    def check_overlap(self, position, size, existing_bounds):
        """Check if a cube at position would overlap with existing objects"""
        half_size = size / 2
        x, y, z = position
        
        new_min_x = x - half_size
        new_max_x = x + half_size
        new_min_y = y - half_size
        new_max_y = y + half_size
        new_min_z = z - half_size
        new_max_z = z + half_size
        
        for bounds in existing_bounds:
            if bounds is None:
                continue
            
            min_x, max_x, min_y, max_y, min_z, max_z = bounds
            
            # Check if bounding boxes overlap
            if not (new_max_x < min_x or new_min_x > max_x or
                    new_max_y < min_y or new_min_y > max_y or
                    new_max_z < min_z or new_min_z > max_z):
                return True
        
        return False
    
    def find_non_overlapping_position(self, x, y, z, size, existing_bounds, spacing):
        """Try to find a non-overlapping position nearby"""
        search_radius = 5
        
        for offset_x in range(-search_radius, search_radius + 1):
            for offset_y in range(-search_radius, search_radius + 1):
                new_x = x + offset_x * spacing
                new_y = y + offset_y * spacing
                new_pos = (new_x, new_y, z)
                
                if not self.check_overlap(new_pos, size, existing_bounds):
                    return new_pos
        
        return None


class CUBE_OT_delete(Operator):
    """Delete selected cubes"""
    bl_idname = "cube.delete_cubes"
    bl_label = "Delete Cubes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selected = context.selected_objects
        
        if not selected:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        count = len(selected)
        bpy.ops.object.delete()
        
        self.report({'INFO'}, f"Deleted {count} object(s)")
        return {'FINISHED'}




class CUBE_OT_compose_mesh(Operator):
    """Merge selected meshes with common faces"""
    bl_idname = "cube.compose_mesh"
    bl_label = "Compose Mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selected = [obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if len(selected) < 2:
            self.report({'ERROR'}, "Select at least 2 mesh objects")
            return {'CANCELLED'}
        
        # Process meshes pairwise
        merged_any = False
        
        while len(selected) > 1:
            obj1 = selected[0]
            merged_with_any = False
            
            for i in range(1, len(selected)):
                obj2 = selected[i]
                
                # Check if meshes have common faces
                if self.have_common_face(obj1, obj2):
                    # Merge the meshes
                    self.merge_meshes(context, obj1, obj2)
                    selected.remove(obj2)
                    merged_with_any = True
                    merged_any = True
                    break
            
            if not merged_with_any:
                # obj1 cannot be merged with any remaining objects
                selected.remove(obj1)
        
        if merged_any:
            self.report({'INFO'}, "Meshes merged successfully")
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No meshes with common faces found")
            return {'CANCELLED'}
    
    def have_common_face(self, obj1, obj2):
        """Check if two meshes have at least one common face"""
        # Get world space vertex positions
        verts1 = self.get_world_vertices(obj1)
        verts2 = self.get_world_vertices(obj2)
        
        # Get face vertex indices
        faces1 = self.get_face_vertices(obj1)
        faces2 = self.get_face_vertices(obj2)
        
        tolerance = 0.0001
        
        # Check each face in obj1 against each face in obj2
        for face1_indices in faces1:
            face1_verts = [verts1[i] for i in face1_indices]
            
            for face2_indices in faces2:
                face2_verts = [verts2[i] for i in face2_indices]
                
                # Check if faces have same vertices (same face)
                if self.faces_match(face1_verts, face2_verts, tolerance):
                    return True
        
        return False
    
    def get_world_vertices(self, obj):
        """Get all vertices in world space"""
        return [obj.matrix_world @ v.co for v in obj.data.vertices]
    
    def get_face_vertices(self, obj):
        """Get list of vertex indices for each face"""
        return [[v for v in poly.vertices] for poly in obj.data.polygons]
    
    def faces_match(self, verts1, verts2, tolerance):
        """Check if two faces have the same vertices"""
        if len(verts1) != len(verts2):
            return False
        
        # For each vertex in face1, check if there's a matching vertex in face2
        matched = [False] * len(verts2)
        
        for v1 in verts1:
            found = False
            for i, v2 in enumerate(verts2):
                if not matched[i] and (v1 - v2).length < tolerance:
                    matched[i] = True
                    found = True
                    break
            
            if not found:
                return False
        
        return all(matched)
    
    def merge_meshes(self, context, obj1, obj2):
        """Merge obj2 into obj1, removing common faces and vertices"""
        # Deselect all
        bpy.ops.object.select_all(action='DESELECT')
        
        # Get common face data before joining
        common_faces = self.find_common_faces(obj1, obj2)
        
        # Select both objects
        obj1.select_set(True)
        obj2.select_set(True)
        context.view_layer.objects.active = obj1
        
        # Join objects
        bpy.ops.object.join()
        
        # Now remove duplicate vertices and faces
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Remove doubles (merges vertices at same location)
        bpy.ops.mesh.remove_doubles(threshold=0.0001)
        
        # Deselect all
        bpy.ops.mesh.select_all(action='DESELECT')
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Remove internal faces (faces that were common)
        self.remove_internal_faces(obj1, common_faces)
        
        return obj1
    
    def find_common_faces(self, obj1, obj2):
        """Find faces that are common between two objects"""
        verts1 = self.get_world_vertices(obj1)
        verts2 = self.get_world_vertices(obj2)
        
        faces1 = self.get_face_vertices(obj1)
        faces2 = self.get_face_vertices(obj2)
        
        common = []
        tolerance = 0.0001
        
        for face1_indices in faces1:
            face1_verts = [verts1[i] for i in face1_indices]
            
            for face2_indices in faces2:
                face2_verts = [verts2[i] for i in face2_indices]
                
                if self.faces_match(face1_verts, face2_verts, tolerance):
                    common.append(face1_verts)
        
        return common
    
    def remove_internal_faces(self, obj, common_face_verts):
        """Remove faces that match the common face vertices"""
        if not common_face_verts:
            return
        
        bpy.ops.object.mode_set(mode='EDIT')
        bm = bmesh.from_edit_mesh(obj.data)
        
        tolerance = 0.0001
        faces_to_remove = []
        
        # Find faces to remove
        for face in bm.faces:
            face_verts = [obj.matrix_world @ v.co for v in face.verts]
            
            for common_verts in common_face_verts:
                if self.faces_match(face_verts, common_verts, tolerance):
                    faces_to_remove.append(face)
                    break
        
        # Remove faces
        for face in faces_to_remove:
            bm.faces.remove(face)
        
        bmesh.update_edit_mesh(obj.data)
        bpy.ops.object.mode_set(mode='OBJECT')




class CUBE_PT_main_panel(Panel):
    """Main panel for Cube Manager"""
    bl_label = "Cube Manager"
    bl_idname = "CUBE_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Cube Manager'
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.cube_manager_props
        
        # Feature Set 1
        box = layout.box()
        box.label(text="Task 1", icon='CUBE')
        
        box.prop(props, "number_of_cubes")
        box.operator("cube.distribute_cubes", icon='GRID')
        box.operator("cube.delete_cubes", icon='TRASH')
        
        layout.separator()
        
        # Feature Set 2
        box = layout.box()
        box.label(text="Mesh Composition", icon='MOD_BOOLEAN')
        box.operator("cube.compose_mesh", icon='AUTOMERGE_ON')




classes = (
    CubeManagerProperties,
    CUBE_OT_distribute,
    CUBE_OT_delete,
    CUBE_OT_compose_mesh,
    CUBE_PT_main_panel,
)


def register():
    # Import mathutils here to avoid issues
    global mathutils
    import mathutils
    
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.cube_manager_props = bpy.props.PointerProperty(
        type=CubeManagerProperties
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.cube_manager_props


if __name__ == "__main__":
    register()
