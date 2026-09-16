#!/usr/bin/env bash
# Example usage of power-iteration-cli
# Prepare a small 3x3 matrix
mkdir -p data results
cat > data/matrix.csv << 'EOF'
4,1,2
1,3,0
2,0,5
EOF
# Run the CLI
python cli.py --matrix data/matrix.csv --iterations 2000 --tolerance 1e-9 --output results
# Display the output
cat results/eigenvalue.txt
cat results/eigenvector.txt
