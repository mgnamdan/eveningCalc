# Helper functions
def add(numOne, numTwo):
    return numOne + numTwo


def subtract(numOne, numTwo):
    return numOne - numTwo


def multiply(numOne, numTwo):
    return numOne * numTwo


def divide(numOne, numTwo):
    try:
        return numOne / numTwo
    except ZeroDivisionError:
        return "Cannot divide by zero!"




# Main definition
def main():
    calcOn = True
    cont = False
    result = 0

    operations = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}

    while calcOn:
        print("Let's do some math! Enter an equation:")
        math = input("   -> ")

        mathChunks = math.split(" ")
        
        if not cont:
            result = float(mathChunks[0])
        else:
            pass

        for i in range(len(mathChunks)):
            if mathChunks[i] in operations.keys():
                numTwo = float(mathChunks[i+1])
                result = operations[mathChunks[i]](result, numTwo)
                if result == "Cannot divide by zero!":
                    break
            else:
                continue

        print(f"Your result is: {result}")
        print("")
        print("Would you like to do more math? (y/n)")
        moreMath = input(" --> ").lower()

        if moreMath == "y" or moreMath == "yes":
            print("Would you like to use the last result? (y/n)")
            keepGoing = input("  --> ").lower()
            if keepGoing == "y" or keepGoing == "yes":
                cont = True
            else:
                cont = False
        else:
            calcOn = False




# Main call
if __name__ == "__main__":
    main()
