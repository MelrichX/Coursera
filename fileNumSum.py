import re

# Ask for file name then open file
file = input('Input file name: ')
handle = open(file)
nums = 0

for line in handle: #Loop that iterates through each line in file
    num = re.findall('[0-9]+', line)    #Creates a list w/ chars [0-9] per line
    for n in num:   # Another loop that iterates through each number taken from lines
        nums += int(n)  # Adds each iterated number to var nums, at end would be sum

    
print(nums)
#sum is 322022