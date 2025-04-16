
# beta4dist

**beta4dist** is a Python package designed for working with the four-parameter beta distribution and implementing likelihood-based estimation methods for its parameters. The package provides functions for generating samples, fitting the four-parameter beta distribution, and performing likelihood-based estimation (LBE).

## Description

The goal of **beta4dist** is to provide an easy-to-use interface for:

- Sampling from the four-parameter beta distribution.
- Fitting the four-parameter beta distribution using likelihood-based estimation.
- Implementing various estimation techniques for parameter inference.

This package is useful for statistical modeling and simulation, especially in situations where data follow a beta distribution but with additional flexibility due to the four-parameter formulation.

## Installation

To install **beta4dist**, you can use the following command:

```bash
pip install beta4dist
```

Alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/soham39039820/beta4dist.git
cd beta4dist
pip install .
```

## Examples

Here are some basic examples demonstrating how to use **beta4dist** for generating samples and performing likelihood-based estimation.

### 1. **Generate Samples from the Four-Parameter Beta Distribution**

You can generate samples from the four-parameter beta distribution using the `r4beta` function:

```python
from beta4dist.distribution import r4beta

# Generate 1000 samples from a 4-parameter beta distribution
samples = r4beta(1000, 2, 3, 0.5, 0.5)
print(samples[:10])  # Print the first 10 samples
```

### 2. **Fit the Four-Parameter Beta Distribution Using Likelihood-Based Estimation**

You can fit the distribution to your data using the `LBE4beta` function:

```python
from beta4dist.beta4_model import LBE4beta

# Generate sample data
import numpy as np
samples = r4beta(1000, 2, 3, 0.5, 0.5)

# Perform likelihood-based estimation
params = LBE4beta(samples)

print("Estimated Parameters:", params)
```

### 3. **Example Test Cases**

The package also includes pre-defined tests to ensure that the model works as expected. You can run these tests using `pytest`:

```bash
pytest
```

This will execute the tests and report any issues.

## Licensing

**beta4dist** is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## References

For more information on the four-parameter beta distribution and its applications, please refer to the paper:

- **Paper Title**: "SoftwareX: Efficient Statistical Modeling with the Four-Parameter Beta Distribution"
- **Authors**: [Your Name], [Collaborators]
- **DOI**: [DOI Link]

---

For more information, bug reports, or feature requests, please open an issue or a pull request on the [GitHub repository](https://github.com/soham39039820/beta4dist).
