
user_inputs = []

def askForInput():

    fileName = input("Type in the file name without .xls:")

    user_inputs.append(fileName)

    user_input = input("Name by you want to search (the tree(s) that contains childrens):")
    user_inputs.append(user_input)


    while True:
        user_input = input("Specific tag name:")
        if user_input == "":
            break
        else:
            user_inputs.append(user_input)
    
    return user_inputs