def bothSubscriptions(englishRollNumbers, frenchRollNumbers):
    subscribedToBoth = englishRollNumbers.intersection(frenchRollNumbers)
    return len(subscribedToBoth)


if __name__ == '__main__':
    n = int(input())
    englishRollNumbers = set(map(int, input().split()))
    b = int(input())
    frenchRollNumbers = set(map(int, input().split()))
    
    result = bothSubscriptions(englishRollNumbers, frenchRollNumbers)
    print(result)