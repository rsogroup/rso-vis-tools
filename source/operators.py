import math
import bpy


class SwapSelectedOperator(bpy.types.Operator):
    bl_idname = "object.rso_swap_material_selected"
    bl_label = "Material der ausgewählten Objekte tauschen"

    def execute(self, context):
        old_material = bpy.data.materials.get(context.scene.rso_src_mat.name)
        new_material = bpy.data.materials.get(context.scene.rso_dst_mat.name)

        if not old_material or not new_material:
            self.report({'WARNING'}, "Invalid materials selected!")
            return {'CANCELLED'}

        for obj in bpy.context.selected_objects:
            for slot in obj.material_slots:
                if slot.material == old_material:
                    slot.material = new_material

        return {'FINISHED'}


class SwapOperator(bpy.types.Operator):
    bl_idname = "object.rso_swap_material"
    bl_label = "Material aller Objekte tauschen"

    def execute(self, context):
        old_material = bpy.data.materials.get(context.scene.rso_src_mat.name)
        new_material = bpy.data.materials.get(context.scene.rso_dst_mat.name)

        if not old_material or not new_material:
            self.report({'WARNING'}, "Invalid materials selected!")
            return {'CANCELLED'}

        for obj in bpy.context.scene.objects:
            for slot in obj.material_slots:
                if slot.material == old_material:
                    slot.material = new_material

        return {'FINISHED'}


class SelectSrcMaterialOperator(bpy.types.Operator):
    """Wählt das Material des aktuell ausgewählten Objekts aus."""
    bl_idname = "material.rso_select_src_material"
    bl_label = "Auswahl"

    def execute(self, context):
        obj = context.active_object
        mat_length = len(obj.material_slots)

        if mat_length < 1:
            return {"FINISHED"}

        current_index = obj.active_material_index
        mat = obj.active_material

        if not mat:
            return {"FINISHED"}

        if mat == context.scene.rso_src_mat:
            obj.active_material_index = (current_index + 1) % mat_length
            mat = obj.active_material

        context.scene.rso_src_mat = mat
        return {'FINISHED'}


class SelectDstMaterialOperator(bpy.types.Operator):
    """Wählt das Material des aktuell ausgewählten Objekts aus."""
    bl_idname = "material.rso_select_dst_material"
    bl_label = "Auswahl"

    def execute(self, context):
        obj = context.active_object
        mat_length = len(obj.material_slots)

        if mat_length < 1:
            return {"FINISHED"}

        current_index = obj.active_material_index
        mat = obj.active_material

        if not mat:
            return {"FINISHED"}

        if mat == context.scene.rso_dst_mat:
            obj.active_material_index = (current_index + 1) % mat_length
            mat = obj.active_material

        context.scene.rso_dst_mat = mat
        return {'FINISHED'}


class RotateMapOperator(bpy.types.Operator):
    """Dreht das Mapping um 90 Grad."""
    bl_idname = "object.rso_rotate_map"
    bl_label = "Map drehen"

    def execute(self, context):

        angle = math.radians(90)

        prev_mode = context.mode

        for obj in bpy.context.selected_objects:
            if obj.type != 'MESH':
                continue

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.object.mode_set(mode='OBJECT')

            for uv_layer in obj.data.uv_layers:
                for uv_data in uv_layer.data:
                    x, y = uv_data.uv
                    new_x = x * math.cos(angle) - y * math.sin(angle)
                    new_y = x * math.sin(angle) + y * math.cos(angle)
                    uv_data.uv = (new_x, new_y)

            bpy.ops.object.mode_set(mode=prev_mode)

        return {'FINISHED'}


class CopyMeshDataOperator(bpy.types.Operator):
    """Trennt die Mesh Daten."""
    bl_idname = "object.rso_copy_mesh_data"
    bl_label = "Objekt trennen"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type != 'MESH':
                continue

            shared_users = len(
                [o for o in bpy.data.objects if o.data == obj.data])

            # Only copy the data, if it is shared with other objects
            if shared_users > 1:
                obj.data = obj.data.copy()

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SwapSelectedOperator)
    bpy.utils.register_class(SwapOperator)
    bpy.utils.register_class(SelectSrcMaterialOperator)
    bpy.utils.register_class(SelectDstMaterialOperator)
    bpy.utils.register_class(RotateMapOperator)
    bpy.utils.register_class(CopyMeshDataOperator)


def unregister():
    bpy.utils.unregister_class(SwapSelectedOperator)
    bpy.utils.unregister_class(SwapOperator)
    bpy.utils.unregister_class(SelectSrcMaterialOperator)
    bpy.utils.unregister_class(SelectDstMaterialOperator)
    bpy.utils.unregister_class(RotateMapOperator)
    bpy.utils.unregister_class(CopyMeshDataOperator)
