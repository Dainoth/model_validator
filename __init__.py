bl_info = {
    "name": "Model Validator",
    "author": "Ovcharov Denis",
    "version": (1, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar",
    "description": "Verification of models of architectural and urban planning solutions based on the relevant requirements to the parameters of high-polygonal models and low-polygonal models of objects placed in electronic form in the information systems of the city of Moscow.",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy
from . import ui, operators, properties


def register():
    properties.register()
    operators.register()
    ui.register()


def unregister():
    properties.unregister()
    operators.unregister()
    ui.unregister()


if __name__ == "__main__":
    register()