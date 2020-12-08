import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve,newton_krylov,excitingmixing, least_squares
# class Reactor:
#     def __init__(self,*args):
#         print(*args)
class Bomba:
    def __init__(self,*args):
        print(*args)

    def grafica_bomba(self):
        x=np.linspace(0,200,100)
        plt.plot(x,-5E-3*x**2 + 1.66E-1*x + 1.5E2)
        plt.show()


def f(z):
    m=1.84429
    T3, T4, Q= z
    f1= (m*(T4-T3)/50)-Q
    f2=m**0.8*((np.log(73/48)*(T4-T3-10))/(50*np.log((T4-45)/(T3-35))))-Q
    f3=((5*np.log(16/11)*(T4-T3))/(50*((2/m)**0.8+4)*np.log((510-T3)/(510-T4))))-Q
    return [f1,f2,f3]
p=(300,350,1.15)

x=fsolve(f,p)

print(x)