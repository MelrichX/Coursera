# easy way to open file for testing, thanks py4e
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "romeo.txt"
handle = open(filename)


counts = dict()                   # empty dictionary 
for line in handle:               # loops through each line in file
    words = line.split()          # splits line into list of words
    for word in words:            # for each word in list
        counts[word] = counts.get(word, 0) + 1     # add words to dictionary or +1 if in already
        
        
lst = list()                      # empty list
for key, val in counts.items():   # loops through each key, value in dictionary
    newtup = (val, key)           # creates new tuple w/ () and reverses dict key, value
    lst.append(newtup)            # appends reversed tuple to empty list

lst = sorted(lst, reverse=True)   # sorts list backwards and saves it

for val, key in lst[:10]:         # loops through sorted tuples up to the 10th place
    print(key, val)               # prints values