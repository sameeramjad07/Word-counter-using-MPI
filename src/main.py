import sys
from mpi4py import MPI
import time
from word_count import count_words, aggregate_counts, save_word_frequencies
from utils import get_file_size, read_and_scatter_file
import os

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if len(sys.argv) != 2:
        if rank == 0:
            print(f"Usage: {sys.argv[0]} <input_file>")
        MPI.Finalize()
        return

    input_file = sys.argv[1]
    start_time = MPI.Wtime()

    # Get file size
    file_size = 0
    if rank == 0:
        file_size = get_file_size(input_file)
        print(f"Input file: {input_file}, Size: {file_size} bytes")
    file_size = comm.bcast(file_size, root=0)

    # Calculate chunk size
    chunk_size = (file_size + size - 1) // size
    if rank == 0:
        print(f"Dividing into {size} chunks, each ~{chunk_size} bytes")

    # Prepare chunk assignment log
    start_byte = rank * chunk_size
    end_byte = min((rank + 1) * chunk_size, file_size)
    log_message = f"Rank {rank}: Assigned chunk from byte {start_byte} to {end_byte}\n"

    # Read and scatter file
    chunk = read_and_scatter_file(input_file, chunk_size, comm, rank, size)

    # Count words in chunk
    local_counts = count_words(chunk.decode('utf-8', errors='ignore'))
    local_word_count = sum(local_counts.values())
    log_message += f"Rank {rank}: Processed {local_word_count} words\n"

    # Gather log messages to root
    log_messages = comm.gather(log_message, root=0)

    # Write logs and execution time (root only)
    if rank == 0:
        os.makedirs('results', exist_ok=True)
        with open('results/worker_logs.txt', 'a', encoding='utf-8') as f:
            for msg in log_messages:
                f.write(msg)
        # Log execution time for scaling (only for large input)
        end_time = MPI.Wtime()
        execution_time = end_time - start_time
        if 'large_input.txt' in input_file:
            with open('results/scaling_times.txt', 'a', encoding='utf-8') as f:
                # Check if entry exists to avoid duplicates (simplified check)
                existing = False
                with open('results/scaling_times.txt', 'r', encoding='utf-8') as f_read:
                    for line in f_read:
                        if f"Processes: {size}" in line and 'large_input.txt' in line:
                            existing = True
                            break
                if not existing:
                    f.write(f"Processes: {size}, File: {input_file}, Time: {execution_time:.4f}\n")

    # Aggregate counts
    global_counts = aggregate_counts(local_counts, comm, rank, size)

    # Output results
    if rank == 0:
        # Sort and get top 5
        sorted_counts = sorted(global_counts.items(), key=lambda x: x[1], reverse=True)
        print("\nTop 5 most frequent words:")
        for word, count in sorted_counts[:5]:
            print(f"{word}: {count}")

        # Save frequencies
        save_word_frequencies(global_counts, "results/word_frequencies.txt")

        # Timing
        print(f"\nExecution time: {execution_time:.4f} seconds")

    MPI.Finalize()

if __name__ == "__main__":
    # Ensure results directory exists
    if not os.path.exists('results'):
        os.makedirs('results')
    main()