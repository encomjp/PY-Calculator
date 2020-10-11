
#GUI from tkinter Lib
import tkinter as tk
window = tk.Tk()

greeting = tk.Label(text="Hello, user!")
greeting.pack()


welcome = "Welcome to basic PY Calculator"
#Declaration of Variables and setting them to None
firstNumber = None
operator = None
secondNumber = None
result = None

#Introduction
def intro():
    return print(welcome)


#Input Class with Throw Exception for debugging purposes
def inp(b):
    try: 
        a = input(b)
        return a
    except:
        raise Exception("Error in inp has accured")

#Check operator and call the math function
def math(a, b, c):
    c = float(c)
    a = float(a)
    if b == "+":
        res = a + c
    elif b == "-":
        res = a - c
    elif b == "/":
        res = a / c
    elif b == "*":
        res = a * c
    else:
        raise Exception("Wrong operator")
    return res
    

#Semi-Main Class
def menu():
        intro()
        firstNumber = inp("Input your first Number: ")
        operator = inp("input your operator: ")
        secondNumber = inp("Input your second Number Number: ")
        result = math(firstNumber, operator, secondNumber)
        print("Result is: ", result)


menu()

    