import urllib.request, urllib.parse, urllib.error # does socket work

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt') # this line is essentially handle = open(filename), DOES NOT READ but opens
counts = dict()


for line in fhand: # for line in "file"
    words = line.decode().split() # make a list with from the decoded bytes to strings per line
    for word in words: # inside the list of words per line
        counts[word] = counts.get(word, 0) + 1 # dictionary GETS word if not in dictionary and sets value to 1, then adds 1 if recurring
print(counts)
    # print(line.decode().strip()) # line.decode() decrypts the BYTES from online file into STRINGS + strip() to get rid  of whitespace