import webbrowser, sys
sys.path.append('..')
from Zolo_function import *

class Internet:
    
    def recherche():
        play("Votre moteur de recherche")
        moteur = input("Moteur à utiliser (Google par défault) : ").lower()
        if moteur in moteurs:
            play("Votre recherche")
            recherche=input("Votre recherche : ")
            if moteur == "google":
                url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                webbrowser.open_new(url)
            elif moteur == "ecosia":
                url="https://www.ecosia.org/search?q="+recherche
                webbrowser.open_new(url)
            elif moteur == "youtube":
                url = "https://www.youtube.com/results?search_query="+recherche
                webbrowser.open_new(url)
            elif moteur == "duckduckgo":
                url = "https://duckduckgo.com/?q="+recherche
                webbrowser.open_new(url)
            elif moteur == "bing":
                url = "https://www.bing.com/search?q="+recherche
                webbrowser.open_new(url)
            elif moteur == "yahoo":
                url = "https://fr.search.yahoo.com/search?p="+recherche
                webbrowser.open_new(url)
            return 0, "Ouvert"
        else:
            play(moteur+" n'est pas pris en charge? Voulez vous utiliser Google ?")
            print("'"+moteur+"' n'est pas pris en charge. Voulez vous utiliser Google (Oui/Non) ?")
            rep=input().lower()
            if rep == "oui":
                url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                webbrowser.open_new(url)
                return 0, "Ouvert"
            else:
                print("Okay, merci d'utiliser un des moteurs disponibles.")
                print("Si vous avez le module liste, vous pouvez faire liste moteur")
                return 0, "Merci d'utiliser un des moteurs disponibles. Vous pouvez utiliser le module 'liste' pour en avoir la liste"

    def meteo():
        play("Votre ville")
        ville = input("Votre ville : ")
        play("Votre code postal")
        code = input("Votre code postal : ")
        url = 'http://www.meteofrance.com/previsions-meteo-france/'+ville+"/"+code
        webbrowser.open_new(url)
        return 0, "Ouvert"

    def help():
        print("Commande :")
        print("- internet recherche")
        print("- internet meteo")
        return 0, "Voici la liste des commandes du module 'internet'"

    def handle(self,args):
        test=args.split(" ")
        if len(test)==1:
            method=args.split(" ")
            try:
                return eval("self."+method[0]+"()")
            except:
                print("Je n'ai pas compris votre demande")
                return 0, "Je n'ai pas compris votre demande"
        else:
            method,arg=args.split(" ",1)
            try:
                return eval("self."+method+"("+arg+")")
            except:
                print("Je n'ai pas compris votre demande")
                return 0, "Je n'ai pas compris votre demande"

moteurs=["google","youtube","duckduckgo","bing","yahoo","ecosia"]
prefix = "internet"
moduleInstance = Internet
