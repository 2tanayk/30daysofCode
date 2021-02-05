arr = []
sums = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sums = [[sum(arr[i][j:(j + 3)]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:(j + 3)]) for j in range(4)] for i in range(4)]
print(max(map(max, sums)))
