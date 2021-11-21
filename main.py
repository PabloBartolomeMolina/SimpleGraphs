import matplotlib.pyplot as plt
import pandas as pd
import os.path


# Save a graph given a plot and a name.
def save_graph(plot, name):
    print(f'Image name, {name}')  # Debugging line.
    plot.savefig(f'{name}.png')


# Get data from Excel file indicated in argument (including path if necessary).
# Sheet to read is passed as parameter. Value 0 as default to just read the first sheet in Excel file.
def get_data_excel(file, sheet = 0):
    # Example line, sheet_name is optional to indicate Excel sheet to read.
    # df = pd.read_excel(r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')

    # Check if file is existing.
    if os.path.isfile(file):
        df = pd.read_excel(f'{file}', sheet)
        print(df) # Print data for debugging purposes.
    else:
        # As file do not exist, create a dummy DataFrame.
        # Useful to debug. Specific implementation to manage this error, TO BE DONE.
        data = {'NUM0': [0, 0, 0, 0], 'NUM1': [1, 1, 1, 1]}
        df = pd.DataFrame(data)
    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    raw_data = get_data_excel('Classeur1.xlsx')

    # Print the plot of the data.
    ax = raw_data.plot()
    ax.set_xlabel('Index of elements')  # Add an x-label to the axes.
    ax.set_ylabel('Value of elements')  # Add a y-label to the axes.
    plt.show()
    # Get image to save it.
    plotted = raw_data.plot().get_figure()
    # Save plot image.
    save_graph(plotted, 'simplegraph1')
