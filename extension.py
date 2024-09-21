#https://cs50.harvard.edu/python/2022/psets/1/extensions/
def main():
    x=input("File name:").lower().strip()
    name,end=x.split('.')
    if(end=="gif"or end=="jpg"or end=="jpeg"or end=="png"):
        print("image/"+end)
    elif(end=="pdf" or end=="zip"):
        print("Application/"+end)
    elif(end=="txt"):
        print("text/plain")
    else:
        print("application/octet-stream")


main()