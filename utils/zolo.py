import json
from os import listdir, path
from utils.module import Module
from utils.config import Config
from utils.api import API


class Zolo:
    def __init__(self):
        """
        Create Zolo
        """
        print("[Zolo] Initialisation de Zolo...")
        self.api = API(self)
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

    def launch(self):
        """
        Launch Zolo
        """
        self.launched = True
        while self.launched:
            rep = input("\n[Zolo] >>> ")
            words = rep.split(" ")
            if words:
                module = self.api.get_module(words[0])
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
                                getattr(module.moduleImport, words[1])(self.api, module, [])
                            else:
                                getattr(module.moduleImport, words[1])(self.api, module, words[2:])
                        else:
                            print("[ERREUR] Commande inconnue")
