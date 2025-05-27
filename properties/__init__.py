from . import custom_props

_modules = [
    custom_props
]

def register():
    for module in _modules:
        module.register()

def unregister():
    for module in reversed(_modules):
        module.unregister()