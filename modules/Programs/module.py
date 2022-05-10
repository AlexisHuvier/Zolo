import subprocess


class Programs:
    programs = {i.strip().split(" ")[0]: i.strip().split(" ")[1] for i in open("modules/Programs/programs.txt", "r").readlines()}
    def info(self, zolo, module, args):
        """
        Info about Programs module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Programs] Version {module.version}")
        
    def open(self, zolo, module, args):
        """
        Open Program

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if args[0] in Programs.programs.keys():
                print(f"[Programs] Ouverture de '{args[0]}'")
                subprocess.call([Programs.programs[args[0]]])
            else:
                print(f"[Erreur] '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : programs open <program>")
    
    def add(self, zolo, module, args):
        """
        Add Program

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if len(args) == 2:
            Programs.programs[args[0]] = args[1]
            open("modules/Programs/programs.txt", "w").write("\n".join([f"{k} {v}" for k, v in Programs.programs.items()]))
            print(f"[Programs] '{' '.join(args)}' ajouté")
        else:
            print("[Programs] Syntaxe : programs add <name> <command>")
    
    def list(self, zolo, module, args):
        """
        List programs

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if Programs.programs:
            print("[Programs] Liste des tâches :")
            for k, v in Programs.programs.items():
                print(f"      - {k}")
        else:
            print("[Programs] Aucun programme")

    def remove(self, zolo, module, args):
        """
        Remove program

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if args[0].isdigit() and 1 <= int(args[0]) <= len(Programs.programs):
                t = Programs.programs[int(args[0]) - 1]
            else:
                t = " ".join(args)
            if t in Programs.programs.keys():
                Programs.programs.remove(t)
                print(f"[Programs] '{t}' supprimé")
                open("modules/Programs/programs.txt", "w").write("\n".join([f"{k} {v}" for k, v in Programs.programs.items()]))
            else:
                print(f"[Erreur] '{t}' introuvable")
        else:
            print("[Erreur] Syntaxe : programs remove <program>")
