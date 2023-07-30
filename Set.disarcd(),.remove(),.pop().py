def set_methods(elements, N):
    '''Perform different set methods'''
    for i in range(N):
        method = input().split()
        if method[0] == 'pop':
            elements.pop()
        elif method[0] == 'remove':
            elements.remove(int(method[1]))
        elif method[0] == 'discard':
            elements.discard(int(method[1]))
        else:
            print('Invalid Option!')
    return sum(elements)
    

if __name__ == '__main__':
    n = int(input())
    elements = set(map(int, input().split()))
    N = int(input())
    
    result = set_methods(elements, N)
    print(result)
