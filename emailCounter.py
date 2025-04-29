# easy way to open file for testing, thanks py4e
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
    
# opens file
handle = open(filename)

#empty dictionary
counts = dict()
# for each line in file
for line in handle:
    if "From " in line:                # if line has From
        words = line.split()           # splits line into list
        for word in words:             # loops through word list
            if "@" in word:            # if contains @ for email, then add to dict with counter
                counts[word] = counts.get(word, 0) + 1
    else:
        continue                       # or continue to next line

email = None           
amount = None
for ename, total in counts.items():
    if email is None or total > amount:
        email = ename
        amount = total

print(email, amount)