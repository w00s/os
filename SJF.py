n = int(input("Enter number of processes\n"))
arrival     = [0] * (n)
burst       = [0] * (n)
turnaround  = [0] * (n)
waiting     = [0] * (n)
service     = [0] * (n)
iscomplete  = [False] * (n)

for i in range(n):
    print()
    arrival[i] = int(input(f"Arrival P{i} : "))
    burst[i] = int(input(f"Burst P{i}   : "))

completed = 0 
time = 0
disp = 0

while completed!=n:
    minburst = 10000
    minid = -1
    for i in range(n):
        if arrival[i]<time and iscomplete[i]==False:
            if burst[i]<minburst:
                minburst=burst[i]
                minid=i

            elif burst[i]==minburst and arrival[i]<arrival[minid]:
                minburst=arrival[i]
                minid=i

    if (minid!=-1):
        service[minid] = time+disp
        waiting[minid] = service[minid] - arrival[minid]
        turnaround[minid] = waiting[minid] + burst[minid]
        iscomplete[minid] = True
        completed+=1
        time = service[minid]+burst[minid]
    else:
        time+=1

for i in range(n):
    waiting[i]-=1
    turnaround[i]-=1
    
print("{:^15}{:^15}{:^15}{:^15}{:^15}".format("PROCESS", "ARRIVAL", "BURST", "TURNAROUND", "WAITING"))
for i in range(n):
    print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(i, arrival[i], burst[i], turnaround[i], waiting[i]))

print("\nAverage wait time       : ", sum(waiting)/len(waiting))
print("Average turnaround time : ", sum(turnaround)/len(turnaround))