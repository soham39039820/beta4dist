# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:47:29 2025

@author: soham
"""

# tests/test_distribution.py

import numpy as np
from beta4dist.distribution import d4beta, p4beta, q4beta, r4beta

def test_d4beta():
    val = d4beta(x=250.5, theta1=200, theta2=300, alpha1=2.5, alpha2=3.0)
    assert val > 0.0  # Ensure it's greater than 0.0 (not strictly greater than 0)
    assert val != 0.0
    
def test_p4beta():
    val = p4beta(x=0.5, theta1=200, theta2=300, alpha1=2.0, alpha2=3.0)
    assert 0 <= val <= 1

def test_q4beta():
    val = q4beta(p=0.95, theta1=200, theta2=300, alpha1=2.0, alpha2=3.0)
    assert 200 <= val <= 300

def test_r4beta():
    samples = r4beta(n=10, theta1=200, theta2=300, alpha1=2.0, alpha2=3.0)
    assert isinstance(samples, np.ndarray)
    assert len(samples) == 10
