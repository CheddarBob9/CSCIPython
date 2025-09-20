# Data structures

# Creates a list
listNames = ["Sally", "Glenn", "Bob"]

# Print the whole list
print(listNames)

# Print one index of the list
print(listNames[1])

# Create a list and print it
listNumbers = [10, 69, 12, 42, 1742, 1749, 23, 9]
print("listNumbers", listNumbers)
print()

# Built in sorting
listNumbers.sort()
print("listNumbers sorted", listNumbers)
print()

# Append to add items 
listNumbers.append(77)
print("append 77 to listNumbers", listNumbers)
print()

# Built in sorting
listNumbers.sort()
print("listNumbers sorted again", listNumbers)
print()

# Boolean to find if something is an index of a list
print("Is 9 in listNumbers?:", 9 in listNumbers)
print()

# Create a list, ask for user input and append to list
userList = list()

while True:
    inp = input("Enter a number, done when finished: ")
    # End value
    if inp == "done": break
    # Convert to float
    userValue = float(inp)
    userList.append(userValue)

# Print output
average = sum(userList) / len(userList)
print("Average:", average)
print()

# Create a string, split the string into a list
stringOfWords = "This is a string of words"
print(stringOfWords)

listOfWords = stringOfWords.split()
print(listOfWords)
print()

# open chapter7Data.txt # Split any line starting with "From " # Print index 2, should be the day of the week
fhand = open("chapter7Data.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        sectionedLines = line.split()
        print(sectionedLines[2])
