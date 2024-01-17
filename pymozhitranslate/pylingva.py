#! /usr/bin/env python
import random
import json
import requests as req
from urllib.parse import quote

class Translator:
    def __init__(self, urls=["https://translate.projectsegfau.lt", "https://mozhi.aryak.me", "https://translate.bus-hit.me"], engine="google", source="auto"):
        self.urls = urls
        self.engine = engine

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
        for i in range(3):
            url = self.build_url("source_languages", query_params)
            try:
                response = req.get(url, timeout=2)
                response.raise_for_status()
                all_languages = response.json()
                lang = {}
                for language in all_languages:
                    name = language['Name']
                    code = language['Id']
                    lang[name] = code
            except (req.exceptions.RequestException, req.exceptions.Timeout, req.exceptions.ConnectionError) as error:
                if i == 0:
                    continue
                else:
                    raise RuntimeError(f"Languages request failed at all atempt: {error}") from error
            return lang

    def translate(self, source, target="en", text=""):
        #if source is empty, set "auto" if engine is google, duckduckgo, deepl, watson
        if source == None:
            if self.engine == "google" or self.engine == "duckduckgo" or self.engine == "deepl" or self.engine == "yandex" or self.engine == "watson":
                # print("Source is empty, setting source to auto")
                source = "auto"
            else:
                raise ValueError("Source is empty see supported languages. Refer to manual for more information")
        
        if text == "" or text == None:
            raise ValueError("Text is empty")
        
        # Check the maximum character limit for each translation engine
        elif self.engine == "google" and len(text) > 5000:
            raise ValueError("Google translate only supports up to 5000 characters")
        
        elif self.engine == "duckduckgo" and len(text) > 1000:
            raise ValueError("Duckduckgo translate only supports up to 1000 characters")
        
        elif self.engine == "deepl" and len(text) > 3000:
            raise ValueError("Deepl translate only supports up to 3000 characters")
        
        elif self.engine == "yandex" and len(text) > 10000:
            raise ValueError("Yandex translate only supports up to 10000 characters")
        
        elif self.engine == "watson" and len(text) > 5000:
            raise ValueError("Watson translate only supports up to 5000 characters")
        # print(f"Translating from {source} to {target}")
        query_params = {
            "from": source,
            "to": target, 
            "text": quote(str(text))
        }

        for i in range(3):
            
            url = self.build_url("translate", query_params)
            
            try:
                response = req.get(url, timeout=5)
                response.raise_for_status()

            except (req.exceptions.RequestException, req.exceptions.ReadTimeout, req.exceptions.ConnectionError) as error:
                if i == 0:
                    continue
                else:
                    raise RuntimeError(f"Translation request failed at all atempt: {error}") from error

            data = response.json()
            return data.get("translated-text")
