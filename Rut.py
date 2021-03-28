num = int(input())
hcows = []
vcows = []
cows = []
for n in range(num):
    cow = input().split(" ")
    cow.append(None)
    cow.append(None)
    if cow[0] == "N":
        cow[3]=cow[1]
        vcows.append(cow)
    if cow[0] == "E":
        cow[4]=cow[2]
        hcows.append(cow)
    cows.append(cow)
answers = [None]*num
index1 = 0
index2 = 0

for cow in cows:
    if cow[0] == "N":
        diff = []
        for cow2 in hcows:
            if int(cow[1]) < int(cow2[1]):
                continue
            if int(cow[2]) > int(cow2[2]):
                continue
            if(cow2[3]!=None):
                if(int(cow2[3])<int(cow[1])):
                    continue
            if int(cow2[2])-int(cow[2])>int(cow[1])-int(cow2[1]):
                diff.append(int(cow2[2])-int(cow[2]))
            if int(cow2[2])-int(cow[2])<int(cow[1])-int(cow2[1]):
                if cow2[3]!=None:
                    if int(cow2[3])>int(cow[1]):
                        cow2[3]=cow[1]
                else:
                    cow2[3] = cow[1]
        if(diff==[]):
            print("Infinity")
        else:
            print(min(diff))
            cow[4]=int(cow[2])+min(diff)
    if cow[0] == "E":
        diff = []
        for cow2 in vcows:
            if int(cow[1]) > int(cow2[1]):
                continue
            if int(cow[2]) < int(cow2[2]):
                continue
            if (cow2[4]!=None):
                if (int(cow2[4]) < int(cow[2])):
                    continue
            if int(cow2[1]) - int(cow[1]) > int(cow[2]) - int(cow2[2]):
                diff.append(int(cow2[1]) - int(cow[1]))
            if int(cow2[1]) - int(cow[1]) < int(cow[2]) - int(cow2[2]):
                if cow2[4]!=None:
                    if int(cow2[4])>int(cow[2]):
                        cow2[4]=int(cow[2])
                else:
                    cow2[4] = int(cow[2])
        if (diff == []):
            print("Infinity"
        else:
            print(min(diff))
            cow[3]=int(cow[1])+min(diff)