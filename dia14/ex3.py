# 3. Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.

def csv_to_dict():
    # Creates the list of dictionaries:
    with open('/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/iris.csv', mode='r') as my_csv:
        data_csv = my_csv.readlines()
        #Store the header
        headers = data_csv[0].strip().split(',')
        # Create a list
        data = []
        for row in data_csv[1:]:
            csv = row.strip().split(',')
            csv_dict = dict(zip(headers,csv))
            data.append(csv_dict)
        
        return data


# function to transform a list of dictionaries in a csv file
def dict_to_csv(data:list):
    with open("/home/thiago/Downloads/codes/python_estudos/30DaysOfPython/dia14/assets/iris_new.csv", mode="w") as f:

        iris_headers = data[0].keys()

        # Write the headers
        for i in iris_headers:
            f.write(f'{i},')
        # Write the values
        for key in data:
            items = key.values()
            f.write('\n')
            for i in items:
                f.write(f'{i},')


#Calls the function to transform the csv in a dictionary
data = csv_to_dict()
dict_to_csv(data)