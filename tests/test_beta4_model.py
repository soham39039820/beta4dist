# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:48:13 2025

@author: soham
"""

# tests/test_beta4_model.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


import numpy as np
from beta4dist.distribution import r4beta
from beta4dist.beta4_model import LBE4beta, fit4beta

def generate_sample_data():
    return r4beta(n=100, theta1=200, theta2=300, alpha1=2.0, alpha2=3.0)

def test_LBE4beta():
    data = generate_sample_data()
    params = LBE4beta(data)

    # Check it's a tuple
    assert isinstance(params, tuple)

    # Check length
    assert len(params) == 4

    # Check all values are floats (optional but good!)
    for val in params:
        assert isinstance(val, float)

def test_fit4beta():
    data = generate_sample_data()
    result = fit4beta(data)
    
    assert isinstance(result, dict)
    
    # Basic parameter and model checks
    for key in ['theta1', 'theta2', 'alpha1', 'alpha2', 'loglik', 'AIC']:
        assert key in result
    
    assert 'status' in result
    assert result['status'] in [0, 1]
