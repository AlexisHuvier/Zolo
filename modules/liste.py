class Liste:
    
    def help():
        print("Vous pouvez lister ces objets :")
        print("- liste moteur")
        print("")
        return 0, "Voici la liste des commandes pour le module 'liste'"
        
    def moteur():
        print("Liste des moteurs :")
        for i in moteurs:
            print("-",i)
        print("")
        return 0, "Voici la liste des moteurs"

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
prefix="liste"
moduleInstance=Liste
