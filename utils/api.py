import json
from os import path
from utils.module import Module


class API:
    def __init__(self, zolo):
        self.__zolo = zolo
        
    def get_config(self):
        """
        Get config
        """
        return self.__zolo.config
        
    def has_module(self, module):
        """
        Return if module is loaded

        Args:
            module (string): Name of module

        Returns:
            bool: True if module is loaded
        """
        return module in [i.name for i in self.__zolo.modules]
    
    def load_module(self, module):
        """
        Load a module

        Args:
            module (string): Name of module
        """
        if path.exists(f"modules/{module}/info.json"):
            module = Module(**json.loads(open(f"modules/{module}/info.json").read()))
            self.__zolo.modules.append(module)
            module.commands = [i for i in dir(module.moduleImport) if not i.startswith("_")]
            return True
        else:
            return False
        
    def reload_module(self, module):
        """
        Reload a module

        Args:
            module (string): Name of module
        """
        for i in self.__zolo.modules:
            if i.name == module:
                self.__zolo.modules.remove(i)
                new = Module(**json.loads(open(f"modules/{module}/info.json").read()), reload=True)
                self.__zolo.modules.append(new)
                new.commands = [i for i in dir(new.moduleImport) if not i.startswith("_")]
                break

    def desactive_module(self, module):
        """
        Desactivate a module

        Args:
            module (string): Name of module
        """
        if module not in self.__zolo.config.disabled_modules:
            self.__zolo.config.disabled_modules.append(module)
        self.__zolo.config.save()

    def active_module(self, module):
        """
        Activate a module

        Args:
            module (string): Name of module
        """
        if module in self.__zolo.config.disabled_modules:
            self.__zolo.config.disabled_modules.remove(module)
        self.__zolo.config.save()

    def stop(self):
        """
        Stop Zolo
        """
        self.__zolo.launched = False

    def get_module(self, prefix):
        """
        Get module from prefix

        Args:
            prefix (string): Prefix

        Returns:
            Module: Module or None
        """
        for i in self.__zolo.modules:
            if i.prefix == prefix:
                return i
    
    def get_all_modules(self):
        """
        Get all modules
        """
        return self.__zolo.modules
