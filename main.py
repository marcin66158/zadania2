zdanie = input()
print(zdanie.count('a'))

###################

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print("Najwieksza jest %i" % (a))
elif b >= a and b >= c:
    print("Najwieksza jest %i" % (b))
elif c >= a and c >= b:
    print("Najwieksza jest %i" % (c))

#####################

liczby = [2, 3, 4, 5, 1.5, 2.5, 3.5, 4.5]

for x in range(len(liczby)):
    liczby[x] = liczby[x] ** 2

print(liczby)

########################

i = 0
parzyste = []
while i < 10:
    wstaw = int(input())

    if wstaw % 2 == 0:
        parzyste.append(wstaw)

    i += 1

print(parzyste)