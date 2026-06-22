n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[False]*n
answer=-10**18

def backtrack(row, current_min):
    global answer
    if row==n:
        answer=max(answer, current_min)
        return 
    
    for col in range(n):
        if not visited[col]:
            visited[col]=True
            new_min=min(current_min, grid[row][col])
            backtrack(row+1, new_min)
            visited[col]=False
   
backtrack(0, 10**18)
print(answer)
# Please write your code here.
