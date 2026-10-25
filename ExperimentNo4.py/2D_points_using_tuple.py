import math

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def farthest(points):
    return max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))

points = []
n = int(input("Enter number of points: "))

for i in range(n):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    points.append((x, y))

p1 = tuple(map(int, input("Enter first point (x y): ").split()))
p2 = tuple(map(int, input("Enter second point (x y): ").split()))

print("Distance:", distance(p1, p2))
print("Farthest point:", farthest(points))