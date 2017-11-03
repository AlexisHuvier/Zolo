import os

class Zolo:
    def help():
        print("Voici les commandes sur moi :")
        print("- zolo info")
        print("- zolo reset")
        print("- zolo aide")
        print("- zolo quitter")
        print("")
        return 0

    def info():
        print("Salut, comme tu le sais, je suis Zolo !")
        print("Je suis un assistant qui peut faire plein de choses (fait 'aide' pour avoir la liste")
        print("Je suis en version",version,"et j'ai été crée par LavaPower")
        return 0

    def reset():
        print("\nJe vais me reset. Si tel est votre désir.")
        input()
        os.remove("./config.txt")
        print("Reset terminé.")
        print("Voulez vous m'arrêter (Oui/Non) ?")
        rep=input()
        if rep.lower()=="oui":
            return 1
        else:
            return 0

    def aide():
        print("Voici la liste des modules :")
        modules=os.listdir("modules")
        print(modules)
        for i in modules:
            test=i.split(".")
            if len(test)==1:
                pass
            else:
                module,osef=i.split(".")
                print("-",module)
        print("")
        print("Par convention, mon développeur ont mis comme préfixe le nom de chaque fichiers des modules")
        print("Cependant, ce n'est pas une certitude, donc fais attention")
        return 0
        
    def quitter():
        return 1

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

version = "1.0.0"
prefix = "zolo"
moduleInstance = Zolo
    

