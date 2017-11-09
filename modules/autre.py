import os, sys
sys.path.append('..')
from Zolo_function import *

class Autre:
    
    def imc():
        play("Votre taille en mètres")
        t=input("Votre taille en m : ")
        play("Votre poids en kilogrammes")
        p=input("Votre poids en kg : ")
        t=pow(float(t),2)
        imc=int(p)/t
        if imc < 16.5:
            print("Votre imc est de :",imc,".Vous êtes en état de famine ")
            print("Il y a un problème....Mangez plus!")
            play("Votre IMC est de "+str(imc)+". Vous êtes en état de famine")
         
        elif imc >= 16.5 and imc <= 18.5:
            print("Votre imc est de :",imc,".Vous êtes en état de maigreur ")
            print("Il faudrait manger un peu plus")
            play("Votre IMC est de "+str(imc)+". Vous êtes en état de maigreur")
         
        elif imc >= 18.5 and imc <= 25:
            print("Votre imc est de :",imc,".Vous avez une corpulence normale")
            print("Bravo")
            play("Votre IMC est de "+str(imc)+". Vous avez une corpulence normale")
         
        elif imc >= 25 and imc <= 30:
            print("Votre imc est de :",imc,".Vous êtes en surpoids")
            print("Régime...")
            play("Votre IMC est de "+str(imc)+". Vous êtes en surpoids")
             
        elif imc >= 30 and imc <= 35:
            print("Votre imc est de :",imc,".Vous êtes en état d'obésité modérée")
            print("Gros régime...")
            play("Votre IMC est de "+str(imc)+". Vous êtes en état d'obésité modérée")
              
        elif imc >= 35 and imc <= 40:
            print("Votre imc est de :",imc,".Vous êtes en état d'obésité sévère")
            print("OMG...")
            play("Votre IMC est de "+str(imc)+". Vous êtes en état d'obésité sévère")
             
        elif imc > 40:
            print("Votre imc est de :",imc,".Vous êtes en état d'obésité massive")
            print("OMFG...")
            play("Votre IMC est de "+str(imc)+". Vous êtes en état d'obésité massive")
        return 0,""

    def ouvrir():
        play("Chose à ouvrir")
        url=input("'Chose' à ouvrir :")
        os.popen(url)
        return 0, "Ouvert"

    def help():
        print("Commande :")
        print("- autre imc")
        print("- autre ouvrir")
        return 0,"Voici la liste des commandes du module 'autre'"

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

prefix = "autre"
moduleInstance = Autre
