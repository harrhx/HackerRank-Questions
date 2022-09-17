num=int(input(''))
data=[]
for i in range(0,num):
    student_name=str(input(''))
    marks=input('')
    li1=[student_name, marks]
    data.append(li1)
for i in range(num-1):
    for j in range(num-i-1):
        if data[j][1]>data[j+1][1]:
            data[j],data[j+1]=data[j+1], data[j]
        elif (data[j][1]==data[j+1][1] and data[j][0]>data[j+1][0]):
              data[j],data[j+1] =data[j+1], data[j]
        print(data)
li=[]
for i in range(num):
    li.append(data[i][1])
li=set(li)
li=list(li)
li.sort()
for i in range(num):
    if data[i][1]==li[1]:
        print(data[i][0])




    
