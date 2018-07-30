import os
import sys
import subprocess
import time
import platform
from collections import OrderedDict

LAUNCHER_VERSION = "0.0.0a"
BOT_VERSION = "0.0.0a"

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
IS_64BIT = platform.machine().endswith("64")

NORMIE_MODE = not False #this will be replaced when I add arguments. 
PYTHON_OK = sys.version_info >= (3,5)

CODES = {0:"she is tired, and all is fine.", 26:"reality really is a simulation, and this should have never happend.", 1:"she did not understand something. Everything is dying."}

HEADER =  "▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░»────Lum-Bot────«░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓\n"
VERSION = "▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░»── V. 0.0.0a ──«░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓\n"
IMG = [
    "                     ***/*/**/*                            \n",
    "                  .*,,,,//*,,,*,,*                         \n",
    "                 .,,*,,*//*,*,,,*.,,.                      \n",
    "                 /***,//**////,,/.,,,/                     \n",
    "         .&&&%,   *,*# *%*/*//*,/,,,**.*                   \n",
    "       .%%%%%%%%%&&&#@(&&%@@,,**,,,,,,,,*///*,             \n",
    "         %%///(.  .**&(&%&&/#(,%,,,,,,,,,///**//////       \n",
    "           %%%%&&&/,,*&(&&&%%,,,,,,,,//////,//////**//.    \n",
    "             *%%%&*,,,,((/#%%,,,,/////*,,,,*,,*/*,///*//   \n",
    "                #%%(*,,.#%/%%%,,,,,,,,,,,,,,.,,,,,.,,////  \n",
    "                  .&&&&&&%&&&&&&&&,,,,,,,,,.,,,,,,,,,.,//  \n",
    "                 (,,%%%&&&&&&&%&&&&,.,,,.,,,,,,,,,,,,*,,*/ \n",
    "                 .  *#//###(#%%%%&&#,,,,,,,,,,,,,,,,,,,,,/*\n",
    "                    %%%#....   /%%&&,,,,,,,,,,,,,,,,,,//.**\n",
    "                    (&&&%%(%&%%,(%&&&,,,,,,,,,,,,,,,,,*,/* \n",
    "                      &&&&&&&%%%*%%&&,,,,,,,,,,,,,,,,,/*/  \n",
    "                       &(&&&%%%%%%%%&%,,,,,,,,,,,,,,,,/,   \n",
    "                        &(&&&&#&(((%%&.,,,,,,,,,,,,,,,*/   \n",
    "                        &&&&&/##/%%%%&&,,,,,,,,.,,,*//.*// \n",
    "                        *,//*,&&&&&#%%&&,,,,,,,/////////   \n",
    "                    &&&&&/##/&&&&&%%#%&&#//**///*       /  \n",
    "                 &&&&&&&%%**&&&&&%%%%(%&& *//,             \n",
    "             .&&&&&&&&%%%%(&&&&&%%%%% .%&/                 \n",
    "           &&&&&&&%%%%%%%#&&&&&%%%%%    %&                 \n",
    "         &&&&&%%%%%%%%%%&&&&&&%%%%%      %&/               \n",
    "       &&&&%%%%%%%%%   %&&&&&%%%%%        #&&&&#           \n",
    "      &&&&%%%%/       %&&&&%%%%%*           (%             \n",
    "      %%%%%%%%%(#/   &&&&&%%%%%               (            \n",
    "        .%%%%%%#.# *&&&&%%%%%                              \n",
    "           #%%%# # &&&&%%%%#                               \n",
    "              /#.#&&&%%%%%                                 \n",
    "                 /&&%%%%                                   \n",
    "                 &%%%%%,#                                  \n",
    "                &%%%%%# */                                 \n",
    "               &%%%%%  ,# #                                \n",
    "              (&%%%%(    *#*/                              \n",
    "             ##&%/#       (*(#(##                          \n",
    "            #####          . /###.                         \n",
    "           .### ,#           (,##                          \n",
    "          .*### .              (##                         \n",
    "          .####,               *###                        \n",
    "         #.##/                   ##/                       \n",
    "         (# ,.                                             \n",
    "        ,,#*                                               \n",
    "       .#.#                                                \n",
    "      /(((                                                 \n",
    "      .#,.                                                 \n",
    "     #*#/                                                  \n",
    "    (*##*                                                  \n",
    "    #.##                                                   \n",
    "   ##, .                                                   \n",
    "  .#####                                                   \n",
    "  ######.                                                  \n",
    "  (###*                                                    \n",
    "\n",
    "Source Molly Ketty\n"
]

