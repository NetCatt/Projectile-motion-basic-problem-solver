
from math import sin, cos, tan, radians
from sympy import*
from numpy import*
x,y,z=symbols('x,y,z')
from matplotlib.pyplot import*
import matplotlib.animation as animation
g=9.8

def Max_Height(u,theta):
    Hmax=(u*sin(radians(theta)))**2/(2*g)
    return Hmax
    return f"Maximum Height of the Projectile is {Hmax} meters"

def Horizontal_range(u,theta):
    R=(u**2*sin(radians(2*theta))/g)
    return R

def Equation_of_path(u,theta):
    func=(x*tan(radians(theta)))-((g*x**2)/(2*u**2*cos(radians(theta))**2))   
    X_co= Horizontal_range(u,theta)
    X=linspace(0,X_co,200)
    
    def anim():

        x_p = linspace(0,X_co,1000)
        y_p = (x_p*tan(radians(theta)))-((g*x_p**2)/(2*u**2*cos(radians(theta))**2))  

        fig, ax = subplots()
        ax.set_xlim([0,X_co+5])
        ax.set_ylim([0,Max_Height(u,theta)+5])
        line, = ax.plot(   [],[], lw=2,  color='teal')
        sctr  = ax.scatter([],[], s=100, color='orange')

        def update(i):
            line.set_ydata(y_p[:i+1])  # update
            line.set_xdata(x_p[:i+1])
            sctr.set_offsets((x_p[i],y_p[i]))
            return line,sctr
        ani = animation.FuncAnimation(fig, update, 1000, interval=5, blit=True)
        grid()
        show()
    
    anim()
    
    return f"Equation of path of projectile motion is {func}\n{Max_Height(u,theta)} and its range is\n{X_co} meters"
print(Equation_of_path(35,70))