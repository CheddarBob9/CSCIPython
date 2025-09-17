x = input("Enter an integer: ")
if int(x) < 0 :
    print("Negative number.")
elif int(x) < 10 :
    print("Less than 10.")
elif int(x) < 20 :
    print("Between 10 and 20.")
else :
    print("20 or more.")

aString = input("Enter a string of letters. ")
try:
    newString = int(aString)
except: 
    newString = -1

print(newString)

aString = input("Enter a series of numbers. ")
try:
    newString = int(aString)
except: 
    newString = -1

print(newString)



# String hours and string rate
sh = input("Enter hours: ")
sr = input("Enter rate: ")

# Try converting to float
try: 
    fh = float(sh)
    fr = float(sr)
except:
    # Print error is failed, and quit
    print("Error, please enter numbers only.")
    quit()

# If no failure, calculate pay
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr

# print the outcome
print("Pay:", xp)