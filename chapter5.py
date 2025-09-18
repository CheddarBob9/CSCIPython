# Loops and Iterations
import time

# Indefinite loops

# The most basic of loops
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")
print(n)

# A loop with a break statement
while True:
    line = input("Enter anything, and 'done' when finished: ")
    if line == "done":
        break
    print(line)
print("Done!")



# Definite loops
for i in [5, 4, 3, 2, 1]:
    print(i)
    time.sleep(2)
print("Blastoff!")

friendList = ["Joseph", "Glenn", "Sally"]
for friend in friendList:
    print("Happy Birthday,", friend)
print("#2025")



# Loop idioms / smart loops
print("Before loop")
for thing in [14, 545, 25, 36, 67, 92, 5, 1]:
    print(thing)
print("After loop")

# Loop to determine largest number
maxNum = 0
for number in [14, 545, 25, 36, 67, 92, 5, 1]:
    if number > maxNum:
        maxNum = number
    print(number)
    print(maxNum)

print("Done", maxNum, "is the largest number in the set")
