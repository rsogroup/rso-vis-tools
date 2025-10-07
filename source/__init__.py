def register():
    from . import properties
    from . import operators
    from . import ui
    properties.register()
    operators.register()
    ui.register()


def unregister():
    from . import properties
    from . import operators
    from . import ui
    properties.unregister()
    operators.unregister()
    ui.unregister()


if __name__ == "__main__":
    register()
