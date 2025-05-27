import bpy

class MY_PT_MainPanel(bpy.types.Panel):
    bl_label = "My Addon Panel"
    bl_idname = "MY_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "My Addon"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("my.basic_operator")

def register():
    bpy.utils.register_class(MY_PT_MainPanel)

def unregister():
    bpy.utils.unregister_class(MY_PT_MainPanel)