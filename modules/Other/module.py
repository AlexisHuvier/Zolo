from re import sub
import subprocess
import os


class Utilities:
    def ping_pc(ip):
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
    
    def connect_pc(ip):
        """
        Dis si un PC est connecté

        Args:
            ip (string): IP à tester
            
        Returns:
            string: Resultat
        """
        lignes = Utilities.ping_pc(ip)
        
        if lignes[0]:
            return ip + " => Nom de domaine introuvable"
        else:
            for i, ligne in enumerate(lignes):
                if not ligne:
                    k = i + 1
                    break
            if len(lignes) - k > 3:
                return ip + " => connecté", lignes[10]
            else:
                return ip + " => non connecté"


class Other:
    def info(zolo, module, args):
        """
        Info about Other module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Other] Version {module.version}")
        
    def open(zolo, module, args):
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
        
    def ping(zolo, module, args):
        """
        Ping IP address

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            rep = Utilities.connect_pc(args[0])
            if len(rep) > 2:
                print(rep)
            else:
                ping = rep[1].split(" ")
                pingfinal = ""
                for i in ping[12]:
                    try:
                        int(i)
                    except:
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
