import subprocess
import sys

def main():
    cmd = (sys.executable, "lamu.py")
    code = subprocess.call(cmd)
    print(code)

def verify_git():
    return True 

if __name__ == "__main__":
    if not verify_git():
        "Please install git!"
    else:
         main()