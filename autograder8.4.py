# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words
# Using the split() method. The program should build a list of words.
# For each word on rach line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# Handle to parse data
fhand = open("chapter8Data.txt")

# List 
wordsList = list()

# For loop to run through the text and split by line
for line in fhand:
    line = line.split()
    # Inner for loop to run through the line and split by word
    for word in line:
        # Append to list
        if word not in wordsList:
            wordsList.append(word)

# Sort the list
wordsList.sort()

# Print output
print(wordsList)
