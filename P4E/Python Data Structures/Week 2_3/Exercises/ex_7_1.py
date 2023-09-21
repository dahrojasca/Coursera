fname = input("Ingresa el nombre del archivo: ")
fh = open(fname)

for line in fh:
    line = line.rstrip().upper()
    print(line)
