"""
A pool in multiprocess contains a pool of processes t wich jobs can be submitted. 
It can manage the process for you and split data as chunks of data. 

"""

from multiprocessing import Pool
import time

def cube(number):
    time.sleep(1)
    return number*number*number


if __name__ == '__main__':
  
    numbers = range(1000)
    pool = Pool()
    #for imp methods, map, apply, join and close

    result = pool.map(cube, numbers)
    #Automatically allocates the maximum number of process available for you
    #Creates as many process and cores in your macine and split the iterable
    #into multiple chunks and given to the process function for parallel execution.
    pool.close()
    pool.join()
    print(result)
