import bpy
from ..operators import basic_ops  # Импортируем операторы для использования в панели

class MY_PT_MainPanel(bpy.types.Panel):
    bl_label = "My Addon"
    bl_idname = "MY_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "My Addon"  # Это создаст новую вкладку в N-панели
    bl_options = {'DEFAULT_CLOSED'}  # Опционально: панель будет свернута по умолчанию

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Основная секция
        box = layout.box()
        box.label(text="Basic Tools")
        box.operator("my.basic_operator", icon='OBJECT_DATA')
        
        # Секция настроек
        box = layout.box()
        box.label(text="Settings")
        box.prop(scene, "my_property")  # Пример использования кастомного свойства
        
        # Секция с развернутыми настройками
        layout.use_property_split = True  # Красивый разделенный вид
        layout.use_property_decorate = False  # Убираем лишние декораторы
        layout.separator()
        
        # Кнопка с иконкой
        row = layout.row()
        row.operator("my.advanced_operator", text="Advanced Action", icon='SETTINGS')

def register():
    bpy.utils.register_class(MY_PT_MainPanel)

def unregister():
    bpy.utils.unregister_class(MY_PT_MainPanel)