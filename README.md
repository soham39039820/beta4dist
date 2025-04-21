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
pip install beta4dist
```
