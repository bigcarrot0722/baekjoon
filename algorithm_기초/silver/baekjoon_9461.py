import sys

for _ in range(int(sys.stdin.readline())):
    triangle = [1, 1, 1, 2, 2]
    index_triangle = int(sys.stdin.readline())
    for i in range(5, index_triangle):
        triangle.append(triangle[i-1]+triangle[i-5])      
    print(triangle[index_triangle-1])
