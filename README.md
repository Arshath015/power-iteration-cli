# Power Iteration CLI Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

Estimate the dominant eigenvalue of a dense matrix from the command line.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Theoretical Background](#theoretical-background)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Analysis Document](#analysis-document)
- [Testing](#testing)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)

## Overview
`power-iteration-cli` provides a tiny but rigorous implementation of the power iteration algorithm. It accepts a matrix via a CSV file, runs a configurable number of iterations, and writes the dominant eigenvalue and eigenvector to `results/`.

## Tech Stack
- Python 3.9+
- NumPy for numerical linear algebra

## Architecture
```text
cli.py
 └─ argparse parses CLI args
    └─ core.iteration.run_power_iteration(matrix, max_iter, tol)
        └─ core.utils.read_matrix(csv_path)
        └─ core.utils.normalize(vector)
    └─ core.utils.write_results(value, vector, out_dir)
```

## Theoretical Background
The power iteration method converges to the eigenpair (λ₁, v₁) associated with the eigenvalue of largest magnitude for a matrix **A** provided that:
1. **A** has a dominant eigenvalue λ₁ such that |λ₁| > |λ₂| for all other eigenvalues λ₂.
2. The initial vector has a non‑zero component in the direction of v₁.

At each iteration the algorithm computes **w** = **A**·**v**, then normalizes **w** to obtain the next approximation of the eigenvector. The Rayleigh quotient r = (**v**ᵀ·**A**·**v**) / (**v**ᵀ·**v**) provides an estimate of the dominant eigenvalue. Convergence is geometric with ratio |λ₂/λ₁|, making the method fast for well‑conditioned problems.

## Installation
```bash
git clone https://github.com/yourorg/power-iteration-cli.git
cd power-iteration-cli
pip install -r requirements.txt
```

## Usage
```bash
python cli.py --matrix data/matrix.csv --iterations 1000 --tolerance 1e-8 --output results/
```
The command reads `data/matrix.csv`, runs the iteration, and writes `eigenvalue.txt` and `eigenvector.txt` in the specified output directory.

## API Reference
- `core.iteration.run_power_iteration(matrix: np.ndarray, max_iter: int = 1000, tol: float = 1e-8) -> Tuple[float, np.ndarray]`
- `core.utils.read_matrix(path: str) -> np.ndarray`
- `core.utils.normalize(vec: np.ndarray) -> np.ndarray`
- `core.utils.write_results(value: float, vector: np.ndarray, out_dir: str) -> None`

## Analysis Document
See [docs/analysis.md](docs/analysis.md) for a benchmark comparing iteration counts vs tolerance on a sample matrix.

## Testing
Run the test suite with:
```bash
pytest -q
```

## Limitations
- Works only with real‑valued dense matrices loaded from CSV.
- Convergence may fail if the matrix lacks a dominant eigenvalue or is ill‑conditioned.

## Roadmap
- Add support for sparse matrices via SciPy.
- Provide a JSON output mode.
- Implement shift‑invert acceleration.

## License
MIT License
