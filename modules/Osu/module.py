from tkinter import EventType
from modules.Osu.osuapi import OsuAPI
from ossapi.enums import *
from datetime import timedelta


class Osu:
    api = OsuAPI()
    
    def info(self, zolo, module, args):
        """
        Info about Osu module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Osu] Version {module.version}")

    def user(self, zolo, module, args):  # sourcery skip: extract-method
        """
        Get user info

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if user := self.api.user(args[0]):
                print(f"[Osu] Utilisateur : {user.username} ({user.id})")
                print(f"      - Actif : {user.is_active} (Dernière visite : {user.last_visit.strftime('%d/%m/%Y à %H:%M') if user.last_visit else '/'})")
                print(f"      - Bot : {user.is_bot} - Supprimé : {user.is_deleted} - Online : {user.is_online} - Supporter : {user.is_supporter} (L'a été : {user.has_supported})")
                print(f"      - Pays : {user.country.name} - Couleur Profile : {user.profile_colour or '/'} - Titre : {user.title or '/'}")
                print(f"      - Twitter : {user.twitter or '/'} - Discord : {user.discord or '/'} - Site : {user.website or '/'}")
                print(f"      - Mode de jeu : {user.playmode} - Style(s) de jeu : {user.playstyle}")
                print(f"      - Nombre de followers : {user.follower_count} - Nombre de posts : {user.post_count}")
                print(f"      - Badges : {', '.join(i.description for i in user.badges)}")
                print(f"      - Total de parties : {sum(i.count for i in user.monthly_playcounts)}")
            else:
                print(f"[Osu] Utilisateur '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : osu user <id>")
        
    def playcounts(self, zolo, module, args):
        """
        Get user playcounts

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if user := self.api.user(args[0]):
                for i in user.monthly_playcounts:
                    print(f"[Osu] {i.start_date.strftime('%m/%Y')} : {i.count}")
            else:
                print(f"[Osu] Utilisateur '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : osu user <id>")
            
    def stats(self, zolo, module, args):
        """
        Get user stats

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if user := self.api.user(args[0]):
                print(f"[Osu] Stats de {user.username} ({user.id})")
                print(f"      - Niveau : {user.statistics.level.current} ({user.statistics.level.progress}%)")
                print(f"      - Score total : {user.statistics.total_score} - Score classé : {user.statistics.ranked_score} - Précision : {user.statistics.hit_accuracy}%")
                print(f"      - Nom de clics : {user.statistics.total_hits} - Combo max : {user.statistics.maximum_combo} - Nombre de replays par les autres : {user.statistics.replays_watched_by_others}")
                print(f"      - Nombre de parties : {user.statistics.play_count} - Temps de jeu : {timedelta(seconds=user.statistics.play_time)}")
                print(f"      - PP {user.statistics.pp} - Rang Pays : {user.statistics.country_rank} - Rang Global : {user.statistics.global_rank}")
                print(f"      - SS+ : {user.statistics.grade_counts.ssh} - SS : {user.statistics.grade_counts.ss} - S+ : {user.statistics.grade_counts.sh} - S : {user.statistics.grade_counts.s} - A : {user.statistics.grade_counts.a}")
            else:
                print(f"[Osu] Utilisateur '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : osu user <id>")
            
    def recent_activity(self, zolo, module, args):
        """
        Get user recent activity

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if user := self.api.user(args[0]):
                print(f"[Osu] Activité récente de {user.username} ({user.id})")
                if len(args) >= 2:
                    ura = self.api.user_recent_activity(args[0], int(args[1]))
                else:
                    ura = self.api.user_recent_activity(args[0])
                for i in ura:
                    match i.type :
                        case EventType.ACHIEVEMENT:
                            print(f"[Osu] Achievement recu : {i.achievement} ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.BEATMAP_PLAYCOUNT:
                            print(f"[Osu] Beatmap {i.beatmap.title} joué {i.count} fois ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.BEATMAPSET_APPROVE:
                            print(f"[Osu] Beatmapset {i.beatmapset.title} approuvé '{i.approval}' ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.BEATMAPSET_DELETE:
                            print(f"[Osu] Beatmapset {i.beatmapset.title} supprimé ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.BEATMAPSET_REVIVE:
                            print(f"[Osu] Beatmapset {i.beatmapset.title} récupéré ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.BEATMAPSET_UPDATE:
                            print(f"[Osu] Beatmapset {i.beatmapset.title} mis à jour ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.BEATMAPSET_UPLOAD:
                            print(f"[Osu] Beatmapset {i.beatmapset.title} uploadé ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.RANK:
                            print(f"[Osu] Rang obtenu {i.rank} sur la beatmap {i.beatmap.title} (GM : {i.mode} - Score : {i.scoreRank}) ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.RANK_LOST:
                            print(f"[Osu] Première place perdue sur la beatmap {i.beatmap.title} (GM : {i.mode}) ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.USER_SUPPORT_AGAIN:
                            print(f"[Osu] Supporte une nouvelle fois Osu ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.USER_SUPPORT_FIRST:
                            print(f"[Osu] Supporte Osu pour la première fois ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.USER_SUPPORT_GIFT:
                            print(f"[Osu] A offert un support à {i.user.username} ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case EventType.USERNAME_CHANGE:
                            print(f"[Osu] {i.user.username} a changé de pseudo (anciennement : {i.user.previousUsername}) ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
                        case _:
                            print(f"[Osu] Event inconnu : {i.type} ({i.created_at.strftime('%d/%m/%Y à %H:%M')})")
            else:
                print(f"[Osu] Utilisateur '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : osu user <id> [<limit>]")
            
    def scores(self, zolo, module, args):
        """
        Get user recent activity

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if user := self.api.user(args[0]):
                print(f"[Osu] Scores de {user.username} ({user.id})")
                if len(args) >= 2:
                    scores = self.api.user_scores(args[0], limit=int(args[1]))
                else:
                    scores = self.api.user_scores(args[0])
                for i in scores:
                    print(f"[Osu] {i.id} - {i.beatmapset.title} ({i.beatmap.mode})")
                    print(f"      - Score : {i.score} - Rang : {i.rank} - PP : {i.pp}")
                    print(f"      - 50 : {i.statistics.count_50} - 100 : {i.statistics.count_100} - 300 : {i.statistics.count_300} - 300g : {i.statistics.count_geki} - 300k : {i.statistics.count_katu} - CS : {i.statistics.count_miss}")        
            else:
                print(f"[Osu] Utilisateur '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : osu user <id> [<limit>]")
    
    def search(self, zolo, module, args):
        """
        Search User

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        if args:
            if users := self.api.search(args[0]):
                print(f"[Osu] Résultats pour '{args[0]}' :")
                for i in users.users.data:
                    print(f"      - {i.username} ({i.id})")
            else:
                print(f"[Osu] Utilisateur '{args[0]}' introuvable")
        else:
            print("[Erreur] Syntaxe : osu user <id> [<limit>]")
