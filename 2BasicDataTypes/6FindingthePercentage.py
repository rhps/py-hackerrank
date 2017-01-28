if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()


point = student_marks[query_name]
total = 0
count = 0

for i in xrange(0,len(point)):
	total = total + point[i]
	count = count+1

ave = total/count
print("%0.2f"%ave)