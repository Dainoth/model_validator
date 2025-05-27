from . import basic_ops, advanced_ops

_modules = [
    basic_ops,
    advanced_ops
]

def register():
    for module in _modules:
        module.register()

def unregister():
    for module in reversed(_modules):
        module.unregister()