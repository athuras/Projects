#!/usr/bin/env python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import mandelbrot as md

res = (2048, 2048)
DPI = 100.
# Still not entirely sure why the image gets flipped, but w/e, YOLO etc.
mset = md.generate_set(-0.85, -0.7, 0., 0.25, resolution=res, maxiter=2048)
fig = plt.figure(figsize=map(lambda x: x / DPI,  res))
ax = fig.add_subplot(111)
ax.imshow(mset.reshape(res), cmap='jet', aspect='equal')
fig.savefig("mandelbrot_pycuda.png", dpi=DPI)

interesting_parameters = [
        {'center' = -.743030-.126433j,
         'mag' = 190.99}]

print 'fin'
