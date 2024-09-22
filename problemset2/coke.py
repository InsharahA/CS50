def main():
    amount_due=50
    while(True):
        print("Amount due", amount_due)
        if(amount_due==0):
            break
        x=int(input("Insert coin:"))
        if(x in [25,10,5]):
            amount_due=amount_due-x
        


main()