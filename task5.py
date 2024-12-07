n = 125**5 + 25**9 - 30
s = ""
while n != 0:
    s += str(n % 5)
    n //= 5
s = s[::-1]
print(s.count("4"))