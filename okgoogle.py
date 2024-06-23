mylist = []
with open("go.txt", "r") as f:
    for line in f:
        mylist.append(line.strip())
print(mylist)