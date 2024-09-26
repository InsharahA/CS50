import sys
import inflect
def main():
    namelist=[]
    while True:
        try:
            name=input("Name:")
            namelist.append(name)
        except EOFError:
            song(namelist)
            sys.exit()

def song(namelist):
    p = inflect.engine()
    print("Adieu, adieu, to ",p.join(namelist))

main()