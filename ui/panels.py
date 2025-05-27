import bpy
from ..operators import basic_ops  # Импортируем операторы для использования в панели

classes = []

class MY_PT_MainPanel(bpy.types.Panel):
    bl_label = "AGR Model Validate"
    bl_idname = "MY_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AGR Validate"  # Это создаст новую вкладку в N-панели
    bl_options = {'DEFAULT_CLOSED'}  # Опционально: панель будет свернута по умолчанию

    def draw(self, context):
        layout = self.layout
        
        # Секция импорта
        box = layout.box()
        box.label(text="Project Import")
        
        # Кнопка импорта
        row = box.row()
        row.operator("my.import_project", 
                    text="Import AGR Projects", 
                    icon='IMPORT')
        
        # Настройки импорта
        box.prop(context.scene, "agr_clear_before_import")
        box.label(text="Select multiple ZIP archives", icon='INFO')

classes.append(MY_PT_MainPanel)

def register():
    # Регистрация кастомных свойств
    bpy.types.Scene.agr_import_settings = bpy.props.BoolProperty(
        name="Advanced Import Settings",
        default=False
    )

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.agr_import_settings

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)