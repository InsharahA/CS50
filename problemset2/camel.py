#https://cs50.harvard.edu/python/2022/psets/2/camel/
def main():
    name = input("Camel case:")
    for i in range(len(name)):
        if(name[i].isupper()):
         name=name[:i]+"_"+name[i].lower()+name[i+1:]


    print(name)

main()