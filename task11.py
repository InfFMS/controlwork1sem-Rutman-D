a = 174457
b = 174505
k = 0
for i in range(a,b + 1):
    ds = []
    for j in range(2, i//2 + 1):
        if i % j == 0:
            ds.append(j)
            if len(ds) > 2:
                break
    if len(ds) == 2:
        print(ds[0], ds[1])