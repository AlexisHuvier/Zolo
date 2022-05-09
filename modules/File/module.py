import os
import shutil


class File:
    def info(zolo, module, args):
        """
        Info about File module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[File] Version {module.version}")
        
    def cat(zolo, module, args):
        """
        Show file content

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if os.path.isfile(args[0]):
                print(f"[File] Fichier : {args[0]}")
                with open(args[0], "r") as f:
                    print(f.read())
            else:
                print("[File] Fichier inconnu")
        else:
            print("[Erreur] Syntaxe : file cat <file>")
    
    def ls(zolo, module, args):
        """
        List files in directory

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            print(f"[File] Répertoire : {args[0]}")
            print("\n         Taille     Nom")
            for i in os.listdir(args[0]):
                if os.path.isfile(i):
                    print("       " + " "*max(0, 9 - len(str(os.path.getsize(i)))) + str(os.path.getsize(i)), i)
                else:
                    print("                ", i)
        else:
            print("[Erreur] Syntaxe : file ls <directory>")
            
    def mkdir(zolo, module, args):
        """
        Create directory

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if os.path.exists(args[0]):
                print("[File] Répertoire déjà existant")
            else:
                os.mkdir(args[0])
                print("[File] Répertoire créé")
        else:
            print("[Erreur] Syntaxe : file mkdir <directory>")
            
    def rm(zolo, module, args):
        """
        Remove file

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if os.path.isfile(args[0]):
                os.remove(args[0])
                print("[File] Fichier supprimé")
            else:
                print("[File] Fichier invalide")
        else:
            print("[Erreur] Syntaxe : file rm <file>")
    
    def rmdir(zolo, module, args):
        """
        Remove directory

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if os.path.isdir(args[0]):
                shutil.rmtree(args[0], ignore_errors=True)
                print("[File] Dossier supprimé")
            else:
                print("[File] Dossier invalide")
        else:
            print("[Erreur] Syntaxe : file rmdir <directory>")
    
    def touch(zolo, module, args):
        """
        Create empty file

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if os.path.exists(args[0]):
                print("[File] Fichier déjà existant")
            else:
                with open(args[0], "w") as f:
                    pass
                print("[File] Fichier créé")
        else:
            print("[Erreur] Syntaxe : file touch <file>")
