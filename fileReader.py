filename = input("Enter file name: ")
file = open(filename)
count = 0
conf = 0


for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        conf += float(line[19::].strip())
    else:
        continue
    
avg = conf / count
print("Average spam confidence:", avg)
