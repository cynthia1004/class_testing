#Convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]
#method 1:
import collections
from itertools import chain
a = [i if isinstance(i, collections.Iterable) else [i,] for i in start_list]
new_list = list(chain.from_iterable(a))
print(new_list)
divisor = 2
result = [x//divisor for x in new_list]
print(result)
my_set = set(result)
print(my_set)

#method 2:
answer = [int(item/2) for sublist in start_list for item in sublist if item % 2 == 0]
for sublist in start_list:
    for item in sublist:
        print(answer)

#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}
date_format = '%m/%d/%Y'
new_dict = {k.capitalize():datetime.datetime.strptime(v, date_format) for k, v in start_dict.items()}
print(new_dict)

