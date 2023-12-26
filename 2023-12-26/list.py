# a=[1,2,[3,4,5]]
# print(a[0]+a[1])

# a[0]=6
# print(a[0])

# a.append(8)
# print(a)
# print(a.index(2))
# a.remove(6)
# print(a)
# a.insert(3,9)
# print(a)
# a.reverse()
# print(a)
# b=a.copy()
# print(b)
# b[0]=155
# print(b)
# c=a[:2]
# print(c)
# c[0]=199
# print(c)
# print(a)
# del a[2]
# print(a)
# print(len(a))

p=[1,2,3,4,5]

for t in range(4):
    p.pop()
    print(p)

a=[1,2,3,4,5,6,7,8,9,10]

# for w in range(5):
#     a.pop(w)
#     print(a)

for w in range(5):
    del(a[w])
    print(a)