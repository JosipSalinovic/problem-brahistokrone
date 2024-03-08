import matplotlib.pyplot as plt
from math import sin, cos,pi
import numpy as np

def fciklo(y,t):
     b=y[0]
     p=y[1]
     aciklo=(-(0.5*sin(p)*b*b)+((G/(2.0))*sin(p)))/(1.0-cos(p))
     vciklo=b

     return np.array([aciklo,vciklo])

# RK-4 metoda
def rk4(f,y,t):
    
 
     k1 = (f(y, t))
     k2 = (f((y+k1*h/2), (t+h/2)))
     k3 = (f((y+k2*h/2), (t+h/2)))
     k4 = (f((y+k3*h), (t+h)))
     k = ((k1+2*k2+2*k3+k4)/6)*h
     
     return k
G=9.81
X1ciklo=[]
X2ciklo=[]
X3ciklo=[]
Y1ciklo=[] 
Y2ciklo=[] 
Y3ciklo=[] 
y1=np.array([0.0,0.01])
y2=np.array([0.0,1.0])
y3=np.array([0.0,2.0])
h = (1.01)/500
time=np.arange(0.0, 1.01,h)

for t in time:
     y1 = y1 + rk4(fciklo,y1,t)
     y2 = y2 + rk4(fciklo,y2,t)
     y3 = y3 + rk4(fciklo,y3,t)
     
     X1ciklo.append(y1[1]-sin(y1[1]))
     X2ciklo.append(y2[1]-sin(y2[1]))
     X3ciklo.append(y3[1]-sin(y3[1]))
     Y1ciklo.append(1.0+cos(y1[1]))
     Y2ciklo.append(1.0+cos(y2[1]))
     Y3ciklo.append(1.0+cos(y3[1]))

     


 
#graf

fig=plt.figure(facecolor='white',figsize=(8,5))
plt.rcParams["font.size"]="16"
graf=fig.add_subplot(1,1,1)

#graf.plot(time,Y1ciklo,lw=2, label='1.tijelo')
#graf.plot(time,Y2ciklo,lw=2, label='2.tijelo')
#graf.plot(time,Y3ciklo,lw=2, label='3.tijelo')
#graf.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
graf.set_ylim(0,pi)
graf.set_xlim(0,1.01)
graf.set_xlabel('$t$ / s')
graf.set_ylabel('$y$ / m')

graf.legend(loc='upper left',shadow=True)

plt.show()    


