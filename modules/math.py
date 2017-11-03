from math import *

class Math:
    
    def calcul(arg="Pas de calcul"):
        print("Resultat :",str(arg))
        return 0

    def help():
        print("Commande :")
        print("- math calcul <calcul>")
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

prefix = "math"
moduleInstance = Math
