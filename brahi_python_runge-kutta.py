from turtle import title
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
from math import sin, cos,pi,sqrt,fabs
import numpy as np
plt.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg-2022-09-07-git-e4c1272711-full_build\bin\ffmpeg'
a= 0.202642367284
G=9.81
b= 0.020531964509



def kosina(y,t) :
     v=y[0]
     x=y[1]
     akc=(-G*(2.0/pi))/(1.0+(4.0/(pi*pi)))
     brz=v
     return np.array([akc,brz])

def parabola(y,t) :
     v=y[0]
     x=y[1]
     akc=(-0.5*(8.0*a*a*x)*v*v-(2.0*G*a*x))/(1+4.0*a*a*x*x)
     brz=v
     return np.array([akc,brz])

def polinom(y,t) :
     v=y[0]
     x=y[1]
     akc=(-((96.0*b*b*(x**5))*v*v)+0.5*(96.0*b*b*(x**5)*v*v)-4.0*b*G*(x**3))/(1.0+16.0*b*b*(x**6))
     brz=v
     return np.array([akc,brz])


def cikloida(y,t) :
     v=y[0]
     x=y[1]
     akc=((0.5*sin(x)*v*v)+(-(G/(2.0))*sin(x)))/(1.0+cos(x))
     brz=v
     return np.array([akc,brz])



# RK-4 metoda
def rk4(f,y,t):
    
 
     k1 = (f(y, t))
     k2 = (f((y+k1*h/2), (t+h/2)))
     k3 = (f((y+k2*h/2), (t+h/2)))
     k4 = (f((y+k3*h), (t+h)))
     k = ((k1+2*k2+2*k3+k4)/6)*h
     
     return k

v_x1=[]
v_y1=[]
v_x2=[]
v_y2=[]
v_x3=[]
v_y3=[]
v_x4=[]
v_y4=[]
v_1=[]
v_2=[]
v_3=[]
v_4=[]
y_1=[]
y_2=[]
y_3=[]
y_4=[]
x_1=[]
x_2=[]
x_3=[]
x_4=[]
y1=np.array([0.0,0.6])
y2=np.array([0.0,1.0])
y3=np.array([0.0,2.0])
y4=np.array([0.0,3.13])
h = (1.25)/700
time=np.arange(0.0, 2.0,h)

for t in time:
    
     y1 = y1 + rk4(kosina,y1,t)
     y2 = y2 + rk4(parabola,y2,t)
     y3 = y3 + rk4(polinom,y3,t)
     y4 = y4 + rk4(cikloida,y4,t)
     """ 
     y1 = y1 + rk4(cikloida,y1,t)
     y2 = y2 + rk4(cikloida,y2,t)
     y3 = y3 + rk4(cikloida,y3,t)
     y4 = y4 + rk4(cikloida,y4,t)

     x_1.append(y1[1]+sin(y1[1]))
     y_1.append((1.0-cos(y1[1])))
     x_2.append(y2[1]+sin(y2[1]))
     y_2.append((1.0-cos(y2[1])))
     x_3.append(y3[1]+sin(y3[1]))
     y_3.append((1.0-cos(y3[1])))
     y_4.append((1.0-cos(y4[1])))
     x_4.append(y4[1]+sin(y4[1]))
     """




     v_x1.append(fabs(y1[0]))
     v_y1.append(fabs((2.00/pi)*y1[0]))
     v_1.append(sqrt((y1[0])**2+((2.00/pi)*y1[0])**2))
     y_1.append((2.00/pi)*y1[1])
     x_1.append(y1[1])
     v_x2.append(fabs(y2[0]))
     v_y2.append(fabs(2*a*y2[1]*y2[0]))
     v_2.append(sqrt((y2[0])**2+(2*a*y2[1]*y2[0])**2))
     y_2.append(a*y2[1]*y2[1])
     x_2.append(y2[1])
     v_x3.append(fabs(y3[0]))
     v_y3.append(fabs(4*b*y3[1]*y3[1]*y3[1]*y3[0]))
     v_3.append(sqrt((y3[0])**2+(4*b*y3[1]*y3[1]*y3[1]*y3[0])**2))
     y_3.append(b*(y3[1])**4)
     x_3.append(y3[1])
     v_x4.append(fabs((y4[0]+cos(y4[1])*y4[0])))
     v_y4.append(fabs((sin(y4[1])*y4[0])))
     v_4.append(sqrt((y4[0]+cos(y4[1])*y4[0])**2+(sin(y4[1])*y4[0])**2))
     y_4.append((1.0-cos(y4[1])))
     x_4.append(y4[1]+sin(y4[1]))
     
     
     


 
