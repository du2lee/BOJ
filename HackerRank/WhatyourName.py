def print_full_name(first, last):
    # Write your code here
    print('Hello', first, last, end='')
    print('! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)