def main():
    x=input("Input:")
    output=""
    for c in x:
        if not(c.lower() in ["a","e","i","o","u"]):
            output+=c
    print(output)


main()