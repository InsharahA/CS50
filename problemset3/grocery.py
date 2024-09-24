def main():
    grocery={}
    while(True):
        try:
            item=input()
        except EOFError:
            break
        else:
            item=item.upper()
            if grocery.get(item) is None:
                grocery.update({item:1})
            else:
                grocery.update({item:grocery.get(item)+1})
    for key in grocery:
        print(grocery.get(key)," ",key)
            



main()