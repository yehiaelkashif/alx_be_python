

def perform_operation( num1, num2, operation):
    match operation :
 
     case "add":
        add= num1 +num2
        return  add
     case "subtract":
        sub= num1-num2
        return sub
    
     case "multiply":
        mult=num1 * num2
        return mult
     case "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            div=num1/num2
            return div
        
        