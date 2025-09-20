# Dealing with Files

# handle = open(filename, mode)
# fhand = open("thisIsData.txt", r) # fhand == file handle

# Does not print the file, but allows access to the file
fhand = open("chapter7Data.txt")

# Initialize count variable
count = 0

# !!! For some reason this messes up finding the len and printing the first 20 chars
# For loop to print the file line by line and count the lines
# fhand = open("Chapter7Data.txt")
# for line in fhand:
#     print(line)
#     count += 1

inp = fhand.read()
print(len(inp))
print(inp[:20])

fhand = open("chapter7Data.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
