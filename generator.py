
def gen_demo():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

test = gen_demo()

print(test)

print(next(test))
print(next(test))
print(next(test))
# print(next(test))

test2 = gen_demo()

for a in test2:
    print(a)



