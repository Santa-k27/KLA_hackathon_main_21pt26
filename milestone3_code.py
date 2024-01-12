import math
countery=1
counterx=1
def isValidPt(a,b,r):
    distance = math.sqrt((a)**2 + (b)**2)
    return distance<r
with open('Solution Files\MileStone3_code\Testcase1.txt','r') as f:
    context=f.readlines()
data=[]
for i in range(len(context)):
    data.append(context[i].rstrip().split(":")[-1])
print(data)
radius=int(int(data[0])/2)
dieht,diewt=map(int,data[1].split('x'))
dieshiftvecx,dieshiftvecy=map(int,data[2][1:-1].split(','))
refx,refy=map(int,data[3][1:-1].split(','))
n_x,n_y=map(int,data[-1].split('x'))
ds_wt,ds_ht=map(int,data[4][1:-1].split(','))
rs_wt,rs_ht=map(int,data[5][1:-1].split(','))
x_st=dieshiftvecx
y_st=dieshiftvecy
x_lab=0
y_lab=0
dieLLC=[[[x_lab,y_lab],[x_st,y_st]]]
while x_st<=(radius):
    while y_st<(radius):
        x_lab,y_lab=x_lab,y_lab+1
        x_st,y_st=x_st,y_st+dieht+(countery*ds_ht)
        countery+=1
        if isValidPt(x_st,y_st,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
        if countery==n_y:
            y_st+=rs_ht
            countery=0
    y_st=dieshiftvecy
    y_lab=-refy
    while y_st>((-1)*radius):
        x_lab,y_lab=x_lab,y_lab-1
        x_st,y_st=x_st,y_st-dieht-(countery*ds_ht)
        countery+=1
        if isValidPt(x_st,y_st+dieht,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
        if countery==n_y:
            y_st+=rs_ht
            countery=0
    x_st=x_st+diewt+(counterx*ds_wt)
    counterx+=1
    if counterx==n_x:
        x_st+=rs_wt
        counterx=0
    x_lab=x_lab+1
x_st=dieshiftvecx
x_lab=-refx
while x_st>=((-1)*radius):
    while y_st<(radius):
        x_lab,y_lab=x_lab,y_lab+1
        x_st,y_st=x_st,y_st+dieht+(countery*ds_ht)
        countery+=1
        if isValidPt(x_st,y_st,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
        if countery==n_y:
            y_st+=rs_ht
            countery=0
    y_st=dieshiftvecy
    y_lab=-refy
    while y_st>((-1)*radius):
        x_lab,y_lab=x_lab,y_lab-1
        x_st,y_st=x_st,y_st-dieht-(countery*ds_ht)
        countery+=1
        if isValidPt(x_st,y_st+dieht,radius):
            if [[x_lab,y_lab],[x_st,y_st]] not in dieLLC:
                dieLLC.append([[x_lab,y_lab],[x_st,y_st]])
        if countery==n_y:
            y_st+=rs_ht
            countery=0
    x_st=x_st-diewt-(counterx*ds_wt)
    counterx+=1
    if counterx==n_x:
        x_st+=rs_wt
        counterx=0
    x_lab=x_lab-1

with open('Solution Files\MileStone3_code\ms3output1.txt','w') as wr:
    for i in dieLLC:
        wr.write("("+str(i[0][0])+","+str(i[0][1])+"):("+str(i[1][0])+","+str(i[1][1])+")\n")
