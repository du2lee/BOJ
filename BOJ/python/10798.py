arr = []
max = 0

for _ in range(5):
    str = input()
    arr.append(str)
    if max < len(str):
        max = len(str)

for i in range(max):
    for j in range(5):
        try:{
            print(arr[j][i], end= "")
        }
        except:{}
print("")