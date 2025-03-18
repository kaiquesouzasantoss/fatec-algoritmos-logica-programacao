num_a, num_b = int(input()), int(input())

if ((num_a >= num_b) and (num_a % num_b == 0)):
    print(f'A ({num_a}) É MAIOR E MULTIPLO DE B!')
elif ((num_b >= num_a) and (num_b % num_a == 0)):
    print(f'B ({num_b}) É MAIOR E MULTIPLO DE A!')