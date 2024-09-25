from pyfiglet import Figlet
import sys
import random
def main ():
    figlet = Figlet()
    if(len(sys.argv)==1):
        str=input("Input:")
        f=random.choice(figlet.getFonts())
        figlet.setFont(font=f)
        print(figlet.renderText(str))
    elif (len(sys.argv)==3):
        if not(sys.argv[1]=="-f" or sys.argv[1]=="-font"):
            print("Invalid entry")
            sys.exit()
        elif (sys.argv[2] not in figlet.getFonts()):
            print("Invalid entry")
            sys.exit()
        else:
            str=input("Input:")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(str))

    else:
        print("Invalid Entry")
        sys.exit()


main()