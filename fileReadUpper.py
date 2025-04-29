# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    with open(fname, "r") as file:
        for line in file:
            print(line.upper().rstrip())
except FileNotFoundError:
    print("Error, File not found")