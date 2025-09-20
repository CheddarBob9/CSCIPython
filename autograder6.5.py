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
