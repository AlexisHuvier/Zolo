import contextlib
import wikipedia
import webbrowser
wikipedia.set_lang("fr")


class Wikipedia:
    def info(self, zolo, module, args):
        """
        Info about Wikipedia module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Wikipedia] Version {module.version}")
        
    def random(self, zolo, module, args):
        """
        Get random wikipedia page

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        while True:
            with contextlib.suppress(Exception):
                name = wikipedia.random()
                page = wikipedia.page(name)
                print("[Wikipedia] Voici les informations de la page random :")
                print(f"            - Titre : {page.title}")
                print(f"            - Résumé : {wikipedia.summary(name)}")
                rep = input("[Wikipedia] Voulez vous ouvrir la page (y/n) : ")
                if rep == "y":
                    webbrowser.open(page.url)
                break
    
        
    def search(self, zolo, module, args):
        """
        Make wikipedia search

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        results = wikipedia.search(" ".join(args), 5)
        print("[Wikipedia] Voici les résultats de la recherche :")
        for i in results:
            print(f"            - {i}")
        
    def page(self, zolo, module, args):
        """
        Get wikipedia page of something

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        try:
            page = wikipedia.page(" ".join(args))
            print("[Wikipedia] Voici les informations de la page :")
            print(f"            - Titre : {page.title}")
            print(f"            - Résumé : {wikipedia.summary(' '.join(args))}")
            rep = input("[Wikipedia] Voulez vous ouvrir la page (y/n) : ")
            if rep == "y":
                webbrowser.open(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"[Wikipedia] L'intitulé est ambigu. Voici les possibilités : {', '.join(e.options)}")
        except wikipedia.exceptions.PageError as e:
            print("[Wikipedia] Page inconnue")
