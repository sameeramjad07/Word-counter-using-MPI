import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os

def read_worker_logs(log_file):
    """Read worker logs to extract chunk assignments and word counts."""
    chunks = []
    word_counts = []
    if not os.path.exists(log_file):
        print(f"Worker log file {log_file} not found.")
        return chunks, word_counts

    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                if "Assigned chunk" in line:
                    parts = line.split()
                    if len(parts) >= 9:  # Ensure enough parts
                        rank = int(parts[1].strip(':'))
                        start = int(parts[6])  # Correct index for start byte
                        end = int(parts[8])   # Correct index for end byte
                        chunks.append((rank, start, end))
                elif "Processed" in line:
                    parts = line.split()
                    if len(parts) >= 4:
                        rank = int(parts[1].strip(':'))
                        count = int(parts[3])
                        word_counts.append((rank, count))
            except (ValueError, IndexError) as e:
                print(f"Error parsing log line: {line.strip()} - {e}")
                continue

    return chunks, word_counts

def animate_mpi_process():
    log_file = 'results/worker_logs.txt'
    chunks, word_counts = read_worker_logs(log_file)
    if not chunks:
        print("No valid worker logs found. Animation skipped.")
        return

    num_processes = len(chunks)
    file_size = max(end for _, _, end in chunks)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 2]})
    plt.subplots_adjust(hspace=0.3)

    # Chunk division plot
    bars = ax1.barh(range(num_processes), [end - start for _, start, end in chunks],
                    left=[start for _, start, _ in chunks])
    ax1.set_title('MPI Chunk Division')
    ax1.set_xlabel('File Position (bytes)')
    ax1.set_ylabel('Process Rank')
    ax1.set_yticks(range(num_processes))
    ax1.set_yticklabels([f'Rank {i}' for i in range(num_processes)])

    # Worker progress plot
    progress = np.zeros(num_processes)
    progress_bars = ax2.barh(range(num_processes), progress)
    ax2.set_title('Worker Progress (Words Processed)')
    ax2.set_xlabel('Words Processed')
    ax2.set_ylabel('Process Rank')
    ax2.set_yticks(range(num_processes))
    ax2.set_yticklabels([f'Rank {i}' for i in range(num_processes)])

    def update(frame):
        # Simulate progress
        for i, bar in enumerate(progress_bars):
            if i < len(word_counts):
                max_words = word_counts[i][1]
                progress[i] = min(max_words * (frame / 50), max_words)
                bar.set_width(progress[i])
        ax2.set_xlim(0, max(max_words for _, max_words in word_counts) * 1.1)
        return progress_bars

    anim = FuncAnimation(fig, update, frames=60, interval=100, blit=True)
    os.makedirs('results', exist_ok=True)
    anim.save('results/mpi_process_animation.mp4', writer='ffmpeg')
    plt.close()

if __name__ == '__main__':
    # Ensure ffmpeg is installed (required for MP4 output)
    try:
        animate_mpi_process()
    except Exception as e:
        print(f"Error creating animation: {e}")