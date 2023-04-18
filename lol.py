dx=x2-x1
dy=y2-y1
if abs(dx)>abs(dy):
 steps=abs(dx)
else:
 steps=abs(dy)
    
if steps==0:
    print("Both points are same")
    xcoordinates=[]
    ycoordinates=[]
    xcoordinates.append(x1)
    ycoordinates.append(y1)
    xcoordinates.append(x2)
    ycoordinates.append(y2)
    
else:
    xincrement=dx/steps
    yincrement=dy/steps
    i=0;
    xcoordinates=[]
    ycoordinates=[]
    while i<steps:
        i=i+1
        x1=x1+xincrement
        y1=y1+yincrement
        xcoordinates.append(x1)
        ycoordinates.append(y1)
plt.plot(xcoordinates,ycoordinates,markerfacecolor='green',markersize=1,marker='o')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("DDA Algorithm")
plt.show()   
