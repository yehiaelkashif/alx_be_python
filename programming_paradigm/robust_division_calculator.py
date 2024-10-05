def safe_divide(numerator, denominator):
    """Perform division and handle errors like ZeroDivisionError and ValueError."""
    try:
        # Convert the inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division and handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.2f}"
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
