def count_substring(string, sub_string):
    count = 0
    for idx in range(len(string) - len(sub_string) + 1):
        if sub_string == string[idx:idx+len(sub_string)]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)