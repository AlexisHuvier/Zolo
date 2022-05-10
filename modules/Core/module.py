import os


class Core:
    def info(self, zolo, module, args):
        """
        Info about Core module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Core] Version {module.version}")

    def stop(self, zolo, module, args):
        """
        Stop Zolo

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        zolo.stop()

    def dismodule(self, zolo, module, args):
        """
        Disactivate a module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if zolo.has_module(args[0]):
                zolo.desactive_module(args[0])
                print(f"[Core] Module {args[0]} désactivé")
            else:
                print("[ERREUR] Module inconnu")
        else:
            print("[ERREUR] Syntaxe : core dismodule <module>")

    def actmodule(self, zolo, module, args):
        """
        Activate a module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if zolo.has_module(args[0]):
                zolo.active_module(args[0])
                print(f"[Core] Module {args[0]} activé")
            else:
                print("[ERREUR] Module inconnu")
        else:
            print("[ERREUR] Syntaxe : core actmodule <module>")

    def modules(self, zolo, module, args):
        """
        Show list of modules

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print("[Core] Liste des modules :")
        for i in zolo.get_all_modules():
            if i.name in zolo.get_config().disabled_modules:
                print(f"[Core] - {i.name} (désactivé)")
            else:
                print(f"[Core] - {i.name}")
                
    def load(self, zolo, module, args):
        """
        Load a module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if zolo.has_module(args[0]):
                print("[ERREUR] Module déjà chargé")
            elif zolo.load_module(args[0]):
                print(f"[Core] Module {args[0]} chargé")
            else:
                print(f"[ERREUR] Le module {args[0]} n'a pas de fichier info.json")
        else:
            print("[ERREUR] Syntaxe : core load <module>")
    
    def reload(self, zolo, module, args):
        """
        Reload a module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if zolo.has_module(args[0]):
                zolo.reload_module(args[0])
                print(f"[Core] Module {args[0]} rechargé")
            else:
                print("[ERREUR] Module inconnu")
        else:
            print("[ERREUR] Syntaxe : core reload <module>")
            
    def reloadall(self, zolo, module, args):
        """
        Reload all modules

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print("[Core] Rechargement de tous les modules...")
        for i in zolo.get_all_modules():
            zolo.reload_module(i)
            print(f"[Core] Module {i.name} rechargé")
        print("[Core] Modules rechargés")
        
    def clear(self, zolo, module, args):
        """
        Clear terminal zolo

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        os.system("cls")
