@echo off
@REM echo Generating large input...
@REM python D:\code\mpi_wordCounter\scripts\generate_large_input.py

echo Running with small input...
mpiexec -n 4 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\input.txt

echo Running with large input...
mpiexec -n 8 python D:\code\mpi_wordCounter\src\main.py D:\code\mpi_wordCounter\data\large_input.txt

echo Generating visualizations...
python D:\code\mpi_wordCounter\scripts\plot_results.py
python D:\code\mpi_wordCounter\scripts\visualize_mpi.py

echo Done!
pause