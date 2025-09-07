"""Basic color mixer: outputs the result of combining two primary colors."""

color_1 = input()
color_2 = input()
a = "red"
b = "blue"
c = "yellow"
if color_1 + color_2 == a + a:
    print("red")
elif color_1 + color_2 == b + b:
    print("blue")
elif color_1 + color_2 == c + c:
    print("yellow")
elif (color_1 + color_2 == a + b) or (color_1 + color_2 == b + a):
    print("purple")
elif (color_1 + color_2 == a + c) or (color_1 + color_2 == c + a):
    print("orange")
elif (color_1 + color_2 == b + c) or (color_1 + color_2 == c + b):
    print("green")
else:
    print("error")
