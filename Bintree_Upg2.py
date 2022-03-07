
from bintreeFile import Bintree

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet not in svenska:
            svenska.put(ordet)           # in i sökträdet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r") as file:
    for line in file:
        for word in line.split():
            if word not in engelska:  
                engelska.put(word)
                if word in svenska:
                    print(word)




