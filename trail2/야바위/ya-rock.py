n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

max_cnt=0
ans=0
for i in range(1, 4):
    cnt=0
    ans=i
    for turn in moves:
        if ans in (turn[0], turn[1]):
            if turn[0]==ans:
                ans=turn[1]
            else:
                ans=turn[0]
        if turn[2]==ans:
            
            cnt+=1
    if cnt>max_cnt:
        max_cnt=cnt

print(max_cnt)





# Please write your code here.