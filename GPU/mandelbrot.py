# Adaptation of the pyCUDA example by ian@ianozsvald.com
# but with matplotlib instead

import numpy as np
import pycuda.driver as cuda
import pycuda.tools
import pycuda.autoinit
import pycuda.gpuarray as gpuarray

from pycuda.compiler import SourceModule
from pycuda.elementwise import ElementwiseKernel


complex_gpu = ElementwiseKernel(
    "pycuda::complex<float> *z, pycuda::complex<float> *q, int *iteration, int maxiter",
    """
    for (int n=0; n < maxiter; n++) {
        z[i] = (z[i]*z[i]) + q[i];
        if (abs(z[i]) > 2.0f) {
            iteration[i] = n;
        };
    }""", "complex5", preamble="#include <pycuda-complex.hpp>",)


def calculate_z_gpu(q, maxiter, z):
    '''
    Returns the number of iterations required for a complex number to escape
    the mandelbrot set.
    '''
    output = np.resize(np.array(0, dtype=np.int32), q.shape)
    q_gpu = gpuarray.to_gpu(q.astype(np.complex64))
    z_gpu = gpuarray.to_gpu(z.astype(np.complex64))

    iterations_gpu = gpuarray.to_gpu(output)
    complex_gpu(z_gpu, q_gpu, iterations_gpu, maxiter)
    iterations = iterations_gpu.get()
    return iterations


def generate_set(x_min, x_max, y_min, y_max, resolution=(1000., 1000.), maxiter=300):
    '''Return the set as a 2-d array'''
    xx = np.arange(x_min, x_max, (x_max - x_min) / resolution[0])
    yy = np.arange(y_min, y_max, (y_max - y_min) / resolution[1]) * 1j
    yy = yy.astype(np.complex64)
    q = np.ravel(xx + yy[:, None]).astype(np.complex64)
    z = np.zeros_like(q)
    return calculate_z_gpu(q, maxiter, z)
