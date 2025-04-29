largest = None
smallest = None
while True:
    user_input = input("Enter an integer number (or 'done' to finish): ")
    if user_input == 'done':
        break
    try:
        num = int(user_input)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

