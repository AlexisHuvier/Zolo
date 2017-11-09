import os, getpass, hashlib
from Zolo_main import *
from Zolo_function import *

try:
    with open('config.txt'):
        pass
except IOError:
    print("Bonjour, je suis Zolo.")
    print("Apparemment, je ne vous connais pas. \nIl me faudrait quelques informations.")
    play("Bonjour, je suis Zolo. Apparemment, je ne vous connais pas. Il me faudrait quelques informations.")
    play("Tout d'abord votre nom")
    nom=input("Tout d'abord votre nom : ")
    play("Puis votre mot de passe")
    mdp=getpass.getpass("Puis votre mot de passe (pour plus de sécurité) : ")
    mon_fichier = open("config.txt", "w")
    mon_fichier.write(nom+"\n"+str(hashlib.md5(mdp.encode('utf8')).hexdigest()))
    mon_fichier.close()
    print("\nEnregistrement fini !")
    print("Merci de me redémarrer pour finaliser la configuration.")
    play("Enregistrement fini ! Merci de me redémarrer pour finaliser la configuration.")
    input()
else:
    mon_fichier=open("config.txt","r")
    contenu=mon_fichier.read().split("\n")
    mon_fichier.close()
    print("Bonjour "+contenu[0])
    play("Bonjour "+contenu[0])
    a=0
    while a!=1:
        play("Entrez votre mot de passe")
        mdp=getpass.getpass("Entrez votre mot de passe : ")
        if str(hashlib.md5(mdp.encode('utf8')).hexdigest())==contenu[1]:
            a=1
            print("\nMot de passe accepté !")
            play("Bon mot de passe")
        else:
            print("\nMauvais mot de passe !\n")
            play("Mauvais mot de passe !")
    input()
    assistant()
    os.system("cls")
    print("Au revoir, "+contenu[0])
    play("Au revoir "+contenu[0])
    input()
