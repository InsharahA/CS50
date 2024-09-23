
    
def main():
    while(True):
        fuel=input("Fraction:")
        x,y=fuel.split("/")
        try:
            x=int(x)
            y=int(y)
            if (x>y):
                raise ValueError
            f=(x/y)*100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break
    if(f<1.0):
        print("E")
    elif(f>99.0):
        print("F")
    else:
        print(round(f),"%")
    


main()