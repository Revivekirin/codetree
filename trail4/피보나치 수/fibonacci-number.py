N = int(input())
N_MAX=100
memo=[-1]*N_MAX
def fibbo(n):
    if memo[n] !=-1:
        return memo[n]
    if n<=2:
        memo[n]=1
    else:
        memo[n]=fibbo(n-1)+fibbo(n-2)

    return memo[n]    

print(fibbo(N))
# Please write your code here.
