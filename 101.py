n = int(input())
def count_num(n):
    while (n != 1 ):
        if n%2 == 1:
            n = 3*n + 1
        else:
            n = int(n/2)
        print(n)

