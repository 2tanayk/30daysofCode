n = int(input())

d = {}

i = 0

while (i < n):
    g = list(input().split())
    d[g[0]] = g[1]
    i += 1

try:
    while (True):
        inp = input()

        if (inp in d):
            print(f"{inp}={d[inp]}")
        else:
            print("Not found")

except EOFError:
    pass
