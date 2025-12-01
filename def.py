def root(a):
    return a * a

a = int(input("number"))

print(root(a))

for i in range(1, a + 1):
    print(f"root of{i:1} = {root(i):1}")