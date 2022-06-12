import sys

N = int(sys.stdin.readline())
word_array = []


for _ in range(N):
    word_input = input()
    value = (word_input, len(word_input))
    word_array.append(value)

word_array  = list(set(word_array))
word_array.sort(key=lambda x : (x[1], x[0]))

for word in word_array:
    print(word[0])