"""Checks if a queen can move from one square to another in one move."""

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
d1 = abs(x1 - x2)
d2 = abs(y1 - y2)
if x1 == x2 or y1 == y2 or d1 == d2:
    print("YES")
else:
    print("NO")
