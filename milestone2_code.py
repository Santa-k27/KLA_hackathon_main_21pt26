import math


def isValidPt(a,b,r):
    distance = math.sqrt((a)**2 + (b)**2)
    return distance<r
with open('Solution Files\MileStone2_code\Testcase3.txt','r') as f:
    context=f.readlines()
data=[]
for i in range(len(context)):
    data.append(context[i].rstrip().split(":")[-1])
radius=int(int(data[0])/2)
dieht,diewt=map(int,data[1].split('x'))
dieshiftvecx,dieshiftvecy=map(int,data[2][1:-1].split(','))
refx,refy=map(int,data[3][1:-1].split(','))
x_st=dieshiftvecx
y_st=dieshiftvecy
x_lab=0
y_lab=1
dieLLC=[[[x_lab,y_lab],[x_st,y_st]]]
while x_st<=(radius):
    while y_st<(radius):
        x_lab,y_lab=x_lab,y_lab+1
        x_st,y_st=x_st,y_st+dieht
        if isValidPt(x_st,y_st,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
    y_st=dieshiftvecy
    y_lab=1
    while y_st>((-1)*radius):
        x_lab,y_lab=x_lab,y_lab-1
        x_st,y_st=x_st,y_st-dieht
        if isValidPt(x_st,y_st+dieht,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
    x_st=x_st+diewt
    x_lab=x_lab+1
x_st=dieshiftvecx
x_lab=0
while x_st>=((-1)*radius-diewt):
    while y_st<(radius):
        x_lab,y_lab=x_lab,y_lab+1
        x_st,y_st=x_st,y_st+dieht
        if isValidPt(x_st+diewt,y_st,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
    y_st=dieshiftvecy
    y_lab=1
    while y_st>((-1)*radius):
        x_lab,y_lab=x_lab,y_lab-1
        x_st,y_st=x_st,y_st-dieht
        if isValidPt(x_st+diewt,y_st+dieht,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
    x_st=x_st-diewt
    x_lab=x_lab-1

with open('Solution Files\MileStone2_code\output3.txt','w') as wr:
    for i in dieLLC:
        wr.write("("+str(i[0][0])+","+str(i[0][1])+"):("+str(i[1][0])+","+str(i[1][1])+")\n")