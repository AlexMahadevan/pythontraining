from sys import argv

script, user_name, age = argv
prompt = 'Answer: '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Now that you are {age}, let's have a talk.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input()

print(f"Where do you live {user_name}?")
lives = input()

print("What kind of computer do you have?")
computer = input()

print(f"""
Alright, {user_name}, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
