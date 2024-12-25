from instagrapi import Client, types
from typing import Dict, List

VERSION = 1.1

class InstaF1nder():
    def __init__(self, creds:Dict[str, str]|None=None):
        '''A Class used for finding instagram account information'''
        self.user_informations = {}
        self.creds = creds

    def login(self, creds:Dict[str, str]|None=None) -> types.User:
        '''Login to the API'''
        self.creds = creds if creds else self.creds
        if not creds:
            raise Exception("Credentials is required!")
        
        self.client = Client()

        username = self.creds["username"]
        password = self.creds["password"]
            
        try:
            self.client.login(username, password)
        except Exception as e:
            print("Error when trying to login!")
            raise e

        self.user_informations = self.client.user_info_by_username_v1(username)
        return self.user_informations

    def get_user_info(self, username: str) -> types.User:
        return self.client.user_info_by_username_v1(username)
        
    def get_user_info_by_id(self, user_id: str, use_cache: bool) -> types.User:
        return self.client.user_info(user_id, use_cache)

    def get_user_following(self, username: str, max_amount: int) -> List[types.UserShort]:
        user_id = self.client.user_id_from_username(username)
        return self.client.user_following_v1(user_id, max_amount)
    
    def get_user_followers(self, username: str, max_amount: int) -> List[types.UserShort]:
        user_id = self.client.user_id_from_username(username)
        return self.client.user_followers_v1(user_id, max_amount)
        