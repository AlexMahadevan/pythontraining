
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# we print a pessage here then open the file
# the w means it's in write mode, it overwrites the files

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# This writes the lines we were propmted to give, I added some extra white space
# with the \n things

target.write(line1)
target.write("\n")
target.write("\n")
target.write(line2)
target.write("\n")
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
