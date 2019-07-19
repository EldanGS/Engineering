"""
Эта задачка чуть сложней предыдущей и потребует от вас размышлений. Мы будем рисовать лестницу.

На вход ваша программа будет получать количество ступенек.


import sys
num_steps = int(sys.argv[1])
Ваша цель напечатать на экран лесенку используя символы пробела " " и решетки "#". Например, для входного параметра (количества ступенек) 4 лесенка должна выглядеть следующим образом:


   #
  ##
 ###
####
Конечно, мы будем подавать на вход вашей программе разное количество ступенек.
How to submit
When you're ready to submit, you can upload files for each part of the assignment on the "My submission" tab.

"""

import sys

num_steps = int(sys.argv[1])

for step in range(1, num_steps + 1):
	print(' ' * (num_steps - step) + '#' * step)

