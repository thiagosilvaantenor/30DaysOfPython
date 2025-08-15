# open files
# my_file = open('/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/txt.txt')
# print(my_file.read())
# my_file.close()

# mode (r,w,a)
# my_file = open('/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/txt.txt', mode='a')
# my_file.write('\nNow you have two lines!')
# my_file.close()

#Context manager
# with open('/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/txt.txt', 'r') as my_file:
#     print(my_file.read())

# Working with .csv
with open('/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/iris.csv', mode='r') as my_csv:
    data_csv = my_csv.readlines()
    data = []

    for row in data_csv:
        sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    
    data.append({'sepal_length': sepal_length, 'sepal_width': sepal_width,
                 'petal_length': petal_length, 'petal_width': petal_width,
                 'species': species}
                )
    