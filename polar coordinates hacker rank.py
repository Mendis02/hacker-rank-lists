import cmath

s = input()
l = list(s)
x = int(l[0])
y = int(l[2])


print(abs(complex(x, y)))
print(cmath.phase(complex(x, y)))