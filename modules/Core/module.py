class Core:
    def info(zolo, module, args):
        """
        Info about Core module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Core] Version {module.version}")

    def stop(zolo, module, args):
        """
        Stop Zolo

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        zolo.stop()

    def dismodule(zolo, module, args):
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

    def actmodule(zolo, module, args):
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

    def modules(zolo, module, args):
        """
        Show list of modules

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print("[Core] Liste des modules :")
        for i in zolo.modules:
            if i.name in zolo.config.disabled_modules:
                print(f"[Core] - {i.name} (désactivé)")
            else:
                print(f"[Core] - {i.name}")
