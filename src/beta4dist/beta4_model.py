# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:17:36 2025

@author: soham
"""

import numpy as np
from scipy.stats import beta
from scipy.optimize import minimize
from scipy.special import digamma
from scipy.stats import kstest, cramervonmises

def LBE4beta(data, n_samples=10000):
    """
    Estimates the parameters of the four-parameter Beta distribution using 
    marginal likelihood estimators based on order statistics and Monte Carlo integration.

    Parameters:
    data : array_like
        The observed data.
    n_samples : int, optional
        The number of samples to use for Monte Carlo integration (default is 10,000).
    
    Returns:
    np.ndarray
        Array containing the estimated parameters (theta1, theta2, alpha1, alpha2).
    """
    
    # Check for zero variance
    if np.var(data) == 0:
        print("Error: The input data has zero variance. Estimation is not possible.")
        return np.array([np.nan, np.nan, np.nan, np.nan])

    # Estimate location parameters using order statistics
    data_sorted = np.sort(data)
    theta1_hat = data_sorted[0]
    theta2_hat = data_sorted[-1]

    # Normalize to [0,1] scale
    z_hat = (data_sorted[1:-1] - theta1_hat) / (theta2_hat - theta1_hat)

    def monte_carlo_integral(func, lower, upper, n_samples):
        """
        Perform Monte Carlo integration to estimate the integral of a function.
        """
        samples = np.random.uniform(lower, upper, n_samples)
        return np.mean(func(samples))

    def neg_marginal_likelihood(params):
        alpha1, alpha2 = params
        n = len(z_hat)
        eps = 1e-8  # small threshold

        # Clip to avoid 0 or 1
        z_hat_clipped = np.clip(z_hat, eps, 1 - eps)
        z_min = np.min(z_hat_clipped)
        z_max = np.max(z_hat_clipped)

        # Define integrands safely
        log_u = lambda u: np.log(np.clip(u, eps, 1)) * beta.pdf(u, alpha1, alpha2)
        log_1mu = lambda u: np.log(np.clip(1 - u, eps, 1)) * beta.pdf(u, alpha1, alpha2)

        # Perform Monte Carlo integration
        E1 = monte_carlo_integral(log_u, z_max + eps, 1 - eps, n_samples)
        E2 = monte_carlo_integral(log_u, eps, z_min - eps, n_samples)
        E3 = monte_carlo_integral(log_1mu, z_max + eps, 1 - eps, n_samples)
        E4 = monte_carlo_integral(log_1mu, eps, z_min - eps, n_samples)

        eq1 = -(n * (digamma(alpha1 + alpha2) - digamma(alpha1)) +
                np.sum(np.log(z_hat_clipped)) +
                E1 / (1 - beta.cdf(z_max, alpha1, alpha2) + eps) +
                E2 / (beta.cdf(z_min, alpha1, alpha2) + eps))

        eq2 = -(n * (digamma(alpha1 + alpha2) - digamma(alpha2)) +
                np.sum(np.log(1 - z_hat_clipped)) +
                E3 / (1 - beta.cdf(z_max, alpha1, alpha2) + eps) +
                E4 / (beta.cdf(z_min, alpha1, alpha2) + eps))

        return eq1**2 + eq2**2

    # Initial guess via method of moments
    mean_z = np.mean(z_hat)
    var_z = np.var(z_hat, ddof=1)
    common_term = (mean_z * (1 - mean_z)) / var_z - 1
    guess_1 = max(common_term * mean_z, 1e-3)
    guess_2 = max(common_term * (1 - mean_z), 1e-3)

    bounds = [(1e-6, None), (1e-6, None)]
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
    # Check for zero variance
    if np.var(data) == 0:
        print("Error: The input data has zero variance. Estimation is not possible.")
        return np.array([np.nan, np.nan, np.nan, np.nan])

    # Estimate parameters
    theta1_hat, theta2_hat, alpha1_hat, alpha2_hat = LBE4beta(data)

    # Status check: 1 if both alpha1 and alpha2 are positive, else 0
    status = 1 if (alpha1_hat > 0 and alpha2_hat > 0) else 0

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
    
    # Store results
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
        "status": status,  # 1 if passed, 0 if failed
    }

    return results

