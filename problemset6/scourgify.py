import csv
import sys
def main():
    try:
        with open(sys.argv[1]) as before,open(sys.argv[2],'w') as after:
            reader=csv.DictReader(before)
            fieldname=["first","last","house"]
            writer=csv.DictWriter(after, fieldnames=fieldname)
            writer.writeheader()
            for line in reader:
                last, first=line["name"].split(sep=",")
                writer.writerow({"first":first, "last":last,"house":line["house"]})



    except IndexError:
        print("Too few or more argument")
    except FileNotFoundError:
        print("Invalid file")

if __name__ =="__main__":
    main()