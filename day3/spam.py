#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:49:43 2018

@author: julianchan
"""

email = "Hellow how are you?"
email2 = "CHEAP ROLEX WATCHES FOR SALE!"
if 'how' in email:
    print('Not a spam')
elif 'rolex' in email.lower():
    print('SPAM!!!')
elif 'cheap' in email.lower():
    print('SPAM!!!')
elif email.count('money')>5:
    print('SPAM!!!')

spam_word = []
non_spam_words = []

spam_word = ['rolex','cheap','viagra']
non_spam_words = ['hello','cats', 'dogs']
##NEW example

import random

x = list(range(20))
y = [3 * xx + 2 + 10*random.random() for xx in x]

plt.plot(x, y, 'bo')
plt.show()
