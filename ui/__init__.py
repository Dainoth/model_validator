from . import panels

_modules = [
    panels
]

def register():
    for module in _modules:
        print(module, " register")  # Отладочное сообщение
        module.register()


def unregister():
    for module in reversed(_modules):
        print(module, " unregister")  # Отладочное сообщение
        module.unregister()
