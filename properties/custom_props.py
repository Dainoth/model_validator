import bpy

def register():
    bpy.types.Scene.my_property = bpy.props.FloatProperty(
        name="My Property",
        description="Example custom property",
        default=1.0,
        min=0.1,
        max=10.0
    )

def unregister():
    del bpy.types.Scene.my_property