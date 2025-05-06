# Parallel Word Count Project

This project implements a **parallel word frequency counter** using **MPI (Message Passing Interface)**. It distributes a text file across multiple processes, counts word frequencies in parallel, and aggregates the results to display the top 5 most frequent words.

## 📁 Project Structure

```text
parallel_word_count/
├── src/                    # Source code
│   ├── main.c             # Main program
│   ├── word_count.h       # Word counting header
│   ├── word_count.c       # Word counting implementation
│   ├── utils.h            # Utility functions header
│   ├── utils.c            # Utility functions implementation
│   └── visualization.c    # Visualization functions
├── data/                   # Input files
│   ├── input.txt          # Sample small input
│   └── large_input.txt    # Generated large input
├── scripts/                # Helper scripts
│   ├── run.sh             # Execution script
│   ├── plot_results.py    # Visualization script
│   └── generate_large_input.py  # Large input generator
├── results/                # Output files
│   ├── word_frequencies.txt  # Word frequency results
│   └── frequency_plot.png   # Visualization plot
├── configs/                # Configuration files
│   ├── config_small.ini    # Small input config
│   └── config_large.ini    # Large input config
├── Makefile                # Build automation
└── README.md               # This file
```

---

## ✅ Prerequisites

- MPI implementation (e.g., MPICH or OpenMPI)
- GCC compiler
- Python 3 with `matplotlib` and `numpy`
- `make`

---

## 🔧 Installation

Clone the repository:

```bash
git clone <repository_url>
cd parallel_word_count





Install dependencies (Ubuntu example):

sudo apt-get install mpich gcc python3 python3-matplotlib python3-numpy make

Building the Project

make

Running the Project





Generate large input file:

python3 scripts/generate_large_input.py





Run the experiments:

bash scripts/run.sh

This will:





Compile the program



Run with small input (4 processes)



Run with large input (8 processes)



Generate visualization

Configuration





configs/config_small.ini: Configuration for small input



configs/config_large.ini: Configuration for large input

Modify these files to change:





Number of processes



Input/output files



Number of top words to display

Output





Console output shows top 5 words and execution time



results/word_frequencies.txt: All word frequencies



results/frequency_plot.png: Bar plot of top 10 words

Experiments

To run with different configurations:

mpirun -np <num_processes> ./word_count <input_file>

Example:

mpirun -np 4 ./word_count data/input.txt

Visualization

The plot_results.py script generates a bar plot of the top 10 most frequent words. To regenerate:

python3 scripts/plot_results.py

Cleaning Up

make clean

Troubleshooting





Ensure MPI is properly installed and configured



Check file permissions for input/output files



Verify Python dependencies are installed



Check available memory for large inputs
```
