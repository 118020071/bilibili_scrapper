newL = []
nNewL = []

with open("userAgent.txt", "r") as f:
    i = 0
    while True:
        try:
            i += 1
            a = f.readline()
            if len(a) == 0:
                break
            a = a.replace("\n", "")
            newL.append(a)
            print(i,end='\r')
        except:
            break

for i in newL:
    if ("(" in i) and (")" in i) and ("/" in i):
        print(i)
        nNewL.append(i)

w = open("newUA.txt", "w")

for i in nNewL:
    print(i, file=w)