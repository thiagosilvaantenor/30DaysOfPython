# 3. Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up
# the shop at night. This means that for employees A, B, and C, employee A will close the shop on day 1,
# then B will close the shop on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.

# Write a program to create a schedule that lists which of your employees will lock up 
# the shop on a given day over a 30 day period. You should list the day number, 
# the employee name, and the day of the week. 
# You can choose any employee to lock the shop on day 1, and you can also choose 
# which day of the week day 1 corresponds to.

# You should make use of the cycle function 
# in the itertools module to create a repeating series of values. 
# You can find documentation here.

import itertools

def employee_scheduler(employees:list, limit:int):
    # D1=Sunday, D2=Monday, ..., D7=Saturday
    days_week = itertools.cycle(("Sunday", "Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday"))
    schedule_list = itertools.cycle(employees)
    output = ''

    for day_number in range(1,31):
        
        output = f'On the {next(days_week)}, {day_number}th of the month\nThe employee: {next(schedule_list)} will close the shop'

        if day_number == limit:
            return output
        

            
print(employee_scheduler(['A','B','C'], 30))







# # String for sequence generation
# Inputstring ='Geeks';

# # Calling the function Cycle from
# # itertools and passing string as 
# #an argument and the function returns
# # the iterator object
# StringBuffer = itertools.cycle(Inputstring)
# SequenceRepeation = 0
# SequenceStart = 0
# SequenceEnd = len(Inputstring)

# for output in StringBuffer:
#     if(SequenceStart == 0):
#         print('Sequence %d'%(SequenceRepeation + 1))

#     # Cycle function iterates through each
#     # element and produces the sequence 
#     # and repeats it the sequence
#     print(output, end =' ')

#     # Checks the End of the Sequence according 
#     # to the given input argument
#     if(SequenceStart == SequenceEnd-1):
        
#         if(SequenceRepeation >= 2):
#             break
#         else:
#             SequenceRepeation+= 1
#             SequenceStart = 0
#             print('\n')
#     else:
#         SequenceStart+= 1