people = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
n, m = 10, 10

def choose(num,x,y,tsum):
    if [x,y] not in memor and x <= 9 and x >= 0 and y <= 9 and y >= 0 and num[x][y] == 1:
        memor.append([x,y])
        tsum = choose(num,x + 1,y,tsum)
        tsum = choose(num,x,y + 1,tsum)
        tsum = choose(num,x + 1 ,y + 1,tsum)
        tsum = choose(num,x - 1,y,tsum)
        tsum = choose(num,x,y - 1,tsum)
        tsum = choose(num,x - 1 ,y - 1,tsum)
        tsum = choose(num,x + 1 ,y - 1,tsum)
        tsum = choose(num,x - 1 ,y + 1,tsum)
        if tsum > 0:
            return tsum + 1
        else : return 1
    return tsum

total = list()
memor = list()
for i in range(n):
    for j in range(m):
        tsum = 0
        value = choose(people, i, j, tsum)
        if value > 0:
            total.append(value)

print(len(total))
print(max(total))