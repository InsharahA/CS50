import random
import sys
def main():
    while True:
     n=input("Level:")
     if n.isdigit() and (int(n)>0):
        num=random.randint(1,int(n))
        while True:
           x=input("Guess:")
           if x.isdigit() and (int(x)>0):

            if(int(x)<num):
                    print("Too small")
            elif (int(x)>num):
                    print("Too Big")
            else:
                    print("Just Right")
                    sys.exit()
                        
           

main()