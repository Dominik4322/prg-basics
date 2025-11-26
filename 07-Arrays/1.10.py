

###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
not_correct_answers = 0
for answer in test_results:
   if answer == True:
      correct_answers = correct_answers + 1

for answer in test_results:
    if answer == False:
        not_correct_answers += 1


percentage_correct = correct_answers / question_number * 100


print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers) 
print("Number of not correct answers", not_correct_answers)
print("Percentage of correct answers", percentage_correct,"%")