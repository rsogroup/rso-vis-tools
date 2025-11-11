import bpy


class RsoMaterialSwapPanel(bpy.types.Panel):
    bl_label = "Materialtausch"
    bl_idname = "VIEW3D_PT_rso_material_swap"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RSO Vis"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        col = box.column(align=True)
        col.label(text="Altes Material")
        col.prop(context.scene, "rso_src_mat", text="")
        col.operator("material.rso_select_src_material",
                     text="Von Objekt wählen")

        box = layout.box()
        col = box.column(align=True)
        col.label(text="Neues Material")
        col.prop(context.scene, "rso_dst_mat", text="")
        col.operator("material.rso_select_dst_material",
                     text="Von Objekt wählen")

        col = layout.column(align=True)
        col.operator("object.rso_swap_material_selected",
                     text="Ausgewählte Elemente")
        col.operator("object.rso_swap_material", text="Alle Elemente")


class RsoMaterialMapPanel(bpy.types.Panel):
    bl_label = "Mapping"
    bl_idname = "VIEW3D_PT_rso_material_map"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RSO Vis"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.rso_rotate_map", text="Richtung drehen")


class RsoMeshPanel(bpy.types.Panel):
    bl_label = "Mesh"
    bl_idname = "VIEW3D_PT_rso_mesh"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RSO Vis"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.rso_copy_mesh_data", text="Objekt trennen")
        layout.operator("object.rso_clean_mesh", text="Mesh bereinigen")


def register():
    bpy.utils.register_class(RsoMaterialSwapPanel)
    bpy.utils.register_class(RsoMaterialMapPanel)
    bpy.utils.register_class(RsoMeshPanel)


def unregister():
    bpy.utils.unregister_class(RsoMaterialSwapPanel)
    bpy.utils.unregister_class(RsoMaterialMapPanel)
    bpy.utils.unregister_class(RsoMeshPanel)
