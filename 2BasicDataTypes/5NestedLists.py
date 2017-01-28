l = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    l.append([name, score])

l.sort()

grades = set([line[1] for line in l])
grades.remove(min(grades))

mini = min(grades)

for i in xrange(len(l)):
	if l[i][1] == mini:
		print l[i][0]