num1 =int (input("Enter the first number:"))
num2= int (input("Enter the second number: "))
operation =input("Choose the operation (+, -, *, /): ")

match operation :

    case "+":
        add= num1 +num2
        print(add)
    case "-":
        sub= num1-num2
        print(sub)
    
    case "*":
        mult=num1 * num2
        print(mult)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            div=num1/num2
            print(div)
