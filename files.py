xfile = open('mbox.txt')
count = 0 
for line in xfile:
    count += 1
print(f"Line Count: {count}")