import subprocess
#
# exit_code = subprocess.call("E:/AUTO_KURSI/14-00.bat")
# if exit_code == 0:
#     print("Success!")
# else:
#     print("Error!")

program = "D:\Personal\GitHub\AE\Grafik/Make_grf.bat"
process = subprocess.Popen(program)
exit_code = process.wait()

if exit_code == 0:
    print("Success!")
else:
    print("Error!")