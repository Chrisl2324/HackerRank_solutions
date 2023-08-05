def birthdayCakeCandles(candles):
    total = 0
    maximum = max(candles)
    for candle in candles:
        if candle == maximum:
            total += 1
    return total 


if __name__ == '__main__':
    candles = list(map(int, input().split()))
    result = birthdayCakeCandles(candles)
    print(result)