import bpy


def register():
    bpy.types.Scene.rso_src_mat = bpy.props.PointerProperty(
        name="Altes Material",
        type=bpy.types.Material,
        description="Das zu ersetzende Material"
    )
    bpy.types.Scene.rso_dst_mat = bpy.props.PointerProperty(
        name="Neues Material",
        type=bpy.types.Material,
        description="Das neue Material"
    )


def unregister():
    del bpy.types.Scene.rso_src_mat
    del bpy.types.Scene.rso_dst_mat
