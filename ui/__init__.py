from . import panels, preferences

_modules = [
    panels,
    preferences
]

def register():
    for module in _modules:
        module.register()

def unregister():
    for module in reversed(_modules):
        module.unregister()