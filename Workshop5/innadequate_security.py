usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

valid = False
user_input = input("Enter Username: ")
while not valid:
    if user_input in usernames:
        valid = True
    else:
        valid = False
        print('Your Username is a lie')
        user_input = input("Enter Username: ")
print("Your Username is Valid")
