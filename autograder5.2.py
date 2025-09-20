# Autograder exercise 5.2
largest = None
smallest = None
while True:
    userNum = input("Enter a number: ")
    # Check for exit word
    if userNum == "done":
        break

    # try converting to float
    try:
        num = int(userNum)
    # Print error message
    except:
        print("Invalid input")
        continue
    
    # Determine largest
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

     # Determine the smallest
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

# Print output
print("Maximum is", largest)
print("Minimum is", smallest)
