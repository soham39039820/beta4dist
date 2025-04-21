# beta4dist

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

## Features

- **Sampling**: Generate random samples from the four-parameter Beta distribution.
- **Parameter Estimation**: Perform likelihood-based estimation for fitting the distribution to observed data.
- **Robustness**: Ensure that parameter estimates obey the natural restrictions of the distribution.
- **Flexible Usage**: Suitable for a wide range of applications, including statistical modeling and simulation.

## Installation

To install **beta4dist**, you can use pip from PyPI:

```bash
`pip install beta4dist`

Generate Samples from the Four-Parameter Beta Distribution

You can generate random samples from the four-parameter Beta distribution using the `r4beta` function:

```python
from beta4dist.distribution import r4beta

# Define parameters
theta1, theta2 = 0, 1
alpha1, alpha2 = 2.5, 3.0

# Generate 100 samples
samples = r4beta(n=100, theta1=theta1, theta2=theta2, alpha1=alpha1, alpha2=alpha2)

print(samples)

### Fit the Four-Parameter Beta Distribution Using Likelihood-Based Estimation

The `LBE4beta` function allows you to fit the four-parameter Beta distribution to your data using likelihood-based estimation:

```python
from beta4dist.beta4_model import LBE4beta, fit4beta
from beta4dist.distribution import r4beta

# Generate sample data
data = r4beta(n=100, theta1=0, theta2=1, alpha1=2.5, alpha2=3.0)

# Estimate parameters
estimates = LBE4beta(data)
print("Estimated Parameters:", estimates)

# Fit and display model diagnostics
fit_results = fit4beta(data)
print("Model Fit Summary:", fit_results)

### Example Test Cases

`beta4dist` includes pre-defined test cases to ensure that the model behaves as expected. You can run these tests using `pytest`.

### Install pytest if you haven't already:

```bash
pip install pytest

### Run test using
pytest

### NOTE: Windows users — if 'pytest' is not recognized, try:
"C:\Users\soham\AppData\Roaming\Python\Python310\Scripts\pytest.exe".

### Licensing

`beta4dist` is licensed under the MIT License. See the LICENSE file for more details.

### References

For more information on the four-parameter Beta distribution and its applications, please refer to the following publication:

- **Paper Title**: *beta4dist: A Python Package for the Four-Parameter Beta Distribution and Likelihood-Based Estimation*
- **Authors**: Soham Ghosh, Sujay Mukhoti, Pritee Sharma


