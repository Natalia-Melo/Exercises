import numpy as np
import re

list_num = np.linspace(1,300,num=300)

cases = {3 : 'Fizz', 5: 'Buzz', 7: 'Bang', 11: 'Bong', 13: 'Fezz',17 : ''}

def change_list(initial_list,  dictionary):
    list_num2: list[str] = ([str(x) for x in initial_list])
    p = [0] * len(initial_list)
    conditions = input_cases() # receive input from user

    for [index, value] in enumerate(conditions):
        check = [int(i-1) for i in initial_list if (i%value==0)]

        for i in check:
            if p[i] == 0:
                # Remove number and introduce first dictionary string
                del list_num2[i]
                list_num2.insert(i,dictionary[value])
                p[i] = 1

            else:
                if value != 13:
                    list_num2[i] += dictionary[value]

                    if value == 11:
                        str1 = list_num2[i]
                        list_num2[i] = str1[-4:]
                else:
                    list_num2[i]=re.sub('B',list_num2[i],dictionary[value]+'B',count = 1)

                if value == 17:
                    list_num2[i] = reverse_function(list_num2[i])

    print(list_num2)
    return list_num2


def reverse_function(string):
    str1 = string[0:4]
    str2 = string[-4:]

    return str2 + string[5:-5] + str1



def input_cases():
    num_of_inputs = int(input("Please input the number of cases to be analysed:"))
    input_list = list()
    for i in range(num_of_inputs):
        input_value = input("Enter value {}:".format(i + 1))
        input_list.append(float(input_value))
    return sorted(input_list)

# Run the code
num=change_list(list_num,cases)
