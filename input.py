
user_inputs = []

def askForInput():

    fileName = input("Type in the file name without .xls :")

    counter = 1

    while True:
        user_input = input(f"Specific tag name {counter}: ")
        if user_input == "":
            break
        else:
            user_inputs.append(user_input)
            counter = counter + 1
    
    return user_inputs, fileName