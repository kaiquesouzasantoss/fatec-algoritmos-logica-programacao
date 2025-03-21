num = int(input())

j, sum = 1, 0

if num > 0:
    while (j <= num):
        sum += (1/j)
        print(f'1/{j} = {1/j} | SUM = {sum}')
        j+=1

    print(f'SUM = {sum}')