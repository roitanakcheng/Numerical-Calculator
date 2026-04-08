import re

print("The 67 Calculator")
print("Type 'quit' to exit the calculator (please kindly use LOWERCASE)\n")

previous = 0
run = True

def doMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Thanks for trying out my calculator, Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.()+" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    doMath()


