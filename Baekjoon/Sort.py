import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

print(sum(arr)//len(arr))
def median(arr):
    arr.sort()
    return arr[len(arr)//2]
print(median(arr))

def mode(arr):

    mode = Counter(arr).most_common()

    if len(arr) > 1:
        if mode[0][1] == mode[1][1]:
            return mode[1][0]
        else:
            return mode[0][0]
    else:
        return mode[0][0]


print(mode(arr))
print(max(arr)-min(arr))