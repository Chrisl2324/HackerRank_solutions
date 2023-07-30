def total_happiness(a, b):
    total_happiness = 0
    for element in arr_elements:
        if element in a:
            total_happiness += 1
        elif element in b:
            total_happiness -= 1
    return total_happiness

if __name__ == '__main__':
    n, m = map(int,input().split())
    arr_elements = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    
    print(total_happiness(a, b))
    