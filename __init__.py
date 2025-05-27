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


def register():
    pass  # Здесь будет код регистрации вашего аддона


def unregister():
    pass  # Здесь будет код удаления вашего аддона


if __name__ == "__main__":
    register()