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
    equations.append(equation)
    equations.append(result)

# Print the list with alternating equation and result
for i in range(0, len(equations), 2):
    equation = equations[i]
    result = equations[i + 1]
    print (equations)