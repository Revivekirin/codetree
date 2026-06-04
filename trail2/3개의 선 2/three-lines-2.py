from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

answer=0
for vx in range(4):
    vy=3-vx
    for xs in combinations(x, vx):
        for ys in combinations(y, vy):
            possible=True
            for xp, yp in points:
                if xp not in xs and yp not in ys:
                    possible=False
                    break
            
            if possible:
                answer=1

print(answer)

# Please write your code here.