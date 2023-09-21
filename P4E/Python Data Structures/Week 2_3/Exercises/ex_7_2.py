fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    total = total + float(line[20:])
    average = total / count
    
print("Average spam confidence:", average)