# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:29:49 2025

@author: soham
"""

# distribution.py

import numpy as np
from scipy.stats import beta
from scipy.optimize import brentq

def d4beta(x, theta1, theta2, alpha1, alpha2):
    """
    Density function of the four-parameter Beta distribution.

    Parameters:
    x : array_like or float
        Quantiles.
    theta1 : float
        Lower bound of the distribution.
    theta2 : float
        Upper bound of the distribution.
    alpha1 : float
        Shape parameter 1.
    alpha2 : float
        Shape parameter 2.

    Returns:
    array_like or float
        Density values at the given quantiles.
    """
    # Convert x to an array if it's a single number
    x = np.atleast_1d(x)  

    # Calculate the density
    x_transformed = (x - theta1) / (theta2 - theta1)
    density = beta.pdf(x_transformed, alpha1, alpha2) / (theta2 - theta1)

    # Return a single value if x was originally a single number
    if x.size == 1:
        return density[0]
    else:
        return density
    

def p4beta(x, theta1, theta2, alpha1, alpha2):
    """
    Cumulative distribution function (CDF) of the four-parameter Beta distribution.

    Parameters:
    x : array_like or float
        Quantiles.
    theta1 : float
        Lower bound of the distribution.
    theta2 : float
        Upper bound of the distribution.
    alpha1 : float
        Shape parameter 1.
    alpha2 : float
        Shape parameter 2.

    Returns:
    array_like or float
        CDF values at the given quantiles.
    """
    x = np.atleast_1d(x)  # Convert x to an array if it's a single number
    x_transformed = (x - theta1) / (theta2 - theta1)
    cdf_values = beta.cdf(x_transformed, alpha1, alpha2)
    if x.size == 1:
        return cdf_values[0]  # Return a single value if x was originally a single number
    else:
        return cdf_values


def q4beta(p, theta1, theta2, alpha1, alpha2):
    """
    Quantile function of the four-parameter Beta distribution.

    Parameters:
    p : array_like or float
        Probabilities.
    theta1 : float
        Lower bound of the distribution.
    theta2 : float
        Upper bound of the distribution.
    alpha1 : float
        Shape parameter 1.
    alpha2 : float
        Shape parameter 2.

    Returns:
    array_like or float
        Quantiles corresponding to the given probabilities.
    """
    p = np.atleast_1d(p)  # Convert p to an array if it's a single number
    quantiles = theta1 + (theta2 - theta1) * beta.ppf(p, alpha1, alpha2)
    if p.size == 1:
        return quantiles[0]  # Return a single value if p was originally a single number
    else:
        return quantiles
    
   
def r4beta(n, theta1, theta2, alpha1, alpha2):
    """
    Random sample generation for the four-parameter Beta distribution.

    Parameters:
    n : int
        Number of random samples to generate.
    theta1 : float
        Lower bound of the distribution.
    theta2 : float
        Upper bound of the distribution.
    alpha1 : float
        Shape parameter 1.
    alpha2 : float
        Shape parameter 2.

    Returns:
    array_like
        Random samples from the four-parameter Beta distribution.
    """
    return theta1 + (theta2 - theta1) * beta.rvs(alpha1, alpha2, size=n)
