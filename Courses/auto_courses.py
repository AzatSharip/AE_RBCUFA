import courses
import best_courses
import subprocess
import os
import datetime


def write_data():
    with open("data.txt", 'w') as file:
        file.write('var comp1 = ["на {}","{}","{}","{}","{}"];'.format(courses.date, courses.doll_val, courses.doll_dynamics, courses.euro_val, courses.euro_dynamics) + '\n')
        file.write('var doll_minus = ["{}"];\nvar euro_minus = ["{}"];'.format(courses.doll_dynamics_arrow, courses.euro_dynamics_arrow) + '\n')
        file.write('var comp_doll = ["{}","{}","{}","{}"];'.format(best_courses.doll_buy, best_courses.doll_buy_b, best_courses.doll_sale, best_courses.doll_sale_b) + '\n')
        file.write('var comp_euro = ["{}","{}","{}","{}"];'.format(best_courses.euro_buy, best_courses.euro_buy_b, best_courses.euro_sale, best_courses.euro_sale_b) + '\n')

def write_prop_to_bat():
    with open("run.bat", 'w') as file:
        today = datetime.datetime.today()
        year = today.strftime("%Y")
        month = today.strftime("%m")

        day = today.strftime("%d")
        # print(bin_name)

        path_to_courses = ('O:\Графика на эфир\{}\март\{}'.format(year, day))

        file.write('chcp 1251\n"C:\Program Files\Adobe\Adobe After Effects CC 2018\Support Files\\aerender.exe" -project D:\Personal\GitHub\AE\Courses\get_courses.aep -comp KURSI -OMtemplate KURSI -output D:\Personal\GitHub\AE\Courses\\render\KURSI_[#####].png')





def bat_run():
    program = "run.bat"
    process = subprocess.Popen(program)
    exit_code = process.wait()

    if exit_code == 0:
        print("Success!")
    else:
        print("Error!")




write_data()
print('Data.txt recorded successfully!')
write_prop_to_bat()
bat_run()