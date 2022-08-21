import numpy as np

"""FCFS"""
wsum = 0
num = int(input("작업개수를 입력하세요."))

print("도착 순서에 따라서 작업명과 도착시간,CPU 사이클을 입력하세요.")
TABLE = []
for i in range(num):
    TABLE.append(input().split())

FCFS = []

FCFS.append([TABLE[0][0], TABLE[0][1], TABLE[0][2]])

csum = 0
for i in range(num - 1):
    csum += int(TABLE[i][2])

    wsum = int(csum - int(TABLE[i + 1][1]))
    rsum = wsum + int(TABLE[i + 1][2])
    FCFS.append([TABLE[i + 1][0], wsum, rsum])
avrw = 0
avrr = 0
for i in range(num):
    avrw += float(FCFS[i][1])
    avrr += float(FCFS[i][2])
avrw = avrw / 3
avrr = avrr / 3
print(FCFS)
print("==============================================================\n")
print("작업번호\tCPU cycle\t대기시간\t반환시간\n");
for i in range(num):
    print("%s\t\t%d\t\t%d\t\t%d\n" % (FCFS[i][0], int(TABLE[i][2]), int(FCFS[i][1]), int(FCFS[i][2])))
print("평균 대기시간 %.2f 평균 반환시간%.2f" % (avrw, avrr))

"""SJF(Shortest Job First) 단기 작업 우선"""

num = int(input("작업개수를 입력하세요."))

print("도착 순서에 따라서 작업명과 도착시간,CPU 사이클을 입력하세요.")
TABLE = []
for i in range(num):
    TABLE.append(input().split())

TABLE = sorted(TABLE, key=lambda TABLE: int(TABLE[2]))

SJF = []

SJF.append([TABLE[0][0], TABLE[0][1], TABLE[0][2]])

csum = 0
for i in range(num - 1):
    csum += int(TABLE[i][2])

    wsum = int(csum - int(TABLE[i + 1][1]))
    rsum = wsum + int(TABLE[i + 1][2])
    SJF.append([TABLE[i + 1][0], wsum, rsum])
avrw = 0
avrr = 0
for i in range(num):
    avrw += float(SJF[i][1])
    avrr += float(SJF[i][2])
avrw = avrw / 3
avrr = avrr / 3
print(SJF)
print("==============================================================\n")
print("작업번호\tCPU cycle\t대기시간\t반환시간\n");
for i in range(num):
    print("%s\t\t%d\t\t%d\t\t%d\n" % (SJF[i][0], int(TABLE[i][2]), int(SJF[i][1]), int(SJF[i][2])))
print("평균 대기시간 %.2f 평균 반환시간%.2f" % (avrw, avrr))

"""RoundRobin"""

num = int(input("작업개수를 입력하세요."))

print("도착 순서에 따라서 작업명과 도착시간,CPU 사이클을 입력하세요.")
TABLE = []
RR = []
RR_save=[]
RR_wait=[]
for i in range(num):
    csum += int(TABLE[i][2])

    wsum = int(csum - int(TABLE[i + 1][1]))
    rsum = wsum + int(TABLE[i + 1][2])
    RR.append([TABLE[i + 1][0], wsum, rsum])
time, exchange = [int(x) for x in input().split()]
cnt = 0
i = 0
j = 0
while (1):
    if (cnt < 4):
        if (int(TABLE[i][2]) - time > 0):
            RR_save[i] = int(TABLE[i][2]) - time

            if (cnt == 0):
                RR_wait[i] = 0
            else:
                RR_wait[i] = RR_wait[i - 1] + 4
        else:
            RR_save[i] = 0
            RR_wait[i] = RR_wait[i - 1] + 4
    else:
        if (int(RR_save[i]) - time > 0):
            RR_save[i] = int(RR_save[i]) - time
            for (j=i-1; RR_wait[j] > RR_wait[i]; j--):
                RR_wait[i] = RR_wait[j] + 4

        else:
            if (RR_save[i] != 0):
                RR_save[i] = 0
                RR_wait[i] = RR_wait[i - 1] + 4
                i += 1
    i += 1
    cnt += 1

    if (i == num):
        i = 0

    orRR_save = RR_save.sort(reverse=True)
    if (orRR_save[0] < 4):
        break
print(RR_save)
print(RR_wait)

