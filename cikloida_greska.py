import matplotlib.pyplot as plt
import math
import numpy as np
# funkcija zdesna diferencijalne jednadžbe cikloide
def f(x,y):
    return -math.sqrt((-y)/(2.0-(-y)))
#parametarske jed.cikloide
def xt(th):
  return th - math.sin(th)

def yt(th):
  return math.cos(th)-1.0

# RK-4 metoda
def rk4(x0,y0,yn,n):
    
    
 h = (yn-y0)/n
    
    
 for i in range(n):
     k1 = (f(x0, y0))
     k2 = (f((x0+k1*h/2), (y0+h/2)))
     k3 = (f((x0+k2*h/2), (y0+h/2)))
     k4 = (f((x0+k3*h), (y0+h)))
     k = ((k1+2*k2+2*k3+k4)/6)*h
     xn = x0 + k
     y0 = y0+h
     x0 = xn
    
     x_p=xn
     y_p=y0    
    
     ax =math.fabs(xn-(math.acos(1.0+y_p)-math.sqrt(y_p*(-2.0-y_p))))
     
     X.append(xn)
     Y.append(-y0)
     G.append(ax)

 return Y,X,G
# Početni uvjeti
x0 = xt(0.1)
y0 = yt(0.1)
yn = -1.9999
G=[]
xn=math.pi
X=[]
Y=[]

#br_koraka=500
for br_koraka in range(100,501,100):
  rk4(x0,y0,yn,br_koraka)

#graf

fig=plt.figure(facecolor='white',figsize=(8,5))
plt.rcParams["font.size"]="16"
graf=fig.add_subplot(1,1,1)
#graf.plot(X,Y,lw=2, label='N=500')
graf.plot(Y[0:100],G[0:100],lw=2, label='N=100')
graf.plot(Y[100:300],G[100:300],lw=2, label='N=200')
graf.plot(Y[300:600],G[300:600],lw=2, label='N=300')
graf.plot(Y[600:1000],G[600:1000],lw=2, label='N=400')
graf.plot(Y[1000:1500],G[1000:1500],lw=2, label='N=500')

#graf.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
graf.set_ylim(5E-09,1E-04)
graf.set_xlim(0,1.9)
#graf.set_xlabel('$x$ / m')
#graf.set_ylabel('$y$ / m')
graf.set_xlabel('$y$ / m')
graf.set_ylabel('$greška$ $od$ $x$ / m')
graf.legend(loc='upper right',shadow=True)
#ax=plt.gca()
#ax.invert_yaxis()

plt.yscale("log")
plt.show()    


