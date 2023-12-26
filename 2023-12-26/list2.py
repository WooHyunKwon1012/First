list1=["KG","KAIROS","로봇","아카데미"] # 출력 예: ['KAIROS','로봇'] 를 만드시오
list2=list1[1:3]

print(list2)

print(list1[1:3])

list4=[]
list4.append(list1[1]) #리스트 맨뒤에 항목을 추가한다
list4.append(list1[2]) 
print(list4)

list5=[]
list5.extend([list1[1],list1[2]]) #리스트 뒤에 리스트를 추가한다. 리스트의 더하기 연산과 기능이 동일하다.
print(list5)

del(list1[0],list1[2])
print(list1)


