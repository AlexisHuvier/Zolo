from ossapi import *
import os


class OsuAPI:
    def __init__(self):
        if os.path.exists("modules/Osu/auth.txt"):
            credits = [i.strip() for i in open("modules/Osu/auth.txt").readlines()]
            self.api = OssapiV2(int(credits[0]), credits[1])
        else:
            self.api = None
    
    def user(self, id):
        return self.api.user(id)
    
    def user_recent_activity(self, id, limit = 5, offset = 0):
        return self.api.user_recent_activity(id, limit, offset)
