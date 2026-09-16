import argparse
import os
from core.iteration import run_power_iteration
from core.utils import read_matrix, write_results

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Estimate dominant eigenvalue using power iteration.'
    )
    parser.add_argument('--matrix', required=True, help='Path to CSV file containing the matrix')
    parser.add_argument('--iterations', type=int, default=1000, help='Maximum number of iterations')
    parser.add_argument('--tolerance', type=float, default=1e-8, help='Convergence tolerance')
    parser.add_argument('--output', default='results', help='Directory to write results')
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    matrix = read_matrix(args.matrix)
    eigenvalue, eigenvector = run_power_iteration(matrix, args.iterations, args.tolerance)
    os.makedirs(args.output, exist_ok=True)
    write_results(eigenvalue, eigenvector, args.output)
    print(f'Dominant eigenvalue: {eigenvalue}')
    print(f'Eigenvector written to {os.path.join(args.output, "eigenvector.txt")}')

if __name__ == '__main__':
    main()
