import courses
import best_courses2



def write_data():
    with open("data.txt", 'w') as file:
        file.write('var comp1 = ["на {}","{}","{}","{}","{}"];'.format(courses.date, courses.doll_val, courses.doll_dynamics, courses.euro_val, courses.euro_dynamics) + '\n')
        file.write('var doll_minus = ["{}"];\nvar euro_minus = ["{}"];'.format(courses.doll_dynamics_arrow, courses.euro_dynamics_arrow) + '\n')
        file.write('var comp_doll = ["{}","{}","{}","{}"];'.format(best_courses2.d_b, best_courses2.db_bank, best_courses2.d_s, best_courses2.ds_bank) + '\n')
        file.write('var comp_euro = ["{}","{}","{}","{}"];'.format(best_courses2.e_b, best_courses2.eb_bank, best_courses2.e_s, best_courses2.es_bank) + '\n')


write_data()
print('Data.txt recorded successfully!')