import math,sys

n,p=map(int,sys.stdin.readline().split())
limit = int(p ** (1/n))+1

def div_cnt(n,p):
    cnt = 0
    while p % n == 0:
        cnt += 1
        p /= n
    return p, cnt

if limit==1:
    print(1)
elif n==1:
    print(p)
else:
    cnt,ans=0,1

    p, cnt = div_cnt(2,p)
    ans *= 2 ** (cnt // n)
    
    for div in range(3, limit, 2):
        p,cnt = div_cnt(div,p)
        if cnt >= n:
            ans *= div ** (cnt // n)
    print(ans)