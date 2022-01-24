import sys

if __name__ == "__main__":
    max_num = 1000000
    flags = [False, False] + [True] * (max_num - 1)
    for i in range(2, max_num + 1):
        if flags[i] == True:
            for j in range(2 * i, max_num + 1 , i):
                flags[j] = False

    while True:
        N = int(sys.stdin.readline())
        if N == 0: break
        
        flag = 0
        for i in range(3, len(flags)):
            if flags[i] and flags[N - i]:
                print(str(N) + " = " +  str(i) +  " + " + str(N - i))
                flag = 1
                break
        if flag == 0:
            print("Goldbach's conjecture is wrong.")
