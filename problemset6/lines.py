import sys
def main():
    lines=[]
    count=0
    try:
        if (sys.argv[1][-3:]==".py"):
            try:
                with open(sys.argv[1]) as file:
                    for line in file.readlines():
                        if (not line.startswith('#') and line!="\n"):
                            count+=1
        

            except FileNotFoundError:
                print("File not found")
                sys.exit()


    except IndexError:
        print("Too few command line argument")
        sys.exit()
    else:
        print(count)
    
main()