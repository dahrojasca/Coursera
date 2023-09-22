name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    emails = line.split()
    email = emails[1]
    counts[email] = counts.get(email, 0) + 1
        
bigcount = None
bigmail = None
for mail,count in counts.items():
    if bigcount is None or count > bigcount:
       bigmail = mail
       bigcount = count
        
print(bigmail, bigcount)