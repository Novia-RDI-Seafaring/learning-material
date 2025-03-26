import numpy as np

def drawShip(ax, angle=0):
    angle = angle*np.pi/180
    verts= np.array([[-0.1, -0.1, 0, 0.1, 0.1, -0.1],[-0.1, 0.1, 0.2, 0.1, -0.1, -0.1]])

    rot = np.array([[np.cos(angle), -np.sin(angle)],
                            [np.sin(angle), np.cos(angle)]])

    verts = rot@verts
    
    ax.plot(verts[0], verts[1], linestyle='-', color='k')
    
def drawVec2(x,label,ax):
    ax.arrow(0, 0, x[0], x[1], head_width=0.1, head_length=0.1, fc='blue', ec='blue')
    ax.text(x[0], x[1], label, verticalalignment='bottom', horizontalalignment='right', fontsize=12)

def drawVec3(vector,label,ax):
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b', pivot='tail', arrow_length_ratio=0.1)
    #ax.text(x[0], x[1], x[2], label, verticalalignment='bottom', horizontalalignment='right', fontsize=12)