class Core:
    def info(zolo, module, args):
        print(f"[Core] Version {module.version}")

    def stop(zolo, module, args):
        zolo.stop()

    def dismodule(zolo, module, args):
        if len(args) == 1:
            zolo.desactive_module(args[0])
            print(f"[Core] Module {args[0]} désactivé")
        else:
            print("[ERREUR] Syntaxe : core dismodule <module>")
    
    def actmodule(zolo, module, args):
        if len(args) == 1:
            zolo.active_module(args[0])
            print(f"[Core] Module {args[0]} activé")
        else:
            print("[ERREUR] Syntaxe : core actmodule <module>")

    def modules(zolo, module, args):
        print("[Core] Liste des modules :")
        for i in zolo.modules:
            if i.name in zolo.config.disabled_modules:
                print(f"[Core] - {i.name} (désactivé)")
            else:
                print(f"[Core] - {i.name}")