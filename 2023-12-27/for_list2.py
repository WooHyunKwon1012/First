marks=[50,39,79,80,43]
num=0
# for mark in marks:
#     num=num+1
#     if mark>= 60:
#         print("%d번 학생 축하합니다 합격입니다"%num)
#     else:
#         continue

for mark in marks:
    num=num+1
    if mark< 60:
        continue
    print("%d번 학생 축하합니다 합격입니다"%num)

