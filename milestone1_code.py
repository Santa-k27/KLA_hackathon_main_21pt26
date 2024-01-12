
def cos(x):
    return round(math.cos(math.radians(x)),5)
def sin(x):
    return round(math.sin(math.radians(x)),5)
def tan(x):
    return round(math.tan(math.radians(x)),5)
import math
import numpy as np
import matplotlib.pyplot as plt
with open('Solution Files\MileStone1_code\milestone4_input.txt','r') as f:
    context=f.readlines()
data=[]
for i in range(len(context)):
    data.append(int(context[i].rstrip().split(":")[-1]))    
radius=int(data[0]/2)
point1=(radius*cos(data[-1]),radius*sin(data[-1]))
point2=((-1)*radius*cos(data[-1]),(-1)*radius*sin(data[-1]))
result=[]
x=np.linspace(min(point1[0], point2[0]), max(point1[0], point2[0]),data[1])
print(x)
for i in range(data[1]):
    y=round(tan(data[-1])*x[i],5)
    result.append([round(x[i],5),y])

for i in result:
    plt.scatter(i[0],i[1], marker='o')
plt.grid(True)
plt.show()

with open('Solution Files\MileStone1_code\milestone4_output.txt','w') as wr:
    for i in result:
        wr.write("("+str(i[0])+","+str(i[1])+")\n")
