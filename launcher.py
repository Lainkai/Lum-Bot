import subprocess
import sys
import cogs.util.intro as intro
from cogs.util.settings import Settings

def main():
    cmd = (sys.executable, "lamu.py")
    while True:
        code = subprocess.call(cmd)
        if code == 86:
            print("Restarting Lum")
            continue
        else: break
        

def verify_git():
    return True 

if __name__ == "__main__":
    settings = Settings()
    if not verify_git():
        "Please install git!"
    else:
        intro.play(settings.version)
        main()