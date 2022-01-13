import matplotlib.pyplot as plt
import random


def open_file(filename):
    x = 0
    names_list = []
    random_names_list = []
    with open(filename) as file:
        for row in file:
            # print(row)
            row = row.split()
            row = row[0]
            names_list.append(row)


        random.shuffle(names_list)

        for name in names_list:
            x += 1
            if x <= 1000:
                random_names_list.append(name)
    print(random_names_list)
    return random_names_list



def make_percent(names, deferred = None):
    letters_percent = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}


    total_names = 0
    if deferred == None:
        for name in names:
            # print(name)
            total_names += 1
            end = name[-1].lower()
            # end = name[0].lower()


            for key in letters_percent:
                if end == key:

                    letters_percent[key] += 1

        for key in letters_percent:
            letters_percent[key] /= total_names

        return letters_percent

# DO IT FOR DEFERRED
    elif names == 0:
        for name in deferred:
            total_names += 1
            end = name[-1].lower()
            for key in letters_percent:
                if end == key:
                    letters_percent[key] += 1

        for key in letters_percent:
            letters_percent[key] /= total_names

        return(letters_percent)


# GRAPHING
def graph_data(boys, girls):

    keys_b = []
    vals_b = []

    keys_g = []
    vals_g = []


    for key, value in boys.items():
        plt.axis([0, 26, 0, 1])

        keys_b.append(key)
        vals_b.append(value)

    for key, value in girls.items():
        plt.axis([0, 26, 0, 1])

        keys_g.append(key)
        vals_g.append(value)

    plt.title('Boys Names and Girls names')

    plt.plot(keys_b, vals_b, '-b')
    plt.plot(keys_g, vals_g, '-r')

    plt.legend(['boys', 'girls'], loc='upper right')
    plt.show()



def graph_def(boy_def, girl_def):
    keys_b = []
    vals_b = []

    keys_g = []
    vals_g = []

    for key, value in boy_def.items():
        plt.axis([0, 26, 0, 1])

        keys_b.append(key)
        vals_b.append(value)

    for key, value in girl_def.items():
        plt.axis([0, 26, 0, 1])

        keys_g.append(key)
        vals_g.append(value)

    plt.title('BOY DEF AND GIRL DEF')

    # print(len(keys_b), len(keys_g))

    plt.plot(keys_b, vals_b, '-b')
    plt.plot(keys_g, vals_g, '-r')

    plt.legend(['boys', 'girls'], loc='upper right')
    plt.show()


# GET THE NUMBERS FOR THE FIRST TIME
def stats(boys_names, girls_names, option = 0):

    boy_total = 0
    girl_total = 0

    boy_def_num = 0
    girl_def_num = 0

    boy_def = []
    girl_def = []

    G_inc = 0
    G_cor = 0

    B_inc = 0
    B_cor = 0

    B_TP = 0
    B_FP = 0
    B_TN = 0
    B_FN = 0

    G_TP = 0
    G_FP = 0
    G_TN = 0
    G_FN = 0


    comp_girls = []
    comp_boys = []

    girl_endings = ['a', 'e', 'i']
    boy_endings = ['l', 'n', 'r', 's', 't']

    def_girl_endings = ['y', 'u']
    def_boy_endings = ['d', 'o']

#### ASSAIGN EACH NAME TO COMP GENERATED LIST OF NAMES
    for name in boys_names:
        boy_total += 1
        end = name[-1].lower()


        if end in boy_endings:
            comp_boys.append(name)
            B_cor += 1

            B_TP += 1
            G_TN += 1

        elif end in girl_endings:
            comp_girls.append(name)
            B_inc += 1

            B_FN += 1
            G_FP += 1

        else:
            if option == 1:
                boy_def_num += 1
                boy_def.append(name)
            else:
                if end in def_boy_endings:
                    B_cor += 1

                    B_TP += 1
                    G_TN += 1
                elif end in def_girl_endings:
                    B_inc += 1

                    B_FN += 1
                    G_FP += 1

                else:
                    boy_def_num += 1
                    boy_def.append(name)

