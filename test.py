#1,1,-1,0,-1,0,0,-1,0
import time

start_time = time.time()
from Train_TicTacToe_NW import *

# use_neural_network([[   1,0,0,
#                         -1,1,0,
#                         0,-1,-1 ]])


# mydict = {"hi": "hello"}
# if 'hi' in mydict:
#     print(mydict['hi'])
# print("--- %s seconds ---" % (time.time() - start_time))

t = 0
f = 0
for i in range(1000):
    if random.choice([False,True,False,False,False]):
        t += 1
    else:
        f += 1
print(t,f)
