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
                    if len(parts) >= 4:
                        rank = int(parts[1].strip(':'))
                        count = int(parts[3])
                        word_counts.append((rank, count))
    return word_counts

def plot_word_frequencies():
    words = []
    counts = []
    
    # Read word frequencies
    freq_file = 'results/word_frequencies.txt'
    if not os.path.exists(freq_file):
        print(f"Frequency file {freq_file} not found.")
        return
    
    with open(freq_file, 'r', encoding='utf-8') as f:
        for line in f:
            word, count = line.strip().split()
            words.append(word)
            counts.append(int(count))
    
    # Get top 5 and top 10 words
    indices = np.argsort(counts)[-10:][::-1]
    top10_words = [words[i] for i in indices]
    top10_counts = [counts[i] for i in indices]
    top5_words = top10_words[:5]
    top5_counts = top10_counts[:5]
    
    # Read worker contributions
    word_counts = read_worker_logs('results/worker_logs.txt')
    
    # Create three-subplot figure
    plt.figure(figsize=(12, 12))
    
    # Plot top 5 words
    plt.subplot(3, 1, 1)
    plt.bar(top5_words, top5_counts, color='skyblue')
    plt.title('Top 5 Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    
    # Plot top 10 words
    plt.subplot(3, 1, 2)
    plt.bar(top10_words, top10_counts, color='lightgreen')
    plt.title('Top 10 Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    
    # Plot worker contributions
    if word_counts:
        ranks = [rank for rank, _ in word_counts]
        counts = [count for _, count in word_counts]
        plt.subplot(3, 1, 3)
        plt.bar(ranks, counts, color='salmon')
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