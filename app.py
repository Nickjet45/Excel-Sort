import pandas as pd

import os

from pandas.io import excel

def find_file():

    #States the files found in the local directory of the program
    print("These files were discovered in the local directory: ")
    i = 1
    for files in os.listdir():
        
        print(str(i) + ": "+ files)
        i += 1
    
    print("If the file you wish to sort is not in the current directory, please input it's path, else input the file")

    filename = input("What is the file name/its path? ")

    #Checks to see if the user has appended .xlsx already, if not do it for them
    if('.xlsx' not in filename):
        filename += '.xlsx'

    #After retrieving the file name from the user, return it
    return filename

#Asks the user for the column they wish to sort the file by

def determineColumn(excel):
    i = 1

    print("These columns were detected: ")
    for columns in excel.columns:

        print(str(i) + ": " + columns)
        i += 1
    
    #Has the user enter the name to sort by
    #TODO Add option to input the number in the column, rather than the name of the column
    column = input("Which column would you like to sort by? Enter the name of the colum: ")

    return column

def main():
    excel_file = find_file()
    
    excel = pd.read_excel(excel_file)

    columnToSort = determineColumn(excel)

if __name__ == '__main__':
    main()