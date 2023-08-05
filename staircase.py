def staircase(n):
    j = 1
    space = n - 1
    for i in range(n):
        print(' '*space + '#'*j, end='')
        print()
        j += 1
        space -= 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)