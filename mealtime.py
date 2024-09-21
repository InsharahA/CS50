#https://cs50.harvard.edu/python/2022/psets/1/meal/
def main():
    time=input("what time is it?")
    x=convert(time)

    if (x>=7.0 and x<=8.0):
        print("Breakfast time")
    elif(x>=12.0 and x<=13.0):
        print("Lunch time")
    elif(x>=18.0 and x<=19.0):
        print("dinner time")


def convert(time):
    hours,minutes=time.split(":")
    minutes=int(minutes)/60
    return(int(hours)+minutes)


if __name__ == "__main__":
    main()