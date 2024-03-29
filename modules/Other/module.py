import subprocess
import os


class Utilities:
    def ping_pc(self, ip):
        """
        Envoie un ping à une IP

        Args:
            ip (string): IP à ping
            
        Returns:
            list(string): Liste des résultats
        """
        try:
            out, _ = subprocess.Popen(["ping", ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
        except (ValueError, OSError) as err:
            return f"Erreur : {err.args[0]}"
        return out.decode("cp850").splitlines()
    
    def connect_pc(self, ip):
        """
        Dis si un PC est connecté

        Args:
            ip (string): IP à tester
            
        Returns:
            string: Resultat
        """
        lignes = Utilities.ping_pc(ip)

        if lignes[0]:
            return f"{ip} => Nom de domaine introuvable"
        for i, ligne in enumerate(lignes):
            if not ligne:
                k = i + 1
                break
        return (f"{ip} => connecté", lignes[10]) if len(lignes) - k > 3 else f"{ip} => non connecté"


class Other:
    utilities = Utilities()
    def info(self, zolo, module, args):
        """
        Info about Other module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Other] Version {module.version}")
        
    def open(self, zolo, module, args):
        """
        Open Program

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            print(f"[Other] Ouverture de {args[0]}")
            os.popen(" ".join(args))
        else:
            print("[ERREUR] Syntaxe : other open <program>")
        
    def ping(self, zolo, module, args):  # sourcery skip: extract-method
        """
        Ping IP address

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            rep = Other.utilities.connect_pc(args[0])
            if len(rep) > 2:
                print(rep)
            else:
                ping = rep[1].split(" ")
                pingfinal = ""
                for i in ping[12]:
                    try:
                        int(i)
                    except Exception:
                        pass
                    else:
                        pingfinal += str(i)
                print(f"[Other] Ping : {pingfinal} ms")
                pingfinal=int(pingfinal)
                if pingfinal < 100:
                    print("[Other] Tu as un bon ping")
                elif pingfinal < 500:
                    print("[Other] Fais attention, ton ping est un peu haut")
                elif pingfinal < 1000:
                    print("[Other] Ton ping est haut, certains jeux multijoueur ne voudront pas de toi")
                else:
                    print("[Other] IMPOSSIBLE DE JOUER EN MULTI, Désolé")

        else:
            print("[ERREUR] Syntaxe : other ping <ip>")
