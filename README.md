# 🚀 Parallel Word Count Project

This project implements a **parallel word frequency counter** using **MPI (Message Passing Interface)**. It distributes a text file across multiple processes, counts word frequencies in parallel, and aggregates the results to display the top 5 most frequent words.

---

## 📁 Project Structure

```text
parallel_word_count/
├── src/
│   ├── main.c                  # Main program
│   ├── word_count.h/.c         # Word counting logic
│   ├── utils.h/.c              # Utility functions
│   └── visualization.c         # Visualization functions
├── data/
│   ├── input.txt               # Sample small input
│   └── large_input.txt         # Generated large input
├── scripts/
│   ├── run.sh                  # Execution script
│   ├── plot_results.py         # Visualization script
│   └── generate_large_input.py # Large input generator
├── results/
│   ├── word_frequencies.txt    # Word frequency results
│   └── frequency_plot.png      # Visualization plot
├── configs/
│   ├── config_small.ini        # Small input config
│   └── config_large.ini        # Large input config
├── Makefile                    # Build automation
└── README.md                   # This file
```

---

## ✅ Prerequisites

- MPI implementation (e.g., MPICH or OpenMPI)
- GCC compiler
- Python 3 with:

  - `matplotlib`
  - `numpy`

- `make`

---

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/sameeramjad07/Word-counter-using-MPI.git
cd Word-counter-using-MPI
```

### Install Dependencies (Ubuntu example)

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Generate a Large Input File

```bash
python scripts/generate_large_input.py
```

### Run the Experiments

```bash
bash scripts/run.sh
```

This script will:

- Compile the program
- Run with small input (4 processes)
- Run with large input (8 processes)
- Generate visualization

---

## ⚙️ Configuration

- `configs/config_small.ini`: Configuration for small input
- `configs/config_large.ini`: Configuration for large input

You can modify these files to change:

- Number of processes
- Input/output file paths
- Number of top words to display

---

## 📤 Output

- Console shows top 5 words and execution time
- `results/word_frequencies.txt`: All word frequencies
- `results/frequency_plot.png`: Bar plot of top 10 words

---

## 🧪 Experiments

To run manually with a custom setup:

```bash
mpirun -np <num_processes> ./word_count <input_file>
```

Example:

```bash
mpirun -np 4 ./word_count data/input.txt
```

---

## 📊 Visualization

To regenerate the bar plot of the top 10 most frequent words:

```bash
python3 scripts/plot_results.py
```

---
