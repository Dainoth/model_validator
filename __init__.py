bl_info = {
    "name": "Model Validator",
    "author": "Ovcharov Denis",
    "version": (1, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar",
    "description": "Modular addon with separated functionality",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy
from . import operators, ui, properties, utilities

def register():
    properties.register()
    operators.register()
    ui.register()
    
def unregister():
    ui.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()