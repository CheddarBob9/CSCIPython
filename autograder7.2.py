# Write a program that prompts for a file name then opens that file and reads through the file,
# Looking for lines of the form: X-DSPAM-Confidence:
# Count these lines and extract the floating point values from each of the lines
# Compute the average of those values and produce an output as shown: Average spam confidence: 0.7507185185185187
# Do not use the sum() function or a variables named sum in your solution.

# count vairable to count lines # runningTotal variable to keep the total
count = 0
runningTotal = 0

# Handle to parse data
fhand = open(input("Enter the file name: "))
# For loop to look at each line individually
for line in fhand:
    # If to find specific lines, add count, and find the total
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        line = line.strip()
        pos = line.find(" ")
        runningTotal = runningTotal + float(line[pos + 1:])
        #print(runningTotal)

average = float(runningTotal) / float(count)

#print()
print("Average spam confidence:", average)
