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


## Examples

Here are some basic examples demonstrating how to use **beta4dist** for generating samples and performing likelihood-based estimation.

### Generate Samples from the Four-Parameter Beta Distribution

You can generate random samples from the four-parameter Beta distribution using the `r4beta` function:


### Fit the Four-Parameter Beta Distribution Using Likelihood-Based Estimation

The `LBE4beta` function allows you to fit the four-parameter Beta distribution to your data using likelihood-based estimation:


### Example Test Cases

**beta4dist** includes pre-defined test cases to ensure that the model behaves as expected. You can run these tests using `pytest`:


This will execute the tests and report any issues.

## Licensing

**beta4dist** is licensed under the **MIT License**. See the LICENSE file for more details.

## References

For more information on the four-parameter Beta distribution and its applications, please refer to the following publication:

- **Paper Title**: *beta4dist: A Python Package for the Four-Parameter Beta Distribution and Likelihood-Based Estimation*
- **Authors**: Soham Ghosh, Sujay Mukhoti, Pritee Sharma

---

For additional information, bug reports, or feature requests, please visit the [GitHub repository](https://github.com/soham39039820/beta4dist) or open an issue or pull request.

