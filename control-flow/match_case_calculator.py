num1 =int (input("Enter the first number:"))
num2= int (input("Enter the second number: "))
operation =input("Choose the operation (+, -, *, /): ")

match operation :

    case "+":
        add= num1 +num2
        print(f"The result is {add}")
    case "-":
        sub= num1-num2
        print(f"The result is {sub}")
    
    case "*":
        mult=num1 * num2
        print(f"The result is {mult}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            div=num1/num2
            print(f"The result is {div}")
