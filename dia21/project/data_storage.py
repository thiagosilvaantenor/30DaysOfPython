# Reads the csv file

def read_csv():
    with open("/home/thiagoos/Downloads/30DaysOfPython/dia22/project/iris.csv", 'r') as file:
        data = file.readlines()
    return data

def format_data(data):
    # transform in to a list
    headers = data[0].strip().split(',')
    list_data = []
    # transforms into a dictionary with the headers
    for row in data[1:]:
        csv = row.strip().split(',')
        csv_dict = dict(zip(headers,csv))
        list_data.append(csv_dict)
    return list_data

