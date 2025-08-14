#!/bin/python3
# exercicio4

#4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
print('Exercise 4')
# Recebe o input das horas e valor hora
name = input("Hello! Please enter the employee's name: ")
hours = int(input('Please, enter the number of hours of work of this employee on this week:'))
hourly_wage = float(input('Now enter the hourly wage of the employee: '))

if (hours > 40) :
    normal_wage = 40 * hourly_wage
    additionalOver = (hours - 40) * hourly_wage * 1.1
    total = round(normal_wage + additionalOver, 2)
    print(f'This employee ({name}) is due some additional play: {total}')
else :
    wage = round(hours * hourlyWage,2)
    print(f"This employee ({name}) dosen't have any overtime: {wage} ")
