import os
import googleapiclient.discovery
import webbrowser


class YouTube:
    api = open("modules/YouTube/apiKey.txt").read() if os.path.exists("modules/YouTube/apiKey.txt") else ""
    api_service_name = "youtube"
    api_version = "v3"
    youtube =  googleapiclient.discovery.build( api_service_name, api_version, developerKey = api) if api != "" else None

    def info(zolo, module, args):
        """
        Info about Math module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[YouTube] Version {module.version}")
        print(f"[YouTube] API Key : {YouTube.api if YouTube.api else 'Aucune'}")
        
    def searchchannel(zolo, module, args):
        """
        Search a channel

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if YouTube.youtube:
            response = YouTube.youtube.search().list(
                part="id,snippet",
                type='channel',
                q=" ".join(args),
                maxResults=5
            ).execute()
            if response:
                print("[YouTube] Résultats de la recherche :")
                for i, item in enumerate(response['items'], 1):
                    print(f"          {i}. {item.get('snippet').get('channelTitle')} - {item.get('id').get('channelId')}")
                nb = input("[YouTube] Pour aller à la vidéo, tapez son numéro ou rien : ")
                if nb.isdigit() and 1 <= int(nb) <= len(response["items"]):
                    webbrowser.open("https://www.youtube.com/channel/"+response["items"][int(nb) - 1]["id"]["channelId"])
            else:
                print("[ERREUR] Aucun résultat")
        else:
            print("[ERREUR] YouTube API Key manquante")
        
    def searchvideo(zolo, module, args):
        """
        Search a video

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if YouTube.youtube:
            response = YouTube.youtube.search().list(
                part="id,snippet",
                type='video',
                q=" ".join(args),
                maxResults=5
            ).execute()
            if response:
                print("[YouTube] Résultats de la recherche :")
                for i, item in enumerate(response['items'], 1):
                    print(f"          {i}. {item.get('snippet').get('title')} ({item.get('snippet').get('channelTitle')}) - {item.get('id').get('videoId')}")
                nb = input("[YouTube] Pour aller à la vidéo, tapez son numéro ou rien : ")
                if nb.isdigit() and 1 <= int(nb) <= len(response["items"]):
                    webbrowser.open("https://www.youtube.com/watch?v="+response["items"][int(nb) - 1]["id"]["videoId"])
            else:
                print("[ERREUR] Aucun résultat")
        else:
            print("[ERREUR] YouTube API Key manquante")
            
    def stats(zolo, module, args):
        """
        Search a video

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if YouTube.youtube:
            response = YouTube.youtube.videos().list(
                part="statistics,contentDetails",
                id=args[0],
                fields="items(statistics," + \
                            "contentDetails(duration))"
            ).execute()
            if response:
                print("[YouTube] Voici les statistiques :")
                print("          Durée :", response["items"][0]["contentDetails"]["duration"])
                print("          Nombre de vues :", response["items"][0]["statistics"]["viewCount"])
                print("          Nombre de likes :", response["items"][0]["statistics"]["likeCount"])
                print("          Nombre de favorites :", response["items"][0]["statistics"]["favoriteCount"])
                print("          Nombre de commentaires :", response["items"][0]["statistics"]["commentCount"])
            else:
                print("[ERREUR] Vidéo inconnue")
        else:
            print("[ERREUR] YouTube API Key manquante")
