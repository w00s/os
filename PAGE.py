size  = int(input("enter size\n"))
reference = [int(x) for x in input("Enter a space seperated reference string\n").split()]
#7 0 1 2 0 3 0 4 2 3 0 3 1 2 0



testframe = ['']*size
faults, pos = 0,0

for i in range(len(reference)):
    if reference[i] not in testframe:
        testframe[pos] = reference[i]
        pos = (pos+1)%size
        print(*testframe)
        faults+=1
        continue
    print(*testframe, "hit")

print(f"\nHits : {len(reference)-faults}\nFaults : {faults}")