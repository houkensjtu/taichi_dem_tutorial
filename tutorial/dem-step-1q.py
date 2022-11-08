import taichi as ti
import math
import os

ti.init(arch=ti.cpu)
vec = ti.math.vec2  # 2-D Vector type

SAVE_FRAMES = False

window_size = 600  # Number of pixels of the window
n = 8192  # Number of grains

density = 100.0
stiffness = 8e3
restitution_coef = 0.001
gravity = -9.81
dt = 0.0001  # Larger dt might lead to unstable results.
substeps = 60

grid_n = 128
grid_size = 1.0 / grid_n  # Simulation domain of size [0, 1]
print(f"Grid size: {grid_n}x{grid_n}")

grain_r_min = 0.002
grain_r_max = 0.003


'''
Your code here
Implement the Grain dataclass.
Then declare a field to store Grains.
'''

@ti.kernel
def init():
'''
Your code here
Spread grains in the computation domain.
'''
    pass


@ti.kernel
def update():
    pass


@ti.kernel
def apply_bc():
    pass


@ti.func
def resolve(i, j):
    pass


@ti.kernel
def contact(gf: ti.template()):
    pass


init()
gui = ti.GUI('Taichi DEM', (window_size, window_size))
step = 0

if SAVE_FRAMES:
    os.makedirs('output', exist_ok=True)

while gui.running:
    for s in range(substeps):
        update()
        apply_bc()
        contact(gf)
    pos = gf.p.to_numpy()
    r = gf.r.to_numpy() * window_size
    gui.circles(pos, radius=r)
    if SAVE_FRAMES:
        gui.show(f'output/{step:06d}.png')
    else:
        gui.show()
    step += 1
