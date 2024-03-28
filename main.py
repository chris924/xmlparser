

from input import askForInput
from xmlparse import parse

def main():
    global user_inputs
    user_inputs, fileName = askForInput()  
    parse(user_inputs, fileName)

main()