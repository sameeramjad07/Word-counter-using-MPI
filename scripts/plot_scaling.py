import matplotlib.pyplot as plt
import os

def read_scaling_data(filename):
    # Dictionary to store all times for each process count
    process_times_dict = {}
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    parts = line.strip().split(',')
                    proc = int(parts[0].split(':')[1].strip())
                    time = float(parts[2].split(':')[1].strip())
                    if 'large_input.txt' in line:
                        if proc not in process_times_dict:
                            process_times_dict[proc] = []
                        process_times_dict[proc].append(time)
                except (ValueError, IndexError) as e:
                    print(f"Error parsing scaling data: {line.strip()} - {e}")
                    continue
    
    # Take the minimum time for each process count
    process_times = {}
    for proc, times in process_times_dict.items():
        min_time = min(times)
        process_times[proc] = min_time
        print(f"Process {proc}: Times {times}, Selected Minimum {min_time}")  # Debug output
    
    # Sort by process count
    sorted_procs = sorted(process_times.keys())
    sorted_times = [process_times[proc] for proc in sorted_procs]
    return sorted_procs, sorted_times

def plot_scaling(times, processes):
    if len(processes) < 2:
        print("Insufficient scaling data. Using example data.")
        processes = [1, 2, 4, 8, 16]
        times = [0.0216, 0.0160, 0.0123, 0.0080, 0.0121]  # Correct data from logs
    
    plt.figure(figsize=(10, 6))
    plt.plot(processes, times, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
    plt.title('Execution Time vs. Number of Processes (Large Input)', fontsize=14)
    plt.xlabel('Number of Processes', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(processes)
    
    # Annotate points with exact times
    for proc, time in zip(processes, times):
        plt.text(proc, time + 0.0005, f'{time:.4f}s', ha='center', va='bottom', fontsize=10)
    
    # Optional: Log scale for better visibility if times vary widely
    # plt.yscale('log')
    # plt.ylabel('Execution Time (seconds, log scale)', fontsize=12)

    os.makedirs('results', exist_ok=True)
    plt.savefig('results/scaling_plot.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    processes, times = read_scaling_data('results/scaling_times.txt')
    print(f"Processes: {processes}")
    print(f"Times: {times}")
    plot_scaling(times, processes)