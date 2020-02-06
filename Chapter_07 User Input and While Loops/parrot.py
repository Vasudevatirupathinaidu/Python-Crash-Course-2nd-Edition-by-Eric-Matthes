# flag - For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True # here active variable is a flag

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else: 
        print(message)