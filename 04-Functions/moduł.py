###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed

import keyboard # your own defined module
answer = ''
# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')

is_salary_hidden = keyboard.input_string('Hide salary? (y/n): ').strip().lower()
hide_input = is_salary_hidden == 'y'

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last Name:', last_name)
print('Age:', age)
if hide_input == False:
    print('Salary:', salary)
else:
    print('Salary: <hidden>')