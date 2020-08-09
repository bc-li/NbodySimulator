import ast
import math
from itertools import combinations, permutations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import scipy as sci
from scipy import integrate


G = 6.67408e-11 
mass_of_sun = 1.989e+30  #mass of the sun (kg)
dis_of_alpha_centauri = 5.326e+12  #distance between stars in Alpha Centauri (m)
revolution_speed_earth = 30000   #relative velocity of earth around the sun (m/s)
orbital_period = 79.91 * 365 * 24 * 3600 * 0.51  #orbital period of Alpha Centauri (s)
constant_1 = G * orbital_period * mass_of_sun / (dis_of_alpha_centauri ** 2 * revolution_speed_earth)
constant_2 = revolution_speed_earth * orbital_period / dis_of_alpha_centauri
print("Let us know how many planets you want to simulate.")
number_of_planets = int(input())
mass = []
for x in range(number_of_planets):
    print("Please input the mass of No.", x+1, "planet.")
    mass_temp = float(input())
    mass.append(mass_temp)


r = []

for x in range(number_of_planets):
    print("Please input the initial position of NO.", x+1, "planet. use format: [x, y, z].")
    r_temp = ast.literal_eval(input())
    r_temp = list(map(float, r_temp))
    r.append(r_temp)

for x in range(number_of_planets):
    r[x] = np.array(r[x], dtype="float64")


rcomup = np.array([0, 0, 0])
rcomdown = 0
for x in range(number_of_planets):
    rcomup = rcomup + mass[x]*r[x]
    rcomdown = rcomdown + mass[x]


r_com = rcomup/rcomdown

velocity = []
for x in range(number_of_planets):
    print("Please input the initial velocity of NO.", x+1, "planet. use format: [x, y, z].")
    velocity_1 = ast.literal_eval(input())
    velocity_1 = list(map(float, velocity_1))
    velocity.append(velocity_1)
for x in range(number_of_planets):
    velocity[x] = np.array(velocity[x], dtype="float64")

vcomup = np.array([0, 0, 0])
vcomdown = 0
for x in range(number_of_planets):
    vcomup = vcomup + mass[x]*velocity[x]
    vcomdown = vcomdown + mass[x]

v_com = vcomup/vcomdown


def NBodyEquation(w, t, G, *mass):
    for r_counter in range(number_of_planets):
        r[r_counter] = w[(3*r_counter):(3*(r_counter+1))]
        velocity[r_counter] = w[(3*number_of_planets+3*r_counter):(3*number_of_planets+3*r_counter+3)]

    dvbydt = []
    dvbydt_temp = np.array([0, 0, 0])
    for y in range(number_of_planets):
        for z in range(number_of_planets):
            if y != z:
                dvbydt_temp = dvbydt_temp + constant_1 * \
                    mass[z] * (r[z]-r[y])/np.linalg.norm(r[z]-r[y])**3
        dvbydt.append(dvbydt_temp)
        dvbydt_temp = np.array([0, 0, 0])

    drbydt = []
    for z in range(number_of_planets):
        drbydt_1 = constant_2*velocity[z]
        drbydt.append(drbydt_1)

    r_derivs = []
    for n in range(number_of_planets):
        r_derivs = np.concatenate((r_derivs, drbydt[n]))

    v_derivs = []
    for dn in range(number_of_planets):
        v_derivs = np.concatenate((v_derivs, dvbydt[dn]))

    derivs = np.concatenate((r_derivs, v_derivs))
    return derivs

init_params = np.array([r, velocity])  
init_params = init_params.flatten()  
time_span = np.linspace(0, 20, 500)  
solution_n_body = sci.integrate.odeint(NBodyEquation, init_params, time_span, args=(G, *mass))
r_sol = []
for zz in range(number_of_planets):
    r_sol_temp = solution_n_body[:, 3*zz: 3*(zz+1)]
    r_sol.append(r_sol_temp)


fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')
line = []
for n_counter in range(number_of_planets):
    line_temp, = ax.plot(r_sol[n_counter][:, 0], r_sol[n_counter][:, 1], r_sol[n_counter][:, 2])
    line.append(line_temp,)


def animate(i):
    for s_counter in range(number_of_planets):
        line[s_counter].set_xdata(r_sol[s_counter][:i, 0])
        line[s_counter].set_ydata(r_sol[s_counter][:i, 1])
        line[s_counter].set_3d_properties(r_sol[s_counter][:i, 2])
    for n in range(number_of_planets):
        return line[n],


ani = animation.FuncAnimation(fig=fig, func=animate, interval=10)

plt.show()
