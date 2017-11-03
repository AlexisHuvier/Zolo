class Texte:

    def chiffrer():
        try:
            cle=int(input("Clé : "))
            if cle<1 or cle>26:
                0/0
        except:
            print("ERREUR : Faites 'texte chiffre' et choisissez une clé entre 0 et 27")
            return 0
        else:
            texteAC=input("Texte à chiffrer : ")
            texteC=""
            for i in texteAC.upper():
                texteC+=codage(i,cle)
            print("Texte chiffré avec la clé",cle,"=",texteC)
            return 0

    def dechiffrerC():
        try:
            cle=int(input("Clé : "))
            if cle<1 or cle>26:
                0/0
        except:
            print("ERREUR : Faites 'texte chiffre' et choisissez une clé entre 0 et 27")
            return 0
        else:
            texteAD=input("Texte à déchiffrer : ")
            texteD=""
            for i in texteAD.upper():
                texteD+=decodage(i,cle)
            print("Texte déchiffré avec la clé",cle,"=",texteD)
            return 0

    def dechiffrer():
        texteAD=input("Texte à déchiffrer : ")
        for cle in range(1,27):
            texteD=""
            for i in texteAD.upper():
                texteD+=decodage(i,cle)
            print("Texte déchiffré avec la clé",cle,"=",texteD)
        return 0

    def help():
        print("Commande :")
        print("- texte chiffrer")
        print("- texte dechiffrerC")
        print("- texte dechiffrer")
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


def codage(lettre, cle):
        nombre = ord(lettre)
        a=0
        if nombre < 65 or nombre > 90:
            a=a
        elif nombre+cle > 90:
            nombre = nombre+cle
            nombre = nombre-26
        elif nombre > 64:
            nombre = nombre +cle
        NLettre = chr(nombre)
        return(NLettre)

def decodage(lettre, cle):
    nombre=ord(lettre)
    a=0
    if nombre <=64 or nombre >= 116:
        a=a
    elif nombre-cle<65:
        nombre=nombre-cle
        nombre = nombre + 26
    elif nombre <=90:
        nombre=nombre-cle
    NLettre = chr(nombre)
    return(NLettre)
    
prefix = "texte"
moduleInstance = Texte
