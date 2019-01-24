numslist = [11,12,12,12,12,12,1,2,2,2,3,1,1,15,23,25,16,24,32,32,32,1,1,1,1,1,1,11,11,15]
numslist.sort()
newlist=[]
newlist.append(numslist[0])
for i in range (0,len(numslist)-1):
    if numslist[i] == numslist[i+1]:
        pass
    else:
        newlist.append(numslist[i+1])
print(newlist)