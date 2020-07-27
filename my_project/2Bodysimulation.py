import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
G = 6.67408e-11 
mass_nd = 1.989e+30  
r_nd = 5.326e+12  
velocity_nd = 30000  
t_nd = 79.91 * 365 * 24 * 3600 * 0.51  
const_1 = G * t_nd * mass_nd / (r_nd ** 2 * velocity_nd)
const_2 = velocity_nd * t_nd / r_nd
mass_1 = 1.1  
mass_2 = 0.907 
r1 = [-0.5, 0, 0] 
r2 = [0.5, 0, 0]  
r1 = sci.array(r1, dtype="float64")
r2 = sci.array(r2, dtype="float64")
r_com = (mass_1 * r1 + mass_2 * r2) / (mass_1 + mass_2)
velocity_1 = [0.01, 0.01, 0]  
velocity_2 = [-0.05, 0, -0.1] 
velocity_1 = sci.array(velocity_1, dtype="float64")
velocity_2 = sci.array(velocity_2, dtype="float64")
v_com = (mass_1 * velocity_1 + mass_2 * velocity_2) / (mass_1 + mass_2)
def Calculate(w, t, G, mass_1, mass_2):
    r1 = w[:3]
    r2 = w[3:6]
    velocity_1 = w[6:9]
    velocity_2 = w[9:12]
    r = sci.linalg.norm(r2 - r1)
    dvelocity_1bydt = const_1 * mass_2 * (r2 - r1) / r ** 3
    dvelocity_2bydt = const_1 * mass_1 * (r1 - r2) / r ** 3
    dr1bydt = const_2 * velocity_1
    dr2bydt = const_2 * velocity_2
    r_derivs = sci.concatenate((dr1bydt, dr2bydt))
    derivs = sci.concatenate((r_derivs, dvelocity_1bydt, dvelocity_2bydt))
    return derivs
init_params = sci.array([r1, r2, velocity_1, velocity_2])  
init_params = init_params.flatten()
time_span = sci.linspace(0, 8, 500)
import scipy.integrate
two_body_sol = sci.integrate.odeint(Calculate, init_params, time_span, args=(G, mass_1, mass_2))
r1_sol = two_body_sol[:, :3]
r2_sol = two_body_sol[:, 3:6]
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')
x = r1_sol[:, 0]
line_2, = ax.plot(r2_sol[:, 0], r2_sol[:, 1], r2_sol[:, 2], color="tab:red")
line_1, = ax.plot(r1_sol[:, 0], r1_sol[:, 1], r1_sol[:, 2], color="darkblue")
def animate(i):
    line_1.set_xdata(r1_sol[:i, 0])
    line_1.set_ydata(r1_sol[:i, 1])
    line_1.set_3d_properties(r1_sol[:i, 2])
    line_2.set_xdata(r2_sol[:i, 0])
    line_2.set_ydata(r2_sol[:i, 1])
    line_2.set_3d_properties(r2_sol[:i, 2])
    return line_1, line_2
ani = animation.FuncAnimation(fig=fig, func=animate, interval=10)
plt.show()