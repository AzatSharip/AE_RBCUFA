import courses
import best_courses



def write_data():
    with open("data.txt", 'w') as file:
        file.write('var comp1 = ["на {}","{}","{}","{}","{}"];'.format(courses.date, courses.doll_val, courses.doll_dynamics, courses.euro_val, courses.euro_dynamics) + '\n')
        file.write('var doll_minus = ["{}"];\nvar euro_minus = ["{}"];'.format(courses.doll_dynamics_arrow, courses.euro_dynamics_arrow) + '\n')
        file.write('var comp_doll = ["{}","{}","{}","{}"];'.format(best_courses.doll_buy, best_courses.bank_doll_buy, best_courses.doll_sale, best_courses.bank_doll_sale) + '\n')
        file.write('var comp_euro = ["{}","{}","{}","{}"];'.format(best_courses.euro_buy, best_courses.bank_euro_buy, best_courses.euro_sale, best_courses.bank_euro_sale) + '\n')
















write_data()