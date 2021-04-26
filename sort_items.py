import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        radek = []
        for row in reader:
            for x in row:
                radek.append(int(x))
            break
    return radek

def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """


def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    for x in range(len(number_array[:-1])):
        lowest = x
        for n in range(x + 1, len(number_array)):
            if direction == "ascending":
                if number_array[n] < number_array[lowest]:
                    lowest = n
            elif direction == "descending":
                if number_array[n] > number_array[lowest]:
                    lowest = n
        number_array[x], number_array[lowest] = number_array[lowest], number_array[x]
    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """


def main():
    row = read_row("numbers_one.csv")
    number_array = selection_sort(row)
    print(number_array)
    number_array = selection_sort(row, "descending")
    print(number_array)
    # Ukol: Selection Sort


    # Ukol: Selection Sort - se smerem razeni
    

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

