# easy way to open file for testing, thanks py4e
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

fileread = open(filename)
count = 0
emails = list()

for line in fileread:
    if "From " in line:  #checks to see line contains 'From '
        count += 1 #adds a counter to count
        lst =  line.split() #splits line into list at whitespace
        emails.append(lst[1]) # appends email from list into email
    
    else:
        continue        
        
for email in emails:
    print(email)
print("There were", count, "lines in the file with From as the first word")
