from math import *


class Math:
    def info(self, zolo, module, args):
        """
        Info about Math module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Math] Version {module.version}")

    def eval(self, zolo, module, args):
        """
        Make a calcul

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        try:
            print(f"[Math] {eval(' '.join(args))}")
        except Exception as e:
            print(f"[ERREUR] {e}")

    def imc(self, zolo, module, args):
        """
        Calculate IMC

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        size = input("Votre taille en mètres : ")
        weight = input("Votre poids en kg : ")
        imc = int(weight) / float(size) ** 2

        print(f"[Math] Votre IMC est de {imc}")
        if imc < 16.5:
            print("[Math] Vous êtes en famine")
        elif imc < 18.5:
            print("[Math] Vous êtes en état de maigreur")
        elif imc < 25:
            print("[Math] Vous avez une corpulence normale")
        elif imc < 30:
            print("[Math] Vous êtes en surpoid")
        elif imc < 35:
            print("[Math] Vous êtes en état d'obésité modérée")
        elif imc < 40:
            print("[Math] Vous êtes en état d'obésité sévère")
        else:
            print("[Math] Vous êtes en état d'obésité morbide")
