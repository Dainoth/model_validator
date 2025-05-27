import bpy
from . import basic_ops, import_ops

_modules = [
    basic_ops,
    import_ops
]

def register():
    for module in _modules:
        module.register()


def unregister():
    for module in reversed(_modules):
        module.unregister()

