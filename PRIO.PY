n = int(input("Enter number of processes\n"))
arrival     = [0] * (n)
burst       = [0] * (n)
turnaround  = [0] * (n)
waiting     = [0] * (n)
iscomplete  = [False] * (n)
priority    = [0]*(n)

for i in range(n):
    print()
    arrival[i] = int(input(f"Arrival P{i}  : "))
    burst[i] = int(input(f"Burst P{i}    : "))
    priority[i] = int(input(f"Priority P{i} : "))

completed = 0 
time = 0
disp = 0

while completed!=n:
    maxprio = 10000
    maxid = -1
    for i in range(n):
        if arrival[i]<time and iscomplete[i]==False:
            if priority[i]<maxprio:
                maxprio=priority[i]
                maxid=i

            elif priority[i]==maxid and arrival[i]<arrival[maxid]:
                maxprio=priority[i]
                maxid=i
    if maxid!=-1:
        time = time + disp + burst[maxid]
        turnaround[maxid] = time-arrival[maxid]
        waiting[maxid] = turnaround[maxid]-burst[maxid]
        iscomplete[maxid]=True
        completed+=1
    else:
        time+=1
    


for i in range(n):
    waiting[i]-=1
    turnaround[i]-=1
    
print("{:^15}{:^15}{:^15}{:^15}{:^15}".format("PROCESS", "ARRIVAL", "BURST", "PRIORITY", "TURNAROUND", "WAITING"))
for i in range(n):
    print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(i, arrival[i], burst[i], priority[i], turnaround[i], waiting[i]))

print("\nAverage wait time       : ", sum(waiting)/len(waiting))
print("Average turnaround time : ", sum(turnaround)/len(turnaround))