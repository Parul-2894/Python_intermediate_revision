"""
 Process don't have the same memory space, becasue f which they need special shared memory object
 to share data . 

 So we can use Value, Array

 We can also use queues
"""
from multiprocessing import Process, Value, Array, Lock
import os 
import time

processes = []

num_processes = os.cpu_count()


def add_100(number, lock):
    with lock:
        for i in range(100):
            time.sleep(0.01)
            number.value +=1



if __name__ == '__main__':  
    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at the beginning is', shared_number.value)
  
    p1 = Process(target=add_100, args=(shared_number, lock,))
    p2 = Process(target=add_100, args=(shared_number, lock,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at the end', shared_number.value)


    # start
    for p in processes:
        p.start()

    for p in processes:
        p.join()  #  The join() method is used to block the main process (i.e., the script that initiated the new process) until the target process completes its execution. This is useful for synchronizing processes and ensuring that the main process waits for all child processes to finish before continuing.

    #without join the main process can complete without the completion of the join process. 
    print("All are done")