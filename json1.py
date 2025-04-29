import json 
import urllib.request

url = input('Enter URL: ') #ask for a URL

with urllib.request.urlopen(url) as url: #sends request and opens url
    data = json.loads(url.read().decode()) #loads json format, reads, and decodes it
total = 0

info = data.get('comments') #gets the values under comments and puts them into info

for person in range(len(info)): #starts looping through the length of ifo
    pers = info[person] # separates each person from the list into pers
    value = pers.get('count') # gets the count from each person in pers
    total += int(value) #adds value to total
    
print(total)

    