dic01=dict(떡볶이='순대',라면='김밥')
dic01['연필']='지우개'
dic01['떡볶이']='어묵'

print(len(dic01))

for i in dic01:
    print(i,end=' ')

for i in dic01.values():
    print(i,end=' ')

del(dic01['연필'])

print("\n")
print(dic01)