numberList=[]
divisorsList=[]

num=int(input("insert number: "))

cnt=0
cnt2=1
while True:
    for k in divisorsList:
        if(cnt%k != 0):
            numberList.append(cnt)
        cnt +=1

    divisorsList.append(cnt2+1)
    
    if(len(numberList)==num):
        break
print(numberList)