# Enter your code here. Read input from STDIN. Print output to STDOUT
r = input().strip().split()
r = list(map(int, r))
d = input().strip().split()
d = list(map(int, d))

fine = 0

if r[-1] - d[-1] > 0:
    fine = 10000
elif r[-2] - d[-2] > 0 and r[-1] - d[-1] == 0:
    fine = 500 * (r[-2] - d[-2])
elif r[-3] - d[-3] > 0 and r[-1] - d[-1] == 0 and r[-2] - d[-2] == 0:
    fine = 15 * (r[-3] - d[-3])
else:
    pass

print(fine)
