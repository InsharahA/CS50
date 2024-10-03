import sys
import csv
import tabulate
def main():
    try:
         if (sys.argv[1][-4:]==".csv"):
            try:
                    with open(sys.argv[1]) as file:
                         items=csv.DictReader(file)
                         
                         print(tabulate.tabulate(items,headers="keys", tablefmt="grid"))
            except FileNotFoundError:
                 print("file does not exist")
                 sys.exit()
                 
    except IndexError:
        print("Too few commandline arg")
        sys.exit()

if __name__=="__main__":
    main()