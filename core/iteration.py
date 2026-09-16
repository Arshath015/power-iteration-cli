import numpy as np
from typing import Tuple
from .utils import normalize

def run_power_iteration(matrix: np.ndarray, max_iter: int = 1000, tol: float = 1e-8) -> Tuple[float, np.ndarray]:
    """Estimate the dominant eigenvalue and eigenvector of *matrix*.

    Parameters
    ----------
    matrix: np.ndarray
        Square real matrix.
    max_iter: int, optional
        Upper bound on iteration count.
    tol: float, optional
        Relative change tolerance for the eigenvalue estimate.

    Returns
    -------
    eigenvalue: float
        Approximated dominant eigenvalue.
    eigenvector: np.ndarray
        Corresponding eigenvector (unit norm).
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError('Matrix must be square')
    n = matrix.shape[0]
    # Start with a random non‑zero vector
    b_k = np.random.rand(n)
    b_k = normalize(b_k)
    eigenvalue_old = 0.0
    for i in range(max_iter):
        # Multiply by matrix
        b_k1 = matrix @ b_k
        # Normalize
        b_k1 = normalize(b_k1)
        # Rayleigh quotient for eigenvalue estimate
        eigenvalue = float(b_k1.T @ matrix @ b_k1)
        # Check convergence
        if np.abs(eigenvalue - eigenvalue_old) <= tol * np.abs(eigenvalue_old if eigenvalue_old != 0 else 1):
            return eigenvalue, b_k1
        b_k = b_k1
        eigenvalue_old = eigenvalue
    # Return last iterate if max_iter reached
    return eigenvalue, b_k
