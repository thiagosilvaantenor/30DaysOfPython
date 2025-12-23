# Menu

from graphing import plot_graph

USER_CHOICE = """
Enter:
- '1' to select a column to be in the y axis
- 'q' to quit

Your choice: """

COLUMNS = {
    "1":"sepal_length",
    "2":"sepal_width",
    "3":"petal_length",
    "4":"petal_width",
}
    

def menu():
    op = ''
    while op != 'q':
        op = input(USER_CHOICE)
        if op == '1':
                y = get_column()
                name_file = input('Enter the name of the file, without the type: ')
                plot_graph(y,name_file.strip())
        elif op == 'q':
                break
        else:
            continue

def get_column():
    options = []
    for i,j in COLUMNS.items():
        options.append(f'{i.strip()} - {j.strip()}')
    column = input(options)
    return COLUMNS.get(column)

menu()

