def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = sum(1 for d in apples if s <= a+d <= t)
    total_oranges = sum(1 for d in oranges if s <= b+d <=t)
    print(total_apples)
    print(total_oranges)

    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)