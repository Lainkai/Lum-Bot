#This is 日本語 (Japanese) for information
#It Loads files and other data.

import json

class joho:
    def __init__(self):
        pass

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
        
        