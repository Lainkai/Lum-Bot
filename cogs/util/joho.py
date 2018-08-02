#This is 日本語 (Japanese) for information
#It Loads files and other data.

import json

class joho:

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)     
    
    def save(self, dicti, path):

        with open(path, "w", encoding="utf-8") as f:
            json.dump(dicti,f)
            