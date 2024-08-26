from importlib import import_module
from .models import modules

def get_pluggable_model_modules():
    """
    Imports pluggable models.
    """
    list_last_element_index = -1
    module_names_with_extensions = [module_path.split('\\')[list_last_element_index].split('/')[list_last_element_index] for module_path in modules]
    module_names = [module_name.split('.')[0] for module_name in module_names_with_extensions]
    return [
        import_module(".models." + module_name, package='engine') for module_name in module_names if module_name != "__init__"
    ]

def get_pluggable_models():
    """
    Returns a list of pluggable model modules with names defined in them.
    """
    return {
        module.PluggableModel().dictionary_name() : module for module in get_pluggable_model_modules()
    }

if __name__ == "__main__":
    models = get_pluggable_models()
    print("done")