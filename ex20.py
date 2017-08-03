
# First we import our all important argv module.
from sys import argv

# Now we unpack it and tell it what to look for when we run it 
# in Terminal.
script, input_file = argv

# Now we're defining a function, called print_all, that will print an
# entire file that we're messing around with.
def print_all(f):
    print(f.read())

# Now we're defining another function, that sets us on the 0 byte of the file
# we're messing around with.
def rewind(f):
    f.seek(0)

# Now we're definining yet another funtion that has two inputs. The first
# is defining and printing the line of the file we're messing around with and the 
# second is the actual content of it.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# We have to open the file we're going to play with.
current_file = open(input_file)

print("First let's print the whole file:\n")

# We use our print_all function on the file we're messing around with to print
# the whole thing.
print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

# We use our rewind function to go back to beginning of the file.
rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
