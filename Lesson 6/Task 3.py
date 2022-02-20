mylist = []
i = 1
while i <= 100:
    mylist.append(i)
    i += 1
print(mylist)
mylist2 = []
for number in mylist:
    if (mylist[number] % 7) == 0:
        print(number)
        mylist2.append(number)
print(mylist2)
#:
