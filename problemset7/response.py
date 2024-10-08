import sys
from validator_collection import validators, checkers

def main ():
   email=(input("Enter the email:"))
   print(checkers.is_email(email))


if __name__=="__main__":
    main()