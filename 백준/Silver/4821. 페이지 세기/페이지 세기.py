import sys
input = sys.stdin.readline

while True:
    total = int(input())
    if total == 0:
        break
    
    ranges = input()    
    
    print_page = set()
    page_range = ranges.split(',')
    
    for i in page_range:
        if '-' in i:
            low, high = map(int, i.split('-'))
            if low<=high:
                for page in range(max(1, low), min(total, high) + 1):
                    print_page.add(page)
        else:   #단일페이지
            page = int(i)
            if 1 <= page <= total:
                print_page.add(page)
                
    print(len(print_page))