A = input()
n=len(A)

def len_run_length(text):
    length=0
    count=1

    for i in range(1, n):
        if text[i]==text[i-1]:
            count+=1
        else:
            count=1
            length+=1+len(str(count))
    length+=1+len(str(count))
    
    return length

answer=10**9
for k in range(n):
    if k==0:
        shifted=A
    else:
        shifted=A[-k:]+A[:-k]
    answer=min(answer, len_run_length(shifted))

print(answer)
# Please write your code here.
