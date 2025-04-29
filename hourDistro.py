# easy way to open file for testing, thanks py4e
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
handle = open(filename)

counts = dict()
# for each line in file
for line in handle:
    if "From " in line:                # if line has From
        words = line.split()           # splits line into list
        for word in words:             # loops through word list
            if ":" in word:            # if contains : for time, then add to dict with counter
                time = word.split(":")[0]       # splits time and saves hour slot into var
                counts[time] = counts.get(time, 0) + 1      #adds time and counter to dictionary
    else:
        continue                       

for time, total in sorted(counts.items()): #sorts and prints counted items
    print(time, total)
