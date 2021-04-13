'''
Trying to spot humans using the Wald--Wolfowitz runs test
'''
import matplotlib.pyplot as plt
import pandas
import math
from pandas.plotting import parallel_coordinates

data = open("data.txt", "r").read().splitlines()

row = 1
for sequence in data:
    num_attempts = len(sequence)
    num_zeros = sequence.count('0')
    num_ones = num_attempts - num_zeros

    # Find the expected number of runs and the variance
    mean_num_runs = 2 * num_zeros * num_ones / num_attempts + 1
    variance_num_runs = (mean_num_runs - 1) * \
        (mean_num_runs - 2) / (num_attempts - 1)

    # Find the actual number of runs
    num_runs = 1
    last_symbol = sequence[0]
    for symbol in sequence[1:]:
        if not symbol == last_symbol:
            num_runs += 1
            last_symbol = symbol

    # print(mean_num_runs, variance_num_runs, num_runs)
    error = (num_runs - mean_num_runs) / math.sqrt(variance_num_runs)
    # plt.scatter(error, num_zeros / num_attempts)
    plt.scatter(error, 1)
    plt.xlabel('Runs error')
    # pc_data = pandas.DataFrame([num_runs, num_ones])
    pc_data = pandas.DataFrame(
        {'num_runs': [num_runs], 'num_ones': [num_ones], 'num_zeros': [num_zeros], 'error': [error], 'dummy': [0]})
    # print(pc_data)

    # parallel_coordinates(pc_data, 'dummy')

    if abs(error) > 3:
        print(error, row)

    row += 1

plt.show()
