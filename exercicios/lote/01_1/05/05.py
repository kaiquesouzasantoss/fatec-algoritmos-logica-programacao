a, b, c = float(input()), float(input()), float(input())

delta = ((b * b) - 4 * a * c)
x_1 = ((- b + delta * 0.5) / (2 * a))
x_2 = ((- b - delta * 0.5) / (2 * a))

print(f'X1 = {x_1} | X2 = {x_2}')