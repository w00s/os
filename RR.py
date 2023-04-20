n = int(input("Enter number of processes\n"))
quantum = int(input("Enter time quantum\n"))
arrival     = [0] * 100
burst       = [0] * 100
turnaround  = [0] * 100
waiting     = [0] * 100
remaining   = [0] * 100

queue       = [0] * 100
front, rear = 0,0

def pushh(id):
    global queue
    global rear

    queue[rear] = id
    rear = (rear+1)%100

def popp():
    global queue
    global front
    global rear

    if front==rear:
        return -1
    return_position = queue[front]
    front = (front+1)%100
    return return_position

for i in range(n):
    print()
    arrival[i] = int(input(f"Arrival P{i} : "))
    burst[i] = int(input(f"Burst P{i}   : "))
    remaining[i] = burst[i]

time = 0
proc_left = n
position = -1
local_time = 0

for i in range(n):
    if arrival[i] == time:
        pushh(i)

while proc_left:
    if local_time==0:
        if position!=-1:
            pushh(position)
        position=popp()
    
    for i in range(n):
        if arrival[i]> time:
            continue
        if i==position:
            continue
        if remaining[i]==0:
            continue
        waiting[i]+=1
        turnaround[i]+=1

    if position!=-1:
        remaining[position]-=1
        turnaround[position]+=1
        if remaining[position] == 0:
            proc_left-=1
            local_time =-1
            position =-1
    else:
        local_time = -1
    
    time +=1
    local_time = (local_time+1)%quantum
    for i in range(n):
        if arrival[i] ==time:
            pushh(i)

print("{:^15}{:^15}{:^15}{:^15}{:^15}".format("PROCESS", "ARRIVAL", "BURST", "TURNAROUND", "WAITING"))
for i in range(n):
    print("{:^15}{:^15}{:^15}{:^15}{:^15}".format(i, arrival[i], burst[i], turnaround[i], waiting[i]))

print("\nAverage wait time       : ", sum(waiting)/n)
print("Average turnaround time : ", sum(turnaround)/n)
