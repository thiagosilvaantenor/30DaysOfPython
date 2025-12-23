from matplotlib import pyplot as plt
# X and Y data points
x_data = [1, 2, 3, 4, 5]
y_data = [5.5, 6.4, 5.3, 4.4, 7.9]

# Create scatter plot and save as PNG
figure = plt.figure()
plt.scatter(x_data, y_data)
figure.savefig("graph.png")


y_data = [1.4, 6.9, 8.8, 3.4, 4.4]

figure = plt.figure()
plt.scatter(x_data, y_data)
#Overwrite the previous file
figure.savefig("graph.png")