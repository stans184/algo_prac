import this

a = [1, 2, 3, 34, 45, 56, 7]

print(a)

print(list(enumerate(a)))

print(divmod(345, 32))

print(type(this))

is_duple = True

print(is_duple)

for i in range(10, 12):
    a = i
    b = a
    print(id(i), id(a), id(b))
