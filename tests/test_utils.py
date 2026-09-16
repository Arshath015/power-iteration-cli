import numpy as np
import os
import tempfile
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.utils import read_matrix, normalize, write_results

def test_read_matrix_success():
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
        tmp.write('1,2,3\n4,5,6\n7,8,9')
        tmp_path = tmp.name
    mat = read_matrix(tmp_path)
    os.unlink(tmp_path)
    assert mat.shape == (3, 3)
    assert np.allclose(mat[0, 0], 1)

def test_normalize_zero_vector():
    try:
        normalize(np.zeros(3))
    except ValueError as e:
        assert 'Zero vector' in str(e)
    else:
        assert False, 'Expected ValueError'

def test_write_results_creates_files():
    with tempfile.TemporaryDirectory() as td:
        write_results(3.14, np.array([1.0, 0.0, 0.0]), td)
        ev_path = os.path.join(td, 'eigenvalue.txt')
        vec_path = os.path.join(td, 'eigenvector.txt')
        assert os.path.isfile(ev_path)
        assert os.path.isfile(vec_path)
        with open(ev_path) as f:
            val = float(f.read().strip())
        assert abs(val - 3.14) < 1e-12
