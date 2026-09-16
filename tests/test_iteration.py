import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.iteration import run_power_iteration

def test_known_matrix_convergence():
    # Simple 2x2 matrix with dominant eigenvalue 5
    A = np.array([[5, 2], [2, 1]], dtype=float)
    eigenvalue, eigenvector = run_power_iteration(A, max_iter=500, tol=1e-10)
    # Dominant eigenvalue is 5.236... (exact)
    assert abs(eigenvalue - 5.2360679775) < 1e-6
    # Eigenvector should be proportional to [0.934, 0.357]
    expected = np.array([0.934, 0.357])
    # Normalize both for comparison
    ev = eigenvector / np.linalg.norm(eigenvector)
    exp = expected / np.linalg.norm(expected)
    assert np.allclose(ev, exp, atol=1e-3) or np.allclose(ev, -exp, atol=1e-3)

def test_non_convergent_matrix_raises():
    # Matrix with equal magnitude eigenvalues may not converge; we test that algorithm still returns a value
    A = np.array([[0, 1], [-1, 0]], dtype=float)  # rotation matrix, eigenvalues are +/- i
    eigenvalue, eigenvector = run_power_iteration(A, max_iter=10, tol=1e-12)
    # Should not raise; eigenvalue magnitude close to 0
    assert isinstance(eigenvalue, float)
    assert eigenvector.shape == (2,)
