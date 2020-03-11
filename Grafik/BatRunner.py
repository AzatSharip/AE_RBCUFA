import subprocess

program = "D:/Personal/GitHub/AE/Grafik/Make_grf.bat"
process = subprocess.Popen(program)
exit_code = process.wait()

if exit_code == 0:
    print("Success!")
else:
    print("Error!")