def uniqueSubscriptions(englishRollNumbers, frenchRollNumbers):
    uniqueRollNumbers = englishRollNumbers.union(frenchRollNumbers)
    return len(uniqueRollNumbers)


if __name__ == '__main__':
    n = int(input())
    englishRollNumbers = set(map(int, input().split()))
    b = int(input())
    frenchRollNumbers = set(map(int, input().split()))
    
    result = uniqueSubscriptions(englishRollNumbers, frenchRollNumbers)
    print(result)
