import os
import sys
import subprocess
import time

LAUNCHER_VERSION = "0.0.0a"
BOT_VERSION = "0.0.0a"

NORMIE_MODE = not False #this will be replaced when I add arguments. 
PYTHON_OK = sys.version_info >= (3,5)

CODES = {0:"she is tired, and all is fine.", 26:"reality is a simulation, and this should have never happend.", 1:"she did not understand something. Everything is dying."}

HEADER =  "▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░»────Lum-Bot────«░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓\n"
VERSION = "▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░»── V. 0.0.0a ──«░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓\n"
INTRO_IMG = """
                     ***/*/**/*                            
                  .*,,,,//*,,,*,,*                         
                 .,,*,,*//*,*,,,*.,,.                      
                 /***,//**////,,/.,,,/                     
         .&&&%,   *,*# *%*/*//*,/,,,**.*                   
       .%%%%%%%%%&&&#@(&&%@@,,**,,,,,,,,*///*,             
         %%///(.  .**&(&%&&/#(,%,,,,,,,,,///**//////       
           %%%%&&&/,,*&(&&&%%,,,,,,,,//////,//////**//.    
             *%%%&*,,,,((/#%%,,,,/////*,,,,*,,*/*,///*//   
                #%%(*,,.#%/%%%,,,,,,,,,,,,,,.,,,,,.,,////  
                  .&&&&&&%&&&&&&&&,,,,,,,,,.,,,,,,,,,.,//  
                 (,,%%%&&&&&&&%&&&&,.,,,.,,,,,,,,,,,,*,,*/ 
                 .  *#//###(#%%%%&&#,,,,,,,,,,,,,,,,,,,,,/*
                    %%%#....   /%%&&,,,,,,,,,,,,,,,,,,//.**
                    (&&&%%(%&%%,(%&&&,,,,,,,,,,,,,,,,,*,/* 
                      &&&&&&&%%%*%%&&,,,,,,,,,,,,,,,,,/*/  
                       &(&&&%%%%%%%%&%,,,,,,,,,,,,,,,,/,   
                        &(&&&&#&(((%%&.,,,,,,,,,,,,,,,*/   
                        &&&&&/##/%%%%&&,,,,,,,,.,,,*//.*// 
                        *,//*,&&&&&#%%&&,,,,,,,/////////   
                    &&&&&/##/&&&&&%%#%&&#//**///*       /  
                 &&&&&&&%%**&&&&&%%%%(%&& *//,             
             .&&&&&&&&%%%%(&&&&&%%%%% .%&/                 
           &&&&&&&%%%%%%%#&&&&&%%%%%    %&                 
         &&&&&%%%%%%%%%%&&&&&&%%%%%      %&/               
       &&&&%%%%%%%%%   %&&&&&%%%%%        #&&&&#           
      &&&&%%%%/       %&&&&%%%%%*           (%             
      %%%%%%%%%(#/   &&&&&%%%%%               (            
        .%%%%%%#.# *&&&&%%%%%                              
           #%%%# # &&&&%%%%#                               
              /#.#&&&%%%%%                                 
                 /&&%%%%                                   
                 &%%%%%,#                                  
                &%%%%%# */                                 
               &%%%%%  ,# #                                
              (&%%%%(    *#*/                              
             ##&%/#       (*(#(##                          
            #####          . /###.                         
           .### ,#           (,##                          
          .*### .              (##                         
          .####,               *###                        
         #.##/                   ##/                       
         (# ,.                                             
        ,,#*                                               
       .#.#                                                
      /(((                                                 
      .#,.                                                 
     #*#/                                                  
    (*##*                                                  
    #.##                                                   
   ##, .                                                   
  .#####                                                   
  ######.                                                  
  (###*                                                                                                                                                              

▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░»───Bak3dChips───«░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓\n
"""

def play_intro():
    try:
        writer(HEADER, 4500)
        writer(VERSION, 4500)
        time.sleep(.25)
        writer(INTRO_IMG)
    except KeyboardInterrupt:
            os.system('cls')
            return

def writer(stringer, cpm=300000):
    for i in stringer:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(60/cpm)


def wait():
    if NORMIE_MODE:
        input("Press enter to continue.")

def run_lum(autorestart):
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

    print("Lum quit and has told us that %s" % CODES[code])

    if NORMIE_MODE:
        wait()

def main():
    play_intro()
    run_lum(True)

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)

    os.chdir(dirname)    
    os.system("cls")
    
    if not PYTHON_OK:
        print("\\( ⴲ 人 ⴲ )/")
        print("Sorry, Lum is afraid of old pythons, so please install python v. 3.5 or 3.6")
        if NORMIE_MODE:
            wait()
        exit(1)

    #check thru args
    if NORMIE_MODE:
        main()