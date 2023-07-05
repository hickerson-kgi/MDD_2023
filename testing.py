import random
def generate_equation():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    equation = f"{num1} {operator} {num2}"
    result = eval(equation)
    return equation, result
equations = []
for _ in range(4):
    equation, result = generate_equation()
    equations.append((equation, result))
# Print the list of equations and their results
for equation, result in equations:
    print({equation}, {result})
