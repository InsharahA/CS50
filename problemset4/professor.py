import random


def main():
    score=0
    level=get_level()
    
    for i in range(10):
        Flag=False
        
        x=generate_integer(level)
        y=generate_integer(level)
        for j in range(3):
            print(x," + ",y," = ", end="")
            ans=int(input())
            if(ans ==(x+y)):
                score+1
                Flag=True
                break
            else: 
                print("EEE")
        if (not Flag):
            print(x," + ",y," = ", (x+y) )
        print()
    print("Score:",score)





def get_level():
    while True:
        try:
            level=int(input("Level:"))
            if(level not in [1,2,3]):
                raise ValueError
            else: 
                return level
        except ValueError:
            pass


def generate_integer(level):
    lower_bound = 10**(level - 1)
    upper_bound = 10**level- 1
    
    return random.randint(lower_bound, upper_bound)


if __name__ == "__main__":
    main()