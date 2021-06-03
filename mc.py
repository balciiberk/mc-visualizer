import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os


def init():
    global inside, outside, a, b, c, pi_list
    a=[-0.5,0.5]
    b=[-0.5,-0.5]
    c=[0.5,0.5]
    ax.plot(a,b,'-r',a,c, '-r',b,a, '-r',c,a, '-r',linewidth=1)
    ax.add_patch(plt.Circle((0,0),0.5,color='g',fill=False))
    inside=[]
    outside=[]
    pi_list = []
def repeat_f(i):
    if i % 2 == 0:
        x,y = np.random.rand(2)-.5
        if np.sqrt(x**2+y**2)<.5:
            inside.append([x,y])
        else:
            outside.append([x,y])
        ax.scatter(x,y,c='b')
        pi_current = 4*len(inside)/(len(inside)+len(outside))
        pi_list.append(pi_current)
        print(f'Pi = {pi_current:.4f}')
    else:
        ax.clear()
        ax.plot(a,b,'-r',a,c, '-r',b,a, '-r',c,a, '-r',linewidth=1)
        ax.add_patch(plt.Circle((0,0),0.5,color='g',fill=False))
        if inside != []:
            ax.scatter(*zip(*inside),c='g')
        if outside != []:
            ax.scatter(*zip(*outside),c='r')
def graph(pi_list):
    plt.plot(range(len(pi_list)), pi_list,'-b',label='Calculated pi')
    plt.plot([0,len(pi_list)],[np.pi,np.pi],'--r', label='Known pi')
    plt.xlabel('iterations')
    plt.ylabel('Value of pi')
    plt.legend()
    plt.show()
if __name__=="__main__":
    speed = 1 # Low numbers for generating faster, high numbers for generating slower
    points_to_generate = 1000
    fig, ax =plt.subplots(figsize=(8, 8), dpi=80)
    ani = FuncAnimation(fig, repeat_f, init_func=init, frames=2*points_to_generate,repeat=False, interval=speed)
    plt.show()
    graph(pi_list)
