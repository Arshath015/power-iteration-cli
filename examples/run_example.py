"""Example usage of power-iteration-cli."""
import os
import subprocess

os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

with open("data/matrix.csv", "w") as f:
    f.write("4,1,2\n1,3,0\n2,0,5\n")

subprocess.run([
    "python", "cli.py",
    "--matrix", "data/matrix.csv",
    "--iterations", "2000",
    "--tolerance", "1e-9",
    "--output", "results"
], check=True)

with open("results/eigenvalue.txt") as f:
    print(f.read())
with open("results/eigenvector.txt") as f:
    print(f.read())
