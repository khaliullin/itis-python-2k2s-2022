# 1 - Without Join():
import threading
import time


def loiter():
    print('You are loitering!')
    time.sleep(3)
    print('You are not loitering anymore!')


t1 = threading.Thread(target=loiter)
t1.start()
print('Hey, I do not want to loiter!')
'''
Output without join()--> 
You are loitering!
Hey, I do not want to loiter!
You are not loitering anymore! #After 5 seconds --> This statement will be printed

'''