import numpy as np
import os
from typing import Any

def read_matrix(path: str) -> np.ndarray:
    """Read a CSV file into a NumPy 2‑D array.

    The CSV must contain only numeric values, rows separated by newlines.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f'Matrix file not found: {path}')
    try:
        data = np.loadtxt(path, delimiter=',')
    except Exception as e:
        raise ValueError(f'Failed to parse matrix CSV: {e}')
    if data.ndim != 2:
        raise ValueError('Matrix must be two‑dimensional')
    return data

def normalize(vec: np.ndarray) -> np.ndarray:
    """Return *vec* scaled to unit Euclidean norm.

    Raises
    ------
    ValueError
        If the norm is zero.
    """
    norm = np.linalg.norm(vec)
    if norm == 0:
        raise ValueError('Zero vector cannot be normalized')
    return vec / norm

def write_results(value: float, vector: np.ndarray, out_dir: str) -> None:
    """Write eigenvalue and eigenvector to text files in *out_dir*.

    Files created:
    - eigenvalue.txt (single float)
    - eigenvector.txt (space‑separated components)
    """
    eigenvalue_path = os.path.join(out_dir, 'eigenvalue.txt')
    eigenvector_path = os.path.join(out_dir, 'eigenvector.txt')
    with open(eigenvalue_path, 'w') as f_val:
        f_val.write(f'{value}\n')
    np.savetxt(eigenvector_path, vector.reshape(1, -1), fmt='%.12f')
