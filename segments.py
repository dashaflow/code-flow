a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
L = max(a1, a2)
R = min(b1, b2)
if L < R:
    print(L, R)
elif L == R:
    print(L)
else:
    print("empty set")