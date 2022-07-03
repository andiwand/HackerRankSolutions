returned = [int(s) for s in input().split()]
due = [int(s) for s in input().split()]

if returned[2] > due[2]:
    print(10000)
elif returned[2] == due[2] and returned[1] > due[1]:
    print(500 * (returned[1] - due[1]))
elif returned[2] == due[2] and returned[1] == due[1] and returned[0] > due[0]:
    print(15 * (returned[0] - due[0]))
else:
    print(0)
