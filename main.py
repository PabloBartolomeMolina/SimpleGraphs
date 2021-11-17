import matplotlib.pyplot as plt
import numpy as np


def save_graph(plt, name):
    print(f'Image name, {name}')  # Debugging line.
    plt.savefig(f'{name}.png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
