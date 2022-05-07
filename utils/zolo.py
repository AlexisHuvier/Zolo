import importlib
import json
from os import listdir, path
from utils.module import Module
from utils.config import Config


class Zolo:
    def __init__(self):
        """
        Create Zolo
        """
        print("[Zolo] Initialisation de Zolo...")
        self.modules = []
        self.launched = False
        print("[Zolo] Chargement de la configuration...")
        self.config = Config.load()
        self.config.save()
        print("[Zolo] Configuration chargée")

        print("[Zolo] Chargement des modules...")
        for i in listdir("modules"):
            if path.exists(f"modules/{i}/info.json"):
                self.modules.append(Module(**json.loads(open(f"modules/{i}/info.json").read())))
            else:
                print(f"[ERREUR] Le module {i} n'a pas de fichier info.json")

        for i in self.modules:
            print(f"[Zolo] Module {i.name} chargé")
            i.commands = [i for i in dir(i.moduleImport) if not i.startswith("_")]

        print("[Zolo] Modules chargés")
        print("[Zolo] Zolo lancé")
        
    def has_module(self, module):
        """
        Return if module is loaded

        Args:
            module (string): Name of module

        Returns:
            bool: True if module is loaded
        """
        return module in [i.name for i in self.modules]
    
    def load_module(self, module):
        """
        Load a module

        Args:
            module (string): Name of module
        """
        if path.exists(f"modules/{module}/info.json"):
            module = Module(**json.loads(open(f"modules/{module}/info.json").read()))
            self.modules.append(module)
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
        for i in self.modules:
            if i.name == module:
                self.modules.remove(i)
                new = Module(**json.loads(open(f"modules/{module}/info.json").read()), reload=True)
                self.modules.append(new)
                new.commands = [i for i in dir(new.moduleImport) if not i.startswith("_")]
                break

    def desactive_module(self, module):
        """
        Desactivate a module

        Args:
            module (string): Name of module
        """
        if module not in self.config.disabled_modules:
            self.config.disabled_modules.append(module)
        self.config.save()

    def active_module(self, module):
        """
        Activate a module

        Args:
            module (string): Name of module
        """
        if module in self.config.disabled_modules:
            self.config.disabled_modules.remove(module)
        self.config.save()

    def stop(self):
        """
        Stop Zolo
        """
        self.launched = False

    def get_module(self, prefix):
        """
        Get module from prefix

        Args:
            prefix (string): Prefix

        Returns:
            Module: Module or None
        """
        for i in self.modules:
            if i.prefix == prefix:
                return i

    def launch(self):
        """
        Launch Zolo
        """
        self.launched = True
        while self.launched:
            rep = input("\n[Zolo] >>> ")
            words = rep.split(" ")
            if words:
                module = self.get_module(words[0])
                if module is None:
                    print("[ERREUR] Module inconnu")
                elif module.name in self.config.disabled_modules:
                    print("[Zolo] Module désactivé")
                else:
                    if len(words) == 1:
                        print(f"[Zolo] Les commandes du module {module.name} sont :")
                        for i in module.commands:
                            print(f"      - {module.prefix} {i}")
                    else:
                        if words[1] in module.commands:
                            if len(words) == 2:
                                getattr(module.moduleImport, words[1])(self, module, [])
                            else:
                                getattr(module.moduleImport, words[1])(self, module, words[2:])
                        else:
                            print("[ERREUR] Commande inconnue")
