import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


def get_average(my_key: str, my_value, second_key: str):
    my_sum = 0
    my_count = 0
    for inx in range(0, len(data)):
        if data.loc[inx][my_key] == my_value:
            my_sum += data.loc[inx][second_key]
            my_count += 1
    return my_sum / my_count


try:
    filename = 'loan.csv'
    with open(filename) as file:
        data = pd.read_csv('loan.csv')
except FileNotFoundError:
    print('No Files!')

data_corr = data.corr()
data = pd.DataFrame(data)

# my_sum_0 = get_average('credit.policy', 0, 'int.rate')
# my_sum_1 = get_average('credit.policy', 1, 'int.rate')
# print((my_sum_0 * 100), my_sum_1 * 100)
#
# purpose = data['purpose'].value_counts().reset_index()
# pup_list = list(purpose['purpose'])
# print(pup_list[0])
#
# int_rate = data['int.rate'].value_counts().reset_index()
# int_list = list(int_rate['int.rate'])
# print(int_list)

