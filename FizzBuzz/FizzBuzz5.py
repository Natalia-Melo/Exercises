import numpy as np

cases = {3 : 'Fizz', 5: 'Buzz', 7: 'Bang', 11: 'Bong', 13: 'Fezz',17 : ''}


def processNumber(i,rules):
    output_list = []

    if i%3 == 0 and '3' in rules:
        output_list.append('Fizz')
    if i%5 == 0 and '5' in rules:
        output_list.append('Buzz')
    if i%7 == 0 and '7' in rules:
        output_list.append('Bang')
    if i%11 == 0 and '11' in rules:
        output_list.clear()
        output_list.append('Bong')
    if i%13 == 0 and '13' in rules:
        output_list.append('Fezz')
        output_list.sort(reverse = True)
    if i%17 == 0 and '17' in rules:
        output_list.reverse()

    if len(output_list) > 0:
        return "".join(output_list)
    else:
        return i


max_num = input('Please input the maximum number: ')

n = input('Please enter the number of rules: ')

rules = []
for i in range(int(n)):
    rules.append(input('Please input rule number: '))

rule = set(rules)

final_list = []
for number in range(1, int(max_num)):
    final_list.append(processNumber(number,rules))

print(final_list)