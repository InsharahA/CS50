import sys
import re

def main ():
   findum(input("Enter the sentence:"))

def findum(text):
    print( len(re.findall(r"\bum\b",text,flags=re.IGNORECASE)))

if __name__=="__main__":
    main()