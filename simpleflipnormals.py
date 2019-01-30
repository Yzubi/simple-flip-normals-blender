import bpy
for bpy.context.scene.objects.active in bpy.context.selected_objects:
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.flip_normals()
    bpy.ops.object.mode_set()
