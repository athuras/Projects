#!/usr/bin/env python
import numpy as np


class Multivariate():
    '''
    Multivariate Normal Distribution: N(mu, Sigma)
    Usage: >>N = Gauss.Multivariate(3) # where 3 is dimensionality
           >>N.evaluate([[0],[0],[0]])
           >>0.15915494309189535
    '''

    def __init__(self, k, mu=None, sigma=None, **kwargs):
        '''
        Initialize the distribution with dimensionality,
        and optional means, and/or covariance matrix.
        dataType defaults to np.double
        '''
        if 'dataType' not in kwargs:
            dataType = np.double
        else:
            dataType = kwargs['dataType']

        if mu is None:
            mu = np.transpose(np.matrix(np.zeros(k, dtype=dataType)))
        elif type(mu) is not np.matrix:
            mu = np.transpose(np.matrix(mu, dtype=dataType))

        if sigma is None:
            cov = np.matrix(np.identity(k, dtype=dataType))
        elif type(sigma) is not np.matrix:
            cov = np.matrix(cov, dtype=dataType)
            # TODO: check that supplied cov is positive definite
            for i in cov.shape:  # Ensure supplied cov is square
                assert i == k

        self.dim = k
        self.mean = mu
        self.cov = cov
        self.det = np.linalg.det(cov)
        self.inv = np.linalg.inv(cov)
        self.dtype = dataType

    def evaluate(self, x):
        '''
        Evaluate the Multivariate Gaussian PDF at vector x
        return np.double
        enforces len(x) == k
        '''
        if type(x) is not np.matrix:
            x = np.matrix(x, dtype=self.dtype)

        phi = np.subtract(x, self.mean)
        return np.double(np.double(1) / (np.double(2) * np.pi ** (self.dim / 2) *
                np.sqrt(self.det)) * np.exp(np.double(-0.5) *
                np.transpose(phi) * self.inv * phi))
