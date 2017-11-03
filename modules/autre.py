import os

class Autre:
    
    def imc():
        t=input("Ta taille en m : ")
        p=input("Ton poids en kg : ")
        t=pow(float(t),2)
        imc=int(p)/t
        if imc < 16.5:
               print("Votre imc est de :",imc,".Vous êtes en état de famine ")
               print("Il y a un problème....Mangez plus!")
         
        elif imc >= 16.5 and imc <= 18.5:
               print("Votre imc est de :",imc,".Vous êtes en état de maigreur ")
               print("Il faudrait manger un peu plus")
         
        elif imc >= 18.5 and imc <= 25:
               print("Votre imc est de :",imc,".Vous avez une corpulence normale")
               print("Bravo")
         
        elif imc >= 25 and imc <= 30:
               print("Votre imc est de :",imc,".Vous êtes en surpoids")
               print("Régime...")
             
        elif imc >= 30 and imc <= 35:
               print("Votre imc est de :",imc,".Vous êtes en état d'obésité modérée")
               print("Régime...")
              
        elif imc >= 35 and imc <= 40:
               print("Votre imc est de :",imc,".Vous êtes en état d'obésité sévère")
               print("Régime...")
             
        elif imc > 40:
               print("Votre imc est de :",imc,".Vous êtes en état d'obésité massive")
               print("Régime...")
        return 0

    def ouvrir():
        url=input("'Chose' à ouvrir :")
        os.popen(url)
        return 0

    def help():
        print("Commande :")
        print("- autre imc")
        print("- autre ouvrir")
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

prefix = "autre"
moduleInstance = Autre
