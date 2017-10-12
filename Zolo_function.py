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

def listObject(typeObj):
    if typeObj=="moteur":
        print("\nListe des moteurs :")
        print("- Google")
        print("- Youtube")
        print("- Duckduckgo")
        print("- Bing")
        print("- Yahoo")
        print("- Ecosia")
        print("")

def reconstituation(liste,debut):
    result=""
    for i in range(debut,len(liste)):
        if i==len(liste)-1:
            result+=liste[i]
        else:
            result+=liste[i]+"+"
    return result
