def print_rangoli(n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(n-1, -n, -1):
        string = '-'.join(alpha[n-1:abs(i):-1] + alpha[abs(i):n])
        print(string.center(4 * n - 3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    