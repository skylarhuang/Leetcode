S = 'aaba'
C = 'b'

## NEW METHOD
lo = -10001
result = []
tmp = []

for n,s in enumerate(S):
    if s == C:
        while len(tmp):
            for _, t in enumerate(tmp):
                result.append(min(abs(lo-t),abs(n-t)))
            tmp = []
        lo = n
        result.append(0)
    else:
        tmp.append(n)
        if n == len(S)-1:
            for _, t in enumerate(tmp):
                result.append(abs(lo-t))}
print(result)


## OLD METHOD
ind = []
for n, s in enumerate(S):
    if s == C:
        ind.append(n)

dis = []
l = [i for i in range(len(S))]

for ind_ in ind:
    dis_ = []
    dis_[:] = [abs(x - ind_) for x in l]
    dis.append(dis_)

result = []
for i in range(len(S)):
    min_ = len(S)
    for l in range(len(dis)):
        if dis[l][i] < min_:
            min_ = dis[l][i]
    result.append(min_)

print (result)