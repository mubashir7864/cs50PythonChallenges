list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

newlist =[]

i,j=0,0

while i < len(list1) and j<len(list2):
    if list1[i] < list2[j]:
        newlist.append(list1[i])
        i+=1
    else:
        newlist.append(list2[j])
        j+=1

print(newlist)
