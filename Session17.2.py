# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:15:52 2018

@author: avatash.rathore
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math


Number_of_question= 50
P_right_Answer =1/5
p_wrong_answer = 4/5
K =5
Number_of_WrongQ = Number_of_question -K

print("""Using Binomial Formula:-C (n, k) = n!/(k!(n−k)!)""")

P = (math.factorial(Number_of_question)/(math.factorial(K)*math.factorial(Number_of_WrongQ))) * ((math.pow(P_right_Answer,K))* (math.pow(p_wrong_answer,Number_of_WrongQ)))
print("Original probablity for exact 5 'D':",P)
print("Probablity using built in func",stats.binom.pmf(5,50,1/5))

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = stats.binom.stats(Number_of_question, P, moments='mvsk')

x = np.arange(stats.binom.ppf(0.01,Number_of_question, P),
              stats.binom.ppf(0.99, Number_of_question, P))
ax.plot(x, stats.binom.pmf(x, Number_of_question, P), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, stats.binom.pmf(x,Number_of_question, P), colors='b', lw=5, alpha=0.5)
rv = stats.binom(Number_of_question, P)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
         label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()