#graf anima
"""
fig=plt.figure(facecolor='white',figsize=(8,5))
plt.rcParams["font.size"]="16"
graf=fig.add_subplot(1,1,1)

graf.plot(x_1,v_1,lw=2, label='kosina')
graf.plot(x_2,v_2,lw=2, label='parabola')
graf.plot(x_3,v_3,lw=2, label='polinom-4.red')
graf.plot(x_4,v_4,lw=2, label='cikloida')
#graf.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
graf.set_ylim(0,7)
graf.set_xlim(0,3.15)
graf.set_xlabel('$x$ / m')
graf.set_ylabel('$v$ / m/s')

graf.legend(loc='lower left',shadow=True)

plt.show()    

#subplot

fig, axs = plt.subplots(3, 2, sharex='col', sharey='row',gridspec_kw={'hspace': 0, 'wspace': 0},facecolor='white',figsize=(3.15*2,2.2*3),dpi=100)
(ax1, ax2), (ax3, ax4), (ax5,ax6) = axs
#fig.suptitle("Problem Brahistokrone-Josip Šalinović")
i=7
#


for ax in axs.flat:
    
    ax.plot(x_3,y_3,lw=1, label='polinom 4.reda')
    ax.plot(x_2,y_2,lw=1, label='parabola')
    ax.plot(x_1,y_1,lw=1, label='kosina')
    
    ax.plot(x_4,y_4,lw=1, label='cikloida')

    ax1.legend(loc='upper left',shadow=True,fontsize=9)
    ax.plot([x_4[i]],[y_4[i]],'o',color='red')
    
    ax.plot([x_3[i]],[y_3[i]],'o',color='blue')

    ax.plot([x_2[i]],[y_2[i]],'o',color='orange')

    ax.plot([x_1[i]],[y_1[i]],'o',color='green')
    
    ax.set_ylim(-0.1,2.1)
    ax.set_xlim(0,3.15)
    ax.set_aspect('equal')
    i=i+110
    ax.label_outer()
fig.supxlabel('$x$ / m')
fig.supylabel('$y$ / m')

plt.show()"""
fig=plt.figure(facecolor='white',dpi=300)
graf=fig.add_subplot(1,1,1)
plt.title("Problem Brahistokrone-Josip Šalinović")
#plt.title("Problem Tautokrone-Josip Šalinović")

graf.set_xlabel('$x$ / m')
graf.set_ylabel('$y$ / m')
graf.plot(x_3,y_3,lw=1, label='polinom 4.reda')
graf.plot(x_2,y_2,lw=1, label='parabola')
graf.plot(x_1,y_1,lw=1, label='kosina')
graf.plot(x_4,y_4,lw=1, label='cikloida')
graf.set_ylim(-0.1,2.1)
graf.set_xlim(0,3.15)     
plt.gca().set_aspect('equal', adjustable='box')
ln1,  = graf.plot([],[],'o',color='green')
ln2,  = graf.plot([],[],'o',color='orange')
ln3,  = graf.plot([],[],'o',color='blue')
ln4,  = graf.plot([],[],'o',color='red')
graf.legend(loc='upper left',shadow=True)

 
def init():
    ln1.set_data([],[])
    ln2.set_data([],[])
    ln3.set_data([],[])
    ln4.set_data([],[])
    
def animate(i):
     
     ln4.set_data([x_4[i]],[y_4[i]])
     ln3.set_data([x_3[i]],[y_3[i]])
     ln2.set_data([x_2[i]],[y_2[i]])
     ln1.set_data([x_1[i]],[y_1[i]])
     


ani=animation.FuncAnimation(fig,animate,init_func=init,frames=700)
FFwriter=animation.FFMpegWriter(fps=60, extra_args=['-vcodec', 'libx264'])
ani.save('tautokrona_za_py.mp4',writer=FFwriter)
