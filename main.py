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
        total_names += 1
        end = name[-1].lower()

        for key in letters_percent:

            if end == key:
                letters_percent[key] += 1



    for key in letters_percent:
        letters_percent[key] /= total_names

        # percent = round(letters_percent[key], 2)

        # print(percent)

    # print(total_names)
    # print(letters_percent)

    return(letters_percent)



boys_names = open_file('Jacob Kahn - male_names.txt')
girls_names = open_file('Jacob Kahn - female_names.txt')

make_percent(boys_names)
make_percent(girls_names)
