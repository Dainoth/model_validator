import os
import zipfile
import tempfile
import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, CollectionProperty
from bpy.types import Operator

class MY_OT_ImportProject(Operator, ImportHelper):
    bl_idname = "my.import_project"
    bl_label = "Import AGR Project"
    bl_description = "Import AGR project from ZIP archive"
    bl_options = {'REGISTER', 'UNDO'}

    filter_glob: StringProperty(default='*.zip', options={'HIDDEN'})
    files: CollectionProperty(type=bpy.types.OperatorFileListElement, options={'HIDDEN', 'SKIP_SAVE'})
    directory: StringProperty(subtype='DIR_PATH', options={'HIDDEN', 'SKIP_SAVE'})

    def execute(self, context):
        # Очистка перед импортом (опционально)
        if hasattr(context.scene, 'agr_clear_before_import') and context.scene.agr_clear_before_import:
            self.clear_scene()

        # Импорт каждого архива в отдельную временную папку
        for file in self.files:
            zip_path = os.path.join(self.directory, file.name)
            
            # Создаем уникальную временную папку для каждого архива
            with tempfile.TemporaryDirectory(prefix="agr_import_") as temp_dir:
                try:
                    # Распаковка в уникальную папку
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)
                        self.report({'INFO'}, f"Processing: {file.name}")
                    
                    # Обработка содержимого архива
                    self.process_archive_contents(temp_dir, file.name)
                    
                except Exception as e:
                    self.report({'ERROR'}, f"Failed to process {file.name}: {str(e)}")
                    continue

        return {'FINISHED'}

    def clear_scene(self):
        """Очистка сцены перед импортом"""
        for obj in bpy.data.objects:
            bpy.data.objects.remove(obj)
        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh)
        for material in bpy.data.materials:
            bpy.data.materials.remove(material)

    def process_archive_contents(self, directory, archive_name):
        """Обработка содержимого архива с уникальным именованием"""
        # Создаем коллекцию для этого архива
        collection = bpy.data.collections.new(f"AGR_{os.path.splitext(archive_name)[0]}")
        bpy.context.scene.collection.children.link(collection)
        
        # Находим все FBX файлы
        fbx_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.fbx'):
                    fbx_files.append(os.path.join(root, file))
        
        # Импортируем FBX в созданную коллекцию
        for fbx_path in fbx_files:
            # Сохраняем текущую активную коллекцию
            old_collection = bpy.context.view_layer.active_layer_collection
            
            # Устанавливаем нашу коллекцию как активную
            bpy.context.view_layer.active_layer_collection = \
                bpy.context.view_layer.layer_collection.children[collection.name]
            
            # Импортируем FBX
            bpy.ops.import_scene.fbx(filepath=fbx_path)
            
            # Возвращаем предыдущую активную коллекцию
            bpy.context.view_layer.active_layer_collection = old_collection
        
        # Обработка GEOJSON (если есть)
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.geojson'):
                    self.process_geojson(os.path.join(root, file), collection)
                    break

def register():
    # Регистрируем кастомное свойство для очистки сцены
    bpy.types.Scene.agr_clear_before_import = bpy.props.BoolProperty(
        name="Clear Scene Before Import",
        description="Remove all objects before importing new archives",
        default=False
    )
    bpy.utils.register_class(MY_OT_ImportProject)

def unregister():
    del bpy.types.Scene.agr_clear_before_import
    bpy.utils.unregister_class(MY_OT_ImportProject)