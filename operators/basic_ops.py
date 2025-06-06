import bpy

class MY_OT_BasicOperator(bpy.types.Operator):
    bl_idname = "my.basic_operator"
    bl_label = "Basic Operator"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        print(f"Basic operator executed with value: {context.scene.my_property}")
        self.report({'INFO'}, "Basic operator executed!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MY_OT_BasicOperator)

def unregister():
    bpy.utils.unregister_class(MY_OT_BasicOperator)