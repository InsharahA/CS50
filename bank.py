def main():
    x=input("Greeting:").lower().strip()

    if (x.startswith("hello",0,5)):
        print("$0")
    elif("h"==x[0]):
        print("$20")
    else:
        print("100")
main()