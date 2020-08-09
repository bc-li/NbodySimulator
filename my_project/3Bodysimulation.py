# Import scipy
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
G = 6.67408e-11
m_nd = 1.989e+30  
r_nd = 5.326e+12 
v_nd = 30000  
t_nd = 79.91 * 365 * 24 * 3600 * 0.51  
K1 = G * t_nd * m_nd / (r_nd ** 2 * v_nd)
K2 = v_nd * t_nd / r_nd
m1 = float(input('Please input the m1: '))
m2 = float(input('Please input the m2: ')) 
m3 = float(input('Please input the m3: '))
r1_input = input('r1')
r2_input = input('r2')
r3_input = input('r3')
r1 = r1_input.split(" ", 2)
r2 = r2_input.split(" ", 2)
r3 = r3_input.split(" ", 2)
r1 = sci.array(r1, dtype="float64")
r2 = sci.array(r2, dtype="float64")
r3 = sci.array(r3, dtype="float64")
r_com = (m1*r1+m2*r2+m3*r3)/(m1+m2+m3)
v1 = [0.01, 0.01, 0] 
v2 = [-0.05, 0, -0.1]  
v3 = [0, -0.01, 0]
v1 = sci.array(v1, dtype="float64")
v2 = sci.array(v2, dtype="float64")
v3 = sci.array(v3, dtype="float64")
v_com = (m1*v1+m2*v2+m3*v3)/(m1+m2+m3)

def ThreeBodyEquations(w, t, G, m1, m2, m3):
    r1 = w[:3]
    r2 = w[3:6]
    r3 = w[6:9]
    v1 = w[9:12]
    v2 = w[12:15]
    v3 = w[15:18]
    r12 = sci.linalg.norm(r2 - r1)
    r13 = sci.linalg.norm(r3 - r1)
    r23 = sci.linalg.norm(r3 - r2)

    dv1bydt = K1 * m2 * (r2 - r1) / r12 ** 3 + K1 * m3 * (r3 - r1) / r13 ** 3
    dv2bydt = K1 * m1 * (r1 - r2) / r12 ** 3 + K1 * m3 * (r3 - r2) / r23 ** 3
    dv3bydt = K1 * m1 * (r1 - r3) / r13 ** 3 + K1 * m2 * (r2 - r3) / r23 ** 3
    dr1bydt = K2 * v1
    dr2bydt = K2 * v2
    dr3bydt = K2 * v3
    r12_derivs = sci.concatenate((dr1bydt, dr2bydt))
    r_derivs = sci.concatenate((r12_derivs, dr3bydt))
    v12_derivs = sci.concatenate((dv1bydt, dv2bydt))
    v_derivs = sci.concatenate((v12_derivs, dv3bydt))
    derivs = sci.concatenate((r_derivs, v_derivs))
    return derivs
init_params=sci.array([r1,r2,r3,v1,v2,v3]) 
init_params=init_params.flatten()
time_span=sci.linspace(0,20,500) 
import scipy.integrate
three_body_sol=sci.integrate.odeint(ThreeBodyEquations,init_params,time_span,args=(G,m1,m2,m3))

r1_sol=three_body_sol[:,:3]
r2_sol=three_body_sol[:,3:6]
r3_sol=three_body_sol[:,6:9]
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')

line_2, = ax.plot(r2_sol[:, 0], r2_sol[:, 1], r2_sol[:, 2], color="tab:red")
line_1, = ax.plot(r1_sol[:, 0], r1_sol[:, 1], r1_sol[:, 2], color="darkblue")
line_3, = ax.plot(r3_sol[:, 0], r3_sol[:, 1], r3_sol[:, 2])


def animate(i):
    line_1.set_xdata(r1_sol[:i, 0])
    line_1.set_ydata(r1_sol[:i, 1])
    line_1.set_3d_properties(r1_sol[:i, 2])
    line_2.set_xdata(r2_sol[:i, 0])
    line_2.set_ydata(r2_sol[:i, 1])
    line_2.set_3d_properties(r2_sol[:i, 2])
    line_3.set_xdata(r3_sol[:i, 0])
    line_3.set_ydata(r3_sol[:i, 1])
    line_3.set_3d_properties(r3_sol[:i, 2])
    return line_1, line_2, line_3,
ani = animation.FuncAnimation(fig=fig, func=animate, interval=10)
plt.show()
