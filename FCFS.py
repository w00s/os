
n = int(input("Enter number of processes\n"))
arrival     = [0] * (n)
burst       = [0] * (n)
turnaround  = [0] * (n)
waiting     = [0] * (n)
completion  = [0] * (n)

for i in range(n):
    print()
    arrival[i] = int(input(f"Arrival P{i} : "))
    burst[i] = int(input(f"Burst P{i}   : "))

for i in range(1, n):
    waiting[i] = arrival[i-1] + burst[i-1] - arrival[i]
    if waiting[i] < 0:
        waiting[i] = 0

for i in range(n):
    turnaround[i] = burst[i] + waiting[i]
    completion[i] = turnaround[i] + arrival[i]


print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}".format("PROCESS", "ARRIVAL", "BURST", "TURNAROUND", "WAITING", "COMPLETION"))
for i in range(n):
    print("{:^15}{:^15}{:^15}{:^15}{:^15}{:^15}".format(i, arrival[i], burst[i], turnaround[i], waiting[i], completion[i]))

print("\nAverage wait time       : ", sum(waiting)/len(waiting))
print("Average turnaround time : ", sum(turnaround)/len(turnaround))

