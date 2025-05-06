from collections import defaultdict
import re
from mpi4py import MPI
import os

def count_words(text):
    """Count word frequencies in a text chunk."""
    # Convert to lowercase and split on non-word characters
    words = re.findall(r'\b\w+\b', text.lower())
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    return counts

def aggregate_counts(local_counts, comm, rank, size):
    """Aggregate word counts across all processes."""
    # Gather all local counts to root
    all_counts = comm.gather(local_counts, root=0)
    
    if rank == 0:
        global_counts = defaultdict(int)
        for counts in all_counts:
            for word, count in counts.items():
                global_counts[word] += count
        return global_counts
    return None

def save_word_frequencies(counts, filename):
    """Save word frequencies to a file."""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{word} {count}\n")