import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
coordinates = list(map(int, data[1:]))

sorted_coordinates = sorted(set(coordinates)) 
rank = {value: index for index, value in enumerate(sorted_coordinates)}  

result = [rank[x] for x in coordinates]
print(" ".join(map(str, result)))
