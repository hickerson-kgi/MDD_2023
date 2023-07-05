import random
def generate_equation():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    equation = f"{num1} {operator} {num2}"
    return equation

# Example usage:
equation = generate_equation()
print("Generated equation:", equation)
result = eval(equation)
print("Result:", result)