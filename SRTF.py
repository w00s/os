n = int(input("Enter number of processes\n"))
arrival     = [0] * (n + 1)
burst       = [0] * (n + 1)
turnaround  = [0] * (n + 1)
waiting     = [0] * (n + 1)
completion  = [0] * (n + 1)
p           = [0] * (n + 1)

for i in range(n):
	arrival[i] = int(input(f"ARRIVAL P{i+1} : "))
	burst[i]   = int(input(f"BURST P{i+1}   : ")) 
	p[i] = [burst[i], arrival[i], i]
	

p.pop()
temp = []

for i in range(sum(burst)):
	l = [j for j in p  if j[1] <= i]
	l.sort(key=lambda x: x[0])
	p[p.index(l[0])][0] -= 1
	for k in p:
		if k[0] == 0:
			t = p.pop(p.index(k))
			temp.append([k, i + 1])

for i in temp:
	completion[i[0][2]] = i[1]

for i in range(len(completion)):
	turnaround[i] = completion[i] - arrival[i]
	waiting[i] = turnaround[i] - burst[i]



arrival.pop()
burst.pop()
turnaround.pop()
waiting.pop()
completion.pop()




print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}". format("PROCESS", "ARRIVAL", "BURST", "COMPLETION", "WAITING", "TURNAROUND"))
for i in range(len(completion)):
	print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}". format(i+1, arrival[i], burst[i], completion[i], waiting[i], turnaround[i]))

print('Average Waiting Time = ', sum(waiting)/len(waiting))
print('Average Turnaround Time = ', sum(turnaround)/len(turnaround))