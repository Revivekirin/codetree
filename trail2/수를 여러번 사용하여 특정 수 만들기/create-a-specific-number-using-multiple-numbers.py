A, B, C = map(int, input().split())

ans=0

for i in range(C//A+1):
    for j in range(C//B+1):
        total = A*i+B*j
        if total>ans and total<=C:
            ans=total

print(ans)
    

# Please write your code here.