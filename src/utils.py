import os
from mpi4py import MPI

def get_file_size(filename):
    """Get the size of a file in bytes."""
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return 0

def read_and_scatter_file(filename, chunk_size, comm, rank, size):
    """Read file and scatter chunks to all processes."""
    data = None
    if rank == 0:
        try:
            with open(filename, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            print(f"Error: File {filename} not found")
            MPI.Finalize()
            exit(1)

    # Scatter data
    chunk = bytearray(chunk_size)
    comm.Scatter([data, chunk_size, MPI.BYTE] if rank == 0 else None, chunk, root=0)
    return chunk