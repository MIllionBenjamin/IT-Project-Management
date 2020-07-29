import numpy as np
import matplotlib.pyplot as plt
import random

THROW_TIMES = 30000


dice_1 = np.random.randint(low = 1, high = 7.5, size = THROW_TIMES, dtype = int)
dice_2 = np.random.randint(low = 1, high = 7.5, size = THROW_TIMES, dtype = int)
each_throw_sum = dice_1 + dice_2

'''
each_throw_sum = []
for i in range(0, THROW_TIMES):
    each_throw_sum.append(random.randint(1,6) + random.randint(1,6))
'''

y = [0] * 11
for sum_value in each_throw_sum:
    y[sum_value - 2] += 1
#plt.hist(each_throw_sum, align="left",edgecolor="black",density = True)
plt.bar([i for i in range(2, 13)], y)
plt.xticks(np.arange(1, 14, 1))
plt.xlabel("Each Throw Sum")
plt.ylabel("Times")
plt.title("Throw Two Dices " + str(THROW_TIMES) + " Times")
plt.show()