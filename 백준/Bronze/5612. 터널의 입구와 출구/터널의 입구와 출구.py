n=int(input())
m=int(input())

current_car=m
max_car=m

for _ in range(n):
    in_car, out_car=map(int, input().split())
    current_car+=in_car
    current_car-=out_car

    if current_car < 0:
        print(0)
        exit()

    else:        
        if current_car >= max_car:
            max_car=current_car

print(max_car)