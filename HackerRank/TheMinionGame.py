def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    for idx, word in enumerate(string):
        if word in 'aeiouAEIOU':
            Kevin += (len(string) - idx)
        else:
            Stuart += (len(string) - idx)

    if Stuart > Kevin:
        print('Stuart', Stuart)
    elif Stuart < Kevin:
        print('Kevin', Kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)