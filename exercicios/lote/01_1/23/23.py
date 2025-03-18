num_a, num_b, num_c, num_d = int(input()), int(input()), int(input()), int(input())

if num_d <= num_a:
    print(num_d, num_a, num_b, num_c)
elif num_d <= num_b:
    print(num_a, num_d, num_b, num_c)
elif num_d <= num_c:
    print(num_a, num_b, num_d, num_c)
else:
    print(num_a, num_b, num_c, num_d)