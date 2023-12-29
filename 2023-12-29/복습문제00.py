word=["Python","Apple","Robot"]
R_Cnt=0
W_Cnt=0

for S in word:
    ans=input("{}\n주어진 단어를 입력하시오 : ".format(S))
    if ans==S:
        R_Cnt=R_Cnt+1
        continue
    else:
        W_Cnt=W_Cnt+1
        continue
    
print("정답: {}개, 오답: {}개".format(R_Cnt,W_Cnt))

a,b,c,d=map(int,input().split()) #옆으로 하나씩 받는건데 뭔가 중요하다고 하는데 모르게쑴

