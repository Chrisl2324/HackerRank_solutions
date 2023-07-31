n, x = list(map(int, input().split()))

total_score = []
for i in range(x):
    scores = list(map(float, input().split()))
    total_score.append(scores)
    
student_scores = zip(*total_score)
for scores in student_scores:
    average = sum(scores)/len(scores)
    print(f'{average:.1f}')
