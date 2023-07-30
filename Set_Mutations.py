
    

def set_mutations(set_a, n):
    '''Perform different mutations on a given set'''
    isValid = False
    while not isValid:
        try:
            for i in range(n):
                operation, length = input().split()
                elements = set(map(int, input().split()))
                if operation == 'intersection_update':
                    set_a.intersection_update(elements)
                elif operation == 'update':
                    set_a.update(elements)
                elif operation == 'symmetric_difference_update':
                    set_a.symmetric_difference_update(elements)
                elif operation == 'difference_update':
                    set_a.difference_update(elements)
                else:
                    print('Invalid Choice!')
            isValid = True
        except ValueError:
            print('Invalid Input! Try Again!')
        except Exception as e:
            print('Error', str(e))

    return sum(set_a)


if __name__ == '__main__':
    try:
        length_a = int(input())
        set_a = set(map(int, input().split()))
        n = int(input())
    except Exception as e:
        print('Error', str(e))
    
    result = set_mutations(set_a, n)
    print(result)
