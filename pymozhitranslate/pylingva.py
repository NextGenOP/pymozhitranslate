#! /usr/bin/env python
import random
import json
import requests as req
from urllib.parse import quote

class Translator:
        
    def __init__(self, url=["https://translate.projectsegfau.lt", "https://mozhi.aryak.me"], engine="google"):
        try:
            self.urls = url
            self.engine = engine
        except req.exceptions.RequestException as er:
            print(er)
            exit()
        except req.exceptions.ConnectionError as er:
            print(er)
            exit()
        except req.exceptions.Timeout as er:
            print(er)
            exit()

    def build_url(self, endpoint, query_params):
        current_url = random.choice(self.urls)
        url = f"{current_url}/api/{endpoint}"
        query_string = "&".join([f"{key}={value}" for key, value in query_params.items()])
        url += f"?engine={self.engine}&{query_string}"
        return url

    def languages(self):
        query_params = {
            "engine": self.engine
        }
        url = self.build_url("source_languages", query_params)
        all_languages = req.get(url).json()
        lang = {}
        for language in all_languages:
            name = language['Name']
            code = language['Id']
            lang[name] = code
        return lang

    def translate(self, source, target, text):
        query_params = {
            "from": source,
            "to": target,
            "text": quote(text)
        }
        url = self.build_url("translate", query_params)
        print(url)
        r = req.get(url)
        r = r.json()
        result = r['translated-text']
        return result