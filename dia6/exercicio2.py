#!/bin/python3
# exercicio2

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
# 2) For the employees above, print out those who are earning an hourly wage above average.

#Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

average = 0


for em in employees :
    average = average + em[2]

average = average / float(len(employees))

print("Employees who's wage is above average: ")
for em in employees :
    if( em[2] > average ) :
        print(f'The employee: {em[0]}, who worked: {em[1]} this week and has a hourly wage of US$ {em[2]}')