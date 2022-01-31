def merge_the_tools(string, k):
    # your code goes here
    arr = set()
    for idx, word in enumerate(string):
        if idx == len(string) - 1:
            arr.add(word)
            print(''.join(arr))
            continue
        
        if idx % k == 0 and idx != 0:
            print(''.join(arr))
            arr = set()
        arr.add(word)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)