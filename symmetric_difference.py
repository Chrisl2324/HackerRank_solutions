def unique_elements(set1, set2):
    '''Returns unique elements from both sets in ascending order'''
    difference1 = set1.difference(set2)
    difference2 = set2.difference(set1)
    differences = difference1.union(difference2)
    differences = list(differences)
    for element in sorted(differences):
        print(element)
        
if __name__ == '__main__':
    m = int(input())
    data1 = list(map(int, input().split()))
    set1 = set(data1)
    n = int(input())
    data2 = list(map(int, input().split()))
    set2 = set(data2)
    
    unique_elements(set1, set2)

    



