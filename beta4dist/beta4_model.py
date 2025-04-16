# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:17:36 2025

@author: soham
"""

import numpy as np
from scipy.stats import beta
from scipy.special import digamma, loggamma
from scipy.optimize import minimize
from scipy.integrate import quad
import statistics

def LBE4beta(data):
    """
    Estimates the parameters of the four-parameter Beta distribution using 
    marginal likelihood estimators based on order statistics, as described 
    in the provided theorem.

    Parameters:
    data : array_like
        The observed data.

    Returns:
    tuple
        A tuple containing the estimated parameters (theta1, theta2, alpha1, alpha2).
    """

    # Estimate theta1 and theta2 using order statistics
    data_sorted = np.sort(data)
    theta1_hat = data_sorted[0]
    theta2_hat = data_sorted[-1]

    # Calculate z_hat values
    z_hat = (data_sorted[1:-1] - theta1_hat) / (theta2_hat - theta1_hat)

    # Define the marginal likelihood equations for alpha1 and alpha2
    def neg_marginal_likelihood(params):
        alpha1, alpha2 = params

        n = len(data)

        # Calculate expectations using numerical integration (quadrature)
        def integrand1(u):
            return np.log(u) * beta.pdf(u, alpha1, alpha2) * (u > z_hat[-1])

        def integrand2(u):
            return np.log(u) * beta.pdf(u, alpha1, alpha2) * (u < z_hat[0])

        def integrand3(u):
            return np.log(1 - u) * beta.pdf(u, alpha1, alpha2) * (u > z_hat[-1])

        def integrand4(u):
            return np.log(1 - u) * beta.pdf(u, alpha1, alpha2) * (u < z_hat[0])

        E1 = quad(integrand1, 0, 1, limit=100)[0]
        E2 = quad(integrand2, 0, 1, limit=100)[0]
        E3 = quad(integrand3, 0, 1, limit=100)[0]
        E4 = quad(integrand4, 0, 1, limit=100)[0]

        # Marginal likelihood equations from the theorem (negated for minimization)
        eq1 = -(n * (digamma(alpha1 + alpha2) - digamma(alpha1)) +
               np.sum(np.log(z_hat)) +
               E1 / (1 - beta.cdf(z_hat[-1], alpha1, alpha2)) +
               E2 / beta.cdf(z_hat[0], alpha1, alpha2))

        eq2 = -(n * (digamma(alpha1 + alpha2) - digamma(alpha2)) +
               np.sum(np.log(1 - z_hat)) +
               E3 / (1 - beta.cdf(z_hat[-1], alpha1, alpha2)) +
               E4 / beta.cdf(z_hat[0], alpha1, alpha2))

        # Combine the equations (e.g., sum of squares)
        return eq1**2 + eq2**2 

    # Solve the equations to find alpha1 and alpha2
    # Use MoM estimates as initial values
    mea = np.mean(z_hat)
    var = statistics.variance(z_hat)
    com_term = (mea * (1 - mea)) / var
    guess_1 = (com_term - 1) * mea
    guess_2 = (com_term - 1) * (1 - mea) 
    
    bounds = [(1e-6, None), (1e-6, None)]
    
    guess_1 = max(abs(guess_1), 1e-3)  # Ensure guess_1 is positive and not too small
    guess_2 = max(abs(guess_2), 1e-3)  # Ensure guess_2 is positive and not too small
    
    # Minimize the negative marginal likelihood with bounds
    result = minimize(neg_marginal_likelihood, [guess_1, guess_2], bounds=bounds, method='L-BFGS-B')
    alpha1_hat, alpha2_hat = result.x
    
    return theta1_hat, theta2_hat, alpha1_hat, alpha2_hat

def fit4beta(data):
    """
    Fits the four-parameter Beta distribution to data, performs consistency checks,
    and reports model selection criteria.

    Parameters:
    data : array_like
        The observed data.

    Returns:
    dict
        A dictionary containing the estimated parameters, model selection criteria,
        and consistency check results.
    """

    # Estimate parameters
    theta1_hat, theta2_hat, alpha1_hat, alpha2_hat = LBE4beta(data)

    consistency_status = "Passed"  # Initialize to "Passed"
    if not (theta1_hat < theta2_hat):
        consistency_status = "Failed: theta1 is greater than theta2"
    if not (alpha1_hat > 0 and alpha2_hat > 0):
        consistency_status = "Failed: alpha1 or alpha2 not positive"

    # Calculate log-likelihood
    z = (data - theta1_hat) / (theta2_hat - theta1_hat)
    z[z == 0] += 1e-6
    z[z == 1] -= 1e-6
    loglik = np.sum(beta.logpdf(z, alpha1_hat, alpha2_hat))

    # Calculate model selection criteria
    k = 4  # Number of parameters
    n = len(data)
    AIC = -2 * loglik + 2 * k
    BIC = -2 * loglik + k * np.log(n)
    AICc = AIC + (2 * k * (k + 1)) / (n - k - 1)
    HQIC = -2 * loglik + 2 * k * np.log(np.log(n))

    # Store results in a dictionary
    results = {
        "theta1": theta1_hat,
        "theta2": theta2_hat,
        "alpha1": alpha1_hat,
        "alpha2": alpha2_hat,
        "loglik": loglik,
        "AIC": AIC,
        "BIC": BIC,
        "AICc": AICc,
        "HQIC": HQIC,
        "consistency_check": consistency_status  # Include the status string
    }

    return results

