#!/usr/bin/env python3
# Plotting graphs using matplotlib:
# 
#     Create a scatter plot where the x axis is the species and the y axis is one of the other columns.
#     Via a user menu, tell us the column they would like to plot in the y axis.
#     Also via the menu, tell us the name of the file they would like to create to contain the final plot image.
# to use the import bellow you need to install matplotlib
# pip install matplotlib
from matplotlib import pyplot as plt

menu = input("""Hello!, please select the a option:

- 1. Plot a graph.
- 2. Exit.\n""")

plot_menu = "Enter the column you want to plot: "