def play_intro():

    try:
        writer(HEADER)
        for l in IMG:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(.07)
        writer(VERSION)
        time.sleep(1)

    except KeyboardInterrupt:
            clrs()
            return

def writer(stringer, cpm=4500):
    for i in stringer:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(60/cpm)

def clrs():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def menu(title, options, sub=None, is_sub=False):
    """Menu function that builds into command prompt returns the keyword of what the user selected
        Options is a dictionary
    """
    clrs()
    if not is_sub:
        while True:
            print("╔════════════════════╗")#fluff For the title
            print("║##%s##║" % title)
            if not sub == None:
                print("╠═══════════════╦════╝")
                print("║##-%s-##║" % sub)
                print("╚═══════════════╝")
            print()#final fluff for title
            print("Please enter the number for your selection. \n")
            i = 1
            for opt in options:
                print(str(i)+". "+options[opt])
                i+=1
            num = input("> ").lower().strip()
        
            try:
                return list(options.keys()).pop(int(num)-1)
            except IndexError:
                print("Invalid Response, Try Again")
                wait()
                clrs()
    else:
        pass
        

def wait():
    if NORMIE_MODE:
        input("Press enter to continue.")

def run_lum(autorestart=None):
    interpreter = sys.executable

    if interpreter is None:
            raise RuntimeError("Lum could not find an Interpreter.")

    cmd = (interpreter, "lamu.py")

    while True:
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if code == 0:
                break
            elif code == 26:
                print("Lum is never gonna give up Darling!")
                print("Restarting")
                continue
            else:
                if not autorestart:
                    break

    print("Lum has quit and said that %s" % CODES[code])
    if NORMIE_MODE:
        wait()

def verify_git():
    writer("Verifying Git Installation...\n", 2000)
    try:
        subprocess.call(["git","--version"], stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        succ = False
    else:
        succ = True

    if not succ:
        writer("WARNING!\n", 1000)
        print("Not all functionality will work without Git installed.")
        wait()
    return succ

def main():
    play_intro()
    if GIT_INSTALLED:
        dic = OrderedDict([("start", "Start Lum-Bot"),
		("restart", "Start Lum-Bot With Auto Restart in case of an Issue"),
		("update","Update Lum-Bot"),
		("exit","Exit the launcher")])
        
    else:
        dic = {
            "start":"Start Lum-Bot",
            "restart": "Start Lum-Bot With Auto Restart in case of an Issue",
            "exit" : "Exit the Launcher"
        
        }
    while True:
        resp = menu("Lum-Bot Launcher", dic, "Main Menu")
        if resp == "start":
            run_lum()
        elif resp == "restart":
            run_lum(True)
        elif resp == "update":
            exit(1)
        elif resp == "exit":
            exit(0)


if __name__ == "__main__":
    if IS_WINDOWS:
        os.system("TITLE Lum-Bot for Discord")
	
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)

    os.chdir(dirname)
    clrs()
    
    if not PYTHON_OK:
        print("\\( ⴲ 人 ⴲ )/")
        print("Sorry, Lum is afraid of old pythons, so please install python v. 3.5 or 3.6")
        if NORMIE_MODE:
            wait()
        exit(1)    
	
    GIT_INSTALLED = verify_git()
	
    #check thru args
    if NORMIE_MODE:
        main()