# Parsing through strings

# While loop to parse
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
print()

# For loop to parse
fruit = "banana"
index = 0
for letter in fruit:
    print(index, letter)
    index += 1
print() 

# For loop counting a letter
count = 0
for letter in fruit:
    if letter == "a":
        count += 1
    print(letter)

print("There were", count, "a's in the variable fruit, wihch was the word", fruit)
print()

# Slicing strings
stringToSlice = "Monty Python"
print(stringToSlice[0:4], "Called [0:4]")
print(stringToSlice[6:7], "Called [6:7]")
print(stringToSlice[0:20], "Called [0:20]")
print()

print(stringToSlice[:4], "Called [:4]")
print(stringToSlice[6:], "Called [6:]")
print()

fruit = "apple"
print("p" in fruit)
print("n" in fruit)
print("ple" in fruit)
if "a" in fruit:
    print("Found it")

# Parsing strings and extracting data
data = "From stephen.marquard@uct.ac.za Sat Jan. 5 09:14:16 2008"
atpos = data.find("@")
print("The @ symbol is found at position", atpos)
print()

sppos = data.find(" ",atpos)
print("The firat space after the @ symbol is found at position", sppos)
print()

host = data[atpos : sppos]
print("The school'  s email address is", host)
print()

# Replace parts of strings
greet = "Hello Bob"
newGreeting = greet.replace("Bob", "Becca")
print("Original greeting:", greet)
print("New greeting:", newGreeting)
print("Original greeting again:", greet)
print()

# Autograder exercise: 6.5
# Write a program using find() and string splicing to extract the number at the end of the line
# Convert the number to floating point, and print it out

text = "X-DSPAM-Confidence:    0.8475"

# Reverse the string
textBackwards = text[::-1]

# Find the first space in textBackwards and subtract from the length of text to find last space of text
lastSpace = len(text) - textBackwards.find(" ")

# Slice the string after the last space
number = text[lastSpace:]

print(float(number))
