class Todo:
    things = [i.strip() for i in open("modules/Todo/todo.txt", "r").readlines()]
    def info(self, zolo, module, args):
        """
        Info about Todo module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Todo] Version {module.version}")
    
    def add(self, zolo, module, args):
        """
        Add thing in Todo list

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            Todo.things.append(" ".join(args))
            open("modules/Todo/todo.txt", "w").write("\n".join(Todo.things))
            print(f"[Todo] '{' '.join(args)}' ajouté")
        else:
            print("[Erreur] Syntaxe : todo add <tâche>")
    
    def list(self, zolo, module, args):
        """
        List things in Todo list

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if Todo.things:
            print("[Todo] Liste des tâches :")
            for i in Todo.things:
                print(f"      - {i}")
        else:
            print("[Todo] Aucune tâche")

    def remove(self, zolo, module, args):
        """
        Remove thing in Todo list

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if args[0].isdigit() and 1 <= int(args[0]) <= len(Todo.things):
                t = Todo.things[int(args[0]) - 1]
            else:
                t = " ".join(args)
            if t in Todo.things:
                Todo.things.remove(t)
                print(f"[Todo] '{t}' supprimé")
                open("modules/Todo/todo.txt", "w").write("\n".join(Todo.things))
            else:
                print(f"[Erreur] '{t}' introuvable")
        else:
            print("[Erreur] Syntaxe : todo remove <tâche>")
