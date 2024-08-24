from threading import Thread
import time
database_value = 0


def increase():
    global database_value
    local_copy = database_value

    local_copy += 1
    
    time.sleep(0.1)

    database_value = local_copy

if __name__ == '__main__':
    print('start_value', database_value)

    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('End Value', database_value)
    print('end_main')
"""
 When yu run it you will see the the last value of the database_value variable is 1
it is happening because of a Race Condition.
A race condition happens when two or more threads try to access the
same variable.
to preven his we use lock object. 
Check threading_using_lock.py

"""

