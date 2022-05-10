from urllib import response
import bs4
import requests
import time
from modules.HB import parser_hb


class HB:
    def info(self, zolo, module, args):
        """
        Info about HB module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[HB] Version {module.version}")
        
    def perso(self, zolo, module, args):
        """
        Get Informations about personnage

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            perso = args[0]
            account = open("modules/HB/account.txt", "r").readlines()
            start = time.time()
            response = parser_hb.connection(account[0].strip(), account[1].strip())
            print(f"[HB] Connexion réussie (Temps : {(time.time() - start):.2f}s)")
            
            start = time.time()
            player = parser_hb.get_infos_for(perso, response.cookies)
            if player:
                print(f"[HB] Informations recueillies pour {player[0]} ({player[2]}) (Temps : {(time.time() - start):.2f}s) :")
                print(f"     - Pseudo MC : {player[1]}")
                print(f"     - Titre : {player[3]}")
                print(f"     - Genre : {player[4]}")
                print(f"     - Status du BG : {player[5]}")
                print(f"     - Nombre de message sur le forum : {player[6]}")
                print(f"     - Pourcentage de quêtes réussies : {player[7]}")
                print(f"     - Nombre de mantra : {player[8]}")
                print(f"     - Nombre de fragments : {player[9]}")
                print(f"     - Activité : {player[10]}")
                print(f"     - Nombre d'ampoules : {player[11]} ({player[12]} allumée(s), {player[13]} éteinte(s), {player[14]} cassée(s))")
            else:
                print(f"[ERREUR] Personnage inconnu (Temps : {(time.time() - start):.2f}s)")
        else:
            print("[ERREUR] Syntaxe : hb perso <perso>")
