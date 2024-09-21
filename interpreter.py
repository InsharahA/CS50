def main():
    #https://cs50.harvard.edu/python/2022/psets/1/interpreter/
    exp=input("Expression:")
    x,y,z=exp.split(" ")
    match y:
        case '+':
            print(float(x)+float(z))
        case '-':
            print(float(x)-float(z))
        case '*':
            print(float(x)*float(z))
        case '/':
            print(float(x)/float(z))
main()