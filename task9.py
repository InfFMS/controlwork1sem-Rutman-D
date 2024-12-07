def AB(n):

    arr = []

    for i in range(1, int(n**0.5) + 1):

        if n % i == 0:
            arr.append(i)

            if i != int(n**0.5):
                arr.append(n//i)

    return arr

print(len(AB(2097152)))
