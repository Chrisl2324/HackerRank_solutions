def plusMinus(arr):
    results = []
    length = len(arr)
    negatives = 0
    positives = 0
    zero = 0
    for item in arr:
        if item < 0:
            negatives += 1
        elif item > 0:
            positives += 1
        else:
            zero += 1
    print(f'{positives/length:.6f}')
    print(f'{negatives/length:.6f}')
    print(f'{zero/length:.6f}')
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plusMinus(arr)
        