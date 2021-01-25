import sys
sys.setrecursionlimit(10000000) #재귀 한도를 늘려준다. RecursionError 방지
 
def dp(x):
    if x == 1:
        m[x] = 0
        return m[x]
 
    if m[x] > 0:
        return m[x]
 
    m[x] = dp(x-1)+1 # 빼기 1 연산, 메모이제이션 + 초기화 기능
 
    if x % 3 == 0: # 나누기 3 연산, 메모이제이션
        div3 = dp(x//3)+1
        m[x] = min(m[x], div3)
 
    if x % 2 == 0: # 나누기 2 연산. 메모이제이션
        div2 = dp(x//2)+1
        m[x] = min(m[x], div2)

    if x % 5 == 0:
        m[x] = min(m[x], dp(x//5)+1)
 
    return m[x]
 
x = int(input())
m = [0]*(10**6+1)
answer = dp(x)
print(answer)
