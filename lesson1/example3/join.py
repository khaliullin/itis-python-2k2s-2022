# 2 - With Join():
import threading
import time


def loiter():
    print('You are loitering!')
    time.sleep(3)
    print('You are not loitering anymore!')


t1 = threading.Thread(target=loiter)
t1.start()
t1.join()
print('Hey, I do not want to loiter!')

'''
Output with join() -->
You are loitering!
You are not loitering anymore! #After 5 seconds --> This statement will be printed
Hey, I do not want to loiter! 

'''
