import matplotlib.pyplot as plt

def open_file(filename):
    x = 0
    names_list = []
    with open(filename) as file:
        for row in file:
            row = row.split()
            x += 1
            if x != 1:
                names_list.append(row[0])
    return names_list




def make_percent(names):
    letters_percent = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}


    total_names = 0

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

    # print(letters_percent)
    return(letters_percent)


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

    plt.title('Boys Names and Girls names \n LEGEND: Boys Names = Blue, Girls names = Red')

    plt.plot(keys_b, vals_b, '-b')
    plt.plot(keys_g, vals_g, '-r')


    plt.show()




def boy_stats(boys_names, girls_names, check = 0):

    name_total = 0

    tot_def = 0
    tot_inc = 0
    tot_cor = 0

    TP = 0
    FP = 0

    TN = 0
    FN = 0

    comp_girls = []
    comp_boys = []

    girl_endings = ['a', 'e', 'i']
    boy_endings = ['l', 'n', 'r', 's', 't']


    if check == 0:
#### ASSAIGN EACH NAME TO COMP GENERATED LIST OF NAMES
        for name in boys_names:
            name_total += 1

            end = name[-1].lower()

            if end in girl_endings:
                # print(f'GIRL: {name}')
                comp_girls.append(name)

            elif end in boy_endings:
                # print(f'BOY: {name}')
                comp_boys.append(name)

            else:
                tot_def += 1

        # for name in girls_names:



    ########### SEE IF EACH NAME IS CORRECT OR INCORRECT FOR BOYS
        for name in comp_boys:

            if name in boys_names:
                tot_cor += 1
                FP += 1

            if name in girls_names:
                tot_inc += 1
                TP += 1


    ############ SEE IF EACH NAME IS CORRECT OR INCORRECT FOR GIRLS
        for name in comp_girls:
            if name in girls_names:
                tot_cor += 1
                FN += 1

            if name in boys_names:
                tot_inc += 1
                TN += 1

        print(TN, FP)
        print(FN, TP)
        print(tot_cor, tot_inc)
        print('---------')


    # CALCULATE PCC, PM, and PD

    else:
        for name in girls_names:
            name_total += 1

            end = name[-1].lower()

            if end in girl_endings:
                # print(f'GIRL: {name}')
                comp_girls.append(name)

            elif end in boy_endings:
                # print(f'BOY: {name}')
                comp_boys.append(name)

            else:

                tot_def += 1



        ########### SEE IF EACH NAME IS CORRECT OR INCORRECT FOR BOYS
        for name in comp_girls:

            if name in girls_names:
                tot_cor += 1
                TP += 1

            if name in boys_names:
                tot_inc += 1
                FP += 1

        ############ SEE IF EACH NAME IS CORRECT OR INCORRECT FOR GIRLS
        for name in comp_boys:
            if name in boys_names:
                tot_cor += 1
                FN += 1

            if name in girls_names:
                tot_inc += 1
                TN += 1

        print(TP, FN)
        print(FP, TN)
        print(tot_cor, tot_inc)


    PCC = ((tot_cor) / (name_total - tot_def))

    PM = ((tot_inc) / (name_total - tot_def))

    PD = ((tot_def) / (name_total))


# CALCULATE PRECISION, RECALL, and F-SCORE

    precision = TP/(TP + FP)

    recall = TP/(TP + FN)

    Fscore = (2 * precision * recall) / (precision + recall)


    # print(FN, TN, TP, FP)
    # print(PCC, PM, PD)






def main(filename1, filename2):
    boys_names = open_file(filename1)
    girls_names = open_file(filename2)

    boy_percent = make_percent(boys_names)
    girl_percent = make_percent(girls_names)

    boy_stats(boys_names, girls_names)
    boy_stats(boys_names, girls_names, 1)

    graph_data(boy_percent, girl_percent)


main('Jacob Kahn - female_names.txt', 'Jacob Kahn - male_names.txt')

