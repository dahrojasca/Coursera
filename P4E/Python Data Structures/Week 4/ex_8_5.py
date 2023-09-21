fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for ln in fh:
    if not ln.startswith("From "):
        continue
    count = count + 1
    words = ln.split()
    print(words[1])

print("There were", count, "lines in the file with From as the first word")