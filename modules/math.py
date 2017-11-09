from math import *

class Math:
    
    def calcul(arg="Pas de calcul"):
        if arg == "Pas de calcul":
            print("Pas de calcul")
            return 0, "Pas de calcul"
        else:
            try:
                arg=float(arg)
                print("Resultat :",str(arg))
                return 0, "Resultat : "+str(arg)
            except:
                print("Ce calcul ne donne pas un nombre")
                return 0, "Ce calcul ne donne pas un nombre"

    def help():
        print("Commande :")
        print("- math calcul <calcul>")
        return 0, "Voici la liste des commandes du module 'math'"

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

prefix = "math"
moduleInstance = Math
