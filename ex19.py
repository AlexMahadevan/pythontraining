
# We identify the function we are creating as being called cheese_and_crackers.
# The function requires two inputs that correspond to the amount of cheese and 
# boxes of crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Now we specify what happens when we call this function with our two inputs.
    # First it prints a message with the first input in it.
    print(f"You have {cheese_count} cheeses!")
    # Now we print a message with the second function input in it.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Now we just print another line of this stupid paragraph.
    print("Man that's enough for a party!")
    # Printing yet another line as part of this function. 
    #The \n is for a new line, so it doesn't all run together.
    print("Get a blanket.\n")

# Now we use the function by adding numbers for the two inputs.
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# Now we create new variables to play with the input of our function,
print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Now we run the function with our two new variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Now we run the function with a straight up math equation for the
# two inputs.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Combine the two.
print("And we combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def shed_work(time, blood, money):
    print(f"It took {time} hours to build the fucking shed.")
    print(f"I spilled {} pints of blood from the sheet metal cuts.")
    print(f"In total, I spent {} dollars on the fucking shed.")