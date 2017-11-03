import webbrowser

class Internet:
    
    def recherche():
        moteur = input("Moteur à utiliser (Google par défault) : ").lower()
        if moteur in moteurs:
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
        else:
            print("'"+moteur+"' n'est pas pris en charge. Voulez vous utiliser Google (Oui/Non) ?")
            rep=input().lower()
            if rep == "oui":
                url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                webbrowser.open_new(url)
            else:
                print("Okay, merci d'utiliser un des moteurs disponibles.")
                print("Si vous avez le module liste, vous pouvez faire liste moteur")
        return 0

    def meteo():
        ville = input("Votre ville : ")
        code = input("Son code postal : ")
        url = 'http://www.meteofrance.com/previsions-meteo-france/'+ville+"/"+code
        webbrowser.open_new(url)
        return 0

    def help():
        print("Commande :")
        print("- internet recherche")
        print("- internet meteo")
        return 0

    def handle(self,args):
        test=args.split(" ")
        if len(test)==1:
            method=args.split(" ")
            try:
                return eval("self."+method[0]+"()")
            except:
                print("Je n'ai pas compris votre demande")
                return 0
        else:
            method,args=args.split(" ",1)
            try:
                return eval("self."+method+"("+args+")")
            except:
                print("Je n'ai pas compris votre demande")
                return 0

moteurs=["google","youtube","duckduckgo","bing","yahoo","ecosia"]
prefix = "internet"
moduleInstance = Internet
