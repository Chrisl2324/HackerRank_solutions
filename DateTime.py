from datetime import datetime, timezone

def convertUTC(timestamp):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    date = datetime.strptime(timestamp, date_format)
    utc = date.astimezone(timezone.utc)
    return utc

def time_delta(timestamp1, timestamp2):
    utc1 = convertUTC(timestamp1)
    utc2 = convertUTC(timestamp2)
    
    difference = abs((utc1 - utc2).total_seconds())
    return int(difference)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)  