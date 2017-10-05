#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, webbrowser, hashlib
from getpass import getpass
from math import *

global liens

def Assistant():
    a=0
    while a!=1:
        print("Que puis-je faire pour vous ?")
        rep=input()
        print("")
        listerep=rep.split(" ")
        try:
            if listerep[0]=="liste":
                if listerep[1]=="moteur":
                    print("\nListe des moteurs :")
                    print("- Google")
                    print("- Youtube")
                    print("- Duckduckgo")
                    print("- Bing")
                    print("- Yahoo")
                    print("- Ecosia")
                    print("")
            elif listerep[0]=="calcul":
                resultat=eval(listerep[1])
                print("Ce calcul fait "+str(resultat))
                print("")
            elif listerep[0]=="imc":
                taille=pow(float(listerep[2]),2)
                imc=int(listerep[1])/taille
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
                input()
            elif listerep[0]=="recherche":
                if listerep[1] == "google":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "ecosia":
                    recherche=""
                    for i in range(2, len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url="https://www.ecosia.org/search?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "youtube":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.youtube.com/results?search_query="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "duckduckgo":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://duckduckgo.com/?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "bing":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.bing.com/search?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "yahoo":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://fr.search.yahoo.com/search?p="+recherche
                    webbrowser.open_new(url)
                else:
                    recherche=""
                    for i in range(1,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                    webbrowser.open_new(url)
            elif listerep[0]=="*recherche":
                if listerep[1] == "google":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "youtube":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.youtube.com/results?search_query="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "duckduckgo":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://duckduckgo.com/?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "bing":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.bing.com/search?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "yahoo":
                    recherche=""
                    for i in range(2,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://fr.search.yahoo.com/search?p="+recherche
                    webbrowser.open_new(url)
                else:
                    recherche=""
                    for i in range(1,len(listerep)):
                        if i==len(listerep)-1:
                            recherche+=listerep[i]
                        else:
                            recherche+=listerep[i]+"+"
                    url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                    webbrowser.open_new(url)
            elif listerep[0]=="meteo":
                ville=listerep[1]
                code=listerep[2]
                url = 'http://www.meteofrance.com/previsions-meteo-france/'+ville+"/"+code
                webbrowser.open_new(url)
            elif listerep[0]=="ouvrir":
                url=""
                for i in range(1,len(listerep)):
                    if i==len(listerep)-1:
                        url+=listerep[i]
                    else:
                        url+=listerep[i]+" "
                os.popen(url)
            elif listerep[0]=="raccourci":
                if listerep[1]=="create":
                    url=""
                    for i in range(3,len(listerep)):
                        if i==len(listerep)-1:
                            url+=listerep[i]
                        else:
                            url+=listerep[i]+" "
                    try:
                        with open('raccourci.txt'):
                            pass
                    except IOError:
                        mon_fichier=open("raccourci.txt","a")
                        mon_fichier.write(listerep[2]+'$'+url)
                        mon_fichier.close()
                    else:
                        mon_fichier=open("raccourci.txt","a")
                        mon_fichier.write("\n"+listerep[2]+'$'+url)
                        mon_fichier.close()
                    print("Enregistré !")
                    print("")
                elif listerep[1]=="list":
                    try:
                        with open('raccourci.txt'):
                            pass
                    except IOError:
                        print("Aucun raccourci.")
                    else:
                        mon_fichier=open("raccourci.txt","r")
                        contenu=mon_fichier.read().split("\n")
                        mon_fichier.close()
                        nb=1
                        for i in contenu:
                            parties=i.split('$')
                            nom=parties[0]
                            url=""
                            for i in range(1,len(parties)):
                                if i==len(parties)-1:
                                    url+=parties[i]
                                else:
                                    url+=parties[i]+" "
                            print(nb,nom,"-",url)
                            nb+=1
                        print("")
                elif listerep[1]=="open":
                    try:
                        with open('raccourci.txt'):
                            pass
                    except IOError:
                        print("Aucun raccourci.")
                    else:
                        mon_fichier=open("raccourci.txt","r")
                        contenu=mon_fichier.read().split("\n")
                        mon_fichier.close()
                        for i in contenu:
                            parties=i.split('$')
                            nom=parties[0]
                            url=""
                            for i in range(1,len(parties)):
                                if i==len(parties)-1:
                                    url+=parties[i]
                                else:
                                    url+=parties[i]+" "
                            if nom==listerep[2]:
                                os.popen(url)
                                break
                elif listerep[1]=="delete":
                    try:
                        with open('raccourci.txt'):
                            pass
                    except IOError:
                        print("Aucun raccourci.")
                    else:
                        mon_fichier=open("raccourci.txt","r")
                        contenu=mon_fichier.read().split("\n")
                        mon_fichier.close()
                        nb=0
                        for i in contenu:
                            parties=i.split('$')
                            nom=parties[0]
                            if nom==listerep[2]:
                                del contenu[nb]
                            nb+=1
                        rac=""
                        nb=0
                        for i in contenu:
                            if nb == len(contenu)-1:
                                rac+=i
                            else:
                                rac+=i+"\n"
                        if rac=="\n" or rac=="":
                            os.remove("raccourci.txt")
                        else:
                            mon_fichier=open("raccourci.txt","w")
                            mon_fichier.write(rac)
                            mon_fichier.close()
                        print("Supprimé !")
                        print("")
                else:
                    print("Voici les arguments possibles :")
                    print("- list : pour lister les raccourcis")
                    print("- open <nom> : pour ouvrir un raccourci")
                    print("- create <nom> <url> : pour créer un raccourci")
                    print("- delete <nom> : pour supprimer un raccourci")
                    print("")
            elif listerep[0]=="reset":
                print("\nJe vais me reset. Si tel est votre désir.")
                input()
                os.remove("config.txt")
                print("Reset terminé.")
                input()
                sys.exit()
            elif listerep[0]=="aide":
                print("\nListe des commandes que je connais :")
                print("- liste <objet>: Liste des objets (moteur)")
                print("- calcul <calcul> : Fait un calcul")
                print("- imc <poids> <taille> : calcul l'imc")
                print("- recherche [<moteur>] <recherche> : Fait une cherche sur un moteur")
                print("- *recherche [<moteur>] <recherche> : Fait une cherche sur un moteur en navigation privée")
                print("- meteo <ville> <code postal> : Donne la météo d'une ville (a écrire sans majuscule ni accent)")
                print("- ouvrir <lien programme> : Ouvrir un programme à partir d'un lien")
                print("- raccourci <create|delete|list|open> [<nom>] [<url>] : Commande pour gérer les raccourcis")
                print("- reset : Reset Zolo")
                print("- quitter : Quitter Zolo")
                print("- aide : Montre cette aide")
                input()
            elif listerep[0]=="quitter":
                a=1
        except:
            pass

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
    
    
