import textwrap

def wrap(string, max_width):
    arr = []
    count = 0
    for idx in string:
        arr.append(idx)
        count += 1
        if count % max_width == 0:
            arr.append('\n')
    return ''.join(arr)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)