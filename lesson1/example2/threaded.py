import threading

fp = open('f', 'w')


def work1():
    for x in range(10000):
        fp.write('1')


def work2():
    for x in range(10000):
        fp.write('2')


t1 = threading.Thread(target=work1)
t1.daemon = True
t2 = threading.Thread(target=work2)
t2.daemon = True

t1.start()
t2.start()
# t1.join()
# t2.join()


# import threading
# lock = threading.Lock()
#
# fp = open('f', 'w')
#
#
# def work1():
#     with lock:
#         for x in range(10000):
#             fp.write('1')
#
#
# def work2():
#     with lock:
#         for x in range(10000):
#             fp.write('2')
#
#
# t1 = threading.Thread(target=work1)
# t1.daemon = True
# t2 = threading.Thread(target=work2)
# t2.daemon = True
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
