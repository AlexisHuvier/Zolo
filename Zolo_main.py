#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, webbrowser, hashlib
from getpass import getpass
from math import *
from Zolo_function import *

global liens

version="0.2.0-Beta"

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
                    listObject(listerep[1])
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
                    recherche=reconstituation(listerep,2)
                    url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "ecosia":
                    recherche=reconstituation(listerep,2)
                    url="https://www.ecosia.org/search?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "youtube":
                    recherche=reconstituation(listerep,2)
                    url = "https://www.youtube.com/results?search_query="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "duckduckgo":
                    recherche=reconstituation(listerep,2)
                    url = "https://duckduckgo.com/?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "bing":
                    recherche=reconstituation(listerep,2)
                    url = "https://www.bing.com/search?q="+recherche
                    webbrowser.open_new(url)
                elif listerep[1] == "yahoo":
                    recherche=reconstituation(listerep,2)
                    url = "https://fr.search.yahoo.com/search?p="+recherche
                    webbrowser.open_new(url)
                else:
                    recherche=reconstituation(listerep,1)
                    url = "https://www.google.fr/?gws_rd=ssl#q="+recherche
                    webbrowser.open_new(url)
            elif listerep[0]=="meteo":
                ville=listerep[1]
                code=listerep[2]
                url = 'http://www.meteofrance.com/previsions-meteo-france/'+ville+"/"+code
                webbrowser.open_new(url)
            elif listerep[0]=="ouvrir":
                url=reconstituation(listerep,1)
                os.popen(url)
            elif listerep[0]=="raccourci":
                if listerep[1]=="create":
                    url=reconstituation(listerep,3)
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
                            url=reconstituation(listerep,1)
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
                            url=reconstituation(listerep,1)
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
                    input()
            elif listerep[0]=="crypter":
                try:
                    cle=int(listerep[1])
                    if cle<1 or cle>26:
                        0/0
                except:
                    print("ERREUR : Faites 'crypter <clé> <texte>' avec 0<clé<27")
                    print("")
                else:
                    texte=""
                    for i in listerep:
                        if i == listerep[0] or i == listerep[1]:
                            pass
                        elif i == listerep[len(listerep)-1]:
                            texte+=i
                        else:
                            texte+=i+" "
                    if texte==" ":
                        print("ERREUR : Faites 'crypter <clé> <texte>' avec 0<clé<27")
                        print("")
                    else:
                        result=""
                        for i in texte.upper():
                            result+=codage(i, cle)
                        print(result)
                        print("")
                        input()
            elif listerep[0]=="decrypter":
                try:
                    cle=int(listerep[1])
                    if cle<1 or cle>26:
                        0/0
                except:
                    print("ERREUR : Faites 'decrypter <clé> <texte>' avec 0<clé<27")
                    print("")
                else:
                    texte=""
                    for i in listerep:
                        if i == listerep[0] or i == listerep[1]:
                            pass
                        elif i == listerep[len(listerep)-1]:
                            texte+=i
                        else:
                            texte+=i+" "
                    if texte==" ":
                        print("ERREUR : Faites 'crypter <clé> <texte>' avec 0<clé<27")
                        print("")
                    else:
                        result=""
                        for i in texte.upper():
                            result+=decodage(i, cle)
                        print(result)
                        print("")
                        input()
            elif listerep[0]=="decrypter*":
                texte=""
                for i in listerep:
                    if i == listerep[0]:
                        pass
                    elif i == listerep[len(listerep)-1]:
                        texte+=i
                    else:
                        texte+=i+" "
                if texte==" ":
                    print("ERREUR : Faites 'crypter <clé> <texte>' avec 0<clé<27")
                    print("")
                else:
                    for cle in range(1,27):
                        result=""
                        for i in texte.upper():
                            result+=codage(i, cle)
                        print(result)
                    print("")
                    input()
            elif listerep[0]=="info":
                print("Salut, comme tu le sais, je suis Zolo !")
                print("Je suis un assistant qui peut faire plein de choses (fait 'aide' pour avoir la liste")
                print("Je suis en version",version,"et j'ai été crée par LavaPower")
                print("")
                input()
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
                print("- meteo <ville> <code postal> : Donne la météo d'une ville (a écrire sans majuscule ni accent)")
                print("- ouvrir <lien programme> : Ouvrir un programme à partir d'un lien")
                print("- raccourci <create|delete|list|open> [<nom>] [<url>] : Commande pour gérer les raccourcis")
                print("- crypter <clé> <texte> : Crypter un texte avec une clé (de 1 à 26)")
                print("- decrypter <clé> <texte> : Décrypter un texte avec une clé (de 1 à 26)")
                print("- decrypter* <texte> : Décrypter un texte sans clé")
                print("- info : Toutes les informations sur Zolo")
                print("- reset : Reset Zolo")
                print("- quitter : Quitter Zolo")
                print("- aide : Montre cette aide")
                input()
            elif listerep[0]=="quitter":
                a=1
            else:
                print("Je n'ai pas compris votre demande")
                print("")
        except:
            pass
    
    
