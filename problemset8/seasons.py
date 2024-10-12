import datetime
from datetime import timedelta
import re
import inflect
import sys


def main():
    date=input("Date of birth:")
    try:
        match=re.match(r"^(\d{4})-(\d{2})-(\d{2})$",date) 
        if match:
            p = inflect.engine()
            birth=datetime.date(int(match.group(1)),int(match.group(2)),int(match.group(3)))
            today=datetime.date.today()
            t3=today-birth
            minute=timedelta(t3.days)
            print(f"{p.number_to_words(minute.total_seconds()/60)} minutes")

    except:
        sys.exit()



...


if __name__ == "__main__":
    main()