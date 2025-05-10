@echo off
@REM echo Generating large input...
@REM python D:\code\mpi_wordCounter\scripts\generate_large_input.py

@REM echo Clearing previous scaling data...
@REM del D:\code\mpi_wordCounter\results\scaling_times.txt

echo Running with small input...
mpiexec -n 4 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\input.txt

echo Running with large input...
mpiexec -n 8 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt

echo Running scaling tests...
mpiexec -n 1 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt
mpiexec -n 2 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt
mpiexec -n 4 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt
mpiexec -n 8 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt
mpiexec -n 16 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt

echo Generating visualizations...
python D:\code\mpi_wordCounter\scripts\plot_results.py
python D:\code\mpi_wordCounter\scripts\visualize_mpi.py
python D:\code\mpi_wordCounter\scripts\plot_scaling.py

echo Done!
pause