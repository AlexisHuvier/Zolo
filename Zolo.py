from Zolo_main import *

try:
    with open('config.txt'):
        pass
except IOError:
    print("Bonjour, je suis Zolo.")
    print("Apparemment, je ne vous connais pas. \nIl me faudrait quelques informations.")
    nom=input("Tout d'abord votre nom : ")
    mdp=getpass("Puis votre mot de passe (pour plus de sécurité) : ")
    mon_fichier = open("config.txt", "w")
    mon_fichier.write(nom+"\n"+str(hashlib.md5(mdp.encode('utf8')).hexdigest()))
    mon_fichier.close()
    print("\nEnregistrement fini !")
    print("Je vous prie de me redémarrer pour finaliser la nouvelle configuration !")
    input()
else:
    mon_fichier=open("config.txt","r")
    contenu=mon_fichier.read().split("\n")
    mon_fichier.close()
    print("Bonjour "+contenu[0])
    a=0
    while a!=1:
        mdp=getpass("Pour plus de sécurité, il faudrait votre mot de passe : ")
        if str(hashlib.md5(mdp.encode('utf8')).hexdigest())==contenu[1]:
            a=1
            print("\nMot de passe accepté !")
        else:
            print("\nMauvais mot de passe !\n")
    input()
    Assistant()
    os.system("cls")
    print("Au revoir, "+contenu[0])
    input()
