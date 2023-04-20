n = int(input("Enter number of processes\n"))
arrival     = [0] * (n)
burst       = [0] * (n)
turnaround  = [0] * (n)
waiting     = [0] * (n)
iscomplete  = [False] * (n)
remaining   = [0]*(n)
priority    = [0]*(n)

for i in range(n):
    print()
    arrival[i] = int(input(f"Arrival P{i}  : "))
    burst[i] = int(input(f"Burst P{i}    : "))
    priority[i] = int(input(f"Priority P{i} : "))
    remaining[i]=burst[i]

completed = 0 
time = 0
disp = 0
prev_id = -1

while completed!=n:
    maxprio = 10000
    maxid = -1
    for i in range(n):
        if arrival[i]<=time and iscomplete[i]==False:
            if priority[i]<maxprio:
                maxprio=priority[i]
                maxid=i

            elif priority[i]==maxid and arrival[i]<arrival[maxid]:
                maxprio=priority[i]
                maxid=i
    if maxid!=-1:
        if maxid!=prev_id:
            time = time + disp
        
        remaining[maxid]-=1
        time+=1
        if remaining[maxid]==0:
            turnaround[maxid] = time-arrival[maxid]
            waiting[maxid] = turnaround[maxid]-burst[maxid]
            iscomplete[maxid]=True
            completed+=1
        prev_id=maxid
    else:
        time+=1
    

    
print("{:^15}{:^15}{:^15}{:^15}{:^15}".format("PROCESS", "ARRIVAL", "BURST", "PRIORITY","TURNAROUND", "WAITING"))
for i in range(n):
    print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(i, arrival[i], burst[i], priority[i], turnaround[i], waiting[i]))

print("\nAverage wait time       : ", sum(waiting)/len(waiting))
print("Average turnaround time : ", sum(turnaround)/len(turnaround))