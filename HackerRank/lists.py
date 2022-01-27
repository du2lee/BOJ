if __name__ == '__main__':
    N = int(input())
    array = []
    
    for _ in range(N):
        arr = input().split()
        if arr[0] == 'insert':
            array.insert(int(arr[1]), int(arr[2]))
        elif arr[0] == 'print':
            print(array)    
        elif arr[0] == 'remove':
            array.remove(int(arr[1]))
        elif arr[0] == 'sort':
            array.sort()
        elif arr[0] == 'pop':
            array.pop()
        elif arr[0] == 'reverse':
            array.reverse()
        elif arr[0] == 'append':
            array.append(int(arr[1]))
