def print_formatted(number):
    # your code goes here
    l1 = len(bin(number)[2:])
    for idx in range(number):
        print(str(idx + 1).rjust(l1), oct(idx + 1)[2:].rjust(l1), hex(idx + 1)[2:].upper().rjust(l1), bin(idx + 1)[2:].rjust(l1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)