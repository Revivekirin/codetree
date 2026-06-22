n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# bad[i][j] = 양수가 아니면 1, 양수면 0
bad = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] <= 0:
            bad[i][j] = 1

# prefix sum
# prefix[i][j] = (0,0)부터 (i-1,j-1)까지 bad의 합
prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = (
            prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
            + bad[i - 1][j - 1]
        )

def get_sum(r1, c1, r2, c2):
    # (r1, c1)부터 (r2, c2)까지의 bad 합
    return (
        prefix[r2 + 1][c2 + 1]
        - prefix[r1][c2 + 1]
        - prefix[r2 + 1][c1]
        + prefix[r1][c1]
    )

answer = -1

# 모든 직사각형 탐색
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                bad_count = get_sum(r1, c1, r2, c2)

                # bad_count가 0이면 전부 양수
                if bad_count == 0:
                    area = (r2 - r1 + 1) * (c2 - c1 + 1)
                    answer = max(answer, area)

print(answer)