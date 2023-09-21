fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for i in fh:
    words = i.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)