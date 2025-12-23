# Plots graphs
from matplotlib import pyplot as plt
from data_storage import format_data, read_csv

# Recives the column name for the y axis

file_formated = format_data(read_csv())

def get_species():
    species = []
    for i in file_formated:
        species.append(i.get('species'))
    return species

def get_y(y):
    values = []
    for i in file_formated:
        values.append(i.get(str(y)))
    return values

def plot_graph(y, file_name):
    file_name = f'{file_name}.png'
    x = get_species()
    # Using comprehension to transform from string to float
    y_values = [float(n) for n in get_y(y)]
    #Uses figure to pyplot creates a new chart and not uses the old one
    figure = plt.figure()
    #using alpha to better view of the points
    plt.scatter(x,y_values, alpha=0.5)
    figure.savefig(file_name)

