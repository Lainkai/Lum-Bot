import sys
import time
from pyfiglet import Figlet

HEADER = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"

IMG = [
    "                     ***/*/**/*                            ",
    "                  .*,,,,//*,,,*,,*                         ",
    "                 .,,*,,*//*,*,,,*.,,.                      ",
    "                 /***,//**////,,/.,,,/                     ",
    "         .&&&%,   *,*# *%*/*//*,/,,,**.*                   ",
    "       .%%%%%%%%%&&&#@(&&%@@,,**,,,,,,,,*///*,             ",
    "         %%///(.  .**&(&%&&/#(,%,,,,,,,,,///**//////       ",
    "           %%%%&&&/,,*&(&&&%%,,,,,,,,//////,//////**//.    ",
    "             *%%%&*,,,,((/#%%,,,,/////*,,,,*,,*/*,///*//   ",
    "                #%%(*,,.#%/%%%,,,,,,,,,,,,,,.,,,,,.,,////  ",
    "                  .&&&&&&%&&&&&&&&,,,,,,,,,.,,,,,,,,,.,//  ",
    "                 (,,%%%&&&&&&&%&&&&,.,,,.,,,,,,,,,,,,*,,*/ ",
    "                 .  *#//###(#%%%%&&#,,,,,,,,,,,,,,,,,,,,,/*",
    "                    %%%#....   /%%&&,,,,,,,,,,,,,,,,,,//.**",
    "                    (&&&%%(%&%%,(%&&&,,,,,,,,,,,,,,,,,*,/* ",
    "                      &&&&&&&%%%*%%&&,,,,,,,,,,,,,,,,,/*/  ",
    "                       &(&&&%%%%%%%%&%,,,,,,,,,,,,,,,,/,   ",
    "                        &(&&&&#&(((%%&.,,,,,,,,,,,,,,,*/   ",
    "                        &&&&&/##/%%%%&&,,,,,,,,.,,,*//.*// ",
    "                        *,//*,&&&&&#%%&&,,,,,,,/////////   ",
    "                    &&&&&/##/&&&&&%%#%&&#//**///*       /  ",
    "                 &&&&&&&%%**&&&&&%%%%(%&& *//,             ",
    "             .&&&&&&&&%%%%(&&&&&%%%%% .%&/                 ",
    "           &&&&&&&%%%%%%%#&&&&&%%%%%    %&                 ",
    "         &&&&&%%%%%%%%%%&&&&&&%%%%%      %&/               ",
    "       &&&&%%%%%%%%%   %&&&&&%%%%%        #&&&&#           ",
    "      &&&&%%%%/       %&&&&%%%%%*           (%             ",
    "      %%%%%%%%%(#/   &&&&&%%%%%               (            ",
    "        .%%%%%%#.# *&&&&%%%%%                              ",
    "           #%%%# # &&&&%%%%#                               ",
    "              /#.#&&&%%%%%                                 ",
    "                 /&&%%%%                                   ",
    "                 &%%%%%,#                                  ",
    "                &%%%%%# */                                 ",
    "               &%%%%%  ,# #                                ",
    "              (&%%%%(    *#*/                              ",
    "             ##&%/#       (*(#(##                          ",
    "            #####          . /###.                         ",
    "           .### ,#           (,##                          ",
    "          .*### .              (##                         ",
    "          .####,               *###                        ",
    "         #.##/                   ##/                       ",
    "         (# ,.                                             ",
    "        ,,#*                                               ",
    "       .#.#                                                ",
    "      /(((                                                 ",
    "      .#,.                                                 ",
    "     #*#/                                                  ",
    "    (*##*                                                  ",
    "    #.##                                                   ",
    "   ##, .                                                   ",
    "  .#####                                                   ",
    "  ######.                                                  ",
    "  (###*                                                    ",
    "",
    "Source Molly Ketty\n\n"
]

def play(version="", release_notes=None):
    f = Figlet(font="Broadway")
    print(HEADER)
    print(f.renderText("LUM"))
    print(f.renderText("BOT"))
    print(HEADER)
    time.sleep(.5)
    for l in IMG:
        sys.stdout.write("\n"+l)
        sys.stdout.flush()
        time.sleep(.046)
    f.setFont(font="Modular")
    time.sleep(.5)
    print(HEADER)
    print(f.renderText("V. "+version))
    print(HEADER)
    time.sleep(.5)

if __name__ == "__main__":
    play()