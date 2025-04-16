# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:44:33 2025

@author: soham
"""

from distribution import d4beta, p4beta, q4beta, r4beta
from beta4_model import LBE4beta, fit4beta


# Define parameters
theta1, theta2 = 200, 300
alpha1, alpha2 = 2.5, 3.0

# Evaluate PDF at a point
pdf_val = d4beta(x=0.5, theta1=theta1, theta2=theta2, alpha1=alpha1, alpha2=alpha2)

# Evaluate CDF at a point
cdf_val = p4beta(x=0.5, theta1=theta1, theta2=theta2, alpha1=alpha1, alpha2=alpha2)

# Compute quantile (inverse CDF) at a given probability level
quantile_val = q4beta(p=0.95, theta1=theta1, theta2=theta2, alpha1=alpha1, alpha2=alpha2)

# Generate random samples
samples = r4beta(n=100, theta1=theta1, theta2=theta2, alpha1=alpha1, alpha2=alpha2)

estimates = LBE4beta(samples)

results = fit4beta(samples)

print(results)