# CALCULATE GIRL NUMBERS
    for name in girls_names:
        girl_total += 1
        end = name[-1].lower()

        if end in girl_endings:
            comp_girls.append(name)
            G_cor += 1

            G_TP += 1
            B_TN += 1

        elif end in boy_endings:
            comp_boys.append(name)
            G_inc += 1

            G_FN += 1
            B_FP += 1

        else:
            if option == 1:
                girl_def_num += 1
                girl_def.append(name)

            else:
                if end in def_girl_endings:
                    G_cor += 1

                    G_TP += 1
                    B_TN += 1
                elif end in def_boy_endings:
                    G_inc += 1

                    G_FN += 1
                    B_FP += 1
                else:
                    girl_def_num += 1
                    girl_def.append(name)


    # GRAPH DEFERRED
    if option == 1:
        boy_def_percent = make_percent(0, boy_def)
        girl_def_percent = make_percent(0, girl_def)
        graph_def(boy_def_percent, girl_def_percent)

    else:
        G_TN = B_TN
        G_TP = B_TP
        G_FN = B_FN
        G_FP = B_FP



    print('-------------- FINAL AMOUNT ---------------')

    print(f'Boys TP: {B_TP}, Girls TN: {G_TN}')
    print(f'Boys FN: {B_FN}, Girls FP: {G_FP}')

    print(f'Girls TP: {G_TP}, Boys TN: {B_TN}')
    print(f'Girls FN: {G_FN}, Boys FP: {B_FP}')

    # print(tot_cor, tot_inc)

    print(f'total_female = {girl_total}')

    print(f'total_male = {boy_total}')


    # CALCULATE PRECISION, RECALL, and F-SCORE FOR BOYS
    B_PCC = ((B_cor) / (boy_total - boy_def_num))

    B_PM = ((B_inc) / (boy_total - boy_def_num))

    B_PD = ((boy_def_num) / (boy_total))


    B_precision = B_TP/(B_TP + B_FP)

    B_recall = B_TP/(B_TP + B_FN)

    B_Fscore = (2 * B_precision * B_recall) / (B_precision + B_recall)


### CALCULATE GIRLS   CALCULATE PRECISION, RECALL, and F-SCORE FOR GIRLS

    G_PCC = ((G_cor) / (girl_total - girl_def_num))

    G_PM = ((G_inc) / (girl_total - girl_def_num))

    G_PD = ((girl_def_num) / (girl_total))



    G_precision = G_TP / (G_TP + G_FP)

    G_recall = G_TP / (G_TP + G_FN)

    G_Fscore = (2 * G_precision * G_recall) / (G_precision + G_recall)



    print(f'Boy precision: {B_precision}, Boy recall: {B_recall}, Boy FSCORE: {B_Fscore}')

    print(f'Boy PCC: {B_PCC}, Boy PM: {B_PM}, Boy PD: {B_PD}')

    print(f'Boy DEFERRED: {boy_def_num}')
    print(f'BOY INCORRECT: {B_inc}')
    print(f'BOY CORRECT: {B_cor}')

    print('---------')

    print(f'Girl precision: {G_precision}, Girl recall: {G_recall}, Girl FSCORE: {G_Fscore}')

    print(f'Girly PCC: {G_PCC}, Girl PM: {G_PM}, Girl PD: {G_PD}')

    print(f'Girl DEFERRED: {girl_def_num}')
    print(f'Girl INCORRECT: {G_inc}')
    print(f'Girl CORRECT: {G_cor}')


    # print('----------------------------------------------')
    # print(f'Girl_deferred: {girl_def}')
    # print('------------------')
    # print(f'Boy_deferred: {boy_def}')







def main(boy_filename, girl_filename):

    girls_names = open_file(girl_filename)
    boys_names = open_file(boy_filename)

    boy_percent = make_percent(boys_names)
    girl_percent = make_percent(girls_names)

    graph_data(boy_percent, girl_percent)

    stats(boys_names, girls_names, 1)
    stats(boys_names, girls_names)


main('Jacob Kahn - kaggle_boys_name.txt', 'Jacob Kahn - kaggle_female_names.txt')

