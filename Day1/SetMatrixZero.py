x, y = map(int, input().split())
a = []

for i in range(x):
    l = list(map(int, input().split()))
    a.append(l)
rows = set()
cols = set()

for i in range(x):
    for j in range(y):
        if a[i][j] == 0:
            rows.add(i)
            cols.add(j)

for i in rows:
    for j in range(y):
        a[i][j] = 0
for j in cols:
    for i in range(x):
        a[i][j] = 0
        
for i in range(x):
    for j in range(y):
        print(a[i][j], end=' ')
    print()