import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Save a graph given a plot and a name.
def save_graph(plt, name):
    print(f'Image name, {name}')  # Debugging line.
    plt.savefig(f'{name}.png')


# Get data from Excel file indicated in argument (including path if necessary).
def get_data_Excel(file):
    # Example line, sheet_name is optional to indicate Excel sheet to read.
    # df = pd.read_excel(r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')

    df = pd.read_excel(f'{file}')
    print(df) # Print data for debugging purposes.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_data_Excel('Classeur1.xlsx')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
