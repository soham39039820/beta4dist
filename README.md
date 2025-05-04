# beta4dist

[![PyPI version](https://badge.fury.io/py/beta4dist.svg)](https://badge.fury.io/py/beta4dist)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**beta4dist** is a Python package designed for working with the four-parameter Beta distribution and implementing likelihood-based estimation methods for its parameters. It allows for sampling, parameter fitting, and likelihood-based estimation (LBE) using a flexible four-parameter formulation of the Beta distribution.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Examples](#examples)
  - [Generate Samples](#generate-samples-from-the-four-parameter-beta-distribution)
  - [Fit the Distribution](#fit-the-four-parameter-beta-distribution-using-likelihood-based-estimation)
  - [Test Cases](#example-test-cases)
- [Licensing](#licensing)
- [References](#references)

## Description

The goal of **beta4dist** is to provide an easy-to-use and efficient interface for working with the four-parameter Beta distribution. This package supports the following features:

- **Sampling** from the four-parameter Beta distribution.
- **Fitting** the distribution to data using likelihood-based estimation (LBE).
- Implementing various **parameter inference techniques** for reliable statistical modeling.

The four-parameter Beta distribution extends the standard Beta distribution by introducing location parameters, providing additional flexibility for modeling data confined to finite intervals with skewness and kurtosis. This makes it especially useful in fields like hydrology, environmental science, and reliability engineering.

---
## Features

- **Sampling** from the four-parameter Beta distribution  
- **Parameter estimation** using likelihood-based methods  
- **Diagnostic summaries** for goodness-of-fit  
- **Fully tested** with Pytest  
- **Applicable in real-world settings** involving environmental and reliability data

---

## Requirements

- Python ≥ 3.7  
- numpy  
- scipy
---

## Installation

To install **beta4dist**, you can use pip from PyPI:

### To install the package for the first time:
```bash
pip install beta4dist
```

### To upgrade to the latest version:
```bash
pip install --upgrade beta4dist
```

### 2. Clone the repository from GitHub:
If you prefer to work with the latest code or contribute, you can clone the repository directly from GitHub:

```bash
git clone https://github.com/soham39039820/beta4dist.git
```

After cloning, navigate to the project directory and install it:

```bash
cd beta4dist
pip install .
```

### Generate Samples from the Four-Parameter Beta Distribution

You can generate random samples from the four-parameter Beta distribution using the `r4beta` function:

```python
import beta4dist
from beta4dist.distribution import r4beta

# Define parameters
theta1, theta2 = 0, 1
alpha1, alpha2 = 2.5, 3.0

# Generate 100 samples
samples = r4beta(n=100, theta1=theta1, theta2=theta2, alpha1=alpha1, alpha2=alpha2)

print(samples)
```
### Fit the Four-Parameter Beta Distribution Using Likelihood-Based Estimation

The `LBE4beta` function allows you to obtain the likelihood-based estimators of the four-parameter Beta distribution to your data. The `fit4beta` offers an end-to-end interface to fit the distribution to real data, with automatic handling of boundary estimation, internal consistency checks, and feasibility diagnostics.

```python
from beta4dist.beta4_model import LBE4beta, fit4beta

estimates = LBE4beta(data)
print("Estimated Parameters:", estimates)

# Fit and display model diagnostics
fit_results = fit4beta(data)
print("Model Fit Summary:", fit_results)
```
### Example Test Cases
beta4dist includes pre-defined test cases to ensure that the model behaves as expected. You can run these tests using pytest.

Install `pytest` if you haven't already:

```bash
pip install pytest
```
Run test using:

```bash
pytest
```
Windows users — if `pytest` is not recognized, try:

```bash
"C:\Users\soham\AppData\Roaming\Python\Python310\Scripts\pytest.exe"
```

### Version
The current version of `beta4dist` is 0.3.1.

To check the version in Python, use the following code:
```python
import beta4dist
print(beta4dist.__version__)
```

### Licensing

`beta4dist` is licensed under the MIT License. See the LICENSE file for more details.

### References

For more information on the four-parameter Beta distribution and its applications, please refer to the following publication:

- **Paper Title**: *beta4dist: A Python Package for the Four-Parameter Beta Distribution and Likelihood-Based Estimation*
- **Authors**: Soham Ghosh, Sujay Mukhoti, Abhirup Banerjee

