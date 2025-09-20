# Open the file "mbox-short.txt" and read it line by line. When you find a line that starts with "From "
# You will parse the From line using aplit() and print out the second word in the line
# Print out a count at the end
# Do not include "From: " with the colon

# List # Not required since we just need to print it out
#emailAddresses = list()
# Count
count = 0

# Handle to parse data
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        count += 1
        pullAddress = line.split()
        #emailAddresses.append(pullAddress[1])
        print(pullAddress[1])

#print(emailAddresses)
print("There were", count, "lines in the file with From as the first word")
