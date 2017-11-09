import os, sys
sys.path.append('..')
from Zolo_function import *

class Zolo:
    def help():
        print("Voici les commandes sur moi :")
        print("- zolo info")
        print("- zolo reset")
        print("- zolo aide")
        print("- zolo quitter")
        print("")
        return 0, "Voici mes commandes"

    def info():
        print("Salut, comme vous le savez, je suis Zolo !")
        print("Je suis un assistant qui peut faire plein de choses (fait 'aide' pour avoir la liste")
        print("Je suis en version",version,"et j'ai été créée par LavaPower")
        play("Salut, comme vous le savez, je suis Zolo !")
        play("Je suis un assistant qui peut faire plein de choses (fait 'aide' pour avoir la liste).")
        return 0,"Je suis en version "+version+" et j'ai été créée par LavaPower"

    def reset():
        print("\nJe vais me reset. Si tel est votre désir.")
        play("Je vais reset. Si tel est votre désir.")
        input()
        os.remove("./config.txt")
        print("Reset terminé.")
        print("Voulez vous m'arrêter (Oui/Non) ?")
        play("Reset terminé. Voulez vous me relancer ?")
        rep=input()
        if rep.lower()=="oui":
            return 1, ""
        else:
            return 0, ""

    def aide():
        print("Voici la liste des modules :")
        play("Voici la liste des modules")
        modules=os.listdir("modules")
        for i in modules:
            test=i.split(".")
            if len(test)==1:
                pass
            else:
                module,osef=i.split(".")
                print("-",module)
                play(module)
        print("")
        print("Par convention, mon développeur ont mis comme préfixe le nom de chaque fichiers des modules")
        print("Cependant, ce n'est pas une certitude, donc fais attention")
        play("Par convention, mon développeur a mis comme préfixe le nom de chaque fichiers des modules.")
        return 0, "Cependant, ce n'est pas une certitude, donc fais attention"
        
    def quitter():
        return 1, ""

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

version = "2.0.0"
prefix = "zolo"
moduleInstance = Zolo
    

