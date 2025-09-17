def thing():
    print("Hello")
    print("Fun")

thing()
print("This is not from thing()")
thing()

# Prompt user for input on a language
language = input("Choose a language, es, fr, or other ")

# Define function to read the language and respond
def greet(language):
    if language == "es":
        return "Hola"
    elif language == "fr":
        return "Bonjour"
    else:
        return "Hello"
    
# Call the greet function
print(greet(language))



# Define the compute pay function
def computePay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * (1.5 * rate))
        return pay
    else:
        pay = hours * rate
        return pay

# Ask users for theirs hours and their rate
userHours = input("Enter your hours: ")
userRate = input("Enter your rate: ")

# store their pay in a variable
myPay = computePay(float(userHours), float(userRate))

# Print the variable
print(myPay)
