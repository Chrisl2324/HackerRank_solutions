n, x = list(map(int, input().split()))

total_score = []
for i in range(x):
    scores = list(map(int, input().split()))
    total_score.append(scores)
    
student_scores = zip(*total_score)
print(list(student_scores))
    