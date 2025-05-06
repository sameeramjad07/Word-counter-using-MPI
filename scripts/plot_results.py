import matplotlib.pyplot as plt
import numpy as np
import os

def read_worker_logs(log_file):
    word_counts = []
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                if "Processed" in line:
                    parts = line.split()
                    rank = int(parts[1].strip(':'))
                    count = int(parts[3])
                    word_counts.append((rank, count))
    return word_counts

def plot_word_frequencies():
    words = []
    counts = []
    
    with open('results/word_frequencies.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word, count = line.strip().split()
            words.append(word)
            counts.append(int(count))
    
    # Take top 10 words
    indices = np.argsort(counts)[-10:][::-1]
    top_words = [words[i] for i in indices]
    top_counts = [counts[i] for i in indices]
    
    # Plot word frequencies
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.bar(top_words, top_counts)
    plt.title('Top 10 Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    
    # Plot worker contributions
    word_counts = read_worker_logs('results/worker_logs.txt')
    if word_counts:
        ranks = [rank for rank, _ in word_counts]
        counts = [count for _, count in word_counts]
        plt.subplot(2, 1, 2)
        plt.bar(ranks, counts)
        plt.title('Words Processed per Worker')
        plt.xlabel('Process Rank')
        plt.ylabel('Words Processed')
        plt.xticks(ranks)
    
    plt.tight_layout()
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/frequency_plot.png')
    plt.close()

if __name__ == '__main__':
    plot_word_frequencies()